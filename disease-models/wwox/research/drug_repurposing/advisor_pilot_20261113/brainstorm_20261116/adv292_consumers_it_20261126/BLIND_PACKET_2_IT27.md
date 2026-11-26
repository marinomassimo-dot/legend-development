# Blind check (second round) of repaired sentences against three 2024-2025 papers (hypothesis level; not medical advice)

Papers (reference class, none about the gene of the record that will carry the sentences): Wang 2024 (PMID 39216838,
GABRA1 variants), Shah 2025 (PMID 40485335, GAT-1 variants), Fu 2025 (PMID 41178115, GABRA1 variants). Files in this
folder: `*_text.txt` (article text), `*_supp*` (supplements, text and PDF; use `pdftoppm` to view pages), `fig_*/`
(figures). Work only from these files. No network. Read no other file on the machine. Crops may use ImageMagick
`convert`; scripts run with `python3 -I` and live in this folder.

For every sentence: SUPPORTED, ADD (true; a missing condition would help but no reader is misled), MUST CHANGE (some part
false, or true only under an unstated condition that changes the inference; give the exact words and the smallest
correction), or UNSETTLED. Check every number, unit, count, direction, species, material, assay, panel and quotation.
Rates over variants or ligands must be counted from the whole table, not from examples. The unit of replication is stated
by you where the sentence gives an n. Statements about "this repository" or "the three other papers of the row" are not
yours to judge.

## W1 (Wang 2024)
"Two benzodiazepine-site GABA-A positive modulators, hispidulin and TP003 (of 10 receptor ligands screened at 10
micromolar for 24 h on total alpha1 protein of three variants in HEK293T, four raised it in at least one variant),
raised variant surface protein and GABA-evoked current in HEK293T for most of eight alpha1 variants (hispidulin
significant for current in 8 of 8, TP003 in 6 of 8; not D219N and R214C); in one heterozygous G251D knock-in iPSC line
(35 to 75 neurons per condition, at least 3 differentiations), surface subunit fluorescence rose, proximity-ligation
puncta rose for gamma2, BiP, calnexin and LMAN1, fell for Grp94 and were unchanged for SEL1L, and no current was
measured (research compounds, not approved drugs)."

## W2 (Wang 2024)
"ligands known to bind GABA-A receptors (most described as benzodiazepine-site; the paper does not classify the sites of
the 6 that did not raise protein, and GABA itself, the orthosteric agonist, was among the 10 screened; binding to the
variants is presumed from the literature, not measured here)."

## S1 (Shah 2025)
"In HEK293 cells 4-phenylbutyrate and glycerol increased the wild-type hGAT-1 mature band (blots not quantified) and
4-phenylbutyrate increased wild-type uptake (Fig 3A); in Drosophila astrocytes neither compound visibly changed wild-type
hGAT-1 expression (single-section images, not quantified, Fig 6B), while 4-phenylbutyrate, but not glycerol, raised the
retained variant G443V about 14-fold (Fig 6I, at least 10 brains per condition). The cell-line effect on wild-type
protein is not shown to be variant-specific; the in vivo wild-type reading is qualitative."

## S2 (Shah 2025)
"4-phenylbutyrate (10 millimolar in HEK293 for 24 h; 1 millimolar in fly food for 48 h) rescued the fully ER-retained
G443V but not the partly trafficked G443D; glycerol 10 percent rescued G443D uptake and mature band in HEK293 (Fig 3B,
4D-E) and G443V uptake in HEK293 only (Fig 3C); the rescue is partial (treated variants reach about 6 to 8 percent of
untreated wild-type uptake in the single-concentration screen); uptake was not measured in flies, where glycerol and
4-phenylbutyrate both gave presynaptic G443V in imaging and glycerol's effect on G443V seizures was not significant;
wild-type uptake was raised in HEK293 (clearly by 4-phenylbutyrate), wild-type fly expression was not. Bile-acid
chaperones are not tested in this paper."

## F2 (Fu 2025)
"IXA554 and IXA105 were tested only to 10 micromolar \"due to the drug toxicity to cells at 25 micromolar\" (no viability
data shown); apart from alpha1 and the IRE1/XBP1s read-outs (XBP1s protein, five target mRNAs, splicing reporter), the
only stress marker read for all three compounds was CHOP (D219N cells, Fig S1E); no cell-viability or off-target assay was
run."
