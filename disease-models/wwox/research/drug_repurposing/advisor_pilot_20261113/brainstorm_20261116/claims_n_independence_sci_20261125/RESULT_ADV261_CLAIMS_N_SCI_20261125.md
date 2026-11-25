# ADV-261 result: independence of the n behind fifteen working-model claims (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; nothing here is medical advice. No spend, no contact, no e-mail address in any request, no claim file edited. Pre-registration: `PREREG_CLAIMS_N_SCI_20261125.md` with amendments 1 (order and listing routes), 2 (headline rows added after reading) and 3 (class FAM; "not checked"). Listing script: `list_claim_n_adv261.py`. Tables: `claim_units_increment1.tsv` (18 rows: CLAIM 002, 005, 007, 014) and `claim_units_increment2.tsv` (22 rows: the other eleven).

## 1. Answer

* **14 of 33 comparison n-statements are not independent (0.42); 11 of 28 (0.39) without the five headline rows added after reading.** ADV-247 found 0.37 for inferences over deposits.
* **The non-independence sits in four claims, not across the board.** CLAIM 002 (7 of 7 rows), CLAIM 021 (3 of 3), CLAIM 033 (2 of 2) and CLAIM 003 (1 of 2). The mouse, rat and fly counts in CLAIM 005, 007, 011, 025, 032 and 047 are animals and hold.
* **CLAIM 002's hyperexcitability rests on slices or neurons, and the claim does not say so.** 2021 field potential: 14 against 14 slices from 5 and 8 organoids, 3 batches. 2021 cell-attached: 24, 41 and 40 neurons from 4, 3 and 3 organoids of one patient family. 2026 week 7: 14 to 30 neurons per line "collected from one experiment" (Figure 1D legend). The claim's "four lines lie within about 10 percent at week 7" is four means of neurons from one experiment.
* **"Two families" in CLAIM 002 matches neither rescue as read here.** The 2021 patient-line rescue is one family; the 2026 AAV9 arm uses four lines from three families (WPM S and D are siblings of the SCAR12 family; WSM S; LM-iPS7). The WOREE AAV9-WWOX arm is 7 organoids in Figure 6 and 8 in Supplementary Figure 10.
* **CLAIM 033's 75 cases are individuals, not families:** 13 new patients from 12 families (two brothers) plus 62 from 45 families, about 57 families. Genotype-class counts are individuals.
* **CLAIM 021 gives slices; the paper prints the animals:** bursts 0 of 11 slices (7 mice), 4 of 23 (14), 36 of 42 (24); sEPSC cells nested in 5 to 10 animals per arm.
* **Not checked (five rows):** PMIDs 17803050, 34214506 and 40875931 are not held; the Chong 2023 report is UNREACHABLE (ADV-259); one supplementary panel (S8) was not opened.

## 2. Per-claim summary

| Claim | Rows | Not independent | Main finding |
|---|---|---|---|
| 002 | 8 | 7 | organoids, slices, neurons from one experiment; clones of one line; "two families" |
| 005 | 5 (+1 NS) | 1 | mouse and rat n hold; the human organoid null is one clone against one line (ADV-247); rat densities: animals not stated |
| 007 | 4 | 0 | mice (2, 6, 5 per group); the four RNA-seq regions are the same animals |
| 014 | 1 | 0 | CAGE n of one, already said |
| 011 | 2 (+1 NS) | 0 | pups; the survival legend prints no n per arm |
| 031 | 1 | 0 | two unrelated children from two families |
| 033 | 2 | 2 | family clusters |
| 003 | 2 | 1 | co-culture n=4 are cultures from two experiments |
| 021 | 3 | 3 | slices, cells, bursts nested in animals |
| 032 | 2 | 0 | n=5 mice; the n=20 has no stated unit |
| 025 | 2 | 0 | patients; fly brains |
| 047 | 1 | 0 | animals, different animals per time point |
| 038, 034, 042 | 0 comparable | - | not held or unreachable |

## 3. Expectations scored

* **C1 (10 to 35 percent non-independent): not met, higher: 0.42 (0.39 without the headline rows).** The prediction was low.
* **C2 (at least two claims with a non-independent headline n not already said): met, three:** CLAIM 002 (week-7 neurons from one experiment), CLAIM 021 (slices where animals are printed), CLAIM 033 (family clusters).
* **C3 (most people and family counts independent): not met.** Two of four person rows are independent (031, 025); the two others are one cohort (033) counted as individuals.

## 4. Wording proposed to IT (not applied; one line per place)

1. **CLAIM 002, hyperexcitability:** "Counts are slices or neurons, not organoids or lines: 2021 field potential 14 v 14 slices from 5 and 8 organoids in 3 batches; 2021 cell-attached 24, 41 and 40 neurons from 4, 3 and 3 organoids of one family; 2026 week 7 cell-attached 14 to 30 neurons per line from one experiment (Fig. 1D). Knockout organoids come from at most two clones of one hESC line."
2. **CLAIM 002, 'two families':** replace by the families of each rescue: "2021: one patient family plus a knockout hESC line; 2026 AAV9: three families (four lines; WPM S and D are siblings). The WOREE AAV9-WWOX arm is 7 organoids in Fig. 6 and 8 in Suppl. Fig. 10."
3. **CLAIM 021:** write the animals beside the slices: "0 of 11 slices (7 mice), 4 of 23 (14), 36 of 42 (24); sEPSC 5 v 8 and 10 v 10 animals."
4. **CLAIM 033 and its Genotype line:** "75 individuals from about 57 families (13 from 12 families, two brothers; 62 from 45 families)."
5. **CLAIM 003:** "co-culture n=4 are cultures from two experiments; the biological unit is not stated."
6. **CLAIM 011:** "the survival legend (Fig. 3B) prints no n per arm; the n=3 and n=7 are supplementary panel S8."
7. **CLAIM 032:** "the n=20 in the Fig. 5 legend has no stated unit; mice are 5 per group."
8. **CLAIM 005:** "rat GFAP and Iba1 densities: mean of three independent experiments, at least three affected and three normal males in each; animals per point not stated."

## 5. Limits

* Only the held texts were read: accepted-manuscript text for PMID 42397075, PMC or Europe PMC XML for the others. Figures were not measured.
* The listing script finds n in the claim records only; the headline rows (002-H1 to H3, 011-H1, 038-H1) were found by reading the papers and are a post-hoc extension, so both shares are given.
* 005-07's sentence names no PMID; the paper was matched by content and the printed density values were not re-read from the figure.
* A claim's effect on strength is a proposal; no claim was edited.

## 8. Update 2026-11-25 (after IT's check, SCI)

* Wording line 2: the WOREE AAV9-WWOX arm is n = 7 for validation and layer markers and **n = 6 for the Ca2+ imaging** in the Figure 6 legend; "7 organoids" was incomplete.
* The family structure of that arm (WPM S and D as siblings of the SCAR12 family; LM-iPS7 as a third family) is read from the 2021 paper's family naming and the 2026 supplementary legend, not from a sentence of the 2026 manuscript; it is a reading, not a quoted statement.
