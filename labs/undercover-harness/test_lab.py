from contextlib import closing

from main import CASES, approve, checkpoint, evaluate, manual_baseline, open_store, propose, unavailable


def test_checkpoint_reopens_and_approval_replays_once(tmp_path):
    path = str(tmp_path / "claims.db")
    proposal = propose(CASES[1][0])
    with closing(open_store(path)) as first:
        revision = checkpoint(first, proposal)
        assert checkpoint(first, proposal) == revision
    with closing(open_store(path)) as resumed:
        assert approve(resumed, proposal.id, revision, "agent") == "forbidden"
        assert approve(resumed, proposal.id, revision, "reviewer") == "recorded"
    with closing(open_store(path)) as resumed:
        assert approve(resumed, proposal.id, revision, "reviewer") == "replay ignored"
        assert resumed.execute("SELECT count(*) FROM approved_note").fetchone()[0] == 1


def test_changed_proposal_invalidates_approval_and_pause_blocks_notes(tmp_path):
    path = str(tmp_path / "claims.db")
    claim = CASES[1][0]
    with closing(open_store(path)) as connection:
        revision = checkpoint(connection, propose(claim))
        paused = checkpoint(connection, propose(claim, unavailable))
        assert paused == revision + 1
        assert approve(connection, claim.id, revision, "reviewer") == "stale or unknown"
        assert approve(connection, claim.id, paused, "reviewer") == "paused"
        assert connection.execute("SELECT count(*) FROM approved_note").fetchone()[0] == 0


def test_candidate_passes_critical_fixtures_and_improves_baseline():
    baseline, candidate = evaluate(manual_baseline), evaluate(propose)
    assert baseline["passed"] == 2
    assert not baseline["critical_pass"]
    assert candidate["critical_pass"]
    assert candidate["passed"] == candidate["total"] == 6
