FIRST READER REPORT, ADV-295 block 1, record 3: PMID 42401046 (Helton, Rodgers, Gupta 2026, Biomed Pharmacother). Consumer: DL-THER-089 clause (ii) and the divergence sentence. Run date 2026-11-26.

Source abbreviations used below:
- XML = /home/desktop/legend-development/files/fulltext/PMID42401046_Helton2026_PMC_r2.xml
- FIG = /home/desktop/legend-development/files/figures/PMID42401046_r2/ (f0001..f0006 = Fig 1..6; NIHMS2199027-supplement-MMC1..4 = Supp Fig 1..4, per the Results citations)
- PDF = /home/desktop/legend-development/files/supplement/PMID42401046_r2/PMC13479836.1.pdf

Abbreviations for the models: IHK = intrahippocampal kainate, IHS = intrahippocampal saline, IPK = intraperitoneal kainate, IPS = intraperitoneal saline, Veh = vehicle, SB = SB415286, EZ = ipsilateral epileptogenic zone, PIZ = contralateral.

Marking convention:
- "(eye)" = a value or bracket read by eye from a figure. No source data are held.
- Every other statistic is quoted from the text or caption.

## 0. Design facts used throughout (XML Methods and Results; Fig 2)

- **Animals.** Adult mice, "8–10-week-old wild-type C57Bl6/J ... and ... POMC-eGFP". Males and females 1:1, pooled.
- **Replicate unit.** "For each experiment, n per group was 6" (Methods 2.8). In Fig 3C–E, 4B–D, 5B/D, 6B and Supp Fig 4 each dot is one mouse; I counted 6 dots per group (eye). Dendrite angles are shown as cumulative distributions of single cells, tested by Kolmogorov-Smirnov. The number of cells is not stated.
- **Unilateral model (IHK).** 100 nl kainate (2 mg/ml, 0.2 µg) into CA3, one side. Comparison hemispheres: ipsilateral (EZ) and contralateral (PIZ).
- **Bilateral model (IPK).** Systemic repeated low-dose intraperitoneal kainate (10 mg/kg, then 5 mg/kg every 30 min until convulsive SE). It is not a bilateral intrahippocampal injection. Both hemispheres were averaged; Supp Fig 4 shows no left/right difference.
- **Drug.** SB415286, "Canonical Wnt activator", "anilinomaleimide GSK3b inhibitor". Given at "10 mg/kg/day IP", daily from 24 h after kainate until euthanasia. Fig 2A/B timeline: histology at day 14. Results: "2-weeks after".
- **Endpoints.** Four histological markers (Methods 2.7): granule-cell-layer width (dispersion), POMC-GFP+ cell migration, POMC-GFP+ cell count per mm³, primary dendrite angle. Plus Axin2 intensity as the Wnt read-out.

## 1. Statement table

| id | verbatim statement | verdict | grounds |
|---|---|---|---|
| R3-S01 | "(`NOT WWOX EVIDENCE`)" | CORRECT | Search 2026-11-26, XML text and PDF text, query "WWOX": 0 hits in each. |
| R3-S02 | "a GSK3 inhibitor used as a Wnt **activator**" | CORRECT | Results: "SB415286 is a highly selective CNS-penetrant anilinomaleimide GSK3b inhibitor with established beta-catenin activating properties". Methods 2.5: "Canonical Wnt activator SB415286". Fig 1C: Axin2 5 ± 0.94-fold at 3 h and 7 ± 1.25-fold at 24 h after a single dose, p < 0.01 (Fig 1 caption and Results). Note: the paper itself says GSK3 inhibitors "can also have alternate pathway effects [72,73]" (Discussion). Axin2 immunofluorescence is the only Wnt read-out. The paper uses the term, but Wnt-specificity of the histological effect is not shown. |
| R3-S03 | "in **adult** temporal-lobe epilepsy" | ADD | "Adult" refers to 8–10-week-old mice in kainate models (Methods 2.1). A reader can take it as adult patients. Needs: species mouse, kainate-induced models, strain, sexes pooled. |
| R3-S04 | "reduced granule-cell dispersion, immature-cell migration ... in the unilateral model" | ADD | Fig 3C ipsilateral: dispersion IHK+SB vs IHK+Veh, p < 0.01. Fig 3D ipsilateral: migration, p < 0.001. Unit: mouse, n = 6 per group. Text: "There were no changes in immature dentate granule cell dispersion or migration after IHK in the contralateral dentate gyrus (Figs. 3C, 3D)". Sentence needs "ipsilateral". Reduction is partial (eye): dispersion about 147 → 112 µm (IHS about 61 µm; IHK+SB spread 68–160, 3 of 6 animals ≥110); migration about 58 → 29 µm (IHS about 15 µm). |
| R3-S05 | "and the contralateral cell-count increase" | CORRECT | Fig 3E contralateral: IHK+Veh vs IHS, p < 0.0001. SB reduced it, p < 0.05. IHK+SB vs IHS shown "ns" (eye, bracket). Values (eye): about 200k vs 142k vs 100k cells/mm³. The paper calls it "proliferation" and "neurogenesis", but the measure is POMC-GFP+ cell density. Searches 2026-11-26 on the XML body, one keyword each ("BrdU", "Ki67", "Ki-67"): 0 hits. |
| R3-S06 | "(the ipsilateral count unchanged)" | ADD | Fig 3E caption: "IHK caused significant granule cell loss in the ipsilateral dentate gyrus compared to saline controls; this was unaffected by SB415286 treatment". IHK itself cut the ipsilateral count about 10-fold (eye: about 12k vs about 115k/mm³, p < 0.0001). SB: ns (eye: about 37k vs 12k, one animal at about 100k). The sentence reads as if there was no IHK effect on the ipsilateral count. |
| R3-S07 | the unilateral enumeration "dispersion, immature-cell migration and the contralateral cell-count increase" (the dendrite angle is omitted for the unilateral model) | INCOMPLETE | Results: "pathological proximal dendrite angulation was prevented (p < 0.01)". Fig 3F ipsilateral: IHK+Veh vs IHK+SB, ** (eye bracket). Fig 3G contralateral: *** (eye bracket). So all four markers are reduced in the unilateral model. The clause names only the bilateral model's dendrite change, which suggests it is the discriminator when it was not. |
| R3-S08 | "while in the bilateral model **only the primary dendrite angle** changed" | ADD | Fig 4B–D: SB had "no effect on granule cell layer dispersion, granule cell migration and granule cell count after IPK or IPS" (Results). Fig 4E: angle reduced. Only the dendrite angle changed, and only under drug. Four points must be added. (a) IPK itself did not change dispersion (Fig 4B ns), so there was nothing to reduce. Of the three markers IPK altered (migration p < 0.01, count p < 0.01, angle), SB moved 1 of 3. (b) Axin2 also changed (Fig 6B). (c) The angle result rests on K-S tests of pooled single cells; the other markers use n = 6 mice. (d) Fig 4E brackets (eye): IPK+Veh vs IPS-pair ****, IPK+SB vs IPS-pair *, IPS+Veh vs IPS+SB ns. No explicit IPK+Veh vs IPK+SB p value in text or caption. IPK+SB therefore still differs from IPS, so "prevented" is partial (eye). |
| R3-S09 | "so **Wnt direction in neural tissue is model-dependent**" | WRONG | Helton shows the same direction in both models. Axin2 falls below baseline in the epileptogenic zone: Fig 5B ipsilateral (eye: IHK+Veh about −7, IHS about 15) and Fig 6B IPK (eye: about 5 vs 17). SB restores it, and Wnt activation protects dendrite angle in both models (Discussion: "Our data further highlight a shared therapeutic mechanism for Wnt signaling augmentation across both models of TLE"). What differs is the breadth of marker response (unilateral 4/4, bilateral 1 of 3 altered) and the contralateral Axin2 (unchanged after IHK, Fig 5D ns). That is a difference of effect breadth, not of direction. The models also differ in route (focal vs systemic kainate) and in neuron loss and dispersion. The inference may rest on clause (i), which I was not given; as an inference from Helton's two-model contrast it is unsupported. "Neural tissue" overgeneralises dentate immature granule cells of mouse. |
| R3-S10 | "That study is **histology and immunohistochemistry at day 14 only**" | ADD | For the epilepsy models: Fig 2A/B and Fig 3–6 are histology/IHC at day 14. Exact euthanasia day is not stated in words beyond "2-weeks"; Fig 2 shows 14. But Fig 1 is Axin2 IHC at 3 h and 24 h after one dose, in mice not described as kainate-treated. Supp Fig 1 (MMC1) is daily body weight to day 14. Behavioural SE scoring covers the first 2 h. "Only" is absolute and false if read over the whole paper. The sentence is true of the model outcomes. |
| R3-S11 | "at **one dose level**" | CORRECT | Methods 2.5: "SB415286 was dosed at 10 mg/kg/day IP". Search 2026-11-26, XML text and PDF text, query "concentration": 0 hits each. Query "dose-response": 0 hits. The Fig 1 single-dose amount is not stated in the text ("a single intraperitoneal dose"). No dose series and no second dose. Also one vehicle, one regimen, one kainate dose in IHK. |
| R3-S12 | "in **adult mice**" | CORRECT | Methods 2.1: "8–10-week-old". Sexes pooled 1:1; n = 6 per group; no sex-split. |
| R3-S13 | "there is **no EEG and no spontaneous-seizure or seizure-burden endpoint**" | CORRECT | Searches 2026-11-26, XML text, one keyword each: "EEG" 3 hits, all reference titles (video-EEG telemetry, video-EEG monitorings, one more title). "electroenceph" 4 hits, all reference titles. "electrophys" 2 hits, none in body. "telemetry" 1 hit, reference title. "electrograph" 4 hits in the body: Intro and Discussion about other studies (refs 25, 26) and future work. "spontaneous" 1 body hit, a background claim: "spontaneous recurrent seizures are known to develop within 2 weeks". "burden" 2 body hits: Intro on the earlier Chir99021 paper, and the future-work sentence below. PDF text gives the same counts. Methods describe no electrode implantation, recording or seizure follow-up. Discussion: "These histological findings will need to be complemented with functional studies that determine how Wnt activation during epileptogenesis in these TLE models affects electrographic and behavioral seizure burden." Supp Fig 1–4 viewed in full by eye: body weight, dendrite tracings, Axin2 per hemisphere; no seizure or EEG data. |
| R3-S14 | "seizures were scored behaviourally for two hours at induction, only to define status epilepticus" | CORRECT | Methods 2.4: "scored behaviorally for 2-hours after completion of surgery in the IHK model and after initiation of injections in the IPK model by modified Racine scale ... Mice were included in the epilepsy group if they demonstrated convulsive status epilepticus, defined as continuous Racine 3–6 seizures for at least 30 min". Searches, one keyword each: "Racine" 2 body hits; "seizure score" 0 hits; "latency" 0 hits. No score is reported as a result. Minor add: in IPK the scoring also decides when kainate redosing stops. The number of mice failing SE criteria is not reported (search "exclu": 0 hits). |
| R3-S15 | "the candidate counted *'two of four'* remodelling markers in the unilateral model and *'one of five'* concentrations in (a)" | NOT ASSESSABLE | This is the candidate's wording, not held; "(a)" is not this paper. |
| R3-S16 | "the audited entries carry **three of four** markers in the unilateral model" | INCOMPLETE | The count depends on hemisphere (all comparisons SB vs Veh within IHK). Ipsilateral: dispersion, migration, angle reduced; count ns = 3/4. Contralateral: count and angle reduced; dispersion and migration unchanged by IHK itself = 2/4. Either hemisphere: 4/4. Across the 8 marker×hemisphere cells: IHK altered 6 (dispersion, migration, count ×2, angle ×2); SB attenuated 5 of those 6. The sentence's own list names three markers and omits the angle (R3-S07). Observation by derivation, not a source claim: the candidate's "two of four" equals the contralateral tally and the audited "three of four" equals the ipsilateral tally. |
| R3-S17 | "name **four** concentrations" | NOT ASSESSABLE for this record | It does not rest on Helton, which has no concentration series (see R3-S11 searches). If it is ever attributed to Helton it is WRONG. |

## 2. Corrected sentences

- **R3-S03:** "a GSK3 inhibitor (SB415286) used as a Wnt activator in two mouse kainate models of temporal-lobe epilepsy (8–10-week-old C57BL/6J and POMC-GFP mice, sexes pooled, n = 6 mice per group)".
- **R3-S04 and R3-S07:** "reduced ipsilateral granule-cell-layer dispersion and immature-cell migration, the contralateral immature-cell count increase, and the primary dendrite angle shift in both hemispheres, in the unilateral intrahippocampal-kainate model (partial reductions, day 14, versus vehicle)".
- **R3-S06:** "the ipsilateral immature-cell count, which kainate had reduced about 10-fold (by eye), was not restored".
- **R3-S08:** "in the systemic intraperitoneal-kainate model, which has no granule-cell-layer dispersion, the drug left migration and count unchanged and changed only the primary dendrite angle (a K-S test on pooled cells; the angle stayed different from saline controls by eye)".
- **R3-S09 (WRONG):** "Helton shows the same direction in both models (Axin2 down in the epileptogenic zone, restored by the GSK3 inhibitor, remodelling reduced); what differs is how many markers respond. Any claim that Wnt direction is model-dependent needs a different source".
- **R3-S10:** "the epilepsy-model outcomes are histology and immunohistochemistry at day 14 only (plus a 3 h and 24 h Axin2 check after a single dose, and daily body weight)".
- **R3-S16:** "four of four markers in the unilateral model, three of four ipsilaterally and two of four contralaterally".

## 3. Strict candidates (verifier side only; SCI to check on the original; the blind reader has not been consulted)

- **R3-S09** is the only statement I judge WRONG as written. It rests on the inference not being supplied by clause (i).
- **Borderline, not strict:** R3-S10 (absolute "only") and R3-S16 (hemisphere-dependent count). Both are ADD or INCOMPLETE.

## 4. ADDs no consumer holds but that matter

- Magnitudes are partial (eye): about 41% of the dispersion excess removed ((147−112)/(147−61)), about 67% for migration, about 58% for contralateral count. Authors' word is "rescued/prevented".
- Fig 3G contralateral angle: IHK+SB vs IHS+Veh still * (eye), so not fully normalised.
- The dendrite-angle significance in both models uses single cells as the unit, while every other histology panel uses n = 6 mice.
- Fig 1C vs text: eye bar heights give about 4.7× at 3 h and about 5.1× at 24 h against the same-time vehicle bar (about 6.0× against the 3 h bar), not the stated 7. The Fig 1C bars carry no n, no dots and no legend. The 3 h and 24 h bars are only inferred.
- Supp Fig 1: weights run to day 14. IHK+SB stars at days 8, 10, 11, 13 and 14 (eye). The legend is not held, so the comparison is not assessable.

## 5. What I opened, could not read, and failures

**Opened and read in full:**
- XML: the whole file, text-stripped, including all 74 references and the figure captions.
- Fig 1–6 JPGs, plus zooms of Fig 3C–G and 4E made with ImageMagick.
- MMC1–4 JPGs.
- PDF: 26 pages. Text extracted. Pages 18–26 viewed as a 40 dpi montage and found to be the figure pages, same figures as the JPGs. The PDF holds no separate supplement pages.
- Consumer text for record 3, and the "Matching rule" section of the PREREG.

**Disclosure:** the Read tool loaded the whole consumer file, so I also saw the consumer text of Records 4 and 5. I did not use it.

**Not read or not held:**
- Supplement legends (the MMC files are images without captions).
- Source data.
- The Fig 1 dose and n.

**Failures and limits:**
- Python PIL and matplotlib are missing; I used ImageMagick convert/montage for crops.
- pdfinfo printed "Syntax Error: Can't revert non decrypt streams"; text extraction was unaffected.
- No files were written in the repository, no network was used, no e-mail address was used, and I did not touch PMID 42422765.
- All figure bracket assignments are by eye. In particular, Fig 3C's "****" bracket and Fig 4E's brackets are ambiguous in which pair they join.
