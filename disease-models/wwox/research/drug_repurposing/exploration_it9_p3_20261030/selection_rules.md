# IT9 P3 selection rules (pre-registration of the selection, written 2026-10-30 BEFORE any family name was used for selection)

Scientist-b2, task `ORCH-ROADMAP-IT9-20261030`, branch `task/it9-p3`. Exploratory, computational, descriptive. Not medical advice. A proposal of the P2 engine is a
direction compatibility ('compatible action'), never a predicted benefit. Reference genotype: a WWOX-DEE genotype class; no individual-level record.

## 0. What had been seen before this file was written (disclosure)

* Read: the P1 and P2 READMEs, `PRE_REGISTRATION.md` of P2, the column headers of all tables used here, per-set counts, the P2 funnel JSON, the status/access/modality counts of
  the IT8 P9 inventory (aggregate counts only).
* Names seen by accident: the first three rows of `candidates_Q2.tsv` (three family names: a tool compound on LDHB, pracinostat, an anti-HIF1A antisense oligonucleotide), the first
  two rows of `deepening_queue.tsv` (acamprosate, amantadine), the list of uncarded items N01 to N11 of IT8 P9, and the fact that the first P2 mimics rows have a seed-specific flag of 0 while
  their Z is below -3 (a sign convention in the P2 table: the flag is computed as z > 3 only). No name has been used to decide any rule below; the thresholds below were chosen from aggregate
  distributions (percentiles of n_signed_targets over the pool, no names).
* Not seen: any ChEMBL/ATC/route data for any pool family, any literature count, any card content for a pool family, any hub or cluster assignment.

## 1. Universe and pool (mechanical)

1. **Funnel** per question and arm, from `funnel_*.json`, `per_question_counts.tsv` and the catalogue inventory (`ranking_it8_p9_20261029/inventory_families.tsv.gz`): catalogued 40,268; identity resolved
   16,475 (`origin = chembl_selected`); usable by the method 13,379 (`mnet_usable = yes`); with gene symbol 13,307; examined 12,560; non-zero; seed-specific; taken to deepening.
   UNKNOWN states are kept as UNKNOWN (28,776 records without structure key, 26,889 without a signed action, 72 without gene symbol, 25,501 with unverified access category);
   they are exclusions of the METHOD, listed with counts, never read as 'not active'.
2. **Seed-specific, recomputed here** (the P2 candidate table flag is not used because it is 0 for every mimics row): from `proposals_p1_<set>.tsv.gz` (total-degree null) and
   `proposals_p1_<set>_indeg.tsv.gz` (in-degree null), column `Z_ind_robust`: **opposes** = Z > 3 in BOTH nulls, **mimics** = Z < -3 in BOTH nulls. Sets: Q2 expression, Q4 expression, Q4 protein, Q5 expression, Q6
   (expression and protein share the one MYC seed; counted once, as set Q6), plus Q1 protein/expression, Q3, Q7 (expected zero). Levels are never merged across sets.
3. **Pool** = all seed-specific families of the sets above (opposes and mimics) + families in the P2 `direct_search` arms (kept as a diagnostic arm: they are hop-0 hits on a seed gene, i.e. the
   plain target search) + KNOWN reference families (section 4). Q1, Q3, Q7 have no seed-specific family; **no family is selected on the evidence of Q1, Q3 or Q7 alone** (they appear only through
   their direct-search arm, as references or as diagnostics).
4. **Unit**: a P2 'family'; families sharing one ChEMBL PARENT molecule are collapsed to that parent for selection (all family ids are kept in the table); DGIdb-only families are never merged by name.

## 2. Diagnostics (artefact flags; reported for every pool family, never used as a score)

* **Main target and hop**: the target carrying most of the family's |contribution| for its top contributing seed (`seed_engine.py explain`; hop 0 if the hop-0 term dominates).
* **Hub-ness** = in-degree + out-degree of the main target in the IT7 signed network. **Hub target** = degree at or above the 95th percentile of all 8,769 graph genes.
* **Promiscuity** = number of distinct signed targets of the family (`n_signed_targets`). **Promiscuous** = 5 or more (about the 90th percentile of the pool).
* **Cluster** = main target symbol. **Mechanism group** = first HGNC gene group of the main target (HGNC REST, gene symbols only; `NO_GROUP` if none, `UNKNOWN` if the service fails); groups are a
  reading aid, not a mechanism claim. **Hub-artefact cluster** = main target is a hub target, OR the median promiscuity of the cluster's members is 5 or more. A hub-artefact cluster is shown
  in `clusters.tsv` and may supply at most **2** selected families in total, labelled `artefact_control`, chosen to show the artefact rather than as biological candidates.
* **Seed-own-target** flag (P2 T3 logic): the main target is itself a seed gene (hop 0 on a seed). Such a family is a direct-search item, not a network finding.

## 3. Feasibility axis (kept SEPARATE from the biological-promise axis; an excluded family is listed with its reason and its promise columns)

Promise columns (never combined with feasibility): arm, question set, Z in both nulls, seed(s), hop, diagnostics. Feasibility is a set of exclusion tests applied after, from ChEMBL data fetched on the day
(`molecule` endpoint: `max_phase`, `molecule_type`, `oral`, `parenteral`, `topical`, `withdrawn_flag`, ATC classifications, `therapeutic_flag`, parent):
* **F1 cytotoxic anticancer**: ATC code L01A, L01B, L01C, L01D or L01XA (alkylating, antimetabolite, plant alkaloid/tubulin, cytotoxic antibiotic, platinum) OR a stated cytotoxic mechanism in the catalogue
  action text (topoisomerase, tubulin, DNA alkylation/synthesis). Targeted oncology agents (kinase, HDAC and similar inhibitors) are NOT excluded by F1; they are flagged `oncology_targeted` and judged
  case by case in the selection note (chronic neurological use requires a stated reason).
* **F2 topical/local only**: ChEMBL `topical` true and `oral` false and `parenteral` false, or ATC D, S01, S02, S03 only.
* **F3 modality outside this profile**: antibody, antibody-drug conjugate, vaccine, cell product, enzyme, oligonucleotide or protein/peptide (P4b qualifies small molecules; an ASO or peptide would need its own route).
  Listed as `modality`, not deleted.
* **F4 identity not resolved**: no ChEMBL parent (source-only record): cannot be profiled; UNKNOWN identity, not 'inactive'.
* **F5 no human exposure statement**: `max_phase` below 1 or absent AND no approved/clinical status in the catalogue (tool compounds, research probes). Reason is stated as 'no human exposure information',
  not 'unsafe'.
* **F6 withdrawn for toxicity** (`withdrawn_flag`): excluded.
* **Not an exclusion (flag only)**: CNS reach, potency, dose, brain exposure (unknown for most; qualified in P4b), approved-versus-clinical status, route.
Reference compounds (section 4) are exempt from F1 to F6 as reference points but keep their flags.

## 4. NEW versus KNOWN (rules)

* **Known to LEGEND** if the family/parent matches by ChEMBL id, normalised name or salt-stripped name any of: the 27 cards (`cards/*.card.json`, packets, `catalog/card_links.json`), IT8 P9 units and members
  (`unit_members.tsv`, `unit_map.tsv`), `uncarded_items.tsv`, `deepening_queue.tsv`, `needs/needs.json`, and the HEADINGS of the hypothesis ledger and discovery ledger (read through
  `registry_records.py catalog`, never grepped). Match type is recorded (card / unit member / queue / uncarded / need / ledger heading). A class-level match (another member of the same carded class) is
  recorded as `class_known`, distinct from `compound_known`.
* **Known to the specific question and the literature SEARCHED**: for every selected family, on the date of the run, PubMed (E-utilities `esearch`, count only) and Europe PMC REST (`resultType=lite`, count):
  (A) `"<name>" AND (WWOX OR WOREE)`; (B) `"<name>" AND (epilep* OR seizure* OR "developmental and epileptic encephalopathy")`; (C) the question's phenotype term set: Q2 `(glycolysis OR lactate OR "pyruvate dehydrogenase")`,
  Q4 `(interneuron OR "excitation inhibition" OR "GABAergic")`, Q5 `(myelin* OR oligodendrocyte* OR microglia* OR astrocyte*)`, Q6 `("radial glia" OR "neural progenitor" OR MYC)`; field `[Title/Abstract]` for PubMed.
  Only the compound name (and a synonym where the ChEMBL preferred name differs) and phenotype terms are sent; no operator identity, no e-mail address. Query string, date, perimeter and hit count are logged in
  `search_log.tsv`. A zero is written as 'no hits in this perimeter on this date'; never 'never attempted'. A non-zero hit count is a count, not a result: hits of query A are opened at title/abstract level to say
  whether they concern the compound in WWOX context; the others are only counted.
* **What it adds**: stated against the nearest known comparator (target, mechanism class, or card) in one sentence.

## 5. Selection algorithm (deterministic; implemented by `select_it9_p3.py`)

Target: **12 to 20 families**, no quota of favourable results; fewer than 12 is permitted if the pool cannot support it, and the reason is written.
1. Candidate set C = pool families (opposes/mimics only) that are NOT excluded by section 3, are not seed-own-target, and whose cluster is not a hub-artefact cluster.
2. Required representation, filled in this order while candidates exist: Q2 at least 2 (one opposes, one mimics if both exist); Q4 protein at least 2; Q5 at least 3; Q6 at least 2 (Q6 is one MYC seed: its
   weight in the final set is capped at 4); at least 4 opposes and at least 4 mimics overall; Q4 expression contributes only through the direct-search arm (it has no robust proposal) and counts as a reference.
3. Within each required slot, choose by lexicographic key: (a) mechanism group not yet represented in the selection; (b) the family's top seed not yet represented; (c) not `class_known` to LEGEND
   (new mechanism class first); (d) higher min(|Z_total|, |Z_indeg|), with |Z| capped at 20 so that a single hub-like seed cannot dominate by magnitude; (e) family id (determinism).
4. After the slots, fill to 12 to 20 by the same key across all sets.
5. **Class cap**: antiseizure drugs (ATC N03, or listed in cards F01, F04, H01 or units U17, U18, U20) plus NMDAR/AMPAR/T-type calcium channel siblings together may be at most **25 percent of the selected set**
   (references included); the share of each class is reported. If the cap binds, the lowest-ranked of that class is moved to `excluded.tsv` with reason `class_cap`.
6. **References**: the KNOWN compounds with a family present in any P2 table (any arm) are listed as reference points; up to **5** are included in the selected set, chosen as the closest to a P2 seed (a card
   whose target is reached by a seed-specific proposal first, then a direct-search hit), flagged `reference`; they count toward 12 to 20 and toward the class cap but never fill the quotas of step 2.
7. **Artefact controls**: up to 2 families from hub-artefact clusters (highest min|Z|), flagged `artefact_control`; they count toward the total.
8. Everything in the pool that is not selected is in `candidates_consolidated.tsv` with `disposition` (selected / excluded:<reason> / not_taken:<reason>); every excluded one is also in `excluded.tsv`.

## 6. What the first-pass profile contains and does not contain

Profile (light, fetched): ChEMBL parent id/name/max phase/molecule type/oral-parenteral-topical flags/ATC/withdrawn; GtoPdb or DGIdb-catalogue action and targets (from the catalogue rows already held and the
`compound_catalog.py` lookup; GtoPdb is queried by ligand name only if the catalogue holds no GtoPdb row); neural-relevance flags from the catalogue (`msig_neural_strict` LINCS state; the target's expression in
brain is NOT fetched here); existing cards. Not in the profile: potency against the target, brain exposure, dose, safety findings, counter-evidence, the WWOX-context data of the target: all in `p4b_work_order.tsv`.

## 7. Limits stated in advance

Thresholds (Z = 3, hub = 95th percentile, promiscuous = 5, Z cap = 20, class cap = 25 percent, 2 controls, 5 references) are judgment settings, not derived quantities; they are fixed here, not tuned on outcomes.
The cluster/mechanism-group assignment is mechanical and coarse. HGNC group lookup and ChEMBL/ATC fields may fail for some ids: the state is then `UNKNOWN` and the F-test is `not evaluable` (the family stays eligible
but flagged), never silently passed as 'feasible'.

---

## AMENDMENT 1 (2026-10-30, after step 1 of the pool build (`pool_build_it9_p3.py`: Z, main target, hop, degree), before any ChEMBL/ATC data, literature count or card match was looked at for a pool family, and before any family name was used)

Seen: aggregate counts only. Pool = 778 distinct families (Q2 124, Q4 protein 52, Q5 160, Q6 491; Q6 expression and protein are one set with one MYC seed). Hub target (degree >= 60) is the main target of
13 of 124 (Q2), 44 of 52 (Q4 protein), 96 of 160 (Q5) and 308 of 491 (Q6) proposals; all proposals are hops 1 to 3, none hop 0, none on a seed's own target. As written in section 2, 'hub target alone' would make
nearly all Q4, Q5 and Q6 clusters artefact clusters and leave the quotas of section 5 unfillable. But the Z used for seed-specificity is already a degree-matched-seed null, in which random seeds reach hub targets
as well, so a hub target is not by itself a failure of seed-specificity. Changes (all other rules unchanged):
* **Hub target becomes a FLAG and a tie-break, not an exclusion** (key (d) of step 3 gains a first sub-key: non-hub main target before hub main target; it is reported in every table).
* **Hub-artefact cluster (section 2) is redefined** as: main target is a hub target AND the median promiscuity of the cluster's members is 5 or more. Families that are individually promiscuous (>= 5 signed
  targets) are flagged `promiscuous`; a promiscuous family can be selected only as an `artefact_control` (still at most 2 in total).
* Step 1 of section 5 now reads: C = pool families not excluded by section 3, not seed-own-target, not `promiscuous`, and not in a hub-artefact cluster (new definition).
The comparison 'which clusters are artefacts of hubs' is kept in `clusters.tsv` under both the original definition (hub target alone, column `hub_target_share`) and the amended one (column `hub_artefact_cluster`).
