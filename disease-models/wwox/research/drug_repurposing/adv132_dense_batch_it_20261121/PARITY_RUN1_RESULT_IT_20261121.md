# ADV-132 parity check, run 1: the 150 existing ADV-131 rows (IT, 2026-11-21)

Rule: `PARITY_RULE_ADV132_IT_20261121.md`, committed (52d924fa4) before this run and not edited since; checker `parity_check.py`; input: the 50 source passages and the 150 renderings exactly as landed on `main` (78e79ace3), `adv131_all_translations_as_landed.json`; raw output `PARITY_RUN1_ADV131_150_ROWS_OUTPUT.txt`.

## Answer first
150 rows, 27 flagged (18 percent), 29 flags (two rows carry two). Every flag was read against the source and the rendering and classified by hand: 29 FALSE POSITIVE, 0 REAL DRIFT. No NUMBER flag at all: every number, decimal, percentage and number-with-unit of the 50 passages is present with the same count in all 150 renderings (the dense passages 23, 42 and 47 included: 36 of 42, 51, 5, 3, 2021, 57.3 to 27.5 pA, about -52 percent, 2 / 3 / 1 / 1 case counts). The check found no problem the blind checks had missed, and it did not see the one change the blind third look called CHANGED (31-FR 'sans rapport structural', now 'non apparentés'): a scope qualifier is not a token class of the rule, which is the stated limit.

## The flags, by class (all FALSE POSITIVE)
| Class | Rows | Why it is not drift |
|---|---|---|
| A word of the source that is translated (a quoted value or an acronym with a language form) | 14-FR, 14-DE, 14-ES ('Yes' to Oui, Ja, Sí); 18-FR, 18-DE, 18-ES (MRI to IRM, MRT, RM) | the rule's name and symbol checks cannot know the language forms |
| Plural of an acronym | 31-FR, 31-ES ('NAMs' to NAM); 49-FR, 49-ES ('IPSCs' to IPSC) | French and Spanish do not pluralise acronyms; the symbol is intact |
| Negation by prefix or by a verb of the source (the source has no cue word) | 15-FR, 15-ES, 19-FR, 19-ES ('unresolved' to 'non résolus', 'no resueltos'); 28-FR, 33-FR ('withheld' to 'n'est pas publiée', 'non publiés'); 31-FR, 31-DE, 31-ES ('unrelated' to 'non apparentés', 'nicht verwandten', 'no relacionados') | the rule says so: a prefix negation is not a source cue; the meaning is the same |
| Negation counted twice or once by construction | 41-FR, 41-ES ('no X or Y' to 'aucune X ni Y', 'sin X ni Y': the coordinating word counted); 42-FR, 42-DE, 42-ES ('unresolved' and 'null' rendered with 'non', 'ohne', 'sin'); 21-DE ('answered no' to 'ergab: nein', 'nein' is not in the German lexicon) | the counts differ by construction, the meaning is the same |
| A modal of ability in the hedge lexicon | 43-FR, 43-DE, 43-ES ('Cannot be read' to 'Ne peut pas', 'Kann nicht', 'No puede': 'peut', 'kann', 'puede' are 'can', not 'may', and sit in the lexicon as 'may') | lexicon crudeness: the three renderings keep the negation and the ability |
| A subjunctive not in the lexicon | 44-DE ('would be needed' to 'wäre nötig') | lexicon gap; the conditional is kept |

## What this says about the rule (not changed here: a change is a new rule with its own record)
By class, 19 of the 29 flags are negation or hedge cue counts (9 prefix or verb negation, 6 construction counts, 3 modal of ability, 1 subjunctive) and 10 are name or symbol flags (6 translated words, 4 acronym plurals); there is no numeric flag. The numeric part raised nothing on 150 rows, so on this sample it is silent and, with nothing to test it against, its sensitivity is shown only by the synthetic check made before the run (a changed decimal is flagged), not by a real drift. The cue part is the noisy one. For the dense batch the numeric and symbol flags will be read as drift candidates first, and a cue flag as a prompt for a second look at the sentence.
