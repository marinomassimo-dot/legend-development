#!/usr/bin/env python3
"""Do the quotations inside prose dossiers occur in a paper anybody can point at?

`locator_audit.py` reads manifests, and a manifest is the one place where a quote is bound to
a fingerprinted artifact. Dossiers are the other place the reading actually lands — the
narrative that explains what a locator means, written while the paper was open — and nothing
has ever looked at the quotations in them.

The hazard is not that a dossier lies. It is that a dossier is prose, so a quotation in one
carries no artifact, no surface and no fingerprint, and a reader has no way to check it
except by reopening the paper. When such a quotation is later promoted into a manifest, the
gate checks it. Until then it is load-bearing and unexamined.

WHAT THIS TOOL IS NOT
---------------------
It is not a gate, and it is deliberately not blocking. Two properties of real dossiers make
a pass/fail verdict meaningless here:

  - Typographic quotes are used BOTH to quote a paper AND to coin a phrase. `“tessuto di
    misura ≠ tessuto di necessità”` and `“half protein, normal brain”` are the author's own
    labels, and no pattern can tell them from a quotation without reading the sentence.
  - A dossier quotes OTHER papers on purpose. `PMID19500159.md` quotes PMID 17803050 by name,
    to record that a claim's own source does not license the word it uses. Scoring that as a
    defect would punish the most careful passage in the corpus.

So the tool sorts quotations into buckets and names what each one means. Reading the buckets
is the work; the exit code is not the verdict.

THE BUCKET THAT EARNS THE TOOL
------------------------------
`elsewhere` — the quotation is verbatim, and it is in a DIFFERENT paper than the dossier's.
That is either scrupulous cross-citation or a misattribution, and the difference is one line
of context away. Nothing else in this repository can tell you a quotation's true source; this
can, because the corpus is local and searchable.

`stitched` is the other one worth the run: a quotation joined by an ellipsis is a shape
`deepdive_manifest.validate` refuses BY NAME in a manifest, and dossiers are full of them.
Each is two verbatim spans whose join is not, and each will fail the day someone promotes it.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import deepdive_manifest as dm  # noqa: E402

# Curly quotes only. The first version of this probe also took backticked spans and drowned:
# in this corpus backticks mean IDENTIFIER — file paths, SHA-256 digests, `PREMISE:
# DEFAULT_FROM_TEXTBOOK` — and 122 of 207 candidate spans were of that kind. A shape that is
# wrong four times out of five is not a weak signal, it is a different signal.
CURLY = re.compile(r"“([^”]{25,900})”")
BLOCKQUOTE = re.compile(r"^>\s?(.*)$")
PMID_IN_NAME = re.compile(r"PMID(\d{6,9})")
ELLIPSIS = re.compile(r"…|\.\.\.")
DECORATION = re.compile(r"[*_]{1,2}")
MIN_QUOTE_CHARS = 25
TEXT_SUFFIXES = (".xml", ".html", ".txt")


def clean(span: str) -> str:
    """Strip markdown emphasis and the quotation marks an author wrapped around a blockquote.

    The dossiers write `> *"..."*` as often as `> ...`, and leaving the wrapper in place makes
    every one of those quotations fail against a source that never contained the wrapper.
    """
    return DECORATION.sub("", span).strip().strip("\"'“”").strip()


def blockquotes(raw: str) -> list[str]:
    """Consecutive `>` lines are ONE quotation.

    Treating each line separately splits every multi-line quote at the point the author's
    editor happened to wrap, which is the same defect — a span cut by layout rather than by
    meaning — that this repository already paid for once in snippet re-capture.
    """
    out: list[str] = []
    buffer: list[str] = []
    for line in raw.splitlines():
        match = BLOCKQUOTE.match(line)
        if match is not None:
            buffer.append(match.group(1))
        elif buffer:
            out.append(" ".join(buffer))
            buffer = []
    if buffer:
        out.append(" ".join(buffer))
    return out


def quotations(raw: str) -> list[str]:
    spans = [clean(span) for span in blockquotes(raw)]
    spans += [clean(span) for span in CURLY.findall(raw)]
    return [span for span in spans if len(span) >= MIN_QUOTE_CHARS]


def declared_text_artifacts(root: Path, disease: str, pmid: str) -> list[str]:
    """What the manifest SAYS this paper's text surfaces are — never a guess."""
    manifest = (root / "disease-models" / disease / "research" / "deepdive_manifests"
                / f"PMID{pmid}.json")
    if not manifest.is_file():
        return []
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return [str(entry.get("path", "")) for entry in data.get("source_artifacts", [])
            if entry.get("kind") in {"article_text", "supplement_text"}]


def resolve(root: Path, corpus: Path, relative: str) -> Path | None:
    for candidate in (root / relative, corpus / Path(relative).name):
        if candidate.is_file():
            return candidate
    return None


def read_text_surfaces(path: Path) -> list[str]:
    try:
        body, abstract = dm._artifact_text(path, "article_text")
    except Exception:                                              # noqa: BLE001
        return []
    return [text for text in (body, abstract) if text]


TAGS = re.compile(r"<[^>]+>")
WHITESPACE = re.compile(r"\s+")


def diagnostic_text(path: Path) -> str:
    """Raw text of a surface, WITHOUT the suspect screen. Never certifies anything.

    🔴 This exists because the screen and the search want opposite things, and conflating
    them cost a real answer. `_artifact_text` refuses a SUSPECT surface, which is exactly
    right when a quote is being CERTIFIED: a defective text layer must never make a locator
    look verified. But the `elsewhere` search is not certifying, it is ASKING WHERE A SENTENCE
    LIVES, and a refused surface answers that perfectly well.

    Found by running the tool: `PMID19500159.md` quotes a sentence that is verbatim in
    PMID 17803050's local HTML — plain `grep` finds it in a second — and the search reported
    `not found`, because 17803050 is precisely the paper whose only surface is a text dump the
    screen refuses. The tool was blind to the one answer it was built to give.

    So the rule is division of labour, not relaxation: this function may say WHERE, and it may
    never say VERIFIED. Nothing in this module writes a locator, records a receipt or clears a
    debt, which is what makes that safe to state rather than merely intend.
    """
    try:
        raw = path.read_bytes().decode("utf-8", errors="replace")
    except OSError:
        return ""
    if path.suffix.lower() in {".xml", ".html"}:
        raw = TAGS.sub(" ", raw)
    return WHITESPACE.sub(" ", raw)


def corpus_index(corpus: Path) -> dict[str, Path]:
    """Every readable text surface in the corpus, keyed by the PMID in its filename."""
    index: dict[str, Path] = {}
    if not corpus.is_dir():
        return index
    for path in sorted(corpus.iterdir()):
        if path.suffix.lower() not in TEXT_SUFFIXES or not path.is_file():
            continue
        found = PMID_IN_NAME.search(path.name)
        if found and found.group(1) not in index:
            index[found.group(1)] = path
    return index


def texts_for(root: Path, corpus: Path, disease: str, pmid: str,
              index: dict[str, Path]) -> list[str]:
    """Declared artifacts first; the corpus filename only when nothing is declared.

    The precedence is not a detail. `locator_audit` learned it by manufacturing a failure
    against a file the manifest never named, and the rule that came out of it — declared beats
    resolved — belongs anywhere a quote meets an artifact.
    """
    texts: list[str] = []
    for relative in declared_text_artifacts(root, disease, pmid):
        resolved = resolve(root, corpus, relative)
        if resolved is not None:
            texts.extend(read_text_surfaces(resolved))
    if texts:
        return texts
    fallback = index.get(pmid)
    return read_text_surfaces(fallback) if fallback is not None else []


def find_elsewhere(span: str, index: dict[str, Path], skip: str,
                   cache: dict[str, str]) -> str | None:
    """Which other paper in the corpus contains this sentence — diagnostically."""
    for pmid, path in index.items():
        if pmid == skip:
            continue
        if pmid not in cache:
            cache[pmid] = diagnostic_text(path)
        if dm._quote_matches(span, cache[pmid])[0]:
            return pmid
    return None


def audit(root: Path, corpus: Path, disease: str) -> dict:
    directory = root / "disease-models" / disease / "research" / "fulltext_dossiers"
    index = corpus_index(corpus)
    cache: dict[str, str] = {}
    results = []
    for path in sorted(directory.glob("*.md")):
        found = PMID_IN_NAME.search(path.name)
        if found is None:
            continue
        pmid = found.group(1)
        spans = quotations(path.read_text(encoding="utf-8"))
        own = texts_for(root, corpus, disease, pmid, index)
        entry = {"file": path.name, "pmid": pmid, "total": len(spans), "verbatim": 0,
                 "stitched": [], "elsewhere": [], "not_found": [], "undecidable": 0}
        if not own:
            entry["undecidable"] = len(spans)
            results.append(entry)
            continue
        for span in spans:
            if ELLIPSIS.search(span):
                entry["stitched"].append(span)
                continue
            if any(dm._quote_matches(span, text)[0] for text in own):
                entry["verbatim"] += 1
                continue
            other = find_elsewhere(span, index, pmid, cache)
            if other is not None:
                entry["elsewhere"].append((other, span))
            else:
                entry["not_found"].append(span)
        results.append(entry)
    return {"results": results}


SCOPE_NOTE = """
HOW TO READ THIS. `not_found` is NOT a defect count. Typographic quotes in these dossiers are
used both to quote a paper and to coin a phrase, and no pattern separates them — every
coinage lands in `not_found` and belongs there until a human reads it.

The two buckets that carry information are `elsewhere` and `stitched`.

`elsewhere` means the quotation is verbatim in a DIFFERENT paper. That is scrupulous
cross-citation as often as it is misattribution: `PMID19500159.md` quotes PMID 17803050 by
name, on purpose, to show that a claim's own source does not license the word it uses. Read
the sentence around it before calling it anything.

`stitched` means a quotation joined by an ellipsis: two verbatim spans whose join is not.
`deepdive_manifest.validate` refuses that shape by name in a manifest. In a dossier nothing
refuses it, so it survives until somebody promotes it — and then it fails, in a session that
did not write it.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--corpus", default="")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    corpus = Path(args.corpus) if args.corpus else root / "files" / "fulltext"
    report = audit(root, corpus, args.disease)

    totals = {"total": 0, "verbatim": 0, "stitched": 0, "elsewhere": 0, "not_found": 0,
              "undecidable": 0}
    for entry in report["results"]:
        totals["total"] += entry["total"]
        totals["verbatim"] += entry["verbatim"]
        totals["stitched"] += len(entry["stitched"])
        totals["elsewhere"] += len(entry["elsewhere"])
        totals["not_found"] += len(entry["not_found"])
        totals["undecidable"] += entry["undecidable"]
        if entry["undecidable"]:
            print(f"    {entry['file']:<40} {entry['total']:>3} quotation(s) — no readable "
                  f"text surface for this paper here")
            continue
        print(f"    {entry['file']:<40} {entry['total']:>3} quotation(s) · "
              f"{entry['verbatim']:>2} verbatim · {len(entry['stitched']):>2} stitched · "
              f"{len(entry['elsewhere']):>2} elsewhere · "
              f"{len(entry['not_found']):>2} not found")
        for span in entry["stitched"]:
            print(f"         [stitched] {span[:120]}")
        for other, span in entry["elsewhere"]:
            print(f"         [elsewhere → PMID {other}] {span[:100]}")
        for span in entry["not_found"]:
            print(f"         [not found] {span[:120]}")

    print()
    print(f"{totals['total']} quotation(s) across {len(report['results'])} dossier(s): "
          f"{totals['verbatim']} verbatim · {totals['stitched']} stitched · "
          f"{totals['elsewhere']} in another paper · {totals['not_found']} not found · "
          f"{totals['undecidable']} undecidable")
    if not totals["total"]:
        print("NOTHING AUDITED — a dossier set that cannot be read is not one with no defects")
    print(SCOPE_NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
