You are an INDEPENDENT second reader (ADV-339 continuation, IT43, 2026-11-28). Hypothesis level; nothing here is medical advice.
Do NOT open: the claim registry records, anything under adv339_exclusivity_it_20261128/, deepdive_manifests, dossiers, or any earlier LEGEND reading of these papers. Use only the paper files listed below.
No answer is expected: each sentence may be right, partly right or wrong. Read the whole source paper(s) for each sentence (text, legends, methods, figures, held supplements).
Split each sentence into atoms (every measurement, arm/genotype assignment, number, and every exclusivity word such as only / none / all / solo / nessun / tutti). Grade each atom:
HOLDS (atom, including the exclusion, supported) | TOO_NARROW (another arm/line/preparation also carries what the sentence gives to one) | WRONG_ARM (named arm does not carry it) | NOT_SUPPORTED (value or statement not in source or contradicted) | UNSETTLED (held source cannot decide; say why) | NOT_GRADED (LEGEND process history).
For each atom give a locator: figure/panel/table/row/group, n, replicate unit, species, and the source words or value. Never label by position.
A negative ('no X in the paper') says where you searched and the search terms.
Write the table as TSV (columns: id, atom_no, atom_text, grade, locator, note) to the path below, then reply to IT with only the path and counts per grade. Hand back before seeing any IT table.
SCI: a sentence whose source text touches dosing or a regimen is marked BLOCKED-SKIP in grade, with no further handling.
Output: /home/desktop/legend-development/files/coordination/adv339_it43/sci_table.tsv

### S1 (CLAIM 035)
SENTENCE (verbatim, registry, Italian/English as written):
**B4 · What is measured.** no cell-derived GSK3β kinase assay is described: in cells GSK3β activity is inferred from Tau phosphorylation at S396 and S404, neurite outgrowth and the S9 blots of Fig 1b (the authors' headings state a regulation of kinase activity); kinase activity is measured only in vitro with purified components; the kinase assay and the microtubule assay are cell-free; the neuronal readout is SH-SY5Y cells treated with retinoic acid, not neurons of a Wwox-deficient animal.
CONTEXT (referent only): 'B4' is a list label.
SOURCE PMID22193544: /home/desktop/legend-development/files/fulltext/PMID22193544_Wang2012_PMC.xml ; figures and supplement in /home/desktop/legend-development/files/supplement/PMID22193544/ (f1-f6.jpg main figures; x1-x3 .png supplementary figures; x4.doc/x5.doc with .txt dumps; article PDF)

### S2 (CLAIM 035)
SENTENCE (verbatim, registry, Italian/English as written):
**B5 · S9.** The only measurement of S9 phosphorylation in this paper concerns the retinoic-acid time course of cells for which no transfection is mentioned, while WWOX expression rises: «the phosphorylation levels of phospho-GSK3β S9 and phospho-β-catenin remained normal» (Fig 1b); it is a correlation; no experiment manipulates WWOX and reads S9 phosphorylation in the text and legends of the paper (the supplementary figures and the figure images were not examined), and the phrase «S9-independent» occurs nowhere in the text.
CONTEXT (referent only): 'B5' is a list label.
SOURCE PMID22193544: /home/desktop/legend-development/files/fulltext/PMID22193544_Wang2012_PMC.xml ; figures and supplement in /home/desktop/legend-development/files/supplement/PMID22193544/ (f1-f6.jpg main figures; x1-x3 .png supplementary figures; x4.doc/x5.doc with .txt dumps; article PDF)

### S3 (CLAIM 019)
SENTENCE (verbatim, registry, Italian/English as written):
Western blot → proteina WWOX non rilevata** (evidence boundary misurata in intake wave 12, `CC-20261004W12-A-Q230P-01`, figure lette come immagini e verificate da un audit cieco il 2026-10-04: Fig. 3b porta **una barra per linea, nessuna barra di errore, nessun punto e nessun n**, con i valori a circa 99–102 % e il nucleo della paziente non superiore a HEK293;
CONTEXT (referent only): The patient is the one of this paper's Western blot (homozygous Q230P). A clause on LEGEND process history (dates, audit) is NOT_GRADED; the sentence opens with the end of 'Western blot -> WWOX protein not detected'.
SOURCE PMID29808465: /home/desktop/legend-development/files/fulltext/PMID29808465_Johannsen2018.pdf (+ .txt) ; /home/desktop/legend-development/files/figures/PMID29808465/

### S4 (CLAIM 019)
SENTENCE (verbatim, registry, Italian/English as written):
Fig. 3c: nessuna banda WWOX nella corsia della paziente, su una sola membrana, una sola esposizione, la linea fibroblastica di **una** paziente e nessun fibroblasto di controllo sano; l'actina è presente in ogni corsia e quella della paziente appare la **più intensa a ispezione visiva**, ma senza densitometria e con SW620 e HEK293 vicine, quindi il sotto-caricamento è *reso improbabile*, non escluso per misura.
CONTEXT (referent only): Same patient and figure set as S3.
SOURCE PMID29808465: /home/desktop/legend-development/files/fulltext/PMID29808465_Johannsen2018.pdf (+ .txt) ; /home/desktop/legend-development/files/figures/PMID29808465/

### S5 (CLAIM 030)
SENTENCE (verbatim, registry, Italian/English as written):
**Evidence boundary (BATCH_20260909_001 — the codon-47 contrast; narrows the EVIDENCE LINE, not the conclusion).** In the Banne 2021 review's Table 1 — resolved from the table's **`rowspan` markup**, not from its linearised text — `c.140C>G p.Pro47Arg` appears **only** as the **second allele of a compound heterozygote**, in trans with the exon-1 frameshift `c.46_49del p.Asp16fs`: 2 patients, Portuguese, onset 5 m / 5 m, **alive at 4 y and 3 y**.
CONTEXT (referent only): 'la review' = Banne 2021 (this PMID). The point of the strand is what the Table 1 gives for p.Pro47Arg (codon 47).
SOURCE PMID33916893: /home/desktop/legend-development/files/fulltext/PMID33916893_Aqeilan2021_PMC.xml ; /home/desktop/legend-development/files/supplement/PMID33916893/ ; /home/desktop/legend-development/files/figures/PMID33916893/

### S6 (CLAIM 030)
SENTENCE (verbatim, registry, Italian/English as written):
**Corroboration (BATCH_20260909_001 — independent secondary source, R4 satisfied).** Corroborated independently by Abu-Remaileh et al. 2015, *J Biol Chem* 290(52), **PMID 26499798** = [[paper_registry_current#PAPER 089]], whose Figure 2B draws P47R in trans with a codon-16 exon-1 truncating allele and is **the only patient row in that figure not assigned a single phenotype class**.
CONTEXT (referent only): 'Corroborated' refers to the statement that p.Pro47Arg is listed only as second allele of a compound heterozygote (in trans with a codon-16 truncating allele).
SOURCE PMID26499798: /home/desktop/legend-development/files/fulltext/PMID26499798_AbuRemaileh2015.pdf ; /home/desktop/legend-development/files/fulltext/PMID26499798_AbuRemaileh2015_PMC.html ; /home/desktop/legend-development/files/figures/PMID26499798/
