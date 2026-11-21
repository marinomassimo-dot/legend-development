# Brief (blind second reader) — RP-041: are the first reader's "unanswerable" questions really unanswerable?

Model sonnet, effort high (stated at dispatch; read back with session_model_census.py). Do not start agents.

## Your role
You are a second, independent staff scientist of a rodent neurophysiology and seizure-phenotyping laboratory. A colleague read two documents and wrote a list of questions that, in their view, cannot be answered from those documents. Your task is to test each question yourself.

## Your only sources (nothing else on this machine, no web, no PubMed)
In /home/desktop/.claude/jobs/6a8c1a55/tmp/rp041_blind/ :
- DOCUMENT_A_pup_brief_v2_consolidated.md
- DOCUMENT_B_invivo_experiment_brief_with_dated_lines.md
- QUESTIONS_ONLY.tsv (q_id, category, question; nothing else: you do not have the colleague's quotes, locations or judgements)
Do not open any other file or folder. In particular do not open /home/desktop/legend-development at all. A fact not in the two documents does not exist for this task. A path or link inside a document that points outside them is "reference not available to the laboratory".

## What to do
Read both documents completely first. Then, for EVERY question in QUESTIONS_ONLY.tsv, search the documents yourself and decide:
- ANSWERED: the documents give the answer unambiguously (quote the exact sentence, verbatim and short, with document and heading or dated-line number, and state the answer in one sentence);
- PARTLY: the documents give part of it, or give conflicting answers (quote what exists, say what is missing or which texts conflict);
- NOT ANSWERED: you looked in the places where it should be and it is not there (name the places you looked);
- UNCLEAR QUESTION: the question cannot be understood as written (say why).
Never invent a number, age, dose or procedure to fill a gap. Do not judge the science. Do not use any e-mail address or personal detail anywhere; no network.

## Output (write only into /home/desktop/.claude/jobs/6a8c1a55/tmp/rp041_blind/out/ ; create it)
1. VERDICTS.tsv: columns q_id, verdict (ANSWERED | PARTLY | NOT_ANSWERED | UNCLEAR), answer_or_gap (one or two sentences), locator (document + heading or line number), verbatim (short quote or "none"), places_searched (for NOT_ANSWERED and PARTLY).
2. RESULT.md, answer first: counts per verdict; list the q_ids you judged ANSWERED (these are where the first reader missed something); list any question that you would add (up to five) that a laboratory would need and that is not in the list (as new questions, same style).
3. NOTES.md: how you read; confidence; anything you could not read.
Chat reply: two lines pointing at the files.
