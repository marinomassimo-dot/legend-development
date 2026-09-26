#!/usr/bin/env python3
"""record_edit_bench.py — Benchmark J's labeller and replay, on fixtures that can fail.

The labeller must (1) attribute a targeted record's edit to INTENDED, (2) call a lost separator
outside the target drift, (3) leave an unattributable change to judgement rather than guess; the
replay must reproduce the edit set exactly and must NOT carry a drift hunk. The committed
results must agree with the documents that quote them.

Run: python3 framework/scripts/test_record_edit_bench.py
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import record_edit_bench as bench  # noqa: E402

PATH = "disease-models/wwox/registries/claim_registry_current.md"
PARENT = ("# Claim Registry Current\n\n## CLAIM 001\n**Title:** one\n\n---\n\n"
          "## CLAIM 002\n**Title:** two\n\n---\n\n## CLAIM 003\n**Title:** three\n")


def ctx(message: str) -> dict:
    return {"sha": "0" * 40, "parent": "1" * 40, "subject": message.splitlines()[0],
            "message": message, "targets": bench.named_ids(message),
            "named_identifiers": bench.identifiers(message),
            "batch_ids": set(bench.BATCH_ID.findall(message.splitlines()[0])),
            "companions": [], "structural": False}


class Identifiers(unittest.TestCase):
    def test_ranges_and_lists_expand(self):
        ids = bench.named_ids("PAPER 081-084 and CLAIM 014/015, LIT-0410-0412; CLAIMS 9, 11 and 36")
        self.assertTrue({("PAPER", "81"), ("PAPER", "84"), ("CLAIM", "14"), ("CLAIM", "15"),
                         ("LIT", "410"), ("LIT", "412"), ("CLAIM", "9"), ("CLAIM", "36")} <= ids)


class Labelling(unittest.TestCase):
    def label(self, child: str, message: str) -> list[dict]:
        event = bench.label_texts(PARENT, child, PATH, ctx(message))
        bench.resolve_commit([event], {})
        return event["hunks"]

    def test_target_record_is_intended_and_lost_separator_is_drift(self):
        child = PARENT.replace("**Title:** two", "**Title:** two, narrowed").replace(
            "## CLAIM 001\n**Title:** one\n\n---\n\n", "## CLAIM 001\n**Title:** one\n\n")
        hunks = {h["unit"]: h for h in self.label(child, "BATCH_X: narrow CLAIM 002")}
        self.assertEqual(hunks["CLAIM 002"]["label"], "INTENDED")
        self.assertEqual(hunks["CLAIM 001"]["label"], "VERBATIM_COPY_DRIFT")

    def test_unattributable_change_goes_to_judgement(self):
        child = PARENT.replace("**Title:** three", "**Title:** three, reworded")
        hunks = self.label(child, "BATCH_X: narrow CLAIM 002")
        self.assertEqual([h["label"] for h in hunks], ["UNRESOLVED"])

    def test_version_line_is_legitimate_collateral(self):
        parent_line = "## CLAIM 001\n**Title:** one\n"
        child = PARENT.replace(parent_line, parent_line + "**Last update:** 2026-09-26\n")
        hunks = self.label(child, "BATCH_X: narrow CLAIM 002")
        self.assertEqual(hunks[0]["label"], "LEGITIMATE_COLLATERAL")


class Replay(unittest.TestCase):
    def test_edit_set_reproduced_and_drift_not_carried(self):
        child = PARENT.replace("**Title:** two", "**Title:** two, narrowed").replace(
            "## CLAIM 001\n**Title:** one\n\n---\n\n", "## CLAIM 001\n**Title:** one\n\n") + (
            "\n---\n\n## CLAIM 004\n**Title:** four\n")
        event = bench.label_texts(PARENT, child, PATH, ctx("BATCH_X: CLAIM 002, CLAIM 003, CLAIM 004"))
        bench.resolve_commit([event], {})
        labels = {h["id"]: h["label"] for h in event["hunks"]}
        self.assertIn("VERBATIM_COPY_DRIFT", labels.values())
        for mode in ("record", "range"):
            result = bench.replay_event(PARENT, child, PATH, "0" * 12, labels, mode)
            self.assertEqual(result["refused"], [], mode)
            self.assertEqual(result["silent_corruption"], [], mode)
            self.assertTrue(result["r_equals_x"], mode)
            self.assertFalse(result["r_equals_child"], mode)      # the drift was not carried
            self.assertEqual(result["counts"].get("VERBATIM_COPY_DRIFT:prevented"), 1, mode)


class CommittedResults(unittest.TestCase):
    def test_documents_quote_the_committed_figures(self):
        corpus = json.loads(bench.CORPUS.read_text(encoding="utf-8"))
        results = json.loads(bench.J2_RESULTS.read_text(encoding="utf-8"))
        unique = corpus["summary_unique_patches"]
        self.assertEqual((unique["file_events"], unique["hunks"]), (72, 708))
        self.assertEqual(unique["labels"].get("ACCIDENTAL_COLLATERAL", 0), 0)
        lost = {name: len(fam["lost_record"]) for name, fam in results["families"].items()}
        self.assertEqual(lost["paper_registry_current.md"], 1)
        for name in ("claim_registry_current.md", "literature_tracking_log_current.md",
                     "working_model_current.md"):
            self.assertEqual(lost[name], 0, name)
        self.assertEqual(sum(fam["silent"] for fam in results["families"].values()), 0)
        import batch_commit
        supported = {Path(p).name for p in batch_commit.RECORD_SCOPED}
        self.assertEqual(supported, {name for name, n in lost.items() if n == 0
                                     and name.endswith("_current.md")
                                     and not name.startswith(("meta_", "research_"))})


if __name__ == "__main__":
    unittest.main(verbosity=1)
