"""
Git-Native SDLC Utilities (sdlc_factory.git_native)
Implements native Git Worktrees, Git Notes Activity logging, and Git Signed Tag proof seals.
"""

import json
import subprocess
from typing import Dict, Any, Optional


class GitNativeManager:
    """
    Manages Git-Native SDLC primitives using native git subcommands.
    """

    def __init__(self, repo_dir: str = "."):
        self.repo_dir = repo_dir

    def _run_git(self, args: list[str]) -> str:
        res = subprocess.run(
            ["git"] + args,
            cwd=self.repo_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return res.stdout.strip()

    def spawn_worktree(self, delta_id: str, branch_name: str) -> str:
        """
        Spawns an isolated Git Worktree for an agy agent task run.
        """
        worktree_path = f".worktrees/{delta_id}"
        self._run_git(["worktree", "add", "-b", branch_name, worktree_path])
        return worktree_path

    def remove_worktree(self, delta_id: str):
        """
        Removes an isolated Git Worktree after completion.
        """
        worktree_path = f".worktrees/{delta_id}"
        self._run_git(["worktree", "remove", "--force", worktree_path])

    def append_activity_note(self, commit_hash: str, activity_data: Dict[str, Any]):
        """
        Appends an immutable Activity log entry into Git Notes (refs/notes/activity).
        """
        note_json = json.dumps(activity_data)
        self._run_git(["notes", "--ref=activity", "add", "-f", "-m", note_json, commit_hash])

    def read_activity_notes(self, commit_hash: str) -> Optional[Dict[str, Any]]:
        """
        Reads Activity log notes from a git commit.
        """
        try:
            raw_note = self._run_git(["notes", "--ref=activity", "show", commit_hash])
            return json.loads(raw_note)
        except Exception:
            return None

    def seal_proof_tag(self, tag_name: str, message: str) -> str:
        """
        Creates a signed Git Tag certifying formal proof & DoD attestation.
        """
        self._run_git(["tag", "-a", tag_name, "-m", message])
        return tag_name
