# Partial benefit beyond the ISR-PDH axis: glial reactivity (IT6 package P10)

Actor `scientist-a`, task branch `task/it6-p10`, mandate `ORCH-ROADMAP-IT6-20261029`, written 2026-10-29. Non-canonical
research material: it changes none of the four scientific current files and writes nothing to the receipt ledger. Association
is not modulation and modulation is not rescue. Nothing here is medical advice; no dose, route, schedule or suitability is
given. Every row that is not measured in a WWOX-deficient system is labelled NOT WWOX EVIDENCE. The reference genotype class is
a WWOX-DEE genotype class; no individual-level record is used.

| File | What it is |
|---|---|
| `README.md` | this cycle, the abstentions and the searches actually run |
| `prediction_declared_20261029.md` | the organoid question, gene sets, decision rule and predictions, committed (`ac692d2e`) BEFORE the data were opened |
| `organoid_glial_panel_cpm.tsv`, `classify_panel.py`, `organoid_glial_panel_classified.tsv` | the panel and the rule applied as declared |
| `p47t_thresholded_query.py`, `p47t_thresholded_query.tsv` | named-gene query of the P47T supplementary sheets |
| `J01_glial_reactivity_modulation.packet.json`, `.card.json` | the card (abstention form, as `F02` and `H02`); the bridge builds it and `cards/check_cards.py` logic returns 0 problems on it |
| `needs_patch.diff`, `integration_note_p10.md` | the exact proposed edits to `needs/needs.json` and the statement about the coverage inputs |
| `../../receipt_staging/scientist-a/FTR-20261029-*.json` | five staged re-read receipts (the integrator records them; each passes `fulltext_receipts.py record --dry-run`) |

## 1. The thread, and why this one

Candidates examined: glia and myelin, redox balance, excitability other than the glutamate node, metabolic function, another
existing need. Chosen: **glial reactivity (NEED-NEUROINFLAMMATION-GLIA)**. The choice rests on the relation between the three things the task names.

* **WWOX evidence.** The need holds three observations from three papers and no card. Reading the sources again turned up a fourth
  (a rat mutant) whose sign is the OPPOSITE of the three, stated as such by its own authors, and a cell-type picture (no Wwox in rat
  microglia; astrocyte-specific deletion never scored for gliosis) that the need did not carry.
* **Available data.** All the sources have manifests and receipts, the organoid deposit and the P47T supplement are local, and the
  catalogue can be queried offline. A discriminating design can be written from time points that already exist in the literature.
* **A question that discriminates.** Whether glial density in a Wwox-deficient brain is below, equal to or above wild type BEFORE the
  first spike decides whether this need is a readout, a seizure consequence or a seizure-independent lever (section 9). Nothing in the record answers it.

Not chosen, and why (the searches are in section 11):

* **Redox** (`NEED-REDOX-OXIDATIVE-STRESS`): `WWOX[tiab]` with oxidative, ROS, redox, superoxide, glutathione, NRF2 or ferroptosis returned
  26 records, but the neural ones are a fly wing reporter, a neuronal-cell high-glucose model and cancer or lung/liver work; no WWOX-DEE
  neural measurement exists, so the sign cannot be settled from data in hand and the next step is a measurement, not a search. One
  descriptive line was added at no cost: in the P47T thresholded sheets no redox gene is listed in the forebrain regions and only
  Gsta4, Mt1 and Mt3 appear in the cerebellum sheet (a looser threshold), which is not a measurement. Left for a later package.
* **Myelin** is already carded (`F02`, `H02`) and its neuron-versus-oligodendrocyte genetics are carried there; this cycle only reuses them for the glial question.
* **Excitability other than glutamate** (chloride gradient, T-type calcium) is carded (`F03`, `H01`); NMDAR pharmacology belongs to another agent.
* **Metabolic function** was worked in iterations 3 to 5.

## 2. The WWOX observations, reconstructed with locators

Manifest entries are `disease-models/wwox/research/deepdive_manifests/PMID<n>.json verbatim_locators.entries[k]`. "Re-opened" means opened at
the source in this cycle (staged receipt); "carried" means taken from the manifest and not re-opened by me.

| # | Species, model | Cell / region | Stage | Comparison | Readout | n | Result | Source and locator | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | mouse, Wwox-null (full knockout) | hippocampus CA1, CA3, whole (dentate unmarked) | 2 weeks, both sexes | KO v Cre-positive WT | IBA1 and GFAP area fraction; Il6 qPCR | stereology and image fields; qPCR n 4 per group (registry reading) | both area fractions up; Il6 significant, Tnf-a not; cause v consequence left open; no seizure measure on these animals | Hussain 2019, PMID 30290271, entries 16, 17, 12 | text passages re-searched; figures carried |
| 2 | mouse, Wwox-null | brain, region NOT stated in the caption | P20 | KO v WT | GFAP and Iba1 percent area | not stated per panel | GFAP about 3.7 to 23.7 (***), Iba1 about 4.5 to 7.6 (*): about six-fold v 1.7-fold; SD bars | Obeid 2026, PMID 42422765, Suppl. Fig. S7 B and D, entry 44 | **re-opened**, mmc1.pdf page 9 |
| 3 | mouse, Wwox-null, neuron-restricted AAV9 at P5 | cortex (panel label, re-opened by the verifier) | read age not carried | treated v KO v WT | GFAP-positive cell count | not carried | about 5 (WT), about 44 (KO), about 5 (treated); the S7 treated-arm panels have no untreated-KO column and cannot be read across | Obeid 2026, S8 panel I, entries 9, 44 | carried |
| 4 | mouse, P47T knock-in homozygote | hippocampus CA1, CA3, DG | 80 and 250 days | P47T/P47T v WT | Gfap+ number and area; Iba1+ number | 3 per group per age, mixed sex | Gfap+ number about 39 and 56 (progressive, bracketed); Iba1+ about 34 at both ages (not progressive); mutant microglial branching falls with age | Hussain 2023, PMID 36828035, entries 20, 21, 22 | carried; text paragraph re-read |
| 5 | mouse, P47T homozygote | PFC, CTX, HPC | adult | v WT | regulator and pathway inference (TNF, NF-kB, IL1B, RELA; IL6-JAK-STAT3 set) | 5 per group, RNA-seq | positive in all three regions; transcriptomic inference, not a cytokine measurement | same, entry 41 | carried |
| 6 | mouse, P47T homozygote | cerebellum | adult | v WT | Il1b, Tnf qPCR | 6 per group | at least two-fold up; ranges overlap WT | same, entries 42, 43 | carried |
| 7 | **rat, lde/lde (13-base-pair exon 9 deletion)** | **cerebral cortex** | **PND 5, 10, 15, 21** | lde/lde v +/+ males | GFAP+ and Iba1+ cells per mm2; western | at least 3 per genotype per age | **LOWER**: GFAP+ cells about 470 v 255, 620 v 330, 1100 v 540, 1570 v 850 (about half from PND 5); Iba1+ 50 v 45 (ns) then 190 v 135, 380 v 215, 320 v 190; GFAP western lower at PND 15 only; Iba1 western lower at all ages | Tochigi 2019, PMID 31340538, entries 4, 7, 9, Fig. 5 B, D, E | **re-opened**, text and Fig. 5 at native size |
| 8 | rat | microglia, astrocytes, oligodendrocytes | PND 21 | +/+ | Wwox immunostaining | not stated | in neurons, astrocytes (dot-like), oligodendrocytes; NOT in Iba1+ microglia | Tochigi 2019, entry 5, Fig. 6 | text re-read |
| 9 | mouse, GFAP-Cre (astrocyte) and Olig2-Cre deletions | astrocytes, oligodendrocytes | P17 and survival | KO v control | delay, weight, survival | G-KO 9 v 8; O-KO 10 v 11 | no abnormality; **gliosis, EEG and seizures not reported for G-KO**; authors: a cell-autonomous function in astrocytes is not excluded | Repudi 2021, PMID 33914858, entries 29, 39, Fig. 1J-O legend | **re-searched** (staged) |
| 10 | mouse, P47T/WT heterozygote, LPS challenge (preprint) | cortex, hippocampus | adult, 12 h | het LPS v WT LPS | microglia, astrocytes, cytokines | 9 per group, 7 of 36 removed as outliers | cortical astrocytes up under LPS (0.0005; own response 0.0040), hippocampal astrocytes flat; TNF-alpha differs, IL-1beta and IL-6 do not; plasma response is the WILD TYPE's | De La Cruz 2025, PMID 39868255, entries 15 to 21, 29 to 31, 34 | carried |
| 10b | mouse, P47T/WT heterozygote, unchallenged | brain (Iba1, Gfap immunostaining) | adult | het v WT | Iba1 and Gfap immunostaining | not stated | "no differences ... (data not shown)": an unverifiable negative, not evidence that the heterozygote is normal | Hussain 2023, PMID 36828035, entry 11 | carried |
| 13 | mouse, neuron-restricted deletion (Synapsin-Cre, S-KO) | cortex and hippocampus bulk RNA-seq | P17 | S-KO v S-Control | top differentially expressed genes, among them genes "elicited during epileptic insults including activation of astrocytes" (Fig. 3A, B) | cortex 4 control v 3 KO; hippocampus 2 v 3 | astrocyte-activation-type genes shift in a brain whose astrocytes are expected to keep Wwox because the driver is neuronal (the paper stains intact Wwox only in CC1+ oligodendrocytes, Supplementary Fig. 1D; astrocytic retention is inferred from the driver, UNVERIFIED by staining); the S-KO seizes from P9. Genes not individually tabulated here | Repudi 2021, PMID 33914858, text of Results and Fig. 3 legend, re-searched 2026-10-29 | text re-searched; the heat map was not re-opened |
| 11 | human cerebral organoid, WWOX knockout | bulk RNA | week 15 | 4 KO v 2 WT libraries | reactive, microglial, cytokine transcripts | 6 libraries | no reactive programme; microglia absent (section 4) | GSE156243 (deposit of PMID 34268881), this cycle | computed here |
| 12 | mouse, P47T homozygote | PFC, CTX, HPC, CB | adult | v WT | thresholded DEG rows | 5 per group | canonical reactive and cytokine transcripts not listed (section 5) | PMID 36828035 supplement, this cycle | queried here |

Seizure timing the glia have to be read against (corrected after verification): Repudi 2021 reports spontaneous tonic-clonic seizures "beginning at P9"
in the neuron-restricted knockout (n = 6 of P14-18 for duration) and, in the null mouse, growth retardation and seizures "within a few days after birth" (Results, text re-checked
2026-10-29). The null mouse's recordings in PMID 42422765 begin at about P14 and show spikes (Fig. 7; text re-read), so a recording before P14 does not exist in THAT paper, but the onset
window is earlier than P14 in the Aqeilan-group mice: **P5 to P8 are the only plausible pre-onset ages**, and the earliest glial reads (P14, P20) are all after onset. The rat's seizures are
sound-evoked after PND 16 (Tochigi Discussion, citing refs 12 and 13, not re-read), so its PND 5 to 15 deficit sits before sound-evoked seizure competence, which is not the same as before any
seizure (no EEG there). The P47T homozygote has chronic spontaneous generalised seizures in adults (> 6 weeks), onset age not stated (entries 59 to 61).

What follows from the table (an inference, marked INFERENZA): the three "excess" rows are from the null and the missense mouse, the one "deficit" row is a
rat in a different region with a different assay and a mostly earlier window. The five differences (species, allele, region, assay, age
window) are confounded; one within-species time course would unconfound them. Row 13 adds that a neuron-only deletion, whose astrocytes keep Wwox, already shifts astrocyte-activation-type genes at P17: that fits H-seizure or H-signal better than an astrocyte-intrinsic cause (H-glia), without separating H-seizure from H-signal.

## 3. Re-reads, each with its new question (staged, not recorded)

All QUESTION_DRIVEN. Prior receipts were reused; no complete re-read was made.

| Staged event | Source | New question | Surface | Depth | Prior |
|---|---|---|---|---|---|
| `FTR-20261029-31340538-01` | Tochigi 2019 | readout, ages, region and n of the reduced glia; before or after seizure competence? | JATS text, Results 2.2 and 2.3, Discussion; Fig. 5 native | partial | FTR-20261019-31340538-01 |
| `FTR-20261029-42422765-01` | Obeid 2026 | age and region of the glial excess; any read before the first spike? | mmc1.pdf p. 9 (S7) rendered; ECoG text | partial | FTR-20261023-42422765-01 |
| `FTR-20261029-30290271-01` | Hussain 2019 | was seizure state recorded in the 2-week mice? | r2 JATS (the earlier receipt's HTML path is not present on this host) | queried | FTR-20260806-30290271-01 |
| `FTR-20261029-33914858-01` | Repudi 2021 | what was scored in the GFAP-Cre and Olig2-Cre deletions? | operator-supplied text; supplementary legend text | queried | FTR-20261003-33914858-03 |
| `FTR-20261029-36828035-01` | Hussain 2023 | are the canonical reactive and cytokine transcripts in the thresholded sheets? | derived text of the supplementary sheets | queried | FTR-20261021-36828035-05 |

What the re-reads changed: (a) Fig. 5 shows the rat deficit is present from PND 5 and roughly constant at half of wild type for GFAP, and the
Iba1 western and Iba1 counts disagree in size at PND 10 (about 0.04 v 0.9 on the blot, about 135 v 190 cells); (b) S7 gives the null
mouse excess a size (six-fold astroglial, 1.7-fold microglial) and no region; (c) the 2-week mouse glial read has no seizure
measure; (d) the astrocyte-specific deletion was scored for delay, weight and survival only; (e) the P47T sheets carry none of the canonical transcripts. The manifest for PMID 30290271 cites a saved HTML
that is not on this host; this cycle used the PMC r2 JATS (sha256 `3672e629...`), which a verifier should use.

## 4. The organoid panel (GSE156243, pre-declared)

Prediction file committed before opening the data. Rule applied as declared by `classify_panel.py`. Data: four knockout and two wild-type
libraries, week 15, from `files/geo/GSE156243/` (unchanged; not redistributed). Note: WWOX CPM is not lower in the knockout libraries
(about 13.7 v 9.9), consistent with the deposit's known engineered lesion, so the genotype label, not the transcript, defines the contrast.

| Set | Result under the declared rule |
|---|---|
| Microglia presence | P2RY12 0, CX3CR1 about 0.03, PTPRC about 0.1, TREM2 about 0.1 to 0.2 CPM: absent. AIF1 about 8 CPM (not specific to microglia in a neural tissue) not separated; CSF1R not separated. TMEM119 is classed RAISED by the rule (about 1.7 v 0.4 CPM) but it rests on one library (168 raw counts against 26 to 32) at trace level and is not interpreted |
| Astroglial lineage and homeostatic (14) | 12 not separated, including GFAP (135 v 154 CPM), SLC1A2, SLC1A3, KCNJ10, ADK (15.2 v 15.2), SOX9, FABP7; GJA1 raised (17.6 v 3.3) and AQP4 raised (0.74 v 0.22, trace) |
| Reactive-pan (10) | genes above 5 CPM in any library: 7 (C3, CD44, VIM, TIMP1, CEBPD, STAT3, SOCS3); RAISED: 2 (VIM 3214 v 1765; CD44 29.7 v 7.6, both radial-glia/progenitor-associated); LOWERED: TIMP1, SOCS3, and SERPINA3 (which is lowered by the rule but never exceeds 3.1 CPM, so it is not among the 7) (SOCS3 5.7 v 14.2, a STAT3 target, with STAT3 itself not separated); C3, CEBPD, STAT3 not separated; LCN2, CHI3L1 not informative. 2 of 7 is under the declared half: **no seizure-independent reactive programme in this tissue** |
| Cytokine and inflammasome (10) | IL1B, IL6, TNF, CXCL8 not informative (under 20 raw counts); NLRP3 and IL1R1 ratio about 2 at 0.5 CPM, not separated; NFKB1, RELA, CCL2, TGFB1 not separated |

Against the predictions: P1 (microglia near zero) held for the specific markers; P2 (astroglial markers shift with the known maturity
difference) was **wrong in form** (nothing coherent shifts apart from GJA1 and the progenitor-type VIM and CD44); P3 held for its four named genes
(C3 not separated, SERPINA3 lower, LCN2 and CHI3L1 not informative); P4 failed as worded for NLRP3 (ratio 1.95 at 0.6 CPM, one library at 33 raw counts), and is not evaluable for IL1B, IL6, TNF. Reading: this
is evidence that, in a human neuron-containing tissue **without microglia and without behavioural seizures**, WWOX loss does not by
itself produce a reactive-astrocyte or cytokine transcript programme at week 15. It does not say the same of a seizing brain, of an
adult, or of microglia. Four against two libraries from one laboratory; no test; transcript level.

## 5. P47T thresholded sheets (queried, not read in full)

`p47t_thresholded_query.py` on the derived text (sha256 `1ac2a870...`). The forebrain sheets list genes with |log2 ratio| at least 1 (HPC 1508 rows, as
the paper states); the cerebellum sheet goes down to about 0.3. Not listed in any region: Gfap, Aif1, Il1b, Tnf, Il6, Lcn2, Serpina3n,
Nlrp3, Stat3, Socs3. Listed: Serpina3g (PFC 2.11, CTX 2.11), Serpina3h (PFC 1.31, CTX 1.91), Nes (PFC 1.17), C3 lower in HPC (-1.26),
and Oas1f up by 6.0 to 7.3 in all three forebrain regions (an interferon-stimulated-family gene with an unexplained size; the paper's Supplementary Fig. S1a places Wwox on chr8, the chromosome of the Oas1 family was NOT checked, and a strain or passenger effect is a possibility that was NOT tested: UNVERIFIED). Il1b and Tnf, which the
paper reports at least twofold up in cerebellum by qPCR, are not in the cerebellum sheet either. **Absence from a thresholded list is
not a measurement of no change**; what the query establishes is that the paper's regulator-level inflammatory inference does not rest on the canonical reactive
or cytokine transcripts being beyond a two-fold threshold.

## 6. Need to compounds (catalogue)

`python3 framework/scripts/repurposing_search.py need NEED-NEUROINFLAMMATION-GLIA --limit 2000 --json` (offline, 2026-10-29): 854 association rows; 738 on
intervention targets (of the 101 rows excluded under the catalogue's own rules, 96 fall among these 738 and 5 among the 116), 116 on readout markers (GFAP 44, IL6 72) which are never links. **Base for every figure that follows: the 642 non-excluded intervention-target rows (738 - 96)**: 465 families; 439 carry no stated action and 203 a stated lowering (439 + 203 = 642); only **59 are curated ChEMBL mechanism rows**
(JAK2 36, TNF 15, IL1B 5, NFKB1 1, NLRP3 1, RELA 1). Status classes on the same 642 rows: no statement 343, approved in any source 248, clinical candidate 48.
No row has a WWOX context. The list is an exploration list by the need's own direction (`uncertain`), not a list of favourable treatments, and it is not ranked here.

**Gap found.** `target IL1R1` returns anakinra, AMG-108 and MEDI-8968; `target CASP1` returns belnacasan, emricasan and nivocasan; neither target is on the need, so the two IL-1-axis
agents with epilepsy exposure (an IL-1 receptor antagonist and a caspase-1 inhibitor) were NOT reachable from the need as written (the DGIdb record for anakinra reached the need only through an NLRP3 row).
IL1R1 (HGNC:5993) and CASP1 (HGNC:1499) are proposed as targets in `needs_patch.diff` (verified against the HGNC REST service, read-only, 2026-10-29; CSF1R HGNC:2433 and IL6R HGNC:6019 checked and not
proposed: CSF1R would add multi-kinase inhibitors with no rationale here, and microglia lack detectable Wwox; IL6R has no WWOX-system observation behind it).

## 7. Compound to contexts (reverse search)

`repurposing_search.py compound <name>` for: anakinra, canakinumab, dapansutrile, ruxolitinib, baricitinib, minocycline, ibudilast, belnacasan, VX-765, pexidartinib, MCC950, disulfiram,
tocilizumab, fingolimod. What the catalogue says (it holds ids, direction and status, not potency or approval for any person): anakinra, canakinumab, dapansutrile, ruxolitinib,
baricitinib, ibudilast and MCC950 reach only this need (JAK2, IL1B, NLRP3, IL6 rows; direction unresolved); minocycline (DGIdb record with 9 target rows) and fingolimod, tocilizumab, pexidartinib and
belnacasan reach **no need** (belnacasan only through the target the patch adds); disulfiram reaches the mTOR need and this one (NFKB1 and the GFAP marker row). None of these
compounds has a card or a WWOX-system assertion, which is why the card is an abstention.

## 8. External precedents, checked at the source (abstract level; NOT WWOX EVIDENCE)

Each was retrieved from PubMed on 2026-10-29 and **only the abstract was read**; none carries a receipt; every statement below is limited to what the abstract says.

| Precedent | Context | What the abstract says | Use here |
|---|---|---|---|
| Giussani 2025, PMID 40614647 | cryptogenic NORSE/FIRES, 14 patients, Italy, retrospective, no comparator | later anakinra use goes with longer intensive care; "no evidence of efficacy on the long-term neurological outcome was demonstrated" | uncontrolled and uninformative for long-term outcome (absence of evidence, not a negative); acute post-infectious syndrome |
| Hanin 2024, PMID 38430119 (pooled case review) | NORSE/FIRES: 28 case reports and series, 75 patients, 52 on anakinra | seizure control within two weeks for up to 73 percent on anakinra (70 percent tocilizumab); no clear effect of timing; "most patients experienced long-term disability and drug-resistant post-NORSE epilepsy"; late anakinra or tocilizumab reduced seizure frequency in 67 percent of a few cases; authors call for prospective studies | acute seizure-control signal in uncontrolled reports with long-term outcome unchanged; added after verification; the acute, immune-triggered context is not the WWOX one |
| Feng 2025, PMID 40481521 | chronic FIRES, three patients, minocycline | one patient had shorter seizures; no significant change in overall seizure frequency | uncontrolled three-patient series, uninformative; not a counter-precedent |
| Chen 2026, PMID 42111266 (review) | pyroptosis in epilepsy | the review abstract says VX-765 "demonstrated favorable safety and preliminary efficacy" in a phase II randomized trial in refractory epilepsy and that the trial "did not meet its primary efficacy endpoint"; MCC950 was discontinued after hepatic findings | **UNVERIFIABLE at trial level**: the registry record NCT01048255 (COMPLETED, checked 2026-10-29 through the registry API, read-only) lists a SAFETY and tolerability primary outcome at 18 weeks and has no posted results; no peer-reviewed trial report was found; the review's "primary efficacy endpoint" wording cannot be confirmed, and its "preliminary efficacy" wording was omitted earlier. Not used as a counter-precedent |
| Galanopoulou 2017, PMID 28462453 | rat multiple-hit infantile-spasms model | VX-765 (and two other agents) had no acute or delayed effect on spasms, well tolerated | counter-precedent in a developmental model |
| Genin 2026, PMID 41841337 | Scn1a+/- Dravet mouse | astroglial GFAP rises from the aggravation phase (PN20 to 35) relative to an earlier presymptomatic time point; remodelling without tissue damage | a genetic-DEE precedent where glia are tracked against stage with video-EEG: the design template of section 9 |
| Bedner 2015, PMID 25765328 | human TLE tissue and a mouse model | astrocyte uncoupling temporally preceded neuronal death and spontaneous seizures; induced by LPS | glial change can be upstream of seizures in an acquired model |
| Hristova 2016, PMID 26669927 | neonatal hypoxia-ischaemia mouse | neuronal STAT3 deletion reduced cell death, tissue loss and microglial and astroglial activation; astroglia-specific deletion reduced cell death, tissue loss and microglial activation (astroglial activation not stated for it); JAK2 inhibition reduced both activations moderately | a neonatal-injury precedent that STAT3 signalling can be harmful; acute injury, not epilepsy |
| Giussani and others (PMID 42367793, 41265024, 40831349) | FIRES case reports and reviews | titles only; not read | listed so the search is auditable, not used |

## 9. Counter-evidence (consolidated)

1. The rat shows the opposite sign, from PND 5, and its authors say so (row 7).
2. The human organoid shows no reactive programme (section 4); the P47T sheets do not carry the canonical transcripts (section 5).
3. Microglia carry no detectable Wwox in the rat; for the astrocyte the deletion was not scored for gliosis (rows 8, 9): the "cause" cannot be assigned to a glial compartment either way.
4. The neuron-restricted rescue that lowers GFAP also stops seizures and restores survival (row 3): the fall in GFAP does not tell which route it used.
5. The verified compound precedents are acute or post-infectious and are **uncontrolled or uninformative for long-term outcome**, with acute seizure-control reports for anakinra (up to 73 percent within two weeks in a pooled case review, uncontrolled) and no usable trial-level result for VX-765 (section 8). They do not show harm; they do not support transfer to a congenital neuron-intrinsic loss either.
6. The P47T heterozygote LPS result is a difference in significance in places, with seven of 36 animals removed asymmetrically and a plasma response that is the wild type's (row 10; entries 9, 25 to 34).
7. Glial direction is context-dependent in the abstracts read: STAT3 removal reduced glial activation and damage in neonatal hypoxia-ischaemia and astrocyte uncoupling preceded seizures in a TLE model (section 8), so "dampen gliosis" is not "remove a cause". The commonly stated protective role of reactive astrocytes was NOT verified here (search (i) was not read).

## 10. Transferability

| Axis | Position |
|---|---|
| Non-neural v neural | every compound precedent is immune-mediated or injury-triggered in a brain that developed normally; the WWOX lesion is congenital and neuron-intrinsic. No non-neural WWOX glial datum is used |
| Knockout v missense | the excess is seen in the null (rows 1 to 3) and in a WW-domain missense knock-in (row 4); NO glial datum exists in a catalytic-domain missense allele, so no statement is made for it |
| Acute v chronic | the null dies at about three weeks (rows 1 to 3 read at P14 to P20); the P47T homozygote is read at 80 and 250 days; the compound precedents are acute |
| Species | mouse excess, rat deficit, human organoid null; no human tissue glial datum |
| Partial v full loss | the unchallenged P47T heterozygote is reported to show no gliosis, "data not shown" (row 10b: an unverifiable negative); the LPS preprint is the only other partial-loss glial datum and is weak (row 10) |

## 11. The searches actually run (2026-10-29)

PubMed (the tool's own translation is the one listed): (a) `WWOX astrocyte OR microglia OR astrogliosis OR neuroinflammation` and (b) `WWOX oxidative stress OR ... redox neurons OR brain` returned
271,002 and 3,025,421 records because the operator precedence was mistranslated; **discarded**. (c) `WWOX[tiab] AND (astrocyte* OR microglia* OR gliosis OR astrogliosis OR neuroinflammation OR oligodendrocyte* OR myelin*)`: 15 records (31340538 and 39868255
and the four mouse papers already carried; 15664696 and 16941225 older localisation papers; 37781246 glioblastoma lines, not used; 42128308 a 2026 review, not used; 41442931 and 42721537 clinical, not used).
(d) `WWOX[tiab] AND (oxidative OR "reactive oxygen" OR ROS OR redox OR superoxide OR glutathione OR NRF2 OR ferroptosis)`: 26 records; titles read, none a WWOX-DEE neural redox measurement; redox thread not taken.
(e) `anakinra AND (FIRES OR NORSE ...)`: 78 records, the tool translated FIRES as the word "fires", so the list was screened by title and two relevant ones read; (f) `VX-765 OR belnacasan OR "caspase-1 inhibitor" AND (epilepsy OR seizures) AND (trial OR phase)`: 11, read;
(g) `minocycline AND (seizures OR epilepsy) AND (randomized OR trial OR "clinical trial")`: 17 records (15 returned), not screened individually; the one relevant record (40481521) came through (e); (h) `astrocyte STAT3 conditional knockout epilepsy OR seizures OR epileptogenesis`: mistranslated (199,603), **discarded**, redone as
`(astrocyte* AND STAT3) AND (seizure* OR epilep*) AND (knockout OR deletion OR inhibitor)` [tiab]: 9, read; (i) `"reactive astrocytes" AND (protective ...) AND (epilepsy OR seizure) AND review`: 4 records, **not read** (titles not retrieved);
(j) `"adenosine kinase" AND astrogliosis AND epilepsy`: 23 records, **not read** (no catalogue compound for ADK: `target ADK` returned 0 rows); (k) glial change preceding seizures in genetic epilepsy (tiab): 3, read. Catalogue: `repurposing_search.py need`,
`target` for IL1B, NLRP3, JAK2, STAT3, CASP1, IL1R1, CSF1R, ADK, TNF, NFKB1, IL6R, GSDMD and `compound` for the fourteen names in section 7.
Not run: ClinicalTrials.gov (the census of 2026-10-20 is cited, not repeated), any search for cell-type-specific Wwox expression in a single-cell atlas (UNVERIFIED which cell types express WWOX in human cortex), any search for a WWOX-null astrocyte culture.

## 12. The next experiment that discriminates

**Question.** Is glial density in a Wwox-deficient brain below, equal to or above wild type BEFORE the first spike, and does the sign change after it?

**Design (wet-lab, not done; no compound).** Wwox-null (or neuron-restricted deletion) pups with wild-type littermates. Sampling at P5, P8, P11, P14 and P17 (the null dies at about three weeks); in the same animals, GFAP and Iba1 density and area fraction on the same sections
in cortex AND hippocampus (so both prior readouts, the rat's density and the mice's area fraction, are measured in both regions); continuous cortical recording from the earliest age an electrode can be placed (the paper's own recordings start at about P14), each animal classified before or after its first spike by a blinded reader; Wwox-null pups treated with the neuron-restricted vector as a control for the neuronal route.
Statistics at the animal level, not the field.
Limits of this design, added after verification: (1) histology is terminal, so each age is a separate cohort; "same animals" means the same sections across readouts within an age, and "before or after first spike" can be assigned to an animal only if its own recording covers the pup from before onset to the sampling age. (2) Spontaneous seizures are reported from P9 in the neuron-restricted deletion, so P5 and P8 are the only plausible pre-onset ages; placing an electrode and recording from P5 in a pup of a few grams (about 5 g at P15 in the null, per PMID 42422765 Fig. 3C, which is far lighter at P5) is a feasibility risk and may need a different method (for example video-scored behaviour plus a terminal acute recording). (3) A recording that starts at P14 cannot show that no spike occurred earlier, so "before first spike" is claimed only for animals recorded from the sampled age itself. (4) The rat deficit is cortical and the mouse excess hippocampal or region-unstated; the design measures both regions, which is its strength.

**Predictions, fixed here, before any new data.**

| Reading | Glial density before first spike | After it |
|---|---|---|
| H-seizure: gliosis is a consequence of seizure-network activity | equal to wild type | above |
| H-delay: neuron-intrinsic glial maturation lags first (the rat picture), then seizures push it up | **below** wild type (as the rat at PND 5 to 15) | crosses to above |
| H-signal: a seizure-independent neuron-derived signal drives it | **above** | above |
| H-glia: astrocyte-intrinsic requirement | below or above regardless of seizures; would need an astrocyte-specific arm scored for GFAP and EEG, which does not exist | |

The organoid result (section 4) is compatible with H-seizure and H-delay and argues against H-signal in that tissue only. Interpretation: if the sign before the first spike is "equal" or "below", this need
is a readout and a seizure-dependent marker and the glial-lever question stays closed; only "above before the first spike" opens a lever question, and even then the first arm would be genetic (an astrocyte or microglia-specific rescue), not a compound.
A compound arm is deliberately not designed.

## 13. Card, abstention, patch

* **Card.** `J01_glial_reactivity_modulation` (axis J, route BENEFICIO_PRECOCE, track A), status `abstention`, same form as `F02` and `H02`: seven disease assertions with receipts that are already recorded, no drug assertions, `directional_summary` UNRESOLVED, `abstention` NO_DRUG_ASSERTIONS_SUPPLIED. A card in this form is justified because the need now has a time-ordered, species-conflicting record and an auditable search; a promoted candidate card is not, because no compound has an assertion in a matching context. It is placed here, not under `cards/`, because the integrator owns that directory; it cites only recorded receipt ids so that it passes the cards checker unchanged when moved.
* **Abstention.** No compound is promoted for glial reactivity. Reopening condition: a time course of glial density against first spike in a Wwox-deficient model, or any glial endpoint under a compound in a Wwox system.
* **Patch.** `needs_patch.diff` (a unified diff against `needs/needs.json`, applied and checked by `needs/check_needs.py --file` on a scratch copy: 0 problems after this README exists) adds observations O4 to O8, two inferences, two counter-evidence lines (three entries), the rationale and `do_not_assume` clauses, targets IL1R1 and CASP1, and the note.
  After integration: place the card under `cards/`, add it to the need's `sources.cards`, then `repurposing_coverage.py run` and `repurposing_view.py run`. Coverage inputs: see `integration_note_p10.md` (no row proposed, with reasons).

## 14. UNVERIFIED, owed

* Every external row in section 8 is abstract level; the VX-765 phase II efficacy result is UNVERIFIABLE at trial level (review wording only; the registry lists a safety primary outcome and no results); the pooled anakinra review (Hanin 2024) is abstract level.
* The seizure onset age in the lde/lde rat (sound-evoked after PND 16) is from the Discussion of the 2019 paper citing earlier papers, which were not re-read.
* Whether the null-mouse S7 tissue is cortex, hippocampus or whole brain (the caption gives none); whether the 2-week mice of PMID 30290271 were seizing.
* The reason the cerebellum Il1b and Tnf qPCR rise is not in the cerebellum RNA-seq sheet; the Oas1f outlier (strain or passenger effect not checked).
* Whether GFAP-Cre recombination in the G-KO mice is astrocyte-restricted (the paper validates by GFAP immunofluorescence).
* The panel figures at P47T Fig. 3 and 4 and Hussain 2019 Figs. 3 and 4 are carried from manifests and were not re-opened.
* Cell types expressing WWOX in human cortex (not searched).
* Everything in sections 4, 5 and 12 marked INFERENZA is owed a blind audit by someone other than its producer.
