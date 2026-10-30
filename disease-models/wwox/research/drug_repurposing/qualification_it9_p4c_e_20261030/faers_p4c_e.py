#!/usr/bin/env python3
"""IT9 P4c-e: openFDA adverse-event report counts for seizure terms (reports, not incidence; no denominator of exposure). Plain search endpoint (the count endpoint needs a key).
  faers_p4c_e.py --help | run
Writes faers_seizure_counts.tsv. Reuses the IT8 P3 retry layer. No key, no e-mail."""
import sys, time, importlib.util, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
NAMES = ["nirogacestat", "roxadustat"]
TERMS = ["Seizure", "Convulsion", "Epilepsy", "Status epilepticus", "Generalised tonic-clonic seizure"]
if len(sys.argv) < 2 or sys.argv[1] != "run":
    print(__doc__); sys.exit(0)
spec = importlib.util.spec_from_file_location("pq", HERE.parent / "pharmacological_qualification_it8_p3_20261029" / "pharm_qualify.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
net = m.Net()
q = urllib.parse.quote
rows = [["drug", "reaction_term", "http", "reports"]]
for n in NAMES:
    base = f'patient.drug.openfda.generic_name:"{n}"'
    s, p = net.get(f"https://api.fda.gov/drug/event.json?search={q(base)}&limit=1")
    rows.append([n, "(all reports)", s, (p.get("meta", {}).get("results", {}).get("total") if isinstance(p, dict) else "")])
    for t in TERMS:
        time.sleep(1)
        s, p = net.get(f"https://api.fda.gov/drug/event.json?search={q(base + ' AND patient.reaction.reactionmeddrapt:\"' + t + '\"')}&limit=1")
        rows.append([n, t, s, (p.get("meta", {}).get("results", {}).get("total") if isinstance(p, dict) and s == 200 else ("0" if s == 404 else ""))])
with open(HERE / "faers_seizure_counts.tsv", "w") as f:
    for r in rows: f.write("\t".join(str(x) for x in r) + "\n")
with open(HERE / "faers_service_log.tsv", "w") as f:
    f.write("attempt\tstatus\tseconds\turl\n")
    for l in net.log: f.write(f"{l['attempt']}\t{l['status']}\t{l['seconds']}\t{l['url']}\n")
print(open(HERE / "faers_seizure_counts.tsv").read())
