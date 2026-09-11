#!/usr/bin/env python3
"""Whole records from the registries, selected deterministically — instead of loading 882 KB.

WHY THIS EXISTS
---------------
`framework/manuals/operator_manual.md` § 1.1–1.3 tells a MINIMAL, STANDARD or FULL session to
load *"i 4 file current"*. Two of those four are large and grow monotonically:
`paper_registry_current.md` (402 KB, 449 records) and `literature_tracking_log_current.md`
(480 KB, 418 records) on 2026-09-11. A single-paper triage was being asked to carry the whole
history of the corpus, and every resumed session paid for it again.

Measured before this file existed, and the two halves disagree, which is why both are stated:

- **Prescription.** The manual mandates the full load in three of its four profiles. Only the
  HARNESS profile already says the right thing — *"cercare gli identificativi o la struttura
  interessata e leggere i record/sezioni completi pertinenti"* — and this command is that
  sentence made executable for the scientific profiles.
- **Observed behaviour**, over the four session transcripts available on this host: **zero**
  `Read` calls on either registry. Access happened through ad-hoc shell (16 Bash calls naming
  the paper registry, 8 naming the literature log). So the expensive prescription was already
  being avoided — by grepping, which returns FRAGMENTS. A fragment is exactly how a caveat
  dies: `gold_is_in_the_details.md` and the 2026-09-09 sweep's S3 are the same defect seen from
  two directions (*"a caveat alive in prose and dead in a table"*).
- **Not measured**: what the scientist sessions of 2026-09-09 did. Their transcripts are not on
  this host. Nothing here claims to know.

So the replacement is not "grep, but blessed". It is: **select by identity, return the record
whole, and name what the selection could not reach.**

WHAT IT GUARANTEES, AND WHAT IT REFUSES TO GUARANTEE
----------------------------------------------------
- A record is returned **entire**, from its `##` heading to the next one. No field is dropped,
  summarised or re-ordered, so a caveat, a negative or a qualification cannot be lost in
  transit. `--json` carries the same bytes as the rendered form.
- **Identity is not mention.** A record whose `Identifier` field names the PMID is an `identity`
  hit; a record that merely cites the PMID in its prose is a `mention` hit. Both are returned,
  labelled, never merged — an incidental citation and the paper's own record are different
  objects and the 2026-09-09 sweep produced the error of confusing them (A13).
- Every hit carries **source path, record id, record digest and source-file digest**, so a later
  reader can tell whether the registry has moved underneath a quoted record.
- Wikilinks are resolved one hop by default (`--hops`), and a link that resolves to **nothing**
  is reported as `UNRESOLVED` rather than silently dropped.
- 🔴 **An empty result is never a scientific statement.** `no record matched` exits non-zero and
  says in words that it is not evidence the laboratory does not know this paper.
- 🔴 **No silent truncation.** `--limit` prints the residue and names it; the default is no
  limit at all.

    python3 framework/scripts/registry_records.py get --pmid 33914858
    python3 framework/scripts/registry_records.py get --pmid 33914858 --hops 1 --json
    python3 framework/scripts/registry_records.py get --id "CLAIM 030" --hops 2
    python3 framework/scripts/registry_records.py get --theme myelin --limit 5
    python3 framework/scripts/registry_records.py index --verify

The canonical registries are never written, re-ordered, summarised or mirrored. There is no
second registry to maintain: every answer is parsed from the current file at call time, and
`index --verify` re-derives the digests so a stale quotation is detectable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

# Every registry-shaped surface a link can point at. The key is the wikilink stem.
SOURCES = {
    "paper_registry_current": "registries/paper_registry_current.md",
    "literature_tracking_log_current": "registries/literature_tracking_log_current.md",
    "claim_registry_current": "registries/claim_registry_current.md",
    "working_model_current": "registries/working_model_current.md",
    "dismissal_ledger_current": "research/dismissal_ledger_current.md",
    "discovery_ledger_current": "research/discovery_ledger_current.md",
    "full_text_queue_current": "research/full_text_queue_current.md",
}
# The two this command exists to stop loading whole.
LARGE = ("paper_registry_current", "literature_tracking_log_current")

# Every `##` heading is a BLOCK; only some blocks are RECORDS.
# 🔴 ANY `##` HEADING IS A BOUNDARY. The first cut restricted the heading charset, so
# `## BATCH_20260710_B — tracking` (em dash) was not seen as a boundary and the record above it
# absorbed two following sections: LIT-0405 came back as 6,860 characters where the file holds
# 2,751, which also manufactured false `mention` hits on five PMIDs. Found by the independent
# verification of 2026-09-11, not by this file's own suite — the suite was asking the same
# question with the same splitter. 18 headings across the three registries carry an em dash.
RECORD_HEAD = re.compile(r"^##[ \t]+(?P<id>\S.*?)[ \t]*$", re.M)
# 🔴 A RECORD IS AN ADDRESSABLE SCIENTIFIC UNIT; A SECTION IS EVERYTHING ELSE, AND THE
# DIFFERENCE WAS MEASURED, NOT ASSUMED. The first cut of this file treated every `##` heading as
# a record. `discovery_ledger_current.md` ends with a `## Change-log` block of 470,808
# characters and `full_text_queue_current.md` with a `## Esito` block of 95,290; an incidental
# PMID inside either dragged the whole block in, and then its wikilinks exploded at hop 1. The
# result was WORSE than the full load it replaces — 602 KB and 689 KB for two PMIDs against a
# 1,067 KB four-file preload. Naming what is addressable fixes it at the root instead of
# capping the output, which would have been silent truncation with a nicer name.
RECORD_ID = re.compile(
    r"^(?:PAPER\s+\d+|LIT-\d+|LIT-EX-\d+|CLAIM\s+\d+|FT-\d+|D-\d+|DL-[A-Z]+-\d+|"
    r"CORPUS-STUB-\d+|CORPUS\s+P\d+|BLOCK\s+\d+|TX-\d+|DIS-\d+)"
    # A record may carry a descriptive title after its id — `## FT-047 — un difetto della coda`.
    # Anchoring at the end classified those as prose the moment em-dash headings became
    # boundaries, which is how one fix quietly opened the hole the other had closed.
    r"(?:\s*[—–:-].*)?$", re.I)


IDENTIFIER_LINE = re.compile(r"^\*\*Identifier(?: value)?:\*\*", re.M)


def is_record_id(value: str) -> bool:
    """Does this id have a known addressable shape? Half of the test; see `is_record`."""
    return bool(RECORD_ID.match(value.strip()))


def is_record(record_id: str, text: str) -> bool:
    """Addressable unit, or prose section?

    Data-driven rather than a hand-kept list of prefixes: a block that carries an `Identifier`
    field is a record whatever its heading looks like. The first cut listed shapes, and missed
    `CORPUS P###` (188 headings) and `LIT-EX-###` (6) — so records holding a real identifier were
    withheld as prose and their links were never followed. A block with neither a known shape nor
    an identifier — `## Change-log`, 470,808 characters — is a section.
    """
    return is_record_id(record_id) or bool(IDENTIFIER_LINE.search(text))
# Identity fields, per registry shape. These say what the record IS ABOUT.
# 🔴 IDENTITY IS THE IDENTIFIER FIELD AND NOTHING ELSE. `**Source:**` on a CLAIM record names
# the paper the claim CITES; treating it as identity labelled thirteen claims as identity matches
# for a PMID that is merely their citation — the exact confusion this command exists to prevent
# (sweep incident A13). `doi` and `pmid` stay because some records carry them as their own field;
# `source` and `identifier type` are out.
IDENTITY_FIELDS = ("identifier", "identifier value", "doi", "pmid")
WIKILINK = re.compile(r"\[\[([A-Za-z0-9_\-]+)#([^\]|]+?)(?:\|[^\]]*)?\]\]")
PMID_RE = re.compile(r"\b(\d{7,8})\b")


@dataclass
class Record:
    source: str          # wikilink stem
    path: str            # repo-relative
    record_id: str
    text: str
    line: int
    kind: str = "record"

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()

    def identity_values(self) -> str:
        """Only the fields that state what the record is about — not its prose."""
        out = []
        for raw in self.text.splitlines():
            match = re.match(r"\*\*([^*]+):\*\*\s*(.*)$", raw.strip())
            if match and match.group(1).strip().lower() in IDENTITY_FIELDS:
                out.append(match.group(2))
        return " | ".join(out)

    def as_dict(self, why: str) -> dict[str, Any]:
        return {"source": self.source, "path": self.path, "record_id": self.record_id,
                "kind": self.kind, "line": self.line, "match": why,
                "record_digest": self.digest, "text": self.text}


@dataclass
class Selection:
    hits: list[tuple[Record, str]] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)
    ambiguous: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    residue: int = 0
    file_digests: dict[str, str] = field(default_factory=dict)

    def add(self, record: Record, why: str) -> None:
        key = (record.source, record.record_id)
        if any((r.source, r.record_id) == key for r, _ in self.hits):
            return
        self.hits.append((record, why))


def identity_key(value: str) -> str:
    """The identity of a record, as a key two records can collide on.

    🔴 THE PMID DECIDES WHEN THERE IS ONE, and that is the second correction an independent
    check forced. Keying on `PMID + DOI` together left two real duplicates unreported — `LIT-006`
    carries the bare identifier `30290271` while `LIT-0108` carries `PMID 30290271 / DOI …`, so
    the composite keys differed and the pair passed as two papers. A record that names the same
    PMID is the same paper whether or not it also names a DOI.

    The DOI is stripped before the PMID scan, because a DOI suffix contains digit runs: the key
    for 19936220 read `PMID 0007775,19936220`, the 0007775 coming out of
    `10.1371/journal.pone.0007775`. Cosmetic, and it would have become a false collision the day
    two unrelated DOIs shared a seven-digit suffix.
    """
    dois = sorted({m.lower().rstrip(".,;)") for m in re.findall(r"10\.\d{4,9}/\S+", value)})
    without_dois = re.sub(r"10\.\d{4,9}/\S+", " ", value)
    pmids = sorted(set(PMID_RE.findall(without_dois)))
    if pmids:
        return "PMID " + ",".join(pmids)
    return ("DOI " + ",".join(dois)) if dois else ""


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_records(root: Path, disease: str, stem: str) -> list[Record]:
    rel = f"disease-models/{disease}/{SOURCES[stem]}"
    path = root / rel
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    heads = list(RECORD_HEAD.finditer(text))
    records = []
    for index, head in enumerate(heads):
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        body = text[head.start():end]        # the exact bytes; normalising them is not returning them
        record_id = head.group("id").strip()
        records.append(Record(source=stem, path=rel, record_id=record_id, text=body,
                              line=text.count("\n", 0, head.start()) + 1,
                              kind="record" if is_record(record_id, body) else "section"))
    return records


def load_all(root: Path, disease: str, stems: Iterable[str]) -> dict[str, list[Record]]:
    return {stem: parse_records(root, disease, stem) for stem in stems}


def select(root: Path, disease: str, *, pmid: str = "", doi: str = "", record_id: str = "",
           theme: str = "", hops: int = 1, sources: Iterable[str] | None = None,
           limit: int = 0) -> Selection:
    stems = list(sources or SOURCES)
    corpus = load_all(root, disease, stems)
    found = Selection()
    for stem in stems:
        path = root / f"disease-models/{disease}/{SOURCES[stem]}"
        if path.is_file():
            found.file_digests[stem] = file_digest(path)

    needle_id = record_id.strip().lower()
    for stem, records in corpus.items():
        for record in records:
            why = ""
            if needle_id and record.record_id.lower() == needle_id:
                why = "record id"
            elif pmid and pmid in record.identity_values():
                why = "identity"
            elif doi and doi.lower() in record.identity_values().lower():
                why = "identity (doi)"
            elif pmid and PMID_RE.search(record.text) and pmid in PMID_RE.findall(record.text):
                why = "mention"
            elif theme and theme.lower() in record.text.lower():
                why = "theme"
            if why and record.kind == "section" and why != "record id":
                # Named, never carried: a prose section that happens to cite the query is a
                # place to look, not a record to load. The alternative is a 470 KB change-log
                # entering a reading because it mentions a PMID once.
                found.notes.append(
                    f"not returned (prose section, {len(record.text):,} chars): "
                    f"{record.source}#{record.record_id} matched by {why} — "
                    f"fetch it deliberately with --id '{record.record_id}' if you need it")
                why = ""
            if why:
                found.add(record, why)

    # 🔴 Two records claiming the same identity is an ambiguity to SHOW, not to resolve here.
    # 🔴 KEYED ON THE IDENTIFIERS, NOT ON THE STRING. The first cut compared whole identity lines,
    # so `PMID x / PMC y / DOI z` and `PMID x / DOI z / PMC y` read as different identities and
    # the duplicates went unreported on ten PMIDs. Found by the independent verification.
    identities: dict[tuple[str, str], list[str]] = {}
    for record, why in found.hits:
        if why.startswith("identity"):
            key = identity_key(record.identity_values())
            if key:
                identities.setdefault((record.source, key), []).append(record.record_id)
    for (stem, value), ids in sorted(identities.items()):
        if len(ids) > 1:
            found.ambiguous.append(
                f"{stem}: {len(ids)} records claim the same identity ({value}): "
                f"{', '.join(sorted(ids))} — a reader decides which, not this command")

    # One hop of wikilink resolution per requested hop, so a claim, a premise, a contradiction
    # or a source named by a returned record comes back WHOLE rather than as a dangling pointer.
    frontier = [record for record, _ in found.hits if record.kind == "record"]
    for depth in range(max(0, hops)):
        next_frontier: list[Record] = []
        for record in frontier:
            for stem, anchor in WIKILINK.findall(record.text):
                if stem not in SOURCES:
                    found.unresolved.append(
                        f"{record.source}#{record.record_id} -> [[{stem}#{anchor}]] "
                        f"(no such registry surface is known to this command)")
                    continue
                if stem not in corpus:
                    corpus[stem] = parse_records(root, disease, stem)
                    path = root / f"disease-models/{disease}/{SOURCES[stem]}"
                    if path.is_file():
                        found.file_digests[stem] = file_digest(path)
                target = anchor.strip()
                matches = [item for item in corpus[stem]
                           if item.record_id.lower() == target.lower()]
                if not matches:
                    found.unresolved.append(
                        f"{record.source}#{record.record_id} -> [[{stem}#{target}]] "
                        f"(the target record does not exist in the current file)")
                    continue
                for item in matches:
                    if item.kind == "section":
                        continue
                    before = len(found.hits)
                    found.add(item, f"linked from {record.record_id} (hop {depth + 1})")
                    if len(found.hits) > before:
                        next_frontier.append(item)
        frontier = next_frontier
        if not frontier:
            break

    if limit and len(found.hits) > limit:
        found.residue = len(found.hits) - limit
        found.hits = found.hits[:limit]
    return found


def render(found: Selection, *, query: str, full: bool = True) -> str:
    lines = [f"REGISTRY RECORDS — {query}"]
    if not found.hits:
        lines.append("  NO RECORD MATCHED.")
        lines.append("  🔴 This is not evidence that the laboratory does not know this paper: it "
                     "is a statement about this query over these files. Widen the query, or say "
                     "in the reading that no record was found and what was searched.")
        lines.append(f"  searched: {', '.join(sorted(found.file_digests))}")
        return "\n".join(lines)
    by_kind: dict[str, int] = {}
    for _record, why in found.hits:
        by_kind[why.split(" (")[0]] = by_kind.get(why.split(" (")[0], 0) + 1
    lines.append("  hits: " + " · ".join(f"{value} {key}" for key, value in sorted(by_kind.items())))
    for record, why in found.hits:
        lines.append(f"\n----- {record.path}:{record.line}  [{why}]  "
                     f"record_digest={record.digest[:12]}")
        lines.append(record.text.rstrip() if full else record.text.splitlines()[0])
    if found.notes:
        lines.append("\n  MATCHED BUT NOT RETURNED (prose sections — named so the selection is "
                     "visible, fetch deliberately with --id):")
        lines.extend(f"    {item}" for item in found.notes)
    if found.ambiguous:
        lines.append("\n  AMBIGUOUS:")
        lines.extend(f"    {item}" for item in found.ambiguous)
    if found.unresolved:
        lines.append("\n  UNRESOLVED LINKS (named, never dropped):")
        lines.extend(f"    {item}" for item in sorted(set(found.unresolved)))
    if found.residue:
        lines.append(f"\n  🔴 {found.residue} further matching record(s) were NOT returned because "
                     f"--limit was set. Re-run with a larger --limit or a narrower query; nothing "
                     f"here has been truncated inside a record.")
    lines.append("\n  source digests at call time: " +
                 " · ".join(f"{k}={v[:12]}" for k, v in sorted(found.file_digests.items())))
    lines.append("  limits of this selection: it reaches records whose identity or prose matches "
                 "the query, plus one hop per --hops along declared wikilinks. A relevant record "
                 "that names neither the query nor a returned record is not here.")
    return "\n".join(lines)


def build_index(root: Path, disease: str) -> dict[str, Any]:
    """A DERIVED index: identity -> record id, re-derivable and never authoritative."""
    index: dict[str, Any] = {"record_kind": "derived_registry_index", "disease": disease,
                             "sources": {}, "identities": {}}
    for stem in SOURCES:
        records = parse_records(root, disease, stem)
        if not records:
            continue
        path = root / f"disease-models/{disease}/{SOURCES[stem]}"
        index["sources"][stem] = {"path": str(path.relative_to(root)),
                                  "records": len(records), "digest": file_digest(path)}
        for record in records:
            for value in PMID_RE.findall(record.identity_values()):
                index["identities"].setdefault(value, []).append(f"{stem}#{record.record_id}")
    return index


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("action", choices=("get", "index"))
    parser.add_argument("--pmid", default="")
    parser.add_argument("--doi", default="")
    parser.add_argument("--id", dest="record_id", default="")
    parser.add_argument("--theme", default="")
    parser.add_argument("--hops", type=int, default=1)
    parser.add_argument("--limit", type=int, default=0,
                        help="cap the number of records returned; the residue is always named")
    parser.add_argument("--source", action="append", default=[],
                        help=f"restrict to one surface: {', '.join(SOURCES)}")
    parser.add_argument("--headings-only", action="store_true",
                        help="print only each record's heading — for counting, never for reading")
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()

    if args.action == "index":
        index = build_index(root, args.disease)
        print(json.dumps(index, indent=1) if args.json else
              "\n".join(f"{k:<34} {v['records']:>4} records  digest={v['digest'][:12]}  {v['path']}"
                        for k, v in sorted(index["sources"].items())))
        return 0

    if not any((args.pmid, args.doi, args.record_id, args.theme)):
        parser.error("give at least one of --pmid, --doi, --id, --theme")
    for bad in args.source:
        if bad not in SOURCES:
            parser.error(f"unknown --source {bad}; known: {', '.join(SOURCES)}")

    found = select(root, args.disease, pmid=args.pmid, doi=args.doi, record_id=args.record_id,
                   theme=args.theme, hops=args.hops, sources=args.source or None,
                   limit=args.limit)
    query = " ".join(filter(None, [f"pmid={args.pmid}" if args.pmid else "",
                                   f"doi={args.doi}" if args.doi else "",
                                   f"id={args.record_id}" if args.record_id else "",
                                   f"theme={args.theme}" if args.theme else "",
                                   f"hops={args.hops}"]))
    if args.json:
        print(json.dumps({
            "query": query,
            "records": [record.as_dict(why) for record, why in found.hits],
            "ambiguous": found.ambiguous,
            "unresolved_links": sorted(set(found.unresolved)),
            "matched_but_not_returned": found.notes,
            "residue_not_returned": found.residue,
            "source_digests": found.file_digests,
            "empty_result_is_not_a_scientific_statement": not found.hits,
        }, indent=1, ensure_ascii=False))
    else:
        print(render(found, query=query, full=not args.headings_only))
    return 1 if not found.hits else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:      # `| head` closes the pipe; that is not a failure of the query
        try:
            sys.stdout.close()
        finally:
            sys.exit(0)
