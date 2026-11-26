# Sentence for IT: card M01 tazemetostat exposure line (from ADV-293, HE, 2026-11-26)

Consumer: `disease-models/wwox/research/drug_repurposing/cards/M01_neurogenic_output_myc_window.card.json` line 543 and
`M01_neurogenic_output_myc_window.packet.json` line 436 (same sentence; any copy of it in view or shareable-package
renderings follows the card).

## Old sentence (exact, from the card)
Two other agents of the same batch, tazemetostat (an EZH2 inhibitor; the abstract of a mouse study says P-glycoprotein limits its brain accumulation, no brain concentration figure found by these routes; the abstract names the compound EPZ-6438 and the identity with tazemetostat is the sheet's; label: epithelioid sarcoma from age 16, follicular lymphoma in adults) and TMP195 (a class IIa HDAC inhibitor, no exposure found by these routes), have no card and are carried as open-question lines only.

## Proposed change (one clause)
Replace "no brain concentration figure found by these routes" with:
"no absolute brain or CSF concentration found by these routes; one measured ratio exists, brainstem TUMOUR (human DIPG
xenograft in mice), not brain parenchyma and not CSF: 3.74 percent of the serum concentration after systemic EPZ-6438
(abstract of PMID 32674144, read; the identity of EPZ-6438 with tazemetostat is the sheet's)".

Scope word to keep: TUMOUR tissue in a xenograft after intraperitoneal dosing. Nothing else in the card sentence changes
(P-glycoprotein statement, label from age 16, TMP195 clause).

## Why (HE verification)
The batch 10 sheet cited PMID 32674144 "title read only; what it showed about exposure is not read" and put the negative
"not found: a measured brain or CSF concentration of tazemetostat given alone" beside it. The blind reader (ADV-293, batch
10, unit U10.35) graded it MUST CHANGE from the delivered abstract; HE confirmed it against the abstract below (the
RESULTS sentence). ADV re-checked it against PubMed independently (Sasaki 2020, Neurosurgery, DOI 10.1093/neuros/nyaa301).
The sheet is corrected (commit cbc2013de). Class of error: negative sitting beside a citation the sheet read by title only.

## Whole source: PubMed record of PMID 32674144 as held (abstract, whole)
```
4. Neurosurgery. 2020 Nov 16;87(6):E680-E688. doi: 10.1093/neuros/nyaa301.

Convection-Enhanced Delivery of Enhancer of Zeste Homolog-2 (EZH2) Inhibitor for 
the Treatment of Diffuse Intrinsic Pontine Glioma.

Sasaki T(1), Katagi H(1), Goldman S(2), Becher OJ(2)(3), Hashizume R(1)(3).

Author information:
(1)Department of Neurological Surgery, Northwestern University Feinberg School 
of Medicine, Chicago, Illinois.
(2)Division of Hematology, Oncology and Stem Cell Transplantation in the 
Department of Pediatrics, Northwestern University Feinberg School of Medicine, 
Chicago, Illinois.
(3)Department of Biochemistry and Molecular Genetics, Northwestern University 
Feinberg School of Medicine, Chicago, Illinois.

BACKGROUND: Diffuse intrinsic pontine glioma (DIPG) is a fatal childhood brain 
tumor and the majority of patients die within 2 yr after initial diagnosis. 
Factors that contribute to the dismal prognosis of these patients include the 
infiltrative nature and anatomic location in an eloquent area of the brain, 
which precludes total surgical resection, and the presence of the blood-brain 
barrier (BBB), which reduces the distribution of systemically administered 
agents. Convection-enhanced delivery (CED) is a direct infusion technique to 
deliver therapeutic agents into a target site in the brain and able to deliver a 
high concentration drug to the infusion site without systemic toxicities.
OBJECTIVE: To assess the efficacy of enhancer of zeste homolog-2 (EZH2) 
inhibitor by CED against human DIPG xenograft models.
METHODS: The concentration of EZH2 inhibitor (EPZ-6438) in the brainstem tumor 
was evaluated by liquid chromatography-mass spectrometry (LC/MS). We treated 
mice-bearing human DIPG xenografts with EPZ-6438 using systemic 
(intraperitoneal) or CED administration. Intracranial tumor growth was monitored 
by bioluminescence image, and the therapeutic response was evaluated by animal 
survival.
RESULTS: LC/MS analysis showed that the concentration of EPZ-6438 in the 
brainstem tumor was 3.74% of serum concentration after systemic administration. 
CED of EPZ-6438 suppressed tumor growth and significantly extended animal 
survival when compared to systemic administration of EPZ-6438 (P = .0475).
CONCLUSION: Our results indicate that CED of an EZH2 inhibitor is a promising 
strategy to bypass the BBB and to increase the efficacy of an EZH2 inhibitor for 
the treatment of DIPG.

Copyright © 2020 by the Congress of Neurological Surgeons.

DOI: 10.1093/neuros/nyaa301
PMCID: PMC7666886
PMID: 32674144 [Indexed for MEDLINE]
```
