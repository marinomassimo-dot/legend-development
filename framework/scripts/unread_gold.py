#!/usr/bin/env python3
"""unread_gold.py — find the gold already at home: high-relevance CORPUS placeholders never read.

Born from failure mode FM-011 (2026-07-09). Johannsen 2018 (CORPUS P383) contained the
experimental functional datum on a WWOX missense variant of interest (Q230P: normal transcript,
absent protein). It was on the registry as `Tier (PHASE 1): A`, `Relevance: HIGH`, and
`Status: screened — corpus placeholder` with a note "no deep-dive performed". Triage had
classified it CORRECTLY. It was a reading-priority error, not a triage error: LEGEND
reconstructed the same conclusion in-silico from scratch while the experimental proof was
already in the corpus.

Usage:
    python3 framework/scripts/unread_gold.py [workspace] [--all] [--mechanism] [--json]

Default: shows only CORPUS items with Tier A **and** Relevance HIGH/VERY HIGH never deep-dived.
These must be read BEFORE opening any new batch of studies.

No external dependencies. Read-only: it modifies no file.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import growth_anchors  # noqa: E402 - the single definition of a canonical record heading

# The public, disease-level paper registry (added once it holds public bibliographic state only).
REGISTRY = "disease-models/wwox/registries/paper_registry_current.md"

# A CORPUS record starts with "## CORPUS <id>" and ends at the next "## ".
#
# The convention comes from `growth_anchors`, never from a regex written here. The version
# this replaced — `^## (CORPUS[ -][^\n]+)$` — also matched the two `## CORPUS COVERAGE …`
# prose section headings, so this tool reported 358 corpus records where the registry holds
# 356, and two of its "unread gold" candidates were appendix preambles with empty tier,
# relevance and status. That inflated 358 is the number `CLAUDE.md` quotes.
BLOCK_RE = growth_anchors.HEADINGS["corpus"]

FIELD_RE = {
    "title": re.compile(r"^\*\*Full title:\*\*\s*(.+)$", re.M),
    "short": re.compile(r"^\*\*Short title:\*\*\s*(.+)$", re.M),
    "authors": re.compile(r"^\*\*Authors:\*\*\s*(.+)$", re.M),
    "year": re.compile(r"^\*\*Year:\*\*\s*(.+)$", re.M),
    "ident": re.compile(r"^\*\*Identifier:\*\*\s*(.+)$", re.M),
    "journal": re.compile(r"^\*\*Journal/source:\*\*\s*(.+)$", re.M),
    "tier": re.compile(r"^\*\*Tier \(PHASE 1\):\*\*\s*(.+)$", re.M),
    "status": re.compile(r"^\*\*Status:\*\*\s*(.+)$", re.M),
    "relevance": re.compile(r"^\*\*Relevance:\*\*\s*(.+)$", re.M),
    "pathway": re.compile(r"^\*\*Primary pathway:\*\*\s*(.+)$", re.M),
    "note": re.compile(r"^\*\*Note:\*\*\s*(.+)$", re.M),
}

# Ordering: higher = more urgent to read.
REL_RANK = {"VERY HIGH": 3, "HIGH": 2, "MODERATE": 1, "LOW": 0}
TIER_RANK = {"A": 3, "B": 2, "C": 1}


def parse_blocks(text: str) -> list[dict[str, str]]:
    marks = list(BLOCK_RE.finditer(text))
    out: list[dict[str, str]] = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = text[m.start():end]
        rec: dict[str, str] = {"id": m.group(1).strip()}
        for key, rx in FIELD_RE.items():
            hit = rx.search(body)
            rec[key] = hit.group(1).strip() if hit else ""
        out.append(rec)
    return out


def is_unread(rec: dict[str, str]) -> bool:
    """A placeholder never taken to deep-dive."""
    blob = (rec["status"] + " " + rec["note"]).lower()
    if "promoted" in rec["status"].lower():
        return False
    return "corpus placeholder" in blob or "no deep-dive performed" in blob


# `DOMAIN_PARITY` lens (2026-07-12). The mechanistically actionable allele of interest (Q230P)
# is a MISSENSE. WWOX missense variants are functionally characterized by ONCOLOGY labs, because
# WWOX was born a tumour suppressor. A triage that weights the neurological phenotype down-ranks
# exactly the papers that carry the mechanism of the allele. This lens hunts for MECHANISM and
# ignores tier, relevance and disease context entirely.
MECHANISM_RE = re.compile(
    r"\b(?:"
    r"missense|variant|mutant|mutation|p\.[A-Z][a-z]{2}\d+|[A-Z]\d{2,3}[A-Z]\b"      # allele
    r"|degrad|stabilit|stabili[sz]|turnover|half-life|proteasom|lysosom|autophag"    # protein fate
    r"|chaperon|hsc70|hsp70|misfold|ubiquitin|folding"                               # proteostasis
    r"|localiz|localis|traffick|binding|interact|partner|co-?ip|rescue"              # function
    r")", re.I,
)


def has_mechanism_signal(rec: dict[str, str]) -> bool:
    """Does the paper promise WWOX mechanism? The disease context is irrelevant."""
    blob = " ".join((rec.get("title", ""), rec.get("short", ""), rec.get("note", ""),
                     rec.get("pathway", "")))
    return bool(MECHANISM_RE.search(blob))


def is_retracted(rec: dict[str, str]) -> bool:
    blob = (rec["status"] + " " + rec.get("journal", "") + " " + rec["note"]).lower()
    return "retract" in blob


def score(rec: dict[str, str]) -> tuple[int, int]:
    rel = REL_RANK.get(rec["relevance"].upper().strip(), -1)
    tier = TIER_RANK.get(rec["tier"].upper().strip(), 0)
    return (rel, tier)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path, default=Path.cwd())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--all", action="store_true", help="show all unread placeholders")
    mode.add_argument(
        "--mechanism",
        action="store_true",
        help="apply the domain-parity mechanism lens",
    )
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    ws = args.workspace

    reg = ws / REGISTRY
    if not reg.exists():
        print(f"ERROR: {REGISTRY} not found under {ws}", file=sys.stderr)
        return 1

    records = [r for r in parse_blocks(reg.read_text(encoding="utf-8")) if is_unread(r)]

    if args.all:
        # --all means ALL. Full stop.
        # Until 2026-07-12 this line was `score(r)[0] >= 1`, which excluded the LOW items
        # (rank 0) and every record without an assigned relevance (rank -1) — i.e. the bulk
        # of the Tier-C "triage only" corpus. Zhang 2025 (Tier C, Relevance LOW) contained the
        # degradation route of the Q230P missense allele of interest, and was invisible even to
        # --all. The tool built to find unread gold could not find the biggest piece. See
        # CLAUDE.md, "parity of sources".
        hits = list(records)
    elif args.mechanism:
        # DOMAIN_PARITY lens: hunt MECHANISM, ignore tier, relevance and disease context.
        # Oncology is ~20 years ahead on WWOX mechanics.
        hits = [r for r in records if has_mechanism_signal(r)]
    else:
        hits = [
            r for r in records
            if r["tier"].upper().strip() == "A"
            and r["relevance"].upper().strip() in ("HIGH", "VERY HIGH")
        ]

    hits = [r for r in hits if not is_retracted(r)]
    hits.sort(key=score, reverse=True)

    if args.json:
        print(json.dumps(hits, indent=2, ensure_ascii=False))
        return 2 if hits else 0

    total_unread = len(records)
    if not hits:
        print(f"No unread Tier-A / Relevance-HIGH CORPUS. ({total_unread} total placeholders)")
        return 0

    print(f"\n🥇 UNREAD GOLD — {len(hits)} papers already on the registry, never deep-dived")
    print(f"   (out of {total_unread} total CORPUS placeholders)")
    print("   Read THESE before opening a new batch.\n")
    print(f"{'ID':<14} {'TIER':<5} {'RELEV':<10} {'YEAR':<6} TITLE")
    print("-" * 108)
    for r in hits:
        title = (r["title"] or r["short"] or "(no title)")[:56]
        print(f"{r['id']:<14} {r['tier']:<5} {r['relevance']:<10} {r['year'][:5]:<6} {title}")
        if r["ident"]:
            print(f"{'':<14} └─ {r['ident'][:88]}")
    print()
    print("Result: exit=2 (unread gold present).")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
