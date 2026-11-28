# ADV-297 result: abstract triage of catalogued-only records, ten seeded draws (SCI, window fc428159, 2026-11-28; hypothesis level; reference genotype class; not medical advice)

PREREG `PREREG_ADV297_SCI_20261128.md` (sha256 4eff489558ff7904ef26c8ccf0313331c6d5cd47459a3f24d2759c5f1887089c, commit 22613d12a, frozen before any abstract was opened). Draw `draw_adv297.py`, seed 20261128, pool 194.

## Verdict

**Not decidable from this draw.** Only 3 of the 10 records had a full-text check, below the 7 the PREREG requires. No parking rule and no rejection is claimed. Counts: **1 miss of 3 checked; 2 of 3 calls confirmed.**

## Step A (abstract and metadata only)

READ-NOW 1, READ-LATER 8, DISCARD 1. Report `STEP_A_REPORT_ADV297_SCI_20261128.md`.

## The ten records

| Draw | PMID | Step A | Outcome |
|---|---|---|---|
| 1 | 16116962 | READ-LATER | access: closed (Europe PMC not open, OpenAlex closed) |
| 2 | 26120275 | READ-LATER | not checked: reader stopped |
| 3 | 31829254 | READ-NOW | not checked: reader stopped |
| 4 | 25502636 | READ-LATER | access: publisher 403 on the listed gold-OA PDF |
| 5 | none (CORPUS P214) | DISCARD | access: entry has no title, abstract or identifier |
| 6 | 32931356 | READ-LATER | not checked: reader stopped |
| 7 | 25662954 | READ-LATER | checked: **MISS** |
| 8 | 26910372 | READ-LATER | checked: no datum met the rule (call confirmed) |
| 9 | 20367991 | READ-LATER | access: 403 on one listed route, 404 on the other |
| 10 | 17690733 | READ-LATER | checked: no datum met the rule (call confirmed) |

Access results 4 (records 1, 4, 5, 9). Semantic Scholar answered 429 to the three queries made for records 1, 4 and 9: a result, not retried. Not checked 3 (records 2, 3, 6): their text was fetched, and part of one response of the batch 1 reader was stopped by a safety classifier before any held file was searched. It was not retried, re-dispatched or done by another route (`STEP_B1_REPORT_STOPPED_ADV297_SCI_20261128.md`). No receipt is recorded for those three. The one READ-NOW record is among them, so the draw says nothing about false alarms.

## The miss

Record 7, a review focused on WWOX, called READ-LATER by the rule's own review clause. Full-text reader: four data (one weak). Blind reader, given the held sentences, the source passage and the rule: agreed on five of six sentences, disagreed on one (card A03). SCI checked the original: Table 1 values, "unpublished observations", the preliminary retinal statement, the figure 6 legend, no S281 in the text. Matching items and proposed wording: `SENTENCES_FOR_IT_ADV297_SCI_20261128.md`.

* **What the abstract hid:** measured affinities (ITC, eight peptides, five of them stated as unpublished) and a preliminary enzyme statement, inside a record typed as a review. The step A reader had written that the full text could hold ligand affinities and the evidence behind the "likely" retinal activity, and still called it READ-LATER, because the frozen rule sends a WWOX-focused review there. In this one case the abstract did not mislead; the rule's review clause did.
* **Weight:** narrow. A fold range widens, a premise gets a measured peptide affinity, an active-site attribution is corrected, one catalytic statement without data is added. No conclusion, need, card direction or ranking reverses.
* **Side finding:** discovery ledger line 29 already cites this paper by its PMC identifier, so a held sentence rested on a record counted "catalogued only, no receipt". Joins by PMID and DOI do not see it.

## Departures from the PREREG

* Step B batches were planned for the six reachable records: two batches of three. The first was stopped. The second ran as planned with the same dispatch text.
* Fetch routes used beyond the two named first (PMC efetch, Europe PMC): the PMC open-data bucket (record 7), the PMC article page (record 6), publisher and repository PDF links listed by Europe PMC or OpenAlex (records 4, 9, 10).
* "Figures" were looked at for none: no figure image was provided to any reader. Every check is "text, tables and figure legends".

## Delegates

All legend-delegate, claude-sonnet-5-5, effort high read back on every turn: step A 2 of 2 turns, batch 1 9 of 9, batch 2 28 of 28, blind check 4 of 4. One at a time.

## For the next increment (ADV-297b, ADV's decision, not started)

A second seeded draw from the remaining 184, restricted before the draw to records with an open full-text route tested by script, so that the denominator can reach 7. The answer will then be about the openly readable part of the tail. SCI's suggestion: keep the step A rule unchanged so the two draws compare, and report reviews apart, since the one miss came from the review clause.

## Limits

One draw, three checks, one model family for every reader. A count of 1 in 3 is not a rate for the 194. The matching rule counts small additions (a range, an attribution) the same as reversals.
