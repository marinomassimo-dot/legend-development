# ADV-171 pre-registration: do the 28 unread sheets of the Ma et al. 2025 S1 Data hold a pre-onset lipid, proteome, synapse or energy sign that pre-dates the ADV-165 chronology, for RP-036 and RP-039? (SCI successor Z, 2026-11-22; hypothesis level; adjacent mouse model, Cyfip2 R87C; not a WWOX result; no compound, dose or rank change; no new source; no contact; no e-mail address to any service; not medical advice)

Workbook: S1 Data of Ma et al. 2025 (the "S38" file; 34 sheets), SHA-256 `906de7531b54d47770f4e36319ad1f49b2b3ca24bef6e8bb063933924e1d9c6d`, verified with `python3 -I` before use (identical to the ADV-165 copy and to ADV's stated value).

## What had been seen before this file was written (so the rules are not mistaken for blind)
* ADV-165: the full article text (publisher XML), and six sheets in full (Fig1A, Fig1B, Fig1C, Fig4C, Fig5D, FigS8). Fig 4C and FigS8 are the NeuN / Olig2 per-animal markers; the early set at PWK 7 (NeuN, Olig2, IBA1) and the PWK 1 shift are already in the ADV-165 result.
* This task, before this file: the 34 sheet NAMES, and for each sheet its number of rows, its largest row width, its count of numeric cells and its text label cells (genotype and age labels, panel titles). No numeric cell of any of the 28 unread sheets was read. From the labels alone: the proteome and lipidome sheets carry age labels PWK 14 and PWK 28 only (Fig8A, 8C, 8G, 8I); the Fig 3A and 3B sheets carry PWK 1, 7, 14 and 28 with Cortex and Hippocampus labels and Animal 1..n columns. Ages of Fig6D, Fig6F and FigS13 (lipid droplet and crystal spot counts) are not yet read from the labels.
* The legends of Fig 3, Fig 6 and Fig 8 in the article text (Fig 3A: qRT-PCR heat maps of DEGs encoding synaptic proteins, n = 6 per genotype; Fig 3B: western blots of synaptic markers in synaptosomes, n = 6 to 8; Fig 8: proteome and lipidome at PWK 14 and 28 only).
* RP-036 and RP-039 rows are read by ADV; I re-grep them in the repository before the result.

## Question
(i) Does any lipid, proteome or energy-related sheet carry a wild-type-compared, per-animal or per-sample value at PWK 7? (ii) If not, does the synapse part (Fig 3A transcripts, Fig 3B synaptosome proteins), which does carry PWK 7, show a per-animal sign at PWK 7 that pre-dates or equals the ADV-165 chronology, and is it of the metabolic family (lipid, lactate, glucose, FDG) that RP-036 and RP-039 hold open?

## Readings (fixed)
* **L-late (predicted):** lipid and proteome values exist only at PWK 14 and PWK 28 (Fig 8), and lipid droplet or crystal counts only at later ages. Then rejecting observation 2 of the assignment applies for RP-036 and RP-039, and the lipid, proteome and energy sheets are closed as "later than the chronology".
* **S-early:** in Fig 3A or 3B at PWK 7, at least three genes or proteins move in one direction, with every R87C animal beyond every WT animal for at least one of them, and a Welch interval (95 percent, per-animal values) that excludes no change for at least two; size reported as a fraction of the age-matched WT mean.
* **S-null:** none of that at PWK 7.
* **S-unread:** the sheet does not give a per-animal row at PWK 7 (a heat-map summary, a mean without animals, or a mixed layout).
In either S-reading the family is recorded as synaptic transcripts and proteins: not lipid, lactate, glucose or FDG, and not the named resume condition of RP-036 or RP-039. A synaptic early sign would be noted as an adjacent early-sign series for the chronology only; it changes no RP row unless it is itself of the held family.

## Decision rules (fixed)
1. **Close as "nothing new for RP-036 / RP-039":** L-late holds AND (S-null, S-unread, or S-early of the synaptic family only). Record the inventory and the PWK 7 synaptic finding in one short result; the dataset stays closed for the metabolic family.
2. **Carry a documented adjacent comparator** (one dated line for ADV to place) only if a lipid, proteome or energy value at PWK 7 with a WT comparator and per-animal rows exists (it would overturn L-late), or if the synaptic sheet carries a metabolic-pathway gene or protein (lactate transporter, glucose transporter, lipid-synthesis enzyme) among the PWK 7 changes.
3. A seizure-to-marker per-animal link remains missing unless the sheets state animal identity across markers: I check whether `Animal n` labels in different sheets can be assumed the same mouse, and I will not assume it.

## Replicate-unit checks I will make (fixed)
Whether Fig 3A and 3B rows are per animal (n = 6 and 6 to 8 per legend) and normalised to the WT mean per age; whether more than one tissue region or gene panel inflates the number of tests (multiplicity, ten or more genes per panel expected); the direction of the PWK 7 shift against the PWK 1, 14 and 28 shifts.

## Limits stated now
Adjacent mouse model, not WWOX; a heterozygous missense knock-in; qRT-PCR and western values are per-animal summaries, no per-cell data; no new source; the proteome tables (S6 Table) and lipid species lists are separate supporting files that are not part of the workbook and are not opened.

## Rejecting observation (named in advance)
A lipid, proteome or energy sheet row with WT and R87C animals at PWK 7 would overturn L-late; a Fig 3A or 3B PWK 7 sign with per-animal separation and a metabolic gene would trigger rule 2. Any one of the assignment's four rejecting observations closes the item with "nothing new".

## Consumer
ADV (result and path). IT only for a verified delta, none expected.
