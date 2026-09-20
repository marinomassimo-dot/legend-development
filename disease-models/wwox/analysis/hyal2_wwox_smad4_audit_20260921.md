# Audit — Hyal-2/WWOX/Smad4 signalling and "bubbling cell death" (PMID 27845895)

**Target.** Hsu LJ, Schultz L, Hong Q, Van Moer K, Heath J, Li MY, Lai FJ, Lin SR, Lee MH, Lo CP,
Lin YS, Chen ST, Chang NS. *"Hyaluronan activates Hyal-2/WWOX/Smad4 signaling and causes bubbling
cell death when the signaling complex is overexpressed."* **Oncotarget** 2017;8(12):19137–19155.
PMID 27845895 · PMCID PMC5386674 · DOI 10.18632/oncotarget.13268 · Licence CC BY 3.0 (verified
via PubMed/PMC copyright query this session).

**Source artefact.** `files/fulltext/PMID27845895_PMC_MCPtext.txt` — 44,591 bytes,
sha256 `3e52aa0bddfc6ee15e32b33793b6ae3b8672313850b9ccda14e2e6b4c835d6c7`.
Content is the `full_text` field returned by the PubMed MCP extractor for PMC5386674, written
verbatim (one trailing newline added by the file writer; nothing removed, nothing reordered).
The extractor returned the abstract as a **separate** JSON field, which is therefore **not** in
that artefact; it is reproduced in full in §0.2 below so that every quotation in this audit is
traceable.

**Why this audit exists.** An external knowledge base (DisMech) carries a WWOX-DEE pathophysiology
node *"Hyal-2/WWOX/Smad4 Complex Failure"* whose single evidence item is this PMID, quoted as
*"In WWOX-deficient cells, HA failed to induce Smad2/3/4 relocation to the nucleus."* LEGEND had
never read this paper. This file establishes what the paper actually measured.

---

## VERDICT

**PARTIALLY SUPPORTED, WITH A SOURCING DEFECT AND A DIRECTION PROBLEM** — the DisMech sentence is a
*verbatim quotation of this paper's abstract*, but the paper's own Results prose, its Figure 2
legend and its Discussion each state the same effect more weakly than the abstract does (the
figure legend reports a **delay** — "Smad4 appeared to relocate into nucleus in 4 hr" — not a
failure); and every cell-death endpoint in the paper arises only in cells transfected to
overexpress the complex, so this paper cannot support a node in which *loss* of the
Hyal-2/WWOX/Smad4 complex **causes** neuronal death — as measured here, loss of WWOX *removes* a
death pathway rather than creating one.

---

## 0. Instrument state and what was read

### 0.1 Extraction defect — confirmed present, and severe in a specific way

The MCP surface for this paper is defective in the manner warned about, and the defect is
**selective**: italicised tokens are deleted, roman ones survive.

- The protein symbol "WWOX" (roman in this journal) survives — 248 occurrences. **A zero count
  for a protein symbol on this surface would still be an instrument reading, not a negative**, but
  here the protein name was not lost.
- The **italicised gene symbol** *WWOX* / *Wwox* **was** deleted throughout, leaving visible
  scars: `"Humangene is located on a chromosomal fragile site 16q23"`, `"alterations ofgene"`,
  `"null mutations ofgene in humans, rats and mice"`, `"wild typemouse embryonic fibroblast (MEF)
  cells"`, `"knockoutMEF cells"`, `"Null mutation ofgene causes severe neural diseases"`.
  **The genotype of the knockout MEF is therefore not recoverable from this surface.** I read it
  as *Wwox*-knockout MEF from context (the section is titled "Wild type WWOX is necessary for HA
  induction of protein nuclear translocation" and contrasts with "wild type … MEF"), and flag that
  as inference, not as a read datum.
- *in vitro* / *in vivo* deleted (0 occurrences, with gaps: `"has been established in[], in cell
  lines"`, `"We further showed theHyal-2/WWOX complex accumulated in the apoptotic nuclei"`).
- **All figure cross-references arrive empty** — every `(Figure)` and `(Figures)` in the artefact
  had a panel identifier that is gone. Panel-level attribution below is therefore reconstructed
  from the surrounding figure legends, which did survive in this paper, and is marked where
  uncertain.
- Tables, the reference list, GenBank accession numbers and the supplementary material are absent
  (`"(GenBank accession)"`, `"(Genbank accession)"`, `"SUPPLEMENTARY MATERIALS FIGURES AND TABLES"`
  as a bare heading). Every in-text citation is an empty bracket `[]` or `[,]`.
- One cell line name was mangled by the same deletion: `"human breast ERWWOXMCF-7 cells"` (Methods)
  — italic superscript status markers lost.

### 0.2 The abstract, verbatim (separate MCP field, not in the artefact file)

> "Malignant cancer cells frequently secrete significant amounts of transforming growth factor beta
> (TGF-β), hyaluronan (HA) and hyaluronidases to facilitate metastasizing to target organs. In a
> non-canonical signaling, TGF-β binds membrane hyaluronidase Hyal-2 for recruiting tumor
> suppressors WWOX and Smad4, and the resulting Hyal-2/WWOX/Smad4 complex is accumulated in the
> nucleus to enhance SMAD-promoter dependent transcriptional activity. Yeast two-hybrid analysis
> showed that WWOX acts as a bridge to bind both Hyal-2 and Smad4. When WWOX-expressing cells were
> stimulated with high molecular weight HA, an increased formation of endogenous Hyal-2/WWOX/Smad4
> complex occurred rapidly, followed by relocating to the nuclei in 20-40 min. In WWOX-deficient
> cells, HA failed to induce Smad2/3/4 relocation to the nucleus. To prove the signaling event, we
> designed a real time tri-molecular FRET analysis and revealed that HA induces the signaling
> pathway from ectopic Smad4 to WWOX and finally to p53, as well as from Smad4 to Hyal-2 and then
> to WWOX. An increased binding of the Smad4/Hyal-2/WWOX complex occurs with time in the nucleus
> that leads to bubbling cell death. In contrast, HA increases the binding of Smad4/WWOX/p53, which
> causes membrane blebbing but without cell death. In traumatic brain injury-induced neuronal
> death, the Hyal-2/WWOX complex was accumulated in the apoptotic nuclei of neurons in the rat
> brains in 24 hr post injury, as determined by immunoelectron microscopy. Together, HA activates
> the Hyal-2/WWOX/Smad4 signaling and causes bubbling cell death when the signaling complex is
> overexpressed."

### 0.3 No figure image was inspected

No figure panel is viewable in this environment. Per rule D-14, no negative asserted only by a
figure panel is adjudicated below. Where the surviving *legend text* makes a claim, that text is
quoted as prose and treated as an authorial statement, not as an inspection of the image.

---

## 1. Does the DisMech-quoted claim exist in the primary?

**Yes — verbatim, and it is in the ABSTRACT.** The sentence

> "In WWOX-deficient cells, HA failed to induce Smad2/3/4 relocation to the nucleus."

is the fifth sentence of the abstract (§0.2 above), word for word as DisMech carries it. The
attribution is therefore not fabricated. But the abstract is the **strongest** of the four places
where this paper states the finding, and the other three are weaker, one of them materially so.

**(a) Results, section "WWOX-negative cells are refractory to HA-induced nuclear relocation of
Smad4 and other proteins":**

> "Treatment of MDA-MB-231 with HA did not effectively induce accumulation of p53 and Smad2/3 in
> the nucleus (Figure; less than 10% for each indicated protein compared to the levels at time
> zero). Similarly, MDA-MB-435S cells were not responsive to HA-mediated nuclear translocation of
> WWOX2, p53, Smad4, and p-Smad2/3 (Figure)."

Note that for MDA-MB-231 the measured proteins named are **p53 and Smad2/3** — Smad4 is not named
for that line — and that "did not effectively induce" with a stated residual "less than 10%" is
not "failed".

**(b) Results, same section, for the knockout MEF:**

> "In stark contrast, when knockoutMEF cells were stimulated with HA, endogenous Smad4 did not
> appear to relocate into nucleus (Figuresand)."

"did not appear to relocate" — hedged, and time-unspecified.

**(c) Figure 2 legend — this contradicts the abstract:**

> "Exposure of wild typeMEF cells to HA (25 μg/ml) resulted in relocation of endogenous Smad4 into
> the nucleus in 5 min (also see). **When knockoutMEF cells were stimulated with HA, Smad4 appeared
> to relocate into nucleus in 4 hr** (also see). The extent of Smad4 nuclear localization was
> quantified (n=4; 20 cells per count)."

In the only WWOX-null genetic system in the paper, the legend states that Smad4 **did** relocate,
at 4 hr instead of 5 min. That is a ~48-fold kinetic delay, not a failure. The abstract's word
"failed" is not what the figure legend says.

**(d) Discussion:**

> "In WWOX-deficient cells, HA cannot effectively induce nuclear translocation of Smads, whereas
> Smad4 may spontaneously migrate to the nucleus."

Again "cannot effectively", plus an explicit concession of WWOX-independent, spontaneous Smad4
nuclear migration.

**Is the claim figure-only?** No — prose statements exist at (a), (b) and (d), so D-14 does not
bar adjudication of the claim's existence. But the *quantitative* content behind it (the "<10%",
the 5 min vs 4 hr kinetics, n=4/20 cells) lives in panels that were not inspected, so the
magnitude is not adjudicated here.

**Finding.** DisMech's quotation is faithful to the abstract and unfaithful to the paper. Per rule
D-15 the attribution is now verified as *existing*; it is simultaneously flagged as **quoting the
strongest sentence in the paper over a figure legend that says something weaker in the paper's own
only genetic system**.

---

## 2. What made the cells "WWOX-deficient"? Is there a rescue arm?

Four distinct manipulations, none of them equivalent, and **no re-expression (rescue) arm anywhere
in the paper**. (String check on the artefact: "rescue" occurs 3 times, all in "Ras rescue-based
yeast two-hybrid"; "re-express" occurs 0 times — the latter is an instrument-safe check because
the term is roman, but it is reported here as an extraction note, not as proof of absence.)

| System | Type | Where used | Quote |
|---|---|---|---|
| MDA-MB-231, MDA-MB-435S | naturally low/absent expressers | Fig 2A | "triple negative MDA-MB-231 and MDA-MB-435S cells express little or no wild type WWOX, but MDA-MB-435S has WWOX2 expression" |
| *Wwox*-knockout MEF (gene symbol deleted by extractor) | germline gene knockout | Fig 2B, Fig 4C | "when knockoutMEF cells were stimulated with HA, endogenous Smad4 did not appear to relocate into nucleus" |
| WWOXsi siRNA | knockdown | Fig 9C | "A plasmid construct was made in pSuppressorNeo vector for expressing siRNA to inhibit the expression of human and mouse WWOX protein"; "Ectopic WWOXsi blocked Smad4-mediated growth inhibition and apoptosis" |
| dn-WWOX (K28T/D29V) and dn-WW | ectopic dominant negative | Fig 4G, dn-WWOX section, Fig 7 | "murine dominant-negative full length WWOX (dn-WWOX) and the-terminal WW domain of WWOX (dn-WW), tagged with EGFP … The mutations were K28T and D29V" |

Consequences for inference:

- MDA-MB-435S is described in the same sentence as **expressing WWOX2**, so calling it
  "WWOX-deficient" is partial; the paper nonetheless scores WWOX2 translocation in it.
- The knockout MEF is the only true null system, is a **fibroblast**, and is used in exactly two
  figures. Its knockdown/knockout validation (WWOX protein blot of the KO line) is not described in
  the retrieved prose.
- The siRNA knockdown efficiency is not stated in prose (contrast: the Hyal-2 antisense efficiency
  *is* stated, "~70% reduction").
- A dominant negative is **not** a deficiency: dn-WWOX is an overexpressed mutant that, by the
  paper's own account, still binds Smad4 ("dn-WWOX, with alterations at K28 and D29 (K28T/D29V),
  was capable of binding Smad4"). Results obtained with it cannot be read as WWOX-null biology.
- **Necessity is asserted (knockdown + knockout) but never closed, because WWOX was never put
  back.** No arm of this paper re-expresses WWOX in a deficient background.

---

## 3. Endogenous versus ectopic — and the paper's own concession

**Endogenous readouts** (no WWOX/Hyal-2/Smad4 construct introduced): Fig 1 (nuclear/cytosolic
fractionation and IF across DU145, MCF7, NCI-H1299, 4T1-Luc and two cold-resistant variants, THP-1,
U937, Jurkat, Molt-4); Fig 2 (MDA-MB-231, MDA-MB-435S, wild-type and knockout MEF); Fig 3
(PH-20-digested HA; blebbistatin, in L929 and 4T1-Luc-c1d); Fig 4A–F and 4H (Hyal-2 expression;
co-IP of endogenous WWOX/Hyal-2/Smads in THP-1, U937, SK-N-SH, Jurkat, L929R, MCF7); Fig 6A
(agonist anti-Hyal-2 antiserum on NCI-H1299); Fig 8 (immunoelectron microscopy, HCT116); Fig 10
(rat traumatic brain injury).

**Ectopic / transfected readouts**: Fig 4G (EGFP and EGFP-dn-WW in COS7); Fig 5 (yeast two-hybrid
— a heterologous organism, and with a **truncated** Smad4: "Compared to wild type murine Smad4
(60 kDa), our truncated Smad4 (43 kDa) has a-terminal deletion from amino acid #392 to 551");
Fig 6B (Hyal-2 antisense mRNA construct in HCT116); the "dn-WWOX blocks HA-induced nuclear
accumulation of Smads" section (EGFP-dn-WWOX electroporated into COS7); Fig 7 (tri-molecular FRET,
DU145 triple-transfected with ECFP-Smad4 + EGFP-WWOX + DsRed-monomer-p53, or ECFP-Smad4 +
EGFP-Hyal-2(−sp) + DsRed-monomer-WWOX); Fig 9 (L929 electroporated with Hyal-2, WWOX and/or Smad4,
or with WWOXsi).

**Every cell-death endpoint in this paper is ectopic.** Fig 7 (bubbling cell death) requires triple
transfection, including a Hyal-2 construct engineered away from its native membrane anchor —
"EGFP-Hyal-2(−sp) is devoid of the GPI linkage and is for intracellular expression". Fig 9
(subG1/apoptosis) requires electroporated constructs at "5 μg DNA constructs … in electroporation".
Fig 10 is immunolocalisation in injured rat cortex with no intervention on the complex.

**The paper concedes this explicitly, three times.**

Title: *"… and causes bubbling cell death when the signaling complex is overexpressed."*

Discussion:

> "High molecular weight HA increases the formation of endogenous Hyal-2/WWOX/Smad4 complex
> rapidly, followed by relocating to the nuclei in 20-40 min, in WWOX-expressing normal and cancer
> cells. **No apparent cell death occurs.**"

Discussion:

> "**While native HA cannot induce cell death**, HA may activate the overly expressed
> Smad4/Hyal-2/WWOX signaling complex and causes bubbling cell death."

Dose-dependence is stated as the mechanism of the artefact, citing the authors' own prior work:

> "When the SMAD-responsive element is overly activated, cell death occurs []."

**This is as clean an authorial concession as a reader could ask for: at endogenous expression, the
pathway runs to the nucleus and nothing dies. Death is a function of construct dose.**

---

## 4. Does the pathway require WWOX, and in which direction?

**Classification: WWOX-DEPENDENT for the Smad arm and for the death endpoint; with a distinct,
smaller WWOX-INHIBITORY arm governing Hyal-2 nuclear localisation.**

*WWOX-dependent (structural necessity).* The complex has no architecture without WWOX:

> "In contrast, Hyal-2 could not bind Smad4 (Figure), indicating that WWOX connects the binding of
> Hyal-2 with Smad4."

> "In this study, we determined by yeast two-hybrid analysis that WWOX acts as a bridge to bind and
> connect both Hyal-2 and Smad4. Hyal-2 binds to the-terminal Tyr33-phosphorylated first WW domain,
> and Smad4 binds to the SDR domain."

And the bridge requires a specific WWOX residue:

> "No binding interaction was observed using a phosphorylation mutant of WW domain, WWOXww(Y33R),
> suggesting an essential role of Y33 phosphorylation in the binding."

*WWOX-dependent (functional necessity for the death endpoint).*

> "Ectopic WWOXsi blocked Smad4-mediated growth inhibition and apoptosis (Figure). In controls,
> scramble siRNA had no effect (Figure). … These observations suggest that WWOX acts synergistically
> with Smad4 in causing apoptosis."

> "Hyal-2 could not bind Smad4 (see Figure), and did not enhance the apoptotic function of Smad4"
> … "Hyal-2 enhanced WWOX-mediated apoptosis, up from 30% to 60%."

Read together: Hyal-2 potentiates death **only through WWOX**; take WWOX away and Hyal-2 adds
nothing to Smad4.

*WWOX-inhibitory sub-arm.* WWOX restrains Hyal-2:

> "Interestingly, endogenous Hyal-2 mainly localized in the nucleus of knockoutMEF cells (~60%). …
> The observations suggest that WWOX limits relocation of Hyal-2 to the nucleus."

> "Without WWOX, Hyal-2 may spontaneously accumulate in the nucleus." (Fig 6 legend)

So in a WWOX-null cell, Hyal-2 is constitutively nuclear. **The paper does not connect that state to
any death, transcriptional or phenotypic outcome in a WWOX-null cell.** It is an unresolved
observation, and is the only part of this paper that could conceivably be developed into a
WWOX-independent downstream node — but it is not developed here.

*Not classified as WWOX-INDEPENDENT-DOWNSTREAM.* Nothing in this paper identifies a step that
operates downstream of WWOX loss and can be engaged without WWOX. The Discussion in fact reports
Smad4 reaching the nucleus by a WWOX-independent route — "whereas Smad4 may spontaneously migrate
to the nucleus" — but that route is not shown to carry the death signal.

**Transferability consequence.** An intervention aimed at restoring Hyal-2/WWOX/Smad4 signalling
requires WWOX protein with an intact, phosphorylatable Tyr33 WW domain. For a genotype with no
functional WWOX protein, **this axis is not an intervention point.**

---

## 5. Direction of effect for a loss-of-function genotype

**The measured endpoint (subG1 apoptosis; bubbling cell death) gets *less*, not more, when WWOX is
scarce.** Every loss-of-WWOX manipulation in this paper *reduces* signalling toward death:
WWOXsi blocks Smad4-mediated apoptosis; dn-WWOX abolishes the FRET signalling that precedes
bubbling death ("Also, dn-WWOX abolished the singling event"); WWOX-low lines and the knockout MEF
show reduced or delayed Smad nuclear relocation.

The authors' own extrapolation is to cancer, and it is explicitly protective-loss:

> "In most cases, malignant cancer cells are either devoid of tumor suppressors WWOX, Smad4 and p53
> or possess mutations in these proteins, HA induced-signaling of Smad4/Hyal-2/WWOX and
> Smad4/WWOX/p53 for growth inhibition and death is blocked. This allows cancer cell growth
> advantage for metastasis [–]."

Their one neural extrapolation points the same way, and is speculative:

> "HA protects neurons from traumatic brain injuries [], and this could be related with HA-mediated
> disappearance of Hyal-2, which reduces the WWOX/Smad4 signaling."

**Direction for a WWOX loss-of-function genotype: this death axis is attenuated, i.e. "better" on
the endpoint as measured.** That is the opposite of what a pathophysiology node named
*"Hyal-2/WWOX/Smad4 Complex Failure"* implies if the node is meant to explain neuronal loss. The
only counterweight this paper offers is the un-followed-up observation that Hyal-2 sits in the
nucleus of WWOX-null cells (§4), and the paper's other explicit statement that Hyal-2 is itself a
damaging protein — "Hyal-2 translocates from the lysosomes to the mitochondria during
staurosporine-mediated apoptosis, suggesting that Hyal-2 participates in damaging to mitochondria
during apoptosis" — but neither is tested in a WWOX-null cell for a death outcome.

---

## 6. Neural material

Present, but thin, and **none of it is WWOX-deficient**.

- **SK-N-SH**, human neuroblastoma line (Methods: "3) human neuroblastoma SK-N-SH cells"). Used for
  Hyal-2 immunoblot and for co-immunoprecipitation of the endogenous complex: "In resting SK-N-SH
  cells, there was a cytosolic Hyal-2/WWOX/Smads complex, whereas HA reduced the level of the
  complex". WWOX-expressing; no death readout in this line.
- **Rat traumatic brain injury**, the paper's only animal work: "In a traumatic brain injury, rats
  were pierced with needles into their brains [,]. We determined that post injury for 3 and 24 hr,
  there were increased numbers of apoptotic neurons in the brain cortex. And, the complex formation
  of WWOX/Hyal-2 was increased with time and accumulated in the apoptotic nuclei of neurons."
  These are **wild-type rats** with intact WWOX; the design is correlative immunolocalisation after
  a stab injury, with no manipulation of WWOX, Hyal-2 or Smad4, no animal numbers, no ethics or
  husbandry statement in the retrieved text, and no method described for the rat tissue (the
  Methods' immunoelectron microscopy protocol is written for HCT116 cells only).
- **No primary neurons.** No neuronal culture appears anywhere. The MEFs are fibroblasts. No
  WWOX-null brain tissue, no WWOX-DEE model, no seizure endpoint. The word "seizure" occurs once,
  in the Introduction, as a cited property of *WWOX*-null humans/rats/mice, not as a measurement:
  "null mutations ofgene in humans, rats and mice result in severe neural diseases (e.g.
  microcephaly, seizure, ataxia, etc.)".

**The neural relevance of this paper to WWOX-DEE is by citation and analogy, not by measurement.**

---

## 7. Abstract-versus-results check

**There IS softening, one internal contradiction, and one methods mismatch.** This is not a clean
paper on that axis.

| # | Abstract assertion | Body | Verdict |
|---|---|---|---|
| A1 | "Yeast two-hybrid analysis showed that WWOX acts as a bridge to bind both Hyal-2 and Smad4." | Fig 5 Y2H; "Hyal-2 could not bind Smad4 …, indicating that WWOX connects the binding of Hyal-2 with Smad4"; corroborated by co-IP | **Matched.** (Caveat stated in body, not abstract: the Smad4 used was truncated, 43 kDa, Δaa 392–551.) |
| A2 | "an increased formation of endogenous Hyal-2/WWOX/Smad4 complex occurred rapidly, followed by relocating to the nuclei in 20-40 min" | In several systems the *measurement* is a **decrease** in cytosolic complex, with nuclear relocation **inferred**: "HA (25 μg/ml) reduced the cytosolic Hyal-2/WWOX/Smads complex in SK-N-SH cells in 30 min"; "The reduction is due to relocation of Hyal-2 to the nucleus"; "HA reduced the complex formation of Hyal-2/WWOX/Smad4 in EGFP-expressing COS7 cells". In THP-1 the complex increased but stayed put: "the complex remained in the cytosol and no apparent translocation to the nucleus was shown". Fig 4's own title is "HA increases the complex formation of Hyal-2, WWOX and Smads, **followed by reduction**". | **Softened / inferential.** The abstract states as a two-step observation what is in part a one-step observation plus an interpretation, and omits the cell line in which step two did not happen. |
| A3 | **"In WWOX-deficient cells, HA failed to induce Smad2/3/4 relocation to the nucleus."** | Results: "did not effectively induce … less than 10%"; "did not appear to relocate". Fig 2 legend: "Smad4 appeared to relocate into nucleus in 4 hr". Discussion: "cannot effectively induce … whereas Smad4 may spontaneously migrate to the nucleus." | **Strengthened to the point of internal contradiction.** The paper's only null genetic system shows delayed relocation; the abstract calls it failure. This is the DisMech evidence item. |
| A4 | "An increased binding of the Smad4/Hyal-2/WWOX complex occurs with time in the nucleus that leads to bubbling cell death." | True only for triple-transfected DU145 with GPI-less Hyal-2; the Discussion states the endogenous complex kills nothing. | **Qualified elsewhere, and the abstract does qualify it** in its own final sentence ("when the signaling complex is overexpressed"). Honest, if read to the end. |
| A5 | "In traumatic brain injury-induced neuronal death, the Hyal-2/WWOX complex was accumulated in the apoptotic nuclei of neurons in the rat brains in 24 hr post injury, **as determined by immunoelectron microscopy**." | Results report "post injury for 3 and 24 hr" and state no method; Methods describe immunoelectron microscopy **for HCT116 cells only** ("Briefly, HCT116 cells were fixed for 1 hour…"), with no rat-brain protocol. | **Method mismatch.** The abstract attributes a technique to an experiment whose Methods are not in the paper as retrieved. Reported as an extraction-limited observation — the supplementary material was not returned — but the main-text Methods do not cover it. |

**Two further body-level overstatements, in the Introduction rather than the abstract:**

> "The Smad/Hyal-2/WWOX complex relocated to the nucleus to induce cell death."

stated with no overexpression qualifier, flatly contradicted by the Discussion's "No apparent cell
death occurs"; and

> "the signaling revealed a critical role of nuclear Hyal-2 and WWOX in causing apoptosis under
> stress conditions"

for the TBI experiment, where nothing was manipulated and therefore no causal role was tested.

**Statistical reporting.** No statistical test, no P value, no error term and no significance
statement appears anywhere in the retrieved text. The quantitative statements are percentage ranges
("~100-300% increased", "less than 10%", "~60%", "up from 30% to 60%", "~70% reduction") with
replication described as: "All experiments in this study were repeated 2-5 times"; "representative
data from 2 experiments" (twice); "All data are average from two experiments". The single stated n
is "(n=4; 20 cells per count)" in Fig 2B. **String checks on the artefact for "P <", "p <", "SEM",
"Student", "ANOVA" all return zero; these terms are roman and would not be deleted by the observed
italic-stripping defect, but the finding is recorded as an extraction-limited note, not as a proof
of absence, because tables and supplementary material were not returned.**

---

## 8. C1q

**The paper is silent on C1q.** The string "C1q" does not occur anywhere in the retrieved text.
"C1q" is roman in this journal and would not be removed by the observed italic-stripping defect —
but the reference list was not returned, so this is recorded as *no prose mention in the retrieved
main text*, which is the strongest statement the instrument supports.

The one place where the question would have been answered is the Introduction's inventory of
Hyal-2 ligands, which names TGF-β, CD44 and Zfra and stops there:

> "Recently, membrane Hyal-2 is shown to bind a 31-amino-acid peptide Zfra (zinc finger-like protein
> that regulates apoptosis) for leading to the activation of spleen Hyal-2CD3CD19Z cell in memory
> anticancer response []."

**The open question from PMID 19484134 — "Hyal-2 could be the potential link for C1q/WOX1 signaling.
Binding of Hyal-2 with C1q remains to be determined." — is NOT closed by this paper.** Eight years
later, the same group does not mention it.

---

## 9. Editorial venue

*Oncotarget*, volume 8, 2017. This is recorded as a **weight on the reading, not a refutation**, and
it is not asked to do argumentative work on its own. What actually carries weight here is internal
and quoted above: no statistical test anywhere; n = 2 for several key panels; heavy reliance on
"data not shown" (at least eleven instances in the retrieved text); a rat experiment with no
Methods, no animal numbers and no ethics statement; and a pattern of asserting nuclear relocation
from a fall in cytosolic signal. The venue is consistent with that profile; the profile does not
need the venue to be visible.

(*Oncotarget*'s indexing status was contested in this period and its MEDLINE/Web of Science
coverage changed around 2017–2018. That is stated from general knowledge and was **not** verified
against a source in this session; it is noted only so a later reader can check it, and no argument
above rests on it.)

---

## 10. What LEGEND may and may not infer

### May infer (with the stated evidence class)

1. **WWOX physically bridges Hyal-2 and Smad4, and Hyal-2 and Smad4 do not bind each other.**
   Yeast two-hybrid plus co-IP, internally consistent, stated in Results and Discussion. Caveat:
   truncated Smad4 (43 kDa, Δ392–551) in the Y2H; heterologous organism.
2. **The Hyal-2–WWOX interaction requires WWOX Tyr33 in the first WW domain**; WWOXww(Y33R)
   abolishes binding to both partners. This is a structural datum about the WWOX protein and is
   mechanistically relevant to any WWOX allele that perturbs the first WW domain.
3. **WWOX restrains Hyal-2 nuclear localisation**: ~60% of endogenous Hyal-2 is nuclear in
   knockout MEF at baseline. This is the single observation in the paper that describes the
   *WWOX-null state* rather than the WWOX-sufficient state, and it is **not followed up**.
4. **At endogenous expression this pathway does not kill cells.** The authors say so twice.
5. **The Hyal-2/WWOX complex accumulates in apoptotic cortical neuronal nuclei after stab injury in
   wild-type rats** — as a correlation, in animals with normal WWOX.

### May NOT infer

1. **May not infer that failure of the Hyal-2/WWOX/Smad4 complex causes neuronal death in a
   WWOX-null genotype.** No experiment in this paper measures death in a WWOX-deficient cell. Every
   WWOX-removal manipulation here *reduces* the death readout. The direction implied by the DisMech
   node is not the direction this paper measures.
2. **May not infer any therapeutic intervention point from this paper for a genotype lacking
   functional WWOX protein.** The pathway is WWOX-dependent and Tyr33-dependent; there is no
   WWOX-independent downstream step identified.
3. **May not carry "bubbling cell death" into the disease model as a WWOX-DEE mechanism.** It is
   produced by triple transfection, one component of which (Hyal-2 without its GPI anchor) does not
   exist in that form in a cell.
4. **May not treat the WWOX-deficiency result as a rescued, necessity-grade result.** There is no
   re-expression arm.
5. **May not adjudicate the magnitude of the WWOX-deficient Smad relocation defect.** The numbers
   live in panels that were not inspected (D-14), and the two prose statements about them — Results
   text and Figure 2 legend — disagree.
6. **May not use this paper to close the C1q/Hyal-2 question** left open by PMID 19484134.

### Is the DisMech evidence item faithfully sourced?

**Partially.** The quotation is verbatim and the PMID is correct, so the attribution is real —
rule D-15 is satisfied as to existence. But it is quoted **from the abstract**, and the same paper's
Figure 2 legend reports that in its only WWOX-null system Smad4 *did* relocate, at 4 hr. A node
built on that single sentence inherits the abstract's overstatement and none of the paper's own
qualifications, and the node's name ("Complex Failure" as a driver of pathology) runs opposite to
the paper's measured direction of effect. **Recommendation: the DisMech node should not be imported
as a WWOX-DEE pathophysiology driver on this evidence. If anything from this paper is to be carried
forward, it is item (3) above — constitutive nuclear Hyal-2 in the WWOX-null state — which is an
open question, not a mechanism.**

---

Author: **Scientist B** · Date: **2026-09-21** · **READ-ONLY** — no canonical LEGEND file was
modified; no registry, queue, ledger or current file was touched; no commit candidate was produced;
no git command was run. Two files written this session: the verbatim full-text artefact
`files/fulltext/PMID27845895_PMC_MCPtext.txt` and this audit.

**Declared limits.** No figure image was inspected — no negative asserted only by a figure panel is
adjudicated here (D-14). **Extraction defect: PRESENT** — the MCP surface deleted all italicised
tokens (the italic gene symbol *WWOX*/*Wwox*, *in vitro*/*in vivo*), emptied every figure
cross-reference, and dropped the reference list, tables, GenBank accessions and supplementary
material; the abstract arrived as a separate field and is reproduced in §0.2. The roman protein
symbol "WWOX" survived (248 occurrences), so the surviving prose is readable, but **no zero string
count in this document is evidence about the paper** — only about the extraction.
