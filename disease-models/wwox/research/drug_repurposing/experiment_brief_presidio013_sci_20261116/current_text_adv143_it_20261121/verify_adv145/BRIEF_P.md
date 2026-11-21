# Brief (cold reader, round 2) — ADV-145: can a collaborating laboratory work from the NEW current text without a call?

Model sonnet, effort high (stated at dispatch; read back with session_model_census.py). Do not start agents. No network, no e-mail or personal detail to anything.

## Who you are
The staff scientist of a rodent neurophysiology and seizure-phenotyping laboratory that was sent ONE document by a collaborator and asked whether the laboratory can run the proposed pup experiment. You have never seen this programme, its repository, its earlier notes, earlier versions of this document or its authors. You know ordinary methods (slice and in vivo electrophysiology, EEG, behavioural scoring, AAV delivery, genotyping, statistics, animal-welfare practice). You do not know the programme's abbreviations or internal labels unless the document explains them.

## Your only source
Exactly one file, read completely, in /home/desktop/.claude/jobs/6a8c1a55/tmp/adv145/ : DOCUMENT_CURRENT_pup_brief.md (it contains its own status box and its own History section). Do not open any other file on this machine, no web, no PubMed, no repository, nothing you remember about this programme. A fact not in the document does not exist for this task. A path or reference that points outside it is "reference not available to the laboratory".

## What to produce (write only into /home/desktop/.claude/jobs/6a8c1a55/tmp/adv145/out/)
1. RESULT.md, answer first, with these four items stated BEFORE anything else, each in its own short paragraph:
   (A) Can the laboratory start without a call: yes / no / only with named gaps closed, and the count of questions in QUESTIONS.tsv and how many of them you mark as blocking a start.
   (B) UNAIDED: which text governs and what it replaces, and where the earlier dated lines and superseded statements went. Answer from the document alone; quote the sentence(s) you rely on, or say that the document does not say.
   (C) The ten items that would most block a start, ranked.
   (D) Any conflict you find BETWEEN sections of this document (numbers, ages, arm names, definitions, which statement is in force) that the document does not itself mark as a conflict. A conflict the document marks with its own CONFLICT-OPEN line is not what is asked here; list it separately as "marked" with its id.
2. QUESTIONS.tsv: every question the laboratory cannot answer from the document alone. Columns: q_id, category (design | n_and_power | ages | genotype_and_controls | readouts | exposure_and_delivery | welfare_and_stopping | statistics | logistics | terminology | document_structure), the question in one sentence, where in the document the answer should have been (heading), what the document says instead (verbatim, short, or "nothing"), blocks_start (yes/no, one line why), nearest_marker (the id of the document's own OPEN-GAP or CONFLICT-OPEN line that covers this gap, e.g. Q12, or "none" if the document does not flag it).
3. CONFLICTS.tsv: columns c_id, location_1 (verbatim short quote with heading), location_2 (verbatim short quote with heading), the conflict in one sentence, flagged_in_document (yes with marker id / no), which one the laboratory would follow and why (or "cannot tell").
4. TERMS.tsv: terms of art or compressed phrases still needing plainer wording: t_id, term as written, where (heading), what you took it to mean (or "unknown"), proposed plain wording.
5. SEARCH_NOTES.md: how you read (passes, order), anything you could not read, confidence per list.

## Rules
- Quote verbatim and short. Never invent a number, age, dose or procedure to fill a gap; a gap is a gap.
- Do not judge the science or the programme's priorities; judge only whether a laboratory could execute from the text. No dose, schedule or clinical recommendation of your own.
- Chat reply: two lines pointing at the files.
