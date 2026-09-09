#!/usr/bin/env python3
"""Where did the identifiers inside a locator's PROPOSITION come from?

🔴 WHY THIS EXISTS, measured rather than imagined.

On 2026-09-09, reading PMID 31428585, a locator's proposition asserted that reference 1
of the paper was `PMID 29581896`. The Europe PMC deposit being read carried the answer in
its own markup — `<ext-link ext-link-type="pmid">29310447</ext-link>` — and 29581896 is a
different paper by the same author. The identifier had been resolved by an external author
search, whose first hit was taken, WHILE THE ARTEFACT CONTAINING THE CORRECT VALUE WAS OPEN.

Two independent blind auditors caught it, both by doing the one thing the reader had not:
looking in the artefact. That is the whole of this check.

WHAT IT DOES

For every locator entry in a work manifest, it extracts the identifier-shaped tokens
asserted in the proposition (PMID, PMCID, DOI) and asks, for each one, a single question:

    does this identifier occur in ANY artefact this manifest declares?

and sorts the answer into three buckets:

    IN_ARTEFACT          the value is in the bytes the reading was done on. Checkable.
    DECLARED_EXTERNAL    the proposition says, in words, that the value came from somewhere
                         else — a ledger, a registry, a DOI-to-PMID resolution, another
                         paper. Legitimate and, crucially, DECLARED.
    UNDECLARED_EXTERNAL  neither. The proposition states an identifier as if it were read
                         off the source, and it is not there.

🔴 THE THIRD BUCKET IS NOT AUTOMATICALLY AN ERROR, AND THE TOOL MUST NOT PRETEND OTHERWISE.
A manifest may legitimately name a corpus PMID in a proposition without saying "resolved
externally" — the sentence may make provenance obvious to a human. What the bucket means
is exactly this: *nothing in the record says where this number came from, and it is not in
the source*. That is a review surface, not a verdict, which is why the default exit code is
0 and `--strict` is opt-in.

It is deliberately NOT a check that the identifier is CORRECT. Nothing local can know that.
It checks the weaker, cheaper and — on the evidence of the failure above — sufficient
property: whether the reading could have got the value from what it declares it read.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PMID_RE = re.compile(r"\bPMID[:\s]*([0-9]{7,8})\b", re.IGNORECASE)
BARE_PMID_RE = re.compile(r"\b([0-9]{8})\b")
PMCID_RE = re.compile(r"\bPMC([0-9]{5,9})\b")
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"'<>,;)\]]+)")

# Phrases that DECLARE an identifier's provenance as outside the artefact. Kept generous on
# purpose: the failure this tool exists for is an UNDECLARED value, and a reader who took
# the trouble to say where a number came from should never be flagged for the wording.
DECLARED_MARKERS = (
    "resolved externally", "external resolution", "resolved from", "not present in this deposit",
    "no pmid in this document", "carries no pmid", "outside this artefact", "outside the artefact",
    "a statement about the ledger", "in this corpus", "no receipt", "receipt status",
    "already read here", "read here", "complete_fulltext_read", "partial_fulltext_read",
    "corpus crossquery", "the corpus holds", "this corpus", "pubmed esearch", "pubmed esummary",
    "resolved to pmids", "doi-to-pmid", "doi to pmid",
)

# 🔴 MARKERS THAT OUTRANK EVERY DECLARATION, AND THE REASON THEY EXIST IS THIS TOOL'S OWN FIRST TEST.
# Written naively, this checker would have MISSED the exact error it was built for. The failing
# proposition read "...attributed to ref 1 (Huang and Chang 2018, PMID 29581896, no receipt here)":
# the phrase "no receipt" is a legitimate declaration ABOUT THE LEDGER, and it silenced the check on
# a completely different assertion sitting in the same sentence — that this identifier IS reference 1
# of the source. The artefact is the authority on that, and it disagreed.
#
# So provenance is not one question but two, and only the second can be waived by a declaration:
#   "this identifier IS a citation of the source"   -> the ARTEFACT adjudicates. Never waivable.
#   "this identifier has some property elsewhere"   -> a ledger or index adjudicates. Declarable.
# `DEFAULTS THAT BIT US` has the general form of this already: *the anti-bug tool is immune to the
# bug* — verify the tool too. This block is that verification, kept as code rather than as a memory.
IDENTITY_CLAIM_MARKERS = (
    "ref ", "ref.", "reference ", "attributed to", "cited to", "cites", "citing", "citation",
    "resolves to", "= pmid", "is pmid", "its pmid",
)

TEXT_KINDS = {"article_text", "supplement_text", "table", "article_binary"}


def artefact_haystack(manifest: dict, root: Path) -> tuple[str, list[str]]:
    """Concatenate the readable bytes of every declared artefact. Missing files are named."""
    chunks: list[str] = []
    missing: list[str] = []
    for art in manifest.get("source_artifacts") or []:
        rel = str(art.get("path", ""))
        if art.get("kind") not in TEXT_KINDS:
            continue
        path = root / rel
        if not path.is_file():
            missing.append(rel)
            continue
        try:
            chunks.append(path.read_bytes().decode("utf-8", "replace"))
        except OSError:
            missing.append(rel)
    return "\n".join(chunks), missing


def identifiers(text: str) -> set[str]:
    found: set[str] = set()
    for m in PMID_RE.finditer(text):
        found.add(m.group(1))
    for m in BARE_PMID_RE.finditer(text):
        found.add(m.group(1))
    for m in PMCID_RE.finditer(text):
        found.add("PMC" + m.group(1))
    for m in DOI_RE.finditer(text):
        found.add(m.group(1).rstrip(".,);"))
    return found


def in_haystack(ident: str, hay: str) -> bool:
    if ident.startswith("PMC") or ident.startswith("10."):
        return ident.lower() in hay.lower()
    # A PMID may appear in markup as a bare number; require a non-digit boundary so that
    # 29310447 does not match inside 293104470.
    return re.search(r"(?<!\d)" + re.escape(ident) + r"(?!\d)", hay) is not None


def declared(text: str) -> bool:
    low = text.lower()
    return any(marker in low for marker in DECLARED_MARKERS)


def claims_source_identity(text: str) -> bool:
    """Does the proposition assert that this identifier IS a citation of the source?

    If it does, the artefact is the authority and no external-provenance declaration may
    silence the check. See the comment on IDENTITY_CLAIM_MARKERS.
    """
    low = text.lower()
    return any(marker in low for marker in IDENTITY_CLAIM_MARKERS)


def audit_manifest(path: Path, root: Path) -> dict:
    manifest = json.loads(path.read_text())
    hay, missing = artefact_haystack(manifest, root)
    rows = []
    entries = ((manifest.get("verbatim_locators") or {}).get("entries")) or []
    for pos, entry in enumerate(entries):
        prop = str(entry.get("proposition", ""))
        # The SNIPPET is verified verbatim by the manifest validator, so identifiers there are
        # the source's own. Only the PROPOSITION — the reader's prose — is in scope here.
        for ident in sorted(identifiers(prop)):
            if in_haystack(ident, hay):
                verdict = "IN_ARTEFACT"
            elif claims_source_identity(prop):
                # The proposition says this identifier is a citation OF THE SOURCE, and the
                # source does not contain it. A declaration cannot excuse this one.
                verdict = "SOURCE_IDENTITY_UNVERIFIED"
            elif declared(prop):
                verdict = "DECLARED_EXTERNAL"
            else:
                verdict = "UNDECLARED_EXTERNAL"
            rows.append({"entry": pos, "identifier": ident, "verdict": verdict})
    return {
        "manifest": str(path),
        "pmid": manifest.get("pmid"),
        "artefacts_missing": missing,
        "rows": rows,
        "counts": {
            v: sum(1 for r in rows if r["verdict"] == v)
            for v in ("IN_ARTEFACT", "DECLARED_EXTERNAL", "UNDECLARED_EXTERNAL",
                      "SOURCE_IDENTITY_UNVERIFIED")
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifest", nargs="*", help="manifest paths; default is every manifest of the disease")
    ap.add_argument("--root", default=".", help="repository root holding files/")
    ap.add_argument("--disease", default="wwox")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any identifier is UNDECLARED_EXTERNAL")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if args.manifest:
        paths = [Path(p) for p in args.manifest]
    else:
        paths = sorted((root / "disease-models" / args.disease / "research" / "deepdive_manifests").glob("PMID*.json"))

    reports = []
    for path in paths:
        try:
            reports.append(audit_manifest(path, root))
        except (json.JSONDecodeError, OSError) as exc:
            reports.append({"manifest": str(path), "error": str(exc), "rows": [],
                            "counts": {"IN_ARTEFACT": 0, "DECLARED_EXTERNAL": 0,
                                       "UNDECLARED_EXTERNAL": 0, "SOURCE_IDENTITY_UNVERIFIED": 0}})

    # 🔴 A MANIFEST WHOSE EVIDENCE IS ABSENT CANNOT BE MEASURED, AND COUNTING IT ANYWAY PRODUCES
    # A HEADLINE NUMBER THAT ANSWERS A DIFFERENT QUESTION. `files/` is gitignored by design, so in
    # most checkouts the majority of manifests point at bytes that are not there; with an empty
    # haystack EVERY identifier is "not in the artefact" and the tool would report a corpus-wide
    # provenance crisis that is really an evidence-locality fact. First run, 2026-09-09: 80
    # manifests, of which only 26 had all their declared artefacts present. The unmeasurable ones
    # are separated here rather than averaged in.
    measurable = [r for r in reports if not r.get("artefacts_missing") and "error" not in r]
    unmeasurable = [r for r in reports if r.get("artefacts_missing") or "error" in r]

    if args.json:
        print(json.dumps({"measurable": measurable, "unmeasurable": unmeasurable}, indent=1))
    else:
        total = {"IN_ARTEFACT": 0, "DECLARED_EXTERNAL": 0, "UNDECLARED_EXTERNAL": 0,
                 "SOURCE_IDENTITY_UNVERIFIED": 0}
        for rep in measurable:
            for k, v in rep["counts"].items():
                total[k] += v
            flagged = [r for r in rep["rows"]
                       if r["verdict"] in ("UNDECLARED_EXTERNAL", "SOURCE_IDENTITY_UNVERIFIED")]
            if flagged:
                print(f"{rep.get('pmid')}  {rep['manifest']}")
                for r in flagged:
                    print(f"    [{r['verdict']}] entries[{r['entry']}]: {r['identifier']}")
        for rep in unmeasurable:
            if rep.get("artefacts_missing"):
                print(f"{rep.get('pmid')}  [UNMEASURABLE - artefact absent] {', '.join(rep['artefacts_missing'])}")
        print(f"manifests: {len(reports)} | measurable (all artefacts present): {len(measurable)} | "
              f"unmeasurable (evidence absent): {len(unmeasurable)}")
        print(f"over the measurable ones -- in artefact: {total['IN_ARTEFACT']} | "
              f"declared external: {total['DECLARED_EXTERNAL']} | undeclared external: "
              f"{total['UNDECLARED_EXTERNAL']} | source-identity unverified: {total['SOURCE_IDENTITY_UNVERIFIED']}")
        print("NOTE: an identifier absent from the artefact is not thereby wrong. This reports "
              "where a reading COULD have got the value, never whether the value is correct.")

    # --strict judges only what could be measured: an absent artefact is an evidence-locality
    # problem for the receipt contract to raise, never a provenance failure of the reading.
    if args.strict and any(r["counts"]["UNDECLARED_EXTERNAL"]
                           or r["counts"]["SOURCE_IDENTITY_UNVERIFIED"] for r in measurable):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
