"""ADV-253 route 2: split canonical registries, ledgers, cards, tables and analysis files into one unit per record, row
or card, and report the units that carry an identifier of the retracted material or one of the value patterns.

Usage: python3 scan_records_adv253.py <repo root> <out.tsv>
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import csv, glob, os, re

repo, out = sys.argv[1:3]
W = os.path.join(repo, "disease-models/wwox")

IDS = re.compile(r"(?<!\d)(28045433|28151481|25447306|26041563|19357348|15240510|29337876|27023526|24434513|23660387|"
                 r"16840440|9683527)(?!\d)|DL-MECH-025|CORPUS-STUB-061|CORPUS P303\b|LIT-0085\b|LIT-0303\b|LIT-0401\b")
WWOX = re.compile(r"wwox", re.I)
VALUES = {
    "decitabine": re.compile(r"decitabin|5-aza-?2|\bdAza\b|aza-?deoxycytidine", re.I),
    "cell_1833": re.compile(r"\b1833\b(?=[^.\n]{0,60}(cell|clone|bone|metasta))|(cell|clone)s?[^.\n]{0,20}\b1833\b", re.I),
    "hgf_met_taz": re.compile(r"\bHGF\b|c-Met\b|HGF/Met|\bTAZ\b"),
    "hif1_bone": re.compile(r"HIF[-1\s]?1?[^\n]{0,200}bone metasta|bone metasta[^\n]{0,200}HIF", re.I),
    "hif1_stabilised": re.compile(r"(stabili[sz]\w*|sequest\w*)[^\n]{0,120}HIF|HIF[-1α]*[^\n]{0,80}stabili[sz]\w*[^\n]{0,120}(WWOX|Wwox)|HDM2[^\n]{0,120}(WWOX|Wwox)|(WWOX|Wwox)[^\n]{0,120}HDM2"),
    "bone_metastasis": re.compile(r"bone metasta|metastasi ossee|metastasi (all'|dell')?oss", re.I),
}
SKIP = re.compile(r"/(corpus_seed|fulltext_read_receipts|reading_state|batch_queue|coverage_report|locator_audits|"
                  r"session_evaluations|assignments|checkpoint|wm_history_split|working_model_history|discovery_ledger_history|"
                  r"join/|ranking\.json|adv253_)")


def units(path):
    t = open(path, errors="replace").read()
    if path.endswith(".json"):
        yield os.path.basename(path), 1, t
        return
    if path.endswith(".tsv"):
        for i, line in enumerate(t.split("\n"), 1):
            if line:
                yield line.split("\t")[0][:60], i, line
        return
    line_no = 1
    for part in re.split(r"(?m)^(?=#{1,4} )", t):
        if part.strip():
            yield part.split("\n")[0].lstrip("# ")[:90], line_no, part
        line_no += part.count("\n")


files = []
for pat in ("registries/*.md", "research/*.md", "research/commit_candidates/*.md", "analysis/**/*.md", "meta/*.md",
            "*.md", "research/drug_repurposing/*.md", "research/drug_repurposing/*.tsv",
            "research/drug_repurposing/cards*/*.card.json", "research/drug_repurposing/**/*.card.json",
            "research/drug_repurposing/ranking*/*.tsv"):
    files += glob.glob(os.path.join(W, pat), recursive=True)
rows, seen, n_units = [], set(), 0
for f in sorted(set(files)):
    rel = os.path.relpath(f, repo)
    if SKIP.search("/" + rel):
        continue
    for name, ln, body in units(f):
        n_units += 1
        ids = sorted({m.group(0) for m in IDS.finditer(body)})
        vals = []
        if WWOX.search(body):
            vals = [k for k, rx in VALUES.items() if rx.search(body)]
        if ids or vals:
            rows.append((rel.replace("disease-models/wwox/", ""), ln, name, ";".join(ids), ";".join(vals)))
with open(out, "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("file first_line unit identifiers value_patterns".split())
    for r in rows:
        w.writerow([c if c != "" else "-" for c in r])
print("files", len(files), "| units", n_units, "| units hit", len(rows), "| with an identifier", sum(bool(r[3]) for r in rows))
