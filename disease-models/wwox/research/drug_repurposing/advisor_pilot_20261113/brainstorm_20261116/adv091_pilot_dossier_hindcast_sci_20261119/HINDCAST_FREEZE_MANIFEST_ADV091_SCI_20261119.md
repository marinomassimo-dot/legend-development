# Hindcast freeze manifest (SCI, ADV-091 item 2): digests written at 2026-11-19T19:05Z, before any score exists

Hypothesis level; a diagnostic, never a licence; not medical advice. No scoring of any pair has been run, no scorer has been shown any file, and the outcome labels were assigned from abstract sentences read on 2026-11-19 (see the KEY file). These files are not edited after this line: a change to the set, the rule, the components or the plan is a new freeze file with a new date, and any score is reported against the digest it was run under.

| file | sha256 | who may read it |
|---|---|---|
| HINDCAST_FREEZE_KEY_ADV091_SCI_20261119.md | 84dac33059a4bea60257b64578436670cc4f34ce40d0e078e027e292be4025c1 | analyst only; never a scorer |
| HINDCAST_FREEZE_SCORER_SHEET_ADV091_SCI_20261119.md | f6368a3fd9d2c17589910305f6ec9cb4d192abe05c4111b3653c5118293c8d99 | Part A to a scorer; Part B analyst only |
| build_hindcast_freeze.py (the pair table and the quote check) | 7798271bf5c1d695952ea769aa6bce8b0256363d93f7ba5134278c144c200e27 | anyone |
| scorer_sheet_template.md (the sheet before the table is filled) | 2f266ba3f4d764091b29baa5223bf824f4968fac2670a5de77e68d5512069aa7 | anyone |

The abstract copies (15 files, Europe PMC plain GET, 2026-11-19) are held outside git in files/hindcast_abstracts_adv091/ and their sha256 digests are in the KEY file. To re-verify the quotes: `python3 -I build_hindcast_freeze.py --check --abstracts <folder>` (16 quotes, all verbatim at the time of freezing).
