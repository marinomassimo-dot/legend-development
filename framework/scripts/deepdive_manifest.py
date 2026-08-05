#!/usr/bin/env python3
"""Deep-dive work manifest — turning omissions into artifacts.

The problem this exists for:

A gate can only see what was written. `session_self_eval.py` verifies that declared
outputs resolve and that a completely-read paper lands somewhere — but it is blind to the
steps that were simply never taken. On 2026-07-26 the research group was never assessed,
field density never measured, multi-hop never attempted and the corpus never cross-queried.
Every check in the repository passed. The session graded itself green. Those omissions
surfaced only because the operator asked.

**An obligation that produces no artifact cannot be enforced.** So each obligation is given
a required slot here. A step is done and carries evidence, or it is explicitly waived with a
reason someone can disagree with. What is impossible is silence.

The second half of the design lives in `fulltext_receipts.py`: a `complete_fulltext_read`
receipt is refused unless a valid manifest exists. The strongest claim the system can make
about a paper becomes unavailable until the work behind it exists. That is the difference
between reducing the gap and closing it.

Residual limit, stated rather than hidden: a manifest can be filled with hollow but
well-formed content. This design does not make that impossible — it makes it *reviewable*
instead of invisible, and it makes the honest path cheaper than the dishonest one. Numeric
evidence and resolved identifiers are harder to fabricate than an unchecked checkbox.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

MANIFEST_DIR = "disease-models/{disease}/research/deepdive_manifests"

# A waiver must be an argument, not a shrug. Short strings like "n/a" or "not relevant"
# are how a checklist dies.
MIN_WAIVER_CHARS = 40
MIN_REASON_CHARS = 20

SECTIONS = ("group_assessment", "field_density", "multihop", "corpus_crossquery",
            "retraction_check", "verbatim_locators")

# A quote shorter than this is not a locator, it is a gesture at one. The threshold is
# deliberately low: the cost of recording a real sentence during a reading is seconds,
# and the cost of recovering it afterwards is re-opening the PDF.
MIN_SNIPPET_CHARS = 30
# 🔴 The refusal lives here, in the gate, not only in a regression test. Reviewed 2026-08-05:
# a locator whose anchor named `files/corpus/*.jsonl` passed `validate()` with zero errors,
# because the only check was a test nobody is obliged to run before writing.
CORPUS_ARTEFACT = re.compile(
    r"files/corpus/|corpus_seed_pubmed|_corpus\.jsonl|corpus_abstracts", re.IGNORECASE)
# Which surface a quote was taken from. Declared per locator, because "which artefact was
# named" and "which surface was actually used" are different facts, and only the first was
# ever checked: an agent could read the abstract, write a plausible dossier, declare the XML,
# and pass. `body`/`table`/`supplement` are text and are machine-checkable against the
# artefact; `figure` is pixels and can only be attested; `abstract` is honest but weak.
LOCATOR_SURFACES = {"body", "figure", "table", "supplement", "abstract"}
TEXT_SURFACES = {"body", "table", "supplement"}
# An elided quote is verbatim in each half and not verbatim as a whole. LEGEND reads it fine;
# a validator doing exact substring matching against a cached source rejects it.
ELISION_RE = re.compile(r"\[\s*(?:…|\.\.\.)\s*\]|\s(?:…|\.\.\.)\s")
# What kind of evidence the group can produce, read off the Methods rather than the journal.
# A descriptive series and a wet-lab mechanism are not interchangeable support for the same
# claim, and this is a separate axis from how many papers the group has on the gene.
RESEARCH_TYPES = {
    "primary_disease_group",   # works on this disease, not merely on this gene
    "experimental_lab",        # wet-lab, generates mechanism
    "adjacent_method_expert",  # native expertise in the method, first encounter with the gene
    "descriptive_clinical",    # cohorts, series, case reports
    "computational",           # in-silico only
    "mixed",                   # state which halves in `weighting`
}


def manifest_path(root: Path, disease: str, pmid: str) -> Path:
    return root / MANIFEST_DIR.format(disease=disease) / f"PMID{pmid}.json"


def _waived(section: Any, name: str, errors: list[str]) -> bool:
    if not isinstance(section, dict):
        errors.append(f"{name}: must be an object")
        return True
    waiver = section.get("waived")
    # `false` is the idiomatic JSON for "I am NOT waiving this". Treating it as a malformed
    # waiver told the author to "state why" — pushing them to write a waiver reason for a
    # section they meant to fill — and returned True, so the section's real contents were
    # never validated at all. The message argued for the omission the gate exists to prevent.
    if waiver is None or waiver is False:
        return False
    if not isinstance(waiver, str) or len(waiver.strip()) < MIN_WAIVER_CHARS:
        errors.append(
            f"{name}: a waiver must state why in at least {MIN_WAIVER_CHARS} characters "
            f"— an unexplained waiver is the omission this manifest exists to prevent"
        )
    return True


def validate(manifest: Any) -> tuple[list[str], list[str]]:
    """Return (errors, incomplete_steps)."""
    errors: list[str] = []
    incomplete: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest must be a JSON object"], []

    for key in ("pmid", "receipt", "landing", "skills_considered", *SECTIONS):
        if key not in manifest:
            errors.append(f"missing required key: {key}")
    if errors:
        return errors, incomplete

    if not isinstance(manifest["landing"], list) or not manifest["landing"]:
        errors.append("landing: must list at least one record ID the reading produced")

    skills = manifest["skills_considered"]
    if not isinstance(skills, list) or not skills:
        errors.append("skills_considered: must be a non-empty list")
    else:
        for entry in skills:
            if not isinstance(entry, dict) or "skill" not in entry or "used" not in entry:
                errors.append("skills_considered: each entry needs 'skill' and 'used'")
                continue
            if not entry["used"]:
                reason = str(entry.get("reason", "")).strip()
                if len(reason) < MIN_REASON_CHARS:
                    errors.append(
                        f"skills_considered: declining '{entry['skill']}' needs a reason of "
                        f"at least {MIN_REASON_CHARS} characters"
                    )

    group = manifest["group_assessment"]
    if not _waived(group, "group_assessment", errors):
        for field in ("total_publications", "publications_on_gene"):
            if not isinstance(group.get(field), int):
                errors.append(f"group_assessment.{field}: must be an integer count")
        if not str(group.get("weighting", "")).strip():
            errors.append(
                "group_assessment.weighting: state how group experience reweights the "
                "observation versus the interpretation — they are not the same weight"
            )
        # Counting a group's papers says nothing about what KIND of evidence it can produce.
        # A descriptive cohort and a wet-lab mechanism are not the same support for the same
        # claim, and "primary for the gene" is not "primary for the disease": on 2026-07-26 a
        # co-author was the founder of the WWOX field and no group on the paper worked on the
        # disease. Both distinctions were available in the Methods and neither was recorded.
        research_type = str(group.get("research_type", "")).strip()
        if research_type not in RESEARCH_TYPES:
            errors.append(
                "group_assessment.research_type: classify the evidence the group can actually "
                f"produce — one of {sorted(RESEARCH_TYPES)} — inferred from the Methods, not "
                "from the journal"
            )
        if not isinstance(group.get("is_primary_group_for_disease"), bool):
            errors.append(
                "group_assessment.is_primary_group_for_disease: must be a boolean, and it is "
                "NOT the same question as being primary for the gene — record both"
            )

    density = manifest["field_density"]
    if not _waived(density, "field_density", errors):
        queries = density.get("queries")
        if not isinstance(queries, list) or not queries:
            errors.append("field_density.queries: at least one measured query is required")
        else:
            for query in queries:
                if not isinstance(query, dict) or not isinstance(query.get("count"), int):
                    errors.append("field_density.queries: each entry needs 'query' and integer 'count'")

    hop = manifest["multihop"]
    if not _waived(hop, "multihop", errors):
        refs = hop.get("gene_direct_refs_in_source")
        if not isinstance(refs, list):
            errors.append("multihop.gene_direct_refs_in_source: must be a list (empty is allowed)")
        else:
            resolved = hop.get("resolved") or []
            queued = hop.get("queued") or []
            if refs and not resolved and not queued:
                errors.append(
                    "multihop: the source cites gene-direct references that were neither "
                    "resolved nor queued — that is unrecorded reading debt"
                )
            if refs and not resolved:
                incomplete.append("multihop: references queued but not resolved")
        # Multi-hop starts at the reference list, so not enumerating it is not a small
        # omission: on 2026-07-26 a `complete_fulltext_read` never listed its 28 references,
        # and the list held a paper that qualified the reading's own inferences. An integer is
        # cheap to state and hard to fake, which is the whole point of a required slot.
        counted = hop.get("references_enumerated")
        if not isinstance(counted, int) or counted < 0:
            errors.append(
                "multihop.references_enumerated: state how many references the source's "
                "reference list actually holds (0 only if it genuinely has none) — multi-hop "
                "starts there, and declaring debt is not the same as enumerating it"
            )

    cross = manifest["corpus_crossquery"]
    if not _waived(cross, "corpus_crossquery", errors):
        if not isinstance(cross.get("hits"), int):
            errors.append("corpus_crossquery.hits: must be an integer")
        if not str(cross.get("query", "")).strip():
            errors.append("corpus_crossquery.query: name what was asked of the existing corpus")

    # A receipt attests that a document was read in full. It does not attest which sentence
    # supports which statement, and those are different facts. On 2026-08-04 an export to an
    # external knowledge base found that **no verbatim locator existed anywhere in the
    # canonical state**, across every complete read in the ledger: fourteen had to be
    # retro-extracted from two already-read papers, with targeted receipts, because the
    # reading had recorded conclusions and not quotations. Capturing the sentence while the
    # document is open costs seconds; recovering it later costs the reading again.
    locators = manifest["verbatim_locators"]
    if not _waived(locators, "verbatim_locators", errors):
        entries = locators.get("entries")
        if not isinstance(entries, list) or not entries:
            errors.append(
                "verbatim_locators.entries: record at least one verbatim quote with the "
                "proposition it supports — or waive the section with an argument if the "
                "reading supports no proposition at all"
            )
        else:
            for position, entry in enumerate(entries, 1):
                if not isinstance(entry, dict):
                    errors.append(f"verbatim_locators.entries[{position}]: must be an object")
                    continue
                if not str(entry.get("proposition", "")).strip():
                    errors.append(
                        f"verbatim_locators.entries[{position}].proposition: name what this "
                        "quote is evidence FOR — a quote with no proposition is decoration"
                    )
                snippet = str(entry.get("snippet", "")).strip()
                if len(snippet) < MIN_SNIPPET_CHARS:
                    errors.append(
                        f"verbatim_locators.entries[{position}].snippet: quote the source "
                        f"verbatim, at least {MIN_SNIPPET_CHARS} characters"
                    )
                if not str(entry.get("anchor", "")).strip():
                    errors.append(
                        f"verbatim_locators.entries[{position}].anchor: state where in the "
                        "source it is — section, figure or table. A quote nobody can find "
                        "again is not verifiable"
                    )
                if CORPUS_ARTEFACT.search(str(entry.get("anchor", ""))) or \
                        CORPUS_ARTEFACT.search(str(entry.get("artifact", ""))):
                    errors.append(
                        f"verbatim_locators.entries[{position}]: anchored to a bibliographic "
                        "corpus. An export of abstracts is not a document; anchor into the "
                        "paper — section, figure or table")
                surface = entry.get("surface")
                if surface is not None and surface not in LOCATOR_SURFACES:
                    errors.append(
                        f"verbatim_locators.entries[{position}].surface: must be one of "
                        f"{sorted(LOCATOR_SURFACES)}")
                if ELISION_RE.search(snippet):
                    errors.append(
                        f"verbatim_locators.entries[{position}].snippet: stitched quote. Two "
                        "spans joined by an ellipsis are each verbatim but the whole is not, "
                        "and an external validator matching exact substrings will reject it. "
                        "Split it into two entries, or quote one contiguous span"
                    )

        # A snippet is verified by matching it against a cached copy of the source. When the
        # source is not full-text indexed, the only text an external validator can hold is the
        # ABSTRACT — so a full-text quote is unverifiable there, however faithful it is.
        # Measured 2026-08-05: 2 of 8 read papers are abstract-only in Europe PMC, and 0 of 17
        # exportable snippets occur in an abstract. At batch scale that is a quarter of the
        # corpus discovering, after the reading, that its evidence cannot be carried out.
        # Declaring the index state costs one lookup while the paper is open; recovering an
        # abstract-anchored quote later costs the reading again.
        # The hole this closes: declared provenance is not the surface actually used. Reading
        # only the abstract, writing a plausible dossier and naming the XML as the source
        # passed every check, because nothing asked WHERE each quote came from.
        declared = [e.get("surface") for e in (entries or []) if isinstance(e, dict)]
        if entries and all(s is None for s in declared):
            incomplete.append(
                "verbatim_locators: no entry declares a `surface` (body/figure/table/"
                "supplement/abstract) — provenance is named but the surface used is not")
        elif entries and declared and all(s == "abstract" for s in declared if s):
            errors.append(
                "verbatim_locators: every locator is anchored to the abstract. Whatever "
                "artefact this manifest names, the abstract is the surface that was read, "
                "and that cannot support a complete full-text reading")

        indexed = locators.get("source_fulltext_indexed")
        if not _waived(locators, "verbatim_locators", []) and indexed is None:
            incomplete.append(
                "verbatim_locators.source_fulltext_indexed: not declared — state whether the "
                "source is full-text indexed (Europe PMC inEPMC/fullTextIdList), because it "
                "decides whether these quotes are externally verifiable")
        elif indexed is False:
            unverifiable = [position for position, entry in enumerate(entries or [], 1)
                            if isinstance(entry, dict)
                            and not str(entry.get("abstract_snippet", "")).strip()]
            reason = str(locators.get("abstract_anchoring_waived", "")).strip()
            if unverifiable and len(reason) < MIN_WAIVER_CHARS:
                errors.append(
                    "verbatim_locators: the source is not full-text indexed, so an external "
                    "validator can only see its abstract. Entries "
                    f"{unverifiable} carry no `abstract_snippet`. Add one where the abstract "
                    "supports the proposition, or set `abstract_anchoring_waived` to an "
                    f"argument of at least {MIN_WAIVER_CHARS} characters saying why the "
                    "abstract cannot carry them")

    retraction = manifest["retraction_check"]
    if not _waived(retraction, "retraction_check", errors):
        if not str(retraction.get("result", "")).strip():
            errors.append("retraction_check.result: state the outcome")

    for section in SECTIONS:
        if isinstance(manifest[section], dict) and manifest[section].get("waived"):
            incomplete.append(f"{section}: waived")

    return errors, incomplete


def load_and_validate(root: Path, disease: str, pmid: str) -> tuple[list[str], list[str]]:
    path = manifest_path(root, disease, pmid)
    if not path.exists():
        return [
            f"no deep-dive work manifest at {path.relative_to(root)} — a complete read "
            f"without one cannot show that the required steps were taken or refused"
        ], []
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.name}: invalid JSON ({exc})"], []
    return validate(manifest)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--pmid", required=True)
    args = parser.parse_args()
    errors, incomplete = load_and_validate(Path(args.workspace).resolve(), args.disease, args.pmid)
    for item in incomplete:
        print(f"  [INCOMPLETE] {item}")
    if errors:
        print("VERDICT: FAIL")
        for error in errors:
            print(f"  [BLOCK] {error}")
        return 1
    print(f"VERDICT: PASS — manifest for PMID {args.pmid} is complete ({len(incomplete)} declared gap(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
