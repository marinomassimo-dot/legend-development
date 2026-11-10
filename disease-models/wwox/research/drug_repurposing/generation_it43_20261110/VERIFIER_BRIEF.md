# IT43 independent reader: brief

You are an independent reader (sonnet, high effort, one delegate). You have NOT been given the verdicts of the search engine and must not look for them: do not read `search_rows.tsv`, `molecules.tsv`, `compound_decisions_it43.tsv`, `eval_results.tsv`, `result_it43.md` or any file whose name contains verdict, qualification or eval. Work only from the files named here and the primary sources.
Rules: zero spend; do not send, search for or store any e-mail address or contact detail; no service that asks for a contact address. Not medical advice. Read-only toward the repository except your one output file. Say "not reached" when a source is not reached; unknown is not negative.

## Part 1: S9 rows (`verify/s9_rows.tsv`, 10 rows)
Question: pyruvate dehydrogenase kinase (PDK1-4) inhibition. For each row state, from the row and, where the PMID is given, from the abstract (PubMed tools): (a) is the recorded action an inhibition of the kinase named (yes / no / unclear) and why; (b) the recorded species; (c) whether the affinity is one datum or two representations of one datum; (d) whether the two sets of affinities (rows from PMID 14641019 and PMID 25404640) come from the same assay type and so may be compared, with the assay words quoted.

## Part 2: four decisive statements (read the PubMed abstract or full text; quote the words)
1. PMID 16476929: the randomised trial of dichloroacetate in MELAS: how many were randomised, how many in each arm stopped study drug, the stated reason, and whether efficacy was judgeable. (A prior note says 15 of 15 against 4 of 15 and 17 of 19 discontinuations for neuropathy: confirm or correct; say what the abstract does not give.)
2. The symbol PDK1 is used both for pyruvate dehydrogenase kinase 1 and, historically, for 3-phosphoinositide-dependent kinase 1 (PDPK1). Find one source that states this and quote it.
3. In `generation_it43_20261110/dgidb_rows_it43.tsv` read only the rows with relation_id S9 and the columns name, gene, interaction_type, claim_source. For the compound named devimistat (and for celecoxib and OSU-03012) say, from a primary or reference source you reach, whether its reported target is the pyruvate dehydrogenase kinase, the other kinase, or something else; if not reached, say so.
4. AZD7545 (PMID 14641019): which isoforms does the abstract report, and does it state anything about PDK3 or PDK4?

## Part 3: sample of 30 rows (`verify/sample_rows.tsv`, relations S2 HCN and S4 connexin/pannexin, drawn at random with a fixed seed)
For each row: does the recorded action fit "block / negative modulation" of the named channel (direction relative to a blocker being wanted), is the molecule a distinct structure or a salt/duplicate of another row, and is any identity doubt visible (two different molecules sharing a name)? Use catalogue knowledge only where you can cite a source; otherwise write "not checked".

## Output
One file: `generation_it43_20261110/verify/VERDICTS.md`: a table per part, every cell with SUPPORTED / CORRECTED / NOT_REACHED and the quoted words; at the end list every disagreement with the rows as given, most important first. Keep it under 250 lines. Report the number of tool calls you made.
