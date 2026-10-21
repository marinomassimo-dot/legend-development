# Roadmap P4, RECUPERO_PROFONDO: the first candidate cards and abstentions

> **Actor** `scientist-a` · **Task** `REPURP-10H-P4-DEEP-A-20261022` · 2026-10-21. Non-canonical research
> record. It touches none of the four scientific current files, `disease_model.md`,
> `framework/scripts/repurposing_bridge.py` or any file of `drug_repurposing/` outside `cards/`.
> **Not medical advice.** Class level, public disease-level material. No dose, route, schedule or
> paediatric suitability appears in the cards or here; nothing is ranked or scored. Every adjacent
> source is **NOT WWOX EVIDENCE**. The deliverable is in
> [`drug_repurposing/cards/`](drug_repurposing/cards/README.md).

## 1 · What was done, and what was not

Twelve input packets in the bridge's JSON shape and the twelve cards the bridge builds from them:
**5 cards and 7 abstentions**, over four axes, the Q230P-class recovery axis first. This was not a
literature sweep and **no paper was opened**: the material is the five notes of the contract, the
roadmap's P4 table (a plan, not an authority), the bridge's note and code, and the claim and
discovery records the notes cite, fetched by `registry_records.py` for the two facts a packet needs as
its disease assertion (CLAIM 019 and DL-THER-089). No panel decided a card, so no
`QUESTION_DRIVEN` reading, no staged receipt and no reading claim exist for this task.

| Axis | Cards | Abstentions |
|---|---|---|
| A · Q230P-class missense recovery | `P4-A-01` 4-phenylbutyrate and bile-acid chaperone class (controversial); `P4-A-02` proteasome-inhibitor class (hypothesis) | `P4-A-03` client-binding chaperone; `P4-A-04` ER-proteostasis regulators; `P4-A-05` HSP70-axis modulation |
| B · premature-stop-codon read-through | `P4-B-01` amlexanox (deferred with reason) | `P4-B-02` read-through class for nonsense alleles |
| C · restoration of WWOX expression | `P4-C-01` AAV9-delivered human WWOX (hypothesis) | `P4-C-02` splice-correcting ASO / editing; `P4-C-03` endogenous boost |
| D · downstream pathway (Wnt/MYC) | `P4-D-01` A51, BLOCK-1 open (controversial) | `P4-D-02` Wnt-lowering agents and GSK3 modulation |

The statuses are the roadmap's own vocabulary (hypothesis, controversial, deferred with reason,
abstention) and are labels for a reader, not a ranking.

## 2 · What each card makes visible that was not visible before

**`P4-A-01` the chaperone class (the Q230P axis).** Three things R1 measured sit side by side and
are easy to read apart. The class behaves as a chaperone of the *fully* ER-retained branch (GAT-1
G443V rescued with protein and function read together; a fly seizure-like phenotype down) and not of
the partly trafficked one (G443D, same compound, no rescue). It **also raises the wild-type protein
in every target of the lot**, so the effect is not variant-specific. And its non-rescuing results
(G443D; a null-allele zebrafish with protein not measured; an HDAC-inhibitor comparator that raised
the immature pool without function) mean the evidence for *chaperoning* rather than *raising the
expression of the cDNA* is inferential. The card adds the objection the three do not state: the
precedents concern membrane or secretory-pathway clients, WWOX is cytosolic, and the repository
withdrew this class once for a wrong-compartment rationale (DIS-004) whose revival trigger is live.
That transfer objection is INFERENZA and **owed a blind audit**. Nothing is known about where Q230P
is lost: its only measurement is "transcript comparable, protein not detected" in one patient
fibroblast line, one membrane, no healthy control, and no inhibitor, chaperone, solubility or
half-life datum exists.

**`P4-A-02` the proteasome-inhibitor class.** The closest recovery precedent in R1 (a recessive
missense protein, "normal mRNA, protein absent", returned from undetectable to about a fifth of
control in patient oligodendrocytes, with two function-adjacent readouts) comes with its own bound:
the working exposure window is toxic to all genotypes outside it, controls included. The card also
carries the opposite case (a stabilised, insoluble, inactive enzyme). It is a probe to place the
lesion, not a candidate, and the card says so by status `hypothesis` conditional on an unmeasured
route.

**`P4-A-03/04/05` abstentions.** A client-binding chaperone needs a ligand of the WWOX SDR domain
and a measured instability to stabilise (no experimental SDR structure exists). ER-proteostasis
regulators need Q230P to be placed in ER or cytosolic quality control at all. HSP70-axis modulation
has no known sign for this lesion (an arimoclomol-type candidate was withdrawn the same day; blocking
the axis in the adjacent enzyme gave insoluble inactive protein). Each names the datum that would
end it.

**`P4-B-01` amlexanox.** The molecule is qualified and not promoted, and the card shows why in
structure rather than in effect size: the reference missense has no premature stop codon, so
read-through is not a mechanism for it at any exposure. For nonsense alleles the eligible class
has never been counted (`P4-B-02` names the enumeration, with stop identity and the +4 nucleotide).
The one independent comparator-controlled study found no phenotypic rescue and no relief of NMD.
Its own authors' sentence is carried verbatim. The foundation-reported individual experience and the
poster abstract are one narrated experience and one uncontrolled account of it, not two replications.

**`P4-C-01` AAV9-WWOX.** The card keeps the three limits the CLAIM 011 narrowing established: a
**threshold, not a continuum** for survival (two points cannot locate it; an equality between unequal
denominators on body weight is not grading); spike-wave discharge measured at **one** level only, so
it cannot support a dose-dependent claim; myelination never quantified in a treated arm and gliosis
binary against wild type with no untreated-null comparator in the quantified treated panels. It adds
what a rescue in a *null* does not say about a *missense*: residual partial function is a reason to
expect a different result, not a larger one. Replication is absent (the two papers share a senior
author and institution), there is no tumour surveillance in a pro-apoptotic tumour suppressor, and
later treatment ages are NOT_MEASURED, which is not "smaller". Access is carried as two separate
facts: a programme with a gene-therapy objective for WOREE is recorded at grant level; no
registered WOREE interventional study exists on that registry on that date; whether that programme's
construct equals the mouse construct, sponsor-declared authorisation, enrolment and first dose are
all UNKNOWN.

**`P4-D-01` A51.** The bridge's only `OPPOSES_DISEASE_CHANGE` among the organoid rows is the
progenitor-identity endpoint; the second assertion (layer neurons, measured no recovery) cannot be
compared and the summary is therefore UNRESOLVED. That is the point of the card: the favourable
match hides the non-match. It carries BLOCK-1 open (Wnt is required for progenitor proliferation
and cortical patterning, and the window between removing excess progenitors and preventing normal
corticogenesis is measured nowhere), the ambiguity of attribution (two pathways suppressed; the
leukaemia paper does not separate Wnt, MYC and CDK), the adult-only human exposure record with no
paediatric record at all, and the point that its panel values can no longer be re-audited. The link
between the organoid compound and the clinical-stage agent is carried from the R3 note and not
verified here. `P4-D-02` records that no Wnt-lowering agent has been given to any WWOX system and
that "lower MYC/Wnt is better" is not a safe default.

## 3 · Gaps in the bridge exposed by building the cards (not patched by me; a Harness agent owns it)

Updated 2026-10-22: the first build exposed three gaps; Harness commit `b96e4cd9` closed two of them
before the cards landed, and the cards were rebuilt.

- **G-1 · the bridge could not represent a measured null: CLOSED by `b96e4cd9`.** `direction` had no
  value for "not significant, not rescued", so five measured nulls had to be entered as UNKNOWN,
  which reads as *owed*. The bridge now has `NO_CHANGE`; the five assertions (`DR-A01-003`,
  `DR-A01-004`, `DR-A02-003`, `DR-B01-002`, `DR-D01-002`) use it, and in a non-comparable cell the
  card says "a measured null, not an unmeasured cell".
- **G-3 · `translation` had no input path and P4 rows had no home: CLOSED in the part that mattered.**
  `translation` (with `access` and `time_to_benefit`) is now filled from the packet, and the two roadmap
  rows `indication_and_transfer` and `verification_scope` are validated. The other roadmap fields
  still travel as untyped extra keys that the bridge keeps unchanged and does not validate
  (`check_cards.py` compensates locally); and `access` still stands for time to access under a name
  that does not say so.
- **G-2 · one `disease_assertion` per packet: STILL OPEN, and now the one gap.** A multi-endpoint
  candidate (AAV9: five endpoint families; A51: progenitors and layer neurons) can have only one
  endpoint compared; every other measured endpoint is forced to `UNRESOLVED` with "endpoint:
  mismatch or unknown", which reads as a context failure although the data exist. The cards keep the
  other families in `p4_card` and out of `drug_assertions`. Precisely what is missing: a list of
  disease assertions keyed by endpoint, each compared only with the drug assertions on the same
  endpoint.

## 4 · DEFAULTS_TAKEN, OWED, STOP

- **Disease assertions chosen** per axis: the Q230P fibroblast protein endpoint (CLAIM 019) for the
  axis A and B cards; spike-wave discharge rate in the null mouse for AAV9; the progenitor fraction
  in the knockout organoid for A51. Context strings differ on purpose, so cross-system rows resolve
  to `UNRESOLVED`; this is the bridge working as designed.
- **Understated depths.** The A51 organoid reading is held at `UNKNOWN` depth because the sources do
  not restate it; measured nulls are `NO_CHANGE` after the bridge change (G-1, now closed in the bridge).
- **Out of scope, not discarded.** BENEFICIO_PRECOCE candidates (ethosuximide, lithium, pro-myelinating
  agents, mTOR and symptomatic agents) are not carded. Lithium's relevant negative on specificity and
  its Wnt-direction conflict are in the known-roads note and would be a natural controversial-direction
  card for the other path.
- **Treatment ages, vector quantities, concentrations and exposure windows** of the sources were
  generalised or omitted on purpose.
- **OWED, blind audit by someone else:** every card-level synthesis sentence and, first, the
  statements marked INFERENZA (the wrong-compartment transfer objection on `P4-A-01` and `P4-A-04`;
  the reading of the A51 split as "hides a non-match"; the encoding of measured nulls). The cards
  also inherit the OWED audits of R1 and R3; the audit of some R1 triples running in parallel was not
  available. No claim is narrowed in a registry by this task.
- **Not verified here:** the identity of the organoid compound with the clinical-stage agent; that
  the grant-level gene-therapy programme uses the mouse construct; receipt ids are checked for
  presence in the ledger, not re-verified.
- **STOP_LOG:** empty. No operator-reserved act was needed.

## 5 · A question for discussion with a treating team (not advice)

If one card were brought to a clinician first, **`P4-C-01`** is the candidate, and only because it is
the card on which the facts are most complete and the unknowns most decision-relevant, not because it
is the best: it holds the only measured rescue in the repository, and also the clearest statement
that the rescue is a threshold in a null, unreplicated, with access and benefit timing unknown.
The question it could put to a team is: *given that the only measured rescue comes from a
constitutive-null mouse, from one laboratory, with a high level that works and a lower one that only
postpones, what would the team want to have seen (an independent replication, an intermediate level, tumour
surveillance, and above all a result in a missense context) before discussing it for a child with a
Q230P-class genotype, and how should an unknown time to access weigh in that discussion?* The Q230P
cards come first in the set but have nothing a clinician could discuss other than what is not known,
which is itself the result they are for.

## 6 · Self-evaluation (short form; the full diagnosis is under `session_evaluations/`)

The upgrade the work forced was the bridge's missing representation of a measured null (G-1), written
where the Harness agent found it; it is now closed and the cards rebuilt with it. The failure this batch
risked most was making a card look like a result: `OPPOSES_DISEASE_CHANGE` on `P4-C-01` and `P4-D-01`
reads as good news, so each carries a `reading_guard` and the A51 card shows the non-match next to
the match. A second risk, naming a first author the notes did not give, was caught on a self-review
before the run and removed.

## 7 · After the R1 blind audit (2026-10-22)

The audit of the R1 manifests overshot 15 triples, among them all three behind the PB-4 narrowing. No
card of this set cites PB-4 or the polysome limitation; the corrected R1 statements that the cards use
(butyrate as a partial, variant-dependent dissociation; a binding or folding measurement "not
established here"; the Parkin negative as one compound, one concentration, a pooled readout) were
carried into `P4-A-01` and `DR-A01-005`. The repairs are unaudited; the cards inherit that.
