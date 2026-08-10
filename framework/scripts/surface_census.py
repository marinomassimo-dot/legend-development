#!/usr/bin/env python3
"""surface_census.py — which reading surface exists, per paper, and whether it can be trusted.

Rule 5d of `CLAUDE.md` ends with an instruction that was never implemented: *"Prefer
XML/HTML PMC over the PDF, always, **and record the absence**."* The preference was
recorded. The absence was not. The local corpus holds dozens of papers whose only surface is
a PDF, and that split existed nowhere in the state — so a session opening the full-text queue
could not tell which entries it could read today and which it would discover, three papers
in, had a defective text layer. That discovery has already been made from scratch more than
once.

This script derives the split and writes it into the queue as a dated section.

🔴 **An `.html` extension is not a structured surface.** Two files in this corpus are the
article's PDF text layer wrapped in `<article><section><pre>` — markup around a dump, with no
JATS metadata behind it. They are the two Suzuki papers that `CLAUDE.md` names as having no
structured deposit at all, and one of them fails the corruption screen. Classifying them
`structured` because of their suffix would have told every future session to read, as
publisher markup, the exact text layer that had to be adjudicated at 600 dpi against the
printed page. So the classification reads the bytes, and demotes what it cannot recognise as
markup. The rule only ever demotes: its worst case is telling you to acquire XML for a paper
that already had good HTML.

What this is **not**:

  * **Not a gate.** No threshold, nothing blocked, no regression re-deriving it. It reports.
  * **Not a verification.** `clean` means "the text carries none of the known corruption
    signatures" — never "quotes taken from it will match the page". Those signatures were
    calibrated against this corpus and catch what has been seen, which is not the same as
    everything there is.
  * **Not a licence to quote a PDF.** `deepdive_manifest._artifact_text` still refuses
    `.pdf` for a text `kind`, and this census does not touch that. Text is extracted from a
    PDF here *only to be screened*, which is the job the screen was written for.

It is a photograph with a date on it. `files/fulltext/` is gitignored and grows between
sessions, so a census can only describe the day it was taken — which is why it prints the
corpus listing digest beside the numbers instead of pretending to be an invariant. Phase 4.7
of `prompt_batch_commit.md` regenerates it *when the corpus is present* and skips it
otherwise: a batch must not abort over a gitignored directory that BATCH_COMMIT never
touches.

🔴 **It is a separate file, and it must stay one.** The first version spliced this table into
`full_text_queue_current.md`, where the operator asked for it, and that quietly disarmed two
existing checks. `session_self_eval.py` counts a paper's presence in the queue as *declared
reading debt*, so a derived table naming every corpus PMID cleared five unread premises that
nobody had read; `batch_queue.py` scans every `*_current.md` for PMIDs and drifted. The
comment above `LANDING_FILES` in `session_self_eval.py` had already written the rule down —
*"counting them would let a paper land in a file that merely reflects the ledger it failed to
reach"* — for the two generated views that already existed. A derived surface is not a
declaration, and it must not live inside a file that is one.

Usage:
    python3 framework/scripts/surface_census.py --disease wwox [--corpus DIR] \
        --out disease-models/wwox/research/surface_census.md

`--corpus` exists because sessions now run in per-session git worktrees while the corpus
lives, once, in the main checkout. Without it a worktree session would have to conclude that
every paper is `absent`, which is false: `absent` means "nothing local for this paper", and
"the corpus directory is not here" is a different fact. The two are kept apart — a missing
corpus root refuses to produce a census rather than emitting dozens of confident lies.

PyMuPDF is optional. Without it every PDF is reported `not_screened`, which is the honest
state and not a silent pass.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import deepdive_manifest
import legend_lint

# 🔴 Imported, not re-implemented, and deliberately reaching for private names. The
# signatures in `deepdive_manifest` were calibrated against all 51 local PDFs — the `q` that
# stands in for `±` 140 times, the `D2` anchored to statistical context so it does not flag a
# real `D2` timepoint, the suspicion-by-absence rule. A second copy of that list would be
# right on the day it was written and wrong on every day after. If either name is renamed
# this import fails loudly at startup; a duplicated screen would fail silently and forever.
SCREEN = deepdive_manifest._refuse_suspect_surface  # noqa: SLF001 — one definition, on purpose
READ_TEXT_SURFACE = deepdive_manifest._artifact_text  # noqa: SLF001

ROOT = Path(__file__).resolve().parents[2]

# `PMID<digits>_` is the corpus filename convention. It is the only identity claim a file
# makes about itself, so it is the only one trusted here.
ARTICLE_FILE = re.compile(r"^PMID(?P<pmid>\d{6,8})_")
MARKUP_SUFFIXES = frozenset({".xml", ".html", ".htm"})
PDF_SUFFIX = ".pdf"
DERIVED_TEXT_SUFFIX = ".txt"
# Suffixes `deepdive_manifest._artifact_text` knows how to open and screen. Restricting the
# call to these keeps its "text verification is unsupported for …" branch unreachable, so
# every ValueError coming back from it is a corruption verdict and never a wrong file type.
SCREENABLE_TEXT = MARKUP_SUFFIXES | {DERIVED_TEXT_SUFFIX}

# What separates publisher markup from a text layer in a costume. JATS metadata is the
# positive signal; a `<pre>` block carrying the body is the negative one. Both are read from
# the raw bytes — no parsing, no guessing at semantics.
JATS_MARKER = re.compile(rb"article-meta|journal-meta|<!DOCTYPE\s+article", re.I)
PRE_BLOCK = re.compile(rb"<pre[\s>]", re.I)

# The full-text queue is not a growth-anchored registry: `growth_anchors.HEADINGS` defines
# `CLAIM`, `PAPER`, `CORPUS` and the rest, and has no entry for `FT`. Checked before writing
# this pattern, per PATTERN_ALREADY_SOLVED_GATE — there was nothing to reuse.
QUEUE_ENTRY = re.compile(r"^## (?P<id>FT-\d+)", re.M)
# 🔴 Anchored at the start of the identity line, and nowhere else. The loose form
# `PMID\s*(\d+)` anywhere in the entry body resolves FT-020 — whose `**Paper:**` line reads
# *"riferimenti 38, 39 e 87 di PMID 34214506 — non risolti a PMID"* — to the paper that
# *cites* the three unknown works. That is the citing source, not the queued paper, and the
# entry says so in the same sentence. Under-resolving is recoverable: it lands in the loss
# ledger, where a human can see it. Mis-resolving attaches a surface verdict to the wrong
# paper, and nothing downstream would ever question it.
# 🔴 The identity-line grammar lives in `legend_lint.py` and is imported, not restated. Both
# files ask the same question — which paper is this entry about — and a second copy would have
# them answer it differently the first time either changed. That drift is not hypothetical: it
# happened inside this file on 2026-08-10, when widening the reader to accept several
# identifiers per line silently dropped the anchoring that keeps `FT-020` from resolving to
# the paper it cites. A unit test caught it; one definition means there is nothing to catch.
IDENTITY_LINE = legend_lint.QUEUE_IDENTITY_RE
entry_identity = legend_lint.queue_entry_identity

SURFACE_MEANING = {
    "structured": "publisher XML/HTML present — read this one (rule 5d)",
    "pdf_only": "no structured surface locally — acquire XML/HTML before reading",
    "absent": "queued, nothing local at all — retrieve first",
}
SENTINEL_MEANING = {
    "SUSPECT": "the text carries a known corruption signature — do not quote it; adjudicate "
               "against the rendered page, or re-acquire the paper structured",
    "clean": "no known signature found — this is not a verification",
    "not_screened": "no deterministic extractor available, or extraction failed",
}
SURFACE_ORDER = ("structured", "pdf_only", "absent")
VERDICT_ORDER = ("SUSPECT", "clean", "not_screened")
# `other` is corpus material that is not an article reading surface: `.md` handoffs, `.docx`
# and `.zip` supplements, `.tar.gz` packages, asset directories. Counted and excluded, never
# silently dropped, and never allowed to make a paper look structured.
SURFACE_KINDS = ("structured", "text_dump", "pdf", "derived_text")


def classify_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == PDF_SUFFIX:
        return "pdf"
    if suffix == DERIVED_TEXT_SUFFIX:
        return "derived_text"
    if suffix not in MARKUP_SUFFIXES:
        return "other"
    raw = path.read_bytes()
    if JATS_MARKER.search(raw):
        return "structured"
    return "text_dump" if PRE_BLOCK.search(raw) else "structured"


@dataclass
class Paper:
    pmid: str
    queue_ids: list = field(default_factory=list)
    files: list = field(default_factory=list)   # [(filename, kind)]

    @property
    def kinds(self) -> set:
        return {kind for _name, kind in self.files}

    @property
    def surfaces(self) -> list:
        return sorted((name, kind) for name, kind in self.files if kind in SURFACE_KINDS)

    @property
    def surface(self) -> str:
        if "structured" in self.kinds:
            return "structured"
        if self.kinds & set(SURFACE_KINDS):
            return "pdf_only"
        return "absent"


@dataclass
class Census:
    papers: list
    losses: list
    sentinel: dict
    corpus_dir: Path
    corpus_entries: int
    corpus_digest: str
    extractor: str
    queue_entries: int
    resolved_entries: int
    corpus_papers: int
    queued_papers: int
    merged: int
    text_dumps: list


def corpus_index(corpus_dir: Path):
    """Map PMID -> [(filename, kind)], and count the entries that name no paper.

    Only the top level is read. Asset directories hold figures and supplements; figures are
    inspected at original resolution during a reading and are never a text surface.
    """
    by_pmid: dict = {}
    unattributed: list = []
    for path in sorted(corpus_dir.iterdir()):
        if path.name.startswith("."):
            continue
        match = ARTICLE_FILE.match(path.name) if path.is_file() else None
        if match:
            by_pmid.setdefault(match.group("pmid"), []).append(
                (path.name, classify_file(path)))
        else:
            unattributed.append(path.name)
    return by_pmid, unattributed


def queue_entries(text: str):
    """Split the queue into (FT id, body), keeping every entry including the last."""
    bounds = [(match.group("id"), match.start()) for match in QUEUE_ENTRY.finditer(text)]
    entries = []
    for index, (entry_id, start) in enumerate(bounds):
        end = bounds[index + 1][1] if index + 1 < len(bounds) else len(text)
        entries.append((entry_id, text[start:end]))
    return entries


def resolve_queue(text: str):
    """Return PMID -> [FT ids], and a typed loss ledger for the entries that resolve to none.

    An entry resolved by DOI alone is *not* a loss — `FT-033` is a 2007 pre-WWOX linkage
    study with no PMID in any local source, and `FT-007`/`FT-009` are bioRxiv preprints. The
    census simply has nothing local to join them to, which is a different fact from the
    entry failing to say what it is, and is recorded as its own state.
    """
    resolved: dict = {}
    losses: list = []
    for entry_id, body in queue_entries(text):
        pmids, dois, state = entry_identity(body)
        if pmids:
            for pmid in pmids:
                resolved.setdefault(pmid, []).append(entry_id)
            continue
        line = IDENTITY_LINE.search(body)
        verbatim = " ".join(line.group(1).split()) if line else "—"
        losses.append((entry_id, "doi_only" if dois else state, verbatim))
    return resolved, losses


def extract_pdf_text(path: Path) -> str:
    import fitz  # noqa: PLC0415 — optional dependency, only needed to screen a PDF

    with fitz.open(path) as document:
        return "\n".join(page.get_text() for page in document)


def extractor_identity() -> str:
    try:
        import fitz  # noqa: PLC0415
    except ImportError:
        return ""
    version = getattr(fitz, "pymupdf_version", None) or getattr(fitz, "VersionBind", "?")
    return f"PyMuPDF {version}"


OFFSET_NOISE = re.compile(r"\s+at offset \d+")


def short_reason(message: str, name: str) -> str:
    """The first sentence of a SUSPECT message, without the filename or the byte offset.

    The full message is a paragraph explaining why the surface must be re-derived rather than
    repaired — that belongs in the validator that refuses a write, not in a census row. The
    offset goes too: it points at a byte in an extraction this table is telling you not to
    quote from.
    """
    body = message.split(f"{name} ", 1)[-1]
    return OFFSET_NOISE.sub("", body.split(". ", 1)[0]).strip().rstrip(".")


def screen_paper(paper: Paper, corpus_dir: Path, have_extractor: bool):
    """Sentinel verdict for the surface this paper would actually be read from.

    Structured markup is screened too, not only the PDFs the operator asked about: the file
    in this corpus that most needed screening wears an `.html` extension, and a census
    trusting the suffix would have declared it clean by never looking.

    🔴 But only the surface you would *read* is screened. Half the structured papers keep the
    publisher's PDF beside the XML, and most of those PDFs have a broken text layer — scoring
    the paper on its worst file marked papers `SUSPECT` whose XML is perfectly good, telling a
    reader to stay away from the one surface rule 5d sends them to. The verdict answers "can I
    quote what I am about to open", so it is computed over exactly that.
    """
    reading_kinds = ({"structured"} if paper.surface == "structured"
                     else set(SURFACE_KINDS) - {"structured"})
    screenable = [(name, kind) for name, kind in paper.files if kind in reading_kinds]
    if not screenable:
        return "", ""

    unscreened = []
    for name, kind in screenable:
        path = corpus_dir / name
        try:
            if kind == "pdf":
                if not have_extractor:
                    unscreened.append(f"{name}: no deterministic extractor")
                    continue
                content = extract_pdf_text(path)
            else:
                # Raises only on corruption: the suffix is known-supported by construction.
                READ_TEXT_SURFACE(path, "article_text")
                continue
        except ValueError as suspect:
            return "SUSPECT", _detail(name, str(suspect), screenable)
        except Exception as error:  # noqa: BLE001 — a failure is "not screened", never "clean"
            unscreened.append(f"{name}: {type(error).__name__}")
            continue
        try:
            SCREEN(path, content)
        except ValueError as suspect:
            return "SUSPECT", _detail(name, str(suspect), screenable)
    if unscreened:
        return "not_screened", "; ".join(unscreened)
    return "clean", ""


def _detail(name: str, message: str, screenable: list) -> str:
    """Name the file only when the paper has more than one, so the common row stays short."""
    reason = short_reason(message, name)
    return reason if len(screenable) == 1 else f"{name}: {reason}"


def queue_file(root: Path, disease: str) -> Path:
    return root / "disease-models" / disease / "research" / "full_text_queue_current.md"


def build(root: Path, corpus_dir: Path, disease: str) -> Census:
    text = queue_file(root, disease).read_text(encoding="utf-8")
    resolved, losses = resolve_queue(text)
    by_pmid, unattributed = corpus_index(corpus_dir)

    papers = {pmid: Paper(pmid=pmid, files=list(files)) for pmid, files in by_pmid.items()}
    for pmid, ids in resolved.items():
        papers.setdefault(pmid, Paper(pmid=pmid)).queue_ids = ids

    have_extractor = bool(extractor_identity())
    sentinel = {}
    for paper in papers.values():
        verdict, detail = screen_paper(paper, corpus_dir, have_extractor)
        if verdict:
            sentinel[paper.pmid] = (verdict, detail)

    listing = "\n".join(
        f"{path.name}:{path.stat().st_size}"
        for path in sorted(corpus_dir.iterdir()) if path.is_file()
    )
    entries = queue_entries(text)
    return Census(
        papers=sorted(papers.values(), key=lambda item: int(item.pmid)),
        losses=losses,
        sentinel=sentinel,
        corpus_dir=corpus_dir,
        corpus_entries=sum(len(files) for files in by_pmid.values()) + len(unattributed),
        corpus_digest=hashlib.sha256(listing.encode("utf-8")).hexdigest()[:16],
        extractor=extractor_identity() or "none",
        queue_entries=len(entries),
        resolved_entries=len(entries) - len(losses),
        corpus_papers=len(by_pmid),
        queued_papers=len(resolved),
        merged=len(set(resolved) & set(by_pmid)),
        text_dumps=sorted(name for files in by_pmid.values()
                          for name, kind in files if kind == "text_dump"),
    )


def order(paper: Paper):
    """Queue entries first, in queue order; then the corpus papers nobody has queued."""
    if paper.queue_ids:
        return (0, int(paper.queue_ids[0].split("-")[1]))
    return (1, int(paper.pmid))


def cell(text: str) -> str:
    return text.replace("|", "\\|")


def render(census: Census, today: str) -> str:
    counts = {name: 0 for name in SURFACE_ORDER}
    for paper in census.papers:
        counts[paper.surface] += 1
    verdicts = {name: 0 for name in VERDICT_ORDER}
    for verdict, _detail in census.sentinel.values():
        verdicts[verdict] += 1
    suspect_pdf_only = sum(
        1 for paper in census.papers
        if paper.surface == "pdf_only"
        and census.sentinel.get(paper.pmid, ("", ""))[0] == "SUSPECT"
    )

    lines = [
        "# Surface census — what can be read now, per paper",
        "",
        "> **Generated file — do not edit by hand.** Regenerate with:",
        "> ```bash",
        "> python3 framework/scripts/surface_census.py --disease wwox \\",
        ">     --out disease-models/wwox/research/surface_census.md",
        "> ```",
        ">",
        "> A companion to [[full_text_queue_current]], and deliberately **not** part of it: a "
        "paper's presence in the queue is a declaration of reading debt that "
        "`session_self_eval.py` counts, and a derived table naming every corpus PMID is not a "
        "declaration of anything.",
        ">",
        "> A photograph, not an invariant. `files/fulltext/` is gitignored and grows between "
        "sessions, so these numbers describe the corpus on the census date and nothing "
        "re-checks them afterwards — compare the listing digest below against your own copy "
        "before trusting a row. This page blocks nothing and has no threshold: it exists so "
        "that rule 5d's *\"record the absence\"* is a fact in the state instead of a "
        "rediscovery made three papers into a reading.",
        "",
        f"**Census date:** {today}  ",
        f"**Corpus:** `{census.corpus_dir.name}` — {census.corpus_entries} entries, "
        f"{census.corpus_papers} papers, listing digest `{census.corpus_digest}`  ",
        f"**Sentinel:** `deepdive_manifest._refuse_suspect_surface`, "
        f"PDF text via {census.extractor}",
        "",
        "### Totals",
        "",
        "| Surface | Papers | What it means |",
        "|---|---:|---|",
    ]
    lines += [f"| `{name}` | {counts[name]} | {SURFACE_MEANING[name]} |"
              for name in SURFACE_ORDER]
    lines += [
        "",
        "Sentinel over the surface each paper would actually be read from — the structured "
        "file where one exists, the PDF otherwise. Structured markup is screened too, because "
        "a suffix is not a surface; see the note below:",
        "",
        "| Verdict | Papers | What it means |",
        "|---|---:|---|",
    ]
    lines += [f"| `{name}` | {verdicts[name]} | {SENTINEL_MEANING[name]} |"
              for name in VERDICT_ORDER]
    lines += [
        "",
        f"🔴 **{suspect_pdf_only} of the {counts['pdf_only']} PDF-only papers cannot be read "
        "from their text layer at all**, and all of them should be acquired as XML/HTML rather "
        "than read from the PDF. A `clean` PDF is still a PDF: `deepdive_manifest` refuses it "
        "as a text surface, and a locator drawn from one has to be anchored to the page.",
        "",
    ]
    if census.text_dumps:
        lines += [
            "🔴 **Marked `text dump` below: markup wrapping a PDF text layer, not publisher "
            "markup.** These files carry an `.xml`/`.html` suffix and no JATS metadata, and "
            "their body sits inside a `<pre>` block. They are counted as PDF-only, because "
            "that is what they are — a suffix is not a surface. Files: "
            + ", ".join(f"`{name}`" for name in census.text_dumps) + ".",
            "",
        ]
    lines += [
        "### Per paper",
        "",
        "| Paper | Queue | Surface | Sentinel | Local surfaces |",
        "|---|---|---|---|---|",
    ]
    for paper in sorted(census.papers, key=order):
        verdict, detail = census.sentinel.get(paper.pmid, ("", ""))
        if not verdict:
            sentinel_cell = "—"
        elif detail:
            sentinel_cell = f"`{verdict}` — {cell(detail)}"
        else:
            sentinel_cell = f"`{verdict}`"
        surfaces = ", ".join(
            f"{name} *(text dump)*" if kind == "text_dump" else name
            for name, kind in paper.surfaces
        )
        lines.append(
            f"| PMID {paper.pmid} | {', '.join(paper.queue_ids) or '—'} "
            f"| `{paper.surface}` | {sentinel_cell} | {surfaces or '—'} |"
        )

    emitted = len(census.papers)
    rows_ok = emitted == census.corpus_papers + census.queued_papers - census.merged
    entries_ok = census.queue_entries == census.resolved_entries + len(census.losses)
    lines += [
        "",
        "### Loss ledger — queue entries this census cannot join to a local surface",
        "",
        "Not all of these are defects. An entry resolved by DOI alone says exactly what it is; "
        "the corpus is simply keyed by PMID, so there is nothing local to join it to. An entry "
        "declaring `NOT_AN_ARTICLE` will never have an identifier. Both are declared rather "
        "than dropped, because an entry missing from a derived surface and an entry with "
        "nothing to say look identical unless the difference is written down.",
        "",
        "| Entry | State | Identity line, verbatim |",
        "|---|---|---|",
    ]
    lines += [f"| {entry_id} | `{state}` | {cell(line)} |"
              for entry_id, state, line in census.losses]
    lines += [
        "",
        f"**Accounting.** Rows: {census.corpus_papers} corpus papers + {census.queued_papers} "
        f"queued papers − {census.merged} in both = **{emitted}** emitted. "
        + ("✓ " if rows_ok else "🔴 MISMATCH — ")
        + f"Entries: {census.resolved_entries} resolved + {len(census.losses)} unjoined = "
        f"**{census.queue_entries}** queue entries. "
        + ("✓" if entries_ok else "🔴 MISMATCH"),
        "",
        "*Not medical advice. This page describes file formats, not findings.*",
        "",
    ]
    return "\n".join(lines) + "\n"


# The per-entry annotation. One generated line inside each hand-written entry, so a session
# choosing what to read next sees the surface where it is deciding, not one file away.
#
# 🔴 This is safe where the census table was not, and the difference is exact: the line names
# only PMIDs the entry's own identity line already declares. It adds no paper to the queue, so
# it cannot turn a derived table into the declared reading debt `session_self_eval.py` counts.
# That was the whole defect, and it is why the corpus-wide table stays in its own file.
SURFACE_FIELD = re.compile(r"^\*\*Surface:\*\*.*\n", re.M)
# Exactly the field, not the prose that starts like it. Four entries carry lines such as
# `**Priorità rivista 2026-08-06:**` deep in their body; a looser pattern would drop the
# generated line into the middle of a narrative in whichever entry lost its `**Priority:**`.
PRIORITY_FIELD = re.compile(r"^\*\*(?:Priority|Priorità):\*\*", re.M)


def surface_note(body: str, census: Census) -> str:
    pmids, _dois, state = entry_identity(body)
    if state == "not_an_article":
        return "**Surface:** `n/a` — non è un articolo, non c'è superficie da censire.\n"
    if not pmids:
        return ("**Surface:** `unjoined` — la voce dichiara solo un DOI; il corpus locale è "
                "indicizzato per PMID, quindi non c'è nulla a cui agganciarla.\n")
    index = {paper.pmid: paper for paper in census.papers}
    parts = []
    for pmid in pmids:
        paper = index.get(pmid)
        if paper is None:
            parts.append(f"PMID {pmid} · `absent`")
            continue
        verdict = census.sentinel.get(pmid, ("", ""))[0]
        clause = f"PMID {pmid} · `{paper.surface}`"
        if verdict:
            clause += f" · sentinella `{verdict}`"
        files = ", ".join(name for name, _kind in paper.surfaces)
        parts.append(clause + (f" · {files}" if files else ""))
    return "**Surface:** " + "  ·  ".join(parts) + "\n"


def annotate(text: str, census: Census) -> str:
    """Rewrite the `**Surface:**` line of every FT entry, in place and idempotently.

    Everything else in the entry is copied byte for byte. The line goes immediately above
    `**Priority:**` where there is one — the queue's own reading order puts identity first,
    then what it costs to read, then why — and directly after the identity line otherwise.
    """
    matches = list(QUEUE_ENTRY.finditer(text))
    if not matches:
        return text
    out = []
    for _entry_id, body in queue_entries(text):
        body = SURFACE_FIELD.sub("", body)
        note = surface_note(body, census)
        priority = PRIORITY_FIELD.search(body)
        if priority:
            cut = priority.start()
        else:
            identity = IDENTITY_LINE.search(body)
            cut = identity.end() + 1 if identity else len(body)
        out.append(body[:cut] + note + body[cut:])
    # The bodies tile `text` from the first heading onward, so everything before it — the
    # queue's own title and Scope — is carried through untouched.
    return text[:matches[0].start()] + "".join(out)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--corpus", type=Path, default=None,
                        help="corpus directory (default: <root>/files/fulltext)")
    parser.add_argument("--out", type=Path, default=None,
                        help="write the census here instead of standard output")
    parser.add_argument("--annotate", action="store_true",
                        help="rewrite the **Surface:** line of every entry in the full-text "
                             "queue, in place and idempotently")
    parser.add_argument("--date", default=date.today().isoformat())
    arguments = parser.parse_args(argv)

    corpus_dir = arguments.corpus or (arguments.root / "files" / "fulltext")
    if not corpus_dir.is_dir():
        print(
            f"corpus directory not found: {corpus_dir}\n"
            "Refusing to emit a census: 'the corpus is not here' is not the same fact as "
            "'this paper has no local surface', and a census that confused them would report "
            "every paper as absent. Point --corpus at the checkout holding files/fulltext.",
            file=sys.stderr,
        )
        return 2

    census = build(arguments.root, corpus_dir, arguments.disease)
    if arguments.annotate:
        path = queue_file(arguments.root, arguments.disease)
        original = path.read_text(encoding="utf-8")
        path.write_text(annotate(original, census), encoding="utf-8")
        print(f"annotated {census.queue_entries} entries in {path.name}")
        if arguments.out is None:
            return 0

    page = render(census, arguments.date)
    if arguments.out is None:
        print(page, end="")
        return 0
    arguments.out.write_text(page, encoding="utf-8")
    print(f"surface census written to {arguments.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
