# Candidate cards (roadmap P4) — RECUPERO_PROFONDO, first set

Actor `scientist-a`, task `REPURP-10H-P4-DEEP-A-20261022`, written 2026-10-21. This subdirectory is
the work of one task and touches nothing else in `drug_repurposing/`. Non-canonical research
material: every card is `IPOTESI` (the bridge forces it) and **nothing here is medical advice**. No
score, rank, probability, blended index, dose, route, schedule or paediatric suitability is
carried; every adjacent source is labelled NOT WWOX EVIDENCE at class level. The analysis note is
[`../../repurposing_10h_scientist-a_cards_20261022.md`](../../repurposing_10h_scientist-a_cards_20261022.md).

## What a file is

| Pattern | Meaning |
|---|---|
| `<id>.packet.json` | The **input** in the shape of [`framework/scripts/repurposing_bridge.py`](../../../../../framework/scripts/repurposing_bridge.py) (schema 1). The roadmap's P4 fields that the bridge has no slot for travel as extra top-level keys (`p4_card`, `not_known`, `abstention_card`, `reading_guard`, `bridge_gaps_exposed`); the bridge keeps them unchanged under `input` and covers them with its checksum, and does not interpret them |
| `<id>.card.json` | What the bridge builds from the packet, unedited. Rebuild with `python3 framework/scripts/repurposing_bridge.py <id>.packet.json > <id>.card.json` |
| `check_cards.py` | Offline regression over this directory: the stored cards equal what the bridge builds; the P4 fields are present (UNKNOWN allowed, absent never); abstentions name their missing datum; no score/rank key; no dose-, schedule- or e-mail-looking token; every receipt id resolves in the ledger. Run from the repository root |

The files are named by axis and candidate; **the order is axis order, not preference**. An axis
listed first is not an axis ranked first, and "non-dominated" is a statement about visible
dimensions that this set does not make.

## The set (12 packets: 5 cards, 7 abstentions)

| Id | Axis | Candidate | State (roadmap vocabulary) | Bridge `directional_summary` | `input_sha256` (bridge, full) |
|---|---|---|---|---|---|
| `P4-A-01` | A · Q230P-class missense recovery | 4-phenylbutyrate class and bile-acid chemical chaperones | controversial | UNRESOLVED | `8bda86b67c901931ef690d628385e4f55211909abf92cd7b88125c813d1a2600` |
| `P4-A-02` | A | Proteasome-inhibitor class (degradation blockade) | hypothesis | UNRESOLVED | `41cfec0b025837ba21d8cba76aaaa17883092881bbd064a3eab90dff66f62dd4` |
| `P4-A-03` | A | Client-binding pharmacological chaperone | abstention | UNRESOLVED | `054448dd02c82f48fd30f4037313e102771b109e4940886d867792b3e2807e65` |
| `P4-A-04` | A | ER-proteostasis regulators (UPR/ERAD) | abstention | UNRESOLVED | `c5aa23aa1cb0b2ec83f4dd0513392305e42193aeb6366cca0afe68072abb6acb` |
| `P4-A-05` | A | HSP70-axis modulation | abstention | UNRESOLVED | `ace4fc6aa77951fff5e2156920e9b4599e84ddd7686bbe428439fdc2f3a46d7f` |
| `P4-B-01` | B · premature-stop-codon read-through | Amlexanox (qualified, not promoted) | deferred with reason | UNRESOLVED | `57dcf9652760c6feba88f6cd7a323f3e4852cb154d8603dbfee77307b0646dd7` |
| `P4-B-02` | B | PTC read-through class for nonsense alleles | abstention | UNRESOLVED | `28153494c7191320dc2ec30b3c1988909b20193c5dde40439fe46af0134ab9f2` |
| `P4-C-01` | C · restoration of WWOX expression | AAV9-delivered human WWOX | hypothesis | OPPOSES_DISEASE_CHANGE (inside the Wwox-null mouse, one endpoint) | `1ca52c7262409654926f5a15d6f7cb97581dc44dc7ca6a1bf9e71dfcdcfd7bb2` |
| `P4-C-02` | C | Splice-correcting ASO / editing | abstention | UNRESOLVED | `b84a5d002bc4ed655b0296dfcb7cc96ea351bac95754c41f4c18ca054fefa842` |
| `P4-C-03` | C | Endogenous boost (CRISPRa or equivalent) | abstention | UNRESOLVED | `9a9a3bda677f320f9859cbe66a603609a9b8a47a71883860a7e85d553c18f73b` |
| `P4-D-01` | D · downstream pathway (Wnt/MYC) | A51, a multi-kinase inhibitor; BLOCK-1 open | controversial | UNRESOLVED (one assertion opposes, one is not comparable) | `c630493956016b2eed2c39b61fef23d50b69bf7487ed7ab993d508e15143e22f` |
| `P4-D-02` | D | Wnt-lowering (tankyrase-type) agents and GSK3 modulation | abstention | UNRESOLVED | `72da2b7fe527cdb64bdef3e98a96414175f2aa4bcb6623950c07fda96628940a` |

`UNRESOLVED` on almost every card is the honest result and not a defect: **no drug assertion
exists in a context that matches the disease assertion**, because no drug has been given to any
WWOX model carrying a missense or splice allele. The one `OPPOSES_DISEASE_CHANGE` (`P4-C-01`) is a
sign comparison inside an engineered-null mouse on one endpoint; its packet carries a
`reading_guard` saying what it does not say.

## Read these before using any card

- `label_lookup` is `NOT_ATTEMPTED` on all twelve: the bridge has no network and no
  pharmacological-label search was run. It is not `NO_MATCH_FOUND` and says nothing about a label.
- `time_to_access` and `time_to_benefit` are separate fields on every card and are `UNKNOWN`
  wherever the repository documents nothing. The clinical census (no registered WOREE
  interventional study on that registry on 2026-10-20) is carried in every card with its own
  caution: *a missing hit does not prove that no study exists.*
- `NON_TROVATO_NELLA_RICERCA` is the novelty state for most candidates; it is never `MAI_TENTATO`.
  Each such state names where it came from (registry-based, dated 2026-10-20 or 2026-10-21) and
  that **no new query was run for the cards**.
- A measured null (not significant, not rescued) is recorded in an assertion's
  `measured_result_note` and encoded as direction `UNKNOWN` because the bridge has no value for it.
  There `UNKNOWN` does **not** mean owed. This is gap G-1 in the note.
- Statements marked INFERENZA in a card are owed a blind audit by someone else; so are the
  card-level syntheses. The audit of some R1 triples that another actor is running in parallel
  was not available to these cards.
- Not carded, deliberately: candidates of the other path (BENEFICIO_PRECOCE: ethosuximide,
  lithium, pro-myelinating, mTOR and symptomatic agents), because this task is
  RECUPERO_PROFONDO only. They are not discarded and their absence here is not a verdict.

Regression: `python3 disease-models/wwox/research/drug_repurposing/cards/check_cards.py`.
