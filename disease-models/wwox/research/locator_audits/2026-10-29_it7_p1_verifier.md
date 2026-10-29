# Independent verification of iteration 7, package P1 (typed signed glycolysis / PDH / lactate subnetwork)

Verifier: independent of the producer. Date: 2026-10-29. Object: commit 8b9861d5 on branch `task/it7-p1`, directory
`disease-models/wwox/research/drug_repurposing/subnetwork_it7_p1_20261029/`. Judged from the sources: the GEO count and TPM deposits on disk
(GSE156243, GSE126075), the iteration-5 per-gene tables, the iteration-6 P4 mouse key-gene table, the HGNC complete set downloaded fresh from the
public HGNC site, UniProt, Ensembl and ChEMBL REST, PubMed abstracts, GEO series and sample pages for GSE215425, and the deep-dive manifests.
Nothing was registered, no contact address was sent, nothing was paid for. Not medical advice.

## 1. Verdict

The numbers, identities and edge typing are accurate. The producer's checker passes (0 problems, also with the fresh HGNC file). Every
recomputed value agrees. The six-gene signature is confirmed and no other gene of the 24 qualifies. The weaknesses are (a) one firewall breach
in the fly head rows, (b) a few readings that go beyond what their source says (PDH "no change", glycolytic flux), (c) a framing that treats six
of 24 as a signal when about four would be expected from the 0.25 bin alone, and (d) several small factual or provenance slips. Nothing found
invalidates the tables as a descriptive record; item D1 needs a decision before the fly factorial is used as an evaluation.

## 2. Defects, severity-ranked

| # | Sev | Defect | Where | Repair |
|---|---|---|---|---|
| D1 | HIGH | **Firewall breach: fly head rows come from the evaluation candidate.** `systems.tsv` marks `fly_head_factorial` (E-MTAB-14948/14949, paper PMID 42909904) as `heldout_candidate` and README section 4 says no observation from an evaluation candidate enters the tables. Yet `fly_head_rnai_abeta` (same paper, same pan-neuronal Wwox RNAi plus Abeta42 design, adult head, day 14) carries O0198 (fly Ldh, log2 fold change 1.29, knockdown plus Abeta42 versus Abeta42; taken from the paper's differential-expression table, i.e. the processed form of the very deposit) and O0195 (lactate, mixed), feeding edges ED077 and the LDHA `sign_fly_head_rnai_abeta` column. The checker only compares system ids, so it cannot see that two system ids describe one experiment. The paper's abstract also states the Ldh/lactate rise, so the fly direction for LDH is known to the network before the test. | observations O0195, O0198; edges ED077; nodes sign_fly_head_rnai_abeta; systems rows 11 and 14 | Either drop the fly rows (and the fly column) and keep the fly factorial held out, or demote the factorial from evaluation and say the fly Ldh/lactate direction is a build input. Add a checker rule tying system ids to accessions. |
| D2 | MEDIUM | **Six of 24 is close to chance for the 0.25 bin.** Across the 8123 genes measurable in both human systems, 1338 (16.5 percent) pass the same rule (same direction, centred log2 at least 0.25 in both). With 24 network genes, about 4 are expected by the bin alone; P(6 or more) is about 0.19 under independence. The genes were chosen for biological reasons, not at random, so this is not a null test, but the question wording ("reproducible HIF-type module") and the "signature" label read stronger than a bin that a sixth of the transcriptome passes. The README does say the bin is a reading aid; it does not say how permissive it is. | README section 1; nodes.tsv `human_concordance` | State the genome-wide pass rate next to the rule. P3 must use the decile-matched null (already planned) and not the six genes as a pass criterion on their own. |
| D3 | MEDIUM | **PDH "no change" rests on an absent significance bracket.** O0193 / ED075 types PDH activity in the fibroblast line as `no_change`, `measured`, from a manifest note that the figure carries no knockout-versus-control bracket; n is unstated, so the figure shows no detectable difference, not equivalence. The paper's own abstract reports higher glycolytic enzyme activities in that line. | observations O0193; edges ED075; E07 | Mark the sign `no_change` with note "no significant difference shown; n not stated; not an equivalence test", or `UNKNOWN`. |
| D4 | MEDIUM | **Glycolytic flux "up" in the knockout fibroblasts is anchored on an oxygen-consumption sentence.** E03 quotes "reduction in oxygen consumption ... suggesting that ... glucose is utilized primarily for glycolysis" (hedged, respiration not a flux of glycolysis). Glucose uptake and lactate are reported elsewhere in the same paper, so the claim is probably right, but the cited anchor does not carry it. | O0197, ED074, E03 | Anchor to the glucose-uptake or lactate-production passage, or retype the readout as `respiration` (down) and drop `flux`. |
| D5 | MEDIUM | **Circular evidence on four inferred edges.** ED080 to ED083 cite E13, the producer-lineage prediction document written before the organoid genes were read, as evidence next to E12/E18. A prediction is not evidence for the mechanism it predicts. E18 supports raised HIF1A in the fibroblasts and cancer cells; it does not by itself show GLUT1/HK2/LDHA regulation by HIF1A in the quoted abstract sentence. The typing `inferred` is right; the evidence column overstates. | edges ED080 to ED083, evidence E13 | Remove E13 from `evidence_ids`; keep it as a note. Add the paper's own target-gene panel if it is read at full text (the manifest shows it was, FTR-20260814). |
| D6 | LOW | **Neuron arm contradicts half of the signature and the question wording includes it.** Day-14 neurons: SLC2A1 -0.35, PDK1 +0.44, LDHB -0.08 (no_change); only LDHA, BNIP3 agree. README labels the neurons "support only", but the question text names "neurons from the same line" as a system where the module is raised. | README section 1; nodes caveat | Say that the neuron arm agrees on 2 of 6 genes. |
| D7 | LOW | **README contradicts the GEO record on the organoid design.** README: "batch/differentiation not stated". GEO overall design: age- and batch-matched WT organoids from one hESC line (WiBR3); 2 of 4 WT libraries failed QC and were excluded. So the build system is one cell line, 4 versus 2 libraries after a 50 percent WT loss, and the batch is stated. The "4 v 2" is already correct. | README section 2; systems.tsv | Correct the text; record "single hESC line; 2 WT removed after QC". |
| D8 | LOW | **Fly replicate count inconsistent.** `fly_head_rnai_abeta` says 5 pooled-head replicates (lactate panel, five replicates); `fly_head_factorial` says 4 pooled-head libraries per cell; the paper's ATP test says N = 4. Different assays, but the table does not say so. | systems.tsv | State n per assay. |
| D9 | LOW | **Provenance of derived values is not committed.** The script docstring says the input SHA-256 is "written into the output header"; the code only prints it, and `derived_gene_values.tsv` has no header lines. The inputs sit outside the repository, so a reader cannot tell which files produced the table. (My recomputation used the same files on disk and matched, but that is not recorded.) | derive_gene_values.py, derived_gene_values.tsv | Write the two SHA-256 values and the CAGE library sizes into a sidecar file or the README. |
| D10 | LOW | **Patient MRS observation sits on a registry sentence.** O0196 / ED078 is typed `measured` from a needs.json entry quoting DL-BIO-008 (n = 1, second variant); the primary report was not re-read in this package. Typing is defensible but the measured weight is that of one confounded case. | E14, ED078 | Keep, and mark source as secondary in the note. |
| D11 | INFO | Several HGNC-symbol based lookups drop PKM, SLC16A3, PDK4, MBP, MOG in the CAGE matrix by symbol; the producer records them as unmeasurable and does not try alias symbols. Correct handling, but an alias search (for example the matrix may hold these under another symbol) was not logged. | derived_gene_values.tsv | Optional note. |

## 3. Check 1: recomputation

**Method.** Independent code (not the producer's) on the deposits: GSE156243 Salmon counts (4 knockout, 2 wild type; libraries scaled to 1e6, arm mean, log2 of
(mean + 0.5) ratio, median-centred over genes with mean count at least 10 in both arms) and GSE126075 TPM matrix (log2 of (TPM + 0.5) ratio,
median-centred over genes with at least 10 estimated tags in both arms, library sizes as in the producer's constants).

* **Organoid, 24 genes: all 24 agree with `derived_gene_values.tsv` to three decimals** (WWOX +0.416, SLC2A1 +1.371, HK2 +2.169, LDHA +0.717, LDHB +0.327,
  BNIP3 +0.420, PDK1 -0.385, HIF1A -0.285, PDHA1 +0.968, PLP1 +0.863 and the others). Nine of them also match the iteration-5 organoid key-gene table.
* **Progenitor CAGE, 20 measurable genes, and neuron CAGE, 20 measurable genes: all agree** (for example SLC2A1 +0.524 / -0.348, LDHA +1.258 / +0.698, PDK1 -0.674 / +0.442,
  HK1 +1.377 / +1.684, PLP1 -1.674 / -1.656). 35 values also agree with the iteration-5 per-gene table.
* **Mouse P17, 66 rows** (4 contrasts, key genes) match the iteration-6 P4 `key_genes.tsv` in value and in the 0.25 sign. The six non-matching signs
  (Wwox in three contrasts, Slc16a3 in three) are genes flagged not measurable, correctly recorded as `UNKNOWN` with the value kept.
* Total independently recomputed or re-read: about 150 numeric observations (requirement was 25).

**Signature rule.** Applying "centred log2 at least 0.25 in the same direction in both the organoid and the progenitor library" to the 24 network genes gives
exactly SLC2A1, HK2, LDHA, LDHB, BNIP3 (up) and PDK1 (down). HK1 (organoid +0.10), SLC2A3 (progenitor -0.23), PDK3 (opposite signs), PDHA1 (progenitor +0.15) and
SLC16A1 (organoid -0.04) fail; PKM, SLC16A3, PDK4, MBP, MOG have no progenitor value. **Confirmed; no other network gene qualifies.** Over the whole measurable
transcriptome 1338 genes qualify, which is why D2 matters.

## 4. Check 2: identities

All 24 gene nodes were checked: HGNC id and approved symbol, status Approved, UniProt accession (present in the HGNC record, primary accession active and
mapped to the same gene symbol and to human), Ensembl human gene (HGNC record and Ensembl lookup, display name equal to the symbol), MGI id (in HGNC
`mgd_id`), Ensembl mouse gene (Ensembl lookup, species and display name), ChEMBL target (single protein, Homo sapiens, UniProt accession equal), and the two fly
ortholog ids (FBgn0001258 is Ldh; FBgn0017558 is Pdk). **No wrong, withdrawn or deprecated identifier was found.** WWOX, BNIP3, MBP, PLP1 and MOG have a blank
ChEMBL target; a ChEMBL query by accession returns no target for any of them, so blank is correct. Set and process nodes (GO:0004739 pyruvate dehydrogenase
activity, GO:0006096 glycolytic process, CHEBI:24996 lactate) are valid terms. The fly Ldh node is shared by LDHA and LDHB (stated; ortholog not one-to-one).

## 5. Check 3: edge typing

* **Measured, 78 edges.** Every measured edge points at observation rows of the same target node and system with the same sign (programmatic, 0 mismatches), and the
  source is WWOX in all of them. 15 sampled by hand against the source: ED001/ED002 (HK2 organoid/progenitor), SLC2A1, LDHA, LDHB, BNIP3, PDK1 in the organoid and progenitor library
  (values above), four mouse set rows and two mouse gene rows (key_genes.tsv), ED054 (MEF HIF1A protein, E01/E04), ED055 (fibroblast, mixed, E06), ED076 (fibroblast lactate, E05). All
  supported. Over-reads: ED075 (D3), ED074 (D4), ED078 (D10).
* **No PDK1 to PDH to lactate link is typed measured.** PDK1 to PDH activity (ED084) is `inferred`; PDH to lactate (ED085) is `hypothesised`; the one PDH activity observation (ED075) is a WWOX to PDH measurement,
  not a PDK1 link. Good. The abstract of PMID 16517406 supports HIF-1 induction of PDK1 and PDK1 inhibition of PDH, in a non-WWOX system, which is how it is typed.
* **Inferred (5), hypothesised (2), association (3):** no causal overclaim. ED079 (WWOX-HIF1A, physical interaction, sign UNKNOWN) and ED087/ED088 (transporter-lactate, no direction) are
  `association` with sign `UNKNOWN`. ED086 (LDHA transcript up implies lactate up) is `hypothesised` and its note says no lactate is measured in any human neural system. The only weakness is
  the evidence column of ED080-ED083 (D5).

## 6. Check 4: paper-level anchors (18 in `evidence.tsv`)

* PMID 25012504 (Cell Death Differ 2014): abstract confirms physical interaction through the first WW domain, increased HIF1A levels and activity, increased glucose uptake, enhanced
  glycolysis, diminished mitochondrial respiration, GLUT1 raised; cells are mouse embryonic fibroblasts and cancer cells. E01, E02 (higher Pdk1, text only, level unspecified), E03, E04 (no
  WWOX effect on HIF1A under hypoxia), E11, E18 match the manifest locators (entries index into `verbatim_locators.entries`, zero-based).
* PMID 16517406 (Cell Metab 2006): abstract confirms HIF-1 induces PDK1, which phosphorylates and inhibits PDH, lowering oxygen consumption. E12 correct; non-WWOX; full text not read, as stated.
* PMID 35328751 (Int J Mol Sci 2022): abstract: WWOX silenced in human normal fibroblasts; higher glycolytic gene expression, activity and lactate in knockout in normoxia normoglycemia; further lactate increase in
  hyperglycaemia. Matches E05; the knockout/knockdown wording is a real inconsistency in the paper and is flagged by the producer. E06/E07 are hand readings of figures.
* PMID 42909904 (Brain Commun 2026): abstract confirms Ldh up, lactate up with Wwox knockdown in an amyloid model (see D1). E08 to E10 match the manifest entries (Ldh log2 fold change 1.2903; lactate rise
  confined to knockdown plus Abeta42; ATP unchanged, N = 4).
* One patient MRS (E14) and the need entries (E15, E16, E19) are internal documents; anchors present.

## 7. Check 5: firewall

* **Compound, reversal, agent, rating:** no compound or agent name, signature-reversal output, frequent-hitter list, card rating or priority label appears in any of the seven tables or in the README. (Compound
  names appear only in the checker's banned-vocabulary list, which is the intended use.) ChEMBL target ids are identity only.
* **Held-out systems:** GSE215425 and the E-MTAB records are not on disk anywhere in the repository or the shared data directory (no counts file was ever downloaded), and no row names `p47t_knockin_brain`, `human_organoid_scrna` or `mouse_p17_hipp_snrna`. The commit history cannot prove
  what was viewed in a browser; the single package commit (2026-10-29 15:03, 19 minutes after the mandate record) is consistent with the README statement and nothing contradicts it.
  **Exception: the fly rows, see D1.**
* The mouse P17 bulk contrasts are declared `seen_comparison` (analysed in the preceding iteration) and used only as a comparison column; correct and consistent.

## 8. Check 6: GSE215425 audit facts (GEO series and sample pages)

Confirmed: public since 2023-02-28; bulk RNA-seq of prefrontal cortex, parietal cortex, hippocampus and cerebellum from homozygous wild type (n = 5) and homozygous P47T mice (n = 5); 37 samples
(10 per region, cerebellum 4 versus 3, i.e. 40 minus 3); sample titles carry animal numbers (wild type M1-M3, F4-F5 = 3 male and 2 female; mutant M6-M7, F8-F10 = 2 male and 3 female), so
the same animals supply every region; sex is not a GEO characteristic field, only in the title, as the README says. Age is not stated in the GEO record (README correctly says not extracted).
The paper (PMID 36828035) describes a WW1-domain partial loss of function knock-in, not a null. All README statements about this system are correct.

## 9. What I could not verify

* Whether the evaluation candidates were looked at in a browser session before commit (no log).
* The CAGE control library size (51,007,825 tags) beyond the producer's own source note; it only affects the measurability call, not the ratio.
* Full text of PMID 16517406 and the target-gene panel of PMID 25012504 beyond the manifest.
