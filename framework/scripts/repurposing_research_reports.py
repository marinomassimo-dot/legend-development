"""Build printable, source-linked PDFs for the public WWOX research dashboard."""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

DIRECTORY = "view/research_reports"
DISCLAIMER = "AI-curated research. Not medical advice."
BASENAME = r"[a-z0-9]+(?:-[a-z0-9]+)*"
SECTIONS = (
    ("What the evidence shows", "evidence"),
    ("What remains uncertain", "limits"),
    ("Research question", "research_question"),
)

CSS = """
body{font-family:sans-serif;color:#20313d;font-size:10.5pt;line-height:1.45}
h1{font-family:serif;font-size:28pt;line-height:1.12;color:#153e54;margin:7pt 0 10pt}
h2{font-size:12pt;color:#153e54;margin:14pt 0 4pt}
p,li{margin:0 0 6pt}
a{color:#17587a}
.meta{color:#345d6d;font-size:9pt}
.notice{background:#eaf2f3;padding:8pt 10pt;margin:10pt 0}
.summary{font-size:12pt;color:#163e4b;margin:12pt 0}
"""


def entries(dr: Path):
    """The curated JSON is the index for rendering links and packaging the PDFs."""
    for source in sorted((dr / DIRECTORY).glob("*.json")):
        data = json.loads(source.read_text(encoding="utf-8"))
        if not re.fullmatch(BASENAME, source.stem) or not re.fullmatch(r"INV-\d{2}", data["investigation"]):
            raise ValueError(f"Invalid report slug or investigation in {source.name}")
        for ref in data["sources"]:
            url = urlsplit(ref["url"])
            if url.scheme != "https" or not url.hostname or url.username or url.password:
                raise ValueError(f"Expected a public HTTPS source in {source.name}")
        yield source.stem, data


def html_report(data: dict) -> str:
    content = [
        '<p class="meta">LEGEND · WWOX / WOREE · RESEARCH BRIEF</p>',
        f'<h1>{escape(data["title"])}</h1><p class="meta">Evidence reviewed through {escape(data["date"])}</p>',
        f'<div class="notice"><b>{DISCLAIMER}</b> This brief supports discussion with a qualified clinical team.</div>',
        f'<p class="summary">{escape(data["summary"])}</p>',
    ]
    for heading, key in SECTIONS:
        content.append(f"<h2>{heading}</h2>")
        content.extend(f"<p>{escape(paragraph)}</p>" for paragraph in data[key])
    content.append("<h2>Sources</h2><ol>")
    for ref in data["sources"]:
        content.append(f'<li><a href="{escape(ref["url"], quote=True)}">{escape(ref["label"])}</a></li>')
    return "".join(content) + "</ol>"


def render_pdf(data: dict) -> bytes:
    import pymupdf

    paper = pymupdf.paper_rect("a4")
    content = paper + (48, 44, -48, -46)
    story = pymupdf.Story(html=html_report(data), user_css=CSS)
    document = story.write_with_links(lambda *_: (paper, content, None))
    try:
        document.set_metadata({"title": data["title"], "author": "LEGEND", "subject": DISCLAIMER})
        return document.tobytes(garbage=4, deflate=True, no_new_id=True)
    finally:
        document.close()


def main(argv=None):
    from repurposing_view import DEFAULT_DR

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dr", type=Path, default=DEFAULT_DR)
    parser.add_argument("--check", action="store_true", help="check the committed PDFs against the sources")
    args = parser.parse_args(argv)
    stale = []
    for slug, data in entries(args.dr):
        path = args.dr / DIRECTORY / f"{slug}.pdf"
        pdf = render_pdf(data)
        if args.check:
            if not path.is_file() or path.read_bytes() != pdf:
                stale.append(slug)
        else:
            path.write_bytes(pdf)
            print(path)
    if stale:
        print("Stale report PDFs: " + ", ".join(stale))
    return int(bool(stale))


if __name__ == "__main__":
    raise SystemExit(main())
