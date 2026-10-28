# Independent verification: closed loop on real work (iteration 3, cases a, b, c, queue section)

Verifier: scientist-a (did not produce the work). Date: 2026-10-28. Read-only toward every subject file.
Subject: `main` f75085ce (commit 28dd1869). Non-canonical; not medical advice; no contact, no spend.
Verdict vocabulary: SUPPORTED, OVERSHOOT, UNDERSHOOT, NOT_IN_SOURCE, UNVERIFIABLE.
Sources used: `catalog/catalog.jsonl.gz` (recomputed), `repurposing_search.py` (re-run), `coverage/*.json`,
`needs/needs.json`, PubMed records for the five apinocaltamide papers (abstract level only; no full text opened
here either), the audited PARS2 note, the E01 card, the committed code and a regenerated handoff.

## 1. Apinocaltamide (case a)

### 1.1 Identity (catalogue)

Re-run `compound apinocaltamide`: two records. `CAT:CHEMBL4217292` carries one ChEMBL_37 curated mechanism row,
"Voltage-gated T-type calcium channel blocker", action BLOCKER, target family CHEMBL2362995 with gene symbols
CACNA1G/H/I and UniProt O43497, O95180, Q9P0X4 (the three alpha1 G/H/I chains), max phase 2, status
clinical_candidate, no approval statement; synonyms ACT-709478 and NBI-827104; reference ids include two PubMed
ids and a sponsor pipeline URL. `CAT:DGIDB:b811c040b8a4` has three DGIdb rows, all with claim_source ChEMBL
(plus NCIt at record level). Verdict: SUPPORTED. The card's statement that the DGIdb record repeats the ChEMBL
claim and is not independent confirmation is exact (all three target rows are claim_source ChEMBL). The mechanism
reference ids are sponsor-linked (a sponsor pipeline page and the discovery paper), so even the ChEMBL row is a
sponsor-derived curation.

### 1.2 The five abstracts, assertion by assertion

| Assertion on the card | Verdict | Note |
|---|---|---|
| Discovery paper (J Med Chem 2017): potent, selective, brain-penetrating, clinical candidate | SUPPORTED | Abstract says "brain-penetrating" for the series; species not in abstract (MeSH: rats, dogs, guinea pigs, macaques). Sponsor authors only. |
| First-in-man paper: healthy volunteers, tolerability, slow absorption, long half-life | SUPPORTED | 65 male subjects; Tmax 20-28 h above 60 mg; half-life 36-43 h. |
| "Healthy adult" volunteers (card, README, LD-001) | NOT_IN_SOURCE (minor) | Abstracts say "healthy subjects"; MeSH for both phase 1 papers include Adolescent and Young Adult; ages are not in the abstracts. "Adult" is an inference. |
| Multiple-dose paper: dizziness, somnolence, headache; up-titration; weak GI CYP3A4 induction | SUPPORTED | The abstract also reports "a tolerability signal ... in cohort 1 (30 mg once daily)" that forced a dose cut. The card mentions up-titration but lists "healthy-adult tolerability" under FOR without that signal. Mild UNDERSHOOT of the against side. |
| Epilepsia 2025: SWD suppression "equivalent to or superior to first-line monotherapy" (DR-H01-001) | SUPPORTED | Verbatim in the abstract; comparator unnamed; sponsor-authored (one author at a contract research organisation). |
| Same paper: generalized convulsive severity reduced "albeit at higher concentration" (DR-H01-002); no effect on focal onset (DR-H01-003); valproate synergy | SUPPORTED | Verbatim. |
| DR-H01-001 and DR-H01-003 developmental_stage "adult" | NOT_IN_SOURCE | The abstract gives no age for the rats. DR-H01-002 says "not stated" for the mice, so the card is internally inconsistent. |
| DR-H01-002 genotype "audiogenic-sensitive mice and wild-type mice" | NOT_IN_SOURCE | The abstract names the models, not the strain used for the electroshock threshold test. |
| "No relevant activity on other targets" is the sponsor's statement | SUPPORTED | Correctly attributed in the card's mechanism field. |
| Cryo-EM paper (Cell Res 2024): Cav3.2 binding | SUPPORTED | Four antagonists, apinocaltamide among them, human Cav3.2 only; nothing about Cav3.1/3.3. |
| Card against-list: "All apinocaltamide sources are sponsor-affiliated" | OVERSHOOT (internal contradiction) | The card's own source list includes the cryo-EM paper, whose authors are at Princeton, Tsinghua and Montpellier. README states the correct form ("all sponsor-affiliated except the structure paper"). The card should say so and credit the structure as the only non-sponsor datum (direct pore block of Cav3.2; no Cav3.1/3.3, no in vivo exposure). |
| DR-H01-004: developing-cortex viability signal belongs to other compounds, in vitro, rat E14 | SUPPORTED | Attributed to two research blockers; the earlier packet (A-ETX-3) says the effect was Cav3.1-dependent and ethosuximide was not tested. The receipt id exists in the ledger. The Cav3.1 dependence is not carried onto this card; since apinocaltamide blocks Cav3.1 too, that is the relevant detail. |

### 1.3 Is "candidate as mechanism-level discriminator only" justified?

Largely yes, as a label for an abstract-level, non-WWOX, sponsor-sourced compound; the card and LD-001 repeat the
limits, give no dose, and write a falsifiable prediction. Concerns:

1. The discriminator logic is circular at one point. The card's first FOR bullet treats ethosuximide as "the
   same target class", but the repository's own needs audit (C10 in `2026-10-28_it3_needs_second_verification.md`)
   says ethosuximide's T-type action is the paper's Methods wording only. The card's `not_known` list holds the
   question, but its `evidence_against` does not carry the premise. A concordant result would raise the T-type
   reading; a discordant result could equally be exposure (apinocaltamide Tmax 20-28 h and half-life 36-53 h in adults).
2. "The one that is structurally unrelated, brain-penetrant, three-subtype, clinical" (README) is overstated as a
   uniqueness claim. The catalogue also carries suvecaltamide (ChEMBL curated, three subtypes, action MODULATOR, not
   BLOCKER), Z944/ulixacaltamide (clinical; ChEMBL record empty, DGIdb only), TTA-A2 and ML218 (research tools with
   rodent use, DGIdb). Several have an independent academic literature, which apinocaltamide lacks (card:
   sponsor-only). The informational-value argument is reasonable, but alternatives were set aside for access or
   independence reasons that are not established (card: time_to_access UNKNOWN).
3. Missing or thin counter-evidence: (a) the cohort-1 tolerability signal; (b) long half-life and slow absorption
   versus a PTZ pup assay with a one-hour late phase (exposure measurement is on the card; the timing mismatch is
   not named); (c) the Wwox-null pup is a sick animal, and weight/glucose confounds on drug disposition are not
   listed; (d) the 2025 abstract positions the compound for childhood absence epilepsy, which the card omits, so
   the FOR side is also slightly under-stated.
4. Over-reach check: "no efficacy claim", "not a treatment proposal", `translation` all UNKNOWN: SUPPORTED. The one
   over-reach is in the queue (section 4): the card appears as a "consistent_mechanism_candidate" row against
   NEED-SEIZURE-CONTROL-SYMPTOMATIC, which the card disclaims.

Verdict on the label: SUPPORTED with corrections C1-C3 below.

## 2. Cases b and c (recomputed from `catalog.jsonl.gz`)

| Claim | Verdict | Recomputation |
|---|---|---|
| Glycine and aspartic acid: opposite_mechanism for NEED-EXCITATORY-GAIN (direction down); no ChEMBL mechanism row | SUPPORTED as classification; OVERSHOOT in reasoning | DGIdb-only records. Glycine: GtoPdb "agonist" on GRIN2A, GRIN2B, GRIN2C, plus TTD GRIN2A unknown. Aspartic acid: GtoPdb "agonist" GRIN2A/2B/2C. Neither has a ChEMBL mechanism row. The glycine record has no GRIN1 row (glycine's own site) and carries GtoPdb "agonist" rows on the pseudogene ASS1P10 and on SLC38A4: the same family-level propagation pattern that LD-003 rejects as an artefact. The sign is right pharmacologically (aspartate agonist at the glutamate site; glycine co-agonist), but LD-002 should say the GluN2 rows are family-level and glycine is a co-agonist. "No repurposing question follows" is editorial, not a finding. |
| Adenosine/regadenoson "opposed" via ABAT is a source artefact (LD-003) | SUPPORTED (rows); UNVERIFIABLE (GtoPdb source) | Adenosine record: 16 target rows incl. ADORA1/2A/2B/3 (ChEMBL agonist), SLC28A1/2/3, SLC5A7, ABCA1/2/3, ATP4B, FTH1P3/4, and one GtoPdb "agonist" on ABAT. Regadenoson: ADORA2A (ChEMBL agonist), ABAT (GtoPdb agonist), ABCA1/2/3, AMPD1. The ABAT row is the only link to the need's target; the real targets (ADORA) are not need targets. GtoPdb source not opened (the README says the same). "Neither opposite nor consistent" omits that the real mechanism (adenosine receptors) may be relevant to seizure control through a receptor the need does not list. |
| PANX1: "catalogue returns nothing" | SUPPORTED literally; UNDERSHOOT in scope | `target PANX1`, `target Panx1`, `target pannexin`: 0 ChEMBL rows (DGIdb needs an HGNC id; run through the need, no row). Scan of all 44,211 records: PANX1 appears in none. But PANX2 and PANX3 carry GtoPdb "inhibitor" rows on carbenoxolone (`CAT:DGIDB:ea45bb50fb31`) and flufenamic acid (`CAT:DGIDB:37352f589f92`). README/LD-005 say carbenoxolone exists "under other targets" without naming these paralogue rows; they should be named and declared not PANX1 evidence. Probenecid and brilliant blue G exist as records with no PANX symbol. |
| EIF2AK4: 0 ChEMBL mechanism rows; six DGIdb rows | SUPPORTED | Ziprasidone, olanzapine, haloperidol decanoate, risperidone, quetiapine fumarate (all PharmGKB, interaction type unknown) and hesperadin (DTC, "inhibitor", stated). `need NEED-ISR-ATTENUATION --limit 500` returns the same six. |
| Hesperadin described as "multi-kinase research inhibitor" | UNDERSHOOT | The record carries 81 target rows, nearly all DTC "inhibitor"; EIF2AK4 is one of 81. Its association row exists but it has no row in `priorities.json` for this need (the 393 to 398 rise is the five antipsychotics only), so search and coverage disagree on hesperadin; the README does not mention it. |
| LD-004 reopening condition (ii) "a catalogued compound with a stated GCN2 action" | OVERSHOOT (internal inconsistency) | Hesperadin already is a catalogued compound with a stated (DTC) inhibitor action on EIF2AK4, so the condition is already met as written. Intended meaning must be "a selective compound or a mechanism row". Also `catalogue_ids` in LD-004 lists only hesperadin although `why` is mostly about the antipsychotics. |
| Known GCN2 tool compounds are not in the catalogue | SUPPORTED (by name search) | No record named GCN2iB or GCN2 anything. Halofuginone records exist. The README says halofuginone's mechanism is from general knowledge; the audited PARS2 note records that the paper itself cites halofuginone as a GCN2-activating prolyl-tRNA-synthetase inhibitor precedent (not tested there). |
| Exploration count 393 to 398 | SUPPORTED | Priorities before the commit: 393; now 398; consistent_mechanism_candidate 201 in both. |

## 3. needs.json observation O5 (EIF2AK4 on NEED-ISR-ATTENUATION) against the PARS2 audit

| O5 element | Verdict | Audit anchor |
|---|---|---|
| GCN2 co-RNAi: bang-sensitive fraction about 87 to about 30; recovery shorter | SUPPORTED | Audit Q1: 0 / 87 / 30 / 4; recovery about 98 s vs about 10 s. |
| ATF4 co-RNAi: about 93 to about 46 ("partly") | SUPPORTED | Audit Q1: 93 / 46 (three vials about 30, 42, 62) / 10 / 0. |
| P-GCN2 and P-eIF2alpha up, P-PERK unchanged | SUPPORTED with an omitted caveat | Audit entry 33: the Fig 6B key is inverted, so bar identity cannot be read from the panel alone; the text resolves it. O5 does not carry this. |
| age_stage "adult 4-7 days" | OVERSHOOT (merge) | Results say 5-7 days and Methods 4-6 days (audit entries 19, 20); "4-7" blends two conflicting statements without saying so. |
| Limits: single-RNAi knockdown measurement; behaviour and delay move together; genetic is not pharmacology | SUPPORTED | Audit S7/S8. |
| Missing limits that the audit records | UNDERSHOOT | No second RNAi line for either gene; no statistics on the double-versus-control residual (30-46% versus 0%); no titration control for the two-construct arms; ATF4 RNAi alone pupariates earlier than control; no mitochondrial readout after suppression. The E01 card carries several of these; O5 should carry or point to them. |
| scope OTHER_DISEASE_PRECEDENT; direction "rescue direction, partial" | SUPPORTED | |
| Target role string "named by a fly precedent, not by a WWOX observation" | SUPPORTED | |
| New `inferred` line (GCN2 versus PERK or eIF2B relevance unmeasured) | SUPPORTED | |

No overreach into pharmacology; the need's direction stays "uncertain".

## 4. The queue (handoff section "Catalogue-derived leads")

Recomputed independently from `coverage_matrix.json` and `priorities.json`: card-attached pairs with disposition in
{consistent_mechanism_candidate, exploration_candidate, opposite_mechanism, source_queried_without_result} number
exactly 10, and the committed section lists exactly those 10 (E03 DCA x PDH; EB-ETX-01 x 2; EB-VGB-01 x 2; F01
memantine; F01 perampanel; G01 lithium; H01 x 2). 22 further card-attached pairs (not_relevant, insufficient_data)
are excluded by design. LD-001..005 have all required fields. The handoff regenerated with
`repurposing_join.py handoff --date 2026-10-28` is byte-identical to the committed file (28 main-table rows, as the
README says). `test_repurposing_join.py`: 49 tests OK.

Rows that depend on L3/L4 cells (over-claim risk pending the coverage correction), 7 of 10: E03 DCA (L3 observed),
EB-ETX-01 x NEED-T-TYPE-CALCIUM (L3 observed), EB-VGB-01 x 2 (L3 and L4 observed), F01 memantine and perampanel (L3
observed), G01 lithium (L3 and L4 observed). EB-ETX-01 x SEIZURE-CONTROL and both H01 rows have L3/L4 none and depend on L1/L2 only.

Findings:
- OVERSHOOT: H01 appears against NEED-SEIZURE-CONTROL-SYMPTOMATIC as "consistent_mechanism_candidate" (driven by
  CACNA1G alone) with the same next-measurement text as the T-type row. The card disclaims symptomatic seizure
  control, and LD-001 covers only NEED-T-TYPE-CALCIUM.
- Consumption: disposition rows have owner, reopening condition and next experiment, so they are consumable. Card
  rows have no owner column, and 4 of 10 (EB-ETX-01 x2, EB-VGB-01 x2: early-format cards without a `p4_card`) show
  "UNKNOWN" for the next measurement; those four are decorative until an owner or next act is attached. LD-002
  ("none (ended)") and LD-003 (coverage maintainer; next act is a coverage correction) record endings and are not
  Scientist work items.
- Broken references: LD-005's `record` points to `README.md#case-d`, which does not exist (cases are a, b, c; the
  PANX1 item is in case b). The card lists an internal source `closed_loop_it3_20261028/case_a_apinocaltamide.md`; that
  file does not exist (the directory holds only the README).
- Code (`catalogue_leads`, `render_catalogue_leads`): no regression found. Weak points: (1) an invalid
  `lead_dispositions.json` raises an uncaught exception although the docstring says "never an error"; (2) the need
  check uses needs that have a priorities row, so a valid need with no priority row would be flagged; (3)
  `catalogue_ids`, `card` paths and id uniqueness are not validated; (4) truncation at 40/160 characters silently
  drops the tail of next-measurement text. `test_shipped_dispositions_are_valid` asserts only "no problems" and one candidate.

## 5. WWOX-value observations table (README)

| Observation | Artefact link real? | Value demonstrated? | Verdict |
|---|---|---|---|
| Counter-evidence retrieved: developing-cortex viability signal attached to the new compound | Yes (DR-H01-004; receipt in ledger) | The signal is on the card. It was carried by hand from the earlier ethosuximide packet; nothing in the loop retrieves it automatically, and the Cav3.1 dependence is dropped. | SUPPORTED with the manual-carry and Cav3.1 caveats |
| Candidate reinterpreted as discriminator; new discriminating question | Yes (LD-001, `next_measurement`) | The two-blocker arm is new to the repository. The question "is the ethosuximide effect T-type mediated" is not new: the needs audit (C10) and the need's own limits already state it. | OVERSHOOT on "new question"; SUPPORTED on "new arm" |
| Wrong transfer avoided: antipsychotics as GCN2 hits | Yes (LD-004) | The coverage layer had already flagged these rows exploration-only, direction unresolved, interaction type UNSTATED, so no transfer was in progress. The loop's addition is the reasoned explanation. | OVERSHOOT |
| Direction not assumed from genetic GCN2 suppression | Yes (O5 limits, LD-004) | Yes; the need's direction was already "uncertain" before the edit. | SUPPORTED |
| New discriminating question: GCN2 versus PERK, which changes the lever for E01 | LD-004 yes | The E01 card (added 2026-10-27 from the same fly reading) already says: read phospho-GCN2 and phospho-PERK separately; which kinase is engaged is unmeasured; a PERK-arm inhibitor "would not be the matched tool". LD-004 restates it. | OVERSHOOT |
| False "opposite" avoided: adenosine/regadenoson | Yes (LD-003) | The false flag is real (rows inspected). The coordinator's audit had reached it first (per the README), so this is confirmation. | SUPPORTED as a verified artefact; OVERSHOOT as a loop discovery |
| Loop gap found: need omitted GCN2 | Yes (needs diff) | EIF2AK4 absent before, present after; the search could not return it before. | SUPPORTED |
| Work saved | none claimed | | SUPPORTED (no claim) |

Net of 8 rows: 3 SUPPORTED, 1 SUPPORTED with caveat, 1 split (SUPPORTED/OVERSHOOT), 3 OVERSHOOT.

## 6. Counts and corrections

Counts. Identity: 1 SUPPORTED. Abstract-level assertions: 12 (7 SUPPORTED, 3 NOT_IN_SOURCE, 1 OVERSHOOT, 1
SUPPORTED with an undershoot). Cases b/c: 8 claims (4 SUPPORTED, 1 SUPPORTED-literal with UNDERSHOOT in scope, 1
UNDERSHOOT, 2 OVERSHOOT). O5: 9 elements (6 SUPPORTED, 1 OVERSHOOT, 1 UNDERSHOOT, 1 SUPPORTED with omitted caveat).
Queue: 10 rows exact, 7 depend on L3/L4 cells, 1 row-pair overshoot, 2 broken references. Value table: see above.

Corrections requested.
- C1. Card H01 `evidence_against`: correct "All apinocaltamide sources are sponsor-affiliated" and credit the cryo-EM
  paper; add the premise that ethosuximide's T-type attribution is the source paper's Methods wording; add the
  cohort-1 tolerability signal; carry the Cav3.1 dependence of the viability signal.
- C2. Card H01: DR-H01-001/003 "adult" and DR-H01-002 genotype wording to not stated at abstract level; "healthy
  adult" to "healthy subjects (age not in the abstract)"; remove the dead internal source `case_a_apinocaltamide.md`.
- C3. README case a: drop "the one that"; name suvecaltamide, Z944, TTA-A2, ML218 as set aside and say why, or say the
  reason is not established.
- C4. LD-005: fix `record` anchor to `#case-b`; name carbenoxolone and flufenamic acid PANX2/PANX3 rows as paralogue,
  not PANX1, evidence. LD-004: rewrite reopening condition (ii); list the antipsychotic ids; say hesperadin has 81
  target rows and is absent from `priorities.json`. LD-002: note the GluN2 rows are family-level and glycine's own
  site is absent from the record.
- C5. needs O5: age "5-7 days (Results) / 4-6 days (Methods)"; add the Fig 6B key caveat and the absent controls.
- C6. Handoff/code: drop or annotate H01 x NEED-SEIZURE-CONTROL-SYMPTOMATIC; add an owner or next-act column, or omit
  the four UNKNOWN early-card rows; make an invalid disposition file a reported problem; validate `card` path and id uniqueness.
- C7. README value table: reword the three OVERSHOOT rows as "stated and recorded", citing the E01 card and the
  existing exploration-only flag as prior art.
