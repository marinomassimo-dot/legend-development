You are an independent blind verifier doing a blind locator audit of 3 proposition/quote/anchor triples about one open-access paper (Hussain et al. 2019, mouse hippocampus, Wwox knockout). You have seen no earlier audit, note or proposal about this paper and must not look for any: do not search the repository, open no file other than the files named below, use no web, no PubMed, no other paper. Run any Python with `python3 -I`, keep scratch files in your own temporary folder (none in the repository), and write no report file: your final message is the report. Do not contact anyone and do not send any personal data or contact details to any service.

Files (absolute paths):
1. The triples: /tmp/it59_c5b/triples_c005b.md
2. The source artefact (it governs): JATS XML /home/desktop/legend-development/files/fulltext/PMID30290271_Hussain2019_PMC_r2.xml (strip the tags yourself, or use file 3).
3. A plain-text rendering of file 2, one paragraph per line, table rows as `ROW: label | cell | cell`: /tmp/it59_c5b/h19_plain.txt (if it differs from the XML, the XML governs).
The figures of this paper are NOT held and no supplement is held: where a triple depends on them, say UNVERIFIABLE_SURFACE and name what is missing.

For each triple answer two mechanical questions and nothing else:
Q1. Does the quote support the proposition (does this sentence carry this claim)?
Q2. Does the source say MORE or LESS than the proposition claims? Search the whole article when the proposition could be contradicted or qualified elsewhere (Abstract, Highlights, Results, Discussion, Conclusions, figure legends can differ). For a proposition marked ABSENCE, search the whole text, name your search terms and the number of hits. Where the proposition is arithmetic or an inference from the source's numbers, say so. Check every number in a proposition against the number printed in the source (value, unit, group, panel).

Verdict labels: SUPPORTED; OVERSHOOT (the proposition says more than the source); UNDERSHOOT (it says less, or leaves out something the source says that changes its meaning); NOT_IN_SOURCE; UNVERIFIABLE_SURFACE (figure or supplement only and you cannot read it: declare it as an attestation).

Output, as your final message: (a) a table `# | Verdict | one-line reason`; (b) under it, for every triple that is not SUPPORTED, the exact words of the source that make it more or less (copy them; do not paraphrase); (c) one line naming anything you could not judge and why. Hard cap: 1,800 words; if you exceed it, say so in your first line. Do not state your own model or effort (the harness reads them back).
