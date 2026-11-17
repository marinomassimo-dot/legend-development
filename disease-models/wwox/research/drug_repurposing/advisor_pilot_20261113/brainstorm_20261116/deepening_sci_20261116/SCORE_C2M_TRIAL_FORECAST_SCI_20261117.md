# Score of my independent forecast of the class-to-member trial (SCI, 2026-11-17; non-canonical; scored literally with HE's definitions; not blind; IT scores independently)

Forecast: `PREDICTIONS_C2M_TRIAL_SCI_INDEPENDENT.md`, sha256 148ee1eb8eec4f30395e9c2f301f9d79230b025b82dd654dbec87a5f65f0c5f0, written 08:41:45Z, before the run; I knew the T7 result and the atom and said so in the file. Outputs read after the digest message: `OUT_A1.txt` (sha256 bf0b1429...), `OUT_A2.txt` (1a7a5676...), `OUT_B1.txt` (422af974...), in HE's scratch folder `set3/c2m/`; scoring definitions from `C2M_TRIAL_FOR_FORECASTER.md` (9bb57120...). HE's own result file was not read.
## What the three outputs contain (my reading)
* **A1 and A2 (input A, no zinc): zinc does not appear at all (0 hits for zinc or Zn in either output).** The metal-ion class gets three members each: Mg2+ (raises), Mn2+ (raises), and Ca2+ with chelators or Ca2+ substitution (lowers). The final 'LOWERING MEMBERS' lines carry Ca2+ and chelators and no zinc.
* **B1 (input B, zinc already listed as a supply item):** zinc is kept twice with direction 'lowers': row 10 ('Ca2+ / Zn2+ (competing divalent cations)', 'compete for the metal sites and inhibit cyclase catalysis in vitro; relevance to GC-C in vivo is tentative') and row 60 (supply item 'Zinc', 'Zn2+ inhibits guanylyl cyclase catalysis in vitro and supports barrier function. Tentative'); the final line has 'Ca2+/Zn2+ competing cations'.
## Scored statements
| id | statement | my P | observed | ln score | coin |
|---|---|---|---|---|---|
| i-1 | STRICT (zinc lowering) in at least one of A1, A2 | 0.80 | **NO** (0 of 2) | -1.609 | -0.693 |
| i-2 | STRICT in both | 0.55 | NO | -0.799 | -0.693 |
| i-3 | exactly one of A1, A2 STRICT | 0.25 | NO | -0.288 | -0.693 |
| ii-1 | LOOSE (an ion other than Mg2+ and Mn2+ listed as lowering) in at least one of A1, A2 | 0.93 | YES (Ca2+ in both) | -0.073 | -0.693 |
| ii-2 | LOOSE in both | 0.80 | YES | -0.223 | -0.693 |
| iii-1 | B1 keeps zinc with direction 'lowers' | 0.65 | YES | -0.431 | -0.693 |
| iii-2 | B1 lists zinc as 'raises' or supply only | 0.20 | NO | -0.223 | -0.693 |
| iii-3 | B1 does not list zinc | 0.15 | NO | -0.163 | -0.693 |
| x-1 | Mg2+ and Mn2+ both 'raises' in A, both runs | 0.90 | YES | -0.105 | -0.693 |
| x-2 | the final line includes zinc, given zinc listed as lowering | 0.95 | YES (B1) | -0.051 | -0.693 |
| x-3 | members listed for the metal-ion class per run, median 5 (3 to 8) | - | A1 3, A2 3, B1 4 (in the (a) block; more in (d)) | within range, below the median | - |
| x-4 | of those lowering, median 2 (1 to 4) | - | A1 1, A2 1, B1 2 | within range, at or below the median | - |
Eight statements are events of two independent questions (i-1, i-2, i-3 are three views of one event; iii-1 to iii-3 a partition); counted all together: **-3.97 (mine) against -6.93 (coin)**; counted once per event (i-1, ii-1, iii-1, x-1): -2.21 against -2.77. **The headline miss is i-1: I put 0.80 on zinc being listed as lowering in at least one of A and it was listed in neither.**
## What this says
1. **The class-to-member step did not recover zinc on the enumeration that lacked it.** A1 and A2 gave the class 'Mg2+/Mn2+ metal site' its natural neighbours (Mg2+, Mn2+, Ca2+, chelators) and stopped; the model that, asked as a probe, knows zinc as a cyclase inhibitor (HE) did not retrieve it when the question was framed as members of that class. So my expectation that a tool-free model asked for members with the explicit instruction 'include members that lower' would reach a metal it knows was wrong: **knowledge in memory is not retrieval by member under a class framing**, and my 0.80 treated them as the same.
2. **The step keeps what the enumeration already holds** (B1: zinc kept twice, as lowering). Whether the step helps therefore depends on whether the class-to-member input contains the member's neighbourhood; on A it did not. This is consistent with the set-3 reading that the failure on T7 sits where the class and its members are demoted or not named, and not in the model's knowledge.
3. **What I got right:** the loose count (a non-Mg, non-Mn ion listed as lowering: Ca2+, both runs), the directions of Mg2+ and Mn2+, and B1's behaviour on a zinc already present.
4. This is a development trial on a tuned-on target with two A runs and one B run; no claim of improvement; the trial result by HE is the owner's.
Limits: three runs; my statements i-1 to i-3 are one event; 'member of the metal-ion class' was read as any metal-ion row in the (a) block; I did not read HE's own scoring.
