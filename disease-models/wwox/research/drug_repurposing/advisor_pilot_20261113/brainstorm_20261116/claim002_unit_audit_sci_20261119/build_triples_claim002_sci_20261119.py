"""SCI 2026-11-19 (ADV-083): the proposition/quote/anchor triples of the CLAIM 002 unit (CLAIM 002's own sentences plus IT's PROVENANCE-01 triples),
with every text quote checked verbatim by script against the plain renderings before dispatch.
Sources: S21 = Steinberg 2021 (PMID 34268881, JATS XML rendered by render_jats_plain_sci_20261119.py), S26 = Steinberg 2026 (PMID 42397075, OUP accepted
manuscript, text extracted from the PDF with line-number and watermark lines removed by this script), BR = Breton 2021 (PMID 34634460, JATS XML rendered the same way).
Writes the delegate's triples file and prints the number of quotes not found.   Run:  python3 -I build_triples_claim002_sci_20261119.py <scratch-dir>
(scratch-dir must already hold steinberg2021_plain.txt and breton_plain.txt; it receives s26_clean.txt and triples_002_for_delegate.md)"""
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
D = Path(sys.argv[1])
fitz = Path("/home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt").read_text(encoding="utf-8")
lines = [x for x in fitz.split("\n") if not re.fullmatch(r"\s*\d{1,3}\s*", x) and "ACCEPTED MANUSCRIPT" not in x and "Downloaded from" not in x]
(D / "s26_clean.txt").write_text(" ".join(" ".join(lines).split()), encoding="utf-8")


def norm(s):
    return " ".join(s.replace("‐", "-").replace("‑", "-").replace("’", "'").replace("‘", "'").split())


SRC = {"S21": norm((D / "steinberg2021_plain.txt").read_text(encoding="utf-8")),
       "S26": norm((D / "s26_clean.txt").read_text(encoding="utf-8")),
       "BR": norm((D / "breton_plain.txt").read_text(encoding="utf-8"))}
T = []


def t(record, prop, quotes, anchor, tag=""):
    T.append(dict(record=record, prop=prop, quotes=quotes, anchor=anchor, tag=tag))


# ---- CLAIM 002's own sentences (record sentences quoted as written; Italian kept, English gloss in brackets) ----
t("Title: «WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype»",
  "Read as a statement about the anchor papers: loss of WWOX causes network hyperexcitability in organoids, and AAV-delivered WWOX rescues the organoid phenotype.",
  [("S21", "Furthermore, we provide a proof of concept that ectopic WWOX expression could potentially rescue these phenotypes."),
   ("S21", "This resulted in hESCs overexpressing WWOX under UBP promoter from the AAVS1 locus (W-AAV)"),
   ("S26", "neuron-targeted AAV9-hSynI-WWOX restoration effectively rescued neuronal functional phenotypes without correcting RG abnormalities")],
  "S21 Abstract and Fig 1 legend (W-AAV construction); S26 Discussion", "TITLE")
t("Summary, first sentence: «WWOX-deficient organoids show hyperexcitability and altered Ca²⁺ dynamics; WWOX re-expression improves the phenotype.»",
  "The Steinberg 2021 organoid anchor shows hyperexcitability AND altered Ca2+ dynamics in WWOX-deficient organoids (the record's Pathway line reads 'P1 — Ca2+ / network dysregulation'). Search S21 for any calcium-imaging or Ca2+-dynamics measurement and name your terms and hit count; also say whether S26 carries one.",
  [("S21", "To characterize the functional properties of the WWOX-KO COs, we performed local field potential recordings (LFP) on 7-week CO slices."),
   ("S21", "The WSM S COs' neurons showed a drastic increase in the firing rate (about a fourfold)")],
  "S21 Results (hyperexcitability section; patient-line section); whole-text search for calcium / Ca2+ / GCaMP / imaging in S21 and S26", "ABSENCE")
t("Summary (i): «aumento dei marcatori GABAergici (GAD67/GAD1/GAD2) con diminuzione delle componenti recettoriali GABA_A (GABRB2/3) e VGLUT1 invariato, cioè disfunzione del compartimento inibitorio misurata a livello di trascritto e di proteina» "
  "[gloss: GABAergic markers GAD67/GAD1/GAD2 up with GABA-A receptor components GABRB2/3 down and VGLUT1 unchanged, i.e. dysfunction of the inhibitory compartment measured at transcript and protein level]",
  "As written, including the words 'dysfunction of the inhibitory compartment' and 'measured at transcript and protein level'.",
  [("S21", "Immunostaining revealed that although VGLUT1 expression remained similar, a marked increase in expression of GAD67 was observed in KO COs compared with WT."),
   ("S21", "RNA levels of SLC17A6 (VGLUT2), SLC17A7 (VGLUT1), GAD1 (GAD67) and GAD2 (GAD65) followed the same trend (Fig 1D)."),
   ("S21", "In the top 100 downregulated genes were genes related to GABA receptors (GABRB3, GABRB2)"),
   ("S21", "did disrupt the balance between glutamatergic and GABAergic neurons.")],
  "S21 Results (first section; RNA-seq section); Fig 1D-F")
t("Summary (ii): «squilibrio E/I spostato verso l'eccitazione, sostenuto dalla misura funzionale del corpus (ampiezza sIPSC dimezzata in Breton 2021: S-CTLs 57.3 ± 31.0pA; S-KOs 27.5 ± 19.4 pA, con la frase degli autori «favors excitation over inhibition, primarily through an impairment in the amplitude of the inhibitory currents»)» "
  "[gloss: E/I imbalance shifted toward excitation, supported by the corpus's functional measure: sIPSC amplitude halved in Breton 2021]",
  "The sIPSC amplitude is about halved in the knockout (57.3 to 27.5 pA) and the authors say the neocortex favors excitation over inhibition through the amplitude of inhibitory currents; the record offers this as support for an E/I imbalance in the organoid anchor's system. Say what the Breton system is and whether 'halved' fits the numbers.",
  [("BR", "S-CTLs 57.3 ± 31.0pA; S-KOs 27.5 ± 19.4 pA"),
   ("BR", "These data indicate that the Wwox S-KO neocortex favors excitation over inhibition, primarily through an impairment in the amplitude of the inhibitory currents.")],
  "BR Results > Unbalanced spontaneous excitatory and inhibitory currents (Fig 4G, H)")
t("Summary (iii): «IPOTESI — «GABA depolarizzante / firma GABAergica immatura», PREMISE: DEFAULT_FROM_TEXTBOOK, e non una firma misurata: nel sorgente le quattro occorrenze di depolariz stanno tutte in un unico paragrafo di Discussione, il cui sostegno sono quattro citazioni di neuroscienza dello sviluppo generale e nessun dato WWOX» "
  "[gloss: not a measured signature: the four occurrences of 'depolariz' all sit in one Discussion paragraph, supported by four general developmental-neuroscience citations and no WWOX data]",
  "COUNT AND ABSENCE: (a) the number of occurrences of 'depolariz' in S21 and whether all sit in one Discussion paragraph; (b) that paragraph's citations are general developmental neuroscience (name them) and it carries no WWOX measurement of GABA polarity. Name your search terms and hit counts.",
  [("S21", "It should be noted that several lines of evidence implicate that during development, GABAergic synapses have a depolarizing effect (Obata et al, 1978; Ben-Ari et al, 2007; Murata & Colonnese, 2020)."),
   ("S21", "Seizure dynamics in developmental epilepsies are known to be dependent on depolarizing GABA responses")],
  "S21 Discussion (the paragraph beginning 'First, although the neuronal population was largely intact')", "COUNT/ABSENCE")
t("Summary (iii), continued: «con il verbo degli autori stessi «further strengthens the idea that depolarizing GABA plays a key role in seizure susceptibility», e la frase clinica che ne segue — «These findings shed a new light on the lack of efficacy of common anticonvulsant therapies on immature neurons» — è tratta da quell'idea, non da una misura in questo sistema» "
  "[gloss: the authors' own verb; and the clinical sentence that follows is drawn from that idea, not from a measurement in this system]",
  "The two quoted sentences are the authors' and are quoted as written; the record's reading is that the clinical sentence derives from the idea and not from a measurement in this system. Check the quotes, their order and what the sentence before them cites as its evidence.",
  [("S21", "The evidence of increased mean spectral power in WWOX-depleted COs and WSM FOs, and its recovery in the presence of lentivirus containing WWOX, further strengthens the idea that depolarizing GABA plays a key role in seizure susceptibility."),
   ("S21", "These findings shed a new light on the lack of efficacy of common anticonvulsant therapies on immature neurons")],
  "S21 Discussion, same paragraph", "ATTRIBUTION")
t("Summary: «Censimento token sull'artefatto dichiarato (PMID34268881_Steinberg2021_PMC.xml): KCC2 0 · NKCC1 0 · SLC12A5 0 · SLC12A2 0 · gramicidin 0 · perforated patch 0 · bumetanide 0» [gloss: token census, all zero]",
  "These seven tokens occur zero times in the article's text (body, legends, Methods, tables; say whether you count the reference list).",
  [],
  "ABSENCE: search the whole of S21 for each of the seven tokens (case-insensitive) and give the count per token", "ABSENCE")
t("Summary: «l'inferenza «quindi la direzione dei marcatori non discrimina fra i due meccanismi» è di LEGEND, non della fonte; la lettura che la fonte dà dello stesso pattern è un'altra: «This can indicate a disruption in development of normal and balanced neuronal networks, supporting the increased electrical activity observed in these organoids.»; la sorpresa degli autori è loro («This finding is even more surprising when considering the decrease in GABA receptor components seen by RNA-seq.»)» "
  "[gloss: the inference that marker direction does not discriminate between the two mechanisms is LEGEND's, not the source's; the source reads the same pattern differently]",
  "The two quoted sentences are the authors' (check attribution and wording); the source nowhere states that the marker direction fails to discriminate between hypo-inhibition and depolarizing GABA (search S21 and say what you searched).",
  [("S21", "This finding is even more surprising when considering the decrease in GABA receptor components seen by RNA-seq."),
   ("S21", "This can indicate a disruption in development of normal and balanced neuronal networks, supporting the increased electrical activity observed in these organoids.")],
  "S21 Discussion, same paragraph", "ATTRIBUTION")
t("Summary: «Astrogenesi aumentata per immunofluorescenza, immunoblot (settimana 20) e qPCR» [gloss: increased astrogenesis by immunofluorescence, immunoblot (week 20) and qPCR]",
  "S21 supports increased astrogenesis in KO organoids by immunofluorescence AND immunoblot at week 20 AND qPCR. Check each of the three techniques in the KO-versus-WT comparison of the knockout organoids (say where the qPCR of astrocytic markers is, if anywhere) and the 'progressed through time' wording.",
  [("S21", "This revealed a marked increase in astrocytic cells in WWOX-KO COs that progressed through time, and was partially reversed in W-AAV COs."),
   ("S21", "This was further supported by immunoblot analysis of week 20 COs (Fig EV2A and B)."),
   ("S21", "It is notable that GFAP also marks RGs (Middeldorp et al, 2010), which are abundant in week 15, but are reduced in number in week 24, which could be a source of noise at early stages.")],
  "S21 Results > astrogenesis section; Fig 3, Fig EV2 legends (Western blot there is 'week 24' in the Fig 3 legend; say which week each technique carries)")
t("Summary: «difetto DDR con perdita del checkpoint apoptotico» [gloss: DNA-damage-response defect with loss of the apoptotic checkpoint]",
  "S21 shows a DNA-damage-response defect and a loss of the apoptotic checkpoint in knockout organoids. Say whether 'loss of the apoptotic checkpoint' is what the source states or what it speculates and then tests with one marker.",
  [("S21", "This led us to speculate that the continued proliferation of damaged cells might be accompanied by diminished apoptosis, which might indicate loss of checkpoint inhibition."),
   ("S21", "This hypothesis was addressed by staining for cleaved caspase-3 in the VZ, which revealed a decline in apoptosis of these cells upon WWOX-KO, and was rescued in the W-AAV COs (Fig EV2G and H).")],
  "S21 Results > astrogenesis and DNA damage response section; Fig EV2")
t("Summary: «attivazione Wnt; dyslamination corticale; firma OXPHOS↓/glicolisi↑» [gloss: Wnt activation; cortical dyslamination; OXPHOS down / glycolysis up signature]",
  "Four findings listed as established in the knockout organoids: Wnt activation, cortical dyslamination, an OXPHOS-down / glycolysis-up signature. Check each against the source's own strength of wording (a gene-set enrichment is not a metabolic measurement; say if S21 measures any metabolism).",
  [("S21", "We found an approximate 1.7-fold increase in the normalized intensity of β-catenin in the nucleus of WWOX-KO COs, supporting the notion of Wnt pathway activation after the loss of WWOX."),
   ("S21", "Gene set enrichment analysis (GSEA) and gene ontology (GO) enrichment analysis of the top 3,000 differentially expressed genes revealed, among others, inhibition of processes related to ATP synthesis-coupled electron transport and oxidative phosphorylation (Appendix Fig S3A)"),
   ("S21", "marked enrichment was seen in pathways related to regionalization, neuron fate commitment and specification, axis specification (ventral–dorsal and anterior–posterior), and glycolysis and gluconeogenesis (Fig 4B and Appendix Fig S3A and B)")],
  "S21 Results > RNA-sequencing section; Fig 4B, 4E; Appendix Fig S3A-B (Appendix figures are not held; say UNVERIFIABLE_SURFACE where a point rests only on them)")
t("Summary: «firing aumentato e normalizzato dal rescue» [gloss: firing increased and normalised by the rescue]; and Evidence boundary: ««normalizzato» is accurate for firing rate (P = 0,7681, parents vs rescued patient organoids)»",
  "Firing is increased in the patient-line organoids and 'normalised' by the rescue; the P value 0.7681 compares parents with rescued patient organoids. Say what that no-difference P value does and does not show, which lines carry it, and whether the knockout (CRISPR) organoids carry a firing rescue and by which vector.",
  [("S21", "There was no significant difference between the firing rate of WSM P and WSM S W-AAV COs' neurons (P = 0.7681)."),
   ("S21", "Importantly, transduction of a lentivirus containing WWOX cDNA resulted in recovery of the KO line, with respect to the mean power spectral density (Fig 2F and G)."),
   ("S21", "Statistical significance was determined using one-way ANOVA with Tukey's multiple comparisons test. Data information: ***P ≤ 0.001 and ****P ≤ 0.0001.")],
  "S21 Results > patient-derived organoids section (cell-attached recordings); Fig 2F-G and its legend; Fig 5B-C")
t("Evidence boundary: «In Figure 4H: for CTIP2/nuclei the WT-versus-W-AAV comparison is drawn and is significant (**) with the rescue ABOVE wild type — an overshoot; for TBR1 and the third (SATB2) sub-panel no WT-versus-W-AAV bracket is drawn, which under the legend's all-pairwise Tukey test means tested and not significant. The paper's own sentence scopes recovery to the knockout comparator, and the section closes with «prevents these changes to some extent». So the rescue normalises two of three layer markers and overshoots the third.» "
  "[Figure panel claim: the figure image is a PDF page; render page 8 of the PDF yourself and read the brackets and asterisks]",
  "Figure 4H panel reading (which markers, which brackets, which asterisks, where the third sub-panel is titled) and the text sentence; also whether 'normalises two of three layer markers' is the right summary given the text says 'CTIP2+ cell and SATB2+ cell numbers recovered' and the legend's statistics. Say what you can read and what you cannot.",
  [("S21", "although CTIP2+ cell and SATB2+ cell numbers recovered and layering improved in W-AAV COs compared with WWOX-KO COs, RNA levels did only partially (Fig 4G and H)."),
   ("S21", "The reintroduction of WWOX prevents these changes to some extent, further supporting its possible implication in gene therapy."),
   ("S21", "Statistical significance was determined using one-way ANOVA with Tukey's multiple comparisons test (WT: n = 9 from 3 batches; KO: n = 16 from 3 batches; and W-AAV: n = 4 organoids from 1 batch).")],
  "S21 Results > RNA-sequencing section (last two paragraphs); Fig 4G-H legend; the figure itself: PDF page 8 of PMID34268881_Steinberg2021.pdf (the loose figure JPGs in the assets folder are not in figure order; do not rely on their names)", "FIGURE")
t("Adjacent negatives: «(1) Organoid size is a clean null — Appendix Table S1, WT vs KO: wk6 0,3675, wk10 0,5619, wk15 0,9949, wk18 0,8952 (ordinary one-way ANOVA, Tukey), all W-AAV rows likewise null. The model does not reproduce the microcephaly seen in some patients.» "
  "[gloss: the size null is a performed and reported test; the model does not reproduce microcephaly]",
  "The four P values and test are as printed in Appendix Table S1 (a Word file in the assets folder; open it with python zipfile and read word/document.xml); 'all W-AAV rows likewise null' (check the 12 rows); and the inference 'the model does not reproduce the microcephaly seen in some patients' versus the source's own sentence.",
  [("S21", "Next, to address the microcephalic phenotype observed in some patients, we measured the diameter of our organoids through the culture period, which showed no significant difference (Appendix Fig S2A).")],
  "S21 Results > first section; Appendix Table S1 (EMMM-13-e13610-s004.docx), rows of Appendix Fig S2A", "SUPPLEMENT TABLE")
t("Adjacent negatives: «(2) Dorsal/ventral identity is unchanged but not uniformly so — Appendix Fig S3C rows: dorsal 1, combined 1, ventral 0,064 (Kruskal–Wallis), where the running text reports simply no significant difference.» [gloss: the ventral value 0.064 is not significant and is not nothing]",
  "The three values and the test as printed in Appendix Table S1 (rows of Appendix Fig S3C), and the running text's sentence (find it in S21 and quote it).",
  [("S21", "Importantly, when examining the expression of dorsal and ventral genes in COs")],
  "S21 Results > RNA-sequencing section; Appendix Table S1, rows of Appendix Fig S3C", "SUPPLEMENT TABLE")
t("Summary, last sentence: «Il rescue del modello con variante splice c.517-2A>G prova che la reintroduzione di WWOX può correggere più domini cellulari, ma non dimostra che un ASO corregga c.1057-2A>G.» "
  "[gloss: the rescue of the c.517-2A>G splice-variant model proves that reintroducing WWOX can correct several cellular domains]",
  "In the c.517-2A>G patient line, which readouts does S21 show reversed by the W-AAV rescue (name each, with the figure and the sentence), and which readouts does it show in the patient line without a rescue arm? Is 'proves' and 'several cellular domains' the source's strength?",
  [("S21", "Consistent with our previous findings, week 10 WSM S COs exhibited increased expression of GAD67 compared with WSM F1 and WSM M2, a phenotype that was reversed in WSM S W-AAV COs (Fig 5D and E)."),
   ("S21", "We next assessed the expression of astrocytic markers and found increased expression of GFAP and S100β in WSM S compared with age-matched controls (Fig 6A)."),
   ("S21", "The status of the Wnt pathway was also assessed using qPCR, with findings suggestive of activation in week 10 WSM S COs compared with the age-matched WSM P and WSM S W-AAV (Fig 6D)."),
   ("S21", "Finally, we evaluated cortical lamination using immunofluorescence and found decreased expression of cortical markers CTIP2+ and SATB2+ in WSM S COs (Fig 6E and F).")],
  "S21 Results > patient-derived organoids section (fourth paragraph); Fig 5, Fig 6")
t("Genotype/model relevance: «umano organoide WWOX-KO + WOREE-derived» (and the Summary names only the WOREE-derived patient line)",
  "The record does not mention the SCAR12 (c.1114G>C) patient-derived organoids; say whether S21's SCAR12 results change what the record's model-relevance and Summary sentences imply (state exactly what S21 reports for the SCAR12 forebrain organoids on the glutamatergic/GABAergic ratio, cortical markers and Wnt).",
  [("S21", "Surprisingly, transcript expression levels of neuronal markers did not show any clear difference in the ratio between glutamatergic and GABAergic neurons (Fig EV4B)."),
   ("S21", "supported the notion of normal neuronal and cortical development (Fig EV4C)"),
   ("S21", "Interestingly, RNA levels of Wnt genes did show a pattern suggestive of the Wnt pathway activation (Fig EV4D), which raises a question regarding its role in the pathogenesis of the milder disease.")],
  "S21 Results > patient-derived organoids section (last paragraph); Fig EV4", "UNDERSHOOT?")
t("Clinical meaning: «Strongly supports the network-level model, la terapia genica e l'uso degli organoidi come piattaforma sperimentale. Non predice da solo risposta clinica né trasferibilità quantitativa al genotipo di riferimento.» "
  "[gloss: strongly supports the network-level model, gene therapy and the use of organoids as an experimental platform]",
  "'Strongly supports ... la terapia genica' (gene therapy) as a reading of the anchor papers' own strength of claim. Compare with the authors' own scope sentences.",
  [("S21", "Furthermore, we provide a proof of concept that ectopic WWOX expression could potentially rescue these phenotypes."),
   ("S21", "This makes generalizing our results more difficult, a problem we partially addressed by gene manipulation in hESCs."),
   ("S21", "As samples from DEE patients in general, and WWOX-related disorders in particular, are limited, we generated patient-derived organoids from only two families, one of each syndrome.")],
  "S21 Abstract; Limitations of study", "INFERENCE")
# ---- IT's six PROVENANCE-01 triples (CC-20260826-PROVENANCE-01, section LOCATOR TRIPLES FOR BLIND AUDIT), proposition and quote as IT wrote them ----
t("IT triple 1 (PROVENANCE-01)",
  "The paper's text asserts a comparison with wild type that the cited panel does not draw.",
  [("S26", "hyperexcitability to a level similar to the WT organoids [Fig. 6A(ii)].")],
  "S26 Results p. 13, describing Figure 6A(ii)", "IT")
t("IT triple 2 (PROVENANCE-01)",
  "The panel half of the same pair: the WT-versus-treated bracket does not exist. Figure 6A(ii): brackets present for WT vs EGFP and for EGFP vs AAV9-hSynI-WWOX; no bracket joining WT and the treated condition.",
  [], "S26 Figure 6 panel A(ii): the figure file is /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_assets/figs/fig_p36_1430x1754.jpeg ; open it as an image and say what brackets and asterisks are printed in each of the three sub-panels", "IT; FIGURE")
t("IT triple 3 (PROVENANCE-01)",
  "The authors state the scope of what the rescue corrects.",
  [("S26", "rescued neuronal functional phenotypes without correcting RG abnormalities")],
  "S26 Discussion p. 16", "IT")
t("IT triple 4 (PROVENANCE-01)",
  "Delivered WWOX protein is not controlled to a physiological level: it spans 0.4x to 7x wild type across lines with the same vector. Attested values (IT): Supplementary Figure 1 panel M, WWOX over HSP-90 relative to JH WT = 1: WPM S1 0.1, WPM D1 0.1, WPM D3 0.3, WPM S1 AAV9 7; panel L: JH WT 1, LM-iPS 0.2, WSM S2 AAV9 0.4, WSM S5 AAV9 0.4, LM-iPS AAV9 0.9.",
  [], "S26 Supplementary Figure 1, panels K-M (supplementary figures volume, page 2). THE SUPPLEMENTARY FIGURES VOLUME IS NOT HELD (absent from the host, no lawful route): declare UNVERIFIABLE_SURFACE for the values and say whether the S26 main text states any WWOX protein level after AAV9-WWOX infection (search S26 and say what it says)", "IT; SUPPLEMENT NOT HELD")
t("IT triple 5 (PROVENANCE-01)",
  "The central composition phenotype is almost entirely the engineered knockout's; the patient lines carry a maturation phenotype instead. Attested values (IT): Figure 2F, 'RGs and Neu cell fraction changes', log2FC versus WT: WWOX-KO Neu about -2.6 and RGs about +0.55; SCAR12 Neu about -0.2 and RGs about -0.15; WOREE both within about 0.05.",
  [], "S26 Figure 2 panel F: /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_assets/fig2F_600dpi.png (crop of panel F; the axis is printed). Read each bar's end value against the axis yourself and say what you read, per genotype and per cell class, with the direction (sign) of each bar; say whether the proposition's sentence about 'maturation phenotype' is what the text says (search S26 and quote)", "IT; FIGURE")
t("IT triple 6 (PROVENANCE-01)",
  "The study declares no randomization and no blinding.",
  [("S26", "No randomization or blinding was applied in this study")],
  "S26 Statistical analysis", "IT")
# ---- the 2026 paper's role in the record's wave note ----
t("Wave note (2026-10-29): «The only add-back after a documented phenotype read in this corpus is the neuron-directed AAV9 arm of the 2026 organoid paper: infection at week 10 on a hyperactivity seen at week 7 in a different organoid cohort, read at week 16, persistence unmeasured, hyperexcitability reduced to a level similar to wild type (not an equivalence test), layer markers up in one patient line and not the other, radial-glia abnormalities of the knockout lines not corrected ('without correcting RG abnormalities'; the patient-line impairment is described as neuronal).»",
  "As written. Check: infection week and read-out week, whether the hyperactivity was documented at week 7 in a different cohort, that persistence is not measured, the layer-marker statement by patient line, and the 'neuronal' description of the patient-line impairment.",
  [("S26", "we infected week 10 organoids with either AAV9-WWOX (see methods) or AAV9-EGFP (AAV9-SynapsinI-EGFP-WPRE), followed by 6 weeks of culture"),
   ("S26", "WWOX restoration increased the expression of both markers in WOREE organoids but not in SCAR12, which showed CTIP2 and SATB2 expression levels similar to WT."),
   ("S26", "Remarkably, neuron-specific restoration of WWOX was sufficient to reduce hyperexcitability to a level similar to the WT organoids [Fig. 6A(ii)].")],
  "S26 Results (AAV9 rescue section); Figure 6; Discussion", "")

bad = []
for i, x in enumerate(T, 1):
    for s, q in x["quotes"]:
        if norm(q) not in SRC[s]:
            bad.append((i, s, q[:80]))
NAMES = {"S21": "Steinberg 2021 (PMID 34268881)", "S26": "Steinberg 2026 (PMID 42397075)", "BR": "Breton 2021 (PMID 34634460)"}
out = ["# Triples to audit (record sentence, proposition, quotes, anchor)", "",
       "Record sentences are CLAIM 002's own words (Italian kept; English glosses in brackets are for convenience, the Italian governs). Quotes were checked verbatim by script against the renderings named in the brief. Non-breaking hyphens in the sources were normalised to '-'; the PDF/XML governs.", ""]
for i, x in enumerate(T, 1):
    out.append(f"## T{i}" + (f" [{x['tag']}]" if x["tag"] else ""))
    out.append(f"- Record sentence: {x['record']}")
    out.append(f"- Proposition: {x['prop']}")
    for j, (s, q) in enumerate(x["quotes"], 1):
        out.append(f"- Quote {j} [{NAMES[s]}]: \"{q}\"")
    out.append(f"- Anchor: {x['anchor']}")
    out.append("")
(D / "triples_002_for_delegate.md").write_text("\n".join(out), encoding="utf-8")
print(len(T), "triples;", sum(len(x["quotes"]) for x in T), "quotes;", "NOT FOUND:", bad)
