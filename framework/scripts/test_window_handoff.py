#!/usr/bin/env python3
"""Regressions for `window_handoff.py`: a fixture repository, a fake agents view, no tmux, no model, no live session."""
import contextlib
import hashlib
import io
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import window_handoff as wh

OLD, NEW = "11111111-aaaa-4bbb-8ccc-000000000001", "22222222-aaaa-4bbb-8ccc-000000000002"


def sessions(old_name="HE - CURRENT 11111111", new_name="he_o_20260101"):
    return [{"sessionId": "99999999-0000", "name": "HE - PREVIOUS 99999999", "state": "done"},
            {"sessionId": OLD, "name": old_name, "state": "done"},
            {"sessionId": NEW, "name": new_name, "state": "busy"}]


class FakeView:
    """The agents view as the rename sees it: a pointer that wraps, a rename mode, a name column that cuts long names."""

    def __init__(self, listing, hint=True, mangle=False, summaries=None, resort=False, saves_elsewhere=None):
        self.listing, self.at, self.editing, self.buffer = listing, 0, False, ""
        self.hint, self.mangle, self.keys = hint, mangle, []
        self.summaries, self.resort, self.saves_elsewhere = summaries or {}, resort, saves_elsewhere

    def __call__(self, root):
        return self

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.editing = False

    def screen(self):
        lines = ["  Completed"]
        for n, s in enumerate(self.listing):
            name = self.buffer if self.editing and n == self.at else s["name"]
            shown = name if len(name) <= 24 else "…" + name[-23:]
            lines.append(f"{wh.POINTER if n == self.at else ' '} ✻ {shown}   {self.summaries.get(s['sessionId'], 'some summary')}")
        if self.editing and self.hint:
            lines.append("  enter to save · esc to cancel")
        return "\n".join(lines)

    def key(self, key):
        self.keys.append(key)
        if key == "Down":
            self.at = (self.at + 1) % len(self.listing)
        elif key == "C-r":
            self.editing, self.buffer = True, self.listing[self.at]["name"]
        elif key == "C-k":
            self.buffer = ""
        elif key == "Escape":
            self.editing = False
        elif key == "Enter" and self.editing:
            target = self.at if self.saves_elsewhere is None else self.saves_elsewhere
            self.listing[target]["name"], self.editing = self.buffer, False
            if self.resort:                  # the view moves the row just saved to the top
                self.listing.insert(0, self.listing.pop(target))
                self.at = 0

    def type(self, text):
        self.buffer += text[:-1] if self.mangle else text


def rename_args(**kw):
    return SimpleNamespace(**{"role": "HE", "old": OLD[:8], "new": NEW[:8], "task": "T", "dry_run": False, "settle": 0, **kw})


STATES = {OLD: "RELEASED", NEW: "BOUND"}


def do_rename(listing, view, args=None, states=STATES):
    said = []
    wh.rename(args or rename_args(), Path("."), say=said.append, listing=lambda: [dict(s) for s in listing],
              view_factory=view, state=states.get)
    return said


class Rename(unittest.TestCase):
    def test_demotes_before_promoting_and_proves_each_by_the_listing(self):
        listing = sessions()
        said = do_rename(listing, FakeView(listing))
        self.assertEqual([s["name"] for s in listing][1:], ["HE - PREVIOUS 11111111", "HE - CURRENT 22222222"])
        proofs = [line for line in said if line.startswith("proof")]
        self.assertTrue(proofs[0].startswith("proof demote") and proofs[0].endswith("OK"), proofs)
        self.assertTrue(proofs[1].startswith("proof promote") and proofs[1].endswith("OK"), proofs)

    def test_a_summary_naming_the_successor_is_not_its_row_after_a_re_sort(self):
        # 2026-11-25: the demoted row moved first and its summary said "successor <temporary name> launched".
        listing = sessions()
        view = FakeView(listing, resort=True, summaries={OLD: "successor he_o_20260101 launched; writing release"})
        do_rename(listing, view)
        self.assertEqual({s["sessionId"]: s["name"] for s in listing}[OLD], "HE - PREVIOUS 11111111")
        self.assertEqual({s["sessionId"]: s["name"] for s in listing}[NEW], "HE - CURRENT 22222222")

    def test_only_the_name_column_of_a_captured_row_counts(self):
        captured = "  ✻ HE - PREVIOUS 70b134a9               successor he_o_20261125 launched; verifying        2h"
        new_row = "❯ * he_o_20261125                        HE bind checks and reading addenda                 4m"
        self.assertFalse(wh.shows(captured, "he_o_20261125"))
        self.assertTrue(wh.shows(new_row, "he_o_20261125"))
        self.assertTrue(wh.shows(captured, "HE - PREVIOUS 70b134a9"))
        self.assertFalse(wh.shows("  ∙ SCI - PREVIOUS ff316249   released", "SCI"))
        self.assertTrue(wh.shows("  ∙ SCI                         released", "SCI"))
        self.assertTrue(wh.shows("  ∙ …strator - CURRENT 11111111   x", "IT Orchestrator - CURRENT 11111111"))
        self.assertFalse(wh.shows("❯ describe a task for a new session", "a task for a new session"))

    def test_another_row_changing_name_is_reported_and_stops_the_run(self):
        listing = sessions()
        with self.assertRaises(wh.Refused) as why:
            do_rename(listing, FakeView(listing, saves_elsewhere=0))
        self.assertIn("ANOTHER ROW CHANGED NAME", str(why.exception))
        self.assertEqual(listing[2]["name"], "he_o_20260101")

    def test_a_long_name_cut_by_the_column_is_still_matched(self):
        listing = sessions(old_name="IT Orchestrator - CURRENT 11111111", new_name="it_17_20260101")
        do_rename(listing, FakeView(listing), rename_args(role="IT Orchestrator"))
        self.assertEqual(listing[1]["name"], "IT Orchestrator - PREVIOUS 11111111")
        self.assertEqual(listing[2]["name"], "IT Orchestrator - CURRENT 22222222")

    def test_nothing_is_renamed_before_release_and_bind(self):
        for states in ({OLD: "BOUND", NEW: "BOUND"}, {OLD: "RELEASED", NEW: "NEVER_BOUND"}):
            listing = sessions()
            view = FakeView(listing)
            with self.assertRaises(wh.Refused):
                do_rename(listing, view, states=states)
            self.assertEqual(view.keys, [])
            self.assertEqual(listing, sessions())

    def test_a_wrong_screen_saves_nothing_and_stops_before_promotion(self):
        for broken in ({"hint": False}, {"mangle": True}):
            listing = sessions()
            view = FakeView(listing, **broken)
            with self.assertRaises(wh.Refused):
                do_rename(listing, view)
            self.assertNotIn("Enter", view.keys)
            self.assertEqual(listing, sessions())

    def test_a_save_the_listing_does_not_show_stops_the_run(self):
        listing = sessions()
        frozen = [dict(s) for s in listing]
        said = []
        with self.assertRaises(wh.Refused):
            wh.rename(rename_args(), Path("."), say=said.append, listing=lambda: [dict(s) for s in frozen],
                      view_factory=FakeView(listing), state=STATES.get)
        self.assertTrue(any("NOT AS PLANNED" in line for line in said))
        self.assertEqual(listing[2]["name"], "he_o_20260101")

    def test_a_third_current_window_or_an_ambiguous_row_refuses(self):
        listing = sessions() + [{"sessionId": "33333333-0000", "name": "HE - CURRENT 33333333"}]
        with self.assertRaises(wh.Refused):
            do_rename(listing, FakeView(listing))
        twins = sessions() + [{"sessionId": "44444444-0000", "name": "he_o_20260101"}]
        with self.assertRaises(wh.Refused):
            do_rename(twins, FakeView(twins))

    def test_dry_run_and_an_already_done_step_touch_nothing(self):
        listing = sessions()
        view = FakeView(listing)
        said = do_rename(listing, view, rename_args(dry_run=True))
        self.assertEqual(view.keys, [])
        self.assertEqual(sum(line.startswith("plan") for line in said), 2)
        done = sessions(old_name="HE - PREVIOUS 11111111", new_name="HE - CURRENT 22222222")
        self.assertTrue(any("nothing to rename" in line for line in do_rename(done, FakeView(done))))


class Prepare(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "repo"
        self.root.mkdir()
        git = ["git", "-C", str(self.root), "-c", "user.name=t", "-c", "user.email=t@example.invalid"]
        subprocess.run(["git", "-C", str(self.root), "init", "-q", "-b", "main"], check=True)
        (self.root / "CKPT.md").write_text("checkpoint K\n", encoding="utf-8")
        subprocess.run([*git, "add", "CKPT.md"], check=True)
        subprocess.run([*git, "commit", "-q", "-m", "c"], check=True)
        subprocess.run([*git, "update-ref", "refs/remotes/development/main", "HEAD"], check=True)
        self.sha = hashlib.sha256(b"checkpoint K\n").hexdigest()
        self.template = Path(tmp.name) / "template.txt"
        self.out = Path(tmp.name) / "brief.txt"
        self.real_watch = wh.watch
        wh.watch = lambda root, *a: SimpleNamespace(stdout="BOUND (x)", returncode=1)
        self.addCleanup(setattr, wh, "watch", self.real_watch)

    def prepare(self, template, **kw):
        self.template.write_text(template, encoding="utf-8")
        args = SimpleNamespace(**{"remote": "development", "no_fetch": True, "set": [], "checkpoint": ["K=CKPT.md"],
                                  "old": OLD[:8], "task": "T", "worktree": "he_p_20260101", "template": str(self.template),
                                  "out": str(self.out), "model": "sonnet", "effort": "high", "autocompact": "400000", **kw})
        said = []
        wh.prepare(args, self.root, say=said.append, sessions=sessions())
        return "\n".join(said)

    GOOD = "read __CKPT_K__ sha256 __SHA_K__; old __OLD_SESSION__ ('__OLD_NAME__'), task __TASK__"

    def test_prints_each_value_and_the_commands_it_does_not_run(self):
        said = self.prepare(self.GOOD)
        self.assertIn(f"sha256 {self.sha}  working copy same", said)
        self.assertIn("old release    BOUND (exit 1", said)
        self.assertIn("TYPE THESE YOURSELF", said)
        self.assertIn("--bg --name he_p_20260101 --model sonnet --effort high", said)
        brief = self.out.read_text(encoding="utf-8")
        self.assertIn(self.sha, brief)
        self.assertIn(OLD, brief)
        self.assertFalse((self.root / ".claude").exists())

    def test_refusals_write_no_brief(self):
        cases = [(self.GOOD + " __CKPT_M__", {}), (self.GOOD + " " + "a" * 64, {}),
                 ("read __CKPT_K__; old __OLD_SESSION__", {}), ("read __SHA_K__", {}),
                 (self.GOOD, {"checkpoint": ["K=CKPT.md@" + "b" * 64]}), (self.GOOD, {"checkpoint": ["K=MISSING.md"]}),
                 (self.GOOD, {"checkpoint": []}), (self.GOOD, {"old": "deadbeef"}), (self.GOOD, {"worktree": "he_o_20260101"})]
        for template, extra in cases:
            with self.subTest(template=template, extra=extra), self.assertRaises(wh.Refused):
                self.prepare(template, **extra)
            self.assertFalse(self.out.exists())


class TheToolStartsAndRetiresNothing(unittest.TestCase):
    def test_every_claude_invocation_it_makes_is_the_agents_view_or_listing(self):
        source = Path(wh.__file__).read_text(encoding="utf-8")
        calls = [line.strip() for line in source.splitlines() if "claude_binary()" in line and "def " not in line]
        self.assertEqual(len(calls), 3, calls)
        self.assertTrue(all("agents" in line or "--bg --name" in line for line in calls), calls)
        self.assertIn('say(f"  cd', next(line for line in source.splitlines() if "--bg --name" in line and "say(" in line))
        self.assertNotIn('"--retire-old"', source)
        for word in ('"stop"', '"rm"', '"--bg"'):
            self.assertNotIn(word, source)

    def test_help_runs_and_names_the_three_commands(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as done:
            wh.main(["--help"])
        self.assertEqual(done.exception.code, 0)
        for command in ("prepare", "rename", "verify"):
            self.assertIn(command, out.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
