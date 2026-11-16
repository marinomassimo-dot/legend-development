#!/usr/bin/env python3
"""Boxed-warning screen of public DailyMed labels for agents OUTSIDE the antiseizure set that act on the I1/I3/I6 chain links.
    python3 outside_set_label_screen.py --help
    python3 outside_set_label_screen.py run <out_tsv> <xml_dir>
One search GET and one XML GET per agent (public DailyMed v2 API, generic client). Records the label title, set id, whether a boxed-warning
section (LOINC 34066-1) exists, its first 200 characters, and the sha256 of the XML. It screens ONLY for the boxed warning: no boxed warning is
NOT 'safe' (flag = unassessed beyond the screen, treat as at least yellow). Mechanism-level labels, no recommendation. Not medical advice."""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, hashlib, json, os, re, time, urllib.parse, urllib.request
AG = [("bumetanide", "NKCC1 (loop-diuretic class)"), ("furosemide", "NKCC1 (loop-diuretic class)"), ("acetazolamide", "carbonic anhydrase (alters HCO3-/Cl- handling)"),
      ("caffeine citrate", "adenosine A1/A2A antagonism"), ("ivabradine", "HCN (If) blockade"), ("ganaxolone", "neurosteroid GABA-A PAM"),
      ("vigabatrin", "GABA-transaminase inhibition (tonic GABA up)"), ("tiagabine", "GAT-1 (tonic GABA up)"), ("dipyridamole", "adenosine uptake (ENT) inhibition"),
      ("lacosamide", "slow sodium-channel inactivation"), ("ethosuximide", "T-type"), ("levetiracetam", "SV2A (release)")]
os.makedirs(sys.argv[3], exist_ok=True)
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u), timeout=90).read()
rows = []
for name, link in AG:
    try:
        j = json.loads(get("https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?pagesize=10&drug_name=" + urllib.parse.quote(name)))
        hit = [d for d in j["data"] if name.split()[0].lower() in d["title"].lower()]
        if not hit:
            rows.append((name, link, "NO LABEL FOUND", "", "", "", "")); continue
        d = hit[0]; raw = get(f"https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{d['setid']}.xml"); time.sleep(0.5)
        open(f"{sys.argv[3]}/{d['setid']}.xml", "wb").write(raw)
        t = raw.decode("utf8", "replace")
        m = re.search(r'<section[^>]*>\s*<id[^>]*/>\s*<code code="34066-1".*?</section>', t, re.S)
        txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(0))).strip()[:200] if m else ""
        rows.append((name, link, d["title"][:90], d["setid"], "yes" if m else "no", txt, hashlib.sha256(raw).hexdigest()[:16]))
    except Exception as e:
        rows.append((name, link, "ERROR " + str(e)[:60], "", "", "", ""))
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["agent", "link_acted_on", "label_title", "setid", "boxed_warning_section", "boxed_first_200_chars", "xml_sha256_16"]); w.writerows(rows)
for r in rows: print(r[:5])
