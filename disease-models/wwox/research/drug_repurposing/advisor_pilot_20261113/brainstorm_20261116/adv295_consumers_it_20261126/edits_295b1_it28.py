"""IT28: SCI's ADV-295 block 1 sentences (SENTENCES_FOR_IT_ADV295_BLOCK1_SCI_20261126.md, sections A and B) as fragment replacements in the ledger, the claim registry and the portfolio.
(file, old_fragment, new_fragment, tag). Applied only after a blind round and through a BATCH_COMMIT candidate for the two scientific current files. Hypothesis level; nothing here is medical advice."""
LED = "disease-models/wwox/research/discovery_ledger_current.md"
CLM = "disease-models/wwox/registries/claim_registry_current.md"
POR = "disease-models/wwox/research/drug_repurposing/research_portfolio.tsv"
X = []
def f(path, old, new, tag): X.append(dict(path=path, old=old, new=new, tag=tag))
f(LED, "so **Wnt direction in neural tissue is model-dependent**",
  "so, in this study, the direction of the Wnt-activation effect is the same in both models (Axin2 fell in the epileptogenic zone and was restored to baseline by the GSK3 inhibitor in both; remodelling was reduced in both) and only the number of remodelling markers that respond differs; a model-dependent Wnt direction is not shown by this paper (immature dentate granule cells, mouse, about 2 weeks after kainate, one dose); in the contralateral dentate gyrus Axin2 did not fall although remodelling occurred and was reduced by the drug, so Axin2 restoration does not account for every effect", "A1")
f(LED, "(the ipsilateral count unchanged)",
  "(the ipsilateral immature (POMC-GFP+) cell density, which kainate reduced markedly relative to saline controls (Fig 3E), was not significantly changed by the drug; n = 6 per group per Methods 2.8)", "A1-add1")
f(LED, "histology and immunohistochemistry at day 14 only",
  "histology and immunohistochemistry at day 14 only for the epilepsy-model outcomes (plus a single-dose Axin2 time course at 3 h and 24 h, and body weight over the treatment period reported only as no effect, with Supplemental Figure 1)", "A1-add2")
f(LED, "compounds that *«potentially increase»* WWOX expression", "compounds *«potentially increasing»* WWOX expression", "A2a")
f(LED, "cell type, dose, species and readout (transcript or protein) are unknown",
  "cell type, dose and readout (transcript or protein) are not given in the deposited sheet (nor in the paper's main text); the species is Homo sapiens in every row of the sheet", "A2b")
f(LED, "valproate LOWERS WWOX expression in human cells", "valproate LOWERS WWOX expression in Homo sapiens (cell or tissue type not given; per the deposited sheet)", "A2c")
f(POR, "matrix pyruvate sensor in mouse neurons and HEK cells",
  "matrix pyruvate sensor (mtPyronicSF; CaMKII-mtPyronicSF in axons) in cultured Sprague-Dawley rat neurons and human HEK293 cells; mouse tissue is used in the paper only for the 13C3-pyruvate infusion, the Sirt3-/- brain immunoprecipitation and the MPC1 cDNA", "A3")
f(CLM, "**Not examined:** the remaining WWOX allele (exome was done in six other patients), RNA, protein, follow-up.",
  "**Not examined (as far as the paper reports):** the remaining WWOX allele; no WWOX sequence result is given. Exome sequencing was done in six selected patients, of whom four are named (P7, P16, P17, P18) and two are not; whether this patient was one of them is not stated. No RNA, protein or follow-up is reported.", "B1")
f(POR, "and the sensor and ATP readouts were never in the same cultures",
  "and the paper's main text and Fig 2 legends do not state whether the sensor datasets (Fig 2F,G; n = 12 to 18 neurons) and the ATP datasets (Fig 2I,J; n = 9 neurons) came from the same cultures; no culture count is given in the Fig 2 legends and no paired measurement is shown (Table S3, which lists 3 cultures for each in SCI's reading, is not in the text the blind reader had)", "B2")
f(LED, "the absence is DRG-specific, not article-wide",
  "incidence and severity are summarised (Fig 6C) for brain only; the absence of tabulated incidence applies to every non-brain site the text lists as affected, DRG among them", "B3")
