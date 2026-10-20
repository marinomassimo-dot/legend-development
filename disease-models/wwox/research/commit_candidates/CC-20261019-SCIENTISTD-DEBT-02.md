# COMMIT CANDIDATE — CC-20261019-SCIENTISTD-DEBT-02

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), task `DEBT-WWOX-DIRECT-D-20261019` wave 2, branch `task/DEBT-WWOX-DIRECT-D-20261019`, 2026-10-20.
**context_policy:** `QUESTION_DRIVEN` for six readings, `SOURCE_FIRST` for three (named per paper in `debts_wave_20261019_scientist-d.md`, wave 2). **Not medical advice.** Class-level statements only; no individual-level record.
**target_wm_version:** `WM_v7.20_2026-10-04` · **Change class:** MINOR (one status line in one queue record, registry presence for six papers, resumed receipts for three; no claim status, baseline claim or working-model block is touched).

## 0 · Why

The first candidate (`CC-20261019-SCIENTISTD-DEBT-01`) queued the open, unread, gene-direct references of the papers read in wave 1. This candidate reports reading them: six new papers and three resumes of partial receipts (nine readings; none of the nine was left unread for want of a body). Two entries of that earlier queue list were wrong and are corrected: Hong 2009 (PMID 19484134) was already resumed by `scientist-a` in another task branch (not read here, to avoid a duplicate), and Park 2004 (PMID 15266310) already has a complete receipt.

## 1 · Ops — `full_text_queue_current.md` (one `replace-within`; dry run 2026-10-20 clean, one op, key `FT-090`)

```json
[
 {
  "op": "replace-within",
  "id": "FT-090",
  "old": "**Current status:** ⬜ aperto.",
  "new": "**Current status:** ✅ read, complete reading (2026-10-20, `CC-20261019-SCIENTISTD-DEBT-02`, receipt `FTR-20261019-25416187-01`; route: Internet Archive capture of the PMC author-manuscript page, no figure or table). Answer to this entry's question: the commentary summarises three reports (the SCAR12 families of Mallaret, the nonsense-variant family of Abdel-Salam, one unpublished family with no data) in support of 'germline WWOX variants are associated with neurological disease'; it adds no data of its own, describes no metabolic phenotype of the biallelic families, and its proposed seizure mechanism is a list of possibilities."
 }
]
```

The route is the finding for the queue: Europe PMC XML fails for author-manuscript PMC deposits, the PMC page and PDF sit behind a challenge, and the Internet Archive capture of the PMC page (raw bytes, `id_` modifier) carries the whole text and the figure blob URLs. It worked for five text surfaces in this task (Hsu 2009, Lin 2011, Huang 2016, Huang 2018, Tabarki 2015).

## 2 · Registry presence proposed (placeholders; the integrator mints ids)

| Placeholder | PMID | Short title | Depth | Registry state found |
|---|---|---|---|---|
| D09 | 25416187 | Tabarki 2015, WWOX and the developing brain (commentary) | complete | `CORPUS-STUB-034`, `LIT-0060`, `FT-032`, `FT-057`, `FT-090` (this entry's status op above) |
| D10 | 27999774 | Hsu 2016, HYAL-2/WWOX/SMAD4 review | complete | `CORPUS-STUB-032`, `LIT-0058` |
| D11 | 25686832 | Lee 2015, Zfra, Z cells and a Wwox heterozygote cure | partial | no record |
| D12 | 22484428 | Zhang 2012, WWOX in A549 cells, mitochondrial pathway | complete | `CORPUS-STUB-121`, `LIT-0140` |
| D13 | 27655721 | Cheng 2016, WWOX SNPs and oral cancer, Kozak variant | complete | `CORPUS P341`, `LIT-0341` |
| D14 | 25612104 | Ekizoglu 2015, WWOX in head and neck cancer | partial | `CORPUS P283`, `LIT-0283` |

Receipt event ids staged under `receipt_staging/scientist-d/`: `FTR-20261019-<PMID>-01` for the six new papers, and `-02`, `-02`, `-03` for the resumes of PMIDs 19918364, 26302329 and 24008736 (each names its prior receipt and `reread_reason: inadequate_prior_coverage`). The three resumed manifests gained appended artefacts and locators only; no persisted locator text was changed (`locator_contradiction_audit.py --working-tree --fail-on-undeclared` clean); the Tsai 2013 artefact note that said the supplement was not retrievable carries a "SUPERSEDED" sentence.

## 3 · Claim-level observations (all MINOR; none narrows or reverses a baseline claim)

- No claim in the registry carries the Zfra heterozygote "cure", the Kozak variant or the autophagy readout; nothing to annotate. `CLAIM 009` (mitochondrial quality control) is not moved: the two wave-2 papers that touch mitochondria (Zhang 2012, overexpression in one line with a cytosolic blot only; Tabarki's list of mechanisms) add no measurement after WWOX loss.
- If a later batch cites a Zfra "cure" of Wwox+/- tumours, or the oral-cancer Kozak mechanism, the manifests record the primaries' limits: one mouse with 70/75 percent inconsistency; a promoter-reporter read as translation, contradicted for expression by an independent tumour series.
- Tsai 2013 (autophagy): the only germline Wwox arm is one MEF blot pair (LC3-II 1.0, 1.9, 1.7 for +/+, +/-, -/-); with an unmeasured flux, it is at most a hypothesis-generating observation for WWOX and autophagy, and it is the sort of arm a WWOX-DEE genotype class could inherit.

## 4 · Parked in wave 2 (added to the wishlist of candidate 01, best value first)

| Order | PMID | Paper | Why | Route status |
|---|---|---|---|---|
| a | 16219768 | Chang 2005, J Biol Chem: WOX1 essential for TNF, UV, staurosporine and p53 death; Tyr33 form binds p53 | the primary behind the Tyr33/p53 model cited by several read papers | free to read (Unpaywall hybrid), publisher bot challenge; browser download |
| b | 12514174 | Chang 2003, J Biol Chem: JNK1 and WOX1 | cited by several read papers | free to read, bot challenge |
| c | 11058590 | Chang 2001, J Biol Chem: hyaluronidase induction of WOX1 | the cloning paper; cited by several read papers | free to read, bot challenge |
| d | 15629131 | Hsu 2005, Biochem Biophys Res Commun: Zfra cloning | the Zfra primary | closed |
| e | 15580310 | Chang 2005, Oncogene: estradiol and WOX1/WOX2 | steroid axis | closed |
| f | 27121845 | Alkhateeb 2016, Metab Brain Dis: families with WWOX, RARS2, C10orf2 variants | a human family report cited as a "null mutation" source | closed |

Not triaged for access: Cancemi 2011 (PMID 21520031) and Guo 2013 (PMID 23197378).

## 5 · Staged leads (not appended to the discovery ledger); all `IPOTESI`

1. **Flux control for the Wwox MEF LC3 arm.** Repeat LC3-II in Wwox +/+, +/- and -/- fibroblasts with and without a lysosomal inhibitor, three biological replicates. Falsifier: no genotype difference in flux.
2. **Same-tissue test of the Kozak variant.** Measure WWOX mRNA and protein by rs11545028 genotype in one tissue type with the allele frequency known (oral and head-and-neck tumours disagree). Falsifier: no difference in either.
3. **Heterozygous Wwox tumour incidence in an untreated cohort** with the same strain and a stated onset age, before any peptide effect is cited. Falsifier: the incidence equals wild type.

## 6 · Shared surfaces left to the Orchestrator

`pathograph`, `batch_queue`, `coverage_report` and `reading_state` not regenerated (commits carry `LEGEND_STALE_SURFACES_BECAUSE`).

### LOCATOR TRIPLES FOR BLIND AUDIT
Eight load-bearing triples were audited blind by a separate agent: six SUPPORTED (one with a note), one UNDERSHOOT-style wording point, one OVERSHOOT ("only" in a Tabarki proposition); narrowings applied before commit; table in `debts_wave_20261019_scientist-d.md`, section "Blind audit, wave 2".
