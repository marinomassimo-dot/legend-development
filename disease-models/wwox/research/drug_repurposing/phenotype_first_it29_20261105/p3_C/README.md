# IT29 P3-C: transfer conditions for the oligodendrocyte-differentiation endpoint

Non-canonical research material, not medical advice. Public edition (WWOX-DEE reference genotype class). Written 2026-11-05. No compound is listed here; the deliverable is the `transfer_conditions` / `transfer_breakers` content in `evidence_it29_C.tsv` (rows C01-C14), meant to be joined to every evidence row of the other Scientists. Repository rows are cited by id from `glia_maturation_it14_p4_20261101` (E-rows), not re-read.

## Decision (10 lines)

1. An external perturbation system is pertinent to WWOX-deficient developing brain only if the deficit arises in first-time postnatal myelination (mouse roughly P7-P21), not in a mature tract (C01-C03). Cuprizone, lysolecithin and EAE are repair models; the repository's own Olig2-Cre data show the lineage matters mainly under that kind of challenge (E24-E26, preprint).
2. The WWOX driver is upstream of the oligodendrocyte (E01-E08 neuron deletion reproduces, E10 lineage deletion does not, E13-E16 neuron add-back restores with the lineage still null). Most pro-differentiation screens use an intrinsic oligodendroglial defect or an intact system; they do not test the missing neuronal signal (C04).
3. Human imaging does not say "hypomyelination": in the WOREE mini-review atrophy (13 of 13 in one series) and callosal hypoplasia (12 of 13) dominate and delayed myelination is a minority (6 of 13), progressing on serial MRI (C11, E31). The endpoint must be stated as delayed myelination plus atrophy, not leukodystrophy.
4. Window: rodent pnd 1-3 is 23-32 weeks of human gestation, pnd 7 is 32-36 weeks, pnd 10 about term; mouse myelination peaks near pnd 20 (C12). The WWOX add-back window (P0-P5) is a late-gestation equivalent; no WWOX patient is treated there.
5. Functional rescues by a pro-differentiation drug exist (C05 Pdk1 icKO memory; C06 NL3 sensory behaviour; C07 early postnatal rescue of mossy-fibre development and attenuated adult seizure susceptibility; C08 neonatal injury, abstract only) but all come from oligodendrocyte-intrinsic, injury or seizure-free models.
6. Null: no source was found in which a pro-differentiation intervention improved conduction, motor, seizure or behaviour in a model where hypomyelination follows a neuronal defect and seizures are present (C14). Bounded search; not proof of no effect.
7. A DEE model with neuronal hyperexcitability (Scn2a gain of function) shows more myelin and slightly faster conduction (C09). Seizure activity alone therefore does not predict hypomyelination, which lowers the seizure-secondary reading of WWOX (IT14 P4 D1/D7) without ruling it out; different gene.
8. The sign can run the other way: an oligodendrocyte maturation block itself caused seizures and death (Myrf cKO, C07), and extra myelin of inhibitory axons protected against seizures in a preprint (C10). The arrow neuron to oligodendrocyte is not the only one.
9. Marker is not function: Pdk1 mutants had thinner but normally compacted myelin; Scn2a mutants had altered maturation transcripts with only slightly faster conduction and unchanged CC1 counts (C13). The WWOX comparison rests on fluorescence intensity and an Mbp transcript share, not conduction.
10. Consequence for the signed-coupling table: a hit read in an OPC screen should be admitted to the WWOX comparison only with the stage, driver, seizure status and readout level written beside it, using the conditions below.

## Transfer-conditions template (one line per external evidence row)

| Item | Pertinent if | Breaks the comparison if |
|---|---|---|
| Phase | primary developmental myelination, postnatal weeks 1-3 (mouse) | adult demyelination/remyelination or ageing |
| Driver | deficit follows a neuronal/axonal defect, or the intervention acts downstream of the neuron | defect is OPC-intrinsic, or the neuron is absent from the assay |
| Seizures | seizure-free system or seizure status reported | seizures, illness or survival loss co-vary with the intervention |
| Timing | treatment in the window matching add-back (late-gestation equivalent, P0-P7) | treatment after the myelination peak or in adults |
| Readout | EM compaction, g-ratio, conduction, behaviour | marker, transcript or immunofluorescence only |
| Attribution | target-specific control present | compound effect only (clemastine class shows an antimuscarinic mechanism in several sources) |
| Human endpoint | delayed myelination/callosal and atrophy components | assumes leukodystrophy-type hypomyelination |

## Evidence by theme

- Driver and seizure confound: C04, C09, C10 and the repository rows E01-E16, E09, E23.
- Functional pro-differentiation results: C05 (full text), C06 (partial text), C07 (abstract and introduction), C08 (abstract), C10 (preprint abstract).
- Human phenotype: C11. Window: C12. Readout level: C13. Null: C14.

## Not established

- Whether a pro-differentiation agent would act in the WWOX system when the missing signal is neuronal (D3/D4 of IT14 P4 remain partial).
- Whether the human myelination delay is primary or a consequence of atrophy and seizures.
- Direction of seizure effect on myelin in WWOX itself (D6, D7 absent).
- Case reports in C11 are read through a mini-review; the primary series were not read.

## Not reachable

- PubMed MCP search errored throughout; Europe PMC REST and NCBI efetch were used. The GABRD preprint and the neonatal hypoxia-ischaemia paper were read at abstract level only; C07 was read at abstract and introduction only.
- Closed WOREE series (Seizure 2026 case series; PMID 42721537) is not open text. Searches for classical Pelizaeus-Merzbacher or hypomyelinating-leukodystrophy rescue studies returned reviews and one integrated-stress-response study (PMC12868624) that was not read; reopen with those model names plus conduction velocity.

## Receipts

Eight draft receipts in `receipts/` (event-id suffix -06), none recorded. Depths: full or partial text for 41980417, 40640134, PMC13651182 (Acta Neuropathol Commun, no PMID found), 38161429, 23583307; introduction only 40673958; abstract only 40058153 and the Research Square preprint 10.21203/rs.3.rs-10024120/v1.
