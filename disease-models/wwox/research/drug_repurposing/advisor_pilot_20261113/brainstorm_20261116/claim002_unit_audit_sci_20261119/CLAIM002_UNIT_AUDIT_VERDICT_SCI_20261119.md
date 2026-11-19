# CLAIM 002 unit: blind wording audit with IT's six PROVENANCE-01 triples (SCI, 2026-11-19, ADV-083; hypothesis level; not medical advice; nothing applied)

## 0. Answer first

CLAIM 002 is **not clean**. Of 25 triples, a fresh blind delegate returned **11 SUPPORTED, 11 OVERSHOOT, 1 UNDERSHOOT, 2 UNVERIFIABLE_SURFACE**. I checked every source passage the delegate quoted against the held texts (22 of 22 found verbatim, term counts agree) and read Figure 4 (Steinberg 2021, PDF page 8), Figure 6 and Figure 2F (Steinberg 2026) myself: the figure readings agree with the delegate's, and where they bear on IT's triples they differ from IT's attestation (section 4). No attribution error of a paper, and no wrong number in the data layer (Table S1 values, the sIPSC means, P values and the firing P value are exact). The exposure is again in the **interpretive layer**, and in one place an **attribution of a measurement to the wrong paper** ("altered Ca2+ dynamics": the 2021 anchor has none, the 2026 paper does).

Four findings matter most for the 27 consumers: (1) the Summary's "altered Ca²⁺ dynamics" is not a result of the 2021 anchor; (2) "prova ... può correggere più domini cellulari" is stronger than the authors' "proof of concept"; (3) the Clinical meaning "Strongly supports ... la terapia genica" is stronger than the authors' "partial rescue ... further study is required before clinical translation"; (4) IT's triple 5 carries bar values that do not match the figure, and its second half overshoots; triple 4 cannot be audited (the supplement is not held). The Source repoint of CLAIM 002 to PAPER 094 can proceed on triples 1, 2, 3 and 6 (SUPPORTED); not on 4 and 5 as written (section 4).

## 1. Method (as dispatched; the brief and the triples are in this folder)

- Triples: 25, built from CLAIM 002's own sentences (Italian kept, glosses in brackets) plus IT's six PROVENANCE-01 triples as IT wrote them (candidate `commit_candidates/CC-20260826-PROVENANCE-01.md`, section "LOCATOR TRIPLES FOR BLIND AUDIT", unchanged on main when I dispatched); 49 text quotes checked verbatim by script before dispatch (`build_triples_claim002_sci_20261119.py`, 0 not found). Figure, absence and supplement triples carried no quote and named the figure file or the search to run.
- Delegate: `legend-delegate`, asked sonnet / effort high; read back with `session_model_census.py`: **sonnet 66 of 66 turns, effort high 66 of 66, peak context 243,345, output 73,917, cache read 10.0 million, 66 turns**. Report as delivered (1,859 words by script, cap 2,200 held): `AUDIT_REPORT_AS_DELIVERED.md` (extracted from the SubagentHandback message by `extract_handback_sci_20261119.py`).
- My checks (post hoc, after the report): `check_findings_sci_20261119.py` (22 quoted source passages found, counts agree: S21 'calcium' 2, 'Ca2+' 1; S26 'Ca2+' 2; 'depolariz' 4); registry sentences of section 6 confirmed present in CLAIM 002 by `check_registry_sentences_sci_20261119.py` (16 of 16). Figures I read myself: Steinberg 2021 Figure 4 (page 8 at 170 dpi: panels B, D, E and H), Steinberg 2026 Figure 6 (all panels) and Figure 2F. Not re-checked by me, "per the delegate": Figure 1D/1F bars and brackets (T3), Figure 5C values (T12), Figure 5E asterisk on VGLUT1 (T16), the mean ± SD printing in Breton (T4), Appendix material.

## 2. Verdicts (the delegate's, after my check; one line each)

| # | Record sentence (short) | Verdict | After my check |
|---|---|---|---|
| T1 | Title: "AAV-WWOX rescues organoid phenotype" | OVERSHOOT | holds: in the 2021 paper "W-AAV" is a plasmid knock-in at the AAVS1 locus (a safe-harbour site), "supraphysiological expression ... and a partial rescue"; the KO LFP rescue used a lentivirus; only the 2026 paper uses an AAV9 vector, neurons only |
| T2 | Summary: "altered Ca²⁺ dynamics" | OVERSHOOT | holds: the 2021 text has no calcium imaging (LFP and cell-attached only); the Ca²⁺ imaging is in the 2026 paper |
| T3 | (i) "disfunzione del compartimento inibitorio misurata a livello di trascritto e di proteina" | OVERSHOOT | holds: the source says "disrupt the balance between glutamatergic and GABAergic neurons"; GABRB2/3 are transcript-only; no function of the inhibitory compartment is measured in 2021 |
| T4 | (ii) sIPSC amplitude halved (Breton) | OVERSHOOT (minor) | numbers exact (27.5/57.3 = 0.48; the frequency fell too, 10.3 to 8.4 Hz); omitted context: mouse Synapsin-Cre knockout, P13 to P17 slices, pooled controls, mean ± SD; the measure is not from the organoid system |
| T5 | (iii) four occurrences of 'depolariz', one paragraph, four general citations, no WWOX data | SUPPORTED | 4 hits, one Discussion paragraph; Obata 1978, Ben-Ari 2007, Murata and Colonnese 2020, Khalilov 2005; that paragraph cites WWOX spectral power as its support |
| T6 | (iii) the authors' verb and the clinical sentence | SUPPORTED | both quotes verbatim and in that order |
| T7 | token census KCC2 ... bumetanide | SUPPORTED | all seven 0 |
| T8 | marker direction: authors' surprise theirs, non-discrimination LEGEND's | SUPPORTED | no statement of non-discrimination anywhere |
| T9 | astrogenesis by IF, immunoblot (week 20), qPCR | SUPPORTED | text says week 20; the Fig 3 / EV2 legend says "week 24" (source-internal conflict); qPCR is in Fig 3B and 3C, not described in the text |
| T10 | "difetto DDR con perdita del checkpoint apoptotico" | OVERSHOOT (minor) | the text speculates ("might indicate loss of checkpoint inhibition") and tests it with one marker (cleaved caspase-3); the Fig EV2 title does say "loss of checkpoint inhibition"; "apoptotic" is the record's word |
| T11 | Wnt activation, dyslamination, OXPHOS down / glycolysis up | UNVERIFIABLE_SURFACE | Wnt and dyslamination supported; the metabolic sets rest on Appendix Fig S3A-B (not held; Fig 4B prints only the regionalization and cell-cycle sets); 2021 measures no metabolism; nuclear β-catenin 1.76 ± 0.03 and 1.67 ± 0.27 against 1 ± 0.18 from 2 WT and 4 KO organoids, no test (I read Fig 4E) |
| T12 | firing increased and normalised by the rescue (P = 0.7681) | SUPPORTED | P and groups exact; a no-difference P is not equivalence; the KO-line rescue is lentiviral and is LFP slow-wave power (Fig 2G, no WT-vs-lenti bracket per the delegate), not firing |
| T13 | Fig 4H: CTIP2 overshoot, TBR1 and SATB2 no bracket | SUPPORTED | I read the same: TBR1 WT-KO **, KO-W-AAV ****, no WT-W-AAV bracket; CTIP2 WT-KO *, KO-W-AAV ****, WT-W-AAV **; third untitled sub-panel ***, ****, no WT-W-AAV bracket; the W-AAV medians sit above WT in all three; "tested and not significant" is an inference from the legend |
| T14 | size null; "does not reproduce the microcephaly seen in some patients" | OVERSHOOT (minor) | four P values, test and the eight W-AAV rows exact; the inference about microcephaly is the record's (organoid diameter is a proxy; the Introduction says many patients do not have microcephaly) |
| T15 | "Dorsal/ventral identity is unchanged but not uniformly so" | OVERSHOOT (minor) | 1 / 0,064 / 1 exact; the source's own text lists axis specification (ventral-dorsal) among enriched pathways and concludes "impaired spatial patterning, axis formation, and cortical layering" |
| T16 | "prova ... può correggere più domini cellulari" (c.517-2A>G) | OVERSHOOT | readouts reversed are real (firing, GAD67, DNA-damage response, some Wnt genes, lamination); astrocyte markers have no quantified rescue; the authors write "proof of concept ... and possibly for therapeutic intervention"; the ASO clause is the record's own inference |
| T17 | model relevance names KO and WOREE only | UNDERSHOOT | the SCAR12 (G372R) organoids show "very mild, if any" differences, no clear glutamatergic/GABAergic ratio change, normal layer markers, a Wnt pattern |
| T18 | Clinical meaning "Strongly supports ... la terapia genica" | OVERSHOOT | "proof of concept"; "partial rescue"; "further study is required before clinical translation"; two families |
| T19 | IT 1: text claims a WT comparison the panel does not draw | SUPPORTED | text "similar to the WT"; no WT-vs-treated bracket (I read Fig 6A(ii)) |
| T20 | IT 2: the panel half | SUPPORTED | all three sub-panels, SCAR12 and WOREE: brackets WT vs EGFP and EGFP vs WWOX only |
| T21 | IT 3: "without correcting RG abnormalities" | SUPPORTED | verbatim, p. 16 |
| T22 | IT 4: WWOX 0.4x to 7x wild type | UNVERIFIABLE_SURFACE | Supplementary Figure 1 is not held; the main text gives no WWOX level after AAV9 |
| T23 | IT 5: Fig 2F bar values and "central composition phenotype almost entirely the engineered knockout's" | OVERSHOOT | the bar values do not match (section 4); the text also reports RG increase in WOREE and SATB2/CTIP2 reduction in KO and WOREE |
| T24 | IT 6: "No randomization or blinding was applied in this study" | SUPPORTED | verbatim (Statistical analysis); the Supplementary Methods are not held |
| T25 | wave note: AAV9 arm at week 10, read at week 16, "different organoid cohort" | OVERSHOOT (minor) | infection week 10 and read week 16 and the layer-marker contrast by line are supported; "in a different organoid cohort" is the record's inference (the source says "an earlier time point"); the AAV9 arm had no knockout line; the treated bars are numerically above WT |

## 3. What the audit does not reach

Appendix Figures S1 to S6 and the 2026 supplementary figures volume and Supplementary Methods are not held (T11 metabolic sets, the Fig S2A panel, T22 values, T24 methods). The delegate could not read them and neither can I. The preprint triple of PROVENANCE-01 (PMID 42128308) is outside the six IT asked for and outside this unit.

## 4. IT's six PROVENANCE-01 triples: disposition

- **Triples 1, 2, 3, 6: SUPPORTED** against the recovered 2026 text and my reading of Figure 6A(ii). These can carry the Source repoint's boundaries as written.
- **Triple 4 (WWOX 0.4x to 7x): UNVERIFIABLE_SURFACE**: the supplementary figures volume of the 2026 paper is not held. Do not propagate it as a verbatim locator until the volume is held; it stays an attestation by the earlier reader.
- **Triple 5 (Fig 2F values): do not use as written.** My own axis read, made before the dispatch and not shown to the delegate, and the delegate's read agree: WWOX-KO neurons about -2.4 and RGs about +1.0; SCAR12 RGs about -0.27 and neurons about +0.19 (positive); WOREE RGs about +0.07 and neurons about -0.06. IT's attestation has KO RGs about +0.55 and SCAR12 neurons about -0.2. The proposition's second half ("the patient lines carry a maturation phenotype instead") is the authors' own sentence ("milder phenotypes ... rather than RG dysfunction") but the same paper reports an RG increase in WOREE organoids and reduced SATB2+ and CTIP2+ neurons in KO and WOREE, so the sentence needs its qualifiers.
- IT's manifest entry numbers in the candidate are zero-based (entries[10] is the manifest's eleventh entry); not an error, but a reader using one-based counting lands on a neighbour.

## 5. Findings F1 to F15 (for IT as correction candidates; each with the source's words and a proposed direction; I apply nothing)

Severity is my reading: **A** = changes what a consumer would conclude; **B** = wording that overstates; **C** = context to add.

| # | Sev | Where | Finding |
|---|---|---|---|
| F1 | A | Summary, first sentence | "altered Ca²⁺ dynamics" is not a result of Steinberg 2021 (S21 'calcium' 2 hits, both unrelated: S100 calcium-binding protein B and a gene list; no calcium imaging). The 2026 paper measures firing by Ca²⁺ imaging (the claim's Pathway line names Ca²⁺ too). |
| F2 | A | Summary, last sentence | "prova che la reintroduzione di WWOX può correggere più domini cellulari": the source says "proof of concept ... and possibly for therapeutic intervention"; astrocyte markers are not quantified in the rescue arm; the Wnt effect is on some genes only. |
| F3 | A | Clinical meaning | "Strongly supports ... la terapia genica": the source says "proof of concept", "partial rescue", "further study is required before clinical translation", two families. |
| F4 | A | IT triple 5 | Bar values wrong (section 4). |
| F5 | B | Title | "AAV-WWOX rescues organoid phenotype": in the 2021 anchor "W-AAV" is a knock-in plasmid at the AAVS1 locus (supraphysiological, partial); the KO LFP rescue is lentiviral; the AAV9 vector is the 2026 paper's and acts on neurons only. The wave note already carries "names a model result with these qualifiers". |
| F6 | B | Summary (i) | "disfunzione del compartimento inibitorio misurata a livello di trascritto e di proteina": the source says an imbalance between glutamatergic and GABAergic neurons; GABRB2/3 are transcript-only. |
| F7 | B | Summary | "difetto DDR con perdita del checkpoint apoptotico": a speculation tested with one marker (cleaved caspase-3), not a demonstrated checkpoint loss. |
| F8 | B | Summary | "firma OXPHOS↓/glicolisi↑": a transcriptional gene-set enrichment resting on Appendix Fig S3A-B (not held); no metabolism is measured. "attivazione Wnt": nuclear β-catenin 1.7-fold from 2 WT and 4 KO organoids, no test (the qPCR panel has significant genes). |
| F9 | B | Evidence boundary | "the rescue normalises two of three layer markers and overshoots the third": in all three sub-panels the W-AAV median sits above WT; the text names only CTIP2 and SATB2 as recovered; "not significant" is an inference from the all-pairwise ANOVA in the legend (W-AAV n = 4 from 1 batch). |
| F10 | B | Summary | "firing aumentato e normalizzato dal rescue": the patient-line firing P = 0.7681 is a no-difference test, not equivalence; the KO-line rescue is lentiviral LFP slow-wave power, not firing. |
| F11 | C | Summary (ii) | the Breton measure is a mouse neuron-specific knockout in P13 to P17 slices with pooled controls and mean ± SD; the frequency also fell. |
| F12 | C | Adjacent negatives | "The model does not reproduce the microcephaly seen in some patients": organoid diameter is a proxy. "Dorsal/ventral identity is unchanged but not uniformly so": the source's own text also lists axis specification as enriched and concludes impaired spatial patterning and axis formation. |
| F13 | C | Model relevance | the SCAR12 (G372R) organoids are absent from the record: "very mild, if any, differences in the forebrain neuronal population development, astrocyte development, and DDR signaling". |
| F14 | C | Summary (astrogenesis) | the text says immunoblot at week 20; the Fig 3 / EV2 legend says week 24; the qPCR panels (Fig 3B week 15, 3C week 24) are not described in the text. |
| F15 | C | Wave note | "in a different organoid cohort" is an inference (the source says "an earlier time point", cell-attached recording; Fig 6A(ii) is Ca²⁺ imaging); the AAV9 arm had no knockout line; the treated bars are numerically above WT in active ROIs and amplitude. |

## 6. The exact registry sentences (CLAIM 002 in `claim_registry_current.md`; markdown marks removed; confirmed present by script) and the direction proposed

1. F5, Title: "WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype". Direction: name the vector arms (knock-in at AAVS1, lentivirus, AAV9 neuron-directed) or leave the Title with the wave note's qualifier.
2. F1, Summary: "WWOX-deficient organoids show hyperexcitability and altered Ca²⁺ dynamics; WWOX re-expression improves the phenotype." Direction: state what each paper measured (local field potential and cell-attached firing in 2021; Ca²⁺ imaging in 2026). Pathway line: "P1 — Ca²⁺ / network dysregulation; P7 — gene therapy readiness".
3. F6, Summary (i): "cioè disfunzione del compartimento inibitorio misurata a livello di trascritto e di proteina". Direction: "squilibrio fra neuroni glutammatergici e GABAergici (GAD67 per immunofluorescenza e GAD1/GAD2 per trascritto; GABRB2/3 solo trascritto)".
4. F11, Summary (ii): "ampiezza sIPSC dimezzata" (Breton): add the system (mouse, P13 to P17, pooled controls).
5. F14: "Astrogenesi aumentata per immunofluorescenza, immunoblot (settimana 20) e qPCR": add that the legend says week 24.
6. F7: "difetto DDR con perdita del checkpoint apoptotico". Direction: "caspasi-3 clivata ridotta nella VZ (un solo marcatore), che gli autori leggono come possibile perdita di checkpoint".
7. F8, F10: "attivazione Wnt; dyslamination corticale; firma OXPHOS↓/glicolisi↑; firing aumentato e normalizzato dal rescue". Direction: "firma trascrizionale (GSEA)"; firing: say which line and which readout.
8. F2: "Il rescue del modello con variante splice c.517-2A>G prova che la reintroduzione di WWOX può correggere più domini cellulari". Direction: "mostra, come proof of concept, ..." with the list of readouts actually reversed.
9. F9, Evidence boundary: "the rescue normalises two of three layer markers and overshoots the third". Direction: "is not distinguishable from wild type in two of three sub-panels (no bracket; medians above WT) and exceeds it in the third".
10. F12: "The model does not reproduce the microcephaly seen in some patients" and "Dorsal/ventral identity is unchanged but not uniformly so": add "organoid diameter" and the source's own axis-patterning sentence.
11. F13, Genotype/model relevance: "umano organoide WWOX-KO + WOREE-derived": add the SCAR12 forebrain-organoid result.
12. F3, Clinical meaning: "Strongly supports the network-level model, la terapia genica e l'uso degli organoidi come piattaforma sperimentale." Direction: "Supports ... la terapia genica come proof of concept (rescue parziale, due famiglie)".
13. F15, Wave note: "infection at week 10 on a hyperactivity seen at week 7 in a different organoid cohort": say "an earlier time point" and that the AAV9 arm had no knockout line.
14. The `Source` line is unchanged by this audit: "Steinberg et al., 2024 preprint; Steinberg et al., 2021, EMBO Molecular Medicine, full text reviewed"; the repoint to PAPER 094 can rest on IT triples 1, 2, 3 and 6 (section 4).

## 7. What did not change, and what is owed

Nothing in the data layer moves: the Table S1 values, the Breton means, the firing P, the Fig 4H brackets and the token counts are exact. IT's correction candidate should be audited as ADV-082's was (a second blind check of the repaired sentences). Open for ADV: CLAIM 005 (NPY and PV sentences) next, then B; the 2021 Appendix Figures and the 2026 supplementary volume remain on the supply list (decision page item 14).

**Not medical advice.** Nothing was applied to any registry, candidate or file outside this folder.
