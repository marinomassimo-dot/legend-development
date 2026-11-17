# RESULT - IT48Q01: Ba2+-sensitive share of resting conductance, rodent neocortical layer II/III pyramidal neurons, P13-17

Date 2026-11-17. Mechanism-level literature package; reference genotype class only; no dose or recommendation. Source files: `measurements.tsv` (23 rows), `SEARCH_RECORD.md` (every query), `human_access_list.tsv` (11 rows). Full texts: `/home/desktop/legend-development/files/fulltext/it48q01_it_20261117/` (git-ignored).

## 1. Answer first

**For the target window (layer II/III pyramidal neurons, P13-17, any rodent, any cortical area): NOT FOUND by query families A, B, C and D.** That wording is deliberate: it means not found by those 28 PubMed and 43 distinct Europe PMC query strings and by the automated full-text screen of 210 PMC ids. It does not mean no such measurement exists.

**For adjacent ages: PARTLY FOUND.** Two papers give numbers from which a Ba2+-sensitive share of resting or input conductance in layer II/III pyramidal neurons can be stated, both outside P13-17 and with different Ba2+ concentrations, so they cannot be combined into a gradient:

| Source | Ba2+ | Age | Share | How obtained |
|---|---|---|---|---|
| Nguyen 2024 (mouse mPFC, L2/3 pyramidal, control-plasmid neurons) | 200 uM (high; K2P also affected) | P26-51 | about 68% of resting membrane conductance (conductance from the Vm change to -500 pA from rest; pre about 9-10 nS, post about 3 nS) | read by eye from Fig. 3-figure supplement 3 f-g; approximate |
| Fmr1-KO auditory-cortex preprint 2026, WT arm (mouse A1, L2/3 pyramidal) | 60 uM (low-intermediate) | P28-42 | about 23% of input conductance (1 - 172.7/(172.7+51.1)), plus 59.6% block of the current at -130 mV (not a resting share) | stated numbers, arithmetic by this package; via WebFetch, not byte-verified; preprint |

No paper gave a pyramidal-neuron value at P7-12, P13-17 or P18-25. The only age-resolved Ba2+ numbers (P10 versus P18+) are for fast-spiking interneurons (Goldberg 2011), listed below as a contrast and excluded from the pyramidal answer.

## 2. Ages and Ba2+ concentrations (pyramidal rows first; interneuron contrast marked)

Ba2+ class used: low = 50 uM or below (Kir2-selective range); intermediate = 60-100 uM; high = 100-500 uM (also partly blocks K2P channels, per the authors cited in the table rows); mM = broad K+ channel block.

| Age band | Paper (row) | Species / area / layer / cell | Ba2+ | What was measured | Share? |
|---|---|---|---|---|---|
| P7-12 | Goldberg 2011 (R09) | mouse barrel, L2/3, FS interneuron (not pyramidal) | 500 uM (high) | Ba2+-blocked outward holding current at -70 mV 21.8 +/- 2.8 pA; maximal Ba2+-sensitive inward current at -120 mV -75.5 +/- 51.3 pA | not a share |
| P7-12 | Richter 1997 (R14, abstract-only) | rat entorhinal, L-II stellate / L-IV pyramidal | not stated | inward rectifier current density, juvenile (P8-14) larger than newborn in pyramidal cells | not a share; entorhinal, abstract-only |
| P13-17 | none found | | | | |
| P14-23 (straddles P13-17 and P18-30) | Xue 2014 (R01) | mouse V1, L2/3 pyramidal control cells | 50 uM (low) | Ba2+-sensitive current density at -125 and -45 mV (values in Extended Data Fig. 4c only; figure not retrievable) | not a share; no numbers read |
| P18-30 | Goldberg 2011 (R07, R08) | mouse barrel, L2/3, FS interneuron (not pyramidal) | 50 uM; 500 uM | Rm 118.7 to 130.7 Mohm (50 uM); 112.3 to 153.1 Mohm (500 uM); holding current blocked 27.5 and 148.1 pA | derived input-conductance fractions about 0.09 and 0.27 (group means; interneuron) |
| P19-25 (layer V-VI, wrong layer) | Day 2005 (R10) | mouse prelimbic/infralimbic, L V-VI pyramidal | 50 and 200 uM | model G_Kir2 : G_Kleak about 10:1 for the 200 uM Ba2+-sensitive current | not a share of resting conductance |
| P26-51 | Nguyen 2024 (R02) | mouse mPFC, L2/3 pyramidal | 200 uM (high) | resting conductance pre/post, % change | about 0.68 (figure-read) |
| P28-42 | Fmr1 preprint, WT (R04, R05) | mouse A1, L2/3 pyramidal | 60 uM | Rin baseline 172.7 Mohm, +51.1 Mohm with Ba2+; -130 mV block 59.6% | about 0.23 (derived); 0.596 at -130 mV (stated, not resting) |
| adult (2-4 months) | Routh 2022 (R03) | mouse V1, L2/3 pyramidal | 25 uM (low) | R_N increased at hyperpolarised Vm; no number in text | not a share |
| cohort P6-P96, age of the Ba2+ experiment not stated | Goodfellow 2009 (R06) | rat mPFC, L2/3 pyramidal | 1 mM (mM) | Ba2+ inhibited the 5-HT1A-evoked outward current 80.9 to 12.7 pA | not a resting-conductance share |
| unknown age | Sutor 1993 (R11), Hwa 1991 (R12), Sceniak 2006 (R13), all abstract-only | rat neocortex (Hwa: layers II/III; Sceniak: visual cortex) | 10-100 uM; 3 mM; not stated | holding current / input resistance / rectification / leak conductance, direction only | not a share |

Reading of the Ba2+ concentration: the sub-50 uM rows (Xue, Routh, Goldberg 50 uM, Day 50 uM) are the Kir2-selective probes and none of them yields a resting share for pyramidal cells at the target age. The only pyramidal "resting share" (Nguyen, about 68%) used 200 uM, and Goldberg shows in the same cell class that 50 uM and 500 uM blocks differ about threefold in the input-conductance fraction (0.09 versus 0.27), so a 200 uM value cannot be read as a Kir2-only share.

## 3. What a developmental gradient looks like in the evidence found

Only one age-resolved Ba2+ comparison exists in the retrievable text, and it is not pyramidal: Goldberg 2011 reports a much smaller Ba2+-sensitive conductance at P10 than at P18+ in L2/3 fast-spiking cells (outward holding current blocked at -70 mV 21.8 pA at P10 versus 148.1 pA at P18+, both at 500 uM; Ba2+-sensitive current at -120 mV -75.5 versus -302.8 pA). For pyramidal cells the age gradient is not recoverable from the retrievable texts. Three developmental intrinsic-property series (Oswald and Reyes 2008, Kroon 2019, Ciganok-Hueckels 2023) and two further L2/3 pyramidal papers (KCNQ2, Niday 2017; layer 2 versus layer 2/3, Luo 2017) were searched in full text and contain no Ba2+ experiment (rows R18-R22).

## 4. Limits

- **Absence is two-route, not proof.** Not found by PubMed MCP strings P1-P28 and Europe PMC strings E1-E46 (43 distinct) plus the 210-id full-text screen (122 with a retrievable body, 91 without). The PubMed MCP tool AND-s every term and returned zero for most multi-concept strings; the Europe PMC full-text route only reaches open texts. Papers behind publishers (older J Neurophysiol, J Physiol, Neurosci Lett) are the likeliest place for a missing value; see `human_access_list.tsv`.
- **Read depth.** For R01, R02, R03, R06, R07-R09 and R10 the Ba2+ passages, the Methods age/layer statements and (R02) one figure were read from the retrieved text; this was not a line-by-line read of whole papers, and no FULLTEXT_READ_RECEIPT was recorded (not requested). R04, R05 and R23 were obtained through WebFetch (a summarising fetch tool), so their quotes are summariser output, not byte-verified; R04 and R05 cover only the first 100,000 of 120,719 characters; R23 covers 200,000 of 219,030. R16 and R17 are snippet-level. Abstract-only rows (R11-R15) are not counted as read.
- **The Nguyen value is a figure read by eye** from an open JPEG; the underlying source data were not opened. It is a share only because the paper defines resting conductance from the Vm response to a -500 pA step and gives pre/post values; that step reaches the Kir range, so it is not the conductance at rest in a strict sense. Control = control-plasmid electroporated neurons.
- **Derived shares** (R04, R07, R08) are this package's arithmetic on group means given in the papers (1 - R_before/R_after), not per-cell numbers and not the authors' own statistic.
- **Xue 2014 is the closest hit to the target** (mouse V1 L2/3 pyramidal control cells, P14-23, 50 uM) but reports Ba2+-sensitive current density in an Extended Data figure only; the image routes returned HTTP 403, and the value is a density, not a share.
- **Routes stopped.** NCBI PMC article pages served a Google reCAPTCHA at about 06:54 on 2026-11-17 and were not requested again; Europe PMC fullTextXML returned HTTP 500 for most ids; bioRxiv direct returned HTTP 429; the APS journal page returned HTTP 403. None was bypassed. No e-mail address was sent anywhere.
- **Species and cell-line transfer.** All rows are mouse or rat; none is human. Channel subtype attributions (Kir2 versus K2P) are the cited authors' statements, not this package's findings.
- This package did not verify or audit its extractions with a second reader; the decisive rows for a downstream decision are R01, R02, R04, R07-R09 and should get the narrow check described in the delegation budget (section 8) before they are used.
