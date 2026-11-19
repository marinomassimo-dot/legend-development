"""SCI 2026-11-19 (ADV-084): the proposition/quote/anchor triples of the CLAIM 005 wording audit (the claim's Title, Summary, Clinical meaning and the NPY / PV / glia / cytokine / GAD
sentences of its Evidence boundary), with every text quote checked verbatim by script against the plain renderings before dispatch.
Sources: S19 = Hussain 2019 (PMID 30290271, JATS XML rendered by ../claim002_unit_audit_sci_20261119/render_jats_plain_sci_20261119.py), S21 = Steinberg 2021 (PMID 34268881, same renderer),
EV = the derived plain text of Expanded View Tables EV1 and EV2 of S21 (files/fulltext/PMID34268881_assets/Table_EV1_EV2_derived.txt, tab-separated).
Writes triples_005_for_delegate.md into the scratch dir and prints the number of quotes not found.   Run:  python3 -I build_triples_claim005_sci_20261119.py <scratch-dir>
(scratch-dir must already hold hussain2019_plain.txt and steinberg2021_plain.txt)"""
import sys
from pathlib import Path

if len(sys.argv) != 2 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
D = Path(sys.argv[1])


def norm(s):
    return " ".join(s.replace("‐", "-").replace("‑", "-").replace("’", "'").replace("‘", "'").split())


SRC = {"S19": norm((D / "hussain2019_plain.txt").read_text(encoding="utf-8")),
       "S21": norm((D / "steinberg2021_plain.txt").read_text(encoding="utf-8")),
       "EV": norm(Path("/home/desktop/legend-development/files/fulltext/PMID34268881_assets/Table_EV1_EV2_derived.txt").read_text(encoding="utf-8"))}
T = []


def t(record, prop, quotes, anchor, tag=""):
    T.append(dict(record=record, prop=prop, quotes=quotes, anchor=anchor, tag=tag))


t("Title: «Reduced GABAergic interneurons and glial activation in WWOX-KO»",
  "Read as a statement about the anchor paper: GABAergic interneurons are reduced and glia are activated in the Wwox knockout. Say which interneuron populations were counted, in which regions, and what 'glial activation' rests on (which markers, which measures).",
  [("S19", "Importantly, we observed that Wwox deletion leads to a significant reduction in the overall number of PV+ and NPY+ GABA-ergic inhibitory interneurons in mouse hippocampus."),
   ("S19", "Additionally, we also detected evidence of active neuroinflammation and gliosis in the brains of Wwox KO mice.")],
  "S19 Discussion, first paragraph; Results 3.1 to 3.4", "TITLE")
t("Genotype/model relevance: «murino / Wwox-KO sistemico; genotipo caution: KO ≠ compound het; segnale GABAergico e gliale plausibilmente trasferibile come meccanismo generale di vulnerabilità» "
  "[gloss: mouse, systemic Wwox knockout; the GABAergic and glial signal plausibly transferable as a general mechanism of vulnerability]",
  "The record calls the knockout 'systemic' and the signal plausibly transferable as a general vulnerability mechanism. Compare with the authors' own scope sentences about patients, and say what the source states about the model (sex, age, constitutive or conditional).",
  [("S19", "In conclusion, our observations may explain, at least in part, what is occurring in the brains of patients affected by WWOX loss of function pathologies."),
   ("S19", "This study provides the first pathophysiological evidence on the effects of Wwox loss of function in the brain.")],
  "S19 Abstract (2 weeks old, both sexes); Discussion, last two paragraphs; Methods > Animal experiments")
t("Summary: «In one systemic constitutive Wwox-KO mouse model at two weeks» ... and the per-group n",
  "One model, two weeks, both sexes; the group sizes are 7 and 7 (PV), 6 and 6 (NPY), 6 and 6 (IBA-1), 8 and 6 (GFAP), 4 and 4 (qRT-PCR), 5 and 5 (Western blot). Check every n against the text, and say whether the source gives the number of litters or the sex split per group.",
  [("S19", "Wwox KO (n = 7) and WT (n = 7) mice"), ("S19", "Wwox KO (n = 6) and WT (n = 6) mice"),
   ("S19", "Wwox KO mice (n = 8) in comparison to WT mice (n = 6)"), ("S19", "Wwox KO mice (n = 5) compared with WT mice (n = 5)")],
  "S19 Results 3.1 to 3.5; Methods > Animal experiments; figure legends", "NUMBERS")
t("Summary: «PV-positive interneuron counts are lower in DG, CA1 and across the whole hippocampus (−44%)» [gloss: PV+ counts lower in dentate gyrus, CA1 and the whole hippocampus (-44%)]",
  "As written: which regions carry a test, the P values, the 44 percent, and what the source says about CA3.",
  [("S19", "Stereological quantification indicated that Wwox KO mice displayed astatistically significant reduction in the total number of PV+ interneurons in the DG region (p < .005, Fig. 1 C1) and CA1 subfield (p < .05, Figs. 1 C2), in comparison to control mice."),
   ("S19", "The overall reduction of PV+ interneurons in Wwox KO mice amounted to 44% when the hippocampus was taken in its entirety (p < .005, Fig. 1 D)."),
   ("S19", "A significantly low number of PV+ interneurons in Wwox KO mice was also evident in the CA1 and CA3 subfields")],
  "S19 Results 3.1; Fig 1 legend")
t("Summary: «NPY-positive counts are lower in DG only» [gloss: NPY+ counts lower in the dentate gyrus only]",
  "As written. Say what the source states for CA1, CA3 and the whole hippocampus (a test, a number, or only a figure panel), and whether the source's own summary sentence and Abstract agree with 'DG only'.",
  [("S19", "the DG region of Wwox KO mice displayed a 30% reduction in the total number of NPY+ interneurons when compared to control WT mice (p < .05)"),
   ("S19", "However, the CA1 and CA3 subfields, did not exhibit any obvious difference in the number of NPY+ interneurons between Wwox KO and WT mice"),
   ("S19", "Number of NPY+ interneurons in the entire hippocampus is shown in Fig. 2 D."),
   ("S19", "In summary, Wwox KO mice exhibit significant reductions in the abundance of both PV+ and NPY+ GABA-ergic interneurons in the various hippocampal subfields."),
   ("S19", "Wwox KO mice displayed significantly reduced numbers of calcium-binding protein parvalbumin (PV) and neuropeptide Y (NPY) expressing interneurons in different subfields of the hippocampus")],
  "S19 Results 3.1 (second paragraph and summary sentence); Abstract; Fig 2 legend", "OVERSHOOT/UNDERSHOOT?")
t("Summary: «IBA1 ... immunoreactive area fractions are higher in CA1, CA3 and whole hippocampus»",
  "As written for IBA-1: the regions, the P values and the dentate gyrus.",
  [("S19", "The area fraction (AF) occupied by IBA-1+ cells was marginally higher in the DG region (Figs. 3 A1, B1 and C1), however the CA1 and CA3 subfields displayed a significant increase (p < .05) in the AF occupied by IBA-1+ structures in Wwox KO mice and when the hippocampus (p < .005) is considered in its entirety")],
  "S19 Results 3.2; Fig 3 legend")
t("Summary: «... and GFAP immunoreactive area fractions are higher in CA1, CA3 and whole hippocampus»",
  "As written for GFAP: the regions, the percentages, the P values and the dentate gyrus.",
  [("S19", "the area fraction (AF) occupied by GFAP+ soma and processes of astrocytes in the CA1 and CA3 subfields displayed a very significant increase of 36% and 53%, respectively (p < .05 Figs. 4 A2–A3, B2–B3, and C2–C3), whereas in the DG region the increment was marginal"),
   ("S19", "When the hippocampus was taken in its entirety, the overall increase in GFAP+ structures was 30% in Wwox KO mice (p < .05, Fig. 4 D).")],
  "S19 Results 3.3; Fig 4 legend")
t("Summary: «Marker-positive abundance and area fraction — not cell loss, not glial cell number.»",
  "The record limits the glial result to an area fraction and says it is not a glial cell number. Compare with the source's own words about the astrocytes and the microglia (hyperplasia, hypertrophy, morphology) and say whether the source counted any glial cells.",
  [("S19", "Astrocytes displayed hypertrophy as well as hyperplasia in the hippocampus of Wwox KO mice."),
   ("S19", "Importantly, IBA-1+ cells in CA1 and CA3 subfields of Wwox KO were less ramified, displayed shorter and thicker processes and larger soma, characteristic of activated microglia")],
  "S19 Results 3.2 and 3.3; Methods > Image analyses of IBA-1+ and GFAP+ immunoreactive structures", "UNDERSHOOT?")
t("Summary, the 2026-10-04 addition «concordanza umana indipendente»: «nelle liste di espressione differenziale deposte di quel paper NPY porta log2FC −6,24 e padj 4,62e-15, ed è il segnale più forte del pannello di marcatori gliali, GABAergici e oligodendrogliali interrogato in quella lettura — non il padj più basso della lista, che è di DACT2 a 2,29e-15 —, e la stringa NPY compare zero volte nel corpo dell'articolo» "
  "[gloss: in the deposited differential-expression lists NPY has log2FC -6.24 and padj 4.62e-15 ... not the lowest padj of the list, which is DACT2 at 2.29e-15; the string NPY occurs zero times in the article body]",
  "Check the NPY row, the DACT2 row, the sentence 'not the lowest padj of the list' against the whole of Expanded View Tables EV1 (upregulated genes) and EV2 (downregulated genes) (the derived text names each row's table; sort by padj yourself over both tables and say which gene has the lowest padj in each table and overall), and count 'NPY' in the article text of S21 (name your search and hit count).",
  [("EV", "ENSG00000122585 NPY 4852 1.16E-18 4.6200000000000001E-15 -6.24"),
   ("EV", "ENSG00000164488 DACT2 168002 4.3000000000000002E-19 2.2900000000000001E-15 -2.72")],
  "EV (derived text of Table EV1 and Table EV2 of S21; the original workbooks are EMMM-13-e13610-s006.xlsx (EV1) and EMMM-13-e13610-s005.xlsx (EV2) in the same assets folder); S21 full text", "NUMBERS/ABSENCE")
t("Summary: the same addition calls the organoid transcript a «concordanza umana indipendente» (independent human concordance) with the mouse NPY-positive cell count, with these limits stated by the record: «trascritto contro conta di cellule marcatore-positive; organoide cerebrale senza risoluzione regionale ... lista tagliata a p grezzo < 0,01 su 2 WT contro 4 KO; null costitutivo in entrambi i sistemi»",
  "Is 'independent human concordance' a fair word for a bulk RNA-seq transcript list from human cerebral organoids (2 WT against 4 KO, nominal-P cut) set beside a mouse stereological count of NPY+ cells in a hippocampal subfield? Say what the two measurements share and do not share, from the two sources' own words (design, sample, region, readout).",
  [("S21", "RNA sequencing (RNA-seq) of week 15 COs and transcriptome analysis (WT: n = 2, KO: n = 4)."),
   ("S19", "the DG region of Wwox KO mice displayed a 30% reduction in the total number of NPY+ interneurons")],
  "S21 Fig 4 legend; S19 Results 3.1", "CLASS: preparation/system")
t("Clinical meaning: «Supports the glial axis as a modifier.»",
  "The record reads the source as support for a glial axis acting as a modifier. Say what the source claims about glia (cause, consequence, modifier, or association) and whether any measurement here can separate a glial modifier from a consequence of seizures or of the interneuron loss.",
  [("S19", "Clinical and experimental observations have provided strong evidence that inflammatory processes within the brain might constitute a crucial mechanism in the pathophysiology of seizures and epilepsy (Vezzani et al., 2011)."),
   ("S19", "We observed that Wwox null mice display signs of neuroinflammation as suggested by the increased detection of IBA-1+ cells (i.e., activated microglia) and GFAP+ astrocytes as well as increased expression of inflammatory cytokines Tnf-a and Il6.")],
  "S19 Discussion, fourth paragraph; whole text (search for 'modifier', 'cause', 'consequence', 'secondary')", "CLINICAL MEANING")
t("Clinical meaning: «The source measures no GABA concentration, no synaptic inhibition, no E/I ratio and no drug.»",
  "ABSENCE: the source measures no GABA concentration, no synaptic inhibition, no E/I ratio and no drug. Search the whole text (name your terms and hit counts); say what the source itself writes about GABA levels and what it measured (Western blot of GAD65/67).",
  [("S19", "GAD65/67 protein expression was shown to accurately reflect levels of GABA synthesis and abundance (Lindefors, 1993), therefore decreased expression of these proteins would also indicate lower GABA levels.")],
  "S19 whole text; Results 3.4", "ABSENCE")
t("Evidence boundary: «NPY CA1/CA3 are reported as showing no obvious difference; the whole-hippocampus NPY panel carries no significance marker — a visual panel observation, not a reported test.»",
  "The CA1/CA3 text is as quoted; the second half is a figure observation (Fig 2D). The figure images of this paper are NOT held on this host: if you cannot open Figure 2D, say UNVERIFIABLE_SURFACE for the second half and say what the text says about the whole hippocampus.",
  [("S19", "However, the CA1 and CA3 subfields, did not exhibit any obvious difference in the number of NPY+ interneurons between Wwox KO and WT mice"),
   ("S19", "Number of NPY+ interneurons in the entire hippocampus is shown in Fig. 2 D.")],
  "S19 Results 3.1; Fig 2 legend. Figures: not held", "FIGURE NOT HELD")
t("Evidence boundary: «IBA1/GFAP in DG are marginal and unmarked.»",
  "The dentate gyrus is called marginal by the text; 'unmarked' (no significance marker on the panel) is a figure observation (Figs 3C1 and 4C1; not held).",
  [("S19", "whereas in the DG region the increment was marginal"),
   ("S19", "was marginally higher in the DG region")],
  "S19 Results 3.2 and 3.3; Fig 3 and 4 legends. Figures: not held", "FIGURE NOT HELD")
t("Evidence boundary: «Il6 and Tnf-a transcripts are both more than 1.5-fold up by qPCR (p below 0.05, n=4/group).» [the registry's current sentence, after its 2026-10-30 correction]",
  "As written: both cytokines more than 1.5-fold up AND p below 0.05 (for which gene or genes?). Read the Results sentence and the Figure 4 legend for which gene carries the significance statement; the figure itself is not held.",
  [("S19", "We observed > 1.5 fold upregulation of both cytokines (Il6 significant at p < .05) in Wwox KO (n = 4) mice in comparison to Wwox WT (n = 4) mice (Fig. 4 E)."),
   ("S19", "(E) Expression of Tnf-a and Il6 in Wwox KO mice hippocampi (n = 4). Y axis in the graph represents relative linear FC values with respect (w.r.t) to Wwox WT mice hippocampi (n = 4); error bars represent ± SEM, *p value < .05, two tailed unpaired Student's t-test.")],
  "S19 Results 3.3; Fig 4E legend", "OVERSHOOT?")
t("Evidence boundary: the registry's correction note quotes the paper: «the paper's Results 3.3 ('> 1.5 fold upregulation of both cytokines (significant at p < .05) in KO (n = 4)')» and says it supersedes the earlier wording «Only Il6, not Tnf-a, is significant».",
  "ABSENCE/QUOTE: the registry puts this quotation in quotation marks as the paper's Results 3.3. Search S19 for that exact string and for any sentence that makes Tnf-a significant; say what the held text says instead, in its exact words.",
  [],
  "S19 Results 3.3; whole text (search 'significant at p', 'Il6', 'Tnf')", "QUOTE CHECK")
t("Evidence boundary: «GAD65/67 is protein abundance only.»",
  "Western blot abundance of GAD65/67 in hippocampal extracts, n = 5 per group; the authors read it as lower GABA synthesis. Say what the source measured and what it infers.",
  [("S19", "As observed in Fig. 5A, Western blot analysis of hippocampal protein extracts obtained from Wwox KO mice (n = 5) compared with WT mice (n = 5) revealed significantly lower levels of GAD65/67 protein expression."),
   ("S19", "We also detected decreased levels of Glutamic Acid Decarboxylase protein isoforms GAD65/67 expression in Wwox null hippocampi suggesting lower levels of GABA synthesis.")],
  "S19 Results 3.4; Abstract; Fig 5 legend")

bad = []
for i, x in enumerate(T, 1):
    for s, q in x["quotes"]:
        if norm(q) not in SRC[s]:
            bad.append((i, s, q[:80]))
NAMES = {"S19": "Hussain 2019 (PMID 30290271)", "S21": "Steinberg 2021 (PMID 34268881)", "EV": "Steinberg 2021 Expanded View Tables EV1/EV2 (derived text)"}
out = ["# Triples to audit (record sentence, proposition, quotes, anchor)", "",
       "Record sentences are CLAIM 005's own words (Italian kept, English glosses in brackets for convenience; the Italian governs). Quotes were checked verbatim by script against the renderings named in the brief. Non-breaking hyphens normalised to '-'; the XML governs.", ""]
for i, x in enumerate(T, 1):
    out.append(f"## T{i}" + (f" [{x['tag']}]" if x["tag"] else ""))
    out.append(f"- Record sentence: {x['record']}")
    out.append(f"- Proposition: {x['prop']}")
    for j, (s, q) in enumerate(x["quotes"], 1):
        out.append(f"- Quote {j} [{NAMES[s]}]: \"{q}\"")
    out.append(f"- Anchor: {x['anchor']}")
    out.append("")
(D / "triples_005_for_delegate.md").write_text("\n".join(out), encoding="utf-8")
print(len(T), "triples;", sum(len(x["quotes"]) for x in T), "quotes;", "NOT FOUND:", bad)
