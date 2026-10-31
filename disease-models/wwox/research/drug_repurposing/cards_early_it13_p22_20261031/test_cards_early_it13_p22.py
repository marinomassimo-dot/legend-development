#!/usr/bin/env python3
"""Targeted tests for the cards_early regeneration (read-only). Run: python3 test_cards_early_it13_p22.py"""
import json, subprocess, sys, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "framework/scripts/repurposing_bridge.py").is_file())
sys.path.insert(0, str(ROOT / "framework/scripts"))
import repurposing_bridge as bridge  # noqa: E402

EARLY = ROOT / "disease-models/wwox/research/drug_repurposing/cards_early"
NEW = {p.name: json.loads(p.read_text()) for p in (HERE / "regenerated").glob("*.card.json")}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


class RegeneratedCards(unittest.TestCase):
    def test_seven_cards(self):
        self.assertEqual(len(NEW), 7)

    def test_equals_bridge_output(self):
        for name, card in NEW.items():
            self.assertEqual(card, bridge.build_card(load(EARLY / name.replace(".card", ".packet"))), name)

    def test_only_endpoint_outcomes_and_sha_differ(self):
        for name, card in NEW.items():
            old = load(EARLY / name)
            diff = {k for k in set(old) | set(card) if old.get(k) != card.get(k)}
            self.assertLessEqual(diff, {"endpoint_outcomes", "input_sha256"}, name)
            if name != "EB-VGB-01.card.json":
                self.assertEqual(diff, {"endpoint_outcomes"}, name)

    def test_abstentions_have_empty_outcomes_and_unresolved(self):
        for name, card in NEW.items():
            if card["abstention"]:
                self.assertEqual(card["endpoint_outcomes"], [], name)
                self.assertEqual(card["directional_summary"], "UNRESOLVED", name)

    def test_vgb_outcome_is_one_question_undeclared(self):
        eo = NEW["EB-VGB-01.card.json"]["endpoint_outcomes"]
        self.assertEqual(len(eo), 1)
        self.assertEqual(eo[0]["assertion_ids"], ["A-VGB-1", "A-VGB-3"])
        self.assertEqual(eo[0]["statuses"], ["OPPOSES_DISEASE_CHANGE"])
        self.assertFalse(eo[0]["discriminators_declared"])
        # nine other rows stay UNRESOLVED: nothing was promoted
        st = [c["status"] for c in NEW["EB-VGB-01.card.json"]["comparisons"]]
        self.assertEqual(st.count("UNRESOLVED"), 9)

    def test_vgb_stored_sha_was_stale_regenerated_matches_packet(self):
        old = load(EARLY / "EB-VGB-01.card.json")
        self.assertEqual(old["input"], NEW["EB-VGB-01.card.json"]["input"])   # same content ...
        self.assertNotEqual(old["input_sha256"], NEW["EB-VGB-01.card.json"]["input_sha256"])  # ... stale digest

    def test_no_prebaked_field(self):
        for name, card in NEW.items():
            self.assertEqual(set(card), set(load(EARLY / name)) | {"endpoint_outcomes"}, name)

    def test_unchanged_cards_untouched(self):
        for n in ("EB-KD-01", "EB-ETX-01"):
            self.assertEqual(load(EARLY / f"{n}.card.json"), bridge.build_card(load(EARLY / f"{n}.packet.json")))


if __name__ == "__main__":
    unittest.main()
