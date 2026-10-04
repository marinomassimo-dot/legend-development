# COMMIT CANDIDATE — CC-20261004W9-A-PETROZZIELLO-PANELS-01 — panels of PMID 42395553 (bioRxiv preprint, NOT peer reviewed): the neuronal-toxicity datum is quantified and genotype-independent; the "no instability" half is one overexpression-only reporter model

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist A of intake wave 9, 2026-10-04.
**Change class:** **MINOR.** Corrects one parenthetical premise in the claim registry's `CLAIM 011`
PREMISE_TAG and in the working model's dose-ceiling paragraph, and adds magnitudes to one dismissal
premise. It narrows no `consolidated baseline` claim. A preprint never raises a claim's status.
`context_policy: QUESTION_DRIVEN`. **Not medical advice.** Applied recombinant protein in cell
culture and post-mortem tissue: no allele of the reference genotype is modelled.

---

## 1 · What the panels show (artefact: the declared PDF, sha256 90078770d759d421a77ab5485e1f553575a5c2efd04df3accc076c6ae062b746)

- **Fig 4B (read as an image).** 100 ng/mL applied WWOX lowers viability in both cortical-neuron lines:
  27Q about 0.112 to 0.079 (ratio 0.71), 65Q about 0.104 to 0.067 (ratio 0.64), hand readings. The legend
  reports a genotype main effect (F(1,28) = 6.181, p = 0.0192; recomputed 0.0191) and no interaction
  (F = 0.3129, p = 0.5804; recomputed 0.5804). The toxicity is therefore quantified and not
  disease-specific on these data; "no between-genotype comparison is reported" is inaccurate.
- **Fig 5B.** The applied-protein gamma-H2AX rise is about ten percent (vehicle ~30,000; 100 and 150 ng/mL
  ~33,000-33,300; camptothecin ~36,500). **Supp Fig 2:** viability at 100 ng/mL, 24 h, same line, is about
  0.32 of vehicle, so the damage readout and cytotoxicity are not separable.
- **Fig 7.** The instability null is a single RPE-1 CAG115 safe-harbour reporter, six clones per arm, 42 days,
  overexpression only; WWOX ~40 times NTC; gamma-H2AX ~1.23 times NTC; traces overlap. **Fig 3B** is the
  inherited repeat length (about 40-51), not somatic instability.
- Arithmetic screen: Fig 7C F(2,11) = 18.07 printed p = 0.003; recomputed p = 0.00033 (printed value
  understates; direction unaffected).

## 2 · Records gated and verdicts

| record | wording | verdict |
|---|---|---|
| `CLAIM 011` PREMISE_TAG and the working model's dose-ceiling paragraph | "no between-genotype comparison is reported" / "Figure 4B is unread, so the toxicity is not disease-specific and is not quantified" | **Narrowed**: Fig 4B read; quantified; a genotype main effect is reported, the interaction is not significant. The record's conclusion (toxicity not disease-specific; no dose position changes; no hazard claim) **holds**. |
| `DIS-028` | gamma-H2AX non-monotonic in WWOX | **Holds**; gain-side magnitudes and the cytotoxicity coincidence are added. Revival trigger unchanged. |
| the title claim "contributes to DNA damage but not somatic instability" (no landed claim carries it) | | Not carried anywhere as a claim; this reading limits it to an overexpression-only reporter model. |
| `FT-047`-family queue rows | none depends on the panels | **Unaffected**. |

## 3 · Ops (provisional; each `old` measured unique in its record)

### 3.1 · `disease-models/wwox/registries/claim_registry_current.md`, record `CLAIM 011`

| field | value |
|---|---|
| op | `replace` |
| old | `the source reports no 65Q-versus-27Q comparison and Figure 4B is unread, so the toxicity is not disease-specific and is not quantified` |
| new | `the source reports a genotype main effect (F(1,28) = 6.181, p = 0.0192) and no treatment x genotype interaction (p = 0.5804), and Figure 4B, read as an image in wave 9, shows viability falling to about 0.71 (27Q) and 0.64 (65Q) of vehicle by hand reading, so the toxicity is quantified and not disease-specific on these data` |

### 3.2 · `disease-models/wwox/registries/working_model_current.md`, dose-ceiling paragraph

| field | value |
|---|---|
| op | `replace` |
| old | `(no between-genotype comparison is reported)` |
| new | `(a genotype main effect is reported, p = 0.0192, with no significant treatment x genotype interaction; viability about 0.71 and 0.64 of vehicle, wave-9 panel reading)` |

### 3.3 · `disease-models/wwox/research/dismissal_ledger_current.md`, record `DIS-028`

| field | value |
|---|---|
| op | `replace` |
| old | `Neither paper cites the other; the observation belongs to reading them together.` |
| new | `Neither paper cites the other; the observation belongs to reading them together. [Wave 9 panel reading of PMID 42395553, hand readings: the applied-protein gamma-H2AX rise is about ten percent (1.10 times at 100 ng/mL) in a culture whose viability at that concentration is about 0.32 of vehicle (Supp Fig 2), so damage and cytotoxicity are not separable; stable overexpression raises gamma-H2AX about 2.0 times in SH-SY5Y and 1.23 times in an RPE-1 reporter line.]` |

## 4 · Verification before propagation

`deepdive_manifest.py --pmid 42395553 --verify-artifacts --require-current-schema` PASS at this commit.
Receipt `FTR-20261004-42395553-02` to be recorded first. Because ops 3.1-3.2 touch two of the four
scientific current files they go through `BATCH_COMMIT` only.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Genotype main effect and no interaction | Two-way ANOVA revealed a significant effect of treatment [F(1, 28)=78.44; p<0.0001], and genotype [F(1,28)=6.181; p=0.0192], with no significant treatment x genotype interaction [F(1,28)=0.3129; p=0.5804] | PMID 42395553, Figure 4 legend, panel B)
- (Toxicity in both genotypes | significantly reduced cell viability in both HD ESC-derived cortical neurons (65Q) (Tukey’s test, p<0.0001) and isogenic control cells (27Q) (Tukey’s test, p<0.0001) | PMID 42395553, Figure 4 legend, panel B)
- (No correlation is with the inherited repeat length | WWOX levels did not correlate with CAG repeat length in PFC (Spearman’s correlation, r=0.05302, p=0.8397) | PMID 42395553, Figure 3 legend, panel B)
- (Instability null | WWOX overexpression did not alter the rate of CAG repeat instability at any time point | PMID 42395553, Results, instability paragraph)
- (Instability analysis statistic | Days in vitro showed a significant effect (p<2×10⁻¹⁶), whereas WWOX overexpression had no effect (p=0.877) | PMID 42395553, Figure 7 legend, panel D)
- (Printed ANOVA for Fig 7C | One-way ANOVA revealed a significant effect of treatment on g-H2AX levels [F(2,11)=18.07; p=0.003] | PMID 42395553, Figure 7 legend, panel C)

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** claim_registry_current.md · working_model_current.md · dismissal_ledger_current.md

All three ops applied; two of them touch two of the four scientific current files, which is why this candidate could only land through `BATCH_COMMIT`. `CLAIM 011`'s live `Status` was read before the edit and is **`flagged for review`**, not a consolidated baseline, so this is a MINOR narrowing and not a baseline reversal — a blind locator audit was nevertheless run because the candidate touches a claim and the working model. **Blind locator audit: 6 triples, 6/6 SUPPORTED, 0 NOT_SUPPORTED, 0 UNVERIFIABLE.** Two audit observations were folded into the landed text: the preprint status is restated inside the PREMISE_TAG and inside the `DIS-028` increment (*bioRxiv, not peer reviewed*, so it raises no status), and the dominant printed **treatment** main effect is named beside the genotype effect so the narrowing cannot be read as a disease-specificity finding. The audit also noted that the candidate's prose gloss *«inherited»* repeat length is not the source's word; that gloss is in the candidate's § 1 only and reaches no landed record.

**Not medical advice.**
