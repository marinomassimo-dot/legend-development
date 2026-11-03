# IT23 independent verification (2026-11-03)

Verifier, not producer. Public edition (WWOX-DEE reference genotype class). Not medical advice. Zero spend. Only key-less public endpoints were used (GitHub API and raw, Zenodo, PyPI, ChEMBL API, the TTD public file, the Every Cure docs page, AWS S3 status). No e-mail address or personal datum was sent, and no author was contacted. Downloads went to the session scratchpad only, at most 37 MB per item. Nothing outside this folder was edited, and no state-changing git command was run. The producer's WIP commit `4a150079` appeared during the verification and does not change the files checked.

Totals over 34 findings (`findings.tsv`): **14 CONFIRMED, 18 CORRECTED, 2 REFUTED**. Every number is in `recomputations.tsv`.

## Verdict per check

| # | Check | Verdict | One line |
|---|---|---|---|
| 1 | NORDic | **CORRECTED** (one sub-claim REFUTED) | The three lines, behaviours and directions are right. The mandate's "`?`/`binding` become inhibition" is false: in TTD they become **activation**, and only presence-only `*` becomes inhibition. Worse than recorded: line 313 is case-sensitive and the current TTD file writes `Inhibitor`, so 45,449 of 45,453 TTD rows, the inhibitors included, become **activation** (F01). "Single-commit repository" is false (216 commits). "Outcome tracks the scenario" holds by construction of the MYELIN_OL rule, not as a finding, and within a scenario the intervention decides everything (0 vs 32 of 32). |
| 2 | EC-KG | **CORRECTED** | 971/15/106, 17,068 and 97.3 % reproduce (definition-dependent, node-pair units). The 1,271 includes 113 pairs found only in text-mining rows (1,158 = 82 % with a non-prediction edge), and the 1,412 denominator cannot be reproduced from committed files. "536 activity-level signs" contradicts the stated rule: 12,068 under it, because LINCS signatures are labelled `activity_or_abundance`. The licence split is correct and conservative. The harm table is incomplete by construction (only WWOX-neighbour disease nodes, so no generic "Seizure"), and its family map is name-based, with one mis-join (citrate anion to lithium citrate). |
| 2b | 15 sign discordances | 9 EC-KG wrong, 5 LEGEND-side suspects, 1 identity artefact | Details below. |
| 3 | CANDO | **CONFIRMED** (one scope correction) | All coverage, join and licence numbers reproduce. "No selection changed" is true but only by absence: 0 of 16 hand-over families join the matrix, and the producer never ran that test. |
| 4 | dseqr / SigCom | **CONFIRMED** (minor corrections) | NoSuchBucket 404 on 5 of 5 re-tested URLs. 13 `/home/alex` files confirmed, of which about 6 are matrix builders. 36 of 36 Jaccards recompute exactly. "Fixed 4 uM / 6 h" applies to 14-17 of the top 20, not 16-18. |
| 5 | Module discovery | **CONFIRMED** (minor corrections) | DIAMOnD MIT, ROBUST and ROBUST-bias-aware GPL-3.0, Drugst.One client MIT. The client POSTs the gene list to `https://api.drugst.one/task/` with `verify=False` (TLS verification off), which is new. Abstention is the right reading, and LEGEND-network DIAMOnD leave-one-out (mean 0.52-0.56, min 0.05) strengthens it. "45 do not" should be 42. Q3 is the integrated stress response, not "interferon-stress-response". |
| 6 | MolNexus | **CONFIRMED** | No licence, no release, no tag, no checkpoint, 3 commits. The demo is about 154 MB, not 190. |
| 7 | Generation S5 vs P4 | **CORRECTED** | Proposals: exactly the 42 harm families change, and only in `carried_limits`; status, eligibility and hand-over are unchanged; summary, clusters and carried decisions are byte-identical; `--no-v1` byte test passes (46 OK). In the handoff file, 3 non-harm rows changed `direct_acting_hits_same_set`. The cause is a pre-existing PYTHONHASHSEED-dependent tie-break (line 790), reproduced by two re-runs. |
| 8 | Overstatement scan | see list | 16 sentences, listed below. |

## The three most important findings

1. **NORDic TTD encoding inverts inhibitors (F01, HIGH).** `("-" if m in decrease_expr_MOA else "+")` with a lowercase list against TTD's capitalised MOA strings: 29,740 `Inhibitor`, 3,555 `Antagonist` and 237 `Blocker` rows all become +1 (activation); 4 of 45,453 rows become -1. The producer's reproduction applied line 313 to lowercase synthetic strings and could not see this. Decision change: **the NORDic drug-target aggregator should be REJECT**, not merely part of a WATCH. The `mpbn` what-if method can stay WATCH.
2. **The S5 FAERS limit rests on an incomplete, partly name-matched table (F15, F16, F23).** The table holds only events whose node is a 1-hop WWOX neighbour (all 986 FAERS rows in the extract are N1). The commonest seizure term is absent, and the README's count (26 compounds) does not match the table's 25. "id join, never a name join" holds only for the last step: 411 of 663 compound nodes reached their families by name, and `citrate(3-)` flags LITHIUM CITRATE ANHYDROUS. The limit wording ("absence would not mean safety") is honest, but a limit that silently omits most seizure reports should not be called final.
3. **"Nothing else changed" in S5 is not byte-true for the hand-over (F21).** `sorted(set(v), key=lambda x: -x[1])[:6]` picks the top 6 phase-4 compounds by set order. Re-running the committed code with PYTHONHASHSEED 1 and 2 gives different handoff files, while proposals, clusters, summary and carried decisions stay identical. The S5-vs-P4 handoff difference in that column is noise, not the FAERS change. Fix: tie-break by name.

## 15 sign discordances: which side is right

| Pair | LEGEND | EC-KG | Judgement | Confidence | Basis |
|---|---|---|---|---|---|
| PAC-1 / CASP3 | +1 | -1 | LEGEND right: procaspase-3 activator | high | Putt et al. 2006, Nat Chem Biol |
| Regorafenib / EPHA2 | -1 | +1 | LEGEND right: Eph2A inhibited | high | Stivarga US label, section 12.1 |
| Dactolisib / PIK3CB, PIK3R1 | -1 | +1 | LEGEND right: pan-class-I PI3K inhibitor (PIK3R1 is a complex-level annotation) | high / medium | Maira et al. 2008, Mol Cancer Ther |
| Eptotermin alfa (BMP-7) / BMPR1B, BMPR2 | +1 | -1 | LEGEND right: agonist ligand | high | EU SmPC (Osigraft) |
| Dibotermin alfa (BMP-2) / BMPR1A, BMPR1B, BMPR2 | +1 | -1 | LEGEND right: agonist ligand | high | EU SmPC (InductOs) |
| Cyproterone / PGR | +1 | -1 | Identity artefact: EC-KG node CHEBI:50742 is free cyproterone, matched by name to the CYPROTERONE ACETATE family (ChEMBL: PR agonist) | medium | ChEMBL mechanism, CHEMBL139835 |
| Panobinostat / SIRT1, SIRT2, SIRT3, SIRT7 | -1 | +1 (prediction) | **LEGEND-side suspect**: hydroxamate pan-HDAC inhibitor of zinc-dependent classes I, II and IV; sirtuins (class III, NAD-dependent) are not established targets. Both signs unsupported; drop or guard the 4 rows | high | Farydak label; Atadja 2009, Cancer Lett |
| Idronoxil / CASP3 | -1 | +1 (prediction) | **LEGEND-side suspect**: induces caspase-dependent apoptosis, so inhibition is implausible; EC-KG's +1 is an indirect effect, not a target action | medium-low | Kamsteeg et al. 2003, Oncogene |

The `reading` column's "both sides have a non-prediction origin" does not show that the EC-KG sign comes from a non-prediction row (F14).

## Overstatement scan: sentences stronger than the evidence

1. NORDic README: "Single-commit repository". False (216 commits).
2. conversion_defect.md: "the statement given in the brief is right in effect". It misses the case-sensitivity inversion (F01).
3. NORDic README: "Which outcome follows is set by the scenario, not by the intervention". True by construction for direction only; within a scenario the intervention decides.
4. NORDic README: "RELA/STAT3 drive all three transcripts". STAT3 has no TNF edge.
5. EC-KG README: "1,271 of the generator's 1,412 signed pairs (90.0 percent) are already in EC-KG". Includes prediction-only rows; 82 % otherwise.
6. EC-KG README: "Only 536 carry an activity-level sign". 12,068 under the stated rule.
7. EC-KG README: "expression aspects give no sign, the same discipline the generator applies". LINCS signatures pass as `activity_or_abundance`.
8. sign_discordance `reading`: "both sides have a non-prediction origin". Pair-level, not sign-level.
9. harm_context_it23.py: "id join, never a name join". The family map upstream is name-based for 62 % of nodes.
10. EC-KG README: "26 matched compounds with a seizure-type adverse event in FAERS". The table has 25, and N1-only.
11. CANDO README: "What it could change: nothing in LEGEND's current selection". Never tested on the hand-over; true only by absence.
12. dseqr README: "16 to 18 of the top 20 ... at a fixed 4 uM and 6 h". 14-17 at that dose and time.
13. dseqr README: "the build scripts read ... (13 files)". 13 files carry the path; about 6 are builders.
14. Modules README: "45 do not". 42.
15. Modules README: "interferon-stress-response seeds". Integrated stress response.
16. MolNexus README: "about 190 MB in git". 154 MB.

## Decisions I would change

| Item | IT23 decision | Mine | Why |
|---|---|---|---|
| NORDic drug-target aggregator (NORDic_DS) | inside WATCH | **REJECT** | Inverts TTD inhibitors (F01); unknown and contrasting signs become inhibition; the TTD URL is dead (F05) |
| NORDic `mpbn` scenario method | WATCH | WATCH (keep) | Structural only; the direction is the premise by construction |
| EC-KG as action source | WATCH | WATCH (keep) | Confirmed: redundant on actions, CTD/LINCS-dominated |
| EC-KG FAERS limit in S5 (de facto adopted) | adopted as a carried limit | **WATCH until fixed** | Rebuild from all hoods and drop counter-ion nodes (F15, F16); otherwise acceptable as annotation |
| CANDO | WATCH | WATCH (keep), reword | Cannot score any hand-over family |
| dseqr | REJECT | REJECT (keep) | Bucket gone, confirmed |
| Module discovery / Drugst.One step | WATCH / REJECT | keep | Strengthened by `verify=False` and DIAMOnD instability |
| MolNexus | not usable | keep | Confirmed |

In addition, fix the hash-seed tie-break at line 790 of `run_generation_it21.py` before any byte-equality claim on a v1 handoff.

## What could not be verified

- That TTD's served file is the version NORDic's authors saw. The case problem holds for the file served on 2026-11-03; older TTD releases were not checked.
- The source row behind each EC-KG discordance sign. Restricted rows are digests without direction; only cyproterone/PGR has a visible DrugCentral `affects` row.
- The 1,412 denominator: the 613-family node match is not committed.
- Whether FAERS rows for generic "Seizure" nodes exist in the fetched set. N2 and unhooded rows are not committed, and the 1.2 GB graph was not re-fetched.
- The Hugging Face EC-KG mirror's content, the CANDO 665 MB matrix, and the MolNexus or KPGT terms (none fetched).
- The pharmacology judgements rest on the cited labels and papers as recalled and were not re-read in full text here. Treat the confidence levels as stated.

## Files

`findings.tsv` (34 findings), `recomputations.tsv` (every recomputed number with its source), `README.md`.
