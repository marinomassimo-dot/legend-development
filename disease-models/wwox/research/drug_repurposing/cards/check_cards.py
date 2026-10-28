#!/usr/bin/env python3
"""Offline regression for the P4 cards in this directory (scientist-a, REPURP-10H-P4-DEEP-A-20261022).

Checks, for every `*.packet.json`: the bridge builds it; the stored `*.card.json` is exactly what the
bridge builds today; the roadmap's P4 fields are all present (UNKNOWN allowed, absent never); an
abstention names its missing datum; no score, rank, probability or blended index appears as a key;
no dose-, route- or schedule-looking token, e-mail string or ellipsis appears; every receipt id
quoted resolves in the receipt ledger (string presence only: content is not re-verified).

Run from the repository root:  python3 disease-models/wwox/research/drug_repurposing/cards/check_cards.py
It reads the bridge; it never writes it.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import repurposing_bridge as bridge  # noqa: E402

P4_KEYS = ("identity", "indication_and_transfer", "novelty_for_woree", "state_of_known_roads",
           "pathway_and_objective", "expected_contribution", "mechanism", "sources",
           "evidence_for_and_against", "time_to_access", "time_to_benefit", "pharmacology",
           "paediatrics_and_interactions", "scope_of_checks", "question_history", "predictions",
           "next_measurement", "status", "value_added", "clinical_census")
STATUS = {"hypothesis", "controversial", "deferred with reason", "abstention"}
FORBIDDEN_KEY = re.compile(r"score|rank|probab|index|weight", re.I)
FORBIDDEN_TEXT = re.compile(
    r"\d\s?(nM|uM|µM|mM|mg|µg|ug|vg|mL|kg)\b|mg/kg|\bq\d+h\b|\be-?mails?\b|@|…|\.\.\.", re.I)
# The e-mail pattern must still catch the word and must not match inside a surname (a citation of a 2014 WWOX paper by its first author).
assert FORBIDDEN_TEXT.search("write to the e-mail address") and FORBIDDEN_TEXT.search("an email") and not FORBIDDEN_TEXT.search("Abu-Remaileh 2014")
RECEIPT = re.compile(r"FTR-\d{8}-\d{8}-\d{2}")


def keys(node):
    if isinstance(node, dict):
        for k, v in node.items():
            yield k
            yield from keys(v)
    elif isinstance(node, list):
        for v in node:
            yield from keys(v)


def strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from strings(v)


def main() -> int:
    ledger = (ROOT / "disease-models" / "wwox" / "registries" / "fulltext_read_receipts.jsonl").read_text(encoding="utf-8")
    problems = []
    packets = sorted(HERE.glob("*.packet.json"))
    for path in packets:
        name = path.name
        packet = json.loads(path.read_text(encoding="utf-8"))
        card = bridge.build_card(packet)
        stored = json.loads((HERE / name.replace(".packet.json", ".card.json")).read_text(encoding="utf-8"))
        if card != stored:
            problems.append(f"{name}: stored card differs from what the bridge builds")
        if card["epistemic_status"] != "IPOTESI" or card["canonical"]:
            problems.append(f"{name}: card is not IPOTESI/non-canonical")
        p4 = packet.get("p4_card", {})
        for k in P4_KEYS:
            if k not in p4 or p4[k] in ("", None):
                problems.append(f"{name}: p4_card.{k} absent (UNKNOWN is allowed, absent is not)")
        if p4.get("status") not in STATUS:
            problems.append(f"{name}: status {p4.get('status')!r} outside {sorted(STATUS)}")
        if p4.get("time_to_access") is None or p4.get("time_to_benefit") is None:
            problems.append(f"{name}: time_to_access and time_to_benefit must both be present and separate")
        for k in ("endpoint_pursued", "functional_evidence_available", "temporal_or_model_limit"):
            if k not in card["p4_fields"]:
                problems.append(f"{name}: bridge p4_fields.{k} absent")
        if card["label_lookup"]["status"] != "NOT_ATTEMPTED":
            problems.append(f"{name}: label_lookup is not NOT_ATTEMPTED, yet no search was run")
        if p4.get("status") == "abstention":
            block = packet.get("abstention_card", {})
            if not block.get("missing_datum") or not block.get("search_record"):
                problems.append(f"{name}: abstention without missing_datum/search_record")
            if card["abstention"] != "NO_DRUG_ASSERTIONS_SUPPLIED":
                problems.append(f"{name}: abstention card carries drug assertions")
        elif not packet["drug_assertions"]:
            problems.append(f"{name}: non-abstention card without assertions")
        if not packet.get("not_known"):
            problems.append(f"{name}: not_known is empty (a card must show what is not known)")
        for k in keys(packet):
            if FORBIDDEN_KEY.search(k):
                problems.append(f"{name}: forbidden key {k!r}")
        for text in strings(packet):
            if FORBIDDEN_TEXT.search(text):
                problems.append(f"{name}: forbidden token in {text[:80]!r}")
            for rid in RECEIPT.findall(text):
                if rid not in ledger:
                    problems.append(f"{name}: receipt {rid} not found in the ledger")
        for row in packet["drug_assertions"]:
            if NW_MISSING(row, packet):
                problems.append(f"{name}: {row['id']} lacks the NOT WWOX EVIDENCE label")
    print(f"{len(packets)} packets checked, {len(problems)} problem(s)")
    for p in problems:
        print("  -", p)
    return 1 if problems else 0


def NW_MISSING(row, packet):
    wwox_ctx = ("Wwox-null" in row["context"]["disease_id"]) or ("organoid" in row["context"]["disease_id"]) \
        or row.get("evidence_scope") == "WWOX_EXPERIMENT_IN_DEE_SYSTEM"
    return (not wwox_ctx) and "NOT WWOX EVIDENCE" not in row["source"]


if __name__ == "__main__":
    raise SystemExit(main())
