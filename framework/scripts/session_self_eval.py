#!/usr/bin/env python3
"""Post-batch self-evaluation gate.

A session can satisfy every existing check and still fail at the thing the system
exists for: a paper read cover to cover that leaves no trace anyone will ever find
again. `legend_lint.py` validates the state that *is* written; the full-text receipt
ledger proves a paper was *read*. Nothing until now compared the two — so a complete
read could name outputs that were never created, and no tool would notice.

That is not hypothetical. On 2026-07-26 a receipt was persisted, hash-chained and
tail-anchored declaring `discovery ledger entries DISC-2026-07-26-A/B/C` and
`dismissal ledger entry DISM-2026-07-26-A`. None existed, and the ID scheme was not
even the one this repository uses. The receipt was immutable and wrong, inside the
one subsystem whose whole purpose is to be trustworthy.

This script closes that gap with executable checks. It deliberately does not
try to score analytical quality: the judgement questions live in
`framework/protocols/session_self_evaluation.md` and stay human.

Exit 0 = PASS, 1 = FAIL.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Files a paper must reach to count as landed. Generated views (batch_queue,
# coverage_report) are excluded on purpose: they are derived from the registries,
# so counting them would let a paper "land" in a file that merely reflects the
# ledger it failed to reach.
LANDING_FILES = (
    "disease-models/{disease}/research/discovery_ledger_current.md",
    "disease-models/{disease}/research/dismissal_ledger_current.md",
    "disease-models/{disease}/research/full_text_queue_current.md",
    "disease-models/{disease}/research/therapeutic_hypotheses_ledger_current.md",
    "disease-models/{disease}/registries/paper_registry_current.md",
    "disease-models/{disease}/registries/literature_tracking_log_current.md",
)

# An `outputs` entry may name a record ID. If it also names a file, the ID must be
# in that file; a bare ID is checked against every landing file.
# Every identifier family used by LANDING_FILES belongs here.  The registry paths were
# already searched, but their triage records (`CORPUS P333` / `LIT-0333`) were invisible to
# this predicate, so a complete read could be correctly attached to both registries and still
# be called an orphan.  One shared predicate keeps "which files count" and "which records in
# those files count" from silently describing different populations.
ID_PATTERN = re.compile(
    r"\b(DL-[A-Z]+-\d+|DIS-\d+|FT-\d+|CLAIM \d+|PAPER \d+|"
    r"CORPUS(?:-STUB-\d+| P\d+)|LIT-\d+|HYP-[\w-]+)\b"
)
MD_PATTERN = re.compile(r"([\w/.-]+\.md)")
HEADING_PATTERN = re.compile(r"(?m)^#{1,6}\s+")

# Files that *reason and decide* rather than record: metas, therapeutic strategies and the
# analysis layer. A PMID cited here is being used as SUPPORT for a conclusion. The registries
# and ledgers are deliberately excluded — recording a paper is not the same as leaning on it.
PREMISE_GLOBS = (
    "disease-models/{disease}/analysis/**/*.md",
    "disease-models/{disease}/therapeutics/*.md",
    "disease-models/{disease}/meta/*.md",
)
PMID_PATTERN = re.compile(r"\bPMID[:\s]*(\d{7,8})\b")
UNREAD_PREMISE_BASELINE = re.compile(r"(?m)^unread_premise_baseline:\s*(\d+)\s*$")


def unread_premises(root: Path, disease: str, receipts: list[dict]) -> dict[str, list[str]]:
    """PMIDs a reasoning file leans on that were never read and carry no declared debt.

    The asymmetry this closes: a paper can be load-bearing for a therapeutic design or a meta
    conclusion while nobody has ever opened it. On 2026-07-26, PMID 22193544 was a premise in
    five files, absent from the paper registry, unread — and every existing check passed. The
    failure is invisible by construction, because leaning on a paper writes nothing anywhere.

    Three things clear a citation, and only three: a persisted `complete_fulltext_read`
    receipt, a registry record that declares the full text reviewed, or an explicit entry in
    the full-text queue. The third is what keeps this honest rather than punitive — declared
    reading debt is legitimate work in progress. Silence is not.
    """
    read_pmids = {
        (receipt.get("study_id") or {}).get("pmid")
        for receipt in standing_reads(receipts)
        if receipt.get("evidence_depth") == "complete_fulltext_read"
    }
    registry = root / f"disease-models/{disease}/registries/paper_registry_current.md"
    queue = root / f"disease-models/{disease}/research/full_text_queue_current.md"
    registry_text = registry.read_text(encoding="utf-8") if registry.exists() else ""
    queue_text = queue.read_text(encoding="utf-8") if queue.exists() else ""

    cited: dict[str, set[str]] = {}
    for pattern in PREMISE_GLOBS:
        for path in sorted(root.glob(pattern.format(disease=disease))):
            for match in PMID_PATTERN.finditer(path.read_text(encoding="utf-8")):
                cited.setdefault(match.group(1), set()).add(path.name)

    unread: dict[str, list[str]] = {}
    for pmid, files in cited.items():
        if pmid in read_pmids or pmid in queue_text:
            continue
        blocks = [block for block in registry_text.split("## PAPER ") if pmid in block]
        if blocks and "full text reviewed" in blocks[0]:
            continue
        unread[pmid] = sorted(files)
    return unread


def load_receipts(ledger: Path) -> list[dict]:
    """Every event, invalidated ones included. History is history."""
    if not ledger.exists():
        return []
    return [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines() if line.strip()]


def standing_reads(receipts: list[dict]) -> list[dict]:
    """The events that still attest a reading.

    🔴 This file answered "what has been read?" by filtering raw events on `evidence_depth`,
    which honours no `receipt_invalidation` at all. `receipt_depth_index` and
    `coverage_report.py` both subtract withdrawn events; this one did not, so an invalidated
    `complete_fulltext_read` would still have cleared the unread-premise ratchet and still
    have demanded a work manifest. Nothing exploited it — the single live invalidation targets
    a `partial_fulltext_read` — but a check that disagrees with the ledger's own index is a
    check that will eventually be believed over it.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import fulltext_receipts

    return fulltext_receipts.active_receipts(receipts)


def resolve(root: Path, name: str, disease: str) -> Path | None:
    """Resolve a path that may be repo-relative or a bare basename."""
    direct = root / name
    if direct.exists():
        return direct
    for template in LANDING_FILES:
        candidate = root / template.format(disease=disease)
        if candidate.name == Path(name).name and candidate.exists():
            return candidate
    return None


def has_structured_landing(text: str, identities: list[str]) -> bool:
    """Require study identity and a real record ID in the same Markdown section.

    A PMID mentioned in a process note, declared gap or cross-reference is not a landing.
    Splitting at headings keeps the test format-agnostic while making incidental mentions
    unable to clear reading debt.
    """
    starts = [match.start() for match in HEADING_PATTERN.finditer(text)]
    if not starts:
        return False
    starts.append(len(text))
    for index in range(len(starts) - 1):
        section = text[starts[index]:starts[index + 1]]
        if ID_PATTERN.search(section) and any(identity in section for identity in identities):
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--disease", default="wwox")
    args = parser.parse_args()
    root = Path(args.workspace).resolve()
    disease = args.disease

    ledger = root / f"disease-models/{disease}/registries/fulltext_read_receipts.jsonl"
    receipts = load_receipts(ledger)
    complete = [r for r in standing_reads(receipts)
                if r.get("evidence_depth") == "complete_fulltext_read"]
    corrected_events = {
        r.get("prior_receipt") for r in receipts
        if r.get("reread_reason") == "receipt_correction"
    }
    active_complete = [r for r in complete if r.get("event_id") not in corrected_events]

    landing_text = ""
    for template in LANDING_FILES:
        path = root / template.format(disease=disease)
        if path.exists():
            landing_text += path.read_text(encoding="utf-8")

    failures: list[str] = []

    # A — a completely read paper must be findable somewhere a human will look.
    for receipt in active_complete:
        pmid = (receipt.get("study_id") or {}).get("pmid")
        doi = (receipt.get("study_id") or {}).get("doi")
        identities = [value for value in (pmid, doi) if value]
        if identities and has_structured_landing(landing_text, identities):
            continue
        failures.append(
            f"ORPHAN_COMPLETE_READ: {receipt.get('event_id')} (PMID {pmid}) is recorded as "
            "completely read but appears in no structured ledger, queue or registry record."
        )

    # B and C — every output a receipt declares must actually exist.
    for receipt in active_complete:
        for output in receipt.get("outputs") or []:
            md = MD_PATTERN.search(output)
            target = resolve(root, md.group(1), disease) if md else None
            if md and target is None:
                failures.append(
                    f"UNRESOLVED_OUTPUT_FILE: {receipt.get('event_id')} declares "
                    f"'{output}' but {md.group(1)} does not exist."
                )
                continue
            if target is not None:
                target_text = target.read_text(encoding="utf-8")
                study = receipt.get("study_id") or {}
                identities = [
                    value for value in (
                        study.get("pmid"), study.get("doi"), receipt.get("event_id")
                    ) if value
                ]
                if identities and not any(value in target_text for value in identities):
                    failures.append(
                        f"OUTPUT_STUDY_MISMATCH: {receipt.get('event_id')} declares "
                        f"'{output}', but the file names none of its PMID, DOI or receipt ID. "
                        "The path may have collided with another study's output."
                    )
            for record_id in ID_PATTERN.findall(output):
                haystack = target.read_text(encoding="utf-8") if target else landing_text
                if record_id not in haystack:
                    where = md.group(1) if md else "any landing file"
                    failures.append(
                        f"UNRESOLVED_OUTPUT_ID: {receipt.get('event_id')} declares "
                        f"'{record_id}' but it is not present in {where}."
                    )

    # D — every complete read must carry a work manifest, so the steps that produce no
    # other artifact (group assessment, field density, multi-hop, corpus cross-query) are
    # either evidenced or explicitly refused. Without this the gate is blind to omission.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    declared_gaps: list[str] = []
    try:
        import deepdive_manifest
    except ImportError:  # pragma: no cover
        deepdive_manifest = None
        failures.append("MANIFEST_VALIDATOR_MISSING: deepdive_manifest.py is unavailable")
    if deepdive_manifest is not None:
        for pmid in sorted({(r.get("study_id") or {}).get("pmid") for r in complete} - {None}):
            errors, incomplete = deepdive_manifest.load_and_validate(root, disease, str(pmid))
            failures.extend(f"WORK_MANIFEST: PMID {pmid}: {error}" for error in errors)
            declared_gaps.extend(f"PMID {pmid}: {item}" for item in incomplete)

    # E — papers the reasoning layer LEANS ON but nobody read. Unlike A-D this is a debt
    # that predates any single session, so it is a ratchet, not a wall: the count may fall,
    # never rise. Blocking on the whole legacy backlog would only teach sessions to route
    # around the check; capping it makes every new unread premise a visible regression.
    warnings: list[str] = []
    unread = unread_premises(root, disease, receipts)
    manifest = root / "framework/state/state_manifest_current.md"
    baseline = None
    if manifest.exists():
        found = UNREAD_PREMISE_BASELINE.search(manifest.read_text(encoding="utf-8"))
        baseline = int(found.group(1)) if found else None
    if baseline is None:
        warnings.append(
            f"UNREAD_PREMISE_BASELINE_MISSING: {len(unread)} unread premise(s) found and no "
            "`unread_premise_baseline:` in the state manifest. Set it to ratchet the debt down."
        )
    elif len(unread) > baseline:
        failures.append(
            f"UNREAD_PREMISE: {len(unread)} reasoning-layer citations lack any read receipt, "
            f"registry full-text declaration or queue entry — above the baseline of {baseline}. "
            "A conclusion may not start leaning on a paper nobody opened."
        )
    for pmid, files in sorted(unread.items()):
        print(f"  [UNREAD PREMISE] PMID {pmid} cited in {', '.join(files)}")

    print(
        f"receipts: {len(receipts)} | complete_fulltext_events: {len(complete)} | "
        f"active_complete_reads: {len(active_complete)} | "
        f"unread_premises: {len(unread)}"
        + (f"/{baseline}" if baseline is not None else "")
    )
    for gap in declared_gaps:
        print(f"  [DECLARED GAP] {gap}")
    for warning in warnings:
        print(f"  [WARN_BUT_PROCEED] {warning}")
    if failures:
        print("\nVERDICT: FAIL")
        for failure in failures:
            print(f"  [BLOCK_BATCH_COMMIT] {failure}")
        print(
            "\nA receipt is a promise about what the reading produced. An unresolved "
            "promise is worse than no receipt: it reports coverage the system does not have."
        )
        return 1
    print("VERDICT: PASS — every complete read has landed and every declared output resolves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
