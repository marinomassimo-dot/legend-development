# Brief (cold reader) — RP-041: can a collaborating laboratory work from this pup brief without a call? (IT, 2026-11-21)

Role: producer acting as a COLD READER. Model sonnet, effort high (stated at dispatch; read back with session_model_census.py). Do not start agents.

## Who you are for this task
You are the staff scientist of a rodent neurophysiology and seizure-phenotyping laboratory that has been sent two documents by a collaborator and asked whether the laboratory can run the proposed pup experiment. You have never seen this programme, its repository, its earlier notes or its authors. You know ordinary methods (slice and in vivo electrophysiology, EEG, behavioural scoring, AAV delivery, genotyping, statistics, animal-welfare practice). You do NOT know the programme's abbreviations, internal labels or what any dated update line "updates" unless the documents say it.

## Your only sources
Exactly two files, read completely, in /home/desktop/.claude/jobs/6a8c1a55/tmp/rp041_cold/ :
- DOCUMENT_A_pup_brief_v2_consolidated.md
- DOCUMENT_B_invivo_experiment_brief_with_dated_lines.md
Do not open any other file on this machine, do not search the web or PubMed, do not read the repository, and do not use anything you remember about this programme. A fact not in the two documents does not exist for this task. If a link or path in a document points outside the two files, record it as "reference not available to the laboratory" and do not follow it.

## What to produce (write only under /home/desktop/legend-development/.claude/worktrees/it_successor_q_20261121/disease-models/wwox/research/drug_repurposing/rp041_cold_read_it_20261121/output/)
1. RESULT.md, answer first: can the laboratory start without a call (yes, no, only with named gaps closed), the count of items in each list below, and the ten items that would block a start, ranked.
2. QUESTIONS.tsv: every question the laboratory cannot answer from the documents alone. Columns: q_id, category (design | n_and_power | ages | genotype_and_controls | readouts | exposure_and_delivery | welfare_and_stopping | statistics | logistics | terminology | document_structure), the question in one sentence, where in the documents the answer should have been (document and heading or dated-line number), what the documents say instead (verbatim, short), blocks_start (yes/no, one line why).
3. CONFLICTS.tsv: every conflict or tension between a dated update line and the text it updates, or between the two documents, or inside one document (numbers, ages, arm names, which line supersedes which, a statement later withdrawn but still standing elsewhere). Columns: c_id, location_1 (verbatim short quote), location_2 (verbatim short quote), the conflict in one sentence, which one the laboratory would follow today and why (or "cannot tell"), proposed repair in one sentence.
4. TERMS.tsv: every term of art, abbreviation, internal label or compressed phrase that needs a plainer form for a laboratory reader. Columns: t_id, term as written, where, what you took it to mean (or "unknown"), proposed plain wording.
5. FOLDIN_PROPOSAL.md: a PROPOSAL (not an edit of either document) of how a clean current text could be assembled: an outline of the sections a laboratory needs in order, which dated lines fold into which section, which statements are superseded and should move to a history section (old text kept there), and what must be stated that no line states today.
6. SEARCH_NOTES.md: how you read (order, passes), anything you could not read, and your own confidence per list.

## Rules
- Quote verbatim and short when you cite. Never invent a number, age, dose or procedure to fill a gap; a gap is a gap.
- Do not judge the science, the hypotheses or the programme's priorities; judge only whether a laboratory could execute from the text. No dose, schedule or clinical recommendation of your own.
- Do not use any e-mail address or personal detail anywhere; zero spend; no network access is needed.
- Your chat reply: two lines pointing at the files.
