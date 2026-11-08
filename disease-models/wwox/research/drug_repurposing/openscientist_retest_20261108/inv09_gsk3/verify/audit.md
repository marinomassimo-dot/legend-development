# Blind audit of INV-09 (GSK3), claim actor vf-09, task ORCH-IT38OS-20261108

Date 2026-11-08. Scope: `items.md` D01-D14, coverage of `extraction.tsv`, sample of `reconcile.tsv`, rows of `evidence.tsv`. Before the verdicts of parts A and B were written I had not opened `README.md`, `phase1_note.md` or `chains.tsv` (see the last section for what I looked at afterwards). Labels DATO / INFERENZA / IPOTESI. All 13 PMIDs below were claimed with `paper_packet.py claim --pmid ... --actor vf-09`.

## Depth reached and routes (what I actually read)

| PMID | Route | Depth |
|---|---|---|
| 42274605 (2026 review, Cells) | PubMed full-text tool (PMC13257079; structured text from PMC, not a page summariser) | full text, all 7 sections (reference numbers are stripped in the text, so the primary studies behind each sentence were not visible); no figures or tables |
| 25345501 | NCBI efetch XML of PMC4393753 | full text; Results "Decreased Ino1 leads to inactivation of GSK3alpha", Discussion, figure 4 caption; blots not viewed |
| 27922641 | NCBI efetch XML of PMC5315558 | full text searched for GSK / glycogen / inactivat (one hit, introduction only); not read line by line |
| 18566399 | NCBI efetch XML of PMC2704026 | full text: Methods (animals, EAE), Results (histology, knock-in), Discussion; figures not viewed |
| 32000863 | NCBI efetch XML of PMC6990504, plus the published Fig. 7 PNG from the publisher static-content server (plain curl) | Methods (seizure), Results (GSK3beta section), Discussion, figure 7 viewed as an image; whole paper not read |
| 23099259 | NCBI efetch XML of PMC3610174 | Methods and Results sections on knock-ins and lithium; not whole text |
| 32463939 | NCBI efetch XML of PMC8554790 | Methods (Mg2+, holding potential), Results (knockdown, CT99021, pairs), captions |
| 29515000 | NCBI efetch XML of PMC6553635 | Results on selectivity, BRET, beta-catenin immunofluorescence, TCF/LEF, AML cell lines; not whole text |
| 39901291 | NCBI efetch XML of PMC11792195 | abstract, methods for nuclear beta-catenin, Results section 6, caption of Fig. 6 |
| 23369789, 38123002, 33197065 | PubMed abstract via efetch | abstract only (38123002 and 23369789 have no PMC full text reached) |
| 15791206 | PubMed abstract; PMC record has metadata and keywords only (not open access) | abstract and keywords only; the muscle inhibitor experiment is NOT reachable by me |
| 34747138, 33914858 | PubMed metadata (authors, abstract) | abstract only; the Brain paper (33914858) has no PMC id; cell counts were checked only through the producer's own deepdive manifest `disease-models/wwox/research/deepdive_manifests/PMID33914858.json` (a derived artefact, not the primary) |

No source was read through WebFetch or a page summariser. Europe PMC full-text REST returned HTTP 500 and one PMC image URL returned 404/403; I did not retry or use other clients beyond those three plain `curl` calls.

## A. Verdicts on the decisive propositions

| ID | Verdict | Confidence | Reason, in one line |
|---|---|---|---|
| D01 | SUPPORTED | high (figure viewed) | Fig. 7d: lithium lowers the PTZ score in +/+, +/- and -/- (all marked ****); fixed PTZ dose 30 mg/kg; one blot lane per genotype and region; the report states both attribution versions (L10/L17-20 versus L152). |
| D02 | SUPPORTED, with a sharpening | high for 25345501, high for 27922641 | 25345501 shows alpha only; 27922641 does not support the convergence statement. |
| D03 | SUPPORTED (sub-claim on 15791206 muscle inhibitor UNVERIFIABLE by me) | medium | Knock-in is a loss of Ser inhibitory control; 23099259 gives no inhibitor to a knock-in; I add a mechanism-level reason. |
| D04 | SUPPORTED, but the item must add one qualifier | high | In HEK293T selective compounds did not raise beta-catenin; the beta-selective compound did in HL-60 and TF-1 at 20 micromolar. |
| D05 | SUPPORTED | medium-high | 38123002 is a muscarinic-antagonist paper; 42274605 says both things (see the reconciliation block). |
| D06 | SUPPORTED, with three additions | high | Knock-in is a double alpha plus beta S21A/S9A line, n = 6 per group, clinical score only. |
| D07 | SUPPORTED as an absence statement; the report's window claim is NOT SUPPORTED and the cited model contradicts it | medium | Wwox-null mice in 32000863 survive under one month. |
| D08 | PARTLY | medium | First half holds at abstract level; the second half is resolvable by the cited paper 32000863. |
| D09 | SUPPORTED | high | Design statement; check against report lines L55, L61, L143-145. |
| D10 | SUPPORTED, with two additions | medium-high | The report's beta-catenin quote for 39901291 is a methods sentence about one peptide at one dose. |
| D11 | SUPPORTED | high | Matches the full text. |
| D12 | SUPPORTED (as IPOTESI) | high | The abstract of 23369789 says nothing about a threshold in beta-catenin. |
| D13 | SUPPORTED | high | Same first and last author in 33914858 and 34747138. 32000863 is another group. |
| D14 | SUPPORTED | high | One lithium PTZ score plus one blot; nothing else in a WWOX system. |

Counts: SUPPORTED 11 (of which 5 with additions), PARTLY 1 (D08), SUPPORTED-as-absence-plus-contradiction 1 (D07), UNVERIFIABLE 0 at proposition level (one sub-claim inside D03). NOT SUPPORTED 0 at proposition level.

### D01 (WWOX datum, 32000863)
- DATO: Fig. 7d (viewed as an image): PTZ + LiCl against PTZ alone in the three genotypes. The PTZ-alone curve peaks near stage 1 in +/+, near 1 in +/-, near 3.5 in -/-; lithium lowers all three (significance mark on all three panels). So lithium is not WWOX-specific in this panel. Dose: PTZ 30 mg/kg, LiCl 60 mg/kg given three times within 1 h (Methods). No lithium-only arm, no ethosuximide-versus-lithium test of threshold; the readout is a score over 60 min after one dose, not a threshold.
- DATO: Fig. 7c, Ser9 blot with one lane per genotype and brain region (the caption says the blot is representative of four experiments): pSer9 densitometry numbers 2.7/3.1/1.3, 3.6/3.5/2.0, 3.9/3.8/2.5 (+/+, +/-, -/-), total GSK3beta flat. Postnatal day 20 per the caption (the Methods text says day 14 for the western tissue: an inconsistency inside the paper).
- DATO: the abstract wording "significantly abolishes the onset of PTZ-induced seizure" is stronger than the figure (the null curve with lithium still reaches about stage 1 early).
- INFERENZA: the item's reading (not WWOX-specific, not attributable to a kinase) is right. The report quotes the abstract sentence (L18) and omits the genotype controls.
- The report does state both versions: Summary and F001 title "cannot be attributed to GSK-3beta alone" against Conclusion L152 "only ... is firmly attributable". The item is faithful.

### D02 (inositol arm, 25345501 and 27922641)
- DATO, 25345501 (full text): INO1 knockdown in SK-N-SH cells raised inhibitory Ser21 phosphorylation of GSK-3alpha (2.4-fold with an 82 percent knockdown) and "GSK3beta was not significantly altered". Valproate (a transient inositol drop) did the same for alpha and "GSK-3beta phosphorylation was not affected". The authors write that alpha phosphorylation kept rising after inositol levels were restored, "suggesting that inhibition of inositol synthesis, but not inositol depletion, is responsible". They call it "the first demonstration in SK-N-SH cells" and say the alpha/beta difference needs further study.
- DATO, 27922641 (full text searched): GSK-3 appears once, in the introduction, as another hypothesis "neither of which has been either confirmed or rejected beyond doubt". The paper has no GSK-3 phospho-readout. Its findings: IMPA1 or SMIT1 knockouts mimic several lithium effects; IP3 given intracerebroventricularly acts lithium-like on forced-swim, amphetamine hyperlocomotion and autophagy markers.
- INFERENZA: the report's F001 statement ("inhibition of inositol synthesis itself inactivates GSK-3", citing both) is carried by one paper, in one human neuroblastoma line, for the alpha isoform, and says nothing about GSK-3beta (the isoform the report is attributing to). So the "convergence" does not support the beta attribution argument as the report phrases it. The item's "alpha (not beta)" is exact.
- INFERENZA: for arm 6 ("inositol-depletion mimic with no GSK-3 action") the item is right that "no GSK-3 action" is not guaranteed for an INO1-type block; the same paper adds that depletion itself did not account for the alpha effect, so a depletion-only tool and a synthesis-block tool may differ. Neither paper tests a brain preparation or a seizure endpoint.

### D03 (S9A knock-in and drug attribution)
- DATO, 23099259: the knock-ins are alpha 21A/21A and beta 9A/9A, serine to alanine, "disable the inhibitory serine phosphorylation". Lithium was given to wild-type mice; the knock-in mice received methylphenidate or amphetamine only (Methods and Results), so no inhibitor is given to a knock-in. The beta 9A mice had a changed baseline (impaired PPI and prolonged hyperactivity after methylphenidate). The report's quote "expression of constitutively active GSK3beta, but not GSK3alpha" is verbatim from the abstract and concerns methylphenidate responses, not drug attribution.
- INFERENZA (mechanism, not in the item): 25345501 introduction (secondary statements) says lithium is a competitive inhibitor of GSK-3 and also raises inhibitory phosphorylation; S9A removes only the second route, so a lithium effect surviving S9A would not prove a kinase-independent action, and an effect abolished by S9A would not isolate beta from the direct-site action. The item's argument stands and can be strengthened by this.
- UNVERIFIABLE by me: "the ATP-site inhibitor still acted in S21A/S9A muscle" (15791206). The abstract and keywords (it lists AR-A014418) are consistent with it, but the PMC record is not open access and I did not reach the Results. The producer's own `gsk3_inv09_20261107/output/evidence.tsv` E05 carries it from a full read; I could not re-test it.
- 15791206 abstract (DATO): in double knock-in cells Wnt3a "induces normal inactivation of GSK3", so the Wnt route does not need Ser21/Ser9 phosphorylation. This supports the item's point that S9A does not test the Wnt branch.

### D04 (isoform selectivity and beta-catenin)
- DATO, 29515000 abstract: "Knockdown of GSK3alpha or GSK3beta individually does not increase beta-catenin". Full text: in HEK293T, 20 micromolar, 24 h, neither BRD0705 (alpha) nor BRD3731 (beta) produced total or nuclear beta-catenin, while BRD0320 and CHIR99021 did; TCF/LEF reporter the same.
- DATO, the qualifier the item should state: in HL-60 BRD3731 raised beta-catenin "starting at 20 micromolar", in TF-1 TCF/LEF induction occurred at 20 micromolar of BRD3731 (60 micromolar of BRD0705), and in the U937 expression profile BRD3731 showed "a trend toward induction of beta-catenin transcriptional programs". Cell selectivity was only 4-6-fold (Kd 3.3 micromolar for BRD3731 on GSK3beta). So a beta-selective compound does raise beta-catenin once the concentration leaves the narrow window; the data refute "harm cannot be escaped" for the alpha-selective compound and for genetic single-isoform loss, not cleanly for a beta-selective chemical. This is what "concentration and cell-line dependence" should be made to say.
- INFERENZA: the report's logic (beta-catenin is downstream of GSK-3beta activity "regardless of which inhibitor") skips redundancy: genetic loss of one isoform does not raise beta-catenin (abstract, and a cited earlier ES-cell result). Neural cells untested, as the item says.
- 33197065 (abstract only, DATO): "GSK3alpha, but not GSK3beta, is required for LTD" and the abstract says the data "rule out a major role for GSK3beta in this process". The report's F004 attributes LTD substrates (KLC-2, PSD-95, tau) to GSK-3beta through 32463939's introduction while citing 33197065 for isoform specificity; the two sentences point at different isoforms (extraction E26 records this correctly).

### D05 (myelin transfer; the 2026 review, 38123002)
- DATO, 38123002 (abstract only): solifenacin, a selective M3 antagonist, in cuprizone mice; "Sol treatment inhibited the Wnt/beta-catenin signaling pathway and reversed the effects of CPZ on OPCs differentiation". The authors conclude Sol may promote differentiation by inhibiting Wnt/beta-catenin; the abstract contains no GSK-3 manipulation. Report L117 ("Inhibiting Wnt/beta-catenin reversed...") presents a downstream effect of a drug as the manipulation. The item is faithful.
- DATO, 42274605, where each statement sits (full text read; this answers the reconciliation question about the two packages):
  - Abstract: "inhibition of GSK-3beta affects beta-catenin stability and is associated with oligodendrocyte differentiation" (favourable direction for GSK-3beta inhibition, as an association); also that observations in demyelination models "have not been established as direct evidence of remyelination in patients" and that agents "act on multiple cell populations".
  - Section 1: Wnt/beta-catenin "inhibit[s] differentiation"; small molecules targeting kinase activity increase oligodendrocyte and neuronal differentiation; GSK-3beta inhibitors "are used clinically for other indications".
  - Section 3, first paragraph (this is the unfavourable-direction statement for Wnt up, and it supports the report's premise F002 at the Wnt level): Wnt activity "maintains progenitor-associated transcription and reduces differentiation"; "continuous Wnt signaling reduces differentiation of oligodendrocyte progenitor cells ... in demyelinated areas"; Wnt signalling acts differently "according to the phase of remyelination".
  - Section 3, same paragraph, last sentence (this is the favourable lithium sentence the inv06 package quotes as EV16): "pharmacological inhibition of GSK-3beta by lithium reduces beta-catenin phosphorylation and promotes oligodendrocyte differentiation". Confirmed verbatim.
  - Section 3, later: Akt-mediated inhibition of GSK-3beta "promotes beta-catenin-dependent transcription associated with oligodendrocyte differentiation"; GSK-3beta inhibition "is associated with increased mTORC1 signaling"; GSK-3beta inhibition acts "through beta-catenin-dependent and beta-catenin-independent mechanisms, with effects that depend on the differentiation status".
  - Section 4: "GSK-3beta inhibition increases beta-catenin levels and neuronal differentiation in neural stem and progenitor cells" (the opposite direction to the report's F005, which says lowered GSK-3beta activity sustains proliferation at the expense of differentiation, citing a DISC1 paper I did not read).
  - Sections 6 and 7: clinical lithium and mTOR-inhibitor studies "primarily affect immune responses"; no direct evidence of remyelination in patients.
  - Reconciliation: both packages are right about where they read. inv09 EV03 (abstract) and inv06 EV16 (section 3) quote two places that say the same thing (GSK-3beta inhibition associated with or promoting oligodendrocyte differentiation). Neither package, as far as I can see from the rows, records that the same review also states, in the same section 3, that continuous Wnt signalling reduces differentiation. The review holds both statements side by side and does not reconcile them (a review sentence, not a primary result; the numbered references behind the sentences were not visible to me). So the report's use of 42274605 as "Supports F002" (harm) is not supported by any sentence of the review about GSK-3beta inhibition; its Wnt-negative premise is supported; the step from one to the other is the report's own, and the review's own GSK-3beta sentences go the other way. inv09 EV03 should say "review states both; GSK-3beta-inhibition sentences favourable; Wnt-activation sentences unfavourable" and its depth should be recorded as full text read by vf-09, not abstract only.
- INFERENZA: the item's conclusion (no WWOX or GSK-3 test of myelin; transfer) holds.

### D06 (EAE, 18566399)
- DATO, what the knock-in did (Methods, Results): "serine-to-alanine mutations in the regulatory serines of both GSK3 isoforms, S21A-GSK3alpha and S9A-GSK3beta", homozygous knock-in replacing both genes, so GSK3alpha/beta "retain maximal activities". MOG35-55 immunisation, n = 6 per group; cumulative disease index 54.5 +/- 4.6 (wild type) against 80.3 +/- 28.9 (knock-in), p < 0.05; incidence 6/6 against 5/6; the acute phase was accelerated. The authors call it "moderately but significantly" promoted. Readout was the clinical score; demyelination histology (Luxol fast blue; at least three animals per group) was shown for lithium, not for the knock-in.
- DATO: lithium pretreatment and post-onset treatment reduced demyelination, microglial activation and leukocyte infiltration in the spinal cord; lithium suppressed MOG-reactive effector T-cell differentiation and IL-6/IL-17.
- DATO, a point against the report's "immune-mediated" framing as settled: the Discussion says lithium could inhibit demyelination, promote remyelination "or a combination", that promotion of remyelination is "a speculative observation and needs to be examined further", and that suppression of microglial activation could contribute. So the paper does not exclude a direct CNS effect; it favours an early immunological effect.
- INFERENZA: the knock-in is a double-isoform allele active in every cell type, so it neither separates alpha from beta nor immune from glial effects. The report's L68 cites only lithium; the knock-in is not in the report. The item states what the source says.
- The model is adult-onset autoimmune demyelination, not developmental myelination (as the item says).

### D07 (windows)
- DATO: the cited 32000863 gives no timing for "perinatal myelination and migration windows" beyond: Wwox-/- mice "survived for less than a month", seizure testing in preweaning mice (abstract), blots and histology at P14-P20, and "spontaneous epileptic seizures" in the null mice. The windows claim therefore has no source in the cited papers within my perimeter (this paper only; 33914858 not read by me, 32581702 and 31340538 not opened).
- INFERENZA: in the cited constitutive null the seizures, the migration and maturation findings (DCX, NeuN at P14-P20) and the death all fall within the same short postnatal period, so "treating after the windows have closed" has little room in that model; the "chronic phenotype" is not shown for the null. The report's use of the neuronal-deletion model changes this but I did not read its ages. So the item's NON RISOLTO is right, and the cited evidence leans against the claim as stated.

### D08 (maturation)
- DATO, 33914858 (abstract): "reduced maturation of oligodendrocytes, reduced myelinated axons and impaired axonal conductivity" in the neuronal-deletion mice. The CC1 and PDGFR-alpha counts at P17 are in the producer's own manifest (it quotes "significantly more OPCs" and CC1 about 155 against 72, nine points per group from three mice); I did not read the paper's figure or text. The non-cell-autonomous claim rests on one validation image per the manifest: UNVERIFIABLE by me.
- DATO that resolves half of the NON RISOLTO: the cited 32000863 reports, in the Wwox-null, persistently high doublecortin at postnatal day 14 and many dentate gyrus neurons lacking NeuN at day 20 (Fig. 6, text), with "abnormal neuronal differentiation and migration" in the abstract. So "neuronal maturation already deficient in WWOX" has a source in a paper the report cites (it is not cited for that line, which cites 38123002 and 19303846). Items D08 should record this; it moves the proposition to a WWOX datum for neuronal differentiation markers in the constitutive null at P14-P20, with the usual limits (blots, markers, not a maturation timeline).

### D09 (proof words)
- Checked against the report: L61 "demonstrates dissociability", L143 "Dissociability is proven if ...", L144 "On-target attribution is proven if the ... knock-in abolishes the anti-seizure rescue", L55 "the effect is proven to be on-target". The item cites L61 and L143; add L55 and L144. INFERENZA: a rescue that is merely absent in a double-active background can be saturation or baseline shift (see D03); "stays at baseline" needs equivalence margins, power and a reference arm. Agreed.

### D10 (compounds)
- DATO, 29515000: CHIR99021 is described as "a commercially available pan-GSK3 inhibitor"; BRD3731 has 14-fold selectivity on enzyme, 4-6-fold in live cells (Kd 3.3 micromolar), the item is right that the window shrank. 32463939 calls CT99021 "its most selective inhibitor" (the report's "selective GSK-3beta inhibitor" repeats that wording) but uses no second inhibitor or isoform tool.
- DATO, 39901291: it is a human dental pulp stem-cell study of the peptides pS9, LRP 6a, L803 and L803-mts; only L803-mts was tested for nuclear beta-catenin (100 micromolar, 24 h). The report's quote "accumulation of beta-catenin in the nucleus of GSK3-betai-treated" is the Methods description of the assay, not a result sentence; the result is for L803-mts. So the report's "even a substrate-competitive GSK-3beta peptide inhibitor produces ..." (F002 and the Evidence Base L116) is correct for one peptide, one dose, one non-neural cell type. Add this to D10 and to extraction E10.
- INFERENZA (internal tension, additional): L803-mts is the report's arm 3, the "tunable partial inhibition" arm, while in the same cited paper it raised nuclear beta-catenin. The report uses the same class as proof that Wnt activation is intrinsic and as a candidate beta-catenin-sparing arm.
- DATO, 23369789 (abstract): "Substrate competitive inhibitors can fulfill the requirement for selectivity and allow fine tuning of the degree of inhibition"; and "a moderate inhibition of a cellular target, particularly for long-term treatment, provides more favorable outcome than complete inhibition". Both are verbatim and general statements. L803-mts is not named in the abstract; the abstract says the authors report "our progress in the development of substrate competitive inhibitors". So the attribution of L803-mts to this PMID is plausible but not shown at abstract level. The item is right to say "review, not read".

### D11 (PI4KIIalpha branch)
- DATO (full text): rat organotypic hippocampal slices, CA1 pairs of transfected and non-transfected neurons; PI4KIIalpha knockdown left AMPA EPSC unchanged and lowered isolated NMDAR EPSC (NBQX, holding -40 mV) by 50 +/- 4 percent (41 against 88 pA, n = 30 pairs). CT99021 (1 micromolar) reduced the isolated NMDAR EPSC to 57 +/- 4 percent of baseline (n = 17); after knockdown the effect was absent (94 +/- 4 percent, n = 11); rescue with wild type but not with the S9/51A mutant. PI4KIIalpha was not required for NMDAR-dependent LTD (caption). Bath includes 4 mM MgSO4 (Methods). No isoform tool, no beta-catenin readout, no WWOX preparation.
- INFERENZA: agreed with the item. The report's "beta-catenin-independent" label is a construction (nothing measured beta-catenin). Also, the branch's effect is a reduction of synaptic NMDAR current by about half when knocked down, which is a cost to excitatory transmission, not a free "useful" arm.

### D12 (threshold)
- Agreed. 23369789's abstract does not contain a beta-catenin threshold or any statement about useful versus harmful branches. The report concedes the differential sensitivity "has not been measured" (L133). IPOTESI label correct.

### D13 (independence)
- DATO (PubMed metadata): 33914858 and 34747138 share first author Repudi and last author Aqeilan (Hebrew University). The 34747138 abstract refers back to "we recently demonstrated that neuronal ablation of murine Wwox ..." so the two are one group's sequence. 32000863 (Cheng ... Hsu) is from National Cheng Kung University in Taiwan, with no author overlap with the other two. Agreed: not independent confirmation, and not a GSK-3 datum.

### D14 (WWOX-side evidence)
- DATO: in the report the WWOX-side GSK-3 evidence is the one lithium PTZ result with the Ser9 blot; the KB sentence about hypersynchrony is marked "unmapped intermediates" (L129, L66). I found no second GSK-3 route in a WWOX system in the report. The paper itself cites a WWOX-GSK3beta interaction in SH-SY5Y cells (ref. 65 of 32000863), which the report does not use.

## B. Coverage audit

Report read in full (152 lines). Twelve points chosen across the whole text; extraction rows searched by content, not only by anchor.

| # | Report anchor and content | Extraction row | Result |
|---|---|---|---|
| 1 | L2-3 interface fragments "View full report" | E82 | PRESENT |
| 2 | L22 F002 heading hedge "partly intrinsic" against Summary "largely on-target" and F002 body "intrinsic property" | E08, E09, E16 (no row carries "partly") | PRESENT_NARROWED (the hedge gradient is lost; only the strong wording is recorded) |
| 3 | L28 quote "moderate inhibition ... more favorable outcome than complete inhibition" | E21 | PRESENT |
| 4 | L35 KB measured excitability defect (elevated EPSC amplitude layer II/III, reduced inhibition, intrinsic hyperexcitability) | E27 | PRESENT |
| 5 | L51 L803-mts peptide as arm 3 | E35 | PRESENT (but see the note error below) |
| 6 | L68 EAE counter-evidence and the "one must not generalize" caveat | E47 | PRESENT |
| 7 | L78 "conventional ASMs fail ~95%" | E51 | PRESENT |
| 8 | L103 "unacceptable as a mechanism-pure or chronically-safe therapeutic" | E53 | PRESENT |
| 9 | L137 isoform tools "partial agonists" not clinically available | E57 | PRESENT |
| 10 | L141 "crossed where relevant onto the S9A background" | E39, E43 | PRESENT_NARROWED (E39 states the cross onto Wwox-null as a general design element; "where relevant" is a hedge that is dropped) |
| 11 | L147 secondary experiment, CT99021 in Wwox-null layer II/III neurons with PI4KIIalpha knockdown occlusion | E59 | PRESENT |
| 12 | L150 med-chem pursuit of substrate-competitive/isoform-selective tools | E62 | PRESENT |

Result: 10 of 12 PRESENT, 2 PRESENT_NARROWED, 0 MISSING. Because two rows were narrowed rather than missing, I scanned the remaining text for the same kind of content (graded hedges and conditional design words). Further narrowed points found: none beyond these two. Other hedges I checked are present: "plausibly" (E20), "mitigated, not eliminated" (E19), "likely more sensitive" (E54), "partly isoform-separable" (E55), "direction well-supported" (E58), "somewhat uncomfortable" (E08 note).

Errors in the extraction found while reading:
- `extraction.tsv` E35 note says "Arm 3 is not separately named in the later six-arm list at L141". It is: L141 reads "...full selective GSK-3beta; substrate-competitive partial; low-dose partial; time-gated post-window; inositol-depletion mimic". Correct the note and add L141 to the anchor of E35.
- E10 treats the report's nuclear beta-catenin quote as a finding about "GSK3-betai-treated cells" generally; see D10 (one peptide, L803-mts).
- E26 and E65 are fine; E39 correctly flags that a "constitutively active" allele abolishing rescue is asserted, not argued.

## C. Reconciliation sample (8 rows of `reconcile.tsv`)

The file has only 2 rows whose `legend_class` is `new_to_legend` (E50, E62) and 1 more row (E05,E38,E74) whose `legend_novelty` column says new_to_legend while its `legend_class` is `verified_or_corrected`. I used these three as the new_to_legend sample and say so. Pointers were opened in the worktree.

| Row | Class sampled | Pointer check | Result |
|---|---|---|---|
| E50 (hierarchy) | new_to_legend | no pointer; `prior_brief_fate` = "omitted (BRIEF forbids presupposing a ranking; lists no hierarchy)" | The prior `gsk3_inv09_20261107/BRIEF.md` has no ranking or hierarchy and does not say "forbids presupposing a ranking"; it says "do not assume correct its separation..." and "Separability, without presupposing it". Fate "omitted" is right; the parenthesis should read "omitted (BRIEF names no hierarchy; section 3 asks that separability not be presupposed)". |
| E62 (med-chem) | new_to_legend | `prior_brief_fate` "omitted (BRIEF: do not increase the number of compounds)" | Verbatim in the prior BRIEF ("Do not increase the number of compounds to show progress"). OK. |
| E05,E38,E74 | new_to_legend by novelty column | pointer to this package's EV01 and EV02; prior fate "omitted (BRIEF names no inositol-depletion arm)" | The prior BRIEF has no word "inositol" (searched). Row text on 25345501 and 27922641 agrees with my reading. One omission: the row does not say that GSK-3beta was unchanged, nor that depletion itself was not the driver (see D02). |
| E01,E44 | already_present_and_used | `gsk3_inv09_20261107/output/evidence.tsv` R02; `investigations_it20.tsv` INV-09; receipts for 32000863 | R02 exists and says lithium lowered the score in wild type and heterozygote as in the null; INV-09 row exists in `ranking_it8_p9_20261029/investigations_it20.tsv`; the ledger carries 7 lines naming 32000863. `prior_brief_fate` "kept (BRIEF premise C)" matches the prior BRIEF section 2C. OK. |
| E14 | already_present_and_used | `deepdive_manifests/PMID33914858.json`; prior BRIEF D | Manifest exists and holds the CC1 and PDGFR-alpha counts; fate "narrowed (BRIEF D: do not describe WWOX hypomyelination automatically as an intrinsic oligodendrocyte defect)" matches the prior BRIEF text. OK. |
| E19,E22,E36,E37 | present_not_used | prior `experiment.tsv` X5 | X5 exists ("prolonged exposure ... separate from the acute result"); the prior BRIEF sections 5 supports "do not assume a post-development phase without risk". OK. |
| E40,E41 | present_not_used | prior `experiment.tsv` X1-X2; BRIEF section 5 | X1 and X2 exist and carry the paired endpoints; fate "modified" with the BRIEF pairing sentence verified. OK. |
| E13 | superseded_or_contradicted | this package's EV03 | EV03 quote is verbatim. Classification is defensible for the direction of the abstract sentence. See the reconciliation block under D05: the review also states the Wnt-negative premise, so "superseded or contradicted" is too strong for E11 and fair for E13 only if the row says the review states both. |

`prior_brief_fate` verified against the previous package BRIEF for four rows (E50, E62, E05, E19 group): three exact, one (E50) with imprecise wording. Row E32 (superseded: the report says Nex/Nestin-Cre, the paper's neuronal arm is Syn1-Cre) was not in my eight; I agree with it only through the prior package's R03 pointer, which exists and says Syn1-Cre. I could not check the original Brain text myself.

## D. Evidence sample (`evidence.tsv`, 5 rows)

| Row | Quote verbatim in source? | Where | Carries the proposition? |
|---|---|---|---|
| EV01 | yes ("led to the inactivation of GSK-3alpha by increasing the inhibitory phosphorylation of this kinase") | abstract of 25345501 | yes for D02 (alpha only). Depth could be raised to full text (Results, Fig. 4 caption): GSK-3beta unchanged. |
| EV02 | yes ("IMPA1 or SMIT1, both mimic several lithium's behavioral and biochemical effects") | abstract of 27922641 | context only; as a "no GSK3 action stated" support it is right and can be upgraded: full text mentions GSK-3 once. |
| EV03 | yes | abstract of 42274605 | carries D05 as a counter on direction, but the row's note ("Direction opposite to the report's use. A review abstract; primary studies behind it not read") omits that section 3 of the same review states Wnt activation reduces differentiation, and the depth label "abstract_only" understates the reading available. |
| EV04 | yes | abstract of 38123002 | yes (drug effect, not a Wnt manipulation). |
| EV05 | yes ("in knock-in mice expressing constitutively active GSK3, EAE developed more rapidly and was more severe") | abstract of 18566399 | yes; the note should add: double alpha/beta S21A/S9A knock-in, n = 6 per group, clinical index only. |

Gap: no evidence row backs D01, D03, D04, D07, D08, D10, D11, D13 or D14. Those propositions rest on reuse "by identifier" of the previous package. For each I checked the source myself (see section A). Rows worth adding: 32000863 Fig. 7d and 7c (D01, D14), 29515000 HL-60/TF-1 BRD3731 at 20 micromolar (D04), 32463939 CT99021 occlusion with the numbers (D11), 39901291 L803-mts nuclear beta-catenin (D10), 18566399 knock-in methods (D06), 33914858 and 34747138 authorship (D13).

## Corrections the producer must make

1. `verify/items.md` D04 statement: add "in HL-60 and TF-1 the beta-selective compound raised beta-catenin from 20 micromolar; the dissociation is shown for the alpha-selective compound and for genetic single-isoform loss, and for both selective compounds only in HEK293T at one concentration".
2. `items.md` D08: split the NON RISOLTO; the neuronal maturation half has a source in the cited 32000863 (DCX at P14, NeuN loss in the dentate gyrus at P20; abstract "abnormal neuronal differentiation and migration"), while the report does not cite it for that line.
3. `items.md` D07 or D14: record that in 32000863 the Wwox-null mice survive under a month and the seizure tests are preweaning, so the "after the windows" claim has no support in the cited model.
4. `items.md` D06: add "double S21A/S9A allele, n = 6 per group, clinical score only; authors call lithium-promoted remyelination speculative".
5. `items.md` D09 anchors: add L55 and L144 to L61 and L143.
6. `evidence.tsv` EV03: change depth to "full text read (vf-09 audit)" or keep the producer's depth and add a row EV06 with the section 3 sentences listed in D05; correct the note so that it states both directions; do the same on `reconcile.tsv` rows E11 and E13 (E11 should record that the review also supports the report's Wnt-negative premise).
7. `evidence.tsv` EV05 note: add the double-isoform and sample-size facts.
8. `extraction.tsv` E35: fix the note (arm 3 is named at L141) and add the anchor; E10: add "one peptide (L803-mts), 100 micromolar, human dental pulp stem cells; the quoted words are a Methods description". Also record the arm-3 tension (D10).
9. `reconcile.tsv` row E50: reword the `prior_brief_fate` parenthesis as given in part C.
10. `reconcile.tsv` row E05,E38,E74: add that GSK-3beta was not significantly altered and that the authors attribute the alpha effect to the synthesis block, not to depletion.
11. `extraction.tsv`: add the L22 heading hedge ("partly intrinsic") to E08 or a new row, and "where relevant" to E39 (part B).
12. Add evidence rows for the propositions listed under part D.

## Open uncertainties

- The 2026 review's primary support for the lithium sentence in section 3 and for the Wnt-negative sentence is not visible to me (references stripped); the reconciliation between the two packages is therefore at the level of what the review states, not of what the primary papers show. A reading of its reference list would settle whether the favourable sentence rests on primary data or on other reviews.
- 15791206 muscle inhibitor experiment: abstract and keywords only.
- 33914858 (Brain): primary text not reached; counts only via the producer's manifest, validation image not seen.
- 19303846 (DISC1), 17850214 and the kinome panel claims: not read by me.
- 25345501 blots and 32000863 other panels (e.g. whether the lithium-only wild type was tested without PTZ) were not examined beyond Fig. 7.
- The inconsistency inside 32000863 (western tissue at day 14 in Methods, day 20 in the caption) is noted but not resolved.

## After the verdicts: what I read afterwards

I opened `README.md`, `phase1_note.md`, `chains.tsv`, `decisive.tsv` and `receipts/INDEX.tsv` only after sections A and B above were written, and changed no verdict because of them. What they add:

- The producer's depth is honest: all five new sources are recorded as `abstract_only` (cap of 5 respected), and the README states that 38123002 and 42274605 were abstract-level. My readings of 25345501, 27922641, 18566399 and 42274605 went to full text, so the corrections above are additions to, not contradictions of, the producer's declared depth.
- README answer 2 says 42274605 gives "the opposite direction". At abstract level that is accurate; at full-text level the review also contains the Wnt-negative premise (section 3). README answer 2, `reconcile.tsv` E11/E13 and `evidence.tsv` EV03 should carry that nuance (correction 6).
- README answer 3 and chain C07 agree with my reading of 25345501 (alpha) and 27922641 (no GSK-3 readout); they should add "GSK-3beta not significantly altered" and "inositol synthesis, not depletion, drives the alpha effect".
- `phase1_note.md` notes the six-arm confusion at L141; the extraction note E35 has the same confusion and is wrong (L141 lists "substrate-competitive partial"). The report has 152 lines; the note says 151 (cosmetic).
- Chain C02 and README (d) carry the dental pulp stem-cell identity for 39901291 but not that the beta-catenin result is for one peptide (L803-mts) that the report also uses as its partial-inhibition arm; add (correction 8).
- Chain C09 already notes that the EAE finding may mean context dependence rather than harm; consistent with my D06.
- No claim in README, chains or decisive.tsv contradicts my verdicts on D01-D14.
