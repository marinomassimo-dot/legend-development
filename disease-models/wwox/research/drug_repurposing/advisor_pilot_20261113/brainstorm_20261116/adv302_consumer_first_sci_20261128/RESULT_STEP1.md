# ADV-302 step 1: catalogued-only records without a receipt that already have a consumer (SCI, window 64fc909a)

Written 2026-11-28T07:07:10Z. Rule and prediction: `PREREG_STEP1.md` (sha256 d792cb3da9b255815015f217d4909dc742a56d99a243e31bd18a0356b1f86cf1, frozen before the first count). Hypothesis level; not medical advice.

## Result

Population: 310 catalogued-only records, **185 without a receipt** (coverage_report at this tip; my own registry-block parse gives the same 185).
**8 of 185 are consumer-bearing** (prediction: at least 6, met). Count A (`consumer_count.py`) and count B (own fixed-string search of PMID, DOI, PMC id and `PAPER NNN`, 62 PMC ids from the NCBI converter included) name the same 8 records on the consumer surfaces; no record is hit by one count only on those surfaces.

Paths are under `disease-models/wwox/`. Line numbers are those of this tip. A "unit" is a distinct claim, section, lead or card after hand reading; a card and its packet count once; a bookkeeping note does not count.

| Record | PMID | Units | Where (file:line, unit) | What the units use |
|---|---|---|---|---|
| CORPUS P303 | 26041563 | 4 | research/discovery_ledger_current.md:447 (DL-MECH-025), :620 (FM-006); disease_model.md:33; registries/working_model_current.md:81 | its retraction status only |
| CORPUS P248 | 19465938 | 2 | research/discovery_ledger_current.md:97, :102 (DL-MOL-003), :208 (DL-MECH-008) | its result (direction of Wnt, WW-domain mechanism) |
| CORPUS P240 | 14695174 | 1 | research/drug_repurposing/cards/A02_proteasome_inhibitor_class.card.json:426 (and the packet:256) | its result (MG-132, truncated proteins), "abstract-level" |
| CORPUS P290 | 25703206 | 1 | research/discovery_ledger_current.md:1218, :1222 (DL-MECH-049). RP-006 (research_portfolio.tsv:7) is a bookkeeping note, not counted | its result; the ledger declares a complete reading of 2026-07-12 with no receipt |
| CORPUS-STUB-063 | 34015398 | 1 | research/discovery_ledger_current.md:110 (DL-MOL-004) | its result |
| CORPUS-STUB-114 | 25411445 | 1 | registries/claim_registry_current.md:631 (CLAIM 030) | its patient (not independent of another report); one of the papers waiting for the operator's supply, no lawful machine route |
| CORPUS-STUB-169 | 16818616 | 1 | research/discovery_ledger_current.md:3794 (DL-REPO-003) | its result |
| CORPUS P368 | 25720522 | 1 | research/discovery_ledger_current.md:3794 (DL-REPO-003) | its result |

## Outside the frozen rule (noticed, not counted)

* Records with **no identifier at all** that are cited by their corpus number: CORPUS P191, P204, P207, P214, P216, P218 (claim_registry_current.md lines 7, 470, 508, 525, 526, 560, 577; P204 also discovery ledger line 1629). Both counts are blind to a corpus number. Their registry entries say "deep-dived — registry placeholder", so they are not unread in the same sense, but no source can be re-opened from the entry. CORPUS P396 (PMID 23566416) is named by corpus number at discovery ledger line 506, as a caution.
* Records hit by count B only outside the consumer surfaces (queues, censuses, manifests, joins, analysis notes, open-questions map, dismissal ledger) are not counted. CORPUS-STUB-043 (PMID 36621327) is named in the dismissal ledger, the mechanism-intervention map and the open-questions map: a candidate for a wider consumer definition.

## Step 2 order (rule of the PREREG: units, then units stating a result, then PMID ascending)

1. P303 (26041563), 4 units. 2. P248 (19465938), 2 units. 3. P240 (14695174), 1 unit, lowest PMID among the one-unit records that state a result. Reserve order if a record has no lawful full text: 16818616, 25703206, 25720522, 34015398 (25411445 excluded: known no route).
