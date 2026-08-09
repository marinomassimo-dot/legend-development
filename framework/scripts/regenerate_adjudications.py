#!/usr/bin/env python3
"""Regenerate page-adjudication crops from the source PDF, and verify them by digest.

## Why the images are not in this repository

A page adjudication reproduces the author's printed characters — that is precisely what
makes it evidence, and precisely why it cannot be redistributed. `PMID 17803050` carries
`Copyright 2007 by the American Association for Laboratory Animal Science`, has no DOI, no
PMCID and no open deposit, and the crops cover substantial portions of the printed page.

So this repository publishes the **recipe**, not the reproduction: source PDF digest, page,
crop rectangle in PDF points, dpi, and the SHA-256 of the resulting image. A reader holding
their own copy of the PDF regenerates the identical bytes and verifies the digest. Nothing
is lost — the verification is exactly as strong — and nothing copyrighted is republished.

It is the same rule the rest of the state already follows: `files/` is gitignored while
every artifact in it is fingerprinted. Page adjudications were the one place doing the
opposite.

## Why each locator carries a needle

`adjudicates: ["entries[10]"]` is a promise: it asserts that a crop shows a locator without
giving anything a command can check. The needle is the search string that resolves the
locator to a span on the printed page, which closes the chain — **needle → span → span
inside crop → crop → digest** — and makes the whole recipe verifiable end to end rather than
by eye. Two conditions, both arithmetic once the needle exists:

- the needle occurs **exactly once** on its page. A fragment that matches twice does not
  identify a location; this repository learned that three times in one day;
- the needle is a fragment of the **snippet of the locator it names**, which is what stops a
  needle from drifting to a neighbouring sentence that happens to sit in the same crop.

Where a locator quotes a table row, the row is not contiguous in the text layer — the columns
are separate runs — so the needle is the row label, or the one cell value unique on the page.

## Usage

    regenerate_adjudications.py verify [--pmid 17803050]   # digests must match; default
    regenerate_adjudications.py write  [--pmid 17803050]   # (re)create the local images

`verify` is the gate: it fails closed when a digest disagrees, when the PDF is absent, or
when the PDF itself is not the one the recipe was taken from.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deepdive_manifest import _match_key, crop_contains_span  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ADJUDICATIONS = ROOT / "disease-models/wwox/research/page_adjudications"
LOCATOR = re.compile(r"^entries\[(\d+)\]$")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def snippets(recipe: dict) -> list[str] | None:
    """The quoted text of each locator, or None when the recipe names no manifest."""
    relative = recipe.get("manifest")
    if not relative:
        return None
    path = ROOT / relative
    if not path.exists():
        return None
    entries = json.loads(path.read_text(encoding="utf-8"))["verbatim_locators"]["entries"]
    return [str(entry.get("snippet", "")) for entry in entries]


def check_needles(page, artifact: dict, quoted: list[str] | None, label: str) -> list[str]:
    """Does each declared needle resolve, uniquely, to a span the crop actually shows?"""
    problems: list[str] = []
    crop = tuple(artifact["crop"])

    for adjudication in artifact["adjudicates"]:
        if not isinstance(adjudication, dict):
            problems.append(
                f"{label}: {adjudication!r} is a bare locator. Every adjudication declares "
                f"the needle that resolves it on the page, so the recipe can be checked "
                f"rather than believed")
            continue

        locator = str(adjudication.get("locator", ""))
        needle = str(adjudication.get("needle", ""))
        if not locator or not needle:
            problems.append(f"{label}: adjudication {adjudication!r} lacks locator or needle")
            continue

        hits = page.search_for(needle)
        if len(hits) != 1:
            problems.append(
                f"{label} {locator}: needle {needle!r} matches {len(hits)} span(s) on page "
                f"{artifact['page']}; a needle that is not unique does not identify a location")
            continue

        span = (hits[0].x0, hits[0].y0, hits[0].x1, hits[0].y1)
        if not crop_contains_span(crop, span):
            problems.append(
                f"{label} {locator}: crop {crop} does not contain the span "
                f"({span[0]:.0f},{span[1]:.0f},{span[2]:.0f},{span[3]:.0f}) it adjudicates")
            continue

        if quoted is None:
            continue
        match = LOCATOR.match(locator)
        if not match or int(match.group(1)) >= len(quoted):
            problems.append(f"{label} {locator}: no such locator in the manifest")
            continue
        # Folding to alphanumerics is the right strength here and the wrong strength for a
        # quote: it is asking whether the needle belongs to this locator, not whether the
        # page says what the snippet says. The crop answers that, by being read.
        if _match_key(needle) not in _match_key(quoted[int(match.group(1))]):
            problems.append(
                f"{label} {locator}: needle {needle!r} is not a fragment of the snippet it "
                f"claims to adjudicate")

    return problems


def recipes() -> list[tuple[Path, dict]]:
    found = []
    for path in sorted(ADJUDICATIONS.glob("*/adjudications.json")):
        found.append((path.parent, json.loads(path.read_text(encoding="utf-8"))))
    return found


def render(pdf, page_number: int, crop: list[float], dpi: int) -> bytes:
    import fitz  # noqa: PLC0415 — optional dependency, only needed to regenerate

    page = pdf[page_number - 1]
    pixmap = page.get_pixmap(clip=fitz.Rect(*crop), dpi=dpi)
    return pixmap.tobytes("png")


def run(action: str, only: str | None) -> int:
    try:
        import fitz  # noqa: F401, PLC0415
    except ImportError:
        print("PyMuPDF is required to regenerate adjudication crops: pip install pymupdf",
              file=sys.stderr)
        return 2

    import fitz  # noqa: PLC0415

    failures: list[str] = []
    checked = 0
    adjudicated = 0

    for directory, recipe in recipes():
        pmid = str(recipe.get("pmid", directory.name))
        if only and pmid != only:
            continue

        source = recipe["source_pdf"]
        pdf_path = ROOT / source["path"]
        if not pdf_path.exists():
            failures.append(
                f"{pmid}: source PDF absent at {source['path']}. The recipe cannot be run "
                f"without your own copy of the article; this repository does not ship it")
            continue
        actual = digest(pdf_path.read_bytes())
        if actual != source["sha256"]:
            failures.append(
                f"{pmid}: source PDF digest mismatch. Expected {source['sha256'][:16]}…, "
                f"found {actual[:16]}…. A different copy of the same article can carry a "
                f"different typesetting, and the crop rectangles are specific to this one")
            continue

        quoted = snippets(recipe)
        if quoted is None:
            print(f"  {pmid}: no manifest declared — needles verified for uniqueness and "
                  f"containment, but not against the locators they name")

        with fitz.open(pdf_path) as pdf:
            for artifact in recipe["artifacts"]:
                name = artifact["file"]
                image = render(pdf, artifact["page"], artifact["crop"], artifact["dpi"])
                produced = digest(image)
                declared = artifact.get("sha256")
                checked += 1
                adjudicated += len(artifact["adjudicates"])

                failures.extend(check_needles(pdf[artifact["page"] - 1], artifact, quoted,
                                              f"{pmid} {name}"))

                if action == "write":
                    (directory / name).write_bytes(image)

                if declared is None:
                    print(f"  {pmid} {name}: no digest declared, produced {produced}")
                elif produced != declared:
                    failures.append(
                        f"{pmid}: {name} regenerated to {produced[:16]}…, recipe declares "
                        f"{declared[:16]}…")
                else:
                    print(f"  {pmid} {name}: OK {produced[:16]}…")

    if failures:
        print(f"\nFAILED — {len(failures)} problem(s) across {checked} artifact(s):",
              file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nOK: {checked} adjudication artifact(s) regenerate to their declared digest, "
          f"and {adjudicated} locator(s) resolve to a span inside the crop that shows them")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("action", nargs="?", default="verify", choices=("verify", "write"))
    parser.add_argument("--pmid", default=None, help="restrict to one study")
    arguments = parser.parse_args()
    return run(arguments.action, arguments.pmid)


if __name__ == "__main__":
    sys.exit(main())
