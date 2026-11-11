# IT45: from recovered activities to contextualised pharmacological hypotheses and research priorities

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Drug repurposing for WWOX loss of function; gene therapy is outside these proposals. Every hypothesis here is IPOTESI unless a line says DATO or INFERENZA; no rank or clinical preference changes.

## What is in this folder

| Step | File | One line |
|---|---|---|
| P1 | `p1_comparisons_it45.md`, `p1_before/` | The ATP/scaffold comparisons recomputed with the HE45 condition reader: 0 role, tier or premise changes; a false COMPARABLE removed on 4 compounds; insufficiency is not equivalence. |
| P2 | `s10_dose/` (`selection_it45.md`, `result_it45.md`), `verify_s10/` | Pointers chosen before reading; one complete chain from observation to a reopened question, with an independent reader (8 corrections kept). |
| P2 | `s12_reopen/`, `s2_dose/` | Other relations: Kir4.1 (complete read, no activator), KCNJ16 (no target for the accession), an HCN1-selective probe pointer (data deposit, no paper read). |
| P3 | `p3_lever_it45.md` | A new combination: a Kv7 lever read against cell class, with relations, alternatives, discriminating results and falsifiers written before names. |
| P4 | `p4_filters_it45.md` | The coarse points measured: 7 pointers recovered from the potency flood, 1 wrong-target proposal avoided, the default `candidate` role replaced (Harness `unqualified_entity`). |
| P5 | `eval_it45.md` | Four conditions with separate measures and an independent premises check. |
| P9 | `../next_batch_it45_20261111/BRIEFS.md` | The next-batch brief. |

Consumed deliveries: SCI45 (`ph_k2p_sci45_20261111`, `k2p_pointers_sci45_20261111`, main a092e709): INV-18 pHo arm and stop criterion, open questions IT45-Q05..Q07, 39 receipts recorded (ledger 1,772). HE45 (main f76439c2): assay-condition reader, shared ChEMBL adapter, `unqualified_entity` role.

## Dashboard changes

Compound view V19 (NRF2 reagent pair, relation S10), V10 next-test and moves, INV-08 and INV-18 clauses, open questions IT45-Q01..Q07; five languages; the translations are the assistant's, not native-reviewed.

## DREAM (P8)

Cause: the next-batch briefs of IT44 and IT45 had no outside citer (*kept but hard to find*). Remedy: this README is the pointer from where a searcher of the IT45 folder starts; the IT44 brief is cited in `generation_it44_20261110/README.md`. Operational lesson (kept, not a new rule): a staged receipt whose `prior_receipt` is a higher event id must be recorded after it — `record_staged_receipts.py` now orders by prior, with a test. Connection: the pH question of SCI45 and the NRF2/Kv7 lever of IT45 both need one measured condition (tissue pH, cell class) before any compound; they are one shared measurement, not a shared cause.

## Limits

* 5 of 8 S10 documents were read only as abstract or ChEMBL copy; supplements not reached. S12 Kir5.1 unresolved. The S2 probe source is a data deposit; no paper read.
* The Kv7 premises (age, current at rest) are unmeasured.
* Reader and delegate full readings of three papers are not recorded as read receipts (residual debt).
* The comparison engine reads the producers' labels; no pH axis yet (SCI45 delta row 10 is with Harness).
* Translations unreviewed by a native speaker.
