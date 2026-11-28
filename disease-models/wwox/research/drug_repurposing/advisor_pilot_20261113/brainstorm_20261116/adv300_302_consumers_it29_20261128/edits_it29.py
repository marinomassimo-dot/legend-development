"""IT29: SCI's ADV-300 sentences J2, J3 and the card G01 target_expression correction, as exact-once fragment replacements (file, old, new, tag).
Applied only after the blind round in VERIFIER_REPORT_AS_DELIVERED_J_ETI_IT29.md (S2, S3, S4 as corrected there). J1 goes through batch_commit.py propagate (ops_claim016_it29.json). J4 (S5, S6) is NOT applied: the verifier's reply on those two was stopped by a safeguard and is not retried. Hypothesis level; nothing here is medical advice."""
TH = "disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md"
MAP = "disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv"
X = []
def f(path, old, new, tag): X.append(dict(path=path, old=old, new=new, tag=tag))
f(TH, "Tutte agiscono sul **trascritto endogeno, non allele-specificamente**.",
  "Tutte agiscono sul **trascritto endogeno, non allele-specificamente**. [IT 2026-11-28, ADV-300 J2] Una quarta leva, documentata solo sul trascritto e in linee tumorali: il lncRNA PARTICLE (il knockdown alza l'mRNA di WWOX, la sovraespressione lo abbassa; per la Figura 3A la legenda indica U2OS e la Discussione MDA-MB-361; il testo scrive «0.7 ± 0.1 fold increase» (media ± SEM secondo i Metodi) mentre le barre stanno a circa 1,9 contro 1,0; la legenda della Figura 3A non indica né n né il tipo di barra d'errore). Specificità allelica non testata (PMID 28769061).", "J2")
f(MAP, "returned a restricted stub and was not read.",
  "returned a restricted stub and was not read in that sweep. [IT 2026-11-28, ADV-300 J3] It was read on 2026-11-28 from the PMC XML (question-driven, queried_not_full_read): a commentary on PMID 42397075 that reports no measurement of its own, so it meets no trigger.", "J3")
ETI = "disease-models/wwox/research/drug_repurposing/view/research_reports/etifoxine.json"
f(ETI, "In the small adult focal epilepsy trial the reproduced crude IRR is 0.863 and the published interval includes no effect.",
  "In the small adult focal epilepsy trial the reproduced crude IRR is 0.863. The same Table 5.2 prints an efficacy of 13.7% with a 95% interval of -1.1% to 26.4%, which includes no effect, and beside it p = 0.027; the two do not agree and the table does not say which test gave the P value.", "ETI")
# Card G01, packet and card (JSON-escaped raw replacement, exact count)
G01_OLD = "GSK3beta is broadly expressed; total protein unchanged between genotypes in the printed densitometry."
G01_NEW = "Total GSK3beta in the printed densitometry (Figure 7c; legend: postnatal day 20, ratio to beta-actin) is 9, 13 and 18 per cent higher in Wwox-null than in wild-type cerebellum, hippocampus and cortex (one lane per genotype per region, no error bars, no test reported; the legend calls the blot representative of four independent experiments), so neither a change nor the absence of one is established."
G01_FILES = ["disease-models/wwox/research/drug_repurposing/cards/G01_lithium_gsk3.packet.json",
             "disease-models/wwox/research/drug_repurposing/cards/G01_lithium_gsk3.card.json"]
