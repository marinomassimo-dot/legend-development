# Independent verification of the redesigned physician view (P12), 2026-10-29

Producer: scientist-d. Verifier: independent subagent with its own DevTools-protocol client (no sandbox-bypass flag). Verdict: viewport measurements reproduce exactly (360/360 and 390/390 with mobile emulation; scrollbar-only differences without); funnel, access and letters match the data; four medium and four low defects and a list of Italian wording fixes sent to the producer.

# P12 independent verification (scientist-c), 2026-10-29

Read-only. Own CDP client (stdlib; Chromium /snap/.../chrome --headless --remote-debugging-port=0, NO sandbox-bypass flag; it starts fine here). Scripts and raw dumps are in .../scratchpad/v/ (cdp.py, t3.py = viewport measurement, t8.py = letters check, exp_*.pdf/txt = exports).

## 1 Viewports (own measurement, both index.html and index_shareable.html, identical results)

Method: Emulation.setDeviceMetricsOverride (mobile true for 360/390 rows marked mob), then window.innerWidth and document.documentElement.scrollWidth after load + 0.4 s. Scenarios: first screen; thread filter (hash `#c=thread:Network%20excitability`, and `#c=thread:Symptom-level` by clicking "Esplora questo filone"); comparison (`#compare=C01_aav9_wwox,C02_splice_aso`; also 4 cards at 360); export (`#export=C01_aav9_wwox`, and two-card export); technical drill-down (`#technical` opened plus every inner details opened).

| Requested | Mobile emu | innerWidth / scrollWidth | Scenarios (5/5 each, both files) | Overflow |
|---|---|---|---|---|
| 360 | yes | 360 / 360 | first, thread, compare, export, export x2, tech | none |
| 360 | no | 360 / 345 | same | none (scrollbar 15) |
| 390 | yes | 390 / 390 | same | none |
| 390 | no | 390 / 375 | same | none |
| 1280 | no | 1280 / 1265 | same | none |

Verdict: the producer's table reproduces exactly (360/360, 390/390 mobile; 345 and 375 non-mobile; 1280/1265). scrollWidth never exceeds innerWidth. Element-level check at 360 mobile: no element protrudes past the viewport outside a scroll container. Contained inner scrollers only: wide tables in the (closed) technical details (TABLE.tbl 362/438/400 > 288) and the 4-card comparison wrapper (328 > 306). Acceptable.

## 2 Content vs data

Funnel (page, data-k attributes and visible text) vs coverage/coverage_summary.json: records 44,211 (units.catalogue_records), families 40,268 (units.families), families target listed 1,180 (families_target_listed), families with stated action 594 (families_with_stated_action_on_a_need_target), cards 33, record-level 1,218 (records_target_listed) and 630 (records_with_stated_action_on_a_need_target): ALL MATCH. Percentages 2.9% (1180/40268) and 1.5% (594/40268) correct. The page labels the units on each row, says "le schede non sono una frazione delle famiglie" and "Una famiglia non è un farmaco distinto": records, families and cards are never conflated.

Access vs catalog/catalog_stats.json (access_category_overlapping_counts): supplement 238, OTC 906, prescription 2,101, experimental 13,021, unknown/unverified 28,234; denominator 44,211: ALL MATCH. Note: unknown is 63.86%, the page prints 63.9% (the brief said 64.0%; 63.9 is the correct rounding). Overlap is stated (bars do not sum), "US evidence only" and "sconosciuto = non ottenuto, non non disponibile" are stated.
- Low: the access note says the US-only evidence comes from "openFDA, NIH DSLD, ChEMBL, MATRIX". ChEMBL (the source of "sperimentale", 13,021) and MATRIX are not US-specific, so "US" is imprecise for that category. Smallest fix: wording "evidenza di accesso da openFDA/DSLD (USA) e da ChEMBL/MATRIX (non specifiche di un paese)".

Priority letters vs `repurposing_view.py positions` (LEGEND_CATALOG_CACHE set): for all 33 cards, in both files, the multiset of letters in the profile "Perché ha questa lettera" equals the positions output (0 mismatches); the needs x interventions tables hold 48 cells with F1 2, F2 5, F3 7, C1 1, C2 2, C3 4, P1 16, P3 11 = exactly the 48 positions. Thread tiles (e.g. Ripristino: F1x2 F3x2 P1x6 P3x1; Sintomi: C2x2 C3 F2x3 F3 P1x4 P3x2) match the positions grouped by need family.

Defect D1 (medium, counts): the goal tiles ("Motivo della priorità" under "Recupero ampio" F x4 P x7; "Beneficio parziale" F x10 C x5 P x18 = 11 + 33 = 44) omit 4 of the 48 positions: cross-goal links (card goal differs from need goal): A51 on MYC C1, AAV9 endpoint families on glycaemia C2, and a P1 and a P3. Two of the four are counter-evidence. Nothing says so. Smallest fix: count positions by need goal (deep F4 P7 + C1 C2 P1 P3 ...) or add the line "4 legami candidato-bisogno incrociano i due obiettivi e non sono contati qui".

No pathway counts are shown as efficacy: charts section says explicitly "Nessun grafico misura l'efficacia: il numero di vie biologiche ... non entra in alcuna priorità"; observation counts per scope are labelled "volume di osservazioni, non forza di prova".

Low: view/README.md revision-3 history line still says "630 records / 603 families"; the data and page say 594 families.

## 3 Italian (physician register)

Generally clear, correct and consistently Italian for orientation text; scientific text left in English as intended. The letters legend explains F/C/P as reasons to study, not probability ("non quanto funzioni: non è un punteggio né una probabilità"; F1: "È un controllo della qualità di lettura, non la misura di un effetto"). Concrete fixes (most to least important):

1. C legend: "va chiarito prima di sperare" -> "va chiarito prima di considerare l'ipotesi" (emotional register; "sperare" itself suggests an expected benefit).
2. P3 explanation, garbled: "...nessuna controprova da fuori WWOX da chiarire, e o nessun sostegno favorevole registrato per questo bisogno o nessuna osservazione..." -> "...nessuna controprova da chiarire da fuori WWOX, e inoltre o manca ogni sostegno favorevole per questo bisogno o manca ogni osservazione in sistemi WWOX sul bisogno." (appears in every P3 profile and tooltip).
3. "controprova" for counter-evidence: in Italian "controprova" usually means a verification/check of a result ("fare la controprova"), so "Controprova da chiarire" can read as "check to do". Keep only if the operator wants it; safer: "Evidenza contraria da chiarire" (letters legend, C1-C3 labels, "4. Controprove" -> "4. Evidenza contraria", "Controprove: 14 voci" -> "Evidenza contraria: 14 voci").
4. "prova" is used for evidence, experiment and proof: "su quali prove", "Tipo di prova", "Prova mancante" (section 5, whose body says "Dato mancante"), "Prova mancante e prossimo esperimento". Use "evidenza" for evidence ("Tipo di evidenza", "Evidenza mancante") and keep "prova/test" only for tests. "Prove, per tipo" (export) -> "Evidenza, per tipo".
5. "scheda" is used for both a thread summary ("Ogni scheda riassume un gruppo di bisogni") and a candidate card ("33 schede candidato"). Rename the thread unit "riquadro" or "filone".
6. Number agreement: "Controprove: 1 voci" -> "1 voce"; "(1 esiti in sistemi WWOX" -> "1 esito"; "1 scheda/e" (export) -> "1 scheda"; "(7 di cui astensioni)" -> "(di cui 7 astensioni)"; "una indicazione di trattamento" -> "un'indicazione di trattamento"; "Obiettivo: 5 bisogni recupero ampio" -> "5 bisogni di recupero ampio"; "Obiettivo di recupero: Obiettivo: Beneficio parziale utile" (doubled label in the comparison table).
7. Gender: "Vigabatrin da sola copre" -> "da solo" (it is masculine; same for "Ketogenic diet" which is English and fine as a title, but the sentence needs the right form, e.g. "copre da sola" only for diet).
8. Mixed language in the comparison: "incerta su inhibitory drive onto pyramidal neurons", "ridurre su seizure/spasm burden", "ripristinare su myelin formation / maturation": either keep the whole target phrase in English in quotes or translate; "su" is ungrammatical here ("direzione voluta: ridurre, su ...").
9. "Nessun risultato di assenza è una conclusione sulla biologia" -> "Un dato assente non è una conclusione sulla biologia".
10. Raw codes in the header warning: "DGIdb: STALE_EXPORT ... PARTIAL" -> "esportazione non aggiornata" / "parziale" (keep the code in the technical details).
11. "bisogno" for "need" is ambiguous to a clinician (unmet clinical need). It is defined once on the first screen; consider "obiettivo biologico" or a short gloss next to the first use. Also "Perché lo studiamo" (first person plural) -> "Perché è in elenco".
12. "La scheda è un'astensione: manca un dato prima di poter disegnare un test" -> "progettare un test". "sperimentale" (access category) is ambiguous (experimental use vs trials) -> "in sperimentazione".
13. Stray label "bisogno:" opening items in "4. Controprove" (profile and export): remove or write "Bisogno: ...".
14. Matrix cell words: F3 cells say only "favorevole", although F3 means "from the target, never tested in WWOX"; C cells say "controprova", P "manca premessa". Use the short forms "ipotesi dal bersaglio" for F3 and "ipotesi, esito WWOX debole" for F2.

## 4 Safety of claims

- No dose, mg, schedule, route found in the body text (regex over the whole shareable and full pages). Cards say "no dose, route or schedule" explicitly. No "efficace", "guarigione", "cura" (only "team clinico curante"), no score or cure ranking; "non è un punteggio né una probabilità" is on the first screen and in the priorities text.
- "Non è un consiglio medico" is visible without scrolling: at 390x844 the header line "Materiale di ricerca, non consiglio medico né graduatoria di trattamenti" is at y=66-119 and the fuller "Da tenere presente" paragraph at y=603; at 360x780 header y=66-137 and the fuller paragraph at y=621-656 (inside the 780 fold); at 1280x900 y=304. OK on all three.
- Source-state warning (DGIdb STALE_EXPORT, DSLD PARTIAL) is compact and above the fold (y=129-144 at 390), but shown as English codes (fix 10).
- Letters legend: F at y=745 (390x844) is on the first screen, C and P below the fold; at 360x780 even F is below it (y=783). Low: the first thread cards start at y=1091. Smallest fix: put the one-line "F / C / P = motivo per studiare, non probabilità" right under the disclaimer.
- Residual risk (low): drug names appear next to "F1/F3" immediately in thread tiles. Disclaimers are close and the legend defines F as a reason to study; the 'favorevole' word in matrix cells (fix 14) is the stronger risk: "favorevole" next to a drug name for an F3 cell, where no WWOX observation exists.
- Counter-evidence is not hidden: C cells, "Controprove" sections, safety signals (VABAM for vigabatrin) are present in profile, export and comparison.

## 5 Paths (walked at 390x844 mobile, CDP clicks/hash)

1. First screen -> thread "Sintomi" (partial benefit: "Obiettivo: 0 bisogni recupero ampio, 2 bisogni beneficio parziale") -> click "Esplora questo filone": hash `#c=thread:Symptom-level`, 13 candidate cards visible, scroll to the navigation block; innerWidth/scrollWidth 390/390. Works.
2. Click candidate link `a[data-open=EB-VGB-01]` (vigabatrin, C2 + P3): profile opens at the six numbered answers (1 Perché lo studiamo, 2 Risultato in WWOX, 3 Precedente esterno o previsione, 4 Controprove, 5 Prova mancante, 6 Prossimo passo), then "Perché ha questa lettera, bisogno per bisogno" and the closed technical block. The six answers are present and short enough; details are one click away ("5 altre nei dettagli tecnici").
3. Main counter-evidence: section 4 shows the safety signal (VABAM, harm on an endpoint other than the pursued one) and the prose "Pro/Contra" line. Works. Defect D2 below.
4. External precedent vs WWOX result: section 2 lists WWOX rows (scope glyph + label: "Caso clinico WWOX (non controllato)", "Esperimento WWOX in un sistema DEE") and says "provato in un sistema WWOX"; a separate "Osservazioni sui bisogni collegati ... possono riguardare altri interventi" is folded in a details. For a card with outside-WWOX data the difference is carried by the scope glyph/label only. Defect D3 below.
5. Export: "Esporta questa scheda" -> `#export=EB-VGB-01`. Printed to PDF via Page.printToPDF (A4, CSS page size): pdfinfo says A4 (595x842 pt), pages: EB-VGB-01 4, C01_aav9_wwox 3, E01_isr_modulators 4, EB-ETX-01 3, D01_a51 3 (matches the producer's "4 PDF pages"). Export at 390 and 360 has no horizontal overflow. Links: 2-12 per export, all https to pubmed.ncbi.nlm.nih.gov, doi.org, www.ebi.ac.uk (ChEMBL); zero non-http hrefs, no repo-relative path in the visible text (regex for `../`, `disease-models/`, `*.md/json/tsv` found none). Banner says "I collegamenti sono identificativi pubblici e restano validi fuori da questa cartella". Same in the full and shareable files.

### Defects (severity, smallest fix)

- D1 (medium) goal tiles drop 4 of 48 positions (see section 2). Fix: count by need goal or print the note.
- D2 (medium) Export and profile are not self-contained off-folder: card prose carries unexplained internal tokens ("CLAIM 001", "CLAIM 031", "A-VGB-5", "T1", "the bridge", "blind audit", "no receipt in the ledger", "DR-AAV-GFAPAREA-LD"). The export itself admits it (last Limiti line: "solo gli identificativi nella tabella delle fonti sono pubblici") but a recipient cannot decode them. Fix: a one-line gloss in the export footer ("CLAIM n, A-xxx-n, DL-..: riferimenti interni, non necessari alla lettura") or strip internal ids from the exported prose. Also the Limiti list mixes Italian and English lines (three English sentences: "Technical comparison is not efficacy...", "Sources and receipt references are retained...", "Shared sources are not independent confirmations; scores are not pooled").
- D3 (medium) For vigabatrin section 3 "Precedente esterno o previsione" contains WWOX human case reports (developmental outcome at two years, seizure control on vigabatrin with the ketogenic diet; "human, WWOX-null class") and WWOX organoid computations, i.e. WWOX material under a heading that reads as "external precedent", with the scope shown as "– Tipo di prova non registrato a livello di affermazione". The WWOX/external distinction the page promises is therefore blurred for this card. Fix: where the scope is unrecorded but the system tag says WWOX, show it in section 2; or rename the heading "Altro (precedente esterno, previsione o tipo non registrato)".
- D4 (medium) Matrix cell wording "favorevole" for F3 (and the legend sentence in fix 14): can be read as a favourable result for the drug in WWOX. Fix: "ipotesi dal bersaglio".
- D5 (low) Italian number/grammar/mixed-language items (section 3 items 2, 6, 7, 8, 13) and English status codes in the header warning.
- D6 (low) Letters legend (C, P) below the fold at 390x844; at 360x780 F as well.
- D7 (low) Access note calls ChEMBL/MATRIX evidence "US".
- D8 (low) view/README.md history line says 603 families (now 594).
- Not defects: raw overflow numbers, A4 page counts and links all hold. The shareable file's graphic 4 is empty by design and says so.
