# Wwox–Brca1 (PMID 27869163) — transferability audit to a biallelic WWOX loss-of-function neurodevelopmental genotype

**Source.** Schrock MS, Batar B, Lee J, Druck T, Ferguson B, Cho JH, Akakpo K, Hagrass H, Heerema NA,
Xia F, Parvin JD, Aldaz CM, Huebner K. *Wwox–Brca1 interaction: role in DNA repair pathway choice.*
**Oncogene** 2016;36(16):2215–2227. PMID 27869163 · PMCID PMC5398941 · DOI 10.1038/onc.2016.389.
`article_types`: Journal Article; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't.
Licence CC BY-NC-ND 4.0, open access (PMC). Metadata verified against the PMID before reading; **it matches.**

**Artefact read.** `files/fulltext/PMID27869163_PMC_MCPtext.txt` — 31,936 bytes,
sha256 `dccafe62187385233e112789c048637f6764f9a9310ed28a769d6032f06a6839`.
Body only, verbatim from the MCP PMC extractor, plus one terminating newline.
The abstract is reproduced in this file (§9) and deliberately **not** in the artefact.

---

## VERDICT

**Essentially nothing transfers.** This is cancer DNA-repair biology end to end; it contains no neuron, no
brain tissue, no developing CNS, no patient with a germline WWOX disorder, and it measures no endpoint with a
neurodevelopmental analogue. **One narrow item does transfer** and is the only reason to keep the paper:
the WWOX function characterised here requires an intact **WW1** domain and is **retained** by a WWOX protein
carrying a catalytic-site point substitution in the **SDR** domain (Y293F) — a domain-resolved, point-mutant
dissociation relevant in principle to a reference genotype whose missense allele lies in the SDR span,
with the heavy caveat recorded in §5.

---

## 1 · The paper's actual claim, and in what system

The claim is that WWOX protein governs **double-strand break (DSB) repair pathway choice**, biasing repair
toward NHEJ and away from HDR, via a physical interaction with BRCA1; and that WWOX loss therefore confers
resistance to ionising radiation (IR) and cisplatin.

> "We have established a role for Wwox in the regulation of DSB repair, such that Wwox-deficient cells exhibit
> enhanced HDR and survival of DSB-inducing agents." — Discussion, ¶1

> "Altogether, the data indicate that Wwox expression significantly alters repair efficiency for all four DSB
> repair pathways (summarized in) such that Wwox expression enhances NHEJ and Alt-NHEJ, but impairs HDR and SSA."
> — Results, "Wwox expression regulates DSB repair pathway choice", final sentence

Systems, in full: primary mouse embryonic fibroblasts (MEFs) from two independent *Wwox*-knockout mouse lines
and wild-type littermates (WT4, WT7, KO3, KO5, Wwox3, Wwox5); MCF10A breast epithelial cells with stable
shWWOX knockdown; MDA-MB-231 breast adenocarcinoma with doxycycline-inducible WWOX (and WW1-mutant and
SDR-mutant derivatives); HeLa DR-GFP and HeLa Sa26; U87 DR-GFP (glioma); HEK293/HW1; H1299 EJ2; HEK293T for
pulldowns; an athymic-nude-mouse subcutaneous xenograft (10 mice total); and a retrospective query of the
REMBRANDT **brain cancer** expression/clinical database. Every system is a cancer line, a cancer model, or an
immortalised reporter line — except the MEFs (§2).

## 2 · Non-cancer material

**Yes, but only one kind, and it is not neural.** The only germline-null, non-transformed, primary material is
**mouse embryonic fibroblast**, harvested at embryonic day 13:

> "MEFs were isolated from individual 13-day embryos ofandmixed background (B6 × 129 SvJ) strain pregnant
> females and designated MEF WT4, WT7, KO3 and KO5 cell lines." — Materials and methods, "Cell lines"
> (the deleted words after "of" and "and" are the italicised genotype symbols; see §10)

So: a germline *Wwox*-null animal, a defined developmental time point (E13), and a primary cell — but a
fibroblast, studied for karyotype, CNV and clonogenic survival of radiation. MCF10A is breast epithelium, and
the paper itself calls it "transformed breast epithelial cell line, MCF10A". HEK293T is embryonic kidney used
only as a transfection host for pulldowns.

**Roman-type string counts in the artefact (informative zeros, not extraction artefacts):**
`neuron` 0 · `neuronal` 0 · `seizure` 0 · `epilep*` 0 · `encephalopath*` 0 · `blinded` 0.
`brain` occurs 3 times and every occurrence is "brain cancer" / "Molecular Brain Neoplasia Data".
There is **no nervous-system material in this paper at all.**

The one sentence touching germline organism-level phenotype is a citation to prior work, not a finding here:

> "Mouse models confirm a tumor suppressor function for Wwox, as complete knockout mice on various genetic
> backgrounds was postnatal lethal." — Introduction, ¶1

## 3 · Does anything bear on a loss-of-function genotype

**Yes — the necessity arm is real and well controlled.** WWOX is removed, not merely added, in most of the
key experiments: germline knockout MEFs; stable shRNA knockdown in MCF10A (shWWOXA, shWWOXB); transient
siWwox in U87, HEK293 and H1299. Sufficiency (re-expression) is used as the *rescue* control, which is the
correct direction of use:

> "To confirm Wwox specificity, we performed a rescue experiment in the U87 DR-GFP cells by transfecting
> siWwox (directed toward Wwox 5′-untranslated region) simultaneously with a full-length Wwox expression
> plasmid, myc-Wwox." — Results, DSB pathway choice

> "To confirm that enhanced survival was because of the absence of Wwox, we established clones KO3A and KO5F
> from the knockout MEF cell lines KO3 and KO5, which were doxycycline inducible for the expression of Wwox.
> Upon Wwox induction, both clones exhibited significantly decreased survival (<0.05) at 7.7 Gy and above (),
> confirming that Wwox expression sensitizes cells to radiation." — Results, IR survival

So the **methodology** is genotype-appropriate (loss-of-function with rescue, two species, several independent
lines). The **biology being measured** is not. Methodological adequacy does not create relevance.

## 4 · Direction for a WWOX-scarce genotype

The direction is **endpoint-dependent, and the two endpoints point opposite ways.**

- *Short-term cell survival of genotoxic insult* — **better** with WWOX scarce. Knockout MEFs survive IR
  ~10-fold better than wild type at ≥7.7 Gy; WWOX-silenced MCF10A survive bleomycin 25- to 100-fold better;
  WWOX-negative MDA-MB-231 survive cisplatin better. Mechanism: enhanced HDR, and the effect is abolished by
  RAD51 knockdown ("knockout MEFs had survival curves similar to wild-type cells").
- *Genome integrity* — **worse** with WWOX scarce, but mildly:

> "The karyotype and CNV results suggest that absence of Wwox protein is associated with mild genome
> instability, likely stemming from endogenous DNA damage" — Results, CNV section

Crucially, **unstressed cells showed no difference**:

> "We first considered whether Wwox loss leads to uninduced genome damage (i.e., damage not due to exposure to
> exogenous cytotoxic agent), but the comet assay, which detects DSBs as comet tails, and immunofluorescence
> assays for DSB markers, 53BP1 and γH2AX, did not reveal differences in untreated Wwox-deficient and
> -expressing cells ()." — Results, CNV section

That negative is the most disease-relevant single sentence in the paper: **absent an exogenous genotoxin, a
WWOX-null primary cell is not visibly damaged.** A developing brain is not irradiated, and this reduces the
prior that WWOX-linked DSB-repair dysregulation contributes to the neurodevelopmental phenotype.

The authors' own extrapolation goes to cancer and nowhere else:

> "we propose that long-term, Wwox-deficient cells carry a higher mutational burden despite short-term cellular
> survival of DNA DSBs because of enhanced HDR." — Discussion, ¶3

> "We propose that determining Wwox expression levels could be an important predictor of response to radiation,
> cisplatin and possibly other chemotherapeutic agents." — Discussion, ¶4

**They make no extrapolation to any non-cancer, germline or neurological setting.** LEGEND must not make one
for them.

## 5 · Domain requirements — the one transferable item

This is the only part of the paper with purchase on a missense genotype, and it is genuinely informative.

Interaction mapping by GST pulldown:

> "GST fused to the WW domain fragment (WW1 and 2, lane 3) bound HA-Brca1; however, the WW domain fragment with
> mutated WW1 (W44F/P47A),which renders the binding domain non-functional, did not bind HA-Brca1 (lane 4),
> suggesting that Wwox interaction with Brca1 occurs through the WW1 domain. In support of this, a WW domain
> with mutated WW2 (Y85A/P88A in lane 5) pulls down HA-Brca1, indicating that WW2 is not essential for the
> interaction; finally, a GST-fused SDR fragment did not bind HA-Brca1 (lane 6) and does not contain either
> WW domain." — Results, "Brca1 and Wwox proteins form a complex"

Functional confirmation with **full-length point mutants** in a WWOX-null cancer line:

> "the MDA MB-231 cells were stably transfected with doxycycline-inducible full-length Wwox harboring WW1
> mutationsW44F/P47A (231/WW1 mut) or full-length Wwox harboring a mutation (Y293F) at the catalytic SDR site
> (231/SDR mut)" — Results, "Wwox interaction with Brca1 through the WW domain..."

> "This suggests that without a functional WW1 domain, Wwox does not sensitize cells to radiation. Conversely,
> upon expression of full-length Wwox harboring an SDR mutant, the cells exhibit significantly decreased
> survival relative to the same cells uninduced (); that is, the SDR mutant Wwox-expressing cells are sensitive
> to radiation because they retain a WW1 domain, which interacts with Brca1." — same section

**What this licenses:** for *this* WWOX function, the SDR catalytic site is dispensable and WW1 is required.
A point substitution at the SDR catalytic tyrosine did **not** behave as a null.

**What this does not license, and the caveat is decisive.** Y293F is a designed, conservative,
catalysis-abolishing substitution chosen precisely to leave the fold intact. A disease missense allele in the
SDR span is a different object: it may destabilise the protein, mislocalise it, or abolish the WW1-dependent
function indirectly by removing the protein altogether. This paper measures **no** WWOX protein level, stability
or localisation for any mutant (§6), so it cannot distinguish "SDR catalysis is dispensable" from "this
particular SDR protein is present and folded". LEGEND may cite this for *"SDR catalytic activity is not
required for the WWOX–BRCA1 interaction or for WWOX-dependent radiosensitisation"* — and for nothing broader
about SDR missense alleles.

On the BRCA1 side the mapping is coarse and hedged: deletion mutants localise the requirement to
"sequences within the Brca1 amino-acid 305–1292 region", and the motif claim is explicitly tentative —
"Wwox may interact with Brca1 near thePPLFmotif ... directly or indirectly". The Results call the motif
"a PPxL Wwox-binding motif at amino acid 981"; the Discussion calls it PPLF. That is a naming inconsistency
in the source, not an extraction artefact of the kind in §10.

## 6 · Protein stability — a clean negative

**Nothing.** The paper does not measure WWOX protein abundance quantitatively, half-life, turnover or
degradation route.

Roman-type string counts in the artefact, all informative zeros:
`cycloheximide` 0 · `half-life` 0 · `degradation` 0 · `proteasom*` 0 · `lysosom*` 0 · `turnover` 0 · `abundance` 0.
The three occurrences of `stabilit*`/`instabilit*` are all **genome** stability ("mild genome instability",
"chromosomal instability"), never protein stability.

Expression is assessed only qualitatively, as a validation that constructs are on or off — "demonstrates the
inducibility of Wwox expression in these cell lines", "shows relative Wwox expression of cell lines used
throughout the manuscript" — both pointing to figures that are not inspectable here. **This paper contributes
nothing to the post-transcriptional-loss question and must not be cited on it.**

## 7 · Abstract versus results, and the mood check

**There is drift, in three places. This is not a "no discrepancy" reading.**

1. **A negative present in the Results is absent from the Abstract.** The Abstract states: "in a cohort of
   cancer patients treated with radiation, Wwox deficiency significantly correlated with shorter overall
   survival times." The Results disclose that in the *unselected* cohort there was no effect at all:

   > "Stratification of patients by Wwox expression did not predict overall survival in a large cohort of brain
   > cancer patients (); however, in cancers treated with radiation, reduced Wwox expression correlated
   > significantly with decreased overall survival vs Wwox normal cancers ()"

   The reported association is a **subgroup** result inside a null main analysis, from a retrospective brain-cancer
   database, with the dichotomy set post hoc ("a fold change of 2 was used to designate patients as downregulated
   Wwox expression"). The Abstract's "This Wwox effect has important consequences in human disease" is stronger
   than the data.

2. **A within-paper inversion on cell cycle.** The Results report that MEFs *did* differ:

   > "Similar experiments in early-passage (~p10) Wwox-knockout and -wild-type MEFs revealed differences for the
   > wild-type and knockout cells in cell cycle phase distribution () and checkpoint activation (), neither of
   > which activities showed correlation with the responses of the cells to IR ()."

   The Discussion then argues from a flat denial of any such difference:

   > "We believe that the enhancement of HDR because of Wwox absence is mutagenic in Wwox-deficient cells based
   > on the cell cycle analysis data (), which demonstrates that Wwox expression does not affect cell cycle phase."

   The "does not affect" statement holds for the 231 cells, not for the MEFs. The mutagenicity argument rests on
   the generalised version.

3. **"Propose" hardens into "established".** The Abstract says "We propose a genome caretaker function for WWOX".
   The Discussion says "we have established that Wwox is a genome caretaker". The G1-HDR mutagenesis mechanism
   offered to support it is explicitly conditional and unmeasured — "If HDR should occur in the G1 phase, when
   sister chromatids are unavailable, the homology search may take place across the entire genome" — no
   phase-resolved HDR assay was performed. **This is a hypothesis re-voiced as a finding**, i.e. exactly the
   failure mode this session has been tracking, occurring inside the source itself.

The core repair-pathway results (HDR up, NHEJ down, Alt-NHEJ down, SSA up on WWOX loss) are stated consistently
across Abstract, Results and Discussion, with rescue controls, and are not subject to this drift.

## 8 · Independence

Senior/corresponding: **Kay Huebner**, Department of Cancer Biology and Genetics and Comprehensive Cancer Center,
The Ohio State University Wexner Medical Center, Columbus OH. Co-senior **C. Marcelo Aldaz**, Department of
Epigenetics and Molecular Carcinogenesis, MD Anderson Cancer Center, Smithville TX. Additional OSU departments:
Radiation Oncology (Xia), Pathology (Heerema), Biomedical Informatics (Parvin).

**Independent of Chang Nan-Shan (NCKU): yes.** **Independent of Aqeilan (HUJI): yes.** No NCKU and no Hebrew
University affiliation appears. The Aqeilan WWOX–ATM work is cited as someone else's and explicitly contrasted:
"Unlike a recently reported interaction between Wwox and the kinase, ATM,the interaction of Wwox with Brca1
appears not to be dependent on DNA damage."

Caveat for corroboration weighting: Huebner and Aldaz are **not naive third parties** — both lead long-standing
WWOX laboratories with a prior commitment to the WWOX-as-tumour-suppressor framing. They constitute a third
independent lineage, distinct from Chang and from Aqeilan, but they are not an outside check.

## 9 · Abstract (reproduced here, not in the fingerprinted artefact)

Per PubMed, PMID 27869163, [DOI](https://doi.org/10.1038/onc.2016.389): "In this study, loss of expression of the
fragile site-encoded Wwox protein was found to contribute to radiation and cisplatin resistance of cells,
responses that could be associated with cancer recurrence and poor outcome. WWOX gene deletions occur in a variety
of human cancer types... We propose a genome caretaker function for WWOX, in which Brca1-Wwox interaction supports
NHEJ as the dominant DSB repair pathway in Wwox-sufficient cells." (Quoted in §7 where load-bearing.)

## 10 · Extraction defect — present

The MCP PMC extractor's italic-deletion defect is **present and severe** in this artefact:

- **All 16 p-values are orphaned**: the italic *P* is deleted, leaving `(<0.01)`, `(<0.05)`, `(<0.001)`,
  `(<0.0001)`, `(;<0.05)`.
- **All n values are deleted**: `(=2)`, `(=4 for each group)` — the xenograft group sizes survive only because
  they are also given in prose (7/8 and 6/8 tumour-bearing; 10 mice total).
- **All figure and table cross-references are deleted**, leaving **35** empty `()` stubs and truncated sentences
  ("as indicated in.", "summarized in)", "described.", "As predicted,shows that...").
- **Italicised gene symbols are deleted**, producing scars: "The 1.2 Mbgene", "identifiedas the third most commonly
  deleted gene", "embryos ofandmixed background", "Wwox3 (Wwox) and Wwox5 (Wwox) MEFs" (genotype superscripts gone),
  "near thePPLFmotif".
- **No figure legends, no tables and no reference list survive.** Concentrations and doses survive only where
  given in prose.

Per **D-14**, no negative asserted only by a figure has been adjudicated here. The §4 comet-assay/53BP1/γH2AX
negative and the §5 pulldown lane assignments are **stated in the body text** and are quoted as body-text claims,
not read off images.

## Closing — what LEGEND may and may not cite this paper for

**May cite for:** (a) WWOX loss shifts DSB repair pathway choice — HDR and SSA up, NHEJ and Alt-NHEJ down —
demonstrated by knockdown/knockout with re-expression rescue across mouse and human cells; (b) a physical
WWOX–BRCA1 interaction requiring **WW1** and not WW2, with the SDR fragment not binding; (c) the point-mutant
dissociation that **SDR catalytic-site substitution Y293F retains** WWOX-dependent radiosensitisation while
**WW1 W44F/P47A abolishes it**; (d) the negative that WWOX-null primary MEFs show **no** excess DSB markers in
the absence of exogenous genotoxin.

**May not cite for:** anything neurodevelopmental, neuronal, epileptic or germline-clinical; any statement about
WWOX protein stability, half-life or degradation route (the paper measures none); any claim about how a disease
**missense** allele in the SDR span behaves (Y293F is a designed catalytic substitution, and no protein level was
measured); the REMBRANDT survival association without recording that the unselected-cohort analysis was null; and
the "established genome caretaker" framing, which the paper's own Abstract states as a proposal.

---

*Author: Scientist B. Date: 2026-09-21. READ-ONLY — no canonical LEGEND file, registry, queue, ledger or current
file was modified; no git operation performed; no commit candidate produced. Declared limits: no figure image was
inspected and no figure-only negative was adjudicated (D-14); the MCP extraction defect is **present** and is
characterised in §10; source licence CC BY-NC-ND 4.0, open access, quotation only, no redistribution of the full
text beyond the local artefact.*
