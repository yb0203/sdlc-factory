"""
Unit tests for Git-Native SDLC Manager
"""

import pytest
from sdlc_factory.git_native import GitNativeManager


def test_git_native_activity_notes():
    git_mgr = GitNativeManager()
    # Test reading notes from HEAD commit
    head_hash = git_mgr._run_git(["rev-parse", "HEAD"])
    assert len(head_hash) == 40

    activity_data = {
        "actor": "architect-agent",
        "thought": "Z3 SMT solver proved invariant fineCents >= 0",
        "status": "PASSED",
    }
    git_mgr.append_activity_note(head_hash, activity_data)
    read_data = git_mgr.read_activity_notes(head_hash)

    assert read_data is not None
    assert read_data["actor"] == "architect-agent"
    assert read_data["status"] == "PASSED"
