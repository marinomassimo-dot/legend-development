#!/usr/bin/env python3
"""ERRATUM SCOPE CHECK — does any locator stand on a panel its own erratum corrected?

## The defect this exists to remove

An erratum names the panels it corrects. A work manifest names the panels its locators stand
on. **Nothing in this repository has ever compared the two.**

Found twice, from both sides, and both times by hand:

- **2026-08-10**, reading `PMID 29724996`: the Author Correction `PMID 30470736` declares image
  duplication in *Fig 3A and D — H&E panels*. That reading checked by eye that its single
  Figure 3 locator reads panel **F**, and wrote: *"That is a fact about which panels I happened
  to use, not a safeguard: nothing in the pipeline checked the erratum against the locators,
  and had a locator sat on 3A it would have passed every gate."*
- **2026-09-09**, reading the erratum itself as its own assigned source: the same check, run
  again by hand, reached the same clean answer — and the same gap was still open.

A defect observed twice, recorded twice, and prevented zero times is not a known limitation.
It is an unimplemented check.

## What it does

For every deep-dive manifest whose `retraction_check` describes an erratum or correction, it
asks one question per locator: **does this locator's anchor name a figure panel the erratum
declares corrected?** Three outcomes, deliberately kept apart because they mean different
things:

- `REVIEW_REQUIRED` — a locator's anchor names a corrected panel. This is not an accusation;
  the locator may well have been read from the corrected version. It means *a human must say
  which version it was read from, in writing.*
- `CLEAR` — a scope is declared and no locator's anchor intersects it.
- `SCOPE_UNDECLARED` — an erratum is recorded in prose but no structured scope exists, so the
  question **cannot be answered**. Reported as loudly as a hit, because a check that silently
  skips what it cannot parse is worse than no check.

## Where the scope comes from, and why it is declared rather than parsed

The scope is read from `retraction_check.corrected_items`, a list of panel identifiers a
reading declares when it records an erratum:

    "retraction_check": {
      "corrected_items": ["Fig 3A", "Fig 3D"],
      ...
    }

🔴 **It is NOT parsed out of the prose, and that refusal is the design.** Erratum prose is free
text — *"Fig. 3a and d—panels that display H&E"*, *"Figures 3A and 3D"*, *"the H&E panels of
Fig 3"* — and a regex over it would be exactly the failure this repository has already paid
for: **a plausible predicate that answers a different question from the one you asked**, whose
output is well-formed whether or not it is right, and which fails *silently* in the quiet
direction. A missed panel would read as `CLEAR`.

So a manifest that records an erratum and declares no `corrected_items` is reported as
`SCOPE_UNDECLARED` rather than guessed at. Declaring two strings costs the reading seconds; a
wrong guess costs a false reassurance that nobody re-opens.

## What it refuses to do

It changes nothing and gates nothing by default. Panel matching is textual over the locator's
`anchor`, so it can only see what an anchor writes down: an anchor that says *"Figure 3,
panel F"* is matchable and one that says *"the histology"* is not. It reports its own blind
spot — locators on a figure surface whose anchor names no panel — as `ANCHOR_UNPARSEABLE`
instead of scoring them clean.

Usage:
    python3 framework/scripts/erratum_scope_check.py
    python3 framework/scripts/erratum_scope_check.py --disease wwox --pmid 29724996
    python3 framework/scripts/erratum_scope_check.py --fail-on-review
    python3 framework/scripts/erratum_scope_check.py --self-test
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Words that make a `retraction_check` block worth asking the question about at all. Kept
# deliberately wide: over-selecting costs a SCOPE_UNDECLARED line a human can dismiss in a
# second, while under-selecting hides the very manifests this tool exists for.
ERRATUM_WORDS = re.compile(r"\b(erratum|errata|correction|corrigend\w*)\b", re.I)

# "Fig 3A", "Figure 3a", "Fig. 3 A", "F3A" is NOT accepted — an identifier a human would not
# write is an identifier a human cannot check.
FIG_RE = re.compile(r"\b(supplement(?:al|ary)?|suppl?\.?|extended[ ]data)?\s*"
                    r"fig(?:ure)?s?\.?\s*(S?)(\d+)", re.I)

# 🔴 MAIN AND SUPPLEMENTARY FIGURES SHARE NUMBERING, AND CONFLATING THEM IS THIS TOOL'S MOST
# DANGEROUS FAILURE. Found on its first live run, against real data: the erratum of
# PMID 29724996 corrects MAIN Figure 3A, and this file's own reading anchors ten locators to
# "Supplemental Figure 3, panel A" — a completely different figure. The first version matched
# them and raised REVIEW_REQUIRED on a locator the erratum does not touch. A tool whose false
# positives land on the reader's own new work is a tool the reader switches off, so the
# namespace is part of the key rather than a note in the output.
# The house anchor style, which the first version of this file did not parse and its own
# self-test caught: "Figure 3, panel F" and "Figure 4, panels A, B and C".
PANELS_RE = re.compile(r"\s*,?\s*panels?\s+([A-Za-z](?:\s*(?:,|and|&|/|-)\s*[A-Za-z]\b)*)", re.I)
# Trailing "a and d" / "A/D" immediately after the number.
TRAIL_RE = re.compile(r"\s*([A-Za-z])\b((?:\s*(?:,|and|&|/)\s*[A-Za-z]\b)*)", re.I)
LETTER_RE = re.compile(r"[A-Za-z]")

# 🔴 Negation-aware SELECTION. The first corpus run of this file reported 59 manifests and
# every single one was a false positive: `retraction_check` blocks overwhelmingly say
# "no retraction, no expression of concern, NO ERRATUM", and matching the bare word treats a
# clean record as a pending one. 59 dismissible lines is not the safe direction — it is how a
# check teaches people to ignore it. So a mention governed by a negation within the same
# sentence is skipped, and the number skipped is REPORTED, never silently dropped.
NEGATION = {"no", "not", "none", "without", "nessun", "nessuna", "nessuno", "neither", "nor",
            "non", "zero"}

# 🔴 Which FIELDS of `retraction_check` may be selected on. `route` describes how the check was
# performed and legitimately contains the word "correction" — "local corpus record, corrections
# field (the harvest preserves PubMed correction links)" is a clean record that the first
# version selected as a pending erratum. Selecting on the FINDING rather than on the METHOD is
# the narrowing that removes that class, and it is a real distinction rather than a filter
# tuned until the number looked right.
SELECTABLE_FIELDS = ("result", "note", "notes", "detail")


def _is_negated(text: str, at: int) -> bool:
    """Is the erratum word at `at` governed by a negation earlier in its own sentence?"""
    before = text[max(0, at - 90):at]
    cut = max(before.rfind("."), before.rfind(";"), before.rfind("\n"))
    clause = before[cut + 1:]
    words = re.findall(r"[A-Za-z]+", clause.lower())
    return any(w in NEGATION for w in words[-6:])


def parse_panel(text: str) -> set[tuple[str, str | None]]:
    """Return {(figure_number, panel_letter_lowercased_or_None)} named anywhere in `text`."""
    found: set[tuple[str, str | None]] = set()
    text = text or ""
    for m in FIG_RE.finditer(text):
        supp = bool(m.group(1)) or m.group(2).upper() == "S"
        number = ("S" if supp else "") + m.group(3)
        rest = text[m.end():]
        letters: set[str] = set()
        pm = PANELS_RE.match(rest)
        tm = TRAIL_RE.match(rest)
        if pm:
            letters |= {c.lower() for c in LETTER_RE.findall(pm.group(1))}
        elif tm:
            letters |= {c.lower() for c in LETTER_RE.findall(tm.group(1) + (tm.group(2) or ""))}
        if letters:
            found |= {(number, c) for c in letters}
        else:
            found.add((number, None))
    return found


def intersects(scope: set[tuple[str, str | None]],
               anchor: set[tuple[str, str | None]]) -> list[str]:
    """Panels named by BOTH the erratum scope and the locator anchor.

    A scope entry with no panel letter ("Fig 3") matches any panel of that figure — an erratum
    that corrects a whole figure corrects every panel in it. An anchor with no letter
    ("Figure 3") against a lettered scope ("Fig 3A") is a HIT, not a miss: the anchor does not
    say which panel, so it cannot be cleared. Both asymmetries fail toward review.
    """
    hits: list[str] = []
    for s_num, s_letter in scope:
        for a_num, a_letter in anchor:
            if s_num != a_num:
                continue
            if s_letter is None or a_letter is None or s_letter == a_letter:
                hits.append(f"Fig {s_num}{(s_letter or a_letter or '').upper()}")
    return sorted(set(hits))


def check_manifest(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return {"manifest": str(path), "status": "UNREADABLE", "detail": str(exc)}

    rc = data.get("retraction_check") or {}
    blob = " ".join(str(rc.get(k, "")) for k in SELECTABLE_FIELDS)
    mentions = list(ERRATUM_WORDS.finditer(blob))
    if not mentions:
        return None  # the word never appears — nothing to ask
    affirmative = [m for m in mentions if not _is_negated(blob, m.start())]
    if not affirmative:
        # Every mention is a negation ("no erratum"). Counted, not silently dropped.
        return {"manifest": str(path), "pmid": str(data.get("pmid") or path.stem),
                "status": "NO_ERRATUM_RECORDED", "detail": "all mentions negated"}

    pmid = str(data.get("pmid") or path.stem)
    declared = rc.get("corrected_items")
    if declared is not None and not declared:
        # DECLARED EMPTY is not UNDECLARED. An erratum can genuinely touch no figure — the
        # erratum of PMID 38182577 corrects an author's name — and a reading that says so in
        # the schema has answered the question, not dodged it.
        return {"manifest": str(path), "pmid": pmid, "status": "CLEAR",
                "scope": [], "review": [], "anchor_unparseable": [],
                "locators": len(entries),
                "detail": "corrected_items declared empty: the erratum names no figure panel"}
    entries = ((data.get("verbatim_locators") or {}).get("entries")) or []

    if not declared:
        return {"manifest": str(path), "pmid": pmid, "status": "SCOPE_UNDECLARED",
                "detail": "retraction_check names an erratum but declares no `corrected_items`; "
                          "the question cannot be answered and is NOT assumed clean"}

    scope: set[tuple[str, str | None]] = set()
    for item in declared:
        scope |= parse_panel(str(item))
    if not scope:
        return {"manifest": str(path), "pmid": pmid, "status": "SCOPE_UNPARSEABLE",
                "detail": f"corrected_items {declared!r} names no recognisable figure panel"}

    review, unparseable = [], []
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            continue
        anchor = parse_panel(e.get("anchor") or "")
        if not anchor:
            if e.get("surface") == "figure":
                unparseable.append(i)
            continue
        hit = intersects(scope, anchor)
        if hit:
            review.append({"entry": f"entries[{i}]", "panels": hit,
                           "anchor": (e.get("anchor") or "")[:120]})

    return {"manifest": str(path), "pmid": pmid,
            "status": "REVIEW_REQUIRED" if review else "CLEAR",
            "scope": sorted(f"Fig {n}{(l or '').upper()}" for n, l in scope),
            "review": review, "anchor_unparseable": unparseable,
            "locators": len(entries)}


def self_test() -> int:
    """Prove the two asymmetries fail toward review, and that a miss is a miss."""
    cases = [
        ("lettered scope, same lettered anchor", {"Fig 3A"}, "Figure 3, panel A", True),
        ("lettered scope, different lettered anchor", {"Fig 3A"}, "Figure 3, panel F", False),
        ("lettered scope, unlettered anchor", {"Fig 3A"}, "Figure 3, histology", True),
        ("whole-figure scope, any panel", {"Fig 3"}, "Figure 3, panel F", True),
        ("different figure entirely", {"Fig 3A"}, "Figure 2, panel H", False),
        ("dotted and spaced spellings", {"Fig. 3 a"}, "Fig 3A, read at 400 dpi", True),
        # The namespace cases. Each one was a live false positive before it was a test.
        ("main scope must NOT match a supplementary anchor", {"Fig 3A"},
         "Supplemental Figure 3, panel A, read at 300 dpi", False),
        ("main scope must NOT match an unlettered supplementary anchor", {"Fig 3A"},
         "Supplement Figures Legend, 'Supplement Figure3.', sentence (A)", False),
        ("supplementary scope DOES match a supplementary anchor", {"Supplementary Fig 3A"},
         "Supplemental Figure 3, panel A", True),
        ("supplementary scope must NOT match a main anchor", {"Supplementary Fig 3A"},
         "Figure 3, panel A", False),
        ("S-prefixed spelling is supplementary", {"Fig S3"},
         "Supplemental Figure 3, panel A", True),
        ("multi-panel house style", {"Fig 4C"}, "Figure 4, panels A, B and C", True),
    ]
    failures = 0
    for name, scope_items, anchor, expect_hit in cases:
        scope: set[tuple[str, str | None]] = set()
        for s in scope_items:
            scope |= parse_panel(s)
        got = bool(intersects(scope, parse_panel(anchor)))
        ok = got == expect_hit
        failures += (not ok)
        print(f"  [{'ok' if ok else 'FAIL'}] {name}: expected hit={expect_hit}, got {got}")
    print(f"self-test: {len(cases) - failures}/{len(cases)} passed")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=".")
    ap.add_argument("--disease", default=None)
    ap.add_argument("--pmid", action="append", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fail-on-review", action="store_true",
                    help="exit non-zero on REVIEW_REQUIRED. SCOPE_UNDECLARED never exits "
                         "non-zero: it is a reading debt, not a defect in the reading.")
    ap.add_argument("--verbose", action="store_true",
                    help="also list manifests whose erratum mentions are all negated")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    root = Path(args.root).resolve()
    pattern = (f"disease-models/{args.disease}/research/deepdive_manifests/*.json"
               if args.disease else "disease-models/*/research/deepdive_manifests/*.json")
    results = []
    for path in sorted(root.glob(pattern)):
        if args.pmid and not any(p in path.stem for p in args.pmid):
            continue
        r = check_manifest(path)
        if r:
            results.append(r)

    if args.json:
        for r in results:
            print(json.dumps(r, ensure_ascii=False))
    else:
        for r in results:
            tag = r["status"]
            if tag == "REVIEW_REQUIRED":
                print(f"  [REVIEW]  PMID {r['pmid']}: {len(r['review'])} locator(s) stand on a "
                      f"corrected panel {r['scope']}")
                for hit in r["review"]:
                    print(f"              {hit['entry']} -> {hit['panels']} :: {hit['anchor']}")
            elif tag == "CLEAR":
                print(f"  [CLEAR]   PMID {r['pmid']}: no locator intersects {r['scope']} "
                      f"({r['locators']} locators)")
            elif tag == "NO_ERRATUM_RECORDED":
                # Suppressed from the listing, never from the count: 51 of 59 on the first
                # corpus run were clean records saying "no erratum", and printing them is how
                # a check trains its reader to skim past it. --verbose shows them.
                if args.verbose:
                    print(f"  [none]    PMID {r['pmid']}: {r.get('detail','')}")
            else:
                print(f"  [{tag}] PMID {r.get('pmid','?')}: {r.get('detail','')}")
            if r.get("anchor_unparseable"):
                print(f"              blind spot: figure locators whose anchor names no panel: "
                      f"{['entries[%d]' % i for i in r['anchor_unparseable']]}")

    counts: dict[str, int] = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("manifests with an erratum recorded: " + str(len(results)) + " | " +
          " | ".join(f"{k}: {v}" for k, v in sorted(counts.items())) or "none")

    if args.fail_on_review and counts.get("REVIEW_REQUIRED"):
        print("VERDICT: REVIEW_REQUIRED — a locator stands on a corrected panel; say in writing "
              "which version it was read from.")
        return 1
    print("VERDICT: REPORTED — this tool judges nothing; SCOPE_UNDECLARED means the question "
          "is still open, never that the answer is clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
