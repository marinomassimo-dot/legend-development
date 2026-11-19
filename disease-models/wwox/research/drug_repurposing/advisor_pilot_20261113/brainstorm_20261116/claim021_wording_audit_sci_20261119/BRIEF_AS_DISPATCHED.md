# Brief as dispatched to the blind verifier (SCI, 2026-11-19, ADV-082; hypothesis level; not medical advice)

Dispatch settings asked: `legend-delegate`, model sonnet, effort high (read back afterwards with `framework/scripts/session_model_census.py`: sonnet x8, effort high x8).

You are an independent blind verifier doing a blind locator audit of 25 proposition/quote/anchor triples about one open-access paper (Breton et al. 2021, Neurobiology of Disease, mouse slice electrophysiology). You have seen no earlier audit, note or proposal about this paper and must not look for any: do not search the repository, open no file other than the files named below, use no web, no PubMed, no other paper. Run any Python with `python3 -I`, keep scratch files in your own temporary folder (none in the repository), and write no report file: your final message is the report. Do not contact anyone and do not send any personal data or contact details to any service.

Files (absolute paths):
1. The triples: `/home/desktop/.claude/jobs/22f2465c/tmp/triples_021_for_delegate.md` (a neutral path on purpose; `TRIPLES_FOR_AUDIT.md` in this folder is a byte-identical copy kept for the record)
2. The source artefact (it governs): `/home/desktop/legend-development/files/fulltext/PMID34634460_Breton2021_EPMC_2026-09-27.xml` (JATS XML; strip the tags yourself, or use file 3).
3. A plain-text rendering of file 2, one paragraph per line, table rows as `row label | cell | cell`, with the table footnote (if it ever differs from the XML, the XML governs): `/home/desktop/.claude/jobs/22f2465c/tmp/breton_plain.txt` (not shipped: a third-party text; regenerate with `render_breton_plain_sci_20261119.py`)
4. Figures, to be opened as images (gr1 = Fig 1 ... gr6 = Fig 6): `/home/desktop/legend-development/files/figures/PMID34634460_r2/gr3.jpg`, `gr4.jpg`, `gr6.jpg`. The supplementary material (Supplementary Table S1, Figs S1 to S4) is NOT held: where a triple depends on it, say UNVERIFIABLE_SURFACE and name what is missing.

For each of the 25 triples answer two mechanical questions and nothing else:
Q1. Does the quote support the proposition (does this sentence carry this claim)?
Q2. Does the source say MORE or LESS than the proposition claims? The quote is not the only passage that matters: search the whole article when the proposition could be contradicted or qualified elsewhere (the Summary/Abstract, Highlights, Results, Discussion, Conclusions and figure legends can differ). For a proposition marked ABSENCE, search the whole text, name your search terms and the number of hits. Where the proposition is arithmetic or an inference from the source's numbers rather than a statement of the source, say so. Where a value comes from a figure, say what is printed in the cell (value and asterisks) or that you cannot read it. Check every number in a proposition against the number printed in the source (value, unit, group, panel), and say if a number or a group label is attributed to a place where it is not printed.

Verdict labels: `SUPPORTED`; `OVERSHOOT` (the proposition says more than the source); `UNDERSHOOT` (it says less, or leaves out something the source says that changes its meaning); `NOT_IN_SOURCE`; `UNVERIFIABLE_SURFACE` (figure or supplement only and you cannot read it: declare it as an attestation).

Output, as your final message: (a) a table `# | Verdict | one-line reason`; (b) under it, for every triple that is not SUPPORTED, the exact words of the source that make it more or less (copy them; do not paraphrase); (c) one line naming anything you could not judge and why. Hard cap: 1,800 words; if you exceed it, say so in your first line. Do not state your own model or effort (the harness reads them back).
