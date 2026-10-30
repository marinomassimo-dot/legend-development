#!/usr/bin/env python3
"""IT10 P2.1 task 2: US label text (openFDA drug/label, key-less, no contact string) for the marketed alternatives: seizure, paediatric, CNS and embryo-fetal statements.
A zero is 'no hit for the pattern in the fetched sections on that date'. Usage: python3 -I labels_it10_p21.py <raw_dir>"""
import csv, hashlib, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
RAW = Path(sys.argv[1]); RAW.mkdir(parents=True, exist_ok=True); HERE = Path(__file__).resolve().parent
NAMES = {"daprodustat": "daprodustat", "vadadustat": "vadadustat", "belzutifan": "belzutifan", "topotecan": "topotecan", "digoxin": "digoxin", "roxadustat": "roxadustat", "molidustat": "molidustat", "enarodustat": "enarodustat", "desidustat": "desidustat"}
PAT = re.compile(r"seizure|convuls|epilep|encephalopath|brain|CNS|central nervous", re.I)
rows = []; snip = []
for k, n in NAMES.items():
    url = "https://api.fda.gov/drug/label.json?" + urllib.parse.urlencode({"search": f'openfda.generic_name:"{n}"', "limit": 3})
    try:
        try:
            b = urllib.request.urlopen(url, timeout=60).read()
        except Exception:
            # fallback: free-text search on the name (the structured field is not populated for every label)
            url = "https://api.fda.gov/drug/label.json?" + urllib.parse.urlencode({"search": n, "limit": 3})
            b = urllib.request.urlopen(url, timeout=60).read()
        (RAW / f"{k}.json").write_bytes(b); d = json.loads(b)
        if n.lower() not in " ".join(d["results"][0].get("openfda", {}).get("generic_name", [])).lower(): raise ValueError("generic_name of the first record does not carry the name (a combination or unrelated label); rejected")
    except Exception as e:
        rows.append([k, getattr(e, "code", "ERR"), 0, "", "", "", "", "NO_US_LABEL_FOUND_openFDA (absent from this source; not a statement about approval elsewhere)"]); time.sleep(1); continue
    for rec in d["results"][:1]:
        eff = rec.get("effective_time"); brand = ";".join(rec.get("openfda", {}).get("brand_name", []))
        secs = {s: " ".join(rec[s]) for s in rec if isinstance(rec[s], list) and s not in ("openfda",) and rec[s] and isinstance(rec[s][0], str)}
        hits = {s: len(PAT.findall(t)) for s, t in secs.items() if PAT.search(t)}
        ped = secs.get("pediatric_use", "")[:600]
        sez = [m.group(0) for m in re.finditer(r"[^.]*\b(seizure|convuls)[^.]*\.", " ".join(secs.values()), re.I)]
        rows.append([k, 200, len(secs), eff, brand, ";".join(f"{s}:{c}" for s, c in sorted(hits.items())), ped.replace("\t", " "), f"seizure_sentences={len(sez)}"])
        for s in sez[:6]: snip.append([k, eff, s.strip()[:400]])
    time.sleep(0.5)
with (HERE / "labels_us_it10_p21.tsv").open("w", newline="") as h:
    c = csv.writer(h, delimiter="\t"); c.writerow(["compound", "http", "n_sections", "label_effective_time", "brand", "sections_with_CNS_or_seizure_terms:count", "pediatric_use_text_first600", "note"]); c.writerows(rows)
with (HERE / "labels_us_seizure_sentences_it10_p21.tsv").open("w", newline="") as h:
    c = csv.writer(h, delimiter="\t"); c.writerow(["compound", "label_effective_time", "sentence_containing_seizure_or_convulsion_(first400)"]); c.writerows(snip)
print(open(HERE / "labels_us_it10_p21.tsv").read()[:3000])
