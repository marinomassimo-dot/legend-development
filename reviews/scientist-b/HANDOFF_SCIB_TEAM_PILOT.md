---
artifact: HANDOFF — Scientist B, Pathograph scientific adjudication pilot
id: HANDOFF-20260825-SCIENTIST-B-TEAM-PILOT
status: OPEN — Phases I–III complete for this actor. **Phase IV cannot be performed by me** (§10
  requires a non-author) and **Phase V's producer is Orchestrator's to designate** (§15).
prepared_by: worktree `.claude/worktrees/lettore-b`, branch `lettore-b`
operating_authority: OPERATOR_DIRECTED_ANALYTICAL_PILOT. `roles/scientist.md` is `PROPOSED`;
  `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` records **OPTION B —
  `ACTIVATION_NOT_CONFIRMED`**, *"No actor authority may be assumed from these contracts"*
  (verified on `main` this session; the citation is Scientist A's, adopted because it is better
  sourced than my own derivation from the contract frontmatter). This handoff activates nothing.
canonical_mutation: NONE
lease: none held. `python3 framework/scripts/lease_state.py --check` → `ACTIVE by derivation: 0`
scope_rule: SCOPE NOT REDUCED. The 20-edge workset is measured, not chosen. Nine edges left
  unadjudicated are undone and declared, not out of scope.
---

# HANDOFF — Scientist B

**Public, disease-level, de-identified. Nothing here is medical advice. No canonical file was
written, no governance modified, no actor activated, no `BATCH_COMMIT` performed, no peer artifact
edited.**

---

## 1 · WORK COMMITS

| SHA | Subject |
|---|---|
| `2261a15` | The first-pass artifacts existed only on the surface nobody gates |
| `8612baa` | Eighteen of twenty edges are not causal, and the vocabulary that types them only types causal |
| `9ca69fe` | The independence rule and the commit-message convention cannot both be obeyed |
| `e8308d1` | The negative control passed and the surface was still wrong, and a peer found it |

Branch `lettore-b` is **not merged and must not be merged by its author.**

## 2 · ARTIFACT REFS

| Artifact | Role |
|---|---|
| `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_SCIB_v1.md` | Phase I first pass, **preserved byte-unchanged**, made durable at `2261a15` |
| `PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_SCIB_v1.md` | Phase I §4/§5/§7 — the 20-edge workset |
| `PILOT_PMID32000863_ADDENDUM_SCIB_v1.md` | Phase I — the eight §12 questions, re-verified |
| `SCIENTIST_OPERATING_PRACTICE_TEAM_PILOT_SCIB_v2.md` | Phase I §13 |
| `PHASE2_CROSS_REVIEW_SCIB_v1.md` | Phase II — review of A and C |
| `PHASE3_REVISED_SYNTHESIS_SCIB_v1.md` | Phase III — revised thesis + the composed account |
| this file | §17 closure |

All under `reviews/scientist-b/`.

## 3 · EXACT SOURCES

**Primary evidence** — read from the shared checkout's `files/`, which is `.gitignore`d, so a
branch carries the manifest and never the evidence.

| Source | Artifact | sha256 |
|---|---|---|
| Cheng *et al.* 2020 · PMID 32000863 | `PMID32000863_Cheng2020_PMC.xml` | `792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5` |
| — figure surface | `…_assets/40478_2020_883_Fig7_HTML.png` (1946×1627) | `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542` |
| — supplement | `…_Cheng2020_supplementary.pdf` | `0acb771cfe3a4c3644b41c10451504047adb715e69727c1889f72774151f8b7f` |
| Wang *et al.* 2012 · PMID 22193544 | `PMID22193544_Wang2012_PMC_JATS.xml` | `eb6f568d046f8df831d15e7f8795fcb1d6ac713ec6305f7ded3ad2a330388268` |
| Ludes-Meyers 2009 · PMID 19936220 | `PMID19936220_Ludes-Meyers2009_PMC.xml` | targeted verification read |
| Suzuki 2009 · PMID 19500159 | `PMID19500159_Suzuki2009.html` | targeted verification read |
| Suzuki 2007 · PMID 17803050 | `PMID17803050_Suzuki2007.html` | targeted verification read |

**Reading depth, declared per source:** PMID 32000863 and 22193544 read in full for the load-bearing
sections and their figures. The last three are **targeted verification reads** — each endpoint's
load-bearing quantity or negative matched verbatim against the artifact. They emit no
`FULLTEXT_READ_RECEIPT`, clear no reading debt, and change no recorded evidence depth.

**Canonical state:** `claim_registry_current.md` at blob `9f4bcede`, `paper_registry_current.md` at
`847879e0` — **byte-identical between this worktree and the shared checkout**, verified, which is
what makes the derivation reachable from here.

**Task surface:** `disease-models/wwox/analysis/pathograph_inventory.md` (sha256 `bbc09af4…`) and
`data/pathograph_export.jsonl` (`39e9a224…`), shared checkout, **UNTRACKED**.

## 4 · OBSERVATION_SCOPE

- **Adjudicated:** 11 of the 20 declared edges with primary evidence; all 20 classified at the
  declaration level; PMID 32000863 re-verified in full against its artifacts.
- **Not adjudicated:** 9 edges — 6 disposed at declaration level (no proposition), 3 genuinely
  blocked on absent full texts (PMID 29808465, 24369382, 30361190, 27495153, 24456803).
- **Not read, deliberately:** `reviews/mirror/PATHOGRAPH_HOSTILE_REVIEW_MIRROR_v1.md` — Mirror's
  plane (§14).
- **Not performed:** node decomposition (recorded as candidates only); Phase IV; Phase V; any
  canonical mutation.
- **Reproducibility boundary:** `files/` is git-ignored. Every registry claim here is verifiable from
  any checkout; **no evidential quotation is**, on any machine but this one.

## 5 · UNRESOLVED — preserved, not closed

1. 🔴 **Phase II is one-third done and must not be recorded as agreement.** §8 is symmetric: A reads
   B and C, B reads A and C, C reads A and B. **I have read A and C. Neither has read me.** Two of
   my Phase II findings — that the Pathograph exists and C's sweep was worktree-confined; that A's
   gate verdict decayed 6 min 23 s before publication — are **unrebutted, not accepted.**
2. **Whether the `Wwox−/−` Ser9 fall is WWOX-proximal or systemic.** Three complementary objections
   compose into one alternative account (Phase III §2); none refutes the observation. One experiment
   settles it: pGSK-3β(Ser9) in pair-fed or glucose-clamped nulls, or in a brain-restricted
   conditional that is not systemically ill.
3. **Whether the ethosuximide genotype restriction survives exposure matching.** C's confound —
   ETS a single 150 mg/kg dose, LiCl 3 × 60 mg/kg — is real and untested, and the canonical evidence
   boundary leans on the contrast.
4. **Whether `ASSOCIATED` is the right token or the vocabulary is the wrong instrument.** A and I
   agree on the token inside a vocabulary all three of us report as insufficient.
5. **Whether breadth or depth is the right Scientist unit of work.** I adjudicated 11 edges; A
   adjudicated 1 to a depth I reached on none. §15 puts that with Orchestrator.

## 6 · OWED TO OTHER ACTORS

**To Orchestrator (§15).**
- Acquire five full texts blocking six edges: **PMID 29808465** (PAPER 041, the load-bearing Q230P
  functional source, `Evidence depth: abstract only — full text paywalled`, and **three** edges rest
  on it while CLAIM 019 is `consolidated baseline`), 24369382, 24456803, 30361190, 27495153.
- Decide whether the Pathograph — generator, inventory, export, plus uncommitted edits to
  `analysis/README.md` and `DATA_SOURCES.md` — may remain on an untracked surface. It is on **0 of
  50 refs** here (**0 of 57** by A's and C's better denominator, which includes tags and the stash).
- Designate the Phase IV hostile reviewer and the Phase V producer.
- Route the four canonical defects to `BATCH_COMMIT`.

**To Plan (§16 bars me).** A second relation plane. Eight of twenty edges carry real, sourced
relations the causal vocabulary cannot express, and **nine of seventy paper records already write
them, in seventeen free-text qualifiers** — `refutes its imported premise for the mouse`,
`bounds its imported premises`, `supplies the functional assay`, `tensions`. The assembler flattens
all seventeen into one `claim_links` kind. **The vocabulary exists and is unparsed.**

**To Mirror (§14).**
- 🔴 **The independence rule and the commit-subject convention cannot both be obeyed.** The mandated
  existence check reads peer branches; this repository states its findings in subject lines. I read
  one and declared it (Phase I §10.2).
- 🔴 **The repository pre-contains the §12 answers** — `locator_contract_live_test.md:375–395`,
  tracked since 2026-08-04, plus CLAIM 016's own `Evidence boundary`. Independence audits must test
  against the tracked tree, not only actor-to-actor contact.
- **The Phase II gate is a race.** Three actors, three instants, three verdicts, each correct when
  taken.
- **A wrong-reason success:** `therapy_levers.md` A2 reaches the right word — *genotype-agnostic* —
  by the wrong derivation, alongside *"abolishes seizures"* and a mechanism attribution the
  experiment does not establish.
- **Three canonical surfaces disagree about four readings:** `paper_registry_current.md` says
  `full text reviewed`, `reading_state.md` says `partial_fulltext_read`, and the receipts are legacy
  reconstructions whose `evidence_basis` is *the paper registry's own declaration*. Zero artifacts,
  zero manifests. Extends Scientist A's finding.

## 7 · CANONICAL DEFECTS — found, located, NOT applied

| # | Defect | Locator |
|---|---|---|
| 1 | CLAIM 016 cites `Fig. 7b` for a `Fig. 7d` result — **the only figure-panel citation in the entire claim registry**, and it routes a verifier to the panel that appears to refute the claim. ⚠️ Not a `7b → 7d` swap: the parenthetical is compound and its second clause is genuinely about `7b` | `claim_registry_current.md:300` |
| 2 | CLAIM 016 `Summary`/`Type` say *"elevated"* / *"abbondanza"* where the panel shows flat abundance and falling Ser9. Present in **14** tracked files at HEAD; **1** of the 14 states the correction. The working-model mirror at `:164` is **half**-corrected, the claim not at all | `:296`, `:297`, `working_model_current.md:164` |
| 3 | CLAIM 016's molecular evidence is a pS9 western; CLAIM 035 declares that assay produces a **false negative** in exactly that setting. The two claims are wikilinked and neither names the other on this point | `:296` ↔ `:637` |
| 4 | `therapy_levers.md` A2 — *"abolishes seizures"*, mechanism attributed to GSK-3β inhibition | `therapy_levers.md:17` |

All four require `BATCH_COMMIT` and the operator. **§16 observed in full.**

## 8 · GRAPH CONTRIBUTIONS (§17 G)

| Class | Count | Which |
|---|---|---|
| Ready for later integration | 2 | `009↔034` as `CONTROVERSIAL_OPEN`; `016↔035` as **`ASSOCIATED`** (revised from `INDIRECT_UNKNOWN_INTERMEDIATES` on A's argument), direction `035 → 016` only |
| Relation unsupported | 14 | 10 with no proposition in their declaration; 4 with a non-causal proposition and no governed type |
| Relation unresolved | 1 | `036↔038` — a real mechanistic fork, wrong object for `CONTROVERSIAL_OPEN` |
| Additional source required | 3 | `001↔002`, `019↔032`, `031↔032` |
| **Architecture-sensitive** *(flag, cuts across)* | 5 | `005↔036`, `005↔037`, `028↔034`, `028↔035`, `030↔035` |

**Retracted:** the claim that the PMID 22193544 manifest carries a locator defect. It does not —
9 of 9 match strictly. The 2/9 was my own tag-stripping. Scientist A found it.

---

*Non-canonical. Nothing here is medical advice. No canonical file was modified in producing it.*
