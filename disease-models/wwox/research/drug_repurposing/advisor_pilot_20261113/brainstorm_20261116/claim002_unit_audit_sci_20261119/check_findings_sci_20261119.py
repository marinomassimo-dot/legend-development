"""SCI 2026-11-19 (ADV-083): check the source words the blind delegate quoted in its findings against the held texts (post-delegate check, a post hoc step), and count a few terms.
Reads the three plain renderings in the scratch dir (argument 1); prints FOUND / NOT FOUND per quote and the term counts.   Run:  python3 -I check_findings_sci_20261119.py <scratch-dir>"""
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
D = Path(sys.argv[1])


def norm(s):
    return " ".join(s.replace("‐", "-").replace("‑", "-").replace("’", "'").replace("‘", "'").split())


S = {k: norm((D / f).read_text(encoding="utf-8")) for k, f in (("S21", "steinberg2021_plain.txt"), ("S26", "s26_clean.txt"), ("BR", "breton_plain.txt"))}
Q = [
    ("S21", "This resulted in supraphysiological expression of WWOX in all cell populations seen in COs and a partial rescue."),
    ("S21", "pAAVS-2aNeo-UBp-IRES-GFP plasmid cloned to carry the WWOX coding sequence was co-electroporated with px330 targeting the AAVS1 locus"),
    ("S26", "Neuronal activity was then measured through Ca2+ imaging, revealing that the firing rate of WOREE organoids was approximately 3-fold higher than that of SCAR12 organoids"),
    ("S21", "although microcephaly is seen in some patients, many other do not exhibit this condition"),
    ("S21", "Of note, we did not observe any statistically significant differences between WT and KO in the expression of these markers (Appendix Table S1)."),
    ("S21", "Overall, RNA-seq reveled impaired spatial patterning, axis formation, and cortical layering in WWOX-KO COs"),
    ("S21", "These results provide a proof of concept for successful reintroduction of WWOX as a mean for correcting the phenotype and possibly for therapeutic intervention"),
    ("S21", "The expression of VGLUT1 remained unchanged between the different lines."),
    ("S21", "Yet, our findings suggest the importance of optimizing population-targeted delivery and fine-tuning of expression levels for successful genetic therapy approaches in patients with WOREE syndrome."),
    ("S21", "although further study is required before clinical translation, our data serve as a proof of concept"),
    ("S21", "SCAR12 FOs exhibited very mild, if any, differences in the forebrain neuronal population development, astrocyte development, and DDR signaling."),
    ("S21", "Western blot analysis of week 24 COs"),
    ("S21", "This was further supported by immunoblot analysis of week 20 COs (Fig EV2A and B)."),
    ("S26", "suggesting that optimal therapeutic intervention may require stage and cell-type-specific targeting depending on disease progression."),
    ("S26", "Patient-derived organoids exhibited milder phenotypes compared to knockout organoids, showing functional neuronal impairments like hyperexcitability and delayed differentiation rather than RG dysfunction."),
    ("S26", "WWOX knockout organoids exhibiting the most pronounced phenotype, followed by WOREE and SCAR12 variants"),
    ("S26", "WWOX-KO and WOREE organoids showed a prominent increase in the relative number of total recognized RG cells (RGs) (Fig. 2D-F)"),
    ("S26", "only WWOX-KO and WOREE organoids exhibited significant reductions in SATB2+ and CTIP2+ neurons"),
    ("S26", "Importantly, the infection with AAV9-WWOX of WOREE organoids did not affect the RGs"),
    ("S26", "in contrast to what we observed in an earlier time point, where both organoids showed similar neuronal hyperactivity [Fig. 1B(i) and Fig. 1C]"),
    ("BR", "S-CTL 10.3 ± 11.5 Hz; S-KOs 8.4 ± 10.0 Hz"),
    ("BR", "we first evaluated the Synapsin-Cre Wwox knockout (S-KO) mouse brain"),
    ("BR", "13 to 17 day old"),
    ("S21", "1.76"),
    ("S21", "1.67"),
]
for s, q in Q:
    print("FOUND    " if norm(q) in S[s] else "NOT FOUND", s, q[:95])
print()
for s, k in (("S21", "calcium"), ("S21", "Ca2+"), ("S26", "Ca2+"), ("S26", "persist"), ("S26", "long-term"), ("S26", "durab"), ("S26", "cohort"), ("S26", "batch"), ("S26", "different differentiation"),
             ("S21", "depolariz"), ("S21", "microcephal"), ("S21", "proof of concept")):
    print(f"count {s} '{k}':", len(re.findall(re.escape(k), S[s], flags=re.I)))
for k in ("1.76", "1.67"):
    for m in list(re.finditer(re.escape(k), S["S21"]))[:1]:
        print(k, "->", S["S21"][max(0, m.start() - 160):m.end() + 120])
for m in list(re.finditer(r"cohort|batch", S["S26"], flags=re.I))[:6]:
    print("S26 cohort/batch ->", S["S26"][max(0, m.start() - 90):m.end() + 70])
