#!/usr/bin/env python3
"""Does the registry's declared locator count match the manifest it names?

🔴 WHY THIS EXISTS, and it is a measurement rather than a worry.

On 2026-09-21 a scientist checked four `paper_registry_current.md` records against the
manifests on disk and found three wrong. The full sweep run the same hour found **16 of 34
declarations wrong**, and the pattern is the finding:

    EVERY ONE OF THE SIXTEEN UNDERSTATES THE MANIFEST. Not one overstates.
    Deltas run +2 to +27 (PMID 38499540 declared 7, manifest holds 34).

Random transcription error produces both directions. One direction means a systematic
cause, and the direction rules out the frightening reading: the registry is not claiming
evidence it does not have, it is **failing to claim evidence it does have**. The counts
were true when written and were never re-derived as their manifests grew — a locator count
is a *measurement of another file*, and this repository already knows that a measurement
copied by hand decays while the thing it measures moves on.

Two of the wrong records carry, in their own text, the sentence *"declaration reconciled
from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001)"* — **the
batch that reconciled those declarations left both counts wrong.** A reconciliation that
does not re-derive is a restatement.

One further cause is proven and worth naming, because two independent actors hit it on the
same day: `verbatim_locators` is an **object**, not a list. `len()` on it returns **6** —
its keys (`waived`, `source_fulltext_indexed`, `source_fulltext_indexed_evidence`,
`abstract_anchoring_waived`, `surface_note`, `entries`) — while the locators live in
`entries`. Any count of 6 in this repository should be read twice.

WHAT THIS ASKS, and it is one mechanical question and no more:

    for every `deepdive_manifests/PMID<n>.json (N locators` declaration in the registry,
    does N equal `len(manifest["verbatim_locators"]["entries"])`?

WHAT THIS DOES NOT ASK. Whether the locators are good, whether they verify, whether the
reading was adequate, or whether the manifest should hold more. `deepdive_manifest.py`,
`locator_audit.py` and `dossier_quote_audit.py` own those questions. **This one only asks
whether a number in one file still describes another file.**

🔴 D-40, 2026-10-21 — THE SAME MISTAKE, MADE AGAIN, WHILE THIS TOOL WAS GREEN ON IT
-----------------------------------------------------------------------------------
Thirteen months of docstring above named the `len()` trap, and on 2026-10-20 a batch
integrator fell into it anyway: it re-measured two manifests with `len(d['verbatim_locators'])`,
got **6** for both, reported the candidate's declared 11 and 9 as wrong, and wrote 6 into two
`paper_registry_current.md` records. `BATCH_20261019_009` repaired them the next day. It was
caught only because the Orchestrator re-measured a number offered as a finding.

**This tool was not blind to the trap. It was blind to the SENTENCE.** `DECLARATION_RE` wants
the count as the first token inside the parenthesis — `(30 locators` — and both records write
`(schema v2, **11** persisted verbatim locators`. Neither was in its population of 34. The
check existed, was correct, ran, and could not see the defect it was built for.

So `--sweep` (below) parses the measured VARIETY of the wordings instead of one of them, and
reports **four distinct states**: agrees · disagrees · manifest absent · **unparsed**. The
fourth is the lesson of D-40 in the shape of an output: a sentence this parser cannot read is
a state of its own, never a clean one, and never silence.

It is a RATCHET, not a gate. `--sweep` exits non-zero only above the baselines measured on
2026-10-21 (`BASELINE_DISAGREEMENTS`, `BASELINE_UNPARSED`, `BASELINE_MANIFEST_ABSENT`), which
only ever come down. REPAIR IS NOT THIS TOOL'S ACT: a registry sentence moves only through
`BATCH_COMMIT`, by the integrator.

    python3 framework/scripts/locator_count_crosscheck.py .            # the narrow 34
    python3 framework/scripts/locator_count_crosscheck.py . --sweep    # the wide parse + ratchet
    python3 framework/scripts/locator_count_crosscheck.py . --depth    # receipt/depth drift (N10)

Exit codes: 0 every declaration matches (`--sweep`: at or below baseline) · 1 at least one
mismatch (`--sweep`: above a baseline) · 2 usage/IO error, or a scan that parsed nothing.
Read-only: it modifies nothing, ever.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REGISTRY = "disease-models/{disease}/registries/paper_registry_current.md"
MANIFEST_DIR = "disease-models/{disease}/research/deepdive_manifests"

# `deepdive_manifests/PMID12345678.json` optionally in backticks, then `(N locators`.
# Anchored on the manifest path so a bare "(7 locators" in prose is never mistaken for a
# declaration about a specific file — the defect this tool reports is a broken *link*
# between two named artefacts, not a loose number.
#
# 🔴 KEPT, AND NO LONGER THE ONLY PATTERN (D-40, 2026-10-21). This one requires the count to
# be the FIRST token inside the parenthesis, and the registry does not write it that way any
# more: `… .json` (schema v2, **11** persisted verbatim locators, …)` is invisible to it, and
# those were exactly the two records the D-40 defect was written into. It is retained because
# the 34 declarations it reaches are a measured, reproducible subset and
# `test_locator_count_crosscheck` pins them; `ASSERTION_RE` below is what the sweep now uses.
DECLARATION_RE = re.compile(
    r"deepdive_manifests/PMID(?P<pmid>\d{6,8})\.json`?\s*\(\s*(?P<count>\d+)\s+locators",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------------------
# 🔴 THE WIDER SWEEP (D-40). Measured variety first, pattern second.
# ---------------------------------------------------------------------------------------
# The registry asserts a locator count in at least these wordings, all live on 2026-10-21:
#
#     (30 locators, schema v2, 3 declared gaps)          the shape DECLARATION_RE knows
#     (schema v2, **11** persisted verbatim locators,    D-40's own shape: count not first
#     (9 verbatim locators, PASS with artefact verification)
#     (6 locator su pagina resa, validatore PASS)        Italian, singular, no plural `s`
#     `… .json`, **7** verbatim locators — 5 persisted   count after the path, no parenthesis
#     20 locator verificati in `deepdive_manifests/…`    count BEFORE the path
#     manifest schema-v2 con **32 locator** verificati   count with NO manifest path at all
#
# So the number may be bold, singular, Italian, before or after the path, inside or outside a
# parenthesis, and separated from the path by prose. The last line above names no file, and a
# pattern that guessed a file for it would invent the link it exists to check: that is the
# UNPARSED state, and it is reported, never counted clean.
ASSERTION_RE = re.compile(
    r"(?:\*\*)?(?P<count>\d{1,3})(?:\*\*)?\s+"
    r"(?:persisted\s+|verificati\s+|persistiti\s+)?(?:verbatim\s+)?"
    r"locator(?:s|i)?\b",
    re.IGNORECASE,
)

MANIFEST_RE = re.compile(r"deepdive_manifests/PMID(?P<pmid>\d{6,9})\.json")

# A number that belongs to a NOUN is not a count of locators. "the only Figure 3 locator",
# "entries 6 and 7", "Table 2 locator" — the number names the thing, not the quantity. Live
# example: `paper_registry_current.md` line 7333 writes *"the only Figure 3 locator"*, which a
# bare `\d+ locator` reads as an assertion of three.
COUNTED_NOUN_BEFORE = re.compile(
    r"(?:fig(?:ure|\.)?|table|tabella|entry|entries|panel|pannello|page|pagina|p\.|pp\.|"
    r"exon|intron|pmid|pmc|supplementary|§)\s*$",
    re.IGNORECASE,
)

# A quantity that is explicitly a PART of the total is not the total.
SUBSET_BEFORE = re.compile(
    r"\b(?:first|last|other|another|further|remaining|additional|new|only|of\s+which|"
    r"altri|altre|primi|prime|ultimi|restanti|nuovi)\s+$",
    re.IGNORECASE,
)

# A count the registry quotes in order to RETIRE it. Both D-40 repairs read
# `[corrected 2026-10-21 from «6 persisted verbatim locators» by BATCH_20261019_009]`: the
# superseded figure is still on the line, verbatim, inside guillemets. Verifying it against
# the manifest would report a disagreement the registry has already resolved in writing.
QUOTE_OPEN, QUOTE_CLOSE = "«", "»"

# What may NOT sit between a count and the manifest path it is attributed to. Each of these
# closes the clause: past one of them the number and the path are two different statements.
# This is what keeps line 7333's *"checked directly against this paper's 38 locators"* from
# being attributed to the erratum manifest named in the parenthesis before it.
ATTRIBUTION_BARRIERS = (";", "—", ")", "]", "[", QUOTE_OPEN, QUOTE_CLOSE, ". ")

#: 🟢 ZERO since `BATCH_20261019_011` (2026-10-21). Measured by this tool's own `--sweep`
#: after that batch: **72 assertions reached**, 17 excluded (1 subset mention, 16 retired
#: quotations), 55 in the four states — **50 agree, 0 disagree, 0 manifest absent, 5
#: unparsed**.
#:
#: The 14 this constant used to hold were all repaired in that one batch, and the fourteen
#: records are named here so a future reader can see which population the zero was measured
#: over: PMID 42397075 (TWICE — `PAPER 001` line 55 and `PAPER 094` line 7383, 30 → 44),
#: 33914858 (`PAPER 004`, 6 → 40), 34747138 (`PAPER 005`, 20 → 29), 36779245 (`PAPER 018`,
#: 30 → 39), 32581702 (`PAPER 020`, 21 → 25), 31340538 (`PAPER 021`, 11 → 15), 35328751
#: (`PAPER 023`, 7 → 28), 33612478 (`CORPUS-STUB-109`, 4 → 10), 39416860 (`PAPER 093`,
#: 11 → 17), 33255508 (`PAPER 095`, 8 → 14), 42589397 (`PAPER 118`, 7 → 10), 39952983
#: (`PAPER 135`, 14 → 21), 35460704 (`PAPER 156`, 6 → 11).
#:
#: 🔴 AND THE D-40 SIGNATURE WAS A FALSE POSITIVE ON BOTH ROWS IT FIRED ON — a correction to
#: this file's own earlier note, which read that 33914858 and 35460704 were *"the D-40
#: signature"* because each asserted exactly **6** against a 6-key mapping. The integrator of
#: `BATCH_20261019_011` did not take the label on trust: `git log` on each manifest shows
#: BOTH holding exactly **6 `entries`** at commit `28faaf0a` (2026-10-03), and the registry
#: sentences were written the same day in `59fba0bc`. Both counts were therefore DERIVED
#: CORRECTLY and merely went stale. **All fourteen were stale totals; none was a
#: mis-measurement.** The signature is a heuristic over a coincidence — `len(entries)` is
#: free to equal the key count — so it is a hint to re-derive, never a finding. Reading it as
#: a finding would have produced the mirror image of D-40: a repair note asserting that a
#: true sentence had never been true.
#:
#: Lowering this number is the only direction it moves. It is now zero, so any disagreement
#: at all is a NEW one and this ratchet goes red on it.
BASELINE_DISAGREEMENTS = 0
#: Five, and each is a sentence that asserts a count while naming no manifest in its clause:
#: three 2026-08 Italian records written before the path was part of the sentence (lines 6856,
#: 6880, 6905, *"manifest schema-v2 con N locator verificati"*) and two on line 7333, where the
#: paper's own 38 locators are discussed beside an ERRATUM's manifest — attributing them to the
#: nearest path would have invented the very link this tool exists to check. Also a ceiling.
#:
#: 🔵 RE-MEASURED AND DELIBERATELY NOT LOWERED by `BATCH_20261019_011` (2026-10-21), which
#: lowered `BASELINE_DISAGREEMENTS` to 0 in the same commit. The five are unchanged because
#: none of them is a count DISAGREEMENT to repair: three are 2026-08 Italian records whose
#: sentence names no manifest, and two are line 7333's, where the paper's own total is
#: discussed beside an ERRATUM's manifest — the case the brief for that batch singled out as
#: unrepairable honestly, because writing the paper's figure next to the erratum's path would
#: assert exactly the link this tool refuses to guess. A ceiling that did not move is
#: reported as not having moved, not quietly re-derived downward.
BASELINE_UNPARSED = 5
#: Zero, and it must stay zero: a declaration whose manifest is gone is never clean.
BASELINE_MANIFEST_ABSENT = 0

STATES = ("agrees", "disagrees", "manifest_absent", "unparsed")


def manifest_entry_count(manifest: dict) -> int | None:
    """How many locators the manifest actually holds.

    Tolerates both shapes deliberately. The current schema puts the locators under
    `verbatim_locators.entries`; older manifests carry `verbatim_locators` as a bare list.
    A tool that understood only one shape would report the other as zero, and a zero from a
    parser is not evidence.
    """
    locators = manifest.get("verbatim_locators")
    if isinstance(locators, dict):
        entries = locators.get("entries")
        return len(entries) if isinstance(entries, list) else None
    if isinstance(locators, list):
        return len(locators)
    return None


def manifest_key_count(manifest: dict) -> int | None:
    """`len(manifest["verbatim_locators"])` — THE WRONG ANSWER, derived on purpose.

    D-40 (2026-10-21): an integrator re-measured two manifests with `len(d['verbatim_locators'])`
    and got 6 for both, because the key holds a MAPPING whose six keys are `waived`,
    `source_fulltext_indexed`, `source_fulltext_indexed_evidence`, `entries`, `note` and
    `artifact_locality_note`. The candidate's own counts, 11 and 9, were right.

    This tool derives the wrong number so that it can SAY SO: when a disagreeing assertion
    equals the key count, the registry's figure is not merely stale, it is the signature of
    that mistake, and the repair is a different one (re-derive, do not assume the manifest grew).
    """
    locators = manifest.get("verbatim_locators")
    return len(locators) if isinstance(locators, dict) else None


def load_manifests(root: Path, disease: str) -> dict[str, tuple[int | None, Path]]:
    out: dict[str, tuple[int | None, Path]] = {}
    directory = root / MANIFEST_DIR.format(disease=disease)
    if not directory.is_dir():
        return out
    for path in sorted(directory.glob("PMID*.json")):
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        pmid = str(manifest.get("pmid") or "")
        if pmid:
            out[pmid] = (manifest_entry_count(manifest), path)
    return out


def scan(text: str, manifests: dict[str, tuple[int | None, Path]]) -> list[dict]:
    findings = []
    for match in DECLARATION_RE.finditer(text):
        pmid = match.group("pmid")
        declared = int(match.group("count"))
        line = text.count("\n", 0, match.start()) + 1
        actual, path = manifests.get(pmid, (None, None))
        findings.append({
            "line": line,
            "pmid": pmid,
            "declared": declared,
            "actual": actual,
            "manifest": path.name if path else None,
            "state": (
                "no_manifest" if actual is None and path is None else
                "unreadable" if actual is None else
                "match" if declared == actual else "mismatch"
            ),
        })
    return findings


def _in_quotation(line: str, position: int) -> bool:
    """Is `position` inside a «…» quotation — a figure the registry quotes to retire it?"""
    opened = line.count(QUOTE_OPEN, 0, position)
    closed = line.count(QUOTE_CLOSE, 0, position)
    return opened > closed


def _clean_gap(line: str, start: int, end: int) -> bool:
    """Nothing between a count and a manifest path that closes the clause."""
    gap = line[start:end]
    return not any(barrier in gap for barrier in ATTRIBUTION_BARRIERS)


def sweep_line(line: str, number: int) -> list[dict]:
    """Every locator-count assertion on one registry line, with the manifest it is about.

    Returns one row per assertion. `pmid` is the manifest the count is attributed to, or ""
    when no manifest path sits in the same clause — the UNPARSED case, which is a state of
    this parser and never a state of the registry.
    """
    manifests = list(MANIFEST_RE.finditer(line))
    rows: list[dict] = []
    for match in ASSERTION_RE.finditer(line):
        before = line[:match.start()]
        quote = line[max(0, match.start() - 90):match.end() + 40].strip()
        if COUNTED_NOUN_BEFORE.search(before[-24:]):
            continue  # "the only Figure 3 locator" — the number names the thing
        if _in_quotation(line, match.start()):
            rows.append({"line": number, "excluded": "retired_quotation",
                         "declared": int(match.group("count")), "quote": quote})
            continue
        if SUBSET_BEFORE.search(before[-24:]):
            rows.append({"line": number, "excluded": "subset_mention",
                         "declared": int(match.group("count")), "quote": quote})
            continue
        best: tuple[int, str] | None = None
        for manifest in manifests:
            if manifest.end() <= match.start():
                if not _clean_gap(line, manifest.end(), match.start()):
                    continue
                distance = match.start() - manifest.end()
            elif manifest.start() >= match.end():
                if not _clean_gap(line, match.end(), manifest.start()):
                    continue
                distance = manifest.start() - match.end()
            else:
                continue
            if best is None or distance < best[0]:
                best = (distance, manifest.group("pmid"))
        rows.append({"line": number, "excluded": None,
                     "declared": int(match.group("count")),
                     "pmid": best[1] if best else "", "quote": quote})
    return rows


def load_key_counts(root: Path, disease: str) -> dict[str, int]:
    """Per PMID, the wrong number — see `manifest_key_count`."""
    out: dict[str, int] = {}
    directory = root / MANIFEST_DIR.format(disease=disease)
    if not directory.is_dir():
        return out
    for path in sorted(directory.glob("PMID*.json")):
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        pmid, keys = str(manifest.get("pmid") or ""), manifest_key_count(manifest)
        if pmid and keys is not None:
            out[pmid] = keys
    return out


def sweep(text: str, manifests: dict[str, tuple[int | None, Path]],
          key_counts: dict[str, int] | None = None) -> list[dict]:
    """The whole registry: one row per locator-count assertion, in file order."""
    key_counts = key_counts or {}
    findings: list[dict] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for row in sweep_line(line, number):
            if row["excluded"]:
                findings.append(row)
                continue
            pmid = row["pmid"]
            if not pmid:
                findings.append({**row, "state": "unparsed", "actual": None,
                                 "manifest": None})
                continue
            actual, path = manifests.get(pmid, (None, None))
            state = ("manifest_absent" if actual is None else
                     "agrees" if actual == row["declared"] else "disagrees")
            findings.append({**row, "actual": actual,
                             "manifest": path.name if path else None,
                             "state": state,
                             "key_count": key_counts.get(pmid),
                             "d40_signature": bool(
                                 state == "disagrees"
                                 and key_counts.get(pmid) == row["declared"])})
    return findings


def tally(findings: list[dict]) -> dict[str, int]:
    counts = {state: 0 for state in STATES}
    for finding in findings:
        if finding.get("excluded"):
            continue
        counts[finding["state"]] += 1
    return counts


DEPTH_LINE_RE = re.compile(r"^\*\*Evidence depth:\*\*(?P<body>.*)$", re.M)
RECEIPT_RE = re.compile(r"FTR-\d{8}-(?P<pmid>\d{6,9})-\d{2}")
DEPTH_WORDS = ("complete_fulltext_read", "partial_fulltext_read", "abstract_only",
               "metadata_only", "legacy_reconstruction")


def scan_depth(text: str, root: Path, disease: str) -> list[dict]:
    """Does each `**Evidence depth:**` line still describe its manifest and the ledger? (N10)

    BATCH_20261019_007 found eight older records whose depth line named a receipt the work
    manifest does not (mostly a later re-read). The decided semantics (Mirror B4): the
    manifest's `receipt` is the reading that PRODUCED it; a depth line may cite a later
    reading it reports, and then names both. So, per line naming a manifest or a receipt:

        receipt_differs   the line names receipts, none of them the manifest's producer
        unknown_receipt   the line names a receipt the ledger does not hold
        depth_differs     the line's depth word is not the strongest STANDING depth the
                          ledger holds for that PMID (either direction, both are reported)

    Report only — an edit to the registry is a BATCH_COMMIT act.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import fulltext_receipts as fr
    ledger = fr.default_ledger_path(root, disease)
    events = fr.load_ledger(ledger) if ledger.is_file() else []
    known = {str(e.get("event_id")) for e in events}
    strongest: dict[str, str] = {}
    for event in fr.active_receipts(events):
        pmid = str((event.get("study_id") or {}).get("pmid") or "")
        depth = str(event.get("evidence_depth") or "")
        if pmid and depth in fr.DEPTHS and (
                pmid not in strongest or fr.DEPTHS[depth] > fr.DEPTHS[strongest[pmid]]):
            strongest[pmid] = depth
    findings = []
    for match in DEPTH_LINE_RE.finditer(text):
        body = match.group("body")
        receipts_named = [m.group(0) for m in RECEIPT_RE.finditer(body)]
        manifest_pmids = re.findall(r"deepdive_manifests/PMID(\d{6,9})\.json", body)
        pmid = (manifest_pmids or [m.group("pmid") for m in RECEIPT_RE.finditer(body)] or [""])[0]
        if not pmid:
            continue
        line = text.count("\n", 0, match.start()) + 1
        problems = []
        manifest_file = root / MANIFEST_DIR.format(disease=disease) / f"PMID{pmid}.json"
        producer = ""
        if manifest_file.is_file():
            try:
                producer = str(json.loads(manifest_file.read_text(encoding="utf-8"))
                               .get("receipt") or "")
            except (OSError, ValueError):
                producer = ""
        if receipts_named and producer and producer not in receipts_named:
            problems.append(f"receipt_differs: line names {', '.join(receipts_named)}; "
                            f"the manifest was produced by {producer}")
        unknown = [r for r in receipts_named if events and r not in known]
        if unknown:
            problems.append(f"unknown_receipt: {', '.join(unknown)}")
        declared = next((w for w in re.findall(r"`([a-z_]+)`", body) if w in DEPTH_WORDS), "")
        if declared and pmid in strongest and declared != strongest[pmid]:
            problems.append(f"depth_differs: line says {declared}, the ledger's strongest "
                            f"standing reading is {strongest[pmid]}")
        findings.append({"line": line, "pmid": pmid, "problems": problems})
    return findings


def report_sweep(args, registry: Path) -> int:
    """`--sweep`: the four states, the two excluded populations, and the ratchet.

    A RATCHET, NOT A GATE (`harness_development_principles.md` principle 3). It runs in under
    a second, waits on nobody and exits non-zero only ABOVE the ceiling measured on
    2026-10-21, so the known understatement tail stays visible and countable while a NEW
    disagreement is loud. Repairing a registry sentence is a `BATCH_COMMIT` act that belongs
    to the integrator; a suite that went red the day one of them was repaired would be a gate
    on scientific work, which is why the ceiling is a ≤ and not an =, and why a ceiling with
    headroom prints its own instruction to come down.
    """
    manifests = load_manifests(args.root, args.disease)
    findings = sweep(registry.read_text(encoding="utf-8"), manifests,
                     load_key_counts(args.root, args.disease))
    counts = tally(findings)
    ceiling = (BASELINE_DISAGREEMENTS if args.max_disagreements is None
               else args.max_disagreements)

    if args.json:
        print(json.dumps({"ceiling": ceiling, "counts": counts,
                          "baseline_unparsed": BASELINE_UNPARSED,
                          "findings": findings}, indent=2))
    else:
        for finding in findings:
            if finding.get("excluded"):
                continue
            where = f"{registry.name}:{finding['line']}"
            if finding["state"] == "disagrees":
                delta = finding["actual"] - finding["declared"]
                mark = (" 🔴 D-40 SIGNATURE: the asserted figure equals "
                        f"len(verbatim_locators) = {finding['key_count']}, the MAPPING's key "
                        "count — not a stale total but a mis-measurement"
                        if finding["d40_signature"] else "")
                print(f"  [DISAGREES] {where} — PMID {finding['pmid']}: the registry asserts "
                      f"{finding['declared']}, {finding['manifest']} holds "
                      f"{finding['actual']} ({delta:+d}){mark}")
            elif finding["state"] == "manifest_absent":
                print(f"  [MANIFEST ABSENT] {where} — PMID {finding['pmid']}: asserts "
                      f"{finding['declared']} locators, manifest absent or unreadable — "
                      f"NOT counted clean")
            elif finding["state"] == "unparsed":
                print(f"  [UNPARSED] {where} — asserts {finding['declared']} locators and "
                      f"names no manifest in the clause: …{finding['quote']}…")
        excluded = [f for f in findings if f.get("excluded")]
        for finding in excluded:
            print(f"  [excluded: {finding['excluded']}] {registry.name}:{finding['line']} — "
                  f"{finding['declared']}: …{finding['quote']}…")

        total = sum(counts.values())
        print(f"\nassertions reached: {total + len(excluded)} "
              f"({len(excluded)} excluded as subset mentions or retired quotations)")
        print(f"agrees: {counts['agrees']} | disagrees: {counts['disagrees']} "
              f"(ceiling {ceiling}) | manifest absent: {counts['manifest_absent']} | "
              f"unparsed: {counts['unparsed']} (declared {BASELINE_UNPARSED})")
        if not total:
            print("NO ASSERTIONS PARSED — a FAILURE of the scan, not a clean registry.")
            return 2
        if counts["disagrees"] < ceiling:
            print(f"🟢 RATCHET HAS HEADROOM: lower BASELINE_DISAGREEMENTS to "
                  f"{counts['disagrees']}. A ceiling only ever comes down.")
        if counts["unparsed"] > BASELINE_UNPARSED:
            print(f"🔴 A NEW UNPARSED ASSERTION: the wordings moved and the pattern did not "
                  f"follow. An unparsed sentence is not a clean one.")
        if counts["disagrees"] > ceiling or counts["unparsed"] > BASELINE_UNPARSED \
                or counts["manifest_absent"] > BASELINE_MANIFEST_ABSENT:
            print("VERDICT: ABOVE BASELINE — re-derive from the manifests; do not retype. "
                  "A registry sentence moves only through BATCH_COMMIT.")
            return 1
        print("VERDICT: AT OR BELOW BASELINE.")
        return 0

    if not sum(counts.values()):
        return 2
    return 1 if (counts["disagrees"] > ceiling
                 or counts["unparsed"] > BASELINE_UNPARSED
                 or counts["manifest_absent"] > BASELINE_MANIFEST_ABSENT) else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--depth", action="store_true",
                        help="check the `**Evidence depth:**` lines against manifest and "
                             "ledger instead of the locator counts (N10, 2026-10-20)")
    parser.add_argument("--sweep", action="store_true",
                        help="the wider parse (D-40): every count assertion in any wording, "
                             "four states — agrees / disagrees / manifest absent / unparsed")
    parser.add_argument("--max-disagreements", type=int, default=None,
                        help=f"ceiling for --sweep (default {BASELINE_DISAGREEMENTS}, "
                             "the measured tail; lowering it is the only direction)")
    args = parser.parse_args(argv)

    registry = args.root / REGISTRY.format(disease=args.disease)
    if not registry.exists():
        print(f"ERROR: {registry} not found", file=sys.stderr)
        return 2

    if args.sweep:
        return report_sweep(args, registry)

    if args.depth:
        rows = scan_depth(registry.read_text(encoding="utf-8"), args.root, args.disease)
        drift = [r for r in rows if r["problems"]]
        if args.json:
            print(json.dumps(drift, indent=2))
        else:
            for row in drift:
                for problem in row["problems"]:
                    print(f"  [DRIFT] {registry.name}:{row['line']} — PMID {row['pmid']}: {problem}")
            print(f"\ndepth lines checked: {len(rows)} | drifting: {len(drift)}")
            if not rows:
                print("NO DEPTH LINES FOUND — a failure of the scan, not a clean registry.")
        return 2 if not rows else (1 if drift else 0)

    manifests = load_manifests(args.root, args.disease)
    findings = scan(registry.read_text(encoding="utf-8"), manifests)

    if args.json:
        print(json.dumps(findings, indent=2))
        return 1 if any(f["state"] == "mismatch" for f in findings) else 0

    mismatches = [f for f in findings if f["state"] == "mismatch"]
    matches = [f for f in findings if f["state"] == "match"]
    missing = [f for f in findings if f["state"] in ("no_manifest", "unreadable")]

    if not findings:
        # Anti-vacuity. A guard whose population is empty passes by agreeing with nothing,
        # and this file's whole value is that it looked at something.
        print("NO DECLARATIONS FOUND — this is a FAILURE of the scan, not a clean registry. "
              "The declaration format has changed or the registry moved.")
        return 2

    for f in sorted(mismatches, key=lambda f: f["line"]):
        delta = f["actual"] - f["declared"]
        print(f"  [MISMATCH] {registry.name}:{f['line']} — PMID {f['pmid']}: "
              f"declared {f['declared']}, manifest holds {f['actual']} ({delta:+d})")
    for f in sorted(missing, key=lambda f: f["line"]):
        print(f"  [NO MANIFEST] {registry.name}:{f['line']} — PMID {f['pmid']}: "
              f"declares {f['declared']} locators, manifest absent or unreadable")

    print(f"\ndeclarations: {len(findings)} | match: {len(matches)} | "
          f"mismatch: {len(mismatches)} | manifest absent: {len(missing)}")

    if mismatches:
        under = [f for f in mismatches if f["actual"] > f["declared"]]
        over = [f for f in mismatches if f["actual"] < f["declared"]]
        print(f"direction: {len(under)} understate the manifest, {len(over)} overstate it.")
        if over:
            print("🔴 An OVERSTATEMENT is the serious direction: the registry claims evidence "
                  "depth the manifest does not hold. Treat it before any understatement.")
        else:
            print("Every mismatch understates. The registry is failing to claim evidence it "
                  "has — which is the benign direction, and still a false number in a "
                  "canonical file.")
        print("VERDICT: MISMATCH — re-derive from the manifests; do not retype.")
        return 1

    print("VERDICT: OK — every declared locator count matches its manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
