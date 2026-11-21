import json
import subprocess
import sys

# Minimal local MCP server fixture. Each line of stdout is a protocol message.
server = """
import json
import sys

for line in sys.stdin:
    message = json.loads(line)
    method = message["method"]
    if method == "notifications/initialized":
        continue
    reply = {"jsonrpc": "2.0", "id": message["id"]}
    if method == "initialize":
        reply["result"] = {
            "protocolVersion": "2025-06-18",
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "agenda-fixture", "version": "1.0"},
        }
    elif method == "tools/list":
        reply["result"] = {"tools": [{
            "name": "lookup_agenda",
            "description": "Read the local synthetic review agenda.",
            "inputSchema": {
                "type": "object", "properties": {"meeting": {"type": "string", "enum": ["M1"]}},
                "required": ["meeting"], "additionalProperties": False,
            },
        }]}
    elif method == "tools/call":
        params = message["params"]
        if params.get("name") == "lookup_agenda" and params.get("arguments") == {"meeting": "M1"}:
            reply["result"] = {"content": [{"type": "text", "text": "Review the accessibility checklist."}]}
        else:
            reply["error"] = {"code": -32602, "message": "Invalid tool or arguments"}
    else:
        reply["error"] = {"code": -32601, "message": "Method not found"}
    print(json.dumps(reply), flush=True)
"""


def exchange(method, params=None):
    messages = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": "2025-06-18", "capabilities": {},
            "clientInfo": {"name": "aiebok-workbook", "version": "1.0"},
        }},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": method, "params": params or {}},
    ]
    run = subprocess.run(
        [sys.executable, "-c", server], input="".join(json.dumps(msg) + "\n" for msg in messages),
        text=True, capture_output=True, timeout=5, check=True,
    )
    init, reply = [json.loads(line) for line in run.stdout.splitlines()]
    assert init["id"] == 1 and init["result"]["protocolVersion"] == "2025-06-18"
    assert reply["id"] == 2 and reply["jsonrpc"] == "2.0"
    return reply["result"]


tools = exchange("tools/list")["tools"]
assert [tool["name"] for tool in tools] == ["lookup_agenda"]
assert tools[0]["inputSchema"]["required"] == ["meeting"]
print("Discovered", tools)

# %%
events = []


def lookup(role, meeting):
    if role != "reviewer":
        events.append("denied")
        return None
    if meeting != "M1":
        events.append("invalid_arguments")
        return None
    result = exchange("tools/call", {"name": "lookup_agenda", "arguments": {"meeting": meeting}})
    events.append("read")
    return result["content"][0]["text"]


assert lookup("guest", "M1") is None
assert lookup("reviewer", "M9") is None
assert lookup("reviewer", "M1") == "Review the accessibility checklist."
assert events == ["denied", "invalid_arguments", "read"]

# %%
from hashlib import sha256
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory


def open_store(path):
    db = sqlite3.connect(path)
    db.executescript("""
        CREATE TABLE IF NOT EXISTS proposals (
          id TEXT PRIMARY KEY, payload TEXT NOT NULL, digest TEXT NOT NULL, approved INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS notes (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
    """)
    return db


def propose(db, identifier, payload):
    digest = sha256(payload.encode()).hexdigest()
    with db:
        db.execute("INSERT INTO proposals VALUES (?, ?, ?, 0)", (identifier, payload, digest))
    return digest


def approve(db, identifier, digest):
    with db:
        return db.execute("UPDATE proposals SET approved = 1 WHERE id = ? AND digest = ?",
                          (identifier, digest)).rowcount == 1


directory = TemporaryDirectory(prefix="aiebok-review-")
database = Path(directory.name) / "review.sqlite"
db = open_store(database)
digest = propose(db, "proposal-1", "M1 has completed accessibility review")
db.close()
db = open_store(database)
assert db.execute("SELECT approved FROM proposals").fetchone() == (0,)
assert not approve(db, "proposal-1", "different-payload")
assert db.execute("SELECT approved FROM proposals").fetchone() == (0,)

# %%
def execute(db, identifier):
    with db:
        db.execute("BEGIN IMMEDIATE")
        row = db.execute("SELECT payload, approved FROM proposals WHERE id = ?", (identifier,)).fetchone()
        if row is None or not row[1]:
            return "awaiting_approval"
        effect = db.execute("INSERT OR IGNORE INTO notes VALUES (?, ?)", (identifier, row[0]))
        return "completed" if effect.rowcount else "replayed"


assert execute(db, "proposal-1") == "awaiting_approval"
assert approve(db, "proposal-1", digest)
assert execute(db, "proposal-1") == "completed"
db.close()
db = open_store(database)
try:
    assert execute(db, "proposal-1") == "replayed"
    assert db.execute("SELECT count(*) FROM notes").fetchone() == (1,)
    print("Decision trace", events + ["awaiting_approval", "approved", "completed", "replayed"])
finally:
    db.close()
    directory.cleanup()
