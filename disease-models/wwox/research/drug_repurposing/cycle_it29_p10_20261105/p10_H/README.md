# IT29 P10 Scientist H: neuronal or axonal route, and the adversarial search (challenge CH-IT29-CLASSIIA-CNS-MYELIN)

Non-canonical working record. Not medical advice. Public edition, WWOX-DEE reference genotype class. Written 2026-11-05. Evidence: `evidence_it29_H.tsv` (11 rows, event-id suffix -08). Receipts: `receipts/` (6 sources read; the 3 abstract-only sources have no receipt).

## Decision (10 lines)

1. Neuron/axon route (point 1): **bounded negative.** No report was found in which a class IIa HDAC (Hdac4, 5, 7, 9) was deleted, inhibited or overexpressed in neurons and a myelination, OPC or axon-to-glia-signalling readout was taken in a developmental or non-injury setting.
2. The nearest neuronal datum is a mouse study with Hdac4 deleted by Nestin-Cre or Thy1-Cre (PMID 23239283): normal cytoarchitecture, but **no myelin or oligodendrocyte stain** was taken. It is not a null for myelin (row H05).
3. The only CNS datum that touches myelin with a class IIa tool is rat stroke (PMID 27103167): MC1568 lowered MBP, MAP2 and pNFH density together with higher mortality and lesion volume. The authors read the myelin loss as secondary to neuronal death. Compound-only, marker, injury, no target control (H01). Weak adverse, not attributable to HDAC4/5.
4. Stroke localisation work places the HDAC4 nuclear response in neurons, not oligodendrocytes (PMID 25967576, H02, H03); in OPCs HDAC4 is present and cytoplasmic, and the authors state that class II roles in oligodendrocyte development "are still not known" (PMID 24657831, H04).
5. Adversarial search (point 2): **no class IIa-specific favourable report was found; no report that class IIa loss is neutral for CNS myelin with a myelin readout.** One favourable row exists for a class I/II inhibitor (Scriptaid, TBI, white matter protected via microglia; abstract only; H10): not attributable to class IIa.
6. The strongest contradiction of "required" is within the PNS source family: Hdac4/5/7 triple Schwann cell deletion delays but does not abolish myelination, adult nerves nearly normal; the Hdac4/5 double mutant is normal after P8 (PMID 35076395, H06, H07). Compensation (Hdac7, then Hdac9 via Mef2d) is the mechanism proposed there.
7. A human Treg-specific Hdac7 result (EAE worse after deletion, PMID 36516268) and a single HDAC4 frameshift case with reduced white matter (PMID 40167013) are context rows, abstract only (H09, H11).
8. Catalytic v scaffold: in Schwann cells the repression of c-Jun by HDAC4 needs NCoR1/SMRT-HDAC3 and deacetylase activity (secondary account, H08). No catalytic-dead class IIa myelin experiment was found for the CNS.
9. Sentence "HDAC4 and HDAC5 are required for myelination" as carried: **not supported for the CNS; narrowed to delay-not-absence in the PNS with two or three paralogs deleted.** It contradicts neither a CNS role nor a neutral one: there are no CNS data.
10. Consequence under the pre-registered table: row "Nothing found" for the neuron/axon route, with a weak adverse compound-only injury datum and a wording narrowing for the PNS.

## Evidence by theme

| Theme | Rows | Reading |
|---|---|---|
| Neuron-side class IIa manipulation with a myelin readout | none | not found |
| Neuronal Hdac4 deletion, any readout | H05 | normal cytoarchitecture, myelin not looked at |
| Class IIa tool in CNS injury, myelin marker | H01, H02, H03 | MC1568: MBP down with neuron loss; nuclear HDAC4 localises to neurons |
| Class IIa in the OPC and oligodendrocyte lineage (expression) | H04 | present; function unknown |
| PNS compensation, against "required" | H06, H07, H08 | delay, not absence; scaffold plus HDAC3 |
| Favourable or neutral searched adversarially | H10 (class I/II), H09, H11 | no class IIa-specific favourable report |

## What is not established
* Whether class IIa loss in neurons alters CNS myelination (no experiment found).
* Whether class IIa HDACs act in OPC/oligodendrocytes (no genetic or catalytic-dead data found; expression only).
* Whether MC1568 acts on class IIa in vivo here (no target-specific control in the source; selectivity not checked by me).
* Whether CNS oligodendroglia have the Hdac7 and Hdac9 compensation seen in Schwann cells (not tested).

## What was not reachable
* Europe PMC returned HTTP 503 intermittently and NCBI esearch returned 500; the PubMed MCP search returned zero hits for Boolean queries and API errors for short ones. Queries were redone through Europe PMC (title/abstract fields) and no failure changed a result, but the PubMed-native count is unverified.
* Full text of 25691750 (Scriptaid) came back only partly; abstract-only. 36516268 and 40167013 are not open access; abstract-only.
* Methods, figures and tables of all six read sources were not read. Methods of the PNS paper (35076395) would give the Cre timing.
* bioRxiv/medRxiv were not searched separately (Europe PMC indexes preprints, no hit found).

## What would reopen it
A neuron-specific or Olig2/Sox10-Cre class IIa deletion with Luxol, Mbp or EM g-ratio; a catalytic-dead class IIa knock-in; an organotypic slice or OPC-neuron co-culture with a class IIa-selective tool and a target control.

## Queries run (database, string, date 2026-11-05)
All Europe PMC REST (search, resultType=lite) unless stated; fields TITLE_ABS.
1. PubMed MCP: `(Hdac4 OR Hdac5 OR Hdac7 OR Hdac9 OR "class IIa histone deacetylase") AND (myelination OR oligodendrocyte OR remyelination OR hypomyelination) AND (neuron OR axon)` -> 0; second Boolean -> 0; `HDAC4 oligodendrocyte`, `HDAC9 myelin`, `HDAC5 myelination` -> API_ERROR.
2. `(HDAC4|HDAC5|HDAC7|HDAC9|class IIa) AND (oligodendrocyte*|myelin*|OPC) AND (neuron*|axon*)` -> 9 hits.
3. `(HDAC4 OR HDAC5 OR HDAC7 OR HDAC9 OR Hdac4 OR Hdac5 OR Hdac9) AND (oligodendrocyte* OR myelin* OR remyelination OR hypomyelination)` -> 17.
4. `("class IIa" OR TMP269 OR MC1568 OR LMK235 OR "HDAC4/5") AND (oligodendro* OR myelin* OR remyelination OR "white matter")` -> 5 (twice, with and without white matter).
5. `(MEF2 OR MEF2C) AND (oligodendrocyte* OR myelination OR remyelination OR "white matter")` -> 19, none class IIa-relevant to myelin except 29472387; `MEF2 AND neuron* AND (myelin*|oligodendrocyte*|white matter)` -> 0.
6. `(HDAC4 OR HDAC9 OR HDAC5 OR HDAC7) AND ("white matter" OR demyelinat* OR leukodystrophy OR "multiple sclerosis" OR EAE OR cuprizone)` -> 9.
7. Hdac9 + glia/myelin -> 8; Hdac5/Hdac7 + oligodendro/OPC/glioma/white matter -> 23 (glioma biology only, none on differentiation); Hdac4 conditional + brain structure fields -> 8 (one relevant: 23239283); Hdac5 and Hdac9 knockout + brain -> 5 each, none myelin.
8. `(HDAC OR HDAC inhibitor) AND remyelination AND (improve* OR promote* OR enhance*)` -> 2 (34656124 PNS phenylbutyrate and 25691750).
9. HDAC4 haploinsufficiency (2q37) + MRI/white matter -> 1 (23431751, a 2q terminal deletion, abstract only, not used).
10. HDAC3 AND (oligodendrocyte*|myelin*) AND (NCoR|SMRT|class IIa|HDAC4) -> 2 (25241747: class I NCoR/HDAC2/3 in neural stem cells, not class IIa; not used).
11. `FULL_TEXT: TMP269 AND (oligodendrocyte OR myelin)` -> 0.
12. Class IIa neuronal Hdac4 gain-of-function + brain: query failed twice (HTTP 503) and was not rerun successfully; stated as incomplete.

## Sources
Read (partial_fulltext): 27103167, 25967576, 24657831, 23239283, 35076395. Read (full text, short commentary): 29729650. Abstract only: 36516268, 25691750, 40167013.
