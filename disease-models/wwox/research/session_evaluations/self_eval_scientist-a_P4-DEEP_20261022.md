# Self-evaluation — scientist-a, REPURP-10H-P4-DEEP-A-20261022, first RECUPERO_PROFONDO cards

## Scope and executable verdict

- Batch/session: roadmap P4, 5 cards and 7 abstentions under `disease-models/wwox/research/drug_repurposing/cards/`, note `disease-models/wwox/research/repurposing_10h_scientist-a_cards_20261022.md`.
- Studies and complete-read receipt IDs: none read in this task; the receipt ids quoted in the packets (presence-checked in the ledger by `check_cards.py`) belong to earlier readings.
- `session_self_eval.py`: workspace verdict FAIL, from seven `ORPHAN_COMPLETE_READ` items for R3 and R1 receipts of other actors (35372341, 36615165, 38147624, 40156289, 42154236, 42217144, 42157447); none concerns this task, which added no receipt, and none was touched (a red caused by a peer is reported, not fixed).
- Receipt verification: `fulltext_receipts.py verify` OK, 721 chained receipts, tail anchored.
- Structural LINT: GATE only BATCH_COMMIT blocked (the same orphans); `public_release_gate.py` PASS, BLOCKS 0, after the commit.
- Local verdict: `check_cards.py` 12 packets, 0 problems; every stored card equals what the bridge builds.
- Workspace/global verdict and concurrent conditions: global FAIL for peer items above; local PASS.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Not applicable: no paper was opened. The cards rest on receipted notes and two registry records fetched whole | partial (by design) | Everything inherited from R1/R3 partials stays partial |
| Main message and original contribution | A card is the qualified material shaped so that what is not known is visible; 12 packets, the favourable bridge matches (AAV9, A51 progenitors) each paired with a reading guard | strong | none |
| Hidden gold beyond keywords/abstract | The ER-retained-branch chaperone precedent is a membrane-client result and WWOX is cytosolic (DIS-004's wrong-compartment objection, live revival trigger); A51's favourable match hides a layer-neuron non-match; the bridge cannot hold a measured null | partial | the first is INFERENZA, audit owed |
| Source parity | Adjacent sources all labelled NOT WWOX EVIDENCE; WWOX-null mouse and organoid rows labelled as non-reference-genotype contexts | strong | none |
| Team type, field density, observation vs interpretation | Carried from R1/R3; not re-derived | partial | none new |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | Bridge forces IPOTESI on the card; assertions tagged DATO only for the source's own result in its own system; transfer statements INFERENZA | strong | audit owed on the INFERENZA ones |
| Existing claims touched | CLAIM 011 narrowing (threshold not continuum) carried as proposed, CLAIM 019, DIS-004 revival trigger, DL-THER-089 BLOCK-1; none edited | strong | none |
| Multi-hop and corpus cross-query | Not applicable; no new reading | n/a | none |

## Persistence diagnosis

- Durable ledger/registry IDs and wikilinks: no registry touched; packets cite CLAIM 003, 011, 019, 028, 030, 032, 040, TX-001..004, TX-007, DIS-004, DL-THER-089, DL-MOL-003 as text.
- Reading queue/debt: none created; inherited audits OWED for R1 and R3.
- Dossier and commit candidate: none; no claim narrowed in a registry.
- Receipt source fingerprint, coverage and supplement state: no receipt; the bridge's `input_sha256` for each packet is in the cards README in full.
- Can a future run distinguish full text from abstract only? Each assertion carries its `reading_depth` and receipt id; the A51 organoid reading is held at UNKNOWN to understate.

## Process and capability diagnosis

- Skills/gates/patterns used: standing brief, `registry_records.py get`, `repurposing_bridge.py`, `check_cards.py`, release gate, LINT.
- Plausible skills deliberately declined, with reasons: `legend-locator-audit` (producer is not verifier, audit owed to someone else); `legend-safety-triage` (BLOCK-1 triage of a molecule is for a promoted candidate, none promoted; no SMILES); `legend-discovery-method` (optional, no novelty claim made).
- Failures, retries, extraction mismatches or concurrency events: see census.
- What caught each failure before an overclaim: see census.
- Disease-agnostic micro-upgrade shipped: the bridge gap record G-1..G-3 in the capability scout log, and a card-consistency regression (`cards/check_cards.py`).
- Regression/evidence that makes the upgrade persistent: `check_cards.py` re-derives every card from its packet and fails on an absent P4 field.
- Residual risk and next decisive action: G-1 (measured null encoded as UNKNOWN) was closed by Harness commit b96e4cd9 and the cards rebuilt with NO_CHANGE; G-2 (one disease assertion per packet) remains open. Blind audit of the INFERENZA statements.

## Attribution census

Incidents, each counted once: (1) an author name the notes never gave, written into a draft packet, caught on my own review before the run; (2) five measured nulls forced into UNKNOWN by the bridge: I refused to let it pass silently and wrote the compensation and the gap; (3) the A51 organoid reading given a partial depth no source restated, caught on review and held at UNKNOWN; (4) a favourable `OPPOSES_DISEASE_CHANGE` on the AAV9 and A51 packets, reading as good news, for which reading guards were added; (5) the Q230P disease assertion first attached to the nonsense-allele abstention, caught on review; (6) the first two commits carried no attribution trailer because the commit wrapper takes the message as given, noticed at the third; (7) the commit wrapper refused a directory pathspec.

```
ATTRIBUTION_CENSUS
incidents: 7
machine: 1   blind_auditor: 0   peer: 0   self: 6
severity_high: 3   of which self: 3
undetected_known: 0
```

`undetected_known: 0` reports the limit of the census, not the absence of defects: no blind audit has run over this work, and one is owed.

## §21c output

`DEFAULTS_TAKEN` and `STOP_LOG` are in the task contract JSON `REPURP-10H-P4-DEEP-A-20261022`, top level and in `WAVE_1_RESULT`; `STOP_LOG` is empty.

## Capability outcome

Gap recorded as new in `capability_scout_log.md` (measured null, one disease assertion per packet, `translation` block with no input path); change to the bridge: none, it belongs to a Harness agent.

## Update 2026-10-22

The R1 blind audit (19 adverse triples) was repaired in a separate task; no card cited the withdrawn PB-4 limitation. DR-A01-005 and P4-A-01 were corrected for the repaired R1 wording; cards rebuilt against the new bridge. Unaudited.
