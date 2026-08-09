#!/usr/bin/env python3
"""Derive a queryable evidence index from the work manifests already in the repository.

Read-only, computed on demand, and **not written to disk**. That is deliberate: a derived
file committed beside its sources becomes a second truth the moment the sources move, and
the repository already carries one drift test for exactly that hazard. Nothing here needs a
drift test because nothing here is stored — the index is rebuilt every time it is asked for,
from the canonical Markdown, which stays the source of truth.

## What an evidence record is

The pieces already exist. A deep-dive work manifest records, for every statement its reading
carries out, the proposition, the sentence quoted verbatim, where that sentence sits, which
fingerprinted artifact it was matched against, and the receipt of the reading that produced
it. What has been missing is that those pieces live in fifteen per-reading files and are not
interrogable across papers. This promotes what is already captured; it extracts nothing new,
and it re-derives no judgement.

## The two tiers, and why the index must show them

Of 235 locator entries, 91 declare neither `surface` nor `artifact`: they predate schema v2
and consist of a proposition, a quote and a prose anchor. They are not worthless — they were
written while the document was open — but they cannot be matched against a fingerprinted
file, so they are not verifiable in the sense the current contract means. An index that
returned all 235 as one undifferentiated set would report 39% unverifiable evidence as
though it were verified. Every query therefore carries its own tier breakdown.

## Coverage is the denominator, not the numerator

Fifteen papers of forty-nine integrated ones have a manifest at all. A query that returns
seven records has not searched the literature; it has searched the manifest-backed third of
it. The report says so, in the same terms as `coverage_report.md`: the denominator is what
is known to exist, not what has been processed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import trace_claim_foundation as tcf  # noqa: E402 - shares the registry parsing

PMID_IN_NAME = re.compile(r"PMID(\d+)")

# A locator is verifiable when it names both the surface it was read from and the
# fingerprinted artifact it was matched against. Anything short of that is recorded at its
# real tier rather than promoted to the one the query would prefer.
VERIFIABLE = "verifiable"
LEGACY_UNANCHORED = "legacy_unanchored"
ABSTRACT_ONLY = "abstract_only"

# The identifier is content-derived, so the separator must be one that cannot occur inside
# the fields it joins. An earlier version used a single space and a stray NUL byte reached
# the source file through it; a visible two-character delimiter fails loudly instead.
ID_DELIMITER = "::"


def evidence_id(pmid: str, proposition: str, snippet: str) -> str:
    """A stable identifier derived from content, so reordering a manifest does not renumber.

    Deriving it from the position in the file would make every insertion look like a change
    to everything after it — the same reason the freeze contract pins blocks rather than
    offsets.
    """
    material = ID_DELIMITER.join((pmid, proposition, snippet))
    return f"EVD-{hashlib.sha256(material.encode('utf-8')).hexdigest()[:12]}"


class EvidenceIndex:
    def __init__(self, root: Path, disease: str) -> None:
        self.root = root
        self.foundation = tcf.Foundation(root, disease)
        self.manifest_dir = root / "disease-models" / disease / "research" / "deepdive_manifests"
        self.losses: list[dict[str, str]] = []
        self.candidates = 0
        self.records: list[dict] = []
        self.papers_by_pmid = self._index_papers()
        self._claim_cache: dict[str, list[str]] | None = None
        self._build()

    def _index_papers(self) -> dict[str, str]:
        by_pmid: dict[str, str] = {}
        for paper_id, fields in self.foundation.papers.items():
            for pmid in tcf.PMID.findall(fields.get("Identifier", "")):
                by_pmid.setdefault(pmid, paper_id)
        return by_pmid

    def lose(self, state: str, subject: str, detail: str) -> None:
        self.losses.append({"state": state, "subject": subject, "detail": detail})

    def _claims_by_paper(self) -> dict[str, list[str]]:
        """Paper -> claims it is evidential for, built once.

        `wikilink_only` edges are excluded here for the same reason they are excluded from a
        drift finding: a cross-reference is navigation, and an evidence record bound to one
        would assert that a paper supports a claim that never named it as a source.
        """
        if self._claim_cache is None:
            cache: dict[str, list[str]] = {}
            for claim_id in self.foundation.claims:
                for paper_id, kind in self.foundation.supporting_papers(claim_id):
                    if kind in tcf.EVIDENTIAL_EDGES:
                        cache.setdefault(paper_id, []).append(claim_id)
            self._claim_cache = {paper: sorted(claims) for paper, claims in cache.items()}
        return self._claim_cache

    def _build(self) -> None:
        for path in sorted(self.manifest_dir.glob("PMID*.json")):
            match = PMID_IN_NAME.match(path.name)
            if not match:
                self.lose("MANIFEST_UNIDENTIFIED", path.name, "filename carries no PMID")
                continue
            pmid = match.group(1)
            try:
                manifest = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                self.lose("MANIFEST_UNPARSEABLE", path.name, str(error)[:80])
                continue
            paper_id = self.papers_by_pmid.get(pmid)
            if paper_id is None:
                self.lose("MANIFEST_WITHOUT_PAPER", f"PMID {pmid}",
                          "read and manifested, but no integrated PAPER record")
            locators = manifest.get("verbatim_locators") or {}
            entries = locators.get("entries") or []
            if not entries:
                self.lose("MANIFEST_WITHOUT_LOCATORS", f"PMID {pmid}",
                          "manifest present, no locator entries")
            claims = self._claims_by_paper().get(paper_id or "", [])
            for entry in entries:
                self.candidates += 1
                proposition = (entry.get("proposition") or "").strip()
                snippet = (entry.get("snippet") or "").strip()
                if not proposition or not snippet:
                    self.lose("LOCATOR_INCOMPLETE", f"PMID {pmid}",
                              "a locator without both a proposition and a quote is not evidence")
                    continue
                surface = entry.get("surface")
                artifact = entry.get("artifact")
                if surface and artifact:
                    tier = ABSTRACT_ONLY if surface == "abstract" else VERIFIABLE
                else:
                    tier = LEGACY_UNANCHORED
                self.records.append({
                    "evidence_id": evidence_id(pmid, proposition, snippet),
                    "pmid": pmid,
                    "paper": paper_id,
                    "claims": claims,
                    "tier": tier,
                    "surface": surface,
                    "artifact": artifact,
                    "anchor": entry.get("anchor"),
                    "proposition": proposition,
                    "snippet": snippet,
                    "receipt": manifest.get("receipt"),
                    "schema_version": manifest.get("schema_version"),
                })
        emitted = len(self.records)
        lost = sum(1 for loss in self.losses if loss["state"] == "LOCATOR_INCOMPLETE")
        if emitted + lost != self.candidates:
            raise AssertionError(
                f"accounting identity broken: emitted {emitted} + lost {lost} "
                f"!= candidates {self.candidates}")

    def coverage(self) -> dict:
        manifested = {record["paper"] for record in self.records if record["paper"]}
        tiers: dict[str, int] = {}
        for record in self.records:
            tiers[record["tier"]] = tiers.get(record["tier"], 0) + 1
        return {
            "papers_in_registry": len(self.foundation.papers),
            "papers_with_evidence_records": len(manifested),
            "evidence_records": len(self.records),
            "by_tier": tiers,
            "verifiable_share": round(
                tiers.get(VERIFIABLE, 0) / len(self.records), 2) if self.records else 0.0,
        }

    def query(self, term: str | None, claim: str | None, tier: str | None) -> list[dict]:
        needle = term.casefold() if term else None
        results = []
        for record in self.records:
            if claim and claim not in record["claims"]:
                continue
            if tier and record["tier"] != tier:
                continue
            haystack = f"{record['proposition']} {record['snippet']}".casefold()
            if needle and needle not in haystack:
                continue
            results.append(record)
        return results


def render_header(index: EvidenceIndex) -> list[str]:
    coverage = index.coverage()
    tiers = ", ".join(f"{name} {count}" for name, count in sorted(coverage["by_tier"].items()))
    return [
        "# Evidence index — derived, not stored",
        "",
        f"records: {coverage['evidence_records']} from "
        f"{coverage['papers_with_evidence_records']} papers, out of "
        f"{coverage['papers_in_registry']} in the registry",
        f"tiers: {tiers}  ·  verifiable share {coverage['verifiable_share']:.0%}",
        "",
        "A query here searches the manifest-backed part of the literature, not the",
        "literature. Records at tier `legacy_unanchored` predate schema v2: they carry a",
        "proposition, a quote and a prose anchor, but no fingerprinted artifact to match",
        "the quote against.",
    ]


def render_losses(index: EvidenceIndex) -> list[str]:
    if not index.losses:
        return []
    lines = ["", "## Losses — named, not normalised"]
    lines.extend(f"  {loss['state']}: {loss['subject']} — {loss['detail']}"
                 for loss in index.losses)
    return lines


def render(index: EvidenceIndex, results: list[dict], limit: int) -> str:
    lines = render_header(index)
    lines.append("")
    lines.append(f"## {len(results)} matching record(s)"
                 + (f", showing {limit}" if len(results) > limit else ""))
    for record in results[:limit]:
        lines.append("")
        lines.append(f"  {record['evidence_id']}  [{record['tier']}]  PMID {record['pmid']}"
                     f"  {record['paper'] or '(no PAPER record)'}"
                     + (f"  -> {', '.join(record['claims'])}" if record["claims"] else ""))
        lines.append(f"    proposition: {record['proposition'][:150]}")
        lines.append(f"    quote:       {record['snippet'][:150]}")
        lines.append(f"    where:       {record['surface'] or 'surface undeclared'} — "
                     f"{(record['anchor'] or 'no anchor')[:90]}")
    lines.extend(render_losses(index))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".")
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--term", help="substring to search in propositions and quotes")
    parser.add_argument("--claim", help="restrict to evidence bound to a claim, e.g. 'CLAIM 005'")
    parser.add_argument("--tier", choices=(VERIFIABLE, LEGACY_UNANCHORED, ABSTRACT_ONLY))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--coverage", action="store_true", help="print coverage only")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    index = EvidenceIndex(Path(args.root).resolve(), args.disease)
    if args.coverage:
        if args.json:
            print(json.dumps({"coverage": index.coverage(), "losses": index.losses}, indent=2))
        else:
            print("\n".join(render_header(index) + render_losses(index)))
        return 0
    results = index.query(args.term, args.claim, args.tier)
    if args.json:
        print(json.dumps({"coverage": index.coverage(), "results": results,
                          "losses": index.losses}, indent=2))
    else:
        print(render(index, results, args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
