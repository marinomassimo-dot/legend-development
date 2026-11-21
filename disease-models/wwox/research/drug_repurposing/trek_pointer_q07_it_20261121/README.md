# IT45-Q07 / ADV-149: potency and species of the TREK-1/TREK-2 dual-inhibitor pointer ONO-TR-772 (IT, 2026-11-21)

Question: what is the true human patch-clamp potency of ONO-TR-772 (15 nM or 0.15 to 0.26 uM) and its species; decision: which potency the K2P tool arm of INV-18 (ladder step 2b) carries. Tool-arm question only; no dose. Public, disease-level; not medical advice.

## Route result (stated before the reading was extended)
- Prediction fixed before the fetch: REJECT the 15 nM reading if the primary text shows it is not human TREK-1 or not manual patch clamp; otherwise it stands as a printed value with its method.
- Route: PMC open-data bucket text `PMC12067145.1/PMC12067145.1.txt` (one request, HTTP 200, 24,416 bytes, no challenge page). SHA-256 `0fd006949e81c64d5a3b6f962c2ef45df2a15f7066a7663bbfcc704deb706399`, **identical** to `source_fingerprint` of the two receipts FTR-20261111-40365404-85 and -86 (SCI 2026-11-11, partial full text read with SI Tables S2 and S3). The map row said the primary was "not read"; it was read on 2026-11-11. The 2026-11-15 package tried the PMC article page (reCAPTCHA, a stop, not solved) and did not know of that bucket read.
- This session re-extracted only the passages below (a targeted check of the same bytes, not a new complete reading), so no new receipt is recorded; the complete reading stands under the two receipts above. `verify_quotes.py` re-checks the quotations against the text (not stored here; fetch as in its header).

## Verbatim passages (Tanaka 2025, ACS Med Chem Lett, PMID 40365404)
1. Abstract: "a potent (TREK-1 IC50 = 15 nM), selective (>10 μM versus other K2P channels except TREK-2), and CNS penetrant (rat K p = 0.98) TREK inhibitor".
2. Main text, K2P profiling paragraph: "14c proved to be >67-fold selective over other K2P channels".
3. Same paragraph: "In human manual patch clamp (MPC), 14c was a potent TREK-1 inhibitor (IC50 = 15 nM), and therefore, more accurately described as a dual TREK-1/2 inhibitor."
4. Same paragraph: "we evaluated 14c in mouse MPC, and it was a potent TREK-1 inhibitor (IC50 = 67 nM)".
(14c = ONO-TR-772 = VU6018042.) The Tl+ flux IC50 0.26 uM (Table 3, Fig. 4) and the QPatch value 0.15 uM (SI Table S2 p. S4) are from the 2026-11-11 reading (`k2p_pointers_sci45_20261111/verify/verdicts.tsv` D02); this main text carries neither a pH nor a temperature for the electrophysiology (the only temperature mentions are in a chemistry-scheme footnote).

## Result
- **The rejecting observation did not occur.** 15 nM is printed, in the abstract and in the Results, as a human manual patch clamp IC50 on TREK-1; the mouse value is 67 nM, also manual patch clamp. The stated species is human for 15 nM; the cell background of the manual patch clamp, protocol, pH, temperature and n are not stated in the main text (and, per the 2026-11-11 reading, not in the SI of this paper).
- The conflict is **by method, not an error**: 15 nM (human MPC), 0.15 uM (QPatch, SI), 0.26 uM (Tl+ flux). The ">67-fold" selectivity equals 10 uM / 0.15 uM (QPatch), not 10 uM / 15 nM (which would be about 667), so the paper's own selectivity arithmetic rests on the QPatch value. Which value is "the true" human patch-clamp potency is NOT decidable from this paper; only its authors can say.
- INFERENCE (not a source value): in the follow-up paper of the same group (PMID 41104520, held reading `it45_ph_series_it55_20261115/verbatim.tsv` V03, V42) manual patch clamp IC50 is 2.7 to 10 times below the Tl+ IC50 for other compounds of the series; for this compound 15 nM against 0.26 uM is about 17 times and 15 nM against 0.15 uM is 10 times. That is outside, but not far outside, the range seen in the series, so 15 nM is not implausible as a manual-patch value, and it is not usable as a working concentration without its conditions.

## What the K2P tool arm carries (decision)
ONO-TR-772 enters a K2P tool arm as a probe-pointer with the potency **stated by method**: human TREK-1 manual patch clamp 15 nM (conditions not stated), QPatch 0.15 uM (TREK-2 0.17 uM), Tl+ flux 0.26 uM (HBSS with 20 mM HEPES, room temperature; pH not stated); mouse TREK-1 manual patch clamp 67 nM; species human and mouse, not rat. For planning a concentration, the earlier guidance stands (0.15 to 0.26 uM; `k2p_pointers_sci45_20261111/verify/audit.md`); the 15 nM is the lower printed bound. No pH series, no neuronal data, no tested second pH: it is a single-pH tool.

Stale statement noted, not edited (generated table): `generation_it40_20261109/conditional_proposals_packages_it47.tsv` row CP-ph_k2p_sci45_20261111::KP1 says the pointer "awaits a primary read"; the primary was read on 2026-11-11.
