# Blind audit, INV-05 (NMDA), verifier vf-05, 2026-11-08, task ORCH-IT38OS-20261108

Scope and depth (stated once, applies throughout). I did not open `README.md`, `phase1_note.md`, `chains.tsv` or `decisive.tsv` of this report folder at any point. I read the whole original report (`/home/desktop/legend-development/files/openscientist_retest_20261108/original_reports/INV-05_NMDA.txt`), `verify/items.md`, `extraction.tsv`, `reconcile.tsv`, `evidence.tsv`, and the previous package `nmda_inv05_20261107/BRIEF.md`. All 17 PMIDs of the items were claimed as `vf-05` (the claim tool shows other actors on 40994429, 15335108, 15075380, 22261077 [os-05], 38529699, 39970743, 20720132 [nm-p] and 34634460 [hc-p, pv-p]).

Routes. No page summariser (WebFetch) was used anywhere. Routes were: PubMed metadata/abstract tool (all PMIDs); Europe PMC REST full-text XML for PMC8609180 (PMID 34634460), which worked once and then returned HTTP 500; PMC full-text tool, which returned an EMPTY body for PMC12677382 (PMID 40994429) and PMC2932667 (PMID 20720132). Consequence: PMID 34634460 was read at full text (Results, Discussion, Methods, Fig 3 legend; supplementary tables not seen). Every other source below was read at abstract level only; where a verdict leans on a full-text fact I did not see, it says so and confidence is lowered.

## A. Verdicts per proposition

| Item | Verdict | Depth | What decided it |
|---|---|---|---|
| D01 | SUPPORTED | abstracts 38529699, 40994429 | See D01 note below. Refinement needed (producer wording "only in vivo support"). |
| D02 | SUPPORTED (abstract level; full text unreachable for me too) | abstract 40994429 | The phrase is a background sentence in the abstract. No infant, window or WWOX datum there. The full text may cite a source; unverifiable here. |
| D03 | SUPPORTED, bounded | PubMed re-run 2026-11-08 | Q10 string: 0 hits (reproduced). Q11 string: I get 4 hits, not 5 (see below). |
| D04 | SUPPORTED | report L9/L30/L125/L161 + abstracts 15335108, 15075380 | Wording applied to availability, not an experiment. Extra: internal inconsistency (below). |
| D05 | SUPPORTED | PubMed "perzinfotel" = 11 hits (reproduced); abstracts of 10 screened, 15075380 read | No clinical failure report found. Abstract confirms 10-fold NR2A over NR2B/NR2C. |
| D06 | SUPPORTED | abstract 22261077; PubMed count reproduced (47) | Single background sentence, no data. |
| D07 | SUPPORTED | abstract 39970743 | Concomitant ketamine, WES result during the second week of memantine, title "Apparent efficacy". |
| D08 | SUPPORTED | FULL TEXT 34634460 (Results 2.2, Discussion 3.4, Fig 3 legend) | Carbenoxolone caveat is in the source itself (details below). |
| D09 | SUPPORTED | abstract 15335108 | Abort reason and retrospective TBI result as stated. |
| D10 | SUPPORTED (stronger than stated) | abstracts 28782587, 21896318 | 28782587 EPSC sentence is about ketamine-induced change, see note. |
| D11 | PARTLY | abstract 20720132 (full text not reachable); full text 34634460 for Mg2+ | Qualitative claim and 1 mM Mg2+ persistence confirmed in the abstract; the "substantial synaptic block" magnitude is not in the abstract and I could not open the Results. |
| D12 | SUPPORTED (IPOTESI) | abstracts 12520755, 17312200, 19204407 (23395831 seen too) | Reviews and a high-dose mouse study; no WWOX ratio. Extra detail below. |
| D13 | SUPPORTED | FULL TEXT 34634460, Fig 3 legend (Europe PMC XML) | Legend: "n = 51 bursts, 5 slices, 3 animals d-APV"; text: d-APV 50 uM "eliminated"; age P13 to P17. |
| D14 | SUPPORTED | abstracts 41409370, 37334223 | 56 percent (51-61) pooled; "4/5 of the surviving children (5/8)". Extra detail below. |

Counts: SUPPORTED 12, PARTLY 1 (D11), NOT SUPPORTED 0, UNVERIFIABLE 0.

### Notes per item (only what adds to or sharpens the item)

D01. DATO confirmed: 38529699 abstract is a homozygous GluN2A(N615S) line ("Grin2a" mice), acute treatment "before the presentation of a high-frequency acoustic stimulus", and radiprodil "more effective in female versus male mice". Report L36 quotes "may have the potential to control seizures in patients with GRIN2A GoF mutations": verbatim in the abstract. The report omits the sex dependence and the reflex-seizure nature. 40994429 abstract: variants tested are GRIN1 and GRIN2B (22/27). Correction to the item wording: 40994429's own abstract also reports GluN2B-S810R knock-in slices and a PTZ onset delay in vivo (458 +/- 90 s vs 207 +/- 23 s). The report did not cite that, so "the report's only in vivo support is 38529699" is true of the report, but the item should not read as if no GluN2B-directed in vivo datum exists in the cited paper. It still says nothing about WWOX or about which subunit carries the WWOX burst.

D03. Q10 reproduced at 0 hits. Q11 (WWOX OR Wwox) AND (NMDA OR GluN2B OR GRIN2B OR "glutamate receptor") returned 4 hits for me (the item says 5; date or string drift, queries.tsv Q11 should record the string verbatim and the date). I screened the titles: the WWOX NMDAR paper (34634460), a DEE re-analysis paper listing WWOX and GRIN2B among genes, a glioblastoma biomarker paper, and an aflatoxin gene-signature paper. None is an NMDA-antagonist-in-WWOX study. Absence bounded as the item says (PubMed title/abstract/MeSH, two strings, one day).

D04 and D05 extras. (a) The report calls competitive block "pan-subunit" (L22, L125) while its own agent perzinfotel is 10-fold NR2A-preferring (abstract 15075380): the class is not uniformly pan-GluN2. (b) Report L125 says "the one competitive agent failed for safety" but L9, L30, L161 name two (selfotel, perzinfotel): internal inconsistency. (c) Among the 11 perzinfotel hits: a rat abstract states perzinfotel has "therapeutic ratios ... superior" to other competitive and uncompetitive NMDA antagonists (PMID 15764736); a 1998 synthesis abstract says it was "under clinical evaluation as a neuroprotective agent for stroke" (PMID 9457246); veterinary MAC studies report no adverse effects in dogs; a rat low-Mg2+ slice study reports EAA-090 "completely blocking spontaneous bursting activity" (PMID 15907811). None is a human failure report, none proves safety. The claim of failure for psychotomimetic or neurotoxic effects stays unsourced; clinical-development records outside PubMed were not searched by me either.

D07. Additional limits visible in the abstract: patient 11 months old, treated during status epilepticus, so the report's heading "neonates/infants" for F007 stretches to a single infant; the abstract gives the variant but no pathogenicity assessment; the authors' rationale (ATP1A2 protects against NMDAR excitotoxicity) is ATP1A2-specific. The report's quote is verbatim.

D08. Read in the source: CBX 100 uM "decreased the frequency of the events by 87%" and duration by 18%, "did not return to normal levels after washout"; BB-FCF 10 uM did not reproduce it; Discussion 3.4: CBX "could block NMDA receptors ... which could partially account for our observations" and "blocks pannexin channels". So the source itself says gap junction block reduces, d-APV eliminates, and the gap-junction label rests on a non-specific blocker. The item is right that report L26 ("NMDAR block is sufficient") and L132/L153 (co-dependence complicates attribution) pull in different directions. Additional source facts the report omits: the model is neuron-specific (Synapsin-Cre); bursts occurred in heterozygotes too (4 of 23 slices, none in 11 wild-type slices); recordings at P13 to P17 and the authors say these mice die at 3 to 4 weeks, so the age "may mimic a late-stage disorder".

D09. Abstract reads: trial "had to be prematurely aborted, since concurrent stroke studies ... revealed an increased number of deaths and other adverse events"; "A retrospective analysis did not confirm that Selfotel was associated with an increased mortality in TBI". Report L42 and L108 compress this to "phase-III trial aborted for excess deaths and adverse events", dropping that the signal came from stroke studies. Report L9 also says selfotel and perzinfotel "failed ... for psychotomimetic and neurotoxic effects": nothing in 15335108 says psychotomimetic.

D10. 28782587 abstract (neonatal rat, PND 7, anterior cingulate): the EPSC increase "largely mediated by GluN2B-containing NMDARs" is the increase after six ketamine injections, not baseline neonatal cortex. Report L33 quotes it as a baseline statement ("in neonatal cortex NMDAR-mediated EPSCs are ..."): that is a misattribution of context, not just weak support. 21896318 abstract (mouse, postnatal day 7 vs adult cortex, hypoxia-ischaemia context): "NR1/NR2B was the main subunit at extrasynaptic membrane ... in the immature brain" is a subcellular-fraction (Western) statement at P7, not a P13 to P17 synaptic measure and not electrophysiology. Quote verbatim, scope narrower than the report's "predominant GluN2 subunit" in immature cortex. Neither paper was read beyond the abstract.

D11. Abstract of 20720132 (rat hippocampal autaptic microcultures): memantine 1 to 10 uM blocks extrasynaptic NMDA-induced current "with a twofold higher potency" than the NMDAR EPSC component, "persists ... in the presence of 1 mM extracellular Mg2+". That contradicts a reading of "tonic/extrasynaptic = inaccessible", as the item says; but report L45/L157 states it as "may be largely Mg2+-blocked", hedged, so the item's "not supported as stated" should say the report hedges and the counter-evidence is from a different preparation (culture, bath NMDA, not slice, not cortex, not tonic). The percentage of synaptic block is not in the abstract; the figure in the item comes from the previous package's receipt, which I did not re-check. Mg2+ of the WWOX recording: 34634460 Methods give 1.3 mM MgSO4 only for the incubation ACSF and a sucrose solution; the recording perfusate is not stated separately. So "remain unmeasured" should read "not stated in the source".

D12. 12520755 abstract: "abnormal inhibition of neuronal activity (by blockade of NMDA Glu receptors ...) triggers neuronal suicide (apoptosis)"; human brain growth spurt "extends from the 6th month of gestation to several years after birth": supports the window claim, on animals. 17312200 abstract (FDA review): "NMDA receptor antagonists, including ketamine, induce neurodegeneration in the developing brain" is verbatim; the same abstract says ketamine effects are dose dependent, exposure doses were "slightly larger than those used in the clinical setting", and "insufficient human data". The report carries none of these limits. 19204407 abstract: C57Bl/6 mice, 4 doses of MgSO4 250 mg/kg on P3, P7 or P14; damage in P3 and P7, "but not P14"; title "High dose". The WWOX slices are P13 to P17 mouse: the one animal study the report uses for "breadth" showed no damage at the matching age. Also the report's phrase "agents acting at the channel Mg2+ site (MgSO4)" is the report's gloss; the abstract only says apoptosis is "potentiated by other drugs with mechanisms of action at Mg-binding sites". No therapeutic-index datum anywhere, as the item says. Abstract level only.

D13. Fig 3 legend (Europe PMC XML, primary text): "n = 51 bursts, 5 slices, 3 animals d-APV; n = 36 bursts, 4 slices, 3 animals CBX; n = 73 bursts, 6 slices, 3 animals BB-FCF". Text: "d-APV (50 uM) eliminated the spontaneous bursting events ... Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal." The item is accurate. One more WWOX datum in the same paragraph, not in the report: the delayed evoked field response (layer V stimulation, layer II/III recording) was larger in S-KO and was reversibly suppressed by d-APV (Supplementary Fig S3, text only seen). Report L51 "the only direct NMDAR evidence is the d-APV-sensitive slice burst" and L136 "No WWOX-specific NMDAR data" are therefore too absolute; this is still not a subunit or receptor-biophysics datum (the source also says mEPSC decay time constant did not differ, 5.18 vs 4.84 ms, "no overt change" in NMDAR:AMPA proportion at -70 mV, where Mg2+ block makes this weak evidence).

D14. 41409370 abstract: 10 studies, 388 patients, 56 percent (51-61), "no heterogeneity"; subgroups 59 percent adults and 50 percent children; "frequent use of concomitant anesthetics". The report cites the pooled figure for "adults and children" and uses it as infant feasibility; the paediatric rate (50 percent) is not mentioned. 37334223 abstract: "Neurologic sequelae including hypotonia and spasticity were reported for 4/5 of the surviving children (5/8)": 5 of 8 neonates survived; the report prints the 4/5 but not that three of eight did not survive; the abstract also says ketamine "appeared to be safe and effective in all neonates treated". Report quote verbatim. Both abstract-level only.

### Additional proposition found during the audit (propose as D15)

X1. Report L36, L62 (diagram), L88 and L89 (matrix: voltage "None", Mg2+ "None") state that GluN2B NAMs are "not use-dependent". The abstracts of the two prototype GluN2B NAMs say the opposite: ifenprodil "antagonized NMDA receptors in an activity-dependent manner" with "39- and 50-fold higher affinity for the agonist-bound activated and desensitized states" (PMID 9003561, rat cultured cortical neurones); Ro 25-6981 "blocked NMDA receptor subtypes in an activity-dependent manner" (PMID 9400004). Radiprodil itself was not checked (its own paper's full text is unreachable); the claim that radiprodil "resembles d-APV in being independent of channel gating" (L36) is therefore uncited and, for the class, contradicted at abstract level. Verdict for the report claim: NOT SUPPORTED for ifenprodil-type NAMs, UNVERIFIED for radiprodil. This matters because the report's "closest mechanistic match to d-APV" argument for radiprodil rests on it (extraction rows E14 and E16 note it is uncited but not that it is contradicted).

## B. Coverage audit of the first extraction (12 points)

| # | Report content point (anchor) | Extraction | Result |
|---|---|---|---|
| 1 | d-APV "Poor BBB penetration; experimental (slice/ICV) only" (L24) | E02 | PRESENT |
| 2 | Gap-junction co-dependence "does not undermine NMDAR-targeting" (L26) | E04 (+E05 for L132) | PRESENT |
| 3 | Failed neuroprotection agents named in passing: aptiganel, dextrorphan, eliprodil, gavestinel, licostinel (L42) | E20, E21 | PRESENT |
| 4 | Quinidine with dextromethorphan for CYP2D6-limited exposure (L92) | E89, E10 | PRESENT |
| 5 | Radiprodil CNS exposure "Good (+)" (L88), "CNS-active" (L119), "CNS target engagement" (L102) | none | MISSING |
| 6 | "slice concentrations do not map directly to clinically/developmentally safe CNS exposure" (L134) | E61 | PRESENT |
| 7 | "Analysis caveat: ... no primary electrophysiology data were available" (L140) | E60 | PRESENT |
| 8 | TCN-201 / MPX-004 / NVP-AAM077-type GluN2A antagonists (L143) | E64, E85 | PRESENT |
| 9 | Diagram: voltage dependence of pore blockers "(trapping)" (L60) | E32 | PRESENT_NARROWED (trapping not recorded) |
| 10 | If blockers work only at low Mg2+ or depolarised potentials the drive is phasic (L145) | E65 note | PRESENT |
| 11 | Amantadine matrix row: weak open-channel, CNS exposure "Good (+)", approved (L93) | E09 | PRESENT_NARROWED (CNS exposure and approval not recorded) |
| 12 | Matrix column "Match to d-APV logic" with scores for every agent (L87-L94) | E58 (ketamine only), E56 (tiers) | PRESENT_NARROWED (per-agent scores not recorded) |

Result: 11 of 12 present (8 PRESENT, 3 PRESENT_NARROWED), 1 MISSING.

Extension for the MISSING kind (matrix cells and evidence-base glosses). Further misses or narrowings in the same family: radiprodil "Good (+)" CNS exposure (L88); ketamine and amantadine CNS exposure cells "Good (+)" (L91, L93; E08 has "CNS-penetrant" for ketamine only); the d-APV matrix row developmental safety "~" and clinical "Experimental (-)" (L87); the "Match to d-APV logic" cells "+ (best)" radiprodil, "+" ifenprodil/traxoprodil, "~" memantine, "-" dextromethorphan, amantadine, nitrous oxide (L88-L94); Evidence Base L102 gloss "CNS target engagement"; Reference Pharmacology L18 "surmountable by glutamate". Rows scanned for other content kinds (caveats, experiments, side remarks, counter-arguments) in L124-L161 and L47-L51: no further miss. Suggested new row wording: `E91 observation: Matrix CNS-exposure column: radiprodil Good (+), ketamine Good (+), amantadine Good (+), memantine Good oral (+), DXM CYP2D6-limited (~), N2O inhaled (~), d-APV none (-); Match-to-d-APV column: radiprodil + (best), ifenprodil/traxoprodil +, memantine ~, ketamine ~ (acute), DXM -, amantadine -, N2O -; Evidence Base L102 glosses PMID 38529699 as "CNS target engagement"; all uncited judgement; anchor L87-L94,L102,L119`.

## C. Reconciliation sample (8 rows of `reconcile.tsv`)

| Row (item_ids) | Class | Pointer / fate check | Result |
|---|---|---|---|
| E11 | new_to_legend | where_in_legend "none". `git grep -i nitrous` outside this folder finds `profiles_it23_p4_20261103/identity_join.tsv` line 1457 (DB06690 nitrous_oxide, CHEMBL1234579) | CORRECTION: not new to LEGEND as a name; "new in this module" is true within the stated perimeter. Reclassify `present_not_used` or state both. Prior fate "omitted": BRIEF has no nitrous oxide, confirmed. |
| E42,E43,E46 | new_to_legend | PMIDs 41409370 and 37334223 occur in LEGEND only in this folder (git grep over the repository) | PASS. Prior fate "narrowed": BRIEF has "neurological outcomes after treatment of status epilepticus are not automatically attributable to the drug", confirmed. |
| E68 | new_to_legend | no Wwox in vivo NMDA test in `nmda_inv05_20261107` | PASS (perimeter: that package and the cited lithium package only). |
| E01 | already_present_and_used | `nmda_inv05_20261107/output/evidence.tsv` rows E23, E24 exist and carry 51 bursts, 5 slices, 3 animals, P13 to P17, 1.3 mM incubation Mg2+; prior fate "kept": BRIEF cites 34634460 with a complete read | PASS. |
| E44 | already_present_and_used | `evidence.tsv` rows E06 and E09 for 39970743 exist; prior fate "kept": BRIEF precedent B | PASS. |
| E04,E05,E70 | present_not_used | `disease-models/wwox/research/deepdive_manifests/PMID34634460.json` exists; the carbenoxolone paragraph, washout, NMDA/pannexin off-target and the 96 vs 87 percent Table S1 / text disagreement are in it (text 87 percent confirmed by me). Prior fate "omitted": BRIEF has no gap-junction question and "Combinations are later developments", confirmed | PASS. |
| E36-E40 | present_not_used | `cards/F04_nmdar_intervention_class.card.json` lines 306 and 529 hold the developing-rat apoptosis statement at abstract level; prior fate "narrowed": BRIEF has "do not deduce a therapeutic window ... from the absence of one apoptosis marker" | PASS with a nit: the quoted phrase "separate, longer exposures" is from the previous README ("Not resolved"), not from the BRIEF. |
| E78 | superseded_or_contradicted | where_in_legend is "this session D04": not a location in LEGEND | CORRECTION: point to a LEGEND location (for example `nmda_inv05_20261107/BRIEF.md` "Correct the external report's inferences" or `output/README.md` answer item 2). Prior fate "omitted" is acceptable (BRIEF does not address the "Refuted" label). |

Extra pointer checks that passed: E02 (`probes.tsv` d-APV row, mild GluN2A preference by compiled grading), E25-E27 (it6 README marks the GluN2B-to-GluN2A timing unverified for mouse cortex).

## D. Evidence sample (`evidence.tsv`, all 7 rows checked)

| Row | Verbatim? | Carries the proposition? |
|---|---|---|
| EV01 (40994429, D02) | yes, abstract | yes for what the sentence is; it shows the claim is a background statement. Fine. |
| EV02 (40994429, D01) | yes, abstract | carries only the variant panel (GRIN1/GRIN2B) half of D01. There is no row for 38529699 (GluN2A N615S, sex dependence, acute dosing), which is the central support of D01. |
| EV03 (15335108, D09) | yes, 23 words | yes. |
| EV04 (15335108, D09) | yes | yes. |
| EV05 (22261077, D06) | yes | yes. |
| EV06 (15075380, D05) | yes | yes for NR2A preference; as the note says, nothing on clinical outcome. |
| EV07 (12365832, D04) | yes | supports "the class failed in stroke", not D04's point (wording of "Refuted"); role should read context. Abstract also lists the failed drugs as "dextrorphan, GV150526, aptiganel and eliprodil"; licostinel absent, as the row says. |

Gap: no evidence rows exist for D07, D08, D10, D11, D12, D13, D14 (and D01's main paper). D08 and D13 rest on the module reading of 34634460, which I confirmed against the primary text; the others have no locator row, so a reader of `evidence.tsv` alone cannot trace them.

## Corrections the producer must make

1. `reconcile.tsv` row E11: legend_class and legend_novelty (nitrous oxide exists in `profiles_it23_p4_20261103/identity_join.tsv` line 1457).
2. `reconcile.tsv` row E78: replace "this session D04" with a LEGEND location.
3. `reconcile.tsv` rows E36-E40: attribute "separate, longer exposures" to the previous README, not the BRIEF.
4. `extraction.tsv`: add E91 (wording above); in E02 add "surmountable"; in E32 add "trapping".
5. `extraction.tsv` E14 and E16 notes: add that class prototypes ifenprodil and Ro 25-6981 are activity-dependent at abstract level (X1), so the "not use-dependent" premise is contradicted for the class, unverified for radiprodil.
6. `items.md`/`decisive.tsv` D01: replace "its only in vivo support" with "the only radiprodil in vivo datum the report cites"; add that 40994429's abstract itself reports a GluN2B-S810R slice and a PTZ in vivo result the report does not use; add sex dependence.
7. D03 and `queries.tsv` Q11: record the exact string and date; today's count is 4, not 5; list the 3 screened non-relevant titles.
8. D09: add that report L9 "psychotomimetic" has no support in the cited paper.
9. D10: replace "may not support" with: the 28782587 EPSC sentence describes the ketamine-induced increase in PND 7 rat anterior cingulate, not baseline; 21896318 is P7 mouse extrasynaptic fraction.
10. D11: "recording Mg2+ unmeasured" to "not stated in the source (1.3 mM in the incubation ACSF)"; mark the synaptic percentage as taken from the previous receipt; note the report hedges ("may").
11. D12: add that 19204407 found no damage at P14 and is titled high dose; 17312200 states doses "slightly larger" than clinical and "insufficient human data".
12. D13 and E01/E52: add the Supplementary Fig S3 datum (larger d-APV-sensitive delayed evoked response in S-KO), the neuron-specific Synapsin-Cre origin, bursts in heterozygotes, and the late-stage caveat; this narrows the report's "only direct NMDAR evidence" (L51) and "No WWOX-specific NMDAR data" (L136).
13. D14: add 5 of 8 survivors (37334223) and the 50 percent paediatric subgroup and concomitant anaesthetics (41409370).
14. D04/D05: add the internal inconsistency "the one competitive agent" (L125) vs two agents (L9, L30, L161), and the perzinfotel rat and stroke-programme abstracts (PMID 15764736, 9457246, 15907811) as bounds on the absence claim.
15. `evidence.tsv`: add locator rows for 38529699, 39970743, 34634460 (D08, D13), 28782587, 21896318, 41409370, 37334223, 20720132, or state in the file that these rest on the module; change EV07 role to context.
16. Add proposition D15 (X1) to the decisive list.

## Open uncertainties

- Full texts of 40994429 and 20720132 not reachable by the PMC tool (empty body), and Europe PMC returned HTTP 500 on my later attempts: D02's "no human datum" and D11's magnitudes are abstract-level or secondary.
- Nothing read beyond abstract for 28782587, 21896318, 15717010, 12520755, 17312200, 19204407, 23395831, 41409370, 37334223, 38529699, 39970743, 15335108, 22261077, 15075380.
- Supplementary Table S1 and Fig S3 of 34634460 not seen by me (text only).
- Perzinfotel clinical-development history outside PubMed not searched; ClinicalTrials-type registries not queried (authentication-gated connectors not used).
- Radiprodil gating/voltage/use properties unverified from any primary source here.
- PubMed counts (47, 11, 0, 4) are date-bound to 2026-11-08 and to the tool's query translation.
