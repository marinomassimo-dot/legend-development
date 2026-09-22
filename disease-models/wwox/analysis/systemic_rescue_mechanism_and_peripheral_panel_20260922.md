# The systemic rescue paradox — how a neuron-restricted vector rescues a death attributed to the periphery, and the smallest panel that could tell the mechanisms apart

**Node:** `SYSTEMIC_RESCUE_MECHANISM` · **Actor:** Scientist C · **Date:** 2026-09-22
**Class:** analysis-only, non-canonical.

> 🔴 **Nothing here is medical advice.** `BLOCK-1` holds. No dose, no route, no schedule, no clinical
> framing appears anywhere in this file. Every clinical question is `HUMAN_REQUIRED` and belongs to a
> treating team.
>
> **READ-ONLY** toward the four scientific current files, every registry, every therapeutics `*current.md`,
> every queue, every ledger, every receipt and the state manifest. Nothing promoted, nothing committed,
> no `BATCH_COMMIT`, no receipt claimed, **no git command executed**, no external contact, no purchase.
>
> 🔴 **No researcher was contacted and none will be.** The `COMMUNITY_FOLLOWUP` entries in §5 are
> **internal artefacts only** — a form for recording what an existing programme's own material makes
> answerable next. They are not correspondence, not drafts of correspondence, and not addressed to anyone.
>
> **Public edition.** Disease-level reasoning over the **WWOX-DEE genotype class**. No individual appears.
>
> 🔴 **Alleles, drivers and species are never pooled.** `Wwox`-null (Aqeilan), `Wwox^ΔCre/ΔCre` (EIIA-Cre,
> Aldaz), the two independent NCKU nulls, `gt/gt`, `P47T`, Synapsin-Cre `S-KO`, Nestin-Cre `N-KO`,
> Alb-Cre `Wwox^hep−/−`, ACTA1 `Wwox^ΔSKM`, rat `lde/lde`, human WOREE and human SCAR12 are **different
> objects** and appear in different rows throughout.
>
> 🔴 **The `gt/gt` hypomorph has no published brain WWOX quantification and no neurological phenotyping.**
> It appears in no row below and supports nothing here. That is a MISSING MEASUREMENT, never evidence.

---

## 0 · `enumerate_baseline_before_scoring` — scope declared before any absence is claimed

**Listed first, then grepped over what was listed. No filename was guessed.**

| Axis | Scope of every sweep in this file |
|---|---|
| **Enumeration** | `find` over `disease-models/wwox/` → **430 `.md`, 102 `.json`, 11 `.jsonl`, 19 `.csv`, 5 `.tsv`, 25 `.py`, 15 `.png`, 2 `.pdb`**. Enumerated, then swept. |
| **FILE-TYPE SCOPE** | 🔴 **UNSCOPED.** No `--include=*.md` anywhere. Every load-bearing number below was recovered from `.json` (`deepdive_manifests/`, `page_adjudications/`) or `.jsonl`, which a Markdown-scoped grep cannot see. |
| **LANGUAGE SCOPE** | 🔴 **BILINGUAL EN/IT.** `acidosis\|acidosi`, `spleen\|milza`, `platelet\|piastrin`, `hypocalc\|ipocalcem`, `h[ae]matopoie\|emopoie\|ematopoie`, `bone\|osso\|ossea`, plus `latte`, `svezzam`, `digiuno`, `sopravvissut`, `promotore`. |
| **DOCUMENT CLASS** | analyses · dossiers · partial-locator files · deepdive manifests · page adjudications · commit candidates · the four current files · queues · ledgers · receipts · session evaluations · seed corpora. |
| **Word boundaries** | `\bbone\b` (not *backbone*), `\bBUN\b` (not *abundance*), `\bmilk\b`/`\blatte\b`, `\bALT\b` in context. |
| **External fetches in this act** | 🔴 **NONE at the time of writing §§0–3.** Every value in §§0–2 is a prior-session attestation carried with its locator. **No zero in this file is a PubMed count of mine.** |

🔴 **The hardest bound, stated first and repeated from the prior audit because it still holds:**
**`files/fulltext/` does not exist in this edition.** Every surface below is named by its locator and its
SHA-256; **no binary is on disk here.** Nothing in this file is a read I performed on a paper. Everything
first-hand in this file is first-hand **against the repository**, and is tagged that way and not more.

### 0.1 · 🔴 A NEW TOOL TRAP, tripped on myself in-act and recorded rather than hidden

> **`grep -E` with a BRE-escaped alternation (`\|`) silently searches for a LITERAL PIPE. No error, no
> warning, exit status 1, count zero.**

My first baseline sweep ran twelve patterns of the form `grep -rilE 'hSyn\|synapsin'`. Under `-E` the
alternation operator is `|`; `\|` is an escaped literal. **Every one of those patterns searched for a
string containing a pipe character, and every one returned 0.** The corrected run:

| pattern | as `-E` with `\|` | corrected |
|---|---:|---:|
| `hSyn\|synapsin\|sinapsin` | **0 files** | **78 files** |
| `vector genome\|vg/dg\|vgcn` | **0** | **22** |
| `tropism\|tropismo` | **0** | **13** |
| `milk\|latte` | **0** | **51** |
| `wean\|svezzam` | **0** | **22** |
| `ketone\|chetoacid` | **0** | **8** |

⇒ **This is failure mode (9)/(11)'s sibling in the query engine rather than the corpus, and it is worse
than both, because it is invisible by construction:** the patterns that returned non-zero in that same
run (`suckl`, `catabol`, `biodistribut`) were exactly the ones with **no alternation**, so the run *looked*
internally consistent. A sweep in which every multi-term pattern returns 0 and every single-term pattern
returns a number is **not** a finding about the corpus; it is a syntax error wearing a result's clothes.

🔴 **THIRTEENTH failure mode, proposed for the catalogue:**
> **A negative count from an alternation must be validated by a positive control INSIDE the alternation.**
> `grep -E 'hSyn|zzzznotarealterm'` must return the `hSyn` files. If it returns 0, the operator is broken,
> not the corpus. This is the repository's own *"always carry a positive control with every negative
> count"* rule, applied to the **syntax** of the query rather than to its subject.

⚠️ **Scope of the damage, bounded honestly.** I re-ran every affected pattern before using any of it, and
**no number in this file descends from the broken run.** I have **not** audited prior files for the same
error and I am not asserting that any of them contain it — that is `CNE-C6`, §7.2.

---

## 1 · THE PARADOX, RESTATED AS AN ASYMMETRY OF EVIDENCE — not as a mystery

The brief's question is *"how does neuron-directed replacement rescue survival when lethality has been
attributed partly to peripheral abnormalities?"* **Before hypothesising a mechanism, the two halves of
that sentence must be graded, because they are not at the same evidence grade and the gap between them
is most of the paradox.**

### 1.1 · What "rescues survival" is attested by — `INHERITED`

`INHERITED` from [`tx007_animal_flow_survival_validity_20260922.md`](tx007_animal_flow_survival_validity_20260922.md) §8.1 and
[`peripheral_phenotype_denominator_audit_20260922.md`](peripheral_phenotype_denominator_audit_20260922.md) §4:

🟢 A large, formally tested, twice-observed survival benefit at `2.63E11` vg of `−WPRE AAV9-hSynI-hWWOX`
in this colony; a formally tested partial benefit at `1.23E11` vg that does not reach rescue.
🔴 **Not** licensed: equivalence to wild type, a continuous dose–response, a transferable threshold, or
any statement about the fate of an individual animal.

### 1.2 · What "attributed to peripheral abnormalities" is attested by — `FIRST-HAND` against the repository

Source: `PMID 19936220` (Ludes-Meyers 2009), **`Wwox^ΔCre/ΔCre` EIIA-Cre mouse, P18** — verified in-act
against `research/deepdive_manifests/PMID19936220.json` (23 adjudicated locators) and
`research/fulltext_dossiers/PMID19936220.md`.

| Limb of the attribution | What was actually measured | 🔴 What the same page also says |
|---|---|---|
| **Metabolic acidosis** | **Total CO₂ `14.50±3.5` vs `21.67±0.333` mEq/L, `p=0.006227`** — Table 3, **WT n=3, HET n=3, KO n=4** | 🔴 **KO SEM is 10× the WT SEM.** ⚠️ And see §1.3 — **no pH, no pCO₂, no anion gap, no lactate was measured anywhere in this paper or any other** |
| **Renal failure / uraemia** | **BUN 37.25 vs 17.67 mg/dL, `p=0.01086`** | ⚠️ **Creatinine never measured in this model.** In the **rat**, where creatinine *was* measured, *"kidneys histologically normal, no proteinuria"* |
| **Renal tubular acidosis as the CAUSE** | WWOX IHC in **kidney only**, **n=1 per genotype**, the KO section doubling as the antibody-specificity control | 🔴 *"supports the renal-tubular-acidosis hypothesis **by expression localisation rather than by function**"* — the repository's own adjudication of Figure 6 |
| **Impaired haematopoiesis / leukopenia** | **WBC 4.2 vs 9.45 ×10³/µL at `n=2` per genotype, 🔴 no test run**; 3% NRBC in **1 of 2** KO examined | ⚪ **RBC, Hb and platelets were never counted.** `platelet\|piastrin\|thrombocy` → **0 files repo-wide before this session** |
| **Splenic atrophy / thymic thinning** | spleen **0.21% vs 0.53%** body weight, `p=0.0015`; thinned thymic cortex (Fig 4, read as image) | 🔴 **Both are RATIOS to body weight, and body weight is itself the phenotype** — see §1.4 |
| **Bone / mineralisation** | **BV/TV 13.35→5.8%**, Md.V/TV 13.3→5.7%, microCT + Von Kossa | 🔴 **KO n=3 vs POOLED WT+HET n=5**; figure caption says `*p<0.05` while the Results text says `p<0.01`; the osteoid limb is `p=0.07` and *"tended"* in Results, restated as *"We observed"* in the Discussion |
| **Hypocalcaemia** | **Ca 10.18 vs 11.13 mg/dL, `p=0.000385`** | ⚠️ **The effect is −8.5%** — statistically strong, biologically small. Phosphate never measured in this model |
| 🔴 **The causal claim itself** | *"we **hypothesize**"*, *"we **speculate**"* — the authors' own verbs | *"impaired hematopoiesis can **also be a contributing factor** to metabolic acidosis and death"* |

### 1.3 · 🆕 `FIRST-HAND` — the acidosis limb was never measured as acidosis

**Applying `verify_the_omitted_clause` to the headline the whole paradox rests on.**

The quoted headline is *"significant **hypocapnia** suggesting a state of **metabolic acidosis**"*. The
sentence beside it, in Table 3, is the only measurement behind it: **a single serum `Total CO₂` value.**

Three things follow, and the repository holds none of them:

1. 🔴 **`Total CO₂` on a chemistry panel is not `pCO₂`.** It is ≈ bicarbonate plus dissolved CO₂ — a
   *metabolic* quantity. **Calling it "hypocapnia" names a respiratory quantity that was not assayed.**
   The word is wrong for the measurement, in the primary, and it has been carried forward verbatim.
2. 🔴 **Without pH, a low total CO₂ does not establish acidosis.** A low bicarbonate is equally the
   *compensation* for a chronic respiratory alkalosis as it is the *lesion* of a metabolic acidosis.
   Distinguishing them requires pH. **`blood gas\|emogasanal` → 0 files, unscoped, both languages.**
3. 🔴 **Without an anion gap there is no route to a mechanism.** `anion gap\|gap anionic` → **0 files,
   unscoped, all file types, both languages, entire repository.** A renal tubular acidosis is
   *normal*-gap; a lactic or ketoacidosis from a starving, hypoglycaemic, growth-arrested pup is
   *raised*-gap. **The single measurement that would separate the authors' own hypothesis from its most
   obvious alternative is a subtraction of numbers that were never all measured in the same animal.**

> 🔴 **THE STATEMENT.** **No measurement of blood pH, pCO₂, anion gap or lactate was identified in any
> WWOX animal, in any allele, strain or species, within the analyses, dossiers, partial-locator files,
> deepdive manifests, page adjudications, commit candidates, the four current files, the queues, the
> ledgers, the receipts or the seed corpora of this repository, in either English or Italian, unscoped
> by file type, using the queries `blood gas|emogasanal`, `anion gap|gap anionic`, `\bpH\b` in blood
> context, `lactate|lattato`, `hypocapni|ipocapni` and `bicarbonat`.** Positive control: `bicarbonat`
> returns **5 files** and `Total CO2` resolves to the Table 3 row, so the sweep reaches the right pages.
>
> ⇒ **"Metabolic acidosis" in the WWOX literature is a one-word inference from one analyte, in four
> animals, at one timepoint, in one model, with ten-fold excess variance, never revisited in 17 years.**

### 1.4 · 🆕 `FIRST-HAND` — the repository already learned the trap that invalidates half of §1.2, and has not applied it

`CLAIM 036` records, in the same paper, that brain weight is *"**brain sparing in cachessia, non
crescita**: assoluto 0.390 → 0.356 g (−8.7%), relativo 5.0% → **8.5%**"* and warns that
*"importarlo senza il rapporto inverte la biologia."*

🔴 **That warning has never been carried to the other organ-weight endpoints in the very same table.**
**Spleen at `0.21%` vs `0.53%` of body weight is the identical construction** — a ratio whose
**denominator collapsed by ~40%** (4.2 g vs 7.07 g at P14, growth **arrest** from day 10).

⚠️ **This does not overturn the splenic finding.** The spleen ratio moves **down** while the brain ratio
moves **up**, so the denominator effect works *against* the splenic result and the finding survives it —
**it is, if anything, understated.** But it makes the *magnitude* uninterpretable, and it makes the
endpoint's behaviour **after rescue** ambiguous in a way nobody has flagged:

> 🔴 **In a treated animal whose body weight is restored, the denominator of every organ-weight ratio is
> restored too. A spleen ratio that "normalises" after treatment may record a recovered spleen, a
> recovered body, or both — and the ratio alone cannot say which.** Any panel that scores spleen or
> thymus must report **absolute organ mass AND the ratio AND body weight**, or it produces a number that
> cannot be attributed. This is the single cheapest design error available in §2 and it is one balance
> reading away from being avoided.

### 1.5 · 🆕 `FIRST-HAND` — the untreated baseline is survivor-conditioned, and the repository applies that lens only to the treated arm

The repository flags survivor conditioning **repeatedly** and **exclusively** for `TX-007`'s treated
cohorts (`denominator_audit_therapeutic_portfolio_20260922.md` ×4,
`discovery_survival_expression_mismatch_20260922.md`, `therapeutic_routing_and_endpoint_hardening.md`).
🔴 **It has never been applied to the untreated-KO chemistry that defines the peripheral phenotype.**

From the same manifest, first-hand: *"As early as 72 h after birth **43% (15 of 35)** of Wwox KOs had
died and **77% had died by 17 days**"*, and the growth curve's *"**survivor-biased n = 8** at day 17"*.

> 🔴 **Table 3's four knockouts were bled at P18 — out of a cohort ~77% dead by P17. The numbers that
> define "the peripheral phenotype of WWOX loss" come from the surviving quartile.**
>
> **And the direction of the bias is the uncomfortable one.** If the survivors are the least affected,
> the true KO derangement is **worse** than Table 3 — which strengthens the phenotype and weakens
> nothing. But the **variance** is then the signal, not the noise: `±3.5` against `±0.333` is what a
> collapsing, heterogeneous population looks like, and **it is equally what a mixture of two populations
> looks like** — some animals acidotic, some not. 🔴 **At n=4 those are indistinguishable, and a mean
> from a mixture is a number no rescue experiment can be scored against.**

⇒ **Consequence for every hypothesis in §3:** *"does treatment normalise analyte X"* presupposes that
untreated X has a **distribution**, not a point. It does not yet have one.

### 1.6 · 🔴 THE STRUCTURAL CONSTRAINT THAT DETERMINES THE WHOLE PANEL — 🆕 `FIRST-HAND`

> **The untreated `Wwox`-null dies at ~3 weeks. Therefore, for every peripheral endpoint measured beyond
> ~P21, there is NO POSSIBLE untreated-KO comparator — not because nobody ran it, but because the
> comparator cannot exist.**

This is not a gap that money or effort closes, and it has four consequences the repository does not state:

1. **Every peripheral endpoint in an adult treated animal is necessarily a treated-vs-WT comparison.**
   That answers *"is the treated animal normal?"* — it **cannot** answer *"did treatment correct it?"*
   The two questions have been used interchangeably in the framing of this paradox.
2. 🔴 **The only window in which the full three-arm design (WT / untreated-KO / treated-KO) is physically
   available is ~P14–P18.** Not P30, where every `TX-007` expression measurement sits. Not P240/P300.
   **The rescue-mechanism question and the expression measurements are in non-overlapping time windows.**
3. **The fertility and breeding data are therefore an ABSOLUTE readout, never a relative one** — and the
   repository's note that the `TX-007` fertility panel has *"NO untreated-KO comparator"* is correct but
   under-stated: it is not a reporting omission, it is **structurally impossible**.
4. ⇒ **Any panel proposed in §2 must be timed at P14–P18 or it forfeits its own control arm.** This is
   the single design decision in this file with the largest effect on what the panel can conclude, and
   §2 is built on it.

### 1.7 · 🆕 `FIRST-HAND` — the breeding scheme is an unrecognised whole-organism peripheral bioassay

`INHERITED` (as a **confound**) from `tx007_animal_flow_survival_validity_20260922.md` §9, Methods verbatim:
> *"**Heterozygote or KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were used for breeding** to
> generate KO mice."*

That file reads this — correctly, and it is the right reading for its own question — as an **unbounded
maternal confound**. 🔴 **Read against MY question it is also something else, and nobody has read it that
way: it is evidence, already published, that some peripheral physiology is rescued.**

A treated `Wwox`-null **dam** must, to appear in that sentence at all: survive to sexual maturity; conceive;
sustain gestation; deliver; and **lactate well enough to rear pups that then entered the paper's other
arms** — with *"litter sizes comparable to WT"* (S4C–S4E). Gestation and lactation are among the most
demanding integrated tests of calcium mobilisation, energy balance, renal clearance and haematopoiesis
that exist in a mouse, and they are imposed **on top of** the animal's own phenotype.

> 🎯 **An animal with BV/TV at 43% of wild type, a bicarbonate of 14.5 mEq/L, uraemia and splenic
> hypocellularity does not raise a normal-sized litter to weaning.** That the treated KO dams did is a
> `DATO`-grade **whole-organism** statement that substantial peripheral function is present in the
> treated adult.

🔴 **Four bounds, stated with the finding and not after it, because they are what make it usable:**

| Bound | Why it matters |
|---|---|
| **It is an INTEGRATED readout, not an analyte.** | It bounds *function*. It says nothing about bicarbonate, platelets or BV/TV individually, and **cannot** be substituted for §2's panel. |
| **It is `n≈3` with no untreated-KO comparator** — and per §1.6 **that comparator cannot exist.** | So it is an absolute statement ("treated adults reproduce"), never a relative one ("treatment restored reproduction"). |
| 🔴 **It is measured in ADULTS, and the lethal window is P14–P21.** | It is therefore evidence about **hypothesis R2** (survival without normalisation) *in the survivor*, and **no evidence at all** about the window in which animals die. |
| **It is survivor-conditioned by construction.** | Only animals that lived to breed can be bred from. **The dams are the ~80% plateau, not the cohort.** |

⇒ **Correctly stated:** *treated `Wwox`-null adults that survive to reproductive age have peripheral
function sufficient for gestation and lactation.* Not *"the peripheral phenotype is rescued."*

---

## 2 · THE HYPOTHESES — 🔴 `diverge_hypotheses`, WRITTEN AND PERSISTED BEFORE ANY TARGETED SEARCH

> 🔴 **§§2–3 of this file were written to disk BEFORE the targeted searches of §4 were run.** §4 was
> deliberately empty at the moment of writing. **That ordering is the experiment**, and it is the only
> thing that makes a `CONFIRMED` in §4 worth anything.

**Distinctness rule enforced on myself: two hypotheses are distinct only if they predict a DIFFERENT
MEASUREMENT. The discriminator column is the whole value of this table; a row that cannot fill it is not
a hypothesis, it is a paraphrase.** The brief's seven candidate classes are ranked, merged and added to.

| # | Mechanism class | What it asserts | 🎯 **DISCRIMINATING MEASUREMENT** — the column that earns the row |
|---|---|---|---|
| **R1** | **CENTRAL CONTROL** | Neuronal WWOX restores hypothalamic / brainstem / autonomic control; the peripheral derangements are downstream of it and normalise **as a set**. | The panel at **P14–P18**, three arms. R1 predicts **coordinated** normalisation on the **same schedule as glucose**, and — critically — **normalisation that survives adjustment for body weight**. |
| **R2** | **SURVIVAL WITHOUT NORMALISATION** | The derangements persist in treated animals; they were never the lethal limb. | **The same panel, read for PERSISTENCE.** A treated animal that is *alive and still acidotic* refutes the causal attribution directly. 🔴 **This is the only hypothesis whose confirming result is an ABNORMAL value**, which makes it the one a "rescue" framing is least likely to look for. |
| **R3** | 🆕 **NUTRITIONAL / CATABOLIC SECONDARY** | The panel is not a set of organ-autonomous WWOX phenotypes but the **stereotyped syndrome of growth arrest and undernutrition** in a neurologically disabled pup. CNS rescue restores feeding and competition; everything else follows the body weight. | 🎯 **BODY WEIGHT AS A COVARIATE, and a WEIGHT-MATCHED comparator.** Under R3 the analytes track **body weight across animals regardless of arm**; under R1 they track **arm/transgene after adjusting for weight**. 🔴 **Same panel, different analysis — R3 costs one column, not one experiment.** The decisive arm is a **weight-matched / growth-restricted WT**, which reproduces the whole panel under R3 and none of it under R1. |
| **R4** | **OFF-CNS TRANSGENE OR VECTOR** | The restriction premise is wrong: vector genomes or protein reach peripheral compartments and act locally. | 🎯 **VECTOR GENOME COPIES (qPCR/ddPCR) IN PERIPHERAL ORGANS** — *not* protein. **Transduction ≠ expression**, and every WWOX measurement made outside the brain to date is a **protein blot**. Predicted decisive tissues: **bone, spleen, bone marrow, kidney, liver**. |
| **R5** | 🆕 **DEVELOPMENTAL PREVENTION, not correction** | Treatment at P0 precedes the derangements; they **never develop** rather than being corrected. Distinct from R1, which corrects an established lesion. | 🎯 **THE TIME COURSE IN THE UNTREATED KO — P3 / P7 / P10 / P14 / P18.** If the analytes are normal at P7 and deranged at P18, they are **late and preventable**; if deranged at P3, they precede any plausible treatment effect. 🔴 **This needs NO treated animal at all**, and it is the cheapest decisive experiment in the file. |
| **R6** | **SURVIVOR SELECTION** | Treated survivors are a biologically selected subgroup. | 🎯 **The panel in treated animals that DIE**, plus a landmark analysis — i.e. **measure before the outcome, not after it**. 🔴 Per §1.5 this cuts **both ways**, and nobody has applied it to the baseline. |
| **R7** | 🆕 **THE ATTRIBUTION WAS NEVER A MEASUREMENT** | *"Peripheral abnormalities cause death"* is a hedged 2009 speculation (*"we hypothesize"*, *"we speculate"*), supported by **expression localisation** rather than function, never tested by anyone including its authors. **The paradox may be an artefact of a speculation inherited as a finding.** | 🎯 **A provenance measurement, not a biological one**: the hedge verbs; the `n`; the field-density count; and the absence of pH / anion gap (§1.3). 🔴 **This is the only hypothesis already largely ADJUDICATED by §1, and it is ranked first for a reason — if R7 is right, R1–R6 are competing to explain something that was never established.** |

### 2.1 · What I DROPPED from the brief's candidate list, and why

| Dropped | Why |
|---|---|
| *"The historical attribution of death was incorrect or incomplete"* as a **separate** class | It is not a mechanism, it is **R7**, and stating it twice would let a provenance finding masquerade as a biological one. Merged. |
| *"Developmental rescue indirectly prevents systemic deterioration"* as distinct from *"CNS control normalizes"* | Kept, as **R5** — but **only because it has a different discriminator** (the untreated time course) than R1 (the covariate-adjusted panel). Without that column it would have been a paraphrase of R1 and I would have dropped it. |

---

## 3 · `preregister_prediction` — EX-ANTE, PERSISTED BEFORE THE TARGETED SEARCH

**Each prediction names what would REFUTE it. Predictions I expect to confirm are marked as such in
advance, so that a confirmation cannot later be re-sold as a discovery.**

| # | Prediction, stated before searching | Expected | What would refute it |
|---|---|---|---|
| **C-P1** | **No vector-genome (DNA) measurement in ANY peripheral organ exists in either gene-therapy paper.** Every peripheral WWOX measurement is a **protein** blot; every vector-genome measurement is **brain**. | `CONFIRMED` | Any qPCR/ddPCR vg count in liver, spleen, bone, marrow, kidney, gonad or nerve. |
| **C-P2** | **The CNS-restriction premise rests on ≤6 organs, by protein blot only, and at least one non-CNS tissue tested later came back POSITIVE.** | `CONFIRMED` — 🔴 and I record in advance that the sciatic-nerve positive is **`INHERITED`**, already in `full_text_queue_current.md`, so I may claim only the *consequence*, never the fact. | A systematic biodistribution panel in either paper. |
| **C-P3** | **No time course of any peripheral analyte exists in any untreated WWOX animal.** Every chemistry value is a **single** timepoint (~P18 mouse, 28 d rat). | `CONFIRMED` | Two or more ages for any one analyte in one model. |
| **C-P4** | **No peripheral analyte has ever been reported with body weight as a covariate, and no pair-fed, weight-matched or growth-restricted control exists in any WWOX study.** | `CONFIRMED` | Any covariate-adjusted analysis or any nutritional control arm. |
| **C-P5** | **Spleen, thymus and bone marrow were not harvested in either gene-therapy paper.** | `CONFIRMED`, less confidently — the 2021 harvest is liver/pancreas/kidney/testis/ovary and the 2026 is liver/sciatic/spinal/4 brain regions, but I have not read either Methods in full. | Any spleen, thymus or marrow in either tissue list. |
| **C-P6** | **The 2009 causal attribution is hedged and has never been tested**; `WWOX AND ("metabolic acidosis" OR "renal tubular acidosis")` returns exactly one record, that paper. | 🔴 **`CONFIRMED` — and it is a `REDISCOVERY`**, already in the manifest's field-density note. **Declared in advance as inherited so that §4 cannot present it as a find.** | A second record, or an unhedged verb. |
| **C-P7** | ⚠️ **A prediction that cuts AGAINST my own most-valued hypothesis.** Body weight **is** rescued in the HD arm (`TX-007` Fig 3C–3D). If so, **R3 and R1 predict the SAME panel result**, and R3 is *not* separable by the panel alone — only by the covariate and the weight-matched arm. | `CONFIRMED`, and it **weakens R3's standalone testability** | Body weight not rescued, which would make R3 separable by the panel alone. |
| **C-P8** | **No treated animal in any WWOX study has had bicarbonate, calcium, phosphate, haematology, electrolytes, spleen or thymus measured** — the prior audit's 0-of-48. I expect to **reproduce** it, not to discover it. | `CONFIRMED` — `INHERITED` | Any filled cell. |

---
## 4 · RESULTS — the targeted search, run AFTER §§2–3 were on disk

### 4.1 · `PREDICTION OUTCOME`, prediction by prediction

| # | Outcome | Evidence, and the scope of the sweep |
|---|---|---|
| **C-P1** | 🟢 **CONFIRMED** | *"we quantified viral DNA (vDNA) levels **in brain tissue** at P30 using qPCR"* — four **brain** regions (`tx007_per_arm_delivery_reconstruction_20260922.md` §, Fig 5A–D). **No vector-genome measurement in any peripheral organ was identified** in the analyses, dossiers, partial-locator files, deepdive manifests, commit candidates or the four current files, in either language, unscoped, using `vector genome\|viral DNA\|AAV DNA\|genome cop\|vg/dg\|vgcn\|qPCR` intersected with `liver\|spleen\|milza\|bone\|marrow\|midollo\|kidney\|rene\|heart\|muscle\|periph\|gonad\|testis\|nerve`. Positive control: the same query returns the **brain** qPCR in four files. |
| **C-P2** | 🟢 **CONFIRMED** — and 🔴 **the fact is `INHERITED`, as declared in advance** | Restriction attested by **protein blot in five organs** (2021: *"liver, pancreas, kidney, testis, and ovary"*, Appendix Fig S2B–C) **plus liver** (2026). The first non-CNS tissue added afterwards came back **POSITIVE**: *"WWOX protein was also detected in the **sciatic nerve** of HD-treated mice"*. `INHERITED` from `full_text_queue_current.md` and `PMID42422765_partial_locators.md`. **Only the consequence in §4.4 is mine.** |
| **C-P3** | 🔴 **REFUTED FOR GLUCOSE, CONFIRMED FOR EVERY OTHER ANALYTE** — recorded against myself | Glucose **does** have a time course: *"Blood glucose was measured at **P10, P20, and P30**"*, plus an attested P180 point. 🎯 **And the refutation is the most productive result in this file** — see §4.3. For bicarbonate, calcium, BUN, electrolytes, haematology, spleen and thymus the prediction stands: every value is a **single** timepoint (mouse P18; rat 28 d). |
| **C-P4** | 🟢 **CONFIRMED** | `pair-fed\|pairfed\|pair fed` → **1 file**, and it is a **hepatocyte-specific `Wwox^hep−/−` HFD** session evaluation about dark-phase food intake — a different object, not a null, not a covariate analysis. `weight-matched\|appaiat` → 5 files, none a WWOX physiology arm. **No covariate-adjusted peripheral analysis and no nutritional control arm was identified in any WWOX study**, unscoped, bilingual. |
| **C-P5** | 🟢 **CONFIRMED** | `spleen\|milza\|thymus\|timo\b\|marrow\|midollo` over both gene-therapy papers' dossiers, partial-locator files **and** deepdive manifests → **zero occurrences**. Positive control: the same pattern returns the EIIA-Cre spleen and thymus findings elsewhere in the corpus. **Neither gene-therapy paper harvested spleen, thymus or bone marrow.** |
| **C-P6** | 🟢 **CONFIRMED, and it is a `REDISCOVERY` — declared as such in advance** | *"we hypothesize"*, *"we speculate"*; `WWOX AND ("metabolic acidosis" OR "renal tubular acidosis")` → **1 record, that paper**; `WWOX AND hematopoiesis` → 3; `WWOX AND "bone mineralization"` → 1; `WWOX AND osteosarcoma` → **28**. All `INHERITED` from the 2026-08-06 field-density block of `PMID19936220.json`. **No credit claimed.** |
| **C-P7** | 🟢 **CONFIRMED, and it cuts against R3 exactly as I said it would** | Weight at P14 is `***` WT-vs-KO and `ns` across treatment days P1–P5 vs WT. ⇒ **R1 and R3 predict the same panel result.** R3 is **not** separable by the panel alone — only by the body-weight covariate and the weight-matched arm. **My preferred hypothesis lost its standalone testability to my own pre-registered prediction, and §5 is built on that loss rather than around it.** |
| **C-P8** | 🟢 **CONFIRMED — `INHERITED`, reproduced not discovered** | The prior audit's **0 of 48**. Reproduced here bilingually and unscoped. **No credit claimed.** |

**Score: 6 confirmed as expected · 1 refuted against me (C-P3) · 1 confirmed in a way that damages my own favoured hypothesis (C-P7) · 3 of the 6 confirmations declared `INHERITED` in advance.**

---

### 4.2 · 🎯 HEADLINE 1 — **THE CONVERSE EXPERIMENT HAS ALREADY BEEN RUN, AND IT DISSOLVES THE PARADOX'S PREMISE**

🔴 **An axis my pre-registration did not contain.** I recorded R1–R7 and predicted C-P1…C-P8, and **none
of them named the loss-of-function direction.** I found this while costing the Purkinje ladder's
"needs new animals" rung, which names a cell-type-specific Cre cross. **I am recording that the winning
result came from outside my own divergence**, exactly as the prior audit recorded its `D6` miss — and
for the same reason: the branch that wins is the one you did not favour.

**The paradox is stated as an asymmetry:** WWOX is put back **only in neurons**, yet a death attributed
to the **periphery** is prevented. That framing silently assumes the peripheral phenotype is
**organ-autonomous** — that liver, kidney, bone, marrow and spleen are deranged *because they lack
WWOX*. **The converse experiment tests that assumption directly, and it has been published.**

> **`FIRST-HAND` against the repository, `PMID 34831305` (the programme's own review),
> `research/deepdive_manifests/PMID34831305.json`, verbatim:**
> *"It is important to emphasize that **N-KO and S-KO recapitulated both neurological phenotypes (such
> as ataxia and seizures), but also systemic phenotypes such as growth retardation, metabolic
> abnormalities, and premature death**…"*
>
> **Corroborated in the 2026 primary, `PMID42422765_partial_locators.md`, verbatim:**
> *"deletion of Wwox in neural stem/progenitor cells (Nestin-Cre) or **postmitotic neurons (Synapsin
> I-Cre) recapitulated the severe neurological and metabolic phenotypes of global KO mice**, whereas
> astrocyte- (GFAP-Cre) or oligodendrocyte-[directed deletion did not]"*

⇒ **Deleting WWOX in postmitotic neurons ALONE — leaving the gene intact in liver, kidney, bone, spleen,
marrow, gut and gonad — reproduces growth retardation, metabolic abnormalities and premature death.**

> 🎯 **THE SYSTEMIC PHENOTYPE IS NEURONALLY DRIVEN. The loss-of-function and gain-of-function directions
> AGREE. A neuron-restricted vector rescuing a neuron-driven systemic phenotype is not a paradox — it is
> the expected result, and the field has held both halves for five years without putting them together
> in this repository.**

🆕 **And a symmetry that sharpens it further, which I believe is new here:** the knockout driver is
**Synapsin-I-Cre** and the therapeutic promoter is **hSynI**. 🔴 **The deletion and the replacement are
addressed to the same promoter's cell population.** `S-KO` therefore does not merely show that *some*
neuronal population is sufficient to cause the systemic phenotype — it shows that **the very population
the vector addresses is sufficient to cause it**, which is the tightest correspondence available between
a loss-of-function model and a gene-therapy target in this disease.

#### 🔴 Every bound, stated with the finding and not after it

| Bound | Consequence |
|---|---|
| ⚠️ **"Metabolic abnormalities" is a REVIEW'S SUMMARY PHRASE, not an analyte list.** | What is established for `S-KO` is **growth retardation**, an unspecified **metabolic** abnormality (almost certainly glucose, by context) and **premature death**. 🔴 **Bicarbonate, calcium, phosphate, haematology, spleen, thymus and bone were NOT stated for `S-KO` and I assert nothing about them.** |
| 🔴 **`S-KO` is a DIFFERENT OBJECT from EIIA-Cre.** | The chemistry panel (total CO₂, Ca, BUN, spleen, thymus, BV/TV) was measured in **`Wwox^ΔCre/ΔCre` EIIA-Cre**. **Nobody has run that panel in `S-KO`.** I cannot and do not say *"`S-KO` is acidotic"*. |
| ⚠️ `N-KO` is **Nestin-Cre**, deleting in NSCs *"and its progenies"* — a **whole-CNS** knockout, not neuron-restricted. | **Only `S-KO` carries the neuron-restricted inference.** `N-KO` is reported alongside it and does not add to it. |
| ⚠️ The review hedges: *"at the reported time frame"*. | The recapitulation is asserted over the observed window, not indefinitely. |
| 🔴 **This is a review locator plus a primary's introduction sentence, not a first-hand read of the `S-KO` paper.** | Grade: **`DATO` that both sources state it**, `PREMISE: METHODS_INVISIBLE` on the measurements behind *"metabolic abnormalities"*. **Finding two concordant statements is not opening a panel** — the lesson this repository learned on the cortical-bone assertion, applied to myself. |

#### What it does and does not settle

🟢 **Settles:** R1 (central control) is **strongly favoured** over any organ-autonomous reading, **for
growth and for the metabolic limb**. The prior audit's *"🔴 Nothing in this repository favours either"*
(§4.4) is 🔴 **superseded** — the repository did hold something, in a `.json` manifest, unconnected.
🔴 **Does not settle:** acidosis, calcium, haematology, spleen, thymus or bone, for which `S-KO` reports
nothing. **R2 remains fully live for exactly those six families**, which is why §5's panel survives this
finding intact rather than being obviated by it.

---

### 4.3 · 🎯 HEADLINE 2 — **GLUCOSE NORMALISES IN AN ARM THAT DIES COMPLETELY**

`verify_the_omitted_clause`, applied to the sentence the whole glucose story rests on.

The clause everyone quotes is *"By P20 … HD … fully normalized … whereas LD-treated mice showed an
intermediate improvement."* **The sentence beside it:**

> **`FIRST-HAND` against the repository, `PMID 42422765` Results, via
> `tx007_per_arm_delivery_reconstruction_20260922.md` (`STATED, both arms`), verbatim:**
> *"Beginning at postnatal day 10 (P10), both LD and HD treatments partially corrected hypoglycemia.
> By P20 … HD … fully normalized … whereas LD-treated mice showed an intermediate improvement.
> **From P30 onward, glucose levels were normalized across all groups**"*

**Set beside the same paper's survival record:**
*"**LD-treated mice did not survive to P90**"* · Fig 3B: the LD curve *"declines from ~20 d, **reaches
0% by ~80 d**"*, `n=20`.

> 🎯 **THE LOW-DOSE ARM HAS NORMAL BLOOD GLUCOSE FROM P30 ONWARD AND IS ENTIRELY DEAD BY ~P80.**
>
> 🔴 **Normalisation of the only peripheral analyte anyone has measured in a treated animal is
> DEMONSTRABLY NOT SUFFICIENT FOR SURVIVAL.** Glucose is not a survival surrogate beyond P20, and an
> efficacy programme scoring glucose at P30 would have scored the arm that dies as a success.

#### Why this matters more than it looks, and 🔴 where it corrects a sibling

`discovery_survival_expression_mismatch_20260922.md` builds its central inference on the P20 glucose
divergence — *"the LD survival collapse FOLLOWS the glucose divergence in time"*, graded `SUPPORTED for
the bulk of mortality`. 🔴 **That file worked from P10 and P20 only; the P30 clause sits in a different
file's table and has never been used anywhere** (`P30 onward\|normalized across all` → **exactly one
occurrence in the entire repository**, unscoped, and it is that table cell). **The divergence the
inference rests on is reported as GONE by P30, while the LD animals go on dying until ~P80.**

⚪ **This is not a criticism of that file** — it did not hold the clause. It is `verify_the_omitted_clause`
doing the job it exists for, across two files neither of which was wrong on its own surface.

#### 🔴 Bounds, because this is the strongest claim in the file

1. **Survivor conditioning.** P30 glucose is measured in LD animals **that reached P30**. The correct
   statement is: *"LD survivors at P30 are normoglycaemic and subsequently die"* — still a dissociation,
   but one **within the survivors**. Those that died before P30 were not sampled.
2. **`STATED`, not `A-fig`.** The P30 normalisation is **running text**. The repository holds attested
   panel statistics at **P20** (`*`/`**`/`ns`) and **no attested P30 test for LD**. Running text in this
   programme has already been shown to over-state a panel twice (*"dose-dependent"* over 7-of-8 `ns`;
   *"we observed"* over `p=0.07`). **Treat the P30 normalisation as the authors' summary, and the
   `REVIVAL_TRIGGER` is the Fig 3E–3H panel values.**
3. **`ns` is not equivalence.** No non-inferiority margin exists anywhere in this paper.
4. ⇒ **Minimum defensible form:** *by P30, blood glucose no longer distinguishes the arm that lives
   from the arm that dies, while survival distinguishes them absolutely.* **That minimum is enough to
   retire glucose as an efficacy endpoint after P20, which is what §5 does with it.**

#### 🆕 And the same quotation adjudicates R5 against R1, for free

*"Beginning at P10, both LD and HD treatments **partially** corrected hypoglycemia."* Treatment is at
**P0–P5**; at **P10** treated animals are still **between** KO and WT. ⇒ **The derangement is not
prevented — it develops and is then progressively corrected.**
🔴 **R5 (developmental prevention) is REFUTED for glucose. R1 (correction of an established lesion) is
supported.** R5 survives untested for every other analyte, and its discriminator — the untreated time
course — remains unrun.

---

### 4.4 · 🎯 HEADLINE 3 — **THE UREA RISES 2.4–2.7× MORE THAN THE CREATININE, AND NOBODY DIVIDED**

The **only model-invariant chemistry analyte** is elevated BUN (`INHERITED`, prior audit §3.3). The
authors of the 2009 mouse paper read uraemia as **kidney failure**. 🔴 **The rat is the only WWOX model
in which BUN and creatinine were both measured — and the repository holds both numbers and has never
put them over each other.**

`INHERITED` values, rat `lde/lde` at 28 d (`PMID 17803050`, `CLAIM 038`, page-adjudicated):
**BUN ×3.2 ♀ / ×3.5 ♂** · **creatinine 0.48→0.64 ♀ (×1.33) / 0.45→0.58 ♂ (×1.29)**, both `P<0.01`.

| | urea fold | creatinine fold | **ratio of folds** |
|---|---:|---:|---:|
| ♀ | 3.2 | 1.33 | 🔴 **2.40** |
| ♂ | 3.5 | 1.29 | 🔴 **2.72** |

> 🔴 **THE UNIT DEFECT DOES NOT TOUCH THIS.** `CC-20260922-CLAIM038-UNIT-CLASS-01` forbids **numeric
> cross-model** comparison because the rat's values are printed `mg/ml` and are certainly `mg/dL`.
> **A fold-change is dimensionless, and a ratio of two fold-changes within one model and one table is
> invariant under any consistent unit error.** This is the one arithmetic the §3.2 constraint permits,
> and it is the one nobody performed.

**What a disproportionate urea rise with a near-normal creatinine means** — and the interpretation is
constrained, not free, because the same paper supplies the controls:

- 🟢 *"kidneys **histologically normal**, no proteinuria"* (`CLAIM 038`, `INHERITED`).
- 🟢 The animal is at **~56% of normal weight at 21 d**, with growth arrest.

⇒ **A ~2.5-fold disproportion between urea and creatinine, in an animal with histologically normal
kidneys and no proteinuria, is the signature of urea PRODUCTION and/or reduced perfusion — protein
catabolism, reduced intake, dehydration — rather than of failing glomerular clearance.** Creatinine,
which tracks clearance and muscle mass, barely moves; urea, which tracks nitrogen turnover and
perfusion, triples.

| Grade | |
|---|---|
| 🟢 **`DATO`** | the four numbers and the two controls |
| 🟢 **`DATO`** | the ratio — it is division |
| 🟡 **`INFERENZA`** | that the pattern indicates catabolic/pre-renal rather than intrinsic renal azotaemia. `PREMISE: DEFAULT_FROM_TEXTBOOK` — **the BUN:creatinine disproportion is a clinical-chemistry convention, and a convention is a reason to look, never a substitute for looking.** 🔴 **In a growing pup, creatinine is additionally depressed by low muscle mass, which INFLATES the ratio independently of perfusion — this is a confound, not a footnote, and it is why §5 ranks creatine kinase and muscle mass beside it rather than after it.** |
| 🔴 **`SPECIES-BOUND`** | This is the **rat `lde/lde`**, a C-terminal frameshift, **not** a null and **not** a mouse. `MECHANISM_TRANSFER_FIREWALL` applies. **Creatinine has never been measured in ANY mouse WWOX model**, so the mouse ratio is not computable and I do not compute it. |

⇒ **Consequence.** The field's own death hypothesis has two limbs — renal tubular acidosis and impaired
haematopoiesis. The renal limb is supported by **expression localisation** (kidney IHC, `n=1`/genotype),
and the only model where its **functional** discriminator exists points **away** from it. Combined with
§1.3 (no pH, no anion gap ever measured) this is the second independent line favouring **R3/R7** on the
renal-acidotic limb — and it costs one division of numbers the repository already held.

---

### 4.5 · What the four hypotheses now stand at

| | Status after §4 | On what |
|---|---|---|
| **R1 · central control** | 🟢 **STRONGLY FAVOURED for growth + the metabolic limb** | `S-KO` recapitulation (§4.2); glucose corrected by a CNS-only vector in two papers (`INHERITED`) |
| **R2 · survival without normalisation** | 🟡 **FULLY LIVE for the six unmeasured families**, and 🎯 **partially supported in an unexpected direction** | §4.3 shows the converse of R2: **normalisation without survival**. Nobody has shown survival *with* a persisting derangement, because nobody has measured one |
| **R3 · nutritional/catabolic secondary** | 🟡 **SUPPORTED but NOT SEPARABLE by the panel alone** | §4.4's urea:creatinine disproportion; growth arrest from day 10; 🔴 C-P7 — weight is rescued, so R1 and R3 predict the same panel |
| **R4 · off-CNS transgene/vector** | 🟡 **UNDER-BOUNDED, not excluded** | §4.6 |
| **R5 · developmental prevention** | 🔴 **REFUTED for glucose**; untested elsewhere | §4.3's *"partially corrected"* at P10 |
| **R6 · survivor selection** | 🟡 **LIVE, and it cuts both ways** | §1.5 (baseline) and §4.3 bound 1 (treated) |
| **R7 · the attribution was never a measurement** | 🟢 **LARGELY ADJUDICATED** | hedge verbs; `n=4`; field density 1; §1.3's missing pH and anion gap; §4.4's disproportion |

### 4.6 · The bound on off-CNS expression, stated in form **B**

> **No measurement bounding off-target vector expression was identified for any organ other than liver,
> pancreas, kidney, testis, ovary and sciatic nerve, within the analyses, dossiers, partial-locator
> files, deepdive manifests, page adjudications, commit candidates, the four current files, the queues
> and the ledgers of this repository, in English or Italian, unscoped by file type, using the queries
> `biodistribut`, `off-target`, `tropism|tropismo`, `vector genome|viral DNA|AAV DNA|genome cop|vg/dg|vgcn`
> and `hSyn|synapsin|sinapsin` intersected with peripheral-organ vocabulary in both languages.**
> Positive control: the same queries return the four-region **brain** vDNA panel, the five-organ 2021
> blot and the sciatic-nerve positive.

**Three consequences the repository does not carry:**

1. 🔴 **Every peripheral WWOX measurement ever made in a treated animal is a PROTEIN BLOT. Transduction
   was never measured outside the brain at all.** A promoter-restricted construct can deposit vector
   genomes in a tissue and express nothing there — so *"no WWOX protein in liver"* bounds **expression**
   and says **nothing** about **vector arrival**. The two have been used interchangeably.
2. 🔴 **Not one of the organs carrying the UNRESCUED peripheral phenotypes was ever assayed.** The
   tested set is liver, pancreas, kidney, testis, ovary, sciatic nerve. The phenotype set is **bone,
   spleen, thymus, bone marrow**. 🔴 **The intersection is empty.**
3. 🔴 **The one non-CNS tissue added after the original five came back POSITIVE.** A generalisation from
   five negatives was contradicted at the first organ appended to the list. *"The restoration is
   brain-only, so peripheral tissues remain null"* — carried in `PMID34747138_locators.md` and its
   manifest — is an **extrapolation**, and the repository should carry it as one.

⚠️ **And the restriction premise rests on an unopened panel.** The five-organ negative is
**Appendix Fig S2B–C**, which the prior audit lists as `T0-b` — *"the unopened basis of the strongest
finding in that reading"*. 🔴 **The premise that makes the paradox a paradox has itself never been
inspected at panel level**, which is precisely the configuration that produced the cortical-bone
provenance failure. `PREMISE: METHODS_INVISIBLE` — a western on whole-organ lysate has an unstated
detection floor and cannot exclude a minority transduced population in any case.

---

## 5 · THE PERIPHERAL PANEL — ranked, costed, and with the rejections stated

**Scoring rule, fixed before scoring:** `VALUE = OUTCOME WIDTH × HYPOTHESIS DISCRIMINATION`.
🔴 **A wide but non-discriminating outcome is LOW value. A narrow but hypothesis-separating one can be
HIGH.** Applied literally below, and it demotes the two endpoints a novelty-driven ranking would promote.

### 5.0 · Two design decisions that precede every endpoint

| | Decision | Why it is not negotiable |
|---|---|---|
| **T** | 🔴 **TIMING: P16 ± 1.** | §1.6 — beyond ~P21 **no untreated-KO comparator can exist**, and the authors say so: *"Behavioral testing could not be performed in untreated-null mice due to severe morbidity and early lethality."* **A panel at P30 forfeits its own control arm.** Every endpoint below is specified at P16 for this reason alone. |
| **W** | 🔴 **BODY WEIGHT IS RECORDED FOR EVERY ANIMAL AND CARRIED AS A COVARIATE, and every organ endpoint is reported as ABSOLUTE MASS *and* RATIO.** | §1.4 — the ratio's denominator is the phenotype being rescued (`brain sparing in cachexia`), and §4.1 C-P7 — the weight covariate is the **only** thing separating R1 from R3. **It costs one column and it is the difference between a descriptive panel and a discriminating one.** |

### 5.1 · The panel — ONE animal, TWO tubes, ONE balance, at P16

| Rank | Endpoint | (1) historical abnormality | (2) authors linked to mortality | (3) from banked material? | (4) 🎯 what it DISCRIMINATES | (5) marginal cost | Width × Discrimination |
|---:|---|---|---|---|---|---|---|
| **1** | 🥇 **Venous blood gas or total CO₂ + Na⁺ K⁺ Cl⁻ + lactate → the ANION GAP** | 🟢 total CO₂ `14.50` vs `21.67`, `p=0.006` (mouse, `n=4`) | 🟢 **the primary limb of the field's own death hypothesis** | 🔴 **NO — never reconstructible** | 🎯 **The gap separates R1/renal-tubular (NORMAL gap) from R3/catabolic-ketotic-lactic (RAISED gap) — the two readings of the same low bicarbonate.** 🔴 **And it separates them for the price of three electrolytes that a panel runs anyway** | **one fresh tube** | 🟢 **HIGH × HIGH** |
| **2** | 🥈 **BUN + creatinine + creatine kinase** (+ the weight covariate as muscle proxy) | 🟢 **the only MODEL-INVARIANT analyte** | 🟢 *"blood chemistry values compatible with kidney failure"* | 🟢 **YES — stable on banked serum** | 🎯 **The urea:creatinine ratio + CK is the exact discriminator `CLAIM 038` names and leaves open** (renal insufficiency vs seizure-driven hypercatabolism), and §4.4 shows the rat already leans one way. **Creatinine has NEVER been measured in any mouse WWOX model** | **same tube** | 🟢 **HIGH × HIGH** |
| **3** | 🥉 **Body weight + ABSOLUTE spleen mass + ABSOLUTE thymus mass + lymphocyte count** | 🟢 spleen `0.21%` vs `0.53%`, `p=0.0015`; thinned thymic cortex | 🟢 *"impaired hematopoiesis can also be a contributing factor to metabolic acidosis and death"* | 🟡 **fixed tissue if it exists; otherwise a balance at necropsy** | 🎯 **Thymic cortical involution + lymphopenia + splenic hypocellularity is the STEREOTYPED undernutrition/stress signature.** Present **with** weight normalised ⇒ R1/R2; present **in proportion to** weight ⇒ R3. 🔴 **Only the absolute-plus-ratio pair can tell those apart (§1.4)** | 🟢 **~60 seconds and a balance — the cheapest endpoint in the file** | 🟢 **MODERATE × HIGH** |
| **4** | **Ca²⁺ + inorganic phosphate + ALP** | 🟡 Ca `−8.5%`, `p=0.000385` (mouse); **ns in rat** — model-specific; PO₄ never measured in mouse | 🟡 named in the systemic list, not in the causal sentence | 🟢 **YES — banked serum** | 🟡 **Ca/PO₄/ALP jointly separate a WWOX-intrinsic mineralisation defect from nutritional/secondary bone disease** — and PO₄ is the missing cell that makes the triad readable at all | **same tube** | 🟡 **NARROW × MODERATE** |
| **5** | **CBC with differential and platelets** | 🟡 WBC `4.2` vs `9.45` at **`n=2`, no test run**; 🔴 **platelets NEVER counted in any WWOX animal, ever** | 🟢 the haematopoietic limb of the death hypothesis | 🔴 **NO — fresh EDTA whole blood only** | 🔴 **DELIBERATELY DEMOTED.** The outcome is maximally **WIDE** (platelets are a total unknown) but **WEAKLY DISCRIMINATING**: cytopenias follow undernutrition, marrow failure and chronic illness alike, so **no CBC result separates R1 from R3**. 🟡 Its discriminating component is the **differential** (lymphopenia), already bought in rank 3 | **same fresh draw as rank 1** | 🔴 **WIDE × LOW ⇒ LOW** |
| **6** | **μCT of archived limbs, treated vs WT** | 🟢 BV/TV `13.35→5.8%` (`KO n=3` vs **pooled** `n=5`) | 🟡 bone is in the systemic list, not the causal sentence | 🟡 **retrospective and non-destructive on fixed bone — IF limbs were kept** | 🟢 **The one system the programme CLAIMS is rescued** (*"cortical bones were of comparable size and thickness to WT"*, **Appendix Fig S4B, unquantified, untested, panel never opened**). μCT converts an unquantified visual comparison into BV/TV. 🔴 **Cannot** give Md.V/TV — that needs in-vivo labelling | 🟢 **existing material, decoupled from the cohort** | 🟢 **MODERATE × HIGH** |

> 🔴 **Ranks 1–5 are ONE terminal collection from ONE animal: a lithium-heparin/serum tube, an EDTA
> tube, and a balance. Rank 6 is independent and needs no animal.** If attached to any cohort already
> being terminated at P16, **the marginal animal cost of the entire panel is ZERO** — which is the only
> route to the `NOT RECONSTRUCTIBLE` cells (C2, C5) that exists at any price (`T2-d`, `INHERITED`).

### 5.2 · 🔴 REJECTED endpoints, and why — the half of the deliverable a panel usually omits

| Rejected | Why |
|---|---|
| 🔴 **BLOOD GLUCOSE** | **The sharpest rejection in the file, and it is `FIRST-HAND` from §4.3.** It is normalised in the arm that dies. Beyond P20 it has **zero remaining discriminating power for survival**, it is already `DATO` for rescue, and including it would spend a tube confirming a settled question. 🟢 **Retained for ONE purpose only: as the panel's internal positive control** — an assay that fails to reproduce the established hypoglycaemia in the untreated arm has failed, and the panel must be able to detect its own failure. |
| 🔴 **The full 10–14 analyte clinical-chemistry panel "because the analyser returns one"** | `PREMISE: DEFAULT_FROM_TEXTBOOK`, flagged as such by the prior audit's `T0-a` and rejected here on the scoring rule: **width without discrimination**. Every analyte above is included because it separates two named hypotheses, not because it comes free with the cartridge. |
| 🔴 **Liver enzymes (ALT/AST)** | Measured only in **`Wwox^hep−/−` under HFD** (a hepatocyte-specific cKO, **not a null**, a different object) and in the rat with **sample-size footnotes rather than significance footnotes** — `CLAIM 038`: *"non importabile in nessuna direzione"*. Adds width, separates no two hypotheses in §2. |
| 🔴 **Testosterone / steroidogenic function** | Genuinely never assayed in any WWOX animal, and **Leydig presence is not Leydig function** — a real gap. But it separates **no two** of R1–R7, and §1.7's breeding data already bound reproductive function at the whole-organism level far more cheaply. **Rejected on discrimination, not on interest.** |
| 🔴 **Body composition (EchoMRI/DEXA)** | Needs a live animal, and **body weight already carries the covariate signal at zero cost**. The increment over a balance does not separate anything. |
| 🔴 **Platelet count as a standalone novelty endpoint** | Retained only inside rank 5. Its novelty (zero prior measurements anywhere) is **width**, and width alone scores LOW under the stated rule. **Recorded explicitly because the temptation to promote it is exactly what the revised rule exists to resist.** |
| 🔴 **Any adult (P30+) timepoint for the discriminating panel** | §1.6 — it forfeits the untreated-KO arm. Adult measurements answer *"is the treated animal normal?"*, which is a different and weaker question. |

### 5.3 · The two arms that would settle R3, and neither is in the panel

R3 is **not separable by the panel alone** (C-P7, adjudicated against me). It needs one of:

| | Arm | Cost | What it delivers |
|---|---|---|---|
| **A** | 🥇 **The body-weight covariate** — already bought, rank W | 🟢 **zero** | Under R3 the analytes track **weight** across animals irrespective of arm; under R1 they track **arm** after adjustment. **One column of analysis, no extra animal, no extra assay.** |
| **B** | **A growth-restricted / weight-matched WT arm** | 🔴 **new animals** | Decisive: under R3 a WT pup held on the KO growth curve reproduces the panel; under R1 it reproduces none of it. 🔴 **Not recommended here** — it adds animals for a hypothesis that arm **A** already tests at zero cost, and `A` should be run first and reported before anyone considers `B`. |

### 5.4 · 🔴 The cheapest decisive experiment in this entire file needs NO treated animal at all

> **The untreated-`Wwox`-null TIME COURSE: the rank 1–5 panel at P3, P7, P10, P14 and P18 in untreated
> animals only.**

**Cost:** untreated nulls are generated as a by-product of every breeding scheme in this programme and
**die anyway**; the panel is one terminal collection per pup. **No treated cohort, no vector, no
therapeutic arm.**

**What it delivers, and nothing else in this file delivers any of it:**
1. 🎯 **The ONLY route to R5.** Analytes normal at P7 and deranged at P18 are **late and preventable**;
   deranged at P3 they precede any treatment. **Currently a single P18 point exists (§4.1 C-P3).**
2. 🎯 **It converts the baseline from a POINT into a DISTRIBUTION**, which §1.5 shows is a precondition
   for scoring *any* rescue: `±3.5` against `±0.333` at `n=4` is equally a shifted mean and a **mixture
   of two populations**, and no rescue experiment can be scored against a mixture.
3. 🎯 **It orders the derangements in time**, which is the only observational route to which limb is
   upstream — and it does so **without** the survivor conditioning that contaminates every P18-only
   measurement (§1.5), because sampling at P3 and P7 precedes most of the mortality.

🔴 **This should be run BEFORE the treated panel, not after it.** A rescue experiment against an
unbounded, single-point, survivor-conditioned baseline is not scorable, and the baseline is the cheaper
half.

---

## 6 · THE PURKINJE THREAD — costed honestly, and the honest answer is mostly "nothing further"

**Priority order applied as given: `RAW DATA REANALYSIS` > `NEW STAIN ON EXISTING SECTION` >
`NEW ANIMAL COHORT`.**

### 6.1 · What remains answerable, tier by tier — and where the answer is "nothing"

| Tier | Remaining? | Verdict |
|---|---|---|
| **`RAW DATA REANALYSIS`** on existing images | 🔴 **NOTHING NEW REMAINS.** | The prior nodes have already specified every move: published-panel re-read at original resolution (rung 0, executable by a reader holding nothing); layer-resolved re-quantification of the whole-slide scans (holder-only); **native-EGFP re-imaging over cerebellum on the 2021 in-vivo reporter sections** (rung 1b, no antibody, baseline-free). 🔴 **The limiting factor is NOT analysis.** It is (i) **access** — *"Data and code availability: Not relevant"*, `BLOCKED — HOLDER-ONLY` — and (ii) **channel count** — two secondaries, four rabbit primaries. **Neither is relieved by any further analysis, so proposing more analysis would be proposing nothing.** |
| **`NEW STAIN ON EXISTING SECTION`** | 🟡 **One move, already specified** | One **mouse** anti-calbindin-D28k on an archived section, inheriting the existing anti-mouse secondary, on **two independent archives** (2021 frozen/FFPE sagittal P17/P19 and 9 months; 2026 frozen/FFPE P10–P180). `INHERITED` in full. **I add nothing to it and claim nothing of it.** |
| **`NEW ANIMAL COHORT`** | 🟡 **Two items, already argued down** | **Necessity** (`Pcp2`/`L7`-Cre × `Wwox^fl/fl`) and **a reporter readout at the therapeutic dose** (existing reporter material is `2E10`/hemisphere; TX-007 is 5–13× higher). `INHERITED`. |

> 🎯 **The deliverable this section owes: what remains is NOT a missing experiment. Every tier is
> specified and the top tier is exhausted. What remains is a PERMISSION and a CHANNEL, and no amount of
> further design converts either into an experiment.** Saying so is the honest output, and inventing a
> fourth move to avoid saying it would be the failure.

### 6.2 · 🆕 My one addition, and it comes from the peripheral axis rather than the cerebellar one

> 🎯 **The peripheral panel and the Purkinje question require a cohort at the SAME AGE, and take
> NON-COMPETING tissues from the SAME ANIMALS.**

| | |
|---|---|
| The peripheral panel is **forced** to P16 ± 1 | §1.6 / §5.0-T — beyond ~P21 the untreated-KO arm cannot exist |
| The 2021 cerebellar archive was cut at **P17/P19** | `INHERITED` — sagittal, 12–14 µm, `n=3` per vector |
| The 2026 archive spans **P10–P180** | `INHERITED` |
| 🔴 **The panel takes BLOOD and two small organs. The Purkinje question takes BRAIN.** | **There is no tissue conflict and no trade-off.** |

⇒ **If a cohort is ever terminated at P16–P19 for either question, it serves both at zero mutual
marginal cost**, and the correct unit of planning is **one termination protocol**, not two experiments.
🔴 **This does not make either question cheaper on its own** and it is not an argument for generating a
cohort — it is an argument about **what to specify if one is generated for any other reason**, including
a cohort generated for neither of these questions.

⚠️ **Honest limit of the addition.** The 2021 reporter material is `2E10`/hemisphere and TX-007 is
`1.23E11`/`2.63E11`; a cohort serving both questions inherits **whichever dose it is dosed at**, and
neither question transfers across that gap. **The co-location is an economy, not a bridge.**

---

## 7 · `COMMUNITY_FOLLOWUP` — 🔴 INTERNAL ARTEFACT ONLY

> 🔴 **No researcher, author, laboratory, foundation, institution or sponsor was contacted, and none
> will be. No email, message or correspondence was drafted, prepared, addressed or sent. Nothing below
> represents anybody or is addressed to anybody. These are rows in a file.**
>
> Every row is written in the only framing that is both true and useful: **their existing work creates a
> natural next experiment.** Rows are numbered `SC-1…SC-5`; where a row narrows an existing row it says
> so rather than duplicating it.

| Field | **SC-1** | **SC-2** | **SC-3** | **SC-4** | **SC-5** |
|---|---|---|---|---|---|
| **EXISTING ASSET** | The **Synapsin-I-Cre `S-KO`** line, already generated and published as recapitulating *"growth retardation, metabolic abnormalities, and premature death"* | The **breeding colony itself**: *"Heterozygote or KO rescued mice … were used for breeding"*, plus **20 breeding cages per group** of HD-treated nulls with fertility and litter sizes comparable to WT | **Untreated `Wwox`-null pups**, generated as an unavoidable by-product of every litter in the programme and dying by ~P21 | **Archived hindlimbs / fixed skeletal material** from treated cohorts, and **Appendix Fig S4B**, which already reports *"cortical bones were of comparable size and thickness to WT"* | The **running vector qPCR** already validated on four brain regions (Fig 5A–D), plus **`KO+RI` / `WT+RI` vehicle arms** that are a matrix-matched vector-free blank |
| **NEW QUESTION** | Does neuron-restricted deletion reproduce the **specific** analytes — bicarbonate, calcium, spleen, thymus, haematology, bone — or only growth, glucose and death? | Which peripheral functions must be intact for a treated null dam to gestate and lactate — i.e. **what does the colony already know about peripheral rescue that was never written down as a result?** | **When** does each peripheral derangement appear — is the panel present at P3, or does it emerge after P7? | Is the cortical-bone rescue **quantitative** — BV/TV and cortical thickness — rather than an unquantified visual comparison? | Do vector genomes reach **bone, spleen, marrow, kidney and liver** — i.e. is the neuronal restriction a restriction on **expression** or also on **arrival**? |
| **MINIMAL EXPERIMENT** | The §5.1 rank 1–5 panel on `S-KO` pups at P16, three arms | **A single supplementary column** — dam genotype and treatment status per animal — plus the fertility/litter records that already exist | The §5.1 panel at **P3 / P7 / P10 / P14 / P18** in untreated nulls only | **Retrospective μCT** on the fixed limbs; non-destructive | **The same qPCR, five more tissues**, on DNA from animals already dissected |
| **NO NEW ANIMALS?** | 🔴 **NO** — needs an `S-KO` cohort, but **no new line, no new construct, no new vector** | 🟢 **YES — zero.** It is a reporting act on records that exist | 🟡 **No new animals *generated*** — these pups are produced and die regardless; the act is a terminal collection instead of a disposal | 🟢 **YES — zero**, conditional on the limbs having been kept (**unknowable from a repository**, `CNE-C3`) | 🟢 **YES — zero**, conditional on peripheral tissue or DNA having been banked |
| **INFORMATION GAIN** | 🎯 **HIGHEST in the file.** It is the **converse** of the gene therapy and it closes §4.2's bound directly: it converts *"metabolic abnormalities"* from a review's summary phrase into an analyte list | 🔴 **Removes an unbounded confound** (`tx007` §9) **and simultaneously converts an unrecognised whole-organism bioassay (§1.7) into a citable result.** One column, two results | 🎯 **The only route to R5, and it converts the baseline from a point into a distribution (§5.4)** — a precondition for scoring any rescue at all | Converts the programme's **third** peripheral-rescue claim from an unquantified *"observed … comparable"* into a number, and closes `RT-G6` | Separates **transduction from expression** — the distinction §4.6 shows has been used interchangeably — and retro-fits the peripheral arm onto the axis the AAV field reports |
| **POTENTIAL THERAPEUTIC VALUE** | If `S-KO` reproduces the full panel, **the whole systemic syndrome is a CNS target** and every peripheral endpoint becomes a **CNS efficacy biomarker**. If it does not, the unrecapitulated analytes are **organ-autonomous and outside any neuron-directed strategy's reach** — which is equally decisive and equally useful | Establishes **durable multi-organ peripheral function under physiological challenge** in treated adults — the most demanding integrated endpoint the programme already possesses and has never reported as one | Defines the **therapeutic window on the peripheral axis**, and tells a programme whether a peripheral endpoint can be prevented or only corrected | Bone is the one **non-CNS** endpoint plausibly readable **non-invasively and longitudinally**; a quantified baseline is what a long-term safety/efficacy follow-up would rest on | Bounds **off-target biodistribution**, which is a safety quantity for any neuron-directed programme and is currently unmeasured outside six organs |

🔴 **`SC-1` is ranked first deliberately**, and it is the only row that needs animals. It is ranked first
because **§4.2's bound is the single largest uncertainty this file leaves open**, and because the line,
the reagents and the panel all already exist — the experiment is a **measurement on an existing model**,
not a new model.

---

## 8 · WHAT IS GENUINELY NEW, WHAT IS INHERITED, AND WHAT I COULD NOT ESTABLISH

### 8.1 · 🆕 NEW in this file — strictly

| # | Finding | Grade |
|---|---|---|
| **N1** | 🎯 **The converse experiment resolves the paradox's premise.** `S-KO` (Synapsin-I-Cre, postmitotic neurons) recapitulates growth retardation, metabolic abnormalities and premature death ⇒ **the systemic phenotype is neuronally driven**, so a neuron-restricted rescue is expected rather than paradoxical. **Plus the promoter symmetry**: the deletion driver (`Synapsin-I-Cre`) and the therapeutic promoter (`hSynI`) address the same population. 🔴 **The two source sentences are `INHERITED`** (both sit in repository surfaces); **the connection to the rescue paradox, and the supersession of the prior audit's "nothing favours either", are new** | 🟢 **C — NOVEL CONNECTION**, bounded to growth/metabolic/death |
| **N2** | 🎯 **Glucose normalises in the arm that dies.** *"From P30 onward, glucose levels were normalized across all groups"* set beside *"LD-treated mice did not survive to P90"* and a 0%-by-~P80 curve ⇒ **normalisation of the only measured peripheral analyte is not sufficient for survival**; glucose is not a survival surrogate after P20. The clause exists in **exactly one** place in the repository and had never been used | 🟢 **D — CORRECTS A LIVE INFERENCE** (a sibling's central argument rests on the divergence this clause reports as gone) |
| **N3** | **The acidosis limb was never measured as acidosis.** **No pH, no pCO₂, no anion gap, no lactate in any WWOX animal, ever** (`anion gap` → **0 files** repo-wide). *"Hypocapnia"* names a respiratory quantity that was not assayed; a low total CO₂ without pH does not establish acidosis; **the anion gap is the free discriminator nobody computed** | 🟢 **E — EXPERIMENT-GENERATING**; it is what makes §5 rank 1 rank first |
| **N4** | **The urea rises 2.4–2.7× more than the creatinine** in the only WWOX model where both exist, with histologically normal kidneys and no proteinuria ⇒ a **catabolic/pre-renal** rather than intrinsic-renal signature. **Unit-invariant**, so licensed despite `CC-20260922-CLAIM038-UNIT-CLASS-01` | 🟢 **C — NOVEL CONNECTION** from a division nobody performed. 🔴 `INFERENZA`, species-bound, muscle-mass-confounded |
| **N5** | 🔴 **The structural comparator constraint.** The untreated null dies at ~3 weeks ⇒ **for every endpoint beyond ~P21 an untreated-KO comparator cannot exist** — the authors state the mechanism (*"could not be performed … due to severe morbidity and early lethality"*). ⇒ **P14–P18 is the only window in which the three-arm design is physically available**, and it does not overlap the P30+ window where every expression measurement sits | 🟢 **E — it determines the whole panel's timing** |
| **N6** | **The breeding scheme is an unrecognised whole-organism peripheral bioassay** — 20 breeding cages per group of treated nulls, fertility and litter sizes comparable to WT. Read as a **confound** by a sibling; never read as **evidence** | 🟡 **C**, heavily bounded (integrated not analyte; adult not lethal window; survivor-conditioned) |
| **N7** | **The organ-weight denominator trap, transferred.** `CLAIM 036`'s *"brain sparing in cachexia"* lesson applies unchanged to spleen and thymus ratios and has never been carried there ⇒ **absolute mass AND ratio AND body weight, or the number cannot be attributed** | 🟡 **B — METHOD TRANSFER** |
| **N8** | **The untreated baseline is survivor-conditioned.** Table 3's `n=4` KO were bled at P18 from a cohort ~77% dead by P17. The repository applies survivor conditioning to the **treated** arm five times and to the **baseline** never. 🔴 And `±3.5` vs `±0.333` at `n=4` is equally a shifted mean and a **two-population mixture** | 🟡 **B** |
| **N9** | **The intersection is empty.** Transgene expression was tested in liver, pancreas, kidney, testis, ovary, sciatic nerve; the unrescued phenotypes live in bone, spleen, thymus, marrow. **No organ appears in both sets.** And **transduction was never measured outside the brain at all** | 🟢 **C** |
| **N10** | **A new tool trap** (`grep -E` with `\|`) and a proposed **thirteenth failure mode**: a negative count from an alternation must carry a positive control **inside** the alternation | 🟢 **METHOD** |
| **N11** | 🔴 **A correction: `n=4`, not three.** The Orchestrator's *"sentence that should travel"* reads *"measured in one model, once, **in three animals**"*. The manifest anchor reads **`WT n = 3, HET n = 3, KO n = 4`**. The sentence is otherwise exactly right; **the number in it is not**, and it is the number most likely to be repeated | 🟡 **CORRECTION** |

### 8.2 · INHERITED — reproduced, relied upon, and claimed as nobody's discovery but their authors'

0-of-48 empty cells and the permanent/recoverable split (`peripheral_phenotype_denominator_audit`) ·
the survival-validity licence table and the maternal confound (`tx007_animal_flow_survival_validity`) ·
`D3`, the multi-system framing and the §7.4 question itself (`DISCOVERY_TRACE_metabolic_gating`) ·
`D4`, *"sicker pups suckle less"*, which is **R3's seed for glucose** and which I extended to the panel ·
the P20 arm-separating glucose statistics (`discovery_survival_expression_mismatch`) ·
the sciatic-nerve positive and *"neuron-specific but not CNS-confined"* (`full_text_queue_current`) ·
the entire Purkinje cost ladder, rungs 0/1/1b/2/3, the EGFP reporter route and the `C1`–`C8` rows
(`purkinje_cheapest_path_and_community_followup`, `purkinje_existing_material_experiment`) ·
`MAB377`/A60 excluding Purkinje cells · the two-secondary reagent gate · `BLOCKED — HOLDER-ONLY` ·
the `Appendix Fig S4B` cortical-bone locator (Orchestrator verification `V1`) ·
`PREMISE: NOBODY_LOOKED` for Purkinje · the `mg/ml` unit defect · `CLAIM 036`'s brain-sparing lesson.

### 8.3 · `COULD NOT ESTABLISH`

| ID | Statement | Why not |
|---|---|---|
| **CNE-C1** | 🔴 **Which analytes "metabolic abnormalities" covers in `S-KO`** | It is a review's summary phrase plus a primary's introduction clause. **The `S-KO` primary was not read in this act and `files/fulltext/` does not exist in this edition.** This is the largest open bound in the file and `SC-1` exists to close it |
| **CNE-C2** | Whether the P30 glucose normalisation survives panel-level inspection | `STATED` in running text; **no attested P30 panel statistic for LD** is held here. Running text in this programme has over-stated a panel at least twice |
| **CNE-C3** | Whether any banked serum, fixed limb or peripheral tissue from any WWOX treated cohort still exists | **Unknowable from a repository.** No external contact was made and none is authorised. Every "existing material" route in §5 and §7 is conditional on this and says so |
| **CNE-C4** | Whether the rat's urea:creatinine disproportion transfers to any mouse | **Creatinine has never been measured in any mouse WWOX model.** The ratio is not computable there, and `MECHANISM_TRANSFER_FIREWALL` forbids importing the rat's |
| **CNE-C5** | Whether the 2021 five-organ peripheral negative bounds anything below its detection floor | **Appendix Fig S2B–C has never been opened by anyone in this repository.** A western on whole-organ lysate has an unstated LOD and cannot exclude a minority population |
| **CNE-C6** | Whether any prior file in this repository contains the `grep -E '\|'` defect | **I did not audit for it and I assert nothing about it.** I re-ran only my own patterns. Recorded so that a later actor can decide whether the audit is worth running |
| **CNE-C7** | The fertility denominator | Running text says *"20 breeding cages per group"* and is called *"the most robustly powered assay in the paper"*; the **plotted panel** carries *"roughly three"* points per group (`PMID42422765.json`, S4C–D). 🔴 **Design `n` and panel `n` disagree and I did not resolve them.** §1.7 is written to survive either |

### 8.4 · Absence claims made in this file, all in form **B**

Each is stated in full at its point of use with its document classes, languages, file scope, queries and
**positive control**: §1.3 (**no pH / pCO₂ / anion gap / lactate in any WWOX animal**) · §4.1 C-P1
(**no peripheral vector-genome measurement**) · §4.1 C-P4 (**no covariate-adjusted analysis, no
pair-fed or weight-matched arm**) · §4.1 C-P5 (**no spleen, thymus or marrow in either gene-therapy
paper**) · §4.6 (**no measurement bounding off-CNS expression beyond six organs**) · §4.3 (**the P30
clause occurs exactly once repo-wide**). 🔴 **No absence in this file is a PubMed count of mine — no
external fetch was made in this act.**

### 8.5 · New tool traps, described so the next actor does not repeat them

1. 🔴 **`grep -E` with `\|` searches for a literal pipe.** Silent, exit-1, count-0. **Validate every
   negative alternation with a positive control term inside the alternation** (§0.1, thirteenth mode).
2. 🔴 **A quantity's NAME can be wrong in the primary and inherited verbatim.** *"Hypocapnia"* labels a
   serum `Total CO₂`. **Check that the word names the assay**, not only that the number is transcribed
   correctly (§1.3).
3. 🔴 **A ratio endpoint whose denominator is itself the rescued phenotype is uninterpretable after
   rescue.** Organ-weight ratios are the type case; the repository already learned it for brain and did
   not transfer it (§1.4).
4. 🟢 **A fold-change ratio is unit-invariant.** Where a unit defect blocks numeric cross-model
   comparison, **within-model ratios of fold-changes remain licensed** — one legitimate arithmetic
   survives the block, and it was the one that mattered (§4.4).
5. 🔴 **"Expression not detected" ≠ "vector not present."** Every peripheral WWOX measurement in this
   literature is a protein blot under a restricted promoter; **transduction was never measured outside
   the brain** (§4.6).

### 8.6 · V0 SHADOW TRACE

| Step | What happened — **including the steps that produced nothing** |
|---|---|
| **BASELINE** | Enumerated `disease-models/wwox/` (430 md · 102 json · 11 jsonl · 19 csv · 5 tsv), then swept **unscoped, bilingual, word-bounded**. 🔴 **The first sweep was VOID** — twelve alternation patterns searched for a literal pipe and returned twelve zeros that looked like findings (§0.1). Re-run before any of it was used. Read the peripheral denominator audit, the two Purkinje nodes, the metabolic-gating trace, the survival-validity node and the `PMID 19936220` manifest in full. |
| **DIVERGE** | Seven classes `R1`–`R7`, each required to name a **different measurement**; two of the brief's candidates merged into `R7` and one kept only because it had its own discriminator. 🔴 **The divergence MISSED the winning branch** — it contained no loss-of-function direction, and `S-KO` (§4.2) came from outside it, found while costing the Purkinje ladder. **Recorded, not smoothed over.** |
| **CONNECT** | Clinical acid-base chemistry (the anion gap as a normal-gap/raised-gap discriminator) · paediatric failure-to-thrive and the stereotyped undernutrition syndrome · the urea:creatinine convention · conditional-genetics logic (deletion and replacement addressed to the **same promoter**). 🔴 **Nothing transferable was found in AAV-biodistribution practice** beyond what the repository already held — that CONNECT branch returned nothing and is recorded as having returned nothing. |
| **PREDICT** | Eight predictions `C-P1`–`C-P8` **written to disk before any targeted search**, three declared `INHERITED` in advance, one (`C-P7`) written specifically to cut against my own favoured hypothesis. |
| **SEARCH** | Repository-only, unscoped, bilingual. 🔴 **No external fetch, no PubMed, no web** — so no zero here is a PubMed count and none is offered as one. **Two searches returned nothing usable and are recorded as such:** `pair-fed\|weight-matched` returned only a hepatocyte-cKO food-intake note (a different object), and the search for a peripheral vector-genome measurement returned **nothing at all**, which is the §4.6 absence rather than a result. |
| **ADJUDICATE** | 6 confirmed · **1 refuted against me** (`C-P3`, glucose does have a time course) · **1 confirmed in a way that cost my favoured hypothesis its standalone testability** (`C-P7`). `R5` refuted for glucose. `R7` largely adjudicated. `R1` strongly favoured for growth/metabolic and **explicitly not** for the six unmeasured families. |
| **REVISIT** | The `C-P3` refutation sent me back to the glucose time course — **and the P30 clause in it is `N2`, the strongest single finding in the file.** 🎯 **The refuted prediction produced more than any confirmed one.** Revisiting §1.5 with `S-KO` in hand also forced the §4.2 bound table: two concordant sentences are not an opened panel, and the repository has been burned by exactly that before. |

### 8.7 · Self-grade

| Axis | Grade | Justification |
|---|---|---|
| **The primary axis** | 🟢 **A−** | The paradox's **premise** is addressed rather than its surface: `S-KO` makes a neuron-restricted rescue expected, and `N2` shows the one measured peripheral analyte is dissociated from survival in both directions people assumed it ran. Marked down because `CNE-C1` — what *"metabolic abnormalities"* covers — is the bound the whole finding hangs on and I could not open it. |
| **The panel** | 🟢 **A−** | Six endpoints, one animal, two tubes, one balance, at a timing **forced** by an argument rather than chosen; the discriminator column filled for every row; six rejections stated with reasons; the scoring rule applied **against** the tempting endpoint (platelets demoted on width-without-discrimination, glucose retired to positive control). 🔴 Marked down because `R3` is not separable by it — established by my own prediction, and §5.3 says so instead of hiding it. |
| **Divergence** | 🟡 **C+** | Seven distinct hypotheses with real discriminators — **and the winner was outside all seven.** Graded on the same standard the prior audit graded itself. |
| **Pre-registration** | 🟢 **A** | Persisted before the targeted search; `INHERITED` expectations declared in advance so no confirmation could be re-sold; one prediction written to cut against me, and it did. |
| **Purkinje** | 🟢 **B+** | The honest answer — *"nothing further on the top tier, and the blocker is permission and channel count, not design"* — delivered without inventing a fourth move. One genuine addition (§6.2), stated with its own limit. |
| **Discipline** | 🟢 **A** | **One file written.** No git. No canonical file, registry, queue, ledger, receipt or manifest touched. No `BATCH_COMMIT`. **No external contact, and none prepared.** No purchase. No clinical framing, no dose, no route. Alleles, drivers and species never pooled. `DATO`/`INFERENZA`/`IPOTESI` separated throughout. |
| **Own errors, recorded** | — | (i) The `grep -E '\|'` void sweep (§0.1), caught only because single-term patterns returned numbers while every multi-term one returned zero. (ii) My DIVERGE missed the loss-of-function direction entirely (§4.2). (iii) `C-P3` refuted. (iv) `C-P7` cost `R3` its standalone testability. All four are in the file rather than absent from it. |
| **Overall** | 🟢 **B+/A−** | A paradox addressed at its premise rather than its surface; a published dissociation nobody had used; an absence (no pH, no anion gap) that reorders the panel; an arithmetic nobody performed; a structural constraint that determines the timing; one new tool trap; one correction to a number about to travel — and a trace that failed twice and says so both times. |

---

**End.** Not medical advice; every clinical question is `HUMAN_REQUIRED` and belongs to a treating team.
Read-only toward every canonical file, registry, queue, ledger, receipt and the state manifest. Nothing
promoted, nothing committed, no receipt claimed, **no git command run, no researcher contacted and no
correspondence prepared**. Public edition: the WWOX-DEE genotype class, never an individual.
