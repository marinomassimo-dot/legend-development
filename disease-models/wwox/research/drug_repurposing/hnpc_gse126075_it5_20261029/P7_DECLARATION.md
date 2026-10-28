# P7 declaration (scientist-c, 2026-10-28): same sets, second system, committed before the organoid run

Purpose: put the P6 set definitions (hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv, the 'symbol' column) next to the WWOX-knockout
organoid (GSE156243: 4 knockout, 2 wild-type libraries, week 15, Salmon gene counts, local file), computed WITH THE SAME METHOD as P6 so
that a set shift is read the same way in both: per-arm mean CPM (library-size normalised on all genes), R = log2((KO+0.5)/(WT+0.5)),
centred by the median R of the measurable universe (estimated count at least 10 in both arms; here the mean count per arm), mean R per
set against 10,000 expression-decile-matched random sets (seed 20261029). The universe is the organoid's own, never the CAGE gene table.
Replicates are never pooled with P6 and no statistic combines the two systems. This is a descriptive re-expression of an existing
dataset, not an independent validation of anything; four versus two libraries allows a minimum single-gene permutation p of 1/15.
Sets: ISR_targets, UPR_branches, OXPHOS_nuclear, Mito_translation, Mito_import, Glycolysis_lactate, PDK_family, the markers sets,
and the two unrelated control sets. Prediction (stated before the run, from the repository's earlier organoid results): ISR targets lower,
glycolysis set higher, OXPHOS flat. Anything else is reported as found. Reading rule: two systems are called CONCORDANT for a set only if
the sign agrees AND each system's own set mean lies outside its matched null; DISCORDANT if the signs differ and each lies outside;
otherwise "one system only" or "not distinguishable". A concordance never goes beyond transcript level.
