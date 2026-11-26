# Blind report, ADV-282 increment 6 (verbatim, SCI 2026-11-26)

Delegate: legend-delegate, model sonnet, effort high stated in the dispatch; census of its transcript: 10 {'high': 10} {'claude-sonnet-5-5': 10} 25135 449099 75793 (turns, effort, model, output tokens, cache-read, peak context). Delivered by its SubagentHandback call and copied byte for byte from the delegate transcript (subagents/agent-a5832ca1bb1bee8da.jsonl). Packet: `BLIND_SENTENCES_ADV282_INC6_SCI_20261126.md` (sha256 fa01c962...). My first reading was frozen before the report (FIRST_READ_ADV282_INC6_SCI_20261126.tsv, sha256 0b97de9f...). Dispatch deviation: the increment 6 dispatch added one clarifying phrase to the rule (an effect of the same compound on the study own outcome endpoint is not an engagement check); increments 4 and 5 were dispatched with the PREREG wording, which counts a dose-response of the same compound.

---

BLIND VERIFIER REPORT, ADV-282 increment 6 (7 blocks). Network not used, no e-mail sent, nothing written in the repository. Scratch script: /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/rna4.py. Python was run with -I -P -E, standard library only.

Note on the class for abstract rows. Abstract silence is never counted as absence. Where an abstract itself reports an engagement readout, I classed it on that readout and said what the abstract does not let me match (dose, cohort, tissue).

======== DR-I01-006 (Stacpoole 2006, PMID 16651305, abstract)
class: CHECK PRESENT (abstract level). Manipulation: DCA 12.5 mg/kg every 12 h for 6 months in children and young people with congenital lactic acidosis. The abstract reports "a fall in plasma clearance of the drug" with chronic dosing, which is a drug-handling measurement in the same patients. It gives no concentration values.
in_study_check: yes.
other_effect: yes. DCA "significantly decreased the rise in blood lactate caused by carbohydrate feeding" (OUTCOME section). Blood lactate is listed among the study's own outcomes, so I record it separately and do not count it as an engagement check. DCA also raised urinary maleylacetone and delta-aminolevulinate (OUTCOME section).
check locator: OUTCOME paragraph, sentences 2 and 3.
verdict: ADD.
findings:
- "Lactate persistently or intermittently raised" is correct (METHODS: "persistent or intermittent hyperlactatemia").
- "Defined defect in most patients" is true but understates. METHODS lists PDH deficiency 11, respiratory-chain defects 25 and mtDNA mutation 7. These sum to 43, which is every enrolled patient (assuming the groups are exclusive).
- "Did not change the clinical outcomes measured over six months" is supported. OUTCOME reports no significant difference in Global Assessment of Treatment Efficacy, linear growth, or frequency or severity of intercurrent illnesses. CONCLUSIONS says it "did not improve neurologic or other measures of clinical outcome". The abstract states "no significant difference", not "no change".
- The note does not say that DCA did lower postprandial lactate (biochemical effect present, clinical effect absent). A reader needs this to read the null correctly.
- The abstract reports no subgroup result for the 11 PDH-deficient patients, so "does not exclude a benefit in a defined genotype" is an inference, not a held finding.
- Design facts a reader needs, all from METHODS: 43 patients aged 0.9 to 19 years (not only "children"), 6 months of placebo preconditioning, then 6 months of DCA or placebo.
proposed wording: "A population with persistent or intermittent hyperlactatemia and a classified defect in all 43 enrolled patients (11 PDH deficiency, 25 respiratory-chain, 7 mtDNA), aged 0.9 to 19 years. DCA 12.5 mg/kg twice daily for 6 months blunted the postprandial lactate rise but gave no significant difference in global assessment, linear growth or intercurrent illness. Heterogeneous and short; the abstract reports no PDH-only subgroup result, so the null does not exclude a benefit in a defined genotype."

======== DR-I01-001 (Durie 2018, PMID 29913407, abstract)
class: CHECK PRESENT BUT NOT MATCHED, at abstract level. The abstract reports PDH activity, Ser300 phosphorylation and PDH protein after DCA in chronic-stage pilocarpine mice. It does not give which dose (50 or 100 mg/kg/day) or which cohort was assayed, and it does not name the tissue. The row field "brain" is not in the abstract; MeSH lists only "Mitochondria".
in_study_check: yes (the PDH measures are the row's own endpoint).
other_effect: yes. DCA was "slightly proconvulsant in the 6 Hz test". DCA lowered total PDH by 23% in No SE mice.
check locator: abstract sentences "In mice that had experienced pilocarpine-induced SE ... PDH activity was reduced by 65% ... partially alleviated with DCA" and "PDH protein ... decreased by 37% and phosphorylation at Ser300 ... increased by 52% in SE mice, but were not significantly changed with DCA".
verdict: ADD.
findings:
- "Partial" is supported: PDH activity was reduced 65% in SE versus No SE and "partially alleviated" by DCA. The abstract gives no statistics for that restoration.
- "Phospho-site did not move significantly" is supported. Ser300 phosphorylation was "not significantly changed with DCA" in SE mice, as was PDH protein.
- "Total PDH fell 23% in non-epileptic mice on treatment" is supported (No SE mice).
- "The authors offer it as a reason for the pro-convulsant signal" is supported ("may explain the proconvulsant effects in the 6 Hz test"). But the signal is specific to the 6 Hz test and described as "slight". The note's generic "pro-convulsant signal" hides this.
- The abstract does not give the DCA dose for the biochemical assays or the tissue.
proposed wording: "In chronic-stage pilocarpine mice, PDH activity was 65% lower than in No SE mice and DCA only partly alleviated this (no statistics in the abstract). Ser300 phosphorylation and PDH protein, both altered in SE mice, were not significantly changed by DCA. DCA lowered total PDH by 23% in No SE mice, which the authors suggest may explain the slight pro-convulsant effect in the 6 Hz test. The abstract does not give the dose (50 or 100 mg/kg/day) or the tissue for these assays."

======== DR-I01-002 (Durie 2018, abstract; acute flurothyl)
class: CHECK PRESENT BUT NOT MATCHED. The only engagement readouts are in chronic-stage pilocarpine mice (see DR-I01-001), not in the animals tested in acute flurothyl. Dose and exposure for the assays are not stated.
in_study_check: yes, but in a different cohort (see DR-I01-001).
other_effect: yes. DCA was slightly proconvulsant in the 6 Hz test (abstract).
check locator: same sentences as DR-I01-001.
verdict: ADD.
findings:
- "Chronic treatment before the test" is supported: "Chronic DCA (50 and 100 mg/kg/day) treatment was tested in acute seizure and chronic pilocarpine models". The duration is not stated.
- "One laboratory" is supported: all three authors are at the School of Biomedical Sciences, University of Queensland.
- "The abstract reports no effect size" is true. It says only "did not increase latencies".
- Wording gap: "did not increase" is one-sided. The row's NO_CHANGE and the note's "null" go beyond it. The abstract does not rule out a decrease in the flurothyl test, and in the 6 Hz test of the same paper DCA was slightly proconvulsant.
- Missing: the two doses, that animals were mice (males per MeSH), and that no engagement readout is reported in the acute-test animals.
proposed wording: "Chronic DCA at 50 and 100 mg/kg/day in mice did not increase latency to flurothyl seizures (no effect size in the abstract; direction of any small change not stated); in the same paper DCA was slightly proconvulsant in the 6 Hz test. PDH engagement was reported only in chronic-stage pilocarpine mice, not in these animals. One laboratory."

======== DR-I01-004 (Durie 2018, abstract; second-hit flurothyl)
class: CHECK PRESENT BUT NOT MATCHED. The same model and stage (chronic-stage SE mice) has PDH activity measured with DCA: 65% reduction, partly alleviated. The abstract does not say that the second-hit cohort is the one assayed, or the dose or duration.
in_study_check: yes (same model and stage; cohort and dose match unverifiable).
other_effect: yes. DCA was slightly proconvulsant in the 6 Hz test, and DCA lowered PDH by 23% in No SE mice.
check locator: as DR-I01-001.
verdict: ADD, with UNSETTLED clauses. If "only" is kept with no dated search, treat the sentence as MUST CHANGE.
findings:
- Supported: second-hit flurothyl latencies "were decreased in SE vs. No SE mice in the chronic stage, but were not restored by DCA".
- Supported: PDH activity is documented as reduced (65%) in this same paper's chronic SE mice.
- The sentence does not say that engagement in that model was only partial. PDH activity was only partly alleviated and the phospho-site and protein were not significantly changed. The null is therefore a null at partial engagement.
- "The only primary seizure-endpoint test of a PDK inhibitor found..." is a universal word with no search in the held bytes. I cannot verify it, so it is UNSETTLED. The abstract's own statement, "Inhibition of this phosphorylation has not yet been explored", dates only to the authors' 2018 knowledge, and the authors call for studies with "other PDH kinase inhibitors".
- "The full text is closed" is a statement about access that is not verifiable from the held bytes, so it is UNSETTLED.
proposed wording: "In chronic pilocarpine mice (PDH activity 65% lower than in No SE), DCA did not restore the reduced second-hit flurothyl latency. PDH activity was only partly alleviated and the phospho-site and protein were not significantly changed, so the null is at partial engagement. Abstract level; as of the held abstract (2018) the authors state this approach had not been explored. [Drop 'only' unless a dated search is cited.]"

======== DR-I01-014 (Simpson 2006, PMID 16765624, abstract)
class: CHECK PRESENT. Manipulation: DCA in the same fibroblast cultures. The abstract reports "In all cells, DCA caused a major shift (40% decrease) from anaplerotic-related pathways ... toward flux through PDC". This is a direct readout of DCA acting on PDC flux (13C-glutamate isotopomer modelling) in the same cultures, including controls, and it is separate from the glycolysis endpoint.
in_study_check: yes.
other_effect: yes, three effects:
- DCA decreased average glycolysis by 29% in patient cells (excluding the splicing-mutation line).
- The 40% shift toward PDC flux occurred in all cells, controls included.
- DCA "did not change LPR or the NTP/NDP ratio in either cell type".
check locator: the abstract sentences "In all cells, DCA caused..." and "Ignoring the patient with the splicing mutation, DCA decreased average glycolysis (29%) in patient cells, but had no significant effect on control cells, and did not change LPR or NTP/NDP in either cell type".
verdict: MUST CHANGE.
findings:
- The n values are correct. Five healthy subjects and six patient lines are stated, and the 29% excludes the one unusual splicing-mutation line (so it rests on five patient lines).
- The sentence says "the response to the PDK inhibitor depended on a pre-existing PDH defect". This is false for PDC flux: the 40% shift toward PDC flux happened "in all cells". It holds only for the glycolysis decrease.
- The row's endpoint and direction list "lactate production" as DECREASE. This is contradicted: DCA "did not change LPR ... in either cell type".
- "No significant effect in control cells" versus a significant effect in patient cells is a difference in significance. The abstract reports no genotype-by-DCA interaction test, so "depended on" is not shown. The 29% is "average glycolysis", not a quoted glucose-consumption-rate figure.
- The abstract does not report glucose-derived acetyl-CoA flux as a DCA-by-genotype result. It reports label-derived acetyl-CoA as higher in PDC-deficient cells at baseline. The "genotype-by-inhibitor interaction on acetyl-CoA flux" is the repository's proposed experiment, not something this abstract shows.
- DCA dose and exposure are not in the abstract.
proposed wording: "In primary fibroblasts (5 healthy subjects, 6 PDC-E1 patient lines), DCA shifted flux toward PDC by about 40% in all cells and, excluding one patient line with an unusual splicing mutation, decreased average glycolysis by 29% in patient cells but not significantly in control cells (no interaction test reported); lactate production rate and NTP/NDP did not change in either cell type. It is a precedent for a glycolysis-lowering responder phenotype. The abstract reports no DCA-by-genotype result on glucose-derived acetyl-CoA flux, so that interaction is the repository's proposed experiment."

======== DA-K01-007 (mouse brain TPM, GSE158681 and GSE158682)
class: CHECK PRESENT. Manipulation: Wwox deletion. Wwox transcript, summed per symbol across Ensembl 92 transcripts in the same tables, is reduced in all four contrasts. Hippocampus tables: about 7-, 16.5- and 12-fold lower. Cortex table: only about 3.2-fold lower, with overlapping values.
in_study_check: yes.
other_effect: yes. Gfap is higher in all four contrasts. Ndrg1, P4ha1, Epas1, Ldha and Pgk1 are lower (see numbers).
check locator: summed Wwox TPM per sample (pseudocount 0.1 gives log2 -2.56, -3.54, -3.21, -1.65).

Groups and contrasts I used. Group labels come from the sample names only; I did not use any series description.
- Contrast 1: GSE158681 S_KO_1-3 versus S_Ctrl_1-2 (KO n=3, control n=2).
- Contrast 2: GSE158681 N_KO_1-2 versus N_Ctrl_1-2 (n=2 versus 2).
- Contrast 3: GSE158681 KO_1-2 versus WT_1-3 (n=2 versus 3).
- Contrast 4: GSE158682 CRTX_S_KO_1-3 versus CRTX_S_Ctrl_1-4 (n=3 versus 4).

Method. I summed transcript TPM per gene_symbol from the fasta headers (0 unmapped transcripts; each of the 10 symbols has exactly one ENSMUSG). I took the mean TPM per group, then log2((mean KO + pc)/(mean control + pc)). The pseudocount that reproduces the note's ranges is 0.1, so I use pc 0.1 below. Values at pc 1 are in parentheses where they differ. "sep" means all KO values lie beyond all control values in one direction.

Recomputed values, contrasts 1/2/3/4:
- Wwox: -2.56 sep, -3.54 sep, -3.21 sep, -1.65 not sep. TPM: S 0.34-0.75 vs 3.32-3.41; N 0.06-0.37 vs 3.49-3.61; KO/WT 0.28-0.38 vs 3.52-4.27; cortex 3.8-9.01 vs 8.01-26.54.
- Hif1a: -0.17, +0.03, +0.06, -0.20. The note's "within ±0.2" holds at pc 0.1. At pc 0.01 the cortex value is -0.21.
- Hk2: +0.15, -0.01, +0.35, +0.02. The note's "-0.01 to +0.35" matches pc 0.1. At pc 1 the range is -0.01 to +0.23. None is sep.
- Epas1: -0.58 sep, -0.53 sep, -0.21 sep, -0.43 not sep. The note's range and "animal-separated in 3 of 4" are both confirmed. At pc 1 the range is -0.21 to -0.56.
- Slc2a1: -0.40, -0.36, -1.04, -0.17 (lower in all four; sep in 2 of 4).
- Ldha: -0.49, -1.27, -0.50, -0.25 (lower in all four).
- Pgk1: -1.0 or so, -1.2, -0.55, -0.26 (pc 1: -1.01, -1.16, -0.55, -0.26; lower in all four).
- Ndrg1: -1.04 or so, -0.87, -1.17, -1.23. At pc 1 all four are sep (4 of 4). Lower in all four, as the note says.
- P4ha1: -0.64, -1.20, -0.98, -0.94 at pc 1. Lower in all four, as the note says.
- Gfap: +2.12, +1.31, +0.65, +0.85 at pc 0.1 (higher in all four; sep in the first three).

verdict: ADD. All the quoted numbers reproduce. The note needs qualifications and has several clauses I cannot check.
findings:
- Arm sizes are 2 to 4 per group, one pooled mean per group, no test. Only contrast 3 and contrast 1 have a KO n of 3 or fewer with a control n of 2 or 3. The note should give n.
- Three contrasts are in the "Hippo" table and one is in the "Cortex" table. The row field says "mouse brain" without separating hippocampus from cortex. In the cortex contrast Wwox is only about 3.2-fold lower with overlapping values (KO 9.01 above control 8.01), so "Wwox-deleted" is weaker there.
- "No elevation of HIF-axis or glycolysis transcripts in any of four contrasts": Hk2 is +0.15 and +0.35 in two contrasts and Hif1a is +0.06 in one, all small. "No consistent elevation" would be safer wording.
- Not verifiable from the held bytes, so UNSETTLED: P17 age; "lines with severe epilepsy and death at 3 to 4 weeks"; "conditional and germline"; "background differences between control groups"; gliosis and hypomyelination; the organoid comparison ("counter-observation to the organoid rows", "does not side with the organoid", "largest unresolved fact"); and "inputs identical by sha256". The held tables show only sample names.
proposed wording: "In mouse brain TPM tables (3 contrasts in hippocampus, 1 in cortex; n 2 to 4 per arm; Wwox falls about 7- to 16-fold in the hippocampal contrasts and about 3-fold, with overlapping values, in cortex), HIF-axis and glycolysis transcripts show no elevation: Hif1a within -0.20 to +0.06 log2, Hk2 -0.01 to +0.35, Epas1 -0.21 to -0.58 (separated in 3 of 4), Slc2a1, Ldha and Pgk1 lower in all four, Ndrg1 and P4ha1 lower in all four, Gfap higher. Pseudocount 0.1 on mean summed transcript TPM per symbol. Bulk tissue, no protein, small n, post hoc."

======== DR-P9-010 (memantine openFDA label JSON)
class: NOT ASSESSABLE (label). The label is a statement, not a measurement. The sentence is about efficacy, not a knockdown or compound engagement, so no engagement check is in scope. The label gives no paediatric drug-level measurement. The pharmacokinetics section has nothing on children; it covers hepatic-impairment subjects.
in_study_check: no. The label reports no paediatric exposure or target readout.
other_effect: not applicable (no manipulation tested for engagement). Paediatric adverse-reaction rates are reported (Study A cough 8.9% vs 3.4%).
check locator: pediatric_use section 8.4.
verdict: ADD.
findings:
- Supported: section 8.4 states that memantine "failed to demonstrate efficacy in two 12-week controlled clinical studies of 578 pediatric patients aged 6 to 12 years with autism spectrum disorders". The only human paediatric controlled data in the label are these. The indication is Alzheimer's dementia in adults (clinical_studies, section 14, adult trial only).
- "A null result" is singular but there are two studies, and their designs differ. Study A is a parallel placebo-controlled trial (memantine n=54 vs placebo n=53; no significant difference on the Social Responsiveness Scale total). Study B is a responder-enriched randomized withdrawal study of 471 patients (no significant difference in loss of response, 153 vs 158). There was also an open-label lead-in (N=903).
- "Memantine failed to demonstrate efficacy" is the label's own wording. The label dosing was extended-release capsules 3, 6, 9 or 15 mg once daily by weight band.
- "Only ... in the label" is true for this one record. The JSON meta says 75 labels in the openFDA query (results.total 75) and only one is held here (an ER-capsule repackager label, effective 2026-09-01). Other memantine labels are not held, so I cannot verify the sentence for them; for those it is UNSETTLED.
- The label also holds juvenile-rat toxicity studies (not human, not efficacy).
proposed wording: "In this memantine ER-capsule label (effective 2026-09-01; one of 75 openFDA records, others not read) the only controlled paediatric human data are two 12-week studies in 578 children aged 6 to 12 with autism spectrum disorders (Study A parallel placebo-controlled, n=54 vs 53; Study B responder-enriched randomized withdrawal, 471 patients), which the label says failed to demonstrate efficacy. The indication is adult Alzheimer's dementia; it is a null in a different disorder with no paediatric engagement measurement."

======== Files actually opened
- /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/BLIND_SENTENCES_ADV282_INC6_SCI_20261126.md (the packet)
- /home/desktop/legend-development/files/fulltext/adv282_abstracts_sci_20261126/PMID16651305_efetch.xml
- /home/desktop/legend-development/files/fulltext/adv282_abstracts_sci_20261126/PMID29913407_efetch.xml
- /home/desktop/legend-development/files/fulltext/adv282_abstracts_sci_20261126/PMID16765624_efetch.xml
- /home/desktop/legend-development/files/fulltext/ketamine_kds_it_20261117/p6_metabolic_ocular/LABEL_memantine_openfda.json
- /home/desktop/legend-development/files/geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz
- /home/desktop/legend-development/files/geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz
- /home/desktop/legend-development/files/reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz
- /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/rna4.py (my scratch script)
- /home/desktop/legend-development/.claude/worktrees/sci_as_20261126/framework/protocols/delegation_budget.md (section headings only, via grep; its sections 2 and 7 were not read in full)
No other file under disease-models/ or any other results or checkpoints was opened.
