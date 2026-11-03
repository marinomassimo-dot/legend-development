# IT22 P7: targeted scouting, one named gap (2026-11-03)

Non-canonical. Not medical advice. Zero spend, no registration, no contact address sent anywhere.

**Gap named.** Comparing alternatives inside a drug class (IT22 integration, point 3) needs measured CNS exposure per compound. The local catalogue and Guide to
Pharmacology hold potency by target and measure type, not brain exposure; `class_alternatives_it22.py` therefore states "no exposure, no brain penetration, no safety" for every row.

**Searched.** GitHub (`theochem/B3DB`, repository metadata via the key-less API), Hugging Face (`maomlab/B3DB`, `zpn/bbbp`, `SaeedLab/BBB`, TDC BBB sets), published curated sets
(rat Kp,uu,BBB 98 compounds; Kp,uu,brain 88 compounds on figshare), Nature portfolio not searched beyond the Scientific Data route (no hit). WWOX was not used as a keyword.

**Tested, smallest probe.** `B3DB_classification.tsv` (CC0-1.0 by the repository's licence record; 7,807 compounds, 4,956 BBB+ / 2,851 BBB-; sha256 `47a160aea1551423ead2aab70b301fb1646aea03cf151fd614eb37c78fa55b82`,
2,635,683 bytes, pushed 2025-09-10) was downloaded to scratch and matched by normalised name to the 791 compound base-names of the IT21 proposals.

| Question | Result |
|---|---|
| gap resolved? | partly: 73 of 791 base-names (9 percent) and 2 of the 14 compounds handed to qualification (sorafenib BBB+, tretinoin BBB+) have a label; the compounds the IT22 hypotheses turn on (tiratricol, sobetirome, tazemetostat, vorinostat, pracinostat, resmetirom) have none |
| what a label is | a binary BBB+/BBB- call pooled from many sources, at a threshold; not Kp,uu, not free exposure, not paediatric; transporter-mediated entry is invisible (levothyroxine and liothyronine are labelled BBB- although thyroid hormone enters the brain through MCT8/OATP1C1) |
| advantage over what exists | none for the decisive compounds; Kp,uu data are scarce (98 and 88 compounds in the published sets) |
| cost / maintenance | 2.6 MB, one file; trivial, but a join on names would add false matches for salts and codes |
| licence | repository record CC0-1.0; the Hugging Face copy states cc0-1.0; per-source reference column inside the file would still need attribution if shown |

**Decision: WATCH, not adopted.** Nothing installed, nothing committed from the third-party file (digest above only). Reopen when a compound whose exposure decides a hypothesis is in the file, or when a Kp,uu table covering the CNS-relevant classes appears. Removal path: none needed.
The exposure question for tiratricol, the HDAC and EZH2 alternatives remains a primary-source reading, handled in the hypothesis dossiers, not a database join.
