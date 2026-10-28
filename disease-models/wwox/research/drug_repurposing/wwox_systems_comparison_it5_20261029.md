# WWOX-deficient systems compared: ISR, mitochondria, glycolysis/lactate, progenitor programmes (IT5 P6 residue and P7)

Scientist-c, 2026-10-28 (file dated for the mandate day 2026-10-29). Exploratory. Transcript level except where a row says otherwise. Not medical
advice. Matrix: wwox_systems_comparison_it5_20261029_matrix.tsv (42 rows, programme x system). P7 declaration (committed before the run):
hnpc_gse126075_it5_20261029/P7_DECLARATION.md. Scripts and outputs: hnpc_gse126075_it5_20261029/p7_organoid_same_sets.py, p7_organoid_set_summary.tsv,
p7_organoid_key_genes.tsv, p7_params.json. No LINCS analysis was repeated and no pipeline was reopened.

## 0. Rules that govern this comparison
- Replicates are never pooled across studies; no combined statistic exists here. Each system keeps its own universe of measurable genes (organoid
  RNA-seq 15,841 genes with mean count at least 10 per arm; CAGE hNPC 9,297 and neurons 8,477 genes with estimated tags at least 10 in both arms).
- The same method was applied to both datasets so a set is read the same way (per-arm library-normalised mean, log2 ratio, median-centred, expression-decile-matched
  random sets, 10,000 draws, seed 20261029); a set "outside the null" is a rank among matched random sets of ONE comparison, never a p value for WWOX.
- P6 has ONE library per arm (library totals recovered from the TSS table: control hNPC 51.0M tags, silenced 14.3M): every statement about the CAGE systems is descriptive. The organoid has 4 knockout vs 2 wild-type libraries (minimum single-gene
  permutation p 1/15). The two organoid analyses (earlier ones and this one) are re-analyses of the same libraries and are ONE system, not two.
- Concordance means: same sign AND each system outside its own matched null. It never goes beyond transcript; it is not flux, enzyme activity, protein or rescue.
- What differs and stays different: knockout (exon deletion; WWOX mRNA not lower, +0.42, so the transcript is not a knockout check there) versus knockdown of unquantified depth
  (hNPC: WWOX not lower in the CAGE tags; neurons about 3 to 4 fold lower on 21 versus 83 tags); 3D mixed-cell organoid, week 15, versus 2D clonal H9-derived progenitors
  and day-14 neurons; RNA-seq counts versus CAGE promoter sums with 9 to 61 percent of tags in the gene table; control possibly native in GSE126075; different laboratories and lines.

## 1. Residue (A): the sign of the GSEA tables of the paper (PMID 31543760, Data_Sheet_1)
What the tables print: Supplementary Table 2, "Enrichment in phenotype hNPC_WWOX_high": 44 rows, ALL with positive enrichment scores (first rows neural-crest differentiation
0.622, neural-crest migration 0.677). Supplementary Table 3, "Enrichment in phenotype hNPC_WWOX_del": 108 rows (counted row by row; the text says 109), ALL with negative enrichment scores
(for example GO_MITOCHONDRIAL_TRANSLATION size 98, -0.437, FDR q 0.119; mitochondrial RNA metabolic process -0.586, 0.110; protein targeting to mitochondrion -0.472, 0.179;
mitochondrial transport -0.384, 0.212; ribosome biogenesis -0.429, 0.055; smallest q 0.029). The column is the un-normalised "Enrichment score" (no NES is printed) and FDR q.
What the paper says: "44 for hNPC/shScrambled and 109 for hNPC/shWWOX (FDR < 0.25)"; Table 1 is headed "Top gene sets enriched in hNPC with native WWOX expression level"; and
"the gene sets were enriched in hNPC/shScrambled cells versus hNPC/shWWOX". The paper does not print the sign convention.
Adjudication: the two supplementary tables are the positive end (Table 2) and the negative end (Table 3) of one GSEA ranking; every row of the shWWOX table is negative and every row
of the control table positive, which is only possible under that convention. A minus sign in the "del" report therefore means the set is enriched at the silenced end, i.e. its genes
rank toward higher expression in shWWOX, NOT depleted in the silenced cells. needs.json O6 and O7 ("on the knockdown side") are right in substance. The dossier sentence "negative
enrichment, in the silenced line, of mitochondrial translation ..." is misleading because a reader takes it as depletion; the same line of that dossier carries the numbers correctly.
Corroboration, same deposit, therefore NOT independent: MRPL/MRPS genes are higher in shWWOX hNPC (+0.28 centred, outside null) and mitochondrial import genes +0.54.
Limit: the sign is derived from the GSEA convention and the paper's own sentences, not printed; the order of the phenotype labels in the run is not shown.

## 2. Programme by programme

| Programme | Organoid KO (4 v 2, RNA-seq) | shWWOX hNPC (n=1, CAGE) | shWWOX neurons (n=1, CAGE) | Verdict |
|---|---|---|---|---|
| ATF4 mRNA | flat (-0.23) | flat (-0.15) | sparse (6 vs 41 tags; below the 10-tag rule, centred about +2.5) | concordant in hNPC only, uninformative (ATF4 is translationally controlled) |
| ISR target set (12; ATF4, XBP1 excluded) | LOWER -0.33 (outside null); CHAC1 -0.76, TRIB3 -0.68, SESN2 -0.39 | HIGHER +0.64 (outside); CHAC1 +2.6, TRIB3 +1.2, SESN2 +1.0 | HIGHER +1.32 (outside) | OPPOSITE SIGNS from systems of very different design (organoid 4 v 2, CHAC1 t -11.6, TRIB3 -4.1, SESN2 -4.3: solid; hNPC n=1 and neuron rise composition-sensitive): UNRESOLVED. Only PSAT1 is up in all |
| UPR branches | flat | flat (rank 0.051) | flat | no signal in any system |
| OXPHOS nuclear transcripts (73) | -0.20 (outside) but the unrelated cytosolic-ribosome control is -0.26 | 0.00 (null edge); control -0.25 | -0.33 (outside); control -0.47 | not specific: moves with an unrelated abundant class; NOT comparable as a respiratory signal |
| Mitochondrial translation (MRPL/MRPS) | LOWER -0.15 (outside) | HIGHER +0.28 (outside) | -0.11 (inside) | DISCORDANT organoid versus hNPC |
| Mitochondrial import | -0.10 (inside) | HIGHER +0.54 (outside) | +0.12 (inside) | one system only |
| Glycolysis / lactate set (10) | HIGHER +0.53 (outside) on this 10-gene HIF-type set; on a 19-gene panel +0.35 (median +0.11), driven by HK2, SLC2A1, SLC2A3, SLC16A3, LDHA | HIGHER +0.46 (outside) on the 10-gene set; 19-gene panel +0.24 (rank 0.20, inside null) | +0.20 (null edge) | LDHA and a HIF-type glycolysis subset are up in both; the broader glycolysis panel is NOT distinguishable from chance in hNPC (hand-picked set; sensitivity A and stage-residual unstable at n=1) |
| PDK1 | LOWER -0.39 | LOWER -0.67 (+-0.45) | +0.44 (+-0.45) | lower in SIGN only in the two systems where measured; both inside the single-gene null (p about 0.30, 0.49); PDK set itself indistinguishable from chance. HIF1A mRNA flat in both (-0.27, -0.11) |
| Progenitor identity (radial-glia markers) | set-dependent: +0.38 on the 9-gene set only because NES (+1.28) and VIM (+0.83) are in it; the four canonical markers +0.11 (rank 0.52, inside null) | LOWER -1.17 (outside); on the four canonical markers -2.03 (robust); SOX2 -1.7, PAX6 -2.9, HES5 -3.1 | LOWER -0.50 (outside) | hNPC drop robust; organoid 'higher' set-dependent / not clearly different; baselines not comparable (week-15 3D mixture versus 2D line) |
| Neuronal pan markers | -0.48 on a 5-gene panel, -0.19 (rank 0.11, inside null) on a 10-gene panel: not clearly lower | lower, inside null (4 of 9 measurable) | LOWER -0.76 (outside; -0.58, rank 0.008 on the 10-gene panel) | lower in neurons only; not clearly lower in the organoid |
| Cell-cycle markers | flat | flat | flat | no signal in any system |
| Protein/phospho ISR, flux, lactate, ATP, OCR | none | none | none | measured in no human neural WWOX system; resazurin lower in hNPC (raw, not respiration); MEF flux shift to glycolysis (mouse, non-neural); fly lactate and Ldh up only with Abeta42, ATP flat |

Reading the maturity confound across systems: in the organoid the glycolytic and LDHA rise is as consistent with a less advanced tissue as with a metabolic change, because the genes fall with
culture time and the KO shows more progenitor markers. In shWWOX hNPC the same genes rise while progenitor markers FALL. A shared "less advanced tissue" explanation therefore does not
cover both systems; each is confounded by something different (organoid composition and maturity; hNPC line state, possible native control, n=1). That narrows, but does not remove, the maturity
objection to the glycolytic signal, and it cannot be turned into a statement about WWOX.

## 3. What this changes in the module (at least one question; four are changed or delimited)
1. ISR attenuation, DIRECTION and CONTEXT: UNRESOLVED. The need's own text said the only signed human datum points down (organoid). The organoid sign is solid for a 4 v 2 design (CHAC1 t -11.6, TRIB3 -4.1, SESN2 -4.3). The shRNA progenitor rise is one library per arm and rests on a handful of genes (CHAC1, TRIB3, PSAT1, SESN2, ATF5), and the neuron rise is composition-sensitive; the neuron ATF4 change (+1.99 to +2.5, 6 vs 41 tags) was set aside by the 10-tag rule. The honest statement is "opposite signs from systems of very different design: unresolved", not two equal data of opposite sign. Neither system measures ATF4 protein or eIF2alpha phosphorylation. Consequences: (a) no human transcript signal can be used as the sign of a "WWOX-dependent ISR change"; (b) a drug-signature reversal built on the organoid list inherits the organoid's ISR-lower sign and there is no basis to assume it generalises; (c) the next experiment is a matched protein/phospho plus target-mRNA measurement in one WWOX-deficient human neural system with a transduction-matched control, not another transcript re-analysis.
2. Mitochondrial respiration, TARGET. No OXPHOS-transcript deficit specific to WWOX loss exists in any system (the unrelated ribosomal control moves as far), and mitochondrial translation has opposite signs between the organoid and the hNPC library; transcripts therefore cannot rank complex I against the other respiratory targets. Only a flux readout (OCR/ECAR) in a human neural system can; the resazurin result stays a raw whole-cell reducing readout.
3. Glycolysis/lactate and the HIF1A-PDK-PDH chain, TARGET. LDHA and a HIF-type glycolysis subset (HK2, SLC2A1, SLC2A3, SLC16A3, LDHA) are up in the organoid, and LDHA and the hand-picked 10-gene HIF-type set are up in the hNPC library; the broader 19-gene glycolysis panel is not distinguishable from chance in hNPC (+0.24, rank 0.20) and the organoid mean is driven by five genes (median +0.11). PDK1 is lower in sign only in both systems and inside its single-gene null in both (p about 0.30 and 0.49), and HIF1A mRNA is flat in both (-0.27, -0.11), so the middle link of the chain (PDK1 raised) has no transcript support at PDK1 in either human neural system; the finding is the absence of support, not a demonstrated decrease. The functional meaning of the LDHA rise (lactate, ECAR) is unmeasured in human neural cells.
4. Differentiation programmes, CONTEXT: system-specific. The hNPC progenitor drop is robust (four canonical markers -2.03); the organoid "higher" is set-dependent (the 9-gene set +0.38 rests on NES and VIM; the four canonical markers +0.11, inside the null), and neuronal markers are not clearly lower in the organoid (-0.19 on a 10-gene panel, inside the null) though lower in the CAGE neurons (-0.58). A WWOX-dependent "arrested progenitor state" cannot be generalised from either system; the shWWOX hNPC library differs in state from its control (SOX2, PAX6, HES5 down), which confounds every metabolic comparison in it.
Not-comparable list (kept, not resolved): knockout versus partial knockdown; 3D mixture versus clonal 2D; RNA-seq versus CAGE; n=4/2 versus n=1; control native or scrambled.

## 4. Limitations
n=1 per arm in P6; four versus two in the organoid; WWOX not demonstrably lower in hNPC; possible native control; compositional CAGE libraries (9 percent of tags in the gene table for knockdown neurons);
sets are author-chosen and about a dozen were examined without correction; centring assumes most genes unchanged; Poisson intervals cover sampling noise only; the glycolysis and ISR sets overlap
(PGK1, PCK2) with metabolic programmes that respond to culture conditions; organoid sets use HGNC symbols and CAGE sets FANTOM5 names with an alias table; every result is transcript level.

## 5. Ready-to-apply ledger text (not applied; the Orchestrator owns the ledgers)
- Dossier PMID31543760, Part 2, "Surfaces read now", Supp Table 3 sentence: replace "include negative enrichment, in the silenced line, of mitochondrial translation, mitochondrial transport and
  protein targeting to mitochondrion" with "list, as enriched at the silenced (shWWOX) end of the ranking, mitochondrial translation, mitochondrial transport and protein targeting to mitochondrion (all 108 rows of Table 3
  carry negative scores, the negative-end convention of GSEA; all 44 rows of Table 2 are positive; the sign convention is not printed in the paper)".
- Discovery/dismissal ledger line (suggested): "GSE126075 holds one CAGE library per arm (4 libraries): the paper's DE and GSEA statistics cannot be re-derived from the deposit, and WWOX is not lower in the hNPC library at tag level
  (3.35 versus 2.90 TPM); descriptive P6 results (ISR targets higher, mito translation/import higher in hNPC) are discordant with the WWOX-knockout organoid (ISR targets lower, mito translation lower); not independent validation of anything."
- Hypothesis text (HIF1A-PDK-PDH chain): "PDK1 is not raised in either human neural WWOX-deficient transcript system held (organoid -0.39 and shWWOX hNPC -0.67 are lower in sign only, both inside the single-gene null; hNPC n=1 per arm); HIF1A mRNA is flat in both; LDHA and a HIF-type glycolysis subset are up in both, the broader glycolysis panel is not distinguishable from chance in hNPC; the middle link has no transcript support at PDK1."

## 6. Correction note
The P6 numbers used here follow the corrected P6 run (library totals recovered from the deposited TSS table, hNSC control 51,007,825 tags, after the Orchestrator's independent verification). Eight of the 11 measurable ISR members are higher at both CAGE stages (not five); ATF4 in neurons is sparse, not absent; neuron-stage values carry the global composition shift of about -1.3 log2; the control-arm identity (shScrambled versus untransduced) and the 9,427-gene equivalence to the paper's GSEA universe are paper-sourced and consistent with, not proven by, GEO. P6 remains n=1 per arm and descriptive.

## 7. Corrections after the independent P7 verification (2026-10-28)
The verification reproduced the arithmetic within about 0.05 and found no pooling. Softened as a result: organoid progenitor "higher" and neuronal "lower" (set-dependent), glycolysis "concordant" (hand-picked HIF-type 10-gene set; a 19-gene panel is inside the null in hNPC), PDK1 "concordant down" (sign only), ISR "two data of opposite sign" (now "unresolved"). Added: HIF1A mRNA flat in both; the neuron ATF4 change set aside by the 10-tag rule; an n_class column in the matrix so n=1 per arm cannot look equal to 4 v 2.
Label check: the deposit columns and sample titles named "WWOX_del" (GSM3590949 hNSC_WWOX_del, GSM3590951 neurons_WWOX_del) carry the sample characteristic "wwox expression: silenced" in GEO, so they are the shRNA-silenced arms; whether the control arms are shScrambled or untransduced is still not stated in GEO.
