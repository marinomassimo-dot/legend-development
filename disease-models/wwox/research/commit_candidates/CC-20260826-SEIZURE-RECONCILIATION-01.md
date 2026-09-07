# COMMIT CANDIDATE — the mouse-seizure contradiction, reconciled across five canonical claims

**Candidate ID:** CC-20260826-SEIZURE-RECONCILIATION-01
**Date:** 2026-08-26
**Status:** queued; **no canonical scientific file modified**, no meta modified, no ledger appended
**Mode:** cross-claim reconciliation over claims already at registry, plus one new full-text read
**Supersedes:** the CLAIM 037 section of [`CC-20260825-ADVERSARIAL-FALSIFICATION-01`](CC-20260825-ADVERSARIAL-FALSIFICATION-01.md);
**extends and corrects** [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md), which found a
two-claim contradiction where there is a five-claim one, and dated the mouse electrographic
evidence to 2026 when it dates to 2020.
**Change class:** 🔴 **MAJOR** — a `DATO` claim's headline is false, and a canonical prohibition
in a `consolidated baseline` claim forbids statements that three other canonical claims already
make. Requires operator authorization.
**Target WM:** current at BATCH_COMMIT time; rebase required
**Batch gate:** intentionally untouched

---

## The finding in one sentence

`CLAIM 005` contains the sentence **"No canonical statement may describe a Wwox-null mouse as
showing epileptogenesis"**, and **three canonical claims in the same file already do** — `CLAIM
004` (`consolidated baseline`), `CLAIM 011` and `CLAIM 016` — while `CLAIM 037`'s title asserts
the phenotype is *"explicitly absent in Wwox-null mice"* against four independent primary
datasets, the earliest from **2020**.

---

## Why the previous candidate under-counted

[`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md) framed this as `CLAIM 037` versus
`CLAIM 011` and dated the falsifier to Obeid 2026. Both are too narrow, and the reason is worth
recording because it is the same shape as the error it was repairing: **it enumerated the papers
it remembered rather than the claims that share the entity.** A mechanical pass over the
registry — every claim coupling a `Wwox`-null mouse to a seizure-family endpoint — returns five,
not two, and the earliest primary evidence is six years older than the candidate says.

---

## Reading provenance

| Source | Artifact | SHA-256 | Surface | Status |
|---|---|---|---|---|
| PMID 42422765 — Obeid 2026, *Mol Ther Methods Clin Dev* 34:201791 | `files/fulltext/PMID42422765_Obeid2026_PMC.html` | `00fadaf411998f4e453f…` | structured PMC text | re-adjudicated here |
| PMID 32000863 — Cheng 2020, *Acta Neuropathol Commun* 8:6 | `files/fulltext/PMID32000863_Cheng2020_PMC.xml` | as declared in `deepdive_manifests/PMID32000863.json` | structured PMC XML | re-adjudicated here |
| PMID 34747138 — Repudi 2021, *EMBO Mol Med* 13 | `files/fulltext/PMID34747138_Repudi2021_PMC.xml` | as declared in `deepdive_manifests/PMID34747138.json` | structured PMC XML | re-adjudicated here |
| PMID 36828035 — Hussain 2023, *Prog Neurobiol* 223:102425 | `files/fulltext/PMID36828035_Hussain2023_PMC.xml` | `004c59b54b5f57e462ccb39643b5f3adb44e7ecaef5eff8d786cb77c3568fd22` | structured PMC XML (NIHMS1957654) | **new acquisition**, see [`CC-20260826-PMID36828035-01`](CC-20260826-PMID36828035-01.md) |

🔴 **Artifact-root note.** `files/` is gitignored and does **not** travel with a branch. This
worktree's `files/fulltext/` holds **37** artifacts; the shared checkout holds **174**. Every
adjudication above was run with the **shared checkout as artifact root**, and
`PMID33914858_Aqeilan2021.pdf` — cited by the superseded candidate — is **not present in this
worktree at all**. Any validation of this candidate must be re-run there.

No receipt is emitted for the three re-adjudications; they are targeted adjudications of named
propositions, not complete reads. PMID 36828035 is a new read and is handled in its own
candidate.

---

## 1. The seven axes, separated

The operator's decomposition, answered. The load-bearing distinction is that **five different
things have been collapsed into the word "seizure"**, and they have five different evidence
states.

### `OBSERVED_ECOG_SWD` — **DIRECTLY MEASURED. `DATO`.**

Obeid 2026, Figure 7E. *"Quantification of SWD events per animal across groups (WT, KO, and KO +
AAV9-hSynI-hWWOX [HD]). WWOX KO pups exhibited a significantly higher number of SWDs relative to
WT, whereas WWOX-rescued pups (HD) showed a marked reduction in SWD incidence. Data are presented
as mean ± SEM (n = 5 pups per group). … ∗∗∗∗p < 0.0001."*

Method (Methods, *"Surgery and ECoG data acquisition"*): transmitter implanted P14, **continuous
wireless 24/7 ECoG for 7 consecutive days**, single channel epidural over right dorsal cortex,
reference contralateral, screened for interictal spikes and SWDs by a **blinded** investigator,
subset cross-validated against time-synchronised video.

⚠️ Limits, unchanged from the prior candidate and still binding: n = 5; single channel;
acquisition began *"immediately after surgery … without a recovery interval"*, so the earliest
hours carry post-anaesthetic state; recording starts at P14, so onset below P14 is unbounded;
Methods declare mean ± SD while the Figure 7 legend declares mean ± SEM.

### `CLINICAL_SEIZURE_PHENOTYPE` — **MEASURED, but in a different animal and by a weaker method than the electrography.**

Three distinct sub-states, which must not be merged:

| Sub-state | Evidence | Method | Source |
|---|---|---|---|
| **Spontaneous behavioural seizures, `Wwox`-null mouse** | *"In our generated Wwox−/− mice, spontaneous epileptic seizures were commonly observed after postnatal day 12. Seizures were frequently induced by mild stressors including noise, strobe lights and novel cage during routine handling (Additional file 2: Movie S1)."* | opportunistic observation during husbandry + one video | **Cheng 2020** |
| **Provoked seizure susceptibility, `Wwox`-null mouse** | enhanced susceptibility to pilocarpine (50 mg/kg) and PTZ (30 mg/kg); *"Half of the pilocarpine- or PTZ-injected Wwox−/− mice evolved into status epilepticus … SE was not observed in Wwox+/+ and Wwox+/− mice."* | Racine scale, 60 min, three genotypes | **Cheng 2020** |
| **Spontaneous generalized tonic-clonic seizures, `Wwox^P47T/P47T` mouse** | *"repeated spontaneous generalized convulsive activity (11–22 seizures during 43–53 h monitoring periods)"*; all three mutants had >4 seizures per 24 h; WT *"no evidence of seizures"* | **simultaneous video-EEG**, 4-channel bilateral frontal + parietal, **14-day post-surgical recovery**, adult, n = 3 vs 3 | **Hussain 2023** |

🔴 **The `P47T` dataset is the methodologically strongest electro-behavioural seizure evidence in
the entire WWOX corpus** — bilateral multi-channel, recovered animals, simultaneous video, and
electro-behavioural concordance scored on the same events. It is also **not a null**: it is a
SCAR12 missense knock-in. It therefore does **not** falsify a statement restricted to nulls, but
it demolishes the framing that seizures are a *rat* phenomenon.

### `EPILEPTOGENESIS` — **NOT MEASURED ANYWHERE. This is the axis everyone has been talking past.**

🔴 **`epileptogenesis` appears zero times in Obeid 2026.** It appears twice in Cheng 2020, both
times as a label for *seizure susceptibility* (*"To further investigate the enhanced
epileptogenesis in Wwox−/− mice, we tested convulsant agent-induced seizure models"*).

**Epileptogenesis is the process by which a brain acquires an enduring predisposition to
spontaneous recurrent seizures.** Measuring it requires longitudinal observation *through* the
transition — a latent period, a documented conversion, or a manipulation that shifts the
conversion. **No WWOX study has done this.** Cheng 2020 measures susceptibility at a time point;
Obeid 2026 measures epileptiform activity across a 7-day window at one age; Hussain 2023 measures
established seizures in adults.

⇒ **`UNRESOLVED` for every WWOX model.** The word is nomenclature borrowed from the field, not a
measurement made in it.

### `NOT_REPORTED_IN_EARLY_MODELS` — **`NOT_REPORTED`, and the negative was a survey artefact.**

| Paper | Statement about null-mouse seizures | Recording performed? |
|---|---|---|
| PMID 17360458 (Aqeilan 2007) | silent | no |
| PMID 18487609 (Aqeilan 2008) | *"they did not exhibit any abnormal behavior or impaired motor skills"* — a **behavioural** negative | no |
| PMID 19936220 (Ludes-Meyers 2009) | epileptogenesis not measured in any form; only brain measurement is organ weight | no |
| PMID 19500159 (Suzuki 2009) | asserts three times, plus a Table 2 `Epilepsy` row empty for both mouse models, that null mice show no epilepsy | no |

🔴 **None of the four is an electrographic negative, because none of the four recorded.** And
Suzuki 2009 — the terminus of the whole chain — is a **literature survey over papers that never
did EEG**, covering the nulls that existed in 2009. It cannot speak to the Hsu/NCKU null used by
Cheng 2020, which did not yet exist. **`NOT_REPORTED ≠ ABSENT`, preserved and now dated.**

### `CONTINUOUS_MONITORING` — **PERFORMED THREE TIMES, in three different senses.**

| Study | Modality | Duration | Age | Recovery before recording | Channels |
|---|---|---|---|---|---|
| Repudi 2021 (EMBO) | cell-attached electrophysiology | acute | P18–21 | n/a | single cell |
| Obeid 2026 | continuous wireless ECoG | 7 days, 24/7 | P14→P21 | **none** — *"immediately after surgery … without a recovery interval"* | 1 |
| Hussain 2023 | simultaneous video-EEG | 21–53 h | adult >6 wk | **14 days** | 4 (bilateral frontal + parietal) |

🔴 **Not to be inferred:** that EEG was *normal* anywhere else. No continuous recording exists
for the Aldaz/EIIA null, `Wwox^+/−`, `Nes-Cre`, `Syn-Cre`, or any null animal outside P14–P21.

### `GENE_THERAPY_RESCUE` — **`DATO`, and it is the strongest causal design in the corpus.**

Genotype → phenotype → **rescue reverses to `ns` against WT**. Two independent instantiations:
Repudi 2021 (cell-attached firing rate: ~6× in KO, no significant difference between rescued and
WT) and Obeid 2026 (SWD: `****` WT-vs-KO, `****` KO-vs-HD, `ns` WT-vs-HD).

🔴 **The rescue is evidence *for* the phenotype.** A rescue arm is only interpretable if the
untreated arm has the phenotype being rescued. `CLAIM 004` and `CLAIM 011` therefore **assert**
the null-mouse seizure phenotype as a precondition of their own content — which is precisely why
the `CLAIM 005` prohibition is self-violating rather than merely over-broad.

### `CANONICAL_PROHIBITION` — **MALFORMED, and the repair is to retarget it, not delete it.**

The sentence is: *"**No canonical statement may describe a Wwox-null mouse as showing
epileptogenesis.** Whether the mouse lacks the phenotype or dies before expressing it is open and
testable: the earliest rat seizure onset (day 16) already exceeds the entire lifespan of the
mouse null."*

Read strictly — `epileptogenesis` as *process* — the prohibition is **accidentally correct**:
nobody has measured epileptogenesis in any WWOX model. Read as written and as applied, it bans
recording **measured seizure and epileptiform phenotypes**, which three canonical claims already
record.

🔴 **The prohibition's instinct was right and its scope was wrong.** It was built to stop an
unmeasured process claim being imported from a rat into a mouse. That guard is still needed. The
previous candidate proposed deleting it; **deleting it discards the guard along with the defect.**
The repair is to say what may not be asserted (*the process*) instead of what may not be
described (*the animal*).

**Contrast case, in the same registry.** `CLAIM 015`'s boundary reads *"'developmentally
pre-wired' must not be read as 'prenatally demonstrated'"*. That is the **well-formed** shape: it
constrains an *inference from a phrase*. `CLAIM 005`'s bans a *class of fact about an entity*.
The registry already contains the pattern; it was applied at one site and not the other.

---

## 2. The operator's central question, answered

| | Content |
|---|---|
| **Directly measured** | SWD rate, `Wwox`-null, P14–21 (Obeid 2026, `p<0.0001`) · interictal spike rate, same (**at the statistical floor**, see below) · cell firing rate, `Wwox`-null P18–21 (Repudi 2021) · provoked seizure severity, `Wwox`-null (Cheng 2020, Racine) · spontaneous GTCS with concordant EEG, `P47T/P47T` adult (Hussain 2023) |
| **Nomenclature** | **`epileptogenesis`** — used by Cheng 2020 and by the `CLAIM 005` prohibition to mean *seizure susceptibility*, which is not what it means. The prohibition and the data are about different objects, and the collision is lexical before it is scientific. Also **`SWD`**: an absence-type electrographic signature, **not** a synonym for "seizure" |
| **Inference** | that mouse SWD corresponds to the *absence* component of the human WOREE seizure spectrum (Obeid 2026 lists six human types: *"tonic, clonic, tonic-clonic, myoclonic, infantile spasms, and absence"*) · that the rat's audiogenic/kindling phenotype transfers to mice |
| **False** | `CLAIM 037`'s *"explicitly absent in Wwox-null mice"* · `CLAIM 005`'s *"whether the mouse lacks the phenotype or dies before expressing it is open"* — it is not open · the superseded candidate's *"nobody has ever performed continuous video-EEG on a Wwox-null mouse"*, already retracted |

🔴 **Not generalised.** SWD at 0.63/hour in a P14–P21 pup is **not** the audiogenic convulsion of
the rat, **not** the PTZ-provoked GTCS of Cheng 2020, and **not** the spontaneous GTCS of the
`P47T` adult. Four phenomena, four methods, three genotypes, two species. The repair records
them separately or it repeats the error it fixes.

### The one negative that is genuinely uninformative

Obeid 2026 panel 7C prints **`0.2000`** over the WT-vs-KO spike-rate bracket while the running
text calls it *"a significant elevation"*. `0.2000` is **exactly** the floor of a two-tailed
Mann–Whitney at the plotted group sizes (3 vs 2): with complete separation, U = 0 and
p = 2/C(5,2) = 0.2000 — the test **cannot return less**. So the text over-claims, and reading
`0.2000` as *no elevation* is the same error sign-flipped. **`0.2000` here means "not tested".**
`PREMISE_TAG: DEFAULT_FROM_TEXTBOOK` on *"p > 0.05 means no effect"*.

---

## 3. Minimum canonical delta — **prepared, NOT applied**

Five edits. Each is the smallest change that removes a falsehood or repairs a malformed rule;
none rewrites content that is not defective.

### Δ1 — `CLAIM 037`, Title. **MAJOR.**

~~`The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype, electrographically documented, and it is explicitly absent in Wwox-null mice`~~

→ `Seizure-related phenotypes in WWOX rodent models are documented in the rat lde/lde, in the Wwox-null mouse (behaviourally since 2020, electrographically since 2026) and in the P47T knock-in mouse (video-EEG, adult); the audiogenic kindling phenotype remains rat-specific`

*Rationale:* the deleted clause is false against four datasets. The retained clause — that the
**audiogenic/kindling** phenotype is rat-specific — is true and is the part worth keeping.

### Δ2 — `CLAIM 037`, Evidence boundary. **MAJOR.**

Replace the opener *"🔴 I topi Wwox-null non hanno epilessia riportata — affermato tre volte in
PMID 19500159…"* with a `NOT_REPORTED ≠ ABSENT` record: PMID 19500159 is a **literature survey**
over four papers none of which recorded EEG, and it predates the Hsu/NCKU null entirely. **Delete**
*"i topi potrebbero morire prima di convulsionare"* — falsified three ways: a mouse with the same
3–4 week lifespan (`Syn-Cre`) seizes from P9; the null itself shows SWDs at P14–21; and Cheng 2020
observes spontaneous seizures from P12, inside the null's lifespan.

**Keep verbatim and untouched:** the entire rat `lde/lde` dataset, the 95%-female caveat, the
34%-is-a-floor caveat, the vacuolisation caveat, the single-laboratory caveat, and the
`PREMISE: DEFAULT_FROM_TEXTBOOK` on proteasomal turnover. **None is affected by this repair.**

### Δ3 — `CLAIM 005`, Evidence boundary. **MAJOR — retarget, do not delete.**

~~`No canonical statement may describe a Wwox-null mouse as showing epileptogenesis. Whether the mouse lacks the phenotype or dies before expressing it is open and testable: …`~~

→ `No canonical statement may assert EPILEPTOGENESIS — the process of acquiring an enduring predisposition to spontaneous recurrent seizures — in any WWOX model, because no study has measured that process: none has observed the transition longitudinally. Measured seizure and epileptiform phenotypes ARE recordable and are recorded — see CLAIM 004, CLAIM 011, CLAIM 016 and CLAIM 037. PMID 19936220 remains free of any seizure measurement; that is a statement about that paper, not about the animal.`

*Rationale:* preserves the guard (an unmeasured process claim), removes the ban on measured
facts, and stops the claim contradicting three of its neighbours.

### Δ4 — `CLAIM 016`, Evidence boundary. **MINOR — add a cross-reference.**

`CLAIM 016` already carries the correct, hard-won boundary that the lithium arm is **not
genotype-specific**. Add only: the seizure phenotype it rests on is now cross-referenced to
`CLAIM 037` and `CLAIM 011`, and Cheng 2020's own spontaneous-seizure observation
(*"commonly observed after postnatal day 12"*) is **opportunistic husbandry observation plus one
video**, not a scored protocol — a floor, not a rate.

### Δ5 — new `CLAIM 040`. **MINOR (addition).**

*"Neuronal restoration of WWOX suppresses spike-wave discharges in the `Wwox`-null mouse to a
level statistically indistinguishable from wild type."* · `DATO` · P1/P7 · T2 · Source
`PAPER 011`, Figure 7E · **Evidence boundary:** n = 5/group, single channel, no post-surgical
recovery interval, P14–P21 only; the interictal-spike endpoint of the same figure is **not**
tested (panel 7C sits at the Mann–Whitney floor); SWD is an absence-type signature and does not
represent the convulsive seizure types of WOREE.

*Rationale:* the only genotype→phenotype→rescue triad on a seizure-adjacent endpoint in the whole
corpus currently exists as a sub-clause of a gene-therapy claim flagged for an unrelated reason.

---

## 4. What is *not* repaired, and must not be

- **Behavioural seizures in the `Wwox`-null mouse remain weakly measured.** Cheng 2020's
  observation is opportunistic; nobody has run a scored, continuous video protocol on a null.
- **The `PMID 33914858` running-text assertion stays `IPOTESI`.** Its cited figure (Fig. 1A–C) is
  a photograph, a weight curve and a Kaplan-Meier curve, and contains no seizure measurement.
  ⚠️ That adjudication was made against an artifact **not present in this worktree**; it is
  inherited from the superseded candidate and must be re-verified in the shared checkout.
- **`CLAIM 011`'s flag is not lifted.** It concerns the dose axis, not the ECoG axis.
- **No claim of EEG normality anywhere else.**
- **Epileptogenesis stays unmeasured** — that is the whole point of Δ3.

---

## 5. Missing decisive experiment

**Continuous video-EEG, P7–P21, five arms, one design:** `Wwox^−/−` (Aqeilan allele),
`Wwox^ΔCre/ΔCre` (Aldaz/EIIA allele), `Nes-Cre`, `Syn-Cre`, `Wwox^+/−`. Simultaneous video so
electrographic and behavioural events are scored on the same animals; recording from **P7**,
five days earlier than any existing null dataset, because the conditional's behavioural onset is
P9; **≥14-day recovery is impossible at these ages** — so the design must instead stagger implant
and onset across littermates and report the post-surgical interval per animal, which the only
existing null dataset does not do. n ≥ 8/arm: the existing n = 5 is why panel 7C sits at its
statistical floor.

**Adopt the Hussain 2023 montage** — bilateral frontal + parietal, four channels — rather than
Obeid's single channel. Bilateral synchrony is what distinguishes a generalized discharge from a
focal artefact, and the single-channel design cannot make that call.

Primary outcomes: SWD rate/hour; interictal spike rate; electro-behavioural concordance; **age of
first electrographic event** — the only measurement that would begin to address epileptogenesis
rather than assert it.

---

## Review required

🔴 **Operator authorization.** MAJOR on three counts: a `DATO` claim's headline deleted as false;
a canonical prohibition inside a `consolidated baseline` claim rewritten; a new claim proposed.
None is a self-authorized edit.
