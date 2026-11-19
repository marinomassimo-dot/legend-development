**ANSWER**

I could not find the operator's correction recorded as the operator's correction in this repository. I found the rule and the pinned tests that encode it. I also found a reasoned account of why the failure happened, but that account sits in code comments and was written by an actor, not the operator.

(1) **The correction.** A translation fix is not verified until you check the page the generator actually produces, not only the translation catalogues.

**The reason, as recorded.** The 2026-11-18 dashboard audit found the catalogues complete (582 of 582). Even so, the rendered FR/ES/DE pages still carried about 23 "original language only" markers. The cause was that `load_allowlist` swaps the Italian redaction-formula wording for the page language's wording inside the replacement texts. That happened before the lookup by hash, so a passage that quoted a formula no longer matched its inventory key. The translation existed and was never found. Regenerating the pages did not change that. Neither the catalogue check nor the translation-completeness check could see this. Only the rendered page showed it.

A second case on 2026-11-19 is recorded in the same test file. A correctly translated Spanish "de 105" matched the forbidden catalogue name 'DE 105' in the shareable audit, and the audit refused the package. That was caught only on freshly built pages.

(2) **How I would verify the new change.** I have not run any of this, because I was told not to run commands.
- Run `python3 -B framework/scripts/test_repurposing_view_i18n.py`. It builds all five pages fresh with `rv.build(DR, "shareable", lg)` and checks them. The key tests are:
  - `test_a_translated_passage_is_never_shown_as_original_language_only_on_the_rendered_page`
  - `test_a_catalogue_translation_that_kept_an_italian_formula_gets_the_page_language_formula`
  - `test_every_freshly_built_page_passes_the_shareable_audit`
  - `test_no_italian_interface_text_is_left_outside_marked_passages`
- Run `repurposing_view.py i18n --what check`. This one compares the committed inventory with a fresh collection.
- Run `repurposing_view.py audit-shareable --dynamic` and `viewports` for each page.
- Run `repurposing_view.py package` and then `package --check` before freezing. Per the README, a package written after the commit leaves the tested clone stale.
- Have an independent reader check the high-risk passages (negations, hedges, unknown versus negative) in each language, as DEPLOY.md requires.
- Don't rely on the committed `view/index.*.html` files. The test comment says "the committed editions can be stale".

(3) **Reason or only rule?** I found the reason, but only in code comments. In the rule documents (README and DEPLOY.md) I found only the rule, not the reason. I found no operator message, session evaluation or lessons file that records this as an operator correction or explains why it was made.

**EVIDENCE**
- `framework/scripts/test_repurposing_view_i18n.py:148-149`: "2026-11-18 dashboard audit: the catalogues were complete (582 of 582) and the rendered FR/ES/DE pages still carried ~23 original-language markers, because the redaction formulas were localised BEFORE the lookup by hash and the text lost its identity. Pinned on the page that is produced, not on the catalogue."
- `framework/scripts/repurposing_view.py:123-128`: the `source_identity` docstring. It says "the translation existed and was never found (2026-11-18 dashboard audit: 17 English passages and a generic phrase marked 'original language only' on FR/ES/DE, and a regeneration did not change that)".
- `framework/scripts/repurposing_view.py:135-139`: the `localise_formulas` docstring, which says 15 passages per language kept the Italian formula.
- `framework/scripts/test_repurposing_view_i18n.py:188-190`: the 2026-11-19 "de 105" vs 'DE 105' collision. It says "Pinned on freshly built pages (the committed editions can be stale)".
- `framework/scripts/test_repurposing_view_i18n.py:44`: an earlier case, "2026-11-12: a curated passage was edited, `i18n --what check` passed, and only the suite found the stale inventory".
- `disease-models/wwox/research/drug_repurposing/view/DEPLOY.md:159`: "Verification before a change of wording is published: `i18n --what check`, `test_repurposing_view_i18n.py`, the static audit of every page, `audit-shareable --dynamic`, `viewports` for each page, and an independent reading of the high-risk passages".
- `framework/scripts/README.md:147`: the pre-freeze procedure, including "`repurposing_view.py i18n --what check`" and the package steps.

**FILES OPENED IN ORDER**
1. `framework/state/state_manifest_current.md` (first 60 lines only, so I did not check `current_state: READY`)
2. `framework/scripts/test_repurposing_view_i18n.py` (lines 1-80, then 130-220)
3. `framework/scripts/repurposing_view.py` (lines 115-144)
4. `framework/scripts/README.md` (line 147)
5. `disease-models/wwox/research/drug_repurposing/view/DEPLOY.md` (lines 155-160)

I also ran several searches across the repository. I did not open §21c, §21d or §21e of LEGEND_CORE, which the project CLAUDE.md says to read first. I also did not open the session-evaluation files or any `active_lessons/` material.

**WHAT YOU WERE UNSURE ABOUT**
- I could not show that the operator was the one who made the correction. The comments say "dashboard audit". The only operator-attributed 2026-11-18 note I found, `ADV-046.md`, is about something else (generalised blocks, inference strength).
- The repository is large, and my searches used keyword patterns and skipped `.tsv`, `.json`, `.jsonl` and `.html` files. A fuller recording may exist under different wording, for example in a session evaluation, the `ledger/` folder, or an operator-feedback file I did not open.
- I did not check whether the "no lease gates your work" and task-branch rules affect how the new change should land.
- The suite needs the module data and i18n files (`HAVE`) or it skips. A skip would look like a pass, so check that the tests actually ran.

**MEMORY_CANARY**
No. I see no private memory notes or auto-memory index from an earlier session in my context. Only the two CLAUDE.md files and the git status were provided.