# COMMIT CANDIDATE — CC-20261003-B-ZFRA-TRANSFER-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 2 2026-10-03, branch `task/sci-B-20261003`.
**context_policy:** `SOURCE_FIRST` for all six readings; LEGEND's own records were opened only after each first pass was written (see `research/intake_wave_20261003_B.md`).
**Not medical advice.** Class-level statements about published models and genotypes only.

## Target
- `dismissal_ledger_current.md`: **create** `DIS-030` after `DIS-029`.
- `full_text_queue_current.md`: **replace-within** `FT-104` — discharge the declared reading debt and record its outcome.

**Number is provisional.** `DIS-030` is the next free number measured on `main` eb01d5f (max `DIS-029`). The integrator renumbers in event order.

## Change class
**MINOR** (§ 7). A rejection record plus a queue-record discharge. No claim status changes here; the related claim qualification is in `CC-20261003-B-HET-ENDPOINT-01`, which must be applied with this one so that `CLAIM 032` and `DIS-030` agree.

## Ordering
Apply after `CC-20261003-B-REGISTRY-01` if the integrator wants the `PAPER 135` / `PAPER 136` wikilinks live; `legend_lint.py` tolerates the reverse order but reports the dangling link until both land.

## The two halves, and why they are rejected together
They are rejected in one record because they are the same citation doing two jobs: PMID 29067327 is cited through this corpus both as *the therapeutic result* and as *the heterozygote result*, and both uses fail for reasons found in the same reading. The first fails because the treated animals have no WWOX allele; the second fails because its only panel does not reproduce its own legend.

**What is NOT rejected:** the heterozygote cognitive deficit itself. That is measured, in a different paper (PMID 36498839, Figure 5A–C), and is carried in `CC-20261003-B-HET-ENDPOINT-01`.

## Op list — `dismissal_ledger_current.md` (record-scoped; dry run 2026-10-03 against `main` eb01d5f: exit 0, 1 op, key `['DIS-029']`, `inserted_bytes` 2651, `replaced_bytes` 0, scope proof clean)

```json
[
 {
  "op": "insert-after",
  "id": "DIS-029",
  "text": "\n### DIS-030 — «The Zfra peptide result transfers to a WWOX genotype class, and `Wwox+/−` mice decline faster than 3×Tg mice» → ❌ **REJECTED on both halves**\n- **PREMISE: DATO** (2026-10-03, `CC-20261003-B-ZFRA-TRANSFER-01`, intake wave 2, Scientist B; read at source under `context_policy: SOURCE_FIRST`). **First half — the transfer.** The treated animals of [[paper_registry_current#PAPER 136]] are 3×Tg-AD (`Psen1` M146V, APPswe, tau P301L) with **wild-type `Wwox`**. There is no WWOX allele in the intervention cohort at all. Dose 2 mM Zfra4–10 in 100 µL PBS by tail vein, four weekly injections from 10 months, PBS sham as the only comparator — no vehicle-plus-scrambled arm, no dose–response, no pharmacokinetics; the melanoma arm of the same paper uses 1 mM in water. **Blinding and randomisation are not mentioned in any of the six sources of this wave** (`blind` and `randomi`: 0 occurrences in each fingerprinted artefact). Group sizes in that paper are inconsistent four ways (Methods 5/5; Fig 1A 6/5; Fig 1B 12/10; Fig 2 3/5), and the histology statistics are computed over **fields (n = 10) and cells (n = 40), not animals**. The authors themselves report that the activated cells do not reach the brain and that efficacy **fails** when treatment starts two months later.\n- **Second half — the heterozygote comparison, which is the sentence the rest of the corpus cites.** It rests on **one unlabelled supplementary bar chart** whose numbers do not reproduce its own legend. The legend claims a drop *«greater than 55%»* at ages 10–12 in `Wwox+/−` against under 50% in 3×Tg. The figure's axes read 3, >10, 8, 10 months, carry **no genotype label on any bar**, contain **no age 12**, and have no n per bar, no error convention and no statistical test. Under either assignment of the two bar pairs to the two genotypes the drops are ≈ 43% and 13% (short-term) and ≈ 52% and 33% (long-term). **No arrangement yields «greater than 55%».**\n- **Boundary:** it does not follow that the peptide is inert, nor that WWOX heterozygotes are normal — [[paper_registry_current#PAPER 135]] measures a heterozygote cognitive deficit properly and is carried as such. What follows is that **this paper may not be cited as a WWOX intervention, and its supplementary figure may not be cited as evidence that heterozygotes decline faster than 3×Tg.**\n- **`REVIVAL_TRIGGER`:** the peptide administered to an animal with a defined WWOX genotype, blinded, with a scrambled-peptide comparator and an endpoint measured per animal; or a labelled, powered replot of the heterozygote comparison with its n and its test stated.\n"
 }
]
```

## Op list — `full_text_queue_current.md` (record-scoped; dry run 2026-10-03 against `main` eb01d5f: exit 0, 1 op, key `['FT-104']`, `replaced_bytes` 189, `inserted_bytes` 1241, scope proof clean)

```json
[
 {
  "op": "replace-within",
  "id": "FT-104",
  "old": "**Next action:** recuperare i pannelli di §3.5 quando esista una rotta di acquisizione che\npreservi le immagini; nel frattempo **non promuovere la contro-evidenza oltre lo stato di flag**.",
  "new": "**Next action:** recuperare i pannelli di §3.5 quando esista una rotta di acquisizione che\npreservi le immagini; nel frattempo **non promuovere la contro-evidenza oltre lo stato di flag**.\n\n🟢 **DISCHARGED 2026-10-03** by `CC-20261003-B-ZFRA-TRANSFER-01` (intake wave 2, Scientist B). The panel was acquired: `mmc1.docx` from the PMC open-access S3 mirror, its `word/media/image1.tiff` extracted and rendered (`files/figure_renders/PMID29067327/supp_fig1.png`, sha256 `a796f685b2e70fa378b0fcb07ba97afbeaad5348bc014f5c0cd39bf42327c755`). 🔴 **The outcome is worse than a flag.** Supplementary Figure 1 carries **no genotype label on any bar**, no n per bar, no error convention and no statistical test; its x-axes read 3, >10, 8, 10 months and contain **no age 12**, while its legend asserts a drop *«greater than 55%»* at ages 10–12. Under either assignment of the two bar pairs to the two genotypes the drops are ≈ 43%/13% and ≈ 52%/33%. The counter-evidence to [[claim_registry_current#CLAIM 032]] therefore **does not survive inspection at all** and is rejected in `DIS-030`, not promoted. The real heterozygote cognitive measurement is in PMID 36498839 (Figure 5A–C), which is a different source and is carried separately."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT

(The treated cohort and its schedule | `five 3×Tg mice received four consecutive weekly injections` | PMID 29067327, Methods, 'Animals')

(The model the treated cohort carries | `The 3×Tg mice develop intracellular A` | PMID 29067327, Methods, 'Animals')

(The statistical declaration states the test and no allocation or masking procedure | `two-tailed Mann–Whitney test (PBS group, ` | PMID 29067327, Figure 2 legend)

(The authors state the activated cells do not reach the brain | `Z cells did not appear to migrate to the brain` | PMID 29067327, Results, 'Zfra induces Z cells to relocate out of the spleen and does not appear to migrate to the brain')

(The authors' own efficacy ceiling | `injected Zfra fails to restore memory deficit` | PMID 29067327, Discussion)

(An earned negative the authors report against themselves | `Zfra treatment did not change the number of BrdU` | PMID 29067327, Results, 'Zfra does not induce neurogenesis in 3xTg mice')

(The body sentence the supplementary panel contradicts | `Wwox heterozygous mice exhibited an age-related faster decline` | PMID 29067327, Results, 'Wwox heterozygous mice exhibit enhanced memory decline')

(Figure attestation: the supplementary panel's own content | `[figure attestation - pixels cannot be quote-matched] Supplementary Fig. S1: two panels, 'Short-term memory' bars at months 3 (~78), >10 (~45), 8 (~75), 10 (~65); 'Long-term memory' bars at months 3 (~87), >10 (~42), 8 (~75), 10 (~50); a red horizontal line at 50 percent and a red vertical line between the second and third bar of each panel; y-axis '% Exploration time'; no genotype appears on either axis.` | PMID 29067327, Supplementary Figure 1, `files/figure_renders/PMID29067327/supp_fig1.png`)

(Figure attestation: the histology statistics are over fields and cells | `[figure attestation - pixels cannot be quote-matched] Fig 3C '# of pT181-Tau tangles per field', PBS ~13 vs Zfra ~9, p < 0.001, 'n = 10'; Fig 3D '% Reduction in intracellular pS35-TPC6A', PBS 100 vs Zfra ~40, p < 0.00001, 'n = 40'.` | PMID 29067327, Figure 3, `files/figures/PMID29067327/native/gr3.jpg`)
