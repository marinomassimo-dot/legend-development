---
record: PHASE I — INDEPENDENT PATHOGRAPH EDGE ADJUDICATION
id: PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_SCIB_v1
actor: scientist-b (NOT ACTIVATED — see §0)
date: 2026-08-25
worktree: .claude/worktrees/lettore-b · branch lettore-b
head_at_authoring: 2261a15e9a8e63cee4a25ac0eeba69ea2c8bdfc0
status: NON-CANONICAL WORK ARTIFACT. Mutates no registry, no claim, no paper record, no
  Pathograph surface, no DisMech file, no role contract, no governance file. No BATCH_COMMIT.
independence: written without reading Scientist A's or Scientist C's artifacts. One leak is
  declared in full at §10.2 — it was a commit *subject line*, seen during the mandated
  existence check, after my own derivation of the same finding was complete.
---

# Phase I — what the twenty declared Pathograph edges actually license

> Editorial note (consolidation, 2026-09-07): wikilinks quoted from the claim registry appeared here in elided form (double brackets, an ellipsis, then the claim id); they are rendered as plain `CLAIM NNN` because the elided form resolves to no file. The ellipsis is in the quoted source.


> **Nothing here is medical advice.** Every therapeutic sentence quoted below is quoted as an
> object of adjudication, not as a recommendation.

---

## 0 · Authority condition, determined before execution

`roles/scientist.md` frontmatter, read at `HEAD:roles/scientist.md`:

```
actor_id_status:
  scientist-b: FIXED on the same execution — same section
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
```

**The contract is `PROPOSED`.** The `ACTOR_ID` is fixed; the *contract* is not binding. I did not
self-activate it and I claim no authority from it.

Lease state, derived rather than read (`python3 framework/scripts/lease_state.py --check`, run at
`2026-08-25T13:20:24Z`): **`ACTIVE by derivation: 0`**. Two findings on historical lease #3, both
pre-existing and untouched here. No lease was acquired for this work and none was needed: nothing
below writes a canonical surface.

**Operating basis declared:** this is an **operator-directed analytical pilot**. Its authority is
the task itself. It is not an exercise of `roles/scientist.md`, and no precedent for that contract
should be read out of it.

`framework/state/state_manifest_current.md` → `current_state: READY`.
`python3 framework/scripts/legend_lint.py .` → **VERDICT: PASS** (one `[INFO]`, CLAIM 010 wikilink
not required for a `background only` claim).

---

## 1 · Where the workset actually lives — measured, and it is not where the task assumes

> ⚠️ **THIS MEASUREMENT IS DATED, AND THE CONDITION IT REPORTS HAS SINCE BEEN CLOSED.**
> Everything in §1 was measured before **2026-08-25T15:24:34+02:00**. At
> **2026-08-25T17:02:49+02:00**, commit **`d422829`** on `legend-operating-convention-v1` —
> *"The Pathograph existed on disk and on no ref, and its three wiring lines went with it"* —
> put the object on a ref. **Verified by me, object-level, over all 57 refs:**
> `pathograph.py`, `test_pathograph.py`, `pathograph_inventory.md` and `pathograph_export.jsonl`
> are now tracked on that branch.
>
> **The finding is not withdrawn and is not rewritten.** It was true when taken, it is why the
> object was preserved, and §17 forbids tidying a history so the sequence reads better. What is
> corrected is the *tense*: read §1 as **"was, until `d422829`"**, not as a present-tense claim.
> A population-derived figure decays; the reader cannot tell whether a conclusion moved with it
> unless the record says so, so this record says so.
>
> Also since superseded: §7's evidence-availability table. The four PMID 32000863 artifacts are
> now present in **this** worktree and all four sha256 match the manifest — `792b5b29…`,
> `0acb771c…`, `ced68a66…`, `9e464859…`. `files/fulltext/` here holds 16 entries, up from the 13
> it held while §1–§8 were written.

§4 says to use the Pathograph inventory *supplied through the canonical task surface*. I looked for
it before assuming it.

### 1.1 The Pathograph is in no commit, on any branch

```bash
for r in $(git for-each-ref --format='%(refname)' refs/heads refs/remotes); do
  git grep -ril 'pathograph' "${r}" -- ; done
```

| Measure | Value |
|---|---|
| refs swept (`refs/heads` + `refs/remotes`) | **50** |
| refs containing the string `pathograph`, case-insensitive | **0** |
| refs containing the string `WWOX` (positive control, same loop) | **50 of 50** |

The negative is not a broken sweep: the control fires on every ref. *(The zsh trap here is real —
`"$r:path"` applies the `:r` modifier and returns ABSENT on every ref. Braces were used.)*

### 1.2 It exists only in the shared checkout's working tree, untracked

| Path (shared checkout, `<REPO_ROOT>`) | git state |
|---|---|
| `framework/scripts/pathograph.py` | **UNTRACKED** |
| `framework/scripts/test_pathograph.py` | **UNTRACKED** |
| `disease-models/wwox/analysis/pathograph_inventory.md` | **UNTRACKED** |
| `disease-models/wwox/analysis/data/pathograph_export.jsonl` | **UNTRACKED** |
| `disease-models/wwox/analysis/README.md` | TRACKED, **modified and uncommitted** (+18 lines) |
| `DATA_SOURCES.md` | TRACKED, **modified and uncommitted** (+1 line) |

`git -C <shared> grep -ril pathograph HEAD` → **0 files**; same command for `wwox` → **363**. So the
shared checkout's own HEAD does not contain the Pathograph either: the generator, the inventory, the
export **and** the two documentation edits that announce them all live on the working tree alone.

🔴 **The workset for this task sits on the one surface nothing gates.** CI reads commits; a local
run reads disk; a sibling worktree reads neither. Four other worktrees on this machine — mine
included — cannot see the object they are being asked to adjudicate, and no regression can fail on
it. This is a property of *where the artifact is*, not of its quality.

### 1.3 What I adjudicated against, fingerprinted

| Artifact | sha256 |
|---|---|
| `pathograph_inventory.md` | `bbc09af474acc71f6549be7d296c1e2b94db04673def1a6c4a66a9baa231a032` |
| `pathograph_export.jsonl` | `39e9a224030d13b350022c696d4f753d855c4859aa00bb7a0320f4e95e361ebd` |
| `pathograph.py` | `c59750d5f9881f338a020061585ab0d3902684065303cfb02d505d196ccbb95e` |

**The registries are byte-identical between my tree and the shared checkout**, which is what makes
the derivation reachable from here at all:

| Registry | blob at my HEAD | blob at shared checkout HEAD | `git hash-object` of shared working copy |
|---|---|---|---|
| `claim_registry_current.md` | `9f4bcede` | `9f4bcede` | `9f4bcede` |
| `paper_registry_current.md` | `847879e0` | `847879e0` | `847879e0` |

The two branches diverge (3 ahead / 3 behind of merge-base `788c357`) and the two registry files do
not. The nodes and edges below are therefore derived from bytes I hold.

---

## 2 · The workset, re-measured rather than inherited

§4 supplied approximate counts and told me to re-measure. Counted mechanically from
`pathograph_export.jsonl`, not from the rendered table:

| Measure | Reported in §4 | **Re-measured** | Agree? |
|---|---|---|---|
| `claim_edge` records | ~20 | **20** | yes |
| …with ≥1 `shared_evidential_papers` | ~17 | **17** | yes |
| …with none | ~3 | **3** | yes |
| …carrying a declared `relation_type` | — | **0** (all `UNTYPED`) | — |
| …in `review_state` | — | **20 of 20 `AWAITING_SCIENTIST_TYPING`** | — |

The three edges with no shared evidential paper: `CLAIM 001↔002`, `CLAIM 003↔004`, `CLAIM 030↔033`.

Governed relation vocabulary, read from the export header (`relation_vocabulary`), not assumed:

```
DIRECT · INDIRECT_UNKNOWN_INTERMEDIATES · ASSOCIATED · CONTROVERSIAL_OPEN
```

---

## 3 · A finding about the workset itself, before any edge is typed

### 3.1 "Shared evidential paper" is a weaker signal than it reads as

`pathograph.py:445` builds a node's `evidential_papers` from
`trace_claim_foundation.EVIDENTIAL_EDGES = frozenset({"source_field", "claim_links"})`, and
`pathograph.py:491` intersects the two endpoints' sets.

So a paper counts as *shared evidence* when **either** the claim's `Source` field cites it **or**
the paper record's own `Claim links` field names the claim. The second is the commoner route and it
points the other way: the claim need not cite the paper at all.

Worked example, verified in the registry text: CLAIM 028's `Source` reads *"papers 207, 218, 206,
214 (corpus 181–220)"* and CLAIM 030's `Source` names PAPER 039/041/042/043. **Neither cites PAPER
056.** PAPER 056's own record does:

```
**Claim links:** 035 (new) · 016 (enriches) · 030 (supplies the functional assay) · 028 (supports)
```

That is how edges `CLAIM 028↔035` and `CLAIM 030↔035` acquire a shared evidential paper.

### 3.2 The registry already writes a per-link relation qualifier, and the assembler drops it

The four values above are not equivalent, and the registry knows it. Measured over the paper
registry at blob `847879e0`:

| Measure | Count |
|---|---:|
| `## PAPER NNN` records | **70** |
| …carrying a `**Claim links:**` field | **69** |
| …whose `Claim links` carry a parenthetical qualifier | **9** |
| distinct qualifier strings written | **17** |

The seventeen: `new` · `supports` · `new, primary` · `conflicting evidence` · `dato misto
vigabatrin` · `supporto P5` · `tensions` · `primary` · `secondary` · `enriches` · `supplies the
functional assay` · `supplies the mouse renal datum` · `bounds its imported premises` · `frames the
serum question` · `co-source` · `counter-directional` · `context dependence`.

None is in the governed vocabulary, and the derivation collapses all of them into one undifferentiated
`claim_links` kind. Three of them invert the reading of the edge they produce:

- **PAPER 058 → `005 (refutes its imported premise for the mouse)`.** This paper is counted as
  *shared evidence* for edge `CLAIM 005↔037`. It does not support both endpoints — it **refutes** a
  premise one of them imported.
- **PAPER 054 → `009 (tensions)`.** Counted as shared evidence for `CLAIM 009↔028` and
  `CLAIM 009↔034`. CLAIM 009's own `Source` field names it *"(evidenza controdirezionale)"*.
- **PAPER 057 → `005 (bounds its imported premises)`.** A bounding relation, not a supporting one.

🔴 **A shared-evidence count that includes refutation, tension and bounding as if they were support
is the wrong prior to hand a Scientist.** §4 uses exactly that count to order the work. The
inventory's own line *"Edges carrying a declared relation type: 0"* reads as work not yet done; part
of it is work already done, in a vocabulary nothing parses.

---

## 4 · The typing problem, measured: this vocabulary is causal and these edges mostly are not

> 🔴 **A PREMISE OF THIS SECTION IS UNSOUND, AND SCIENTIST C FOUND IT. Recorded 2026-08-25,
> position NOT yet revised — Scientist A has not reported and I am holding.**
>
> C's challenge: **three of the four relation tokens have no published definition anywhere**, so
> agreement on a token is agreement on a label, not on a criterion. **I measured it and C is
> right.** The only semantic gloss published for any token is an *illustrative example* inside
> `pathograph_inventory.md` — `(relation: DIRECT — the same experiment measures both endpoints)` —
> which glosses `DIRECT` only. `pathograph.py`'s `RELATION_VOCABULARY` tuple carries a comment about
> *enforcement* (*"An annotation carrying anything else is a named loss, never a guess and never a
> silent drop"*) and no semantics for any value. **`INDIRECT_UNKNOWN_INTERMEDIATES`, `ASSOCIATED`
> and `CONTROVERSIAL_OPEN` are undefined.**
>
> *(My first sweep for this was contaminated and I discarded it: `DIRECT` and `ASSOCIATED` are
> ordinary English words and matched on 56 and 44 of 57 refs respectively. The question is whether a
> **definition** exists, not whether the string does.)*
>
> **What this costs §4.** The measurement in the first table — 10 of 20 edges carry no proposition
> at all, 7 bare wikilink entries and 3 bare see-alsos — is a measurement of the *registry* and
> stands untouched. The second table's verdict, *"typeable? no"* for eight edges, **does not**: I
> reasoned about what `ASSOCIATED` "asserts" and what `INDIRECT_UNKNOWN_INTERMEDIATES` "encodes",
> and I supplied both glosses myself. So did Scientist A. Two actors independently inventing
> compatible semantics for an undefined token is not convergence on a criterion.
>
> **The honest restatement is stronger than what I wrote, not weaker:** it is not that no governed
> type fits these eight edges — it is that **nobody can say whether any type fits any edge, because
> three of the four types mean nothing published.** The inventory's line *"Edges carrying a declared
> relation type: 0"* reads as work not yet done; part of it is **undoable by construction** until
> the vocabulary is defined. That is a defect in the instrument, and defining it is Plan's under
> §16, not mine.
>
> Carried forward to the rebuttal round rather than acted on now. It also bears on my Phase II §3.4
> concession and my Phase III revision to `ASSOCIATED`; both are held pending A's response.

For every one of the 20 edges I extracted the *sentence* that declares it — the line in the endpoint
claim's block that contains the wikilink to the other endpoint — rather than accepting the
`declaring_fields` label.

| What actually declares the edge | Edges | Which |
|---|---:|---|
| **Nothing but a bare `Wikilinks:` list entry** — a co-mention, no proposition | **7** | 001↔031 · 003↔004 · 019↔033 · 028↔035 · 030↔032 · 037↔038 · 037↔039 |
| **A bare "Vedi CLAIM NNN" cross-reference** and nothing more | **3** | 009↔028 · 019↔030 · 030↔033 |
| **A sentence asserting something about the pair** | **10** | 001↔002 · 005↔036 · 005↔037 · 009↔034 · 016↔035 · 019↔032 · 028↔034 · 030↔035 · 031↔032 · 036↔038 |

Of the ten that carry a proposition, I then asked what *kind* of proposition it is:

| Kind of proposition | Edges | Typeable in `DIRECT / INDIRECT_UNKNOWN_INTERMEDIATES / ASSOCIATED / CONTROVERSIAL_OPEN`? |
|---|---:|---|
| Causal-mechanistic relation between the endpoints' subjects | **1** (016↔035) | yes |
| Contradiction about the *sign* of a biological relation | **1** (009↔034) | yes — `CONTROVERSIAL_OPEN` |
| Epistemic / methodological — bounds, refutes a premise, supplies an assay, instantiates a principle, fails to predict, contrasts two models | **8** | **no** |

🔴 **This is the load-bearing result of my Phase I edge work.** The governed vocabulary types
*causal* relations. **Eighteen of twenty edges are not causal assertions.** They are the sentences a
disciplined registry writes about its own evidence: *this model is not that model*; *this paper
refutes the premise that one imported*; *this claim supplies the assay the other one needs*; *this
observation instantiates that principle*.

§5 says: if no existing type fits, say so, and do not invent one. **I say so, for eight edges, and
I invent nothing.** The correct outcome for those eight is not `ASSOCIATED` — `ASSOCIATED` would
assert a biological association that no source claims. It is *relation unsupported in the causal
vocabulary, and a second relation plane is owed*.

For the seven bare-wikilink edges and the three bare see-alsos the outcome is different again and
simpler: **a co-mention is not a proposition.** §2 forbids assigning a relation because two claims
share a paper; a fortiori because one claim's `Wikilinks` line names the other. Ten of twenty edges
in this graph have never had a scientific proposition attached to them by anybody.

---

## 5 · Per-edge adjudication — Tier 1, the GSK3β cluster

Primary evidence re-read at the artifact this session; all four declared artifact fingerprints for
PMID 32000863 re-verified byte-identical to the manifest, and the Wang 2012 XML re-verified.

### E-016-035 · CLAIM 016 ↔ CLAIM 035

| Field | Content |
|---|---|
| **SOURCE CONCEPT** | CLAIM 035 — *"WWOX is a direct, residue-mapped inhibitor of GSK3β through an Axin-like docking motif in the SDR domain (388–407 / L404); the inhibition is S9-independent and its neuronal output requires Tau"* |
| **TARGET CONCEPT** | CLAIM 016 — *"GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency"* |
| **CURRENT REPOSITORY ASSERTION** | `claim_registry_current.md:297`, field `Meccanismo aggiunto (BATCH_20260726_001)`: *"WWOX non è soltanto correlata al livello di GSK3β — ne è un **inibitore fisico diretto**, tramite il motivo di docking Axin-like 388–407/L404 del dominio SDR ([[paper_registry_current#PAPER 056]], [[claim_registry_current#CLAIM 035]])."* Declared reciprocal by the assembler; the reverse direction is a bare `Wikilinks` entry (`:299`). |
| **PRIMARY SOURCES** | PAPER 056 = Wang *et al.* 2012, *Cell Death Differ* 19:1049–1059, PMID 22193544 · PAPER 019 = Cheng *et al.* 2020, *Acta Neuropathol Commun*, PMID 32000863 |
| **ARTIFACT IDENTITY** | `PMID22193544_Wang2012_PMC_JATS.xml` sha256 `eb6f568d046f8df831d15e7f8795fcb1d6ac713ec6305f7ded3ad2a330388268` · `PMID32000863_Cheng2020_PMC.xml` sha256 `792b5b29…f00f5` · `40478_2020_883_Fig7_HTML.png` sha256 `ced68a66…62542`, native 1946×1627 |

**MODEL / SYSTEM.** Wang 2012: human SH-SY5Y under retinoic-acid differentiation; recombinant
proteins; endogenous co-IP from mouse brain extract. No WWOX-DEE allele tested. Cheng 2020: mouse,
constitutive `Wwox−/−`, postnatal day 20 for the blot, PTZ 30 mg/kg for the behaviour.

**OBSERVATION — what was directly measured.**
Wang 2012, verified in the artifact: *"This indicates that WWOX amino acids 388–407 are required for
its interaction with GSK3β"*; *"the mutation of L404A, but not L311A, completely abolishes the
binding of WWOX to GSK3β"*; *"Ectopically expressed WWOX significantly inhibited Tau phosphorylation
at S404 and S396 but not S422"*; *"immunoprecipitation was performed in mouse brain extracts … both
GSK3β and WWOX were precipitated"*; and critically *"We found that the phosphorylation levels of
phospho-GSK3β S9 and phospho-β-catenin remained normal."*

Cheng 2020, read from the image at native resolution and at 3× on the densitometry row (Fig. 7c):

| Blot row | Cerebellum +/+ · +/− · −/− | Hippocampus | Cortex |
|---|---|---|---|
| pGSK3β (Ser9) | 2.7 · 3.1 · **1.3** | 3.6 · 3.5 · **2.0** | 3.9 · 3.8 · **2.5** |
| GSK3β (total) | 2.2 · 2.4 · **2.4** | 2.3 · 2.4 · **2.6** | 2.2 · 2.4 · **2.6** |

One lane per genotype per region. No error bars, no replicate values, **no statistical test on
panel c** — the caption offers only *"The representative results of four independent experiments are
shown."*

**AUTHOR INTERPRETATION.** *"Increased activation of GSK3β was determined … as evidenced by
dephosphorylation of GSK3β at Ser9"*; *"Together, these results suggest an important role of GSK3β
in the hypersusceptibility to epileptic seizure induction due to Wwox loss in neuronal cells."*
Cheng 2020 does **not** measure the WWOX–GSK3β interaction: it cites it — *"WWOX has been shown to
interact with and inhibit GSK3β … in human neuroblastoma SH-SY5Y cells [65]"*, and reference 65 is
verbatim *"Wang HY Juo LI Lin YT … WW domain-containing oxidoreductase promotes neuronal
differentiation via negative regulation of glycogen synthase kinase 3β Cell Death Differ 2012"* —
i.e. PAPER 056 itself.

**SCIENTIST INTERPRETATION.** Two arms, and they do not join where the graph wants them to.

1. *WWOX ⊣ GSK3β* is as well-founded as this corpus gets: five orthogonal assays, a point mutation
   that abolishes binding, and an endogenous brain co-IP. At the **molecular** scale this is `DIRECT`.
2. *GSK3β de-repression → seizure susceptibility* is not established by Cheng 2020. Its two supports
   are a single-lane pS9 blot with no statistics, and a lithium experiment adjudicated below.
3. 🔴 **The two arms use incompatible readouts, and nobody in this repository has said so.** Wang
   2012's inhibition is **S9-independent** — the registry records this (`:297`) and CLAIM 035's own
   `Clinical meaning` draws the consequence for *future* work: *"la de-repressione di GSK3β causata
   dalla perdita di WWOX sarebbe **invisibile a un western anti-fosfo-S9**, che è il saggio standard
   — qualunque studio WWOX-DEE che usi pS9 come readout di attività GSK3β produrrà un **falso
   negativo**."* CLAIM 016's principal molecular evidence **is a pS9 western in a WWOX-deficient
   setting.** If Wang's mechanism holds, the Ser9 dephosphorylation Cheng observes cannot be the
   signature of the lost WWOX brake; it needs a second, unmeasured cause. The warning was written,
   exported (`dismech_export_spec.md`, assertion `035-f`), reviewed — and never turned around and
   pointed at the claim sitting next to it in the same document.

**RELATION DIRECTION.** `CLAIM 035 → CLAIM 016` only. CLAIM 016 supplies nothing to CLAIM 035; the
reciprocity the assembler reports comes from a `Wikilinks` list entry, not from evidence.

**RELATION TYPE.** `INDIRECT_UNKNOWN_INTERMEDIATES` — the governed value fits, and it fits *because*
of point 3: between the residue-mapped brake and the murine seizure phenotype there is at least one
intermediate nobody has measured, and the readout that was used is one the mechanism predicts would
not report it.

> ⚠️ **SUPERSEDED IN PHASE II — this first-pass verdict is preserved, not corrected in place**
> (§9 forbids erasing the dissent trail). Scientist A argued that
> `INDIRECT_UNKNOWN_INTERMEDIATES` asserts a causal path with unspecified intermediates, whereas
> here the path itself is untested — and supplied evidence I did not have (Wang 2012's S9A mutant
> behaves like wild type, so the Ser9 axis is *dispensable* by design, not merely unengaged).
> **I accepted the argument and revised to `ASSOCIATED`, direction `035 → 016`.** Reasoning in
> `PHASE2_CROSS_REVIEW_SCIB_v1.md` §3.4.

**CAUSAL LIMIT.** No selective GSK3β inhibitor; no `Gsk3b` genetic epistasis on the `Wwox`-null
background; no target-engagement measurement in the lithium arm (no pS9, no β-catenin, no Tau blot
after LiCl); no WWOX-DEE allele in Wang 2012; species and system change between the two arms
(human neuroblastoma / recombinant → constitutive-null mouse).

**NEGATIVE / COUNTER-EVIDENCE DELIBERATELY SOUGHT.**
- Sought whether Cheng 2020 measures the interaction itself → it does not; it cites ref. 65.
- Sought whether total GSK3β rises, as CLAIM 016's `Summary` says → it does not; +9%, +13%, +18% on
  single lanes with no test, against −52%, −44%, −36% on pS9. The measured change is phosphorylation,
  not abundance.
- Sought whether the paper's own Discussion offers competing mechanisms for its lithium result → it
  does, verbatim: *"Administration of lithium in mice has been demonstrated to attenuate PTZ-induced
  clonic seizure [10], and rescue Wnt-dependent cerebellar midline fusion and neurogenesis deficits
  early in development [38]"*; *"Lithium treatment has also been shown to induce β-catenin-mediated
  myelin gene expression in mouse Schwann cells and enhance remyelination"*. Reference 10 is
  *"Bahremand A … Additive anticonvulsant effects of agmatine and lithium chloride on
  pentylenetetrazole-induced clonic seizure in mice: **involvement of α2-adrenoceptor**"* — the
  paper's own cited support for the effect is in ordinary mice and attributes it to a different
  receptor system.

**CONTRADICTORY EVIDENCE.** The readout mismatch at point 3. Not a contradiction between the two
papers — Wang shows pS9 unchanged under WWOX *gain*, which does not formally forbid a pS9 change
under WWOX *loss* through an indirect route — but a contradiction between the mechanism the edge
asserts and the measurement offered as its evidence.

**EVIDENCE SUFFICIENCY.** Sufficient to carry `CLAIM 035 → CLAIM 016` as
`INDIRECT_UNKNOWN_INTERMEDIATES`. **Not** sufficient to carry it as `DIRECT`, and not sufficient in
the reverse direction at all.

**GRAPH RECOMMENDATION.** **Carry with qualification**, direction `035 → 016`, type
`INDIRECT_UNKNOWN_INTERMEDIATES`, with the readout mismatch attached as a stated limit. The
reciprocal direction: **relation unsupported**.

---

### E-028-035 · CLAIM 028 ↔ CLAIM 035

**CURRENT REPOSITORY ASSERTION.** `claim_registry_current.md:643`, CLAIM 035 `Wikilinks`:
`… · [[claim_registry_current#CLAIM 028]]`. **That is the entire declaration.** One-way,
`CLAIM 035 → CLAIM 028`, no sentence anywhere in either block relates them.

**Shared evidential paper:** PAPER 056 — and via §3.1 only, from PAPER 056's own `Claim links`
qualifier `028 (supports)`. CLAIM 028's `Source` names corpus stubs 207/218/206/214 and not PAPER
056.

**SCIENTIST INTERPRETATION.** CLAIM 028 is an interpretive principle (*"WWOX biological output is
strongly partner- and context-dependent; expression level alone is insufficient…"*, `Type: INFERENZA
— principio interpretativo trasversale`). CLAIM 035 is a residue-level biochemical result. Wang 2012
*is* a good instance of the principle — a function that changes with no change in level is precisely
"expression level alone is insufficient". But **instantiation is not a causal relation between two
propositions**, and no source asserts one.

**RELATION TYPE.** **No governed type fits.** `DIRECT` and `INDIRECT_UNKNOWN_INTERMEDIATES` assert
mechanism between subjects; `ASSOCIATED` asserts a biological association; `CONTROVERSIAL_OPEN`
asserts dispute. What holds here is *instance-of-a-principle*, which the vocabulary does not carry.
I do not invent a token.

**GRAPH RECOMMENDATION.** **Relation unsupported** in the causal plane; **architecture-sensitive** —
belongs to a principle/instance plane the graph does not yet have. See §7 DC-3.

---

### E-030-035 · CLAIM 030 ↔ CLAIM 035

**CURRENT REPOSITORY ASSERTION.** `claim_registry_current.md:637`, CLAIM 035 `Clinical meaning`:
*"**(1) Un saggio funzionale per gli alleli missense del dominio SDR** — pull-down GSK3β +
inibizione della chinasi su Tau in vitro — più economico e meglio definito dell'attività
ossidoreduttasica, il cui substrato fisiologico è ignoto (vedi [[claim_registry_current#CLAIM
030]])."* One-way, `035 → 030`. Shared paper PAPER 056, via qualifier `030 (supplies the functional
assay)`.

**SCIENTIST INTERPRETATION.** The proposition is real and it is **methodological**: CLAIM 035
supplies a measurable assay for the property CLAIM 030 asserts is decisive (residual *function*, not
abundance). It is a good and non-obvious link. It asserts nothing about WWOX causing anything in
CLAIM 030's subject matter.

Worth recording because it strengthens both endpoints: CLAIM 030's four-allele series is explicitly
non-commensurable (`Impact on Working Model`: *"le misure di abbondanza confrontate non sono
commensurabili (WB su fibroblasti per P47T e Q230P; IF su organoidi per G372R)"*), and CLAIM 035
offers the commensurable functional readout that would fix that. **G372R is the natural negative
control** the registry already names.

**RELATION TYPE.** **No governed type fits** — *supplies-an-assay-for* is not causal.

**GRAPH RECOMMENDATION.** **Relation unsupported** in the causal plane; **ready for integration** in
a methodological plane if one is created. Scientifically the strongest of the three non-causal
GSK3β-cluster edges and the one I would least like to see dropped.

---

## 6 · Per-edge adjudication — Tier 2 and Tier 3

Depth declared honestly: for these eight edges I verified the **load-bearing quantity or negative of
each endpoint verbatim against the primary artifact**, and did not re-read the papers end to end.
Every quotation below was extracted from the artifact this session, not transcribed from the registry.

### E-005-037 · CLAIM 005 ↔ CLAIM 037 — the strongest non-causal edge in the graph

Declared in CLAIM 005 `Evidence boundary`: *"Seizures in the Wwox literature are a **rat `lde/lde`**
phenotype — see [[claim_registry_current#CLAIM 037]]."* Shared paper PAPER 058, qualifier
**`005 (refutes its imported premise for the mouse)`**.

**Verified in the artifact** (`PMID19500159_Suzuki2009.html`), three separate assertions:
*"Although neither epileptic seizures nor abnormal behavior has been reported in Wwox KO (knockout)
mice…"*; *"Although neither abnormal behavior nor impaired motor skill was observed in the Wwox KO
mice (Aqeilan et al. …)"*; *"Although the reason for no detection of spontaneous epilepsy in the KO
mice is unknown … the KO mice may die before they experience epileptic seizure."*
Rat phenotype verified first-hand: *"Excluding the 3 rats that died, 19 of 20 rats (95%) experienced
at least once audiogenic seizure"*; *"None of the 14 normal rats experienced audiogenically induced
or spontaneous epileptic seizures or any other abnormal behavior."* Figure 6's caption confirms the
95% cohort is *"21- to 33-day-old lde/lde **females**"* — the sex restriction is declared only there.

**Interpretation.** The relation is **refutation of an imported premise**, and it runs species-first:
the seizure phenotype attached to WWOX loss in the mouse literature was imported, and its terminus
asserts the opposite for the mouse. This is not an association between two biological facts; it is
one claim correcting another's provenance.

**Type: no governed type fits.** `CONTROVERSIAL_OPEN` is the near miss and it is wrong — nothing is
in dispute here. One claim carried a premise; the other's source denies it, in its own words, three
times. **Recommendation: relation unsupported in the causal plane; architecture-sensitive** — the
graph needs a *refutes-premise-of* relation and has no way to say it.

### E-005-036 · CLAIM 005 ↔ CLAIM 036

Declared in CLAIM 036 `Evidence boundary`: *"🔴 Driver Cre **diverso** da quello di CLAIM 005:
EIIA-Cre qui, BK5-Cre in PMID 30290271 — allele floxed condiviso, knockout diverso."* One-way,
`036 → 005`. Shared paper PAPER 057, qualifier `005 (bounds its imported premises)`.

**Verified in the artifact** (`PMID19936220_Ludes-Meyers2009_PMC.xml`): every quantity CLAIM 036
carries is present — glucose `143.5` vs `250.6`, BUN `37.25` vs `17.67`, bicarbonate `14.50` vs
`21.67`, `p=0.000131`, `p=0.01086`. The paper's own words: *"All Wwox KO mice displayed significant
hypocapnia suggesting a state of metabolic acidosis"*; *"we speculate that the lack of Wwox
expression in the kidney tubules in KO mice is likely responsible for the development of severe
metabolic acidosis of renal tubule origin (RTA)"*.

**Interpretation.** A **model-comparability bound**: a systemic null measured at P14–P18 is
simultaneously hypoglycaemic, acidotic, uraemic and anaemic, so brain phenotypes measured in that
window cannot separate cell-autonomous loss from secondary metabolic damage — *and* the two claims
use different Cre drivers on a shared floxed allele. The declaration does not assert that CLAIM 036's
subject causes CLAIM 005's; it asserts that CLAIM 005 cannot be read as cleanly as it appears.

⚠️ **Minor source-internal mismatch, recorded not normalised:** the paper writes *"hypocapnia"* for
what its Table 3 measures as total CO₂ / bicarbonate. Total CO₂ is not pCO₂. It does not change the
acidosis reading; it does mean the word and the measurement differ in the source.

**Type: no governed type fits. Recommendation: relation unsupported in the causal plane;
architecture-sensitive** (*bounds-the-interpretation-of*).

### E-036-038 · CLAIM 036 ↔ CLAIM 038

Declared in CLAIM 038 `Summary`: *"Il ratto è dunque **uremico senza essere ipoglicemico** — profilo
opposto a quello del topo null, che è entrambi (vedi CLAIM 036)."* Reciprocal. Shared paper
PAPER 057, qualifier `038 (supplies the mouse renal datum)`.

**Verified**: rat values `12.6 → 40.3` (♀) and `10.1 → 35.6` (♂) for BUN, `0.64` / `0.58` for
creatinine, all present in `PMID17803050_Suzuki2007.html`, alongside *"The concentrations of
electrolytes … GLU, and TG were comparable in the normal and mutant rats"*. The two competing
explanations are both verbatim from the sources and they are **from different papers**: the mouse
paper speculates RTA; the rat paper writes *"the production of urea-nitrogen and creatinine may be
increased due to hypercatabolism and muscle disruption"* and notes *"we could not find any pathologic
alteration in their kidneys."*

**Interpretation.** A **cross-model contrast with an unresolved mechanistic fork.** Same marker,
two species, two incompatible explanations, neither tested, and neither paper considers the other's.

**Type.** This is the one Tier-2 edge where a governed value is arguable: the fork is a genuine open
dispute about the cause of a shared observation. `CONTROVERSIAL_OPEN` fits the *fork*. It does not
fit the *edge*, which joins two claims that agree on the measurements and disagree about nothing.
**I decline to type it** rather than borrow a value for the wrong object.
**Recommendation: relation unresolved.**

### E-037-038 · CLAIM 037 ↔ CLAIM 038 · and E-037-039 · CLAIM 037 ↔ CLAIM 039

Both declared **by bare `Wikilinks` entries only**, in both directions. No sentence in any block
relates them. Shared papers PAPER 058/059 and PAPER 059 respectively.

The underlying science is sound and first-hand — *"95% of the mutant rats but none of the normal
rats had ataxic gait"* and *"we did not detect any marked pathologic changes in the cerebella of
lde/lde rats"*, both verified verbatim in `PMID17803050_Suzuki2007.html` — but **the graph has not
been told what relation to draw**. Same model, same paper, three phenotypes is a *co-occurrence in
one animal*, which is real and is not a causal relation between the propositions.

**Recommendation for both: relation unsupported** as declared. What the evidence would license is a
`same-model` grouping, which is a node-attribute question, not an edge.

🔴 **One new observation from this re-reading, unremarked anywhere I searched:** Suzuki 2009 reports
*"The relative weight of brain was significantly larger in affected than in normal females and
males."* That is the **same brain-sparing-in-cachexia signature** CLAIM 036 identifies and warns
about in the mouse (*"assoluto 0.390 → 0.356 g (−8.7%), relativo 5.0% → 8.5% … la significatività è
sul relativo, guidata dal denominatore crollato"*). The confounder CLAIM 036 quantifies for the
mouse has an unremarked counterpart in the rat, in a paper both CLAIM 037 and CLAIM 038 rest on.
This bears on E-005-036, E-036-038 and E-037-038 simultaneously and belongs in whichever of them
survives.

### E-009-034 · CLAIM 009 ↔ CLAIM 034 — the second typeable edge

Declared in CLAIM 034 `Summary`: *"La direzione è opposta alla cornice deficienza→ROS di
CLAIM 009."* Reciprocal, and the reverse side is the `⚠️ Counter-directional evidence` field.
Shared papers PAPER 054, PAPER 071.

**Interpretation.** CLAIM 009 frames WWOX deficiency → ROS. CLAIM 034 reports, in diabetic mouse
photoreceptors, that WWOX rises and its siRNA knockdown **reduces** superoxide by 27–37%. This is a
genuine disagreement about the **sign** of a biological relation, and the registry has already
refused to over-state it: CLAIM 009's own note explains why the status stays `in observation` and
does not rise to `conflicting evidence` — *"il protocollo riserva quello stato a studi comparabili,
e questi non lo sono"*.

**Type: `CONTROVERSIAL_OPEN`.** This is the value's proper use: two claims asserting opposite signs
for the same relation, with the non-comparability declared rather than hidden.

**CAUSAL LIMIT / counter-evidence sought.** CLAIM 034's own `Clinical meaning` supplies the
strongest objections against itself — acute adult knockdown ≠ germline developmental loss; WWOX here
is a *stress-induced* protein; the loss-of-function evidence is **n = 2** against a non-inert
scrambled control. I read them and I agree with them: they weaken CLAIM 034, and they do not remove
the contradiction, because CLAIM 009 is an `INFERENZA` whose own `Source` is *"mechanistic
synthesis"* — a phrase, not a paper.

**GRAPH RECOMMENDATION.** **Carry with qualification** as `CONTROVERSIAL_OPEN`, with the
non-comparability recorded on the edge. **The one edge in this graph I would carry into a scientific
graph today without hesitation.**

### E-028-034 · CLAIM 028 ↔ CLAIM 034

Declared in CLAIM 034 `Clinical meaning`: *"è evidenza concreta che il segno della relazione
WWOX↔ROS è fissato dal contesto, e istanzia direttamente CLAIM 028."* One-way, `034 → 028`.

**Interpretation.** Explicit instantiation — the registry uses the word *"istanzia"*. Same structural
shape as E-028-035, and the same verdict: **no governed type fits**; principle/instance is not
causal. **Relation unsupported in the causal plane; architecture-sensitive.**

Two of CLAIM 028's four edges are instantiations of it. That is a property of the node, not of the
edges: CLAIM 028 is an **interpretive principle wearing a claim record**, and every link into it will
have this shape. See §7 DC-3.

### E-009-028 · CLAIM 009 ↔ CLAIM 028

Declared by a bare cross-reference inside CLAIM 009's counter-directional field: *"Vedi
CLAIM 034 e CLAIM 028."* One-way. Shared paper PAPER 054, qualifier `009 (tensions)`.

**Recommendation: relation unsupported.** A "see also" is not a proposition, and the shared paper is
declared as being *in tension* with one endpoint.

---

## 7 · Edges whose primary evidence I could not reach

Nine of twenty. I state what is missing rather than adjudicating on abstracts (§6).

**Six of these nine are nonetheless disposed of at the declaration level**, and that disposition does
not depend on the missing evidence: their declaration carries no proposition at all (§4), so there is
nothing for a source to support. Only **three** — `001↔002`, `019↔032`, `031↔032` — carry a real
proposition *and* lack the evidence to adjudicate it. Those three, and only those three, are the
genuine *additional source required* cases.

| Edge | Shared paper | Why not adjudicated | What would unblock |
|---|---|---|---|
| 001↔002 | none | No shared evidence; endpoints are a clinical drug observation and an organoid model | A source measuring both, or acceptance that this is a hypothesis edge |
| 003↔004 | none | No shared evidence; bare `Wikilinks` both ways | as above |
| 030↔033 | none | No shared evidence; bare "Vedi CLAIM 030" | as above |
| 001↔031 | PAPER 045 | PMID 30361190 — **no local full text** (0 files matching in `files/fulltext/`) | acquire PAPER 045 full text |
| 019↔030 | PAPER 041, 042 | PMID 29808465 closed-access Springer, no PMCID; PMID 24369382 — **neither present locally** | acquire PAPER 041 (the load-bearing Q230P functional source) |
| 019↔032 | PAPER 041 | same | same |
| 019↔033 | PAPER 040 | PAPER 040 is a **review + curated variant dataset**, not primary; §6 forbids resting an edge on it | a primary cohort source for the survival statistic |
| 030↔032 | PAPER 039, 041, 043 | PAPER 039 present; **041 and 043 absent locally** | acquire 041 and 043 |
| 031↔032 | PAPER 049 | PMID 27495153 — **no local full text** | acquire PAPER 049 |

**Denominator for the availability negative:** `files/fulltext/` in the shared checkout holds **174**
entries; the fourteen edge-relevant PMIDs were each matched by filename. Five returned zero:
29808465, 24369382, 24456803, 30361190, 27495153.

🔴 **`files/` is git-ignored** (privacy hard-guard). So the evidence for the adjudicated edges does
not travel with a worktree and is unreachable from any checkout that is not this machine. Everything
in §5 and §6 was read from the shared checkout by absolute path. **A second actor on another machine
cannot reproduce it**, which is a reproducibility boundary of the pilot and not of the science.

---

## 8 · Figure / text discrepancies material to the graph

### 8.1 🔴 The canonical claim cites the wrong panel

`claim_registry_current.md:300`, CLAIM 016 `Evidence boundary`, on the lithium result:

> *"il litio ha soppresso le crisi da PTZ in TUTTI E TRE i genotipi, wild-type incluso **(Fig. 7b**;
> per l'etosuccimide il testo dichiara `n.s.` in `+/+` e `+/−` e significativo in `−/−`…)"*

**The lithium panel is Fig. 7d.** Verified verbatim in the caption — *"d Pretreatment of a GSK3β
inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure activity in Wwox −/− mice"* — and in the
Results — *"(Fig. 7 d)"*. **Fig. 7b is the ethosuximide panel.**

Measured over the whole claim registry with a deliberately permissive pattern
(`Fig(ure|\.)? ?[0-9]+ ?[a-h]\b`): **exactly one figure-panel citation exists in the entire file, in
any form, for any figure — and it is this one, and it is wrong.**

The materiality is not typographic: a reader auditing the claim opens Fig. 7b, finds the panel that
**does** show the genotype-restricted pattern, and concludes the claim is refuted by its own locator.
The registry's single point of contact with a figure panel is a miss.

⚠️ **The correction is not a `7b → 7d` swap.** The parenthetical is compound: its second clause *is*
about ethosuximide, for which `Fig. 7b` is correct. A blind substitution breaks the half that is
right.

### 8.2 The figure uses a significance marker its caption never defines

Fig. 7's caption defines exactly two tokens: *"n.s., non-significant. *** P < 0.001"*. Panel d
carries **`****`** on all three genotype panels. Four asterisks appear nowhere in the caption. A
reader working from the caption cannot decode panel d's marker.

### 8.3 The two drug experiments are not the same experiment, and the paper compares them anyway

Read from the panels at native resolution:

| | Panel b — ethosuximide | Panel d — lithium |
|---|---|---|
| Arms | Control · PTZ · PTZ+ETS | PTZ · PTZ+LiCl — **no Control** |
| `+/+` | Control N=4 · PTZ N=20 · ETS N=16 → PTZ vs ETS **`n.s.`** | PTZ N=12 · LiCl N=8 → **`****`** |
| `+/−` | Control N=5 · PTZ N=18 · ETS N=12 → **`n.s.`** | PTZ N=12 · LiCl N=12 → **`****`** |
| `−/−` | Control N=4 · PTZ N=6 · ETS N=6 → **`***`** | PTZ N=6 · LiCl N=7 → **`****`** |

Three consequences, all graph-material:

1. **Lithium is not genotype-restricted; ethosuximide is.** The drug the paper favours lacks the
   specificity its comparator has.
2. **The wild-type lithium effect was detected with fewer animals** (12 vs 8) than the wild-type
   ethosuximide comparison that returned `n.s.` (20 vs 16). The non-significance of ETS in `+/+` is
   therefore not attributable to a smaller cohort.
3. **No vehicle arm and no LiCl-alone arm in panel d.** A Racine-scale readout cannot separate
   anticonvulsant action from acute lithium sedation without one.

And **no genotype × treatment interaction test appears anywhere.** Every marker is a within-genotype
pairwise comparison. This cuts **both ways** and I record it against my own preferred reading too:
"significant in `−/−`, `n.s.` in `+/+`" does not establish that ethosuximide's effect *differs*
between genotypes any more than three separate `****` establish that lithium's does not.

The paper's own summary claim — *"its efficacy is better than the commonly used anticonvulsant drug
ethosuximide"* — is a comparison across two differently-designed experiments with no head-to-head
test. **Unsupported as stated.**

### 8.4 🔴 An unsupported wording has propagated, and the mirror was only half-corrected

> ⚠️ **Two Phase II corrections to this section, from both peers.** (1) I first wrote *"a disproven
> wording"*. **It is not disproven** — the abundance direction really is upward, by 9–18%, on
> single unstatisticized lanes. A and C independently make the same objection; the wording is
> *unsupported and misdescribed*, not invented, and calling it invented is the same error with the
> sign reversed. (2) I first wrote that the working-model mirror *"is already corrected"*. C is
> right that it is not: `working_model_current.md:164` reads *"not merely elevated abundance"*,
> which still presupposes abundance is elevated. **Half-corrected**, which is the accurate word,
> and the divergence from the claim stands either way.

CLAIM 016's `Summary` (`:296`) reads *"In Wwox-null mice, GSK3β is elevated in cortex, hippocampus
and cerebellum"*. Fig. 7c shows total GSK3β essentially flat and pSer9 falling by 36–52%. Measured
at HEAD `2261a15`, over tracked files, excluding `reviews/scientist-b/` (this record is excluded from
its own reproduction command — recording the negative would otherwise falsify it):

```bash
git grep -lI -iE "GSK3.{0,3}(β|beta) is elevated" HEAD -- . ':!reviews/scientist-b'
```

| Measure | Count |
|---|---:|
| tracked files at HEAD, excluding `reviews/scientist-b/` | 581 |
| …asserting *"GSK3β is elevated"* | **14** |
| …of those, also stating the correction | **1** (`locator_contract_live_test.md`) |

Among the fourteen: the canonical claim registry; `dismech_export_spec.md` where it is assertion
`016-a`, **typed `DATO`**; four blind-review sheets and prompts that put it in front of reviewers as
a reference proposition; five DisMech derivation artefacts; and `therapy_levers.md`, where it opens
*"A2. Lithium (GSK3β inhibition) — the strongest repurposing signal"*.

Meanwhile `working_model_current.md:164` — the BLOCK-2 **mirror** of CLAIM 016 — already carries the
corrected framing: *"now framed as **de-repression** (loss of a physical brake), not merely elevated
abundance"*.

🔴 **The mirror was corrected and the claim it mirrors was not.** Two canonical surfaces disagree on
the one point the figure decides, and the disagreement has been stable long enough to be exported,
blinded and reviewed in the uncorrected form.

⚠️ **A wrong-reason success, recorded for Mirror.** `therapy_levers.md` calls the lithium lever
*"genotype-agnostic"* — which is what Fig. 7d actually shows. It reaches that word by reasoning
*"acts downstream of WWOX loss"*, not from the panel; and in the same sentence it says lithium
*"abolishes seizures"*, which overstates *"suppressed seizure activity"*, and attributes the effect
to GSK3β inhibition, which the experiment does not establish. The right label, the wrong derivation,
two overstatements travelling with it.

---

## 9 · Decomposition candidates (§7 — recorded, not acted on)

**DC-1 · CLAIM 016 compresses SOURCE + RELATION + TARGET across two scales and two papers.**
Title: *"GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency"*.
Latent source `WWOX deficiency`; latent relation `contributes to (via GSK3β hyperactivation)`;
latent target `seizure susceptibility`; latent intermediate `GSK3β activation state`.
The compression is why the edge to CLAIM 035 cannot be typed cleanly: the molecular arm is `DIRECT`
and the phenotype arm is `INDIRECT_UNKNOWN_INTERMEDIATES`, and one node cannot hold both.
`dismech_export_spec.md` §12.3 has already decomposed it into seven heterogeneous sub-assertions
(`016-a` … `016-f`) — two in `ELIGIBILITY_DEBT`, one a duplicate of `035-a1`, three inferences, one
textbook premise, one clinical caveat. **Decomposition would change scientific meaning: it would
stop the claim asserting a mechanism it does not measure.**

**DC-2 · CLAIM 035's title carries four propositions.** Direct inhibition · residue mapping
(388–407/L404) · S9-independence · Tau-dependence. `035-f` — the pS9 false-negative warning — is an
`INFERENZA` that travels inside a `DATO`-typed claim, and it is precisely the proposition that
undercuts CLAIM 016. **Graph materialization is impaired**: a consumer linking to "CLAIM 035" cannot
tell whether it is importing a binding datum or a measurement warning.

**DC-3 · CLAIM 028 is a principle, not a claim, and the graph has no principle node.**
`Type: INFERENZA — principio interpretativo trasversale`; `Source: papers 207, 218, 206, 214 (corpus
181–220)` — corpus stubs, not PAPER records. Two of its four edges (034→028, 035→028) are
*instantiations*. **Decomposition is the wrong instrument here; the right one is a node type.**
Forcing a principle into the claim plane is what makes its edges untypeable.

**DC-4 · CLAIM 038 states its own two hypotheses inside one claim.** Title carries the observation,
both competing explanations, and the fact that neither was tested. Correctly written as prose;
un-materializable as one node. Latent shape: one OBSERVATION node (elevated BUN/creatinine in two
rodent models) with two HYPOTHESIS nodes attached (RTA · seizure-driven hypercatabolism), each
carrying its own source and its own untested status.

---

## 10 · Independence — what held and what leaked

### 10.1 What held

I read no artifact of Scientist A or Scientist C. My adjudication of the §12 questions was completed
in my v1 pilot (committed `2261a15`) and re-verified against the primary artifacts this session
before any peer surface was touched.

### 10.2 🔴 What leaked, declared in full

§3 makes Phase II conditional on all three first-pass artifacts **existing**. Checking existence
required listing peer worktrees. In doing so I ran `git log --oneline -1` on Scientist C's branch and
read the commit **subject**:

> `c55c25c The panel was read before the claim that cites it, and the citation points at the wrong panel`

That subject states a conclusion — the same conclusion as my §8.1. I had already derived and written
§8.1 before this check, and my derivation is self-contained (caption verbatim → Results verbatim →
panel at native resolution → single `Fig. 7[a-d]` occurrence in the registry). Nothing in my finding
came from C. But the leak is real and I record it rather than let it pass.

🔴 **This is a protocol defect, not an individual lapse, and it will recur for every actor.** This
repository's commit-message convention is to state the finding in the subject line. The Phase I
independence rule and that convention are **mutually incompatible**: the mandated existence check
cannot be performed without reading conclusions. Any actor obeying both instructions is contaminated
by the act of obeying.

**Available mitigations, none of which I am authorized to adopt:** check existence with
`git ls-tree --name-only` alone (filenames only — which is how I checked Scientist A, whose artifacts
are untracked and so produced no subject line to read); or route the existence check through an actor
that does not adjudicate; or suspend the subject-line convention for Phase I commits.

### 10.3 A second, structural contamination that predates all three of us

The repository **already contains the answers to the §12 questions**, in tracked files, at
`disease-models/wwox/analysis/locator_contract_live_test.md:375–395` (dated 2026-08-04):

> *"**Figure 7d has three panels — +/+, +/− and −/− — and lithium suppresses seizures in all
> three.**"* · *"Ethosuximide … **is** genotype-specific: Figure 7b marks it non-significant in +/+
> and +/− and significant only in −/−."* · *"**'Elevated' is the wrong word.** … GSK3β is
> **dis-inhibited, not more abundant.**"*

and in CLAIM 016's own `Evidence boundary`, propagated by `BATCH_20260810_005`.

🔴 **No Scientist reading the primary evidence for PMID 32000863 through this repository can be
independent of the repository's own conclusion.** The §12 exercise measures whether three actors can
re-derive a recorded answer, which is a real and useful thing to measure — but it is **not** what the
prompt says it measures. My own v1 pilot does not cite `locator_contract_live_test.md` and did not
find it; that is a gap in my v1 provenance and I record it as mine.

**What is genuinely new in this session, relative to that pre-existing analysis:** §8.1 (the
canonical claim cites the wrong panel, while the analysis file cites the right one), §8.4 (the
propagation count, and the mirror/claim divergence), §5 E-016-035 point 3 (the pS9 readout mismatch
between CLAIM 016's evidence and CLAIM 035's own warning), §3.2 (the dropped link qualifiers), §4
(the causal-vocabulary mismatch), and §6's brain-sparing observation in the rat.

---

## 11 · 🔴 RETRACTED IN PHASE II — a defect I reported in the manifest was in my own tool

**What I wrote in Phase I.** That `deepdive_manifests/PMID22193544.json`'s nine locators matched
`PMID22193544_Wang2012_PMC_JATS.xml` (sha256 `eb6f568d…88268`) only **2 of 9** strictly and 9 of 9
whitespace-insensitively; that the seven failures had one mechanical cause — inline markup around
`β` and subscripted residue ranges extracting with surrounding spaces; and that this **confirmed on
a second paper** the legacy-manifest defect class the PMID 32000863 manifest predicts.

**What is true.** Scientist A re-derived the same surface and reported **9 / 9 strict**. I tested
the difference:

| Tag-stripping | entity-unescape order | Strict matches |
|---|---|---|
| `<[^>]+>` → **space** (mine) | either | **2 of 9** |
| `<[^>]+>` → **empty** (A's) | either | **9 of 9** |

**The nine locators match the artifact strictly, character for character. There is no defect in this
manifest.** `GSK3<italic>β</italic>` collapses to `GSK3β` when tags are stripped to nothing; my
substitution inserted the space I then went on to diagnose. I named the right mechanism and
attributed it to the wrong object.

**What this costs and what it does not.** The retraction removes a finding; it removes no evidence —
all nine Wang 2012 locators are sound, which is what §5's E-016-035 rests on, and that was true under
both measurements. What it does remove is my claim to have confirmed the defect class on a second
paper. **That claim is withdrawn. The class remains predicted and unconfirmed here.**

🔴 **The failure mode, named because it is the one I am most prone to.** I ran a negative control
(a fabricated sentence, correctly not found) and it passed, so the comparison looked validated. A
negative control tests whether the comparison is trivially permissive. **It cannot test whether the
surface being compared against is the right surface.** The missing control was the one A ran without
meaning to: derive the surface a second way and see whether the number moves. When a measurement
depends on a transformation I chose, the transformation is part of the measurement and needs its own
control.

---

## 12 · §17 G — graph contributions, classified

Every edge receives **exactly one** primary disposition. The four buckets partition the twenty; the
flags below them do not, and are marked as flags.

| Primary disposition | Edges | Which |
|---|---:|---|
| **Carry with qualification** | **2** | 009↔034 · 016↔035 |
| **Relation unsupported** | **14** | *(10 with no proposition)* 001↔031 · 003↔004 · 009↔028 · 019↔030 · 019↔033 · 028↔035 · 030↔032 · 030↔033 · 037↔038 · 037↔039 — *(4 with a non-causal proposition and no governed type)* 005↔036 · 005↔037 · 028↔034 · 030↔035 |
| **Relation unresolved** | **1** | 036↔038 |
| **Additional source required** | **3** | 001↔002 · 019↔032 · 031↔032 |
| | **20** | |

**Carry with qualification, in full:**
- `E-009-034` — `CONTROVERSIAL_OPEN`, reciprocal, with the endpoints' non-comparability recorded on
  the edge.
- `E-016-035` — `INDIRECT_UNKNOWN_INTERMEDIATES`, direction `035 → 016` **only**, carrying the
  readout-mismatch limit. The reverse direction falls under *relation unsupported* and is counted
  once, with the edge.

**Flag — architecture-sensitive (5, cutting across the buckets):** 005↔036 · 005↔037 · 028↔034 ·
028↔035 · 030↔035. Each has a real relation that **the governed vocabulary cannot express** —
*bounds*, *refutes the premise of*, *instantiates*, *supplies the assay for*. For four of the five
that relation is written in the registry; for `028↔035` it is latent and I supply it, which is why
that edge sits in *unsupported* on its declaration and carries the flag on its content. A second
relation plane is owed, and creating its vocabulary is Plan's work under §16, not mine.

**Defects for the canonical surface, none applied here (4)**
1. CLAIM 016 `Evidence boundary` cites `Fig. 7b` for a `Fig. 7d` result — compound clause, see §8.1.
2. CLAIM 016 `Summary` says *"GSK3β is elevated"*; the panel shows flat abundance and falling pSer9.
   The working-model mirror at `:164` is only **half**-corrected — *"not merely elevated abundance"*
   still presupposes abundance is elevated (C's objection, accepted) — and the claim is not
   corrected at all.
3. CLAIM 016's molecular evidence is a pS9 western, which CLAIM 035 declares produces a false
   negative in exactly that setting. Neither claim names the other on this point.
4. `therapy_levers.md` A2 — *"abolishes seizures"*, and mechanism attributed to GSK3β inhibition.

All four require `BATCH_COMMIT` and the operator. **Not applied. §16 observed in full.**

---

## 13 · OBSERVATION_SCOPE

**In scope:** the 20 declared claim↔claim edges of the WWOX Pathograph inventory at sha256
`bbc09af4…`; the primary artifacts named in §5–§6 with their fingerprints; the claim and paper
registries at blobs `9f4bcede` and `847879e0`.

**Out of scope and untouched:** node decomposition (recorded only, §9); the 302 relational-proposition
candidates in the export; the working model; DisMech; every role contract; every governance file;
`reviews/mirror/PATHOGRAPH_HOSTILE_REVIEW_MIRROR_v1.md`, which exists in the mirror worktree and
which I deliberately did not open — it is Mirror's plane (§14) and reading it during Phase I would
import a process judgement into a scientific adjudication.

**Reproducibility boundary:** `files/` is git-ignored. Every primary artifact in §5–§6 was read from
`<REPO_ROOT>/files/fulltext/` by absolute path. A reader on another machine
can verify every registry claim and no evidential quotation.
