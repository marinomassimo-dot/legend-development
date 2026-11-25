"""IT 2026-11-25 (IT23): dated corrections and notes on the ledger, one dossier and the R1 research note, by the ordinary route (none of the four scientific current files).
Idempotent: each edit is (file, old, new); skipped when new is already present. Run from the repository root. Hypothesis level; nothing here is medical advice."""
import importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("edits_it23", HERE / "edits_it23.py")
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
W = Path("disease-models/wwox/research")
LED = W / "discovery_ledger_current.md"; R1 = W / "repurposing_10h_scientist-a_20261021.md"; DOS = W / "fulltext_dossiers/PPR1015434.md"
CQ = ("[IT 2026-11-25, ADV-281: neither paper gives an activity check for chloroquine (searched chloroquine, CQ, LC3, p62, SQSTM, lysotracker, lysosom, autophag, bafilomycin and NH4Cl over both article XMLs and the supplement PDFs; xlsx source data not searched; "
      "the only lysosomal readout is mt-Keima with bafilomycin, a mitophagy-reporter control), so this null does not show that lysosomal degradation was blocked in these cells.]")
S38 = ("[cell-line identity, 2026-11-25: the cell models of PMID 28708106 are HepG2, which Cellosaurus 57.0 registers as misclassified (a hepatoblastoma, not a hepatocellular carcinoma line, CVCL_0027), and the mouse hepatoma line Hepa 1-6 (CVCL_0327, no problematic-line flag), "
       "plus Hepa 1-6 tumour-bearing mice; label only: no other human liver line is used, and the direction of the finding is unchanged.]")
DOS_OLD = "Glial knockdown with neuronal Aβ42: lifespan\n22 vs 24 days (p = 0.0095), locomotion unaffected — hence **neuronal, not glial, Wwox is the\nrelevant pool** for amyloid toxicity."
DOS_NEW = "Glial knockdown with neuronal Aβ42: " + E.CLAIM_NOTES["S36 (preprint dossier doi 10.1101/2025.05.01.651195, PPR1015434)"][0].replace("Neuronal more than glial", "neuronal more than glial", 1) + " [IT 2026-11-25, ADV-280: replaces «hence neuronal, not glial, Wwox is the relevant pool»; blind check.]"
EDITS = [
    (LED, E.DL058_OLD, E.DL058_NEW),
    (LED, "testo, otto figure, legenda PDF e tre video letti integralmente. Dossier: `staging/deepdive_PMID35883580_Liu2022.md`.",
     "testo, otto figure, legenda PDF e tre video letti integralmente. Dossier: `staging/deepdive_PMID35883580_Liu2022.md`. [IT 2026-11-25, ADV-280: the receipts record the figures (FTR-20261019-35883580-01 captions only; FTR-20261125-35883580-01 read) and the supplementary material not read; none records reading the three videos, so «tre video letti integralmente» has no receipt behind it.]"),
    (LED, "- **Evodiamina (PMID 28708106):** `parked`; aumenta WWOX protein in modelli HCC, ma l'effetto è citotossico, solo parzialmente WWOX-dipendente, senza target engagement/BBB/PK/safety pediatrica. Potrebbe aumentare Q230P misfolded.",
     "- **Evodiamina (PMID 28708106):** `parked`; aumenta WWOX protein in modelli HCC, ma l'effetto è citotossico, solo parzialmente WWOX-dipendente, senza target engagement/BBB/PK/safety pediatrica. Potrebbe aumentare Q230P misfolded. " + S38),
    (R1, "BiP is raised in wild type and not in the mutant.", "BiP is raised in wild type and not in the mutant. " + E.CLAIM_NOTES["S40 (research note R1, PMID 38731820)"][0]),
    (R1, "half of pathogenic variants wild-type-abundant (38378758);", "half of pathogenic variants wild-type-abundant (38378758) " + E.CLAIM_NOTES["S39 (research note R1, Premise 0 row)"][0] + ";"),
    (R1, "chloroquine shows no substantial change and the traces coincide (Figure 3A-C) [REPAIRED 2026-10-22].", "chloroquine shows no substantial change and the traces coincide (Figure 3A-C) [REPAIRED 2026-10-22]. " + CQ),
    (R1, "(Figure 4, read from the image).", "(Figure 4, read from the image). " + CQ),
    (DOS, DOS_OLD, DOS_NEW),
]
if __name__ == "__main__":
    for p, old, new in EDITS:
        t = p.read_text(encoding="utf-8")
        if new in t: print("already", p.name, old[:40]); continue
        assert t.count(old) >= 1, (p, old[:60])
        n = t.count(old); assert n == 1 or old == "(Figure 4, read from the image).", (p, n, old[:50])
        p.write_text(t.replace(old, new, 1), encoding="utf-8"); print("done", p.name, old[:40])
