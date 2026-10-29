# IT7 P7 independent verification: physician view extended with the pilot outputs, and the redistributable package

Verifier (not the implementer). Tree under test: branch task/it7-p7, HEAD a69884aa. Own headless Chromium with a hand-written DevTools client
(no use of the implementer's scripts for the browser measurements); own recomputation of every number from the census files. Read-only except this report.

## Verdict

PASS with defects. No blocker. The numbers are right, the package hashes are right, the audit passes, the test suite passes (145 tests, OK),
no horizontal overflow at any width. The defects are about legibility of two tables at 360 px, one visible inconsistency between the context
legend and four authored verdicts, a model line that drops its reason, English residue in an Italian page, and a few Italian corrections.

## 1. Browser (own client; mobile emulation at 360 and 390, desktop 1280)

Routes measured on index.html and index_shareable.html: no hash, #selection, #hypotheses, #predictive, #contexts, #section=selection, #section=hypotheses, #section=predictive.

| Width | scrollWidth vs innerWidth, all 8 routes, both files | Elements wider than the viewport outside a scroll container |
|---|---|---|
| 360 | 360 / 360 | 0 |
| 390 | 390 / 390 | 0 |
| 1280 | 1265 / 1280 (scrollbar) | 0 |

A4 print of each section route (print media, preferCSSPageSize): selection 4 pages, hypotheses 9 pages, predictive (with the context comparison) 5 pages.

Screenshots at 360 px read (selection, hypotheses top, predictive and contexts tail):
* Prose, cards, the three separated blocks of a hypothesis and the funnel indicators are legible, with good type size.
* DEFECT (medium): two tables are not usable at 360 px although nothing overflows, because the columns are squeezed and words break mid-word.
  The "overlap of the two methods" table of the selection section breaks its headers and numbers ("entr/am/bi", "rec/ord", "2.8/94", "11.34/0", "15.24/2").
  The context comparison table breaks its row names ("Trascri/tti", "OXPH/OS") and the verdict chips ("disc/ord/ant/e", "non/risol/to"), one letter group per line.
  Fix: below about 480 px render these two tables as stacked cards or give the table container horizontal scroll with a fixed first column.
* Tap targets (low): measured on the section routes, the "details" summaries are 21 to 23 px high, below the 24 px WCAG 2.2 minimum and well below 44 px; in the full view in-text links are 15 to 22 px high.
  The two top buttons ("Torna alla vista", "Stampa o salva come PDF") are fine.

## 2. Numbers recomputed from the census files and the catalogue

From record_usability.tsv.gz and counts.json (P2), results_summary.json and e1_p47t_summary.json (P3), context_matrix.tsv (P4):

| Shown | Recomputed | Result |
|---|---|---|
| 44,211 records / 40,268 families | 44,211 / 40,268 | match |
| target row 24,423 / 23,425; stated action after rules 16,362 / 15,447 | same | match |
| M-net usable 14,125 / 13,379 | same | match |
| M-sig any context 2,478 / 2,310; neural 1,008 / 931 | same (extended equals strict) | match |
| 7.8 percent of 11,899 testable | 931 / 11,899 = 7.82 percent | match |
| UNKNOWN_NO_STRUCTURE_KEY 28,969 / 28,369; reasons 22,557 + 4,691 + 1,219 + 502 | sums to 28,969; 28,369 + 11,899 = 40,268 | match |
| Overlap table (records 376 / 2,894 / 632 / 11,340 of 15,242; families 578 / 2,410 / 353 / 8,558 of 11,899) | records both 376, net-only 2,894, sig-only 632; families both 578, sig-only 353; both rows sum to the denominators | match |
| Evaluated 0 / 256 / 8 | counts.json funnel actually_evaluated 0; nU 256; 256/595 = 43.0 percent; 256/40,268 = 0.6 percent | match |
| SIG rho 0.143, 90 percent interval 0.039 to 0.243 | 0.14295; bootstrap90 0.0393 to 0.2428 | match |
| NET-EXT 0.047, REF-1 -0.085, NET-WWOX minus NET-EXT -0.0015 | 0.04744; -0.08543; 0.04594 - 0.04744 = -0.0015 | match |
| P47T hippocampus D 0.329, null 95th percentile 0.389, exact one-sided p 0.060 | D 0.3292; p95 0.3885; p 0.0595 (15 of 252) | match; the page shows only the producer value, the 0.396 verifier value is not shown (see defect 9) |
| Context matrix: 182 cells (13 x 14), 93 measured, 89 unknown | 182 rows; 89 UNKNOWN; 93 other; 6 models by the declared mapping | match; per-quantity higher / lower / no-sign / unknown columns also match the TSV |

Authored context verdicts, judged independently at the level of models (organoid, shRNA line, mouse deposit, fly, rat, P47T) from the TSV:

| Quantity | Authored | My reading | Agree |
|---|---|---|---|
| Q02 ISR target set | discordant | organoid lower, shRNA higher | yes |
| Q09 mitochondrial translation | discordant | lower and higher resolved, also inside the mouse deposit | yes |
| Q13 glial reactivity | discordant | higher (mouse null, P47T), lower (rat) | yes |
| Q14 hyperexcitability | concordant | higher in organoid, mouse deposit, P47T (rat sign only); 3 of 4 models | yes |
| Q12 myelin | single system | lower in the mouse deposit only | yes |
| Q01 ATF4 mRNA | unresolved | only lower_sign_only in mouse, no resolved sign | yes |
| Q08 OXPHOS | unresolved | lower_non_specific, not attributable | yes |
| Q03 ISR protein | no data | one model (fly) measured | yes, but see inconsistency below |
| Q04, Q06 | concordant, no signal | all measured cells inside noise | yes in substance, label issue below |
| Q05 glycolysis | unresolved | higher in organoid and fly (amyloid arm), none opposed | disagree with the page's own legend (below) |
| Q07 lactate / ATP | no data where needed | lower in shRNA line, higher in fly amyloid arm: opposed resolved signs | disagree with the page's own legend |
| Q10, Q11 | unresolved | opposed resolved signs across shRNA, mouse null, patient organoid | defensible on composition grounds, not by the page's own legend |

Thirteen of fourteen are defensible; none is plainly wrong. The problem is internal consistency (defect 3).

## 3. Content truth of "Ipotesi a confronto" (9 records)

Confirmed: priority, model position and observed evidence are separate blocks in every card. Priority shows the F/C/P position and the work-order reason and says it is not a statement about efficacy.
No score, no ordering, no calibrated probability, no percentile (the page states that the percentile is not shown at all). No recommendation. A grep of the section for dose, mg, rank, score and "recommend" found none used as a claim.
The model line is "nessun vantaggio dimostrato, esplorativo" only for CMP-04 and CMP-05; the other seven say "il modello non si applica a questa ipotesi (non valutata)". The sentence that a share of linked pathways is not a share of disease treated is present in the selection section.

Logic of "does not apply", checked against the P5 record text:
* CMP-01 and CMP-02: justified (not in the P3 universe, card-linked firewalled out, protein fate rather than a transcript module).
* CMP-03 (gene addition), CMP-06 (diet), CMP-08 (an ion, no signed target row): justified.
* CMP-09 (glia, not the glycolysis module): justified.
* CMP-07 (NMDAR): the record says memantine and perampanel are usable by the network method but firewalled out of P3. "Does not apply" is true for the question (receptor physiology, not a transcript module) but "non valutata" hides that these compounds are in the usable census.
* CMP-05 (PDK inhibition): DEFECT. The P5 source says "DCA is card-linked and firewalled out of P3 ... No model position for this compound." The page nevertheless puts the P3 negative on this card ("nessun vantaggio dimostrato"). It is a statement about the comparison of methods on the glycolysis module, not about the compound; for CMP-05 the source gives no model position for the compound.
* The card-linked firewall is NOT explained on the page. In the source, the reason (card-linked families were firewalled out of every method) sits in the model line; the page keeps only "il modello non si applica ... (non valutata)" with no reason, and strips the firewall token from the visible text. A physician cannot tell "outside the question" from "excluded by rule". Add one reason line per card, and one sentence in the intro explaining the firewall (a compound with a card was kept out of the method comparison on purpose, so the comparison could not be tuned on the compounds the cards already discuss).
* The model block has no definition of what "posizione del modello" is; "nessun vantaggio dimostrato" can be read as "the drug has no advantage". Suggested: "il confronto dei metodi (P3) non ha mostrato un vantaggio nell'ordinare i composti; esplorativo; non è un giudizio sul composto".

Other content findings:
* The section says "potenza ed esposizione non sono riportate in questa versione", but the English card text carries concentrations and efficacy-like numbers from external precedents: "toxicity ceiling near 4 mM", "from tens of uM", "1.3 mM Mg2+", "effective at more than 80 percent of the 27 tested ... variants", "up to 73 percent within two weeks in 75 pooled patients", "urinary oxalate +22 percent", "dose-limiting". They are labelled external or abstract-level, but they contradict the sentence and the 73 percent and 80 percent items read as efficacy figures. Either remove or move them to the details with an explicit "not WWOX evidence, not a dose".
* The F3 / C / P chips are positions, but "F3" on a phone (no tooltip) can read as a rank. Add the one-line key (F = favourable hypothesis, 3 = from the target, not tested in WWOX) in the intro.
* Context legend defines "Concordante" as the same resolved sign in at least two models, yet Q04 and Q06 are shown as "concordante: nessun segnale" (no resolved sign anywhere). Use a separate label, "nessun segnale in nessun sistema misurato", and note that small arms give low power.

## 4. Deployment package and proposal

* File set and hashes: all 13 files recomputed with sha256sum and byte counts: every row of the DEPLOY.md table matches (index.html a4fd47c3..., 2,459,077 bytes, identical to index_shareable.html; manifest.json e565d6e7...). The manifest lists every file except itself, and the workflow handles that case.
* The proposal is safe as written: single trigger workflow_dispatch; lives under view/, not .github (this commit touches nothing under .github; the only existing workflow is the pre-existing release gate); no secrets, no third-party service, no spend, no account creation; verify job fails on any extra file, digest mismatch or absent required file; deploy needs verify.
* Package content: audit-shareable --dynamic run myself: index_shareable.html PASS (0 violations) and shareable_package/index.html PASS (0 violations). Class B content is present and declared: twelve ChEMBL records in a separate CC BY-SA 3.0 file with licence text and credit. No class C text found: counts-only sources are not embedded; a 400-name random sample per origin (DGIdb-only, MATRIX-only, openFDA-only, ChEMBL) found no catalogue name from a withheld source other than a few that occur in the page's own cited-literature prose (nedosiran, anakinra, digoxin), consistent with the stated prose policy. No outbound resource is loaded (no src to a URL, no fetch); the external links are licence and source pages.
* "Publishing does not change what history holds": true. The deployed site adds no history and remedies none; the statement is accurate and stated.
* The reserved decision is stated exactly: the act of external publication (enable Pages, copy the workflow, run it, attach the zip, change visibility) and any history or visibility remedy; prior approval is not extended.

Defects in the deployment documents:
* The workflow header cross-references "DEPLOY.md, section 8" for the operator act; the act is in sections 6 and 9 (section 8 is the rollback). Fix the reference.
* Least privilege: the workflow sets pages: write and id-token: write at the top, so the verify job also receives them. Move them to the deploy job.
* The verify job checks the package only against its own manifest.json, which sits in the same directory: a changed file with a regenerated manifest passes, and manifest.json is never checked. It does not run audit-shareable or the release gate. DEPLOY.md should say that the audit is a manual precondition (it does, section 7) and that the verify job is an integrity check, not a content check.
* The github-pages environment normally restricts deployments to the default branch: say that the workflow must be dispatched from the branch that holds it, after landing.
* Rollback: complete for the Pages route and the zip route; add "disable the Pages source" next to "Unpublish site" (the label of the control depends on the Pages source type and could not be verified offline) and that Actions artefacts and the deployment history remain until deleted.
* Precondition missing: a search-engine decision. The page carries no robots meta; a public Pages site is indexable. Decide on a noindex meta before publication or accept indexing explicitly.
* Preconditions otherwise correct; the section 6 note that the package README and manifest still say "local preview, not published" is true (README line 1 and 5, manifest perimeter) and must change in the same commit as the decision.

## 5. Test suite

framework/scripts/test_repurposing_view.py with the catalogue cache set: Ran 145 tests, OK (430 s). Resource warnings about unclosed sockets in the viewport test only.

## Severity-ranked defect list

1. MEDIUM - CMP-05 card carries the P3 negative as its model position although the source says there is no model position for the compound (firewalled out). Fix text or label.
2. MEDIUM - The card-linked firewall and the reason for each "il modello non si applica" are not shown or explained; "non si applica" and "non valutata" are conflated (CMP-07). Add a reason line per card and an intro sentence.
3. MEDIUM - Context legend vs verdicts: "Concordante" requires a resolved sign in two models, but Q04 and Q06 are labelled concordant with no sign; Q05 (higher in two models, none opposed) is "non risolto"; Q07, Q10, Q11 have opposed resolved signs yet are not "discordante"; Q03 (one model) is "nessun dato" while Q12 (one model) is "un solo sistema". State that verdicts are an authored reading and give the reason per quantity, or align labels with the legend.
4. MEDIUM - At 360 and 390 px the method-overlap table and the context table break words mid-word and are hard to read, although nothing overflows.
5. LOW-MEDIUM - "Potenza ed esposizione non sono riportate" is contradicted by concentrations and percentage figures in the English external-precedent text (4 mM, tens of uM, 73 percent, 80 percent, +22 percent).
6. LOW - Page is a mix of Italian and raw English tokens: the context matrix cells show no_resolvable_sign, UNKNOWN, set_dependent, lower_non_specific; quantity names and all card prose are in English; a placeholder "un registro del repositorio" appears inside an English sentence. Disclosed at section level, but the matrix tokens should be translated.
7. LOW - Workflow: top-level pages/id-token write permissions for the verify job; wrong section reference (8 instead of 6 and 9); tags not pinned to SHAs (stated); default-branch environment rule not mentioned; no noindex decision.
8. LOW - Tap targets of 21 to 23 px (summaries) and 15 to 22 px (in-text links).
9. LOW - P47T null 95th percentile is shown as 0.389 only; the verifier draw (0.396) is in the P5 record but not on the page, although with 252 exact assignments the percentile should not depend on a draw: state which it is.

## Italian corrections (concrete)

* "Iperecitabilità di rete" -> "Ipereccitabilità di rete" (double c).
* "deposito murino P17" -> "dataset murino (P17)" or "serie di dati murina (P17)" ("deposito" is a calque of "deposit").
* "mosca" -> "Drosophila (mosca)"; "ratto" ok.
* "95° percentile del nullo appaiato" -> "95° percentile della distribuzione nulla appaiata" ("nullo" is not a noun).
* "furono registrati" -> "sono stati registrati"; "ha ricongelato gli input" -> "ha congelato di nuovo gli input".
* "Pronti per un test con nome non significa consigliate" -> "«Pronta per un test con nome» non significa «consigliata»" (agreement with "schede").
* "Presenti nel catalogo non significa valutati" is acceptable as a heading; in the body use "Essere presenti nel catalogo non significa essere valutati".
* "Effetto osservato (L3)" and "Recupero osservato (L4)": the L3 and L4 codes are unexplained to a physician; add the plain meaning or drop the codes.
* "IC90" -> write once as "intervallo di confidenza al 90%" before using the abbreviation.
* "Concordante: nessun segnale" -> "Nessun segnale in tutti i sistemi misurati".
* "Quantità più alto più basso nessun segno sconosciuto" column header row is clear in the table but reads as a sentence to a screen reader; add "n. contesti" to the headers.
