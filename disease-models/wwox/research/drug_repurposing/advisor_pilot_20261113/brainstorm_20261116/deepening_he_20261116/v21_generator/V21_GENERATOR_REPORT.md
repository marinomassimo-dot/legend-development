# V2.1 through the v2 generator (HE, 2026-11-16; revised after ADV's tier decision; a description of the instrument, NOT a score; no agent is recommended; not medical advice)

Written for: ADV, SCI, IT. Rule `rule_v2.json` sha256 2cb4a908... (checked by the generator); V2.1 cells = `V21_CELLS_SCI.tsv`, the frozen blob sha256 84ee2332... (checked by the script; the tier change below is applied by the script to a copy, never to the blob). Origin ids mapped as ADV's merge note says (T26 to O-REPUDI21; T23 and T27 to the composite O-REPUDI21+O-P47T-GSE215425, one origin). Run A reproduces `scores_v2.tsv` byte for byte (`run_note.txt`). Reproduce: `python3 run_v21.py --repo . --out out`.

**Disclosure.** My first report of this run used SCI's evidence tier 2 for the T23 cells and was sent before ADV decided the tier. ADV then corrected T23 to tier 1 (transcript-only threads are tier 1 in the matrix; IT, blind on T23, also read 1). The PRIMARY runs below use tier 1; the tier-2 runs are kept as sensitivity. **The decision moved the top set** (table).

**Perimeter.** V2.1 has no allowed outcome table yet: the sealed A1 table (08:11:55Z) and the I2 rows (17:43Z) existed before the merge commit (IT's confirmation). This output is an instrument description, not a score; nothing was compared with any outcome table.

## Side by side (seizure endpoint; P6-P8 and the development endpoint are not scorable in every run)
| | A: v2 only | B-primary: v2 + V2.1, T23 tier 1 | B-sensitivity: v2 + V2.1, T23 tier 2 (SCI's) |
|---|---|---|---|
| pooled and P13-P15 top set by score_all | **4**: benzodiazepine, nmdar_pore_blocker, sodium_channel, valproate_type (9); tie_set_weak | **5**: the same four plus gabaa_pam_synaptic_selective (9); **not_discriminating**; informativeness 0.643 | **1**: gabaa_neurosteroid_extrasynaptic (10 against 9 for five classes); discriminating; informativeness 0.929 |
| later_unspecified top set | 4, same classes | 5, same five; not_discriminating | 5, same five; not_discriminating |
| neurosteroid class: score_all and rank | 0, unscorable (no cells) | **8, rank 6** | 10, rank 1 |
| neurosteroid class: origin-collapsed score and rank | unscorable | 8, rank 4 | 10, rank 1 |
| neurosteroid class against its degree-preserving null (null_ge_fraction, excess) | n/a | 0.998, −9.6 | 0.978, −8.2 |
| origin-collapsed top three, pooled | benzodiazepine 9, nmdar_pore_blocker 9, ampa_antagonist 6 | benzodiazepine 9, synaptic-selective 9, nmdar_pore_blocker 9 | neurosteroid 10, benzodiazepine 9, synaptic-selective 9 |

| S-line collapsed (Breton, Repudi and the composite as one origin, O-SLINE-S) | C-primary (tier 1) | C-sensitivity (tier 2) |
|---|---|---|
| pooled top set by score_all | 5, same as B-primary; not_discriminating | 1, neurosteroid 10; discriminating |
| neurosteroid origin-collapsed | 6 (rank 6) | 6 (rank 6) |
| origin-collapsed top three | benzodiazepine 9, synaptic-selective 9, nmdar_pore_blocker 9 | the same three |

## Reading (instrument, not result)
1. **The tier decision decides whether the top set narrows.** At tier 1 the neurosteroid class enters the table at 8, below the nine-point class tie, and the top set GROWS from 4 to 5 (the synaptic-selective class also enters, at 9) and stays not discriminating; at tier 2 it enters at 10 and the top set shrinks to 1. Nothing else in the cells changed.
2. **In neither case is a new class above its null:** the neurosteroid class has null_ge_fraction 0.998 (tier 1) and 0.978 (tier 2); the synaptic-selective class 0.957 to 0.975; only benzodiazepine (0.595 to 0.643) sits at its null.
3. **Both split classes had no scorable cells in v2**: V2.1 is what makes them rows of the table, which is exactly what rule R3 asked for; the narrowing at tier 2 was the instrument registering a class that had been absent.
4. **S-line collapse:** the official score_all is unchanged; the origin-collapsed ranking puts the neurosteroid class at rank 6 in both tier settings, so its lead at tier 2 depends on counting the S-line transcripts as an independent origin from Breton.
5. Per-thread-sum ranks the synaptic-selective class first (36) in both settings (tier 1: neurosteroid 28).

## Limits
Tiers and axes are as SCI and ADV wrote them; the generator takes them as given. The tier change is applied by the script to the six T23 cells only (`with_tier`); T26 and T27 are tier 1 already. Developmental windows stay unscorable because no V2.1 cell carries a window other than P13-P15.
