# V2.1 through the v2 generator (HE, 2026-11-16; a description of the instrument, not a score; no agent is recommended; not medical advice)

Written for: ADV, SCI, IT. Rule `rule_v2.json` sha256 2cb4a908... (checked by the generator); V2.1 cells = `V21_CELLS_SCI.tsv` blob sha256 84ee2332... (the frozen blob of ADV's merge note, checked by the script); origin ids mapped as ADV's note says (T26 to O-REPUDI21; T23 and T27 to the composite O-REPUDI21+O-P47T-GSE215425, one origin). Run A reproduces `scores_v2.tsv` byte for byte (run_note.txt). Reproduce: `python3 run_v21.py --repo . --out out`. Files in `out/`: cells and scores for A (v2 only), B (v2 + V2.1, mapped), C (B with O-BRETON21, O-REPUDI21 and the composite collapsed to one id, O-SLINE-S); `top_sets_compared.tsv`.

## The two numbers
| seizure endpoint | A: v2 only | B: v2 + V2.1 (mapped) | C: B, S-line overlap collapsed |
|---|---|---|---|
| pooled, top set by score_all | **4**: benzodiazepine, nmdar_pore_blocker, sodium_channel, valproate_type (all 9); label tie_set_weak | **1**: gabaa_neurosteroid_extrasynaptic (10 against 9 for five classes); label discriminating, informativeness 0.929, 14 scorable classes | **1**, same class, score_all 10 |
| P13-P15, top set | 4, same classes, tie_set_weak | 1, the same class | 1, the same class |
| later_unspecified, top set | 4, same classes | **5**: benzodiazepine, gabaa_pam_synaptic_selective, nmdar_pore_blocker, sodium_channel, valproate_type (all 9); not_discriminating | 5, same |
| P6-P8 and the development endpoint, every window | not scorable (null ordering) | not scorable | not scorable |
| origin-collapsed ranking, pooled | benzodiazepine 9, nmdar_pore_blocker 9, ampa_antagonist 6 | **neurosteroid 10**, benzodiazepine 9, synaptic-selective 9 | **benzodiazepine 9, synaptic-selective 9, nmdar_pore_blocker 9; neurosteroid falls to 6 (rank 6)** |

## What the numbers are made of (read before using them)
1. **The new top class is a class that entered the table.** In A both split classes (gabaa_neurosteroid_extrasynaptic and gabaa_pam_synaptic_selective) have no scorable cells (score 0, rank unscorable). V2.1 gives them their first cells (T23: two neurosteroid-type agents `match` at directness 2, two synaptic-selective agents `neutral`), which is exactly what R3 asked for. The top set shrinking from 4 to 1 is the instrument registering one more class with a match link, not an agent beating others.
2. **Against its degree-preserving null the new top class is not above chance:** null_ge_fraction 0.978 and excess −8.2 (the null mean is 18.2 against an observed 10), the same pattern as valproate_type (0.999), sodium_channel (0.968) and the synaptic-selective class (0.975). Only benzodiazepine (0.643) and nmdar_pore_blocker (0.682) sit near their null. So "discriminating" here means a one-point lead in a rank, not an excess over what the table's structure alone would give.
3. **The lead depends on whether the S-line is one origin.** C collapses the S-line deposits (Breton 2021 electrophysiology and Repudi 2021 transcripts, same consortium and line, ADV's caveat): the official score_all rank is unchanged (10), but the origin-collapsed ranking drops the neurosteroid class from 1 to 6 (score 6), because its only evidence now shares an origin with evidence the other classes already have (INFERRED from the rank change). The per-thread-sum view puts gabaa_pam_synaptic_selective first (36), neurosteroid second (32), benzodiazepine third (18): three views, three firsts.
4. **No outcome table was opened.** This run reads only the cell files and the frozen rule; nothing was compared with the sealed A1 table or any extraction (ADV's scoring perimeter).

## Limits
The V2.1 cells carry the axis `GABAergic-tonic` and the thread evidence tier 2 as SCI wrote them; the generator takes them as given. The S-line collapse is ADV's sensitivity, applied to every cell with those origins in v2 and V2.1 alike (A with the same collapse is byte-identical to A: v2 has no composite). Developmental windows stay unscorable because no V2.1 cell carries a window other than P13-P15.
