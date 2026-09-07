---
record: PILOT SCIENTIFIC ADJUDICATION
id: PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_SCIB_v1
pilot: G-1
actor: scientist-b (NOT ACTIVATED — operator-directed analytical session; no TASK_ACK, no lease,
  `roles/scientist.md` deliberately not activated and no authority traced to it)
date: 2026-08-25
worktree: .claude/worktrees/lettore-b
branch: lettore-b
head: fb31c2a172c2c5dcb5f54ad5cd28ef12d78b6da9
object: PMID 32000863 (Cheng et al. 2020) · WWOX → GSK-3β → seizure → lithium
status: NON-CANONICAL PILOT ARTIFACT — analytical only. Mutates no registry, no claim, no
  paper record, no Pathograph, no DisMech file, no Scientist contract, no governance file,
  no canonical hypothesis.
independence: written without reading Scientist A's output for this task, and without reading
  the Plan crosswalk. Every statement Plan is reported to have made was re-derived from the
  primary artifact or from the upstream DisMech source before being used.
---

# Pilot G-1 — what the lithium experiment in PMID 32000863 actually shows

> **Bottom line, stated before the evidence so it can be checked against it.** The lithium
> experiment does **not** demonstrate rescue of a WWOX-specific epileptic mechanism, and it does
> not identify GSK-3β as the molecule through which lithium acts. Figure 7d shows lithium
> suppressing PTZ-provoked seizure activity **significantly in all three genotypes, wild-type
> included**, with the wild-type effect detected using *fewer* animals than the wild-type
> ethosuximide comparison that returned `n.s.` The paper's own cited support for the effect
> (ref. 10) reports it in ordinary mice and attributes it to α2-adrenoceptor involvement, not to
> GSK-3β. The strongest proposition the experiment licenses is: *systemic lithium pretreatment
> raises the threshold for PTZ-provoked seizure in this paradigm, irrespective of Wwox genotype.*
>
> **Nothing here is medical advice.** Lithium is a drug with a narrow therapeutic index; nothing
> in this document supports its use in any patient.

---

## 1 · Worktree / source state, measured

### 1.1 This tree

| Fact | Measured value | How |
|---|---|---|
| Working directory | `<REPO_ROOT>/.claude/worktrees/lettore-b` | `pwd` |
| Branch | `lettore-b` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `fb31c2a172c2c5dcb5f54ad5cd28ef12d78b6da9` (2026-08-25T00:20:22+02:00) | `git rev-parse HEAD` |
| vs local `main` (`788c357`) | **3 ahead, 0 behind** | `git rev-list --left-right --count main...HEAD` → `0  3` |
| vs `origin/main` (`8ab8e4b`) | **458 ahead, 0 behind**; `origin/main` is an ancestor of HEAD | `git merge-base --is-ancestor origin/main HEAD` → YES |
| Last fetch of the shared object store | 2026-08-24T14:24:28 | `stat` on `FETCH_HEAD` in the common git dir |
| Uncommitted | one untracked file, `reviews/scientist-b/SCIENTIST_OPERATING_PRACTICE_DISCOVERY_SCIB_v1.md` | `git status --porcelain` |

No fast-forward was owed before measuring. `origin/main` is 458 commits behind HEAD and contains
none of the work read here; the public remote is not the current canonical surface and was not
used as one.

### 1.2 LEGEND scientific surfaces, and their state

`framework/state/state_manifest_current.md` → `current_state: READY`, `framework_version: v3.3.1`,
`working_model_version: WM_v4.3`, `last_batch_commit_id: BATCH_20260815_001` (2026-08-15).

`python3 framework/scripts/legend_lint.py .` → **VERDICT: PASS** (one `[INFO]`, CLAIM 010 wikilink
not required for a `background only` claim).

Surfaces read for this adjudication, all at `fb31c2a`:

- `disease-models/wwox/registries/claim_registry_current.md` — CLAIM 016 (canonical, `in observation`)
- `disease-models/wwox/registries/fulltext_read_receipts.jsonl` — receipt `FTR-20260804-32000863-01`
- `disease-models/wwox/research/deepdive_manifests/PMID32000863.json` — 25 locators, schema v2
- `disease-models/wwox/analysis/data/dismech_sidecar_016_024_035.jsonl` — the export sidecar
- `framework/state/state_manifest_current.md` — §4 batch scope records

### 1.3 A measured local absence, declared as local

The receipt `FTR-20260804-32000863-01` names `files/fulltext/PMID32000863_Cheng2020_PMC.xml`, and
the manifest additionally names the supplementary PDF and two figure PNGs. **None of those files
exists in this worktree.** `files/` is in `.gitignore` (privacy hard-guard, line 8), so evidence
artifacts do not travel with a worktree checkout.

I state this as a property of *this tree*, not of the system. The artifacts do exist in the shared
checkout at `<REPO_ROOT>/files/fulltext/`, and were read from there. This
is the same class the manifest's own note names — *"the manifest survived, the evidence did not
travel with it"* — observed a second time, from the receiving side.

### 1.4 Artifact identity, verified rather than assumed

| Artifact | SHA-256 | Verified against |
|---|---|---|
| `PMID32000863_Cheng2020_PMC.xml` (PMC6990504, JATS) | `792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5` | **matches** `source_fingerprint` in receipt `FTR-20260804-32000863-01` |
| `PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png` (1946×1627) | `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542` | recorded here; the manifest declares the artifact but carries no digest for it |
| `PMID32000863_Cheng2020_supplementary.pdf` | `0acb771cfe3a4c3644b41c10451504047adb715e69727c1889f72774151f8b7f` | recorded here |

A second, independently retrieved copy of the same article exists at
`~/Desktop/Claude Workspace/staging/fulltext_xml_20260705/32000863_PMC6990504.xml` with a
**different** digest (`7d235c00…`, 158 798 bytes vs 156 335). Two PMC snapshots of one article taken
a month apart are not byte-identical; the receipt's fingerprint identifies *which* snapshot was
read, and that is the one used here. This is not a discrepancy in content — it is the reason the
fingerprint is worth carrying.

**Figure surface used.** All panel-level statements below were read from the rendered PNG at native
1946×1627 and at crops magnified 2.2–3×, not from the caption and not from the running text. Where
the panel and the text differ, the difference is recorded rather than normalised.

---

## 2 · The current DisMech assertion, recovered from the upstream source

Plan's paraphrase was not used. The entry was recovered directly.

**Source of record.** `monarch-initiative/dismech`, default branch `main`,
`kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml`.

| Field | Value |
|---|---|
| Entry name | `WWOX-Related Developmental and Epileptic Encephalopathy` |
| Disease term | `MONDO:0014533` — developmental and epileptic encephalopathy, 28 |
| Synonyms | WOREE syndrome · WWOX-related epileptic encephalopathy · DEE28 · EIEE28 |
| Blob SHA (git) | `d61eff6b37de0c280908c269814b798065e32959`, 90 354 bytes, 1 772 lines |
| SHA-256 of my retrieved copy | `332e72e8897ad8a9618783c5e70a8f382ad3ba5b87bcad37ef30640265b0c1ff` |
| Only commit touching the file | `4ca217ff336e`, 2026-08-19T23:58:06Z — *"curate(WWOX DEE28/WOREE): new entry with four de-bundled mechanism arms (#8986)"* |
| Retrieved | 2026-08-25, repo `pushed_at` 2026-08-25T08:28:18Z |

The GSK-3β material occupies **four** distinct positions in the entry. All four are reproduced
verbatim, because the adjudication turns on which of them carries the limitation.

### 2.1 Pathophysiology node (line 126)

```yaml
- name: Wnt/GSK-3beta Signalling Dysregulation
  biological_scale: MOLECULAR
  description: >-
    WWOX loss produces significantly increased activation of glycogen synthase kinase
    3beta across cerebral cortex, hippocampus and cerebellum in Wwox-null mice. This
    arm is separated from the others because it carries its own pharmacological test:
    inhibiting GSK-3beta with lithium abolishes induced seizures in these animals.
  biological_processes:
  - preferred_term: Wnt signaling pathway
    term: { id: GO:0016055, label: Wnt signaling pathway }
    modifier: DYSREGULATED
  evidence:
  - reference: PMID:32000863
    supports: SUPPORT
    evidence_source: MODEL_ORGANISM
    snippet: "Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced seizure in Wwox-/- mice."
    explanation: >-
      The pharmacological result that makes this a causal arm for seizures rather
      than a correlated biochemical change.
  downstream:
  - target: Neocortical Network Hypersynchrony
    causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES
    description: >-
      GSK-3beta inhibition suppresses induced seizures, placing this arm upstream of
      network-level hyperexcitability; the intervening steps are not mapped.
```

**Limitation present at this node: none.** This is the position that carries the causal edge to the
seizure phenotype, and it is the position with no caveat field.

### 2.2 The upstream edge into the node (line 107)

```yaml
  downstream:
  - target: Wnt/GSK-3beta Signalling Dysregulation
    causal_link_type: DIRECT
    description: >-
      Loss of the WWOX hub releases GSK-3beta from normal restraint.
```

Source node: `Loss of WWOX Scaffold Function`. Relationship type: `DIRECT`.

### 2.3 Animal-model arm (line 1090) — **where the limitation actually lives**

```yaml
  - target: Wnt/GSK-3beta Signalling Dysregulation
    relationship: RECAPITULATES
    fidelity: MODERATE
    description: >-
      The only node in this pathograph with a pharmacological intervention attached:
      GSK-3beta activation rises, and inhibiting it with lithium abolishes induced
      seizures.
    limitations: >-
      The rescue was measured against pentylenetetrazol-*induced* seizures, not the
      spontaneous seizures that define the human disease, so it establishes that this
      arm can gate seizure threshold rather than that it drives the clinical epilepsy.
      Lithium is also not a selective GSK-3beta inhibitor.
    readouts:
    - name: GSK-3beta activation in brain
      direction: INCREASED
      snippet: "We determined that a significantly increased activation of glycogen synthase kinase 3β (GSK3β) occurs in Wwox-/- mouse cerebral cortex, hippocampus and cerebellum."
    - name: Induced-seizure onset after GSK-3beta inhibition
      direction: ABOLISHED
      interpretation: >-
        Lithium abolishes the onset of PTZ-induced seizures in Wwox-null mice.
      snippet: "Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced seizure in Wwox-/- mice."
```

Model: `Wwox-null mouse (germline knockout)`, `publication: PMID:32000863`, described as *"the only
pharmacological test of a druggable node in the pathograph."*

### 2.4 Knowledge-gap discussion (line 1676)

```yaml
- discussion_id: gap_gsk3b_as_a_druggable_node
  kind: KNOWLEDGE_GAP
  status: OPEN
  attaches_to: [ "pathophysiology#Wnt/GSK-3beta Signalling Dysregulation" ]
  rationale: >-
    … The rescue was measured against pentylenetetrazol-induced seizures - a provoked-threshold
    assay - whereas the human disease is defined by spontaneous, drug-resistant seizures, and a
    compound can raise a chemical seizure threshold without touching established epileptogenic
    networks. Lithium is also not a selective GSK-3beta inhibitor, so the experiment licenses
    "GSK-3beta inhibition raises seizure threshold in this model" rather than identifying lithium
    as the agent. …
  proposed_experiments:
  - name: Selective GSK-3beta inhibition against spontaneous seizures
```

### 2.5 Snippet fidelity — checked, not assumed

Every DisMech snippet drawn from PMID 32000863 was matched against the fingerprinted XML:

| Snippet (opening) | Verdict |
|---|---|
| "Inhibition of GSK3β by lithium ion significantly abolishes…" | present — differs only in `Wwox-/-` vs the source's superscripted `Wwox −/−` |
| "We determined that a significantly increased activation…" | present — same markup-rendering difference |
| "Together, our findings reveal that the neurodevelopmental…" | **exact** |
| "Cerebral malformations, such as microcephaly…" | present — same markup-rendering difference |
| "Here, we report that targeted disruption of Wwox gene…" | **exact** |
| "Degenerative alterations including severe hypomyelination…" | **exact** |

**DisMech quotes the source honestly.** No snippet is fabricated, drifted or trimmed to change
meaning. Everything problematic below is about *what the quoted sentences license*, never about
whether they were quoted correctly. The `Wwox-/-` / `Wwox −/−` divergence is the same
transcription-versus-extraction class already documented in the LEGEND manifest's own audit note.

---

## 3 · Primary evidence reconstruction

**Cheng Y-Y, Lai F-J, et al. (2020)** *Wwox deficiency leads to neurodevelopmental and degenerative
neuropathies and glycogen synthase kinase 3β-mediated epileptic seizure activity in mice.*
Acta Neuropathol Commun 8:6. DOI `10.1186/s40478-020-0883-3`. PMC6990504. National Cheng Kung
University. Section titles, Methods, Results, Discussion, all seven main figures and all nine
supplementary figures were available; Additional file 2 (seizure video) was not retrieved.

### 3.1 Design of the seizure experiments (Methods, *Induction of seizure*)

| Element | As stated |
|---|---|
| Convulsants | pilocarpine 50 mg/kg i.p. (with methylscopolamine 1 mg/kg 30 min prior); PTZ 30 mg/kg i.p. |
| Ethosuximide | 150 mg/kg i.p., **45 min before** PTZ. Described as *"a T-type Ca²⁺ channel blocker that has anticonvulsant activity"* |
| Lithium | *"LiCl (i.p., 60 mg/kg) were pretreated **three times within 1 h** before PTZ injection."* → cumulative ≈180 mg/kg (~4.2 mEq/kg) in the hour before challenge |
| Readout | modified Racine scale, stages 0–6, scored for 60 min |
| Statistics | *"one-way analysis of variance (ANOVA) to compare the difference among groups"*; significance at P<0.05; means ± SEM |
| **Age at seizure testing** | **not stated anywhere in this section** |

The abstract describes the animals as "preweaning". The Methods for the seizure experiments give no
age. Elsewhere the paper works at P14–P20, and the nulls die within weeks; but for the experiment
being adjudicated the age is simply absent from the record.

### 3.2 Figure 7 as a whole

| Panel | Content |
|---|---|
| **7a** | Pilocarpine 50 mg/kg vs saline control, three genotypes, 60 min Racine trace. **No drug-rescue arm.** |
| **7b** | PTZ 30 mg/kg ± ethosuximide, three genotypes, three groups per panel |
| **7c** | Western blot: pGSK3β(Ser9), total GSK3β, Wwox, β-actin across cerebellum / hippocampus / cortex × three genotypes |
| **7d** | PTZ 30 mg/kg ± LiCl, three genotypes, **two** groups per panel |

**Lithium was tested in the PTZ model only.** It was never tested against pilocarpine, and never
against the spontaneous seizures the paper reports from P12 onward (Additional file 2, a video;
never quantified, no EEG anywhere in the paper).

### 3.3 Figure 7 legend — the full significance key

> *"The results are expressed as means ± SEM. n.s., non-significant. \*\*\* P < 0.001"*

That is the entire key. The string `****` occurs **zero times** in the extracted text of the whole
article, including every figure legend.

### 3.4 Figure 7c, read from the image

Densitometry printed under the blots, across `+/+ · +/− · −/−`:

| Blot | Cerebellum | Hippocampus | Cortex |
|---|---|---|---|
| **pGSK3β (Ser9)** | 2.7 · **3.1** · 1.3 | 3.6 · **3.5** · 2.0 | 3.9 · **3.8** · 2.5 |
| **total GSK3β** | 2.2 · 2.4 · 2.4 | 2.3 · 2.4 · 2.6 | 2.2 · 2.4 · 2.6 |

Three things the panel shows and the text does not say:

1. **Total GSK-3β is flat.** What falls in the null is the *inhibitory* Ser9 phosphorylation. The
   kinase is **dis-inhibited, not more abundant**.
2. **The heterozygote is not intermediate.** On the phospho blot `+/−` sits *at or above* `+/+` in
   every one of the three regions. There is no gene-dosage gradient.
3. **The panel carries no statistics at all** — one lane per genotype per region, no error bars, no
   n, no significance marker. The legend says *"representative results of four independent
   experiments"* and reports no quantification across them.

Yet the abstract states a *"significantly* increased activation"* — and that is the sentence
DisMech quotes as the biochemical readout. **The word "significantly" is not backed by any
displayed test.**

### 3.5 A text discrepancy inside the Methods

Methods, *Western blotting*: tissues *"isolated from three genotypes of mice at **postnatal day
14**"*. Figure 7c legend: *"at **postnatal day 20**"*. Both cannot describe the same blot. Minor,
but it is a discrepancy between the artifact's own two statements of the same fact, and it is not
recorded on any LEGEND surface.

---

## 4 · Figure 7b — adjudication

**Panel locator:** Figure 7b, `40478_2020_883_Fig7_HTML.png`, sha256 `ced68a66…`, three stacked
genotype panels in the lower-left quadrant, read at 2× magnification of the native image.

| | |
|---|---|
| **Treatment** | PTZ 30 mg/kg i.p.; ethosuximide 150 mg/kg i.p. 45 min before PTZ |
| **Groups per panel** | three — Control (saline), PTZ, PTZ+ETS |
| **Genotypes** | `+/+`, `+/−`, `−/−`, one panel each |

**Group sizes, read from the panel legends:**

| Genotype | Control | PTZ | PTZ + ETS |
|---|---|---|---|
| `+/+` | 4 | 20 | 16 |
| `+/−` | 5 | 18 | 12 |
| `−/−` | 4 | 6 | 6 |

**Significance brackets, read from the panel** (nested: an outer bracket spanning Control↔PTZ+ETS,
an inner upper bracket Control↔PTZ, an inner lower bracket PTZ↔PTZ+ETS):

| Genotype | Control vs PTZ | **PTZ vs PTZ+ETS** | Control vs PTZ+ETS |
|---|---|---|---|
| `+/+` | \*\*\* | **n.s.** | \*\*\* |
| `+/−` | \*\*\* | **n.s.** | \*\*\* |
| `−/−` | \*\*\* | **\*\*\*** | \*\*\* |

**Observed effect.** Ethosuximide reduces PTZ-provoked seizure severity to a statistically
detectable degree **only in the null**. In wild-type and heterozygote the ETS trace is
indistinguishable from PTZ alone.

**Is the effect genotype-specific?** **Yes, as displayed.** This is the panel in the paper that
shows a genotype-restricted drug effect.

**Limits.**
- In `+/+` and `+/−` the PTZ response itself peaks at Racine ≈1.0–1.3, leaving little dynamic range;
  a **floor effect** is a live alternative to genotype specificity. Against that reading: the WT ETS
  comparison is the best-powered drug comparison in the whole figure (20 vs 16 animals) and still
  returns `n.s.`, so this is not simply an underpowered cell.
- `Control vs PTZ+ETS` remains `***` in the null: the rescue is **partial**, not normalisation.
- No genotype × treatment interaction test is shown anywhere. "Significant here and not there" is
  not a test of a difference between the two.
- One-way ANOVA is declared for a 60-min repeated-observation time series. The unit of analysis
  (animal, or animal-timepoint) is not stated and no repeated-measures structure or multiplicity
  correction is named.

---

## 5 · Figure 7d — adjudication

**Panel locator:** Figure 7d, same artifact and digest, three stacked genotype panels in the
lower-right quadrant, read at native resolution and at 3× on each legend/bracket region.

| | |
|---|---|
| **Treatment** | PTZ 30 mg/kg i.p.; LiCl 60 mg/kg i.p. ×3 within the preceding hour |
| **Groups per panel** | **two** — PTZ, PTZ+LiCl. **There is no saline control arm.** |
| **Genotypes** | `+/+`, `+/−`, `−/−`, one panel each |

**Group sizes and brackets, read from the panel legends:**

| Genotype | PTZ | PTZ + LiCl | **PTZ vs PTZ+LiCl** |
|---|---|---|---|
| `+/+` | 12 | 8 | **\*\*\*\*** |
| `+/−` | 12 | 12 | **\*\*\*\*** |
| `−/−` | 6 | 7 | **\*\*\*\*** |

**Observed effect.** Lithium pretreatment lowers the PTZ-provoked Racine trace in every genotype,
with a significance bracket printed on **all three** panels.

**Is wild-type also affected?** **Yes — decisively, and at the same marked significance level as the
null.** The wild-type effect is not a marginal residue: it is detected with 8 lithium-treated
animals, whereas the ethosuximide comparison in the same genotype returned `n.s.` with 16. **Fewer
animals, stronger result.** A power artifact cannot explain the difference between panel b and
panel d in wild-type; the two drugs genuinely behave differently in the control genotype.

**Magnitude, for completeness.** The absolute suppression *is* larger in the null — the `−/−` PTZ
trace peaks near Racine 3.5–4 and falls to ≈1.0–1.6 under LiCl, whereas the `+/+` PTZ trace peaks
near 1.3 and falls toward 0.2–0.5. But no test compares those magnitudes, and a larger absolute drop
from a higher baseline is what any effective anticonvulsant would produce in the sicker group.

**Limits.**
- **No untreated control arm.** Panel b has one; panel d does not. Without it, "abolishes the onset"
  cannot be evaluated against baseline — only against PTZ alone.
- **`****` is undefined.** The figure legend defines `n.s.` and `*** P < 0.001` and nothing more; the
  string `****` appears nowhere in the article text. The most significant marker in the panel that
  anchors the paper's therapeutic claim has no declared meaning.
- **No cross-genotype comparison and no interaction test.**
- **No target engagement.** pGSK3β(Ser9) was never measured in a lithium-treated animal. Figure 7c
  is untreated mice; there is no post-treatment blot anywhere in the paper or supplement.
- **Confound intrinsic to the readout.** The Racine scale scores motor behaviour. ≈180 mg/kg LiCl
  delivered i.p. within one hour is a high acute load, and acute lithium is sedating and
  hypolocomotor. On a motor-behavioural scale, sedation and a raised seizure threshold are not
  distinguishable. No locomotor, temperature or serum-lithium control is reported. *(Analytical
  inference, mine — the paper neither raises nor excludes it.)*
- **Unequal and unexplained group sizes** (`+/+` 12 vs 8), with no allocation or blinding statement
  anywhere in the Methods.

---

## 6 · The three layers, kept apart

### A · EXPERIMENTAL OBSERVATION — what was measured

1. In untreated `Wwox−/−` mice at P14 or P20 (the two surfaces disagree), pGSK3β(Ser9) densitometry
   is lower than in `+/+` and `+/−` in cerebellum, hippocampus and cortex; total GSK3β densitometry
   is flat across all genotypes and regions. One lane per condition, no statistics. `+/−` is not
   intermediate.
2. `Wwox−/−` mice reach higher Racine scores after PTZ 30 mg/kg and after pilocarpine 50 mg/kg than
   `+/+` and `+/−` littermates; half progress to status epilepticus, which is never seen in the
   control genotypes.
3. Ethosuximide 150 mg/kg reduces the PTZ trace significantly in `−/−` only; `n.s.` in `+/+` and
   `+/−`. Rescue in `−/−` is partial (still `***` vs control).
4. LiCl 60 mg/kg ×3 reduces the PTZ trace with a `****` bracket in **all three** genotypes.
5. No group in the paper received lithium without PTZ; no group received PTZ without a genotype
   comparator in panel d; no biochemical measurement was made in any lithium-treated animal.
6. Spontaneous seizures are reported from P12 in `−/−`, evidenced by a video, never quantified,
   never subjected to any drug.

### B · AUTHOR INTERPRETATION — what the authors say it means

| Locator | Verbatim |
|---|---|
| Abstract | *"Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced seizure in Wwox−/− mice."* |
| Abstract, closing | *"…targeting GSK3β with lithium ion ameliorates epilepsy."* |
| Results, GSK-3β section, final ¶ | *"Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7 d)."* |
| Results, same ¶ | *"Together, these results suggest an important role of GSK3β in the hypersusceptibility to epileptic seizure induction due to Wwox loss in neuronal cells."* |
| Discussion, penultimate ¶ | *"Administration of GSK3β inhibitor lithium chloride effectively ameliorated the seizure susceptibility in Wwox−/− mice, **and its efficacy is better than the commonly used anticonvulsant drug ethosuximide**."* |
| Discussion, closing | *"Future studies, as well as more evaluations, will be needed to test whether GSK3β inhibitors may be promising candidates for treatment of human neurological disorders due to loss or dysfunction of WWOX."* |
| Discussion | *"Whether lithium treatment can rescue the deficits in neuronal migration and differentiation during development in Wwox−/− mice remains to be studied."* |

Two properties of this layer matter.

- **The authors' statements about panel d are true and incomplete.** Every one of them is restricted
  to `Wwox−/−`. None of them is false. None of them mentions that the same bracket is printed on the
  wild-type panel. *Incomplete is not false* — which is exactly why a downstream reader who never
  opens the image inherits a genotype-specific result that the panel does not support.
- **The comparative claim has no supporting test.** *"Its efficacy is better than … ethosuximide"*
  compares two separate experiments, run on separate cohorts, with different group sizes, and — panel
  d having no saline arm — without even a shared baseline. No ETS-vs-LiCl bracket exists anywhere.
  And the comparison runs *against* the paper's own thesis: ethosuximide is the drug that behaves
  genotype-selectively here; lithium is the one that does not.

### C · LEGEND SCIENTIFIC INTERPRETATION — what the evidence licenses

**Licensed:**

- `L1` — In this constitutive null, the inhibitory Ser9 phosphorylation of GSK-3β is reduced across
  three brain regions while total kinase is unchanged. **Dis-inhibition, not over-abundance.**
  Weakened by: no statistics, single lanes, P14/P20 discrepancy, whole-animal null, no cell-type
  resolution.
- `L2` — `Wwox−/−` mice have a lowered threshold to two mechanistically distinct convulsants and
  show spontaneous seizures. Robust; two independently targeted knockout strains agree.
- `L3` — **Systemic lithium pretreatment raises the threshold for PTZ-provoked seizure in this
  paradigm, irrespective of Wwox genotype.** This is the strongest formulation panel d supports.
- `L4` — Ethosuximide's effect in this paradigm is detectable only in the null, i.e. the paper does
  contain a genotype-restricted pharmacological observation — **for the comparator drug**, and it is
  a partial rescue.

**Not licensed:**

- ✗ *"Lithium rescues a WWOX-specific epileptic mechanism."* Contradicted by the wild-type panel.
- ✗ *"Lithium's effect identifies GSK-3β as the responsible target."* No selectivity control, no
  target engagement, no alternative-inhibitor arm. See §7.
- ✗ *"GSK-3β dis-inhibition drives the seizure phenotype."* The biochemistry and the pharmacology are
  never joined by an experiment; they are joined by a sentence.
- ✗ *"Lithium ameliorates the epilepsy of this model."* The disease-defining phenotype — spontaneous,
  recurrent seizures — was never treated.
- ✗ *"Lithium is more effective than ethosuximide."* No test exists.
- ✗ Any statement resting on `+/−` being mechanistically intermediate. On the only relevant blot it
  is not.

---

## 7 · The critical question, and target attribution

> **Does lithium demonstrate rescue of a WWOX-specific epileptic mechanism?**

**No.** The experiment demonstrates the weaker proposition: *lithium reduces susceptibility to
PTZ-induced seizures* — in Wwox-null, Wwox-heterozygous **and wild-type** mice alike. The
genotype-specificity that would make it a mechanism-directed rescue is absent from the panel that is
supposed to establish it, and the paper never claims it in words — it simply never reports the
control-genotype result.

These three propositions are not equivalent and this document does not treat them as such:

| # | Proposition | Status against this evidence |
|---|---|---|
| P1 | Lithium reduces susceptibility to PTZ-induced seizures | **SUPPORTED**, in all three genotypes |
| P2 | Manipulating a GSK-3β-related pathway can alter seizure threshold in this paradigm | **NOT ESTABLISHED** — no manipulation specific to that pathway was performed |
| P3 | Lithium rescues a WWOX-specific epileptic mechanism | **NOT SUPPORTED**, and the panel argues against it |

Note carefully that P2 is *not* free. DisMech's gap discussion concludes that the experiment
*"licenses 'GSK-3beta inhibition raises seizure threshold in this model' rather than identifying
lithium as the agent."* That inverts the inferential direction. What the experiment holds fixed is
**the drug**; what it never varies or verifies is **the target**. It therefore licenses a statement
about lithium and not a statement about GSK-3β. P2 requires either a second, structurally unrelated
GSK-3β inhibitor, or a demonstration that lithium engaged Ser9 phosphorylation in the treated
animals. Neither exists.

### 7.1 What was and was not experimentally linked

| Layer | Established here? | Evidence |
|---|---|---|
| **Drug effect** | ✅ yes | Fig 7d, `****` in all three genotypes |
| **Pathway association** | ⚠️ correlative only | Fig 7c — untreated animals, no statistics, no link to the drug arm |
| **Molecular target attribution** | ❌ **no** | no selectivity control, no second inhibitor, no post-treatment pGSK3β(Ser9), no genetic epistasis |
| **Genotype specificity** | ❌ **no, for lithium** | wild-type panel carries the same marker |

### 7.2 The paper's own citation argues against its attribution

This is the sharpest piece of counter-evidence in the article, and it is in the Discussion, three
sentences after the claim it undercuts:

> *"Administration of lithium in mice has been demonstrated to attenuate PTZ-induced clonic seizure
> [10], and rescue Wnt-dependent cerebellar midline fusion and neurogenesis deficits early in
> development [38]. Lithium treatment has also been shown to induce β-catenin-mediated myelin gene
> expression in mouse Schwann cells and enhance remyelination of the injured peripheral nerves in
> mice [47]."*

Reference **[10]** resolves to: **Bahremand A, et al. (2011)** *Additive anticonvulsant effects of
agmatine and lithium chloride on pentylenetetrazole-induced clonic seizure in mice: **involvement of
α2-adrenoceptor***. Eur J Pharmacol 666:93–99, PMID 21651904.

So the paper cites, in support of its own lithium result, a study that (i) reports the same
anticonvulsant effect in **ordinary mice with no Wwox lesion**, and (ii) attributes it
mechanistically to **α2-adrenoceptor involvement, not GSK-3β**. The prior literature the authors
themselves invoke establishes both that the effect is Wwox-independent and that a competing target
has been proposed for it.

References [38] and [47] compound this: they document lithium acting on Wnt-dependent cerebellar
midline fusion and on β-catenin-mediated myelination — two processes independently disrupted in this
same mouse. Lithium's pleiotropy is not a hypothetical objection here; it is documented in the
paper's own bibliography, in this exact tissue.

**LEGEND principle applied:** *a pharmacological rescue does not automatically identify the molecular
target responsible for the rescue.* This is a textbook instance — and one where the paper supplied,
without noticing, the citation that makes the point.

---

## 8 · Causal relation — what, if anything, is representable

### 8.1 Relations the primary supports

**RELATION A — biochemical (supportable, qualified)**

| Field | Value |
|---|---|
| SOURCE CONCEPT | Constitutive germline `Wwox` loss (whole-animal null) |
| RELATION | reduces inhibitory Ser9 phosphorylation of GSK-3β without changing total GSK-3β abundance |
| TARGET CONCEPT | GSK-3β dis-inhibition (kinase activity state) |
| PRIMARY EVIDENCE | PMID 32000863 |
| LOCATOR | Figure 7c, `40478_2020_883_Fig7_HTML.png` sha256 `ced68a66…`, densitometry row read at 3× |
| VERBATIM | *"Increased activation of GSK3β was determined in the cerebellum, hippocampus and cerebral cortex of Wwox−/− mice at postnatal day 20, as evidenced by dephosphorylation of GSK3β at Ser9."* (Fig. 7 legend, panel c) |
| MODEL / SYSTEM | Mouse, `Wwox−/−` germline KO, brain tissue, P14 or P20 (sources disagree) |
| CAUSAL LIMIT | Correlative in a whole-animal null. Single lane per condition, **no statistics of any kind**, so the abstract's "significantly" is unsupported by the panel. Heterozygote not intermediate. Cannot separate neuronal-autonomous from non-autonomous. Physical WWOX–GSK-3β inhibition is established elsewhere (Wang 2012, PMID 22193544), **not here**. |
| CAUSAL TYPE | `INDIRECT_UNKNOWN_INTERMEDIATES` |

**RELATION B — pharmacological (supportable, and it is not a disease-mechanism edge)**

| Field | Value |
|---|---|
| SOURCE CONCEPT | Systemic LiCl pretreatment (60 mg/kg i.p. ×3 within 1 h) |
| RELATION | reduces PTZ-provoked seizure severity **irrespective of Wwox genotype** |
| TARGET CONCEPT | PTZ-provoked seizure severity (Racine 0–6 over 60 min) |
| PRIMARY EVIDENCE | PMID 32000863 |
| LOCATOR | Figure 7d, three stacked genotype panels, per-panel `****` brackets |
| VERBATIM | *"d Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice."* (Fig. 7 legend — the caption names only the null; the panel marks all three) |
| MODEL / SYSTEM | Mouse, `+/+`, `+/−` and `−/−`, PTZ 30 mg/kg i.p., age not stated |
| CAUSAL LIMIT | No untreated control arm. `****` undefined in the legend. No cross-genotype or interaction test. No target engagement. Motor-scale readout cannot separate anticonvulsant action from acute lithium sedation. Effect present in wild-type ⇒ **carries no information about WWOX biology**. |
| CAUSAL TYPE | `DIRECT` in the trivial sense that a drug was given and a behaviour changed — but the source concept is *the compound*, not a disease node, so this relation does not belong in a disease pathograph at all. |

### 8.2 The relation DisMech asserts, and why neither governed type fits it

DisMech's load-bearing edge is:

> `Wnt/GSK-3beta Signalling Dysregulation` → `Neocortical Network Hypersynchrony`,
> `causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES`

**Neither `DIRECT` nor `INDIRECT_UNKNOWN_INTERMEDIATES` is scientifically justified for this edge on
the strength of PMID 32000863**, and I decline to pick one.

The reason is structural, not a matter of degree. Both governed types presuppose that the **source
node is the cause** and differ only in whether the path between source and target is mapped.
`INDIRECT_UNKNOWN_INTERMEDIATES` says *"we know the cause, we do not know the route."* What this
experiment leaves unknown is **the identity of the source node itself** — whether GSK-3β is the
molecule through which lithium acted. There is no governed type for *"the intervention worked and we
have not established what it worked on,"* and inventing one is outside this pilot's remit. Recording
the edge as `INDIRECT_UNKNOWN_INTERMEDIATES` reads to any consumer as *"GSK-3β causes the
hyperexcitability by an unmapped route,"* which is more than the evidence says.

**What the evidence does support** is the pathway edge as a **correlated biochemical arm** —
relation A — with the pharmacology recorded separately as a non-specific observation, not as the
thing that makes the arm causal.

---

## 9 · DisMech adjudication

**Local analytical label (this document only, not repository vocabulary):**

### 9.1 Node-level verdicts

| DisMech position | Verdict | Why |
|---|---|---|
| §2.3 **animal-model arm** (`limitations` field) | **supported but materially requires qualification** | The two limitations it states are correct and were independently confirmed: PTZ-provoked ≠ spontaneous, and lithium is not selective. What it omits is the decisive one — the same suppression is significant in wild-type. Its readout `direction: ABOLISHED` also overstates a partial suppression measured with no baseline arm. |
| §2.4 **knowledge-gap discussion** | **supported but materially requires qualification** | The best-reasoned position in the entry. But its conclusion — that the experiment licenses *"GSK-3beta inhibition raises seizure threshold in this model"* — is the one thing the experiment does **not** license, because the target was never verified. It correctly refuses to credit lithium and then credits GSK-3β instead, which is the same unearned attribution with the label moved. |
| §2.2 **`Loss of WWOX Scaffold Function` → `Wnt/GSK-3beta Dysregulation`, `DIRECT`** | **primary evidence points to a different formulation** | Defensible from Wang 2012 (physical inhibition, residue-resolved), **not** from PMID 32000863, which shows only an abundance/phospho correlation in a whole-animal null with no statistics. If PMID 32000863 is the cited evidence, `DIRECT` is stronger than it supports. |
| §2.1 **pathophysiology node + its downstream edge** | 🔴 **stronger than the primary evidence** | See below. |

### 9.2 The load-bearing finding

> **The current structured causal statement does not preserve the experimental limitation visible in
> the primary evidence — at the one position where the limitation would change what a consumer
> concludes.**

DisMech does hold the limitation. It holds it in the `animal_models` block and in the `discussion`
block. **It does not hold it on the pathophysiology node, and the pathophysiology node is where the
causal edge to the seizure phenotype lives.**

The node's `description` reads:

> *"This arm is separated from the others because it carries its own pharmacological test: inhibiting
> GSK-3beta with lithium abolishes induced seizures in these animals."*

and its evidence `explanation` reads:

> *"The pharmacological result that makes this a causal arm for seizures rather than a correlated
> biochemical change."*

That second sentence is the exact inferential step the experiment does not support. The lithium
result **cannot** promote this arm from correlation to causation, because the identical result occurs
in animals with two intact `Wwox` alleles and normal Ser9 phosphorylation. A manipulation that
produces the same outcome in the presence and in the absence of the lesion is, definitionally, not
evidence that the lesion's arm is causal. The node states that it is — with no `limitations` field,
because the pathophysiology schema position has none.

Three consequences follow, and each is checkable:

1. **The caveat does not travel with the edge.** Any consumer that reads the pathograph — the node,
   its `description`, its evidence and its `downstream` edge — receives the promotion-to-causal
   claim and none of the qualification. The qualification is two schema blocks away, attached to a
   *model*, not to the *mechanism*.
2. **The stated limitations are the second and third most important ones, not the first.** *Provoked
   vs spontaneous* and *lithium is not selective* are both real. But an entry could satisfy both and
   still be wrong in the same way, because neither says the control genotype responded.
3. **The pathograph's pharmacological anchor is on the wrong drug.** The animal-model block calls
   this *"the only node in this pathograph with a pharmacological intervention attached."* In the
   primary, the intervention with a genotype-restricted effect is **ethosuximide** — which appears
   nowhere in the DisMech entry. The entry curated the drug the authors promoted, not the drug whose
   panel shows specificity.

### 9.3 Proposed qualification (analysis only — not an edit, and not mine to make)

Were the entry to be corrected, the minimal change that would preserve the limitation at the load-
bearing position is to replace the node's causal-promotion `explanation` with something like:

> *The pharmacological result is reported for this arm, but Figure 7d prints the same significance
> bracket on the wild-type and heterozygous panels as on the null. Lithium therefore raises the
> PTZ threshold irrespective of genotype and does not, on its own, promote this arm from a
> correlated biochemical change to a causal one. No post-treatment measurement of GSK-3β Ser9
> phosphorylation was made, so target engagement is unverified.*

DisMech is a Monarch-maintained resource; correcting it is a pull request under their review, not an
act available to this document. Recorded here as a finding for the integrator to route.

---

## 10 · LEGEND canonical pointer defect — independently confirmed

Plan reports one defective pointer. **I confirm the defect and find it in two places, and the
correction is not the one a naive read of Plan's report would produce.**

Verified directly from the artifact: **Figure 7b is the ethosuximide experiment; Figure 7d is the
lithium experiment.** Confirmed three ways — the Results text (*"Pretreatment of an antiepileptic
drug ethosuximide suppressed PTZ-induced seizure in Wwox−/− mice (Fig. 7 b)"* … *"lithium chloride
significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7 d)"*), the figure
legend (`b` = ETS, `d` = LiCl), and the panels themselves (7b: three groups incl. saline control,
green ETS trace; 7d: two groups, blue LiCl trace).

Sweep of the tracked tree at `fb31c2a` for a `Fig 7b` pointer, any spacing (`git grep -nE`): four
hits. One is correct (`deepdive_manifests/PMID32000863.json:89`, the ethosuximide locator, which
properly cites 7b). Two carry the defect. One is the manifest's own summary note.

### DEFECT 1 — canonical scientific file

**FILE:** `disease-models/wwox/registries/claim_registry_current.md`, line 300, CLAIM 016,
`🔴 Evidence boundary` block, propagated by `BATCH_20260810_005`.

**CURRENT FORM** (exact substring):

> `(Fig. 7b; per l'etosuccimide il testo dichiara `n.s.` in `+/+` e `+/−` e significativo in `−/−`, e per il litio **non dichiara il converso**)`

**PROPOSED FORM:**

> `(Fig. 7d; per l'etosuccimide — esperimento distinto, **Fig. 7b** — il testo dichiara `n.s.` in `+/+` e `+/−` e significativo in `−/−`, e per il litio **non dichiara il converso**)`

**WHY.** The sentence this parenthesis closes is *"il litio ha soppresso le crisi da PTZ in TUTTI E
TRE i genotipi, wild-type incluso"* — the **lithium** observation, which is Figure **7d**. The
pointer says 7b, which is the **ethosuximide** experiment.

The parenthesis then bundles a *second* observation under the same pointer — the ethosuximide
`n.s.`/significant pattern — and for that clause `Fig. 7b` is **correct**. **A bare `7b → 7d` swap
would repair the first clause and break the second.** The proposed form splits the two pointers.
This is the practical difference between correcting a pointer and re-reading the sentence it points
from.

**PRIMARY LOCATOR.** Figure 7d, `files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png`,
sha256 `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542`, native 1946×1627, three
stacked genotype panels each bracketing PTZ against PTZ+LiCl with `****`; `+/+` N = 12 vs 8,
`+/−` N = 12 vs 12, `−/−` N = 6 vs 7. Source XML sha256 `792b5b29…` (PMC6990504), receipt
`FTR-20260804-32000863-01`.

**CLASSIFICATION.** Candidate for lawful later integration via `BATCH_COMMIT`. `claim_registry_current.md`
is one of the four scientific current files and changes only through a gated batch. **No edit was
made by this document.**

### DEFECT 2 — state-control file, same error, not previously reported

**FILE:** `framework/state/state_manifest_current.md`, line 112, `batch_20260810_005_scope`.

**CURRENT FORM** (exact substring):

> `lithium suppressed PTZ seizures in ALL THREE genotypes including wild-type (PMID 32000863 Fig 7b, read from the image), so the experiment does not establish a WWOX-specific pharmacological rescue.`

**PROPOSED FORM:**

> `lithium suppressed PTZ seizures in ALL THREE genotypes including wild-type (PMID 32000863 Fig 7d, read from the image), so the experiment does not establish a WWOX-specific pharmacological rescue.`

**WHY.** Same error, same origin — the batch record and the claim it propagated repeat one another,
so the defect was duplicated at propagation time rather than introduced twice. Here there is no
ethosuximide clause, so the correction is a clean `7b → 7d`.

**PRIMARY LOCATOR.** As above.

**CLASSIFICATION.** The manifest is the one state-control file updatable outside a `BATCH_COMMIT`
(§0 of that file). But this string is the historical scope record of a *completed* batch, and
silently rewriting what a past batch said is a different act from updating current state. **I
recommend an in-place correction with an explicit inline marker** (e.g. `Fig 7d [corrected
2026-08-2x from "Fig 7b"; see PILOT_PMID32000863…SCIB_v1 §10]`) rather than either a silent rewrite
or leaving a known-false pointer in the record. That choice is the integrator's and the operator's,
not mine, and no edit was made.

### What this pair says about propagation

The three-genotype observation was captured correctly at reading time — the deepdive manifest's Fig
7d locators are right, including the note that entry 0 is deliberately `text_only` because the
caption is *true but incomplete*. The pointer degraded **between the manifest and the two records
that cite it**, and it degraded identically in both, because one was written from the other. The
reading was sound; the transport was not. That is the same failure class the manifest itself names
one paragraph earlier about a different field.

---

## 11 · Negative and counter-evidence

Collected deliberately, because the attractive interpretation here is unusually attractive: a rare
disease, a druggable node, an approved drug.

| # | Observation | Locator | Weight |
|---|---|---|---|
| N1 | **Lithium suppresses PTZ seizures in wild-type mice at the same marked significance as in nulls** | Fig 7d, `+/+` panel, `****`, N = 12 vs 8 | ⛔ **Decisive** against genotype specificity |
| N2 | Wild-type lithium effect is detected with **8** treated animals; the wild-type ethosuximide comparison returns `n.s.` with **16** | Fig 7b vs 7d legends | Removes "underpowered control genotype" as an explanation |
| N3 | The paper's own ref. **[10]** (Bahremand 2011, PMID 21651904) reports lithium attenuating PTZ clonic seizure in **ordinary mice** and attributes it to **α2-adrenoceptor** | Discussion, final substantive ¶ | ⛔ Undercuts both Wwox-dependence and GSK-3β attribution, from the paper's own bibliography |
| N4 | Refs [38] and [47] document lithium acting on Wnt-dependent cerebellar midline fusion and on β-catenin-mediated myelination — **both independently disrupted in this same mouse** | Discussion, final substantive ¶ | Pleiotropy is documented in this tissue, not hypothetical |
| N5 | **No post-treatment pGSK3β(Ser9) measurement.** Target engagement never demonstrated | absent from Figs 1–7 and Suppl. Figs S1–S9 | ⛔ No target attribution possible |
| N6 | **Figure 7d has no untreated control arm** — unlike 7b | Fig 7d, two groups per panel | "Abolishes the onset" is not evaluable against baseline |
| N7 | **`****` is undefined.** Legend gives only `n.s.` and `*** P < 0.001`; the string `****` occurs **0** times in the article text | Fig 7 legend; full-text scan | The marker anchoring the therapeutic claim has no declared threshold |
| N8 | **Figure 7c carries no statistics** — single lanes, no error bars, no n, no marker — yet the abstract says *"significantly* increased activation"*, and that sentence is DisMech's quoted biochemical readout | Fig 7c, image | Text↔panel disagreement on the *only* biochemical evidence |
| N9 | **Total GSK-3β is flat** (2.2/2.4/2.4 · 2.3/2.4/2.6 · 2.2/2.4/2.6). CLAIM 016's `Summary` still says *"GSK3β is elevated"* | Fig 7c densitometry | LEGEND's own Summary describes abundance where the panel shows dis-inhibition; the claim block's later `Meccanismo aggiunto` already corrects this, the `Summary` line does not |
| N10 | **Heterozygote is not intermediate** on the phospho blot — `+/−` sits at or above `+/+` in all three regions | Fig 7c densitometry | No gene-dosage gradient; any dosage reasoning on this node is unfounded |
| N11 | **Lithium was never tested against spontaneous seizures**, which are the disease-defining phenotype; nor in the pilocarpine model | Fig 7a has no rescue arm; Movie S1 never quantified, no EEG anywhere | Provoked-threshold assay ≠ established epileptogenic network |
| N12 | Racine is a **motor-behavioural** scale and ≈180 mg/kg LiCl in one hour is a high acute load; acute lithium is sedating. No locomotor, temperature or serum-lithium control | Methods, *Induction of seizure* | Sedation and threshold elevation are not separable on this readout *(my inference; paper is silent)* |
| N13 | *"its efficacy is better than … ethosuximide"* — **no head-to-head test exists**; separate cohorts, different N, no shared baseline | Discussion, penultimate ¶ | An unsupported comparative claim in the sentence that motivates the therapeutic proposal |
| N14 | Methods say western-blot tissue at **P14**; Fig 7c legend says **P20** | Methods *Western blotting* vs Fig 7 legend | Internal discrepancy on the age of the only biochemical measurement |
| N15 | **Age of the seizure-experiment animals is never stated** | Methods, *Induction of seizure* | Unrecorded in the primary and on every LEGEND surface |
| N16 | One-way ANOVA declared for 60-min repeated-observation traces; unit of analysis unstated, no repeated-measures structure, no multiplicity correction, no blinding or allocation statement | Methods, *Statistical analysis* | Applies to every panel of Figure 7 |

**Disagreements between text and panel, itemised:** N1 (caption names only `−/−`; panel marks all
three), N7 (`****` printed, never defined), N8 ("significantly" asserted, never tested), N9/N10
(abundance language over a dis-inhibition panel with no dosage gradient), N14 (P14 vs P20).

**Counter-weight, stated fairly.** The paper is otherwise strong and internally controlled: two
independently targeted knockout strains were built specifically to exclude an aberrant product of a
retained exon 1, and they agree on every behavioural measure. The seizure hypersusceptibility itself
(`L2`) is well supported across two mechanistically distinct convulsants. The weakness is confined
to the pharmacological layer — and that layer is precisely the one the downstream knowledge graph
promoted to a causal arm.

---

## 12 · Candidate graph representation

**Recommendation: do not add a new edge from this paper. Qualify the existing one.**

Representable, if the integrator chooses to carry it:

```
NODE   Wwox loss (constitutive germline null, mouse)
  --[ INDIRECT_UNKNOWN_INTERMEDIATES ]-->
NODE   GSK-3β dis-inhibition (reduced Ser9 phosphorylation, total kinase unchanged)
       evidence  PMID:32000863 · Figure 7c · MODEL_ORGANISM
       limits    no statistics on the panel; single lanes; P14/P20 discrepancy;
                 heterozygote not intermediate; whole-animal null; cell type unresolved;
                 physical WWOX–GSK-3β inhibition is Wang 2012 (PMID 22193544), not this paper
```

**Not representable from this paper:**

```
NODE   GSK-3β dis-inhibition  --[ ??? ]-->  NODE  seizure phenotype
```

Neither `DIRECT` nor `INDIRECT_UNKNOWN_INTERMEDIATES` is justified (§8.2). The only experiment
offered for this edge produces the same result in animals without the lesion, and never verifies
that lithium engaged the named target. **If this edge is carried, it must be carried as an
untested hypothesis, not as a causal link supported by a pharmacological rescue.**

Separately, and outside the pathograph:

```
OBSERVATION  Systemic LiCl (60 mg/kg ×3 i.p.) reduces PTZ-provoked Racine severity
             in Wwox +/+, +/− and −/− mice alike
             PMID:32000863 · Figure 7d · genotype-independent
             ⇒ a general anticonvulsant observation; carries no WWOX-specific information
```

---

## BRAINSTORMING / HYPOTHESIS SPACE

**Everything below is `IPOTESI` or `INFERENZA`. None of it modifies any verdict above, and no item
here is evidence for anything.**

1. **`IPOTESI` — the specificity signal in this paper is on the wrong drug.** Ethosuximide, not
   lithium, shows the genotype-restricted effect (`n.s.` in `+/+` and `+/−`, `***` in `−/−`). If that
   survives a properly powered replication with an interaction test, the mechanistically interesting
   lead here is **T-type Ca²⁺ channel dependence** of the Wwox-null seizure phenotype — a hypothesis
   the paper generated and then walked past on its way to GSK-3β. *Test:* ETS dose–response in all
   three genotypes with a formal genotype × treatment term.

2. **`IPOTESI` — the decisive missing experiment is cheap and already specified.** A single western
   blot for pGSK3β(Ser9) in LiCl-treated `−/−` and `+/+` brain would convert "lithium worked" into
   "lithium engaged the target," or falsify it. It requires no new model and no new reagent.

3. **`IPOTESI` — a selectivity arm would separate drug from target.** A structurally unrelated
   GSK-3β inhibitor with CNS exposure (e.g. a tideglusib-class or CHIR-class compound, dose-matched
   for target engagement) run in the same PTZ paradigm across all three genotypes. If the
   genotype-independent pattern reproduces, the effect is anticonvulsant, not mechanistic; if a
   genotype-restricted effect appears, the lithium panel was confounded — plausibly by sedation.

4. **`INFERENZA` — the endpoint, not the drug, is what needs changing.** PTZ threshold is a
   *provoked* assay. DisMech's own proposed experiment (selective GSK-3β inhibition against
   spontaneous seizures on continuous video-EEG in the neuronal-deletion model) is the right shape.
   Worth adding to it: score locomotor activity in parallel, so that a sedative floor cannot be read
   as an anticonvulsant ceiling.

5. **`IPOTESI` — Wnt/β-catenin may matter here for a reason unrelated to seizures.** The paper's own
   refs [38] and [47] have lithium rescuing Wnt-dependent cerebellar midline fusion and driving
   β-catenin-mediated myelination — and this mouse has defective cerebellar midline fusion *and*
   CNS/PNS hypomyelination. The pleiotropy that ruins the seizure attribution is, from another angle,
   a **developmental** hypothesis the paper explicitly leaves open (*"Whether lithium treatment can
   rescue the deficits in neuronal migration and differentiation … remains to be studied"*). That is
   a different experiment with a different endpoint and a different therapeutic window — early,
   developmental, structural — and it should not borrow credibility from the seizure panel.

6. **`IPOTESI` — the heterozygote question, reframed.** `+/−` is not intermediate on pGSK3β(Ser9)
   (N10) and is indistinguishable from wild-type on every quantified developmental measure in the
   supplement, yet the manifest records a Tc-MEP **latency** signal in `+/−` statistically
   indistinguishable from the null while amplitude is normal (Fig 2b–c). If that dissociation
   replicates, the carrier readout is **electrophysiological, not biochemical** — and it says the
   GSK-3β arm is not the one that reports haploinsufficiency.

7. **`INFERENZA` — generic vs specific anticonvulsant mechanisms, as a modelling stance.** A
   compound that raises seizure threshold in wild-type animals is, for a disease model, a
   *symptomatic* lever and not a mechanistic one. The two should not occupy the same node type. The
   distinction is worth carrying explicitly in any WWOX therapeutic representation, because a
   mechanism-shaped node with a symptomatic drug attached is exactly how an attractive but unearned
   therapeutic rationale enters a knowledge graph.

8. **`IPOTESI` — therapeutic testing, stated with its own limits.** Nothing here supports lithium in
   WWOX-DEE. Its narrow therapeutic index, its documented pro-convulsant role in the
   lithium–pilocarpine model, and the absence of any test against spontaneous seizures are three
   independent reasons a positive PTZ panel in mice does not travel. LEGEND's own dismissal record
   `DIS-009` already rejected the adjacent safety argument. If a GSK-3β-directed hypothesis is ever
   pursued, it should be pursued with a selective agent, against spontaneous seizures, with target
   engagement measured — i.e. the three things this experiment did not do.

---

## Appendix · Reproduction

```bash
# state
git -C .claude/worktrees/lettore-b rev-parse HEAD                    # fb31c2a…
python3 framework/scripts/legend_lint.py .                            # VERDICT: PASS

# artifact identity
shasum -a 256 files/fulltext/PMID32000863_Cheng2020_PMC.xml           # 792b5b29… == receipt
shasum -a 256 files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png
#                                                                       ced68a66…

# upstream DisMech entry
gh api "repos/monarch-initiative/dismech/contents/kb/disorders/\
WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml" --jq '.content' | base64 -d
# blob d61eff6b37de0c280908c269814b798065e32959 · commit 4ca217ff336e (2026-08-19)

# the pointer defect (this file is excluded so that recording the negative does not falsify it)
git grep -nE "Fig\.? ?7 ?b" -- . ':!reviews/scientist-b/PILOT_PMID32000863*'
#   → claim_registry_current.md:300          DEFECT 1
#   → state_manifest_current.md:112          DEFECT 2
#   → deepdive_manifests/PMID32000863.json:89   correct (ethosuximide locator)
#   → deepdive_manifests/PMID32000863.json:280  manifest summary note
```

**Denominators, stated.** The `Fig 7b` sweep runs over **tracked files at `fb31c2a` only**. It does
not cover `files/` (gitignored), untracked working files, other worktrees, or any branch other than
this one. Four hits out of the tracked tree; two are defects. No claim is made about surfaces this
sweep does not reach.
