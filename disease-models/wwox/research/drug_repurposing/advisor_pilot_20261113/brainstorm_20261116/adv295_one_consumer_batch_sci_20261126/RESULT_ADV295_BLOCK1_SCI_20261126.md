# ADV-295 block 1: result (SCI, windows c6d4dd83 and 8fe7aef9, 2026-11-26; hypothesis level; not medical advice)

PREREG `dc88c85b4f3ab51751c123a0a6f775eb00199cfef1b5c5cb918acd443bb41d6c` (unchanged, one matching rule). Per-record results: `FIRST_READING_RESULT_REC1_2_ADV295_SCI_20261126.md`, `RESULT_REC1_2_ADV295_SCI_20261126.md`, `RESULT_REC3_ADV295_SCI_20261126.md`, `RESULT_REC4_ADV295_SCI_20261126.md`, and record 5 below. Every first-reader and blind-reader report is in this folder verbatim (the longest SubagentHandback input of each transcript). Every delegate: legend-delegate, claude-sonnet-5-5, effort high, read back from its own transcript on every turn (5 first readers, 5 blind readers; one delegate at a time; figures read by delegates, none in SCI's context).

## Record 5: 41210171 (Vono 2025), consumer DL-METH-118 (lines 3710 to 3731)

First reader (report sha256 ca80bbe90d459567fa475a10b6c093d7b6dab3f3f7169236f68f2e87b6ca0b74): 15 units, no WRONG; 9 ADD, 4 CORRECT, 1 NOT ASSESSABLE; three borderline sentences. Blind reader (packet sha256 ea825f25db2dcce9dfd4a0b0f390f4770408d217f9988b92e56b14f488880e45; report sha256 13da94ec64623ccbdb36cab1b4f0fead7725cfe2d5f4ee9993a8a6bc398ccf20): one MUST CHANGE, four ADD.

* **Not strict (one of the two conditions only; listed apart): "the absence is DRG-specific, not article-wide".** The first reader judged it ADD ("every tissue except brain"), the blind reader MUST CHANGE (lowest consequence): both state the same fact, the incidence table (Fig 6C, brain only; two brain rows) is the only one, and the absence covers injection site, spinal cord, cauda equina and roots, and DRG, with heart named only in the Discussion. They differ on the label. Wording true under both: "incidence and severity are tabulated for brain only; the absence of tabulated incidence applies to every non-brain site the text lists as affected, DRG among them".
* **ADD (loose), both readers:** the meningeal count needs its context (Fig 6C, female cynomolgus, unit the animal: vehicle 2 of 3, both minimal; treated 12 of 12 = 8 minimal, 3 slight, 1 moderate; perivascular 0 of 3 against 3 of 12) and the stated basis of the "test-article-related" class (higher incidence, a severity trend in the high-titre group); the pooled severity range is not DRG-specific; the four sectioned DRG levels do not show that DRG was graded per animal; "independent of pre-existing titre" rests on a Fig 6A legend, with no DRG incidence by titre group (n = 4 per group, overlapping low and medium bands), a brain-infiltrate trend with titre, and lower DRG vector load in high-titre animals (text; Fig 2 not held); the concurrent-control incidence in Vono is brain only, not DRG.
* **Held correct (both):** DRG lesions are described in prose keyed to a representative photomicrograph (Fig 6A, one group-3 animal) with no incidence and no control comparison for that tissue; the methods list DRG at four levels as sectioned and stained; vehicle n = 3; WWOX absent (0 hits, 2026-11-26).
* Unread by necessity: Figures 1 to 5 are not held as images (file names and PDF text searched, 707 of 714 PDFs under `files/`, 2026-11-26); the Fig 6A and 6B histology images are not gradeable at 759 px; the Fig 6C numbers are read from a render.
* Counts: strict 0; listed apart 1; loose 0 (no strict); ADD matched by both readers 5 sentences.

## Block 1 totals (records, not sentences)

| record | consumer | strict | listed apart | ADD (both readers) | changes a decision-bearing sentence |
|---|---|---|---|---|---|
| 42807679 | CLAIM 032 | 0 | 1 (exome sentence: first reader strict, blind ADD) | 2 | no |
| 41254692 | DL-REPO-003 | **1** (two sentences: a misquoted «potentially increase»; "species unknown" against Homo sapiens in Table S7) | 0 | 1 | no (low in substance) |
| 42401046 | DL-THER-089 | **1** ("Wnt direction in neural tissue is model-dependent") | 0 | 2 | **yes** (a stated BLOCK-1 reason) |
| 39546604 | RP-033 | **1** ("mouse neurons", rat) | 1 ("never in the same cultures": first reader WRONG, blind UNSETTLED) | 0 | no (the row already corrects the species) |
| 41210171 | DL-METH-118 | 0 | 1 ("DRG-specific": first ADD, blind MUST CHANGE) | 5 | no |

* **Strict records: 3 of 5.** PREREG prediction 2 of 5 (range 0 to 3): inside the range, above the point estimate. The rejecting observation (0 strict) is not met; by ADV's rule (2 or more strict) block 2 would be five records.
* **Strict records that change a decision-bearing sentence: 1 of 5** (42401046). The other two strict records are a form-only misquote and an unreferenced species word (41254692), and a species error already corrected inside its own row (39546604).
* **Listed apart: 3 sentences in 3 records** (the two readers differ on the same sentence). For each, IT gets both readings and a wording true under both (file `SENTENCES_FOR_IT_ADV295_BLOCK1_SCI_20261126.md`).
* **Loose records** (strict or ADD): 5 of 5.
* Not completed classes: 42807679 figures (Figures 1 and 2 not held); 41210171 figures (Figures 1 to 5 not held). Both are stated limits, not unread-by-choice.

## Remaining debt (arithmetic from the AU recount, not re-run)

AU recount (the ADV-292 recipe: `rank_held_partials_adv265.py`, `containment_adv265.py`, `content_check_adv280.py`, `count_adv280.py`; `consumer_count.py` is not in the repository, it was a scratch script of the previous window; exclusions 28151481, 28045433, 41948127, 33958783 and the ten ADV-292 records): 17 eligible readable partials, 15 completable. Block 1 completed the class of four records (41254692, 42401046, 39546604, 41210171) and read figures 3 to 7 of a fifth (42807679, class not completable). If all five were among the 17 and the four among the 15, the debt after block 1 is 12 eligible and 11 completable partials, eight of them feeding DL-MECH-170 alone (block 2: 32719346, 33704440, 35079122, 35243344, 36282524). **This is arithmetic, not a recount**: the recipe has to be re-run to confirm it (about an hour); I have not run it.

## Verification note

Every strict sentence was checked on the original by SCI with a dated search (2026-11-26): the Qin XML ("potentially increas" 1 hit, "potentially increase" 0), the Table 3 header and rows of the Khadija XML (no WES column), the Helton XML ("shared therapeutic mechanism", "restored", "baseline"; "model-dependent" and "opposite" 0), the Tiwari Methods (Sprague-Dawley rat pups).
