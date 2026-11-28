# ADV-295 block 2, record 3 (PMID 35079122): blind reader report, verbatim

Subagent hand-back saved verbatim by SCI on 2026-11-28 (legend-delegate, claude-sonnet-5-5, effort high read back from the transcript). Model output, hypothesis level, not medical advice; not edited.

---

**Blind sentence-level reading: ADV-295 block 2, record 8 (PMID 35079122, Cabungcal 2022). Consumer DL-MECH-170. Hypothesis-level research only; nothing here is medical advice.**

Sentence judged: "The T-type change is lesion-specific in sign and age (an increase in Cntnap2, PMID 40834072; a decrease under developmental oxidative stress, PMID 35079122)."

Result: no MUST CHANGE. The decrease and its direction are supported, but cell type, species, readout, ages and models need to be added. The cross-lesion contrast cannot be decided, because PMID 40834072 is not held for this packet.

## 1. Verdicts

| id | verbatim statement | verdict | grounds |
|---|---|---|---|
| R8-S01 | "The T-type change" | ADD | The held paper measures T-type Ca2+ current density in thalamic reticular nucleus (TRN) neurons only: mouse, ex vivo slices at about 25°C, replicate unit the neuron. The sentence names no cell type, species or readout. Quote: "we found reduced T-Ca2+ currents in TRN neurons of young adult, but not peripubertal Gclm-KO mice" (Introduction, last paragraph). |
| R8-S02 | "is lesion-specific in sign" (meaning: the direction depends on which lesion) | UNSETTLED | The decrease side is held (S05). The increase side is not. The held paper has no Cntnap2 arm (search below). Whatever the other paper shows, this is a contrast between two studies, not a matched test of lesions, and should be labelled so. Within the held paper, every model that showed a change showed a decrease. The one rise is under NAC treatment, which is not a lesion (Fig. 3G, 3H). |
| R8-S03 | "and age" (meaning: the age of the change also depends on the lesion) | UNSETTLED | The age of the Cntnap2 change is not held. Within the held paper, age does depend on the insult. Gclm-KO alone: "hypofunction of T-Ca2+ channels in TRN of Gclm-KO mice emerges later during late adolescence/early adulthood" (Results, Fig. 2). With an early-life challenge, the decrease is present at PND20-30. The sentence itself gives no age. |
| R8-S04 | "an increase in Cntnap2, PMID 40834072" | UNSETTLED | Not held. It would have to carry a measured increase in T-type current (not only transcript or protein, unless the sentence says so), with cell type or nucleus (TRN, if it is to be compared), species, Cntnap2 genotype and zygosity, age, readout and voltage protocol, comparator and replicate unit. |
| R8-S05 | "a decrease under developmental oxidative stress, PMID 35079122" | ADD | The direction is supported, but only in specific windows (details below). |

**R8-S05, values read by eye, T-Ca2+ current density in pA/pF, mouse TRN neurons**

- **Gclm-KO, young adult (PND60-75), C57BL/6J background.**
  - Fig. 1G at -110 mV: WT about -3.75, KO about -2.65 (about 29% lower). Replicate unit neuron, WT 9 and KO 10. Overall two-way ANOVA p<0.0001.
  - Fig. 1B, current at resting potential (RMP): WT about -1.83, KO about -1.11. The legend says "p = 0.034, one-tailed t-test", so two-tailed it would be about 0.068.
  - Fig. 1B legend gives WT n=10, KO n=11. By eye I count 11 WT and 9 KO points.
- **Gclm-KO, peripubertal (PND20-30): no decrease.**
  - Fig. 2D at -110 mV: WT and KO both about -7.0. Fig. 2C legend n: WT 24, KO 19 neurons.
  - Discussion: "both T-Ca2+ and SK currents are not affected despite the presence of OxS and reduced PV expression [24]". So developmental oxidative stress without an added challenge or older age did not lower the current.
- **PND20-30 after a PND10-20 challenge.**
  - Fig. 2D at -110 mV: WT about -7.0; Gclm-KO plus GBR about -3.5; WT plus BSO and GBR about -3.7.
  - The asterisks span about -90 to -110 mV.
  - Fig. 2C at RMP: "Kruskal-Wallis, p = 0.062", not significant.
- **Prenatal MAM (G16, C57BL/6JRj), recorded young (legend PND21-30).**
  - Fig. 4H at -110 mV: control about -7.0, MAM about -2.9. The asterisks are at -70 mV and more negative.
  - Fig. 4G at RMP: not significant per the legend.
- **Fig. 3G (replotted WT and KO-GBR at RMP).** It carries an asterisk over KO-GBR that I could not tie clearly to a stated comparison.

**Further limits on S05 (not separate verdicts)**
- **Control for the MAM recordings (read by eye).** The "WT" in Fig. 4E-H appears to be the same dataset as the Gclm WT of Figs. 2 and 3. The points in Fig. 2C and 4G match (n=24 in both), and the bars and curves look identical. Methods describe offspring of NaCl-treated females as the MAM comparator. The Fig. 4 recordings therefore may not use that comparator. The paper does not say either way.
- **Statistics.** The Fig. 1G degrees of freedom (289) equal 19 cells x 17 voltages minus 34. This implies voltage points from one cell were treated as independent. Fig. 4H (578) fits 36 cells the same way.
- **Animal numbers.** The number of mice behind the recordings is not reported.
- **Oxidative stress measurement.**
  - 8-oxo-dG was measured here only in the WT, KO-GBR and KO-GBR-NAC set (Fig. 3) and the MAM set (Fig. 4).
  - For adult and peripubertal Gclm-KO it is cited from earlier work. For BSO plus GBR WT mice I found no measurement.
  - The figure legends say PND40 for the staining, while the MAM Results text says PND20-30.
- **Causal support.** NAC prevention applies to the KO-GBR model only (Fig. 3). For MAM the paper reports co-occurrence ("Concomitant presence").

**Searches behind the negatives (2026-11-28, case-insensitive, on the XML-extracted text and `41380_2021_1425_MOESM1_ESM.txt` with base64 field-code lines removed)**
- `Cntnap2`: 0 hits in both.
- `adult MAM`: 0 hits in both. I also saw no adult MAM recording on reading the text and figures.
- Animal numbers: `mice per group`, `animals per`, `number of animals`, `mice/`. All hits concern immunohistochemistry.
- The BSO-GBR 8-oxo-dG negative rests on reading the full text, legends and all four figures, not on a separate keyword search, so treat it as unverified under the matching rule.

## 2. Corrected wording for the ADD items (there is no MUST CHANGE)

- **R8-S01:** "The change in T-type Ca2+ current density in thalamic reticular nucleus (TRN) neurons (mouse, ex vivo slices) ..."
- **R8-S05:** "a decrease under developmental redox or neurodevelopmental insults in mouse TRN neurons: in Gclm-KO at PND60-75 but not at PND20-30; and already at PND20-30 after an added early-life challenge (GBR at PND10-20 in Gclm-KO, or BSO plus GBR at PND10-20 in WT) or prenatal MAM (G16), chiefly from hyperpolarized potentials, with no significant young-age decrease reported at resting potential (Fig. 2C, 4G); ex vivo, neuron-level statistics (PMID 35079122)."

Whole sentence, with the unheld leg marked: "Across two separate studies (not a matched comparison), the T-type change may differ in sign and age with the insult (an increase in Cntnap2, PMID 40834072 [not checked here; cell type, age and readout to be stated]; [R8-S05 wording])."

## 3. Counts

5 statements: MUST CHANGE 0; ADD 2 (S01, S05); NO CHANGE 0; UNSETTLED 3 (S02, S03, S04).

Under the matching rule, record 8 offers no strict candidate from this reader. It counts toward loose through the two ADDs.

## 4. Opened, not read, failures, disk

**Opened**
- The "## Matching rule" section of `PREREG_ADV295_BLOCK2_SCI_20261126.md`, and the whole blind packet.
- Under `/home/desktop/legend-development/files/`:
  - `fulltext/PMID35079122_Cabungcal2022_PMC_r2.xml`: full body, methods and legends; references as titles only.
  - `figures/PMID35079122_r2/`: all 4 main figures.
  - `supplement/PMID35079122_r2/41380_2021_1425_MOESM1_ESM.txt`: all supplementary methods; embedded EndNote data only skimmed.
  - The supplement docx, listed only: it has no embedded media, and I found no supplementary figures or tables.
  - `PMC9126813.1.pdf`: converted to text but not read line by line; figure images from pages 5-7 extracted to compare panels.

**Not opened or not read:** PMID 40834072; PMID 42422765; any registry, ledger, receipt, note or other reader's file; the cited reference 24. I did not search the repository. My auto-loaded session context (project instructions, memory index, git status) held no verdict on record 8 that I saw.

**Failures (none affected a verdict):** Python PIL is not installed, and one grep pattern exceeded ugrep's complexity limit; I redid both another way. No network use.

**Disk:** about 4.8 MB of scratch in `/home/desktop/.claude/jobs/fc428159/tmp/b2r3blind/` and `b2r3blind_scripts/`, both deleted. Free space stayed above 1.0 GB (1.7 GB at start, 3.1 GB at end). No file was written in the repository.

