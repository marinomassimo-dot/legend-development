# Blind verifier report, verbatim: regional reach deciding rows (verifier: legend-delegate; brief stated model sonnet and effort high; read back by `framework/scripts/session_model_census.py` from the subagent transcript: model claude-sonnet-5-5, effort high)

The verifier received propositions only (no conclusions, no thresholds). Persisted from the session transcript. **Route result for the deciding source:** Voronin 2024 (PMC11489525) was NOT reached by the verifier by five routes (PMC page: reCAPTCHA; Europe PMC XML: HTTP 500; E-utilities: front matter only, publisher forbids XML full text; PubMed full-text tool: empty; Cell Press page: HTTP 403), and was not reached by me either (PMC page: reCAPTCHA; Europe PMC PDF render: "Just a moment" challenge). The producer reached the PMC page once without a challenge. The Table 2 numbers therefore rest on one reading (the producer's) and are not independently verified.

BLIND VERIFIER REPORT (sonnet, high). Working copies are in /tmp/bv_v20261121 (untrusted downloads, not in the repo). No e-mail or contact detail was sent anywhere; no browser header was spoofed.

SUMMARY: V4 is supported for the numbers and age; the denominator is not stated in the abstract. V5 is partly supported: no cortex or cerebellum value is printed, only a pooled range. V1 and V2 are NOT REACHED (full text of Voronin 2024 unreachable by any plain route). V3 is only partly checkable from the abstract.

ROUTES FOR VORONIN 2024 (PMC11489525)
- PMC article page https://pmc.ncbi.nlm.nih.gov/articles/PMC11489525/: route stopped: challenge (served the reCAPTCHA challenge page, 21337 bytes). The legacy URL www.ncbi.nlm.nih.gov/pmc/articles/PMC11489525/ gave the same challenge page.
- Europe PMC fullTextXML for PMC11489525: HTTP 500 Internal Server Error, tried twice.
- E-utilities efetch db=pmc id=11489525: returned only front matter and abstract (13 KB). The XML carries the comment "The publisher of this article does not allow downloading of the full text in XML form."
- PubMed full-text tool: returned full_text empty and the message "PMC sent no full text for PMC11489525". Abstract only.
- Cell Press page (cell.com ... S1525-0016(24)00464-8): HTTP 403 with a challenge page, route stopped: challenge. I did not look for the article at the Cell Press URL carrying its own PII S1525-0016(24)00467-2.
- That is five routes. Table 2 and the Results text were not reached.

V1 (Table 2 values, column order, headers, dose units): NOT REACHED. I cannot confirm or refute any number, the HPC / Cortex / Cerebellum column order, or the dose unit. The only dose text I read is the abstract: "Functional improvements were seen at doses of 3e11 to 5e11 vector genomes/g brain, which resulted in transfection of ≥50% of the neurons." That gives the unit as vg per g brain for the efficacious doses. It says nothing about Table 2.

V2 ("14%, 78%, and 61% ... cerebellum, hippocampus, cortex" sentence and its arithmetic): NOT REACHED. The sentence, its paragraph, and the two 3.0e11 Table 2 rows were not seen. For reference only, the arithmetic implied by the proposition's own numbers is: study 2 gives 33/30/10 and study 3 gives 123/73/18 (HPC/Cortex/Cerebellum). Means are HPC 78, Cortex 51.5, Cerebellum 14. That matches the quoted 78% (HPC) and 14% (cerebellum). It does NOT match 61% for cortex (51.5). This is the proposition against itself, not a source reading. Either the quoted text or the proposed table rows are off. Checking this needs the source.

V3 (vector, route, age, species): partly checkable. Abstract (PubMed/PMC, via efetch XML and the PubMed tool): "we designed a gene therapy vector, adeno-associated virus (AAV)9.Syn.hCDKL5, in which human CDKL5 gene expression is driven by the synapsin promoter. In biodistribution studies conducted in mice, intracerebroventricular (i.c.v.) injection resulted in broader, more optimal biodistribution than did intra-cisterna magna (i.c.m.) delivery." Also "i.c.v. delivery of AAV9.Syn.hCDKL5 to neonatal male Cdkl5 knockout mice".
- Supported at abstract level: AAV9 capsid, synapsin promoter, human CDKL5, mouse, i.c.v., i.c.m. compared, neonatal.
- NOT REACHED: "postnatal day 0" injection age, and the harvest age for the Table 2 rows. The abstract does not state either.
- The abstract says the promoter is "the synapsin promoter", not "human synapsin" (in the abstract).

V4 (McLean 2014, PMID 24882721) — SUPPORTED for the numbers and age; the denominator is not stated in the abstract.
- Route: efetch pubmed XML (eutils). The article is not in PMC (idconv: "Identifier not found in PMC"), so the abstract is the only reachable source.
- Verbatim: "We observed widespread GFP expression in neurons throughout the brain, spinal cord, and peripheral nerves and ganglia at 6 weeks-of-age. Region-specific quantification of GFP expression showed high neuronal transduction rates in substantia nigra pars reticulata (43.9±5.4%), motor cortex (43.5±3.3%), hippocampus (43.1±2.7%), cerebellum (29.6±2.3%), cervical spinal cord (24.9±3.9%), and ventromedial striatum (16.9±4.3%), among others."
- Also verbatim: "we employ the human synapsin 1 (hSYN1) gene promoter to drive neuron-specific expression of green fluorescent protein (GFP) after neonatal i.c.v. injection of rAAV9 in mice."
- All six numbers match. The abstract adds ± values, which are likely SEM, but the abstract does not say SEM or SD.
- Harvest age is 6 weeks. Injection age is only "neonatal" in the abstract.
- Denominator: the abstract says only "neuronal transduction rates". That presumably means GFP-positive neurons as a fraction of neurons (the paper's marker is not named in the abstract). This was NOT reached; the full text is needed.

V5 (Repudi 2021, EMBO Mol Med, PMC8649866) — percentages are given only as a pooled range. No cortex or cerebellum value is printed in the text or legends.
- Routes: Europe PMC fullTextXML (163 KB) and E-utilities efetch db=pmc (159 KB). Two independent byte streams. A regex scan for percent figures near cortex, cerebellum, hippocampus, NeuN or double-positive found only one hit, in both.
- Printed text: "Specific neuronal WWOX expression was detected in cortex (Figs 1D and 2D), hippocampus (Fig 2E), and cerebellum (Fig 2F) of P17‐P19‐treated mice. The percentage of NeuN and WWOX double‐positive cells was calculated and found to range between 60 and 70% (Figs 1E and 2G)."
- Legend Fig 1E: "Graph showing the percentage of NeuN and WWOX double‐positive cells in different parts of the brain (cortex, hippocampus, and cerebellum) from KO mice injected with AAV‐mWwox at P17. ... ( n = 3) brains." (Fig 1 harvest P17; AAV9-hSynI-mWwox, 2 × 10^10)
- Legend Fig 2G: "Graph represents the percentage of neurons showing the transgene (NeuN and WWOX positive) expression at different parts (cortex, hippocampus, and cerebellum) of the KO brain at P19 after AAV injection ... 3 identical sagittal sections ... ( n = 3) brains. ... Error bars represent ± SD."
- So there is no per-region printed number for cortex or cerebellum. The only printed value is the pooled "between 60 and 70%". Per-region values exist only as bars in the graphs, and I did not read them (no image reading done).
- Injection: Methods and Results state "injected into the ICV region of Wwox‐null mice at birth (P0)", and the doses are "2 × 10 10 /hemisphere". The proposition's route, age and construct (AAV9-hSynI, ICV, P0) are confirmed.
- Note: the legends call these constructs "AAV-mWwox" and "AAV-hWWOX". Fig 1 is the mouse Wwox construct and Fig 2 the human WWOX construct.