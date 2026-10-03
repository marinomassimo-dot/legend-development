# Intake wave 5 — 2026-10-03 — Scientist A

`context_policy: SOURCE_FIRST` — the first pass on all six sources was written before
`CC-20261003W3-C-RESTORATION-SPEC-01` (the wave-3 six-parameter restoration spec) or any registry
record was opened. The comparison with wave 3 is in
[`commit_candidates/CC-20261003W5-A-WINDOW-STATUS-01.md`](commit_candidates/CC-20261003W5-A-WINDOW-STATUS-01.md).

**Theme:** the gene-replacement architecture for a recessive null CNS disease.
**None of the six sources mentions WWOX.** Every statement below is a transferable lesson from
another gene with its transfer limit stated. **Nothing here is medical advice.**

---

## The assigned question

> *What does each source add to, or limit in, the claim that a WWOX gene-replacement programme can be
> specified today with its four hardest parameters bounded by evidence rather than by analogy — cargo
> size and cassette, the developmental window, the dose level and its two-sided risk, and the immune
> cost of expressing a foreign protein in an immature CNS — and for each parameter, does the source
> measure it in a recessive null model, or carry it over from a dose-sensitive dominant one?*

## The answer, in one paragraph

**One of the four parameters is now bounded by measurement; two are bounded only in shape; one is not
bounded at all, and it is the one the assignment assumed was not a problem.** Cargo size and cassette
design is measured end to end, with a quantified penalty at every step above the AAV packaging limit
and a quantified bonus below half of it — but it cannot be *applied*, because this repository holds
no WWOX cassette budget, which is arithmetic on a sequence rather than an experiment. Dose has a
measured *shape* and no transferable magnitude: the striking new result is that a gene's two
phenotypes need not share a dose. The developmental window remains unmeasured — wave 3's negative
survives six further sources including the first human one — but it gains two refinements, one of
which points the window later rather than earlier. And the immune cost is **not** bounded: a
recessive-null patient is cross-reactive-immunological-material negative, so the delivered protein is
foreign to them, which means the assignment's premise that "WWOX is a self protein" is false for the
reference genotype — and the one complete IND-enabling package for a recessive loss-of-function CNS
disease in this corpus tested transgene immunogenicity only in wild-type animals, dosed in the first
days of life.

## Parameter by parameter

### 1 · Cargo size and cassette — MEASURED, and newly so

| Rung | Measurement | Source | Model class |
|---|---|---|---|
| 1.7 kb coding sequence + minimal synthetic promoter | the short promoter is what *permits* self-complementary packaging; scAAV stated to transduce "at least 10-fold more cells" | PMID 41712282 | **recessive null** (mouse) |
| weak minimal promoter in a clinical lot | lot was 42% genome-containing, so 1×10^15 vg carried 2.38×10^15 capsids; promoter weakness credited as an overexpression-safety lever | PMID 41314141 | **recessive, human** |
| cDNA under a strong large ubiquitous promoter | better rescue, but the promoter "cannot always be implemented" with a large transgene | PMID 39358605 | **recessive null** (mouse + primate) |
| 5.136 kb, above the ~4.7 kb limit | packages, at a **two-fold yield loss** vs a 4.617 kb same-day control; 94.60:5.40 full:empty; the "75.81% full-length" is a **4–6 kb bin**, with **15.22% above 6 kb** | PMID 40988338 | dominant heterozygote |
| >6.0 kb open reading frame | single-vector replacement impossible; split-intein dual vector, no human data | PMID 41712149 | dominant (review) |

Three of the five measurements come from recessive-null programmes, which is the strongest
model-class provenance of any of the four parameters. **The block is internal:** the WWOX cassette
budget — coding-sequence length for a stated isoform, promoter, regulatory elements, poly(A), ITR to
ITR — is not recorded anywhere in this repository, and until it is, none of the ladder can be
applied. Candidate: [`CC-20261003W5-A-CARGO-CASSETTE-01`](commit_candidates/CC-20261003W5-A-CARGO-CASSETTE-01.md).

### 2 · The developmental window — STILL NOT MEASURED, with two refinements

Every apparent window result in these six sources resolves to delivery, to dose or to immunity:

- **PMID 41712282**: same dose, same route, P10 versus 3 months → cerebellar vector
  15.7×10^3 ± 3.1×10^3 against 1.2×10^3 ± 7.4×10^2 vg per genome. Switching the adult route to
  intracisterna magna recovered part of it (7.5×10^3). Delivery, not window.
- **PMID 39358605**: neonates at 4×10^13 vg/kg, adults at 2–5×10^12 vg/kg. An order of magnitude of
  dose, not a window.
- **PMID 40988338**: the neonatal arm got only the lowest dose by a forebrain-biased route and
  reached ~70% of wild-type protein; the juvenile arms that worked used 3–10× more vector and reached
  near-wild-type protein brain-wide. The authors say so themselves.
- **PMID 41314141**, the first human source: "the timing of the intervention is likely to have a very
  large impact" — but n = 4, open label, no natural-history comparator, no dose-response, and "no
  formal statistics were performed on this cohort". An interpretation, not a measurement.
- **PMID 40809677**: an immune result, with the adult arm on four times the vector.

**Refinement 1 — a single window does not exist to be measured.** PMID 39358605 separates endpoints
by age for the first time in this corpus: adult treatment left **brain structure** unrescued while
still rescuing **motor function**. PMID 41712282 shows the same shape from the other side (seizure
resistance and delta-wave abnormality recovered in adults; sleep architecture and theta/alpha less
so, with the authors declining to choose between underpowering and a non-rescuable developmental
feature). Any WWOX window claim must name its endpoint class.

**Refinement 2 — the counter-datum points later.** PMID 41712149 reports a conditional knock-in in
which the endogenous gene is reactivated on demand: at P30 after symptoms, complete rescue of both
seizure types; and **at P90, in adulthood, protein restored and seizures rescued "despite months of
prior seizures"**. This is the corpus's only design with expression matched across ages *by
construction*, and efficacy did not fall — close to the inverse of wave 3's revival trigger. Limits:
review-level with the primary not retrieved; a dominant haploinsufficiency with one intact allele;
and seizure rescue is not developmental rescue. The practical consequence is that the direction of
error is asymmetric — the risk is closing the window **too early**.
Candidate: [`CC-20261003W5-A-WINDOW-STATUS-01`](commit_candidates/CC-20261003W5-A-WINDOW-STATUS-01.md).

### 3 · Dose and its two-sided risk — SHAPE measured, magnitude not transferable

The new result, and the one that most directly tests the assignment's premise about a neuro-metabolic
gene: in PMID 41712282 the metabolic and the seizure endpoint were read in the same animals at the
same two doses and **had different dose-response curves**. Plasma citrate fell dose-dependently to
**65 ± 8.0% of wild type** at the high dose — an overshoot past normal, from a knockout baseline about
20% *above* wild type — while the chemoconvulsant endpoint **saturated**, the low dose matching the
high. The authors put the matching risk on the record: overexpressing the same gene in development
has been reported to cause autistic-like behaviour and altered white-matter integrity.

So a programme that predicts rescue of both a metabolic axis and a seizure axis must decide **which
endpoint sets the dose**. Transfer limit: the comparator's metabolic axis has a directly measurable
analyte in blood and CSF, which is the only reason the mismatch was visible. WWOX has no such
analyte here — a WWOX programme would see one curve and conclude it had found the dose. This
reinforces wave 3's `RC-C-20261003w3` from a second direction, and two further sources in this wave
cannot state their dose in protein units at all: PMID 41712282's antibody does not recognise the
endogenous mouse protein (no wild-type reference), and PMID 39358605's target antibody was unreliable
and had to be proxied by a partner subunit.

A second pattern: in three sources the harm of the top dose sits below the headline — a dose-confined
50% surgical attrition visible only in a supplementary table (PMID 40988338, Table S3: 5 of 10
high-dose mice, 5 recorded, against 0 of 8 and 0 of 4); "no significant adverse events" covering
dose- and time-dependent nerve and spinal-cord degeneration plus a treatment-associated leucocytosis
and one unexplained death (PMID 39358605); and a "well tolerated" highest-ever intrathecal dose whose
adverse-event table does not reconcile with itself (PMID 41314141).
Candidate: [`CC-20261003W5-A-DOSE-TWO-SIDED-01`](commit_candidates/CC-20261003W5-A-DOSE-TWO-SIDED-01.md).

### 4 · The immune cost — NOT bounded, and the assignment's premise here was wrong

The assignment's note on PMID 40809677 reads: *"WWOX is a self protein, so the transfer is to vector
and route immunity, not to transgene immunity."* **This is false for a biallelic null.** "Self" is
what the immune system has seen, not the species of the coding sequence — and PMID 41314141
operationalises exactly that distinction in children: patients with *"predicted null mutations (no
residual endogenous MFSD8 protein)"* were classified **CRIM-negative** and given prednisone **plus**
sirolimus **plus** tacrolimus, where a patient predicted to make some protein got two drugs. The one
immune event in the trial occurred in the single CRIM-*positive* patient on the two-drug regimen,
after the steroid taper. A WWOX null sits in the three-drug class.

What is missing is the measurement:

- **PMID 39358605** — the nearest architectural analogue — tested transgene immunogenicity in
  **wild-type** mice dosed at **P1–3**, by interferon-γ ELISpot, with **no antibody assay anywhere**
  (despite a figure title claiming "no B cell response"); the GLP primates were wild type too. Every
  animal in the immunogenicity package already expressed the orthologue.
- **PMID 41712282** put a human transgene into a knockout host — the closest thing here to a
  protein-naive recipient — and reported **no immune endpoint at all**.
- **PMID 40809677** supplies the mechanism and its limits: early expression buys **cellular** but not
  **humoral** tolerance ("neither treatment time point circumvented eliciting a humoral immune
  response"); the protection does **not** transfer to a later dose (a redose after a neonatal prime
  still cost 25.3% of neurons, and only 3 of 7 animals expressed the transgene in the redosed
  hemisphere); and it is **antigen-specific** — EGFP in the same compartment at the same age was
  inert, so "foreign protein" is not one category. It also delivers the design warning that matters
  most: tolerance is thought to need MHC II-dependent regulatory T cells, neurons do not express
  MHC II, and the authors suspect their **neuron-specific promoter** "may have hampered the
  development of Cas9-reactive Tregs".
- **PMID 41712149** bounds what asymptomatic CSF change looks like at scale in children: transient
  protein elevations above 50 mg/dL in **about three-quarters** of patients in the antisense extension
  studies.

The three design choices therefore interact, and two run against intuition: a neuron-restricted
promoter is safer for overexpression but possibly worse for tolerance; early dosing buys cellular
tolerance only, and buys nothing for a second dose.
Candidate: [`CC-20261003W5-A-TRANSGENE-IMMUNITY-01`](commit_candidates/CC-20261003W5-A-TRANSGENE-IMMUNITY-01.md).

## Model-class provenance, counted

| Parameter | Measured in a recessive null | Carried from a dominant / dose-sensitive model | Human |
|---|---|---|---|
| Cargo and cassette | PMID 41712282, PMID 39358605 | PMID 40988338, PMID 41712149 | PMID 41314141 |
| Window | PMID 41712282, PMID 39358605 (both resolve to delivery/dose) | PMID 40988338, PMID 41712149 | PMID 41314141 (interpretation only) |
| Dose, two-sided | PMID 41712282, PMID 39358605 | PMID 40988338 | PMID 41314141 (no dose-response) |
| Transgene immunity | **none** — PMID 39358605 used wild-type animals; PMID 41712282 ran no immune endpoint | PMID 40809677 (wild-type host, bacterial antigen) | PMID 41314141 (protocol, under triple immunosuppression) |

## Independence of the sources — a caution

Three of the six share vector-design lineage and must not be counted as independent attestations of
promoter behaviour: PMID 41314141 uses the minimal JeT promoter and its vector's inventor is an
author; PMID 41712282 is from the same institution and uses a JeT-plus-intron promoter; and
PMID 39358605's reagents-and-tools table records that its CBh plasmid came from that same
investigator. The promoter-strength trade-off is attested by one design tradition plus one
independent group (PMID 40988338, hSyn1).

Two of the six are also linked by citation: PMID 40809677 names the trial registration of
PMID 41314141 among the early-phase trials that establish the precedent for CNS AAV administration
to young children. The mechanism paper and the clinical paper are therefore about the same
intervention class, which is why their disagreement about what early delivery buys — tolerance in one,
an untested assumption in the other — is worth more than a coincidence of topic.

Also noted for dose positioning: PMID 41314141's human dose (1×10^15 vg total, intrathecal) is about
2.5× the human dose PMID 39358605 proposes for a four-year-old (4×10^14 genome copies,
intracisterna magna, scaled by CSF volume on FDA advice). Different diseases, different routes,
different scaling — carried as positioning, not as a dose for anything.

## What would change the model if true

1. **The WWOX cassette budget** — one number, no experiment — selects a rung of the cargo ladder and
   with it the promoter, the packaging mode and whether a dual-vector route is needed.
2. **A WWOX pharmacodynamic readout with a wild-type reference** makes a two-axis dose-response
   measurable at all; without one, a mismatch like PMID 41712282's is undiscoverable.
3. **An immunogenicity study in a protein-naive host at the intended age of dosing**, with both T-cell
   and antibody readouts, converts the immune cost from a named gap into a specified requirement.
4. **The conditional-reactivation primary** behind PMID 41712149's P90 statement either hardens or
   removes the only evidence that the window may be wider than assumed.

## What would falsify the central claims

- That the window is unmeasured: a source in this set holding expression constant across ages. None
  does — a checkable statement about six artefacts on disk.
- That transgene immunity applies: evidence that a biallelic-null patient presents WWOX protein as
  self, which would move the reference genotype into the CRIM-positive class.
- That the two axes can disagree on dose: a demonstration that the seizure-endpoint saturation in
  PMID 41712282 is a power artefact.

## Verdicts

| # | PMID | Verdict | One-line reason |
|---|---|---|---|
| A1 | 41314141 | **INGEST** | The only human high-dose intrathecal AAV9 source; supplies the CRIM rule and the empty-capsid arithmetic. Efficacy not established. |
| A2 | 40988338 | **INGEST** | Quantified oversized-packaging penalty, an expression ceiling, and a dose-confined attrition found only in the supplement. |
| A3 | 39358605 | **INGEST** | The nearest architectural analogue for a recessive null, and the paper that locates the immunogenicity gap. |
| A4 | 41712282 | **INGEST** | The two-axis dose mismatch and the age-versus-route delivery arithmetic. |
| A5 | 40809677 | **INGEST** | Mechanism of the window × immunity interaction, with three limits that bound it. |
| A6 | 41712149 | **INGEST** | Positioning map; carries the one expression-matched age comparison and the sharpest transfer limit of the wave. |

No source was OFF-AXIS and none DEFERRED: all six were acquired lawfully and free from Europe PMC,
and one supplement was acquired from the PMC article instance.

## Dedup, integrity and reading debt

`paper_packet.py packet --pmid <N>` was run for all six before any reading: every one returned
"no title recorded · manifest: none — this is a first reading · prior read: depth=none · receipts=0 ·
acquisition: no route recorded". **No reading debt was discharged by this wave**, because no existing
registry statement depended on any of these six — they had no registry presence at all, which is why
`CC-20261003W5-A-REGISTRY-01` creates it. Correspondingly, **no registry statement needed
correcting**: there was none to compare against the source. PubMed `efetch` showed no retraction,
expression of concern or correction notice and no `CommentsCorrections` element for any of the six,
and `dependency_integrity.py screen --manifest-block` returned `SCREENED_CLEAN` for all six
(26/30, 58/65, 53/55, 46/48, 47/49 and 83/89 references screened). PMID 41712149's 89 screened
references independently corroborate the 89 reference call-outs counted in its body.

Patient-overlap check (brief rule 19): only PMID 41314141 reports patients, four children with a
different gene in a different disease, so no overlap with this corpus is possible. The animal-level
analogue of the double-count problem did appear and is recorded: PMID 41712282's vehicle control arms
for the P10 sleep and power-spectrum analysis were already published by the same group.

## Coverage honesty

All six readings are `partial_fulltext_read`, not `complete_fulltext_read`. Figure panels were not
rendered for any paper, so figures are `captions_only` throughout (`not_present` for PMID 41712149,
whose surface carries no figure), and supplements were fetched for one paper only. Where a number
lives in a panel it is not carried. The one case where the supplement changed the reading — the
PMID 40988338 packaging bin and Table S3 attrition — is in the dossier and in the candidates, and is
the wave-4 lesson reproduced: the supplement weakened the body's own sentence in both directions it
touched.
