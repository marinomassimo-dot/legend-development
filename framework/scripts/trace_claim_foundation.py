#!/usr/bin/env python3
"""Trace a canonical claim down to the species and reading depth of what it rests on.

Read-only. It writes nothing, and its output is a *view*, never a second source of truth.

## What it is for

On 2026-08-06 a premise that five canonical surfaces carried turned out to be inverted:
a mouse paper was credited with an epilepsy phenotype it never measured, because two
citation hops had converted an explicit negative about a **rat** into a positive assertion
about a **mouse**. Finding it took three sessions of chasing citations by hand.

The chain that produced that error is visible in structure, not only in prose: a claim
declares the model it is about, every paper declares the organism it studied, and the
registries record which papers a claim rests on. When those disagree, the claim is
carrying a phenotype across a species boundary that nobody declared.

## Why it refuses to read the narrative

After that investigation the claim's own `Evidence boundary` field was rewritten to
narrate the whole finding. A tool that reads that paragraph would "discover" the drift by
quoting a conclusion a human had already written — a passing test that measures nothing.

So the detector is restricted, deliberately and checkably, to declared fields:

* `Genotype/model relevance:` on the claim — the model the claim says it is about;
* `Model/species:` on each paper — the organism that paper studied;
* `Wikilinks:` / `Claim links:` — the edges between them.

`Summary`, `Note`, `Evidence boundary` and every other prose field are never consulted.
``--explain`` prints the exact fields used, so the restriction is auditable rather than
promised. A finding this tool reports is therefore derived from what the registries
*declare*, not from what someone already wrote down about the answer.

## Loss is named, never normalised

Following the export contract in `dismech_export_spec.md`, anything the tool cannot
represent is counted rather than quietly dropped, and the accounting identity
``emitted + lost == candidates`` is asserted on every run. A species value it does not
recognise becomes `SPECIES_UNNORMALISED`; it never becomes a guess.

## Coverage is always declared

Most integrated papers have no work manifest, so most evidence is not locator-backed. A
partial answer that looks complete is a scientific regression, so every trace reports the
manifest-backed share of what it just traversed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import growth_anchors  # noqa: E402 - the single definition of a canonical record heading

# Only these fields may inform a finding. The narrative fields of a record are excluded by
# construction: the claim under test had its own prose rewritten to describe the answer,
# so a detector allowed to read it would be scoring a human's conclusion as its own.
STRUCTURAL_FIELDS = {
    "claim": ("Genotype/model relevance", "Status", "Type", "Wikilinks", "Source"),
    "paper": ("Model/species", "Claim links", "Wikilinks", "Evidence depth", "Identifier"),
}

FIELD = re.compile(r"^\*\*([^:*]+):\*\*\s*(.*)$")
PAPER_REF = re.compile(r"\bPAPER\s+(\d{3})\b")
CLAIM_REF = re.compile(r"\bCLAIM\s+(\d{3})\b")
PMID = re.compile(r"\bPMID\s*(\d{7,8})\b")
PREMISE_TAG = re.compile(r"PREMISE:\s*([A-Z_]+)")

# Registry prose is bilingual by policy — CONTRIBUTING.md keeps entries in the language they
# were reasoned in — so the vocabulary has to be too. Matching is on whole words against the
# start of the declared value; an unrecognised value is a declared loss, never a guess.
ORGANISM = {
    "mouse": ("mouse", "mice", "murine", "murino", "murina", "topo", "topi"),
    "rat": ("rat", "rats", "ratto", "ratti"),
    "human": ("human", "umano", "umana", "patient", "paziente"),
    "zebrafish": ("zebrafish",),
    "drosophila": ("drosophila",),
}
# Two different kinds of non-organism marker, and conflating them cost a false positive.
#
# A SCOPE marker says the value describes the *breadth* of a record rather than an organism:
# `revisione mista (cellulare/animale/umano indiretti)` names three organisms precisely
# because it is a mixed review of all of them. Such a value can never be one side of a
# species comparison, whatever organism words it happens to contain.
#
# A SURFACE marker says a non-organism preparation is present alongside a real organism:
# `mouse (C57Bl/6J), STZ diabetes; 661W cone photoreceptor line` is a mouse study that also
# used a cell line. Letting a surface marker veto the organism would throw away a genuine
# species declaration.
#
# Both lists are bilingual. The first version had a bilingual organism vocabulary and an
# English-only non-organism one, so an Italian review was read as a human study — the same
# unevenness the repository keeps paying for, reproduced inside one function.
SCOPE_MARKERS = (
    "review", "revisione", "mixed", "mista", "misto", "not assessed",
    "non valutat", "indirect", "indirett", "meta-", "meta-coorte",
)
SURFACE_MARKERS = (
    "cell line", "linea cellulare", "in vitro", "in silico", "organoid",
    "biophysics", "biofisic", "computational", "ricombinant", "recombinant",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def split_records(text: str, convention: str) -> dict[str, str]:
    """Split a registry into ``{identifier: block}`` using the canonical heading matcher.

    The pattern comes from ``growth_anchors``, never from a regex written here: a consumer
    that invents its own record heading is how a record silently gets absorbed into its
    neighbour's body.
    """
    pattern = growth_anchors.HEADINGS[convention]
    matches = list(pattern.finditer(text))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[" ".join(match.group(1).split())] = text[match.end():end]
    return blocks


def declared_fields(block: str, kind: str) -> dict[str, str]:
    """Return only the declared fields this tool is allowed to see, in first-line form.

    A field's continuation lines are prose by definition — the point where an author starts
    explaining — so only the value on the field's own line is kept.
    """
    allowed = STRUCTURAL_FIELDS[kind]
    found: dict[str, str] = {}
    in_fence = False
    for line in block.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = FIELD.match(line.strip())
        if not match:
            continue
        name = match.group(1).strip()
        if name in allowed and name not in found:
            found[name] = match.group(2).strip()
    return found


def normalise_species(raw: str) -> tuple[str | None, str]:
    """Map a declared model/species value to a comparable organism.

    Returns ``(organism, state)``. ``state`` is one of ``organism``, ``multiple``,
    ``non_organism``, ``undeclared`` or ``unnormalised``; every state but the first is a
    loss the caller counts rather than a value it invents.

    🔴 ``multiple`` exists because the first version of this function did not have it, and
    the omission produced three false positives on its first run. Records here routinely
    declare more than one model in one field — ``ratto lde/lde (misure primarie) e topo
    Wwox-null (misura convergente)``, ``umano fetale + rat lde/lde + hNPC`` — and returning
    the first synonym that matched meant **dictionary iteration order chose the species**.
    A claim that honestly declares two models was then reported as crossing a boundary it
    had itself declared. A multi-organism value is not a species: it is a value this
    comparison cannot use, and saying so is the whole point of the loss ledger.
    """
    if not raw:
        return None, "undeclared"
    lowered = raw.casefold()
    if any(marker in lowered for marker in SCOPE_MARKERS):
        return None, "scope"
    words = set(re.findall(r"[a-zà-ÿ]+", lowered))
    matched = sorted(organism for organism, synonyms in ORGANISM.items()
                     if words & set(synonyms))
    if len(matched) > 1:
        return None, "multiple"
    if matched:
        return matched[0], "organism"
    if any(marker in lowered for marker in SURFACE_MARKERS):
        return None, "non_organism"
    return None, "unnormalised"


class Foundation:
    """The graph this tool derives, plus everything it could not represent."""

    def __init__(self, root: Path, disease: str) -> None:
        registries = root / "disease-models" / disease / "registries"
        self.claims_raw = split_records(read(registries / "claim_registry_current.md"), "claims")
        self.papers_raw = split_records(read(registries / "paper_registry_current.md"), "papers")
        self.manifest_dir = root / "disease-models" / disease / "research" / "deepdive_manifests"
        self.losses: list[dict[str, str]] = []
        self.candidates = 0

        self.claims = {cid: declared_fields(block, "claim")
                       for cid, block in self.claims_raw.items()}
        self.papers = {pid: declared_fields(block, "paper")
                       for pid, block in self.papers_raw.items()}
        self.premises = {cid: sorted(set(PREMISE_TAG.findall(block)))
                         for cid, block in self.claims_raw.items()}

        self.manifest_pmids = {
            match.group(1)
            for path in sorted(self.manifest_dir.glob("PMID*.json"))
            for match in [re.match(r"PMID(\d+)", path.name)] if match
        }

    def lose(self, state: str, subject: str, detail: str) -> None:
        self.losses.append({"state": state, "subject": subject, "detail": detail})

    def supporting_papers(self, claim_id: str) -> list[str]:
        """Papers a claim rests on, read from both directions of the declared edges."""
        number = claim_id.split()[-1]
        linked = set(PAPER_REF.findall(self.claims.get(claim_id, {}).get("Wikilinks", "")))
        for pid, fields in self.papers.items():
            if number in CLAIM_REF.findall("CLAIM " + fields.get("Claim links", "")):
                linked.add(pid.split()[-1])
            if number in {n for n in re.findall(r"\b(\d{3})\b", fields.get("Claim links", ""))}:
                linked.add(pid.split()[-1])
        return sorted(f"PAPER {n}" for n in linked)

    def trace(self, claim_id: str) -> dict:
        if claim_id not in self.claims:
            raise KeyError(f"{claim_id} is not a record in the claim registry")
        claim = self.claims[claim_id]
        declared_model, model_state = normalise_species(
            claim.get("Genotype/model relevance", ""))
        if model_state in {"unnormalised", "multiple", "scope"}:
            self.lose(f"CLAIM_MODEL_{model_state.upper()}", claim_id,
                      claim.get("Genotype/model relevance", "")[:80])

        supports, drifts = [], []
        for paper_id in self.supporting_papers(claim_id):
            self.candidates += 1
            fields = self.papers.get(paper_id)
            if fields is None:
                self.lose("PAPER_UNRESOLVED", paper_id, f"linked by {claim_id}")
                continue
            organism, state = normalise_species(fields.get("Model/species", ""))
            if state in {"unnormalised", "multiple", "scope"}:
                self.lose(f"SPECIES_{state.upper()}", paper_id,
                          fields.get("Model/species", "")[:80])
            elif state == "undeclared":
                self.lose("SPECIES_UNDECLARED", paper_id, "no Model/species field")
            pmids = PMID.findall(fields.get("Identifier", ""))
            entry = {
                "paper": paper_id,
                "pmid": pmids[0] if pmids else None,
                "species": organism,
                "species_state": state,
                "species_declared": fields.get("Model/species", "")[:60],
                "manifest_backed": bool(pmids) and pmids[0] in self.manifest_pmids,
            }
            supports.append(entry)
            if declared_model and organism and organism != declared_model:
                drifts.append({
                    "claim": claim_id,
                    "claim_model": declared_model,
                    "paper": paper_id,
                    "pmid": entry["pmid"],
                    "paper_species": organism,
                })

        emitted = len(supports)
        lost = sum(1 for loss in self.losses if loss["state"] == "PAPER_UNRESOLVED")
        if emitted + lost != self.candidates:
            raise AssertionError(
                f"accounting identity broken: emitted {emitted} + lost {lost} "
                f"!= candidates {self.candidates}")

        backed = sum(1 for entry in supports if entry["manifest_backed"])
        return {
            "claim": claim_id,
            "status": claim.get("Status", ""),
            "type": claim.get("Type", ""),
            "declared_model": declared_model,
            "declared_model_state": model_state,
            "premise_tags": self.premises.get(claim_id, []),
            "supports": supports,
            "species_drift": drifts,
            "coverage": {
                "supporting_papers": emitted,
                "manifest_backed": backed,
                "share": round(backed / emitted, 2) if emitted else 0.0,
            },
            "losses": self.losses,
        }


def render(result: dict, explain: bool) -> str:
    lines = [f"# {result['claim']} — foundation trace", ""]
    lines.append(f"status: {result['status']} · type: {result['type']}")
    lines.append(f"declared model: {result['declared_model'] or '(undeclared)'} "
                 f"[{result['declared_model_state']}]")
    if result["premise_tags"]:
        lines.append(f"premise tags on the record: {', '.join(result['premise_tags'])}")
    lines.append("")
    lines.append("## Rests on")
    for entry in result["supports"]:
        mark = "locator-backed" if entry["manifest_backed"] else "no work manifest"
        pmid = f"PMID {entry['pmid']}" if entry["pmid"] else "no PMID"
        lines.append(f"  {entry['paper']:<10} {pmid:<14} "
                     f"{entry['species'] or entry['species_state']:<12} ({mark})")
    coverage = result["coverage"]
    lines.append("")
    lines.append(f"## Coverage — {coverage['manifest_backed']}/{coverage['supporting_papers']} "
                 f"supporting papers are manifest-backed ({coverage['share']:.0%})")
    lines.append("  The rest carry no verbatim locator: their support is registry-declared,")
    lines.append("  not quote-verified. Absence of a drift finding below is bounded by this.")
    lines.append("")
    if result["species_drift"]:
        lines.append("## 🔴 SPECIES DRIFT")
        for drift in result["species_drift"]:
            lines.append(
                f"  {drift['claim']} declares model '{drift['claim_model']}' but rests on "
                f"{drift['paper']} (PMID {drift['pmid']}), a '{drift['paper_species']}' study.")
        lines.append("")
        lines.append("  A phenotype is crossing a species boundary that the claim does not")
        lines.append("  declare. This is the shape of the 2026-08-06 imported-premise defect.")
    else:
        lines.append("## No species drift among the declared edges")
    if result["losses"]:
        lines.append("")
        lines.append("## Losses — named, not normalised")
        for loss in result["losses"]:
            lines.append(f"  {loss['state']}: {loss['subject']} — {loss['detail']}")
    if explain:
        lines.append("")
        lines.append("## Fields consulted (and only these)")
        for kind, names in STRUCTURAL_FIELDS.items():
            lines.append(f"  {kind}: {', '.join(names)}")
        lines.append("  Narrative fields (Summary, Note, Evidence boundary, Clinical meaning)")
        lines.append("  are never read: the claim under test has the answer written in its own")
        lines.append("  prose, so a detector allowed to read it would be scoring a human's work.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--disease", default="wwox", help="disease model to trace")
    parser.add_argument("--claim", help="claim identifier, e.g. 'CLAIM 005'")
    parser.add_argument("--all-drift", action="store_true",
                        help="scan every claim and report only the species drifts")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--explain", action="store_true",
                        help="print the fields the detector was allowed to read")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()

    if args.all_drift:
        findings, scanned = [], 0
        for claim_id in sorted(Foundation(root, args.disease).claims):
            result = Foundation(root, args.disease).trace(claim_id)
            scanned += 1
            findings.extend(result["species_drift"])
        if args.json:
            print(json.dumps({"scanned": scanned, "drift": findings}, indent=2))
        else:
            print(f"scanned {scanned} claims · {len(findings)} species-drift findings")
            for drift in findings:
                print(f"  {drift['claim']}: model '{drift['claim_model']}' rests on "
                      f"{drift['paper']} (PMID {drift['pmid']}) — '{drift['paper_species']}'")
        return 0

    if not args.claim:
        parser.error("one of --claim or --all-drift is required")
    result = Foundation(root, args.disease).trace(args.claim)
    print(json.dumps(result, indent=2) if args.json else render(result, args.explain))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
