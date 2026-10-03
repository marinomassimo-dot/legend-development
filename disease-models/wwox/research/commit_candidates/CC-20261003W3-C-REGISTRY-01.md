# CC-20261003W3-C-REGISTRY-01 — registry landing for the six PMIDs of intake wave 3, group C

- `context_policy: SOURCE_FIRST`
- Purpose: give every PMID this reader handled a structured registry presence, so that
  `legend_lint.py` does not raise `ORPHAN_COMPLETE_READ` once the six receipts are appended to
  `fulltext_read_receipts.jsonl`. Wave 1 left eight PMIDs without one and the LINT blocked
  `BATCH_COMMIT` until they existed; this candidate is written so that does not recur.
- Change class: **MINOR**. Additive records in two registries plus two year corrections; no claim is
  created, narrowed or reversed.
- **Numbers below are provisional.** They were measured with
  `python3 framework/scripts/registry_records.py catalog` at commit `0e6fd4e9b886`
  (1,313 records projected): highest `CORPUS P` = **P400**, highest `PAPER` = **132**, highest
  `LIT-` = **LIT-0431**, highest `FT-` = **FT-192**, highest `CLAIM` = **042**. Other branches land
  continuously, so the integrator must re-run `catalog` after merging `main` and renumber before
  applying.

## Which PMIDs need what

| PMID | Registry presence today | Needed |
|---|---|---|
| 41124647 | **present** — `CORPUS P348` and `LIT-0348` | no new record; two year corrections, proposed in `CC-20261003W3-C-ALLELE-CLASS-01` |
| 40349107 | none (`registry_records.py get --pmid 40349107` → NO RECORD MATCHED) | one paper-registry record + one tracking-log record |
| 39847501 | none | one paper-registry record + one tracking-log record |
| 40263630 | none | one paper-registry record + one tracking-log record |
| 42181696 | none | one paper-registry record + one tracking-log record |
| 42521212 | none | one paper-registry record + one tracking-log record |

"NO RECORD MATCHED" is a statement about that query over those files, not evidence that the
laboratory does not know the paper.

## Ops (provisional)

### `disease-models/wwox/registries/paper_registry_current.md` — five `append` operations

Each appended under the heading that carries the corpus stubs, addressed with
`"heading": "<the corpus section heading>", "under": "Paper Registry Current"` because that file
carries duplicated headings. Each record follows the shape of `CORPUS P348`, and each carries its
PMID **and** its record id in the same section, which is what the orphan check looks for.

| id (provisional) | PMID | Short title | Year | Journal | Tier | Status | Primary pathway | Species / model | Role |
|---|---|---|---|---|---|---|---|---|---|
| `CORPUS P401` | 40349107 | Neuron-targeted gene therapy rescues multiple phenotypes of STXBP1-related disorders… | 2025 | Mol Ther | C | read — partial (receipt `FTR-20261003-40349107-01`) | P-TX — delivery and vector engineering | mouse + nonhuman primate | transferable-method corpus; **not a WWOX paper** |
| `CORPUS P402` | 39847501 | Neonatal but not juvenile gene therapy reduces seizures and prolongs lifespan in SCN1B-Dravet syndrome mice | 2025 | J Clin Invest | C | read — partial (receipt `FTR-20261003-39847501-01`) | P-TX — delivery and timing | mouse | transferable-method corpus; **not a WWOX paper** |
| `CORPUS P403` | 40263630 | Antisense oligonucleotide treatment in a preterm infant with early-onset SCN2A developmental and epileptic encephalopathy | 2025 | Nat Med | C | read — partial (receipt `FTR-20261003-40263630-01`) | P-TX — route, schedule and n-of-1 architecture | human, n = 1 | transferable-architecture corpus; **not a WWOX paper**; article type includes Case Reports |
| `CORPUS P404` | 42181696 | AAV9-mediated targeting of natural antisense transcript as a novel treatment for Dravet syndrome | 2026 | Mol Ther Nucleic Acids | C | read — partial (receipt `FTR-20261003-42181696-01`) | P-TX — transcript upregulation | mouse | transferable-method corpus; **not a WWOX paper** |
| `CORPUS P405` | 42521212 | Augmenting and Assaying Nav1.1 Protein Quantity for Dravet Syndrome Therapy | 2026 | Ann Clin Transl Neurol | C | read — partial (receipt `FTR-20261003-42521212-01`) | P-BIO — pharmacodynamic assay | human iPSC | transferable-method corpus; **not a WWOX paper** |

Each record carries, in its `**Note:**` field, the sentence that keeps it honest:
*"Carried for a transferable lesson from a different gene. The transfer limit is stated in the
dossier; no datum from this paper bounds a WWOX claim without that limit restated."*

### `disease-models/wwox/registries/literature_tracking_log_current.md` — five `append` operations

`LIT-0432` … `LIT-0436`, one per PMID in the same order, each with: identifier line
(`PMID … / PMC… / DOI …`), date discovered and screened `2026-10-03`, discovery window
`intake wave 3 2026-10-03 (C)`, discovery source `Orchestrator wave-3 selection, group C`,
tier `C`, status `screened`, filter decision `transferable-method corpus`,
`**Directness to the reference genotype:** indirect — different gene`,
`**Over-inference risk:** HIGH — the single named risk is importing a dose, a window or a
tolerability statement from another gene without its transfer limit`,
`**Claim links:** none`, `**Working Model impact:** none`, and the matching `CORPUS P4NN` link.

## Verification after application

```bash
python3 framework/scripts/registry_records.py get --pmid 40349107   # and the other four
python3 framework/scripts/legend_lint.py .                          # no ORPHAN_COMPLETE_READ
python3 framework/scripts/growth_anchors.py check
```

### LOCATOR TRIPLES FOR BLIND AUDIT

None. This candidate asserts no scientific proposition: it proposes bookkeeping records whose content
is the identity metadata of the six papers and a pointer to each dossier. Every scientific
proposition drawn from these papers is carried, with its triples, in
`CC-20261003W3-C-ALLELE-CLASS-01` and `CC-20261003W3-C-RESTORATION-SPEC-01`.


---

## BATCH DISPOSITION — `BATCH_20261003_002` (2026-10-03, ACTOR_ID `scientist`, Scientist G), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** DEFERRED

Its ops are a prose specification (a table of field values and a description of the LIT records), not an executable op list, and the numbers it declares (`CORPUS P401`–`P405`, `LIT-0432`–`0436`) were already taken (`LIT-0432`–`0443` exist after this batch). Nothing is owed urgently: the five PMIDs it would register carry `partial_fulltext_read` receipts only, so `legend_lint.py` raises no `ORPHAN_COMPLETE_READ` and `test_batch_queue.py` does not count them (measured on this branch). **Unblock:** an executable op list — five `insert-after CORPUS P400` records and five `LIT-` records after the highest `LIT-` then present — written against a fresh `registry_records.py catalog`.

**Not medical advice.**

---

## BATCH DISPOSITION — `BATCH_20261003_004` (2026-10-03, ACTOR_ID `scientist`, Scientist I), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED — the DEFERRED disposition of `BATCH_20261003_002` is superseded by this batch, which wrote the executable ops its predecessor asked for. Class **MINOR**.

**Renumbered and authored.** The declared `CORPUS P401`–`P405` were **still free** (highest `CORPUS P` measured 400) and were applied as declared; the declared `LIT-0432`–`0436` were long taken and became **`LIT-0471`–`0475`**. The five corpus records and five tracking-log records were **authored by the integrator** from this candidate's field tables — short and full titles, year, journal, tier, status, pathway, species and role — with DOIs taken from each reading's own receipt rather than invented, and each record naming this candidate as its origin.

**Depth labels off the receipts:** all five PMIDs are `partial_fulltext_read`, and every record also carries the literal *partial full text*. PMID 41124647 needed no new record, exactly as the candidate said.

**Not medical advice.**
