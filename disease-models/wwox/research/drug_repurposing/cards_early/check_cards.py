#!/usr/bin/env python3
"""Mechanical checks for the early-benefit candidate cards (cards_early/).

Run from anywhere:  python3 check_cards.py [--extra-source PATH ...]

What it checks, per input packet and the card the bridge builds from it:
  1. the stored card is byte-for-byte what `repurposing_bridge.build_card` returns now;
  2. every roadmap P4 field is present (UNKNOWN rather than absent) and the later P4 blocks are complete;
  3. no key anywhere is a score, rank, probability, dose, schedule or suitability field, and no string
     carries a dose-like quantity;
  4. no e-mail string and no truncated hexadecimal digest;
  5. every «quoted» passage occurs verbatim (after markdown stripping) in a repository source file,
     contains no ellipsis, and is therefore not stitched;
  6. an assertion outside WWOX carries the label NOT WWOX EVIDENCE;
  7. a candidate card names one endpoint and keeps time to access apart from time to benefit;
     an abstention card says ASTENSIONE and names its missing datum.

It reads files and prints; it writes nothing. It verifies mechanics, not science: a card that passes is
not true, only well-formed. Exit 0 on pass, 1 on any failure.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_root() -> Path:
    for parent in [HERE, *HERE.parents]:
        if (parent / "framework" / "scripts" / "repurposing_bridge.py").is_file():
            return parent
    raise SystemExit("cannot find the repository root")


ROOT = find_root()
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import repurposing_bridge as bridge  # noqa: E402

ROADMAP_KEYS = ["identity", "indication_and_transfer", "novelty_for_woree", "known_roads_state",
                "path_and_objective", "expected_contribution", "mechanism", "sources", "evidence_pro_contra",
                "time_to_access", "time_to_benefit", "pharmacology", "paediatrics_and_interactions",
                "verification_scope", "question_history", "predictions", "next_measure", "status", "value_added"]
FORBIDDEN_KEYS = re.compile(r"(score|rank|probab|likelihood|blend|dose|dosage|schedule|regimen|posology|suitab|index)", re.I)
ALLOWED_KEYS = {"pediatric_suitability"}            # emitted by the bridge, must stay UNKNOWN
DOSE_LIKE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|mcg|µg|ug|ml|mL|g|IU|ng/mL)\b(?:\s?/\s?(?:kg|day|d|m2|m²))?")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
HEX_RUN = re.compile(r"\b[0-9a-fA-F]{12,}\b")
QUOTE = re.compile(r"«([^»]+)»")
NOT_WWOX_NEEDED = re.compile(r"WOREE|WWOX|Wwox")

SOURCE_FILES = [
    "disease-models/wwox/registries/claim_registry_current.md",
    "disease-models/wwox/research/repurposing_known_roads_20261020_scientist-a.md",
    "disease-models/wwox/research/repurposing_early_benefit_20261020_scientist-b.md",
    "disease-models/wwox/research/repurposing_10h_scientist-d_20261021.md",
    "disease-models/wwox/research/repurposing_10h_scientist-c_20261021.md",
    "disease-models/wwox/research/repurposing_10h_scientist-b_20261021.md",
    "disease-models/wwox/research/drug_repurposing/clinical_census_20261020.md",
    "disease-models/wwox/research/discovery_ledger_current.md",
    "disease-models/wwox/research/dismissal_ledger_current.md",
    "disease-models/wwox/research/deepdive_manifests/PMID32000863.json",
]


def norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("**", "").replace("*", "").replace("`", "")
    text = re.sub(r"\n\s*>\s?", " ", text)
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def walk(node, path=()):
    if isinstance(node, dict):
        for key, value in node.items():
            yield path + (key,), key, value
            yield from walk(value, path + (key,))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from walk(value, path + (i,))


def strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for value in node.values():
            yield from strings(value)
    elif isinstance(node, list):
        for value in node:
            yield from strings(value)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extra-source", action="append", default=[],
                    help="extra file to search for quotes (e.g. a note on an unlanded branch)")
    args = ap.parse_args(argv)

    corpus, missing = [], []
    for rel in SOURCE_FILES:
        path = ROOT / rel
        if path.is_file():
            corpus.append(norm(path.read_text(encoding="utf-8", errors="replace")))
        else:
            missing.append(rel)
    for extra in args.extra_source:
        corpus.append(norm(Path(extra).read_text(encoding="utf-8", errors="replace")))
    blob = "\n".join(corpus)

    failures: list[str] = []
    unverified: list[str] = []
    packets = sorted(HERE.glob("*.packet.json"))
    if not packets:
        failures.append("no packets found")
    for packet_path in packets:
        name = packet_path.name.replace(".packet.json", "")
        fail = lambda msg: failures.append(f"{name}: {msg}")  # noqa: E731
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        card_path = packet_path.with_name(name + ".card.json")
        if not card_path.is_file():
            fail("card file missing")
            continue
        stored = json.loads(card_path.read_text(encoding="utf-8"))
        # 1 reproducibility
        try:
            rebuilt = bridge.build_card(packet)
        except ValueError as exc:
            fail(f"bridge refuses the packet: {exc}")
            continue
        if rebuilt != stored:
            fail("stored card differs from what the bridge builds from the packet now")
        # 2 fields
        fields = packet.get("p4_roadmap_fields", {})
        if sorted(fields) != sorted(ROADMAP_KEYS):
            fail(f"p4_roadmap_fields keys differ: missing {sorted(set(ROADMAP_KEYS) - set(fields))}, extra {sorted(set(fields) - set(ROADMAP_KEYS))}")
        for key, value in fields.items():
            if not isinstance(value, str) or not value.strip():
                fail(f"p4_roadmap_fields.{key} is empty (use UNKNOWN)")
        for key in ("endpoint_pursued", "functional_evidence_available", "temporal_or_model_limit"):
            if stored["p4_fields"].get(key, "") in ("", None):
                fail(f"p4_fields.{key} missing")
        if "label_lookup" not in stored or stored["label_lookup"]["status"] not in bridge.LOOKUP_STATUS:
            fail("label_lookup absent from card")
        for key in ("not_known", "evaluation_frame", "must_never", "card_kind"):
            if not packet.get(key):
                fail(f"packet lacks {key}")
        # 3 forbidden keys / dose-like strings
        for path, key, value in walk(packet):
            if len(path) == 1 and key == "route":
                continue
            if isinstance(key, str) and FORBIDDEN_KEYS.search(key) and key not in ALLOWED_KEYS:
                fail(f"forbidden key at {'/'.join(map(str, path))}")
        for key in ("pediatric_suitability",):
            if stored["translation"].get(key) != "UNKNOWN":
                fail(f"translation.{key} is not UNKNOWN")
        for text in strings(packet):
            if DOSE_LIKE.search(text):
                fail(f"dose-like quantity in text: {DOSE_LIKE.search(text).group(0)!r}")
            if EMAIL.search(text):
                fail("e-mail-like string")
            for run in HEX_RUN.findall(text):
                if len(run) != 64:
                    fail(f"hexadecimal run of length {len(run)} that is not a full digest: {run[:6]}...")
        # 5 verbatim quotes
        for text in strings(packet):
            for quote in QUOTE.findall(text):
                if "…" in quote or "..." in quote:
                    fail(f"quote stitched with an ellipsis: {quote[:50]!r}")
                    continue
                if norm(quote) not in blob:
                    unverified.append(f"{name}: quote not found in the source files read: {quote[:70]!r}")
        # 6 label for non-WWOX
        for row in [packet["disease_assertion"], *packet["drug_assertions"]]:
            if not NOT_WWOX_NEEDED.search(row["context"]["disease_id"]):
                if row.get("evidence_label") != "NOT WWOX EVIDENCE":
                    fail(f"assertion {row['id']} is outside WWOX and lacks evidence_label NOT WWOX EVIDENCE")
            if row["epistemic_status"] == "DATO" and row.get("reading_depth") == "UNKNOWN" and "note" not in row:
                fail(f"assertion {row['id']} is DATO with reading depth UNKNOWN and no note")
        # 7 candidate vs abstention
        status = fields.get("status", "")
        if packet["card_kind"] == "CANDIDATE_CARD":
            if not packet["drug_assertions"]:
                fail("candidate card with no drug assertion")
            if stored["p4_fields"]["endpoint_pursued"] == "UNKNOWN":
                fail("candidate card does not name its endpoint")
            if fields.get("time_to_access") == fields.get("time_to_benefit"):
                fail("time to access and time to benefit are the same text")
            if stored["assessment"] != "REQUIRES_QUALIFICATION":
                fail(f"unexpected bridge assessment {stored['assessment']}")
        else:
            if packet["drug_assertions"] or stored.get("abstention") != "NO_DRUG_ASSERTIONS_SUPPLIED":
                fail("abstention card carries drug assertions or the bridge did not mark the abstention")
            if not status.startswith("ASTENSIONE") or "Missing datum" not in status:
                fail("abstention card must start status with ASTENSIONE and name the Missing datum")

    print(f"packets checked: {len(packets)}")
    if missing:
        print("source files absent in this checkout (quotes may be unverified):", *missing, sep="\n  ")
    if unverified:
        print("QUOTES NOT VERIFIED:", *unverified, sep="\n  ")
    if failures:
        print("FAIL:", *failures, sep="\n  ")
        return 1
    if unverified:
        print("PASS WITH UNVERIFIED QUOTES (pass --extra-source for a note on an unlanded branch)")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
