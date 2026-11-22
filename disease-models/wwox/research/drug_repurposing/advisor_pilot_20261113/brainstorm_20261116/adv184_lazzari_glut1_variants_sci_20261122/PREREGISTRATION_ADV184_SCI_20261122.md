# ADV-184 pre-registration: does Lazzari et al. 2026 (PMID 42928124, SLC2A1 variants in endothelial and HeLa models) give an ADDITIONAL, credible discriminator for INV-16 Step 1 among (a) reduced GLUT1 abundance, (b) altered localisation or turnover, (c) loss of transport despite apparent surface presence? (SCI successor Z, 2026-11-22; method transfer only; no HDAC5 pharmacology, direction, ranking or compound change; no GLUT1 or HDAC5 claim for WWOX from this source; no author contact; no e-mail address to any service; not medical advice)

Fixed BEFORE any body text, figure or supplement of the paper was read.

## What had been seen when this was written
* ADV-184's text: the identifiers, the one-sentence description (SLC2A1 variants in endothelial and HeLa models; Codex read it at source level only) and the exits. Step 0 (reported to ADV): the PMC open-data bucket route gave the full JATS XML (139,494 bytes, SHA-256 starting a361cf58), the 19-page PMC PDF (SHA-256 starting 3106aaf7) and a 25-page supplement PDF (SHA-256 starting 7b5abafb); the eight figure image files are declared in the XML but not in the bucket, so figures are read from the PDF pages. From file names and sizes only; nothing of their content.
* The repository, read first: the INV-16 row of `investigations_it20.tsv` (HDAC5 knockdown against catalytic and localisation rescue in human neural cells; the edge rests on one muscle knockdown observation) and `hdac5_inv16_20261107/output/experiment.tsv` Step 1: HDAC5 knockdown with a second reagent and siRNA-resistant rescue; readouts SLC2A1 transcript, GLUT1 protein and surface fraction, HIF1A and EPAS1 activity beside it, and one pre-registered functional endpoint (glucose entry with its metabolic fate; OCR/ECAR, lactate or uptake alone are not benefit); discriminating result "change that reverses on rescue = HDAC5-dependent; no change = edge not supported in this system". Steps 2 to 4 (catalytic and localisation mutants, SLC2A1 gain and loss arms, compound arm) read only as far as their first lines.
* Not seen: anything of the Lazzari text, methods, figures, supplement or numbers; no other paper on GLUT1 variants was consulted for this task.

## Rival readings and what each predicts for the Step 1 readouts (fixed now)
| Reading | transcript | total GLUT1 | surface GLUT1 (absolute) | surface fraction | glucose entry | entry per surface GLUT1 |
|---|---|---|---|---|---|---|
| (a) reduced abundance | down or unchanged | down | down in proportion | unchanged | down, tracks total | unchanged |
| (b) altered localisation or turnover | unchanged | unchanged or down | down | down | down, tracks surface | unchanged |
| (c) loss of transport despite surface presence | unchanged | unchanged | unchanged | unchanged | down | down |
Consequences already visible from Step 1 as written: (a) against (b) is separated by the surface fraction (given total); (c) against both is separated by glucose entry set against surface amount, which Step 1 lists only as a separate readout ("surface fraction" and "functional endpoint") without saying that entry is to be expressed per surface transporter. That normalisation is the candidate delta I will look for support for. A fraction alone cannot show an absolute fall in surface GLUT1 (case a), so the absolute surface amount is also needed; I will check whether the paper makes that point with data.

## Readings of the paper (fixed)
* **KEEP:** the paper measures, in a preparation that supports the transfer, a discriminator Step 1 does not already contain (for example per-surface-transporter activity, a surface-specific functional control, an origin or localisation control such as a compartment marker with a leakage control, or a turnover measurement), AND the observation does not depend on tagged overexpression or on an unmatched matrix, AND I can name ONE addition with its strongest rival and a refuting observation.
* **NARROW to a caveat:** the key observation depends on tagged overexpression, on endothelial or HeLa cells against a neural system, or on measurements that do not separate the rivals; or the only usable content is a normalisation or labelling control (one sentence on how Step 1's surface and entry readouts are expressed).
* **CLOSE as duplicate:** the paper only restates total against surface, or Step 1 already has the separation.
* **REJECT:** the paper's variant-protein behaviour cannot be transferred to a regulator knockdown (the paper concerns variant GLUT1 proteins, Step 1 concerns changed regulation of a normal protein): then the method-transfer content is stated as what it is and no change follows.

## My expectation, stated so the reading can refute it
Moderate confidence that the outcome is NARROW or CLOSE: the variants are likely expressed from constructs in HeLa and endothelial cells, so the abundance, localisation and activity of mutant proteins are measured under overexpression, and a matrix transfer to neural progenitors is not supported by the paper. If a per-surface activity readout or a surface-specific functional control is present and clean, a one-sentence normalisation caveat on Step 1 (entry per surface GLUT1, absolute surface amount next to the fraction) is the most likely survivor.

## Checks (fixed)
Which variants, which cells, how expressed (endogenous, stable line, transient, tagged); how surface was measured (biotinylation, antibody, imaging) and with what intracellular leakage control; how glucose entry was measured (2-deoxyglucose, a FRET sensor, radiolabelled) and in what units, per cell, per well or per surface amount; replicate units and n; whether any total, surface and activity value is reported for the same cultures; supplement read as headings and captions first; the DREAM analogy (total, located and functional GLUT1 as three quantities, the same shape as ADV-181's stock against new sheath) is kept only if it changes a real experiment or its reading.

## Consumers
ADV (result path and the exact decision affected, what would reject the change, an existing consumer or NONE). IT only if one technical qualification changes interpretation.
