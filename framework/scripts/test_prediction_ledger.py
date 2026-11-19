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
        self.row = {c: "" for c in pl.COLUMNS + pl.OPTIONAL_COLUMNS}
        self.row.update(pred_id="P1", package=UNDER, statement_ref=f"{UNDER}/predictions_frozen.md#P1",
                        freeze_commit=self.freeze, freeze_blob_sha256=pl.sha256(self.statement.encode()),
                        kind="generative", outcome_ref=f"{UNDER}/outcome.tsv", outcome_commit=self.outcome,
                        predictor="sci", scorer="it", status="held", outcome_sha256=pl.sha256(b"x\t1\n"))

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, **change):
        row = dict(self.row, **change)
        return pl.check_row(self.root, row, self.root / RECEIPTS)

    def write_ledger(self, rows):
        path = self.root / "ledger.tsv"
        with path.open("w") as handle:
            pl.write_tsv(rows, pl.COLUMNS + pl.OPTIONAL_COLUMNS, handle)
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

    def test_a_statement_ref_with_a_space_instead_of_a_hash_names_the_same_file(self):
        bad, _, order = self.check(statement_ref=f"{UNDER}/predictions_frozen.md F1")
        self.assertEqual((bad, order), ([], "yes"))

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

    def test_a_receipt_before_the_freeze_names_the_study_and_is_a_warning_when_blindness_is_declared(self):
        (self.root / RECEIPTS).write_text(json.dumps({"event_at": "2026-11-09T09:00:00+00:00", "event_id": "FTR-1",
                                                       "record_kind": "legacy_reconstruction",
                                                       "study_id": {"pmid": "123", "doi": None}}) + "\n")
        bad, _, _ = self.check(outcome_study_id="PMID 123; PMID 9")
        self.assertTrue(any("1 outcome source(s)" in b and "123" in b and "FTR-1" in b and "legacy_reconstruction" in b for b in bad), bad)
        bad, warn, _ = self.check(outcome_study_id="PMID 123", blindness="declared")
        self.assertEqual(bad, [])
        self.assertTrue(any("blindness declared, not shown" in w and "123" in w for w in warn), warn)

    def test_a_public_outcome_in_the_tree_is_a_warning_only_when_blindness_is_declared(self):
        bad, warn, _ = self.check(outcome_ref=f"{UNDER}/predictions_frozen.md", blindness="declared", outcome_commit="",
                                  outcome_sha256="")
        self.assertEqual(bad, [])
        self.assertTrue(any("outcome_in_tree_at_freeze = yes (blindness declared, not shown)" in w for w in warn))
        bad, _, _ = self.check(blindness="maybe")
        self.assertTrue(any("blindness" in b for b in bad))

    def test_several_outcome_sources_are_checked_and_prefixes_are_normalised(self):
        self.assertEqual(pl.study_ids("PMID 123; doi:10.1/X ;; PMID: 45"), ["123", "10.1/x", "45"])
        (self.root / RECEIPTS).write_text(json.dumps({"event_at": "2026-11-09T09:00:00+00:00",
                                                       "study_id": {"pmid": "45", "doi": None}}) + "\n")
        bad, _, _ = self.check(outcome_study_id="PMID 123; PMID 45")
        self.assertTrue(any("read receipt" in b for b in bad))

    def test_a_declared_freeze_time_earlier_than_the_commit_is_flagged_as_not_shown_by_git(self):
        # the fixture's freeze commit is dated 2026-11-10T10:00:00Z
        _, warn, _ = self.check(freeze_utc_declared="2026-11-10T09:00:00Z")
        self.assertTrue(any("freeze time declared, not shown by git (rebased)" in w for w in warn), warn)
        for ok in ("2026-11-10T10:00:00Z", "2026-11-10T11:30:00+00:00", ""):
            _, warn, _ = self.check(freeze_utc_declared=ok)
            self.assertFalse(any("not shown by git" in w for w in warn), (ok, warn))
        bad, _, _ = self.check(freeze_utc_declared="yesterday")
        self.assertTrue(any("not an ISO time" in b for b in bad))

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


class OutcomeDigest(Fixture):
    def test_a_committed_outcome_needs_its_digest_recorded_and_equal(self):
        bad, _, _ = self.check(outcome_sha256="")
        self.assertTrue(any("digest (outcome_sha256) is not recorded" in b for b in bad))
        bad, _, _ = self.check(outcome_sha256="0" * 64)
        self.assertTrue(any("outcome_sha256 does not match" in b for b in bad))
        self.assertEqual(self.check()[0], [])


class Guard(Fixture):
    """The outcome table to be opened is a NEW file (`sealed.tsv`), created after the guard says so."""
    TABLE = f"{UNDER}/sealed.tsv"

    def setUp(self):
        super().setUp()
        self.rule = commit(self.root, f"{UNDER}/rule.json", "{}\n", "rule", "2026-11-10T09:00:00+00:00")
        self.later = commit(self.root, f"{UNDER}/other.md", "later\n", "later", "2026-11-11T10:00:00+00:00")
        self.row.update(outcome_ref=self.TABLE, outcome_commit="", outcome_sha256="", blindness="")

    def guard(self, rows=None, requires=(f"{UNDER}/rule.json",), table=None):
        ledger = self.write_ledger(self.row_list(rows))
        if table is not None:
            (self.root / self.TABLE).write_text(table)
        return pl.guard(self.root, ledger, self.TABLE, list(requires), self.root / RECEIPTS)

    def row_list(self, rows):
        return [self.row] if rows is None else rows

    def test_may_open_when_freeze_rule_and_files_are_committed(self):
        ok, lines = self.guard()
        self.assertTrue(ok, lines)
        self.assertTrue(lines[0].startswith("OUTCOME_MAY_OPEN: " + self.TABLE))
        self.assertIn(self.freeze[:12], lines[0])
        self.assertIn(f"{UNDER}/rule.json", lines[0])

    def test_refused_when_no_row_names_the_table(self):
        ok, lines = self.guard(rows=[dict(self.row, outcome_ref=f"{UNDER}/elsewhere.tsv")])
        self.assertFalse(ok)
        self.assertIn("nothing was frozen against it", lines[0])

    def test_refused_when_the_freeze_commit_is_unknown_or_head_or_unrecorded(self):
        self.assertFalse(self.guard(rows=[dict(self.row, freeze_commit="1" * 40)])[0])
        head = run(self.root, "rev-parse", "HEAD")
        ok, lines = self.guard(rows=[dict(self.row, freeze_commit=head, statement_ref=f"{UNDER}/other.md",
                                           freeze_blob_sha256=pl.sha256(b"later\n"))])
        self.assertFalse(ok)
        self.assertTrue(any("freeze commit is HEAD itself" in l for l in lines), lines)
        ok, lines = self.guard(rows=[dict(self.row, freeze_blob_sha256="")])
        self.assertTrue(any("freeze_blob_sha256 is not recorded" in l for l in lines), lines)

    def test_refused_when_a_required_file_is_missing_dirty_or_pinned_wrong(self):
        self.assertTrue(any("not committed in HEAD" in l for l in self.guard(requires=[f"{UNDER}/nope.md"])[1]))
        (self.root / f"{UNDER}/rule.json").write_text("{\"changed\": 1}\n")
        self.assertTrue(any("uncommitted change" in l for l in self.guard()[1]))
        run(self.root, "checkout", "--", f"{UNDER}/rule.json")
        ok, lines = self.guard(requires=[f"{UNDER}/rule.json=" + "0" * 64])
        self.assertTrue(any("not the pinned" in l for l in lines), lines)
        good = pl.sha256(b"{}\n")
        self.assertTrue(self.guard(requires=[f"{UNDER}/rule.json={good}"])[0])

    def test_an_existing_table_must_be_the_sealed_one(self):
        ok, lines = self.guard(table="x\t1\n")
        self.assertFalse(ok)
        self.assertTrue(any("digest is not recorded" in l for l in lines), lines)
        sealed = dict(self.row, outcome_sha256=pl.sha256(b"x\t1\n"))
        self.assertTrue(self.guard(rows=[sealed], table="x\t1\n")[0])
        ok, lines = self.guard(rows=[sealed], table="tampered\n")
        self.assertTrue(any("differs from the sealed digest" in l for l in lines), lines)

    def test_the_cli_prints_the_exact_lines_and_exit_codes(self):
        ledger = self.write_ledger([self.row])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = pl.main(["--root", str(self.root), "guard", str(ledger), "--outcome", self.TABLE,
                            "--require", f"{UNDER}/rule.json", "--receipts", RECEIPTS])
        self.assertEqual((code, out.getvalue().startswith("OUTCOME_MAY_OPEN: ")), (0, True))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = pl.main(["--root", str(self.root), "guard", str(ledger), "--outcome", self.TABLE,
                            "--require", f"{UNDER}/missing.md", "--receipts", RECEIPTS])
        self.assertEqual((code, out.getvalue().startswith("OUTCOME_REFUSED: ")), (1, True))


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

    def test_summary_counts_per_kind_and_never_pools_kinds(self):
        head = "\t".join(pl.COLUMNS) + "\n"

        def row(i, kind, status):
            cells = {c: "" for c in pl.COLUMNS}
            cells.update(pred_id=i, kind=kind, status=status)
            return "\t".join(cells[c] for c in pl.COLUMNS) + "\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.tsv"
            path.write_text(head + row("a", "generative", "held") + row("b", "generative", "failed") + row("c", "generative", "mixed")
                            + row("d", "generative", "open") + row("e", "paper_content", "held"))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(pl.main(["summary", str(path)]), 0)
        text = out.getvalue()
        self.assertIn("kind=generative: rows 4; held 1, mixed 1, failed 1; held 1 of 3 scored (33%)", text)
        self.assertIn("is below 30: a count, not a calibration", text)
        self.assertIn("kind=paper_content: rows 1; held 1, mixed 0, failed 0; held 1 of 1 scored (100%)", text)

    def test_summary_of_a_missing_ledger_exits_two(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            self.assertEqual(pl.main(["summary", "/nonexistent/ledger.tsv"]), 2)

    def test_help_is_safe_and_writes_nothing(self):
        before = run(self.root, "status", "--porcelain")
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as stop:
            pl.main(["--help"])
        self.assertEqual(stop.exception.code, 0)
        self.assertEqual(run(self.root, "status", "--porcelain"), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
