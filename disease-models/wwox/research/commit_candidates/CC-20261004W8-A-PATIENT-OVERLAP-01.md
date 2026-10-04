# COMMIT CANDIDATE — CC-20261004W8-A-PATIENT-OVERLAP-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 8 2026-10-04, branch `task/sci-A-20261004w8`.
**context_policy:** `SOURCE_FIRST` — first passes written before comparison; the L239R counting rule (`CC-20261003W3-A-L239R-01`, `CC-20261003W5-B-PATIENT-OVERLAP-01`) was read only after the first pass of PMID 41835067.
**Not medical advice.** Class-level statements only.

## Target
`paper_registry_current.md`: `PAPER 117` (Piard 2019) and `PAPER 013` (Sunnetci-Akkoyunlu 2025).

## Finding
1. **PMID 37946251's WWOX case = Piard 2019 Patient 11 (DATO).** The later paper's own Table 1 says so; the held Piard Supplementary Table 1 (read cell-wise) gives Patient 11 the same genotype, `c.[517_1056del];[705dupG]`. Count once. Note also that `PAPER 174` (a review) already uses Piard 11 among its six genotypes.
2. **PMID 41835067's homozygous p.Leu239Arg child may be `PAPER 013` case 50 (INFERENZA).** Both female, both from consanguineous families, recruitment windows compatible; neither source prints enough (syndrome, EEG, onset, family structure) to confirm or exclude. Counted once under the standing rule.

## Registry records needed
`PAPER 208`, `PAPER 210` (created by `CC-20261004W8-A-REGISTRY-01`; renumber with it).

## Change class
**MINOR** — annotations on two paper records; no claim, block or baseline touched.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on this branch: exit 0, 2 op(s), keys ['PAPER 117', 'PAPER 013'])

```json
[
 {"op": "replace-within", "id": "PAPER 117",
  "old": "**Note:** Erratum `PMID 30783266` is linked",
  "new": "**Patient overlap (2026-10-04, `CC-20261004W8-A-PATIENT-OVERLAP-01`):** Patient 11 (in-frame deletion of exons 6-8 + `c.705dup`) is re-reported as the WWOX case of [[paper_registry_current#PAPER 208]] (PMID 37946251), whose Table 1 names it 'Patient 11 (Table S1) in case series in Piard et al'; same genotype in this paper's Supplementary Table 1. One patient, counted once (DATO: the later authors state the identity).\n**Note:** Erratum `PMID 30783266` is linked"},
 {"op": "replace-within", "id": "PAPER 013",
  "old": "never as independent replications without author confirmation (`CC-20261003W3-A-L239R-01`).",
  "new": "never as independent replications without author confirmation (`CC-20261003W3-A-L239R-01`). 🔴 **Update 2026-10-04 (`CC-20261004W8-A-PATIENT-OVERLAP-01`):** a third source, [[paper_registry_current#PAPER 210]] (PMID 41835067), reports one homozygous p.Leu239Arg female child of a consanguineous family with neonatal-onset seizures, reached through a cerebral-palsy referral stream; identity with case 50 here is not excluded (INFERENZA). Read sources now hold **2-4** homozygous p.Leu239Arg children in **1-3** families (Serin 2018, PMID 30094525, unread and not counted)."}
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the WGS paper identifies its WWOX case with a patient of an earlier case series | Reported as Patient 11 (Table S1) in case series in Piard et al [97]. | PMID 37946251, Table 1 row 009Sev001 (image); files/supplements/PMID37946251/13073_2023_1240_Tab1_HTML.jpg)
(the WGS paper says the compound heterozygous variants were reported before | These compound heterozygous variants were previously reported as part of a case series expanding the phenotypic spectrum associated with this gene [97]. | PMID 37946251, Results, Structural variants; files/fulltext/PMID37946251_Pagnamenta2023_PMC.xml)
(the WGS case genotype is an exons 6-8 in-frame deletion with a frameshift in trans | A fifth SV led to an in-frame 219 kb deletion of exons 6–8 of WWOX, leading to loss of 180 amino acids including the mitochondrial targeting sequence. | PMID 37946251, Results, Structural variants; files/fulltext/PMID37946251_Pagnamenta2023_PMC.xml)
(the CP-cohort child is female from a consanguineous family | CP_P14.1 F 1,2 Yes Short neck, hypertelorism, scoliosis, global developmental delay, hypotonia, seizures and spasticity | PMID 41835067, Table 1; files/fulltext/PMID41835067_Yigit2026_PMC.xml)
(the CP-cohort child is homozygous for p.Leu239Arg | Hom (maternal paternal) P (PP3, PM3, PM2, PP5) | PMID 41835067, Table 2; files/fulltext/PMID41835067_Yigit2026_PMC.xml)
(seizure onset in the CP-cohort child is neonatal | Tonic-clonic seizures began at two weeks of age , and anti- seizure medication was initiated . | PMID 41835067, Supplementary file 1; files/supplements/PMID41835067/Supplementary_file_1.docx)
