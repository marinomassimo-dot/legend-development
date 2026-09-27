# COMMIT CANDIDATE — CC-20260927-CLAIM037-AUDIOGENIC-01

**Candidate ID:** CC-20260927-CLAIM037-AUDIOGENIC-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** `61ea50b`
**Author:** ACTOR_ID `scientist`, Mirror-repair task on `BATCH_20260927_001`
**Source of the task:** Mirror ex-post finding **F9** (BLOCKING-SCIENTIFIC), persisted at
[`session_evaluations/2026-09-27_BATCH_20260927_001_mirror_review.md`](../session_evaluations/2026-09-27_BATCH_20260927_001_mirror_review.md).
`BATCH_20260927_001` diagnosed the defect correctly and deliberately did not repair it; this
candidate is that repair, written and **not applied**.
**Receipts read:** `FTR-20260913-24369382-01` (PMID 24369382, `complete_fulltext_read`,
`source_locator files/fulltext/PMID24369382_Mallaret2014_PMCreader.html`, `source_fingerprint`
`a3a15a3be0353058fcb6160d602e03f5605b5148edfbb8de081d9f98e45a1413`) · superseded prior
`FTR-20260726-24369382-01` (documentary reconstruction, nine `unknown_legacy` coverage keys).
**Manifest read:** `deepdive_manifests/PMID24369382.json`, schema v2, 35 locator entries
(28 body, 7 figure); entries **17, 18, 19, 20, 27, 33** carry this candidate's subject.
**Dossier read:** `fulltext_dossiers/PMID24369382.md` §1, §2, §3.
**First-hand surface read:** yes — `files/fulltext/PMID24369382_Mallaret2014_PMCreader.html` in the
shared checkout, re-hashed in this session to
`a3a15a3be0353058fcb6160d602e03f5605b5148edfbb8de081d9f98e45a1413`, **equal to the receipt's
`source_fingerprint`**. The Methods paragraph *"Animal experiments"* and the Results section
*"Conditional knock-out mouse model"* were read directly on that surface; every quote below was
taken from it, not from the dossier and not from the manifest.
**`context_policy`: `QUESTION_DRIVEN`** — declared. The source was reopened to answer one narrow
question: *does an inspectable method exist in which a `Wwox` mouse was audiogenically provoked,
and with what n, age, stimulus and comparator?* Held before opening it: `CLAIM 037`, `CLAIM 005`,
the two receipts, the manifest and the dossier named above, and the disposition of
`CC-20260922-SEIZURE-ASCERTAINMENT-01`. Nothing else about the paper was re-derived, and the
cohort, variant, pull-down and protein-abundance material of that reading is untouched here.

---

## 1 · CURRENT_TARGET — what `CLAIM 037` says today, and which two clauses are false

`CLAIM 037` (`claim_registry_current.md`, **Status:** `in observation`, **Type:** `DATO`), in its
`Evidence boundary`, carries:

1. ⛔ *"**Neither is a measurement this repository can inspect:** `get_full_text_article(pmc_ids=["PMC3914474"])` was attempted on 2026-09-22 and returned **`full_text: ""`** — **the body is not served by any route available here**, so **there is no `n`, no strain, no stimulus protocol and no control to read.**"*
2. *"And **no Wwox mouse of any allele has ever been audiogenically provoked in any inspectable method** (`PREMISE: NOBODY_LOOKED`; the only provocation ever applied to a Wwox mouse is chemoconvulsant)."*

**Both are false as of 2026-09-13**, and they were already false when they were written on
2026-09-22. The receipt `FTR-20260913-24369382-01` records a `complete_fulltext_read` over a
**local** surface — the failure of one remote route is not the absence of every route, and the
route that worked was the repository's own `files/` directory. The claim's own `REVIVAL_TRIGGER`
names exactly this event: *"acquisition of PMID 24369382's body, **or** any audiogenic-provocation
experiment on a Wwox mouse."* It has fired.

🔵 **What is NOT proposed.** The claim's **title** — *"the audiogenic/kindling phenotype remains
rat-specific"* — is not settled by this candidate, and this candidate does not strike it. What the
mouse now has is an **audiogenic provocation with a comparator**; what it still does not have is a
**kindling** result (no shortening latency across repeated sessions in the mouse, and the two mouse
exposures are at different ages with a survivorship-reduced denominator, which is not a kindling
design), no EEG correlate, and no scoring scale. The rat's 19/20 on three stimulations with
56±24 → 36±4 → 25±3 s latencies remains the only kindling-like series. The honest revision is that
**"audiogenic" is no longer rat-specific and "kindling" still is** — and that distinction is the
substance of the change, not a softening of it.

---

## 2 · PROPOSED_DELTA

Target: `claim_registry_current.md` → `CLAIM 037` `Evidence boundary`, and the `Title`.
**One canonical file, one record, via `BATCH_COMMIT` under `LINT`.**

| # | Delta |
|---|---|
| **D1** | **Strike clause 1 in full.** Replace with: *"🔵 **The body IS inspectable and has been read in full.** `FTR-20260913-24369382-01`, `complete_fulltext_read` over the local surface `files/fulltext/PMID24369382_Mallaret2014_PMCreader.html` (sha256 `a3a15a3b…`), supersedes the 2026-07-26 documentary reconstruction. The 2026-09-22 sentence — that `PMC3914474` is *"not served by any route available here"* — **recorded the failure of one remote route as the absence of every route, while the article's body was already in this repository's `files/` directory.** `D-<next>`: a remote-retrieval failure bounds that route, never the corpus."* |
| **D2** | **Strike clause 2 and its `PREMISE: NOBODY_LOOKED`.** The provocation exists, is inspectable, and is recorded in D3. Retire the premise with its reason, in the convention this registry already uses for a falsified premise, rather than deleting it silently. |
| **D3** | **Record the result, with its denominators and its comparator** (locators in §5): full **constitutive** `Wwox` knock-out; **11–14 kHz** sustained tone, 5–10 min, speakers on three sides of the cage, behaviour video-recorded; at **16 days, 3 of 8** knock-outs seized (audiogenic tonic-clonic, within the first minutes); at **20 days the four surviving mice** were exposed to a 14 kHz tone and **all** seized; **`n = 8` wild-type mice of matched age and background seized zero times** on 11 or 14 kHz. Spontaneous seizures *"a few"* from ~2 weeks, **no denominator in the paper**. Evidence class: **behavioural, photographic/video, unscored — no EEG, no scoring scale, no quantification on the panel** (manifest entry 33). Other stimuli, including handling, *"also induced seizures on some occasions"* — so the stimulus is not shown to be specifically acoustic. |
| **D4** | **Record the constitutive-vs-"conditional" Methods discrepancy as a method fact, not a defect of ours.** The Results section is headed *"Conditional knock-out mouse model"*; the Methods state that the `BK5-Cre` dam's Cre is *"activated in oocytes with Cre protein persisting in the embryo leading to constitutive recombination and producing full knock-out progeny"*. **The animal is a whole-body null.** Consequence, which is why it belongs in the record: this animal models **neither** human missense allele and cannot speak to a hypomorphic phenotype, so the result transfers as *biallelic-null vulnerability*, `T2`, and **not** as a phenotype of `p.Pro47Thr` or `p.Gly372Arg`. |
| **D5** | **Title, minimally amended:** *"the **audiogenic** phenotype is now documented in the constitutive `Wwox`-null **mouse** as well (behaviourally, with a wild-type comparator); the **kindling-like** progression remains rat-specific."* The rest of the title is unchanged. |
| **D6** | **`REVIVAL_TRIGGER`, replaced rather than removed** (the old one has fired): *"reopen on any **electrographic** correlate of an audiogenically provoked seizure in a `Wwox` mouse; on any **repeated-session** audiogenic protocol in one mouse cohort at one age (the kindling question); or on an audiogenic provocation in a **hypomorphic** `Wwox` allele, which is the only route by which this result could reach a WWOX-DEE genotype."* |
| **D7** | **Source line gains** `[[paper_registry_current#PAPER 042]]` (PMID 24369382) with receipt `FTR-20260913-24369382-01`, so the claim's sources name the reading the boundary now rests on. |

**Not proposed, named so the scope is closed:** no `Status` change (`in observation` stands — a
behavioural, unscored, single-laboratory result with a moving denominator does not consolidate
anything); no BLOCCO 1 field; no therapeutic statement of any kind; no edit to the rat evidence or
to any caveat on it; no edit to `working_model_current.md` beyond the changelog row the batch owes;
nothing from Supplementary Video 1, which remains an unretrieved declared debt.

---

## 3 · CLAIM 005 — the boundary re-checked, and what it owes

`CLAIM 005` is **`consolidated baseline`**. Its `Evidence boundary` says: *"Seizures in the Wwox
literature are a **rat `lde/lde`** phenotype — see `CLAIM 037`."* 🔴 **That sentence is now wrong in
the same way `CLAIM 037` was**, and it is wrong in a `consolidated baseline` record.

What survives untouched, and must not be swept away with it:

- the **prohibition** — *"No canonical statement may assert EPILEPTOGENESIS … in ANY WWOX model"* —
  **survives entirely.** Mallaret measures no longitudinal transition, no latent period, no
  conversion and no manipulation of conversion. An audiogenic provocation is **provoked
  susceptibility**, which is one of the four axes `CLAIM 005` forbids merging, not epileptogenesis;
- the statement that **PMID 19936220 contains no seizure measurement** survives — it is a statement
  about that paper;
- the statement that **PMID 19500159's Table 2 asserts no epilepsy in the mouse** survives as a
  description of that survey, and `CLAIM 037` already records why it is a survey artefact.

**Proposed `CLAIM 005` delta (minimal, one sentence):** replace *"Seizures in the Wwox literature
are a rat `lde/lde` phenotype"* with *"Seizures in the `Wwox` literature were long read as a rat
`lde/lde` phenotype; the constitutive `Wwox`-null **mouse** is documented with spontaneous seizures
and with audiogenically provoked seizures against a wild-type comparator (PMID 24369382, receipt
`FTR-20260913-24369382-01`) — behaviourally and unscored. The four axes still must not be merged."*
Everything else in that boundary is byte-identical.

---

## 4 · CHANGE_CLASS — **MAJOR**, declared honestly

**MAJOR.** Not because of the word count, and the candidate does not argue itself down:

1. it **strikes text in a record whose current wording was set by `BATCH_20260922_SEIZURE`, an
   operator-authorised MAJOR batch** (`working_model_current.md` `WM_v5.0`), and one of the two
   struck clauses is that batch's own sentence;
2. it **narrows a sentence inside `CLAIM 005`, which is `consolidated baseline`**;
3. it **retires a `PREMISE: NOBODY_LOOKED`** and reverses the direction of a negative — precisely
   the class `epistemic_discipline` §2 calls the compounding loss.

**Consequences of that class, which this candidate accepts rather than routes around:**

- **`HUMAN_GATE`: yes.** A MAJOR touching a `consolidated baseline` record and an
  operator-authorised batch's text is not landed by the author alone; the operator sees this
  candidate before `BATCH_COMMIT`.
- **`REVIEW_REQUIRED`: Mirror (hostile review, non-zero scientific delta) and `legend-locator-audit`
  (blind), because the claim's title calls the audiogenic phenotype rat-specific and this reading
  narrows it.** §6 is written to be handed to that auditor **alone**.
- **Producer ≠ verifier:** the reading in §5 is `scientist-a`'s (2026-09-13); this candidate is
  written by `scientist` and must be verified by neither.

**`CANONICAL_TARGETS`:** `claim_registry_current.md` (`CLAIM 037`, `CLAIM 005`) —
**one of the four scientific current files**, so this is a `BATCH_COMMIT` object under `LINT`, and
**nothing here is applied by this task.** `working_model_current.md` gains only the changelog row
its batch writes.
**Batch gate:** `BATCH_COMMIT`, MAJOR, operator-authorised.

---

## 5 · DIRECT_EVIDENCE — the reading, with what it does and does not carry

**Surface:** `files/fulltext/PMID24369382_Mallaret2014_PMCreader.html`, sha256 `a3a15a3b…`, read
first-hand in this session; Methods *"Animal experiments"* and Results *"Conditional knock-out
mouse model"* read in full.

| What is measured | What is not |
|---|---|
| Audiogenic provocation with a **wild-type comparator at `n = 8`, zero seizures** | No EEG, no electrographic correlate, no scoring scale, no latency series, no statistic and no error term anywhere in the paper |
| Two exposures, two ages, **two denominators the paper states** (3/8 at 16 d; 4/4 survivors at 20 d) | No repeated-session series in one cohort at one age → **the kindling question is not answered** |
| Stimulus fully specified: 11–14 kHz, 5–10 min, speakers on three sides, video-recorded | **Acoustic specificity is not established** — handling *"also induced seizures on some occasions"* |
| Genotype fully specified in Methods: `Wwox^flox/flox` × `BK5-Cre` dam → **constitutive** null | The animal models **neither** human missense allele; nothing here reaches a hypomorph |
| Spontaneous seizures from ~2 weeks | *"A few"* — **no denominator, no count, no duration** |
| Figure 4: sixteen still frames with burnt-in timestamps | Photographs are documentation, not quantification; **Supplementary Video 1 is unretrieved** and no statement here rests on it |

**Single laboratory, and it is the same laboratory as the claim's other mouse source**
(Aldaz co-author; the knock-out is `Ludes-Meyers et al., 2009`). Never independently replicated.
That belongs in the record next to the result.

---

## 6 · LOCATOR TRIPLES FOR BLIND AUDIT

1. (The provoked-seizure experiment used a sustained 11–14 kHz tone for 5–10 minutes on 16-day-old knock-out mice. | "To investigate susceptibility to epilepsy, 16-day-old knock-out mice were exposed to sustained sound (11–14 kHz tone) for 5–10 min." | `files/fulltext/PMID24369382_Mallaret2014_PMCreader.html` — Results, section headed "Conditional knock-out mouse model", third sentence of the opening paragraph)
2. (At the 16-day exposure, three of eight knock-out mice had audiogenic tonic-clonic seizures. | "A few knock-out mice (three of eight) presented with audiogenic tonic-clonic seizures in the first minutes after sound exposure." | same surface — Results, "Conditional knock-out mouse model", immediately after the exposure protocol)
3. (The second exposure was at 20 days, at 14 kHz, and its cohort was the four animals that had survived. | "At 20 days, the four surviving mice were exposed to a 14 kHz tone." | same surface — Results, "Conditional knock-out mouse model", two sentences after the three-of-eight result)
4. (At the 20-day exposure every knock-out mouse seized, with wild running, tonic contractions and clonic movements. | "All knock-out mice presented at different times with seizures, consisting as before of wild running followed by tonic contractions and clonic movements, and had uncontrolled sphincter relaxation" | same surface — Results, "Conditional knock-out mouse model", sentence after the 20-day exposure)
5. (Eight wild-type mice of matched age and background were exposed and none seized. | "No wild-type mice of matched age and background ( n = 8) presented with seizures upon 11 or 14 kHz sound exposure." | same surface — Results, "Conditional knock-out mouse model", final sentence of the paragraph, after the mice's death before four weeks)
6. (Seizures were also provoked by stimuli other than sound, including handling. | "Other stimuli such as animal handling also induced seizures on some occasions." | same surface — Results, "Conditional knock-out mouse model", between the 20-day seizure description and the balance-disturbance sentence)
7. (Spontaneous seizures began at about two weeks of age and are reported without a denominator. | "Interestingly, we observed that the Wwox knock-out mice start having a few spontaneous seizures at ∼2 weeks of age." | same surface — Results, "Conditional knock-out mouse model", opening paragraph, before the exposure protocol)
8. (The mice tested are full constitutive knock-outs, because the Cre acts in the oocyte, although the Results section is headed "Conditional knock-out mouse model". | "Cre recombinase in these females is activated in oocytes with Cre protein persisting in the embryo leading to constitutive recombination and producing full knock-out progeny" | same surface — Materials and methods, "Animal experiments", second paragraph)
9. (The sound stimulation was delivered in the home cage from speakers on three sides, and behaviour was video-recorded. | "Exposure to digital 11 and 14 kHz tones (5–10-min exposure) was conducted using speakers adjacent to three sides of the cages. Mice behaviour was monitored and recorded using a video camera." | same surface — Materials and methods, "Animal experiments", second paragraph, after the genotype description)
10. (The exposed animals were 16 to 20 days old and wild-type counterparts were exposed alongside them. | "Wwox knock-out mice and wild-type counterparts (16–20 days of age) were exposed to sound stimulation while in conventional polycarbonate cages." | same surface — Materials and methods, "Animal experiments", second paragraph)
11. (These knock-out mice live at most three to four weeks. | "These knock-out mice are characterized by a short lifespan of only 3 to 4 weeks maximum" | same surface — Results, "Conditional knock-out mouse model", second sentence)
12. (The animals died before four weeks of age of failure to thrive. | "They eventually died before 4 weeks of age from failure to thrive." | same surface — Results, "Conditional knock-out mouse model", after the balance-disturbance sentence)
13. (The abstract states that the knock-out mouse displays both spontaneous and audiogenic seizures, and reads the rat as the prior instance. | "Moreover, we observed that the short-lived Wwox knock-out mouse display spontaneous and audiogenic seizures, a phenotype previously observed in the spontaneous Wwox mutant rat presenting with ataxia and epilepsy" | same surface — Abstract, final sentences)
14. (The authors describe the knock-out mouse's susceptibility as progressive and covering both spontaneous and audiogenic seizures. | "The Wwox knock-out mice show a progressive susceptibility to spontaneous and audiogenic tonic-clonic epilepsy, suggesting a neurodegenerative process." | same surface — Discussion, second paragraph)
15. (The authors state that early death prevented them from testing whether the balance problem is cerebellar. | "However, the severe condition and early death of the Wwox knock-out mice prevented us from testing whether the balance problems were directly related to cerebellar dysfunction or not." | same surface — Discussion, sentence following the progressive-susceptibility sentence)
16. (The rat comparison in this paper is to ataxic gait and audiogenic seizures in homozygous lde rats. | "as homozygous lde rats present with ataxic gait and audiogenic seizures" | same surface — Discussion, the paragraph naming the spontaneous rat mutation lde)
17. (The seizure evidence in Figure 4 is sixteen photographic still frames with no trace, scale bar, scoring annotation or numeric readout. | "Panel A: eight frames of a single white mouse on a wooden surface, labelled t 0, t 2 s, t 4 s, t 6 s, t 7 s, t 9 s, t 11 s, t 42 s. Panel B: eight frames showing two mice, labelled t 0, t 2 s, t 4 s, t 6 s, t 8 s, t 10 s, t 12 s, t 14 s. No trace, scale bar, scoring annotation or numeric readout appears anywhere in the figure." | figure attestation, not a quotation — `files/figures/PMID24369382/renders_s3/fig4_panel_600dpi.png` (4134×4683, sha256 `4af4d463…`), Figure 4 panels A and B, all sixteen frames; recorded as manifest entry 33 of `deepdive_manifests/PMID24369382.json`)

---

## 7 · TRANSFER_BOUNDARY

⚠️ **This result does not reach a WWOX-DEE genotype, and the candidate says so in the record it
proposes.** The animal is a **constitutive biallelic null**; the reference genotype is biallelic
LoF that is **potentially hypomorphic**. `T2` for conserved vulnerability to biallelic loss, **`T3`
for any transfer of an audiogenic phenotype to a human genotype** — which is the transferability
`CLAIM 037` already declares, unchanged by this candidate. Nothing about acoustic provocation in a
mouse licenses any statement about a person, and **nothing here is medical advice**. No therapeutic
statement is added, removed or implied anywhere in this candidate.

## 8 · THERAPEUTIC_EFFECT

**None.** No strategy, score, ranking, caution or monitoring text is touched, and no drug is named.

---

**Falsifiers of this candidate** (what would make it wrong, stated before review):

- if the local HTML surface were shown not to be the deposited article — but its sha256 equals the
  receipt's `source_fingerprint`, the receipt supersedes the earlier reconstruction by name, and the
  passages above were read on that file directly in this session;
- if `CLAIM 037`'s two struck clauses were meant as *"not served by the PMC API route on
  2026-09-22"* rather than as a corpus-level negative — but they say *"not served by any route
  available here"* and *"in any inspectable method"*, and they carry a `PREMISE` tag, which is a
  corpus-level claim;
- if a Plan- or operator-level decision on record restricted `CLAIM 037` to remote-route evidence.
  Searched: the claim record, `CC-20260826-SEIZURE-RECONCILIATION-01`,
  `CC-20260922-SEIZURE-ASCERTAINMENT-01`, `CC-20260826-CLAIM037-01`, the `BATCH_20260922_SEIZURE`
  changelog row and the `BATCH_20260927_001` report. Found none; all three of the latter record the
  contradiction as an open residue.
