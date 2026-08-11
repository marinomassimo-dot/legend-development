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
import hashlib
import html
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path
from typing import Any
from html.parser import HTMLParser
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parent))

import corpus_firewall as firewall  # noqa: E402

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
CURRENT_SCHEMA_VERSION = 2
# 🔴 The refusal lives here, in the gate, not only in a regression test. Reviewed 2026-08-05:
# a locator whose anchor named `files/corpus/*.jsonl` passed `validate()` with zero errors,
# because the only check was a test nobody is obliged to run before writing.
# Reviewed 2026-08-06: by-name recognition survives no rename, and a copy out of
# `files/corpus/` is the obvious move for anyone the name check has just refused. The shared
# definition also asks what the file IS — see `corpus_firewall.looks_like_corpus`.
CORPUS_ARTEFACT = firewall.CORPUS_ARTEFACT
# Which surface a quote was taken from. Declared per locator, because "which artefact was
# named" and "which surface was actually used" are different facts, and only the first was
# ever checked: an agent could read the abstract, write a plausible dossier, declare the XML,
# and pass. `body`/`table`/`supplement` are text and are machine-checkable against the
# artefact; `figure` is pixels and can only be attested; `abstract` is honest but weak.
LOCATOR_SURFACES = {"body", "figure", "table", "supplement", "abstract"}
TEXT_SURFACES = {"body", "table", "supplement"}
# 🔴 How the running text and the printed panel stand to each other, per locator.
#
# `surface` above records which surface a quote came FROM. It cannot record what this field
# records: whether anyone looked at the other one. A `body` locator is not `text_only` by
# construction — it may be contradicted by a panel nobody has opened yet — so the two facts
# are independent and only the first was ever captured.
#
# The reason this is a field and not a convention: on 2026-08-04 a figure panel reversed a
# conclusion the running text did not contain, on 2026-08-06 an unmarked asterisk was the
# difference between "not significant" and "not tested", and on 2026-08-10 Figure 3B of
# PMID 42422765 turned a "dose-dependent" continuum into a threshold. In all three the text
# was accurate and incomplete, which is the failure mode a text-only pipeline cannot see.
#
# Deliberately NOT named `evidence_relation`: that key already exists in the DisMech sidecar
# layer carrying `SUPPORT | PARTIAL | REFUTE`, which answers a different question — does this
# evidence support the claim. This one answers: does the panel agree with the text.
PANEL_TEXT_RELATIONS = {
    "text_only",                    # the statement rests on the running text; no panel bears on it
    "panel_only",                   # read from the image; the text carries no equivalent
    "text_confirmed_by_panel",      # both were looked at and they agree
    "text_contradicted_by_panel",   # both were looked at and they do not — see COUPLING below
    # 🔴 The panel bears on the sentence and neither agrees nor disagrees with it. Added
    # 2026-08-10 on SIX independent instances across five papers, found by three actors who
    # had not spoken: PMID 36779245 entry 0, where the text says one versus two missense
    # variants make no difference and Figure 4A orders null/missense ABOVE missense/missense
    # with overlapping bands; PMID 32000863 entry 0, where the caption says lithium suppressed
    # seizures in Wwox−/− mice — true — and the panel shows the same suppression in +/+ and
    # +/−; the Iatan case; and the two pairs on PMID 38182577 that B DOWNGRADED from
    # contradiction after checking that the panel is not the one the sentence cites.
    #
    # Every admitted value was false on those entries, and that is what decided it: `text_only`
    # denies a panel that exists, `panel_only` denies a text relation that exists,
    # `text_confirmed_by_panel` is false, `text_contradicted_by_panel` is the word that was
    # removed after being verified wrong, and `unknown_legacy` is false for a reading made
    # today. **When no admitted value is true, the defect is the enum.** Forcing one would
    # write a known falsehood into canonical state, which outlasts any ordering of contracts.
    #
    # "Incomplete is not false" is the shortest statement of the relation.
    "panel_qualifies_text",         # the panel bears on it and does neither — see COUPLING below
    "unknown_legacy",               # captured before this field existed; owed a re-read, not a guess
}
# 🔴 COUPLING. `text_contradicted_by_panel` and `panel_qualifies_text` are both assertions
# about ANOTHER locator, so both have to name it. Without the pointer the claim is
# unfalsifiable prose sitting in a JSON field: a reader cannot tell which sentence was
# overturned or qualified, and a command cannot check anything at all. The marker therefore
# belongs to the PANEL locator — the evidence that makes the assertion — and the pointer
# resolves to the text locator it bears on.
POINTER_RE = re.compile(r"^entries\[(\d+)\]$")
# Which pointer and needle each coupled relation carries. One table, because the alternative
# is the shape this repository keeps finding in itself: the same rule written twice and
# maintained once.
#
# `qualifies_needle` rather than the bare `needle` the field was first emitted with. That is a
# deliberate divergence from the coining manifest and it is the smaller vocabulary, not the
# larger: `contradicts`/`contradicts_needle` already fixes the grammar as
# `<pointer>`/`<pointer>_needle`, so a bare `needle` would be a SECOND naming convention
# living beside the first. Same pointer name, same needle rule, one suffix law.
COUPLED_RELATIONS = {
    "text_contradicted_by_panel": (
        "contradicts", "contradicts_needle", "contradict", "overturns"),
    "panel_qualifies_text": ("qualifies", "qualifies_needle", "qualify", "qualifies"),
}
POINTER_FIELDS = {spec[0] for spec in COUPLED_RELATIONS.values()}
NEEDLE_FIELDS = {spec[1] for spec in COUPLED_RELATIONS.values()}
ARTIFACT_KINDS = {"article_binary", "article_text", "supplement_text", "figure", "table"}
SHA256_RE = re.compile(r"[a-f0-9]{64}")
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


# 🔴 An EXPLICIT whitespace class. Never `str.split()`, and never `\s`.
#
# Python's definition of whitespace includes the C0 separators — `'\x1d'.isspace()` is True —
# so `" ".join(value.split())` silently swallows them. That is not a nicety: PMID 17803050's
# extracted text renders `(P < 0.023)` as `(P \x1d 0.023)`, and `str.split()` turns that into
# `(P 0.023)`. Both the corrupt artifact and a quote copying the corruption normalise to the
# same string, so the match is stamped `strict` and the missing comparator disappears from the
# record. The normaliser was laundering the defect it was supposed to expose.
#
# A C0 separator is not whitespace in any typography. It is a glyph that did not survive
# extraction, and it must reach the SUSPECT check below intact.
# The class holds ONLY what a typesetter would actually set. `\f` (form feed) and `\v`
# (vertical tab) are NOT presentation whitespace in extracted text — they are damage, and
# folding them is the same laundering as `\x1d`. The corpus proves it: PMID 17803050's
# transcribed surface holds the literal bytes `Ca2\x0c, inorganic phos-` where the paper
# prints `Ca²⁺` — the form feed stands in for the superscript plus. Collapse it to a space
# and the quoted `Ca2` matches STRICTLY, and a calcium ion loses its charge in the record.
PRESENTATION_WHITESPACE = re.compile(r"[ \t\n\r   ]+")

# C0 controls that are never legitimate text. Tab, newline and carriage return are excluded
# because they are real layout characters; everything else here is extraction damage.
C0_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def _normalise_text(value: str) -> str:
    """Normalise presentation whitespace without weakening exact-word matching."""
    unified = unicodedata.normalize("NFKC", html.unescape(value))
    return PRESENTATION_WHITESPACE.sub(" ", unified).strip()


def _match_key(value: str) -> str:
    """Canonical quote key resilient only to markup and presentation punctuation.

    PMC inline tags split ``(Figure 3E)`` and superscripts such as ``1005PPGY1008`` into
    separate text nodes. Removing non-alphanumeric presentation characters restores the
    authored character sequence while preserving wording, order, digits and case.

    🔴 It does **not** preserve meaning, and the docstring above said "presentation
    punctuation" as if every discarded character were decoration. Folding to alphanumerics
    maps ``(P < 0.05)``, ``(P > 0.05)`` and ``(P 0.05)`` onto the single key ``P005``. On the
    one axis where this repository has already been wrong — `CLAIM 005`, corrected over the
    difference between "no significance marker" and "not significant" — the verifier was
    blind, and it stamped `verified` regardless. Use `_quote_matches`, never this alone.
    """
    normal = unicodedata.normalize("NFKC", html.unescape(value))
    return "".join(character for character in normal if character.isalnum())


# Characters whose removal can invert a scientific proposition rather than tidy it.
# Comparators and equality decide whether a result is a result; a sign decides direction.
DECISIVE_CHARACTERS = frozenset("<>≤≥=≠−–—-+±")


def crop_contains_span(
    crop: tuple[float, float, float, float],
    span: tuple[float, float, float, float],
) -> bool:
    """Does an adjudication crop contain the whole span it claims to adjudicate?

    Both are ``(x0, y0, x1, y1)`` in PDF points. The crop is declared by whoever rendered it;
    the span is what ``page.search_for`` returns for the quoted text.

    🔴 **An adjudication artifact must contain the entire span it adjudicates.** Image
    anchoring is currently the looser of the two evidence routes: a text locator is compared
    character by character against its artifact, while an image locator is believed on its
    word. On 2026-08-09 a crop declared to adjudicate a table row stopped at x=320 while the
    row ran to x=524 — the whole male-rat half of the quoted values sat outside the picture,
    and a locator anchored there would have been "verified" against pixels that do not exist.

    Unlike almost everything else this repository enforces, this needs no reader: both
    rectangles are already in hand, and containment is arithmetic. Edges count as contained —
    a span flush against the boundary is fully rendered, and being strict by a hair would
    reject correct artifacts and teach people to pad crops until the check stops complaining.
    """
    crop_x0, crop_y0, crop_x1, crop_y1 = crop
    span_x0, span_y0, span_x1, span_y1 = span
    return (
        crop_x0 <= span_x0
        and crop_y0 <= span_y0
        and crop_x1 >= span_x1
        and crop_y1 >= span_y1
    )


def _fold_with_offsets(value: str) -> tuple[str, str, list[int]]:
    """Return ``(normalised, alphanumeric key, offset of each kept character)``.

    The offsets are what make the fold auditable: they let the caller walk back from a match
    in the folded key to the exact span of the original text it came from, and compare what
    the fold threw away on each side.
    """
    normal = _normalise_text(value)
    kept: list[str] = []
    offsets: list[int] = []
    for index, character in enumerate(normal):
        if character.isalnum():
            kept.append(character)
            offsets.append(index)
    return normal, "".join(kept), offsets


def _decisive_sequence(value: str) -> tuple[str, ...]:
    """The ordered decisive characters of a span — what the fold would silently discard."""
    return tuple(character for character in value if character in DECISIVE_CHARACTERS)


def _quote_matches(snippet: str, text: str) -> tuple[bool, str]:
    """Verify a quote against an artifact surface. Returns ``(matched, mode)``.

    ``strict``   the authored character sequence was found intact — the only unqualified pass.
    ``folded``   found after discarding punctuation, **and** the decisive characters of the
                 quote match those of the exact span it was found in.
    ``refused``  the fold located the words but the decisive characters disagree.

    🔴 **The question is not "does the snippet look risky?" — it is "does normalising change
    the answer?"** The first version of this asked the former, by inspecting the snippet for
    comparators. That catches SUBSTITUTION and is blind to DELETION, which is the dangerous
    direction: `(P 0.05)` carries no comparator to notice, and folds onto exactly the same key
    as the `(P < 0.05)` the source states. Nothing about such a quote looks wrong.

    So the fold is now checked against its own evidence. The match is located in the folded
    key, the corresponding span of the original artifact text is cut back out through the
    offset map, and the decisive characters of that span are compared with the snippet's. A
    deletion, a substitution and an inserted sign are all caught, because all three change the
    sequence being compared rather than the appearance of the quote.
    """
    snippet_normal = _normalise_text(snippet)
    text_normal = _normalise_text(text)
    if snippet_normal in text_normal:
        return True, "strict"

    _snippet_normal, snippet_key, _snippet_offsets = _fold_with_offsets(snippet)
    text_normal_folded, text_key, text_offsets = _fold_with_offsets(text)
    if not snippet_key:
        return False, "folded"
    # `find` takes the FIRST occurrence. If the same word sequence appears more than once in
    # the artifact with different punctuation — a sentence restated in the discussion, a
    # figure caption echoing the body — the span compared is the first one, not necessarily
    # the one the reader quoted. That can refuse a quote another occurrence would have
    # matched. This is deliberate and it is the safe direction of the error: a refusal costs
    # a re-capture, an acceptance costs a false `verified` on the axis that decides whether a
    # result is a result. If false refusals ever become common enough to matter, scan every
    # occurrence and accept when ANY span agrees — never widen by relaxing the comparison.
    position = text_key.find(snippet_key)
    if position < 0:
        return False, "folded"

    start = text_offsets[position]
    end = text_offsets[position + len(snippet_key) - 1] + 1
    span = text_normal_folded[start:end]
    if _decisive_sequence(span) != _decisive_sequence(snippet_normal):
        return False, "refused"
    return True, "folded"


# 🔴 Elements that do NOT interrupt a word, so the text either side of them is contiguous in
# the author's sentence. Every other tag is treated as a block boundary and still contributes a
# separator, which is the conservative direction: unknown markup keeps the old behaviour and
# only these known-inline tags change.
#
# Why this list exists. Until 2026-08-10 every text node was joined with a space, so
# `<italic>WWOX</italic>‐DEE` came out as `WWOX ‐DEE` — a space the author never wrote,
# manufactured at a markup boundary. Measured: 53 of the 59 local structured surfaces contain
# at least one such boundary, `PMID24550385` alone has 218, and the token most often broken is
# the gene this repository is about, because a journal italicises it in every sentence.
#
# The damage was not the failed matches. It was the REPAIRS: quotes re-taken from the joined
# output carry the fabricated space, so they verify today and will stop verifying — correctly —
# the moment this is fixed. On PMID 32000863 the five snippets carrying it are exactly the five
# a note recorded as repaired that morning, an insert recorded before the cause was known.
# **A repair inherits the correctness of the tool it was verified against.**
XML_INLINE_TAGS = {
    "italic", "bold", "sup", "sub", "sc", "underline", "monospace", "roman", "sans-serif",
    "overline", "strike", "styled-content", "named-content", "xref", "ext-link", "uri",
    "inline-formula", "inline-graphic", "email", "fn", "target", "milestone-start",
    "milestone-end", "break",
}
HTML_INLINE_TAGS = {
    "i", "em", "b", "strong", "sup", "sub", "span", "a", "code", "small", "u", "mark",
    "abbr", "cite", "q", "s", "var", "kbd", "samp", "time", "big", "tt", "font", "label",
}


def _xml_surfaces(raw: bytes) -> tuple[str, str]:
    """Return (non-abstract text, abstract text) from XML/HTML-like content.

    A quote found only in ``<abstract>`` must not validate a locator declared as ``body``.
    ElementTree handles PMC XML. Malformed XML fails closed; silently stripping its tags would
    merge the abstract back into the body and recreate the shortcut this validator prevents.

    Inline elements are joined with NO separator and block elements with one — see
    ``XML_INLINE_TAGS``. This does not weaken the suspect screen: ``_refuse_suspect_surface``
    runs on the raw decoded bytes upstream of here, so a printable substitution is caught
    before any joining happens and cannot be normalised away by this function.
    """
    try:
        root = ElementTree.fromstring(raw)
    except ElementTree.ParseError as exc:
        raise ValueError(f"cannot parse structured XML: {exc}") from exc

    body_parts: list[str] = []
    abstract_parts: list[str] = []

    def local_name(node: ElementTree.Element) -> str:
        return node.tag.rsplit("}", 1)[-1].lower() if isinstance(node.tag, str) else ""

    def walk(node: ElementTree.Element, in_abstract: bool = False) -> None:
        here = in_abstract or local_name(node) == "abstract"
        target = abstract_parts if here else body_parts
        if node.text:
            target.append(node.text)
        for child in node:
            block = local_name(child) not in XML_INLINE_TAGS
            if block:
                target.append(" ")
            walk(child, here)
            if block:
                target.append(" ")
            if child.tail:
                target.append(child.tail)

    walk(root)
    return _normalise_text("".join(body_parts)), _normalise_text("".join(abstract_parts))


class _SurfaceHTMLParser(HTMLParser):
    """Separate common full-text HTML abstract containers from the article body."""

    VOID_ELEMENTS = {
        "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "param", "source", "track", "wbr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._abstract_stack: list[bool] = []
        self.body: list[str] = []
        self.abstract: list[str] = []

    def _separate(self, tag: str) -> None:
        """A block boundary interrupts a word; an inline one does not — see HTML_INLINE_TAGS."""
        if tag.lower() in HTML_INLINE_TAGS:
            return
        (self.abstract if any(self._abstract_stack) else self.body).append(" ")

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in self.VOID_ELEMENTS:
            self._separate(tag)
            return
        values = " ".join(value or "" for key, value in attrs if key in {"id", "class"})
        marker = tag.lower() == "abstract" or bool(
            re.search(r"(?:^|[-_\s])abstract(?:$|[-_\s])", values, re.IGNORECASE))
        self._separate(tag)
        self._abstract_stack.append(marker or any(self._abstract_stack))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        return

    def handle_endtag(self, tag: str) -> None:
        if self._abstract_stack:
            self._abstract_stack.pop()
        self._separate(tag)

    def handle_data(self, data: str) -> None:
        (self.abstract if any(self._abstract_stack) else self.body).append(data)


def _html_surfaces(raw: bytes) -> tuple[str, str]:
    parser = _SurfaceHTMLParser()
    parser.feed(raw.decode("utf-8", errors="strict"))
    parser.close()
    return _normalise_text("".join(parser.body)), _normalise_text("".join(parser.abstract))


# 🔴 Substitutions that are PRINTABLE, and therefore invisible to any control-character
# check. Adjudicated at 600 dpi against the printed page of PMID 17803050 on 2026-08-09: the
# C0 screen sees 34 corruptions in that paper and roughly 145 more are ordinary letters.
# `q` alone stands in for `±` 140 times.
#
# This matters most in the repair case. Fix the 34 controls and the artifact goes CLEAN at the
# C0 gate while staying wrong on the page — a surface that now looks verified and is not.
#
# Every signature below was calibrated against all 51 local PDFs before shipping. Bare
# `\bD2\b` was the draft, and it flags `two days (D2), D5 and D7` in PMID 26675548, which is a
# real timepoint label. It is anchored to statistical context instead. `q` and `t` produce
# zero hits across the other fifty PDFs.
PRINTABLE_SUBSTITUTIONS = (
    (re.compile(r"\d\s+q\s+\d"), "'q' where the page prints U+00B1 '±'"),
    (re.compile(r"\bD2\s+test\b|\banalyz\w+\s+by\s+D2\b|\bD2\s*=\s*\d"),
     "'D2' where the page prints U+03C7 U+00B2 'χ²'"),
    (re.compile(r"\d\s+t\s+\d{2,}"), "'t' where the page prints U+00D7 '×'"),
)

# Suspicion by ABSENCE — what the surface does NOT have. Fourteen corpus PDFs carry
# statistical language and not one of these operators; two are adjudicated corrupt. A paper
# that tests significance and never once prints a comparator is not a tidy paper, it is a text
# layer that lost them. This is the only signature that survives a "repair" of the visible
# damage, which is exactly why it exists.
TYPOGRAPHIC_OPERATORS = "<>≤≥±×−"
STATISTICAL_LANGUAGE = re.compile(
    r"significan|P-value|P value|standard deviation|\bt[- ]test\b|chi-squared", re.I)
MIN_STATISTICAL_MENTIONS = 3


def _refuse_suspect_surface(path: Path, *parts: str) -> None:
    """A declared text surface holding C0 controls is SUSPECT and is refused, not cleaned.

    🔴 Refused, never normalised. Stripping the controls would launder the defect into every
    quote drawn from the surface, and the quotes would then verify — against a document that
    no longer matches the paper. A C0 separator is not stray whitespace; it is the residue of
    a glyph that did not survive extraction, and on 2026-08-09 the glyph it replaced was the
    `<` in `(P < 0.023)`. The surface has to be re-derived from the source, which is work a
    validator cannot do and must not pretend to have done.
    """
    for part in parts:
        found = C0_CONTROL.search(part)
        if found:
            raise ValueError(
                f"SUSPECT text surface: {path.name} contains the C0 control "
                f"U+{ord(found.group()):04X} at offset {found.start()}. A control character is "
                f"not whitespace — it is a glyph that did not survive extraction, so every "
                f"quote taken from this surface is unverifiable. Re-derive the artifact from "
                f"the source; do not strip the controls"
            )

    # The remaining checks read entities, not raw markup: a PMC XML writes `&lt;`, and that IS
    # a comparator. Counting raw bytes would refuse every structured artifact in the corpus —
    # precisely the surfaces that are known good.
    for part in parts:
        readable = html.unescape(part)
        for pattern, description in PRINTABLE_SUBSTITUTIONS:
            found = pattern.search(readable)
            if found:
                raise ValueError(
                    f"SUSPECT text surface: {path.name} contains {description} at offset "
                    f"{found.start()} ({found.group()!r}). This substitution is PRINTABLE, so "
                    f"no control-character check can see it, and repairing the controls would "
                    f"leave the surface looking clean and reading wrong. Adjudicate against "
                    f"the rendered page and re-derive; do not edit the character"
                )
        mentions = len(STATISTICAL_LANGUAGE.findall(readable))
        operators = sum(readable.count(character) for character in TYPOGRAPHIC_OPERATORS)
        if mentions >= MIN_STATISTICAL_MENTIONS and operators == 0:
            raise ValueError(
                f"SUSPECT text surface: {path.name} uses statistical language "
                f"({mentions} mentions) and contains none of "
                f"{' '.join(TYPOGRAPHIC_OPERATORS)}. Suspicion here is by ABSENCE: a paper "
                f"that tests significance and never prints a comparator is a text layer that "
                f"lost them. Adjudicate against the rendered page before declaring this "
                f"surface"
            )


def _artifact_text(path: Path, kind: str) -> tuple[str, str]:
    """Return (body/supplement text, abstract text) for strict write-time verification.

    🔴 The control screen runs on the RAW DECODED BYTES of every branch, before any parser
    and before any normalisation. It used to run on the parsed output, which left the XML
    branch defended **by accident**: ElementTree rejects C0 controls as not-well-formed, so
    XML artifacts were refused without the screen ever executing. A defence that only works
    because a third-party parser happens to be strict is not a defence — it is a coincidence
    with a good track record, and it disappears silently the day the parser becomes tolerant
    or someone swaps in a lenient one. No test would have noticed.
    """
    suffix = path.suffix.lower()
    if suffix == ".docx":
        with zipfile.ZipFile(path) as archive:
            raw = archive.read("word/document.xml")
        _refuse_suspect_surface(path, raw.decode("utf-8", errors="replace"))
        body, _abstract = _xml_surfaces(raw)
        return body, ""
    if suffix == ".xml":
        raw = path.read_bytes()
        _refuse_suspect_surface(path, raw.decode("utf-8", errors="replace"))
        return _xml_surfaces(raw)
    if suffix in {".html", ".htm"}:
        raw = path.read_bytes()
        _refuse_suspect_surface(path, raw.decode("utf-8", errors="replace"))
        return _html_surfaces(raw)
    if suffix in {".txt", ".md"}:
        raw_text = path.read_text(encoding="utf-8")
        _refuse_suspect_surface(path, raw_text)
        return _normalise_text(raw_text), ""
    if kind in {"article_text", "supplement_text", "table"}:
        raise ValueError(f"text verification is unsupported for {path.suffix or 'this file type'}")
    return "", ""


def _pointer_needle_errors(
    entry: dict, entries: list, target: int, position: int, relation: str
) -> list[str]:
    """Does a coupled relation address its target by CONTENT as well as by position?

    🔴 `contradicts: "entries[N]"` is a positional pointer into a reorderable array, and the
    three checks around it — the target exists, it is a text surface, it is not this one —
    cannot see a **slip**. Insert a locator above the target and the index silently resolves
    to a different sentence: every field still well formed, the pairing now wrong, the
    validator silent. That is the same shape as a name collision and a field collision, and
    it is the one this repository already knew how to prevent.

    The prevention was half-copied. `adjudications.json` never writes `entries[N]` alone: it
    writes it beside a **needle**, and `check_needles` asks two arithmetic questions — does
    the needle occur exactly once, and is it a fragment of the snippet of the locator it
    names. `contradicts` took the addressing grammar and left behind the half that makes the
    address safe.

    So the needle here answers the same two questions in this array's terms: the fragment must
    belong to the snippet the index resolves to, and to **no other entry's**, because a
    fragment that matches two entries does not identify one. If the index slips, the fragment
    stops being found where the index points, and the check says so.

    Folding to alphanumerics is the right strength: this asks whether the needle belongs to
    that locator, not whether the page says what the snippet says. The artifact answers that.
    """
    pointer, needle_field, _bare, verb = COUPLED_RELATIONS[relation]
    needle = str(entry.get(needle_field) or "").strip()
    prefix = f"verbatim_locators.entries[{position}].{needle_field}"
    if not needle:
        return [
            f"{prefix}: `{pointer}` is a position in a list that can be reordered, so it "
            f"must be accompanied by a fragment of the snippet it {verb}. Without it an "
            f"inserted locator silently redirects the relation at a different sentence, "
            f"and every other check still passes"
        ]
    key = _match_key(needle)
    if not key:
        return [f"{prefix}: the fragment carries no alphanumeric content to match on"]
    if key not in _match_key(str(entries[target].get("snippet", ""))):
        return [
            f"{prefix}: {needle!r} is not a fragment of the snippet of entries[{target}], "
            f"which is what `{pointer}` names. Either the index has slipped or the "
            f"fragment was taken from the wrong sentence"
        ]
    also = [index for index, other in enumerate(entries)
            if index != target and key in _match_key(str(other.get("snippet", "")))]
    if also:
        return [
            f"{prefix}: {needle!r} also occurs in entries{also}. A fragment that matches more "
            f"than one locator does not identify one, so it cannot protect the index it "
            f"accompanies — quote a longer or more distinctive span"
        ]
    return []


ADJUDICATION_DIR = "page_adjudications"
ADJUDICATION_RECIPE = "adjudications.json"


def _adjudication_recipe_errors(
    root: Path, relative: str, digest: str, prefix: str
) -> list[str]:
    """A page adjudication is absent BY POLICY, so absence is not the question to ask.

    🔴 Two tools encoded two policies and the generalist was the one that was wrong. Rule 5e
    says a crop proving what an author printed *is* a reproduction of what the author printed,
    so the state ships **the derivation and never the derived**: source digest, page, rectangle
    in PDF points, dpi and the SHA-256 of the image, in an `adjudications.json` beside the
    reading. `regenerate_adjudications.py` turns that back into the identical bytes from a
    reader's own copy.

    Meanwhile `--verify-artifacts` looked for the file on disk and called its absence a defect
    — so `PMID 21212533` was unvalidatable anywhere while its own recipe reported
    *«11 adjudication artifacts regenerate to their declared digest, and 8 locators resolve to
    a span inside the crop that shows them»*. The manifest was right, the recipe was right, and
    the check between them was asking a question the policy had already answered.

    What this function does and does not certify, because the difference matters:

    - it verifies that the recipe **declares this artifact with this digest**, which is the
      only half a validator holding no source PDF can honestly check;
    - it does **not** verify that the recipe regenerates. That needs the article, and it is
      `regenerate_adjudications.py`'s job — run separately, with its own suite in the release
      battery. Delegation, not a waiver: the byte check moves to the tool that can perform it,
      and neither tool is left asserting something it cannot see.

    🔴 And the delegation stops exactly there, because half of that tool WAS an echo of this
    one. `regenerate_adjudications.py` imported `crop_contains_span` FROM this module, so its
    verdict *«the locators resolve to a span inside the crop»* was produced by the same code a
    validator would be trusting it to corroborate — a defect in the matching would have been
    invisible to the check built to confirm it. Only the DIGEST was genuinely independent: it
    renders the page with `fitz`, crops, hashes and compares, and that path touches nothing
    here.

    Closed 2026-08-11. `regenerate_adjudications.span_is_fully_shown` answers the same
    question in a different arithmetic — clip the span to the crop, require the clipped area
    to equal the span's area — rather than copying four comparisons, which would have been an
    echo spelled differently. The two are compared against each other over a dense grid of
    boundary cases in `test_regenerate_adjudications.py`, so a future edit to one and not the
    other fails rather than passes quietly.

    `_match_key` is still shared, and deliberately: it decides whether a needle is a fragment
    of the snippet it names, which is a question about THIS module's own bookkeeping, not a
    corroboration of it.

    So this function still delegates artifact identity and nothing else. Span containment
    stays here as well, now genuinely checked twice instead of once.

    Anything outside `page_adjudications/` is untouched: a missing artifact is still a BLOCK.
    """
    parts = Path(relative).parts
    if ADJUDICATION_DIR not in parts:
        return [f"{prefix}.path: artifact does not exist: {relative}"]
    recipe = root / Path(*parts[: parts.index(ADJUDICATION_DIR) + 2]) / ADJUDICATION_RECIPE
    if not recipe.is_file():
        return [f"{prefix}.path: {relative} is absent and no {ADJUDICATION_RECIPE} sits beside "
                f"it. A page adjudication is published as a recipe; without one there is "
                f"neither the image nor the means to rebuild it"]
    try:
        entries = json.loads(recipe.read_text(encoding="utf-8")).get("artifacts", [])
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{prefix}.path: {recipe.name} cannot be read ({exc})"]
    name = Path(relative).name
    declared = [entry for entry in entries if Path(str(entry.get("file", ""))).name == name]
    if not declared:
        return [f"{prefix}.path: {name} is absent from disk and its {ADJUDICATION_RECIPE} does "
                f"not declare it either, so nothing can rebuild it"]
    recorded = str(declared[0].get("sha256", ""))
    if recorded != digest:
        return [f"{prefix}.sha256: the manifest and {ADJUDICATION_RECIPE} disagree on "
                f"{name} — manifest {digest[:12]}…, recipe {recorded[:12]}…"]
    return []


def _safe_repo_path(root: Path, relative: str) -> Path:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError("artifact path escapes the workspace") from exc
    return candidate


def validate(
    manifest: Any,
    *,
    root: Path | None = None,
    verify_artifacts: bool = False,
    require_current_schema: bool = False,
) -> tuple[list[str], list[str]]:
    """Return (errors, incomplete_steps)."""
    errors: list[str] = []
    incomplete: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest must be a JSON object"], []

    schema_version = manifest.get("schema_version", 1)
    if not isinstance(schema_version, int) or schema_version < 1:
        errors.append("schema_version: must be a positive integer")
        schema_version = 1
    if schema_version > CURRENT_SCHEMA_VERSION:
        errors.append(
            f"schema_version: {schema_version} is newer than validator version "
            f"{CURRENT_SCHEMA_VERSION}")
    if require_current_schema and schema_version != CURRENT_SCHEMA_VERSION:
        errors.append(
            f"schema_version: new complete reads require {CURRENT_SCHEMA_VERSION}; "
            f"found {schema_version}")
    if verify_artifacts and root is None:
        errors.append("artifact verification requires a workspace root")

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

    artifacts: dict[str, dict[str, str]] = {}
    text_cache: dict[str, tuple[str, str]] = {}
    if schema_version >= 2:
        declared_artifacts = manifest.get("source_artifacts")
        if not isinstance(declared_artifacts, list) or not declared_artifacts:
            errors.append(
                "source_artifacts: schema v2 requires at least one fingerprinted full-text "
                "or visual artifact")
        else:
            for position, artifact in enumerate(declared_artifacts, 1):
                prefix = f"source_artifacts[{position}]"
                if not isinstance(artifact, dict):
                    errors.append(f"{prefix}: must be an object")
                    continue
                path_value = str(artifact.get("path", "")).strip()
                digest = str(artifact.get("sha256", "")).strip()
                kind = str(artifact.get("kind", "")).strip()
                if not path_value:
                    errors.append(f"{prefix}.path: must be a repository-relative path")
                    continue
                if path_value in artifacts:
                    errors.append(f"{prefix}.path: duplicate artifact {path_value}")
                objection = firewall.corpus_objection(path_value, root)
                if objection:
                    errors.append(f"{prefix}.path: {objection} — a bibliographic corpus is "
                                  "not evidence")
                if not SHA256_RE.fullmatch(digest):
                    errors.append(f"{prefix}.sha256: lowercase SHA-256 required")
                if kind not in ARTIFACT_KINDS:
                    errors.append(f"{prefix}.kind: must be one of {sorted(ARTIFACT_KINDS)}")
                artifacts[path_value] = {"sha256": digest, "kind": kind}
                if verify_artifacts and root is not None:
                    try:
                        resolved = _safe_repo_path(root, path_value)
                    except ValueError as exc:
                        errors.append(f"{prefix}.path: {exc}")
                        continue
                    if not resolved.is_file():
                        errors.extend(_adjudication_recipe_errors(
                            root, path_value, digest, prefix))
                    elif SHA256_RE.fullmatch(digest):
                        actual = hashlib.sha256(resolved.read_bytes()).hexdigest()
                        if actual != digest:
                            errors.append(
                                f"{prefix}.sha256: fingerprint mismatch for {path_value}")

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
            # 🔴 ZERO-BASED, changed 2026-08-10, and the discrepancy it removes was documented
            # as harmless for weeks. It was not. This loop counted from ONE while `contradicts`
            # and `adjudications.json` count from zero, so a SINGLE error line could carry two
            # `entries[N]` with opposite meanings — the notation collision inside the message
            # whose job is to disambiguate.
            #
            # It cost twice in one evening. Five needles on three branches would each have been
            # attached to the wrong locator by anyone who trusted the printed index; they were
            # right only because they were derived from the JSON. And a peer reading
            # `entries[1].abstract_snippet` went to entry 1, which has no such field, while the
            # defect was in entry 0.
            #
            # Zero wins because the published formats already use it: `adjudications.json`
            # writes `entries[N]` counting from zero and `regenerate_adjudications.py` indexes
            # the list directly. A reader copies the reference grammar, not the diagnostic
            # text, so the diagnostic is what moves.
            for position, entry in enumerate(entries):
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
                if firewall.names_a_corpus(str(entry.get("anchor", ""))) or \
                        firewall.names_a_corpus(str(entry.get("artifact", ""))):
                    errors.append(
                        f"verbatim_locators.entries[{position}]: anchored to a bibliographic "
                        "corpus. An export of abstracts is not a document; anchor into the "
                        "paper — section, figure or table")
                surface = entry.get("surface")
                if schema_version >= 2 and surface is None:
                    errors.append(
                        f"verbatim_locators.entries[{position}].surface: required by schema v2")
                elif surface is not None and surface not in LOCATOR_SURFACES:
                    errors.append(
                        f"verbatim_locators.entries[{position}].surface: must be one of "
                        f"{sorted(LOCATOR_SURFACES)}")
                if schema_version >= 2 and surface == "abstract":
                    errors.append(
                        f"verbatim_locators.entries[{position}].surface: abstract material may "
                        "be recorded as triage context, but cannot be an evidentiary locator "
                        "for a complete read")

                # `panel_text_relation` is OPTIONAL here on purpose. Whether a manifest is
                # allowed to omit it is a question about the corpus — which readings predate
                # the field — and this function sees one manifest with no way to know that.
                # The coverage obligation therefore lives in `growth_anchors.py`, where the
                # grandfathered set is recorded and a NEW omission shows up as a new member of
                # a ratcheted list. What is checkable from inside a single manifest is checked
                # here, and fails closed: the value, and the pointer the contradiction owes.
                relation = entry.get("panel_text_relation")
                if relation is not None and relation not in PANEL_TEXT_RELATIONS:
                    errors.append(
                        f"verbatim_locators.entries[{position}].panel_text_relation: must be "
                        f"one of {sorted(PANEL_TEXT_RELATIONS)}")
                # Both coupled relations are checked by one block, because they differ only in
                # the words: each asserts something about another locator, so each must name
                # it, and each owes the same needle for the same reason. Two copies of this
                # would be the fourth-site failure in the module that documents it.
                coupled = COUPLED_RELATIONS.get(str(relation))
                pointer_field = coupled[0] if coupled else None
                pointed = entry.get(pointer_field) if coupled else None
                if coupled:
                    _pointer, _needle_field, bare, verb = coupled
                    match = POINTER_RE.match(str(pointed or ""))
                    if match is None:
                        errors.append(
                            f"verbatim_locators.entries[{position}].{pointer_field}: "
                            f"`{relation}` asserts something about another locator, so it "
                            "must name it as `entries[N]`. Unpointed, the claim is prose in a "
                            "JSON field: no reader can tell which sentence it bears on and no "
                            "command can check it")
                    else:
                        # 🔴 ZERO-BASED, and that is a deliberate choice between two
                        # conventions this repository already uses for the same thing.
                        # `adjudications.json` refers to locators as `entries[N]` counting from
                        # zero, and `regenerate_adjudications.py` indexes the list directly.
                        # The error messages in THIS function count from one. A reader will
                        # copy the reference grammar, not the diagnostic text, so `contradicts`
                        # follows the recipe files. The mismatch is real and is worth removing
                        # at the next touch of the message strings; it is not worth a rename of
                        # a published recipe format today.
                        target = int(match.group(1))
                        # Both sides are zero-based now; the `- 1` this used to carry was the
                        # only place the two conventions were reconciled, silently.
                        if target == position:
                            errors.append(
                                f"verbatim_locators.entries[{position}].{pointer_field}: a "
                                f"locator cannot {bare} itself")
                        elif target >= len(entries):
                            errors.append(
                                f"verbatim_locators.entries[{position}].{pointer_field}: no "
                                f"entries[{target}] in this manifest")
                        elif entries[target].get("surface") not in TEXT_SURFACES:
                            errors.append(
                                f"verbatim_locators.entries[{position}].{pointer_field}: "
                                f"entries[{target}] is not a text surface. What a panel "
                                f"{verb} is something the text said; pointing at another "
                                "panel records a relation between images, which is a "
                                "different finding and needs its own words")
                        else:
                            errors.extend(_pointer_needle_errors(
                                entry, entries, target, position, str(relation)))
                for field in sorted(POINTER_FIELDS | NEEDLE_FIELDS):
                    if entry.get(field) is None:
                        continue
                    owner = next(name for name, spec in COUPLED_RELATIONS.items()
                                 if field in spec[:2])
                    if relation != owner:
                        errors.append(
                            f"verbatim_locators.entries[{position}].{field}: only a "
                            f"`{owner}` locator may carry one")

                artifact_values = entry.get("artifact")
                if isinstance(artifact_values, str):
                    artifact_paths = [artifact_values]
                elif isinstance(artifact_values, list) and all(
                    isinstance(item, str) and item.strip() for item in artifact_values
                ):
                    artifact_paths = artifact_values
                else:
                    artifact_paths = []
                if schema_version >= 2 and not artifact_paths:
                    errors.append(
                        f"verbatim_locators.entries[{position}].artifact: required by schema v2")
                unknown = [path for path in artifact_paths if path not in artifacts]
                if schema_version >= 2 and unknown:
                    errors.append(
                        f"verbatim_locators.entries[{position}].artifact: not declared in "
                        f"source_artifacts: {unknown}")

                if (
                    verify_artifacts and root is not None and schema_version >= 2
                    and surface in TEXT_SURFACES and snippet and artifact_paths and not unknown
                ):
                    matched = False
                    verification_failures: list[str] = []
                    for artifact_path in artifact_paths:
                        metadata = artifacts[artifact_path]
                        try:
                            resolved = _safe_repo_path(root, artifact_path)
                            if artifact_path not in text_cache:
                                text_cache[artifact_path] = _artifact_text(
                                    resolved, metadata["kind"])
                            body_text, abstract_text = text_cache[artifact_path]
                        except (OSError, KeyError, ValueError, zipfile.BadZipFile) as exc:
                            verification_failures.append(str(exc))
                            continue
                        matched, mode = _quote_matches(snippet, body_text)
                        if matched:
                            break
                        # The abstract probe runs whatever the body verdict was. It is
                        # diagnostic, not permissive — it never sets `matched` — and skipping
                        # it on a refusal would hide the single most useful thing we can tell
                        # the author: the sentence exists, in the wrong surface.
                        abstract_matched, _abstract_mode = _quote_matches(
                            snippet, abstract_text)
                        if abstract_matched:
                            verification_failures.append(
                                "quote occurs in the abstract but not the non-abstract body")
                        if mode == "refused":
                            verification_failures.append(
                                "UNVERIFIABLE_PUNCTUATION: the quote was not found with its "
                                "characters intact, and it carries a comparator, an equality "
                                "or a signed number. Falling back to alphanumeric matching "
                                "would compare a string with those characters removed, which "
                                "cannot tell '< 0.05' from '> 0.05' or from no comparator at "
                                "all. Re-capture this quote from the document")
                    if not matched:
                        detail = "; ".join(verification_failures) or "exact text not found"
                        errors.append(
                            f"verbatim_locators.entries[{position}].snippet: not verified in "
                            f"the declared {surface} artifact ({detail})")
                if ELISION_RE.search(snippet):
                    errors.append(
                        f"verbatim_locators.entries[{position}].snippet: stitched quote. Two "
                        "spans joined by an ellipsis are each verbatim but the whole is not, "
                        "and an external validator matching exact substrings will reject it. "
                        "Split it into two entries, or quote one contiguous span"
                    )

                # `abstract_snippet` exists so that a locator on a source nobody can index
                # stays verifiable through the one surface an external validator does hold.
                # Until 2026-08-06 nothing checked that the quote was actually IN the abstract,
                # so any string discharged the duty and the field certified only that its
                # author had typed something. Found by mutation-testing the reading of PMID
                # 19500159: a fabricated abstract quote passed while the same fabrication in
                # `snippet` was caught, because only one of the two was ever matched. The
                # abstract text is already parsed and cached one branch above; not using it
                # was the whole defect.
                abstract_snippet = str(entry.get("abstract_snippet", "")).strip()
                if (
                    verify_artifacts and root is not None and schema_version >= 2
                    and abstract_snippet and artifact_paths and not unknown
                ):
                    abstract_matched = False
                    abstract_failures: list[str] = []
                    # 🔴 Searched across every declared TEXT artifact, not only the one this
                    # locator names. `abstract_snippet` is a claim about the paper's abstract;
                    # it is not a claim about the surface this particular quote came from. The
                    # narrower reading blocked `PMID 17803050` entry 0, whose locator is a page
                    # adjudication: the check demanded an abstract from a PNG, which no image
                    # can offer, and reported the reading as defective for it.
                    #
                    # The locator's own artifact still goes first, so a manifest that does
                    # declare a matching text surface behaves exactly as before.
                    searchable = list(dict.fromkeys(
                        artifact_paths
                        + [path for path, meta in artifacts.items()
                           if meta.get("kind") in {"article_text", "supplement_text"}]))
                    for artifact_path in searchable:
                        metadata = artifacts[artifact_path]
                        try:
                            resolved = _safe_repo_path(root, artifact_path)
                            if artifact_path not in text_cache:
                                text_cache[artifact_path] = _artifact_text(
                                    resolved, metadata["kind"])
                            _body_text, abstract_text = text_cache[artifact_path]
                        except (OSError, KeyError, ValueError, zipfile.BadZipFile) as exc:
                            abstract_failures.append(str(exc))
                            continue
                        if not abstract_text:
                            abstract_failures.append(
                                f"{artifact_path} exposes no abstract surface")
                            continue
                        abstract_matched, mode = _quote_matches(
                            abstract_snippet, abstract_text)
                        if abstract_matched:
                            break
                        if mode == "refused":
                            abstract_failures.append(
                                "UNVERIFIABLE_PUNCTUATION: not found with its characters "
                                "intact, and it carries a comparator, an equality or a signed "
                                "number")
                    if not abstract_matched:
                        detail = "; ".join(abstract_failures) or "exact text not found"
                        errors.append(
                            f"verbatim_locators.entries[{position}].abstract_snippet: not "
                            f"found in the abstract of any declared artifact ({detail}). An "
                            "abstract anchor that is not in the abstract verifies nothing")

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
        if schema_version < 2 and entries and all(s is None for s in declared):
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
        elif indexed is not None:
            # This boolean gates a real duty: `false` obliges every locator to carry an
            # abstract anchor or an argued waiver. Until 2026-08-07 nothing accompanied it, so
            # flipping it to `true` discharged that duty silently — the last honour-system
            # field in a chain where artifact existence, fingerprint, body match, abstract
            # separation and abstract-anchor match are all verified. It is not checked online:
            # a validator that needs the network fails on a plane and, worse, fails *open* on
            # a hiccup. Instead it is made symmetric with `retraction_check`, which has always
            # worked this way — a claim plus the evidence for it, reviewable in a diff.
            # Audited 2026-08-07: all eleven declarations then in the repository were correct
            # against Europe PMC, so this requirement was introduced with zero grandfathering,
            # a window that closes the first time a manifest lands without it.
            # SCALE LIMIT, stated rather than discovered later: this is a bridge, not the
            # destination. "Reviewable in a diff" presumes a reviewer, and at five hundred
            # manifests that reviewer does not exist. The destination is to *derive* the index
            # state from a cached Europe PMC snapshot and stop asking an author for it at all —
            # the same shape as the receipt ledger's anchor. The evidence string written here
            # already has the field a derivation would populate, so that migration is a change
            # of author, not of schema. Revisit when manifests pass ~100, or sooner if any
            # audit finds a declaration that disagrees with the database.
            evidence = str(locators.get("source_fulltext_indexed_evidence", "")).strip()
            if len(evidence) < MIN_WAIVER_CHARS:
                errors.append(
                    "verbatim_locators.source_fulltext_indexed_evidence: state how the index "
                    f"state was determined, in at least {MIN_WAIVER_CHARS} characters — the "
                    "query, the date and what came back (e.g. 'Europe PMC EXT_ID:19936220 on "
                    "2026-08-06: inEPMC=Y, PMCID PMC2777388'). A bare boolean that gates the "
                    "abstract-anchoring duty is the one field left that nobody can check")
        if indexed is False:
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


def load_and_validate(
    root: Path,
    disease: str,
    pmid: str,
    *,
    artifact_root: Path | None = None,
    verify_artifacts: bool = False,
    require_current_schema: bool = False,
) -> tuple[list[str], list[str]]:
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
    return validate(
        manifest,
        # A branch transports the manifest, while copyright-controlled evidence may
        # intentionally live only in the shared checkout's gitignored files/.  Keep
        # manifest discovery and evidence resolution separate without weakening the
        # existing containment check.  Omitting artifact_root preserves the original
        # fail-closed single-workspace behaviour.
        root=artifact_root or root,
        verify_artifacts=verify_artifacts,
        require_current_schema=require_current_schema,
    )


def verification_scope(*, verify_artifacts: bool, require_current_schema: bool) -> str:
    """Describe exactly what a successful CLI run established.

    Structural validation is useful for auditing legacy manifests, but it is not the
    persistence boundary. Keep that distinction in the verdict itself so a bare ``PASS``
    cannot be mistaken for hash- and quote-level verification.

    🔴 The adjudication clause states the POLICY, not whether it fired on this run. A page
    adjudication is absent by rule 5e — the state publishes the derivation and never the
    derived — so its bytes are checked against `adjudications.json` here and regenerated by
    `regenerate_adjudications.py` there. A verdict that said "artifact existence verified" flat
    would be claiming a check the policy forbids it from performing, on every run, whether or
    not any adjudication was involved. Describing the contract cannot drift; describing the
    incident would need a channel this function does not have.
    """
    delegated = (
        "; page adjudications are checked against their recipe rather than on disk (rule 5e), "
        "and regeneration is verified by regenerate_adjudications.py"
    )
    if verify_artifacts and require_current_schema:
        return (
            "MANIFEST STRICT: current schema required; local artifact existence, SHA-256 "
            "and exact text locators verified" + delegated
        )
    if verify_artifacts:
        return (
            "ARTIFACT CHECKS: local artifact existence, SHA-256 and exact text locators "
            "verified where declared; legacy schema still allowed" + delegated
        )
    if require_current_schema:
        return (
            "CURRENT SCHEMA, STRUCTURE ONLY: local artifact existence, SHA-256 and exact "
            "text locators NOT VERIFIED"
        )
    return (
        "STRUCTURE ONLY: local artifact existence, SHA-256 and exact text locators NOT "
        "VERIFIED"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument(
        "--artifact-workspace",
        help=(
            "optional workspace root used only to resolve and verify source artifacts; "
            "the manifest is still loaded from --workspace"
        ),
    )
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--pmid", required=True)
    parser.add_argument(
        "--verify-artifacts", action="store_true",
        help="verify local existence, SHA-256 and exact text locators",
    )
    parser.add_argument(
        "--require-current-schema", action="store_true",
        help="refuse legacy manifest schemas",
    )
    args = parser.parse_args()
    errors, incomplete = load_and_validate(
        Path(args.workspace).resolve(), args.disease, args.pmid,
        artifact_root=(
            Path(args.artifact_workspace).resolve()
            if args.artifact_workspace is not None else None
        ),
        verify_artifacts=args.verify_artifacts,
        require_current_schema=args.require_current_schema,
    )
    for item in incomplete:
        print(f"  [INCOMPLETE] {item}")
    scope = verification_scope(
        verify_artifacts=args.verify_artifacts,
        require_current_schema=args.require_current_schema,
    )
    if errors:
        print(f"VERDICT: FAIL — verification scope: {scope}")
        for error in errors:
            print(f"  [BLOCK] {error}")
        return 1
    state = "complete" if not incomplete else "structurally valid with declared gaps"
    print(
        f"VERDICT: PASS — manifest for PMID {args.pmid} is {state} "
        f"({len(incomplete)} gap(s)); verification scope: {scope}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
