#!/usr/bin/env python3
"""What a bibliographic corpus is, and how every guard recognises one.

A local corpus of abstracts is useful for triage and catastrophic as evidence, so three
independent places have to refuse it: the harvester that creates one, the receipt writer that
records a reading, and the deep-dive manifest that anchors quotes. Until now each carried its
own copy of one regular expression, which is two failure modes at once — the copies drift, and
**a name is not a fact**.

Recognition by name is the weaker half and cannot be made strong. `--out-dir` is a free
parameter; a corpus can be copied, renamed, or produced by a different tool entirely, and the
regex sees none of that. Reviewed 2026-08-06: even the harvester's own destination check was
bypassable with `files/corpus/../../staging/wwox.jsonl`, which matches the pattern as a string
and writes somewhere else.

So this module carries both halves:

* `CORPUS_ARTEFACT` — the naming convention, enforced at creation so the convention holds;
* `looks_like_corpus` — what the *file on disk* actually is, which no rename survives.

The second is the load-bearing one. A guard that only knows the first is a guard against
accidents, not against the failure mode: hundreds of greppable abstracts sitting locally make
answering from them feel like working, and the file does not have to be called `corpus` for
that to happen.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

# The naming convention. Enforced where corpora are created, so the paths the guards match
# are the paths that exist. Matched against a RESOLVED path — see `names_a_corpus`.
CORPUS_ARTEFACT = re.compile(
    r"files/corpus/|corpus_seed_pubmed|_corpus\.jsonl|corpus_abstracts", re.IGNORECASE)

# Fields that identify a harvested PubMed record. A JSONL whose first line carries these is a
# bibliographic export whatever it has been renamed to.
CORPUS_RECORD_KEYS = frozenset({"record_type", "abstract_parts", "identifiers", "pmid"})
# The header of a derived seed TSV, under either the current or the pre-2026-08-05 column name.
CORPUS_TSV_COLUMNS = frozenset({"pmid", "title"})
CORPUS_TSV_MARKERS = ("pubmed_free_full_text_link", "free_full_text", "abstract")

SNIFF_BYTES = 65536


def names_a_corpus(value: str) -> bool:
    """True when a path *string* follows the corpus naming convention.

    Resolves `..` first: `files/corpus/../../staging/wwox.jsonl` contains `files/corpus/` and
    is not in `files/corpus/` at all. Comparing the unresolved string is how a check that
    reads correctly accepts the one input it exists to refuse.
    """
    text = str(value or "").strip()
    if not text:
        return False
    normalised = text.replace("\\", "/")
    if ".." in Path(normalised).parts:
        try:
            normalised = Path(normalised).resolve().as_posix()
        except (OSError, RuntimeError):
            return False
    return bool(CORPUS_ARTEFACT.search(normalised))


def looks_like_corpus(path: Path) -> bool:
    """True when the file itself is a harvested bibliographic export.

    Content, not convention. This is what survives `cp files/corpus/wwox.jsonl
    files/fulltext/paper.jsonl`, which is the whole reason the naming check is not enough.
    Absent or unreadable files return False: this decides "is this a corpus", not "does this
    exist", and the callers already check existence separately.
    """
    try:
        if not path.is_file():
            return False
        with path.open("rb") as handle:
            head = handle.read(SNIFF_BYTES)
    except OSError:
        return False

    first = head.split(b"\n", 1)[0].strip()
    if first.startswith(b"{"):
        try:
            record = json.loads(first.decode("utf-8", errors="replace"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            record = None
        if isinstance(record, dict) and len(CORPUS_RECORD_KEYS & set(record)) >= 3:
            return True

    header = first.decode("utf-8", errors="replace")
    if "\t" in header:
        columns = {column.strip().lower() for column in header.split("\t")}
        if CORPUS_TSV_COLUMNS <= columns and any(m in columns for m in CORPUS_TSV_MARKERS):
            return True
    return False


def corpus_objection(value: str, root: Path | None = None) -> str:
    """The reason this path may not be evidence, or "" if there is none.

    One sentence, one place, so three guards cannot disagree about what they are refusing.
    """
    if names_a_corpus(value):
        return ("names a bibliographic corpus. An export of abstracts is not a document; "
                "read the paper")
    candidate = Path(value) if root is None else root / value
    if looks_like_corpus(candidate):
        return ("is a harvested bibliographic export, whatever it has been renamed to: its "
                "contents are PubMed records, not a paper. An abstract is not a reading")
    return ""
