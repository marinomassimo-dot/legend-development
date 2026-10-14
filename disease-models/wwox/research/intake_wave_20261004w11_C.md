# Intake wave 11 (2026-10-04) — Scientist C, group C: restoration-spec and safety increments, fresh literature

context_policy: SOURCE_FIRST for all four readings (comparison with held records done only after each first pass). Nothing here is medical advice. No individual-level record.

Question assigned: what does each source add to, or limit in, the specification of a lawful WWOX restoration attempt (route, dose ceiling, biodistribution, toxicity of overexpression)?

Answer in one line: none of the four mentions WWOX; two add route-level or dose-method increments (PMID 42538560, PMID 42436860), one is a secondary pointer (PMID 42812991), one is an earned null for the gene (PMID 42807309).

| PMID | Verdict | Depth | What is new versus held | WWOX content |
|---|---|---|---|---|
| 42538560 | INGEST (route-level only) | partial | Choroid-plexus compartment gradient after single-site ICV in mouse; "choroid plexus" is in 0 of 1539 registry records | zero |
| 42436860 | INGEST (premise corrected) | partial | Peripheral-nerve AAV, not a CNS cassette; dose chosen at n = 2 per dose; legends, Methods and figure disagree on route, sex, n | zero |
| 42812991 | ABSTRACT-SUFFICIENT beyond a pointer role | partial | Review; names two primaries not held (NHP DRG detargeting; intracranial B-cell re-dosing); no dose table beyond Box 1 | zero |
| 42807309 | OFF-AXIS (earned null for WWOX) | partial | 16q23.1 signal attributed by the authors to CTRB1/CTRB2; WWOX never named | zero |

All four: no registry record existed (`registry_records.py get --pmid`), no prior receipt (`paper_packet.py packet`), PubMed carries no retraction/erratum/concern link (PMID 42538560 carries one comment-on link only).

## Per paper (class level, transfer limits exact)

**42538560 (Pooley et al., Fluids Barriers CNS 2026).** AAV2/ShH10 Y445F, 10 microlitre unilateral ICV into adult mouse. Low dose 3.5e10 genomes (EGFP), high dose 1.0e11 (SaCas9 and Aqp1 guides). Contralateral indel fraction about two thirds of injected (text; Fig. 5b panel about 13 vs 20 percent). AQP1 protein removal 59/39 percent (injected/contralateral, -0.15 mm), 78/54 (-1.8 mm), 45-49 (-2.1 mm), third ventricle about 37 percent then 26 percent not significant, fourth ventricle 3 percent not significant; recomputed from the Fig. 6 panel means, all within reading error. Dose, transgene, readout and time differ between the two in vivo experiments, so no dose effect is isolated. Transfer limit: mouse choroid-plexus epithelium, reporter and CRISPR payloads; route-level caution only. Candidate CC-20261004W11-C-CPDIST-01.

**42436860 (Itson-Zoske et al., Mol Ther Adv 2026).** Premise test: the selection called it a CNS cassette; it is a peripheral sensory-neuron programme (sciatic nerve). Dose 4e11 GC (20 microlitres, 2e13 GC per ml) per rat, from a two-rats-per-dose pilot, data not shown. DRG genome about 0.6-1.5 percent of sciatic-nerve copies (Fig. 5 panel). Safety read-out is naive-versus-treated histology and IHC; control-vector comparison is in the unread supplement. Internal inconsistencies recorded (route in legends, sex in Methods, n in Fig. 5). Transfer limit: rat, AAV6.2FF, peptide payload, peripheral route; no CNS dose ceiling. Candidate CC-20261004W11-C-PERIPHAAV-01.

**42812991 (Yu et al., Front Aging Neurosci 2026, review).** Secondary source. Statements carried only as "per the review". Recomputation flag: Box 1's fixed dose 1.4e14 gc at "about 3.4e11 gc/mL CSF" implies about 410 mL, above a usual adult CSF volume; no Box 1 dose is carried. Supplementary Table 1 not fetched.

**42807309 (Tan et al., World J Emerg Med 2026).** Common-variant, European-ancestry summary-statistics pleiotropy. 16q23.1 recurred in all four acute-pancreatitis/fat pairs; the paper assigns it to CTRB1/CTRB2 (figure also labels BCAR1). Colocalization names three loci without listing them in the text; an orange node sits at 16q23.1 on the intrapancreatic-fat branch of Figure 3. WWOX is absent from text and figure labels. The cytoband-level distance between those genes and WWOX was not measured here. Not a WWOX-DEE allele observation and says nothing about WWOX function.

## Comparison with held records (after the first pass)

- `CLAIM 047` holds four CNS AAV cassette bounds, including that route is not only a distribution parameter (a canine ICV-versus-ICM encephalitis statement). The choroid-plexus gradient is an increment, not a restatement.
- `DIS-033` (window not measured) is untouched by all four.
- PAPER 211/230/231 hold the DRG-immunosuppression series; PMID 42436860 adds no immunosuppression arm. Hordeaux 2020b (the detargeting primary) is not held.
- No held record mentions choroid plexus or tibial-nerve models.

## What would change the model, and what would falsify it

If a same-transgene dose series across ventricles showed contralateral and third/fourth-ventricle coverage rising with dose without toxicity, the route-level caution would weaken; a large-animal choroid-plexus map would test mouse-to-human scaling. Nothing in this group bears on the WWOX allele-class questions.

## Brief premises tested

Three of four selection sentences were wrong or unsupported: "ICV is the route a WWOX attempt would use" (a premise, not a held fact), "a CNS AAV cassette" (peripheral), "a recurrent signal at the WWOX locus" (not attributed to WWOX by the authors).

## Not read

Supplements of all four (not located or not fetched); Figures 1-4 images of PMID 42538560 and Figures 1-4 and 7 of PMID 42436860; Sections 3.1, 3.3, 4 and Table 2 of PMID 42812991; genetic-correlation and MR sections of PMID 42807309; reference lists (counts only).

## Artefacts

Manifests `disease-models/wwox/research/deepdive_manifests/PMID<pmid>.json` (all four PASS under `--verify-artifacts --require-current-schema`); dossiers `disease-models/wwox/research/fulltext_dossiers/PMID<pmid>.md`; candidates CC-20261004W11-C-CPDIST-01, -PERIPHAAV-01, -REGISTRY-01; receipts `scratchpad/receipts_pending_w11/sciC_<pmid>_1.json`.
