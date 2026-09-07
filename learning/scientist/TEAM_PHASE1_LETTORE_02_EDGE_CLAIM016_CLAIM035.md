# PHASE I — EDGE ADJUDICATION · `CLAIM 016 <-> CLAIM 035`

**Actor:** Scientist A, worktree `lettore`, branch `lettore`.
**Status:** NON-CANONICAL. No canonical file written, no wikilink annotated, no relation type
applied to the repository. This is an adjudication *record*, not an edit.
**Peer isolation:** Scientist B's pilot not read (Phase II gate closed on C — artifact 00 §5).
**Public, disease-level, de-identified. Nothing here is medical advice.**

---

## EDGE / TASK ID

`PATHOGRAPH-EDGE-CLAIM016-CLAIM035` · edge 8 of the 20 measured in
`legend-operating-convention-v1:disease-models/wwox/analysis/pathograph_inventory.md` § 2 ·
triage class `PRIMARY_AVAILABLE`. *(Path qualified by ref 2026-08-26: the inventory exists on that
branch only, not on `main` or `lettore`.)*

## SOURCE CONCEPT · TARGET CONCEPT

The edge as the registry declares it is **undirected and untyped**, and both endpoints are
compressed claim titles rather than entities. Held apart before anything is decided:

| Endpoint | Declared title | Latent entities |
|---|---|---|
| `CLAIM 035` | *WWOX is a direct, residue-mapped inhibitor of GSK3β through an Axin-like docking motif in the SDR domain (388–407 / L404); the inhibition is S9-independent and its neuronal output requires Tau* | ENTITY(WWOX protein) — RELATION(inhibits, by direct binding) → ENTITY(GSK3β) — RELATION(requires) → ENTITY(Tau) |
| `CLAIM 016` | *GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency* | ENTITY(GSK3β activity state) — RELATION(contributes to) → PHENOTYPE(seizure susceptibility), conditioned on ENTITY(WWOX loss) |

## CURRENT REPOSITORY ASSERTION

Read from `main` (`788c357`) via `git show`, never from my checked-out tree.

| Field | Value |
|---|---|
| Reciprocal | **yes** — both records wikilink the other |
| Declared in | `Meccanismo aggiunto (BATCH_20260726_001)`, `Wikilinks` |
| Relation type | `UNTYPED` — `NO_DECLARED_RELATION_ANNOTATION` |
| Shared evidence | `PAPER 056` |

The load-bearing sentence, verbatim from `claim_registry_current.md`, `CLAIM 016`:

> *"WWOX non è soltanto correlata al livello di GSK3β — ne è un **inibitore fisico diretto**,
> tramite il motivo di docking Axin-like 388–407/L404 del dominio SDR
> ([[paper_registry_current#PAPER 056]], [[claim_registry_current#CLAIM 035]]). L'affermazione
> causale si sposta quindi da «GSK3β è elevata» (osservazione di abbondanza) a «GSK3β è
> de-repressa» (perdita di un freno fisico). L'inibizione è **S9-indipendente**: nel sistema di
> Wang la fosfo-S9 e l'abbondanza di GSK3β restano invariate mentre l'output della chinasi
> cambia."*

So the repository's implicit reading of this edge is: **035 supplies the mechanism that makes 016
causal.** That is the proposition adjudicated below.

## PRIMARY SOURCE(S)

| Role | Paper | Artifact | Fingerprint |
|---|---|---|---|
| **Shared evidence** (`PAPER 056`) | Wang H-Y *et al.* 2012, *Cell Death Differ* 19:1049 · PMID 22193544 · PMC3354054 · DOI 10.1038/cdd.2011.188 | `files/fulltext/PMID22193544_Wang2012_PMC_JATS.xml` | sha256 `eb6f568d046f8df831d15e7f8795fcb1d6ac713ec6305f7ded3ad2a330388268`, 96 230 bytes |
| Endpoint evidence for `CLAIM 016` (`PAPER 019`) | Cheng Y-Y *et al.* 2020, *Acta Neuropathol Commun* 8:6 · PMID 32000863 | `files/fulltext/PMID32000863_Cheng2020_PMC.xml` + Fig. 7 PNG | sha256 `792b5b29…f00f5` · `ced68a66…62542` |

Structured JATS preferred over PDF throughout (`CLAUDE.md` §5d). Abstract held separate from
body; **every locator below is BODY-EXACT**, none is abstract-sourced.

**Verification performed this session, not inherited:** the nine verbatim locators recorded in
`deepdive_manifests/PMID22193544.json` were re-matched against a text surface I re-derived today
from the JATS artifact (strip tags to empty, *then* unescape entities — the order that a prior
session got wrong and paid for). **9 / 9 match the non-abstract body; 0 / 9 are found in the
abstract.**

---

## MODEL / SYSTEM

| | `PAPER 056` (Wang 2012) | `PAPER 019` (Cheng 2020) |
|---|---|---|
| Organism | **Human** cell line + **mouse** brain extract | **Mouse** |
| Cell type / tissue | SH-SY5Y neuroblastoma; recombinant GST fusions; whole mouse brain extract | cerebellum, hippocampus, cortex (blot); whole animal (behaviour) |
| Genotype | WWOX wild type + engineered point mutants (L404A, L311A); GSK3β WT / S9A / kinase-dead / R96A; RNAi knockdown — **no WWOX-DEE allele tested** | `Wwox+/+`, `Wwox+/−`, `Wwox−/−` constitutive systemic null |
| Developmental stage | not applicable (immortal line); mouse brain stage not stated | P20 (blot); preweaning (seizure work) |
| Condition | retinoic-acid–induced differentiation; *in vitro* kinase assay; GST pull-down; turbidimetric microtubule assay; MD simulation | PTZ 30 mg/kg; pilocarpine 50 mg/kg; LiCl 60 mg/kg; ethosuximide 150 mg/kg; drug-naive for the blot |

🔴 **The two endpoints are measured in different organisms, different preparations and different
decades of assay, and never in the same animal.**

---

## OBSERVATION — what was directly measured

**From `PAPER 056`, BODY-EXACT, all re-verified today against sha256 `eb6f568d…8268`:**

1. *"WWOX296−320 and WWOX388−412 contain FXXXLI/VXRLE, a highly conserved GSK3β-binding motif
   within GSKIP115−139, Axin381−405, and FRAT205−229"* — sequence homology to three canonical
   GSK3β docking partners.
2. *"This indicates that WWOX amino acids 388–407 are required for its interaction with GSK3β."*
3. *"the mutation of L404A, but not L311A, completely abolishes the binding of WWOX to GSK3β"* —
   a single-residue requirement with an internal negative control.
4. *"Ectopically expressed WWOX significantly inhibited Tau phosphorylation at S404 and S396 but
   not S422."* — substrate-selective inhibition; S422 is the MKK4 site and is untouched.
5. *"immunoprecipitation was performed in mouse brain extracts to verify the physiological
   interaction between WWOX and GSK3β. Figure 2e shows that both GSK3β and WWOX were precipitated
   by anti-GSK3β or anti-WWOX antibodies."* — the interaction exists **between endogenous
   proteins in brain**, not only between overexpressed ones.
6. 🔴 *"We found that the phosphorylation levels of phospho-GSK3β S9 and phospho-β-catenin
   remained normal."* — while GSK3β output onto Tau falls.
7. 🔴 *"Transfection with GFP–GSK3β WT and S9A notably decreased SH-SY5Y cell differentiation,
   whereas KD and R96A did not affect SH-SY5Y cell differentiation"* — **the S9A mutant, which
   cannot be switched off by Ser9 phosphorylation, behaves exactly like wild-type GSK3β.**
8. *"Neither WWOX overexpression nor GSK3β knockdown promoted neurite outgrowth in the Tau
   knockdown condition, indicating that Tau is the effector of both WWOX and GSK3β"* — epistasis
   placing the three on one linear path.
9. *"SH-SY5Y cells in which WWOX expression was reduced by RNAi showed increased pTau S396 levels
   and notably decreased neurite outgrowth"* — losing WWOX raises GSK3β output, the direction
   `CLAIM 016` needs.

**From `PAPER 019` (Cheng 2020), established in the preserved pilot and its addendum:**

10. pGSK3β(Ser9)/β-actin falls in `Wwox−/−` brain at P20 in three regions; total GSK3β/β-actin is
    approximately unchanged (9–18% upward drift); **`+/−` is at wild-type level, not
    intermediate**; **no statistics of any kind** attach to the panel.
11. LiCl 60 mg/kg suppresses PTZ-evoked Racine score **significantly in `+/+`, `+/−` and `−/−`
    alike** (Fig. 7d), with no saline arm and no interaction test.
12. GSK3β was **never** measured in a lithium-treated animal.

### 🔴 The measured fact that decides this edge

**`PAPER 056` — the shared evidential paper — contains no seizure endpoint of any kind.**
Counted over the whole artifact: `seizure` **0**, `epilep` **0**, `convuls` **0**, `lithium`
**0**, `LiCl` **0** — in a 49 334-character non-abstract body and its abstract, both derived
today from sha256 `eb6f568d…8268`. *Denominator declared:* the complete JATS text surface, body
and abstract, of that one artifact.

⇒ The edge's "shared evidential paper" is shared **bibliographically** — both claim records cite
it — and **not evidentially**: it measures one endpoint and never the other.

---

## AUTHOR INTERPRETATION

**Wang 2012**, Discussion, BODY-EXACT: *"our results connect WWOX, GSK3β and Tau in an exclusive,
direct manner and describe a novel mechanism by which WWOX promotes neuronal SH-SY5Y cell
differentiation"*. The authors' scope is **neuronal differentiation**. They claim no disease, no
excitability, no seizure.

**Cheng 2020** cites Wang 2012 explicitly as its mechanistic premise — *"WWOX has been shown to
interact with and inhibit GSK3β, thereby increasing the microtubule assembly activity of Tau and
promoting neurite outgrowth in human neuroblastoma SH-SY5Y cells [65]"* — and its reference list
carries `WangHY… Cell Death Differ 2012 19 1049` (PMID 22193544 appears once). It then concludes:
*"these results suggest an important role of GSK3β in the hypersusceptibility to epileptic seizure
induction due to Wwox loss"*, and defers the therapeutic question — *"Future studies, as well as
more evaluations, will be needed…"*.

So the composite the edge encodes is **Cheng's**, built by citing Wang, and Wang's authors assert
no part of it.

---

## SCIENTIST INTERPRETATION — what the evidence licenses

### The composition fails at a named joint

The attractive reading is a clean chain:

```
WWOX loss → loss of docking-motif inhibition → GSK3β de-repressed → seizure susceptibility
             (Wang, DATO)                        (Cheng, observed)     (Cheng, lithium)
```

Two of the three arrows do not survive contact with the evidence, and the second failure is new.

**Arrow 3 fails on pharmacology** — established in the preserved pilot: the only support is a
lithium experiment that is significant in wild-type animals and never measured its own target.

🔴 **Arrow 2 fails on readout identity, and this is the finding this edge adjudication
produces.** Cheng's *sole* in-vivo evidence that GSK3β is de-repressed in `Wwox−/−` brain is
**Ser9 dephosphorylation**. Wang establishes, twice and by design, that the Ser9 axis is not how
WWOX controls GSK3β in neurons:

- WWOX represses GSK3β output onto Tau *while* **"phospho-GSK3β S9 … remained normal"** (obs. 6);
- the **S9A** mutant — a GSK3β constitutively immune to Ser9 inhibition — suppresses
  differentiation **exactly like wild type**, whereas kinase-dead and R96A do not (obs. 7). The
  Ser9 switch is dispensable for the very output being measured.

**Therefore Cheng's Ser9 decrease cannot be attributed to loss of the Wang mechanism.** Losing a
docking-motif inhibitor predicts raised GSK3β activity **with Ser9 unchanged**. Cheng observed
Ser9 *changed*. That is a different event, requiring a different cause — upstream kinase
signalling (Akt / PKA / PKC), or the diseased-brain state itself. `CLAIM 036` records that a
systemic constitutive `Wwox`-null mouse at this age is metabolically decompensated, which is a
standing confound for any whole-brain phospho-signalling readout in this model.

The registry already holds half of this insight, in `CLAIM 035`'s `Clinical meaning`: *"la
de-repressione di GSK3β causata dalla perdita di WWOX sarebbe **invisibile a un western
anti-fosfo-S9** … qualunque studio WWOX-DEE che usi pS9 come readout di attività GSK3β produrrà
un **falso negativo**."* **The other half was never drawn.** Cheng did not get a negative — Cheng
got a *positive* Ser9 change, and by `CLAIM 035`'s own logic that positive is evidence of
something other than the WWOX-proximal mechanism. Two canonical claims are wikilinked to each
other while one of them contains the argument that the other's key measurement does not mean what
it is taken to mean.

### The counter-argument, stated at its strongest and weighed

Ser9 dephosphorylation and loss of docking inhibition are **not mutually exclusive**. A brain
without WWOX could plausibly carry both: (i) loss of the physical brake, invisible to pS9, and
(ii) a secondary Ser9 fall from altered upstream signalling. Under that reading both push GSK3β
activity up, Cheng's observation corroborates raised activity even though it is not the
WWOX-proximal channel, and the edge survives with a longer path — which is exactly what
`INDIRECT_UNKNOWN_INTERMEDIATES` encodes.

**This is a serious argument and it is not refuted.** What it lacks is a measurement. Nothing in
either paper tests whether the Wang mechanism operates in `Wwox−/−` brain: no pull-down, no
substrate-specific kinase readout, no L404-dependent manipulation *in vivo*. The reading is
available; it is not evidenced. And the heterozygote weighs against its simple form — if WWOX
dosage set the Ser9 state, `+/−` should sit between the other two, and it does not (addendum §1.4).

### Direction

Directionality is licensed for the **035 half only**: WWOX → GSK3β, established by binding, by a
single-residue requirement with an internal control, and by loss- and gain-of-function in the
same system. **No direction is licensed for the 016 half** from either paper — GSK3β state and
seizure susceptibility are never measured in the same animal, and the only intervention that
joins them is non-specific.

---

## RELATION TYPE

Governed vocabulary, from the assembler's own accepted set — nothing outside it is used:
`DIRECT` · `INDIRECT_UNKNOWN_INTERMEDIATES` · `ASSOCIATED` · `CONTROVERSIAL_OPEN`.

| Candidate | Verdict |
|---|---|
| `DIRECT` | ❌ Reserved for *"the same experiment measures both endpoints"*. No experiment in either paper measures both. |
| `INDIRECT_UNKNOWN_INTERMEDIATES` | ❌ **for the edge as declared.** It asserts a causal path with unspecified intermediates. Here the intermediates are not merely unknown — the one bridging measurement offered (Ser9) is the one the mechanism paper shows is not the operative channel. Typing it this way would encode as *unknown-but-real* something that is *untested*. |
| **`ASSOCIATED`** | ✅ **for the edge as declared.** Both claims concern GSK3β in WWOX-deficient systems and are evidentially linked through a shared citation; no experiment links them. This is what `ASSOCIATED` is for. |
| `CONTROVERSIAL_OPEN` | ❌ No finding of either paper contradicts the other's *observations*. The tension is about whether they compose, not about what was seen. Using it would mislabel a composition gap as a contested result. |

### 🔴 The edge is one token where the evidence is two

Typing this edge with a single token loses the fact that its two halves are supported at
completely different strengths. Recorded here for later Plan work — **not** as a proposal to
create vocabulary or split the registry:

| Sub-relation | Best-supported type | Evidence |
|---|---|---|
| WWOX ⊣ GSK3β (physical, residue-mapped, S9-independent) | `DIRECT` | `PAPER 056`, five orthogonal assays, one point mutation, endogenous brain co-IP |
| GSK3β state → seizure susceptibility | **unsupported** | only the lithium experiment, which works in wild type and never measured its target |
| Composite `CLAIM 016` as a causal statement | `ASSOCIATED`, with the qualification below | — |

A one-token edge between two compressed titles cannot carry that. The limitation is structural,
not a defect of this adjudication.

---

## CAUSAL LIMIT — what prevents a stronger interpretation

1. The shared evidential paper measures **one** of the two endpoints. Zero seizure content.
2. The two endpoints are never measured in the same organism, let alone the same animal.
3. The bridging readout (Ser9) is shown by the shared paper to be **not the channel** WWOX uses.
4. `PAPER 056` tested **no WWOX-DEE allele** — only wild-type WWOX and engineered mutants. Its
   `Genotype/model relevance` field says so. Transfer to a disease genotype is `INFERENZA`.
5. SH-SY5Y is a neuroblastoma line under RA differentiation, not a neuron and not a network.
6. Cheng's model is a **systemic constitutive** null with documented metabolic decompensation
   (`CLAIM 036`) — a standing confound for whole-brain phospho-signalling.
7. Panel 7c carries no statistics at all (addendum §1.3).
8. `WWOX AND GSK3` returns **five records in all of PubMed** (`PAPER 056` manifest,
   `field_density`, executed 2026-07-26). A near-empty intersection in a rare disease means the
   edge is **untested**, not tested-and-rejected — and it means this edge rests on a two-paper
   literature of which one is this shared paper.

---

## NEGATIVE / COUNTER-EVIDENCE deliberately sought

Sought against the *attractive* reading — that Wang's beautiful residue-level mechanism explains
Cheng's in-vivo finding:

1. 🔴 **The S9A mutant behaves like wild type** (obs. 7). Designed, orthogonal, and it removes the
   Ser9 axis as the operative control in the very assay Wang uses.
2. 🔴 **pS9 remains normal while GSK3β output falls** (obs. 6). Stated by the authors themselves.
3. 🔴 **Zero seizure/lithium content in the shared paper**, over the whole text surface.
4. 🔴 **The heterozygote is not intermediate** in Cheng's panel — against a simple WWOX-dosage →
   GSK3β-state mechanism (addendum §1.4).
5. 🔴 **No WWOX-DEE allele was ever tested** in the mechanism paper.
6. ⚠️ **The mechanism paper's own group profile is asymmetric.** Per its manifest: the senior
   author's lab is a GSK3β/kinase-signalling lab with 3 of 472 records on WWOX; WWOX entered as
   the starting hypothesis supplied by the field's founder, not through an unbiased screen. That
   makes the *biochemistry* the part to trust most and the *WWOX framing* the part that is
   weaker as independent confirmation.
7. ⚠️ **Searched and not found:** any measurement in either paper of the Wang mechanism operating
   in `Wwox−/−` brain — no pull-down, no L404-dependent manipulation *in vivo*, no
   substrate-specific GSK3β activity readout. *Denominator:* both complete text surfaces.

**Found in support, and it is real:** the interaction is detectable between **endogenous proteins
in mouse brain** (obs. 5). That is the single strongest bridge from the cell line to the tissue,
and it is why `CLAIM 035` deserves its `DATO` on the mechanism half.

## CONTRADICTORY EVIDENCE

None between the two papers' **observations**. The tension is between the *inference* Cheng draws
from Ser9 and the *mechanism* Wang establishes as S9-independent. Recorded as a composition
failure, not as a contradiction, because that is what it is.

---

## EVIDENCE SUFFICIENCY

**Not sufficient to carry the edge into a scientific graph as a mechanistic relation.**
Sufficient to carry it as an association between two claims about GSK3β in WWOX-deficient
systems, provided the qualification travels with it.

## GRAPH RECOMMENDATION

### 🔴 **carry with qualification** — as `ASSOCIATED`, never as `INDIRECT_UNKNOWN_INTERMEDIATES`

Qualification that must travel with the edge, or the edge should not travel:

> The two endpoints are supported by different papers in different organisms and are never
> measured together. The shared evidential paper (`PAPER 056`) contains no seizure endpoint. The
> only bridging measurement — GSK3β Ser9 dephosphorylation — is on the axis that same paper shows
> is **not** how WWOX controls GSK3β, so it cannot be attributed to loss of the WWOX mechanism.
> The half of the edge that is strongly evidenced is WWOX ⊣ GSK3β; the half that reaches the
> seizure phenotype is carried only by a non-genotype-specific, non-target-attributed
> pharmacological experiment.

**Per-half disposition, for whoever integrates:**

| Half | Disposition |
|---|---|
| WWOX ⊣ GSK3β, residue-mapped, S9-independent | **carry existing relation** — `DIRECT`, within `PAPER 056`'s system, with the no-DEE-allele boundary attached |
| GSK3β state → seizure susceptibility | **relation should remain hypothesis rather than established edge** |
| `CLAIM 016` ⟷ `CLAIM 035` as declared | **carry with qualification**, `ASSOCIATED` |
| Whether the Wang mechanism operates *in vivo* in `Wwox−/−` brain | **additional source required** — and there may be no such source: the field is five papers wide |

**Not applied to the repository.** Typing an edge means annotating a wikilink inside
`claim_registry_current.md`, which is one of the four canonical current files and changes only
through `BATCH_COMMIT`. This record is the input to that, not a substitute for it.

---

## DECOMPOSITION_CANDIDATE

Recorded per dispatch §7 as evidence for later Plan work. **No canonical claim was decomposed.**

### DC-1 · `CLAIM 016`

- **Exact title:** *GSK3β hyperactivation may contribute to seizure susceptibility in WWOX
  deficiency*
- **Latent source:** GSK3β hyperactivation (an ENTITY in a STATE)
- **Latent relation:** *may contribute to* — hedged causal, `CAUSAL` class in the inventory's own
  connective scan
- **Latent target:** seizure susceptibility (a PHENOTYPE)
- **Hidden third element:** *in WWOX deficiency* is neither source nor target — it is the
  **condition** under which the relation is asserted to hold, and a graph with no place for a
  conditioning genotype will silently promote it into one of the two endpoints.
- **Why materialization is impaired:** the title compresses ENTITY + STATE + hedge + RELATION +
  PHENOTYPE + CONDITION into one node label. As a node it is unusable; as an edge it has no typed
  form; and the hedge *may* — the single most important word in it — has no representation at all
  in a four-token relation vocabulary.
- **Would decomposition change scientific meaning?** **Yes, and that is the point.** Decomposed,
  the two halves are visibly supported at different strengths, and the weak half stops borrowing
  the strong half's credibility. Compressed, the whole node inherits the tone of its best
  evidence. **This is a decomposition that should happen, and it should be a reading, not a
  parse.**

### DC-2 · `CLAIM 035`

- **Exact title:** *WWOX is a direct, residue-mapped inhibitor of GSK3β through an Axin-like
  docking motif in the SDR domain (388–407 / L404); the inhibition is S9-independent and its
  neuronal output requires Tau*
- **Latent source:** WWOX (SDR domain, residues 388–407, L404)
- **Latent relations:** *inhibits* (direct, physical) → GSK3β; *requires* → Tau; plus a negative
  qualifier, *S9-independent*, which is a statement about the **mechanism's channel** and not
  about either endpoint
- **Latent target:** GSK3β, with Tau as a required downstream effector
- **Why materialization is impaired:** this is **two edges and one mechanism attribute** in one
  title. `WWOX ⊣ GSK3β` and `GSK3β → Tau` are separate relations with separate evidence; the
  `S9-independent` qualifier belongs to neither edge but to how the first one works — and it is
  the qualifier that adjudicates edge `016<->035` above. **A graph that cannot carry it loses the
  fact that decides the neighbouring edge.**
- **Would decomposition change scientific meaning?** Not for the two edges — both are separately
  well evidenced. **Yes for the qualifier**: as prose inside a title it is invisible to a graph;
  as a typed mechanism attribute it becomes the thing that stops `016<->035` from being typed
  causally.

### DC-3 · Registry/mirror wording divergence on `CLAIM 035`

The inventory § 3.1 records that `CLAIM 035` is relational in the **registry title only**, the
working-model mirror row using *"via an Axin-like S…"* where the title uses *"requires"*. Two
wordings of one node, no LINT rule keeping their relational content in sync. Flagged, not
resolved — resolving it is a canonical write.

---

## OBSERVATION_SCOPE

- Two primary artifacts, both structured (JATS), both fingerprinted, both read as body-with-
  abstract-held-separate; one figure asset read at 2× and 6×; one 24-page supplementary PDF
  searched with its denominator declared.
- Canonical state read from `main` (`788c357`) exclusively via `git show`.
- `PAPER 056` was **not** re-read end to end this session. Its nine recorded verbatim locators
  were re-verified against the artifact, and the specific passages this edge turns on (RA
  differentiation / pS9; the GSK3β mutant panel; the mouse-brain co-IP; the Discussion) were read
  in full. **This is a targeted verification read, not a complete read**: it emits no
  `FULLTEXT_READ_RECEIPT`, clears no reading debt, and does not alter the paper's recorded
  evidence depth.
- No peer Scientist artifact was opened.
- Nineteen of the twenty measured edges were **not** adjudicated. Their triage class is recorded
  in artifact 00 § 3.2; twelve of them are adjudicable now and were left undone for want of
  session, not for want of evidence.

---

*Non-canonical. Nothing here is medical advice. No canonical file was modified in producing it.*
