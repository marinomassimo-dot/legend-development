# ADV-195 result (SCI): CLOSE as a ROUTE RESULT, no reading (hypothesis level; no ranking change; no drug promotion; not medical advice)

result_at: 2026-11-23T11:40Z
task: ORCH-SCI-ADV065-DEEPEN-20261118, step 88 (assignment ADV-195, SCI's own MEETING prospect of the 11:35Z round)
source: the authors' 2025 SCN2A p.E512K organoid paper, Neuroscience Bulletin, PMID 40540154, PMC12569333, DOI 10.1007/s12264-025-01429-w.

## 0. Verdict

**CLOSE as a route result. Nothing of the body was read, so no pre-registration was written and no question (a), (b) or (c) of the assignment is answered.** The five lawful routes named by ADV and the two obvious neighbours returned no full text without a person's browser. The item moves to the operator-supply list, as Jia 2024 did; it is NOT a finding that the paper adds nothing.

My own error to correct: my MEETING reply called the source "open". Europe PMC already printed `isOpenAccess: N` and `license: none` for it; having a PMC id is not open access. The route check I should have done before proposing it takes one call.

## 1. Route table (all plain requests, no browser, no header spoofing, no contact address sent)

| Route | Result |
|---|---|
| PMC open-data bucket, prefix `PMC12569333` (with and without `.1`) | HTTP 200, zero objects: the article is not in the open subset |
| PMC article page | HTTP 200 but the body is the "Checking your browser - reCAPTCHA" page (21 337 B): a challenge, not bypassed |
| Europe PMC `fullTextXML` | HTTP 500 |
| Europe PMC `supplementaryFiles` | HTTP 200, an error bean (297 B), no files |
| Europe PMC PDF render (`ptpmcrender`) | HTTP 403 (5 631 B HTML) |
| PMC BioC (`pmcoa.cgi`) | HTTP 200, "No result can be found" |
| NCBI E-utilities `efetch db=pmc` | HTTP 200, 9 834 B: front matter only; the file carries the comment "The publisher of this article does not allow downloading of the full text in XML form" |
| Publisher page (Springer Nature Link, DOI route, one request) | HTTP 200, 378 KB of HTML, but only the abstract, the reference list and the article metadata; no body sections (eight section titles: Abstract, References, Acknowledgements, Author information, Ethics declarations, Additional information, Rights and permissions, About this article) |

## 2. What is known at abstract level only (NOT a reading)

The abstract (Europe PMC record) says: a patient-derived organoid model with a novel SCN2A variant (p.E512K); gain-of-function features of the variant channel; MEA recordings of patient-derived cortical organoids showing "increased spiking and remarkable network bursts"; "differential responses to various anti-seizure drugs" and a good response to carbamazepine; the claim that individualised organoids can serve as a platform for preclinical pharmacological assessment. It names no isogenic correction, no vehicle arm, no unit, no n and no per-compound number. Therefore the abstract settles none of my expectations (including the "no isogenic control" expectation ADV flagged as unverified: it stays UNVERIFIED), and it must not be quoted as agreement or disagreement with the ADV-191 pattern.

## 3. Consumer and what would reopen it

* ONE consumer line, for ADV at the RP-043 touch (replaces "Pointer, not dispatched"): *the 2025 E512K organoid paper (PMID 40540154) is not retrievable by any lawful machine route tried on 2026-11-23 (PMC page reCAPTCHA, bucket empty, Europe PMC 500 and 403, efetch front matter only, publisher page abstract only); abstract level only; the per-compound burst, synchrony and design questions stay open and on the operator-supply list.*
* Reopening condition: the operator supplies the article PDF (then evidence_presence.py by SHA-256, read with a pre-registration; the three questions of ADV-195 stand as written), or the paper appears in the PMC open subset.
* Nothing in the ADV-191 clause changes. No ranking change, no drug promotion, no WWOX or clinical claim.

## 4. Not done

No body, figure, table or supplement of the paper was read; nothing was downloaded beyond the route responses above (the Springer HTML, 4dbf57ba7dc2 first 12 hex of the SHA-256, the efetch front matter and the error pages sit in a scratch folder, not in git).
