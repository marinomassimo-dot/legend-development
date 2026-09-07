# COMMIT CANDIDATE — mTOR: from "wrong direction" to INSUFFICIENT / not directly measured

**Candidate ID:** CC-20260826-MTOR-DIRECTION-01
**Status:** proposed — not integrated, not committed
**Base head:** `b80ae8b` (branch `lettore-b`; 0 behind / 20 ahead of `main`)
**Receipts:** none of its own. This candidate *removes* an interpretation; the reading it rests on is
the absence of a locator in `FTR-…-34268881` and in the manifest, dossier and commit candidate for
that paper.
**Author:** scientist-b

---

**CURRENT_TARGET**

Two sub-canonical sites, both verified this session:

1. `disease-models/wwox/research/discovery_ledger_current.md`, `DL-MECH-034`, line 691:
   *"**Altri assi alterati (DATO)**: … **autofagia ↓** (RB1CC1/FIP200, MDM2, RB1); **mTOR/EIF4EBP1 ↓**."*
2. `disease-models/wwox/analysis/mechanism_intervention_map.md`, `N-01 — mTOR inhibitors
   (rapamycin / everolimus) → **wrong biological direction**`, ranked **#2** in `TOP_NEGATIVE_FINDINGS`.

**🔴 CORRECTION TO THIS CANDIDATE'S OWN SITE COUNT — it is 4 sites, not 2**

The two sites named above were measured by locating the `N-01` *block*. A **phrase-level** sweep for
the retired verdict's wording — `wrong (biological )?direction` · `points? the wrong way` ·
`same (direction|way) as the lesion`, anchored within ±3 lines of an mTOR-family or `N-01` token,
over **436 tracked `.md`/`.json`/`.jsonl` files** at `bf88c1a` — returns **26 hits**. Of these,
**20 quote the verdict in order to retire it** (correctly typed, in the four analysis files and this
candidate), **1 already carries the correction** (`mechanism_intervention_map.md:31`), and
🔴 **5 assert it**, all in `mechanism_intervention_map.md`, at lines **116, 624, 625, 627, 811**.

They cluster into **three** blocks, and the ledger line makes a fourth site:

| Site | Location | Wording | Previously named? |
|---|---|---|---|
| **M0** | `discovery_ledger_current.md:691` (`DL-MECH-034`) | *"**autofagia ↓** … **mTOR/EIF4EBP1 ↓**"*, tagged **`(DATO)`** | ✅ "Site 1" |
| **M1** | `mechanism_intervention_map.md:112–120`, §2.2 *"Refused admission"* | *"would push the **same direction as the lesion**"* … *"**This is the single most consequential negative in the file**"* | 🔴 **NO.** §2.2 is named at line 32, but for a **count** defect — the directional assertion is named by nothing |
| **M2** | `mechanism_intervention_map.md:624–632` (`N-01` entry) | heading *"→ **wrong biological direction**"* · *"Failure mode: acts in the wrong direction"* · *"pushes the **same way as the lesion**"* | ✅ "Site 2" |
| **M3** | `mechanism_intervention_map.md:811–812` (`TOP_NEGATIVE_FINDINGS` #2) | *"**mTOR inhibition points the wrong way** (N-01)"* | ⚠️ implicitly — *"demote from `TOP_NEGATIVE_FINDINGS`"* never quotes this line |

🔴 **M1 survives any repair scoped to "the `N-01` block".** It sits in a different section, is not
labelled `N-01` at the point of assertion (it only cross-references *"See §5, N-01"*), and carries
the file's **strongest** wording. This is the failure mode of commit `b80ae8b` — *the verdict I
repaired in two files never reached the layer that carries it* — **recurring inside the repair
itself**.

**PROPOSED_DELTA — four sites**

| Site | Delta |
|---|---|
| **M0** | re-tag **`(DATO)` → `(DATO trascrittomico — non locatorato, non-FDR, n = 2/4)`**. The recorded direction is **preserved**; only its evidential type changes |
| **M1** | *"would push the **same direction as the lesion**"* → *"would push the **same direction as the only directional datum**, which is a **non-locatored transcriptomic signal at n = 2/4** and is **not a measurement of mTORC1 signalling**"*. And *"the single most consequential negative in the file"* → *"a negative whose **weight rests on one weak datum**"*. 🔴 **Preserve byte-for-byte** the block's correctly-bounded sentence: *"…`CORPUS-STUB-043` … status `not_processed`: **nobody has read it, so it cannot carry a direction** and is not cited here as evidence for or against."* |
| **M2** | failure mode and heading: *"acts in the wrong direction"* → **`INSUFFICIENT — mai misurato a livello proteico in alcun sistema WWOX`**. ⚠️ The block's existing *"Honest weight of the negative"* paragraph **already says this** and is preserved — **the heading contradicts its own body today** |
| **M3** | demote `N-01` out of `TOP_NEGATIVE_FINDINGS`; the replacement text must **not** assert a direction |

**No edit at `mechanism_intervention_map.md:774`** — the `DEPRIORITIZE` list names `N-01` without a
direction and is correctly bounded.

- **mTOR inhibitors remain out at every tier and stay in `DEPRIORITIZE`.** This candidate does not
  promote them. It changes *why* they are out — from *"it points the wrong way"* to *"nobody has
  measured it"* — and that difference decides whether the cheapest experiment in the portfolio (one
  blot, no intervention) is worth running.

**🔴 SCOPE FIREWALL — the axis this candidate must not touch**

| | **Axis 1 — mTOR therapeutic inference** *(under repair)* | **Axis 2 — proteostasis / CMA-autophagy** *(not under repair)* |
|---|---|---|
| **Question** | does mTORC1 signalling move in a WWOX-deficient neuron? | how is the **WWOX protein** degraded? |
| **Evidence** | one transcriptomic dataset, n = 2 vs 4, raw `P<0.01`, **no verbatim locator** | CMA, HSC70, LAMP1, chloroquine, 3-MA, K63 ubiquitination, P252A/Q230P — **locatored, independently evidenced, not in question** |

**They share the token `autophag`/`autofag` and nothing else.** A sweep on it would "repair" a chain
that is not in question while hunting a statement that lives in one line.

🆕 **The canonical layer refutes a single-mechanism autophagy reading by itself.** All three
`autophag` hits in the canonical registries are verbatim source titles pointing in **two opposite
directions** — `CORPUS-STUB-043` *"WWOX **activates** autophagy … by regulating mTOR"* (LPS lung
injury) · `CORPUS-STUB-056` *"…**inhibits** autophagy"* (paclitaxel, ovarian) · `CORPUS-STUB-139`
*"WWOX **suppresses** autophagy…"* (methotrexate, SCC). **All three are `not_processed`,
`Claim links: none`** — nobody has read them, so none can carry a direction.
*(This corroborates a correction already recorded at `mechanism_intervention_map.md:32`; it is
reported as independent confirmation, not as a new finding.)*

**CANONICAL SURFACE — re-measured, with the recipe**

**Population:** 436 tracked `.md`/`.json`/`.jsonl` at `bf88c1a`. **Family:** `\bmTOR\b` ·
`EIF4EBP1|4E-?BP` · `autophag|autofag` · `rapamyc|sirolim` · `everolim` · `\bLC3\b` ·
`SQSTM1|\bp62\b`, case-insensitive.

| Surface | mTOR | autophag | other 5 | Directional statements |
|---|---|---|---|---|
| `claim_registry_current.md` · `working_model_current.md` · `disease_model.md` · `state_manifest_current.md` | 0 | 0 | 0 | **0** |
| 🆕 `therapeutic_strategies_current.md` | **0** | **0** | **0** | **0** |
| `paper_registry_current.md` | 2 | 3 | 0 | **0** — all `**Full title:**` fields |
| `literature_tracking_log_current.md` | 2 | 3 | 0 | **0** — all `**Note:** Title:` fields |

> **`MTOR_CANONICAL_DIRECTIONAL_STATEMENTS: 0 / 10 hits · 5 unique records × 2 registries · all `not_processed` stubs`**

⚠️ **Two corrections to the prior measurement this candidate inherited.** *(i)* The
*"canonical layer is clean"* table covered **four** surfaces and never scanned
`therapeutic_strategies_current.md` — the therapeutic tracker, the most decision-facing surface.
It **is** clean, so the verdict survives, but a negative measured over a subset is a negative about
the subset. *(ii)* The bibliographic count of **8 (4 + 4)** re-derives as **10 (5 + 5)**; 8 is not
reproducible from any subset of the declared family, and no token set is being reconstructed to
justify it.

**CHANGE_CLASS:** MINOR — **at all four sites.** No canonical file is touched; no `BATCH_COMMIT` is
required.

**CANONICAL_TARGETS:** none. `discovery_ledger_current.md` is a designated non-canonical append-only
ledger; `mechanism_intervention_map.md` is analysis layer. **No file among the four scientific
current files is touched, and no `BATCH_COMMIT` is required.**

**DIRECT_EVIDENCE**

One bulk RNA-seq — hESC-derived WWOX-KO cerebral organoids, week 15, **n = 2 WT vs n = 4 KO**
(started 4 + 4; one WT failed QC, one excluded for not clustering), fold-change + **raw `P < 0.01`**,
**no FDR control**. No protein, no p-S6, no p-4E-BP1, no LC3-II/p62, no autophagic flux, no
rapamycin arm.

**LOCATORS**

🔴 **None exist, and that is the candidate.** `deepdive_manifests/PMID34268881.json` carries **12**
verbatim locators and **not one** touches mTOR, `EIF4EBP1` or autophagy; `fulltext_dossiers/PMID34268881.md`
never names them; `commit_candidates/CC-20260814-34268881-01.md` never names them. The sole
occurrence in the repository is the `DL-MECH-034` prose line.

**TRANSFER_BOUNDARY**

⚠️ **Deliberately empty.** TSC is not imported. The reflex *"genetic DEE ⇒ try an mTOR inhibitor"* is
the transfer this candidate exists to refuse. Two further boundaries, both measured this session:

- across **238 files** (whole disease model + every local full text) the words `rapamycin`,
  `sirolimus` and `everolimus` occur in **three files, all of them analysis files arguing this
  question**. Zero in any registry, ledger, manifest or primary;
- `claim_registry_current.md`, `working_model_current.md`, `disease_model.md` and
  `state_manifest_current.md` return **zero** mTOR-family hits. **The interpretation never reached
  the canonical layer.**

🔴 **Scope guard for whoever applies this.** Of the 84 `autophag`/`autofag` mentions in disease-model
markdown, a large share belong to the **WWOX-protein-turnover** axis — CMA, HSC70, LAMP1,
chloroquine, 3-MA, K63 ubiquitination, the P252A/Q230P chain, `4-PBA`/`TUDCA`. That axis is
independently evidenced, locatored, and **not in question**. It shares a word with the mTOR axis and
nothing else. **A token-level edit will damage it.** Touch only the two sites named above.

**THERAPEUTIC_EFFECT**

Zero movement in ranking. mTOR inhibitors stay out at every tier; no positive WWOX rationale exists;
no WWOX system has ever received one. **Only the reason changes** — *"nobody has measured it"*
instead of *"it points the wrong way"*. The first invites `E-D3` (one blot, no intervention, closes
the row); the second forecloses it. **This is a weakening of a negative, not a promotion of a drug
class.**

**REVIEW_REQUIRED:** Plan (integration of a ledger re-tag). Mirror **not** required — no baseline
claim, no block, no MAJOR classification in question.

**HUMAN_GATE:** none. No spend, no governance change, no canonical file, no clinical statement.

---

**REVIVAL_TRIGGER** (carried, so the negative does not become dogma)

*Reopen if a **protein-level** mTORC1 readout in a WWOX-deficient neuronal system — p-S6
(S235/236, S240/244) and the **p-4E-BP1 / total-4E-BP1 ratio**, with an assay-positive control —
shows mTORC1 **hyperactivation**; or if an autophagic **flux** measurement (LC3-II/p62 ±
bafilomycin A1) in a WWOX-deficient neuron fixes the sign of the WWOX→autophagy relationship.*
The trigger must fix a **sign**, not merely produce a number: the axis is directionally
undetermined, not merely unmeasured.

**Target WM:** none — no working-model change proposed.
**Batch gate:** not a `BATCH_COMMIT` object.
