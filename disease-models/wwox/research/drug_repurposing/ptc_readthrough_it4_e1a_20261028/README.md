# Premature-stop read-through for WWOX nonsense alleles: enumeration and reasoned abstention (IT4 E1, question A, scientist-b, 2026-10-28)

Non-canonical research material. Not medical advice; no efficacy, dose, wet-lab or clinical claim; nothing here changes the four scientific current files. No receipt was written or staged (no full text was read; see "Depth of every reading"). Association is not modulation, and modulation is not rescue.

Need: `NEED-WWOX-PTC-READTHROUGH` (Track B, variant/lesion-specific; goal deep_recovery). Track and goal are separate fields: this is **Track B + deep_recovery**, not "recovery" in general.

## Why this question (two lines)

It is the one restoration need whose only card (`cards/B02_readthrough_class`) is an abstention that names a single missing datum (the allele enumeration), and the answer decides whether read-through stays an open lever, is conditioned on an NMD assay, or is dropped from the reference-genotype portfolio. Gene addition, splice correction, missense rescue and endogenous boost each already have a card with real content; this is the one that could be moved by a computation that costs nothing.

## 1. Premise to verify

P: "At least some of the nonsense alleles recorded for WWOX are plausibly amenable to translational read-through, so a read-through agent is a candidate lever for them." The census flags five alleles as "READ-THROUGH candidate" (`analysis/woree_therapeutic_class_census_20260921.md`): p.(Arg54*), p.(Trp44*), p.(Arg264*), p.(Gln191*), p.Trp218*. The flag is a repository remark, not a measurement.

Three separable conditions must hold for P: (a) the PTC-bearing transcript persists (escapes NMD) so there is a template; (b) the stop codon and its +4 context are permissive and the amino acid inserted at the stop is tolerated; (c) the cell type that matters (neurons, in a developing brain) can be reached by a read-through agent and the restored full-length protein is functional. This note tests (a) and (b) from sequence, and brings published evidence on (c) from other diseases. None is a WWOX measurement.

## 2. WWOX knowledge used, and its depth

| What | Source | Depth |
|---|---|---|
| No WWOX allele of any class has been assayed with an NMD inhibitor or by NMD-discriminating quantification; no read-through experiment on WWOX | `analysis/wwox_nmd_assay_census_20260922.md` (§1.1-1.3 and the counts table) | passages (first ~120 lines of 40 kB), repository analysis, not re-run |
| NMD premise withdrawn for the splice-acceptor allele; exon-9 architecture; "NEVER TESTED"; the Arg264Ter fetus with brain tissue and no RNA extracted | `research/commit_candidates/CC-20260922-NMD-PREMISE-WITHDRAWAL-01.md` | passages (first ~80 lines of 22 kB) |
| The five recorded nonsense alleles, patients and "no NMD assay" | `analysis/woree_therapeutic_class_census_20260921.md` rows 189-193; `analysis/ft116_cohort_triage_20260921.md` §6.1 | passages (grep context) |
| Davids 2019 (PMID 30362252), exon-6 microdeletion: abstract says NMD; the body says "not expressed or were degraded" | abstract read by me (PubMed); body statement via `analysis/nmd_adjudication_reference_allele_20260922.md` L1-L2 | abstract (mine) + repository quotation of the body |
| 32 single-nucleotide nonsense alleles | `analysis/data/WWOX_clinvar_all_variants.csv` (commit a2e0dd0f, sha256 09c8cbbb...884; ClinVar snapshot date not recorded in the repository) | the whole table was parsed by script; classifications and review status are ClinVar's, not re-assessed |
| Transcript and protein geometry | NM_016373.4 GenBank record (NCBI efetch, sha256 2ead8d3e...3b), exons 1..9 with c.1056/c.1057 the last junction; UniProt Q9NZC7 features (WW1 16-49, WW2 57-90, NLS 50-55, region 125-414, active site Tyr293) | whole record parsed; the script asserts that every ClinVar reference nucleotide matches the RefSeq sequence |

Distinctions kept: protein abundance (Q230P fibroblast line, not detected, one donor, `needs.json` ENDOGENOUS-BOOST O2) versus function (not measured for any nonsense allele) versus cellular rescue (no WWOX read-through experiment) versus wider outcomes (none). Nothing here is transferred between variants: the reference genotype class (destabilising SDR missense plus the canonical splice-acceptor allele) carries no premature stop in the stated analysis, so read-through is **not a lever for that class at all**.

## 3. Result of the enumeration (prediction from sequence only)

`ptc_alleles.tsv`, produced by `ptc_enumeration.py` (offline; command in its docstring). 32 single-nucleotide nonsense alleles in the committed ClinVar snapshot (frameshifts, deletions and Ter415 extension variants are excluded by construction).

* **NMD position (50-55 nt rule, last junction c.1056/c.1057): 23 predicted NMD-sensitive** (exons 1-8, more than 55 nt upstream), **1 borderline** (p.Trp335*, c.1005G>A, 51 nt), **8 predicted to escape** (exon 9: c.1057C>T, c.1060C>T, c.1114G>T, c.1165C>T, c.1171G>T, c.1193G>A, c.1204G>T, c.1216C>T). All five alleles the census flags as read-through candidates are in the NMD-sensitive group (Trp218* computed by hand: TGG codon, 402 nt upstream). The rule is a prediction; it has errors in both directions, and WWOX has never been tested (census).
* **Context:** stop codons UAA 10, UAG 12, UGA 10 (counts from the table, summed over contexts). The context usually reported as most permissive for UGA, a following C, is **absent from all 32** (UGA is followed by G in 6 alleles, U in 3, A in 1; the only +4 C cases are UAG-C p.Gln191* and UAA-C p.Gln353*). The ranking of tetranucleotide contexts is from literature I did not read beyond the abstract (PMID 10917599: context determines aminoglycoside susceptibility; PMID 26176195: efficiency depends on codon identity and context; PMID 36400713 title: "U UGA C ... favorable context to ELX-02"), so the statement is weak.
* **Amino acid inserted:** ataluren read-through is reported to insert Gln/Lys/Tyr at UAA/UAG and Trp/Arg/Cys at UGA, by mispairing at codon positions 1 and 3 (PMID 27702906, abstract). In 19 of 32 alleles the original amino acid is both in that set and reachable through a position-1 or position-3 mismatch, so a wild-type residue is plausible; in 13 it is not (e.g. Trp44 for the UAG allele c.131G>A, a position-2 change; the Gly, Glu and Ser stops). For the recorded candidates: Arg54* (CGA to UGA, Arg possible), Arg264* (CGA to UGA, Arg possible), Gln191* (CAG to UAG, Gln possible), Trp44*: UGA allele c.132G>A yes, UAG allele c.131G>A no (ClinVar holds both; the census records c.131G>A). A plausible residue is not evidence of function, and the insertion bias is from reporter systems.
* **Domain:** exon 2 stops hit WW1 (Trp44 is a WW1 residue); stops before codon 125 remove the SDR region entirely; stops at 353-406 leave Tyr293 and most of the SDR region intact, so a C-terminal truncation may or may not be a loss of function. Of the eight NMD-escape alleles, three are Pathogenic or Pathogenic/Likely pathogenic in ClinVar, three are uncertain and two have conflicting classifications; c.1057C>T is also the first nucleotide of exon 9, next to the acceptor lesion of the reference genotype, and a splicing effect was not assessed.
* **N-terminal escape hypothesis (not tested):** for exon 2-3 alleles the next in-frame Met after codon 54 is codon 114 (loses both WW domains). A downstream-start NMD escape has been shown for N-terminal CFTR stops (PMID 36143233, abstract). For WWOX this is a question, not a finding.

## 4. Counter-evidence (all from other diseases; abstract depth unless stated)

* Read-through needs a template: in cystic fibrosis patients carrying W1282X the response to gentamicin was found only where nonsense transcript levels were higher; lowering NMD raised transcript and response (PMID 17290305). Combining read-through drugs with NMD inhibitors was synergistic on nonsense mRNA levels in DMD cells (PMID 37145099); NMD inhibitor candidates from a CFTR screen (CC-115, samotolisib, elimusertib; PMID 42772852) are kinase inhibitors with unassessed transcriptome-wide effects, and none is a WWOX-relevant or paediatric proposal.
* Clinical record of the lead agent: ataluren did not meet its primary endpoint in the phase 3 DMD trial (6MWD difference 13.0 m, 95% CI -7.4 to 33.4, p=0.213; PMID 28728956), and a placebo-controlled crossover in nonsense-variant Dravet syndrome and CDKL5 deficiency (n=15, 12 weeks, the nearest nonsense DEE precedent) found no effect on seizures, cognition, motor or behaviour (PMID 33538404). Both are small or short or use a different endpoint than a developing-brain recovery would; they are the real evidence, not a reason to exclude other agents.
* Mechanism is disputed or agent-specific: in a purified system ataluren acts by inhibiting release-factor activity while G418 acts by near-cognate mispairing (PMID 33414181), against the near-cognate-tRNA account of PMID 27702906. Aminoglycosides in brain: G418 reached full-length MeCP2 in the mouse brain only after intraventricular injection in a Rett R294X model (PMID 32469049); this is a route problem, not a dose proposal.
* Positive neuro precedents exist and are not WWOX evidence: ataluren restored SMC1A protein in nonsense DEE85 patient-derived lines (PMID 41770211), small-molecule read-through restored ATM production in a nonsense Atm mouse model (PMID 34723800; the abstract states restoration of production only), aminoglycosides read through CDKL5 nonsense mutations with slight kinase restoration (PMID 31232219, title only).

## 5. Pharmacology (keyless sources)

* **ChEMBL REST** (queried 2026-10-28): ataluren CHEMBL256997, max phase 4, first approval 2014, mechanism "80S ribosome modulator" (action MODULATOR) on CHEMBL3987582 (human 80S ribosome, a protein-nucleic-acid complex), mechanism references: EMA product information and PMIDs 25193627, 27702906, 27791186; indications Duchenne (4), cystic fibrosis (3), epilepsy (2, NCT02758626 = the CDKL5/Dravet trial above), haemophilia A/B (2), aniridia (2). Amlexanox CHEMBL1096: curated mechanism is PDE4 inhibition only (its read-through use is not a ChEMBL mechanism). Gentamicin CHEMBL6067485: no mechanism row, no drug warning rows retrieved. No drug-warning rows for ataluren were returned. ClinicalTrials.gov (keyless API): ataluren studies include terminated and completed trials in CF, DMD, aniridia and the Dravet/CDKL5 study.
* **Guide to Pharmacology** public download (ligands.csv and interactions.csv, version 2026.3.1): ligands ataluren (7341), ELX-02 (10944), gentamicin, paromomycin, amlexanox exist; **ataluren, ELX-02 and paromomycin have no interaction rows**; amlexanox has IKBKE and TBK1 inhibition rows; gentamicin has TRPA1 (mouse) and TRPV5 rows. The GtoPdb web-service route needs an API key and was not used.
* **DGIdb cache (catalogue)**: ataluren has a DGIdb-only record with 83 target rows, including DMD "dystrophin nonsense mutant" (TTD) and RPS9 (ChEMBL); read as drug-to-ribosome and disease-annotation claims, not WWOX evidence.
* **Result:** the catalogue cannot reach any read-through agent from this need, because the need lists only WWOX as a target, and no catalogue record has WWOX as a target. This is a loop gap of the same kind as the missing GCN2 target in iteration 3, not a negative. The only catalogue-reachable agents sit on the ribosome, and they lack GtoPdb interactions.

## 6. Decision: reasoned abstention, with three consequences

No card is written (no drug assertion on a WWOX system exists to put on one, and the evidence above gives no compound that deserves a packet). Disposition for the lead queue: **insufficient, with a narrowed missing datum**.

1. **What changes in the B02 abstention.** The missing datum "the enumeration" is now supplied (as a prediction): 32 alleles, 23 NMD-sensitive, 1 borderline, 8 predicted escape; the five alleles flagged as read-through candidates are all in the NMD-sensitive group. The new missing datum is a **transcript-level NMD measurement on a recorded nonsense allele** (with and without an NMD-discriminating arm), because until it exists the read-through "candidate" flag has nothing under it for exons 1-8. Order of assay value: p.Arg264* (the allele the triage says could reach three reported patients, conditional on cohort overlap; UGA-U context, Arg possible) and p.Arg54*/p.Trp44* (UGA) as the NMD-sensitive test cases; p.Gln353* (UAA-C, predicted escape, the best context in the table) as the escape test case.
2. **Reference-genotype portfolio.** Read-through has no applicable target in the reference genotype class (a missense allele plus an exon-9 acceptor splice allele: no stop codon). This is an inference from the class composition, not a finding that read-through fails: read-through has never been tested for WWOX. Caveat from the independent verification: the unmeasured intron-8 retention outcome predicted for the splice allele would create a stop codon, so even this inference rests on an unmeasured prediction.
3. **Catalogue loop.** Add the translation-termination and NMD machinery as targets of the need so the forward search can reach read-through and NMD-inhibitor agents (ready-to-apply text below). Not applied here: it would force a coverage regeneration for an abstention.

**Reopening conditions:** a measured PTC transcript level (not an inference from a western) in patient-derived cells for any recorded nonsense allele; or a WWOX read-through experiment of any kind; or a nonsense-DEE read-through trial with a positive seizure or developmental endpoint.

**Closing (for the portfolio) if:** the transcript assay shows NMD-sensitive alleles at undetectable mRNA and an NMD-escape allele shows a stable truncated protein with retained function.

## Ready-to-apply text (not applied)

`coverage/lead_dispositions.json`, new entry (id to be assigned by the integrator):

```json
{
 "id": "LD-006",
 "need": "NEED-WWOX-PTC-READTHROUGH",
 "subject": "premature-stop read-through agents (ataluren, aminoglycosides, ELX-02) for WWOX nonsense alleles",
 "catalogue_ids": ["CAT:CHEMBL256997"],
 "decision": "insufficient",
 "why": "The need lists only WWOX as a target, so the catalogue returns no read-through agent through it; agents sit on the ribosome (ChEMBL: ataluren 80S ribosome modulator). Sequence enumeration of 32 ClinVar nonsense alleles: 23 predicted NMD-sensitive, 1 borderline, 8 predicted escape; all five census 'candidate' alleles are NMD-sensitive, and no allele has the UGA-C context. No WWOX read-through or NMD measurement exists. Closest nonsense-DEE trial (ataluren in CDKL5/Dravet, n=15) was negative.",
 "reopening_condition": "a measured PTC transcript level in patient-derived cells for a recorded WWOX nonsense allele, or any WWOX read-through experiment",
 "next_experiment": "transcript-level NMD assay (NMD-discriminating arm) on a patient-derived line carrying p.Arg264* or p.Arg54*, and on a predicted-escape allele such as p.Gln353*",
 "owner": "Scientist (measurement; not done here)",
 "card": null,
 "record": "ptc_readthrough_it4_e1a_20261028/README.md"
}
```

`needs/needs.json`, `NEED-WWOX-PTC-READTHROUGH.targets`, add (role text "pathway_member" unless the integrator decides otherwise; HGNC ids to be checked against the live HGNC service as for the other targets): `GSPT1` (eRF3a), `ETF1` (eRF1), `SMG1`, `UPF1`; and a note that the 80S ribosome (ChEMBL target CHEMBL3987582) is the ChEMBL target of ataluren and is not a gene symbol. Add `inferred`: "Whether a recorded nonsense allele escapes NMD is predicted by position (23 sensitive, 1 borderline, 8 escape of 32 ClinVar alleles) and not measured."

## Depth of every reading

* PubMed abstracts only (not full text): 30362252, 28728956, 27702906, 33414181, 17290305, 37145099, 42772852, 36143233, 33538404, 32469049, 34723800, 41770211, 10917599, 26176195, 36866921 (retrieved, not used: the retrieved text was cut before its results), 36400713 (title only), 31232219 (title only), 25193627 and 27791186 (identifiers only).
* ClinicalTrials.gov structured record for NCT02758626 read for status and outcome titles; its posted numeric results were seen but not interpreted (the registry's own value lines are unreliable without the table headings).
* Repository documents: passages, as listed in section 2.
* No full text, no supplement and no figure was read; no FULLTEXT_READ_RECEIPT is warranted and none is staged. Europe PMC returned HTTP 503 during the session and was not used.

## What was not verified

* The ClinVar table is a repository snapshot with no recorded date; allele classifications may have changed.
* The 50-55 nt rule, the context ranking and the insertion set are from the literature read at abstract depth or from general knowledge, and no NMD-predictor tool was run.
* Current regulatory status of ataluren in the EU or elsewhere was not verified (the ChEMBL mechanism reference points at EMA product information; a 2021 abstract says approved by the EMA).
* The 19-of-32 "wild-type residue plausible" count uses the rule "original amino acid in the reported set and a mismatch at codon position 1 or 3" and ignores tRNA abundance and context.


## Independent verification (2026-10-28)

An independent verifier recomputed the enumeration from NM_016373.4 and the repository's ClinVar export without reading this note: 32 alleles, 23 NMD-sensitive, 1 borderline (p.Trp335*, 51 nt from the last junction: borderline at a 55 nt cutoff, sensitive at 50), 8 escaping, all in exon 9; the five census candidate alleles are NMD-sensitive; no UGA with +4 C; the 19 of 32 'ataluren-insertable' figure is definition-dependent (22 if W, R, C, Q, Y and K are pooled, 8 for W, R and C alone). Minor: five of the eight exon-9 alleles are not established pathogenic in ClinVar; the census writes p.Arg54* as c.160G>T whereas RefSeq has C at c.160 (c.160C>T). Report: `locator_audits/2026-10-28_it4_ptc_enumeration_independent_verification.md`.
