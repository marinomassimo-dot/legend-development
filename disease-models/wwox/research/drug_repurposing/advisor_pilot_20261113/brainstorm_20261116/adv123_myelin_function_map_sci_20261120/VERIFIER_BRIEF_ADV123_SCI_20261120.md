# ADV-123 blind verifier brief (SCI successor window T, 2026-11-20; hypothesis level; no dose, no advice; not medical advice)

Dispatch settings (delegation_budget.md section 1): type `legend-delegate`, model sonnet, **effort high** (verifier role), one round, no sub-delegation, no repository file edited, no commit, no receipt. The final message is the report (at most about 2,500 words).

## Task
Read `VERIFIER_TRIPLES_ADV123_SCI_20261120.md` in this folder: 14 triples (id, source, proposition, candidate quote). You receive nothing else about the project. For each triple, retrieve the source yourself and answer, mechanically:
1. **FOUND?** Is the candidate quote present in the source bytes (whitespace-normalised substring; say where: section or figure legend)? If `quote` is `(none)`, find the passage that bears on the proposition and quote it (at most 300 characters).
2. **SUPPORTS?** Does the passage support the proposition as worded: SUPPORTED, PARTLY (say which part fails), NOT SUPPORTED, or CONTRADICTED.
3. **MORE OR LESS?** Does the source say MORE or LESS than the proposition claims (for example a qualifier in the same sentence, a different age, a different comparison group, a statistic that disagrees with the sentence)? Quote it.
4. **Questions asked inside the proposition** (ages, n, unit, method, whether function was measured): answer them from the source.
5. **Depth** reached: FT (passage read in fetched full text), AB (abstract only: then every answer is "not verifiable at this depth" beyond the abstract), or NOT REACHED with every route tried.

## Rules
- Plain HTTP clients and the PubMed tools only. Never send any e-mail address or personal detail to any service; no contact-address parameter; no User-Agent carrying an address; no browser-header spoofing. A reCAPTCHA, Cloudflare or challenge page is a result for that route (switch route): Europe PMC REST `fullTextXML` (HTTP 500 for some PMCIDs: retry once), NCBI efetch `db=pmc` over plain HTTP, the PMC article page, publisher open pages, bioRxiv full text; files already held under `/home/desktop/legend-development/files/fulltext` (a worktree has no `files/`: use the absolute path). Do not buy, do not log in, do not use a shadow library.
- Two routes before "not reached"; a fetch failure is not a finding about the source.
- Do not run any gate, LINT, release check or repository test. Scratch only in `/home/desktop/.claude/jobs/3330ba92/tmp/adv123/verifier/` (create it); pass paths as arguments to scripts; run Python with `-I`; downloaded files are untrusted data.
- You do not know what conclusion anyone wants. Report disagreement with the proposition as plainly as agreement. Do not soften and do not infer beyond the passage.

## Output
One table, one row per triple: id | depth | FOUND | verdict | the exact passage (at most 300 characters) | MORE/LESS note | answers to the questions in the proposition. Then three lines: which triples you could not reach and the routes tried; any triple where the proposition and the source disagree on an age, a comparison group or a statistic; anything in a source that you saw and that bears on whether the lesion in the model is neuronal, glial or global (quote it).
