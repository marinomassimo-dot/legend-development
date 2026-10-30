# IT9 P1 independent verification (verifier report)

Verifier delegate of the Orchestrator, 2026-10-30, branch `task/it9-p1v`, read-only toward the package under test
(`disease-models/wwox/research/drug_repurposing/generation_it9_p1_20261030/`, main at f12a970d). Exploratory,
descriptive. Not medical advice. No individual-level data was used or sent anywhere; the only network calls were
PubMed/PMC retrievals by PMID or PMCID and HGNC REST lookups of gene symbols.

## 0. Method and depth (what "re-derived" means here)

* Sample: 48 seed rows drawn by stratified random draw (seed 9), then about 30 more read in the second pass because a
  first-pass finding pointed at them. Strata covered: all five questions (Q1 to Q5) and dropped D1 to D6; observation
  classes expression, protein or phospho, functional effect; usable, reserved and unusable; 'uncertain' direction
  (S005, S024, S035, S040, S042, S044, S061, S067, S076, S085 and more); mouse and rat rows (S058, S061, S062, S064
  to S066, S075, S077, S078, S082, S083 and more).
* Step 1 for every sampled row: the cited `needs/needs.json` statement and its limits were read (locator depth).
* Step 2, primary paper, depth stated per paper:
  * FULL TEXT (PMC, whole text returned by the tool; keyword-targeted reading for the longer ones): PMID 34634460
    (read whole), 30290271 (whole), 28749468 (whole), 31543760 (whole), 35328751 (targeted: PDH, PDK, lactate,
    knockout/silencing), 41124647 (targeted: P252A, P282A, POLE4, CHX, MG-132, mRNA), 36828035 (targeted: video EEG,
    cytokines, GSEA), 34268881 (targeted: GAD67, NPY, glycolysis, LFP, Wnt).
  * ABSTRACT ONLY: 29808465, 25012504, 31340538, 42397075 (Brain 2026, no PMC), 33914858 (Brain 2021, no PMC),
    34747138.
  * NOT OPENED: 42422765 (AAV paper; rows S013 to S015, S092 and the baseline numbers carried into S075, S080, S081),
    36537114, 32000863, 38563965, 30853297. Rows resting only on these are verified at locator depth only.
* Everything below that says "contradicts the source" was checked against text returned by the tool; the PMC
  extraction strips italic gene and allele names, so a few sentences are readable only by structure (flagged where it
  matters).

## 1. Decision-level summary

* No hard failure of the package's structure: `check_seeds.py` PASS (111 rows, 70 HGNC-bearing rows, 0 failures);
  the closed-world test passes; 12 HGNC symbols re-fetched live agree with `hgnc_check.tsv` (section 5).
* Content findings: 4 HIGH, 11 MEDIUM, 9 LOW. The HIGH items are (H1) a carried factual error on Tnf/Il6 that makes
  S085 'uncertain' wrong, (H2) intervention-arm information written inside USABLE rows (S081 reason, S067 guard),
  (H3) dropped question D1 mixes a well-founded Wnt-bulk drop with a MYC/radial-glia sub-question that the stated reason
  does not touch, and (H4) the usable/reserved rule is applied by quantity in some places and by presence in others,
  so the usable side carries the very endpoint magnitudes that the reserved side holds out.
* Most sampled rows re-derived at the depth available (section 3); the findings below are the exceptions. I did not tally
  a pass rate: rows differ in depth, and a count of rows is not a result.

## 2. Row-level findings (stratified sample and follow-ups)

### HIGH

* **H1. S085 (TNF, Q5, direction 'uncertain') and S086 (IL6) rest on a reading that the primary paper contradicts.**
  Locator NEED-NEUROINFLAMMATION-GLIA:O1 (PMID 30290271) says "Il6, not Tnf-a, is significant by qPCR (registry
  reading)". The paper's Results 3.3 says "We observed > 1.5 fold upregulation of both cytokines (significant at
  p < .05) in KO (n = 4)", and the abstract says "overexpression of inflammatory cytokines Tnf-a and Il6". In the P47T
  paper (36828035) both cytokines are at least 2-fold up (n = 6). So the Wwox-null hippocampus is up for Tnf as well, S085's
  reason "sign not consistent across the two mouse models" is false, and the row should be up (mouse, two models), with the
  rat as the only opposing system. Level also needs care: the P47T and null values are qPCR transcripts (expression),
  correctly typed. Fix at the needs-table source, not only in the seed. Depth: full text (30290271), targeted (36828035).
* **H2. Intervention-arm information is written into USABLE rows (leak into generation).**
  (a) S081 (AIF1, Q5, usable): the reason text contains "in the neuronal-AAV9 supplement the Iba1 panel shows no significant
  difference among arms", and its locator cites NEED-NEUROINFLAMMATION-GLIA:O3, the AAV add-back statement. That is an
  intervention-arm result inside a usable row. (b) S067 (GAD1, Q4, usable): the `evaluation_guard` column reads "the
  protein-versus-transcript split (rescue normalises GAD67 area but not transcript) is an add-back response and is held
  out", which states the add-back result in the very row a generator reads. The paper (34268881) confirms the add-back
  reverses GAD67 immunostaining and that the RNA 'followed the same trend' only for the knockout-versus-wild-type
  contrast; the guard sentence is accurate but must not travel with the usable row. Remove both sentences from usable
  rows (put them in a reserved row or a P3-only file).
* **H3. Dropped question D1 conflates two different questions; the MYC/radial-glia part is supported and the stated reason
  does not apply to it.** D1's reason is that the alteration "cannot be separated from maturity/composition" because
  Wnt readouts move with culture time in 62 unperturbed spheroid samples and a 4 v 2 permutation has minimum p 1/15.
  Both facts concern bulk Wnt transcripts (S094 to S099), and for those the drop is sound. The MYC rows are different:
  S100 is single-cell, radial-glia-resolved (MYC the top upregulated gene in knockout radial glia) and S101 is a protein-level
  readout (MYC+ fraction of SOX2+ cells about 60, 50, 55 percent v about 20 percent) in the engineered knockout AND two
  patient-derived lines, and NEED-MYC-PROGENITOR-PROLIFERATION:O2 records MYC up in radial-glia pseudobulk in all three
  (logFC about 1.8, 1.65, 1.6). A within-cell-type contrast is the standard answer to a composition confound; maturity
  within radial glia remains open, and the cell-cycle panel has no error bars (O1 limits), but neither point is the stated
  reason. The abstract of 42397075 (abstract depth only) states radial-glia cell-cycle disruption and MYC overexpression
  in knockout, with milder phenotypes in patient lines. Recommendation: split D1 into D1a Wnt (drop stands) and D1b
  MYC/radial-glia (reconsider as a retained question or keep dropped with a MYC-specific reason, for example n of
  organoids single-digit and no error bars). The only lever (A51) is correctly held out either way.
* **H4. The usable/reserved boundary is applied by presence in some rows and by magnitude in others.** README section 3
  says presence of hyperexcitability or hypomyelination is usable and the quantity is reserved ("burst frequency",
  "myelinated-axon counts", "g-ratio", "gliosis under add-back" are held-out endpoints). Yet usable S077 carries
  "about 3.3 times fewer myelinated axons" (and the evaluation_guard on S077 names the same count as the held-out
  endpoint); usable S058 carries slice bursting 36/42, 4/23, 0/11 and its own guard calls burst frequency an endpoint; usable
  S059 carries Ca2+ firing "WOREE about 3-fold above SCAR12" while reserved S015 scores the add-back on exactly that spontaneous
  Ca2+ firing; usable S080 carries GFAP area 23.7 v 3.7 percent while reserved S092 scores gliosis on GFAP-positive cells;
  usable S006 carries "chronic spontaneous generalised seizures" while S075 holds seizure burden out. A generator sees the
  endpoint scale it will later be scored on. Fix: state presence only on usable rows (the counts live in the source
  locator), or declare that baseline (untreated genotype) magnitudes are usable and only the treated-versus-untreated
  contrast is reserved, and apply that to S075, S014 and S110 too (see M7).

### MEDIUM

* **M1. S030 and S031 (Q2, human knockout fibroblast, PMID 35328751): the reason misstates the source and a usable row is
  missing.** S030 says "no PDK activity or protein measured". The paper's Results say "the activities of pyruvate
  dehydrogenase kinase (PDK) and citrate synthase (CS) were not changed" (normoxia normoglycaemia) and, in a later
  condition, "no significantly important differences in the activity of pyruvate dehydrogenase" (the text is
  internally ambiguous about which enzyme the assay measures), and the qPCR section says "expression levels of SLC2A1,
  SLC2A4, ENO1, PKM2, and PDK (all p < 0.05) are significantly higher in the KO cell line than in control" (normoxia
  normoglycaemia), with the Discussion repeating "increased expression of [PDK]--the PDHA inhibitor". There is no human PDK
  transcript-up row (only S022 lower-in-sign in two human neural systems, and S029 up in mouse MEF), and the 'PDK1
  valence uncertain' framing of Q2 omits a third human system with PDK up. The cell line is described by the paper as
  gene-silenced/CRISPR 'downregulation' (it calls it KO); knockout versus knockdown is not stated on S030/S031.
* **M2. Asymmetric confound standard between D1 and Q2/Q4.** D1 is dropped for maturity/composition, but the Q2 organoid
  transcripts rest on the same 4 v 2 organoid contrast and the needs statement itself says the glycolytic shift "is as
  consistent with a less advanced tissue as with a metabolic block" (NEED-PDH-PYRUVATE-AXIS:O3); Q4 organoid rows S067 to
  S069 carry "composition cannot be excluded" (GAD1 ten-fold). The README acknowledges the Q2 maturity rival and keeps
  Q2 because a second human system (hNPC) agrees in sign. State that rule (cross-system sign agreement rescues a
  transcript row; single-system confounded rows are dropped) and apply it to S068, S069, S067, or demote them.
* **M3. S104 (D2 GSK3B pSer9, mouse Wwox-null, three brain regions, P20) meets the README's own usable rule but is
  excluded with a circular reason.** It is a measurement, one level (phospho), tier B, not a response. Its reason class is
  UNUSABLE_DROPPED_QUESTION, i.e. dropped because the question was dropped. 'n = 3, images, one laboratory' is not
  applied to usable S064/S065 (GAD65/67 western, five lanes, one laboratory) or S082 (P47T). Either seed S104 as a usable
  phospho row with the kinase-activity caveat (lithium response stays reserved) or state a numeric threshold used for both.
* **M4. S005 is an inference carried as an observation, and its premise conflicts with S004.** S005 asserts "similarly low
  WWOX immunoblot signal" for WOREE and SCAR12 organoids and concludes that residual function per molecule is the unmeasured
  variable; S004 says "amount relative to wild type not seen in the text passage". Neither is checked against the paper
  (42397075 is abstract-only here, and the abstract says only that patient-derived organoids are milder, with hyperexcitability).
  Both are usable. S005 is a hypothesis; its class should be unusable until the immunoblot is read.
* **M5. Level merging inside single rows.** S067 (level `expression`) carries GAD1 transcript AND "GAD67 surface area per
  nucleus" (protein/immunofluorescence); S066 (level `protein`) carries NPY-positive cell counts AND "human knockout
  organoid NPY transcript also strongly down (log2 -6.24)"; S023 and S028 and S002 mention the other level in the reason
  (S002 and S028 only as cross-reference, acceptable). S067 and S066 break rule (ii) (never converted into another level) in
  spirit: split into one row per level and species. The log2 -6.24 comes from the deposited table cited via
  NEED-INHIBITORY-HYPOFUNCTION:O3; it does not appear in the 34268881 text (no 'NPY' string in the extracted full text).
* **M6. Cell counts typed as protein.** S063 (PVALB), S066 (NPY) and S083 (rat GFAP and Iba1 cells per mm2) are
  stereological or immunostained cell counts (cell number), typed `protein`. The paper's own protein measurement is only
  GAD65/67 by western (S064/S065). Cell number and protein amount are different levels; add a level value (for example
  `cell_count`/`pathology`) or type them `pathology` like S082.
* **M7. Reserved rows that hold a plain state observation, and a state inside a response row.** S075 (reserved,
  RESERVED_ENDPOINT) holds the untreated-knockout seizure and SWD state (spontaneous tonic-clonic seizures from P9; null SWD
  about 0.635 per hour v about 0.03), a plain genotype observation, while the analogous P47T seizure state (S006) is usable; S014,
  S092 and S110 mix an untreated-knockout baseline with the response; S009 buries a plain state (P252A mRNA not
  decreased, faster turnover by cycloheximide chase) inside a reserved intervention-response row, so the state has no seed.
  Split baseline state (usable by presence, or at least unreserved) from treated contrast (reserved).
* **M8. S061 direction 'uncertain' for the excitatory amplitude contradicts the paper's own reading.** 34634460 (full
  text) states mEPSC amplitude "increased", sEPSC "more large-amplitude events ... leftward shift" with means 23.3 v 24.7 pA, no change in
  frequency, and concludes "favors excitation over inhibition, primarily through an impairment in the amplitude of the
  inhibitory currents". The seed reads the means and calls it unchanged-to-slight, which is a defensible magnitude reading, but
  'uncertain' hides that the authors report an increase in amplitude distribution (abstract: "elevated amplitude of
  excitatory post-synaptic currents"). Use `up` with the effect-size caveat, or `unchanged` for means and a separate row for the
  distribution shift. This matters because Q4's conditional pair (inhibitory primary versus excitatory gain primary) is
  decided by exactly this row.
* **M9. S056 misstates the ovarian-cancer paper.** Reason: "authors report no change by WWOX status" for phospho-eIF2A and
  phospho-IRE-1 blots. Full text (28749468): p-eIF2A is induced by paclitaxel and tunicamycin, and no WWOX-status comparison of
  p-eIF2A is stated; for p-IRE-1 "the intensity of the pIRE-1 band induced by thapsigargin was less in WWOX-null Vector-9
  compared with WWOX-overexpressing WWOX-8 cells indicating higher levels of ER stress in the latter"; only PERK activation is
  stated not to change with WWOX status. The row is correctly unusable (non-neural, stressor-induced), but its stated content
  is wrong, and the drug-induced context (paclitaxel/tunicamycin/thapsigargin) is not in the context field. The same
  paper's IRE-1 inhibitor result (KIRA6 and GSK2656157 effects) is an intervention response that, if ever seeded, is reserved.
* **M10. D6 (Redox) 'no neural WWOX-loss redox measurement' is inconsistent with the package's own S033.** S033 (Q2, usable) is
  the authors' "mitochondrial redox activity" (resazurin/PrestoBlue reduction, about 32 percent lower) in WWOX-silenced
  human neural progenitors; 31543760 (full text) also runs an oxidative-stress gene-set PCA (SOD1, SOD2, PRDX2 and others
  differentiate genotypes, sign not stated). Resazurin reduction is a metabolic-activity readout, not ROS or oxidative stress,
  so dropping D6 is defensible, but the drop reason should say "no ROS or oxidative-damage readout in a neural WWOX-loss system" and
  point at S033 instead of denying a redox-named readout exists.
* **M11. Evaluation-guard inconsistency on S027.** S027 is usable=yes, but its reason says "already used as the IT7
  independent contrast, so spent as a held-out" and the guard repeats the IT7 P3 readout warning. A row that is "spent as
  a held-out" should not be in the generation set; either reserve it or delete the phrase. The Q2 six-gene module
  (S017 to S022, S025) is usable under a guard that only a human reader at P3 can honour: if P2 seeds on those genes
  and P3 scores by signature reversal of the same genes the circularity is mechanical. Consider tagging these rows
  `reserved_for_evaluation=partial` or exporting the guard as a machine field that P3 must read.

### LOW

* L1. S001 context "adult-derived"; the needs row says age UNKNOWN and the abstract (29808465) describes two young
  girls. Remove "adult-derived". The comparator for 'down' is three non-fibroblast reference lines with no control
  fibroblast lane (needs limits); put the comparator in the context field.
* L2. S003 (c.517-2A>G, blood cDNA): level `expression`, direction `down` for an exon-skipping RT-PCR product pattern (no
  full-length product). That is a splicing outcome, not a transcript-abundance decrease; no quantification exists. Use direction
  `uncertain` or a `splicing`-type level; the NMD fate of the shorter product is unknown.
* L3. S062 resting membrane potential values (-79.25, -75.51, -73.62 mV) are in Table 1 of 34634460 and not in the
  extracted text; verified in direction only (text: "resting membrane potential was depolarized").
* L4. S071 (D3, SLC12A5) types a NKCC1/KCC2 ratio under the single gene SLC12A5; the entity is a ratio. Harmless because the row is
  unusable, but a ratio is not a gene.
* L5. D3 text "no ... GABA response": sIPSCs (GABAergic currents) are measured in 34634460 (S060), recorded with a high-chloride
  internal solution; what is missing is E_GABA/chloride and exogenous GABA response. Reword so S060 is not contradicted.
* L6. S110 (D5) joins a mouse glucose and weight observation with a human clinical failure-to-thrive observation in one row (two
  species, two systems; README rule says never pool across systems).
* L7. Rat orthology "not checked" (README section 4): the live HGNC record for AIF1 does list a rat ortholog link (RGD:61924);
  GFAP not checked here. The statement can be closed for AIF1.
* L8. S082 and S083 compare cell-count/area assays across species with opposite signs (mouse up, rat down) in two usable rows;
  correctly kept as separate rows with the contrast stated. No change needed beyond L-level typing (M6).
* L9. P47T paper hallmark GSEA reports "hypoxia, apoptosis, and glycolysis pathways enrichment in all three brain regions"
  (36828035); S027 records the six-gene module as INCONCLUSIVE. Both can hold (set-level versus six-gene module), but the paper's
  statement is not recorded as its own row (a mouse glycolysis set-level observation that favours the human direction).

## 3. Verified without discrepancy (at stated depth)

S001/S002 (protein absent, transcript normal: abstract 29808465), S006 (video EEG >6 weeks, n = 3 per genotype: 36828035
methods), S010/S009 caveat (below), S019/S021/S025 (numbers re-read by the checker from tables; sign only here), S032 (abstract
25012504: enhanced glycolysis, diminished respiration, increased HIF1alpha, increased glucose uptake in Wwox-deficient cells),
S033 (resazurin lower, Figure 2, p < 0.05), S058 (36 of 42, 4 of 23, 0 of 11; hippocampal slices indistinguishable), S060
(57.3 v 27.5 pA, sIPSC frequency also reduced), S063 to S065 (PV 44 percent, NPY 30 percent DG only, GAD65/67 western n = 5
per genotype, p < .05), S072/S073 (d-APV eliminates bursts, reversible; BB-FCF minimal effect; CBX 87 percent frequency
decrease without washout), S084 (P47T: both cytokines >= 2-fold, n = 6), S082 (abstract-level only for the Wwox-null; P47T
astrogliosis), S083 (abstract 31340538: reduced astrocyte and microglia populations in lde/lde rat cortex with hypomyelination),
S100/S101 sources (abstract level), S104 (as stated in the needs row, not independently opened).

## 4. The P252A/P282A caveat and the dropped questions

* **P252A versus P282A.** The caveat is justified and correctly placed. In the PMC text of 41124647 the variant names in the
  superscript are stripped, but the structure is unambiguous: "These results suggest that the P252A mutation causes rapid degradation
  of WWOX protein through a lysosome-dependent pathway"; MG-132 did not increase any of the three proteins; chloroquine and
  NH4Cl restored the unstable mutant, 3-MA did not; mRNA of the unstable mutant "was not decreased"; the stable mutant "appeared to
  lose its interaction with POLE4" while the unstable one's POLE4 interaction "was also markedly reduced, likely due to the low
  abundance". So P252A = unstable, P282A = stable, both lose tumour-suppressive activity (as the abstract states), and
  the POLE4 binding loss of the stable mutant is an authors' appearance ("appeared to"), not a quantified result. The proband with
  both homozygous variants "did not suffer from WWOX-related nervous system disease" (Discussion) and the authors speculate
  residual function, which S010's reason carries correctly. One precision for S010: MG-132 did not accumulate even the wild type,
  so the proteasome negative is uninformative (needs limits say so); S009's reason ("MG-132 and 3-MA do not") should carry it.
* **Dropped questions.** D3: sound (no E_GABA, chloride or NKCC1/KCC2 protein in the sources read; see L5 for wording). D4: sound
  (prediction only; no assay). D5: sound as an endpoint-and-confounder (abstract of 25012504 independently reports lethal
  hypoglycaemia in Wwox-deficient mice; S110's mixed-species row is L6). D6: defensible, reason to be reworded (M10). D2:
  GSK3B part is not supported as a drop by the README's own rule (M3); mTOR/autophagy part (transcripts only, mixed signs) is
  sound. D1: Wnt drop sound, MYC/radial glia drop not supported by the stated reason (H3). Verdict: no dropped question is
  unsupported in the sense of having NO data; two (D1 MYC, D2 GSK3B) have usable-by-rule rows that were excluded by question-level
  choice.

## 5. HGNC, orthology and individual-level data

* HGNC re-fetched live (symbols only sent): PVALB HGNC:9704, GAD1 HGNC:4092, GAD2 HGNC:4093, AIF1 HGNC:352, TCF7L2 HGNC:11641,
  PDK1 HGNC:8809, EIF2S1 HGNC:3265, EIF2AK3 HGNC:3255, EIF2AK4 HGNC:19687, CACNA1G HGNC:1394, PANX1 HGNC:8599, BNIP3
  HGNC:1084: all 12 Approved and equal to `hgnc_check.tsv`; MGI and RGD ortholog links present for all 12 (RGD for AIF1,
  PVALB, GAD1, GAD2, TCF7L2, PDK1, EIF2S1, EIF2AK3, EIF2AK4, CACNA1G, PANX1, BNIP3). Orthology is symbol-level link, as the README
  says; no one-to-one claim is made. The collision notes (TCF4 versus TCF7L2; IBA1 = AIF1; GAD65/67 = GAD2/GAD1 on one antibody)
  are correct, and the combined GAD65/67 antibody is disclosed on both rows.
* Individual-level data: none found. No e-mail-like string, no c.1057 allele string, no patient identifier or date; the
  rows describe published cohorts at class level (for example 'WOREE lines (3 individuals)' is a count of cell lines, S004).
  S010 reproduces a published single-case statement (proband homozygous for both thyroid-cancer variants, not a WWOX-DEE
  individual); acceptable as published literature.

## 6. 'Already explored' per question (section 6 of the README and the questions.tsv column)

* The column is headed "not a claim of never attempted" and uses 'carded', 'abstention', 'threads'. Mostly sound. Three
  wording risks (MEDIUM/LOW):
  * Q1 cell: "Only gene addition has a result in a WWOX system; all other cards carry no WWOX-side result of the intervention".
    Scope is 'cards', but reads as a field-level statement, and the package's own reserved rows S009 (chloroquine restores P252A
    protein, a non-neural cell line) and S016 (Wwox CRISPRa in a fly amyloid model) are intervention results on WWOX that are
    not cards. Add "in this repository's cards" and list S009/S016.
  * D3, D4, D6 falsifier text turns a scoped absence into a universal: "No WWOX system has a measurement of E_GABA...";
    "No read-through or NMD measurement on any WWOX allele exists"; "no neural WWOX-loss redox measurement". The needs rows
    themselves say "an absence in what was read, not a result of a bounded search" (NEED-GABA-CHLORIDE-GRADIENT:O1). Use
    "none found in the sources read (date)"; the existing test passes only because it does not look at these files.
  * Q4 cell: "new content lies in interneuron-function and resting-state mechanisms" is a steer about novelty built from the card
    list alone; mark it as 'not carded', not as 'new'.
  Q1 'Why it is in': "only route to restoring the lost function itself" is a strong sentence; a gene addition card exists and
  is described in the same table. Soften to "the route aimed at the lost function itself".

## 7. What was not done

* 42422765 (AAV paper), 36537114 and 32000863 were not opened; rows resting on them (S013 to S015, S092, S075, S080, S081, S110,
  S074, S039) are verified at locator depth only.
* Abstract-only papers: no number from 42397075 or 33914858 (for example 3.3 times fewer myelinated axons, MYC percentages)
  was verified against full text.
* No attempt was made to re-run the centred-ratio computations; the checker already re-reads them from the committed tables.
* This verification does not make any seed usable or unusable; it lists what the package owner should change.
