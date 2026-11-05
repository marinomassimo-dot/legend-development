# R2: restoration after onset in DEE and hypomyelination models, and human timing precedents

Scientist `sb-r2`, challenge `CH-SB-POSTONSET-RESTORATION` part 2, task `ORCH-SCIBATCH-DR-20261105`, 2026-11-05.
Non-canonical research material. **Not medical advice**: no dose, schedule, administration route, preparation or
clinical preference appears here, for any species; exposure is described qualitatively only. Public edition — the
subject is the WWOX-DEE reference genotype class and no individual-level record is used. Nothing outside this
directory was edited; receipts are staged drafts, not recorded. Status vocabulary is the one defined in
`BRIEF_R1.md` and in `rescue_window_it6_20261029.md`.

Table: `evidence_r2.tsv`, 65 rows over 12 sources. Queries: `queries.tsv`, 29 entries. Proposals: `module_inputs.md`.

**Depth, stated once and applied everywhere.** Nine sources were read beyond the abstract and three at abstract level
only. **No figure image was inspected in any source**, so every row of the nine is labelled `partial_fulltext`, never
`full_text`, and figures are recorded as `captions_only` (or `not_read`) in the receipts. For eight sources the prose
read covers abstract, results and discussion, with introduction, methods and limitations as recorded per receipt;
supplements were not opened anywhere. The ninth (PMID 28100454) was read through the open article page in three
question-directed passes because the structured-text routes refused it. The staged receipts in `receipts/` carry the
section-by-section truth and all nine pass `staged_receipt_check.py`.

---

## 0 · Decision (10 lines)

1. **DATO.** Post-onset restoration of a DEE gene has recovered seizures, survival, behaviour **and cognition**, fully,
   in a conditional Dravet model treated after manifest seizures and again in adults ten weeks after onset, the adult
   arm with a within-animal pre-treatment recording (R01-R04, R09; PMID 35013317).
2. **DATO.** A glial endpoint — reactive astrogliosis, by cell counts, morphology and transcripts — also recovered
   after onset in that model (R08). No myelin endpoint exists in it.
3. **DATO.** A second DEE model treated while symptomatic (gain-of-function silencing, ~3 weeks after seizure onset)
   recovered survival, seizure frequency and a composite welfare-cognitive endpoint (R15-R17; PMID 36173683).
4. **DATO.** The only two hypomyelination precedents reachable both treated **before** onset of the myelin deficit, and
   in both the structural myelin endpoint moved least: about 10 percent of wild type with reduced compaction in one
   (R25), below wild type in the other (R54), while oligodendrocyte number, apoptosis, glia, respiration, locomotion
   and lifespan moved far more (R26, R29, R55, R57). **No post-onset myelin arm exists in either** (R30, R59).
5. **DATO.** A brain-directed AAV replacing a missing protein in a short-lived null — the closest structural analogue of
   the WWOX design — worked at P2 and was **completely ineffective at P10**, at twice the exposure (R37; PMID 39847501).
6. **INFERENZA.** That cliff is **not** evidence of biological irreversibility. The authors attribute it to transgene
   level and distribution and state that rodent AAV CNS expression falls sharply with injection after P3-P4 (R38, R39).
   A perinatal-only AAV window in a rodent is therefore partly a property of the modality in the rodent.
7. **DATO.** In the same source, pre-onset treatment rescued survival, seizure severity and **parvalbumin interneuron
   excitability** (R40, R41) while **growth was not rescued at all** (R42). Survival is not a proxy for growth.
8. **DATO.** Human: stage at treatment dominates. The same intervention and endpoint gave near-normal milestones
   pre-symptomatically and much poorer ones post-symptomatically in SMA (R50, R52); in MLD the white-matter and atrophy
   score was **arrested at a worse plateau** when treatment followed symptoms, and children entering rapid progression
   did not benefit at all (R46, R47).
9. **INFERENZA.** The split that the evidence supports is not prevented-versus-recovered by endpoint class alone. It is:
   endpoints sustained by **ongoing** dysfunction (seizures, network firing, astrogliosis, transcriptome, interneuron
   excitability) recover after onset; endpoints that are **accumulated structure** (myelin sheath, atrophy) are at best
   arrested; endpoints with a **peripheral or developmental-growth component** recover least, even pre-onset.
10. **IPOTESI.** For `INV-01`: the added arm should be powered on seizure and network endpoints, must carry a
    within-animal pre-treatment recording, a treated wild-type arm and a quantified myelin endpoint scored as
    *arrest versus reversal* — and must measure the restoration actually achieved at the age of treatment, or a null
    result will be uninterpretable in exactly the way R37 is.

---

## 1 · Matrix: endpoint class by restoration timing

Counts are **studies** (not rows), counted once per source per cell; a source appears in several cells. This is a
tabulation, not a meta-analysis. The models differ in gene, lesion class, species and life span; the published
literature selects for success, and three of the twelve sources here exist *because* a post-onset arm could not be run,
which is itself a publication-shaped fact.

| Endpoint class | PREVENTED / EARLY-WINDOW (pre-onset) | RECOVERED (post-onset) | UNMEASURED or UNVERIFIED after onset |
|---|---|---|---|
| Survival | 6 (32610343, 31943325, 39847501, 36173683, 28100454, 37901435) + 2 human (35065785, 35715566) | 3 (35013317 full, 36173683 full, 35065785 partial in human early-symptomatic) | 1 failure at onset (39847501); 2 models could not be tested at all (31943325, 39847501 juvenile arm) |
| Seizure or network hyperexcitability | 4 (31943325, 39847501, 32848094, 31607539) | 2 (35013317 full, incl. an adult arm; 36173683 partial) | 0 reachable — the class with the best post-onset evidence |
| Motor | 3 (32610343, 28100454, 31943325) + 2 human (35065785, 35715566) | 1 human, partial (35065785) | 1 (35013317: the model has no motor deficit, so no recovery is measurable) |
| Cognition and behaviour | 1 (36173683 neonatal) + 1 human (35065785) | 2 (35013317 full, 36173683 partial) | 1 (41883162: age not stated) |
| Neuronal structure (interneuron) | 2 (39847501 PV excitability, 31607539) | 1 (35013317, recovered but overshot wild type) | **interneuron NUMBER: 0 sources, UNMEASURED everywhere in this set** |
| Myelin and glia | 2 myelin (32610343, 28100454) + 1 glia (35013317 astrogliosis is post-onset, see next column) | 1 glial only (35013317 astrogliosis); 1 human, arrest not reversal (35065785) | **myelin sheath after onset: 0 sources. UNMEASURED.** Both authors name it as the untested next step |
| Systemic and metabolic | 3 (39847501 growth not rescued; 36173683 growth partial; 32610343 respiration full) | 0 | growth and glycaemia after onset: UNMEASURED |

**Reading.** Seizure and network endpoints are the only class with clean, well-controlled post-onset recovery.
Myelin sheath after onset is empty across the whole searched literature. Systemic growth is the endpoint that failed
even pre-onset, in the source closest to the WWOX design.

---

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
and after the onset of pathology would be beneficial" remains to be shown (R59). **The post-onset myelin arm does not
exist in the literature this search reached.** The human anchor points the same way: the MRI white-matter and atrophy
score was arrested at a worse plateau in the early-symptomatic group than in the pre-symptomatic group (R47) — damage
present at treatment stayed.

### 2.4 The age cliff, and why it is not irreversibility (R37-R39, PMID 39847501)

The single most useful source for `INV-01`, because its design is the WWOX design: a constitutive null that dies in the
third postnatal week, a brain-directed AAV supplying the missing protein, a seizure endpoint and an interneuron
endpoint. At P2 it prolonged survival, reduced seizure severity (though **not** the time to first seizure, R40),
prevented thermally induced seizures and fully restored parvalbumin interneuron and pyramidal excitability (R41).
At P10, at twice the exposure, **all eight treated null animals died in the usual window** (R37).

The authors do not read this as irreversibility. They attribute it to transgene level and distribution, note that
single-stranded AAV needs one to two weeks to reach therapeutic expression, and report that other studies and their own
unpublished work found sharply reduced AAV CNS expression with injection after P3-P4 in rodents (R38, R39). The two
explanations were not separated experimentally. This is why the row is `UNVERIFIED` and `outcome = none` rather than a
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

---

## 3 · Counter-evidence, collected

24 of the 65 rows are `role = counter`. The ones that change a reading:

* **An age cliff exists and is attributed to delivery, not biology** (R37-R39). Treat an observed window as a candidate
  vector-kinetics artefact until the restoration achieved at that age is measured.
* **A cellular endpoint overshot rather than normalised** while the phenotype fully recovered (R07). An interneuron or
  firing measure used as a success criterion needs its acceptable direction pre-specified.
* **The intervention itself changes behaviour in normal animals** (R18, R19). Without a treated wild-type arm, an
  intervention effect is scored as a rescue.
* **Growth did not recover even pre-onset**, in the source whose design most resembles the WWOX one (R42), and stayed
  below wild type in another (R21).
* **The structural myelin endpoint moved least in both myelin models even with pre-onset treatment** (R25, R28, R54),
  and in humans it was arrested at a stage-dependent plateau rather than reversed (R47).
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

* **Lesion viability.** Every clean post-onset recovery here sits in a lesion compatible with life at the treatment age:
  a haploinsufficiency treated at P30 and P90, a homozygote treated at P40 whose untreated median survival is about ten
  weeks. The Wwox null dies at about P15. The P30 and P90 arms **cannot be reproduced in it**, and the one source with a
  comparably short-lived null is the one whose later arm failed (R37).
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

* Whether any **structural myelin** deficit re-myelinates after onset under gene restoration or correction: no source,
  in any model, in either direction. Both relevant author groups name it as untested.
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
* **PMID 28100454** was read through the open PMC article page in three question-directed passes, not as structured
  full text (Europe PMC and the efetch route both refused). Depth is recorded as `partial_fulltext`; figures were not
  viewed; one row carries `attestation_without_quote` because no verbatim sentence was captured for its figures (R58).
* **Stxbp1, Scn2a and Kcnq2 post-onset restoration**: not found. Bounded search — PubMed via NCBI E-utilities,
  queries Q10, Q11, Q13, Q14, Q24, Q25, run 2026-11-05, 93 records screened by title across those six strings. Recorded
  as UNMEASURED, not as absent.
* **A post-onset myelin-correction arm in any hypomyelination model**: not found. Bounded search — queries Q16 and Q23,
  13 records, 2026-11-05, plus the explicit statements of both myelin papers that they did not do it.
* **Supplementary material** of every source: not opened. **No figure image was inspected in any source.** Figures were
  read as captions only, except in PMID 28100454 where they were not read at all. Two rows rest on a caption that
  itself carries the result (R34, R41); the row names the caption as its section. Because of this, no row claims
  `full_text` depth: the strongest label used is `partial_fulltext`, and `staged_receipt_check.py` refused the three
  receipts on which this record had first over-claimed a complete read, which is how the error was caught.
* The PubMed MCP tool conjoins every term of a query with AND, so long strings return zero hits (Q06, Q07, Q17). All
  substantive searching was done through NCBI E-utilities and Europe PMC REST instead.
* No third-party bytes were saved inside the repository; all downloads stayed in the session scratch directory.

---

## 8 · Receipts

Nine staged receipts in `receipts/` with index `receipts/INDEX.tsv`, event-id suffix `-25`, none recorded. One source
had a prior receipt (PMID 39847501, `FTR-20261003-39847501-01`, whose manifest carries no locator entries): its receipt
is set to `new_question_outside_prior_coverage`. All others are `first_read`. The three `abstract_only` sources carry no
receipt, because no text beyond the PubMed record was read for them; they are cited as abstract rows in the table and
listed in section 7.
