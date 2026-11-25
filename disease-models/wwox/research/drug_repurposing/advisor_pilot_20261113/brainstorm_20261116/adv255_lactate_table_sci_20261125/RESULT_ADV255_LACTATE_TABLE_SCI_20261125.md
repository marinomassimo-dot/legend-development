# ADV-255 result: human lactate per report in WWOX deficiency (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; aggregate counts per publication; nothing here is medical advice. No spend, no contact, no e-mail address in any request, no registry or card edit. Pre-registration: `PREREG_ADV255_SCI_20261125.md`. Table: `lactate_per_report.tsv`.

## 1. Answer

* **Blood or unspecified-sample lactate is stated normal in 14 subjects from 5 publications** (24456803, 27495153, 30361190, 30746283, 35792847), and CSF lactate normal in 1 of those subjects. No held report states a raised blood or CSF lactate in a passage that could be read. None prints a value or a reference range.
* **Spectroscopy is not one-directional.** One publication reports small lactate peaks at 4 months and none at 2 years 4 months (35573960); one reports "extremely low" lactate, with a second candidate variant in another gene (30362252). Other reports call spectroscopy normal or non-diagnostic without naming lactate (29808465, 30853297 and others).
* **The one statement of a raised value cannot be verified here.** The registry gives "mildly elevated, 2.4-3.3 mmol/L" for one subject of Chong 2023 (36537114). The held copy is 8 delivered chunks with no lactate passage; there is no open copy (Europe PMC: no PMC record, subscription only). It may well be correct; no stored locator supports it. The reading it comes from used a 47-chunk surface that the queue entry FT-125 later found to mix passages of unrelated documents, which is a further reason to see the sentence again.
* So the card wording "normal or low" holds for blood as far as the readable reports go, and **needs "in most reports"** because of one transient spectroscopy peak and one unverified raised value.
* **Two records say something the held sources contradict:** the hypothesis record calls the "extremely low" report the only human brain spectroscopy datum, and map record N-06 calls it the single spectroscopy case. 35573960 is a second report with a lactate statement on spectroscopy, in the opposite direction at one age. (Two analysis notes, `OVERNIGHT_CHECKPOINT_20260922.md` and `AUTONOMOUS_SESSION_STATE.md`, had already noted the age-dependent peaks; the two records were not updated.)

## 2. Per-consumer verdict

| Consumer | Verdict | Wording proposed (not applied) |
|---|---|---|
| E02 card | wording needs change | "Human lactate in WWOX deficiency: blood normal where stated (5 publications, up to 14 subjects, no values); spectroscopy mixed (one report with small peaks in early infancy and none later, one report 'extremely low'); one raised value in the registry is without a held source passage." |
| E04 card | wording needs change | `evidence_against`: replace "Four sources report normal human metabolism" with the sentence above (the four-source count was withdrawn on 2026-10-27). `not_known` item with "2.4 to 3.3 mmol/L": add "(registry statement; no held source passage)". |
| E03 card | unchanged | it states no human lactate datum |
| N-06 | conclusion unchanged; text needs correction | not "the single MRS case": add 35573960 (peaks at 4 months, absent at 2 years 4 months); the screen count rises from 3 to up to 14 subjects. "Does not report reliably" stands. |
| HYP-20260709-01 | one sentence is wrong | replace "the only human brain spectroscopy datum reports lactate extremely low" with "human spectroscopy is mixed: extremely low in one report (confounded), small peaks at 4 months and none at 2 years 4 months in another". No score change proposed. |
| DL-BIO-009 | count understated | "two primary sources (3 patients)" becomes five publications with lactate named normal, up to 14 subjects; keep DL-BIO-005 downgraded. "Lactate has been looked for in blood and reported normal where stated." |
| `meta_metabolism`, CLAIM 009, PAPER 017 | mark the Chong value | "registry statement; passage not held" until the publisher PDF is supplied or the gateway chunks are re-delivered |

## 3. Counted publications and expectations

Seven publications name lactate with a direction (the five above, 35573960, 30362252). Five are normal in every sample.

* E1 (2 to 5 publications contradict "normal or low"): **not met**, 1 (35573960). Chong would be a second if it were verified.
* E2 (at least half are normal in every sample): **met**, 5 of 7.
* E3 (the Chong source states a raised lactate): **not testable**; the held copy has no passage. Counted as not met.
* E4 (no publication states lactate below range): **not met as written**: 30362252 says "extremely low"; it gives no value or range, and on spectroscopy a low lactate is hard to tell from a normal one.

## 4. Coverage, and what was not read

* Route 1: tracked files. Route 2: held text, XML, HTML and PDF-without-text-copy files naming WWOX (542 files, 80 with a lactate word), plus JSON, DOCX and XLSX; the reports of the ADV-135 set one by one, with the supplements scanned for those silent ones that had a spreadsheet, document or zip supplement.
* No lactate word found in the copy read of: 24369382, 25416187, 28721938, 30356099 (with supplement tables), 31618474 (its WWOX row), 33919646, 36779245, 37974179, 39101447, 39416860, 39507621, 42193054. Silence is not a normal result.
* ADV-135 listed 15 human reports not held as full text; none was read here. A Europe PMC title and abstract query for WWOX with lactate returned four records, none a clinical report.
* Possible family overlap among the Saudi reports (shared variants) was not resolved: 14 is an upper bound.
* Single-representation rows: 30362252; rows marked "not re-checked" carry no direction and were read once.
* 24949445 mentions WWOX through a heterozygous duplication and was excluded by the inclusion rule.

## 5. Next

* One item for the operator-supplied PDF list: Chong 2023, DOI 10.1002/ajmg.a.63074 (wanted: the lactate sentence and its reference range). Consumers: `meta_metabolism`, CLAIM 009, E04, PAPER 017. The queue already has an entry for this paper (FT-125); the lactate sentence belongs there.
