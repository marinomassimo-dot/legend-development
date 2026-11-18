# I18 · The PY-motif proteome test (HE, v1, 2026-11-16; non-canonical; hypothesis; not medical advice)

Written for: ADV, SCI, IT (second reader to be named). Mechanism level only. Reference genotype class only. Labels: HELD-DATA (table), INFERRED, ASSUMED. Files: `i18_proteome/PREREGISTRATION.md` (committed as f633ac494 before any fold change was joined to a motif; sha256 70067dee1baeb5a7c3f1f1d32cbd8ce1e3dbdff10c4e2a306fa186c62eb2d473), `parse_zeng_table.py`, `i18_analysis.py`, `results/`.

## Answer first
1. **Preregistered verdict: INCONCLUSIVE.** In the one protein-level WWOX perturbation table held (TMT proteome of WWOX-silenced human endothelial cells, Zeng 2024, PMID 38563965, Supplemental Table 1; 2,031 proteins, 2,025 analysed), proteins that carry a PPxY outside the extracellular and transmembrane parts (118 of 2,025) show a median log2 fold change **+0.0315** above matched non-carriers (matched by intensity decile and compartment; 108 carriers and 1,291 non-carriers in the 11 usable strata); permutation p 0.068; bootstrap 95% interval **−0.015 to +0.064**. The rule asked for |D| ≥ 0.05 with p < 0.05 and decoys below half of D for a SUPPORT, or an interval inside ±0.05 for a KILL; neither holds.
2. **What the interval does exclude (descriptive, not the preregistered verdict):** a fall of the carriers by 0.05 log2 or more (the shield variant M− at the size the rule named) lies outside the interval (the lower end is −0.015). A rise of 0.05 (M+) is inside it (upper end +0.064). The sign in the table, if anything, is the adaptor direction, small (about a 2% increase in abundance).
3. **The decoys shift the same way, about half as much:** PPxF carriers +0.0185 (p 0.25) and PPxA carriers +0.0157 (p 0.12), against +0.0315 for PPxY; the secondary sets are PPxY anywhere +0.0353 (p 0.042; one of five tests) and LPxY without PPxY +0.0383 (p 0.020; interval +0.003 to +0.075). With five tests the smallest p (0.020) does not survive a Bonferroni threshold of 0.01. The decoy shift is 0.59 of the primary one, above the rule's 0.5: the data cannot separate a PPxY-specific effect from a general small rise of proline-rich proteins.
4. **A limit that matters more than the number: this table has few membrane proteins.** 230 of the 2,026 proteins with a sequence carry an annotated transmembrane segment (11%), and of the 118 carriers 13 are membrane proteins and 105 soluble; only 3 membrane carriers fall in a usable stratum. So the test barely touches channels (of the channel genes of this round only SCN1A and the calcium-channel auxiliary subunit CACNA2D1 are rows; SCN1A is a one-row anecdote, see the note below, and not part of the test); it tests the broader claim ("loss of WWOX WW1 competition shifts the level of PPxY-carrying proteins") for soluble proteins only (post hoc split, labelled in `results_summary.tsv`: soluble-only D +0.0305, interval −0.017 to +0.062; membrane-only 3 carriers, uninterpretable). The channel claim of I8 is untested by it.
5. **Share view (descriptive):** among carriers 23 of 118 have BH < 0.05 and rise, 14 fall; among 1,466 clean non-carriers 225 rise and 153 fall (19.5% against 15.3% rise, 11.9% against 10.4% fall).

## D1 · Chain
(1) WWOX WW1 binds PPxY motifs (ASSUMED, general WW-domain knowledge; P47 sits inside WW1 16 to 49, HELD from UniProt). (2) NEDD4-family ligases read PY motifs (ASSUMED). (3) Silencing WWOX changes occupancy of PPxY motifs and therefore the level of the carrying protein, one direction for all carriers of a given kind (the hypothesis). (4) A protein-level table with partial silencing should therefore show a shift of carriers against matched non-carriers (INFERRED). (5) The held table is endothelial and soluble-dominated (HELD), so a null or small result speaks for that population only.

## D2 · Why it is non-obvious
Every earlier test of I8 was about channels and RNA. This one needs neither: it asks the protein table whether the motif predicts anything.

## D3 · Consequences and the surprising prediction
The prediction written before the result: carriers shift as one group, in one direction, in non-neural cells, with no channel in the table. The result is a small shift in the adaptor direction that the decoys partly share. The surprising-prediction criterion (a motif-specific shift of at least 0.05 log2) is NOT met.

## D4 · Model
None needed; the test is a matched, stratified permutation (seed 1, 10,000 draws) with a stratified bootstrap (5,000 draws). The matching removes intensity and compartment as explanations; it does not remove cell-type, function or abundance-class effects that correlate with proline-rich motifs.

## D5 · Experiments at three costs
(a) No new data: apply the identical script to any other protein-level WWOX perturbation table as it appears (none other is held); reduce the carrier set to proteins with a PPxY followed by an acidic or phosphorylatable context (a sharper motif definition, written before use) and to nuclear or cytoplasmic ligase-pathway proteins; the interval narrows with more carriers only. (b) One cell experiment: a membrane-enriched proteome (surface biotinylation plus TMT) of WWOX-silenced cells, so that channels and receptors enter the table; and a WW1-mutant (P47T-type) against WWOX-null comparison in the same preparation, so a PY effect separates from a protein effect. (c) Clinical: none.

## D6 · Intervention logic
None at this level: a table-level shift of soluble proteins names no agent. BLOCK-1 not applicable.

## D7 · Combination
I8 (channel route): unchanged by this table; the K2P/Kir/Kv7 kill stands; the Nav and interneuron-amplitude route stays. I4: the same table is a protein-level look at the metabolic panel for a different question; not done here.

## D8 · Stronger or killed
Stronger: a membrane-enriched proteome in which channel carriers move together, or a PPxY-specific shift in a second table. Killed (for this table, by the preregistered rule): not killed. The interval excludes carriers falling by 0.05 log2 or more; it does not exclude a small rise.

## D9 · Cheapest next step
(1) Preregister a sharper carrier definition and run it once (HE; no new data). (2) Ask SCI and IT whether any membrane-enriched proteome of a WWOX perturbation is held or public (HE can screen the public deposits for protein-level WWOX perturbation tables; a PRIDE or ProteomeXchange search is a lawful public read, not run here).

## Note: the one channel row
SCN1A (Nav1.1, a carrier with PPSY at 1983) is a row of the table: log2 fold change +0.02, BH-adjusted p 0.92, mean log2 intensity 19.2. This is one protein, looked up after the preregistered run (the rows of the I8 channels were not looked up before it); it is not a test. **Data-quality flag (ADV's request):** the accession is P35498 (human SCN1A, Swiss-Prot) and the intensity is at the 99.1th percentile of the table (max 20.1, median 16.3), which is unexpected for a neuronal sodium channel in cultured endothelial cells; the table carries no peptide-count or coverage column (its columns are row, protein, accession, BH-adjusted p, fold change and the two intensities), so the identification cannot be checked from it and the row should not be used as a measurement of Nav1.1 until the peptide evidence is seen. CACNA2D1 (an auxiliary subunit, not a PPxY carrier here) falls −0.35 (BH 0.0069).

## Limits
Endothelial cells, partial siRNA silencing, silencing efficiency not stated in the held text (a keyword search found nothing; WWOX is not a row of the table), biological n unknown ("run in triplicate" is all the methods say), mRNA of the same samples not held, 2,031 quantified proteins (the abundant part), 6 of 2,031 rows lost to a missing sequence or NA intensity, the motif regions rest on UniProt topology (soluble proteins are read whole), strata with fewer than 3 carriers or non-carriers dropped (9 of 20), per-protein fold changes of the third-party table are kept outside git (digests in the run note).
