# UnderCover-inspired claims harness

Run from the AIeBOK repository root. The demo proposes a review step using fictional policy data. The eval compares routing, source selection, and required documentation against fixed cases.

```sh
python labs/undercover-harness/main.py demo
python labs/undercover-harness/main.py eval
python -m pytest labs/undercover-harness/test_lab.py -q
```

SQLite 3.35+ is required for `RETURNING`. The approval test reopens a database across calls, rejects stale and unauthorized approvals, and records a single local note when approval is replayed. No real claims, hosted models, settlements, or messages are involved.
