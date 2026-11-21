# SEARCH_RECORD - IT48-Q01 juvenile half, forward-citation route (2026-11-21)

Producer: model sonnet, effort high (as stated at dispatch). Route: citations, not strings. Pre-registration: `SO_before_search.md`, written before the first call. Clients: `curl` and a small Python (urllib, run with `python3 -I`, User-Agent "legend-literature-client"; no key, no e-mail, no mailto parameter, no contact in any header). Zero spend. No agent started. Raw call logs and pulled JSON are in `/tmp/it48fwd/data/` (scratch; not repository files). Counts below are from those logs.

## 1. Seeds (13 papers) and what each route returned

Seed = paper reporting a Ba2+ experiment in cortical L2/3 pyramidal neurons (brief list) plus the rows R01-R13 papers of the 2026-11-17 package; Richter 1997 (R14) and Furdan 2026 (R16) added because they were in that package. "OA citing/cited" = OpenAlex `filter=cites:<W>` and `referenced_works` (resolved in batches of 50 by `filter=openalex:`). "EPMC" = Europe PMC REST `/MED/<pmid>/citations` and `/references` (pageSize 1000).

| Seed | OpenAlex id | OA citing (pulled / listed) | OA cited | EPMC citations | EPMC references |
|---|---|---|---|---|---|
| Xue 2014 (V1 L2/3, P14-23, 50 uM) | W2077208091 | 774 / 801 (see failure F1) | 51 | 643 | 49 |
| Nguyen 2024 (mPFC L2/3) | W4387542144 | 46 / 46 | 79 | 30 | 78 |
| Goldberg 2011 | W2116361248 | 146 / 153 | 92 of 95 | 122 | 86 |
| Day 2005 | W2077525799 | 196 / 202 | 58 | 148 | 54 |
| Routh 2022 | W4296709443 | 10 / 10 | 47 | 5 | 45 |
| WNK3 2022 (PMID 36311015) | W4304956755 | 5 / 5 | 77 of 80 | 5 | 78 |
| Goodfellow 2009 (R06) | W2031156732 | 105 / 110 | 68 | 75 | 67 |
| Sutor 1993 (R11) | W2067916139 | 26 / 26 | 15 | 21 | 17 |
| Hwa 1991 (R12) | W1971499158 | 22 / 23 | 18 | 19 | 20 |
| Sceniak 2006 (R13) | W2120176506 | 176 / 180 | 56 of 57 | 133 | 54 |
| Richter 1997 (R14, extra) | W2134818522 | 24 / 24 | 18 | 19 | 18 |
| Furdan 2026 (R16, extra) | W7154068342 | 3 / 3 | 68 | 1 | 67 |
| Fmr1 A1 preprint 2026 (R04/R05) | W7127609459 (resolved by DOI) | 0 / 0 | 56 | not queried (no PMID) | not queried |

Union of the OpenAlex pulls: 2,170 unique works (1,519 citing at least one seed, 665 cited by at least one seed; some are both), of which 1,155 carry a PMC id and 1,015 do not. Europe PMC citations/references not already in the OpenAlex union: 145 (139 preprints, 4 MED, 1 PMC, 1 blank). Those 145 were not opened in full text (see section 4).

## 2. Query/URL pattern (every call type; the exact URLs are in the logs)

- OA1: `https://api.openalex.org/works/pmid:<PMID>?select=id,doi,title,...` (resolve seeds; about 20 curl calls, not in the script log; Fmr1 preprint by `doi:`)
- OA2: `https://api.openalex.org/works?filter=cites:<W>&select=...&per-page=200&cursor=...` (forward citations; 12 seeds)
- OA3: `https://api.openalex.org/works/<W>?select=id,referenced_works` then `works?filter=openalex:<W1>|<W2>...` (backward references)
- OA4: Xue only: `works?filter=cites:W2077208091,publication_year:<Y>` for Y = 2014..2026, per-page 100 (13 calls)
- OA5: one call `filter=cites:W2567363407` (works citing the Fucke thesis): count 0
- EP1: `https://www.ebi.ac.uk/europepmc/webservices/rest/MED/<PMID>/citations|references?format=json&pageSize=1000`
- NC1: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<PMCID>&retmode=xml` (automated Ba2+ screen of PMC bodies; 438 calls logged, all HTTP 200)
- HD1: `http://archiv.ub.uni-heidelberg.de/volltextserver/8349/1/Dissertation_ThomasFucke.pdf` (open repository PDF) and `https://archiv.ub.uni-heidelberg.de/volltextserver/8349/` (landing page for the DOI)
- HTTP codes in the script logs (curl calls are not in them): OpenAlex 61 x 200 and 1 x 401 (F1); Europe PMC 24 x 200; NCBI efetch 438 x 200. Two OpenAlex `search`/`fulltext.search` calls returned 429 (F2).

## 3. Screening and how the candidate was found

1. Titles and abstracts of the union were used only to decide what to open (no verdict). An inclusive neuro keyword filter did not discriminate (1,829 of 2,170 matched), so it was not used to cut the set.
2. Automated full-text screen: for every OpenAlex work with a PMC id the PMC XML was fetched by efetch and searched for Ba2+ / BaCl2 / barium plus layer 2/3, pyramidal and an age token (P12-P18). 400 of the 1,155 PMC-id works were processed before this screen was stopped on finding the first candidate (59 of the 400 had no body text; 10 had a Ba2+ mention in the body; none of the 10 looked like a rodent L2/3 pyramidal Ba2+ measurement at P13-P17 by title and by the Ba2+ hit lines: reviews, a human-cortex study, injury, stress, network-modelling, metabolic and social-behaviour papers; they were judged from titles and hit lines, not read in full).
3. A separate title/abstract screen of the 1,015 works without a PMC id (strict filter: layer 2/3 or pyramidal or cortical neurons, plus development/intrinsic/rectification/Ba2+/Kir terms; 123 titles) found one record whose abstract matched the question: "Biophysical Characterization and Simulation of Neocortical Layer 2/3 Pyramidal Neurons during Postnatal Development" (T. Fucke, heiDOK 2008; OpenAlex W2567363407), which OpenAlex lists as citing Hwa and Avoli 1991 (seed R12). Its abstract states 1-to-6-week-old rats, KIR pharmacology and a developmental input-resistance series.
4. Full text: the open repository PDF (140 pages, SHA-256 4a8895d12848ad1f93ec7845c88367dbc51340c0111edfcfd233d13e29eabe38) was downloaded to `/home/desktop/legend-development/files/fulltext/it48q01_fwd_it_20261121/` and converted with `pdftotext -layout` (5,385 lines; text SHA-256 f555421e2481416325e88f8b04a53086bd3440eec85652c24c5d375f499ab67c). The full text was searched for barium/Ba2+/BaCl2 (all 18 hits inspected) and the Methods, the Ba2+ Results, the controls (phenytoin, TTX, ZD7288, spermine), the HH-fit section and the Kir discussion were read in full. 14 quotes were machine-matched (NFKC, whitespace-normalised) against the extracted text before being written to the receipt.
5. Stop rule: the brief says to stop at the first candidate; the PMC screen was killed at 400 of 1,155 (process killed, not completed). Nothing in this record says the other 755 PMC-id works, the 1,015 non-PMC works or the 145 Europe-PMC-only works contain no further measurement.

## 4. Routes that failed or were limited (route results; nothing bypassed)

- F1: OpenAlex cursor paging returned HTTP 401 on page 2 for the Xue 2014 citing list (cursor beyond the first 200 results). Worked around, not bypassed, by year-sliced requests (OA4): 774 of 801 listed citing works retrieved (27 not returned by the year slices). Europe PMC returned 643 for the same seed, of which 108 were not in the OpenAlex pull (mostly preprints).
- F2: OpenAlex `search`/`fulltext.search` filter returned HTTP 429 "Anonymous search is temporarily rate-limited" on two calls; not retried in a loop and not worked around with a key (a key would require an e-mail address, which must not be sent). The citation filter route (`cites:`) was not rate-limited. OpenAlex replies carry a notice that keyless requests share a daily budget; no key or account was created.
- F3: efetch returned no body text for 59 of 400 PMC-id works (publisher-withheld XML, supplements, meeting records); not counted as read.
- F4: No captcha, 403, 500 or other challenge page was met on any route in this session. No browser header was set; no e-mail or personal detail was sent anywhere.
- F5: Europe PMC-only works (139 preprints): not opened. bioRxiv direct access was not attempted (the 2026-11-17 record shows HTTP 429 and a summariser-only path for the preprints).
- F6: Backward references of 3 seeds were partly unresolved in OpenAlex (Goldberg 3 of 95, WNK3 3 of 80, Sceniak 1 of 57); the Europe PMC reference lists were used as the second view (all but 7 entries were already in the union).

## 5. Papers behind publishers (supply list) surfaced by the screen but not opened

Opened-by-title candidates whose full text was not reachable and which could hold a P13-P17 Ba2+ measurement: Interlaminar Differences of Intrinsic Properties of Pyramidal Neurons in the Auditory Cortex of Mice (Cereb Cortex 2008, PMID 18775844); Maturation of Layer V Pyramidal Neurons in the Rat Prefrontal Cortex (J Neurophysiol 2004, PMID 14602839; layer V, not the question); M1 Muscarinic Receptor Modulation of Kir2 Channels ... Prefrontal Cortex Pyramidal Neurons (J Neurophysiol 2007, PMID 17376848); Sutor 1993 (PMID 8233033), Hwa 1991 (PMID 1857546), Sceniak 2006 (PMID 16510775) and Richter 1997 (PMID 9209118) as in the earlier `human_access_list.tsv`. No paywalled paper was needed to reach the candidate: the candidate is an open PhD thesis.

## 6. Absence statement (what the negative part of this record does and does not say)

Apart from the one candidate in `candidates.tsv`, none of the PMC-body works screened (400) and none of the title-screened non-PMC works (123 of 1,015) was identified as a rodent neocortical L2/3 pyramidal Ba2+ measurement at P13-P17. This is two routes (OpenAlex and Europe PMC for the citation graph; full-text regex on PMC bodies and title/abstract screening for selection) and is not proof; the screen was stopped at the first candidate by the brief.
