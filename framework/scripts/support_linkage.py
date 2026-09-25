#!/usr/bin/env python3
"""Report registry citation/link discrepancies without adjudicating scientific support.

A missing edge is a review candidate, never an instruction to add it. Two signs
(other-claim reference and a difference marker) yield POSSIBLE_CONTRAST, not a
scientific verdict: supporting evidence can come from different conditions.
Existing declared edges are not scientifically verified by this check.
The record splitter and identifiers reuse coverage_report; links reuse claim_links.
Read-only, advisory, exit 0 unless inputs cannot be read.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coverage_report  # noqa: E402
import growth_anchors  # noqa: E402
from claim_links import declared_claim_links

parse_entries = coverage_report.parse_entries
FIELD = coverage_report.FIELD
PMID = coverage_report.PMID
CLAIM_HEADING = growth_anchors.HEADINGS["claims"]

UNLINKED = "UNLINKED_SUPPORT"
CONTRAST = "POSSIBLE_CONTRAST"
UNCLASSIFIED = "UNCLASSIFIED"
UNCHECKED = "UNCHECKED"

# A claim named inside a sentence: `CLAIM 005`, `[[claim_registry_current#CLAIM 005]]`.
CLAIM_REFERENCE = re.compile(r"\bCLAIM\s+(\d{3})\b")

# Sentence scope. A boundary is terminal punctuation followed by whitespace and a character that
# does not continue a sentence (not lowercase, not a digit: `Fig. 2C`, `n = 2; the …` stay whole
# where they must), or the registry's own 🔴 statement marker.
SENTENCE_BOUNDARY = re.compile(r"(?<=[.;!?])\s+(?=[^\s\da-zà-ÿ])|\s*🔴\s*")
MARKUP = re.compile(r"[*_`]+")

# Difference and opposition, as STEMS so inflection does not defeat them (diverso/diversa/diversi,
# differ/different/difference/differenza/differente). This is the lexical half of a two-sign
# test; see the module docstring for why a miss here is loud rather than silent.
CONTRAST_MARKERS = re.compile(
    r"(?i)\b(?:"
    r"differ\w*|divers[oaie]\b|distint\w*|distinct\w*|dissimil\w*"
    r"|unlike|whereas|contrast\w*|contrar\w*|contrapost\w*|oppost[oaie]|opposite"
    r"|invece|mentre|a\s+differenza|rather\s+than|piuttosto\s+che|versus|vs\.?"
    r"|not\s+the\s+same|non\s+(?:è|sono)\s+(?:lo\s+stesso|la\s+stessa|gli\s+stessi"
    r"|le\s+stesse|uguali?|equivalent[ei])"
    r")"
)


@dataclass(frozen=True)
class Result:
    kind: str       # UNLINKED_SUPPORT | POSSIBLE_CONTRAST | UNCLASSIFIED | UNCHECKED
    claim: str      # "CLAIM 026"
    pmid: str
    field: str      # the claim field that named the PMID
    record: str     # owning registry record, "" when UNCHECKED
    reason: str
    sentence: str = ""   # the sentence the verdict was reached on


def claim_support_fields(fields: dict[str, str]) -> dict[str, str]:
    """`Summary`, `Source` and every `Evidence boundary…` variant, by lower-cased key."""
    return {key: value for key, value in fields.items()
            if key in ("summary", "source") or "evidence boundary" in key}


def sentences(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_BOUNDARY.split(text) if part and part.strip()]


@dataclass(frozen=True)
class Reading:
    kind: str       # UNLINKED_SUPPORT | POSSIBLE_CONTRAST | UNCLASSIFIED
    why: str


def classify_citation(sentence: str, claim_id: str, owner_links: set[str]) -> Reading:
    """Report lexical and structural clues; they do not establish the citation relation."""
    named = {f"CLAIM {n}" for n in CLAIM_REFERENCE.findall(sentence)} - {claim_id}
    attributed = sorted(named & owner_links)
    marker = CONTRAST_MARKERS.search(MARKUP.sub("", sentence))
    if attributed and marker:
        return Reading(CONTRAST, f"other linked claim(s) {', '.join(attributed)} and "
                                 f"difference marker {marker.group(0)!r}; possible contrast, "
                                 "requires scientific review; support is not ruled out")
    if attributed:
        return Reading(UNCLASSIFIED, f"the sentence attributes the PMID to "
                                     f"{', '.join(attributed)}, which the record links, but "
                                     f"carries no contrast marker: support or comparison?")
    if marker:
        return Reading(UNCLASSIFIED, f"the sentence marks a contrast ({marker.group(0)!r}) but "
                                     f"attributes the PMID to no claim the record links")
    return Reading(UNLINKED, "")


# The most demanding verdict wins across several citing sentences.
_PRECEDENCE = {UNLINKED: 0, UNCLASSIFIED: 1, CONTRAST: 2}


def claims(text: str) -> list[tuple[str, dict[str, str]]]:
    marks = list(CLAIM_HEADING.finditer(text))
    out = []
    for index, mark in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        body = text[mark.end():end]
        fields = {m.group("key").strip().lower(): m.group("value").strip()
                  for m in FIELD.finditer(body)}
        out.append((" ".join(mark.group(1).split()), fields))
    return out


def owners_by_pmid(papers_text: str) -> dict[str, dict[str, str]]:
    """PMID -> the record that owns it: a PAPER over any CORPUS placeholder, else the first."""
    owners: dict[str, dict[str, str]] = {}
    for entry in parse_entries(papers_text):
        for pmid in PMID.findall(entry.get("identifier", "")):
            current = owners.get(pmid)
            if current is None or (current["_kind"] != "PAPER" and entry["_kind"] == "PAPER"):
                owners[pmid] = entry
    return owners


def citations(fields: dict[str, str]) -> dict[str, list[tuple[str, str]]]:
    """PMID -> every (field, sentence) that cites it, in field order."""
    found: dict[str, list[tuple[str, str]]] = {}
    for key, value in claim_support_fields(fields).items():
        for sentence in sentences(value):
            for pmid in dict.fromkeys(PMID.findall(sentence)):
                found.setdefault(pmid, []).append((key, sentence))
    return found


def check(claims_text: str, papers_text: str) -> list[Result]:
    owners = owners_by_pmid(papers_text)
    results: list[Result] = []
    for claim_id, fields in claims(claims_text):
        for pmid, cited in citations(fields).items():
            first_field, first_sentence = cited[0]
            owner = owners.get(pmid)
            if owner is None:
                results.append(Result(UNCHECKED, claim_id, pmid, first_field, "",
                                      "no registry record's Identifier names this PMID",
                                      first_sentence))
                continue
            is_stub = owner["_id"].startswith("CORPUS-STUB")
            links = set() if is_stub else declared_claim_links(owner.get("claim links"))
            if not is_stub and claim_id in links:
                continue
            if is_stub:
                missing = (f"owning record is a CORPUS-STUB (Status: {owner.get('status', '?')}; "
                           f"Claim links: {owner.get('claim links', '?')[:60]})")
            else:
                missing = (f"Claim links does not name {claim_id} "
                           f"(declares: {owner.get('claim links', '<absent>')[:60]!r})")
            readings = [(classify_citation(sentence, claim_id, links), key, sentence)
                        for key, sentence in cited]
            reading, key, sentence = min(readings, key=lambda r: _PRECEDENCE[r[0].kind])
            reason = missing if reading.kind == UNLINKED else f"{missing}; {reading.why}"
            results.append(Result(reading.kind, claim_id, pmid, key, owner["_id"], reason,
                                  sentence))
    return results


def excerpt(sentence: str, pmid: str, width: int = 240) -> str:
    text = " ".join(sentence.split())
    if len(text) <= width:
        return text
    at = max(0, text.find(pmid) - width // 2)
    return ("…" if at else "") + text[at:at + width] + "…"


def render(results: list[Result]) -> str:
    lines = []
    for r in results:
        line = f"{r.kind} {r.claim} PMID {r.pmid} via {r.field} -> {r.record or '-'}: {r.reason}"
        if r.sentence:
            line += f" | sentence: «{r.sentence}»"
        lines.append(line)
    counts = {kind: sum(1 for r in results if r.kind == kind)
              for kind in (UNLINKED, CONTRAST, UNCLASSIFIED, UNCHECKED)}
    lines.append(f"unlinked_support: {counts[UNLINKED]} | possible_contrast: {counts[CONTRAST]} "
                 f"| unclassified: {counts[UNCLASSIFIED]} | unchecked: {counts[UNCHECKED]}")
    return "\n".join(lines)


def check_root(root: Path, disease: str) -> list[Result]:
    claims_path = root / growth_anchors.REGISTRIES["claims"].format(disease=disease)
    papers_path = root / growth_anchors.REGISTRIES["papers"].format(disease=disease)
    return check(claims_path.read_text(encoding="utf-8"),
                 papers_path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--disease", default="wwox")
    args = parser.parse_args(argv)
    try:
        results = check_root(Path(args.root), args.disease)
    except OSError as error:
        print(f"UNCHECKABLE: {error}", file=sys.stderr)
        return 2
    print(render(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
