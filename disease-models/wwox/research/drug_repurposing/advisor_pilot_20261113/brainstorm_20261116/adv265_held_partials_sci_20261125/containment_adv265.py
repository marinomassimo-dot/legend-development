"""ADV-265: for ranked held partials, which unread classes do the held bytes contain? (frozen rule: ADV-219 scan)
Usage: python3 containment_adv265.py <repo root> <root checkout> <ranking_adv265.tsv> <out tsv> [top N]"""
import sys
if len(sys.argv) < 5 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, glob, importlib.util, os, re
repo, held, rank, out = sys.argv[1:5]; topn = int(sys.argv[5]) if len(sys.argv) > 5 else 40
A = os.path.join(repo, "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv219_receipt_label_audit_sci_20261124/labelling_flags_adv219.py")
sp = importlib.util.spec_from_file_location("a219", A); a = importlib.util.module_from_spec(sp); sp.loader.exec_module(a)
rows = list(csv.DictReader(open(rank), delimiter="\t"))
res = []
for r in rows:
    if r["unread_classes"] == "-" or int(r["consumers_route2"]) == 0: continue
    f = os.path.join(held, r["held_file"]) if not r["held_file"].startswith("/") else r["held_file"]
    ext = f.rsplit(".", 1)[-1].lower()
    found, err = ({}, "not scanned")
    if os.path.exists(f):
        if ext == "xml": found, err = a.scan_xml(f)
        elif ext == "pdf": found, err = a.scan_pdf(f)
        else:
            try: found, err = a.scan_pages([open(f, errors="replace").read()]), None
            except Exception as ex: found, err = {}, str(ex)
    found = found or {}
    key = r["study_key"]
    supp = []
    if re.fullmatch(r"\d+", key):
        for sub in ("files/supplement", "files/fulltext", "files/deepening_downloads"):
            for p in glob.glob(os.path.join(held, sub, "**", "*"), recursive=True):
                b = os.path.basename(p)
                if ("PMID" + key in b or "PMC" in b and key in b) and a.SUPP_NAME_RX.search(b): supp.append(os.path.relpath(p, held))
    cont = []
    for c in r["unread_classes"].split(";"):
        if c in found or (c == "supplementary" and supp): cont.append(c)
    res.append((key, r["consumers_route2"], r["unread_classes"], ";".join(cont) or "-", ext, err or "-", ";".join(supp)[:120] or "-", r["held_file"][-70:]))
    if len(res) >= topn: break
with open(out, "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n"); w.writerow("study_key consumers unread_classes contained_in_held_bytes ext scan_error supplement_files held_file".split()); w.writerows(res)
for x in res[:topn]: print(x[0], "c=%s" % x[1], "unread:", x[2], "| contained:", x[3], "|", x[4], x[5][:30])
