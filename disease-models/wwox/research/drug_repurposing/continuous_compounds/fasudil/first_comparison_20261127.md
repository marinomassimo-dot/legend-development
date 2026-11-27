# Fasudil, opening comparison for the WWOX programme

The closure sources confirm that the coculture and explant endpoints used Y0503. They also separate CSF analyte, kinase potency and developmental engagement. [Completed comparison and disposition](rock_engagement_and_disposition_20261127.md)

| Preparation | Opening observation | Transfer limit |
|---|---|---|
| Rodent oligodendrocyte precursor model, ROCK substrate | The public caption reports a fasudil effect on MYPT1 phosphorylation at nominal 100 µM in the model. The paper also uses another ROCK inhibitor in the myelination experiments. | Assign MYPT1, lineage markers and actual sheath endpoints to their own compounds, concentrations and experimental units before transferring an effect to fasudil. [Primary study record and Figure 1 caption](https://pubmed.ncbi.nlm.nih.gov/25289646/) |
| Conditional mouse RhoA loss in the oligodendroglial lineage | The authors report faster differentiation and myelination with changes in cortical and membrane tension. | Loss of RhoA is a pathway perturbation. It cannot identify fasudil potency or establish a defect in WWOX axons. [Primary study abstract](https://pubmed.ncbi.nlm.nih.gov/39495111/) |
| Adult ALS trial of intravenous fasudil, sampled lumbar CSF | In two treated arms the published hydroxyfasudil means were 5.8 and 9.4 µg/L. | The measured species is the metabolite, with no direct equivalence to nominal parent bath concentration or target engagement in developing WWOX cells. Sampling denominators, timing and analytical limits are part of the next targeted audit. [Adult trial and source for the exposure values](https://pmc.ncbi.nlm.nih.gov/articles/PMC12741558/) |
| WWOX neuronal deletion and laboratory analysis of axonal denominators | Neuronal WWOX loss is sufficient for myelin and circuit phenotypes in mice. The held comparison follows all eligible axons and tests propagation separately from marker changes. | Adult demyelination or a newly differentiated oligodendrocyte does not resolve first-sheath formation in juvenile WWOX. [Primary WWOX study](https://pubmed.ncbi.nlm.nih.gov/33914858/) · [Held quantitative denominator](../clemastine/axonal_denominator.md) |

**Replay the exposure scale.** For hydroxyfasudil with a mass of 307.37 g/mol, nM = µg/L × 1,000 / 307.37. The two published mean CSF values convert to 18.87 and 30.58 nM. These values provide a human metabolite concentration scale. They cannot be divided by the parent assay dose to estimate an efficacy margin. [PubChem chemical identity and mass](https://pubchem.ncbi.nlm.nih.gov/compound/3064778) · [ROCK-ALS](https://pmc.ncbi.nlm.nih.gov/articles/PMC12741558/)

```sh
python3 -c 'print(*(round(x * 1000 / 307.37, 2) for x in (5.8, 9.4)))'
# 18.87 30.58
```

**Opening checkpoint.** The initial comparison registered the parent–metabolite and developmental first-sheath questions. [Registered prediction](pretest_20261127.md) · [Completed decision and replay](rock_engagement_and_disposition_20261127.md)
