# ADV-068 pre-registration, frozen before any count table is opened (SCI, 2026-11-19; hypothesis level; no dose, no recommendation; not medical advice)

Question (ADV-068, census choice A). In the public per-animal bulk RNA deposits of the neuron-targeted Wwox deletion at P17, does the lower Pvalb transcript look like a PV-specific deficit (fewer PV cells or less Pvalb per cell) or like part of a broader fall of late-maturing neuronal genes (maturation delay or a late-stage effect of the mutant)? The per-animal step cannot separate fewer PV cells from less Pvalb per cell; it can separate "PV-specific" from "falls together".

## What the deposits are (stated before opening any count; metadata only, fetched from the GEO series text)
* GSE158681: whole hippocampi at P17, 14 samples, one sample per library: WT n = 3 against Wwox-null n = 2; S-Ctrl n = 2 against S-KO n = 3 (S = neuronal deletion, Synapsin-Cre line); N-Ctrl n = 2 against N-KO n = 2 (N = neural stem and progenitor deletion, Nestin-Cre line). GSE158682: cortices at P17, S-Ctrl n = 4 against S-KO n = 3. GSE158685: the SuperSeries of GSE158681, GSE158682 and GSE158684 (the single-nucleus deposit: S_Ctrl1-4 against S_KO1-4, held as two pooled matrices).
* **Same laboratory, same Cre lines and the same P17 cohort family as the held single-nucleus data: not independent origins.** Whether one GEO sample is one animal is not stated in the metadata; it is assumed, not verified.
* The Pvalb direction in these deposits is already known to me from IT13 P3a (lower in all four within-line contrasts; PV-selective against a flat pan-interneuron panel): **retrospective for the Pvalb element, prospective for the late-maturing and reference sets**, which I have not seen.

## Unit, contrasts and the stop rule
* **Unit = one GEO sample treated as one animal.** Contrasts are within-line (knockout against its own line's controls); no pooling across lines.
* **Stop rule S (ADV's): a contrast with fewer than three animals per arm gets descriptive values only, no rule verdict ("a measurement").** Only **cortex S-KO against S-Ctrl (3 against 4)** meets it; the hippocampal contrasts (S 3 against 2, N 2 against 2, null 2 against 3) are descriptive.

## Gene sets (mouse symbols; fixed now; chosen from general knowledge of postnatal expression, not from these data; a judgement, not a calibrated list)
* REF_STABLE (pan-neuronal, expressed early): Snap25, Rbfox3, Syt1, Stmn2, Tubb3, Map2.
* PV_SET (PV-cell genes): Pvalb, Syt2, Kcnc1, Kcnc2.
* INT_NONPV (other interneuron genes): Gad1, Gad2, Slc32a1, Sst, Vip, Npy, Cck, Calb2, Htr3a, Lhx6, Dlx1, Dlx2, Dlx5.
* LATE_NONPV (late-maturing neuronal genes not specific to PV cells): Grin2a, Slc12a5, Nrgn, Camk2a, Scn8a.
* GLIA_GUARD: oligodendrocyte Mbp, Plp1, Mog, Mobp; astrocyte Gfap, Aqp4, Aldh1l1; microglia Cx3cr1, P2ry12, Tmem119, Csf1r. Deletion check: Wwox.

## Normalisation and statistic
Per animal and gene: log2(TPM + 1) from the deposited TPM table. Per contrast, the control mean per gene; per knockout animal and gene the difference from that mean (log2 fold change); a signature value per animal is the mean over its genes; the contrast value is the mean over knockout animals, with every animal's value listed. Control noise: the same signature value for each control animal against the mean of the other control animals (leave-one-out). Reference-normalised signature = signature minus the REF_STABLE value of the same animal. No p-value across arms is the basis of a verdict (n is 2 to 4); an exact permutation count may be shown as description.

## Decision rules (written before the values; thresholds are not calibrated)
* **R-A, PV-specific pattern:** reference-normalised PV_SET at most -0.5, **and** reference-normalised LATE_NONPV and INT_NONPV each within plus or minus 0.2, **and** every knockout animal's PV_SET value below the lowest control animal's.
* **R-B, falls together (maturation delay or late-stage effect):** reference-normalised PV_SET at most -0.5 **and** reference-normalised LATE_NONPV at most -0.25 (the same sign and at least half the PV shift). This is the pre-registered STOP: no PV-specific lever follows.
* **R-C, no PV deficit in this contrast:** PV_SET above -0.5.
* **R-D, mixed or uninformative:** anything else.
* **Composition caveat:** if the oligodendrocyte guard mean is at most -1.0 or REF_STABLE moves by at least 0.3 in the knockout, the verdict is taken on the reference-normalised values and flagged composition-confounded; raw values are shown beside them.
* Applied to the primary contrast only (cortex S); other contrasts are reported with the same arithmetic as description.

## What this step cannot show
Cell number, cell identity, per-cell expression, protein or function; whether a PV deficit would be a cause, a consequence or a maturation effect of a lethal phenotype; independence from the held single-nucleus data; anything about people.
