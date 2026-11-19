# Brief as dispatched to the blind verifier (SCI, 2026-11-19, ADV-081; hypothesis level; not medical advice)

Dispatch settings asked: `legend-delegate`, model sonnet, effort high (read back afterwards with `framework/scripts/session_model_census.py`).

You are an independent blind verifier doing a blind locator audit of 22 proposition/quote/anchor triples about one open-access paper. You have seen no earlier audit, note or proposal about this paper and must not look for any: do not search the repository, open no file other than the four named below, use no web, no PubMed, no other paper. Run any Python with `python3 -I`, keep scratch files in your own temporary folder (none in the repository), and write no report file: your final message is the report. Do not contact anyone and do not send any personal data or contact details to any service.

Files (absolute paths):
1. The triples: `/home/desktop/.claude/jobs/7fa05322/tmp/triples_for_delegate.md` (a neutral path on purpose; `TRIPLES_FOR_AUDIT.md` in this folder is a byte-identical copy kept for the record)
2. The source artefact (it governs): `/home/desktop/legend-development/files/fulltext/PMID33520443_Baryla2021_PMC7811782_refetched_20261119.xml` (PMC XML of Baryla et al. 2021, PeerJ; strip the tags yourself, or use file 3).
3. A plain-text rendering of file 2, one paragraph per line, for convenience (if it ever differs from the XML, the XML governs): `/home/desktop/.claude/jobs/7fa05322/tmp/baryla_plain.txt`
4. Figures, to be opened as images: `/home/desktop/legend-development/files/figures/PMID33520443/peerj-09-10604-g002.jpg` (Fig 2), `.../peerj-09-10604-g004.jpg` (Fig 4, GDM group correlations), `.../peerj-09-10604-g005.jpg` (Fig 5, NGT group correlations). The supplementary table is in `.../peerj-09-10604-s001.docx`; open it only if a triple cannot be judged without it.

For each of the 22 triples answer two mechanical questions and nothing else:
Q1. Does the quote support the proposition (does this sentence carry this claim)?
Q2. Does the source say MORE or LESS than the proposition claims? The quote is not the only passage that matters: search the whole article when the proposition could be contradicted or qualified elsewhere (the Abstract, Results, Discussion and Conclusions can differ). For a proposition marked ABSENCE, search the whole text, name your search terms and the number of hits. Where the proposition is arithmetic or an inference from the source's numbers rather than a statement of the source, say so. Where a value comes from a figure, say what is printed in the cell (value and asterisks) or that you cannot read it.

Verdict labels: `SUPPORTED`; `OVERSHOOT` (the proposition says more than the source); `UNDERSHOOT` (it says less); `NOT_IN_SOURCE`; `UNVERIFIABLE_SURFACE` (figure only and you cannot read it: declare it as an attestation).

Output, as your final message: (a) a table `# | Verdict | one-line reason`; (b) under it, for every triple that is not SUPPORTED, the exact words of the source that make it more or less (copy them; do not paraphrase); (c) one line naming anything you could not judge and why. Hard cap: 1,400 words; if you exceed it, say so in your first line. Do not state your own model or effort (the harness reads them back).
