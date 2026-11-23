"""ADV-201 increment 2: the ketamine brief built from SCI's content pack (../content/), not from the stand-in.

Usage: python3 -I build_final.py --landed <main sha> [--out out/ketamine_brief_pilot_final.pdf]

Reads A to F of the pack (markdown tables and the two graph TSVs), draws the evidence graph on a landscape
page, and stamps the PDF with the content commit, the main commit that carries it and the SHA-256 of every
input file (last page, page footers, PDF keywords), so a cold reader can say which input it read. Reuses the
Story helpers of build_pilot.py. Nothing outside this folder is read or written except `git` queries.

Layout rules this builder adds on top of pymupdf's Story (which repeats no table header and cannot keep a
heading with its table):
 * a table that continues on the next page gets its header row there (found by asking Story where every row landed; a spacer row keeps
   the copy from stranding at a page foot; layout is repeated until nothing moves);
 * a heading is kept with its table the same way (Story ignores page-break-before and loops on it);
 * every table is followed by a 1 pt spacer: a heading placed straight after a table made Story loop for
   ever once SCI's corrected rows moved a page break (2026-11-23);
 * the graph layout is fixed per node id: an unknown node, kind, edge or status stops the build with a message.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from html import escape, unescape
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_pilot as bp  # noqa: E402  (CSS, margins)

CONTENT = HERE.parent / "content"
INPUTS = ["00_README_CONTENT_PACK.md", "A_decision_evidence.md", "B_references.md", "C_methods_and_coverage.md", "D_negative_and_quantitative.md",
          "E_evidence_graph_nodes.tsv", "E_evidence_graph_edges.tsv", "E_evidence_graph_spec.md",
          "F_deciding_measurement.md", "VERIFICATION_LEDGER_ADV200.tsv"]

CSS_FINAL = bp.CSS + """
.tbl td{font-size:8pt;line-height:1.22;padding:2.2pt 4pt}
.tbl td b{font-size:8pt}
.wide td b{font-size:7.2pt}
.small b{font-size:8.2pt}
.guide td b{font-size:8.7pt}
.wide td{font-size:7.2pt;line-height:1.17;padding:1.1pt 4pt}
.wide th{font-size:7.4pt}
.absrow{border-left:5pt solid #000}
.status{font-size:7.4pt;font-weight:bold}
ul{margin:0 0 4pt 0;padding-left:12pt}
li{margin:0 0 3pt 0;font-size:8.8pt}
.prov td{font-size:7.4pt;font-family:monospace}
"""

# ---------------------------------------------------------------------------- typography
_TYPO = [(re.compile(r"\+/-"), "\u00b1"),            # +/- -> plus-minus sign
         (re.compile(r"\buM\b"), "\u00b5M"),          # uM -> micro sign + M
         (re.compile(r"(\d) C\b"), "\\1 \u00b0C")]    # 35 C -> 35 degree C


def typo(text: str) -> str:
    for rx, rep in _TYPO:
        text = rx.sub(rep, text)
    return text


def esc(text: str) -> str:
    return typo(escape(text))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------- markdown reading
def inline(text: str) -> str:
    """Escape, then turn **bold** into <b>; nothing else is interpreted."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(text.strip()))


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_md(path: Path):
    """-> sections [{level, title, lines (outside tables), tables [{header, rows}]}]."""
    sections = [{"level": 1, "title": "", "lines": [], "tables": []}]
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(#{1,3}) (.*)", line)
        if m:
            sections.append({"level": len(m.group(1)), "title": m.group(2).strip(), "lines": [], "tables": []})
        elif line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|\s*$", lines[i + 1]):
            header = split_row(line)
            rows = []
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            sections[-1]["tables"].append({"header": header, "rows": rows})
            continue
        elif line.strip():
            sections[-1]["lines"].append(line)
        i += 1
    return sections


def find(sections, start: str):
    return next(s for s in sections if s["title"].startswith(start))


def paragraphs_html(lines: list[str]) -> str:
    if lines:  # text between a heading and a table: the heading is not "straight before" the table (an empty section is not text)
        _STATE["pending"] = []
    out, bullets = [], []

    def flush():
        nonlocal bullets
        if bullets:
            out.append("<ul>" + "".join(f"<li>{inline(b)}</li>" for b in bullets) + "</ul>")
            bullets = []
    for line in lines:
        if line.lstrip().startswith(("* ", "- ")):
            bullets.append(line.lstrip()[2:])
        elif re.match(r"^\d+\. ", line.strip()):
            flush()
            out.append(f'<p style="margin:0 0 3pt 14pt;text-indent:-14pt">{inline(line.strip())}</p>')
        else:
            flush()
            out.append(f"<p>{inline(line)}</p>")
    flush()
    return "".join(out)


# ---------------------------------------------------------------------------- tables (with repeated headers)
WIDTH_HINT = {"#": 4, "Stage": 4, "Status": 10, "Ref": 6, "Locator": 14, "No.": 3, "PMID": 7, "DOI": 12, "Unit": 6,
              "Assay or source": 20, "Value as printed": 19, "Spread as the source gives it": 13,
              "Exposure definition": 12, "Edge": 6, "From to": 9, "Relation": 12, "Source": 20}
_STATE = {"n": 0, "h": 0, "copies": set(), "pads": {}, "pending": [], "pairs": []}  # table counter within one layout pass; header copies chosen by the last pass


HEAD_MARGIN = {"h1": 3, "h2": 9, "h3": 7}


def hd(tag: str, text: str, style: str = "") -> str:
    """A heading that stays with the table that follows it: if Story strands it at a page foot, the next pass puts a spacer before it."""
    _STATE["h"] += 1
    hid = f"h{_STATE['h']}"
    _STATE["pending"].append(hid)
    pad = _STATE["pads"].get(f"p_{hid}")
    brk = f'<div id="p_{hid}" style="height:{pad:.1f}pt"></div>' if pad else ""
    return f'{brk}<{tag} id="{hid}"{f" style={chr(34)}{style}{chr(34)}" if style else ""}>{esc(text)}</{tag}>'


def cell_html(header: str, text: str) -> str:
    if header == "Status":
        if text.startswith("ABSTRACT-ONLY"):
            return f'<td class="status">[{inline(text)}]</td>'
        return f'<td class="status">{inline(text)}</td>'
    return f"<td>{inline(text)}</td>"


def table_html(tbl: dict, wide: bool = False, link_pmid: bool = False) -> str:
    _STATE["n"] += 1
    tid = f"t{_STATE['n']}"
    for hid in _STATE["pending"]:  # every heading since the last text belongs with this table
        _STATE["pairs"].append((hid, tid))
    _STATE["pending"] = []
    hdr = tbl["header"]
    n = len(hdr)
    fixed = {k: WIDTH_HINT.get(h) for k, h in enumerate(hdr) if WIDTH_HINT.get(h)}
    free = [k for k in range(n) if k not in fixed]
    rest = max(100 - sum(fixed.values()), 20)
    widths = [fixed.get(k, rest // max(len(free), 1)) for k in range(n)]
    scale = 100 / sum(widths)
    widths = [round(w * scale, 1) for w in widths]
    cls = "tbl" + (" wide" if wide else "")
    ths = "".join(f"<th width='{w}%'>{esc(h.replace('**', ''))}</th>" for h, w in zip(hdr, widths))
    body = []
    for k, row in enumerate(tbl["rows"]):
        row = row + [""] * (n - len(row))
        cells = []
        is_abs = "Status" in hdr and row[hdr.index("Status")].startswith("ABSTRACT-ONLY")
        for h, c in zip(hdr, row):
            if link_pmid and h == "PMID" and c.isdigit():
                cells.append(f'<td><a href="https://pubmed.ncbi.nlm.nih.gov/{c}/">{c}</a></td>')
            elif link_pmid and h == "DOI" and c.startswith("10."):
                cells.append(f'<td><a href="https://doi.org/{escape(c, quote=True)}">{escape(c)}</a></td>')
            else:
                cells.append(cell_html(h, c))
        if is_abs:  # heavy bar at the row's left edge: reproduced from the abstract, not the full text
            cells[0] = cells[0].replace("<td", '<td class="absrow"', 1)
        # a continuation page: repeat the header row; if Story would strand that copy at the page foot, a spacer row fills the page first
        pad = _STATE["pads"].get(f"p_{tid}_{k}")
        padrow = f'<tr id="p_{tid}_{k}"><td colspan="{n}" style="height:{pad:.1f}pt;padding:0;border:0"></td></tr>' if pad else ""
        copy = f'{padrow}<tr id="c_{tid}_{k}">{ths}</tr>' if f"{tid}_{k}" in _STATE["copies"] else ""
        body.append(f'{copy}<tr id="{tid}_{k}">' + "".join(cells) + "</tr>")
    return (f'<table class="{cls}"><tr id="{tid}_h">{ths}</tr>{"".join(body)}</table>'
            '<div style="height:1pt"></div>')


def _paper(landscape):
    import pymupdf
    paper = pymupdf.paper_rect("a4-l" if landscape else "a4")
    return paper, paper + (bp.MARGIN_X, bp.MARGIN_TOP, -bp.MARGIN_X, -bp.MARGIN_BOTTOM)


def _guarded(paper, rect):
    count = [0]

    def where(n, filled, **_):  # fail fast if a block cannot fit on a page (Story would otherwise loop for ever)
        count[0] += 1
        if count[0] > 25:
            raise SystemExit("Story did not finish in 25 pages: a table row or block is taller than the page")
        return paper, rect, None
    return where


def _positions(html, landscape):
    import pymupdf
    paper, rect = _paper(landscape)
    story = pymupdf.Story(html=html, user_css=CSS_FINAL)
    seen = {}

    def posfn(p):
        if p.open_close & 1 and p.id and p.id not in seen:
            seen[p.id] = (p.page_num, p.rect)
    writer = pymupdf.DocumentWriter(io.BytesIO())
    story.write(writer, _guarded(paper, rect), posfn)
    writer.close()
    return seen


def story_doc(builder, landscape: bool):
    """Lay out builder() with a header copy on every continuation page of every table; returns a Document."""
    import pymupdf
    paper, rect = _paper(landscape)
    copies: set[str] = set()
    pads: dict[str, float] = {}
    for _ in range(12):
        _STATE.update(n=0, h=0, copies=copies, pads=pads, pending=[], pairs=[])
        html = builder()
        info = _positions(html, landscape)
        pages = {k: v[0] for k, v in info.items()}
        rows = defaultdict(dict)
        for ident, pg in pages.items():
            m = re.fullmatch(r"(t\d+)_(\d+)", ident)
            if m:
                rows[m.group(1)][int(m.group(2))] = pg
        need = {f"{tid}_{k}" for tid, d in rows.items() for k in sorted(d) if k > 0 and d[k] != d[k - 1]}
        new_pads = dict(pads)
        for cid in need:  # a header copy stranded at a page foot while its row starts the next page
            c = f"c_{cid}"
            if c in pages and pages[c] != pages[cid]:
                if f"p_{cid}" in pads:
                    raise SystemExit(f"header copy {c} is still stranded after a spacer; reflow the table")
                new_pads[f"p_{cid}"] = rect.y1 - info[c][1][1] - 5
        for hid, tid in _STATE["pairs"]:  # a heading left at a page foot while its table starts on the next page
            first = pages.get(f"{tid}_0", pages[f"{tid}_h"])
            if pages[hid] != first and f"p_{hid}" not in pads:
                tag = re.search(rf'<(h[123]) id="{hid}"', html).group(1)
                new_pads[f"p_{hid}"] = rect.y1 - (info[hid][1][1] - HEAD_MARGIN[tag]) - 5  # a spacer that fills the page to within 1 pt makes Story drop everything after it
        if need == copies and new_pads == pads:
            break
        copies, pads = need, new_pads
    else:
        raise SystemExit("table header copies and spacers did not settle in 12 passes")
    story = pymupdf.Story(html=html, user_css=CSS_FINAL)
    doc = story.write_with_links(_guarded(paper, rect))
    while len(doc) > 1 and not doc[len(doc) - 1].get_text().strip():  # a spacer after a table that ends at the page foot spills onto an empty last page
        doc.delete_page(len(doc) - 1)
    # completeness: the end of the text that went in must be in the document that came out (Story can drop content silently)
    plain = _norm(unescape(re.sub(r"<[^>]+>", " ", html))).strip()
    words = [w for w in plain[-300:].split() if len(w) > 4][-12:]  # table cells come out in column order, so test words, not a phrase
    got = _norm("\n".join(p.get_text() for p in doc))
    missing = [w for w in words if w not in got]
    if missing:
        raise SystemExit(f"Story dropped the end of the text (missing {missing}); check the spacers")
    return doc


# ---------------------------------------------------------------------------- section builders
def display_title(t: str) -> str:
    """The pack refers to sections by title, not by letter: drop a leading 'A. ' and the long tail after a colon where asked."""
    return re.sub(r"^[A-F]\. ", "", t)


def file_head(secs, size="19pt", margin="0"):
    """Level-1 title and the intro lines of one pack file (the lines between the title and the first section).
    The title joins the heading chain kept with the next table; the intro lines do not break the chain."""
    top = next(s for s in secs if s["level"] == 1 and s["title"])
    return (hd("h1", display_title(top["title"]), f"font-size:{size};margin-top:{margin}")
            + "".join(f'<p class="small">{inline(l)}</p>' for l in top["lines"]))


def sections_html(secs, wide=False, skip=(), special=None):
    """Every level-2 section of a file in its own order: heading kept with its table, paragraphs, tables."""
    out = []
    for s in secs:
        if s["level"] != 2 or s["title"] in skip:
            continue
        if special and s["title"].startswith(special[0]):
            out.append(special[1](s))
        else:
            out.append(hd("h2", s["title"]) + paragraphs_html(s["lines"]) + "".join(table_html(t, wide=wide) for t in s["tables"]))
    return "".join(out)


ORDER_TEXT = ("Decision evidence, from p. {A}. The deciding measurement, from p. {F}. Figure 1 (evidence graph), p. {G}, and its edge list, p. {E}. "
              "Negative and ambiguous results and the quantitative details, from p. {D}. Methods and coverage, then References and build provenance, from p. {M}.")


def front_html(A, pagemap):
    order = ORDER_TEXT.format(**(pagemap or {k: "?" for k in "AGEFDM"}))
    out = [
        '<p class="meta">LEGEND · WWOX / WOREE · RESEARCH BRIEF · PILOT, FINAL CONTENT</p>',
        "<h1>Ketamine in WWOX-related epilepsy</h1>",
        '<div class="tag"><b>AI-curated research brief for discussion with a clinical team</b><br>'
        '<span class="small">Hypothesis level. Not medical advice. No dose, schedule or recommendation. Reference genotype class only.</span></div>',
        f'<p class="note"><b>Page order.</b> {esc(order)}<br>'
        '<b>In the tables, a heavy bar at the left edge of a row and the mark [ABSTRACT-ONLY] mean that the row was reproduced from the PubMed abstract and not from the full text.</b></p>',
        file_head(A, "17pt", "6pt"),
        sections_html(A),
    ]
    return "".join(out)


def f_html(F):
    return file_head(F, "19pt", "14pt") + sections_html(F)


def edge_list_html(edges):
    hdr = ["Edge", "From to", "Relation", "What the link says", "Status", "Source"]
    rows = [[e["edge_id"], f"{e['from']} to {e['to']}", e["relation"].replace("_", " "), re.sub(r"\s*\(draw lightly\)", "", e["label"]), e["status"], e["source"]] for e in edges]  # the pack's drawing hint is not reader text
    return ('<h1 style="font-size:17pt">Figure 1: edge list</h1>'
            '<p class="small">Each line of the graph on the previous page, with its relation, status and source.</p>'
            + table_html({"header": hdr, "rows": rows}, wide=True))


def _matrices(s):
    out = [hd("h2", s["title"]) + paragraphs_html(s["lines"])]
    t = s["tables"][0]
    hdr = t["header"]
    defi = hdr.index("Exposure definition")
    groups = {"Nominal bath concentration (applied to a preparation; no plasma protein)": lambda d: d.startswith("bath"),
              "Total plasma (measured in blood plasma)": lambda d: d.startswith("plasma"),
              "Cerebrospinal fluid (lumbar)": lambda d: d.startswith("CSF")}
    used = set()
    for title, pred in groups.items():
        rows = [r for r in t["rows"] if pred(r[defi])]
        used.update(id(r) for r in rows)
        out.append(hd("h3", f"Matrix: {title}") + table_html({"header": hdr, "rows": rows}, wide=True))
    rest = [r for r in t["rows"] if id(r) not in used]
    if rest:
        out.append(hd("h3", "Other") + table_html({"header": hdr, "rows": rest}, wide=True))
    return "".join(out)


def d_html(D):
    return file_head(D) + sections_html(D, wide=True, special=("Quantitative details", _matrices))


def back_html(B, C, provenance_rows, commit, landed=""):
    refs = next(s for s in B if s["tables"])
    out = [file_head(C), sections_html(C)]
    out.append(file_head(B, "19pt", "12pt").replace("</p>", "</p>", 1)
               + table_html(refs["tables"][0], wide=True, link_pmid=True)
               + sections_html(B, skip=(refs["title"],)))
    prow = [[n, h] for n, h in provenance_rows]
    out.append(hd("h2", "Build provenance (for the project team)")
               + f"<p class='small'>Content commit: <b>{esc(commit)}</b> (last commit touching the content folder)." + (f" Landed on main as <b>{esc(landed)}</b>." if landed else "")
               + " Input files and the SHA-256 of each:</p>"
               + table_html({"header": ["File", "SHA-256"], "rows": prow}, wide=False).replace('class="tbl"', 'class="tbl prov"'))
    return "".join(out)


# ---------------------------------------------------------------------------- evidence graph
DY = -8
COLX = {0: (36, 160), 1: (230, 376), 2: (452, 612), 3: (648, 806)}
BOX = {  # node -> (column, y0, y1)   hand-placed for the 18 nodes of the pack; see the module docstring
    "N1": (0, 66, 122), "N2": (0, 136, 192), "N3": (0, 206, 262), "N4": (0, 276, 332), "N18": (0, 344, 410), "N16": (0, 420, 480),
    "N17": (1, 66, 120), "N5": (1, 126, 476),
    "N8": (2, 66, 182), "N11": (2, 190, 306), "N15": (2, 314, 368), "N13": (2, 376, 430), "N14": (2, 438, 492),
    "N6": (3, 66, 120), "N7": (3, 128, 182), "N9": (3, 190, 244), "N10": (3, 252, 306), "N12": (3, 376, 430),
}
KIND_TEXT = {"observation": "data read in a source", "inference": "reasoned from data", "claim": "a claim for one drug class",
             "alternative": "a rival reading, not measured", "experiment": "a proposed measurement", "gap": "a documented absence"}
EDGE_STYLE = {  # status -> look; distinct in greyscale by width, dash pattern and tag fill (OBSERVED solid, INFERRED dashed, HYPOTHESISED dotted)
    "OBSERVED": dict(w=2.6, dash=None, cap=0, fill=(0, 0, 0), ink="#fff", order=3, text="stated by the source, or a documented absence"),
    "INFERRED": dict(w=1.8, dash="[4 2.4] 0", cap=0, fill=(0.78, 0.78, 0.78), ink="#000", order=2, text="a reasoning step from observations"),
    "HYPOTHESISED": dict(w=1.7, dash="[0.1 3.6] 0", cap=1, fill=(1, 1, 1), ink="#000", order=1, text="predicted or competing; none tested"),
}
CONTEXT_ONLY = dict(w=1.0, dash="[4 2.4] 0", cap=0, fill=(1, 1, 1), ink="#555", order=0, color=(0.55, 0.55, 0.55), text="not a test (drawn lightly)")


def edge_look(e):
    if e["relation"] == "context_only" or e["status"] == "CONTEXT ONLY":
        return CONTEXT_ONLY
    if e["status"] not in EDGE_STYLE:
        raise SystemExit(f"edge {e['edge_id']} has the unknown status {e['status']!r}: add it to EDGE_STYLE")
    return EDGE_STYLE[e["status"]]


TAG_FRAC = {"G7": 0.82, "G10": 0.82, "G12": 0.82, "G14": 0.82, "G17": 0.60, "G18": 0.70}  # the horizontals carry their tag next to the hub, clear of the two bus lanes


def box_rect(nid):
    import pymupdf
    if nid not in BOX:
        raise SystemExit(f"graph node {nid} has no place in BOX: add coordinates")
    c, y0, y1 = BOX[nid]
    return pymupdf.Rect(COLX[c][0], y0 + DY, COLX[c][1], y1 + DY)


def routes():
    """Polylines per edge id (page coordinates; y given before DY): straight where possible, two elbow buses."""
    L = lambda n, y: (box_rect(n).x0, y + DY)   # noqa: E731  point on the left side of node n at y
    R = lambda n, y: (box_rect(n).x1, y + DY)   # noqa: E731
    cx = lambda n: (box_rect(n).x0 + box_rect(n).x1) / 2  # noqa: E731
    B = lambda n: (cx(n), box_rect(n).y1)       # noqa: E731
    T = lambda n: (cx(n), box_rect(n).y0)       # noqa: E731
    return {
        "G1": [B("N2"), T("N3")], "G2": [B("N1"), T("N2")], "G3": [B("N3"), T("N4")],
        "G4": [R("N3", 234), L("N5", 234)],
        "G5": [L("N6", 93), R("N8", 93)], "G6": [L("N7", 155), R("N8", 155)],
        "G7": [L("N8", 150), R("N5", 150)],
        "G8": [L("N9", 217), R("N11", 217)], "G9": [L("N10", 279), R("N11", 279)],
        "G10": [L("N11", 260), R("N5", 260)],
        "G11": [L("N12", 403), R("N13", 403)],
        "G12": [L("N13", 410), R("N5", 410)],
        "G13": [L("N14", 465), R("N5", 465)],
        "G14": [L("N15", 341), R("N5", 341)],
        "G15": [R("N16", 450), L("N5", 450)],
        "G16": [R("N17", 90), L("N8", 90)],
        "G17": [R("N17", 106), (428, 106 + DY), (428, 215 + DY), L("N11", 215)],
        "G18": [R("N17", 98), (440, 98 + DY), (440, 388 + DY), L("N13", 388)],
        "G19": [R("N18", 376), L("N5", 376)],
    }


def _along(pts, frac):
    segs = [(abs(pts[k + 1] - pts[k]), k) for k in range(len(pts) - 1)]
    target = sum(s for s, _ in segs) * frac
    for s, k in segs:
        if target <= s:
            return pts[k] + (pts[k + 1] - pts[k]) * (target / s)
        target -= s
    return pts[-1]


def _node_style(kind):
    return dict(fill=(0, 0, 0) if kind == "experiment" else ((0.88, 0.88, 0.88) if kind == "inference" else (1, 1, 1)),
                width={"observation": 2.0, "claim": 1.2, "alternative": 1.3}.get(kind, 1.0),
                dashes="[4 3] 0" if kind == "alternative" else ("[1 2] 0" if kind == "gap" else None))


def draw_graph_node(page, rect, n):
    kind = n["kind"]
    if kind not in KIND_TEXT:
        raise SystemExit(f"graph node {n['node_id']} has the unknown kind {kind!r}: add it to KIND_TEXT and the drawing")
    st = _node_style(kind)
    sh = page.new_shape()
    sh.draw_rect(rect)
    sh.finish(color=(0, 0, 0), fill=st["fill"], width=st["width"], dashes=st["dashes"])
    sh.commit()
    pad = 3.0
    if kind == "claim":  # double outline
        inner = page.new_shape()
        inner.draw_rect(rect + (2.8, 2.8, -2.8, -2.8))
        inner.finish(color=(0, 0, 0), width=0.8)
        inner.commit()
        pad = 6.0
    ink = "#fff" if kind == "experiment" else "#000"
    head = f"{n['node_id']} · {kind.upper()} ({n['stage'].split()[0]}) {n['ref']}"
    box = rect + (pad, 2.5, -pad, -4.5 if kind == "claim" else -1.5)  # a claim's inner outline sits 2.8 pt inside the box

    def html_at(size):
        return (f"<p style='margin:0;font-size:{size * 0.84:.1f}pt'><b>{esc(head)}</b></p>"
                f"<p style='margin:1pt 0 0;font-size:{size:.1f}pt;line-height:1.1'>{esc(n['label'])}</p>")
    css = f"body{{font-family:sans-serif;color:{ink}}}"
    size = next((z for z in NODE_SIZES if _probe(box, html_at(z), css)), None)  # the largest type that fits this box without shrinking
    if size is None:
        raise SystemExit(f"graph node {n['node_id']} does not fit at {NODE_SIZES[-1]} pt: shorten the label in the pack or enlarge BOX")
    spare, _ = page.insert_htmlbox(box, html_at(size), css=css, scale_low=1)
    if spare < 0:
        raise SystemExit(f"graph node {n['node_id']} overflowed at {size} pt after fitting; check _probe")
    return size


NODE_SIZES = [10.0, 9.6, 9.2, 8.8, 8.4, 8.0, 7.6, 7.2]
_SCRATCH = {}


def _probe(box, html, css):
    """True when html fits in box at its own size (tried on a scratch page, nothing is drawn on the real one)."""
    import pymupdf
    if "page" not in _SCRATCH:
        _SCRATCH["doc"] = pymupdf.open()
        _SCRATCH["page"] = _SCRATCH["doc"].new_page(width=842, height=595)
    spare, _ = _SCRATCH["page"].insert_htmlbox(box, html, css=css, scale_low=1)
    return spare >= 0


def draw_key(page, kinds, statuses, y0):
    import pymupdf
    page.draw_rect(pymupdf.Rect(36, y0, 806, 558), color=(0, 0, 0), width=0.7)

    def label(x, y, w, h, t, sz=6.4):
        page.insert_htmlbox(pymupdf.Rect(x, y, x + w, y + h), f"<p style='margin:0;font-size:{sz}pt;line-height:1.1'>{t}</p>", css="body{font-family:sans-serif;color:#000}")
    label(40, y0 + 10, 38, 12, "<b>Edges</b>", 7.2)
    x = 78
    for st, sty in statuses:
        ink = sty.get("color", (0, 0, 0))
        s = page.new_shape()
        s.draw_line(pymupdf.Point(x, y0 + 15), pymupdf.Point(x + 62, y0 + 15))  # long enough that the pattern shows on both sides of the tag
        s.finish(color=ink, width=sty["w"], dashes=sty["dash"], lineCap=sty["cap"])
        s.commit()
        t = page.new_shape()
        t.draw_rect(pymupdf.Rect(x + 20, y0 + 9, x + 42, y0 + 21))
        t.finish(color=ink, fill=sty["fill"], width=0.8)
        t.commit()
        label(x + 66, y0 + 5, 76, 24, f"<b>{st}</b>: {esc(sty['text'])}", 6.2)
        x += 144
    s = page.new_shape()
    for off in (0, 5):
        s.draw_line(pymupdf.Point(x + 6 + off, y0 + 6), pymupdf.Point(x + 6 + off, y0 + 24))
    s.finish(color=(0, 0, 0), width=2.2)
    s.commit()
    label(x + 22, y0 + 5, 66, 24, "<b>Double bar</b>: the transfer breaks here", 6.2)
    label(40, y0 + 36, 38, 12, "<b>Nodes</b>", 7.2)
    x = 78
    for kind in kinds:
        st = _node_style(kind)
        r = pymupdf.Rect(x, y0 + 34, x + 22, y0 + 46)
        s = page.new_shape()
        s.draw_rect(r)
        s.finish(color=(0, 0, 0), fill=st["fill"], width=st["width"], dashes=st["dashes"])
        s.commit()
        if kind == "claim":
            i2 = page.new_shape()
            i2.draw_rect(r + (2.2, 2.2, -2.2, -2.2))
            i2.finish(color=(0, 0, 0), width=0.7)
            i2.commit()
        label(x + 26, y0 + 32, 92, 18, f"<b>{kind.upper()}</b>: {esc(KIND_TEXT[kind])}", 6.2)
        x += 120
    label(40, y0 + 53, 764, 14, "Letters in brackets are the stages: D data, I inference, H hypothesis, E experiment. Status is carried by line style, fill and the words, never by colour. "
          "No weights, scores or probabilities are drawn; nothing here implies that any drug should or should not be used.", 6.2)


def graph_page(doc, nodes, edges):
    import pymupdf
    page = doc.new_page(width=842, height=595)
    page.insert_htmlbox(pymupdf.Rect(36, 22, 806, 54),
                        "<p class='meta' style='margin:0;font-size:7.6pt'>LEGEND · EVIDENCE GRAPH</p><h1 style='margin:0;font-family:serif;font-size:14.5pt'>Figure 1. Where the transfer from the d-APV slice result to ketamine breaks</h1>",
                        css="body{font-family:sans-serif;color:#000}")
    ids = {n["node_id"] for n in nodes}
    if ids != set(BOX):
        raise SystemExit(f"graph nodes in the pack differ from BOX: new {sorted(ids - set(BOX))}, gone {sorted(set(BOX) - ids)}")
    route = routes()
    if {e["edge_id"] for e in edges} != set(route):
        raise SystemExit(f"graph edges in the pack differ from routes(): new {sorted({e['edge_id'] for e in edges} - set(route))}")
    tags = {}
    for e in sorted(edges, key=lambda e: edge_look(e)["order"]):  # heavy lines last, each with a white halo: they bridge the lighter ones
        sty = edge_look(e)
        ink = sty.get("color", (0, 0, 0))
        pts = [pymupdf.Point(*p) for p in route[e["edge_id"]]]
        for width, colour, dashes, cap in ((sty["w"] + 4.5, (1, 1, 1), None, 0), (sty["w"], ink, sty["dash"], sty["cap"])):
            s = page.new_shape()
            s.draw_polyline(pts)
            s.finish(color=colour, width=width, dashes=dashes, lineCap=cap, closePath=False)
            s.commit()
        v = pts[-1] - pts[-2]
        nrm = v / abs(v)
        perp = pymupdf.Point(-nrm.y, nrm.x)
        tip, base = pts[-1], pts[-1] - nrm * 8
        h = page.new_shape()
        h.draw_polyline([tip, base + perp * 3.6, base - perp * 3.6, tip])
        h.finish(color=ink, fill=ink, closePath=True, width=0.4)
        h.commit()
        pos = _along(pts, TAG_FRAC.get(e["edge_id"], 0.5))
        total = sum(abs(pts[k + 1] - pts[k]) for k in range(len(pts) - 1))
        if total < 30:  # a short edge: the tag goes beside the line so the arrow stays visible
            pos = pos + pymupdf.Point(20, 0)
        if e["relation"] == "transfer_break":
            d = pts[-1] - pts[0]
            dn = d / abs(d)
            dp = pymupdf.Point(-dn.y, dn.x)
            m = page.new_shape()
            for off in (0, 5):
                c = pts[0] + dn * (12 + off)
                m.draw_line(c + dp * 9, c - dp * 9)
            m.finish(color=(0, 0, 0), width=2.4)
            m.commit()
            pos = pts[0] + dn * 40
        tags[e["edge_id"]] = (pos, sty)
    scales = [draw_graph_node(page, box_rect(n["node_id"]), n) for n in nodes]
    for eid, (pos, sty) in tags.items():
        r = pymupdf.Rect(pos.x - 11, pos.y - 7, pos.x + 11, pos.y + 7)
        sh = page.new_shape()
        sh.draw_rect(r)
        sh.finish(color=sty.get("color", (0, 0, 0)), fill=sty["fill"], width=0.9)
        sh.commit()
        page.insert_htmlbox(r + (0, 1.6, 0, 0), f"<p style='margin:0;font-size:8pt;text-align:center'><b>{eid}</b></p>", css=f"body{{font-family:sans-serif;color:{sty['ink']}}}")
    kinds = [k for k in KIND_TEXT if any(n["kind"] == k for n in nodes)]
    looks = {}
    for e in edges:
        st = "CONTEXT ONLY" if (e["relation"] == "context_only" or e["status"] == "CONTEXT ONLY") else e["status"]
        looks[st] = edge_look(e)
    draw_key(page, kinds, sorted(looks.items(), key=lambda kv: -kv[1]["order"]), 486)
    return min(scales)  # smallest node type size in pt


# ---------------------------------------------------------------------------- assembly
def read_tsv(path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s))


def find_pages(doc, titles):
    """First page (1-based) at or after the previous hit where a large-type line (14 pt or more) starts with each title:
    a table cell or a sentence that merely mentions a title does not count."""
    start, out = 0, []
    for t in titles:
        for i in range(start, len(doc)):
            lines = [(sp["size"], _norm(sp["text"]).strip()) for blk in doc[i].get_text("dict")["blocks"] if "lines" in blk
                     for ln in blk["lines"] for sp in ln["spans"][:1]]
            if any(size >= 14 and text.startswith(_norm(t)) for size, text in lines):
                out.append(i + 1)
                start = i
                break
        else:
            raise SystemExit(f"title not found as large type in the PDF: {t}")
    return out


def assemble(pack, commit, landed, pagemap):
    import pymupdf
    A, B, C, D, F, nodes, edges, prov = pack
    doc = pymupdf.open()
    doc.insert_pdf(story_doc(lambda: front_html(A, pagemap) + f_html(F), False))
    min_scale = graph_page(doc, nodes, edges)
    doc.insert_pdf(story_doc(lambda: edge_list_html(edges) + d_html(D), True))
    doc.insert_pdf(story_doc(lambda: back_html(B, C, prov, commit, landed), False))
    return doc, min_scale


def build(out: Path, landed: str = "") -> Path:
    import pymupdf
    pack = [parse_md(CONTENT / "A_decision_evidence.md"), parse_md(CONTENT / "B_references.md"), parse_md(CONTENT / "C_methods_and_coverage.md"),
            parse_md(CONTENT / "D_negative_and_quantitative.md"), parse_md(CONTENT / "F_deciding_measurement.md"),
            read_tsv(CONTENT / "E_evidence_graph_nodes.tsv"), read_tsv(CONTENT / "E_evidence_graph_edges.tsv")]
    commit = subprocess.run(["git", "log", "-1", "--format=%H", "--", str(CONTENT)], capture_output=True, text=True, cwd=CONTENT).stdout.strip() or "uncommitted"
    prov = [(n, sha256(CONTENT / n)) for n in INPUTS]
    if landed:  # the sha must name a commit that contains the content commit; never hand-typed into the PDF unverified
        full = subprocess.run(["git", "rev-parse", "--verify", landed + "^{commit}"], capture_output=True, text=True, cwd=CONTENT).stdout.strip()
        if not full or subprocess.run(["git", "merge-base", "--is-ancestor", commit, full], cwd=CONTENT).returncode != 0:
            raise SystemExit(f"--landed {landed} does not contain content commit {commit[:12]}")
        landed = full
    pack.append(prov)
    titles = ["Ketamine in WWOX-related epilepsy", "The deciding measurement", "Figure 1. Where the transfer", "Figure 1: edge list",
              "Negative and ambiguous results, and the quantitative details", "Methods and coverage"]
    pagemap = None
    for _ in range(4):  # the page-order line on page 1 needs the page numbers of the later sections: lay out until they stop moving
        doc, min_scale = assemble(pack, commit, landed, pagemap)
        new = dict(zip("AFGEDM", find_pages(doc, titles)))
        if new == pagemap:
            break
        pagemap = new
    else:
        raise SystemExit("page-order line did not settle")
    total = len(doc)
    footer = "AI-curated brief for discussion with a clinical team · Not medical advice · content " + commit[:12] + (" · main " + landed[:12] if landed else "")
    for page in doc:
        w, h = page.rect.width, page.rect.height
        page.insert_htmlbox(pymupdf.Rect(bp.MARGIN_X, h - 36, w - 110, h - 14), f"<p style='margin:0;font-size:7.2pt'>{escape(footer)}</p>", css="body{font-family:sans-serif;color:#222}")
        page.insert_htmlbox(pymupdf.Rect(w - 110, h - 36, w - bp.MARGIN_X, h - 14), f"<p style='margin:0;font-size:7.2pt;text-align:right'>{page.number + 1} / {total}</p>", css="body{font-family:sans-serif;color:#222}")
    marks = [("Decision evidence", pagemap["A"]), ("The deciding measurement", pagemap["F"]), ("Figure 1. Evidence graph", pagemap["G"]),
             ("Figure 1: edge list", pagemap["E"]), ("Negative results and quantitative details", pagemap["D"]),
             ("Methods, references and provenance", pagemap["M"])]
    doc.set_toc([[1, n, p] for n, p in marks])
    keywords = "pilot; not medical advice; content-commit " + commit + ("; main " + landed if landed else "") + "; " + "; ".join(f"{n}={h[:12]}" for n, h in prov)
    doc.set_metadata({"title": "Ketamine in WWOX-related epilepsy (pilot, final content)", "author": "LEGEND",
                      "subject": "AI-curated research brief for discussion with a clinical team", "keywords": keywords})
    doc.xref_set_key(doc.pdf_catalog(), "Lang", "(en)")
    sys.path.append(str(bp.LIBS))
    try:
        doc.subset_fonts()
    except Exception as exc:
        print("font subsetting skipped:", exc)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(doc.tobytes(garbage=4, deflate=True, no_new_id=True))
    print(f"{total} pages; smallest graph node text {min_scale:.1f} pt; page order {pagemap}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--landed", default="", help="main-branch commit that contains the content commit; verified with git")
    ap.add_argument("--out", type=Path, default=HERE / "out/ketamine_brief_pilot_final.pdf")
    args = ap.parse_args()
    print(build(args.out, args.landed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
