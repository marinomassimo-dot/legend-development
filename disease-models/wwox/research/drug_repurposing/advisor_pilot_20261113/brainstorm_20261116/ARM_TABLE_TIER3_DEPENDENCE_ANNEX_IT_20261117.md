# Dependence pass on the 24 cells whose best origin row is tier 3 (ADV-018; IT; host clock 2026-11-17 ~09:25Z; non-canonical; hypotheses; mechanism level; no agent, no dose; not medical advice)

Written for: ADV (assignment ADV-018, evaluation P23), SCI (revision 4 rows), HE. Notes-only annex on arm table v8 (cell ids as in v8; no table changed). Inputs: SCI's transfer table revision 4 keyed by cell_id (sha256 prefix fbe49b50), R4's columns (`it_r4_lever_table_20261117/`), the table of best tiers `ROW_LEVEL_TIER_V8_IT_20261117.tsv` made by `build_row_level_tier.py`.
## Premises corrected first (ADV's, confirmed here)
* **Row-level best tier per cell: 38 cells have a row naming them; best tier 1: 5; tier 2: 9; tier 3 only: 24; so tier 1 or 2 is 14 of 75 (0.19).** The reading-level figure of M078 (26 of 75; tier 3 only 11 among the 37 reading-origin cells) lets a reading's tier-1 or 2 row for ANOTHER arm upgrade a cell: it overstates. (ADV's reading-level recomputation gave 26 and 12: the 12th is C018, whose only origin is an assumption row; my 11 excludes it.)
* The 37 cells with no origin carry no sign (as v8 notes say); nothing in them depends on anything.
## Rule used for the two lists (mine, stated so it can be rejected)
CITABLE as a WWOX-specific lever in the next generation round = the cell's best row set contains a WWOX observation whose `direction_allowed` is not 'sign not entitled', **and** I find no qualifier that removes the entitlement; it is cited with its tier-3 label and its slice-line scope (S-KO is a protein-null background, class A, by R4). Everything else is PARKED with the deciding observation named. The mechanical rule would also admit C047 and C061; I park them and say why.
## One line per cell (best row type; dependence; list)
Dependence labels: **circuit** = R4's circuit-lever column (class-agnostic for the circuit step; the slice line that stands in is a class-A null background); **transfer** = a system transfer SCI already qualifies; **clinical** = counts of children, not a variant-class dependence.
| cell | arm | idea | best row(s) | dependence | list and deciding observation |
|---|---|---|---|---|---|
| C001 | T-type blocker | I1 | WWOX obs R03 ('may raise'; R08 not entitled) | circuit (class A background) | **CITABLE** (interval +) |
| C055 | T-type blocker (v3 row) | I1 | WWOX obs R03 + simulation R17a | circuit (class A) | **CITABLE** (interval +, duration 0) |
| C069 | postsynaptic scaffold restoration | LIVE1-H1 | WWOX obs R05a ('may raise', aggregated sIPSC) | circuit/adaptor-directed (needs protein retained) | **CITABLE at tier 3**, aggregated sIPSC only; per-cell sIPSC (authors' item 1) would test it |
| C006 | T-type blocker | I10 | transfer R13 (digenic mouse) | transfer | PARKED: a T-type effect on a Wwox-null burden measure in the paired slice design |
| C007 | NMDAR pore blocker | I1 | simulation R17c | circuit (class A) | PARKED: the paired slice drug test (a simulation cannot confirm itself) |
| C011 | NMDAR pore blocker | I4 | simulation R17c (the I1 sign carried to I4) | circuit | PARKED: same test |
| C015 | GABA-A PAM | I9 | simulation R17a; qualifier 'only after maturation' assumed | circuit | PARKED: sign at P13-P17 vs older slices |
| C018 | GABA-A PAM | I10 | assumption A01 | none | PARKED: no held reading; any burden readout under a GABA-A modulator in Wwox-null slices |
| C024 | sodium-channel blocker | I10 | WWOX obs R01 and simulation R17b, both 'sign not entitled' | circuit (class A) | PARKED: sign not entitled; the interneuron:pyramidal effect ratio of the agent class |
| C031 | substrate | I1 | R16 (MEF) not entitled; simulation R17c | transfer + circuit | PARKED: a neuronal metabolic readout in Wwox-null slices (the I21 trigger) |
| C035 | substrate | I4 | fly transfer R14, MEF R16, simulation R17c | transfer | PARKED: same trigger |
| C046 | persistent-sodium-preferring blocker | I11b | WWOX obs R04 (Table 1), not entitled | circuit | PARKED: a persistent-sodium readout (none held) |
| C047 | sodium-channel blocker (non-selective) | I11b | R01 'may raise', R04 not entitled, simulation R17b | circuit, conditional | PARKED (mechanical rule would admit it): aggravation only if the interneuron effect exceeds the pyramidal one by about 2.5 in log terms; unmeasured for any agent class |
| C049 | raised ambient GABA | I1/I10 | WWOX obs R05a, not entitled | circuit | PARKED: per-cell sIPSC and tonic current with a THIP reserve |
| C053 | T-type / valproate-type | I2 | clinical counts R18, not entitled | clinical | PARKED: outcome by class with n >= 3 children (the 8-PDF visit; the Argentina series' response table, if any) |
| C054 | NMDAR pore blocker (v3 row) | I1 | WWOX obs R02 not entitled; simulation R17c | circuit (class A) | PARKED: paired slice drug test |
| C057 | K2P/Kv7 leak opener | I8 | WWOX obs R08 not entitled (the '0' rests on HE's motif result, not a sign) | circuit | PARKED: leak and Ba2+ readouts; the juvenile Ba2+ share is still open (IT48-Q01) |
| C061 | GABA-A positive modulator | I17 | R08 'may lower' (Gabrd fall, not specific in direction), R18 not entitled | clinical | PARKED (mechanical rule would admit it): the Gabrd fall appears in an epilepsy line unrelated to Wwox (-0.66 in [4d]) and the held counts are 3 against 4; deciding: an onset-day split with >= 8 children per class or an E_GABA measure |
| C065 | PV-interneuron activation (transfer) | I5/I9/I10 | transfer R12 | transfer | PARKED: the Wwox-side premise (PV cells deficient) is unmeasured |
| C066 | T-type blockade / Cacna1g deletion (transfer) | I1/I10 | transfer R13 | transfer | PARKED: a Wwox-null background replication of the digenic result |
| C067 | genetic Ldh lowering (fly) | I4 | fly transfer R14, MEF R16 | transfer | PARKED: neuronal metabolic readout in Wwox-null slices |
| C068 | ENT1 inhibitor label | I4 | transfer R15 (adenosine not measured) | transfer | PARKED: adenosine measurement in a Wwox-null background |
| C071 | receptor assembly and ER export of delta-containing receptors | LIVE1-H4 | WWOX obs R08 and organoid O3, not entitled | class-agnostic for the lever; genotype-dependent for the line | PARKED: protein-level surface delta receptor (a transcript is not function) |
| C075 | endocannabinoid-type presynaptic brake | LIVE1-H6 | WWOX obs R08, not entitled | circuit | PARKED: no held readout |
**Counts:** CITABLE 3 (C001, C055, C069); PARKED 21. Dependence (my reading of R4's columns and SCI's rows, not measured): circuit-lever 13 cells (C001, C007, C011, C015, C024, C046, C047, C049, C054, C055, C057, C069, C075), system transfer 7 (C006, C031, C035, C065, C066, C067, C068), clinical 2 (C053, C061), none 1 (C018), class-agnostic 1 (C071).
## Limits
Tier is SCI's cap, not mine; a WWOX observation at tier 3 is a limited observation (one pool per arm, aggregated values), not a null result; 'citable' means 'may be cited with its tier-3 label', not 'supported for a drug'; no cell value or sign was changed here; the dependence labels are judgement. Not medical advice.

## Update 2026-11-17 (IT, host 11:39Z; wording from SCI's closure note IT56-Q05; the C069 line above is not edited)
* **C069 now reads:** "circuit/adaptor-directed (needs protein present; level not required to be wild-type; P47T: present in two matrices, level unquantified)". Before: "(needs protein retained)".
* **What changed:** the dependence wording only; "retained" implied an unchanged level that no held datum gives. C069 still depends on the variant being a protein-present one, which P47T meets, and on R05a (aggregated sIPSC, a null background).
* **What did not change:** C069 stays CITABLE at tier 3 (aggregated sIPSC only); no phasic measurement exists in P47T animals, so it does not become tier 2 for P47T; the other 23 cells, the counts (CITABLE 3, PARKED 21) and the dependence tally (circuit 13, system transfer 7, clinical 2, none 1, class-agnostic 1) are unchanged. Whether a scaffold-restoring lever acts through the WW1 groove is the I8 question, not this line's.

[Update 2026-11-21, RP-037 (IT): this annex holds no class-E row (its cells are circuit, transfer and clinical dependences). The class-E change (a conditional engineered-suppressor-tRNA class, NOT-RANKED against gene addition, RP-015's nonsense half narrowed and not closed) is recorded as a dated update line under the RNA-directed row of `it_r4_lever_table_20261117/R4_LEVER_TABLE_BY_CLASS_IT_20261117.md`; no cell of this annex changes.]
