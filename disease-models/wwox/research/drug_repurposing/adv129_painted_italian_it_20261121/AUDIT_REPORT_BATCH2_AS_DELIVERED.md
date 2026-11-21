# Blind check, batch 2 (six repaired renderings and one new label), as delivered (2026-11-21)

Delegate: legend-delegate, requested sonnet and effort high (reported claude-sonnet-5-5 and effort high; the transcript is the source). Input: `TRANSLATION_PAIRS_BATCH2_FOR_BLIND_CHECK.md` (10 item-language rows). Counts: FAITHFUL 5 (B3 ES; B4 EN, FR, DE, ES), MINOR 5, CHANGED 0.

| ID | Lang | Verdict | Issue | Corrected wording offered |
|---|---|---|---|---|
| B1 | FR | MINOR | 'l'auteur de l'analyse' shifts the object from the extraction to the analysis | '95e percentile de la distribution nulle appariée, environ 0,39 (extraction de la personne qui l'a produite)' |
| B1 | DE | MINOR | 'Ersteller der Analyse' same shift; generic masculine | '95. Perzentil der gepaarten Nullverteilung, etwa 0,39 (Extraktion der Person, die sie erstellt hat)' |
| B1 | ES | MINOR | 'quien produjo el análisis' same shift | 'percentil 95 de la distribución nula emparejada, aproximadamente 0,39 (extracción de quien la produjo)' |
| B2 | DE | MINOR | 'Etiketten' reads as stickers; field term for US drug labelling is 'Kennzeichnung/Labels'; comma splice | '... Die Linie ist hier nicht verfügbar; ob sie erhältlich ist, ist nicht bekannt; Magnesium: US-Labels (Kennzeichnung) nach Namen, Italien nicht geprüft.' |
| B2 | ES | MINOR | 'etiquetas' is a calque; 'etiquetado' is the field term (register only, optional) | '... magnesio: etiquetado de EE. UU. por nombre, Italia no verificada.' |

Delegate's notes: the B1 MINOR verdicts rest on one point (the Italian names the producer of the extraction); B2 verdicts are register-only and optional; B3 ES and the new label B4 in all four languages FAITHFUL. Could not read: nothing.

## What was applied (orchestrator)
All five corrected wordings applied verbatim (the delegate's own wording, no new interpretive sentence, so no third check). Final state of the six: see `view/i18n/content_{fr,de,es}.json` hashes 2def981c1485 and 95f673af346c.
