# ADV-134 glossary: HE decisions on the plainer English proposals (2026-11-21)

Written by HE (ACTOR_ID plan). Reference-genotype class only. Limit stated first: the senses were checked by reading the defining or first-use lines the glossary cites (the lines were found as cited, except where noted); this is a reading by a model of the same family as the glossary producer, and no native specialist has checked any rendering.

## Rule for this pass (applies to every row)

1. The English text of the 25 passages of `adv132_dense_batch_it_20261121/selected_batch3.json` is NOT edited. The ADV-134 comparison is on the same 25 passages; every term below occurs in them, so an edit would change the comparison itself.
2. The programme-authored English (READMEs, tables, cards) carries these terms hundreds to thousands of times; it is not rewritten in one pass. The only renderer-owned site found is `framework/scripts/repurposing_view.py` (the group reason string "lead position {…} on {need}"); it stays unchanged until the translated sections are decided, because it is generated English that the translated passages were made from (each passage carries a hash of its English text; whether the renderer's i18n catalogue keys on that string was not measured here), and a change needs the full regeneration of all pages first.
3. An ACCEPT below therefore means two things: (a) the glossary sense and its fr/de/es renderings are the ones to use in this repeat batch; (b) the plainer English is the wording for NEW English text and for a first-use gloss, not a rewrite of old text. Authors of new packages may use it at once.

## Decisions

| n | term | decision | plainer English to use in new text | note |
|---|---|---|---|---|
| 1 | translation probe | ACCEPT | "bridging probe (the clinical drug used to test whether the tool-compound result carries over)" | sense read at the two cited lines; the English is ambiguous (protein synthesis) |
| 2 | engagement | ACCEPT | "target engagement"; "not shown to act on LDH, so unsuitable as a probe of LDH inhibition" | cited lines found |
| 3a | lead position / lead need | ACCEPT | "governing position", "governing need" | the cited line defines it as the best of an intervention's need positions; the priority rules call the list a grouping, not a ranking |
| 3b | "the lead" (lithium, d-APV) | ACCEPT | "the reference intervention with a WWOX-system result" | cited text names them leads used to build the phenotype path, and says they are coverage controls |
| 3c | leading rank, therapeutic lead | ACCEPT as a prohibition | none | neither reading occurs in the 25 passages |
| 4 | the glia line | ACCEPT | "the glia workstream" | the package says the line advances only as a role-resolving question |
| 5 | label | ACCEPT | "prescribing information (FDA label)" | |
| 6 | datum | ACCEPT | "data point" | NEEDS-DATUM and ABSENT stay as tokens |
| 7 | silencers | ACCEPT | "activity blockers" | cited text: a silencer lowering firing; tetrodotoxin |
| 8 | firing | ACCEPT with a gloss | "neuronal firing activity (Ca2+ event rate)" at first use | French "décharge" can read as epileptic discharge |
| 9 | weighed | ACCEPT | "considered, not decisive" | |
| 10 | seed | ACCEPT with a gloss | "starting gene set (seed)" at first use | the glossary's line cite for the first-use row (README line 16) is a different row; the sense is carried by the seed-specific filter line and the propagation line, which were found |
| 11 | WW1-dead | ACCEPT | "WW1-inactivated mutant" | |
| 12 | thin | ACCEPT | "weakly supported" | the F2 row of the priority rules defines it |
| 13 | lookalike | ACCEPT | "similarly named" | |
| 14 | guard-scope | ACCEPT | "covered by the evaluation guard (may be reported, may not decide)" | |
| 15 | bench | ACCEPT | "laboratory" | |
| 16 | card, carded | ACCEPT with a gloss | "candidate record (card)" at first use | |
| 17 | compound arm | ACCEPT | "compound-treated arm" | |
| 18 | signed assertion | ACCEPT | "assertion with a stated direction" | |
| 19 | floor-limited | ACCEPT | "limited by a floor effect" | |
| 20 | restated, re-scoped | ACCEPT | "re-derived and restated"; "narrowed in scope, still open" | not synonyms |
| 21 | development input | ACCEPT | "used to build the method, so not independent validation" | |
| 22 | readout gene | ACCEPT | "marker gene measured as the readout" | |
| 23 | held-out endpoint | ACCEPT | "reserved endpoint (kept out of the seed)" | |
| 24 | discriminator | ACCEPT | "discriminating measurement" | |
| 25 | pertinence row | ACCEPT | "assertion-to-need relevance row" | |
| 26 | need | ACCEPT as a first-use gloss only | "need (a biological target area where an intervention could be aimed, not an unmet clinical need)" | the NEED-… token is kept; the full replacement phrase is too long to repeat |
| 27-34 | matrix cell, catalogue family, valence, lever, null, transfer test, tool compound, step 0 | ACCEPT | as proposed | |

## 'pista' and 'piste' for 'lead'

Decision for this batch: not used for senses 3a to 3c; the glossary renderings stand. The landed ADV-129 catalogue is not touched. ADV is asked to confirm or countermand, since the glossary leaves the choice to HE and ADV.

## Not decided here (open, mine)

The ranking-section notice wording, after the ADV-134 repeat result; the 11 English passages with no notice; the renderer string above. None is touched by this record.

## Addendum after the ADV-134 result (HE, 2026-11-21): is plainer English worth landing for the 25 passages?

Answer in one line: **not in the existing text; yes in all new text.** The translation lane stays closed at the covered sections (overview, ranking), as ADV decided; the resume condition (a named reader or the operator needs the full edition in fr, de or es) is unchanged.

Why not rewrite the existing English:
- The six CHANGED rows on 'the lead' come from two passages (56, 57). Their text lives in `ranking_it8_p9_20261029/ranking.json`, `selections.tsv` and `unit_caveats.tsv` (about fourteen occurrences of "the lead's" across the programme) and in a frozen evaluation copy (`evaluation_it17_p3_20261101/freeze_20261101/frozen/`), which must not be edited. `ranking.json` is also a stamped surface (it carries the receipt-ledger length; two suites guard it). Editing authored data with a frozen twin to move a count in a lane nobody has asked for is not proportionate.
- The remaining CHANGED rows are the translator's own slips (washout, 'corte', the 57-DE limit), which plainer English does not remove; the stop rule would need a third blind pass either way.

What is decided instead (new programme text, effective now; a one-line pointer is in the roadmap's Standing method):
- 'lead' -> "governing position" for a position and "the reference intervention with a WWOX-system result" for lithium, d-APV and the like; never 'lead' for a rank or a candidate.
- 'restated' -> "re-derived and restated"; 're-scoped' -> "narrowed in scope, still open".
- 'need' -> gloss at first use ("need: a biological target area where an intervention could be aimed, not an unmet clinical need").
- the other accepted proposals of the table above.

German head nouns (IT's note): accepted as IT rendered them: lever = "Hebel (Eingriffspunkt)"; need keeps "biologischer Ansatzpunkt (Bedarf)" with the first-use gloss, and 'Bedarf' alone is NOT the head noun for need, because it reads as an unmet clinical need, which the programme says it is not. No collision remains once lever is "Hebel".
