# COMMIT CANDIDATE — CC-20261004W7-B-PATIENT-OVERLAP-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 7 2026-10-04, branch `task/sci-B-20261004w7`.
**context_policy:** `SOURCE_FIRST` — first pass written and committed from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261004w7_B.md`).
**Not medical advice.** Class-level statements about published patients and genotypes only.

## Target
`paper_registry_current.md` · `PAPER 171` (Al Baradie 2022) and `PAPER 143` (Nagarajan 2023): one sentence appended to each `Role`.

## Finding (counting, class level; every overlap judgement is INFERENZA)
1. **`c.606-1G>A` homozygotes.** PMID 36937954 adds one more homozygote of this canonical acceptor allele, from a Saudi tertiary children's hospital tested 2015-2018, with nothing printed beyond the variant row. Held reports of the same allele: Shaukat 2018 (`PAPER 045`), Al Baradie 2022 family 3 (`PAPER 171`, open overlap with Tabarki 2015), Tabarki 2015 (unread) and PMID 26345274 (five patients, unread). The new row can be neither matched nor excluded; count it once as unlinked.
2. **The Tabarki 2015 premise of the selection record does not hold for PMID 42807679.** The Tunisian patient there is a heterozygous contiguous 16q deletion; Tabarki 2015 is held as a homozygous sequence allele. That paper cannot resolve the overlap; PMID 36937954 is the source that bears on it, and it is too thin to settle it.
3. **`p.Arg264*` homozygotes.** Held: the Piard 2019 sibling pair (India, consanguineous) and one Nagarajan 2023 child (India). Nothing printed excludes identity of the Nagarajan child with Piard patient 14; count at most three, possibly two. The two Turkish homozygotes of PMID 42394473 are a separate population and are counted as new.
4. **No overlap found** for PMID 40429983 (Romanian compound heterozygote), PMID 42248868 (no patient detail) or PMID 42807679 (no WWOX sequence allele).

## Change class
**MINOR** — counting qualifications on two paper records; no claim status changes.

## Registry records needed
`PAPER 201`, `PAPER 202` (created by `CC-20261004W7-B-REGISTRY-01`; renumber with it).

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on main 70513cd merged into the branch: exit 0, 2 op(s), anchors ['PAPER 171', 'PAPER 143'])

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 171",
  "old": "**do not use its percentages as a WOREE denominator.**",
  "new": "**do not use its percentages as a WOREE denominator.** 🔴 **Family 3 / Tabarki 2015, one more candidate (`CC-20261004W7-B-PATIENT-OVERLAP-01`, intake wave 7):** [[paper_registry_current#PAPER 202]] (PMID 36937954) reports one more homozygous `c.606-1G>A` from a Saudi tertiary children's hospital tested 2015-2018, with no sex, onset, course or outcome printed — it can be neither matched to nor excluded from family 3, Tabarki 2015 or the five patients of PMID 26345274. Count it once as unlinked; the four held reports of this allele are not independent families until a primary settles it. PMID 42807679 (a Tunisian heterozygous 16q deletion) cannot bear on the Tabarki overlap at all. `PREMISE: INFERENZA`."
 },
 {
  "op": "replace-within",
  "id": "PAPER 143",
  "old": "overlap with earlier reports is not excluded by the source.",
  "new": "overlap with earlier reports is not excluded by the source. 🔴 **One specific candidate (`CC-20261004W7-B-PATIENT-OVERLAP-01`, intake wave 7):** the homozygous `p.Arg264Ter` child here and the homozygous `p.Arg264*` sibling pair of [[paper_registry_current#PAPER 117]] (Piard 2019 Supplementary Table 1 patients 13-14: origin India, consanguineous; patient 14 male, 18 months at last examination) share allele and country; nothing printed in either excludes identity. Until a primary or the authors settle it, count at most three and possibly two p.Arg264* homozygotes across the two papers. The two Turkish p.Arg264* homozygotes of [[paper_registry_current#PAPER 201]] are a separate population and do not overlap either. `PREMISE: INFERENZA`."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(a homozygous c.606-1G>A row is listed without per-patient phenotype | WWOX (NM_016373.4):c.606-1G > A Homozygous Pathogenic | PMID 36937954, Table 2; files/fulltext/PMID36937954_Alotibi2023_PMC.xml)
(the cohort was tested at one Saudi children's hospital between 2015 and 2018 | A retrospective study on 105 patients diagnosed with NDDs between 2015 and 2018. | PMID 36937954, Methods, Study population; files/fulltext/PMID36937954_Alotibi2023_PMC.xml)
(the Tunisian WWOX-including event is a heterozygous de novo deletion | Arr16q(74,718,513 87,891,103)x1 L L WWOX ANKRD11 ZNF778 CDH15 CDH13 De novo P | PMID 42807679, Table 3 row P8; files/fulltext/PMID42807679_Khadija2026_PMC.xml)
(two Turkish case rows are homozygous p.Arg264* | 51 M WWOX Nonsense c.790C>T p.Arg264* Hom Reported ClinVar ID:241105 PVS1, PM3, PM2 P Neonatal GES | PMID 42394473, Table 2 row 51; files/fulltext/PMID42394473_Karaer2026_PMC.xml)
(the paper does not state whether the two WWOX patients are related | Two patients with WWOX p.Arg264* (Cases 29, 51) exhibited generalized epileptic spasms, developmental regression, and abnormal MRI | PMID 42394473, Discussion; files/fulltext/PMID42394473_Karaer2026_PMC.xml)


---

## BATCH DISPOSITION

**Verdict:** `PROPAGATED` by `BATCH_20261004_001` (2026-10-04, MINOR, WM_v7.13 → WM_v7.14; ACTOR_ID `scientist`, Scientist K, batch integrator).
**Surfaces written:** paper_registry_current.md

Two `replace-within` ops, on `PAPER 171` (Al Baradie 2022) and `PAPER 143` (Nagarajan 2023); both `old` strings measured **exactly one** occurrence inside their live records. Wikilinks renumbered with the registry candidate: `PAPER 201` → `205`, `PAPER 202` → `206`.
🔴 **Every overlap judgement keeps its `INFERENZA` label, as the dispatch required, and none is resolved.** The Nagarajan `p.Arg264*` homozygote **may** be Piard patient 14 — allele and country shared, nothing printed in either source excluding identity — so the landed count is *at most three and possibly two*. The `c.606-1G>A` homozygote of PMID 36937954 is **unlinked and undetermined** against Al Baradie family 3, Tabarki 2015 and PMID 26345274, and is counted **once as unlinked**. Tabarki 2015 remains **unread**, and the record says so rather than treating it as a resolver. PMID 42807679 is a heterozygous contiguous 16q deletion and cannot bear on the Tabarki overlap at all.
One integrator amendment from the blind audit: the Alotibi window is the **diagnosis** window (2015–2018), not a testing window. An auditor also verified, by reading every occurrence of WWOX, *consanguin\**, *sibling* and *famil\** in the Karaer artefact, that it states **nothing** about whether its two `p.Arg264*` cases are related, while naming siblings explicitly where it has them — an informative silence, and the reason those two are counted as a separate population rather than merged.
