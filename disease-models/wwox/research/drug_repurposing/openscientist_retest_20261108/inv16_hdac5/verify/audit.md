# Blind audit — INV-16 (HDAC5), verifier vf-16, task ORCH-IT38OS-20261108

Non-canonical working record, not medical advice. Public edition, WWOX-DEE reference genotype class. Written 2026-11-08. Quotes are 25 words or fewer. Labels DATO / INFERENZA / IPOTESI.

**How I worked.** I read `verify/items.md`, `extraction.tsv`, `reconcile.tsv`, `evidence.tsv` and the complete original report (`/home/desktop/legend-development/files/openscientist_retest_20261108/original_reports/INV-16_HDAC5.txt`, 155 lines). I wrote the part A and part B verdicts below before opening `README.md`, `phase1_note.md` or `chains.tsv`. Every PMID in the items was claimed for `vf-16` (the claim tool also showed other claimants on some PMIDs; nothing was recorded). Routes used, all with plain default clients: the PubMed connector (abstracts and metadata; this is the record itself, not a page summariser), NCBI E-utilities efetch (PMC full-text XML for 40478640, 39923817, 32000863, 26061431; PubMed abstract text for 32236769, 33164260, 12641737, 18308563, 40667573, 36124413, 35704695), `pubmed_identity_check.py` (identity MATCH for 40667573, 28106060, 12641737, 18308563, 33164260, 37843550). Not reachable by me: full text of 22991226 (no PMC record; I did not retry the publisher route that returned HTTP 403 earlier), full text of 17956988 (PMC XML withheld by the publisher; the PMC HTML page returned no article body to a plain request; not retried), full text of 15194749, 23916482, 41830506 (not opened; abstract only), and any figure image. No source was read through a page summariser.

**Producer disclosure weighed.** The producer says it viewed about 12 abstracts beyond its 5 receipts and ran claims late. Consequence for this audit: the five receipts (40478640, 11804585, 23916482, 41830506, 32236769) are the only recorded readings; statements about 15194749, 12641737, 40754252, 28106060, 39049738, 40667573, 22991226, 26061431 rest on abstracts or earlier receipts. I re-read each of those abstracts myself, so the depth words in the items hold at "abstract" level, and where an item says "not read" it is accurate. The producer's items never claim more than abstract depth for these; the late claims are a process fault, not a content fault.

---

## A. Decisive propositions

### P01 — HDAC5 to SLC2A1 through MEF2 is a transfer from HDAC4/mouse heart; human muscle HDAC5 knockdown gave LOWER GLUT1 — SUPPORTED (abstract level; absence clause perimeter not re-run)

The record the producer calls "in the module": `disease-models/wwox/research/drug_repurposing/batch_it28_p3_hdac5_20261105/A_edge_origin/receipts/FTR-20261105-22991226-04.json` (abstract-only receipt, full text recorded as unobtained), restated in `.../hdac5_inv16_20261107/output/evidence.tsv` row H07 and `.../nb3b_action_it32_20261107/output/README.md` item 1.

Primary source (I read the PubMed record): Raichur et al. 2012, J Mol Endocrinol 49(3):203-211, PMID 22991226. DATO, abstract: "Knockdown of HDAC5 in human primary muscle cells increased glucose uptake and was associated with increased GLUT4 (SLC2A4) expression and promoter activity but was associated with reduced GLUT1 (SLC2A1) expression."
- Species: human. Cell type: primary muscle cells (knockdown also after differentiation onset, per the abstract).
- Perturbation: knockdown (the authors call it "inhibition of HDAC5"; the abstract does not support catalytic inhibition).
- Readout of the GLUT1 change: "expression". The abstract does not say transcript or protein (its MeSH list names RT-PCR and Western blotting as methods but does not link them to GLUT1). It is not an uptake measure: uptake rose while GLUT1 fell. The GLUT4 arm carries a promoter-activity result; the GLUT1 arm carries none.
- So the report's own prediction table (`L75`: knockdown gives "GLUT1 up") has the opposite sign to the only HDAC5 knockdown datum on GLUT1 that LEGEND holds, and the report cites neither. DATO.
- The HDAC4/mouse-heart half: 32236769 abstract confirms exercise, AMPK, HDAC4 phosphorylation, GLUT1 up "through reducing its inhibition on MEF2a", ChIP-PCR "novel interaction" MEF2a-GLUT1 in HF + exercise hearts. The paper's own title says exercise acts "through inhibiting HDAC4". The report's gloss "relief came from phosphorylation and consequent mislocalization, not from blocking catalysis" (`L20`) is not in the abstract and sits against the title's word "inhibiting". 33164260 is a mouse ischaemia-reperfusion/cardiomyocyte paper (HDAC4 "proven to repress" beta-catenin and GLUT1), with no MEF2 and no HDAC5. The report labels the pair "cardiac/cancer" (`L118`); neither is cancer. Both are HDAC4, both cardiac.
- Absence clause ("no HDAC5-GLUT1 neural data exist"): I did not rerun a search for it; it stands on the producer's and earlier packages' bounded title/abstract searches. Depth: abstracts only; full text of 22991226 unreached by me and by earlier packages.
- One neural-adjacent datum the item should name: 34021541 (mouse hippocampal neurons, epilepsy models) shows HDAC5 silencing lowering HIF1α and PFKFB3, not GLUT1.

### P02 — catalysis versus scaffold is output-, paralog- and cell-dependent — SUPPORTED (one clause unverifiable by me)

- 39923817: I read the PMC full text (XML). DATO: the HDAC5 cysteine mutants "exhibited almost no deacetylase activity" in the in-vitro assay, "retained their ability to bind HDAC3"; the authors list as a limit that the mutation may disrupt binding to some other factor. Abstract: nucleus accumbens medium spiny neurons, rat, Scn4b repressed "deacetylase-dependent". Results: neither CSCS nor 3SA-CSCS reduced cue-reinstated seeking. Items's "with HDAC3/MEF2C binding kept" holds.
- Missing half that favours the report: the same paper states the CSCS mutants "did not alter HDAC5-MEF2C binding" nor "HDAC5's ability to reduce MEF2-dependent gene expression in cultured primary striatal neurons". So in rat striatal neurons the MEF2-reporter output is catalysis-independent while Scn4b is catalysis-dependent. This is the cleanest statement of the P02 inference (output-dependent) and the producer's item and `evidence.tsv` do not record the MEF2 half. DATO, full text.
- 17956988: abstract confirms "His-976-Tyr ... catalytic efficiency 1,000-fold higher than WT" and extension to HDAC5 and -7. The clause "without raising reporter repression" comes from the Results, which I could not open (publisher withholds the XML); it rests on the producer's/earlier package's partial-full-text receipt (`hdac5_inv16_20261107/output/receipts/FTR-20261108-17956988-91.json`, verbatim locator recorded). UNVERIFIABLE by me for that clause.
- No source tests catalysis for SLC2A1: absence, perimeter as the producer's; not rerun.

### P03 — the Bdnf paper shows a class II inhibitor derepressing (MC1568) — PARTLY (core supported; one clause conflates two experiments)

Source 23916482 (Koppel and Timmusk 2013, Neuropharmacology 75:106-115). I read the abstract; Methods and Results not read. DATO, what was measured:
- Cells: rat primary neurons (title: "cortical neurons"; MeSH "Animals, Newborn", "Cerebral Cortex"). Four inhibitors compared on Bdnf mRNA: SAHA (class I/IIb), MS-275 (class I), MC1568 (class II selective, the authors' label), tubacin (HDAC6).
- Readout: "inhibition of class II HDACs resulted in rapid upregulation of Bdnf mRNA levels" (a transcript, not promoter reporter), whereas class I inhibition was "markedly delayed". Histone acetylation at promoters I and IV rose rapidly with SAHA.
- Separate experiment: "HDAC4 and HDAC5 repressed Bdnf promoter IV activity" (overexpression/reporter; cell type not given in the abstract).
- Separate again: the CRE element is "critical" for promoter IV induction by MS-275, MC1568, SAHA and valproate, while "MEF2-binding CaRE1 element was not necessary for promoter IV induction by HDAC inhibition". The MEF2-independence is about the inhibitor-induced response, not about the HDAC4/5 repression.
- The item's phrase "HDAC4/HDAC5 repressed promoter IV, with MEF2 element not required" can be read as MEF2 being unnecessary for HDAC4/5 repression; the abstract does not say that. Rewrite as two clauses.
- The report's conclusion "catalytic inhibitors act on only part of the class IIa repressive output" (`L33`, `L99`) is not in the abstract. The abstract shows an inhibitor derepressing quickly: the opposite use. SUPPORTED. It also does not show that MC1568 acts through HDAC5 catalysis (MC1568 selectivity is disputed in `nb3_class_iia_it32_20261107/output/README.md` item 4 and `tools.tsv` T08; I did not check that dispute against a primary source).
- INFERENZA: for this MEF2-family target the only cited neuronal inhibitor result contradicts "catalytic inhibition gives little/no change"; but it does not test SLC2A1 or HDAC5 specifically and works through CRE, not MEF2.

### P04 — direction of the GLUT1 change in WWOX deficiency is undetermined — SUPPORTED (module pointers confirmed; primary datasets not reopened)

- `nb3b_action_it32_20261107/output/README.md` item 5 exists and says what the item says (SLC2A1 higher in organoid and shWWOX human neural progenitors/neurons, lower in P17 mouse brain, nominal in P47T; "A change in SLC2A1 is not a benefit"). I did not reopen the underlying expression sets.
- 25491415 abstract (review): Wwox-knockout mice "succumb to hypoglycemia and other metabolic defects" by 3-4 weeks. 34747138 abstract: neuronal WWOX restoration rescued "brain hyperexcitability and seizures, hypoglycemia, myelination deficits". Neither abstract mentions brain glucose or GLUT1 amount. Systemic hypoglycaemia is not brain GLUT1: item is right.
- Addition the item lacks: 27308416 is a short commentary; its abstract says WWOX "modulates HIF1α, thereby regulating this metabolic state" of aerobic glycolysis and does not name GLUT1 or SLC2A1. The report's "WWOX loss raises GLUT1 via HIF1α-driven aerobic glycolysis (PMID 27308416)" (`L45`) is the report's reading, not the abstract's.

### P05 — SMRT/N-CoR-HDAC3 supplies the activity linked to class II HDACs — SUPPORTED

11804585 (Fischle 2002, Mol Cell): abstract read. DATO: the catalytic domain of HDAC4 binds HDAC3 via N-CoR/SMRT; loss of that binding loses the enzymatic activity associated with HDAC4; "HDAC4 and other class II HDACs are inactive in the context of the SMRT/N-CoR-HDAC3 complex" and regulate transcription "independently of any intrinsic HDAC activity" (HeLa, in vitro). HDAC5 is not named in the abstract; SLC2A1 and neurons not addressed. The report's `L33` sentence is uncited: item right. INFERENZA that deserves recording: for HDAC5 itself the abstract-level class statement is contradicted for other outputs by 39923817 (Scn4b, rat NAc, catalysis-dependent) and by 26061431 (cytosolic Hsp70 deacetylation by HDAC5 in human cancer lines); the report cites neither.

### P06 — no primary promoter-level source that MEF2 governs SLC2A1 — PARTLY (absence stands at its perimeter; a second route turns up one more MEF2-GLUT1 report)

- My title/abstract query `MEF2 AND (GLUT1 OR SLC2A1) AND (promoter OR transcription)` returned 3 hits (26267903 Neuro2a HMB, abstract: HMB raised MEF2 activity and GLUT1/GLUT3 expression; 18483800 GLUT4 in L6; 15364617 GLUT4 in rat heart). It did not return 32236769 (abstract spells MEF2a). The producer's count was 5; the difference is the query form.
- Second route (the producer says none was run): `(MEF2 OR "myocyte enhancer factor") AND ("glucose transporter 1" OR GLUT1 OR Slc2a1) AND (HDAC4 OR HDAC5 OR "class IIa")` returned 32236769 and 40250106. DATO, 40250106 abstract (Vet Microbiol 2025): HDAC4 knockdown/overexpression changed glucose uptake and "HDAC4 regulated GLUT1 and GLUT3 expression through ... MEF2A", in PEDV-infected Vero (monkey) and IPEC-J2 (pig) cells; not promoter-level, not HDAC5, not human, not neural. The earlier package already held it (`hdac5_inv16_20261107/output/queries.tsv` Q04), so LEGEND knew it; the item's "5 hits" list omits it.
- 32236769 ChIP-PCR is binding evidence of MEF2a at GLUT1 in HF + exercise mouse hearts, abstract only; "governs" is not shown. The item's wording is right.
- Verdict logic: the claim "no promoter-level source" survives; the claim as bounded ("second route not run") needs the second route and 40250106 added.

### P07 — 3.5-19.1 nM is a span across HDAC4/5/7/9 — SUPPORTED

40478640 (Gautam et al., J Chem Inf Model 2025). I read the PMC full text (XML); figures and the per-HDAC table were not rendered. DATO:
- The abstract: "SPR ... using four different purified class IIa HDACs and MEF2A ... fairly comparable nanomolar affinity (3.5 nM to 19.1 nM)". So the range does not cover HDAC5 alone; it pools HDAC4, 5, 7 and 9. The per-HDAC K_D values, rate constants and error (mean ± SD, three independent experiments) are in a figure I could not read.
- Text in Results 2.5: "slightly higher SPR affinities (lower K_D values) for HDAC4-MEF2A and HDAC7-MEF2A" and "slightly weaker affinity (higher experimental K_D value)" for HDAC9. INFERENZA: HDAC5 sits between those, so 3.5 and 19.1 are probably not HDAC5's values; its own value is unknown to me.
- Methods 3.1: HDAC4, HDAC5, HDAC9 from MyBioSource, HDAC7 and MEF2A from LSBio (vendor proteins, catalogue numbers only; tag and length not in the text); MEF2A immobilised on CM5 chips; 1:1 kinetic fit. The MD part uses "only truncated class IIa HDAC regions", no DNA. Not a neuron measurement; not a repression measurement; the report's "nanomolar MEF2 sequestration" (`L10`) is a chip-surface binding constant, not sequestration in cells.
- Locator correction for `evidence.tsv` V01: the sentence with "3.5 nM to 19.1 nM" is verbatim in the Abstract, the end of the Introduction, and the Conclusion, not in Results 2.5 (Results 2.5 says "fairly comparable to nanomolar affinity" and points to a figure).

### P08 — the HDAC7 PROTAC shows the method, not an HDAC5 degrader — SUPPORTED

39049738 (Adv Sci 2024) abstract read: PROTAC B4 "selectively targets and degrades HDAC7"; LPS-stimulated macrophages and a mouse model; HDAC7 role "surpasses its deacetylase function"; TLR4 pathway, TRAF6-TAK1 interaction. Not neural, not MEF2, not GLUT1; Results (selectivity, deacetylase-dead rescue) not read by me. 40667573 (review, Future Med Chem 2025) abstract read: degraders "effectively eliminating both enzymatic and scaffolding functions"; "selective HDAC4 and HDAC6 degraders"; cancer context. So the report's `L48` quote is accurate; its step to "direct proof-of-principle ... exactly the question posed here" and "HDAC5 sibling" is the overreach the item names. Report `L122` itself concedes HDAC5-selective degraders may not exist.

### P09 — the ketogenic-therapy paper's finding is incomplete seizure control — SUPPORTED

41830506 (Klepper et al., Epilepsia Open 2026) abstract read. DATO: 53 Glut1DS patients on ketogenic dietary therapy; epilepsy in 44; "On KDT monotherapy 27/44 (61%) patients became >90% seizure free, rated as responders. 17/44 were non-responders." Of the 17, 10 responded to KDT plus antiseizure comedication and 7 did not. "No correlations of seizure control to ... SLC2A1 variants." The report's quote (`L36`: ketones "as an alternative fuel ... effectively control[] seizures") is verbatim the abstract's first, background sentence. The paper's finding is "failure to control epilepsy is more common than expected". Ketones bypass glucose transport; the abstract says nothing about raising GLUT1. The report's inference that this "establish[es] that higher brain glucose-transport capacity is generally protective" (`L36`) is not drawn by the paper (INFERENZA by the report; not supported by this source). Item correct. `evidence.tsv` V07 carries the finding sentence but not the 17/44; add a row for it.

### P10 — the deacetylase-independence source is an HSV-1 ICP0 paper — SUPPORTED (with a wording correction on setting)

15194749: Lomonte et al. 2004, J Virol 78(13):6744-6757, title "Functional interaction between class II histone deacetylases and ICP0 of herpes simplex virus type 1" (report's table label "Class II HDACs & ICP0 of HSV-1" is correct; the PMID matches). I read the PubMed abstract only; PMC421675 exists, not opened. DATO what it says: class II (not "class IIa" in the abstract) HDACs 4, 5, 7 bind ICP0 "through their amino-terminal regions"; "This region ... is responsible for the repression, in a deacetylase-independent manner, of MEF2 by sequestering it under an inactive form in the nucleus"; "ICP0 is able to overcome the HDAC5 amino-terminal- and MITR-induced MEF2A repression in gene reporter assays".
- Scope: the deacetylase-independent statement belongs to "this region" (the N-terminal region, homologous to MITR), which has no catalytic domain; in the abstract it reads as background characterisation, with the new result being ICP0 relieving N-terminal/MITR repression of MEF2A in reporter assays. It supports deacetylase-independent MEF2 repression by N-terminal fragments, in a viral-protein context; not full-length HDAC5, not neurons, not SLC2A1.
- The report quotes the clause with a changed subject: "these proteins are 'responsible for the repression ...'" (`L22`), moving it from "this region" to the proteins. Small, and it widens the claim.
- Item correction: the abstract does not place the reporter assays in HeLa (HeLa appears only in MeSH). Say "cell line not given in the abstract".
- Corroboration the item could cite: 39923817 (rat striatal neurons) shows catalytically impaired HDAC5 still reducing MEF2-dependent expression; 26061431 states HDAC5's nuclear repression does not depend on its own deacetylase activity while arguing a separate cytosolic catalytic role. Independent labs, so the MEF2-output half of the report's scaffold claim has more support than the ICP0 paper alone.

### P11 — lithium suppressed PTZ seizures in all three Wwox genotypes — SUPPORTED (through an existing receipt; figure not viewed by me)

32000863 (Cheng et al. 2020): I read the PMC text. Abstract: lithium "significantly abolishes the onset of PTZ-induced seizure in Wwox-/- mice", and the Fig. 7d legend reads "suppressed PTZ-induced seizure activity in Wwox -/- mice ... n.s., non-significant". The report's word "abolishes" is the abstract's. The genotype-nonspecific point is in the figure, which I did not view; the ledger receipt `FTR-20260927-32000863-02` (figures read, image and legend) records: panel d stacks +/+, +/- and -/-, each with its own bracket, "lithium suppresses in all three genotypes". I confirmed the receipt text, not the image. The "no known catalytic substrate / scaffold hub / GSK-3 beta" statements are credited by the report to an internal knowledge-base entry without an ID (`L36`), so they cannot be checked as a source.

### P12 — HDAC5 loss or inhibition lowered HIF-1alpha and GLUT1 mRNA in hypoxic cancer lines — PARTLY

Check against the held file `disease-models/wwox/research/drug_repurposing/decisive_rechecks_it36_20261108/output/hdac5_hif.tsv` (rows A01-A07, B01-B02, C01-C02, D01-D03) and the sources.
- 26061431 (Chen et al. 2015, Cell Cycle): I read the PMC full text, figures not viewed. DATO: in Hep3B, HeLa and MCF7 (human), "only HDAC5 knockdown remarkably impaired hypoxic accumulation of HIF-1α", proteasome-dependent (MG132 rescue). LMK235 (called HDAC5-specific by the authors) lowers HIF-1alpha accumulation in Hep3B; "similar effects ... within HeLa and MCF7 (not shown)"; also in rat H9c2 cardiomyocytes. The catalytic mutant C698/H704A "was unable to stabilize HIF-1α"; the cytosolic S278/279A mutant raises it, the nuclear-locked mutant "barely" does.
- GLUT1/CA9: "only HDAC5 knockdown significantly blunted the hypoxic upregulation of CA-IX (p = 0.0035) and GLUT1 (p = 0.0014)" after 6 h hypoxia (qRT-PCR). The text does not name the cell line for this mRNA experiment (figure); t-test on 2^-ddCt, threshold p < 0.01; no HIF1A knockdown arm is described in the text, so HIF-dependence of the GLUT1 fall is the authors' background statement. The LMK235 arm measured HIF-1alpha protein/localisation, not GLUT1 or CA9 mRNA.
- So the item's "knockdown or LMK235 lowered HIF-1alpha and the GLUT1 and CA9 mRNA response" is right for knockdown (human cancer lines, hypoxia, transcript), and right for LMK235 only for HIF-1alpha. "Needing catalytic and cytosolic HDAC5" is shown for HIF-1alpha stabilisation, not for the GLUT1 mRNA. The cell lines are human cancer lines (not neural, not WWOX-deficient). The report's `L83` and `L153` cross-check is the only place HIF is touched; it cites none of this.
- The sign agrees with 22991226 (muscle) and opposes the report's table: two independent human contexts give lower GLUT1 on HDAC5 loss.
- "Three reports run the other way" (hdac5_hif.tsv D01-D03; I read all three abstracts): 42413489 (Mol Cell 2026, PDAC): HDAC5 loss reprograms hyper-acetylated FOXA1 to HIF1α-target genes, "potentiates HIF1α transcriptional activation" (clear opposite). 36124413 (PCOS mouse ovary): HDAC5 overexpression "suppressed activation of ... HIF-1α/VEGFA/VEGFR2 signaling" (opposite; mouse, non-neural, partly via VEGFR2 acetylation). 35704695 (PC12, intermittent hypoxia): HDAC5 dephosphorylation/degradation goes with more HIF-1α, but the same abstract calls HDAC5 "an upstream activator of HIF-1 signaling": direction ambiguous at abstract level, as `hdac5_hif.tsv` D03 itself says. So two clear and one ambiguous.
- 34021541 (item P12 lists it): mouse hippocampal neurons and lithium-pilocarpine model, no hypoxia, no cancer line; HDAC5 silencing reduced HIF1α and PFKFB3; GLUT1 not measured. It is a neural datum for the HIF arm, not a hypoxic-cancer-line datum. 19071119: abstract only; HDAC4/HDAC5 "enhanced transactivation by HIF-1alpha without stabilizing" it, human cell line unnamed.
- Reuse versus independent confirmation: the lowering of HIF-1alpha comes from one lab and one paper (26061431) with a neural-epilepsy paper as a second, weaker, non-hypoxic supporter; the GLUT1/CA9 mRNA arm is a single paper.

### P13 — raising GLUT1 in a haploinsufficiency mouse raised CSF glucose and reduced seizures — SUPPORTED

40754252 (Tang et al., Neurobiol Dis 2025) abstract read: transgenic human GLUT1 locus in a GLUT1DS mouse; "raised cerebrospinal fluid (CSF) glucose levels, improved motor performance and reduced the frequency of seizures"; the rise in GLUT1 was "at least partly the result of an increase in murine Slc2a1 (Glut1) activity, most likely ... a long non-coding RNA". The abstract also says ketogenic diets "do not address the underlying cause - low brain glucose", i.e. the paper separates fuel bypass from restoring GLUT1. 28106060: title and identity only (AAV9 not seen by me). The item's INFERENZA (favourable analogy for a deficiency lesion, not evidence for WWOX loss where GLUT1 may already be higher) stands.

### Verdict table

| P | Verdict | One-line reason |
|---|---|---|
| P01 | SUPPORTED | human primary muscle, knockdown, GLUT1 "expression" lower (level not stated), uptake up; abstract level; neural-absence perimeter not rerun |
| P02 | SUPPORTED | 39923817 read in full; 17956988 reporter clause unreached by me; MEF2-half of 39923817 missing from item |
| P03 | PARTLY | inhibitor-derepression core right; "MEF2 element not required" is about inhibitor induction, not HDAC4/5 repression |
| P04 | SUPPORTED | module pointer confirmed; 27308416 abstract names HIF1α, not GLUT1 |
| P05 | SUPPORTED | HDAC4 catalytic domain, HeLa/in vitro; HDAC5 not named |
| P06 | PARTLY | absence holds at one-route perimeter; second route finds 40250106 (HDAC4-MEF2A-GLUT1/3, Vero and pig cells) |
| P07 | SUPPORTED | pooled over four HDACs; per-HDAC values only in a figure; HDAC5 value probably inside, not at an end |
| P08 | SUPPORTED | method precedent in macrophages only |
| P09 | SUPPORTED | 17/44 non-responders confirmed; quote is the abstract's background sentence |
| P10 | SUPPORTED | wording fix: HeLa not tied to reporter assays; statement belongs to "this region"; report changed the subject |
| P11 | SUPPORTED | via existing figure-read receipt; I did not view the figure |
| P12 | PARTLY | knockdown arm right; LMK235 arm has no mRNA readout; 34021541 is not hypoxic or cancer; two of three counter-reports clear, one ambiguous |
| P13 | SUPPORTED | abstract; analogy only |

Counts: SUPPORTED 10, PARTLY 3, NOT SUPPORTED 0, UNVERIFIABLE 0 as whole propositions (UNVERIFIABLE clauses: P02 reporter clause; P11 image; P01 neural-absence search).

---

## B. Coverage audit of the first extraction

I read all 155 lines of the report and compared with the 60 rows of `extraction.tsv`. Twelve points, deliberately from the ends of lists, caveats, side remarks and a compound named in passing.

| # | Report point (anchor) | Extraction row | Result |
|---|---|---|---|
| 1 | "Truly HDAC5-selective catalytic inhibitors and ... PROTAC degraders may not yet be fully optimized; existing class IIa inhibitors are largely pan-selective" (`L122`) | E37, E38 | PRESENT |
| 2 | MC1568 named in passing inside the Bdnf evidence (`L33`) | E39, E31 | PRESENT |
| 3 | Last item of the supporting-actions list: HIF1α knockdown to separate scaffold/MEF2 axis from Warburg axis (`L153`) | E49 | PRESENT |
| 4 | "Confirm ... via promoter ChIP and MEF2-reporter ... before committing to the full ARMS design" (`L151`) | E47 | PRESENT |
| 5 | Confidence label "high — mechanistically triangulated across five findings" and "Refuted / disfavored" for an untested hypothesis (`L111`, `L114`) | E58, E03 | PRESENT |
| 6 | "This is a weighted inference requiring functional confirmation, not a settled fact" and "The two can coexist" (`L45`) | E16 | PRESENT |
| 7 | Third decision branch: abandon if raising GLUT1 worsens the signature "regardless of mechanism" (`L149`) | E52 | PRESENT |
| 8 | Paralog control: "confirm HDAC5-selective degradation by Western across class IIa members" (`L144`) | E46 | PRESENT |
| 9 | Nuclear-locked "14-3-3 S→A" versus cytoplasm-locked mutants, and the predicted-outcome table (`L73-81`, `L139`) | E43, E59 | PRESENT |
| 10 | "A second, independent axis shows HDAC4 represses the β-catenin → GLUT1 program" (`L20`) | E24 | PRESENT_NARROWED (the word "independent" and the report's use of it as separate support is not recorded; E24 note "cancer context" is wrong, 33164260 is a mouse cardiac paper) |
| 11 | "WWOX-DEE knowledge base ... loss-of-function scaffold hub with no known catalytic substrate" and lithium (`L36`) | E18 | PRESENT |
| 12 | "Localization modulator (forced nuclear export)" as the alternative route (`L148`) | E41 | PRESENT |

Result of B: 11 PRESENT, 1 PRESENT_NARROWED, 0 MISSING of 12. Because no MISSING was found I did not need the extension scan, but I swept the remaining lines for the same kinds of content (hedges, caveats, compounds, experiments, counter-arguments, ends of lists) and found no further miss. Two annotation errors in the extraction (not coverage misses): E24 note "cancer context" (should be mouse myocardial ischaemia-reperfusion/cardiomyocytes); E29 note "rodent cultured neurons" and `reconcile.tsv` row E06 "mouse hippocampal neurones": the 12641737 abstract says "cultured hippocampal neurones" and names no species. Also E53 "Direct SLC2A1 evidence is HDAC4-based (cardiac, cancer)" repeats the cancer label.

### Additional checks made while reading the report (not in `items.md`)

- His/Tyr gloss (`L24`, `L58`). The report says the weak activity is restored by mutation of "an active site histidine to tyrosine" and adds "because the active-site histidine is naturally replaced by tyrosine". DATO, abstract of 17956988: "A catalytic Tyr is conserved in all HDACs except for vertebrate class IIa enzymes where it is replaced by His." So class IIa carry His where other HDACs carry Tyr; the report's explanatory clause is inverted. The 18308563 abstract (read) gives the report's quoted restoration conditions correctly and adds that class IIa enzymes "isolated from mammalian cells are contaminated with other deacetylases", which the report does not carry. The producer's `README.md` section d and `reconcile.tsv` row E04 have this right.
- 12641737 (Chawla et al. 2003, J Neurochem): abstract read. It measures nucleocytoplasmic localisation of HDAC4 and HDAC5 in cultured hippocampal neurones (species not stated). It does not measure repression or catalysis; "HDAC5 repression is governed by catalysis-independent localization" (`L31`) is the report's addition. The producer marks this correctly (E30) but writes "mouse" in `reconcile.tsv` row E06 and `README.md` section c, and "rodent" in `extraction.tsv` E29 and `chains.tsv` C01/C06; the abstract names no species.
- `chains.tsv` C01 context "HDAC4 in rat/mouse heart and cancer lines": 32236769 and 33164260 are mouse (heart failure after infarction; ischaemia-reperfusion with cardiomyocytes); neither is cancer nor rat. Same error as `extraction.tsv` E24 and E53 notes.

---

## C. Reconciliation sample (8 rows of `reconcile.tsv`, plus one extra)

Class availability: `reconcile.tsv` has no row labelled `superseded_or_contradicted` (its classes are already_present_and_used, unverified, verified_or_corrected, present_not_used, new_to_legend). I took 4 new_to_legend, 2 already_present_and_used, 2 present_not_used (the minimum for the first three classes was 3, 2, 2) and could not sample the fourth class. I note below which rows should carry it.

| # | Row (items) | Class | Pointer check | `prior_brief_fate` vs `hdac5_inv16_20261107/BRIEF.md` | Verdict |
|---|---|---|---|---|---|
| 1 | E06,E29,E30 | new_to_legend | `git grep` for 12641737 across `disease-models`: hits only in this retest folder, so "not held" is true. Abstract matches the row except species. | "kept": BRIEF section 5 lists localisation among the structure-function comparisons; `experiment.tsv` step 2 has "localisation (nuclear-locked versus cytoplasmic)". Checked, correct. | OK; fix "mouse" (abstract names no species) |
| 2 | E12,E13 | new_to_legend | 40754252 and 28106060 appear in no other package (git grep). Abstract matches (CSF glucose, seizures, partly murine Slc2a1 via a lncRNA). | "narrowed": BRIEF section 4 says the GLUT1-deficiency precedent "shows a possibility in that lesion, not a benefit of an increase in WOREE". Checked, correct. | OK |
| 3 | E25 | new_to_legend | 15194749 not held elsewhere (git grep). Identity MATCH. Row says reporter assays "in HeLa": the abstract does not say so. | "omitted": BRIEF contains no ICP0 or N-terminal MEF2 statement. Checked, correct. | OK; delete "in HeLa" |
| 4 | E34,E35,E36 | new_to_legend | 39049738 and 40667573 held nowhere else (git grep). Abstracts match (macrophage, TRAF6-TAK1; cancer review). | "narrowed": BRIEF section 5, "an HDAC7 PROTAC precedent is methodological". Checked, correct. | OK |
| 5 | E01,E02,E60 | already_present_and_used | `ranking_it8_p9_20261029/investigations_it20.tsv` line 17 holds INV-16 (read); `hdac5_inv16_20261107/output/three_questions.tsv` Q1-Q3 exists and Q3 is the desirability question. | "kept": BRIEF Goal splits the question into three. Checked, correct. | OK |
| 6 | E42-E46 | already_present_and_used | `hdac5_inv16_20261107/output/experiment.tsv` exists, four steps; step 1 knockdown with wild-type rescue, step 2 one structure-function comparison, step 4 compound arm. The report's PROTAC arm and full mutant panel are not in it. | "narrowed": BRIEF section 5 "not all mutants as a mandatory panel"; "Do not make the package depend on a hypothetical HDAC5 degrader". Checked, correct. | OK |
| 7 | E05,E33 | present_not_used | `batch_it28_p3_hdac5_20261105/B_class_iia_biology/README.md` line 18 holds 11804585 with the SMRT/N-CoR-HDAC3 sentence (read). `receipts/FTR-20261108-17956988-91.json` holds the H976F "preserved WT interactions with ... HDAC3-N-CoR" locator (read). | "kept": the BRIEF never names HDAC3; HDAC3 partner binding is kept only as a mutant control in `experiment.tsv` step 2. "kept via experiment.tsv" is accurate; "kept in the brief" is not. | OK; reword fate note |
| 8 | E24 | present_not_used | `hdac5_inv16_20261107/verify/audit_h.md` line 95 lists 33164260 full text as not read (checked). But `output/evidence.tsv` row H12 and `output/README.md` Q1 use 33164260 as the HDAC4 counter-sign. | "kept": BRIEF does not name 33164260; the baseline package does. | Class is wrong: it is already_present_and_used |
| 9 (extra) | E58,E59 | unverified | `decisive_rechecks_it36_20261108/output/hdac5_hif.tsv` and its README item 1 contradict the report's table (knockdown raises GLUT1) in human cancer lines. | "omitted": ok. | Should be superseded_or_contradicted, partly |

Other rows that fit `superseded_or_contradicted`: E03,E07,E08 (the NB3 neuronal catalytic-loss arm in 39923817 cuts against "scaffold only"; the row itself says so, class is `unverified`).

The README tallies (60 items; class counts 23/13/12/9/3; fate counts 19/18/12/11) match `reconcile.tsv` when recomputed from its rows.

---

## D. Evidence sample (`evidence.tsv`, all 9 rows checked against the source)

| ev | Quote verbatim? | Locator right? | Carries the proposition? | Note |
|---|---|---|---|---|
| V01 | yes ("fairly comparable nanomolar affinity (3.5 nM to 19.1 nM)") | no: it is in the Abstract, end of Introduction and Conclusion; Results 2.5 only says "fairly comparable to nanomolar affinity" and points to a figure | yes (pooled over four HDACs) | fix locator |
| V02 | yes | Introduction: yes | yes (MD on truncated regions) | |
| V03 | yes | Abstract: yes | yes for P05 (HDAC4, HeLa/in vitro) | HDAC5 not named; the row says so |
| V04 | yes | Abstract: yes | yes for P03 (rapid Bdnf mRNA rise on class II inhibition) | MC1568 is identified as the class II inhibitor only in the preceding abstract sentence |
| V05 | yes | Abstract: yes | context only | cell type of the reporter not in the abstract |
| V06 | yes | Abstract: yes | yes, and the row note is correct (MEF2 arm not used by the inhibitor) | the item P03 text should say so |
| V07 | yes | Abstract: yes | partly: it shows insufficient control but not the number the item names (17 of 44) | add a row: "17/44 were non-responders" (same abstract) |
| V08 | yes (spans a line break in the abstract) | Abstract: yes | context for P01 (HDAC4, mouse heart) | |
| V09 | yes | Abstract: yes | yes for P06/P01 as binding association in HF + exercise hearts | |

Rows missing for decisive propositions (the nine rows back P01 HDAC4 half, P03, P05, P06, P07, P09 only):
- P01: no row for the HDAC5 knockdown sentence of 22991226, the datum the producer calls the opposite sign. Suggested row, depth `abstract_only`, quote "was associated with reduced GLUT1 (SLC2A1) expression", system human primary muscle cells, note "level (mRNA/protein) not stated; uptake and GLUT4 rose".
- P02: 39923817 ("The cysteine mutants exhibited almost no deacetylase activity", Results; and the MEF2-reporter statement in Results/Discussion that CSCS mutants did not alter HDAC5 reducing MEF2-dependent expression in striatal neurons); 17956988 reporter sentence is in a receipt only.
- P10: 15194749 ("responsible for the repression, in a deacetylase-independent manner, of MEF2 by sequestering it"; subject "This region").
- P12: 26061431 ("only HDAC5 knockdown significantly blunted the hypoxic upregulation of CA-IX"; "LMK235 effectively induced HIF-1α degradation") live in `hdac5_hif.tsv`, not here.
- P08, P11, P13: no rows (P11 rests on the ledger receipt FTR-20260927-32000863-02).

---

## Corrections the producer must make

1. `verify/items.md` P03: split "HDAC4/HDAC5 repressed promoter IV, with MEF2 element not required" into two clauses: HDAC4/5 overexpression repressed the promoter IV reporter; the MEF2-binding CaRE1 element was not necessary for promoter IV induction by HDAC inhibition (CRE was critical). State that the abstract's "inhibition of class II HDACs" is a transcript result in rat primary (cortical) neurons and that the repression experiment's cell type is not in the abstract.
2. `verify/items.md` P06 and `README.md` section d (MEF2 governs SLC2A1): run and record the second route; add 40250106 (HDAC4 regulating GLUT1/GLUT3 "through ... MEF2A" in Vero and IPEC-J2 cells; abstract only; already held in `hdac5_inv16_20261107/output/queries.tsv` Q04) next to 32236769 and 26267903; give the hit count of the exact query string (my copy of the title/abstract string returned 3, not 5; 32236769 is missed by it because the abstract writes MEF2a).
3. `verify/items.md` P10 and `reconcile.tsv` row E25: remove "in HeLa" from the reporter-assay description (the abstract names no cell line for them); state that the deacetylase-independent sentence is about "this region" (the N-terminal region), and that the report changed the subject to "these proteins".
4. `verify/items.md` P12 and `README.md` answer 2: say that GLUT1 and CA9 mRNA were measured with HDAC5 knockdown only (26061431, cell line not named in the text for that panel, p = 0.0035 and 0.0014); LMK235 and the catalytic mutant were read on HIF-1alpha protein and localisation. Remove 34021541 from the "hypoxic human cancer lines" source list (mouse hippocampal neurons, no hypoxia, HIF1α and PFKFB3 only) or list it as the neural, non-hypoxic supporter. State "two clear and one ambiguous" for the three counter-reports (35704695 is ambiguous at abstract level, as `hdac5_hif.tsv` D03 says).
5. `verify/items.md` P02 and `evidence.tsv`: add the MEF2 half of 39923817 (catalytically impaired HDAC5 still reduced MEF2-dependent expression in cultured rat striatal neurons) so the "output-dependent" inference is shown with both outputs from one paper.
6. `evidence.tsv` V01: change locator "(Results 2.5)" to "(Abstract; end of Introduction; Conclusion)"; add the per-HDAC statement from Results 2.5 ("slightly higher SPR affinities ... HDAC4 ... HDAC7"; "slightly weaker affinity" for HDAC9) as a row for P07.
7. `evidence.tsv`: add rows for 22991226 (knockdown sentence), 41830506 ("17/44 were non-responders"), 15194749, 39923817 as listed under D.
8. `extraction.tsv` E24 and E53 notes, `chains.tsv` C01 context: replace "cancer" (and "rat") by "mouse heart failure after infarction / ischaemia-reperfusion, cardiomyocytes". `extraction.tsv` E24: record that the report calls this axis "independent". `extraction.tsv` E29, `reconcile.tsv` row E06, `README.md` section c, `chains.tsv` C01/C06: delete the species ("mouse", "rodent"); the abstract gives none.
9. `reconcile.tsv`: row E24 class `present_not_used` to `already_present_and_used` (used in `hdac5_inv16_20261107/output/README.md` Q1); row E58,E59 and row E03,E07,E08 should carry (or note) `superseded_or_contradicted`; row E05,E33 `prior_brief_fate` note should say "kept via experiment.tsv step 2 controls, not named in the BRIEF".
10. `README.md` section i: 40667573 abstract was read by me and supports the report's L48 sentence (degraders "eliminating both enzymatic and scaffolding functions"; "selective HDAC4 and HDAC6 degraders"); update from "not read" once the producer has done the same.

## Open uncertainties

- The level of the human-muscle GLUT1 change (transcript or protein) and whether it is HDAC5-specific rests on an abstract. The full text of 22991226 remains unreached by any open route known to me. This is the single datum that most affects the sign argument, and nothing here narrows it.
- Per-HDAC SPR values (figure) and whether HDAC5's own value is nearer 3.5 or 19.1 nM: unknown to me.
- 17956988 reporter-repression result (Results), 15194749 Results, 23916482 Results (which cell type carried the HDAC4/5 reporter repression), and figure images for 26061431, 32000863: not seen by me.
- Whether MC1568 acts on class IIa catalysis at all (module says selectivity is disputed; I did not open that primary).
- The GLUT1/CA9 mRNA cell line in 26061431 (figure only) and whether the fall is HIF-dependent (no HIF1A knockdown arm described in the text).
- The absence claims ("no HDAC5-GLUT1 neural datum"; "no promoter-level MEF2-SLC2A1 source"): bounded to title/abstract searches by the producer and earlier packages; I ran two PubMed strings only (P06). Neither is a systematic negative.
- Weight of the producer's disclosure: five recorded readings plus about 12 unrecorded abstract views. All abstract-level depth statements in the items held when I re-read the abstracts; no overstatement of depth found. The late claim order is a process defect.
