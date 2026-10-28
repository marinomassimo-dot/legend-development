# Independent verification of the WWOX nonsense-allele enumeration, 2026-10-28

Producer: scientist-b (ptc_readthrough_it4_e1a_20261028). Verifier: independent subagent; own computation first from NM_016373.4 and the repository ClinVar export. Verdict: no disagreement on any count; wording caveats applied to the note.

# Independent verification: WWOX NM_016373.4 PTC / NMD enumeration (scientist-d)

Producer's files (README, ptc_enumeration.py, ptc_alleles.tsv) were NOT read. Script: ptc_v.py in this directory; downloads in dl/ (Python -I).

## 1. Transcript (NCBI efetch, NM_016373.4, GenBank flat file)
- mRNA 2241 nt; CDS 126..1370 (1245 nt, 414 aa + stop; I translated it, ATG...TAA OK; codon 218 = TGG, 335 = TGG).
- 9 exons (mRNA coords): 1..232, 233..297, 298..355, 356..534, 535..641, 642..730, 731..916, 917..1181, 1182..2241.
- Exon-exon junctions in CDS coords (last nt of exon, c.): 107 | 172 | 230 | 409 | 516 | 605 | 791 | 1056 (last junction c.1056|c.1057; consistent with the acceptor name c.1057-2A>G). Exon 9 = c.1057..*.
- Exon of a CDS position: e1 c.1-107, e2 108-172, e3 173-230, e4 231-409, e5 410-516, e6 517-605, e7 606-791, e8 792-1056, e9 1057-.

## 2. ClinVar export (git show a2e0dd0f:disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv; file unchanged at HEAD)
Filter: title contains NM_016373.4, c.N X>Y single-nucleotide, p.XxxNNNTer. Each allele re-derived from the RefSeq sequence (ref base asserted, new codon asserted = stop, p. residue/number cross-checked). Result: **32 distinct SNV stop-gained alleles** (c.-level unique; two codons have two alleles each: W44 c.131/c.132, Y61 c.183 G/A, Y107 c.321 G/A, W288 c.863/c.864). Non-SNV Ter hits excluded (c.808_811dup p.Ser271Ter is a duplication; three stop-loss/del Ter415 rows).
Distance d = nt from the 3' end of the stop codon to the last junction (c.1056 minus last nt of the stop codon); the rule: d > 55 NMD-sensitive, 50 < d <= 55 borderline, d <= 50 or in last exon: escape. (Alternative convention, from the first nt of the stop: d+2.)

| # | c. | p. | exon | stop | +4 | d (nt, stop 3' end to last junction) | class | ClinVar |
|---|---|---|---|---|---|---|---|---|
| 1 | c.102C>A | p.Tyr34Ter | 1 | UAA | G | 954 | NMD | Likely pathogenic |
| 2 | c.127C>T | p.Gln43Ter | 2 | UAG | T | 927 | NMD | Pathogenic |
| 3 | c.131G>A | p.Trp44Ter | 2 | UAG | G | 924 | NMD | Pathogenic |
| 4 | c.132G>A | p.Trp44Ter | 2 | UGA | G | 924 | NMD | Pathogenic |
| 5 | c.160C>T | p.Arg54Ter | 2 | UGA | G | 894 | NMD | Pathogenic |
| 6 | c.183C>G | p.Tyr61Ter | 3 | UAG | G | 873 | NMD | Pathogenic |
| 7 | c.183C>A | p.Tyr61Ter | 3 | UAA | G | 873 | NMD | Pathogenic/Likely pathogenic |
| 8 | c.184G>T | p.Gly62Ter | 3 | UGA | T | 870 | NMD | Pathogenic |
| 9 | c.196G>T | p.Glu66Ter | 3 | UAA | A | 858 | NMD | Pathogenic |
| 10 | c.214C>T | p.Gln72Ter | 3 | UAA | G | 840 | NMD | Pathogenic/Likely pathogenic |
| 11 | c.255C>G | p.Tyr85Ter | 4 | UAG | T | 801 | NMD | Pathogenic |
| 12 | c.321C>G | p.Tyr107Ter | 4 | UAG | G | 735 | NMD | Pathogenic |
| 13 | c.321C>A | p.Tyr107Ter | 4 | UAA | G | 735 | NMD | Pathogenic/Likely pathogenic |
| 14 | c.403G>T | p.Gly135Ter | 4 | UGA | A | 651 | NMD | Likely pathogenic |
| 15 | c.511G>T | p.Glu171Ter | 5 | UAA | T | 543 | NMD | Likely pathogenic |
| 16 | c.571C>T | p.Gln191Ter | 6 | UAG | C | 483 | NMD | Likely pathogenic |
| 17 | c.583G>T | p.Glu195Ter | 6 | UAA | G | 471 | NMD | Pathogenic/Likely pathogenic |
| 18 | c.730C>T | p.Gln244Ter | 7 | UAG | G | 324 | NMD | Pathogenic/Likely pathogenic |
| 19 | c.749C>G | p.Ser250Ter | 7 | UGA | G | 306 | NMD | Pathogenic |
| 20 | c.779C>G | p.Ser260Ter | 7 | UGA | G | 276 | NMD | Pathogenic |
| 21 | c.790C>T | p.Arg264Ter | 7 | UGA | T | 264 | NMD | Pathogenic/Likely pathogenic |
| 22 | c.863G>A | p.Trp288Ter | 8 | UAG | G | 192 | NMD | Pathogenic |
| 23 | c.864G>A | p.Trp288Ter | 8 | UGA | G | 192 | NMD | Pathogenic |
| 24 | c.1005G>A | p.Trp335Ter | 8 | UGA | T | 51 | BORDERLINE | Pathogenic |
| 25 | c.1057C>T | p.Gln353Ter | 9 | UAA | C | -3 | ESCAPE (last exon) | Pathogenic |
| 26 | c.1060C>T | p.Gln354Ter | 9 | UAG | G | -6 | ESCAPE (last exon) | Uncertain significance |
| 27 | c.1114G>T | p.Gly372Ter | 9 | UGA | G | -60 | ESCAPE (last exon) | Pathogenic/Likely pathogenic |
| 28 | c.1165C>T | p.Gln389Ter | 9 | UAG | A | -111 | ESCAPE (last exon) | Conflicting classifications of pathogenicity |
| 29 | c.1171G>T | p.Glu391Ter | 9 | UAA | G | -117 | ESCAPE (last exon) | Pathogenic |
| 30 | c.1193G>A | p.Trp398Ter | 9 | UAG | G | -138 | ESCAPE (last exon) | Uncertain significance |
| 31 | c.1204G>T | p.Glu402Ter | 9 | UAG | A | -150 | ESCAPE (last exon) | Conflicting classifications of pathogenicity |
| 32 | c.1216C>T | p.Gln406Ter | 9 | UAA | G | -162 | ESCAPE (last exon) | Uncertain significance |

Negative d = stop lies wholly in exon 9 (the last exon); magnitude is nt past the junction (stop end beyond c.1056).

Literature allele not in the export: **p.Trp218\*** (PMID 39039877, per repo census). Codon 218 = c.652-654 (TGG), exon 7. c.654G>A (UGA) or c.653G>A (UAG); +4 = c.655 = A (codon 219 = AGT), so UGA+A or UAG+A; not a +4 C. Distance (stop 3' end c.654 to c.1056) = **402 nt** (404 from first nt) => NMD-sensitive by a wide margin under any rule. It is NOT among the 32 ClinVar alleles (no ClinVar row for c.653/c.654 in the export).

## 3. Tallies (my numbers)
- Total 32 = **23 NMD-sensitive** (exons 1-8, d >= 192) + **1 borderline** (p.Trp335*, c.1005G>A, exon 8, UGA, +4 T, d = 51 / 53 from stop start) + **8 escape**, all in exon 9 (c.1057C>T p.Gln353* ... c.1216C>T p.Gln406*).
- NMD-sensitive by exon: e1 1; e2 4; e3 5; e4 4 (Y85, Y107 x2, G135); e5 1; e6 2; e7 4; e8 2 (W288 x2). Check sum = 23.
- Stop codon: UAA 10, UAG 12, UGA 10. **UGA with +4 C: 0. +4 C at all: 2** (p.Gln191* UAG-C, exon 6, NMD-sensitive; p.Gln353* UAA-C, exon 9, escape). +4 G 20, T 6, A 4.
- 19/32 alleles have an original amino acid among the near-cognate insertions at their own stop (UGA: W/C/R; UAA/UAG: Q/Y/K) - I reproduce 19 under exactly this (Roy 2016-type) mapping. If instead one pools {W,R,C,Q,Y,K} irrespective of stop type: 22; with W/R/C only: 8. So the '19' depends on the amino-acid-set choice; it is a weak, literature-derived heuristic, not a measured property.

## 4. Rule-choice dependence
- Only p.Trp335* depends on the rule. Last exon / first 50 nt of exon 8 boundary: its stop ends at c.1005, 51 nt from the junction => strict 50-nt rule: marginally NMD-sensitive (the repo itself writes the 50-nt limit as 'ends at or before c.1006'); 55-nt rule: borderline; a 'stop must be >55' rule: borderline. Calling it 'borderline' is the defensible label; it is not an escape under any common variant, and not a confident 'sensitive'. Moving the cut to 'c.1006' is the repo's 50-nt statement.
- Nothing else changes between 50 and 55 nt (next-closest non-last-exon allele W288*: 192 nt; exon 9 alleles are escape regardless).
- Exon 9 is the last exon and the 3' UTR has no intron, so escape is mechanistic; but 50-55 nt is a predictor, not a measurement: long-exon NMD (exon 8 is 266 nt, exon 9 1060 nt) and the 'fair-weather' variability (class-A/B rule exceptions, long 3'UTR NMD) are not excluded. Escape from NMD also does not imply a stable/functional protein: exon 9 truncations remove the C-terminal SDR region.
- Distances for exon-1 alleles (e.g. Y34*, near start) can be affected by the start-proximal NMD-escape exception (reinitiation downstream); the simple rule ignores it.

## 5. Repo premise records
- CC-20260922-NMD-PREMISE-WITHDRAWAL-01 s1.3 and wwox_nmd_assay_census_20260922.md: both state **NEVER TESTED / PREMISE: NOBODY_LOOKED** - no WWOX allele of any class assayed with NMD inhibitor or NMD-discriminating quantification; ataluren, PTC124, G418, geneticin, gentamicin, readthrough (translational) = 0 repo hits; cycloheximide 78 hits are all protein-half-life chases. The census explicitly scopes it as a statement about the literature/repo as of 2026-09-22 (708 PubMed records), not about biology. The CC is 'PROPOSED - NOT PROPAGATED'. I did NOT independently re-run the PubMed census (not asked; no cross-check), so 'NEVER TESTED' is repo-attested, not verified by me; the claim as worded is correctly scoped.
- The CC and census use the same architecture arithmetic I did: last junction c.1056|c.1057; 50-nt limit c.1006, 55-nt limit c.1001.
- 'Reference genotype class' in this public edition: a WWOX-DEE genotype class (CLAUDE.md s0); concretely compound-heterozygous N/M (claim_registry line 98: 'the reference genotype = compound het N/M'), i.e. one missense allele (Q230P, p.Gln230Pro) plus a null-predicted acceptor splice allele c.1057-2A>G (splice_allele_rna_evidence_20260922.md, nmd_adjudication_reference_allele). The class is a syntactic label (working model, Gao 2025 N/N, N/M, M/M). It contains **no stop-gained allele**: neither a missense nor an exon-9 acceptor splice change is a nonsense codon. Predicted c.1057-2A>G outcomes (cryptic acceptor c.1063: no PTC; intron-8 retention: PTC downstream of last EEJ) are repo predictions, none measured (0 PubMed records for the allele; ClinVar VUS).
- Census read-through-candidate nonsense alleles in woree_therapeutic_class_census_20260921.md (lines 189-193): R54* (c.160, there written c.160G>T; ClinVar/RefSeq say c.160C>T - a typo in the census, since c.160 is C), W44* c.131G>A, R264* c.790C>T, Q191* c.571C>T, W218*. My classification: R54* e2 d=894, W44* e2 924, R264* e7 264, Q191* e6 483, W218* e7 402 - **all five NMD-sensitive**, matches the producer.

## 6. Comparison with producer's numbers
| item | producer | me | status |
|---|---|---|---|
| alleles | 32 | 32 | agree |
| NMD-sensitive | 23 | 23 | agree |
| borderline | 1 (W335*) | 1 (W335*, d=51) | agree |
| escape | 8, all exon 9 | 8, all exon 9 | agree |
| five census read-through candidates all NMD-sensitive | yes | yes (W218* 402 nt; computed, not in ClinVar export) | agree |
| 19/32 original aa among ataluren-inserted | 19 | 19 only under stop-specific near-cognate sets (UGA: W/C/R; UAA/UAG: Q/Y/K); 22 pooled; 8 W/R/C only | agree on the number, conditional on the aa set - a definition, not a datum |
I have no disagreement on counts. Not asserted by the task but worth flagging: the UGA+C count is 0 and +4 C count is 2 (my figures; producer's were not given for these).

Disagreement severity: none material (counts identical). Minor: (i) W335* label depends on 50 vs 55 nt; (ii) 19/32 depends on aa-set definition and is a weak heuristic; (iii) 5 of the 8 exon-9 alleles are VUS / conflicting in ClinVar (Q354*, W398*, Q406* VUS; Q389*, E402* conflicting), so 'escape' alleles are not all established pathogenic; (iv) the census's c.160G>T for R54* is wrong.

## 7. Does 'read-through is not a lever for the reference genotype class' follow?
- It follows from class composition, not from the NMD numbers: translational read-through (ataluren, aminoglycosides, ELX-02) acts only on a premature stop codon in the transcript; the reference class (Q230P missense + c.1057-2A>G acceptor) has no stop-gained allele, so there is no nonsense target. The NMD sensitivity of the 23/32 ClinVar nonsense alleles is irrelevant to this conclusion (and sensitivity does not by itself exclude read-through, it only lowers available mRNA).
- Residual caveats: (a) the premise is conditional on the class as stated; a change of the defined allele set revives the question; (b) one c.1057-2A>G outcome predicted by the repo (intron-8 retention / intronic poly(A)) would create a PTC, so read-through is not strictly impossible for that allele's aberrant transcript, but that is an unmeasured, repo-predicted RNA outcome and read-through on an NMD-immune but unmeasured transcript is speculation; (c) 'not a lever' should be tagged as an inference from classification (INFERENCE), not an experimentally tested negative: read-through has also never been tested for WWOX (NEVER TESTED), so the supported wording is 'no applicable target in this class', not 'read-through fails'.
- Therefore the conclusion is supported if worded 'no PTC allele in the class, hence no read-through target', and is overstated if worded as a demonstrated negative.
