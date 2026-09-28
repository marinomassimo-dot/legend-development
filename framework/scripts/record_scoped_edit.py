#!/usr/bin/env python3
"""Edit ONE record (or range) of a Markdown registry — every other byte provably unchanged — or refuse.

🔴 WHY THIS EXISTS
------------------
`BATCH_COMMIT` propagated into the four scientific current files by *"full rewrite, unchanged
sections copied verbatim"* (`legend-commit` step 4). A full rewrite asks the writer to copy
hundreds of kilobytes it was not asked to change, and nothing checks that it did. Benchmark J
(`framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/`) asked whether an editor that touches
only the addressed record can replace the rewrite without losing an edit a batch legitimately
makes; this is that editor. It turns "copied verbatim" from a matter of care into a
post-condition that is checked before a byte is written.

🔴 NOT TO BE CONFUSED WITH `scoped_record_edit.py`
-------------------------------------------------
That tool edits one FIELD of one JSONL ledger line under an operator authorisation and refuses
interior lines of a hash chain. This one edits Markdown BLOCKS of the registries and grants no
authority: the BATCH_COMMIT discipline (LINT, snapshot, one batch at a time) still decides
whether an edit may happen at all. Different object, different contract; one tool each.

WHAT A RECORD IS
----------------
Exactly what `registry_records.py` says, and nothing parsed here: the file is cut with
`registry_records.partition` at the surface's identity level (`IDENTITY_LEVELS`, measured in
D0), headings inside fences are not headings, and a block runs to the next heading of the same
or a higher level. Anchors:

  --id "CLAIM 006"        a record, by its identity token (`### 🔴 DL-MECH-029 — …` is DL-MECH-029)
  --heading "Changelog"   a section or nested sub-block, by its exact heading text
    --under "Paper Registry Current"   only with --heading: keep the hit whose enclosing
                          headings include this exact text (two `## Purpose` sections under
                          different `#` parents; Benchmark J · J5)
  --preamble              the bytes before the first heading

🔴 AN END NOBODY WROTE DOWN IS NOT A BOUNDARY
---------------------------------------------
A block runs to the next heading at or above its level — and the LAST block at its level has no
such heading, so its end was silently taken to be EOF. In `working_model_current.md` that made
`id: BLOCK 3` span 49194 → 96155 and cover `## Changelog` and every batch section after it: the
containment this tool exists to make executable was not in force, and the next `id:`-anchored edit
on that record could land in the changelog. Such a span is now reported as an ASSUMED end, and an
op that depends on where the block ends (`replace`, `replace-within`, `delete`, `insert-after`) is
REFUSED with `UNBOUNDED_SPAN` when the assumed tail covers headings. Two ways past it, both
explicit: address the sub-block by its own `--heading`, or pass `--to-eof` (`"to_eof": true` in an
ops file) to assert that the record does reach the end of the file — an append to a genuinely-last
record stays possible either way. A last block that covers no heading is not refused at all.

🔴 AND A BYTE-CONSERVING MOVE INSIDE THE RECORD IS NOT AN EDIT OF THE RECORD
----------------------------------------------------------------------------
Everything proven below is about the record's OUTSIDE. `BATCH_20260928_005` op `B2` moved 488
bytes of grounds from one STATEMENT LINE of a record onto another — severing a `DO_NOT_INFER`
prohibition from its grounds and re-parenting them under a `DO_NOT_CITE` prohibition about a
different allele — and every proof here held, because the record's boundary, its record set and
(at the repair) even its total were untouched. An edit that moves a run of ≥ 200 bytes out of one
line of the addressed record and into a line that does not continue it is now REFUSED with
`CROSS_LINE_MOVE`; an op that means to split or join a statement declares it with `--reflow`
(`"reflow": true`), as `--to-eof` declares the other. A line merely changing length, a line
relocated intact, and an indented or blockquoted line are not refused. Measured over Benchmark J's
72 historical events: zero legitimate edits refused. See `cross_line_moves`.

OPERATIONS
----------
  replace         the whole block → new text (its own heading first)
  replace-within  one exact, UNIQUE old string inside the block → new string
  insert-before   new complete block(s) before the anchor
  insert-after    new complete block(s) after the anchor (a leading `---`/blank run attaches
                  to the anchor, as the separator a new neighbour needs)
  append          new complete block(s) at the end of the file
  delete          the whole block

WHAT IS CHECKED BEFORE ANYTHING IS WRITTEN
------------------------------------------
- the bytes before and after the edited range are the input's bytes;
- every block other than the target keeps its exact bytes (the block that gains a neighbour may
  differ only by a trailing separator);
- the result re-parses to exactly the expected keys: nothing appears, disappears or re-segments.

REFUSALS (exit 3; nothing written)
----------------------------------
  ANCHOR_MISSING · ANCHOR_AMBIGUOUS (a duplicate id or heading) · FENCED_ANCHOR (the heading exists
  only inside a code fence) · NESTED_RECORD (the block contains another record, so editing it
  rewrites that record too) · IDENTITY_CHANGED (the new text renames the block without
  `--rename-to`) · RESEGMENTATION (new text carries a heading at or above the block's level —
  the "`##` record swallows the following `#`" defect of D0 — or would glue onto the next
  heading) · UNBOUNDED_SPAN (the block's end is EOF by assumption and covers headings; see above)
  · CROSS_LINE_MOVE (content reparented across a statement boundary inside the addressed
  record without `--reflow`; see above) · OLD_NOT_UNIQUE / OLD_ABSENT (`replace-within`) · DUPLICATE_ID (an insert whose
  record already exists) · POSTCONDITION (a check above failed: a defect of this tool, reported).

    python3 framework/scripts/record_scoped_edit.py blocks --file <md>
    python3 framework/scripts/record_scoped_edit.py replace --file <md> --id "CLAIM 006" --text-file new.md
    python3 framework/scripts/record_scoped_edit.py replace-within --file <md> --heading Changelog \\
        --old-file old.txt --new-file new.txt
    python3 framework/scripts/record_scoped_edit.py apply --file <md> --ops ops.json   # atomic batch

Without `--apply` every command is a dry run: it prints the unified diff and the scope proof.
Exit codes: 0 done (or dry run clean) · 2 invalid invocation / unreadable file · 3 refused.
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
from typing import Any

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import registry_records as rr  # noqa: E402

OPS = ("replace", "replace-within", "insert-before", "insert-after", "append", "delete")
SEPARATOR_RUN = re.compile(r"\A(?:[ \t]*(?:---)?[ \t]*\n)+")

#: 🔴 THE DEFECT THIS NUMBER IS CALIBRATED ON, AND THE FLOOR IS MEASURED, NOT CHOSEN.
#: `BATCH_20260928_005` op `B2` re-parented 488 bytes of grounds from a `DO_NOT_INFER` statement
#: onto a `DO_NOT_CITE` statement about a different allele, leaving the prohibition a bare edict.
#: Every proof this repository runs held: the record boundary untouched, `propagate`'s
#: all-or-nothing proof satisfied, `grep -c "Concatenarle in"` returning 1 before and 1 after.
#:
#: The floor is bytes and not sentences because a sentence is a judgement and a byte count is not.
#: Replayed over `BENCH-J-RECORD-SCOPED-EDIT/j0_corpus.json` — 72 historical (commit, file)
#: events, 337 changed records — the refusal count by floor is: 40 B → 23 records (6.8 %), 80 B →
#: 2, 120 B → 0, 200 B → 0, 400 B → 0. So the honest floor is anywhere at or above 120, and 200 is
#: taken for the margin it leaves a corpus this one does not contain, not to buy a number back.
#: `B2`'s own run is 487 bytes, so the margin is not bought at the defect's expense either. Over
#: 99 more recent (commit, file) events it fires three times, and all three are real cross-line
#: moves: `B2` itself at `da250b5`, its Mirror repair at `327a558`, and `a225a9a3` moving a 424-byte
#: supersession note off a `Status:` line — the last two being exactly the intentional reflows that
#: `--reflow` exists to declare. See `cross_line_moves`.
MOVED_BYTES_FLOOR = 200


class Refusal(Exception):
    """A scope violation or an ambiguous anchor. Nothing has been written when this is raised."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code


@dataclass
class Op:
    op: str
    id: str = ""
    heading: str = ""
    preamble: bool = False
    text: str = ""
    old: str = ""
    new: str = ""
    rename_to: str = ""
    under: str = ""
    reflow: bool = False
    """The caller declares that this op MEANS to split or join a statement inside the record.

    🔴 THE ESCAPE MUST EXIST AND MUST BE EXPLICIT, exactly as `--to-eof` is for the EOF-spanning
    span. Splitting a paragraph that has grown two arguments, or joining two that were one, is a
    legitimate edit; doing it BY ACCIDENT, inside an op whose footer swears the record's meaning is
    unchanged, is `B2`. So the act is not forbidden — it is made undeniable, and a reviewer reading
    the op list can see which ops claimed it. Setting it on every op to make a batch pass is the
    one way to lose the guarantee, and it is visible in the op list when someone does."""

    to_eof: bool = False
    """The caller asserts the addressed block really does run to end of file.

    🔴 IT IS NOT NEEDED MERELY BECAUSE A SPAN REACHES EOF. `UNBOUNDED_SPAN` is keyed on the
    assumed tail COVERING HEADINGS, not on the span ending at EOF, and this field is the way past
    that one condition. The distinction is the whole design: the LAST record of every registry
    reaches EOF (`CLAIM 041`, `PAPER 118`, `LIT-0420`, `DL-MECH-113`, `DIS-020` on this checkout),
    so a refusal keyed on EOF would refuse the commonest edit in the repository — appending to or
    amending the newest record — and the flag would have to be passed on nearly every op, which is
    how an assertion stops being read. See `_check_bounded`: `not span.swallowed` returns
    early. Do not "simplify" the condition to `span.to_eof`."""

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Op":
        known = {k: raw[k] for k in ("op", "id", "heading", "preamble", "text", "old", "new",
                                     "rename_to", "under", "to_eof", "reflow") if k in raw}
        if known.get("op") not in OPS:
            raise ValueError(f"unknown op {raw.get('op')!r}; expected one of {', '.join(OPS)}")
        return cls(**known)

    def anchor(self) -> str:
        return (f"id={self.id}" if self.id
                else f"heading={self.heading}" + (f" under={self.under}" if self.under else "")
                if self.heading
                else "preamble" if self.preamble else "end-of-file")


@dataclass
class Span:
    start: int
    end: int
    level: int
    key: str
    kind: str
    to_eof: bool = False
    """No heading at or above `level` follows: the block's end was ASSUMED to be EOF, not read
    off a boundary in the file. See `swallowed`."""
    swallowed: tuple[tuple[int, str], ...] = ()
    """(level, heading text) of every heading strictly inside an unbounded span — the content the
    span covers because the file gave it no end, which may or may not belong to the record."""


@dataclass
class Report:
    ops: list[dict[str, Any]] = field(default_factory=list)
    changed_keys: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- surface

def levels_for(path: str, surface: str = "") -> tuple[int, ...]:
    stem = surface or Path(path).stem
    return rr.IDENTITY_LEVELS.get(stem, (2,))


def _headings(text: str) -> list[tuple[int, int, int, str]]:
    return rr.heading_lines(text)


def _fenced_heading_texts(text: str) -> list[str]:
    out, fenced = [], False
    for line in text.splitlines():
        if rr.FENCE.match(line):
            fenced = not fenced
        elif fenced:
            match = rr.HEADING.match(line)
            if match:
                out.append(match.group("text").strip())
    return out


def _is_identity(title: str, level: int, own: str, levels: tuple[int, ...]) -> bool:
    return level in levels and (rr.is_record_id(title) or bool(
        rr.IDENTIFIER_LINE.search(rr.unfenced(own))))


def identity_headings(text: str, levels: tuple[int, ...]) -> list[tuple[int, int, str]]:
    """(offset, level, identity key) of every record definition, at every identity level."""
    heads = _headings(text)
    out = []
    for index, (offset, _line, level, title) in enumerate(heads):
        own_end = heads[index + 1][0] if index + 1 < len(heads) else len(text)
        if _is_identity(title, level, text[offset:own_end], levels):
            out.append((offset, level, rr.identity_token(title) or title.strip()))
    return out


def _span_from(text: str, offset: int, level: int, key: str, kind: str) -> Span:
    """The block's bytes. When no heading at or above `level` follows, the end is not READ off the
    file — it is assumed to be EOF, and every heading inside that assumed tail is recorded so the
    caller is told what the span covers instead of finding out afterwards (D0/EOF defect)."""
    heads = _headings(text)
    end = next((h[0] for h in heads if h[0] > offset and h[2] <= level), None)
    if end is not None:
        return Span(offset, end, level, key, kind)
    swallowed = tuple((h[2], h[3].strip()) for h in heads if offset < h[0] < len(text))
    return Span(offset, len(text), level, key, kind, to_eof=True, swallowed=swallowed)


def enclosing_headings(heads: list[tuple[int, int, int, str]], offset: int) -> list[str]:
    """The exact texts of the headings that enclose the heading at `offset`: for each strictly
    lower level, the nearest one before it — the path a reader sees above that heading."""
    index = next(i for i, h in enumerate(heads) if h[0] == offset)
    level, out = heads[index][2], []
    for _o, _l, lv, title in reversed(heads[:index]):
        if lv < level:
            out.append(title.strip())
            level = lv
    return out


def resolve(text: str, op: Op, levels: tuple[int, ...]) -> Span:
    """The one span an anchor names, or a refusal that says why there is not exactly one."""
    heads = _headings(text)
    if op.preamble:
        end = heads[0][0] if heads else len(text)
        return Span(0, end, 0, "@preamble", "preamble")
    if op.id:
        wanted = " ".join(op.id.split())
        hits = [(o, lv, k) for o, lv, k in identity_headings(text, levels) if rr.same_id(k, wanted)]
        if not hits:
            fenced = [t for t in _fenced_heading_texts(text) if rr.same_id(rr.identity_token(t), wanted)]
            if fenced:
                raise Refusal("FENCED_ANCHOR", f"{wanted!r} exists only as a heading inside a code "
                              "fence, which Markdown does not render as a heading")
            raise Refusal("ANCHOR_MISSING", f"no record {wanted!r} at identity level(s) {levels}")
        if len(hits) > 1:
            raise Refusal("ANCHOR_AMBIGUOUS", f"record {wanted!r} is defined {len(hits)} times")
        offset, level, key = hits[0]
        return _span_from(text, offset, level, key, "record")
    if op.heading:
        wanted = op.heading.strip()
        hits = [(o, lv, t) for o, _l, lv, t in heads if t.strip() == wanted]
        if not hits:
            if wanted in _fenced_heading_texts(text):
                raise Refusal("FENCED_ANCHOR", f"heading {wanted!r} exists only inside a code fence")
            raise Refusal("ANCHOR_MISSING", f"no heading {wanted!r}")
        if op.under:
            parent = op.under.strip()
            hits = [h for h in hits if parent in enclosing_headings(heads, h[0])]
            if not hits:
                raise Refusal("ANCHOR_MISSING", f"no heading {wanted!r} under {parent!r}")
        if len(hits) > 1:
            raise Refusal("ANCHOR_AMBIGUOUS", f"heading {wanted!r} occurs {len(hits)} times"
                          + (f" under {op.under.strip()!r}" if op.under else ""))
        offset, level, title = hits[0]
        index = next(i for i, h in enumerate(heads) if h[0] == offset)
        own_end = heads[index + 1][0] if index + 1 < len(heads) else len(text)
        kind = "record" if _is_identity(title, level, text[offset:own_end], levels) else "section"
        key = rr.identity_token(title) if kind == "record" else title.strip()
        return _span_from(text, offset, level, key or title.strip(), kind)
    raise Refusal("ANCHOR_MISSING", "no anchor given (--id, --heading or --preamble)")


def _nested_records(text: str, span: Span, levels: tuple[int, ...]) -> list[str]:
    return [k for o, _lv, k in identity_headings(text, levels) if span.start < o < span.end]


def _first_heading(block: str) -> tuple[int, str] | None:
    line = block.split("\n", 1)[0]
    match = rr.HEADING.match(line.rstrip("\r"))
    return (len(match.group("hashes")), match.group("text").strip()) if match else None


def _check_body_headings(new: str, level: int, levels: tuple[int, ...], skip_first: bool,
                         what: str) -> None:
    """New text may nest deeper headings; it may not open a heading at or above `level` (it
    would re-segment the file) nor define another record (records are created by insert)."""
    heads = _headings(new)
    for index, (offset, _line, lv, title) in enumerate(heads):
        if skip_first and offset == 0:
            continue
        if lv <= level:
            raise Refusal("RESEGMENTATION", f"{what} carries heading {'#' * lv} {title!r} at or "
                          f"above the block's level {level}: it would cut the block and re-segment "
                          "what follows")
        own_end = heads[index + 1][0] if index + 1 < len(heads) else len(new)
        if _is_identity(title, lv, new[offset:own_end], levels):
            raise Refusal("NESTED_RECORD", f"{what} defines record {title!r} inside the block; "
                          "create records with insert-before / insert-after / append")


# ---------------------------------------------------------------- one operation

def _trail_norm(block: str) -> str:
    """A block's bytes with its trailing separator run removed: what 'unchanged' means for the
    block that gains a new neighbour (FREEZE_SCOPE_GATE's refinement, learned_gates_registry)."""
    return re.sub(r"(?:\n[ \t]*(?:---)?[ \t]*)+\n?\Z", "", block)


#: ops whose effect depends on where the addressed block ENDS. `insert-before` uses only the
#: block's start, and `append` has no anchor at all, so neither can be mis-scoped by an
#: unstated end.
END_SENSITIVE = ("replace", "replace-within", "delete", "insert-after")


def _check_bounded(span: Span, op: Op) -> None:
    """🔴 An end nobody wrote down is not a record boundary.

    The last block at its identity level has no following heading to stop it, so its span was
    silently taken to EOF — which in `working_model_current.md` made `id: BLOCK 3` cover the whole
    `## Changelog` and every batch section after it, and a tool that exists to make narrowness
    EXECUTABLE gave that edit no containment at all (Benchmark J; Mirror finding 13 on
    BATCH_20260928_001). The span is still computed the same way — `registry_records.partition`
    decides what a block is and nothing is re-parsed here — but an assumed end is now stated and,
    when it covers headings, refused: the caller either addresses the sub-block by its own
    `--heading`, or says with `--to-eof` that the record really does reach the end of the file.

    A genuinely-last record with nothing after it (`CLAIM 041`, `PAPER 118`, `LIT-0420`,
    `DL-MECH-113`, `DIS-020` on this checkout) swallows no heading and is not refused: the
    assumption is only unsafe where there is something to be wrong about.
    """
    if op.op not in END_SENSITIVE or not span.to_eof or not span.swallowed or op.to_eof:
        return
    inside = "; ".join(f"{'#' * lv} {title}" for lv, title in span.swallowed)
    raise Refusal("UNBOUNDED_SPAN", f"no heading at or above level {span.level} follows "
                  f"{span.key!r}, so its end is EOF by assumption, not by a boundary in the file: "
                  f"the span {span.start}→{span.end} covers {len(span.swallowed)} heading(s) "
                  f"that may not belong to it ({inside}). Address the sub-block by its own "
                  "--heading, or pass --to-eof to assert that the record does run to end of file")


def apply_one(text: str, op: Op, levels: tuple[int, ...]) -> tuple[str, dict[str, Any]]:
    """Apply one operation to `text` and prove its scope, or raise `Refusal`."""
    if op.under and not op.heading:
        raise Refusal("ANCHOR_MISSING", "--under qualifies a --heading and names nothing alone")
    cut = min(levels)
    before_blocks = rr.partition(text, levels)
    before_ids = [k for _o, _lv, k in identity_headings(text, levels)]
    expect_new: list[str] = []
    expect_gone: list[str] = []
    grows: str = ""           # key of the block allowed a trailing-separator difference
    if op.op == "append":
        if text and not text.endswith("\n"):
            raise Refusal("RESEGMENTATION", "the file does not end with a newline; appending would "
                          "glue the new block onto its last line")
        span = Span(len(text), len(text), cut, "@end", "end")
    else:
        span = resolve(text, op, levels)
    target = text[span.start:span.end]
    if op.op in ("replace", "replace-within", "delete"):
        nested = _nested_records(text, span, levels)
        if nested:
            raise Refusal("NESTED_RECORD", f"{span.key!r} contains record(s) {', '.join(nested)}; "
                          "editing it would rewrite them — address them by their own id")
    # After NESTED_RECORD: when the assumed tail holds whole records, that is the sharper
    # refusal and the one the caller can act on directly.
    _check_bounded(span, op)
    if op.op == "replace":
        new_block = op.text
        _check_replacement(target, new_block, span, op, levels, text)
        start, end, insert = span.start, span.end, new_block
        if op.rename_to:
            expect_gone.append(span.key)
            expect_new.append(op.rename_to)
    elif op.op == "replace-within":
        if not op.old:
            raise Refusal("OLD_ABSENT", "replace-within needs a non-empty old string")
        count = target.count(op.old)
        if count == 0:
            raise Refusal("OLD_ABSENT", f"old string not found inside {span.key!r}")
        if count > 1:
            raise Refusal("OLD_NOT_UNIQUE", f"old string occurs {count} times inside {span.key!r}; "
                          "widen it until it is unique")
        new_block = target.replace(op.old, op.new, 1)
        _check_replacement(target, new_block, span, op, levels, text)
        at = span.start + target.index(op.old)
        start, end, insert = at, at + len(op.old), op.new
    elif op.op == "delete":
        start, end, insert = span.start, span.end, ""
        if span.kind == "record":
            expect_gone.append(span.key)
        new_block = ""
    else:                                   # insert-before / insert-after / append
        new_block = op.text
        if not new_block.endswith("\n"):
            raise Refusal("RESEGMENTATION", "inserted text must end with a newline, or the "
                          "following heading would be glued onto its last line")
        lead = SEPARATOR_RUN.match(new_block)
        body = new_block[lead.end():] if lead else new_block
        if lead and op.op == "insert-before":
            raise Refusal("RESEGMENTATION", "insert-before text may not start with a separator: it "
                          "would attach to the preceding block, which is not the anchor")
        if lead and op.op in ("insert-after", "append"):
            grows = span.key if op.op == "insert-after" else (
                before_blocks[-1].key if before_blocks else "")
        first = _first_heading(body)
        if not first or first[0] > cut:
            raise Refusal("RESEGMENTATION", f"inserted text must start with a heading at level ≤ "
                          f"{cut} (a complete block); otherwise it becomes part of the neighbour")
        for block in rr.partition(body, levels):
            if block.kind == "record":
                expect_new.append(block.key)
        if op.op == "insert-before":
            start = end = span.start
        else:
            start = end = span.end
        insert = new_block
    out = text[:start] + insert + text[end:]
    _postconditions(text, out, start, end, insert, span, op, levels, before_blocks, before_ids,
                    expect_new, expect_gone, grows)
    return out, {"op": op.op, "anchor": op.anchor(), "key": span.key, "range": [start, end],
                 "span": [span.start, span.end], "span_end_assumed": span.to_eof,
                 "span_swallows": [f"{'#' * lv} {t}" for lv, t in span.swallowed],
                 "to_eof_asserted": bool(op.to_eof),
                 # The batch report can show that the op list did not silently change the record's
                 # line shape, and which ops declared that they meant to.
                 "lines": [len(statement_lines(target)), len(statement_lines(new_block))]
                 if op.op in ("replace", "replace-within") else [],
                 "reflow_asserted": bool(op.reflow),
                 "replaced_bytes": len(text[start:end].encode()),
                 "inserted_bytes": len(insert.encode()), "new_records": expect_new,
                 "removed_records": expect_gone}


# ------------------------------------------------- statement boundaries inside one record
#
# 🔴 A BYTE-CONSERVING EDIT WAS INVISIBLE TO EVERY PROOF ABOVE.
#
# Everything this tool proves is about the record's OUTSIDE: the bytes before and after the
# edited range, the other blocks, the record set. Inside the addressed record it proves nothing,
# and it does not have to for the containment argument to hold — but `BATCH_20260928_005` op `B2`
# showed what that leaves open. It inserted a new `DO_NOT_CITE` statement INSIDE the existing
# `DO_NOT_INFER` line of `CLAIM 032`, so that the prohibition was left standing as a bare edict
# and its 488 bytes of grounds — which argue about the `Wwox^+/−` null/wild-type genotype,
# `CLAIM 033` and Q230P — ended up under a prohibition about the `P47T/WT` missense heterozygote,
# joined to that statement's REVIVAL_TRIGGER by a single space. Two allele arguments, merged
# across a boundary the batch's own footer swore was unchanged. The record's boundary was
# untouched, so `propagate`'s all-or-nothing proof held; the record set was unchanged, so the
# post-condition held; `grep -c "Concatenarle in"` returned 1 before and 1 after, so every
# presence check held. It survived a FULL BATCH CYCLE and was caught by an ex-post Mirror review
# two batches later, as BLOCKING-SCIENTIFIC. The repair (`327a558`) is byte-for-byte conserving:
# 219 + 2,659 = 707 + 2,171 = 2,878 B.
#
# WHY THE OBVIOUS INVARIANTS ARE THE WRONG ONES, each measured rather than argued:
#
#  · "the number of PARAGRAPHS in the record is unchanged" — `B2` leaves the paragraph count
#    unchanged, so it catches nothing here. Worse, the two prohibitions of `CLAIM 032` are
#    ADJACENT LINES with no blank line between them, so a blank-line partition puts both
#    statements and their grounds in ONE unit and cannot see a move between them at all. A first
#    draft of this check keyed on blank lines and did NOT fire on `da250b5`. Hence
#    `statement_lines`.
#  · "every line's length is unchanged" — a legitimate `replace-within` changes a line's length
#    and a legitimate `append` adds lines, so this refuses nearly every real edit.
#  · "a per-line digest plus a declared expected-change set" — the declaration would have to
#    enumerate the lines the op touches, which is the op itself restated; an op list that declares
#    its own diff proves nothing about whether the diff moved meaning.
#
# So the signature checked is about CONTENT and not shape: a run of bytes LEAVES one statement of
# the record and is GAINED, verbatim, by a statement that does not continue it. Both halves are
# required. A line relocated intact is a reorder and is exempt. A deletion whose text happens to
# exist elsewhere in the record is not reported, because no line gained it. Indenting or
# blockquoting a line does not move it (`LINE_FURNITURE`).


def statement_lines(block: str) -> list[str]:
    """The block's statement lines: its non-blank lines, in order.

    🔴 THE LINE AND NOT THE BLANK-LINE PARAGRAPH, because that is the boundary the defect crossed.
    In `claim_registry_current.md` the two prohibitions of `CLAIM 032` are ADJACENT LINES with no
    blank line between them — `🔴 **`DO_NOT_INFER` …**` then `🔴 **`DO_NOT_CITE` …**` — so a
    blank-line partition puts both, and their grounds, in one unit and sees nothing when content
    moves from one to the other. Measured: a first draft of this check keyed on blank lines and did
    NOT fire on `da250b5`, the commit that introduced `B2`. The registries write one statement per
    line; the line is the unit a reader attributes meaning to, so it is the unit checked.
    """
    return [line for line in block.split("\n") if line.strip()]


def _folded(value: str) -> str:
    """Whitespace-folded text: a join that replaced a newline with a space still matches."""
    return " ".join(value.split())


#: Bytes of shared opening that identify which after-line CONTINUES a given before-line. These
#: lines open with a distinctive marker and field name (`🔴 **`DO_NOT_CITE` — …`, `**Last
#: update:** …`), so the opening is what a reader uses to say "this is the same statement,
#: edited" — and the check needs exactly that, because a statement edited in place is not a
#: statement whose content was reparented.
#:
#: 🔴 MEASURED, TWICE, AND BOTH TIMES DOWNWARD. At 24 B the J0 replay reported 5 refusals, and all
#: five were the same artefact: the registries' `**Last update:**` line shares exactly 23 bytes of
#: opening with its own replacement (`**Last update:** 2026-0`), so the line was read as removed
#: and the note it keeps was read as reparented. The floor exists only to stop a one-character
#: coincidence pairing two unrelated lines; every real field opening is longer than 8 bytes, and
#: ranking is by LONGEST shared opening, so the right pair still wins where several are possible.
CONTINUATION_PREFIX_BYTES = 8

#: Leading Markdown furniture — blockquote, list and table markers — stripped before two lines'
#: openings are compared. 🔴 The second measured artefact: `419b6803` blockquoted an existing
#: `CLAIM 004` flag by prefixing `> `, which left the two lines sharing NO opening at all, so 768
#: bytes of an unchanged statement were reported as reparented. Indenting or quoting a statement
#: does not move it.
LINE_FURNITURE = re.compile(r"\A[\s>*+|-]*")


def _opening(line: str) -> str:
    return LINE_FURNITURE.sub("", line)


def _prefix_bytes(left: str, right: str) -> int:
    """Bytes the two lines share from the start, ignoring leading Markdown furniture."""
    left, right = _opening(left), _opening(right)
    limit = min(len(left), len(right))
    index = 0
    while index < limit and left[index] == right[index]:
        index += 1
    return len(left[:index].encode())


def _continuations(before: list[str], after: list[str]) -> dict[int, int]:
    """before-line index → the after-line index that continues it.

    Identical text first, so an untouched line is never mistaken for a rewritten neighbour; then
    the longest shared opening, once, greedily. A line with no continuation was removed outright.
    """
    taken: set[int] = set()
    found: dict[int, int] = {}
    by_text: dict[str, list[int]] = {}
    for index, line in enumerate(after):
        by_text.setdefault(line, []).append(index)
    for index, line in enumerate(before):
        for candidate in by_text.get(line, ()):
            if candidate not in taken:
                found[index] = candidate
                taken.add(candidate)
                break
    ranked = sorted(
        ((_prefix_bytes(before[i], after[j]), i, j)
         for i in range(len(before)) if i not in found
         for j in range(len(after)) if j not in taken),
        key=lambda item: (-item[0], item[1], item[2]))
    for shared, i, j in ranked:
        if shared < CONTINUATION_PREFIX_BYTES or i in found or j in taken:
            continue
        found[i] = j
        taken.add(j)
    return found


def _residue(line: str, continuation: str, floor: int) -> list[str]:
    """Runs of ≥ `floor` bytes that this line lost — not present in the line that continues it."""
    if not continuation:
        return [line] if len(line.encode()) >= floor else []
    return [line[i1:i2] for tag, i1, i2, _j1, _j2 in difflib.SequenceMatcher(
        None, line, continuation, autojunk=False).get_opcodes()
        if tag in ("delete", "replace") and len(line[i1:i2].encode()) >= floor]


def _gained(line: str, predecessor: str, floor: int) -> list[str]:
    """Runs of ≥ `floor` bytes this line gained — absent from the line it continues."""
    if not predecessor:
        return [line] if len(line.encode()) >= floor else []
    return [line[j1:j2] for tag, _i1, _i2, j1, j2 in difflib.SequenceMatcher(
        None, predecessor, line, autojunk=False).get_opcodes()
        if tag in ("insert", "replace") and len(line[j1:j2].encode()) >= floor]


def _shared_run(source: str, destination: str, floor: int) -> str:
    """The longest run the two share, once whitespace is folded, if it reaches `floor` bytes."""
    left, right = _folded(source), _folded(destination)
    match = difflib.SequenceMatcher(None, left, right, autojunk=False).find_longest_match(
        0, len(left), 0, len(right))
    run = left[match.a:match.a + match.size]
    return run if len(run.encode()) >= floor else ""


def cross_line_moves(old_block: str, new_block: str,
                     floor: int = MOVED_BYTES_FLOOR) -> list[tuple[str, str, str]]:
    """(from, to, the moved run) for every run of ≥ `floor` bytes REPARENTED inside one block.

    A run is reparented when it leaves one statement line of the block and is GAINED, verbatim, by
    a line that does not continue it. Both halves are required, and that is what keeps the check
    narrow: a line that merely changes length loses nothing to anyone, a deletion whose text
    happens to exist elsewhere in the record is not reported because no line gained it, and a line
    relocated intact is a reorder and is exempted explicitly below.
    """
    before, after = statement_lines(old_block), statement_lines(new_block)
    continuation = _continuations(before, after)
    predecessor = {j: i for i, j in continuation.items()}
    lost = {i: _residue(line, after[continuation[i]] if i in continuation else "", floor)
            for i, line in enumerate(before)}
    entered = {j: _gained(line, before[predecessor[j]] if j in predecessor else "", floor)
               for j, line in enumerate(after)}
    found: list[tuple[str, str, str]] = []
    for source, runs in lost.items():
        for destination, arrivals in entered.items():
            if continuation.get(source) == destination:
                continue
            for gone in runs:
                for arrived in arrivals:
                    run = _shared_run(gone, arrived, floor)
                    if not run:
                        continue
                    # A whole line that left one place and arrived intact in another is a
                    # REORDER: no statement is severed and no two arguments are merged, so it
                    # passes. Reparenting is a PART of a line landing inside another.
                    if (_folded(run) == _folded(before[source])
                            and _folded(run) == _folded(after[destination])):
                        continue
                    found.append((f"line {source + 1}", f"line {destination + 1}", run))
    return found


def _check_line_boundaries(target: str, new_block: str, span: Span, op: Op) -> None:
    """Refuse an edit that reparents content across a line boundary inside the record."""
    if op.reflow:
        return
    moved = cross_line_moves(target, new_block)
    if not moved:
        return
    where, into, run = moved[0]
    excerpt = _folded(run)
    excerpt = excerpt[:120] + ("…" if len(excerpt) > 120 else "")
    raise Refusal("CROSS_LINE_MOVE",
                  f"{len(run.encode())} byte(s) leave {where} of {span.key!r} and are gained, "
                  f"verbatim, by {into}, which does not continue it: the edit REPARENTS content "
                  f"across a statement boundary INSIDE the addressed record — which every proof "
                  f"here misses, because the record's own boundary, its record set and (in the "
                  f"repair's case) even its total are untouched. BATCH_20260928_005 op B2 severed "
                  f"a DO_NOT_INFER prohibition from its grounds exactly so, leaving a bare edict "
                  f"and two allele arguments merged in one paragraph, and it took an ex-post "
                  f"Mirror review two batches later to see it. Moved run: {excerpt!r}"
                  + (f" — and {len(moved) - 1} more" if len(moved) > 1 else "")
                  + ". Address each line with its own op, or pass --reflow (\"reflow\": true) to "
                    "declare that this op means to split or join a statement.")


def _check_replacement(target: str, new_block: str, span: Span, op: Op,
                       levels: tuple[int, ...], text: str) -> None:
    _check_line_boundaries(target, new_block, span, op)
    if span.kind == "preamble":
        if _headings(new_block):
            raise Refusal("RESEGMENTATION", "the preamble may not gain a heading")
        return
    old_first = _first_heading(target)
    new_first = _first_heading(new_block)
    if not new_first or new_first[0] != span.level:
        raise Refusal("RESEGMENTATION", f"the new text must open with the block's own level-"
                      f"{span.level} heading")
    if span.kind == "record":
        old_id, new_id = span.key, rr.identity_token(new_first[1]) or new_first[1]
        wanted = op.rename_to or old_id
        if not rr.same_id(new_id, wanted):
            raise Refusal("IDENTITY_CHANGED", f"the new heading defines {new_id!r}, not {wanted!r}"
                          + ("" if op.rename_to else "; pass --rename-to to rename a record"))
        if op.rename_to and any(rr.same_id(k, op.rename_to)
                                for _o, _l, k in identity_headings(text, levels)):
            raise Refusal("DUPLICATE_ID", f"record {op.rename_to!r} already exists")
    elif old_first and new_first[1] != old_first[1] and new_first[1] != op.rename_to:
        raise Refusal("IDENTITY_CHANGED", f"the section heading changes from {old_first[1]!r} to "
                      f"{new_first[1]!r}; pass --rename-to with the new heading")
    _check_body_headings(new_block, span.level, levels, True, "the new text")
    if span.end < len(text) and not new_block.endswith("\n"):
        raise Refusal("RESEGMENTATION", "the new text must end with a newline, or the next "
                      "heading would be glued onto its last line")


def _postconditions(text: str, out: str, start: int, end: int, insert: str, span: Span, op: Op,
                    levels: tuple[int, ...], before_blocks: list[rr.Block],
                    before_ids: list[str], expect_new: list[str], expect_gone: list[str],
                    grows: str) -> None:
    def fail(message: str) -> None:
        raise Refusal("POSTCONDITION", message)

    if out[:start] != text[:start]:
        fail("bytes before the edited range changed")
    if out[start + len(insert):] != text[end:]:
        fail("bytes after the edited range changed")
    after_ids = [k for _o, _lv, k in identity_headings(out, levels)]
    for new in expect_new:
        if any(rr.same_id(new, k) for k in before_ids):
            raise Refusal("DUPLICATE_ID", f"record {new!r} already exists in the file")
    expected = [k for k in before_ids if not any(rr.same_id(k, g) for g in expect_gone)]
    if sorted(map(_idnorm, after_ids)) != sorted(map(_idnorm, expected + expect_new)):
        extra = sorted(set(map(_idnorm, after_ids)) - set(map(_idnorm, expected + expect_new)))
        lost = sorted(set(map(_idnorm, expected + expect_new)) - set(map(_idnorm, after_ids)))
        raise Refusal("RESEGMENTATION", f"the result defines a different record set "
                      f"(unexpected {extra or '—'}, missing {lost or '—'})")
    after_blocks = {b.key: out[b.start:b.end] for b in rr.partition(out, levels)}
    touched = {span.key} | set(expect_gone)
    if op.rename_to:
        touched.add(op.rename_to)
    for block in before_blocks:
        if block.key in touched or _covers(block, span) or block.kind == "preamble" and span.kind == "preamble":
            continue
        old = text[block.start:block.end]
        new = after_blocks.get(block.key)
        if new is None:
            if op.op == "delete" and block.start >= span.start and block.end <= span.end:
                continue
            fail(f"block {block.key!r} disappeared")
        if new != old and not (block.key == grows and _trail_norm(new) == _trail_norm(old)):
            if op.op in ("insert-before", "insert-after", "append") and _trail_norm(new) == _trail_norm(old):
                fail(f"block {block.key!r} changed its trailing separator")
            fail(f"block {block.key!r} changed although it was not the target")


def _covers(block: rr.Block, span: Span) -> bool:
    """The partition block that holds a nested target (a `--heading` sub-block) is the target."""
    return block.start <= span.start < block.end and span.end <= block.end and span.kind != "end"


def _idnorm(value: str) -> str:
    return " ".join(value.split()).lower()


# ---------------------------------------------------------------- batch

def apply_ops(text: str, ops: list[Op], levels: tuple[int, ...]) -> tuple[str, Report]:
    """All operations in order, each anchored on the text the previous one produced — all or
    nothing: a refusal anywhere leaves the caller with the input unchanged."""
    report = Report()
    current = text
    for index, op in enumerate(ops):
        try:
            current, info = apply_one(current, op, levels)
        except Refusal as refusal:
            refusal.args = (f"op {index + 1}/{len(ops)} ({op.op} {op.anchor()}): {refusal.args[0]}",)
            raise
        report.ops.append(info)
        report.changed_keys.append(info["key"])
    return current, report


# ---------------------------------------------------------------- CLI

def _read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8")


def _arg_text(inline: str | None, file: Path | None) -> str:
    if file is not None:
        return _read_text(file)
    return inline or ""


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    lister = sub.add_parser("blocks", help="list the addressable blocks of a file")
    lister.add_argument("--file", type=Path, required=True)
    lister.add_argument("--surface", default="")
    for name in OPS + ("apply",):
        p = sub.add_parser(name)
        p.add_argument("--file", type=Path, required=True)
        p.add_argument("--surface", default="", help="identity-level surface stem (default: file stem)")
        p.add_argument("--apply", action="store_true", help="write the result (default: dry run)")
        p.add_argument("--json", action="store_true")
        if name == "apply":
            p.add_argument("--ops", type=Path, required=True,
                           help="JSON list of {op, id|heading[+under]|preamble, text|old|new, rename_to}")
            continue
        if name != "append":
            group = p.add_mutually_exclusive_group(required=True)
            group.add_argument("--id", default="")
            group.add_argument("--heading", default="")
            group.add_argument("--preamble", action="store_true")
            p.add_argument("--under", default="",
                           help="with --heading: the exact text of an enclosing heading, to "
                                "choose between sections that share a heading")
            p.add_argument("--to-eof", action="store_true",
                           help="assert that the addressed block really runs to end of file; "
                                "without it an op on a span whose end the file does not state, "
                                "and which covers headings, is refused (UNBOUNDED_SPAN)")
        if name in ("replace", "replace-within"):
            p.add_argument("--reflow", action="store_true",
                           help="declare that this op means to split or join a statement inside "
                                "the record; without it, content re-parented from one line of "
                                "the addressed record onto another is refused "
                                "(CROSS_LINE_MOVE)")
        if name in ("replace", "insert-before", "insert-after", "append"):
            p.add_argument("--text", default=None)
            p.add_argument("--text-file", type=Path)
        if name == "replace":
            p.add_argument("--rename-to", default="")
        if name == "replace-within":
            p.add_argument("--old", default=None)
            p.add_argument("--old-file", type=Path)
            p.add_argument("--new", default=None)
            p.add_argument("--new-file", type=Path)
    args = parser.parse_args(argv)
    try:
        text = _read_text(args.file)
    except (OSError, UnicodeDecodeError) as error:
        print(f"TOOL ERROR: cannot read {args.file}: {error}", file=sys.stderr)
        return 2
    levels = levels_for(str(args.file), args.surface)
    if args.command == "blocks":
        for block in rr.partition(text, levels):
            print(f"{block.line:>6}  {block.kind:<8} L{block.level}  {block.key}")
        dups = [k for _o, _l, k in identity_headings(text, levels)]
        repeated = sorted({k for k in dups if dups.count(k) > 1})
        if repeated:
            print(f"DUPLICATE record ids (every edit anchored on them is refused): {repeated}")
        for offset, level, key in identity_headings(text, levels):
            span = _span_from(text, offset, level, key, "record")
            if span.to_eof and span.swallowed:
                print(f"UNBOUNDED span {key!r} {span.start}→{span.end}: no heading at or above "
                      f"level {level} follows, so the end is assumed. It covers "
                      + "; ".join(f"{'#' * lv} {t}" for lv, t in span.swallowed)
                      + " — replace/replace-within/delete/insert-after here are refused "
                        "(UNBOUNDED_SPAN) unless --to-eof says the record reaches EOF.")
        return 0
    try:
        if args.command == "apply":
            ops = [Op.from_dict(item) for item in json.loads(_read_text(args.ops))]
        else:
            ops = [Op(op=args.command, id=getattr(args, "id", "") or "",
                      heading=getattr(args, "heading", "") or "",
                      preamble=bool(getattr(args, "preamble", False)),
                      text=_arg_text(getattr(args, "text", None), getattr(args, "text_file", None)),
                      old=_arg_text(getattr(args, "old", None), getattr(args, "old_file", None)),
                      new=_arg_text(getattr(args, "new", None), getattr(args, "new_file", None)),
                      rename_to=getattr(args, "rename_to", "") or "",
                      under=getattr(args, "under", "") or "",
                      to_eof=bool(getattr(args, "to_eof", False)),
                      reflow=bool(getattr(args, "reflow", False)))]
    except (OSError, ValueError, TypeError) as error:
        print(f"invalid invocation: {error}", file=sys.stderr)
        return 2
    try:
        out, report = apply_ops(text, ops, levels)
    except Refusal as refusal:
        print(f"REFUSED — {refusal}\nNothing was written.", file=sys.stderr)
        return 3
    diff = "".join(difflib.unified_diff(text.splitlines(keepends=True),
                                        out.splitlines(keepends=True),
                                        str(args.file), str(args.file) + " (edited)", n=1))
    summary = {"file": str(args.file), "applied": bool(args.apply), "ops": report.ops,
               "input_sha256": _digest(text), "output_sha256": _digest(out),
               "scope_proof": "bytes outside each edited range identical; every other block "
                              "identical; record set as declared"}
    if args.apply and out != text:
        args.file.write_bytes(out.encode("utf-8"))
    if args.json:
        print(json.dumps({**summary, "diff": diff}, ensure_ascii=False, indent=1))
    else:
        sys.stdout.write(diff)
        for info in report.ops:
            print(f"  scope {info['key']!r}: span {info['span'][0]}→{info['span'][1]}"
                  + (" (end ASSUMED — no following heading at or above the block's level"
                     + (f"; covers {', '.join(info['span_swallows'])}"
                        if info["span_swallows"] else "; covers no heading") + ")"
                     if info["span_end_assumed"] else "")
                  + (" — asserted with --to-eof" if info["to_eof_asserted"] else ""))
        print(("APPLIED" if args.apply else "DRY RUN — nothing written; add --apply") +
              f": {len(report.ops)} op(s), keys {report.changed_keys}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
