"""ADV-279: which unread classes of the held partials are readable from held bytes, under the old and the wider rule.

Usage: python3 count_adv279.py <repo root> <root checkout> <ranking_adv265.tsv> <containment_all.tsv> <out tsv>
Read-only; no network. The rule is the one stated in PREREG_ADV279_RULE_SCI_20261125.md.
"""
import sys

if len(sys.argv) != 6 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import csv, importlib.util, json, os, re

repo, held, ranking, containment, out = sys.argv[1:6]
A219 = os.path.join(repo, "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/"
                          "adv219_receipt_label_audit_sci_20261124/labelling_flags_adv219.py")
spec = importlib.util.spec_from_file_location("a219", A219)
a219 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a219)

SEALED = ("adv174", "adv175")
SKIP = ("/check_runs", "/coordination", "/retraction_watch")
IMG = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff")
SUPP_EXT = IMG + (".pdf", ".xlsx", ".xls", ".docx", ".doc", ".zip", ".csv", ".pptx", ".mp4", ".mov", ".avi")
SUPP_RX = re.compile(r"supp|mmc\d|moesm|[-_.]s\d{2,3}(?!\d)|[-_]sd\d|_esm|image_\d|table_\d|data_sheet|extended|appendix", re.I)
MAIN_FIG_RX = re.compile(r"(?:[-_.](?:g|f)0*\d{1,2}|[-_]?fig(?:ure)?[-_ ]?0*\d{1,2}|gr\d{1,2})[a-z]?(?:\.large)?\.[a-z]{3,4}$", re.I)
TEXT_CLASSES = ("discussion", "tables", "limitations")

done = set()
with open(os.path.join(repo, "disease-models/wwox/registries/fulltext_read_receipts.jsonl")) as handle:
    for line in handle:
        e = json.loads(line)
        k = e.get("study_id", {}).get("pmid") or e.get("study_id", {}).get("doi")
        w = str(e.get("workflow", "")) + " " + " ".join(map(str, e.get("outputs") or []))
        if re.search(r"adv[-_]?(265|269|272|276)", w, re.I):
            done.add(k)

files, by_stem = [], {}
for d, sub, names in os.walk(os.path.join(held, "files")):
    sub[:] = [s for s in sub if not s.startswith(SEALED)]
    if any(x in d for x in SKIP):
        continue
    for n in names:
        p = os.path.join(d, n)
        files.append(p)
        by_stem.setdefault(os.path.splitext(n)[0].lower(), []).append(p)
        by_stem.setdefault(n.lower(), []).append(p)

old = {r["study_key"]: r["contained_in_held_bytes"] for r in csv.DictReader(open(containment), delimiter="\t")}
rows = [r for r in csv.DictReader(open(ranking), delimiter="\t")
        if r["study_key"] not in done and int(r["n_unread"]) > 0 and int(r["consumers_route2"]) > 0]


def rel(p):
    return os.path.relpath(p, held)


def is_supp(p):
    return "/supplement" in "/" + rel(p).lower() or bool(SUPP_RX.search(os.path.basename(p)))


def text_scan(p):
    ext = p.rsplit(".", 1)[-1].lower()
    try:
        if ext == "xml":
            found, _ = a219.scan_xml(p)
        elif ext == "pdf":
            found, _ = a219.scan_pdf(p)
        elif ext in ("html", "txt"):
            found = a219.scan_pages([open(p, errors="replace").read()])
        else:
            return {}
    except Exception:
        return {}
    return found or {}


result = []
for r in rows:
    key, unread = r["study_key"], r["unread_classes"].split(";")
    held_file = r["held_file"] if r["held_file"].startswith("/") else os.path.join(held, r["held_file"])
    pmc = set(re.findall(r"PMC(\d{5,9})", held_file))
    xmls = [held_file] if held_file.endswith(".xml") and os.path.exists(held_file) else []
    for x in xmls:
        m = re.search(r'<article-id pub-id-type="pmc(?:id)?">\s*(?:PMC)?(\d+)', open(x, errors="replace").read())
        if m:
            pmc.add(m.group(1))
    keys = ([key] if re.fullmatch(r"\d+", key) else []) + sorted(pmc)
    # route A: identifier path scan
    rx = [re.compile(r"(?<![0-9])" + k + r"(?![0-9])") for k in keys]
    mine = [p for p in files if any(x.search(rel(p)) for x in rx)]
    mine_text = [p for p in mine if p.lower().endswith((".xml", ".pdf", ".html", ".txt")) and not is_supp(p)]
    if held_file not in mine_text and os.path.exists(held_file):
        mine_text.append(held_file)
    a_hit = {}
    figs = [p for p in mine if p.lower().endswith(IMG) and not is_supp(p)
            and (MAIN_FIG_RX.search(os.path.basename(p)) or "/figures/" in "/" + rel(p))]
    pdfs = [p for p in mine_text if p.lower().endswith(".pdf")]
    if "figures" in unread and (figs or pdfs):
        a_hit["figures"] = (figs or pdfs)[:3]
    supp = [p for p in mine if p.lower().endswith(SUPP_EXT) and is_supp(p)]
    if "supplementary" in unread and supp:
        a_hit["supplementary"] = supp[:3]
    for c in TEXT_CLASSES:
        if c in unread:
            for p in mine_text:
                if c in text_scan(p):
                    a_hit[c] = [p]
                    break
    # route B: names the article's own XML declares
    all_xml = sorted(set(xmls + [p for p in mine_text if p.endswith(".xml")]))
    b_hit = {}
    declared = 0
    for x in all_xml:
        t = open(x, errors="replace").read()
        fig_names, supp_names = set(), set()
        declared = max(declared, len(re.findall(r"<fig[ >]", t)))
        for block in re.findall(r"<fig[ >].*?</fig>", t, re.S):
            fig_names |= set(re.findall(r'<(?:graphic|media)[^>]*href="([^"]+)"', block))
        for block in re.findall(r"<supplementary-material[ >].*?</supplementary-material>", t, re.S):
            supp_names |= set(re.findall(r'href="([^"]+)"', block))
        for label, names in (("figures", fig_names), ("supplementary", supp_names)):
            if label not in unread:
                continue
            for n in names:
                base = os.path.basename(n).lower()
                hits = by_stem.get(base) or by_stem.get(os.path.splitext(base)[0]) or []
                wanted = IMG if label == "figures" else SUPP_EXT
                # a short or generic declared name ("1.pdf", "Data_Sheet_1.pdf", "Table_2.xlsx") would match
                # another article's file: require the study's keys in the path
                stem = os.path.splitext(base)[0]
                generic = len(stem) < 8 or bool(re.fullmatch(r"(?:data_?sheet|table|image|video|movie|fig(?:ure)?|supp\w*|presentation)[-_ ]?s?\d*", stem))
                hits = [p for p in hits if p.lower().endswith(wanted)
                        and (not generic or any(k.search(rel(p)) for k in rx))]
                if hits:
                    b_hit.setdefault(label, []).extend(hits[:1])
        found = text_scan(x)
        for c in TEXT_CLASSES:
            if c in unread and c in found:
                b_hit[c] = [x]
    old_c = [] if old.get(key, "-") == "-" else old[key].split(";")
    wide = [c for c in unread if c in a_hit or c in b_hit]
    result.append({
        "study_key": key, "consumers": int(r["consumers_route2"]), "kinds": r["kinds"], "unread": r["unread_classes"],
        "old_rule": ";".join(old_c) or "-", "wider_rule": ";".join(wide) or "-",
        "route_A": ";".join(c for c in unread if c in a_hit) or "-",
        "route_B": (";".join(c for c in unread if c in b_hit) or "-") if all_xml else "no_xml",
        "files_A": ";".join(sorted({rel(p) for v in a_hit.values() for p in v}))[:600] or "-",
        "files_B": ";".join(sorted({rel(p) for v in b_hit.values() for p in v}))[:600] or "-",
        "declared_main_figs": declared, "declared_figs_found_by_name": len({os.path.splitext(os.path.basename(p))[0].lower() for p in b_hit.get("figures", [])}),
        "held_file": rel(held_file), "latest_event": r["latest_event"], "units": r["units"],
    })


def order(x):
    w = set(x["wider_rule"].split(";"))
    return (-x["consumers"], -len(w & {"tables", "figures", "supplementary"}), -int("discussion" in w), x["study_key"])


result.sort(key=order)
with open(out, "w") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(result[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(result)
qualify = [x for x in result if x["wider_rule"] != "-"]
print("studies excluded as read in ADV-265/269/272/276:", len(done))
print("fresh studies with consumers and an unread class:", len(result))
print("old rule:", sum(x["old_rule"] != "-" for x in result))
print("wider rule:", len(qualify), "| route A:", sum(x["route_A"] != "-" for x in result),
      "| route B:", sum(x["route_B"] not in ("-", "no_xml") for x in result),
      "| both routes:", sum(x["route_A"] != "-" and x["route_B"] not in ("-", "no_xml") for x in result),
      "| no XML (route B impossible):", sum(x["route_B"] == "no_xml" for x in result))
for c in ("discussion", "figures", "tables", "supplementary", "limitations"):
    print(" class", c, "wider", sum(c in x["wider_rule"].split(";") for x in result),
          "A", sum(c in x["route_A"].split(";") for x in result), "B", sum(c in x["route_B"].split(";") for x in result),
          "old", sum(c in x["old_rule"].split(";") for x in result))
for x in qualify[:16]:
    print(x["study_key"], "c=%d" % x["consumers"], "| unread", x["unread"], "| A", x["route_A"], "| B", x["route_B"])
