# INV-15 (PV interneurons) — blind verifier audit (actor vf-15, task ORCH-IT38OS-20261108)

Status of this file: parts A and B were written BEFORE opening the producer's `README.md`, `phase1_note.md` or `chains.tsv`; parts C and D and the closing tables are appended after.

## How the sources were reached (depth honesty)

| PMID | Route | What I read |
|---|---|---|
| 30290271 | local cache `files/fulltext/PMID30290271_Hussain2019_PMC_r2.xml` (PMC XML, text-stripped by me) | Abstract, Methods 2.1, 2.3, 2.4, Results 3.1 and 3.4, Fig 1 caption. Whole-document text search for "44%", n, ages. Figure images not viewed. |
| 34634460 | local cache `files/fulltext/PMID34634460_Wwox_osc2021_PMC_r2.xml` (PMC XML) | Complete text: Results 2.1–2.6, Fig 4 and Fig 6 legends, Table 1, Discussion 3.1–3.4, Methods 5.1–5.4, 6.6, 6.7. Supplement not opened. |
| 27845895 | PubMed tool `get_full_text_article` (PMC5386674), returns the full PMC text, not a summary | Complete text including Results, Fig 2 legend, Discussion. Figure images not viewed. Reached through a tool, not a page I could open myself: confidence slightly lower than for a local file. |
| 42812881 | same tool (PMC13620914), saved to a file and searched | Abstract, and keyword/section searches of the full text (no WWOX, no Hyal/hyaluronidase, HAS3/HAPLN passages, PV/PNN passages). Not a complete linear read of 93,708 characters. |
| 33914858 | local cache `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt` | Abstract, Methods (Cre lines, electrophysiology), Results on spheroids and Fig 7 legend; keyword searches for IPSC, interneuron, parvalbumin (zero hits). |
| 35966957 | PubMed tool (PMC9353198) | Full text returned, **but the tool stripped italic gene names** ("the line", "the line"), so the sentence that ties 36 percent to Syn1-Cre is inferable from context (the abstract calls the 85 percent line the "little-known alternative", the Methods list stock 003966) and not directly legible. Confidence lowered on that single attribution. |
| 42583891, 31340538, 33255508, 41442931, 40507943 | PubMed tool metadata (abstracts) | Abstract only. |

Identity checks run: `pubmed_identity_check.py` for 30290271, 34634460, 42812881, 33914858: all MATCH. Claims placed for 30290271, 34634460, 27845895, 42812881, 33914858, 35966957 as vf-15 (other actors hold claims on 30290271 and 42812881; no conflict handled by me).

## Part A — decisive propositions

### Focus 1 — PMID 30290271 PV-positive count (read myself)

DATO, Results 3.1 (heading "Wwox KO mice hippocampi exhibit a decrease in PV+ and NPY+ inhibitory interneurons"): "The overall reduction of PV+ interneurons in Wwox KO mice amounted to 44% when the hippocampus was taken in its entirety (p < .005, Fig. 1 D)." Quote is verbatim (21 words).
- n: Wwox KO 7, WT 7 (Results 3.1 and Fig 1 caption); two-tailed unpaired Student t test; optical fractionator (Methods 2.4, every 15th or 20th section).
- Age: "Wwox KO mice (2 weeks old) and age-matched WT controls" (Methods 2.1); Fig 1 caption "2 wk. old".
- Region: whole hippocampus 44 percent (p < .005); DG p < .005; CA1 p < .05; CA3 "also evident" in the text but no p value is printed for CA3 in the text I read.
- Model: full (global) knockout made with BK5-Cre in oocytes, controls Cre+; Wwox wt/wt littermates, mixed 129SV/C57Bl/6 background (Methods 2.1). Both sexes. These mice die by about 3 weeks.
- Not examined by the paper: cell death, survival, or a pan-neuronal/Nissl count of the same sections, so a marker-positive count cannot separate fewer cells from lower PV in surviving cells (this is the item's INFERENZA). Also "some hippocampal areas ... complete absence of such cells" (Results 3.1) describes areas of the tissue, not a per-animal count.
- GAD65/67: Western blot of hippocampal homogenate, KO n = 5, WT n = 5, p < .05 (Results 3.4). Homogenate protein: not cell-type-resolved.
- NPY+ cells: 30 percent lower in DG (KO 6, WT 6), a second interneuron class (so the paper's reduction is not PV-exclusive).
Verdict on the item: figure, n, age and region are correct as stated by the item. See D02.

### Focus 2 — PMID 34634460 (read myself; Methods and Results)

- Recorded interneurons: Table 1 column "IN" has cells/animals 5/4 (S-WT + S-HT) and 6/5 (S-KO). Methods 6.6 states that pyramidal neurons were identified "based on their appearance under the infrared filter and their electrophysiological features" and "confirmed based on comparison of the spike-half width, input resistance, and membrane time constant". No immunostaining, reporter line, Pvalb/Gad driver or post-hoc identification appears anywhere in the text (zero hits for "parvalbumin"; "PV" occurs only in unrelated tokens). The interneurons were therefore not PV-identified, as the item states. The authors themselves leave the origin open: "a change in pre- or post-synaptic properties unrelated to action potential firing, or ... a WWOX-dependent decrease in the interneuron population ... for which we did not account" (Discussion 3.3; quote shortened).
- mIPSC: the paper has the string "mIPSC" zero times. Miniature currents were recorded only for EPSCs, with TTX (Results 2.3: "Postsynaptic, but not presynaptic, glutamatergic changes"). The word "postsynaptic" in the paper refers to the glutamatergic mEPSC amplitude, not to the sIPSC fall. For sIPSCs Results 2.5 concludes only that the knockout "favors excitation over inhibition, primarily through an impairment in the amplitude of the inhibitory currents".
- Internal solution: Methods 5.3, "For recordings of sIPSCs, a high-chloride intracellular solution was used" (140 mM KCl). Isolation: "Spontaneous EPSCs and IPSCs were isolated by voltage-clamping pyramidal neurons at -70 mV in K-Gluconate or KCl intracellular solution respectively." No GABA-A or glutamate-receptor antagonist is named for the sIPSC recordings; Methods 5.4 lists only TTX, d-APV, CBX and BB-FCF. So the item's "no antagonist is named for isolation" is correct. (My own INFERENZA, not asserted as a defect of the paper: with 140 mM KCl, an inward-at-minus-70 mV readout is also what an EPSC would give, so isolation rests on the chloride gradient and is not pharmacologically confirmed in the text.)
- The only way the paper reports the sIPSC means: amplitude S-CTL 57.3 ± 31.0 pA vs S-KO 27.5 ± 19.4 pA; frequency 10.3 ± 11.5 Hz vs 8.4 ± 10.0 Hz (Results 2.5). The frequency fall is therefore small against its spread, and its significance is given only through KS p values (Fig 4 H, h2). cells/animals for sIPSC: S-CTL 14 cells, 7 animals; S-KO 9 cells, 5 animals; S-WT 7 cells/4 animals; S-HET 7 cells/4 animals (Fig 4 legend).
- Operator rule on statistics (do not assert a definitive contradiction of the paper's statistics with a model the authors did not declare): see D13 below; the audit trail in `inv15_pv` as shown in `verify/items.md` states "compatible with events as units; no contradiction of the paper is asserted", which respects the rule. I reproduced the arithmetic and add one robustness check (below) without changing the wording.

### Focus 3 — PMID 42812881 and the second step of the chain

The review (Front Mol Neurosci 2026; review article type) was reached in abstract plus keyword-searched full text. It contains no occurrence of WWOX and none of hyaluronidase or Hyal-2; link-protein (HAPLN) and HAS3 passages concern seizure-related loss of aggrecan/HAS3/HAPLN1 and diffuse extracellular space, not Wwox. Therefore the second step (hyaluronan/PNN to PV maturation and seizure threshold) is supported only by a review of the rodent PNN literature, with the abstract sentence quoted by the report. Two points the report does not carry, both from the review's full text: (a) "Germline PV-cell Acan deletion eliminated WFA-defined nets but produced limited changes in adult PV-cell electrophysiology" — direct counter-evidence (with compensation noted) against the step "disrupted nets delay PV maturation"; (b) the "hyaluronan deficiency ... precipitate seizures" statement rests on Has3-deficient mice with about 40 percent lower extracellular-space volume in CA1 stratum pyramidale, a diffuse-matrix biophysics mechanism and not a net-around-PV mechanism. The statement that step 2 is review/abstract level only is SUPPORTED, and indeed a little stronger: the review itself hedges that WFA staining is "not a complete proxy for functional ECM state".

### Focus 4 — PMID 33914858 (read myself)

Both models are in the paper. Mouse: Synapsin I-Cre (stock 003966) S-KO, deletion described as "particularly in most of the differentiated neurons" (Results; Cre expressed from E12.5), not "essentially all neurons". Human: CRISPR WWOX-knockout WiBR3 oligocortical spheroids. Fig 7 legend (verbatim numbers): patch-clamp resting membrane potential OS-WT n = 3 vs OS-WWOX-KO n = 4 (−52.1 ± 0.90 vs −21.28 ± 6.91 mV, P < 0.01, Student t); LFP spectral power 9 slices from three organoids vs 6 slices from two organoids; myelin staining n = 3–5 per group. No IPSC, interneuron or parvalbumin term occurs anywhere in the paper. So "3 and 4 per group" is true for the patched-cell readout, and the LFP readout rests on 9 and 6 slices from only 3 and 2 organoids; the item says "small (3 and 4)", which is correct for cells and slightly understates the slice/organoid structure. The paper itself says "Further studies are needed to specify and quantify the imbalance between excitatory and inhibitory neuronal circuits". The report's double citation is accurate.

### Verdict table (A)

| ID | Verdict | Basis (short) |
|---|---|---|
| D01 | SUPPORTED | Table 1 IN cells 5/4 and 6/5; identification by spike width/input resistance/tau; no PV tool; authors list a reduced interneuron population as unexamined. |
| D02 | SUPPORTED | Verbatim 44 percent, KO 7 vs WT 7, 2 weeks, whole hippocampus p < .005; GAD65/67 homogenate n = 5/5. Caveat: CA3 has no printed p. The contradiction of "no PV measurement has ever been reported" holds for a marker-positive count in the global knockout hippocampus (not neocortex, not live cells). |
| D03 | SUPPORTED | No mIPSC in the paper; 140 mM KCl; no antagonist named; "postsynaptic" concerns mEPSCs under TTX; sIPSC conclusion in the paper is only amplitude impairment. |
| D04 | SUPPORTED | Report-internal: L34 table B ("↓ both, transiently"), L39 ("only explanation F predicts the amplitude reduction"), L80 ("B delayed maturation (partly)") under amplitude. Additionally, L39's reasoning is about "quantal amplitude", whereas the measured quantity is sIPSC (action-potential-dependent) amplitude, which also includes multi-quantal, summed events. |
| D05 | SUPPORTED | Abstract/Discussion wording verified; native HA not lethal, overexpressed complex lethal; authors link HA neuroprotection in TBI to less Hyal-2/WWOX/Smad4 signalling. Nuance for the producer: in WWOX-knockout MEFs Smad4 "appeared to relocate into nucleus in 4 hr" (Fig 2 legend) — delayed or attenuated, not absent; "WWOX-negative" lines are MDA-MB-231 and MDA-MB-435S cancer cells with little WWOX; all non-neuronal. |
| D06 | SUPPORTED | Abstract sentence verbatim; review has no WWOX and no hyaluronidase item; PNN-PV half only; not PV-exclusive ("selected populations"). |
| D07 | SUPPORTED | Step 1 non-neuronal cell lines (27845895), step 2 review-level (42812881); my own PubMed/Europe PMC searches found nothing that joins them (see D10 perimeter); hyaluronan review 40507943 (same laboratory, 2025) not opened by anyone, abstract does not mention nets. |
| D08 | PARTLY | Locus unmeasured (no mIPSC): verified in 34634460. KO sIPSC amplitude is about 48 percent of control (27.5/57.3): arithmetic verified. The recombinant-receptor primary papers named in `function_pharm_it14_p3_20261101/README.md` were not reopened by me. Wording: "no GABAergic drug has been tested in WWOX material" needs the perimeter "experimental preparation"; a case report exists of vigabatrin in two children with WWOX-related encephalopathy (PMID 41442931, abstract only), a clinical exposure and not a test of the compensation hypothesis. |
| D09 | SUPPORTED | Abstract verified: rat scPCP model, AUT00206, behaviour. WWOX side: interneuron AP amplitude 45.03 ± 3.58 vs 60.78 ± 3.31 mV (marked significant), spike counts not different, 5/4 and 6/5 cells/animals, no Kv3 current (Table 1, Results 2.6). Note the paper's own Discussion says the interneuron action-potential properties are "unchanged", at odds with its Table 1 star on AP amplitude. |
| D10 | SUPPORTED (perimeter) | My PubMed strings found 4 hits for WWOX/interneuron terms (the three of the producer plus a vigabatrin case report), 0 hits for the Cre-line string. Europe PMC Cre-line string gave 14 hits, none relevant. The producer's Europe PMC strings were screened on the first 25 of 93 and 52 titles only; PubMed title/abstract search cannot see a conditional line mentioned only in a full text (33914858 describes Olig2-, GFAP-, Nestin-Cre lines that the producer's Q3 string did not retrieve). The absence is "not found in the searched index and the first titles screened". |
| D11 | SUPPORTED | See Focus 4. |
| D12 | SUPPORTED (single attribution at lower confidence) | 36 percent of NeuN-high nuclei, 6–8 week male mice, whole-brain Mecp2-mCherry reporter, minimum 2–3 mice per genotype, versus 85 percent for the alternative line; Southern whole-brain 26.2 percent recombination; "incomplete deletion ... in the cortex". Tool dropped the line names; attribution to Syn1-Cre inferred. 33914858 itself says "most of the differentiated neurons". A further point the producer can use: the same Cre-line study found incomplete cortical deletion, which also weakens the report's premise that the recorded layer II/III pyramidal cell is itself Wwox-null (explanation F). |
| D13 | SUPPORTED | Cells and animals are declared per comparison in the Fig 4 legend; Methods 6.7 says statistical design is "in the results section". I recomputed: of 18 printed KS p values in Fig 4 B, C, F, H, 10 lie below the smallest two-sided exact p for the stated per-cell group sizes, and also below the smallest asymptotic p for the same sizes (both conventions give 10 of 18). Unit not declared; "compatible with events as units" is the correct level. One extra legend oddity not in the item: sEPSC legend gives S-CTL 18 cells/10 animals while S-WT 14 + S-HET 17 = 31 cells. |
| D14 | SUPPORTED | Methods 5.1 Synapsin I-Cre conditional, S-KO = Wwox fl/fl; Cre+, P13–P17. The title's "in vitro" means slice recordings. The report's "global in-vitro KO" (L27, L54, L104 "global WWOX KO") is wrong and also inconsistent with the report's own L25. |

Counts (A): SUPPORTED 13 (D12 flagged lower confidence for its single attribution, D10 with narrowed perimeter), PARTLY 1 (D08), NOT SUPPORTED 0, UNVERIFIABLE 0, total 14 (D01–D14).

## Part B — coverage audit of the first extraction

I read the whole of `INV-15_PV.txt` (143 lines), then `extraction.tsv` (E01–E61). Twelve points chosen across the text:

| # | Report point (anchor) | Extraction row | Result |
|---|---|---|---|
| 1 | "plus a sixth postsynaptic alternative" in the Summary (L12) | E07, E20 | PRESENT |
| 2 | Targeted PubMed queries returned zero papers, "with intermittent database errors" (L20, L118) | E04 | PRESENT |
| 3 | Disrupted Cortical Neuronal Migration node (INDIRECT_UNKNOWN_INTERMEDIATES) and tangential migration from the medial ganglionic eminence (L46) | E36 | PRESENT |
| 4 | Confidence-level paragraph: PV–PNN verified against abstract; WWOX–hyaluronan link KB-derived and to be confirmed (L48) | E39 | PRESENT |
| 5 | Favourable remark that the IPSC design is sound with both heterozygote and wild-type littermates (L51) | E43 | PRESENT |
| 6 | Gene-therapy rescue is at hyperexcitability/seizure level and does not confirm the inhibitory node (L57) | E45 | PRESENT |
| 7 | Table row C: "No GABAergic augmentation needed; marker is a biomarker, not a target" (L35) | E23 | PRESENT |
| 8 | "AMPA-kinetics modulation" named in passing as an example for explanation E (L37) | E25 | PRESENT |
| 9 | End of the follow-up list, experiment 9: IPSC/PV endpoints added to organoid and AAV9 paradigm (L138) | E56 | PRESENT |
| 10 | Decision rule listing "PNN-modifying agents" and gating on experiments 1–3 and 5 only (L140) | E57, E22 | PRESENT |
| 11 | Experiment 2: PV-Cre;ChR2 light-evoked IPSC "isolates the PV-specific contribution from the aggregate IPSC" (L124) | E49 | PRESENT_NARROWED (the second purpose clause is not in the row; the row keeps "separates reduced function from reduced marker only") |
| 12 | Limitations: absence "may partly reflect a genuinely unstudied area rather than incomplete curation" (L118) | E47 | PRESENT |

Result B: 11 PRESENT, 1 PRESENT_NARROWED, 0 MISSING (12 of 12 present). Because no point was MISSING, no extension scan was triggered; I did, however, scan the remaining lines for the same kinds of content (caveats, passing compounds, counter-arguments) and found none that lacked a row. Minor narrowing only: E44 turns "can inflate statistical confidence substantially" into "could inflate"; the report's claim that PV is "the dominant PNN-bearing population" (L46) is carried in E37 without the contrast with the review's "selected neuronal populations" wording (reconcile, not coverage).

---

(Everything below was written after I opened `README.md`, `chains.tsv` and the head of `phase1_note.md`, which I did only once the A and B verdicts above were saved. Reading them changed no A or B verdict.)

## Part C — reconciliation sample (8 rows of `reconcile.tsv`)

Sample: new_to_legend E12, E49, E56; already_present_and_used E24, E26; present_not_used E22, E41; superseded_or_contradicted E03. Previous package: `disease-models/wwox/research/drug_repurposing/pv_inv15_20261107/` (found with `git grep -l "INV-15" -- disease-models`); its `BRIEF.md` and `output/experiment.tsv`, `evidence.tsv`, `alternatives.tsv` were opened.

| Row | Pointer opened | Pointer exists and says what the row claims? | Finding |
|---|---|---|---|
| E03 (superseded) | `pv_inv15_20261107/output/evidence.tsv` P01–P06 | Yes. P01 carries 44 percent, KO 7/WT 7, CA3 unmarked; P05 states the absence of apoptosis/lineage data; P06 GAD65/67 KO 5/WT 5. | OK. Note "complete read plus re-check" is consistent with my own read. |
| E12 (new) | none by design; I ran `git grep` over `wwox/research` and `wwox/analysis` for interneuron-restricted Cre/deletion wording | No pre-existing statement found; the previous `experiment.tsv` X10 only says "a new animal line" is not proposed. | OK for "new as an explicit absence statement". |
| E49 (new) | none; checked `wwox/research` | **Overstated.** `wwox/research/commit_candidates/CC-20260826-EGABA-CLOSURE-01.md` line 87 (mechanism M3, interneuron number/firing) already lists "optogenetic interneuron drive" as the revival trigger that would discriminate M3 in WWOX. The PV-specific PV-Cre;ChR2 per-connection design is new, the optogenetic interneuron-drive idea is not. | Change `legend_novelty` to "partly: PV-Cre;ChR2 per connection new; optogenetic interneuron drive named in CC-20260826-EGABA-CLOSURE-01 (M3)". |
| E56 (new) | none; checked `wwox/analysis` | **Overstated.** `wwox/analysis/mechanism_intervention_map.md` (E-2, line 1236 and the E_GABA row near 612) already proposes a decisive GABA experiment in WWOX-KO neurons/organoids; `wwox/analysis/interneuron_sparing_rule_test_20260923.md` (limit 8, around line 456) already warns that dorsally patterned organoids commonly lack GABAergic interneurons, so any interneuron statement there is "not measured". The report's idea of adding PV endpoints to the spheroid is therefore partly known and has a precondition (interneurons present in an oligocortical spheroid) the extraction does not carry. | Change `legend_novelty` to "partly"; add the precondition; the AAV9 half (no inhibitory endpoint) remains new. |
| E24 (already_present) | `function_pharm_it14_p3_20261101/question_scoring.tsv` Q-PVfire; `pv_inv15_20261107/output/experiment.tsv` X8 | Yes. Q-PVfire reads "interneuron AP amplitude 60.8 to 45.0 mV (n 5 and 6 cells); ... thin Kv3 public pharmacology"; X8 holds the Kv3 versus GABA-A slice comparison. | OK. |
| E26 (already_present) | `function_pharm_it14_p3_20261101/README.md` H1 | Yes. H1 is clobazam plus N-desmethylclobazam, hypothesis only, "no GABAergic drug has been tested in any WWOX preparation". | OK. |
| E22 (present_not_used) | `pv_inv15_20261107/output/experiment.tsv` X7, X9; `evidence.tsv` R04 | Yes. X7 is a net-staining arm, X9 refutation conditions; R04 carries "ChABC is not intrinsically PNN-specific". No PNN-modifying agent is in the prior package, so "present, not used" is right for the pharmacology. | OK. |
| E41 (present_not_used) | receipt `FTR-20261107-33914858-50` in `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | Exists (further 33914858 receipts exist, up to `-99` on 2026-11-08). Prior README and experiment table contain no spheroid/organoid statement (searched). The spheroid numbers (3 and 4 cells; 9 and 6 slices) are as I read them. | OK. |

`prior_brief_fate` checked against `pv_inv15_20261107/BRIEF.md` for five rows (four required):

| Row | Producer value | Brief says | Result |
|---|---|---|---|
| E03 | modified | Item 2: "restore the omitted evidence: PMID 30290271", not equating marker loss with cell loss | Correct. |
| E11 | modified | Item 3: verify "the conditional identity of the model" | Correct. |
| E57 | modified | Item 6: "Do not require all the experiments of the report as a prerequisite" | Correct. |
| E55 | narrowed | Item 6: "do not propose new animal lines if a simpler comparison can change the decision first"; `experiment.tsv` X2/X10 prefer the Cre-positive littermate comparison | Correct. |
| E49 | **omitted** | Item 4: "hypotheses based on PV-Cre must consider that identification and recombination depend on the appearance of the Pvalb program"; `experiment.tsv` X2: "A PV-Cre line is not proposed first" | **Incorrect or at least too strong.** The brief qualified PV-Cre-based designs; the optogenetic design itself is not in the table. Use `narrowed`. The producer's README (b) repeats "optogenetic PV-ChR2 ... omitted"; change it to match. |

Part C result: 6 of 8 sampled rows fully accurate; 2 (E49, E56) have an overstated `legend_novelty = yes`; 1 `prior_brief_fate` wrong (E49).

Count check of the producer's own summary (README (a)): kind counts and `legend_class` and `prior_brief_fate` totals recomputed from the TSV files: all agree.

## Part D — evidence sample (`evidence.tsv`, V01–V10, every row backs a decisive proposition)

| Row | Quote verbatim in the source at the stated place? | Carries the proposition? | Note |
|---|---|---|---|
| V01 (42583891) | Yes. Abstract, first sentence (abstract only; I read it too). | Context only for D09 (class origin). Correct role. | Efficacy is in a rat phencyclidine behavioural model, as the note says. |
| V02 (search list) | Not a quote. I reran a close string (my own, with `GABAergic` added) and got those three plus 41442931 (vigabatrin MRI case report). | Counter to the report's "zero papers" (D02): yes; the hit list is correct for the producer's string. | OK. |
| V03 (search list) | Not a quote. Reran the exact Q2 string: same four PMIDs. | Context for D07. | OK. |
| V04 (search, 0 hits) | Not a quote; my own Cre-line strings also returned 0 in PubMed and 14 irrelevant hits in Europe PMC. | D10 absence with perimeter: yes. | See D10 perimeter note in the table above. |
| V05 (33255508) | Yes: "GABAergic basket cells and granule cells from cerebellar cortex" is in the abstract. | Context only; correctly labelled "Not a PV datum". | OK. |
| V06 (31340538) | Yes: "characterized by a reduction in neurite growth without a reduced number of neurons" is in the abstract (preceded by "cortices were"). | Context for D02; the note correctly says absence from the abstract is not absence in the paper. | OK. |
| V07 (30290271) | Yes, Results 3.1, verbatim, full sentence continues "(p < .005, Fig. 1 D)". | Yes, it carries the 44 percent; n = 7/7 and age 2 weeks are not in the quote (they are in the same Results paragraph and Fig 1 caption). | OK; consider adding a second row for "(n = 7) and WT (n = 7)" and for Methods 2.1 "(2 weeks old)". |
| V08 (34634460) | Yes, Methods 5.1 (italics stripped). | Carries D14 (conditional model). It does **not** carry D01 or D03, which are listed in `proposition_ids` for this row. | Correction needed. |
| V09 (27845895) | Quote is verbatim, **but the locator "(Results)" is wrong**: the sentence is in the Discussion (first paragraph). The abstract has a different wording ("HA failed to induce Smad2/3/4 relocation to the nucleus"). | Carries the loss-of-signalling datum for D05; as a counter for D07 it is the first-step datum. | Correct the section. |
| V10 (42812881) | Yes, abstract (the PubMed text has " - " where the report has an em dash; harmless). | Carries D06's PNN-PV half. | OK. |

Missing evidence rows (no verbatim row in this folder; the proposition relies on a reused row from another package that I could confirm in the source): D03 (140 mM KCl, no mIPSC, "postsynaptic" about mEPSCs), D01 (interneuron identification, Table 1 N), D09 (AP amplitude 45.03 vs 60.78 mV, 5/4 and 6/5), D11 (3 vs 4 cells), D12 (36 percent), D13 (cells/animals per comparison). Suggested verbatim rows (all ≤25 words, checked by me in the cached XML/text): "For recordings of sIPSCs, a high-chloride intracellular solution was used" (34634460, Methods 5.3); "These results were consistent with a postsynaptic mechanistic change to pyramidal neurons" (Results 2.3); "S-CTLs n = 14 cells from 7 animals; S-KOs n = 9 cells from 5 animals" (Fig 4 legend); "OS-WT, n = 3; OS-WWOX-KO, n = 4" (33914858, Fig 7 legend B); "only a proportion of neurons (~36%) in the line express Cre" (35966957 Discussion; the gene name is stripped in the tool's text).

## Verdict per proposition (final table)

| ID | Verdict | Confidence / depth | Note |
|---|---|---|---|
| D01 | SUPPORTED | high; full text | |
| D02 | SUPPORTED | high; Results/Methods/Fig 1 caption; figure image not viewed | CA3 carries no p value in the text |
| D03 | SUPPORTED | high; full text | high chloride is in Methods 5.3 (the item says 5.4, the pharmacology section that names no antagonist) |
| D04 | SUPPORTED | high; report text | |
| D05 | SUPPORTED | high; full text through a tool | KO MEF Smad4 relocation delayed (4 h), not absent |
| D06 | SUPPORTED | medium-high; abstract plus keyword-searched full text | review also reports germline PV-cell Acan deletion removing WFA nets with limited PV electrophysiology change |
| D07 | SUPPORTED | medium; bounded searches only | 40507943 and 34831305 not opened by anyone |
| D08 | PARTLY | medium | recombinant-receptor primaries not reopened; wording perimeter "experimental preparation" |
| D09 | SUPPORTED | high for WWOX datum, abstract-only for the class source | |
| D10 | SUPPORTED with perimeter | medium | titles-only screening of Europe PMC (25 of 93, 25 of 52) |
| D11 | SUPPORTED | high | slice/organoid structure (9 and 6 slices from 3 and 2 organoids) is a refinement |
| D12 | SUPPORTED | medium (line name stripped in tool text) | |
| D13 | SUPPORTED | medium-high; own recomputation | 10 of 18 holds under exact and asymptotic KS; stays "compatible with", not a contradiction |
| D14 | SUPPORTED | high | |

Counts: SUPPORTED 13, PARTLY 1, NOT SUPPORTED 0, UNVERIFIABLE 0 (of 14).

## Corrections the producer must make

1. `inv15_pv/evidence.tsv`, row V09: locator "(Results)" → "Discussion, first paragraph". Row V08: `proposition_ids` "D01,D03,D14" → "D14" (or add rows that carry D01 and D03; suggested quotes above).
2. `inv15_pv/decisive.tsv`, D03 locator: add "Methods 5.3 (high-chloride internal), 5.4 (no antagonist listed)".
3. `inv15_pv/decisive.tsv`, D08 statement: replace "no GABAergic drug has been tested in WWOX material" by "in any WWOX experimental preparation (mouse, rat, organoid); clinical exposure to GABAergic drugs (for instance vigabatrin, PMID 41442931, abstract) is not a test of this hypothesis".
4. `inv15_pv/decisive.tsv`, D10: add to the perimeter "Europe PMC titles screened: first 25 of 93 and 25 of 52 hits; a conditional line described only in a full text (33914858 describes Olig2-, GFAP-, Nestin- and Synapsin-Cre lines) is invisible to a PubMed title/abstract string".
5. `inv15_pv/decisive.tsv`, D11 statement: "3 and 4 per group" → "3 and 4 patched cells for resting potential; 9 and 6 slices from 3 and 2 organoids for field power".
6. `inv15_pv/reconcile.tsv`, row E49: `legend_class` new_to_legend → keep only if `legend_novelty` becomes "partly (optogenetic interneuron drive is named in CC-20260826-EGABA-CLOSURE-01, M3 row)"; `prior_brief_fate` omitted → narrowed. Row E56: `legend_novelty` yes → partly, citing `wwox/analysis/mechanism_intervention_map.md` (E-2) and `wwox/analysis/interneuron_sparing_rule_test_20260923.md` (limit 8, organoid interneuron content). `README.md` (b) and (g) must be changed accordingly.
7. `inv15_pv/README.md` (d), first bullet and the statement on 27845895: add "in knockout MEFs Smad4 relocation is delayed (about 4 h) rather than absent" and that the "WWOX-negative" lines are MDA-MB-231 and MDA-MB-435S cancer cells with little WWOX.
8. `inv15_pv/README.md`, the 42812881 sentence: add the counter-evidence from the review itself (germline PV-cell Acan deletion removes WFA nets with limited change in adult PV-cell electrophysiology, compensation noted) as a limit on the step "disrupted nets delay PV maturation".
9. `inv15_pv/phase1_note.md` says "142 lines"; the file has 143 lines (the Bottom line text is L143, its heading L142). Anchors elsewhere (E29 uses L143) are consistent with the file; harmless, but state it once.

## Open uncertainties

- Figures of 30290271 (Fig 1) and 34634460 (Fig 4, Fig 6) were not viewed by me; every figure-dependent number is from text, legends and Table 1.
- The unit of the KS tests in 34634460 is not declared. My "10 of 18" arithmetic assumes the group sizes in the Fig 4 legend are the per-cell sizes and pairs each printed p with its comparison by the legend order; it supports "compatible with events as units" and nothing stronger. The paper does not say whether exact or asymptotic KS was used; the count is the same under both conventions. No contradiction of the paper's statistics is asserted here, in line with the operator rule.
- sIPSC isolation in 34634460 rests on chloride gradient with a 140 mM KCl pipette and no named antagonist. Whether glutamatergic events contaminate the "sIPSC" trace cannot be decided from the text; the supplement was not opened.
- The 36 percent reporter figure comes from the Syn1-Cre line of 35966957 by inference (tool text lost the gene names); a direct reread of the PDF or PMC page is advised before the figure is carried anywhere else.
- The review 42812881 was searched by keyword, not read start to finish; a counter-statement beyond the two passages found (Acan, Has3) may exist.
- 34747138 (AAV9 gene therapy) was not reopened by the producer or by me; "no cell-type-resolved inhibitory readout" for it is unchecked (extraction E42, README (i)).
- 40507943 (hyaluronan review, same laboratory as 27845895, 2025) and 34831305 (WWOX models review) were not opened by anyone; the abstract of 40507943 does not mention nets or interneurons.
- Sources reached only through a tool that returns text (27845895, 35966957, 42812881): treated as the real papers' text but not as page-level reads.
