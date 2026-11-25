# PREREG B, ADV-287: the counted universe, the strata rule, the seed and the sample (SCI, 2026-11-25; hypothesis level; not medical advice)

Frozen before any source is opened. PREREG A hash 0d0f2fae45055823 (22:03:28Z). Scripts: `universe_adv287.py`, `sample_adv287.py`; outputs: `universe_adv287.tsv` (hash a20c81ecc4437e26), `route_counts_adv287.tsv`, `sample_adv287.tsv` (hash db6e4646b3ed06b7), `sample_screened_out_adv287.tsv`.

## Counts (two routes; difference explained)

* 30 packets scanned. Union of statements after de-duplication within a card: **302**. Route 1 (structured fields): **188** (62 percent of the union; PREREG A predicted 40 to 70 percent and 250 to 500 statements: both inside). Route 2 only: **114**.
* Why route 2 finds 114 more: statements in fields the structured list does not name: the genotype-context strings of disease assertions (18, design descriptions such as "RNAi plus Abeta42 versus control"), `not_known` prose (10), `p4_card` for/against prose and `p4_fields` (16 and more), assertion context fields (age bands, ranges), and source-description strings. Route 1 misses them because the field list is by design the measured-result fields; route 2 over-counts because the word "range" or "ratio" matches without a value (three such sentences were drawn and screened out below).
* Excluded: the five cards IT re-derived (D02, F02, E03, I01, H01): **62** statements; Obeid-mention sentences: **2**. **Universe after exclusions: 239** (route 1: 150, route 2 only: 89).

## Strata rule, seed, sample

* Strata = route 1 and route 2 only; proportional allocation by largest remainder (13 and 7 of 20); within a stratum a uniform draw by Python `random.Random(287)` over rows sorted by (card, sentence); 6 reserves per stratum in draw order. Result: 20 statements from **12 card families** (at least 6 required): H02 7, A01 2, J01 2, E02 1, C04 1, F03 1, P11 1, L01 1, F01 1, A02 1, B01 1, K01 1.
* **Sentence-level screen (frozen here, made on the sentence alone, no source opened):** a sampled sentence with no computed or comparative quantity (only a label such as an age band, or the word "range" or "ratio" without a value) is replaced by the next reserve of its stratum. Three were screened out and replaced (listed with reasons in `sample_screened_out_adv287.tsv`).
* **Obeid rule:** a sampled statement whose only source is the Obeid 2026 article is replaced by the next reserve and recorded; it is never opened.
* One family (H02) carries 7 of 20 because it holds 40 of the 239 statements; the proportional rule is kept, and the family concentration is a stated limit of the estimate.

## Step 1 protocol (frozen)

A producer reads, for each sampled statement, the card's own source pointer (locator, receipt id, held full text or table), extracts the WHOLE source table or answer to a file, recomputes the statement from all rows, and classifies CORRECT, INCOMPLETE, WRONG or NOT ASSESSABLE (the reason named). Every non-CORRECT is verified by SCI on the held bytes. One blind reader (sonnet, effort high, stated) then receives the verbatim sentence plus the whole extracted source table and nothing else. The rate is reported over the assessable statements with the exact binomial interval; the rejecting observation is the one of PREREG A.
