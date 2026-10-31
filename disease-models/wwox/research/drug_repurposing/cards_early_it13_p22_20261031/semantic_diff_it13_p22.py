#!/usr/bin/env python3
"""Semantic before/after diff of the cards_early cards against their regenerated copies (read-only).

Usage: semantic_diff_it13_p22.py [--package DIR]   (default: the directory of this script)
For each regenerated card it checks: the card equals what the bridge builds from the packet now; the
stored card and the regenerated one differ ONLY in `endpoint_outcomes` and `input_sha256`; every other
top-level key (evidence = comparisons, contexts = input, nulls = comparisons/limits, provenance =
input/translation/label_lookup) is identical. Prints a table and returns 1 on any other difference.
"""
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "framework/scripts/repurposing_bridge.py").is_file())
sys.path.insert(0, str(ROOT / "framework/scripts"))
import repurposing_bridge as bridge  # noqa: E402

EARLY = ROOT / "disease-models/wwox/research/drug_repurposing/cards_early"
ALLOWED = {"endpoint_outcomes", "input_sha256"}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--package", default=str(HERE))
    args = ap.parse_args(argv)
    bad = 0
    for new_path in sorted((Path(args.package) / "regenerated").glob("*.card.json")):
        name = new_path.name.replace(".card.json", "")
        new = json.loads(new_path.read_text(encoding="utf-8"))
        old = json.loads((EARLY / f"{name}.card.json").read_text(encoding="utf-8"))
        packet = json.loads((EARLY / f"{name}.packet.json").read_text(encoding="utf-8"))
        problems = []
        if bridge.build_card(packet) != new:
            problems.append("regenerated card is not what the bridge builds from the packet")
        diff = sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k))
        if set(diff) - ALLOWED:
            problems.append(f"unexpected differing keys: {sorted(set(diff) - ALLOWED)}")
        same_sha = old["input_sha256"] == new["input_sha256"]
        print(f"{name}\tdiffering={diff}\tinput_sha256_same={same_sha}\t"
              f"new_endpoint_outcomes={len(new['endpoint_outcomes'])}\t"
              f"summary={old['directional_summary']}->{new['directional_summary']}\t{'; '.join(problems) or 'OK'}")
        bad += bool(problems)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
