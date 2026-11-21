# Pre-registration: Fig. 5G neuronal subtypes and ion-channel gene sets against EV9C (SCI window X, 2026-11-21; hypothesis level; no dose; reference genotype class only; not medical advice)

Origin: the in-silico step I named at the close of ADV-142 (`../adv142_baseline_five_metric_sci_20261121/RESULT_ADV142_BASELINE_FIVE_METRIC_SCI_20261121.md`, CHOICE) and ADV's instruction to run it now (RP-043). Sources: Brain 2026 accepted manuscript (AM, held `files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf`, layout text and page images) and bioRxiv v2 preprint Expanded View (EV9C, held). Read-only; held bytes only; no external contact.

## Disclosure: what I had already seen
AM Fig. 5F at image level (early-neuron share WT about 0.33, WOREE about 0.66, SCAR12 about 0.68; log2 fold changes about +1.0 and -1.0 for both) and the Fig. 5F-G sentence in the Results; EV9C at 100 dpi (two labelled blue points, RPS29 and RPL38, left of the left 0.5 line; no point right of the right line; none purple), plus the AM statement that only two genes differ between SCAR12 and WOREE neurons (Supplementary 8F). I had NOT measured the Fig. 5G subtype proportions, read Fig. 5C-D (gene-ontology terms) at full resolution, or read the Results passage that mentions reduced voltage-gated and ligand-gated ion-channel genes in context.

## Questions fixed now
Q1. Fig. 5G: per genotype (WT, WOREE, SCAR12), which neuronal subtypes exist and in what proportion, and do WOREE and SCAR12 differ in any subtype by more than 10 percentage points by eye? (Row B of the competing-explanations table: does an immature state differ between the two patient-derived genotypes in a way that could carry the week-16 rate gap?)
Q2. Do the AM and EV9C name any ion-channel or synaptic gene as differing between WOREE and SCAR12 neurons? Do the Results lines on reduced ion-channel and neurotransmission genes compare patient-derived against WT pooled, or WOREE against SCAR12? (Row G, line or allele effect: can this data set carry a WOREE-SCAR12 gene-level difference at all?)
Q3. n and unit of Fig. 5: how many organoids, lines and cells per genotype; is any test printed for the subtype or early-share comparison?

## Predictions (written before opening Fig. 5G, 5C-D or the Results passage)
* P1 (60 percent): all subtypes present in all three genotypes; the early-share gain in both patient-derived genotypes is spread over at least two subtypes.
* P2 (85 percent): no ion-channel or synaptic gene is named as differing between WOREE and SCAR12; the only two named are the ribosomal genes of EV9C.
* P3 (70 percent): the ion-channel statement compares patient-derived neurons pooled against WT, not WOREE against SCAR12.
* P4 (55 percent): no subtype differs between WOREE and SCAR12 by more than 10 percentage points by eye.
* P5 (80 percent): one scRNA sample per genotype, no test printed for Fig. 5F-G; the lines are pooled inside a genotype.

## Rules
Classes MADE / VISUAL / NOT PRINTED / UNREADABLE as in ADV-140 and ADV-142; each number carries its version (AM or PP2); by-eye readings are labelled VISUAL and measured with ImageMagick and numpy from the held page image (PIL, matplotlib and cv2 are not installed); a blind re-measurement of the Fig. 5G proportions by a different delegate on the cropped image only; no third-party image is committed. Close with a CHOICE (next verifiable step, rejecting observation, what unblocks).
