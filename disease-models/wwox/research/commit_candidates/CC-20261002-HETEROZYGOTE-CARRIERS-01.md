# COMMIT CANDIDATE — CC-20261002-HETEROZYGOTE-CARRIERS-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 2026-10-02, branch `task/sci-A-20261002`.
**context_policy:** `SOURCE_FIRST` for the six readings; the comparison with LEGEND's records was made after each first pass (see `research/intake_wave_20261002_A.md` § 1).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`claim_registry_current.md` · `CLAIM 032` (status `in observation`) — one appended qualification paragraph. Status, title, summary and source line are unchanged.

## Change class
**MINOR** (§ 7: block update without a policy change, on a non-baseline claim). It neither narrows nor reverses a `consolidated baseline` claim. No working-model change is proposed; the bump is the batch's to compute.

## Why
`CLAIM 032` already says human carriers have never had cognition, EEG or excitability assessed (`PREMISE: NOBODY_LOOKED`). This wave read four sources that each carry heterozygous carriers, and the most tempting one — 172 UK Biobank carriers of `p.Glu17Lys` — is a **missense** carrier set with **no phenotype reported**. Recording the four now, each with what it does not show, prevents any of them from being counted later as a negative for haploinsufficiency. They are cited by PMID because their `PAPER` records are created by `CC-20261002-INTAKE-A-REGISTRY-01`, whose numbers are provisional.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-02 against `main` 2c35e3f: exit 0, 1 op, keys `['CLAIM 032']`)
The `old` string is the closing sentence of the record's `DO_NOT_CITE` line. It occurs **once** in `CLAIM 032`, and the op adds one new line after it without moving any byte of that line (no `reflow`).

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 032",
  "old": "`REVIVAL_TRIGGER`: a powered survival comparison of a **null** heterozygote against wild type, or an EEG/cognitive endpoint in any WWOX heterozygote of any allele.",
  "new": "`REVIVAL_TRIGGER`: a powered survival comparison of a **null** heterozygote against wild type, or an EEG/cognitive endpoint in any WWOX heterozygote of any allele.\n🔴 **Human heterozygous carriers — intake wave 2026-10-02 (`CC-20261002-HETEROZYGOTE-CARRIERS-01`): four new carrier observations, none of them a demonstrated negative.** (a) **PMID 30746283** — both parents and an unaffected sib of a child homozygous for a canonical splice-donor allele (`c.409+1G>T`) are heterozygous carriers described as *«healthy»*; no examination, EEG or cognitive measure is reported, and the allele's splice consequence is untested. (b) **PMID 29390993** — the two parents of a compound heterozygote for a last-exon nonsense allele (`p.Gln354Ter`) and an intragenic exon 6–8 duplication each carry one allele, and they are asymptomatic **by an inclusion criterion** (*«offspring of asymptomatic … parents»*), not by a reported examination. (c) **PMID 32081867** — one control *«without psychiatric history»* carries an array-called heterozygous loss that, mapped on Ensembl GRCh37 (`PREMISE: INFERENZA` — reader's computation, not the paper's statement), spans canonical exons 6–7 and most of exon 8. It is the only exon-level, null-class heterozygote of the wave, and it is unvalidated by qPCR and neurologically unassessed. The same paper's ASD-case deletion lies inside canonical intron 5 and is **not** a canonical-exon loss. (d) **PMID 40191585** — 172 UK Biobank participants carry the **missense** `p.Glu17Lys` by WES, with zygosity per carrier unstated and **no phenotype reported**: this falls under the `DO_NOT_INFER` above, says nothing about haploinsufficiency, and is not an unaffected-carrier series. ⇒ `PREMISE: NOBODY_LOOKED` stands: no new carrier has a cognitive, EEG or excitability endpoint. The sentence of PMID 30746283 that *«one functional copy of the WWOX gene is sufficient for conducting normal neuronal activity»* is an inference from the zygosity of reported cases, not a measurement, and is not support for this claim. `REVIVAL_TRIGGER`: a phenotype readout (cognition, EEG, seizure history) in the UK Biobank `p.Glu17Lys` carriers, or in any carrier of an exon-level WWOX deletion.",
  "reflow": false
 }
]
```

## Dependencies
The receipts `FTR-20261002-30746283-01`, `-29390993-01`, `-32081867-01` and `-40191585-01` should be appended before this op, so the paragraph rests on persisted readings.

### LOCATOR TRIPLES FOR BLIND AUDIT
(heterozygous carriers of a homozygous splice-donor allele are reported healthy | Parents and healthy sister tested and they are carrier for the same mutation. | PMID 30746283, Result, first clinical report; files/fulltext/PMID30746283_Ehaideb2018_PMC.xml)
(the splice allele's consequence is untested | This mutation might cause intron sequence to be included in the mRNA or the elimination of exon. | PMID 30746283, Discussion; files/fulltext/PMID30746283_Ehaideb2018_PMC.xml)
(the authors' one-copy sentence is an inference from zygosity | All of these mutations are homozygous and most of them are located in or near the first WW domain, suggesting that one functional copy of the WWOX gene is sufficient for conducting normal neuronal activity. | PMID 30746283, Discussion first paragraph; files/fulltext/PMID30746283_Ehaideb2018_PMC.xml)
(parents are asymptomatic by inclusion criterion | and (7) offspring of asymptomatic | PMID 29390993, Methods, inclusion criteria; files/fulltext/PMID29390993_Rim2018_PMC.xml)
(one allele is a heterozygous nonsense variant called by PVS1 | AR NM_016373.2 c.1060C > T p.Gln354Ter Heterozygosity Pathogenic PVS1, PM2, PM3, PP4 | PMID 29390993, Table 1; files/fulltext/PMID29390993_Rim2018_PMC.xml)
(the other allele is an intragenic exon 6-8 duplication called without PVS1 | AR NM_016373.2 exon 6–8 duplication _ Heterozygosity Likely pathogenic PM2, PM3, PP4, PP5 | PMID 29390993, Table 1; files/fulltext/PMID29390993_Rim2018_PMC.xml)
(a control carries a heterozygous WWOX loss at these coordinates | C294=16 | D294=78386295 | E294=78466632 | F294=Loss | G294=WWOX | PMID 32081867, Supplementary Table S3; files/fulltext/PMID32081867_assets/41598_2020_59922_MOESM2_ESM_xlsxdump.txt)
(controls are defined only by absence of psychiatric history | without psychiatric history, recruited at the Division of Toxicology and Clinical Pharmacology, Headache Centre | PMID 32081867, Supplementary Methods; files/fulltext/PMID32081867_assets/41598_2020_59922_MOESM1_ESM.docx)
(the case deletion involves the last exon of shorter transcripts | deletion involving the last exon of the two shorter gene transcript variants of the WWOX gene (NM_130791.3 and NR_120436.1) | PMID 32081867, Results; files/fulltext/PMID32081867_Bacchelli2020_PMC.xml)
(172 UK Biobank participants carry the WWOX missense | 172 individuals in the UKBB who carried the WWOX c.49G>A variant | PMID 40191585, Materials and methods; files/fulltext/PMID40191585_Robertson2025_PMC.xml)
(carrier copy number is not determined by the method | Additionally, FoundHaplo cannot determine the exact number of disease haplotype copies in a test individual. | PMID 40191585, Discussion; files/fulltext/PMID40191585_Robertson2025_PMC.xml)
