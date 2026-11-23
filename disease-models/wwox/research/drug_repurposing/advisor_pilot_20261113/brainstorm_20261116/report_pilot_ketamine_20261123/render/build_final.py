"""ADV-201 increment 2: the ketamine brief built from SCI's content pack (../content/), not from the stand-in.

Usage: python3 -I build_final.py [--out out/ketamine_brief_pilot_final.pdf]

Reads A to F of the pack (markdown tables and the two graph TSVs), draws the 18-node, 19-edge evidence
graph on a landscape page, and stamps the PDF with the content commit and the SHA-256 of every input
file (printed on the Methods page and written into the PDF keywords), so a cold reader can say which
input it read. Reuses the Story helpers of build_pilot.py. Nothing outside this folder is read or
written except `git log` for the content commit.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import subprocess
import sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_pilot as bp  # noqa: E402  (CSS, margins, Story helper)

CONTENT = HERE.parent / "content"
INPUTS = ["A_decision_evidence.md", "B_references.md", "C_methods_and_coverage.md", "D_negative_and_quantitative.md",
          "E_evidence_graph_nodes.tsv", "E_evidence_graph_edges.tsv", "E_evidence_graph_spec.md",
          "F_deciding_measurement.md", "VERIFICATION_LEDGER_ADV200.tsv"]

CSS_FINAL = bp.CSS + """
.wide td{font-size:7.6pt}
.wide th{font-size:7.4pt}
.absrow{border-left:5pt solid #000}
.status{font-size:7.4pt;font-weight:bold}
ul{margin:0 0 4pt 0;padding-left:12pt}
li{margin:0 0 3pt 0;font-size:8.8pt}
.prov td{font-size:7.4pt;font-family:monospace}
"""


# ---------------------------------------------------------------------------- markdown reading
def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inline(text: str) -> str:
    """Escape, then turn **bold** into <b>; nothing else is interpreted."""
    out = escape(text.strip())
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_md(path: Path):
    """-> list of sections {level, title, lines(list of str outside tables), tables([{header, rows}])}."""
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
            bullets.append(re.sub(r"^\d+\. ", "", line.strip()))
        else:
            flush()
            out.append(f"<p>{inline(line)}</p>")
    flush()
    return "".join(out)


WIDTH_HINT = {"#": 4, "Stage": 4, "Status": 10, "Ref": 6, "Locator": 14, "No.": 3, "PMID": 7, "DOI": 12, "Unit": 6,
              "Assay or source": 20, "Value as printed": 19, "Spread as the source gives it": 13, "Exposure definition": 12}


def cell_html(header: str, text: str) -> str:
    if header == "Status":
        if text.startswith("ABSTRACT-ONLY"):
            return f'<td class="status">[{inline(text)}]</td>'
        return f'<td class="status">{inline(text)}</td>'
    return f"<td>{inline(text)}</td>"


def table_html(tbl: dict, wide: bool = False, link_pmid: bool = False) -> str:
    hdr = tbl["header"]
    n = len(hdr)
    fixed = {k: WIDTH_HINT.get(h) for k, h in enumerate(hdr) if WIDTH_HINT.get(h)}
    free = [k for k in range(n) if k not in fixed]
    rest = max(100 - sum(fixed.values()), 20)
    widths = [fixed.get(k, rest // max(len(free), 1)) for k in range(n)]
    scale = 100 / sum(widths)
    widths = [round(w * scale, 1) for w in widths]
    head = "<tr>" + "".join(f"<th width='{w}%'>{escape(h)}</th>" for h, w in zip(hdr, widths)) + "</tr>"
    body = []
    for row in tbl["rows"]:
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
        body.append("<tr>" + "".join(cells) + "</tr>")
    # the 1 pt spacer after the table is deliberate: a heading placed straight after a table made pymupdf's Story
    # loop for ever on the corrected pack (found 2026-11-23); with a block between them it finishes
    return f'<table class="tbl{" wide" if wide else ""}">{head}{"".join(body)}</table><div style="height:1pt"></div>'


# ---------------------------------------------------------------------------- Story sections
def story_doc(html: str, landscape: bool):
    import pymupdf
    paper = pymupdf.paper_rect("a4-l" if landscape else "a4")
    rect = paper + (bp.MARGIN_X, bp.MARGIN_TOP, -bp.MARGIN_X, -bp.MARGIN_BOTTOM)
    story = pymupdf.Story(html=html, user_css=CSS_FINAL)
    count = [0]

    def where(n, filled, **_):  # fail fast if a block cannot fit on a page (Story would otherwise loop for ever)
        count[0] += 1
        if count[0] > 25:
            raise SystemExit("Story did not finish in 25 pages: a table row or block is taller than the page")
        return paper, rect, None
    return story.write_with_links(where)


def front_html(A):
    intro = A[0]["lines"] + find(A, "A. Decision")["lines"]
    decision = find(A, "The decision this page serves")
    out = [
        '<p class="meta">LEGEND · WWOX / WOREE · RESEARCH BRIEF · PILOT, FINAL CONTENT</p>',
        "<h1>Ketamine in WWOX-related epilepsy</h1>",
        '<div class="tag"><b>AI-curated research brief for discussion with a clinical team</b><br>'
        '<span class="small">Hypothesis level. Not medical advice. No dose, schedule or recommendation. Reference genotype class only. '
        "Content verified 2026-11-23.</span></div>",
        "<h2>The decision this page serves</h2>" + paragraphs_html(decision["lines"]),
        "<h2>Where to find what</h2>",
        '<table class="guide"><tr><td width="30%"><b>Primary anchor</b></td><td>Row W2 and the graph nodes N1 and N2: d-APV 50 uM stopped the bursts in five Wwox-knockout slices from three animals [1].</td></tr>'
        '<tr><td><b>Compound measured in Wwox tissue</b></td><td>d-APV, a competitive antagonist (W2). Row W9: no dedicated ketamine or memantine intervention comparison was found in a WWOX system (absence in an index is not proof of absence).</td></tr>'
        '<tr><td><b>Strongest contrary or weakening evidence</b></td><td>Section D1 (D1.1 to D1.5, D1.9) and the rivals in Block 2 (I3 Ih, I4 disinhibition).</td></tr>'
        '<tr><td><b>Measurement that would change the choice</b></td><td>Page "The one measurement that would change the choice" (section F).</td></tr></table>',
        f'<p class="note">{inline(find(A, "A. Decision")["lines"][1]) if len(find(A, "A. Decision")["lines"]) > 1 else ""}</p>' if False else "",
    ]
    how = [l for l in A[1]["lines"] if l.startswith("**How to read")] if len(A) > 1 else []
    howtxt = [l for l in find(A, "A. Decision")["lines"] if l.startswith("**How to read")]
    if howtxt:
        out.append(f'<p class="note">{inline(howtxt[0])}<br><b>Open item flagged by the content team: the sIPSC plus/minus figures of Breton et al. (row W5) are printed without a named statistic.</b><br><b>A heavy bar at the left edge of a row, and the mark [ABSTRACT-ONLY], means the row was reproduced from the PubMed abstract and not from the full text.</b></p>')
    for title in ("Block 1", "Block 2", "Block 3", "Block 4"):
        s = find(A, title)
        out.append(f"<h2>{escape(s['title'])}</h2>")
        out += [table_html(t) for t in s["tables"]]
    plain = find(A, "What the evidence supports")
    out.append(f"<h2>{escape(plain['title'])}</h2>" + paragraphs_html(plain["lines"]))
    return "".join(out)


def f_html(F):
    out = ['<h1 style="font-size:19pt">The one measurement that would change the choice</h1>']
    for s in F:
        if s["level"] == 2:
            out.append(f"<h2>{escape(s['title'])}</h2>" + paragraphs_html(s["lines"]) + "".join(table_html(t) for t in s["tables"]))
        elif s["level"] == 1 and s["lines"]:
            pass
    return "".join(out)


def d_html(D):
    out = ['<h1 style="font-size:19pt">Negative and ambiguous results, and the quantitative details</h1>']
    d1 = find(D, "D1.")
    out.append(f"<h2>{escape(d1['title'])}</h2>" + "".join(table_html(t, wide=True) for t in d1["tables"]))
    d2 = find(D, "D2.")
    out.append(f'<div class="sec"><h2>{escape(d2["title"])}</h2>' + paragraphs_html(d2["lines"]))
    t = d2["tables"][0]
    hdr = t["header"]
    defi = hdr.index("Exposure definition")
    groups = {"Nominal bath concentration (applied to a preparation; no plasma protein)": lambda d: d.startswith("bath"),
              "Total plasma (measured in blood plasma)": lambda d: d.startswith("plasma"),
              "Cerebrospinal fluid (lumbar)": lambda d: d.startswith("CSF")}
    used = set()
    for title, pred in groups.items():
        rows = [r for k, r in enumerate(t["rows"]) if pred(r[defi])]
        used.update(id(r) for r in rows)
        out.append(f"<h3>Matrix: {escape(title)}</h3>" + table_html({"header": hdr, "rows": rows}, wide=True))
    rest = [r for r in t["rows"] if id(r) not in used]
    if rest:
        out.append("<h3>Other</h3>" + table_html({"header": hdr, "rows": rest}, wide=True))
    out.append("</div>")
    d3 = find(D, "D3.")
    out.append(f'<div class="sec"><h2>{escape(d3["title"])}</h2>' + "".join(table_html(x, wide=True) for x in d3["tables"]) + paragraphs_html(d3["lines"]) + "</div>")
    return "".join(out)


def back_html(B, C, provenance_rows, commit, landed=""):
    refs = B[1:]  # first real section is the table, notes follow
    tbl = next(s for s in B if s["tables"])["tables"][0]
    notes = find(B, "Notes on identifiers")
    out = ["<h1 style=\"font-size:19pt\">Methods and coverage</h1>"]
    for s in C:
        if s["level"] == 2:
            out.append(f"<h2>{escape(s['title'])}</h2>" + paragraphs_html(s["lines"]) + "".join(table_html(t) for t in s["tables"]))
    out.append('<div class="sec"><h1 style="font-size:19pt">References</h1>'
               "<p class='small'>One numbered list for every source used in the tables. Depth read is what this pack read: FT full text, FT+fig full text with figure image, AB abstract only. PMID and DOI link to the record.</p>"
               + table_html(tbl, wide=True, link_pmid=True) +
               f"<h3>{escape(notes['title'])}</h3>" + paragraphs_html(notes["lines"]) + "</div>")
    prow = "".join(f"<tr><td>{escape(n)}</td><td>{h}</td></tr>" for n, h in provenance_rows)
    out.append('<h2>Provenance: which input this PDF was built from</h2>'
               f"<p class='small'>Content commit: <b>{escape(commit)}</b> (last commit touching the content folder)." + (f" Landed on main as <b>{escape(landed)}</b>." if landed else "") + f" Input files and the SHA-256 of each:</p>"
               f"<table class='tbl prov'><tr><th width='45%'>File</th><th>SHA-256</th></tr>{prow}</table>")
    return "".join(out)


# ---------------------------------------------------------------------------- evidence graph
COL = [36, 242, 448, 654]            # four columns of 150 pt with 56 pt channels between them
CW, NH = 150, 62
ROW0, PITCH = 68, 69
POS = {  # node -> (column, row), rows 1-based
    "N1": (0, 1), "N2": (0, 2), "N3": (0, 3), "N4": (0, 4),
    "N17": (1, 1), "N16": (1, 2), "N5": (1, 4), "N18": (1, 6),
    "N8": (2, 1), "N11": (2, 3), "N15": (2, 4), "N13": (2, 5), "N14": (2, 6),
    "N6": (3, 1), "N7": (3, 2), "N9": (3, 3), "N10": (3, 4), "N12": (3, 5),
}


def node_rect(nid):
    import pymupdf
    c, r = POS[nid]
    x, y = COL[c], ROW0 + PITCH * (r - 1)
    return pymupdf.Rect(x, y, x + CW, y + NH)


def _pt(nid, side, d=0.0):
    r = node_rect(nid)
    cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
    return {"L": (r.x0, cy + d), "R": (r.x1, cy + d), "T": (cx + d, r.y0), "B": (cx + d, r.y1)}[side]


def routes():
    """Hand-routed polylines for the fixed topology of the pack (every edge id must appear here)."""
    P = _pt
    X = {"G18": 400, "G17": 410, "G12": 420, "G13": 428, "G10": 436, "G7": 442}
    def elbow(eid, start, end):
        (x0, y0), (x1, y1) = start, end
        return [(x0, y0), (X[eid], y0), (X[eid], y1), (x1, y1)]
    return {
        "G1": [P("N2", "B"), P("N3", "T")],
        "G2": [P("N1", "B"), P("N2", "T")],
        "G3": [P("N3", "B"), P("N4", "T")],
        "G4": [P("N3", "R"), P("N5", "L")],
        "G5": [P("N6", "L"), P("N8", "R")],
        "G6": [P("N7", "L"), P("N8", "R", 14)],
        "G7": elbow("G7", P("N8", "L", 10), P("N5", "R", -24)),
        "G8": [P("N9", "L"), P("N11", "R")],
        "G9": [P("N10", "L"), P("N11", "R", 14)],
        "G10": elbow("G10", P("N11", "L", 10), P("N5", "R", -12)),
        "G11": [P("N12", "L"), P("N13", "R")],
        "G12": elbow("G12", P("N13", "L", 10), P("N5", "R", 12)),
        "G13": elbow("G13", P("N14", "L"), P("N5", "R", 24)),
        "G14": [P("N15", "L"), P("N5", "R")],
        "G15": [P("N16", "B"), P("N5", "T")],
        "G16": [P("N17", "R", -10), P("N8", "L", -10)],
        "G17": elbow("G17", P("N17", "R"), P("N11", "L", -10)),
        "G18": elbow("G18", P("N17", "R", 10), P("N13", "L", -10)),
        "G19": [P("N18", "T"), P("N5", "B")],
    }


def graph_pages(doc, nodes, edges):
    import pymupdf
    page = doc.new_page(width=842, height=595)
    page.insert_htmlbox(pymupdf.Rect(36, 26, 806, 62),
                        "<p class='meta' style='margin:0;font-size:8pt'>LEGEND · EVIDENCE GRAPH</p><h1 style='margin:1pt 0 0;font-family:serif;font-size:15pt'>Figure 1. Where the transfer from the d-APV slice result to ketamine breaks</h1>",
                        css="body{font-family:sans-serif;color:#000}")
    rects = {n["node_id"]: node_rect(n["node_id"]) for n in nodes}
    route = routes()
    badges = {}
    for e in edges:
        pts = [pymupdf.Point(*p) for p in route[e["edge_id"]]]
        obs = e["status"] == "OBSERVED"
        s = page.new_shape()
        s.draw_polyline(pts)
        s.finish(color=(0, 0, 0), width=2.2 if obs else 1.1, dashes=None if obs else "[5 3] 0", closePath=False)
        s.commit()
        v = pts[-1] - pts[-2]
        n = v / abs(v)
        perp = pymupdf.Point(-n.y, n.x)
        tip = pts[-1]
        base = tip - n * 7
        h = page.new_shape()
        h.draw_polyline([tip, base + perp * 3.2, base - perp * 3.2, tip])
        h.finish(color=(0, 0, 0), fill=(0, 0, 0), closePath=True, width=0.4)
        h.commit()
        segs = [(abs(pts[k + 1] - pts[k]), k) for k in range(len(pts) - 1)]
        k = max(segs)[1]
        mid = (pts[k] + pts[k + 1]) / 2
        if e["relation"] == "transfer_break":
            d = pts[k + 1] - pts[k]
            dn = d / abs(d)
            dp = pymupdf.Point(-dn.y, dn.x)
            m = page.new_shape()
            for off in (-3.0, 3.0):
                c = mid + dn * (off + 0.0) + dn * 12
                m.draw_line(c + dp * 8, c - dp * 8)
            m.finish(color=(0, 0, 0), width=2.2)
            m.commit()
        badges[e["edge_id"]] = (mid, obs)
    for n_ in nodes:
        draw_graph_node(page, rects[n_["node_id"]], n_)
    for eid, (mid, obs) in badges.items():  # black tag = OBSERVED, white tag = HYPOTHESISED
        r = pymupdf.Rect(mid.x - 9, mid.y - 6, mid.x + 9, mid.y + 6)
        sh = page.new_shape()
        sh.draw_rect(r)
        sh.finish(color=(0, 0, 0), fill=(0, 0, 0) if obs else (1, 1, 1), width=0.9)
        sh.commit()
        page.insert_htmlbox(r + (0, 1.2, 0, 0), f"<p style='margin:0;font-size:6.6pt;text-align:center'><b>{eid}</b></p>",
                            css=f"body{{font-family:sans-serif;color:{'#fff' if obs else '#000'}}}")
    key(page)
    return page


def draw_graph_node(page, rect, n):
    import pymupdf
    kind, stage = n["kind"], n["stage"]
    black = kind == "experiment"
    dashed = stage.startswith("H") or kind == "alternative"
    grey = kind == "inference"
    gap = kind == "gap"
    sh = page.new_shape()
    sh.draw_rect(rect)
    sh.finish(color=(0, 0, 0), fill=(0, 0, 0) if black else ((0.9, 0.9, 0.9) if grey else (1, 1, 1)),
              width=1.9 if stage == "D" and kind in ("observation", "claim") else 1.0,
              dashes="[4 3] 0" if dashed else ("[1 2] 0" if gap else None))
    sh.commit()
    if dashed:
        x = rect.x0 - rect.height
        hat = page.new_shape()
        while x < rect.x1:
            hat.draw_line(pymupdf.Point(max(x, rect.x0), rect.y1 - max(rect.x0 - x, 0)),
                          pymupdf.Point(min(x + rect.height, rect.x1), rect.y0 + max(x + rect.height - rect.x1, 0)))
            x += 7
        hat.finish(color=(0.84, 0.84, 0.84), width=0.5)
        hat.commit()
        page.draw_rect(rect + (3, 3, -3, -2), color=None, fill=(1, 1, 1))
    ink = "#fff" if black else "#000"
    ref = n["ref"]
    html = (f"<p style='margin:0;font-size:6.2pt'><b>{escape(n['node_id'])} · {escape(kind.upper())}</b> {escape(ref)}</p>"
            f"<p style='margin:1pt 0 0;font-size:6.9pt;line-height:1.12'>{escape(n['label'])}</p>")
    spare, _ = page.insert_htmlbox(rect + (3, 2, -3, -1), html, css=f"body{{font-family:sans-serif;color:{ink}}}")
    if spare < 0:
        raise SystemExit(f"graph node {n['node_id']} overflows; enlarge NH or shorten via the pack")


def key(page):
    import pymupdf
    y0 = 484
    page.draw_rect(pymupdf.Rect(36, y0, 806, 552), color=(0, 0, 0), width=0.7)
    items = [
        "<b>Edges.</b> Heavy solid line, black tag: OBSERVED (a stated measurement or a documented absence). Dashed line, white tag: HYPOTHESISED (reasoned or predicted; none tested). Double bar: the break in transfer (G4). The edge list on the next page gives each edge's relation and source.",
        "<b>Nodes.</b> Heavy outline: data read in a source. Grey fill: inference. Dashed outline: hypothesis or rival reading, not measured. Black fill: proposed experiment. Dotted outline: a documented absence. Status is carried by line style, fill and the words, never by colour.",
        "No weights, scores or probabilities are drawn; unlike models are not summed; nothing here implies that any drug should or should not be used.",
    ]
    yy = y0 + 4
    for t in items:
        page.insert_htmlbox(pymupdf.Rect(42, yy, 800, yy + 22), f"<p style='margin:0;font-size:7.4pt'>{t}</p>", css="body{font-family:sans-serif;color:#000}")
        yy += 21


def edge_list_html(edges):
    rows = "".join(
        f"<tr><td><b>{e['edge_id']}</b></td><td>{e['from']} to {e['to']}</td><td>{escape(e['relation'].replace('_', ' '))}</td>"
        f"<td>{escape(e['label'])}</td><td class='status'>{e['status']}</td><td>{escape(e['source'])}</td></tr>" for e in edges)
    return ('<h1 style="font-size:17pt">Figure 1: edge list</h1><table class="tbl wide"><tr><th width="5%">Edge</th><th width="9%">From to</th>'
            '<th width="12%">Relation</th><th>What the link says</th><th width="12%">Status</th><th width="22%">Source</th></tr>' + rows + "</table>")


# ---------------------------------------------------------------------------- assembly
def read_tsv(path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def build(out: Path, landed: str = "") -> Path:
    import pymupdf
    A = parse_md(CONTENT / "A_decision_evidence.md")
    B = parse_md(CONTENT / "B_references.md")
    C = parse_md(CONTENT / "C_methods_and_coverage.md")
    D = parse_md(CONTENT / "D_negative_and_quantitative.md")
    F = parse_md(CONTENT / "F_deciding_measurement.md")
    nodes = read_tsv(CONTENT / "E_evidence_graph_nodes.tsv")
    edges = read_tsv(CONTENT / "E_evidence_graph_edges.tsv")
    commit = subprocess.run(["git", "log", "-1", "--format=%H", "--", str(CONTENT)], capture_output=True, text=True, cwd=CONTENT).stdout.strip() or "uncommitted"
    prov = [(n, sha256(CONTENT / n)) for n in INPUTS]
    if landed:  # the sha must name a commit that contains the content commit; never hand-typed into the PDF unverified
        full = subprocess.run(["git", "rev-parse", "--verify", landed + "^{commit}"], capture_output=True, text=True, cwd=CONTENT).stdout.strip()
        if not full or subprocess.run(["git", "merge-base", "--is-ancestor", commit, full], cwd=CONTENT).returncode != 0:
            raise SystemExit(f"--landed {landed} does not contain content commit {commit[:12]}")
        landed = full
    parts = [story_doc(front_html(A), False)]
    doc = pymupdf.open()
    doc.insert_pdf(parts[0])
    toc_marks = [("Decision evidence", 1)]
    graph_pages(doc, nodes, edges)
    toc_marks.append(("Figure 1. Evidence graph", len(doc)))
    el = story_doc(edge_list_html(edges), True)
    doc.insert_pdf(el)
    f_doc = story_doc(f_html(F), False)
    toc_marks.append(("The one measurement that would change the choice", len(doc) + 1))
    doc.insert_pdf(f_doc)
    d_doc = story_doc(d_html(D), True)
    toc_marks.append(("Negative results and quantitative details", len(doc) + 1))
    doc.insert_pdf(d_doc)
    b_doc = story_doc(back_html(B, C, prov, commit, landed), False)
    toc_marks.append(("Methods, references and provenance", len(doc) + 1))
    doc.insert_pdf(b_doc)
    total = len(doc)
    footer = "AI-curated brief for discussion with a clinical team · Not medical advice · content " + commit[:12] + (" · main " + landed[:12] if landed else "")
    for page in doc:
        w, h = page.rect.width, page.rect.height
        page.insert_htmlbox(pymupdf.Rect(bp.MARGIN_X, h - 36, w - 110, h - 14), f"<p style='margin:0;font-size:7.2pt'>{escape(footer)}</p>", css="body{font-family:sans-serif;color:#222}")
        page.insert_htmlbox(pymupdf.Rect(w - 110, h - 36, w - bp.MARGIN_X, h - 14), f"<p style='margin:0;font-size:7.2pt;text-align:right'>{page.number + 1} / {total}</p>", css="body{font-family:sans-serif;color:#222}")
    doc.set_toc([[1, n, p] for n, p in toc_marks])
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
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--landed", default="", help="main-branch commit that contains the content commit; verified with git")
    ap.add_argument("--out", type=Path, default=HERE / "out/ketamine_brief_pilot_final.pdf")
    args = ap.parse_args()
    print(build(args.out, args.landed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
