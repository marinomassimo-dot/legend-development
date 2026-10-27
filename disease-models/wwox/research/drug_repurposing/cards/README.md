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
| `P4-A-01` | A · Q230P-class missense recovery | 4-phenylbutyrate class and bile-acid chemical chaperones | controversial | UNRESOLVED | `7eebb5ed2106299775e78c6a0ff505d71140fcaa123daf83e69437036fc5236f` |
| `P4-A-02` | A | Proteasome-inhibitor class (degradation blockade) | hypothesis | UNRESOLVED | `dccbcd5b0b5c9f657fa9287cea5554fc87b8e9b7fc2e726af45ed87c7bbde972` |
| `P4-A-03` | A | Client-binding pharmacological chaperone | abstention | UNRESOLVED | `5e4ae43e3b1ee1d1b0c18c2ad4c8eba69a9f0ec180e9ba6a519cd90c02b40bd6` |
| `P4-A-04` | A | ER-proteostasis regulators (UPR/ERAD) | abstention | UNRESOLVED | `23b2a4839e74483cbaf3065aa054581b92661ed919473c3f1398d0610407ceaf` |
| `P4-A-05` | A | HSP70-axis modulation | abstention | UNRESOLVED | `77435531ca722e59b67e2bf0e0150ce4099563bd9be2a642f60a4bb9c3068dfe` |
| `P4-B-01` | B · premature-stop-codon read-through | Amlexanox (qualified, not promoted) | deferred with reason | UNRESOLVED | `a18010935432097cf57cb81e37da0bdc091e5864d089764d864d4cc7e7dfcdf2` |
| `P4-B-02` | B | PTC read-through class for nonsense alleles | abstention | UNRESOLVED | `50d6bb33272ddd378d91c41338cfefa18a44ae383d25e9a60b887be2f88b2ae4` |
| `P4-C-01` | C · restoration of WWOX expression | AAV9-delivered human WWOX | hypothesis | OPPOSES_DISEASE_CHANGE (inside the Wwox-null mouse, one endpoint) | `e9948aa8dc70bf3c450e47f633674da42191f0efdc2313bae76433da62316a3c` |
| `P4-C-02` | C | Splice-correcting ASO / editing | abstention | UNRESOLVED | `a317cfa159e006c7364a841c755d628d21d47512539627809eb70eece28883c8` |
| `P4-C-03` | C | Endogenous boost (CRISPRa or equivalent) | abstention | UNRESOLVED | `590778e336c1fa7916033cbd7c318846c8b7e09d0388cfde0b3aeb64b6817e1e` |
| `P4-D-01` | D · downstream pathway (Wnt/MYC) | A51, a multi-kinase inhibitor; BLOCK-1 open | controversial | UNRESOLVED (one assertion opposes, one is not comparable) | `309bdb13c11de85bfed3d8654750001949e20178f62857c7d1aac4071447c87b` |
| `P4-D-02` | D | Wnt-lowering (tankyrase-type) agents and GSK3 modulation | abstention | UNRESOLVED | `870d6aabd0537095f1b1ca658ab4c5351dbf37210f33164e7e3a0ce4a88409ba` |

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
- A measured null (not significant, not rescued) is encoded `NO_CHANGE`, which the bridge (commit
  `b96e4cd9`, after the first build of these cards) now distinguishes from `UNKNOWN`: five
  assertions use it (`DR-A01-003`, `DR-A01-004`, `DR-A02-003`, `DR-B01-002`, `DR-D01-002`). In a
  cell that is not comparable it stays `UNRESOLVED`, with the reason that it is a measured null.
  `UNKNOWN` therefore still means owed.
- The cards were rebuilt after that bridge change; `translation` (including `access` = time to
  access and `time_to_benefit`) is now filled from the packet, and `p4_roadmap_fields` carries the
  two roadmap rows the bridge validates.
- After the blind audit of R1 (2026-10-22) the R1 statements used here were re-read against the repaired note:
  no card cites the withdrawn PB-4 limitation of polysome-based evidence; `DR-A01-005` and the
  `P4-A-01` text were corrected (butyrate is a partial, variant-dependent dissociation of quantity
  from function; a binding, thermal-stability or folding measurement is "not established here").
- Statements marked INFERENZA in a card are owed a blind audit by someone else; so are the
  card-level syntheses. The audit of some R1 triples that another actor is running in parallel
  was not available to these cards.
- Not carded, deliberately: candidates of the other path (BENEFICIO_PRECOCE: ethosuximide,
  lithium, pro-myelinating, mTOR and symptomatic agents), because this task is
  RECUPERO_PROFONDO only. They are not discarded and their absence here is not a verdict.
  *(2026-10-27, package W1.1: lithium (`G01_lithium_gsk3`), memantine (`F01_glutamate_receptor_node`) and the AAV9
  endpoint families (`C04_aav9_endpoint_families`) were carded from evidence already in the repository; the
  classification of every derived card against the curated set is in the module README, section "Roadmap
  iteration 2, package W1.1".)*

Regression: `python3 disease-models/wwox/research/drug_repurposing/cards/check_cards.py`.
