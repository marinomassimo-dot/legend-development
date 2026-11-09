# IT40 P2 — reconciliation of the membrane (7) and AMPA/NMDA (12) proposals with the consumers

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Sources: `it39_science_delivery_20261108/README.md` and the `consumer_delta.md`, `engine_consumption.md`, `experiments.tsv`, `prediction_matrix.tsv` of `membrane_hypotheses_20261108/output/` and `ampa_nmda_discrim_20261108/output/`. State of the consumers was checked at edfa347f before editing: none of the 19 was applied (grep for the wording in `needs.json`, `investigations_it20.tsv`, the packets). Applied by `apply_delta.py` in this folder (idempotent; every added text starts with `[IT40] <id>`).

States: **applied** (done in IT40), **applied, corrected** (applied with a change and the reason), **open-question row**, **out of scope**.

## A — membrane physiology (34634460 Table 1 and the HCN sources)

| # | Consumer | State | Note |
|---|---|---|---|
| A1 | NEED-INTRINSIC-EXCITABILITY `inferred` | applied, corrected | The producer's standard-error multiples (3.9 and 2.9 SE; z 1.6) were **not recomputed** here, so they are not carried; the printed-mean arithmetic (18.55 x 1.39 = 25.8 ms) is carried as an inference. |
| A2 | same, O1 `limits` | applied | Methods facts (K-gluconate, 3.5 mM K+, no junction correction, identity by Rin/tau, access resistance up to 40 MOhm, drug list without a synaptic blocker = inference). |
| A3 | INV-18 `decisive_uncertainty` | applied | Plus one sentence: a blocker response shows contribution, not a defect. |
| A4 | INV-18 `next_test` | applied | The E_K arithmetic belongs to a voltage-clamp difference current, not to the sag peak. |
| A5 | same need `counter_evidence` | applied, corrected | Wording "removes sag" of the IT39 line is corrected to "reduces"; the Fig 2 oral dose-response bars disagree with the text and no percentage is quoted. A concentration is quoted as printed (3 vs 30 micromol/L) in the need only; the cards forbid concentrations and do not carry it. |
| A6 | view text for INV-18 | applied | Carried in the INV-18 uncertainty and the need counter-evidence as a principle sentence. |
| A7 | probe notes | applied | Carried in INV-18 `evidence_available` as tool notes; no `probe_links.tsv` row (the catalogue gains no mechanism; Kv7 openers were abstract-level reads). |

## B — AMPA/NMDA discrimination

| # | Consumer | State | Note |
|---|---|---|---|
| B1 | NEED-EXCITATORY-GAIN `inferred` | applied | |
| B2 | same, O2 `limits` | applied | Corrects IT38: the d-APV residual is about 20 percent against the wild-type floor; figure-read, 10–15 percent. |
| B3 | same, O8 `limits` | applied | The disagreement list; comparisons may rest only on direction/non-recovery and incidence. |
| B4 | same `counter_evidence` | applied | Gap-junction half of carbenoxolone has no supporting datum; direct NMDAR block neither shown nor excluded. |
| B5 | INV-05 `decisive_uncertainty` | applied | Radiprodil/TCN-201 limits. The science session INV-05 delivery (`nmda_composition_discrim_20261109/`, in progress) may refine the GluN2B NAM range; not consumed until delivered. |
| B6 | INV-05 `next_test` | applied | Ordered arms live in free text only (format limit, see below). |
| B7 | card F01 (perampanel) | applied, corrected | Packet `not_known`; concentrations removed because the card checker forbids them (potency stated as submicromolar to about one micromolar). Card rebuilt from the packet, `check_cards.py` 0 problems. |
| B8 | card F04 | applied | Packet `not_known`: NBQX and GYKI 52466 are use-only, mechanism not read. |
| B9 | open question | open-question row `IT40-Q01` | New measurement; not answerable from other preparations. |
| B10 | open question | open-question row `IT40-Q02` | Matched-effect control for carbenoxolone. |
| B11 | open question | open-question row `IT40-Q03` | GABA-A arm. |
| B12 | tool routing | out of scope | No ranking change, no compound; mefloquine stays held (abstract only; the Cx36 full text unreachable). Recorded, nothing to apply. |

## Not applied, with the reason kept

* No `bridges.tsv` or `probe_links.tsv` row: a conductance-level or composition hypothesis has no gene–gene edge in any source read; writing one would invent a link.
* `prediction_matrix.tsv` has no consumer in the generator or the view (format limit). IT40 P5 gives it a minimal reader (Harness link, `hypothesis_package.py`) if delivered; otherwise it stays in the package folder.
* No rank, direction state or compound nomination changed.

## Receipts (21 staged, none a complete read)

Trial in a throwaway clone failed first on six receipts: three re-reads without a parent (34018186, 37982354, 40994429: parents set from the ledger to `-41`, `-41`, `-33`, reason `new_question_outside_prior_coverage`), and two `receipt_correction` events whose `analysis_at` differed from the corrected event (set equal to it). One cascade error (`-52` prior) cleared with its parent. No duplicate events; parallel readings of 34634460 (`-51` and `-61`) share the original parent `FTR-20261019-34634460-01`, `-62` corrects `-61`. Coverage vocabulary is unchanged: references are `not_read` in 18 of 21; 6 are abstract-only. No partial reading was recorded as complete.
