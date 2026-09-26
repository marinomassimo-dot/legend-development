# Record Repair Queue — defects found in the record, and what fixes each one

> **Public edition — de-identified, disease-level.** No identified person, no report or sample
> identifier, no institution, no family-relationship data. **Not medical advice**, and no dose, route
> or schedule appears here by design.
>
> **Research layer — non-canonical. READ-ONLY toward the four canonical current files.** This file
> *records* repairs; it does not perform the gated ones. A repair that touches
> `working_model_current.md`, `claim_registry_current.md`, `paper_registry_current.md` or
> `literature_tracking_log_current.md` still goes through `BATCH_COMMIT` under `LINT` — that is
> method, not ceremony (LEGEND_CORE §21e).
>
> Created: 2026-09-26 · Created by: Harness Engineering, at the operator's instruction, under §21e (T0).

---

## Why this is a queue and the experiment ledger is a ledger

A defect is **consumed**: it is fixed, verified, and leaves. An experiment **accumulates**: its record
persists after the run, carrying its result. Opposite lifecycles, so two files —
[`experiment_ledger_current.md`](experiment_ledger_current.md) accumulates, this one drains. They were
deliberately not merged: merging two files later is easy, splitting one is not.

**A row is closed only with its verification named.** "Fixed" without a check is how a defect returns.

### Schema

```
ID        REP-NN             stable, never reused
LAYER     model | harness    which layer owns it
SEVERITY  invalidates-an-experiment | contradiction | missing-artefact | over-claim | stale | preventive
FIX       the specific edit or acquisition
VERIFY    the command or observation that closes the row
PATH      T0 | BATCH_COMMIT | RECEIPT | ACQUISITION
STATUS    OPEN | IN_PROGRESS | CLOSED (with the verification) | WONT_FIX (with the reason)
```

🔴 **Count note, stated rather than smoothed:** the operator was told *fourteen* while five of six
delegated streams had reported. The last two streams and this session's own verification raised it to
**17 actions plus 1 verified-clean**. The number in a report is a measurement at a moment, and it is
recorded moving rather than retro-fitted.

---

## Index

| ID | Layer | Severity | One line | Status |
|---|---|---|---|---|
| `REP-01` | model | 🔴 invalidates-an-experiment | The catalytic serine is the wrong residue, by 17.9 Å | `OPEN` |
| `REP-02` | model | 🔴 contradiction | Two files disagree on whether a fibroblast reporter exists | `OPEN` |
| `REP-03` | model | 🔴 missing-artefact | A supplement declared read cell-by-cell is not in the tree | `OPEN` |
| `REP-04` | model | 🔴 over-claim | The only scalable readout rests on a review, primary not found | `OPEN` |
| `REP-05` | model | 🔴 receipts | Three full texts read this session, no receipts recorded | `OPEN` |
| `REP-06` | model | contradiction | A 2025 genotype–phenotype source is carried in half | `OPEN` |
| `REP-07` | model | over-claim | A bacterial-SDR property attributed to WWOX downstream | `OPEN` |
| `REP-08` | model | over-claim | "The Δexon-7 product cannot fold" is unsupported | `OPEN` |
| `REP-09` | model | preventive | A non-WWOX structure must never be admitted as WWOX | `OPEN` |
| `REP-10` | model | over-claim | A wrong reason given for a right primer choice — mine | `OPEN` |
| `REP-11` | model | method | Measure location and state, not abundance | `OPEN` |
| `REP-12` | model | 🔴 safety | The tumour axis is a gate, and it is triply supported | `OPEN` |
| `REP-13` | model | status | The lead candidate moves — in both directions | `OPEN` |
| `REP-14` | model | over-claim | One agent's precedent is regulatory, not mechanistic | `OPEN` |
| `REP-15` | **harness** | 🔴 stale | An egress assumption is suspending real work | `OPEN` |
| `REP-16` | **harness** | 🔴 stale | "No full text in PMC" is an XML verdict, not a full-text verdict | `OPEN` |
| `REP-17` | model | stale | Structural coordinates are four versions behind | `OPEN` |
| `REP-18` | model | ✅ verified-clean | Retraction hygiene checked and correct — recorded so it is not re-opened | `CLOSED` |

---

## REP-01 · 🔴 The catalytic serine is the wrong residue, by 17.9 Å

**LAYER** model · **SEVERITY** invalidates-an-experiment · **PATH** `T0` for the analysis surfaces,
`BATCH_COMMIT` for any canonical heading that repeats it

**What is wrong.** This repository and the wider field name **`Ser281`** as WWOX's catalytic serine.
Measured this session on `AF-Q9NZC7-F1` v6 **and** on the v2.0 coordinates the repository holds,
identical to the hundredth of an ångström:

| | |
|---|---|
| `Ser281` OG → `Tyr293` OH | **17.85 Å** |
| `Ser281` OG → `Lys297` NZ | **16.70 Å** |
| **`Ser260` OG → `Tyr293` OH** | **4.44 Å** |
| `Asn232` ND2 → `Lys297` NZ | 4.80 Å |
| `Tyr293` OH → `Lys297` NZ | 4.17 Å |

`Ser281` cannot participate in catalysis at that distance. The tetrad is
**`Asn232 – Ser260 – Tyr293 – Lys297`**, and `Ser260` sits 33 residues before the catalytic tyrosine
— the spacing a short-chain dehydrogenase/reductase with an insertion in its fold would give.
Independently, UniProt annotates residue 260 as a substrate site, and the repository's **own**
first-shell cleft list already contains `S260 4.19` and **omits `S281` entirely**. The evidence was
in the file.

**Provenance of the error.** The source (PMID 24932569, PMC4151823) says the residues were
*"predicted to be required"*, attributes the data to **unpublished observations**, and its readout was
**perinuclear localisation** — no catalytic activity was measured. A prediction became a fact in
transmission.

🔴 **Why this is the most operationally expensive row in the list.** Any future experiment needing a
catalytic-dead control would have used **`S281A`** — a negative control 17.9 Å from the active site,
masquerading as a catalytic one. It would have appeared to work, because it would have shown no
catalytic change, and nobody would have known why.

**FIX** — Correct the residue in every surface that names a catalytic serine. Record the tetrad.
State in one line that a catalytic-dead arm is **`N232A` / `S260A` / `Y293F` / `K297A`**.
Cross-reference `EXP-20260926-Q230P-SUBSTITUTION-01`, whose control arm depends on it.

**VERIFY** — `grep -rn "S281\|Ser281" disease-models/ framework/` returns no surface asserting
catalysis, and every remaining occurrence carries the correction.

---

## REP-02 · 🔴 Two files disagree on whether a fibroblast reporter exists

**LAYER** model · **SEVERITY** contradiction · **PATH** `T0`

**What is wrong.** `analysis/wwox_activity_sensor_census_20260921.md` scores PMID 35328751 as
*"no reporter construct"* and *"abstract-level"*. `analysis/wwox_metabolism_reviews_audit_20260921.md`,
which read the body, **records its HRE-luciferase reporter**. The paper has one: an HRE reporter with
a Renilla control, four enzyme-activity assays, fractionation of endogenous WWOX with purity controls,
and quantified immunocytochemistry, in **human skin fibroblasts** with knockout and cDNA arms.

The file that answers *"does a WWOX reporter exist?"* excludes the only fibroblast one, and nobody
reconciled the two. That is the highest operational cost of any contradiction in the record, because
the census is the file a future session would consult.

**FIX** — Reconcile to the body-reading. Re-score the record. Add the reagent used there
(`PA5-29701`), which appears nowhere in the 17-row antibody census; its epitope is unknown and is
resolvable by that census's own fragment-competition design.

🔴 **Carry the bound with the fix:** that reporter reads a **WW1-mediated** interaction, so a rescue
producing SDR-inert but WW1-competent protein would **pass** it. It is a necessary-condition gate —
fail ⇒ dead, pass ⇒ *not shown to work*. See `EXP-20260926-SDR-INTEGRITY-READOUT-05`.

**VERIFY** — both files state the same score, and the census row names the reporter and the bound.

---

## REP-03 · 🔴 A supplement declared read cell-by-cell is not in the working tree

**LAYER** model · **SEVERITY** missing-artefact · **PATH** `ACQUISITION`

**What is wrong.** `files/fulltext/PMID36779245_Oliver2023_suppl_TableS1.xlsx` is **absent** — 139
files in that directory, none matching. Two analysis files depend on it:
`analysis/oliver2023_tableS1_and_q230p_cohort_map_20260923.md` carries a `sha256`, and
`analysis/q230p_person_count_reconciliation_20260923.md` cites it as *"read cell-by-cell this
session"*. It closes the central arithmetic of the missense-class contrast.

**A declaration is not an attestation.** The recorded hash is a claim about a file that is not here to
be hashed.

**FIX** — Re-acquire the supplement (open access), verify the recorded `sha256`, and place it at the
declared path. If the hash does not match, that is a second and larger finding.

**VERIFY** — `sha256sum` of the placed file equals the value recorded in the analysis file.

---

## REP-04 · 🔴 The only plate-scalable readout rests on a review

**LAYER** model · **SEVERITY** over-claim · **PATH** `T0`

**What is wrong.** *"Golgi localisation requires an intact SDR domain"* is the load-bearing citation
for the only continuous, plate-scalable, SDR-integrity-dependent readout available — the closest thing
to an amenability assay this programme could build. It is sourced to **PMID 14526170, which is a
review** by the same laboratory. The primary source was searched on PubMed this session
(`WWOX AND Golgi`) and **not found**: the hits are the review, a rat testicular-development paper, a
2018 interactome paper, and unrelated records.

**FIX** — Either locate the primary and record it with its read depth, or downgrade the claim to
review-depth and say so wherever the readout is proposed. Do not build an assay programme on it until
one of the two is done.

**VERIFY** — the readout proposal in `EXP-20260926-SDR-INTEGRITY-READOUT-05` names either a primary
source or an explicit review-depth label.

---

## REP-05 · 🔴 Three full texts were read this session and no receipts were recorded

**LAYER** model · **SEVERITY** receipts · **PATH** `RECEIPT`

**What is wrong.** Three readings happened and none is persisted, because the reading actors are
read-only toward `framework/` and could not record.

| Source | Depth achieved | What it carries |
|---|---|---|
| PMID 30202070 / PMC6131187 | full text | The verbatim non-functional-accumulation passage and the EndoH/trafficking result behind `REP-11` |
| PMID 24891511 / PMC4094081 | **full text with all 8 figures at 300 dpi** | The abundance-and-function rescue behind `REP-13`. Saved to `files/fulltext/PMID24891511_Nakasone2014_PMC_2026-09-26.html` |
| PMID 24932569 / PMC4151823 | full text | The provenance that resolves `REP-01` |

**FIX** — `python3 framework/scripts/fulltext_receipts.py record` for each, with `verbatim_locators`.
🔴 Hand-editing the ledger breaks its hash chain and halts LEGEND — use the tool.

**VERIFY** — `python3 framework/scripts/fulltext_receipts.py verify` passes, chain intact, and the
state-manifest tail anchor matches.

---

## REP-06 · A 2025 genotype–phenotype source is carried in half

**LAYER** model · **SEVERITY** contradiction · **PATH** `BATCH_COMMIT`

**What is wrong.** PMID 40875931 (*Neurology* 2025) replicates the severity gradient for **morbidity**
— hypertonia, seizures, respiratory complications, by allele class **56.8 % / 29.5 % / 13.6 %** —
while **mortality is not significant, p = 0.432**. The repository records the second half only. A
source carried in half argues for whichever half is quoted.

**FIX** — Record both halves in the same row, so neither can travel alone.

**VERIFY** — the record names the morbidity replication and the mortality non-significance together.

---

## REP-07 · A bacterial-SDR property is attributed to WWOX downstream

**LAYER** model · **SEVERITY** over-claim · **PATH** `T0`

**What is wrong.** The 28-amino-acid insertion into the Rossmann fold, the αE/αF masking and the
blocked four-helix bundle come from PMID 17258342, which is about **3α-hydroxysteroid
dehydrogenase/carbonyl reductase from *Comamonas testosteroni*** and **does not mention WWOX**.
`analysis/q230p_structural_mechanism_20260922.md` §5.2 attributes it correctly; the transfer to WWOX
happened downstream — and this session's orchestrator repeated it in a delegate briefing and in an
operator report before the misattribution was caught.

**FIX** — Label every WWOX statement built on it as a **transferred prior**, not a WWOX property.

**VERIFY** — each occurrence carries the transfer label and the source organism.

---

## REP-08 · "The Δexon-7 product cannot fold" is unsupported, and the true bound is different

**LAYER** model · **SEVERITY** over-claim · **PATH** `T0`

**What is wrong.** `D-30` states the exon-7-skipped product *"cannot fold"*. An in-frame SDR deletion
three times larger **is made and mislocalises to the nucleus** — worse, not absent. And the measured
bound this session is sharper than either: Δexon-7 deletes the putative catalytic **`Ser260`** and
eight cofactor-pocket-wall residues (`V208 C209 N210 A211 A212 H236 V258 S259`) while retaining both
WW domains ⇒ **SDR-dead, WW-competent.**

**FIX** — Withdraw *"cannot fold"*. Substitute the measured bound.

**Carry with it, because it settles a therapeutic question:** enforced exon-7 skipping is
`REFUTED-AS-THERAPY, RETAINED-AS-MEASUREMENT`. It would remove the domain whose partial loss is mild
and destroy the one that tracks severity — and the natural experiment has run: the exon-7 acceptor
allele `c.606-1G>A` is carried homozygously by five patients who all died before their third birthday
(PMID 26345274). 🟢 **The repository already holds that mortality**, in
`analysis/splice_allele_rna_evidence_20260922.md`, with the correct hedge that losing an acceptor does
not compel skipping — a delegate claimed otherwise and was wrong.

**VERIFY** — `D-30` no longer asserts unfoldability, and the skipping verdict names both halves.

---

## REP-09 · A non-WWOX structure must never be admitted as WWOX

**LAYER** model · **SEVERITY** preventive · **PATH** `T0`

**What is wrong.** `1WL8` is cited by a reagent vendor's page beside a WWOX antibody. Verified at
RCSB: it is **GMP synthase subunit A of *Pyrococcus horikoshii***, an archaeal glutamine
amidotransferase, deposited 2004 by a structural-genomics consortium, no PubMed identifier. The likely
origin is a transcription slip from the mouse WWOX accession `Q91WL8`.

**The only experimental WWOX structure in existence is `1WMV`** — solution NMR of **WW2 alone**,
roughly residues 51–101. **The SDR domain has zero residues of experimental coverage.**

**FIX** — Record the negative now, so the citation cannot be admitted later. This is the same failure
class as reading an index term as an experiment, which this repository has already made twice.

**VERIFY** — a dismissal-ledger row exists for `1WL8`, and the structural surfaces state that SDR
experimental coverage is zero.

---

## REP-10 · A wrong reason given for a right primer choice — this session's own

**LAYER** model · **SEVERITY** over-claim · **PATH** `T0`

**What is wrong.** The orchestrator described the exon 4→9 cross-pair as uniquely unable to amplify
genomic DNA, and offered it as an advantage. Measured from `NG_011698.1`: **all four pairs span
≥ 271 kb of intron** and are equally genomic-incompatible — the published exon 4→8 pair spans
**316,951 nt**, the cross-pair 1,095,806 nt, and both of the original pairs 271,598 and 778,855 nt.

The preference for the published pair stands on its real reasons: it is published and working, its
melting temperatures are paired, and it resolves a 31 % shift against 21 %.

**Recorded because of its shape, not its size.** The wrong reason **did not change the conclusion**,
which is exactly why it would not have been noticed. That is the failure mode worth logging.

**VERIFY** — no surface claims a unique anti-genomic property for any one pair.

---

## REP-11 · The design rule that must propagate: measure location and state, not abundance

**LAYER** model · **SEVERITY** method · **PATH** `T0`

**What is wrong.** Protein-fate protocols in this repository count bands. Read at full text this
session (PMID 30202070): blocking degradation with a proteasome inhibitor **or** a lysosomal inhibitor
raised the mutant protein and *"neither one rescued"* the cellular phenotype; the accumulating species
*"remained sensitive to EndoH"* and *"did not advance through the secretory pathway"*.

🎯 **Blocking degradation accumulates protein at its point of failure.** This is not the slogan
"abundance is not function" — it is the mechanism behind it, and it means **a band count cannot
distinguish a rescue from an inert accumulation.**

**FIX** — Every protein-fate protocol gains a localisation or conformational-state readout beside the
abundance readout. Applies to `EXP-...-01`, `-03` and `-05`.

**VERIFY** — no protocol in the repository proposes abundance as a sufficient rescue readout.

---

## REP-12 · 🔴 The tumour axis is a gate, and it is triply supported

**LAYER** model · **SEVERITY** safety · **PATH** `BATCH_COMMIT` for the therapeutic surface

**What is wrong.** The tumour risk of a partial-restoration strategy is treated as a footnote. Three
independent lines converge:

| Line | Evidence |
|---|---|
| The best-fitting drug class amplifies a **pro-tumorigenic** transcription factor | PMID 32653364 |
| Losing **one** WWOX allele is haploinsufficient for tumour initiation | *"significantly greater in Wwox+/− than Wwox+/+"*, **P = 1.3 × 10⁻⁷** (PMID 17575124); spontaneous lung papillary carcinoma in adult heterozygotes (PMID 17360458) |
| The **viable low-dose hypomorph** is itself tumour-prone | *"higher incidence of spontaneous B-cell lymphomas"* and testicular atrophy (PMID 17823927) |

🔴 **In this gene, the partially-restored state is the tumour-prone state — and the drug class that
best fits the folding lesion independently raises tumour risk.** Consequence, which must be stated
wherever the candidate appears: **the Niemann-Pick safety database for that agent is the wrong
reference class on this axis**, because those patients are not WWOX-deficient. Partial mitigation to
weigh, not to assume: the agent is a **co-inducer**, amplifying an existing stress response rather
than activating the factor constitutively.

Note also that the heterozygote anchor **fails** for this endpoint: 50 % of normal WWOX is
demonstrably insufficient for at least one tumour endpoint, while being sufficient for
neurodevelopment. Two thresholds, not one.

**FIX** — Promote the tumour axis from note to gate on the therapeutic surface, with the wrong-
reference-class statement attached.

**VERIFY** — no therapeutic surface names the candidate class without the gate.

---

## REP-13 · The lead candidate moves — in both directions

**LAYER** model · **SEVERITY** status · **PATH** `BATCH_COMMIT` for the hypotheses surface

**What is wrong.** The candidate is recorded as **withdrawn**, on the reasoning that amplifying the
HSP70 axis could accelerate delivery of the mutant to the lysosome. `T0` is not a resting place for a
status that the evidence has moved, and the evidence moved twice.

**Toward revival.** The HSP70 family is **split**: read at full text with figures (PMID 24891511),
one paralogue destabilises the client and the other stabilises it, distinguished there by three
separate reagent sets whose discrimination is demonstrable on the panels. Broad induction produced
stabilisation **with functional benefit** in primary patient-derived fibroblasts — filipin, n = 3,
p < 0.01, on the endogenous allele — with a genotype **specificity control**: the same compound did
nothing in a different-domain genotype. That is the only published abundance-**and**-function rescue on
any node in this space.

**Toward caution, and these are new.**
1. 🔴 **The transcription factor the candidate agent acts through was never tested** in that paper —
   the term appears only in its reference list. The chain *compound worked → co-induction works →
   this agent* has an **unmeasured link**.
2. 🔴 **The effect required Hsp90**: an Hsp90 inhibitor abolished it. The lever is a folding **system**,
   not the abundance of one chaperone. This independently strengthens the conclusion that Hsp90 and
   HDAC6 inhibitors are directionally adverse here — they would abolish the mechanism, not merely
   accelerate clearance.
3. 🔴 **The abundance half of that paper is its weak half** — representative blots, no densitometry,
   no statistics, fold-increase `UNKNOWN`. The functional sentence is better supported than the
   abundance sentence it follows.
4. 🔴 **EndoH was never run there.** So that paper and `REP-11`'s source **never meet head-on**: this
   is an **open question, not a contradiction**, and it must not be reported as a clean asymmetry
   between two laboratories. The orchestrator reported it as clean before the full text arrived.

**FIX** — Move the status from `withdrawn` to **directionally unresolved, resolvable by one
experiment**, carrying all four bounds and `REP-12`'s gate. Any experimental arm must detect the two
paralogues with **separate reagents** — most antibodies do not distinguish them, and here they point
opposite ways.

**VERIFY** — the hypotheses surface carries the new status, the four bounds and the gate.

---

## REP-14 · One agent's precedent is regulatory, not mechanistic

**LAYER** model · **SEVERITY** over-claim · **PATH** `T0`

**What is wrong.** `analysis/proteostasis_rationale.md` carries an agent whose central-nervous-system
evidence is the strongest on the table — measured in human cerebrospinal fluid, with paediatric
neurological use. But mechanistically it is an **active-site chaperone for a different enzyme**, and
**there is no pocket at the WWOX lesion**: `Gln230` has relSASA **0.000**, reproduced this session on
two model versions. It is a **regulatory and pharmacokinetic precedent only**.

**FIX** — Relabel. Keep it as the precedent it is; remove the mechanistic implication.

**VERIFY** — the rationale states the precedent class explicitly.

---

## REP-15 · 🔴 HARNESS — an egress assumption is suspending real work

**LAYER** harness · **SEVERITY** stale · **PATH** `T0`

**What is wrong.** The repository records `rest.uniprot.org`, `www.ebi.ac.uk` and `files.rcsb.org` as
`connect_rejected`, notes it as *"an allowlist, not a per-host failure"*, and **suspends the
conservation and dimer-model work on that basis**.

**All three answered on 2026-09-26**, as did the PDBe mapping service, the RCSB search API, NCBI
E-utilities and the AlphaFold API. That is how this session obtained the human proteome for the
peptide-uniqueness check, the current structural coordinates and three genomic records.

🔴 **The defect is not the stale host list. It is that a negative network observation was allowed to
suspend scientific work without a retry policy.** An instrument reading is not a finding.

**FIX** — Retry every route recorded as blocked before work is suspended on it, and record the retry
date beside each. Unblock the conservation work — 🟢 already partly done: a ten-species alignment
built this session shows `Gln230` **invariant**, which closes the open item that asked whether the
glutamine identity is the conserved element. Re-run the multimer model, which is the cheapest
falsifier of the interface verdict.

**VERIFY** — no surface suspends work on a network verdict without a retry date.

---

## REP-16 · 🔴 HARNESS — "no full text in PMC" is an XML verdict, not a full-text verdict

**LAYER** harness · **SEVERITY** stale · **PATH** `T0`, and it has the widest reach in this list

**What is wrong.** For at least one publisher's content in PMC, every machine route reports no full
text: the XML carries an explicit publisher prohibition on XML download, `efetch` returns an empty
body, and Europe PMC's full-text XML returns `500`. **The rendered HTML page and the figure images are
served in full.**

One paper went from `abstract-depth` — where it had sat in the queue, correctly flagged and
deliberately not promoted — to **full text with all eight figures at 300 dpi** on that route alone,
and it is the paper that moved the lead candidate's status (`REP-13`).

🔴 **Consequence beyond this paper: every `abstract-depth` verdict in `full_text_queue_current.md`
that was reached by an XML or API route is now suspect.** The programme's reading-depth counters are
built on those verdicts.

**FIX** — Add the rendered-page route to the acquisition cascade **before** any unavailability verdict.
Re-triage the `abstract-depth` entries whose verdict came from an XML route. Record the rule: *a
no-XML result is not a no-full-text result.*

**VERIFY** — the acquisition cascade documents the rendered-page tier, and a sample of re-triaged
entries reports how many moved.

---

## REP-17 · Structural coordinates are four versions behind

**LAYER** model · **SEVERITY** stale · **PATH** `T0`

**What is wrong.** The repository holds `AF-Q9NZC7-F1` **Monomer v2.0**; the current model is **v6**.
🟢 **Nothing is wrong with the conclusions:** every load-bearing number reproduced identically on v6
this session — burial, pLDDT, the cleft geometry, the tetrad distances, the helix hydrogen-bond
pattern. Refresh so future work does not diverge from a superseded file.

**FIX** — Place the v6 coordinates beside the v2.0 file, keeping both with their version in the
filename; record that the measured values agree.

**VERIFY** — both files present, and the structural analysis names the version it used.

---

## REP-18 · ✅ Verified clean — retraction hygiene

**LAYER** model · **STATUS** `CLOSED` · **VERIFIED** 2026-09-26

A delegate raised a retracted paper as a possible contamination of the record. Checked: **PMID
25447306 is already correctly quarantined** in `registries/batch_queue.md` with *"may not support or
promote any claim; audit every claim already resting on it; readable for audit only"*, and appears in
two census files only as an enumerated search hit that was explicitly excluded. A second retracted
item — the most attractive-looking methodological hit in an adjacent search space, PMID 37156116 — was
caught by a delegate and excluded before use.

**No action.** Recorded so the question is not re-opened, and so the working practice that caught both
is visible.

---

## Closing rule

A row leaves this file only into `CLOSED` with its verification named, or into `WONT_FIX` with its
reason. 🔴 **Nothing is deleted** — a defect that was silently removed is a defect that will return
wearing different words.
