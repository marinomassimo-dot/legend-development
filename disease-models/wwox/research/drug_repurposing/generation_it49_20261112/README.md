# IT49: from conditional hypotheses to useful generation

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. IPOTESI throughout. No rank, sign, tier or qualification changed; no predictive improvement is claimed from better access to knowledge.

## 1. The eight reachable-but-unmapped hypotheses now act (P4)
State recomputed from the manifest (`hypothesis_package.hypotheses_for(INV-18)`), not assumed: the unmapped set was exactly SCI43 KH1-KH5 and HCN HY1-HY3 (the two INV-18 packages whose layouts differ from the three mapped in IT47).
| | before (IT48 tree) | after |
|---|---|---|
| package rows read by the generator | 16 (3 packages) | **24 (5 packages; 5 layouts)** |
| reachable and unmapped | 8 (KH1-KH5, HY1-HY3) | **0** |
| cells kept per row | observation, relation, context, action, premise, rivals, measure, expected | the same plus **`reopen_or_abandon`** (the package's own weakening or opposite cells; "not stated by the package" for the earlier 16) |
| context join | per package | **per row** (`symbols_by_key`: KH1 Kir2/K2P genes, KH2 Kv7 genes, KH3 and HY1-3 HCN and Kv7 genes) |
| dashboard reader rows | 4 | **6** (+ KH1-K, HY1-HCN), five languages |

Mapping decisions (reviewable in `PKG_MAP`): what would **favour** or **weaken** a row (the packages' favourable and opposite or weakening cells) is a measurement outcome and goes to the measure and reopen slots, **not** to the expected result; where a package states no expectation (HCN rows) the slot says "not stated by the package (missing)". No direction is invented. The rival cell is the package's own where it has one (HY rows; KH rows via the opposite-context cell); otherwise the other rows are listed without calling them rivals. The mapping was fixed after reading one full row per package, so it is not a pre-registered mapping.
**KH1 carries the IT48 and IT49 limits** on its premise: a Ba2+ response does not identify Kir2 (it blocks Kir2-type, K2P-type leak and astroglial Kir4.1); shares from different preparations or cohorts are not additive; no measurement exists in the pertinent age band and layer, so the premise is unresolved and the 23 percent figure is a transfer from an older age.
Shown by running the path: `python3 generation_it40_20261109/conditional_proposals.py` (before: "reachable but not mapped: 8"; after: `{}`), then the reader rows and the five-language page. A row added to a manifest would not have been enough: the output and the page were regenerated and audited.

## 2. One bounded generalisation case (P5) — `p5_case_inv02/`
Selection rule fixed before any row was read (INV-02, ISR modulators). Result: the hypothesis layouts generalise by a manifest row and a mapping entry; a **design-only package** (steps, controls, branches) does not: the generator has nothing to read (IT49-Q03, to Harness). The simple target search gave 0 rows for the node the card cares about (eIF2B activation) and 6 of 12 rows that are not primary-target hits. The cell-class join is unknown for all 11 ISR genes (IT49-Q02, a zero-spend extraction). The first experiment did not change (the protein-level sign first); the plate content did (qualification of readouts, engagement control). Not shown: a better prediction. One retrospective case, scored by its builder.

## 3. SCI48 and the pilot close-out (P1-P3)
Dispositions in `../generation_it48_20261112/README.md`; the pilot balance is in the IT48 record.

## 4. Questions and priorities returned to the research loop (P6)
`IT49-Q01` (HY1: matched-excursion sag and Ih; **wet measurement**; decides whether K+/leak identity precedes any HCN lever), `IT49-Q02` (**reanalysis possible**: ISR gene class means), `IT49-Q03` (engine/infrastructure: design-only packages). Existing: IT48-Q01 (literature still executable: the Kir2 drug-name search; the share itself is a measurement), IT48-Q02..Q04 (SCI48). SCI49 had not been delivered when this note was written (`git log` of main), so nothing of it is consumed here.

## Limits
Translations are the assistant's (a sonnet delegate produced the twelve new passages; the checker verified identifiers and numbers, not fluency). Reader rows for six of the eight new rows exist only in the generator table, not on the page. The dashboard still shows the first-screen "where to begin" table unchanged: no new kind of next step appeared.

## 5. The generative reading (operator integration, 2026-11-12)
Four questions asked of this cycle's work, answered from what exists on disk; the count of rows consumed measures accessibility, not benefit.
| Question | Answer | Evidence still missing |
|---|---|---|
| Which previously unused knowledge now permits a hypothesis? | KH1-KH5 and HY1-HY3 (eight conditional INV-18 hypotheses, each with observation and source, relation, preparation and cell context, premise, rivals the packages declare, a measure, a reopen or abandon condition) are rows the generator reads and the dashboard shows two of; KH1 carries three limits that stop it being read as a Kir2 share | that the rows change a later choice |
| Which compound, probe or comparison becomes pertinent? | HY2: an Ih tool blocker with a second structurally different blocker and a separate T-type arm, always with engagement shown; KH2: a Kv7 opener as a mechanism comparator in the spiking range, not for resting Rin; KH1: **no** tool exists (no Kir2 activator in the catalogue), so the honest output is a measurement first; INV-08: two reagents become comparators (SCI48) | that any of these separates a mechanism in a Wwox preparation |
| Which experiment separates the rival explanations? | HY1: matched starting potential and excursion, sag and Ih (recruitment against more or different HCN); KH1: Ba2+-sensitive current per pF with synaptic blockers and a measured junction potential (difference-current ladder), then dynamic clamp (sufficiency only); KH5: capacitance, tau and age (maturation delay against a K conductance lesion); HY2: sag removal with engagement, then bursts | a slice measurement (IT49-Q01) |
| Which new questions deserve depth? | IT49-Q01 (wet), IT49-Q02 (reanalysis), IT49-Q03 (engine), IT48-Q01 (literature still executable: Kir2 drug-name search; the share itself is a measurement), IT48-Q02..Q04 | priority by value of the next discriminating test, unchanged |
A favourable result would also feed the return loop (a thread that survives its own refuting measure can merit depth); none of the eight rows has such a result yet. Permanent home of the orientation: the standing method of `roadmap_current.md` (one bullet added).

## Update 2026-11-13 (IT50; the text above is kept)
SCI49 packages A and B were delivered after this note was written and are consumed (IT49 commits 2454a3ac and 387f6ae4; ledger 1,865 then 1,903); the line above that SCI49 had not been delivered is historical. Current references: open questions IT49-Q04..Q11 (from SCI49), IT48-Q01 evidence (drug-name half concluded). The INV-02 case's conclusion that a design-only package cannot be read still stands; IT50 restated the ISR hypotheses in the generator's layout (`../isr_inv02_it50_20261113`) while Harness builds the minimal design link.
