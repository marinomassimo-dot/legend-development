# Blind recheck of 39 rows (36 repaired batch-3 rows and three ADV-131 rows in their final wording), report as delivered

Delegate: legend-delegate, model claude-sonnet-5-5, effort high (dispatch; read back with session_model_census.py). Input: BLIND_ROWS_RECHECK_FOR_CHECK.md only (row ids with an E prefix are the ADV-131 rows 31-FR, 34-DE, 36-DE). Persisted verbatim from the hand-back.

FAITHFUL 21, MINOR 12, CHANGED 6

I read only BLIND_ROWS_RECHECK_FOR_CHECK.md, in full, and edited nothing. I did not open the delegation-budget protocol, because the brief said to read nothing else about this task. I could not check the underlying science against any paper, only each rendering against its source sentence.

Number, name and identifier checks found no discrepancy in any of the 39 rows. This covers every value and range, all dates, PMIDs (42397075, 32000863), GSE158684, card, IT and P ids, gene symbols, the NEED-* tags, the underscore tags and the NP1B1 to NP1B4 range. Decimal commas are acceptable. All six CHANGED rows concern a domain term (a wrong rendering of "lead" or "target engagement"), not a number. The rows that are not FAITHFUL are listed below.

| Row | Verdict | Source fragment | Rendering fragment | Proposed repair |
|---|---|---|---|---|
| 51-FR | CHANGED | "neuronal engagement and brain exposure not shown" (engagement = target engagement) | "engagement neuronal et exposition cérébrale non démontrés" | "engagement de la cible dans les neurones (target engagement) et exposition cérébrale non démontrés". In French "engagement neuronal" is neural lineage commitment, so the domain term is wrong. |
| 51-FR | (same row, minor) | "only at about 0.1 to above 5 millimolar" | "n'inhibe ... qu'd'environ 0,1 à plus de 5 millimolaires" | Garbled elision. Use "qu'à des concentrations d'environ 0,1 à plus de 5 millimolaires". |
| 51-FR | (same row, minor) | "so the ... contrast ... is also a second transfer test" | "de sorte que ... soit aussi un second test" | The subjunctive turns a result into a purpose. Use "est aussi". |
| 51-FR | (same row, minor) | "a pre-onset age group" | "un groupe d'âge pré-apparition" | "un groupe d'âge avant l'apparition (des crises)". |
| 51-ES | MINOR | "so the ... contrast ... is also a second transfer test" | "de modo que ... sea también una segunda prueba" | The subjunctive reads as purpose, not result. Use "es también". |
| 51-ES | (same row) | "upstream of PDK1" | "por encima de PDK1" | "aguas arriba de PDK1". |
| 52-ES | MINOR | "human firing recovery" and "a reduction of firing" | "recuperación humana de la descarga"; "reducción de la descarga" | "descarga" reads as epileptic discharge. Use "disparo" or "actividad de disparo". |
| 52-ES | (same row) | "WW1-dead" | "WW1 muerto" | Calque. Use "WW1 inactivo (dominio WW1 mutado)". |
| 52-ES | (same row) | "bench protocol sheet" | "hoja de protocolo de banco" | "hoja de protocolo de laboratorio". |
| 52-FR | MINOR | "burst scoring is read" | "le quantification des salves est lu" | Gender and agreement error. Use "la quantification (cotation) des salves est lue". |
| 52-FR | (same row) | "WW1-dead" | "WW1-mort" | Calque. Use "WW1 inactif". |
| 52-FR | (same row) | "an acute effect on an endpoint" | "un effet aigu sur un critère" | "critère de jugement". |
| 53-DE | MINOR | "a US label that names no LDH mechanism" | "ein US-Fachinformation, das keinen LDH-Mechanismus nennt" | Gender error. Use "eine US-Fachinformation, die ... nennt". |
| 53-DE | (same row) | "weighed, not decisive" | "gewichtet, nicht entscheidend" | "gewichtet" means statistically weighted. Use "berücksichtigt" or "abgewogen". |
| 53-ES | MINOR | "weighed, not decisive" | "ponderada, no decisiva" | "sopesada" or "considerada". |
| 53-FR | MINOR | "LDH-engagement probe" | "sonde d'engagement de la LDH" | "sonde d'engagement de cible (target engagement) de la LDH". |
| 53-FR | (same row) | "fly Ldh-alone arm" | "le bras Ldh seule chez la drosophile" | The species is not in the source (DE and ES keep "fly"). Use "mouche", or confirm Drosophila against the source paper. |
| 63-DE | MINOR | "a protein-level HIF datum ... that separates ..." | "ein HIF-Messwert ..., das ... trennt" | Gender error. Use "der ... trennt". |
| 64-FR | MINOR | "no wild-type or drug-by-genotype test" | "aucun test sauvage ni médicament par génotype" | Elided noun. Use "aucun test chez le sauvage ni test médicament × génotype". |
| 65-FR | MINOR | "littermates" | "témoins de portée" | "témoins" adds the meaning "controls", which is not in this source. Use "animaux de la même portée". |
| 66-ES | MINOR | "the lookalike BTX-A51" | "el homónimo aproximado BTX-A51" | "el nombre parecido BTX-A51". |
| 75-DE | MINOR | "decisive datum ABSENT from both sources" | "entscheidender Messwert ... ABWESEND" | "abwesend" is used for persons. Use "FEHLT" or "NICHT VORHANDEN". If ABSENT is a verdict token like SOURCE READ, copy it unchanged. |
| E34-DE | MINOR | "the class is carded" | "auf einer Karteikarte erfasst" | "Karte" is used everywhere else. Use "als NMDAR-Interventionsklasse mit einer Karte geführt". |
| 67-ES | CHANGED | "lead position F2" | "posición de pista F2" | "pista" means clue or track, not a lead compound or intervention. Use "posición de la intervención líder (lead) F2". |
| 71-ES | CHANGED | "lead position F2" | "posición de pista F2" | Same repair as 67-ES. |
| 72-ES | CHANGED | "lead position F2" | "posición de pista F2" | Same repair as 67-ES. |
| 73-ES | CHANGED | "lead position F3" | "posición de pista F3" | Same repair as 67-ES, with F3. |
| 73-FR | CHANGED | "lead position F3" | "position de piste F3" | Use "position de l'intervention de tête (lead) F3". |

Row 57-DE uses "Leitsubstanz" for "the lead", and my reading of it is that "lead" there means the lead compound or intervention. The "lead position" rows should follow it. I marked these five CHANGED because I do not know the programme glossary. If the glossary fixes "lead" as "pista", downgrade them to MINOR, but the rendering would still be opaque to a pharmacologist.

FAITHFUL rows: 51-DE, 52-DE, 54-DE, 57-DE, 59-DE, 59-ES, 59-FR, 62-DE, 62-ES, 62-FR, 64-DE, 64-ES, 65-DE, 65-ES, 66-FR, 69-DE, 69-ES, 69-FR, 70-ES, E31-FR, E36-DE.

Systematic observations
- Agreement and elision errors. Several errors look like mechanical substitutions that left grammar broken: FR "qu'd'environ", FR "le quantification ... lu", DE "ein US-Fachinformation, das", DE "HIF-Messwert, das". All four are in text that looks like repaired rows. A grammar pass over every repaired row is warranted.
- "de sorte que" and "de modo que". FR and ES use the subjunctive where the source states a consequence ("so ... is also"). This turns a result into a purpose.
- "Target engagement" is rendered well only in Spanish. ES 51 and 53 write "interacción con la diana (target engagement)". FR 51 gets it wrong, and FR 53 is bare "engagement de la LDH". Standardise on "engagement de la cible" for French.
- Calques. These are "WW1 muerto/mort", "protocolo de banco" and ES "descarga" for firing. For French "décharge" (firing), I judged it acceptable ("fréquence de décharge" is standard), though it could be misread as epileptic discharge.
- "Seed". It is kept as "Seed" in DE but rendered "graine" in FR and "semilla" in ES. This is inconsistent and arguably opaque. Confirm it against the programme glossary.
- Guard and weigh terms. "guard-scope" is rendered "Schutzbereich" (DE), "périmètre de garde" (FR) and "ámbito de guarda" (ES), which are consistent with each other but literal. "Weighed" is rendered literally in DE, ES and FR.
- Terminology consistency inside DE. "Komparator" and "Vergleichssubstanz" both appear, and so do "Verbindung" and "Substanz". This is not a meaning change.
- "none" in the L2 counts. It is translated ("ninguna"), while neighbouring snake_case values (direction_unresolved, not_evaluable) stay English. This is acceptable, but confirm that "none" is not an enum value.
