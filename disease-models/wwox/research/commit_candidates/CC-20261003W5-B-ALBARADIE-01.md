# COMMIT CANDIDATE — CC-20261003W5-B-ALBARADIE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 5 2026-10-03, branch `task/sci-B-20261003w5`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w5_B.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`discovery_ledger_current.md` · `DL-MECH-022` (genotype positioning between the null WOREE pole and the hypomorphic SCAR12 pole): one dated bullet before `Interconnessioni`.

## Finding
PMID 35792847 shows one allele on both sides of the WOREE/SCAR12 line: three P47T homozygotes — the SCAR12 founding allele — are labelled WOREE by the authors, but present with onset at six months, no microcephaly, no optic atrophy, seizures controlled in two of three, and one ambulant sib with tremor and ataxic gait. In the same series the Q230P homozygote sits at the severe end (onset 21 days, suppression-burst, optic atrophy, band heterotopia). The paper itself does no genotype-phenotype analysis — its abstract's claim of correlations is not carried by its body — so the observation is the reader's, from the paper's tables.

**Genotype caution.** Q230P homozygous is not the reference genotype; the severe homozygous course does not position Q230P in trans with a splice-acceptor allele. P47T ≠ Q230P.

## Change class
**MINOR** — an addition to an open discovery lead; no claim or block change.

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main 48f1fe9 (branch base; no registry file changed on the branch): exit 0, 1 op(s), anchors ['DL-MECH-022'])

```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-022",
  "old": "- **Interconnessioni**: [[claim_registry_current#CLAIM 019]]",
  "new": "- 🟡 **ADDITION — 2026-10-03 (intake wave 5, Scientist B, `CC-20261003W5-B-ALBARADIE-01`; read at source, receipt `FTR-20261003-35792847-01`).** [[paper_registry_current#PAPER 156]] gives **one allele on both sides of the WOREE/SCAR12 line**: three P47T homozygotes (the SCAR12 allele of [[paper_registry_current#PAPER 042]]) labelled WOREE by the authors, with onset at 6 months, no microcephaly, no optic atrophy, seizures controlled in two of three, and one sib ambulant with action tremor and ataxic gait. In the same series the Q230P **homozygote** presents at the severe end (onset 21 days, suppression-burst, optic atrophy, band heterotopia). `PREMISE: DATO` for the descriptions; `INFERENZA` for the reading that the WOREE/SCAR12 boundary is a continuum within an allele class rather than two allele-defined syndromes (n = 3, two families, no functional data). It does not position the reference genotype: Q230P homozygous ≠ the compound heterozygote, and a severe homozygous course says nothing about Q230P in trans with a splice-acceptor allele.\n- **Interconnessioni**: [[claim_registry_current#CLAIM 019]]"
 }
]
```

## Registry records needed
`PAPER 156` (created by `CC-20261003W5-B-REGISTRY-01`); `PAPER 042` exists.

### LOCATOR TRIPLES FOR BLIND AUDIT
(the P47T allele is homozygous in a family-1 patient | Patient 1.2 WWOX c.139C>A (p.Pro47Thr) Homozygous Familial mutation testing Missense | PMID 35792847, Table 2; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(a P47T-homozygous sib walks with tremor and ataxic gait | action tremors, and an ataxic gait. | PMID 35792847, Results, Patient 1.2; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(the Q230P allele is homozygous in family 6 | Patient 6 WWOX c.689A>C (p.Gln230Pro) Homozygous WES Missense | PMID 35792847, Table 2; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(the Q230P homozygote had a suppression-burst EEG | An EEG showed a suppression-burst background pattern | PMID 35792847, Results, Patient 6; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(the Q230P homozygote has band heterotopia on MRI | Brain MRI showed supratentorial tissue volume loss with subcortical band heterotopia. | PMID 35792847, Results, Patient 6; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(the abstract claims genotype-phenotype correlations | We established correlations between genotype and phenotype in our cases and previously reported cases. | PMID 35792847, Abstract, Results; files/fulltext/PMID35792847_AlBaradie2022_JLE_abstract.html)
