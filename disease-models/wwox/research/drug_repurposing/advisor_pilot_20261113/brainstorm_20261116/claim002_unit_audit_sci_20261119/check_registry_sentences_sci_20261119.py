"""SCI 2026-11-19 (ADV-083): confirm that every registry sentence quoted in the verdict note's section 6 is present in CLAIM 002 of claim_registry_current.md
(markdown asterisks and backticks removed on both sides before matching). Prints FOUND / NOT FOUND per fragment.
Run:  python3 -I check_registry_sentences_sci_20261119.py <path to claim_registry_current.md>"""
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
text = Path(sys.argv[1]).read_text(encoding="utf-8")
a = text.index("## CLAIM 002\n")
b = text.index("\n---\n", a)
claim = text[a:b]


def clean(s):
    return " ".join(s.replace("*", "").replace("`", "").split())


C = clean(claim)
FR = [
    "WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype",
    "WWOX-deficient organoids show hyperexcitability and altered Ca²⁺ dynamics; WWOX re-expression improves the phenotype.",
    "P1 — Ca²⁺ / network dysregulation; P7 — gene therapy readiness",
    "cioè disfunzione del compartimento inibitorio misurata a livello di trascritto e di proteina",
    "ampiezza sIPSC dimezzata",
    "Astrogenesi aumentata per immunofluorescenza, immunoblot (settimana 20) e qPCR",
    "difetto DDR con perdita del checkpoint apoptotico",
    "attivazione Wnt; dyslamination corticale; firma OXPHOS↓/glicolisi↑; firing aumentato e normalizzato dal rescue",
    "Il rescue del modello con variante splice c.517-2A>G prova che la reintroduzione di WWOX può correggere più domini cellulari",
    "the rescue normalises two of three layer markers and overshoots the third",
    "The model does not reproduce the microcephaly seen in some patients",
    "Dorsal/ventral identity is unchanged but not uniformly so",
    "umano organoide WWOX-KO + WOREE-derived",
    "Strongly supports the network-level model, la terapia genica e l'uso degli organoidi come piattaforma sperimentale.",
    "infection at week 10 on a hyperactivity seen at week 7 in a different organoid cohort",
    "Steinberg et al., 2024 preprint; Steinberg et al., 2021, EMBO Molecular Medicine, full text reviewed",
]
bad = 0
for f in FR:
    ok = clean(f) in C
    bad += (not ok)
    print("FOUND    " if ok else "NOT FOUND", f[:100])
print("not found:", bad)
