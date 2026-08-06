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


def _normalise_text(value: str) -> str:
    """Normalise presentation whitespace without weakening exact-word matching."""
    return " ".join(html.unescape(value).split())


def _match_key(value: str) -> str:
    """Canonical quote key resilient only to markup and presentation punctuation.

    PMC inline tags split ``(Figure 3E)`` and superscripts such as ``1005PPGY1008`` into
    separate text nodes. Removing non-alphanumeric presentation characters restores the
    authored character sequence while preserving wording, order, digits and case.
    """
    normal = unicodedata.normalize("NFKC", html.unescape(value))
    return "".join(character for character in normal if character.isalnum())


def _xml_surfaces(raw: bytes) -> tuple[str, str]:
    """Return (non-abstract text, abstract text) from XML/HTML-like content.

    A quote found only in ``<abstract>`` must not validate a locator declared as ``body``.
    ElementTree handles PMC XML. Malformed XML fails closed; silently stripping its tags would
    merge the abstract back into the body and recreate the shortcut this validator prevents.
    """
    try:
        root = ElementTree.fromstring(raw)
    except ElementTree.ParseError as exc:
        raise ValueError(f"cannot parse structured XML: {exc}") from exc

    body_parts: list[str] = []
    abstract_parts: list[str] = []

    def walk(node: ElementTree.Element, in_abstract: bool = False) -> None:
        local = node.tag.rsplit("}", 1)[-1].lower() if isinstance(node.tag, str) else ""
        here = in_abstract or local == "abstract"
        target = abstract_parts if here else body_parts
        if node.text:
            target.append(node.text)
        for child in node:
            walk(child, here)
            if child.tail:
                target.append(child.tail)

    walk(root)
    return _normalise_text(" ".join(body_parts)), _normalise_text(" ".join(abstract_parts))


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

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in self.VOID_ELEMENTS:
            return
        values = " ".join(value or "" for key, value in attrs if key in {"id", "class"})
        marker = tag.lower() == "abstract" or bool(
            re.search(r"(?:^|[-_\s])abstract(?:$|[-_\s])", values, re.IGNORECASE))
        self._abstract_stack.append(marker or any(self._abstract_stack))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        return

    def handle_endtag(self, tag: str) -> None:
        if self._abstract_stack:
            self._abstract_stack.pop()

    def handle_data(self, data: str) -> None:
        (self.abstract if any(self._abstract_stack) else self.body).append(data)


def _html_surfaces(raw: bytes) -> tuple[str, str]:
    parser = _SurfaceHTMLParser()
    parser.feed(raw.decode("utf-8", errors="strict"))
    parser.close()
    return _normalise_text(" ".join(parser.body)), _normalise_text(" ".join(parser.abstract))


def _artifact_text(path: Path, kind: str) -> tuple[str, str]:
    """Return (body/supplement text, abstract text) for strict write-time verification."""
    suffix = path.suffix.lower()
    if suffix == ".docx":
        with zipfile.ZipFile(path) as archive:
            raw = archive.read("word/document.xml")
        body, _abstract = _xml_surfaces(raw)
        return body, ""
    if suffix == ".xml":
        return _xml_surfaces(path.read_bytes())
    if suffix in {".html", ".htm"}:
        return _html_surfaces(path.read_bytes())
    if suffix in {".txt", ".md"}:
        return _normalise_text(path.read_text(encoding="utf-8")), ""
    if kind in {"article_text", "supplement_text", "table"}:
        raise ValueError(f"text verification is unsupported for {path.suffix or 'this file type'}")
    return "", ""


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
    match_cache: dict[str, tuple[str, str]] = {}
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
                        errors.append(f"{prefix}.path: artifact does not exist: {path_value}")
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
                                match_cache[artifact_path] = tuple(
                                    _match_key(value) for value in text_cache[artifact_path])
                            body_key, abstract_key = match_cache[artifact_path]
                        except (OSError, KeyError, ValueError, zipfile.BadZipFile) as exc:
                            verification_failures.append(str(exc))
                            continue
                        snippet_key = _match_key(snippet)
                        if snippet_key in body_key:
                            matched = True
                            break
                        if snippet_key in abstract_key:
                            verification_failures.append(
                                "quote occurs in the abstract but not the non-abstract body")
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
                    for artifact_path in artifact_paths:
                        metadata = artifacts[artifact_path]
                        try:
                            resolved = _safe_repo_path(root, artifact_path)
                            if artifact_path not in text_cache:
                                text_cache[artifact_path] = _artifact_text(
                                    resolved, metadata["kind"])
                                match_cache[artifact_path] = tuple(
                                    _match_key(value) for value in text_cache[artifact_path])
                            _body_key, abstract_key = match_cache[artifact_path]
                        except (OSError, KeyError, ValueError, zipfile.BadZipFile) as exc:
                            abstract_failures.append(str(exc))
                            continue
                        if not abstract_key:
                            abstract_failures.append(
                                f"{artifact_path} exposes no abstract surface")
                            continue
                        if _match_key(abstract_snippet) in abstract_key:
                            abstract_matched = True
                            break
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


def load_and_validate(
    root: Path,
    disease: str,
    pmid: str,
    *,
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
        root=root,
        verify_artifacts=verify_artifacts,
        require_current_schema=require_current_schema,
    )


def verification_scope(*, verify_artifacts: bool, require_current_schema: bool) -> str:
    """Describe exactly what a successful CLI run established.

    Structural validation is useful for auditing legacy manifests, but it is not the
    persistence boundary. Keep that distinction in the verdict itself so a bare ``PASS``
    cannot be mistaken for hash- and quote-level verification.
    """
    if verify_artifacts and require_current_schema:
        return (
            "MANIFEST STRICT: current schema required; local artifact existence, SHA-256 "
            "and exact text locators verified"
        )
    if verify_artifacts:
        return (
            "ARTIFACT CHECKS: local artifact existence, SHA-256 and exact text locators "
            "verified where declared; legacy schema still allowed"
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
