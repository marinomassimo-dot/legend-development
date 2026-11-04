# IT23: what the external capabilities added to the generator, and what they did not (2026-11-03)

Non-canonical. Public edition. Not medical advice. Cases and the current method were frozen before any capability was tried ([`cases_it23_p1_20261103`](../cases_it23_p1_20261103/README.md)).
Everything below separates **capability technique** (it runs), **biological plausibility** (a reason to expect it matters) and **predictive performance** (a check against truth): no tool reached the third.

## 1. Result in one table (one probe per tool; decisions after independent verification, 34 findings)

| Capability | Decision | What it added to the calculation | What changed in a proposal or comparison | Why it stops there |
|---|---|---|---|---|
| EC-KG (Every Cure graph) | WATCH as a source; **one relation type adopted as a carried limit** | adverse-event reports (FAERS, CC0) as counter-evidence for a seizure disorder; a sign-discordance audit of LEGEND's action table | 31 family-level seizure-report signals (22 compounds) reach 31 proposal rows and 1 hand-over (tretinoin, Q5) as a limit; no eligibility, blocker or hand-over moved; the audit exposed 5 LEGEND-side suspect sign rows (panobinostat on SIRT1/2/3/7, idronoxil on CASP3) | 82-90 percent of LEGEND's signed pairs are already there; the table of events is incomplete by construction (direct WWOX neighbours only) |
| NORDic | drug-target step **REJECT**; Boolean what-if method WATCH | a reproduction of the aggregator's conversion defects (unknown or `binding` -> activation; presence-only and contrasting signs -> inhibition; and, found by the verifier, TTD `Inhibitor` -> activation: 45,449 of 45,453 rows) | a 21-node Q5 what-if (3,072 cells) separated interventions only through the assumed scenario | the direction of benefit is the scenario premise by construction; missing: the producing cell type, cytokine and pathway protein, a measured cytokine-to-myelin link |
| CANDO | WATCH | coverage and meaning of the signature (max over predicted pockets of ECFP4 Dice x site confidence, no direction) | none: the matrix cannot score any of the 16 hand-over families | 14 not approved and absent, 2 under unmerged identities; TR agonists and EZH2 inhibitors absent; the score has no direction, potency or exposure |
| dseqr + LINCS | **REJECT** as a route now | a keyless SigCom pass with 9 explicit role scenarios | top-20 Jaccard reverse v mimic 0.00; against LEGEND's lists 0.00 (2 compounds in depth, both on the opposite arm) | dseqr's data bucket returns 404 on 5 of 5 URLs; build scripts read author-local paths; 54 of 834 signature genes are landmark genes |
| Disease-module discovery | WATCH (abstention) | first neighbours, random walk, DIAMOnD-style on STRING and on LEGEND's own network, with seed/edge/hub sensitivity | Q3: 31 engine-new proteins, only 3 with a signed documented compound action; hub domination on LEGEND's network; Jaccard 0.30-0.48 under 10 percent edge removal | seed sets of 6-12 genes; Drugst.One's drug step is unsigned proximity, sends the gene list to a web API and turns off TLS checking |
| MolNexus | not usable; reopen when a root LICENSE and official checkpoints with checksum exist | nothing | nothing | no licence, no release, no checkpoint, no paper |
| DeepPurpose, drexml, GEMGen, RDKG-115, RECeSS/stanscofi, Open Targets MIRA, BitBIRCH | not tried | - | - | none of the trials left a concrete gap these would resolve (no missing interaction value, no circuit question, no usable hardware path, no measured catalogue redundancy limit) |

## 2. The five questions, for the one improvement that exists (the carried adverse-event limit)

1. **Knowledge now entering the calculation:** compound-level adverse-event reports (a relation type the generator had no table for), joined to families by exact normalised name with the route recorded.
2. **What changes:** the hand-over of tretinoin for the cytokine question now carries "FAERS seizure reports" among its limits; 30 other proposal rows carry it. No proposal is added, withdrawn or reordered.
3. **Why it is biologically pertinent:** the disease under study is a developmental epileptic encephalopathy; a compound that is reported with seizure events is counter-evidence to be weighed before any experiment, whatever its network score.
4. **What could refute it:** the reports are spontaneous and confounded by indication (an antiseizure drug is reported with epilepsy because it is used for it: the limit says so for ATC N03 drugs); the event set is incomplete, so absence means nothing.
5. **Second case:** it applies to every question's rows by the same family join (Q2, Q4, Q5, Q6 rows are flagged); the sign-discordance audit was developed on the same extract and applies to any signed pair.

## 3. Contrasting cases and the frozen current method

Q5 cytokines (best-sustained direction, role unknown), Q6 MYC (may be compensatory), Q8 NFE2L2 (inputs insufficient). Why: [`cases_it23_p1_20261103/README.md`](../cases_it23_p1_20261103/README.md). The NORDic what-if ran on Q5 only; Q6 and Q8 had too few usable seed rows. For Q8 the right output stays an abstention that names the measurement.

## 4. Contrary results, abstentions, residual gaps

- No sustainable emerging candidate came out of IT23, after pertinent trials: **the absence is a scientific result for these inputs**, distinct from the unavailability of single tools (MolNexus, dseqr's data).
- A measurement that would unlock more than any tool: per-contrast gene lists from one WWOX-loss deposit with threshold and direction fixed in advance (larger qualified seed set); protein/pathway readouts of the cytokine axis in the producing cell type.
- Unresolved: 5 LEGEND-side sign suspects (source check); the FAERS event table; the 613-family match list behind the 1,412 denominator is not committed.

## 5. Components

Adopted: the carried adverse-event limit (`relations_it23_p2_20261103/harm_context_it23.py`, optional file read by the generator), the sign-discordance audit, the deterministic tie-break in the hand-over. Kept as reference, not wired in: the Boolean what-if scripts, the module probe, the signature comparison. Removed from git: CANDO derived score tables (digests kept). Waiting: EC-KG as a source (revisit with a per-row sign origin), CANDO (revisit if the matrix covers the hand-over families and its data terms are read), MolNexus (condition above). Rejected: dseqr route, NORDic drug-target step, Drugst.One drug step.
