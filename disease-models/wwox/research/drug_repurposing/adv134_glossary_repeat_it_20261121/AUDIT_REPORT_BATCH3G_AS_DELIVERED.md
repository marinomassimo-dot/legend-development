# Blind check of the glossary batch (75 rows), report as delivered

Delegate: legend-delegate, model sonnet, effort high (stated in the dispatch; read back from its transcript with `session_model_census.py`: models `claude-sonnet-5-5` on 3 turns, efforts `high` on 3 turns, dispatch effort `high`, 117,314 subagent tokens, 4.5 minutes). A new delegate, not one of the two of ADV-132 and not the glossary producer. Input: `BLIND_PAIRS_BATCH3G_FOR_CHECK.md` only. The report below is the delegate's final message, persisted verbatim from the hand-back (the harness refuses subagent files); the harness's own indentation of the hand-back lines is removed.

FAITHFUL 51, MINOR 16, CHANGED 8

Scope: I read the whole file (75 rows, 25 passages) and compared each rendering to its source sentence by sentence. I did not read anything else in the repository and used no external service. Every number, date, range, percentage, PMID, GEO id, card id and underscore tag matched the source in all 75 rows. These tags copied unchanged: AMPAR_untested, NEED-*, partial_benefit, direction_unresolved, observed_*, audit_repair_not_rejudged and the rest. No number or identifier error was found.

**Rows that are not FAITHFUL**

| Row | Verdict | Source fragment | Rendering fragment | Proposed repair |
|---|---|---|---|---|
| 52-FR | CHANGED | "a 2-week washout" | "avec 2 semaines de sevrage" | "sevrage" means withdrawal, not washout. Use "avec 2 semaines de lavage (wash-out)". Same row, minor: "burst scoring" is rendered "le décompte des salves", use "la cotation des salves". The typo "triheteromères" should be "trihétéromères". |
| 52-ES | CHANGED | "which are not slice values" | "que no son valores de corte" | "valores de corte" reads as cut-off thresholds. Use "que no son valores obtenidos en cortes". |
| 56-FR | CHANGED (role word) | "the lead's seizure readout"; "the G01 seizure lead is untouched" | "l'intervention de référence"; "l'intervention de référence pour les crises de la fiche G01" | "lead" is the leading candidate, not a reference or comparator intervention. Use "le candidat de tête (lead)" or "la piste principale". |
| 56-DE | CHANGED (role word) | same as 56-FR | "Referenzintervention" | "Leitkandidat (Lead)". |
| 56-ES | CHANGED (role word) | same as 56-FR | "la intervención de referencia" | "el candidato principal (lead)". |
| 57-FR | CHANGED (role word) | "the lead's result is a bursting readout in slices" | "le résultat de l'intervention de référence est une lecture de salves" | "le résultat du candidat de tête (lead)". |
| 57-DE | CHANGED (role word), plus a scope change | the same "lead" fragment. Second fragment: "has a firing readout" | "Referenzintervention"; "eine Auslesung der neuronalen Aktivität in einem menschlichen WWOX-defizienten neuralen System" | "Leitkandidat (Lead)". The negative claim is about firing. Rendering it as "neuronal activity" broadens its scope to include network or MEA activity. Use "eine Auslesung des Feuerns (der Entladungsrate)". |
| 57-ES | CHANGED (role word) | same as 57-FR | "la intervención de referencia" | "el candidato principal (lead)". |
| 51-FR | MINOR | "restated IT9 P4a"; "restated after IT10 P2.1" | "réexaminé et reformulé" | "restated" means re-issued. "réexaminé" adds a re-examination the source does not state. Use "reformulé". Also: "a DepMap bulk test" is rendered "test DepMap en masse", use "test DepMap bulk (en vrac)". |
| 51-DE | MINOR | "restated" | "neu abgeleitet und neu formuliert" | "neu abgeleitet" means re-derived, which is not in the source. Use "neu formuliert". |
| 51-ES | MINOR | "restated"; "a DepMap bulk test" | "reexaminado y reformulado"; "prueba DepMap en masa" | "reformulado"; "prueba DepMap en bulk (a granel)". |
| 52-DE | MINOR | "the only human firing recovery"; "a reduction of firing" | "Wiederherstellung der neuronalen Aktivität (Feuern)"; "Verringerung der neuronalen Aktivität (Feuern)" | The head noun is the broader "neuronal activity". Use "Wiederherstellung des Feuerns (der Entladungsrate)". |
| 53-FR | MINOR | "only 2 are 30 fold or more on every pair" (selectivity); "restated" | "dont seules 2 sont à 30 fois ou plus sur chaque paire"; "réexaminé et reformulé" | The word "selective" is lost. Use "dont seules 2 sont sélectives à 30 fois ou plus sur chaque paire". Also "reformulé" only. |
| 53-DE | MINOR | "restated" | "neu abgeleitet und neu formuliert" | "neu formuliert". |
| 53-ES | MINOR | "restated" | "reexaminado y reformulado" | "reformulado". |
| 55-FR | MINOR | "a report selected for the finding" | "sélectionné pour la découverte" | "découverte" means discovery. Use "sélectionné pour la constatation (l'anomalie)". |
| 58-DE | MINOR | "matched potency strata" (developmental potency) | "abgeglichener Potenzstrata" | "Potenz" alone is ambiguous with compound potency and impotence. Use "Strata gleichen Differenzierungspotenzials". |
| 58-ES | MINOR | "matched potency strata" | "estratos de potencia celular emparejados" | "potencia" suggests pharmacological potency. Use "estratos de potencialidad (potencial de diferenciación) celular emparejados". |
| 62-FR | MINOR | "its benefit is in absence-type models, convulsive models only at higher concentration" | "son bénéfice se limite aux modèles de type absence, aux modèles convulsifs seulement à concentration plus élevée" | "se limite" adds a restriction and contradicts the clause that follows. Use "son bénéfice se situe dans les modèles de type absence ; dans les modèles convulsifs, seulement à concentration plus élevée". |
| 62-DE | MINOR | "the only WWOX link" | "die einzige WWOX-Verbindung" | "Verbindung" means chemical compound in a pharmacology text. Use "der einzige Bezug zu WWOX". |
| 66-FR | MINOR | "IT11 P2.2 restatement" | "Réexamen et reformulation" | "Reformulation". |
| 66-DE | MINOR | "restatement" | "Neuableitung und Neuformulierung" | "Neuformulierung". |
| 66-ES | MINOR | "restatement" | "Reexamen y reformulación" | "Reformulación". |
| 70-ES | MINOR | "must not be pre-registered" | "no debe preinscribirse" | "preinscribir" means to pre-enrol. Use "preregistrarse". |

**Systematic points**

1. **"lead".** The six CHANGED rows for passages 56 and 57 share one cause: "lead" is rendered as "intervention de référence", "Referenzintervention" and "intervención de referencia". In pharmacology "reference intervention" means a comparator. "lead" here is the leading candidate (lithium in 56, d-APV in 57). This is my judgement as a domain reader. The three languages agree with each other, so it is a deliberate choice. If the producer's glossary fixes it, this is the one decision to re-open. Elsewhere "lead position" is rendered "position dominante", "maßgebliche Position" and "posición principal", which is acceptable.

2. **"restated".** "restated" is rendered as "re-examined and reformulated" (FR, ES) or "re-derived and reformulated" (DE) in passages 51, 53 and 66, nine rows in all. This adds an act of re-examination or re-derivation that the source does not state. I graded these MINOR. They could be graded CHANGED if the glossary does not explicitly fix this mapping.

3. **Bracketed glosses.** The producer added glosses throughout. I did not downgrade rows for them, treating them as intentional glossary devices. Examples: "(target engagement)", "(étape-barrière)", "Vorbedingungs-/Gate-Experiment", "(de la molécule-outil au médicament)", "(Eingriffspunkt)", "(axe d'intervention biologique)", "(área diana biológica)", "(avec résultat dans un système WWOX)", "(dont l'expression sert de mesure)". Under a strict "nothing added" rule, most rows would become MINOR. Two glosses carry real risk:
   - **"need" in DE.** It is rendered "Ansatzpunkt (Bedarf)" in 59, 61, 62, 63, 67, 69, 71, 72 and 73. "Ansatzpunkt" is the head noun, and "lever" is rendered "Hebel (Eingriffspunkt)". The two near-synonyms for different concepts invite confusion. Use "Bedarf" as the head noun.
   - **"need" in FR and ES.** The glosses "(axe d'intervention biologique)" and "(área diana biológica)" recast a need as a target area.

4. **Interpretation applied in all three languages.** "PTZ-alone null cohorts" in 55 is read as knockout (null) cohorts: "(null)", "(Null)", "(nulas)". This is plausible, since "null mouse" is used in 70, but "null" could also mean no-effect. Please confirm against the source paper.

5. **Terms judged acceptable, listed for transparency.**
   - FR "banque" for sequencing library.
   - DE "Auswertungssperre (Guard)".
   - "knockdown" rendered as "silenciamiento" in ES.
   - "hup" copied as is.
   - "wet lab" rendered simply as "Labor/laboratoire/laboratorio" in 58, losing the contrast with the computational step. This is trivial.

6. **Other observations.** No hedge was lost or inverted. "May", "about", "unknown", "not detected, not excluded", "only" and "at least" are preserved everywhere. No negation was flipped. The decimal commas are acceptable. The 116 + 89 = 205 and 5+1+2+2+2 = 12 tallies are intact.
