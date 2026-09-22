# PRE-REGISTRATION — Johannsen 2018 (PMID 29808465) Methods retrieval

> **Discovery-space artefact.** `HYPOTHESIS ≠ CLAIM`. Nothing here is canonical.
> **Not medical advice.** Reasons about a reference WWOX-DEE genotype class, not any person.
> Primitive: `preregister_prediction`. Written and committed **before** the full text is retrieved.

---

## 1 · Why this paper, and why now

Two independent censuses this session concluded the same thing: the reagent and chemistry evidence
for the Q230P molecular-state question **is not in the repository** (0 of 81 manifests name a
detergent; 0 record a pellet step; 11 mention an antibody and none a catalogue number). The
instruction to *classify by actual chemical recipe, not the word RIPA* therefore has to go to the
papers' Methods.

**Baseline enumeration then found something larger.**

| Artefact | State |
|---|---|
| `deepdive_manifests/PMID29808465.json` | 🔴 **does not exist** — not among the 81 |
| `reading_state.md:98` | 🔴 **`abstract_only` · read** |
| receipts | one carries `reread_reason: inadequate_prior_coverage` |

**PMID 29808465 is the primary functional source for Q230P** — two homozygous sisters, patient
fibroblasts, *qRT-PCR transcript normal + Western blot protein not detected*, with the authors
leaving **impaired translation** and **premature degradation** both open. It is cited by
`PAPER 041` and load-bearing in the claim registry.

🔴 **The canonical status `MOLECULAR FATE UNRESOLVED` currently rests on an abstract.** Its Methods
have never been read. That is not a criticism of the grading — `abstract_only` is recorded
honestly, and the `PREMISE: DETECTION_FLOOR` note already refuses to read *not detected* as
*absent*. It means the highest-information available action is to read the Methods.

---

## 2 · The question

*Does Johannsen 2018's Methods section contain the chemistry needed to distinguish* **H3
post-translational degradation** *from* **H4 insolubility/misfolding** *— and if not, what is the
narrowest experiment that would?*

This matters because the two route to different interventions. If the Q230P species is degraded,
the target is turnover. If it partitions into a pellet the lysate discarded, the protein was
**present and never loaded onto the gel** — a different problem entirely, and one where "not
detected" is an artefact of fractionation rather than a measurement of abundance.

---

## 3 · EX-ANTE PREDICTIONS — with falsifiers

| # | Prediction | Falsifier |
|---|---|---|
| **P1** | **No pellet / insoluble-fraction analysis** is reported. The post-spin pellet is discarded unexamined. | Any resuspension, denaturing re-solubilisation or pellet blot is described. |
| **P2** | The lysis buffer is either **unnamed**, or named **without full detergent composition**; no SDS/urea/guanidine denaturing recovery step appears. | A complete recipe with a strong denaturant is stated. |
| **P3** | The **immunoblot detection floor is not quantified** — no dilution series, no recombinant standard, no stated LOD. | Any explicit sensitivity limit is reported. |
| **P4** | **No measurement of synthesis rate** — no pulse-label, no puromycin, no polysome fractionation. So "impaired translation" is offered as an alternative the paper **did not test**. | Any synthesis-rate measurement is present. |
| **P5** | The antibody is identified by **vendor at most**, with its **epitope region not stated**. | The epitope or immunogen region is given. |

## 4 · The consequence, pre-stated so it cannot be retrofitted

- **If P1 ∧ P2 hold:** *protein not detected* **cannot discriminate H3 from H4** in this source.
  The canonical `MOLECULAR FATE UNRESOLVED` is then not merely cautious but **exactly right**, and
  it cannot be narrowed from this paper at all. The therapeutic branch in §20 of the operator
  brief stays unselected — and that is a result, not a stall.
- **If P1 is falsified** (a pellet was examined): that is the highest-value datum in the corpus for
  this question and changes the next experiment immediately.
- **If P4 is falsified**: "impaired translation" becomes a tested alternative rather than an open
  one, which would narrow the state map by one hypothesis.

🔴 **Scoring rule, fixed now:** each prediction gets `SUPPORTED` / `REFUTED` / `AMBIGUOUS` /
`UNTESTED`. If the full text proves unobtainable, every prediction is scored **`UNTESTED`** and
none is quietly dropped. Retrieval failure is not evidence for a prediction.

---

## 5 · RESULT

### 5.1 Retrieval outcome: **BLOCKED**, and the distinction matters

| Route | Outcome | What it establishes |
|---|---|---|
| PubMed MCP `convert_article_ids` | **no PMCID** | authoritative: the article is **not in PMC** |
| Unpaywall (`api.unpaywall.org`) | `curl (56) CONNECT tunnel failed, response 403` | 🔴 **transport blocked by this environment's network policy** |
| Europe PMC (`ebi.ac.uk`) | same 403 tunnel failure | 🔴 **transport blocked** |

🔴 **Only the first row is evidence about the paper.** The other two say nothing whatever about
whether an open copy exists — they say this container is not permitted to ask. Recording a blocked
request as "not available" would be the same error class as §6's self-matching `pgrep`: reporting a
property of the instrument as a property of the subject.

### 5.2 Predictions: all **`UNTESTED`** — none dropped, none inferred

| # | Prediction | Score |
|---|---|---|
| P1 | no pellet / insoluble fraction examined | **`UNTESTED`** |
| P2 | no full detergent composition | **`UNTESTED`** |
| P3 | detection floor not quantified | **`UNTESTED`** |
| P4 | no synthesis-rate measurement | **`UNTESTED`** |
| P5 | epitope region not stated | **`UNTESTED`** |

🔴 **The scoring rule fixed in §4 is honoured exactly: retrieval failure is not evidence for a
prediction.** I expected P1–P5 to hold, and I still do — and that expectation is worth nothing, so
it is not recorded as support. Had this been scored after the fact, the temptation to write "the
predictions are almost certainly right" would have been strong and would have been unfalsifiable.

### 5.3 🎯 What was obtained anyway — `NEW DETAIL`, from metadata alone

Retrieval failed; the cycle did not. The PubMed record carries indexer-assigned MeSH terms that the
abstract does not mention:

> **`HEK293 Cells`** · **`RNA Stability`** · `Cells, Cultured`

Both are **new to the repository's `abstract_only` record**, and both bear directly on the
molecular-state question:

- **`HEK293 Cells`** implies a **heterologous expression arm** — a second, independent measurement
  of Q230P protein in a non-patient context. The repository has been reasoning as though this
  source contains patient fibroblasts only. If an overexpression experiment exists, it is a
  different detection regime (higher expression, different chaperone load, different lysis) and it
  may be where a residual band would be visible if one exists anywhere.
- **`RNA Stability`** implies transcript stability was assessed as such, not merely level — a
  finer measurement than *"qRT-PCR normal"*.

🔴 **Bounded honestly:** MeSH terms are **indexer-assigned**, not author statements. They establish
that a professional indexer judged these topics present; they do **not** establish what was
measured, in which figure, or with what result. This is a **pointer**, not a datum, and it is
recorded at that strength. It does not narrow `MOLECULAR FATE UNRESOLVED` by even one hypothesis.

### 5.4 Grade and effect

**Grade: `NEW DETAIL`** — not `NEW CONNECTION`, because nothing here changes a mechanism; and not
`NONE`, because two previously unrecorded experimental contexts are now on file.

**Effect: `CREATED FOLLOW-UP` + `PREVENTED FALSE NOVELTY`.**
The false novelty prevented is subtle and worth naming: this session was one step from treating
*"the repository holds no lysis chemistry for Q230P"* as *"no lysis chemistry was ever published
for Q230P."* The baseline check showed the load-bearing paper was never read past its abstract —
so the corpus-level absence measured in `DISCOVERY_TRACE_lysis_chemistry` is, for this paper at
least, **an artefact of our own reading depth**, not a property of the literature.

### 5.5 The one precise action this leaves

**`HUMAN_REQUIRED`** — obtain Johannsen et al. 2018, *Neurogenetics* 19(3):151–156,
`doi:10.1007/s10048-018-0549-5`, and read **Methods** for: lysis buffer composition, any
pellet/insoluble handling, the HEK293 arm's design, antibody identity and epitope, and whether
transcript **stability** (not level) was measured.

Blocked here by network policy, not by the paper. A deployment permitted to reach Unpaywall,
Europe PMC or a library proxy may well obtain it without any human at all — **this is an
environment limit, and it should not be recorded as a literature limit.**

---

## 6 · SECOND ACQUISITION WAVE — routes exhausted, and a rediscovery caught in time

> # 🔴 SUPERSEDED — READ §7 FIRST
>
> **§6.1 below is a duplicate.** A `HUMAN_ACQUISITION_PACKET` for this paper already existed when
> it was written, in
> [`johannsen2018_acquisition_and_body_20260922.md`](johannsen2018_acquisition_and_body_20260922.md)
> (Scientist, same day, 700 lines, with an Orchestrator verification block). That file is the
> **operative** packet. §6.1 is kept unedited as the evidence of how the duplication happened; do
> not work from it.

### 6.1 `SOURCE_ACQUISITION_PACKET` — PMID 29808465

| Field | Value |
|---|---|
| **PMID / DOI** | 29808465 · `10.1007/s10048-018-0549-5` |
| **Citation** | Johannsen J, Kortüm F, Rosenberger G, Bokelmann K, Schirmer MA, Denecke J, Santer R. *Neurogenetics* 2018;19(3):151–156 |
| **Why load-bearing** | only source measuring Q230P transcript **and** protein in patient material; `MOLECULAR FATE UNRESOLVED` rests on it |
| **Repo read depth** | 🔴 `ABSTRACT_ONLY` · no deep-dive manifest |
| **Missing fields that matter** | lysis recipe · pellet handling · HEK293 arm design · antibody identity/epitope · detection floor · whether RNA **stability** (not level) was tested |
| **Routes tried** | PubMed MCP (**no PMCID — authoritative, not in PMC**) · Unpaywall, Europe PMC, Crossref, OpenAlex, Semantic Scholar, Springer landing, NCBI idconv (**all `CONNECT tunnel failed, 403`**) · Scholar Gateway (**Wiley corpus; Springer title absent**) |
| **Failure classes** | `NO OPEN FULL TEXT IDENTIFIED` (PMC only) + `NETWORK POLICY BLOCKED` (all HTTP) + `CORPUS OUT OF SCOPE` (Scholar Gateway) |
| **Resolution needed** | `HUMAN_OR_ALTERNATE_DEPLOYMENT` — any deployment with Unpaywall/Europe PMC/library-proxy egress, or a human with the PDF |

🔴 **No route remains in this environment. Stop retrying it.** Predictions stay `UNTESTED`.

### 6.2 🎯 The search returned a WWOX antibody-epitope hit — and it is a `REDISCOVERY`

Scholar Gateway surfaced Davids et al., *Human Mutation* 2018/2019,
[DOI](https://doi.org/10.1002/humu.23675), whose Methods name **two WWOX antibodies by exon-range
immunogen**: ProteinTech (exons 1–7) and Abcam (exons 1–5). Against a session that had just
measured *"11 manifests mention an antibody, zero record a catalogue number,"* this looked like
precisely the §18 epitope-geometry datum the corpus lacked.

**`enumerate_baseline_before_scoring` step 2 ran first, and killed it.**
`disease-models/wwox/analysis/wwox_antibody_epitope_census_20260922.md:111–112` **already holds
both**, as entries `A5` and `A6`, from the same paper, already at `full-text` depth — and already
carries the analysis I was about to derive, in sharper form:

- **`A5`** (ProteinTech, exons 1–7 ⇒ aa 1–≈280) — 🔴 **spans residue 230**
- **`A6`** ⭐ (Abcam, exons 1–5 ⇒ aa 1–172) — 🟢 **N-terminal, stops 58 residues before Q230**

**Graded `REDISCOVERY`. Effect: `PREVENTED FALSE NOVELTY`.** Third clean instance of this
primitive in one session, and the first where it killed a finding that had *external* provenance
and therefore looked especially credible.

### 6.3 What the rediscovery nonetheless corrects — and it sharpens weak-C

The earlier census claim was scoped to **`deepdive_manifests/` only**, and at that scope it was
true. But the **analysis layer holds rich epitope data the manifest layer does not** — supplier,
exon-range immunogen, span-vs-Q230 assessment, assay class, provenance.

🎯 **This is the strongest evidence yet for weak-C (incidental capture).** The datum was *read*,
*analysed* and *written down* — into a hand-authored analysis file, because a reader's question
made it relevant. It never reached the structured layer, because no field exists for it there.
Same repository, same paper, same session-week: **present in prose, absent in schema.**

🔴 **And it bounds my own §17/§18 conclusion.** *"Epitope-geometry reasoning cannot be run over
held artefacts"* is **wrong as stated** — it can, just not from manifests. The corrected form:

> *No antibody epitope data was identified in `deepdive_manifests/*.json` (n=81, structured layer).
> The analysis layer holds a dedicated epitope census; **that** is where the reasoning must start.*

**The lysis-chemistry conclusion is not rescued by this.** A parallel check is now owed: whether an
analysis-layer artefact holds lysis recipes the manifest census missed. **Pre-registered here
before looking**, so it cannot be retrofitted: I expect **no** such file to exist, because no
reader's question has yet made buffer composition relevant — which is exactly what the
design-vs-bench gradient in `DISCOVERY_TRACE_lysis_chemistry` §6 predicts.

---

## 7 · 🔴 THE PRE-REGISTERED CHECK REFUTED ME, AND THE REFUTATION IS THE FINDING

§6.3 pre-registered: *"I expect **no** analysis-layer file to hold lysis recipes, because no
reader's question has yet made buffer composition relevant."*

**REFUTED, immediately and completely.** An unfiltered `ls` of this very directory returns:

| File | Lines | What it already contained |
|---|---|---|
| `wwox_missense_abundance_lysis_census_20260922.md` | **676** | *"A Western blot reading 'protein absent' is a statement about the lysate that was loaded, not about the cell"* — the **exact** question `DISCOVERY_TRACE_lysis_chemistry` posed, with predictions written before the search and scored, a buffer-lineage analysis, and §4 *"The one experiment that settles it"* |
| `johannsen2018_acquisition_and_body_20260922.md` | **700** | full cascade with an `example.com` **control** proving blanket egress block; Scholar Gateway probed with **three** framings; citation-chaining exhausted; eleven extraction targets graded `PREMISE: METHODS_INVISIBLE`; a ranked `HUMAN_ACQUISITION_PACKET`; Orchestrator verification |
| `wwox_antibody_epitope_census_20260922.md` | — | `A5`/`A6` epitope geometry (§6.2) |
| `q230p_minimum_discriminator_20260922.md` | **964** | the minimal discriminating experiment |
| `wwox_missense_stability_census_20260922.md` | — | every WWOX missense with a protein-level measurement |

🔴 **My entire Q230P wave this turn was a rediscovery of work completed earlier the same day.** The
acquisition attempt, the routes, the failure classes, the packet — all already done, and done
better: that session proved the egress block **with a control**, where I merely observed 403s.

🔴 **Even the finding I reported as new was not new.** §5.3 graded `HEK293 Cells` in the MeSH as
`NEW DETAIL`. `wwox_missense_abundance_lysis_census_20260922.md` §1.4 is titled
*"🆕 A lead the abstract does not contain: Johannsen 2018 has a HEK293 arm."* **Same lead, same
day, same directory.** Correct grade: **`REDISCOVERY`**.

### 7.1 Root cause — a fourth member of the search-defect family, and the worst

My "step 1 · ENUMERATE by listing" ran:

```bash
ls disease-models/wwox/analysis/ | grep -E "DISCOVERY_TRACE_lysis|PREREG_johannsen"
```

🔴 **The listing was filtered by a pattern derived from what I expected to find.** By construction
it could return only my own files. The two files that would have stopped the whole wave were in the
unfiltered output, in the directory I was writing into.

```
§3  grep -i lysis   matched  ana-LYSIS        — pattern hit an unrelated superstring
§6  pgrep -f <job>  matched  the asker        — pattern hit the query itself
§7  ls | grep <my own names>                  — the FILTER WAS THE HYPOTHESIS
```

The third is the worst because the first two produce a wrong *number* while this one produces a
**confidently empty baseline**, which reads exactly like a clean field. `enumerate_baseline`'s
step 2 says *read what you enumerated*; it never said **do not narrow the enumeration to your own
expectation.** It does now.

### 7.2 What survives from this turn, honestly scored

**Survives** — the manifest-layer census (0 detergents / 0 pellet steps in 81 manifests) is still
a true measurement, and the contrast with a rich analysis layer is now the **strongest** evidence
for incidental-capture (weak C): the datum was read, analysed and written into hand-authored prose
because a reader's question made it relevant, and never reached the structured layer. Also
surviving: the `md_status.py` fix, the two real bugs it closed, and the search-defect family.

**Does not survive** — every Q230P scientific conclusion in this turn. All of it was held.

### 7.3 The correction I owe the record

`MOLECULAR FATE UNRESOLVED` was **never** resting on an abstract in the way §1 implies. The *read
receipt* is `abstract_only` and the reading debt is genuinely undischarged — that part stands, and
the prior session says so itself. But the **analysis layer had already established the
consequences** of that undischarged debt, in depth. I read `reading_state.md` and concluded the
programme had not looked. It had.

> 🎯 **Source-depth awareness cuts both ways.** §9 of the skill warns against reading *our* absence
> as the *literature's* absence. This is the mirror failure: reading a **low read-receipt depth**
> as **low programme-level knowledge**. A receipt records what was read; it does not record what
> was worked out.
