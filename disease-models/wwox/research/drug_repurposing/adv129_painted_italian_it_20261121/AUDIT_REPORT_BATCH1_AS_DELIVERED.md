# Blind check, batch 1 (13 translation pairs), as delivered (2026-11-21)

Delegate: legend-delegate, requested sonnet and effort high (reported claude-sonnet-5-5; effort cannot be seen from inside the run, the transcript is the source). Input: `TRANSLATION_PAIRS_FOR_BLIND_CHECK.md` (item order in `pair_key.json`: P01 to P03 are the three authored items that were already in the catalogue but never reached a non-Italian page; P04 to P13 are the ten passages added by this assignment). Hand-back persisted by the orchestrator; only the rows that are not FAITHFUL are reproduced here, the rest of the 52 item-language rows are all FAITHFUL.

Counts: FAITHFUL 46, MINOR 5, CHANGED 1.

| ID | Lang | Verdict | Issue | Corrected wording offered |
|---|---|---|---|---|
| P02 | DE | MINOR | "US-Zulassungsetiketten" adds "Zulassungs-" (approval or registration), which is not in the Italian "etichette USA"; "Etiketten" reads oddly for drug labels | "Elektrophysiologie an Schnitten des neuronenspezifischen Knockouts aus dem Originalartikel: Die Linie ist hier nicht verfügbar, ob sie erhältlich ist, ist nicht bekannt; Magnesium: US-Etiketten (Produktinformationen) nach Namen, Italien nicht geprüft." |
| P02 | ES | MINOR | "knockout neurona-específico" is a calque; idiomatic "específico de neuronas" | "Electrofisiología en cortes del knockout específico de neuronas del artículo original: la línea no está disponible aquí, no se sabe si se puede obtener; magnesio: etiquetas de EE. UU. por nombre, Italia no verificada." |
| P03 | ES | MINOR | same calque | "Electrofisiología en cortes del knockout específico de neuronas del laboratorio de origen: la línea no está disponible aquí, no se sabe si se puede obtener." |
| P04 | FR | MINOR | "producteur" can be read as a manufacturer; the Italian names the analyst who produced the extraction, as opposed to the verifier in P13 | "... (extraction du producteur de l'analyse, par opposition au vérificateur)"; shorter: "extraction de l'analyste producteur" |
| P04 | DE | CHANGED | "Herstellerextraktion" means the manufacturer's extraction: a mistranslation of a role in a verification workflow | "... (Extraktion durch den Ersteller der Analyse)" |
| P04 | ES | MINOR | "productor" reads as a producer or manufacturer | "... (extracción del analista productor)"; alternative "extracción de quien produjo el análisis" |

Delegate's notes: P13 (verifier's extraction) FAITHFUL in all four languages; "Prüfer" acceptable and to be paired with "Ersteller" in P04. Ambiguities of the Italian original that all four renderings keep literally ('morto' in P01, 'silenziatori'): not translation errors, no change proposed. Not readable or not done: nothing; all 13 items read in full; no other file opened, no web search.

## What was applied (orchestrator)
P02 DE: "US-Etiketten nach Namen" (the added word 'Zulassung' removed; the delegate's parenthetical 'Produktinformationen' not adopted, it adds words). P02 ES and P03 ES: the delegate's wording. P04 FR: "extraction par l'auteur de l'analyse". P04 DE: the delegate's wording. P04 ES: "extracción de quien produjo el análisis" (the delegate's alternative). These six repairs go to the narrow second check (`TRANSLATION_PAIRS_BATCH2_FOR_BLIND_CHECK.md`).
