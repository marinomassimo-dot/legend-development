#!/usr/bin/env python3
"""What a bibliographic corpus is, and how every guard recognises one.

A local corpus of abstracts is useful for triage and catastrophic as evidence, so three
independent places have to refuse it: the harvester that creates one, the receipt writer that
records a reading, and the deep-dive manifest that anchors quotes. Until now each carried its
own copy of one regular expression, which is two failure modes at once — the copies drift, and
**a name is not a fact**.

Recognition by name is the weaker half and cannot be made strong. `--out-dir` is a free
parameter; a corpus can be copied or renamed, and the regex sees none of that. Content
recognition deliberately targets the committed harvester schema: claiming to recognise every
bibliographic format would turn an evidence guard into a paper-rejection hazard. Reviewed
2026-08-06: even the harvester's own destination check was
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

# Fields and values that identify this harvester's PubMed records. Requiring an exact record
# type plus the stable schema is intentional. "Three familiar keys" produced a false positive
# for an unrelated experimental JSONL carrying `record_type`, `pmid`, and `identifiers`.
CORPUS_RECORD_TYPES = frozenset({"PubmedArticle", "PubmedBookArticle"})
CORPUS_RECORD_KEYS = frozenset({"pmid", "title", "abstract_parts", "identifiers"})
# The header of a derived seed TSV, under either the current or the pre-2026-08-05 column name.
CORPUS_TSV_COLUMNS = frozenset({"pmid", "title"})
CORPUS_TSV_MARKERS = ("pubmed_free_full_text_link", "free_full_text", "abstract")

SNIFF_BYTES = 1048576


def _first_json_record(text: str) -> dict | None:
    """Decode the first object from JSONL, a JSON object, or a JSON array.

    `json.loads(first_line)` only recognised compact JSONL. The same records pretty-printed
    across lines or wrapped in an array survived a rename, which made a content firewall
    depend on whitespace and packaging. `raw_decode` needs only the first array element, not
    the closing bracket or the rest of a potentially large corpus.
    """
    candidate = text.lstrip("\ufeff \t\r\n")
    if candidate.startswith("["):
        candidate = candidate[1:].lstrip()
    if not candidate.startswith("{"):
        return None
    try:
        value, _ = json.JSONDecoder().raw_decode(candidate)
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


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

    text = head.decode("utf-8", errors="replace")
    record = _first_json_record(text)
    if (record is not None
            and record.get("record_type") in CORPUS_RECORD_TYPES
            and CORPUS_RECORD_KEYS <= set(record)):
        return True

    first = head.split(b"\n", 1)[0].strip()
    header = first.decode("utf-8", errors="replace")
    if "\t" in header:
        columns = {column.strip().lower() for column in header.split("\t")}
        if CORPUS_TSV_COLUMNS <= columns and any(m in columns for m in CORPUS_TSV_MARKERS):
            return True
    return False


def path_like(value: str) -> bool:
    """True when a value is a locator rather than a sentence.

    🔴 Free prose was being run through the corpus check, so an honest workflow note —
    "triaged from files/corpus/ then read the publisher PDF end to end" — was refused, while
    the same reading described vaguely sailed through. That guard rewards under-documenting
    the provenance, which is the opposite of what this repository is for: triage from the
    corpus is a PERMITTED use and saying so out loud must stay free. A locator has no spaces.
    """
    text = str(value or "").strip()
    return bool(text) and not any(character.isspace() for character in text)


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
