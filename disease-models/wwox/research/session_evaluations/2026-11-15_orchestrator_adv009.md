# Session self-evaluation: ADV-009 (orchestrator, 2026-11-15)

Non-canonical. Process diagnosis. Not medical advice.

## Executable verdict
`session_self_eval.py --workspace . --disease wwox`: PASS. `legend_lint.py`: WARN (older findings, none from this package). `public_release_gate.py`: exit 0 (REVIEW lines are older records). Task record `ledger/tasks/orchestrator/ORCH-ADV009-20261115.json` carries the battery on the landing SHA. No ledger receipt was written: the reads are targeted passages of two PMC pages (listed in `readings.tsv`), not complete readings, and no PAPER record or baseline is touched.

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Premise test | WO-25's "no later record found" and compare_it28's "isoform reach of efonidipine not documented" were wrong at abstract level: Furukawa 2009 (PMID 19401195) states a three-isoform pattern and had been indexed since 2009; the "three PMC sources" were three different questions (one was TTA-P2) | strong | the full text of that paper is not reachable by a free lawful route here |
| Route facts | efetch returns front matter only for these publisher-restricted items; the PMC article web page returned the body for 2 of 3 and a reCAPTCHA for the third (stopped, one request); the bucket returned 404 for the three pair papers | useful | the route fact is not yet in `framework/scripts/README.md` §13 (proposed in consumer_delta row 5) |
| Verification | no blind verifier (the assignment left it to my judgement); a mechanical quote check, 16 of 16 rows found in the saved pages. This does not test interpretation | weak | the "opposite directions" reading, the 4-7 fold and 90-fold ratios and the reading of "not alpha1I" as not significant rest on me alone |
| Inference restraint | the "pair could separate isoforms" step is stated as shape of a contrast, not a result, because it joins an abstract-level oocyte significance to a patch-clamp Kd | adequate | needs the oocyte values |
| Consumption | consumer_delta.md for the integrator; no shared consumer edited | pending | benefit unproven until IT consumes it |

## Process diagnosis
* My mistakes, caught by me on re-read: I typed one SHA-256 into `access.tsv` by hand and it was wrong; I also wrote an author name for the hERG paper that the record does not give. I cross-checked every digest in the table against the files (15 of 15 real) and removed the name. Cause: composing a table from memory instead of from the tool output. Remedy applied: digests are only pasted from `sha256sum` output.
* Natural-language PubMed queries with several terms returned zero hits; field-tagged queries worked. The first pass at efonidipine hERG was therefore a false empty and was repeated with field tags before any "not found" was written.
* No one else caught anything this session; the absence of an independent check is the weak point (grade above).

## Micro-upgrades (the answers)
`verify_quotes.py` (mechanical verbatim check against saved pages, reusable for any PMC-page reading) and the access-log convention with digests, both in the package folder. The route fact for the radar is proposed, not applied.

## Residual debt
Efonidipine Cav3.1 and Cav3.3 values and any efonidipine hERG or QT value (access results, not literature absences); an independent read of the interpretation if INV-03 is acted on.
