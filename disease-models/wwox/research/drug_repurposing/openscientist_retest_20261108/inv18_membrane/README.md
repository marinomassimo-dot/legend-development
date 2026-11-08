# INV-18 membrane physiology, HCN and alternatives: reconcile with LEGEND (producer os-18, Phase 2, 2026-11-08)

Not medical advice; no dose, schedule or route; reference genotype class only. The report is external AI-generated material, assessed here, not instructions. Cap of newly read sources: 5 (see section i for the overrun).

## Answer first

* DATO: the report's central physiological datum is real and already held (Table 1 of PMID 34634460: neuron-deleted model, layer II/III, P13-17, acute slices); input resistance was measured (102.88 / 143.26 / 143.03 megaohm, WT / HT / KO, about 40 percent higher in both mutants), which the report missed, but its concern that sag was never normalised for input resistance stands in substance: the same -200 pA step was applied and sag is reported in absolute mV.
* INFERENZA: the report's parsimony argument (one Ih increase gives all three signs) and its H3 rejection test both lean on "sag is HCN-specific"; no source read establishes that sag is HCN-exclusive and none refutes it (one review calls it the hallmark, another calls it characteristic and modulated by co-expressed channels); exclusivity is the report's premise. The H3 test is circular because the report's own table gives "No" for sag under H1/H2 and under H3.
* DATO: the "restraining Ih" counterevidence is one thalamic rat model (GAERS, neuron-level burst result) plus a thalamic knockout for rebound; the GAERS authors themselves doubt that compensation is tied to seizure development, and in that model the increased Ih came with lower input resistance and unchanged resting potential and sag, so it did not reproduce the report's triad. "Multiple models" overstates it.
* DATO: ivabradine's anti-absence effect was largest on injection into the cortical initiation network (seizure time cut by 96 percent against 40 percent in thalamic VB), and it removed sag in normal cortical layer 5/6 neurons; the report's "thalamocortical, not neocortical" contrast is partly reversed at the injection site (the cortical slice data are from normal Wistar rats). Elacridar is an efflux-transporter inhibitor used for exposure, not an HCN agent.
* IPOTESI: nothing new changes the first experiment already in the module: sag and rebound at matched starting potential and deflection, then Ih in voltage clamp, then separate cell and burst effects, with a second blocker chemotype.
* Not found: any WWOX measurement of Ih, Kv7, Cav3, membrane lipids or chloride gradient in neurons (bounded searches, `queries.tsv`; earlier bounded searches in `disease-models/wwox/research/drug_repurposing/hcn_20261107/output/queries.tsv`).

## a. Coverage

59 extraction items (Phase 1): limit 10, experiment 9, counter_evidence 7, observation 5, mechanism_step 5, hypothesis_favourable 5, compound 5, alternative_explanation 4, other 3, link_proposed 2, recommendation 2, inference 1, open_question 1. Cited sources: 23 PMIDs (all identities confirmed), 6 chains.
By `legend_class` (items): already_present_and_used 23; verified_or_corrected 17; present_not_used 12; new_to_legend 4; unverified 3; superseded_or_contradicted 0 (E46 reclassified after the audit).
By `prior_brief_fate` (items): modified 20; narrowed 17; kept 11; omitted 11.

## b. What the previous brief (`disease-models/wwox/research/drug_repurposing/hcn_20261107/BRIEF.md`) kept, narrowed, modified, omitted

* Kept: Table 1 and Methods reuse, matched-potential first experiment, sequence of voltage clamp then network effect.
* Narrowed: lipid precedent (bridge only, no supplementation proposal; preprint 37732182 is not independent), filamin A (precedent apart from the WWOX link), GSK3 (reuse cautions, no new lithium work).
* Modified: "HCN is a candidate, not an identification"; refutation criteria (sag removal without burst benefit supports HCN in sag, not refutes it; worsening is not compensation); TTX-deprivation adaptation not transferred to hyperexcitability; Kv7 and T-type arms separate; developmental trajectories not turned into opposite pharmacology.
* Omitted by the brief (not necessarily by the package): chloride gradient and bumetanide, GAERS Ih as counter-evidence, the CaV3.3 knockout, PIP2 sources, the ivabradine-elacridar paper, the Ih reversal-potential statement, WWOX serum lipid source details, SCR2682.

## c. Sustainable favourable reasons

* A larger sag and rebound with a depolarized rest are measured in the neuron-deleted knockout (cells as units; HT versus KO untested).
* Ivabradine blocks sag and hyperpolarizes cortical L5/6 neurons in normal rat slices (PMID 34018186), so HCN does contribute to sag and rest in cortex: this makes an HCN contribution testable, not shown in Wwox.
* The report's decomposition (HCN, K+/leak, T-type) matches Branch D and the module's T-type package; the H2 gating route is a coherent hypothesis whose bridge is missing.

## d. Errors and counter-evidence found

* "No input-resistance control": read literally (no Rin measurement) it is wrong, Rin is in Table 1; read as the report's parenthesis (sag depends on Rin) it stands, since sag was not matched or normalised (reconcile row E46, verified_or_corrected). Also missing: Ih in voltage clamp, isoform quantification. Review 37982354 notes open HCN lowers Rin, while Wwox shows depolarisation with Rin up, a fewer-open-conductances pattern the report does not address.
* "Culture-class preparation / immature in-vitro model": the held model is acute slices, P13-17; TTX-deprivation in cultures (PMID 33547341) is a different condition.
* "Multiple models" for restraining Ih: GAERS thalamic neurons and a thalamic reticular knockout; no neocortical L2/3 case; seizure restraint not shown.
* Sag exclusivity: no source read establishes it and none refutes it; the H3 sag test is circular by the report's own table (`decisive.tsv` D01).
* "Thalamocortical, not neocortical" for ivabradine: the source includes cortical injection and cortical-neuron sag block.
* "Corroborated by" counts reviews and a preprint of the same work (37732182) and a same-laboratory DRG study (41818135) as confirmations.
* "Bumetanide failed" is adult epileptogenesis in rats with low brain penetration; it does not test chloride in immature or Wwox tissue.
* 25760945 is a Cdk5 to Cav3.1 regulation paper; its rebound sentence is background, not a finding.
* "Ih reverses near -30 mV": uncited in the report; the only Ih value found is in review 37982354 (around -20 to -30 mV), not to be confused with the -31 mV burst-current reversal in 34634460 Results 2.2; primary measurement not located (two classic reviews are not open access).
* Statistics of the source: sag(HT), rebound(KO) and rest(HT) p values are not reproducible under assumed Welch/SEM; no contradiction of the paper is asserted (operator rule: no definitive contradiction using a model the authors did not declare); the unit of the authors' test is not stated.

## e. Hypotheses still explorable, and what weakens them

* H1 (more HCN function): weakened if, at matched potential and deflection, Ih density, V1/2 and surface HCN1 are the same in KO and WT; supported for sag only if a verified, engaged blocker removes the excess sag.
* H2 (gating by membrane lipids): a conditional question with no WWOX bridge; weakened by no difference in neuronal membrane cholesterol/PIP2 or in V1/2.
* Scaffold route: needs a WWOX-HCN1 or WWOX-filamin interaction; none found.
* H3 (non-HCN composite) and Branch D: weakened if blocker-sensitive K+ currents do not differ; a Kv7-opener rescue would not prove a Kv7 lesion.
* Chloride arm and GSK3 arm: no triad-level datum; explorable only as separate arms.

## f. Priority question / experiment

At matched starting potential and matched peak deflection in KO, HT and WT cells, does the excess sag and rebound persist, and is the ZD7288-sensitive (and second-chemotype-sensitive) current different in voltage clamp? Replicates are animals (5, 6, 15 in Table 1).

## g. Consequence for drug repurposing

No compound is nominated. Novelty classes: Ih-blocker tool arm with two chemotypes: already_in_legend (INV-18); Kv7 opener as an RMP probe: already_in_legend as a lead, SCR2682 itself new_to_legend; T-type blocker arm: already_in_legend (T-type package); bumetanide/NKCC1 arm: new_to_legend, weak (null in another system, poor penetration); cholesterol or PIP2 manipulation: new_to_legend as a hypothesis, no WWOX bridge; GSK3 arm: already_in_legend; ivabradine as a tool or candidate: new_to_legend at source level, transfer from absence-epilepsy model only. Literature novelty: not assessed.

## h. Consumers to update

None needs changing for the main conclusions. Candidate wording notes for the integrator (not applied): NEED-INTRINSIC-EXCITABILITY/INV-18 could add (1) "ivabradine removes sag and hyperpolarizes cortical L5/6 neurons in normal rat slices" as an HCN-contribution precedent (PMID 34018186), and (2) the GAERS authors' reading of compensation (PMID 24953239) next to the "discordant precedents" text. Both are additions, neither changes a rank.

## i. Not reachable, caps and overruns

* Newly read with staged receipts (5, validated by `staged_receipt_check.py`): 37982354 (full text by pattern search, partial_fulltext), 34018186 (partial_fulltext), 36099307 (partial_fulltext, computational paper), 24953239 (partial_fulltext, re-read; prior complete receipt exists), 20573906 (abstract_only). Receipts are in `receipts/` with `INDEX.tsv`.
* Overrun: 14 further sources were read at abstract level through the PubMed tool or Europe PMC records without receipts (25071191, 31063701, 25760945, 28912545, 29867437, 40953803, 24871327, 41818135, 17074978, 17605039, 23055973, 39793889, 36271927, 25491415) to answer what the listed PMIDs actually say; they carry `abstract_only` in `evidence.tsv` and no claim beyond the abstract. Reading claims were made for the five receipted PMIDs only and after the texts were opened (late); no reading claim exists for the 14 abstract-level PMIDs (`queries.tsv` Q10).
* Not reached: Methods and figures of the new full texts; the primary measurement of the Ih reversal potential; Supplementary of any source; PMC full text for 20573906 (stub only); 41818135, 31063701 and the other abstract-only papers beyond the abstract.
* Not done: reopening of 34634460 (reused); no bridges.tsv or probe_links.tsv (no relation read in a source that the validators accept).

## j. Queries run

`queries.tsv` (Q01-Q12).

## Audit appendix (blind verifier vf-18, 2026-11-08)
Verdicts on the 14 decisive propositions: 13 SUPPORTED (D02, D06, D08, D10 with a correction or caveat; D07-D10 and D12 at abstract depth only), 1 PARTLY (D01: the ivabradine/sag datum and the circularity of the H3 sag test hold, but "sag is not an HCN-exclusive signal in the sources read" said more than the sources do; reworded). None NOT SUPPORTED, none UNVERIFIABLE; sub-parts not checked by the verifier: 33547341 (D04) and the 22989944 sodium-current clause (D06). Coverage check of the first extraction: 12 points sampled across the report, 12 PRESENT, 0 PRESENT_NARROWED, 0 MISSING; one accuracy defect (E25 note wrongly said the poor-penetration statement was uncited; it is cited at L59 to 20573906), repaired. Reconciliation sample: 8 rows, pointers exist; E46 class overstated and changed to verified_or_corrected; E09 and E10 notes widened; the "only in" claim for 25071191 was incomplete (deepdive_manifests/PMID35243344.json also lists it). Evidence sample: no fabricated quote, none over 25 words; V02 is the converse of the proposition it backs, V03 shows modulation only, V01/V04 escape sequences and garbled unit cleaned, V15/V17 system fields trimmed to what the abstracts say, five rows added for 34634460 (V28-V32) so D02 and D05 are traceable. Narrowings applied: D02 premise not simply wrong; D03 value kept apart from the -31 mV burst-current reversal; D04 counter-instance (lower Rin, unchanged RMP and sag in GAERS); D06 injection site reverses the thalamocortical contrast in part; D09 combination behavioural effect; D10 lithium-in-wild-type marked as background knowledge; anchors L50 (D04) and L35 (D07) dropped. Operator rule kept: no p value or statistic of the source is asserted as contradicting the paper; a recomputation under assumed Welch/SEM is reported only as not reproducible under those assumptions. Not reached: Methods and figures of the new full texts; Fig 6 panels (legend text only); 33547341 and 22989944 not re-read; Europe PMC absence screens covered titles of the first 10 hits per query; no os-18 reading claim for the 14 abstract-level PMIDs.
