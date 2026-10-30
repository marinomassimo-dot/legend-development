# Correction note (2026-10-31), added by IT10 P5; the original files are not rewritten

Source: IT10 P2.2 (`axis_it10_p22_20261031/premises.tsv` PR1, self-audit `selfaudit_reread_output.txt`) and a re-read by the orchestrator of the publisher text (PMC7104842, Results 3.3 and Figure 4E) and of the repository copy `files/fulltext/PMID30290271_Hussain2019_PMC_r2.xml`.

## What the source says

Results 3.3 of Hussain 2019 (PMID 30290271): "We observed > 1.5 fold upregulation of both cytokines ( Il6 significant at p < .05) in Wwox KO ( n = 4) mice in comparison to Wwox WT (n = 4) mice ( Fig. 4 E )". Figure 4E: Il6 about 1.48-fold with one asterisk; Tnf-a about 1.85-fold with a large error bar and no mark (bar values read by eye from the figure image, not digitised). So **only Il6 is significant in the null hippocampus; Tnf-a is a non-significant increase.** The authors' own abstract ("overexpression of inflammatory cytokines Tnf-a and Il6") and Discussion ("increased expression of inflammatory cytokines Tnf-a and Il6") nevertheless state that both are increased, which their significance mark does not support; both statements are recorded.

## Items corrected by reference (originals unchanged)

1. `CHANGES.md` item 1 (this folder): the sentence quoted from the paper there omits the word "Il6", and the conclusion "Correct to: Il6 and Tnf-a both up" is **withdrawn**. The earlier registry/map reading "Il6, not Tnf-a" (and manifest entry 17 of `deepdive_manifests/PMID30290271.json`, anchor "il6 but not tnf-a") was right as to significance. The consequence stated there ("the need's direction statement and the J01 card/need counter-evidence that relied on 'Il6, not Tnf' should be re-read") is superseded: they were right and have been restored (IT10 P5: `needs/needs.json` NEED-NEUROINFLAMMATION-GLIA O1 and counter-evidence; card J01 DA-J01-002).
2. `seeds.tsv` **S085** (TNF, reason column): "Tnf-a transcript >1.5-fold up in the null hippocampus (p<0.05, paper section 3.3 ...); the registry reading 'Il6, not Tnf-a' in the needs table is wrong" is wrong on both counts. Read it as: Tnf-a increase, **not significant** (null hippocampus, n 4 v 4); the P47T cerebellum observation (at least two-fold, n 6, p<0.05, transcript, distributions overlap the wild-type range) is a separate observation and stands. The seed rows are left as stored (they feed the IT9 tables); the IT10 generation path removes the null-hippocampus origin from S085 in `generation_it10_p1_20261031/origin_overrides.tsv`.
3. `seeds.tsv` **S086** (IL6): "together with Tnf-a (S085)" should read "Tnf-a is not significant (S085)"; the Il6 observation itself is significant (about 1.48-fold, not strictly above 1.5).
4. Everything generated from S085 in IT9 inherits a non-significant null-hippocampus datum for the TNF arm: see `qualification_it9_p4c_d_20261030/CORRECTION_NOTE_IT10_20261031.md` for the qualification records (P4CD-01, P4CD-02, P4CD-04) and `axis_it10_p22_20261031/README.md` section 1 for voclosporin.

## Not changed

The Il6 seed, the P47T cytokine seeds (S084 and the P47T arm of S085) and the glial area-fraction rows. No IT9 decision is changed by this note; IT10 P5 did not re-examine whether any of them rested on the null-hippocampus Tnf-a significance alone (the decisive data recorded for P4CD-04 and the others do not name it).
