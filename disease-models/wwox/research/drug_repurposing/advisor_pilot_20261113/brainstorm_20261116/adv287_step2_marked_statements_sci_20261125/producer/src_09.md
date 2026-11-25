# src_09 (card E02_ldh_inhibition, /p4_card/next_measurement)

## Verbatim sentence (marked word: "every" in "30 fold or more on every pair")
The arm is a nanomolar human-LDHA inhibitor taken from the curated database target entries: 205 qualify, 116 have no LDHB datum at all (unknown, not non-selective) and, of the 89 with a same-document LDHA and LDHB pair, 74 have a pair under 10 fold and only 2 are 30 fold or more on every pair, so selectivity over LDHB must be established per compound (list by id in qualification_it9_p4a_20261030/ldha_nanomolar_selectivity.tsv);

## Source pointers
- Card packet: disease-models/wwox/research/drug_repurposing/cards/E02_ldh_inhibition.packet.json, /p4_card/next_measurement.
- Package: disease-models/wwox/research/drug_repurposing/qualification_it9_p4a_20261030/ (README.md section 1; qualify_p4a.py; ldha_nanomolar_selectivity.tsv; ldha_ldhb_pairs.tsv; collected.json.gz; run_summary.json). ChEMBL REST pull of 2026-10-30: human LDHA single-protein target CHEMBL4835 (P00338), types IC50, Ki, Kd: 1428 of 1428 rows, not truncated; human LDHB single-protein target CHEMBL4940 (P07195), same types: 373 of 373 rows, not truncated. run_summary.json: n_nm = 205, n_pairs = 185, n_sel = 205.
- Selection rule of the 205 (stated in README section 1 and verified against collected.json.gz): molecules with at least one LDHA row of type IC50, Ki or Kd, relation "=", units nM, value 100 nM or less. A ratio is formed only between two rows of the same ChEMBL document with the same standard type and units and both relations "=" (README "Rules kept"). Ratio column = LDHB value divided by LDHA value of the same document and type. Species: ChEMBL target organism is Homo sapiens for every row of the two targets; assay text is quoted in the pairs table.

## README section 1 (verbatim)
## 1. LDHB for every nanomolar human-LDHA inhibitor (ChEMBL target + GtoPdb)

* **Denominators.** Human LDHA single-protein target CHEMBL4835 (accession P00338), types IC50, Ki, Kd: 1,428 of 1,428 rows retrieved, **not truncated** (the IT8 P3 pull was 1,000 of 1,428). Human LDHB single-protein target CHEMBL4940 (accession P07195), same types: 373 of 373 rows, not truncated. **205 molecules** have at least one "=" value of 100 nM or less on LDHA (IT8 P3 had 134 among the first 1,000 rows; the verifier's 206 used a slightly different release or definition). All 205 molecule records were fetched: 203 are parent records, 2 are child records; 0 molecule lookups failed in the final run.
* **LDHB datum per compound.** 116 of 205 have **no LDHB row in ChEMBL**: LDHB selectivity is UNKNOWN for them, not "non-selective" and not "selective". 89 have at least one **same-document LDHA and LDHB pair**; none has LDHB rows only in other documents. 185 pairs in total, 182 with both relations "=" (ratio LDHB/LDHA formed), 3 not formed because the LDHA side is censored.
* **Distribution of the 182 same-document ratios, per compound (89 compounds with an "=" pair):** 74 compounds have at least one pair under 10 fold, 30 have at least one pair under 1 (LDHB-preferring in that document), 23 have at least one pair of 30 fold or more, and only **2 are 30 fold or more on every pair** (CHEMBL3763437, ratio 267 on LDHA 30 nM; CHEMBL5597066, ratio 352 on LDHA 14.5 nM). The pooled median of per-compound minima is 2.5. Pairs from one paper are not independent samples and nothing is pooled into a property of the class.
* **The three compounds named by the IT8 verifier.** CHEMBL3335794: LDHA 2.6 nM and LDHB 43 nM in CHEMBL3763153 (16.5 fold) and LDHA 38 nM and LDHB 1,150 nM in CHEMBL4028893 (30.3 fold; the assays are not the same format: erythrocyte LDHB and liver LDHA enzymes, 5 min): LDHA-preferring, not selective in the sense of a clean window. CHEMBL3335792 (LDHA 5 nM) and CHEMBL3359440 (LDHA 30 nM, and 610 nM in a second row of the same document): **no LDHB row at all** (UNKNOWN).
* **Identity and availability, as the sources state.** The ChEMBL `availability_type` is -1 (not stated) for all 205 and `max_phase` is empty; 203 have no preferred name. GtoPdb (release 2026.3.1) holds **no LDHA or LDHB interaction row**, and only one of the 205 molecules (CHEMBL3752910) is a GtoPdb ligand (its LDH link is not in GtoPdb). Commercial or research availability is therefore **not stated by any source consulted** and is not assumed. Parent versus salt: 203 parents, 2 child records (see the selectivity table).

## Complete table 1: ldha_nanomolar_selectivity.tsv (all 205 molecules; columns as stored)
| molecule_chembl_id | pref_name | parent_chembl_id | record_role | max_phase | chembl_availability_type | first_approval | gtopdb_ligand_id | gtopdb_approved | ldha_best_nM_equals | n_ldha_rows | n_ldhb_rows | n_same_document_pairs | same_document_ldhb_over_ldha_equals | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHEMBL126519 |  | CHEMBL126519 | parent | None | -1 |  |  |  | 50 | 7 | 4 | 3 | 0.166667;3.33333;20 | same-document LDHA/LDHB pair |
| CHEMBL2059009 |  | CHEMBL2059009 | parent | None | -1 |  |  |  | 46 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL2059807 |  | CHEMBL2059807 | parent | None | -1 |  |  |  | 69 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL2059809 |  | CHEMBL2059809 | parent | None | -1 |  |  |  | 60 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL2059811 |  | CHEMBL2059811 | parent | None | -1 |  |  |  | 93 | 5 | 1 | 2 | 9.01961;6.86567 | same-document LDHA/LDHB pair |
| CHEMBL2059812 |  | CHEMBL2059812 | parent | None | -1 |  |  |  | 8 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL2316885 |  | CHEMBL2316885 | parent | None | -1 |  |  |  | 19 | 3 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL2316886 |  | CHEMBL2316886 | parent | None | -1 |  |  |  | 68 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3335792 |  | CHEMBL3335792 | parent | None | -1 |  |  |  | 5 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3335794 |  | CHEMBL3335794 | parent | None | -1 |  |  |  | 1.7 | 8 | 2 | 3 | 16.5385;30.2632;30.2632 | same-document LDHA/LDHB pair |
| CHEMBL3359440 |  | CHEMBL3359440 | parent | None | -1 |  |  |  | 30 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL338325 |  | CHEMBL338325 | parent | None | -1 |  |  |  | 100 | 2 | 3 | 3 | 1;190;190 | same-document LDHA/LDHB pair |
| CHEMBL3581177 |  | CHEMBL3581177 | parent | None | -1 |  |  |  | 100 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581179 |  | CHEMBL3581179 | parent | None | -1 |  |  |  | 60 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581180 |  | CHEMBL3581180 | parent | None | -1 |  |  |  | 90 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581181 |  | CHEMBL3581181 | parent | None | -1 |  |  |  | 100 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581182 |  | CHEMBL3581182 | parent | None | -1 |  |  |  | 60 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581184 |  | CHEMBL3581184 | parent | None | -1 |  |  |  | 85 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581194 |  | CHEMBL3581194 | parent | None | -1 |  |  |  | 40 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581197 |  | CHEMBL3581197 | parent | None | -1 |  |  |  | 6 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581198 |  | CHEMBL3581198 | parent | None | -1 |  |  |  | 90 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3581199 |  | CHEMBL3581199 | parent | None | -1 |  |  |  | 30 | 1 | 1 | 1 | 6 | same-document LDHA/LDHB pair |
| CHEMBL3581200 |  | CHEMBL3581200 | parent | None | -1 |  |  |  | 25 | 1 | 1 | 1 | 16.4 | same-document LDHA/LDHB pair |
| CHEMBL3581201 |  | CHEMBL3581201 | parent | None | -1 |  |  |  | 15 | 1 | 1 | 1 | 9.33333 | same-document LDHA/LDHB pair |
| CHEMBL3581203 |  | CHEMBL3581203 | parent | None | -1 |  |  |  | 35 | 1 | 1 | 1 | 6.57143 | same-document LDHA/LDHB pair |
| CHEMBL3581204 |  | CHEMBL3581204 | parent | None | -1 |  |  |  | 30 | 1 | 1 | 1 | 4 | same-document LDHA/LDHB pair |
| CHEMBL3581205 |  | CHEMBL3581205 | parent | None | -1 |  |  |  | 30 | 1 | 1 | 1 | 16.3333 | same-document LDHA/LDHB pair |
| CHEMBL3752910 |  | CHEMBL3752910 | parent | None | -1 |  | 14226 |  | 9.012 | 1 | 1 | 1 | 0.922326 | same-document LDHA/LDHB pair |
| CHEMBL3763437 |  | CHEMBL3763437 | parent | None | -1 |  |  |  | 30 | 1 | 1 | 1 | 266.667 | same-document LDHA/LDHB pair |
| CHEMBL3764412 |  | CHEMBL3764412 | parent | None | -1 |  |  |  | 63.1 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL3765327 |  | CHEMBL3765327 | parent | None | -1 |  |  |  | 16 | 1 | 1 | 1 | 13.75 | same-document LDHA/LDHB pair |
| CHEMBL4059985 |  | CHEMBL4059985 | parent | None | -1 |  |  |  | 9 | 2 | 1 | 2 | 0.888889;0.888889 | same-document LDHA/LDHB pair |
| CHEMBL4062709 |  | CHEMBL4062709 | parent | None | -1 |  |  |  | 65 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4065858 |  | CHEMBL4065858 | parent | None | -1 |  |  |  | 3 | 5 | 2 | 5 | 1.04009;1.04009;1.66667;0.00746269 | same-document LDHA/LDHB pair |
| CHEMBL4069450 |  | CHEMBL4069450 | parent | None | -1 |  |  |  | 84 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4069726 |  | CHEMBL4069726 | parent | None | -1 |  |  |  | 42 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4069796 |  | CHEMBL4069796 | parent | None | -1 |  |  |  | 95 | 2 | 1 | 2 | 1.35789;1.35789 | same-document LDHA/LDHB pair |
| CHEMBL4075666 |  | CHEMBL4075666 | parent | None | -1 |  |  |  | 65 | 2 | 1 | 2 | 1.15385;1.15385 | same-document LDHA/LDHB pair |
| CHEMBL4076027 |  | CHEMBL4076027 | parent | None | -1 |  |  |  | 57 | 2 | 1 | 2 | 1.36842;1.36842 | same-document LDHA/LDHB pair |
| CHEMBL4076264 |  | CHEMBL4076264 | parent | None | -1 |  |  |  | 95 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4076958 |  | CHEMBL4076958 | parent | None | -1 |  |  |  | 91 | 2 | 1 | 2 | 1.05495;1.05495 | same-document LDHA/LDHB pair |
| CHEMBL4080497 |  | CHEMBL4080497 | parent | None | -1 |  |  |  | 38 | 2 | 1 | 2 | 1.28947;1.28947 | same-document LDHA/LDHB pair |
| CHEMBL4081890 |  | CHEMBL4081890 | parent | None | -1 |  |  |  | 0.11 | 8 | 1 | 2 | 0.84375;0.84375 | same-document LDHA/LDHB pair |
| CHEMBL4090677 |  | CHEMBL4090677 | parent | None | -1 |  |  |  | 19 | 2 | 1 | 2 | 1.05263;1.05263 | same-document LDHA/LDHB pair |
| CHEMBL4100845 |  | CHEMBL4100845 | parent | None | -1 |  |  |  | 0.33 | 3 | 1 | 2 | 0.740741;0.740741 | same-document LDHA/LDHB pair |
| CHEMBL4101800 |  | CHEMBL4101800 | parent | None | -1 |  |  |  | 53 | 2 | 1 | 2 | 1.16981;1.16981 | same-document LDHA/LDHB pair |
| CHEMBL4103659 |  | CHEMBL4103659 | parent | None | -1 |  |  |  | 95 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4294999 |  | CHEMBL4294999 | parent | None | -1 |  |  |  | 52 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4435570 |  | CHEMBL4435570 | parent | None | -1 |  |  |  | 4 | 1 | 1 | 1 | 19.25 | same-document LDHA/LDHB pair |
| CHEMBL4436150 |  | CHEMBL4436150 | parent | None | -1 |  |  |  | 9 | 1 | 1 | 1 | 3.33333 | same-document LDHA/LDHB pair |
| CHEMBL4437061 |  | CHEMBL4437061 | parent | None | -1 |  |  |  | 65 | 1 | 1 | 1 | 3.23077 | same-document LDHA/LDHB pair |
| CHEMBL4444202 |  | CHEMBL4444202 | parent | None | -1 |  |  |  | 42 | 1 | 1 | 1 | 6.42857 | same-document LDHA/LDHB pair |
| CHEMBL4444963 |  | CHEMBL4444963 | parent | None | -1 |  |  |  | 7 | 1 | 1 | 1 | 7.14286 | same-document LDHA/LDHB pair |
| CHEMBL4445937 |  | CHEMBL4445937 | parent | None | -1 |  |  |  | 100 | 1 | 1 | 1 | 4.8 | same-document LDHA/LDHB pair |
| CHEMBL4450897 |  | CHEMBL4450897 | parent | None | -1 |  |  |  | 16 | 2 | 1 | 2 | 4.6875;0.0258621 | same-document LDHA/LDHB pair |
| CHEMBL4453059 |  | CHEMBL4453059 | parent | None | -1 |  |  |  | 15 | 1 | 1 | 1 | 3.66667 | same-document LDHA/LDHB pair |
| CHEMBL4467769 |  | CHEMBL4467769 | parent | None | -1 |  |  |  | 5 | 1 | 1 | 1 | 7 | same-document LDHA/LDHB pair |
| CHEMBL4468333 |  | CHEMBL4468333 | parent | None | -1 |  |  |  | 47 | 1 | 1 | 1 | 8.29787 | same-document LDHA/LDHB pair |
| CHEMBL4474069 |  | CHEMBL4474069 | parent | None | -1 |  |  |  | 80 | 1 | 1 | 1 | 3.125 | same-document LDHA/LDHB pair |
| CHEMBL4475593 |  | CHEMBL4475593 | parent | None | -1 |  |  |  | 10 | 2 | 1 | 2 | 6;0.00983607 | same-document LDHA/LDHB pair |
| CHEMBL4520899 |  | CHEMBL4520899 | parent | None | -1 |  |  |  | 9 | 2 | 1 | 2 | 5.44444;0.0731343 | same-document LDHA/LDHB pair |
| CHEMBL4521960 |  | CHEMBL4521960 | parent | None | -1 |  |  |  | 14 | 1 | 1 | 1 | 4.07143 | same-document LDHA/LDHB pair |
| CHEMBL4534918 |  | CHEMBL4534918 | parent | None | -1 |  |  |  | 27 | 2 | 1 | 2 | 5.18519;0.0358974 | same-document LDHA/LDHB pair |
| CHEMBL4536094 |  | CHEMBL4536094 | parent | None | -1 |  |  |  | 13 | 2 | 1 | 2 | 3.53846 | same-document LDHA/LDHB pair |
| CHEMBL4543194 |  | CHEMBL4543194 | parent | None | -1 |  |  |  | 21 | 2 | 1 | 2 | 3.80952 | same-document LDHA/LDHB pair |
| CHEMBL4543949 |  | CHEMBL4543949 | parent | None | -1 |  |  |  | 15 | 2 | 1 | 2 | 4.66667;0.0137255 | same-document LDHA/LDHB pair |
| CHEMBL4545064 |  | CHEMBL4545064 | parent | None | -1 |  |  |  | 9 | 1 | 1 | 1 | 17.7778 | same-document LDHA/LDHB pair |
| CHEMBL4555982 |  | CHEMBL4555982 | parent | None | -1 |  |  |  | 37 | 1 | 1 | 1 | 5.13514 | same-document LDHA/LDHB pair |
| CHEMBL4557701 |  | CHEMBL4557701 | parent | None | -1 |  |  |  | 17 | 2 | 1 | 2 | 8.23529;0.0141414 | same-document LDHA/LDHB pair |
| CHEMBL4574842 |  | CHEMBL4574842 | parent | None | -1 |  |  |  | 69 | 1 | 1 | 1 | 9.56522 | same-document LDHA/LDHB pair |
| CHEMBL4575930 |  | CHEMBL4575930 | parent | None | -1 |  |  |  | 52 | 1 | 1 | 1 | 15 | same-document LDHA/LDHB pair |
| CHEMBL4576717 |  | CHEMBL4576717 | parent | None | -1 |  |  |  | 3 | 1 | 1 | 1 | 11.6667 | same-document LDHA/LDHB pair |
| CHEMBL4578904 |  | CHEMBL4578904 | parent | None | -1 |  |  |  | 58 | 1 | 1 | 1 | 3.44828 | same-document LDHA/LDHB pair |
| CHEMBL4583899 |  | CHEMBL4583899 | parent | None | -1 |  |  |  | 25 | 2 | 1 | 2 | 7.2;0.0072 | same-document LDHA/LDHB pair |
| CHEMBL4589484 |  | CHEMBL4589484 | parent | None | -1 |  |  |  | 55 | 1 | 1 | 1 | 2.54545 | same-document LDHA/LDHB pair |
| CHEMBL4591832 |  | CHEMBL4591832 | parent | None | -1 |  |  |  | 82 | 1 | 1 | 1 | 9.7561 | same-document LDHA/LDHB pair |
| CHEMBL4740977 |  | CHEMBL4740977 | parent | None | -1 |  |  |  | 12 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4741188 |  | CHEMBL4741188 | parent | None | -1 |  |  |  | 23 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4742726 |  | CHEMBL4742726 | parent | None | -1 |  |  |  | 31 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4746456 |  | CHEMBL4746456 | parent | None | -1 |  |  |  | 25 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4746658 |  | CHEMBL4746658 | parent | None | -1 |  |  |  | 15 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4747300 |  | CHEMBL4747300 | parent | None | -1 |  |  |  | 7 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4748782 |  | CHEMBL4748782 | parent | None | -1 |  |  |  | 0.0667 | 5 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4749903 |  | CHEMBL4749903 | parent | None | -1 |  |  |  | 7 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4751209 |  | CHEMBL4751209 | parent | None | -1 |  |  |  | 47 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4751355 |  | CHEMBL4751355 | parent | None | -1 |  |  |  | 15 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4751495 |  | CHEMBL4751495 | parent | None | -1 |  |  |  | 10 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4752751 |  | CHEMBL4752751 | parent | None | -1 |  |  |  | 11 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4752866 |  | CHEMBL4752866 | parent | None | -1 |  |  |  | 24 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4752940 |  | CHEMBL4752940 | parent | None | -1 |  |  |  | 6 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4753360 |  | CHEMBL4753360 | parent | None | -1 |  |  |  | 59 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4753379 |  | CHEMBL4753379 | parent | None | -1 |  |  |  | 0.0634 | 6 | 1 | 1 | 1.66667 | same-document LDHA/LDHB pair |
| CHEMBL4754755 |  | CHEMBL4754755 | parent | None | -1 |  |  |  | 15 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4754861 |  | CHEMBL4754861 | parent | None | -1 |  |  |  | 36 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4755095 |  | CHEMBL4755095 | parent | None | -1 |  |  |  | 36 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4756608 |  | CHEMBL4756608 | parent | None | -1 |  |  |  | 33 | 3 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4758227 |  | CHEMBL4758227 | parent | None | -1 |  |  |  | 25 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4758290 |  | CHEMBL4758290 | parent | None | -1 |  |  |  | 15 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4759378 |  | CHEMBL4759378 | parent | None | -1 |  |  |  | 7 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4759499 |  | CHEMBL4759499 | parent | None | -1 |  |  |  | 8 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4760911 |  | CHEMBL4760911 | parent | None | -1 |  |  |  | 9 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4761628 |  | CHEMBL4761628 | parent | None | -1 |  |  |  | 21 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4761804 |  | CHEMBL4761804 | parent | None | -1 |  |  |  | 36 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4762840 |  | CHEMBL4762840 | parent | None | -1 |  |  |  | 50 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4762895 |  | CHEMBL4762895 | parent | None | -1 |  |  |  | 33 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4762989 |  | CHEMBL4762989 | parent | None | -1 |  |  |  | 14 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4763489 |  | CHEMBL4763489 | parent | None | -1 |  |  |  | 14 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4763797 |  | CHEMBL4763797 | parent | None | -1 |  |  |  | 38 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4763863 |  | CHEMBL4763863 | parent | None | -1 |  |  |  | 52 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4764953 |  | CHEMBL4764953 | parent | None | -1 |  |  |  | 74 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4777867 |  | CHEMBL4777867 | parent | None | -1 |  |  |  | 9 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4777976 |  | CHEMBL4777976 | parent | None | -1 |  |  |  | 33 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4780015 |  | CHEMBL4780015 | parent | None | -1 |  |  |  | 87 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4782843 |  | CHEMBL4782843 | parent | None | -1 |  |  |  | 0.0193 | 5 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4783252 |  | CHEMBL4783252 | parent | None | -1 |  |  |  | 9 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4783367 |  | CHEMBL4783367 | parent | None | -1 |  |  |  | 13 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4783945 |  | CHEMBL4783945 | parent | None | -1 |  |  |  | 8 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4784359 |  | CHEMBL4784359 | parent | None | -1 |  |  |  | 54 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4784520 |  | CHEMBL4784520 | parent | None | -1 |  |  |  | 17 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4784731 |  | CHEMBL4784731 | parent | None | -1 |  |  |  | 16 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4785391 |  | CHEMBL4785391 | parent | None | -1 |  |  |  | 24 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4786033 |  | CHEMBL4786033 | parent | None | -1 |  |  |  | 23 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4786241 |  | CHEMBL4786241 | parent | None | -1 |  |  |  | 23 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4786346 |  | CHEMBL4786346 | parent | None | -1 |  |  |  | 39 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4786682 |  | CHEMBL4786682 | parent | None | -1 |  |  |  | 3 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4786717 |  | CHEMBL4786717 | parent | None | -1 |  |  |  | 9 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4787852 |  | CHEMBL4787852 | parent | None | -1 |  |  |  | 0.1235 | 5 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4787940 |  | CHEMBL4787940 | parent | None | -1 |  |  |  | 11 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4788048 |  | CHEMBL4788048 | parent | None | -1 |  |  |  | 24 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4790159 |  | CHEMBL4790159 | parent | None | -1 |  |  |  | 8 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4791940 |  | CHEMBL4791940 | parent | None | -1 |  |  |  | 32 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4792513 |  | CHEMBL4792513 | parent | None | -1 |  |  |  | 1 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4793796 |  | CHEMBL4793796 | parent | None | -1 |  |  |  | 52 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4794789 |  | CHEMBL4794789 | parent | None | -1 |  |  |  | 9 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4797357 |  | CHEMBL4797357 | parent | None | -1 |  |  |  | 5 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4799233 |  | CHEMBL4799233 | parent | None | -1 |  |  |  | 47 | 4 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4846303 |  | CHEMBL4846303 | parent | None | -1 |  |  |  | 27 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4846426 |  | CHEMBL4846426 | parent | None | -1 |  |  |  | 17 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4846757 |  | CHEMBL4846757 | parent | None | -1 |  |  |  | 77 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4847068 |  | CHEMBL4847068 | parent | None | -1 |  |  |  | 0.3 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4847105 |  | CHEMBL4847105 | parent | None | -1 |  |  |  | 8 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4847591 |  | CHEMBL4847591 | parent | None | -1 |  |  |  | 0.44 | 4 | 1 | 3 | 296.296;0.34188;0.851064 | same-document LDHA/LDHB pair |
| CHEMBL4849137 |  | CHEMBL4849137 | parent | None | -1 |  |  |  | 5 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4850573 |  | CHEMBL4850573 | parent | None | -1 |  |  |  | 0.07 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4851612 |  | CHEMBL4851612 | parent | None | -1 |  |  |  | 34 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4851964 |  | CHEMBL4851964 | parent | None | -1 |  |  |  | 84 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4852130 |  | CHEMBL4852130 | parent | None | -1 |  |  |  | 5 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4853535 |  | CHEMBL4853535 | parent | None | -1 |  |  |  | 13 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4854797 |  | CHEMBL4854797 | parent | None | -1 |  |  |  | 26 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4854958 |  | CHEMBL4854958 | parent | None | -1 |  |  |  | 0.001 | 4 | 1 | 3 | 260.87;6;5.45455 | same-document LDHA/LDHB pair |
| CHEMBL4855986 |  | CHEMBL4855986 | parent | None | -1 |  |  |  | 0.1 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4856298 |  | CHEMBL4856298 | parent | None | -1 |  |  |  | 90 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4856798 |  | CHEMBL4856798 | parent | None | -1 |  |  |  | 8 | 3 | 1 | 3 | 250;0.21978;0.425532 | same-document LDHA/LDHB pair |
| CHEMBL4857168 |  | CHEMBL4857168 | parent | None | -1 |  |  |  | 23 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4857703 |  | CHEMBL4857703 | parent | None | -1 |  |  |  | 29 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4858373 |  | CHEMBL4858373 | parent | None | -1 |  |  |  | 59 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4859303 |  | CHEMBL4859303 | parent | None | -1 |  |  |  | 0.016 | 4 | 1 | 3 | 263.158;7.24638;8.47458 | same-document LDHA/LDHB pair |
| CHEMBL4860066 |  | CHEMBL4860066 | parent | None | -1 |  |  |  | 1.1 | 4 | 1 | 3 | 730.769;21.8391;34.5455 | same-document LDHA/LDHB pair |
| CHEMBL4861089 |  | CHEMBL4861089 | parent | None | -1 |  |  |  | 6 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4861379 |  | CHEMBL4861379 | parent | None | -1 |  |  |  | 0.3 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4863968 |  | CHEMBL4863968 | parent | None | -1 |  |  |  | 39 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4864519 |  | CHEMBL4864519 | parent | None | -1 |  |  |  | 0.5 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4865191 |  | CHEMBL4865191 | parent | None | -1 |  |  |  | 71 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4869869 |  | CHEMBL4869869 | parent | None | -1 |  |  |  | 37 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4872291 |  | CHEMBL4872291 | parent | None | -1 |  |  |  | 47 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4872528 |  | CHEMBL4872528 | parent | None | -1 |  |  |  | 17 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4872752 |  | CHEMBL4872752 | parent | None | -1 |  |  |  | 0.91 | 4 | 1 | 3 | 227.273;7.46269;6.84932 | same-document LDHA/LDHB pair |
| CHEMBL4873611 |  | CHEMBL4873611 | parent | None | -1 |  |  |  | 0.008 | 4 | 1 | 3 | 600;2.14286;2.72727 | same-document LDHA/LDHB pair |
| CHEMBL4873879 |  | CHEMBL4873879 | parent | None | -1 |  |  |  | 0.4 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4874506 |  | CHEMBL4874506 | parent | None | -1 |  |  |  | 21 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4875236 |  | CHEMBL4875236 | parent | None | -1 |  |  |  | 22 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4876708 |  | CHEMBL4876708 | parent | None | -1 |  |  |  | 15 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4876783 |  | CHEMBL4876783 | parent | None | -1 |  |  |  | 0.004 | 4 | 1 | 3 | 375;1.42857;1.57895 | same-document LDHA/LDHB pair |
| CHEMBL4877797 |  | CHEMBL4877797 | parent | None | -1 |  |  |  | 1.5 | 4 | 1 | 3 | 3.18471;0.149254;0.322581 | same-document LDHA/LDHB pair |
| CHEMBL4877988 |  | CHEMBL4877988 | parent | None | -1 |  |  |  | 7 | 3 | 1 | 3 | 285.714;0.4;0.869565 | same-document LDHA/LDHB pair |
| CHEMBL4878761 |  | CHEMBL4878761 | parent | None | -1 |  |  |  | 18 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL4879296 |  | CHEMBL4879296 | parent | None | -1 |  |  |  | 41 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL5171701 |  | CHEMBL5171701 | parent | None | -1 |  |  |  | 13 | 2 | 2 | 4 | 13.0769;138.462;0.894737;9.47368 | same-document LDHA/LDHB pair |
| CHEMBL5172378 |  | CHEMBL5172378 | parent | None | -1 |  |  |  | 13 | 2 | 2 | 4 | 0.684615;23.8462;0.0468421;1.63158 | same-document LDHA/LDHB pair |
| CHEMBL5176448 |  | CHEMBL5176448 | parent | None | -1 |  |  |  | 2.9 | 2 | 2 | 4 | 22.4138;113.793;1.03175;5.2381 | same-document LDHA/LDHB pair |
| CHEMBL5177632 |  | CHEMBL5177632 | parent | None | -1 |  |  |  | 4 | 1 | 1 | 1 | 11.75 | same-document LDHA/LDHB pair |
| CHEMBL5180187 |  | CHEMBL5221507 | child/salt-or-other-record | None | -1 |  |  |  | 90 | 2 | 2 | 2 | 0.5;7.77778 | same-document LDHA/LDHB pair |
| CHEMBL5181496 |  | CHEMBL5181496 | parent | None | -1 |  |  |  | 0.9 | 2 | 2 | 4 | 3.11111;34.4444;0.636364;7.04545 | same-document LDHA/LDHB pair |
| CHEMBL5181996 |  | CHEMBL5181996 | parent | None | -1 |  |  |  | 2.2 | 2 | 2 | 4 | 6.81818;40.9091;0.681818;4.09091 | same-document LDHA/LDHB pair |
| CHEMBL5182266 |  | CHEMBL5182266 | parent | None | -1 |  |  |  | 2.9 | 2 | 2 | 4 | 5.86207;23.4483;2.46377;9.85507 | same-document LDHA/LDHB pair |
| CHEMBL5183539 |  | CHEMBL5183539 | parent | None | -1 |  |  |  | 1.6 | 1 | 1 | 1 | 6.125 | same-document LDHA/LDHB pair |
| CHEMBL5185237 |  | CHEMBL5185237 | parent | None | -1 |  |  |  | 2.5 | 2 | 2 | 4 | 0.68;15.2;0.154545;3.45455 | same-document LDHA/LDHB pair |
| CHEMBL5187919 |  | CHEMBL5187919 | parent | None | -1 |  |  |  | 90 | 1 | 1 | 1 | 9 | same-document LDHA/LDHB pair |
| CHEMBL5188480 |  | CHEMBL5188480 | parent | None | -1 |  |  |  | 3.8 | 2 | 2 | 4 | 6.57895;171.053;0.367647;9.55882 | same-document LDHA/LDHB pair |
| CHEMBL5189798 |  | CHEMBL5189798 | parent | None | -1 |  |  |  | 26 | 2 | 2 | 4 | 2.88462;36.5385;0.174419;2.2093 | same-document LDHA/LDHB pair |
| CHEMBL5189879 |  | CHEMBL5189879 | parent | None | -1 |  |  |  | 3.7 | 1 | 1 | 1 | 12.4324 | same-document LDHA/LDHB pair |
| CHEMBL5192632 |  | CHEMBL5192632 | parent | None | -1 |  |  |  | 66 | 1 | 1 | 1 | 6.06061 | same-document LDHA/LDHB pair |
| CHEMBL5194549 |  | CHEMBL5194549 | parent | None | -1 |  |  |  | 2.5 | 2 | 2 | 4 | 3.8;36;2.96875;28.125 | same-document LDHA/LDHB pair |
| CHEMBL5194727 |  | CHEMBL5194727 | parent | None | -1 |  |  |  | 43 | 1 | 1 | 1 | 6.74419 | same-document LDHA/LDHB pair |
| CHEMBL5196259 |  | CHEMBL5196259 | parent | None | -1 |  |  |  | 8.6 | 2 | 2 | 4 | 6.62791;94.186;0.35625;5.0625 | same-document LDHA/LDHB pair |
| CHEMBL5196929 |  | CHEMBL5196929 | parent | None | -1 |  |  |  | 2.7 | 2 | 2 | 4 | 3.03704;122.222;0.149091;6 | same-document LDHA/LDHB pair |
| CHEMBL5197729 |  | CHEMBL5197729 | parent | None | -1 |  |  |  | 36 | 1 | 1 | 1 | 2.08333 | same-document LDHA/LDHB pair |
| CHEMBL5201115 |  | CHEMBL5201115 | parent | None | -1 |  |  |  | 1.8 | 2 | 2 | 4 | 1.22222;47.2222;0.0594595;2.2973 | same-document LDHA/LDHB pair |
| CHEMBL5202219 |  | CHEMBL5202219 | parent | None | -1 |  |  |  | 10 | 2 | 2 | 4 | 3.4;29;0.453333;3.86667 | same-document LDHA/LDHB pair |
| CHEMBL5205566 |  | CHEMBL5205566 | parent | None | -1 |  |  |  | 90 | 2 | 2 | 4 | 2.22222;8.33333;0.465116;1.74419 | same-document LDHA/LDHB pair |
| CHEMBL5206296 |  | CHEMBL5206296 | parent | None | -1 |  |  |  | 12.03 | 1 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |
| CHEMBL5416627 |  | CHEMBL5499297 | child/salt-or-other-record | None | -1 |  |  |  | 2.6 | 1 | 1 | 1 | 16.5385 | same-document LDHA/LDHB pair |
| CHEMBL5597066 |  | CHEMBL5597066 | parent | None | -1 |  |  |  | 14.5 | 5 | 1 | 1 | 351.818 | same-document LDHA/LDHB pair |
| CHEMBL5597243 |  | CHEMBL5597243 | parent | None | -1 |  |  |  | 72 | 1 | 1 | 1 | 16.6667 | same-document LDHA/LDHB pair |
| CHEMBL6150047 |  | CHEMBL6150047 | parent | None | -1 |  |  |  | 25 | 2 | 0 | 0 |  | no LDHB row in ChEMBL (UNKNOWN, not non-selective) |

## Complete table 2: ldha_ldhb_pairs.tsv (all 185 same-document pairs; columns as stored; ratio_kind "ratio_equals" = both relations "=" and a ratio formed; the other kind = not formed)
| molecule_chembl_id | pref_name | document | type | ldha_relation | ldha_nM | ldhb_relation | ldhb_nM | ratio_kind | ldhb_over_ldha | ldha_assay | ldhb_assay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CHEMBL126519 |  | CHEMBL1131124 | Ki | = | 300 | = | 50 | ratio_equals | 0.166667 | inhibitory activity against Plasmodium falciparum LDH (pLDH) | inhibitory activity against Human Lactate Dehydrogenase (LDH-M) |
| CHEMBL126519 |  | CHEMBL1131124 | Ki | = | 300 | = | 1000 | ratio_equals | 3.33333 | inhibitory activity against Plasmodium falciparum LDH (pLDH) | inhibitory activity against Human Lactate Dehydrogenase (LDH-H) |
| CHEMBL126519 |  | CHEMBL3763153 | Ki | = | 50 | = | 1000 | ratio_equals | 20 | Competitive inhibition of human LDH5 in presence of NADH | Competitive inhibition of human LDH1 in presence of NADH |
| CHEMBL2059811 |  | CHEMBL4028893 | IC50 | = | 1020 | = | 9200 | ratio_equals | 9.01961 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL2059811 |  | CHEMBL4028893 | IC50 | = | 1340 | = | 9200 | ratio_equals | 6.86567 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL3335794 |  | CHEMBL3763153 | IC50 | = | 2.6 | = | 43 | ratio_equals | 16.5385 | Competitive inhibition of human LDH5 in presence of NADH | Competitive inhibition of human LDH1 in presence of NADH |
| CHEMBL3335794 |  | CHEMBL4028893 | IC50 | = | 38 | = | 1150 | ratio_equals | 30.2632 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL3335794 |  | CHEMBL4028893 | IC50 | = | 38 | = | 1150 | ratio_equals | 30.2632 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL338325 |  | CHEMBL1131124 | Ki | = | 100 | = | 100 | ratio_equals | 1 | inhibitory activity against Plasmodium falciparum LDH (pLDH) | inhibitory activity against Human Lactate Dehydrogenase (LDH-M) |
| CHEMBL338325 |  | CHEMBL1131124 | Ki | = | 100 | = | 19000 | ratio_equals | 190 | inhibitory activity against Plasmodium falciparum LDH (pLDH) | inhibitory activity against Human Lactate Dehydrogenase (LDH-H) |
| CHEMBL338325 |  | CHEMBL3763153 | Ki | = | 100 | = | 19000 | ratio_equals | 190 | Competitive inhibition of human LDH5 in presence of NADH | Competitive inhibition of human LDH1 in presence of NADH |
| CHEMBL3581199 |  | CHEMBL3580578 | IC50 | = | 30 | = | 180 | ratio_equals | 6 | Inhibition of human LDH-A by biochemical assay | Inhibition of LDH-B (unknown origin) |
| CHEMBL3581200 |  | CHEMBL3580578 | IC50 | = | 25 | = | 410 | ratio_equals | 16.4 | Inhibition of human LDH-A by biochemical assay | Inhibition of LDH-B (unknown origin) |
| CHEMBL3581201 |  | CHEMBL3580578 | IC50 | = | 15 | = | 140 | ratio_equals | 9.33333 | Inhibition of human LDH-A by biochemical assay | Inhibition of LDH-B (unknown origin) |
| CHEMBL3581203 |  | CHEMBL3580578 | IC50 | = | 35 | = | 230 | ratio_equals | 6.57143 | Inhibition of human LDH-A by biochemical assay | Inhibition of LDH-B (unknown origin) |
| CHEMBL3581204 |  | CHEMBL3580578 | IC50 | = | 30 | = | 120 | ratio_equals | 4 | Inhibition of human LDH-A by biochemical assay | Inhibition of LDH-B (unknown origin) |
| CHEMBL3581205 |  | CHEMBL3580578 | IC50 | = | 30 | = | 490 | ratio_equals | 16.3333 | Inhibition of human LDH-A by biochemical assay | Inhibition of LDH-B (unknown origin) |
| CHEMBL3752910 |  | CHEMBL5649169 | Kd | = | 9.012 | = | 8.312 | ratio_equals | 0.922326 | Binding affinity to human LDHA incubated for 45 mins by Kinobead based pull down assay | Binding affinity to human LDHB incubated for 45 mins by Kinobead based pull down assay |
| CHEMBL3763437 |  | CHEMBL3763153 | Ki | = | 30 | = | 8000 | ratio_equals | 266.667 | Competitive inhibition of human LDH5 in presence of NADH | Competitive inhibition of human LDH1 in presence of NADH |
| CHEMBL3765327 |  | CHEMBL3763153 | IC50 | = | 16 | = | 220 | ratio_equals | 13.75 | Competitive inhibition of human LDH5 in presence of NADH | Competitive inhibition of human LDH1 in presence of NADH |
| CHEMBL4059985 |  | CHEMBL4028893 | IC50 | = | 9 | = | 8 | ratio_equals | 0.888889 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4059985 |  | CHEMBL4028893 | IC50 | = | 9 | = | 8 | ratio_equals | 0.888889 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4065858 |  | CHEMBL4028893 | IC50 | = | 424 | = | 441 | ratio_equals | 1.04009 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4065858 |  | CHEMBL4028893 | IC50 | = | 424 | = | 441 | ratio_equals | 1.04009 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4065858 |  | CHEMBL4028893 | IC50 | < | 10 | = | 441 | not_formed (LDHA censored or other relation) |  | Inhibition of human LDHA using sodium pyruvate as substrate in presence of NAPDH | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4065858 |  | CHEMBL4428136 | IC50 | = | 3 | = | 5 | ratio_equals | 1.66667 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4065858 |  | CHEMBL4428136 | IC50 | = | 670 | = | 5 | ratio_equals | 0.00746269 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4069796 |  | CHEMBL4028893 | IC50 | = | 95 | = | 129 | ratio_equals | 1.35789 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4069796 |  | CHEMBL4028893 | IC50 | = | 95 | = | 129 | ratio_equals | 1.35789 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4075666 |  | CHEMBL4028893 | IC50 | = | 65 | = | 75 | ratio_equals | 1.15385 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4075666 |  | CHEMBL4028893 | IC50 | = | 65 | = | 75 | ratio_equals | 1.15385 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4076027 |  | CHEMBL4028893 | IC50 | = | 57 | = | 78 | ratio_equals | 1.36842 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4076027 |  | CHEMBL4028893 | IC50 | = | 57 | = | 78 | ratio_equals | 1.36842 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4076958 |  | CHEMBL4028893 | IC50 | = | 91 | = | 96 | ratio_equals | 1.05495 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4076958 |  | CHEMBL4028893 | IC50 | = | 91 | = | 96 | ratio_equals | 1.05495 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4080497 |  | CHEMBL4028893 | IC50 | = | 38 | = | 49 | ratio_equals | 1.28947 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4080497 |  | CHEMBL4028893 | IC50 | = | 38 | = | 49 | ratio_equals | 1.28947 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4081890 |  | CHEMBL4028893 | IC50 | = | 32 | = | 27 | ratio_equals | 0.84375 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4081890 |  | CHEMBL4028893 | IC50 | = | 32 | = | 27 | ratio_equals | 0.84375 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4090677 |  | CHEMBL4028893 | IC50 | = | 19 | = | 20 | ratio_equals | 1.05263 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4090677 |  | CHEMBL4028893 | IC50 | = | 19 | = | 20 | ratio_equals | 1.05263 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4100845 |  | CHEMBL4028893 | IC50 | = | 27 | = | 20 | ratio_equals | 0.740741 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4100845 |  | CHEMBL4028893 | IC50 | = | 27 | = | 20 | ratio_equals | 0.740741 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4101800 |  | CHEMBL4028893 | IC50 | = | 53 | = | 62 | ratio_equals | 1.16981 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and in abs | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4101800 |  | CHEMBL4028893 | IC50 | = | 53 | = | 62 | ratio_equals | 1.16981 | Inhibition of human liver LDHA using sodium pyruvate as substrate after 5 mins in presence of NAPDH and EDTA b | Inhibition of human erythrocytes LDHB using sodium pyruvate as substrate after 5 mins in presence of NAPDH by  |
| CHEMBL4435570 |  | CHEMBL4428136 | IC50 | = | 4 | = | 77 | ratio_equals | 19.25 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4436150 |  | CHEMBL4428136 | IC50 | = | 9 | = | 30 | ratio_equals | 3.33333 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4437061 |  | CHEMBL4428136 | IC50 | = | 65 | = | 210 | ratio_equals | 3.23077 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4444202 |  | CHEMBL4428136 | IC50 | = | 42 | = | 270 | ratio_equals | 6.42857 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4444963 |  | CHEMBL4428136 | IC50 | = | 7 | = | 50 | ratio_equals | 7.14286 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4445937 |  | CHEMBL4428136 | IC50 | = | 100 | = | 480 | ratio_equals | 4.8 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4450897 |  | CHEMBL4428136 | IC50 | = | 16 | = | 75 | ratio_equals | 4.6875 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4450897 |  | CHEMBL4428136 | IC50 | = | 2900 | = | 75 | ratio_equals | 0.0258621 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4453059 |  | CHEMBL4428136 | IC50 | = | 15 | = | 55 | ratio_equals | 3.66667 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4467769 |  | CHEMBL4428136 | IC50 | = | 5 | = | 35 | ratio_equals | 7 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4468333 |  | CHEMBL4428136 | IC50 | = | 47 | = | 390 | ratio_equals | 8.29787 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4474069 |  | CHEMBL4428136 | IC50 | = | 80 | = | 250 | ratio_equals | 3.125 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4475593 |  | CHEMBL4428136 | IC50 | = | 10 | = | 60 | ratio_equals | 6 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4475593 |  | CHEMBL4428136 | IC50 | = | 6100 | = | 60 | ratio_equals | 0.00983607 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4520899 |  | CHEMBL4428136 | IC50 | = | 9 | = | 49 | ratio_equals | 5.44444 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4520899 |  | CHEMBL4428136 | IC50 | = | 670 | = | 49 | ratio_equals | 0.0731343 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4521960 |  | CHEMBL4428136 | IC50 | = | 14 | = | 57 | ratio_equals | 4.07143 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4534918 |  | CHEMBL4428136 | IC50 | = | 27 | = | 140 | ratio_equals | 5.18519 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4534918 |  | CHEMBL4428136 | IC50 | = | 3900 | = | 140 | ratio_equals | 0.0358974 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4536094 |  | CHEMBL4428136 | IC50 | = | 13 | = | 46 | ratio_equals | 3.53846 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4536094 |  | CHEMBL4428136 | IC50 | > | 50000 | = | 46 | not_formed (LDHA censored or other relation) |  | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4543194 |  | CHEMBL4428136 | IC50 | = | 21 | = | 80 | ratio_equals | 3.80952 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4543194 |  | CHEMBL4428136 | IC50 | > | 50000 | = | 80 | not_formed (LDHA censored or other relation) |  | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4543949 |  | CHEMBL4428136 | IC50 | = | 15 | = | 70 | ratio_equals | 4.66667 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4543949 |  | CHEMBL4428136 | IC50 | = | 5100 | = | 70 | ratio_equals | 0.0137255 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4545064 |  | CHEMBL4428136 | IC50 | = | 9 | = | 160 | ratio_equals | 17.7778 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4555982 |  | CHEMBL4428136 | IC50 | = | 37 | = | 190 | ratio_equals | 5.13514 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4557701 |  | CHEMBL4428136 | IC50 | = | 17 | = | 140 | ratio_equals | 8.23529 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4557701 |  | CHEMBL4428136 | IC50 | = | 9900 | = | 140 | ratio_equals | 0.0141414 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4574842 |  | CHEMBL4428136 | IC50 | = | 69 | = | 660 | ratio_equals | 9.56522 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4575930 |  | CHEMBL4428136 | IC50 | = | 52 | = | 780 | ratio_equals | 15 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4576717 |  | CHEMBL4428136 | IC50 | = | 3 | = | 35 | ratio_equals | 11.6667 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4578904 |  | CHEMBL4428136 | IC50 | = | 58 | = | 200 | ratio_equals | 3.44828 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4583899 |  | CHEMBL4428136 | IC50 | = | 25 | = | 180 | ratio_equals | 7.2 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4583899 |  | CHEMBL4428136 | IC50 | = | 25000 | = | 180 | ratio_equals | 0.0072 | Inhibition of LDHA in human MiPaca2 cells assessed as inhibition of lactate production | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4589484 |  | CHEMBL4428136 | IC50 | = | 55 | = | 140 | ratio_equals | 2.54545 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4591832 |  | CHEMBL4428136 | IC50 | = | 82 | = | 800 | ratio_equals | 9.7561 | Inhibition of human recombinant carboxy-terminal His-tagged LDHA by UV endpoint assay | Inhibition of human recombinant carboxy-terminal His-tagged LDHB by UV endpoint assay |
| CHEMBL4753379 |  | CHEMBL5316276 | IC50 | = | 3 | = | 5 | ratio_equals | 1.66667 | Inhibition of human LDHA | Inhibition of human LDHB |
| CHEMBL4847591 |  | CHEMBL4814030 | IC50 | = | 27 | = | 8000 | ratio_equals | 296.296 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4847591 |  | CHEMBL4814030 | IC50 | = | 23400 | = | 8000 | ratio_equals | 0.34188 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4847591 |  | CHEMBL4814030 | IC50 | = | 9400 | = | 8000 | ratio_equals | 0.851064 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4854958 |  | CHEMBL4814030 | IC50 | = | 23 | = | 6000 | ratio_equals | 260.87 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4854958 |  | CHEMBL4814030 | IC50 | = | 1000 | = | 6000 | ratio_equals | 6 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4854958 |  | CHEMBL4814030 | IC50 | = | 1100 | = | 6000 | ratio_equals | 5.45455 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4856798 |  | CHEMBL4814030 | IC50 | = | 8 | = | 2000 | ratio_equals | 250 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4856798 |  | CHEMBL4814030 | IC50 | = | 9100 | = | 2000 | ratio_equals | 0.21978 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4856798 |  | CHEMBL4814030 | IC50 | = | 4700 | = | 2000 | ratio_equals | 0.425532 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4859303 |  | CHEMBL4814030 | IC50 | = | 19 | = | 5000 | ratio_equals | 263.158 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4859303 |  | CHEMBL4814030 | IC50 | = | 690 | = | 5000 | ratio_equals | 7.24638 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4859303 |  | CHEMBL4814030 | IC50 | = | 590 | = | 5000 | ratio_equals | 8.47458 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4860066 |  | CHEMBL4814030 | IC50 | = | 26 | = | 19000 | ratio_equals | 730.769 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4860066 |  | CHEMBL4814030 | IC50 | = | 870 | = | 19000 | ratio_equals | 21.8391 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4860066 |  | CHEMBL4814030 | IC50 | = | 550 | = | 19000 | ratio_equals | 34.5455 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4872752 |  | CHEMBL4814030 | IC50 | = | 22 | = | 5000 | ratio_equals | 227.273 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4872752 |  | CHEMBL4814030 | IC50 | = | 670 | = | 5000 | ratio_equals | 7.46269 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4872752 |  | CHEMBL4814030 | IC50 | = | 730 | = | 5000 | ratio_equals | 6.84932 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4873611 |  | CHEMBL4814030 | IC50 | = | 5 | = | 3000 | ratio_equals | 600 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4873611 |  | CHEMBL4814030 | IC50 | = | 1400 | = | 3000 | ratio_equals | 2.14286 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4873611 |  | CHEMBL4814030 | IC50 | = | 1100 | = | 3000 | ratio_equals | 2.72727 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4876783 |  | CHEMBL4814030 | IC50 | = | 8 | = | 3000 | ratio_equals | 375 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4876783 |  | CHEMBL4814030 | IC50 | = | 2100 | = | 3000 | ratio_equals | 1.42857 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4876783 |  | CHEMBL4814030 | IC50 | = | 1900 | = | 3000 | ratio_equals | 1.57895 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4877797 |  | CHEMBL4814030 | IC50 | = | 314 | = | 1000 | ratio_equals | 3.18471 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4877797 |  | CHEMBL4814030 | IC50 | = | 6700 | = | 1000 | ratio_equals | 0.149254 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4877797 |  | CHEMBL4814030 | IC50 | = | 3100 | = | 1000 | ratio_equals | 0.322581 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4877988 |  | CHEMBL4814030 | IC50 | = | 7 | = | 2000 | ratio_equals | 285.714 | Inhibition of recombinant human LDHA using sodium pyruvate as substrate preincubated for 5 mins followed by di | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4877988 |  | CHEMBL4814030 | IC50 | = | 5000 | = | 2000 | ratio_equals | 0.4 | Inhibition of LDHA in human MIA PaCa2 cells assessed as reduction in lactate production incubated for 2 hrs by | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL4877988 |  | CHEMBL4814030 | IC50 | = | 2300 | = | 2000 | ratio_equals | 0.869565 | Inhibition of LDHA in human A673 cells assessed as reduction in lactate production incubated for 2 hrs by fluo | Inhibition of recombinant human LDHB using sodium pyruvate as substrate preincubated for 5 mins followed by di |
| CHEMBL5171701 |  | CHEMBL5136995 | IC50 | = | 13 | = | 170 | ratio_equals | 13.0769 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5171701 |  | CHEMBL5136995 | IC50 | = | 13 | = | 1800 | ratio_equals | 138.462 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5171701 |  | CHEMBL5136995 | IC50 | = | 190 | = | 170 | ratio_equals | 0.894737 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5171701 |  | CHEMBL5136995 | IC50 | = | 190 | = | 1800 | ratio_equals | 9.47368 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5172378 |  | CHEMBL5136995 | IC50 | = | 13 | = | 8.9 | ratio_equals | 0.684615 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5172378 |  | CHEMBL5136995 | IC50 | = | 13 | = | 310 | ratio_equals | 23.8462 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5172378 |  | CHEMBL5136995 | IC50 | = | 190 | = | 8.9 | ratio_equals | 0.0468421 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5172378 |  | CHEMBL5136995 | IC50 | = | 190 | = | 310 | ratio_equals | 1.63158 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5176448 |  | CHEMBL5136995 | IC50 | = | 2.9 | = | 65 | ratio_equals | 22.4138 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5176448 |  | CHEMBL5136995 | IC50 | = | 2.9 | = | 330 | ratio_equals | 113.793 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5176448 |  | CHEMBL5136995 | IC50 | = | 63 | = | 65 | ratio_equals | 1.03175 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5176448 |  | CHEMBL5136995 | IC50 | = | 63 | = | 330 | ratio_equals | 5.2381 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5177632 |  | CHEMBL5136995 | IC50 | = | 4 | = | 47 | ratio_equals | 11.75 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5180187 |  | CHEMBL5120856 | IC50 | = | 400 | = | 200 | ratio_equals | 0.5 | Inhibition of human recombinant LDHA using pyruvate as substrate preincubated for 10 mins followed by substrat | Inhibition of human recombinant LDHB using pyruvate as substrate preincubated for 10 mins followed by substrat |
| CHEMBL5180187 |  | CHEMBL5120856 | Ki | = | 90 | = | 700 | ratio_equals | 7.77778 | Non-competitive inhibition of human recombinant LDHA assessed as inhibition constant using varying concentrati | Non-competitive inhibition of human recombinant LDHB assessed as inhibition constant using varying concentrati |
| CHEMBL5181496 |  | CHEMBL5136995 | IC50 | = | 0.9 | = | 2.8 | ratio_equals | 3.11111 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5181496 |  | CHEMBL5136995 | IC50 | = | 0.9 | = | 31 | ratio_equals | 34.4444 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5181496 |  | CHEMBL5136995 | IC50 | = | 4.4 | = | 2.8 | ratio_equals | 0.636364 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5181496 |  | CHEMBL5136995 | IC50 | = | 4.4 | = | 31 | ratio_equals | 7.04545 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5181996 |  | CHEMBL5136995 | IC50 | = | 2.2 | = | 15 | ratio_equals | 6.81818 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5181996 |  | CHEMBL5136995 | IC50 | = | 2.2 | = | 90 | ratio_equals | 40.9091 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5181996 |  | CHEMBL5136995 | IC50 | = | 22 | = | 15 | ratio_equals | 0.681818 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5181996 |  | CHEMBL5136995 | IC50 | = | 22 | = | 90 | ratio_equals | 4.09091 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5182266 |  | CHEMBL5136995 | IC50 | = | 2.9 | = | 17 | ratio_equals | 5.86207 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5182266 |  | CHEMBL5136995 | IC50 | = | 2.9 | = | 68 | ratio_equals | 23.4483 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5182266 |  | CHEMBL5136995 | IC50 | = | 6.9 | = | 17 | ratio_equals | 2.46377 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5182266 |  | CHEMBL5136995 | IC50 | = | 6.9 | = | 68 | ratio_equals | 9.85507 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5183539 |  | CHEMBL5136995 | IC50 | = | 1.6 | = | 9.8 | ratio_equals | 6.125 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5185237 |  | CHEMBL5136995 | IC50 | = | 2.5 | = | 1.7 | ratio_equals | 0.68 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5185237 |  | CHEMBL5136995 | IC50 | = | 2.5 | = | 38 | ratio_equals | 15.2 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5185237 |  | CHEMBL5136995 | IC50 | = | 11 | = | 1.7 | ratio_equals | 0.154545 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5185237 |  | CHEMBL5136995 | IC50 | = | 11 | = | 38 | ratio_equals | 3.45455 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5187919 |  | CHEMBL5136995 | IC50 | = | 90 | = | 810 | ratio_equals | 9 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5188480 |  | CHEMBL5136995 | IC50 | = | 3.8 | = | 25 | ratio_equals | 6.57895 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5188480 |  | CHEMBL5136995 | IC50 | = | 3.8 | = | 650 | ratio_equals | 171.053 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5188480 |  | CHEMBL5136995 | IC50 | = | 68 | = | 25 | ratio_equals | 0.367647 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5188480 |  | CHEMBL5136995 | IC50 | = | 68 | = | 650 | ratio_equals | 9.55882 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5189798 |  | CHEMBL5136995 | IC50 | = | 26 | = | 75 | ratio_equals | 2.88462 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5189798 |  | CHEMBL5136995 | IC50 | = | 26 | = | 950 | ratio_equals | 36.5385 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5189798 |  | CHEMBL5136995 | IC50 | = | 430 | = | 75 | ratio_equals | 0.174419 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5189798 |  | CHEMBL5136995 | IC50 | = | 430 | = | 950 | ratio_equals | 2.2093 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5189879 |  | CHEMBL5136995 | IC50 | = | 3.7 | = | 46 | ratio_equals | 12.4324 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5192632 |  | CHEMBL5136995 | IC50 | = | 66 | = | 400 | ratio_equals | 6.06061 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5194549 |  | CHEMBL5136995 | IC50 | = | 2.5 | = | 9.5 | ratio_equals | 3.8 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5194549 |  | CHEMBL5136995 | IC50 | = | 2.5 | = | 90 | ratio_equals | 36 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5194549 |  | CHEMBL5136995 | IC50 | = | 3.2 | = | 9.5 | ratio_equals | 2.96875 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5194549 |  | CHEMBL5136995 | IC50 | = | 3.2 | = | 90 | ratio_equals | 28.125 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5194727 |  | CHEMBL5136995 | IC50 | = | 43 | = | 290 | ratio_equals | 6.74419 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196259 |  | CHEMBL5136995 | IC50 | = | 8.6 | = | 57 | ratio_equals | 6.62791 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196259 |  | CHEMBL5136995 | IC50 | = | 8.6 | = | 810 | ratio_equals | 94.186 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196259 |  | CHEMBL5136995 | IC50 | = | 160 | = | 57 | ratio_equals | 0.35625 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196259 |  | CHEMBL5136995 | IC50 | = | 160 | = | 810 | ratio_equals | 5.0625 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196929 |  | CHEMBL5136995 | IC50 | = | 2.7 | = | 8.2 | ratio_equals | 3.03704 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196929 |  | CHEMBL5136995 | IC50 | = | 2.7 | = | 330 | ratio_equals | 122.222 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196929 |  | CHEMBL5136995 | IC50 | = | 55 | = | 8.2 | ratio_equals | 0.149091 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5196929 |  | CHEMBL5136995 | IC50 | = | 55 | = | 330 | ratio_equals | 6 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5197729 |  | CHEMBL5136995 | IC50 | = | 36 | = | 75 | ratio_equals | 2.08333 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5201115 |  | CHEMBL5136995 | IC50 | = | 1.8 | = | 2.2 | ratio_equals | 1.22222 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5201115 |  | CHEMBL5136995 | IC50 | = | 1.8 | = | 85 | ratio_equals | 47.2222 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5201115 |  | CHEMBL5136995 | IC50 | = | 37 | = | 2.2 | ratio_equals | 0.0594595 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5201115 |  | CHEMBL5136995 | IC50 | = | 37 | = | 85 | ratio_equals | 2.2973 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5202219 |  | CHEMBL5136995 | IC50 | = | 10 | = | 34 | ratio_equals | 3.4 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5202219 |  | CHEMBL5136995 | IC50 | = | 10 | = | 290 | ratio_equals | 29 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5202219 |  | CHEMBL5136995 | IC50 | = | 75 | = | 34 | ratio_equals | 0.453333 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5202219 |  | CHEMBL5136995 | IC50 | = | 75 | = | 290 | ratio_equals | 3.86667 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5205566 |  | CHEMBL5136995 | IC50 | = | 90 | = | 200 | ratio_equals | 2.22222 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5205566 |  | CHEMBL5136995 | IC50 | = | 90 | = | 750 | ratio_equals | 8.33333 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5205566 |  | CHEMBL5136995 | IC50 | = | 430 | = | 200 | ratio_equals | 0.465116 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5205566 |  | CHEMBL5136995 | IC50 | = | 430 | = | 750 | ratio_equals | 1.74419 | Inhibition of LDHA (unknown origin) | Inhibition of LDHB (unknown origin) |
| CHEMBL5416627 |  | CHEMBL5316276 | IC50 | = | 2.6 | = | 43 | ratio_equals | 16.5385 | Inhibition of recombinant human LDHA | Inhibition of recombinant human LDHB |
| CHEMBL5597066 |  | CHEMBL5584248 | IC50 | = | 44 | = | 15480 | ratio_equals | 351.818 | Inhibition of human LDH-A incubated for 10 mins in presence of NADPH by fluorescence based reader assay | Inhibition of human LDH-B incubated for 10 mins in presence of NADPH by fluorescence based reader assay |
| CHEMBL5597243 |  | CHEMBL5584248 | IC50 | = | 72 | = | 1200 | ratio_equals | 16.6667 | Inhibition of human LDH-A incubated for 10 mins in presence of NADPH by fluorescence based reader assay | Inhibition of human LDH-B incubated for 10 mins in presence of NADPH by fluorescence based reader assay |
