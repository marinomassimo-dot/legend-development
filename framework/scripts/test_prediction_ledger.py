#!/usr/bin/env python3
"""Tests for prediction_ledger.py on a scratch git repository (never the real checkout)."""
from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prediction_ledger as pl  # noqa: E402

MAIL = "t" + chr(64) + "scratch.invalid"  # built at run time: no literal address in the file
UNDER = "pkg"
RECEIPTS = "receipts.jsonl"


def run(root: Path, *args: str) -> str:
    done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True,
                          env={"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": MAIL,
                               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": MAIL,
                               "GIT_COMMITTER_DATE": "2026-11-16T08:00:00+00:00",
                               "PATH": "/usr/bin:/bin:/usr/local/bin", "HOME": str(root)})
    return done.stdout.strip()


def commit(root: Path, name: str, text: str, message: str, date: str) -> str:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    run(root, "add", name)
    subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", message, "--date", date],
                   check=True, env={"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": MAIL,
                                    "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": MAIL,
                                    "GIT_COMMITTER_DATE": date, "PATH": "/usr/bin:/bin:/usr/local/bin",
                                    "HOME": str(root)})
    return run(root, "rev-parse", "HEAD")


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        run(self.root, "init", "-q", "-b", "main")
        self.statement = "P1: X holds\n"
        self.freeze = commit(self.root, f"{UNDER}/predictions_frozen.md", self.statement, "freeze",
                             "2026-11-10T10:00:00+00:00")
        self.outcome = commit(self.root, f"{UNDER}/outcome.tsv", "x\t1\n", "outcome",
                              "2026-11-12T10:00:00+00:00")
        (self.root / RECEIPTS).write_text("")
        self.row = {c: "" for c in pl.COLUMNS}
        self.row.update(pred_id="P1", package=UNDER, statement_ref=f"{UNDER}/predictions_frozen.md#P1",
                        freeze_commit=self.freeze, freeze_blob_sha256=pl.sha256(self.statement.encode()),
                        kind="generative", outcome_ref=f"{UNDER}/outcome.tsv", outcome_commit=self.outcome,
                        predictor="sci", scorer="it", status="held")

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, **change):
        row = dict(self.row, **change)
        return pl.check_row(self.root, row, self.root / RECEIPTS)

    def write_ledger(self, rows):
        path = self.root / "ledger.tsv"
        with path.open("w") as handle:
            pl.write_tsv(rows, pl.COLUMNS, handle)
        return path


class SweepFindsFilesByNameAndText(Fixture):
    def test_name_and_text_hits_carry_first_add_commit_and_blob(self):
        text_commit = commit(self.root, f"{UNDER}/README.md", "These were frozen before reading.\n",
                             "readme", "2026-11-11T10:00:00+00:00")
        commit(self.root, f"{UNDER}/notes.md", "nothing here\n", "plain", "2026-11-11T11:00:00+00:00")
        rows = {r["path"]: r for r in pl.sweep(self.root, UNDER)}
        self.assertEqual(set(rows), {f"{UNDER}/predictions_frozen.md", f"{UNDER}/README.md"})
        self.assertEqual(rows[f"{UNDER}/predictions_frozen.md"]["via"], "name")
        self.assertEqual(rows[f"{UNDER}/predictions_frozen.md"]["first_add_commit"], self.freeze)
        self.assertEqual(rows[f"{UNDER}/README.md"]["via"], "text")
        self.assertEqual(rows[f"{UNDER}/README.md"]["first_add_commit"], text_commit)
        self.assertEqual(rows[f"{UNDER}/predictions_frozen.md"]["blob_sha256_at_add"],
                         pl.sha256(self.statement.encode()))

    def test_first_add_survives_a_later_edit(self):
        commit(self.root, f"{UNDER}/predictions_frozen.md", self.statement + "late note\n", "edit",
               "2026-11-13T10:00:00+00:00")
        row = pl.sweep(self.root, UNDER)[0]
        self.assertEqual(row["first_add_commit"], self.freeze)
        self.assertEqual(row["commits_touching"], "2")


class CheckSeparatesWhatGitProves(Fixture):
    def test_clean_row_passes_with_order_yes(self):
        bad, warn, order = self.check()
        self.assertEqual((bad, order), ([], "yes"))
        self.assertEqual(warn, [])

    def test_paper_content_is_labelled(self):
        _, warn, _ = self.check(kind="paper_content")
        self.assertIn("memory of the paper not excluded", warn)

    def test_outcome_already_in_tree_at_freeze_is_a_violation(self):
        bad, _, _ = self.check(outcome_ref=f"{UNDER}/predictions_frozen.md")
        self.assertTrue(any("already in the tree" in b for b in bad))

    def test_wrong_blob_digest_is_a_violation(self):
        bad, _, _ = self.check(freeze_blob_sha256="0" * 64)
        self.assertTrue(any("freeze_blob_sha256" in b for b in bad))

    def test_edit_after_freeze_is_a_warning_not_a_violation(self):
        commit(self.root, f"{UNDER}/predictions_frozen.md", self.statement + "edit\n", "edit",
               "2026-11-13T10:00:00+00:00")
        bad, warn, _ = self.check()
        self.assertEqual(bad, [])
        self.assertTrue(any(w.startswith("EDITED") for w in warn))

    def test_same_commit_is_reported_not_inferred(self):
        bad, warn, order = self.check(outcome_commit=self.freeze, outcome_ref="")
        self.assertEqual((bad, order), ([], "same_commit"))
        self.assertTrue(any("order is declared" in w for w in warn))

    def test_outcome_older_than_freeze_is_not_ancestor(self):
        bad, _, order = self.check(freeze_commit=self.outcome, statement_ref=f"{UNDER}/outcome.tsv",
                                   freeze_blob_sha256="", outcome_commit=self.freeze, outcome_ref="")
        self.assertEqual(order, "not_ancestor")
        self.assertTrue(any("not an ancestor" in b for b in bad))

    def test_no_outcome_commit_is_unknown(self):
        _, _, order = self.check(outcome_commit="", outcome_ref="")
        self.assertEqual(order, "unknown")

    def test_receipt_before_freeze_is_a_violation_after_is_not(self):
        receipts = self.root / RECEIPTS
        early = {"event_at": "2026-11-09T09:00:00+00:00", "study_id": {"pmid": "123", "doi": None}}
        late = {"event_at": "2026-11-12T09:00:00+00:00", "study_id": {"pmid": "456", "doi": None}}
        receipts.write_text(json.dumps(early) + "\n" + json.dumps(late) + "\n")
        bad, _, _ = self.check(outcome_study_id="PMID:123")
        self.assertTrue(any("read receipt" in b for b in bad))
        bad, _, _ = self.check(outcome_study_id="456")
        self.assertEqual(bad, [])

    def test_same_actor_as_predictor_and_scorer_is_a_violation(self):
        bad, _, _ = self.check(scorer="sci")
        self.assertTrue(any("same actor" in b for b in bad))

    def test_undeclared_roles_warn(self):
        _, warn, _ = self.check(predictor="", scorer="")
        self.assertTrue(any("not both declared" in w for w in warn))

    def test_unknown_commit_and_vocabulary(self):
        bad, _, _ = self.check(freeze_commit="1" * 40)
        self.assertTrue(any("not found" in b for b in bad))
        bad, _, _ = self.check(status="great", kind="guess")
        self.assertEqual(len(bad), 2)


class CliExitCodes(Fixture):
    def cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = pl.main(["--root", str(self.root), *argv])
        return code, out.getvalue(), err.getvalue()

    def test_clean_ledger_exits_zero_and_violation_exits_one(self):
        ok = self.write_ledger([self.row])
        code, out, _ = self.cli("check", str(ok), "--receipts", RECEIPTS)
        self.assertEqual(code, 0)
        self.assertIn("freeze_precedes_outcome=yes", out)
        bad = self.write_ledger([dict(self.row, scorer="sci")])
        self.assertEqual(self.cli("check", str(bad), "--receipts", RECEIPTS)[0], 1)

    def test_strict_makes_an_edit_fatal(self):
        commit(self.root, f"{UNDER}/predictions_frozen.md", self.statement + "edit\n", "edit",
               "2026-11-13T10:00:00+00:00")
        ledger = self.write_ledger([self.row])
        self.assertEqual(self.cli("check", str(ledger), "--receipts", RECEIPTS)[0], 0)
        self.assertEqual(self.cli("check", str(ledger), "--receipts", RECEIPTS, "--strict")[0], 1)

    def test_malformed_ledger_exits_two(self):
        path = self.root / "bad.tsv"
        path.write_text("pred_id\tpackage\nP1\tx\n")
        self.assertEqual(self.cli("check", str(path))[0], 2)
        dup = self.write_ledger([self.row, self.row])
        self.assertEqual(self.cli("check", str(dup))[0], 2)

    def test_sweep_writes_header_and_rows(self):
        out = self.root / "cands.tsv"
        code, _, err = self.cli("sweep", "--under", UNDER, "--out", str(out))
        self.assertEqual(code, 0)
        self.assertIn("candidates 1", err)
        self.assertTrue(out.read_text().startswith("\t".join(pl.CANDIDATE_COLUMNS)))

    def test_help_is_safe_and_writes_nothing(self):
        before = run(self.root, "status", "--porcelain")
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as stop:
            pl.main(["--help"])
        self.assertEqual(stop.exception.code, 0)
        self.assertEqual(run(self.root, "status", "--porcelain"), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
