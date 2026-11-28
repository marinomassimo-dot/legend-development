# ADV-339 part 1 — first six exclusivity sentences (IT41, 2026-11-28)

Hypothesis level; nothing here is medical advice. Rule, order and bands: `PREREG_ADV339.md` (frozen in commit `4c8533c10` before any source). Net: `enumerate_adv339.py` (233 candidate sentences in 42 claims, lexical markers; unmarked exclusivity is missed). An enumerating delegate (sonnet, medium, no source opened) counted about 49 sentences as exclusivity (about 35 with a complete-read source at PMID level); S1-S6 are the first six in claim order that it listed with a complete-read source. CLAIM 003 sentences repaired by `BATCH_20261128_011` were excluded; CLAIM 002 (P = 0.7681, "only in WSM") and CLAIM 005 (NPY, DG only) were skipped as already judged by ADV-082 to ADV-084.

## Readers
* **First reader** (sonnet, medium): had the article texts but NOT the figure images of PMID 34747138, its Appendix, or the Steinberg figure pages (they sat in `files/figures` and `files/supplement`, not beside the text files: my packet was incomplete, not the corpus). Result: HOLDS 2 (S5, S6), not holding 1 (S1), UNSETTLED 3 (S2, S3, S4); 35 atoms: 23 supported, 2 not, 10 unsettled.
* **Second reader** (sonnet, high, blind to the first, full source list incl. the PDF with Figure 5): HOLDS 2 (S3, S6), TOO_NARROW 4 (S1, S2, S4, S5); 44 atoms: 39 supported, 4 not, 1 unsettled.

## Per sentence (my adjudication, labelled as mine, not a third blind reading)
| S | Claim | Sentence gives | Both readers | Adjudicated |
|---|---|---|---|---|
| S1 | 003 | O-KO arm = weight/survival ~120 d, one clasping image, one anti-MBP at P17; no EM, g-ratio, axon count, CC1/OPC count, ephys, "no age after P17" | assay exclusions hold (both); "no age after P17" false: clasping and CC1/WWOX validation are P18, survival runs to ~120 d (both). Weight is shown to P16 only (Fig 1K): the sentence's "up to ~120 d" is true for survival only | **not holding on the age atom; content exclusions hold** |
| S2 | 003 | the only oligodendrocyte-lineage datum is external (Fig 3B, fetal 16 pcw), WWOX max in radial glia, min tied in Oli and Mic ~0.08 | first: unsettled (Fig 6D/E not opened); second: holds for WWOX-by-lineage, fails on the literal "any oligodendrocyte-lineage datum" (organoid clusters 9/10 in Suppl Fig 3C are enriched for OPC/microglia markers; Fig 6D,E pathways) | **reading-dependent**: holds as a WWOX-expression-by-lineage statement (the colon says so), too narrow if "dato" is read literally |
| S3 | 004 | untested against WT: axons/field, CC1, PDGFRa; brackets WT-KO and KO-rescued only | first: unsettled (figure not held); second: HOLDS, Fig 4C and 5B/5H brackets read at 400 dpi; the WT-vs-rescued tests that exist (6 months, Fig 5E unmyelinated axons and 5F g-ratio) are other endpoints | **holds** |
| S4 | 004 | every behavioural endpoint compared with WT only; adult recordings only in treated animals | first: unsettled (Appendix not held); second: TOO_NARROW, minor: Appendix Fig S3A shows an untreated KO clasping image beside WT (qualitative) | **reading-dependent**: holds for quantified endpoints, too narrow if a qualitative image counts |
| S5 | 005 | GABAergic and glial signal in hippocampus, systemic BK5-Cre KO, 2 weeks, one study | first: holds; second: another study (Repudi 2021 EMBO Mol Med Fig 3E-G) has GFAP/Iba1 increases in CA3 of the systemic null at P19 | **arm, region and age exclusions hold; "in a single study" is a literature count** (outside the PREREG rule) and is wrong for the glial half, at a different age and in a different allele |
| S6 | 005 | O-KO n = 11/10, P = 1.0; no astrocyte function, seizure or network measurement | both: holds; the "review's own sentence" clause cannot be checked (the review is not a source) | **holds** (checkable part) |

## Rate, with denominators (PREREG bands: E1 under 10 percent, E2 30 percent or more of checked sentences not holding)
* Second reader's strict reading: **4 of 6 sentences** not holding (67 percent); **4 of 44 atoms** (9 percent).
* My adjudication: **1 of 6 firm** (S1, an age atom; 17 percent), **2 of 6 reading-dependent** (S2, S4), **1 of 6 outside the rule's scope for its failing atom** (S5), 2 of 6 holds (S3, S6). Range **17 to 67 percent of sentences**: not E1, and not settled E2.
* The stopping observation (all six hold) is **not met**: the pattern does not close.
* Where the sentences fail, the failing atom is usually an **ancillary exclusion** (age, "single study", "every endpoint"), not the arm assignment; the arm assignments (O-KO has no EM, WT-vs-KO brackets only, BK5-Cre hippocampus) held in every sentence the sources could test.

## What the first-reader failure teaches
Three of six sentences stayed UNSETTLED for one reader and were decided by the other because the figure images and the Appendix were held in other folders. A packet built from the text file alone turns a held source into "not held". Search `files/figures`, `files/supplement` and `figure_renders` by PMID before dispatch.

## Proposed wording repairs (dated pointer; a BATCH_COMMIT only after part 2, if a decision changes)
* S1 (CLAIM 003, line of `CC-20261003R-OKO-STRENGTH-01`): replace "nessuna età successiva a P17" by "nessuna lettura istologica o funzionale oltre P17-P18 (la sopravvivenza arriva a circa 120 giorni; il peso è mostrato fino a P16)".
* S2 (CLAIM 003): "L'unico dato di lignaggio oligodendrocitario" to "L'unico dato di espressione di WWOX per lignaggio oligodendrocitario".
* S4 (CLAIM 004 wave note): add "(an untreated KO clasping image sits beside WT in Appendix Fig S3A; no quantified null behaviour)".
* S5 (CLAIM 005): "in un solo studio" to "in un solo studio per il segnale GABAergico; il segnale gliale ha un secondo studio a P19 (PMID 34747138, Fig 3E-G)".
No RP premise changes on these six (the S-KO/N-KO/O-KO attribution is untouched).

## Limits
Values in S2 and S3 are read from boxplots and bars. The mp4 files were not opened. Fig EV1F of 34747138 is not held. S6's review clause is unchecked. The enumerator's "counted" list is one delegate's sentence reading; its borderline list (#20, #22, #24, #32, #39, #82-#84, #86, #120, #160, #228, #229) was not examined.
