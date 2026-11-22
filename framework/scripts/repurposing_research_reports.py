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
STAGES = (
    ("Data / Evidence", "evidence", "#246465", "#e6f2ef"),
    ("Inference", "inference", "#2c5480", "#e9eff7"),
    ("Hypothesis", "hypothesis", "#694a82", "#f1ebf6"),
    ("Experiment", "experiment", "#82562a", "#faf0df"),
)

CSS = """
body{font-family:sans-serif;color:#20313d;font-size:10.3pt;line-height:1.36}
h1{font-family:serif;font-size:27pt;line-height:1.08;color:#153e54;margin:6pt 0 7pt}
h2{font-size:11.5pt;color:#153e54;margin:8pt 0 4pt}
p,li{margin:0 0 4pt}
a{color:#17587a}
.meta{color:#345d6d;font-size:9pt}
.notice{background:#eaf2f3;padding:5pt 8pt;margin:7pt 0}
.summary{font-size:11.4pt;color:#163e4b;margin:8pt 0}
.graph{border-collapse:collapse;width:100%;margin:2pt 0 4pt;page-break-inside:avoid}
.node{font-size:9.5pt;vertical-align:top;padding:6pt;width:22%}
.node b{font-size:8.4pt}
.arrow{text-align:center;vertical-align:middle;width:4%;font-size:15pt;color:#496572}
.caption{font-size:8.4pt;color:#496572;margin:3pt 0 8pt}
.stage{border-left:3pt solid;padding:4pt 7pt;margin:5pt 0 0}
.sources{font-size:8.8pt;margin-top:4pt}
"""


def entries(dr: Path):
    """The curated JSON is the index for rendering links and packaging the PDFs."""
    for source in sorted((dr / DIRECTORY).glob("*.json")):
        data = json.loads(source.read_text(encoding="utf-8"))
        if not re.fullmatch(BASENAME, source.stem) or not re.fullmatch(r"INV-\d{2}", data["investigation"]):
            raise ValueError(f"Invalid report slug or investigation in {source.name}")
        for label, key, _, _ in STAGES:
            if not data["graph"].get(key, "").strip() or not any(paragraph.strip() for paragraph in data.get(key, [])):
                raise ValueError(f"{source.name}: {label} needs a graph node and explanatory text")
        for ref in data["sources"]:
            url = urlsplit(ref["url"])
            if url.scheme != "https" or not url.hostname or url.username or url.password:
                raise ValueError(f"Expected a public HTTPS source in {source.name}")
        yield source.stem, data


def knowledge_graph(data: dict) -> str:
    nodes = [
        f'<td class="node" style="background:{tint}"><b style="color:{ink}">{label}</b><br>'
        f'{escape(data["graph"][key])}</td>'
        for label, key, ink, tint in STAGES
    ]
    arrow = '<td class="arrow">→</td>'
    return (
        '<h2>Knowledge graph</h2><table class="graph"><tr>'
        + arrow.join(nodes)
        + '</tr></table><p class="caption">Arrows show the reasoning from observations to a proposed test.</p>'
    )


def html_report(data: dict) -> str:
    content = [
        '<p class="meta">LEGEND · WWOX / WOREE · RESEARCH BRIEF</p>',
        f'<h1>{escape(data["title"])}</h1><p class="meta">Evidence reviewed through {escape(data["date"])}</p>',
        f'<div class="notice"><b>{DISCLAIMER}</b> This brief supports discussion with a qualified clinical team.</div>',
        f'<p class="summary">{escape(data["summary"])}</p>',
    ]
    content.append(knowledge_graph(data))
    for label, key, ink, tint in STAGES:
        content.append(f'<h2 class="stage" style="color:{ink};background:{tint}">{label}</h2>')
        content.extend(f"<p>{escape(paragraph)}</p>" for paragraph in data[key])
    content.append("<h2>Limits for WOREE</h2>")
    content.extend(f"<p>{escape(paragraph)}</p>" for paragraph in data["limits"])
    content.append('<h2>Sources</h2><ol class="sources">')
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
