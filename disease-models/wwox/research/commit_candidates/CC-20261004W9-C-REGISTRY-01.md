# CC-20261004W9-C-REGISTRY-01 — registry landings for the six sources Scientist C read in intake wave 9

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist C of intake wave 9,
2026-10-04. **Change class: MINOR** (identity records only; no claim is touched).
**Nothing here is medical advice.** All numbers below are **provisional**: PAPER, LIT, CORPUS-STUB
and FT numbering moves as other branches land, and the integrator renumbers from
`registry_records.py catalog` at integration time. Highest ids seen on this branch at 2026-10-04:
`PAPER 216`, `LIT-0508`, `CORPUS-STUB-179`, `FT-177`.

Every PMID below needs a registry presence or LINT blocks BATCH_COMMIT with `ORPHAN_COMPLETE_READ`
once its receipt lands. Two of the six are **preprints keyed by DOI**, which have no PMID.

## 1 · Landings, per source

| # | Source | Receipt | Landing proposed | Why this landing |
|---|---|---|---|---|
| 1 | PMID 40183601 (Henry 2025, *Epilepsia*, 733-family paediatric epilepsy cohort) | `FTR-20261004-40183601-01` | **`PAPER 217`** in `paper_registry_current.md` | It carries WWOX primary data: four diagnosed individuals and the only measured RNA consequence for `c.107+119C>G` in the literature read so far. A full PAPER record, not a stub. |
| 2 | PMID 42738875 (Tang 2026, *Cells*, WWOX protein in plasma neuronal-enriched vesicles) | `FTR-20261004-42738875-01` | **`PAPER 218`** | First blood-accessible WWOX protein measurement; bears on the biomarker line. |
| 3 | PMID 42770556 (Lima 2026, *eLife*, PRMT1–SFPQ intron retention) | `FTR-20261004-42770556-01` | **`PAPER 219`** | WWOX-bearing mechanism source; also records a citation that does not support its own sentence. |
| 4 | PMID 42771216 (Köhler 2026, *J Neurooncol*, AAV delivery substrates) | `FTR-20261004-42771216-01` | **`CORPUS-STUB-180`** plus a `LIT-0509` line | WWOX occurs zero times: an earned null, read for a transferable method question only. A stub is the honest landing. |
| 5 | medRxiv preprint doi `10.64898/2026.01.16.26344264` (`PPR1269651`, optical genome mapping in 57 trios) | `FTR-20261004-PPR1269651-01` | **`LIT-0510`**, keyed by DOI with the PPR id, **labelled PREPRINT — NOT PEER REVIEWED** | No PMID exists; a preprint never earns a PAPER record and never raises a claim. |
| 6 | Research Square preprint doi `10.21203/rs.3.rs-9950101/v1` (`PPR1316475`, FASD GWAS) | `FTR-20261004-PPR1316475-01` | **`LIT-0511`**, keyed by DOI with the PPR id, **labelled PREPRINT — NOT PEER REVIEWED** | Same reason; the WWOX result is a common-variant modifier association on a parent-side haplotype, unreplicated. |

## 2 · Required content of each record

Each PAPER record must carry, at minimum: PMID, DOI, journal and year, the receipt event id, the
artefact path and full 64-hex sha256 as declared in the deep-dive manifest, the evidence depth
(`partial_fulltext_read` for all six), and one sentence of what the paper measures. Each LIT record
for a preprint must carry the DOI, the PPR id, the receipt event id, and the words *preprint, not
peer reviewed*.

## 3 · What must NOT be written

- No individual-level description of any case in any of these sources (public edition).
- No statement that the deep intronic allele's consequence is quantified — it is not (see
  `CC-20261004W9-C-DEEPINTRONIC-01`).
- No elevation of either preprint's content to a claim.

## 4 · Known registry statements to re-check at integration

`registry_records.py get --pmid` returned **no record on any surface** for all four PMIDs and both
DOIs before this reading, so no existing registry statement about these sources can be wrong. The
one correction this wave proposes to an existing surface is in
`CC-20261004W9-C-DEEPINTRONIC-01` §7 and concerns a selection note, not a registry record.

### LOCATOR TRIPLES FOR BLIND AUDIT

Not applicable: this candidate proposes identity records and asserts no scientific proposition. The
propositions behind each record are in the three sibling candidates of this wave.

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** paper_registry_current.md · literature_tracking_log_current.md

Three `PAPER` records, one `CORPUS-STUB`, and six `LIT` records. 🔴 **Renumbered:** the declared `PAPER 217`–`219` collided with group B's block and with landed records, and the declared `LIT-0509` was already taken by the previous batch; re-measured at `a405efc30550` and landed as **`PAPER 241`–`243`**, **`CORPUS-STUB-180`** (the declared stub number **held**, the ceiling being 179) and **`LIT-0533`–`0538`**. The two preprints are keyed by **DOI and PPR id**, labelled *PREPRINT — NOT PEER REVIEWED*, and given **no PAPER record by design**. `CORPUS-STUB-180` is written as an **earned null** and says so: WWOX occurs zero times in a paper that was genuinely read for a transferable-method question. Identity for all six came from the artefacts' JATS front matter, and **editors are excluded from every Authors field** — one paper had an Academic Editor and another two editor contribs. The integrator added a measured discrepancy the candidate could not have seen: the Research Square preprint's **cover page and manuscript byline print different first authors**, and the manuscript byline is the one used. § 3's prohibitions were honoured: no individual-level description, no claim that the deep intronic consequence is quantified, no elevation of either preprint.

**Not medical advice.**
