# Aldaz wave — verification standing of the fourteen readings

**Actor** ACTOR_ID `scientist` · **Date** 2026-09-28 · **Task** `a1-residue-repairs`
**Class** a bookkeeping record of **evidential standing**. It states no scientific fact, reverses
nothing, and touches no canonical file.

> **Why this file exists.** The decision-A1 reading census
> ([`vps_recovery_20260925/a1_reading_census_20260928.md`](vps_recovery_20260925/a1_reading_census_20260928.md))
> § 4 L7 found that the Aldaz wave's own closing report records **five of its fourteen readings as
> having received no dedicated independent verification pass** — and that **no record on `main` says
> so**. All fourteen readings are on `main`: their dossiers, manifests and commit candidates landed
> in recovery group G4.3 and were propagated by the Aldaz R-batches. So `main` presents fourteen
> readings of uniform apparent standing, when their standing is not uniform.
>
> The census's own judgement, adopted here: *"it is a bookkeeping fact about evidential standing
> rather than a scientific statement … but it is the one I would put in front of the operator anyway,
> because it is the kind of fact that is cheap to record now and unrecoverable later."*

## The five readings with no dedicated independent verification pass

| PMID | Standing |
|---|---|
| `27869163` | reading on `main`; **no dedicated independent verification pass** |
| `35409089` | reading on `main`; **no dedicated independent verification pass** |
| `24932569` | reading on `main`; **no dedicated independent verification pass** |
| `30619736` | reading on `main`; **no dedicated independent verification pass** |
| `15064722` | reading on `main`; **no dedicated independent verification pass** |

**Source.** `git show 06ee25a2e80ee61c8c7fd888bfbb51b6fc09f1d9:disease-models/wwox/research/2026-09-14_aldaz_final_report.md`
§ 3 — the wave's own closing report, i.e. the producer declaring its own coverage floor. The other
nine of the fourteen did receive a dedicated pass; those verification records are the 22-record
`verifications` group of the same decision-A1 set, which is **not on `main`** (decision A1) and is
read with `git show 06ee25a2e80ee61c8c7fd888bfbb51b6fc09f1d9:<path>`.

## What this does and does not mean

- ⚠️ **It is not a finding against any of the five readings.** No defect is asserted in any of them
  here, and nothing in them is withdrawn, weakened or re-statused. Several were subject to *other*
  forms of scrutiny — blind locator audits, Mirror consultations, machine schema verification — which
  are not the same thing as a dedicated independent verification pass and are not counted as one.
- 🔴 **It does mean their locators carry a different evidential standing from the nine**, and that a
  later reader must not infer uniform verification from uniform presence on `main`.
- 🟢 **Two of the five have since had specific defects found and repaired** by exactly the route this
  record exists to enable, which is evidence that the gap is real rather than nominal:
  - `35409089` — the figure-audit row in `fulltext_dossiers/PMID35409089.md` contradicted its own
    manifest `entries[58]`; repaired 2026-09-28 in this task (census § 3 C3), and the correction
    **strengthened** the paper's control rather than weakening it;
  - `30619736` — the largest enriched pathway behind it was at risk of being landed as strengthening
    `CLAIM 026`'s trafficking leg; adjudicated as **background-like and refused** in
    [`commit_candidates/CC-20260928-A1-RESIDUE-01.md`](commit_candidates/CC-20260928-A1-RESIDUE-01.md)
    (census § 4 L4).

## Disposition

**Recorded, not scheduled.** Whether any of the five earns a dedicated verification pass is a
prioritisation call for the Orchestrator, not a defect to be cleared: the readings are complete and
receipted, and three of the five have had no defect found by any route. This record exists so that
the choice is made knowingly.

`REVIVAL_TRIGGER`: any of the five being cited to narrow, reverse, corroborate or remove a
`consolidated baseline` claim, or to justify a MAJOR working-model bump — at which point
`legend-locator-audit`'s floor is reached on a reading whose independent-verification standing is
declared here rather than assumed.

**Not medical advice.**
