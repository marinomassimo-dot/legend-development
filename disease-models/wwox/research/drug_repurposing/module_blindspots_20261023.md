# What the repurposing module cannot see — four blind spots, measured (2026-10-23)

Actor `scientist-d`, task `MODULE-D-20261023`, contract `ORCH-MODULE-BATCH-20261023`. A measurement study
of `framework/scripts/repurposing_join.py` against the 21 hand-made cards (`cards/`, `cards_early/`) and
the module's own proof (`module_proof_20261023.md`). **Non-canonical research material.** Every
non-WWOX source named is **NOT WWOX EVIDENCE**; the dated ChEMBL lookups in § 2.4 are class-level and
retrieved 2026-10-23. No dose, no suitability statement, no score and no rank of any drug appears here
(the two rankings in § 4 order missing data and defect classes by count, never candidates). Nothing here
is medical advice. No extractor was written; nothing in the map, the registries, the four current files
or the framework was edited.

Companion files: `typed_assertions_20261023.tsv` (blind spot 1), `early_benefit_map_records_candidate_20261023.md`
(blind spot 2), `map_identifier_edits_20261023.diff` (blind spot 4, `git apply --check` clean against the
map as of this commit).

---

## 0 · Findings in order of consequence

| # | Finding | Number | Where |
|---|---|---|---|
| F1 | **The join reads the audit field at the wrong depth.** `manifest_evidence` takes `contradicts_locator["auditors"]`; the declared schema (and `locator_contradiction_audit.py`) puts it at `contradicts_locator["audit"]["auditors" / "verdicts"]`. Every one of the corpus's declarations is therefore read as `UNAUDITED / UNSTATED`. | **301 of 301** declarations carry a structured audit; the join reports 0 audited. The 6 entries behind the two AUDIT rows (`Q-R-02`: 5, `Q-N-17`: 1) each carry `auditors: 1` and a verdict. | § 5.1 (D1) |
| F2 | The 59 abstentions do **not** name a missing datum. All 59 carry the single string `NO_RECEIPTED_EVIDENCE_FOR_THIS_QUERY`. Their real cause is linkage, not absence of evidence: **50 of 59 resolve with no new reading** (3 tool fixes and the identifier edits); 9 remain. | 59 → 9 (simulated) | § 4.1 |
| F3 | A rule over the manifests (propositions + snippets + ChEMBL dictionary) reproduces the **core four fields** of 9 of 30 typed assertions; 10 more only with named extra inputs; 11 never. It works where the literature is large and clean and fails where the WWOX evidence is. | 9 / 10 / 11 of 30; WWOX-sourced rows: **2** / 8 / 8 of 18 | § 2 |
| F4 | The "20 prose-cited records" are **21**, and **19 of the 21 cite no paper at all** (not even author-year): one cites author-year (`R-04`, "Wang 2012"), one cites a ledger id that itself carries no paper (`R-08`). | 21 | § 5.4 (D4) |
| F5 | The early-benefit axis is half-visible: the map already names the ketogenic diet (`R-05`), vigabatrin (`N-04`) and mTOR inhibitors (`N-01`) — 3 of the 9 early-benefit cards have a map record, and the join abstains on all three because of F4. | 3 of 9 | § 3 |
| F6 | The ChEMBL adapter returns `MATCH_FOUND` for free text; **8 of the 10 cached "matches" are not the named substance** (sentences such as "HSP70 co-inducers" returned an unrelated molecule). | 8 / 10 | § 5.5 (D5) |
| F7 | 7 of 226 discovery-ledger leads never become queries (`lstrip("🔴 ")` strips one emoji only). | 7 / 226 | § 5.2 (D2) |

---

## 1 · How this was measured

- Cards: 21 packets (12 in `cards/`, 9 in `cards_early/`); 30 `drug_assertions` in total
  (A01 5, A02 3, B01 2, C01 1, D01 2, EB-ETX 3, EB-KD 3, EB-VGB 11).
- Manifests: 579 in `research/deepdive_manifests/`. A "locator" is a manifest `entries[i]`.
- Join state: `join/queries.json` (332), `join/evidence.json` (332 tables, 59 with `abstention`),
  `join/cards.json` (26).
- Registries were read only with `registry_records.py` (`get --theme/--id`, `catalog`), never grepped.
- Locating an assertion in a manifest was **my reading**: I matched each assertion's quoted content to an
  entry by content. The cards declare file-and-section locators, not `PMID#entry`, so the pairing is new
  work and is stated as such in the TSV. For claim-carried rows (vigabatrin, ketogenic diet) I matched
  by content within the PMIDs of the named claim and did **not** verify authorship in the manifest.
- The producibility classes (P1/P2/X) are **hand judgements over 25 located entries**. A mechanical
  co-occurrence probe over the same 25 (drug-term regex and a direction-cue regex) was run to show the gap
  between "words co-occur" and "a typed assertion": 24 of 25 entries contain the drug term, 23 a direction
  cue, 22 both — yet only 9 rows reduce to a correct core-four row (§ 2.2).
- Simulations of tool fixes were run in scratch against a copy of the derive logic and a patched copy of
  the map; no repository file was changed. They are measurements of what the query set would be, not a run
  of the module.

---

## 2 · Blind spot 1 — typed pharmacological assertions

### 2.1 The table

`typed_assertions_20261023.tsv`: one row per assertion of the 21 cards, **30 rows** (the 13 abstention cards,
7 in `cards/` and 6 in `cards_early/`, carry no assertion). Columns: card, assertion id, drug, target,
endpoint, context/model, direction, locator (`manifest#entries[i]`), the locator the card itself declares,
source status, audit status from `contradicts_locator`, producibility class, what the rule would need.

| Property | Count |
|---|---|
| Source status | **WWOX 18** · NOT WWOX EVIDENCE **12** (A01 5, A02 3, B01 2, ETX-3 1, VGB-8 1) |
| Direction | INCREASE 8 · DECREASE 8 · NO_CHANGE 5 · UNKNOWN 9 |
| Located in a manifest entry | **25 of 30**; 5 not located (VGB-2, -7, -9, -10, -11: the claim registry text is the only carrier) |
| Located entry's snippet is a *figure attestation* (a Scientist's reading, not a source quote) | 5 rows |
| Located entry itself declares a `contradicts_locator` | 4 rows (A01-005, ETX-1, ETX-2, KD-1), all four with a structured audit (§ 5.1) |
| Row sits in a manifest that declares any contradiction | 10 rows; every declaration in those manifests has a structured audit |
| Context: all five dimensions present in the located entry's own text | **0 of 25**; per dimension: genotype 15, disease 14, cell/model 9, stage 9, species 8 |

### 2.2 For how many rows could a rule have produced the row

The rule meant: for a manifest entry with a standing receipt, take (proposition + snippet); require a
drug-dictionary term (ChEMBL name or class, via `repurposing_adapter.py`), a measured-entity token, an
endpoint term and a direction cue in the same entry; emit drug, target, endpoint, direction and the
locator `PMID#entry`. Judged row by row on the core four fields:

| Class | Meaning | Rows | Of which WWOX-sourced | Of which NOT WWOX EVIDENCE |
|---|---|---|---|---|
| **P1** | the four fields are lexically recoverable from one entry, with the needs listed | **9** (30 %) | 2 (VGB-1, VGB-3) | 7 |
| **P2** | an entry holds the content but a named non-lexical input is missing | **10** (33 %) | 8 | 2 |
| **X** | no manifest entry can yield the row | **11** (37 %) | 8 | 3 |

P1: A01-001, -003, -004, A02-001, B01-001, ETX-3, VGB-1, VGB-3, VGB-8.
P2: A01-005, B01-002, C01-001, D01-001, D01-002, ETX-1, KD-1, VGB-4, VGB-5, VGB-6.
X: A01-002, A02-002 (cross-paper aggregates), A02-003, ETX-2, KD-2, KD-3 (UNKNOWN as an absence or a
pattern), VGB-2, -7, -9, -10, -11 (no located entry).

The headline is the split by source: **the rule works on the non-WWOX literature (7 of 12 rows) and
barely on the WWOX evidence (2 of 18)**, because the WWOX evidence is carried by the claim registry, by
Scientists' figure readings and by patient tables, not by clean results sentences. Nine of the 30 rows have
direction UNKNOWN; **a lexical rule can emit none of them as UNKNOWN** (UNKNOWN here means "owed": an
absence, a crossing curve, a missing table cell), and for three of them (VGB-4, -5, -6) it would emit
NO_CHANGE where the card deliberately says UNKNOWN — a disagreement that is a judgement, not an error.

### 2.3 What exactly the rule would need (count of P1+P2 rows needing each: 19)

| Need | Rows | Supplied by the ChEMBL / Open Targets dictionary? |
|---|---|---|
| A resolvable drug name or class | 15 of 19 | **Yes**, for the 7 substances the 15 rows use (§ 2.4) |
| A vocabulary for non-molecular or paper-internal interventions (diet, AAV9 vector, the compound "A51") | 4 (C01, D01 ×2, KD-1) | **No**: ChEMBL returns an unrelated or unnamed molecule for all three terms |
| A measured-entity pattern (gene/variant/phenotype token) | 19 | **No**. The cards' `target` is the *measured entity* (GAT-1 G443V, HIKESHI, spike-wave discharges, epileptic spasms), never the drug's pharmacological target: **0 of 30** `target` values equal a dictionary target |
| A phenotype ontology (spasms, VABAM, seizure control) | 3 P1 + 4 P2 (VGB-4, -5, -6, KD-1) | **No** (not in ChEMBL; HPO/MeSH would be a new dependency) |
| A direction lexicon with a negation class that maps a *measured* null to NO_CHANGE and not to UNKNOWN | 7 rows (4 NO_CHANGE rows, and the 3 rows where it would emit one) | No |
| An endpoint normaliser for composite or time-windowed endpoints | A01-005, ETX-1 (+ the P2 endpoints) | No |
| Comparator handling (a null for A beside a positive for B) | B01-002 | No |
| Splitting one bundled row into per-allele rows | B01-001 | No |
| Paper-level context metadata (species, cell type, genotype, stage, disease), because no entry carries all five | **19 of 19** (and 30 of 30) | No |
| Figure-attestation handling (the value lives in a Scientist's proposition, not in a quote) | 5 (C01, D01 ×2, ETX-1, ETX-2) | No |
| A judgement the lexicon cannot carry (confounded combination, multi-drug list) | 3 (VGB-4, -5, -6) | No |
| A policy to **drop** doses present in the entry (cards carry none) | any entry with a dose, e.g. A02-001 | No |

**The deliverable number is therefore: 9 of 30 reproducible with a drug dictionary + variant pattern +
direction-and-negation lexicon + paper-level metadata; 19 of 30 if every named extra input were built;
11 of 30 never from manifests.** The dictionary supplies one column (the drug) and one linkage (class by
shared target: ethosuximide and mibefradil share a ChEMBL target id; carfilzomib and bortezomib share
`26S proteasome inhibitor`). It supplies none of the other four columns and none of the context.

### 2.4 What the dictionary actually returned (ChEMBL via `repurposing_adapter.py query chembl`, 2026-10-23, NOT WWOX EVIDENCE)

| Term | Result | Reading |
|---|---|---|
| phenylbutyrate | SODIUM PHENYLBUTYRATE, mechanism "glutamine sequestering agent" | identity right; the curated mechanism is **not** the chaperone/HDAC activity the A01 rows concern |
| sodium butyrate | molecule, no mechanism | identity right, no mechanism |
| tauroursodeoxycholic acid | TAURURSODIOL, mechanism "Unknown", no target | identity right, empty |
| carfilzomib, bortezomib | "26S proteasome inhibitor", one target | right, gives the class |
| amlexanox | "Phosphodiesterase 4 inhibitor" | identity right; the curated mechanism is not the read-through/NMD activity the B01 rows concern |
| ethosuximide, mibefradil | "Voltage-gated T-type calcium channel blocker", same target id | right, links the two |
| vigabatrin | GABA-transaminase inhibitor | right |
| ketogenic diet | ETILAMFETAMINE | **false** `MATCH_FOUND` |
| A51 | an unnamed molecule (no `pref_name`) | cannot be confirmed |
| AAV9 | an unnamed molecule (no `pref_name`) | **false** `MATCH_FOUND` |

The mechanism a dictionary returns is the substance's regulatory MoA; the assertions are about what the
substance did in a model. For two of the five substances with a curated mechanism (PBA, amlexanox) the two
are different, so a dictionary-derived "target" would be misleading in exactly the rows that matter.

### 2.5 Minimal change proposed for blind spot 1 (lean)

A **locator shortlist, not an extractor**: `repurposing_join.py run --locate` adds, per derived card, the
list `PMID#entries[i]` of the entries (in that card's papers) whose text contains the candidate's name or
its ChEMBL synonyms, with the entry's first 120 characters. This is what the Scientist spent the search
time on in § 1 and it is a pure string test: 24 of the 25 located entries would have been in the shortlist.
It emits no drug/target/endpoint/direction. Direction, endpoint and context stay with the Scientist, which
is the module's own stated position (`module_proof_20261023.md` § 5) and is confirmed by § 2.2.

---

## 3 · Blind spot 2 — the early-benefit axis

### 3.1 What exists

`cards_early/` (9 cards: 3 candidates, 6 abstentions) and the P3 early-benefit note
(`repurposing_early_benefit_20261020_scientist-b.md`: five endpoint families — excitability/EEG,
myelination, neuroinflammation/gliosis, growth/metabolism, survival/function — and twenty qualified
relations in its § 3):

| Card | Kind | The one endpoint it pursues |
|---|---|---|
| `EB-KD-01` ketogenic diet | candidate | clinician-reported seizure control, symptomatic only |
| `EB-VGB-01` vigabatrin | candidate | clinical cessation of epileptic spasms with a stated criterion |
| `EB-ETX-01` ethosuximide (T-type contrast) | candidate | late-phase PTZ-provoked seizure score (preclinical; no human endpoint) |
| `EB-GROWTH-AX-01` | abstention (axis) | head circumference, height, weight against SD scores, repeated |
| `EB-DEV-AX-01` | abstention (axis) | within-patient developmental measure across an intervention |
| `EB-PDANCHOR-AX-01` | abstention (axis) | none can be named (no calibrated WWOX read-out in a living-patient matrix) |
| `EB-HORM-AX-01` ACTH, corticosteroids, phenobarbital regimens | abstention | spasm cessation, if a comparator exists |
| `EB-CBD-AX-01` cannabidiol | abstention | seizure control, if a response is first defined |
| `EB-MTOR-AX-01` mTOR-inhibitor class | abstention | none supported |

### 3.2 What the join sees today (correcting the proof)

`module_proof_20261023.md` § 3, item 2 says the map names no early-benefit record. Measured against the map and
`join/queries.json`: the map names **three** of the nine — `R-05` ketogenic diet (card `EB-KD-01`), `N-04`
vigabatrin (`EB-VGB-01`), `N-01` mTOR inhibitors (`EB-MTOR-AX-01`) — and the join **abstains on all
three** because those records cite their evidence by description (D4). For ethosuximide the join holds the
lead `Q-DL-MECH-170` (20 papers) and no card, because only a map record carries a candidate name. Cannabidiol
and the hormonal regimens have no map record, and the three axis cards (growth, development,
pharmacodynamic anchor) are endpoints, not interventions.

| Visibility | Cards |
|---|---|
| Map record exists, join abstains (identifier gap) | KD, VGB, mTOR — 3 |
| Lead query exists, no card (no candidate name) | ETX, HORM (leads `DL-MECH-134`, `DL-THER-106`) — 2 |
| Nothing in the join | CBD — 1 |
| Not an intervention, correctly absent | growth, development, PD anchor — 3 |

### 3.3 Proposed records (candidate file; the map is untouched)

`early_benefit_map_records_candidate_20261023.md`: three new records `R-10` (ethosuximide), `R-11`
(cannabidiol), `R-12` (ACTH / corticosteroid / phenobarbital regimens) in the map's own table form, each
carrying only fields copied from the cards plus a `SOURCE_IDS` row; one added row on `R-05`, `N-04`, `N-01`
naming the endpoint; and one data row for `AXES` (`early_benefit`). Resolved with the join's own parsers:
`R-10` reaches 21 papers, `R-11` 1, `R-12` 14. They sit beside `Q-DL-MECH-170/171/172` and `Q-N-03` (ETX),
`Q-DL-MECH-134`, `Q-DL-THER-106` and `Q-CLAIM001` (HORM), `Q-R-05`/`Q-N-04`/`Q-N-01` (the three that exist),
with `Q-N-15` as the guard for every seizure-control card. The three axis cards get no record: an endpoint
placed in the intervention universe would be a category error.

---

## 4 · Blind spot 3 — missing data in abstentions

### 4.1 The premise, measured: the module's 59 abstentions

All 59 abstention strings are identical. What recurs is not a missing datum but a missing **link**. Cause
per abstention, from the query text and the registries, with the effect of each fix simulated in scratch:

| Rank by count | Cause (what is missing) | Abstentions | Supplied by | Simulated effect |
|---|---|---|---|---|
| 1 | The record cites its evidence by description or not at all (map `R-04…R-09`, `N-01…N-15`) | **21** | an identifier in the record (§ 5.4) | 21 → 4 with the identifier diff alone; → 1 with the lead-side fixes below |
| 2 | The record already carries a manifest PMID in `bound_from` and/or a bound claim that has papers; the tool drops both (pathograph lines) | **19** | tool fix M3 (§ 5.3) | 19 → 0 (12 via `bound_from`, 17 via the bound claim, 19 either) |
| 3 | A lead names another lead that has papers; the tool follows claims but not leads | **11** of 16 leads | tool fix M2 (§ 5.2) | 16 → 5 (9 one hop, 2 more with the emoji fix and a second round) |
| 4 | The record names no source (3 experiment-design leads; 2 literature leads; 1 claim "mechanistic synthesis") | **6** | a reading, or an experiment | not resolvable by the tool |
| 5 | The record names a paper whose registry row has no PMID (`PAPER 008` "pending normalization"; `CORPUS P216` "PENDING") | **2** | a PMID lookup, then a read | not resolvable by the tool |
| — | The record is an external-safety statement with no registry row (`N-08`) | **1** (counted in rank 1) | a new registry row | not resolvable |

Simulated end state with the identifier diff and all lead/pathograph fixes: **59 → 9** (3 claims, 5 leads,
`Q-N-08`). Fifty of 59 abstentions resolve without a single new reading.

The nine that remain, by what could supply them:

| Route | Rows |
|---|---|
| A lawful full-text read after a PMID is found (a PMID with a lawful body must first exist) | `CLAIM 008`, `CLAIM 022` (PMID lookup first); `CLAIM 010`, `DL-MECH-004`, `DL-MECH-052` (literature not yet named); `Q-N-08` (external dichloroacetate safety source, NOT WWOX EVIDENCE) — **6** |
| Only an experiment | `DL-MECH-149`, `DL-MECH-150`, `DL-MECH-160` (experiment-design leads) — **3** |

### 4.2 The hand-made cards' named missing data (the data the task text had in mind)

The cards that *do* name missing data carry it in `not_known`: **89 entries across the 21 cards** (7 packets
also carry an `abstention_card.missing_datum` with the search that failed). I clustered the 89 entries by
what is missing. **The routing of each entry (read / experiment / neither) is my judgement from the entry's
own wording**; "read" means a published source may already hold it, which is not established.

| Rank (cards, then entries) | Missing datum | Cards | Entries | What could supply it |
|---|---|---|---|---|
| 1 | Denominators, counts, comparators, definitions of response (cohort size, base rate, what "Yes" means) | 8 | 17 | **a lawful read** of the cohort source or its supplement, or a registry |
| 2 | An agent or read-out never tested in a WWOX system | 7 | 8 | only an experiment |
| 2 | Genotype class or allele context of the response | 7 | 7 | read for 2 (HORM, CBD source rows); experiment for 5 |
| 2 | Prospective endpoints, baselines, instruments, anchors | 7 | 13 | only an experiment or a prospective cohort |
| 5 | Time to access / time to benefit | 5 | 9 | **neither**: a clinical and regulatory matter outside this module |
| 6 | Fate of the Q230P protein (made, cleared, insoluble, where surveilled) | 4 | 8 | only an experiment (the A-series' own decisive test) |
| 6 | Mechanism or direction unresolved (which arm carries the effect) | 4 | 4 | only an experiment |
| 6 | Exposure, CNS exposure, paediatric suitability | 4 | 6 | **neither**: label and treating-team matters; no statement made here |
| 9 | Function of any recovered protein | 3 | 3 | only an experiment |
| 9 | Endpoint outcomes already reported in WWOX papers (EEG outcome in a report, hormonal concurrency in VABAM reports, the blocked mTOR paper) | 3 | 6 | **a lawful read** |
| 9 | Dose, window, safety bound, replication, interaction | 3 | 6 | only an experiment |
| 12 | A ligand or structure for the SDR domain | 1 | 2 | only an experiment (or a structure) |

By route over the 89 entries: **experiment 44, read 23, neither 15, mixed 7**. By card: 18 cards have at
least one experiment-only entry, 10 at least one read-supplied entry, 6 at least one neither-entry. A
lawful read is therefore the right next act for the **cohort-denominator** cluster (rank 1, 17 entries,
8 cards) and the **already-reported** cluster (6 entries, 3 cards): 23 entries, one-quarter of the total.
Everything that touches Q230P or a WWOX-system test is an experiment, not a reading.

---

## 5 · Blind spot 4 — prose-cited records, and the defects found on the way

### 5.1 D1 · The audit field is read at the wrong depth

**Status at landing: already repaired on `main` by commit `9c4dbe4d` (plan), which reads the nested shape and re-derives `Q-N-17` and `Q-R-02` as READ rows. The measurement below is the evidence for that repair; M1 is done.**

`repurposing_join.manifest_evidence` (lines ~372–386) reads `declaration.get("auditors")` and
`declaration.get("verdict")`. The schema that `locator_contradiction_audit.py` writes and checks
(`_entry_audit_evidence`) is `contradicts_locator = {…, "audit": {"auditors": n, "verdicts": […]}}`.
Over all 579 manifests: **301 declarations; 301 carry a structured `audit` object; the join reads 301 as
zero-auditor / `UNSTATED`.** For the two handoff AUDIT rows: `Q-R-02` rests on 36779245 entry 38
(`SUPPORTS`) and 42422765 entries 38, 40, 41, 45 (`PARTIAL`, `UNDERSHOOT`, `OVERSHOOT`, `OVERSHOOT`; three
cite `locator_audit_PMID42422765_20261021.md`); `Q-N-17` rests on 30619736 entry 33 (`UNDERSHOOT`,
`CORRECTED`). Each has `auditors: 1`. Whether one auditor is enough, or whether the *repairs* written
after those audits are themselves unaudited (some `what_changed` fields say so), is a policy and reading
question; "no auditor" is not. The module's claim that two candidates stand on unaudited contradictions
(`module_proof_20261023.md` § 2, item 2) and the two AUDIT rows of the handoff were produced by this misread.
The same defect makes `unaudited_contradictions` constant across the corpus, so it cannot steer anything.

### 5.2 D2 · Leads dropped and leads not followed

`lead_queries` filters with `record.record_id.upper().lstrip("🔴 ").startswith("DL-")`, which strips the
red circle and the space only. Seven of 226 leads begin with another marker (⭐ `DL-MECH-033`, `DL-MECH-037`;
🎯 `DL-MECH-034`; ⚠️ `DL-BIO-008`; 🟢 `DL-MECH-040`, `DL-MOL-012`; 🥇 `DL-MECH-046`) and never become queries.
Two of them (`DL-MECH-034`, `DL-BIO-008`) are exactly the records the identifier diff should name, so naming
them would resolve nothing until D2 is fixed. Separately, `lead_queries` emits no `leads_named`, so a lead
that cites another lead inherits nothing, though a map record does.

### 5.3 D3 · Pathograph lines ignore the evidence they carry

Of 40 pathograph queries, 19 abstain. Each line's `bound_from` names its origin (12 name a manifest
`PMIDnnnnnnnn.json|entries[i]` that exists; the other 7 name a registry heading) and each is bound to a
claim; 17 of the 19 bound claims have papers. The second hop drops the bound claim because the line's
`origin_id` *is* the bound claim (`named = [n for n in named if n != query["origin_id"]]`), and the
first hop scans only the line's text, not `bound_from`.

### 5.4 The 21 map records, with identifiers (diff: `map_identifier_edits_20261023.diff`)

"Prose-cited" in the proof means 20; the count is **21** (`Q-R-04…R-09`, `Q-N-01…N-15`). Only `R-04` cites
a paper in author-year form ("Wang 2012"), and `R-04` and `R-08` name ids (batch and candidate ids; a
ledger lead) that the join cannot turn into papers. The join also does not read dismissal-ledger ids
(`DIS-nnn`), which `N-11` needs. For each record, `registry_records.py` was used to find the registry
records that carry its evidence; "PMIDs now" is the number the current join gives the id.

| Record | Candidate identifier(s) | Status | PMIDs now (join, 2026-10-23) |
|---|---|---|---|
| R-04 Lithium (GSK3β) | `CLAIM 016`, `CLAIM 035`, `PAPER 019`, `PAPER 056` (Wang 2012) | **exists** | 3 / 1 / 1 / 1 |
| R-05 Ketogenic diet | `CLAIM 042`, `CLAIM 020`, `DL-MECH-020` | **exists** | 3 / 1 / 8 |
| R-06 Anti-neuroinflammatory | `CLAIM 006`, `DL-REPO-002` | **exists** | 1 / 2 |
| R-07 Bumetanide | `DL-MECH-035`, `DL-MECH-098`, `CLAIM 002`, `PAPER 305` | **ambiguous**: the WWOX-side statement ("depolarizing GABA") sits in `DL-MECH-035`/`-098`; bumetanide's own evidence is external (`PAPER 305`). Diff names `DL-MECH-035` only | 11 / 1 / 4 / 1 |
| R-08 Base / prime editing | `DL-MOL-013` (already cited), `DL-MOL-011` | **exists but resolves to 0**: the cited lead carries no paper; two hops needed | 0 / 0 |
| R-09 Proteostasis, SDR missense | `CLAIM 019`, `DL-MECH-036`, `DL-MECH-037`, `DL-BIO-001` | **exists** (`DL-MECH-037` needs D2) | 6 / 1 / – / 3 |
| N-01 mTOR inhibitors | `PAPER 039`, `DL-MECH-034` | **exists** (`DL-MECH-034` needs D2) | 1 / – |
| N-02 Lithium as WWOX-specific modifier | `CLAIM 016`, `PAPER 019` | **exists** | 3 / 1 |
| N-03 Sodium-channel blockers | `DL-REPO-001` | **exists** | 1 |
| N-04 Vigabatrin / GABAergic push | `CLAIM 001`, `CLAIM 031`, `DL-MECH-035` | **exists** | 10 / 4 / 11 |
| N-05 Boosting WWOX expression alone | `DL-MOL-004`, `CLAIM 019`, `DL-MECH-069` | **exists** | 1 / 6 / 3 |
| N-06 Lactate as readout | `DL-BIO-008`, `DL-MECH-120`, `CLAIM 009`, `CLAIM 025` | **ambiguous**: four candidates; `DL-BIO-008` ("contradiction on lactate") fits "four sources vs one outlier". Diff names it; it needs D2 | – / 1 / 8 / 2 |
| N-07 Digoxin | `PAPER 091`, `CLAIM 025` | **exists** | 1 / 2 |
| N-08 Dichloroacetate | none (`DL-MECH-020` mentions it in passing) | **must be created** (external toxicity source, NOT WWOX EVIDENCE) | – |
| N-09 pTyr33 peptide | `DL-MOL-008`, `CLAIM 023` | **exists** | 2 / 4 |
| N-10 Splice-switching ASO | `DL-MOL-011`, `DL-MOL-013` | **exists but resolves to 0**; the precedent it cites (an approved antisense) has no registry row and is a partial create | 0 / 0 |
| N-11 4-PBA / TUDCA | `DIS-004`, `DL-MECH-036`, `DL-MECH-037` | **exists** (`DIS-004` is invisible to the join; `DL-MECH-037` needs D2) | – / 1 / – |
| N-12 HSP70 co-inducers | `DL-MECH-047`, `CLAIM 019` | **exists**, partial: the drug named has no row | 1 / 6 |
| N-13 Pro-myelinating agents | `CLAIM 003`, `DL-MECH-031` | **exists** | 4 / 5 |
| N-14 Antioxidants | `CLAIM 009`, `CLAIM 034`, `PAPER 054`, `PAPER 071` | **exists** (the two counter-directional systems are `PAPER 054`, `PAPER 071`) | 8 / 2 / 1 / 1 |
| N-15 Seizure control ≠ developmental protection | `CLAIM 031`, `DL-MECH-039` | **exists** | 4 / 1 |

Tally: **exists 16** (R-04, R-05, R-06, R-09, N-01, N-02, N-03, N-04, N-05, N-07, N-09, N-11, N-12,
N-13, N-14, N-15), **ambiguous 2** (R-07, N-06), **exists but resolves to 0** 2 (R-08, N-10), **must be
created 1** (N-08). The diff touches 20 records (everything but N-08) and adds one `SOURCE_IDS` row to each
R-record table and one `**Source ids:**` line to each N-record. These are *proposals for a Selector*: an
id appearing in a record is not a statement that the id's papers support the record's claim, and the
ambiguous rows are named so that a human chooses.

### 5.5 D5 · A free-text lookup is not an identity

The derived cards call ChEMBL with the map heading's candidate name. Of the 10 cached `MATCH_FOUND`
responses, **2** return the molecule named (`Lithium`, `Memantine`); the other 8 return an unrelated or
unnamed molecule for a sentence or a class ("HSP70 co-inducers" → a cobalt-cyanocobalamin entry;
"Pannexin-1 blockade" → atracurium; "Lithium as a WWOX-specific disease modifier" → a blood-group
substance). A card showing `ChEMBL: MATCH_FOUND` is read as evidence that the dictionary knows the
candidate. It does not.

---

## 6 · Minimal changes proposed to the module

All are modes or data rows of existing tools; none adds a file to `framework/scripts/`.

| # | Change | Size | Fixes |
|---|---|---|---|
| M1 | `manifest_evidence`: read `declaration["audit"]["auditors"|"verdicts"]`, fall back to the top-level keys; add a test over the 301 declarations | ~8 lines + 1 test | D1; retires or re-points the two AUDIT rows |
| M2 | `lead_queries`: `re.match(r"^[^A-Za-z]*DL-", id)` instead of `lstrip`; emit `leads_named`; run the second hop up to 3 rounds | ~10 lines | D2; leads 16 → 5 |
| M3 | pathograph: scan `bound_from` for `PMID\d+`; stop excluding the bound claim from its own line's second hop | ~6 lines | D3; 19 → 0 |
| M4 | `chembl` adapter: an `exact` request flag (default for the join) accepting `MATCH_FOUND` only when `pref_name` or a synonym equals the queried name, else `NO_MATCH_FOUND` with the nearest hit recorded | ~12 lines | D5 |
| M5 | `run --locate`: per derived card, the manifest entries containing the candidate's name or ChEMBL synonyms (a shortlist; no field of an assertion) | ~25 lines | blind spot 1, § 2.5 |
| M6 | `AXES["early_benefit"]` data row (candidate file § "axis row") | 1 row | blind spot 2 |
| M7 | Apply `map_identifier_edits_20261023.diff` after a Selector pass on R-07, N-06; create the `N-08` source row; add `R-10…R-12` from the candidate file | data | blind spots 2 and 4 |
| M8 | Correct `module_proof_20261023.md`: § 2 item 2 (D1), § 3 item 2 (3 of 9 early-benefit cards have map records), § 3 item 4 (21 records, 19 cite nothing) | prose | the proof's own three statements |

Simulated together (scratch, § 1): query set 332 → 339, abstentions **59 → 9**; map records without papers
21 → 1.

**What I would not build**

- An assertion extractor, or an LLM pass over locators: § 2.2 shows 22 of 25 entries pass a co-occurrence
  test and only 9 of 30 rows come out right, and the 8 WWOX rows that fail do so on judgement (confounded
  combinations, figure readings, absences), not on vocabulary.
- An endpoint or phenotype ontology service, or a context-metadata scraper: they would serve 19 rows and
  the cards already hold the same fields typed by a reader.
- A prose-citation resolver for the map: only one record cites author-year, and two of the 21 need a human
  choice. Naming an id is cheaper and exact.
- A deeper graph walker than three rounds, or any ranking over abstentions or candidates.
- A drug-disease join from Open Targets to fill `target`: the cards' `target` is the measured entity and
  no dictionary value equals it.
- A second schema for typed assertions inside the join: the bridge already has one.

## 7 · Limits

The P1/P2/X classes and the missing-datum routes (§ 4.2) are one reader's judgements; the TSV carries the
reason per row so they can be contested. Locators for claim-carried rows were matched by content, not by
authorship. The ChEMBL lookups were 14 adapter queries (three HTTP requests each) on 2026-10-23, not cached into the repository. The
simulation of M1–M4 and the identifier diff is a count of what the query set would be, not a run of the
module, and does not test that a named id's papers support the record. Nothing here promotes, scores or
recommends any candidate, and nothing here is medical advice.
