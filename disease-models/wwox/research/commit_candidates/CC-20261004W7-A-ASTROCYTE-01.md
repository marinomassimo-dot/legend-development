# COMMIT CANDIDATE — CC-20261004W7-A-ASTROCYTE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 7 2026-10-04, branch `task/sci-A-20261004w7`.
**context_policy:** `SOURCE_FIRST` — the review was read and its first pass written before `CLAIM 005` or any other record about the glial axis was opened.
**Not medical advice.**

## What changed

A 2026 narrative review from a group with no WWOX publications (PMID 42558002) tabulates the WWOX astrocyte evidence beside twelve other genetic epilepsies. Three things in it bear on LEGEND's glial axis:

1. **It marks every WWOX row "Unclear"** in the column that asks whether the astrocyte phenotype is reactive or cell-intrinsic — the one column that would answer cell autonomy. For SCN1A, SLC6A1, MECP2 and ALDH7A1 it fills that column with "Reactive", "Intrinsic" or both.
2. **It states the downstream direction explicitly for WWOX**, from the conditional-knockout evidence: astrocyte changes "occur as a result of neuronal dysfunction and seizure activity".
3. **The negative it rests that on is narrower than the conclusion.** Checked against the primary LEGEND holds on disk, the astrocyte conditional knockout was negative for three gross organismal measures — developmental delay, weight loss and postnatal lethality — in the astrocyte **and** oligodendrocyte knockouts. No astrocyte function, seizure or network measurement was made in those animals, so the negative cannot carry a direction by itself; what carries it is the correlation (GFAP up in the neuronal knockout), and the review's own conclusion says the relative contribution of astrocytes is hard to establish.

This is a third-party reading of evidence LEGEND already holds, not new evidence. It is proposed as an addition to the evidence boundary of `CLAIM 005`, which makes no cell-autonomy assertion of its own.

## Target
- `claim_registry_current.md`, record `CLAIM 005` — append one sentence to the end of the existing `**Evidence boundary:**` field.

## Change class
**MINOR.** `CLAIM 005` is `consolidated baseline`, so the test of § 7 is whether this narrows or reverses it. It does neither: the claim asserts lower PV-positive interneuron counts and higher IBA1/GFAP area fractions in one constitutive knockout, and says nothing about whether the glial change is cell-autonomous. The addition records that an independent group, reading the same primaries, leaves that question open and states the downstream direction — and it names the limit of the evidence behind that direction. No summary, status, transferability or clinical-relevance field is touched. **If the integrator judges this to narrow the claim, it must be re-classed MAJOR and routed through `legend-locator-audit` before propagation; the triples below are supplied for that.**

## Op list — `claim_registry_current.md` (record-scoped)

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 005",
  "old": "🔵 **PMID 19936220 remains free of any seizure measurement — that is a statement about that paper, not about the animal.**",
  "new": "🔵 **PMID 19936220 remains free of any seizure measurement — that is a statement about that paper, not about the animal.** 🔵 **Third-party reading of the glial axis (2026-10-04, `CC-20261004W7-A-ASTROCYTE-01`, intake wave 7 Scientist A):** a narrative review by a group with no WWOX publications (PMID 42558002, [[paper_registry_current#PAPER 184]]) tabulates four WWOX models beside twelve other genetic epilepsies and marks **every one of them `Unclear`** in the column that asks whether the astrocyte phenotype is reactive or cell-intrinsic, while filling that column for SCN1A, SLC6A1, MECP2 and ALDH7A1. It states the direction for WWOX — astrocyte changes «occur as a result of neuronal dysfunction and seizure activity» — on the strength of the astrocyte conditional knockout. 🔴 That negative is narrower than the conclusion drawn from it: in the primary (PMID 33914858) the astrocyte **and** oligodendrocyte conditional knockouts are negative for three **gross organismal** measures — developmental delay, weight loss and postnatal lethality — with no astrocyte function, seizure or network measurement made in those animals, so the direction rests on a correlation (GFAP up in the neuronal knockout), as the review's own conclusion concedes («it can be difficult to establish the relative contribution of astrocytes»). Nothing in this claim's own measurements is changed: cell autonomy of the glial change remains unmeasured in every WWOX model LEGEND holds."
 }
]
```

## Two defects of the review itself, recorded but not propagated

- A Table 1 cell reads **"No seizures"** for the constitutive null while the narrative for the same row says only "although no seizure activity was reported". A reader taking the table at face value reads a measured negative where the review means a silent primary. This is a defect of the review, not of LEGEND, and no LEGEND record repeats it; it is recorded in `research/fulltext_dossiers/PMID42558002.md` and in the paper-registry Role field proposed by `CC-20261004W7-A-REGISTRY-01`.
- The narrative calls the organoid primary "iPSCs edited to carry a patient variant"; that paper used CRISPR-engineered human ES cells for the knockout and separately patient-derived iPSCs. The review's own Table 1 row is correct.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Every WWOX row is marked Unclear on the reactive-versus-cell-intrinsic axis, for the constitutive null | `Evidence of astrogliosis upregulation of cytokines TNF‐a and IL‐6 Unclear No seizures Wwox−/− mice 2 weeks old` | Table 1, Hussain 2019 row, `files/fulltext/PMID42558002_Lange2026_PMC.xml`)
- (…and for the P47T model, with the reason given | `Astrocyte reactivity, upregulation of pro‐inflammatory pathways Unclear, as age of seizure onset not reported` | Table 1, Hussain 2023 row, `files/fulltext/PMID42558002_Lange2026_PMC.xml`)
- (The cell-autonomy datum the review carries is a negative on three gross organismal measures | `Whilst Repudi et al. (2021) found WWOX to be expressed in astrocytes, they did not observe developmental delay, weight loss, or postnatal lethality in mice where WWOX was conditionally knocked out in astrocytes.` | Results, WWOX paragraph, `files/fulltext/PMID42558002_Lange2026_PMC.xml`)
- (The directional conclusion drawn from it | `indicating that changes in astrocyte phenotypes occur as a result of neuronal dysfunction and seizure activity` | Results, WWOX paragraph, final clause, `files/fulltext/PMID42558002_Lange2026_PMC.xml`)
- (The review's own conclusion is weaker than that direction | `Due to the complex and interdependent networks between glial cells and neurons, it can be difficult to establish the relative contribution of astrocytes.` | Conclusion, `files/fulltext/PMID42558002_Lange2026_PMC.xml`)
- (In the primary, the negative covers the oligodendrocyte and astrocyte knockouts and three gross measures | `either in oligodendrocytes (O-KO) or in astrocytes (G-KO) does not cause phenotypic abnormalities, such as developmental delay` | figure legend, `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt`)
- (…naming the three measures | `(P17), weight loss (K and N) and postnatal lethality (L and O) either in O-KO or in G-KO mice compared with their corresponding control group` | figure legend, `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt`)
