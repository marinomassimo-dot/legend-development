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
- A record is returned **entire**, from its identity heading to the next heading of the same
  or a higher level — at the level each surface defines records (`IDENTITY_LEVELS`, measured
  in D0), with its nested blocks and its enclosing heading path. No field is dropped,
  summarised or re-ordered, so a caveat, a negative or a qualification cannot be lost in
  transit. `--json` carries the same bytes as the rendered form.
- **Identity is not mention.** A record whose `Identifier` field names the PMID is an `identity`
  hit; a record that merely cites the PMID in its prose is a `mention` hit. Both are returned,
  labelled, never merged — an incidental citation and the paper's own record are different
  objects and the 2026-09-09 sweep produced the error of confusing them (A13).
- Every hit carries **source path, record id, record digest and source-file digest**, so a later
  reader can tell whether the registry has moved underneath a quoted record.
- 🔴 **The preamble of every consulted surface travels with the answer**, once per surface. The
  bytes before a file's first `##` belong to no record, so selective retrieval dropped them while
  returning every record whole — and that is where each registry states that it is the
  de-identified public edition, that it is **not medical advice**, and (in the discovery ledger)
  what `DATO / INFERENZA / IPOTESI / ESPANSIONE` mean and that leads are re-statused, never
  deleted. A reader who filters on `Type` needs the file that defines `Type`. This is the defect
  named below one level up: a caveat alive in the file header and dead in every record.
- Every answer carries the **commit the registries were read at**, and whether any of them was
  uncommitted in the working tree at that moment (`BOUND` / `DIRTY` / `UNBOUND`, the three states
  `derived_inputs.py` already names). A digest says the bytes have moved; only the commit says
  WHICH TREE they were quoted from, and `DIRTY` says the quotation reproduces somebody's
  uncommitted edit rather than anything a second reader can check out. Reported, never refused:
  this command reads, and a reader who is told DIRTY can decide.
- Wikilinks are resolved one hop by default (`--hops`), and a link that resolves to **nothing**
  is reported as `UNRESOLVED` rather than silently dropped.
- 🔴 **An empty result is never a scientific statement.** `no record matched` exits non-zero and
  says in words that it is not evidence the laboratory does not know this paper.
- 🔴 **No match and a broken tool are different exits.** `0` records returned · `1` no record
  matched · `2` invalid invocation or TOOL ERROR (a file the command could not read, a crash).
  Until 2026-09-24 an uncaught exception also exited `1`, so an unreadable registry read as
  "nothing matched".
- 🔴 **No silent truncation.** `--limit` prints the residue and names it; the default is no
  limit at all.
- 🔴 **A field filter reports its denominator and the values it actually matched.** `--field`
  matches a DECLARED field as a case-insensitive substring, because in this corpus a field value
  is free prose: 21 of the 39 claim `Type` values are compound (`DATO + INFERENZA prudente`), and
  only four are a bare epistemic level. So `Type=INFERENZA` returns 14 of the 39 records that
  declare `Type`, of which exactly 2 declare a bare `INFERENZA` — and the answer prints both
  numbers and every distinct value behind them rather than choosing for the reader. A field no
  searched surface declares is a **named refusal with near-miss suggestions**, never an empty
  result. `fields` prints the whole derived vocabulary, per surface.

    python3 framework/scripts/registry_records.py get --pmid 33914858
    python3 framework/scripts/registry_records.py get --pmid 33914858 --hops 1 --json
    python3 framework/scripts/registry_records.py get --id "CLAIM 030" --hops 2
    python3 framework/scripts/registry_records.py get --theme myelin --limit 5
    python3 framework/scripts/registry_records.py fields --source claim_registry_current
    python3 framework/scripts/registry_records.py get --theme myelin \
        --field "Status=consolidated baseline" --source claim_registry_current
    python3 framework/scripts/registry_records.py index --verify
    python3 framework/scripts/registry_records.py get --pmid 33914858 --json | \
        python3 -c "import json,sys; print(json.load(sys.stdin)['repository'])"

The canonical registries are never written, re-ordered, summarised or mirrored. There is no
second registry to maintain: every answer is parsed from the current file at call time, and
`index --verify` re-derives the digests so a stale quotation is detectable.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

if str(HERE) not in sys.path:        # the guarded form `paper_packet.py` already uses
    sys.path.insert(0, str(HERE))
import derived_inputs  # noqa: E402

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
    r"^(?:PAPER\s+\d+|LIT-\d+|LIT-EX-\d+|CLAIM\s+\d+|FT-\d+|D-\d+|DL-[A-Z]+-\d+[a-z]?|"
    r"CORPUS-STUB-\d+|CORPUS\s+PMID\s+\d+|CORPUS\s+P\d+|BLOCK\s+\d+|TX-\d+|DIS-\d+)"
    # A record may carry a descriptive title after its id — `## FT-047 — un difetto della coda`.
    # Anchoring at the end classified those as prose the moment em-dash headings became
    # boundaries, which is how one fix quietly opened the hole the other had closed.
    r"(?:\s*[—–:-].*)?$", re.I)


IDENTIFIER_LINE = re.compile(r"^\*\*Identifier(?: value)?:\*\*", re.M)
# The id alone, for `--id DL-MECH-029` against `### 🔴 DL-MECH-029 — Q230P: …`.
ID_TOKEN = re.compile(
    r"^(PAPER\s+\d+|LIT-EX-\d+|LIT-\d+|CLAIM\s+\d+|FT-\d+|D-\d+|DL-[A-Z]+-\d+[a-z]?|"
    r"CORPUS-STUB-\d+|CORPUS\s+PMID\s+\d+|CORPUS\s+P\d+|BLOCK\s+\d+|TX-\d+|DIS-\d+)(?=$|[\s—–:-])",
    re.I)
# Leading emoji and markers are decoration: `### 🎯 DL-MECH-034 — …` defines DL-MECH-034. A leading
# WORD is not: `### Update DL-MOL-006 — …` and `### STATUS UPDATE — DL-MECH-017` are updates.
DECORATION = re.compile(r"^[^0-9A-Za-z]+")
HEADING = re.compile(r"^(?P<hashes>#{1,6})[ \t]+(?P<text>\S.*?)[ \t]*$")
FENCE = re.compile(r"^[ \t]{0,3}(?:```|~~~)")
# 🔴 WHERE A RECORD IS DEFINED IS A PROPERTY OF THE SURFACE, AND IT WAS MEASURED, NOT ASSUMED
# (governance/design_records/d0_registry_record_shapes_20260924.md). Splitting on `##` alone left
# 168 records unaddressable — 153 `DL-*` at `###`/`####`, 12 `DIS-*` at `###`, 3 `BLOCK n` at `#`
# — and let a `##` record swallow the `#` heading after it. The level is surface-aware because
# the shape alone is not enough: `# FT-158 … FT-169` is a range heading that PRECEDES the real
# `## FT-158`, which is also why "first occurrence is identity" is not a rule here.
IDENTITY_LEVELS = {
    "paper_registry_current": (2,),
    "literature_tracking_log_current": (2,),
    "claim_registry_current": (2,),
    "working_model_current": (1,),
    "dismissal_ledger_current": (3,),
    "discovery_ledger_current": (3, 4),
    "full_text_queue_current": (2,),
}


# Three declaration shapes, all measured in D0: `**Name:** value` (registries, queue),
# `- **Name:** value` (dismissal ledger), and `- **Name**: value · **Name**: value` (discovery
# ledger — the colon outside the bold, several fields on one line). Before D2 only the first
# was read, so the two ledgers' Status, Tag, Verdict and Outcome were invisible to `--field`.
# 🔴 The bulleted shapes are read ONLY where D0 found them to be the declaration: elsewhere a
# bold lead-in on a bullet is prose, and reading it as a field moved the queue's `Status` and
# `Priority` counts and added 47 "fields" to three surfaces that declare none of them.
BULLETED_FIELDS = ("dismissal_ledger_current", "discovery_ledger_current")
FIELD_PLAIN = re.compile(r"^\*\*(?P<name>[^*]+):\*\*\s*(?P<rest>.*)$")
FIELD_START = re.compile(r"^(?:[-*][ \t]+)?\*\*(?P<name>[^*]+?)(?::\*\*|\*\*:)[ \t]*(?P<rest>.*)$")
FIELD_NEXT = re.compile(r"[ \t]+·[ \t]+(?=\*\*[^*]+?(?::\*\*|\*\*:))")


def declared_fields(line: str, *, bulleted: bool = False) -> list[tuple[str, str]]:
    """The `(name, value)` pairs one line declares, verbatim; prose declares none.

    A ` · ` splits the line only where a bold field name follows it, so a value that itself
    contains a middle dot stays whole."""
    if not bulleted:
        plain = FIELD_PLAIN.match(line.strip())
        return [(plain.group("name").strip(), plain.group("rest").strip())] if plain else []
    match = FIELD_START.match(line.strip())
    if not match:
        return []
    out: list[tuple[str, str]] = []
    first, *others = FIELD_NEXT.split(match.group("rest"))
    out.append((match.group("name").strip(), first.strip()))
    for segment in others:
        inner = FIELD_START.match(segment)
        if inner:
            out.append((inner.group("name").strip(), inner.group("rest").strip()))
    return out


def is_record_id(value: str) -> bool:
    """Does this id have a known addressable shape? Half of the test; see `is_record`."""
    return bool(RECORD_ID.match(DECORATION.sub("", value.strip())))


def identity_token(value: str) -> str:
    """`🔴 DL-MECH-029 — Q230P: …` -> `DL-MECH-029`; a heading that is not an id -> ``."""
    match = ID_TOKEN.match(DECORATION.sub("", value.strip()))
    return " ".join(match.group(1).split()) if match else ""


def same_id(left: str, right: str) -> bool:
    return bool(left) and " ".join(left.split()).lower() == " ".join(right.split()).lower()


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
    level: int = 2
    end_line: int = 0
    heading_path: tuple[str, ...] = ()
    own_text: str = ""       # heading to the first nested heading: what a SECTION is matched on
    contains: tuple[str, ...] = ()

    @property
    def identity_id(self) -> str:
        return identity_token(self.record_id) if self.kind == "record" else ""

    @property
    def match_text(self) -> str:
        """A record matches on all of itself. A section matches only on its own prose: a
        `## Run …` section holding forty ledger records is not a mention of each of their PMIDs,
        and the records answer for themselves."""
        return self.text if self.kind == "record" else self.own_text

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()

    def fields(self) -> list[tuple[str, str]]:
        """Every `**Name:** value` line this record declares, in order, verbatim.

        Names are not lower-cased here and values are not stripped of their markup: the caller
        decides how to compare, and the report prints what the file says. A field whose value
        carries a wikilink or an em dash is still that field's value.
        """
        out = []
        bulleted = self.source in BULLETED_FIELDS
        for raw in self.text.splitlines():
            out.extend(declared_fields(raw, bulleted=bulleted))
        return out

    def identity_values(self) -> str:
        """Only the fields that state what the record is about — not its prose."""
        out = []
        for raw in self.match_text.splitlines():
            match = re.match(r"\*\*([^*]+):\*\*\s*(.*)$", raw.strip())
            if match and match.group(1).strip().lower() in IDENTITY_FIELDS:
                out.append(match.group(2))
        return " | ".join(out)

    def as_dict(self, why: str) -> dict[str, Any]:
        return {"source": self.source, "path": self.path, "record_id": self.record_id,
                "identity_id": self.identity_id, "kind": self.kind, "line": self.line,
                "end_line": self.end_line, "heading_level": self.level,
                "heading_path": list(self.heading_path), "contains_records": list(self.contains),
                "match": why, "record_digest": self.digest, "text": self.text}


@dataclass
class Selection:
    hits: list[tuple[Record, str]] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)
    ambiguous: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    residue: int = 0
    file_digests: dict[str, str] = field(default_factory=dict)
    preambles: dict[str, str] = field(default_factory=dict)
    repository: dict[str, Any] = field(default_factory=dict)
    field_report: list[dict[str, Any]] = field(default_factory=list)
    term_report: list[dict[str, Any]] = field(default_factory=list)
    navigation: list[dict[str, Any]] = field(default_factory=list)

    def add(self, record: Record, why: str) -> None:
        # Keyed on the POSITION, not the heading text: two `### Change-log` blocks are two
        # blocks, and a key on the text returned the first and silently dropped the second.
        key = (record.source, record.line)
        if any((r.source, r.line) == key for r, _ in self.hits):
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


def surface_preamble(path: Path) -> str:
    """The bytes before the first `##` — verbatim, never summarised, never reflowed.

    🔴 THESE BYTES BELONG TO NO RECORD, WHICH IS WHY THEY WERE LOST. `parse_records` splits on
    `##` and every byte after the first heading lands in exactly one block; the header does not,
    so a command that returns records whole still returned nothing of it. Measured across the
    seven surfaces: 25 to 1,737 characters each, carrying the public-edition and de-identification
    notice, "Not medical advice", and the discovery ledger's epistemic vocabulary.

    Returned as read. The same rule as a record: the caller decides what to do with it, and this
    function does not decide that a caveat is short enough to paraphrase.
    """
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    head = RECORD_HEAD.search(text)
    return text[:head.start()].strip() if head else text.strip()


def note_surface(found: "Selection", path: Path, stem: str) -> None:
    """One place where a surface becomes *consulted*: its digest and its preamble together.

    Two call sites set this — the initial `stems` loop and the hop loop, which may reach a file
    `--source` never named. They were one line each and stayed in step by luck; a surface whose
    digest was recorded without its preamble would be a file quoted without its own caveat.
    """
    if path.is_file():
        found.file_digests[stem] = file_digest(path)
        found.preambles[stem] = surface_preamble(path)


def repository_state(root: Path, paths: Iterable[Path]) -> dict[str, Any]:
    """The commit these exact files were read at, and whether any was uncommitted.

    🔴 A DIGEST IS NOT A PROVENANCE. The record digest and the source-file digest say that the
    bytes quoted are the bytes read; neither says which tree they came from. A reader holding a
    quoted record and a digest that no longer matches cannot tell whether the registry moved
    forward, whether they are on another branch, or whether the quotation was taken from an
    uncommitted edit that exists in no clone at all. The commit answers the first two and
    `DIRTY` answers the third.

    Reused rather than rewritten: `derived_inputs.input_state` already computes this, already
    defines the three states, and is already the guard other generators call. What is NOT reused
    is `refuse_if_dirty` — this command is read-only, so a dirty tree is a fact to REPORT, not a
    reason to refuse an answer. Refusing here would make the selective path fail exactly when a
    BATCH_COMMIT has the registries open, which is when a reader most needs to look at them.

    `verdict` is the module's own vocabulary, carried verbatim so there is one definition of
    these three states in the repository and not two (`test_record_conventions.py` exists
    because five modules once held five private copies of one definition).
    """
    state = derived_inputs.input_state(root, list(paths))
    block: dict[str, Any] = {
        "verdict": state.verdict,
        "commit": state.head,
        "inputs": state.inputs,
        "dirty_inputs": [{"status": status, "path": rel} for status, rel in state.dirty],
    }
    if state.detail:
        block["detail"] = state.detail
    return block


def parse_constraint(raw: str) -> tuple[str, str]:
    """`Status=in observation` -> ("Status", "in observation"). The `=` is the only separator."""
    if "=" not in raw:
        raise ValueError(f"--field expects NAME=VALUE, got {raw!r}")
    name, value = raw.split("=", 1)
    if not name.strip():
        raise ValueError(f"--field expects a field name before '=', got {raw!r}")
    return name.strip(), value.strip()


def matches_constraints(record: Record, constraints: list[tuple[str, str]]) -> bool:
    """All constraints, case-insensitive substring, over the record's DECLARED fields only.

    🔴 SUBSTRING, AND THE ANSWER SAYS SO. `Type=INFERENZA` matches `INFERENZA` and it also
    matches `DATO + INFERENZA prudente` — because in this corpus 21 of the 39 claim `Type`
    values are compound prose, and only four are a bare level. Exact matching would return 2
    claims and call it "the inferential claims"; substring returns 16 and would call the same
    thing by the same name. NEITHER is the answer on its own, so the selection reports the
    distinct values it actually matched and lets the reader decide. Resolving it here would be
    the `identity` / `mention` confusion again, one field along.

    Declared fields only, never the prose: a record whose Summary discusses an inference is not
    a record whose Type declares one.
    """
    if not constraints:
        return True
    declared = record.fields()
    for name, value in constraints:
        if not any(field_name.lower() == name.lower() and value.lower() in field_value.lower()
                   for field_name, field_value in declared):
            return False
    return True


def field_census(root: Path, disease: str, stems: Iterable[str]) -> dict[str, Any]:
    """Which fields each surface declares, and what values they take — derived, never listed.

    A reader filtering on a field should pick from what the files hold, not guess. The first
    draft of the filter took `--status` and `--has-fulltext` from the roadmap that proposed it;
    this census is how that roadmap's own example queries were found not to fit the corpus —
    `Status` is free prose (143 `not_processed` beside a value carrying a wikilink), and the
    epistemic level lives in `Type`, not in `Status`.
    """
    census: dict[str, Any] = {"record_kind": "derived_field_census", "disease": disease,
                              "surfaces": {}}
    for stem in stems:
        records = [item for item in parse_records(root, disease, stem) if item.kind == "record"]
        if not records:
            continue
        names: dict[str, dict[str, Any]] = {}
        for record in records:
            for name, value in record.fields():
                slot = names.setdefault(name, {"records": 0, "values": {}})
                slot["records"] += 1
                slot["values"][value] = slot["values"].get(value, 0) + 1
        census["surfaces"][stem] = {"records": len(records), "fields": names}
    return census


def heading_lines(text: str) -> list[tuple[int, int, int, str]]:
    """Every Markdown heading as (char offset, line, level, text) — fences excluded.

    🔴 A LINE INSIDE A FENCED BLOCK IS NOT A HEADING. The literature log's own record template,
    `## LIT-[NNN]` inside a code fence, was returned as a record.
    """
    out, fenced, offset = [], False, 0
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced:
            match = HEADING.match(line.rstrip("\r\n"))
            if match:
                out.append((offset, number, len(match.group("hashes")), match.group("text")))
        offset += len(line)
    return out


def unfenced(text: str) -> str:
    lines, fenced = [], False
    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced:
            lines.append(line)
    return "".join(lines)


def parse_records(root: Path, disease: str, stem: str) -> list[Record]:
    """Records and the sections between them, cut by heading semantics measured in D0.

    A block runs from its heading to the next heading of the SAME OR A HIGHER level, so nested
    `###`/`####` blocks — the dated additions and corrections appended to a record — travel with
    it. A record is a heading at this surface's identity level (`IDENTITY_LEVELS`) that begins
    with a known id or carries an `Identifier` field. A heading nested inside a record is part
    of that record, not a block of its own — unless it is itself a record (`DL-MECH-069b` inside
    `DL-MECH-069`), in which case it is addressable AND still inside its parent, and the parent
    names it in `contains`.
    """
    rel = f"disease-models/{disease}/{SOURCES[stem]}"
    path = root / rel
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    heads = heading_lines(text)
    levels = IDENTITY_LEVELS.get(stem, (2,))
    spans = []
    for index, (offset, line, level, title) in enumerate(heads):
        end = next((h[0] for h in heads[index + 1:] if h[2] <= level), len(text))
        own_end = heads[index + 1][0] if index + 1 < len(heads) else len(text)
        own = text[offset:own_end]
        identity = level in levels and (is_record_id(title) or bool(
            IDENTIFIER_LINE.search(unfenced(own))))
        spans.append((offset, end, line, level, title.strip(), own, identity))
    records, path_stack = [], []
    for offset, end, line, level, title, own, identity in spans:
        path_stack = [item for item in path_stack if item[0] < level]
        inside = [s for s in spans if s[6] and s[0] < offset < s[1]]
        if identity or not inside:
            body = text[offset:end]      # the exact bytes; normalising them is not returning them
            nested = tuple(identity_token(s[4]) or s[4] for s in spans
                           if s[6] and offset < s[0] < end)
            records.append(Record(
                source=stem, path=rel, record_id=title, text=body, line=line,
                kind="record" if identity else "section", level=level,
                end_line=text.count("\n", 0, end), heading_path=tuple(p[1] for p in path_stack),
                own_text=own, contains=nested))
        path_stack.append((level, title))
    return records


def load_all(root: Path, disease: str, stems: Iterable[str]) -> dict[str, list[Record]]:
    return {stem: parse_records(root, disease, stem) for stem in stems}


def terms_hit(text: str, terms: list[str], mode: str) -> bool:
    """Literal, case-insensitive, and nothing else: no stemming, no synonyms, no ranking."""
    lowered = text.lower()
    found = [term.lower() in lowered for term in terms]
    return any(found) if mode == "any" else all(found)


def select(root: Path, disease: str, *, pmid: str = "", doi: str = "", record_id: str = "",
           theme: str | Iterable[str] = "", match: str = "all", hops: int = 1,
           sources: Iterable[str] | None = None, open_sections: bool = False,
           limit: int = 0, constraints: list[tuple[str, str]] | None = None) -> Selection:
    constraints = list(constraints or [])
    terms = [theme] if isinstance(theme, str) else list(theme)
    terms = [term for term in terms if term.strip()]
    if match not in ("any", "all"):
        raise ValueError(f"match must be 'any' or 'all', got {match!r}")
    stems = list(sources or SOURCES)
    corpus = load_all(root, disease, stems)
    found = Selection()
    for stem in stems:
        note_surface(found, root / f"disease-models/{disease}/{SOURCES[stem]}", stem)

    searched = dict(corpus)     # before `--hops` widens `corpus`; see the field report below
    needle_id = record_id.strip().lower()
    for stem, records in corpus.items():
        for record in records:
            why = ""
            if needle_id and (record.record_id.lower() == needle_id
                              or same_id(record.identity_id, needle_id)):
                why = "record id"
            elif pmid and pmid in record.identity_values():
                why = "identity"
            elif doi and doi.lower() in record.identity_values().lower():
                why = "identity (doi)"
            elif pmid and pmid in PMID_RE.findall(record.match_text):
                why = "mention"
            elif terms and terms_hit(record.match_text, terms, match):
                why = "theme"
            elif constraints and not any((needle_id, pmid, doi, terms)):
                # With no other selector, the constraints ARE the selection. The candidate is
                # named here and the filter below decides it, for this branch exactly as for
                # every other — evaluating `matches_constraints` in both places was one call per
                # record spent to reach the same answer twice.
                why = "field"
            if why and constraints and why != "record id" and not matches_constraints(
                    record, constraints):
                # With another selector, they filter it. `--id` is exempt: a record asked for
                # by name is returned, and a filter that silently withheld it would make
                # `--id X --field Y=z` indistinguishable from "X does not exist".
                why = ""
            if why and record.kind == "section" and why != "record id":
                # Named, never carried: a prose section that happens to cite the query is a
                # place to look, not a record to load. The alternative is a 470 KB change-log
                # entering a reading because it mentions a PMID once.
                found.notes.append(
                    f"not returned (prose section, {len(record.text):,} chars): "
                    f"{record.source}#{record.record_id} matched by {why} — "
                    f"open it deliberately with --id '{record.record_id}' --open-section")
                why = ""
            if why and record.kind == "section" and not open_sections:
                # 🔴 NAMING A SECTION IS NAVIGATION, NOT A REQUEST TO LOAD IT. A section's text
                # is everything under its heading — for the ledger's title that is the whole
                # 598 KB file. By default the answer says where the section is, how big it is
                # and which records it holds; `--open-section` loads it, and says so.
                found.navigation.append({
                    "relation": "section named by --id",
                    "source": record.source, "path": record.path, "heading": record.record_id,
                    "line": record.line, "end_line": record.end_line, "level": record.level,
                    "heading_path": list(record.heading_path), "chars": len(record.text),
                    "contains_records": list(record.contains)})
                why = ""
            if why:
                found.add(record, why)

    # 🔴 A DEFINITION IS RETURNED; THE LATER HEADINGS THAT NAME IT ARE LISTED, NOT MERGED. D0
    # found `### Update DL-MOL-006`, `### STATUS UPDATE — DL-MECH-017`, `## CORREZIONE
    # APPEND-ONLY FT-062 …`: each updates a record and none is its identity. Returning them as
    # the record would be first-occurrence identity again; dropping them would hide the update.
    token = identity_token(record_id) if needle_id else ""
    if token:
        names_it = re.compile(r"(?<![\w-])" + re.escape(token) + r"(?![\w-])", re.I)
        for stem, records in searched.items():
            for record in records:
                if same_id(record.identity_id, token) or not names_it.search(record.record_id):
                    continue
                found.navigation.append({
                    "relation": f"heading names {token}; not its definition",
                    "source": record.source, "path": record.path, "heading": record.record_id,
                    "line": record.line, "end_line": record.end_line, "level": record.level,
                    "heading_path": list(record.heading_path), "chars": len(record.text),
                    "contains_records": list(record.contains)})

    # 🔴 THE DENOMINATOR IS OVER THE SEARCHED SURFACES, so it is computed HERE — before the
    # hop loop, which widens `corpus` with whatever a link reaches. A denominator that grew
    # because a wikilink pulled in another registry would be a different question's answer.
    # 🔴 AND THE DENOMINATOR TRAVELS WITH THE FILTER, and the distinct values it matched travel
    # with it too. "3 records match Type=INFERENZA" is unreadable without knowing how many
    # records declare `Type` at all, and dangerous without seeing that one of the three
    # declares `DATO + INFERENZA prudente`. A field that no searched surface declares is a
    # named refusal, not an empty result — the same rule as the empty selection.
    for name, value in constraints:
        declaring, matched, values = 0, 0, {}
        for stem, records in searched.items():
            for record in records:
                if record.kind != "record":
                    continue
                for field_name, field_value in record.fields():
                    if field_name.lower() != name.lower():
                        continue
                    declaring += 1
                    if value.lower() in field_value.lower():
                        matched += 1
                        values[field_value] = values.get(field_value, 0) + 1
                    break
        entry: dict[str, Any] = {
            "field": name, "value": value, "records_declaring_the_field": declaring,
            "records_matching": matched,
            "distinct_values_matched": dict(sorted(values.items(), key=lambda kv: -kv[1])),
        }
        if declaring == 0:
            # 🔴 A REFUSAL THAT SUGGESTS NOTHING IS A REFUSAL THE READER RETYPES. The first cut
            # matched substrings only, so `Stato` (an Italian slip in a bilingual corpus, and
            # this corpus IS bilingual) suggested nothing at all while `Status` sat one letter
            # away. difflib is standard library; a spell-check here costs nothing and the
            # alternative is the reader guessing twice.
            declared_names = {field_name for _stem, records in searched.items()
                              for record in records if record.kind == "record"
                              for field_name, _value in record.fields()}
            near = sorted(set(difflib.get_close_matches(name, sorted(declared_names), n=5,
                                                        cutoff=0.6))
                          | {field_name for field_name in declared_names
                             if name.lower() in field_name.lower()
                             or field_name.lower() in name.lower()})
            entry["no_surface_declares_this_field"] = True
            entry["similar_field_names"] = near
        found.field_report.append(entry)

    # 🔴 EACH TERM'S OWN COUNT TRAVELS WITH THE ANSWER, over the same searched records. An empty
    # `all` of two terms reads the same whether one term is absent from the corpus or both are
    # common and never meet — and those are different findings.
    for term in terms:
        found.term_report.append({
            "term": term, "match": match,
            "records_containing": sum(1 for records in searched.values() for record in records
                                      if record.kind == "record"
                                      and term.lower() in record.text.lower()),
            "records_searched": sum(1 for records in searched.values() for record in records
                                    if record.kind == "record")})

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
    defined: dict[tuple[str, str], list[int]] = {}
    for record, _why in found.hits:
        if record.kind == "record" and record.identity_id:
            defined.setdefault((record.source, record.identity_id.upper()), []).append(record.line)
    for (stem, value), lines in sorted(defined.items()):
        if len(lines) > 1:
            found.ambiguous.append(
                f"{stem}: {len(lines)} records are DEFINED as {value} (lines "
                f"{', '.join(map(str, lines))}) — none was chosen; a reader decides")
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
                    note_surface(
                        found, root / f"disease-models/{disease}/{SOURCES[stem]}", stem)
                target = anchor.strip()
                matches = [item for item in corpus[stem]
                           if item.record_id.lower() == target.lower()
                           or same_id(item.identity_id, target)]
                if not matches:
                    why_not = ("an Obsidian block reference, not a heading — this command "
                               "resolves headings only" if target.startswith("^") else
                               "the target record does not exist in the current file")
                    found.unresolved.append(
                        f"{record.source}#{record.record_id} -> [[{stem}#{target}]] ({why_not})")
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

    # Over the files actually consulted, which `--hops` may have widened past `stems`, and
    # after the hop loop for that reason. Never over SOURCES: naming a file this call did not
    # open would bind the answer to a tree state it never read.
    found.repository = repository_state(
        root, [root / f"disease-models/{disease}/{SOURCES[stem]}" for stem in found.file_digests])

    if limit and len(found.hits) > limit:
        found.residue = len(found.hits) - limit
        found.hits = found.hits[:limit]
    return found


def field_report_lines(report: list[dict[str, Any]]) -> list[str]:
    """The denominator and the values matched — never the count alone."""
    lines: list[str] = []
    for entry in report:
        lines.append(f"\n  FIELD FILTER  {entry['field']}={entry['value']}")
        if entry.get("no_surface_declares_this_field"):
            lines.append(f"    🔴 NO SEARCHED SURFACE DECLARES A FIELD NAMED {entry['field']!r}. "
                         f"An empty result here is a statement about the field name, not about "
                         f"the corpus.")
            similar = entry.get("similar_field_names") or []
            lines.append(f"    similar field names present: "
                         f"{', '.join(similar) if similar else '(none)'} — "
                         f"`fields` prints every field each surface declares")
            continue
        lines.append(f"    {entry['records_matching']} of "
                     f"{entry['records_declaring_the_field']} record(s) declaring {entry['field']}")
        values = entry["distinct_values_matched"]
        if values:
            lines.append("    🔴 matched as a SUBSTRING — the distinct values behind that count:")
            for value, count in list(values.items())[:12]:
                lines.append(f"      {count:>4}x  {value[:110]}")
            if len(values) > 12:
                lines.append(f"      … and {len(values) - 12} further distinct value(s); "
                             f"`--json` carries them all")
    return lines


def term_report_lines(report: list[dict[str, Any]]) -> list[str]:
    if not report:
        return []
    mode = report[0]["match"]
    return [f"\n  TERMS ({mode}, literal, case-insensitive): " + " · ".join(
        f"{entry['term']!r} in {entry['records_containing']} of {entry['records_searched']} record(s)"
        for entry in report)]


def repository_line(block: dict[str, Any]) -> str:
    """One line, and it says DIRTY out loud when it is."""
    if not block:
        return "  read at: (repository state not computed)"
    verdict, commit = block.get("verdict", "?"), (block.get("commit") or "")[:12]
    if verdict == derived_inputs.DIRTY:
        names = ", ".join(item["path"] for item in block.get("dirty_inputs", [])[:3])
        more = "" if len(block.get("dirty_inputs", [])) <= 3 else \
            f" (+{len(block['dirty_inputs']) - 3} more)"
        return (f"  🔴 read at commit {commit}, WORKING TREE DIRTY: {names}{more} — a record "
                f"quoted from here reproduces an uncommitted edit and is not in any clone")
    if verdict == derived_inputs.UNBOUND:
        return (f"  read at: UNBOUND — {block.get('detail', 'not bound to a commit')}; "
                f"this answer cannot be tied to a tree")
    return f"  read at commit {commit}, working tree clean for the files consulted"


def preamble_lines(preambles: dict[str, str]) -> list[str]:
    """Once per consulted surface, BEFORE the records — a reading frame read after the thing it
    frames is a reading frame that arrived too late."""
    lines: list[str] = []
    for stem, text in sorted(preambles.items()):
        if not text:
            continue
        lines.append(f"\n  SURFACE PREAMBLE — {stem} (verbatim; belongs to no record):")
        lines.extend(f"    {row}" if row else "" for row in text.splitlines())
    return lines


def render(found: Selection, *, query: str, full: bool = True) -> str:
    lines = [f"REGISTRY RECORDS — {query}"]
    lines.extend(preamble_lines(found.preambles))
    if not found.hits and not found.navigation:
        lines.append("  NO RECORD MATCHED.")
        lines.append("  🔴 This is not evidence that the laboratory does not know this paper: it "
                     "is a statement about this query over these files. Widen the query, or say "
                     "in the reading that no record was found and what was searched.")
        lines.append(f"  searched: {', '.join(sorted(found.file_digests))}")
        lines.extend(term_report_lines(found.term_report))
        lines.extend(field_report_lines(found.field_report))
        lines.append(repository_line(found.repository))
        return "\n".join(lines)
    by_kind: dict[str, int] = {}
    for _record, why in found.hits:
        by_kind[why.split(" (")[0]] = by_kind.get(why.split(" (")[0], 0) + 1
    lines.append("  hits: " + " · ".join(f"{value} {key}" for key, value in sorted(by_kind.items())))
    for record, why in found.hits:
        lines.append(f"\n----- {record.path}:{record.line}-{record.end_line}  [{why}]  "
                     f"record_digest={record.digest[:12]}  h{record.level}"
                     + (f"  in: {' > '.join(record.heading_path)}" if record.heading_path else "")
                     + (f"  contains: {', '.join(record.contains)}" if record.contains else ""))
        lines.append(record.text.rstrip() if full else record.text.splitlines()[0])
    if found.navigation:
        lines.append("\n  HEADINGS NAMED BY THE QUERY (navigation — not loaded; --id <heading> "
                     "--open-section loads a section whole):")
        for item in found.navigation:
            held = item["contains_records"]
            lines.append(f"    [{item['relation']}]  "
                         f"{item['path']}:{item['line']}-{item['end_line']}  h{item['level']}  "
                         f"{item['heading'][:80]}  ({item['chars']:,} chars; "
                         f"{len(held)} record(s)"
                         + (f": {', '.join(held[:12])}" + (" …" if len(held) > 12 else "")
                            if held else "") + ")")
    if found.notes:
        lines.append("\n  MATCHED BUT NOT RETURNED (prose sections — named so the selection is "
                     "visible, fetch deliberately with --id):")
        lines.extend(f"    {item}" for item in found.notes)
    lines.extend(term_report_lines(found.term_report))
    lines.extend(field_report_lines(found.field_report))
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
    lines.append(repository_line(found.repository))
    lines.append("  limits of this selection: it reaches records whose identity or prose matches "
                 "the query, plus one hop per --hops along declared wikilinks. A relevant record "
                 "that names neither the query nor a returned record is not here.")
    return "\n".join(lines)


def catalog(root: Path, disease: str, stems: Iterable[str],
            columns: Iterable[str] = ()) -> dict[str, Any]:
    """One row per record, projected from the current files at call time — never stored.

    A column is a DECLARED field (`fields` lists them); its denominator travels with it, and a
    column no catalogued surface declares is a named refusal, the rule `--field` already keeps.
    """
    columns = list(columns)
    out: dict[str, Any] = {"record_kind": "derived_catalog", "disease": disease, "rows": [],
                           "columns": {}, "file_digests": {}}
    records = []
    for stem in stems:
        path = root / f"disease-models/{disease}/{SOURCES[stem]}"
        if path.is_file():
            out["file_digests"][stem] = file_digest(path)
        records.extend(item for item in parse_records(root, disease, stem) if item.kind == "record")
    for name in columns:
        declaring = sum(1 for item in records
                        if any(n.lower() == name.lower() for n, _v in item.fields()))
        entry: dict[str, Any] = {"records_declaring_the_field": declaring,
                                 "records_catalogued": len(records)}
        if not declaring:
            names = {n for item in records for n, _v in item.fields()}
            entry["no_surface_declares_this_field"] = True
            entry["similar_field_names"] = sorted(set(difflib.get_close_matches(
                name, sorted(names), n=5, cutoff=0.6)))
        out["columns"][name] = entry
    for item in records:
        identity = item.identity_id or item.record_id
        title = DECORATION.sub("", item.record_id)[len(identity):].strip(" \t—–:-") \
            if item.identity_id else ""
        row: dict[str, Any] = {"source": item.source, "id": identity, "title": title,
                               "line": item.line, "level": item.level}
        declared = item.fields()
        for name in columns:
            row[name] = [v for n, v in declared if n.lower() == name.lower()]
        out["rows"].append(row)
    out["repository"] = repository_state(
        root, [root / f"disease-models/{disease}/{SOURCES[stem]}" for stem in out["file_digests"]])
    return out


def build_index(root: Path, disease: str) -> dict[str, Any]:
    """A DERIVED index: identity -> record id, re-derivable and never authoritative."""
    index: dict[str, Any] = {"record_kind": "derived_registry_index", "disease": disease,
                             "sources": {}, "identities": {}, "repository": {}}
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
    index["repository"] = repository_state(
        root, [root / f"disease-models/{disease}/{SOURCES[stem]}" for stem in index["sources"]])
    return index


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("action", choices=("get", "index", "fields", "catalog"))
    parser.add_argument("--column", action="append", default=[], metavar="FIELD",
                        help="catalog: add a DECLARED field as a column; repeatable")
    parser.add_argument("--open-section", action="store_true",
                        help="load a section named by --id whole; by default it is navigation")
    parser.add_argument("--pmid", default="")
    parser.add_argument("--doi", default="")
    parser.add_argument("--id", dest="record_id", default="")
    parser.add_argument("--theme", action="append", default=[],
                        help="literal, case-insensitive term; repeatable (see --match)")
    parser.add_argument("--match", choices=("all", "any"), default="all",
                        help="with several --theme terms: every term (all) or at least one (any)")
    parser.add_argument("--field", action="append", default=[], metavar="NAME=VALUE",
                        help="keep only records whose DECLARED field NAME contains VALUE "
                             "(case-insensitive substring); repeatable, and all must hold. "
                             "Run the `fields` action first to see what each surface declares.")
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

    if args.action == "fields":
        census = field_census(root, args.disease, args.source or SOURCES)
        if args.json:
            print(json.dumps(census, indent=1, ensure_ascii=False))
            return 0
        for stem, surface in sorted(census["surfaces"].items()):
            print(f"\n{stem}  ({surface['records']} records)")
            for name, slot in sorted(surface["fields"].items()):
                top = sorted(slot["values"].items(), key=lambda kv: -kv[1])
                shown = " · ".join(f"{value[:46]} ({count})" for value, count in top[:4])
                more = f" · +{len(top) - 4} more" if len(top) > 4 else ""
                print(f"  {name:<32} {slot['records']:>4} record(s), "
                      f"{len(top):>3} distinct   {shown}{more}")
        print("\n  🔴 These vocabularies are DERIVED from the files, not declared anywhere. "
              "A value is free prose in this corpus: filter with --field and read the distinct "
              "values the answer reports back.")
        return 0

    if args.action == "catalog":
        for bad in args.source:
            if bad not in SOURCES:
                parser.error(f"unknown --source {bad}; known: {', '.join(SOURCES)}")
        table = catalog(root, args.disease, args.source or SOURCES, args.column)
        if args.json:
            print(json.dumps(table, indent=1, ensure_ascii=False))
        else:
            for name, entry in table["columns"].items():
                if entry.get("no_surface_declares_this_field"):
                    print(f"🔴 no catalogued surface declares {name!r}; similar: "
                          f"{', '.join(entry['similar_field_names']) or '(none)'}")
                else:
                    print(f"column {name}: declared by {entry['records_declaring_the_field']} of "
                          f"{entry['records_catalogued']} record(s)")
            for row in table["rows"]:
                cells = [f"{row['source'][:14]:<14}", f"{row['id']:<16}", f"L{row['line']:<6}"]
                for name in args.column:
                    values = row[name]
                    cells.append(f"{name}={(values[0][:40] if values else '—')}"
                                 + (f" (+{len(values) - 1})" if len(values) > 1 else ""))
                cells.append(row["title"][:70])
                print("  ".join(cells))
            print(f"\n{len(table['rows'])} record(s), projected from the current files at call "
                  f"time; nothing was stored.")
            print(repository_line(table["repository"]))
        return 0 if table["rows"] else 1

    if args.action == "index":
        index = build_index(root, args.disease)
        print(json.dumps(index, indent=1) if args.json else
              "\n".join(f"{k:<34} {v['records']:>4} records  digest={v['digest'][:12]}  {v['path']}"
                        for k, v in sorted(index["sources"].items())) +
              "\n" + repository_line(index["repository"]))
        return 0

    if not any((args.pmid, args.doi, args.record_id, args.theme, args.field)):
        parser.error("give at least one of --pmid, --doi, --id, --theme, --field")
    try:
        constraints = [parse_constraint(item) for item in args.field]
    except ValueError as error:
        parser.error(str(error))
    for bad in args.source:
        if bad not in SOURCES:
            parser.error(f"unknown --source {bad}; known: {', '.join(SOURCES)}")

    found = select(root, args.disease, pmid=args.pmid, doi=args.doi, record_id=args.record_id,
                   theme=args.theme, match=args.match, hops=args.hops,
                   sources=args.source or None, open_sections=args.open_section,
                   limit=args.limit, constraints=constraints)
    query = " ".join(filter(None, [f"pmid={args.pmid}" if args.pmid else "",
                                   f"doi={args.doi}" if args.doi else "",
                                   f"id={args.record_id}" if args.record_id else "",
                                   (f"theme={'+'.join(args.theme)} ({args.match})"
                                    if args.theme else ""),
                                   " ".join(f"field:{item}" for item in args.field),
                                   f"hops={args.hops}"]))
    if args.json:
        print(json.dumps({
            "query": query,
            "records": [record.as_dict(why) for record, why in found.hits],
            "ambiguous": found.ambiguous,
            "unresolved_links": sorted(set(found.unresolved)),
            "matched_but_not_returned": found.notes,
            "sections_named_not_loaded": found.navigation,
            "residue_not_returned": found.residue,
            "source_digests": found.file_digests,
            "surface_preambles": found.preambles,
            "field_filters": found.field_report,
            "term_report": found.term_report,
            "repository": found.repository,
            "empty_result_is_not_a_scientific_statement": not found.hits and not found.navigation,
        }, indent=1, ensure_ascii=False))
    else:
        print(render(found, query=query, full=not args.headings_only))
    return 1 if not found.hits and not found.navigation else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:      # `| head` closes the pipe; that is not a failure of the query
        try:
            sys.stdout.close()
        finally:
            sys.exit(0)
    except Exception as error:   # noqa: BLE001 — a failure must never read as `no record matched`
        print(f"TOOL ERROR — {type(error).__name__}: {error}. This is not an empty result; "
              f"nothing was searched to completion.", file=sys.stderr)
        sys.exit(2)
