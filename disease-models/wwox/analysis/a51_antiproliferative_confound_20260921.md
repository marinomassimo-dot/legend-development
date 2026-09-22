# The A51 anti-proliferative confound — can it be resolved from the published data?

**Date:** 2026-09-21 · **Actor:** Scientist B · **Node:** `A51_ANTIPROLIFERATIVE_CONFOUND`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and every
> ledger. Nothing promoted, nothing committed. **BLOCK-1 observed: no safety triage, no druggability score.**
>
> 🔴 **Provenance rule for this entire file, because the whole node runs on it.** `PMID 42397075` has **no PMC
> deposit**, and the 22 local artefacts its manifest fingerprints (`files/fulltext/PMID42397075_*`) **do not exist
> in this checkout** — `files/fulltext/` is absent entirely. **Every panel value below is a prior session's
> figure attestation, recorded in `deepdive_manifests/PMID42397075.json`, and neither I nor the coordinator can
> re-open the pixels.** Each use is marked `prior-session attestation`. Nothing here is a fresh measurement, and
> the one piece of arithmetic I perform on those values is labelled as my derivation, not as a reading.
>
> **Nothing here is medical advice.**

---

## 0. Read depth declared up front

| Source | Depth **this session** | Returned body length | Figure access |
|---|---|---|---|
| `deepdive_manifests/PMID42397075.json` | 🟢 **all 30 entries read, plus `surface_note`, `source_artifacts` (22), `group_assessment`, `field_density`, `multihop`** | local JSON; not a fetched body | n/a |
| `PMID 42397075` itself | 🔴 **not fetchable — no PMCID**; `convert_article_ids` returns the PMID alone | **0 bytes** | 🔴 **none** |
| `files/fulltext/` | 🔴 **directory does not exist in this checkout** — all 22 fingerprinted artefacts unreachable | n/a | n/a |
| Receipt ledger | `FTR-20260810-42397075-04`, `complete_fulltext_read`, coverage all-`read`, evidence basis states *all ten supplementary figures inspected* | n/a | n/a |

⚠️ **Two provenance notes recorded rather than smoothed.** (i) The manifest's own `receipt` field reads
`FTR-20260810-42397075-03`, while the ledger's closing receipt for this paper is `-04` — the manifest was
evidently written before the reading closed, and the two are not in conflict, but the mismatch should not be
discovered later by someone else. (ii) `convert_article_ids` returns **no DOI** for this PMID; the DOI below is
taken from the manifest's own `doi` field **and** from an in-act `get_article_metadata` response in a prior wave
— **two routes, one of which is silent**, stated as required.

---

## 1. The direct answer

**The confound stands, and the Wave-7 claim was right but under-specified — so this file both confirms it and
sharpens it.** Reading all thirty manifest entries: **no proliferation readout, no cell-death readout and no
total-cell-count exists for the A51-treated arm.** The one proliferation index in the paper — `pH3⁺SOX2⁺` — sits
on supplementary page 10 and carries **only the four genotypes** (WT, KO, WOREE, SCAR12); the A51 arm is on page
12 and its entry records **five identity-marker percentages and nothing else.** `MKI67` appears once, on page 5,
as a **cluster-annotation marker** for cycling radial glia — an annotation, not an assay. No caspase, no TUNEL,
no EdU or BrdU appears anywhere in thirty entries drawn from a **complete** supplementary read.
🔴 **And the sharper point, which Wave 7 did not make: every A51 value is a *percentage of cells*, and the
denominator is never reported.** A percentage cannot separate *more of X* from *fewer of everything else* —
which is the confound in its exact form.
**But the counter-argument is stronger than I allowed, and it partly survives its own test.** I derived the
redistribution arithmetic: if A51 removed only SOX2⁺ cells, the remaining fractions would rise by ≈**1.37×**,
predicting NEUN⁺ ≈8.2 % against the ≈18 % observed. **NEUN⁺ exceeds pure redistribution by roughly a factor of
two, and that is not explained by progenitor removal alone.** SATB2⁺ (≈1.5× the prediction) and CTIP2⁺ (≈1.1×)
do not. ⇒ **The published data support neither reading cleanly.** They are consistent with a **mixed** effect —
some genuine neuronal gain on top of a compositional shift — and they cannot be resolved further, because the
arithmetic's own assumption (that total cell number changed *only* through the SOX2⁺ loss) is precisely what an
anti-proliferative agent would violate, and **the number that would test it was not reported.**
**One unreported number decides the whole thing: total cells per organoid, or any absolute count, under A51
versus vehicle.** The paper reports exactly that quantity for the genotype comparison (Figure 2 panel D: WT
5649, WWOX-KO 3020, SCAR12 3422, WOREE 5916) and **provides no equivalent for the treated arm.**

---

## 2. Task 1 — the manifest entry table: what each attests, and on what surface

All thirty entries were read. The table lists every entry that could bear on proliferation, death, cell number or
the A51 arm; the remainder are listed in aggregate beneath.

| # | Surface | Anchor | What it attests | Bears on the confound? |
|---|---|---|---|---|
| **23** | `figure` · `panel_only` | **Supplementary figures volume page 12**, 170 ppi, **re-read at 258 ppi** | 🔴 **THE A51 PANEL.** *"Supplementary Figure 7, panels F and G, percentage of cells, groups WT NT / WT DMSO / KO-1B / KO-1B A51"* — then **SOX2⁺, SOX2⁺MYC⁺, SATB2⁺, NEUN⁺, CTIP2⁺**, with brackets. **Five identity markers. Nothing else.** The anchor adds that the same page carries panel C, an **AP2γ immunoblot** — and that immunoblot is a **genotype/rescue** comparison (JH-WT 1 against the mutant lines and the AAV9-rescued knockout), **not an A51 condition** | 🔴 **Yes — and it is the negative.** No pH3, no Ki67, no EdU/BrdU, no caspase, no TUNEL, **no denominator** |
| **24** | `figure` · `panel_only` | Supplementary volume **page 10**, 170 ppi, re-read at 258 ppi | 🔴 **THE ONLY PROLIFERATION INDEX — and it is the genotype arm.** *"Supplementary Figure 5, panel B, pH3+SOX2+ percentage of cells: WT about 3, WWOX-KO about 10 with bracket ****, SCAR12 about 4.5 with no bracket, WOREE about 6 with bracket *."* Also panel F TCF-4 and **panel E p53: WT 1, KO2 1.51, KO1 1.61** — again genotype only | 🔴 **Yes — it is the readout that exists for the wrong arm** |
| **2** | `figure` · `panel_only` | Figure 2, panels D/E/F, 174 ppi | 🔵 **THE ONLY TOTAL CELL COUNTS**: *"Panel D cell counts: WT 5649, WWOX-KO 3020, SCAR12 3422, WOREE 5916."* **Genotype arm** | 🔵 **Yes — it proves the paper knew how to report this quantity, and did, for the other comparison** |
| **29** | `figure` · `panel_only` | Supplementary volume **page 5**, 170 ppi | `MKI67` appears here: *"Panel E: VIM/SOX2/GFAP for RG, **CENPF/MKI67/TOP2A for cycling RG**, FAM107A/HOPX/LIFR for outer RG, NEUROD6/MEF2C/SYN1 for neurons."* | ⚠️ **No.** This is **cluster annotation**, not a treatment readout. `MKI67` is used to *name* a cell type, not to measure proliferation under a drug |
| **22** | `figure` · `panel_only` | Supplementary volume **page 18**, 170 ppi, re-read at 258 ppi | 🔴 **THE ASYMMETRY.** For the **AAV9** arm the paper *does* report no-effect controls: *"Panel E: volcano of untreated over treated radial glia, every point labelled no change. Panel F: cell-cycle densities for WOREE n=2560 and WOREE-wwox n=2003, superimposed."* | 🔴 **Yes — the gene-therapy arm carries a cell-cycle readout and an n; the pharmacological arm carries neither** |
| **17** | `body` · `text_only` | Results p. 11; dose and schedule in supplementary File009, *"MYC inhibition"* | *"established to suppress Wnt and MYC expression"* — the compound descriptor. **125 nM, weeks 8→15** are recorded in the same entry's anchor chain | context |
| **25** | `figure` | Supplementary volume page 7 | Suppl. Fig. 4 — MYC pseudobulk in RG across genotypes; SOX2⁺MYC⁺/SOX2⁺ WT ≈20 %, KO-A2 ≈43, KO-1B ≈54 | genotype arm only |
| **18–20** | `body` | Statistical analysis | *"Experiments were performed in independent differentiations, except for single-cell RNA-seq, MYC inhibition and NSCs CHIP-Seq"*; *"No randomization or blinding was applied in this study"*; multiplicity correction declared | 🔴 **Yes — the A51 experiment is one of the three without independent differentiations** |
| 0,1,3–16,21,26–28 | `body` and `figure` | Results/Discussion/Figs 2,4,5,6, Suppl. 1,8,9,10 | MYC as top RG gene; the maturation phenotype; Fig. 4J's one-sided P; the *"similar to WT"* rescue over-read; *"without correcting RG abnormalities"*; the 17-fold WWOX-protein spread; patient genotypes; the WOREE-vs-SCAR12 empty volcano | not proliferation/death readouts |

**Result of the census, stated exactly:** across **30 locators drawn from a reading whose receipt records that
all ten supplementary figures were inspected**, the strings `pH3` and `prolifer` occur **only** at entry 24
(genotype arm), `MKI67` **only** at entry 29 (cluster annotation), `cell count` **only** at entry 2 (genotype
arm), and **`caspase`, `TUNEL`, `EdU`, `BrdU`, `apopto`, `viability` occur nowhere at all.**

⚠️ **The honest bound on that negative.** This is a **prior session's non-observation across a complete
supplementary read**, not a locator-set artefact and not a re-verifiable absence. It is stronger than "the
manifest doesn't mention it" and weaker than "I looked and it is not there." **It is recorded at that strength
and no higher.**

---

## 3. Task 2 — does the readout that exists resolve the confound? **No, and the reason is structural**

`pH3⁺SOX2⁺` measures mitotic progenitors across **WT / KO / WOREE / SCAR12**. The A51 question is about
**KO-1B versus KO-1B + A51**. The genotype arm cannot substitute, for three independent reasons:

1. **Wrong contrast.** It answers *"is the untreated knockout hyperproliferative?"* (it is: ≈10 % vs WT ≈3 %,
   `****`). It says nothing about what A51 does to that index.
2. **Wrong page, wrong figure, and the paper had the option.** The proliferation index is Suppl. Fig. 5 on page
   10; the A51 arm is Suppl. Fig. 7F–G on page 12. **The assay existed, in the same supplement, two pages away,
   and was not applied to the treated condition.**
3. **Enormous dispersion even where it was applied.** The same entry records *"Whiskers on SCAR12 and WOREE reach
   41 and 44"* against medians of ≈4.5 and ≈6 — so even the genotype-arm index is a wide, weakly-powered
   measurement. Extrapolating it to a treated condition would compound that.

⇒ **The confound is not resolved by anything the paper reports.**

---

## 4. Task 3 — the minimum the paper would have had to report

Three quantities, none exotic, and **the paper demonstrably knew how to produce two of them**:

| Missing quantity | Why it decides | Does the paper report it elsewhere? |
|---|---|---|
| **Proliferation index in KO+A51 vs KO+DMSO** (`pH3⁺SOX2⁺`, or EdU/Ki67) | Directly distinguishes *fewer progenitors because fewer were made* from *fewer progenitors because the excess resolved* | 🟡 **Yes — for the genotype arm** (Suppl. Fig. 5B). The assay was in hand |
| **A cell-death readout in KO+A51** (cleaved caspase-3, TUNEL, viability) | A51's parent compound **activates p53**; the paper itself measures p53 across genotypes (WT 1, KO2 1.51, KO1 1.61). **Suppression and killing look identical in a percentage** | 🔴 **No — nowhere, for any arm** |
| 🔵 **Total cells per organoid, or any absolute count, in KO+A51 vs vehicle** | 🔴 **This one alone would decide it.** Every A51 value is a *percentage of cells*; the denominator is never given. **If total cell number fell under A51, the entire fraction table can move without a single new neuron** | 🔵 **Yes — for the genotype arm.** Figure 2 panel D: **WT 5649, WWOX-KO 3020, SCAR12 3422, WOREE 5916**. And the AAV9 arm gets its own n (WOREE 2560 / WOREE-wwox 2003). **The treated pharmacological arm gets neither** |

🔴 **That asymmetry is the finding of this section.** Within one paper, the **gene-therapy** arm receives a
DEG volcano, a cell-cycle density comparison and explicit n's — offered as a **safety** argument — while the
**pharmacological** arm receives five identity-marker percentages with no denominator, no proliferation index
and no death readout. **The arm that needed the controls least got them.**

---

## 5. Task 4 — the counter-argument, at full force, and then the verdict

### 5.1 The counter-argument

**A pure anti-proliferative agent should not increase a neuronal marker.** `NEUN⁺` rose from ≈6 % to ≈18 %, with
a `*` against the untreated knockout and `ns` against wild type. If A51 merely suppressed the progenitor pool,
the intuition says nothing should have *gained*. **This is the strongest argument for the normalisation reading
and it must be given its weight.**

### 5.2 The reply — and it is arithmetic, not rhetoric

🔴 **Every A51 value is a *percentage of cells*.** Percentages are compositional: remove cells from one category
and **every other category rises automatically**, with no new cells of any kind. So the intuition in §5.1 is not
valid as stated — a fraction *can* rise under pure removal.

### 5.3 My own derivation, with its assumptions stated — `INFERENZA`, not a reading

🔵 **This is a calculation I performed on prior-session panel values. It is not a measurement, it is not in the
paper, and it is not in the manifest.**

**Assume** (a) panels F and G share one denominator, (b) the categories are sufficiently non-overlapping, and
(c) **A51's only effect is to remove SOX2⁺ cells** — the strictest pure-anti-proliferative case.

SOX2⁺ falls ≈60 % → ≈33 %, i.e. **27 percentage points of the original total**. The denominator falls to ≈73 %,
so every surviving fraction is inflated by ≈**100/73 ≈ 1.37×**.

| Marker | Observed KO | Predicted under pure removal (×1.37) | Observed KO+A51 | Observed ÷ predicted |
|---|---|---|---|---|
| **NEUN⁺** | ≈6 % | ≈8.2 % | **≈18 %** | 🔵 **≈2.2×** |
| SATB2⁺ | ≈0.35 % | ≈0.48 % | ≈0.7 % | ≈1.5× |
| CTIP2⁺ | ≈0.2 % | ≈0.27 % | ≈0.3 % | ≈1.1× |

⇒ **NEUN⁺ exceeds pure redistribution by roughly a factor of two. Progenitor removal alone does not account for
it.** SATB2⁺ and CTIP2⁺ sit close to what redistribution predicts, which is consistent with their `ns` brackets.

**The counter-argument therefore survives, in narrowed form: something real happened to the pan-neuronal
compartment, and it is not purely arithmetic.**

### 5.4 Why that still does not resolve it

🔴 **Assumption (c) is exactly what an anti-proliferative agent violates.** If A51 also suppressed division of
other cycling populations — which is what a general elongation blockade does — the denominator falls further,
the inflation factor exceeds 1.37, and more of the NEUN⁺ rise is absorbed. **The factor is unknown because the
denominator was never reported.** And a rise in NEUN⁺ *percentage* is compatible with the absolute number of
NEUN⁺ cells being flat or even falling, if the organoid is simply smaller.

⚠️ Three further limits on the arithmetic, stated so it is not over-read: the values are *"about"* figures from a
prior session's 170/258 ppi panel read; the markers are not guaranteed mutually exclusive; and panels F and G may
not share a denominator at all.

### 5.5 Verdict

> **The published data support neither reading cleanly.** A pure anti-proliferative account under-predicts the
> NEUN⁺ rise by roughly twofold; a clean normalisation account cannot be sustained either, because every measure
> is a fraction of an unreported denominator and the agent's mechanism is one that changes denominators. **The
> data are consistent with a mixed effect, and the confound cannot be resolved from what is published.**

**Against my Wave-7 sentence, this is a partial self-correction and I record it as one.** *"Cannot be
distinguished using the published data"* **holds**. *"The experiment has no proliferation index and no cell-death
readout"* **holds, verified across all thirty entries**. What Wave 7 did **not** say, and should have, is that
**there is one piece of internal evidence bearing on the question — the NEUN⁺ magnitude — and it leans against a
purely anti-proliferative reading.** A one-sided finding would have been landed too strong.

⇒ **`TX-004` should be lowered on *ambiguity*, not on *refutation*.** Its only supporting experiment cannot
demonstrate what it is cited for; it also cannot be said to have shown the opposite.

---

## 6. Task 5 — is the A51 gap a one-off or a pattern? One paragraph

Within this single paper it is **not** a one-off but an **asymmetry**: the gene-therapy arm carries a DEG volcano,
superimposed cell-cycle densities and explicit n's, while the pharmacological arm carries five percentages and no
denominator — the arm most in need of the controls received none of them. Looking across the intervention arms
LEGEND holds, a weaker but real pattern shows: the common missing element is not a *specific* assay but a
**denominator** — the A51 arm reports fractions without totals; the mouse gene-therapy survival threshold has
**no measured expression difference behind it**; the `lde` rat migration result rests on `n = 3` stated once in
Methods and nowhere in Results; and the human cohort endpoints sit in a column headed *"Death/ last date of
examination"* that does not separate death from follow-up. 🔴 **The recurring defect in this corpus is a
numerator reported without its denominator**, and `W7-C4`'s observation that LEGEND has no in-system selectivity
control belongs to the same family. **Stated as an observation only; no governance proposal is made here, and the
question of whether LEGEND should adopt a minimum readout set is not this file's to answer.**

---

## 7. What LEGEND already knew · what is new

### 7.1 Already held

- `DL-THER-089`: the full Suppl. Fig. 7F–G split; A51 at **125 nM, weeks 8→15**; non-selectivity; the three
  declared method defects (no independent differentiations for the MYC-inhibition experiment, no randomisation or
  blinding, one clone); the open BLOCK-1 question; `IPOTESI`, not a candidate.
- Wave 6: A51 ≈ BTX-A51 (CK1α + CDK7 + CDK9), zero CNS data, contested Wnt direction.
- Wave 7: the schedule finding — continuous exposure is the harmful regimen in a developing vertebrate; `W7-C4`,
  the missing in-system selectivity control.
- `CLAIM 028` and `TX-004`'s rule that *"lower MYC/Wnt = better" is NOT a safe default*.

### 7.2 New in this node

1. ✅ **Verified across all 30 manifest entries**: the A51 arm has **no proliferation index, no cell-death
   readout and no total cell count**. `pH3`/`prolifer` occur only at entry 24 (genotype arm); `MKI67` only at
   entry 29 (cluster annotation); `cell count` only at entry 2 (genotype arm); `caspase`, `TUNEL`, `EdU`, `BrdU`,
   `apopto`, `viability` **occur nowhere**.
2. 🔴 **The sharper statement of the confound, which Wave 7 did not make: every A51 value is a *percentage of
   cells* and the denominator is never reported.** That is the confound in its exact form.
3. 🔵 **A quantitative test of the counter-argument, derived here**: pure SOX2⁺ removal predicts a ≈1.37×
   inflation of every other fraction; **NEUN⁺ exceeds that by ≈2.2×**, SATB2⁺ by ≈1.5×, CTIP2⁺ by ≈1.1×.
   **The pan-neuronal gain is not fully arithmetic — and the arithmetic's own assumption is what the drug
   violates.**
4. 🔴 **The within-paper asymmetry**: the **AAV9** arm gets a DEG volcano, cell-cycle densities and n's
   (WOREE 2560 / WOREE-wwox 2003) offered as *safety*; the **A51** arm gets none of these.
5. ✅ **The paper reports the deciding quantity for the other comparison and not for this one**: Figure 2 panel D
   gives **WT 5649, WWOX-KO 3020, SCAR12 3422, WOREE 5916**. No A51 equivalent exists.
6. 🔴 **Partial self-correction recorded against Wave 7**: the claim stands, but it was one-sided; the NEUN⁺
   magnitude is real counter-evidence and was not weighed.
7. ⚠️ **Provenance defects found while reading the manifest**: `files/fulltext/` **does not exist in this
   checkout**, so all 22 fingerprinted artefacts are unreachable; and the manifest's `receipt` field says `-03`
   while the ledger's closing receipt is `-04`.

---

## 8. Corrections, with exact file and line coordinates

**W8-C1 — `DL-THER-089` should carry the confound in its sharpened form, and the self-correction with it.**
- **File:** `disease-models/wwox/research/discovery_ledger_current.md` · `DL-THER-089` begins **line 2331**; the
  panel table follows **line 2337**; the BLOCK-1 bullet follows the table.
- **Proposed addition:** `🔵 **AGGIORNAMENTO 2026-09-21 (seconda passata) — il confondimento antiproliferativo è VERIFICATO e NON RISOLVIBILE dai dati pubblicati, ma NON è unilaterale.** Lette tutte e **30** le voci del manifest `PMID42397075.json`: per il braccio **A51** non esiste **alcun indice di proliferazione, alcun readout di morte cellulare e alcun conteggio cellulare totale**. `pH3`/`prolifer` compaiono solo alla voce 24 (braccio **genotipico**: Suppl. Fig. 5B, WT ≈3 % vs KO ≈10 % `****`); `MKI67` solo alla voce 29, come **marcatore di annotazione di cluster**; `cell count` solo alla voce 2 (Fig. 2D: **WT 5649, WWOX-KO 3020, SCAR12 3422, WOREE 5916**, braccio genotipico); `caspase`, `TUNEL`, `EdU`, `BrdU` = **zero**. 🔴 **E tutti i valori A51 sono *percentuali di cellule* con denominatore mai riportato** — una percentuale non distingue «più di X» da «meno di tutto il resto». ⚖️ **Contro-argomento, pesato e parzialmente valido:** se A51 rimuovesse solo cellule SOX2⁺ (60 %→33 %), ogni altra frazione salirebbe di ≈**1,37×**, predicendo NEUN⁺ ≈8,2 % contro il ≈18 % osservato — **NEUN⁺ eccede la redistribuzione pura di ≈2,2×** (SATB2⁺ ≈1,5×, CTIP2⁺ ≈1,1×). *Derivazione dello scrivente su valori di pannello di sessione precedente; `INFERENZA`, non una misura.* ⇒ **I dati non sostengono né la lettura «normalizzazione» né quella «antiproliferativa»; sono compatibili con un effetto misto.** 🔵 **Un solo numero non riportato deciderebbe: cellule totali per organoide sotto A51 contro veicolo.** 🔴 **Asimmetria interna al paper:** il braccio **AAV9** riceve un volcano DEG, densità di ciclo cellulare sovrapposte e le n (WOREE 2560 / WOREE-wwox 2003), offerti come argomento di **sicurezza**; il braccio **farmacologico** non riceve nulla di tutto ciò.`

**W8-C2 — the manifest's receipt pointer is stale.**
- **File:** `disease-models/wwox/research/deepdive_manifests/PMID42397075.json` · top-level key `receipt`
- **Exact current value:** `"receipt": "FTR-20260810-42397075-03"`
- **Proposed:** `"receipt": "FTR-20260810-42397075-04"` — the ledger's closing receipt for this paper, which is
  also the one `PAPER 094` and `DL-THER-089` both cite. ⚠️ **A manifest is a receipted artefact; whether it may
  be edited outside a `BATCH_COMMIT` is not my call.** Flagged, not changed.

**W8-C3 — the artefact set this corpus's strongest organoid reading depends on is unreachable.**
- **Observation:** `files/fulltext/` **does not exist in this checkout**, so **all 22 artefacts** fingerprinted by
  `PMID42397075.json` are unreachable, and `PMID 42397075` has **no PMC deposit** to re-derive them from.
- **Why it matters here specifically:** this node, Wave 1's TX-004 classification, Wave 3's ceiling analysis and
  Wave 6's A51 identification **all** rest on that one manifest. LEGEND already recorded the general form of this
  problem for `PMID 34268881` — *"files/ is gitignored by design, so a manifest travels and its evidence bytes do
  not"* — and there the artefacts were **re-acquirable from PMC and re-derived byte-identical**. 🔴 **Here they
  are not re-acquirable by that route at all.**
- **Proposed:** record `PMID 42397075` as a **single point of failure** for the TX-004 axis and queue re-acquisition
  of the PDF and supplementary volume by whatever route the prior session used.

**W8-C4 — the deciding experiment can be stated in one line and should be.**
- **File:** `disease-models/wwox/analysis/mechanism_intervention_map.md` · `DECISIVE_PRECLINICAL_EXPERIMENTS`
- **Proposed:** extend the `E-10` row (which Wave 7 already proposed extending) so that **every arm reports
  absolute counts and a proliferation and death readout, not fractions**. 🔵 **The single cheapest discriminator
  for the existing data is not a new experiment at all: total cells per organoid under A51 versus vehicle. If the
  authors hold it, one number closes this node.**

---

## 9. Source attribution

Retrieved from **PubMed**; the primary was **not** retrievable and was not re-read. DOI verified on two routes as
required — ⚠️ **one of which is silent**: `convert_article_ids` returns the PMID alone with **no DOI** for this
record; the value below is carried by the manifest's own `doi` field **and** by an in-act `get_article_metadata`
response from an earlier wave of this session.

| PMID | Citation | DOI |
|---|---|---|
| 42397075 | Steinberg DJ, Zonca A, Abdellatif D *et al.* Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026 — 🔴 **no PMCID; artefacts unreachable in this checkout; all panel values are prior-session attestations** | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |

---

**End.** Not medical advice. No safety triage was run and no druggability score assigned. Read-only toward every
canonical file; nothing promoted, nothing committed.
