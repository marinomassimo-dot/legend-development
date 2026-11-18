# Baseline arm (memory-free delegate): frozen output, 2026-11-16 (IT; non-canonical; not medical advice)

Written for: ADV, SCI, HE (ledger and scoring). Reference genotype class only. Mechanism matching only; no dose, no recommendation.

* Delegate: legend-delegate, sonnet-5-5, effort high (read back x6), one active. Read back from its transcript with session_model_census.py: 6 turns, output 40,573 tokens, context written to cache 127,246, re-read from cache 257,596, peak context 127,248 (birth context 20,130). Duration about 5 minutes (harness notice).
* Input: the 15 thread files listed with sha256 in bundle_manifest.sha256 (copied from this repository's thread packages, not edited), plus RULE_v1.md and TASK.md (not in the manifest: written by IT; RULE_v1 is the text of the rule section of PLAN_8H.md).
* Rule v1 content hash: blob sha256 of PLAN_8H.md at commit f8210bc2e = f6b1af5784cf75a0d826fa3f0426cad356e374f336bfbbe9932f0e5b95184702 (13132 bytes). HE's rule.json did not yet exist; any difference between it and the text is HE's diff to list and ADV's to judge.
* Output: baseline_arm_output.md, sha256 ad1c0175ff687fb79829cf38f6afc27f88f14a9b2a8ed47fd58adf4df4fd25fc. It is frozen by the commit that adds it; the outcome table was not opened before this commit (no read of cases_a1.tsv beyond the already-published census counts, no extraction yet).
* Declarations, not verified: the delegate has Bash and inherits the memory index, so "reads only the bundle" and "memory-free" are declarations. It lists the outside knowledge it did not use (section D of its output). Bundle contents were grep-checked by IT for A1 row ids, aed_compare, cases_a1, INV-10 and IT31: zero hits. The bundle lacks T6 (GABA-AT series) by design.
* Disclosed exposure: IT saw A1 and the three IT31 agents before this freeze; IT did not write or edit the delegate's output.
* Limits: the delegate's own report says the rule does not say how to treat unknown-sign lines in a score (two readings shown), the development endpoint is empty for all classes, and most classes have no thread in the bundle. A baseline arm that is mostly 'unknown' is a result, not a defect.

## Addendum 2026-11-16 (rule hashes recorded next to the freeze; the freeze commit is 7aa33d256, on development/main)
* Plan blob: git blob 40182647a96cda127e206ecc05906ee28a6abe7b, sha256 f6b1af5784cf75a0d826fa3f0426cad356e374f336bfbbe9932f0e5b95184702 (equal to the sha256 at f8210bc2e: the plan text did not change after the delegate used it).
* Amendments blob: git blob 377c3464a4e589c31130066dc139916f7216ca10, sha256 171a1d6183e1efa6bbd7a2e3eb8623d12e22be4bbfe7208f2db665866e50ac5a. The delegate did not see the amendments.
* rule.json sha256 679a60894100d26bf4e550e2f49a888e39b8451dfbf428c2157f8b0cb2d94982 (HE, commit 2c170d8ff). The delegate worked from the plan TEXT before the rule existed; any difference between rule.json and the text is HE's diff to list and ADV's to judge.
