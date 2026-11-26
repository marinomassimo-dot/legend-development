# Blind check of proposed sentences against three 2024-2025 papers (hypothesis level; not medical advice)

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
micromolar for 24 h on total alpha1 protein of three variants in HEK293T: four raised it in at least one variant, one
lowered it in one variant), raised variant surface protein and GABA-evoked current in HEK293T for most of eight alpha1
variants (hispidulin significant for current in 8 of 8, TP003 in 6 of 8; not D219N and R214C); in one heterozygous G251D
knock-in iPSC line, surface subunit fluorescence and proximity-ligation puncta rose and no current was measured (research
compounds, not approved drugs)."

## W2 (Wang 2024; a clause about "ligands that bind the client")
"ligands known to bind the benzodiazepine site of GABA-A receptors (binding to the variants presumed from the literature,
not measured in this paper; 6 of 10 screened ligands did not raise protein)."

## S1 (Shah 2025)
"In HEK293 cells 4-phenylbutyrate and glycerol increased the wild-type hGAT-1 mature band (blots not quantified) and
4-phenylbutyrate increased wild-type uptake (Fig 3A); in Drosophila astrocytes neither changed wild-type hGAT-1
expression (Fig 6B) while the retained variant G443V rose about 14-fold (Fig 6I). The cell-line effect on wild-type
protein is not shown to be variant-specific; in vivo it was variant-selective in this paper."

## S2 (Shah 2025)
"4-phenylbutyrate (10 millimolar in HEK293 for 24 h; 1 millimolar in fly food for 48 h) rescued the fully ER-retained
G443V but not the partly trafficked G443D; glycerol 10 percent rescued G443D uptake and mature band in HEK293 (Fig 3B,
4D-E) and G443V uptake in HEK293 only (Fig 3C); wild-type uptake was raised in HEK293 (clearly by 4-phenylbutyrate),
wild-type fly expression was not." (Also part of S2: "Bile-acid chaperones are not in this paper.")

## F1 (Fu 2025; additions to a sentence about two compound series raising variant GABA-A current)
"current was measured for D219N (100 micromolar GABA, n = 8) and G251D (1 mM GABA, n = 8), not P260L; unchanged GABRA1
mRNA was shown for D219N only (12 h); in the one heterozygous G251D iPSC line only IXA62 and IXA554 were tested and the
read-outs are surface alpha1, beta2/3 and gamma2 fluorescence and proximity ligation, no current; the G251D surface
biotinylation bar for IXA105 carries no significance mark (Fig 5C) although the text gives 2.3-fold."

## F2 (Fu 2025; transfer limits)
"IXA554 and IXA105 were tested only to 10 micromolar \"due to the drug toxicity to cells at 25 micromolar\" (no viability
data shown), and only alpha1 (wild type and variants) and CHOP were read."
