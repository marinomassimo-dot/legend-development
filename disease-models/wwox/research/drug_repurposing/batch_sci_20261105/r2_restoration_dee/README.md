# R2: restoration after onset in DEE and hypomyelination models, and human timing precedents

Scientist `sb-r2`, challenge `CH-SB-POSTONSET-RESTORATION` part 2, task `ORCH-SCIBATCH-DR-20261105`.
First issue 2026-11-05; **revised 2026-11-06 after a blind locator audit and an independent review** (see
`RESPONSE.md` for the finding-by-finding answer). Non-canonical research material. **Not medical advice**: no dose,
schedule, administration route, preparation or clinical preference appears here, for any species; exposure is
described qualitatively only. Public edition — the subject is the WWOX-DEE reference genotype class and no
individual-level record is used. Nothing outside this directory was edited; receipts are staged drafts, not recorded.
Status vocabulary is the one defined in `BRIEF_R1.md` and in `rescue_window_it6_20261029.md`.

Table: `evidence_r2.tsv`, 78 rows over 17 sources. Queries: `queries.tsv`, 32 entries. Proposals: `module_inputs.md`
(contributions only). Correction record: `RESPONSE.md`.

**What the correction round changed, in one paragraph.** The blind audit checked 64 locators and returned 55 supported,
7 overshoot, 1 not-in-source and 1 unverifiable; all nine are fixed below and in the table. The review found four
membership errors in the matrix of section 1 and one headline — a pre-onset survival benefit — asserted in three
decision lines with no row behind it; the matrix is now computed from the table and the missing row is R66. The
largest change is scientific, not clerical: **my myelin null was a search artefact.** My queries were anchored on
hypomyelination, Pelizaeus, jimpy, shiverer, Plp1 and Mbp, so no string could reach an enzyme-deficiency, connexin,
tubulin or astrocyte-transporter leukodystrophy. Five sources in those families were read in this round, and one of
them reverses a structural white-matter abnormality seven months after a documented onset. The headline "myelin after
onset has never been tested" was wrong as stated; the defensible null is narrower and is given in line 4.

**Depth, stated once and applied everywhere.** Ten sources were read beyond the abstract and seven at abstract level
only. **No figure image was inspected in any source**, so no row is labelled `full_text`; figures are recorded as
`captions_only` (or `not_read`) in the receipts. For nine sources the prose read covers abstract, results and
discussion, with introduction, methods and limitations as recorded per receipt; supplements were not opened anywhere.
PMID 28100454 was read through the open article page in four question-directed passes because the structured-text
routes refused it. The staged receipts in `receipts/` carry the section-by-section truth and all ten pass
`staged_receipt_check.py --check-doi`.

---

## 0 · Decision (10 lines)

1. **DATO.** Post-onset restoration of a DEE gene recovered spontaneous and provoked seizures, death from seizures,
   working memory and spatial learning in a conditional Dravet model treated after manifest seizures at P30, and
   abolished established seizures again in adults ten weeks after onset with a within-animal pre-treatment recording
   (R01-R04, R09; PMID 35013317). Within that same arm sociability only trended (R05), interneuron excitability
   overshot rather than normalised (R06, R07), and two of nine treated animals died after the thermal challenge with
   incompletely restored protein (R11): the recovery is complete at the level of the phenotype and partial at the level
   of the cellular and social measures. The adult arm carries a seizure endpoint only. **"Fully" was the authors'
   phenotype-level word and is withdrawn as an endpoint-by-endpoint grade.**
2. **DATO.** A glial endpoint — reactive astrogliosis, by cell counts, morphology and transcripts — also recovered
   after onset in that model (R08). No myelin endpoint exists in it.
3. **DATO.** A second DEE model treated while symptomatic, about three weeks after seizure onset, recovered survival
   and improved seizure frequency, interictal spikes and a composite welfare-cognitive endpoint **partially**
   (R15-R17; PMID 36173683). It silences a mutant channel transcript rather than replacing a missing protein, so it is
   a timing precedent and not a replacement one.
4. **DATO, corrected.** The two hypomyelination precedents **reachable by my queries** both treated before onset, and
   in both the structural myelin endpoint moved least — about 10 percent of wild type with reduced compaction in one
   (R25), below wild type in the other (R54) — while oligodendrocyte number, apoptosis, glia, respiration, locomotion
   and lifespan moved far more (R26, R29, R55, R57); both author groups state that treating later was not done (R30,
   R59). **My wider null was a search artefact and is withdrawn.** Searching enzyme, connexin, tubulin and
   astrocyte-transporter leukodystrophies reaches a class that is not empty: an astrocyte-directed vector given seven
   months after a documented vacuolation onset **fully reversed** cerebellar white-matter vacuolation and normalised
   water content (R67, R68; PMID 40051162); a systemic administration as late as P20 in a null that dies within a
   month rescued lethality and globally improved myelination (R72, R73); and enzyme re-expression improved or
   normalised myelin-lineage markers with the effect blunted in old animals (R74). **The defensible null is narrower:
   no source in any of these families measured myelin sheath morphometry after onset** — no electron microscopy, no
   g-ratio — and all three correct a glial or metabolic lesion, not a neuron-driven one (R69).
5. **DATO.** A brain-directed AAV replacing a missing protein in a short-lived null — the closest structural analogue
   of the WWOX design — extended lifespan, reduced seizure severity without changing time to first seizure, and fully
   restored parvalbumin interneuron and pyramidal excitability at P2 (R66, R40, R41), while at P10, at twice the
   exposure, all eight treated null animals died in the usual window with the restoration achieved never measured
   (R37; PMID 39847501).
6. **INFERENZA, corrected.** That cliff is not evidence of biological irreversibility. The authors attribute it to
   transgene level and distribution, and report — **citing other studies and their own unpublished work, not a finding
   of this paper** — that rodent CNS expression falls sharply with injection after the first postnatal days (R38, R39).
   That generalisation is specific to route, capsid and promoter: a single systemic administration as late as P20
   rescued lethality in another short-lived null (R72), and a systemic vector at four to five weeks in a null already
   symptomatic produced transduction of a few percent of neurons and still a measurable survival benefit (R77). A
   perinatal-only window in a rodent is therefore partly a property of **the modality as delivered**.
7. **DATO.** In the same source, pre-onset treatment extended survival and restored interneuron excitability while
   **growth was not rescued at all** (R66, R41, R42). Survival is not a proxy for growth.
8. **DATO, narrowed.** Human: stage at treatment is **associated** with outcome in both precedents, and in neither is
   it separated from the eligibility rules that follow from stage. In SMA, near-normal milestones were reached
   pre-symptomatically and much poorer ones in the symptomatic trials of the same intervention — a **cross-trial
   secondary statement** inside the pre-symptomatic report, flagged by its own authors as limited by differing design,
   endpoints and eligibility (R50, R52). In MLD, within one report, the composite white-matter and atrophy score was
   arrested at a worse plateau when treatment followed symptoms and children entering rapid progression did not
   benefit at all (R46, R47). "Dominates" is withdrawn.
9. **INFERENZA, corrected.** The split is not prevented-versus-recovered by endpoint class alone. Endpoints sustained
   by ongoing dysfunction — seizures, network firing, astrogliosis, the **cortical** transcriptome — recovered after
   onset in two channel or channel-transcript models, with interneuron excitability moving but overshooting. Endpoints
   that are accumulated structure were **not measured after onset at the level of the myelin sheath in any model**: the
   only post-onset structural readouts on record are a composite human imaging score that stabilised at a
   stage-dependent plateau (R47) and a rodent white-matter vacuolation and water-content endpoint that was fully
   reversed in a glial-gene lesion (R67, R68). Endpoints with a peripheral or developmental-growth component recovered
   least, failing even pre-onset (R42).
10. **IPOTESI.** For `INV-01`: power the added arm on seizure and network endpoints, carry a within-animal
    pre-treatment recording, a treated wild-type arm and a quantified myelin endpoint scored as *arrest versus
    reversal* — and **measure the restoration actually achieved at the age of treatment**, or a null result will be
    uninterpretable in exactly the way R37 is. Three independent sources now support that last requirement: a stated
    transduction threshold (R65), a full structural rescue under only about a fifth regional coverage (R70), and a
    survival benefit at a few percent of neurons after onset (R77).

---

## 1 · Matrix: endpoint class by restoration timing

**Recomputed from `evidence_r2.tsv` on 2026-11-06**, after the review found four membership errors in the hand-written
version. Cells count **distinct sources**, not rows; a source appears in several cells. Columns are built from
`age_at_restoration_vs_onset` and `outcome` only — not from `status_vocab` — which is the construction the combined
matrix of both R packages uses (`verify/review_R/review_R.md` section 3), because those two columns use the same closed
value sets in both packages while the status vocabulary is applied differently in each. `at_onset` is shown separately
because the audit showed one row previously placed there is in fact a pre-onset arm. Rows whose age is `not_stated`
cannot enter a timing cell and are listed in their own column.

This is a tabulation, not a meta-analysis. The models differ in gene, lesion class, species and life span; the
published literature selects for success; failures are reported inside otherwise positive papers, so the negative cells
are under-counted; and three of the seventeen sources exist *because* a post-onset arm could not be run.

| Endpoint class | Pre-onset | At onset | Post-onset | Age not stated |
|---|---|---|---|---|
| Survival | 7 studies; full in 3, partial in 5, none in 1 | 1 study; none | **4 studies; full in 1 (35013317), partial in 3 (35013317, 36173683, 23011033)** | 1 study, full (23817205) |
| Seizure or network hyperexcitability | 3 studies; all partial | — | **2 studies; full in 1 (35013317), partial in 2 (35013317, 36173683)** | — |
| Motor | 5 studies; partial in 5, full in 1 | — | **4 studies; full in 1 (40051162), partial in 1 (35715566), none in 1 (35065785), not measured in 1 (35013317)** | — |
| Cognition and behaviour | — | — | **2 studies; full in 1 (35013317), partial in 2 (35013317, 36173683)** | 3 studies (35065785, 36173683, 41883162) |
| Neuronal structure | 2 studies; full in 1 (39847501), partial in 1 (32610343) | — | **1 study (35013317); full on the fast-spiking measure, partial overall because it overshot** | 1 study (31607539) |
| Myelin and glia | 4 studies; full in 1 (32610343 oligodendrocyte number), partial in 3, not measured in 3 | — | **3 studies; full in 2 (35013317 astrogliosis, 40051162 vacuolation and water), partial in 2 (40051162 diffusion, 35065785 imaging score)** | 2 studies, partial (23817205, 37149081) |
| Systemic and metabolic | 4 studies; full in 1 (32610343 respiration), partial in 1, none in 1 (39847501 growth), not measured in 2 | — | 1 study; not measured | — |
| Molecular state (bulk transcriptome) | — | — | **1 study (35013317); partial** | — |

**Reading, corrected.** Seizure and network endpoints remain the class with the cleanest post-onset recovery, but both
clean cases are channel or channel-transcript lesions, and WWOX is neither — so this is the least transferable part of
the package, and for a non-channel gene the external record is **split rather than negative** (see `RESPONSE.md` on
cross-package point (a)). The post-onset myelin-and-glia cell is **no longer empty**: it holds a full reversal of a
white-matter vacuolation and water-content endpoint in a glial-gene lesion. What remains empty, across every bounded
search run by me and by the reviewer, is **myelin sheath morphometry after onset** — and **interneuron number at any
timing**. Systemic growth is still the endpoint that failed even pre-onset in the source closest to the WWOX design.

## 2 · Evidence by theme

### 2.1 Post-onset restoration that worked, and the quality of the design (R01-R14, PMID 35013317)

A conditional Dravet knock-in whose silenced allele is restored on demand. Symptoms are stated to begin P18-P24;
restoration at P30 was given to animals **selected for already seizing during handling**, and the adult arm at P90
recorded two weeks of video-EEG in each animal **before** treatment, randomised after that baseline. Recovered: death
from seizures (R01), spontaneous seizures on two weeks of recording, 0 of 9 against 7 of 8 (R02), thermally induced
seizures (R03), working memory and spatial learning (R04), astrogliosis and inflammation transcripts (R08), the
cortical transcriptome entirely (R13), and in the adult arm the established seizures of animals that had been seizing
for about ten weeks (R09).

Three qualifications that matter more than the headline. First, interneuron excitability did **not** normalise: fast-
spiking cells recovered but overshot, non-fast-spiking cells became more excitable than both other groups, and the
authors write that recovery was complete at the level of the phenotype while the cellular measure was not (R06, R07).
The whole-animal benefit therefore came from *an alternative* excitation-inhibition balance, not from repair of the
cellular deficit. Second, sociability only trended toward recovery (R05). Third, two of nine treated animals died
after the thermal challenge, and their protein level was found to be incompletely restored (R11) — a transduction
threshold, discovered post hoc. In the adult arm the protein reached normal levels in cortex and hippocampus but not
cerebellum or striatum, and the seizure endpoint recovered anyway (R10).

The paper's own Introduction records why this mattered: earlier upregulation approaches delivered at later stages had
produced only mild amelioration, and the field could not tell insufficient restoration from irreversible damage (R14).
That is the same ambiguity the WWOX record now faces, and this source resolved it by making restoration efficient.

### 2.2 Post-onset correction in a second DEE model (R15-R23, PMID 36173683)

A homozygous gain-of-function model, seizures from P18, treated while symptomatic at P40 — the most advanced post-onset
arm in this set. Survival, seizure frequency and interictal spikes, and nest building (a composite of social, cognitive
and motor performance) all improved against a non-hybridizing control in the same genotype (R15-R17). Re-treatment
after relapse in neonatally treated animals worked again (R23), so the benefit is maintenance-dependent rather than a
single switch. The neonatal arm of the same model gives the pre-onset comparison in the same laboratory (R21, R22), and
growth stayed below wild type even there (R21).

Two counters. The intervention has its own behavioural signature: open-arm time fell in every treated group **including
treated wild type** (R18), and novel-arm time fell in treated wild type (R19). Without that wild-type arm both would
have been scored as rescues. And the authors state that seizures prevented a within-animal before-and-after behavioural
comparison (R20) — the same obstacle the WWOX design has, solved in 2.1 by taking a *physiological* rather than a
behavioural baseline.

This source corrects an expression excess, not a missing protein. It is a timing precedent, not a replacement one.

### 2.3 The myelin question: both precedents are pre-onset, and myelin moved least (R24-R31, R54-R59)

Two independent hypomyelination models, two different modalities, same shape of answer.

In the PMD model, a single administration at birth raised lifespan about eleven to twelve fold, fully restored
oligodendrocyte number (81-101 percent of control), normalised respiratory control and restored open-field locomotion
to wild-type levels — yet myelinated axons reached only **about 10 percent** of control at three weeks and persisted at
eight months with less compaction, conduction velocity reached about 17 percent, and rotarod reached at most 36 percent
(R24-R29). Survival in that model was driven by brainstem respiratory control, not by global myelin (R29): the
mechanism of benefit was not the structural endpoint. The germline arm of the same paper, correcting the same lesion
earlier and completely, **did** restore myelination and conduction to wild-type levels (R31) — which separates timing
and completeness from irreversibility.

In the leukodystrophy model, an oligodendrocyte-directed AAV was given at P10, an age **chosen** to precede the stated
onset of severe demyelination in the fourth postnatal week (R56). Myelin density improved but did not reach wild type
(R54), while oligodendrocyte apoptosis fell from about half of counted cells to about one in twenty, astrogliosis and
macrophage counts fell sharply (R55), motor measures improved markedly (R57) and survival rose partially (R58).

Both papers state plainly that treating later was not done: "additional preclinical development is needed to optimize
dosage and timing, including treating later in disease" (R30) and "Whether replacement of Cx47 at later disease stages
and after the onset of pathology would be beneficial" remains to be shown (R59). The human anchor points the same way:
the composite MRI white-matter and atrophy score was arrested at a worse plateau in the early-symptomatic group than in
the pre-symptomatic group (R47) — damage present at treatment stayed.

**Correction, 2026-11-06.** The first issue of this record concluded from the two paragraphs above that "the post-onset
myelin arm does not exist in the literature this search reached". That was true of what my searches reached and
misleading as a general claim, because the searches could not reach the relevant families — see section 2.7. The
defensible residue is stated in decision line 4 and in section 6.

Two further corrections inside this section, both from the blind audit. The germline arm of the PMD study **increased**
myelination and restored conduction velocity, motor function and lifespan to wild-type levels; myelination itself
reached about half of wild type with incomplete compaction and is deliberately outside the restored-to-wild-type list,
so R31 is regraded `partial` and the claim that complete early correction normalises the sheath is withdrawn. And the
conduction-velocity row (R28) no longer asserts that conduction "tracked the myelin level rather than the functional
benefit": that dissociation is not in the source, which introduces the measurement to ask whether myelin contributes
to the functional gains and concludes that the treatment increases functional myelin.

### 2.4 The age cliff, and why it is not irreversibility (R37-R39, PMID 39847501)

The single most useful source for `INV-01`, because its design is the WWOX design: a constitutive null that dies in the
third postnatal week, a brain-directed AAV supplying the missing protein, a seizure endpoint and an interneuron
endpoint. At P2 it prolonged survival (R66 — a row **added in the correction round**, because the review found this
claim asserted in three decision lines with no row behind it), reduced seizure severity though **not** the time to
first seizure (R40), prevented thermally induced seizures and fully restored parvalbumin interneuron and pyramidal
excitability (R41). At P10, at twice the exposure, **all eight treated null animals died in the usual window** (R37).

The authors do not read this as irreversibility. They attribute it to transgene level and distribution, note that
single-stranded AAV needs one to two weeks to reach therapeutic expression, and report that other studies and their own
unpublished work found sharply reduced AAV CNS expression with injection after the first postnatal days in rodents
(R38, R39) — a statement they **cite from others and from unpublished observations**, not a finding of this paper, which
the first issue of this record did not make clear. The two explanations were not separated experimentally. Two sources
read in the correction round show the generalisation is specific to route, capsid and promoter rather than to rodent
age: a single systemic administration as late as P20 rescued lethality in another short-lived null (R72), and a
systemic vector at four to five weeks in an already symptomatic null transduced only a few percent of neurons and
still moved survival (R77). This is why the row is `UNVERIFIED` and `outcome = none` rather than a
recovery failure: the restoration achieved at the lethal window was never measured. Set against 2.1, where a
BBB-crossing capsid restored protein and rescued seizures in **adult** animals, the conclusion is that the obstacle at
later ages in these models is delivery and kinetics at least as much as biology.

Growth is the exception that cuts the other way: body weight never exceeded about half the wild-type value through P80
even with pre-onset treatment and rescued survival (R42). The authors trace it to peripheral and gastrointestinal roles
of the gene.

### 2.5 Human timing precedents (R45-R53)

SMA, one intervention, one endpoint, two stages: treated before symptoms, 14 of 14 infants sat independently and 11 did
so inside the normal developmental window, against none of 23 untreated natural-history cases; in the symptomatic
trials of the same intervention 64 percent and 44 percent reached that endpoint and did so months later, and one infant
in each cohort walked by 18 months (R50, R52). Even pre-symptomatically, five of 14 were below the normal range for
gross motor development at 18 months (R53) — residual deficit is the norm.

MLD, within one report: pre-symptomatic and early-symptomatic groups both beat the matched untreated cohort on motor
function and most treated children kept normal cognition (R45, R48), but children entering the rapid progression phase
at treatment **could not benefit**, two of them died of progression, and engraftment and enzyme levels were normal in
the children who deteriorated (R46). The authors state that most symptomatic cases would not be eligible at all, because
progression outruns the months needed for enzyme reconstitution (R49).

Both are carried as human timing precedents with their limits — single-arm or single-centre designs, historical
comparators, small numbers, cross-trial comparison in the SMA case — and never as a WWOX expectation. Neither has a
seizure, interneuron or quantified myelin endpoint.

### 2.6 Bypass rather than replacement (R36, R60-R62)

Reducing a modifier gene, not the mutated one, bought survival in three DEE models (R36, R60) — the same logic as the
module's existing Meis2 lead. It decayed: four of 14 treated animals died between two and six months and the authors
allow the effect may be confined to a three-to-four-week interval (R61). In the same study a compound blocking the same
channel, begun at P10, did not extend lifespan at all while the transcript-level intervention at P2 did (R62). That is
the bridge-versus-restoration question in one experiment, though age, mechanism and modality are confounded in it.

### 2.7 The five sources of the correction round, and what they actually settle (R67-R78)

Added 2026-11-06 on the Orchestrator's instruction, after the review showed my myelin queries could not reach the
relevant gene families. One was open at full text; four are abstract level.

**PMID 40051162 — the row that broke my headline (R67-R71, read at full text).** An astrocyte-specific gene; an
astrocyte-directed, barrier-crossing vector; treatment at 10 months of age, which the authors state is **7 months
after cerebellar white-matter vacuolation onset** and call a "post-symptomatic strategy". Against a null-vector arm in
the same genotype, vacuolation was **fully rescued to control levels** a year later (R67), water content normalised in
every region where it was raised while diffusion metrics improved only partly (R68), and a progressive motor deficit —
documented in the same cohort two months *before* treatment — reverted within two to four months (R69). Two details
matter more than the headline. Only about a fifth of cerebellar white-matter astrocytes and Bergmann glia were
transduced and cerebellar protein stayed **below** the physiological range, yet the cerebellar endpoint fully rescued
(R70): a transduction threshold is endpoint-specific. And this gene's overexpression is separately reported to be
deleterious, producing a phenotype worse than the null, while the exposure used here harmed no treated wild-type
animal (R71) — the hazard-plus-control pair the WWOX arm needs. What this source does **not** contain: any electron
microscopy or g-ratio. Vacuolation and water are not sheath (R69).

**PMID 23817205 (R72, R73, abstract).** A single systemic administration **as late as P20** in a null whose lifespan is
a month or less "completely rescued their early lethality" and "globally improved CNS myelination, although some
abnormalities persisted in the content and distribution of myelin-specific and -enriched lipids". This is the source
that breaks two of my own statements at once: the post-first-postnatal-days generalisation in decision line 6, and the
transfer breaker that a short lifespan forbids a later-delivery design. Note carefully what it does **not** say: the
abstract never locates onset, so these rows are `not_stated` on the timing axis and cannot be read as post-onset
recovery.

**PMID 37149081 (R74, abstract).** Enzyme re-expression improved or normalised oligodendrocyte and neuronal lineage
markers, and the authors state the effect "is blunted in old mice", attributing the limit to neuronal rather than
oligodendrocyte recovery. An author-stated age dependence for a myelin-lineage endpoint — and the attributed
bottleneck is the neuron, which for a neuron-driven lesion is the pessimistic half. The endpoint is marker expression,
not sheath or conduction; the title's "reverses dysmyelination" is stronger than the abstract's own report.

**PMID 41566774 (R75, R76, abstract).** The second antisense hypomyelination precedent `BRIEF_R2.md` asked for by name.
Lifespan, motor phenotypes and seizures all improved and visual evoked potential latencies recovered — a conduction
readout, not a marker. But the authors' own verb is **prevents** myelin and oligodendrocyte loss, so this is an
early-window result and not a post-onset myelin recovery. Its stated major limitation is the most directly useful thing
in it: the oligonucleotide **failed to reach cerebellar granule neurons by any route tried** (R76) — a blind spot in
exactly the structure that carries the ataxia phenotype and that the WWOX vector already reaches least.

**PMID 23011033 (R77, R78, abstract).** Read on the Orchestrator's explicit instruction although this gene family was
assigned to the sibling package; flagged here and in the row so the integrator knows why the boundary moved. Juvenile
delivery at four to five weeks, when the model is already symptomatic, achieved only about two to four percent neuronal
transduction and "modest improvements in survival were still observed" (R77). That breaks the all-or-nothing reading of
a transduction threshold. Wild-type animals given the same neonatal vector showed no significant deficit (R78), which
places the lethal-reactivation hazard reported elsewhere on **abrupt conditional reactivation** rather than on gene
addition as such.

**What the five do not do.** None measures myelin sheath morphometry. All three white-matter sources correct a glial or
metabolic lesion in the cell that carries it, not a neuron-driven one. Four of the five are abstract level, so no
method, comparator, figure or limitation beyond the quoted sentences was read.

---

## 3 · Counter-evidence, collected

24 of the 65 rows are `role = counter`. The ones that change a reading:

* **An age cliff exists and is attributed to delivery, not biology** (R37-R39), and two further sources show the
  generalisation behind it is route- and capsid-specific rather than age-specific (R72, R77). Treat an observed window
  as a candidate modality artefact until the restoration achieved at that age is measured.
* **A cellular endpoint overshot rather than normalised** while the phenotype fully recovered (R07). An interneuron or
  firing measure used as a success criterion needs its acceptable direction pre-specified.
* **The intervention itself changes behaviour in normal animals** (R18, R19). Without a treated wild-type arm, an
  intervention effect is scored as a rescue. For R18 the **direction is contested**: the source reads the same
  open-arm result as a normalised disease marker, this record read it as a cost, and after the blind audit the grade
  `worse` was withdrawn to `partial` with both readings stated. R19 keeps `worse` because it is measured in wild-type
  animals, where no normalised-disease-marker reading is available.
* **Growth did not recover even pre-onset**, in the source whose design most resembles the WWOX one (R42), and stayed
  below wild type in another (R21).
* **The structural myelin endpoint moved least in both myelin models even with pre-onset treatment** (R25, R28, R54),
  and the human composite imaging score was arrested at a stage-dependent plateau rather than reversed (R47) — but a
  white-matter vacuolation and water endpoint **was** fully reversed after onset in a glial-gene lesion (R67, R68), so
  the class is not uniformly unrecoverable and the honest residue is sheath morphometry alone.
* **An author-stated age ceiling exists for a myelin-lineage endpoint**, and its authors attribute the limit to
  neuronal rather than oligodendrocyte recovery (R74) — the half that transfers worst to a neuron-driven lesion.
* **A modality can be blind to a whole structure**: an oligonucleotide failed to reach cerebellar granule neurons by
  any route tried (R76), in the region that carries the ataxia phenotype.
* **Benefit can decay** (R61) and **can require re-treatment** (R23): a short follow-up will miss both.
* **Human post-symptomatic treatment failed outright** in rapidly progressing cases with molecularly successful
  correction (R46).
* **Two models could not be asked the question at all** because death follows the first seizure (R32, and the juvenile
  arm of R37). The WWOX null is a third such model; the absence of a post-onset arm in the WWOX literature is the
  field's normal condition, not a gap peculiar to WWOX.

---

## 4 · What the added arm of `INV-01` must measure, given these precedents (IPOTESI, 10 lines)

1. **A within-animal pre-treatment recording**, not a between-group contrast: the one design here that proved
   post-onset recovery in adults did exactly that (R09), and the two that could not said so as a limitation (R20, R32).
2. **The restoration actually achieved, measured at the age of treatment and in the regions that matter** — without it
   a null arm is uninterpretable in the way R37 is, and cannot be told from a kinetics failure (R38).
3. **Keep the electrocorticogram and add a network readout**: seizure and network endpoints are the only class with
   clean post-onset recovery (R02, R03, R09, R16), so they carry the arm's statistical power.
4. **An interneuron endpoint in two parts**: excitability (recovered post-onset in R06, pre-onset in R41) and **number**,
   which no source in this set measured — the module should not assume it behaves like excitability.
5. **A quantified myelin endpoint scored as arrest versus reversal**, with a treated-at-onset comparator sacrificed at
   the treatment age; the precedents license only arrest, and only pre-onset (R25, R47, R54).
6. **A treated wild-type or heterozygote arm**, because the intervention has its own effects in a normal brain
   (R18, R19, R44).
7. **Growth and glycaemia as primary, not supportive, endpoints**: this is the class that failed even pre-onset (R42).
8. **Follow-up long enough to see decay, and a pre-specified re-treatment arm** (R23, R61).
9. **Pre-specify that a cellular measure may overshoot**, and score partial normalisation as partial, not as support
   (R07); partial myelin with full functional benefit is the expected pattern, not an anomaly (R29).
10. **Report the region-by-region coverage of the vector** before calling any endpoint unrecoverable (R10, R43).

---

## 5 · Conditions under which these precedents do not transfer to the neuron-restricted, short-lived, hypomyelinated Wwox null

* **Lesion viability — narrowed by the correction round.** Every clean post-onset *seizure* recovery here sits in a
  lesion compatible with life at the treatment age: a haploinsufficiency treated at P30 and P90, a homozygote treated at
  P40 whose untreated median survival is about ten weeks. The Wwox null dies at about P15, so those arms cannot be
  reproduced in it, and the one source with a comparably short-lived null is the one whose later arm failed (R37).
  **But a short lifespan does not by itself forbid a later-delivery design**: a systemic administration as late as P20
  in a null that dies within a month rescued lethality and improved myelination (R72, R73). The breaker is therefore
  about the *age the endpoint must be read at*, not about the delivery age as such.
* **Modality.** Three sources correct a gain of function or an excess transcript by knockdown (R15-R23, R32-R36, R60-R62).
  WWOX loss cannot be corrected by knockdown of anything. Only two sources here actually replace a missing protein in
  vivo (39847501, 28100454), and both are pre-onset.
* **Driver and target cell.** Both myelin precedents state an oligodendrocyte-intrinsic defect, one of them explicitly
  cell-autonomous (R54-R59). In the Wwox system the driver is neuronal and lineage deletion is phenotypically silent, so
  the cell the intervention must reach is a different one. This is the IT29 P3-C condition and it holds here.
* **Mechanism of the human precedents.** MLD works by cross-correction from engrafted donor-type myeloid cells, with a
  months-long latency to enzyme reconstitution (R45, R49); SMA has a peripheral motor endpoint and depends on newborn
  screening that does not exist for WWOX (R50-R53). Neither is cell-autonomous neuronal restoration and neither has a
  seizure, interneuron or myelin endpoint.
* **Endpoint identity.** No source here measured interneuron number, radial-glia or progenitor composition, or
  glycaemia. The WWOX progenitor phenotype — the part no genetic add-back after onset has corrected — has no precedent
  in this set at all, in either direction.
* **Age mapping.** The P30 mouse age in 2.1 is mapped by its authors to roughly 4 human years and P90 to roughly 20, with
  citations. Those are the authors' mappings for that model. No human age follows for WWOX from anything here, and the
  rodent myelination peak near P20 (carried as context from the IT29 P3-C row set, not re-read here) is the anchor the
  myelin transfer condition needs.
* **Direction of a window.** An observed perinatal-only window in a rodent may be the modality's window, not the
  disease's (R38, R39). This cuts both ways: it weakens "WWOX restoration after onset cannot work", and it equally
  forbids concluding that it can.

---

## 6 · What is not established

* Whether a **myelin sheath** deficit re-myelinates after onset under gene restoration or correction: no source
  reached by any of these searches measured sheath morphometry — electron microscopy or g-ratio — after a documented
  onset, in either direction. What is now on record after onset is a white-matter **vacuolation and water-content**
  reversal in a glial-gene lesion (R67-R69) and a composite human imaging score that was arrested (R47). Neither is a
  sheath measurement, and the two hypomyelination author groups still name later treatment as untested.
* Whether any of this transfers to a **neuron-driven** myelin lesion. All three post-onset white-matter sources correct
  a glial or metabolic lesion in the cell that carries it; the Wwox myelin deficit follows a neuronal defect and the
  oligodendrocyte-lineage deletion is phenotypically silent. The one source that speaks to this attributes its own
  age-dependent ceiling to limited **neuronal** rather than oligodendrocyte recovery (R74), which is the less
  encouraging half of it.
* Whether **interneuron number** (as opposed to excitability) responds to restoration at any age.
* Whether the P10 failure in R37 is biological or kinetic. The paper does not separate them, and neither does this record.
* Whether post-onset recovery of seizures in a haploinsufficiency transfers to a complete null of a different gene class:
  the two post-onset successes here both restore a channel or correct a channel transcript, not a lost scaffold protein.
* Whether the behavioural costs seen in treated wild-type animals (R18, R19) are modality-specific; only one source ran
  that arm for behaviour.
* Dose-response of restoration: no source here ran more than a monotone exposure series, and the one transduction
  threshold on record is from an abstract (R65).
* Whether any of the human stage effects reflect the stage itself or the selection and eligibility rules that follow
  from it; the MLD authors state they refined eligibility during the study.

## 7 · What was not reachable

* **Full text refused**: PMID 31607539 (Europe PMC returned HTTP 500; the publisher blocks XML download at PMC) and
  PMID 41883162 (same block). Both are carried as `abstract_only` rows (R63, R65) and no method, figure or table of
  either was read.
* **PMID 32848094** (the most-cited Dravet upregulation study) is not open by any route allowed here; `abstract_only`
  (R64). Its two treatment ages both precede the onset stated for that model elsewhere, so nothing is lost on the
  timing axis, but its methods were not read.
* **The symptomatic SMA primary reports** (PMIDs 33743238, 34536405) are not open by these routes. The
  pre-symptomatic-versus-symptomatic contrast is therefore carried as a **secondary statement inside** PMID 35715566
  (R52), with the authors' own caution that the trials differ in design, endpoints and eligibility. The symptomatic
  numbers were not verified at their source.
* **PMID 28100454** was read through the open PMC article page in **four** question-directed passes, not as structured
  full text (Europe PMC and the efetch route both refused). Depth is recorded as `partial_fulltext`; figures were not
  viewed. The fourth pass was made in the correction round to re-acquire the survival sentence: R58 previously carried
  `attestation_without_quote`, and it now carries a verified verbatim span. **No row in this package carries an
  attestation in place of a quote any longer.**
* **Stxbp1, Scn2a and Kcnq2 post-onset restoration**: not found. Bounded search — PubMed via NCBI E-utilities,
  queries Q10, Q11, Q13, Q14, Q24, Q25, run 2026-11-05, 93 records screened by title across those six strings. Recorded
  as UNMEASURED, not as absent. The reviewer's independent search (V02) corroborates the Stxbp1 null.
* **The myelin null, restated honestly.** The first issue of this record claimed that no post-onset myelin-correction
  arm exists in any hypomyelination model, on the strength of queries Q16 and Q23. Those queries were anchored on
  hypomyelination, Pelizaeus, jimpy, shiverer, Plp1 and Mbp, so **no string in them could reach an enzyme-deficiency,
  connexin, tubulin or astrocyte-transporter leukodystrophy** — which is where the relevant arms turned out to be. The
  claim was a search artefact and is withdrawn. What survives, after queries Q30 and Q31 of this round plus the
  reviewer's V01, V03 and V06: **no source measured myelin sheath morphometry (electron microscopy or g-ratio) after a
  documented onset**, in any family, in either direction. Q30 returned a single hit that proved to be an unrelated
  ocular-surface review, and Q31 returned none.
* **Interneuron number at any timing**: not found, in my searches and in the reviewer's V04 and V07 independently.
  Recorded as UNMEASURED.
* **Supplementary material** of every source: not opened. **No figure image was inspected in any source.** Figures were
  read as captions only, except in PMID 28100454 where they were not read at all. Two rows rest on a caption that
  itself carries the result (R34, R41); the row names the caption as its section. Because of this, no row claims
  `full_text` depth: the strongest label used is `partial_fulltext`, and `staged_receipt_check.py` refused the three
  receipts on which this record had first over-claimed a complete read, which is how that error was caught.
* **Four of the five correction-round sources are abstract level** (PMIDs 23817205, 37149081, 41566774, 23011033):
  Europe PMC returned an empty body for all three that have a PMC record, and no method, comparator, figure or
  limitation beyond the quoted abstract sentences was read for any of them. Their rows are `UNVERIFIED` or carry the
  authors' own verb, and two of them (R72, R73) are `not_stated` on the timing axis because their abstract never
  locates onset.
* The PubMed MCP tool conjoins every term of a query with AND, so long strings return zero hits (Q06, Q07, Q17). All
  substantive searching was done through NCBI E-utilities and Europe PMC REST instead.
* No third-party bytes were saved inside the repository; all downloads stayed in the session scratch directory.

---

## 8 · Receipts

Ten staged receipts in `receipts/` with index `receipts/INDEX.tsv`, event-id suffix `-25`, none recorded. Nine carry
`event_at` on 2026-11-05 and one (PMID 40051162, read in the correction round) on 2026-11-06. One source had a prior
receipt (PMID 39847501, `FTR-20261003-39847501-01`, whose manifest carries no locator entries): its receipt is set to
`new_question_outside_prior_coverage`. All others are `first_read`. The seven `abstract_only` sources carry no receipt,
because no text beyond the PubMed record was read for them; they are cited as abstract rows in the table and listed in
section 7. Every receipt passes `staged_receipt_check.py --check-doi`, and `receipts/INDEX.tsv` records that check with
its date in `validated_ok`.
