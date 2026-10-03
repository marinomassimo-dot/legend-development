# COMMIT CANDIDATE — CC-20261003-B-HET-ENDPOINT-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 2 2026-10-03, branch `task/sci-B-20261003`.
**context_policy:** `SOURCE_FIRST` for all six readings; LEGEND's own records were opened only after each first pass was written (see `research/intake_wave_20261003_B.md`).
**Not medical advice.** Class-level statements about published models and genotypes only.

## Target
- `claim_registry_current.md`: **replace-within** `CLAIM 032` — record that the second half of its own `REVIVAL_TRIGGER` has fired, with the four limits that travel with the firing source, and restate the trigger.

## Change class
**MINOR** (§ 7). `CLAIM 032` is `in observation`, not `consolidated baseline`, and its status does not change. The edit appends to the record's closing `REVIVAL_TRIGGER` line and replaces nothing else.

🔴 **This is the edit most in need of a blind locator audit in this wave.** It brings evidence that bears *against* the «carriers are well» reading, from the same laboratory whose other heterozygote source this wave rejects. If the audit finds the n = 5 cognitive result overstated, this edit is the one to withdraw.

## Ordering
Apply together with `CC-20261003-B-ZFRA-TRANSFER-01`, so that `CLAIM 032` and `DIS-030` land in the same batch and no reader meets one without the other. `CC-20261003-B-REGISTRY-01` supplies `PAPER 135`.

## What fires, and what does not
`CLAIM 032`'s trigger reads: *«a powered survival comparison of a null heterozygote against wild type, or an EEG/cognitive endpoint in any WWOX heterozygote of any allele»*. The **second** disjunct fires: PMID 36498839 Figure 5A–C is a cognitive endpoint in a null `Wwox+/−` heterozygote. The **first** does not: no survival comparison is offered. No EEG or excitability endpoint exists in any WWOX heterozygote, which is why the trigger is restated rather than retired.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-03 against `main` eb01d5f: exit 0, key `['CLAIM 032']`, `replaced_bytes` 163, `inserted_bytes` 2046, lines 17–18, scope proof *bytes outside each edited range identical; every other block identical; record set as declared*)

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 032",
  "old": "`REVIVAL_TRIGGER`: a powered survival comparison of a **null** heterozygote against wild type, or an EEG/cognitive endpoint in any WWOX heterozygote of any allele.",
  "new": "`REVIVAL_TRIGGER`: a powered survival comparison of a **null** heterozygote against wild type, or an EEG/cognitive endpoint in any WWOX heterozygote of any allele.\n🟢 **The second half of that `REVIVAL_TRIGGER` has fired (2026-10-03, `CC-20261003-B-HET-ENDPOINT-01`, intake wave 2, Scientist B).** [[paper_registry_current#PAPER 135]] (PMID 36498839, read at source) measures a **cognitive endpoint in a null `Wwox+/−` heterozygote**: at 10–11 months the heterozygotes perform significantly worse than age-matched wild type on novel-object recognition and in the Morris water maze (n = 5, ANOVA with Bonferroni post hoc), and carry significantly more hippocampal TPC6AΔ plaques (** p < 0.01). That is the first endpoint of this kind in this corpus, and it bears **against** the reading that one functional copy leaves cognition intact. ⚠️ **Four limits travel with it, each measured at source.** (1) n = 5 per group, one laboratory, unblinded — `blind` and `randomi` occur zero times in the artefact. (2) The same figure's legend states n = 5 in one sentence and n = 20 in the next for the same panels, and its learning-curve axis is mislabelled *«% Exploration time»* for an escape latency. (3) The authors themselves report that pS37-TIAF1, TIAF1, wild-type TPC6A and pT181-tau are **not** significantly raised in the heterozygote, which they attribute to the remaining allele. (4) The other heterozygote source the corpus cites for this — PMID 29067327's supplementary figure — **does not survive inspection** and is rejected in `DIS-030`. 🔴 The claim therefore stays `in observation`: one unblinded n = 5 cognitive result from the laboratory that supplies the entire surrounding literature narrows the *«carriers are well»* reading but does not reverse it, and no EEG or excitability endpoint exists in any WWOX heterozygote. **`REVIVAL_TRIGGER` restated:** an independent replication of a cognitive deficit in a WWOX null heterozygote, or any EEG or network-excitability endpoint in a WWOX heterozygote of any allele."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT

(The heterozygote conclusion as the paper states it; the quote stops where JATS markup interrupts the run, and the sentence continues «Wwox gene in the gnome leads to memory deficiency» [sic] | `lacking one allele of ` | PMID 36498839, Results 2.5, 'WWOX Deficiency Led to Protein Aggregation and Memory Loss in Mice')

(Figure attestation: the heterozygote behavioural and plaque panel, and its internal n inconsistency | `[figure attestation - pixels cannot be quote-matched] Fig 5B left panel: y-axis '% Exploration time', x-axis 'Day' 0-5, two curves labelled Wwox+/- and Wwox+/+ with * at day 3 and *** at day 4; right panel '% Time in target quadrant' with 'n = 5' printed on the plot.` | PMID 36498839, Figure 5B, `files/figures/PMID36498839/native/ijms-23-14510-g005.jpg`)

(The other heterozygote aggregates the authors report as not raised | `Aggregation of pS37-TIAF1, TIAF1, wild-type TPC6A, and pT181-Tau were not significantly increased` | PMID 36498839, Results 2.6)

(The rejected alternative source's body sentence | `Wwox heterozygous mice exhibited an age-related faster decline` | PMID 29067327, Results, 'Wwox heterozygous mice exhibit enhanced memory decline')
