# ADV-259 result: the Chong 2023 lactate statement (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; nothing here is medical advice. No spend, no contact, no e-mail address in any request. Pre-registration: `PREREG_ADV259_SCI_20261125.md`. Paper: PMID 36537114, DOI 10.1002/ajmg.a.63074.

## 1. Disposition: UNREACHABLE

No route reached the passage. The value "2.4 to 3.3 mmol/L" is neither verified nor contradicted. The prediction (unreachable) held.

## 2. Routes

| Route | Result |
|---|---|
| `evidence_presence.py` for the PMID | the two declared artefacts are present and match; both are the 8-chunk gateway surface, which has no lactate word (ADV-255) |
| `files/` by name, DOI and title | those two files only; no PDF or page render |
| Earlier tool results of this machine's project sessions (DOI plus lactate) | no lactate excerpt of this paper carrying a value, subject label or unit (the one match belongs to another report) |
| Receipts, manifest, dossier, locator audit | no stored quote of the lactate statement; the sentence is in the repository since the first public-edition commit (2026-07-26) |
| Europe PMC full text; preprint search | HTTP 500 and no PMC record; no preprint |
| PubMed page | HTTP 203 with a hidden body, treated as a route result |
| Publisher (DOI and article page) | HTTP 403, not retried |
| OpenAlex; Semantic Scholar | closed; no repository copy |
| Web search | the publisher and abstract pages, a laboratory publication page (no text, no PDF), and a ResearchGate listing. **The ResearchGate copy was not fetched:** its right to be there is not established. |

Not tried: the Scholar Gateway connector (needs the operator's sign-in); institutional access or a library.

## 3. What weakens the number beyond being unseen

* The July reading used the gateway surface that FT-125 found mixing passages of unrelated documents.
* The extraction-defect note of 2026-10-21 found that this paper's held surfaces drop hyphens in words and minus signs, so figures from them need a page to be trusted.
* No locator was ever stored for the sentence.

## 4. Wording for IT (not applied)

For `CLAIM 009`, card `E04`, `meta_metabolism` and `PAPER 017`: "Chong 2023: a mildly raised lactate (2.4 to 3.3 mmol/L) in one of five subjects is a registry statement with no stored quote and no held passage (UNREACHABLE, 2026-11-25). Do not use the number until the page is seen." The number is written in `PAPER 017` and `E04` (inside a `not_known` item); `CLAIM 009` and `meta_metabolism` carry only the qualitative statement. ADV-255 shows blood lactate named normal in five other publications.

## 5. Receipt and request list

No receipt was recorded: no new text of the paper was read. Row 2 of `operator_pdf_wishlist_20261021.md` already asks for this PDF; a dated line there now adds the lactate need and its consumers.
