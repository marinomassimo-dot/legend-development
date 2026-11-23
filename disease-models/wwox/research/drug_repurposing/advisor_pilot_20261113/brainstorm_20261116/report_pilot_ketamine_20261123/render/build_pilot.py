"""ADV-201 rendering pilot: one printable ketamine brief built from a content file.

Usage: python3 build_pilot.py [--content pilot_stand_in.json] [--out out/ketamine_pilot_20261123.pdf]

PyMuPDF Story carries the text and tables; the evidence graph is drawn natively on its own page
(vector, text in the embedded report fonts). Nothing under framework/ or view/ is imported or
changed. matplotlib is not needed for this PDF; layout_test_figure.py shows the figure route.
"""
from __future__ import annotations

import argparse
import json
import sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "framework").is_dir())
OLD_JSON = REPO / "disease-models/wwox/research/drug_repurposing/view/research_reports/ketamine.json"
LIBS = Path.home() / ".local/legend-figures-libs"  # isolated fontTools / matplotlib, appended last

PAGE_W, PAGE_H = 595.28, 841.89
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 46, 44, 52

CSS = """
body{font-family:sans-serif;color:#161616;font-size:9.4pt;line-height:1.32;margin:0}
h1{font-family:serif;font-size:24pt;line-height:1.08;color:#000;margin:3pt 0 5pt}
h2{font-size:11.5pt;color:#000;margin:9pt 0 4pt}
h3{font-size:9.6pt;color:#000;margin:7pt 0 2pt}
p{margin:0 0 4pt}
a{color:#1a1a1a}
.meta{color:#333;font-size:8.4pt}
.tag{border:1.4pt solid #000;padding:5pt 8pt;margin:6pt 0;font-size:11pt}
.note{border:0.8pt solid #777;padding:4pt 7pt;margin:4pt 0;font-size:8.6pt}
.small{font-size:8.2pt;color:#222}
.guide{border-collapse:collapse;width:100%;margin:4pt 0 6pt}
.guide td{font-size:8.7pt;vertical-align:top;padding:3pt 4pt;border-bottom:0.6pt solid #888}
.dec{border-collapse:collapse;width:100%;margin:2pt 0 5pt}
.dec th{font-size:8pt;text-align:left;vertical-align:top;color:#000;border-top:1.4pt solid #000;border-bottom:1.4pt solid #000;padding:3pt 4pt}
.dec td{font-size:8.2pt;vertical-align:top;padding:3pt 4pt;border-bottom:0.6pt solid #888}
.c-DATA{border-left:4pt solid #000}
.c-INFERENCE{border-left:2pt solid #000}
.c-HYPOTHESIS{border-left:0.6pt solid #000}
.c-EXPERIMENT{border-left:4pt double #000}
.tbl{border-collapse:collapse;width:100%;margin:3pt 0 6pt}
.tbl th{font-size:8pt;text-align:left;vertical-align:top;color:#000;border-top:1.4pt solid #000;border-bottom:1.4pt solid #000;padding:3pt 4pt}
.tbl td{font-size:8.2pt;vertical-align:top;padding:3pt 4pt;border-bottom:0.6pt solid #888}
.sec{page-break-before:always}
.bib p{margin:0 0 5pt;font-size:8.6pt}
"""

TYPE_NOTE = {
    "DATA": "a value reported by a source",
    "INFERENCE": "a reading drawn from data; it is not itself a measurement",
    "HYPOTHESIS": "a claim not yet measured in the setting that matters",
    "EXPERIMENT": "a proposed measurement and what each outcome would mean",
}


def load_refs(content: dict):
    old = json.loads(OLD_JSON.read_text(encoding="utf-8"))
    pool = list(old["sources"]) + [s for c in old["chapters"] for s in c["sources"]]
    refs = {}
    for ref in content["references"]:
        hit = next((s for s in pool if ref["match"] in s["label"]), None)
        if hit is None:
            raise SystemExit(f"reference {ref['id']} ({ref['match']}) not found in {OLD_JSON.name}")
        refs[ref["id"]] = {**ref, "url": hit["url"], "source_label": hit["label"]}
    return refs, old


def ph(text: str) -> str:
    """Escape, and mark every PLACEHOLDER token so it cannot be missed on paper."""
    return escape(text).replace("PLACEHOLDER", "<b>[PLACEHOLDER]</b>")


def ref_cell(row_refs, refs) -> str:
    parts = []
    for rid, loc in row_refs:
        parts.append(f'<a href="{escape(refs[rid]["url"], quote=True)}">[{rid}]</a> {ph(loc)}')
    return "<br>".join(parts)


def decision_table(content: dict, refs: dict) -> str:
    """One table per evidence class: a class heading, its own column heads, no colspan rows
    (colspan group rows left stray background slivers in the Story output)."""
    head = ("<tr><th width='6%'>Row</th><th width='11%'>Type</th><th width='41%'>Statement</th>"
            "<th width='22%'>Model, endpoint</th><th width='20%'>Source, locator</th></tr>")
    out = []
    for group in content["groups"]:
        out.append(f'<h3>{escape(group["title"])}</h3><table class="dec">{head}')
        for row in group["rows"]:
            flags = ""
            if row.get("anchor"):
                flags += "<br><b>ANCHOR</b>"
            if row.get("rival"):
                flags += "<br><b>RIVAL</b>"
            out.append(
                f'<tr><td><b>{row["id"]}</b></td>'
                f'<td class="c-{row["type"]}"><b>{row["type"]}</b>{flags}</td>'
                f'<td>{ph(row["statement"])}</td><td>{ph(row["model"])}</td>'
                f'<td>{ref_cell(row["refs"], refs)}</td></tr>'
            )
        out.append("</table>")
    return "".join(out)


def html_front(content: dict, refs: dict) -> str:
    guide = "".join(f"<tr><td width='28%'><b>{escape(a)}</b></td><td>{ph(b)}</td></tr>"
                    for a, b in content["reading_guide"])
    types = "; ".join(f"<b>{k}</b> {v}" for k, v in TYPE_NOTE.items())
    return (
        '<p class="meta">LEGEND · WWOX / WOREE · RESEARCH BRIEF · PILOT FORMAT</p>'
        f'<h1>{escape(content["compound"])} in WWOX-related epilepsy</h1>'
        f'<div class="tag"><b>{escape(content["cover_tag"])}</b><br>'
        '<span class="small">Not medical advice. No dosing or treatment guidance. Evidence reviewed through '
        f'{escape(content["evidence_through"])}.</span></div>'
        f'<p class="note">{ph(content["status_line"])}</p>'
        f'<p><b>Bottom line.</b> {escape(content["bottom_line"])}</p>'
        f'<h2>Where to find what</h2><table class="guide">{guide}</table>'
        '<h2>Decision evidence</h2>'
        '<p class="small">Each row is one decision-bearing statement. Reference numbers link to the source and are '
        'listed once on the last page; a locator names the figure, table or section. Three evidence classes are kept '
        f'apart (A, B, C). Types: {types}.</p>'
        + decision_table(content, refs)
    )


def html_back(content: dict, refs: dict, old: dict) -> str:
    m = content["methods"]
    rows = "".join(f"<tr><td width='24%'><b>{escape(a)}</b></td><td>{ph(b)}</td></tr>" for a, b in m["corpus"])
    out = [
        '<h2>Methods and coverage</h2>',
        f'<table class="guide">{rows}</table>',
        '<h3>How statuses are assigned</h3>',
        "<p class='small'>A <b>DATA</b> row restates a value as the source reports it, with its setting. An <b>INFERENCE</b> "
        "row is a reading of data and carries the rows it rests on. A <b>HYPOTHESIS</b> has not been measured in the "
        "setting that matters. An <b>EXPERIMENT</b> row states the measurement and what each outcome would change. In the "
        "evidence graph, an edge is OBSERVED only when the link is supported by a reported measurement in a Wwox "
        "preparation, and HYPOTHESISED otherwise.</p>",
        f'<h3>Figure 2</h3><p class="small">{ph(m["figure2_reserved"])}</p>',
    ]
    a = content["appendix_a"]
    head = ("<tr><th width='6%'>Row</th><th width='20%'>Item</th><th width='40%'>What was reported</th>"
            "<th width='34%'>Boundary and what weakens it</th></tr>")
    body = []
    for chapter, idx, link in a["rows"]:
        r = old["chapters"][chapter - 1]["table"]["rows"][idx]
        body.append(f"<tr><td><b>{escape(link)}</b></td><td>{escape(r[0])}</td><td>{escape(r[1])}</td><td>{escape(r[2])}</td></tr>")
    out.append(f'<div><h2>{escape(a["title"])}</h2>'
               '<p class="small">Text is copied from the existing ketamine report; the row column points to the decision table.</p>'
               f'<table class="tbl">{head}{"".join(body)}</table></div>')
    b = content["appendix_b"]
    head = "<tr>" + "".join(f"<th width='{w}%'>{escape(c)}</th>" for c, w in zip(b["columns"], (22, 22, 48, 8))) + "</tr>"
    body = "".join("<tr>" + "".join(f"<td>{ph(c)}</td>" for c in row) + "</tr>" for row in b["rows"])
    out.append(f'<h2>{escape(b["title"])}</h2><table class="tbl">{head}{body}</table>')
    # bibliography
    locs: dict[int, list[str]] = {}
    for g in content["groups"]:
        for row in g["rows"]:
            for rid, loc in row["refs"]:
                locs.setdefault(rid, [])
                if loc not in locs[rid]:
                    locs[rid].append(loc)
    def entry(r):
        loc = "; ".join(locs.get(r["id"], []))
        extra = f" {escape(r['pmid_label'])}." if r.get("pmid_label") else ""
        acc = f" <b>Access:</b> {ph(r['access'])}" if r.get("access") else ""
        url = r["url"]
        shown = url if len(url) < 70 else url[:44] + "…/" + url.rsplit("/", 1)[-1]
        return (f'<p><b>[{r["id"]}]</b> {escape(r["short"])}.{extra} <b>Locators cited:</b> {ph(loc)}.{acc} '
                f'<a href="{escape(url, quote=True)}">{escape(shown)}</a></p>')
    prim = "".join(entry(r) for r in refs.values() if r["kind"] == "primary")
    leg = "".join(entry(r) for r in refs.values() if r["kind"] == "legend")
    out.append('<div class="sec bib"><h2>References</h2><h3>Primary literature</h3>' + prim +
               "<h3>LEGEND records</h3><p class='small'>Internal syntheses and audits of the literature above. "
               "They are not independent evidence and add no measurement of their own.</p>" + leg + "</div>")
    return "".join(out)


def story_doc(html: str):
    import pymupdf
    paper = pymupdf.paper_rect("a4")
    content = paper + (MARGIN_X, MARGIN_TOP, -MARGIN_X, -MARGIN_BOTTOM)
    story = pymupdf.Story(html=html, user_css=CSS)
    return story.write_with_links(lambda *_: (paper, content, None))


# ---------------------------------------------------------------------------- evidence graph
NODE_FILL = {"DATA": (1, 1, 1), "INFERENCE": (0.9, 0.9, 0.9), "HYPOTHESIS": (1, 1, 1), "EXPERIMENT": (0, 0, 0)}


def draw_node(page, rect, spec):
    import pymupdf
    kind, title, text, refs = spec
    fill = NODE_FILL[kind]
    shape = page.new_shape()
    shape.draw_rect(rect)
    shape.finish(color=(0, 0, 0), fill=fill, width=2.0 if kind == "DATA" else 1.1,
                 dashes="[4 3] 0" if kind == "HYPOTHESIS" else None)
    shape.commit()
    if kind == "HYPOTHESIS":  # light hatch so the class survives a greyscale photocopy
        hatch = page.new_shape()
        x = rect.x0 - rect.height
        while x < rect.x1:
            a, b = pymupdf.Point(max(x, rect.x0), rect.y1 - max(rect.x0 - x, 0)), pymupdf.Point(min(x + rect.height, rect.x1), rect.y0 + max(x + rect.height - rect.x1, 0))
            hatch.draw_line(a, b)
            x += 7
        hatch.finish(color=(0.82, 0.82, 0.82), width=0.5)
        hatch.commit()
        pad = rect + (4, 14, -4, -2)
        page.draw_rect(pad, color=None, fill=(1, 1, 1))
    ink = "#fff" if kind == "EXPERIMENT" else "#000"
    html = (f'<p style="margin:0;font-size:7.6pt"><b>{escape(kind)} · {escape(title)}</b></p>'
            f'<p style="margin:2pt 0 0;font-size:9pt">{escape(text)}</p>'
            f'<p style="margin:2pt 0 0;font-size:8pt">{escape(refs)}</p>')
    spare, _ = page.insert_htmlbox(rect + (5, 4, -5, -3), html, css=f"body{{color:{ink};font-family:sans-serif}}")
    if spare < 0:
        raise SystemExit(f"graph node {title!r} overflows its box; enlarge it")


def edge(page, a, b, status, label=None, label_at=0.5, label_dx=0, break_mark=False, break_at=0.5):
    import pymupdf
    pa, pb = pymupdf.Point(*a), pymupdf.Point(*b)
    shape = page.new_shape()
    shape.draw_line(pa, pb)
    shape.finish(color=(0, 0, 0), width=2.4 if status == "OBSERVED" else 1.2,
                 dashes=None if status == "OBSERVED" else "[5 3] 0")
    shape.commit()
    v = (pb - pa)
    n = v / abs(v)
    perp = pymupdf.Point(-n.y, n.x)
    tip = pb
    base = pb - n * 8
    head = page.new_shape()
    head.draw_polyline([tip, base + perp * 3.6, base - perp * 3.6, tip])
    head.finish(color=(0, 0, 0), fill=(0, 0, 0), width=0.5, closePath=True)
    head.commit()
    mid = pa + v * label_at
    if break_mark:
        bm = pa + v * break_at
        m = page.new_shape()
        for off in (-3.2, 3.2):
            c = bm + n * off
            m.draw_line(c + perp * 9 + n * 4, c - perp * 9 - n * 4)
        m.finish(color=(0, 0, 0), width=2.2)
        m.commit()
    if label:
        w = 6.0 * max(len(s) for s in label.split("\n")) * 0.78 + 8
        h = 9.4 * (label.count("\n") + 1) + 3
        box = pymupdf.Rect(mid.x - w / 2 + label_dx, mid.y - h / 2, mid.x + w / 2 + label_dx, mid.y + h / 2)
        page.draw_rect(box, color=None, fill=(1, 1, 1))
        spare, _ = page.insert_htmlbox(box + (1, 0, -1, 0), "<p style='margin:0;text-align:center;font-size:7.3pt'><b>" + escape(label).replace("\n", "<br>") + "</b></p>", css="body{color:#000;font-family:sans-serif}")
        if spare < 0:
            raise SystemExit(f"edge label {label!r} overflows")


def figure_page(doc, content: dict):
    import pymupdf
    page = doc.new_page(width=PAGE_W, height=PAGE_H)
    g = content["graph"]
    page.insert_htmlbox(pymupdf.Rect(MARGIN_X, MARGIN_TOP, PAGE_W - MARGIN_X, 96),
                        "<p class='meta' style='margin:0;font-size:8.4pt'>LEGEND · EVIDENCE GRAPH</p>"
                        "<h1 style='margin:2pt 0 0;font-family:serif;font-size:17pt'>Figure 1. Where the transfer from d-APV to ketamine breaks</h1>",
                        css="body{font-family:sans-serif;color:#000}")
    n1 = pymupdf.Rect(130, 112, 466, 170)
    n2 = pymupdf.Rect(130, 214, 466, 258)
    y3, h3 = 336, 100
    n3a = pymupdf.Rect(46, y3, 198, y3 + h3)
    n3b = pymupdf.Rect(222, y3, 374, y3 + h3)
    n4 = pymupdf.Rect(398, y3, 550, y3 + h3)
    n5 = pymupdf.Rect(110, 520, 486, 570)
    # edges first, nodes on top (labels sit on the line and interrupt it)
    edge(page, (298, 170), (298, 214), "OBSERVED", "OBSERVED", 0.5)
    edge(page, (190, 258), (122, y3), "OBSERVED", "OBSERVED\n(d-APV tested)", 0.5)
    edge(page, (298, 258), (298, y3), "HYPOTHESISED", "HYPOTHESISED", 0.83, break_mark=True, break_at=0.25)
    edge(page, (406, 258), (474, y3), "HYPOTHESISED", "HYPOTHESISED", 0.5)
    edge(page, (122, y3 + h3), (190, 520), "HYPOTHESISED", "HYPOTHESISED\n(reference arm)", 0.5)
    edge(page, (298, y3 + h3), (298, 520), "HYPOTHESISED", "HYPOTHESISED", 0.5)
    edge(page, (474, y3 + h3), (406, 520), "HYPOTHESISED", "HYPOTHESISED", 0.5)
    for r, key in ((n1, "n1"), (n2, "n2"), (n3a, "n3a"), (n3b, "n3b"), (n4, "n4"), (n5, "n5")):
        draw_node(page, r, g[key])
    # break annotation
    page.insert_htmlbox(pymupdf.Rect(312, 262, 398, 314),
                        "<p style='margin:0;font-size:7.8pt'><b>BREAK IN TRANSFER.</b> The slice result is for a competitive "
                        "antagonist. No pore blocker was tested in Wwox tissue.</p>", css="body{font-family:sans-serif;color:#000}")
    # key
    ky = 632
    page.draw_rect(pymupdf.Rect(MARGIN_X, ky, PAGE_W - MARGIN_X, ky + 150), color=(0, 0, 0), width=0.8)
    page.insert_htmlbox(pymupdf.Rect(MARGIN_X + 8, ky + 4, 300, ky + 20), "<p style='margin:0;font-size:9pt'><b>Key (does not depend on colour)</b></p>", css="body{font-family:sans-serif;color:#000}")
    def sample_line(y, status):
        s = page.new_shape()
        s.draw_line(pymupdf.Point(MARGIN_X + 10, y), pymupdf.Point(MARGIN_X + 62, y))
        s.finish(color=(0, 0, 0), width=2.4 if status == "OBSERVED" else 1.2, dashes=None if status == "OBSERVED" else "[5 3] 0")
        s.commit()
    sample_line(ky + 34, "OBSERVED")
    sample_line(ky + 56, "HYPOTHESISED")
    m = page.new_shape()
    for off in (-3, 3):
        m.draw_line(pymupdf.Point(MARGIN_X + 33 + off - 3, ky + 85), pymupdf.Point(MARGIN_X + 33 + off + 3, ky + 71))
    m.finish(color=(0, 0, 0), width=2.2)
    m.commit()
    texts = [
        (ky + 26, "<b>OBSERVED</b>: the link is supported by a reported measurement in a Wwox preparation (read within that one preparation)."),
        (ky + 48, "<b>HYPOTHESISED</b>: the link is proposed and has not been measured in Wwox tissue."),
        (ky + 70, "<b>Double bar</b>: the break in transfer; the evidence stops here."),
    ]
    for y, t in texts:
        page.insert_htmlbox(pymupdf.Rect(MARGIN_X + 74, y, PAGE_W - MARGIN_X - 6, y + 22), f"<p style='margin:0;font-size:8pt'>{t}</p>", css="body{font-family:sans-serif;color:#000}")
    # node swatches
    sx = MARGIN_X + 10
    for i, (kind, label) in enumerate((("DATA", "DATA: heavy outline"), ("INFERENCE", "INFERENCE: grey fill"), ("HYPOTHESIS", "HYPOTHESIS: dashed, hatched"), ("EXPERIMENT", "EXPERIMENT: black fill"))):
        r = pymupdf.Rect(sx + i * 122, ky + 96, sx + i * 122 + 112, ky + 118)
        draw_node(page, r, (kind, "", "", "")) if False else None
        s = page.new_shape()
        s.draw_rect(r)
        s.finish(color=(0, 0, 0), fill=NODE_FILL[kind], width=2.0 if kind == "DATA" else 1.1, dashes="[4 3] 0" if kind == "HYPOTHESIS" else None)
        s.commit()
        ink = "#fff" if kind == "EXPERIMENT" else "#000"
        bg = "" if kind != "HYPOTHESIS" else ""
        page.insert_htmlbox(r + (2, 2, -2, 0), f"<p style='margin:0;text-align:center;font-size:7.2pt'><b>{label}</b></p>", css=f"body{{font-family:sans-serif;color:{ink}}}")
    page.insert_htmlbox(pymupdf.Rect(MARGIN_X + 8, ky + 124, PAGE_W - MARGIN_X - 8, ky + 148),
                        "<p style='margin:0;font-size:7.8pt'>Reference numbers in brackets are in the list on the last page. Every statement drawn here "
                        "is a row of the decision table. The graph shows no dose, no pooled effect and no probability. "
                        "<b>Stand-in content: see the PLACEHOLDER marks in the table.</b></p>", css="body{font-family:sans-serif;color:#000}")
    return page


def build(content_path: Path, out: Path) -> Path:
    import pymupdf
    content = json.loads(content_path.read_text(encoding="utf-8"))
    refs, old = load_refs(content)
    front = story_doc(html_front(content, refs))
    back = story_doc(html_back(content, refs, old))
    doc = pymupdf.open()
    doc.insert_pdf(front)
    n_front = len(front)
    figure_page(doc, content)
    doc.insert_pdf(back)
    total = len(doc)
    footer = (f"AI-curated research brief for discussion with a clinical team · Not medical advice · PILOT, stand-in content")
    for page in doc:
        page.insert_htmlbox(pymupdf.Rect(MARGIN_X, PAGE_H - 36, PAGE_W - 110, PAGE_H - 14),
                            f"<p style='margin:0;font-size:7.4pt'>{escape(footer)}</p>", css="body{font-family:sans-serif;color:#222}")
        page.insert_htmlbox(pymupdf.Rect(PAGE_W - 110, PAGE_H - 36, PAGE_W - MARGIN_X, PAGE_H - 14),
                            f"<p style='margin:0;font-size:7.4pt;text-align:right'>{page.number + 1} / {total}</p>", css="body{font-family:sans-serif;color:#222}")
    sections = [("Decision evidence", 1), ("Figure 1. Evidence graph", n_front + 1)]
    for page in back:
        lines = [l.strip() for l in page.get_text().splitlines()]
        for key, name in (("Methods and coverage", "Methods and coverage"), ("Appendix A.", "Appendix A: negative and ambiguous results"),
                          ("Appendix B.", "Appendix B: quantitative details"), ("References", "References")):
            if any(l.startswith(key) for l in lines) and name not in [n for n, _ in sections]:
                sections.append((name, n_front + 1 + page.number + 1))
    doc.set_toc([[1, n, p] for n, p in sections])
    doc.set_metadata({"title": f"{content['compound']} in WWOX-related epilepsy (pilot format)", "author": "LEGEND",
                      "subject": content["cover_tag"], "keywords": "pilot; stand-in content; not medical advice"})
    doc.xref_set_key(doc.pdf_catalog(), "Lang", "(en)")
    sys.path.append(str(LIBS))  # last, so PyMuPDF and system packages keep priority
    try:
        doc.subset_fonts()
    except Exception as exc:  # subsetting only shrinks the file
        print("font subsetting skipped:", exc)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(doc.tobytes(garbage=4, deflate=True, no_new_id=True))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content", type=Path, default=HERE / "pilot_stand_in.json")
    ap.add_argument("--out", type=Path, default=HERE / "out/ketamine_pilot_20261123.pdf")
    args = ap.parse_args()
    print(build(args.content, args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
