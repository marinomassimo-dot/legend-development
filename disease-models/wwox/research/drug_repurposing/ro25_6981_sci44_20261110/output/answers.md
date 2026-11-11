# IT43-Q01: Ro 25-6981 primary source (package B), answers

Not medical advice. Reference genotype class only; nothing is promoted. Labels DATO / INFERENZA / IPOTESI. Row ids refer to `decisive.tsv`.

**One line.** DATO: primary text now gives Ro 25-6981 potency, conditions and site on GluN1/GluN2B diheteromers (IC50 0.049 uM human and 0.042 uM rat oocytes at -40 mV, 30 uM glycine, EDTA, pH 7.4: D01, D02; 59 nM beside ifenprodil 105 nM in one rat oocyte experiment: D04; ATD-interface site by structure: D10), but **no maximum inhibition** for any composition, and for GluN1/GluN2A/GluN2B triheteromers only a binding statement without a number (D08) and a structure (D09): the functional maximum and potency on triheteromers are still unreached (D14).

## Tier reached, per composition

| Composition | Quantity | Tier | Deciding rows |
|---|---|---|---|
| GluN1/GluN2B diheteromer, recombinant | potency (IC50, functional, oocyte) | PRIMARY (a table in a text actually read; Fig 3 image not seen) | D01, D02, D04 |
| GluN1/GluN2B diheteromer | maximum inhibition | not stated in any text read; only a by-eye plateau in a figure of one paper (D04, curves fitted to 100 percent) and a chicken native-culture plateau (D06) | D04, D06 |
| GluN1/GluN2B diheteromer | site | PRIMARY by structure for the diheteromer (crystal, cryo-EM) and in the triheteromer structure; mutagenesis and competition with ifenprodil not read here (the competition value is 'details not shown') | D10, D09, D05 |
| GluN1/GluN2A diheteromer | selectivity | single concentration only (less than 20 percent at 100 uM); not an IC50; conflicts in order with the abstract-level 52 uM | D03 |
| GluN1/GluN2A/GluN2B triheteromer | binding | statement in a text actually read ("submicromolar", about 3-fold weaker than diheteromer), number in an unreachable figure; not function | D08 |
| GluN1/GluN2A/GluN2B triheteromer | maximum inhibition and potency (function) | not reached; role stays unresolved | D14 |
| Native tissue | percent of the isolated NMDAR current removed | one slice measurement by eye from a bar chart (rat entorhinal layer V, 500 nM about 93 percent); composition inferred by the authors; abstract-level SCN value | D11, D12 |

## What the primary sources do not say

* No fitted maximal inhibition of Ro 25-6981 on GluN1/GluN2B in a text read; Hedegaard fits a variable-slope Hill equation and does not say whether the bottom was free (D01). The ifenprodil ceilings (88 percent and 32 percent) of the earlier package **cannot be carried to Ro 25-6981**.
* No functional triheteromer number for Ro 25-6981: the triheteromer cryo-EM paper reports binding and structure, and its oocyte inhibition percentages (3 uM Ro on engineered constructs) sit in Fig S1H, not reached. Whether the retention-signal paper (PMID 25505316) tested Ro 25-6981 is not known: only its abstract was reached.
* Triheteromer binding "about 3-fold weaker" is a binding comparison on purified protein in detergent at pH 8 with the diheteromer value taken from another paper (Lee 2014) whose text read has no such value; it is not a current measurement and not a verified fold.
* The native entorhinal result (about 93 percent at 500 nM) is far above the recombinant triheteromer ceiling of ifenprodil, yet that paper's own composition is an inference, the amplitude is evoked (presynaptic NR2B action is shown in the same paper), Zn2+ is ambient, and values come from bars read by eye. It does not show the composition of the Wwox slice, and it is not a transfer of one compound to another.
* The abstract-level Fischer values (9 nM, 52 uM; PMID 9400004) are still unverified; the 52 uM value does not match the less-than-20-percent-at-100-uM entry of Hedegaard (D03) and the paper behind the 9 nM entry was not reached; Stroebel 2016 lists 9 nM as a copied literature entry.
* Concentrations are nominal and the salt differs between papers (maleate, hydrochloride, none stated); recombinant data were taken without Mg2+ and with Zn2+ chelated, so they do not say what the same drug removes under 1-2 mM Mg2+ and ambient Zn2+.
* Inconsistencies inside the sources, not resolved: the 2008 binding paper's abstract says micromolar KD against nM values in its Results; Chamberlain's text says 100 nM Zn2+ while the panel label says 200 nM.

## Roles

DATO/INFERENZA: Ro 25-6981 is a **second tool of the ifenprodil site by site and structure** and by matched potency (59 versus 105 nM; 60 versus 103 nM in chicken culture), which controls for chemotype and the molecule's own off-target action. It **does not yet control for diheteromer versus triheteromer weighting**: no maximum on either composition. Tier for the engine: diheteromer potency PRIMARY; triheteromer maximum unresolved; the next work is the slice measurement M-R1 (new_measurements.tsv), with M-R2 only after the three unopened documents are read.

## Perimeter

PubMed (strings Q01-Q06, 2026-11-10/11, first 25-30 titles of each); eight papers opened as text, three at abstract level (20410362, 25505316, 11897110), 9400004 not retried; full texts withheld by PMC XML for 20410362 and 25505316; figure images unavailable in the open bucket for 28232581, 27062927, 22197913. No search of Europe PMC or Crossref was made in this package (one route per source).

## Corrections after independent verification (V3, Orchestrator, 2026-11-11)
D05 had the displacement direction reversed (Ro 25-6981 displaced ifenprodil from the ATD, Ki 2-4 nM); D06 Mg2+ is in the wash buffer only; D01 and D04 carry unsupported qualifiers; D08 is a statement without a number and Lee 2014 Extended Data Fig 2g prints a diheteromer Kd of 48 +/- 22 nM; the "GluN2A decreases inhibition by ifenprodil or Ro" sentence extends ifenprodil and CP-101,606 data to Ro 25-6981. Diheteromer potency is PRIMARY; no maximum inhibition is measured for any composition; the triheteromer has structure and an unnumbered binding statement but no functional value. Logged in CORRECTIONS_V3.tsv. Three producer receipts list figures or discussion as read although one figure was viewed or the discussion was read in part (the closed coverage vocabulary has no partial value; flagged for the integrator).
