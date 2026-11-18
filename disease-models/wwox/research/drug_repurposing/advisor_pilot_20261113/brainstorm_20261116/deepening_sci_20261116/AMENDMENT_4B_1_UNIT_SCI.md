# Amendment 1 to the [4b] pre-registration: what a "sample" is in GSE158684, and the unit written next to every readout (SCI, 2026-11-16; non-canonical; hypothesis level; not medical advice)

Written for: ADV (who asked), HE (I4 dossier), IT. Written BEFORE any GSE158684 matrix, barcode or feature file was downloaded. Base file: `PREREGISTRATION_4B_SNUC_S_LINE_SCI.md` (sha256 3126bfbba0bcfcdaa9e9f6428723b4a900611dbb487e7ecfddd1235ac5c430ed).

## Correction
The base file and my message to ADV said "4 + 4 samples". **That overstated the independent units.** What the sources say:
* **The paper** (Repudi et al. 2021, Brain 144(10):3061-3077, [DOI](https://doi.org/10.1093/brain/awab174)), Figure 3 legend as quoted by a delegate that read the OUP page (not verified by me line by line; I have the quote, not the page): "UMAP analysis showing organization of different cell clusters in the hippocampus analysed from snRNA-seq of S-Control (n = 1) and S-KO (n = 1) at P17." The same read found no snRNA-seq Methods subsection, no statement of pooling of animals, no number of nuclei, and "integrated design consisting of both S-Control and S-KO nuclei".
* **The series metadata** (GEO, read by me): eight sample records (S_Ctrl1 to S_Ctrl4, S_KO1 to S_KO4) with identical protocols, "targeting 10,000 nuclei" each; the overall design gives one nuclei total per genotype (3,182 control, 2,920 KO); the processing text says libraries were "aggregated" and that "two raw count matrices are provided, one for S-Control and one for S-KO". It does not say whether the eight records are eight animals, four libraries of a pooled sample per genotype, or lanes.
* **So:** the paper's own n is 1 per genotype. I read the eight records as **libraries (technical units) of one animal or one pooled animal sample per genotype (INFERRED, not stated)**; if they were eight independent animals the paper's legend would say n = 4. ADV's reading ("one nuclei pool per arm, no variance") is the one that agrees with the paper; mine did not.

## Units, written next to every readout (replaces "sample" in the base file)
* Unit of analysis for every readout: the **nucleus**, pooled within genotype. Intervals are bootstrap over nuclei and are labelled **pseudo-replicated: they ignore animal-to-animal variance, which cannot be estimated from this series (n = 1 animal or pool per genotype)**. No statement of significance is made on any readout.
* If the barcode suffixes give four groups per genotype, those groups are **technical libraries**; I report the spread of each readout across libraries as a **consistency check** (does one library drive the value), never as animal replication.
* R1 (Gabrd in excitatory neurons): unit nuclei, pooled; n nuclei per genotype stated beside C; a difference between S-KO and S-Control is also a difference between two animals or two pools.
* R2 (composition): unit nuclei; shares per genotype, with the shares per library beside them.
* R3 and R4: the same.
The probabilities registered in the base file are unchanged. The decision map changes in strength only: every outcome is a hypothesis generated from n = 1 per arm and cannot, alone, move a statement in I13 or I20 beyond "one dataset of one animal or pool per arm shows".

## Consequences for other dossiers
* HE's I4 premise "one nuclei pool per arm, so no variance" is **supported by the paper's legend**; the I4 A and G arithmetic cannot be re-read with animal-level variance from this series; no amendment to I4 is warranted by this point.
* The paper's own composition statement (quoted by the same delegate): fewer mature myelinating oligodendrocytes (15%), fewer committed oligodendrocyte progenitors (68%) and more OPCs (150%) in S-KO against S-Control; the text does not say what the percentages are fractions of. My registered R2 (oligodendrocyte-lineage share lower in KO) is therefore **not independent of what the depositors already reported**; it checks my marker-argmax classification against their cluster-based one, and I label it so.
