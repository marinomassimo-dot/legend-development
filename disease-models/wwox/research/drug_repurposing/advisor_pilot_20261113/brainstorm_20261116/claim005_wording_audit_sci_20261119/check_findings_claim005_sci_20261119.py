"""SCI 2026-11-19 (ADV-084): check the source words the blind delegate quoted in its CLAIM 005 findings against the held texts (post-delegate check, a post hoc step), recount a few terms,
and recompute the padj ranking over Expanded View Tables EV1 and EV2 of Steinberg 2021 (the derived text's first column names the table).
Run:  python3 -I check_findings_claim005_sci_20261119.py <scratch-dir>   (scratch-dir holds hussain2019_plain.txt and steinberg2021_plain.txt)"""
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
D = Path(sys.argv[1])


def norm(s):
    return " ".join(s.replace("‐", "-").replace("‑", "-").replace("’", "'").replace("‘", "'").split())


S = {"S19": norm((D / "hussain2019_plain.txt").read_text(encoding="utf-8")), "S21": norm((D / "steinberg2021_plain.txt").read_text(encoding="utf-8"))}
Q = [
    ("S19", "A significantly low number of PV+ interneurons in Wwox KO mice was also evident in the CA1 and CA3 subfields (Figs. 1 A2–A3, B2–B3, and C2–C3)."),
    ("S19", "Our analysis also shows that the overall number of NPY+ interneurons is reduced in the DG region of Wwox KO mice."),
    ("S19", "A significant reduction in the number of NPY+ cells is apparent in the DG subfield of a Wwox KO mouse (B1)"),
    ("S19", "Wwox KO mice hippocampi exhibit increase in IBA-1+ cells indicating microglia activation."),
    ("S19", "The area occupied by the IBA-1+ or GFAP+ structures (i.e., area fraction) in the binary image was quantified"),
    ("S19", "The finding of biomarkers of neuroinflammation in Wwox KO mice brains supports the idea that inflammation might play a role in Wwox related epilepsy. However, further investigation is needed to gather additional mechanistic insight on what is cause or consequence upon Wwox loss of function."),
    ("S19", "Activated microglia and astrogliosis, are among the most evident deleterious changes affecting hippocampus function as a consequence of epileptic seizures"),
    ("S19", "gliosis"),
    ("S21", "1,246 genes were upregulated in WWOX-KO COs and showed both a fold change greater than 1.2 (FC > 1.2) and a significant P-value (P < 0.01), and 1,021 genes were downregulated (FC < 1/1.2, P < 0.01)"),
    ("S21", "we noticed a marked increase in GABAergic markers. This finding is even more surprising when considering the decrease in GABA receptor components seen by RNA-seq."),
]
for s, q in Q:
    print("FOUND    " if norm(q) in S[s] else "NOT FOUND", s, q[:100])
print()
for s, k in (("S19", "modifier"), ("S19", "cause"), ("S19", "consequence"), ("S19", "significant at p"), ("S19", "Il6"), ("S19", "Tnf"), ("S19", "litter"), ("S19", "cell number"),
             ("S21", "NPY"), ("S21", "neuropeptide")):
    print(f"count {s} '{k}':", len(re.findall(re.escape(k), S[s], flags=re.I)))
rows = [x.rstrip("\n").split("\t") for x in Path("/home/desktop/legend-development/files/fulltext/PMID34268881_assets/Table_EV1_EV2_derived.txt").read_text(encoding="utf-8").splitlines()]
v = []
for r in rows:
    if len(r) >= 7 and r[0] in ("EV1_up", "EV2_down"):
        try:
            v.append((float(r[5]), r[2], r[0], r[6]))
        except ValueError:
            pass
v.sort()
print("rows:", len(v), "| lowest padj overall:", v[:4])
for tab in ("EV1_up", "EV2_down"):
    print(tab, "lowest padj:", [x for x in v if x[2] == tab][:3])
