"""Local educational claims-triage harness with synthetic evidence."""
import json
import sqlite3
from argparse import ArgumentParser
from collections.abc import Callable
from contextlib import closing
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Policy:
    id: str
    effective: str
    documents: frozenset[str]


POLICIES = (
    Policy("delay-v1", "2025-01-01", frozenset({"carrier_notice"})),
    Policy("delay-v2", "2026-01-01", frozenset({"carrier_notice", "itinerary"})),
)


@dataclass(frozen=True)
class Claim:
    id: str
    incident_date: str
    category: str
    documents: tuple[str, ...]


@dataclass(frozen=True)
class Proposal:
    id: str
    route: str
    policy: str | None
    missing: tuple[str, ...] = ()


def read_policy(claim: Claim) -> Policy | None:
    if claim.category != "delay":
        return None
    return max((policy for policy in POLICIES if policy.effective <= claim.incident_date),
               key=lambda policy: policy.effective, default=None)


PolicyLookup = Callable[[Claim], Policy | None]


def propose(claim: Claim, lookup: PolicyLookup = read_policy) -> Proposal:
    """One tool call. Return a routing proposal with no side effects."""
    try:
        policy = lookup(claim)
    except TimeoutError:
        return Proposal(claim.id, "paused", None)
    if policy is None:
        return Proposal(claim.id, "manual_review", None)
    missing = tuple(sorted(policy.documents - set(claim.documents)))
    return Proposal(claim.id, "request_documents" if missing else "adjuster_review", policy.id, missing)


def checkpoint(connection: sqlite3.Connection, proposal: Proposal) -> int:
    payload = json.dumps(asdict(proposal), sort_keys=True)
    with connection:
        row = connection.execute("""
            INSERT INTO proposal VALUES (?, 1, ?)
            ON CONFLICT (id) DO UPDATE SET revision = revision + 1, payload = excluded.payload
            WHERE proposal.payload <> excluded.payload
            RETURNING revision
        """, (proposal.id, payload)).fetchone()
        if row is None:
            row = connection.execute("SELECT revision FROM proposal WHERE id = ?", (proposal.id,)).fetchone()
    return row[0]


def open_store(path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.executescript("""
        CREATE TABLE IF NOT EXISTS proposal (
            id TEXT PRIMARY KEY, revision INTEGER NOT NULL, payload TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS approved_note (
            id TEXT NOT NULL, revision INTEGER NOT NULL, payload TEXT NOT NULL,
            PRIMARY KEY (id, revision)
        );
    """)
    return connection


def approve(connection: sqlite3.Connection, claim_id: str, revision: int, role: str) -> str:
    """Persist one local note for the exact reviewed revision."""
    if role != "reviewer":
        return "forbidden"
    connection.execute("BEGIN IMMEDIATE")
    with connection:
        row = connection.execute(
            "SELECT payload FROM proposal WHERE id = ? AND revision = ?", (claim_id, revision)
        ).fetchone()
        if row is None:
            return "stale or unknown"
        if json.loads(row[0])["route"] == "paused":
            return "paused"
        inserted = connection.execute("""
            INSERT INTO approved_note VALUES (?, ?, ?)
            ON CONFLICT (id, revision) DO NOTHING
        """, (claim_id, revision, row[0]))
        return "recorded" if inserted.rowcount else "replay ignored"


def unavailable(_claim):
    raise TimeoutError("fixture policy service timeout")


# Keep these expectations fixed while comparing candidate and baseline.
CASES = (
    (Claim("historical", "2025-07-01", "delay", ("carrier_notice",)), "adjuster_review", "delay-v1", (), False),
    (Claim("current", "2026-04-01", "delay", ("carrier_notice",)), "request_documents", "delay-v2", ("itinerary",), True),
    (Claim("complete", "2026-04-01", "delay", ("carrier_notice", "itinerary")), "adjuster_review", "delay-v2", (), False),
    (Claim("unsupported", "2026-04-01", "baggage", ()), "manual_review", None, (), True),
    (Claim("before", "2024-04-01", "delay", ()), "manual_review", None, (), True),
    (Claim("outage", "2026-04-01", "delay", ()), "paused", None, (), True),
)


def manual_baseline(claim: Claim, _lookup: PolicyLookup) -> Proposal:
    return Proposal(claim.id, "manual_review", None)


def evaluate(candidate: Callable[[Claim, PolicyLookup], Proposal]) -> dict:
    rows = []
    for claim, expected_route, expected_policy, expected_missing, critical in CASES:
        lookup = unavailable if claim.id == "outage" else read_policy
        actual = candidate(claim, lookup)
        checks = (actual.route == expected_route, actual.policy == expected_policy, actual.missing == expected_missing)
        rows.append({"id": claim.id, "critical": critical, "route": checks[0], "source": checks[1],
                     "documents": checks[2], "pass": all(checks), "observed": asdict(actual)})
    critical_results = [row["pass"] for row in rows if row["critical"]]
    return {"passed": sum(row["pass"] for row in rows), "total": len(rows), "cases": rows,
            "critical_pass": bool(critical_results) and all(critical_results)}


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", default="demo", choices=("demo", "eval"))
    parser.add_argument("--db", default=":memory:", help="SQLite file for the demo, defaults to an in-memory store")
    args = parser.parse_args()
    if args.mode == "eval":
        baseline, candidate = evaluate(manual_baseline), evaluate(propose)
        gate = candidate["critical_pass"] and candidate["passed"] >= baseline["passed"]
        print(json.dumps({"baseline": baseline, "candidate": candidate, "gate": gate}, indent=2))
        return 0 if gate else 1

    claim = CASES[1][0]
    proposal = propose(claim)
    with closing(open_store(args.db)) as connection:
        revision = checkpoint(connection, proposal)
        print(json.dumps({"proposal": asdict(proposal), "revision": revision,
                          "status": "awaiting reviewer approval"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
