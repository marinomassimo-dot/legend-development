"""SCI 2026-11-19 (ADV-084): confirm that every registry sentence quoted in the CLAIM 005 verdict note is present in CLAIM 005 of claim_registry_current.md
(markdown asterisks and backticks removed on both sides before matching). Prints FOUND / NOT FOUND per fragment.
Run:  python3 -I check_registry_sentences_claim005_sci_20261119.py <path to claim_registry_current.md>"""
import sys
from pathlib import Path

if len(sys.argv) != 2 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
text = Path(sys.argv[1]).read_text(encoding="utf-8")
a = text.index("## CLAIM 005\n")
b = text.index("\n---\n", a)


def clean(s):
    return " ".join(s.replace("*", "").replace("`", "").split())


C = clean(text[a:b])
FR = [
    "Reduced GABAergic interneurons and glial activation in WWOX-KO",
    "murino / Wwox-KO sistemico; genotipo caution: KO ≠ compound het; segnale GABAergico e gliale plausibilmente trasferibile come meccanismo generale di vulnerabilità",
    "In one systemic constitutive Wwox-KO mouse model at two weeks, PV-positive interneuron counts are lower in DG, CA1 and across the whole hippocampus (−44%), NPY-positive counts are lower in DG only",
    "IBA1/GFAP immunoreactive area fractions are higher in CA1, CA3 and whole hippocampus",
    "Marker-positive abundance and area fraction — not cell loss, not glial cell number.",
    "concordanza umana indipendente",
    "non il padj più basso della lista, che è di DACT2 a 2,29e-15",
    "Supports the glial axis as a modifier.",
    "The source measures no GABA concentration, no synaptic inhibition, no E/I ratio and no drug",
    "NPY CA1/CA3 are reported as showing no obvious difference; the whole-hippocampus NPY panel carries no significance marker — a visual panel observation, not a reported test.",
    "IBA1/GFAP in DG are marginal and unmarked.",
    "Il6 and Tnf-a transcripts are both more than 1.5-fold up by qPCR (p below 0.05, n=4/group).",
    "GAD65/67 is protein abundance only.",
    "Only Il6, not Tnf-a, is significant",
    "> 1.5 fold upregulation of both cytokines (significant at p < .05) in KO (n = 4)",
]
bad = 0
for f in FR:
    ok = clean(f) in C
    bad += (not ok)
    print("FOUND    " if ok else "NOT FOUND", f[:100])
print("not found:", bad)
