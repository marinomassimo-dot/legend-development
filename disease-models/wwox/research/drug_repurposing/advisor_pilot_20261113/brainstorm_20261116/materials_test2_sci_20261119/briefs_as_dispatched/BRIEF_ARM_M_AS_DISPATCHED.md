You are a delegate for one bounded scientific question. Hypothesis level only: no dose, schedule or recommendation for any agent in any person; this is not medical advice. Reference genotype class: WWOX loss of function (developmental and epileptic encephalopathy; mouse models). Reply in English. Write no files: your final message is the report. Send no e-mail address, name or other personal or contact data to any service, and use no contact-address parameter in any request.

Settings for this run: model sonnet, effort medium. At most 60 tool calls in total. Final report at most 800 words. One run; you will not see any other delegate's work.

THE QUESTION
A laboratory studies a mouse model of WWOX loss of function. Beyond its main experiments it could add one of six optional measurements, but it can take only ONE. Which one should it take first, and in what order would you rank the six? The answer is a conditional, hypothesis-level line of the form "if a laboratory can take only one optional measurement, take X first, because ...". No laboratory is named and none is asked to do anything.

The six measurements, listed in a fixed order (the position in this list carries no meaning):
1. Glucose tied to seizure timing (seizure-and-death lines, at seizure time, ketone and lactate by age, milk intake)
2. EEG or ECoG before P14
3. PV count and signal per cell, late-maturing marker, myelin marker at two ages
4. Structural myelin endpoints (EM counts, g-ratio, MBP, CC1)
5. Heterozygote carrier latency
6. Callosal conduction re-measurement, rescue arm, animal-level statistics

WHAT TO RETURN (one fixed format; at most 800 words in total)
1. Your order of the six, first to last, using the names above.
2. For each of the six: what it could change (which decision or hypothesis) and what it needs (preparation, age, animals, controls).
3. One sentence: what would change your order.
For each fact that decides the order, say where it comes from: a held original named below (file and locator), another source you found (PubMed id or URL), or "from memory". When you can, check a claim against an original before relying on it.

HOW TO WORK
Your material is what this brief lists and nothing else from this repository: open only the files and folders named in this brief (Read, Grep, Glob and Bash must stay inside those paths; do not search the rest of the repository). Ignore the repository's session-start routine: this brief replaces it. PubMed and the web are allowed. Run any Python as `python3 -I`. The folder /home/desktop/legend-development/files/ is a shared, read-only root.

HELD ORIGINALS (the same list for every delegate; paths are absolute)
Root: /home/desktop/legend-development/files/
- Repudi 2021, Brain (PMID 33914858), neuron-targeted deletion paper: fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf and its text layer fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt; supplement folder fulltext/PMID33914858_Repudi2021_Brain_operator_supplied_supplement/ (extracted/awab174-suppl_data and the .zip).
- Cheng 2020 (PMID 32000863): fulltext/PMID32000863_Cheng2020_PMC.xml; supplement fulltext/PMID32000863_Cheng2020_supplementary.pdf; figures fulltext/PMID32000863_Cheng2020_assets/.
- Hussain 2023 (PMID 36828035): fulltext/PMID36828035_Hussain2023_PMC.xml and fulltext/PMID36828035_Hussain2023.pdf; figures fulltext/PMID36828035_Hussain2023_assets/; supplement folder supplement/PMID36828035/ (Supplementary_figures.pdf, Supplementary_data.xlsx, Supplementary_gene_data.xlsx, Supplementary_tables.docx, Supplementary_data_all_sheets_derived.txt).
- Abu-Remaileh 2019 (PMID 30755385): fulltext/PMID30755385_AbuRemaileh2019_PMC_r2.xml.
- Suzuki 2009 (PMID 19500159), held at abstract level only: fulltext/origin_it_20261117/abstract_19500159.txt.

ADDITIONAL MATERIALS FOR THIS RUN (project working notes and records; open these in addition to the held originals; they are statements by the project, not originals)
Worktree root: /home/desktop/legend-development/.claude/worktrees/sci-test2-materials-20261119/ (call it W; paths below are relative to W unless they start with /)
Folder N = W/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116
- Needs (verbatim extract of the two needs, with the file's reading rules and vocabularies): /home/desktop/.claude/jobs/8846a6c0/tmp/pack/needs_two_entries_verbatim.json (NEED-INHIBITORY-HYPOFUNCTION, NEED-SYSTEMIC-GLYCAEMIA-GROWTH; source file disease-models/wwox/research/drug_repurposing/needs/needs.json).
- Cards: disease-models/wwox/research/drug_repurposing/cards/F02_myelination_activity_sign.card.json; .../H02_gabaat_inactivator_myelin_exposure.card.json; .../E04_ketogenic_lactate_axis.card.json (the .packet.json files beside them are not part of your material).
- Open-question rows (verbatim rows with the file's header): /home/desktop/.claude/jobs/8846a6c0/tmp/pack/open_question_rows_verbatim.tsv (IT59-Q02, IT59-Q03, IT59-Q04, RS-NP3A1).
- Arm-table notes with their dated lines: N/ARM_TABLE_V9_NOTES_IT_20261117.md.
- Working notes: N/adv068_pv_per_animal_sci_20261119/PV_PER_ANIMAL_RESULT_ADV068_SCI_20261119.md; N/adv070_stage_adjusted_p3a_sci_20261119/STAGE_ADJUSTED_REREAD_RESULT_ADV070_SCI_20261119.md; N/h_glucose_axis_adv074_sci_20261119/GLUCOSE_METABOLIC_AXIS_FIRST_PASS_ADV074_SCI_20261119.md; N/i_deletion_completeness_olig2_adv076_sci_20261119/DELETION_COMPLETENESS_AND_OLIG2_ADV076_SCI_20261119.md; N/harm_against_phenotype_adv079_sci_20261119/HARM_AGAINST_PHENOTYPE_ADV079_SCI_20261119.md.
- Heterozygote register note: N/hussain_s2_s6_het_register_sci_20261119/HETEROZYGOTE_REGISTER_SCI_20261119.md.
Not part of your material: any ordering page, coverage table or other file that ranks these measurements, including anything the notes above may point to for that purpose. Do not open such files.
