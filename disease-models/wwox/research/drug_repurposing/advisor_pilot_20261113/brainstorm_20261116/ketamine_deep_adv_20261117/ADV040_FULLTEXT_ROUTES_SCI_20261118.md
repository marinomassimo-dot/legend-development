# ADV-040: lawful free routes to the full text of three closed sources (SCI, 2026-11-18)

Non-canonical working note. Not medical advice; no dose and no recommendation. Result: **all three sources stay closed on every lawful route tried; no file was obtained, so no FULLTEXT_READ_RECEIPT was written and nothing was read beyond what the abstracts already gave.** Method: one plain request per route, empty User-Agent, no key, no e-mail address or contact parameter sent to any service, no account, no payment, no request to authors. A Cloudflare, proof-of-work or rate-limit response ended that route with no retry and no bypass. Requests were made 2026-11-18 about 00:28 to 00:45 UTC. Raw responses are in the session scratchpad, not in the repository.

## Routes and HTTP outcomes
| Route | 36256600 memantine (Brain, DOI 10.1093/brain/awac380) | 38461760 Kuki 2024 (J Neurol Sci, DOI 10.1016/j.jns.2024.122950) | 23197747 Rosati 2012 (Neurology, DOI 10.1212/wnl.0b013e318278b685) |
|---|---|---|---|
| Europe PMC search (core record) | 200; `isOpenAccess` N, `inEPMC` N, no PMCID; only a DOI link marked "Subscription required" | same | same |
| Europe PMC `supplementaryFiles` | 404 | 404 | 404 |
| PMC ID converter (no tool/email parameters) | 200; no PMCID returned | 200; none | 200; none |
| OpenAlex work by DOI | 200; `oa_status` closed, `any_repository_has_fulltext` false; locations: publisher and PubMed only | 200; closed; publisher and PubMed only | 200; closed; **one repository location, University of Florence "Florence Research", version submittedVersion, handle 2158/794578** |
| Semantic Scholar graph API by DOI | 200; `isOpenAccess` false, no `openAccessPdf` | 200; same | 200; same |
| Crossref work record | 200; OUP reuse licence only; PDF links point to the publisher | 200; Elsevier TDM links (`api.elsevier.com`, which need an API key: not used) | 200; link to the neurology.org PDF only |
| Preprint servers (Europe PMC `SRC:PPR` title searches) | 200; 2 hits, neither is this trial | 200; 2 hits, neither is this paper | not searched as a preprint (2012, not a preprint-era paper); Europe PMC title search found only the record itself |
| Publisher PDF or page, one plain GET | OUP article PDF: **403, Cloudflare "Just a moment"**: route ended | ScienceDirect article page: 403, an 833 kB JavaScript shell with no article text and no challenge marker; no text obtained | neurology.org `pdfdirect`: **403, Cloudflare "Just a moment"**: route ended |
| Handle resolver for the Florence record | n/a | n/a | `hdl.handle.net/2158/794578`: 500 "Cannot Connect to Server": no redirect |
| Florence repository record `flore.unifi.it/handle/2158/794578` | n/a | n/a | **403, Cloudflare "Just a moment"**: route ended |
| CORE API (no key) | 429, empty body (key required in practice): not retried | not tried after the 429 | not tried after the 429 |
| BASE search | 200 but an "Oh noes!" proof-of-work page (Anubis): route ended | not tried after the proof-of-work page | not tried after the proof-of-work page |
| OpenAlex title search | 429 rate limit: not retried; redundant, since the DOI lookup already lists every location | not tried | not tried |

## Verdict per paper
| PMID | Result | Why |
|---|---|---|
| 36256600 (memantine crossover) | **closed** | no open-access copy exists in any index queried; the publisher PDF is behind a Cloudflare challenge |
| 38461760 (Kuki 2024) | **closed** | no open-access copy; the publisher page returns no article text without script execution; the keyed Elsevier text API is excluded by the no-key rule |
| 23197747 (Rosati 2012) | **closed on every route tried, with one named lead** | OpenAlex records a submitted-version copy at the University of Florence repository; both the handle resolver and the repository record are unreachable (500; Cloudflare challenge) |

## What this changes in K7 and K8
Nothing. K7 and K8 stay at the verdicts already written in the KDS synthesis: K7 "does not stand" and K8 "numbers recompute only unpaired; 'only' holds for published randomised DEE trials". The blocked items remain exactly those the synthesis lists: for K8, the paired analysis and its test, the composite responder definition, harms by arm, funder and the 31-versus-30 discrepancy; for K7, the itemised adverse events and the composition of the non-inflammatory stratum in Kuki, and the endpoint definitions and midazolam add-on in Rosati. No sentence of either verdict gains or loses support from this attempt.

## Open routes that this session did not use (a human visit is the remaining step)
| Source | Human route that stays within the rules | Ranking for a human visit |
|---|---|---|
| Rosati 2012 | the Florence repository record in a normal browser session (a person can pass the challenge; the agent may not) | first: a free submitted-version copy is recorded there |
| Memantine trial (Brain 2023) | the publisher page in a browser, or the institutional library | second: decides the paired analysis and the responder definition that K8 rests on |
| Kuki 2024 | the publisher page or library access | third: decides the non-inflammatory stratum that K7 rests on |

Not tried on purpose, per the brief: Unpaywall and any service that asks for a contact address; the keyed Elsevier API; any request to the authors; any account or payment; a retry or workaround after a challenge page.
