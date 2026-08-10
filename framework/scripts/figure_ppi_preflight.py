#!/usr/bin/env python3
"""Inventory a PDF's raster information ceiling before rendering pages.

The effective PPI is the native pixel dimension divided by the placed size on the
PDF page.  Vector-only pages have no raster ceiling and are reported separately.
This is a preflight tool: it never renders or modifies the source.
"""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path

import fitz


def inventory(pdf_path: Path) -> dict:
    document = fitz.open(pdf_path)
    pages = []
    for number, page in enumerate(document, 1):
        images = []
        for image in page.get_image_info(xrefs=True):
            x0, y0, x1, y1 = image["bbox"]
            placed_width = abs(x1 - x0)
            placed_height = abs(y1 - y0)
            if not placed_width or not placed_height:
                continue
            ppi_x = image["width"] * 72.0 / placed_width
            ppi_y = image["height"] * 72.0 / placed_height
            images.append(
                {
                    "xref": image.get("xref", 0),
                    "pixels": [image["width"], image["height"]],
                    "effective_ppi_x": round(ppi_x, 1),
                    "effective_ppi_y": round(ppi_y, 1),
                    "effective_ppi_ceiling": round(min(ppi_x, ppi_y), 1),
                }
            )
        ceilings = [item["effective_ppi_ceiling"] for item in images]
        pages.append(
            {
                "page": number,
                "raster_images": images,
                "raster_ceiling": None
                if not ceilings
                else {
                    "minimum": round(min(ceilings), 1),
                    "median": round(statistics.median(ceilings), 1),
                    "maximum": round(max(ceilings), 1),
                },
                "note": "vector_or_text_only" if not ceilings else "measured_before_render",
            }
        )
    return {"source": str(pdf_path), "page_count": len(document), "pages": pages}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()
    result = inventory(args.pdf)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['source']}: {result['page_count']} pages")
        for page in result["pages"]:
            ceiling = page["raster_ceiling"]
            if ceiling is None:
                print(f"page {page['page']}: vector/text only; no raster PPI ceiling")
            else:
                print(
                    f"page {page['page']}: {len(page['raster_images'])} raster image(s); "
                    f"effective PPI min/median/max "
                    f"{ceiling['minimum']}/{ceiling['median']}/{ceiling['maximum']}"
                )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
