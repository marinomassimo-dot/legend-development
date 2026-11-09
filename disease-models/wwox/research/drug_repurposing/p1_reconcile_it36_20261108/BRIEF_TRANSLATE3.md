# Brief: translations of added sentences (IT36, mechanical)

Role: translator. No web, no PubMed. Read `p1_reconcile_it36_20261108/translate_tasks3.json`. For each task write Italian (it), French (fr), Spanish (es) and German (de).
- mode ADD: `english` is a sentence block appended to an existing passage; translate only that block.
- mode EDIT: `new_english` replaces `old_english`; translate the full `new_english`.
Rules: keep every identifier, number, PMID, gene symbol, compound name, unit and the tag `[IT36]` exactly as written; do not add, drop or soften a hedge ("not shown", "unknown", "does not say"); scientific register, no interpretation. For terminology, match what the existing translations use (look up the same English terms in `view/i18n/content_source.json` against `view/i18n/content_it.json`, `_fr`, `_es`, `_de` by key; do not edit those files).
Output: one file `p1_reconcile_it36_20261108/translations_it39.json`: an object keyed by task `key`, each value `{"it": "...", "fr": "...", "es": "...", "de": "..."}`. Validate that it parses (`python3 -c "import json;json.load(open(...))"`). Final message: completed or not, number of keys, and the model and effort you observe.


Compound names keep their English international spelling in every language.
