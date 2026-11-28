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

# Collapsed table backgrounds can be painted on following pages by MuPDF Story.
CSS = """
body{font-family:sans-serif;color:#20313d;font-size:10.3pt;line-height:1.36}
h1{font-family:serif;font-size:27pt;line-height:1.08;color:#153e54;margin:6pt 0 7pt}
h2{font-size:11.5pt;color:#153e54;margin:8pt 0 4pt}
p,li{margin:0 0 4pt}
a{color:#17587a}
.meta{color:#345d6d;font-size:9pt}
.notice{background:#eaf2f3;padding:5pt 8pt;margin:7pt 0}
.summary{font-size:11.4pt;color:#163e4b;margin:8pt 0}
.graph{border-collapse:separate;border-spacing:0;width:100%;margin:2pt 0 4pt;page-break-inside:avoid}
.node{font-size:9.5pt;vertical-align:top;padding:6pt;width:22%}
.node b{font-size:8.4pt}
.arrow{text-align:center;vertical-align:middle;width:4%;font-size:15pt;color:#496572}
.caption{font-size:8.4pt;color:#496572;margin:3pt 0 8pt}
.stage{border-left:3pt solid;padding:4pt 7pt;margin:5pt 0 0}
.sources{font-size:9.2pt;margin-top:4pt}
.chapter{page-break-before:always}
.chapter h2.title{font-family:serif;font-size:25pt;line-height:1.1;margin:5pt 0 8pt}
.chapter p{margin-bottom:7pt}
.comparison{border-collapse:separate;border-spacing:0;width:100%;margin:7pt 0 11pt}
.comparison th{font-size:9.5pt;vertical-align:top;text-align:left;color:#fff;background:#245467;padding:7pt}
.comparison td{font-size:9.5pt;vertical-align:top;background:#f0f5f5;padding:7pt;border-bottom:1pt solid #fff}
.contents{padding:6pt 9pt;background:#f1f4f7;color:#294b5d;font-size:9.2pt}
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
        sources = data["sources"] + [ref for chapter in data.get("chapters", []) for ref in chapter["sources"]]
        for ref in sources:
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


def source_list(sources: list[dict]) -> str:
    items = "".join(
        f'<li><a href="{escape(ref["url"], quote=True)}">{escape(ref["label"])}</a></li>'
        for ref in sources
    )
    return '<h2>Sources</h2><ol class="sources">' + items + "</ol>"


def chapter_html(number: int, chapter: dict) -> str:
    content = [
        f'<section class="chapter"><p class="meta">LEGEND · EVIDENCE DOSSIER · {number:02d}</p>',
        f'<h2 class="title">{escape(chapter["title"])}</h2>',
        f'<p class="summary">{escape(chapter["takeaway"])}</p>',
    ]
    if chapter.get("table"):
        headings = "".join(f"<th>{escape(text)}</th>" for text in chapter["table"]["columns"])
        rows = [
            "<tr>" + "".join(f"<td>{escape(text)}</td>" for text in row) + "</tr>"
            for row in chapter["table"]["rows"]
        ]
        content.append(f'<table class="comparison"><tr>{headings}</tr>{"".join(rows)}</table>')
    for section in chapter["sections"]:
        content.append(f'<h2>{escape(section["label"])}</h2>')
        content.extend(f"<p>{escape(paragraph)}</p>" for paragraph in section["paragraphs"])
    content.append(source_list(chapter["sources"]))
    content.append("</section>")
    return "".join(content)


def html_report(data: dict) -> str:
    content = [
        '<p class="meta">LEGEND · WWOX / WOREE · RESEARCH REPORT</p>',
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
    content.append(source_list(data["sources"]))
    chapters = data.get("chapters", [])
    if chapters:
        topics = " · ".join(f"{number:02d} {chapter['title']}" for number, chapter in enumerate(chapters, 1))
        content.append(f'<p class="contents"><b>In this report</b><br>{escape(topics)}</p>')
        content.extend(chapter_html(number, chapter) for number, chapter in enumerate(chapters, 1))
    return "".join(content)


def render_pdf(data: dict) -> bytes:
    import pymupdf

    paper = pymupdf.paper_rect("a4")
    content = paper + (48, 44, -48, -46)
    story = pymupdf.Story(html=html_report(data), user_css=CSS)
    document = story.write_with_links(lambda *_: (paper, content, None))
    try:
        document.set_metadata({"title": data["title"], "author": "LEGEND", "subject": DISCLAIMER})
        chapters = data.get("chapters", [])
        bookmarks = {f"LEGEND · EVIDENCE DOSSIER · {number:02d}": chapter["title"]
                     for number, chapter in enumerate(chapters, 1)}
        outline = [[1, data["title"], 1]]
        for page in document:
            first_line = page.get_text().splitlines()[0]
            if first_line in bookmarks:
                outline.append([1, bookmarks[first_line], page.number + 1])
            y = page.rect.height - 29
            page.draw_line((48, y - 10), (page.rect.width - 48, y - 10), color=(0.75, 0.82, 0.84), width=0.6)
            page.insert_text((48, y), "LEGEND  /  WWOX RESEARCH", fontsize=8, color=(0.21, 0.36, 0.42))
            page.insert_text((page.rect.width - 88, y), f"{page.number + 1}  /  {len(document)}", fontsize=8, color=(0.21, 0.36, 0.42))
        document.set_toc(outline)
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
