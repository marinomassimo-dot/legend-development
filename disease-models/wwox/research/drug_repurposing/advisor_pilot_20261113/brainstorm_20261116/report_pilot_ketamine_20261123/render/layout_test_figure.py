"""Layout test for a second quantitative figure: SYNTHETIC numbers, NOT DATA, never part of the brief.

It checks only that the figure route works: matplotlib 3.10.3 from the isolated folder
~/.local/legend-figures-libs is appended to sys.path inside this script (system packages keep
priority), the figure is written as a vector PDF with embedded TrueType fonts, and PyMuPDF places it
on an A4 page next to the report fonts. Run: python3 layout_test_figure.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.append(str(Path.home() / ".local/legend-figures-libs"))  # last: PyMuPDF keeps its own numpy path

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pymupdf  # noqa: E402

matplotlib.rcParams.update({"pdf.fonttype": 42, "font.family": "DejaVu Sans", "font.size": 8})


def make_figure(path: Path) -> None:
    fig, ax = plt.subplots(figsize=(6.6, 2.6))
    # Three settings are kept visibly distinct by marker, hatch and row, never pooled.
    rows = [("nominal bath concentration", "o", "SYNTHETIC", 1.0, 3.0, 9.0),
            ("total plasma, clinical setting", "s", "SYNTHETIC", 0.5, 1.2, 2.0),
            ("unbound exposure, animal setup", "^", "SYNTHETIC", 0.2, 0.6, 1.1)]
    for i, (label, marker, _, lo, mid, hi) in enumerate(rows):
        ax.plot([lo, hi], [i, i], color="black", lw=1.4)
        ax.plot([mid], [i], marker, color="white", mec="black", ms=7, mew=1.4)
    ax.set_yticks(range(3), [r[0] for r in rows])
    ax.set_xscale("log")
    ax.set_xlabel("exposure (unit as stated in the pack)")
    ax.set_title("LAYOUT TEST, SYNTHETIC VALUES, NOT DATA", fontsize=9, fontweight="bold")
    ax.grid(axis="x", color="0.8", lw=0.5)
    fig.tight_layout()
    fig.savefig(path, format="pdf")
    plt.close(fig)


def main() -> int:
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    fig_pdf = out / "layout_test_figure.pdf"
    make_figure(fig_pdf)
    doc = pymupdf.open()
    page = doc.new_page(width=595.28, height=841.89)
    page.insert_htmlbox(pymupdf.Rect(46, 44, 549, 100), "<p style='font-size:12pt'><b>Layout test only: not part of the brief and not data.</b></p>")
    src = pymupdf.open(fig_pdf)
    page.show_pdf_page(pymupdf.Rect(46, 110, 549, 110 + 503 * src[0].rect.height / src[0].rect.width), src, 0)
    doc.save(out / "layout_test_page.pdf", garbage=4, deflate=True)
    fonts = {(f[3], f[1]) for f in pymupdf.open(out / "layout_test_page.pdf")[0].get_fonts()}
    print("fonts on the test page:", sorted(fonts))
    print("vector paths on the page:", len(pymupdf.open(out / "layout_test_page.pdf")[0].get_drawings()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
