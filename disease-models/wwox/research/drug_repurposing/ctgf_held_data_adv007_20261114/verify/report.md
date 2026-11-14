# V-ADV007 report (blind verifier), placed here by the Orchestrator

The verifier's Write of `verify/report.md` was refused by the harness ("Subagents should return findings as text"). This file is its returned report, copied unchanged in substance from the hand-back; the orchestrator added only this header and the final read-back line. The verifier's own files are `stage_a.md`, `verdicts.tsv` (32 claims: 26 CONFIRMED, 3 NARROWED, 3 UNVERIFIABLE, 0 CONTRADICTED) and `rerun1/`, `rerun2/` (all 9 output files byte-identical to `output/` as it stood then).

**Verdict (verifier): (b) on both legs, with one precise statement about (c).**
- The shipped flags were never computed: `composition_class.tsv` line 198 (CCN2) has blank log2fc and rho; the generator looks the gene up under the authors' older symbol CTGF, so every 0 in that row is a default. The same holds for all 15 renamed genes.
- Computed properly, the rule would still give 0, for the wrong reason: Spearman rho against log10 day over 62 samples is -0.009; the time course is non-monotone (within-line slope -0.69 per log10 day, bootstrap -1.83 to -0.30; day-bin means +1.61, -0.36, -1.03, -0.21, +0.91; a 15-week organoid sits near the trough; for day 60 and later the slope is positive). The between-line t interval (-3.11 to +0.46) includes zero and within-line R2 is 0.04.
- Maturation and composition are not excluded as the cause of the rise: observed +1.15 on log2(CPM+1); single markers predict a median +0.26 (range -0.31 to +1.53; NES and VIM each predict most or all); a composite progenitor-minus-neuronal score predicts +1.21 (calibration R2 0.61); a 12-marker regression +1.22 (R2 0.84, overfit risk).
- Direction is not consistent across the held tables (organoid up; P17 null allele down, N allele up, S allele and cortex not separated; P47T mixed and not significant; snRNA up in one pool with a composition shift; CAGE uninformative).

**Where the producer was stronger than the data:** the coupling summary (median 0.26) read as "maturation explains a minority" while a combined score projects the whole rise; the proxy transcript was called unique only inside a 85-100 percent window (three rows qualify at 70-105 percent) and overstates H_N (centred +1.28 against the committed +1.111), so the committed value is quoted; "360; 199" are the gene's line positions in the two lists, not counts. **Weaker or omitted:** no CAGE row; the 4 v 2 exact permutation floor (two-sided 0.13) not stated beside DESeq2 padj 0.007.

**What could change the verdict:** a replicated organoid contrast with more than 2 WT, or confirmation that the 4 KO libraries are separate clones; the Ensembl cDNA map so the P17 gene sums can be rebuilt; cluster-resolved snRNA with replicate pools; cell-state markers measured in the same organoid libraries.

**Could not check (UNVERIFIABLE):** the committed gene-level P17 numbers; leave-one-line-out slopes (re-run only); the astro and "neither" counts of the snRNA overlap; clone independence of the KO organoids; the Ensembl annotation of the proxy transcript; the CAGE row (its own reading).

Note the verifier's own coupling numbers agree with the producer's because both import the committed estimators: this shows the run reproduces, not that the estimator is valid.

Dispatch: asked sonnet, effort high. Read back by `session_model_census.py` from the transcript: claude-sonnet-5-5 x44 turns, effort high x44 (the verifier's last line said "low"; the transcript read-back governs). 44 turns, output 51,210 tokens, cache read 3,111,079, cache written 125,260.
