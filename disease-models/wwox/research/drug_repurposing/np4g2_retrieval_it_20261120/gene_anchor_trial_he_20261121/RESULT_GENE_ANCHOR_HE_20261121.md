# Gene-anchor trial for the scout's reopen-row query (HE, 2026-11-21)

Reference-genotype class only; abstract-level retrieval counts, not a reading and not a claim. Question (IT, NP4G2 result, "Defect found in the engine path"): does putting the disease gene in a
reopen-row query repair the query that read `TITLE_ABS:opc AND TITLE_ABS:drg`? Recall set: IT's `K_core_record_ids.tsv` (29 records, 28 with a PubMed record; the 29th is a preprint PubMed does not hold).
Script: `measure_gene_anchor.py`; numbers: `result_he_20261121.json` (PubMed arms). Route: **PubMed title/abstract**, because Europe PMC answered HTTP 500 to every query on 2026-11-21 (first
run: three queries answered, the fourth failed; later runs: all failed, also a bare `WWOX` query). The Europe PMC arms are therefore not measured; the scout's real query is Europe PMC, so
the table below is the PubMed analogue of its query terms, and the preprint is out of reach by construction. The scout's window is 2024-11-20 to 2026-11-20.

| Arm | Query (PubMed, `[tiab]`) | Records, all years | K_core found | Records, scout window | K_core found |
|---|---|---|---|---|---|
| B (before) | opc AND drg | 17 | 0 of 28 | 1 | 0 |
| G (gene first, as IT proposed) | wwox AND opc AND drg | 0 | 0 | 0 | 0 |
| G1 | wwox AND opc | 0 | 0 | 0 | 0 |
| G1b | wwox AND drg | 1 | 1 (PAPER 140, a rat DRG injury paper) | 0 | 0 |
| S (subject words, no gene) | oligodendrocyte AND differentiation | 4690 | 2 | 631 | 2 |
| SG | wwox AND oligodendrocyte | 3 | 3 | 2 | 2 |
| **GD (what the flag now builds)** | wwox AND differentiation | 45 | 2 (PAPER 029, PAPER 094) | 7 | 2 |
| D (subject word alone) | differentiation | 646253 | 0 | 65359 | 0 |

## What it says
1. **The literal proposal does not work.** Prepending the gene to the two abbreviations makes a three-way AND that returns nothing (G): the abbreviations OPC and DRG are what the row calls its objects,
   and almost no paper carries both with the gene. The first implementation of the flag was G; the trial overturned it before landing.
2. **The defect is the object choice, not the missing gene alone.** The gene with the row's own top subject word (`differentiation`, which `key_terms` already ranks first once the form words are
   skipped) returns 7 records in the window, two of them on topic and in K_core, where the query before returned 1 record and none of K_core. The subject word alone (D) is useless (65 359 records),
   and subject words without the gene (S) bury the same two records in 631. So the gene supplies the precision and the subject word the recall.
3. **The flag was changed to GD:** for a reopen-row question that names no drug, `--gene-anchor` searches `TITLE_ABS:<GENE> AND TITLE_ABS:<top subject word>` (and the keyword query `<gene> <subject word>`);
   a drug-naming row, a row with no plain subject word of 5 or more letters, and every other surface keep their search. Off by default, so the plan digest does not move.

## Limits (read before relying on it)
- GD was chosen **after** the K_core numbers were seen, on the same set and on one row: it is tuned, not validated. Two of 28 is a small gain on a set in which 26 records cannot be reached by any
  short query (S, the widest arm, finds the same two); a different row could behave differently. IT's recall set was also computed by an author who had read much of it (IT's own caveat).
- PubMed is the second route; Europe PMC (the scout's own) was down. Its preprints are not covered, and `TITLE_ABS` is not `[tiab]` (it also matches differently on plurals and truncation).
- The cost is one query per anchored row (the same number as before: the anchored query replaces the old one). Nothing in the default run changes.
- Not tested: other disease folders' reopen rows. The gene is `WWOX` only because the module path names it; `--gene-anchor GENE` takes any symbol.

## Verdict
KEEP as an opt-in flag with the GD form (not G); NOT proposed as a default; the default stays until a second row or a live Europe PMC rerun shows the same direction. Re-run
`python3 -I measure_gene_anchor.py <out.json>` when Europe PMC answers again (the PubMed arms run by default and the Europe PMC arms follow; `--no-epmc` skips them).

## Addendum (HE, 2026-11-21, ADV's bounded question): is there a held-out row, and what would change the default
Searched the repository for another recall set (`*record_ids*`, known-positive, recall-set and gold-set names; the retrieval packages; the reopen tables of all packages): the only
known-positive sets are IT's three for NP4G2 (`K_record_ids.tsv`, `K_core_record_ids.tsv`, `K_title_record_ids.tsv`), which are the set the flag was fitted on. The other glia rows (NP4G1,
NP4G3) share its topic and would be drawn from the same K, so they are not held out; no other reopen row has a frozen list of known positives, and building one would be a package of its own
(a judgement of what each row's positives are), not a count I can run once. **Not run; recorded as the typed condition.**

Condition for ever changing the default of `--gene-anchor` (all four, written before the first query): (1) at least two reopen rows other than NP4G2, in different disease themes, each with a known-positive
set of at least 10 PubMed records frozen from held material (receipt ledger, census or an earlier briefing's items that were later read) before any query; (2) Europe PMC answering, so the
scout's own query is measured, with the PubMed analogue as a second route; (3) on each row the anchored query finds at least as many positives as the current one and a higher share of positives
among the records it returns; (4) the number of records the anchored query returns stays readable (the cap of the scout's briefing). Until then the flag stays opt-in.
