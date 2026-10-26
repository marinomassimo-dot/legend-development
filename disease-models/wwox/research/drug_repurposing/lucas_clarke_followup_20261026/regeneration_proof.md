# Regeneration proof — the cards and the research queue, 2026-10-26

Scientist `scientist-c`. Commands are run from the repository root of the task worktree; all runs are offline except the ones named live. The handoff
file is **rendered** (`repurposing_join.py handoff --write`), never typed.

## 1 What "consumable by the module" meant here, measured
The join builds a card only for a query that carries a **candidate name**, and a candidate name comes from one place: a `### R-nn` / `### N-nn` heading of
`analysis/mechanism_intervention_map.md`. Claim, lead and pathograph queries get an evidence table but **no card and no handoff row**. This was measured
before it was used: two staged leads were appended in a throwaway copy of the tree (`git archive` of the committed branch, outside the repository), and the join was run
before and after:

| Run in the throwaway copy | queries | evidence tables | cards | handoff rows |
|---|---|---|---|---|
| baseline | 339 | 339 | 26 | 26 |
| after appending `lead_isr_signed_readout_gap.json` and `lead_ldh_stiripentol_weak_link.json` (numbered there as DL-MECH-173 and DL-REPO-004) | 341 (+2: `Q-DL-MECH-173`, `Q-DL-REPO-004`) | 341 | **26 (+0)** | **26 (+0)** |

So the leads enter the module's *evidence* layer (each reaches PAPER 567's receipted manifest; `Q-DL-REPO-004` reaches 52 papers, most inherited through DL-BIO-008 and DL-BIO-009) but not its research queue.
Two map records (R-10 and R-11) were therefore added to the mechanism map in the format of R-01..R-09, with the endpoint in a **bold** span of `DECISIVE_PRECLINICAL_TEST` (the join's bound-paper screen needs one) and with
`SOURCE_IDS` restricted to PAPER 567: the first version named related claims and leads too, and the join then inherited 52 and 54 papers for what is, in fact, one reading.

## 2 The regeneration, in order
1. `repurposing_join.py run` (offline, cached adapters): **339 queries, 26 cards**; vs the previous state (2026-10-25): ~205 queries and ~126 evidence tables CHANGED, +0 added. The cause is the registry and manifest state that landed on 2026-10-26 (PAPER 567, its manifest with 104 locators and the blind audits, the dated consequence notes), not my files. A second `run` immediately after: **0 changed** in queries, evidence and cards (deterministic, incremental).
2. R-10 and R-11 added to the map; their adapter calls made live once and cached (`chembl`, `openfda`, `pubtator3` by candidate name or first two gene tokens; the PubMed bound-paper check live for the single PMID); `run` again: **341 queries, 28 cards, +2 added (`Q-R-10`, `Q-R-11`)**, 17 map-record queries CHANGED only because the insertion moved the line numbers the join records as `origin_line` (their evidence digests did not change). A further `run`: 0 changed.
3. `repurposing_join.py handoff --date 2026-10-26 --write research/repurposing_batch_selection_20261026_module.md`: **28 rows** (previous refresh: 26).

## 3 What changed in the queue, on the treated cases
Rows of the 2026-10-25 handoff against the rendered 2026-10-26 handoff (only the rows that differ):

| Query | Candidate (map heading) | 2026-10-25 | 2026-10-26 |
|---|---|---|---|
| `Q-N-06` | Lactate as a WWOX readout | READ, 49 papers, 29 complete | READ, 50 papers, **30 complete** (PAPER 567 now reached) |
| `Q-N-07` | Digoxin | READ, 2 papers, 1 complete | READ, 4 papers, 3 complete (PAPER 567 among the two added) |
| `Q-N-08` | Dichloroacetate | READ, 47 papers, 28 complete | READ, 48 papers, **29 complete** |
| `Q-R-05` | Ketogenic diet | READ, 49 papers, 30 complete | READ, 50 papers, **31 complete** |
| `Q-N-01`, `Q-N-11`, `Q-R-09` | mTOR, 4-PBA/TUDCA, proteostasis | READ, one paper fewer | READ, one more complete read each |
| `Q-N-15`, `Q-N-17`, `Q-R-08` | AUDIT rows | AUDIT | AUDIT, one more complete read in the denominator |
| **`Q-R-10`** (new) | ISRIB-class eIF2B activators and other ISR attenuators | not a row | **REPLICATE**: ONE_PAPER (PMID 42909904, 104 locators, audit state read from the manifest); bound-paper screen **UNVERIFIED**: the paper's title and abstract carry none of the endpoint words *eIF2, alpha, phosphorylation, protein*, so the row says *BIND FIRST* |
| **`Q-R-11`** (new) | Stiripentol (LDH-lowering rationale) | not a row | **REPLICATE**: ONE_PAPER (the same); screen **UNVERIFIED**: the endpoint word *activity* is not in the title or abstract. The card's label lookup is MATCH_FOUND for stiripentol (US label, openFDA) |

Reading: the module reproduces, by command, the two facts the cards state by hand — the ISR and LDH strands each rest on **one** reading, and that reading does not measure the endpoint the decisive test names (eIF2 alpha phosphorylation; LDH activity).
No ranking, score or dose is in these rows.

## 4 `diff`: where the derived card and the hand-made card differ
`repurposing_join.py diff Q-N-08 cards/E03_pdk_inhibition_dca.card.json`, `diff Q-N-06 cards/E02_ldh_inhibition.card.json`, `diff Q-R-05 cards/E04_ketogenic_lactate_axis.card.json`: in all three the derived card carries `NO_DRUG_ASSERTIONS_SUPPLIED`
and an empty comparison list, while the hand-made card carries the compound-level assertions (DCA and PDK2 tool compounds; stiripentol, GSK2837808A and nedosiran; none for the diet). The join has **no path from an adapter result to a drug assertion**; that is a module gap, not a gap in the biology, and it is why the E-series cards exist beside the derived ones.
For E04 the two agree on the abstention.

## 5 Verification commands (rerun to check)
```
python3 disease-models/wwox/research/drug_repurposing/cards/check_cards.py          # 16 packets checked, 0 problem(s)
python3 framework/scripts/repurposing_join.py run                                   # second run: 0 changed
python3 framework/scripts/repurposing_join.py queries | grep Q-R-1                  # Q-R-10, Q-R-11 with their origin lines
python3 framework/scripts/repurposing_join.py handoff --date 2026-10-26 --write disease-models/wwox/research/repurposing_batch_selection_20261026_module.md
python3 framework/scripts/repurposing_join.py diff Q-N-08 disease-models/wwox/research/drug_repurposing/cards/E03_pdk_inhibition_dca.card.json
```
After the integrator appends the two staged leads (`discovery_lead.py append --staged --apply` on `main`), the join gains the two lead queries (evidence only, as measured in section 1); no further step is owed for the queue.
