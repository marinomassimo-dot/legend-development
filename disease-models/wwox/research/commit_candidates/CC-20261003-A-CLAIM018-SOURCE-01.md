# COMMIT CANDIDATE — CC-20261003-A-CLAIM018-SOURCE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 2 2026-10-03, branch `task/sci-A-20261003`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003_A.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`claim_registry_current.md` · `CLAIM 018` (`consolidated baseline`) — the `Source` line only.

## What changes
The Source line names *«Weisz-Hubshman / Piard 2019 abstract-supported»*. *Piard* was the byline wrongly carried by `PAPER 025` (Weisz-Hubshman 2019) until 2026-09-27. The Piard 2019 paper (PMID 30356099) was read in full with its four supplementary tables on 2026-10-03: `c.517-2A>G` occurs **0** times (scratch search of the body text and the four tables, all zero). The repair names Weisz-Hubshman alone, at the depth the PAPER 025 record now carries.

## Change class
**MAJOR, taken conservatively** (DEFAULTS_TAKEN): the conclusion and status do not move, but a named source is removed from a consolidated baseline claim, which narrows its evidence line. If the integrator judges a mis-attributed byline to be a citation repair rather than a narrowing, it may run as MINOR. The removed source supported nothing, so no blind audit of a quote is possible for it; the triple below anchors the absence claim's counterpart in the source that does carry the allele.

## Registry landing
PMID 30356099 → `PAPER 117`; PMID 30853297 → `PAPER 025` (both exist).

## Ordering
The receipts `FTR-20261003-<pmid>-01` named below must be appended to the ledger before this candidate is propagated, so that no record cites a receipt the ledger does not hold.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-03 against `main` f5f9468 with `record_scoped_edit.py apply`: exit 0, 1 op(s), keys ['CLAIM 018'])

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 018",
  "old": "**Source:** Weisz-Hubshman / Piard 2019 abstract-supported + prior claim integration",
  "new": "**Source:** Weisz-Hubshman 2019 ([[paper_registry_current#PAPER 025]], PMID 30853297; measured blood-cDNA RT-PCR, read at body depth) + prior claim integration. 🔴 Source line repaired 2026-10-03 (`CC-20261003-A-CLAIM018-SOURCE-01`): *«Piard 2019»* was the byline borrowed by PAPER 025 until 2026-09-27; the Piard 2019 paper (PMID 30356099) contains **no** `c.517-2A>G` in its body or its four supplementary tables (0 matches, `FTR-20261003-30356099-01`), so it supports nothing in this claim. The conclusion and status are unchanged."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the Piard 2019 genotype-phenotype paragraph names its null genotypes without any exon-6 splice allele | These genotypes are observed in seven patients: homozygous deletion of exon 1 to 4 in P10 | PMID 30356099, Discussion, Phenotype/genotype correlations; files/fulltext/PMID30356099_Piard2019_EPMC.xml)
