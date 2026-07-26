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
import sys
from pathlib import Path
from typing import Any

MANIFEST_DIR = "disease-models/{disease}/research/deepdive_manifests"

# A waiver must be an argument, not a shrug. Short strings like "n/a" or "not relevant"
# are how a checklist dies.
MIN_WAIVER_CHARS = 40
MIN_REASON_CHARS = 20

SECTIONS = ("group_assessment", "field_density", "multihop", "corpus_crossquery", "retraction_check")
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
    if waiver is None:
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
