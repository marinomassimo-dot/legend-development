# IT29 P10-F: class IIa HDACs inside the central oligodendrocyte lineage

Non-canonical working record, not medical advice. Public edition, WWOX-DEE reference genotype class. Scientist F, 2026-11-05. Evidence: `evidence_it29_F.tsv` (9 rows); receipts: `receipts/` (7 drafts, suffix -08).

## Decision (10 lines)

1. Not found after bounded search: no genetic loss, conditional deletion, overexpression, nuclear-export mutant, catalytic-dead allele or selective inhibitor of HDAC4, 5, 7 or 9 was done in OPCs, oligodendrocytes, CNS myelinating culture, slices, or an oligodendroglia-specific CNS in vivo model, with a differentiation or myelin readout. Queries below.
2. The only central OL-lineage class IIa data are expression and localisation after stroke (F06, F07): HDAC4 and HDAC5 are mainly cytoplasmic; HDAC4 nuclear shuttling occurs in neurons, not in APC+ oligodendrocytes. Association only.
3. The only CNS compound datum on a myelin readout is MC1568 after stroke (F08): MBP, axon and dendrite densities fall, with larger lesion and higher mortality. Compound-only, no target control, viability confounded; the authors themselves read the myelin loss as likely secondary to neuronal death. It is a weak adverse lead, not a measurement of OL differentiation.
4. The only CNS class IIa genetic datum is Nes-Cre / Thy1-Cre Hdac4 deletion (F09): no gross cytoarchitecture or cell-death change; myelin never examined. Silent on the endpoint.
5. The peripheral source behind the carried sentence is weaker than the sentence. Hdac4 plus Hdac5 removed together from Schwann cells gives a transient delay (myelin-sheath density lower at P0 and P2, equal at P8, adult normal) (F01). Either alone: little or nothing (F02).
6. Even the triple Hdac4/5/7 Schwann-cell deletion ends with almost normal adult myelin; Hdac9, normally absent, is induced via MEF2D (F04, F05). So class IIa loss delays, it does not prevent, PNS myelination.
7. Function: the Schwann-cell mechanism is scaffold. HDAC4 acts through NCoR1/HDAC3, not through Mef2 binding, and TSA (which spares class IIa) reverses it (F03). A class IIa catalytic inhibitor is therefore a different perturbation from the loss tested; no CNS data separate the two.
8. Consequence under the pre-registered table: "Nothing found" for the CNS row; the PNS text must be worded as a transient delay in a double (or triple) mutant, not "required".
9. Direction counts: favourable 1 (F03, culture gain-of-function, PNS), adverse 1 (F08, compound, confounded), null 1, context_dependent 2, undetermined 4.
10. What would reopen it: an Olig2/Sox10/Cnp/Pdgfra-Cre (or inducible) deletion of Hdac4+5 (with Hdac7/9) with CC1/MBP/g-ratio readout, or a class IIa compound with an Hdac4/5/7/9 knockout control in OPC differentiation culture.

## Evidence by theme

**A. Peripheral anchor, re-read to the cut that matters (PMID 29472387; Elife 35076395).** All rows carry `PNS`. F01: P0-Cre Hdac4 flox crossed to global Hdac5 null; myelin-sheath density per area control vs mutant 1.47 vs 0.18 (P0), 8.83 vs 3.99 (P2), not different at P8, parameters normal in older animals; c-Jun stays raised. F02: Hdac5 null alone has no obvious myelination phenotype; Hdac4 cKO alone raises c-Jun but does not lower myelin genes by P5. F04: the Elife paper reports a subtle delay for Hdac4 cKO alone, a much longer delay for Hdac4/5/7 loss, impaired conduction during regeneration, Remak bundle defects, yet adult tKO nerves almost normal. F05: Hdac9 induced 4.4-fold in adult tKO. Reading depth is partial in both; the decisive statements are in the sections read. The earlier receipt left Methods/Discussion unread; this round read the in-vivo Results, Discussion and the animal Methods paragraph (see receipt).

**B. Function of the class IIa HDAC in myelinating cells: scaffold.** F03 and the commentary (PMID 29729650): class IIa HDACs lack prominent deacetylase activity; HDAC4 recruits NCoR1/SMRT-HDAC3; Mef2-binding mutants still repress c-Jun; NCoR-binding mutants do not. Culture, Schwann cells, gain-of-function only. Whether any of this holds in oligodendroglia is not tested by anyone I could find.

**C. CNS oligodendrocyte lineage: expression only.** F06 (PMID 24657831): in peri-infarct rat corpus callosum HDAC4+ NG2+ OPCs increase after stroke, HDAC5+ OPCs do not; HDAC4+ or HDAC5+ among APC+ oligodendrocytes unchanged; both mainly cytoplasmic (epifluorescence only; authors call for confocal). The paper argues class I are likelier mediators than class II. F07 (PMID 25967576): nuclear HDAC4 appears in neurons only; across animals it correlates with MAP2, pNFH and MBP densities (r about 0.7), which is a neuronal-side association, not a test.

**D. CNS compound and genetic datum.** F08 (PMID 27103167), see decision 3. F09 (PMID 23239283), see decision 4. Neither isolates oligodendroglia.

## What is not established

* Any effect (any sign) of class IIa loss or inhibition on OPC differentiation, CC1 counts, Mbp/Plp, g-ratio or conduction in CNS.
* Which cell carries a class IIa effect on CNS myelin: oligodendroglia or axon-bearing neuron. The only hint (nuclear HDAC4 is neuronal) is correlational.
* Catalytic versus scaffold in any CNS cell. The scaffold reading comes from Schwann-cell culture.
* Hdac7/Hdac9 expression along the OL lineage: not read (no transcriptomic atlas was fetched; a bounded search for atlas papers was not run, since atlases count only as transcript context).
* A target-controlled class IIa compound result in glia: MC1568 and TMP269 appear in glial papers only for inflammation or neuronal protection (nearest material below).

## Verdict on the carried sentence

"HDAC4 and HDAC5 are required for myelination" is **narrowed to the point of contradiction**: the source supports "joint loss of Hdac4 and Hdac5 transiently delays myelin development in Schwann cells (PNS)", reversed by P8, with Hdac7/Hdac9 compensation; it says nothing on CNS. The CNS wording should be "not reached in CNS after bounded search", with F08 noted as a confounded compound-only adverse lead.

## What was not reachable

* PubMed MCP `search_articles` returned API errors throughout; NCBI esearch and Europe PMC search were down for about 10 minutes; Europe PMC came back and was used for every query. NCBI efetch (PMC) worked for full texts.
* Figures, tables and supplement of every source were not read (bytes were not saved; supplement unavailable).
* PMID 12451133 (Marin-Husstege 2002, pan-HDAC activity needed for OL progression) and Shen 2005 were met as abstracts or secondary citations only; they are class-unspecific and outside the brief's reading scope.

## Nearest related material, not the endpoint (abstracts only, not read in full)

TMP269 neuroprotection after ischemia (31552900), TMP269 in Parkinson models (39842624), class IIa inhibition and macrophage polarisation after stroke (40581210; HDAC9 the most upregulated), MC1568 inflammatory modulation in glial culture (40211035), HDAC7 in Tregs and EAE (36516268), NCoR1/SMRT expression map in mouse brain (32072640). None addresses oligodendrocyte differentiation.

## Queries run (Europe PMC REST `search`, 2026-11-05 09:50 to 09:58 UTC; PubMed MCP failed)

1. `HDAC4|HDAC5|HDAC7|HDAC9 AND (oligodendrocyte OR oligodendroglia OR "oligodendrocyte precursor")` full-text mode (445, 276, 170, 220 hits; reviews and atlases, screened by title).
2. `TITLE_ABS:(HDAC4 OR HDAC5 OR HDAC7 OR HDAC9 OR the "histone deacetylase 4/5/7/9" strings OR "class IIa") AND TITLE_ABS:(oligodendrocyte(s) OR oligodendroglia(l) OR "oligodendrocyte precursor" OR OPC(s) OR "white matter" OR myelination OR remyelination OR dysmyelination)`: 17 hits.
3. `TITLE_ABS:(TMP269 OR MC1568 OR LMK-235 OR LMK235 OR "class IIa HDAC*" OR "class IIa histone") AND TITLE_ABS:(oligodendro* OR myelin* OR OPC)`: 4 hits.
4. `TITLE_ABS:(Hdac4 OR Hdac5 OR Hdac7 OR Hdac9) AND TITLE_ABS:(oligodendro* OR myelin* OR "white matter" OR OPC*)`: 22 hits.
5. `TITLE_ABS:(MEF2 OR MEF2C OR MEF2D) AND TITLE_ABS:(oligodendro* OR myelin* OR OPC*)`: 20 hits, none class IIa in oligodendroglia.
6. `TITLE_ABS:(NCoR OR SMRT OR NCOR1 OR NCOR2) AND TITLE_ABS:(oligodendro* OR "CNS myelin*")`: 6 hits.
7. `TITLE_ABS:("histone deacetylase") AND TITLE_ABS:(oligodendrocyte differentiation) AND TITLE_ABS:(class II ... HDAC4/5/7/9/6)`: 3 hits.
8. `TITLE_ABS:(TMP269 OR MC1568 OR "LMK-235" OR "MC-1568") AND TITLE_ABS:(glia* OR astrocyt* OR microglia* OR neuron* OR brain OR CNS OR nervous)`: 38 hits.
9. HDAC4/5/7/9 crossed with demyelination, cuprizone, multiple sclerosis, EAE, hypomyelination, leukodystrophy, corpus callosum (7 hits); HDAC4 + glia + knockout/Cre (1); Hdac4 conditional + brain (7); HDAC9 knockout + brain/glia/myelin/stroke (2).
10. `EXT_ID:<PMID> AND SRC:MED` metadata calls; full texts through Europe PMC fullTextXML and NCBI efetch db=pmc. PubMed MCP `get_article_metadata` for 29472387 (abstract only). No e-mail address was sent to any service.
