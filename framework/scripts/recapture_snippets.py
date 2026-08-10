#!/usr/bin/env python3
"""Re-take a snippet from its artifact when normalisation, not the reader, moved the text.

🔴 WHY THIS IS COUPLED TO A TOOL FIX AND NOT A STANDING UTILITY
---------------------------------------------------------------
A repair inherits the correctness of the tool it was verified against. On 2026-08-10 the
extractor joined every text node with a space, so `<italic>WWOX</italic>‐DEE` came out as
`WWOX ‐DEE`; quotes re-taken from that output carry a space the author never wrote. They
verified when written and stopped verifying the moment the join was fixed — **correctly**,
because they had stopped being the author's characters.

Measured before the fix, and the prediction held to the entry: 38 of 54 snippets survived, 16
did not. On `PMID 32000863` the five carrying the fabricated space were exactly the five a
manifest note had recorded as repaired that morning — a set written down before the cause was
known, which is why the correlation is evidence rather than a search result.

So this ships with the join fix, in one commit. Separated, the re-capture becomes a debt that
looks settled, and a debt that looks settled is the kind nobody reopens.

HOW IT FINDS THE SPAN — no anchors, no heuristics
-------------------------------------------------
The earlier version of this repair guessed: longest unique leading fragment, then trailing,
then a window. It was wrong three times in one session, and each wrong answer was a plausible
span at a plausible length, which is the only dangerous kind.

None of that is needed here, because the defect is *invisible to the fold*. The folded key of
the recorded snippet and of the true span are identical — a space folds away — so the fold
locates the span exactly and the offset map cuts the authored characters back out.
`_quote_matches` already does both; this reuses them rather than re-deriving them.

Two refusals, and they are the whole safety argument:

  - the folded key must occur **exactly once** in the artifact. `_quote_matches` takes the
    first occurrence by design, which is safe for a verdict and unsafe for a repair: a
    sentence restated elsewhere with different punctuation would be copied in from the wrong
    place, and the result would verify;
  - the re-taken span must match `strict` afterwards. A repair that cannot be verified by the
    check that rejected the original is not a repair.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import deepdive_manifest as dm  # noqa: E402


def _edge(value: str, *, tail: bool) -> str:
    """The run of non-alphanumeric characters at one edge of a normalised quote."""
    characters = reversed(value) if tail else value
    out: list[str] = []
    for character in characters:
        if character.isalnum():
            break
        if not character.isspace():
            out.append(character)
    return "".join(reversed(out) if tail else out)


def _extend(text: str, start: int, end: int, snippet_normal: str) -> str:
    """Grow the folded span over edge punctuation the recorded quote also carried."""
    wanted_tail = _edge(snippet_normal, tail=True)
    while end < len(text) and wanted_tail:
        character = text[end]
        if character.isalnum() or character.isspace() or character not in wanted_tail:
            break
        wanted_tail = wanted_tail.replace(character, "", 1)
        end += 1
    wanted_head = _edge(snippet_normal, tail=False)
    while start > 0 and wanted_head:
        character = text[start - 1]
        if character.isalnum() or character.isspace() or character not in wanted_head:
            break
        wanted_head = wanted_head.replace(character, "", 1)
        start -= 1
    return text[start:end]


def retake(snippet: str, text: str) -> tuple[str | None, str]:
    """Return ``(span, reason)``. ``span`` is None when the re-capture is refused."""
    if dm._quote_matches(snippet, text)[1] == "strict":
        return None, "already strict"
    _normal, snippet_key, _offsets = dm._fold_with_offsets(snippet)
    text_normal, text_key, text_offsets = dm._fold_with_offsets(text)
    if not snippet_key:
        return None, "the snippet carries no alphanumeric content to locate on"
    occurrences = text_key.count(snippet_key)
    if occurrences == 0:
        return None, "the snippet's words do not occur in this artifact at all"
    if occurrences > 1:
        return None, (f"the snippet's words occur {occurrences} times; a repair may not "
                      f"choose between them")
    position = text_key.find(snippet_key)
    start = text_offsets[position]
    end = text_offsets[position + len(snippet_key) - 1] + 1
    # The fold's span runs from the first alphanumeric to the last, so a quote the author
    # closed with a bracket comes back open: `(Fig. 2A )` folds to a key ending at `2A`, and
    # the cut drops the `)` the source does contain. Extending over adjacent non-alphanumerics
    # that the recorded quote ALSO carried is not inventing — those characters are in the
    # source and were in the quote — while stopping at anything the quote did not have keeps
    # the repair from annexing the next clause.
    span = _extend(text_normal, start, end, dm._normalise_text(snippet))
    if dm._quote_matches(span, text)[1] != "strict":
        return None, "the re-taken span does not verify strictly, which should be impossible"
    return span, "re-taken"


def artifact_texts(root: Path, corpus: Path, manifest: dict) -> list[str]:
    texts: list[str] = []
    for entry in manifest.get("source_artifacts", []):
        if entry.get("kind") not in {"article_text", "supplement_text"}:
            continue
        relative = str(entry.get("path", ""))
        for candidate in (root / relative, corpus / Path(relative).name):
            if candidate.is_file():
                try:
                    body, _abstract = dm._artifact_text(candidate, "article_text")
                except Exception as exc:                           # noqa: BLE001
                    print(f"    ! {candidate.name}: {exc}")
                else:
                    texts.append(body)
                break
    return texts


def process(path: Path, root: Path, corpus: Path, write: bool) -> tuple[int, int]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    texts = artifact_texts(root, corpus, manifest)
    if not texts:
        return 0, 0
    retaken = refused = 0
    for index, entry in enumerate(manifest.get("verbatim_locators", {}).get("entries", [])):
        if entry.get("surface") not in dm.TEXT_SURFACES:
            continue
        snippet = str(entry.get("snippet", ""))
        best_span, best_reason = None, "no declared artifact holds it"
        for text in texts:
            span, reason = retake(snippet, text)
            if span is not None:
                best_span, best_reason = span, reason
                break
            if reason == "already strict":
                best_span, best_reason = None, reason
                break
            best_reason = reason
        if best_reason == "already strict":
            continue
        if best_span is None:
            refused += 1
            print(f"    !!! entries[{index}] REFUSED: {best_reason}")
            print(f"        {snippet[:110]}")
            continue
        retaken += 1
        print(f"    entries[{index}]  {len(snippet)} -> {len(best_span)} chars")
        print(f"      WAS: {snippet[:110]}")
        print(f"      NOW: {best_span[:110]}")
        entry["snippet"] = best_span
    if write and retaken:
        path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
                        encoding="utf-8")
        print(f"    WROTE {path.name}")
    return retaken, refused


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--corpus", default="")
    parser.add_argument("--pmid", default="")
    parser.add_argument("--write", action="store_true",
                        help="persist; without it nothing is written")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    corpus = Path(args.corpus) if args.corpus else root / "files" / "fulltext"
    directory = root / "disease-models" / args.disease / "research" / "deepdive_manifests"
    pattern = f"PMID{args.pmid}.json" if args.pmid else "PMID*.json"

    retaken = refused = 0
    for path in sorted(directory.glob(pattern)):
        print(f"{path.stem}")
        one, two = process(path, root, corpus, args.write)
        retaken += one
        refused += two
    print()
    print(f"{retaken} re-taken · {refused} refused")
    if not args.write:
        print("DRY RUN — pass --write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
