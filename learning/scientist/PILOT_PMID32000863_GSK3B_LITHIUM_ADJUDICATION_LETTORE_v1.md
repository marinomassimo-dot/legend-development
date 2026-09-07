# PILOT ADJUDICATION G-1 — PMID 32000863 · GSK3β / lithium

**Actor:** worktree `lettore` (branch `lettore`). I do **not** self-assign the "Scientist A" /
"Scientist B" label: nothing I can measure from inside this worktree establishes which of the two
independent readers I am, and self-attestation is not identification. The branch name is the
addressable fact; the A/B mapping is the dispatcher's to assert.

**Status:** NON-CANONICAL pilot artifact. Nothing canonical was mutated. No claim registry, paper
registry, manifest, sidecar, contract or governance file was written.

**Peer isolation:** no peer Scientist output was read. `lettore-b` and `lettore-c` worktrees exist
on this disk and were **not** inspected; the only foreign-actor file read was Plan's crosswalk,
which the task explicitly directs me to recover the DisMech statement from.

---

## 1. Worktree / source state (measured, not assumed)

| Fact | Measured value |
|---|---|
| Worktree | `<REPO_ROOT>/.claude/worktrees/lettore` |
| Branch | `lettore` |
| HEAD | `9b0cf470a320bc13afc0b456f5a6e50a9153e19e` (2026-08-14 16:40 +0200) |
| vs local `main` (`788c357`, 2026-08-22) | **201 behind, 0 ahead** — HEAD is a *strict ancestor* (`git merge-base --is-ancestor HEAD main` → 0) |
| vs `origin/main` (`8ab8e4b`, 2026-08-01) | 254 ahead — **the public remote is the stale surface, not `main`** |
| Dirty in my worktree | `M disease-models/wwox/research/deepdive_manifests/PMID42422765.json`; two untracked `framework/protocols/scientist_*.md` |

**I did not fast-forward, and that is a deliberate call.** My branch carries **zero** commits of its
own, so a fast-forward would normally be the correct first move before measuring anything. It is
not safe here: `main` *does* touch the one file my worktree holds dirty (`0b433b7`, `8ce4fa8`,
`8821500` all modify `PMID42422765.json`). Reverting or stashing to clear the way would be a
destructive write over an edit I did not author and whose owner has not declared it finished —
the exact failure the one-actor-one-worktree rule exists to prevent.

**So the canonical state was read non-destructively via `git show main:<path>`**, never from my own
checked-out tree. Every canonical quotation in this document is from `main` (`788c357`), and I say
so at each point. The stale-tree hazard is real and was measured, not waved at: had I read the
claim registry from my own working tree I would have been reading a 2026-08-14 view of a file
whose load-bearing correction landed later.

**Evidence artifacts do not travel with branches.** `.gitignore:7` is `files/`, so the primary
full text exists in exactly one place — the shared checkout. All artifact reads and all hashing
below were done against `<REPO_ROOT>/files/`, i.e. the tree that will
still have them tomorrow.

### Surfaces actually read

| Surface | Ref / path | Kind |
|---|---|---|
| `claim_registry_current.md` | `main` | canonical |
| `deepdive_manifests/PMID32000863.json` | `main` — byte-identical at `e4aa80c` (`git diff` empty) | canonical |
| `dismech_sidecar_016_024_035.jsonl` | `main` | canonical (LEGEND→DisMech projection) |
| `DISMECH_INTEGRATION.md`, `staging/dismech_dryrun/*.yaml` | `main` / shared checkout | LEGEND-authored export, not upstream |
| `dismech_legend_evidence_crosswalk_v2.md` | **untracked**, in the `evidence-index` worktree | Plan's, non-canonical |
| `PMID32000863_Cheng2020_PMC.xml` + Fig7 PNG + supplementary PDF | shared checkout `files/` | **primary** |

**Absence discipline.** I enumerated all 40+ local refs and the working disk before saying
anything was missing. Where I report absence below it is scoped as *"absent from every local ref
and from disk"* — never as global absence.

---

## 2. The DisMech assertion — and an honest boundary around it

### 2.1 What I could not do

**The upstream DisMech entry is not an admitted local source.** It exists at
`dismech.monarchinitiative.org` (Monarch's Disorder Mechanisms KB). I searched every local ref and
the whole disk: there is **no cached copy of the upstream WWOX entry anywhere**. The local
`staging/dismech_dryrun/MONDO_0013687.yaml` and `MONDO_0014533.yaml` are **LEGEND's own outbound
dry-run export**, and neither contains `PP03`, `PP13`, or PMID 32000863 at all.

I attempted live retrieval: the DisMech homepage is reachable without login, but
`/disorders/MONDO:0014533` returns **HTTP 404**, and a web search did not surface the entry. I did
not guess further.

**Consequence, stated plainly:** the node/edge *structure* below is recorded **as transcribed by
Plan**, and I could not verify it at source. I flag it rather than launder it. This does not
sink the adjudication, because the one component that is checkable against the primary — the
evidence snippet — I *did* verify independently, and it is the component that carries the
epistemic weight.

### 2.2 The statement under adjudication (Plan §C.4, unverified-at-source except where marked)

- **Node** `PP03 Wnt/GSK-3beta Signalling Dysregulation`; `biological_processes: GO:0016055 Wnt
  signaling pathway [DYSREGULATED]`. Description: *"…This arm is separated from the others because
  it carries its own pharmacological test: inhibiting GSK-3beta with lithium abolishes induced
  seizures in these animals."*
- **Node evidence**: `PMID:32000863`, `SUPPORT`, `MODEL_ORGANISM`, snippet
  **"Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced seizure in
  Wwox-/- mice."**; explanation *"The pharmacological result that makes this a causal arm for
  seizures rather than a correlated biochemical change."*
- **Edge** `PP03 → PP13`, type **`INDIRECT_UNKNOWN_INTERMEDIATES`**: *"GSK-3beta inhibition
  suppresses induced seizures, placing this arm upstream of network-level hyperexcitability."*
- **`animal_models[0].modeled_mechanisms[1]`** — readout *"Induced-seizure onset after GSK-3beta
  inhibition"*, `direction: ABOLISHED`. **`limitations`**: *"The rescue was measured against
  pentylenetetrazol-**induced** seizures, not the spontaneous seizures that define the human
  disease… Lithium is also not a selective GSK-3beta inhibitor."*
- **`discussions[2] gap_gsk3b_as_a_druggable_node`**, `KNOWLEDGE_GAP`, `OPEN`, attached to PP03;
  proposed experiment: selective GSK-3β inhibition against **spontaneous** seizures on video EEG.

### 2.3 ✅ What I verified independently, at source

The DisMech evidence snippet is **verbatim the paper's ABSTRACT sentence** — and *only* the
abstract:

```
DisMech snippet → present in ABSTRACT : True
DisMech snippet → present in BODY     : False
```

Exact-match after normalising U+2212 MINUS → ASCII hyphen (DisMech writes `Wwox-/-`, the paper
writes `Wwox−/−`). Pre-normalisation the match is False — a benign transcoding, but the same
character class that CLAUDE.md §5d records as load-bearing elsewhere.

**This is the single most important structural fact about the DisMech entry:** its evidence for
the causal arm is drawn from the abstract. The abstract is precisely the surface on which the
genotype restriction is stated most strongly and the panel data are least visible. The limitation
that would qualify the edge is not *hidden* in the paper — it is simply **not present on the
surface DisMech quoted from.**

---

## 3. Primary evidence reconstruction

**Artifact (preferred structured surface, per CLAUDE.md §5d — XML/HTML over PDF, always):**

| | |
|---|---|
| `files/fulltext/PMID32000863_Cheng2020_PMC.xml` | sha256 `792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5` |
| `…_assets/40478_2020_883_Fig7_HTML.png` | sha256 `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542`, 1946×1627 |
| `…_Cheng2020_supplementary.pdf` | sha256 `0acb771cfe3a4c3644b41c10451504047adb715e69727c1889f72774151f8b7f` |

Both hashes match the four `source_artifacts` declared in the canonical manifest. Cheng *et al.*
2020, *Acta Neuropathol Commun* 8:6, PMC6990504, DOI 10.1186/s40478-020-0883-3. **No PDF text
layer was used**; the JATS XML carries correct entities and there is no rendered page for it to
diverge from.

> **🔴 A derived-surface defect I introduced and caught — worth recording.**
> My first flattener unescaped `&lt;` **before** stripping tags, so `***P &lt; 0.001` became
> `***P < 0.001` and the tag regex then swallowed `< 0.001…>` as if it were markup. The legend
> silently rendered as `***P WWOX has bee` — the significance threshold *deleted*, with no error.
> One quote failed and exposed it. My first repair over-corrected (replacing tags with a space
> broke attributed tags like `<italic toggle="yes">`, giving `* P < 0.05`). The correct order is
> **strip all tags to empty, then unescape**. This is CLAUDE.md §5c/§5d reproduced in miniature at
> my own hands: a derived text surface that looked clean and read wrong. Every quote below was
> re-verified after the fix.

**Verification result: 13/13 evidentiary quotes match the declared artifact EXACTLY**
(non-abstract body surface, with the XML abstract held separate).

### Experimental design as actually specified (Methods, "Induction of seizure")

| Element | Value |
|---|---|
| Convulsant | PTZ (GABA-A antagonist), i.p. **30 mg/kg** — the authors' own "low dose" |
| Second convulsant (7a) | pilocarpine 50 mg/kg, after methylscopolamine 1 mg/kg |
| Ethosuximide | i.p. **150 mg/kg**, **45 min before** PTZ (T-type Ca²⁺ blocker) |
| LiCl | i.p. **60 mg/kg**, **three times within 1 h before** PTZ |
| Readout | modified Racine scale, **ordinal stages 0–6**, scored 60 min |
| Genotypes | `Wwox+/+`, `Wwox+/−`, `Wwox−/−` |

### 🔴 The statistics, verbatim and complete

> *"We performed statistical tests with one-way analysis of variance (ANOVA) to compare the
> difference among groups. The differences were considered significant when the P values were less
> than 0.05."*

That is the **entire** Statistical analysis section. Four consequences, each load-bearing:

1. **One-way ANOVA only.** No two-way design, therefore **no genotype × treatment interaction term
   anywhere in the paper.** The test that would establish genotype specificity *was never run*.
2. **No post-hoc procedure named**, though multiple pairwise brackets are drawn per panel.
3. **A parametric test on an ordinal scale.** Racine stages are ranks, not interval measurements.
4. **Repeated measures treated as independent.** Each animal is scored ~60 times over 60 min; no
   repeated-measures or time-factor handling is described.

---

## 4. Figure 7b adjudication — ETHOSUXIMIDE

**Panel assignment established from the primary, three independent ways** — legend, Results text,
and the panel itself. Not from Plan.

Legend (BODY-EXACT): *"b Higher seizure activity was observed in Wwox−/− mice after injection of
PTZ (30 mg/kg), a GABAergic receptor antagonist, as compared with Wwox+/+ and Wwox+/− mice.
**Pretreatment of ethosuximide (ETS, 150 mg/kg) suppressed PTZ-induced seizure activity in
Wwox−/− mice.**"*

Results (BODY-EXACT): *"Pretreatment of an antiepileptic drug ethosuximide suppressed PTZ-induced
seizure in Wwox−/− mice **(Fig. 7b)**, although ethosuximide pretreatment had no effects on the
behavior changes in Wwox+/+ and Wwox+/− mice treated with a low dose of PTZ."*

**Read from the image**, three stacked genotype sub-panels, arms Control (blue) / PTZ (red) /
PTZ+ETS (green):

| Genotype | N (Ctrl / PTZ / PTZ+ETS) | Ctrl vs PTZ | **PTZ vs PTZ+ETS** | Ctrl vs PTZ+ETS |
|---|---|---|---|---|
| `+/+` | 4 / 20 / 16 | `***` | **`n.s.`** | `***` |
| `+/−` | 5 / 18 / 12 | `***` | **`n.s.`** | `***` |
| `−/−` | 4 / 6 / 6 | `***` | **`***`** | `***` |

- **Treatment:** ethosuximide 150 mg/kg, 45 min pre-PTZ.
- **Observed effect:** suppression of PTZ-evoked Racine score, **significant only in `−/−`**.
- **Genotype-specific?** **Apparently yes** — this panel *is* the genotype-restricted one.
- **Limits — and they matter:** the apparent specificity is **confounded by a floor**. In `+/+`
  and `+/−` the PTZ response itself peaks near stage ~1 on a 0–6 scale; there is almost nothing
  for a drug to suppress. `n.s.` here is consistent with a real absence of effect *and* with an
  effect that the paradigm has no dynamic range to detect. The authors' own phrasing concedes the
  confound — *"treated with a **low dose** of PTZ"*. **No interaction test was performed**, so
  even this panel does not formally establish genotype-dependence of the drug response.

---

## 5. Figure 7d adjudication — LITHIUM

Legend (BODY-EXACT): *"**d Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed
PTZ-induced seizure activity in Wwox−/− mice.** The results are expressed as means ± SEM. n.s.,
non-significant. ***P < 0.001"*

Results (BODY-EXACT): *"Injection of a potent GSK3β inhibitor lithium chloride significantly
suppressed PTZ-induced epileptic seizure in Wwox−/− mice **(Fig. 7d)**."*

**Read from the image at 4× magnification**, three stacked genotype sub-panels, arms PTZ (red) /
PTZ+LiCl (blue):

| Genotype | N (PTZ / PTZ+LiCl) | Control (saline) arm | **PTZ vs PTZ+LiCl** |
|---|---|---|---|
| `+/+` | 12 / 8 | **absent** | **`****`** |
| `+/−` | 12 / 12 | **absent** | **`****`** |
| `−/−` | 6 / 7 | **absent** | **`****`** |

- **Treatment:** LiCl 60 mg/kg i.p. × 3 within 1 h pre-PTZ.
- **Observed effect:** suppression of PTZ-evoked Racine score in **all three genotypes**.
- **Is WT also affected?** **YES — unambiguously.** The wild-type panel carries the same
  four-asterisk marker as the null panel.
- **Limits:**
  - **No saline control arm** in panel d, unlike panel b. The lithium experiment is a two-arm
    comparison; the three-arm structure that anchors panel b is absent.
  - **`****` is undefined in the paper.** The Fig. 7 legend defines only `n.s.` and `***P < 0.001`.
    Programmatic check: the literal string `****` occurs **0 times in the entire XML** — it exists
    *only* as ink in the rendered panel. Fig. 1 defines `*/**/***`; nothing defines a fourth tier.
  - **Text ≠ panel.** Legend and Results both name **only** `Wwox−/−`. The two genotypes where the
    drug also worked are simply not mentioned. This is not a contradiction — it is a **selective
    silence**, and it is the whole reason a caption-only read would invert the conclusion.

### 🔴 The pointer fact, established from the primary

**Figure 7b is the ethosuximide experiment. Figure 7d is the lithium experiment.** Plan asserted
this; I did not take it on that basis. It is confirmed by the figure legend, by the Results
sentence, and by the panels themselves, independently.

### Page-adjudication recipe (CLAUDE.md §5e — publish the derivation, never the derived)

Source `40478_2020_883_Fig7_HTML.png`, sha256 `ced68a66…62542`. Crops written **outside the
repository** (session scratchpad); `.gitignore` excludes adjudication crops by policy. PIL 11.3.0,
`Image.crop(box)` then `resize(w*s, h*s, Image.LANCZOS)`, saved PNG.

| id | crop box (L,U,R,Lo) px | scale | sha256 of crop |
|---|---|---|---|
| `d_WT` | 1330, 560, 1870, 700 | 4× | `3e78668e5a5c6cd2a24f8fd92a5e83ad9e76d6d9b481eeb1d9e04d0ac331ea17` |
| `d_HET` | 1330, 870, 1870, 1010 | 4× | `e604a99eab57b7503e0d78c13c3c6def595404151a3e2a25591c5c2ff671076b` |
| `d_KO` | 1330, 1195, 1870, 1345 | 4× | `4d197ad3e2048ef220ba60e27091bbfd5b7a8f4b7681d3d995effb1c15259780` |
| `b_WT` | 190, 480, 640, 620 | 4× | `6a988a61d62d53ba0f894c50473db156b785129a1f0b4348809b9ded772f0943` |
| `b_HET` | 190, 845, 640, 985 | 4× | `788c33baa2508bad44cbfbd6f9a34fca18f480c4879805a001e183c20f2f8426` |
| `b_KO` | 190, 1195, 640, 1345 | 4× | `ba649d64c9ce9b8415b2492aaa5a9572328f7e45fc0b1d4ce19ced99551ecebb` |

**Re-executed after recording: all six regenerate byte-identically.** The recipe is a command, not
a prose memory.

---

## 6. The three epistemic layers, kept apart

### A. EXPERIMENTAL OBSERVATION (what was measured — no interpretation)

1. `Wwox−/−` mice score higher on the Racine scale after pilocarpine (7a) and after PTZ (7b) than
   `+/+` and `+/−` littermates. SE occurred in ~half of challenged nulls and in **no** `+/+` or
   `+/−` mouse (BODY-EXACT).
2. Spontaneous seizures occur in `Wwox−/−` from ~P12, triggered by noise, strobe light, cage
   change (BODY-EXACT). **These were observed, never used as a drug endpoint.**
3. pGSK3β(Ser9) densitometry falls in `−/−` across cerebellum / hippocampus / cortex
   (2.7 3.1 **1.3** / 3.6 3.5 **2.0** / 3.9 3.8 **2.5**); **total GSK3β is flat**
   (2.2 2.4 2.4 / 2.3 2.4 2.6 / 2.2 2.4 2.6). Measured in **untreated** brain at P20.
4. ETS 150 mg/kg reduces PTZ score significantly in `−/−`; `n.s.` in `+/+` and `+/−`.
5. **LiCl 60 mg/kg reduces PTZ score significantly in `+/+`, `+/−` AND `−/−`.**
6. All of the above by one-way ANOVA; **no interaction term, no repeated-measures model, no
   post-hoc named.**
7. **Not measured:** GSK3β activity (or Ser9 phosphorylation) **in lithium-treated animals**.
   There is no target-engagement readout anywhere in the lithium arm.

### B. AUTHOR INTERPRETATION (what the authors say it means)

- Abstract: *"Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced
  seizure in Wwox−/− mice."* · *"targeting GSK3β with lithium ion ameliorates epilepsy."*
- Results close (BODY-EXACT): *"Together, these results suggest an important role of GSK3β in the
  hypersusceptibility to epileptic seizure induction due to Wwox loss in neuronal cells."*
- Discussion (BODY-EXACT): *"Administration of GSK3β inhibitor lithium chloride effectively
  ameliorated the seizure susceptibility in Wwox−/− mice, and **its efficacy is better than the
  commonly used anticonvulsant drug ethosuximide**."*
- Discussion, closing (BODY-EXACT): *"**Future studies, as well as more evaluations, will be needed
  to test whether GSK3β inhibitors may be promising candidates** for treatment of human
  neurological disorders due to loss or dysfunction of WWOX."*

The authors use "suggest" and defer the therapeutic question. Their own framing is weaker than the
abstract's, and weaker than what downstream representations have made of it.

### C. LEGEND SCIENTIFIC INTERPRETATION (what the evidence licenses)

**What is licensed as `DATO`:**
- `Wwox−/−` mice have a lowered threshold to chemoconvulsants and spontaneous seizures from ~P12.
- GSK3β is **dis-inhibited, not more abundant**, in `Wwox−/−` brain (Ser9 falls, total flat). The
  correct verb is *de-repressed*.
- **Lithium at 60 mg/kg raises the PTZ seizure threshold in mice — all three genotypes.**
- Ethosuximide's suppression reached significance only in `−/−`, in a design with a floor in the
  other two arms and no interaction test.

**What is NOT licensed:**
- That lithium *rescues a WWOX-specific epileptic mechanism*. The comparison that would show it
  was neither designed nor run, and the panel points the other way.
- That the observed benefit is *mediated by GSK3β*. No target engagement was measured.
- Any transfer to **spontaneous** seizures — the phenotype that defines the human disorder.

**Load-bearing premise, tagged.** Every inference of the form *"lithium helps because de-repressed
GSK3β is the target"* rests on a genotype specificity **this experiment did not measure**.
`PREMISE_TAG: PREMISE: DEFAULT_FROM_TEXTBOOK` — the textbook default being *"a drug that rescues a
mutant phenotype acts on the mutated pathway."* That is a research target, not a foundation.

---

## 7. THE CRITICAL QUESTION

> **Does lithium demonstrate rescue of a WWOX-specific epileptic mechanism?**

# ❌ NO.

The three formulations are **not** equivalent, and only the weakest two survive:

| Proposition | Verdict |
|---|---|
| **(i)** Lithium rescues a WWOX-specific epileptic mechanism | ❌ **REFUTED by the paper's own panel.** `Wwox+/+` mice, which have two functioning copies and no WWOX-related mechanism to rescue, respond to lithium with the same significance marker as nulls. A rescue that occurs in animals with nothing to rescue is not a rescue — it is a drug effect. |
| **(ii)** Lithium reduces susceptibility to **PTZ-induced** seizures in this paradigm | ✅ **SUPPORTED**, in all three genotypes. |
| **(iii)** Manipulating a GSK3β-related pathway can alter seizure threshold here | ⚠️ **PARTIALLY / UNDER-DETERMINED.** True only if lithium's effect runs through GSK3β, which was not measured. As stated it is an *interpretation of the intervention*, not an observation. |

**What the experiment actually shows: an anticonvulsant that works, in a model that has seizures.**

The clean internal control is the paper's own comparator. **Ethosuximide** — a T-type Ca²⁺
blocker with no proposed relationship to WWOX — is the arm that behaves *genotype-restrictedly*.
**Lithium** — the arm carrying the mechanistic story — is the one that works everywhere. If
genotype-restricted suppression were the signature of hitting the WWOX-specific mechanism, this
paper assigns that signature to the wrong drug.

---

## 8. TARGET ATTRIBUTION

**Does the experiment establish that lithium's effect is mediated specifically through GSK3β?**
**No.** Separating the four things the design conflates:

| Layer | Established? | Evidence |
|---|---|---|
| **Drug effect** | ✅ Yes | LiCl 60 mg/kg suppresses PTZ Racine score, `****`, all three genotypes (Fig. 7d) |
| **Pathway association** | ✅ Yes, but **correlative and untreated** | pGSK3β(Ser9) ↓ in `−/−` at P20 (Fig. 7c), total GSK3β flat — measured in drug-naive brain |
| **Molecular target attribution** | ❌ **No** | Zero target-engagement readout in treated animals. GSK3β activity was never measured after lithium. |
| **Genotype specificity** | ❌ **No — actively contradicted** | WT responds as strongly as null; no interaction test exists |

Applying the standing LEGEND principle — *a pharmacological rescue does not automatically identify
the molecular target responsible for the rescue* — the two halves of the argument **never meet**:
Fig. 7c measures GSK3β in animals that got no drug; Fig. 7d measures seizures in animals whose
GSK3β was never assayed. The inference bridges them by assumption.

**Lithium is a textbook-pleiotropic agent** and the paper knows it: direct and indirect GSK3
inhibition, **inositol monophosphatase inhibition**, Wnt/β-catenin, myelin gene expression. It is
not a selective GSK3β probe, and no selective GSK3β inhibitor was tested. The minimal
target-attributing experiment — a selective GSK3β inhibitor, or a genetic *Gsk3b* manipulation,
against the same endpoint — is absent.

---

## 9. CAUSAL RELATION — what may be represented

The genotype-specific rescue edge is **not** supportable. Two weaker relations are, if the limits
travel with them.

### Relation 1 — the drug effect (defensible)

| Field | Value |
|---|---|
| **SOURCE CONCEPT** | Lithium chloride (pharmacological agent, 60 mg/kg i.p. × 3 within 1 h) |
| **RELATION** | reduces severity of |
| **TARGET CONCEPT** | PTZ-induced (chemoconvulsant-provoked) seizure activity |
| **PRIMARY EVIDENCE** | PMID 32000863 |
| **LOCATOR** | Figure 7d, all three genotype sub-panels; Results, GSK-3β section, final paragraph |
| **VERBATIM** | *"Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7d)."* |
| **MODEL / SYSTEM** | Mouse, `Wwox+/+`, `Wwox+/−` **and** `Wwox−/−`; preweaning; PTZ 30 mg/kg |
| **CAUSAL LIMIT** | **Not genotype-specific** — significant in wild-type. **Provoked, not spontaneous.** No saline arm in the panel. Significance marker `****` undefined in the paper. One-way ANOVA; no interaction test. |
| **Causal typing** | **`DIRECT`** in the trivial sense that the drug was administered and the endpoint measured. The intermediates are unknown, but no intermediate *node* is being asserted. |

### Relation 2 — the biochemical association (defensible, and it is NOT a rescue edge)

| Field | Value |
|---|---|
| **SOURCE CONCEPT** | WWOX loss of function |
| **RELATION** | is associated with de-repression (Ser9 dephosphorylation) of |
| **TARGET CONCEPT** | GSK3β |
| **PRIMARY EVIDENCE** | PMID 32000863 |
| **LOCATOR** | Figure 7c densitometry row; Results, GSK-3β section |
| **VERBATIM** | *"we determined dephosphorylation of GSK3β at Ser9 (active GSK3β) in Wwox−/− mouse cerebellum, hippocampus and brain cortex by western blotting"* |
| **MODEL / SYSTEM** | Mouse brain, P20, three regions, **drug-naive** |
| **CAUSAL LIMIT** | Correlative and cross-sectional. **Total GSK3β is flat** — the change is in inhibitory phosphorylation, not abundance. Heterozygote is **not** intermediate (sits at/above WT on the phospho blot). |
| **Causal typing** | **`INDIRECT_UNKNOWN_INTERMEDIATES`** |

### Relation 3 — GSK3β → seizure phenotype: **DO NOT FORCE THIS EDGE**

The edge `PP03 → PP13` asserts that the GSK3β arm sits causally upstream of network
hyperexcitability, **and it rests entirely on the lithium result**. That result does not carry it:
the pharmacology is not target-attributed and not genotype-specific. Neither `DIRECT` nor
`INDIRECT_UNKNOWN_INTERMEDIATES` is scientifically justified **from this paper alone** for a
*WWOX-specific* causal arm. `INDIRECT_UNKNOWN_INTERMEDIATES` would be defensible only for the far
weaker statement *"GSK3β dysregulation co-occurs with, and pharmacological GSK3β-directed
intervention modifies, seizure threshold in this model"* — which is not what the edge says.

---

## 10. DISMECH ADJUDICATION

**Local analytical label: _supported but materially requires qualification_ — trending on the node
description toward _stronger than the primary evidence_.**

> **The question that matters: does the structured causal statement preserve the experimental
> limitation visible in the primary evidence?**
>
> **Partially — it preserves two limitations and misses the one that changes the meaning.**

| Limitation visible in the primary | Preserved in DisMech? |
|---|---|
| Provoked (PTZ) ≠ spontaneous seizures | ✅ **Yes**, explicitly, in `limitations` |
| Lithium is not a selective GSK-3β inhibitor | ✅ **Yes**, explicitly |
| GSK3β as druggable node is an open gap | ✅ **Yes** — `KNOWLEDGE_GAP`/`OPEN`, with the right proposed experiment (selective inhibition vs **spontaneous** seizures on video EEG) |
| **The same suppression is significant in `Wwox+/+` and `Wwox+/−`** | ❌ **ABSENT** |
| No target engagement measured in treated animals | ❌ Absent |
| Statistics cannot support genotype-dependence (one-way ANOVA, no interaction) | ❌ Absent |

**Credit where due:** DisMech's entry is *not* naive. It already carries the provoked-vs-spontaneous
caveat and the non-selectivity caveat, and it has an open knowledge gap proposing very nearly the
right experiment. On the standard "does the KB overclaim" test it does better than the review
literature does.

**But the missing limitation is the load-bearing one, and here is precisely why.** The two
recorded limitations both weaken *how far the result generalises* — from provoked to spontaneous
seizures, from lithium to GSK3β. Neither touches **whether the result is about WWOX at all.** The
wild-type arm does. With it, the reader learns that this is an anticonvulsant effect observed in a
seizure model. Without it, `direction: ABOLISHED` on a readout named *"Induced-seizure onset after
GSK-3beta inhibition"*, attached to a node whose description says the arm *"carries its own
pharmacological test"*, reads as a mechanism-specific rescue. **The phrase "its own pharmacological
test" is doing the overclaiming**: the test is presented as what separates this arm from merely
correlated biochemistry, and it is exactly the test that does not discriminate.

**Compounding factor:** the node evidence is **abstract-sourced** (§2.3, verified). DisMech is
quoting the surface on which the limitation is invisible. This is not curator error — it is a
structural property of abstract-level evidence, and it is the strongest available argument for
panel-level evidence as a curation surface. It is also worth noting that LEGEND's own outbound
sidecar exports **nothing** for this paper (both `CLAIM 016` occurrences terminate at
`LINK_ROLE_NON_SUPPORTING`, `locator_status: NOT_EXTRACTED`), so the qualification LEGEND holds is
currently not reaching DisMech through the export path either.

**Recommended qualification (analysis only — not a repository edit):** add to
`animal_models[0].modeled_mechanisms[1].limitations`:

> *"The same suppression of PTZ-induced seizure activity was significant in `Wwox+/+` and
> `Wwox+/−` littermates (Fig. 7d), so the experiment does not establish a WWOX-specific
> pharmacological rescue. GSK3β activity was not measured in lithium-treated animals; the
> comparator ethosuximide, by contrast, was non-significant in `+/+` and `+/−` (Fig. 7b). The
> paper reports one-way ANOVA only, with no genotype × treatment interaction test."*

---

## 11. LEGEND CANONICAL POINTER DEFECT — confirmed independently

I confirm the defect **from the primary artifact**, not from Plan.

**FILE:** `disease-models/wwox/registries/claim_registry_current.md`, `CLAIM 016`, the
*🔴 Evidence boundary* block (line 300 as read at `main` `788c357`).

**CURRENT FORM** (verbatim):

> …registra che **il litio ha soppresso le crisi da PTZ in TUTTI E TRE i genotipi, wild-type
> incluso** (Fig. 7b; per l'etosuccimide il testo dichiara `n.s.` in `+/+` e `+/−` e significativo
> in `−/−`, e per il litio **non dichiara il converso**).

**PROPOSED FORM:**

> …registra che **il litio ha soppresso le crisi da PTZ in TUTTI E TRE i genotipi, wild-type
> incluso** (**Fig. 7d**; per l'etosuccimide — **Fig. 7b** — il testo dichiara `n.s.` in `+/+` e
> `+/−` e significativo in `−/−`, e per il litio **non dichiara il converso**).

**WHY.** A single parenthesis carries two different experiments and labels both with one figure
number. Figure 7b is the **ethosuximide** panel; Figure 7d is the **lithium** panel. The pointer
therefore sends a verifying reader to the panel that appears to **contradict** the claim it is
attached to: at Fig. 7b they find `n.s.` in `+/+` and `+/−` — textbook genotype specificity — and
conclude the claim's central assertion is false. **The claim's substance is correct and its
citation refutes it.** That is worse than a typo: it is a pointer that converts a correct
correction into apparent error under exactly the scrutiny the correction was written to invite.

**PRIMARY LOCATORS** (all BODY-EXACT against sha256 `792b5b29…f00f5`):
- *"d Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice."* — Fig. 7 legend, panel d
- *"Pretreatment of ethosuximide (ETS, 150 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice."* — Fig. 7 legend, panel b
- *"Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7d)."* — Results
- *"Pretreatment of an antiepileptic drug ethosuximide suppressed PTZ-induced seizure in Wwox−/− mice (Fig. 7b), although…"* — Results
- Panel adjudication recipe: §5 above, six crops, all regenerate.

**CLASSIFICATION:** candidate for lawful later integration via **`BATCH_COMMIT`**. Change class
**MINOR** — pointer correction only; no claim status, conclusion or epistemic tag changes.
`CLAIM 016` remains `in observation`. **I did not perform the edit.** The claim registry is one of
the four canonical current files and changes only through `BATCH_COMMIT`.

**Secondary observation (lower severity), reported not repaired.** In
`deepdive_manifests/PMID32000863.json`, entry `[0]` states the proposition *"READ FROM THE IMAGE,
NOT THE TEXT: lithium suppressed PTZ-induced seizures in ALL THREE genotypes…"* while declaring
`surface: "body"`, `panel_text_relation: "text_only"`, `artifact: …_PMC.xml`. Its quote is the
*caption*, which does not contain the three-genotype finding. The properly surfaced locator does
exist — entry `[22]`, `surface: figure`, `panel_only`, artifact `…Fig7_HTML.png` — and it already
records *"each carries its own **** significance bracket"*, which I independently re-derived at 4×
before reading it. So the evidence is correctly anchored **somewhere**; entry `[0]` is a duplicate
whose declared surface contradicts its own proposition. Worth a manifest hygiene pass; it does not
affect the adjudication.

---

## 12. NEGATIVE EVIDENCE / COUNTER-EVIDENCE

The negative evidence **is** the result here. Actively sought, against the attractive reading:

1. 🔴 **Wild-type responds to lithium.** `Wwox+/+`, PTZ N=12 vs PTZ+LiCl N=8, `****`. Decisive. An
   animal with two intact *Wwox* alleles has no WWOX-related mechanism to rescue.
2. 🔴 **The heterozygote responds too** (N=12 vs 12, `****`) — no genotype gradient of any kind.
3. 🔴 **The authors cite prior work that lithium is anticonvulsant in ordinary mice.** Discussion,
   BODY-EXACT: *"Administration of lithium in mice has been demonstrated to attenuate PTZ-induced
   clonic seizure [10]"*. **The paper contains its own refutation of specificity, in its own
   Discussion, one sentence after the claim it undercuts.** Lithium's PTZ effect was already known
   in wild-type mice; the paper's WT panel reproduces it.
4. 🔴 **No target engagement.** GSK3β activity was never measured in a lithium-treated animal.
5. 🔴 **No selective GSK3β probe.** Only lithium — and the paper's own Discussion lists its Wnt,
   β-catenin/myelin and remyelination actions **in this very system**, all plausible confounds.
6. 🔴 **PTZ-provoked ≠ the disease phenotype.** The paper documents *spontaneous* seizures from P12
   triggered by noise, strobe and handling (BODY-EXACT) — and **never tests lithium against them.**
   The endpoint that would matter clinically was available and not used.
7. 🔴 **Statistics cannot support genotype-dependence.** One-way ANOVA, no interaction term, no
   post-hoc named, parametric test on ordinal Racine data, repeated measures treated as
   independent.
8. 🔴 **`****` is undefined** — zero occurrences in the XML; the legend defines only up to `***`. A
   reader cannot recover the threshold that was applied to the decisive panel.
9. 🔴 **No saline arm in Fig. 7d**, though Fig. 7b has one. The lithium panel is the weaker design
   of the two, and it is the one carrying the mechanistic claim.
10. ⚠️ **Text/panel asymmetry.** Legend and Results name only `Wwox−/−` for lithium. The Discussion
    then asserts lithium's *"efficacy is better than… ethosuximide"* — a cross-experiment
    comparison between arms with different control structures, different N and different
    pre-treatment schedules, for which **no test is reported.**
11. ⚠️ **The comparator inverts the expected pattern.** Ethosuximide, mechanistically unrelated to
    WWOX, is the genotype-restricted arm; lithium, the mechanistic candidate, is not.
12. ⚠️ **Floor effect cuts both ways.** The `n.s.` results in the `+/+`/`+/−` ETS arms are
    themselves weakly supported — low-dose PTZ leaves little dynamic range. This *protects* the
    lithium finding rather than undermining it: for lithium to reach significance in the same
    low-ceiling wild-type arm makes the WT effect more striking, not less.
13. ℹ️ **Small and unequal N in the null arms** (6–7) versus 8–20 in controls; ANOVA across
    markedly unbalanced groups without a stated correction.

**No observation was found that supports genotype-specific lithium rescue.** The search was run in
both directions; this direction came back empty.

---

## BRAINSTORMING / HYPOTHESIS SPACE

*Separated deliberately. Nothing below modifies the verdict above. Every item is `IPOTESI` or
`INFERENZA`; none is `DATO`.*

**On GSK3β** — `INFERENZA`: the de-repression is real, residue-mapped elsewhere
(`CLAIM 035` / Wang 2012, L404 docking motif), and **S9-independent** — which means a Ser9 western
is the *wrong assay* for WWOX-driven GSK3β activity and the Fig. 7c readout may under-report it.
`IPOTESI`: a direct kinase-activity readout (substrate phosphorylation, e.g. CRMP2/Tau) in
lithium-treated `Wwox−/−` brain is the missing target-engagement measurement, and it is cheap.

**On Wnt** — `ESPANSIONE`: lithium's Wnt/β-catenin arm is an equally good explanation for the
seizure-threshold shift and is *not excluded*. The paper itself notes lithium rescues Wnt-dependent
cerebellar midline fusion — a phenotype this model has. `IPOTESI`: a Wnt-null-but-GSK3β-active
probe would separate the two arms.

**On seizure threshold** — `IPOTESI`: the cleanest reading of Fig. 7d is that lithium raises
seizure threshold **generically**, and the `Wwox−/−` brain simply sits closer to that threshold
because it is structurally malformed. This is the *amplifier-not-driver* reading already carried in
`CLAIM 016`, and Fig. 7d is consistent with it — arguably better evidence for it than for the
GSK3β-arm reading.

**WWOX-specific vs generic anticonvulsant** — `IPOTESI`: the discriminating experiment is not more
lithium. It is **a selective GSK3β inhibitor (or conditional *Gsk3b* manipulation) tested in all
three genotypes with an explicit genotype × treatment interaction test**, against **spontaneous**
seizures on video-EEG. Note this is very nearly what DisMech's own `KNOWLEDGE_GAP` already
proposes — the gap is well posed; only the node's confidence is out of step with it.

**On therapeutic testing** — `IPOTESI`, and it must stay one: none of this is a repurposing
signal. Under the Track C gate (function · *signed* direction · proximal Tier 1/2 readout · CNS
paediatric safety), this node fails at least two — direction is unsigned because target
attribution failed, and no proximal readout exists. Lithium in a paediatric DEE population carries
a serious risk profile (renal, thyroid, narrow therapeutic index, interaction with dehydration
during seizures), and a genuinely non-specific anticonvulsant effect is a **weaker** rationale than
a specific one, not a stronger one.

**A methodological hypothesis worth its own line** — `INFERENZA`: this case is a strong argument
that **abstract-sourced evidence and panel-level evidence are not interchangeable curation
surfaces.** Every limitation DisMech captured is stated in the paper's *text*; the one it missed
exists only as ink in a *panel*. That is a predictable, structural blind spot, not bad luck — and
it is testable: sample other DisMech entries whose evidence is abstract-sourced and check whether
their missing qualifications are also panel-resident.

---

## SUCCESS CONDITION — the two answers, stated flat

**WHAT DID THE EXPERIMENT ACTUALLY SHOW?**
That lithium chloride at 60 mg/kg raises the threshold to PTZ-provoked seizures in mice —
**significantly in wild-type, heterozygous and Wwox-null animals alike** — in a two-arm design with
no saline control, no measurement of GSK3β in treated animals, an undefined significance marker,
and statistics (one-way ANOVA) incapable of testing genotype-dependence. Separately and in
untreated brain, GSK3β is de-repressed in Wwox-null mice via loss of Ser9 phosphorylation, with
total protein unchanged.

**HOW STRONG A CAUSAL STATEMENT DOES THAT EVIDENCE LICENSE?**
Only: *"lithium reduces chemoconvulsant-provoked seizure severity in this mouse model, in a manner
that is **not** genotype-specific and **not** attributed to GSK3β."* It licenses **no** WWOX-specific
pharmacological rescue, **no** target attribution to GSK3β, and **no** transfer to spontaneous
seizures. The mechanistic edge from the GSK3β arm to the seizure phenotype is **not** carried by
this experiment, and the current DisMech representation — despite carrying two of the three
relevant caveats — does not preserve the limitation that decides the question.

---

*Non-canonical. Nothing here is medical advice. No canonical file was modified in producing it.*
