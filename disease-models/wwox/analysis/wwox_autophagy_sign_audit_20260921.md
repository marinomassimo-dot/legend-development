# WWOX / autophagy sign audit — PMID 24008736

**Target.** PMID 24008736 · PMCID PMC3789168 · DOI 10.1038/cddis.2013.308 · *Cell Death Dis* 2013;4(9):e792.
Tsai C-W, Lai FJ, Sheu HM, Lin YS, Chang TH, Jan MS, Chen SM, Hsu PC, Huang TT, Huang TC, Sheen MC, Chen ST, Chang WC, Chang NS, Hsu LJ.
Identifiers verified against `mcp__PubMed__get_article_metadata` on 2026-09-21; all four (PMID, PMCID, DOI, PII `cddis2013308`) match the task brief exactly.

**Source artefact.** `files/fulltext/PMID24008736_PMC_MCPtext.txt` — 32 855 bytes,
`sha256 ccfcb113bece0d4c795cc09c7f64f8a85569aa5c8f39b4abb6f8465042c83031`.
Verbatim MCP body text, no abstract, no truncation. Every quotation below is from that file
unless explicitly marked `[ABSTRACT]`, in which case it is from the PubMed metadata record.

---

## VERDICT

**FIXES A SIGN — WWOX ⊣ autophagy — AND ONE ARM REACHES OUTSIDE THE ONCOLOGY STRESS CONTEXT, BUT THAT ARM IS A SINGLE UNCLAMPED STEADY-STATE LC3-II WESTERN.**
The direction is consistent across four independent arms, and one of them — *Wwox*-knockout mouse
embryonic fibroblasts, no drug, no tumour — is a germline loss-of-function observation that a
WWOX-DEE genotype class could in principle inherit. That arm is real and it is the reason this
reading changes something. It is also one blot, on one readout, with no lysosomal clamp, reported
in a single sentence whose genotype labels the extractor deleted, and it is not neural.

---

## 1 · Actual title and claim, versus the registry gloss

**Title, verbatim:** *"WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated human squamous cell carcinoma"*.

The registry stub `CORPUS-STUB-139` glosses this as *"WWOX suppresses autophagy"*. Under rule D-15
the stub is a secondary source and had to be checked. **It checks out as far as it goes, and it is
incomplete in a way that matters.** The gloss reproduces the first five words of the title and drops
the operative scoping clause — *"for inducing apoptosis in methotrexate-treated human squamous cell
carcinoma"*. The registry therefore recorded a direction without recording that the paper's own
title binds that direction to a drug, a cancer, and an apoptotic endpoint.

The paper's own summary sentence, Discussion, first paragraph, carries the same scope explicitly:

> "Thus, WWOX suppresses autophagy for inducing apoptosis in MTX-treated human SCC."

And the paper's own therapeutic reading of its result, immediately after, is purely oncological:

> "A clear strategy in cancer targeting is boosting WWOX for suppression of autophagy in treating cancers."

The gloss is not wrong. It is a title fragment, and it silently promoted a scoped claim to an
unscoped one. That promotion is the thing this audit had to catch.

---

## 2 · The sign, stated precisely

The sign is **suppression**: WWOX reduces autophagy. It is directional, not "modulate-without-
direction", and it is stated directionally in the Results, not only in the abstract.

**Results, section "WWOX suppresses autophagy in SCC cells":**

> "Our results showed that ectopic overexpression of WWOX dramatically decreased the lipidated LC3-II protein expression in MTX-treated SCC-9 cells ()."

> "We detected significantly reduced amount of Atg12–Atg5 conjugate in the SCC-9 cells overexpressing WWOX, and MTX treatment further downregulated the expression level of Atg12–Atg5 conjugate in these cells ()."

> "Our results showed that ectopic overexpression of WWOX suppressed protein expression of Beclin-1 in both SCC-9 and SCC-15 cells ()."

**Abstract statement [ABSTRACT]:**

> "Thus, WWOX renders SCC cells susceptible to MTX-induced apoptosis by dampening autophagy, and the failure in inducing WWOX expression leads to chemotherapeutic drug resistance."

**One important asymmetry between the two.** The *closing* sentence of that same Results section is
direction-neutral:

> "Together, our results clearly demonstrate a role of WWOX in the regulation of autophagy in SCC cells."

"A role in the regulation" is weaker than "suppresses". The directional sentences are the individual
experimental ones; the section's own summary retreats to non-directional language. The title and the
abstract do not retreat. This is a small softening inside the Results that the abstract does not
reproduce — see § 9.

**Sign of the mTOR limb, separately:** WWOX *raises* mTORC1 activity, which is consistent with
suppressing autophagy.

> "Ectopic overexpression of WWOX in SCC-15 cells significantly augmented MTX-induced phosphorylation of mTOR and p70S6K, as compared with the GFP-transfected control cells (). Conversely, siRNA-mediated knockdown of WWOX suppressed MTX-stimulated activation of the mTOR/p70S6K signaling pathway in SCC-15 cells ()."

---

## 3 · How the sign was established — necessity versus sufficiency

Four arms carry the sign. Two are sufficiency, two are necessity. Enumerated:

### Sufficiency arms (gain of function) — do NOT transfer to a loss-of-function genotype

| Arm | System | Readout | Direction supported |
|---|---|---|---|
| S1. Transient WWOX cDNA overexpression | SCC-9 (WWOX-low, MTX-resistant), + MTX | LC3-II ↓ | WWOX ⊣ autophagy |
| S2. Transient WWOX cDNA overexpression | SCC-9 and SCC-15 | Beclin-1 ↓; Atg12–Atg5 ↓ (SCC-9) | WWOX ⊣ autophagy |

S2 is worth isolating: the Beclin-1 sentence carries **no MTX qualifier** — "in both SCC-9 and
SCC-15 cells" — so on the paper's own wording this is a basal, drug-independent effect of WWOX
excess on an autophagy initiation protein. It is still overexpression.

### Necessity arms (loss of function) — these are the ones that could transfer

| Arm | System | Readout | Direction supported |
|---|---|---|---|
| N1. Lentiviral shRNA knockdown of WWOX | SCC-15, + MTX | rescue of LC3-II | WWOX required for the MTX-driven autophagy suppression |
| N2. Germline *Wwox*-knockout MEFs | mouse embryonic fibroblasts, **no drug, no tumour** | LC3-II ↑ | WWOX ⊣ autophagy, basally |

**N1, verbatim:**

> "Lentiviral small hairpin RNA (shRNA)-mediated knockdown of WWOX expression partially prevented MTX-induced reduction of LC3-II in SCC-15 cells ()."

Note "**partially** prevented". N1 is a partial rescue inside MTX stress, and the knockdown construct
is characterised elsewhere in the paper as sub-total: *"This WWOXsi-expressing construct has been
demonstrated to suppress WWOX protein expression by >50% compared with the control scrambled siRNA."*
(Materials and Methods, "Expression constructs, siRNA, lentiviral shRNA and gene transfection"). A
>50% knockdown giving a partial rescue is internally coherent but is not a clean necessity
demonstration.

**N2, verbatim — the load-bearing sentence of this entire audit:**

> "In our recently developedgene knockout mouse embryonic fibroblasts, increased expression of LC3-II protein was detected in the cytosolic protein extracts from theandcells using western blotting, as compared with thecontrol cells ()."

The word-joins ("developedgene", "from theandcells", "with thecontrol cells") are the extractor's
italic deletions: the surviving skeleton is *"our recently developed **Wwox** gene knockout mouse
embryonic fibroblasts … from the **[genotype]** and **[genotype]** cells … compared with the
**[genotype]** control cells"*. **I cannot read the genotype labels on this surface.** The sentence
is unambiguous that it compares knockout-derived MEFs against control MEFs and that LC3-II is higher
in the knockout; it is not readable here whether the two knockout arms are *Wwox*⁻/⁻ and *Wwox*⁺/⁻,
or two independent lines. That distinction matters for a heterozygous carrier and is **not
adjudicable from this artefact**.

### What this enumeration means for transfer

A WWOX-DEE genotype is a loss-of-function state. S1 and S2 are therefore irrelevant to it:
overexpression establishes that excess WWOX can push autophagy down, not that scarce WWOX lets it
rise. N1 is loss of function but only inside MTX stress in a cancer line. **N2 is the only arm that
is simultaneously loss-of-function, germline, drug-free and non-transformed.** The paper's transfer
value to this repository rests on one sentence.

---

## 4 · Autophagy readouts, and whether FLUX was measured

Readouts actually used, by name:

1. **Steady-state LC3-II western blot** — SCC-9, SCC-15, and the knockout MEFs.
2. **Beclin-1 and Atg12–Atg5 conjugate protein levels** — western blot. These are pathway-component
   abundances, not flux.
3. **GFP-LC3 puncta by fluorescence microscopy** — *"The amounts of GFP-LC3 puncta were markedly
   reduced in MTX-treated SCC-15 cells, as compared with the untreated SCC-15 cells ()."*
4. **Transmission electron microscopy of autophagosomes** — *"Our data clearly demonstrated that the
   cytoplasmic autophagosomes disappeared upon treatment of SCC-15 cells with MTX ()."*
5. **A lysosomal-protease clamp, in one arm only** — E64d plus pepstatin A.

**p62/SQSTM1: zero occurrences.** p62, SQSTM1, bafilomycin, chloroquine and mCherry-GFP-LC3 return
zero string counts. These are **roman-type method words, not italicised tokens**, so under the
instrument warning these zeros *are* informative: this paper did not use p62, did not use
bafilomycin or chloroquine, and did not use a tandem mCherry-GFP-LC3 reporter.

**Was flux measured? Partially, in one direction, in one arm, and not in the arm that matters.**

The authors did run a lysosomal clamp, and they ran it for exactly the reason a careful reader would
demand. Verbatim, Results, section "MTX modulates autophagy in SCC cells":

> "To exclude the possibility that the decrease in LC3 protein expression in MTX-treated SCC-15 cells could be due to increased autophagic flux,we used protease inhibitors E64d and pepstatin A to inhibit lysosomal enzymes in the autophagic vacuoles. Our data revealed that MTX treatment decreased LC3-II protein expression in SCC-15 cells at 12 h, and the presence of E64d and pepstatin A did not prevent MTX-induced downregulation of LC3 protein expression (), suggesting that the reduction of LC3 protein levels in MTX-treated SCC-15 cells is not caused by rapid lysosomal turnover."

This is a genuine and correctly-reasoned flux control. It rules out the specific confound that
falling LC3-II reflects accelerated degradation rather than reduced autophagosome formation, and the
GFP-LC3 puncta and TEM autophagosome counts independently corroborate the same direction with
morphology rather than protein abundance. On the **MTX-in-SCC-15** arm, the sign is about as well
supported as a 2013 autophagy paper gets.

**But the clamp was applied to the MTX arm, not to the WWOX arms.** There is no E64d/pepstatin A
condition reported for the WWOX-overexpression experiments, and none for the *Wwox*-knockout MEFs.
The knockout-MEF result is therefore a **bare steady-state LC3-II comparison with no flux clamp** —
exactly the measurement that cannot by itself distinguish "knockout cells make more autophagosomes"
from "knockout cells clear autophagosomes more slowly". Both readings are consistent with elevated
LC3-II in *Wwox*-null MEFs, and they carry opposite functional meaning.

There is a further complication the authors themselves surface, and it cuts against reading LC3-II
level as an autophagy level at all in this system:

> "Treatment of SCC-15 cells with a proteasome inhibitor MG132 blocked MTX-induced LC3 protein downregulation, indicating that LC3 protein is degraded via the ubiquitin/proteasomal pathway post MTX treatment ()."

Restated in the Discussion: *"the reduction of LC3 protein via a proteasomal degradation pathway was
associated with the presence of WWOX."* So in the MTX/SCC-15 arm the LC3-II drop is substantially a
**proteasomal destruction of the LC3 protein itself**, not a readout of autophagic activity. The
morphological readouts (puncta, TEM) are what actually carry the autophagy claim there. In the
knockout MEFs there are no morphological readouts — only the LC3-II blot, in the system where the
paper has just shown LC3 abundance to be proteasomally controlled.

---

## 5 · Is mTOR measured, or inferred?

**Measured, directly, by phospho-western — and the link from mTOR to autophagy is inferred.**

Measured, Results, section "MTX treatment modulates mTOR signaling in SCC cells via WWOX":

> "we examined protein phosphorylation of mTOR and its downstream effector p70 S6 kinase (p70S6K) at Ser2448 and Thr389, respectively. Our data showed that MTX stimulated protein phosphorylation of mTOR and p70S6K in SCC-15 cells after 24 h of treatment, whereas mTOR phosphorylation was downregulated in SCC-9 cells following MTX treatment ()."

Physical interaction is also measured, twice:

> "Interestingly, we detected colocalization of WWOX with mTOR in SCC-15 cells by confocal microscopy (). Co-immunoprecipitation analysis further confirmed their interaction in SCC-15 cells (and)."

**4E-BP1: zero occurrences** (roman-type, informative zero) — the second canonical mTORC1 substrate
was not assayed. p70S6K Thr389 is the only downstream substrate measured.

**What is inferred, and stated as inferred by the authors themselves.** The claim that mTOR is the
route from WWOX to autophagy is a hypothesis in the Results, not a result:

> "Together, we determined that MTX stimulated mTOR/p70S6K signaling in SCC-15 cells via WWOX, raising the possibility that WWOX may regulate autophagy through mTOR activation in MTX-treated SCC-15 cells."

And in the Discussion, one step further removed:

> "It is possible that WWOX indirectly affects ULK complex via modulating mTORC1 activation."

**There is no epistasis test.** "rapamycin" occurs once in the artefact, and only as the expansion of
the acronym ("mammalian target of rapamycin"); there is no rapamycin or Torin arm, no
constitutively-active or kinase-dead mTOR arm, no ULK1 phospho-site blot (Atg13, FIP200, Atg101 and
ULK appear only in a Discussion sentence about the literature). **The WWOX→mTOR limb and the
WWOX→autophagy limb are each measured; the arrow between them is asserted, not tested.** A
repository citing this paper for "WWOX acts on autophagy *through* mTOR" would be overreading it.

The authors also flag their own mTOR signal as transient and of unknown significance:

> "We detected a transient increase in the phosphorylation of mTOR and p70S6K in MTX-treated SCC-15 cells. It is unclear if the duration of mTORC1 signaling may determine distinct cellular effects in SCC cells."

---

## 6 · Cellular context, and the paper's own scoping

**Context:** three human tongue-biopsy-derived squamous cell carcinoma lines — SCC-4, SCC-9, SCC-15
(*"SCC-4, -9 and -15 cells derived from human tongue biopsieswere kind gifts from Dr. Dar-Bin
Shieh"*, Materials and Methods) — under methotrexate, plus a 5-fluorouracil confirmation arm, plus
human tumour biopsies from patients given continuous intra-arterial MTX, plus the *Wwox*-knockout
MEFs.

**The paper scopes itself, repeatedly and explicitly, to that stress.** Its own scoping language,
verbatim:

> "Thus, WWOX suppresses autophagy for inducing apoptosis in MTX-treated human SCC." *(Discussion)*

> "We show here that WWOX downregulated the expression levels of Atg12–Atg5 and Beclin-1 and suppressed autophagy in MTX-treated SCC cells." *(Discussion)*

> "Together, we determined that, following MTX treatment, autophagy was suppressed in MTX-sensitive SCC-15 and SCC-4 cells, but not in MTX-resistant SCC-9 cells, suggesting that inhibition of autophagy may sensitize SCC cancer cells to chemotherapeutic drugs." *(Results)*

The section heading is "**WWOX suppresses autophagy in SCC cells**" — scoped to SCC in the heading
itself.

**Is the sign context-dependent on the paper's own showing?** The *autophagy* sign is not reported as
flipping between contexts: WWOX excess lowers autophagy proteins in the MTX-resistant line and the
MTX-sensitive line alike, and WWOX loss raises LC3-II in drug-free MEFs. What *is* strongly
context-dependent is the **mTOR** limb, and the authors say so: MTX raises mTOR phosphorylation in
SCC-15 but *lowers* it in SCC-9 (*"whereas mTOR phosphorylation was downregulated in SCC-9 cells
following MTX treatment"*). That divergence tracks WWOX abundance in the authors' reading, but it
means the mTOR response to a stressor is not a fixed quantity even between two lines of the same
tumour type.

The authors also concede their mechanism is unexplained:

> "The molecular mechanisms underlying downregulation of essential proteins for autophagy by WWOX in SCC cells are largely unclear."

> "The molecular mechanism by which WWOX regulates mTORC1 signaling in SCC cells is currently under investigation."

A mechanism the authors call "largely unclear" is a weak basis for asserting that the mechanism
operates identically in post-mitotic neurons.

---

## 7 · Non-cancer, neural or developmental material

**Neural: none. Developmental: one arm, and only in the embryological sense of the cell type.**

Roman-type string counts on the artefact: "neuron" 0, "neural" 0, "brain" 0, "epilep" 0. These are
not italicised tokens, so these zeros are **informative negatives**: the paper contains no neural,
neuronal, brain or epilepsy material at all. The MeSH terms returned by PubMed corroborate —
Apoptosis, Autophagy, Carcinoma Squamous Cell, Cell Line Tumor, Methotrexate, Tongue Neoplasms,
TOR Serine-Threonine Kinases — no nervous-system descriptor.

**The one non-cancer datum is the MEF arm**, quoted in full at § 3 (N2). Mouse embryonic fibroblasts
from a *Wwox* germline knockout are primary, non-transformed, untreated cells. They are
"developmental" only in that they are embryo-derived; the paper reports no developmental phenotype,
no differentiation assay, no timecourse, and no neural derivative. Beyond that single sentence, the
paper is cancer-framed throughout — background, rationale, every other experiment, the entire
Discussion, and the therapeutic conclusion.

**What this means for how this repository may cite this paper.** It may be cited for: (a) a physical
WWOX–mTOR interaction, demonstrated by colocalisation and co-IP in a human cell line; (b) the
direction WWOX ⊣ autophagy-protein abundance, established chiefly by gain of function in cancer
lines under drug; (c) **one germline loss-of-function observation, in non-neural primary mouse
cells, that LC3-II rises when WWOX is absent.** It may **not** be cited as evidence about neurons, about
brain development, about seizure biology, or about what autophagy does to a WWOX-deficient neuron's
survival — the paper contains no observation of any of those. Citing (c) requires carrying its
limits with it: one blot, no flux clamp, genotype labels unreadable on this surface, fibroblasts.

---

## 8 · Direction for a loss-of-function genotype

**With WWOX scarce, this axis moves toward MORE autophagy.** Three lines of the paper's own evidence
point the same way, only one of which is a genetic loss-of-function:

1. *Wwox*-knockout MEFs: *"increased expression of LC3-II protein was detected"* versus control.
2. WWOX-low SCC-9 has high constitutive autophagy: *"Our data indicated that the basal autophagy is
   active in SCC-9 cells, as evidenced by the presence of numerous autophagosomes in the cytoplasm
   and a high level of LC3-II protein expression."* (Discussion) — This is a correlational
   comparison between two unrelated tumour lines, not a controlled manipulation.
3. WWOX knockdown rescues LC3-II in SCC-15 under MTX (N1, partial).

**Is that good or bad on the paper's own measured endpoint?** On the paper's endpoint it is
unambiguously **survival-promoting**, which in an oncology frame the authors call bad:

> "These results suggest that SCC-9 cells may utilize the autophagic pathway as a survival mechanism to evade the perturbations of cellular biosynthetic processes by the antimetabolite MTX and sustain cell viability upon metabolic stress."

> "Recent studies have suggested that autophagy has important roles in chemoresistance of cancer cells to some antimetabolic agents.Accumulating evidence has demonstrated that inhibition of autophagy increases the susceptibility of cancer cells to cytotoxic chemotherapy." *(Introduction)*

**This is the inversion that a careless citation would produce, and it must be stated plainly.** The
paper's measured endpoint is *cancer-cell death*. High autophagy in a WWOX-low cell keeps that cell
alive. The authors label that outcome undesirable **because they want the cell to die.** In a
WWOX-DEE genotype class, the cells in question are neurons, and the desired outcome is the opposite
one. The valence attached to "more autophagy" in this paper is therapeutic-context valence, not
biology, and it **does not transfer**. The paper measures nothing about whether elevated autophagy in
a WWOX-scarce non-cancer cell is protective, neutral or harmful — it measures only that it obstructs
methotrexate.

**Do the authors extrapolate?** Only into oncology, never out of it. Their single extrapolative
sentence is: *"A clear strategy in cancer targeting is boosting WWOX for suppression of autophagy in
treating cancers."* Read literally as a general principle, it would prescribe *raising* WWOX to
*lower* autophagy — which is the WWOX-restoration direction a WWOX-DEE therapeutic program already
wants for unrelated reasons, and it says nothing about whether the autophagy consequence would be
wanted. **No author extrapolation to a constitutional loss-of-function genotype exists in this paper.**

---

## 9 · Abstract-versus-Results check

**There is not "none". Three discrepancies, all in the direction of the abstract overstating, plus
one omission that runs the other way.**

**9a · "blocked" versus "partially prevented" — a strengthening.**
Abstract [ABSTRACT]: *"When WWOX was knocked down in SCC-15, MTX-induced mTOR signaling and autophagy
inhibition were **blocked**."*
Results: *"Lentiviral small hairpin RNA (shRNA)-mediated knockdown of WWOX expression **partially
prevented** MTX-induced reduction of LC3-II in SCC-15 cells ()."*
"Blocked" asserts abolition; the Results report partial rescue with a knockdown characterised as
>50%. This is the single clearest abstract-over-Results step in the paper, and it sits on the
necessity arm — the arm that carries the most weight for transfer.

**9b · "cure of SCC in MTX therapy" — a strengthening on the clinical claim.**
Abstract [ABSTRACT]: *"WWOX … regulates the susceptibility of SCC to methotrexate (MTX) in vitro and
**cure** of SCC in MTX therapy."*
What the Results actually contain is immunohistochemistry on biopsies: *"MTX treatment upregulated
WWOX protein expression along with caspase-3 activation and apoptotic cell death (terminal
deoxynucleotidyl transferase dUTP nick-end labeling (TUNEL)-positive staining) in the SCC tumor
biopsies ()."* The cure itself is attributed to **prior** work, not to this study: *"Previous studies
showed that continuous intra-arterial infusion of MTX leads to complete cure of the disease."* The
abstract's grammar allows a reader to attribute the cure finding to this paper. No survival data, no
response-rate data, no patient number, no control arm appears anywhere in the body text.

**9c · Mechanism asserted in the abstract, hedged in the Results — a strengthening.**
Abstract [ABSTRACT]: *"**Mechanistically**, WWOX physically interacted with mammalian target of
rapamycin (mTOR), which potentiated MTX-increased phosphorylation of mTOR and its downstream
substrate p70 S6 kinase, along with dramatic downregulation of the aforementioned proteins in
autophagy, in SCC-15."*
Results: *"…**raising the possibility** that WWOX may regulate autophagy through mTOR activation in
MTX-treated SCC-15 cells."*
Discussion: *"**It is possible** that WWOX indirectly affects ULK complex via modulating mTORC1
activation."*
The word "Mechanistically", and the "along with" that yokes the mTOR phosphorylation to the autophagy
protein downregulation in a single clause, present as established a causal chain the body text twice
marks as a possibility. No epistasis experiment exists (§ 5).

**9d · Omission running the other way — the abstract is SILENT on the knockout MEFs.**
The *Wwox*-knockout MEF LC3-II result appears in the Results and **nowhere in the abstract**. It is
the paper's only genetic, drug-free, non-cancer loss-of-function observation, and therefore the
single most transferable datum in it — and an abstract-only reader would never see it. This is not
an overstatement; it is the opposite error, and it is the reason the stub `CORPUS-STUB-139` could not
have been corrected by reading the abstract. **Only the full text surfaces the arm that changes this
repository's standing conclusion.**

**No inversion was found.** Nothing in the Results points the opposite way from the abstract.

---

## 10 · Does the standing negative conclusion survive?

The standing conclusion under audit: *"the direction of the WWOX/autophagy axis is not fixed anywhere
in this corpus."*

**It does not survive as stated. It must narrow, and the narrowing is substantive.**

This paper fixes a direction, and it does so on a readable surface: WWOX ⊣ autophagy. It fixes it
four times over, in two cell lines by gain of function, once by knockdown under drug, and — decisively
for this repository — **once by germline knockout in drug-free, non-transformed mouse embryonic
fibroblasts, where WWOX absence raises LC3-II.** That last arm is not an oncology observation. It is
a loss-of-function observation in primary cells, and a WWOX-DEE genotype class is a loss-of-function
state. The claim that *no member of the corpus* fixes a direction is now false, and any reasoning
file that rests on it is resting on a premise this reading removed.

**On what narrowed grounds a negative still stands.** Three, and they are not evasions:

1. **The direction is not fixed on FLUX.** No arm in this paper clamps lysosomal degradation while
   manipulating WWOX. The one lysosomal clamp (E64d/pepstatin A) was applied to the MTX arm, not to
   any WWOX arm, and in that same system the authors show LC3 protein is proteasomally destroyed —
   so LC3-II abundance is not a clean proxy for autophagic activity here. "LC3-II rises when WWOX is
   lost" is compatible with more autophagosome formation *and* with slower autophagosome clearance.
   Those are opposite sign for cell fate. **The direction of the axis is fixed on steady-state
   autophagy-protein abundance; it is not fixed on flux.**
2. **The direction is not fixed in neural tissue.** The paper contains zero neural, neuronal, brain
   or epilepsy content (informative roman-type zeros, § 7). MEFs are not neurons, and autophagy
   regulation in a proliferating fibroblast and in a post-mitotic neuron are not interchangeable.
   **The direction of the axis is fixed in fibroblasts and carcinoma lines; it is not fixed in a
   neural or developmental context.**
3. **The mTOR route is not fixed at all.** The WWOX–mTOR interaction is measured and the
   WWOX→autophagy relation is measured, but no experiment connects them. The authors say so twice.
   **Any standing negative about the *mTOR-mediated* direction survives intact and untouched.**

**Recommended restatement of the standing conclusion:**

> The direction of the WWOX→autophagy axis **is** fixed in this corpus as suppressive — WWOX excess
> lowers, and WWOX loss raises, steady-state autophagy-protein abundance — on the evidence of
> PMID 24008736, including one germline loss-of-function arm in non-transformed cells. That
> direction is **not** established on autophagic flux, is **not** established in neural or
> developmental tissue, and the **mTOR-mediated** route between WWOX and autophagy remains asserted
> rather than tested anywhere in this corpus. The three remaining unread stubs (31966718, 33300063,
> 36621327 — all verified closed here) cannot narrow or widen this until obtained.

**Consequence for the two reasoning files.** Their negative argument rested on four stubs
"catalogued in two opposite directions". One of the four is now read, and it does not merely fail to
cancel out — it supplies a loss-of-function arm. The argument as built (a standoff between unread
glosses) is no longer available and should be rewritten to the narrowed form above. Note also that
`PMID 33300063`, glossed in the same suppressive direction as this one, is now the *concordant*
unread member; the sole discordant gloss is `PMID 36621327` (WWOX activating autophagy), and the
whole remaining tension in this corpus reduces to that one closed paper. **That is a sharper and more
actionable statement of the gap than the symmetric standoff it replaces, and it raises the
acquisition priority of 36621327 specifically above the other two.**

---

## Declared limits and attestation

- **Author:** Scientist A. **Date:** 2026-09-21.
- **READ-ONLY.** No canonical LEGEND file was modified. No registry, queue, ledger or current file
  was touched. No git operation was performed. No commit candidate was produced. Exactly two files
  were written: the verbatim artefact and this analysis.
- **No figure was inspected.** No figure image is available on this surface. Per rule **D-14**, no
  negative asserted only by a figure has been adjudicated here. Every result in this paper is
  reported by its figure call-outs, which the extractor rendered as 45 empty parentheses; the
  directional claims above rest on the authors' prose statements about those figures, not on the
  figures.
- **Extraction defect: PRESENT and confirmed by internal evidence.** The MCP extractor deleted every
  italicised token. Signatures observed in the artefact: 45 empty parentheses `()` where figure and
  reference cross-references stood; the word-joins "Humangene" (×2, for *Human WWOX gene*),
  "ofmRNA"/"themRNA" (×4), "developedgene", "from theandcells", "with thecontrol cells",
  "ingene knockout mice", "carryingcDNA", "preventingpurine biosynthesis", "cell growthand".
  A clean external confirmation: the PubMed metadata abstract reads *"the susceptibility of SCC to
  methotrexate (MTX) in vitro and cure"*, whereas the PMC-derived abstract field reads
  *"methotrexate (MTX)and cure"* — the italic *in vitro* deleted between the two surfaces.
  Consequently **"in vitro" and "in vivo" return zero counts on this surface and those zeros are
  instrument readings, not findings.** The same applies to every italicised gene symbol and to the
  genotype labels of the knockout MEFs (§ 3, N2), which are therefore **not readable here**.
- **Informative zeros (roman-type method words, genuinely absent from the paper):** p62, SQSTM1,
  bafilomycin, chloroquine, mCherry, 4E-BP, randomi\*, blinded, neuron, neural, brain, epilep\*.
- **Not recoverable on this surface:** tables, figure legends, the reference list, and therefore all
  quantitative effect sizes, n, and p-values. No quantitative magnitude is asserted anywhere in this
  audit.
- **Not medical advice.** Nothing here substitutes for a treating clinical team.
- **Attribution.** Article metadata and full text retrieved from PubMed / PubMed Central.
  DOI: https://doi.org/10.1038/cddis.2013.308 · PMID 24008736 · PMCID PMC3789168.
  Licence CC BY-NC-ND 3.0, open access.
