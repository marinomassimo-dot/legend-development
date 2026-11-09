# Engine consumption (Package B, producer an-b). Proposals only; nothing is applied.

Not medical advice; no dose, schedule or route; reference genotype class only. No gene-gene link is written or implied.

## Where each hypothesis would be consumed

| Hypothesis | Need | Investigation | Card | Open question it would feed |
|---|---|---|---|---|
| BH1 AMPA dependence of the burst (exploratory) | `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR` in `disease-models/wwox/research/drug_repurposing/needs/needs.json` (fields `inferred` item 3, `notes`, `counter_evidence`) | `INV-05` in `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/investigations.tsv` (fields `decisive_uncertainty` and `next_test`) | `cards/F01_glutamate_receptor_node.card.json` (the perampanel arm in `p4_fields.endpoint_pursued`) and `cards/F04_nmdar_intervention_class.card.json` | Does the burst survive a verified AMPA/kainate block, and does AMPA block remove bursts at less total charge removed than NMDAR block does? |
| BH2 NMDAR composition at matched current (exploratory) | same need (`inferred` item 3 and `observed` O7 limit) | `INV-05` (`next_test` already names the matched-current d-APV and GluN2B NAM arms) | `cards/F04_nmdar_intervention_class.card.json`; `cards/P11_magnesium_nmdar_gate.card.json` for the bath Mg2+ prerequisite | Does a GluN2B NAM remove bursts at a smaller measured fraction of the isolated NMDAR current than d-APV needs, with Mg2+ and a measured slice co-agonist level stated for any GluN2A tool? |
| BH3 carbenoxolone attribution and a cleaner connexin or pannexin discrimination (exploratory; audit: close to a withdrawal of the gap-junction attribution) | same need (`observed` O4, `counter_evidence` gap-junction withdrawal) | `INV-05` (`decisive_uncertainty`, one added clause) | `cards/F04_nmdar_intervention_class.card.json` (limits) | Does a matched-effect control that lowers the evoked EPSCs by the same measured fraction reproduce the carbenoxolone burst fall, and does a Panx1 blocker with shown engagement change bursts? |

The view card text and the three-language content files under `disease-models/wwox/research/drug_repurposing/view/i18n/` would carry the wording downstream; no card was opened for editing, so no card edit is named. The GABA-A arm (M16), the kainate separation (M17) and the HCN pointer (M18) have no consumer beyond `INV-05` free text and the HCN package. No ranking promotion is proposed and no direction state changes: INV-05 stays at its present rank and its `direction_state` stays `resolved` for the d-APV result only.

## Format limits (precise)

* `investigations.tsv` (and `investigations_it20.tsv`), field `next_test`: one free-text string per investigation. It cannot hold three comparisons with their own decision rules, nor an ordered arm list (AMPA antagonist first, d-APV added only if bursts persist, positive-control d-APV last for non-reversing agents, washout order). The ordered application and washout schedule of `experiments.tsv` and `prediction_matrix.tsv` (columns `order_application_washout`) has no place in this field.
* `needs.json` `observed` entries (fields `statement`, `locators`, `readout_level`, `limits`): there is no field for a recording-condition covariate (bath Mg2+, K+, temperature, blockers actually present), for "measured versus nominal bath", or for a disagreement among text, legend, table and figure for the same quantity (baseline 2.29 against 0.84 per minute for the same 119 bursts; carbenoxolone n 36/4 against 13/6; brilliant blue FCF n 73/6 against 25/6; carbenoxolone amplitude as "no change", a median rise and a lower bar; Suppl Fig S1 counts 126 and 102+41 against 119; S3 latency n = 6 animals against 6 slices/3 animals; Fig 4 S-CTL 18 cells against 31; pooled-baseline unpaired normalisation in Fig 3D and Table S1). These can be written in `limits` text only, so the view cannot show which number a comparison may rest on.
* `needs.json` `intervention_direction` (fields `direction`, `on`, `certainty`): one direction on one entity. A matched-effect or matched-current design (the arm compares two interventions at an equal measured fractional effect, on at least two metrics, with a receptor-agnostic release-reducing control) cannot be expressed, and neither can a within-slice paired design; "down on postsynaptic glutamatergic gain" does not say whether the comparator is total NMDAR block, subunit-preferring block or AMPA block.
* `prediction_matrix.tsv` (hypotheses by arms) has no consumer: neither the generator nor the view has a table whose rows are experimental arms and whose columns are competing hypotheses. It stays in the package folder.
* `bridges.tsv` (validator `check_bridge_row`, `BRIDGE_FIELDS` in `framework/scripts/repurposing_search.py`: gene_a, hgnc_a, relation, gene_b, hgnc_b, status, context, evidence_ref, note; no sign or direction column): none of BH1 to BH3 is a gene-to-gene relation read in a source. Carbenoxolone, brilliant blue FCF and mefloquine act on channels and junction proteins; writing a pair such as PANX1 with a GRIN gene would invent a link and is not done. No `bridges.tsv` is delivered.
* `probe_links.tsv` (`PROBE_FIELDS`: probe, catalogue_id, identity_key, identity_source, target_group, target_members, action_term, kind, evidence_ref, limits, not_shown): perampanel, radiprodil and TCN-201 could be rows with target groups of AMPA receptor, GluN2B and GluN2A members, but this package did not check which of them the catalogue already lacks, and the AMPA-antagonist mechanism of NBQX and GYKI was not read; no `probe_links.tsv` is delivered.
* Hypotheses format (`hypotheses.tsv` of this package, the common-brief columns) holds a chain with DATO/INFERENZA/IPOTESI per step in one string; the generator's hypothesis record has no per-step label field, so the per-step labels would be flattened.

## New measurements, kept separate from literature

The following are experimental needs. Other literature cannot be presented as a substitute and the consumers should say "to be measured", not "known":

1. Recording Mg2+ and K+ as measured bath values, with temperature, perfusion and blockers actually present (M01).
2. A within-slice paired design (each slice its own baseline), because the source compares drug groups with one pooled baseline by unpaired tests.
3. Whether the burst survives a verified AMPA/kainate block (M07); abolition alone is not informative (loss of Mg2+ relief).
4. A receptor-agnostic release-reducing control and at least two metrics for every matched-effect arm (M08, M10), because a matched percent is metric-dependent.
5. The isolated NMDAR EPSC in the knockout slices and the matched-current curves for d-APV and a GluN2B NAM, including the NAM-sensitive fraction (M04, M05); M05 cannot split a GluN2A-diheteromer share from a triheteromer share.
6. The slice co-agonist level (glycine or D-serine) before any TCN-201 arm (M06).
7. Carbenoxolone's effect on AMPA and NMDA EPSCs, spike width, input resistance and coupling in these slices, with matched controls (M09, M10).
8. A Panx1 engagement readout in the slice before a brilliant blue FCF null is interpreted (M11).
9. A floor control for the delayed-response amplitude metric (wild type reads about 0.115 mV).
10. A GABA-A arm with an evoked IPSC and E/I measurement (M16; potentiator abolition alone is also predicted by H4); kainate separation is an open need until a tool and its mechanism paper are read (M17).
11. AMPAR/NMDAR ratio and AMPA EPSC kinetics in the knockout cells (the mEPSC shift is an AMPA inference only); evoked IPSC and E/I ratio.
12. Slice equilibration time for each drug at 35 C and the temperature mismatch with the source preparations (room temperature in culture, oocytes and the TCN-201 paper; 30-33 C in the radiprodil and Madry slices; 35 C in the WWOX preparation).
13. TTX/action-potential dependence of the burst, and heterozygote drug sensitivity (4 of 23 slices burst). Both are in scope as measurements, not as separate hypotheses.
