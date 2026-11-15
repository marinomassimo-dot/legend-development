# RP-004 (ADV-011): predictions frozen BEFORE the body text of the chosen paper is read

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Committed before any reader opens the body of PMID 18620777 (Hepatol/J Hepatol 2008, author manuscript PMC2574998). What is known when this is written: the abstract only (Europe PMC record, quoted in `README.md`) and the fact that the PMC article page serves the full text (size and section words counted, not read). Nobody has read the body.

Item chosen: P287, "The JNK inhibitor SP600129 [sic] enhances apoptosis of HCC cells induced by the tumor suppressor WWOX". The abstract states: forced WWOX in SNU387 cells increased apoptosis induced by staurosporine and the JNK inhibitor; WWOX shRNA in SNU449 cells increased proliferation and resistance to the inhibitor-induced apoptosis.

## Predictions about what the body will and will not show (each can be wrong; scored after reading)
| # | Prediction | Why it matters for a WWOX loss-of-function contrast |
|---|---|---|
| F1 | The gain arm (SNU387) and the loss arm (SNU449) are two DIFFERENT cell lines, not an isogenic pair | the "WWOX status" effect is then confounded with line identity |
| F2 | One inhibitor chemotype only (the anthrapyrazolone), at one or two concentrations, no dose-response curve | off-target kinase activity cannot be excluded |
| F3 | No genetic JNK control (no JNK1/2 knockdown or dominant-negative) | the effect cannot be assigned to JNK |
| F4 | JNK activity (phospho-c-Jun or phospho-JNK) is not shown to differ by WWOX status | the mechanism line "WWOX interacts with JNK1" is an inference, not measured here |
| F5 | Apoptosis is read by one or two assays on a small number of independent experiments, with modest effect sizes | transfer weight |
| F6 | No non-cancer or neuronal cell is used | transfer to neurons is unsupported by this paper |
| F7 | The paper reports an effect with the inhibitor alone on viability in the WWOX-high versus WWOX-low line that is NOT in the same direction as the combined staurosporine effect, or does not report it at all | whether "WWOX-low = resistance" is general or specific to the inhibitor |
Scoring rule fixed now: a prediction is HELD if the body states or clearly implies it; MISSED if the body states the opposite; NOT DETERMINABLE if the body is silent and cannot be checked. A rejected prediction is reported as such; no prediction is reworded after reading.

## The case-level predictions (about the world, for the later experiment; fixed now)
* P-a: in an isogenic WWOX-null versus rescued neural line, JNK-inhibitor-induced cell death is NOT lower in the null line once a second chemotype and a genetic JNK control are used (the HCC pattern is line-specific or off-target). Probability stated qualitatively: more likely than not.
* P-b: tau phosphorylation in the WWOX-deficient line falls with the same inhibitors (the IT47 INV-09 row E04 direction, Sze 2004, abstract level) AND does not require the apoptosis difference: the two readouts dissociate. Qualitatively: possible, not favoured.
These two are what the "rejecting experiment" in the case design can falsify; neither is a claim.
