# ADV-134 parity classification, glossary batch (IT, 2026-11-21)

Limit stated first: this is a mechanical floor written by the producer's side, not a verdict; the translator and the classifier are the same model, and no native specialist has read anything. Rule: `adv132_dense_batch_it_20261121/PARITY_RULE_ADV132_IT_20261121.md`, unchanged. Script: `adv132_dense_batch_it_20261121/parity_check.py`, unchanged. Input: `batch3g_translations.json` (25 passages, 75 rows).

## Runs
* Draft run (scratch, before the file entered the repository): 59 of 75 flagged. Two REAL DRIFTS found and repaired before the registered run: (1) the gene name `Adm` was omitted in all three languages of passage 51 ("..., Ankrd37, Adm beside Pgk1, ..."); (2) Spanish passage 69 had `alpha1/2/3/5` and `alpha2/alpha1` rewritten as `alfa...` (a symbol changed); also the French range `1-4` of passage 55 had been written `1 à 4` (a number token changed; restored). A later mechanical vocabulary alignment (burst, slice, wild-type, arm) changed no number or symbol.
* Run 1 (`PARITY_BATCH3G_RUN1_OUTPUT.txt`): 59 of 75 flagged, after the three repairs above and before the grammar pass.
* Grammar pass: after the vocabulary alignment (Spanish `rodaja` to `corte`, `salvaje` to `silvestre`, `grupo` to `brazo`; French `bouffée` to `salve`; German `Slice` to `Schnitt`) every row touched was re-read in context; three gender and article agreements broke and were repaired (`las mismas cortes`, `una corte`, `las cortes heterocigotas`). Run 2 (`PARITY_BATCH3G_RUN2_AFTER_GRAMMAR_OUTPUT.txt`) is identical to run 1: 59 of 75.

## Classification of the 59 flags (every flag read in context, source cues against rendering cues)
No flag is a REAL DRIFT. Each is a FALSE POSITIVE of one of these causes; the rows listed were checked one by one against the cue lists.

| Cause | Rows (passage-language) | Why it is not a drift |
|---|---|---|
| Source word with a negating prefix (un-, non-), rendered with a negation word | 51-FR/DE/ES (unreplicated, uninterpretable, unchanged), 52-FR/DE/ES (unrelated), 56-FR/DE/ES (unverified, untouched), 59-DE/ES (uncarded, undecidable), 63-FR/DE/ES (unchanged, unresolved), 66-ES (unchanged), 68-FR/DE/ES (unquantified), 69-FR/DE/ES (uncarded), 71-FR/DE/ES (untested), 74-FR/ES (unresolved), 75-FR/DE/ES (uncarded) | the rule says a prefix negation is not a source cue; the rendering word is the faithful translation |
| Source 'null' (a result of no effect) rendered 'ohne Effekt' / 'kein Effekt' (glossary row 31) | 51-DE, 63-DE, 68-DE, 71-DE, 72-DE, 73-DE, 74-DE | 'null' is not in the English cue list; the German rendering is the glossary's |
| Spanish or French double negation ('no ... ningún', 'ne ... aucune', 'non pas', 'ni') | 51-FR/ES, 52-FR/ES, 53-FR/ES, 55-ES, 57-FR/DE/ES, 60-ES, 63-ES, 66-FR | one source negation is two lexicon words in the rendering |
| Glossary glosses that add a negation or a symbol: 'donnée de développement (non indépendante)' (row 21), 'US label' to 'notice officielle américaine (information de prescription FDA)' (row 5), '(avec résultat dans un système WWOX)' (row 3b), 'sonde ... dont l'action sur la LDH est démontrée' (row 2) | 56-FR/DE/ES, 57-FR/ES, 66-FR/ES (non indépendante), 53-FR/DE/ES (FDA; US dropped; ES extra LDH), 56-FR/DE/ES (WWOX added) | added by the glossary on purpose; none changes a number, limit, hedge or negation of the source |
| Modal 'can/cannot' or 'would', and words that end in the lexicon suffix | 51-FR/ES 'peut' (can share), 52-FR 'peut', 'retrait' (ends in -rait), 52-DE/ES 'kann', 'puede', 54-FR/DE/ES 'peuvent', 'können', 'pueden' (cannot decide), 66-FR/DE/ES 'peut', 'kann', 'puede' (cannot return), 70-ES 'auditoría' (ends in -ría), 70-DE 'wäre' for 'would' (not in the German list), 63-DE 'blieben' for 'would remain' (not in the list) | 'can' is not an English hedge cue; the German subjunctives are a lexicon gap |
| 'about' used as a preposition ('is about an expression seed') | 56-FR/DE/ES (HEDGE 2 to 0) | not a hedge; the rendering says 'concerne', 'betrifft', 'se refiere' |
| 'about' kept as a hedge by a word outside the list | 59-ES 'unos 50' | hedge present, word not in the Spanish list |
| Underscore tag words counted by the rule's word split (`not_WWOX`, `no_T_type_measurement`, `none`, `not_evaluable`), copied unchanged | 61-FR/ES, 62-FR/DE/ES, 64-DE/ES, 72-FR/DE/ES, 74 | the tags are identifiers and are copied unchanged; the rule counts their English words only on the source side where the target lexicon has no match |
| Emphasis capitals ('NOT', 'IS') rendered in capitals in the target | 56-FR 'EST', 56-DE 'IST', 62-FR 'PAS', 62-DE 'NICHT', 62-ES 'NO' | same emphasis kept |
| Translated acronym or abbreviation | 53-FR/ES 'ARN' for 'RNA' (mRNA), 55-FR 'IRM', 55-DE 'MRT', 55-ES 'RM' for 'MRI', 52-DE 'Abb.' for 'Fig', 52-ES 'ROI' for 'ROIs' | standard term in the target language |
| Negation expressed by a noun ('l'absence de changement', 'Fehlen einer Veränderung', 'ausencia de cambio') | 54-FR, 59-DE/ES | a negation present in meaning, not in the word list |

## What the check did not see
Meaning, scope, attachment of a modifier, a wrong referent. The blind check is the test.
