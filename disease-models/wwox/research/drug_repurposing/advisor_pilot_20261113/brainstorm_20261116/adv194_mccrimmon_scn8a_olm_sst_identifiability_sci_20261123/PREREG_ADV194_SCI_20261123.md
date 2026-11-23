# ADV-194 pre-registration (SCI, written before the body of the source was opened; hypothesis level; no treatment claim; not medical advice)

analysis_at: 2026-11-23T10:09Z (written before any byte of the McCrimmon text, figures, Methods, supplement or tables was read)
task: ORCH-SCI-ADV065-DEEPEN-20261118, accepted step 87 for assignment ADV-194 (assignments/ADV-194.md, Codex independent review 14)
source: McCrimmon et al., Cell Reports 2025, PMID 40925365, PMC12674601, DOI 10.1016/j.celrep.2025.116217

## 1. What has been seen BEFORE this file

* The text of assignment ADV-194 and ADV's message: the question (is the reported O-LM/SST relationship a worked example of selecting a discriminator for in-silico circuit models, or does it show that a model with enough adjustable parameters reproduces known outcomes), the provenance categories to map, and the Codex screen as relayed (model and single-nucleus Methods passages only; ADV warns its description can contradict the figures). I have taken the Codex description as a lead, not as a reading of the paper.
* The held comparators as quoted in the assignment: HE ADV-153 Rule 1 (a rival enters a circuit pilot only if, after its own re-fit, it reproduces the two held numbers within the held interval with the free parameter declared), the RP-045 row (pilot only on triggers (i) to (iii) AND a built structural rival re-fitted to the held numbers; READOUT TYPE / CLAIM TYPE line) and the predictive synthesis. I have not yet opened those three files myself: they are opened before any line is proposed (section 4).
* Step 0 only (names and sizes; nothing opened): the PMC open-data bucket PMC12674601.1 lists 23 objects. Downloaded unread into a scratch folder: the article .txt (105 585 B), .xml (269 272 B), .json (2 826 B), .pdf (3 686 233 B); eight figure jpg files (f0001 to f0008, 259 892 to 1 026 664 B); the supplement PDF "Figures S1 to S7 and Table S1" (16 838 910 B) and Tables S2 to S5 (xlsx, 98 819 to 4 327 470 B). NOT downloaded: six supplementary videos (5.9 to 36.5 MB) and nothing from GEO (GSE281622 is not touched). SHA-256 first 12 hex: txt 7cc137ac8449, xml ea2ee7bcf33a, pdf b01c22ad5aba, f0005 b97fef13276c, f0006 95bd823f0f78, f0007 3f3172068032, supplement pdf b122cb169b3b, Table S3 bba9447bd598.
* Note for the reader: the bucket has EIGHT figure files; the assignment says Figures 5 to 7. The mapping of file to figure number is settled from the captions, not assumed.
* I have NOT opened the body, any figure, the supplement or any table.

## 2. The quantities the question needs (fixed before reading)

For every number or image the model depends on, one row: what it is, which preparation, who set it, and its role. Roles are closed to six: SET (taken as an input before fitting), CALIBRATED (control data used to fix a baseline), FITTED (mutant output the free variables were adjusted to match), FREE (a variable the authors allowed to move), PREDICTED (a model output compared afterwards with a measurement not used to set or fit it), UNUSED (measured and not entered). The question is then which measurements are PREDICTED or UNUSED rather than SET or FITTED. Also fixed: what the final staining or single-nucleus count DIRECTLY measures (a marker fraction, a cell count and a lineage identity are three different quantities).

## 3. Readings (stated now; each falsifiable by the body)

* **Reading F ("fit and confirm", my expected outcome, 0.50):** cell numbers or conductances were set from a preliminary immunostaining and the mutant theta measures were fitted; the later staining or snRNA confirms the SAME quantity that supplied the model's prior (a marker fraction), so it is a restatement, not a test; composition-only and conductance-only versions were tested only as one-parameter reversions inside the combined fitted model.
* **Reading K ("out-of-fit readout", 0.15):** at least one measurement (a direct intrinsic-current recording, or a lineage-resolved count) was entered neither as a setting nor as a fit target, and it separates composition-only from conductance-only versions that were each re-fitted.
* **Reading P ("pooled libraries", 0.20, can coexist with F or K):** the single-nucleus comparison in Fig 7 pools three differentiations into one library per condition; the nuclei are then not independent units for a genotype conclusion, whatever the nucleus-level p value.
* **Reading D ("already covered", 0.15):** the content adds nothing to Rule 1 plus the READOUT TYPE / CLAIM TYPE line of RP-045.

## 4. Fixed exits

* **KEEP** only if Reading K holds: a measurement that is PREDICTED or UNUSED, with a defined unit and with a contrast that differs between at least two constrained rivals each re-fitted; then ONE measure or condition is nominated for the RP-045 note.
* **NARROW** if Reading F holds (with or without P): the limit (an apparently confirming measurement that shares its biological source or structural assumption with what set the model confirms nothing about the alternatives) and ONE rule line for a future prospective case, written only after the RP-045 row, Rule 1 and the synthesis are opened and found NOT to carry it.
* **CLOSE** if Reading D holds, or if the paper offers no mapping that the repository lacks, with the reason and the covering lines named.
* A model reversion ranks sensitivities inside the chosen model; it cannot by itself establish mechanism or exclude rivals. What the authors REPORT is kept in one column and what LEGEND would INFER in another. No SCN8A treatment claim, no transport to WWOX, no LEGEND predictive-validation claim, no new simulation, package, score, model training or dashboard change, no download or reanalysis of GSE281622, no WNT work, no message to the Codex science lane.
* **Reading order:** the .txt in full (cut at the reference list), the .xml only for sentences the .txt flattened (STAR Methods tables); the figure files as images, panel by panel; the supplement PDF and Tables S2 to S5 by name and header first; the PDF only to settle a conflict. A challenge page, 403 or 429 is a route result.
