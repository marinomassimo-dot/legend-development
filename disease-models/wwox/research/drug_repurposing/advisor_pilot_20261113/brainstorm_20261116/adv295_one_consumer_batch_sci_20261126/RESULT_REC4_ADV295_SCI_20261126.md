# ADV-295 block 1, record 4: result after the blind step (SCI, window 8fe7aef9, 2026-11-26; hypothesis level; not medical advice)

Record 39546604 (Tiwari 2024, Sci Adv 10:eadp7423), consumer RP-033, the two blocks of `next_action` that name the paper (04:19:29Z and 04:23:08Z), extracted by script into `CONSUMER_TEXT_REC3_5_ADV295_SCI_20261126.md`. PREREG `dc88c85b4f3ab51751c123a0a6f775eb00199cfef1b5c5cb918acd443bb41d6c`. First reader: legend-delegate, claude-sonnet-5-5, effort high on 30 of 30 turns; report verbatim in `FIRST_READER_REPORT_REC4_ADV295_SCI_20261126.md` (sha256 3867170b45d4cb7ae50c42f6d35644fe335b34ab613600163f8decd80812121b). Blind reader: legend-delegate, sonnet, effort high on 18 of 18 turns, given the Matching rule and `BLIND_PACKET_REC4_ADV295_SCI_20261126.md` (sha256 99b5c7b748fbc6c133c16c91fe1c3ab5b5fc97cc5dba4014f9508b7b22c2f6d1) only; report verbatim in `BLIND_READER_REPORT_REC4_ADV295_SCI_20261126.md` (sha256 7d6ae2e80f9a1a3f2f1261f482e29b906ebc125a784ce5cda15a49f299d209e6). Class read: Discussion, Methods, all five main figures, all nine supplement pages (figures read by the delegates; values by eye are marked in their reports).

## Strict (rule applied as written): 1 sentence, already superseded inside the row

* **"matrix pyruvate sensor in mouse neurons and HEK cells"**: first reader WRONG, blind MUST CHANGE. SCI check on the original: Methods, "Primary neuronal cultures", "Hippocampi were dissected from 1- to 3-day old (mixed sex) Sprague-Dawley rat pups"; the shRNA target is a rat sequence; mouse tissue appears only for the 13C3-pyruvate infusion (Fig 1), the Sirt3-/- brain immunoprecipitation (Fig 4D,E) and mouse MPC1 cDNA. **The same field already says**, in the 04:23:08Z block, "The Tiwari preparation is rat culture (neurons and axons) plus HEK, not mouse (ADV's earlier wording in report 30 corrected)". So the defect is real as written but the field's reading was already repaired: it changes no decision-bearing sentence, it removes a contradiction inside the row. The first reader's added scope (rat for the sensor experiments; mouse only for three other uses; the Fig 2E-G legend does not name hippocampal or cortical) is the only residual ADD.

## Listed apart (two readers differ on the same sentence; not counted)

* **"and the sensor and ATP readouts were never in the same cultures"**: first reader WRONG (unsupported as written), blind UNSETTLED. Both ran the same searches on the held text (2026-11-26; "same neuron", "simultan", "co-express", "same culture": 0 hits); Table S3 lists "3 (cultures)" for the sensor row (Fig 2F,G) and for the ATP row (Fig 2H,I) without culture identity; the Fig 2H legend and drawing show both reporters in one terminal, as a schematic; no paired per-culture measurement is shown. Wording that is true under both readings: "the paper does not state whether the sensor datasets (Fig 2F,G) and the ATP datasets (Fig 2I,J) came from the same cultures; both list 3 cultures (Table S3); no paired measurement is shown". The conclusion drawn from the clause ("whether it separates entry from PDH regulation is untested in it") stands without it: both readers verified the negative "never tests the sensor against a PDH, PDK or consumption perturbation" by one-keyword searches (PDK, DCA, dichloroacetate, oligomycin, FCCP, rotenone, antimycin, efflux: 0 hits in the XML and the supplement text).

## ADD (loose)

First reader only (the blind reader returned NO CHANGE or no ADD, so none is counted as matched): "(a stock, not a rate)" needs the label and the lack of calibration ("the paper itself calls this peak 'mitochondrial pyruvate uptake'; no calibration, slope or rate is analysed"); "validates the sensor for ENTRY only" needs the HEK additions (Sirt3 KD partial response, WT versus QQ MPC1 rescue); "MPC1 knockdown abolishes the axonal response" is true of the group mean (Table S3: 0.68 ± 0.10, 21 neurons, against 0.06 ± 0.08, 12 neurons; unit the neuron; 3 cultures given once for the row), two knockdown neurons reach about 0.65 by eye; "a response to a RISE in pool was never shown" is ambiguous as written.

## Held correct (both readers)

Peak at a 10 mM external step (Fig 2G "peak ΔF/F0"); pH correction only for the cyto-pHluorin-corrected ATP measurement; PDH only as Discussion background (one body occurrence, ref 66); "21 against 12 neurons" (Table S3; the Fig 2 legend says "n = 12 to 18" and disagrees); the parental sensor paper is ref 23, Arce-Molina 2020, PMID 32142409.

## Counts, record 4

Strict 1 (rule as written; superseded in the row: not decision-bearing). Listed apart 1. Loose 1 (strict). ADD matched by both readers: 0; ADD from the first reader only: 4.

## Limits

Source data and the Dryad archive are not held; the Fig 2G dots are overplotted at 731 px, so the caption's n (12 to 18) against Table S3 (21 and 12) cannot be settled by counting dots; the parental dynamic range is not in the held set.
