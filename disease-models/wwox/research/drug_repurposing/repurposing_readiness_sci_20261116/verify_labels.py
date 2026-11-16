#!/usr/bin/env python3
"""Mechanical quote check of the readiness-sheet producer output against the raw public DailyMed label XML (generic client, default User-Agent).

    python3 verify_labels.py --help
    python3 verify_labels.py run <producer_dir> <out_dir>

Reads producer/signals.tsv and producer/sheets.tsv, fetches each setid named in `accessed_how` once from
https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/<setid>.xml , normalises whitespace/case/markup and checks each label-sourced quote
(minus a trailing '[fragment]' marker and ellipses) as a substring of the label text. Writes label_verify.tsv and label_text_sha256.tsv.
No e-mail address or other personal datum is sent; one GET per setid.
"""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, hashlib, re, time, urllib.request
from pathlib import Path
P, OUT = Path(sys.argv[2]), Path(sys.argv[3]); OUT.mkdir(parents=True, exist_ok=True)
def norm(s):
    s = re.sub(r"<[^>]+>", " ", s); s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#8217;", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[^a-z0-9%<>=.,;:()/'\"\- ]", " ", s.lower()); return re.sub(r"\s+", " ", s).strip()
sigs = list(csv.DictReader(open(P / "signals.tsv"), delimiter="\t"))
sheets = list(csv.DictReader(open(P / "sheets.tsv"), delimiter="\t"))
sid_re = re.compile(r"setid=([0-9a-f-]{36})")
texts, shas = {}, []
def get(sid):
    if sid not in texts:
        raw = urllib.request.urlopen(f"https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{sid}.xml", timeout=60).read()
        shas.append((sid, len(raw), hashlib.sha256(raw).hexdigest())); texts[sid] = norm(raw.decode("utf-8", "replace")); time.sleep(1)
    return texts[sid]
rows = []
for r in sigs:
    q = r["verbatim_sentence"]; m = sid_re.search(r["accessed_how"])
    if r["source_kind"] == "abstract" or not m or q.startswith("none found"):
        rows.append((r["agent"], r["signal_type"], r["source_kind"], "not label-checked here", q[:90])); continue
    qq = norm(re.sub(r"\s*\[(?:fragment|boxed[^\]]*)\]|\.\.\.|…", "", q)).rstrip(". "); 
    try: t = get(m.group(1)); ok = qq in t
    except Exception as e: rows.append((r["agent"], r["signal_type"], r["source_kind"], f"fetch failed: {type(e).__name__}", q[:90])); continue
    rows.append((r["agent"], r["signal_type"], r["source_kind"], "FOUND verbatim in label text" if ok else "NOT FOUND", q[:90]))
with open(OUT / "label_verify.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["agent", "signal_type", "source_kind", "result", "quote_start"]); w.writerows(rows)
with open(OUT / "label_text_sha256.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["setid", "xml_bytes", "sha256"]); w.writerows(shas)
import collections; print(collections.Counter(r[3] for r in rows))

# ---- second pass: quote-like fields of sheets.tsv against the same label XML, and PubMed abstracts by PMID (NCBI efetch, no contact parameter)
FIELDS = ["mechanism_sentence", "class_level_approved_indications", "bbb_statement", "pediatric_label_statement", "interaction_or_contraindication_class"]
pm_cache = {}
def abstract(pmid):
    if pmid not in pm_cache:
        raw = urllib.request.urlopen(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml", timeout=60).read()
        pm_cache[pmid] = norm(raw.decode("utf-8", "replace")); time.sleep(0.5)
    return pm_cache[pmid]
srows = []
for r in sheets:
    blob = " ".join(r.values()); sids = set(sid_re.findall(blob)) | set(re.findall(r"setid ([0-9a-f-]{36})", blob)); pm = set(re.findall(r"PMID (\d{6,8})", blob))
    for fld in FIELDS:
        v = r.get(fld, "")
        if not v or v.startswith(("not stated", "none found")):
            srows.append((r["agent"], fld, "not checked (empty/not stated)", v[:70])); continue
        parts = [p for p in re.split(r"\s*;\s*|\s+\[[^\]]*\]\s*", v) if len(p) > 25]
        for p in parts:
            qq = norm(re.sub(r"\.\.\.|…", "", p)).rstrip(". ")
            src = "label" if any(qq in get(s) for s in sids) else ("abstract" if any(qq in abstract(x) for x in pm) else None)
            srows.append((r["agent"], fld, f"FOUND in {src}" if src else "NOT FOUND", p[:90]))
with open(OUT / "sheet_verify.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["agent", "field", "result", "quote_start"]); w.writerows(srows)
print(collections.Counter(x[2] for x in srows))
