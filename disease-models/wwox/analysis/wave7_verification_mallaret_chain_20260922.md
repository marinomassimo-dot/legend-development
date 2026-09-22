# Wave 7 verification — the chain under CLAIM 005, and the paper nobody read

**Actor:** Orchestrator · **Date:** 2026-09-22 · **Status:** verification of a delegate hand-back,
performed before landing. Non-canonical. Nothing here is medical advice.

> Scientist A's Wave 7 returned five items (`F-1`, `F-2`, `F-3`, `C-3`, `C-4`) plus a 🔴 `C-2`
> asserting that a `consolidated baseline` claim contains a false statement. `C-2` touches canonical
> text, so it was verified first and alone. The verification changed the answer twice: `C-2` is a
> false alarm, `F-1` is true but is *not* the finding it was reported as, and the finding underneath
> `F-1` is larger than either.

---

## 1 · `C-2` — false alarm, caught before landing

**Reported:** *"`CLAIM 003` states 'All three links of that chain have since been read in full.'
Verifiably not true of the third link: 19936220 → complete, 19500159 → complete,
**24369382 → partial_fulltext_read, legacy_reconstruction.** Two of three."*

**Two independent defects in the report.**

**(a) Wrong claim.** The sentence occurs exactly once in `claim_registry_current.md`, at line 116,
inside **`CLAIM 005`** (*Reduced GABAergic interneurons and glial activation in WWOX-KO*), not
`CLAIM 003`. Per-file count of the string across the four canonical files:
`claim_registry_current` = 1, all others = 0.

**(b) Wrong chain.** The three links are named explicitly, not in the claim block but in the batch
log that created the sentence — `working_model_current.md:260`, `BATCH_20260806_002`:

> *"The imported-premise chain under CLAIM 005 traced end to end, every link read in full with
> persisted receipts: **PAPER 057** (Ludes-Meyers 2009, PMID 19936220, `FTR-20260806-19936220-01`),
> **PAPER 058** (Suzuki 2009, PMID 19500159, `FTR-20260806-19500159-01`), **PAPER 059**
> (Suzuki 2007, PMID 17803050, `FTR-20260806-17803050-01`)."*

Measured against the ledger:

| PMID | receipt | `record_kind` | `evidence_depth` |
|---|---|---|---|
| 19936220 | `FTR-20260806-19936220-01` | `contemporaneous_receipt` | `complete_fulltext_read` |
| 19500159 | `FTR-20260806-19500159-01` | `contemporaneous_receipt` | `complete_fulltext_read` |
| 17803050 | `FTR-20260806-17803050-01` | `contemporaneous_receipt` | `complete_fulltext_read` |
| 24369382 | `FTR-20260726-24369382-01` | `legacy_reconstruction` | `partial_fulltext_read` |

**Three of three.** `24369382` is a *co-attributed* source named in the preceding sentence, not a
link of the traced chain. **`C-2` must not be landed.**

**But the misreading is the repository's fault, not only the reader's.** The claim block names
**two** of the three links in its own text (`19936220`, `19500159`) and never names `17803050`,
while the sentence immediately before *"all three links"* names `19936220` **and Mallaret 2014**.
A reader with only the claim in front of them assembles the wrong triple — which is exactly what
happened. The third link lives only in a batch-log row 144 lines away in a different file. This is
a wording defect worth repairing (→ `CC-20260922-CLAIM005-CHAIN-NAMING-01`), and it is the second
time this session that a defect reported against the science turned out to be a defect in where the
science is written down.

---

## 2 · `F-1` — true at abstract depth, and it is the most important thing in this wave

**Reported:** Mallaret 2014's abstract asserts mouse seizures, against `CLAIM 005`'s prohibition.

**Verified.** According to PubMed, PMID 24369382 ([DOI](https://doi.org/10.1093/brain/awt338),
Mallaret M, Synofzik M, … **Aldaz CM**, Koenig M, *Brain* 2014;137(Pt 2):411–9) states in its
abstract, verbatim:

> *"Moreover, we observed that the short-lived Wwox knock-out mouse display spontaneous and
> audiogenic seizures, a phenotype previously observed in the spontaneous Wwox mutant rat
> presenting with ataxia and epilepsy, indicating that homozygous WWOX mutations in different
> species causes cerebellar ataxia associated with epilepsy."*

Note **`we observed`** — a first-person observation claim about the mouse null, in a paper
co-authored by **C. Marcelo Aldaz**, whose laboratory produced the knockout.

**This contradicts, head-on, the source the canonical prohibition rests on.** PMID 19500159
(Suzuki 2009) states three times, plus a Table 2 whose `Epilepsy` row is empty for both mouse
models, that Wwox-null mice show no epilepsy. `CLAIM 005` concludes from it: *"No canonical
statement may describe a Wwox-null mouse as showing epileptogenesis."* `CLAIM 037` records the
same, and its evidence boundary does not mention Mallaret at all.

Two papers, both authoritative, flatly opposed on the same animal. The repository decided the
question in Suzuki's favour and issued a prohibition — **without ever having read the body of the
paper on the other side.**

### 2a · The repository already had this, and explained it away wrongly

`disease-models/wwox/research/fulltext_dossiers/PMID30370248.md:71` — a *completed full-text read*
of a review — already caught the review asserting mouse seizures, and diagnosed it as a miscitation:

> *"The body says that Mallaret et al. showed spontaneous and audiogenic seizures in a short-lived
> Wwox-KO mouse. Reference 53 is not a mouse experiment: it is the human SCAR12 paper. … the
> sentence points to the wrong species and source."*

🔴 **That diagnosis is wrong, and it is wrong in the direction that suppressed the conflict.** The
review's citation is *faithful*: the human SCAR12 paper does report a mouse observation, in its own
abstract, in the first person. The review inherited the claim from Mallaret rather than inventing
it. What the dossier established — that reference 53 is a human genetics paper — is true and is not
the same thing as establishing that no mouse experiment is behind the sentence.

So the correct state of the question is not *"a review miscited a human paper"*. It is: **a 2014
*Brain* paper co-authored by the maker of the mouse claims to have observed seizures in it; nobody
in this repository has read that paper's body; and a canonical prohibition was written as though
the matter were settled.**

### 2b · Why nobody read it, measured rather than assumed

`get_copyright_status(["24369382"])` — `checked_sources: ["pubmed","pmc"]`, so PMC *was* consulted:

```
license.is_open_access: false
copyright.statement: "© The Author (2013). Published by Oxford University Press on behalf of
                      the Guarantors of Brain. All rights reserved."
pmc_id: PMC3914474   (deposit exists; body not licensed for retrieval)
```

**This is a paywall, not a route failure** — the distinction this session has had to draw twice
before, in the opposite direction (PMID 36779245 Table S1 was open access and therefore a route
problem). A PMCID exists and is not a body: the fifth instance of that trap this session, and the
first where the cause is licensing rather than an empty stub.

Consequence: `24369382` **cannot be read in full by any route available to this actor.** Acquiring
it is a human action. That is `HUMAN_REQUIRED` in the purchasing sense only — and per §27 a tool or
access boundary is not a scientific stop. The science that can proceed without it proceeds.

### 2c · What changes, and what does not

- ❌ The prohibition is **not lifted**. An abstract is not a read, and a first-person sentence in an
  abstract is exactly the kind of assertion this repository refuses to promote — the Tochigi
  precedent (`LIT-0405`, *"decreased plasma GH"* refused as a reading, and the body reported it as
  not significant) is the governing example.
- ✅ The prohibition's **status** changes: from *settled against the mouse* to **contested, with the
  contesting evidence unread and paywalled**. `CLAIM 005` and `CLAIM 037` currently give a reader no
  hint that a later paper asserts the opposite. That is the defect.
- ✅ A `REVIVAL_TRIGGER` is warranted on both claims: *acquisition of PMID 24369382's body*.
- ✅ The testable question sharpens. Suzuki's own escape hatch — the mice may die before seizing —
  is now joined by a second, symmetrical possibility: **the mice may seize and Suzuki's cohort may
  not have been watched in the way Mallaret's was** (audiogenic stimulation is a provocation, not an
  observation; 19500159's rat result is 19/20 *on stimulation*). Neither paper's methods section has
  been compared on **how the mice were observed**, because one of them has never been opened.

---

## 3 · `F-2` — rediscovery of something the repository holds in a stronger form, and a correction to my own first verdict

**Reported:** *"P47 is a buried fold-stabilising core residue yet P47T has normal protein — weakens
the burial ⇒ destabilisation ⇒ degradation inference in `DL-BIO-001`/`HYP-20260709-08`."*

### 3a · The premise as stated is false, by this repository's own measurement

`discovery_ledger_current.md` `DL-MECH-037` records the pipeline output on AlphaFold `AF-Q9NZC7-F1`:

| variant | domain | relSASA | burial | SSE | pLDDT | d(triad) | ΔΔG | protein | phenotype |
|---|---|---:|---|---|---:|---:|---:|---|---|
| **P47T** | WW1 | **0.286** | **partially exposed** | β-strand | 82.3 | 51.4 Å | **+2.81** | **normal** | mild |
| **P47R** | WW1 | 0.286 | partially exposed | β-strand | 82.3 | 51.4 Å | +2.53 | n.d. | **severe** |
| **Q230P** | SDR | **0.000** | **buried (core)** | **α-helix** | 98.5 | 8.2 Å | +1.51 | **absent** | severe |
| **G372R** | SDR | 0.163 | partially exposed | β-strand | 93.8 | 17.8 Å | +1.58 | nearly absent | mild |

**P47 is not buried.** Scientist A took *"part of the hydrophobic core that stabilizes the WW fold"*
from Mallaret's abstract and read a paper's prose assertion as a burial measurement. The finding
must not be landed in the form reported.

### 3b · 🔴 And my own first verdict on it was wrong — recorded here rather than quietly dropped

Having found `CLAIM 033`'s four-word summary `il ΔΔG non discrimina`, and having found `DL-MECH-033`
(2026-07-10) setting up a two-branch in-silico test and calling it *"il prossimo passo in-silico
prioritario"*, I drafted the conclusion that **the experiment was run, the answer landed in the
claim registry, and nobody propagated it back** — a seventh instance of "existence in the wrong
place", and one that would have weakened `TX-003`.

**That is false. I checked before writing it up, and the check found me at fault.** `DL-MECH-037`,
87 lines below `DL-MECH-033` in the same file, *is* the propagation, and it is more careful than
what I was about to write:

- **Finding 1 — ΔΔG predicts neither abundance nor severity.** With a control better than mine:
  **the same residue**, P47T (ΔΔG **+2.81**, the highest of all four) → mild, protein normal; and
  **P47R** (ΔΔG +2.53) → **severe**. *"Il ΔΔG più alto ha il fenotipo più lieve."* My version used
  P47T against Q230P — two different residues. The repository's uses one residue against itself.
- **Finding 2 — the consequence I had not thought to draw.** The *"recoverable window"* heuristic
  (ΔΔG 0.8–3.5) classifies **all three** variants as `stability (rescuable window)` while their
  phenotypes diverge ⇒ the window has no demonstrated predictive value, and the argument
  *"7/13 pathogenic ClinVar missense fall in the recoverable window, therefore misfolding
  dominance"* — **cited in `CLAIM 019` in support of the proteostatic hypothesis** — is explicitly
  demoted there.
- **Finding 3 — what *does* discriminate.** Burial. And it resolves the P47T anomaly rather than
  merely recording it: P47 sits **51 Å from the active site**, in an autonomous WW1 module, so its
  lesion is **functional** (PPxY binding abolished, Mallaret's pull-down) **and not structural** —
  *"ed è esattamente per questo che la proteina P47T è presente a livelli normali. La serie torna."*
- **And a caution on `TX-003` sharper than the one I intended to propose:** a **buried proline in an
  α-helix imposes a backbone constraint a chaperone cannot remove** — *"un chaperone favorisce il
  raggiungimento di uno stato foldato, non cambia la chimica del backbone"* — so the open question
  is whether a folded *and catalytically active* state exists for Q230P at all. With the two sides
  weighed (8.2 Å from the triad, so perturbation by proximity not contact; against 22 heavy contacts
  within 5 Å in a dense core) and the honest verdict that neither is decisive in silico.
- **Plus a designed negative control I did not have:** run the proteostatic rescue **in parallel on
  Q230P and G372R**. If the surface lesion responds identically to the core lesion, the structural
  model is false and the rescue is a non-specific chaperone artefact.

**So `F-2` is a rediscovery, and my escalation of it would have been a false finding.** The rule
that caught it is the one I have been applying to delegates all session — *check the repository
before reporting anything as absent* — and this is the first time this session it has caught **me**
in the act of writing a claim rather than after the fact. It goes in the census as `self`,
`severity_high` (it would have reached a commit candidate), `undetected_known: 0`.

**No commit candidate is raised from `F-2`.** There is nothing to propagate. `D-26` is withdrawn
before it was written.

### 3c · The one real residual — a missing forward link, worth one line

`DL-MECH-033` still presents the two-branch test as *"il prossimo passo in-silico prioritario"* and
its `Interconnessioni` list names `CLAIM 019`, `CLAIM 007`, `CLAIM 008`, `DL-MECH-026`,
`HYP-20260709-08` and `RC-013` — **not `DL-MECH-037`**, the entry that performed the test. A reader
landing on `033` is told an experiment is pending; the entry saying it was done and what it returned
is 87 lines away with no pointer. That is navigational, not scientific, it is on a research surface
rather than a canonical one, and it was **directly encountered by this wave's work** — which is the
Operator's stated condition for repairing a defect in place rather than queueing an audit. Repaired
as a dated append-only line. **No audit is opened; no gate is added.**

## 4 · `F-3`, `C-3`, `C-4` — accepted as reported

- **`F-3`** MeSH strain indexing (`Mice, 129 Strain`, `Mice, Inbred C57BL` on 24369382) is index
  metadata, not a background comparison. **The Wave 4 negative stands.** Confirmed against the
  metadata record: both terms present, no comparative statement anywhere in the abstract. Worth one
  line in the queue, nothing more.
- **`C-3`** The discriminating trait of a legacy record is *absence of dossier + absence of manifest*
  (13/22). Consistent with `24369382`, which has neither and is the case in hand.
- **`C-4`** `get_copyright_status` as a one-call pre-test before attempting a body: **5/5 this
  session, now 6/6** — this wave's call returned `is_open_access: false` *before* any fetch was
  attempted, converting what would have been three failed acquisition routes into one measurement.
  This is a genuine, cheap, disease-agnostic method upgrade and should be written into the
  acquisition path rather than left in a hand-back.

---

## 5 · Census of this verification

| item | reported as | verified as |
|---|---|---|
| `C-2` | 🔴 false statement in `CLAIM 003` | **false alarm** — wrong claim *and* wrong chain; 3/3 read in full |
| `F-1` | abstract contradicts a prohibition | **true, and larger**: the contradiction was already in a dossier and was explained away wrongly |
| `F-2` | P47 buried, weakens the inference | **premise false and finding already held**: P47 is surface (relSASA 0.286), and `DL-MECH-037` holds the whole result in a stronger form |
| *(my own escalation of `F-2`)* | *"the experiment was run and never propagated"* | 🔴 **false — caught by checking before writing.** `DL-MECH-037` is the propagation |
| `F-3` | MeSH ≠ background comparison | confirmed |
| `C-3` | legacy trait = no dossier + no manifest | confirmed |
| `C-4` | copyright pre-test | confirmed, 6/6 |

**Two of six delegate items required correction before landing, and a third item — my own
escalation of `F-2` — was false and was caught in the act of being written.** The standing rule
held in both directions: *never trust a delegate census without a repository check*, and the same
check applies to the coordinator. It has now paid out five times this session; twice it found the
repository at fault rather than the delegate, and once it found me.

```
ATTRIBUTION_CENSUS
incidents: 3
machine: 0   blind_auditor: 0   peer: 0   self: 3
severity_high: 1   of which self: 1
undetected_known: 0
```

`severity_high: 1` is the `F-2` escalation: it was headed for a commit candidate under `D-26` and
would have reached the record. The two delegate corrections (`C-2`, `F-2`-as-reported) were refused
by a writer and are not high. `undetected_known: 0` reports the limit of this census, not the
absence of defects in it.

**`UNREAD_PREMISE` impact:** none. `24369382` was already `partial_fulltext_read` /
`legacy_reconstruction` before this wave and remains so; no premise is newly imported, and the
count does not regress from 0. What changes is that a canonical claim will now *say* that one of
its co-attributed sources is unread and says the opposite — which is a decrease in hidden debt,
not an increase in declared debt.
