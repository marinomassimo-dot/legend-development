---
artifact: MIRROR decision packet + repair specification (Annex C.2 support)
review_id: DECISION-MINIMIZATION-AND-RECORD-SCOPE-SPEC-001
object: the seven human decisions of PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2
  § 10, reduced; the JSONL record-scope repair specification; scientific hostile-review templates
continues: PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2 §§ 2, 3, 8, 10
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: SEVEN DECISIONS REDUCE TO TWO. Five were mechanical repairs of an already-decided policy
  or vacuous on the live tree; one of the two remaining has a dependent that only exists in one
  of its branches.
scope_note: every reduction below is a measurement, not an argument. Where I claim a node is
  mechanical I state the command that shows it decides nothing.
own_gate_delta: measured on a `git archive HEAD` export with this file added — release gate
  `BLOCKS 301 → 301` (+0); independent scanner blocking `695 → 700` (+5), every one of them an
  `ITALIAN_CITY` / `ITALIAN_HOSPITAL` hit on the five published author name strings named in
  § 1.2, which are that section's subject. Kept for the reason given in v2 § 0.2: redacting them
  would concede that a false positive is a true one.
---

# Five of the seven were not decisions, and one of them could not have blocked anything that exists

---

## 1 · PHASE 6 — PRIVACY_MINIMUM_HUMAN_DECISIONS

### 1.1 · The dependency graph, with the evidence on each edge

```
  ┌─ NORMATIVE ROOTS ─────────────────────────────────────────────────────────────┐
  │                                                                               │
  │  D-A  OPERATOR_IDENTITY_AS_EVIDENCE                                           │
  │       "is the Operator inside the gate's scope, or only the clinical record?"  │
  │         │                                                                     │
  │         ├──► PATH_IDENTITY ................ MECHANICAL once D-A is answered    │
  │         └──► non-path operator identity ... MECHANICAL once D-A is answered    │
  │                                                                               │
  │  D-B  PUBLIC_EMAIL                                                            │
  │       "do 430 published corresponding-author addresses ship?"                 │
  │         │                                                                     │
  │         ├── permit ──► ORCID permitted a fortiori ....... NO DECISION NEEDED   │
  │         └── block  ──► D-C  ORCID .............. A SECOND DECISION, only here  │
  │                                                                               │
  └───────────────────────────────────────────────────────────────────────────────┘

  ┌─ MECHANICAL, NO POLICY CONTENT ───────────────────────────────────────────────┐
  │  AFFILIATION ┐                                                                │
  │  INSTITUTION ├── one repair: field-scope the two detectors                     │
  │  AUTHOR_NAMES┘                                                                │
  │  JSONL_RECORD_SCOPE ── § 2                                                     │
  │  WINDOWS_SEPARATORS ── vacuous: 0 live occurrences                             │
  └───────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 · Why each removed node is mechanical, measured

| node | v2 decision | why it is not a decision | measurement |
|---|---|---|---|
| **WINDOWS_SEPARATORS** | D5 | Including `C:\Users\` in the closed prefix set of v2 § 1.6 **cannot block anything that exists**, so the decision has no consequence to weigh | live occurrences of a Windows home root in the tracked tree: **0** |
| **AFFILIATION · INSTITUTION · AUTHOR_NAMES** | part of D1 | The geography and institution detectors exist to catch **the private individual's** geography. An Italian city inside a published author's affiliation is a false positive *by the detectors' own purpose*, and `CLAUDE.md` already settles that the public edition carries no individual-level record. Nothing is left to decide; the repair is to scope the two detectors to non-`.authors[…]` context | **498 of 506** blocking geo/institution findings (98 %) sit inside `.authors[…]`. Field-scoping leaves **8**, of which 2 are `.keywords[].term` and 6 are outside the corpus seed. The 12 author-name hits — `Florence` ×6, `Ao` ×2, `AO` ×2, `Napoli`, `Meyer` — are inside that 498 |
| **PATH_IDENTITY** | part of D4 | The Operator **already approved** blocking this class (v1 § 8, 57 live occurrences). The derived rule implements that approval correctly; it grants nothing | live tree **57 → 59**, a strict superset: 0 removed, 2 added, both at `launch/KERNEL_SPEC.md:42`. 0 FN / 0 FP on 26 fixtures against 17 FN / 1 FP shipped |
| **JSONL_RECORD_SCOPE** | part of D4 | "Evaluate a block rule on a block" has no policy content. The only thing that made it a decision was verdict risk, and that is measured | totals identical under all three scopes (494 / 489 / 5); § 2 |
| **R5 dedup key · R7 `NG` boundary** | part of D4 | R5 changes only the **visible count** (301 → 491), never a verdict — both states are BLOCK. R7 removes a finding that is 100 % false positive | § 2.4 and § 3.5 of v2 |

### 1.3 · The two that remain, and the one that is conditional

**D-A · Is the Operator's identity inside the gate's scope?**
`CLAUDE.md` says the public edition excludes the individual-level clinical record and says nothing
about the Operator. The system's own digest sets list the Operator's token beside the
case-identifier tokens. Those two cannot both be the policy. **Nothing mechanical can settle it,
because the contradiction is between two normative statements.** Its consequences: 57 (→59) live
path findings, and the 16 non-path occurrences of v2 § 4, of which the derived rule reduces the
uncovered set to 14 whichever way D-A goes.

**D-B · Do the 430 published corresponding-author addresses ship?**
245 of the 301 human-visible gate blocks are those addresses. Option C of v2 § 3.2 moves the
authoritative gate **from 301 to 300**; this single answer moves it to 56.

**D-C · Are the 480 ORCIDs in scope? — a decision only if D-B = block.**
An ORCID is an identifier; an email is a contact channel. So the implication runs one way only:

- **D-B = permit** ⟹ ORCID permitted *a fortiori* — a resolvable bibliographic identifier is
  weaker than a deliverable address. **No decision.**
- **D-B = block** ⟹ D-C is genuinely open, because one may rationally close contact channels while
  permitting identifiers. Then it must be asked, and the asymmetry named: the gate currently blocks
  430 of the weaker identifier and misses **480 of the stronger**, in **139 of 706 records**.

### 1.4 · `PRIVACY_MINIMUM_HUMAN_DECISIONS = 2 (+1 conditional)`

Down from seven. The other two of v2 § 10 — D6 `canonical surface` and D7 the stale CLAUDE.md
assertions — are **not privacy decisions** and are routed with their own objects
(`REV-ORCHMAJOR2-F8-MIRROR-001` and `REV-P0-CANDIDATES-MIRROR-001` § 2.3).

---

## 2 · PHASE 7 — JSONL_RECORD_SCOPE_SPEC

### 2.1 · The seven declared fixture classes, measured

The unit is **not the record.** The v2 spec said RECORD and one of the seven classes falsifies it.

| fixture | required | TODAY (file block) | RECORD | **RECORD + PAPER** |
|---|---|---|---|---|
| **F-A** same record | BLOCK | BLOCK | BLOCK | **BLOCK** |
| **F-B** different records, **same paper** | BLOCK | BLOCK | **SILENT ✗** | **BLOCK** |
| **F-C** different papers | silent | **BLOCK ✗** | SILENT | **SILENT** |
| **F-D** malformed record | fail closed | **SILENT ✗** | **SILENT ✗** | **SILENT ✗** — § 2.3 |
| **F-E** multiline invalid JSON | fail closed | BLOCK | BLOCK | BLOCK — right verdict, § 2.4 |
| **F-F** variant split across records, explicit reassembly | BLOCK | BLOCK | BLOCK | **BLOCK** |
| **F-G** legitimate public bibliography | silent | BLOCK (email) | BLOCK (email) | BLOCK — **that is D-B, not a scope question** |

**RECORD + PAPER passes 6 of 7 and strictly dominates RECORD.** On the live tree it is
verdict-identical to RECORD — 494 / 489 / 5, the same set, including the same recovery of the
suppressed `fulltext_read_receipts.jsonl:83`.

### 2.2 · The rule

```
UNIT(.jsonl)  =  the set of records sharing a paper identity
                 · identity = the record's `pmid` field
                 · a record with no `pmid` is its own unit
                 · a record that does not parse is its own unit, and is a finding (§ 2.3)

per-record predicates      → evaluated on the record
linkage predicates         → evaluated on the PAPER unit
cross-unit reassembly      → stays at FILE scope, and only via cross_paragraph_pairing,
                             which requires explicit reassembly language
attribution_window(.jsonl) → the PAPER unit, never the file
negation escape hatch      → the PAPER unit, never the file
locator                    → file:line + the JSON field path
```

**Why the paper and not the file.** *"File-level reconstruction only when normatively necessary"*
is the brief's rule and the paper unit is where it lands: two records with the same `pmid` are two
views of one publication, so re-identification across them is real (F-B). Two records with
different `pmid`s are two publications, so linkage across them is an artefact of storage (F-C).
The `pmid` field is the mechanical expression of that distinction and the corpus already carries
it in 706 of 706 records.

### 2.3 · Malformed records must fail closed, and nothing today can observe that they do

F-D is SILENT under **all three** scopes because `scan_privacy_and_secrets` treats `.jsonl` as
plain text end to end and never parses. And **0 of 1 137 tracked records are malformed**, so no
fixture in the tree exercises it. The rule:

> A line in a `.jsonl` that does not parse as JSON is a finding — `UNPARSEABLE_RECORD`, severity
> BLOCK — not a silence. A record whose structure cannot be read is a record whose privacy content
> cannot be bounded, and the paper unit it belongs to cannot be determined either.

This changes no verdict today, which is the only safe moment to install it.

### 2.4 · F-E is right for the wrong reason

Pretty-printed JSON in a `.jsonl` blocks under every scope because its variants land on one
physical line. The verdict is correct and the mechanism is coincidence: nothing noticed the file
was not JSONL. Under § 2.3 each of its four lines fails to parse and the file fails closed on its
structure, which is the reason it should fail for.

### 2.5 · The locator obligation

v2 § 2.4 measured that `deduplicate()` hides **190 of 491** blocking findings, 185 of them emails
in one file, because on `.jsonl` one line is one record and the dedup key ends at the line. A
record-scoped gate without a record-internal locator reports **records touched**, not findings.
The field path is already computed to attribute the finding; carrying it into the key costs
nothing and makes the count a count.

---

## 3 · PHASE 8 — SCIENTIFIC_REVIEW_READINESS

**No adjudication is opened here.** Mirror holds no routing for any of these, and Annex C.3 puts
review opening with Orchestrator. What follows is what a reviewer would be handed.

### 3.1 · Class A — the mouse-epilepsy cluster · CLAIM 004 · 005 · 011 · 016 · 037

The mechanical candidate generator of v2 § 8 (v3, shared-axis link coverage) emits **8 unlinked
pairs, all DATO-vs-DATO, 5 of them on `MOUSE / EPILEPSY`**, which is the axis on which CLAIM 005
writes a *prohibition*:

> **"No canonical statement may describe a Wwox-null mouse as showing epileptogenesis."**

| A | B | shared axis | linked? |
|---|---|---|---|
| CLAIM 004 | CLAIM 005 | MOUSE/EPILEPSY | no |
| CLAIM 004 | CLAIM 016 | MOUSE/EPILEPSY | no |
| CLAIM 005 | CLAIM 016 | MOUSE/EPILEPSY | no |
| CLAIM 016 | CLAIM 037 | MOUSE/EPILEPSY | no |
| CLAIM 004 | CLAIM 037 | HUMAN/EPILEPSY, MOUSE/EPILEPSY, MOUSE/SURVIVAL | no |
| CLAIM 005 | CLAIM 037 | MOUSE/EPILEPSY, RAT/EPILEPSY | **yes — the reconciled control** |

**Mandatory checklist, one row per pair, and every row answered against the source and not the claim:**

| # | check | what refutes the claim |
|---|---|---|
| 1 | **same model** | name the organism, strain and allele each side measured. `lde/lde` rat ≠ `Wwox`-null mouse ≠ human WWOX-DEE. A shared axis across two models is not a contradiction, it is a species discordance and must be **carried**, not resolved |
| 2 | **same endpoint** | ECoG spike-wave ≠ observed convulsion ≠ audiogenic seizure ≠ "seizure susceptibility". Two claims disagreeing about different endpoints do not disagree |
| 3 | **nomenclature vs measurement** | does the disputed word name a measurement or a summary of one? CLAIM 011's flag is exactly this — *"dose-dependent"* names a continuum where Figure 3B shows a threshold between 1.23 and 2.63 × 10¹¹ vg |
| 4 | **date ordering** | which reading came first, and does the later one cite the earlier? An unreferenced pair whose members were read months apart is a coverage gap; one read in the same batch is an authoring gap |
| 5 | **full-text locator** | resolve every disputed proposition to a verbatim locator in a manifest, independently. A claim with no locator on the disputed sentence cannot enter the comparison |
| 6 | **not-reported vs absent** | CLAIM 005's own boundary is the model: *"no EEG, no seizure observation, no behavioural assay, no brain histology"* — the assay could not have detected it. Distinguish that from Table 2's **empty `Epilepsy` row**, which is a reported negative |
| 7 | **baseline reversal** | would resolving the pair move a `consolidated baseline` claim? CLAIM 004 and CLAIM 005 are both consolidated baseline. If yes, the floor is MIRROR_REQUIRED and a locator audit precedes the reading |
| 8 | **prohibition vs datum** | CLAIM 005 carries a **normative sentence**, not a measurement. A claim can contradict a datum or violate a prohibition, and those are different findings with different remedies — one is re-read, the other is re-write |

### 3.2 · Classes B–F — the prepared bundles

| class | object | the first question, and why it is the first |
|---|---|---|
| **B** provenance item A | the imported-premise chain PMID 19936220 → 19500159 → 17803050, already traced end to end and recorded in CLAIM 005's boundary | **Is the chain still the only route?** Re-run the inbound audit: list every surface naming these sources as a premise's origin *today*, and mark each with the five verdicts of `IMPORTED_PREMISE_ATTRIBUTION_GATE`. The 2026-08-06 audit found three different verdicts in one session; the registry has grown since |
| **C** CLAIM 032 | *"WWOX haploinsufficiency is not deleterious: the therapeutic threshold is well below full restoration"* — `in observation`, typed `DATO (topo, ratto, e ogni famiglia umana pubblicata)` | **What would a negative look like, and could the sources have shown it?** A claim over *every published human family* is a closed-world assertion about a population that grows. Check 6 first: unmeasured ≠ absent. Then the shared-axis pairs — CLAIM 032 appears opposite CLAIM 004, 005, 017 and 020 on SURVIVAL |
| **D** CLAIM 002 · 003 | organoid network hyperexcitability + AAV rescue (`DATO + INFERENZA prudente`); non-cell-autonomous hypomyelination (`DATO`) | **Where does the DATO end and the INFERENZA begin, in one sentence each?** CLAIM 002's type is mixed and its title contains both halves. Check 8: a rescue in an organoid is a datum about an organoid |
| **E** CLAIM 016 · 035 | GSK3β hyperactivation *may contribute* to seizure susceptibility; WWOX as a residue-mapped direct GSK3β inhibitor | **Is 035 the mechanism 016 asserts, or a different one at the same target?** Both are `in observation`, both typed DATO + INFERENZA, and they are not cross-referenced. Check 1 and 2: five orthogonal biochemical assays and a point mutation are not a seizure endpoint |
| **F** AAV9 endpoint split | CLAIM 004 and CLAIM 011, both about AAV9-WWOX rescue, the first `consolidated baseline`, the second `flagged for review` | **List every endpoint measured and the direction of each.** CLAIM 011's flag already records that Figure 3B resolves survival and glycaemia and **not** ECoG/SWD, myelination or gliosis, and that the reading which would resolve them is `partial_fulltext_read`. One significant endpoint is not "rescue"; check 7 applies to 004 because it is consolidated |

### 3.3 · `SCIENTIFIC_REVIEW_READINESS = TEMPLATES READY, ROUTING ABSENT`

The candidate generator, the fixture that validates it, the checklist and the six bundles exist.
No adjudication is opened, and none will be from this seat without a Task Contract.

---

## 4 · WHAT_WOULD_CHANGE_MY_MIND

- **§ 1.2 AFFILIATION** — if the geography detectors were installed to catch something other than
  the private individual's geography, field-scoping them is a policy change and belongs back in
  the human packet. Test: find the decision record that installed `ITALIAN_CITIES`.
- **§ 1.3 D-C** — if an ORCID is resolvable to a contact channel in practice, the *a fortiori*
  edge breaks and D-C becomes unconditional.
- **§ 2.2** — if two records can share a `pmid` and describe different individuals (a corrigendum,
  a re-analysis), the paper unit over-groups and F-C's protection weakens. Test: enumerate
  duplicate `pmid`s in the corpus seed and read one.
- **§ 3.1** — if any of the five unlinked pairs turns out to be linked through a third claim, the
  candidate is a graph-distance question and not a coverage gap, and the generator needs
  transitive closure.
