#!/usr/bin/env python3
"""Which records of the model use a study: the consumer count that reading queues are ordered by.

A unit is a claim, a section of the working or disease model, a lead, a hypothesis, a card, or a portfolio or investigation
row. A study is joined to a unit when the unit's text carries its PMID, its DOI or its registry id (`PAPER NNN`). The rule is
the one SCI froze for ADV-265 (route 2, and ADV-269/276/279 ordered on it), with two false joins removed (ADV-279):

* `PAPER NNN` is matched only as written by the registry, in capitals. A lower-case "paper 204" is a corpus placeholder
  number (P181 to P220) or a remark on a wrong pointer, and joined an unrelated PAPER 204.
* A `**Next-search agenda:**` line is a plan ("read next", "skip, already read"), not a use of the study.

Together the two removed 35 of 1,272 joins on 2026-11-25. Not covered: a portfolio or investigation row is one long line,
and a mention of the same kind inside it still counts.

Print-only: reads tracked files, writes nothing, gates nothing. A count says that a record names the study, not that the
record's statement depends on it: open the unit before choosing the paper.

    python3 framework/scripts/consumer_count.py 33958783 36979157     # these studies, with the units
    python3 framework/scripts/consumer_count.py                       # every study of the receipt ledger with a consumer
    python3 framework/scripts/consumer_count.py --old-rule 33958783   # the ADV-265 matching, to compare
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_root import RootError, add_root_argument, resolve_root_argument  # noqa: E402

MODEL = "disease-models/wwox"
LEDGER = f"{MODEL}/registries/fulltext_read_receipts.jsonl"
REGISTRIES = ("registries/paper_registry_current.md", "registries/literature_tracking_log_current.md")
SURFACES = (
    ("claim", "registries/claim_registry_current.md"), ("model", "registries/working_model_current.md"),
    ("model", "disease_model.md"), ("lead", "research/discovery_ledger_current.md"),
    ("hypothesis", "research/therapeutic_hypotheses_ledger_current.md"),
    ("card", "research/drug_repurposing/cards*/*.json"),
    ("portfolio", "research/drug_repurposing/research_portfolio.tsv"),
    ("ranking", "research/drug_repurposing/ranking*/investigations*.tsv"),
)
AGENDA_LINE = re.compile(r"(?im)^[ \t>*-]*\*{0,2}next[- ]search agenda\b.*$")


def registry_ids(root: Path) -> dict[str, set[str]]:
    """PMID or DOI -> the `PAPER NNN` ids whose own identifier lines carry it."""
    ids: dict[str, set[str]] = collections.defaultdict(set)
    for name in REGISTRIES:
        path = root / MODEL / name
        if not path.is_file():
            continue
        for unit in re.split(r"(?m)^(?=## )", path.read_text(encoding="utf-8", errors="replace")):
            head = re.match(r"## (PAPER \d+)", unit)
            if not head:
                continue
            own: set[str] = set()
            for line in unit.split("\n"):
                if "Identifier" in line:
                    own |= set(re.findall(r"(?:PMID\W{0,4}|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{6,8})", line))
                    own |= set(re.findall(r"(10\.\d{4,9}/[^\s)\]>*`|]+)", line))
            for value in own:
                ids[value.rstrip(".,;")].add(head.group(1))
    return dict(ids)


def units(root: Path, old_rule: bool = False) -> list[tuple[str, str, str, str]]:
    """(kind, path under the model, unit name, text) for every unit of every surface."""
    out: list[tuple[str, str, str, str]] = []
    base = root / MODEL
    for kind, pattern in SURFACES:
        for found in sorted(glob.glob(str(base / pattern))):
            text = Path(found).read_text(encoding="utf-8", errors="replace")
            rel = os.path.relpath(found, base)
            if found.endswith(".json"):
                out.append((kind, rel, os.path.basename(found).split("_")[0], text))
            elif found.endswith(".tsv"):
                out += [(kind, rel, line.split("\t")[0], line) for line in text.split("\n")[1:] if line]
            else:
                for part in re.split(r"(?m)^(?=#{2,4} )", text):
                    name = part.split("\n")[0].lstrip("# ")[:60] or "preamble"
                    out.append((kind, rel, name, part if old_rule else AGENDA_LINE.sub("", part)))
    return out


def pattern(key: str, ids: dict[str, set[str]], old_rule: bool = False) -> re.Pattern:
    """The study's search terms: identifiers ignore case, a registry id does not."""
    parts = []
    for term in sorted({key} | ids.get(key, set()), key=len, reverse=True):
        if re.fullmatch(r"\d{5,9}", term):
            parts.append(r"(?<![\d.])%s(?!\d)" % term)
        elif term.startswith("PAPER "):
            written = r"PAPER[ _#]?%s(?!\d)" % term.split()[1]
            parts.append(written if old_rule else f"(?-i:{written})")
        else:
            parts.append(re.escape(term))
    return re.compile("|".join(parts), re.I)


def consumers(keys, ids: dict[str, set[str]], all_units, old_rule: bool = False) -> dict[str, list[str]]:
    """key -> the sorted `kind:file:unit` names that carry it."""
    lowered = [(unit, unit[3].lower()) for unit in all_units]
    result = {}
    for key in keys:
        # cheap pre-filter: the identifier or the registry number must occur at all before the pattern runs
        needles = {key.lower()} | {term.split()[-1] for term in ids.get(key, ())}
        rx = pattern(key, ids, old_rule)
        result[key] = sorted({"%s:%s:%s" % (kind, rel.split("/")[-1], name)
                              for (kind, rel, name, body), low in lowered
                              if any(n in low for n in needles) and rx.search(body)})
    return result


def ledger_keys(root: Path) -> list[str]:
    keys = set()
    for line in (root / LEDGER).read_text(encoding="utf-8").splitlines():
        if line.strip():
            study = json.loads(line).get("study_id") or {}
            key = study.get("pmid") or study.get("doi")
            if key:
                keys.add(str(key))
    return sorted(keys)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Which records of the model use a study. Print-only.")
    add_root_argument(ap)
    ap.add_argument("keys", nargs="*", help="PMID or DOI (default: every study of the receipt ledger)")
    ap.add_argument("--old-rule", action="store_true", help="the ADV-265 matching, with its two false joins")
    args = ap.parse_args(argv)
    try:
        root = resolve_root_argument(getattr(args, "root", None))
    except RootError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    keys = args.keys or ledger_keys(root)
    found = consumers(keys, registry_ids(root), units(root, args.old_rule), args.old_rule)
    for key in sorted(keys, key=lambda k: (-len(found[k]), k)):
        if args.keys:
            print(f"{key}\t{len(found[key])}")
            for name in found[key]:
                print(f"\t{name}")
        elif found[key]:
            print(f"{key}\t{len(found[key])}\t{'; '.join(found[key])[:300]}")
    if not args.keys:
        print(f"{sum(bool(v) for v in found.values())} of {len(keys)} studies have a consumer; "
              f"{sum(map(len, found.values()))} joins", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
