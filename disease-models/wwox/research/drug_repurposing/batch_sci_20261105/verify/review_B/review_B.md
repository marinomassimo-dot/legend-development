# Review B — independent review of the conclusions of package `b1_whitematter`

Reviewer `rev-b` (not the producer), 2026-11-05. Scope: the ten numbered statements of the
README Decision section and the five proposal sections of `module_inputs.md`. The verbatim
quotes are being audited blind by another actor and are not re-audited here; where a quote
bears on a conclusion it is named and handed over. Non-canonical review material. Not medical
advice: no dose, schedule, route, titration or clinical preference appears here, for any
species. Nothing outside this directory was written. Zero spend, no account, no registration,
no contact address sent anywhere.

## Verdicts

| | HOLDS | NARROW | REJECT | UNVERIFIABLE |
|---|---|---|---|---|
| Decision statements (10) | 0 | 9 | 1 | 0 |
| `module_inputs.md` §1-§5 (5, with §5 broken into its 5 items) | 2 | 5 | 2 | 0 |

REJECT: statement 3; `module_inputs` §5 item 1 (in part) and §5 item 3.
Everything else narrows. No statement is unverifiable: every headline number recomputes, and
every source named exists and says what the row says it says.

## The six corrections that change what the module should consume

1. **"Four independent cohorts" is three centres at most (statement 1, §1 note on DR-H02-005,
   §5 item 2).** PMID 36601084 (172 children) and PMID 34786694 (77 children) come from the
   same department of one hospital, share eight authors including the senior author, and cover
   overlapping years. The package's own row B1-13 says so ("the same centre published the
   larger cohort of B1-01") and the Decision line contradicts its own table. The same defect
   hits statement 6: PMID 28230253 and PMID 39570186 are both single-centre cohorts from one
   division with the same senior author (2017, n=104; 2024, n=108), so the two hormonal-therapy
   signals are one centre, not two.

2. **Statement 3 inverts the human record (REJECT).** The two "full-text human cohorts" are one
   risk-factor cohort whose age range is restricted to infancy, and one diffusion study that
   never tested age or duration as risk factors at all — its age and duration figures are
   baseline comparisons between groups of about eleven, i.e. an unreported test read as a test
   that found nothing. Four independent human sources with a positive age signal were not read,
   three of them returned by the package's own query Q3: PMID 19054414 (controlled, blinded,
   ten sites: the abnormality in 22 percent of exposed against 4 percent of naive infants, and
   "there was no statistically significant difference in the incidence or prevalence of
   prespecified MRI abnormalities" in children aged 2-16 and adults), PMID 18783433 ("Young age
   and relatively high dose appear to be risk factors"; median age 11 months in those with the
   finding against 5 years in those without, with *shorter* exposure in the former),
   PMID 20384718 ("Younger infants (<=12 months) and those with cryptogenic IS were more likely
   to develop abnormal signal changes"), PMID 19258289 ("likely to be age-dependent and
   time-dependent because it has never been observed in adult patients"). The "pooled review"
   that statement 3 and §5 item 3 both cite has no row, no receipt and no identifier anywhere
   in the package.

3. **The sibling null is unreachable, not absent (statement 7).** Query Q8 was conjunctive with
   myelin vocabulary and restricted to title and abstract; a histopathology endpoint inside a
   toxicology package is normally in neither. A plain identifier search returns 24 CPP-115 and
   OV329 records, of which the package saw six. Among the unseen, the open-access EILAT XVIII
   progress report (PMID 42470358) states in its OV329 toxicology section that "The results of
   standard GLP toxicology studies of OV329 have been described in the EILAT XVI progress
   report" — so a standard toxicology package for a sibling exists; EILAT XVI (PMID 35946083)
   and EILAT XVII (PMID 39008349) are subscription-only, so its content is blocked, not
   missing. No myelin, white-matter, vacuolation or intramyelinic word occurs anywhere in
   EILAT XVIII; its one new sibling safety datum is a mouse tissue-distribution comparison in
   which OV329 was below the assay's limit of quantitation in brain, eyeball and retina while
   vigabatrin accumulated (retina-to-plasma concentration ratio about 4.3).

4. **The GABA axis is unsigned, and a molecule-specific rival exists (statement 8, §2
   mechanism, §3 `do_not_assume`).** The literature that actually measures GABA on the
   oligodendrocyte lineage was never searched and is two-sided. In the package's direction, and
   a far better source than its 1989 explant culture: PMID 27796063, where "endogenously
   released GABA, acting on GABA[A] receptors, greatly reduces the number of oligodendrocyte
   lineage cells", with less myelination. Against it: PMID 31349008, where "chronic treatment
   with GABA and baclofen, specific GABA[B] receptor agonist, accelerates OPC differentiation",
   with more myelin segments and more myelin basic protein; PMID 35980256 (a GABA-B agonist
   promotes remyelination); PMID 39682762 (removing GABA-B from oligodendrocyte precursors
   protects against demyelination). Raising extracellular GABA engages both receptor classes,
   whose documented effects on this lineage have opposite signs. Separately, vigabatrin
   depletes taurine and inhibits taurine transport, and taurine deficiency is reported as a
   cause of its retinal phototoxicity, including in neonatal rats (PMIDs 19194884, 20132888,
   25062867) — a documented molecule-specific mechanism for the better-characterised tissue
   lesion, which is the direct rival to a class reading.

5. **The harm tag does not exist as a field, and statement 9 pre-empts a registered
   condition.** No `harm tag` or `safety_flag` appears in any of the 39 packet cards. The
   module carries this as `p4_card.status` (H02 is `controversial`), as counter-evidence rows
   ordered safety-first, and above all as *computed* positions F1-F3 / C1-C3 / P1-P3, where C3
   is "harm or null from outside WWOX" — printed by `repurposing_view.py positions` from the
   card's rows, not authored. `undetermined` is in no closed vocabulary: card `direction` is
   {INCREASE, DECREASE, UNKNOWN, NO_CHANGE} across all cards, needs `direction` is {up, down,
   restore, modulate, uncertain}. And `view/work_order.json`, entry NEED-MYELINATION, already
   registered the condition: "its presence would make the sibling tag a card-level C3 for
   vigabatrin as well" — the vigabatrin C3 was pre-registered as following from *demonstrated*
   added injury in a Wwox-deficient model, not from outside-WWOX human cohorts. Statement 9
   asserts it now, from those cohorts. Its phrase "a retina-sparing sibling" also asserts what
   the card explicitly guards against ("the retinal advantage rests on an ERG in rats";
   "'gentler on the retina' must not be read as 'gentler on myelin'").

6. **"The human literature shows those three do not recover together" is false (statement 10,
   §4).** No human source in the package measures vacuolation or myelin content; the README
   says so itself under "What is not established". The separation of the three readouts comes
   from two abstract-level rat studies. The same paragraph in §4 states the mis-attribution and
   then attributes two of its three readouts to rats in the next clause.

## Sources the producer missed, and what each one does

| PMID | What it is | Why it matters here |
|---|---|---|
| 19054414 | 205 infants aged <=24 months, 332 images, ten sites, two neuroradiologists blinded to treatment group, against 668 children aged 2-16 and adults with 2,074 images | The only controlled cross-age human design in this literature, and the primary source of the label's 22 against 4 percent. Positive in infants, null in children and adults: this is the human age evidence statement 3 denies exists. Also reports resolution "even in subjects who remained on vigabatrin therapy" |
| 18783433 | 23 exposed, 7 of 22 with the finding after excluding the first-detected one, compared with 56 unexposed with infantile spasms | Tests age *and* duration directly: younger at the examination, shorter exposure, higher peak amount. Breaks statement 3 and independently supports the package's own "intensity not accumulation" transfer condition |
| 20384718 | 107 children, 95 exposed, 25 of 81 (30.9 percent) with the finding, 12 unexposed all normal, follow-up in 15 | A fourth independent rate, an unexposed comparator, an age signal (<=12 months), a cryptogenic-aetiology signal, and reversal in one child without stopping |
| 19258289 | 22 exposed infants, 34 examinations, blinded retrospective review | Peak of the finding three to six months after start; independent of duration and epilepsy type; explicit age-dependence argument |
| 38092645 | Narrative review of the abnormality and its differential diagnosis | Rates of 22-32 percent and risk factors "cryptogenic infantile spasms, age <12 months old, high dosage, and possible concomitant hormonal therapy". The nearest match to the "pooled review" statement 3 cites with no row; by the brief it is a pointer, not a unit |
| 42470358 | EILAT XVIII progress report, open access, OV329 section | Says standard GLP toxicology of OV329 is reported in EILAT XVI; carries a new mouse brain/eye/retina distribution comparison. Turns statement 7 from an absence into a blocked route |
| 35946083, 39008349 | EILAT XVI and XVII progress reports | Where the sibling toxicology is actually described. Both subscription-only in Europe PMC: record as blocked |
| 27796063 | Endogenous GABA, GABA-A, developing cortex slices | Supports the package's direction better than anything it used, and relocates the axis to a receptor subtype |
| 31349008, 35980256, 39682762 | GABA-B on oligodendrocyte precursors and remyelination | The opposite sign. Together with the row above, these make "raised GABA" an unsigned axis rather than a harm axis |
| 19194884, 20132888, 25062867 | Taurine depletion and taurine-transport inhibition by vigabatrin; neonatal rats | A molecule-specific rival mechanism for the drug's other tissue lesion, which is what a class reading has to beat |

## Statement by statement

**S1 — NARROW.** Every rate recomputes: 38/172 = 22.1, 25/77 = 32.5, 18/64 = 28.1,
34/76 = 44.7 percent. Three defects. (a) Independence: see correction 1. (b) Denominator: all
four are rates among children imaged during exposure, and for PMID 40527948 the abstract
itself gives the exposed denominator — 76 of the treated cohort (57.6 percent) were imaged, so
the rate per exposed child is about 26 percent (34 of about 132), not 44.7; for PMID 36601084
the package's own breaker records 143 exposed-but-unimaged exclusions. (c) The statement
carries no unexposed comparator, although the package's B1-35 holds one (7 of 52) and
PMID 19054414 holds another (4 percent of naive infants) — and the whole point of the WWOX
transfer is that a count without a denominator is not an excess.

**S2 — NARROW.** The four figures check (25/38 = 65.8 percent; 25 of 44; 13 of 13 in B1-35;
the optic-nerve metric in B1-18). One correction with a consequence: resolution is reported
both after stopping *and* during continued exposure (PMID 19054414, "The majority of these MRI
abnormalities resolved, even in subjects who remained on vigabatrin therapy"; one child in
PMID 20384718 reversed without cessation). The package builds its exposure-window logic on
reversal being contingent on stopping (B1-14 transfer condition), and that contingency is not
what the literature shows. Two wording notes: the "13 of 13" is carried from a held manifest
whose quoted sentence is about a different figure (7 of 52) — handed to the quote auditor —
and "a quantitative white-matter metric" should name the tract, since the optic nerve is also
the retinotoxicity target, as B1-18's own breaker says.

**S3 — REJECT.** See correction 2. The verb "does not survive a full-text human reading" uses
depth as a trump card where the deeper source cannot test the question (restricted age range)
and the second "cohort" did not test it; and it suppresses a positive human record of four
independent sources, three of them inside the package's own query output. The animal half of
the sentence ("In animals the window dependence rests on abstract-level rat and dog studies
only") is accurate and should be kept.

**S4 — NARROW.** Both rat abstracts say what the row says. But PMID 10840396 also reports that
after the drug-free period "the T2 relaxation time remained elevated in the hypothalamus" —
the one *quantitative* imaging measure did not normalise. "Imaging and vacuolation resolved"
therefore overstates the imaging half, and the architecture built on "imaging resolves, tissue
does not" (S10, transfer condition 4, §4) inherits it. Both rows are abstract-level, so
"endpoint-specific" is an abstract-level reading of two studies.

**S5 — NARROW.** Three narrowings. (a) An absence of a significant difference in a univariate
list, in 76 children, with no stated power and myelination graded from routine reports, is
"not demonstrated", not "negative"; the package's own B1-09 breaker says exactly this and the
Decision line drops it. (b) "The one human test" ignores the package's own B1-19
(PMID 42033488), a POLR2A developmental and epileptic encephalopathy in which the pattern
appeared on a baseline carrying delayed myelination and callosal hypoplasia — the closest
human analogue of the WWOX baseline that exists, and in the opposite direction. One case is
not a test, so the right phrase is "the only cohort-level test". (c) In that same cohort 14 of
34 cases were originally reported as normal; under-recognition bears asymmetrically on a
baseline-abnormal subgroup, which is the package's own B1-07/B1-10 argument and is not carried
into the statement that uses the null.

**S6 — NARROW.** The symptomatic-form association is real but comes from one centre twice (see
correction 1). "But not with the imaging finding itself" is contradicted inside the package:
B1-11 records, from PMID 42735667, "concomitant prednisolone therapy (OR 4.07, 95% CI
1.22-17.3) were associated with VABAM in univariable analyses". The record is split two
negative to one positive, not clean.

**S7 — NARROW.** See correction 3. Two further bounds: the OV329 texts were read at
keyword depth and their own quote says the histology is "detailed in the Supplement", which
was not retrieved, so even the main-text null is bounded by that; and B1-32's statement is a
2012 statement, as its own breaker says.

**S8 — NARROW.** See correction 4. Four further weaknesses in the four pieces: the explant
culture produced *no* intramyelinic oedema from either agent, so it did not reproduce the
lesion at issue; the cerebrospinal GABA comparison is two cases against eleven, both preterm
with post-haemorrhagic hydrocephalus, so baseline injury and GABA are not separable (the row
says so, the statement says "the children with the abnormality"); in the succinic
semialdehyde dehydrogenase cohort gamma-hydroxybutyrate correlates as strongly as GABA, so
the agent is unidentified; and GABA-aminotransferase deficiency is complete lifelong loss of
an enzyme in a lethal multisystem disorder. The statement also omits the package's own
counter-row B1-29, which is a direct in-vivo dissociation in the opposite direction.

**S9 — NARROW.** See correction 5. Answering the question put to this review: it is neither a
research-priority tag the module already uses nor clinical advice — it is a request for a
field that does not exist, in two words that are in no closed vocabulary, and it pre-empts the
one condition the work order registered in advance. Written in the module's own idiom the
substance survives: add the counter-evidence rows, let the position follow, and keep the
sibling at UNKNOWN because the endpoint is unmeasured rather than clean.

**S10 — NARROW.** See correction 6. The design itself is sound and is the package's best
contribution; only the justifying clause and its citation are wrong — B1-07 and B1-10 support
the detection-bias arm only. Two additions the evidence now supports: the imaging readout
should include a quantitative measure, since the qualitative images normalised in
PMID 10840396 while regional T2 did not; and the receptor-subtype conflict (correction 4)
gives the series a second discriminating arm that the current text does not have.

## `module_inputs.md`

**§1, seventeen new `drug_assertions` — NARROW.** What is right: both existing ids named do
exist and are correctly characterised (DR-H02-005 is the label row, `brain_MRI_abnormality`,
`queried_not_full_read`, `EXTERNAL_DATABASE_RECORD`; DR-H02-009 is the single sibling child
case, `epileptic_spasms`, `partial_fulltext_read`), both receipt ids named exist in
`receipts/`, and the field list matches the packet. What is wrong:

* `direction` is a closed set in the consumer — {INCREASE, DECREASE, UNKNOWN, NO_CHANGE} over
  all 39 packet cards. The proposal introduces `UNDETERMINED` (DR-H02-013, -014),
  `NOT_MEASURED` (-026, -027) and six compound strings (-016, -017, -019, -020, -022, -024,
  -025). Map the first two to UNKNOWN and move every qualification into `note`.
* DR-H02-025 is a sign inversion waiting to happen: "INCREASE for GABA, DECREASE for
  vigabatrin" on target `CNS_myelination`, from a clinical disease-severity score in an
  autoimmune model. Read literally it says vigabatrin lowers myelination, the opposite of the
  source. It also breaks the card's own convention that signs compare only where target,
  endpoint and every context dimension match.
* DR-H02-015 proposes NO_CHANGE from a non-significant univariate comparison read at abstract
  level: UNKNOWN. DR-H02-016 proposes INCREASE from a distribution its authors call
  hypothesis-generating: UNKNOWN.
* DR-H02-019 files optic-nerve fractional anisotropy under `CNS_myelination`: a diffusion
  metric in the retinotoxicity target tract read as myelination.
* DR-H02-028 and -029 are not drug assertions. Two genetic conditions with no drug exposure do
  not belong in `drug_assertions`; §2 already proposes them in `mechanism`, which is their
  place.
* The DR-H02-005 note inherits the independence error of S1.

**§2, text fields — NARROW.** Every field named exists (`p4_card.mechanism`, top-level
`evidence_against`, top-level `not_known`, `p4_card.status` = `controversial`,
`p4_card.question_history`). Three repairs: the harm-tag paragraph (correction 5); the
mechanism paragraph must carry the receptor-subtype conflict and the taurine rival or it gives
the card a sign the literature does not give; and part of the `evidence_against` addition
restates what the card already holds (the hormonal rival, the "gentler on the retina must not
be read as gentler on myelin" caution, the lethal highest level in the rat spasm model),
against the brief's "cite, do not repeat".

**§3, `needs/needs.json` NEED-MYELINATION — NARROW.** Shapes are right: `counter_evidence` is
a list of free-text strings, `do_not_assume` is a string, and leaving `observed` untouched is
correct because no WWOX source was read. Two repairs: the `counter_evidence` text carries
"did not predispose" as a test (S5), and `do_not_assume` asserts a GABA-raising exposure as a
candidate myelin stressor without the opposite-sign literature, which is the one place where
an unsigned axis would become a signed premise in a canonical-adjacent file.

**§4, `view/work_order.json` NEED-MYELINATION — NARROW.** Fields exist. The `data` replacement
carries the mis-attribution of correction 6. The `would_change` replacement is described as
"unchanged in substance" while inserting "WWOX-specific" into the registered sentence "a
position without harm rows" — that is a substantive edit to a pre-registered line and should
be flagged as such, not as a non-change. The `feasibility` addition (reading a WWOX count
against published aetiology strata rather than a pooled rate) is the single most useful
proposal in the package and should be kept as written.

**§5 item 1 — REJECT in part.** "One with a GABA-pathway gene (B1-20)" is wrong: B1-20 is
PMID 42355787, a PCDH19-clustering epilepsy with a concurrent systemic carnitine deficiency.
PCDH19 is not a GABA-pathway gene and the row claims nothing of the kind; the GABA-receptor
subunit remark belongs to a different source (PMID 42735667, row B1-11). The rest of item 1
follows from B1-19 and is the package's most transfer-relevant finding.

**§5 item 2 — NARROW.** Inherits "four independent exposed cohorts". It should also carry the
two unexposed comparators (7 of 52 in B1-35; 4 percent of naive infants in PMID 19054414),
since the claim being qualified is precisely that a WWOX count without a denominator is not an
excess.

**§5 item 3 — REJECT.** It rests entirely on S3. A species split is the right shape, but the
human half is supported, not contested: one restricted-range null against four independent
positive sources including a controlled cross-age design.

**§5 items 4 and 5 — HOLDS.** No new claim id, and no evidence added on whether raising GABA
helps or harms seizure control. Both correct and correctly abstained.

## The consequences table of BRIEF_B1.md, as pre-registered

* Row 1 (risk in the first two years, mostly reversible) — **applied in substance, in the wrong
  file.** The pre-registered action was a transfer condition on card H02; the package put it in
  its own README prose and in the needs proposal, and §2 proposes no transfer condition for
  H02.
* Row 2 (rodent or dog start-age series confirmed at full text) — **antecedent never met, and
  an unregistered opposite action taken.** Q15 was blocked, so full-text confirmation does not
  exist. The table gave no action for that case; the pre-registered default was to keep the
  sentence "with its sources and its species limits". The package instead downgraded the
  premise (§5 item 3) on a human reading this review rejects. This is the largest deviation in
  the package.
* Row 3 (hormonal therapy not separable) — **applied**, with the A1 half correctly marked
  pending.
* Row 4 (nothing on a myelin-deficient baseline) — **applied**, and the bounded null is
  honest, though the sibling null of row B1-34 is not (correction 3).

Depth honesty: "nine at full text" in the README is the strongest reading of its own depths.
Against the brief's "8 to 12 sources read at full text (design and results)" the deliverable is
six partial full-text readings plus three keyword-directed inspections. The counts are stated
transparently in the same paragraph, so this is a wording narrowing, not a misreport. Receipt
arithmetic checks: 6 + 3 + 18 = 27 files in `receipts/INDEX.tsv`, matching the README.

## What I could not verify

* The content of the sibling toxicology summaries (PMID 35946083, PMID 39008349): subscription
  only, no open route, no contact address used. The sibling white-matter question is therefore
  open-by-blockage and should be recorded that way.
* The "13 of 13" resolution figure and the "normalising within three months" phrasing of
  B1-18: one is carried from another actor's held manifest, the other sits in a full text I did
  not open for this review. Both are handed to the quote auditor.
* Whether the two children of the WWOX report are inside the 64-child aetiology cohort. They
  cannot be excluded: PMID 41442931 and PMID 42735667 share the first author, the
  neuroradiologist and a further co-author at one institution, and the cohort's intake window
  (August 2019 to August 2025) precedes the report. If they are the same children, B1-11's
  genetic-aetiology signal is not independent corroboration of the WWOX observation but partly
  the same observation, and §1's DR-H02-016 and §5 item 1 would both need that caveat. This is
  a question for package A1, which owns the WWOX reports.

## Queries run for this review

| id | route | string | run (UTC) | hits | what it decided |
|---|---|---|---|---|---|
| RB1 | PubMed metadata | PMIDs 36601084, 34786694, 40527948, 42735667, 40670421, 10840396 | 2026-11-05T23:04Z | 6 | centre and author identity (S1, S6); the design of the diffusion study (S3); the exposed denominator of 76/57.6 percent (S1); the hypothalamic T2 sentence (S4); the prednisolone odds ratio (S6) |
| RB2 | PubMed search | `vigabatrin AND (MRI OR "magnetic resonance") AND (systematic review[pt] OR meta-analysis[pt] OR review[pt])` | 2026-11-05T23:05Z | 35 | the nearest match to the uncited "pooled review" (PMID 38092645) |
| RB3 | PubMed search | `"CPP-115"[All Fields] OR "CPP115"[All Fields] OR "OV329"[All Fields] OR "OV-329"[All Fields]` | 2026-11-05T23:07Z | 24 | the eighteen sibling records the package's conjunctive query could not see (S7) |
| RB4 | PubMed metadata + PMC full text | PMIDs 42470358, 41711325, 41279952, 39793055, 39008349, 36826597, 35946083, 35293728, 33735567; full text of PMC13675778 | 2026-11-05T23:09Z | 9 + 1 | the OV329 toxicology pointer and the distribution comparison; no myelin vocabulary anywhere in EILAT XVIII (S7) |
| RB5 | Europe PMC REST | `EXT_ID:35946083`, `EXT_ID:39008349` with resultType=core | 2026-11-05T23:12Z | 2 | both subscription only: the sibling toxicology is blocked, not absent (S7) |
| RB6 | PubMed search | `vigabatrin[Title] AND (abnormalities[Title] OR imaging[Title] OR MRI[Title] OR "magnetic resonance"[Title] OR toxicity[Title] OR neurotoxicity[Title])`, 2005-2018 | 2026-11-05T23:13Z | 37 | the four missed primary human series (S3) |
| RB7 | PubMed metadata | PMIDs 19054414, 18783433, 20384718, 19258289, 23199677 | 2026-11-05T23:15Z | 5 | the human age evidence and the resolution-under-exposure fact (S2, S3) |
| RB8 | PubMed search | `(GABA[tiab] OR "GABAA receptor"[tiab] OR "GABA-A"[tiab]) AND ("oligodendrocyte precursor"[tiab] OR OPC[tiab] OR "oligodendrocyte progenitor"[tiab]) AND (myelination[tiab] OR differentiation[tiab] OR "white matter"[tiab])` | 2026-11-05T23:17Z | 30 | the two-sided GABA-to-myelination literature (S8) |
| RB9 | PubMed search | `vigabatrin[tiab] AND (taurine[tiab] OR "taurine deficiency"[tiab])` | 2026-11-05T23:17Z | 32 | the molecule-specific taurine rival (S8) |
| RB10 | PubMed metadata | PMIDs 42033488, 42355787, 27796063, 31349008, 39570186, 41442931 | 2026-11-05T23:19Z | 6 | PCDH19 against "a GABA-pathway gene" (§5 item 1); the GABA receptor-subtype signs (S8); one-centre identity of the hormonal signals (S6); the shared origin of the WWOX report and the aetiology cohort |

Bibliographic metadata and abstracts in this review come from PubMed. No full text was saved
inside the repository; the one full text retrieved (PMC13675778) was read through the PMC tool
and left in the session's tool-results area outside the repository.
