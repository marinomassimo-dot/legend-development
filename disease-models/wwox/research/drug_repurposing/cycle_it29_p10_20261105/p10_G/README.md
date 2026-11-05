# IT29 P10-G: PMID 29472387 to completion, and catalytic v scaffold for class IIa HDACs in myelinating glia

Non-canonical research material, not medical advice. Public edition (WWOX-DEE reference genotype class). Written 2026-11-05 by Scientist G. Rows are in `evidence_it29_G.tsv` (G01-G22); receipt drafts in `receipts/` (event-id suffix -08), not recorded in the ledger.

## Decision (10 lines)

1. The sentence "HDAC4 and HDAC5 are required for Schwann cell myelination" is **wider than its source**. What 29472387 shows (Mpz-Cre Hdac4 deletion plus Hdac5 germline null, mouse sciatic nerve) is a **transient delay** that is gone by P8; the Hdac4/5/7 triple (35076395, same group) gives a longer delay, and adult myelin and conduction are normal in both.
2. Genotype table is complete (below). Hdac5 null alone: null. Hdac7 deletion alone: null. Hdac4 deletion alone: **subtle, transient** (fewer myelinated axons at P2, none at P8). Only multiple paralogs removed give a clear phenotype.
3. Mechanism stated by the authors is **scaffold**: nuclear HDAC4 represses c-Jun by recruiting NCoR1/SMRT-HDAC3 (a class I enzyme), independent of Mef2 (G15, G16). HDAC4's own catalytic site was **not** tested (no catalytic-dead allele). So no datum in the Schwann literature is a counter-reason for a class IIa **catalytic** inhibitor.
4. The effect is on **differentiation timing** (promyelinating to myelinating step) and on **remyelination kinetics**, not on maintenance; maintenance defects in the Schwann literature belong to HDAC3 (G20), not class IIa.
5. B38 wording: the evidence row's `adverse` is supported only for developmental timing of Schwann myelination; `loss` as an action and `context_dependent` as a direction are both defensible, but the most exact is: action = genetic loss of two (or three) paralogs, scaffold, catalytic not separated; direction = adverse, transient, with adult `null`. B38's `HDAC4+HDAC5` target label is right; B39's "compensation by HDAC4" fits the Hdac5 single null (the authors propose Hdac4/Hdac5 redundancy); once both are removed the compensator is Hdac7 (up threefold), then Hdac9 de novo when Hdac7 is also removed.
6. **No CNS oligodendroglia datum on HDAC4/5/7/9 loss was found** after bounded search (queries below). The only CNS class IIa-directed datum with a myelin stain is a rat stroke study with the compound MC1568 (G18): MBP density down, but confounded by larger lesions and deaths, compound only.
7. A weak counter-signal for CNS transfer: in neural stem cells **Ncor deletion raises oligodendrocyte genes** (G19), the opposite direction of the Schwann route where the NCoR partner is needed. In vitro, not class IIa.
8. One axon-side hint, not a result: all Hdac5-null genotypes conduct more slowly than wild type, and the authors guess a neuronal cause (G12).
9. Consequence under the pre-registered table: **nothing found in CNS, plus a narrower PNS-only wording**. The lever is not penalised; the empty "HDAC4 / HDAC5 in CNS oligodendroglia" row stays, dated.
10. Sentence for the records (22 words): **"Mouse Schwann-cell Hdac4 plus Hdac5 deletion delays peripheral myelination transiently (recovered by P8); single deletions are null or subtle; no CNS datum."**

## 1. Genotype table of PMID 29472387 and its sequel (complete)

Cre line: `P0-Cre` (Mpz-Cre, hemizygous) from the Wrabetz laboratory; onset age not stated in the text of 29472387; the 2022 paper notes Mpz-Cre is already active in Schwann cell precursors. Hdac4 is floxed (exon 6), Hdac5 is a **global** null (not Schwann-specific), Hdac7 is floxed (exons 2-10; 2022 paper).

| Genotype (Schwann-cell Cre unless said) | Myelin readout | Result | Source | Row |
|---|---|---|---|---|
| Hdac4 cKO alone | RT-qPCR P0, P2, P5; EM P2, P8 (2022) | slight: P0 Periaxin, Mpz, Hmgcr down; P2 Hmgcr down; P5 none. EM: fewer myelinated axons at P2 (912 v 1363), none at P8; g-ratio unchanged | 29472387 (transcript); 35076395 (EM) | G01, G02 |
| Hdac5 germline null alone | RT-qPCR; EM P2, P8; crush | no phenotype; myelin genes not decreased | both | G03, G04 |
| Hdac7 cKO alone | EM P2, P8; crush | no phenotype | 35076395 | G05 |
| Hdac4 cKO + Hdac5 null ("HDAC4/5 ScKO", "dKO") | RT-qPCR P0, P2, P8; EM P0, P2, P8 | P0 myelin profiles 0.18 v 1.47 per 100 um2; P2 3.99 v 8.83; **P8 no deficit**; myelin genes down at P0, P2, normal P8; c-Jun and Runx2 stay up | 29472387 | G06 |
| same, older and adult | EM, conduction (2022) | normal | 29472387 (older ages, panels unseen); 35076395 | G07 |
| Hdac4 cKO + Hdac5 null + Hdac7 cKO ("tKO") | EM P2, P8, P21; g-ratio; protein | myelinated axons 18.5% v 54.6% at P2, 31.6% v 54.6% at P8 (both control values as printed), 97.9% v 99.9% at P21; g-ratio 0.80 v 0.76 at P8 | 35076395 | G08 |
| tKO adult, uninjured | EM, conduction, RNA-seq | myelin and conduction normal; Remak bundles disorganised, melanocytic-lineage genes up | 35076395 | G09 |
| dKO and tKO after crush | EM, g-ratio, compound action potential | dKO 388 v 1,889 myelinated axons at 10 dpi; tKO none at 10 dpi and 1 of 8 nerves conducting at 40 dpi; catch-up later | 35076395 | G10, G11 |
| In culture: shRNA Hdac4; HDAC4 3SA gain; Mef2-binding mutants; NCoR/HDAC3-binding mutants | c-Jun, Krox20, Periaxin, myelin mRNAs | knockdown blocks cAMP induction of Krox20 and Periaxin; nuclear HDAC4 induces them; Mef2 mutants keep repression; D934N and H803A lose most of it | 29472387 | G13-G16 |

Myelin readout in 29472387: transcripts (RT-qPCR) and electron microscopy (myelin-profile density, myelination index). **Not measured there:** g-ratio, conduction, thickness. The 2022 paper adds g-ratio and compound action potentials.

Additional reading on 29472387 itself: onset (embryonic) of Cre, supplementary Fig. S5-S7 (genotype panels, older ages, injury) were not available; the numbers above come from the main text and legends.

## 2. Catalytic v scaffold, evidence by theme

* **Class IIa HDACs as pseudo-enzymes.** The authors state (29472387, Introduction) that class IIa HDACs lack prominent deacetylase activity because of a catalytic-site tyrosine to histidine change, and work mainly as corepressors.
* **Scaffold route shown (G15, G16).** N-terminal (Mef2-binding) route is dispensable for c-Jun repression; C-terminal NCoR1/SMRT-HDAC3 recruitment is needed (point mutants D934N, H803A; partial loss). TSA (pan-HDAC, weak on class IIa) re-expresses c-Jun (G17), read by the authors as dependence on a bona fide deacetylase, probably HDAC3, not HDAC4. The HDAC4 catalytic site itself was never mutated.
* **HDAC3 as downstream effector (G20, abstract only).** Hdac3 Schwann deletion does not delay formation of myelinating cells but destabilises the sheath later (30517863). That does not match the class IIa delay, so HDAC3 is not the sole effector (inference, not shown).
* **Compound in a myelinating context.** None in a Schwann cell or oligodendrocyte culture. The sole item is MC1568 in rat stroke (G18, 27103167): compound only, selectivity taken from the source, outcome confounded by larger infarcts and deaths in that arm; MBP is a marker. TMP269 appears in neuroprotection and inflammation papers (seen in the search, abstract level; not myelin) and was not read as myelin evidence.
* **Catalytic-dead rescue or class IIa-selective inhibitor in a myelinating cell: not found.** See queries.

## 3. What could transfer to CNS myelination, row by row

| Part of the Schwann result | Could transfer to CNS? | Why |
|---|---|---|
| Direction (loss delays differentiation) | **Open** | Only a hypothesis; no CNS oligodendroglia datum. Partner evidence points the other way in neural stem cells (G19) |
| Cell type | **No** | Schwann cell biology (cAMP/Gpr126 axis, c-Jun as brake, Krox20) differs from oligodendrocyte biology; c-Jun is not known as the brake in CNS myelination (general knowledge, not from the sources read). Even Olig1 is repressed by nuclear HDAC4 in Schwann cells (G14), where Olig1 has a different role |
| Timing | Partly | Delay with catch-up by P8 (development) and by later days (injury) is a kinetic effect; an equivalent CNS kinetic delay would still show in a P10-P21 white matter window, which is where WWOX loss acts |
| Partners (NCoR1/HDAC3, not Mef2) | **Unknown** | NCoR/SMRT and HDAC3 are expressed in CNS, but their direction differs (G19) and HDAC3 loss in oligodendrocytes is adverse in class I literature already carried in B-rows |
| Redundancy (needs 2-3 paralogs) | **Probably** | Hdac7 and de novo Hdac9 compensate; a CNS single-paralog loss or a selective inhibitor of one paralog is less likely to show a phenotype; a pan-class IIa compound acts like a multi-paralog loss |
| Scaffold function | **Not a catalytic-inhibitor datum** | An inhibitor of the catalytic pocket is a different perturbation; whether pocket binding changes NCoR1/HDAC3 recruitment is not in these sources |
| Readout | Narrow | Transcript, EM density and conduction in nerve; none in CNS tissue |

## 4. What the same mutants would need to show to be a counter-reason for a catalytic inhibitor

All of the following, none of which exists in the sources read:
1. An oligodendroglia-lineage conditional deletion (not Schwann) of the relevant paralog set, with a deficit in myelinated fraction, g-ratio or ultrastructure in white matter (not only Mbp or Plp transcript), persisting past the catch-up window.
2. A **catalytic-site point mutant** (Tyr to His reversed, or a pocket-blocking mutant) that **fails to rescue** the null phenotype while an NCoR-binding-competent catalytic-dead form **does** rescue: this separates catalytic from scaffold. If the catalytic-dead form rescues, the inhibitor is not a counter-reason.
3. A class IIa-selective inhibitor in oligodendroglia or myelinating co-culture with a target-specific control (the null phenotype reproduced, and no extra effect in the null), without loss of viability.
4. A statement of whether the inhibitor alters NCoR1/HDAC3 recruitment (the pocket binders are not shown to).

## 5. Not established

Whether any class IIa paralog matters for CNS myelination; whether the effect in 29472387 is cell-autonomous in vivo beyond the Cre line (Mpz-Cre also acts in Schwann cell precursors, 35076395); whether Hdac5 acts in the axon (G12, conjecture); what the older-age panels show; whether pocket-binding inhibitors disturb the NCoR1/HDAC3 scaffold; the selectivity of MC1568 (taken from the source).

## 6. Not reachable

* Supplementary PDF of 29472387 (Fig. S5-S8, Tables S1-S2): not retrieved. Reopen by the open copy on the publisher or PMC site.
* Figure images of every paper (legends only).
* Full text of 24657831, 30517863 (PMC ID found, abstract used for the row only), 29431744, 26859354, 40167013 and 40650056 (review, text searched for class IIa/oligodendrocyte statements only, none found): abstract-level; no receipts written for them.
* Full text of the TMP269 CNS papers seen in the search (39842624, 40581210): abstract only, not myelin.

## 7. Queries run (all 2026-11-05)

* PubMed MCP `search_articles` (class IIa AND myelin family; TMP269 OR MC1568 AND oligodendrocyte): `API_ERROR` twice; one query on HDAC3/NCoR returned 0. PubMed E-utilities esearch returned no JSON (throttled), so Europe PMC REST search was used for all searches below (`TITLE_ABS`, `SRC:MED`).
* `(HDAC4|HDAC5|HDAC7|HDAC9|"class IIa") AND (Schwann|oligodendrocyte(s)|myelination)`: 14 hits; relevant: 29472387, 35076395, 29729650, 24657831, 25103231 (proliferation only), 27103167.
* `(TMP269|MC1568|LMK235|"class IIa HDAC inhibitor"|"class IIa-selective") AND (oligodendro*|myelin*|Schwann)`: 1 hit (27103167).
* `(HDAC3|NCoR1|Ncor1) AND (oligodendro*|Schwann) AND myelin*`: 6 hits (29472387, 36218239, 35320455, 29431744, 30517863, 34656124); the HDAC3 papers are class I, listed not read.
* `(Mef2|MEF2C|Mef2d) AND (oligodendro*|Schwann|myelin*)`: 4 hits, relevant 35076395.
* `(HDAC4|HDAC5|HDAC9|HDAC7) AND (oligodendrocyte(s)|OPC|oligodendroglia)`: 6 hits, none functional.
* `HDAC3 AND oligodendrocyte(s)|oligodendroglia`: 15 hits (26859354, 25241747, 32803489 and others; class I).
* `(NCoR|NCoR1|SMRT) AND (oligodendrocyte(s)|Schwann)`: 5 hits (25241747 read).
* `(deacetylase-dead|catalytically inactive|deacetylase activity|enzymatic activity) AND HDAC3 AND (myelin|oligodendrocyte|Schwann)` and `... AND (catalytic ...)`: 0 hits.
* `(class IIa|HDAC4|HDAC5|HDAC9) AND (axon|neurons) AND (myelin|myelination)`: 4 hits (stroke papers, miRNA papers).
* `(HDAC4|Hdac4) AND (myelin|hypomyelination|"white matter")`: 9 hits (40167013 case report; none in oligodendroglia).
* `(HDAC5|HDAC9) AND (myelin|myelination|demyelination|remyelination|cuprizone)`: 8 hits, none functional in glia.
* `class IIa HDAC(s) AND (glia|astrocyte|microglia|"white matter")`: 8 hits (astrocyte HDAC7, microglia TMP269; none myelin).

**Bounded negative:** no class IIa HDAC loss or inhibition study with a CNS oligodendrocyte differentiation or myelination readout was found after these queries in PubMed-indexed titles and abstracts (via Europe PMC). Full-text-only mentions would be missed. What would reopen it: an Olig2/Cnp/Pdgfra-driven Hdac4/5/7/9 conditional line; a class IIa-selective compound in OPC differentiation with a target-specific control; or a bioRxiv preprint (not searched; Europe PMC preprint records were excluded by `SRC:MED`).

## Sources read (depth)

29472387 `partial_fulltext` (Introduction, Results, Discussion, Methods, figure legends; supplement unavailable); 35076395 `partial_fulltext` (Results, figure legends, Discussion first half; Methods not read); 27103167 `full_text` text of accepted manuscript, figures not viewed (receipt partial); 29729650 `full_text` commentary; 25241747 `partial_fulltext` (Results sections on NCOR/HDAC2/HDAC3); abstract only: 30517863, 24657831, 40167013.
