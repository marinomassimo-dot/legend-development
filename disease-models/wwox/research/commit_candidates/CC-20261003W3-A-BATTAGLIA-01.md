# COMMIT CANDIDATE — CC-20261003W3-A-BATTAGLIA-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 3 2026-10-03, branch `task/sci-A-20261003w3`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w3_A.md`, which also declares two exposures before reading).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`paper_registry_current.md`: `PAPER 046` (Battaglia 2023, PMID 38161429).

## What the reading found
1. `Evidence depth` declares `complete_fulltext_read` against a legacy reconstruction and a bounded verification; the new receipt is partial only for the open multihop queue.
2. "101 casi da 9 studi" is carried as a model/species line; 101 is a sum of overlapping sources (Banne 2021's 56 collated cases predate and can include seven of the other eight); the review's own Clinical section says 84.
3. "Oliver 7/13" is the fraction re-imaged, all of whom progressed; the review's "approximately 13%" divides serially imaged numerators by all 101.
4. The record says the review "nega" (denies) polymicrogyria; the review does not mention it.
5. The Q230P "eight cases overall" and the exon 6-8 instability statement are citations of the review's reference 1, not counts or measurements by these authors. The abstract's "all affected patients" with MRI anomalies is contradicted by its own Piard row (80%).

## Noted, NOT proposed (research layer, append-only, other batches)
- `DL-MOL-012` sources the Q230P "8 casi" to this review; its provenance is the review's reference 1 (Aldaz and Hussain 2020).
- `DL-MECH-042` infers "il primo segno rilevabile è cerebellare" from one fetus at 21 weeks (Iacomino 2020, re-used in Figure 1) against a five-patient cohort with an unaffected cerebellum; the inference is not supported by a denominator. Already partly addressed by `CC-20260922-VERMIS-HYPOPLASIA-FREQUENCY-01`.

## Change class
**MINOR** — background paper record (`Claim links: none — background`); no claim or working-model block changes.

## Ordering
The receipts named below must be appended to the ledger before this candidate is propagated, so that no record cites a receipt the ledger does not hold. Receipt: `FTR-20261003-38161429-01`.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on copies of `main` c740c6e: exit 0, 5 op(s), keys ['PAPER 046' x5])

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 046",
  "old": "**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)",
  "new": "**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-38161429-01` (every section, Table 1, Figure 1 and the reference list read; partial only because the multihop queue of gene-direct references is open); earlier `FTR-20260726-38161429-01` (legacy reconstruction) and `FTR-20260927-38161429-02` (bounded verification); manifest `deepdive_manifests/PMID38161429.json`; dossier `research/fulltext_dossiers/PMID38161429.md`"
 },
 {
  "op": "replace-within",
  "id": "PAPER 046",
  "old": "**Model/species:** human — 101 casi da 9 studi",
  "new": "**Model/species:** human — Table 1 sums nine overlapping sources to '101'; this is not a patient count (Banne 2021's 56 collated cases predate and can include seven of the other eight sources, and the review's own Clinical section says 84 patients)"
 },
 {
  "op": "replace-within",
  "id": "PAPER 046",
  "old": "Progressione su imaging seriato (Tabarki 5/5; Oliver 7/13).",
  "new": "Progressione su imaging seriato (Tabarki 5/5; Oliver: 7 of 13 had serial MRI and all 7 progressed — 7/13 is the fraction re-imaged, not a progression rate). The review's 'approximately 13%' divides these numerators by all 101, including patients never re-imaged, and is not a rate."
 },
 {
  "op": "replace-within",
  "id": "PAPER 046",
  "old": "**Omissione rilevata:** la review nega la polimicrogiria,",
  "new": "**Omissione rilevata:** la review non menziona la polimicrogiria (silent, not a denial),"
 },
 {
  "op": "replace-within",
  "id": "PAPER 046",
  "old": "→ Q230P è un **hotspot ricorrente**; il suo meccanismo è dichiarato **non dimostrato**.",
  "new": "→ Q230P è un **hotspot ricorrente**; il suo meccanismo è dichiarato **non dimostrato**. 🔴 Provenance: the 'eight cases overall' is the review's citation of its reference 1 (Aldaz and Hussain 2020), not a count made by these authors; the same holds for its statement that exon 6-8 deletions give unstable products. The abstract's 'All affected patients showed brain anomalies' is contradicted by its own Piard row (abnormal MRI in 80%)."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the review counts 84 reported patients in its clinical section | 84 patients have been reported in the literature with descriptions of the individual phenotypes | PMID 38161429, Clinical findings para 1; files/fulltext/PMID38161429_Battaglia2023_PMC_2026-09-27.xml)
(one summed source is itself a collation of 56 published cases | Similar features were found in 2021 by Banne et al., who retrospectively analyzed 45 variants in 56 WOREE published cases. | PMID 38161429, Imaging findings, Banne/Oliver paragraph; files/fulltext/PMID38161429_Battaglia2023_PMC_2026-09-27.xml)
(seven of thirteen Oliver patients had serial MRI and those progressed | Lastly, 7 of 13 patients underwent serial MRI, which showed progression of the abnormalities with age | PMID 38161429, Imaging findings, Banne/Oliver paragraph; files/fulltext/PMID38161429_Battaglia2023_PMC_2026-09-27.xml)
(the 13% progression figure is stated over the whole review | approximately 13% of the patients included in the study also demonstrated age-related progression | PMID 38161429, Imaging findings, closing paragraph; files/fulltext/PMID38161429_Battaglia2023_PMC_2026-09-27.xml)
(one cited study found abnormal MRI in 80% | The study detected abnormal brain MRI in 80% of them | PMID 38161429, Imaging findings, Johannsen/Piard paragraph; files/fulltext/PMID38161429_Battaglia2023_PMC_2026-09-27.xml)
(the eight-case Q230P count is attributed to reference 1 | has been described both in homozygosity and in compound heterozygosity in eight cases overall | PMID 38161429, Genetic findings para 6; files/fulltext/PMID38161429_Battaglia2023_PMC_2026-09-27.xml)
