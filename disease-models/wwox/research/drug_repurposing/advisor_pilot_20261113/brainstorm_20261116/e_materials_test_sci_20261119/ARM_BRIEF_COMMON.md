# Common brief for both arms (identical text; SCI, 2026-11-19; hypothesis level; no dose, no clinical recommendation; not medical advice; reference genotype class: WWOX loss of function in developmental and epileptic encephalopathy)

You are a scientific delegate. Do not start agents. Send no personal, account or contact data to any service; if a service shows a challenge or CAPTCHA, stop that route (no repeated attempts, no browser). Use lawful open routes only.

## The decision (identical for both arms)
Does the **WWOX WW1-domain / PPxY-motif partner branch**, with **ERBB4 and NETO2 proposed as partners of interest in neurons and interneurons (proposed, not established)**, justify (a) a pharmacological comparison, (b) a distinct experiment, or (c) neither, and which? Search for any other neural partner the evidence supports; do not limit yourself to the two names.

## Answer these six questions
1. Which interactions are **direct** (binding shown with a defined WW domain, motif, species and assay) and which are **only proposed or inferred** (motif scan, yeast two-hybrid not confirmed, co-expression, text mining)?
2. Which were **observed in pertinent neural systems** (state species, preparation, cell type, age, genotype)?
3. Which **functional consequences** were measured (endpoint, direction, size, n), and which are only claimed?
4. Does an **interpretable pharmacological lever** exist: the compound class, the action and its direction, the selectivity, the alternative actions of the compound, and the difference between a repurposing drug and an experimental probe?
5. Which **signs, functions or transfers are not supported** (across species, age, cell type, disease)?
6. Can the result **improve a pharmacological comparison or generate a distinct experiment**? For any hypothesis you keep, write the chain: observation, relation, hypothesised action, context, pharmacological comparison, prediction, the result that would reject it. "No compound is justified yet" is an allowed answer if you name the measurement that would change the choice.

## Rules of evidence
* Abstracts only locate sources. A substantive claim needs the **complete original opened lawfully** (open full text in PMC or Europe PMC, publisher open access, or a preprint); read the Methods, figure legends and table cells that carry the claim. A claim you could only support from an abstract or a secondary description must be marked "abstract only" or "secondary".
* Keep species, preparation, cell, age, genotype and endpoint explicit for every claim. An absence claim ("no study shows X") must state the search perimeter (databases, queries, dates).
* Do not promote a proposed interaction to a direct one, and do not transfer a sign or function across species, age or cell type without saying so.

## Budget and format (the same for both arms)
* At most **60 tool calls** in total (every Read, Bash, search, fetch counts). Count them as you go; stop at the cap and say what was left undone.
* The final report is one markdown file of at most **2200 words** including its table, with exactly these sections: `Decision`, `Q1` to `Q6`, `Search perimeter`, `Pivotal claims` (a table: claim | source (first author, year, journal) | locator (figure, table or section) | depth: full text / abstract only / secondary), `Limits`.
* Write the report to the output path given in your dispatch, nothing else outside it.
