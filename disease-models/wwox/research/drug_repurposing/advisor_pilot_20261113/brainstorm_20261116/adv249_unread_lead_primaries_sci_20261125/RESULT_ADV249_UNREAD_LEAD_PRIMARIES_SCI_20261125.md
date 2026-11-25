# ADV-249 result: primaries behind discovery-ledger leads that were never read (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; nothing here is medical advice. Open copies only; no spend, no contact, no delegate. Pre-registration: `PREREG_ADV249_SCI_20261125.md` (frozen before the listing was run). Listing: `list_leads_adv249.py` → `never_read_leads.tsv`.

## 1. Answer

* 239 lead ids; 153 name a primary PMID (103 distinct). **86 leads name none** and are outside this audit.
* The listing flagged 12 primaries. One (26857392) holds an old reconstructed "partial" receipt, so by the assignment's wording it is outside the class: my listing rule ignored such receipts. One (25703206) is declared read in full by the ledger itself and has no receipt: a ledger gap, not counted. **Ten are never read.**
* **Only three of the ten could be read** lawfully today, plus the 26857392 paper. Six could not be read (table in section 4), one was not reached (20067585, no open copy found).
* Lead wording against the paper: **one overstates** among the three in class (0.33); two of four with 26857392.
* The two most consumed never-read primaries (the Wnt direction behind cards D01 and D02) are closed. This is not news: the lead has said since 3 October that none of its three primaries was read at full text, and Bouteille 2009 is queued as `FT-180`.

## 2. Per paper

Receipts recorded for the four, with exactly the sections read: figures from captions only, supplements not opened, reference lists not read.

### DL-MECH-032 ← PMID 36572560 (Yook 2022): **overstates**
* Lead: the paper shows WWOX is a GSK-3β-binding protein through the GID motif ("DATO"), so WWOX loss may dysregulate GSK-3β; repurposing candidate.
* Paper: a study of the SARS-CoV-2 nucleocapsid. **It has no WWOX experiment**: WWOX is one name in a list of motif-carrying proteins, cited from other work (Howng 2010; Wang 2012). Its own result is that the viral protein binds GSK-3β through such a motif **without** changing GSK-3 activity or Wnt output, so the motif alone says nothing about direction.
* Already on file: Wang 2012 is completely read (PAPER 056, CLAIM 035): binding through the SDR domain, with inhibition. The lead's two open questions (direction, which domain) have answers there.
* Unit: no numerical WWOX claim. Contradiction: the S202R variant is assigned to Delta in the abstract and to another lineage ("Lota") in Results and Discussion.
* Promote: no. Wording for IT: "DL-MECH-032: this 2022 paper only lists WWOX among GID-motif proteins; binding and direction rest on Wang 2012 (CLAIM 035). No repurposing inference follows from this paper."

### DL-MECH-025 ← PMID 28151481 (Maroni 2017, retracted): **equals**
* Lead: a retracted paper must not support anything. Confirmed: retraction notice PMID 35680840 (*Cell Death Dis* 13:542, 2022): loading-control bands reused across panels and publications; the editors no longer have confidence in the data; one author disagrees.
* Label fix: the lead writes "retraction PMID 28151481", which is the retracted article; the notice is 35680840.
* Not checked: the lead's statement that review 28045433 reuses its Figure 3B (review not opened).
* Inside the paper: decitabine lowers Wwox in cultured cells and raises it in the xenograft. Not for citation either way. Promote: no.

### DL-BIO-006 ← PMID 29108237 (O'Leary 2017): **equals** (its half of the lead)
* Paper: two circular RNAs from WWOX exons (KIRKOS-71, exons 2 to 8; KIRKOS-73, exons 7 and 8) change after irradiation, down in two cell lines, up in a third; found in exosomes from the **culture medium** of two tumour lines. KIRKOS-71 not detected in endothelial cells. No fibroblast, lymphoblastoid or neural material.
* The lead's serum-exosome sentence belongs to Xu 2017 (not read here).
* Unit: cultures of cell lines; n = 3 stated for knockdown and pull-down only, not for the expression changes.
* Contradictions: exosome results are cited to Figure 1c and 1f while the exosome panels are 2c and 2f; the methods state an incubator at 95 % oxygen.
* Neither circle contains exon 9, so neither can report on an exon 9 acceptor allele (the lead already says it does not). Promote: no.

### DL-BIO-003 ← PMID 26857392 (Schirmer 2016): **overstates** (outside the class)
* Lead: the authors "document" transcripts ending in intron 8, and an assay "already published and validated" measures what fraction of WWOX transcript correctly includes exon 9.
* Paper: the transcripts ending in intron 8 are **cited from database entries**, not measured. The assay compares an exon 8 to 9 amplicon with an exon 4 to 6 amplicon in 88 lymphoblastoid lines (mean 67 % against a cloned-cDNA standard; r = 0.68). **It was never tried on a splice-altering variant** and does not separate exon skipping, intron retention, a cryptic site or alternative termination.
* Unit: one lymphoblastoid line per donor; the AA genotype group is 5 of 89.
* Contradiction: the variant's identifier appears as rs11644322, rs11644332 (abstract conclusion) and rs11466322 (results and legends).
* Wording for IT (DL-BIO-003, PAPER 050): "a junction-versus-core RT-qPCR used in lymphoblastoid lines; not validated for detecting exon 9 loss. Alternative 3′ ends in intron 8 are cited from databases."
* PAPER 050 already exists; it says "full text reviewed (complete)" while the only earlier receipt is a reconstruction with unknown sections.

## 3. New questions

| Question | Observation that would answer it |
|---|---|
| In reference-genotype-class cells, what does the exon 8 to 9 amplicon actually lose with an acceptor-site allele? | RT-PCR from exon 7 into the 3′ UTR, or long reads, on carrier and control RNA with and without blocking nonsense-mediated decay, beside the junction assay |
| Does the retraction of 28151481 reach anything through review 28045433? | open the review's Figure 3 and compare with the retracted panels |

No new question from the other two.

## 4. Not read

| PMID | Lead (consumers) | Route result |
|---|---|---|
| 19465938 | DL-MOL-003, DL-MECH-008 (D01, D02) | closed per Europe PMC and OpenAlex; publisher page is a subscription preview (`FT-180`) |
| 23030478 | DL-MOL-003 (D01, D02) | closed; publisher 403 challenge |
| 42190144 | DL-MOL-001, MECH-001, REPO-001 (F01) | university archive copy returned 403 |
| 34015398 | DL-MOL-004 (C03) | closed per Europe PMC and OpenAlex |
| 18371080 | DL-MOL-008 | closed per the same two |
| 42275215 | DL-MECH-014 | open-access per OpenAlex; publisher answered with a 403 challenge page |
| 20067585 | DL-BIO-013, MECH-066 | no open copy found; abstract-only receipt |

## 5. Predictions

| | Prediction | Outcome |
|---|---|---|
| P1 | overstating share between 0.33 and 0.67 | Met at the lower edge (1 of 3 in class; 2 of 4 read) |
| P2 | at least one internal contradiction (0.6) | Met (all four) |
| P3 | at least four of six transfer a direction from non-neural work to neural cells | Not met: four read, one such transfer |
| P4 | no card disposition changes | Met: only D02 names one of the four leads (DL-MECH-032), beside a direction the card already calls contested |

## 6. Limits

Four papers, not six. Figures were not viewed, so "contradiction" means text and captions. My verdicts have no second reader. The consumer count covers portfolio, investigations, cards, claims, model records and triggers; the paper registry is not counted.

## 7. DREAM

Not yet consumed: the two wordings. The cheap class here is not exhausted by access: 86 leads name no primary at all, which no receipt check can reach.
