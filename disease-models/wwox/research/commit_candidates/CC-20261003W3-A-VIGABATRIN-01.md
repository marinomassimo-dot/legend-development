# COMMIT CANDIDATE — CC-20261003W3-A-VIGABATRIN-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 3 2026-10-03, branch `task/sci-A-20261003w3`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w3_A.md`, which also declares two exposures before reading).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`claim_registry_current.md`: `CLAIM 001` (status `conflicting evidence`) — one appended line of efficacy observations, inserted after its `Impact on Working Model` line. Does not touch the sentence edited by the wave-2 `CC-20261003-A-VIGABATRIN-01`; dry-run applied cleanly both after that candidate and on bare `main`.

## Observations added
- PMID 37583270 (`PAPER 142`): predicted null/null compound genotype; failed initial hormonal therapy; clinical spasm control on vigabatrin; seizure-free at 12 months. Response is clinical (≥ 4 weeks cessation), no EEG criterion, no safety imaging.
- PMID 42092735 (`PAPER 144`): homozygous p.Leu239Arg; vigabatrin added to phenobarbital did not stop spasms; valproate then clobazam did.
- Not carried: the other three Nagarajan children responded to nitrazepam, zonisamide or nothing; no VABAM imaging is reported anywhere in this wave's sources.

## Change class
**MINOR** — adds two n = 1 observations in both directions; the status `conflicting evidence` and BLOCCO 1 position are unchanged; `CLAIM 001` is not a consolidated baseline claim.

## Ordering
The receipts named below must be appended to the ledger before this candidate is propagated, so that no record cites a receipt the ledger does not hold. Receipts: `FTR-20261003-37583270-01`, `FTR-20261003-42092735-01`. Propagate with or after `CC-20261003W3-A-REGISTRY-01` (the line links `PAPER 142` and `PAPER 144`).

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` c740c6e: exit 0, 1 op(s), keys ['CLAIM 001'])

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 001",
  "old": "**Impact on Working Model:** BLOCCO 1 safety position unchanged; BLOCCO 2 status updated to conflicting evidence",
  "new": "**Impact on Working Model:** BLOCCO 1 safety position unchanged; BLOCCO 2 status updated to conflicting evidence\n**Additional efficacy observations (intake wave 3, 2026-10-03, `CC-20261003W3-A-VIGABATRIN-01`):** (a) [[paper_registry_current#PAPER 142]] (Nagarajan 2023): one child with a predicted null/null compound genotype (frameshift + nonsense) failed initial hormonal therapy and reached clinical spasm control on vigabatrin, seizure-free at 12 months; response there is defined clinically (cessation ≥ 4 weeks) with no electrographic criterion, and no safety imaging is reported. (b) [[paper_registry_current#PAPER 144]] (Serce Pehlevan 2026): homozygous p.Leu239Arg — vigabatrin added to phenobarbital did not stop spasms; valproate then clobazam did. Both n = 1 per drug, different genotypes, short follow-up; neither changes the status. Not medical advice."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(a predicted null/null child failed hormonal therapy and responded to vigabatrin | 37 WWOX M FUA (2), ES (4) Absent MIC, C HYP FIHT, response with VGB ESC, SF (12) | PMID 37583270, Table 4 row 37; files/fulltext/PMID37583270_Nagarajan2023_PMC.xml)
(response means clinical cessation for at least four weeks | Response to treatment was defined by a complete clinical cessation of epileptic spasms lasting for at least 4‐week duration during the course of therapy. | PMID 37583270, Methods, Outcome measures; files/fulltext/PMID37583270_Nagarajan2023_PMC.xml)
(vigabatrin with phenobarbital did not stop spasms in the p.Leu239Arg child | Initially, vigabatrin was added to phenobarbital; however, the patient continued to experience epileptic spasms despite this combination. | PMID 42092735, Case Presentation para 5; files/fulltext/PMID42092735_SercePehlevan2026_PMC.xml)
(spasms stopped after clobazam was added | Following the addition of clobazam, the spasms completely subsided | PMID 42092735, Case Presentation para 5; files/fulltext/PMID42092735_SercePehlevan2026_PMC.xml)


---

## BATCH DISPOSITION — `BATCH_20261003_002` (2026-10-03, ACTOR_ID `scientist`, Scientist G), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED (MINOR — `CLAIM 001` is `conflicting evidence`, status unchanged)

Links renumbered: Nagarajan is `PAPER 143`, Serce Pehlevan `PAPER 145`. Blind audit: 4 triples, 3 SUPPORTED, 1 SUPPORTED_NARROWER — clobazam was added after valproate had already reduced the spasms and the remission is one month on combined therapy, which the op's *valproate then clobazam* already states.

**Not medical advice.**
