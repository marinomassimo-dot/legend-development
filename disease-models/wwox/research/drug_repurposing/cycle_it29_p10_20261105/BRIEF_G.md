# BRIEF G (IT29 P10, challenge CH-IT29-CLASSIIA-CNS-MYELIN)

Scientist G. First read `disease-models/wwox/research/drug_repurposing/cycle_it29_p10_20261105/BRIEF_COMMON_P10.md` (constraints and deliverables bind you) and `QUESTION.md` in the same folder. Your directory: `disease-models/wwox/research/drug_repurposing/cycle_it29_p10_20261105/p10_G/` (create it; write nowhere else). Evidence file: `evidence_it29_G.tsv`; event-id suffix `-08`.

## Your sub-question: the peripheral source (PMID 29472387) to completion, and catalytic v scaffold for class IIa in any myelinating glia

1. Read PMID 29472387 completely (PMC5881490 is the open copy named in the existing receipt): Methods, the full genotype table, figures described in text, Discussion. Extract exactly which genotypes were made and which showed a phenotype (Hdac4 alone, Hdac5 alone, double; Cre line and onset; germline v conditional), what the myelin readout was (transcript, g-ratio, electron microscopy, conduction), whether the authors state catalytic or scaffold (MEF2, NCoR/SMRT-HDAC3) mechanism, and whether the effect is on differentiation or on maintenance. Set `reread_reason` `new_question_outside_prior_coverage` and `prior_receipt` `FTR-20261105-29472387-06`.
2. Then read other Schwann-cell, peripheral-nerve or glial myelin work on class IIa HDACs (HDAC4/5/7/9; MEF2; HDAC3 with NCoR) that separates catalytic from scaffold function, including any catalytic-dead rescue or class IIa-selective inhibitor experiment in a myelinating cell.
3. State, row by row, which parts of the Schwann result could transfer to CNS myelination and which could not (cell type, timing, partner proteins), and what the same mutants would need to show to be a counter-reason for a catalytic inhibitor.

Already known, do not re-read: the IT28 P3 HDAC5 batch (muscle origin, HDAC4 neuronal catalytic-site mutant, potency discordance): `batch_it28_p3_hdac5_20261105/README.md`.

Stop when the genotype table of 29472387 is complete and either at most ten further sources are read or the Schwann/peripheral class IIa literature is exhausted. The deliverable includes the sentence to be carried in the records, in 25 words or fewer, naming genotype and tissue, e.g. what the decision-scope row should say in place of "HDAC4 and HDAC5 are required for Schwann cell myelination".

Also relevant (appeared after this brief was drafted): `phenotype_first_it29_20261105/p14_verify/origin_check.tsv` rows S1-29 and S1-30 flag that the signed-table action/direction for B38 (`loss` / `context_dependent`) disagrees with the evidence row (`loss of class IIa corepressors` / `adverse`). Your genotype table should settle which wording the source supports.
