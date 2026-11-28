# ADV-297 step B batch 2 (records 7, 8, 10): full-text reader report

legend-delegate, claude-sonnet-5-5, effort high on 28 of 28 turns. Model output, hypothesis level, not medical advice; saved verbatim but for one mark: a space put into a quoted, elided link so that it is not read as a broken relative link.

---

FULL-TEXT CHECK, three papers. Hypothesis-level, public literature; nothing here is medical advice.

**Counted data:** record 7 (PMID 25662954) has 4, one of them borderline. Record 8 (PMID 26910372) has 0. Record 10 (PMID 17690733) has 0.

Held paths below are relative to `/home/desktop/legend-development/.claude/worktrees/sci_av_20261128/disease-models/wwox/`:
- CR = `registries/claim_registry_current.md`
- DL = `research/discovery_ledger_current.md`
- A03 = `research/drug_repurposing/cards/A03_client_binding_chaperone.card.json`

## Record 7, PMID 25662954 (Farooq, Exp Biol Med 2015, PMC4374002)

### (1) What it is
A single-author review that also carries the author's own material on human WWOX. There are no cells or animals.
- A homology model of the WW1-WW2 tandem (FBP21 template) with a p73 peptide docked.
- A 2 µs molecular dynamics run, unliganded and liganded.
- Table 1: ITC at 25 °C, pH 7, eight 12-mer PPPY peptides, WW1 alone against WW1-WW2. Errors are 1 SD from at least three measurements. The text attributes the ErbB4 and WBP1/2 findings to the lab's earlier papers and calls the p73, PTCH1, PTPN14, SMAD7 and TMG2 comparisons unpublished.
- Sequence alignments, and an SDR homology model (mpRDH template) with NADPH and retinal docked.
- A statement of preliminary biochemistry on bacterially purified recombinant SDR. No data, conditions, n or constants are shown.

### (2) Counted data

**D1. SDR retinol/retinal activity.**
- Locator: section "SDR domain of WWOX appears to serve as a retinal oxidoreductase", last paragraph.
- Datum: in the author's lab, purified recombinant SDR catalyses retinol to retinal and "appears to" catalyse the reverse efficiently. Retinal to retinoic acid "may" also occur. All of it is preliminary and unshown.
- Held, DL:3850: "the corpus's SDR reading has rested on one laboratory's crude-extract enzymology."
- Changed: "...has rested on one laboratory's crude-extract steroid enzymology and, from a second laboratory, a preliminary statement without data (2015 review) that bacterially purified recombinant SDR domain interconverts retinol and retinal."
- Held, A03:78 (same text at :88): "One repository reading reports steroid substrates with apparent Km values for a WWOX fusion protein in a bacterial crude extract, unreplicated and with no purified-protein binding (PMID 21476439)..."
- Changed: add "a second source states, without data, retinol/retinal oxidoreduction by purified recombinant SDR". This adds a substrate class and an evidence level. It is not a measured binder.
- CR:738 ("il cui substrato fisiologico è ignoto") would only gain a qualifier: an in vitro candidate, with the physiological substrate still unknown.

**D2. Cofactor and evidence level of the active-site map.**
- Locator: same section (alignment, Figure 6 legend) and the SDR fold section (Figure 7 legend).
- Datum: GXXXGXG accommodates NADP+/NADPH. S260 is proposed to stabilise the retinoid substrate and Y293/K297 form the dyad. The basis is alignment and a homology model. The string "281" does not occur in the body.
- Held, DL:29: "la mappa del sito attivo SDR di WWOX è S260 (substrato), **S281 + motivo YxxxK Y293–K297** (catalisi), motivo Rossmann GxxxGxG N-terminale per NAD ([struttura, PMC4374002] (...))."
- Changed: "...GxxxGxG for NADP(H) (assigned by alignment and homology modelling in a review, not an experimental structure; S281 is not from this source)".
- DL:336 (NS-007, "residuo catalitico/NAD-binding") would likewise read NADP-binding.
- The held line cites this very paper for the map.

**D3. Size and scope of the tandem gain.**
- Locator: Table 1.
- Kd in µM, WW1 then WW1-WW2, with my fold calculation:

| Peptide | WW1 | WW1-WW2 | Fold |
|---|---|---|---|
| ErbB4 | 179±10 | 75±8 | 2.4 |
| p73 | 107±9 | 60±6 | 1.8 |
| PTCH1 | 278±19 | 79±8 | 3.5 |
| PTPN14 | 763±62 | 214±30 | 3.6 |
| SMAD7 | 272±29 | 53±8 | 5.1 |
| TMG2 | 202±23 | 84±9 | 2.4 |
| WBP1 | 368±44 | 141±12 | 2.6 |
| WBP2 | 133±18 | 42±7 | 3.2 |

- Held, DL:1228 (entry sourced to PMID 25703206): "WW1 **nel modulo tandem** lega **2-3× più forte** che da solo, con **guadagno entropico**."
- Changed: "...lega circa 1,8–5× più forte (otto peptidi PPPY di 12 residui, ITC)". The review's own prose says two- to three-fold and its table does not agree.
- Held, CR:503 (CLAIM 024 summary): "Cooperative WW1–WW2 architecture improves recognition of dual PPxY-containing partners."
- Changed: "...improves recognition of PPxY ligands, including single-motif peptides (1.8- to 5.1-fold lower Kd for eight 12-mers), as well as of dual-motif partners."

**D4. SMAD7 peptide binding (borderline, weakest of the four; drop it if "adds an evidence level to a premise" is too loose).**
- Locator: Table 1, SMAD7 row (LESPPPPYSRYP).
- Held, DL:3650: "WWOX è una proteina a dominio WW che lega PPXY. **Ipotesi competitiva mai testata qui: WWOX stabilizza Smad4 competendo con Smurf per gli stessi motivi PPXY.**" The same bullet names Smad2/Smad7 PPXY.
- Changed: "WWOX WW1 binds a SMAD7 PPPY 12-mer in vitro (Kd 272 µM alone, 53 µM in tandem); competition with Smurf remains untested."

### (3) Uncounted
- Alignment places the WWOX SDR closest to RDH11/12/13 and a mycobacterial RDH, and poorly similar to HSD1/2/3. This is borderline against DL:44 ("membership of the SDR / 17-beta-HSD family predicts no substrate"). I did not count it because the conclusion of that sentence stays.
- The MD "lid" (WW2 on the WW1 binding face, displaced by ligand, with the W44/Q65/V73, T67/W31/Y33 contacts) is already held in DL:1234-1236 from another source. This review says 2 µs; the held entry says 4 µs.
- The static homology model shows no interdomain contact while the MD shows association.
- The SDR homology model with docked NADPH and retinal does not change the held "no experimental structure" statements (A03:77, DL:1300-1301).
- WW2 showed no intrinsic binding. Already held.
- WW1 similarity to ITCH/NEDD4 WW domains, a survey of non-Trp WW domains, and the vision and RAR ideas (speculation).
- Figure legends write "RXXXK" where the text writes "YXXXK".

### (4) Searches
All held files in the dispatch list, including card and packet JSON and both comparator TSVs. Keywords:
- identifiers (PMID, author)
- WW2, tandem, lid/coperchio, chaperone, dumbbell/interdomain
- SDR/short-chain, retinoic/retinol/retinal, retinoid/all-trans/retinaldehyde (0 hits)
- Y293/K297/S260, NAD/cofactor/Rossmann, substrate, purified/recombinant, enzyme/enzimatica
- 17β/HSD/steroid, crude extract/enzymology/Saluda/21476439
- Kd/affinity, ErbB4, p73, WBP, SMAD7/PTCH1/PTPN14/TMG2
- Hippo/YAP/ITCH/NEDD4, retina/vision/optic/photoreceptor

## Record 8, PMID 26910372 (CNV-67048 and intracranial aneurysm)

### (1) What was measured
Human, Han Chinese, two-stage case-control. Germline CNV-67048 deletion was typed by qPCR on blood DNA in 976 cases and 1200 controls.
- Pooled OR per deleted copy 1.35 (1.16–1.57). One copy 1.24 (1.02–1.52), two copies 1.77 (1.24–2.53).
- WWOX mRNA was lower in aneurysm tissue than in border tissue (70 pairs, P = 0.004). It was lower with the deletion genotypes in both tissues (P = 0.001 and 0.002).
- Western blot on 10 pairs showed on average 48% less WWOX.
- No cell type is resolved (bulk tissue).

### (2) Counted data
None.

Nearest held sentences, and why they do not change:
- CR:679 concerns a different, specifically identified common intronic deletion (PMID 41345172) that "removes no exon". This paper does not identify CNV-67048 with it and does not say whether CNV-67048 removes an exon.
- CR:676-677 (CLAIM 032 revival triggers) ask for EEG or network data in a heterozygote, or phenotype in carriers of an exon-level deletion. Neither is met.
- CR:996 (CLAIM 045: "dal lato umano, una coorte di portatori con un comparatore e un fenotipo misurato") is the closest. This is disease-ascertained case-control work on a CNV not shown to remove a functional allele, so I did not treat the trigger as fired. The caller may want to look at this judgement.

### (3) Uncounted, worth knowing
- Controls: 860 / 283 / 57 with zero, one and two copies deleted. So 4.75% of controls carry two deleted copies, and the deletion allele frequency is about 0.165 (my calculation).
- Validation-stage one-copy OR is not significant: 1.16 (0.89–1.52).
- Coordinates chr16:76,929,120-76,942,453 are given with no genome build.
- Quality problems: the aneurysm results say "increased risk of lung cancer" and speak of "tumor tissues". Expression values by genotype are not printed. Hypertension is about 60% in cases against 20% in controls (used as a covariate).

### (4) Searches
- CNV/copy number
- aneurysm/67048/subarachnoid (0 hits), intracranial/cerebrovascular, stroke/haemorrhage
- vascular/endothelial/vessel
- heterozygous/haploinsufficiency/carrier, including combined with healthy/unaffected and with risk/surveillance
- glioma/COPD/lung cancer, hypertension
- GWAS/common variant/polymorphism/susceptibility
- common or intronic deletion, PAPER 209/41345172
- carrier items in the open-questions map

## Record 10, PMID 17690733 (Hezova, Ehrmann, Kolar 2007)

### (1) What it reviews
A narrative review despite its "Methods and Results" abstract heading. It covers the gene and protein structure; reported partners (p73, AP-2, YAP/ErbB4); a Drosophila model; expression and loss in breast, prostate, ovarian, pancreatic, gastric, liver and lung cancer; and Wox1 in the developing nervous system and in Tau phosphorylation. Everything WWOX-related is cited from others.

### (2) Counted data
None. Condition 1 fails throughout.

### (3) Uncounted
No own WWOX result. The authors mention an earlier study of theirs on androgen receptor in brain tumour cell lines, which is not a WWOX datum. "WWOX has not yet been studied in brain tumors" is a 2007 statement of the literature, not a result.

### (4) Searches
Identifier and author search plus "Hezova|brain tumour" (0 hits for the latter). The only identifier hits were "Farooq" mentions belonging to record 7. I ran no topic-by-topic comparison, because no datum passes condition 1.

## (5) Not read, and failures
- No figure images and no supplements for any of the three. Nothing was downloaded.
- Record 7 was read from the supplied text, record 10 from the PDF text. For record 8 I extracted title, abstract, body, tables, figure legends and acknowledgements from the XML, and left out its reference list.
- Held files were searched by keyword and read around hits, not whole. Lines mentioning 42422765 or Obeid were skipped.
- One over-large retinoid search output was not opened; narrower searches replaced it.
- Two `grep` patterns failed on regex complexity. One was a CR search for reduced WWOX in human tissue, covered only partly by the other searches. The other was a source-text context search for "281"; a plain count (0) replaced it.
- The scratch directory is deleted. I wrote no repository file.
