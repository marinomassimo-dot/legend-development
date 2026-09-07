# COMMIT CANDIDATE — `CANONICAL_CROSS_CLAIM_CONTRADICTION`: first census over the claim registry

**Candidate ID:** CC-20260826-CROSS-CLAIM-CENSUS-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** structural census over `claim_registry_current.md`, plus adjudication of each candidate
**Change class:** MIXED — one MAJOR (already carried by
[`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md)), one
`NEEDS_SCIENTIFIC_ADJUDICATION` with a concrete cheap resolution, the rest dismissed with reasons
**Target WM:** current at BATCH_COMMIT time
**Batch gate:** intentionally untouched

---

## 0. What this is, and what it is not

A new failure type — **`CANONICAL_CROSS_CLAIM_CONTRADICTION`**: two canonical claims that state
incompatible things about the same entity and endpoint, neither citing the other. The registry
has never been swept for it.

🔴 **The screen is not the finding.** The script returns *candidate pairs*; every one is then
adjudicated by hand against the primaries, and **most are dismissed**. A pair survives only if no
species/region/stage/endpoint difference explains it. Reporting the 40 screen hits as
"40 contradictions" would be the same error this repository keeps paying for — a number that is
about the instrument rather than the corpus.

**Method.** `claim_registry_current.md` → 39 claims → per claim: PMIDs, PAPER refs, model class,
endpoint class, directional terms (`ABSENT`/`PRESENT`, `INCREASED`/`DECREASED`,
`RESCUE`/`NO_RESCUE`, `PROHIBIT`). Pair when a **shared entity** (PMID, PAPER, or model) meets a
**shared endpoint** and **opposing direction**. Strong signals only — no generic NLP, per
instruction.

**Population and denominator.** 39 claims → C(39,2) = **741** possible pairs → **39 screened
positive** → **2 survive adjudication**.

**Reproduction — executable, not prose:**

```bash
python3 framework/scripts/cross_claim_contradiction_census.py
```

🔴 **The committed script is not byte-identical to the scratch version that first ran this, and
the difference is recorded rather than hidden.** The exploratory run returned **40** candidate
pairs; the committed script returns **39**. Two deliberate refinements account for it: a `p47t`
model class was added, and a noisy `\bzero\b` token was dropped from the `ABSENT` pattern.
**Publishing "40" beside a command that prints "39" would be an attestation, not a recipe** — the
same defect as quoting a digest from a run other than the one described. The reproducible figure
is 39.

**Nothing adjudicated below changed**: all five pairs discussed in §1–§3 still surface, and the
refined script ranks `CLAIM 005 ↔ CLAIM 016` (score 7) into view where the scratch run's top-18
cutoff had buried it — so the committed instrument is, on this corpus, strictly the better one.

⚠️ These counts are properties of **this** registry revision and will move with it. Re-run rather
than cite.

---

## 1. `CONFIRMED` — the mouse-seizure contradiction (five claims)

Carried in full by [`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md).
Recorded here in census form only.

- **CLAIM_A:** `CLAIM 005` (`consolidated baseline`) — *"No canonical statement may describe a
  Wwox-null mouse as showing epileptogenesis."* · and `CLAIM 037` (`in observation`) — *"…it is
  explicitly absent in Wwox-null mice"*
- **CLAIM_B:** `CLAIM 004` (`consolidated baseline`, rescues *"crisi"*) · `CLAIM 011`
  (*"ipereccitabilità / SWD su ECoG"*) · `CLAIM 016` (*"lithium significantly suppresses
  PTZ-induced seizure susceptibility"* in Wwox-null mice)
- **SHARED_ENTITY:** the `Wwox`-null mouse
- **SHARED_ENDPOINT:** seizure / epileptiform activity
- **APPARENT_CONTRADICTION:** a prohibition and an absence-claim against three claims that record
  the prohibited fact
- **POSSIBLE_CONTEXT_RESOLUTION:** partial only — *allele*. At least three distinct nulls exist
  (Aqeilan, Aldaz/EIIA, Hsu/NCKU) and Suzuki 2009's survey predates the third. This explains why
  the 2009 negative was *written*; it does not rescue a present-tense claim about "Wwox-null
  mice" in a registry that also contains the positives.
- **NEEDS_SCIENTIFIC_ADJUDICATION:** **no — adjudicated.** `CONFIRMED`.

---

## 2. ~~`NEEDS_SCIENTIFIC_ADJUDICATION`~~ → **`TRUE_CONTRADICTION`** — the two gene-therapy claims imply incompatible dose thresholds

> 🔴 **ADJUDICATED 2026-08-26 — and the prediction below was WRONG.** Appendix Fig S1A of
> PMID 34747138 has since been read at 300 dpi:
> [`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md). **All three Repudi
> vectors are WPRE-free.** The context resolution proposed in this section — that WPRE would
> reconcile the two studies — is **falsified**. The discriminant is excluded, not confirmed, and
> the contradiction is therefore **sharpened**: same lab, same FVB background, same hSynI/AAV9/
> hWWOX architecture, same WPRE status, same RT-qPCR/bGH titration — and Repudi's 3–6× **lower**
> dose outperforms Obeid's LD entirely. This section is left standing as written so the failed
> prediction is legible; §2's original text below is superseded by that candidate.

This one is **new**, is not carried by any existing candidate, and is therapeutically
load-bearing.

- **CLAIM_A:** `CLAIM 004` (`consolidated baseline`, Repudi 2021 *EMBO Mol Med*, PMID 34747138) —
  a single neonatal ICV injection rescues survival, seizures, myelination and behaviour.
  **Dose, from Methods:** *"Approximately 1 µl (2 × 10¹⁰ GC/hemisphere)"* × 2 hemispheres =
  **4 × 10¹⁰ GC total**.
- **CLAIM_B:** `CLAIM 011` (`flagged for review`, Obeid 2026, PMID 42422765) — the flag note
  establishes a **survival threshold between 1.23 × 10¹¹ and 2.63 × 10¹¹ vg**, with the low dose
  explicitly **failing** to rescue survival (death displaced ~20 → ~90 days, then the curve
  reaches zero).
- **SHARED_ENTITY:** `Wwox`-null mouse, AAV9-hSynI-WWOX, neonatal ICV
- **SHARED_ENDPOINT:** survival rescue
- **APPARENT_CONTRADICTION:** `CLAIM 004` reports **full survival rescue at 4 × 10¹⁰**, three-fold
  **below** the dose `CLAIM 011` says **fails**. Read together, the registry asserts both that
  ~10¹¹ vg is a floor and that a third of it suffices.
- **POSSIBLE_CONTEXT_RESOLUTION:** 🔴 **vector configuration, and Obeid 2026 says so explicitly.**
  *"At a dose of 4 × 10¹⁰ vg, exclusion of WPRE was insufficient to rescue lethality in KO mice,
  whereas treatment with WPRE-containing vectors at the same dose resulted in survival."*
  Obeid tested **exactly** Repudi's total dose and found the outcome inverted by the presence of
  WPRE. Repudi's vectors (`AAV9-hSynI-mWwox-IRES-EGFP`, `AAV9-hSynI-hWWOX`) — **WPRE status is
  never stated in the EMBO text (zero occurrences of `WPRE` or `woodchuck`)**.
- 🔴 **`NOT_REPORTED ≠ ABSENT` applies to me here too.** Silence in the EMBO text is **not**
  evidence that Repudi's vector lacked WPRE; the construct map is in Appendix Fig S1A, which this
  session does not hold. I must not resolve this by assuming the convenient reading.
- **NEEDS_SCIENTIFIC_ADJUDICATION:** **YES**, and it is cheap: **read Appendix Fig S1A of
  PMID 34747138.** One figure decides it.

**Why it matters beyond bookkeeping.** If the resolution holds, then **vg dose is not the
transferable quantity across studies — expression is.** `CLAIM 011`'s threshold would be a
threshold *for a WPRE-free hSynI vector*, and any inference of the form *"a clinical WWOX dose
must exceed ~10¹¹ vg"* would be reading a vector-specific constant as a biological one. That is
exactly the class of error `CLAIM 011`'s own flag was raised to prevent, one level up.

**Proposed canonical effect (deferred until the figure is read):** annotate both claims with the
dose *and the vector configuration*, never the dose alone.

---

## 3. `NOT_A_CONTRADICTION` — dismissed, with the resolution named

The screen's remaining high-scoring pairs. Each is recorded so the next census does not
re-litigate them.

| Pair | Screen signal | Resolution |
|---|---|---|
| `CLAIM 004` ↔ `CLAIM 011` *(highest raw score, 15)* | both null-mouse, 5 shared endpoints, `RESCUE`/`NO_RESCUE` | **Artefact of vocabulary.** Both describe rescue; both texts contain "increase" and "decrease" because rescue raises myelin and lowers gliosis. Complementary, not opposed — *except* on dose, which is §2 |
| `CLAIM 011` ↔ `CLAIM 031` | `RESCUE`/`NO_RESCUE`, shared PAPER 011, seizure endpoint | **Different intervention and species.** 031 is about anti-seizure *drugs* in *humans* not rescuing development; 011 is *gene therapy* in *mice*. No common proposition |
| `CLAIM 037` ↔ `CLAIM 038` | shared PMID 17803050, rat model, seizure + survival | **Different endpoint.** 038 is BUN/creatinine; seizures enter only as a candidate *explanation* for hypercatabolism, in the rat, where they are documented |
| `CLAIM 037` ↔ `CLAIM 039` | shared PMID 17803050, rat, `ABSENT`/`PRESENT` | **Different phenotype.** 039 is ataxic gait penetrance; "absent" refers to cerebellar pathology, not seizures |
| `CLAIM 014` ↔ `CLAIM 015` | `PROHIBIT` vs `PRESENT` | 🔴 **Well-formed prohibition — the contrast case.** *"'developmentally pre-wired' must not be read as 'prenatally demonstrated'"* constrains an **inference from a phrase**. `CLAIM 005`'s bans a **class of fact about an entity**. Same registry, two shapes, one correct |
| `CLAIM 005` ↔ `CLAIM 038` | shared PMID 19936220, `PROHIBIT`/`PRESENT` | Subsumed by §1; 038's seizure mention is rat-scoped |
| `CLAIM 009` ↔ `CLAIM 034` | `INCREASED`/`DECREASED`, shared PAPER 054/071 | **Different direction of perturbation.** 009 is WWOX *loss*; 034 is WWOX *up-regulation* under metabolic stress. Opposite manipulations may licitly have opposite signs |
| `CLAIM 032` ↔ `CLAIM 033` | `ABSENT`/`PRESENT`, human, survival | **Consistent.** "Haploinsufficiency not deleterious" and "biallelic null worse than missense" are the same monotone dose-of-function story |
| `CLAIM 031` ↔ `CLAIM 032` / `CLAIM 033` | shared PAPER 045/018 | Different propositions on a shared source; no opposing assertion |

---

## 4. What the census says about the registry as an object

Three observations, each of which is a capability finding rather than a scientific one.

1. **The failure mode is uneven application, not ignorance** — the pattern CLAUDE.md already
   names. The registry *contains* the correct prohibition shape (`CLAIM 015`) and the correct
   `NOT_REPORTED ≠ ABSENT` discipline. Both were applied at one site and not carried to the next.
2. **A prohibition is the highest-risk object a claim can contain.** It is the only construct that
   can make the registry *self-violating*, and it is invisible to LINT, which validates links,
   statuses and IDs — not whether one claim forbids what another asserts. **One prohibition in 39
   claims was malformed; there is no check that would have caught it.**
3. **Claims cross-reference by wikilink but not by contradiction.** `CLAIM 037` and `CLAIM 011`
   sat in the same file for seven weeks stating opposite things about the same animal, and
   **neither cites the other**. Adjacency in a registry is not adjacency in reasoning.

---

## 5. Proposed capability micro-upgrade

Add `CANONICAL_CROSS_CLAIM_CONTRADICTION` as a **LINT `WARN_BUT_PROCEED`** check, not a blocker:

- flag any claim containing a prohibition pattern (`may not`, `must not`, `No canonical statement`,
  `nessun[a] claim/statement`) **whose object is an entity+endpoint that another claim asserts**;
- report the pair, never adjudicate it — a genuine contradiction and a species difference look
  identical to a matcher.

🔴 **Scale note, stated out loud as required.** This screen is O(n²) over claims: 741 pairs at
n = 39, ~500 000 at n = 1000, ~50 M at n = 10 000. **It will not survive the thousandth batch in
this form.** Before it ships it must be re-cast as an index over (entity, endpoint) buckets, which
is linear in claims and quadratic only within a bucket. Writing this down now is cheaper than
discovering it when the registry is large and the check silently starts timing out — the exact
"future alarm nobody hears" the growth section warns about. **The limit is carried in the script's
own docstring**, not only here, so it travels with the tool rather than with this candidate.

**No silent caps:** the script prints `NOT SHOWN: N further pair(s) below the --top cutoff`
whenever its display limit truncates the list. A screen that quietly shows 18 of 39 reads as
coverage it does not have.

---

## Review required

§1 requires operator authorization via
[`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md).
§2 requires **one figure to be read** (PMID 34747138, Appendix Fig S1A) before any canonical
effect. §5 is a proposal, not an edit.
