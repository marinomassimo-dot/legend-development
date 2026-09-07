#!/usr/bin/env python3
"""Assemble the causal graph LEGEND already declares — and refuse to author the rest.

Read-only over the registries. It writes only the two derived surfaces it is asked to
write, and it never touches a canonical current file.

## What this is, and what it deliberately is not

LEGEND already holds a partial causal graph. Claims are its nodes; the wikilinks between
claims are its edges; and the relational content — *what* one claim does to another — is
written in prose inside claim titles and inside the verbatim propositions captured by
full-text readings. What has been missing is not the graph. What has been missing is the
graph *as an object*: enumerable, countable, and separable into "declared", "annotated but
untyped" and "written down somewhere but never annotated".

This tool assembles that object. It performs five operations, in order, and each one is a
mechanical transformation of something already in the repository:

1. **Inventory the nodes** — every claim record, with its declared fields.
2. **Inventory the edges** — every claim→claim link the registry declares, in the field
   that declares it, with the direction each side declares.
3. **Extract candidate edges** — every proposition already written in the repository that
   contains a relational connective from a closed, declared lexicon.
4. **Classify what is absent** — an isolated node, an asymmetric link and an unlinked prose
   mention are three different absences, and only one of them is about biology.
5. **Type the existing edges** — from a declared annotation, and from nothing else.

🔴 **It generates no causal inference.** Step 5 is the load-bearing restriction. An edge is
typed only when a claim record *annotates* the link with a relation type; today no record
does, so every edge is emitted `UNTYPED` with the reason attached. That is not a gap in this
tool — it is the measurement. Deriving `DIRECT` from "both endpoints are `DATO`" would
manufacture exactly the causal assertion the Orchestrator role is not permitted to make: two
demonstrated facts are not a demonstrated relation between them, and the difference is the
entire subject of this layer. Typing is Scientist work, performed against evidence; this
tool prepares the packet and reads back the verdict.

The same restriction governs step 3. A relational proposition is emitted verbatim, with its
provenance and its matched connective. The text is split around the connective for reading
convenience, and that split is marked `endpoints_resolved: false`, because deciding which
biological entity sits on each side of a sentence is a reading, not a regex.

## What a candidate edge is drawn from, and what it is not drawn from

Three declared populations, and their whole extent:

* every claim's `Title` field — a declared, atomic, one-line statement of the claim;
* every row of the working model's BLOCK 2 claim mirror — the second, independently worded
  declaration of the same nodes, kept in sync by a LINT rule;
* every `proposition` in every deep-dive work manifest — the statements a reading captured
  with a verbatim quote behind them.

`Summary`, `Clinical meaning` and `Evidence boundary` are **not** scanned, and the exclusion
is deliberate rather than an oversight. Those fields are prose paragraphs; converting a
paragraph into atomic assertions is the atomization contract specified in §4 of
`dismech_export_spec.md`, which is a reading operation with its own review. Sweeping them
with a regex would produce sentence fragments wearing the authority of an extraction. The
population scanned is declared in every report so the denominator is never implied.

## Two known limits of the lexicon, stated rather than discovered later

A multi-word connective is matched as one string, so an adverb inserted into it —
*"contributes **directly** to"* — reads as no connective at all. And six entries are also
common nouns or attributive adjectives in this corpus (`control`, `reduced`, `rescue`,
`controls`, `increase`, `increased`); they produced 162 of the first run's 302 candidates,
almost all of them noise. Deleting them would have taken *"WWOX loss reduced myelination"*
with them, so they are kept, marked `AMBIGUOUS_BARE_FORM` and sorted to the back of the
review queue. Neither limit is hidden: both are reported in the output.

## Coverage is reported, never assumed

Most locator-backed propositions belong to papers that no claim declares as a source. A
candidate from such a paper is still a candidate — it is a relationship someone wrote down
while reading — but it is not attached to a node, and the report says how many are in that
state rather than quietly binding them to the nearest claim.

## Losses are named

Following the export contract, anything the assembler cannot represent is counted rather
than dropped, and the accounting identity ``emitted + lost == scanned`` is asserted on every
run for the candidate population.

Run:

```bash
python3 framework/scripts/pathograph.py --disease wwox
python3 framework/scripts/pathograph.py --disease wwox --json
python3 framework/scripts/pathograph.py --disease wwox \
    --out disease-models/wwox/analysis/pathograph_inventory.md \
    --export disease-models/wwox/analysis/data/pathograph_export.jsonl
python3 framework/scripts/pathograph.py --disease wwox --verify \
    --out disease-models/wwox/analysis/pathograph_inventory.md \
    --export disease-models/wwox/analysis/data/pathograph_export.jsonl
```
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

# The fields this tool is allowed to read from a claim record. `trace_claim_foundation`
# keeps its own, shorter list and audits itself against it; widening that constant to serve
# this tool would weaken a restriction another tool advertises. The two lists are separate
# on purpose, and both are allow-lists rather than "everything except prose".
CLAIM_FIELDS = (
    "Title", "Status", "Type", "Pathway", "Genotype/model relevance",
    "Transferability", "clinical relevance", "Wikilinks", "Source",
)

# The relation vocabulary a Scientist may write. An annotation carrying anything else is a
# named loss, never a guess and never a silent drop.
RELATION_VOCABULARY = (
    "DIRECT",
    "INDIRECT_UNKNOWN_INTERMEDIATES",
    "ASSOCIATED",
    "CONTROVERSIAL_OPEN",
)

# The syntax a Scientist uses to type an existing edge: the annotation follows the wikilink,
# in the parenthetical position the registries already use for link annotations
# (`[[paper_registry_current#PAPER 045]] (Shaukat — lato efficacia)`).
#
#     [[claim_registry_current#CLAIM 004]] (relation: DIRECT — the rescue measures both)
#
# Reading it costs one regex. Inventing it from the endpoints' declared fields would cost
# the layer its meaning.
CLAIM_LINK = re.compile(
    r"\[\[claim_registry_current#CLAIM\s+(\d{3})\]\](?:\s*\(relation:\s*([^)]*)\))?"
)
RECORD_LINK = re.compile(r"\[\[([a-z_]+_current)#([^\]|]+?)(?:\|[^\]]*)?\]\]")
ANY_WIKILINK = re.compile(r"\[\[[^\]]*\]\]")
BARE_CLAIM = re.compile(r"\bCLAIM\s+(\d{3})\b")
MIRROR_ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(.+?)\s*\|")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")

# 🔴 The working model's version history names claims constantly — *"CLAIM 014 refined,
# CLAIM 015 promoted to consolidated baseline"* — and none of it is a relationship. On the
# first run 20 of 21 co-mentions came from changelog prose and version-history rows, which
# would have shipped a page of bookkeeping presented as candidate biology. The exclusion is
# declared here, counted at every run and printed in the report, so it is a stated bound and
# not a silent filter.
HISTORY_ROW = re.compile(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|")
CHANGELOG_FIELD = re.compile(r"^\*\*(Last update|Version|Date baseline|Prev)")
BATCH_ID = re.compile(r"\bBATCH_\d{8}")

# The closed relational lexicon. Registry prose is bilingual by policy, so the lexicon is
# too. A class is a property of the *word*, not a verdict about the relationship: an
# `ASSOCIATIVE` connective does not make an edge `ASSOCIATED`, and nothing downstream is
# allowed to read it that way.
CONNECTIVES: dict[str, tuple[str, ...]] = {
    "ARROW": ("→", "->", "⇒", "=>", "↔", "<->", "⟶"),
    "CAUSAL": (
        "causes", "cause", "caused", "induces", "induce", "induced", "inducing",
        "leads to", "lead to", "leading to", "results in", "result in", "resulting in",
        "drives", "drive", "triggers", "trigger", "produces", "produce",
        "underlies", "underlie", "mediates", "mediate", "abolishes", "abolish",
        "rescues", "rescue", "rescued", "restores", "restore", "restored",
        "impairs", "impair", "impaired", "disrupts", "disrupt", "disrupted",
        "destabilizes", "destabilises", "destabilize", "perturbs", "perturb",
        "activates", "activate", "inhibits", "inhibit", "blocks", "block",
        "suppresses", "suppress", "suppressed", "prevents", "prevent",
        "contributes to", "contribute to", "regulates", "regulate",
        "controls", "control", "modulates", "modulate", "reduces", "reduce",
        "reduced", "increases", "increase", "increased",
        "causa", "causano", "provoca", "provocano", "inducono", "porta a", "portano a",
        "determina", "determinano", "contribuisce a", "contribuiscono a",
        "regola", "regolano", "inibisce", "inibiscono", "attiva", "attivano",
        "corregge", "peggiora", "migliora",
    ),
    "ASSOCIATIVE": (
        "associated with", "association with", "correlates with", "correlated with",
        "co-occurs", "co-occur", "tracks with", "parallels",
        "associato a", "associata a", "associati a", "associate a", "correla con",
    ),
    "DEPENDENCY": (
        "depends on", "depend on", "dependent on", "requires", "require", "required for",
        "downstream of", "upstream of", "secondary to", "due to",
        "dipende da", "dipendono da", "richiede", "richiedono",
        "a valle di", "a monte di", "secondario a",
    ),
}

# 🔴 Six lexicon entries are also common nouns or attributive adjectives in this corpus, and
# on the first run they produced 162 of 302 candidates: `control` (60 — *"the control
# cohort"*), `reduced` (40 — *"reduced g-ratio"*), `rescue` (33 — *"the rescue"*), `controls`
# (12), `increase` (9) and `increased` (8). Deleting them from the lexicon would have been
# the easy fix and the wrong one: *"WWOX loss reduced myelination"* is a real relational
# proposition and would have gone with them. They are kept, marked, and sorted to the back of
# the review queue, so the noise is quarantined rather than either shipped or discarded.
AMBIGUOUS_FORMS = frozenset({
    "cause", "caused", "control", "controls", "drive", "increase", "increased",
    "impaired", "produce", "reduce", "reduced", "rescue", "rescued", "restored",
    "block", "blocks", "trigger", "suppressed", "disrupted", "induced",
})

# Node attributes that exist in the operator's model of this layer but nowhere in the
# registries. They are emitted at their real state so the report distinguishes "annotation
# LEGEND has not written" from "biology LEGEND has not found".
UNANNOTATED = "NOT_ANNOTATED"
BIOLOGICAL_SCALES = ("MOLECULAR", "CELLULAR", "TISSUE", "ORGANISM")

UNTYPED = "UNTYPED"
NO_ANNOTATION = "NO_DECLARED_RELATION_ANNOTATION"
UNRECOGNISED = "RELATION_TYPE_UNRECOGNISED"

MARKER = "Generated file"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_fields(block: str, allowed: tuple[str, ...]) -> dict[str, str]:
    """Declared fields in first-line form, fenced blocks skipped, first occurrence kept.

    Same semantics as `trace_claim_foundation.declared_fields`, against this tool's own
    allow-list. A field's continuation lines are prose by definition — the point where an
    author starts explaining — so only the value on the field's own line is kept.
    """
    found: dict[str, str] = {}
    in_fence = False
    for line in block.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = tcf.FIELD.match(line.strip())
        if not match:
            continue
        name = match.group(1).strip()
        if name in allowed and name not in found:
            found[name] = match.group(2).strip()
    return found


def field_carrying(block: str, needle: str) -> str:
    """Which declared field's paragraph contains `needle`, or `body` when none does.

    A link in the `Wikilinks:` field is an annotation someone maintained. The same link
    inside an `Evidence boundary:` paragraph is a cross-reference someone wrote while
    explaining something. Both are declared; they are not the same act, and collapsing them
    would hide which edges are curated and which are incidental.
    """
    current = "body"
    for line in block.splitlines():
        match = tcf.FIELD.match(line.strip())
        if match:
            current = match.group(1).strip()
        if needle in line:
            return current
    return "body"


class Connective:
    """One lexicon hit inside a proposition."""

    __slots__ = ("start", "text", "klass")

    def __init__(self, start: int, text: str, klass: str) -> None:
        self.start = start
        self.text = text
        self.klass = klass

    @property
    def ambiguous(self) -> bool:
        return self.text.casefold() in AMBIGUOUS_FORMS

    def key(self) -> tuple[int, int, int, str]:
        # An unambiguous form anchors the proposition wherever it sits, so *"the engineered
        # allele abolishes protein and causes mortality"* anchors on `abolishes` rather than
        # on whichever bare form came first. Then earliest wins; on a tie the longer
        # connective wins, so "contributes to" is not reported as "contribute". The class
        # name breaks any remaining tie so the choice never depends on dictionary order.
        return (int(self.ambiguous), self.start, -len(self.text), self.klass)


def build_lexicon() -> list[tuple[re.Pattern[str], str, str]]:
    patterns: list[tuple[re.Pattern[str], str, str]] = []
    for klass, entries in CONNECTIVES.items():
        for entry in entries:
            if klass == "ARROW":
                pattern = re.compile(re.escape(entry))
            else:
                pattern = re.compile(rf"(?<![\w-]){re.escape(entry)}(?![\w-])", re.IGNORECASE)
            patterns.append((pattern, entry, klass))
    return patterns


LEXICON = build_lexicon()


def find_connectives(text: str) -> list[Connective]:
    hits = [Connective(match.start(), entry, klass)
            for pattern, entry, klass in LEXICON
            for match in pattern.finditer(text)]
    return sorted(hits, key=Connective.key)


def candidate_id(source_kind: str, source_ref: str, text: str) -> str:
    material = "::".join((source_kind, source_ref, text))
    return f"RPC-{sha256_text(material)[:12]}"


class Pathograph:
    """The graph the registries declare, assembled without adding to it."""

    def __init__(self, root: Path, disease: str) -> None:
        self.root = root
        self.disease = disease
        self.registries = root / "disease-models" / disease / "registries"
        self.manifest_dir = root / "disease-models" / disease / "research" / "deepdive_manifests"
        self.foundation = tcf.Foundation(root, disease)

        self.losses: list[dict[str, str]] = []
        self.scanned = 0
        self.history_lines_excluded = 0

        self.claim_blocks = self.foundation.claims_raw
        self.fields = {cid: read_fields(block, CLAIM_FIELDS)
                       for cid, block in self.claim_blocks.items()}

        self.working_model = tcf.read(self.registries / "working_model_current.md")
        self.mirror = self._read_mirror()

        self.links = self._read_links()
        self.record_links = self._read_record_links()
        self.nodes = self._build_nodes()
        self.edges = self._build_edges()
        self.candidates = self._build_candidates()
        self.findings = self._build_findings()
        self.inputs = self._input_digest()

    # ------------------------------------------------------------------ inputs

    def _input_files(self) -> list[Path]:
        return sorted(
            [self.registries / "claim_registry_current.md",
             self.registries / "paper_registry_current.md",
             self.registries / "working_model_current.md"]
            + sorted(self.manifest_dir.glob("PMID*.json"))
        )

    def _input_digest(self) -> dict:
        entries = []
        for path in self._input_files():
            entries.append({
                "path": str(path.relative_to(self.root)),
                "sha256": sha256_text(tcf.read(path)),
            })
        joined = "\n".join(f"{item['path']}:{item['sha256']}" for item in entries)
        return {"files": len(entries), "digest": sha256_text(joined)}

    def lose(self, state: str, subject: str, detail: str) -> None:
        self.losses.append({"state": state, "subject": subject, "detail": detail})

    # ------------------------------------------------------------------- read

    def _read_mirror(self) -> dict[str, str]:
        """BLOCK 2 of the working model: claim id -> the mirror's own wording of the title."""
        mirror: dict[str, str] = {}
        for line in self.working_model.splitlines():
            match = MIRROR_ROW.match(line.strip())
            if match:
                mirror.setdefault(f"CLAIM {match.group(1)}", match.group(2).strip())
        return mirror

    def _read_links(self) -> list[dict]:
        """Every claim→claim link the registry declares, with its field and annotation."""
        links: list[dict] = []
        for cid, block in sorted(self.claim_blocks.items()):
            number = cid.split()[-1]
            for match in CLAIM_LINK.finditer(block):
                target = f"CLAIM {match.group(1)}"
                if match.group(1) == number:
                    self.lose("SELF_LINK", cid, "a claim links to itself")
                    continue
                raw = (match.group(2) or "").strip()
                relation, basis = self._read_relation(cid, target, raw)
                links.append({
                    "source": cid,
                    "target": target,
                    "field": field_carrying(block, match.group(0)),
                    "relation_type": relation,
                    "relation_type_basis": basis,
                    "relation_annotation": raw,
                })
        return links

    def _read_relation(self, source: str, target: str, raw: str) -> tuple[str, str]:
        if not raw:
            return UNTYPED, NO_ANNOTATION
        declared = raw.split("—")[0].split("--")[0].strip().upper()
        if declared in RELATION_VOCABULARY:
            return declared, "DECLARED_ANNOTATION"
        self.lose(UNRECOGNISED, f"{source} -> {target}",
                  f"annotation {raw!r} is not one of {', '.join(RELATION_VOCABULARY)}")
        return UNTYPED, UNRECOGNISED

    def _read_record_links(self) -> list[dict]:
        """Links from a claim to a record in another registry — declared, and not causal."""
        found: list[dict] = []
        for cid, block in sorted(self.claim_blocks.items()):
            for match in RECORD_LINK.finditer(block):
                registry, record = match.group(1), match.group(2).strip()
                if registry in ("claim_registry_current", "paper_registry_current"):
                    continue
                found.append({"source": cid, "registry": registry, "record": record})
        return sorted(found, key=lambda item: (item["source"], item["registry"], item["record"]))

    # ------------------------------------------------------------------ nodes

    def _build_nodes(self) -> list[dict]:
        degree: dict[str, int] = {cid: 0 for cid in self.claim_blocks}
        for link in self.links:
            degree[link["source"]] = degree.get(link["source"], 0) + 1
            degree[link["target"]] = degree.get(link["target"], 0) + 1

        nodes = []
        for cid in sorted(self.claim_blocks):
            declared = self.fields.get(cid, {})
            supports = self.foundation.supporting_papers(cid)
            nodes.append({
                "kind": "claim_node",
                "id": cid,
                "title": declared.get("Title", ""),
                "status": declared.get("Status", UNANNOTATED),
                "epistemic_type": declared.get("Type", UNANNOTATED),
                "pathway": declared.get("Pathway", UNANNOTATED),
                "transferability": declared.get("Transferability", UNANNOTATED),
                "clinical_relevance": declared.get("clinical relevance", UNANNOTATED),
                "genotype_model_relevance": declared.get("Genotype/model relevance", UNANNOTATED),
                # Not derived from the pathway, not derived from the model, not derived at
                # all. No registry field declares it, and a scale guessed from a pathway
                # label would be an assertion about biology wearing a schema's clothes.
                "biological_scale": UNANNOTATED,
                "evidential_papers": [paper for paper, kind in supports
                                      if kind in tcf.EVIDENTIAL_EDGES],
                "cross_reference_papers": [paper for paper, kind in supports
                                           if kind not in tcf.EVIDENTIAL_EDGES],
                "mirror_title": self.mirror.get(cid, ""),
                "claim_link_degree": degree.get(cid, 0),
            })
        return nodes

    # ------------------------------------------------------------------ edges

    def _build_edges(self) -> list[dict]:
        """Undirected pairs, carrying every direction each side declares."""
        pairs: dict[tuple[str, str], list[dict]] = {}
        for link in self.links:
            key = tuple(sorted((link["source"], link["target"])))
            pairs.setdefault(key, []).append(link)

        papers = {node["id"]: set(node["evidential_papers"]) for node in self.nodes}
        pathway = {node["id"]: node["pathway"] for node in self.nodes}
        status = {node["id"]: node["status"] for node in self.nodes}
        etype = {node["id"]: node["epistemic_type"] for node in self.nodes}

        edges = []
        for (left, right), declarations in sorted(pairs.items()):
            directions = sorted({f"{item['source']} -> {item['target']}"
                                 for item in declarations})
            types = sorted({item["relation_type"] for item in declarations})
            bases = sorted({item["relation_type_basis"] for item in declarations})
            if len(types) > 1:
                self.lose("RELATION_TYPE_CONFLICT", f"{left} <-> {right}",
                          f"the two directions declare different types: {', '.join(types)}")
            edges.append({
                "kind": "claim_edge",
                "edge_id": f"{left} <-> {right}",
                "endpoints": [left, right],
                "directions_declared": directions,
                "reciprocal": len(directions) == 2,
                "declaring_fields": sorted({item["field"] for item in declarations}),
                "relation_type": types[0] if len(types) == 1 else UNTYPED,
                "relation_type_basis": bases[0] if len(bases) == 1 else "CONFLICTING_BASES",
                # The packet a Scientist needs to type the edge, entirely from declared
                # fields. It is context for a reading, not a derivation of the type.
                "review_packet": {
                    "endpoint_status": {left: status[left], right: status[right]},
                    "endpoint_type": {left: etype[left], right: etype[right]},
                    "endpoint_pathway": {left: pathway[left], right: pathway[right]},
                    "shared_evidential_papers": sorted(papers[left] & papers[right]),
                },
                "review_state": ("TYPED" if len(types) == 1 and types[0] != UNTYPED
                                 else "AWAITING_SCIENTIST_TYPING"),
            })
        return edges

    # ------------------------------------------------------------- candidates

    def _emit_candidate(self, source_kind: str, source_ref: str, text: str,
                        evidence: dict | None = None) -> dict | None:
        self.scanned += 1
        text = " ".join(text.split())
        if not text:
            self.lose("PROPOSITION_EMPTY", source_ref, "no text to scan")
            return None
        hits = find_connectives(text)
        if not hits:
            return None
        primary = hits[0]
        left = text[:primary.start].strip(" ,;:—-")
        right = text[primary.start + len(primary.text):].strip(" ,;:—-")
        # A connective at the very start of a sentence has nothing on its left, so the
        # proposition is not stating a relation between two things — *"Controls are clean"*.
        # Degenerate, not deleted: it goes to the back of the queue with the reason attached.
        degenerate = len(left) < 3 or len(right) < 3
        return {
            "kind": "relational_proposition",
            "candidate_id": candidate_id(source_kind, source_ref, text),
            "source_kind": source_kind,
            "source_ref": source_ref,
            "text": text,
            "connective": primary.text,
            "connective_class": primary.klass,
            "connectives_all": sorted({f"{hit.klass}:{hit.text}" for hit in hits}),
            "morphology": "AMBIGUOUS_BARE_FORM" if primary.ambiguous else "FINITE_OR_MULTIWORD",
            # A split on a string, presented as a split on a string. Which biological entity
            # sits on each side is a reading; the flag says so in the record itself so no
            # consumer can mistake the halves for endpoints.
            "lexical_split": {
                "left": left,
                "right": right,
                "degenerate": degenerate,
                "endpoints_resolved": False,
            },
            "evidence": evidence or {},
            "review_priority": "LOW" if (primary.ambiguous or degenerate) else "NORMAL",
            "review_state": "AWAITING_SCIENTIST_REVIEW",
        }

    def _build_candidates(self) -> list[dict]:
        found: list[dict] = []

        for cid in sorted(self.claim_blocks):
            title = self.fields.get(cid, {}).get("Title", "")
            candidate = self._emit_candidate(
                "claim_title", f"claim_registry_current.md#{cid}|Title", title)
            if candidate:
                candidate["bound_claims"] = [cid]
                found.append(candidate)

        for cid in sorted(self.mirror):
            candidate = self._emit_candidate(
                "working_model_mirror_title",
                f"working_model_current.md#BLOCK 2|{cid}", self.mirror[cid])
            if candidate:
                candidate["bound_claims"] = [cid]
                found.append(candidate)

        found.extend(self._manifest_candidates())

        deduped: dict[str, dict] = {}
        for candidate in found:
            existing = deduped.get(candidate["candidate_id"])
            if existing is None:
                deduped[candidate["candidate_id"]] = candidate
            else:
                self.lose("CANDIDATE_DUPLICATE", candidate["candidate_id"],
                          f"{candidate['source_ref']} repeats {existing['source_ref']}")
        return sorted(deduped.values(), key=lambda item: (item["source_kind"],
                                                          item["source_ref"],
                                                          item["candidate_id"]))

    def _claims_by_pmid(self) -> dict[str, list[str]]:
        by_pmid: dict[str, list[str]] = {}
        for node in self.nodes:
            for paper in node["evidential_papers"]:
                identifier = self.foundation.papers.get(paper, {}).get("Identifier", "")
                for pmid in tcf.PMID.findall(identifier):
                    by_pmid.setdefault(pmid, []).append(node["id"])
        return {pmid: sorted(set(claims)) for pmid, claims in by_pmid.items()}

    def _manifest_candidates(self) -> list[dict]:
        bindings = self._claims_by_pmid()
        found: list[dict] = []
        for path in sorted(self.manifest_dir.glob("PMID*.json")):
            relative = str(path.relative_to(self.root))
            try:
                manifest = json.loads(tcf.read(path))
            except json.JSONDecodeError as error:
                self.lose("MANIFEST_UNREADABLE", relative, str(error))
                continue
            pmid = str(manifest.get("pmid", "")).strip()
            if not pmid:
                self.lose("MANIFEST_PMID_UNDECLARED", relative, "no pmid field")
                continue
            locators = manifest.get("verbatim_locators") or {}
            entries = locators.get("entries") or []
            for index, entry in enumerate(entries):
                proposition = str(entry.get("proposition", ""))
                candidate = self._emit_candidate(
                    "locator_proposition", f"{relative}|entries[{index}]", proposition,
                    evidence={
                        "pmid": pmid,
                        "receipt": manifest.get("receipt", ""),
                        "surface": entry.get("surface", UNANNOTATED),
                        "artifact": entry.get("artifact", UNANNOTATED),
                        "anchor": entry.get("anchor", ""),
                        "snippet": entry.get("snippet", ""),
                    })
                if candidate:
                    candidate["bound_claims"] = bindings.get(pmid, [])
                    found.append(candidate)
        return found

    # --------------------------------------------------------------- findings

    def _build_findings(self) -> dict:
        linked = {endpoint for edge in self.edges for endpoint in edge["endpoints"]}
        isolated = sorted(set(self.claim_blocks) - linked)

        asymmetric = [
            {"edge_id": edge["edge_id"],
             "declared": edge["directions_declared"],
             "missing": f"{edge['endpoints'][1]} -> {edge['endpoints'][0]}"
                        if edge["directions_declared"] == [
                            f"{edge['endpoints'][0]} -> {edge['endpoints'][1]}"]
                        else f"{edge['endpoints'][0]} -> {edge['endpoints'][1]}"}
            for edge in self.edges if not edge["reciprocal"]
        ]

        unlinked = self._unlinked_mentions()
        comentions = self._working_model_comentions()

        shared = self._shared_evidence_without_edge()
        self_relational = self._self_relational_nodes()
        self_relational_ids = {item["claim"] for item in self_relational}
        locator_bound = {claim for candidate in self.candidates
                         if candidate["source_kind"] == "locator_proposition"
                         for claim in candidate.get("bound_claims", [])}

        # 🔴 An asserted relation and a place to look are not the same finding, and the
        # first version of this classifier merged them into one "suspected gap". A claim
        # named in another claim's prose, or paired with one in a working-model sentence, is
        # a relationship this repository already states and has not annotated — a gap, and a
        # confirmed one. A claim that shares a paper with another, or whose title happens to
        # be relational, is material for a reading. Merging them handed a Scientist fourteen
        # equally weighted items of which two were actually established.
        confirming = ("UNLINKED_PROSE_MENTION", "WORKING_MODEL_COMENTION")
        classified = []
        for cid in isolated:
            reasons = []
            if cid in {item["source"] for item in unlinked} or \
               cid in {item["target"] for item in unlinked}:
                reasons.append("UNLINKED_PROSE_MENTION")
            if any(cid in pair["claims"] for pair in comentions):
                reasons.append("WORKING_MODEL_COMENTION")
            if any(cid in pair["claims"] for pair in shared):
                reasons.append("SHARED_EVIDENTIAL_PAPER")
            if cid in self_relational_ids:
                reasons.append("SELF_RELATIONAL_TITLE")
            if cid in locator_bound:
                reasons.append("LOCATOR_PROPOSITION_BOUND")
            if any(reason in confirming for reason in reasons):
                verdict = "ANNOTATION_GAP_CONFIRMED"
            elif reasons:
                verdict = "REVIEW_MATERIAL_PRESENT"
            else:
                # A statement about this repository, never about biology: the assembler
                # found nothing here to annotate. The literature is not the denominator.
                verdict = "NO_RELATION_MATERIAL_IN_REPOSITORY"
            classified.append({"claim": cid, "verdict": verdict,
                               "material": sorted(set(reasons))})

        return {
            "isolated_claims": classified,
            "self_relational_nodes": self_relational,
            "mirror_relational_disagreement": self._mirror_disagreement(),
            "asymmetric_links": sorted(asymmetric, key=lambda item: item["edge_id"]),
            "unlinked_prose_mentions": unlinked,
            "working_model_comentions": comentions,
            "working_model_history_lines_excluded": self.history_lines_excluded,
            "shared_evidence_without_edge": shared,
            "scale_annotation": {
                "vocabulary": list(BIOLOGICAL_SCALES),
                "nodes_total": len(self.nodes),
                "nodes_annotated": sum(1 for node in self.nodes
                                       if node["biological_scale"] != UNANNOTATED),
            },
            "typing": {
                "edges_total": len(self.edges),
                "edges_typed": sum(1 for edge in self.edges
                                   if edge["relation_type"] != UNTYPED),
                "vocabulary": list(RELATION_VOCABULARY),
            },
        }

    def _mirror_disagreement(self) -> list[dict]:
        """Nodes where the registry title and the working-model mirror row disagree on
        whether the claim states a relation at all.

        The two are the same node written twice, and a LINT rule keeps their *status* in
        sync. Nothing keeps their relational content in sync, and it has diverged: the mirror
        writes *"Vigabatrin → VABAM"* where the registry writes *"Vigabatrin associated with
        VABAM"*, and elsewhere the arrow exists on only one side. Which wording is right is
        a reading; that they disagree is a measurement, and it is the normalisation this
        layer is for.
        """
        by_source: dict[str, dict[str, dict]] = {"claim_title": {},
                                                 "working_model_mirror_title": {}}
        for candidate in self.candidates:
            if candidate["source_kind"] in by_source:
                for cid in candidate.get("bound_claims", []):
                    by_source[candidate["source_kind"]][cid] = candidate
        registry = set(by_source["claim_title"])
        mirror = set(by_source["working_model_mirror_title"])
        found = []
        for cid in sorted(registry ^ mirror):
            side = "registry title only" if cid in registry else "mirror row only"
            candidate = by_source["claim_title" if cid in registry
                                  else "working_model_mirror_title"][cid]
            found.append({
                "claim": cid,
                "relational_in": side,
                "connective": candidate["connective"],
                "text": candidate["text"],
                "other_wording": (self.mirror.get(cid, "") if cid in registry
                                  else self.fields.get(cid, {}).get("Title", "")),
            })
        return found

    def _self_relational_nodes(self) -> list[dict]:
        """Claims whose own declared title states a relation.

        🔴 This is the shape of the graph as it stands, and it is why the layer looked
        empty. *"Neuronal WWOX deletion induces non-cell-autonomous hypomyelination"* is an
        edge — a cause, a relation and an effect — compressed into a node label. The causal
        content of this model is largely *inside* its nodes rather than on its edges, which
        is exactly the material a decomposition would work from and exactly the reading the
        Orchestrator must not perform: splitting that title into two entities and a typed
        relation decides which half is the cause.
        """
        found = []
        for candidate in self.candidates:
            if candidate["source_kind"] != "claim_title":
                continue
            for cid in candidate.get("bound_claims", []):
                found.append({
                    "claim": cid,
                    "title": candidate["text"],
                    "connective": candidate["connective"],
                    "connective_class": candidate["connective_class"],
                    "morphology": candidate["morphology"],
                    "candidate_id": candidate["candidate_id"],
                })
        return sorted(found, key=lambda item: item["claim"])

    def _unlinked_mentions(self) -> list[dict]:
        """`CLAIM 009` written in prose where no wikilink annotates the relation."""
        declared = {(link["source"], link["target"]) for link in self.links}
        found: list[dict] = []
        for cid, block in sorted(self.claim_blocks.items()):
            number = cid.split()[-1]
            masked = ANY_WIKILINK.sub(" ", block)
            for target_number in sorted(set(BARE_CLAIM.findall(masked))):
                if target_number == number:
                    continue
                target = f"CLAIM {target_number}"
                if (cid, target) in declared:
                    continue
                # The field is located in the *masked* text: the same claim number occurs
                # inside the wikilink that annotates a different relation, and searching the
                # raw block would report whichever line came first.
                found.append({"source": cid, "target": target,
                              "field": field_carrying(masked, f"CLAIM {target_number}")})
        return found

    def _working_model_comentions(self) -> list[dict]:
        """Two claims named in one working-model sentence with no edge between them.

        Line-scoped first, then sentence-scoped: a mirror row is one line and must not merge
        with its neighbours, and a narrative paragraph must not merge two sentences that
        happen to sit together.

        The version history is excluded — see `HISTORY_ROW` — and the count of excluded
        lines is carried out of here so the report can state the bound.
        """
        pairs: dict[tuple[str, str], str] = {}
        undirected = {tuple(sorted(edge["endpoints"])) for edge in self.edges}
        for line in self._model_lines():
            for sentence in SENTENCE_SPLIT.split(line):
                mentioned = sorted({f"CLAIM {number}"
                                    for number in BARE_CLAIM.findall(sentence)})
                for index, left in enumerate(mentioned):
                    for right in mentioned[index + 1:]:
                        key = (left, right)
                        if key in undirected or key in pairs:
                            continue
                        pairs[key] = " ".join(sentence.split())
        return [{"claims": list(key), "sentence": value}
                for key, value in sorted(pairs.items())]

    def _model_lines(self) -> list[str]:
        """Working-model lines that state the model, with the version history removed."""
        kept: list[str] = []
        self.history_lines_excluded = 0
        for line in self.working_model.splitlines():
            stripped = line.strip()
            if (HISTORY_ROW.match(stripped) or CHANGELOG_FIELD.match(stripped)
                    or BATCH_ID.search(stripped)):
                self.history_lines_excluded += 1
                continue
            kept.append(line)
        return kept

    def _shared_evidence_without_edge(self) -> list[dict]:
        """Two claims resting on the same paper, with no edge declared between them.

        🔴 This is not a missing edge. Two claims can rest on one paper and stand in no
        relation whatsoever — a cohort study supports a genotype claim and a respiratory
        claim at once. It is listed as a review candidate, at the bottom of the priority
        order, and typing any of it is Scientist work.
        """
        undirected = {tuple(sorted(edge["endpoints"])) for edge in self.edges}
        papers = {node["id"]: set(node["evidential_papers"]) for node in self.nodes}
        found: list[dict] = []
        identifiers = sorted(papers)
        for index, left in enumerate(identifiers):
            for right in identifiers[index + 1:]:
                shared = sorted(papers[left] & papers[right])
                if shared and (left, right) not in undirected:
                    found.append({"claims": [left, right], "shared_papers": shared})
        return found

    # ---------------------------------------------------------------- outputs

    def coverage(self) -> dict:
        manifests = sorted(self.manifest_dir.glob("PMID*.json"))
        bindings = self._claims_by_pmid()
        bound = sum(1 for candidate in self.candidates
                    if candidate["source_kind"] == "locator_proposition"
                    and candidate.get("bound_claims"))
        locator_candidates = sum(1 for candidate in self.candidates
                                 if candidate["source_kind"] == "locator_proposition")
        return {
            "claims_total": len(self.nodes),
            # Three different denominators that are easy to quote as one another: the raw
            # wikilink occurrences in the registry, the distinct directed links they resolve
            # to, and the undirected edges those pairs collapse into. On this corpus they
            # are 41, 30 and 20. All three are correct and none is "the number of edges".
            "claim_link_occurrences": len(self.links),
            "claim_links_directed_distinct": len({(link["source"], link["target"])
                                                  for link in self.links}),
            "manifests_total": len(manifests),
            "manifests_bound_to_a_claim": sum(1 for path in manifests
                                              for match in [re.match(r"PMID(\d+)", path.name)]
                                              if match and match.group(1) in bindings),
            "propositions_scanned": self.scanned,
            "candidates_emitted": len(self.candidates),
            "candidates_without_connective": self.scanned - len(self.candidates) - sum(
                1 for loss in self.losses
                if loss["state"] in ("PROPOSITION_EMPTY", "CANDIDATE_DUPLICATE")),
            "locator_candidates": locator_candidates,
            "locator_candidates_bound_to_a_claim": bound,
            "candidates_normal_priority": sum(1 for candidate in self.candidates
                                              if candidate["review_priority"] == "NORMAL"),
            "candidates_low_priority": sum(1 for candidate in self.candidates
                                           if candidate["review_priority"] == "LOW"),
        }

    def assemble(self) -> dict:
        coverage = self.coverage()
        # emitted + lost + no-connective == scanned. A candidate population that does not
        # balance means propositions were dropped between the scan and the report.
        accounted = (coverage["candidates_emitted"]
                     + coverage["candidates_without_connective"]
                     + sum(1 for loss in self.losses
                           if loss["state"] in ("PROPOSITION_EMPTY", "CANDIDATE_DUPLICATE")))
        if accounted != coverage["propositions_scanned"]:
            raise AssertionError(
                f"candidate accounting does not balance: {accounted} accounted for "
                f"against {coverage['propositions_scanned']} scanned")
        return {
            "record_kind": "pathograph_inventory",
            "schema_version": 1,
            "disease": self.disease,
            "inputs": self.inputs,
            "coverage": coverage,
            "nodes": self.nodes,
            "edges": self.edges,
            "claim_to_record_links": self.record_links,
            "candidates": self.candidates,
            "findings": self.findings,
            "losses": sorted(self.losses, key=lambda item: (item["state"], item["subject"])),
        }


# ---------------------------------------------------------------- rendering


SAMPLE = 12


def _table(rows: list[list[str]], header: list[str]) -> list[str]:
    lines = ["| " + " | ".join(header) + " |",
             "|" + "|".join("---" for _ in header) + "|"]
    lines.extend("| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |"
                 for row in rows)
    return lines


def render_markdown(graph: dict, command: str) -> str:
    coverage = graph["coverage"]
    findings = graph["findings"]
    out: list[str] = []
    out.append("# WWOX pathograph — inventory of the graph the registries already declare")
    out.append("")
    out.append(f"> **{MARKER} — do not edit by hand.** Regenerate with:")
    out.append("> ```bash")
    out.append(f"> {command}")
    out.append("> ```")
    out.append("> It is a *view* over the canonical registries plus the deep-dive work")
    out.append("> manifests, never a second source of truth. A regression re-derives it and")
    out.append("> fails if this file has drifted.")
    out.append("")
    out.append("> **Public edition — de-identified.** Disease-level only. Nothing here is")
    out.append("> medical advice, and nothing here describes an individual.")
    out.append("")
    out.append("## What this page is")
    out.append("")
    out.append("The causal layer is assembled, not authored. Every node below is an existing")
    out.append("claim record, every edge is a link the registry already declares, and every")
    out.append("candidate is a sentence already written in this repository. The assembler")
    out.append("adds no relationship and types no edge: a relation type appears here only")
    out.append("when a claim record annotates the link with one, and the count of those")
    out.append("annotations is reported below whatever it happens to be.")
    out.append("")
    out.append("## Population and coverage")
    out.append("")
    out.extend(_table([
        ["Claim nodes", str(coverage["claims_total"])],
        ["Claim→claim wikilink occurrences", str(coverage["claim_link_occurrences"])],
        ["…distinct directed links", str(coverage["claim_links_directed_distinct"])],
        ["…undirected edges they collapse into", str(findings["typing"]["edges_total"])],
        ["Edges carrying a declared relation type", str(findings["typing"]["edges_typed"])],
        ["Nodes carrying a biological scale", str(findings["scale_annotation"]["nodes_annotated"])],
        ["Deep-dive manifests read", str(coverage["manifests_total"])],
        ["…of which bound to at least one claim", str(coverage["manifests_bound_to_a_claim"])],
        ["Propositions scanned", str(coverage["propositions_scanned"])],
        ["…carrying a relational connective", str(coverage["candidates_emitted"])],
        ["…locator-backed candidates", str(coverage["locator_candidates"])],
        ["…locator-backed and bound to a claim", str(coverage["locator_candidates_bound_to_a_claim"])],
    ], ["Measure", "Count"]))
    out.append("")
    out.append("The scanned population is three declared surfaces and no others: every claim")
    out.append("`Title`, every row of the working model's BLOCK 2 mirror, and every")
    out.append("`proposition` in every deep-dive work manifest. `Summary`, `Clinical meaning`")
    out.append("and `Evidence boundary` are prose paragraphs and are **not** scanned —")
    out.append("atomizing a paragraph is a reading operation with its own contract, and a")
    out.append("regex sweep of one would produce fragments wearing an extraction's authority.")
    out.append("")

    out.append("## 1 · Nodes")
    out.append("")
    out.extend(_table([
        [node["id"], node["title"][:96], node["status"], node["epistemic_type"][:40],
         node["pathway"][:40], node["biological_scale"], str(node["claim_link_degree"]),
         str(len(node["evidential_papers"]))]
        for node in graph["nodes"]
    ], ["Node", "Declared title", "Status", "Type", "Pathway", "Scale", "Deg", "Papers"]))
    out.append("")

    out.append("## 2 · Edges declared by the registry")
    out.append("")
    out.extend(_table([
        [edge["edge_id"],
         "yes" if edge["reciprocal"] else "**one-way**",
         ", ".join(edge["declaring_fields"]),
         edge["relation_type"],
         edge["relation_type_basis"],
         ", ".join(edge["review_packet"]["shared_evidential_papers"]) or "—"]
        for edge in graph["edges"]
    ], ["Edge", "Reciprocal", "Declared in", "Type", "Basis", "Shared evidence"]))
    out.append("")
    out.append("Every edge carrying `NO_DECLARED_RELATION_ANNOTATION` is an edge that exists")
    out.append("and has never been given a direction of causation, an intermediate, or an")
    out.append("evidence type. Typing it requires reading the evidence behind both endpoints;")
    out.append("the assembler refuses to derive it from the endpoints' declared fields,")
    out.append("because two demonstrated facts are not a demonstrated relation between them.")
    out.append("")
    out.append("A Scientist types an edge by annotating the wikilink in the claim record:")
    out.append("")
    out.append("```markdown")
    out.append("[[claim_registry_current#CLAIM 004]] (relation: DIRECT — the same experiment")
    out.append("measures both endpoints)")
    out.append("```")
    out.append("")
    out.append(f"Accepted values: `{'` · `'.join(RELATION_VOCABULARY)}`. Anything else is")
    out.append("reported as `RELATION_TYPE_UNRECOGNISED` and is never coerced into a type.")
    out.append("")

    out.append("## 3 · Where the causal content actually sits")
    out.append("")
    relational = findings["self_relational_nodes"]
    out.append(f"{len(relational)} of {coverage['claims_total']} claim titles state a")
    out.append("relation, and every declared edge states none. The causal content of this")
    out.append("model is largely **inside its nodes**: *\"Neuronal WWOX deletion induces")
    out.append("non-cell-autonomous hypomyelination\"* is a cause, a relation and an effect")
    out.append("compressed into a node label. That is why the edge layer reads as empty —")
    out.append("not because the relationships were never established, but because they were")
    out.append("written where a graph cannot see them.")
    out.append("")
    out.append("Decomposing such a title into two entities and a typed relation decides")
    out.append("which half is the cause. That is a reading, and it is Scientist work; the")
    out.append("assembler lists the titles and stops there.")
    out.append("")
    out.extend(_table([
        [item["claim"], f"`{item['connective']}`", item["connective_class"],
         item["morphology"].replace("_", " ").casefold(), item["title"][:90]]
        for item in relational
    ], ["Node", "Connective", "Class", "Morphology", "Declared title"]))
    out.append("")
    disagreement = findings["mirror_relational_disagreement"]
    if disagreement:
        out.append("### 3.1 Where the two wordings of a node disagree")
        out.append("")
        out.append("Each node is written twice — once as a registry `Title`, once as a row of")
        out.append("the working model's BLOCK 2 mirror — and a LINT rule keeps their *status*")
        out.append("in sync. Nothing keeps their relational content in sync, and it has")
        out.append("diverged. Which wording is right is a reading; that they disagree is a")
        out.append("measurement, and normalising it is what this layer is for.")
        out.append("")
        out.append("🔴 Not every row here is a difference in content. A multi-word connective")
        out.append("is matched as one string, so an adverb inserted into it — *\"contributes")
        out.append("**directly** to\"* — reads as absent. Read the two wordings, not the flag.")
        out.append("")
        out.extend(_table([
            [item["claim"], item["relational_in"], f"`{item['connective']}`",
             item["text"][:70], item["other_wording"][:70]]
            for item in disagreement
        ], ["Node", "Relational in", "Connective", "That wording", "The other wording"]))
        out.append("")

    out.append("## 4 · What is absent, separated by *kind* of absence")
    out.append("")
    out.append("### 4.1 Annotation gaps — the relationship is in the repository, the edge is not")
    out.append("")
    if findings["asymmetric_links"]:
        out.append("**One-way links.** One side declares the link and the other does not.")
        out.append("")
        out.extend(_table([[item["edge_id"], ", ".join(item["declared"]), item["missing"]]
                           for item in findings["asymmetric_links"]],
                          ["Edge", "Declared", "Not declared"]))
        out.append("")
    if findings["unlinked_prose_mentions"]:
        out.append("**Unlinked prose mentions.** A claim names another claim in prose with no")
        out.append("wikilink, so the relation is asserted in text and invisible to the graph.")
        out.append("")
        out.extend(_table([[item["source"], item["target"], item["field"]]
                           for item in findings["unlinked_prose_mentions"]],
                          ["Claim", "Names", "In field"]))
        out.append("")
    if findings["working_model_comentions"]:
        out.append("**Working-model co-mentions.** Two claims named in one sentence of the")
        out.append("working model with no edge between them in the registry.")
        out.append("")
        out.extend(_table([[" ↔ ".join(item["claims"]), item["sentence"][:150]]
                           for item in findings["working_model_comentions"]],
                          ["Claims", "Sentence"]))
        out.append("")

    out.append("### 4.2 Isolated nodes")
    out.append("")
    out.extend(_table([[item["claim"], item["verdict"], ", ".join(item["material"]) or "—"]
                       for item in findings["isolated_claims"]],
                      ["Node", "Verdict", "Material found in the repository"]))
    out.append("")
    out.append("🔴 `NO_RELATION_MATERIAL_IN_REPOSITORY` is a statement about this repository,")
    out.append("not about biology. It means the assembler found nothing here to annotate — no")
    out.append("unlinked mention, no co-mention, no shared evidential paper, no relational")
    out.append("proposition bound to the claim. The literature is not the denominator.")
    out.append("")

    out.append("### 4.3 Shared evidence without an edge — review candidates, lowest priority")
    out.append("")
    out.append("Two claims resting on the same paper are not thereby related. This list is a")
    out.append("place to look, not a set of missing edges.")
    out.append("")
    shared = findings["shared_evidence_without_edge"]
    out.extend(_table([[" ↔ ".join(item["claims"]), ", ".join(item["shared_papers"])]
                       for item in shared[:SAMPLE]],
                      ["Claims", "Shared evidential papers"]))
    if len(shared) > SAMPLE:
        out.append("")
        out.append(f"Showing {SAMPLE} of {len(shared)}. The complete list is in the export.")
    out.append("")

    out.append("## 5 · Candidate edges — propositions already written, awaiting review")
    out.append("")
    out.append("A candidate is a sentence that already exists in the repository and contains a")
    out.append("connective from the closed lexicon. It is **not** an edge. The lexical split")
    out.append("shown in the export is a split on a string; which biological entity sits on")
    out.append("each side is a reading, and every record carries `endpoints_resolved: false`.")
    out.append("")
    by_kind: dict[str, int] = {}
    by_class: dict[str, int] = {}
    for candidate in graph["candidates"]:
        by_kind[candidate["source_kind"]] = by_kind.get(candidate["source_kind"], 0) + 1
        by_class[candidate["connective_class"]] = by_class.get(candidate["connective_class"], 0) + 1
    out.extend(_table([[kind, str(count)] for kind, count in sorted(by_kind.items())],
                      ["Source", "Candidates"]))
    out.append("")
    out.extend(_table([[klass, str(count)] for klass, count in sorted(by_class.items())],
                      ["Connective class (lexical)", "Candidates"]))
    out.append("")
    out.append("A connective class is a property of the word, not a verdict about the")
    out.append("relationship. An `ASSOCIATIVE` connective does not make an edge `ASSOCIATED`.")
    out.append("")
    out.append("### 5.1 Candidates bound to a claim node")
    out.append("")
    bound = [candidate for candidate in graph["candidates"] if candidate.get("bound_claims")]
    out.extend(_table([
        [", ".join(candidate["bound_claims"]),
         candidate["source_kind"],
         f"`{candidate['connective']}`",
         candidate["text"][:120]]
        for candidate in bound[:SAMPLE]
    ], ["Bound to", "Source", "Connective", "Proposition (verbatim)"]))
    out.append("")
    out.append(f"Showing {min(SAMPLE, len(bound))} of {len(bound)} bound candidates; the")
    out.append("complete set, with evidence and provenance, is in the export. The worklist")
    out.append("in cost order — what needs an annotation, what needs a type, what needs a")
    out.append("decomposition, what needs a reading — is printed by:")
    out.append("")
    out.append("```bash")
    out.append("python3 framework/scripts/pathograph.py --disease wwox --queue --limit 20")
    out.append("```")
    out.append("")

    out.append("## 6 · Losses")
    out.append("")
    if graph["losses"]:
        out.extend(_table([[loss["state"], loss["subject"], loss["detail"][:110]]
                           for loss in graph["losses"]],
                          ["State", "Subject", "Detail"]))
    else:
        out.append("None. Every scanned proposition was either emitted as a candidate or")
        out.append("carried no connective from the lexicon.")
    out.append("")
    out.append("## Provenance")
    out.append("")
    out.append(f"Derived from {graph['inputs']['files']} input files; digest")
    out.append(f"`{graph['inputs']['digest'][:16]}`. Sources: the claim, paper and")
    out.append("working-model registries, and every deep-dive work manifest.")
    out.append("")
    return "\n".join(out) + "\n"


def render_export(graph: dict) -> str:
    """One JSON object per line: manifest first, then nodes, edges, candidates, findings."""
    records = [{
        "record_kind": "derivation_manifest",
        "schema_version": graph["schema_version"],
        "disease": graph["disease"],
        "inputs": graph["inputs"],
        "coverage": graph["coverage"],
        "relation_vocabulary": list(RELATION_VOCABULARY),
        "biological_scale_vocabulary": list(BIOLOGICAL_SCALES),
        "connective_lexicon": {klass: sorted(entries)
                               for klass, entries in CONNECTIVES.items()},
        "generated_by": "framework/scripts/pathograph.py",
        "authored_content": "none — every record is a transformation of a declared input",
        "serialisation": "one JSON object per line, sort_keys=True, ensure_ascii=False",
    }]
    records.extend(graph["nodes"])
    records.extend(graph["edges"])
    records.extend({"kind": "claim_to_record_link", **link}
                   for link in graph["claim_to_record_links"])
    records.extend(graph["candidates"])
    records.append({"kind": "findings", **graph["findings"]})
    records.extend({"kind": "loss", **loss} for loss in graph["losses"])
    return "".join(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n"
                   for record in records)


def regeneration_command(disease: str, out: str | None, export: str | None) -> str:
    parts = ["python3 framework/scripts/pathograph.py", f"--disease {disease}"]
    if out:
        parts.append(f"\\\n>     --out {out}")
    if export:
        parts.append(f"\\\n>     --export {export}")
    return " ".join(parts)


def render_report(graph: dict) -> str:
    coverage = graph["coverage"]
    findings = graph["findings"]
    lines = [
        f"PATHOGRAPH — {graph['disease']} (assembled, not authored)",
        "",
        f"  nodes                          {coverage['claims_total']}",
        f"  claim->claim link occurrences  {coverage['claim_link_occurrences']}"
        f" -> {coverage['claim_links_directed_distinct']} distinct directed",
        f"  declared claim<->claim edges   {findings['typing']['edges_total']}",
        f"  edges with a declared type     {findings['typing']['edges_typed']}"
        f" of {findings['typing']['edges_total']}",
        f"  nodes with a biological scale  {findings['scale_annotation']['nodes_annotated']}"
        f" of {findings['scale_annotation']['nodes_total']}",
        f"  propositions scanned           {coverage['propositions_scanned']}",
        f"  candidate relational props     {coverage['candidates_emitted']}",
        f"  ...normal review priority      {coverage['candidates_normal_priority']}",
        f"  ...low (ambiguous/degenerate)  {coverage['candidates_low_priority']}",
        f"  ...bound to a claim node       {coverage['locator_candidates_bound_to_a_claim']}"
        f" of {coverage['locator_candidates']} locator-backed",
        "",
        f"  claim titles that state a relation "
        f"{len(findings['self_relational_nodes'])} of {coverage['claims_total']}"
        f"  <- the causal content is inside the nodes",
        f"  registry/mirror disagree on it {len(findings['mirror_relational_disagreement'])}",
        "",
        "ABSENCES, BY KIND",
        f"  one-way links                  {len(findings['asymmetric_links'])}",
        f"  unlinked prose mentions        {len(findings['unlinked_prose_mentions'])}",
        f"  working-model co-mentions      {len(findings['working_model_comentions'])}",
        f"  isolated nodes                 {len(findings['isolated_claims'])}",
        f"  ...gap confirmed               "
        f"{sum(1 for item in findings['isolated_claims'] if item['verdict'] == 'ANNOTATION_GAP_CONFIRMED')}",
        f"  ...review material present     "
        f"{sum(1 for item in findings['isolated_claims'] if item['verdict'] == 'REVIEW_MATERIAL_PRESENT')}",
        f"  ...no material in repository   "
        f"{sum(1 for item in findings['isolated_claims'] if item['verdict'] == 'NO_RELATION_MATERIAL_IN_REPOSITORY')}",
        f"  shared evidence, no edge       {len(findings['shared_evidence_without_edge'])}",
        f"  losses                         {len(graph['losses'])}",
    ]
    return "\n".join(lines) + "\n"


def render_queue(graph: dict, limit: int) -> str:
    """The Scientist worklist, in the order the evidence makes cheapest to settle.

    Ordering is by *what has already been established*, not by importance: a relation this
    repository already states in prose needs an annotation, not a reading; an untyped edge
    with shared evidence has one paper to open; a bound candidate has a quote attached. The
    order is a cost order and nothing else — none of it ranks biological significance, which
    is not the assembler's to rank.
    """
    findings = graph["findings"]
    lines = [f"PATHOGRAPH REVIEW QUEUE — {graph['disease']}", ""]

    lines.append("A · ANNOTATE — the relation is already stated, the edge is not")
    for item in findings["unlinked_prose_mentions"]:
        lines.append(f"    {item['source']} names {item['target']} in `{item['field']}`"
                     f" with no wikilink")
    for item in findings["working_model_comentions"]:
        lines.append(f"    {' + '.join(item['claims'])} paired in one working-model sentence")
    for item in findings["asymmetric_links"]:
        lines.append(f"    {item['edge_id']} is declared one way only"
                     f" — {item['missing']} is missing")
    lines.append("")

    lines.append("B · TYPE — the edge exists and carries no relation type")
    for edge in graph["edges"]:
        if edge["review_state"] != "AWAITING_SCIENTIST_TYPING":
            continue
        shared = edge["review_packet"]["shared_evidential_papers"]
        lines.append(f"    {edge['edge_id']}"
                     f" — shared evidence: {', '.join(shared) if shared else 'none'}")
    lines.append("")

    lines.append("C · DECOMPOSE — the node title carries the relation")
    for item in findings["self_relational_nodes"]:
        # The connective is flagged when it is one of the bare forms that double as nouns
        # here — *"quality control"*, *"seizure control"*, *"the rescue"*. The title still
        # belongs in the queue; the matched word may simply not be the relation in it.
        flag = " [ambiguous form]" if item["morphology"] == "AMBIGUOUS_BARE_FORM" else ""
        lines.append(f"    {item['claim']} `{item['connective']}`{flag}"
                     f" — {item['title'][:80]}")
    lines.append("")

    lines.append("D · REVIEW — locator-backed candidate propositions bound to a node")
    ranked = [candidate for candidate in graph["candidates"]
              if candidate["review_priority"] == "NORMAL"
              and candidate["source_kind"] == "locator_proposition"
              and candidate.get("bound_claims")]
    for candidate in ranked[:limit]:
        lines.append(f"    {', '.join(candidate['bound_claims'])}"
                     f" | PMID {candidate['evidence']['pmid']}"
                     f" | {candidate['text'][:96]}")
    if len(ranked) > limit:
        lines.append(f"    ... {len(ranked) - limit} more; raise --limit or read the export")
    lines.append("")
    low = graph["coverage"]["candidates_low_priority"]
    lines.append(f"Not listed here: {low} candidates whose connective is an ambiguous bare "
                 f"form or whose split is degenerate. They are in the export, at the back "
                 f"of the queue, not discarded.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--disease", default="wwox", help="disease model to assemble")
    parser.add_argument("--json", action="store_true", help="machine-readable inventory")
    parser.add_argument("--queue", action="store_true",
                        help="print the Scientist review worklist in cost order")
    parser.add_argument("--limit", type=int, default=20,
                        help="how many candidate propositions the queue lists")
    parser.add_argument("--out", help="write the generated Markdown surface to this path")
    parser.add_argument("--export", help="write the JSONL export to this path")
    parser.add_argument("--verify", action="store_true",
                        help="re-derive and compare against --out / --export; exit 1 on drift")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    graph = Pathograph(root, args.disease).assemble()
    command = regeneration_command(args.disease, args.out, args.export)
    markdown = render_markdown(graph, command)
    export = render_export(graph)

    if args.verify:
        drift = []
        for path_value, expected, label in ((args.out, markdown, "markdown"),
                                            (args.export, export, "export")):
            if not path_value:
                continue
            path = root / path_value
            if not path.is_file():
                drift.append(f"{label}: {path_value} does not exist")
                continue
            if path.read_text(encoding="utf-8") != expected:
                drift.append(f"{label}: {path_value} has drifted from its sources")
        if not args.out and not args.export:
            print("--verify needs --out and/or --export to compare against", file=sys.stderr)
            return 2
        for line in drift:
            print(f"DRIFT {line}", file=sys.stderr)
        print("VERIFY: DRIFT" if drift else "VERIFY: CURRENT")
        return 1 if drift else 0

    if args.out:
        path = root / args.out
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8")
    if args.export:
        path = root / args.export
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(export, encoding="utf-8")

    if args.json:
        print(json.dumps(graph, sort_keys=True, ensure_ascii=False, indent=2))
    elif args.queue:
        print(render_queue(graph, args.limit), end="")
    else:
        print(render_report(graph), end="")
        if args.out:
            print(f"written: {args.out}")
        if args.export:
            print(f"written: {args.export}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
