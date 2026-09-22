# NATIVE-PRIMITIVE SCORECARD — evidence as of 2026-09-22

**Directive:** §21 (native-primitive scorecard), under §24 — *"DO NOT IMPLEMENT THE NATIVE METHOD
YET."* This file **records evidence**. It recommends nothing for implementation, and no primitive
below is shipped.

**Rule of the scorecard, fixed here:** a primitive earns an evidence count only from an instance
where it **changed an outcome** — a conclusion, a grade, a next experiment, or a caught error. A
primitive that merely ran does not count. Failures are counted with the same weight as benefits,
and a primitive with zero recorded failures is marked as *untested against failure*, not as clean.

---

## §1 · The table

| primitive | observed benefit | observed failure | evidence count | candidate status |
|---|---|---|---|---|
| **`diverge_hypotheses`** — force 3–7 mechanistically distinct explanations before choosing one | (a) `DISCOVERY_TRACE` cycle 1: my chosen `D1` was a rediscovery; **`D3`, which survived only because divergence was mandatory, was the one that held** and produced the surviving question. (b) Survival/expression mismatch file: 6 hypotheses → `H3`+`H5` composite, neither of which was my first instinct | **Not yet observed to fail.** Cost is real but small; the risk it carries — that breadth substitutes for depth — has not yet materialised and has not been adversarially tested | **2** | 🟢 **strong candidate** |
| **`preregister_prediction`** — write predictions and the falsifier *before* the search or read | (a) `DISCOVERY_TRACE` §7 committed empty at `fd5bebd`, then searched → `H1` refuted and honestly graded `REDISCOVERY` rather than retrofitted. (b) This session's recursive re-read: `P1`/`P2` **refuted**, and the refutation is what produced the finding — had the question been written afterwards I would have reported "the paper is silent on cerebellum", which is false | **Not yet observed to fail.** Untested against the case where a pre-registered prediction is *so* specific that it blinds the reader to the unpredicted finding | **2** | 🟢 **strong candidate** |
| **`connect_domains`** — import a result from a neighbouring field with an explicit `WHAT TRANSFERS` / `WHAT DOES NOT` split | Lou 2018 (`PMID 29141528`), a protein-engineering paper on an unrelated SDR: **stabilisation and activity were anti-correlated across the entire engineered panel** (all seven more-stable mutants lost activity; best retained 28.7%). This is the single strongest constraint the session has placed on the Q230P chaperone hypothesis, and it came from outside the WWOX corpus. **(b) Atanasov 2007 (`PMID 17314322`), verified first-hand:** a *pathogenic human SDR missense* (11β-HSD2 `Y338H`) functionally rescued by osmolyte and permissive temperature — the existence proof the chaperone argument lacked. 🔴 And the two instances **do not agree**, which is what makes the pair useful: Lou 2018 (engineered stabilisation → activity lost) and Atanasov 2007 (natural destabilisation → activity recoverable) together say the stability and activity axes in an SDR are **decoupled, with a sign that depends on where the lesion sits** | **Not yet observed to fail**, but the failure mode is known and severe: an analogy imported without the `DOES NOT` half becomes a premise. The session has one near-miss of exactly this class (the uncited `SDR homodimerisation` premise amplified into a therapeutic fork) — not from `connect_domains`, but it is the same disease | **2** | 🟢 **strong candidate** (promoted) |
| **`recursive_reread`** — old paper + a question written before re-opening it | Repudi 2021 (`PMID 34747138`), completely read six weeks ago for dose and myelination: the re-read established that the **founding** study's transduction number is NeuN-gated **in cerebellum too**, and that all of its physiology is neocortical by stated coordinates. Scope of `PREMISE: NOBODY_LOOKED` for Purkinje widened from one paper to the programme | **Three of five returns were zero** (`§5.3`) — exit accounting, Leydig/bone/glucose, and the bare 60–70% were all already held. That is the primitive behaving correctly, but it means the yield per re-read is low and the cost is a full-text fetch | **1** | 🟡 **promising, under-evidenced** |
| **`enumerate_baseline_before_scoring`** — before judging anything "new", enumerate *every* repository file bearing the identifier, by listing, not by guessing filenames | Emerged **from its own absence**: §3 of the re-read missed `PMID34747138_partial_locators.md`, a second dossier for the same PMID. Two rediscoveries would have been graded as discoveries. **(b) Same day, different actors:** two delegates independently proposed as a *first* measurement an experiment whose published prior (Johannsen 2018, `PMID 29808465`) sits in the discovery ledger under a heading naming the allele — see `q230p_three_designs_one_experiment_20260922.md` | Its only instance is a **failure**, not a benefit. It has never yet been run *as* a primitive | **2 (both failures)** | 🟠 **identified by defect, twice; still never run deliberately** |
| **`gate_is_not_quantity`** — ask what the *instrument* structurally excludes before reading its number | (a) `NeuN⁺WWOX⁺` excludes Purkinje **and** basket cells ⇒ a cerebellar percentage is a granule-cell measurement. (b) `get_copyright_status.is_open_access` is a **licence** field, not a retrievability verdict ⇒ ORDER, never SKIP. (c) `MAB377` clone A60, ditto. (d) `11beta-hydroxysteroid` tokenises as **one** term, so the family phrase `"hydroxysteroid dehydrogenase"` cannot match it — a **search** gate. (e) TX-007's archive has **two secondaries, ever**, so four rabbit primaries compete for one channel — a **reagent** gate that makes the whole archive marker-blind to Purkinje cells, not merely the 61% figure. Five instances, four domains (antibody, metadata API, query tokenisation, fluorophore channel) | **Not yet observed to fail**; the obvious risk — using it to dismiss any number one dislikes — has not been tested and needs an adversarial case | **3** | 🟢 **strong candidate** |
| **`verify_the_omitted_clause`** — when checking a delegate's or a paper's headline, read what sits *beside* the quoted sentence, because the transmitted clause is chosen for the claim and the adjacent one is chosen for nothing | 🔴 **Six instances across two waves, each the highest-value item of its file.** (a) Atanasov 2007's *"rather than … loss of catalytic activity"* — the clause that decides whether the precedent transfers at all. (b) Hamdan 2006's `BRET_50`-vs-`BRET_max` paragraph — a **second free discriminator**, two paragraphs past the quoted one. (c) TX-007's Methods: an **empty parenthesis** beside a populated one — extraction damage visible only in the neighbouring token. (d) Johannsen's abstract: *"fibroblasts of **one** patient"* — the `n` sits one clause from the result the whole model rests on, and the ledger does not carry it. (e) Chen 2024: the quoted housekeeping collapse is **UV *plus* cold shock**, in COS7, at 4–22 °C, and **30 °C is not among the temperatures studied** — a design rule was resting on evidence that does not cover its own condition. (f) Breton 2021: *"placed **caudal-side down**"* — the clause explaining *why* the cerebellum is removed, which turns "delete one sentence" into "a second block and a second cut plane" | **Not yet observed to fail**, and its cost is the highest on this page: it requires fetching the source rather than trusting the quote. On a correct report it returns nothing | **6** | 🟢 **strongest candidate on this page.** But see §2 — three of the six are corrections to *delegates*, not to *sources* |
| **`outcome_distribution_width`** — an experiment's value is the width of its outcome distribution, not the importance of the quantity it measures | Caught my own endorsement of a host-reference qPCR whose outcome was **arithmetically bounded** (mtDNA ≈0.06 pp, ploidy ≈0.03 % against the 8.75–12.05× needed): *a foreseeable result is a validation, not a discriminator.* Changed the recommended next experiment. **(b) applied prospectively this wave:** Scientist K's soluble/pellet blot has a narrow outcome distribution because *both* competing mechanisms predict less soluble protein; adding a 26–30 °C arm — one plate, no new reagent — makes the same blot separate foldable-but-unstable from fold-incompetent | **Not yet observed to fail.** Untested against the case where a foreseeable result is exactly what a programme needs (a required control) — the primitive as stated would wrongly demote it | **2** | 🟢 **strong candidate** (promoted) |

---

## §2 · What the scorecard says, and does not say

**Revised after the three-Scientist wave of 2026-09-22.** Four primitives now carry two or more
outcome-changing instances — `diverge_hypotheses`, `preregister_prediction`, `connect_domains`,
`outcome_distribution_width` — and two carry more: `gate_is_not_quantity` (5, across four unrelated
instrument classes) and `verify_the_omitted_clause` (3, all in one wave).

**🔴 The finding that should not be buried in a table.** `verify_the_omitted_clause` returned the
single most valuable item in **all three** delegate hand-backs of that wave, and it did so for a
reason that is structural rather than lucky: **a report transmits the clause that supports its
claim, so the adjacent clause is the one nobody has yet had a reason to read.** In one case that
adjacent clause decided whether the whole precedent transferred; in another it supplied a second
free discriminator on data the design already collects; in the third it distinguished a missing
catalogue number from a deleted one. This is the closest thing on this page to a primitive that
pays for itself every time it is run.

⚠️ **The correlation objection I raised this morning is partly answered and partly replaced.**
Three of the six instances came from a second wave and different actors, so they are no longer one
day's single sample. But a sharper objection takes its place: **three of the six are corrections to
delegate *reports*, not to *sources*.** That may be measuring how much a hand-back compresses
rather than a property of the literature. The two cleanly source-side instances — Hamdan's second
discriminator and Breton's `caudal-side down` — are the ones that carry the claim, and there are
**two** of them, not six.

**Still not said.** Only `enumerate_baseline_before_scoring` has ever been **observed to fail**,
and **both** its instances *are* failures — the second (two delegates proposing as novel an
experiment published in 2018) came from a different actor than the first, which is why it counts
as evidence and not as a repeat. Six primitives with no recorded failure remain *untested
against failure*, not clean, and the honest reading of §24 has not changed: **nothing here is
implemented, and nothing is recommended for implementation.**

**The missing instrument, unchanged.** Every row's failure column would fill fastest by running a
primitive deliberately on a case where it should *not* help and recording that it did not. No such
run has been made.

## §3 · Not on the scorecard, and why

- **`census_verify.py`** is a shipped tool, not a reasoning primitive; it is routed in
  `framework/scripts/README.md` §4 and does not belong here.
- **`FLAG FIRST, SCORE ONLY AFTER MECHANISM + REAGENT + ALLELE VERIFICATION`** is standing operator
  law for this session, not a candidate primitive.
- **`stage explicit paths, never `git add -A` while delegates write`** is an operating rule adopted
  after a real incident; it is process hygiene, not a method.
