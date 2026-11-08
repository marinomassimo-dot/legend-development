# Engine consumption (Package A, producer mh-a)

Not medical advice; no dose, schedule or route; reference genotype class only. Nothing here is applied.

## Where each hypothesis would be consumed

| Hypothesis | Need | Investigation | Where | Open question it would feed |
|---|---|---|---|---|
| MH1 passive size plus conductance-level reading (exploratory) | `NEED-INTRINSIC-EXCITABILITY` in `disease-models/wwox/research/drug_repurposing/needs/needs.json` (fields `observed`, `inferred`, `counter_evidence`) | `INV-18` in `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/investigations_it20.tsv` (field `decisive_uncertainty`, field `next_test`) | Text of `inferred` and `next_test` only | Does the excess sag and rebound persist at matched potential and matched deflection, with capacitance reported? |
| MH2 HCN contribution after matching (exploratory, tool arm) | same need | `INV-18` (`intervention`, `question`) | Already carried by INV-18; the additions are the engagement-first order and the sag-removed-without-burst-benefit reading | Is the ZD7288- and ivabradine-sensitive current per pF different in KO, and what does each blocker do to bursts? |
| MH3 recording, selection and network-state control (exploratory) | same need (field `observed` limits, `counter_evidence`) | `INV-18` (`decisive_uncertainty`) | Limits text | Were intrinsic properties recorded under synaptic blockade, with identity independent of Rin and tau? |

The view card for INV-18 and the three-language content files under `disease-models/wwox/research/drug_repurposing/view/i18n/` carry this text downstream; no card was opened or edited here, so a card id is not named. No ranking promotion is proposed and none of the hypotheses changes the direction state.

## Format limits (precise)

* `bridges.tsv` (validator `check_bridge_row` and `BRIDGE_FIELDS` in `framework/scripts/repurposing_search.py`: gene_a, hgnc_a, relation, gene_b, hgnc_b, status, context, evidence_ref, note; no sign or direction column; both genes must carry an HGNC id). A conductance-level hypothesis cannot be expressed: MH1 is a statement about cell capacitance, resting K+ conductance and a matched-potential comparison, with no gene pair read in any source, and a gene-gene link would have to be invented. None is written; no `bridges.tsv` is delivered.
* `probe_links.tsv` (`PROBE_FIELDS`: probe, catalogue_id, identity_key, identity_source, target_group, target_members, action_term, kind, evidence_ref, limits, not_shown). A tool such as ZD7288 or ivabradine could in principle be a row with target group HCN channels, but this package adds no mechanism the catalogue lacks, and the Kv7 openers were read at abstract level only, so no row is delivered. A Kv7 opener row would also have to name KCNQ members, which the abstract-only reads do not allow me to state beyond what the abstracts say.
* `needs.json` `observed` entries carry `locators`, `readout_level` and `limits`; there is no field for the comparison condition "matched potential and matched deflection", for capacitance, for access resistance by genotype or for "recorded under synaptic blockade yes/no". These can be stated only in free text in `limits`. A structured field for recording conditions would let the view show that Table 1 is a fixed-current comparison. This is a limit of the format, not a request made here.
* `investigations_it20.tsv` has one `next_test` string per investigation; it cannot hold three separate experiments with their own decision rules (E1 to E5 in `experiments.tsv`).
