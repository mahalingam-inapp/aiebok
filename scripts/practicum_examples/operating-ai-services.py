import json
from time import perf_counter
from uuid import uuid4
from wsgiref.util import setup_testing_defaults


def answer(version, question):
    if version == "v2" and question == "special request":
        raise TimeoutError("candidate timed out")
    return "Use the reservation form." if question == "reserve a room" else "Send to the service desk."


class Service:
    def __init__(self, store=None):
        self.store = store

    def __call__(self, environ, start_response):
        path = environ["PATH_INFO"]
        if path == "/health":
            status, result = "200 OK", {"ready": True}
        elif path == "/predict" and environ["REQUEST_METHOD"] == "POST":
            status, result = self.predict(environ)
        else:
            status, result = "404 Not Found", {"error": "unknown endpoint"}
        body = json.dumps(result).encode()
        start_response(status, [("Content-Type", "application/json"), ("Content-Length", str(len(body)))])
        return [body]

    def predict(self, environ):
        try:
            size = int(environ.get("CONTENT_LENGTH") or "0")
            if not 0 < size <= 4096:
                raise ValueError("invalid length")
            payload = json.loads(environ["wsgi.input"].read(size))
            question = payload.get("question") if isinstance(payload, dict) else None
            if not isinstance(question, str) or not question.strip():
                raise ValueError("missing question")
        except (ValueError, UnicodeError):
            return "400 Bad Request", {"error": "invalid question"}

        canary = environ.get("HTTP_X_AIEBOK_CANARY") == "1"
        requested = self.store.active_version(canary=canary) if self.store else "v1"
        served = requested
        start = perf_counter()
        try:
            result = answer(served, question)
        except TimeoutError:
            served = "v1"
            result = answer(served, question)
        request_id = uuid4().hex
        if self.store:
            self.store.record(request_id, requested, served, (perf_counter() - start) * 1000)
        return "200 OK", {"id": request_id, "requested_version": requested, "served_version": served, "answer": result}


def request(app, path, data=None, *, canary=False):
    from io import BytesIO

    environ = {}
    setup_testing_defaults(environ)
    environ["PATH_INFO"] = path
    if canary:
        environ["HTTP_X_AIEBOK_CANARY"] = "1"
    if data is not None:
        body = json.dumps(data).encode()
        environ.update({"REQUEST_METHOD": "POST", "CONTENT_LENGTH": str(len(body)), "wsgi.input": BytesIO(body)})
    status = []
    payload = b"".join(app(environ, lambda value, headers: status.append(value)))
    return status[0], json.loads(payload)


assert request(Service(), "/health") == ("200 OK", {"ready": True})
status, result = request(Service(), "/predict", {"question": "reserve a room"})
assert status == "200 OK" and result["served_version"] == "v1"
assert request(Service(), "/predict", {"question": ""})[0] == "400 Bad Request"

# %%
import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory


class Store:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        with self.conn:
            self.conn.executescript("""
                CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY, version TEXT NOT NULL, canary TEXT);
                INSERT OR IGNORE INTO config VALUES (1, 'v1', NULL);
                CREATE TABLE IF NOT EXISTS traces (
                    id TEXT PRIMARY KEY, requested TEXT, served TEXT, elapsed_ms REAL, fallback INTEGER
                );
                CREATE TABLE IF NOT EXISTS decisions (version TEXT, reason TEXT);
            """)

    def active_version(self, *, canary=False):
        version, candidate = self.conn.execute("SELECT version, canary FROM config WHERE id = 1").fetchone()
        return candidate if canary and candidate else version

    def record(self, request_id, requested, served, elapsed_ms):
        with self.conn:
            self.conn.execute("INSERT INTO traces VALUES (?, ?, ?, ?, ?)",
                              (request_id, requested, served, elapsed_ms, int(served != requested)))

    def activate(self, version, reason):
        if version not in {"v1", "v2"}:
            raise ValueError("unknown version")
        with self.conn:
            self.conn.execute("UPDATE config SET version = ?, canary = NULL WHERE id = 1", (version,))
            self.conn.execute("INSERT INTO decisions VALUES (?, ?)", (version, reason))

    def stage(self, version, reason):
        if version not in {"v1", "v2"}:
            raise ValueError("unknown version")
        with self.conn:
            self.conn.execute("UPDATE config SET canary = ? WHERE id = 1", (version,))
            self.conn.execute("INSERT INTO decisions VALUES (?, ?)", (version, reason))


directory = TemporaryDirectory(prefix="aiebok-service-")
database = Path(directory.name) / "release.sqlite"
store = Store(database)
store.stage("v2", "start synthetic canary")
service = Service(store)
status, stable = request(service, "/predict", {"question": "special request"})
assert status == "200 OK" and stable["requested_version"] == "v1"
status, response = request(service, "/predict", {"question": "special request"}, canary=True)
assert status == "200 OK" and response["served_version"] == "v1"
trace = store.conn.execute("SELECT requested, served, fallback FROM traces WHERE id = ?", (response["id"],)).fetchone()
assert trace == ("v2", "v1", 1)
assert "question" not in {column[1] for column in store.conn.execute("PRAGMA table_info(traces)")}

# %%
def gate(store, version, minimum=4, max_fallback_rate=0.2, p95_limit_ms=1000):
    rows = store.conn.execute(
        "SELECT elapsed_ms, fallback FROM traces WHERE requested = ? ORDER BY elapsed_ms", (version,)
    ).fetchall()
    if len(rows) < minimum:
        return False, f"insufficient sample ({len(rows)}/{minimum})"
    rate = sum(fallback for _, fallback in rows) / len(rows)
    from math import ceil
    p95 = rows[ceil(0.95 * len(rows)) - 1][0]
    return rate <= max_fallback_rate and p95 <= p95_limit_ms, f"fallback rate {rate:.1%}, p95 {p95:.2f} ms"


assert gate(store, "v2")[1].startswith("insufficient sample")
for question in ("special request", "reserve a room", "reserve a room"):
    request(service, "/predict", {"question": question}, canary=True)
passed, reason = gate(store, "v2")
assert not passed and "50.0%" in reason
for _ in range(3):
    request(service, "/predict", {"question": "reserve a room"})
assert gate(store, "v1")[0]
print("Canary", reason)

# %%
from urllib.request import Request, ProxyHandler, build_opener
from wsgiref.simple_server import make_server, WSGIRequestHandler


class QuietHandler(WSGIRequestHandler):
    def log_message(self, format, *args):
        pass


store.activate("v1", "rollback after blocked canary")
store.conn.close()
reopened = Store(database)
try:
    assert reopened.active_version() == "v1"
    assert reopened.active_version(canary=True) == "v1"
    assert ("v1", "rollback after blocked canary") in reopened.conn.execute("SELECT version, reason FROM decisions").fetchall()
    # The server runs in this thread because the SQLite connection belongs to it.
    from concurrent.futures import ThreadPoolExecutor

    with make_server("127.0.0.1", 0, Service(reopened), handler_class=QuietHandler) as server:
        server.timeout = 5
        address = f"http://127.0.0.1:{server.server_port}"

        def fetch():
            client = build_opener(ProxyHandler({}))
            with client.open(address + "/health", timeout=5) as response:
                assert json.load(response)["ready"]
            call = Request(address + "/predict", data=b'{"question":"reserve a room"}',
                           headers={"Content-Type": "application/json", "X-AIEBOK-CANARY": "1"})
            with client.open(call, timeout=5) as response:
                return json.load(response)

        with ThreadPoolExecutor(max_workers=1) as pool:
            result = pool.submit(fetch)
            server.handle_request()
            server.handle_request()
            assert result.result()["served_version"] == "v1"
finally:
    reopened.conn.close()
    directory.cleanup()
print("Rollback persisted and HTTP smoke passed")
