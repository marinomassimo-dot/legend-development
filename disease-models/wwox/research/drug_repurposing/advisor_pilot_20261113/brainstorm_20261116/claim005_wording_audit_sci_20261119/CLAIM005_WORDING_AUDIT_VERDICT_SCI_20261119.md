# CLAIM 005 wording audit and the class of each overshoot (SCI, 2026-11-19, ADV-084; hypothesis level; not medical advice; nothing applied)

## 0. Answer first

CLAIM 005 is **not clean, but it is the cleanest of the three claims I audited**: of 17 triples a fresh blind delegate returned **7 SUPPORTED, 3 UNDERSHOOT, 4 OVERSHOOT, 1 NOT_IN_SOURCE, 2 UNVERIFIABLE_SURFACE**. I checked every source passage and count it quoted against the held bytes (10 of 10 quoted passages found verbatim, all counts agree) and recomputed the padj ranking over both Expanded View tables myself. The Title, the model scope, every n and every P value of the Summary are exact (the data layer holds again). The exposure is again interpretive, plus **one registry correction that quotes its source with a word missing** (T16), which is new.

The five findings that matter: (1) the Clinical meaning's "Supports the glial axis as a modifier": the paper says inflammation "might play a role" and that cause or consequence is open, and the word "modifier" is absent; (2) the correction note of 2026-10-30 puts in quotation marks, as the paper's Results 3.3, a sentence that drops "Il6" from the parenthesis, so it says both cytokines are significant where the held text attaches the P value to Il6 alone (the three held copies agree); (3) "il padj più basso della lista, che è di DACT2" is true only inside the downregulated table (the overall lowest is HK2, then TCEAL5); (4) "concordanza umana indipendente" joins a bulk organoid transcript to a mouse cell count for one gene, while the same organoid paper reports the opposite sense for the GABAergic markers (GAD up against S19's GAD65/67 down); (5) the Il6/Tnf-a sentence reads as if the P value covered both.

## 1. Method (as dispatched; brief and triples in this folder)

- Scope (ADV-084: "NPY and PV sentences"): the claim's Title, genotype/model line, Summary (including the 2026-10-04 organoid NPY addition), Clinical meaning, and the Evidence boundary sentences on NPY, glia, cytokines and GAD. **Not audited:** the long imported-premises paragraph of the Evidence boundary (early death, epileptogenesis, Mallaret 2014, the third-party review, the organoid glia null) and the wave note: they rest on many other papers and were verified by their own earlier audits.
- Triples: 17 (36 quotes verified verbatim by script before dispatch, 0 not found; `build_triples_claim005_sci_20261119.py`), built from the claim's own sentences against Hussain 2019 (held JATS XML, three byte copies; figures and supplement not held) and Steinberg 2021 (XML and the Expanded View tables as derived text and workbooks).
- Delegate: `legend-delegate`, asked sonnet / effort high; read back: **sonnet 14 of 14 turns, effort high 14 of 14, peak context 87,068, output 22,591, cache read 0.72 million**. Report as delivered (1,706 words by my count, cap 1,800 held): `AUDIT_REPORT_AS_DELIVERED.md`.
- My checks (post hoc): `check_findings_claim005_sci_20261119.py` (quoted passages found; counts: 'modifier' 0, 'cause' 12, 'consequence' 8, 'significant at p' 1, 'Il6' 6, 'Tnf' 5; S21 'NPY' 0; padj ranking over 2,267 rows: HK2 8.75e-34, TCEAL5 9.43e-21, DACT2 2.29e-15, NPY 4.62e-15); the registry sentences of section 5 confirmed present in CLAIM 005 by `check_registry_sentences_claim005_sci_20261119.py` (15 of 15). I also read the 2026-10-30 verifier's file (`research/locator_audits/2026-10-30_it9_p1_verifier.md`, finding H1) to see what its quotation says. Not re-checked by me, per the delegate: nothing figure-based (no figure of Hussain 2019 is held).

## 2. Verdicts

| # | Record sentence (short) | Verdict | After my check |
|---|---|---|---|
| T1 | Title: reduced GABAergic interneurons and glial activation | SUPPORTED | scope is PV+ and NPY+ interneurons and IBA-1/GFAP area fractions; the title is a fair summary |
| T2 | model scope; "plausibilmente trasferibile" | SUPPORTED | constitutive full knockout, 2 weeks, both sexes; the authors' own scope sentence is stronger ("may explain, at least in part, what is occurring in the brains of patients") than the record's hedge |
| T3 | one model, two weeks, the n | SUPPORTED | every n matches; no litter count and no per-group sex split in the text |
| T4 | PV lower in DG, CA1, whole (-44%) | UNDERSHOOT (minor) | P values exact; CA3 omitted: "A significantly low number of PV+ interneurons ... was also evident in the CA1 and CA3 subfields" (CA3 P value only on a panel not held) |
| T5 | NPY lower "in DG only" | UNDERSHOOT (minor) | the stated numbers are DG only (30 percent, p < .05; CA1/CA3 "no obvious difference"); the authors' summary and Abstract say "in the various hippocampal subfields" and the whole hippocampus is only "shown in Fig. 2 D"; the record is the more careful reading |
| T6 | IBA1 higher in CA1, CA3, whole | SUPPORTED | CA1/CA3 p < .05, whole p < .005, DG "marginally higher" |
| T7 | GFAP higher in CA1, CA3, whole | SUPPORTED | 36 and 53 percent (p < .05), whole 30 percent (p < .05), DG "marginal" |
| T8 | "not cell loss, not glial cell number" | UNDERSHOOT (minor) | the measurement limit is right (area fraction; no glial cell counted: 'cell number' 0 hits) but the authors claim "hypertrophy as well as hyperplasia" and activated-microglia morphology |
| T9 | NPY row and "not the lowest padj of the list, which is DACT2" | OVERSHOOT (minor) | NPY and DACT2 rows exact, NPY 0 hits in the article; DACT2 is the lowest padj only in the downregulated table; over both tables HK2 (8.75e-34) and TCEAL5 (9.43e-21) are lower |
| T10 | "concordanza umana indipendente" | OVERSHOOT | one transcript direction in a bulk organoid RNA-seq (2 WT against 4 KO, nominal-P list) beside a mouse hippocampal cell count; the organoid paper reports "a marked increase in GABAergic markers" (opposite in sense to S19's GAD65/67 reduction) and never mentions NPY; independence is not judgeable from the texts |
| T11 | "Supports the glial axis as a modifier." | OVERSHOOT | "supports the idea that inflammation might play a role ... further investigation is needed ... what is cause or consequence"; 'modifier' 0 hits; the authors' own Introduction calls gliosis a consequence of seizures; one time point at 2 weeks in a constitutive knockout, no glial manipulation |
| T12 | the source measures no GABA concentration, synaptic inhibition, E/I ratio or drug | SUPPORTED | the GAD65/67 Western blot is the only GABA-axis measure and the authors infer GABA levels from it |
| T13 | NPY whole-hippocampus panel carries no significance marker | UNVERIFIABLE_SURFACE | CA1/CA3 half supported; the panel (Fig 2D) is not held; the text gives no test for the whole hippocampus |
| T14 | IBA1/GFAP in DG "marginal and unmarked" | UNVERIFIABLE_SURFACE | "marginal" is in the text for both; "unmarked" rests on panels 3C1 and 4C1 (not held) |
| T15 | Il6 and Tnf-a both > 1.5-fold up "(p below 0.05, n=4/group)" | OVERSHOOT | "We observed > 1.5 fold upregulation of both cytokines (Il6 significant at p < .05)"; the Fig 4E legend names no gene for its asterisk; no fold value is printed |
| T16 | correction note quotes Results 3.3 as "... (significant at p < .05) in KO (n = 4)" | NOT_IN_SOURCE | the held sentence (three byte copies, two digests): "We observed > 1.5 fold upregulation of both cytokines (Il6 significant at p < .05) in Wwox KO (n = 4) mice in comparison to Wwox WT (n = 4) mice (Fig. 4 E)." The string in the registry omits "Il6" and changes the meaning |
| T17 | GAD65/67 protein abundance only | SUPPORTED | Western blot, n = 5 against 5, p < .05; the authors infer lower GABA synthesis |

## 3. The class of each overshoot (ADV-084's request)

Classes (the four ADV named, plus three that the evidence added):
- **A** wrong-paper attribution (a measurement credited to a paper that did not make it);
- **B** preparation or vector conflated (organoid with mouse, knock-in plasmid with AAV, transcript with cell count);
- **C** meaning stronger than the authors' own limit (clinical meaning, a mechanism word, "proof");
- **D** title word;
- **E** scope slip (a quantifier or a unit of comparison that the source does not carry: "lowest of the list", "DG only", "p for both", "two of three", a region or table left out);
- **F** a quotation that the held bytes do not carry (a word dropped from a quoted source sentence);
- **G** a hedge lost (a speculation or a single-marker test written as a finding).

| Finding | Class |
|---|---|
| T11 "glial axis as a modifier" | **C** |
| T10 "concordanza umana indipendente" | **B** (also G: one gene chosen, the GABAergic markers run the other way) |
| T9 DACT2 "lowest padj of the list" | **E** |
| T15 Il6 and Tnf-a "p below 0.05" | **E** |
| T16 the correction note's quotation | **F** |
| T4, T5, T8 (undershoots) | **E** (regions and whole-hippocampus omitted) and, for T8, the authors' interpretation left out |

Across the claims audited with the same method (002 and 005 classified here in full; for 021 only the three major findings that checkpoint E names, F1 to F3, are used, and I did not re-classify its other ten; 025 was IT's candidate and is not classified here), by class: **C is the most consequential** (021 F1 closing inference and Clinical meaning extended to the human EEG; 002 F2 "prova", F3 "Strongly supports ... la terapia genica"; 005 T11 "modifier"); **E is the commonest** (021 F3 "UNDERSTATES" holds for four starred rows only; 002 F9, F10, F12; 005 T9, T15 and the undershoots T4, T5); **B** (002 F5 vector, 005 T10); **D** (021 F2 "directly", 002 F5); **A** once (002 F1 "altered Ca²⁺ dynamics"); **F** once (005 T16); **G** (002 F7, F8; 005 T10). This is a count of a few findings, not a rate. In all three claims the numbers hold.

**The pattern, for ADV's decision (a proposal, not applied):** the failures sit at four moments of writing, and each has a mechanical guard that would have caught it: (1) **a verb or a measurement word in a Summary, Title or Clinical meaning sentence** ("rescues", "altered Ca²⁺ dynamics", "modifier", "concordance") should name the paper and preparation that measured it, so class A and B surface at writing time; (2) **a Clinical meaning or Title sentence** should sit beside the authors' own limit sentence (partial rescue, "further investigation is needed", "proof of concept"), copied, not paraphrased, so class C and D surface; (3) **a quantifier** ("only", "lowest", "all", "both", "two of three") should carry the unit it quantifies over (which table, which region, which gene) in the same sentence, so class E surfaces; (4) **a quotation in quotation marks** should be pasted by script from the held bytes, never typed, and the script's check recorded, so class F cannot occur (the T16 string passed a verifier because nobody re-read the held sentence). The pattern across three claims says a rule at the point of writing is cheaper than auditing 47 claims; I did not test the rule.

## 4. The T16 finding in detail (a registry correction that does not match the held text)

The Evidence boundary's correction note (2026-10-30, `BATCH_20261019_031`, `CC-20261030-INTEGRATOR-IT9-BATCH-01`) supersedes "Only Il6, not Tnf-a, is significant" with the paper's Results 3.3 quoted as "> 1.5 fold upregulation of both cytokines (significant at p < .05) in KO (n = 4)". The finding H1 of `research/locator_audits/2026-10-30_it9_p1_verifier.md` carries the same quotation. All three held byte copies of the paper (the two with digests `3672e628fd6f` and `ea6e0fa2fa11`, identical sentence) read "(Il6 significant at p < .05)". What survives of the correction: **direction** ("> 1.5 fold upregulation of both cytokines" and the Abstract "overexpression of inflammatory cytokines Tnf-a and Il6") is in the source, so Tnf-a up is supported; **significance for Tnf-a is not stated** (the text is silent, the legend's asterisk names no gene, the figure is not held). The earlier wording "Only Il6, not Tnf-a, is significant" is closer to the sentence on Il6 but also says more than the text on Tnf-a (a silence is not a "not significant"). Consumers: the IT9 seed rows S085 and S086 (TNF and IL6 direction) were repaired on this correction (H1 of the verifier file); their direction stands, their stated significance basis does not. I cannot tell from the files whether the verifier read another text version; the held bytes are three copies of one sentence.

## 5. Findings G1 to G9 for IT (correction candidates; exact registry sentences; proposed direction; nothing applied)

1. G1 (T4, E), Summary: "PV-positive interneuron counts are lower in DG, CA1 and across the whole hippocampus (−44%)": add that the text also calls CA3 significantly low (CA3 P value on a panel not held).
2. G2 (T5, E), Summary: "NPY-positive counts are lower in DG only": keep, add that the authors' own summary and Abstract say "in the various hippocampal subfields" and the whole-hippocampus panel is referenced but carries no number in the text.
3. G3 (T8, E), Summary: "Marker-positive abundance and area fraction — not cell loss, not glial cell number.": add the authors' interpretation ("hypertrophy as well as hyperplasia", activated-microglia morphology) beside the measurement limit.
4. G4 (T9, E), Summary: "non il padj più basso della lista, che è di DACT2 a 2,29e-15": say "il più basso fra i geni downregolati (tabella EV2)"; over both tables the lowest are HK2 (8,75e-34) and TCEAL5 (9,43e-21).
5. G5 (T10, B/G), Summary: "concordanza umana indipendente": direction proposed: "una direzione concorde per un gene (NPY, trascritto bulk di organoide) con il conteggio murino"; add that the same organoid paper reports GABAergic markers up (GAD67, GAD1, GAD2), the opposite sense to the mouse GAD65/67 reduction; independence is not demonstrated by the two texts.
6. G6 (T11, C), Clinical meaning: "Supports the glial axis as a modifier.": direction: "Supports a glial association; the authors leave cause or consequence open (the wave note's seizure-secondary reading fits at least as well)".
7. G7 (T15, E), Evidence boundary: "Il6 and Tnf-a transcripts are both more than 1.5-fold up by qPCR (p below 0.05, n=4/group).": direction: "both more than 1.5-fold up; the text attaches p < .05 to Il6; no fold value is printed".
8. G8 (T16, F), Evidence boundary correction note: the quoted string "> 1.5 fold upregulation of both cytokines (significant at p < .05) in KO (n = 4)": replace by the held sentence with "Il6" (section 4) and say that the direction for Tnf-a is the source's and its significance is not stated; the superseded wording "Only Il6, not Tnf-a, is significant" is also stronger than the text on Tnf-a; check the IT9 seed rows S085 and S086's basis.
9. G9 (T13, T14), supply: the figures of Hussain 2019 (Figs 1 to 5) are not held (the figures folder is empty); the panel-level significance markers the record cites (NPY whole hippocampus, IBA1/GFAP in the dentate gyrus, the qPCR asterisks) cannot be audited until they are; add to the supply list (decision page item 14).

Registry sentences quoted above are confirmed present in CLAIM 005 (markdown marks removed) by the check script; the Source line is unchanged by this audit.

## 6. What did not change

Nothing in the data layer moves: the PV and NPY P values and percentages, the IBA-1 and GFAP regional values, the GAD Western blot n and the NPY and DACT2 table rows are exact. Two further items for ADV: a cross-claim observation for IT (CLAIM 002 reports GAD markers up in the organoid and CLAIM 005 the mouse GAD65/67 down; the sentence "concordanza" in 005 should not read as if the GABAergic picture agreed); and a second blind check of IT's repaired sentences is owed, as for 021 and 002.

**Not medical advice.** Nothing was applied to any registry, candidate or file outside this folder.
