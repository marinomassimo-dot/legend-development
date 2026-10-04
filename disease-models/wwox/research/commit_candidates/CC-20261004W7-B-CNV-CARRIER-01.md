# COMMIT CANDIDATE — CC-20261004W7-B-CNV-CARRIER-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 7 2026-10-04, branch `task/sci-B-20261004w7`.
**context_policy:** `SOURCE_FIRST` — first pass written and committed from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261004w7_B.md`).
**Not medical advice.** Class-level statements about published patients and genotypes only.

## Target
- `claim_registry_current.md` · `CLAIM 032` (one copy of WWOX; carriers): one paragraph after the wave-5 carrier paragraph.
- `dismissal_ledger_current.md` (research/): **create** `DIS-035` after `DIS-034` (provisional number; last landed `DIS-034` measured by `registry_records.py catalog` 2026-10-04).

## Finding
(a) PMID 42807679: a de novo heterozygous ~13 Mb 16q23q24 deletion including WWOX in an infant with callosal dysgenesis, hydrocephaly and microcephaly. Examined: karyotype, array-CGH (hg18), inheritance. Not examined: the other WWOX allele, RNA, protein, follow-up. Contiguous-gene; not a WWOX-DEE allele-class observation and not a haploinsufficiency datum.
(b) PMID 41345172: a common intronic WWOX deletion (47 % in SANAD; gnomAD AF 0.339, 1447 homozygotes) with a nominal drug-response association, joined in the Results to a genome-wide-strength signal ~660 kb away. Not a disease-allele or dose datum; proposed as `DIS-035`.
(c) PMID 40429983's exon-5 copy **gain** is an allele in trans with a donor allele in a compound heterozygote — a biallelic genotype, not a carrier; it is recorded in `PAPER 203` and not here.

## Change class
**MINOR** — a qualification inside an `in observation` claim and one new dismissal; no status change.

## Registry records needed
`PAPER 204`, `PAPER 205` (created by `CC-20261004W7-B-REGISTRY-01`; renumber with it).

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on main 70513cd merged into the branch: exit 0, 1 op(s), anchors ['CLAIM 032'])

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 032",
  "old": "and neither is a demonstrated negative. `PREMISE: INFERENZA`.",
  "new": "and neither is a demonstrated negative. `PREMISE: INFERENZA`.\n🔴 **A third heterozygous observation with a phenotype — intake wave 7, 2026-10-04 (`CC-20261004W7-B-CNV-CARRIER-01`); again not a haploinsufficiency datum.** [[paper_registry_current#PAPER 204]] (PMID 42807679): a de novo heterozygous ~13 Mb 16q23q24 deletion including WWOX, ANKRD11 and CDH13 in a male infant with callosal dysgenesis, hydrocephaly and microcephaly (no epilepsy recorded). What was examined in the carrier: karyotype and array-CGH (hg18); inheritance. **Not examined:** the remaining WWOX allele (exome was done in six other patients), RNA, protein, follow-up. Dozens of genes are deleted, ANKRD11 among them, so the phenotype neither fires nor refutes the trigger above for WWOX. 🔴 **Not a dosage datum either way:** the common WWOX intronic deletion of [[paper_registry_current#PAPER 205]] (PMID 41345172; gnomAD AF 0.339, **1447 homozygotes**) removes no exon; its population frequency says nothing about losing one functional copy. `PREMISE: DATO + INFERENZA`."
 }
]
```

## Op list — `research/dismissal_ledger_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on main 70513cd merged into the branch: exit 0, 1 op(s), anchors ['DIS-034'])

```json
[
 {
  "op": "insert-after",
  "id": "DIS-034",
  "text": "\n### DIS-035 — «The common WWOX intronic CNV of PMID 41345172 is an epilepsy or WWOX-DEE dose datum» → ❌ **NOT SUPPORTED — a common polymorphism with a nominal association**\n- **PREMISE: DATO + INFERENZA:** the deletion (chr16:78,371,638-78,385,000, GRCh37) is intronic, carried at 47 % allele frequency in SANAD and homozygously by 1447 gnomAD individuals (Supplementary Figure 19); the paper used it to calibrate its CNV caller. Its own best association in Supplementary Table 4 is nominal (drug response, LRR univariate p = 1.68e-4; genotype p = 7.72e-3; every other phenotype p ≥ 0.037). The genome-wide-strength meta-p of 4.65e-22 sits at chr16:79,043,240, ~660 kb away; the Results sentence joins the two. The authors themselves ask for validation because of FRA16D. Read and recorded by `CC-20261004W7-B-CNV-CARRIER-01`.\n- **Confine:** this rejects a disease-allele or dose reading only. A modest pharmacogenetic association of a common CNV in new-onset epilepsy is untested here, not refuted.\n- **`REVIVAL_TRIGGER`:** replication at genome-wide significance in an independent cohort with orthogonal CNV genotyping (PCR or sequencing) of the deletion itself.\n"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the WWOX-including 16q deletion is heterozygous and de novo with callosal dysgenesis | P8 M1 M Dysgenesis of CC Hydrocephaly Microcephaly 46,XY Arr16q(74,718,513 87,891,103)x1 L L WWOX ANKRD11 ZNF778 CDH15 CDH13 De novo P | PMID 42807679, Table 3; files/fulltext/PMID42807679_Khadija2026_PMC.xml)
(exome sequencing covered six selected patients only | Whole-exome sequencing (WES) was performed in six selected patients whose clinical phenotype remained incompletely explained after chromosomal microarray analysis. | PMID 42807679, Methods; files/fulltext/PMID42807679_Khadija2026_PMC.xml)
(the common deletion recurs at 47 % in SANAD | In SANAD we re-discovered this intronic CNV in WWOX as common deletions with an allele frequency of 47% spanning the region chr16: 78,373,644 - 78,384,121. | PMID 41345172, Methods; files/fulltext/PMID41345172_De2025_PMC.xml)
(the strongest meta-analysis p lies at a different position | in the LRR based meta-analysis the meta-P value was 4.65x10-22 at chr16:79,043,240 | PMID 41345172, Results; files/fulltext/PMID41345172_De2025_PMC.xml)
(the authors ask for validation because of the fragile site | Since WWOX has a well-known fragile site (FRA16D27) further experimental validation is required to confirm these findings. | PMID 41345172, Results; files/fulltext/PMID41345172_De2025_PMC.xml)
(the deletion's best drug-response p in SANAD is nominal | SANAD_LRR_univariate chr16 78383363 drug_response -0.51500000000000001 0.17799999999999999 1.6799999999999999E-4 | PMID 41345172, Supplementary Table 4 sheet SANAD; files/fulltext/PMID41345172_De2025_supplement/41598_2025_28338_MOESM4_ESM_cells.txt)
