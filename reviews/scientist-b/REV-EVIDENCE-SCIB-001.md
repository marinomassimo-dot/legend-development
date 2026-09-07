---
REVIEW_ID: REV-EVIDENCE-SCIB-001
OBJECT: the 39 canonical CLAIM records and the PAPER records they cite
REVIEWED_TREE: 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 — identical to `main` (0 ahead, 0 behind)
LEVEL: declared outside the Annex C.1 ladder — see § 0
REVIEWER: scientist-b
AUTHOR: the canonical registries (no single author; findings are addressed to the integrator)
ADJUDICATOR: unassigned — no ACTIVE ORCHESTRATOR_LEASE (lease_state.py → ACTIVE by derivation: 0)
STANDARD: reviews/scientist-b/SCIENTIST-REVIEW-STANDARD-v1.md
date: 2026-08-25
---

# REV-EVIDENCE-SCIB-001 — review of the current WWOX evidence objects

## 0 · Authority and level, declared rather than assumed

Annex C.1 says reviews open only through Orchestrator. There is no Orchestrator: five leases
exist, all `STALE` or `RELEASED`, `ACTIVE by derivation: 0`. This review was opened by direct
operator instruction. It therefore claims **no rung of the C.1 ladder** and is offered as an
evidence-object review under `EVIDENCE → Scientist + Plan/provenance` (Annex C.4), for an
adjudicator to be named.

`roles/scientist.md` is `PROPOSED` and, per `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`, is
**not binding**. No authority in this review is traced to it. Annexes C, D, G, I and J bind on
their own terms and are what this document follows.

🔴 **`scientist-b` is not activated, and this document does not activate it.** The canonical
record at `788c357` states *"BENCH-AB-001 NOT STARTED. Scientist A NOT ACTIVATED. Scientist B NOT
ACTIVATED."* There was no `TASK_ACK`, no `TASK_CLAIM`, no Agent Card registration and no L1/L2
qualification. This review is **operator-directed work performed in the `lettore-b` worktree**,
recorded under that ACTOR_ID for attribution only. It is not a registration, not a capability
declaration, and not evidence that any bootstrap step ran.

## 1 · Preconditions (Standard § 2), all executed on the reviewed tree

| # | Check | Result |
|---|---|---|
| P-1 | Tree named | `788c357`, equal to `main`. The worktree began the session **203 commits behind**; it was fast-forwarded before any measurement was taken |
| P-2 | `legend_lint.py .` | **PASS** (1 INFO: CLAIM 010 background-only, wikilink not required) |
| P-2 | `fulltext_receipts.py verify` | **OK — 128 chained receipts, tail anchored** |
| P-2 | `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 · registry_only 15 · unread_premises 4 |
| P-2 | `public_release_gate.py` | **PASS / BLOCKS 0** (4 pre-existing `[REVIEW]` parent-of-origin notices, none from this review) |
| P-2 | `run_release_regressions.py` | **FAIL — 7 tests, the seven already enumerated in `CAND-20260818-SCIENTIST-AB-SPEC`, reproduced here at a fourth tip. Diagnosed in § 3 F-10** |
| P-3 | `coverage_report.py` / `reading_state.py` regenerated and diffed | **no drift** on this tree (both were stale by 6 receipts on the pre-fast-forward worktree — a branch artifact, now gone) |
| P-4 | Source identifiability | **6 findings** — § 3 F-2, F-5 |
| P-5 | Source reading depth | **joined for all 39 claims** — § 2 table |
| P-6 | Verified readings compared to their claims | done for PMID 25331887 (29 locators) — § 3 F-3 |

## 2 · The population, measured before it was interpreted

Deepest receipt available on **any** paper a claim wikilinks, joined from
`fulltext_read_receipts.jsonl` to `paper_registry_current.md` `Identifier:` fields:

| Deepest receipt among a claim's sources | Claims | of 39 |
|---|---:|---:|
| `complete_fulltext_read` | 22 | 56% |
| `partial_fulltext_read` | 6 | 15% |
| no receipt, but ≥1 PAPER source | 5 | 13% |
| **no PAPER source at all** (only `CORPUS` placeholders, or none) | 6 | 15% |

Of the 11 claims in the bottom two rows, **6 are `consolidated baseline`**: `006`, `007`, `008`,
`018`, `022`, `023`. The other five are `010` (background only), `025`, `026`, `027`
(in observation) and `028` (flagged for review) — statuses that already carry the uncertainty.

🔴 **Stated qualification, because the number is easy to over-read.** "No receipt" is not "never
read". 15 PAPER records carry a legacy full-text declaration with no surviving receipt, and
`growth_anchors` already freezes those 15 identities under `HISTORICAL_DEBT_RATCHET_GATE`. But
`PAPER 007`, `PAPER 008` and `PAPER 025` — the sources of four of the six baseline claims above —
are **in neither set**: they carry no receipt *and* no `Evidence depth` field at all. That is a
third state the ratchet does not currently count.

Reproduction: the join is a dozen lines over the two registries and the ledger; the identities
above are what it returns, and every finding below names its own command.

## 3 · Findings

Ordered by consequence. Each carries the object, the field, and what would make me wrong.

---

### F-1 · `CLAIM 018` is `consolidated baseline` / `DATO` / T1 / HIGH and its own Source field says it rests on an abstract

**Object:** `claim_registry_current.md` → `CLAIM 018`, `Source:` line.

**STEELMAN.** The allele `c.517-2A>G` is a canonical acceptor-site variant; exon skipping is the
expected consequence and the clinical literature treats it as pathogenic. The claim is very
probably true, and the registry has kept it visible rather than hiding it.

**EVIDENCE_AGAINST.** The claim asserts a **measured functional outcome** — *"causes exon 6
skipping in humans"* — while its own `Source` field reads *"Weisz-Hubshman / Piard 2019
**abstract-supported** + prior claim integration"*. Its single wikilink is `PAPER 025` (Piard
2019, PMID 30853297), which has **no `Evidence depth` field and no receipt in the ledger**.
"Weisz-Hubshman" is named in prose and resolves to no record at all.

Per `gold_is_in_the_details.md` rule 8 and `EVIDENCE_SURFACE_BINDING_GATE`, an abstract is not a
reading. `DATO` is defined as *"directly supported by a primary source, traceable, not
extrapolated"*. An object cannot be `DATO` and abstract-supported at the same time, and this one
says both, in adjacent fields.

**Why it matters more than its size.** T1 · HIGH · *"directly relevant because this allele sits
in the reference genotype logic"*. It is load-bearing for how the reference genotype is read.

**VERDICT: WEAKENED.** Not refuted — the biology is likely right. The *epistemic type is not
earned*.

**REFINED_FORMULATION (proposal, not an edit).** Either read `PMID 30853297` and requalify, or
retype the claim to `INFERENZA` with `PREMISE: DEFAULT_FROM_TEXTBOOK` on *acceptor-site variant →
exon skipping* until a primary reports the transcript. Resolve or delete the unlinked
"Weisz-Hubshman" pointer.

**WHAT_WOULD_CHANGE_MY_MIND.** A locator from `PMID 30853297`, or any other source, reporting the
transcript consequence in a human sample — RT-PCR, RNA-seq or minigene. One locator closes this.

**REVIEWER_CONFIDENCE:** high on the defect, low on the biology being wrong.

---

### F-2 · `CLAIM 006` and `CLAIM 007` are `consolidated baseline` on a paper the system itself lists as an **unread premise**

**Objects:** `CLAIM 006`, `CLAIM 007` → `PAPER 007` → (unlinked) `CORPUS-STUB-053`.

**The chain, each link checkable.** `PAPER 007` = *"Hussain 2023 P47T"*, `Identifier: pending
normalization`, no `Evidence depth`, `Claim links: 006, 007`. Its full title in the registry —
*"WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation,
and cerebellar degeneration in mice"* — is carried verbatim by `CORPUS-STUB-053`, which **does**
have an identifier: **PMID 36828035**, `Status: not_processed`, `Claim links: none`.

And `growth_anchors.py measure` returns `unread_premises: [25595186, 35328751, 36271927,
**36828035**]`. The system's own tracker names this paper as never read.

**So two halves of one paper sit in the registry unaware of each other**: the half with the claim
links has no identity, the half with the identity has no claim links, and the tool that would
have flagged the paper as unread cannot see that two baseline claims depend on it — because the
dependency runs through the identifier-less half.

**VERDICT: WEAKENED** (both claims).

**REFINED_FORMULATION.** Normalize `PAPER 007` → PMID 36828035 / DOI 10.1016/j.pneurobio.2023.102425,
cross-link `CORPUS-STUB-053` append-only, and **either** read the paper **or** demote both claims
from `consolidated baseline` until it is read. Both claims are LOW clinical relevance and T3, so
the cost of demoting is small and the cost of leaving them is a precedent.

**WHAT_WOULD_CHANGE_MY_MIND.** A receipt for PMID 36828035, or evidence that `PAPER 007` is a
different publication than `CORPUS-STUB-053` — in which case the finding becomes worse, not
better, because then the source is unidentifiable.

**Note on scope.** `CLAIM 007`'s content (*P47T abolishes PPxY binding*) is independently
supported by `PAPER 042` (Mallaret 2014, complete read, peptide pull-down quoted verbatim in the
registry) — but `CLAIM 007` **does not wikilink it**. The support exists in the repository and
not in the object. That is F-4's problem seen from the other side.

---

### F-3 · `CLAIM 029` states a mechanism at a strength its own verified reading contradicts, while `PAPER 030` understates the reading that exists

**Objects:** `CLAIM 029` `Summary:` · `PAPER 030` `Evidence depth:` ·
`deepdive_manifests/PMID25331887.json` (29 locators, receipt `FTR-20260810-25331887-01`,
`partial_fulltext_read`).

**The claim says:** *"DNA damage promotes **ITCH-dependent K63** ubiquitination of WWOX on
**Lys274**…"*

**The verified reading of that same paper says, in three places:**

| Locator | What the panel shows |
|---|---|
| `entries[18]` + `entries[19]` | The K274 assignment rests on Fig 6A, whose **Input GST row shows markedly less K274R than wild type** with GAPDH even across lanes and **no input-normalised quantification anywhere in the figure**. The paper itself reports K274R as less stable, which makes the confound worse: *"lacked ubiquitination"* cannot be separated from *"was present in smaller amount"* |
| `entries[22]` + `entries[23]` | The catalytically dead ITCH **C830A carries a clearly visible ubiquitin ladder** in the lane the text names as the negative comparison, and more in the damage-treated lane. Reduced, not abolished ⇒ **ITCH is a major contributor, not the sole ligase**. The word *dependent* overstates the panel |
| manifest `note` | The **K63-versus-K48 discrimination is in supplementary S6C**, and the half-life datum in S7B — both in a supplement that is **unretrievable by every sanctioned route** (`FT-053`; PMC and Europe PMC both return not-open-access). *K63* in the canonical claim is carried by the authors' assertion, not by a surface anyone here has seen |

**And `PAPER 030` still declares** `Evidence depth: abstract reviewed (PubMed metadata; full text
not yet extracted)` — 15 days after a 29-locator strict-PASS reading of that PMID.

**Both directions of drift in one object pair:** the claim says more than the reading supports,
and the paper record says less than the reading contains.

**Why `READING_MUST_LAND_GATE` did not catch it.** The manifest's `landing` field is
`['FTR-20260810-25331887-01', 'discovery_ledger_current', 'full_text_queue_current']`. The
reading **did** land — in two non-canonical layers, and the discovery ledger handled it
carefully, including a `PREMISE: NON RISOLTA` on the stabilization. The gate is satisfied. The
canonical claim is still at abstract level. That is Standard § 4 A-4.

**VERDICT: REFINED.**

**REFINED_FORMULATION.** `CLAIM 029` summary → *"…promotes K63-linked ubiquitination of WWOX to
which ITCH is a major contributor (a catalytically dead ITCH mutant does not abolish it), with
K274 named as the acceptor on evidence that is not input-normalised"*, plus `PREMISE_TAG` on the
K63 linkage (supplement unretrievable, `FT-053`). `PAPER 030` evidence depth →
`partial_fulltext_read`, receipt named, supplement gap named.

**WHAT_WOULD_CHANGE_MY_MIND.** Retrieval of S6C and S7B; or an input-normalised repeat of Fig 6A;
or a second paper establishing the ITCH-K274 link independently.

**REVIEWER_CONFIDENCE:** high — every element is a verified locator in this repository.

---

### F-4 · `PAPER 027` and `PAPER 030` are the same paper, with a wrong author on one, and both declare `Claim links: 029`

**Objects:** `PAPER 027` · `PAPER 030`.

Identical `Full title`, identical DOI `10.1073/pnas.1409252111`, identical **PMID 25331887**.
`PAPER 030` names the correct authors (Abu-Odeh, Salah, Herbel, Hofmann, Aqeilan). **`PAPER 027`
attributes it to "Schrock et al."** — the same class of metadata error already corrected once in
this registry, when `PAPER 021` was found to name Kumada instead of Tochigi and to carry an
invented title.

`CLAIM 029` wikilinks only `PAPER 030`. But **both paper records declare `Claim links: 029`**, so
a reader auditing from the paper side sees two mechanistic sources for one claim. There is one.

`EVIDENCE_REUSE_GATE` does not fire: nobody reused a cohort. `CLAIM_MIRROR_PARITY_GATE` does not
fire: it compares `CLAIM` ids, not `PAPER` identifiers. **No existing check reaches a duplicate
inside the paper registry** — Standard § 4 A-3.

Measured over the whole registry: 25331887 is the **only** PMID appearing in the `Identifier:`
field of two distinct `PAPER` records. Every other repeat is a legitimate `PAPER`↔`CORPUS`
placeholder pair, preserved append-only by design.

**VERDICT: REFINED** (a registry defect, not a scientific one).

**REFINED_FORMULATION.** Resolve `PAPER 027` as a duplicate of `PAPER 030`, append-only, using
the pattern already applied to `CORPUS-STUB-085` and `CORPUS-STUB-048`; correct the Schrock
attribution in the withdrawal note; leave `PAPER 030` as the record of account.

**WHAT_WOULD_CHANGE_MY_MIND.** Evidence that "Schrock et al." denotes a genuinely different
publication that was mis-stamped with this PMID and DOI — which would still be a defect, only a
different one.

---

### F-5 · Five claims — two of them `consolidated baseline` — have no identifiable source

**Objects:** `CLAIM 022`, `023` (`consolidated baseline`) · `025`, `027` (`in observation`) ·
`028` (`flagged for review`).

Their only source wikilinks are `CORPUS P216`, `P206`, `P191`, `P214`, `P207`, `P218` — every one
of which carries `Identifier: **PENDING**`, from the 181–220 batch of 2026-04-17. No PMID, no
DOI, no title beyond a topic line.

**The consequence is not that the evidence is weak — it is that the object is unreviewable.**
Review question 4 (*what would falsify this?*) has no answer when nobody can open the source. And
the registry's own consolidation rule — *"at least 3 convergent studies"* or *"a single
high-impact study"* — cannot be evaluated at all: you cannot count studies you cannot identify,
and you cannot judge impact you cannot locate.

**One of the six ambiguities is load-bearing, and it decides a baseline claim.** `CORPUS P206` is
annotated *"likely overlaps `PAPER 026` (PMID 32185845, WWOX–p73 phospho-binding); verify before
merge — flagged for the operator"*, open since 2026-04-17. `CORPUS P206` is the **sole** source
of `CLAIM 023`, which asserts *"WWOX **relocalizes** p73 from nucleus to cytoplasm, reducing
nuclear transcriptional activity"*. `PAPER 026` is Shkedi 2020, `Source type: experimental
biochemistry / **quantitative binding study**`.

Both branches are findings, and there is no third:

- if `P206` **is** `PAPER 026`, a quantitative binding study is being cited for a **subcellular
  relocalization** it does not measure — `MECHANISM_DIRECTNESS_GATE`;
- if `P206` is **not** `PAPER 026`, then a `consolidated baseline` claim's only source is a paper
  nobody can name.

`CLAIM 028` compounds it: it is an `INFERENZA` from *"convergence multi-paper (207, 218, 206,
214)"*, and **independence cannot be assessed** because none of the four is identified. If two of
them turn out to be one paper, the convergence is three, not four.

**VERDICT: WEAKENED** for 022 and 023; **CONFIRMED-as-recorded** for 025, 027, 028, whose
non-baseline statuses already carry the uncertainty honestly.

**REFINED_FORMULATION.** Resolve the six identifiers, or demote 022 and 023 from
`consolidated baseline` until resolved. Resolving `P206` first: it is the one that decides a
baseline claim and is already flagged.

---

### F-6 · `CLAIM 009` — the caveat was appended and the operative sentence was not re-derived

**Object:** `CLAIM 009`, `Clinical meaning:` line.

The claim now carries two counter-directional primaries: `PAPER 054` (mouse diabetic
photoreceptor — WWOX **up**-regulated, siRNA knockdown **reduces** superoxide) and `PAPER 071`
(fly — Wwox loss **lowers** and overexpression **raises** thresholded CM-H2DCFDA, with Wwox×Idh
and Wwox×Sod interactions). The claim states the consequence explicitly and well: *"la direzione
deficienza→ROS non è quindi stabilita come monotona né come indipendente dal contesto"*.

**The `Clinical meaning:` line above it is unchanged:** *"Supports NAC / CoQ10 / creatine / KD
logic, but remains only partially CNS-linked in pediatric WWOX."*

The caveat offered there is about **CNS transferability**. The new evidence attacks something
else — the **sign**. An antioxidant rationale requires deficiency→ROS↑; if the direction is not
established as monotone, the rationale is undercut at its root and not merely at its reach. The
reader who reads the operative sentence and stops — which is what an operative sentence is for —
gets a licence the object's own body withdraws four lines below.

The dossier that introduced the tension (`fulltext_dossiers/PMID21075834.md`) flagged the
**Summary** sentence and its own Strategy space says *"antiossidanti … non possono essere
promossi da questo studio"*. Neither reached the `Clinical meaning` line.

**VERDICT: REFINED.**

**REFINED_FORMULATION.** *"Does not currently support an antioxidant rationale: the sign of
WWOX↔ROS is context-dependent and two primaries run counter. The metabolic branch remains open as
a mechanistic biomarker panel, not as an intervention rationale."*

**WHAT_WOULD_CHANGE_MY_MIND.** A matched-model, matched-stage measurement in a WWOX-deficient
neuron showing ROS↑ with a WWOX-dose rescue — which is also the revival trigger the claim already
records.

---

### F-7 · `CLAIM 032`'s human arm is ascertainment-conditioned, and a dominant human WWOX signal has been read and reaches no canonical record

**Object:** `CLAIM 032` — *"WWOX haploinsufficiency is not deleterious"*, `in observation`, T1/T2,
**VERY HIGH** clinical relevance, cited as redefining *"la soglia di successo di ogni leva del
portafoglio"*.

**STEELMAN, and it is strong.** The animal arm is real and well-quoted: Aldaz 2014 heterozygote
lifespan *"indistinguishable from WT"*, Tochigi 2019 `+/lde` rats at half band intensity with
normal cortical IHC, and the hypomorph-viable / null-lethal contrast placing a threshold below
50%. The claim also carries three limits of its own, including that the threshold is known for
survival and morphology and **not** for cognition or epilepsy.

**EVIDENCE_AGAINST — the human arm.** *"Ogni famiglia umana pubblicata … ha genitori portatori
eterozigoti sani"* is offered as evidence. It is not. Autosomal-recessive families enter the
literature **through** an affected biallelic proband; healthy heterozygous parents are a property
of that ascertainment route, not an observation about heterozygotes. A heterozygote with a
phenotype would be ascertained through a different route entirely and would never be filed as a
"WWOX-DEE family". The observation is true and carries approximately zero information about the
proposition it is cited for. `DENOMINATOR_FIRST_COHORT_GATE` is adjacent but does not fire: there
is no percentage here to inspect — Standard § 4 A-5.

**EVIDENCE_AGAINST — a measurement that exists and is not in the model.** `PMID 18674750` (Lee
2008, *Am J Hum Genet*) has a receipt in this ledger, `partial_fulltext_read`: rs2548861 in WWOX
intron 8 associated with low HDL-C at region-wide significance across 9,798 subjects including
two unascertained Finnish cohorts, with luciferase and EMSA supporting a cis-regulatory
mechanism, and the effect is **dominant** — one copy, ~17% higher probability of low HDL-C.

`grep 18674750` over `paper_registry_current.md`, `claim_registry_current.md` and
`working_model_current.md` returns **nothing**. The paper has no PAPER record, no CORPUS
placeholder, and no claim link.

I do **not** conclude that this refutes `CLAIM 032`: a small dominant regulatory allele on a
quantitative lipid trait is a different object from coding haploinsufficiency, and the reader who
recorded it said exactly that. But a claim whose title is *"haploinsufficiency is not
deleterious"* must carry the one human quantitative measurement of a single-copy WWOX effect this
corpus possesses, if only to bound it.

**VERDICT: REFINED** — status `in observation` is correct and is not challenged.

**REFINED_FORMULATION.** (a) Mark the carrier-parent observation `PREMISE: ASCERTAINMENT-
CONDITIONED — carries no weight for this proposition` rather than listing it as support; the
animal arm stands on its own and is what the claim actually rests on. (b) Add the boundary:
*single-copy WWOX variation has a measured dominant effect on a human quantitative trait
(PMID 18674750, non-coding regulatory, ~1.5% of variance); the claim concerns coding
haploinsufficiency for the CNS phenotype and does not extend to quantitative traits.*

**WHAT_WOULD_CHANGE_MY_MIND.** A carrier cohort ascertained independently of an affected proband
— population biobank heterozygotes phenotyped for cognition or EEG. That is also the experiment
the claim needs and does not have.

---

### F-8 · Reading outruns propagation: 25 papers have a receipt and no `PAPER` record, 11 of them complete reads

Joined from the ledger to the `Identifier:` fields of the 70 `PAPER` records:

- **82** PMIDs carry at least one receipt;
- **25** of them have **no `PAPER` record**; **11** of those 25 are `complete_fulltext_read`;
- **9** of the 25 appear nowhere in the registry at all — not even as a `CORPUS` placeholder:
  `15070730`, `18674750`, `20067585`, `21212533`, `21776376`, `23435430`, `39952983`, `42082822`,
  `42397075`.

🔴 **The count is a ceiling, not a work list.** At least one member is deliberately unpromoted:
`23446842` sits as `CORPUS-STUB-179` under `PUBLICATION_INTEGRITY_HOLD` — retracted, correctly
never promoted. `42397075` is the frozen source of `BENCH-AB-001` and its non-promotion may be
intentional. The actionable set is therefore ≤ 24 and must be triaged, not batch-promoted.

This is the same shape as F-2 and F-3 at population scale, and it is the finding most likely to
grow: the system reads faster than it propagates, which the state manifest already says of
commit candidates. The named instances above show the cost is not bookkeeping — `18674750` is a
first-of-its-kind human measurement that no canonical surface knows exists, and `33255508`
(Aldaz 2020, complete read, no PAPER record) is very likely the identity of the unidentified
*"Aldaz/Banne cluster"* that F-9 is about.

**VERDICT: not a claim-level verdict — a system finding for Plan and the integrator.**

---

### F-9 · `CLAIM 008` is `consolidated baseline` on an unidentified cluster of reviews

`PAPER 008` = *"Aldaz/Banne clinical spectrum"*, `Authors: Aldaz / Banne cluster`,
`Year: 2019–2021`, `Identifier: **multiple / pending normalization**`,
`Source type: **review / clinical spectrum**`. It is the sole source of `CLAIM 008`
(`consolidated baseline`, `DATO`, T1 contextual).

Two defects in one record. A **review** as the sole evidence for a `DATO` baseline claim is the
category error this repository has already ruled on explicitly, when `PAPER 063` was promoted
with the note *"it is a review and is recorded as one — no independent corroboration of the
primaries it enumerates"*. And a record whose identifier is *"multiple"* is not one source; it is
an unbounded set, which is why nobody can count it against the consolidation rule.

**VERDICT: WEAKENED.** The claim's *content* — that WOREE and SCAR12 form a spectrum — is
uncontroversial and supported elsewhere in this registry by primaries (`PAPER 042`, `PAPER 043`,
`PAPER 045`). The defect is that the object does not cite them.

**REFINED_FORMULATION.** Resolve the identity (start with PMID 33255508, Aldaz 2020 — complete
read already in the ledger, F-8), split the cluster into records, and relink `CLAIM 008` to the
primaries that support it, keeping the review as context.

---

### F-10 · The router migration disarmed five of its own guards, and the enumeration exists while the diagnosis does not

**Object:** `scripts/run_release_regressions.py` — `REGRESSION VERDICT: FAIL`, 7 failing tests.

**What is already known, and is not my finding.** `CAND-20260818-SCIENTIST-AB-SPEC` enumerates
exactly these seven test ids at three tips, compares them by parsed assertion text rather than by
count, and records `ADDED ∅ / REMOVED ∅ / SAME-REASON 7/7`. That work is correct and I reproduce
it: **the same seven fail at `788c357`**, six days and many commits later. The enumeration is
honest and the discipline behind it is exemplary.

**What is not recorded anywhere is why.** Five of the seven have **one cause**, and it is
verifiable in two commands:

| Failing assertion | String it requires in `CLAUDE.md` | Before `04cbd3b` | After |
|---|---|---:|---:|
| `test_abstract_corpus_is_not_evidence::test_the_bootstrap_bounds_the_corpus` | `pubmed_corpus_harvest` | 1 | **0** |
| `test_locator_obligation_reaches_every_route::test_the_bootstrap_states_the_rule` | `verbatim_locators` | 1 | **0** |
| `test_fulltext_trace_contract::test_normative_layers_make_receipts_universal` | `FULLTEXT_READ_RECEIPT` | 1 | **0** |
| `test_fulltext_trace_contract::test_normative_write_rules_name_the_append_only_carveout` | `state-control` | 1 | **0** |
| `test_session_self_eval::test_diagnosis_is_wired_before_growth_and_takeaways` | `session_self_evaluation.md` | 1 | **0** |

`04cbd3b` is *"CLAUDE.md becomes a router, after every rule in it was given a canonical home"*.
The migration was deliberate and is documented rule-by-rule in
`governance/design_records/claude_md_migration_map.md`. **The five tests are pinned to a
location, not to an obligation**, so a migration that preserved every rule failed every test that
looked for the rules in the old place.

**The sharpest form of it.** `test_session_self_eval` checks four files for the self-diagnosis
wiring; three still pass and only the `CLAUDE.md` one fails. The *obligation* is intact. What
broke is the **alarm**. And `claude_md_migration_map.md` line 48 records rule 8 — *abstract
corpus is not evidence* — as `PRESERVED`, *"enforced by
`scripts/test_abstract_corpus_is_not_evidence.py`"*, while that enforcement has been red since the
commit the map documents. The map asserts an enforcement the enforcer can no longer perform.

**Why this belongs in an evidence review and not only in Mirror's process review.** The guard
that has been disarmed is the one that keeps *"an abstract is not a reading"* honest — and F-1 of
this review is a `consolidated baseline` `DATO` claim that says *"abstract-supported"* in its own
Source field. The standing state contains exactly the defect the disarmed guard exists to
prevent. I do not claim the guard would have caught `CLAIM 018`: that claim predates the guard,
and the guard is fail-closed at the *writer*, not an auditor of standing state (Standard § 4
A-1). The two facts are adjacent, not causal, and I state them as adjacent.

**A permanently red suite is not a suite. It is a light nobody looks at.** `designed_for_growth`
names this exact hazard — *"a future alarm nobody hears, and the day it means something no one
will look"* — and the seven have now been red across at least four tips.

**The other two failures are unrelated and are the guards working correctly:**
`test_release_runner_verdict` reports `governance/scripts/test_candidate_content_hash.py` as a
tracked test file not registered in the runner — a real, one-line gap that the
every-test-is-actually-run guard exists to catch; `test_release_surface` reports two shebanged
entrypoints without the executable bit, including `framework/scripts/lease_state.py`.

**One difference between my run and the recorded baseline, declared rather than folded in.** My
run shows **7 suites**, the record shows 6 suites / 7 tests. The extra suite is
`framework/scripts/test_surface_census.py`, whose `LiveCorpus` tests read the local evidence tree:
this worktree's `files/fulltext` holds **13** artifacts against **174** in the shared checkout.
That is environmental and is the rule *"a branch carries the manifest, it does not carry the
evidence"* seen from the failing side — not a defect in the suite and not a new failure.

**VERDICT: not a claim verdict — a system finding.**

**REFINED_FORMULATION.** Re-anchor the five assertions to the normative file that now owns each
rule — `gold_is_in_the_details.md`, `fulltext_read_receipt.md`, `session_self_evaluation.md`,
`LEGEND_CORE.md` — or, better, to *the set of files the migration map names as each rule's home*,
so the next migration re-anchors them by moving the map rather than by editing five tests.
Whoever does it owns `scripts/` and `framework/scripts/`; it is not this review's to write.

**WHAT_WOULD_CHANGE_MY_MIND.** Evidence that the five strings were intended to remain in
`CLAUDE.md` and their removal was itself the defect — in which case the repair is in the router,
not in the tests, and the diagnosis stands with its remedy inverted.

## 4 · Axes searched with no finding

Reported because silence on an axis is an incomplete review, not a clean object.

| Axis | Searched | Result |
|---|---|---|
| Claim-mirror parity | all 39 registry statuses vs the BLOCK 2 table in `working_model_current.md`, string-compared | **39/39 agree.** Three rows initially read as mismatches and were not: `001`, `011`, `012` carry the status inside bold markup or with a parenthetical. My parser was wrong, the registry was right |
| Status vocabulary | all 39 against the six legal strings | all valid; LINT concurs |
| Receipt-chain integrity | `fulltext_receipts.py verify` | 128 chained, tail anchored |
| Publication integrity | every `PUBLICATION_INTEGRITY_HOLD` record and its citers | 2 held records (`19936220` EoC-adjacent note; `23446842` retracted). **No canonical claim rests on either**, and both records say so with the verification recorded. Correct |
| Generated-view drift | `coverage_report.py` and `reading_state.py` regenerated and diffed | no drift on this tree |
| Duplicate `CLAIM` ids | registry ids vs mirror ids | none |
| Rescue-comparator discipline on `CLAIM 004` | the claim's own evidence boundary against `deepdive_manifests/PMID34747138.json` | **already done, and done well.** The comparator is written into the claim: g-ratio normalizes, unmyelinated axon count is significant *against* the rescue, three endpoints are never tested WT-vs-rescued, 60–70% transduction, n=3 EM, ketamine. Nothing to add |
| Genotype-specificity of the lithium arm (`CLAIM 016`) | the claim against `deepdive_manifests/PMID32000863.json` | **already caught**: lithium suppressed PTZ seizures in all three genotypes including wild type, and the claim says so with a `REVIVAL_TRIGGER`. Nothing to add |
| Drug-repurposing objects | `therapeutic_strategies_current.md` and the hypotheses ledger for NAC / CoQ10 / creatine | no downstream object cites `CLAIM 009`'s antioxidant sentence; F-6 is a latent licence, not a propagated one |

## 5 · One capability upgrade, proportional and reusing what exists

**`CLAIM_EVIDENCE_FLOOR_RATCHET` — proposed, not built.**

`growth_anchors.py` already freezes the *identities* of 15 `PAPER` records that assert a full-text
reading the current standard cannot certify (`registry_only_fulltext`, under
`HISTORICAL_DEBT_RATCHET_GATE`: do not delete, do not retroactively upgrade, freeze the exact set,
block every new identity, report a falling set as an invitation to lower the baseline).

**The identical mechanism is absent one level up.** No ratchet freezes the *claims* whose declared
epistemic type exceeds the deepest verified evidence reachable from their sources. That set is
measurable today with the join in § 2 and has **6 members**: `006`, `007`, `008`, `018`, `022`,
`023`.

This is not a new mechanism. It is the mechanism that already exists, applied to the second site —
which `CLAUDE.md` names as this system's characteristic failure: *"the failure mode of a system
that grows by accretion is not ignorance, it is **uneven application**"*, with
`append_only_prefix` in the ledger and not the registries as its own example. `PATTERN_ALREADY_
SOLVED_GATE` says grep the vocabulary before inventing; the vocabulary is `ratchet`, and it
returns the paper-level implementation and nothing at claim level.

It will still be informative at the thousandth batch, because it is a frozen identity set that may
only shrink, never a count someone can bump to make a suite green.

**Not built here**, because `framework/scripts/` is not this review's to write and a reviewer who
implements its own finding has reviewed nothing. Offered to whoever owns that contract.

## 6 · AUTHOR_RESPONSE

**Required and outstanding.** Annex C.2: silence is not acceptance. No canonical file was edited
by this review; every `REFINED_FORMULATION` above is a proposal for a `BATCH_COMMIT` that only the
integrator may open.
