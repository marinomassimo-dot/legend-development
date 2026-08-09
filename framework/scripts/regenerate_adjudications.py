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
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ADJUDICATIONS = ROOT / "disease-models/wwox/research/page_adjudications"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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

        with fitz.open(pdf_path) as pdf:
            for artifact in recipe["artifacts"]:
                name = artifact["file"]
                image = render(pdf, artifact["page"], artifact["crop"], artifact["dpi"])
                produced = digest(image)
                declared = artifact.get("sha256")
                checked += 1

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
        print(f"\nFAILED — {len(failures)} of {checked} artifact(s):", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nOK: {checked} adjudication artifact(s) regenerate to their declared digest")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("action", nargs="?", default="verify", choices=("verify", "write"))
    parser.add_argument("--pmid", default=None, help="restrict to one study")
    arguments = parser.parse_args()
    return run(arguments.action, arguments.pmid)


if __name__ == "__main__":
    sys.exit(main())
