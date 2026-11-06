# Blind re-audit of three narrowed statements (IT31)

Depth for all three: full text, raw HTML of the PMC article pages (pmc.ncbi.nlm.nih.gov, fetched with curl, tags stripped by script). No page summariser was used for quotes. Europe PMC fullTextXML returned HTTP 500 and the PubMed MCP full-text tool returned an empty body, so neither was used.

| Statement | Verdict |
|---|---|
| S1 (PMC6757916, PMID 12122058) | SUPPORTED, with one wording note |
| S2 (PMC6792938, PMID 9482779) | SUPPORTED for the KD values; the ifenprodil part is a mix-up risk (see below) |
| S3 (PMC6368479, Table 2) | SUPPORTED on b, on the table note and on the footnote a text; the "does not make clear" clause is OVERSHOOT on the extracted table |

## S1
Locators (Materials and Methods, Electrophysiology and data analysis; Fig. 2 legend):
- "contained (in mM): 100 NaCl, 5 HEPES, 0.3 BaCl2, and 10 Tricine"; "pH was adjusted to 7.3 with KOH".
- "saturating concentration of both L-glutamate and glycine (100 uM each)".
- "performed at room temperature (18-24 C) ... currents ... at -60 mV".
- Fig. 2 legend: "IC50 ... 155 nM ... for NR2B wt"; "For NR2A wt ... IC50 values are 28 ... uM" (the "28 and 75 uM" pair is for NR2A wt and NR2B-(LIVBP NR2A)).
- Mg2+ appears only in the reference list (Paoletti 1995, "potentiation ... by extracellular Mg2+"). It is not in the Methods text. The solution composition is given without Mg and the paper never says Mg is absent. This matches the statement.
- cRNA: "Xenopus laevis oocytes were prepared ... injected with cRNAs ... as described by Paoletti et al. (1995, 1997)". The Methods name no species. This matches the statement.

More than the statement says:
- The 28 uM value is stated at -60 mV, equilibrium (Fig. 2A), and Fig. 2B shows the NR2A low-affinity inhibition is voltage-dependent. A reader who reuses 28 uM needs that.
- The legend reports 155 nM with Hill slope 0.98 and 96% maximal inhibition.
- The paper uses the 10 uM ifenprodil correction (about 10%) only for mutants.
- The 155 nM and 28 uM figures are "estimated values" from fits, with 3-15 oocytes per point.
- In a different context the paper uses LIVBP domains of rat NR2A and mouse NR2B for protein expression. That is not the oocyte cRNA.
- The statement's "NR1/NR2B vs NR1/NR2A" is a shorthand. The paper's labels are "NR2B wt" and "NR2A wt", and NR1 is the partner. The NR1 splice variant is not seen in the text I scanned.

## S2
Locators (Results, Fig. 2C legend):
- "yielding high- and low-affinity mKD values of 41 and 774 nM, respectively (Fig. 2C)" (27- to 29-d-old animals). The legend gives "41 nM (52%) and 774 nM (48%)". So the "mean KD" wording is right; the paper writes mKD.
- Holding potential, Methods: "holding potential of -60 mV".
- Abstract: "ifenprodil (10 microM) inhibits both the high-affinity population and a significant proportion of the low-affinity component". This supports the S2 ifenprodil clause.

Attribution of the 0.21 uM figure: it belongs to this paper (9482779), not to 9143010.
- Results: "inhibition curves to ifenprodil were biphasic, with IC50 values of 0.21 and 58 uM for the high- and low-affinity components" (27- to 29-d-old neurons, steady-state currents "in the continuous presence of 30 uM glycine", Fig. 4, four neurons, relative amplitudes 70% and 30%).
- It was fitted at 30 uM glycine and -60 mV (holding potential given in Methods).
- PMID 9143010 is Pahk and Williams, Neurosci Lett 1997;225:29-32, "Influence of extracellular pH on inhibition by ifenprodil at NMDA receptors in Xenopus oocytes". It was read at abstract level only. It reports recombinant NR1/NR2B in oocytes and a smaller ifenprodil inhibition at alkaline pH. It reports no 0.21 uM value in the abstract, and it is not cited by PMC6792938 (no match found in its text).

Trap in the ifenprodil clause: two different "high/low affinity" axes exist in this paper.
- Glycine-affinity populations: 41 nM and 774 nM.
- Ifenprodil-affinity components: 0.21 uM and 58 uM, at 70/30%.
These are not the same populations. The text says 10 uM ifenprodil "inhibited the high-affinity [ifenprodil] component completely but left the low-affinity [ifenprodil] component almost unaffected". The statement that 10 uM ifenprodil inhibits "part of the low-affinity [glycine] population" rests on the abstract and on the kinetic (7-chlorokynurenic acid dissociation) section, which I read only as far as the method description. I did not confirm the exact quantitative result there. So the "inhibits ... part of the low-affinity one" clause is SUPPORTED at abstract level only; the full-text figure was not checked.

Also omitted: the abstract gives "approximately 20 nM" for young (2-3 day) neurons, and "approximately 800 nM" as the low-affinity value. It adds a third, NR2A/NR2B-containing population interpretation. Note that the 41 nM figure is for the 27-29-day-old group.

## S3
Raw table text (Table 2 and its notes):
- Notes: "IC50 values were determined by TEVC using Xenopus oocytes unless noted otherwise; -, data not available a 3 uM glycine was used for IC50 determination b IC50 was calculated at human NMDA receptors c As determined by Ca2+ influx assay using HEK cells".
- Ifenprodil row: "Ifenprodil b 39.5 0.11 29.1 75.9 [90]". Ro 25-6981 row: "52 0.009 - - [91]". The Ro row has no marker. The ifenprodil row carries b only.
- Footnote a markers appear on rows for TCN-201 (0.11 a; 0.446 a; 0.32 a), "034 a, b", "MPX-007 ... a, b", and in the second table on GNE-8324. MPX-004 carries b only.

Findings:
- The three footnote texts are correct as stated.
- The "does not make clear which rows footnote a covers" clause is an OVERSHOOT. The rows are marked with superscripts in the table, and a is present on TCN-201, 034 and MPX-007, but not on the ifenprodil or Ro 25-6981 rows. So the 3 uM glycine does not apply to ifenprodil (39.5 / 0.11 / 29.1 / 75.9 uM) per the table. The extracted text shows the superscripts as inline letters, so the rendering may differ from the printed page, but the inline markers are present in the source.
- More: footnote c (TCN-201 first row, 0.11 / 50) is NOT TEVC, but a Ca2+ influx assay in HEK cells, an exception to the table note. The second table's EC50 note has a parallel structure.
- The table note "unless noted otherwise" is only partly explicit for rows with no marker. Rows with no marker are TEVC in oocytes by the note.
- The ifenprodil row uses a single reference [90]. The ifenprodil GluN2B value 0.11 uM and the Ro value 0.009 uM are from different references, so they are not from one head-to-head experiment.

## Anything the statements omit that matters
- S1: the 28 uM NR2A figure is a low-affinity, voltage-dependent inhibition read at -60 mV. The 155 nM value is a fit, not a single measurement.
- S2: keep the glycine-affinity populations and the ifenprodil-affinity components apart; the 0.21 uM belongs to the ifenprodil curve.
- S3: because the ifenprodil row has no a, do not state "3 uM glycine" for it.

## Setting
Ran as Sonnet 5.5 (claude-sonnet-5-5); effort as I see it was a low reasoning-effort setting. I cannot read the exact effort value.
