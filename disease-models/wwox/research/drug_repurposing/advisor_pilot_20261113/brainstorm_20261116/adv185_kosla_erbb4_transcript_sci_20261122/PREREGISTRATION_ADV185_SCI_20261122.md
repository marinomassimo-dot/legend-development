# ADV-185 pre-registration: does the held material of Kosla et al. 2019 (PMID 31543760; GEO GSE126075) give a per-gene ERBB4 comparison, shScrambled against shWWOX, with direction, size, replicates and unit? (SCI successor Z, 2026-11-22; hypothesis level; a transcript comparison cannot test the post-translational stabilisation arm; no compound, direction, ranking, candidate or NRG1 handle; no WWOX claim beyond what the source measures; no author contact; no e-mail address to any service; not medical advice)

Fixed BEFORE any per-gene value (the GEO TPM matrix, a GSEA table line or a figure panel for ERBB4) was opened.

## What had been seen when this was written
* ADV-185's text and the audit it points to (`analysis/hnpc_differentiation_audit_20260920.md`, lines 106 to 111 and 245 to 247): a quotation from the paper's Results that names ERBB4 and NRG1 in the "hNPC/shScrambled" leading edge of a lineage-commitment gene set and not in the "hNPC/sh[WWOX]" edge; the audit calls it a directional contrast. A leading-edge membership is a set statement, not an abundance.
* My own ADV-178 Part B read of the same paper (2026-11-22): the expression platform is CAGE (promoter-level 5' tag counts, TPM, CAGEr; deposited as GSE126075); the GEO record lists 4 samples for native and silenced WWOX before and after differentiation, i.e. one sample per genotype per stage, with no replicate number in the text; the paper's differential-expression threshold is |log2FC| > 1 with p < 0.05; Supplementary Tables 1 to 3 were searched by text for ITGB1 and CDH2 only (not for ERBB4); WWOX knockdown was verified by a single three-lane Western blot.
* Step 0 (reported to ADV): the series suppl/ directory of GEO lists `GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz` (263 KB) and a TSS-level file (897 KB), reachable by a plain HTTPS request (listing only; nothing downloaded or opened).
* Not seen: the sample-to-genotype mapping of the four GEO samples beyond "native and silenced before and after differentiation", any ERBB4, NRG1 or WWOX TPM, any rank-metric value in the GSEA tables, any figure panel for the lineage-commitment set.

## Which quantity the premise needs (decided before reading a number)
Three quantities are kept apart: (1) SET MEMBERSHIP (ERBB4 in a GSEA leading edge: a rank-position statement for a gene set, direction only through the ranking metric, no size); (2) TRANSCRIPT FOLD (ERBB4 TPM in shWWOX against shScrambled, per stage); (3) PROTEIN LEVEL (full-length JMa ErbB4). The stabilisation arm of the L result (less ErbB4 without WWOX) is post-translational and needs (3). A transcript fold (2) can only show whether ERBB4 is also lower at RNA level without WWOX (a second, independent route to "less ErbB4 in WWOX-deficient neural precursors") or unchanged or higher (premise stays unmeasured at protein level). Membership (1) is not an input to either.

## Readings (fixed)
Stage compared first: undifferentiated progenitors (the neural-precursor question); the differentiated-neuron pair is read second and reported separately. Floor: a comparison is interpretable only if the higher of the two TPM values is at least 1 TPM. Size: |log2 fold| of 1 or more, the paper's own threshold, is called a difference in size; smaller is "within the paper's threshold". There is one sample per cell, so no variance and no test can be computed from the deposit; every fold is a point estimate.
* **T-down:** ERBB4 TPM lower in shWWOX by a log2 fold of at most -1 in the progenitor pair, floor met. Reading: a descriptive RNA-level lead toward "less ErbB4 without WWOX", one sample per cell, not a measured protein premise.
* **T-flat:** within the paper's threshold, floor met: the transcript does not support a second route; protein premise unmeasured.
* **T-up:** log2 fold of at least +1: no RNA-level support (and nothing for or against stabilisation, which is post-translational).
* **T-floor:** both values below 1 TPM, or the gene absent from the file: no interpretable comparison.
* **Positive and identity controls (fixed now):** WWOX itself must be lower in the shWWOX samples than in their stage-matched scrambled samples (otherwise sample labels or the knockdown are in doubt and no ERBB4 reading is made); the neural-progenitor and neuronal marker pattern (for example SOX2, NES, PAX6 against MAP2, TUBB3, DCX) must differ between the two stages in the expected direction (identity of the stage). The sample-to-genotype mapping is taken from the GEO sample titles, not guessed.

## Exits (fixed)
* **KEEP:** a per-gene ERBB4 comparison with direction, size and the replicate structure needed for inference (more than one sample per cell, or a variance in a deposit). Not expected: the record lists one sample per genotype per stage.
* **NARROW:** a point fold exists (floor met, controls pass) but with one sample per cell and no variance: reported as a descriptive transcript lead with its direction, size and the three quantities kept apart.
* **CLOSE:** floor not met, controls fail, the deposit cannot be read, or the audit's quotation is the only source; with the precise reason and the minimal measurement needed (full-length JMa ErbB4 protein plus RNA in WWOX-deficient neural precursors or organoids against control, replicated).
* Also stated whatever the outcome: the comparison is a knockdown in an H9-derived line with a partial knockdown shown by one blot, not the DEE genotype class; it does not test stabilisation.

## My expectation, stated so the reading can refute it
Moderate confidence in NARROW or CLOSE. ERBB4 is mostly an interneuron and later-stage gene and may sit near or below 1 TPM in H9 progenitors; if so, T-floor and CLOSE. If it is above the floor, a lower value in shWWOX would be the direction the leading-edge quotation suggests; I do not expect a size I could call robust from one sample per cell.

## Checks (fixed)
Sample mapping from GEO titles; WWOX control; stage-identity genes; ERBB4, NRG1, ERBB2, ERBB3 values in all four samples; the same genes in the TSS-level file (promoter-level: which ERBB4 promoters carry the counts; a gene-level TPM may hide a promoter switch); the GSEA tables of the supplement searched for ERBB4 and for any per-gene rank-metric value; the audit's quotation checked against the paper's Results sentence.

## Consumers
ADV (result and path, KEEP, NARROW or CLOSE). IT only if a concrete consumer delta exists (the IT59-Q01 clause already carries the stabilisation arm as untested; a transcript lead would add at most one half-sentence).
