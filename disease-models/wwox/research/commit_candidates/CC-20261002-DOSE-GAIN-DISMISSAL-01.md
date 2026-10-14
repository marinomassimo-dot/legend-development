# COMMIT CANDIDATE — CC-20261002-DOSE-GAIN-DISMISSAL-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 2026-10-02, branch `task/sci-A-20261002`.
**context_policy:** `SOURCE_FIRST` for the six readings; the comparison with LEGEND's records was made after each first pass (see `research/intake_wave_20261002_A.md` § 1).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`research/dismissal_ledger_current.md` — four new entries after `DIS-020`: `DIS-022`, `DIS-023`, `DIS-024`, `DIS-025`. **The numbers are provisional**: `DIS-021` already exists (it sits at the head of the active list), and peer scientists of the same wave may take the next numbers. The integrator renumbers on collision and updates the two `PAPER` records of `CC-20261002-INTAKE-A-REGISTRY-01` that cite `DIS-022`, `DIS-023` and `DIS-025`.

## Change class
**MINOR** — four rejections recorded with premise and revival trigger (`epistemic_discipline.md` §2.1–§2.2). No current file and no claim status changes.

## Why
The brief framed the 16q23.1 duplication as LEGEND's first gene-**dose-gain** datum, and the ASD paper as a source of heterozygous WWOX **losses**. On reading, the duplication contains only WWOX's last exon, and the ASD case's deletion is intronic for the canonical transcript. Both are attractive readings that would otherwise be made again; one is repeated in the source's own abstract. `DIS-024` and `DIS-025` pre-empt two readings of the FoundHaplo paper that its text does not support. The re-audit rule (§2.3) applies to all four: each names what would reopen it.

## Op list — `research/dismissal_ledger_current.md` (record-scoped; dry run 2026-10-02 against `main` 2c35e3f: exit 0, 1 op, keys `['DIS-020']`; the editor reports `DIS-020`'s end as assumed because it is the file's last block, and the insert covers no heading)

```json
[
 {
  "op": "insert-after",
  "id": "DIS-020",
  "text": "\n### DIS-022 — «The 16q23.1 microduplication of PMID 24949445 is a WWOX gene-dose-gain datum» → ❌ **NOT SUPPORTED — the interval does not contain the gene**\n- **PREMISE: DATO + INFERENZA:** the source prints `arr 16q23.1 (77,445,915–78,190,209) dup` on NCBI36 (Table 4) and calls WWOX and MAF *«dose-sensitive genes»* it *«affects»*. Mapped to GRCh37 with Ensembl REST (reader's computation) the minimal interval is chr16:78,888,414–79,632,708, which holds only the last WWOX exon (exon 9) and the 3′ part of intron 8. The stated maximum size cannot reach exons 1–8. A partial 3′ copy adds no complete WWOX copy.\n- **Confine:** this rejects the dose-gain reading only. Whether the duplication disrupts anything depends on its structure, which the source does not report. Inheritance is unknown (no paternal DNA), and the phenotype (a language-dominant neurodevelopmental disorder with epilepsy that normalised on valproate) is outside the WWOX-DEE band.\n- **`REVIVAL_TRIGGER`:** a duplication containing the whole WWOX coding sequence, with segregation or expression data.\n\n### DIS-023 — «The ASD-case WWOX deletion of PMID 32081867 is a heterozygous null allele of WWOX» → ❌ **NOT SUPPORTED — intronic for the canonical transcript**\n- **PREMISE: DATO + INFERENZA:** the source describes it as involving *«the last exon of the two shorter gene transcript variants»* (NM_130791.3, NR_120436.1); its coordinates chr16:78,302,399–78,361,149 (hg19, Table S5) lie wholly inside canonical intron 5 on Ensembl GRCh37 (reader's computation). The call is not among the qPCR-validated CNVs.\n- **Confine:** an effect on WWOX expression or on the shorter isoforms is not excluded; it is not measured. The source's *«WWOX heterozygous variants act as weak risk factors»* rests on this case plus a citation, with no WWOX-specific statistic.\n- **`REVIVAL_TRIGGER`:** an expression or splicing readout in a carrier of this deletion, or a validated deletion removing canonical WWOX exons in an ASD case series with a controlled comparison.\n\n### DIS-024 — «PMID 40191585 shows that heterozygous p.Glu17Lys carriers are unaffected» → ⏸️ **NOT MEASURED**\n- **PREMISE: DATO:** the source reports 172 UK Biobank carriers by WES and **no phenotype of any carrier**; zygosity per carrier is not stated (*«FoundHaplo cannot determine the exact number of disease haplotype copies»*). The variant is a missense whose pathogenicity LEGEND classes UNASSIGNABLE. Under `CLAIM 032`'s `DO_NOT_INFER`, a missense heterozygote says nothing about haploinsufficiency in either direction.\n- **Confine:** absence of a reported phenotype is not a reported absence of phenotype.\n- **`REVIVAL_TRIGGER`:** any phenotype analysis (neurological, cognitive, EEG, seizure codes) of these carriers.\n\n### DIS-025 — «WWOX c.49G>A is a founder allele of the population named by PMID 40191585, per Weisz-Hubshman 2019» → ❌ **NOT SUPPORTED BY THE CITED SOURCE**\n- **PREMISE: INFERENZA (text-layer count with positive control):** Supplementary Table 1 of PMID 40191585 cites its reference 21 (PMID 30853297, `PAPER 025`) for the founder origin. The held PDF text layer of PMID 30853297 contains `c.49`, `49G`, `Glu17` and `E17K` zero times, while the control string `517-2` occurs 11 times. LEGEND's first-hand read of that paper attaches its only founder claim to a different allele. What PMID 40191585 does show — a 157 kb core haplotype shared by all 175 carriers it examined — is a founder effect among those carriers, unrelated to that citation.\n- **Confine:** a text-layer zero is bounded by the layer; a figure or table image in PMID 30853297 naming the variant would reopen this.\n- **`REVIVAL_TRIGGER`:** any primary source that reports `c.49G>A` in the named population with haplotype evidence.\n"
 }
]
```

## Reproduction of the coordinate computations (`PREMISE: INFERENZA`, reader's, free public reference)
- `GET https://grch37.rest.ensembl.org/map/human/NCBI36/16:77445915..78190209:1/GRCh37` → `16:78888414-79632708` (response sha256 `d18cc68b7f461b8966569153ad1ceee8a750552684e609c328bd6d2854246bcb`).
- `GET https://grch37.rest.ensembl.org/lookup/symbol/homo_sapiens/WWOX?expand=1` (sha256 `62e1eb90624465ad6697f7f82e2414d010e8621b3d0f0cc5ad9e18c31a9e6f97`): canonical ENST00000566780 exons — 5: 78,198,080–78,198,186 · 6: 78,420,757–78,420,845 · 7: 78,458,767–78,458,952 · 8: 78,466,385–78,466,649 · 9: 79,245,505–79,246,564.
- `GET …/lookup/symbol/homo_sapiens/MAF` (sha256 `a153c282c348fa6bc020c955c7e691c9c825e2f076e17a44ab331376f01823fc`): 79,619,740–79,634,611.

### LOCATOR TRIPLES FOR BLIND AUDIT
(the duplication's printed coordinates, build and inheritance | 1 Array CGH arr 16q23.1 (77,445,915–78,190,209) dup 0.744–0.827 Unknown | PMID 24949445, Table 4; files/fulltext/PMID24949445_Szymanska2014_PMC.xml)
(the coordinates are on NCBI36/hg18 | All genomic coordinates are based on the NCBI36/hg18 reference genome. | PMID 24949445, Patients and Methods; files/fulltext/PMID24949445_Szymanska2014_PMC.xml)
(the authors call WWOX and MAF dose-sensitive genes affected by the duplication | The duplication found in Patient 1 affects two dose-sensitive genes: WWOX (OMIM 605131) and MAF (OMIM 177075). | PMID 24949445, Discussion; files/fulltext/PMID24949445_Szymanska2014_PMC.xml)
(segregation is not established | The significance of this change in our patient is limited by the lack of paternal DNA and detailed clinical data about speech development in the father. | PMID 24949445, Discussion; files/fulltext/PMID24949445_Szymanska2014_PMC.xml)
(the case deletion involves the last exon of shorter transcripts | deletion involving the last exon of the two shorter gene transcript variants of the WWOX gene (NM_130791.3 and NR_120436.1) | PMID 32081867, Results; files/fulltext/PMID32081867_Bacchelli2020_PMC.xml)
(the case deletion's coordinates | E24=chr16:78302399-78361149 | F24=12 | G24=58751 | PMID 32081867, Supplementary Table S5; files/fulltext/PMID32081867_assets/41598_2020_59922_MOESM2_ESM_xlsxdump.txt)
(the WWOX weak-risk statement rests on a citation and this case | Rare CNVs overlapping WWOX have been reported at greater frequency in ASD cases versus unaffected controls6, thus suggesting that WWOX heterozygous variants act as weak risk factors, generally associated with milder ASD phenotypes, as in our case. | PMID 32081867, Discussion; files/fulltext/PMID32081867_Bacchelli2020_PMC.xml)
(172 carriers by WES, no phenotype reported | 172 individuals in the UKBB who carried the WWOX c.49G>A variant | PMID 40191585, Materials and methods; files/fulltext/PMID40191585_Robertson2025_PMC.xml)
(the founder table row for WWOX c.49G>A and its founder-origin citation | cephalopathy 28 DEE28 616211 WWOX c.49G>A AR WWOX coding | PMID 40191585, Supplementary Table 1 page 26; files/fulltext/PMID40191585_assets/lqaf033_supplemental_file_pymupdf.txt)
(all examined carriers share one core haplotype | All of the 175 WWOX c.49G>A carriers shared a core haplotype of 157 kb. | PMID 40191585, Results; files/fulltext/PMID40191585_Robertson2025_PMC.xml)

## BATCH DISPOSITION — `BATCH_20261002_001` (2026-10-02, ACTOR_ID `scientist`), append-only

**Nothing above this line was rewritten.**

**Verdict:** PROPAGATED

**MINOR** confirmed: four rejections into the non-canonical dismissal ledger, no canonical file and
no claim status touched. `DIS-022`–`DIS-025` held their provisional numbers (live highest was
`DIS-021`); `CC-20261002-BIOMARKER-REJECTIONS-01` had already moved to `DIS-026`–`DIS-029`, so no
renumbering was needed and the `PAPER` records of `CC-20261002-INTAKE-A-REGISTRY-01` that cite
`DIS-022`, `DIS-023` and `DIS-025` are correct as written. Applied as one `insert-after DIS-020`
merged with this wave's other dismissal block, so the ledger reads `DIS-022` … `DIS-029` in
numeric order; the editor refused the first form of that insert (`RESEGMENTATION`: the text had to
end with a newline) and the refusal was fixed rather than forced.
