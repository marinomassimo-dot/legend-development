# Paper Registry Current

> **Public edition — de-identified.** Disease-level registry from public literature. All individual-linking data removed (names, geography, report/sample IDs, dates, parent-of-origin, cell-line ownership). Specific variants appear only as decoupled disease-model worked examples drawn from public literature, never as one persistent individual's inherited alleles. Some entries remain in their original language. Not medical advice.
## WWOX Paper Registry
**Version:** v1.8.2
**Date baseline:** 2026-03-28  
**Last update:** 2026-09-26 — `BATCH_20260926_ALDAZ_R4` (PAPER 032/053 evidence boundary and receipt updates; PAPER 103 linked to CLAIM 026). Prev: 2026-09-26 — `BATCH_20260926_ALDAZ_R2` (registry-only completion of recovered VPS readings; canonical P6 legend and Mirror corrections). Prev: 2026-09-22 — `BATCH_20260922_BIBLIO` (**traceability repair, no scientific change**): `PAPER 011`'s Journal/source line expanded `OMTA` as *Molecular Therapy - Methods & Clinical Development* — a **different Cell Press journal** (`omtm`) — and so contradicted the correct name already printed on the Identifier line directly beneath it. Now ***Molecular Therapy Advances*** (`Mol Ther Adv`, DOI code `omta`) in both places. **No note, boundary, number or evidence-depth field changed.** Prev: 2026-07-25 — `BATCH_20260725_001` (public audit, **traceability repair, no scientific change**): the historical CLAIM 028 source typo 213→207 was resolved against the tracking log and CORPUS P207; the superseded 213 pointer remains visibly withdrawn in the batch summary. Prev: `BATCH_20260725_DEPTH` normalized PAPER 005 evidence-depth metadata without scientific change. Prev: 2026-07-10 — URG_2026-07-09_001 category 5 invalidated the retracted/dependency-contaminated source line without affecting a baseline claim.

---

## Purpose
Canonical registry of papers already integrated or baseline-linked in the WWOX system.

### Status values
- discovered
- screened
- filtered_in
- filtered_out
- processed
- claim_linked
- integrated
- flagged_for_review
- background_only
- superseded

### Rule
A paper found is not yet a paper processed.
A paper processed is not yet a paper integrated.
A paper integrated is not necessarily a paper that changes BLOCCO 1.

### Pathway-code legend
The canonical P1–P7 codes follow the WWOX working model and claim registry. **P6 = neuroinflammation / glia** (for example `PAPER 007`, `PAPER 114`, `CLAIM 006`). DNA-damage response and genome stability are described by name, without a P-code; `P9` is not a canonical code. Historical FASE-1 triage entries that say `P6 — DDR / genome stability` retain their source wording for audit, but the label's words, not that legacy code, determine their topic. New and reassessed records use this legend.

---

## PAPER 001
**Short title:** Steinberg 2024 organoids
**Full title:** WWOX deficiency impairs neurogenesis and neuronal function in human organoids
**Authors:** Steinberg et al.
**Year:** 2024
**Source type:** preprint / organoid study
**Journal/source:** bioRxiv
**Identifier:** preprint
**Status:** superseded
**Primary pathway:** P1 — Ca²⁺ / network dysregulation
**Secondary pathway:** P3 / P7
**Model/species:** human organoids
**Genotype/model:** WWOX-KO + WOREE-derived WWOX-deficient models
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 002
**Role:** core baseline paper
**Note:** key paper for network dysregulation, radial glia, MYC, AAV rescue. 🔵 **Superseded 2026-09-27 (`BATCH_20260927_004`, `CC-20260826-PROVENANCE-01` §C) by [[paper_registry_current#PAPER 094]]** — the refereed version of this work, PMID 42397075 / DOI 10.1093/brain/awag239, *Brain* 2026, read completely (`FTR-20260810-42397075-04`, manifest `deepdive_manifests/PMID42397075.json`, 30 locators). **Kept append-only and resolvable rather than merged away:** nothing measured here is withdrawn, and the preprint identity is still cited downstream. ⚠️ **What this supersession does NOT do, deliberately:** it does not move [[claim_registry_current#CLAIM 002]]'s `Source`. That repointing, and **three** of the five boundaries the refereed reading carries, are **DEFERRED** — ⚠️ **corrected 2026-09-28 (Mirror `F1`, as adjudicated): the other two boundaries were written**, as verbatim quotations in [[claim_registry_current#CLAIM 002]]’s provenance note, each cited there by receipt + manifest entry (`FTR-20260810-42397075-04`, `deepdive_manifests/PMID42397075.json` entries **13** and **20** — ⚠️ that manifest's own `receipt` field names `FTR-20260810-42397075-03`, the **partial** reading whose `outputs` first name the manifest, while the **complete** read cited here is `-04`, whose `outputs` also name it; 🟢 **decided 2026-09-28** (`framework/protocols/fulltext_read_receipt.md`, CLOSED): a manifest's `receipt` names the reading that **produced** the manifest — the **earliest** ledger event for the same study whose `outputs` name that file — so `-03` is not merely *one admissible* target but **the** correct value, and `manifest_receipt_provenance.py` does not list `PMID42397075.json` among its non-conforming manifests. The hop is intact and this conclusion is **stronger**, not weaker (ground rewritten 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 2 on `BATCH_20260928_002`, replacing *«leaves the target of a manifest's `receipt` field deliberately open — the producing reading, or the most recent one — and states that neither is a referential defect»*: that OPEN was closed 25 minutes after the last commit of the batch that rested on it)). They are persisted locators of this complete read, not unverified attestations: what is absent from this checkout is the artefact, not the reading — no artefact of PMID 42397075 exists in this checkout and PubMed returns no PMCID for it — 🔵 **true on 2026-09-27, and half-corrected on 2026-10-04** (`CC-20261004W10-Y-ARTEFACT-RECOVERY-01`): the PMCID statement still holds, but the article itself was re-acquired free from the publisher's open-access endpoint and measured to be the same document, so a body-surface triple of that reading is auditable again; the supplementary-surface triples are not, because the supplement is still unobtainable and a SHA-256 sweep of this host on 2026-10-04 recovered none of it, so the blind audit of those seven triples came back `UNVERIFIABLE_SURFACE` 7/7 **for absence of bytes, not on the merits** (`research/locator_audits/2026-09-27_wave2_audit_B.md`). Moving the foundation of a `consolidated baseline` claim onto a reading whose bytes nobody can open is the one move the locator discipline exists to prevent.

---

## PAPER 002
**Short title:** Baryła 2022 metabolism review
**Full title:** WWOX and metabolic regulation in normal and pathological conditions
**Authors:** Baryła / Kośla / Bednarek
**Year:** 2022
**Source type:** review
**Journal/source:** *Journal of Molecular Medicine*
**Identifier:** DOI 10.1007/s00109-022-02265-5
**Status:** integrated
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** review / mixed
**Genotype/model:** WWOX general biology
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Role:** metabolic/redox framework paper
**Note:** useful for HIF1A / PDK1 / ROS / ETC logic

---

## PAPER 003
**Short title:** Choi 2026 VABAM
**Full title:** Vigabatrin-Associated Brain MRI Abnormalities in Two Children With WWOX-Related Epileptic Encephalopathy
**Authors:** Choi et al.
**Year:** 2026
**Source type:** short communication / clinical report
**Journal/source:** *Pediatric Neurology*
**Identifier:** PMID 41442931
**Status:** integrated
**Primary pathway:** P2 — GABAergic vulnerability / safety
**Secondary pathway:** P4 imaging caution
**Model/species:** human
**Genotype/model:** WWOX-related encephalopathy
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** 001
**Role:** safety anchor paper
**Note:** direct human safety signal; CLAIM 001 now conflicting evidence due to You 2024 / Chong 2023 — safety position for the reference genotype unchanged

---

## PAPER 004
**Short title:** Repudi 2021 Brain myelination
**Full title:** Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects
**Authors:** Repudi S, Steinberg DJ, Elazar N, Breton VL, Aquilino MS, Saleem A, Abu-Swai S, Vainshtein A, Eshed-Eisenbach Y, Vijayaragavan B, Behar O, Hanna JJ, Peles E, Carlen PL, Aqeilan RI
**Year:** 2021
**Source type:** murine mechanistic study
**Journal/source:** *Brain* 2021;144(10):3061-3077
**Identifier:** PMID 33914858 / DOI 10.1093/brain/awab174
**Status:** integrated
**Primary pathway:** P4 — myelination / white matter
**Model/species:** mouse
**Genotype/model:** neuronal deletion
**Transferability:** T2
**clinical relevance:** MODERATE
**Claim links:** 003 · 045 · 005 (the `045` link is the heterozygote arm of the same figure set, cited by `CLAIM 045` as a proportion without a statistical test; the `005` link is `CLAIM 005`'s evidence boundary, which names this paper's Figure 1 legend as the primary behind the astrocyte- and oligodendrocyte-conditional-knockout negative) [`045` added 2026-10-03 by `BATCH_20261003_003`, closing the reciprocal-link defect class Mirror F2 named on `BATCH_20261003_001`; `005` added 2026-10-04 by `BATCH_20261004_001`, the same class. 🔴 **Every number must precede every annotation on this line:** `claim_links.declared_claim_links` stops walking at the first token that is neither a number nor a separator, and a square-bracket note is not stripped the way a parenthesis is — the first attempt at this repair appended ` · 005` after this bracket and LINT still reported `UNLINKED_SUPPORT`]
**Role:** myelination anchor paper
**Evidence depth:** `partial_fulltext_read` (**partial full text**) on the surface that can be audited today — receipt `FTR-20261003-33914858-02` (rendered browser print; its coverage map reads `results`/`methods`/`figures` read, the rest `not_read`). The earlier `FTR-20260923-33914858-01` is recorded in the ledger at **complete** depth, but on the publisher HTML that is **absent from this checkout** (see the artefact-debt note below), so this record does not inherit that depth (BATCH_20261003_003, depth read off the ledger's coverage maps). Ricevute `FTR-20260923-33914858-01` e `FTR-20261003-33914858-02`, manifest `deepdive_manifests/PMID33914858.json` (6 locator su pagina resa, validatore PASS), dossier `fulltext_dossiers/PMID33914858.md`.
**Quantità, dalla pagina stampata (2026-10-03, `CC-20261003W4-B-REGISTRY-01`), che la nota qui sotto rimandava a un PDF mai ottenuto:** assoni mielinizzati per campo nel corpo calloso a P17, S-Control 180 ± 40 contro S-KO 55 ± 35 — circa **3.3 volte**, non le «3.5–4 volte» a cui il testo corrente del lavoro arrotonda; assoni non mielinizzati nel nervo ottico 55 ± 20 contro 270 ± 60; g-ratio significativamente più alto in entrambi i tratti; oligodendrociti maturi CC1-positivi ridotti di **due volte** con OPC significativamente più numerosi; **nessuna morte oligodendrocitaria** significativa (CC1 + caspasi 3 clivata). Limite di potenza su ogni numero di spessore: l'analisi del g-ratio è potenziata a livello di assone, circa 600 assoni, 100 per topo, **n = 3 per genotipo**.
🔴 **Debito di artefatto, dichiarato 2026-10-03:** l'HTML dell'editore che la ricevuta `FTR-20260923-33914858-01` dichiara come propria superficie di testo autorevole — `files/fulltext/PMID33914858_Repudi2021_OUP.html`, sha256 `3baf27af9f906a8bfa013924a90a0eca7713b25463d6f039fddef0242caac902` — **non è presente in questo checkout**, né lo sono i cinque supplementi che quella ricevuta nomina; cercati per nome su tutta la macchina e per SHA-256 su 504 file candidati. I locator di quella lettura sono quindi **non auditabili** finché l'artefatto non rientra. La ri-acquisizione è stata ritentata il 2026-10-03 e fallisce su ogni rotta libera: OUP risponde HTTP 403 dietro Cloudflare su tre URL, non esiste PMCID, Unpaywall e OpenAlex nominano solo quella posizione bronze con `has_repository_copy: false`, e l'indice CDX di Wayback non ha alcuna cattura. Cosa sbloccherebbe: una copia dell'operatore dello stesso HTML, o un prestito interbibliotecario. 🟢 **Parzialmente sbloccato lo stesso giorno (2026-10-03, `BATCH_20261003_003`):** l'operatore ha fornito il **PDF dell'articolo** (`files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf`, sha256 `113522bb09b42a2dc0252bc1d7b112b66e3a68323ab1348c042f0ac8c8e8fa4c`, 17 pagine) con un layer di testo derivato (`PMID33914858_Repudi2021_Brain_operator_supplied.txt`, sha256 `665f777280b0476f6e5cb69997027c1b0ae0052e738a2b68fce0335ef40e7124`, `pdftotext -layout -nopgbrk`; lettere greche e segno meno sono lossy in quel layer). **I cinque supplementi e l'HTML dell'editore restano assenti**, quindi questa nota non discharge il debito: nessun locator di `FTR-20260923-33914858-01` è stato ri-ancorato qui e né il manifest né la ricevuta sono stati toccati da questo batch. Compito di lettura proposto: una nuova ricevuta con `reread_reason: inadequate_prior_coverage` su questa superficie, supplementi dichiarati non disponibili.
**Note:** justifies MRI + DTI logic. Identifier normalizzato + abstract/key-findings verificati via PubMed 2026-07-05 (CC-2026-07-05-002). Full-text PDF OA-ma-bot-blocked (Oxford advance-access) → handoff `files/fulltext/PMID33914858_Repudi2021.handoff.md` per recupero manuale; arricchimento quantitativo del claim rimandato al PDF. Reperto cross-pathway (abstract): organoidi cerebrali umani WWOX-KO mostrano iperattivazione + ipomielinizzazione → cross-link [[claim_registry_current#CLAIM 002]]. ⚠️ Duplicato corpus **CORPUS-STUB-087** (stesso DOI) → mergiare in un prossimo BATCH_COMMIT.
**Artefatto e misura, aggiornati il 2026-10-03 (`CC-20261003R-ARTEFACT-DEBT-01`, ricevuta `FTR-20261003-33914858-03`):** l'operatore ha fornito il **PDF tipografico dell'articolo** (17 pagine, sha256 `113522bb09b42a2dc0252bc1d7b112b66e3a68323ab1348c042f0ac8c8e8fa4c`) e l'**archivio supplementare completo** (sha256 `cfb264e45a6d6e2d7082853de293431594c8235cf087fbecbd0b3fcf1956c276`: metodi e nove figure supplementari, due video, tre fogli di calcolo). Il debito sull'HTML dell'editore è **superato, non saldato** — quell'artefatto resta assente, e nulla di canonico vi poggia più. Il layer di testo derivato dal nuovo PDF è **rifiutato** come superficie di citazione (screen del validatore: 24 controlli C0, più le sostituzioni stampabili note di questa rivista), quindi ogni locator dell'articolo è `rendered_text` o `figure` su pagina resa; il testo del supplemento è invece **pulito** allo stesso screen. 🔴 **Due reperti precedenti sono ritirati da questo artefatto:** la legenda della Supplementary Fig. 3, che `FTR-20260923-33914858-01` dichiarava **mancante** da File009, è **presente** nello stesso file con lo stesso sha256 (1125 burst, 149 / 834 / 142 in tre esempi S-KO, 100–200 s) — l'assenza era dell'estrazione, non del documento; e un **data-availability statement esiste** («available from the corresponding author upon reasonable request»), pur senza alcun accession, il che conferma la sostanza del reperto precedente e ne corregge la formulazione. 🔴 **Vincolo di misura su ogni quantità di mielina di questo lavoro:** tutte vengono da **n = 3 animali per genotipo** (legenda della Figura 5, pannelli (A) e (C), e legenda della Figura 4(G)), mentre ciascun pannello riporta 13–15 punti e gli asterischi sono calcolati **sui campi visivi**, non sugli animali; ⚠️ **Integrator amendment, `BATCH_20261003_005`, from the blind audit:** i numeri *n* = 2500 e *n* = 1200 della legenda della Figura 5(B) sono **assoni contati**, non animali, e non vanno citati come numerosità animale — il n = 3 per genotipo sta nelle parti (A) e (C) della stessa legenda; e i fold change del testo corrente sono gonfiati in una sola direzione — «~3.5–4 volte» misura 3.3 volte sulle medie degli autori stessi, «~6 volte» misura 4.9 volte sulle loro medie e circa 4.2 volte sul pannello a 600 dpi. ⚠️ **Integrator amendment, `BATCH_20261003_005`, from the blind audit:** il testo stampato porta la **tilde** (*«∼6-fold»*), quindi è un'approssimazione dichiarata e non una cifra esatta: ciò che si registra qui è che l'approssimazione è arrotondata **in una sola direzione**, non che gli autori abbiano affermato un valore puntuale. ⚠️ Discrepanza di digest registrata e non risolta: `FTR-20260923-33914858-01` nomina File010.mp4 con sha256 `2ef48d089be350fb3bef68799c443305b9ca9124ea318066f6a2fad8607ecb3c`, l'archivio attuale con `87ec870a96251af9ee3211d4b7b0599360d1a035c2e1cbd41ca46ced6adf52bd`; l'artefatto precedente è assente e i due non sono confrontabili.
**Wikilinks:** [[claim_registry_current#CLAIM 003]]

---

## PAPER 005
**Short title:** Repudi 2021 EMBO gene therapy
**Full title:** Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes
**Authors:** Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI
**Year:** 2021
**Source type:** preclinical gene therapy study
**Journal/source:** *EMBO Molecular Medicine* 2021;13(12):e14599
**Identifier:** PMID 34747138 / PMCID PMC8649866 / DOI 10.15252/emmm.202114599
**Status:** integrated
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260810-34747138-01`, JATS XML PMC8649866 (`structured`, sentinella `clean`), 20 locator verificati in `deepdive_manifests/PMID34747138.json` (validatore PASS, 0 gap). Chiude il debito misurato di `FTR-20260809-34747138-02`, che dichiarava discussion/methods/references `not_read` e figures `captions_only`. Prima del 2026-08-10 questo campo diceva *«full text reviewed (verified 2026-07-05, retrieved via Europe PMC)»* — una verifica di metadati e contenuti-chiave, non una lettura integrale con locator.
**Primary pathway:** P7 — gene therapy readiness
**Secondary pathway:** P1 / P4
**Model/species:** mouse
**Genotype/model:** Wwox-null
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 004
**Role:** causal strategy anchor
**Note:** preclinical, but central for trial-readiness logic; now complemented by Obeid 2026. Full text verified 2026-07-05 (retrieved via Europe PMC/PMC MCP; According to PubMed, [DOI](https://doi.org/10.15252/emmm.202114599)) — CC-2026-07-05-001; CLAIM 004 finora derivato da review, ora ancorato a fonte primaria. Dettagli verificati: singola ICV neonatale (P0) AAV9-hSynI-WWOX (murino o umano, equivalenti) recupera sopravvivenza, crescita, ipoglicemia, crisi, atassia, mielinizzazione (OPC→oligodendrociti maturi, g-ratio, corpo calloso+nervo ottico), comportamento e neuroinfiammazione (GFAP/Iba1); restauro neuronale-only → mielinizzazione non-cell-autonoma; gliosi downstream della disfunzione neuronale; ipoglicemia reversibile da restauro CNS-only; durata ≥9 mesi, nessuna leakage periferica. ⚠️ Modello Wwox-null sistemico + P0 → design-principle trasferibili, non dose/timing (genotype caution "alta", the reference genotype compound het N/M).
**Confini della lettura integrale (2026-08-10, `BATCH_20260810_005`) — tutti dai locator, nessuno inferito:**
- 🔴 **Il comparatore che manca.** Dove il rescue è confrontato con il **wild type** e non con il null non trattato, gli autori stessi lo dichiarano incompleto: *«there are still some differences between rescued and WT mice which could be attributed to an oligodendrocyte-specific WWOX function in regulating the myelination process»* (Discussion). Nei pannelli di microscopia elettronica **l'unico confronto WT-contro-rescued effettivamente tracciato è il conteggio di assoni non mielinizzati, ed è significativo CONTRO il rescue** (~26 per campo in WT contro ~52 nei trattati, `**`). Nei pannelli dove il rescue appare più forte — assoni mielinizzati per campo, corpo calloso ~130/46/105 e nervo ottico ~140/68/124 — le parentesi corrono **WT-vs-KO** e **KO-vs-rescued**, **mai WT-vs-rescued**: il divario residuo visibile non è testato. Stesso schema nella figura mielinizzazione/OPC: CC1⁺ WT ~170 / KO+GFP ~77 / rescued ~135, PDGFRα⁺ WT ~53 / KO+GFP ~87 / rescued ~70, entrambi i valori trattati **fra** KO e WT e **nessuno dei due testato contro WT**. Il g-ratio, invece, **normalizza**: la nuvola trattata si sovrappone al WT mentre quella KO resta piatta a 0.8–0.95.
- **Finestra P0, e la ragione dichiarata:** *«The limited life span and poor conditions of Wwox-null mice prompted us to treat these mice very early on in their life (P0)»*; il dosaggio post-natale è **lavoro futuro dichiarato**, non fatto. `REVIVAL_TRIGGER`: un risultato post-natale cambierebbe la lettura dell'intero lavoro. In WOREE la diagnosi segue l'esordio delle crisi di mesi.
- **Trasduzione 60–70% dei neuroni**, non quasi-totale: l'efficacia è ottenuta con un cervello **parzialmente** trasdotto. **Gli oligodendrociti non sono mai trasdotti** (co-staining CC1/anti-WWOX) — è questo che rende il recupero della mielina **non-cell-autonomo** e non un effetto diretto.
- **Dose e via, esatte:** ICV neonatale singola, *«Approximately 1 μl (2 × 10¹⁰ GC/hemisphere) virus was dispensed»*, con *«Free-hand intracranial injections»* — a mano libera, non stereotassiche.
- **n = 3 per genotipo** nella quantificazione EM (*«100 axons per mouse, n = 3 per genotype»*); elettrofisiologia **sotto ketamina/medetomidina** — il contrasto fra gruppi regge, i tassi di scarica assoluti non sono quelli di un cervello sveglio; analisi **in cieco** sul genotipo, dichiarata.
- **Il rilievo oncologico è un non-segnale in una casistica piccola, e i tre qualificatori SONO il reperto:** *«we did not detect gross tumor formation in the limited number of adult Wwox-null mice treated with AAV9-hSynI-WWOX that we examined (age 8–11 months)»*. WWOX è oncosoppressore e il restauro è solo cerebrale: i tessuti periferici restano null.
- 🟢 **Controllo positivo per la regola 5d.** Su questa superficie JATS il comparatore sopravvive intatto (*«Results were considered significant when the P < 0.05»*). La stessa frase nel PDF di **PMID 33914858** — stesso primo autore, stesso anno, stesso laboratorio — si estrae come `P 5 0.05`, comparatore distrutto, ed è la ragione per cui [[full_text_queue_current#FT-044]] è sospesa. **La politica riguarda la superficie, non il paper.**
- **Multi-hop chiuso senza debito:** 62 riferimenti enumerati, 36 gene-directed, **36 su 36 già noti** — la prima volta che accade in questo corpus.
- **Debito dichiarato:** figure dell'Appendix e review-process file non aggiudicati; `legend-locator-audit` e `legend-hypothesis-forge` sono **dovuti**, non declinati.
⚠️ Duplicato corpus **CORPUS-STUB-048** (stesso DOI) → risolto in `BATCH_20260810_005`, placeholder conservato append-only. 🔴 **Correzione:** questa nota indicava anche `CORPUS-STUB-042` come duplicato dello stesso DOI. **Non lo è** — `CORPUS-STUB-042` è PMID 35107375 (*WWOX-Mediated Degradation of AMOTp130…*, filovirus VP40), un lavoro diverso. Un placeholder innocente stava per essere assorbito in un altro record.

---

## PAPER 006
**Short title:** Hussain 2019 GABA/glia
**Full title:** Wwox deletion leads to reduced GABA-ergic inhibitory interneuron numbers and activation of microglia and astrocytes in mouse hippocampus
**Authors:** Hussain T, Kil H, Hattiangady B, Lee J, Kodali M, Shuai B, Attaluri S, Tome-Garcia J, Meghed M, Jang M-H, Shetty AK, Aldaz CM
**Year:** 2019
**Source type:** murine mechanistic study
**Journal/source:** *Neurobiology of Disease* 121:163–176
**Identifier:** PMID 30290271 / PMCID PMC7104842 / DOI 10.1016/j.nbd.2018.09.026
**Status:** integrated
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260806-30290271-01`, 2026-08-06
**Primary pathway:** P2 — GABAergic vulnerability
**Secondary pathway:** P6 — glia
**Model/species:** mouse
**Genotype/model:** Wwox-KO
**Transferability:** T2
**clinical relevance:** MODERATE
**Claim links:** 005
**Role:** pathway support (marker-level). **Not** safety support.
**Note:** do not overtranslate as "GABA forbidden" — and, since 2026-08-06, do not translate it as a medication caution either. The source measures marker-positive counts, glial area fractions and GAD65/67 protein; it measures no GABA, no inhibitory current, no E/I ratio, no seizure and no drug. `CORPUS-STUB-085` is this same paper (duplicate, resolved 2026-08-06; the stub is preserved as append-only history).

---

## PAPER 007
**Short title:** Hussain 2023 P47T
**Full title:** WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12
**Authors:** Hussain T, Sanchez K, Crayton J, Saha D, Jeter C, Lu Y, Abba M, Seo R, Noebels JL, Fonken L, Aldaz CM
**Year:** 2023
**Source type:** variant-specific mechanistic study
**Journal/source:** *Progress in Neurobiology* 223:102425 (NIH author manuscript NIHMS1957654)
**Identifier:** PMID 36828035 / PMCID PMC10835625 / DOI 10.1016/j.pneurobio.2023.102425
**Status:** integrated
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-36828035-03`; manifest `deepdive_manifests/PMID36828035.json`, dossier `fulltext_dossiers/PMID36828035.md`. Earlier partial receipts `FTR-20260826-36828035-01` / `-02` stand in the ledger.
**Identity record (BATCH_20260926_ALDAZ, 2026-09-26):** until this batch the record carried an invented `Full title` (a restatement of `CLAIM 006` + `CLAIM 007`, not the title of any article) and no identifier, so an identity query for PMID 36828035 could not reach it. Normalised from the article XML. The same paper is also `PAPER 112` (registered by `BATCH_20260926_ALDAZ_R1`) and `CORPUS-STUB-053` → `PAPER 112`; both are kept append-only and point here. Transferability and clinical relevance are unchanged by this normalisation: the proposal to raise clinical relevance to MODERATE (CC-20260826-PROVENANCE-PAPER007-01 §3.B) is not adopted: the field rates relevance to the reference genotype, both claims this record carries hold P47T ≠ Q230P and stay T3, and the paper's value as the corpus's electro-behavioural seizure dataset for a long-lived WWOX mouse is carried by `CLAIM 037`, not by this field.
**Survival boundary — cite the CURVE, not the text's mean (`CC-20260826-PMID36828035-02` §6.3, verified at source 2026-09-27).** The running text gives a **mean long-term survival of 393 ± 32 days** for the homozygote against **495 ± 23** for the heterozygote and **542 ± 8** for wild type, and the caption reports the test over a cohort of **n = 14 / 30 / 25** with **log-rank p = 0.001**. 🔴 **The mean and the plotted curve are not reconcilable at face value**, and the paper states no computation rule for the mean: Figure 1b runs to 600 days with about **26 % of homozygotes still alive at the last plotted day** and a 50 % crossing near **470–500 d**, while **wild type itself ends near 0.90, not flat at 1.0** — so "comparable to wild type" has a moving comparator here too. Any canonical use of this dataset quotes the curve, the three cohort sizes and the log-rank value; a bare "mean survival 393 days" understates the homozygote's tail and hides the comparator's own decline. Locators: `deepdive_manifests/PMID36828035.json` entries 13–15 (text), 18 (panel), 56–57 (caption and test, added 2026-09-27).
**Primary pathway:** P6 — neuroinflammation
**White-matter boundary — the Olig2⁺ deficit is a CORPUS-CALLOSUM measurement and it is not a myelin result (`CC-20260826-CLAIM006-HARDENING-01` residue, 2026-09-27).** Figure 4e counts Olig2⁺ oligodendrocytes *"in three independent 500 μm2 regions spanning the entire imaged corpus callosum"*, `n = 3` mice per group, unpaired t-test at `p < 0.01` — 🔴 **ma l'unità del dato è la REGIONE, non l'animale**: la didascalia prosegue *«Each data point shows measurement from a single independent region from n = 3 mice/group»*, quindi il test gira su **~9 regioni da 3 animali** — **pseudoreplicazione non corretta dagli autori**; l'`n` biologico è **3** (locator entry 64, aggiunto 2026-09-28 da `CC-20260928-MIRROR003-REPAIRS-01` M7, come metà «unità di campionamento» della entry 58 il cui snippet si fermava una frase prima): mutant ≈122 vs wild type ≈205 at 80 days and ≈117 vs ≈235 at 250 days, each with an asterisk. 🔴 **No within-genotype 80-vs-250-day bracket is drawn, so progression is UNTESTED**, and the widening relative gap is driven by the **wild type rising**, not by the mutant falling — 80 days is the earliest age sampled, not a demonstrated onset. ⚠️ **The same paper reports no myelin difference in the region above it**: *"no significant differences in Mbp staining were detected when comparing"* the two genotypes in parietal cortex above the corpus callosum (Results 2.6, Supplementary Figs. 6a–d), which does not establish equivalent myelination elsewhere or by other measures but does forbid reading the cell-count deficit as a demonstrated hypomyelination. **Scope:** this is white matter, **not** the hippocampal compartment of [[claim_registry_current#CLAIM 006]], and it is not carried by any claim today; `Olig2` appears in no claim but [[claim_registry_current#CLAIM 003]], whose residual oligodendroglial limb is a different model and a different question. Locators: `deepdive_manifests/PMID36828035.json` entries 23 (panel), 36 (Mbp), 58 (caption, added 2026-09-27).
**Secondary pathway:** P3 — interaction logic
**Transcriptome bound — the KEGG synapse hit is an EXPRESSION programme and is not a measure of inhibition (`CC-20260826-PMID36828035-01` §2.5, verified at source 2026-09-28).** The paper reports *«Suppression of GABAergic and glutamatergic synapses in CTX and HPC was also detected in KEGG pathways suggesting abnormal neurotransmission likely related to the epileptic and seizure activity»*, with the finding located in **Supplementary Figs. S11 and S12**, which are not retrieved here. 🔴 **This is a pathway-enrichment result over transcript abundance. It measures no current, no reversal potential, no chloride concentration and no E/I ratio**, and it may not be recruited to the E_GABA question or to any statement about the **sign or strength** of GABAergic transmission. ⚠️ The authors' own hedges — *«suggesting»*, *«likely related»* — are the correct epistemic level and travel with the sentence. **Scope:** `Wwox^P47T/P47T` cortex and hippocampus; the enrichment direction is not reported per gene here and no gene-level locator exists on this checkout.
**Model/species:** mouse / functional variant study
**Genotype/model:** P47T
**Transferability:** T3 with genotype caution
**clinical relevance:** LOW
**Claim links:** 006, 007, 041
**Role:** genotype caution anchor
**Note:** key for "P47T ≠ Q230P". In-silico read-across (IPOTESI, `INBOX-006` — quarantine record, private overlay, CC-2026-07-04-004): pur essendo clinicamente distinto da Q230P ("P47T ≠ Q230P" resta valido sul piano fenotipico), P47T appartiene alla **stessa classe di stabilità** — variante destabilizzante (ΔΔG in-silico +2.8), lontana dal sito attivo (~48 Å), LoF parziale, topo che sopravvive >1 anno. ⚠️ **Lettura poi RITIRATA (repair 2026-07-14):** P47T **non** è equivalente sul piano meccanicistico — ha **proteina normale** e un difetto di binding **WW1/PPxY**, cioè un'altra lesione in un altro dominio. Resta un **comparator model**, **non** un banco read-across: nessuna prova su un missenso SDR sepolto può passare di lì. Vedi `MECHANISM_TRANSFER_FIREWALL`. ⚠️ **`BATCH_20260926_ALDAZ`:** *proteina normale* è la lettura di Mallaret 2014 ([[paper_registry_current#PAPER 042]], fibroblasti umani, per ispezione visiva), non di questo paper — qui l'abbondanza di proteina non è quantificata ([[claim_registry_current#CLAIM 007]]); il *binding WW1/PPxY* è misurato solo come recupero da due oligopeptidi PPPY. `BATCH_20260926_MALLARET`: anche in Mallaret 2014 la proteina P47T non è "normale" come misura — è *presente, di abbondanza simile ai controlli all'ispezione visiva (non quantificata)*; vedi [[claim_registry_current#CLAIM 030]].

---

## PAPER 008
**Short title:** Aldaz/Banne clinical spectrum
**Full title:** WOREE / SCAR12 clinical spectrum reviews
**Authors:** Aldaz / Banne cluster
**Year:** 2019–2021
**Source type:** review / clinical spectrum
**Journal/source:** various
**Identifier:** multiple / pending normalization
**Status:** integrated
**Primary pathway:** clinical spectrum / genotype-phenotype
**Model/species:** human review
**Genotype/model:** WWOX-related disorders broad spectrum
**Transferability:** T1 contextual
**clinical relevance:** MODERATE
**Claim links:** 008
**Role:** nosology anchor
**Note:** contextual, not directly therapeutic

---

## PAPER 009
**Short title:** NIH ODS mitochondrial supplements fact sheet
**Full title:** Dietary Supplements for Primary Mitochondrial Disorders — Health Professional Fact Sheet
**Authors:** NIH ODS
**Year:** current baseline use
**Source type:** professional fact sheet
**Journal/source:** NIH
**Identifier:** uploaded background source
**Status:** background_only
**Primary pathway:** P5 — mitochondrial support
**Model/species:** background review
**Genotype/model:** non-WWOX specific
**Transferability:** T3 indirect
**clinical relevance:** background only
**Claim links:** 009 supportive only
**Role:** support context
**Note:** useful for supplement context, not causal WWOX logic

---

## PAPER 010
**Short title:** Druck/Aqeilan 2026 mutational signatures
**Full title:** Endogenous Processes Underlying Clock-Like Mutational Signatures
**Authors:** Druck T, Aqeilan RI, Aldaz CM, Zanesi N, Huebner K (Ohio State + Hebrew Univ/Cyprus + MD Anderson)
**Year:** 2026
**Source type:** mechanistic / oncology-related
**Journal/source:** Genes, Chromosomes & Cancer 2026;65(1):e70106
**Identifier:** PMID 41562193 · PMCID PMC12820907 · DOI 10.1002/gcc.70106
**Status:** background_only
**Status change note:** declassato deliberatamente da `claim_linked` (v1.1) a `background_only` (v1.2) — la decisione della sessione 2026-03-29 è stata di non procedere con un claim operativo per il genotipo di riferimento; nessun dato CNS pediatrico diretto. 2026-06-28: full text recuperato; decisione background_only RICONFERMATA — nessun dato CNS pediatrico, nessuna variante del genotipo di riferimento, attribuzione causale SBS40c↔WWOX = IPOTESI.
**Evidence depth:** full text reviewed — `FTR-20260909-41562193-01` (`complete_fulltext_read`, 2026-09-09); manifest `deepdive_manifests/PMID41562193.json` (27 locators — 19 text, 8 figure — strict PASS, 0 gaps). 🔴 **Until 2026-09-09 this declaration had no complete receipt behind it**: the ledger held one `legacy_reconstruction` whose `source_locator` pointed at the registry row itself, whose `source_fingerprint` was `null`, and whose own `evidence_basis` recorded that the coverage map did not survive. The record therefore leaves the `registry_only_fulltext_declarations_baseline` set.
**Primary pathway:** P7 / broader WWOX biology
**Model/species:** indirect / non-the reference genotype CNS-focused
**Genotype/model:** WWOX loss broader biology
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none
**Role:** background only
**Note:** genomic instability / DNA damage response — no operative function for the reference genotype. [Titolo placeholder pre-scan precedente: "WWOX loss associated with clock-like mutational signatures".] Modelli: Wwox-ko MEF; WwoxP47T kidney 225d (Aldaz); Wwox-ko cortex P18 (Aqeilan, unico tessuto neurale, dati non disaggregati nel testo); Fhit-ko kidney/lymphoma. Tesi: FHIT-loss → SBS5; WWOX-loss → SBS40c (cosine SBS40c↔SBS5=0.916; ↔SBS3/HRD=0.824). CAVEAT: (1) SBS40c SOLO con SigProfilerAssignment, NON con SigProfilerExtractor → algoritmo-dipendente; (2) Wwox-ko da solo ha troppo pochi SBS, segnale emerge solo in co-loss Fhit-ko; (3) nessun paziente umano WWOX/WOREE, varianti worked-example (Q230P, c.1057-2A>G) assenti; (4) nessun safety signal, nessuna terapia, nessun biomarker proposto dagli autori. Asse genome-stability già coperto da [[claim_registry_current#CLAIM 029]] (in observation).

---

## PAPER 011
**Short title:** Obeid 2026 neuron-specific gene therapy
**Full title:** Neuron-Specific WWOX Gene Therapy Produces Dose-Dependent, Durable Rescue in a Model of WWOX-Related Epileptic Encephalopathy
**Authors:** Obeid et al.
**Year:** 2026
**Source type:** preclinical gene therapy study (peer-reviewed)
**Journal/source:** Molecular Therapy Advances (OMTA — *Mol Ther Adv*) 2026;34 (Cell Press)
**Identifier:** PMID 42422765 / PMCID PMC13343157 / DOI 10.1016/j.omta.2026.201791 — *Mol Ther Adv* 2026;34(3):201791. Identifier normalizzato in BATCH_20260710_A (era "da confermare"); main text full letto integralmente. Versione published del preprint bioRxiv omonimo.
**Status:** integrated
**Evidence depth:** complete_fulltext_read — article and S1–S8; latest receipt `FTR-20260814-42422765-06`; strict schema-v2 manifest `deepdive_manifests/PMID42422765.json`
**Primary pathway:** P7 — gene therapy readiness
**Secondary pathway:** P4 / P6 indiretto
**Model/species:** murine — Wwox-null (severo)
**Genotype/model:** Wwox-null full KO
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 011
**Role:** P7 design-principle paper
**Note:** AAV9-hSynI-hWWOX ICV neonatale; rescue dose-dependent durable su survival, ECoG/SWD, myelination, gliosis; neuron-specific targeting; full KO ≠ the reference genotype ma design principles sono trasferibili alla logica di trial-readiness. — Versione published (peer-reviewed, OMTA vol 34) del preprint bioRxiv; riferimento preprint conservato per tracciabilità. Design-principle quantitativi dai supplementari S1–S8 (BATCH_20260703 discovery): promotore SynI neuronale ottimale vs MBP/CMV; WPRE aumenta WWOX 3–16.7×/regione (trade-off dose↔sicurezza; la review PAPER 029 lo sintetizza come "WPRE removed to avoid overexpression"); espressione durevole fino a P300; neuron-specific (fegato negativo). Gap traslazionale per il genotipo di riferimento: nessun dato post-onset/età avanzata. Main-text OMTA full da recuperare (NS-019). ⚠️ `UPSTREAM_CITATION_FAILURE` (`CC-20260826-UPSTREAM-CITATION-FAILURE-01`, propagated `BATCH_20260927_001`): this paper's framing of its Figure 7 as confirmatory rests on reference 43 = [[paper_registry_current#PAPER 063]], a review with no new cohort, so its ECoG dataset is plausibly the first of its kind in the null rather than a replication.
🔴 **Corretto 2026-08-10 (`CC-20260810-42422765-S8`, BATCH_20260810_002) — la scorciatoia «finestra terapeutica P1–P5» è stata rimossa perché la Figura S8 non la sostiene.** Al suo posto, ciò che S8 mostra davvero: **efficacia dimostrata a più dosi postnatali precoci, P5 incluso; l'intervallo è campionato in modo incompleto per ciascun endpoint e il limite superiore oltre P5 non è stato testato.** In dettaglio, e ogni punto è una precisazione che la scorciatoia cancellava: (1) **nessuna evidenza P0 va attribuita a S8** — S8 non contiene alcun gruppo trattato a P0; (2) la sopravvivenza a **P40** include P1/P2/P3/P5 ma **non P4**; la sopravvivenza a **P300** include **solo P1 e P5**; (3) peso e glicemia a **P14** includono P1–P5, ma i test disegnati sono WT-vs-KO e WT-vs-P5 — **non esiste un confronto trattato-vs-KO**, e `ns` non è equivalenza; (4) i pannelli istologici/molecolari **E–I testano solo P5**; MBP è rappresentativa e non quantificata, e le statistiche GFAP confrontano WT-vs-KO e WT-vs-P5, non KO-vs-P5. *«P1–P5» leggeva come un intervallo continuo e validato ciò che è un insieme di punti campionati a maglie larghe, con il confronto che conta — trattato contro non trattato — mai disegnato.*
🔴 **Completamento 2026-08-15 (`CC-20260814-42422765-01`, BATCH_20260815_001).** Articolo e supplementi S1–S8 sono ora letti integralmente. L'espressione a lungo termine resta regionalmente disomogenea e sovrafisiologica nei sopravvissuti; P300 è una coorte survivor-selected e non prova sostituzione fisiologica uniforme. In S2 le etichette del grafico indicano `n=5`, la didascalia `n=4`: entrambe le numerosità sono preservate come discrepanza.

---

## PAPER 012
**Short title:** Sapuppo 2026 WOREE syndrome plus
**Full title:** WWOX-Related Epileptic Encephalopathy (WOREE Syndrome): Clinical Case Study and Literature Review
**Authors:** Sapuppo et al.
**Year:** 2026
**Source type:** human case report (peer-reviewed)
**Journal/source:** Current Issues in Molecular Biology 2026;48(5):449 (MDPI)
**Identifier:** PMID 42193054 · PMCID PMC13205014 · DOI 10.3390/cimb48050449
**Status:** integrated
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-42193054-01` (the earlier `FTR-20260726-42193054-01` is a legacy reconstruction); manifest `deepdive_manifests/PMID42193054.json`; dossier `research/fulltext_dossiers/PMID42193054.md`
**Primary pathway:** clinical spectrum / genotype-phenotype
**Secondary pathway:** P5 hypothesis-adjacent / weak P7 contextual
**Model/species:** human
**Genotype/model:** exon 6–7 deletion + exon 8 frameshift case
**Transferability:** T1 phenotypic / low therapeutic
**clinical relevance:** MODERATE
**Claim links:** 012
**Role:** phenotype-severity refinement paper
**Note:** MRI precoce normale non esclude rete severamente disorganizzata; nomenclatura "WOREE syndrome plus" non operativamente validata. Versione published del preprint Preprints.org [titolo preprint precedente: "WWOX Gene Disease as Infantile Catastrophic Epileptic Encephalopathy (WOREE Syndrome Plus): A Comprehensive Case Study with Brief Literature Update"] — stesso caso: CNV 38 kb esoni 6–7 + c.1043del p.Phe348Serfs*57 esone 8, ClinVar 421407. INCOERENZA PRISMA interna nella literature review (200→150→30 full-text; testo dichiara '70 esclusi su 30 full-text' = contraddizione aritmetica; nessuna figura PRISMA): conteggio review a bassa affidabilità, case report non invalidato. Test parentale non eseguito → cis/trans non determinato. Nessuno studio funzionale. Varianti del genotipo di riferimento (Q230P, c.1057-2A>G) NON presenti. 🔴 **Table 1 verificata riga per riga 2026-10-03 (`CC-20261003-A-SAPUPPO-01`):** tutte le righe tranne il caso indice trascrivono pazienti già contati — otto da Piard 2019 ([[paper_registry_current#PAPER 117]]) e uno da Dong 2023 ([[paper_registry_current#PAPER 134]], citato come rif. 11 = Mignot); secondi alleli omessi (delezione esone 4; G137E; H150P), `c.517_791del` etichettata in frame (275 nt, fuori frame), età d'esordio alterate (*«2–3 d»* dove la fonte dà 1 g, 5 g, 2,5 m, 3 m), sesso del paziente Dong invertito rispetto al testo della fonte, conseguenza proteica del caso indice data come quella della sola delezione dell'esone 6. **Non usare la Table 1 come fonte di conteggio; contare solo il caso indice.**

---

## PAPER 013
**Short title:** Turkish DEE cohort 2025
**Full title:** Genetic Etiology of Developmental and Epileptic Encephalopathy in a Turkish Cohort: a Single-Center Study with Targeted Gene Panel and Whole Exome Sequencing
**Authors:** Sunnetci-Akkoyunlu et al.
**Year:** 2025
**Source type:** human cohort study
**Journal/source:** Genes
**Identifier:** PMID 41153369
**Status:** processed
**Primary pathway:** clinical spectrum / cohort context
**Secondary pathway:** weak P1 / weak P7 contextual
**Model/species:** human
**Genotype/model:** two siblings with homozygous WWOX p.L239R (`c.716T>G`, Table 1: case 49 male, 3 months, West syndrome, multifocal EEG; case 50 female, 11 months, EIDEE, hypsarrhythmia), consanguineous, carrier parents
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-41153369-01` (first reading of the tables; earlier `FTR-20260921-41153369-01` had no tables and no gene symbols); manifest `deepdive_manifests/PMID41153369.json`; dossier `research/fulltext_dossiers/PMID41153369.md`
**Transferability:** T1 contextual
**clinical relevance:** LOW-MODERATE
**Claim links:** none
**Role:** supportive cohort context paper
**Note:** useful as human spectrum support only; not a strategy-shaping paper. 🔴 The paper reports EEG and syndrome only for its WWOX patients — no onset age, treatment, MRI, development, survival or movement description — so it cannot serve as a 'no parkinsonism' comparator: absence of a movement description here is not reported, not a reported absence. Which sibling had hypsarrhythmia is contradictory in the source (Discussion: case 49; Table 1: case 50). The 2026 case report of the same allele from the same university ([[paper_registry_current#PAPER 145]]) does not cite this cohort, and identity of its patient with case 49 is not excluded: count the cohort siblings and that child as at most three carriers and possibly two, never as independent replications without author confirmation (`CC-20261003W3-A-L239R-01`). 🔴 **Update 2026-10-04 (`CC-20261004W8-A-PATIENT-OVERLAP-01`, `BATCH_20261004_002`):** a third source, [[paper_registry_current#PAPER 220]] (PMID 41835067), reports one **homozygous** `p.Leu239Arg` female child of a consanguineous family, reached through a cerebral-palsy referral stream, whose *«Tonic-clonic seizures began at two weeks of age»* — ⚠️ the source's own words, and it adds *«There was no need for postnatal intensive care»*, so «neonatal-onset» would be the reader's label and is not used here (integrator amendment, blind audit). **Identity with case 50 here is not excluded (`INFERENZA`)**: neither source prints syndrome, EEG, onset detail or family structure sufficient to confirm or exclude it. Read sources therefore hold **2-4** homozygous `p.Leu239Arg` children in **1-3** families (Serin 2018, PMID 30094525, **unread and not counted**).

---

## PAPER 014
**Short title:** Gao 2025 WWOX-DEE genotype-phenotype
**Full title:** WWOX-Related Developmental and Epileptic Encephalopathy: Expanding the Clinical Spectrum and Deciphering the Genotype-Phenotype
**Authors:** Gao K, Riley LG, Raubenheimer J, Oliver KL, Wykes AD, Mentz J, Lee SJ, Pinner J, Cardamone M, Scheffer I, Gold WA
**Year:** 2025
**Source type:** cohort study / parent-reported registry
**Journal/source:** *Neurology*
**Identifier:** PMID 40875931 / DOI 10.1212/WNL.0000000000213883
**Status:** integrated
**Evidence depth:** full text reviewed (PDF)
**Primary pathway:** clinical spectrum / genotype-phenotype / P2 / sorveglianza respiratoria
**Model/species:** human — 50 individui, 45 famiglie
**Genotype/model:** biallelic WWOX variants — N/N / N/M / M/M
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** 013
**Role:** largest human WWOX-DEE cohort; genotype-aware risk stratification
**Note:** survey parentale con bias di sopravvivenza documentato; 3 segnali robusti (crisi, ipertonia, respiratorio) in N/N vs N/M e M/M; Q230P in 2 individui nel cohort; the reference genotype verosimilmente N/M

---

## PAPER 015
**Short title:** Teplyshova 2024 adult WWOX-DEE
**Full title:** Case report: Adult patient with WWOX developmental and epileptic encephalopathy — 40 years of observation
**Authors:** Teplyshova A, Sharkov A
**Year:** 2024
**Source type:** case report
**Journal/source:** *Frontiers in Genetics*
**Identifier:** PMID 39507621 / PMC PMC11537890 / DOI 10.3389/fgene.2024.1477466
**Status:** integrated
**Evidence depth:** full text reviewed (PMC open access)
**Primary pathway:** clinical spectrum / natural history
**Secondary pathway:** P4 (myelination long-term)
**Model/species:** human
**Genotype/model:** omozigote p.Thr12Met (N-terminal, non WW domain)
**Transferability:** T1 phenotypic
**clinical relevance:** MODERATE
**Claim links:** none
**Role:** natural history long-span; supportive context
**Note:** primo adulto documentato con WWOX-DEE (40 anni); progressione: epilessia cronica → regressione motoria adolescenza → complicanze respiratorie severe età adulta; genotipo diverso dal genotipo di riferimento; non cambia strategia

---

## PAPER 016
**Short title:** You 2024 vigabatrin case WWOX
**Full title:** Developmental epileptic encephalopathy caused by homozygosity of a c.172+1G>C variant in the WWOX gene
**Authors:** You Y, Wu W, Du Y, Hu J, Li B
**Year:** 2024
**Source type:** case report
**Journal/source:** *Molecular Genetics & Genomic Medicine*
**Identifier:** PMID 39101447 / PMC PMC11298992 / DOI 10.1002/mgg3.2500
**Status:** integrated
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-39101447-01` (earlier: `FTR-20260921-39101447-01`, partial); manifest `deepdive_manifests/PMID39101447.json`; dossier `research/fulltext_dossiers/PMID39101447.md`
**Primary pathway:** P2 — safety / AED management
**Model/species:** human
**Genotype/model:** omozigote splice site donatore c.172+1G>C (isodisomia inferita da LOH copy-neutral); minigene esoni 1–3 in HEK293T: **skipping dell'esone 2** (WT 426 bp, mutante 361 bp; 65 nt, fuori frame) — la troncatura è una traduzione in silico; nessun RNA del paziente, nessuna proteina (corretto `CC-20261003-A-VIGABATRIN-01`)
**Transferability:** T1 (umano) — genotipo null/null ≠ the reference genotype compound het missense + splice
**clinical relevance:** MODERATE-HIGH — safety-relevant (conflicting evidence vigabatrin)
**Claim links:** 001 (conflicting evidence)
**Role:** tensione evidence su vigabatrin; non pro-vigabatrin
**Note:** riduzione delle crisi **visibili** con VGB in 1 caso null/null, ma il VEEG a 11 mesi registra ancora attacchi elettrici e spasmi non notati a casa; senza MRI controllo per VABAM; follow-up brevissimo (13 mesi); non invalida Choi 2026; genotipo null/null ≠ the reference genotype

---

## PAPER 017
**Short title:** Chong 2023 WOREE spectrum KD Q230P
**Full title:** Expansion of the clinical and molecular spectrum of WWOX-related epileptic encephalopathy
**Authors:** Chong SC, Cao Y et al. (Baylor College of Medicine / CUHK / Undiagnosed Diseases Network)
**Year:** 2023
**Source type:** case series
**Journal/source:** *American Journal of Medical Genetics Part A*
**Identifier:** PMID 36537114 / DOI 10.1002/ajmg.a.63074
**Status:** integrated
**Evidence depth:** partial full text (Scholar Gateway, 47 chunk — non open access)
**Primary pathway:** P1 clinical / KD support / P3 (Q230P SDR mechanism)
**Secondary pathway:** P5 (lattato P4)
**Model/species:** human — 5 pazienti WOREE (tutti null/null)
**Genotype/model:** null/null (SNV splice + delezioni esoni)
**Transferability:** T1 per KD e fenotipi clinici; T2 per meccanismi molecolari
**clinical relevance:** MODERATE-HIGH
**Claim links:** 001 (dato misto vigabatrin) / 009 (supporto P5) / 013 supportivo
**Role:** KD support + Q230P SDR mechanism + spectrum expansion
**Note:** KD associata a miglioramento crisi in 3/5 (P1, P2, P4) [corretto 2026-09-29 da `BATCH_20260929_001`: la fonte nomina **tre** responder (P1, P2, P4) ma **non dice quanti dei cinque abbiano iniziato la dieta**, quindi «3/5» non è un tasso di risposta; l'unica portatrice di `p.Gln230Pro` (P5, eterozigote composta con delezione dell'esone 5, più una variante *GRIA4* de novo) **non ha alcuna voce di dieta** in Tabella 1; «tutti null/null» ripete la previsione degli autori (*«predicted to be null»*), non una misura per l'allele missense — receipt `FTR-20260929-36537114-02`, [[claim_registry_current#CLAIM 042]]]; vigabatrin: resistente in P3, combinato con KD in P4; lattato lievemente elevato in P4 (2.4-3.3 mmol/L); Q230P/SDR: trascritto normale ma proteina assente/instabile → meccanismo post-traduzionale → compatibile con funzione residua parziale nel genotipo di riferimento; pancreatite ricorrente e sordità neurosensoriale come feature espansive; valutazione visiva indicata (4/5 con deficit visivo)

---

## PAPER 018
**Short title:** Oliver 2023 WWOX-DEE epilettologia mortalità
**Full title:** WWOX developmental and epileptic encephalopathy: Understanding the epileptology and the mortality risk
**Authors:** Oliver KL, Trivisano M, Mandelstam SA, et al.
**Year:** 2023
**Source type:** multicenter cohort study
**Journal/source:** *Epilepsia*
**Identifier:** PMID 36779245 / PMC PMC10952634 / DOI 10.1111/epi.17542
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260804-36779245-02`; manifest `deepdive_manifests/PMID36779245.json` (30 locators, schema v2, 3 declared gaps; structural PASS — two declared artefacts, including the 2026-08 XML the first 20 locators quote, are absent from this deployment, which is an evidence-locality fact and not a provenance failure of the reading); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's. **Two later PARTIAL re-reads exist and NEITHER supersedes the complete one** (`CC-20260914-EVIDENCE-DEPTH-01`, re-derived from the ledger 2026-09-27): `FTR-20260810-36779245-03` (methods, results, tables, discussion) and `FTR-20260923-36779245-04` (**supplementary only** — it read `Table S1`, the surface `-02` recorded as `unavailable`, and found a variant/ACMG census with no age, outcome or survival column). A later partial is an ADDITION to the covered surface, never a downgrade of the complete event, and the two together are why this record's depth does not move. Ten locators were added on 2026-09-27 (entries 20-29, by two wave-2 packages) from a re-acquired PMC surface (`PMID36779245_Oliver2023_PMC_2026-09-27.xml`), declared beside the historical artefact rather than substituted for it.
**Primary pathway:** clinical spectrum / natural history / survival analysis
**Model/species:** human — 13 pazienti, 12 famiglie, 5 centri
**Genotype/model:** biallelic WWOX variants — N/N / N/M / M/M
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** 031 · 033 — ⚠️ **lifecycle decision, 2026-09-27 (`BATCH_20260927_004`, `CC-20260914-EVIDENCE-DEPTH-01`'s second residue, deferred by `BATCH_20260927_003` as a decision owed registry-wide).** Measured first: **exactly one record in the whole registry** was in this state — `Status: filtered_in` beside a `complete_fulltext_read`, with `Claim links: pending` — so the decision applies across every record in that state and that is this one. `filtered_in` is a triage value and is **false of a paper that has been read completely**, hence `processed`. And `pending` was a placeholder that outlived the reading: [[claim_registry_current#CLAIM 031]] names this record in its own `Source` and `Wikilinks`, and [[claim_registry_current#CLAIM 033]] names it in both as well, so the edges are declared from the claims' side already. 🔴 **This is not the anti-pattern `BATCH_20260927_002`'s Mirror finding F5 named:** that was an edge invented to clear an advisory warning on a record no claim cited: here the claims cite the record, and the declaration makes the registry agree with them rather than the reverse
**Role:** epilettologia WWOX-DEE; sopravvivenza Kaplan-Meier; missense vs non-missense survival
**Patient overlap (2026-10-03, `CC-20261003W5-B-PATIENT-OVERLAP-01`):** patient 6 (EIMFS; `p.Glu17Lys` with two intronic deletions, introns 3 and 4) is the WWOX patient of [[paper_registry_current#PAPER 172]] (Burgess 2019): this paper says its patients 6 and 7 were 'briefly reported' and cites Burgess; genotype, sex, consanguinity and recruiting country agree. One patient, counted here. This paper, not Burgess, carries the RNA result: intron-4 deletion → exon 5 skipping, intron-3 deletion benign.
**Next action:** none — the full text was retrieved and read completely on 2026-08-04 (`FTR-20260804-36779245-02`). The instruction to retrieve it stood for six weeks after the reading and is removed here, not silently: a registry that asks for work already done sends a reader to repeat it.
**Superseded declaration (append-only):** this record declared `Evidence depth: abstract + frammenti Scholar Gateway` until BATCH_20260920_001. The prior value is preserved rather than overwritten in silence — it is the trace of how long the registry and the ledger disagreed, on a T1 / HIGH record. `Status: filtered_in` and `Claim links: pending` are deliberately NOT changed by that batch: whether this reading produces a claim is a scientific question it did not ask. ⚠️ **Superseded in turn by `BATCH_20260927_004`, which measured the population and decided** — see the `Claim links` field above: `Status` is now `processed` and the links are `031 · 033`. The sentence is kept rather than corrected, because it was true of `BATCH_20260920_001` and is the trace of what that batch declined to do; without this pointer it now reads as a contradiction of the fields two lines above it. Note added 2026-09-28 (Mirror `N5`).
**Note:** key finding: presenza ≥1 missense aumenta sopravvivenza 5 anni da <50% a >75% (p=0.0085). Tipi crisi: focali 85%, spasmi 77%, toniche 69%. EEG: slow background, multifocal discharges. MRI: frontotemporal atrophy, hippocampal atrophy, thin corpus callosum. Sindromi: EIDEE 8/13, IESS 2, EIMFS 2. Distonia 11/13.

---

## PAPER 019
**Short title:** Cheng 2020 GSK3β seizure axis
**Full title:** Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and glycogen synthase kinase 3beta-mediated epileptic seizure activity in mice
**Authors:** Cheng et al.
**Year:** 2020
**Source type:** murine mechanistic study
**Journal/source:** *Acta Neuropathologica Communications*
**Identifier:** PMID 32000863 / DOI 10.1186/s40478-020-0883-3
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260804-32000863-01`; manifest `deepdive_manifests/PMID32000863.json` (25 locators, schema v2, strict PASS, 3 declared gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**Primary pathway:** P3 — prenatal structure / GSK3β
**Secondary pathway:** P4 / P1
**Model/species:** mouse
**Genotype/model:** Wwox-null full KO
**Transferability:** T2 mechanistic
**clinical relevance:** HIGH
**Claim links:** 015, 016
**Role:** structural / GSK3β anchor paper
**Note:** severe model; supports prenatal malformation axis and GSK3β as research node; full text still prioritized. ⚠️ `UPSTREAM_CITATION_FAILURE` (`CC-20260826-UPSTREAM-CITATION-FAILURE-01`, propagated `BATCH_20260927_001`): this is the only primary source for spontaneous behavioural seizures in a Wwox-null mouse, and its own observation is opportunistic husbandry plus one video — a floor, not a rate. It carries more weight than its citation count suggests and less certainty than its unanimity suggests.

---

## PAPER 020
**Short title:** Iacomino 2020 migration
**Full title:** Loss of Wwox Perturbs Neuronal Migration and Impairs Early Cortical Development
**Authors:** Iacomino et al.
**Year:** 2020
**Source type:** translational developmental study
**Journal/source:** *Frontiers in Neuroscience*
**Identifier:** PMID 32581702 / DOI 10.3389/fnins.2020.00644
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-32581702-01`; manifest `deepdive_manifests/PMID32581702.json` (21 locators, schema v2, strict PASS, 0 gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**Primary pathway:** P3 — prenatal structure / migration
**Secondary pathway:** P4
**Model/species:** human fetal tissue + rat + hNPC
**Genotype/model:** WWOX deficiency / null-like developmental models
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 014, 015
**Role:** migration / cortical assembly anchor paper
**Note:** one of the key structural papers from the 180-paper test; full text remains high priority

---

## PAPER 021
**Short title:** Tochigi 2019 rat lde/lde
**Full title:** Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination in a Rat Model of Lethal Dwarfism with Epilepsy
**Authors:** Tochigi et al.
**Year:** 2019
**Metadata correction (BATCH_20260806_002):** the previous record read *"Kumada et al."* and gave the title as *"…in a Rat Model of **Lissencephaly**"*. Both were wrong: the author is **Tochigi**, and the published title ends *"…in a Rat Model of **Lethal Dwarfism with Epilepsy**"*. The word *lissencephaly* appears nowhere in the paper and was never its subject — the invented title had been silently steering this record toward a migration/layering interpretation the study does not make. Corrected from the complete full-text read, receipt `FTR-20260806-31340538-01`.
**Role correction (BATCH_20260806_002):** reclassified from *"prenatal cortex / myelin assembly anchor"* to **early postnatal cortical neurite/glial/myelin maturation anchor (PND5–21)**. The study measures NeuN count/signal, cortical thickness, MAP2, MBP, CNP, APC/CC1, GFAP and Iba1 at PND5/10/15/21. It measures **no prenatal time point**, no OPC abundance, no lineage autonomy, no rescue or reversibility, no myelin ultrastructure, no conduction and no GSK3β/Tau mechanism. `n ≥ 3` males per group per age, multiple uncorrected Student t-tests, no declared blinding, randomisation or power calculation.
**Source type:** rat developmental study
**Journal/source:** *International Journal of Molecular Sciences*
**Identifier:** PMID 31340538 / DOI 10.3390/ijms20143596
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260806-31340538-01`; manifest `deepdive_manifests/PMID31340538.json` (11 locators, schema v2, strict PASS, 0 gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**Primary pathway:** P4 — myelination / white matter
**Secondary pathway:** P3
**Model/species:** rat
**Genotype/model:** lde/lde Wwox-deficient rat
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 014, 015
**Role:** prenatal cortex / myelin assembly anchor
**Note:** strong support for structural + hypomyelination axis

---

## PAPER 022
**Short title:** Kośla 2019 hNPC differentiation
**Full title:** The WWOX Gene Influences Cellular Pathways in the Neuronal Differentiation of Human Neural Progenitor Cells
**Authors:** Kośla et al.
**Year:** 2019
**Source type:** human cell differentiation study
**Journal/source:** *Frontiers in Cellular Neuroscience*
**Identifier:** PMID 31543760 / DOI 10.3389/fncel.2019.00391
**Status:** processed
**Primary pathway:** P3 — neuronal differentiation / developmental programs
**Secondary pathway:** P5 indirect
**Model/species:** human neural progenitor cells
**Genotype/model:** WWOX-silenced / deficient hNPC context
**Transferability:** T2
**clinical relevance:** MODERATE-HIGH
**Claim links:** 014
**Role:** supporting developmental mechanism paper
**Note:** useful for cytoskeleton and differentiation pathway support

---

## PAPER 023
**Short title:** Baryła 2022 IJMS WWOX/HIF1A axis
**Full title:** The WWOX/HIF1A Axis Downregulation Alters Glucose Metabolism and Predispose to Metabolic Disorders
**Authors:** Baryła et al.
**Year:** 2022
**Source type:** mechanistic metabolic study
**Journal/source:** *International Journal of Molecular Sciences*
**Identifier:** PMID 35328751 / DOI 10.3390/ijms23063326
**Status:** processed
**Primary pathway:** P5 — metabolism / HIF1A
**Secondary pathway:** none
**Model/species:** una sola linea di fibroblasti cutanei umani immortalizzati, 1BR.3.N (ECACC 90020508), in quattro condizioni incrociate ossigeno × glucosio [corretto 2026-10-03 da «mixed mechanistic / non-CNS direct» con `CC-20261003W4-B-HIF1A-SCOPE-01`]
**Genotype/model:** **due bracci, non uno** [corretto 2026-10-03 da «WWOX downregulation framework» con `CC-20261003W4-B-HIF1A-SCOPE-01`]. (a) perdita: sgRNA CRISPR/Cas9 con selezione in puromicina, policlonale — mRNA circa 3× più basso e proteina circa 8.5× più bassa; il lavoro la chiama «KO» ovunque, ma è un knockdown, e ogni affermazione che eredita da qui la parola knockout eredita una deplezione parziale. (b) ri-fornitura: cDNA WWOX lentivirale a circa 850× mRNA e >700× proteina — sovrafisiologica, e **assente da ogni record LEGEND fino a questa lettura**. 🔴 I due bracci non sono speculari: il lattato nel mezzo sale nella perdita in tutte e quattro le condizioni **e sale anche** nella sovraespressione rispetto al wild type in normossia-normoglicemia e in ipossia-iperglicemia, e l'uptake di glucosio inverte di segno con la condizione in entrambi i bracci. Nessun endpoint di questo sistema è quindi un reporter monotono della dose di WWOX.
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Role:** metabolic axis anchor
**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20261003-35328751-02` su JATS Europe PMC (PMC8955937), manifest `deepdive_manifests/PMID35328751.json` (7 locator, validatore PASS con `--verify-artifacts`), dossier `fulltext_dossiers/PMID35328751.md`. Parziale per due ragioni dichiarate: i pannelli non sono stati ispezionati come immagini e le Figure S1–S6 **non sono scaricabili** (l'endpoint `supplementaryFiles` di Europe PMC restituisce HTTP 500 per questo PMCID), quindi ogni affermazione sul braccio di sovraespressione poggia su testo corrente che porta i propri numeri. Ricevuta precedente `FTR-20260921-35328751-01`, su un'estrazione testuale che aveva cancellato ogni token in corsivo.
**Integrity note (2026-10-03, `CC-20261003W4-B-HIF1A-SCOPE-01`):** due saggi della stessa quantità si contraddicono dentro il lavoro e solo uno arriva alla Discussione. La Discussione afferma aumento di HIF1α «together with its translocation to the nucleus»; il blot frazionato riporta la proteina **ridotta nel citoplasma** del knockdown in due condizioni e «We didn't observed WWOX influence on HIF1α protein in nuclear fraction», mentre l'immunocitochimica su cellula intera mostra un aumento nelle due condizioni normossiche. Il positivo robusto del lavoro è il reporter di transattivazione HRE, non il livello proteico e non la traslocazione. Misurato anche un **negativo**: espressione e attività della citrato sintasi non mostrano influenza di WWOX in alcuna condizione, e non esiste respirometria. ⚠️ Il negativo è della citrato sintasi, **non** dell'intero braccio ossidativo: l'attività della piruvato deidrogenasi scende significativamente nel braccio di sovraespressione in ipossia (p < 0.001, Results 2.5) — precisato il 2026-10-03 da `BATCH_20261003_003` su audit cieco.
**Note:** complements PAPER 002 by giving a more focused WWOX/HIF1A axis paper

---

## PAPER 024
**Short title:** Abu-Remaileh 2014 HIF1A glucose metabolism
**Full title:** Tumor suppressor WWOX regulates glucose metabolism via HIF1alpha modulation
**Authors:** Abu-Remaileh et al.
**Year:** 2014
**Source type:** mechanistic metabolic study
**Journal/source:** *Cell Death and Differentiation*
**Identifier:** PMID 25012504 / DOI 10.1038/cdd.2014.95
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260814-25012504-01`; manifest `deepdive_manifests/PMID25012504.json` (22 locators, schema v2, strict PASS, 0 gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**Primary pathway:** P5 — metabolism / HIF1A
**Secondary pathway:** none
**Model/species:** cell / animal metabolic models
**Genotype/model:** WWOX loss / downregulation
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Role:** foundational HIF1A metabolic anchor
**Note:** strengthens HIF1A/Warburg framework. 🔴 `BATCH_20260815_001`: lettura completa `FTR-20260814-25012504-01`. L'asse WW1/HIF1α è sostenuto in MEF con rescue, knock-down e controllo WFPA. L'endpoint in vivo è glicemia acuta a 40 minuti, non uptake/flux; i trascritti supplementari sono `GLUT1/PHD3` (n=2), non `PDK1/PHD3`; `100 mg/kg` resta una `REPORTED_DOSE_AMBIGUITY`. Digossina è validazione del bersaglio, non candidato terapeutico.

---

## PAPER 025
**Short title:** Weisz-Hubshman 2019 EJPN exon 6 / Q230P
**Full title:** Novel WWOX deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay and dysmorphism among Yemenite Jews
**Authors:** Weisz-Hubshman M, Meirson H, Michaelson-Cohen R, Beeri R, Tzur S, Bormans C, Modai S, Shomron N, Shilon Y, Banne E, Orenstein N, Konen O, Marek-Yagel D, Veber A, Shalva N, Imagawa E, Matsumoto N, Lev D, Lerman Sagie T, Raas-Rothschild A, Ben-Zeev B, Basel-Salmon L, Behar DM, Heimer G
**Year:** 2019
**Source type:** human case series
**Journal/source:** *Eur J Paediatr Neurol* 2019;23(3):418-426
**Identifier:** PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003 (verified at PubMed and against the publisher PII S1090-3798(18)30411-2, 2026-09-27) / no PMCID
**Status:** processed
**Primary pathway:** genotype-phenotype / exon 6 logic
**Secondary pathway:** clinical spectrum
**Model/species:** human
**Genotype/model:** severe compound heterozygous and splice-related human variants
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** 018, 019
**Role:** exon 6 skipping + Q230P compound-context anchor
**Note:** important for allele-specific logic and exon-based pathogenicity. 🔴 **Byline corrected 2026-09-27:** the record carried *"Piard et al."*, the first author of a DIFFERENT 2019 WWOX paper (`PMID 30356099`, Genet Med, the 20-case WOREE cohort) — the identifier of one paper with the byline of another. Corrected against four independent surfaces (PubMed metadata, the publisher's own figure package, this model's splice-transcript census, and Oliver 2023's Table S1, which lists the two papers as separate rows). Nothing about [[claim_registry_current#CLAIM 018]] or [[claim_registry_current#CLAIM 019]] changes: a wrong byline is not a wrong finding. ⚠️ **Read depth is NOT abstract-only** — `FTR-20260923-30853297-01/-02`, `partial_fulltext_read`, body pages read — and any note asserting abstract depth for this record contradicts the receipt ledger. 🟢 **Evidence restored 2026-09-28 (`BATCH_20260928_007`, receipt `FTR-20260928-30853297-03`):** the publisher PDF is back at `files/fulltext/PMID30853297_WeiszHubshman2019.pdf`, byte-identical to the receipted artefact (sha256 `9cb9d2a27100ffde68cb60478cbd0e2bf5504d9dd46f2ed547849425851c06c4`), and the quotations below are persisted as `rendered_text` locators in `deepdive_manifests/PMID30853297.json`, because the PDF's text layer is refused by the suspect-surface screen; they passed a blind locator audit. Carries a **measured** RNA outcome: RT-PCR on **blood**-derived cDNA across exon 6 (*«Total RNA was isolated from blood using Trisol reagent»*, Methods § 2.4). A control sample gives one product of **593 bp** (Fig. 4C legend). The homozygote gives *«only the 504 bp band»*, which the Results call *«consistent with the prediction»* of *«an 89 bp deletion of exon six in the mutant allele»* (§ 3.4, p. 423), while the **Abstract** states it as shown (*«Complementary DNA sequencing demonstrated that the WWOX c.517-2A > G splice-site variant causes skipping of exon six»*); Methods § 2.4 names sequencing (*«gel electrophoresis and sequencing by ABI Prism 3100 Genetic Analyzer»*), and **no figure displays a cDNA or junction chromatogram**. ⚠️ **Source-internal conflict on the two-band result:** § 3.4 gives *«two PCR products sized 593 bp and 504 bp»* to the compound heterozygotes of family 2, but Fig. 4C (*«Family 3, cDNA analysis»*) has **no family-2 lane** — its two-band lane belongs to a family-3 relative whose genotype label in the legend disagrees with the pedigree (pedigree detail deliberately omitted in this public edition); so the family-2 result is stated in text and not displayed. Also a `Q230P` primary (`c.689A>C`; the two compound heterozygotes carry it with `c.517-2A>G`), whose only population figure is gnomAD (*«allele count of three out of a total of 246,218 alleles»*). 🔴 **The 1:177 carrier rate belongs to `c.517-2A>G` alone**: *«two out of the 353 (706 chromosomes) Yemenite Jewish control samples»*, 95% CI *«0.0016–0.0204»* by the *«binomial exact confidence interval approach»* (§ 3.3, p. 423). No control-cohort denominator was measured for the missense allele, so the rate must never be attached to it. ⚠️ LEGEND's own Clopper–Pearson for 2/353 gives 0.00069–0.0203: the printed upper bound reproduces and the lower bound does not. ⚠️ **No protein work of any kind** (`Western` 0, `blot` 0, an earned zero with controls `WWOX` 49, `splice` 18), so `CLAIM 030`'s `PREMISE: DETECTION_FLOOR` is untouched by this source.


## PAPER 026
**Short title:** ChemBioChem 2020 WWOX–p73 phospho-binding
**Full title:** Phosphorylation of the WWOX Protein Regulates Its Interaction with p73
**Authors:** Shkedi et al.
**Year:** 2020
**Source type:** experimental biochemistry / quantitative binding study
**Journal/source:** *ChemBioChem*
**Identifier:** PMID 32185845 / DOI 10.1002/cbic.202000032
**Status:** integrated
**Primary pathway:** signaling organization / PTM / partner affinity
**Secondary pathway:** cross-pathway interpretive principle
**Model/species:** in vitro domain-peptide biophysics
**Genotype/model:** WWOX WW1 and Tyr33-phosphorylated state vs p73-derived PPXY-containing peptide; non-CNS direct
**Transferability:** T2 conceptual / indirect
**clinical relevance:** LOW direct / HIGH architectural
**Claim links:** 028
**Role:** mechanistic anchor paper for ligand-specific phospho-state dependence
**Note:** Quantitative ITC and fluorescence-anisotropy study showing that Tyr33 phosphorylation decreases affinity for a p73-derived peptide. Does not close the full cellular p73 branch, but materially strengthens CLAIM 028 and introduces disciplined tension with older cell-based literature reporting enhanced WWOX–p73 interaction.

## PAPER 027
**Short title:** PNAS 2014 ATM/DDR
**Full title:** WWOX, the common fragile site FRA16D gene product, regulates ATM activation and the DNA damage response
**Authors:** Abu-Odeh M, Salah Z, Herbel C, Hofmann TG, Aqeilan RI
**Year:** 2014
**Source type:** primary mechanistic DDR study
**Journal/source:** *Proceedings of the National Academy of Sciences USA*
**Identifier:** PMID 25331887 / DOI 10.1073/pnas.1409252111
**Status:** integrated
**Evidence depth:** `partial_fulltext_read` — receipts `FTR-20260810-25331887-01` (body) and `FTR-20260909-25331887-02` (supplement); no single complete receipt or resolved study-level rollup. The seven figure PNG locators in `deepdive_manifests/PMID25331887.json` still fail strict regeneration, so the SI-only narrowing candidate is deferred.
**Primary pathway:** genome stability / ATM / DNA damage response
**Secondary pathway:** developmental vulnerability (candidate)
**Model/species:** cellular DDR systems / cancer-linked mechanistic context
**Genotype/model:** WWOX deficiency with damage-induced nuclear relocalization and ATM interaction; non-CNS pediatric direct
**Transferability:** T2 conceptual / indirect
**clinical relevance:** LOW direct / MEDIUM structural
**Claim links:** 029
**Role:** new structural-axis paper
**Note:** Shows that WWOX deficiency reduces ATM activation, compromises γ-H2AX response and impairs DNA repair; introduces a plausible genome-/replicative-stress vulnerability branch relevant to proliferative developmental compartments, but not yet promotable to core clinical logic.
**Identity correction (BATCH_20260926_ALDAZ_R5):** PMID 25331887 is Abu-Odeh et al., not Schrock et al. `PAPER 030` is a duplicate record retained for historical links; this is the canonical identity. No claim-strength promotion follows from correcting metadata or from aggregating two partial receipts.


## PAPER 028
**Short title:** Cell Commun Signal 2024 WWOX/TRAF2 switch
**Full title:** Dissociation of the nuclear WWOX/TRAF2 switch renders UV/cold shock-mediated nuclear bubbling cell death at low temperatures
**Authors:** Chang et al.
**Year:** 2024
**Source type:** mechanistic stress-signaling study
**Journal/source:** *Cell Communication and Signaling*
**Identifier:** PMID 39420317 / DOI 10.1186/s12964-024-01866-6
**Status:** processed
**Evidence depth:** full text reviewed (PMC open access)
**Primary pathway:** signaling organization / stress-contingent partner switching
**Secondary pathway:** weak support for CLAIM 028
**Model/species:** cellular stress paradigms (UV / cold shock) / mechanistic systems
**Genotype/model:** WWOX/TRAF2/TRADD/p53 complex dynamics; non-CNS direct
**Transferability:** T3 mechanistic / indirect
**clinical relevance:** VERY LOW direct / LOW architectural
**Claim links:** 028 supportive only
**Role:** secondary support paper
**Note:** Shows WWOX-dependent nuclear relocalization of TRAF2 and stress-contingent dissociation of WWOX/TRAF2 complexes in an idiosyncratic UV/cold-shock paradigm. Useful as secondary support for context-sensitive partner-switching logic, but not sufficient for a new claim or working-model propagation.


## PAPER 029
**Short title:** Neurobiol Dis 2026 — WWOX brain review (Aqeilan lab)
**Full title:** WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities
**Authors:** Obeid M, Wang J, Abudiab B, Akkawi R, Aqeilan RI
**Year:** 2026
**Source type:** narrative review (secondary) — from the source lab (Aqeilan, Hebrew Univ–Hadassah)
**Journal/source:** *Neurobiology of Disease* 225 (2026) 107446
**Identifier:** PMID 42128308 / DOI 10.1016/j.nbd.2026.107446 — open access (CC BY-NC)
**Status:** integrated
**Evidence depth:** full text reviewed (pymupdf extraction, 17 pp)
**Primary pathway:** cross-pathway synthesis (P1 network, P2 GABA, P3 prenatal, P4 myelin, P5 metabolism, P7 gene therapy)
**Model/species:** review of mouse / human organoid / Drosophila / clinical evidence
**Genotype/model:** consolidates the 3-class gene-dosage genotype–phenotype framework (null/null severe-lethal; null/missense intermediate ← the reference genotype; hypomorphic missense milder/SCAR12) + documented outliers (Feng 2024 missense early-death; Havali 2021; Oliver intron-4)
**Transferability:** T2 framework (corroborating, not primary DATO)
**clinical relevance:** HIGH (BLOCCO 2) — genotype framework + gene-therapy design/safety; NO BLOCCO 1 change
**Claim links (corroborates):** 002, 011, 013, 016, 019, 020, 028 strengthened; 025 nuanced (HIF1α-independent tension, Lucas-Clarke 2025); identifies "paper 210" = Breton et al. 2021
**Role:** authoritative current synthesis (source lab) — corroborates baselines; surfaces NEW primaries → queued FT-007..FT-011
**Note:** Review → corroborates, does NOT create new DATO. NEW design principles for AAV9-WWOX: human synapsin promoter (neuron-specific), WPRE removed (avoid overexpression), controlled dose, critical early postnatal window. SAFETY caveat: DRG / peripheral-organ dose-limiting toxicity at high systemic dose (pediatric regulatory concern). Epigenetic dCas9/CRISPRa upregulation flagged as future option for HYPOMORPHIC states (relevant to the reference genotype's residual Q230P allele). Strategic event (press, not peer-reviewed): first-in-human WWOX gene therapy, Aqeilan lab, June 2026 — see full_text_queue FT-012.


## PAPER 030
**Short title:** Abu-Odeh 2014 WWOX–ATM DDR
**Full title:** WWOX, the common fragile site FRA16D gene product, regulates ATM activation and the DNA damage response
**Authors:** Abu-Odeh M, Salah Z, Herbel C, Hofmann TG, Aqeilan RI
**Year:** 2014
**Source type:** mechanistic primary (cell/mouse) — oncology/DDR context
**Journal/source:** *Proc Natl Acad Sci U S A* 2014;111(44):E4716-25
**Identifier:** PMID 25331887 · PMCID PMC4226089 · DOI 10.1073/pnas.1409252111
**Status:** superseded
**Evidence depth:** superseded metadata; see `PAPER 027` for the two partial full-text receipts and unresolved figure-locator debt
**Primary pathway:** genome stability / ATM / DNA damage response
**Model/species:** HEK293, HeLa, mouse — non-CNS, oncology/DDR
**Genotype/model:** Wwox deficiency (cell lines + mouse); not pediatric CNS
**Transferability:** T2 conceptual / indirect for the reference genotype
**clinical relevance:** INDIRECT — structurally important (genome-stability axis), not operational
**Claim links:** 029
**Role:** primary mechanistic source for the WWOX→ATM/DDR axis (CLAIM 029)
**Note:** Promosso 2026-06-28 (BATCH_20260628_002) da corpus-paper 138 a PAPER record completo per ancorare CLAIM 029. Metadati verificati via PubMed (According to PubMed). Tesi: Wwox-deficiency riduce attivazione ATM, compromette induzione/mantenimento γ-H2AX, impairs DNA repair; danno → ITCH-mediata K63-ubiquitinazione di WWOX su Lys274 → accumulo nucleare → interazione con ATM. Contesto tumorale/genome-instability, NON CNS pediatrico → CLAIM 029 resta `in observation`. Full text non ancora estratto (solo abstract).
**Wikilinks:** [[claim_registry_current#CLAIM 029]]
**Identity correction (BATCH_20260926_ALDAZ_R5):** this is the same PMID as `PAPER 027`, not independent support. Its original abstract-only note records the state at promotion in June 2026 and is superseded by the receipts and limits now attached to `PAPER 027`.


## PAPER 031
**Short title:** Breton 2021 neocortical excitability
**Full title:** Altered neocortical oscillations and cellular excitability in an in vitro Wwox knockout mouse model of epileptic encephalopathy
**Authors:** Breton VL, Aquilino MS, Repudi S, Saleem A, Mylvaganam S, Abu-Swai S, Bardakjian BL, Aqeilan RI, Carlen PL
**Year:** 2021
**Source type:** murine electrophysiology (ex vivo slice)
**Journal/source:** *Neurobiol Dis* 2021;160:105529
**Identifier:** PMID 34634460 / PMCID PMC8609180 / DOI 10.1016/j.nbd.2021.105529
**Status:** integrated
**Evidence depth:** full text verificato (files/fulltext/PMID34634460_Breton2021.md, PMC MCP)
**Primary pathway:** P1 — network hyperexcitability / cortical oscillatory disorganization
**Secondary pathway:** P2 — E/I balance; P4 — myelin (discussione)
**Model/species:** mouse — neuron-specific Wwox S-KO (Synapsin-Cre), P13–17
**Genotype/model:** neuron-specific conditional KO; non null/null sistemico, non compound het
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 021 · 002 (the sIPSC amplitude measurement this record carries is the competing, MEASURED account of the organoid GABA pattern — added 2026-09-27, `BATCH_20260927_004`, when `CLAIM 002` began citing it by wikilink; the edge is evidential, not an advisory-silencing declaration)
**Role:** fonte primaria verificata di CLAIM 021 (network-state pathology come core pathway); fonte della misura funzionale inibitoria che `CLAIM 002` oppone all'ipotesi immature-GABA
**Note:** Promosso 2026-07-05 (CC-2026-07-05-003) da placeholder corpus a PAPER pieno; CLAIM 021 era ancorato solo a [[paper_registry_current#CORPUS P210]] (identificato via review Obeid 2026), ora ancorato a full-text verificato. According to PubMed, [DOI](https://doi.org/10.1016/j.nbd.2021.105529). Contenuto verificato: burst neocorticali spontanei (36/42 slice KO vs 0/11 WT), assenti in ippocampo (patologia predominante di rete neocorticale), propagazione L2/3→L5 ~11 mm/s, accoppiamento fase-ampiezza delta-gamma/theta-HFO (biomarker epilessia pediatrica); burst **NMDAR-dipendenti** (d-APV abolisce) — ⚠️ **la metà gap-junction di questa dipendenza è RITIRATA come non attribuibile il 2026-09-27 (`BATCH_20260927_004`, `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`; vedi [[claim_registry_current#CLAIM 021]]) — ritiro di attribuzione, NON affermazione che le gap junction non siano coinvolte: l’occlusione non è mai stata testata.** Il carbenoxolone a 100 μM riduce la frequenza degli eventi dell’**87%** e la durata del **18%**, ma *«This did not return to normal levels after washout.»*, e gli autori stessi scrivono che *«CBX may not be specific to gap junctions»*. ⚠️ **E l’esclusione della pannexina NON è blanket — la sua narrowness viaggia con essa:** gli autori escludono quella via **per il solo effetto del CBX**, sulla base del BB-FCF (*«indicating that the suppressive effects of CBX were not due to pannexin 1 channel opening»*), **ma aggiungono immediatamente** che *«a subset of these bursts may be influenced by pannexin 1 channels»*, e in Discussion §3.4 che *«we cannot rule out the possibility that a pannexin 1 blocker could be an anti-epileptic treatment at earlier developmental»* stadi. Il precedente *«pannexina no»* era quindi falso come scritto; corretto il 2026-09-28 (Mirror `F2`), verificato su `files/fulltext/PMID34634460_Breton2021_EPMC_2026-09-27.xml`, sha256 `934b4e1a42ac19f5cd8912994fb171beabdeb94a6631b23d9a383dab1db906aa`); ↑ampiezza mEPSC (postsinaptico), ↓ampiezza+frequenza sIPSC (sbilancio E/I); piramidali L2/3 depolarizzati, ↑sag/Ih, ↑rebound post-inibitorio. Lead terapeutici (IPOTESI, non DATO): blocco gap-junction / modulazione NMDAR — ⚠️ CBX non specifico, Ih-blocker (ZD7288) controversi. ⚠️ Duplicati corpus **CORPUS P210** e **CORPUS P300** (stesso paper) → mergiare in un prossimo BATCH_COMMIT.
**Wikilinks:** [[claim_registry_current#CLAIM 021]]


## PAPER 032
**Short title:** Hussain 2018 WWOX interactome TAP-MS
**Full title:** Delineating WWOX Protein Interactome by Tandem Affinity Purification-Mass Spectrometry: Identification of Top Interactors and Key Metabolic Pathways Involved
**Authors:** Hussain T, Lee J, Abba MC, Chen J, Aldaz CM
**Year:** 2018
**Source type:** proteomics / interactome / TAP-MS
**Journal/source:** *Front Oncol* 2018;8:591
**Identifier:** PMID 30619736 / PMCID PMC6300487 / DOI 10.3389/fonc.2018.00591
**Status:** claim_linked
**Evidence depth:** complete_fulltext_read — `FTR-20260913-30619736-01`; manifest `deepdive_manifests/PMID30619736.json`
**Primary pathway:** P5 — trafficking / endomembrane systems / metabolism
**Secondary pathway:** P3 — Wnt/DVL / scaffold-interaction logic
**Model/species:** HEK293T TAP-MS / proteomics; validation co-IP/GST pulldown
**Genotype/model:** full-length WWOX SFB-tag interactome; not WWOX-DEE/patient model
**Transferability:** T3 — HEK293T tagged over-expression, no neural tissue or disease variant
**clinical relevance:** LOW — hypothesis-generating research only
**Claim links:** 026
**Role:** primary source for the prey list, trafficking-protein co-association and pathway annotation in `CLAIM 026`; no functional coupling assay
**Note:** Promoted 2026-07-05 from [[paper_registry_current#CORPUS P182]]; do not duplicate. The 216 prey passed CRAPome and MUSE computational filters, without an in-experiment control purification. Reciprocal co-IP of over-expressed proteins supports co-association with SEC23IP, SCAMP3 and VOPP1; lysate pull-down is shown for SEC23IP/SCAMP3, not VOPP1, and establishes no direct binding. InnateDB enrichment includes four metabolic and four non-metabolic pathways; the metabolic enzymes are outside the top-14 prey tier. No trafficking assay, metabolic flux or coupling experiment was performed. Acetyl-CoA convergence is a KEGG map interpretation; Figure 5B includes DBT although the filtered 216 exclude it. The `CLAIM 026` reading is therefore hypothesis-generating.
**Wikilinks:** [[claim_registry_current#CLAIM 026]]


## Registry rules
- Same PMID/DOI → update existing entry, do not duplicate
- Preprint later published → upgrade single record
- Title near-match without identifier → possible duplicate review
- No paper may be promoted operationally without genotype/model filter and clinical relevance evaluation

---

## CORPUS COVERAGE APPENDIX — Phase 1 alignment to 180-paper corpus
Purpose: add registry-level placeholders for corpus papers not yet ingested as full PAPER records, without renumbering or overwriting the existing registry.
Coverage note: matched corpus papers already represented in PAPER 001–025 = 12; new corpus placeholders added below = 168.
Rule: these records are registry placeholders only. They do NOT imply processing, claim linkage, or integration.

## CORPUS-STUB-001
**Corpus paper no:** 1
**Full title:** WWOX and Its Binding Proteins in Neurodegeneration
**Identifier:** PMID 34359949 / DOI 10.3390/cells10071781
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-003
**Corpus paper no:** 3
**Full title:** WWOX-Related Neurodevelopmental Disorders: Models and Future Perspectives
**Identifier:** PMID 34831305 / DOI 10.3390/cells10113082
**Status:** promoted — see [[paper_registry_current#PAPER 063]] (BATCH_20260810_005)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-004
**Status:** resolved — see [[paper_registry_current#PAPER 095]] (BATCH_20260920_002, `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`)
**Registry role:** corpus placeholder only — conservato append-only come storia di audit, mai cancellato
**Next action:** none — risolto
**Corpus paper no:** 4
**Full title:** WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders
**Identifier:** PMID 33255508 / DOI 10.3390/ijms21238922

**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-005
**Corpus paper no:** 5
**Full title:** WWOX, the FRA16D gene: A target of and a contributor to genomic instability
**Identifier:** PMID 30350478 / DOI 10.1002/gcc.22693
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-006
**Corpus paper no:** 6
**Full title:** WWOX Phosphorylation, Signaling, and Role in Neurodegeneration
**Identifier:** PMID 30158849 / DOI 10.3389/fnins.2018.00563
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none - upgraded (30158849 → `PAPER 150`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-007
**Corpus paper no:** 7
**Full title:** The WWOX gene in brain development and pathology
**Identifier:** PMID 32389029 / DOI 10.1177/1535370220924618
**Status:** promoted — see [[paper_registry_current#PAPER 153]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — upgraded to [[paper_registry_current#PAPER 153]] by `CC-20261003W4-A-REGISTRY-01`; this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-008
**Corpus paper no:** 8
**Full title:** WWOX: a fragile tumor suppressor
**Identifier:** PMID 25538133 / DOI 10.1177/1535370214561590
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-009
**Corpus paper no:** 9
**Full title:** WWOX Controls Cell Survival, Immune Response and Disease Progression by pY33 to pS14 Transition
**Identifier:** PMID 35883580 / DOI 10.3390/cells11142137
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-010
**Corpus paper no:** 10
**Full title:** Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration
**Identifier:** PMID 38542478 / DOI 10.3390/ijms25063507
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none - upgraded (38542478 → `PAPER 149`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-011
**Corpus paper no:** 11
**Full title:** Modeling WWOX Loss of Function in vivo: What Have We Learned?
**Identifier:** PMID 30370248 / DOI 10.3389/fonc.2018.00420
**Status:** promoted — see [[paper_registry_current#PAPER 067]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-012
**Corpus paper no:** 12
**Full title:** WWOX tumor suppressor gene
**Identifier:** PMID 18437686 / DOI 10.14670/HH-23.877
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-013
**Corpus paper no:** 13
**Full title:** Neurological Disorders Associated with WWOX Germline Mutations - A Comprehensive Overview
**Identifier:** PMID 33916893 / DOI 10.3390/cells10040824
**Status:** promoted — see [[paper_registry_current#PAPER 040]] (BATCH_20260710_B); placeholder kept as audit trail, do not duplicate
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-014
**Corpus paper no:** 14
**Full title:** WWOX Tumor Suppressor Gene in Breast Cancer, a Historical Perspective and Future Directions
**Identifier:** PMID 30211123 / DOI 10.3389/fonc.2018.00345
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-015
**Corpus paper no:** 15
**Full title:** WWOX tuning of oleic acid signaling orchestrates immunosuppressive macrophage polarization and sensitizes hepatocellular carcinoma to immunotherapy
**Identifier:** PMID 39500530 / DOI 10.1136/jitc-2024-010422
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-016
**Corpus paper no:** 16
**Full title:** WWOX in biological control and tumorigenesis
**Identifier:** PMID 17458891 / DOI 10.1002/jcp.21099
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-017
**Corpus paper no:** 17
**Full title:** WWOX: its genomics, partners, and functions
**Identifier:** PMID 19708029 / DOI 10.1002/jcb.22298
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-018
**Corpus paper no:** 18
**Full title:** Molecular Functions of WWOX Potentially Involved in Cancer Development
**Identifier:** PMID 33946771 / DOI 10.3390/cells10051051
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-019
**Corpus paper no:** 19
**Full title:** Molecular Biology of the WWOX Gene That Spans Chromosomal Fragile Site FRA16D
**Identifier:** PMID 34210081 / DOI 10.3390/cells10071637
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-020
**Corpus paper no:** 20
**Full title:** WWOX at the crossroads of cancer, metabolic syndrome related traits and CNS pathologies
**Identifier:** PMID 24932569 / DOI 10.1016/j.bbcan.2014.06.001
**Status:** promoted — see [[paper_registry_current#PAPER 053]] (BATCH_20260710_B); placeholder kept as audit trail, do not duplicate
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-021
**Corpus paper no:** 21
**Full title:** WWOX, large common fragile site genes, and cancer
**Identifier:** PMID 25595185 / DOI 10.1177/1535370214565992
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-022
**Status:** resolved — see [[paper_registry_current#CORPUS P022]] (BATCH_20260920_002, `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`)
**Registry role:** corpus placeholder only — conservato append-only come storia di audit, mai cancellato
**Next action:** none — risolto
**Corpus paper no:** 22
**Full title:** Decoding the link between WWOX and p53 in aggressive breast cancer
**Identifier:** PMID 31075076 / DOI 10.1080/15384101.2019.1616998

**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-023
**Corpus paper no:** 23
**Full title:** WWOX, the chromosomal fragile site FRA16D spanning gene: its role in metabolism and contribution to cancer
**Identifier:** PMID 25595186 / DOI 10.1177/1535370214565990
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-024
**Corpus paper no:** 24
**Full title:** WWOX Modulates ROS-Dependent Senescence in Bladder Cancer
**Identifier:** PMID 36364214 / DOI 10.3390/molecules27217388
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-025
**Corpus paper no:** 25
**Full title:** Alteration of WWOX in human cancer: a clinical view
**Identifier:** PMID 25681467 / DOI 10.1177/1535370214561953
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-026
**Corpus paper no:** 26
**Full title:** WWOX, a chromosomal fragile site gene and its role in cancer
**Identifier:** PMID 17163164 / DOI 10.1007/978-1-4020-5133-3_14
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-027
**Status:** resolved — see [[paper_registry_current#CORPUS P027]] (BATCH_20260920_002, `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`)
**Registry role:** corpus placeholder only — conservato append-only come storia di audit, mai cancellato
**Next action:** none — risolto
**Corpus paper no:** 27
**Full title:** WWOX promotes osteosarcoma development via upregulation of Myc
**Identifier:** PMID 38182577 / DOI 10.1038/s41419-023-06378-8

**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-028
**Corpus paper no:** 28
**Full title:** WWOX-mediated p53/SAT1 and NRF2/FPN1 axis contribute to toosendanin-induced ferroptosis in hepatocellular carcinoma
**Identifier:** PMID 39894307 / DOI 10.1016/j.bcp.2025.116790
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-029
**Corpus paper no:** 29
**Full title:** WWOX gene and gene product: tumor suppression through specific protein interactions
**Identifier:** PMID 20146584 / DOI 10.2217/fon.09.152
**Status:** promoted — see [[paper_registry_current#PAPER 085]] (BATCH_20260909_001, `CC-20260909-20146584-01`)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-031
**Corpus paper no:** 31
**Full title:** Loss of Endothelial WWOX: A Risk Factor for ARDS in Smokers?
**Identifier:** PMID 33105088 / DOI 10.1165/rcmb.2020-0444ED
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-032
**Corpus paper no:** 32
**Full title:** HYAL-2-WWOX-SMAD4 Signaling in Cell Death and Anticancer Response
**Identifier:** PMID 27999774 / DOI 10.3389/fcell.2016.00141
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-033
**Corpus paper no:** 33
**Full title:** Association between WWOX/MAF variants and dementia-related neuropathologic endophenotypes
**Identifier:** PMID 34852950 / DOI 10.1016/j.neurobiolaging.2021.10.011
**Status:** promoted — see [[paper_registry_current#PAPER 196]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — upgraded to [[paper_registry_current#PAPER 196]] by `CC-20261003W6-A-REGISTRY-01` (receipt `FTR-20261003-34852950-01`); this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-034
**Corpus paper no:** 34
**Full title:** The fragile site WWOX gene and the developing brain
**Identifier:** PMID 25416187 / DOI 10.1177/1535370214561952
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-035
**Corpus paper no:** 35
**Full title:** The Role of WWOX in Cancer Progression: Mechanisms and Therapeutic Potential
**Identifier:** PMID 41228229 / DOI 10.3390/cancers17213435
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-037
**Corpus paper no:** 37
**Full title:** Common Chromosomal Fragile Site Gene WWOX in Metabolic Disorders and Tumors
**Identifier:** PMID 24520212 / DOI 10.7150/ijbs.7727
**Status:** promoted — see [[paper_registry_current#PAPER 155]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — upgraded to [[paper_registry_current#PAPER 155]] by `CC-20261003W4-A-REGISTRY-01`; this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-038
**Corpus paper no:** 38
**Full title:** Roles of the WWOX in pathogenesis and endocrine therapy of breast cancer
**Identifier:** PMID 25476151 / DOI 10.1177/1535370214561587
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-039
**Corpus paper no:** 39
**Full title:** WWOX somatic ablation in skeletal muscles alters glucose metabolism
**Identifier:** PMID 30755385 / DOI 10.1016/j.molmet.2019.01.010
**Status:** promoted — see [[paper_registry_current#PAPER 061]] (BATCH_20260810_003, `CC-20260810-30755385`)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-040
**Corpus paper no:** 40
**Full title:** Role of WWOX and NF-kB in lung cancer progression
**Identifier:** PMID 27234396 / DOI 10.1186/2213-0802-1-15
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-041
**Corpus paper no:** 41
**Full title:** WWOX binds MERIT40 and modulates its function in homologous recombination, implications in breast cancer
**Identifier:** PMID 37248434 / DOI 10.1038/s41417-023-00626-x
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-042
**Corpus paper no:** 42
**Full title:** WWOX-Mediated Degradation of AMOTp130 Negatively Affects Egress of Filovirus VP40 Virus-Like Particles
**Identifier:** PMID 35107375 / DOI 10.1128/jvi.02026-21
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-043
**Corpus paper no:** 43
**Full title:** WWOX activates autophagy to alleviate lipopolysaccharide-induced acute lung injury by regulating mTOR
**Identifier:** PMID 36621327 / DOI 10.1016/j.intimp.2022.109671
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-044
**Corpus paper no:** 44
**Full title:** Pleiotropic Functions of Tumor Suppressor WWOX in Normal and Cancer Cells
**Identifier:** PMID 26499798 / DOI 10.1074/jbc.R115.676346
**Status:** promoted — see [[paper_registry_current#PAPER 089]] (BATCH_20260909_001, `CC-20260909-26499798-01`)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-045
**Corpus paper no:** 45
**Full title:** Phosphorylation/de-phosphorylation in specific sites of tumor suppressor WWOX and control of distinct biological events
**Identifier:** PMID 29310447 / DOI 10.1177/1535370217752350
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-046
**Corpus paper no:** 46
**Full title:** Wwox-Brca1 interaction: role in DNA repair pathway choice
**Identifier:** PMID 27869163 / DOI 10.1038/onc.2016.389
**Status:** promoted — see [[paper_registry_current#PAPER 109]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-047
**Corpus paper no:** 47
**Full title:** WWOX, the tumour suppressor gene affected in multiple cancers
**Identifier:** PMID 19609013
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-048
**Corpus paper no:** 48
**Full title:** Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes
**Identifier:** PMID 34747138 / DOI 10.15252/emmm.202114599
**Status:** promoted — duplicato di [[paper_registry_current#PAPER 005]], che esiste dal 2026-07-05 e ha ricevuto la lettura integrale il 2026-08-10 (BATCH_20260810_005)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-049
**Corpus paper no:** 49
**Full title:** WWOX-rs13338697 genotype predicts therapeutic efficacy of ADI-PEG 20 for patients with advanced hepatocellular carcinoma
**Identifier:** PMID 36530994 / DOI 10.3389/fonc.2022.996820
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-050
**Corpus paper no:** 50
**Full title:** Pleiotropic tumor suppressor functions of WWOX antagonize metastasis
**Identifier:** PMID 32300104 / DOI 10.1038/s41392-020-0136-8
**Status:** promoted — see [[paper_registry_current#PAPER 068]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-051
**Corpus paper no:** 51
**Full title:** Regulation of cell signaling and apoptosis by tumor suppressor WWOX
**Identifier:** PMID 25595191 / DOI 10.1177/1535370214566747
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-052
**Corpus paper no:** 52
**Full title:** Twenty-five years of WWOX insight in cancer: a treasure trove of knowledge
**Identifier:** PMID 40327201 / DOI 10.1007/s10142-025-01601-5
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-053
**Corpus paper no:** 53
**Full title:** WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice
**Identifier:** PMID 36828035 / DOI 10.1016/j.pneurobio.2023.102425
**Status:** promoted — see [[paper_registry_current#PAPER 112]] (`BATCH_20260926_ALDAZ_R1`), itself superseded by [[paper_registry_current#PAPER 007]] (`BATCH_20260926_ALDAZ`) — **cite `PAPER 007`**, the live record (pointer added by `BATCH_20260926_ALDAZ_R2`, `CC-20260914-PLACEHOLDER-IDENTITY-01`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-054
**Corpus paper no:** 54
**Full title:** Role of WWOX/WOX1 in Alzheimer's disease pathology and in cell death signaling
**Identifier:** PMID 22202011 / DOI 10.2741/e516
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-055
**Corpus paper no:** 55
**Full title:** The cancer gene WWOX behaves as an inhibitor of SMAD3 transcriptional activity via direct binding
**Identifier:** PMID 24330518 / DOI 10.1186/1471-2407-13-593
**Status:** promoted — see [[paper_registry_current#PAPER 108]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-056
**Corpus paper no:** 56
**Full title:** WWOX promotes apoptosis and inhibits autophagy in paclitaxel-treated ovarian carcinoma cells
**Identifier:** PMID 33300063 / DOI 10.3892/mmr.2020.11754
**Status:** promoted — see [[paper_registry_current#PAPER 152]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — upgraded to [[paper_registry_current#PAPER 152]] by `CC-20261003W4-A-REGISTRY-01`; this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-057
**Corpus paper no:** 57
**Full title:** WWOX Polymorphisms as Predictors of the Biochemical Recurrence of Localized Prostate Cancer after Radical Prostatectomy
**Identifier:** PMID 37324196 / DOI 10.7150/ijms.84364
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-058
**Corpus paper no:** 58
**Full title:** Phosphorylation of the WWOX Protein Regulates Its Interaction with p73
**Identifier:** PMID 32185845 / DOI 10.1002/cbic.202000032
**Status:** superseded
**Registry role:** preserved corpus placeholder
**Claim links:** 028
**Next action:** none — upgraded to PAPER 026
**Note:** Preserved for lossless corpus alignment. Full integrated record now lives in PAPER 026.

## CORPUS-STUB-059
**Corpus paper no:** 59
**Full title:** The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature
**Identifier:** PMID 30356099 / DOI 10.1038/s41436-018-0339-3
**Status:** superseded
**Registry role:** preserved corpus placeholder — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — upgraded to PAPER 117
**Note:** Preserved for lossless corpus alignment. Full integrated record now lives in [[paper_registry_current#PAPER 117]] (`BATCH_20260927_003`). 🔴 **Restored 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` (Mirror N6):** `BATCH_20260927_003` deleted this placeholder rather than preserving it, on a reason — *"no record with an empty `Authors` field survives for a byline to be borrowed from again"* — that did not distinguish it from the 167 stubs which have no `Authors` field either. **The convention, written down once here:** a placeholder promoted to a full record is re-statused `superseded` and kept, never deleted; the audit trail from corpus ordinal to PAPER record is the whole point of the placeholder. The byline hazard is carried by `PAPER 025`'s and `PAPER 117`'s own notes instead.

## CORPUS-STUB-060
**Corpus paper no:** 60
**Full title:** Epilepsy in patients with WWOX-related epileptic encephalopathy (WOREE) syndrome
**Identifier:** PMID 35792847 / DOI 10.1684/epd.2022.1444
**Status:** promoted — see [[paper_registry_current#PAPER 171]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — upgraded to [[paper_registry_current#PAPER 171]] by `CC-20261003W5-B-REGISTRY-01` (receipt `FTR-20261003-35792847-01`); this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-061
**Corpus paper no:** 61
**Full title:** Functions and Epigenetic Regulation of Wwox in Bone Metastasis from Breast Carcinoma
**Identifier:** PMID 28045433 / DOI 10.3390/ijms18010075
**Status:** background_only
**Registry role:** corpus placeholder only
**Claim links:** none
**Integrity status:** dependency-contaminated
**Next action:** none — non usare come corroborazione; riaprire solo dopo audit fonte-per-fonte indipendente
**Note:** URG_2026-07-09_001 (2026-07-10): review declassata perché riusa dati del primario Bendinelli et al. 2017, PMID 28151481 / DOI 10.1038/cddis.2016.403, ritirato nel 2022 (DOI retraction 10.1038/s41419-022-04992-6) per duplicazione/riuso/manipolazione di controlli western blot. La review dipende inoltre da altre fonti della stessa linea con segnali di integrità. Nessun claim canonico la utilizza. Conservata lossless come audit trail, non come evidenza.

## CORPUS-STUB-062
**Corpus paper no:** 62
**Full title:** Influence of WWOX/MAF genes on cognitive performance in patients with Parkinson's disease
**Identifier:** PMID 40139278 / DOI 10.1016/j.nbd.2025.106887
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-063
**Corpus paper no:** 63
**Full title:** WWOX activation by toosendanin suppresses hepatocellular carcinoma metastasis through JAK2/Stat3 and Wnt/beta-catenin signaling
**Identifier:** PMID 34015398 / DOI 10.1016/j.canlet.2021.05.010
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-065
**Corpus paper no:** 65
**Full title:** WWOX attenuates the progression of gallbladder cancer by suppressing cellular glycolysis through the modulation of the P73/HIF-1alpha signaling pathway
**Identifier:** PMID 40198927 / DOI 10.1016/j.tice.2025.102885
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-066
**Corpus paper no:** 66
**Full title:** WWOX protects against ferroptosis to alleviate acute lung injury by mediating p53 deacetylation
**Identifier:** PMID 41443103 / DOI 10.1016/j.intimp.2025.116067
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-067
**Corpus paper no:** 67
**Full title:** Role of WW domain proteins WWOX in development, prognosis, and treatment response of glioma
**Identifier:** PMID 25432984 / DOI 10.1177/1535370214561588
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-068
**Corpus paper no:** 68
**Full title:** Mechanistic Investigation of WWOX Function in NF-kB-Induced Skin Inflammation in Psoriasis
**Identifier:** PMID 38203337 / DOI 10.3390/ijms25010167
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-069
**Corpus paper no:** 69
**Full title:** WWOX Inhibits Metastasis of Triple-Negative Breast Cancer Cells via Modulation of miRNAs
**Identifier:** PMID 30622118 / DOI 10.1158/0008-5472.CAN-18-0614
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-070
**Corpus paper no:** 70
**Full title:** WWOX inhibition by Zfra1-31 restores mitochondrial homeostasis and viability of neuronal cells exposed to high glucose
**Identifier:** PMID 35984507 / DOI 10.1007/s00018-022-04508-7
**Status:** promoted — see [[paper_registry_current#PAPER 097]] (`BATCH_20260921_002`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-071
**Corpus paper no:** 71
**Full title:** WWOX, a new potential tumor suppressor gene
**Identifier:** PMID 17690733 / DOI 10.5507/bp.2007.002
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-072
**Corpus paper no:** 72
**Full title:** Decreased WWOX expression promotes angiogenesis in osteosarcoma
**Identifier:** PMID 28977834 / DOI 10.18632/oncotarget.17126
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-073
**Corpus paper no:** 73
**Full title:** WWOX controls hepatic HIF1alpha to suppress hepatocyte proliferation and neoplasia
**Identifier:** PMID 29724996 / DOI 10.1038/s41419-018-0510-4
**Status:** promoted — see [[paper_registry_current#PAPER 091]] (BATCH_20260909_001, `CC-20260909-29724996-01`)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-074
**Corpus paper no:** 74
**Full title:** Wwox Binding to the Murine Brca1-BRCT Domain Regulates Timing of Brip1 and CtIP Phospho-Protein Interactions
**Identifier:** PMID 35409089 / DOI 10.3390/ijms23073729
**Status:** promoted — see [[paper_registry_current#PAPER 111]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-075
**Corpus paper no:** 75
**Full title:** Wwox inactivation enhances mammary tumorigenesis
**Identifier:** PMID 21499303 / DOI 10.1038/onc.2011.115
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-076
**Corpus paper no:** 76
**Full title:** Loss of tumor suppressor WWOX accelerates pancreatic cancer development through promotion of TGFbeta/BMP2 signaling
**Identifier:** PMID 36572673 / DOI 10.1038/s41419-022-05519-9
**Status:** promoted — see [[paper_registry_current#PAPER 069]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-077
**Corpus paper no:** 77
**Full title:** Loss of fragile WWOX gene leads to senescence escape and genome instability
**Identifier:** PMID 37897534 / DOI 10.1007/s00018-023-04950-1
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record. **Promoted 2026-10-02 to [[paper_registry_current#PAPER 130]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (first-hand `partial_fulltext_read`, receipt `FTR-20261002-37897534-01`); this placeholder is kept as history and its `Status: not_processed` describes the placeholder, not the paper.**

## CORPUS-STUB-078
**Corpus paper no:** 78
**Full title:** WWOX loss activates aerobic glycolysis
**Identifier:** PMID 27308416 / DOI 10.4161/23723548.2014.965640
**Status:** promoted — see [[paper_registry_current#PAPER 072]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-079
**Corpus paper no:** 79
**Full title:** Cancerous Protein Network That Inhibits the Tumor Suppressor Function of WWOX
**Identifier:** PMID 30214895 / DOI 10.3389/fonc.2018.00350
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-080
**Corpus paper no:** 80
**Full title:** WWOX regulates the Elf5/Snail1 pathway to affect epithelial-mesenchymal transition of ovarian carcinoma cells
**Identifier:** PMID 32096174 / DOI 10.26355/eurrev_202002_20154
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-081
**Corpus paper no:** 81
**Full title:** WWOX modulates the ATR-mediated DNA damage checkpoint response
**Identifier:** PMID 26675548 / DOI 10.18632/oncotarget.6571
**Status:** promoted — see [[paper_registry_current#PAPER 080]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-082
**Corpus paper no:** 82
**Full title:** Roles of FHIT and WWOX fragile genes in cancer
**Identifier:** PMID 16225988 / DOI 10.1016/j.canlet.2005.06.048
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-083
**Corpus paper no:** 83
**Full title:** Wwox Deficiency Causes Downregulation of Prosurvival ERK Signaling and Abnormal Homeostatic Responses in Mouse Skin
**Identifier:** PMID 33195192 / DOI 10.3389/fcell.2020.558432
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record. **Promoted 2026-10-02 to [[paper_registry_current#PAPER 129]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (first-hand `partial_fulltext_read`, receipt `FTR-20261002-33195192-01`); this placeholder is kept as history and its `Status: not_processed` describes the placeholder, not the paper.**

## CORPUS-STUB-084
**Corpus paper no:** 84
**Full title:** Interaction of Wwox with Brca1 and associated complex proteins prevents premature resection at double-strand breaks
**Identifier:** PMID 34998176 / DOI 10.1016/j.dnarep.2021.103264
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-085
**Corpus paper no:** 85
**Full title:** Wwox deletion leads to reduced GABA-ergic inhibitory interneuron numbers and activation of microglia and astrocytes in mouse hippocampus
**Identifier:** PMID 30290271 / DOI 10.1016/j.nbd.2018.09.026
**Status:** resolved — duplicate of [[paper_registry_current#PAPER 006]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — the full processed record lives in PAPER 006
**Note:** Added during Phase 1 corpus-to-registry alignment. Resolved 2026-08-06 as the same publication as PAPER 006, which carries the complete-read receipt `FTR-20260806-30290271-01`. Preserved lossless as append-only history, not deleted and not a second record of the same paper.

## CORPUS-STUB-086
**Corpus paper no:** 86
**Full title:** WWOX rs11644322 Polymorphism, Gemcitabine, and Pancreatic Cancer
**Identifier:** PMID 29200707 / DOI 10.4103/ijmpo.ijmpo_125_17
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-087
**Corpus paper no:** 87
**Full title:** Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects
**Identifier:** PMID 33914858 / DOI 10.1093/brain/awab174
**Status:** superseded — identità duplicata
**Registry role:** puntatore storico; il record vivo di questo DOI è [[paper_registry_current#PAPER 004]]
**Claim links:** none
**Next action:** nessuna. Mergiato il 2026-10-03 con `CC-20261003W4-B-REGISTRY-01`, come la nota di `PAPER 004` chiedeva dal 2026-07-05. Il testo originale dello stub è conservato sopra; nulla è cancellato.
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-088
**Corpus paper no:** 88
**Full title:** Wwox Deletion in Mouse B Cells Leads to Genomic Instability, Neoplastic Transformation, and Monoclonal Gammopathies
**Identifier:** PMID 31275852 / DOI 10.3389/fonc.2019.00517
**Status:** promoted — see [[paper_registry_current#PAPER 110]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-089
**Corpus paper no:** 89
**Full title:** Role of WWOX/WOX1 in Alzheimer's disease pathology and in cell death signaling (Schol Ed)
**Identifier:** PMID 23277037 / DOI 10.2741/s358
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-090
**Corpus paper no:** 90
**Full title:** Genotype and phenotype of WWOX gene related developmental and epileptic encephalopathy [Chinese]
**Identifier:** PMID 39039877 / DOI 10.3760/cma.j.cn112140-20240229-00135
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-091
**Corpus paper no:** 91
**Full title:** Loss of lung WWOX expression causes neutrophilic inflammation
**Identifier:** PMID 28283473 / DOI 10.1152/ajplung.00034.2017
**Status:** promoted — see [[paper_registry_current#PAPER 102]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-092
**Corpus paper no:** 92
**Full title:** WWOX Loses the Ability to Regulate Oncogenic AP-2gamma and Synergizes with Tumor Suppressor AP-2alpha in High-Grade Bladder Cancer
**Identifier:** PMID 34204827 / DOI 10.3390/cancers13122957
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-094
**Corpus paper no:** 94
**Full title:** Loss of WWOX contributes to cisplatin resistance in triple-negative breast cancer cells by modulating miR-182 and miR-214
**Identifier:** PMID 39473747 / DOI 10.55730/1300-0144.5891
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-095
**Corpus paper no:** 95
**Full title:** LINC01137/miR-186-5p/WWOX: a novel axis identified from WWOX-related RNA interactome in bladder cancer
**Identifier:** PMID 37519886 / DOI 10.3389/fgene.2023.1214968
**Status:** promoted — see [[paper_registry_current#PAPER 060]] (BATCH_20260810_002, `CC-20260805-001`)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-096
**Corpus paper no:** 96
**Full title:** Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome
**Identifier:** PMID 37974179 / DOI 10.1186/s12920-023-01731-4
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — upgraded to [[paper_registry_current#PAPER 134]] by `CC-20261003-A-REGISTRY-01` (receipt `FTR-20261003-37974179-01`); this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-098
**Corpus paper no:** 98
**Full title:** Albendazole exerts an anti-hepatocellular carcinoma effect through a WWOX-dependent pathway
**Identifier:** PMID 36257459 / DOI 10.1016/j.lfs.2022.121086
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-099
**Corpus paper no:** 99
**Full title:** RHBDD2-WWOX protein interaction during proliferative and differentiated stages in normal and breast cancer cells
**Identifier:** PMID 34109992 / DOI 10.3892/or.2021.8108
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-100
**Corpus paper no:** 100
**Full title:** Antineoplastic Nature of WWOX in Glioblastoma Is Mainly a Consequence of Reduced Cell Viability and Invasion
**Identifier:** PMID 36979157 / DOI 10.3390/biology12030465
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-101
**Corpus paper no:** 101
**Full title:** Integrative multi-omics and Mendelian randomization identify WWOX and THBS2 as potential therapeutic targets in mature T/NK-cell lymphoma
**Identifier:** PMID 41254692 / DOI 10.1186/s12967-025-07301-9
**Status:** promoted — see [[paper_registry_current#PAPER 222]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — read at full text in intake wave 8 (2026-10-04), receipt `FTR-20261004-41254692-01`, landed as [[paper_registry_current#PAPER 222]]; its phase-2 placeholder twin [[literature_tracking_log_current#LIT-0122]] is retired with it (`BATCH_20261004_002`)
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-102
**Corpus paper no:** 102
**Full title:** WWOX and p53 Dysregulation Synergize to Drive the Development of Osteosarcoma
**Identifier:** PMID 27550453 / DOI 10.1158/0008-5472.CAN-16-0621
**Status:** promoted — see [[paper_registry_current#PAPER 065]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-103
**Corpus paper no:** 103
**Full title:** Correlation between osteosarcoma and the expression of WWOX and p53
**Identifier:** PMID 29085479 / DOI 10.3892/ol.2017.6747
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-104
**Corpus paper no:** 104
**Full title:** The common fragile site FRA16D gene product WWOX: roles in tumor suppression and genomic stability
**Identifier:** PMID 25245215 / DOI 10.1007/s00018-014-1724-y
**Status:** promoted — see [[paper_registry_current#PAPER 088]] (BATCH_20260909_001, `CC-20260909-25245215-01`)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-105
**Corpus paper no:** 105
**Full title:** WWOX inhibits the invasion of lung cancer cells by downregulating RUNX2
**Identifier:** PMID 27834355 / DOI 10.1038/cgt.2016.59
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-107
**Corpus paper no:** 107
**Full title:** WWOX protein expression in normal human tissues
**Identifier:** PMID 16941225 / DOI 10.1007/s10735-006-9046-5
**Status:** promoted — see [[paper_registry_current#PAPER 106]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-108
**Corpus paper no:** 108
**Full title:** The WWOX gene modulates high-density lipoprotein and lipid metabolism
**Identifier:** PMID 24871327 / DOI 10.1161/CIRCGENETICS.113.000248
**Status:** promoted — see [[paper_registry_current#PAPER 062]] (BATCH_20260810_004)
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-109
**Corpus paper no:** 109
**Full title:** Associations between TUBB-WWOX SNPs, their haplotypes, gene-gene, and gene-environment interactions and dyslipidemia
**Identifier:** PMID 33612478 / DOI 10.18632/aging.202514
**Status:** processed — letto per intero il 2026-10-03, verdetto **OFF-AXIS**
**Registry role:** record di lettura; nessuna claim ne discende
**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20261003-33612478-01`, JATS Europe PMC (PMC7950260), manifest `deepdive_manifests/PMID33612478.json` (4 locator, validatore PASS), dossier `fulltext_dossiers/PMID33612478.md`
**Claim links:** none
**Next action:** nessuna. 🔴 **DO_NOT_CITE a sostegno di un effetto di dose di WWOX sui lipidi.** Studio di associazione su SNP comuni (MAF > 10% per costruzione) in una sola popolazione; i due SNP assegnati a WWOX distano circa 500 kb e sono in LD debole **per ammissione degli autori**, e le posizioni che il lavoro stesso stampa collocano rs2222896 **fuori dal corpo del gene** WWOX nello stesso build usato da `PAPER 156`; gli autori **ritirano** l'associazione rs2548861–HDL-C («we speculated that mutations at rs2548861 were not correlated with HDL-C concentration in these subjects»); nulla di WWOX è misurato o perturbato, e gli autori elencano il lavoro funzionale fra i propri limiti. Due incoerenze interne registrate: l'abstract dà l'interazione rs3132584 × rs2222896 come 2.548× «and predicted hypertension» mentre i Risultati danno 1.523× per l'ipertensione, e la Tabella 1 stampa il peso del gruppo normale come 54.48 ± 110.29 kg.
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-110
**Corpus paper no:** 110
**Full title:** Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation [PREPRINT bioRxiv]
**Identifier:** PMID 39868255 / DOI 10.1101/2025.01.17.633677
**Status:** promoted — see [[paper_registry_current#PAPER 114]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-111
**Corpus paper no:** 111
**Full title:** Remote modulation of WWOX by an intronic variant associated with survival of Chinese gastric cancer patients
**Identifier:** PMID 37615513 / DOI 10.1002/ijc.34703
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-112
**Corpus paper no:** 112
**Full title:** Fragile Gene WWOX Guides TFAP2A/TFAP2C-Dependent Actions Against Tumor Progression in Grade II Bladder Cancer
**Identifier:** PMID 33718178 / DOI 10.3389/fonc.2021.621060
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-113
**Status:** resolved — see [[paper_registry_current#CORPUS P113]] (BATCH_20260920_002, `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`)
**Registry role:** corpus placeholder only — conservato append-only come storia di audit, mai cancellato
**Next action:** none — risolto
**Corpus paper no:** 113
**Full title:** Unveiling the relationship between WWOX and BRCA1 in mammary tumorigenicity and in DNA repair pathway selection
**Identifier:** PMID 38499540 / DOI 10.1038/s41420-024-01878-8

**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-114
**Corpus paper no:** 114
**Full title:** WWOX-related encephalopathies: delineation of the phenotypical spectrum and emerging genotype-phenotype correlation
**Identifier:** PMID 25411445 / DOI 10.1136/jmedgenet-2014-102748
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-115
**Corpus paper no:** 115
**Full title:** Introduction to a thematic issue for WWOX
**Identifier:** PMID 25802472 / DOI 10.1177/1535370215574226
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-116
**Corpus paper no:** 116
**Full title:** Determination of WWOX Function in Modulating Cellular Pathways Activated by AP-2alpha and AP-2gamma Transcription Factors in Bladder Cancer
**Identifier:** PMID 35563688 / DOI 10.3390/cells11091382
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-117
**Corpus paper no:** 117
**Full title:** Wwox suppresses breast cancer cell growth through modulation of the hedgehog-GLI1 signaling pathway
**Identifier:** PMID 24393846 / DOI 10.1016/j.bbrc.2013.12.133
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-119
**Corpus paper no:** 119
**Full title:** WWOX gene restoration prevents lung cancer growth in vitro and in vivo
**Identifier:** PMID 16223882 / DOI 10.1073/pnas.0505485102
**Status:** promoted — see [[paper_registry_current#PAPER 082]] (BATCH_20260909_001, `CC-20260909-16223882-01`)
**Integrity status:** 🔴 `PUBLICATION_INTEGRITY_HOLD` — **expression of concern**. Field added in `BATCH_20260806_002`, closing a debt declared on 2026-08-06. **No canonical claim rests on this record.** It is cited once, as reference 17 of [[paper_registry_current#PAPER 057]], among four background xenograft examples in that paper's Introduction, and supports none of its measured results — verified during the complete read (`FTR-20260806-19936220-01`). Not admissible as evidentiary support; admissible only as bibliographic lineage.
**Registry role:** corpus placeholder only — **conservato append-only come storia di audit, mai cancellato**
**Claim links:** none
**Next action:** none — risolto per promozione
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-120
**Corpus paper no:** 120
**Full title:** Endothelial knockdown of WWOX increases inflammation in ventilator-induced lung injury
**Identifier:** PMID 38563965 / DOI 10.1152/ajplung.00277.2023
**Status:** promoted — see [[paper_registry_current#PAPER 113]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-121
**Corpus paper no:** 121
**Full title:** WWOX-mediated apoptosis in A549 cells mainly involves the mitochondrial pathway
**Identifier:** PMID 22484428 / DOI 10.3892/mmr.2012.860
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-122
**Corpus paper no:** 122
**Full title:** WWOX expression in giant cell lesions of the jaws
**Identifier:** PMID 23849374 / DOI 10.1016/j.oooo.2013.05.007
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-123
**Status:** resolved — see [[paper_registry_current#CORPUS P123]] (BATCH_20260920_002, `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`)
**Registry role:** corpus placeholder only — conservato append-only come storia di audit, mai cancellato
**Next action:** none — risolto
**Corpus paper no:** 123
**Full title:** WWOX guards genome stability by activating ATM
**Identifier:** PMID 27308504 / DOI 10.1080/23723556.2015.1008288

**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-124
**Corpus paper no:** 124
**Full title:** WWOX Possesses N-Terminal Cell Surface-Exposed Epitopes WWOX7-21 and WWOX7-11 for Signaling Cancer Growth Suppression
**Identifier:** PMID 31752354 / DOI 10.3390/cancers11111818
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-125
**Corpus paper no:** 125
**Full title:** Tumor suppressor WWOX moderates the mitochondrial respiratory complex
**Identifier:** PMID 26390919 / DOI 10.1002/gcc.22286
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-126
**Corpus paper no:** 126
**Full title:** WWOX sensitises ovarian cancer cells to paclitaxel via modulation of the ER stress response
**Identifier:** PMID 28749468 / DOI 10.1038/cddis.2017.346
**Status:** processed
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-28749468-01`; manifest `deepdive_manifests/PMID28749468.json` (9 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID28749468.md`
**Primary pathway:** ER stress / UPR (oncological context)
**Model/species:** human ovarian carcinoma cell lines; PEO1 is a WWOX-null by homozygous deletion of exons 4-8. No neural material anywhere in the paper
**Transferability:** T3 — no WWOX allele of the reference genotype class; the stressor is a chemotherapeutic
**clinical relevance:** BACKGROUND
**Role:** 🔴 Every quantified endpoint measures WWOX as **pro-death under stress**: restoring it roughly halves survival under paclitaxel and tunicamycin, removing it roughly doubles it. A «rescue» in this system is the restoration of the cell's ability to die, which is the wrong sign for a neurodevelopmental disorder — recorded as a cross-species direction in `CC-20261003-C-APOPTOSIS-DIRECTION-01`. ⚠️ The paper's central IRE-1 claim is weaker than its prose: Figures 5c-5e carry **no significance marker and no P-value at all**, the absolute viability increment from KIRA6 is the same in the WWOX-expressing and WWOX-null clones (about 0.19 against about 0.18), Figure 7e is reported as positive and prints `p=0.13`, and the Figure 6 legend declares panels a-h for a six-panel figure
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record. 🟢 **Read first-hand 2026-10-03 (`CC-20261003-C-REGISTRY-01`, intake wave 2, Scientist C); the stub is enriched rather than promoted, and the placeholder is kept as history.** Not medical advice.
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-127
**Corpus paper no:** 127
**Full title:** Dissociation of the nuclear WWOX/TRAF2 switch renders UV/cold shock-mediated nuclear bubbling cell death at low temperatures
**Identifier:** PMID 39420317 / DOI 10.1186/s12964-024-01866-6
**Status:** superseded
**Registry role:** preserved corpus placeholder
**Claim links:** 028 supportive only
**Next action:** none — upgraded to PAPER 028
**Note:** Preserved for lossless corpus alignment. Full processed record now lives in PAPER 028.

## CORPUS-STUB-128
**Corpus paper no:** 128
**Full title:** Methylation of WWOX gene promotes proliferation of osteosarcoma cells
**Identifier:** PMID 33455117
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-129
**Corpus paper no:** 129
**Full title:** Loss of Wwox drives metastasis in triple-negative breast cancer by JAK2/STAT3 axis
**Identifier:** PMID 30154439 / DOI 10.1038/s41467-018-05852-8
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-130
**Corpus paper no:** 130
**Full title:** WWOX, the common chromosomal fragile site, FRA16D, cancer gene
**Identifier:** PMID 14526170 / DOI 10.1159/000072844
**Status:** promoted — see [[paper_registry_current#PAPER 101]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-131
**Corpus paper no:** 131
**Full title:** Characterization of WWOX expression and function in canine mast cell tumors and malignant mast cell lines
**Identifier:** PMID 33129329 / DOI 10.1186/s12917-020-02638-3
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-132
**Corpus paper no:** 132
**Full title:** Silencing of Wwox Increases Nuclear Import of Dvl proteins in Head and Neck Cancer
**Identifier:** PMID 32368285 / DOI 10.7150/jca.40840
**Status:** promoted — see [[paper_registry_current#PAPER 201]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — read at full text in intake wave 7 (2026-10-04), receipt `FTR-20261004-32368285-01`
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-133
**Corpus paper no:** 133
**Full title:** WWOX: a candidate tumor suppressor gene involved in multiple tumor types
**Identifier:** PMID 11572989 / DOI 10.1073/pnas.191175898
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-134
**Corpus paper no:** 134
**Full title:** Analysis of WWOX gene expression and protein levels in pterygium
**Identifier:** PMID 32314321 / DOI 10.1007/s10792-020-01368-7
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-135
**Corpus paper no:** 135
**Full title:** WWOX — the FRA16D cancer gene: expression correlation with breast cancer progression and prognosis
**Identifier:** PMID 16360296 / DOI 10.1016/j.ejso.2005.11.002
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-136
**Corpus paper no:** 136
**Full title:** LncRNA WWOX-AS1 sponges miR-20b-5p in hepatocellular carcinoma and represses its progression by upregulating WWOX
**Identifier:** PMID 32931356 / DOI 10.1080/15384047.2020.1806689
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-137
**Corpus paper no:** 137
**Full title:** The WWOX tumor suppressor gene in endometrial adenocarcinoma
**Identifier:** PMID 24126431 / DOI 10.3892/ijmm.2013.1526
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-138
**Corpus paper no:** 138
**Full title:** WWOX, the common fragile site FRA16D gene product, regulates ATM activation and the DNA damage response
**Identifier:** PMID 25331887 / DOI 10.1073/pnas.1409252111
**Status:** superseded
**Registry role:** preserved corpus placeholder
**Claim links:** 029
**Next action:** none — upgraded to PAPER 027
**Note:** Preserved for lossless corpus alignment. Full integrated record now lives in PAPER 027.

## CORPUS-STUB-139
**Corpus paper no:** 139
**Full title:** WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated human squamous cell carcinoma
**Identifier:** PMID 24008736 / DOI 10.1038/cddis.2013.308
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none - upgraded (24008736 → `PAPER 148`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-140
**Corpus paper no:** 140
**Full title:** The role of the WWOX gene in leukemia and its mechanisms of action
**Identifier:** PMID 23525648 / DOI 10.3892/or.2013.2361
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-141
**Corpus paper no:** 141
**Full title:** Novel Mutation With Literature Review WW Domain-Containing Oxidoreductase (WWOX) Gene
**Identifier:** PMID 35712340 / DOI 10.7759/cureus.25003
**Status:** promoted — see [[paper_registry_current#PAPER 144]]
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none — upgraded to [[paper_registry_current#PAPER 144]] by `CC-20261003W3-A-REGISTRY-01` (receipt `FTR-20261003-35712340-01`); this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-142
**Corpus paper no:** 142
**Full title:** WWOX suppresses proliferation and induces apoptosis via G2 arrest and caspase 3 pathway in nasopharyngeal carcinoma cells
**Identifier:** PMID 31966508
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-143
**Corpus paper no:** 143
**Full title:** WWOX binds the specific proline-rich ligand PPXY: identification of candidate interacting proteins
**Identifier:** PMID 15064722 / DOI 10.1038/sj.onc.1207680
**Status:** promoted — see [[paper_registry_current#PAPER 104]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-145
**Corpus paper no:** 145
**Full title:** Reduced WWOX protein expression in human astrocytoma
**Identifier:** PMID 23675860 / DOI 10.1111/neup.12040
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-146
**Corpus paper no:** 146
**Full title:** WWOX induces apoptosis and inhibits proliferation in cervical cancer and cell lines
**Identifier:** PMID 23525362 / DOI 10.3892/ijmm.2013.1314
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-147
**Corpus paper no:** 147
**Full title:** WWOX Induction Promotes Bcl-XL and Mcl-1 Degradation Through a Lysosomal Pathway upon Stress Response
**Identifier:** PMID 41677633 / DOI 10.3390/cells15030270
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** none - upgraded (41677633 → `PAPER 147`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-148
**Corpus paper no:** 148
**Full title:** WWOX protein expression varies among ovarian carcinoma histotypes and correlates with less favorable prognosis
**Identifier:** PMID 15982416 / DOI 10.1186/1471-2407-5-64
**Status:** promoted — see [[paper_registry_current#PAPER 105]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-149
**Corpus paper no:** 149
**Full title:** Wwox suppresses prostate cancer cell growth through modulation of ErbB2-mediated androgen receptor signaling
**Identifier:** PMID 17704139 / DOI 10.1158/1541-7786.MCR-07-0211
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-150
**Corpus paper no:** 150
**Full title:** Normal cells repel WWOX-negative or -dysfunctional cancer cells via WWOX cell surface epitope 286-299
**Identifier:** PMID 34140629 / DOI 10.1038/s42003-021-02271-2
**Status:** promoted — see [[paper_registry_current#PAPER 096]] (`BATCH_20260921_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-152
**Corpus paper no:** 152
**Full title:** Tumor Suppressor WWOX inhibits osteosarcoma metastasis by modulating RUNX2 function
**Identifier:** PMID 26256646 / DOI 10.1038/srep12959
**Status:** promoted — see [[paper_registry_current#PAPER 074]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-153
**Corpus paper no:** 153
**Full title:** Cellular Expression and Subcellular Localization of Wwox Protein During Testicular Development and Spermatogenesis
**Identifier:** PMID 33565365 / DOI 10.1369/0022155421991629
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-154
**Corpus paper no:** 154
**Full title:** Downregulated Expression of WWOX in Cervical Carcinoma: A Case-Control Study
**Identifier:** PMID 33688485 / DOI 10.22088/IJMCM.BUMS.9.4.273
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-155
**Corpus paper no:** 155
**Full title:** TGFalpha-EGFR pathway in breast carcinogenesis, association with WWOX expression and estrogen activation
**Identifier:** PMID 35290621 / DOI 10.1007/s13353-022-00690-3
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-156
**Corpus paper no:** 156
**Full title:** WWOX dysfunction induces sequential aggregation of TRAPPC6ADelta, TIAF1, tau and amyloid beta, and causes apoptosis
**Identifier:** PMID 27551439 / DOI 10.1038/cddiscovery.2015.3
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-157
**Corpus paper no:** 157
**Full title:** EHBP1, TUBB, and WWOX SNPs, Gene-Gene and Gene-Environment Interactions on Coronary Artery Disease and Hypertension
**Identifier:** PMID 35559044 / DOI 10.3389/fgene.2022.843661
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-158
**Corpus paper no:** 158
**Full title:** WWOX gene expression abolishes ovarian cancer tumorigenicity in vivo and decreases attachment to fibronectin via the ITGA3 integrin
**Identifier:** PMID 19458077 / DOI 10.1158/0008-5472.CAN-08-2974
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-159
**Corpus paper no:** 159
**Full title:** LncRNA WWOX-AS1 inhibits the proliferation, migration and invasion of osteosarcoma cells
**Identifier:** PMID 29845204 / DOI 10.3892/mmr.2018.9058
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-160
**Corpus paper no:** 160
**Full title:** WWOX expression in different histologic types and subtypes of non-small cell lung cancer
**Identifier:** PMID 17289881 / DOI 10.1158/1078-0432.CCR-06-2016
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-161
**Corpus paper no:** 161
**Full title:** Deregulated WWOX is involved in a negative feedback loop with microRNA-214-3p in osteosarcoma
**Identifier:** PMID 27840941 / DOI 10.3892/ijmm.2016.2800
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-162
**Corpus paper no:** 162
**Full title:** WWOX modulates the gene expression profile in the T98G glioblastoma cell line rendering its phenotype
**Identifier:** PMID 25051421 / DOI 10.3892/or.2014.3335
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-164
**Corpus paper no:** 164
**Full title:** Somatic loss of WWOX is associated with TP53 perturbation in basal-like breast cancer
**Identifier:** PMID 30082886 / DOI 10.1038/s41419-018-0896-z
**Status:** promoted — see [[paper_registry_current#PAPER 066]] (`BATCH_20260815_001`)
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-165
**Corpus paper no:** 165
**Full title:** VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX
**Identifier:** PMID 30285739 / DOI 10.1186/s12915-018-0576-6
**Status:** promoted — see [[paper_registry_current#PAPER 103]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-166
**Corpus paper no:** 166
**Full title:** Recently defined epileptic encephalopathy related to WWOX gene mutation: six patients and new mutations
**Identifier:** PMID 34034642 / DOI 10.1080/01616412.2021.1932173
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-167
**Corpus paper no:** 167
**Full title:** High and Low WWOX Gene Expression Levels in Acute Myeloid Leukemia
**Identifier:** PMID 31532107 / DOI 10.7754/Clin.Lab.2019.190119
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-168
**Corpus paper no:** 168
**Full title:** Conditional Wwox deletion in mouse mammary gland by means of two Cre recombinase approaches
**Identifier:** PMID 22574198 / DOI 10.1371/journal.pone.0036618
**Status:** promoted — see [[paper_registry_current#PAPER 107]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-169
**Corpus paper no:** 169
**Full title:** A role for the WWOX gene in prostate cancer
**Identifier:** PMID 16818616 / DOI 10.1158/0008-5472.CAN-06-0956
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-170
**Corpus paper no:** 170
**Full title:** Loss of WWOX expression in gastric carcinoma
**Identifier:** PMID 15131042 / DOI 10.1158/1078-0432.ccr-03-0594
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-171
**Corpus paper no:** 171
**Full title:** WWOX gene may contribute to progression of non-small-cell lung cancer (NSCLC)
**Identifier:** PMID 20480411 / DOI 10.1007/s13277-010-0039-3
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-172
**Corpus paper no:** 172
**Full title:** Characterization of WWOX inactivation in murine mammary gland development
**Identifier:** PMID 23254778 / DOI 10.1002/jcp.24310
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-173
**Corpus paper no:** 173
**Full title:** Fhit and Wwox loss-associated genome instability: A genome caretaker one-two punch
**Identifier:** PMID 27773744 / DOI 10.1016/j.jbior.2016.09.008
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-174
**Corpus paper no:** 174
**Full title:** Ectopic WWOX Expression Inhibits Growth of 5637 Bladder Cancer Cell In Vitro and In Vivo
**Identifier:** PMID 27352332 / DOI 10.1007/s12013-015-0654-0
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-175
**Status:** resolved — see [[paper_registry_current#PAPER 093]] (BATCH_20260920_002, `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`)
**Registry role:** corpus placeholder only — conservato append-only come storia di audit, mai cancellato
**Next action:** none — risolto
**Corpus paper no:** 175
**Full title:** WWOX-related epileptic encephalopathy caused by a novel mutation in the WWOX gene: a case report
**Identifier:** PMID 39416860 / DOI 10.3389/fped.2024.1453778

**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-176
**Corpus paper no:** 176
**Full title:** WWOX suppresses KLF5 expression and breast cancer cell growth
**Identifier:** PMID 25400415 / DOI 10.3978/j.issn.1000-9604.2014.09.03
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-177
**Corpus paper no:** 177
**Full title:** EBV-LMP1 regulating AKT/mTOR signaling pathway and WWOX in nasopharyngeal carcinoma
**Identifier:** PMID 31966718
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-178
**Corpus paper no:** 178
**Full title:** B-cell-specific Wwox deletion promotes plasmablastic tumor development and proinflammatory signature
**Identifier:** PMID 41090157 / DOI 10.1016/j.bneo.2025.100153
**Status:** promoted — see [[paper_registry_current#PAPER 115]] (`BATCH_20260926_ALDAZ_R1`)
**Registry role:** corpus placeholder only — kept append-only as audit history, never deleted
**Claim links:** none
**Next action:** none — resolved by promotion
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.



## CORPUS-STUB-179
**Corpus paper no:** 179
**Full title:** p73 participates in WWOX-mediated apoptosis in leukemia cells
**Identifier:** PMID 23446842 / DOI 10.3892/ijmm.2013.1289
**Status:** not_processed
**Integrity status:** 🔴 `PUBLICATION_INTEGRITY_HOLD` — **retracted**. Field added in `BATCH_20260806_002`, closing a debt declared on 2026-08-06. **No canonical claim rests on this record.** Its only entanglement was a receipt-to-PAPER identity mismatch: the legacy receipt `FTR-20260726-23446842-01` was quarantined append-only by `FTR-20260806-23446842-02`, and active depth and generated coverage no longer attribute it to this PMID. Not admissible as evidentiary support in any form.
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

---

## CORPUS-STUB-180
**Corpus paper no:** 180
**Full title:** Patient-derived tissue cultures complement neurospheres for preclinical evaluation of AAV-mediated gene delivery in glioblastoma
**Authors:** Köhler F, Hess K, Koloske C, Gaunitz F, Rosahl SK, Gerlach R, Kallendrusch S
**Year:** 2026
**Journal/source:** *Journal of Neuro-Oncology* 2026;179(3):93
**Identifier:** PMID 42771216 / PMCID PMC13597561 / DOI 10.1007/s11060-026-05807-w
**Status:** processed
**Record provenance:** created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9 2026-10-04, Scientist C); identity authored from the artefact's JATS front matter at `a405efc30550`. The candidate's provisional `CORPUS-STUB-180` was re-measured and holds (`CORPUS-STUB` max was 179); its provisional `LIT-0509` was already taken and became `LIT-0536`.
**Registry role:** 🔴 **an EARNED NULL, not an unscreened placeholder.** The paper was read in full-text part for one transferable-method question and **WWOX occurs zero times in it**. A stub is the honest landing: there is no WWOX content to record in a PAPER record, and the reading is nevertheless real and receipted.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42771216-01`; manifest `deepdive_manifests/PMID42771216.json`; dossier `research/fulltext_dossiers/PMID42771216.md`
**Claim links:** none
**Next action:** none — read, measured null, and registered. No re-read is owed unless a question about AAV delivery substrates in patient-derived tissue is asked of it.
**LIT link:** [[literature_tracking_log_current#LIT-0536]]
**Note:** class-level record. Not medical advice.

---
## Corpus Range 181–220 — Consolidated Classification (Commit 2026-04-17)

> Questo blocco è un riepilogo di triage per i paper 181–220.
> Non contiene schede complete. Le schede individuali saranno aggiunte paper-by-paper in sessioni future.
> La classificazione si basa su deep-dive escalation dei paper più model-shifting e triage avanzato per i rimanenti.

### High-value mechanistic / model-shifting
- **182** — WWOX interactome / trafficking–metabolism coupling (endomembrane → Acetyl-CoA) → CLAIM 026 — source normalized 2026-07-05 to [[paper_registry_current#PAPER 032]]
- **191** — WWOX/HIF1A axis in human non-tumoral GDM leukocytes → CLAIM 025
- **204** — WW1–WW2 tandem cooperativity / domain architecture → CLAIM 024
- **206** — WWOX–p73 routing/scaffold biology / Tyr33 phosphorylation → CLAIM 023
- **210** — Neocortical hyperexcitability / oscillatory pathology / NMDAR + gap junction dependence → CLAIM 021 — source normalized 2026-07-05 to [[paper_registry_current#PAPER 031]]
- **214** — HYAL-2 / WWOX / SMAD4 ECM-to-nucleus signaling → CLAIM 027
- **216** — First prenatal severe null human case (homozygous deletion exons 1–6) → CLAIM 022

### Human spectrum refinement / strong support
- **181** — human spectrum support
- **195** — human spectrum support
- **196** — human spectrum support

### Strong support / secondary refinement
- **183** — supporto secondario
- **188** — supporto secondario
- **189** — supporto secondario
- **194** — supporto secondario
- **199** — supporto secondario
- **200** — supporto secondario
- **207** — deep, high-confidence, partial-access translational analysis → linked CLAIM 028 (context-dependence)
- ~~**213** — context/partner-dependence mechanistic support → CLAIM 028~~ — withdrawn by `BATCH_20260725_001`: duplicate source-number typo for CORPUS P207; no P213 record exists
- **218** — context/partner-dependence mechanistic support (quantitative phospho-state / p73 binding) → CLAIM 028
- **219** — supporto secondario

### New propagation beyond initial 181–220 core
- **138** — ATM / DDR competence / genome-stability axis → CLAIM 029 / RC-012

### Lower-impact support papers
- 185, 190, 193, 197, 201, 202, 203, 205, 208, 209, 211, 215, 217, 220

### Non-substantive update
- **198** — corrigendum / nessun impatto operativo

### Processing notes
- Deep-dive / high-confidence: 182, 191, 204, 206, 207, 210, 214, 216
- Advanced triage only: tutti i restanti paper in questo range
- Schede complete da aggiungere in sessioni future, paper-by-paper, secondo priorità


---

# FASE 1 TRIAGE CORPUS — PAPERS 221–400

**Date:** 2026-04-18
**Total corpus placeholders added:** 179 (CORPUS P221..P400 minus P264)

## Purpose

This section holds **corpus-level placeholders** for papers screened in FASE 1 triage 221–400.
These are **not** PAPER 0NN structural entries. PAPER 0NN numbering is reserved for papers
that have completed deep-dive integration and have propagated at least one claim, working
model element, or research line.

Corpus placeholders preserve discovery, triage tier, and preliminary pathway routing without
forcing premature elevation to structural status.

## Tier A corpus entries (7)

Papers marked tier A are priority full-text retrieval targets. Upon successful retrieval and
deep-dive, they may be promoted to PAPER 029+ structural entries via the standard commit
pipeline (RULE 2 consistency check + RULE 4 change log).

## Tier B corpus entries (16)

Tier B entries are secondary full-text targets; promotion to PAPER 0NN is conditional on
deep-dive yielding model-shifting content.

## Tier C corpus entries (156)

Tier C entries remain background-only unless convergence signals across meta-axes trigger
re-evaluation.

## Dedup

CORPUS P264 is **not created** — paper PMID 39101447 is already integrated as PAPER 016
(You 2024) from SESSION_COMMIT_LOG 181–220.

---

## CORPUS P221
**Short title:** WWOX tumour suppressor gene polymorphisms and ovarian cancer pathology and pr...
**Full title:** WWOX tumour suppressor gene polymorphisms and ovarian cancer pathology and prognosis
**Authors:** Paige et al.
**Year:** 2010
**Source type:** Multicenter Study
**Journal/source:** Eur J Cancer
**Identifier:** PMID 20074932 / DOI 10.1016/j.ejca.2009.12.021
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0221
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P222
**Short title:** The WWOX tumor suppressor is essential for postnatal survival and normal bone...
**Full title:** The WWOX tumor suppressor is essential for postnatal survival and normal bone metabolism
**Authors:** Aqeilan et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 18487609 / PMC2490770 / DOI 10.1074/jbc.M800855200
**Tier (FASE 1):** B
**Status:** read — corpus placeholder, not promoted (`CC-20260914-PLACEHOLDER-READS-01`, `BATCH_20260926_ALDAZ_R2`); see `Evidence depth`
**Evidence depth:** complete_fulltext_read — `FTR-20260811-18487609-01`; manifest `deepdive_manifests/PMID18487609.json` (23 locators, schema v2, strict PASS, 0 gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**LIT link:** LIT-0222
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P223
**Short title:** Correlation of WWOX, RUNX2 and VEGFA protein expression in human osteosarcoma
**Full title:** Correlation of WWOX, RUNX2 and VEGFA protein expression in human osteosarcoma
**Authors:** Yang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** BMC Med Genomics
**Identifier:** PMID 24330824 / PMC3878685 / DOI 10.1186/1755-8794-6-56
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0223
**Primary pathway:** P8 — bone / RUNX2 axis
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P224
**Short title:** Deletion of the WWOX gene and frequent loss of its protein expression in huma...
**Full title:** Deletion of the WWOX gene and frequent loss of its protein expression in human osteosarcoma
**Authors:** Yang et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Cancer Lett
**Identifier:** PMID 19896763 / DOI 10.1016/j.canlet.2009.09.018
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0224
**Primary pathway:** P8 — bone / RUNX2 axis
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P225
**Short title:** Identification of a novel splice-site WWOX variant with paternal uniparental...
**Full title:** Identification of a novel splice-site WWOX variant with paternal uniparental isodisomy in a patient with infantile epileptic encephalopathy
**Authors:** Nishino et al.
**Year:** 2024
**Source type:** Case Reports
**Journal/source:** Am J Med Genet A
**Identifier:** PMID 38407561 / DOI 10.1002/ajmg.a.63575
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0225
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P226
**Short title:** A WWOX-binding molecule, transmembrane protein 207, is related to the invasiv...
**Full title:** A WWOX-binding molecule, transmembrane protein 207, is related to the invasiveness of gastric signet-ring cell carcinoma
**Authors:** Takeuchi et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Carcinogenesis
**Identifier:** PMID 22226915 / DOI 10.1093/carcin/bgs001
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0226
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P227
**Short title:** Hypermethylation-mediated reduction of WWOX expression in intraductal papilla...
**Full title:** Hypermethylation-mediated reduction of WWOX expression in intraductal papillary mucinous neoplasms of the pancreas
**Authors:** Nakayama et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Br J Cancer
**Identifier:** PMID 19352382 / PMC2694421 / DOI 10.1038/sj.bjc.6604986
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0227
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P228
**Short title:** Expression of ORAOV1, CD133 and WWOX correlate with metastasis and prognosis...
**Full title:** Expression of ORAOV1, CD133 and WWOX correlate with metastasis and prognosis in gastric adenocarcinoma
**Authors:** Lu et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Int J Clin Exp Pathol
**Identifier:** PMID 31966760 / PMC6965444
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0228
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P229
**Short title:** Role of WW Domain-containing Oxidoreductase WWOX in Driving T Cell Acute Lymp...
**Full title:** Role of WW Domain-containing Oxidoreductase WWOX in Driving T Cell Acute Lymphoblastic Leukemia Maturation
**Authors:** Huang et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 27339895 / PMC5016130 / DOI 10.1074/jbc.M116.716167
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0229
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P230
**Short title:** Molecular alterations of the WWOX gene in nasopharyngeal carcinoma
**Full title:** Molecular alterations of the WWOX gene in nasopharyngeal carcinoma
**Authors:** Yang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Neoplasma
**Identifier:** PMID 24299313 / DOI 10.4149/neo_2014_023
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0230
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P231
**Short title:** TMEM207 hinders the tumour suppressor function of WWOX in oral squamous cell...
**Full title:** TMEM207 hinders the tumour suppressor function of WWOX in oral squamous cell carcinoma
**Authors:** Bunai et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** J Cell Mol Med
**Identifier:** PMID 29164763 / PMC5783854 / DOI 10.1111/jcmm.13456
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0231
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P232
**Short title:** Molecular analysis of WWOX expression correlation with proliferation and apop...
**Full title:** Molecular analysis of WWOX expression correlation with proliferation and apoptosis in glioblastoma multiforme
**Authors:** Kosla et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** J Neurooncol
**Identifier:** PMID 20535528 / PMC2996532 / DOI 10.1007/s11060-010-0254-1
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0232
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P233
**Short title:** Wwox expression may predict benefit from adjuvant tamoxifen in randomized bre...
**Full title:** Wwox expression may predict benefit from adjuvant tamoxifen in randomized breast cancer patients
**Authors:** Eremo et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Oncol Rep
**Identifier:** PMID 23381945 / DOI 10.3892/or.2013.2261
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0233
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P234
**Short title:** Angiomotin Counteracts the Negative Regulatory Effect of Host WWOX on Viral P...
**Full title:** Angiomotin Counteracts the Negative Regulatory Effect of Host WWOX on Viral PPxY-Mediated Egress
**Authors:** Liang et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** J Virol
**Identifier:** PMID 33536174 / PMC8103691 / DOI 10.1128/JVI.00121-21
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0234
**Primary pathway:** animal model — pathway variable
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P235
**Short title:** Exosomal miR-625-3p secreted by cancer-associated fibroblasts in colorectal c...
**Full title:** Exosomal miR-625-3p secreted by cancer-associated fibroblasts in colorectal cancer promotes EMT and chemotherapeutic resistance by blocking the CELF2/WWOX pathway
**Authors:** Zhang et al.
**Year:** 2022
**Source type:** Article
**Journal/source:** Pharmacol Res
**Identifier:** PMID 36336217 / DOI 10.1016/j.phrs.2022.106534
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0235
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P236
**Short title:** WWOX CNV-67048 Functions as a Risk Factor for Epithelial Ovarian Cancer in Ch...
**Full title:** WWOX CNV-67048 Functions as a Risk Factor for Epithelial Ovarian Cancer in Chinese Women by Negatively Interacting with Oral Contraceptive Use
**Authors:** Chen et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Biomed Res Int
**Identifier:** PMID 27190995 / PMC4842385 / DOI 10.1155/2016/6594039
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0236
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P237
**Short title:** Ectopic expression of the WWOX gene suppresses stemness of human ovarian canc...
**Full title:** Ectopic expression of the WWOX gene suppresses stemness of human ovarian cancer stem cells
**Authors:** Yan et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 25789010 / PMC4356412 / DOI 10.3892/ol.2015.2971
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0237
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P238
**Short title:** Diverse effect of WWOX overexpression in HT29 and SW480 colon cancer cell lines
**Full title:** Diverse effect of WWOX overexpression in HT29 and SW480 colon cancer cell lines
**Authors:** Nowakowska et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Tumour Biol
**Identifier:** PMID 24938873 / PMC4190457 / DOI 10.1007/s13277-014-2196-2
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0238
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P239
**Short title:** Strategies by which WWOX-deficient metastatic cancer cells utilize to survive...
**Full title:** Strategies by which WWOX-deficient metastatic cancer cells utilize to survive via dodging, compromising, and causing damage to WWOX-positive normal microenvironment
**Authors:** # et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Cell Death Discov
**Identifier:** PMID 31123603 / PMC6529460 / DOI 10.1038/s41420-019-0176-4
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0239
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P240
**Short title:** An opposing view on WWOX protein function as a tumor suppressor
**Full title:** An opposing view on WWOX protein function as a tumor suppressor
**Authors:** Watanabe et al.
**Year:** 2003
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 14695174
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0240
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P241
**Short title:** The correlation of the expressions of WWOX, LGR5 and vasohibin-1 in epithelia...
**Full title:** The correlation of the expressions of WWOX, LGR5 and vasohibin-1 in epithelial ovarian cancer and their clinical significance
**Authors:** Yu et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Int J Clin Exp Pathol
**Identifier:** PMID 31933749 / PMC6944017
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0241
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P242
**Short title:** Conditional inactivation of the mouse Wwox tumor suppressor gene recapitulate...
**Full title:** Conditional inactivation of the mouse Wwox tumor suppressor gene recapitulates the null phenotype
**Authors:** Abdeen et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** J Cell Physiol
**Identifier:** PMID 23254685 / PMC3943428 / DOI 10.1002/jcp.24308
**Tier (FASE 1):** B
**Status:** promoted — see [[paper_registry_current#PAPER 075]] (`BATCH_20260815_001`)
**LIT link:** LIT-0242
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P243
**Short title:** Gene expression of WWOX, FHIT and p73 in acute lymphoblastic leukemia
**Full title:** Gene expression of WWOX, FHIT and p73 in acute lymphoblastic leukemia
**Authors:** Chen et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 24137446 / PMC3796419 / DOI 10.3892/ol.2013.1514
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0243
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P244
**Short title:** Park 2004 — WWOX in 18 linee di HCC: mRNA e proteina ridotti, due trascritti aberranti, quattro varianti codificanti
**Full title:** Frequent downregulation and loss of WWOX gene expression in human hepatocellular carcinoma
**Authors:** Park SW, Ludes-Meyers J, Zimonjic DB, Durkin ME, Popescu NC, Aldaz CM (6 authors, artefact `contrib-group`, confirmed by esummary)
**Year:** 2004
**Source type:** primary research — descriptive expression survey in established human cell lines + tissue IHC
**Journal/source:** *Br J Cancer* 2004;91(4):753-759
**Identifier:** PMID 15266310 / PMC2364795 / DOI 10.1038/sj.bjc.6602023
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-15266310-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID15266310.json`, dossier `fulltext_dossiers/PMID15266310.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260926_ALDAZ_R2` (`CC-20260914-15266310-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0244
**Primary pathway:** oncology / tumor suppressor biology — 🔴 **corrected from `P6 — DDR / genome stability`**, assigned in FASE 1 triage without a reading: the paper contains no DDR assay and no genome-stability endpoint
**Model/species:** linee cellulari umane di HCC (18), fegato adulto umano normale, 5 sezioni di HCC. **Nessun animale, nessun allele germinale, nessun materiale neurale**
**Genotype/model:** WWOX wild-type e somatico; nessun allele WWOX-DEE
**Transferability:** **T3**
**clinical relevance:** **LOW** (unchanged)
**Claim links:** none — the reading proposes none
**Role:** background corpus, **letto**: la fonte della serie HCC del gruppo Aldaz. Il suo valore per questo repository non è oncologico ma **di sequenza e di reagente**: due linee HCC portano giunzioni in frame esone 5→9 (Δ6–8), una con un **inserto di 96 bp** derivato dall'introne 8, confermate per sequenziamento (DATO in due linee tumorali; ogni trasferimento ad alleli di splicing WWOX-DEE è `ESPANSIONE`; il prodotto previsto di ~30 kDa è INFERENZA degli autori, **mai mostrato**); quattro varianti codificanti (P252A, D183N, A179T, R314H) chiamate *"very likely"* polimorfismi **senza saggio funzionale, frequenza di popolazione, DNA normale appaiato né mappa di dominio** (PREMISE `DEFAULT_FROM_TEXTBOOK`); e l'antisiero del gruppo stampato come **`140 μg/ml`** su una superficie JATS della versione di record
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. *(2026-09-26: no longer true for reading depth — this paper has since been read in full; see `Evidence depth`. Triage status unchanged.)*
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-15266310-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Reading note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** Nessun test statistico compare nel lavoro; la densitometria dei Western è l'unica quantificazione. Difetti misurati in questa lettura, non dichiarati dagli autori: la Figura 2 **contraddice il testo su due corsie** (SNU423 ha una banda Northern forte; SNU475 non ne ha alcuna); la Figura 4 mostra **17 linee, non 18** (Chang assente), e la frase *"72% (13 out of 18)"* conta le 13 barre **sotto 0.10**, cioè *"oltre il 90% in meno"*, su un denominatore di 17; **nessuna corsia di riferimento Peo/WWOX è mostrata** e il blot di destra non ha corsia di fegato normale, quindi sei valori di Fig. 4B sono standardizzati attraverso una corsia che nessuno può vedere; banda citogenetica **16q24** nei Results contro **16q23** in legenda e abstract; l'inserto è dato a **96 bp** ma le coordinate 5281331–5281425 ne coprono **95**; *"Five cell lines"* seguito da sei nomi; percentuali 60/61 (mRNA) e 72/75 (proteina) contro 13/17 = 76.5%. Tre negativi poggiano su dati **non mostrati** (Southern; 5-aza-dC + TSA; IHC definita *preliminary*). Dependency screen `SCREENED_CLEAN` (28 of 38). Kept as a CORPUS record: the candidate proposed promotion; this batch completes the record in place. *(The triage `Note` and the R1 `Registration note` above are superseded for every field this batch writes; their text is kept as history.)*

## CORPUS P245
**Short title:** WWOX, a novel WW domain-containing protein mapping to human chromosome 16q23....
**Full title:** WWOX, a novel WW domain-containing protein mapping to human chromosome 16q23.3-24.1, a region frequently affected in breast cancer
**Authors:** Bednarek et al.
**Year:** 2000
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 10786676
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0245
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P246
**Short title:** The role of WWOX tumor suppressor gene in the regulation of EMT process via r...
**Full title:** The role of WWOX tumor suppressor gene in the regulation of EMT process via regulation of CDH1-ZEB1-VIM expression in endometrial cancer
**Authors:** Płuciennik et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 25892250 / DOI 10.3892/ijo.2015.2964
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0246
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P247
**Short title:** WWOX suppresses cell growth and induces cell apoptosis via inhibition of P38...
**Full title:** WWOX suppresses cell growth and induces cell apoptosis via inhibition of P38 nuclear translocation in cholangiocarcinoma
**Authors:** Wang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Cell Physiol Biochem
**Identifier:** PMID 25502636 / DOI 10.1159/000366372
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0247
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P248
**Short title:** Inhibition of the Wnt/beta-catenin pathway by the WWOX tumor suppressor protein
**Full title:** Inhibition of the Wnt/beta-catenin pathway by the WWOX tumor suppressor protein
**Authors:** Bouteille et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Oncogene
**Identifier:** PMID 19465938 / DOI 10.1038/onc.2009.120
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0248
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P249
**Short title:** Impact of WWOX alterations on p73, ΔNp73, p53, cell proliferation and DNA plo...
**Full title:** Impact of WWOX alterations on p73, ΔNp73, p53, cell proliferation and DNA ploidy in salivary gland neoplasms
**Authors:** Gomes et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Oral Dis
**Identifier:** PMID 21332605 / DOI 10.1111/j.1601-0825.2011.01802.x
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0249
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P250
**Short title:** [Effects of WWOX on ovarian cancer cell attachment in vitro]
**Full title:** [Effects of WWOX on ovarian cancer cell attachment in vitro]
**Authors:** [Article in Chinese]
**Year:** 2009
**Source type:** Article
**Journal/source:** Zhonghua Zhong Liu Za Zhi
**Identifier:** PMID 19950548
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0250
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P251
**Short title:** Genetic alterations of the WWOX gene in breast cancer
**Full title:** Genetic alterations of the WWOX gene in breast cancer
**Authors:** Ekizoglu et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Med Oncol
**Identifier:** PMID 21983861 / DOI 10.1007/s12032-011-0080-0
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0251
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P252
**Short title:** Expression of WW domain-containing oxidoreductase WWOX in pterygium
**Full title:** Expression of WW domain-containing oxidoreductase WWOX in pterygium
**Authors:** Huang et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Mol Vis
**Identifier:** PMID 26120275 / PMC4480446
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0252
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P253
**Short title:** Novel Homozygous Mutation in the WWOX Gene Causes Seizures and Global Develop...
**Full title:** Novel Homozygous Mutation in the WWOX Gene Causes Seizures and Global Developmental Delay: Report and Review
**Authors:** Ehaideb et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Transl Neurosci
**Identifier:** PMID 30746283 / PMC6368664 / DOI 10.1515/tnsci-2018-0029
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0253
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. **Promoted 2026-10-02 to [[paper_registry_current#PAPER 119]] by `CC-20261002-INTAKE-A-REGISTRY-01` (first-hand full-text read `FTR-20261002-30746283-01`); this placeholder is kept as history.**

## CORPUS P254
**Short title:** New syngeneic inflammatory-related lung cancer metastatic model harboring dou...
**Full title:** New syngeneic inflammatory-related lung cancer metastatic model harboring double KRAS/WWOX alterations
**Authors:** Bleau et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 24473991 / DOI 10.1002/ijc.28574
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0254
**Primary pathway:** P8 — bone / RUNX2 axis
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P255
**Short title:** Exogenous WWOX enhances apoptosis and weakens metastasis in CNE2 nasopharynge...
**Full title:** Exogenous WWOX enhances apoptosis and weakens metastasis in CNE2 nasopharyngeal carcinoma cells through the intrinsic apoptotic pathway
**Authors:** Chen et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Int J Clin Exp Pathol
**Identifier:** PMID 31966369 / PMC6965803
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0255
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P256
**Short title:** Circular RNA CircMTO1 Inhibits Proliferation of Glioblastoma Cells via miR-92...
**Full title:** Circular RNA CircMTO1 Inhibits Proliferation of Glioblastoma Cells via miR-92/WWOX Signaling Pathway
**Authors:** Zhang et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Med Sci Monit
**Identifier:** PMID 31456594 / PMC6738003 / DOI 10.12659/MSM.918676
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0256
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P257
**Short title:** Tyrosine phosphorylation of WW proteins
**Full title:** Tyrosine phosphorylation of WW proteins
**Authors:** Reuven et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25627656 / PMC4935225 / DOI 10.1177/1535370214565991
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0257
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P258
**Short title:** LncRNA HOTAIRM1 Inhibits the Proliferation and Invasion of Lung Adenocarcinom...
**Full title:** LncRNA HOTAIRM1 Inhibits the Proliferation and Invasion of Lung Adenocarcinoma Cells via the miR-498/WWOX Axis [Retraction]
**Authors:** No authors listed
**Year:** 2024
**Source type:** Article
**Journal/source:** Cancer Manag Res
**Identifier:** PMID 38282791 / PMC10812133 / DOI 10.2147/CMAR.S460239
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0258
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P259
**Short title:** miR-187* Enhances SiHa Cervical Cancer Cell Oncogenicity Via Suppression of WWOX
**Full title:** miR-187* Enhances SiHa Cervical Cancer Cell Oncogenicity Via Suppression of WWOX
**Authors:** Hung et al.
**Year:** 2020
**Source type:** Article
**Journal/source:** Anticancer Res
**Identifier:** PMID 32132039 / DOI 10.21873/anticanres.14084
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0259
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P260
**Short title:** Molecular alterations in the tumor suppressor gene WWOX in oral leukoplakias
**Full title:** Molecular alterations in the tumor suppressor gene WWOX in oral leukoplakias
**Authors:** Pimenta FJ, Cordeiro GT, Pimenta LG, Viana MB, Lopes J, Gomez MV, Aldaz CM, De Marco L, Gomez RS (9 authors, esummary). 🔴 **Two authors share the surname `Pimenta`** (`Pimenta FJ`, first; `Pimenta LG`, third): an `et al.` key cannot distinguish them
**Year:** 2008
**Source type:** Article
**Journal/source:** Oral Oncol
**Identifier:** PMID 18061530 / PMC4143237 / DOI 10.1016/j.oraloncology.2007.08.019
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-18061530-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID18061530.json`, dossier `fulltext_dossiers/PMID18061530.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260926_ALDAZ_R2` (`CC-20260914-18061530-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0260
**Primary pathway:** oncology / tumor suppressor biology — lesione premaligna, trascritti aberranti ed espressione proteica. 🔴 **Corrected from `P6 — DDR / genome stability`**: no DNA-damage, repair or genome-stability assay exists in this paper
**Model/species:** tessuto umano adulto: **23 leucoplachie orali consecutive** (una clinica, mar 2005 - giu 2006; 14 M / 9 F, 29-67 anni, 19 fumatori) + mucosa normale da volontari appaiati **in numero non dichiarato**. Nessuna linea cellulare, nessun animale, nessun allele germinale, nessuna analisi di DNA genomico, **nessun materiale neurale**
**Genotype/model:** WWOX somatico; nessun allele WWOX-DEE
**Transferability:** **T3**
**clinical relevance:** **LOW** — unchanged
**Claim links:** none — the reading proposes none
**Role:** Serie trasversale: trascritti WWOX alterati o assenti in **6/23** lesioni, proteina ridotta all'IHC in **6/23**, alterazione combinata in **8/23 (35%)**; alterazioni in 5/11 displasie moderate-severe, 3/8 lievi, **0/4 senza displasia** — gradiente **non significativo** ricalcolato (p=0.26; p=0.40), e il paper non riporta alcun test. Un prodotto Δ6-8 pulito coesiste con un secondo trascritto aberrante in una lesione benigna (#OL23)
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. *(2026-09-26: no longer true for reading depth — this paper has since been read in full; see `Evidence depth`. Triage status unchanged.)*
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-18061530-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Reading note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** Manoscritto d'autore (Europe PMC `fullTextXML` 404; efetch rifiuta l'XML; ptpmcrender 403; **la pagina PMC ha servito un interstiziale reCAPTCHA sotto HTTP 200 per tre richieste** e l'articolo solo dopo 75 s di attesa). **Limiti misurati in questa lettura:** 🔴 **la scala IHC è cambiata rispetto al paper OSCC del 2006 dello stesso gruppo con lo stesso antisiero e protocollo** (`CORPUS P367`: qui +1 0-50%, +2 51-75%, +3 >76%; nel 2006 +1 0-10%, +2 11-50%, +3 >50%), per cui un "+2" nei due lavori non è la stessa grandezza — e la Discussione confronta il 35% di qui con il 50% di allora; la scala lascia indefinito 75-76%; **il numero dei controlli non compare da nessuna parte**; #OL16 è contato come alterato senza sequenza; **quattro dei cinque prodotti sequenziati uniscono interni di esone** (giunzioni non canoniche) dopo **due round nidificati da 35 cicli** su materiale microdissezionato, e nessun artefatto di template-switching è escluso — una giunzione a metà esone amplificata così non è di per sé evidenza di un trascritto in vivo (INFERENZA del lettore); IHC e RT-PCR eseguite **su aree diverse** della lesione; la legenda di Fig. 2a dice *"(strong)"* dove i pixel mostrano marcatura bruna tenue; la frase di sintesi scrive *"expression"* dove intende *"alteration"*. Il Δ6-8 in una lesione benigna è un segnale di fondo, **non** un delta a `CLAIM 018` o `CLAIM 033`. Specificità dell'antisiero delegata al rif. 30 = PMID 14526170 (`PAPER 101`). *(The triage `Note` and the R1 `Registration note` above are superseded for every field this batch writes; their text is kept as history.)*

## CORPUS P261
**Short title:** Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenes...
**Full title:** Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenesis of osteosarcoma
**Authors:** Del Mare S, Kurek KC, Stein GS, Lian JB, Aqeilan RI — corrected in `BATCH_20260909_001` from the triage value *"Mare et al."*
**Year:** 2011
**Source type:** 🔴 **Review** — corrected in `BATCH_20260909_001` from `Article`. **This field is load-bearing and must not be softened back:** under `epistemic_discipline` a review is a secondary source and cannot be primary evidence for a claim, so every number in it is a pointer to its cited primary, never a measurement.
**Journal/source:** Am J Cancer Res 2011;1(5):585–594
**Identifier:** PMID 21731849 / PMC3124638 / **no DOI assigned by the publisher**
**Tier (FASE 1):** C
**Status:** read — corpus placeholder, **deliberately not promoted to a PAPER record** (`CC-20260909-21731849-01`, §1)
**Evidence depth:** complete_fulltext_read — `FTR-20260909-21731849-01`; manifest `deepdive_manifests/PMID21731849.json` (18 locators, schema v2, strict PASS, 0 gaps)
**LIT link:** LIT-0261
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** human + mouse (secondary)
**Genotype/model:** no WWOX-DEE allele; bone/osteosarcoma biology
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none — the reading adds two qualification notes to [[claim_registry_current#CLAIM 036]] and creates no link
**Role:** secondary source; **citation-fidelity reference point** for the osteosarcoma line
**Note:** Read in full 2026-09-09 (`CC-20260909-21731849-01`). Acquisition recorded because it constrains re-verification: Europe PMC `fullTextXML` 404; NCBI `efetch db=pmc PMC3124638` returns front matter and abstract with no `<body>`, `<sec>`, `<fig>` or `<ref>`; obtained via `pdf=render`, text by `pdftotext -nopgbrk` without `-layout`. Declared extraction limit: hyphens joined (`Wwoxdeficient`, `paraffinembedded`).

## CORPUS P262
**Short title:** Expression of WWOX and FHIT is downregulated by exposure to arsenite in human...
**Full title:** Expression of WWOX and FHIT is downregulated by exposure to arsenite in human uroepithelial cells
**Authors:** Huang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Toxicol Lett
**Identifier:** PMID 23618899 / DOI 10.1016/j.toxlet.2013.04.007
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0262
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** rat
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P263
**Short title:** WW domain-containing oxidoreductase in neuronal injury and neurological diseases
**Full title:** WW domain-containing oxidoreductase in neuronal injury and neurological diseases
**Authors:** Chang et al.
**Year:** 2014
**Source type:** Review
**Journal/source:** Oncotarget
**Identifier:** PMID 25537520 / PMC4322972 / DOI 10.18632/oncotarget.2961
**Tier (FASE 1):** B
**Status:** read — partial full text (FTR-20261002-25537520-01; figures captions only) — no claim promoted
**LIT link:** LIT-0263
**Primary pathway:** review — neuronal injury, tau/GSK-3β, TGF-β/TIAF1, neurodevelopment (triage value "P6 — DDR / genome stability" corrected 2026-10-02 by CC-20261002-B-NONLINEAGE-01)
**Model/species:** review — secondary source, no primary data (triage value "rat" corrected 2026-10-02 by CC-20261002-B-NONLINEAGE-01)
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400. Read 2026-10-02 (dossier fulltext_dossiers/PMID25537520.md): a provenance map, not evidence. Its epilepsy and developmental sentences rest on PMID 24369382, PMID 24456803 and PMID 19500159, each held from the primary; its tau-inhibitor, TIAF1 (cited as "unpublished") and in-vivo transcription-factor statements are the authors' own laboratory, and its Conclusion asserts in-vivo transcription-factor control that its own body says "remains to be established". Do not cite its sentences as independent support. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P265
**Short title:** MiR-214 Mediates Cell Proliferation and Apoptosis of Nasopharyngeal Carcinoma...
**Full title:** MiR-214 Mediates Cell Proliferation and Apoptosis of Nasopharyngeal Carcinoma Through Targeting Both WWOX and PTEN
**Authors:** Han et al.
**Year:** 2020
**Source type:** Article
**Journal/source:** Cancer Biother Radiopharm
**Identifier:** PMID 32101017 / PMC7578184 / DOI 10.1089/cbr.2019.2978
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0265
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P266
**Short title:** Decreased expression of WWOX in the development of esophageal squamous cell c...
**Full title:** Decreased expression of WWOX in the development of esophageal squamous cell carcinoma
**Authors:** Guo et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Mol Carcinog
**Identifier:** PMID 22213016 / DOI 10.1002/mc.21853
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0266
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P267
**Short title:** Germline mutation and aberrant transcripts of WWOX in a syndrome with multipl...
**Full title:** Germline mutation and aberrant transcripts of WWOX in a syndrome with multiple primary tumors
**Authors:** Xu et al.
**Year:** 2019
**Source type:** Case Reports
**Journal/source:** J Pathol
**Identifier:** PMID 31056747 / DOI 10.1002/path.5288
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0267
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P268
**Short title:** Frequent attenuation of the WWOX tumor suppressor in osteosarcoma is associat...
**Full title:** Frequent attenuation of the WWOX tumor suppressor in osteosarcoma is associated with increased tumorigenicity and aberrant RUNX2 expression
**Authors:** Kurek et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 20530675 / PMC3037996 / DOI 10.1158/0008-5472.CAN-09-4602
**Tier (FASE 1):** C
**Status:** read — corpus placeholder, **deliberately not promoted to a PAPER record** (`CC-20260909-20530675-01`, §1)
**Evidence depth:** complete_fulltext_read — `FTR-20260909-20530675-01` (prior `FTR-20260814-20530675-01`, `inadequate_prior_coverage`); manifest `deepdive_manifests/PMID20530675.json` (31 locators, schema v2, strict PASS, 0 gaps)
**LIT link:** LIT-0268
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** mouse (Wwox-null) + human osteosarcoma
**Genotype/model:** no WWOX-DEE allele, no neural endpoint, no CNS measurement anywhere in the paper
**Transferability:** T3 — `ESPANSIONE`
**clinical relevance:** LOW
**Claim links:** none — the reading adds one qualification to [[claim_registry_current#CLAIM 036]] and creates no link
**Role:** background corpus only; source of the osteosarcoma-penetrance number the downstream literature quotes
**Note:** 🔴 **The prior note — *"FASE 1 triage 221–400 — no deep-dive performed"* — was false as of 2026-09-09 and is superseded.** The paper was read in full. It is the source of the strongest pro-osteosarcoma number in this literature (*"100% of Wwox-deficient mice had developed OS by 18 days-of-age"*), and **its own Figure S1 legend reports 19 of 22 knockout mice with tumours (86%)**. See [[claim_registry_current#CLAIM 036]] for the arithmetic and the screening-criterion caveat. Receipt-ledger defect recorded and **not** silently repaired: the prior receipt `FTR-20260814-20530675-01` carries the wrong `study_id.doi`, and `receipt_correction` cannot lawfully change study identity, so `FTR-20260909-20530675-01` **omits `doi` from `study_id`** and carries the correct value in `evidence_basis`. Referred upward as an open protocol gap; a `record_kind: identity_correction` is named and deliberately not implemented.

## CORPUS P269
**Short title:** The fragile genes FHIT and WWOX are inactivated coordinately in invasive brea...
**Full title:** The fragile genes FHIT and WWOX are inactivated coordinately in invasive breast carcinoma
**Authors:** Guler et al.
**Year:** 2004
**Source type:** Article
**Journal/source:** Cancer
**Identifier:** PMID 15073846 / DOI 10.1002/cncr.20137
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0269
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P270
**Short title:** Tumor Suppressor WWOX Contributes to the Elimination of Tumorigenic Cells in...
**Full title:** Tumor Suppressor WWOX Contributes to the Elimination of Tumorigenic Cells in Drosophila melanogaster
**Authors:** O'Keefe et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 26302329 / PMC4547717 / DOI 10.1371/journal.pone.0136356
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0270
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P271
**Short title:** Loss of WWOX expression in human extrahepatic cholangiocarcinoma
**Full title:** Loss of WWOX expression in human extrahepatic cholangiocarcinoma
**Authors:** Wang et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** J Cancer Res Clin Oncol
**Identifier:** PMID 18629536 / PMC12160241 / DOI 10.1007/s00432-008-0449-4
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0271
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P272
**Short title:** Characterizing WW domain interactions of tumor suppressor WWOX reveals its as...
**Full title:** Characterizing WW domain interactions of tumor suppressor WWOX reveals its association with multiprotein networks
**Authors:** Abu-Odeh et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 24550385 / PMC3979411 / DOI 10.1074/jbc.M113.506790
**Tier (FASE 1):** C
**Status:** read — corpus placeholder, not promoted (`CC-20260914-PLACEHOLDER-READS-01`, `BATCH_20260926_ALDAZ_R2`); see `Evidence depth`
**Evidence depth:** complete_fulltext_read — `FTR-20260810-24550385-02`; manifest `deepdive_manifests/PMID24550385.json` (20 locators, schema v2, strict PASS, 0 gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**LIT link:** LIT-0272
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P273
**Short title:** PARTICLE triplexes cluster in the tumor suppressor WWOX and may extend throug...
**Full title:** PARTICLE triplexes cluster in the tumor suppressor WWOX and may extend throughout the human genome
**Authors:** O'Leary et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Sci Rep
**Identifier:** PMID 28769061 / PMC5541130 / DOI 10.1038/s41598-017-07295-5
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0273
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P274
**Short title:** Strategies of oncogenic microbes to deal with WW domain-containing oxidoreduc...
**Full title:** Strategies of oncogenic microbes to deal with WW domain-containing oxidoreductase
**Authors:** Chang et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25488911 / PMC4935232 / DOI 10.1177/1535370214561957
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0274
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P275
**Short title:** Helicobacter pylori infection promotes methylation of WWOX gene in human gast...
**Full title:** Helicobacter pylori infection promotes methylation of WWOX gene in human gastric cancer
**Authors:** Yan et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Biochem Biophys Res Commun
**Identifier:** PMID 21466786 / DOI 10.1016/j.bbrc.2011.03.127
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0275
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P276
**Short title:** Association between WWOX and the risk of malignant tumor, especially among As...
**Full title:** Association between WWOX and the risk of malignant tumor, especially among Asians: evidence from a meta-analysis
**Authors:** # et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Onco Targets Ther
**Identifier:** PMID 29662317 / PMC5892619 / DOI 10.2147/OTT.S152140
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0276
**Primary pathway:** animal model — pathway variable
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P277
**Short title:** Association of Wwox with ErbB4 in breast cancer
**Full title:** Association of Wwox with ErbB4 in breast cancer
**Authors:** Aqeilan et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 17909041 / DOI 10.1158/0008-5472.CAN-07-2147
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0277
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P278
**Short title:** Therapeutic Zfra4-10 or WWOX7-21 Peptide Induces Complex Formation of WWOX wi...
**Full title:** Therapeutic Zfra4-10 or WWOX7-21 Peptide Induces Complex Formation of WWOX with Selective Protein Targets in Organs that Leads to Cancer Suppression and Spleen Cytotoxic Memory Z Cell Activation In Vivo
**Authors:** Su et al.
**Year:** 2020
**Source type:** Article
**Journal/source:** Cancers (Basel)
**Identifier:** PMID 32764489 / PMC7464583 / DOI 10.3390/cancers12082189
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0278
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P279
**Short title:** [Effects of WWOX gene transfection on cell growth of epithelial ovarian cancer]
**Full title:** [Effects of WWOX gene transfection on cell growth of epithelial ovarian cancer]
**Authors:** [Article in Chinese]
**Year:** 2008
**Source type:** Article
**Journal/source:** Zhonghua Fu Chan Ke Za Zhi
**Identifier:** PMID 18953870
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0279
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P280
**Short title:** Physical and functional interactions between the Wwox tumor suppressor protei...
**Full title:** Physical and functional interactions between the Wwox tumor suppressor protein and the AP-2gamma transcription factor
**Authors:** Aqeilan et al.
**Year:** 2004
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 15548692 / DOI 10.1158/0008-5472.CAN-04-2055
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0280
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P281
**Short title:** Inhibition of breast cancer cell growth in vitro and in vivo: effect of resto...
**Full title:** Inhibition of breast cancer cell growth in vitro and in vivo: effect of restoration of Wwox expression
**Authors:** Iliopoulos et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Clin Cancer Res
**Identifier:** PMID 17200365 / DOI 10.1158/1078-0432.CCR-06-2038
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0281
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P282
**Short title:** Inactivation of the Wwox gene accelerates forestomach tumor progression in vivo
**Full title:** Inactivation of the Wwox gene accelerates forestomach tumor progression in vivo
**Authors:** Aqeilan et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 17575124 / PMC2621009 / DOI 10.1158/0008-5472.CAN-07-1081
**Tier (FASE 1):** C
**Status:** promoted — see [[paper_registry_current#PAPER 077]] (`BATCH_20260815_001`)
**LIT link:** LIT-0282
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P283
**Short title:** Epigenetic and genetic alterations affect the WWOX gene in head and neck squa...
**Full title:** Epigenetic and genetic alterations affect the WWOX gene in head and neck squamous cell carcinoma
**Authors:** Ekizoglu et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 25612104 / PMC4303423 / DOI 10.1371/journal.pone.0115353
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0283
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P284
**Short title:** Tumor suppressor WWOX binds to ΔNp63α and sensitizes cancer cells to chemothe...
**Full title:** Tumor suppressor WWOX binds to ΔNp63α and sensitizes cancer cells to chemotherapy
**Authors:** Salah et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Cell Death Dis
**Identifier:** PMID 23370280 / PMC3564006 / DOI 10.1038/cddis.2013.6
**Tier (FASE 1):** C
**Status:** promoted — see [[paper_registry_current#PAPER 079]] (`BATCH_20260815_001`)
**LIT link:** LIT-0284
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P285
**Short title:** Association between CpG island methylation of the WWOX gene and its expressio...
**Full title:** Association between CpG island methylation of the WWOX gene and its expression in breast cancers
**Authors:** Wang et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Tumour Biol
**Identifier:** PMID 19188760 / DOI 10.1159/000197911
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0285
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P286
**Short title:** Dias 2007 — IHC di WWOX in 53 lesioni tiroidee: marcatura assente o debole nel carcinoma papillare, conservata nei follicolari
**Full title:** Association between decreased WWOX protein expression and thyroid cancer development
**Authors:** Dias EP, Pimenta FJ, Sarquis MS, Dias Filho MA, Aldaz CM, Fujii JB, Gomez RS, De Marco L (8 authors, esummary). The page prints `Flavio J Pimenta` without the accent and `C M Aldaz`
**Year:** 2007
**Source type:** Article
**Journal/source:** Thyroid
**Identifier:** PMID 18047428 / PMC4150466 / DOI 10.1089/thy.2007.0232
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-18047428-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID18047428.json`, dossier `fulltext_dossiers/PMID18047428.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260926_ALDAZ_R2` (`CC-20260914-18047428-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0286
**Primary pathway:** oncology / tumor suppressor biology — espressione proteica tissutale (IHC). 🔴 **Corrected from `P6 — DDR / genome stability`**: no DNA-damage, repair or genome-stability measurement exists in this paper, and no RNA or DNA assay of any kind
**Model/species:** tessuto tiroideo umano adulto: **53 lesioni da 46 pazienti** eutiroidei sottoposti a tiroidectomia totale (22 PTC, 11 FTC, 20 FA; 7 pazienti con due lesioni). Nessuna linea cellulare, nessun animale, nessun allele germinale, **nessun materiale neurale proprio**
**Genotype/model:** WWOX somatico; nessun allele WWOX-DEE
**Transferability:** **T3**
**clinical relevance:** **LOW** — unchanged
**Claim links:** none — the reading proposes none
**Role:** Osservazione IHC in oncologia adulta: marcatura WWOX presente in 11/11 FTC, 19/20 FA e **8/22 PTC** (conteggi ricostruiti dalle percentuali); intensità 3+ in 82% FTC, 20% FA, **0% PTC**; assenza in 64% PTC. La direzione regge in ogni taglio della tabella (ricalcolato p≈4.5×10⁻⁸) e nelle 7 coppie intra-paziente. L'epitelio follicolare normale marca, sempre citoplasmatico. **Parità delle fonti** e nient'altro
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. *(2026-09-26: no longer true for reading depth — this paper has since been read in full; see `Evidence depth`. Triage status unchanged.)*
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-18047428-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Reading note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** Manoscritto d'autore (Europe PMC `fullTextXML` 404; efetch rifiuta l'XML; ptpmcrender 403; **la pagina PMC ha servito un interstiziale reCAPTCHA sotto HTTP 200 per tre richieste** e l'articolo solo dopo 75 s di attesa). 🔴 **La Figura 1 è in scala di grigi su entrambe le vie disponibili** (raster PDF e blob CDN PMC, misurato): in un'immunoistochimica DAB/ematossilina il cromogeno non è separabile dal controcolorante, quindi **nessun grado di intensità del paper è verificabile sulla sua stessa figura**. **Difetti interni misurati:** i Risultati danno *"no expression in seven out of seven microcarcinomas"* mentre la Discussione descrive un **microcarcinoma di 0.6 cm con espressione moderata** *"in association with an FTC"*, co-occorrenza che i Metodi non prevedono (solo FA+PTC); l'abstract dice *"no expression in PTCs"* per le coppie, il corpo 5/7 assente e 2 deboli; il pannello 1J è *"weak"* nei Risultati e *"the same expression as normal thyroid"* in legenda; l'**estensione** della marcatura è stata registrata e mai riportata; unico p-value `= 0.000` senza tabella; 53 lesioni da 46 pazienti trattate come indipendenti; un solo patologo; controllo negativo per sola omissione del primario; **antisiero senza fonte né referenza** — non può servire come fonte di validazione anticorpale per nulla. **L'unica frase neurale è una citazione** (rif. 12 = PMID 16941225, `PAPER 106`): questo lavoro non va citato come seconda fonte per l'espressione neurale di WWOX, che conterebbe due volte una sola osservazione. Dependency screen: `UNSCREENABLE_NO_REFERENCE_LIST` — nessun riferimento vagliato. *(The triage `Note` and the R1 `Registration note` above are superseded for every field this batch writes; their text is kept as history.)*

## CORPUS P287
**Short title:** The JNK inhibitor SP600129 enhances apoptosis of HCC cells induced by the tum...
**Full title:** The JNK inhibitor SP600129 enhances apoptosis of HCC cells induced by the tumor suppressor WWOX
**Authors:** Aderca et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** J Hepatol
**Identifier:** PMID 18620777 / PMC2574998 / DOI 10.1016/j.jhep.2008.05.015
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0287
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P288
**Short title:** WWOX gene is associated with HDL cholesterol and triglyceride levels
**Full title:** WWOX gene is associated with HDL cholesterol and triglyceride levels
**Authors:** Sáez et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** BMC Med Genet
**Identifier:** PMID 20942981 / PMC2967537 / DOI 10.1186/1471-2350-11-148
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0288
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P289
**Short title:** Intertwined Relationship of WWOX and RUNX2 Proteins as a Biomarker for Predic...
**Full title:** Intertwined Relationship of WWOX and RUNX2 Proteins as a Biomarker for Predicting Response and Survival in Patients With Childhood Bone Cancer in North India: A Pilot Study
**Authors:** Sharma et al.
**Year:** 2025
**Source type:** Article
**Journal/source:** Cureus
**Identifier:** PMID 41141138 / PMC12552799 / DOI 10.7759/cureus.93160
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0289
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P290
**Short title:** Allostery mediates ligand binding to WWOX tumor suppressor via a conformation...
**Full title:** Allostery mediates ligand binding to WWOX tumor suppressor via a conformational switch
**Authors:** Schuchardt et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** J Mol Recognit
**Identifier:** PMID 25703206 / PMC4376589 / DOI 10.1002/jmr.2419
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0290
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P291
**Short title:** In vitro and in silico assessment of the effect of WWOX expression on invasiv...
**Full title:** In vitro and in silico assessment of the effect of WWOX expression on invasiveness pathways associated with AP-2 transcription factors in bladder cancer
**Authors:** # et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** BMC Urol
**Identifier:** PMID 33691672 / PMC7944886 / DOI 10.1186/s12894-021-00806-7
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0291
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P292
**Short title:** Expression of FRA16D/WWOX and FRA3B/FHIT genes in hematopoietic malignancies
**Full title:** Expression of FRA16D/WWOX and FRA3B/FHIT genes in hematopoietic malignancies
**Authors:** Ishii et al.
**Year:** 2003
**Source type:** Article
**Journal/source:** Mol Cancer Res
**Identifier:** PMID 14638866
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0292
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P293
**Short title:** Genetic and epigenetic alterations of WWOX in the development of gastric card...
**Full title:** Genetic and epigenetic alterations of WWOX in the development of gastric cardia adenocarcinoma
**Authors:** Guo et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Environ Mol Mutagen
**Identifier:** PMID 23197378 / DOI 10.1002/em.21748
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0293
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P294
**Short title:** The tumour suppressor gene WWOX is mutated in autosomal recessive cerebellar...
**Full title:** The tumour suppressor gene WWOX is mutated in autosomal recessive cerebellar ataxia with epilepsy and mental retardation
**Authors:** Mallaret et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Brain
**Identifier:** PMID 24369382 / PMC3914474 / DOI 10.1093/brain/awt338
**Tier (FASE 1):** A
**Status:** promoted — see [[paper_registry_current#PAPER 042]] (BATCH_20260710_A); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0294
**Primary pathway:** clinical spectrum / SCAR12
**Model/species:** human + mouse — il paper non contiene esperimenti su ratto; il ratto *lde* è solo un comparatore citato (corretto da `BATCH_20260926_MALLARET`; valutazione in [[paper_registry_current#PAPER 042]])
**Genotype/model:** unassigned in triage
**Transferability:** see [[paper_registry_current#PAPER 042]] (T1/T2 — genotype caution P47T ≠ Q230P)
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Role:** priority full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P295
**Short title:** Generation and characterization of mice carrying a conditional allele of the...
**Full title:** Generation and characterization of mice carrying a conditional allele of the Wwox tumor suppressor gene
**Authors:** Ludes-Meyers et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 19936220 / PMC2777388 / DOI 10.1371/journal.pone.0007775
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0295
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.
**Resolved (BATCH_20260806_002):** promoted to [[paper_registry_current#PAPER 057]] after the complete full-text read (`FTR-20260806-19936220-01`). This placeholder is preserved append-only as triage lineage; the integrated record is authoritative. Its `Tier B` and `Primary pathway: P5` were triage guesses and are superseded there.

## CORPUS P296
**Short title:** Upregulation of the putative oncogene COTE1 contributes to human hepatocarcin...
**Full title:** Upregulation of the putative oncogene COTE1 contributes to human hepatocarcinogenesis through modulation of WWOX signaling
**Authors:** Zhang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 24899407 / DOI 10.3892/ijo.2014.2482
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0296
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P297
**Short title:** Functional and clinical characterization of the putative tumor suppressor WWO...
**Full title:** Functional and clinical characterization of the putative tumor suppressor WWOX in non-small cell lung cancer
**Authors:** Becker et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** J Thorac Oncol
**Identifier:** PMID 21892104 / DOI 10.1097/JTO.0b013e31822e59dd
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0297
**Primary pathway:** P9 — immune / glia / inflammation
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P298
**Short title:** Neuroimaging features of WOREE syndrome: a mini-review of the literature
**Full title:** Neuroimaging features of WOREE syndrome: a mini-review of the literature
**Authors:** Battaglia et al.
**Year:** 2023
**Source type:** Review
**Journal/source:** Front Pediatr
**Identifier:** PMID 38161429 / PMC10757851 / DOI 10.3389/fped.2023.1301166
**Tier (FASE 1):** A
**Status:** promoted — see [[paper_registry_current#PAPER 046]] (BATCH_20260710_B); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0298
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Role:** priority full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P299
**Short title:** Molecular origin of the binding of WWOX tumor suppressor to ErbB4 receptor ty...
**Full title:** Molecular origin of the binding of WWOX tumor suppressor to ErbB4 receptor tyrosine kinase
**Authors:** Schuchardt et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Biochemistry
**Identifier:** PMID 24308844 / PMC3906126 / DOI 10.1021/bi400987k
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0299
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P300
**Short title:** Early infantile-onset epileptic encephalopathy 28 due to a homozygous microde...
**Full title:** Early infantile-onset epileptic encephalopathy 28 due to a homozygous microdeletion involving the WWOX gene in a region of uniparental disomy
**Authors:** Davids et al.
**Year:** 2019
**Source type:** Article
**Journal/source:** Hum Mutat
**Identifier:** PMID 30362252 / PMC6296882 / DOI 10.1002/humu.23675
**Tier (FASE 1):** A
**Status:** promoted — see [[paper_registry_current#PAPER 044]] (BATCH_20260710_B); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0300
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Role:** priority full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P301
**Short title:** Novel mutations in WWOX, RARS2, and C10orf2 genes in consanguineous Arab fami...
**Full title:** Novel mutations in WWOX, RARS2, and C10orf2 genes in consanguineous Arab families with intellectual disability
**Authors:** Alkhateeb et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Metab Brain Dis
**Identifier:** PMID 27121845 / DOI 10.1007/s11011-016-9827-9
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0301
**Primary pathway:** unassigned — triage only
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P302
**Short title:** Expression of CD133, E-cadherin and WWOX in colorectal cancer and related ana...
**Full title:** Expression of CD133, E-cadherin and WWOX in colorectal cancer and related analysis
**Authors:** Sun et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Pak J Med Sci
**Identifier:** PMID 28523049 / PMC5432716 / DOI 10.12669/pjms.332.11687
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0302
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P303
**Short title:** Mol Cancer
**Full title:** Mol Cancer
**Authors:** . Jun:14:112. doi:.1186/s12943-015-0389-y.
**Year:** unknown
**Source type:** Article
**Journal/source:** Retracted article
**Identifier:** PMID 26041563 / PMC4453100
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0303
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P304
**Short title:** ACK1 promotes hepatocellular carcinoma progression via downregulating WWOX an...
**Full title:** ACK1 promotes hepatocellular carcinoma progression via downregulating WWOX and activating AKT signaling
**Authors:** Xie et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 25738261 / DOI 10.3892/ijo.2015.2910
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0304
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P305
**Short title:** The tumor suppressor gene WWOX links the canonical and noncanonical NF-κB pat...
**Full title:** The tumor suppressor gene WWOX links the canonical and noncanonical NF-κB pathways in HTLV-I Tax-mediated tumorigenesis
**Authors:** Fu et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Blood
**Identifier:** PMID 21115974 / PMC3318777 / DOI 10.1182/blood-2010-08-303073
**Tier (FASE 1):** C
**Status:** promoted — see [[paper_registry_current#PAPER 086]], the record that carries this paper's reading (pointer written by `BATCH_20260926_ALDAZ_R2`, `CC-20260914-PLACEHOLDER-IDENTITY-01`); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0305
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Next action:** none — promotion completed; see the PAPER record
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P306
**Short title:** WWOX oxidoreductase--substrate and enzymatic characterization
**Full title:** WWOX oxidoreductase--substrate and enzymatic characterization
**Authors:** Sałuda-Gorgul et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Z Naturforsch C J Biosci
**Identifier:** PMID 21476439 / DOI 10.1515/znc-2011-1-210
**Tier (FASE 1):** A
**Status:** read in full 2026-10-04 — receipt `FTR-20261004-21476439-01` and manifest exist; promoted to [[paper_registry_current#PAPER 244]] and kept here as history
**LIT link:** LIT-0306
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** HIGH
**Claim links:** none — the reading supports no canonical claim. Promoted to [[paper_registry_current#PAPER 244]] on 2026-10-04.
**Role:** deep-dive — full text required; the only assay of WWOX catalysis **identified in the corpus read here as of 2026-09-28** (`PREMISE: INFERENZA` for the *only-one* scoping; the paper itself is now READ IN FULL — receipt `FTR-20261004-21476439-01`, manifest `deepdive_manifests/PMID21476439.json`, 17 verbatim locators, blind locator audit 2026-10-04). Scoped 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` M9
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. 🔴 **Re-tiered 2026-09-27 (C / LOW → A / HIGH):** this is the only measurement of WWOX catalytic activity **identified in the corpus read here as of 2026-09-28** (`PREMISE: INFERENZA` — the record is at abstract depth with `PREMISE: UNREAD_PRIMARY` and no receipt, so *"the only published"* was a claim about the literature this record cannot make) — dehydrogenase activity on seven steroid substrates with NAD⁺ and NADP⁺ and published apparent Km values, oxidation only. 🔵 **READ IN FULL 2026-10-04** (`FTR-20261004-21476439-01`; blind locator audit the same day — 17 triples, 15 SUPPORTED, 2 NOT_SUPPORTED_AS_LABELLED, 0 UNVERIFIABLE): the activity is measured in the **soluble fraction of a bacterial crude extract**, because activity was lost in *any attempt of purification to near-homogeneity*; the protein is **wild-type human WWOX expressed from a cDNA *fragment* excised with BamHI/EcoRI** as a NusA or GST fusion — the paper never prints *full-length* for the insert and describes no domain-only construct, so *full-length* is a DERIVATION (`PREMISE: INFERENZA`) and **no allele of any kind was tested**; **no Vmax, kcat, specific activity or reaction product is reported**, although the Methods promise a Vmax; Table II's own footnote states the Km values are the DIFFERENCE between the WWOX and empty-vector extracts; 13 of the 14 Km values lie below the lowest substrate concentration Table I used (the single exception is testosterone with NADP⁺); and all 14 printed Mann-Whitney p values (0.0000–0.0091) lie below the floor attainable with the stated n of *at least two or three* (a DERIVATION from the printed n, `PREMISE: INFERENZA`). The reduction negative is a *results-not-shown* sentence over the same seven steroids, and the paper adds that the reduction activities were *similar* in both extracts. See `CC-20261004W10-X-ENZYMOLOGY-01`. **Acquisition, corrected:** a DOI DOES exist — `10.1515/znc-2011-1-210` — and Unpaywall and OpenAlex both classify the article hybrid open access with a publisher-hosted PDF; the publisher answers automated fetches with HTTP 202 and zero bytes. The blocker is an automated-traffic challenge, **not** the absence of a deposit: one human fetch of the publisher PDF closes it, at no cost (`FT-130`, packet item `A11`). **NOT promoted to a PAPER record:** no reading stands behind it.

## CORPUS P307
**Short title:** WW domain-containing proteins, WWOX and YAP, compete for interaction with Erb...
**Full title:** WW domain-containing proteins, WWOX and YAP, compete for interaction with ErbB-4 and modulate its transcriptional function
**Authors:** Aqeilan et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 16061658 / DOI 10.1158/0008-5472.CAN-05-1150
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0307
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P308
**Short title:** WW domain-containing oxidoreductase's role in myriad cancers: clinical signif...
**Full title:** WW domain-containing oxidoreductase's role in myriad cancers: clinical significance and future implications
**Authors:** Gardenswartz et al.
**Year:** 2014
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 24510053 / DOI 10.1177/1535370213519213
**Tier (FASE 1):** C
**Status:** read — corpus placeholder promoted to a read record (`CC-20260909-24510053-01`)
**Evidence depth:** full text reviewed — `FTR-20260909-24510053-01` (`complete_fulltext_read`); manifest `deepdive_manifests/PMID24510053.json` (9 locators, **all page adjudications**, strict PASS, 0 gaps; `regenerate_adjudications.py verify` 9/9)
**LIT link:** LIT-0308
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** no WWOX-DEE allele; oncology review
**Transferability:** T3
**clinical relevance:** LOW — **proposed unchanged, and that is not an oversight.** The paper genuinely contains nothing about the reference genotype; inflating the field because the reading turned out useful would corrupt exactly the signal the field exists to carry. Its value is mechanistic and archival, not clinical.
**Claim links:** none — no new claim is created by this reading
**Role:** **read secondary source; carries the primary provenance for `DIS-001`'s ACK1 cascade**
**Note:** 🔴 **Source type `Review` is kept prominent: secondary throughout, and no claim gains or loses evidentiary support from this reading.** Metadata corrections applied in `BATCH_20260909_001`: pages are **253–263**, not 253–9. The reading's product is provenance — it supplies the published source of the ACK1→WWOX polyubiquitination cascade that active rejection `DIS-001` rests on (ref 31 = PMID 16288044, Mahajan NP, Whang YE, Mohler JL, Earp HS, *Cancer Res* 2005;65:10514–23), a paper this repository holds at **no depth at all**. It also supplies a citable in-the-wild instance of premise `D-01` in a WWOX-specific source by the gene's own primary group: ubiquitination defined as labelling *"and thus designated for degradation via the proteasomal system"*, cited to a bone-formation review with no WWOX data. Its dated negative — *"So far no ubiquitin E3 ligase was associated with WWOX under normal or disease states."* — is recorded **with its date bound**. Acquisition note: the PDF text layer is `SUSPECT` (12 `þ` for `+`, 8 `0x02` for `−`), so all nine locators are anchored to rendered pages under rule 5e.

## CORPUS P309
**Short title:** Novel compound heterozygous mutations in the WWOX gene cause early infantile...
**Full title:** Novel compound heterozygous mutations in the WWOX gene cause early infantile epileptic encephalopathy
**Authors:** Yang et al.
**Year:** 2019
**Source type:** Case Reports
**Journal/source:** Int J Dev Neurosci
**Identifier:** PMID 31669195 / DOI 10.1016/j.ijdevneu.2019.10.003
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0309
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P310
**Short title:** Cancer Manag Res
**Full title:** Cancer Manag Res
**Authors:** . Jun:12:4379-4390. doi:.2147/CMAR.S244573. eCollection.
**Year:** unknown
**Source type:** Article
**Journal/source:** Retracted article
**Identifier:** PMID 32606933 / PMC7295110
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0310
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P311
**Short title:** Exploring the mechanism of WWOX growth inhibitory effects on oral squamous ce...
**Full title:** Exploring the mechanism of WWOX growth inhibitory effects on oral squamous cell carcinoma
**Authors:** Yang et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 28521426 / PMC5431404 / DOI 10.3892/ol.2017.5850
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0311
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P312
**Short title:** Relevance of Sp Binding Site Polymorphism in WWOX for Treatment Outcome in Pa...
**Full title:** Relevance of Sp Binding Site Polymorphism in WWOX for Treatment Outcome in Pancreatic Cancer
**Authors:** Schirmer et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** J Natl Cancer Inst
**Identifier:** PMID 26857392 / PMC4859408 / DOI 10.1093/jnci/djv387
**Tier (FASE 1):** C
**Status:** promoted — see [[paper_registry_current#PAPER 050]] (BATCH_20260710_B); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0312
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P313
**Short title:** The downregulation of WWOX induces epithelial-mesenchymal transition and enha...
**Full title:** The downregulation of WWOX induces epithelial-mesenchymal transition and enhances stemness and chemoresistance in breast cancer
**Authors:** Li et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 30335523 / PMC6434457 / DOI 10.1177/1535370218806455
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0313
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P314
**Short title:** The correlation analysis of WWOX expression and cancer related genes in neuro...
**Full title:** The correlation analysis of WWOX expression and cancer related genes in neuroblastoma- a real time RT-PCR study
**Authors:** Nowakowska et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Acta Biochim Pol
**Identifier:** PMID 24455756
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0314
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P315
**Short title:** The role of WWOX polymorphisms on COPD susceptibility and pulmonary function...
**Full title:** The role of WWOX polymorphisms on COPD susceptibility and pulmonary function traits in Chinese: a case-control study and family-based analysis
**Authors:** Xie et al.
**Year:** 2016
**Source type:** Multicenter Study
**Journal/source:** Sci Rep
**Identifier:** PMID 26902998 / PMC4763216 / DOI 10.1038/srep21716
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0315
**Primary pathway:** animal model — pathway variable
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P316
**Short title:** Genetic alterations of WWOX in Wilms' tumor are involved in its carcinogenesis
**Full title:** Genetic alterations of WWOX in Wilms' tumor are involved in its carcinogenesis
**Authors:** Płuciennik et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Oncol Rep
**Identifier:** PMID 22842668 / DOI 10.3892/or.2012.1940
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0316
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P317
**Short title:** Genetic alterations of the tumor suppressor gene WWOX in esophageal squamous...
**Full title:** Genetic alterations of the tumor suppressor gene WWOX in esophageal squamous cell carcinoma
**Authors:** Kuroki et al.
**Year:** 2002
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 11956080
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0317
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P318
**Short title:** Loss of wwox expression in zebrafish embryos causes edema and alters Ca(2+) d...
**Full title:** Loss of wwox expression in zebrafish embryos causes edema and alters Ca(2+) dynamics
**Authors:** Tsuruwaka et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** PeerJ
**Identifier:** PMID 25649963 / PMC4312067 / DOI 10.7717/peerj.727
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0318
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** zebrafish
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P319
**Short title:** The polymorphisms and haplotypes of WWOX gene are associated with the risk of...
**Full title:** The polymorphisms and haplotypes of WWOX gene are associated with the risk of lung cancer in southern and eastern Chinese populations
**Authors:** Huang et al.
**Year:** 2013
**Source type:** Comparative Study
**Journal/source:** Mol Carcinog
**Identifier:** PMID 22693020 / DOI 10.1002/mc.21934
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0319
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P320
**Short title:** Upregulation of tumor suppressor WWOX promotes immune response in glioma
**Full title:** Upregulation of tumor suppressor WWOX promotes immune response in glioma
**Authors:** Yang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Cell Immunol
**Identifier:** PMID 24044959 / DOI 10.1016/j.cellimm.2013.07.015
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0320
**Primary pathway:** P9 — immune / glia / inflammation
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P321
**Short title:** Tumor suppressor genes FHIT and WWOX are deleted in primary effusion lymphoma...
**Full title:** Tumor suppressor genes FHIT and WWOX are deleted in primary effusion lymphoma (PEL) cell lines
**Authors:** Roy et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Blood
**Identifier:** PMID 21685375 / PMC3158728 / DOI 10.1182/blood-2010-12-323659
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0321
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P322
**Short title:** miR-134 induces oncogenicity and metastasis in head and neck carcinoma throug...
**Full title:** miR-134 induces oncogenicity and metastasis in head and neck carcinoma through targeting WWOX gene
**Authors:** Liu et al.
**Year:** 2014
**Source type:** Comparative Study
**Journal/source:** Int J Cancer
**Identifier:** PMID 23824713 / DOI 10.1002/ijc.28358
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0322
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P323
**Short title:** Synergistic effect of toosendanin and regorafenib against cell proliferation...
**Full title:** Synergistic effect of toosendanin and regorafenib against cell proliferation and migration by regulating WWOX signaling pathway in hepatocellular carcinoma
**Authors:** Yang et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** Phytother Res
**Identifier:** PMID 34058790 / DOI 10.1002/ptr.7174
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0323
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P324
**Short title:** Frequent loss of WWOX expression in breast cancer: correlation with estrogen...
**Full title:** Frequent loss of WWOX expression in breast cancer: correlation with estrogen receptor status
**Authors:** Nunez MI, Ludes-Meyers J, Abba MC, Kil H, Abbey NW, Page RE, Sahin A, Klein-Szanto AJP, Aldaz CM
**Year:** 2005
**Source type:** primary immunohistochemistry series on pooled breast tissue microarrays (16 normal, 15 DCIS, 203 invasive ductal carcinoma) with an independent 23-tumour immunoblot set
**Journal/source:** Breast Cancer Res Treat
**Identifier:** PMID 15692750 / PMC4145848 / DOI 10.1007/s10549-004-1474-x
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-15692750-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID15692750.json`, dossier `fulltext_dossiers/PMID15692750.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260926_ALDAZ_R2` (`CC-20260913-ALDAZ-B003-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0324
**Primary pathway:** baseline expression / tumour-tissue protein loss — 🔴 **corrected from `P5 — metabolism / mitochondria / redox`**, which reproduced the laboratory's SDR/sex-steroid framing as though it were the paper's measurement; the paper measures no steroid, receptor function or enzyme activity, and its own words are that the SDR domain *"is **predicted** to be involved in sex-steroid metabolism"*
**Model/species:** human adult breast tissue
**Genotype/model:** none — somatic tumour tissue, no WWOX allele
**Transferability:** **T3**, `ESPANSIONE`
**clinical relevance:** LOW — unchanged
**Claim links:** none — the reading proposes none
**Role:** the anti-WWOX reagent's **method** paper of record — the paper `PAPER 105` cites for its immunostaining protocol and scoring — and it contains **no immunohistochemical specificity control of any kind**
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. *(2026-09-26: no longer true for reading depth — this paper has since been read in full; see `Evidence depth`. Triage status unchanged.)*
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Reading note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** Read in full (`FTR-20260913-15692750-01`, 12 of 12 panels inspected as images). **Over-inference risk, evaluated** where the triage said *"not evaluated"*: **HIGH on the SDR/sex-steroid framing, LOW on the staining observation.** The inferential step is from *"WWOX immunostaining correlates with ER status"* to *"further strengthen the hypothesis that WWOX plays a role in sex-steroid metabolism"*, with nothing hormonal measured; the staining observation itself (34% completely negative, 60% reduced-or-lost, ER− worse than ER+) is a competent series, and the ER association is a measured contingency-table correlation over all 203 invasive cases, **unadjusted**. Its immunoblot is the better of the reagent pair: molecular-weight marks at 39 kD and 31 kD, a `NEG.` PEO1 lane on each of two gels blank for WWOX while carrying actin in that same lane, and a two-gel composite declared in its own caption. It delegates the antibody's characterisation onward to `PMID 14526170` (`PAPER 101`). Kept as a CORPUS record, as `CORPUS P261` and `P268` are: the candidate proposed promotion; this batch completes the record in place and creates no new PAPER number for it. *(The triage `Note` and the R1 `Registration note` above are superseded for every field this batch writes; their text is kept as history.)*

## CORPUS P325
**Short title:** Primary WWOX phosphorylation and JNK activation during etoposide induces cyto...
**Full title:** Primary WWOX phosphorylation and JNK activation during etoposide induces cytotoxicity in HEK293 cells
**Authors:** Jamshidiha et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Daru
**Identifier:** PMID 22615609 / PMC3304374
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0325
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P326
**Short title:** SENP2 regulated the stability of β-catenin through WWOX in hepatocellular car...
**Full title:** SENP2 regulated the stability of β-catenin through WWOX in hepatocellular carcinoma cell
**Authors:** Jiang et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Tumour Biol
**Identifier:** PMID 24969559 / DOI 10.1007/s13277-014-2239-8
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0326
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P327
**Short title:** Early onset epileptic encephalopathy caused by novel compound heterozygous mu...
**Full title:** Early onset epileptic encephalopathy caused by novel compound heterozygous mutation of WWOX gene
**Authors:** Su et al.
**Year:** 2020
**Source type:** Case Reports
**Journal/source:** Int J Dev Neurosci
**Identifier:** PMID 32037574 / DOI 10.1002/jdn.10013
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0327
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P328
**Short title:** The Tumor-Suppressor WWOX and HDAC3 Inhibit the Transcriptional Activity of t...
**Full title:** The Tumor-Suppressor WWOX and HDAC3 Inhibit the Transcriptional Activity of the β-Catenin Coactivator BCL9-2 in Breast Cancer Cells
**Authors:** El-Hage et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Mol Cancer Res
**Identifier:** PMID 25678599 / DOI 10.1158/1541-7786.MCR-14-0180
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0328
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P329
**Short title:** The prognostic significance of WWOX expression in patients with breast cancer...
**Full title:** The prognostic significance of WWOX expression in patients with breast cancer and its association with the basal-like phenotype
**Authors:** Wang et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** J Cancer Res Clin Oncol
**Identifier:** PMID 20401669 / PMC11828298 / DOI 10.1007/s00432-010-0880-1
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0329
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P330
**Short title:** Complement C1q activates tumor suppressor WWOX to induce apoptosis in prostat...
**Full title:** Complement C1q activates tumor suppressor WWOX to induce apoptosis in prostate cancer cells
**Authors:** Hong et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 19484134 / PMC2685983 / DOI 10.1371/journal.pone.0005755
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0330
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P331
**Short title:** Virus-encoded miR-155 ortholog in Marek's disease virus promotes cell prolife...
**Full title:** Virus-encoded miR-155 ortholog in Marek's disease virus promotes cell proliferation via suppressing apoptosis by targeting tumor suppressor WWOX
**Authors:** Zhu et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** Vet Microbiol
**Identifier:** PMID 33191002 / DOI 10.1016/j.vetmic.2020.108919
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0331
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P332
**Short title:** Alternative transcripts of the candidate tumor suppressor gene, WWOX, are exp...
**Full title:** Alternative transcripts of the candidate tumor suppressor gene, WWOX, are expressed at high levels in human breast tumors
**Authors:** Driouch et al.
**Year:** 2002
**Source type:** Comparative Study
**Journal/source:** Oncogene
**Identifier:** PMID 11896615 / DOI 10.1038/sj.onc.1205273
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0332
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P333
**Short title:** The tumor suppressor WW domain-containing oxidoreductase modulates cell metab...
**Full title:** The tumor suppressor WW domain-containing oxidoreductase modulates cell metabolism
**Authors:** Abu-Remaileh et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25491415 / PMC4935230 / DOI 10.1177/1535370214561956
**Tier (FASE 1):** B
**Status:** promoted — see [[paper_registry_current#PAPER 073]] (`BATCH_20260815_001`)
**LIT link:** LIT-0333
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P334
**Short title:** Tumor Suppressor WWOX and p53 Alterations and Drug Resistance in Glioblastomas
**Full title:** Tumor Suppressor WWOX and p53 Alterations and Drug Resistance in Glioblastomas
**Authors:** Chiang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Front Oncol
**Identifier:** PMID 23459853 / PMC3586680 / DOI 10.3389/fonc.2013.00043
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0334
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P335
**Short title:** Comparative mapping and genomic annotation of the bovine oncosuppressor gene...
**Full title:** Comparative mapping and genomic annotation of the bovine oncosuppressor gene WWOX
**Authors:** Manera et al.
**Year:** 2009
**Source type:** Comparative Study
**Journal/source:** Cytogenet Genome Res
**Identifier:** PMID 20016169 / DOI 10.1159/000245919
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0335
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P336
**Short title:** WWOX induces apoptosis and inhibits proliferation of human hepatoma cell line...
**Full title:** WWOX induces apoptosis and inhibits proliferation of human hepatoma cell line SMMC-7721
**Authors:** Hu et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** World J Gastroenterol
**Identifier:** PMID 22736928 / PMC3380332 / DOI 10.3748/wjg.v18.i23.3020
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0336
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P337
**Short title:** Gourley 2005 — mRNA di WWOX variante 1 e variante 4 in 71 tumori ovarici e 13 ovaie controlaterali
**Full title:** WWOX mRNA expression profile in epithelial ovarian cancer supports the role of WWOX variant 1 as a tumour suppressor, although the role of variant 4 remains unclear
**Authors:** Gourley C, Paige AJW, Taylor KJ, Scott D, Francis NJ, Rush R, Aldaz CM, Smyth JF, Gabra H (9 authors, esummary; the artefact's meta tags print the fifth as `N-J FRANCIS`) — corrected from the literal placeholder `# et al.`
**Year:** 2005
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 15870886 / PMC4166600 / DOI 10.3892/ijo.26.6.1681
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260928-15870886-01` (a contemporaneous re-read of 2026-09-28 over the fingerprinted HTML/PDF, route (b) of `CC-20260914-15870886-01`; the 2026-09-14 reading `FTR-20260914-15870886-01` had not been appended to the ledger when this record was written); work manifest `deepdive_manifests/PMID15870886.json`, dossier `fulltext_dossiers/PMID15870886.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260928_007` (`CC-20260914-15870886-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0337
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** tessuto umano adulto: 71 tumori ovarici epiteliali consecutivi (83 prelevati, 12 esclusi) + 13 ovaie **controlaterali** di donne operate per sospetta malignità con istologia benigna; più la linea PEO1hyg1.6 (delezione omozigote esoni 4-8) e sei cloni transfettati. Nessun animale, nessun allele germinale, **nessun materiale neurale**
**Genotype/model:** unassigned in triage
**Transferability:** **T3**
**clinical relevance:** LOW
**Claim links:** none — no claim rests on this paper and this reading creates none
**Role:** Osservazione di espressione in oncologia adulta: l'mRNA WWOX full-length (variante 1) è ridotto nei tumori ovarici rispetto all'ovaio controlaterale (mediana 9.57 vs 22.9, Mann-Whitney p<0.0001, n=71 vs 13). Il trascritto Δ6-8 (variante 4) è **non quantificabile** e presente in **9/13 ovaie non maligne**, il che è la ragione del *"remains unclear"* nel titolo. Nessun meccanismo, nessun esperimento funzionale di WWOX (l'unica transfezione misura la sensibilità del saggio, mRNA contro proteina)
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.
**Identity note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** identity fields only, from `CC-20260914-15870886-01` §2. A reading of this paper exists (manifest `deepdive_manifests/PMID15870886.json`, dossier `fulltext_dossiers/PMID15870886.md`) but **no receipt was ever persisted** — the manifest carries one declared multihop gap and the strict receipt writer refuses declared gaps — so this record declares **no reading depth**, keeps its triage status and assessment fields, and carries none of the reading's findings. They wait for a persisted receipt (the load-bearing antecedent to read first is PMID 11572989). *(Superseded by the Reading note below for every field `BATCH_20260928_007` writes; kept as history.)*
**Reading note (BATCH_20260928_007, 2026-09-28, receipt `FTR-20260928-15870886-01`):** Manoscritto d'autore, non versione di record (Europe PMC `fullTextXML` 404; efetch rifiuta l'XML; pagina PMC 200 senza User-Agent; PDF dietro proof-of-work). **Difetti interni misurati in questa lettura, da riverificare sulla versione di record prima di citarli fuori da qui:** il testo scrive *"69 normal ovarian tissues"* dove i normali sono **13** e la Figura 2 lo conferma con barre multiple di 1/13; il limite inferiore normale è 9.3 nel testo mentre **nessuna barra normale esiste sotto 10** nei pixel; il denominatore oscilla fra 71 e 69 nello stesso paragrafo; **le Tabelle IIIA e IIIB totalizzano entrambe 66 e si contraddicono** (43 vs 42 espressori, 23 vs 24 non-espressori) con un'unica nota `P=0.006` sotto entrambe; la Figura 1C stampa `R2 = 0.9953` dove la legenda dà `R=0.9953` e la correlazione è retta da **un solo clone** (cinque punti a x<2, uno a ~(7,100)); la Figura 3A stampa `p=0.792`, valore che il testo non riporta. **Il limite che l'abstract non porta:** la variante 4 **non è un fattore prognostico indipendente** nel modello multivariato. Anticorpo policlonale anti-WW-domain **senza fonte né referenza**; la corsia parentale PEO1hyg1.6 priva di banda è un dato di specificità che però non può essere attribuito ad alcun antisiero identificato

## CORPUS P338
**Short title:** Aberrant expression of WWOX protein in epithelial ovarian cancer: a clinicopa...
**Full title:** Aberrant expression of WWOX protein in epithelial ovarian cancer: a clinicopathologic and immunohistochemical study
**Authors:** Lan et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Int J Gynecol Pathol
**Identifier:** PMID 22317867 / DOI 10.1097/PGP.0b013e3182297fd2
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0338
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P339
**Short title:** Combinations of single nucleotide polymorphisms WWOX-rs13338697, GALNT14-rs96...
**Full title:** Combinations of single nucleotide polymorphisms WWOX-rs13338697, GALNT14-rs9679162 and rs6025211 effectively stratify outcomes of chemotherapy in advanced hepatocellular carcinoma
**Authors:** Lin et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Asia Pac J Clin Oncol
**Identifier:** PMID 28695683 / DOI 10.1111/ajco.12745
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0339
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P340
**Short title:** Study of FHIT and WWOX expression in mucoepidermoid carcinoma and adenoid cys...
**Full title:** Study of FHIT and WWOX expression in mucoepidermoid carcinoma and adenoid cystic carcinoma of salivary gland
**Authors:** Dincer et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Oral Oncol
**Identifier:** PMID 20060354 / DOI 10.1016/j.oraloncology.2009.12.003
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0340
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P341
**Short title:** Functional genetic variant in the Kozak sequence of WW domain-containing oxid...
**Full title:** Functional genetic variant in the Kozak sequence of WW domain-containing oxidoreductase (WWOX) gene is associated with oral cancer risk
**Authors:** Cheng et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 27655721 / PMC5342485 / DOI 10.18632/oncotarget.12082
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0341
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P342
**Short title:** Association of polymorphisms in WWOX gene with risk and outcome of osteosarco...
**Full title:** Association of polymorphisms in WWOX gene with risk and outcome of osteosarcoma in a sample of the young Chinese population
**Authors:** Zhang et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Onco Targets Ther
**Identifier:** PMID 26929649 / PMC4767064 / DOI 10.2147/OTT.S99106
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0342
**Primary pathway:** P8 — bone / RUNX2 axis
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P343
**Short title:** W44X mutation in the WWOX gene causes intractable seizures and developmental...
**Full title:** W44X mutation in the WWOX gene causes intractable seizures and developmental delay: a case report
**Authors:** Elsaadany et al.
**Year:** 2016
**Source type:** Case Reports
**Journal/source:** BMC Med Genet
**Identifier:** PMID 27495153 / PMC4975905 / DOI 10.1186/s12881-016-0317-z
**Tier (FASE 1):** B
**Status:** promoted — see [[paper_registry_current#PAPER 049]] (BATCH_20260710_B); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0343
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P344
**Short title:** FRA16D common chromosomal fragile site oxido-reductase (FOR/WWOX) protects ag...
**Full title:** FRA16D common chromosomal fragile site oxido-reductase (FOR/WWOX) protects against the effects of ionizing radiation in Drosophila
**Authors:** O'Keefe et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Oncogene
**Identifier:** PMID 16007179 / DOI 10.1038/sj.onc.1208806
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0344
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** Drosophila
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P345
**Short title:** The long non-coding RNA PARTICLE is associated with WWOX and the absence of F...
**Full title:** The long non-coding RNA PARTICLE is associated with WWOX and the absence of FRA16D breakage in osteosarcoma patients
**Authors:** O'Leary et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 29152092 / PMC5675644 / DOI 10.18632/oncotarget.21086
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0345
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P346
**Short title:** Biophysical basis of the binding of WWOX tumor suppressor to WBP1 and WBP2 ad...
**Full title:** Biophysical basis of the binding of WWOX tumor suppressor to WBP1 and WBP2 adaptors
**Authors:** McDonald et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** J Mol Biol
**Identifier:** PMID 22634283 / PMC3412936 / DOI 10.1016/j.jmb.2012.05.015
**Tier (FASE 1):** C
**Status:** read — corpus placeholder, not promoted (`CC-20260914-PLACEHOLDER-READS-01`, `BATCH_20260926_ALDAZ_R2`); see `Evidence depth`
**Evidence depth:** complete_fulltext_read — `FTR-20260811-22634283-02`; manifest `deepdive_manifests/PMID22634283.json` (14 locators, schema v2, strict PASS, 0 gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**LIT link:** LIT-0346
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P347
**Short title:** [Expressions of WWOX and CD133 in colorectal cancer and their clinical signif...
**Full title:** [Expressions of WWOX and CD133 in colorectal cancer and their clinical significance]
**Authors:** [Article in Chinese]
**Year:** 2015
**Source type:** Article
**Journal/source:** Nan Fang Yi Ke Da Xue Xue Bao
**Identifier:** PMID 26607080
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0347
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P348
**Short title:** Genetic and Functional Evidence Links Germline Biallelic Inactivating Variant...
**Full title:** Genetic and Functional Evidence Links Germline Biallelic Inactivating Variants in WWOX to Histological Mixed-Type Thyroid Cancer
**Authors:** Zhang et al.
**Year:** 2025
**Source type:** Article
**Journal/source:** Adv Sci (Weinh)
**Identifier:** PMID 41124647 / PMC12767083 / DOI 10.1002/advs.202507602
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0348
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P349
**Short title:** A multi-exon deletion within WWOX is associated with a 46,XY disorder of sex...
**Full title:** A multi-exon deletion within WWOX is associated with a 46,XY disorder of sex development
**Authors:** White et al.
**Year:** 2012
**Source type:** Case Reports
**Journal/source:** Eur J Hum Genet
**Identifier:** PMID 22071891 / PMC3283189 / DOI 10.1038/ejhg.2011.204
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0349
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P350
**Short title:** [Effect of WWOX gene on the attachment and adhesion of ovarian cancer cells]
**Full title:** [Effect of WWOX gene on the attachment and adhesion of ovarian cancer cells]
**Authors:** [Article in Chinese]
**Year:** 2009
**Source type:** Article
**Journal/source:** Zhonghua Fu Chan Ke Za Zhi
**Identifier:** PMID 19957554
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0350
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P351
**Short title:** Alternating expression levels of WWOX tumor suppressor and cancer-related gen...
**Full title:** Alternating expression levels of WWOX tumor suppressor and cancer-related genes in patients with bladder cancer
**Authors:** Płuciennik et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Oncol Lett
**Identifier:** PMID 25295115 / PMC4186597 / DOI 10.3892/ol.2014.2476
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0351
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P352
**Short title:** Homozygous deletions may be markers of nearby heterozygous mutations: The com...
**Full title:** Homozygous deletions may be markers of nearby heterozygous mutations: The complex deletion at FRA16D in the HCT116 colon cancer cell line removes exons of WWOX
**Authors:** Alsop et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** Genes Chromosomes Cancer
**Identifier:** PMID 18273838 / DOI 10.1002/gcc.20548
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0352
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P353
**Short title:** Functional genetic variant of WW domain-containing oxidoreductase (WWOX) gene...
**Full title:** Functional genetic variant of WW domain-containing oxidoreductase (WWOX) gene is associated with hepatocellular carcinoma risk
**Authors:** Lee et al.
**Year:** 2017
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 28426730 / PMC5398630 / DOI 10.1371/journal.pone.0176141
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0353
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P354
**Short title:** [The relationship between FHIT and WWOX expression and clinicopathological fe...
**Full title:** [The relationship between FHIT and WWOX expression and clinicopathological features in hepatocellular carcinoma]
**Authors:** [Article in Chinese]
**Year:** 2010
**Source type:** Article
**Journal/source:** Zhonghua Gan Zang Bing Za Zhi
**Identifier:** PMID 20510001 / DOI 10.3760/cma.j.issn.1007-3418.2010.05.011
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0354
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P355
**Short title:** Expression of B Cell-Specific Moloney Murine Leukemia Virus Integration Site...
**Full title:** Expression of B Cell-Specific Moloney Murine Leukemia Virus Integration Site 1 (BMI-1) and WW Domain-Containing Oxidoreductase (WWOX) in Liver Cancer Tissue and Normal Liver Tissue
**Authors:** Yu et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Med Sci Monit
**Identifier:** PMID 30242144 / PMC6166521 / DOI 10.12659/MSM.909675
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0355
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P356
**Short title:** West syndrome, developmental and epileptic encephalopathy, and severe CNS dis...
**Full title:** West syndrome, developmental and epileptic encephalopathy, and severe CNS disorder associated with WWOX mutations
**Authors:** Shaukat et al.
**Year:** 2018
**Source type:** Case Reports
**Journal/source:** Epileptic Disord
**Identifier:** PMID 30361190 / DOI 10.1684/epd.2018.1005
**Tier (FASE 1):** A
**Status:** promoted — see [[paper_registry_current#PAPER 045]] (BATCH_20260710_A); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0356
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Role:** priority full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P357
**Short title:** Transforming growth factor beta1 signaling via interaction with cell surface...
**Full title:** Transforming growth factor beta1 signaling via interaction with cell surface Hyal-2 and recruitment of WWOX/WOX1
**Authors:** Hsu et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** J Biol Chem
**Identifier:** PMID 19366691 / PMC2708898 / DOI 10.1074/jbc.M806688200
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0357
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P358
**Short title:** Drosophila orthologue of WWOX, the chromosomal fragile site FRA16D tumour sup...
**Full title:** Drosophila orthologue of WWOX, the chromosomal fragile site FRA16D tumour suppressor gene, functions in aerobic metabolism and regulates reactive oxygen species
**Authors:** O'Keefe et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Hum Mol Genet
**Identifier:** PMID 21075834 / PMC3016910 / DOI 10.1093/hmg/ddq495
**Tier (FASE 1):** C
**Status:** promoted — see [[paper_registry_current#PAPER 071]] (`BATCH_20260815_001`)
**LIT link:** LIT-0358
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** Drosophila
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P359
**Short title:** The supposed tumor suppressor gene WWOX is mutated in an early lethal microce...
**Full title:** The supposed tumor suppressor gene WWOX is mutated in an early lethal microcephaly syndrome with epilepsy, growth retardation and retinal degeneration
**Authors:** Abdel-Salam et al.
**Year:** 2014
**Source type:** Case Reports
**Journal/source:** Orphanet J Rare Dis
**Identifier:** PMID 24456803 / PMC3918143 / DOI 10.1186/1750-1172-9-12
**Tier (FASE 1):** A
**Status:** promoted — see [[paper_registry_current#PAPER 043]] (BATCH_20260710_B); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0359
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE-HIGH
**Claim links:** none — triage only
**Role:** priority full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P360
**Short title:** Identification of IGF1, SLC4A4, WWOX, and SFMBT1 as hypertension susceptibili...
**Full title:** Identification of IGF1, SLC4A4, WWOX, and SFMBT1 as hypertension susceptibility genes in Han Chinese with a genome-wide gene-based association study
**Authors:** Yang et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** PLoS One
**Identifier:** PMID 22479346 / PMC3315540 / DOI 10.1371/journal.pone.0032907
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0360
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P361
**Short title:** Effect of the WWOX gene on the regulation of the cell cycle and apoptosis in...
**Full title:** Effect of the WWOX gene on the regulation of the cell cycle and apoptosis in human ovarian cancer stem cells
**Authors:** Yan et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Mol Med Rep
**Identifier:** PMID 25891642 / PMC4464321 / DOI 10.3892/mmr.2015.3640
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0361
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P362
**Short title:** A novel whole exon deletion in WWOX gene causes early epilepsy, intellectual...
**Full title:** A novel whole exon deletion in WWOX gene causes early epilepsy, intellectual disability and optic atrophy
**Authors:** Ben-Salem et al.
**Year:** 2015
**Source type:** Case Reports
**Journal/source:** J Mol Neurosci
**Identifier:** PMID 25403906 / DOI 10.1007/s12031-014-0463-8
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0362
**Primary pathway:** clinical spectrum / SCAR12
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P363
**Short title:** A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with...
**Full title:** A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with lethal dwarfism and epilepsy
**Authors:** Suzuki et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Genes Brain Behav
**Identifier:** PMID 19500159 / DOI 10.1111/j.1601-183X.2009.00502.x
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0363
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** rat
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.
**Resolved (BATCH_20260806_002):** promoted to [[paper_registry_current#PAPER 058]] after the complete full-text read (`FTR-20260806-19500159-01`). This placeholder is preserved append-only as triage lineage; the integrated record is authoritative. Its triage `Primary pathway: P5 — metabolism` was wrong: the paper's primary axis is **P2, excitability and epileptogenesis**.

## CORPUS P364
**Short title:** Reversing effect of exogenous WWOX gene expression on malignant phenotype of...
**Full title:** Reversing effect of exogenous WWOX gene expression on malignant phenotype of primary cultured lung carcinoma cells
**Authors:** Zhou et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** Chin Med J (Engl)
**Identifier:** PMID 20367991
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0364
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P365
**Short title:** Modeling genetic epileptic encephalopathies using brain organoids
**Full title:** Modeling genetic epileptic encephalopathies using brain organoids
**Authors:** Steinberg et al.
**Year:** 2021
**Source type:** Article
**Journal/source:** EMBO Mol Med
**Identifier:** PMID 34268881 / PMC8350905 / DOI 10.15252/emmm.202013610
**Tier (FASE 1):** A
**Status:** promoted — see [[paper_registry_current#PAPER 039]] (BATCH_20260710_A); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0365
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human organoid
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Role:** priority full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P366
**Short title:** Methylation status of WWOX gene promoter CpG islands in epithelial ovarian ca...
**Full title:** Methylation status of WWOX gene promoter CpG islands in epithelial ovarian cancer and its clinical significance
**Authors:** Yan et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Biomed Rep
**Identifier:** PMID 24648952 / PMC3917087 / DOI 10.3892/br.2013.86
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0366
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P367
**Short title:** Characterization of the tumor suppressor gene WWOX in primary human oral squa...
**Full title:** Characterization of the tumor suppressor gene WWOX in primary human oral squamous cell carcinomas
**Authors:** Pimenta FJ, Gomes DA, Perdigão PF, Barbosa AA, Romano-Silva MA, Gomez MV, Aldaz CM, De Marco L, Gomez RS (9 authors, esummary). 🔴 Two later papers of this group spell the third author `Perdigao` and the fifth `Romano-Silva MV`; esummary and this article give **`Perdigão PF`** and **`Romano-Silva MA`**
**Year:** 2006
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 16152610 / PMC4145845 / DOI 10.1002/ijc.21446
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-16152610-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID16152610.json`, dossier `fulltext_dossiers/PMID16152610.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260926_ALDAZ_R2` (`CC-20260914-16152610-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0367
**Primary pathway:** oncology / tumor suppressor biology — espressione e trascritti aberranti. 🔴 **Corrected from `P6 — DDR / genome stability`**: this paper performs no DNA-damage assay of any kind (no irradiation, adduct, repair, checkpoint or γH2AX); it is RT-PCR, sequencing, western and IHC on 20 tumours
**Model/species:** tessuto umano adulto: **20 carcinomi orali a cellule squamose consecutivi in fumatori** (un ospedale, ago 2003 - giu 2004) + mucosa orale normale da volontari appaiati (numero assente dal corpo del testo; l'abstract dice 10). Nessuna linea cellulare, nessun animale, nessun allele germinale, **nessun materiale neurale**
**Genotype/model:** WWOX somatico, inclusa una missense somatica S329F; nessun allele WWOX-DEE
**Transferability:** **T3**
**clinical relevance:** **LOW** — unchanged
**Claim links:** none — nessuna claim poggia su questo lavoro e questa lettura non ne crea una
**Role:** Serie descrittiva: trascritti WWOX aberranti o assenti in **7/20** tumori (perdita esoni 6-8 in #CA2, #CA5, #CA21, #CA24; perdita esone 7 in #CA2; perdita parziale esoni 8-9 in #CA12), proteina ridotta all'IHC in **8/20**, e **una nuova mutazione somatica missense S329F** (esone 8, dominio SDR, wild type nel sangue, assente in 30 DNA germinali). Nessun esperimento funzionale — S329F non va promossa in alcuna interpretazione di varianti germinali (`CLAIM 030`/`CLAIM 033`). **Fonte del pattern di marcatura (citoplasmatico) dell'antisiero Aldaz in un terzo epitelio**
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. *(2026-09-26: no longer true for reading depth — this paper has since been read in full; see `Evidence depth`. Triage status unchanged.)*
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-16152610-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Reading note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** Manoscritto d'autore, non versione di record (Europe PMC `fullTextXML` 404; efetch rifiuta l'XML; pagina PMC 200 senza User-Agent; PDF dietro proof-of-work). **Difetti interni misurati in questa lettura, da riverificare sulla versione di record:** la legenda della Fig. 1a assegna **#CA12 alla classe Z** (delezione esoni 6-8) mentre i Risultati gli assegnano una perdita parziale 8-9 — **i pixel nativi danno ragione ai Risultati**, perché la corsia #CA12 non ha banda al livello Z; il conteggio degli esoni persi nell'abstract non coincide con i Risultati (tre tumori Δ6-8 contro quattro); il western mostra **10 dei 20** tumori senza che la legenda dica "rappresentativo", e vi si vede una **banda debole a 46 kDa in #CA3**, tumore in cui la RT-PCR non trova alcun trascritto; la soglia +3 è `>50%` nei Metodi e `>51%` nella nota di Tabella II; `C329T` confonde numerazione di codone e nucleotide. **Nessun test statistico compare nel paper.** Specificità dell'antisiero **importata** dal rif. 21 (PMID 14526170, `PAPER 101`); la pre-adsorbimento con proteina GST è riferita senza dire se eseguita qui o nel rif. 21. 🔴 **Un negativo che non si può leggere come lo leggono gli autori:** la Discussione afferma *"evidence that the aberrant transcripts are not translated into protein"*, ma l'epitopo dell'antisiero (residui 12-94) è **conservato** da un prodotto Δ6-8, la striscia porta un solo marcatore a 46 kDa e **nessuna scala di peso molecolare**, e metà della coorte non è mostrata — un western che non mostra un prodotto troncato non è evidenza di non-traduzione se finestra di taglia ed epitopo non sono stabiliti (INFERENZA del lettore, cautela di metodo riusabile). *(The triage `Note` and the R1 `Registration note` above are superseded for every field this batch writes; their text is kept as history.)*

## CORPUS P368
**Short title:** Aberrant gene promoter methylation of p16, FHIT, CRBP1, WWOX, and DLC-1 in Ep...
**Full title:** Aberrant gene promoter methylation of p16, FHIT, CRBP1, WWOX, and DLC-1 in Epstein-Barr virus-associated gastric carcinomas
**Authors:** He et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Med Oncol
**Identifier:** PMID 25720522 / DOI 10.1007/s12032-015-0525-y
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0368
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P369
**Short title:** Versatile communication strategies among tandem WW domain repeats
**Full title:** Versatile communication strategies among tandem WW domain repeats
**Authors:** Dodson et al.
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25710931 / PMC4436281 / DOI 10.1177/1535370214566558
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0369
**Primary pathway:** animal model — pathway variable
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P370
**Short title:** Activated tyrosine kinase Ack1 promotes prostate tumorigenesis: role of Ack1...
**Full title:** Activated tyrosine kinase Ack1 promotes prostate tumorigenesis: role of Ack1 in polyubiquitination of tumor suppressor Wwox
**Authors:** Mahajan et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 16288044 / DOI 10.1158/0008-5472.CAN-05-1127
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0370
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P371
**Short title:** Fragile genes as biomarkers: epigenetic control of WWOX and FHIT in lung, bre...
**Full title:** Fragile genes as biomarkers: epigenetic control of WWOX and FHIT in lung, breast and bladder cancer
**Authors:** Iliopoulos et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Oncogene
**Identifier:** PMID 15674328 / DOI 10.1038/sj.onc.1208398
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0371
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P372
**Short title:** Zfra Inhibits the TRAPPC6AΔ-Initiated Pathway of Neurodegeneration
**Full title:** Zfra Inhibits the TRAPPC6AΔ-Initiated Pathway of Neurodegeneration
**Authors:** Lin et al.
**Year:** 2022
**Source type:** Article
**Journal/source:** Int J Mol Sci
**Identifier:** PMID 36498839 / PMC9739312 / DOI 10.3390/ijms232314510
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0372
**Primary pathway:** P9 — immune / glia / inflammation
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P373
**Short title:** WWOX protein expression varies among RCC histotypes and downregulation of WWO...
**Full title:** WWOX protein expression varies among RCC histotypes and downregulation of WWOX protein correlates with less-favorable prognosis in clear RCC
**Authors:** Lin et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Ann Surg Oncol
**Identifier:** PMID 22555346 / DOI 10.1245/s10434-012-2371-x
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0373
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P374
**Short title:** Common chromosomal fragile site FRA16D tumor suppressor WWOX gene expression...
**Full title:** Common chromosomal fragile site FRA16D tumor suppressor WWOX gene expression and metabolic reprograming in cells
**Authors:** Dayan et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Genes Chromosomes Cancer
**Identifier:** PMID 23765596 / DOI 10.1002/gcc.22078
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0374
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P375
**Short title:** Genetic association study identifies a functional CNV in the WWOX gene contri...
**Full title:** Genetic association study identifies a functional CNV in the WWOX gene contributes to the risk of intracranial aneurysms
**Authors:** Fan et al.
**Year:** 2016
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 26910372 / PMC4941300 / DOI 10.18632/oncotarget.7546
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0375
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P376
**Short title:** Structural insights into the functional versatility of WW domain-containing o...
**Full title:** Structural insights into the functional versatility of WW domain-containing oxidoreductase tumor suppressor
**Authors:** Amjad Farooq
**Year:** 2015
**Source type:** Review
**Journal/source:** Exp Biol Med (Maywood)
**Identifier:** PMID 25662954 / PMC4374002 / DOI 10.1177/1535370214561586
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0376
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P377
**Short title:** Large common fragile site genes and cancer
**Full title:** Large common fragile site genes and cancer
**Authors:** Smith et al.
**Year:** 2007
**Source type:** Review
**Journal/source:** Semin Cancer Biol
**Identifier:** PMID 17140807 / DOI 10.1016/j.semcancer.2006.10.003
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0377
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P378
**Short title:** Stewart 2014 — decitabina e IHC di FHIT/WWOX/FUS1/PTEN in biopsie appaiate: WWOX sale come **trend non significativo** (P = 0.0547)
**Full title:** Impact of decitabine on immunohistochemistry expression of the putative tumor suppressor genes FHIT, WWOX, FUS1 and PTEN in clinical tumor samples
**Authors:** Stewart DJ, Nunez MI, Jelinek J, Hong D, Gupta S, **Aldaz M**, Issa JP, Kurzrock R, Wistuba II (9 authors, artefact `contrib-group`, **initials as printed**). The sixth byline is preserved as printed; its identity is not in doubt — the `contrib-group` gives given name *Marcelo* with affiliation *UT MD Anderson Cancer Center, Smithville, TX*, the campus where the same artefact family prints *"Aldaz C Marcelo"* (`Aldaz CM`)
**Year:** 2014
**Source type:** primary research — analisi correlativa IHC su biopsie appaiate dentro uno studio di fase I
**Journal/source:** *Clin Epigenetics* 2014;6(1):13
**Identifier:** PMID 25024751 / PMC4094901 / DOI 10.1186/1868-7083-6-13
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-25024751-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID25024751.json`, dossier `fulltext_dossiers/PMID25024751.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260926_ALDAZ_R2` (`CC-20260914-25024751-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0378
**Primary pathway:** epigenetica / riespressione farmacologica — 🔴 **corrected from `P6 — DDR / genome stability`**: no DDR or genome-stability endpoint exists in the paper
**Model/species:** **umano** — tumori solidi e linfomi refrattari, tessuto bioptico appaiato (pre-trattamento e giorno 12 del ciclo 1). Nessun animale, nessuna linea cellulare, **nessun materiale neurale, nessun bambino**
**Genotype/model:** WWOX wild-type somatico; **nessun allele germinale, nessun allele WWOX-DEE**
**Transferability:** **T3**
**clinical relevance:** **LOW** (unchanged) — e **nessuna implicazione terapeutica** per il genotipo di riferimento: un de-repressore trascrizionale può contare solo dove un allele funzionale è presente ma sotto-espresso, e questo lavoro misura tessuto tumorale somatico adulto con WWOX wild-type
**Claim links:** none — the reading proposes none
**Role:** background corpus, **letto**: l'unica misura umana *in vivo* appaiata di proteina WWOX sotto un inibitore farmacologico delle DNA-metiltransferasi che questa lettura abbia trovato (`WWOX AND decitabine` = **6** record in PubMed, 2026-09-14)
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. *(2026-09-26: no longer true for reading depth — this paper has since been read in full; see `Evidence depth`. Triage status unchanged.)*
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-25024751-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Reading note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** ⚠️ Il risultato WWOX è un **trend non significativo**: mediana 30 → 100 con **P = 0.0547** su 17 pazienti a punteggio basale ≤ 150 (7 aumenti, 8 invariati, 2 diminuzioni). La **Tabella 2 stampa `0.05`** dove testo e figura danno 0.0547 — un arrotondamento che si legge come significatività; la Figura 1 lo chiama *"strong trend"* (la Figura 1 è grafica vettoriale: i marcatori sono stati contati dai comandi di disegno del PDF, 17 e 17). Il **meccanismo dichiarato non è misurato**: gli autori stessi affermano che la metilazione promotore-specifica non è stata saggiata, e il surrogato globale LINE-1 **non correla** né col punteggio (n = 44, r = 0.09, P = 0.57) né con la sua variazione (n = 19, r = −0.04, P = 0.87). Il **P = 0.0002 aggregato** su FHIT+WWOX+FUS1 mescola osservazioni **non indipendenti** da al più 25 pazienti ed è trascinato da FHIT (8/8, P = 0.014). Dosi e schedule **accorpate** in ogni analisi; **un solo** patologo, nessuna cecità dichiarata; nessun braccio di controllo; anticorpo WWOX **Abcam commerciale 1:100 senza catalogo né clone** — non il policlonale del gruppo Aldaz usato negli altri lavori di questo lotto. Nessuna associazione fra aumento di espressione e risposta tumorale (P = 0.25). Kept as a CORPUS record: the candidate proposed promotion; this batch completes the record in place. *(The triage `Note` and the R1 `Registration note` above are superseded for every field this batch writes; their text is kept as history.)*

## CORPUS P379
**Short title:** MicroRNA-153 promotes Wnt/β-catenin activation in hepatocellular carcinoma th...
**Full title:** MicroRNA-153 promotes Wnt/β-catenin activation in hepatocellular carcinoma through suppression of WWOX
**Authors:** Hua et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Oncotarget
**Identifier:** PMID 25708809 / PMC4414157 / DOI 10.18632/oncotarget.2927
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0379
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P380
**Short title:** Gene mapping and expression analysis of 16q loss of heterozygosity identifies...
**Full title:** Gene mapping and expression analysis of 16q loss of heterozygosity identifies WWOX and CYLD as being important in determining clinical outcome in multiple myeloma
**Authors:** Jenner et al.
**Year:** 2007
**Source type:** Multicenter Study
**Journal/source:** Blood
**Identifier:** PMID 17609426 / DOI 10.1182/blood-2007-02-075069
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0380
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P381
**Short title:** Association study of a functional copy number variation in the WWOX gene with...
**Full title:** Association study of a functional copy number variation in the WWOX gene with risk of gliomas among Chinese people
**Authors:** Yu et al.
**Year:** 2014
**Source type:** Randomized Controlled Trial
**Journal/source:** Int J Cancer
**Identifier:** PMID 24585490 / DOI 10.1002/ijc.28815
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0381
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P382
**Short title:** Frequent PVT1 rearrangement and novel chimeric genes PVT1-NBEA and PVT1-WWOX...
**Full title:** Frequent PVT1 rearrangement and novel chimeric genes PVT1-NBEA and PVT1-WWOX occur in multiple myeloma with 8q24 abnormality
**Authors:** Nagoshi et al.
**Year:** 2012
**Source type:** Article
**Journal/source:** Cancer Res
**Identifier:** PMID 22869583 / DOI 10.1158/0008-5472.CAN-12-0213
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0382
**Primary pathway:** unassigned — triage only
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P383
**Short title:** A novel missense variant in the SDR domain of the WWOX gene leads to complete...
**Full title:** A novel missense variant in the SDR domain of the WWOX gene leads to complete loss of WWOX protein with early-onset epileptic encephalopathy and severe developmental delay
**Authors:** Johannsen et al.
**Year:** 2018
**Source type:** Case Reports
**Journal/source:** Neurogenetics
**Identifier:** PMID 29808465 / DOI 10.1007/s10048-018-0549-5
**Tier (FASE 1):** A
**Status:** promoted — see [[paper_registry_current#PAPER 041]] (BATCH_20260710_A); placeholder kept as audit trail, do not duplicate
**LIT link:** LIT-0383
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** HIGH
**Claim links:** none — triage only
**Role:** priority full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P384
**Short title:** A functional copy number variation in the WWOX gene is associated with lung c...
**Full title:** A functional copy number variation in the WWOX gene is associated with lung cancer risk in Chinese
**Authors:** Yang et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Hum Mol Genet
**Identifier:** PMID 23339925 / DOI 10.1093/hmg/ddt019
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0384
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P385
**Short title:** Expression of common chromosomal fragile site genes, WWOX/FRA16D and FHIT/FRA...
**Full title:** Expression of common chromosomal fragile site genes, WWOX/FRA16D and FHIT/FRA3B is downregulated by exposure to environmental carcinogens, UV, and BPDE but not by IR
**Authors:** Thavathiru E, Ludes-Meyers JH, MacLeod MC, Aldaz CM (4 authors, esummary)
**Year:** 2005
**Source type:** Article
**Journal/source:** Mol Carcinog
**Identifier:** PMID 16187332 / PMC4166602 / DOI 10.1002/mc.20122
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-16187332-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID16187332.json`, dossier `fulltext_dossiers/PMID16187332.md`.
**Tier (FASE 1):** C
**Status:** read — corpus record completed in place by `BATCH_20260926_ALDAZ_R2` (`CC-20260914-16187332-01`), **not promoted to a PAPER record**; see `Evidence depth`
**LIT link:** LIT-0385
**Primary pathway:** P6 — DDR / genome stability — **unchanged and correct**, the only record of this Tier-C lot for which it is. Precisazione: il paper misura **l'espressione di WWOX dopo danno al DNA**, non il ruolo di WWOX nella risposta al danno
**Model/species:** **due sole linee trasformate**: MCF-7 (p53 wild type) e Saos-2 (p53-null). Nessuna cellula primaria, nessun tessuto, nessun animale, nessun allele WWOX, **nessun materiale neurale**
**Genotype/model:** WWOX wild-type; nessun allele WWOX-DEE
**Transferability:** **T3**
**clinical relevance:** **LOW** — unchanged; il valore è metodologico e di riconciliazione, non clinico
**Claim links:** none — 🔴 and deliberately so: this reading does **not** touch `CLAIM 029`, which concerns WWOX's contribution to DNA-damage-response competence; this paper measures the converse direction (WWOX expression after damage) and no ATM, γH2AX, relocalisation or repair endpoint
**Role:** **Fonte primaria di uno dei due lati del conflitto direzionale UV registrato in `fulltext_dossiers/PMID20146584.md` § 3 [ref corrected 2026-09-28 from “§ 3.2” · CC-20260928-SECTION-REFS-01].** In MCF-7, UV-C 254 nm (10 J/m²) e BPDE (0.5 µM) riducono l'mRNA di WWOX e FHIT a 24 h mentre IR 10 Gy **non lo riduce**, con p21 indotto da tutti e tre; l'effetto persiste in Saos-2 p53-null; la **proteina** WWOX cala solo dopo irradiazioni ripetute (48 h 2×, 72 h 3×). Caffeina abolisce il ritardo in fase S e recupera parte del segnale. 🔴 **Il conflitto non è aggiudicato in nessuna direzione:** i due lati non stanno sullo stesso asse — qui mRNA a 24 h (e la caduta è **transitoria**: trascritti ricomparsi a 48 h, *data not shown*), là un'induzione *"immediately"* su dati non pubblicati; nessun punto temporale immediato è misurato qui. L'altra metà della coppia rif. [69]/[70], PMID 15798093, resta non letta. La persistenza della proteina oltre la perdita del trascritto non è un'emivita e non va citata accanto all'endpoint Q230P di `CLAIM 019`
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. *(2026-09-26: no longer true for reading depth — this paper has since been read in full; see `Evidence depth`. Triage status unchanged.)*
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-16187332-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Reading note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** Manoscritto d'autore (Europe PMC `fullTextXML` 404; efetch rifiuta l'XML; **la pagina PMC ha restituito HTTP 200 con un interstiziale reCAPTCHA di 21315 B** e l'articolo solo al secondo tentativo; PDF via proof-of-work). **Limiti misurati nei pixel nativi, che vincolano la portata del risultato:** il GAPDH è **visibilmente più debole nella corsia 15 J/m²** e più chiaro in quella BPDE, quindi solo il risultato a **10 J/m²** e il confronto con IR sono netti dal punto di vista del carico; nella corsia BPDE la banda WWOX è **ridotta ma chiaramente presente**, non abolita, mentre il testo dice *"dramatic decrease"*; il testo cita **1B e 1C invertiti** rispetto agli assi dei pannelli e alla legenda; **non esiste alcun braccio con caffeina senza UV**, né in citofluorimetria né al Northern, e la caffeina porta la frazione S **sotto** il controllo non irradiato mentre il G1 sale sopra; la corsia caffeina 10 mM ha GAPDH più carico; **nulla nel paper è quantificato** (nessuna densitometria, nessun test statistico, nessun blot replicato); sei risultati sono *"data not shown"*. La Discussione propone ATR-vs-ATM e poi **argomenta contro il proprio ramo ATR-Chk1** sul risultato della caffeina. *(The triage `Note` and the R1 `Registration note` above are superseded for every field this batch writes; their text is kept as history.)*

## CORPUS P386
**Short title:** Cigarette smoking extract causes hypermethylation and inactivation of WWOX ge...
**Full title:** Cigarette smoking extract causes hypermethylation and inactivation of WWOX gene in T-24 human bladder cancer cells
**Authors:** Yang et al.
**Year:** 2012
**Source type:** Comparative Study
**Journal/source:** Neoplasma
**Identifier:** PMID 22248280 / DOI 10.4149/neo_2012_028
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0386
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P387
**Short title:** Cloning of WWOX gene and its growth-inhibiting effects on ovarian cancer cells
**Full title:** Cloning of WWOX gene and its growth-inhibiting effects on ovarian cancer cells
**Authors:** Xiong et al.
**Year:** 2010
**Source type:** Article
**Journal/source:** J Huazhong Univ Sci Technolog Med Sci
**Identifier:** PMID 20556583 / DOI 10.1007/s11596-010-0358-z
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0387
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P388
**Short title:** Components of DNA damage checkpoint pathway regulate UV exposure-dependent al...
**Full title:** Components of DNA damage checkpoint pathway regulate UV exposure-dependent alterations of gene expression of FHIT and WWOX at chromosome fragile sites
**Authors:** Ishii et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Mol Cancer Res
**Identifier:** PMID 15798093 / DOI 10.1158/1541-7786.MCR-04-0209
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0388
**Primary pathway:** clinical spectrum / SCAR12
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P389
**Short title:** Common fragile genes and digestive tract cancers
**Full title:** Common fragile genes and digestive tract cancers
**Authors:** Kuroki et al.
**Year:** 2006
**Source type:** Review
**Journal/source:** Surg Today
**Identifier:** PMID 16378185 / DOI 10.1007/s00595-005-3094-4
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0389
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P390
**Short title:** Common chromosomal fragile sites and cancer: focus on FRA16D
**Full title:** Common chromosomal fragile sites and cancer: focus on FRA16D
**Authors:** O'Keefe et al.
**Year:** 2006
**Source type:** Review
**Journal/source:** Cancer Lett
**Identifier:** PMID 16242840 / DOI 10.1016/j.canlet.2005.07.041
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0390
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P391
**Short title:** Expression of fragile histidine triad (FHIT) and WW-domain oxidoreductase gen...
**Full title:** Expression of fragile histidine triad (FHIT) and WW-domain oxidoreductase gene (WWOX) in nasopharyngeal carcinoma
**Authors:** Chen et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Asian Pac J Cancer Prev
**Identifier:** PMID 23534718 / DOI 10.7314/apjcp.2013.14.1.165
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0391
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P392
**Short title:** Inhibition of miR-24 suppresses malignancy of human non-small cell lung cance...
**Full title:** Inhibition of miR-24 suppresses malignancy of human non-small cell lung cancer cells by targeting WWOX in vitro and in vivo
**Authors:** Wang et al.
**Year:** 2018
**Source type:** Article
**Journal/source:** Thorac Cancer
**Identifier:** PMID 30307120 / PMC6275841 / DOI 10.1111/1759-7714.12824
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0392
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P393
**Short title:** WW domain-binding protein 2: an adaptor protein closely linked to the develop...
**Full title:** WW domain-binding protein 2: an adaptor protein closely linked to the development of breast cancer
**Authors:** Chen et al.
**Year:** 2017
**Source type:** Review
**Journal/source:** Mol Cancer
**Identifier:** PMID 28724435 / PMC5518133 / DOI 10.1186/s12943-017-0693-9
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0393
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P394
**Short title:** Bone metastatic process of breast cancer involves methylation state affecting...
**Full title:** Bone metastatic process of breast cancer involves methylation state affecting E-cadherin expression through TAZ and WWOX nuclear effectors
**Authors:** Matteucci et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Eur J Cancer
**Identifier:** PMID 22717556 / DOI 10.1016/j.ejca.2012.05.006
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0394
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** mouse
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P395
**Short title:** A cascade of protein aggregation bombards mitochondria for neurodegeneration...
**Full title:** A cascade of protein aggregation bombards mitochondria for neurodegeneration and apoptosis under WWOX deficiency
**Authors:** Sze et al.
**Year:** 2015
**Source type:** Article
**Journal/source:** Cell Death Dis
**Identifier:** PMID 26355344 / PMC4650446 / DOI 10.1038/cddis.2015.251
**Tier (FASE 1):** B
**Status:** screened — corpus placeholder
**LIT link:** LIT-0395
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P396
**Short title:** Hypoxia inducible factor-1 is activated by transcriptional co-activator with...
**Full title:** Hypoxia inducible factor-1 is activated by transcriptional co-activator with PDZ-binding motif (TAZ) versus WWdomain-containing oxidoreductase (WWOX) in hypoxic microenvironment of bone metastasis from breast cancer
**Authors:** Bendinelli et al.
**Year:** 2013
**Source type:** Article
**Journal/source:** Eur J Cancer
**Identifier:** PMID 23566416 / DOI 10.1016/j.ejca.2013.03.002
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0396
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P397
**Short title:** Editorial: WW Domain Proteins in Signaling, Cancer Growth, Neural Diseases, a...
**Full title:** Editorial: WW Domain Proteins in Signaling, Cancer Growth, Neural Diseases, and Metabolic Disorders
**Authors:** Chang et al.
**Year:** 2019
**Source type:** Editorial
**Journal/source:** Front Oncol
**Identifier:** PMID 31428585 / PMC6688159 / DOI 10.3389/fonc.2019.00719
**Tier (FASE 1):** C
**Status:** read — corpus placeholder, not promoted (`CC-20260914-PLACEHOLDER-READS-01`, `BATCH_20260926_ALDAZ_R2`); see `Evidence depth`
**Evidence depth:** complete_fulltext_read — `FTR-20260909-31428585-02`; manifest `deepdive_manifests/PMID31428585.json` (20 locators, schema v2, strict PASS, 0 gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
**LIT link:** LIT-0397
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P398
**Short title:** Evidences that the polymorphism Pro-282-Ala within the tumor suppressor gene...
**Full title:** Evidences that the polymorphism Pro-282-Ala within the tumor suppressor gene WWOX is a new risk factor for differentiated thyroid carcinoma
**Authors:** Cancemi et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 21520031 / DOI 10.1002/ijc.25937
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0398
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** Drosophila
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P399
**Short title:** Deletion and mutation of WWOX exons 6-8 in human non-small cell lung cancer
**Full title:** Deletion and mutation of WWOX exons 6-8 in human non-small cell lung cancer
**Authors:** Zhou et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** J Huazhong Univ Sci Technolog Med Sci
**Identifier:** PMID 16116962 / DOI 10.1007/BF02873566
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0399
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P400
**Short title:** Fragile histidine triad protein, WW domain-containing oxidoreductase protein...
**Full title:** Fragile histidine triad protein, WW domain-containing oxidoreductase protein Wwox, and activator protein 2gamma expression levels correlate with basal phenotype in breast cancer
**Authors:** Guler et al.
**Year:** 2009
**Source type:** Article
**Journal/source:** Cancer
**Identifier:** PMID 19130459 / PMC2640223 / DOI 10.1002/cncr.24103
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0400
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

---

## CORPUS P401
**Short title:** Aeran 2025 Mol Ther — neuron-targeted gene therapy in STXBP1-related disorders, with promoter-resolved cell-type coverage and a primate arm
**Full title:** Neuron-targeted gene therapy rescues multiple phenotypes of STXBP1-related disorders
**Authors:** Aeran R, et al.
**Year:** 2025
**Source type:** primary research — preclinical gene replacement, mouse and nonhuman primate
**Journal/source:** *Mol Ther* 2025
**Identifier:** PMID 40349107 / DOI 10.1016/j.ymthe.2025.05.011
**Tier (FASE 1):** C
**Status:** processed
**Record provenance:** created by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01` (intake wave 3 2026-10-03, Scientist C), which described the records in a table and did not write them
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-40349107-01` (figure panels not rendered; supplement not fetched); manifest `deepdive_manifests/PMID40349107.json`
**LIT link:** [[literature_tracking_log_current#LIT-0471]]
**Primary pathway:** P7 — delivery and vector engineering
**Model/species:** mouse and nonhuman primate
**Genotype/model:** no WWOX genotype — this source does not mention WWOX
**Transferability:** T4 — promoter-resolved cell-type coverage, dorsal-root-ganglion histopathology and serum neurofilament light transfer as method; doses do not
**clinical relevance:** BACKGROUND — transferable method only
**Claim links:** none
**Role:** transferable-method corpus; **not a WWOX paper**. The strongest off-target-organ-risk contribution of the wave-3 group-C set, and the source of its dose-versus-protein figures. Read with `RL-C-20261003w3`, which carries the audit-narrowed reading of its neurofilament and nerve-conduction numbers.
**Note:** Carried for a transferable lesson from a different gene. The transfer limit is stated in the dossier; no datum from this paper bounds a WWOX claim without that limit restated. Not medical advice.
## CORPUS P402
**Short title:** Chen 2025 J Clin Invest — neonatal but not juvenile gene therapy in an SCN1B Dravet model, and the exposure difference behind it
**Full title:** Neonatal but not juvenile gene therapy reduces seizures and prolongs lifespan in SCN1B-Dravet syndrome mice
**Authors:** Chen C, et al.
**Year:** 2025
**Source type:** primary research — preclinical gene replacement, mouse
**Journal/source:** *J Clin Invest* 2025
**Identifier:** PMID 39847501 / DOI 10.1172/JCI182584
**Tier (FASE 1):** C
**Status:** processed
**Record provenance:** created by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01` (intake wave 3 2026-10-03, Scientist C)
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-39847501-01` (figure panels not rendered; supplement not fetched); manifest `deepdive_manifests/PMID39847501.json`
**LIT link:** [[literature_tracking_log_current#LIT-0472]]
**Primary pathway:** P7 — delivery and timing
**Model/species:** mouse
**Genotype/model:** no WWOX genotype — this source does not mention WWOX
**Transferability:** T4 — interneuron-promoter coverage transfers as method; the age comparison does not transfer as a window result
**clinical relevance:** BACKGROUND — transferable method only
**Claim links:** none
**Role:** transferable-method corpus; **not a WWOX paper**. One of the two results in the wave-3 set that look like a window result and resolve to delivery: the authors attribute the P10 failure to transgene level and distribution and show the restricted expression themselves. Carried in `DIS-033`.
**Note:** Carried for a transferable lesson from a different gene. The transfer limit is stated in the dossier; no datum from this paper bounds a WWOX claim without that limit restated. Not medical advice.
## CORPUS P403
**Short title:** Wagner 2025 Nat Med — antisense oligonucleotide treatment in a preterm infant with early-onset SCN2A developmental and epileptic encephalopathy
**Full title:** Antisense oligonucleotide treatment in a preterm infant with early-onset SCN2A developmental and epileptic encephalopathy
**Authors:** Wagner M, et al.
**Year:** 2025
**Source type:** primary research — single-patient clinical report (article type includes Case Reports)
**Journal/source:** *Nat Med* 2025
**Identifier:** PMID 40263630 / DOI 10.1038/s41591-025-03656-0
**Tier (FASE 1):** C
**Status:** processed
**Record provenance:** created by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01` (intake wave 3 2026-10-03, Scientist C)
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-40263630-01` (figure panels not rendered; supplement not fetched); manifest `deepdive_manifests/PMID40263630.json`
**LIT link:** [[literature_tracking_log_current#LIT-0473]]
**Primary pathway:** P7 — route, schedule and n-of-1 architecture
**Model/species:** human, n = 1
**Genotype/model:** no WWOX genotype — this source does not mention WWOX
**Transferability:** T4 — the n-of-1 architecture and the lumbar intrathecal route transfer; the modality and the allele do not
**clinical relevance:** BACKGROUND — transferable architecture only
**Claim links:** none
**Role:** transferable-architecture corpus; **not a WWOX paper**. ⚠️ Its cumulative-exposure statements do not reconcile with one another across the main text and the extended data (a 30.5 mg total over seven doses, ten further 8 mg doses, and a stated 94 mg total), so no cumulative dose from this report may be carried without naming which statement it came from — a blind-audit finding of `BATCH_20261003_004`.
**Note:** Carried for a transferable lesson from a different gene. The transfer limit is stated in the dossier; no datum from this paper bounds a WWOX claim without that limit restated. Not medical advice.
## CORPUS P404
**Short title:** Diaz 2026 Mol Ther Nucleic Acids — AAV9 targeting of a natural antisense transcript in Dravet syndrome, with a non-monotonic dose-response
**Full title:** AAV9-mediated targeting of natural antisense transcript as a novel treatment for Dravet syndrome
**Authors:** Diaz J, et al.
**Year:** 2026
**Source type:** primary research — preclinical transcript upregulation, mouse
**Journal/source:** *Mol Ther Nucleic Acids* 2026
**Identifier:** PMID 42181696 / DOI 10.1016/j.omtn.2026.102942
**Tier (FASE 1):** C
**Status:** processed
**Record provenance:** created by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01` (intake wave 3 2026-10-03, Scientist C)
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-42181696-01` (figure panels not rendered; supplement not fetched); manifest `deepdive_manifests/PMID42181696.json`
**LIT link:** [[literature_tracking_log_current#LIT-0474]]
**Primary pathway:** P7 — transcript upregulation
**Model/species:** mouse
**Genotype/model:** no WWOX genotype — this source does not mention WWOX
**Transferability:** T4 — the non-monotonic dose-response and the protein-versus-rescue dissociation transfer as warnings, not as values
**clinical relevance:** BACKGROUND — transferable method only
**Claim links:** none
**Role:** transferable-method corpus; **not a WWOX paper**. The source of the wave-3 set's load-bearing negative: survival, febrile and spontaneous seizures improved while cortical target protein moved from ~0.45 to ~0.49 of wild type, not significantly. ⚠️ Its overshoot attribution for the top dose is explicitly a hypothesis and is scoped to one vector given intracerebroventricularly, and one of its seizure tables is three animals per arm with no statistical test — both blind-audit findings of `BATCH_20261003_004`. Carried in `RL-C-20261003w3` and `DIS-033`.
**Note:** Carried for a transferable lesson from a different gene. The transfer limit is stated in the dossier; no datum from this paper bounds a WWOX claim without that limit restated. Not medical advice.
## CORPUS P405
**Short title:** Saravanan 2026 Ann Clin Transl Neurol — an endogenous HiBiT knock-in for assaying NaV1.1 protein quantity, as a pharmacodynamic template
**Full title:** Augmenting and Assaying Nav1.1 Protein Quantity for Dravet Syndrome Therapy
**Authors:** Saravanan S, et al.
**Year:** 2026
**Source type:** primary research — assay development in human induced pluripotent stem cells
**Journal/source:** *Ann Clin Transl Neurol* 2026
**Identifier:** PMID 42521212 / DOI 10.1002/acn3.70500
**Tier (FASE 1):** C
**Status:** processed
**Record provenance:** created by `BATCH_20261003_004` from the op specification of `CC-20261003W3-C-REGISTRY-01` (intake wave 3 2026-10-03, Scientist C)
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-42521212-01` (figure captions only; supplement captions only); manifest `deepdive_manifests/PMID42521212.json`
**LIT link:** [[literature_tracking_log_current#LIT-0475]]
**Primary pathway:** P-BIO — pharmacodynamic assay
**Model/species:** human induced pluripotent stem cells
**Genotype/model:** no WWOX genotype — this source does not mention WWOX
**Transferability:** T4 — the reporter architecture transfers as method; nothing WWOX-specific exists (`WWOX AND HiBiT` returned 0 PubMed records, ESearch 2026-10-03)
**clinical relevance:** BACKGROUND — transferable method only
**Claim links:** none
**Role:** transferable-method corpus; **not a WWOX paper**. The named next acquisition of `RC-C-20261003w3`. ⚠️ Its copy-number caveat is clone-specific — a 20q11.21 duplication in one clone and its derivatives, which the authors say *«can confer»* a survival advantage, with a second clone free of it (blind-audit narrowing, `BATCH_20261003_004`).
**Note:** Carried for a transferable lesson from a different gene. The transfer limit is stated in the dossier; no datum from this paper bounds a WWOX claim without that limit restated. Not medical advice.
## CORPUS COVERAGE — 181–220 DEEP-DIVE PAPERS (lint 2026-06-09)
Purpose: restore the paper↔claim audit trail. These corpus IDs (181–220 batch) were deep-dived into CLAIM 021–028 but had no registry record — full PAPER records (001–028) stop at 028, CORPUS-STUB at 179, and CORPUS Pxxx triage starts at 221. Entries below are claim-linked placeholders built from `literature_tracking_log_current.md` (Tracking update — papers 181–220, 2026-04-17). Full bibliographic identifiers (PMID/DOI) PENDING — to be completed on promotion to full PAPER record. Lossless / append-only; no renumbering.

## CORPUS P210
**Topic:** Neocortical network hyperexcitability / oscillatory pathology (neuron-specific Wwox loss)
**Deep-dive level:** deep, high-confidence, partial/full-text-limited
**Claim links:** → CLAIM 021
**Identifier:** PMID 34634460 / PMCID PMC8609180 / DOI 10.1016/j.nbd.2021.105529 — normalized to [[paper_registry_current#PAPER 031]]
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Source description from tracking log 2026-04-17. Normalized in BATCH_20260705_001 to full PAPER record [[paper_registry_current#PAPER 031]]; placeholder retained as audit trail for the 181-220 corpus batch.

## CORPUS P216
**Topic:** Prenatal null-severe onset — human fetal case, homozygous deletion first six exons
**Deep-dive level:** deep, high-confidence, partial-access human case analysis
**Claim links:** → CLAIM 022
**Identifier:** PENDING
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Source description from tracking log 2026-04-17.

## CORPUS P206
**Topic:** WWOX–p73 phosphorylation-dependent routing/scaffold logic
**Deep-dive level:** deep, high-confidence, partial-access mechanistic analysis
**Claim links:** → CLAIM 023
**Identifier:** PMID 15070730 / DOI 10.1073/pnas.0400805101 / PMC384759 — resolved in `BATCH_20260909_001` from the literal string `PENDING`; normalized to [[paper_registry_current#PAPER 081]]
**Status:** promoted — see [[paper_registry_current#PAPER 081]] (BATCH_20260909_001, `CC-20260909-15070730-01`); placeholder **conservato append-only come storia di audit, mai cancellato**
**Note:** Source description from tracking log 2026-04-17. 🔴 **The duplicate hypothesis this record carried is DISPROVED, not merged.** The placeholder read *"likely overlaps PAPER 026 (PMID 32185845); verify before merge"*; the complete read `FTR-20260909-15070730-02` establishes the source as **PMID 15070730**, a different paper, so the two records must NOT be merged. `PAPER 026` remains abstract-only and continues to report the **opposite direction** for the Tyr33 effect (phosphorylation *decreases* affinity for a p73-derived peptide) — a standing tension recorded on both records and deliberately not resolved by this batch, an abstract-only record having no parity with a complete full-text read.

## CORPUS P204
**Topic:** WW1–WW2 tandem cooperativity (WW-domain architecture / variant interpretation)
**Deep-dive level:** deep, high-confidence, partial-access structural analysis
**Claim links:** → CLAIM 024
**Identifier:** PENDING
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Source description from tracking log 2026-04-17.

## CORPUS P191
**Topic:** WWOX/HIF1A axis in human non-tumoral GDM leukocytes (state marker)
**Deep-dive level:** full text deep
**Claim links:** → CLAIM 025
**Identifier:** PENDING
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Source description from tracking log 2026-04-17.

## CORPUS PMID 42082822
**Short title:** Denkboy Ongen 2026 — WWOX p.Ala141Thr in hypospadias / 46,XY DSD
**Full title:** The Role of WWOX Gene Variant in Hypospadias and 46,XY Disorders of Sexual Development
**Authors:** Denkboy Ongen Y, Tezcan-Unlu H, Unal U, Efendi-Erdem E, Cecener G, Eren E
**Year:** 2026
**Source type:** case report with protein and in-silico analysis
**Journal/source:** *Reprod Sci* 2026;33(5):1020–1025
**Identifier:** PMID 42082822 / PMC PMC13230315 / DOI 10.1007/s43032-026-02112-9
**Corpus paper no:** N/A — post-harvest discovery
**Record provenance:** 🔴 **POST-HARVEST, AND THE IDENTIFIER SAYS SO.** This paper was published after the 2026-08-06 corpus harvest, so it holds no corpus-paper number and has no `LIT-0###` entry. `CORPUS P401` would claim a position in a harvest it was never in, and the 31 gaps inside 182–400 are other papers' numbers, so the record is keyed on the identity that is primary, stable and already how every receipt and manifest names a study: the PMID. One convention extended by one form (`growth_anchors.RECORD_PATTERNS`), no second numbering, no allocator, no migration — every historical `CORPUS P###` and `CORPUS-STUB-###` is untouched. Created by `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01` (BATCH_20260920_003).
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only, and this record has no corpus-paper number at all
**Status:** read — post-harvest corpus record, classified CORPUS by the operator on 2026-09-20
**Evidence depth:** complete_fulltext_read — `FTR-20260811-42082822-01`; manifest `deepdive_manifests/PMID42082822.json` (9 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** none on-axis — hypospadias and 46,XY disorders of sexual development
**Model/species:** human — one 7-month-old proband, with family genotyping and Western blot
**Genotype/model:** `p.Ala141Thr`, homozygous in the proband. No WWOX-DEE allele, no neural endpoint, no CNS measurement anywhere in the paper.
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none — this record carries a reading, not a claim
**Role:** 🔴 **A NEGATIVE, AND IT IS THE REASON THE READING IS WORTH KEEPING. THE VARIANT DOES NOT SEGREGATE WITH THE PHENOTYPE**, and the paper's own Results sentence says so: a healthy first-degree relative carries the IDENTICAL HOMOZYGOUS genotype, with Western blot showing WWOX protein reduced in that relative as much as in the proband. Reduced protein is therefore shown NOT to be sufficient for the reported phenotype in this family. Recorded as a boundary on any inference that reads a WWOX missense plus reduced protein as explanatory on its own.
**LIT link:** none — no literature entry exists for this PMID; it postdates the harvest that created that series
**Note:** The in-silico prediction that `p.Ala141Thr` disrupts the protein's secondary structure is the authors' modelling, not a measurement, and is carried as such. The publication gate raises `REVIEW / PARENT_OF_ORIGIN_ATTRIBUTED` on this paper's manifest: the finding is attributed to a published study's own subjects and is not linked to the reference genotype, which is the reviewed and admissible case — read 2026-09-20, no change required.

---

## CORPUS P022
**Short title:** Abdeen & Aqeilan 2019 — WWOX and p53 in aggressive breast cancer
**Full title:** Decoding the link between WWOX and p53 in aggressive breast cancer
**Authors:** Abdeen SK, Aqeilan RI
**Year:** 2019
**Source type:** 🔴 **Review** — and specifically the authors' review of their own primary study. A secondary source; every number is a pointer to its primary.
**Journal/source:** *Cell Cycle* 2019;18(11):1177–1186
**Identifier:** PMID 31075076 / PMC PMC6592247 / DOI 10.1080/15384101.2019.1616998
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only; this record is outside that window and the reading is complete, so a reading-priority label has no verdict to carry here (`BATCH_20260920_002`)
**Status:** read — corpus placeholder resolved into its own corpus record (`CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`, BATCH_20260920_002)
**Evidence depth:** complete_fulltext_read — `FTR-20260811-31075076-02`; manifest `deepdive_manifests/PMID31075076.json` (9 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** none on-axis — BLBC/TNBC oncology, ER signalling, EMT and genomic instability
**Model/species:** human, secondary — BLBC and TNBC cell and tumour biology
**Genotype/model:** no WWOX-DEE allele; breast-cancer tumour suppression
**Transferability:** T3 — no WWOX-DEE allele, no neural endpoint, no CNS measurement anywhere in it.
**clinical relevance:** LOW
**Claim links:** none — this record carries a reading, not a claim
**Role:** **methodological control, and it earns the word.** It FALSIFIES `DL-METH-091`'s generalisation that authors restating their own work state it more firmly: here they hedge three times in two sentences, and label the inference from WWOX to p53 by way of ER signalling speculation themselves.
**LIT link:** [[literature_tracking_log_current#LIT-0049]]
**Note:** The reading also records an asymmetry worth keeping: the modals present in the running text are COMPRESSED in the figure caption and in the schematic, so a reader who takes the drawing for the argument gets a firmer claim than the prose makes.

---

## CORPUS P027
**Short title:** Akkawi 2024 — WWOX/Trp53 osteosarcoma and Myc; the title contradicts the body
**Full title:** WWOX promotes osteosarcoma development via upregulation of Myc
**Authors:** Akkawi R, Hidmi O, Haj-Yahia A, Monin J, Diment J, Drier Y, Stein GS, Aqeilan RI
**Year:** 2024
**Source type:** primary experimental — traceable `Wwox/Trp53` double-knockout mouse, tdTomato reporter, bone-marrow mesenchymal stem cells, Myc ChIP-seq
**Journal/source:** *Cell Death Dis* 2024;15(1):13
**Identifier:** PMID 38182577 / PMC PMC10770339 / DOI 10.1038/s41419-023-06378-8
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only; this record is outside that window and the reading is complete, so a reading-priority label has no verdict to carry here (`BATCH_20260920_002`)
**Status:** read — corpus placeholder resolved into its own corpus record (`CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`, BATCH_20260920_002)
**Evidence depth:** complete_fulltext_read — `FTR-20260810-38182577-02`; manifest `deepdive_manifests/PMID38182577.json` (30 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** P8 — bone / RUNX2 axis
**Model/species:** mouse (Osterix1-Cre; Wwox/Trp53) plus human osteosarcoma tumours
**Genotype/model:** no WWOX-DEE allele; somatic double knockout in bone
**Transferability:** T3 — no WWOX-DEE allele, no neural endpoint.
**clinical relevance:** LOW
**Claim links:** none — this record carries a reading, not a claim
**Role:** 🔴 **THE TITLE ASSERTS THE OPPOSITE OF THE PAPER'S OWN BODY.** The body states plainly that WWOX LOSS RAISES Myc, the figure legend states the inverse correlation, panel H shows it in human tumours, and the abstract says restoring WWOX REDUCED Myc protein levels. The title reads *'WWOX promotes osteosarcoma development via upregulation of Myc'*. This is the same direction measured in liver by PMID 29724996.
**LIT link:** [[literature_tracking_log_current#LIT-0054]]
**Note:** INTEGRITY: this article carries a published erratum, PMID 38355659, recorded as `PAPER 092` — an editorial notice and not a study. An erratum is not an integrity event and this record carries no hold. TWO QUALIFIED PAIRS were DOWNGRADED FROM CONTRADICTION on 2026-08-10 and are kept qualified rather than dropped: the text calls the WWOX add-back a restoration citing Fig 6D, which contains no WWOX re-expression lane, while Fig 6G is the only panel in the article that does; and the text describes Myc as lowly expressed in the p53-only knockout while citing Fig 6A–B, the Venn and the pathway panel. 🔴 NOT A DUPLICATE, AND THE CHECK IS RECORDED BECAUSE THE SUSPICION WAS MINE. `LIT-0054` is this study, PMID 38182577. `LIT-0416` is the ERRATUM, PMID 38355659, which merely NAMES this PMID in its short title — so a substring search over entry bodies returned two entries for one paper. Identity is not mention, which is the distinction `registry_records.py` exists to keep; only `LIT-0054` is linked from here.

---

## CORPUS P113
**Short title:** Bidany-Mizrahi 2024 — WWOX and BRCA1 in DSB repair-pathway choice
**Full title:** Unveiling the relationship between WWOX and BRCA1 in mammary tumorigenicity and in DNA repair pathway selection
**Authors:** Bidany-Mizrahi T, Shweiki A, Maroun K, Abu-Tair L, Mali B, Aqeilan RI
**Year:** 2024
**Source type:** primary experimental — `K14-Cre;Brca1;Wwox` transgenic mouse, human TNBC cell lines, 53BP1 and RAD51 foci
**Journal/source:** *Cell Death Discov* 2024;10(1):145
**Identifier:** PMID 38499540 / PMC PMC10948869 / DOI 10.1038/s41420-024-01878-8
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only; this record is outside that window and the reading is complete, so a reading-priority label has no verdict to carry here (`BATCH_20260920_002`)
**Status:** read — corpus placeholder resolved into its own corpus record (`CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`, BATCH_20260920_002)
**Evidence depth:** complete_fulltext_read — `FTR-20260909-38499540-02`; manifest `deepdive_manifests/PMID38499540.json` (34 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** mouse (K14-Cre; Brca1; Wwox) plus human TNBC cell lines
**Genotype/model:** no WWOX-DEE allele; mammary tumorigenesis
**Transferability:** T3 — no WWOX-DEE allele, no neural endpoint.
**clinical relevance:** LOW
**Claim links:** none — this record carries a reading, not a claim
**Role:** **three caption-versus-panel direction errors, recorded as a reading-fidelity finding.** The paper's model — WWOX presence directs repair to NHEJ, WWOX loss compromises NHEJ and raises HDR — is correct in the body; three figure-caption TITLES state it backwards.
**LIT link:** [[literature_tracking_log_current#LIT-0133]]
**Note:** THE THREE PAIRS, each verified on both sides. Figure 2: the caption says the combined loss redirects repair TO NHEJ; the panel shows losing WWOX dropping the NHEJ marker about four-fold and raising the HDR marker about six-fold. Figure 4: the caption attributes a reduction in HDR to LOSS of WWOX; the experiment is OVEREXPRESSION, labelled EV against WWOX OE, with the caption's own body saying so two lines below its title. Figure 5: the caption attributes an INCREASE in NHEJ to LOSS of WWOX, which is wrong in both directions at once. Nothing measured in the paper is demoted by this; what is recorded is that its captions cannot be cited without the panels.

---

## CORPUS P123
**Short title:** Hazan 2015 commentary — WWOX activates ATM; the primary's hedge is gone
**Full title:** WWOX guards genome stability by activating ATM
**Authors:** Hazan I, Abu-Odeh M, Hofmann TG, Aqeilan RI
**Year:** 2015
**Source type:** 🔴 **Commentary** — a secondary source restating the authors' own primary (PMID 25331887).
**Journal/source:** *Mol Cell Oncol* 2015;2(4):e1008288
**Identifier:** PMID 27308504 / PMC PMC4905350 / DOI 10.1080/23723556.2015.1008288
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only; this record is outside that window and the reading is complete, so a reading-priority label has no verdict to carry here (`BATCH_20260920_002`)
**Status:** read — corpus placeholder resolved into its own corpus record (`CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`, BATCH_20260920_002)
**Evidence depth:** complete_fulltext_read — `FTR-20260810-27308504-01`; manifest `deepdive_manifests/PMID27308504.json` (14 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human and mouse, secondary — FRA16D common fragile site, WWOX–ATM association
**Genotype/model:** no WWOX-DEE allele; DNA-damage response at a common fragile site
**Transferability:** T3 — no WWOX-DEE allele, no neural endpoint.
**clinical relevance:** LOW
**Claim links:** none — this record carries a reading, not a claim
**Role:** **citation-fidelity control, with its own control case recorded first.** Not everything the commentary asserts is inflated: WWOX-dependent ATM monomerisation is a real measurement in the primary.
**LIT link:** [[literature_tracking_log_current#LIT-0142]]
**Note:** 🔴 WHAT CHANGED BETWEEN THE PRIMARY AND ITS OWN COMMENTARY, one year apart. The sentence that maps a laboratory manipulation onto a GENOTYPE is word-for-word identical through 'reduced activation of ATM' — except that the primary writes MIGHT REDUCE and the commentary states it flatly. And the primary captions its Figure 7D model *Hypothetical*; the commentary redraws substantially the same model as its Figure 1 and the word `hypothetic` occurs ZERO times in the entire commentary. The schematic qualifies rather than contradicts the caption: it says something the caption does not say and cannot be read as saying.

---

## CORPUS P182
**Topic:** WWOX interactome / trafficking–metabolism coupling (endomembrane → Acetyl-CoA)
**Deep-dive level:** full text deep
**Claim links:** → CLAIM 026
**Identifier:** PMID 30619736 / PMCID PMC6300487 / DOI 10.3389/fonc.2018.00591 — normalized to [[paper_registry_current#PAPER 032]]
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Source description from tracking log 2026-04-17. Normalized in BATCH_20260705_001 to full PAPER record [[paper_registry_current#PAPER 032]]; placeholder retained as audit trail for the 181-220 corpus batch.

## CORPUS P214
**Topic:** HYAL-2 / WWOX / SMAD4 ECM membrane-to-nucleus signaling
**Deep-dive level:** deep with supporting experimental paper
**Claim links:** → CLAIM 027
**Identifier:** PENDING
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Source description from tracking log 2026-04-17.

## CORPUS P207
**Topic:** Context-dependence support (WWOX output partner/context-dependent)
**Deep-dive level:** deep, high-confidence, partial-access translational analysis
**Claim links:** → CLAIM 028 (tracking-log mapping confirmed; source pointer normalized to 207/218/206/214 by `BATCH_20260725_001`)
**Identifier:** PENDING
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** `BATCH_20260725_001` resolved the historical 213→207 typo by operator-authorized cross-file audit. No P213 record exists; scientific interpretation unchanged.

## CORPUS P218
**Topic:** Quantitative p73-binding support (strengthens context-dependence principle)
**Deep-dive level:** integrated as mechanistic support (v1.7 propagation)
**Claim links:** → CLAIM 028 (refinement support)
**Identifier:** PENDING
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Integrated 2026-04-18 per paper_registry header changelog.

---

## PAPER 039
**Short title:** Steinberg 2021 brain-organoid WOREE model
**Full title:** Modeling genetic epileptic encephalopathies using brain organoids
**Authors:** Steinberg DJ, Repudi S, Saleem A, et al. (Aqeilan lab)
**Year:** 2021
**Source type:** primary — human brain organoid model (hESC KO + patient iPSC)
**Journal/source:** *EMBO Mol Med* 2021;13(8):e13610
**Identifier:** PMID 34268881 / PMCID PMC8350905 / DOI 10.15252/emmm.202013610
**Status:** claim_linked
**Evidence depth:** partial_fulltext_read — `FTR-20260814-34268881-03`; articolo, 11/11 figure e tutti gli otto supplementi depositati letti, ma Appendix Figures S1–S6 sono assenti dal pacchetto ufficiale
**Primary pathway:** P1 — network hyperexcitability / E-I balance
**Secondary pathway:** P5 — metabolism (OXPHOS↓/glycolysis↑); P3 — Wnt; DDR
**Model/species:** human cerebral & forebrain organoids; WiBR3 hESC WWOX-KO; patient iPSC (WSM c.517-2A>G WOREE; WPM G372R SCAR12); W-AAV / lenti-WWOX rescue
**Genotype/model:** KO ≠ the reference genotype (compound het N/M); patient lines include an SDR-domain missense (G372R)
**Transferability:** T2
**clinical relevance:** HIGH — piattaforma umana + il controllo negativo (G372R) necessario a testare il rescue proteostatico
**Claim links:** 002, 030, 032 · 005 (added 2026-10-04 by `BATCH_20261004_001`: `CLAIM 005`'s evidence boundary names this organoid paper as one of the three WWOX rows a third-party review leaves `Unclear` on glial cell autonomy)
**Role:** primary source for CLAIM 002 extension; provides the human bench for HYP-08
**Note:** Promosso in BATCH_20260710_A da [[paper_registry_current#CORPUS P365]]. 🔴 Corretto in `BATCH_20260815_001`: il paper misura marker GABAergici, componenti recettoriali e ipereccitabilità, **non** inversione del cloro, NKCC1/KCC2, risposta al GABA o farmacologia GABA; “GABA depolarizzante” è quindi ipotesi meccanicistica, non dato. Il rescue W-AAV è ubiquitario, sovrafisiologico e parziale. RNA-seq effettivo `n=2 WT` contro `n=4 KO` dopo due esclusioni; EV1/EV2 usa selezione raw-`P<0.01`, distinta dalla significatività aggiustata. La firma OXPHOS/glicolisi è bulk transcriptomics confondibile da maturazione, identità regionale e composizione, non flusso. Cinque simboli corrotti dall'auto-date Excel sono annotati: SEPT7, SEPT5, MARCH7, MARCH2, MARCH8. Le Appendix Figures S1–S6 restano l'unico debito.
**Wikilinks:** [[claim_registry_current#CLAIM 002]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 032]]

---

## PAPER 041
**Short title:** Johannsen 2018 — Q230P: complete loss of WWOX protein
**Full title:** A novel missense variant in the SDR domain of the WWOX gene leads to complete loss of WWOX protein with early-onset epileptic encephalopathy and severe developmental delay
**Authors:** Johannsen J, Kortüm F, Rosenberger G, Bokelmann K, Schirmer MA, Denecke J, Santer R
**Year:** 2018
**Source type:** primary — case report + functional analysis on patient fibroblasts
**Journal/source:** *Neurogenetics* 2018;19(3):151-156
**Identifier:** PMID 29808465 / DOI 10.1007/s10048-018-0549-5 — no PMCID (closed access, Springer)
**Status:** claim_linked
**Evidence depth:** abstract only — full text paywalled (handoff card: files/fulltext/PMID29808465_Johannsen2018.handoff.md). L'abstract è esplicito e quantificato sui due metodi (qRT-PCR + Western blot).
**Primary pathway:** genotype / protein stability / proteostasis
**Secondary pathway:** clinical spectrum WWOX-DEE
**Model/species:** human — fibroblasti di paziente; due sorelle omozigoti (famiglia consanguinea, Afghanistan)
**Genotype/model:** **p.Gln230Pro omozigote** — the missense allele (Q230P), nel dominio SDR
**Transferability:** T1 — variante identica a quella del genotipo di riferimento
**clinical relevance:** VERY HIGH — è l'unico studio funzionale sull'allele missense (Q230P)
**Claim links:** 019, 030, 032
**Role:** fonte funzionale primaria per il meccanismo di Q230P; fonda l'ipotesi di rescue proteostatico
**Note:** Promosso in BATCH_20260710_A da [[paper_registry_current#CORPUS P383]] (Tier A, **clinical relevance HIGH**, `no deep-dive performed` — era a corpus dal 2018 e mai letto; vedi discovery ledger FM-021). **Finding centrale:** in fibroblasti delle pazienti, **qRT-PCR mostra livelli di trascritto WWOX normali** e il **Western blot mostra assenza di proteina WWOX**; gli autori concludono per *"impaired translation or premature degradation of the WWOX protein"*. Fenotipo: epilessia precoce refrattaria, **microcefalia progressiva**, ritardo profondo, anomalie RMN, atrofia ottica bilaterale in una delle due. Gli autori le descrivono come i primi individui all'estremo **più severo** dello spettro pur portando **un solo missense**. → Conferma sperimentalmente la predizione in-silico di [[claim_registry_current#CLAIM 019]] e sposterebbe il bersaglio terapeutico dell'allele missense sulla **degradazione proteica** ⚠️ (lettura poi corretta — **CAUSA NON RISOLTA**: gli autori stessi dichiarano due alternative, traduzione compromessa oppure degradazione prematura; l'insolubilità è la terza). **Da recuperare dal PDF:** N e controlli del WB, densitometria, e soprattutto **se sia stata testata l'inibizione del proteasoma o un chaperone chimico**. Coautore **Markus A. Schirmer**, anche del paper JNCI sull'assay di inclusione dell'esone 9 → stesso gruppo: possiede i pezzi sperimentali per entrambi gli alleli worked-example.
**Wikilinks:** [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 032]]

---

## PAPER 042
**Short title:** Mallaret 2014 — WWOX in SCAR12 (P47T / G372R)
**Full title:** The tumour suppressor gene WWOX is mutated in autosomal recessive cerebellar ataxia with epilepsy and mental retardation
**Authors:** Mallaret M, Synofzik M, Lee J, et al., Aldaz CM, Koenig M
**Year:** 2014
**Source type:** primary — genetics + functional (Western blot, peptide pull-down)
**Journal/source:** *Brain* 2014;137(Pt 2):411-419
**Identifier:** PMID 24369382 / PMCID PMC3914474 / DOI 10.1093/brain/awt338
**Status:** claim_linked
**Evidence depth:** complete_fulltext_read — receipt `FTR-20260913-24369382-01` (2026-09-13, `scientist-a`; count corrected by `FTR-20260913-24369382-02`). Work manifest `deepdive_manifests/PMID24369382.json`, schema v2, 42 verbatim locators (35 body on the PMC reader text, 7 figure attestations; entries 35–41 added 2026-09-27 by wave-2 `m002`, verified `--verify-artifacts --require-current-schema` PASS). All four printed figures inspected as images; no tables printed. Declared debt: Supplementary Video 1 and the supplementary index are unreachable; no conclusion rests on either.
**Primary pathway:** genotype-phenotype / WW1 domain function
**Model/species:** human (fibroblasti di paziente; due famiglie) + topo Wwox-KO costitutivo — i Methods: *"constitutive recombination and producing full knock-out progeny"* (femmine BK5-Cre × Wwox flox/flox); l'intestazione dei Results dice *"Conditional knock-out mouse model"*: l'animale è un KO completo derivato da un allele condizionale
**Genotype/model:** **p.Pro47Thr omozigote** (WW1) e **p.Gly372Arg omozigote** (SDR) — entrambi SCAR12, presentazione *"milder"* rispetto ai modelli murino e di ratto secondo gli autori
**Transferability:** T1/T2 — genotipo caution OBBLIGATORIA: P47T ≠ Q230P (domini e meccanismi diversi)
**clinical relevance:** HIGH — fornisce UNA riga della serie allelica su cui poggia [[claim_registry_current#CLAIM 030]]: P47T omozigote con proteina presente nei fibroblasti del paziente e binding al peptide PPPY perduto in vitro, fenotipo SCAR12 (*"milder"* rispetto ai modelli murino e di ratto secondo gli autori). 🔴 **La dissociazione abbondanza/severità NON è dimostrata da questo paper:** l'abbondanza è misurata in UN SOLO individuo, su tre passaggi della stessa coltura contro quattro linee di controllo, *"based on visual inspection"*, senza densitometria né statistica, e per G372R non è misurata affatto. La dimostrazione è la costruzione CROSS-PAPER di `CLAIM 030`, la cui conclusione non è intaccata. 🔴 La Discussione usa l'abbondanza nella direzione OPPOSTA: attribuisce la presentazione umana più lieve rispetto ai modelli murino e di ratto a una *partial loss of function*, per due ragioni congiunte — la proteina P47T è *"still present, at least in human skin fibroblasts"* e il dominio deidrogenasi/reduttasi è *"presumably still functional in Family 1 and partially functional in Family 2, unlike the dehydrogenase/reductase domain of the WWOX mouse and rat models"*; l'assenza di proteina nel ratto *lde* è affermata separatamente, su dato citato (*"Mutated WWOX is not detected in western blots of lde rat tissues"*).
**Claim links:** 007, 008, 019, 030, 033 · 037 (the mouse audiogenic and spontaneous seizure dataset, added by `BATCH_20260927_002`)
**Role:** fonte primaria della serie allelica; àncora della regola "P47T ≠ Q230P"; **e — registrato 2026-09-27 da `BATCH_20260927_002` — l'unica fonte, nel corpus letto qui al 2026-09-27 (`PREMISE: INFERENZA`), di una provocazione audiogena con comparatore wild-type in un topo `Wwox`**, su cui poggia ora [[claim_registry_current#CLAIM 037]]
**Mouse seizure dataset (registered by `BATCH_20260927_002`, 2026-09-27; audited blind the same day):** il paper contiene l'unico esperimento di provocazione audiogena su un topo `Wwox` con comparatore nel corpus letto qui al 2026-09-27 (`PREMISE: INFERENZA` — un universale di corpus, non di letteratura). Genotipo: `Wwox^flox/flox` × femmine `BK5-Cre`, Cre *"activated in oocytes … leading to constitutive recombination and producing full knock-out progeny"* — **KO completo**, benché l'intestazione dei Results dica *"Conditional knock-out mouse model"*. Protocollo (Materials and methods, *"Animal experiments"*, terzo capoverso): toni digitali **11 e 14 kHz**, 5–10 min, animali *"in conventional polycarbonate cages"*, altoparlanti su tre lati, comportamento videoregistrato. Risultati: **3 su 8** KO a 16 giorni (*"in the first minutes after sound exposure"*); a 20 giorni **i quattro sopravvissuti** convulsionano *"at different times"*, con *"uncontrolled sphincter relaxation"* — ⚠️ la didascalia della Fig. 4 descrive **tre** topi (il primo a 30 s, poi *"two other mice"* a 4 min) mentre il testo dice tutti e quattro, e il paper non dice se i quattro includano i tre del giorno 16; comparatore **0 su 8** wild-type di età e background corrispondenti su 11 o 14 kHz; *"Other stimuli such as animal handling also induced seizures on some occasions"* → la specificità acustica **non è stabilita**; crisi spontanee da *"∼2 weeks of age"* **senza denominatore** e senza procedura di osservazione nei Methods. Classe di evidenza: **comportamentale e fotografica, non scorata** — nessun EEG, nessuna scala, nessuna latenza, nessuna statistica; Fig. 4 sono sedici fotogrammi (manifest `entries[33]`, 0-based). Debito dichiarato: Supplementary Video 1 non recuperato, e nessuna affermazione vi poggia. Un solo laboratorio — quello stesso dell'allele (Ludes-Meyers et al., 2009) — mai replicato indipendentemente. ⚠️ Il KO costitutivo **non modella** nessuno dei due alleli missense umani dello stesso paper: T2 per la vulnerabilità da perdita biallelica, **T3** per qualunque trasferimento del fenotipo audiogeno a un genotipo umano.
**Note:** Promosso in BATCH_20260710_A da [[paper_registry_current#CORPUS P294]]. **Finding decisivo:** Western blot su fibroblasti del paziente P47T (passaggi 10/13/14 vs 4 controlli): *"Based on visual inspection, similar amounts of the mutant and wild-type WWOX protein"*, *"suggesting that the mutation does not alter global protein levels"*; nessuna densitometria né statistica. **La proteina P47T è presente** — su *"visual inspection"* dichiarata, in un solo individuo, tre passaggi della stessa coltura contro quattro controlli: l'abbondanza non è quantificata. Peptide pull-down in vitro con costrutti di fusione e un solo peptide (WBP1, motivo PPPY): gli autori riportano che i costrutti p.Pro47Thr *"failed to interact"* e che la mutazione è *"sufficient to abrogate the affinity"*. In figura (Fig. 3) la corsia del costrutto tandem WW1-2 mutante è vuota entro la misura; quella del costrutto WW1-only mutante non è strettamente vuota (≤ ~2,5–2,8% della densità integrata della corsia wild-type — limite superiore: la corsia wild-type è saturata), ma quella densità è contigua a una scia che si assottiglia dalla banda wild-type saturata e il pannello non distingue binding residuo da alone laterale (lettura di figura attestata, non quantificata dagli autori). La generalizzazione a *"PPXY motif containing interacting partners"* è della didascalia degli autori, non del dato. Gli autori attribuiscono la mitezza a una *partial loss of function*: proteina *"still present, at least in human skin fibroblasts"* e dominio SDR *"presumably still functional in Family 1"*. Pazienti della Famiglia 1: 17-26 anni al 2014. *(`BATCH_20260926_MALLARET`: testo fin qui sottoposto ad audit cieco in quattro giri.)* → **Nessuna menzione di Gln230.** Vedi [[claim_registry_current#CLAIM 030]].
**Wikilinks:** [[claim_registry_current#CLAIM 007]] · [[claim_registry_current#CLAIM 008]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 033]] · [[claim_registry_current#CLAIM 037]] · [[claim_registry_current#CLAIM 005]]

---

## PAPER 045
**Short title:** Shaukat 2018 — West syndrome / DEE in WWOX-null
**Full title:** West syndrome, developmental and epileptic encephalopathy, and severe CNS disorder associated with WWOX mutations
**Authors:** Shaukat Q, Hertecant J, El-Hattab AW, Ali BR, Suleiman J
**Year:** 2018
**Source type:** primary — case reports (n=2) + a literature table of 23 cases that **includes these two** (21 previously reported; 13 families printed, 14 by the column sum; partly re-interpreted from published images by one author, Table 1 footnote `#`)
**Journal/source:** *Epileptic Disord* 2018;20(5):401-12
**Identifier:** PMID 30361190 / DOI 10.1684/epd.2018.1005 — bronze OA
**Status:** claim_linked
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-30361190-01` (the earlier `FTR-20260726-30361190-01` is a legacy reconstruction, not a reading); manifest `deepdive_manifests/PMID30361190.json`; dossier `research/fulltext_dossiers/PMID30361190.md`
**Primary pathway:** clinical spectrum / treatment response
**Secondary pathway:** P2 — GABAergic safety (vigabatrin)
**Model/species:** human — due bambini non imparentati, famiglie consanguinee
**Genotype/model:** null biallelici — caso 1: delezione omozigote esoni 3-4; caso 2: **splice acceptor omozigote c.606-1G>A** (introne 6)
**Transferability:** T1
**clinical relevance:** VERY HIGH
**Claim links:** 001, 031
**Role:** fonte primaria per il concetto DEE-non-EE e per il lato "efficacia" del claim vigabatrin
**Note:** Promosso in BATCH_20260710_A da [[paper_registry_current#CORPUS P356]] (Tier A, priorità HIGH, mai deep-dived). **Trattamento:** caso 1 — prednisolone (protocollo UKISS) → risposta parziale; **vigabatrin → "the spasms resolved"**; poi mioclonie focali/cloniche migliorate con **levetiracetam**. Caso 2 — fenobarbital → miglioramento; **vigabatrin → risposta parziale**; a 11 mesi spasmi in cluster nonostante 4 antiepilettici. **Nessun VABAM riportato.** **DEE non EE (testuale):** *"The developmental outcome was unfavourable with profound impairment **despite improvement of epileptic activity**"*; *"the cognitive and psychomotor impairment **preceded the onset of epileptic encephalopathy** and **did not improve with achievement of better control of epileptic activity**"*. **Fenotipo intermedio:** Table 1 riporta due fratelli (Mignot 2015, casi 3-4) compound eterozigoti **frameshift + missense (p.Pro47Arg)** con ritardo profondo ed epilessia severa ma **senza tetraparesi spastica, senza microcefalia e con RMN normale**. Su 23 casi: ritardo severo + epilessia in **23/23**; tetraparesi spastica **14/23** → è la spasticità, non l'epilessia, a discriminare. **Polimicrogiria** parietale bilaterale nel caso 2 → WWOX partecipa alla migrazione neuronale. **Metabolico normale** in entrambi (lattato, ammonio, acilcarnitine, aminoacidi, acidi organici, transferrina). Microcefalia **acquisita** (nascita normale → −3.38 SD a 6 mesi). 🔴 **Read at source 2026-10-03 (`CC-20261003W4-A-SHAUKAT-01`):** Table 1 records **one** MRI age per child, 2 months for both (row 'Age at MRI'; the source does not state that no further scan was performed) — progression is therefore not demonstrated in these two, and the abstract's 'progressive brain atrophy' comes from literature rows. Child 2's 'acquired microcephaly' is −1.62 SD at 11 months. The four heterozygous parents are genotyped, not examined (child 2: 'unremarkable family history'); family 1 has two affected, ungenotyped cousins. The DEE sentence is qualified by the authors ('in some of these cases'). Tarta-Arsene 2017 is not in Table 1.
**Wikilinks:** [[claim_registry_current#CLAIM 001]] · [[claim_registry_current#CLAIM 031]]

---

## PAPER 040
**Short title:** Banne 2021 — WWOX germline mutations, comprehensive overview
**Full title:** Neurological Disorders Associated with WWOX Germline Mutations—A Comprehensive Overview
**Authors:** Banne E, Abudiab B, Abu-Swai S, Repudi SR, Steinberg DJ, Shatleh D, Alshammery S, Lisowski L, Gold W, Carlen PL, Aqeilan RI
**Year:** 2021
**Source type:** review + curated variant dataset (ClinVar, DECIPHER, VarSome, PubMed, gnomAD)
**Journal/source:** *Cells* 2021;10(4):824
**Identifier:** PMID 33916893 / PMCID PMC8067556 / DOI 10.3390/cells10040824
**Status:** claim_linked
**Evidence depth:** full text reviewed — back-filled in `BATCH_20260909_001` onto receipt `FTR-20260909-33916893-01` (`complete_fulltext_read`, prior `FTR-20260726-33916893-01`, `inadequate_prior_coverage`); manifest `deepdive_manifests/PMID33916893.json` (35 locators, schema v2, strict PASS, 0 gaps). Prior provenance string retained for audit: *CC-2026-07-05-007, letto per intero*.
**Primary pathway:** genotype-phenotype / clinical spectrum
**Model/species:** human — meta-coorte da letteratura e database
**Genotype/model:** 56 pazienti WOREE/DEE28 + 6 SCAR12 (la coorte pubblicata più ampia al 2021). ⚠️ **Nota di conteggio, non un errore:** la colonna `Cases` del supplemento depositato somma a **58**, di cui due interruzioni prenatali — 58−2 = 56, 58−1 = 57 (la cifra della legenda del supplemento). **È una regola d'inclusione e non va registrata come errore.**
**Transferability:** T1
**clinical relevance:** HIGH — è il denominatore di riferimento per la casistica WWOX
**Claim links:** 008, 019, 033
**Role:** dataset di riferimento delle varianti patogenetiche WWOX; base per il ragionamento genotipo-fenotipo
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS-STUB-013]]. Consolida le varianti riportate distinguendo alleli causa-malattia da varianti benigne, e stima la correlazione tipo-di-variante ↔ fenotipo. Gli autori (lab Aqeilan) chiudono con una discussione su **approcci di medicina personalizzata**. ⚠️ È una **review con dataset curato**, non uno studio primario: le frequenze aggregano coorti eterogenee, con bias di pubblicazione verso i casi severi. Da usare come denominatore, non come stima di prevalenza. Nota di coerenza: il conteggio "56 WOREE / 6 SCAR12" è al 2021 e va aggiornato con le coorti successive ([[paper_registry_current#PAPER 018]], Oliver 2023).
**Wikilinks:** [[claim_registry_current#CLAIM 008]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 033]]

---

## PAPER 043
**Short title:** Abdel-Salam 2014 — early lethal WWOX microcephaly syndrome (p.Arg54*)
**Full title:** The supposed tumor suppressor gene WWOX is mutated in an early lethal microcephaly syndrome with epilepsy, growth retardation and retinal degeneration
**Authors:** Abdel-Salam G, Thoenes M, Afifi HH, Körber F, Swan D, Bolz HJ
**Year:** 2014
**Source type:** primary — case report (2 sorelle) + WES
**Journal/source:** *Orphanet J Rare Dis* 2014;9:12
**Identifier:** PMID 24456803 / PMCID PMC3918143 / DOI 10.1186/1750-1172-9-12
**Status:** claim_linked
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-24456803-01` (the earlier `FTR-20260726-24456803-01` is a legacy reconstruction without a coverage map, so the previous `complete` wording had no receipt behind it until now); manifest `deepdive_manifests/PMID24456803.json`; dossier `research/fulltext_dossiers/PMID24456803.md`
**Primary pathway:** clinical spectrum / null biallelico
**Model/species:** human — famiglia egiziana consanguinea
**Genotype/model:** **p.Arg54\* omozigote** (`c.160C>T`, esone 2) — nonsenso, null biallelico **predetto** (nessun saggio di RNA o proteina dell'allele umano). 🔴 Nomenclatura: il corpo del paper e la Table 2 scrivono `c.160G>T`, ma la Figure 1D e l'Additional file 1 degli stessi autori scrivono `c.160C>T`, e su NM_016373.4 la posizione c.160 è **C** (codone 54 = CGA): `G>T` non può generare p.Arg54\*. Usare `c.160C>T` (correzione `CC-20261003-A-ARG54-01`)
**Transferability:** T1
**clinical relevance:** HIGH — è il benchmark del caso peggiore (proteina zero su entrambi gli alleli)
**Claim links:** 030, 032
**Role:** estremo inferiore della serie allelica; sostiene il claim sull'aploinsufficienza
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P359]]. Fenotipo index: esordio crisi a **2 mesi**, risposta **parziale** a valproato + lamotrigina; **microcefalia progressiva/acquisita** (OFC −3.6 SD a 3 mesi → **−4.6 SD a 12 mesi**); nessuna tappa di sviluppo acquisita; **atrofia ottica + pigmentazione retinica anomala**, ERG ridotto, VEP ritardato; RMN: atrofia sopratentoriale, pattern girale semplificato, ipoplasia ippocampo/lobo temporale, **corpo calloso sottile**; **cervelletto non menzionato**. **Screening metabolico su sangue e urine normale** (funzione epatica e renale, emocromo, emogasanalisi, ammonio, lattato sierico, urea, elettroliti, aminoacidi e acidi organici, VLCFA). 🔴 Corretto 2026-10-03 (`CC-20261003-A-ARG54-01`): la versione precedente aggiungeva *«mitocondriale»* e *«biopsia muscolare»*, che il paper non riporta. **Morte a 16 mesi in stato epilettico.** Sorella maggiore: morta a 3 mesi con decorso simile, **mai vista dagli autori e mai genotipizzata** (*«probably affected»*) — non è un secondo omozigote confermato. ⭐ **Citazione chiave per [[claim_registry_current#CLAIM 032]]:** *"As in rats, **no tumors** were observed in the patient or **heterozygous mutation carriers**"* → nessun tumore **finora** nei portatori eterozigoti di questa famiglia. ⚠️ Corretto 2026-10-03 (`CC-20261003-A-ARG54-01`): la frase precedente (*«non oncologicamente a rischio»*) contraddiceva gli autori, che nello stesso paragrafo scrivono *«an increased cumulative lifetime risk, especially if exposed to carcinogenic agents, seems conceivable»* e consigliano controlli preventivi. È un'osservazione su una famiglia, non un negativo di rischio. ⚠️ Limiti: famiglia singola, **nessun assay proteico** (la nullità è inferita dal nonsenso), nessuna autopsia.
**Wikilinks:** [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 032]]

---

## PAPER 044
**Short title:** Davids 2019 — EIEE28 da microdelezione WWOX in disomia uniparentale
**Full title:** Early infantile-onset epileptic encephalopathy 28 due to a homozygous microdeletion involving the WWOX gene in a region of uniparental disomy
**Authors:** Davids M, Markello T, Wolfe LA, Chepa-Lotrea X, Tifft CJ, Gahl WA, Malicdan MCV
**Year:** 2019
**Source type:** primary — case report + expression analysis (NIH Undiagnosed Diseases Program)
**Journal/source:** *Hum Mutat* 2019;40(1):42-47
**Identifier:** PMID 30362252 / PMCID PMC6296882 / DOI 10.1002/humu.23675
**Status:** claim_linked
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read; Suppl. Table S1 — 23 pazienti — NON recuperata)
**Primary pathway:** genotype / transcript isoform biology
**Model/species:** human — fibroblasti di paziente
**Genotype/model:** **microdelezione omozigote di 22 kb sull'esone 6**, entro una regione di **disomia uniparentale materna** 16q22.1-16q24.3. Fenotipo misto per varianti concomitanti in **HSPG2** (perlecan) → confondente scheletrico.
**Transferability:** T2
**clinical relevance:** MODERATE-HIGH — fornisce il **metodo** per caratterizzare un difetto di trascritto
**Claim links:** none — background metodologico
**Role:** template metodologico (RNA + isoform-resolved Western) per dimostrare l'effetto di una variante sul trascritto
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P300]] (Tier A, priorità HIGH, mai deep-dived). **Finding trasferibile (letto dal CORPO, 2026-09-27, `FTR-20260927-30362252-02`, `CC-20260922-SPLICE-ARM-01`, `BATCH_20260927_004`):** il corpo afferma una **disgiunzione**, non l'NMD — *«The exon 1–2 junction, however, was detected and was only slightly reduced in our patient, whereas the exon 7–8 junction was barely detectable, suggesting that the two longer transcripts were **not expressed or were degraded**.»* — mentre *«nonsense mediated decay»* compare nell'**abstract** e nella **legenda della Figura 2B** (*«indicating that the deletion causes nonsense mediated decay of the two longer transcripts»*), come inferenza tratta dallo stesso qPCR di giunzione. ⚠️ **Nessun blocco della traduzione è stato usato su nessuna superficie raggiungibile gratuitamente:** `cycloheximide`, `puromycin`, `emetine`, `UPF1` = 0 occorrenze, e **il corpo PMC non contiene affatto la sezione Methods** (i metodi sono in un supplemento che Europe PMC dichiara non open access) — quindi è un'affermazione su **ogni superficie gratuita**, non una proprietà dell'esperimento. Un rapporto di giunzione non dimostra NMD senza un blocco della traduzione: le due alternative — mancata espressione contro degradazione — **restano irrisolte**, esattamente come in [[claim_registry_current#CLAIM 019]]. Al Western (legenda Fig. 2C, verbatim): *«Western blot analysis shows the lack of expression of the longest transcript at 46kDa in the proband»*, con l'isoforma corta da **19 kDa** (soli domini WW) aumentata e la terza (**33 kDa**) non rilevata né in paziente né in controllo → **abbondanza senza funzione**. 🔵 I valori `46` / `19` / `33` kDa sono ora locatorati sulla superficie JATS e non poggiano più su un'estrazione che li cancellava. ⭐ **Clinical relevance:** il triplo assay (qPCR giunzione-specifica sui tre trascritti + Western isoform-resolved + ddPCR CNV) è il **template pronto** per dimostrare l'effetto dell'allele di sito accettore `c.1057-2A>G`. ⚠️ Nota critica: qui l'NMD **avviene** perché la lesione è sull'**esone 6**; l'esone 9 è l'**ultimo**, e un PTC nell'ultimo esone **sfugge all'NMD** — l'assay per il genotipo di riferimento va progettato di conseguenza (discovery ledger DL-MECH-045). **MRS cerebrale: lattato "estremamente basso"** — outlier confuso dalla variante HSPG2.
**Wikilinks:** [[paper_registry_current#PAPER 021]]

---

## PAPER 046
**Short title:** Battaglia 2023 — neuroimaging WOREE (mini-review)
**Full title:** Neuroimaging features of WOREE syndrome: a mini-review of the literature
**Authors:** Battaglia et al.
**Year:** 2023
**Source type:** **narrative mini-review** (non sistematica)
**Journal/source:** *Front Pediatr* 2023;11:1301166
**Identifier:** PMID 38161429 / PMCID PMC10757851 / DOI 10.3389/fped.2023.1301166
**Status:** background_only
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-38161429-01` (every section, Table 1, Figure 1 and the reference list read; partial only because the multihop queue of gene-direct references is open); earlier `FTR-20260726-38161429-01` (legacy reconstruction) and `FTR-20260927-38161429-02` (bounded verification); manifest `deepdive_manifests/PMID38161429.json`; dossier `research/fulltext_dossiers/PMID38161429.md`
**Primary pathway:** neuroimaging / clinical monitoring
**Model/species:** human — Table 1 sums nine overlapping sources to '101'; this is not a patient count (Banne 2021's 56 collated cases predate and can include seven of the other eight sources, and the review's own Clinical section says 84 patients)
**Genotype/model:** misto
**Transferability:** T2
**clinical relevance:** MODERATE — utile per gli endpoint di imaging, **non** come fonte di prevalenze
**Claim links:** none — background
**Role:** background di imaging; **non** fonte di claim (review secondaria)
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P298]] come **background**. ⚠️ **Limite metodologico dirimente:** review **narrativa non sistematica**, senza PRISMA né criteri di inclusione; le coorti **si sovrappongono** (Banne n=56 ricompila casi già pubblicati) → **nessuna prevalenza aggregata è calcolabile**; solo le percentuali intra-studio sono oneste. **Reperto più costante:** corpo calloso ipoplasico/sottile, presente in **tutti e 9** gli studi. Poi atrofia cerebrale, iperintensità T2 simmetriche della sostanza bianca, atrofia ottica, ritardo di mielinizzazione. Anomalie già a **15-19 giorni**; **RMN fetale a 21 settimane**: lieve ipoplasia del verme cerebellare con girazione e laminazione corticale **normali**. Progressione su imaging seriato (Tabarki 5/5; Oliver: 7 of 13 had serial MRI, and the review states that their serial MRI 'showed progression of the abnormalities with age' — a subgroup statement, not a per-patient count (integrator amendment from blind audit, `BATCH_20261003_002`) — 7/13 is the fraction re-imaged, not a progression rate). The review's 'approximately 13%' divides these numerators by all 101, including patients never re-imaged, and is not a rate. ⚠️ **Due correzioni ai nostri prior:** (1) "atrofia ottica 100% a tutte le età" vale **solo nella coorte Oliver**, dove è stata cercata sistematicamente; altrove non tabulata → sotto-accertata. (2) **Non usare "demielinizzazione progressiva"**: la review parla sistematicamente di **ritardo di mielinizzazione / ipomielinizzazione** e di **atrofia progressiva** — un ritardo è in principio recuperabile, una demielinizzazione molto meno. La questione resta aperta. **Omissione rilevata:** la review non menziona la polimicrogiria (silent, not a denial), che è invece documentata in [[paper_registry_current#PAPER 045]] (Shaukat, caso 2) e in Ben-Salem 2015. ⭐ **For the disease model:** *"the p.Gln230Pro pathogenic variant affects the S[D]R domain and has been described both in homozygosity and in compound heterozygosity in **eight cases overall**. Nevertheless, **how missense variants affecting the SDR domain impair WWOX catalytic activity has not been demonstrated yet**."* → Q230P è un **hotspot ricorrente**; il suo meccanismo è dichiarato **non dimostrato**. 🔴 Provenance: the 'eight cases overall' is the review's citation of its reference 1 (Aldaz and Hussain 2020), not a count made by these authors; the same holds for its statement that exon 6-8 deletions give unstable products. The abstract's 'All affected patients showed brain anomalies' is contradicted by its own Piard row (abnormal MRI in 80%). **Gap:** nessuna metrica quantitativa (no volumetria, no area del CC, no DTI/FA, no MRS strutturata, no OCT/ERG/VEP) → un endpoint di imaging per il genotipo di riferimento va progettato internamente.
**Wikilinks:** [[paper_registry_current#PAPER 045]] · [[claim_registry_current#CLAIM 019]]

---

## PAPER 049
**Short title:** Elsaadany 2016 — W44X, crisi intrattabili e ritardo
**Full title:** W44X mutation in the WWOX gene causes intractable seizures and developmental delay: a case report
**Authors:** Elsaadany L, El-Said M, Ali R, Kamel H, Ben-Omran T
**Year:** 2016
**Source type:** primary — case report (2 sorelle)
**Journal/source:** *BMC Med Genet* 2016;17(1):53
**Identifier:** PMID 27495153 / PMCID PMC4975905 / DOI 10.1186/s12881-016-0317-z
**Status:** claim_linked
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-27495153-01` (the earlier `FTR-20260726-27495153-01` is a legacy reconstruction without a coverage map, so the previous `complete` wording had no receipt behind it until now); manifest `deepdive_manifests/PMID27495153.json`; dossier `research/fulltext_dossiers/PMID27495153.md`
**Primary pathway:** clinical spectrum / null biallelico
**Model/species:** human — famiglia araba consanguinea (Qatar)
**Genotype/model:** **p.Trp44Stop omozigote** (c.131G>A, esone 2) — null biallelico
**Transferability:** T1
**clinical relevance:** HIGH — comparatore fenotipico del null puro
**Claim links:** 031, 032
**Role:** fonte primaria sul decorso del null biallelico e sulla risposta agli antiepilettici
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P343]]. Esordio crisi a **7 settimane** in entrambe le sorelle. **Case 1 (older sibling): fenobarbitone, clonazepam, fenitoina e levetiracetam tutti falliti**; sorella: risposta **parziale** a fenobarbitone, clobazam e topiramato (the source's Table 1 enters 'Partial' for the family, against the four failures stated for the older sister). **Survival:** the older sister was alive at 7 years in a vegetative state, ventilated through a tracheostomy since about 2 years; the younger alive at 20 months — a predicted null/null genotype with survival well beyond infancy under intensive support, not an early death. RMN: **scarsa mielinizzazione già a 9 settimane**, assente a 23; assottigliamento simmetrico del **corpo calloso**; atrofia fronto-temporale; deformità ippocampale; **nessuna microcefalia** (OFC +0.37 SD). EEG: **perdita degli elementi del sonno**, background discontinuo, ~8 spasmi/ora su registrazione 24h. Pallore dei dischi ottici con **ERG normale**. Workup metabolico e mitocondriale interamente normale. Genitori **eterozigoti sani** ([[claim_registry_current#CLAIM 032]]). ⚠️ **Nota terminologica (correzione):** questo case report descrive la mielinizzazione come progressivamente compromessa; **non se ne inferisca "demielinizzazione progressiva"** come descrizione di malattia — la letteratura più ampia parla di **ipomielinizzazione + atrofia progressiva** ([[paper_registry_current#PAPER 046]]). ⚠️ W44X non è mai stata validata funzionalmente (NMD solo predetta).
**Wikilinks:** [[claim_registry_current#CLAIM 031]] · [[claim_registry_current#CLAIM 032]] · [[paper_registry_current#PAPER 046]]

---

## PAPER 050
**Short title:** Schirmer 2016 — Sp1 site in WWOX, assay giunzione esone 8-9
**Full title:** Relevance of Sp Binding Site Polymorphism in WWOX for Treatment Outcome in Pancreatic Cancer
**Authors:** Schirmer MA, Lüske CM, Roppel S, et al., Brockmöller J, Ghadimi BM
**Year:** 2016
**Source type:** primary — pharmacogenomics + functional (EMSA/supershift, siRNA, 89 LCL)
**Journal/source:** *J Natl Cancer Inst* 2016;108(5):djv387
**Identifier:** PMID 26857392 / PMCID PMC4859408 / DOI 10.1093/jnci/djv387
**Status:** claim_linked
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read; supplementary non recuperati)
**Primary pathway:** transcriptional regulation of WWOX; assay design
**Model/species:** human — 381 pazienti PDAC, 89 linfoblastoidi, linee cellulari
**Genotype/model:** rs11644322 G>A, **introne 8** — sito Sp1/Sp3
**Transferability:** T2 conceptual — oncologico, **non** WWOX-DEE
**clinical relevance:** MODERATE-HIGH — **fonte dell'assay di inclusione dell'esone 9**
**Claim links:** none — biomarker/assay seed
**Role:** origine metodologica dell'assay qPCR region-specifico; nessun claim canonico
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P312]]. **Perché è a registro nonostante sia oncologico:** gli autori quantificano separatamente i **trascritti della giunzione esone 8→esone 9** e i **trascritti core (esoni 4-6)** (rapporto ~67%; r=0.68 intra-linea). L'allele di sito accettore `c.1057-2A>G` è esattamente la **perdita dell'accettore dell'esone 9**: esiste dunque **un assay pubblicato e validato** che misura la regione d'interesse. ⭐ **Doppio valore per il modello di malattia:** (a) è il baseline per **qualunque** strategia di correzione dell'allele di sito accettore; (b) può fornire l'evidenza funzionale (**criterio ACMG PS3**) capace di **riclassificare la VUS** dell'allele di sito accettore. ⚠️ **Da riprogettare prima dell'uso:** loro misurano *espressione*, non *splicing aberrante*; e poiché l'esone 9 è l'**ultimo** (PTC → **NMD-escape**), un calo di abbondanza **potrebbe non osservarsi**. Servono primer che spannino la giunzione + sequenziamento, non solo qPCR. **Segnale su Sp1:** l'allele G lega Sp1/Sp3 più forte → più WWOX (EMSA + supershift + siRNA). ⚠️ **Non un candidato terapeutico**: quasi tutti i modulatori di Sp1 disponibili lo **inibiscono** (direzione sbagliata), e Sp1 controlla migliaia di geni. Coautore **Markus A. Schirmer**, anche di [[paper_registry_current#PAPER 041]] (Johannsen, Q230P) → **lo stesso gruppo possiede i pezzi sperimentali per entrambi gli alleli worked-example**.
**Wikilinks:** [[paper_registry_current#PAPER 041]]

---

## PAPER 053
**Short title:** Aldaz 2014 — WWOX at the crossroads (cancer, metabolic syndrome, CNS)
**Full title:** WWOX at the crossroads of cancer, metabolic syndrome related traits and CNS pathologies
**Authors:** Aldaz CM, Ferguson BW, Abba MC
**Year:** 2014
**Source type:** **review** (lab Aldaz)
**Journal/source:** *Biochim Biophys Acta* 2014;1846(1):188-200
**Identifier:** PMID 24932569 / PMCID PMC4151823 / DOI 10.1016/j.bbcan.2014.06.001
**Status:** background_only
**Evidence depth:** complete_fulltext_read — `FTR-20260913-24932569-02` (supersedes legacy reconstruction `FTR-20260726-24932569-01`); manifest `deepdive_manifests/PMID24932569.json`
**Primary pathway:** P5 — metabolism; interattoma; CNS
**Model/species:** review — topo, umano
**Genotype/model:** modelli murini condizionali; GWAS umani
**Transferability:** T2
**clinical relevance:** HIGH per il claim sull'aploinsufficienza; **background** per il resto
**Claim links:** 032
**Role:** review conduit for heterozygote evidence, checked against primaries; not independent proof that haploinsufficiency is generally benign
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS-STUB-020]] come **background con un claim link**. ⭐ **Citazioni chiave per [[claim_registry_current#CLAIM 032]]:** *"loss of one Wwox allele (i.e. **haploinsufficiency**) appears **not to be deleterious** or carcinogenic in the longer-lived heterozygous mice"*; *"The lifespan of the Wwox heterozygotes was **indistinguishable from WT mice**"*; *"loss of a single Wwox allele… **did not have any observable phenotypic effect** in the mammary gland"*. ⚠️ Nota: negli eterozigoti è documentato **aumento di tumorigenicità sotto carcinogeni chimici** o su fondo suscettibile — irrilevante per una strategia che *aumenta* WWOX, ma da non dimenticare. **Altri contenuti**: WWOX degradato via **poliubiquitinazione/proteasoma** (ACK1 fosforila Tyr287; substrato dell'E3 ligasi **ITCH**) — ⚠️ meccanismi di degradazione **regolata**, non controllo-qualità di proteina misfolded: **non assumere** che inibire ACK1/ITCH salvi Q230P. Il dominio **SDR governa anche la localizzazione subcellulare** (S281A/Y293F/K297A necessari sia alla catalisi sia alla localizzazione perinucleare) → il readout funzionale di Q230P deve includere la **localizzazione**. WWOX inibisce TGFβ/SMAD3 sequestrando SMAD3 nel citoplasma. Topi Wwox-KO: morte postnatale 72h-4 settimane, **ipoglicemia**, ipocalcemia, acidosi metabolica, nanismo. ⚠️ **Conflicting evidence da registrare:** Aldaz colloca WWOX in sede **perinucleare/Golgi** e attribuisce il ruolo pro-apoptotico riportato dal lab Chang ad **artefatto da vettori adenovirali**; il lab Chang lo colloca in mitocondri e nucleo. La disputa tocca direttamente il SDR.
**Wikilinks:** [[claim_registry_current#CLAIM 032]] · [[paper_registry_current#PAPER 021]]
**Assessment note (BATCH_20260926_ALDAZ_R4):** The historical review quotations in Note are retained as quotations, not adopted as primary findings. Ref 51 tests early growth/survival/blood/bone with a pooled WT+HET n=5 and does not substantiate a general no-carcinogenesis claim; the review’s lifespan sentence is uncited. Ref 55 (`PAPER 107`) covers mammary survival/tumours/premalignant histology but has no heterozygote branching group. Ref 50 (PMID 17360458) reports spontaneous tumour excess in untreated heterozygous mice (10/58 vs 2/60, p=0.03), omitted from the review’s framing. The SDR point-mutant localisation requirement is an unpublished Aldaz observation, not a cited primary result. Ref 69 (PMID 16223882) carries an Expression of Concern; this review disputes rather than depends on its apoptosis claim. These limits supersede the unqualified inferences in Note.

**R6 source clarification:** The review's phrase about unchanged heterozygote lifespan has no reference and `PAPER 107` follows tissue-restricted `BK5-Cre; Wwox+/flox` mice only to about day 118; it cannot establish germline lifespan equivalence. The review's «not deleterious or carcinogenic» framing omits untreated spontaneous tumours in ref 50 (`PAPER 078`). These quotations remain historical source text, not endorsed conclusions.

---

## PAPER 054
**Short title:** Saadane 2021 — photoreceptor calpain–WWOX
**Full title:** Photoreceptor Cell Calcium Dysregulation and Calpain Activation Promote Pathogenic Photoreceptor Oxidative Stress and Inflammation in Prodromal Diabetic Retinopathy
**Authors:** Saadane A, Du Y, Thoreson WB, Miyagi M, Lessieur EM, Kiser J, Wen X, Berkowitz BA, Kern TS
**Year:** 2021
**Source type:** primary — in vivo mouse + ex vivo retina + 661W cone photoreceptor line
**Journal/source:** *The American Journal of Pathology* 2021;191(10):1805-1821
**Identifier:** PMID 34214506 / PMCID PMC8579242 / DOI 10.1016/j.ajpath.2021.06.006
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260726-34214506-01`
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Secondary pathway:** P1 — Ca²⁺ / network dysregulation
**Model/species:** mouse (C57Bl/6J, Capn1⁻/⁻), STZ diabetes 2 months; 661W cone photoreceptor line
**Genotype/model:** wild-type WWOX; acute siRNA knockdown. **No WWOX-variant model.**
**Transferability:** **T3** — non-CNS-pediatric, wild-type background, acquired-stress model. Not a WWOX-DEE model and must never be read as one.
**clinical relevance:** INDIRECT
**Claim links:** 034 (new) · 028 (supports) · 009 (tensions)
**Role:** cross-context mechanistic bridge; directional counter-example
**Note:** Ca²⁺→calpaina→WWOX→superossido in un neurone eccitabile post-mitotico. Il dato più forte è **non guidato**: proteomica label-free LFQ (log2 N −3.55 → D −1.75 → DT −2.94; p 0.002 / 0.01), con `Wwox` mRNA ↑1.9× nella retina esterna. ⚠️ **La tesi degli autori — «Wwox was identified as a substrate for calpain», disegnata come via confermata in Figura 10 — non è dimostrata da questo lavoro:** nessun saggio di taglio, nessun frammento, e la direzione è invertita per un substrato (la calpaina sale e WWOX sale, mRNA compreso). Rigettata come affermazione, non come possibilità, in [[dismissal_ledger_current#DIS-008 — «La calpaina è una via di degradazione/turnover per WWOX» → ⏸️ **NON STABILITA (rigettata come affermazione, non come possibilità)**]]. ⚠️ Limiti trovati leggendo, non dichiarati dagli autori: l'esperimento WWOX decisivo è **n = 2** (legenda Fig 9) pur riportando SD e *P* ≤ 0.001; il controllo scrambled **non è inerte** (Fig 9C); l'inibitore di calpaina porta il superossido **sotto** il non-diabetico (Fig 6A); l'endpoint funzionale **non localizza ai fotorecettori** (onda-a invariata, solo l'onda-b è compromessa e recuperata, Fig 8); il codice del composto è stampato erroneamente come `MDL 27180` nei Results (il reale è **MDL 28170**). Espansione discovery: [[discovery_ledger_current#DL-MECH-061 — Ca²⁺→calpaina come regolatore dell'ABBONDANZA di WWOX in un neurone eccitabile (NON come via di degradazione)|DL-MECH-061]].
**Wikilinks:** [[claim_registry_current#CLAIM 034]] · [[claim_registry_current#CLAIM 028]] · [[claim_registry_current#CLAIM 009]]

---

## PAPER 055
**Short title:** Rotem-Bamberger 2022 — WW2 e cooperatività tandem WW-PPxY
**Full title:** Structural insights into the role of the WW2 domain on tandem WW-PPxY motif interactions of oxidoreductase WWOX
**Authors:** Rotem-Bamberger S et al.
**Year:** 2022
**Source type:** primary — biofisica strutturale; frammenti WW di WWOX umana purificati + peptidi ErbB4 sintetici
**Journal/source:** *Journal of Biological Chemistry* 2022;298(8):102145
**Identifier:** PMID 35716775 / PMCID PMC9293652 / DOI 10.1016/j.jbc.2022.102145
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260726-35716775-02`
**Primary pathway:** architettura di dominio / interpretazione delle varianti
**Model/species:** in vitro — nessuna WWOX full-length, nessuna variante patogenica, nessuna cellula, nessun animale
**Genotype/model:** WWOX wild-type, frammenti WW1/WW2 e tandem; **nessun allele WWOX-DEE testato**
**Transferability:** T2/T3 indiretta — alta per l'interpretazione di varianti e per il disegno dei saggi, nulla come leva terapeutica
**clinical relevance:** INDIRECT
**Claim links:** 024 (primary) · 028 (secondary)
**Role:** fonte primaria identificata per la cooperatività WW1–WW2, finora ancorata al solo placeholder [[paper_registry_current#CORPUS P204]]
**Note:** WW2 contribuisce con **due meccanismi distinti**: pre-ordina/stabilizza il WW1 altrimenti instabile, e può ingaggiare direttamente un secondo motivo PPxY quando sequenza, spaziatura, linker e orientamento creano una topologia compatibile (affinità fino a ~10×). ⚠️ **L'effetto WW2 diretto più grande si ottiene con peptidi tandem ingegnerizzati a linker corto**; il PY1PY2 nativo di ErbB4 guadagna affinità ma resta prevalentemente legato a WW1. **La sola presenza di due motivi non stabilisce quindi l'occupazione di WW2.** Limiti: nessuna validazione full-length o cellulare; la posa AlphaFold è modellata, non risolta sperimentalmente; il CD è in parte confuso dal peptide. **Lineage:** il candidato CC-20260726-002 proponeva di verificare se il placeholder [[paper_registry_current#CORPUS P204]] (Identifier PENDING, fonte di CLAIM 024) sia questa stessa pubblicazione. **La conferma non esiste**: il placeholder è conservato non fuso e questo record è creato come fonte identificata autonoma. Il riferimento `CORPUS P376` del candidato è un indice della TSV di seed, **non** il record [[paper_registry_current#CORPUS P376]] del registry (che è Farooq 2015, PMID 25662954): non usarlo come lineage.
**Wikilinks:** [[claim_registry_current#CLAIM 024]] · [[claim_registry_current#CLAIM 028]] · [[paper_registry_current#CORPUS P204]]

---

## PAPER 056
**Short title:** Wang 2012 — WWOX inibisce GSK3β via L404 (differenziamento neuronale)
**Full title:** WW domain-containing oxidoreductase promotes neuronal differentiation via negative regulation of glycogen synthase kinase 3β
**Authors:** Wang H-Y, Juo L-I, Lin Y-T, Hsiao M, Lin J-T, Tsai C-H, Tzeng Y-H, Chuang Y-C, Chang N-S, Yang C-N, Lu P-J
**Year:** 2012
**Source type:** primary — biochimica + biologia cellulare (SH-SY5Y) + co-IP endogena da cervello di topo
**Journal/source:** *Cell Death and Differentiation* 2012;19(6):1049-1059
**Identifier:** PMID 22193544 / PMCID PMC3354054 / DOI 10.1038/cdd.2011.188
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipts `FTR-20260726-22193544-01` (lettura completa) e `FTR-20260726-22193544-02` (correzione del solo path di output, nessuna rilettura)
**Primary pathway:** P1 — neurosviluppo / crescita neuritica
**Secondary pathway:** GSK3β / Tau / microtubuli; funzione del dominio SDR
**Model/species:** SH-SY5Y umana (differenziata con RA); proteine ricombinanti; estratto di cervello di topo (solo co-IP endogena)
**Genotype/model:** WWOX wild-type + mutanti puntiformi ingegnerizzati L404A / L311A e troncamenti Δ286 / Δ389. **Nessun allele WWOX-DEE testato.**
**Transferability:** **T2** — meccanicistico, risolto a livello di residuo, direttamente rilevante per la funzione SDR; ma linea aneuploide di origine tumorale, basato su sovraespressione, nessun materiale da paziente, nessun neurosviluppo in vivo. Non è un modello WWOX-DEE.
**clinical relevance:** INDIRECT — alto valore come *saggio* e come *vincolo di disegno*, non come terapia
**Claim links:** 035 (new) · 016 (enriches) · 030 (supplies the functional assay) · 028 (supports)
**Role:** fonte primaria, risolta a livello di residuo, dell'arco WWOX–GSK3β che il modello trattava già come portante; e fonte di un difetto documentato di figura supplementare
**Note:** WWOX lega GSK3β tramite il dominio ADH/SDR su un segmento di 20 residui (**388–407**) **richiesto per l'interazione** (Fig. 3c), mentre il motivo di docking Axin/FRAT/GSKIP conservato è contenuto nell'intervallo **distinto** `WWOX388−412` (Fig. 2a) — la fonte nomina due intervalli, `WWOX296−320` e `WWOX388−412`, e questo record ne fondeva due in uno fino al 2026-09-27 (`CC-20260826-GSK3B-S9-AXIS-01` `D11`, `BATCH_20260927_004`), con **L404 strettamente necessario**: `L404A` abolisce legame, inibizione della chinasi in vitro e in cellula, recupero dell'assemblaggio dei microtubuli e beneficio sul differenziamento, mentre il vicino `L311A` non fa nulla di tutto ciò. Il legame blocca la fosforilazione di Tau su **S396/S404** ma non su S422 (sito MKK4), con la **fosfo-S9 invariata** — *«We found that the phosphorylation levels of phospho-GSK3β S9 and phospho-β-catenin remained normal.»* (Results, Fig. 1b–c). ⚠️ **Corretto il 2026-09-27 dopo audit cieco (`research/locator_audits/2026-09-27_wave2_audit_C.md`, verdetto OVERSHOOT), e la correzione va nella direzione scomoda:** il candidato voleva scrivere che *l'abbondanza totale di GSK3β non è riportata in nessun punto del lavoro — una misura assente*. **È falso.** La legenda della Figura 1 elenca fra i livelli misurati *«phospho-GSK3βS9, GSK3β, β-catenin, phospho-β-catenin and actin»* e il pannello (c) li quantifica per densitometria: **il GSK3β totale è blottato e densitometrato.** Ciò che manca è la sua **invarianza narrativa** — nessuna frase del lavoro afferma che l'abbondanza totale resti normale — e i valori del pannello sono una superficie di figura non letta qui. Quindi: `NOT_ASSERTED` sull'invarianza, **non** `MEASURE_ABSENT` sulla misura (`CC-20260826-GSK3B-S9-AXIS-01` `D13`, `BATCH_20260927_004`). Il risultato più fisiologico è la **co-IP reciproca fra proteine endogene in estratto di cervello di topo**. 🔴 **Difetto documentato:** la Supplementary Figure A, citata dal testo *e* dalla propria legenda come la co-IP che dimostra *«WWOX does not associate with Tau»*, **non contiene alcun blot per Tau** — i suoi due pannelli sono etichettati WWOX e GSK3β. Il negativo **non è valutabile**: vedi [[dismissal_ledger_current#DIS-010 — «WWOX non lega Tau (Wang 2012)» → ⏸️ **NON STABILITA — il negativo è rifiutato per assenza di dato**]]. ⚠️ Altri limiti trovati leggendo: linea cellulare unica e aneuploide; sovraespressione ovunque (stechiometria endogena mai misurata); endpoint di differenziamento soggettivo e non in cieco; ampiezze d'effetto **incoerenti fra figure** per la stessa manipolazione; il saggio chinasico non è ricostruibile senza ambiguità (0.3 vs 0.2 µg di GST-WWOX, 25 µg/ml vs 0.5 µg di Tau, 30 °C/20 min vs 20 °C/10 min); il modello di interfaccia Fig 3f-h è **predizione GOR IV innestata su 1O9U**, non dato strutturale; il controllo di folding per L404A è a **partner singolo** (c-jun); WWOXtide è attivo a concentrazione **millimolare**. ⚠️ Il co-autore **Chang N-S** è l'originatore del campo WWOX; [[paper_registry_current#PAPER 053]] registra che le affermazioni del suo laboratorio su **localizzazione** e ruolo pro-apoptotico sono contestate da Aldaz. Nulla in questo lavoro dipende da quella localizzazione contesa, quindi la disputa non si propaga — ma il flag viaggia con qualunque uso della sua cornice di biologia cellulare. **Lineage:** il riferimento `CORPUS P263` del candidato CC-20260726-003 è un indice della TSV di seed, **non** il record [[paper_registry_current#CORPUS P263]] del registry (che è Chang 2014, PMID 25537520).
**Wikilinks:** [[claim_registry_current#CLAIM 035]] · [[claim_registry_current#CLAIM 016]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 028]] · [[paper_registry_current#PAPER 019]] · [[paper_registry_current#PAPER 053]]

---

## PAPER 057
**Short title:** Ludes-Meyers 2009 — allele condizionale `Wwox^flox` + fenotipo sistemico del null
**Full title:** Generation and characterization of mice carrying a conditional allele of the Wwox tumor suppressor gene
**Authors:** Ludes-Meyers JH, Kil H, Parker-Thornburg J, Kusewitt DF, Bedford MT, Aldaz CM
**Year:** 2009
**Source type:** primary — generazione di reagente + fenotipizzazione murina di base
**Journal/source:** *PLoS ONE* 2009;4(11):e7775
**Identifier:** PMID 19936220 / PMCID PMC2777388 / DOI 10.1371/journal.pone.0007775
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260806-19936220-01`, corretto append-only da `FTR-20260806-19936220-02` (solo lista output; nessuna rilettura). Manifest schema-v2 con 23 locator verbatim verificati.
**Integrity status:** clean — nessuna ritrattazione, expression of concern o correzione su PubMed o Europe PMC al 2026-08-06
**Primary pathway:** P5 — metabolismo / rene
**Secondary pathway:** reagente condizionale; ematopoiesi; osso
**Model/species:** topo; allele `Wwox^flox` (esone 1 floxed, cassetta pgk-neo ritenuta e fiancheggiata da siti FRT) e null sistemico `Wwox^ΔCre/ΔCre` generato con **EIIA-Cre** (Jackson 003724)
**Genotype/model:** nessun allele WWOX-DEE. **Driver Cre diverso** da PMID 30290271, che usa BK5-Cre: allele floxed condiviso, knockout diverso.
**Transferability:** T3 — null sistemico murino, fenotipizzazione motivata dall'oncologia. Ciò che trasferisce è **metodologico**, non fenotipico.
**clinical relevance:** INDIRECT
**Claim links:** 036 (new) · 038 (supplies the mouse renal datum) · 005 (bounds its imported premises)
**Role:** primario **dell'allele** `Wwox^flox`, e solo parzialmente **del modello** usato da PMID 30290271. **Non** è una fonte di fenotipo neurologico.
**Note:** Mortalità di prima mano e quantificata: **43% (15/35) morti a 72 h, 77% entro il giorno 17, nessuno oltre lo svezzamento**; Fig. 3B mostra un **arresto** della crescita (plateau a ~4 g dal giorno 10 al 17). 🔴 **L'epilettogenesi non è misurata qui in nessuna forma** — nessun EEG, crisi, comportamento o istologia cerebrale; l'unica misura cerebrale del paper è il peso dell'organo in Table 2. Le parole *seizure* ed *epilepsy* compaiono nel corpo una volta ciascuna, in una frase di Discussione che cita il **ratto** `lde`. 🔴 L'ablazione proteica è mostrata **solo in rene, polmone e milza** (identità dei tessuti visibile unicamente nel raster della Fig. 2C) e l'IHC solo nel rene: **nessun lisato cerebrale**. ⚠️ Il peso cerebrale è brain sparing (assoluto −8.7%, relativo 5.0% → 8.5%), non crescita. ⚠️ **Conflitto irrisolto sull'osteosarcoma:** 9 KO per necroscopia completa, raggi X, istopatologia multiorgano e microCT → **zero** lesioni neoplastiche, contro 4/13 (31%) riportati da Aqeilan 2007 (PMID 17360458); gli autori chiudono con *"The reason(s) for the discrepancies between studies remain to be determined."* ⚠️ L'osteoide è `p = 0.07` e «tended» nei Results, ma «we observed» nella Discussione. ⚠️ `N. Ob/BS` è significativo a `p = 0.02` **senza direzione dichiarata** e senza figura. ⚠️ Trappola di trascrizione: le coppie numeriche dell'osso sono ordinate WT/HET prima, KO poi, mentre il soggetto della frase è «KO mice» — l'inversione ricorre tre volte. ⚠️ Il χ² mendeliano è a 3 giorni, dentro la finestra in cui si verifica il 43% della mortalità. **Ipotesi degli autori mai testata:** acidosi tubulare renale come causa di morte — `WWOX AND ("metabolic acidosis" OR "renal tubular acidosis")` restituisce **un solo record PubMed, questo paper**, in diciassette anni. **Reagente:** eterozigoti normali su ogni asse misurato; la cassetta neo ritenuta è stata testata e non è ipomorfica.
**Wikilinks:** [[claim_registry_current#CLAIM 036]] · [[claim_registry_current#CLAIM 038]] · [[claim_registry_current#CLAIM 005]] · [[paper_registry_current#PAPER 058]] · [[paper_registry_current#CORPUS P295]]

---

## PAPER 058
**Short title:** Suzuki 2009 — mappatura di `lde` su `Wwox` + crisi audiogene nel ratto
**Full title:** A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with lethal dwarfism and epilepsy
**Authors:** Suzuki H, Katayama K, Takenaka M, Amakasu K, Saito K, Suzuki K
**Year:** 2009
**Source type:** primary — mappatura di linkage + sequenziamento + EEG + fenotipizzazione comportamentale
**Journal/source:** *Genes, Brain and Behavior* 2009;8(7):650–660
**Identifier:** PMID 19500159 / DOI 10.1111/j.1601-183X.2009.00502.x — **nessun PMCID**
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260806-19500159-01`; manifest schema-v2 con **30 locator** verificati (24 corpo, 2 tabella, 4 figura)
**Integrity status:** clean — nessuna ritrattazione, expression of concern o correzione su PubMed al 2026-08-06
**Supplementary status:** ⚠️ **unavailable, non saltati** — Figure S1/S2, Video S1 e Tabelle S1/S2 esistono e sono citati cinque volte; il recupero restituisce **HTTP 403** su entrambe le vie Wiley e il PDF non contiene allegati. Curve di crescita, sopravvivenza, pesi d'organo e statistica di segregazione sono letti solo come i Results li descrivono.
**Primary pathway:** P2 — eccitabilità / epilettogenesi
**Secondary pathway:** genetica del modello; espressione proteica
**Model/species:** ratto, ceppo inbred LDE; delezione spontanea di 13 bp nell'esone 9 di `Wwox`
**Genotype/model:** **strutturalmente frameshift C-terminale (371–424aa), funzionalmente null a livello proteico** — mRNA normale, né 47 né 42 kDa rilevabili in testicolo e ippocampo, con epitopo dell'anticorpo **fuori** dalla regione alterata. Nessun allele umano.
**Transferability:** T2 per la vulnerabilità conservata da perdita biallelica; **T3** per il trasferimento del fenotipo epilettico
**clinical relevance:** MODERATE
**Claim links:** 037 (new) · 005 (refutes its imported premise for the mouse) · 038 (frames the serum question)
**Role:** **terminale effettivo** della catena di citazioni che attribuiva l'epilettogenesi a un modello murino
**Note:** 🔴 **Afferma l'opposto della premessa importata, quattro volte:** *"Although neither epileptic seizures nor abnormal behavior has been reported in Wwox KO (knockout) mice"* (Introduzione); *"neither abnormal behavior nor impaired motor skill was observed in the Wwox KO mice … lde/lde rats show ataxic gait and spontaneous epileptic seizures"* (Discussione); *"the reason for no detection of spontaneous epilepsy in the KO mice is unknown … the KO mice may die before they experience epileptic seizure"*; e **Table 2**, dove la riga `Epilepsy` è compilata solo per `lde/lde` ed è **vuota per entrambi i modelli murini**. Fenotipo del ratto di prima mano: 19/20 (95%) crisi audiogene, 30/50 (60%) spontanee, 0/14 controlli, latenza 56±24 → 36±4 → 25±3 s, spike interictali ~10 Hz in tutti i mutanti non stimolati, vacuoli ippocampali 9/9 contro 0/10. 🔴 Il 95% è una coorte **solo femminile**, dichiarata unicamente nella didascalia della Fig. 6. 🔴 La didascalia della Fig. 1 **assegna male i propri pannelli** (il titolo dà normal a (a, b); l'immagine mostra normal in (a, c)): chi legge la didascalia senza l'immagine inverte quale ippocampo è malato. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — la scomparsa della proteina mutante è attribuita al sistema ubiquitina-proteasoma **senza saggio di turnover, inibitore o determinazione di via**. ⚠️ Due affermazioni comparative poggiano interamente su [[paper_registry_current#PAPER 059]]: il siero «normale» e il GH ipofisario basso; la seconda è **refutata** da quella fonte. ⚠️ Table 2 elenca osteosarcoma per il KO murino, propagando una affermazione contestata da [[paper_registry_current#PAPER 057]], accettato più tardi nel 2009.
**Wikilinks:** [[claim_registry_current#CLAIM 037]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 038]] · [[paper_registry_current#PAPER 059]] · [[paper_registry_current#PAPER 057]] · [[paper_registry_current#CORPUS P363]]

---

## PAPER 059
**Short title:** Suzuki 2007 — fenotipo originario del ratto `lde`, prima che il gene fosse noto
**Full title:** Phenotypic Characterization of Spontaneously Mutated Rats Showing Lethal Dwarfism and Epilepsy
**Authors:** Suzuki H, Takenaka M, Suzuki K
**Year:** 2007
**Source type:** primary — caratterizzazione fenotipica di un mutante spontaneo
**Journal/source:** *Comparative Medicine* 2007;57(4):360–369
**Identifier:** PMID 17803050 — **nessun DOI registrato, nessun PMCID, nessun deposito PMC**
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260806-17803050-01`; manifest schema-v2 con **32 locator** verificati (25 corpo, 4 tabella, 3 figura)
**Integrity status:** clean — nessuna ritrattazione, expression of concern o correzione su PubMed al 2026-08-06
**Primary pathway:** P5 — metabolismo / rene
**Secondary pathway:** P2 eccitabilità; P1 funzione motoria; sviluppo testicolare
**Model/species:** ratto, ceppo inbred LDE derivato da una colonia chiusa Wistar-Imamichi
**Genotype/model:** locus **`lde` ipotetico** — il gene non era ancora identificato. Nessun allele WWOX-DEE.
**Transferability:** T3
**clinical relevance:** INDIRECT
**Claim links:** 037 (co-source) · 038 (new, primary) · 039 (new, primary)
**Role:** fenotipo originario del ratto `lde`, **antecedente all'identificazione del gene**
**Note:** 🔴 **Credibilità strutturale:** accettato in **aprile 2007, due anni prima** che lo stesso gruppo mappasse `lde` su `Wwox`, e **nessuna** delle 35 referenze è WWOX-correlata perché nessuna poteva esserlo. I fenotipi non possono essere un gruppo WWOX-motivato che trova un risultato WWOX-forma. **Chimica ematica (Table 2, `n=4` normali / `5` mutanti per sesso):** BUN 12.6 → **40.3** ♀ e 10.1 → **35.6** ♂; creatinina 0.48 → **0.64** ♀ e 0.45 → **0.58** ♂; fosfato significativo solo ♀. **Glucosio, calcio, Na⁺, K⁺, Cl⁻ e trigliceridi tutti non significativi** — il ratto è **uremico senza essere ipoglicemico**. 🔴 **Spiegazione concorrente mai testata:** reni **istologicamente normali**, niente proteinuria, niente anemia, e gli autori propongono *"the production of urea-nitrogen and creatinine may be increased due to **hypercatabolism and muscle disruption**"* con precedente nel ceppo SER — ipotesi che compete direttamente con l'acidosi tubulare renale proposta per il topo in [[paper_registry_current#PAPER 057]]. 🔴 **Refuta una citazione che poggia su di esso:** [[paper_registry_current#PAPER 058]] attribuisce il nanismo al GH ipofisario basso citando questo paper, ma qui la differenza **non è significativa**, le cellule GH-positive sono presenti, e il paper conclude che il nanismo *"cannot be explained solely by low levels of plasma GH"*. La frase non qualificata esiste **solo nell'abstract** di questo paper: l'abstract sovradichiara il proprio corpo. **Fenotipo:** crisi 33.8% (22/65) ♂ e 33.9% (19/56) ♀, esordio 16–63 d, tre pattern, osservazione >6 h/giorno — **un pavimento, non un tasso**, per dichiarazione degli autori; atassia **95%** contro 0%, **non cerebellare**; sopravvivenza fino a 77 d ♂ e 84 d ♀ contro 1.5% di mortalità nei normali; vacuoli in CA1 e amigdala, assenti nei normali, senza corrispettivo in epilessia umana. ⚠️ Il χ² mendeliano poggia su **33 di 254 figliate**, selezionate per sopravvivenza. ⚠️ CPK, ALP, GPT e GOT portano note di **numerosità, non di significatività**: il CPK femminile è ~8.5× più alto **senza marcatore**. ⚠️ Brain sparing anche qui, con peso cerebrale assoluto **non** significativamente ridotto nei maschi. **Causa di morte: esplicitamente ignota.**
**Wikilinks:** [[claim_registry_current#CLAIM 037]] · [[claim_registry_current#CLAIM 038]] · [[claim_registry_current#CLAIM 039]] · [[paper_registry_current#PAPER 058]] · [[paper_registry_current#PAPER 057]]

## PAPER 060
**Short title:** Kołat 2023 — asse LINC01137/miR-186-5p/WWOX in carcinoma vescicale
**Full title:** LINC01137/miR-186-5p/WWOX: a novel axis identified from WWOX-related RNA interactome in bladder cancer
**Authors:** Kołat D, Kałuzińska-Kołat Ż, Kośla K, Orzechowska M, Płuciennik E, Bednarek AK
**Year:** 2023
**Source type:** primario in vitro + in silico — rianalisi CAGE-seq e coorti pubbliche
**Journal/source:** *Frontiers in Genetics* 2023;14:1214968
**Identifier:** PMID 37519886 / PMCID PMC10373930 / DOI 10.3389/fgene.2023.1214968
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260805-37519886-01`; manifest `deepdive_manifests/PMID37519886.json`
**Integrity status:** clean
**Primary pathway:** regolazione a RNA / ncRNA — contesto oncologico
**Model/species:** linee cellulari umane di carcinoma vescicale, sovraespressione di WWOX wild-type
**Genotype/model:** WWOX wild-type; **nessun allele WWOX-DEE, nessun contesto neuronale o dello sviluppo**
**Transferability:** **T3 — indiretta**
**clinical relevance:** LOW
**Claim links:** none — **nessuna nuova claim, nessun cambiamento al working model**
**Role:** promosso da `CORPUS-STUB-095` (BATCH_20260810_002, `CC-20260805-001`); il placeholder è conservato append-only
**Note:** Promozione **di registro e di provenienza, non di portata**: la lettura completa è avvenuta il 2026-08-05 e il record ne prende atto, ma il paper resta oncologia/immunologia adulta e va letto come `DISCOVERY_ONLY`. È la fonte da cui è emerso [[full_text_queue_current#FT-037]] (PMID 36499501), l'unico dei 29 riferimenti gene-/asse-diretti assente da ogni file LEGEND, e dà a miR-186-5p un ruolo **predetto** in una rete ceRNA — non misurato. Il valore per il modello di malattia sta nel metodo di enumerazione della bibliografia, non nella biologia vescicale.
**Wikilinks:** [[paper_registry_current#CORPUS-STUB-095]] · [[full_text_queue_current#FT-037]] · [[literature_tracking_log_current#LIT-0117]]

## PAPER 061
**Short title:** AbuRemaileh 2019 — ablazione di WWOX nel muscolo scheletrico e metabolismo del glucosio
**Full title:** WWOX somatic ablation in skeletal muscles alters glucose metabolism
**Authors:** Abu-Remaileh M, Aqeilan RI, et al.
**Year:** 2019
**Source type:** primario sperimentale — KO tessuto-specifico murino + knock-down acuto in C2C12
**Journal/source:** *Molecular Metabolism* 2019;22:132–140
**Identifier:** PMID 30755385 / DOI 10.1016/j.molmet.2019.01.010
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt `FTR-20260810-30755385-01`; manifest `deepdive_manifests/PMID30755385.json`
**Integrity status:** clean
**Primary pathway:** P5 — metabolismo
**Model/species:** topo, delezione di *Wwox* muscolo-specifica; linee C2C12
**Genotype/model:** KO condizionale muscolo-scheletrico; **non** un allele WWOX-DEE, **non** CNS
**Transferability:** T2 — meccanismo trasferibile, tessuto no
**clinical relevance:** INDIRECT
**Claim links:** 009 (evidenza a sostegno: la perdita di WWOX nel muscolo scheletrico è **sufficiente** a produrre fenotipi metabolici locali e sistemici)
**Role:** promosso da `CORPUS-STUB-039` (BATCH_20260810_003, `CC-20260810-30755385`); il placeholder è conservato append-only
**Note:** 🔴 **Confine di misura, da tenere.** **Misurato:** captazione muscolare di FDG, mtDNA, trascritti, p-AMPK/p-ACC, lattato sierico, fibra slow-twitch. **Non misurato:** l'ossidazione mitocondriale del glucosio — nessuna respirometria muscolare, nessun saggio di flusso. Prima del 2026-08-10 [[meta_metabolism_current]] la elencava fra i `Core Findings (DATO)`: era un'inferenza dai marcatori a monte, e ora è etichettata come tale. 🔴 **Confine causale:** delezione tessuto-specifica + FDG locale + knock-down acuto sostengono una componente **muscolo-intrinseca**; **non** provano che l'intero fenotipo in vivo sia autonomo di tessuto. Promozione condizionata a flusso ex-vivo su fibre primarie o rescue muscolo-specifico. ⚠️ **Discrepanza interna non risolta:** la didascalia della Figura 2 data l'ITT a **10 mesi**, Methods 4.4 a **6 mesi** — quattro mesi sono una finestra di malattia diversa in un topo; chi cita quella figura dichiara entrambe le età finché non è risolta alla fonte ([[full_text_queue_current#FT-048]]). Disegno statistico limitato. 🔑 **Il contributo che va oltre il paper:** è una delle tre fonti dell'inferenza *«il tessuto di misura non è il tessuto di necessità»* ([[full_text_queue_current#FT-049]]) — un KO muscolare che produce un fenotipo sistemico, accanto a un KO epatico che non abbassa l'HDL e a un restauro neuronale che recupera la periferia.
**Wikilinks:** [[paper_registry_current#CORPUS-STUB-039]] · [[claim_registry_current#CLAIM 009]] · [[meta_metabolism_current]] · [[full_text_queue_current#FT-048]] · [[full_text_queue_current#FT-049]] · [[literature_tracking_log_current#LIT-0063]]

## PAPER 062
**Short title:** Iatan 2014 — WWOX, HDL e metabolismo lipidico
**Full title:** The WWOX gene modulates high-density lipoprotein and lipid metabolism
**Authors:** Iatan I, Choi HY, Ruel I, et al.
**Year:** 2014
**Source type:** primario sperimentale + genetica umana — KO murino epatocita-specifico e total-body, più aplotipo intronico in coorti umane
**Journal/source:** *Circulation: Cardiovascular Genetics* 2014;7:491–504
**Identifier:** PMID 24871327 / DOI 10.1161/CIRCGENETICS.113.000248
**Status:** processed
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read) — receipt del 2026-08-10; manifest `deepdive_manifests/PMID24871327.json`; locator in `fulltext_dossiers/PMID24871327_locators.md`
**Integrity status:** clean
**Primary pathway:** P5 — metabolismo lipidico
**Model/species:** topo (KO epatocita-specifico e total-body); coorti umane
**Genotype/model:** ablazione completa di *Wwox* nel topo; nell'uomo un **aplotipo intronico**, senza cambiamento codificante e **senza saggio funzionale**
**Transferability:** T3 — endpoint periferici, nessun endpoint neurale
**clinical relevance:** INDIRECT
**Claim links:** none — **nessuna claim canonica ne dipende**, e la lettura è la ragione per cui non ne nasce una
**Role:** promosso da `CORPUS-STUB-108` (BATCH_20260810_004); il placeholder è conservato append-only. Chiude [[full_text_queue_current#FT-039]].
**Note:** 🔴 **È il primario che [[paper_registry_current#PAPER 055]] descriveva come *«strong evidence»* per il ponte `WWOX → omeostasi lipidica → mielina`, e la lettura mostra che l'etichetta non si trasferisce.** Il negativo centrale del paper è che **rimuovere *Wwox* dagli epatociti NON abbassa l'HDL circolante**: l'effetto HDL compare solo nel null total-body, misurato in cuccioli di 2 giorni che muoiono entro 4 settimane. Il passo che il primario licenzia davvero è `WWOX → ApoA-I/ABCA1 → biogenesi HDL`, **whole-body e non epatocita-autonomo**. Effect size: ApoA-I proteina −55%/−50% (KO epatico), −80% (KO totale); ABCA1 −50% nei maschi, invariato nelle femmine. 🔴 **La seconda gamba del ponte — `omeostasi lipidica → mielina` — non riceve nulla da qui: il paper non misura alcun endpoint neurale.** `PREMISE_TAG`: ogni inferenza che sia passata da questo nodo alla mielina poggiava su una premessa che questo primario **non contiene**. L'`ESPANSIONE` che resta è più stretta e reale — ApoA-I e ABCA1 sono indipendentemente rilevanti per la gestione lipidica del CNS, quindi il nodo **resta aperto come espansione da testare, non come inferenza sostenuta**. ⚠️ Debito dichiarato: il Supplementary è `unavailable` (cascata documentata; AHA all-rights-reserved) e porta il dato trigliceridi `P=0.0025` da cui parte la storia sesso-specifica; il multi-hop non è stato svolto ([[full_text_queue_current#FT-046]]).
**Wikilinks:** [[paper_registry_current#CORPUS-STUB-108]] · [[paper_registry_current#PAPER 055]] · [[full_text_queue_current#FT-039]] · [[full_text_queue_current#FT-046]] · [[full_text_queue_current#FT-049]] · [[literature_tracking_log_current#LIT-0128]]

---

## PAPER 063
**Short title:** Steinberg 2021 — atlante dei modelli WWOX
**Full title:** WWOX-Related Neurodevelopmental Disorders: Models and Future Perspectives
**Authors:** Steinberg DJ, Aqeilan RI
**Year:** 2021
**Source type:** review narrativa / atlante di modelli — **nessuna coorte sperimentale nuova**
**Journal/source:** *Cells* 2021;10(11):3082
**Identifier:** PMID 34831305 / PMCID PMC8623516 / DOI 10.3390/cells10113082
**Status:** processed
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260810-34831305-03`, JATS XML PMC8623516; manifest `deepdive_manifests/PMID34831305.json` (13 locator, validatore PASS con root sul checkout condiviso); dossier `fulltext_dossiers/PMID34831305.md`. Le 224 citazioni sono state enumerate.
**Integrity status:** clean
**Primary pathway:** P3 / P4 / P7 — architettura causale fra modelli
**Model/species:** ratto; topo globale, ipomorfo, condizionale e cell-targeted; tessuto umano; hNPC/neuroblastoma; organoidi cerebrali, di proencefalo e oligocorticali
**Genotype/model:** trasversale — nessun allele proprio
**Transferability:** MODERATE per l'architettura causale, LOW per la traduzione quantitativa
**clinical relevance:** HIGH come mappa di ricerca; **BACKGROUND come evidenza di claim**
**Claim links:** none — **è una sintesi, non una replica indipendente dei primari che elenca**
**Role:** promosso da `CORPUS-STUB-003` (BATCH_20260810_005) via `CC-20260810-34831305-01`; il placeholder è conservato append-only.
**Note:** 🔴 **Il valore è che il gruppo primario del gene mette più sistemi-modello su una sola mappa causale; il limite è che la lettura non può ereditare lo statuto `DATO` dei primari solo perché li enumera.** Reperti di superficie: sono nominate quattro delezioni cell-targeted (Nestin-Cre, Synapsin-I-Cre, GFAP-Cre, Olig2-Cre) e **solo Nestin e Synapsin ricapitolano il fenotipo null** nell'intervallo riportato; l'accoppiamento neurone→oligodendrocita è riassunto come **difetto di maturazione** (OL maturi ↓, OPC ↑, mielinizzazione ↓); è distinto un compartimento umano **assente o poco sviluppato nei roditori** (glia radiale esterna / oSVZ) mentre WWOX precoce negli organoidi si concentra nella glia radiale ventricolare; l'arricchimento trascrizionale negli organoidi WWOX-KO (trasporto elettronico ATP-linked, OXPHOS, glicolisi/gluconeogenesi, ciclo cellulare, regionalizzazione Wnt) è **programma di espressione, non misura di flusso**. 🔴 **Tre tensioni registrate, non appianate.** (1) *Inflazione di sintesi:* la review descrive il litio come soppressore delle crisi da PTZ **nel contesto KO**; l'audit d'immagine già persistito del primario PMID 32000863 mostra la soppressione nei pannelli **WT, eterozigote e KO** — quindi **non può sostenere un rescue farmacologico WWOX-specifico** (vedi [[claim_registry_current#CLAIM 016]]). (2) *«Efficient and safe» eccede l'evidenza:* non ci sono dati umani né esperimenti formali di sicurezza in questa fonte; è un'ipotesi di design preclinico. (3) *Compressione dei modelli:* Tabella 1 e Figura 2 collassano ceppi distinti, modelli cell-targeted e bracci negativi, il che migliora la leggibilità e oscura **quale modello sostenga quale affermazione causale**. ⚠️ Debito: figure servite dalla CDN PMC a 757×434 e 772×550 contro originali dichiarati nell'XML di 4542×2601 e 4248×3026 — **artefatti scalati**, ispezionati ai pixel nativi perché leggibili; le rotte `/bin/` e il pacchetto OA hanno restituito HTTP 404. **Assenza del supplementary dedotta** dalla struttura XML completa, non da una dichiarazione dell'editore. ⚠️ Standing caution (`CC-20260826-UPSTREAM-CITATION-FAILURE-01`, propagated `BATCH_20260927_001`): this review is cited as the authority for a null-mouse seizure measurement it does not contain, and it is independently recorded in [[claim_registry_current#CLAIM 016]] as narrowing what its primary left broad. It is a citation conduit, not a source of measurement.
**Wikilinks:** [[paper_registry_current#CORPUS-STUB-003]] · [[paper_registry_current#PAPER 004]] · [[paper_registry_current#PAPER 005]] · [[claim_registry_current#CLAIM 003]] · [[claim_registry_current#CLAIM 004]] · [[claim_registry_current#CLAIM 016]] · [[full_text_queue_current#FT-049]] · [[literature_tracking_log_current#LIT-0030]]

---

## PAPER 064
**Short title:** Drusco 2011 — common-fragile-site mouse-model review
**Full title:** Common Fragile Site Tumor Suppressor Genes and Corresponding Mouse Models of Cancer
**Identifier:** PMID 21318118 / PMCID PMC3035048 / DOI 10.1155/2011/984505
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-21318118-01`; manifest `deepdive_manifests/PMID21318118.json`
**Source type:** narrative review; background, not independent primary evidence
**Transferability:** T3
**Claim links:** none
**Note:** Preserves the 2011 review-level tension that global-null mice had no reported abnormal behaviour or motor impairment; its proposed compound chemical-challenge model was not tested. Figure 1 contains no WWOX panel.

## PAPER 065
**Short title:** WWOX/p53 cooperation in osteosarcoma lineage
**Full title:** WWOX and p53 Dysregulation Synergize to Drive the Development of Osteosarcoma
**Identifier:** PMID 27550453 / DOI 10.1158/0008-5472.CAN-16-0621
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-27550453-01`; manifest `deepdive_manifests/PMID27550453.json`
**Source type:** primary mouse genetics
**Transferability:** T3; oncology and lineage context
**Claim links:** 032
**Note:** Wwox loss impairs differentiation without producing osteosarcoma alone; Wwox/p53 double loss accelerates tumour formation in early Osx1-lineage cells but not mature Oc-lineage cells. Table S6 cytogenetics and p53-IHC classification remain explicit limitations.

## PAPER 066
**Short title:** Somatic WWOX/TP53 cooperation in basal-like breast cancer
**Full title:** Somatic loss of WWOX is associated with TP53 perturbation in basal-like breast cancer
**Identifier:** PMID 30082886 / DOI 10.1038/s41419-018-0896-z
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-30082886-01`; manifest `deepdive_manifests/PMID30082886.json`
**Source type:** primary mouse/cell/human-cohort study
**Transferability:** T3
**Claim links:** 032
**Note:** Supports context-dependent WWOX–p53 cooperation. Mouse comparisons are background-confounded; human deletion groups are small and no pairwise double-versus-TP53-only survival test establishes common co-occurrence.

## PAPER 067
**Short title:** Abdeen 2018 — in-vivo WWOX model review
**Full title:** Modeling WWOX Loss of Function in vivo: What Have We Learned?
**Identifier:** PMID 30370248 / DOI 10.3389/fonc.2018.00420
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-30370248-01`; manifest `deepdive_manifests/PMID30370248.json`
**Source type:** narrative review; secondary evidence
**Transferability:** background only
**Claim links:** none
**Note:** Used as a historical model map, not replication. It miscites a human SCAR12 paper for rodent seizures and pools species in its figure; primary mouse/rat readings control the interpretation.

## PAPER 068
**Short title:** WWOX antagonizes metastasis through context-dependent axes
**Full title:** Pleiotropic tumor suppressor functions of WWOX antagonize metastasis
**Identifier:** PMID 32300104 / DOI 10.1038/s41392-020-0136-8
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-32300104-01`; manifest `deepdive_manifests/PMID32300104.json`
**Source type:** primary cell/xenograft study
**Transferability:** T3
**Claim links:** none
**Note:** Directly supports miR-146a targeting of SMAD3 3′UTR with partial anti-miR rescue and contextually replicates WWOX–DVL2 association. Computational targets and denominator-sensitive supplementary analyses are not promoted as validated therapeutic evidence.

## PAPER 069
**Short title:** WWOX/KRAS cooperation in pancreatic cancer
**Full title:** Loss of tumor suppressor WWOX accelerates pancreatic cancer development through promotion of TGFβ/BMP2 signaling
**Identifier:** PMID 36572673 / DOI 10.1038/s41419-022-05519-9
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-36572673-01`; manifest `deepdive_manifests/PMID36572673.json`
**Source type:** primary conditional-mouse and acinar-cell study
**Transferability:** T3
**Claim links:** 032
**Note:** Acinar Wwox loss alone has no detected phenotype; with KrasG12D it accelerates ADM/PanIN and PDAC. Culture supports a cell-autonomous component, not autonomous sufficiency; TGFβ/BMP inhibition remains future work.

## PAPER 070
**Short title:** WWOX/p53 cooperation in cutaneous SCC
**Full title:** WWOX loss cooperates with p53 deficiency to drive cutaneous squamous cell carcinoma through destabilization of p63
**Identifier:** PMID 41984841 / PMCID PMC13099603 / DOI 10.1073/pnas.2534844123
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260810-41984841-01`; manifest `deepdive_manifests/PMID41984841.json`
**Source type:** primary conditional mouse/cell/human-tissue study
**Transferability:** T3
**Claim links:** 032
**Note:** Wwox loss cooperates with p53 deficiency but is insufficient alone in this model. The WWOX–p63 axis is supported; the proposed direct ITCH/proteasomal stabilization of WWOX is superseded by PAPER 079's substrate-resolved reading. ChIP-seq n=1, nonphysiological rescue and outcome-model limits remain attached.

## PAPER 071
**Short title:** Wwox–Idh/Sod redox genetics in Drosophila
**Full title:** WWOX, the chromosomal fragile site FRA16D spanning gene, has a role in cell metabolism
**Identifier:** PMID 21075834 / PMCID PMC3016910 / DOI 10.1093/hmg/ddq495
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260811-21075834-01`; manifest `deepdive_manifests/PMID21075834.json`
**Source type:** primary fly genetics plus HEK293 experiment
**Transferability:** T3
**Claim links:** 009 (counter-directional) · 034 (context dependence)
**Note:** Thresholded CM-H2DCFDA, Wwox×Idh and Wwox×Sod interactions support a redox-metabolic resilience network, not a universal deficiency→ROS direction or a treatment recommendation. No metabolic flux was measured.

## PAPER 072
**Short title:** Abu-Remaileh 2014 — glycolysis commentary
**Full title:** WWOX loss activates aerobic glycolysis
**Identifier:** PMID 27308416 / DOI 10.4161/23723548.2014.965640
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260811-27308416-01`; manifest `deepdive_manifests/PMID27308416.json`
**Source type:** commentary on PAPER 024; no independent experimental cohort
**Transferability:** background only
**Claim links:** 009 as interpretation, not replication
**Note:** Its metabolic observations transmit PMID 25012504 and must not be counted as a second core paper.

## PAPER 073
**Short title:** Aqeilan 2015 — WWOX biology review
**Identifier:** PMID 25491415 / PMCID PMC4935230 / DOI 10.1177/1535370214561956
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260811-25491415-01`; manifest `deepdive_manifests/PMID25491415.json`
**Source type:** review; secondary evidence
**Transferability:** background only
**Claim links:** none
**Note:** Carries an internally reversed HIF1α/glucose formulation and a questionable transmission of Drosophila ROS; neither is promoted as a new datum.

## PAPER 074
**Short title:** WWOX rescue suppresses osteosarcoma metastasis
**Full title:** Tumor Suppressor WWOX inhibits osteosarcoma metastasis by modulating RUNX2 function
**Identifier:** PMID 26256646 / DOI 10.1038/srep12959
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260811-26256646-01`; manifest `deepdive_manifests/PMID26256646.json`
**Source type:** primary rescue-model study
**Transferability:** T3
**Claim links:** 032
**Note:** WWOX re-expression suppresses migration, invasion and lung metastasis. RUNX2 mediation remains inference because direct perturbation, occupancy, reporter and interaction tests are absent; small and unequal mouse arms remain attached.

## PAPER 075
**Short title:** Conditional Wwox allele and systemic-null phenotype
**Identifier:** PMID 23254685 / PMCID PMC3943428 / DOI 10.1002/jcp.24308
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260811-23254685-01`; manifest `deepdive_manifests/PMID23254685.json`
**Source type:** primary mouse genetics
**Transferability:** T3
**Claim links:** 036
**Note:** Germline deletion recreates systemic collapse and osteopenia. Rare malignant-appearing osteoblasts lack an incidence denominator and do not settle the cross-study osteosarcoma conflict.

## PAPER 076
**Short title:** Wwox loss and impaired steroidogenesis
**Full title:** Targeted ablation of the WW domain-containing oxidoreductase tumor suppressor leads to impaired steroidogenesis
**Identifier:** PMID 18974271 / PMCID PMC2654736 / DOI 10.1210/en.2008-1087
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260811-18974271-01`; manifest `deepdive_manifests/PMID18974271.json`
**Source type:** primary systemic-null mouse study
**Transferability:** T3
**Claim links:** 036
**Note:** The endocrine phenotype is measured, but gonadal autonomy cannot be separated from pituitary suppression, developmental delay and terminal systemic illness.

## PAPER 077
**Short title:** Wwox heterozygosity and NMBA tumour susceptibility
**Identifier:** PMID 17575124 / PMCID PMC2621009 / DOI 10.1158/0008-5472.CAN-07-1081
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260811-17575124-01`; manifest `deepdive_manifests/PMID17575124.json`
**Source type:** primary carcinogen-challenge mouse study
**Transferability:** T3
**Claim links:** 032
**Note:** Adult heterozygotes can be unremarkable without challenge yet show strong NMBA-dependent susceptibility. Protein positivity in tumours does not prove integrity of the residual allele.

## PAPER 078
**Short title:** Targeted deletion of Wwox
**Full title:** Targeted deletion of Wwox reveals a tumor suppressor function
**Identifier:** PMID 17360458 / PMCID PMC1820689 / DOI 10.1073/pnas.0609783104
**Status:** processed
**Evidence depth:** complete_fulltext_read with inaccessible SI Figure 4 gap — `FTR-20260811-17360458-01`; manifest `deepdive_manifests/PMID17360458.json`
**Source type:** primary mouse genetics
**Transferability:** T3
**Claim links:** 032 · 036
**Note:** Establishes complete pre-weaning mortality and carcinogen-sensitive heterozygous tumour susceptibility. The 4/13 morphology-only juvenile bone-lesion finding conflicts with 0/9 by multimodal examination in PAPER 057 and remains unsettled.

**R6 correction:** Table 1 also reports an excess of **spontaneous** tumours in untreated heterozygotes aged 9–18 months (10/58 versus 2/60, p = 0.03), in addition to the ENU challenge result (37/46 versus 20/42, p = 0.002). The previous Note described only carcinogen susceptibility; the spontaneous result is not a stress interaction.

## PAPER 079
**Short title:** WWOX competes with ITCH for ΔNp63α
**Identifier:** PMID 23370280 / PMCID PMC3564006 / DOI 10.1038/cddis.2013.6
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260814-23370280-02`; manifest `deepdive_manifests/PMID23370280.json`
**Source type:** primary transformed-cell mechanistic study
**Transferability:** T3
**Claim links:** none
**Note:** WWOX competes with ITCH for ΔNp63α, reducing substrate ubiquitination/turnover and raising ΔNp63α half-life while cytoplasmic sequestration lowers transcriptional activity. It does not show ITCH stabilizing WWOX; that separate mechanism belongs to PMID 24550385.

## PAPER 080
**Short title:** WWOX supports the ATR checkpoint response
**Full title:** WWOX modulates the ATR-mediated DNA damage checkpoint response
**Identifier:** PMID 26675548 / DOI 10.18632/oncotarget.6571
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260814-26675548-02`; manifest `deepdive_manifests/PMID26675548.json`
**Source type:** primary cultured-cell mechanistic study
**Transferability:** T3
**Claim links:** none
**Note:** WWOX loss associates with weaker p-CHK1, defective G2/M arrest and more APH-associated breaks; wild-type rescue improves the break phenotype. The ATM→ITCH→K63-WWOX→ATR chain remains composite, and the APH dose conflict (0.2 mM versus 0.2 μM) is preserved.
## PAPER 081
**Short title:** WWOX–p73: WW1 binding, Tyr33 phosphorylation, and cytoplasmic rerouting
**Full title:** Functional association between Wwox tumor suppressor protein and p73, a p53 homolog
**Identifier:** PMID 15070730 / DOI 10.1073/pnas.0400805101 / PMC384759
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-15070730-02`; manifest `deepdive_manifests/PMID15070730.json` (38 locators, strict PASS, 0 gaps)
**Source type:** primary experimental (cell-line biochemistry and immunofluorescence)
**Transferability:** T2 mechanistic / indirect for the reference genotype
**clinical relevance:** INDIRECT — structurally important for model architecture
**Claim links:** → [[claim_registry_current#CLAIM 023]] (primary source of its mechanism)
**Note:** Promoted from `CORPUS P206`, whose `Identifier` was the literal string `PENDING`; the placeholder is preserved append-only. 🔴 **The promotion also disproves the placeholder's own duplicate hypothesis:** `CORPUS P206` carried the note *"likely overlaps PAPER 026 (PMID 32185845); verify before merge"*, and this reading establishes the source as PMID 15070730, a different paper. The two records must NOT be merged, and `PAPER 026` (abstract-only) continues to report the opposite direction for the Tyr33 effect — a standing tension recorded on both records, not resolved here. Identification independently corroborated: `scientist-c`, reading PMID 21115974 the same morning, identified this paper as that paper's reference 19. **Binding leg is the best-supported content**: bidirectional co-IP, endogenous interaction in two cell types, PPxY dependence confirmed three ways, direct GST pull-down with the isolated first 50 aa, p53 excluded as a specificity control. **Routing leg is overexpression-dependent by the authors' own words** and its only graded-dose titration (Fig 5) carries no dose labels, no merged channel, no cell count, no n and no statistic. Three citation defects recorded and independently reconfirmed: the Discussion credits Fig 1G with a Y34 binding result Fig 1G does not contain; it cites "Fig. 3 D" twice for a figure declaring only (A), (B), (C); and zero P-values appear anywhere in the body. Fig 5 has no caption on either surface, so which panel is the reduced dose is an assumption, not a datum.
**Reading debt:** PMID 12514174 (Chang et al., murine Wox1/JNK) is the source of the entire Y33 rationale and this corpus does not hold it — a `DATO` in the source that has never been verified here.

## PAPER 082
**Short title:** Ad-WWOX restoration in lung cancer — the reagent-provenance source
**Full title:** WWOX gene restoration prevents lung cancer growth in vitro and in vivo
**Identifier:** PMID 16223882 / DOI 10.1073/pnas.0505485102 / PMC1266103
**Status:** background_only
**Evidence depth:** full text reviewed — `FTR-20260909-16223882-01` (`complete_fulltext_read`); manifest `deepdive_manifests/PMID16223882.json` (26 locators, strict PASS, 0 gaps, 12/12 page adjudications verified)
**Source type:** primary experimental (oncology; no CNS material, no reference-genotype allele)
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none — 🔴 **deliberately none.** `CLAIM 002` and `CLAIM 004` must NOT be linked to this record; the non-link is recorded as a decision, not an omission.
**Role:** reagent provenance — the source of the Ad-WWOX construct used downstream
**Integrity status:** 🔴 `PUBLICATION_INTEGRITY_HOLD` — **expression of concern**, PMID 28373548, *PNAS* 2017;114(16):E3365, DOI `10.1073/pnas.1704296114`, signed by Inder M. Verma. **Standing as of 2026-09-09; NOT a retraction.** Carried forward from `CORPUS-STUB-119`, where the field was added in `BATCH_20260806_002`, and now backed by a complete read of the expression of concern as its own source (`FTR-20260909-28373548-01`, fingerprint `28069dd2cf98d2eb…`). **Scope is narrow and precise:** one panel — *"Fig. 1B, β-actin panel, appears to have duplicated bands"*. The original data no longer exist (*"more than 7 years after publication"*); the published remedy is a **2014 replicate**, and the editors publish it **without stating that they verified it** — every confirmatory sentence is attributed to the authors. **Operational consequence:** Fig. 1B is the panel demonstrating that Ad-WWOX expresses Wwox at controlled load. The WWOX row is not contested and the 2014 replicate reproduces its lane pattern, so *that Wwox appears after infection* holds; **the quantitative between-lane reading does not hold without qualification.** Anyone citing load comparability must cite the 2017 replacement, not the 2005 panel.
**Note:** Promoted from `CORPUS-STUB-119`, placeholder preserved append-only. Closes the `FT-076` reagent-provenance debt opened from PMID 20530675.

## PAPER 083
**Short title:** Pancreatic Ad-WWOX restoration, and an inherited reagent dependency
**Full title:** Role of the WWOX gene, encompassing fragile region FRA16D, in suppression of pancreatic carcinoma cells
**Identifier:** PMID 18460020 / DOI 10.1111/j.1349-7006.2008.00841.x / PMC11159152
**Status:** background_only
**Evidence depth:** full text reviewed — `FTR-20260909-18460020-01` (`complete_fulltext_read`); manifest `deepdive_manifests/PMID18460020.json` (34 locators — 22 text/table, 12 figure — strict PASS, 0 gaps)
**Source type:** primary experimental (oncology; no CNS material, no reference-genotype allele)
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** none — 🔴 **deliberately none.** Not linkable to `CLAIM 002` or `CLAIM 004`, for three independent reasons: reagent non-independence (below); the standing expression of concern on the source of those reagents; and an ex-vivo engraftment-**prevention** design, which is not rescue of an established neuronal phenotype. **Nothing about adenoviral or AAV WWOX delivery in a neuronal context may cite this paper.**
**Reagent provenance:** 🔴 Ad-WWOX, Ad-GFP, immunoblot anti-Wwox and IHC anti-Wwox are **all** cited to ref 21 = PMID 16223882 = [[paper_registry_current#PAPER 082]], which carries a **standing expression of concern** (PMID 28373548). This record exists largely to make that dependency visible rather than inherited: a per-PMID retraction check cannot see the integrity status of the papers a paper's *reagents* descend from.
**Note:** What is supportable from this paper: pWWOX raises Smad4 protein ~2.7×, surviving β-actin normalisation. What is **not**: that WWOX loss is an established early event in pancreatic precursor lesions; and post-transcriptional Smad4 regulation, whose mRNA arm is *"data not shown"* and is therefore `IPOTESI`. The paper has **no limitations section** — do not record one. Methodological defects recorded in the learned-gates registry, not as claims: invalid χ² across all seven Table 1 contingencies; undefined significance asterisk in Fig 5b; MOI-10 dose-decoupling; Fig 3b/3d without loading control; unadjusted survival claim; a burned-in `Neural invasion` panel label in Fig 4b(iii).

## PAPER 084
**Short title:** WWOX cis-regulatory variation and low plasma HDL-C in humans
**Full title:** WW-domain-containing oxidoreductase is associated with low plasma HDL-C levels
**Identifier:** PMID 18674750 / DOI 10.1016/j.ajhg.2008.07.002 / PMC2495060
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-18674750-01` (prior `FTR-20260811-18674750-01`, `inadequate_prior_coverage`); manifest `deepdive_manifests/PMID18674750.json` (41 locators over 12 fingerprinted artifacts, strict PASS, 0 gaps)
**Source type:** primary human genetic association study (non-coding regulatory variant; 9,798 subjects; 21-year prospective arm)
**Transferability:** T3 — `ESPANSIONE` toward the reference genotype and deliberately not more
**clinical relevance:** LOW
**Claim links:** none — no claim is created, modified or retired by this reading
**Note:** Lee JC, Weissglas-Volkov D, Kyttälä M, … Croce CM, **Aqeilan RI**, … Pajukanta P. *Am J Hum Genet* 2008 Aug;83(2):180–192. **The corpus's only human quantitative WWOX phenotype outside cancer and outside neurodevelopment**, which is why the record exists; it carries no neural endpoint and licenses no transfer to the reference genotype. Recorded production defect, explicitly **not** an integrity hold: in Table S2 the Reference Allele equals the Minor Allele in 5 of 21 rows (rs8050128 C/C, rs12918952 G/G, rs2288033 A/A, rs12828 G/G, rs391870 A/A), one of which — rs12918952 — is the nonsynonymous Ala179Val row. Retraction check re-run 2026-09-09 returns nothing.

## PAPER 085
**Short title:** WWOX interactome review (Salah/Aqeilan/Huebner 2010)
**Full title:** WWOX gene and gene product: tumor suppression through specific protein interactions
**Identifier:** PMID 20146584 / DOI 10.2217/fon.09.152 / PMC2832309
**Status:** processed
**Evidence depth:** 🔴 **`partial_fulltext_read`** — `FTR-20260909-20146584-01`; manifest `deepdive_manifests/PMID20146584.json` (15 locators, strict PASS, 0 gaps). **The label denotes an unretrievable surface, not a shallow reading:** the text was read in full and the downgrade is confined to two NIHMS figure images (`nihms-180622-f0001.jpg`, `nihms-180622-f0002.jpg`) that sit behind a PMC challenge, so `figures: captions_only`. The two figure locators carry `surface: body` and attest the caption text only, never the panel. Tracked as `FT-096`. Cost of the debt, measured: Figure 2 is the panel the text twice designates as its own signalling summary.
**Source type:** secondary — narrative interactome review (11 pages, 90 references, 2 figures, 0 tables, 13 sections). A **joint Aqeilan/Huebner review** — the WWOX group with the FHIT group — which is load-bearing for how it is weighted.
**Transferability:** T3 — `ESPANSIONE`
**clinical relevance:** LOW
**Claim links:** none
**Publication integrity:** no retraction, no expression of concern, no erratum.
**Note:** Promoted from `CORPUS-STUB-029`, placeholder preserved append-only. Recorded findings, none promoted to a claim: a p53 non-replication whose caveat is lost between this document and CMLS chapter 8; a directional conflict in which 2010 reports WWOX **reduced** after UV where 2014 reports it **increased**, both on unpublished data; the authors' own counter-case on intronic replication-stress deletions; the SDR domain declared functionally uncharacterised; and a hypomorph defined by argument rather than measurement. **Term screen over 29,965 characters:** `epilep`, `seizure`, `brain`, `CNS`, `WOREE`, `encephalopath`, `ataxia`, `intellectual`, `recessive`, `germline`, `neuro` all zero; `syndrome` ×4, all Bloom's/Fanconi. Recorded as a **chronological control** on the 2014 measurements, not as an independent confirmation.

## PAPER 086
**Short title:** WWOX in HTLV-I Tax tumorigenesis (NF-κB corner)
**Full title:** The tumor suppressor gene WWOX links the canonical and noncanonical NF-κB pathways in HTLV-I Tax-mediated tumorigenesis
**Identifier:** PMID 21115974 / DOI 10.1182/blood-2010-08-303073 / PMC3318777
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-21115974-01`; manifest `deepdive_manifests/PMID21115974.json` (35 locators, strict PASS, 0 gaps)
**Source type:** primary experimental (viral oncology; group Xiao, Pittsburgh — **not** the Aqeilan group)
**Transferability:** T3 — `ESPANSIONE`
**clinical relevance:** LOW
**Claim links:** → [[claim_registry_current#CLAIM 023]] (corroborates the *"not only by binding"* leg only)
**Note:** The first study in this corpus to place WWOX inside **viral** tumorigenesis, and the only one placing it in the **HTLV-I / NF-κB** corner. 🔴 **R4 blind locator audit run and NOT clean — 12 of 32 triples defective, one disqualifying — and the corrections are the substance of this record.** The candidate was going to assert that this paper supplies a partner in which binding is WW-independent *and rerouting is excluded*, thereby qualifying `CLAIM 023`'s mechanism. **That middle leg did not survive**: supplemental Figure S2A carries Myc-WWOX in all eight lanes with no WWOX-negative comparator, and its Input block carries Myc-WWOX, Hsp90 and LaminB but **no Tax input row** — it shows where the *complex* is recovered, never where Tax *goes*. The paper's assertion that WWOX does not relocalise Tax therefore rests on **unshown data** and is recorded as an author assertion, not a result. Two further findings the audit produced: the paper states *"all the mice had tumors by 18 weeks of age (Figure 1A)"* while **Figure 1A, read point by point at 700%, shows ~41% of that cohort still tumour-free at 18 weeks**, reaching 0% only at ~25 weeks; and the Results heading *"Knockout of p100/p52 **prevents** tumorigenesis"* stands against 10% tumour-free at 52 weeks, where the Discussion says *"reduce"* and the abstract says *"delays"*.

## PAPER 087
**Short title:** Editor's introduction to the CMLS 71(23) fragile-site special issue
**Full title:** Role of common fragile sites and corresponding genes in cancer development
**Identifier:** PMID 25238781 / DOI 10.1007/s00018-014-1716-y / PMC11113964
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-25238781-01`; manifest `deepdive_manifests/PMID25238781.json` (15 locators / 2 artifacts, strict PASS, 0 gaps)
**Source type:** 🔴 secondary — **EDITOR'S INTRODUCTION** to a nine-chapter multi-author review. Two pages, single-authored, no figure, no table, no supplement, 11 references, received and accepted the same day (2014-08-28). PubMed's publication types (*review-article, Review, Journal Article*) and the PMC `article-type="review-article"` both **over-describe** it. **It must not be weighted as a systematic review.**
**Transferability:** T3 — `ESPANSIONE`, and the honest form is that **no transfer is available from this literature layer, and the reading measures why**
**clinical relevance:** LOW
**Claim links:** none
**Publication integrity:** no retraction, no expression of concern, no erratum.
**Note:** 🔴 **The taxonomic finding this record exists to carry.** The document's opening paragraph assigns **human genetic disorders to *rare* fragile sites and cancer to *common* ones**. WWOX spans FRA16D, a **common** site; the reference genotype is a Mendelian recessive human genetic disorder of WWOX. **Measured over the 7,211-character body with the reference list separated off:** `epilep`, `seizure`, `brain`, `CNS`, `WOREE`, `encephalopath`, `ataxia`, `intellectual`, `recessive`, `syndrome`, `germline` and `neuro` occur **zero times each — twelve of twelve** — in the introduction to a review whose chapter 8 is entirely about WWOX. **Operational consequence, and it is the point:** any future reasoning of the form *"the fragile-site literature does not mention a neurological phenotype, therefore…"* is **invalid by construction**. The silence is predicted by the field's own taxonomy and carries no evidential weight.

## PAPER 088
**Short title:** CMLS chapter 8 — the field's dedicated WWOX review
**Full title:** The common fragile site FRA16D gene product WWOX: roles in tumor suppression and genomic stability
**Identifier:** PMID 25245215 / DOI 10.1007/s00018-014-1724-y / PMC11113097
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-25245215-01`; manifest `deepdive_manifests/PMID25245215.json` (21 locators / 5 artifacts, strict PASS, 0 gaps)
**Source type:** secondary — chapter 8 of the CMLS 71(23) common-fragile-site special issue, the field's own dedicated WWOX review. 11 pages, 109 references, 2 schematic figures, 1 partner table, 26 sections. Received and accepted the same day (2014-08-28), the special-issue signature. 🔴 Unlike its own editor's introduction ([[paper_registry_current#PAPER 087]], over-described) and unlike [[paper_registry_current#PAPER 090]] (under-described), **the metadata here is CORRECT**: `genre_discriminator.py` returns AGREES.
**Transferability:** T3 — `ESPANSIONE`
**clinical relevance:** LOW
**Claim links:** none
**Publication integrity:** no retraction, no expression of concern, no erratum; `commentscorrections` empty at 2026-09-09.
**Weighting:** authoritative as an **index** of what the field held in 2014 and of which primary source carries which claim; **carries no evidence of its own** — every datum is a restatement, two load-bearing steps rest on *unpublished data*, and Figure 2 is labelled *"Hypothetical model"* by its own authors.
**Note:** Promoted from `CORPUS-STUB-104`, placeholder preserved append-only. 🔴 **Restatement-fidelity result.** The editor's introduction to the same issue ([[paper_registry_current#PAPER 087]]) restated this chapter as *"Authors **conclude** that these observations indicate that WWOX is functionally required for cell homeostasis…"*. Chapter 8's own closing proposal is **near-verbatim the same sentence with one word changed**: it says *"we **propose**"*. Its Concluding remarks hedge three further times — *"it can be argued"*, *"might have important roles"*, *"it can be speculated"*. **The chapter delivers the content it was promised to deliver, at a weaker epistemic grade than the promise assigned it — and here the summariser and the summarised are the same person.** 🔴 **Measured absence.** Over the 31,756-character body: `epilep`, `seizure`, `brain`, `CNS`, `WOREE`, `encephalopath`, `intellectual`, `recessive`, `syndrome`, `germline` — **ten of twelve literally zero**; `ataxia` occurs once as the expansion of the ATM gene name; `neuro` occurs twice, **both inside Table 1 rows**, with zero occurrences in running prose. Field density measured 2026-09-09: `WWOX AND FRA16D` = 119; `WWOX AND (epilepsy OR encephalopathy)` = 118 — two literatures of comparable size and disjoint vocabulary. Citation defects recorded: Table 1's TAU row cites `[107, 108]` where [107] is PMID 21901168, a MEK/WOX1 T-cell leukaemia paper; and its GSK3β row cites PMID 22193544, the paper at the centre of dismissal case `D-14`.

## PAPER 089
**Short title:** Pleiotropic functions of WWOX (Abu-Remaileh 2015 review)
**Full title:** Pleiotropic Functions of Tumor Suppressor WWOX in Normal and Cancer Cells
**Identifier:** PMID 26499798 / DOI 10.1074/jbc.R115.676346 / PMC4692203
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-26499798-01`; manifest `deepdive_manifests/PMID26499798.json` (28 locators, schema v2, strict PASS, 0 gaps)
**Source type:** 🔴 secondary — a **REVIEW**. It is primary only for its own Figure 2B, a genotype schematic drawn by the authors, and as a **dated position statement** by the primary WWOX laboratory.
**Transferability:** T2 / T3
**clinical relevance:** INDIRECT
**Claim links:** → [[claim_registry_current#CLAIM 030]] (corroborates the P47R limb at genotype level, secondary weight only)
**Note:** Promoted from `CORPUS-STUB-044`, placeholder preserved append-only. **R4 satisfied — two independent blind locator audits run before this record.** Where this review restates a primary this corpus already holds — the ITCH/K63 biology of PMID 24550385 — it adds **no independent weight**, and no claim gains support from it on that route. Registered and deliberately **not** adjudicated: the second allele in trans with P47R is annotated three different ways across sources — Banne Table 1 `p.Asp16fs`, the review text *"exon 1 frameshift"*, and Figure 2B `A16*`. **No claim in the registry should carry either annotation as established.**

## PAPER 090
**Short title:** Hazan & Aqeilan 2015 — editorial, not review
**Full title:** Current questions and controversies in chromosome fragile site research: does WWOX, the gene product of common fragile site FRA16D, have a passive or active role in cancer?
**Identifier:** PMID 27551470 / DOI 10.1038/cddiscovery.2015.40 / PMC4979517
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-27551470-01`; manifest `deepdive_manifests/PMID27551470.json` (22 locators / 5 artifacts, strict PASS, 0 gaps)
**Source type:** 🔴 **EDITORIAL, NOT REVIEW** — and this field is the point of the record. The PMC deposit carries `article-type="editorial"` and subject `Editorial`; PubMed assigns publication type `Journal Article` with **no `Review` tag**. 17 references, five sections, no measurement of its own. **It must not be weighted as a systematic review**, and the dispatch that assigned it called it one.
**Transferability:** T3 — `ESPANSIONE`, and weaker than that word usually implies
**clinical relevance:** LOW
**Claim links:** none
**Publication integrity:** no retraction, no expression of concern, no erratum (PubMed esummary 2026-09-09; no `<related-article>`, no change-history event).
**Note:** 🔴 **Standing caution, and the reason the record is worth creating: this paper's restatements are not sources.** Of its 17 references this repository holds three at `complete_fulltext_read` and one partial. **On all four, checking changed something.** Ref 9 (PMID 17360458): datum faithful (10/58 vs 2/60), but the haploinsufficiency inference is transmitted **stripped of the source's own interpretive status**. Ref 12 (PMID 23370280): faithful on cytoplasmic retention, but **drops the source's headline** that WWOX *increases* ΔNp63α abundance while lowering its activity. Ref 7 (PMID 24510053): cited for a **loss-only framing the review itself contradicts** — that review reports *increased* WWOX in breast, gastric and prostate carcinomas. Ref 8 (PMID 25331887): the ITCH step's citation **points where this repository's own record does not**. The remaining 13 are unread and are **queued, not believed**.

## PAPER 091
**Short title:** WWOX controls hepatic HIF1α to suppress hepatocyte proliferation and neoplasia
**Full title:** WWOX controls hepatic HIF1α to suppress hepatocyte proliferation and neoplasia
**Identifier:** PMID 29724996 / DOI 10.1038/s41419-018-0510-4 / PMC5938702
**Status:** processed
**Evidence depth:** complete_fulltext_read — `FTR-20260909-29724996-01` (prior `FTR-20260810-29724996-01`, `inadequate_prior_coverage`); manifest `deepdive_manifests/PMID29724996.json` (38 locators, 13 new, schema v2, strict PASS, 0 gaps)
**Source type:** primary experimental (mouse conditional knockout, in vivo)
**Primary pathway:** P5 — metabolism / HIF1α–glycolysis
**Genotype/model:** `Wwox^ΔHep` (Alb-Cre × Wwox^fl/fl), DEN-induced HCC, ± high-fat diet — **not** a WWOX-DEE allele
**Transferability:** T3 toward the reference genotype (liver, carcinogen, neoplasia endpoint; **no neural endpoint anywhere in the paper**)
**clinical relevance:** INDIRECT
**Claim links:** → [[claim_registry_current#CLAIM 025]] as **qualifying** evidence. No new claim created.
**Publication integrity:** ordinary Author Correction attached — **PMID 30470736**, image duplication in the Fig 3A/3D H&E panels. Annotated, **no** `PUBLICATION_INTEGRITY_HOLD`. The erratum is not an annotation taken on trust: it was **read as its own assigned source in the same wave** (`FTR-20260909-30470736-01`, `complete_fulltext_read`, manifest `PMID30470736.json` PASS 0 gaps), and its declared scope was checked directly against this paper's 38 locators — **none of which sits on Fig 3A or 3D** (the only Figure 3 locator, `entries[7]`, reads panel F). **Any future locator on Figure 3A or 3D must be drawn from the corrected version and say so.** The read surface behind all 38 locators is verifiably post-correction: the 2026-09-09 deposit carries «This article has been corrected.» and a dated *Change history 11/23/2018* entry, both anchored as locators in the erratum's manifest. 🔴 The clean result is a fact about which panels this corpus happened to use, **not a safeguard**.
**Note:** Promoted from `CORPUS-STUB-073`, placeholder preserved append-only; `LIT-0096` completed. Constraints that travel with the record: **no neural transfer** (transfer verdict `ESPANSIONE`); **no therapeutic promotion of digoxin**; the only **quantified** mouse panel in this paper for WWOX loss in liver tumours is `Supplement Fig S1A`: **DEN-induced** tumours of control mice against parenchyma of the same mice, ~1.02 vs ~0.49 on a fold-change axis, n=3 vs n=3 and **no significance mark** — a direction with no declared statistic, not an established mouse datum. `Supplement Fig S1B` shows the same comparison by IHC in one representative animal and **quantifies nothing**. And there is **no measurement of any kind in carcinogen-free (spontaneous) liver tumours** (arm corrected and *adjacent* dropped in `BATCH_20260926_ALDAZ_R2`, `CC-20260912-29724996-02` + `CC-20260914-29724996-04`; the word is audited in `deepdive_manifests/PMID29724996.json` `entries[34]`); and **the human premise carries three cohort sizes** — 438, 434, 417 — so any record citing the TCGA analysis must name which number it used.

## PAPER 092
**Short title:** Published erratum to PMID 38182577 (WWOX/Myc osteosarcoma)
**Full title:** Correction: WWOX promotes osteosarcoma development via upregulation of Myc
**Identifier:** PMID 38355659 / DOI 10.1038/s41419-024-06518-8 / PMC10867017
**Status:** processed
**Evidence depth:** full text reviewed — `FTR-20260909-38355659-01` (`complete_fulltext_read`); manifest `deepdive_manifests/PMID38355659.json` (8 locators, strict PASS, 0 gaps)
**Source type:** **published erratum**, attached to PMID 38182577
**Transferability:** T3 — `ESPANSIONE`
**clinical relevance:** LOW
**Claim links:** none — **the source supports no biological proposition.**
**Note:** Read as a source in its own right, because reading a full text obliges a receipt. It establishes the corrected scope of PMID 38182577 from the deposit itself, closing that paper's `SCOPE_UNDECLARED` status: the erratum's body is four paragraphs, carries **no `<fig>` element**, and corrects **no item beyond an author name** — `Haji Yehya` → `Haj-Yahia`. Checked against the re-downloaded corrected deposit of the original article, whose `<article-title>` still reads *"WWOX promotes osteosarcoma development via upregulation of Myc"*, unchanged. 🔴 **The erratum had the opportunity to correct a title that asserts the opposite of its own paper's direction, and corrected a hyphen in a surname.** No `PUBLICATION_INTEGRITY_HOLD` is proposed.
## PAPER 093
**Short title:** Feng 2024 WWOX-DEE case report, variant of unclear significance
**Full title:** WWOX-related epileptic encephalopathy caused by a novel mutation in the WWOX gene: a case report
**Authors:** Feng D, Li Y, Zhang YT, Song YJ, Qin DY, Wang F
**Year:** 2024
**Source type:** case report
**Journal/source:** *Front Pediatr* 2024;12:1453778
**Identifier:** PMID 39416860 / PMC PMC11479972 / DOI 10.3389/fped.2024.1453778
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only; this record is outside that window and the reading is complete, so a reading-priority label has no verdict to carry here (`BATCH_20260920_002`)
**Status:** processed
**Record provenance:** read in full; corpus placeholder promoted to a PAPER record by `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01` (BATCH_20260920_002). `processed` and not `claim_linked`: this reading creates no claim.
**Evidence depth:** complete_fulltext_read — `FTR-20260810-39416860-01`; manifest `deepdive_manifests/PMID39416860.json` (11 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** clinical description / natural history — no pathway is measured in this paper
**Model/species:** human — one boy, onset at one month, death at six months
**Genotype/model:** 🔴 **SDR-domain missense, and its pathogenicity is NOT established by this paper.** The authors' own last sentence says so, and a second DEE-gene variant is present (`CACNA1A c.4646A>G p.Gln1549Arg`, heterozygous — the inheritance detail is in the published paper and in the reading manifest, and is deliberately not restated here). The phenotype is first-hand; the attribution to WWOX is not.
**Transferability:** T1 — human, and the allele class (SDR-domain missense) is the reference genotype's own. The VUS boundary is written into `Genotype/model` rather than used to demote the record: `gold_is_in_the_details` rule 3 is that disease context does not downgrade a paper.
**clinical relevance:** MODERATE — **proposed at MODERATE and not HIGH, deliberately.** The clinical course is informative for the disease class, and the causal attribution the record would need for HIGH is one the paper itself declines to make.
**Claim links:** none — this record carries a reading, not a claim
**Role:** **citation-fidelity reference point.** A downstream review (PMID 42128308 §9) presents this case as an established homozygous WWOX case and omits both the VUS classification and the `CACNA1A` co-variant.
**LIT link:** [[literature_tracking_log_current#LIT-0191]]
**Note:** 🔴 THE PAPER CONTRADICTS ITSELF ON THE NUCLEOTIDE. The running text and the PubMed abstract write `c.991C>A`; Table 1 and the Discussion write `c.911C>A`. The protein change `p.Ser304Tyr` settles it arithmetically against the abstract. Recorded, not resolved at source. The phenotype that survives whatever the variant's classification: refractory seizures from one month, no object tracking, no head control, bilateral hearing impairment, death at six months.

---

## PAPER 094
**Short title:** Steinberg 2026 WWOX-MYC organoids, neurogenesis, gene-therapy rescue
**Full title:** Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids
**Authors:** Steinberg DJ, Zonca A, Abdellatif D, Rosh I, Kustanovich I, Hidmi O, Manenti C, Maroun K, Stern S, Davila-Velderrain J, Aqeilan RI
**Year:** 2026
**Source type:** primary experimental — human iPSC neural organoids, scRNA-seq, isogenic CRISPR knockout plus patient-derived lines
**Journal/source:** *Brain* 2026
**Identifier:** PMID 42397075 / DOI 10.1093/brain/awag239
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only; this record is outside that window and the reading is complete, so a reading-priority label has no verdict to carry here (`BATCH_20260920_002`)
**Status:** processed
**Record provenance:** read in full; this PMID was in no registry at all, so the record is new, created by `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01` (BATCH_20260920_002). `processed` and not `claim_linked`: this reading creates no claim.
**Evidence depth:** complete_fulltext_read — ⚠️ **of an artefact that is no longer on this host.** The bytes that reading declares (sha256 `b6b44816bb5a029ad6dd3760dbf02ae94c5fcb69f8a9b5721f45c128bbf189a0`) are absent from every checkout, and a SHA-256 sweep of the host on 2026-10-04 (`evidence_presence.py --search`) recovered **none** of the sixteen absent artefacts of this reading, among them the published supplement that carries the detailed Materials and methods. A replacement article surface was acquired lawfully and free on 2026-10-04 (`files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf`, sha256 `9775f766f68929e05665aa572196f4889083b501dc7f6792f1b9243e7dc0fd4b`, 36 pp) and measured to be the **same document with different bytes**: all six figure digests reproduce byte for byte and all 15 body snippets verify verbatim, while the file digest differs and each of the 36 pages carries a download-dated stamp — the only difference found, 🔵 and the stamp is the *observed* difference rather than a proven cause, since no second download was compared. 🔴 **Thirteen of the fourteen supplementary-figure locators of that reading therefore quote bytes that exist nowhere.** `FTR-20260810-42397075-04`; manifest `deepdive_manifests/PMID42397075.json` (30 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** P3 — prenatal structure / neurogenesis
**Model/species:** human — iPSC-derived neural organoids: wild-type, isogenic WWOX-knockout, and patient-derived lines
**Genotype/model:** WOREE and SCAR12 patient lines carried alongside an engineered null; the paper names both syndromes
**Transferability:** T2 — patient-derived human cells carrying the real genotypes, which is stronger than a rodent model, but a model system and not a clinical observation. Every T1 record in this registry is human clinical evidence.
**clinical relevance:** HIGH — **gene therapy restored neuronal function** in the patient-derived organoids, normalising hyperexcitability and promoting maturation, without disturbing radial-glia populations.
**Claim links:** none — this record carries a reading, not a claim
**Role:** **the mechanistic organoid reading**: MYC as the top significantly upregulated gene in WWOX-deficient radial glia, and the cell-cycle route to reduced neuronal generation. ⚠️ **Two sentences of this paper are not what its own panels plot (2026-10-04, `CC-20261004W10-Y-PANEL-VS-TEXT-01`, measured against each panel's own axis ticks and re-measured by an independent blind audit).** (a) The running text assigns a *"prominent increase"* in radial glia to the knockout **and to WOREE** jointly — adding, fairly, that it is *"more pronounced in the WWOX-KO organoids"* — and calls SCAR12 *"similar to WT"*; panel 2F plots **WOREE's radial-glia deviation at about +0.05 to +0.08 log2FC, the smallest of the three and visually indistinguishable from zero**, while **SCAR12's is about −0.25**, larger in magnitude and of the **opposite sign**. *"Similar to WT"* therefore describes WOREE better than it describes SCAR12. (The radial-glia bar is a colour composite of the subtypes — verified as a yellow→orange→red gradient at 600 dpi — so its extent is the block's and not necessarily one fitted log2FC; the caveat applies identically to all three rows, so the *ordering* survives it.) (b) The abstract's *"accumulation of cells in the G2/M and S phases"* holds for the `S` (≈ +0.77) and `G2M` (≈ +0.50) bins of panel 4C while the separately plotted **`M` bin falls (≈ −0.37)**; that panel carries no error bars and no significance marks, being a point estimate from the single scRNA-seq experiment (`WWOX-KO n = 2396`, `WT n = 2152` cells). 🔵 Cell counts recomputed from panel D sum to the n printed on panel A: 5649 + 3020 + 3422 + 5916 = 18 007.
**LIT link:** [[literature_tracking_log_current#LIT-0417]]
**Note:** TWO BOUNDARIES CARRIED FROM THE READING. (1) The central composition phenotype is almost entirely in the ENGINEERED KNOCKOUT — Figure 2F plots a neuronal cell-fraction log2FC of about −2.4 against wild type, with the radial-glia block at about +1.0 (re-measured 2026-10-04 against the panel's own axis ticks and confirmed by two independent blind audits at −2.35/−2.38 and +0.98/+0.99, `CC-20261004W10-Y-ORGANOID-GLIA-01`; the earlier figures of −2.6 and +0.55 were read from a rendering of an artefact no longer on this host, and the knockout's radial-glia gain is the larger of the two corrections) — while the patient lines show near-normal composition with a maturation phenotype instead, inverting the early/late neuronal balance. Composition and maturation are separable and the paper shows them separately. 🔵 **A THIRD BOUNDARY, ADDED 2026-10-04 (`CC-20261004W10-Y-ORGANOID-GLIA-01`): this paper measures no glia.** No oligodendrocyte, astrocyte, OPC or microglial population is annotated — five cell labels only (`RG`, `oRG`, `cRG`, `NP`, `Neu`; n = 18 007 cells), with glial progenitors folded into the mixed radial-glia cluster the authors decline to resolve further — and no myelin, myelin protein, g-ratio, axon count or OPC quantification is measured anywhere (`OLIG`, `SOX10`, `PDGFRA`, `MBP`, `GFAP`, `AQP4`, `S100B`, `OPC`: zero occurrences each in the body; blind audit 2026-10-04, 6/6 triples SUPPORTED). Its one oligodendrocyte sentence cites a **gene-set enrichment bar** (`oligodendrocyte specification & myelin`, NES ≈ +1.3) in a contrast run in neuronal progenitors and neurons, in the same panel where `cholesterol production inhibition` and `glycerophospholipid biosynthesis` move the opposite way; the panel's own caption names neither term. 🔵 The only oligodendrocyte-lineage number in the paper is in **external public data** (Fig. 3B, human fetal single-cell at 16 post-conceptional weeks, not these organoids), where WWOX is highest in radial glia and **lowest, and tied, in `Oli` and `Mic`** (≈ 0.08 each on the blind re-measurement — the earlier 0.10/0.07 ordering is withdrawn). It therefore bears on neither [[claim_registry_current#CLAIM 003]] nor [[claim_registry_current#CLAIM 005]], and that is an **earned null**, not an omission. (2) 🔴 GUARD AGAINST A FALSE INFERENCE, recorded because it was one step away: Figure 5E shows canonical Wnt signalling among negatively-enriched GO processes and the A51 compound suppresses Wnt, but co-occurring enrichment is not a demonstrated mechanism.

---

## PAPER 095
**Short title:** Aldaz & Hussain 2020 review — WWOX loss of function across CNS disorders
**Full title:** WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders
**Authors:** Aldaz CM, Hussain T
**Year:** 2020
**Source type:** 🔴 **Review** — a secondary source. Under `epistemic_discipline` every number in it is a pointer to its cited primary, never a measurement.
**Journal/source:** *Int J Mol Sci* 2020;21(23):8922
**Identifier:** PMID 33255508 / PMC PMC7727818 / DOI 10.3390/ijms21238922
**Tier (FASE 1):** not applicable — the FASE 1 triage covered corpus papers 221–400 only; this record is outside that window and the reading is complete, so a reading-priority label has no verdict to carry here (`BATCH_20260920_002`)
**Status:** processed
**Record provenance:** read in full; corpus placeholder promoted to a PAPER record by `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01` (BATCH_20260920_002). `processed` and not `claim_linked`: this reading creates no claim.
**Evidence depth:** complete_fulltext_read — `FTR-20260806-33255508-01`; manifest `deepdive_manifests/PMID33255508.json` (8 locators, schema v2, strict PASS, 0 gaps)
**Primary pathway:** review across axes — no primary measurement of its own
**Model/species:** human and mouse, secondary — expression databases, Allen Mouse Brain Atlas, single-cell RNA-seq
**Genotype/model:** no allele of its own; it reviews SCAR12 (MIM 614322), EIEE28/WOREE (MIM 616211) and WWOX copy-number variants in ASD
**Transferability:** T2 — human CNS scope and on-axis syndromes, carried as a secondary source.
**clinical relevance:** MODERATE — it carries the **Q230P recurrence census**: eight reported WOREE cases from six families as of its cutoff.
**Claim links:** none — this record carries a reading, not a claim
**Role:** **secondary source carrying the Q230P recurrence census**, and the expression map that puts the highest WWOX levels in entorhinal cortex, basolateral amygdala, frontal-cortex layer 5 neurons and cerebellar granule and basket cells.
**LIT link:** [[literature_tracking_log_current#LIT-0031]]
**Note:** FOUR THINGS THE READING MARKS, each because the review states more carefully than it is usually cited as stating. The OPC observation is LINEAGE EXPRESSION and not evidence that WWOX acts cell-autonomously in oligodendrocytes. The LPS result is a descriptive expression response in public mouse microglia data. The GABA-synthesis finding is a reviewed primary result from Wwox-null hippocampus, not a new experiment here. And the WWOX–myelin connection is labelled by the authors themselves a SUGGESTION arising from assembled observations — the lipid and trafficking routes are two potential themes, not tested mediators. The authors also acknowledge explicitly that the molecular effects of most missense variants were unknown.

## PAPER 096
**Short title:** Chen 2021 — epitopo di superficie WWOX 286-299; la cellula che lo espone e quella che lo riceve
**Full title:** Normal cells repel WWOX-negative or -dysfunctional cancer cells via WWOX cell surface epitope 286-299
**Authors:** Chen Y-A, … Chang N-S
**Year:** 2021
**Source type:** primary — biologia cellulare + xenotrapianto; **endpoint interamente oncologici**
**Journal/source:** *Communications Biology* 2021;4:753
**Identifier:** PMID 34140629 / PMCID PMC8211909 / DOI 10.1038/s42003-021-02271-2
**Status:** processed
**Record provenance:** letto in batch `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION` (wave 2 e 5); segnaposto `CORPUS-STUB-150` promosso da `CC-20260920-PAPER34140629-PROMOTION-01` (`BATCH_20260921_001`). Il passaggio sul dominio SDR è stato ri-verificato dall'orchestratore contro l'artefatto in cache.
**Evidence depth:** `partial_fulltext_read` — ricevuta `FTR-20260920-34140629-01`; artefatto `files/fulltext/PMID34140629_PMC_MCPtext.txt`, 61 298 byte, `sha256 a2d6f1c1…`; **`figures: unavailable`, nessun pannello ispezionato** (in questo checkout non esiste rotta né al deposito JATS né a un'immagine). Per `D-14` nessun negativo affermato da una sola figura è aggiudicato.
**Primary pathway:** oncologia / segnalazione di superficie Hyal-2–WWOX
**Secondary pathway:** dominio SDR
**Model/species:** MEF murini `Wwox+/+` e `Wwox−/−`; linee tumorali umane; topo
**Genotype/model:** WWOX wild-type e cellule WWOX-deficienti; **nessun allele WWOX-DEE**
**Transferability:** **T3**
**clinical relevance:** **LOW**
**Claim links:** none — questo record porta una lettura, non una claim
**Role:** 🔴 **negativo registrato.** Ogni endpoint del paper è oncologico e **non genera alcuna claim**, deliberatamente. Il suo valore per questo modello è di chiudere una voce `not_processed` su un paper già letto — cioè di impedire che venga riletto — e di registrare che la rilevanza è bassa **senza gonfiarla per il fatto di essere stato promosso**.
**Note:** La promozione non aggiunge peso scientifico. Il record esiste perché un paper letto lasciato a `not_processed` è il modo in cui lo stesso paper viene riletto, cosa già accaduta due volte in questa settimana per esattamente questa ragione.

---

## PAPER 097
**Short title:** Carvalho 2022 — Zfra1-31 protegge neuroni in iperglicemia e abbassa pY33-WWOX; l'attribuzione causale a «inibizione di WWOX» resta aperta
**Full title:** WWOX inhibition by Zfra1-31 restores mitochondrial homeostasis and viability of neuronal cells exposed to high glucose
**Authors:** Carvalho C, Correia SC, Seiça R, Moreira PI — **tutti Università di Coimbra** (CNC / CIBB / IIIUC / Istituto di Fisiologia). Chang NS compare **solo in bibliografia** (rif. 16, 21, 22, 47), mai come autore
**Year:** 2022
**Source type:** primary — colture neuronali differenziate + braccio animale osservazionale
**Journal/source:** *Cellular and Molecular Life Sciences* 2022;79(9):487
**Identifier:** PMID 35984507 / PMCID PMC11071800 (**stub: corpo di lunghezza zero**) / DOI 10.1007/s00018-022-04508-7
**LIT link:** LIT-0093
**Status:** processed
**Record provenance:** segnaposto `CORPUS-STUB-070` promosso da `CC-20260921-PAPER35984507-PROMOTION-01` (`BATCH_20260921_002`). 🔴 **Acquisito NON per una rotta migliore ma perché l'operatore ha fornito il PDF e il supplementary**, dopo che ogni rotta automatica aveva restituito un corpo vuoto. Nessun toolchain PDF esiste in questo deployment: il testo è stato estratto con [`framework/scripts/pdf_text_extract.py`](../../../framework/scripts/pdf_text_extract.py), scritto per questa lettura.
**Evidence depth:** `partial_fulltext_read` ×2 — ricevute `FTR-20260921-35984507-01` (articolo, artefatto `files/fulltext/PMID35984507_OPERATOR_PDFtext.txt`, `sha256 b9a4e3e3…`; PDF sorgente `sha256 a7ce53cf…`) e `FTR-20260921-35984507-02` (supplementary, `sha256 2977c175…`; PDF sorgente `sha256 4430b209…`). **`figures: captions_only` in entrambe: nessun pannello ispezionato.** Per `D-14` nessun negativo affermato da una figura è aggiudicato qui; tutti i negativi sotto sono negativi **testuali**.
**Strumento validato prima di accettare uno zero:** controlli positivi tutti vivi — `SH-SY5Y` 3, `Western blot` 35, `Zfra1-31` 62, `WWOX` 112, `Seahorse` 4, `Goto-Kakizaki` 4, `ABN413` 1, `ab193624` 1; nel supplementary, a livello di **frase**: `mitochondrial membrane potential` 3, `caspase 3 activity` 1. 🔴 Un primo matcher più tollerante aveva prodotto `S8G = 1` da un **font program** — falso positivo individuato e corretto con una barriera binaria, regressione sotto test.
**Primary pathway:** P5 — metabolismo / mitocondri / redox (iperglicemia)
**Secondary pathway:** asse pTyr33-WWOX; direzione terapeutica dei peptidi Zfra
**Model/species:** SH-SY5Y umane differenziate (25 mM glucosio, 48 h; Zfra1-31 20 µM a 3 h «EI» o 24 h «LI»); ratti Goto-Kakizaki 6 e 12 mesi vs **Wistar di pari età** — **braccio animale puramente osservazionale, nessun animale ha ricevuto Zfra**
**Genotype/model:** WWOX **wild-type**; **nessun allele WWOX-DEE**, nessun CNS in sviluppo, nessun endpoint convulsivo
**Transferability:** **T3**
**clinical relevance:** **MODERATE — e la rilevanza è interamente di direzione terapeutica, non di meccanismo di malattia.** Vincola una classe di candidati; non descrive questa malattia.
**Claim links:** none — questo record porta una lettura, non una claim
**Role:** 🔴 **Il paper più richiesto della sessione, e la lettura lo ridimensiona nel punto esatto in cui era stato citato.** È **evidenza vera**: Zfra1-31 protegge neuroni umani differenziati su un pannello ampio e internamente coerente (vitalità, ΔΨm, respirometria Seahorse, danno ossidativo, fissione-fusione, MTCO1/ND1/VDAC, autofagia, Aβ, pTau, proteine sinaptiche, p53, caspasi-3) **abbassando il segnale pTyr33-WWOX**, e il risultato temporale — l'attivazione di WWOX **precede** il danno — è il suo reperto meglio sostenuto. **Ma il verbo del titolo non è dimostrato dai suoi dati.**
**Negativi testuali, articolo E supplementary, tutti zero:** `siRNA`, `shRNA`, `knockdown`, `knockout`, `CRISPR`, `silenc*`, `transfect*`, `lentivir*` — **nessun braccio genetico su WWOX**; `scrambled`, `S8G`, `inactive peptide` — **nessun controllo di specificità del peptide**; `bafilomycin`, `chloroquine`, `autophagic flux` — **nessun clamp di flusso autofagico**.
**🔴 Il reperto che un abstract non poteva dare:** la tabella anticorpi elenca **sia** `Anti-WWOX (phospho Y33) Abcam (ab193624)` **sia** `WWOX Merck Millipore (ABN413)` — un anticorpo per **WWOX totale era in casa** — e la normalizzazione dichiarata è *"β-actin was used as a loading control"*. **Nessun dato di WWOX totale è riportato in nessun punto**, e nessun rapporto pWWOX/WWOX compare in alcuna legenda. Un segnale pTyr33 su β-actina scende se scende la fosforilazione **o** se scende la proteina; poiché la zfration prende WWOX **come substrato**, il **~64 %** (braccio **LI**, appaiato a **~16 %** di vitalità) è esattamente la quantità che **non distingue** *«Zfra ha inibito WWOX»* da *«Zfra ha consumato WWOX»*.
**Controllo di specificità: «data not shown».** Verbatim: *"Zfra1-31 … does not affect mitochondria and cells function under control conditions (data not shown)."*
**Braccio animale — meglio controllato dell'abstract, e non monotono:** *"young animals (6-month-old) present increased levels of pWWOX (tyr33), when compared to **age-matched control rats** and to 12-month-old GK rats"* — corteccia ~+20 %, ippocampo ~2×. Ma a **12 mesi** il segnale corticale **scende ~20 %** e l'ippocampo non è significativo. Limite dichiarato dagli autori: *"Due to the limited amount of rat brain samples, we were unable to perform key experiments done in neuronal cells."*
**⚠️ `D-15` — l'unico risultato genetico su WWOX nel paper è di altri:** *"it was previously shown that inhibition of tyr33 phosphorylation by a **dominant-negative WWOX** was able to abolish apoptotic cell death in a MPP+ rat model for PD"* è una **citazione al rif. [18]**, cioè la linea già tenuta come `PMID 18371080` / `FT-109`. **Non va ri-vocalizzata come braccio genetico di questo paper**, e non è una seconda osservazione.
**Formulazione canonica, da usare ovunque questo paper venga citato:** *«Evidenza neuronale indipendente che Zfra1-31 è protettivo riducendo il segnale pY33-WWOX; l'attribuzione causale della protezione all'**inibizione** di WWOX resta irrisolta — nessuna perturbazione genetica ortogonale, nessun controllo con peptide inattivo, WWOX totale mai misurata.»*
**Effetto sul modello:** **nessuna claim.** Restringe una frase di [`peptide_intervention_audit_20260920.md`](../analysis/peptide_intervention_audit_20260920.md) e la voce `HYP-20260705-05`. **La conclusione terapeutica per il genotipo di riferimento non cambia e anzi si rafforza:** inibizione e consumo puntano nella stessa direzione dove il problema è *troppa poca* WWOX funzionale — resta **obiezione di categoria, non di dose**.
**Note:** `A9` è **chiuso**; nessuna ulteriore acquisizione serve. **REVIVAL_TRIGGER:** una pubblicazione che riporti **WWOX totale** accanto a pTyr33-WWOX sotto Zfra1-31, o un braccio genetico su WWOX accanto al peptide in modello neuronale — quella singola misura decide fra le due letture.

---

## PAPER 098
**Short title:** Ludes-Meyers 2007 — Wwox hypomorphic mice display a higher incidence of B-cell lymphomas and develop testicular atrophy
**Full title:** Wwox hypomorphic mice display a higher incidence of B-cell lymphomas and develop testicular atrophy
**Authors:** Ludes-Meyers JH, Kil H, Nuñez MI, Conti CJ, Parker-Thornburg J, Bedford MT, Aldaz CM
**Year:** 2007
**Journal/source:** *Genes Chromosomes Cancer* 2007;46(12):1129-1136
**Identifier:** PMID 17823927 / PMCID PMC4143238 / DOI 10.1002/gcc.20497
**Status:** processed
**Record provenance:** created by `BATCH_20260926_ALDAZ_R1` (2026-09-26): a full-text reading recovered from the VPS backup had no registry record at all; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-17823927-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID17823927.json`, dossier `fulltext_dossiers/PMID17823927.md`.
**Source type:** primary research — mouse genetics, long-term ageing/tumorigenesis cohort, histopathology; NIH author manuscript NIHMS222061
**Primary pathway:** P7 — gene therapy readiness / dose-threshold logic
**Model/species:** topo, un'unica linea gene-trap `Wwox^gt/gt` (ES XG218, 129/Ola); embrioni 10.5 dpc e adulti; **nessun tessuto neurale, nessun allele umano**
**Genotype/model:** gene-trap nell'introne 4: allele previsto produrre una proteina di fusione Wwox–β-geo che conserva i due domini WW e perde il dominio SDR — **previsione dalla mappa di dominio, non misura**; nessun allele WWOX-DEE
**Transferability:** **T3**
**clinical relevance:** **LOW**
**Claim links:** 032 — endpoint-bounded source, linked by `BATCH_20260926_ALDAZ_R6`
**Role:** La fonte primaria del **braccio ipomorfo** su cui poggia la frase finale del `Summary` di `CLAIM 032`, che oggi non la cita: dimostra che una riduzione globale massiccia di Wwox è compatibile con la sopravvivenza in adulto, **con sopravvivenza cumulativa significativamente ridotta** (P = 0.0188, Breslow). Non misura funzione, non misura cervello. **Il confronto con il `Summary` di `CLAIM 032`:** la proteina è **non rilevabile** in rene, timo, milza, fegato ed embrioni e **rilevabile solo nel testicolo** (mRNA ridotto dell'85–98%), non "bassa ma rilevabile"; **nessuna funzione è misurata**; e "vitale" va letto con il costo di sopravvivenza (23% dei `gt/gt` morti entro 18 mesi contro 0% dei WT, senza causa identificabile all'autopsia). La correzione del `Summary` è tenuta per il batch di `CLAIM 032`, da decidere insieme a `CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01` (stessa frase).
**LIT link:** [[literature_tracking_log_current#LIT-0418]]
**Note:** Manoscritto d'autore, non versione di record (efetch nega l'XML, Europe PMC `fullTextXML` 404, PDF dietro proof-of-work). **Le due tabelle supplementari (rapporti mendeliani; fertilità) sono irrecuperabili — ogni rotta Wiley 403** — quindi i due risultati che vi poggiano sono riportati come dichiarazioni degli autori con i conteggi non visti. Difetti interni misurati in questa lettura: il footnote maschile di Table 1 stampa `P = 0.23`, che è **la statistica χ² (0.231), non il suo P (0.63)**; la legenda di Fig. 2G dichiara `P < 0.005` per il gruppo vecchio, non raggiungibile da un rank-sum a n = 4 vs 4 (minimo bilaterale esatto 0.029); i denominatori tumorali (14, 14, 18) sono minori delle coorti di sopravvivenza (20, 19, 20) senza spiegazione; il fondo genetico F2 non è mai nominato; anti-CD3 è usato e nessun risultato CD3 è riportato; la legenda di Fig. 1 stampa `hm 5 Wwoxgt/gt` per `hm =` (difetto di conversione, non corretto). **Ciò che la lettura aggiunge:** nei pixel di Fig. 3 **nessuna curva scende sotto il 50% entro 104 settimane**, quindi nessuna mediana di sopravvivenza è raggiunta e l'osservazione si ferma a 2 anni — esiste una *sopravvivenza cumulativa ridotta*, non una *lifespan* misurata; il fenotipo tumorale è **solo femminile** (9/14 vs 3/15, χ² 5.85, P = 0.015 non corretto; maschi 5/14 vs 5/18); l'atrofia testicolare nei maschi anziani poggia su due animali su quattro; `Wwox` è fortemente espresso nelle cellule di Leydig WT. **Il cervello non è mai stato saggiato** in questo modello: l'assenza è di valutazione, non evidenza di un SNC normale.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-17823927-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-17823927-01` §2 and §4, re-derived on main's current text. The claim link the reading proposes (`CLAIM 032`) is **held for the claim batch**, together with every claim-text change; `Claim links` stays `none` until then. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record.

**Claim-link resolution (BATCH_20260926_ALDAZ_R6):** the earlier R2 assessment note describes the then-held state; the measured limits now appear in [[claim_registry_current#CLAIM 032]].

---

## PAPER 099
**Short title:** Ramos 2008 — Low levels of WWOX protein immunoexpression correlate with tumour grade and a less favourable outcome in patients with urinary bladder tumours
**Full title:** Low levels of WWOX protein immunoexpression correlate with tumour grade and a less favourable outcome in patients with urinary bladder tumours
**Authors:** Ramos D, Abba M, López-Guerrero JA, Rubio J, Solsona E, Almenar S, Llombart-Bosch A, Aldaz CM
**Year:** 2008
**Journal/source:** *Histopathology* 2008;52(7):831-839
**Identifier:** PMID 18452537 / PMCID PMC4151645 / DOI 10.1111/j.1365-2559.2008.03033.x
**Status:** processed
**Record provenance:** created by `BATCH_20260926_ALDAZ_R1` (2026-09-26): a full-text reading recovered from the VPS backup had no registry record at all; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-18452537-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID18452537.json`, dossier `fulltext_dossiers/PMID18452537.md`.
**Source type:** primary research — serie clinica retrospettiva monocentrica con immunoistochimica; NIH author manuscript NIHMS222064
**Primary pathway:** oncologia adulta / biomarcatore tissutale, fuori dagli assi del modello
**Model/species:** tessuto umano adulto: 101 tumori vescicali primari **non consecutivi** (81 TUR, 20 cistectomie) + 10 uroteli normali e 5 metaplasie squamose da non oncologici; **nessuna linea cellulare, nessun animale, nessun genotipo germinale, nessun materiale neurale**
**Genotype/model:** WWOX somatico; nessun allele WWOX-DEE
**Transferability:** **T3** — nulla verso il genotipo di riferimento
**clinical relevance:** **LOW**
**Claim links:** none — e l'assenza è il dato: nessuna claim poggia su questo lavoro e questa lettura non ne crea una
**Role:** Osservazione di associazione in oncologia adulta: la perdita di WWOX all'IHC accompagna grado (τ −0.319), stadio, dimensione e progressione in vescica, **bivariata, non aggiustata, di entità debole-moderata**; recidiva nulla e sopravvivenza globale non significativa (P = 0.053); i tre strati non sono un gradiente (il gruppo *moderato* ha le curve migliori). Utile come **parità delle fonti** e come conferma indipendente del pattern di marcatura (granulare citoplasmatico, mai nucleare) dell'anticorpo policlonale di questo gruppo. Nessun meccanismo.
**LIT link:** [[literature_tracking_log_current#LIT-0419]]
**Note:** Manoscritto d'autore, non versione di record (Europe PMC `fullTextXML` 404; PDF dietro proof-of-work). **Difetti interni misurati in questa lettura, che potrebbero essere stati corretti in bozza e vanno riverificati sulla versione di record prima di citarli fuori da qui:** la riga `Total` di Table 2 (18/33/50, 45.5%) contraddice il testo e le somme della sua stessa tabella (26/25/50; 50/101 = 49.5%); la legenda di Fig. 5 chiama il pannello C *tumour size* mentre il pannello mostra **Progression No/Yes, P = 0.029**; Fig. 5B etichetta lo stadio I/II/III e stampa `P = 0.004` dove il testo dà 0.003; l'età va 42-91 nel testo e 38-91 in Table 1; il punteggio combinato (intensità 0-3 × estensione 0-4) può valere solo 0,1,2,3,4,6,8,9,12, quindi la classe «moderato 5-7» contiene **il solo valore 6**; un errore di citazione attribuisce al rif. 11 (prostata) un risultato ovarico del rif. 10. **Le dimensioni d'effetto stanno solo in Fig. 4B**: τ-b di Kendall al massimo −0,319 (grado), −0,191 (progressione), −0,021 (recidiva). Nessun modello di Cox, nessuna correzione per molteplicità, nessuna statistica di concordanza fra osservatori, nessuna dichiarazione di cecità; 55% dei cistectomizzati è WWOX-basso (P = 0,024) e le curve di sopravvivenza non sono aggiustate per trattamento o stadio. Dipendenza segnalata: rif. 20 (PMID 16223882) porta un **Expression of Concern** — **citazione di sfondo, nessun reagente, metodo o dato riusato**. **Nota interpretativa sull'unità dell'anticorpo (`CC-20260914-15266310-01` §3 (a) [ref corrected 2026-09-28 from “§3a” · CC-20260928-SECTION-REFS-01], INFERENZA, non DATO):** questo manoscritto stampa una concentrazione `140 mg / ml` la cui unità non è risolvibile qui; lo stesso laboratorio, per il suo antisiero anti-WWOX, stampa **`140 μg/ml`** su una superficie JATS pulita della versione di record di PMID 15266310 (`CORPUS P244`), il che sostiene la lettura della stringa di qui come **micro perso** nella conversione del manoscritto, per quello che plausibilmente è lo stesso stock. Non prova che i due reagenti siano lo stesso lotto (quattro anni di distanza). **La stringa citata nel manifest e nel dossier di questa lettura resta com'è stampata** e non va alterata.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-18452537-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-18452537-01` §2–§4, re-derived on main's current text. The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record.

---

## PAPER 100
**Short title:** Zeng 2021 — Cigarette Smoke and Nicotine-Containing Electronic-Cigarette Vapor Downregulate Lung WWOX Expression, Which Is Associated with Increased Severity of Murine Acute Respiratory Distress Syndrome
**Full title:** Cigarette Smoke and Nicotine-Containing Electronic-Cigarette Vapor Downregulate Lung WWOX Expression, Which Is Associated with Increased Severity of Murine Acute Respiratory Distress Syndrome
**Authors:** Zeng Z, Chen W, Moshensky A, Shakir Z, Khan R, Crotty Alexander LE, Ware LB, Aldaz CM, Jacobson JR, Dudek SM, Natarajan V, Machado RF, Singla S
**Year:** 2021
**Journal/source:** *Am J Respir Cell Mol Biol* 2021;64(1):89–99
**Identifier:** PMID 33058734 / PMCID PMC7780991 / DOI 10.1165/rcmb.2020-0145OC
**Status:** processed
**Record provenance:** created by `BATCH_20260926_ALDAZ_R1` (2026-09-26): a full-text reading recovered from the VPS backup had no registry record at all; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-33058734-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID33058734.json`, dossier `fulltext_dossiers/PMID33058734.md`.
**Transferability:** not assessed in this registration — held with the reading's candidate
**clinical relevance:** not assessed in this registration — held with the reading's candidate
**Claim links:** none — held for the operator's decision on the reading's candidate
**Role:** the peer-reviewed leg that **splits**: vascular leak and histologic injury are significantly greater under both LPS and MRSA, and endothelial cells isolated from the same animals secrete more IL-6, KC and MCP-1 under MRSA; what does **not** reproduce is the cytokine leg **in BALF, in vivo**, measured twice (LPS and MRSA) with no significant difference on twelve bars per figure. The model is an endothelial conditional deletion with about 85% residual knockdown, which is **not** the intratracheal siRNA model of `PAPER 102` (PMID 28283473). 🔴 The "multi-tissue convergence" wording of `DL-MECH-012` is **not** withdrawn by this reading, and must not be recorded as if it were; its re-derivation belongs to the discovery-ledger batch.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-ALDAZ-C003-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the `Role` field is written from `CC-20260914-UNRECORDED-READS-01` §2.2, in the wording its VPS consultation (`SCI-CONSULT-20260914-C`, findings C5–C7; record kept in the backup) substituted, renumbered (`PAPER 094` on the VPS is `PAPER 102` here) and with its last sentence re-derived: the VPS attributed the convergence withdrawal to a VPS batch that never reached main. `Transferability`, `clinical relevance` and the rest of the assessment stay with `CC-20260913-ALDAZ-C003-01`, queued for the discovery-ledger batch; `Claim links` stays `none`, as the candidate proposes.

---

## PAPER 101
**Short title:** Ludes-Meyers 2003 — WWOX, the common chromosomal fragile site, FRA16D, cancer gene
**Full title:** WWOX, the common chromosomal fragile site, FRA16D, cancer gene
**Authors:** Ludes-Meyers, Bednarek, Popescu, Bedford, Aldaz (surnames as the dossier gives them)
**Year:** 2003
**Journal/source:** *Cytogenet Genome Res* 100(1-4):101-110
**Identifier:** PMID 14526170 / DOI 10.1159/000072844
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-130` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-14526170-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID14526170.json`, dossier `fulltext_dossiers/PMID14526170.md`.
**Source type:** **review-shaped article carrying its own primary data** — 8 figures, 0 tables, ~56 references, 10 published pages. 🔴 Neither available label fits: PubMed declares `['Journal Article']` with no Review tag, while the abstract says *"we will review"* **and** *"present evidence"*.
**Primary pathway:** **none** — methodological / reagent provenance. It measures no pathway.
**Model/species:** human cancer cell lines and mouse xenograft
**Genotype/model:** none — no WWOX allele of interest. WWOX-DEE did not exist as a described entity in 2003.
**Transferability:** **T3 (no transfer)** toward the reference genotype.
**clinical relevance:** LOW — unchanged, and correctly LOW at triage. Its value is entirely methodological and entirely upstream.
**Claim links:** none — the reading proposes none, deliberately: the paper licenses no claim in a WWOX-DEE disease model. What the corpus needs from it is a reagent **boundary**, and a boundary belongs in the records that lean on the reagent.
**Role:** **the terminus of this corpus's anti-WWOX antibody specificity citation chain** — `16941225 → {15982416, 15692750} → 14526170`, all three now read with receipts (`PAPER 106`, `PAPER 105`, `CORPUS P324`, this record).
**LIT link:** [[literature_tracking_log_current#LIT-0149]]
**Note:** The immunogen is stated **once**: *"a GST fusion to WWOX amino acid residues 12–94 containing both of the WW domains"*, which **reconciles** the two differing immunogen descriptions in `15982416` rather than adjudicating between them — insert and fusion partner, both true of one construct. Sole specificity control: Fig. 5A, `Peo/Vector` versus `Peo/WWOX` — a genetic null against a reconstituted positive, on one epithelial lysate. **No immunohistochemistry of any kind exists anywhere in the chain**, so the IHC-level control the tissue atlas (`PAPER 106`) presupposed does not exist at any point. 🔴 **Fig. 5A carries no molecular-weight marks of any kind** — a **panel attestation** (native resolution, re-rendered at 1100 dpi in the VPS verification `ALDAZ-VERIFY-W5`, record kept in the backup `06ee25a`), not a count over the body text; the paper's only two marks sit on Fig. 5B and read *"85 kd"* and *"39.5 kd"*. The *"~46 kDa"* attribution is therefore unverifiable on the panel that asserts it. 🔴 **The null lane is not blank**, and the residual band sits at **higher** molecular weight — whereas an exon-4–8-deleted WW-retaining product must be **smaller** than 46 kDa, so that band cannot be that product. The authors state the reagent *"will also detect proteins encoded by the aberrantly spliced mRNAs"* because its epitopes lie in the retained WW domains, so that epitope/deletion geometry is **the authors' own statement**, not an inference of ours; any reading of the Peo/PEO1 null as "expresses no WWOX protein" narrows to the authors' *"does not produce **full-length** WWOX"*. Three unpublished assertions (`unpublished observation`, `manuscript in preparation`, `data not shown`) are carried in the abstract or in figure captions **without** the qualifier the body gives them, and one caption cross-references *"Fig. 7a"*, a panel that does not exist.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-ALDAZ-B004-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260913-ALDAZ-B004-01` §1–§2, re-derived on main's current text, renumbered from the VPS record `PAPER 093` (VPS numbering). The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. The candidate's §3 (`DL-MECH-012` reagent parenthetical, which supersedes `CC-20260913-ALDAZ-B003-01` §3.1) and the `PMID16941225.md` §4 item 1 [ref corrected 2026-09-28 from “§4.1” · CC-20260928-SECTION-REFS-01] premise completion are **not** in this batch: they belong to the discovery-ledger batch. The candidate's own "verified by count" clause for the missing ladder is not carried (a text count cannot establish a panel absence).

---

## PAPER 102
**Short title:** Singla 2017 — Loss of lung WWOX expression causes neutrophilic inflammation
**Full title:** Loss of lung WWOX expression causes neutrophilic inflammation
**Authors:** Singla S, Chen J, Sethuraman S, Sysol JR, Gampa A, Zhao S, Machado RF
**Year:** 2017
**Journal/source:** *Am J Physiol Lung Cell Mol Physiol* 2017;312(6):L903–L911
**Identifier:** PMID 28283473 / DOI 10.1152/ajplung.00034.2017
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-091` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-28283473-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID28283473.json`, dossier `fulltext_dossiers/PMID28283473.md`.
**Source type:** primary experimental (murine airway siRNA + A549 mechanism arm)
**Primary pathway:** inflammatory signalling / lung
**Model/species:** 🔴 **acute intratracheal anti-WWOX siRNA, 10 mg/kg, one duplex with its sequence printed, in WILD-TYPE male C57BL/6 mice** — **not** a knockout and **not** whole-body. Mechanism arm in A549 cells only.
**Genotype/model:** no WWOX disease variant; no neural material of any kind
**Transferability:** T3 — compartment-bound; nothing reaches the reference genotype
**clinical relevance:** LOW — research only
**Claim links:** none — the reading proposes no claim link
**Role:** the antecedent of the WWOX–lung axis and the corpus's only source for a positive pulmonary inflammatory phenotype (the positive leg `DL-MECH-012` refers to); the paper `PAPER 100` (PMID 33058734) defines itself against by difference
**LIT link:** [[literature_tracking_log_current#LIT-0114]]
**Note:** **The phenomenon is real and broader than the corpus recorded:** WWOX knockdown **alone, with no stimulus**, carries the asterisk on **all eight** quantitative panels of Figure 1 — BALF leukocytes, neutrophils, total protein, FITC-dextran flux, IL-6, IL-1β, KC and MIP-2. 🔴 **But the scope the corpus attached to it was wrong:** the authors write *"acute, global knockdown of **lung** WWOX expression"*, and "global" is modified by "lung" in **all three** places they use it — the Introduction (*"global lung silencing"*), the Results **section heading** (*"Global loss of murine lung WWOX expression causes neutrophilic alveolitis"*) and the Discussion. Global **within the organ**, never whole-body; `knockout` occurs **zero** times. **Compartment is epithelium-weighted by an IMPORTED CITATION and not measured here:** *"the predominant cell type affected by intratracheal siRNA delivery is the alveolar epithelial cell (52)"*, inside the limitations paragraph. **No endothelial cell is measured anywhere.** **Limits carried into the record:** twelve mice per in vivo experiment split 6/6 then 3/3, so **n = 3 per group**, under a caption calling it *"n = 3 independent experiments"* — a replication structure the design does not contain; Methods say 54 h between siRNA and LPS while the Figure 1 caption says 72 h, neither marked as a correction; **one unreplicated siRNA, with off-target effects explicitly not excluded by the authors themselves**; no multiplicity correction across eight BALF endpoints; no declared blinding of the manual differential. **Mechanism:** c-Jun/AP-1 de-repression with IL-8-dependent neutrophil chemotaxis, established **in A549 cells only** and abolished by dual c-Jun silencing; bridged in vivo by a systemic JNK inhibitor that 🔴 **attenuates without normalising** (Fig. 5A ≈60→≈47 against control arms at ≈5–8), visible only in the panel. The compound is named three ways in one article (`SP100625`/`SP500125`/`SP600125`); the drawn axis glyph reads `SP600125`. *"Widespread pulmonary neutrophilic inflammation"* is **not** this paper's wording — `widespread` occurs zero times here; it is the sequel's phrase. This paper says *"neutrophilic alveolitis"* and *"neutrophil influx"*. Its mechanistic origin, `PMID 17178850`, is unread in this repository and queued at HIGH priority as `FT-183`.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-28283473-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-28283473-01` P1–P2, re-derived on main's current text, renumbered from the VPS record `PAPER 094` (VPS numbering). The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. The P2 scope wording ("all three" uses of *global*, not two) is the correction the VPS §21d consultation (`ALDAZ-CONSULT-READS-20260914`, delta B; record kept in the backup) applied. Not in this batch: P3 (the compartment-split formulation for `DL-MECH-012`, which the same consultation found must be re-derived because `PMID 33058734` is a split result, not "the negative") and the six non-canonical "whole-body" sites the candidate's §7 lists.

---

## PAPER 103
**Short title:** Bonin 2018 — VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX
**Full title:** VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX
**Authors:** Bonin F, Taouis K, Azorin P, Petitalot A, Tariq Z, Nola S, Bouteille N, Tury S, Vacher S, Bièche I, Ait Rais K, Pierron G, Fuhrmann L, Vincent-Salomon A, Formstecher E, Camonis J, Lidereau R, Lallemand F, Driouch K
**Year:** 2018
**Journal/source:** *BMC Biol* 2018;16(1):109
**Identifier:** PMID 30285739 / DOI 10.1186/s12915-018-0576-6
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-165` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-30285739-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID30285739.json`, dossier `fulltext_dossiers/PMID30285739.md`.
**Source type:** primary experimental (interaction biochemistry + cell biology + retrospective clinical series)
**Primary pathway:** P5 — trafficking / endomembrane
**Model/species:** HEK-293T, MDA-MB-468, HeLa, NIH3T3, A549; SCID mice n=10/group; 448 retrospective human breast tumours
**Genotype/model:** 🔴 **no neural material and no WWOX disease variant** — WWOX-DEE appears once, as a Background citation
**Transferability:** T3
**clinical relevance:** LOW — a breast-oncology axis measured in non-neural systems
**Claim links:** 026 — interaction limb only; no metabolic inference
**Role:** the **independent** WW1/PPPY measurement for VOPP1 that `PAPER 032` does not contain
**LIT link:** [[literature_tracking_log_current#LIT-0181]]
**Note:** 🔴 Three working documents called this paper *the only independent support* for VOPP1–WWOX via WW1/PPPY while it sat in the registry as an unscreened stub — real support with **no** registry record, the mirror image of a declaration without attestation. **What it measures:** WWOX–VOPP1 by three routes — yeast two-hybrid (ten clones, VOPP1 C-terminus), reciprocal co-IP of over-expressed proteins, **and an endogenous co-IP from MDA-MB-468 with an IgG control, neither partner over-expressed**, which is the one datum `PAPER 032` lacks. **Mutagenesis on both sides, and graded:** WWOX **Y33R** *"abolished"* the interaction (the authors' word), while of VOPP1's three PPxY motifs (PPYY¹¹⁹, PPAY¹⁵⁷, PPPY¹⁶⁵) **Y165A** leaves no detectable band, **Y157A** a reduced but present doublet, and **Y119A** retains binding, with a whole-cell-lysate row confirming every mutant is expressed. 🔴 The authors' own text puts the Y165 result as *"strongly affected"* and the motif as required for a *"robust"* interaction — *"abolished"* is their word for Y33R, **not** for Y165A. **DIRECTNESS IS NOT ESTABLISHED:** `recombinant` 0, `GST` 0, `purified` only of DNA, no biophysical measurement, and the paper never itself claims direct binding — so a bridging protein is excluded by nothing. **Asserted but not measured:** *"sequestration"* (static co-localisation only — no flux, transport or retention assay); VOPP1's transmembrane and signal-peptide motifs (predicted by TMHMM2.0/SignalIP); and *"only Y165 matters"*, which its own Figure 1e lane 7 contradicts. **Limits:** no blot declares a replicate count anywhere; Figure 4d's quantification has no error bars and no n; Figure 4e is in NIH3T3, printed in the panel and named nowhere in text or caption; the whole-cohort survival result is **not** significant (`P=0.09` over all 448), significance being confined to luminal and luminal B subsets; two different WWOX cut-offs are used in one paper (Table S1 dichotomises at `<1`/`>1`, 302/146; Figure 7a and the statistics section use `0.6`, 193/255), unreconciled; Table S3 is more precise than the text (p = 0.016, CI 1.26–9.24); in A549, VOPP1 drives death below the empty-vector baseline (~7.4% vs ~18.6%); the anti-VOPP1 antibody is raised in-house with no dedicated validation panel. **Dependency:** reference PMID 16223882 carries an Expression of Concern (PMID 28373548) — citation only, Background framing, no reagent, method or dataset reused. Its five VOPP1 antecedents are unread here and queued as `FT-185`–`FT-189`; 🔴 three of them propose **mutually competing** mechanisms, and `FT-187`, from which this corpus imports VOPP1's lysosomal identity, reports only **partial** co-localisation and casts doubt on the direct NF-κB route.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-30285739-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-30285739-01` §2 and §4, re-derived on main's current text, renumbered from the VPS record `PAPER 095` (VPS numbering). The claim link the reading proposes (`CLAIM 026`) is **held for the claim batch**, together with every claim-text change; `Claim links` stays `none` until then. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. The Y165A/Y157A grading is the correction the VPS §21d consultation (`ALDAZ-CONSULT-READS-20260914`, delta A; record kept in the backup) applied to the candidate's "only Y165A abolishes". The candidate's §3 sentence for `CLAIM 026` is held with the link.

---

## PAPER 104
**Short title:** Ludes-Meyers 2004 — WWOX binds the specific proline-rich ligand PPXY: identification of candidate interacting proteins
**Full title:** WWOX binds the specific proline-rich ligand PPXY: identification of candidate interacting proteins
**Authors:** Ludes-Meyers JH, Kil H, Bednarek AK, Drake J, Bedford MT, Aldaz CM
**Year:** 2004
**Journal/source:** *Oncogene* 2004;23(29):5049–5055
**Identifier:** PMID 15064722 / DOI 10.1038/sj.onc.1207680
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-143` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; title, authors and pages from the article metadata of the reading's artefact `files/fulltext/PMID15064722_LudesMeyers2004_efetch.xml` (the dossier header gives only `Ludes-Meyers et al. 2004`)
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-15064722-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID15064722.json`, dossier `fulltext_dossiers/PMID15064722.md`.
**Source type:** primary experimental (WW-domain interaction biochemistry) — NIH author manuscript NIHMS222052
**Primary pathway:** P3 — interaction logic / WW-domain scaffold
**Model/species:** *in vitro* throughout — bacterially expressed GST–WW-domain fusions, synthetic biotinylated peptides, His-tagged candidates in *E. coli* — plus **one** mammalian line, **MCF-7** human breast cancer (the GST pull-down of endogenous SIMPLE, and the immunofluorescence). 🔴 **The paper's own *"in vivo"* means *in MCF-7 cells*: there is no animal and no in vivo binding experiment.**
**Genotype/model:** no WWOX disease variant. 🔴 **No neural cell, tissue or system** — and the one neural element must not be recorded as nothing: the screen substrate is a **human brain cDNA library of 27 648 clones**, expressed as **bacterial** fusion proteins.
**Transferability:** T3 — domain logic only; nothing here reaches the reference genotype
**clinical relevance:** LOW — 2004 cancer-cell-line and peptide biochemistry with no neural, animal or clinical measurement. Its value to this corpus is **provenance and mechanism, not clinical directness**, and provenance weight is deliberately not written into this field.
**Claim links:** 007 — mechanistic antecedent only; the P47T assay is `PAPER 007`.
**Role:** bounded antecedent for `CLAIM 007`: tested WW1 binding to the WBP-1 PPPY peptide and endogenous SIMPLE recovery in MCF-7. Four ligands and eight WW-domain constructs were compared in vitro. It does not test P47T, neural tissue or DVL2; the two-oligopeptide P47T result is `PAPER 007`'s.
**LIT link:** [[literature_tracking_log_current#LIT-0162]]
**Note:** WW1 binding is demonstrated for the tested WBP-1 PPPY peptide; WW1 is required and sufficient for endogenous SIMPLE recovery in MCF-7 under the reported pull-down conditions, with WBP-1 and SIMPLE mutagenesis. The biotinylated peptide is 14 residues and contains a nine-residue WBP-1 core. Four candidate proteins were far-Western-confirmed; a fifth clone remained unidentified at publication. Figure 2 uses duplicate-positive colonies as a qualitative selection criterion. Uncircled spots do not establish additional validated partners. Figure 1b has faint CDC25-row WW-domain signal, so an absolute no-ligand WW2 conclusion is not supported. The paper provides no quantitative affinity or neural/P47T test. The receipt names the PDF while text locators resolve to its declared HTML-derived reading surface; both digests remain recorded. The formerly inaccurate manifest entries 4, 19 and other audited propositions were corrected in `BATCH_20260926_ALDAZ_R7` after the blind locator audit. PMID 7644498 remains an unread antecedent.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-15064722-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260913-15064722-01` §1 and §3, re-derived on main's current text, renumbered from the VPS record `PAPER 096` (VPS numbering). The claim link the reading proposes (`CLAIM 007`, as its mechanism primary) is **held for the claim batch**, together with every claim-text change; `Claim links` stays `none` until then. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. Held with the link: the candidate's §2 (a `Source` addition and three boundaries in `CLAIM 007`'s `Genotype/model relevance`, which touch a consolidated-baseline claim and owe a blind locator audit first), its §4 dismissal negatives and its §5 reading debt.

---

## PAPER 105
**Short title:** Nunez 2005 — WWOX protein expression varies among ovarian carcinoma histotypes and correlates with less favorable outcome
**Full title:** WWOX protein expression varies among ovarian carcinoma histotypes and correlates with less favorable outcome
**Authors:** Nunez, Rosen, Ludes-Meyers, … Aldaz (as the dossier gives them)
**Year:** 2005
**Journal/source:** *BMC Cancer* 5:64
**Identifier:** PMID 15982416 / DOI 10.1186/1471-2407-5-64
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-148` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-15982416-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID15982416.json`, dossier `fulltext_dossiers/PMID15982416.md`.
**Source type:** primary descriptive immunohistochemistry + immunoblot series on pooled tissue microarrays (444 invasive epithelial ovarian carcinomas, two institutions; 38 tumours and 5 normal ovaries by immunoblot). **Not an experiment:** no intervention, no genotype, univariate statistics only.
**Primary pathway:** baseline expression / tumour-tissue protein loss — **and explicitly not P5**: the paper measures no steroid, no receptor function and no enzyme activity
**Model/species:** human adult ovarian tumour and normal ovarian tissue
**Genotype/model:** none — human somatic tumour tissue, no WWOX allele
**Transferability:** **T3**, `ESPANSIONE` toward the reference genotype, and deliberately not more
**clinical relevance:** LOW — unchanged, and correctly LOW at triage
**Claim links:** none — the reading proposes no claim link
**Role:** the reagent paper of record for this corpus's **immunoblot-grade** anti-WWOX antibody validation (one of the two papers the tissue atlas `PAPER 106` delegates specificity to; it delegates onward to `PAPER 101`)
**LIT link:** [[literature_tracking_log_current#LIT-0166]]
**Note:** Evidence surface: **17 of 17 panels inspected as images** at native resolution off the publisher's ESM originals. Contains the paper's own unresolved question — whether the WWOX–PR association is a consequence of histotype composition — **left open by the authors and left open by this reading**. Text/table discrepancy recorded, not an integrity hold: Table 2's PR cell prints `p = 0.00` where Results and Abstract both give `p = 0.008`. Survival association is **univariate and unadjusted** (`p = 0.03`), with the authors themselves offering stage and histotype composition as alternative explanations. Immunohistochemistry carries a pre-absorption control asserted as *"data not shown"*; the reagent's own characterisation is delegated to `PMID 14526170` (`PAPER 101`, now read: immunoblot grade, no IHC control anywhere in the chain). The "internal tension" over its two immunogen descriptions is **dissolved, not adjudicated**, by `PAPER 101`: both are true of one construct, epitope N-terminal.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260913-ALDAZ-B003-01` §1.1, re-derived on main's current text. The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. The candidate's §3.1 (`DL-MECH-012` parenthetical) is superseded by `CC-20260913-ALDAZ-B004-01` §3.1, which stays queued for the discovery-ledger batch.

---

## PAPER 106
**Short title:** Nunez 2006 — WWOX protein expression in normal human tissues
**Full title:** WWOX protein expression in normal human tissues
**Authors:** Nunez, Ludes-Meyers, Aldaz (as the dossier gives them)
**Year:** 2006
**Identifier:** PMID 16941225 / DOI 10.1007/s10735-006-9046-5
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-107` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-16941225-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID16941225.json`, dossier `fulltext_dossiers/PMID16941225.md`.
**Source type:** primary descriptive immunohistochemistry atlas (tissue microarrays + whole sections, >30 organs; one five-lane immunoblot). **Not an experiment**: no intervention, no genotype, no statistics.
**Primary pathway:** baseline expression / tissue and cell-type distribution
**Model/species:** normal adult human tissue
**Genotype/model:** none — no WWOX allele
**Transferability:** **T3**, baseline expression only
**clinical relevance:** LOW (background)
**Claim links:** none — the reading proposes none, deliberately: a map of where a protein sits in adult human tissue under one antibody carries no allele, dosage, development or disease
**Role:** the baseline tissue and cell-type expression map the corpus's tissue arguments were resting on while it was unread (`FT-057`, 2026-08-10) — now read, and narrower than that use implied
**LIT link:** [[literature_tracking_log_current#LIT-0127]]
**Note:** **Every CNS cell-type call in it is text- and table-only** (18 IHC panels, not one of them CNS), on **two cores per brain region**, with **no negative control anywhere**; antibody specificity is delegated to two papers (`PAPER 105`, `CORPUS P324`), both now read, which delegate onward to `PAPER 101` — the chain terminates at immunoblot grade with **no immunohistochemical control anywhere in it and no neural validation**. Its own Table 1 contradicts its Results on limbic cortex. Skeletal muscle is *"inconclusive"*, not negative. Fig 1 carries a **brain** band the running text never mentions. *"Capillaries were consistently negative in all the organs analyzed"*; the word *microglia* does not occur in the paper in any form — **its silence is not a negative**; astrocytes are reported WWOX-positive (text and table only, two cores, no co-marker — a baseline observation, not an activation marker). **What must NOT be done with this reading:** (1) do not close `CLAIM 003`'s open oligodendrocyte question — *"Oligodendrocytes showed no WWOX immunoreactivity"* is adult human, two cores, no panel, no marker, no negative control; (2) do not carry "skeletal muscle negative"; (3) do not quote the Discussion's hormonal-tissue hierarchy as measured — it is a qualitative ranking of categorical grades on duplicate cores; (4) do not treat `DL-MECH-010`'s AAV-transgene negatives in mouse as the same fact as this paper's endogenous human negatives (hepatocytes here are strongly positive). A blind locator audit of the seven highest-risk triples ran on the VPS (keep 5, soften 2, withdraw 0); the three manifest entries it revised (`entries[24]`, `[28]`, `[36]`) carry their declared `contradicts_locator` and the audit object in `deepdive_manifests/PMID16941225.json`, and none bears on the points above.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-16941225-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260913-16941225-01` §1, §2 and §4, re-derived on main's current text. The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. Not in this batch: the candidate's §3 compartment-boundary paragraph on `DL-MECH-012` (discovery-ledger batch).

---

## PAPER 107
**Short title:** Ferguson 2012 — Conditional Wwox deletion in mouse mammary gland by means of two Cre recombinase approaches
**Full title:** Conditional Wwox deletion in mouse mammary gland by means of two Cre recombinase approaches
**Authors:** Ferguson BW, Gao X, Kil H, Lee J, Benavides F, Abba MC, Aldaz CM
**Year:** 2012
**Journal/source:** *PLoS ONE* 2012;7(5):e36618
**Identifier:** PMID 22574198 / DOI 10.1371/journal.pone.0036618
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-168` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-22574198-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID22574198.json`, dossier `fulltext_dossiers/PMID22574198.md`.
**Source type:** primary research — genetica murina condizionale (sopravvivenza, morfometria, trascrittoma)
**Primary pathway:** P7 — gene therapy readiness / dose-threshold logic (the mammary leg of `CLAIM 032`'s threshold); secondary: oncology / tumor suppressor biology
**Model/species:** topo, allele `Wwox flox/flox` con **esone 1** floxato; driver **BK5-Cre** (K5, attivo da E13.5) e **MMTV-Cre linea D**; fondo misto 129SV/C57Bl/6; organoidi mammari; trapianto in SCID. **Nessun tessuto nervoso esaminato in alcun topo**
**Genotype/model:** delezione somatica tessuto-ristretta, omozigote ed eterozigote; **nessun allele WWOX-DEE, nessuna eterozigosi germinale**
**Transferability:** **T3** per il contenuto mammario e oncologico; **T2 indiretta** per il solo confine di dose
**clinical relevance:** **MODERATE** — è il primario dietro un leg di un claim `VERY HIGH`, non una fonte clinica in proprio
**Claim links:** 032 — endpoint-bounded source, linked by `BATCH_20260926_ALDAZ_R6`
**Role:** **fonte primaria** (rif. 55) della frase della review Aldaz 2014 (`PAPER 053`) che la Note di `PAPER 053` elenca fra le citazioni chiave per `CLAIM 032` — *"loss of a single Wwox allele… did not have any observable phenotypic effect in the mammary gland"*. Vale per **sopravvivenza, tumori e istologia premaligna** degli eterozigoti; **non** per il branching, che non ha alcun gruppo eterozigote. 🔴 Il *"lifespan of the Wwox heterozygotes was indistinguishable from WT mice"* della review **non è attribuibile a questo lavoro**: gli eterozigoti qui sono **`BK5-Cre; Wwox +/fl`**, somatici e tessuto-ristretti, con sopravvivenza tracciata solo fino a ~giorno 118 (n = 41, 100%). ⚠️ **~45% della perdita di branching è attribuibile al solo Cre** (Cre(−) WT ≈ 5.45, Cre(+) WT ≈ 4.05, KO ≈ 2.35 rami/mm), e i controlli MMTV accorpano Cre(+) e Cre(−). **Lead aperto, non promosso:** tutti i 22 `BK5-Cre; Wwox fl/fl` muoiono fra il giorno 68 e il 117, causa non determinata (DATO); una ricombinazione di BK5-Cre fuori dall'epitelio bersaglio è un'IPOTESI del lettore con premessa `DEFAULT_FROM_TEXTBOOK`, **assenza di valutazione, non evidenza di un fenotipo neurale**. `REVIVAL_TRIGGER`: istologia cerebrale, EEG o osservazione di crisi in `BK5-Cre; Wwox fl/fl`, o una mappa di ricombinazione della linea BK5-Cre.
**LIT link:** [[literature_tracking_log_current#LIT-0184]]
**Note:** Difetti misurati in questa lettura: la **media di 115 giorni dichiarata per i KO BK5 è aritmeticamente impossibile** — con una morte al giorno 68 e nessuna dopo il 117, il massimo possibile per n = 22 è 114.8, e la mediana della curva è ~100; i box plot qPCR danno p < 0.001 su 3 topi per gruppo, il che suggerisce che i triplicati tecnici siano stati contati come osservazioni (INFERENZA); **Table S1 eccede il proprio cutoff** (sonda Stat3 p = 0.0102; 19 sonde su 913 con p > 0.01); cicli PCR 24/26/28/32 in legenda contro 24/28/32 nei Methods; follow-up del trapianto 9 mesi nei Results e 10 nei Methods; il Western pStat3 dichiarato *"significant increase"* è **senza densitometria e senza statistica**, con Stat3 totale più alto in un KO. La delezione dell'esone 1 lascia **~13–15% di segnale mRNA residuo** negli organoidi e una sonda 3′ dell'array solo 2–3× ridotta, origine non determinata. Il follow-up degli eterozigoti MMTV *"beyond one year"* è dichiarato **senza numeri e senza patologia mostrata**. Dipendenza segnalata: PMID 16223882 (Expression of Concern) — citazione di sola introduzione, nessun topo, reagente o analisi ne dipende. Debito di lettura portante: **PMID 21499303** (Abdeen 2011), il risultato sugli eterozigoti che questo lavoro contesta esplicitamente, senza ricevuta.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-22574198-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-22574198-01` §3 and §4, re-derived on main's current text. The claim link the reading proposes (`CLAIM 032`) is **held for the claim batch**, together with every claim-text change; `Claim links` stays `none` until then. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. Held with the link: the `PAPER 053` `Note` append (ref-55 boundary now attested — that `Note` on main does not yet carry the boundary the candidate appends to), the `CLAIM 032` `Source`/`Wikilinks` and optional limit, and the `FT-181` closure.

**Claim-link resolution (BATCH_20260926_ALDAZ_R6):** the earlier R2 assessment note describes the then-held state; the measured limits now appear in [[claim_registry_current#CLAIM 032]].

---

## PAPER 108
**Short title:** Ferguson 2013 — The cancer gene WWOX behaves as an inhibitor of SMAD3 transcriptional activity via direct binding
**Full title:** The cancer gene WWOX behaves as an inhibitor of SMAD3 transcriptional activity via direct binding
**Authors:** Ferguson BW, Gao X, Zelazowski MJ, Lee J, Jeter CR, Abba MC, Aldaz CM
**Year:** 2013
**Journal/source:** *BMC Cancer* 2013;13:593
**Identifier:** PMID 24330518 / DOI 10.1186/1471-2407-13-593
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-055` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-24330518-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID24330518.json`, dossier `fulltext_dossiers/PMID24330518.md`.
**Source type:** primary research — biologia cellulare + trascrittoma + co-IP/pull-down, **con una coda di meta-analisi** su 819 tumori mammari pubblici (da cui il tag `Meta-Analysis` di PubMed: la meta-analisi è una sezione, non il disegno)
**Primary pathway:** architettura di dominio / interpretazione delle varianti; secondaria: TGF-β/SMAD signalling
**Model/species:** linee epiteliali mammarie umane MCF10 e 184B5, linea tumorale MCF7; dataset di espressione tumorale pubblici. **Nessun animale, nessun genotipo germinale, nessun materiale neurale**
**Genotype/model:** WWOX wild-type più il mutante di dominio **`W44F/P47A`** (WW1) come reagente; **nessun allele WWOX-DEE**
**Transferability:** **T3** per il contenuto oncologico mammario; **T2 indiretta** per il solo dato di dominio
**clinical relevance:** **INDIRECT-LOW**
**Claim links:** none — the reading proposes none: a new claim would need a second, independent source in a system other than one breast epithelial line at overexpression
**Role:** fonte primaria di un **partner WW1-dipendente** (SMAD3, motivo PPGY): co-IP **endogena** in MCF10 e pull-down GST-WW1+2 di Flag-SMAD3. ⚠️ **Il mutante WW1 `W44F/P47A` non abolisce il legame**: lascia una banda residua debole ma visibile, e il carico dell'esca non è mostrato — il testo dice *lost*, il pannello dice *ridotto*. **Contesto, non emendamento:** coerente con `CLAIM 024` e niente di più (costrutto WW1+2 in tandem, mutato solo WW1: non separa i due domini e non dice nulla sulla cooperatività); adiacente e non sovrapposto a `CLAIM 026`; SMAD3 ≠ SMAD4 di `CLAIM 027`. Il sequestro citoplasmatico come meccanismo è IPOTESI degli autori (nessun frazionamento, nessun saggio di import, una sola cellula mostrata). Per il resto contesto oncologico.
**LIT link:** [[literature_tracking_log_current#LIT-0079]]
**Note:** ⚠️ Difetti misurati in questa lettura, non dichiarati dagli autori: **SMAD3 è al rango 7**, non fra i primi quattro, nel foglio ChEA degli autori stessi (E2F4, SOX2 umano, MYC murino 71.85, E2F1 umano, SOX2 murino, E2F1 murino, poi SMAD3 54.78) — la Figura 2C mostra i primi quattro **umani**, un filtro non dichiarato; **PTHLH in MCF7 scende di ~20 volte** mentre la legenda lo chiama l'unica eccezione all'aumento, cioè direzione opposta e non un nullo; nella ChIP il **controllo IgG supera il segnale SMAD3** nella condizione WWOX + TGF-β al promotore ANGPTL4 (~1.1 contro ~0.45); il reporter è detto *"significant"* **senza alcun test**; **nessuna barra SEM visibile** sulla barra shWWOX benché la legenda dichiari tre esperimenti ± SEM; unità incoerenti (TGF-β1 *"20 ng/μL"* per il confocale contro 10 ng/mL altrove; tampone co-IP *"50 nM Tris–HCl"*); *"induction of WWOX"* nei Results descrive una **trasfezione transiente** nei Methods; il knockdown *"80–90%"* non è quantificato; la correlazione WWOX–ANGPTL4 nei dati pubblici è detta significativa **senza coefficiente né P**, e i cluster sono costruiti su quei due geni stessi.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-24330518-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-24330518-01` §2–§4, re-derived on main's current text. The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record.

---

## PAPER 109
**Short title:** Schrock 2017 — Wwox–Brca1 interaction: role in DNA repair pathway choice
**Full title:** Wwox–Brca1 interaction: role in DNA repair pathway choice
**Authors:** Schrock et al. (13 authors per the dossier)
**Year:** 2017
**Journal/source:** *Oncogene* 2017;36(16):2215–2227
**Identifier:** PMID 27869163 / DOI 10.1038/onc.2016.389
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-046` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-27869163-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID27869163.json`, dossier `fulltext_dossiers/PMID27869163.md`.
**Source type:** primary research, experimental (cell biology + xenograft + public-database re-analysis)
**Primary pathway:** DNA-damage response / genome stability: DSB repair-pathway choice (HR/SSA vs NHEJ), WWOX–BRCA1 axis
**Model/species:** whole-body `Wwox−/−` mouse MEFs; human cancer and immortalised lines
**Genotype/model:** no WWOX-DEE allele
**Transferability:** **T3** — oncology cell biology, no neural or developmental system
**clinical relevance:** LOW — unchanged, and the reason is now on the record
**Claim links:** none — the reading proposes no claim link
**Role:** the primary behind the WWOX–BRCA1 repair-pathway-choice reading the discovery ledger carries (`DL-MECH-024`, `DL-METH-094`), which the corpus had held only through a review's one-sentence summary
**LIT link:** [[literature_tracking_log_current#LIT-0070]]
**Note:** **The end-resection step is a correlate, not a measurement, in this source:** there is no resection assay of any kind (no ssDNA quantification, no SMART, no resection tracts); the phrase rests on RPA32/Rad51 foci counts plus the authors' own *"we hypothesize"*, and **Figure 7c prints a `?` beside the Wwox→MRN arrow**. The direct measurement exists in `PAPER 111` (SMART, mouse). The foci correlate is narrower in time than it reads: RPA32 inverts at 3 h, Rad51 already differs at 0 h **before irradiation**. The `981PPLF984` localisation **fails on the paper's own mutants** (residue 981 lies only in ΔM2; ΔM1 also loses binding and is unexplained; the IgG control lane is positive for Wwox in ΔC). NHEJ and Alt-NHEJ are enhanced and HDR and SSA impaired across four integrated reporters in four host lines, each with its own baseline — **no experiment has two pathways compete for the same break**, so "dominance" is not what was measured. Supplementary Figure 5 (the reciprocal co-IP) could not be adjudicated lane by lane, so the text's *"confirmed in the opposite direction"* is unverified here. The MEF establishment protocol is in ref 35 (PMID 24244712), not in this paper; `KO4` appears nowhere in it; PMID 27773744 is not cited by it.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-27869163-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260913-27869163-01` §1 and §4, re-derived on main's current text. The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. Not in this batch: the candidate's §2 (`DL-MECH-024`) and §3 (`DL-METH-094`) appends, which belong to the discovery-ledger batch.

---

## PAPER 110
**Short title:** McBride 2019 — Wwox Deletion in Mouse B Cells Leads to Genomic Instability, Neoplastic Transformation, and Monoclonal Gammopathies
**Full title:** Wwox Deletion in Mouse B Cells Leads to Genomic Instability, Neoplastic Transformation, and Monoclonal Gammopathies
**Authors:** McBride KM, Kil H, Mu Y, Plummer JB, Lee J, Zelazowski MJ, Sebastian M, Abba MC, Aldaz CM
**Year:** 2019
**Journal/source:** *Front Oncol* 2019;9:517
**Identifier:** PMID 31275852 / DOI 10.3389/fonc.2019.00517
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-088` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-31275852-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID31275852.json`, dossier `fulltext_dossiers/PMID31275852.md`.
**Source type:** conditional-knockout mouse cohort + primary-B-cell repair assays
**Primary pathway:** DNA-damage response / genome stability: DNA-repair **pathway choice** at class-switch junctions
**Model/species:** mouse — 🔴 **the model switches between the paper's halves, and is named per experiment:** tumour, survival and incidence data come from the **`Cd19`-conditional** B-cell knockout; the class-switch, junction and translocation experiments use naïve splenic B cells from **whole-body `Wwox`-null** juveniles aged 16–17 days (primary, non-transformed cells from an engineered line). Deletion is protein-verified and tissue-restricted in the conditional model, with cerebellum, lung and kidney Wwox-replete
**Genotype/model:** no WWOX disease allele; no neural material
**Transferability:** `T3`
**clinical relevance:** LOW
**Claim links:** 029 — bounded murine observation added by `BATCH_20260926_ALDAZ_R5`
**Role:** the corpus's only measurement of WWOX loss on **class-switch recombination** and junction structure — a repair **pathway-choice** endpoint beside the burden endpoints the corpus already holds; unique in PubMed at reading time and **unreplicated**, which is the most important thing about its strength. Blunt joins fall from 26/77 to 5/61 and long-microhomology junctions rise from 1/77 to 8/61, while junction-adjacent mutation frequency is unchanged (5.2 vs 5.0 × 10⁻³/bp) and AID protein is not elevated; switching is only mildly reduced (~75% of wild type). The mechanism is explicitly unknown in the source. This paper measures no ATM, γH2AX, 53BP1 or relocalisation.
**LIT link:** [[literature_tracking_log_current#LIT-0111]]
**Note:** **Limits that exist only in the pixels, the table or the supplement:** the stated translocation fold change is not the panel's — text and PDF print "2.5-fold", Figure 6C reads ≈ 0.22 vs ≈ 1.45 per 10⁶ cells (≈ 6.5-fold), unresolved and recorded as an ambiguity; Figure 5's caption miscounts its own denominator ("76 WT" against 77 elsewhere); Methods say three independent experiments where Figures 5A and 6C say n = 4; Figure 4D carries an undeclared AID⁻/⁻ arm (~0.3%); Figure 5A prints p = 0.15 for insertions > 1 nt, reported in text only as "not significantly different"; survival denominators are irreconcilable (17/44, 34/14, 27/9, no attrition stated). **Recomputed:** tumour incidence 16/34 vs 2/14 → Fisher exact **p = 0.0493** (components not significant alone: lymphoma p = 0.70, plasmacytoma p = 0.085); SPEP 10/27 vs 1/9 → **p = 0.22**, no test stated in the paper. Heterozygotes were collected and never reported. Dependency screen `SCREENED_CLEAN` (59 of 61 screened).
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-31275852-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-31275852-01` §2, §4 and the §9 correction, re-derived on main's current text. The claim link the reading proposes (`CLAIM 029`) is **held for the claim batch**, together with every claim-text change; `Claim links` stays `none` until then. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. The candidate's §9 correction is honoured in `Model/species`: the repair experiments are named as the whole-body null line and "non-engineered" is not written. Held with the link: the §3 sentence for `CLAIM 029` and its working-model mirror.

**Claim-link resolution (BATCH_20260926_ALDAZ_R5):** the earlier assessment note correctly described the held state at R2; the bounded observation now appears in [[claim_registry_current#CLAIM 029]], with `Status: in observation` and no CNS transfer.

---

## PAPER 111
**Short title:** Park 2022 — Wwox Binding to the Murine Brca1-BRCT Domain Regulates Timing of Brip1 and CtIP Phospho-Protein Interactions with This Domain at DNA Double-Strand Breaks, and Repair Pathway Choice
**Full title:** Wwox Binding to the Murine Brca1-BRCT Domain Regulates Timing of Brip1 and CtIP Phospho-Protein Interactions with This Domain at DNA Double-Strand Breaks, and Repair Pathway Choice
**Authors:** Park et al. (7 authors per the dossier)
**Year:** 2022
**Journal/source:** *Int J Mol Sci* 2022;23(7):3729
**Identifier:** PMID 35409089 / DOI 10.3390/ijms23073729
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-074` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-35409089-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID35409089.json`, dossier `fulltext_dossiers/PMID35409089.md`.
**Source type:** primary research, experimental (mouse cell biology)
**Primary pathway:** DNA-damage response / genome stability: DSB end-resection timing; BRCA1-BRCT A/B/C complex formation; WWOX–BRCA1 axis
**Model/species:** mouse MEFs (`Wwox−/−`, siWwox) and mouse tumour lines
**Genotype/model:** no WWOX-DEE allele
**Transferability:** **T3** — and this paper makes mouse→human transfer of the WWOX–BRCA1 repair mechanism *weaker*, not stronger (see Note)
**clinical relevance:** LOW
**Claim links:** none — the reading proposes no claim link
**Role:** the direct, in-mouse measurement of early end resection under Wwox loss (SMART ssDNA tracts), which `PAPER 109` infers only from foci; and the source of the species boundary on the WWOX–BRCA1 interaction
**LIT link:** [[literature_tracking_log_current#LIT-0097]]
**Note:** **Species boundary:** the human WWOX–BRCA1 interaction is mapped to WW1 binding BRCA1 near `981PPLF984` in the exon-11 region; this paper shows that motif is *«conserved in primates but not in rodent species»*, that exon 11 is dispensable in mouse, and maps the mouse interaction to the **BRCT** domain — **the two species use different binding surfaces for the same partner**, so any inference from a mouse repair phenotype toward a human WWOX-DEE genotype must cross a demonstrated species difference in the interaction itself. Resection tracts by SMART are longer in KO than WT at 1 h (5–10 µm against 1–2 µm), with elevated pRPA foci and chromatin loading. **Left open by the paper and by this reading:** whether recruitment timing or protein abundance drives the phenotype — both measured, neither tested against the other. One `text_contradicted_by_panel` relation is internal to this paper (Figure 4F against its own Results sentence). The Chk2-inhibition synthetic-lethality content is an oncology lever (killing WWOX-deficient cells) and is not carried toward the reference genotype. **Citation identity, measured:** ref 17 of `PMID 38499540` ("Park et al.") is **PMID 34998176** (*DNA Repair* 2022;110:103264), still unread and queued inside `FT-176` (this paper’s reference debt); this paper is that article's ref 39.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-35409089-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260913-35409089-01` §1, §3 and §4, re-derived on main's current text. The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. Not in this batch: the candidate's §2 (`DL-METH-084`) and §3 (`DL-MECH-024`) appends (discovery-ledger batch); the `PMID38499540.json` `multihop.queued[0]` pmid is another reading's manifest and stays its owner's.

---

## PAPER 112
**Short title:** Hussain 2023 — WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12
**Full title:** WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12
**Authors:** Hussain et al.
**Year:** 2023
**Journal/source:** *Progress in Neurobiology* 223:102425
**Identifier:** PMID 36828035 / DOI 10.1016/j.pneurobio.2023.102425
**Status:** superseded
**Superseded by:** [[paper_registry_current#PAPER 007]] — same paper (`BATCH_20260926_ALDAZ`, 2026-09-26); this record is kept append-only as audit history and never deleted
**Record provenance:** placeholder `CORPUS-STUB-053` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** carried by `PAPER 007`, the canonical record of this paper. `BATCH_20260926_ALDAZ_R1` registered the reading on this record (receipt `FTR-20260913-36828035-03`, manifest `deepdive_manifests/PMID36828035.json`, dossier `fulltext_dossiers/PMID36828035.md`); `BATCH_20260926_ALDAZ` moved the declaration to `PAPER 007`, so one receipt backs one record.
**Transferability:** not assessed in this registration — held with the reading's candidate
**clinical relevance:** not assessed in this registration — held with the reading's candidate
**Claim links:** none — see `PAPER 007`
**Next action:** none — superseded by PAPER 007
**Duplicate record (BATCH_20260926_ALDAZ, 2026-09-26):** **same paper as [[paper_registry_current#PAPER 007]]**, which carries `CLAIM 006` and `CLAIM 007` and now holds this record's identity and evidence depth. Kept append-only, never deleted: its receipt and its registration by `BATCH_20260926_ALDAZ_R1` stay resolvable. Cite `PAPER 007`, not this record.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-36828035-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.

---

## PAPER 113
**Short title:** Zeng 2024 — Endothelial knockdown of the tumor suppressor, WWOX, increases inflammation in ventilator-induced lung injury
**Full title:** Endothelial knockdown of the tumor suppressor, WWOX, increases inflammation in ventilator-induced lung injury
**Authors:** Zeng Z, Abdelwahid E, Chen W, Ascoli C, Pham T, Jacobson JR, Dudek SM, Natarajan V, Aldaz CM, Machado RF, Singla S
**Year:** 2024
**Journal/source:** *Am J Physiol Lung Cell Mol Physiol* 2024;326(6):L689–L698
**Identifier:** PMID 38563965 / DOI 10.1152/ajplung.00277.2023
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-120` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-38563965-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID38563965.json`, dossier `fulltext_dossiers/PMID38563965.md`.
**Transferability:** not assessed in this registration — held with the reading's candidate
**clinical relevance:** not assessed in this registration — held with the reading's candidate
**Claim links:** none — held for the operator's decision on the reading's candidate
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.

---

## PAPER 114
**Short title:** De La Cruz 2025 — Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation
**Full title:** Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation
**Authors:** De La Cruz et al.
**Year:** 2025
**Journal/source:** bioRxiv preprint, not peer reviewed (v1 posted 2025-01-18)
**Identifier:** PMID 39868255 / DOI 10.1101/2025.01.17.633677
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-110` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260913-39868255-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID39868255.json`, dossier `fulltext_dossiers/PMID39868255.md`.
**Source type:** 🔴 **PREPRINT (bioRxiv v1, NOT peer reviewed), licence cc_no, no published version** — primary experimental, mouse
**Primary pathway:** P6 — neuroinflammation / glia; secondary: extrinsic inflammatory challenge
**Model/species:** mouse
**Genotype/model:** `Wwox WT/P47T` **heterozygote** + LPS 10 mg/kg — not a WWOX-DEE allele of the reference genotype's class
**Transferability:** T3 — preprint, heterozygote, WW1 missense with intact protein, single 12 h endpoint
**clinical relevance:** LOW — the challenge-sensitisation hypothesis is retained in Role, without claim support
**Claim links:** none — the reading proposes none, deliberately: the proposition that one impaired allele may be silent until an inflammatory challenge arrives is `IPOTESI`, and a claim now would consolidate a preprint's framing ahead of its evidence
**Role:** the extrinsic-challenge leg of the inflammation axis and a hypothesis generator for challenge sensitisation; **not** an independent replication of `PAPER 007`
**LIT link:** [[literature_tracking_log_current#LIT-0130]]
**Note:** In five of six quantitative brain and plasma endpoints a significant between-genotype difference under LPS coexists with **no significant LPS response in either genotype**; cortical astrocytes (p=0.0005 between, p=0.0040 within) are the exception. 🔴 **The paper models mortality and measures none:** Methods declare *"The risk for mortality was measured using a simple linear regression model"*, while no death, survival curve or humane endpoint is reported and every animal is euthanised at a fixed 12 h — what is modelled is the MSS clinical score, a correlate of mortality in the cited ref 19, so no statement about WWOX and sepsis *mortality* is supported. No peripheral cytokine differs between genotypes and the significant plasma IL-6/TNF-α responses are **wild type's**. **No WWOX protein or transcript is measured anywhere in the paper.** Seven of 36 animals removed by ROUT, three of them from the wild-type LPS arm. Two citation defects in its use of `PAPER 007` are recorded in the joint synthesis of the reading. **REVIVAL_TRIGGER** for any claim: a peer-reviewed version, or any second group entering the WWOX × sepsis intersection.
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260913-39868255-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260913-39868255-01` §1 and §2, re-derived on main's current text. The reading proposes no claim link, and none is written. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. Pathway reconciliation: the candidate's `P6 — neuroinflammation` follows the canonical P1–P7 legend above. The FASE-1 `P6 — DDR / genome stability` labels are historical, not a second meaning for current records. Not in this batch: the candidate's §3 (`DL-MECH-012` tag and legs, `DL-REPO-002` wording), which belongs to the discovery-ledger batch.

---

## PAPER 115
**Short title:** Hussain 2025 — B-cell–specific Wwox deletion promotes plasmablastic tumor development and proinflammatory signatures in myeloma model
**Full title:** B-cell–specific Wwox deletion promotes plasmablastic tumor development and proinflammatory signatures in myeloma model
**Authors:** Hussain T, Bramble MD, Liu B, Abba MC, Chesi M, Aldaz CM
**Year:** 2025
**Journal/source:** *Blood Neoplasia* 2025;2(4):100153
**Identifier:** PMID 41090157 / DOI 10.1016/j.bneo.2025.100153
**Status:** processed
**Record provenance:** placeholder `CORPUS-STUB-178` promoted by `BATCH_20260926_ALDAZ_R1` (2026-09-26) to register a full-text reading recovered from the VPS backup; bibliographic fields from the reading's dossier header
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260914-41090157-01` (read on the VPS laboratory checkout; recovered into this ledger by `fulltext_receipts.py rechain`, 2026-09-26); work manifest `deepdive_manifests/PMID41090157.json`, dossier `fulltext_dossiers/PMID41090157.md`.
**Source type:** cross-model mouse cohort + RNA-seq/WES genomics + public-dataset re-analysis
**Primary pathway:** DNA-damage response / genome stability (secondary: inflammation)
**Model/species:** mouse — the `Cd19`-conditional *Wwox* knockout of `PAPER 110` crossed into Vk∗MYC myeloma mice; murine B/plasma-cell lineage on a *MYC*-driven background
**Genotype/model:** no WWOX disease allele; no neural material
**Transferability:** `T3`
**clinical relevance:** LOW
**Claim links:** 029 — bounded murine observation added by `BATCH_20260926_ALDAZ_R5`
**Role:** the direct sequel to `PAPER 110` (same laboratory, same conditional allele): B-cell *Wwox* deletion on a *MYC* background with a genomic-instability phenotype **confined to the tumours, not the marrow** — and two qualifications that must travel with any use of it: the mismatch-repair signature SBS26 is present in a **wild-type** marrow sample too, and SBS85 appears in **none** of the four tumours whose hypermutation the paper attributes to AID/APOBEC, while the *Aicda*/*Apobec2* overexpression offered as that mechanism fails its own test (P = .2646 / .2680). Declared conflict: one author receives royalties from licensing Vk∗MYC mice.
**LIT link:** [[literature_tracking_log_current#LIT-0194]]
**Note:** **"Knockout" is a ~3–5-fold reduction, not an ablation** (Supplementary Figure S1b: KO ≈ 0.3 vs WT ≈ 1.5; *Wwox* transcript down only 1.61 log₂ in sorted CD138⁺ cells). The incidence result is marginal and test-dependent (χ² P = .036 as printed; Fisher exact two-tailed p = 0.052 on the same 17/27 vs 4/14 table). Monoclonal gammopathy is genotype-independent (24/24 KO, 14/14 WT). Wild-type Vk∗MYC mice get the same tumour kinds and **none of those four WT tumours was sequenced**, so every "tumour vs marrow" contrast is within-knockout. The inflammation signature rests on 87 genes of which 31 are immunoglobulin V genes — a clonality pattern; no cytokine or NF-κB protein was measured. Figure 7B's caption overstates its own table; the chr11 interval carrying *Rel*, *Xpo1*, *Bcl11a* is a gain in two tumours and a loss in a third. 🔴 **The paper contradicts itself about which tumour is which histology** (Figure 6A/6B against Figure 6C's caption), and the *Aicda*/*Apobec2* claim is attached to those two points; nothing in the artefact adjudicates. The only human evidence is a median-split re-analysis of four public microarray series. The heterozygous arm — the one dose-sensitivity handle — is never analysed for survival or incidence. Dependency screen `SCREENED_CLEAN` (70 of 74 screened).
**Registration note (BATCH_20260926_ALDAZ_R1, 2026-09-26):** registered as READ IN FULL, and nothing more. What the reading found is **not propagated** into any claim, working-model block, ledger or assessment field: the recovered VPS candidates that carry it (`CC-20260914-41090157-01`) are re-queued and held for the operator's decision (`disease-models/wwox/research/vps_recovery_20260925/README.md`). A reader must not infer from this record that the reading confirmed or changed anything in canon.
**Assessment note (BATCH_20260926_ALDAZ_R2, 2026-09-26):** the assessment half of this registration is now written — the fields from `Source type` to `Note` — from `CC-20260914-41090157-01` §2 and §4, re-derived on main's current text. The claim link the reading proposes (`CLAIM 029`) is **held for the claim batch**, together with every claim-text change; `Claim links` stays `none` until then. The registration note above is superseded for these fields only; no claim, working-model block or ledger entry is changed by this record. Held with the link: the §3 sentence for `CLAIM 029`. Nothing is routed toward `CLAIM 006` or `CLAIM 025`, as the candidate's §7 requires.

**Claim-link resolution (BATCH_20260926_ALDAZ_R5):** the earlier assessment note correctly described the held state at R2; the bounded observation now appears in [[claim_registry_current#CLAIM 029]], with `Status: in observation` and no CNS transfer.

---

## PAPER 116
**Short title:** Saeki 2011 — GSK-3β2 phosphorylates tau less than GSK-3β1: tau is a disfavoured substrate for β2, not β2 a weak kinase
**Full title:** Glycogen synthase kinase-3β2 has lower phosphorylation activity to tau than glycogen synthase kinase-3β1
**Authors:** Saeki K, Machida M, Kinoshita Y, Takasawa R, Tanuma S
**Year:** 2011
**Journal/source:** *Biol Pharm Bull* 2011;34(1):146–149
**Identifier:** PMID 21212533 / DOI 10.1248/bpb.34.146 (no PMCID)
**Status:** processed
**Record provenance:** created by `BATCH_20260926_ALDAZ_R2` (2026-09-26) from `CC-20260914-UNRECORDED-READS-01` §2.1: a complete reading persisted on 2026-07-26 had no registry record at all. Identity fields from Europe PMC as the candidate recorded them (queried 2026-09-14).
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20260726-21212533-01`; manifest `deepdive_manifests/PMID21212533.json`, 14 locators
**Source type:** primary experimental — HEK293T co-expression and in vitro kinase assays with recombinant enzymes; a four-page Note (no Limitations section, no supplementary material)
**Primary pathway:** GSK-3β isoform biochemistry — tau substrate discrimination between the β1 and β2 splice isoforms
**Model/species:** human HEK293T cells (co-expression with tau) and recombinant enzymes in vitro; no animal, no neural tissue
**Genotype/model:** no WWOX allele and no WWOX measurement — the paper bears on the GSK-3β node of the discovery ledger, not on WWOX directly
**Transferability:** T3 (HEK293T co-expression and in vitro)
**clinical relevance:** LOW
**Claim links:** none — no claim cites it
**Role:** isoform-discrimination anchor for the GSK-3β node — the source of "tau is a disfavoured substrate for β2", **not** "β2 is a weak kinase": on the synthetic peptide pGS-2 the two isoforms are equally active (234.5 ± 7.8 for β1 against 246.5 ± 2.4 nmol/min/mg for β2), and both phosphorylate APP at Thr668 to a similar level.
**LIT link:** none — this PMID has no literature-log record, and this batch does not create one
**Note:** 🔴 **Boundary that travels with the record:** the Figure 3 titration series are **not matched** between isoforms (β1 runs 0-0.1-0.3-1-3, β2 runs 0-0.3-1-3-10, no shared top concentration), so **no fold figure may be taken from Figure 3**. The C-terminal deletion is asymmetric: the same 40-residue tail is indispensable to one isoform and dispensable to the other; the higher-order-structure explanation is the authors' hypothesis, and no GSK-3β2 structure exists to settle it. **Canonical use today:** cited by the discovery ledger in `DL-MECH-066` and `DL-MECH-068`; the reading manifest also lists `DL-MECH-067` and `DL-BIO-013` as landing context. The full-text queue (`FT-026`, with its two resolved references queued as `FT-027` and `FT-028`), per the manifest's landing. **Provenance ceiling, declared:** none of the reading's artefacts is present on this disk, so this identity block rests on the manifest and an external bibliographic lookup; re-acquisition is owed before the record is cited outside this corpus.

---
## PAPER 117
**Short title:** Piard 2019 Genet Med — WOREE phenotypic spectrum, 20 additional cases
**Full title:** The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature
**Authors:** Piard J, Hawkes L, Milh M, Villard L, Borgatti R, Romaniello R, Fradin M, Capri Y, Héron D, Nougues MC, Nava C, Tarta Arsene O, Shears D, Taylor J, Pagnamenta A, Taylor JC, Sogawa Y, Johnson D, Firth H, Vasudevan P, Jones G, Nguyen-Morel MA, Busa T, Roubertie A, van den Born M, Brischoux-Boucher E, Koenig M, Mignot C, Kini U, Philippe C
**Year:** 2019
**Source type:** primary cohort + review of the literature
**Journal/source:** *Genet Med* 2019;21(6):1308-1318
**Identifier:** PMID 30356099 / PMCID PMC6752669 / DOI 10.1038/s41436-018-0339-3
**Status:** processed
**Record provenance:** created by `BATCH_20260927_003` (2026-09-27) from `CC-20260921-PAPER025-IDENTITY-01` OP 2, which promotes `CORPUS-STUB-059` / `LIT-0083` with metadata verified at PubMed on 2026-09-27. The stub is replaced, not kept beside this record.
**Evidence depth:** `partial_fulltext_read` — receipts `FTR-20260811-30356099-01` and `FTR-20260921-30356099-02` (a third, `FTR-20260927-30356099-03`, reads the presentation-age and diagnosis-age questions); a fourth, `FTR-20261003-30356099-01`, reads every section, all three figures and Supplemental Tables 1–4, and stays partial only because the manifest's multihop queue (nine WWOX-direct references) is open; manifest `deepdive_manifests/PMID30356099.json`; dossier `research/fulltext_dossiers/PMID30356099.md`
**Primary pathway:** genotype-phenotype / human clinical spectrum
**Model/species:** human
**Genotype/model:** biallelic WWOX variants across null and missense classes; the largest **primary** WOREE case series in the corpus read here as of 2026-09-28 (20 new cases; `PREMISE: INFERENZA`) — **not** the largest cohort, see `Role`
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** none declared by this batch — the record is created for identity and cohort reasoning, and no claim link is added to clear a warning
**Role:** largest **primary** WOREE case series in the corpus read here as of 2026-09-28 — **20 new cases** (`PREMISE: INFERENZA`); as *cohorts* both `PMID 40875931` (50 individuals / 45 families) and [[paper_registry_current#PAPER 018]] (75 pooled: 13 primary + 62 from the literature) are **larger**. Genotype-phenotype correlation, null genotypes most severe. Scoped 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` M9; the earlier unqualified *"largest WOREE cohort"* was false against two records this registry already holds
**Patient overlap (2026-10-03, `CC-20261003W4-A-PATIENT-OVERLAP-01`):** 🔴 Patient 8 (Supplemental Table 1: `c.[173-1G>T];[c.918del]`, non-consanguineous, West syndrome, initially thin corpus callosum then atrophy with midbrain flattening, death at almost 3 y) matches the single patient of [[paper_registry_current#PAPER 151]] (Tarta-Arsene 2017) on genotype and on every compared attribute; Tarta-Arsene is a co-author here. This paper neither cites that report nor lists it in its literature table, and counts P8 among its '20 additional' patients. `PREMISE: INFERENZA` — one patient, reported twice: the new-patient count is at most 19, and any aggregate that adds Tarta-Arsene 2017 to this cohort counts him twice.
**LIT link:** [[literature_tracking_log_current#LIT-0083]]
**Patient overlap (2026-10-04, `CC-20261004W8-A-PATIENT-OVERLAP-01`, `BATCH_20261004_002`):** Patient 11 (in-frame deletion of exons 6-8 + `c.705dup`) is re-reported as the WWOX case of [[paper_registry_current#PAPER 218]] (PMID 37946251), whose Table 1 names it *«Reported as Patient 11 (Table S1) in case series in Piard et al»*; the genotype matches this paper's Supplementary Table 1. **One patient, counted once** — `DATO`, because the later authors state the identity themselves. Note that [[paper_registry_current#PAPER 174]] (a review) already uses Piard 11 among its six genotypes, so the same patient is reachable by three routes and must be counted once across all three.
**Note:** Erratum `PMID 30783266` is linked and is **administrative**: one patient was investigated by genome rather than exome sequencing; no case count, genotype, phenotype or outcome changes. 🔴 **The online-first trap, by name:** issue year 2019, electronic publication 2018-10-25; Oliver 2023's Table S1 cites it as *"Piard J et al. Genet in Med. 2018"*. **ONE paper** — a PAPER record created from Oliver's string would duplicate this one. ⚠️ This is also the byline that was borrowed by `PAPER 025` (`PMID 30853297`, EJPN) until 2026-09-27; the two are separate papers by different first authors. 🔴 **Supplement read 2026-10-03 (`FTR-20261003-30356099-01`, `CC-20261003-A-PIARD-01`; class-level, figures from Supplemental Tables 1–4 recounted by script):** (1) the body's *«8 of 20»* premature deaths sits beside a mean (40 months) and range that belong to **nine** deaths listed in S1, only five of them under 36 months; S4's *«Deceased 20/37»* reconciles only with nine here plus the literature deaths **including a terminated pregnancy**. (2) The seven-patient null group behind *«the most severe clinical presentation»* includes a homozygous deletion that by its own S1 coordinates also removes NUDT7, VAT1L and CLEC3A, a never-genotyped sibling, a terminated pregnancy and two W44\* homozygotes **alive** at 7 y and 20 m; the series' homozygous p.Arg264\* sibling pair (deaths at 8 y 11 m and 5 y 2 m) is outside it. (3) *«premature death has never been described in patients with missense … only genotype»* holds only under the < 3 y definition: a **homozygous p.Gln230Pro** patient died at 3 y 3 m (S1). (4) S2 labels the Mallaret homozygous family `p.(Pro47Arg)` where S3 and Figure 1b give `p.Pro47Thr`; S2's three p.(Gly137Glu) families are two in S1; Figure 1a labels the exon-6 deletion in-frame (89 nt, out-of-frame). (5) Measured RNA exists for two patients only — a canonical acceptor `c.173-1G>T` → `r.[173_230del]` (exon 3 skipping) and p.Ser318Leu (no anomaly); the protein row is headed *«not based on experimental evidence»*. (6) `PREMISE: INFERENZA` — patient P8 (intron-2 acceptor + exon-8 frameshift, onset 1 m, West, death ≈ 3 y) matches the Tarta-Arsene 2017 case as tabulated by PMID 35573960 on six attributes; do not sum the two sources until Tarta-Arsene 2017 is read. `c.517-2A>G` occurs **nowhere** in this paper's body or its four supplementary tables (0 matches).

---

## PAPER 118
**Short title:** Hammouz 2026 IJMS — WWOX/HIF1A balance across breast subtypes and ovarian carcinoma (TCGA, DFS proxy)
**Full title:** WWOX/HIF1A Balance Delineates Context-Dependent Molecular States in Breast Cancer Subtypes and Ovarian Carcinoma
**Authors:** Hammouz RY, Maciejek K, Bednarek AK
**Year:** 2026
**Source type:** primary research — retrospective bioinformatic analysis of TCGA RNA-seq and clinical data
**Journal/source:** *Int J Mol Sci* 2026;27(15):6740
**Identifier:** PMID 42589397 / PMCID PMC13467099 / DOI 10.3390/ijms27156740
**Status:** processed
**Record provenance:** created 2026-09-28 by `CC-20260928-MIRROR003-REPAIRS-01` (Mirror ex-post review of `BATCH_20260927_003`, finding M3). 🔴 **Why it did not exist:** `BATCH_20260927_003` bounded [[claim_registry_current#CLAIM 025]] on a first-hand reading of this paper and registered no record for it, so the bounding source was invisible to `trace_claim_foundation` — which showed `CLAIM 025` resting on [[paper_registry_current#PAPER 091]] alone — and LINT could only emit `[INFO] UNLINKED_SUPPORT_UNCHECKED`, the weaker screen. Metadata taken from the declared JATS artefact's own `article-meta`. 🔴 **Why the `Claim links: 025` field stands — stated as derivation of the bound, not as receipt-existence (2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDING 3).** [[claim_registry_current#CLAIM 025]]'s `Evidence boundary` **derives its bound from this paper's own Cox models and event structure** — `228` OV patients with `161` events against `390` BRCA with `22`, `HR 1.11, 95% CI 0.92–1.35, p = 0.27`, concordance `0.49` — so the **evidential** edge is true. The receipt and the manifest establish that the reading **happened**; they do not establish that a source is **evidence for a claim**, and a receipted reading of an irrelevant paper would clear `[INFO] UNLINKED_SUPPORT_UNCHECKED` equally well — which is exactly the defect Mirror's `F5` named on `BATCH_20260927_002`, where `claim_links` is an evidential edge in `trace_claim_foundation.EVIDENTIAL_EDGES`. The producing candidate's wording, which licensed this field on receipt-existence, is superseded by its own appended correction note.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20260927-42589397-02` (first-hand, PMC JATS XML, `files/fulltext/PMID42589397_ZZ2026_PMC_2026-09-27.xml`, sha256 `ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af`); prior receipt `FTR-20260921-42589397-01` is a **verification receipt of another actor's reading** and declares tables and figures unavailable. Manifest `deepdive_manifests/PMID42589397.json`, **7** verbatim locators — 5 persisted with `FTR-20260927-42589397-02`, and **2 appended on 2026-09-28** (entries 6 and 7, anchored at `Results 2.6.2` and `Methods 5.1`) **inside that receipt's own declared coverage** (`methods: read`, `results: read`), both re-verified verbatim against the fingerprinted artefact and each occurring exactly once, so no quotation is at risk; the `receipt_correction` for that count is **recorded**: `FTR-20260928-42589397-03` (`prior_receipt: FTR-20260927-42589397-02`, `reread_reason: receipt_correction`, `event_at 2026-09-28T05:49:52Z`), appended by the Orchestrator at commit `082ed19` — which is `BATCH_20260928_002`'s own base commit, 44 minutes before that batch's propagation commit `c5eec22`, so the correction was already in the ledger before the batch that called it *owed* began (corrected 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 1 on `BATCH_20260928_002`, replacing *«a `receipt_correction` event on that lineage is owed for the count and is prepared for the Orchestrator to append»*). ⚠️ The manifest's `receipt` field carried `FTR-20260921-42589397-01` until 2026-09-28 and now names **`FTR-20260927-42589397-02`**, the reading that produced it. 🟢 **Repaired 2026-09-28 by `framework/scripts/manifest_receipt_repoint.py`**, which derives the value from the ledger rather than from any report, under the semantics `framework/protocols/fulltext_read_receipt.md` decided the same day (CLOSED: *«a manifest's `receipt` names the reading that PRODUCED the manifest: the EARLIEST ledger event for the same study whose `outputs` name that manifest file»*); `manifest_receipt_provenance.py --pmid 42589397` now reports **CONFORMS**. 🔴 **The old value was wrong on two independent grounds, and the second is the checkable one:** `-01` names this manifest in no `outputs` at all (`UNNAMED`), *and* its `source_fingerprint` is `572a7e6b14b8d10ec993c901dd367b2163437077f5b6fb429e874a5fc43e6e16` — a **different document** from the `ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af` this manifest declares in `source_artifacts` and against which every locator in it verifies, which `-02` fingerprints exactly. The repair therefore tightened the artefact binding `require_work_manifest` enforces, not only the pointer semantics. ⚠️ The manifest was **not** hand-edited: it was rewritten by a sanctioned instrument, and its bytes are pinned — `pathograph_export.jsonl`'s derivation manifest carries an **aggregate** sha256 over its whole 119-file input set, deep-dive manifests included, so the one-byte change made the pathograph STALE and it was regenerated in the same landing. (Present tense corrected 2026-09-28 by `CC-20260928-MIRROR002B-REPAIRS-01`, discharging **`REP-26`** of `research/record_repair_queue_current.md` and applying Mirror FINDING 2 on `BATCH_20260928_002`, from *«still names `FTR-20260921-42589397-01` … the two targets `fulltext_read_receipt.md` deliberately leaves open for that field … routed to whoever owns manifest re-pointing»*.) **Gaps, disambiguated:** **one** evidence gap was declared — Supplementary Tables S4–S8 unfetched (`verbatim_locators.note`, and the receipt's single `DECLARED GAP`) — 🟢 **discharged 2026-09-28** by `FTR-20260928-42589397-04` (closing sentence of this field); the **five** a reader may also meet are the manifest's `waived` **deep-dive sections** (`group_assessment`, `field_density`, `multihop`, `corpus_crossquery`, `retraction_check`), which `deepdive_manifest.py` reports in its own vocabulary as *"structurally valid with declared gaps (5 gap(s))"*. The earlier *«7 verbatim locators, 5 declared gaps»* collapsed two senses of *gap* into one phrase that read as five holes in the evidence (2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDINGS 4, 5 and 6; FINDING 5's own falsifier holds and the figure **5** is the tool's, so what is repaired is the ambiguity, not a wrong count). 🟢 **Supplementary debt discharged (2026-09-28, `FTR-20260928-42589397-04`, Supplementary File S1, sha256 `7f9d4bcff7ffcb47b41eabb79be7bf1db3a737eece865259cd387988f0ee5ccb`).** Table S7 (p. 8) gives the per-subtype rows — basal-like `HR 1.11, p 0.92`, «high»; HER2-enriched `0.17, 0.13`, «high»; Lum A `0.46, 0.45`, «low»; Lum B (printed «RLum B») `1.32, 0.76`, «low»; OV `0.96, 0.8`, «low» — and *«none reached conventional statistical significance»*. Its «more favourable DFS group» column **confirms** the running text for all five; 🔴 **its own HR column does not**: no single orientation reconciles the two (caption «High vs Low»: basal-like, Lum A, OV disagree; reverse: HER2-enriched, Lum B disagree), and the Supplementary Figure S1 Kaplan–Meier panels, image-inspected, fit the reverse orientation (INFERENZA from curve geometry). The **HER2-enriched and Luminal B labels are source-internally contested**; the non-invariance is not (HRs straddle 1 under either orientation). Table S6 confirms the continuous-ratio values verbatim (BRCA `0.25 (0.15–0.44)` per SD; OV `1.11 (0.92–1.35)`, p 0.27; OV combined `1.44 (0.99–2.09)`, p 0.055). Tables S4–S5 (LASSO models) carry **no ratio row** — the bootstrapped breast model is ratio-free — and body §2.6.2's citation of Table S5 for subtype Cox results is a mis-citation (S5 is the OV model). Table S8 carries no survival direction.
**Primary pathway:** P5 — HIF1A / metabolism (oncological context)
**Model/species:** human tumour datasets (TCGA breast `n = 390`, ovarian `n = 228`); no WWOX allele, no perturbation, no neural material
**Genotype/model:** none — expression-ratio analysis, not a genotype study
**Transferability:** T3
**clinical relevance:** BACKGROUND — bounds the DIRECTION of the ratio–outcome association; authorises no transfer to a non-tumoural CNS claim
**Claim links:** 025 (**bounding source, not corroborating** — same group, same dataset family, tumour only, no perturbation, so it does not raise `CLAIM 025`'s corroboration weight)
**Role:** the source that removes sign-invariance from the WWOX/HIF1A ratio–outcome association: the direction is subtype-dependent and the authors call their subtype effects *"descriptive and hypothesis-generating rather than formally validated prognostic groupings"*. Also the source of the ovarian null's event structure — 161 events in 228 against 22 in 390 — which shows that null is event-rich rather than underpowered.
**LIT link:** [[literature_tracking_log_current#LIT-0420]]
**Note:** ⚠️ **Not the same paper as `LIT-0019`** (PMID 41007296, *Biology* 2025, same group, overall survival): checked by PMID, DOI, PMCID and title. 🔴 The authors' own hedge travels with the record: the subtype directions are *"tended to show"*, and the breast bootstrap leaves optimism-corrected C-indices *"centred close to 0 with a wide interval (approximately −0.50 to 0.46)"*.

---

## PAPER 119
**Short title:** Ehaideb 2018 Transl Neurosci — two families, homozygous splice-donor and homozygous nonsense WWOX alleles, with a review table
**Full title:** Novel Homozygous Mutation in the WWOX Gene Causes Seizures and Global Developmental Delay: Report and Review
**Authors:** Ehaideb SN et al.
**Year:** 2018
**Source type:** primary research — case report (two families) with literature review
**Journal/source:** *Transl Neurosci* 2018;9:203
**Identifier:** PMID 30746283 / PMCID PMC6368664 / DOI 10.1515/tnsci-2018-0029
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-A-REGISTRY-01` (intake wave 2026-10-02, Scientist A). Provisional number: if `PAPER 119` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-30746283-01`; manifest `deepdive_manifests/PMID30746283.json`; dossier `research/fulltext_dossiers/PMID30746283.md`
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** homozygous canonical splice donor `c.409+1G>T` (one child; carrier parents and sib); homozygous `p.Arg54*` (two sibs, no parental testing)
**Transferability:** T1 (human WWOX-DEE; null-class alleles, not the reference genotype class)
**clinical relevance:** MODERATE — adds two families and a carrier observation; no measurement
**Claim links:** 032 (carrier observation in the qualification paragraph of `CC-20261002-HETEROZYGOTE-CARRIERS-01`; not a supporting source)
**Role:** Splice-donor allele with no RNA test, and three heterozygous carriers described only as *«healthy»*. 🔴 Its review Table 1 transcribes the Q230P report as `p.Gly230Pro` / `c.689A<C`, and its Discussion says *«All of these mutations are homozygous»* beside a compound heterozygote in the same table — do not use this table as a source for any allele.
**Patient overlap (2026-10-03, `CC-20261003W5-B-PATIENT-OVERLAP-01`):** 🔴 the homozygous `p.Arg54*` sibship (older sister, younger brother) is probably family 2 of [[paper_registry_current#PAPER 171]] (Al Baradie 2022), re-described without cross-citation: same allele pair, sibship structure and sexes, onset at two months with spasms, the sister's hypertelorism / large ears / high arched palate, and a word-for-word identical MRI sentence (asymmetrical volume loss with asymmetrical ventricular dilatation and callosal thinning); the ages printed (18 and 3 months here; 5 y and 3 y 9 mo there, the sister 'first seen … at the age of 18 months, with her younger brother') advance by the same interval. One EEG descriptor differs (burst suppression here, hypsarrhythmia there). `PREMISE: INFERENZA` — not author-confirmed: count the sibship once. That paper also lists these three children as separate literature rows.
**LIT link:** [[literature_tracking_log_current#LIT-0253]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 120
**Short title:** Bayanova 2023 Mol Neurobiol — WGS in 20 children with early-onset epilepsy; one WWOX compound heterozygote (missense + splice donor)
**Full title:** Whole-Genome Sequencing Among Kazakhstani Children with Early-Onset Epilepsy Revealed New Gene Variants and Phenotypic Variability
**Authors:** Bayanova M et al.
**Year:** 2023
**Source type:** primary research — diagnostic WGS case series (n = 20)
**Journal/source:** *Mol Neurobiol* 2023;60(8)
**Identifier:** PMID 37095367 / PMCID PMC10293429 / DOI 10.1007/s12035-023-03346-3
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-A-REGISTRY-01` (intake wave 2026-10-02, Scientist A). Provisional number: if `PAPER 120` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-37095367-01`; manifest `deepdive_manifests/PMID37095367.json`; dossier `research/fulltext_dossiers/PMID37095367.md`
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** `c.911C>A p.(Ser304Tyr)` + `c.230+1G>T`, labelled compound heterozygous; phase not shown
**Transferability:** T2 (one case; segregation and function absent)
**clinical relevance:** LOW-MODERATE — one new case, alleles named, no segregation
**Claim links:** none
**Role:** One case with two novel alleles called by ACMG on a commercial platform. 🔴 It is a Journal Article, not a corrigendum: its linked erratum corrects an author surname. The WWOX pedigree's proband arrow marks a sib drawn unaffected.
**LIT link:** [[literature_tracking_log_current#LIT-0421]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 121
**Short title:** Rim 2018 BMC Med Genomics — 172-gene panel in 74 intractable early-onset epilepsies; one WWOX compound heterozygote (last-exon nonsense + exon 6–8 duplication)
**Full title:** Efficient strategy for the molecular diagnosis of intractable early-onset epilepsy using targeted gene sequencing
**Authors:** Rim JH et al.
**Year:** 2018
**Source type:** primary research — diagnostic panel series (n = 74)
**Journal/source:** *BMC Med Genomics* 2018;11:6
**Identifier:** PMID 29390993 / PMCID PMC5796507 / DOI 10.1186/s12920-018-0320-7
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-A-REGISTRY-01` (intake wave 2026-10-02, Scientist A). Provisional number: if `PAPER 121` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-29390993-01`; manifest `deepdive_manifests/PMID29390993.json`; dossier `research/fulltext_dossiers/PMID29390993.md`
**Primary pathway:** clinical spectrum / WWOX-DEE · allele classes
**Model/species:** human
**Genotype/model:** `c.1060C>T p.(Gln354Ter)` (last coding exon) + intragenic exon 6–8 duplication, phase by parental testing; infantile-spasm group
**Transferability:** T1 (human; neither allele is the reference genotype's)
**clinical relevance:** MODERATE — the only intragenic WWOX duplication in LEGEND, with carrier parents asymptomatic by inclusion criterion
**Claim links:** 032 (carrier observation; not a supporting source)
**Role:** An intragenic duplication called without PVS1; a direct tandem copy of exons 6–8 would be in frame (540 nt, reader's arithmetic), so its class is uncertain. The nonsense allele lies in the last exon (NMD escape expected; not addressed by the source). 🔴 Not a dose-gain datum.
**LIT link:** [[literature_tracking_log_current#LIT-0422]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 122
**Short title:** Szymańska 2014 Biomed Res Int — seven neurodevelopmental/neurometabolic cases; a 16q23.1 duplication called 'WWOX and MAF'
**Full title:** The Analysis of Genetic Aberrations in Children with Inherited Neurometabolic and Neurodevelopmental Disorders
**Authors:** Szymańska K et al.
**Year:** 2014
**Source type:** primary research — clinical case series (n = 7)
**Journal/source:** *Biomed Res Int* 2014:424796
**Identifier:** PMID 24949445 / PMCID PMC4052700 / DOI 10.1155/2014/424796
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-A-REGISTRY-01` (intake wave 2026-10-02, Scientist A). Provisional number: if `PAPER 122` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-24949445-01`; manifest `deepdive_manifests/PMID24949445.json`; dossier `research/fulltext_dossiers/PMID24949445.md`
**Primary pathway:** gene dose (rejected reading)
**Model/species:** human
**Genotype/model:** array-CGH duplication, NCBI36 chr16:77,445,915–78,190,209, inheritance unknown
**Transferability:** T3 for WWOX (the CNV holds only WWOX exon 9)
**clinical relevance:** BACKGROUND — recorded so the dose-gain reading is not made again
**Claim links:** none — the rejection is `DIS-022` (`CC-20261002-DOSE-GAIN-DISMISSAL-01`)
**Role:** 🔴 The authors' *«affects two dose-sensitive genes: WWOX … and MAF»* is not supported by their own coordinates: mapped to GRCh37 (Ensembl, reader's computation) the interval holds only WWOX's last exon and the 3′ part of intron 8. Not a WWOX dose-gain datum.
**LIT link:** [[literature_tracking_log_current#LIT-0423]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 123
**Short title:** Robertson 2025 NAR Genom Bioinform — FoundHaplo; WWOX p.Glu17Lys is a founder allele carried by 172 UK Biobank participants
**Full title:** Identifying individuals with rare disease variants by inferring shared ancestral haplotypes from SNP array data
**Authors:** Robertson E et al.
**Year:** 2025
**Source type:** primary research — statistical-genetics method with application
**Journal/source:** *NAR Genom Bioinform* 2025;7(2):lqaf033
**Identifier:** PMID 40191585 / PMCID PMC11970371 / DOI 10.1093/nargab/lqaf033
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-A-REGISTRY-01` (intake wave 2026-10-02, Scientist A). Provisional number: if `PAPER 123` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-40191585-01`; manifest `deepdive_manifests/PMID40191585.json`; dossier `research/fulltext_dossiers/PMID40191585.md`
**Primary pathway:** population genetics of WWOX alleles
**Model/species:** human
**Genotype/model:** missense `c.49G>A p.(Glu17Lys)`; 172 UKBB carriers by WES (zygosity per carrier unstated, no phenotype); 0 of 1,573 in an epilepsy cohort; 157 kb core haplotype shared by all 175 carriers
**Transferability:** T2 for allele frequency; none for phenotype (no carrier phenotype reported)
**clinical relevance:** MODERATE — fixes the gene of `p.E17K` and makes its recurrence a founder effect; licenses nothing about carriers
**Claim links:** 032 (missense-carrier observation, under `DO_NOT_INFER`; not a supporting source)
**Role:** Answers by reading that `p.E17K` is WWOX `c.49G>A` (and `p.Cys121Trp` is SCN1B). Its disease haplotypes come from three duos at the clinical centre of PAPER 018; two are likely PAPER 018's two `p.Glu17Lys` patients (INFERENZA) — counted once. 🔴 Its supplementary founder-origin citation (reference 21, PAPER 025) is not supported by that paper's text layer (`DIS-025`).
**LIT link:** [[literature_tracking_log_current#LIT-0424]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 124
**Short title:** Bacchelli 2020 Sci Rep — PsychArray CNVs in 128 ASD families; one intronic-for-canonical WWOX deletion in a case, one exon 6–8 deletion in a control
**Full title:** An integrated analysis of rare CNV and exome variation in Autism Spectrum Disorder using the Infinium PsychArray
**Authors:** Bacchelli E et al.
**Year:** 2020
**Source type:** primary research — family-based case-control CNV study
**Journal/source:** *Sci Rep* 2020;10:3198
**Identifier:** PMID 32081867 / PMCID PMC7035424 / DOI 10.1038/s41598-020-59922-3
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-A-REGISTRY-01` (intake wave 2026-10-02, Scientist A). Provisional number: if `PAPER 124` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-32081867-01`; manifest `deepdive_manifests/PMID32081867.json`; dossier `research/fulltext_dossiers/PMID32081867.md`
**Primary pathway:** gene dose / heterozygous carriers
**Model/species:** human
**Genotype/model:** case: heterozygous loss inside canonical intron 5 (shorter isoforms' last exon); control: heterozygous loss spanning canonical exons 6–7 and most of 8 (reader's mapping, unvalidated)
**Transferability:** T2 (human array data; no WWOX expression test)
**clinical relevance:** LOW-MODERATE — the one exon-level null-class heterozygote of the wave sits in a control without psychiatric history, neurologically unassessed
**Claim links:** 032 (carrier observation; not a supporting source)
**Role:** 🔴 The paper's *«significant role of … WWOX … in ASD susceptibility»* rests on one case whose deletion does not remove a canonical WWOX exon (`DIS-023`) plus a citation, with no WWOX-specific statistic. Table S5 prints the cytoband as `16p23.1` for a 16q23.1 interval.
**LIT link:** [[literature_tracking_log_current#LIT-0425]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 125
**Short title:** Yang 2023 Zoological Research — marmoset colony WGS; a 17-SNP intronic WWOX haplotype suggestively associated with handling-evoked seizures
**Full title:** Population genetics of marmosets in Asian primate research centers and loci associated with epileptic risk revealed by whole-genome sequencing
**Authors:** Yang X et al.
**Year:** 2023
**Source type:** primary research — population-genetics WGS with pedigree association
**Journal/source:** *Zoological Research* 2023;44(5):837-847
**Identifier:** PMID 37501399 / PMCID PMC10559097 / DOI 10.24272/j.issn.2095-8137.2022.514
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator) to land a reading that `CC-20261002-B-NONLINEAGE-01` § 3 deliberately left without a registry record.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-37501399-01`; manifest `deepdive_manifests/PMID37501399.json`; dossier `research/fulltext_dossiers/PMID37501399.md`
**Primary pathway:** non-lineage association signals / intron 8
**Model/species:** common marmoset (*Callithrix jacchus*), 38 animals in two captive colonies
**Genotype/model:** no WWOX copy-number event; 17 intronic SNPs on one haplotype in the last intron of the marmoset WWOX model transcript
**Transferability:** T3 (non-coding primate association; no WWOX function measured)
**clinical relevance:** BACKGROUND — an earned near-null, recorded so it is not later counted as primate evidence that WWOX variation causes epilepsy
**Claim links:** none — `CLAIM 037` is explicitly untouched (`research/intake_wave_20261002_B.md` § 2)
**Role:** 🔴 The abstract's deletion sentence is about a **KCTD18-like** CNV, not WWOX: the CNV tables hold no WWOX event. The WWOX signal is SNP-only, suggestive (LAMP P 2.4e-6 to 9.2e-6 against a 1e-5 threshold), with λ 0.825, carriers among unaffected animals in one colony, and no genome-wide signal by the authors' own statement. Annotated into `DL-MECH-107` by `CC-20261002-B-INTRON8-01` as **not** convergence.
**LIT link:** [[literature_tracking_log_current#LIT-0426]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 126
**Short title:** Chou 2019 Cell Commun Signal — p53/TIAF1/WWOX triad; the brain-aggregation statement rests on one xenograft arm
**Full title:** A p53/TIAF1/WWOX triad exerts cancer suppression but may cause brain protein aggregation due to p53/WWOX functional antagonism
**Authors:** Chou PY, Lin SR, Lee MH et al.
**Year:** 2019
**Source type:** primary research — cell and xenograft study
**Journal/source:** *Cell Commun Signal* 2019;17:76
**Identifier:** PMID 31315632 / PMCID PMC6637503 / DOI 10.1186/s12964-019-0382-y
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator) to land a reading that `CC-20261002-B-NONLINEAGE-01` § 3 deliberately left without a registry record.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-31315632-01`; manifest `deepdive_manifests/PMID31315632.json`; dossier `research/fulltext_dossiers/PMID31315632.md`
**Primary pathway:** aggregation / TIAF1 lineage
**Model/species:** cell lines plus nude-mouse xenograft (Wwox-intact)
**Genotype/model:** no WWOX-DEE genotype; overexpression and knockdown in tumour lines
**Transferability:** T3 (tumour-bearing mice with intact Wwox; no neural WWOX-loss arm)
**clinical relevance:** BACKGROUND — an earned null for the brain
**Claim links:** none — `CLAIM 003`, `CLAIM 006`, `CLAIM 030`, `CLAIM 037` are all untouched by this reading
**Role:** 🔴 Single-laboratory lineage, not independent support: 26 of 56 references, and all six behind the brain-aggregation background sentence, are the same laboratory, and `WWOX AND TIAF1 NOT Chang NS[au]` returns 0 on PubMed. The brain statement rests on **one** xenograft experiment, one lane per condition, with non-reducing blots in which the α-tubulin housekeeping control also aggregates; the authors state the mechanism is unknown, and the SDR-vs-WW binding account contradicts itself inside the paper. It down-weights nothing and adds no independent replication to `DL-BIO-004`.
**LIT link:** [[literature_tracking_log_current#LIT-0427]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 127
**Short title:** Kałuzińska 2021 Cancers — PLEK2/RRM2/GCSH, a 'WWOX-dependent' glioma triad defined by a correlation, not a perturbation
**Full title:** PLEK2, RRM2, GCSH: A Novel WWOX-Dependent Biomarker Triad of Glioblastoma at the Crossroads of Cytoskeleton Reorganization and Metabolism Alterations
**Authors:** Kałuzińska Ż et al.
**Year:** 2021
**Source type:** primary research — bioinformatic analysis of public bulk tumour expression data
**Journal/source:** *Cancers* 2021;13(12):2955
**Identifier:** PMID 34204789 / PMCID PMC8231639 / DOI 10.3390/cancers13122955
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator); the reading's own candidate, `CC-20261002-BIOMARKER-REJECTIONS-01`, records the rejection and creates no registry record.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-34204789-01`; manifest `deepdive_manifests/PMID34204789.json`; dossier `research/fulltext_dossiers/PMID34204789.md`. Figure panels and supplement are **not** read and are owed.
**Primary pathway:** biomarkers (rejected)
**Model/species:** human bulk tumour RNA-seq (672 samples, public data)
**Genotype/model:** none — WWOX is a stratifying variable, never a manipulated one
**Transferability:** T3 (glioma classification; no neural WWOX-loss system)
**clinical relevance:** BACKGROUND — recorded so the title is not transferred to this model
**Claim links:** none — the rejection is `DIS-026` (`CC-20261002-BIOMARKER-REJECTIONS-01`)
**Role:** 🔴 *«WWOX-dependent»* here means a cut-point on WWOX transcript abundance (222.6) plus a Spearman correlation (|R| 0.42–0.44). **There is no knockdown, no overexpression, no rescue and no protein measurement in the study**, so none of the three genes is a readout of a WWOX state. The authors do not overclaim: *«usefulness of PLEK2 , RRM2 , and GCSH as diagnostic or predictive biomarkers is yet to be confirmed»*. Same department as `PAPER 128`'s companion reading PMID 37781246 (Bednarek, Łódź) — the two are not independent.
**LIT link:** [[literature_tracking_log_current#LIT-0428]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 128
**Short title:** Zhang & Freudenreich 2007 Mol Cell — the FRA16D Flex1 AT-repeat stalls replication forks and breaks chromosomes in yeast
**Full title:** An AT-rich sequence in human common fragile site FRA16D causes fork stalling and chromosome breakage in *S. cerevisiae*
**Authors:** Zhang H, Freudenreich CH
**Year:** 2007
**Source type:** primary research — yeast genetics / replication
**Journal/source:** *Mol Cell* 2007;27(3):367-379
**Identifier:** PMID 17679088 / PMCID PMC2144737 / DOI 10.1016/j.molcel.2007.06.012
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator); `CC-20261002-BIOMARKER-REJECTIONS-01` § 4 states deliberately that this paper is **not** entered in the biomarker ledger in either direction.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-17679088-01`; manifest `deepdive_manifests/PMID17679088.json`; dossier `research/fulltext_dossiers/PMID17679088.md`. Figure panels and supplement are **not** read and are owed.
**Primary pathway:** locus fragility / FRA16D architecture
**Model/species:** *Saccharomyces cerevisiae* (often `rad52Δ`/`rad50Δ`, with hydroxyurea)
**Genotype/model:** none — a human DNA sequence element assayed in yeast; no WWOX protein, transcript or function is measured
**Transferability:** T3 — **OFF-AXIS for the assigned hypothesis.** Every measurement is somatic and mitotic, and the authors' own prediction terminates in *«cancer-causing rearrangements»*; it supports no statement about germline exon-scale deletions or about why one allele class is deleted. *«WWOX»* occurs 9 times in 189,143 bytes.
**clinical relevance:** BACKGROUND — a mechanistic precedent, not evidence about WWOX
**Claim links:** none
**Role:** What transfers is one mechanistic precedent: FRA16D carries a characterised replication-barrier element (Flex1; Flex4 and Flex5-p do **not** increase fragility), which is a real reason this locus is rearrangement-prone. 🔴 The paper never states which WWOX intron or exon Flex1 lies in — the fact the hypothesis would turn on is absent from the body. Carried as `LEAD-C1` (Flex1 AT-repeat length as a candidate rearrangement-risk covariate, `IPOTESI`, blocked on acquiring Finnis 2005) in `research/intake_wave_20261002_C.md` § 4, and as neither a biomarker nor a rejected biomarker.
**LIT link:** [[literature_tracking_log_current#LIT-0429]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 129
**Short title:** Chou 2020 Front Cell Dev Biol — `Wwox−/−` mouse skin; pERK and total ERK1/2 reduced in keratinocytes
**Full title:** Wwox Deficiency Causes Downregulation of Prosurvival ERK Signaling and Abnormal Homeostatic Responses in Mouse Skin
**Authors:** Chou PY et al.
**Year:** 2020
**Source type:** primary research — constitutive knockout mouse tissue study
**Journal/source:** *Front Cell Dev Biol* 2020;8:558432
**Identifier:** PMID 33195192 / PMCID PMC7652735 / DOI 10.3389/fcell.2020.558432
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator), promoting the corpus placeholder `CORPUS-STUB-083`, which is kept as history.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-33195192-01`; manifest `deepdive_manifests/PMID33195192.json`; dossier `research/fulltext_dossiers/PMID33195192.md`. Figure panels and the supplement — including Supplementary Figure S9, which carries the total-ERK half of the result — are **not** read and are owed.
**Primary pathway:** ERK signalling / tissue homeostasis
**Model/species:** mouse (constitutive `Wwox−/−` and littermates), HaCaT cells
**Genotype/model:** constitutive null; **no** overexpression arm (loss of function only)
**Transferability:** T2 for the perturbation, T3 for the tissue — keratinocytes, hair follicles, dermis and fat; **no neural tissue anywhere in the paper**
**clinical relevance:** MODERATE — the one WWOX-dependence in this wave shown by a real perturbation, in a tissue a living patient can be biopsied from
**Claim links:** none — `CLAIM 011` is annotated by `CC-20261002-WWOX-DOSE-CEILING-01`, which cites this paper for a two-sided statement about level, not as support
**Role:** Supplies two things and no more. (a) The pERK observation (*«keratinocytes expressed significantly reduced levels of pERK and total ERK1/2 protein»*, IHC over 25 regions from 3 mice), **rejected as a disease biomarker on specificity and retained by name only as a possible pharmacodynamic readout inside a controlled system** — `DIS-027`. (b) The explicit statement *«A certain amount of WWOX expression may be necessary for maintaining normal physiological functions in cells»*, with raised WWOX increasing proliferation in HT29 **cited from Nowakowska 2014, which is unread**. 🔴 Same Tainan laboratory and same knockout line as `PAPER 130`: the two are one group, not two.
**LIT link:** [[literature_tracking_log_current#LIT-0106]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 130
**Short title:** Cheng 2023 Cell Mol Life Sci — `Wwox` loss, senescence escape and genome instability in MEFs and fibroblasts
**Full title:** Loss of the fragile WWOX gene leads to senescence escape and genome instability
**Authors:** Cheng YY et al.
**Year:** 2023
**Source type:** primary research — knockout and knockdown cell study
**Journal/source:** *Cell Mol Life Sci* 2023;80(11):338
**Identifier:** PMID 37897534 / PMCID PMC10613160 / DOI 10.1007/s00018-023-04950-1
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator), promoting the corpus placeholder `CORPUS-STUB-077`, which is kept as history.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-37897534-01`; manifest `deepdive_manifests/PMID37897534.json`; dossier `research/fulltext_dossiers/PMID37897534.md`. Figure panels and the supplement are **not** read and are owed.
**Primary pathway:** senescence / genome instability / redox
**Model/species:** mouse embryonic fibroblasts, HEK293T, human dermal fibroblasts — **no neural and no in vivo arm**
**Genotype/model:** `Wwox−/−` knockout plus knockdown; ⚠️ the comparator in most figures is `Wwox+/−`, **not** wild type
**Transferability:** T2 for the perturbation, T3 for the phenotype (culture passages 20–30)
**clinical relevance:** MODERATE — carries one therapeutic-direction lead and four rejected biomarker candidates
**Claim links:** none — adjacent to `CLAIM 009` (redox, *in observation*) and `CLAIM 034` and resolving neither
**Role:** Source of `DIS-028` (γ-H2AX rejected as a WWOX readout because it rises both when WWOX is **lost**, here, and when WWOX is **added**, PMID 42395553 — the two papers do not cite each other, and the observation belongs to reading them together) and of `DIS-029` (SA-β-gal, p16/p21/p27 and microsatellite instability rejected as generic and unsamplable). The **NAC rescue** — *«during the passage culture prevented microsatellite instability and resulted in senescence induction in the late-passage Wwox −/− MEFs»* — is carried as `LEAD-C2` (`IPOTESI`) in `research/intake_wave_20261002_C.md` § 4 and is **deliberately not promoted**: it is a fibroblast-culture result with no neural and no in vivo arm. 🔴 Same laboratory and knockout line as `PAPER 129`.
**LIT link:** [[literature_tracking_log_current#LIT-0100]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 131
**Short title:** Mondragon-Estrada 2025 Birth Defects Res — spina bifida GWAS in Bangladesh; three imputed WWOX intron-8 SNPs, nominal and unreplicated
**Full title:** Folate Interaction With Genetic Risk for Neural Tube Defects Among Infants in Bangladesh
**Authors:** Mondragon-Estrada E et al.
**Year:** 2025
**Source type:** primary research — case-control GWAS (89 cases / 97 controls in the association models)
**Journal/source:** *Birth Defects Research* 2025;117(12):e70007
**Identifier:** PMID 41378749 / PMCID PMC12697008 / DOI 10.1002/bdr2.70007
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` § 6 (intake wave 2026-10-02, batch integrator). Its only landing before this batch was the queue record `FT-142`, which satisfies LINT and not the paper registry.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-41378749-01`; manifest `deepdive_manifests/PMID41378749.json`; dossier `research/fulltext_dossiers/PMID41378749.md`
**Primary pathway:** non-lineage association signals / intron 8
**Model/species:** human infants
**Genotype/model:** three imputed (R² 0.78) common SNPs inside WWOX **intron 8**; no WWOX-DEE genotype
**Transferability:** T3 — common non-coding variation, nominal significance, no function
**clinical relevance:** BACKGROUND — an earned null; the authors call the work *«hypothesis-generating»*
**Claim links:** none
**Role:** 🔴 Three source-internal corrections, each measured on reading: the abstract's *«coding region of WWOX»* means the gene body — the variants are **intronic**; the abstract pairs rs7184417 with rs28688166's statistics; and the association models use 89/97, not the 91/97 of the cohort description. OR ≈ 6.2 at p 2.2e-6 against a **suggestive** threshold only, and the locus is **absent from the paper's own technical replication**, which reproduced two other loci. Annotated into `DL-MECH-107` by `CC-20261002-B-INTRON8-01` as **not** convergence; `FT-142`'s negative was narrowed by `CC-20261002-B-NONLINEAGE-01` from *«not a WWOX paper»* to *«not a WWOX-function paper»*.
**LIT link:** [[literature_tracking_log_current#LIT-0430]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 132
**Short title:** Xia 2017 Transl Psychiatry — infant brain-volume GWAS; rs10514437 (WWOX intron) with white-matter volume, below the study's own threshold
**Full title:** Genome-wide association analysis identifies common variants influencing infant brain volumes
**Authors:** Xia K et al.
**Year:** 2017
**Source type:** primary research — GWAS of neonatal MRI volumes (561 infants)
**Journal/source:** *Transl Psychiatry* 2017;7(8):e1188
**Identifier:** PMID 28763065 / PMCID PMC5611727 / DOI 10.1038/tp.2017.159
**Status:** processed
**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` § 6 (intake wave 2026-10-02, batch integrator), for the same reason as `PAPER 131`: its only landing was `FT-142`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-28763065-01`; manifest `deepdive_manifests/PMID28763065.json`; dossier `research/fulltext_dossiers/PMID28763065.md`. Supplement read by label only (appendix plot books unread) and owed.
**Primary pathway:** white matter / non-lineage association signals
**Model/species:** human infants, MRI at about 5 weeks
**Genotype/model:** rs10514437, genotyped (not imputed), MAF 0.03, in a WWOX intron; no WWOX-DEE genotype
**Transferability:** T3 — normal-range volumetry in common variation; neither supports nor bounds a biallelic-null mechanism
**clinical relevance:** BACKGROUND — bounded context, not evidence
**Claim links:** none — `CLAIM 003` (hypomyelination, `consolidated baseline`) is explicitly **untouched**: this is volume in normal-range infants, and it neither supports nor narrows that claim
**Role:** P 1.56e-8 against the study's own four-phenotype threshold of 1.25e-8, **unreplicated** (unavailable in PNC and ENIGMA2), with no eQTL and no functional link. 🔴 **The direction matters and is easy to invert:** the effect is given per copy of the **common** allele (−3.76% WM), so the **minor** allele goes with *more* white matter. Survives only as *«WWOX-locus common variation may be associated with infant WM volume — unreplicated»*.
**LIT link:** [[literature_tracking_log_current#LIT-0431]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 133
**Short title:** Riva 2022 Front Pediatr — WOREE with p.Arg264* and an exon-6-only deletion missed by exome CNV calling; fibroblast RT-PCR
**Full title:** A Phenotypic-Driven Approach for the Diagnosis of WOREE Syndrome
**Authors:** Riva A, Nobile G, Giacomini T, et al.; Zara F, Iacomino M
**Year:** 2022
**Source type:** primary research — single case report
**Journal/source:** *Front Pediatr* 2022;10:847549
**Identifier:** PMID 35573960 / PMCID PMC9100683 / DOI 10.3389/fped.2022.847549
**Status:** processed
**Record provenance:** created by `CC-20261003-A-REGISTRY-01` (intake wave 2 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35573960-01`; manifest `deepdive_manifests/PMID35573960.json`; dossier `research/fulltext_dossiers/PMID35573960.md`
**Primary pathway:** clinical spectrum / WWOX-DEE · allele detection
**Model/species:** human
**Genotype/model:** stop `c.790C>T p.(Arg264*)` (exon 7) + 84.8 kb deletion removing exon 6 only (out-of-frame skip), each from an unaffected parent; predicted null/null
**Transferability:** T1 for allele detection; T3 for any genotype with residual protein
**clinical relevance:** MODERATE — a measured transcript consequence of an exon deletion (exon 5–7 junction in patient fibroblast RNA) and an exome CNV false negative
**Claim links:** 001 (drug-response observation, through `CC-20261003-A-VIGABATRIN-01`)
**Role:** Day-1 onset; vigabatrin, ACTH, ketogenic diet and five other drugs ineffective; phenobarbital and nitrazepam stopped for adverse events (not reported ineffective). 🔴 The exome CNV analysis was *«unremarkable»*: allele-class censuses built on NGS-diagnosed patients are lower bounds for single-exon deletions. No protein; the stop allele's NMD not tested.
**LIT link:** [[literature_tracking_log_current#LIT-0432]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 134
**Short title:** Dong 2023 BMC Med Genomics — compound WWOX deletions (exons 6–8 / intron-5 + exon-6) resolved by WGS and gap PCR after exome called a homozygous exon 6 deletion
**Full title:** Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome
**Authors:** Dong XS, Wen XJ, Zhang S, Wang DG, Xiong Y, Li ZM
**Year:** 2023
**Source type:** primary research — single case report with structural-variant resolution
**Journal/source:** *BMC Med Genomics* 2023;16:291
**Identifier:** PMID 37974179 / PMCID PMC10652538 / DOI 10.1186/s12920-023-01731-4
**Status:** processed
**Record provenance:** created by `CC-20261003-A-REGISTRY-01`; promotes [[paper_registry_current#CORPUS-STUB-096]] (kept as history). Provisional number.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-37974179-01`; manifest `deepdive_manifests/PMID37974179.json`; dossier `research/fulltext_dossiers/PMID37974179.md`
**Primary pathway:** clinical spectrum / allele architecture
**Model/species:** human
**Genotype/model:** one allele: 177 kb deletion of exons 6–8 (in-frame, predicted); other allele: two separate deletions — 13.26 kb inside intron 5 and 53.9 kb removing exon 6 only (out-of-frame, predicted); breakpoints by gap PCR and Sanger, phase by segregation
**Transferability:** T1 for allele detection; none for missense or splice-acceptor classes
**clinical relevance:** MODERATE — the exome call was right on exon-6 dosage and blind to the heterozygous loss of exons 7–8 and to phase
**Claim links:** none
**Role:** No RNA or protein from either allele. 🔴 Source-internal defects: the inheritance sentence swaps the two deletion sizes of the two-deletion allele; the pedigree draws the proband with the female symbol while the text and supplement say male; the *«earliest onset»* claim (day 15) is contradicted by published day-1 onsets, and the drug-resistance clause is verbatim from PMID 35573960 although only two drugs are named. Tabulated again by PMID 42193054 under a wrong reference number — count once.
**LIT link:** [[literature_tracking_log_current#LIT-0118]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 135
**Short title:** Kim 2025 Sci Rep — WWOX intronic SNVs and self-reported sleep duration (n = 8,840), with a Drosophila Wwox hypomorph
**Full title:** Genome-wide identification and functional validation of the WW domain containing oxidoreductase gene associated with sleep duration
**Authors:** Kim S, Kang SW, Kim SE, Kim HJ, Kim SA, Lee YW, Kim EY, Shin C, Lee HW
**Year:** 2025
**Source type:** primary research — genome-wide association study with an invertebrate functional arm
**Journal/source:** *Sci Rep* 2025;15(1):5552
**Identifier:** PMID 39952983 / PMCID PMC11828923 / DOI 10.1038/s41598-024-81158-8
**Status:** processed
**Record provenance:** created 2026-10-03 by `CC-20261003-C-REGISTRY-01` (intake wave 2, Scientist C). 🔴 **Why it did not exist:** the PMID was addressed by `FT-016` and by `DL-MECH-013` but by no registry record, so a reading of it would have been an `ORPHAN_COMPLETE_READ` for LINT. Provisional number: if `PAPER 135` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-39952983-02` (prior `FTR-20260811-39952983-01`, `inadequate_prior_coverage`); manifest `deepdive_manifests/PMID39952983.json` (14 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID39952983.md`
**Primary pathway:** behavioural / network-state endpoints (non-seizure)
**Model/species:** human community cohorts (Ansan n = 4,635, Ansung n = 4,205) and *Drosophila melanogaster*
**Genotype/model:** common intronic SNVs `rs16948804` and `rs4887991` at 16q23.1-q23.2, one LD block in the distal gene body; *Drosophila* `Wwox^f04545` insertion hypomorph (mRNA at about 8 per cent of control), homozygous, backcrossed six times, males only
**Transferability:** T3 — no WWOX-DEE allele, no patient, no measured WWOX expression in any human
**clinical relevance:** LOW — supplies a non-seizure behavioural endpoint in the fly; the human arm licenses nothing about the reference genotype class
**Claim links:** none
**Role:** The only source in the corpus with a quantified **non-seizure behavioural** endpoint for *Wwox* loss: daytime sleep falls from about 500 to about 300 minutes with daytime bout length shortened, while night-time sleep RISES from about 560 to about 650 minutes and the free-running period and rhythmicity are untouched — a day-to-night redistribution, not a uniform loss, with **no rescue arm, one allele, one control background and males only**. 🔴 The human arm is **suggestive by the authors' own statement** (*«the WWOX gene did not reach the conventional genome-wide significance level»*; *«the number of subjects in each cohort was not sufficient for GWAS»*), the reported Bonferroni values imply correction over about 1.8e5 tests rather than the 6.42 million imputed SNVs, and the effect — 12 to 18 minutes — co-moves with **time in bed** while habitual sleep efficiency and the Epworth score do not move at all.
**LIT link:** [[literature_tracking_log_current#LIT-0433]]
**Note:** class-level record; no individual-level detail is carried in this public edition. ⚠️ The declared artefacts of this paper's deep-dive manifest were absent from the corpus at the start of this reading and the manifest was BLOCK; a Europe PMC re-fetch returned byte-identical files (sha256 match on all four), which were restored under their declared names, and the manifest now validates PASS with artefact verification on. Not medical advice.

## PAPER 136
**Short title:** Chang 2015 Cell Death Discov — WWOX dysfunction and the sequential TRAPPC6AΔ/TIAF1/tau/Aβ aggregation cascade
**Full title:** WWOX dysfunction induces sequential aggregation of TRAPPC6AΔ, TIAF1, tau and amyloid β, and causes apoptosis
**Authors:** Chang JY, Chang NS
**Year:** 2015
**Source type:** primary research — cell biology (FRET, co-IP, aggregation assays) plus one mouse genotype
**Journal/source:** *Cell Death Discov* 2015;1:15003
**Identifier:** PMID 27551439 / PMCID PMC4981022 / DOI 10.1038/cddiscovery.2015.3
**Status:** processed
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03, Scientist B). Provisional number: if `PAPER 136` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-27551439-02`; manifest `deepdive_manifests/PMID27551439.json`; dossier `research/fulltext_dossiers/PMID27551439.md`
**Primary pathway:** P4 — proteostasis / aggregation cascade
**Model/species:** cell lines (COS7, HEK293, SK-N-SH, SCC-9, BCC, B16F10, Jurkat, L929), Wwox−/− and Wwox+/+ MEF, Wwox−/− mouse cortex
**Genotype/model:** constitutive Wwox null (mouse) and WWOX knockdown/over-expression in lines; no human allele
**Transferability:** T3 — no neuron with a WWOX genotype; the cell-death assay is transient over-expression and does not discriminate the Δ isoform from wild type
**clinical relevance:** BACKGROUND — fixes the ordering claim of the cascade and bounds it; licenses no therapeutic inference
**Claim links:** 043 (evidence-class bound; this is the paper the bound is measured on)
**Role:** The fixed point of the cascade-ordering claim, and the reading narrows it. The order is inferred from TGF-β1 shuttling kinetics in fibroblasts and from siRNA asymmetry reported in the companion paper; the one endogenous WWOX/TPC6A interaction is a co-IP in HEK293; the apoptosis link is transient over-expression in which wild-type TPC6A is **equally potent** as the Δ isoform. 🔴 Three internal inconsistencies are carried: Results say the Y112F mutant aggregates less and the Discussion says it does not (Figure 5a reports p = 0.040 for Y112F and p = 0.002 for S35G, i.e. the mutant called non-aggregating has the strongest TGF-β1 response); the Discussion names Tyr216 for a step the Results and Figure 5i call Tyr112, in a protein of 159–173 residues; and the S35G mutant is said both to fail to aggregate and to aggregate significantly more under TGF-β1. 🔴 Figure 7 has **no wild-type comparator**: its control is the same Wwox−/− tissue with the antibodies peptide-blocked.
**LIT link:** [[literature_tracking_log_current#LIT-0434]]
**Note:** class-level record; no individual-level detail is carried in this public edition. This paper belongs to a corpus in which one laboratory supplies every record of the mechanism: PubMed 2026-10-02 returns 0 records for `WWOX AND TIAF1 NOT Chang NS[au]` and 4 for `"TRAPPC6A" AND (aggregation OR plaque)`, all four of them this group's. Not medical advice.

## PAPER 137
**Short title:** Chang 2015 Oncotarget — TRAPPC6AΔ as an extracellular plaque-forming protein; pT181-tau in the 3-week-old Wwox-null brain
**Full title:** Trafficking protein particle complex 6A delta (TRAPPC6AΔ) is an extracellular plaque-forming protein in the brain
**Authors:** Chang JY, Lee MH, Lin SR, Yang LY, Sun HS, Sze CI, Hong Q, Lin YS, Chou YT, Hsu LJ, Jan MS, Gong CX, Chang NS
**Year:** 2015
**Source type:** primary research — isoform isolation, antibody production, human post-mortem IHC and filter retardation, mouse knockout IHC
**Journal/source:** *Oncotarget* 2015;6(5):3578–3589
**Identifier:** PMID 25650666 / PMCID PMC4414138 / DOI 10.18632/oncotarget.2876
**Status:** processed
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03, Scientist B). Provisional number: if `PAPER 137` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-25650666-03`; manifest `deepdive_manifests/PMID25650666.json`; dossier `research/fulltext_dossiers/PMID25650666.md`
**Primary pathway:** P4 — proteostasis / aggregation cascade
**Model/species:** human post-mortem cortex and hippocampus; constitutive Wwox knockout mouse (3 weeks); COS7; SK-N-SH; APP/PS1 mouse
**Genotype/model:** constitutive Wwox null (exon 1, and separately exons 2/3/4); no human WWOX allele
**Transferability:** T3 — a constitutive null that dies at about a month models no human missense or splice allele; the human arm has no WWOX genotype
**clinical relevance:** MODERATE — the only tau datum in a young WWOX-null brain in this corpus, now bounded
**Claim links:** 043 (evidence-class bound)
**Role:** The founding paper of the cascade's first node. 🔴 Panel-level reading (from images embedded in the article PDF at 1500–1750 px, because the PMC rasters are 550 px and unreadable) changes two things the earlier partial reading could not see. **(1)** Figure 3A: the human filter-retardation comparison is **null** for this protein — p = 0.942 (TPC6A) and p = 0.850 (TIAF1) — while p-WWOX (0.036), NFT (0.014) and Aβ (0.003) separate on the same blot, so the null is not an assay failure and the abstract's *«preceding Aβ generation»* is a reading of a flat cross-section. **(2)** Figure 5D, the pT181-tau claim: Wwox+/+ ≈ 11, Wwox−/+ ≈ **6**, Wwox−/− ≈ 26 aggregates, n = 5, one bracket p = 0.0176 — **the heterozygote mean is below wild type**, so the panel carries no gene dosage and is a section count, not tau biochemistry. 🔴 The human measurement used the pan-specific antibody, which the Methods say cannot resolve the isoforms; all four antisera are validated by peptide blocking only. ⚠️ The supplementary PDF contradicts the Methods on antibody numbering (84–100/Tyr112 versus 70–86/Tyr116 for the identical peptide).
**LIT link:** [[literature_tracking_log_current#LIT-0435]]
**Note:** class-level record; no individual-level detail is carried in this public edition. This paper belongs to a corpus in which one laboratory supplies every record of the mechanism: PubMed 2026-10-02 returns 0 records for `WWOX AND TIAF1 NOT Chang NS[au]` and 4 for `"TRAPPC6A" AND (aggregation OR plaque)`, all four of them this group's. Not medical advice.

## PAPER 138
**Short title:** Lin 2022 IJMS — MPP+ and TPC6AΔ in a neuroblastoma line; Wwox heterozygote memory and cortical plaques at 10–11 months
**Full title:** Zfra Inhibits the TRAPPC6AΔ-Initiated Pathway of Neurodegeneration
**Authors:** Lin YH, Shih YH, Yap YV, Chen YW, Kuo HL, Liu TY, Hsu LJ, Kuo YM, Chang NS
**Year:** 2022
**Source type:** primary research — cell-line pharmacology, mouse behaviour and immunohistochemistry
**Journal/source:** *Int J Mol Sci* 2022;23(23):14510
**Identifier:** PMID 36498839 / PMCID PMC9739312 / DOI 10.3390/ijms232314510
**Status:** processed
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03, Scientist B). Provisional number: if `PAPER 138` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-36498839-02`; manifest `deepdive_manifests/PMID36498839.json`; dossier `research/fulltext_dossiers/PMID36498839.md`
**Primary pathway:** P4 — proteostasis / aggregation cascade; P7 — heterozygote endpoints
**Model/species:** Wwox+/+, +/− and −/− MEF; SK-N-SH; 3×Tg-AD mice; Wwox+/− and Wwox+/+ mice at 3, 10 and 11 months
**Genotype/model:** constitutive Wwox heterozygote and null (mouse); the treated cohort is 3×Tg-AD with wild-type Wwox
**Transferability:** T3 for the cascade; **T2 for the heterozygote behavioural endpoint**, which is a null/wild-type genotype measured on a cognitive readout
**clinical relevance:** MODERATE — carries the first cognitive endpoint in a WWOX heterozygote found in this corpus
**Claim links:** 032 (fires its stated `REVIVAL_TRIGGER`: *«an EEG/cognitive endpoint in any WWOX heterozygote of any allele»*) · 043 (evidence-class bound)
**Role:** 🟢 The usable content is Figure 5: Wwox+/− mice at 10–11 months perform worse than wild type on novel-object recognition and in the water maze (n = 5; ANOVA with Bonferroni) and carry more hippocampal TPC6AΔ plaques (** p < 0.01), while the authors themselves report that pS37-TIAF1, TIAF1, wild-type TPC6A and pT181-tau are **not** significantly increased in the heterozygote. 🔴 The headline pT12-WWOX result is **contradicted by its own panel**: Figure 7C's immunointensity chart reports **p > 0.05**, and the significant plaque count rests on n = 3 with one of three animals near zero. 🔴 Three internal inconsistencies: Methods say three weekly injections and Results say four; Methods say five mice per group and the Figure 3 legend says ten, naming the groups *«sham»* and *«control»* with no Zfra group; the Figure 5 legend says n = 5 and then n = 20 for the same panels, and Figure 5B's y-axis says *«% Exploration time»* for an escape-latency curve. ⚠️ The paper declares a patent on the intervention it evaluates. ⚠️ Supplementary Figures S1–S5 (including the pT12-WWOX antibody characterisation) were acquired but **not opened**.
**LIT link:** [[literature_tracking_log_current#LIT-0436]]
**Note:** class-level record; no individual-level detail is carried in this public edition. This paper belongs to a corpus in which one laboratory supplies every record of the mechanism: PubMed 2026-10-02 returns 0 records for `WWOX AND TIAF1 NOT Chang NS[au]` and 4 for `"TRAPPC6A" AND (aggregation OR plaque)`, all four of them this group's. Not medical advice.

## PAPER 139
**Short title:** Lee 2017 Alzheimers Dement (N Y) — Zfra4–10 peptide in 3×Tg-AD mice; not a WWOX model
**Full title:** Zfra restores memory deficits in Alzheimer's disease triple-transgenic mice by blocking aggregation of TRAPPC6AΔ, SH3GLB2, tau and amyloid β
**Authors:** Lee MH, Shih YH, Lin SR, Chang JY, Lin YH, Sze CI, Kuo YM, Chang NS
**Year:** 2017
**Source type:** primary research — interventional mouse study plus cell-free biochemistry
**Journal/source:** *Alzheimers Dement (N Y)* 2017;3(2):152–168
**Identifier:** PMID 29067327 / PMCID PMC5651433 / DOI 10.1016/j.trci.2017.02.001
**Status:** processed
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03, Scientist B). Provisional number: if `PAPER 139` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-29067327-02`; manifest `deepdive_manifests/PMID29067327.json`; dossier `research/fulltext_dossiers/PMID29067327.md`
**Primary pathway:** P8 — therapeutic candidates (peptide)
**Model/species:** 3×Tg-AD mice (Psen1 M146V, APPswe, tau P301L) with **wild-type Wwox**; nude mice with melanoma; human post-mortem hippocampus; MCF7, DU145, L929, COS7
**Genotype/model:** no WWOX allele in the treated cohort; one supplementary Wwox+/− behavioural panel with no treatment arm
**Transferability:** T3 — transfer to a congenital biallelic WWOX loss crosses a different gene, a different lesion and a different developmental window
**clinical relevance:** MODERATE as a bounded therapeutic read; it is **not** a WWOX intervention
**Claim links:** 043 (evidence-class bound)
**Role:** 🔴 **Not a WWOX model.** Dose and route, for the record: Zfra4–10 at 2 mM in 100 µL PBS by tail vein, four weekly injections from 10 months, PBS sham as the only comparator — no vehicle-plus-scrambled arm, no dose–response, no pharmacokinetics (the melanoma arm uses 1 mM in water). 🔴 **Blinding and randomisation are not mentioned**: the strings `blind` and `randomi` occur zero times in the fingerprinted artefact. 🔴 Group sizes are inconsistent four ways — Methods 5/5, Figure 1A 6/5, Figure 1B 12/10, Figure 2 3/5 — and the histology statistics are computed over fields (n = 10) and cells (n = 40), not animals. 🔴 **The paper's only WWOX-genotype datum does not reproduce its own legend.** Supplementary Figure 1, now extracted and inspected, claims a drop *«greater than 55%»* at ages 10–12 in Wwox+/− against under 50% in 3×Tg; the figure's axes read 3, >10, 8, 10 months, carry **no genotype label**, contain no age 12, no n per bar and no test, and under either assignment of bar pairs the drops are ≈ 43%/13% and ≈ 52%/33%. 🟢 Earned negatives the authors report against themselves: no neurogenesis, Z cells do not reach the brain, and efficacy fails when treatment starts at 12 months.
**LIT link:** [[literature_tracking_log_current#LIT-0437]]
**Note:** class-level record; no individual-level detail is carried in this public edition. This paper belongs to a corpus in which one laboratory supplies every record of the mechanism: PubMed 2026-10-02 returns 0 records for `WWOX AND TIAF1 NOT Chang NS[au]` and 4 for `"TRAPPC6A" AND (aggregation OR plaque)`, all four of them this group's. Not medical advice.

## PAPER 140
**Short title:** Li 2009 PLoS One — WOX1 activation with CREB and NF-κB in rat DRG after sciatic transection; the pro-death direction
**Full title:** Dramatic co-activation of WWOX/WOX1 with CREB and NF-κB in delayed loss of small dorsal root ganglion neurons upon sciatic nerve transection in rats
**Authors:** Li MY, Lai FJ, Hsu LJ, Lo CP, Cheng CL, Lin SR, Lee MH, Chang JY, Subhan D, Tsai MS, Sze CI, Pugazhenthi S, Chang NS, Chen ST
**Year:** 2009
**Source type:** primary research — in-vivo rat nerve-injury time course, p53-knockout mice, cell-line reporter assays, FRET, immuno-EM
**Journal/source:** *PLoS One* 2009;4(11):e7820
**Identifier:** PMID 19918364 / PMCID PMC2771921 / DOI 10.1371/journal.pone.0007820
**Status:** processed
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03, Scientist B). Provisional number: if `PAPER 140` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-19918364-01`; manifest `deepdive_manifests/PMID19918364.json`; dossier `research/fulltext_dossiers/PMID19918364.md`
**Primary pathway:** P3 — neuronal injury and WWOX directionality
**Model/species:** adult Sprague-Dawley rat DRG and spinal cord; p53−/− mice; HEK-293; SK-N-SH; primary DRG cultures
**Genotype/model:** wild-type rats — endogenous injury-induced WWOX activation, no WWOX allele
**Transferability:** T3 for a loss-of-function genotype; the measurement is of WWOX **gain** of nuclear activity under stress
**clinical relevance:** MODERATE — the one record whose direction is pro-death for activated WWOX, which bears on any strategy that raises WWOX activity
**Claim links:** 044 (directional ambiguity)
**Role:** 🟢 In-vivo time course over two months with sham and contralateral controls. 🔴 Three bounds found at source. **(1)** The directional claim — WOX1 inhibits CREB/CRE/AP-1 and enhances NF-κB — is a **Gal4-fusion luciferase assay after transient over-expression in HEK-293 fibroblasts**; no panel of Figure 5 contains a neuron. **(2)** The chronic accumulation is **not lateralised**: Supplementary Figure S3 gives ≈ 72% of small neurons with nuclear p-WOX1 contralaterally against ≈ 71% ipsilaterally at month 2, with sham already at 31–37%, so axotomy is not its sufficient cause. **(3)** The abstract's *«>65%»* and *«40–65%»* are **bin labels of a categorical heat map** (Figure 4) with no n, no error and no test. Neuronal death at the endpoint is *«less than 5%»*. 🟢 Confirmed at source, discharging `FT-159`: the paper classifies neurons **by diameter only** (<20, 20–30, >30 µm) and the strings `nocicept`, `unmyelin`, `IB4`, `CGRP` and `substance P` occur zero times — the size→modality step is LEGEND's imported convention, not the authors'. ⚠️ One of its 53 references (PNAS 2005, WWOX restoration in lung cancer) carries a 2017 editorial expression of concern and is cited for background only.
**LIT link:** [[literature_tracking_log_current#LIT-0438]]
**Note:** class-level record; no individual-level detail is carried in this public edition. This paper belongs to a corpus in which one laboratory supplies every record of the mechanism: PubMed 2026-10-02 returns 0 records for `WWOX AND TIAF1 NOT Chang NS[au]` and 4 for `"TRAPPC6A" AND (aggregation OR plaque)`, all four of them this group's. Not medical advice.

## PAPER 141
**Short title:** Hsu 2021 Cells — review of WWOX binding partners in neurodegeneration; provenance of the SDR–tau mechanism
**Full title:** WWOX and Its Binding Proteins in Neurodegeneration
**Authors:** Hsu CY, Lee KT, Sun TY, Sze CI, Huang SS, Hsu LJ, Chang NS
**Year:** 2021
**Source type:** secondary — narrative review (PubMed article type includes Review)
**Journal/source:** *Cells* 2021;10(7):1781
**Identifier:** PMID 34359949 / PMCID PMC8304785 / DOI 10.3390/cells10071781
**Status:** processed
**Record provenance:** created by `CC-20261003-B-REGISTRY-01` (intake wave 2 2026-10-03, Scientist B). Provisional number: if `PAPER 141` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.
**Evidence depth:** secondary source — a review carries no reading depth of its own; receipt `FTR-20261003-34359949-02` records a `partial_fulltext_read` of the review text, Table 1 and all figure legends
**Primary pathway:** P4 — proteostasis / aggregation cascade (provenance record)
**Model/species:** none — no cohort, no experiment; its three figures are schematics
**Genotype/model:** none
**Transferability:** n/a — a review contributes no transferable datum; nothing may inherit DATO status from it
**clinical relevance:** BACKGROUND — provenance only
**Claim links:** 043 (evidence-class bound; the review is where the mechanism is stated most compactly) · 044 (the two-phospho-state proposal, cited by `CLAIM 044` as an unreconciled direction, not as a measurement) [added 2026-10-03 by `CC-20261004-MIRROR-02`, Mirror F2 on `BATCH_20261003_001`]
**Role:** 🔴 **The sentence that matters most for an SDR-destabilising allele occurs only in this review's abstract.** *«WWOX binds Tau via its C-terminal SDR domain»* occurs exactly once in the fingerprinted artefact, inside `<abstract>`, and **zero times in the body**; the body states only the GSK-3β version, attributed to two same-laboratory primaries (Sze 2004 J Biol Chem, PMID 15126504, which LEGEND holds as abstract-only; and Wang 2012 Cell Death Differ, PMID 22193544). There is no third, independent primary. 🔴 *«it only takes less than 15 days after birth»* is a **ceiling imposed by the null mouse's one-month lifespan**, not a measured latency, and is juvenile rather than embryonic. 🔴 *«the stronger the binding, the better»* is an **analogy transferred from cancer suppression**, used in §10.3 to motivate a therapeutic programme, with no neuronal measurement. 🟢 The review is self-critical in one place that applies to its own group's data: on the p73 literature it writes that *«transient overexpression may cause artificial binding effects»*.
**LIT link:** [[literature_tracking_log_current#LIT-0439]]
**Note:** class-level record; no individual-level detail is carried in this public edition. This paper belongs to a corpus in which one laboratory supplies every record of the mechanism: PubMed 2026-10-02 returns 0 records for `WWOX AND TIAF1 NOT Chang NS[au]` and 4 for `"TRAPPC6A" AND (aggregation OR plaque)`, all four of them this group's. Not medical advice.

## PAPER 142
**Short title:** Dudekula 2010 Aging — Zfra in mitochondrial apoptosis; a perspective that performs no experiment
**Full title:** Zfra is a small wizard in the mitochondrial apoptosis
**Authors:** Dudekula S, Lee MH, Hsu LJ, Chen SJ, Chang NS
**Year:** 2010
**Source type:** secondary — narrative perspective; `research-article` in the JATS deposit and *Journal Article* in PubMed, but the article has **no Methods, no Results**, one schematic figure and a 51-entry reference list
**Journal/source:** *Aging (Albany NY)* 2010;2(12):1023–1029
**Identifier:** PMID 21212468 / PMCID PMC3034171 / DOI 10.18632/aging.100263
**Status:** processed
**Record provenance:** 🔴 **Identity landing written by `BATCH_20261003_001`, not by the reader.** The reading is intake wave 3's, by ACTOR_ID `scientist` (Scientist B), branch `task/sci-B-20261003w3`, and its receipt landed on `main` with no registry record of any kind — which is `ORPHAN_COMPLETE_READ`, a `BLOCK_BATCH_COMMIT` that stopped every batch, not only its own wave's. Every field here is transcribed from that reading's own receipt, manifest and dossier. **The scientific landing was completed on 2026-10-03 by `BATCH_20261003_002`**, from wave 3 B's own candidate `CC-20261003W3-B-REGISTRY-01` — the reading's author — and not by the integrator, who did not open the article. What that candidate assesses, carried verbatim in its terms: `Primary pathway` mitochondrial apoptosis / Zfra-WWOX antagonism; `Model/species` none, a secondary account of cell-line experiments published elsewhere; `Genotype/model` none, every statement is about ectopically overexpressed Zfra or WOX1; `Transferability` T4 — overexpression in cancer lines, no neuron, no human allele; `clinical relevance` LOW, useful as an endpoint map (Bcl-2-family level, cytochrome-c release and membrane potential are separable endpoints) and not as evidence; `Claim links` none. The Zfra-versus-WWOX relation it describes is an inhibition of a GAIN-of-function effect, and the article states the endogenous question as open in its own words. Not a duplicate record: the identity landing of 2026-10-03 and this scientific landing are the same record, completed.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-21212468-01`; manifest `deepdive_manifests/PMID21212468.json`; dossier `research/fulltext_dossiers/PMID21212468.md`. Coverage as the receipt declares it: body and figure read, tables and supplements `not_present`.
**Primary pathway:** organelle-level apoptosis (Zfra / WWOX), as the wave's own selection question framed it
**Model/species:** none — the article reports no experiment of its own
**Genotype/model:** none
**Transferability:** n/a — a perspective contributes no transferable datum; nothing may inherit `DATO` status from it
**clinical relevance:** BACKGROUND — provenance only
**Claim links:** none
**Role:** 🔴 **Nothing in this article is a new measurement.** Its organelle statements — Zfra binding the first WW and the SDR domain, Ser8 phosphorylation and relocation to mitochondria, Bcl-2 / Bcl-xL downregulation without cytochrome-c release, membrane-potential dissipation — are each **cited** to earlier primaries of the same laboratory, and the dossier records that three of them carry one and the same citation. The article states its own limit: whether endogenous Zfra blocks the apoptotic function of p53 and WOX1 *«remains to be determined»*. No n, no statistic and no effect size appears anywhere, and there is no neuronal datum.
**LIT link:** [[literature_tracking_log_current#LIT-0440]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 143
**Short title:** Nagarajan 2023 Epilepsia Open — genetic IESS in 124 children; four biallelic WWOX with per-patient treatment and outcome
**Full title:** Landscape of genetic infantile epileptic spasms syndrome — A multicenter cohort of 124 children from India
**Authors:** Nagarajan B, Gowda VK, Yoganathan S, et al.; Sahu JK
**Year:** 2023
**Source type:** primary research — multicentre cross-sectional cohort of genetically confirmed IESS
**Journal/source:** *Epilepsia Open* 2023;8:1383-1404
**Identifier:** PMID 37583270 / PMCID PMC10690684 / DOI 10.1002/epi4.12811
**Status:** processed
**Record provenance:** created by `CC-20261003W3-A-REGISTRY-01` (intake wave 3 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-37583270-01` (earlier: `FTR-20260921-37583270-01`, partial); manifest `deepdive_manifests/PMID37583270.json`; dossier `research/fulltext_dossiers/PMID37583270.md`
**Primary pathway:** clinical spectrum / WWOX-DEE · drug response (spasms)
**Model/species:** human
**Genotype/model:** four children (Table 1 rows 37-40): frameshift + nonsense (x2, compound heterozygous as stated); in-frame exons 6-8 deletion + `c.517-3C>A` (compound heterozygous as stated; neither consequence measured); homozygous `c.790C>T p.Arg264Ter`. Phase not shown for the compound genotypes.
**Transferability:** T1 for the clinical course of predicted-null genotypes; none for missense classes
**clinical relevance:** MODERATE — the only multi-patient WWOX series in LEGEND with per-patient spasm treatment and outcome
**Claim links:** 001 (vigabatrin observation, through `CC-20261003W3-A-VIGABATRIN-01`)
**Role:** Spasm onset 2-4 months; microcephaly and central hypotonia in all four. Clinical spasm control (≥ 4 weeks, no electrographic criterion) with vigabatrin, nitrazepam or zonisamide in three at 6-12 months; the homozygous p.Arg264Ter child drug-refractory with a failed ketogenic diet at 30 months. 🔴 No denominator of all IESS; p.Trp398Ter is labelled 'missense' in the source; the deletion column says 'exons 5 to 8' for a c.517-c.1056 span; row 39's outcome reads 'persistent spasms' and 'seizure-free' together; none of the four rows is marked as previously published, but the children were tested from January 2018 and overlap with earlier reports is not excluded by the source. 🔴 **One specific candidate (`CC-20261004W7-B-PATIENT-OVERLAP-01`, intake wave 7):** the homozygous `p.Arg264Ter` child here and the homozygous `p.Arg264*` sibling pair of [[paper_registry_current#PAPER 117]] (Piard 2019 Supplementary Table 1 patients 13-14: origin India, consanguineous; patient 14 male, 18 months at last examination) share allele and country; nothing printed in either excludes identity. Until a primary or the authors settle it, count at most three and possibly two p.Arg264* homozygotes across the two papers. The two Turkish p.Arg264* homozygotes of [[paper_registry_current#PAPER 205]] are a separate population and do not overlap either. `PREMISE: INFERENZA`.
**LIT link:** [[literature_tracking_log_current#LIT-0441]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 144
**Short title:** Sukkar 2022 Cureus — homozygous WWOX c.406A>G (p.Ile136Val) in a child WITHOUT seizures; attribution unproven
**Full title:** Novel Mutation With Literature Review: WW Domain-Containing Oxidoreductase (WWOX) Gene
**Authors:** Sukkar G, Alzahrani RM, Altirkistani BA, Al Lohaibi RS
**Year:** 2022
**Source type:** primary research — single case report with a literature table
**Journal/source:** *Cureus* 2022;14(5):e25003
**Identifier:** PMID 35712340 / PMCID PMC9193507 / DOI 10.7759/cureus.25003
**Status:** processed
**Record provenance:** created by `CC-20261003W3-A-REGISTRY-01`; promotes [[paper_registry_current#CORPUS-STUB-141]] (kept as history). Provisional number.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35712340-01` (earlier: `FTR-20260921-35712340-01`, partial); manifest `deepdive_manifests/PMID35712340.json`; dossier `research/fulltext_dossiers/PMID35712340.md`
**Primary pathway:** clinical spectrum — boundary case
**Model/species:** human
**Genotype/model:** homozygous missense `c.406A>G` (`p.Ile136Val` in the source's Table 3), four nucleotides upstream of the exon 4 donor; splice alteration predicted in silico only; DNA only
**Transferability:** none — the genotype-phenotype attribution is not established
**clinical relevance:** LOW
**Claim links:** none
**Role:** 🔴 **Do not count as a WOREE or SCAR12 case.** No **early** seizure disorder in the source's own words (Discussion para 1; at 21 months, with an 'abnormal gaze around three times' noted and not called a seizure) (integrator amendment, `BATCH_20261003_002`), normal MRI, walking and ten words at 21 months; raised CK, cholestasis and low lipids asserted, not shown, to be WWOX-related; an affected sibling with seizures was not genotyped. The literature table (Table 3) attributes `c.160G>T` to two unrelated reports and is not a count source.
**LIT link:** [[literature_tracking_log_current#LIT-0160]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 145
**Short title:** Serce Pehlevan 2026 J Paediatr Child Health — homozygous WWOX p.Leu239Arg with neonatal–infantile hypokinetic–rigid features; neurotransmitters not measured
**Full title:** WWOX Mutation as a Rare Cause of Neonatal-Infantile Parkinsonism Mimicking a Neurotransmitter Disorder: A Case Report
**Authors:** Serce Pehlevan O, Gider Yaman G, Gok A, Tekin Orgun L
**Year:** 2026
**Source type:** primary research — single case report
**Journal/source:** *J Paediatr Child Health* 2026;62(7):1273-1277
**Identifier:** PMID 42092735 / PMCID PMC13378201 / DOI 10.1111/jpc.70401
**Status:** processed
**Record provenance:** created by `CC-20261003W3-A-REGISTRY-01` (resolves `FT-106`). Provisional number.
**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-42092735-01` (every section read; partial only because the cited prior report of the allele, PMID 30094525, is queued in the manifest); earlier `FTR-20260921-42092735-01`; manifest `deepdive_manifests/PMID42092735.json`; dossier `research/fulltext_dossiers/PMID42092735.md`
**Primary pathway:** clinical spectrum / movement phenotype
**Model/species:** human
**Genotype/model:** homozygous missense `c.716T>G p.(Leu239Arg)`; carrier parents; DNA only
**Transferability:** T3 for any allele-level movement phenotype (n = 1, confounded)
**clinical relevance:** MODERATE — a presentation a clinician may take for a monoamine disorder
**Claim links:** 001 (vigabatrin observation, through `CC-20261003W3-A-VIGABATRIN-01`)
**Role:** Hypokinetic-rigid features with hypomimia from the neonatal period, persisting at 4 months. 🔴 CSF neurotransmitters were never measured and no dopaminergic drug was tried, so 'mimicking a neurotransmitter disorder' is a clinical working diagnosis, not a tested one; perinatal confounders (resuscitation, a thalamic diffusion focus) are present. Spasms continued on vigabatrin + phenobarbital and stopped on valproate + clobazam (one month seizure-free at 4 months). Its cited prior report of the allele is Serin 2018 (PMID 30094525), not [[paper_registry_current#PAPER 013]] from the same university, which it does not cite; identity with that cohort's case 49 is not excluded — do not sum carriers (see `CC-20261003W3-A-L239R-01`).
**LIT link:** [[literature_tracking_log_current#LIT-0442]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 146
**Short title:** Lee 2010 Cell Death Dis - TGF-beta1 drives TIAF1 self-aggregation independently of the type II receptor, and aggregated TIAF1 precedes amyloid in vitro
**Full title:** TGF-β induces TIAF1 self-aggregation via type II receptor-independent signaling that leads to generation of amyloid β plaques in Alzheimer's disease
**Authors:** Lee MH, Lin SR, Chang JY, et al.; Sze CI, Chang NS
**Year:** 2010
**Source type:** primary research - cell biology and postmortem human tissue
**Journal/source:** *Cell Death Dis* 2010;1:e110
**Identifier:** PMID 21368882 / PMCID PMC3032296 / DOI 10.1038/cddis.2010.83
**Status:** processed
**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 146` / `LIT-0443`. The integrator renumbers in event order and updates the anchors.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-21368882-01`; manifest `deepdive_manifests/PMID21368882.json`; dossier `research/fulltext_dossiers/PMID21368882.md` (figure panels read as legends only)
**Primary pathway:** protein aggregation / TIAF1-APP cascade
**Model/species:** cell lines (COS7, L929, Mv1Lu, HCT116, NCI-H1299, SK-N-SH, SH-SY5Y and others), postmortem human hippocampus, APP/PS1 and APP transgenic mouse
**Genotype/model:** no WWOX genotype - WWOX is not manipulated or measured in this paper
**Transferability:** T4 for WWOX: this is the upstream link of the TIAF1 cascade, not a WWOX experiment
**clinical relevance:** LOW for WWOX directly; MODERATE as the primary behind the TIAF1 arm of the aggregation cascade
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** WWOX/WOX1 occurs three times in the whole article - a yeast-two-hybrid positive control, a cited background sentence on the TGF-beta1/Hyal-2/WOX1/Smad4 route, and one Discussion sentence on C1q - with no WWOX manipulation, readout or figure. What it does fix: TIAF1 aggregation is TbetaRII-independent and Smad4 prevents it; human hippocampal filter retardation gives TIAF1 aggregates in 59.0% of nondemented (n=41, age 59.0±17.0) and 54% of Alzheimer samples (n=97, age 80.0±8.8), with Aβ in 15% and 48%. ⚠️ The 'aggregation precedes amyloid' inference is cross-sectional across two groups that differ by ~21 years of mean age, and TIAF1 aggregation itself is not higher in the demented group. ⚠️ The abstract says aggregation causes Thr668 DEphosphorylation; the Results say TIAF1 overexpression INCREASED Thr668 phosphorylation and TGF-beta1 suppressed it - carry the two-step form.
**LIT link:** [[literature_tracking_log_current#LIT-0443]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 147
**Short title:** Su 2026 Cells - stress-induced WWOX degrades Bcl-XL/Mcl-1 through a lysosomal route, and WWOX-null cells SURVIVE serum starvation better than wild type
**Full title:** WWOX Induction Promotes Bcl-X<sub>L</sub> and Mcl-1 Degradation Through a Lysosomal Pathway upon Stress Responses
**Authors:** Su YH, Chiang W, Wang YY, Kung YH, Cheng PS, Chang TH, Chang NS, Lai FJ, Hsu LJ
**Year:** 2026
**Source type:** primary research - cell biology
**Journal/source:** *Cells* 2026;15:270
**Identifier:** PMID 41677633 / PMCID PMC12897155 / DOI 10.3390/cells15030270
**Status:** processed
**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41677633-02` (earlier: `FTR-20260920-41677633-01`, partial, over a text extraction); manifest `deepdive_manifests/PMID41677633.json`; dossier `research/fulltext_dossiers/PMID41677633.md`
**Primary pathway:** organelle biology / proteostasis / redox
**Model/species:** primary mouse embryonic fibroblasts (`Wwox+/+` and `Wwox-/-`), HeLa Tet-On, human SCC-15
**Genotype/model:** constitutive mouse null versus wild type; inducible ectopic WWOX; shRNA knockdown. No heterozygote arm, no human missense or splice allele
**Transferability:** T3 for the direction of effect; T4 for mechanism in neurons - nothing in this paper is neural
**clinical relevance:** MODERATE - three measurable organelle endpoints (ΔΨm, ROS, anti-apoptotic Bcl-2-family protein level) with a pharmacological handle (NAC)
**Claim links:** none
**Role:** 🔴 **Direction: under serum starvation the WWOX-NULL cell is the surviving cell.** ⚠️ The direction is attested by the Results text (3.3, 3.6); the approximate magnitudes that follow were read off the panels by the reader and no panel locator was persisted — the receipt declares `figures: captions_only` — so they are a reading aid, not a locatored datum (integrator amendment, `BATCH_20261003_002`). Viability ~35%→~21% at 72 h in `Wwox+/+` against ~40% flat to 96 h in `Wwox-/-` (Fig 4A); sub-G0/G1 ~21% vs ~11% (Fig 4B); ΔΨm falls to ~0.34 of control in `Wwox+/+` and stays ~0.79 in `Wwox-/-` (Fig 4C); ROS rises more in `Wwox+/+` at 6-48 h and is EQUAL at baseline (Fig 8A). Bcl-XL and Mcl-1 fall post-transcriptionally in `Wwox+/+` only; MG132 does not rescue, chloroquine, E64d and pepstatin A do. ⚠️ No autophagic-flux assay anywhere; the lysosomal route is inhibitor pharmacology on static westerns, and the authors ask for the genetic test themselves. ⚠️ Neither Bcl-XL nor Mcl-1 co-immunoprecipitates with WWOX. ⚠️ Text-versus-panel: the Results name chloroquine as the rescuing lysosome inhibitor and Figure S3B shows NH₄Cl, in the same experiment, failing to rescue.
**LIT link:** [[literature_tracking_log_current#LIT-0165]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 148
**Short title:** Tsai 2013 Cell Death Dis - WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated squamous carcinoma; the flux clamp is on the drug, never on WWOX
**Full title:** WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated human squamous cell carcinoma
**Authors:** Tsai CW, Lai FJ, Sheu HM, et al.; Chang NS, Hsu LJ
**Year:** 2013
**Source type:** primary research - cell biology with tumour biopsies
**Journal/source:** *Cell Death Dis* 2013;4:e792
**Identifier:** PMID 24008736 / PMCID PMC3789168 / DOI 10.1038/cddis.2013.308
**Status:** processed
**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-24008736-02` (earlier: `FTR-20260921-24008736-01`, partial, no figures); manifest `deepdive_manifests/PMID24008736.json`; dossier `research/fulltext_dossiers/PMID24008736.md`. Partial for one reason only: the supplement deposited under this identifier is a different article's supplement (see `CC-20261003W3-B-SUPPDEPOSIT-01`)
**Primary pathway:** autophagy / mTOR / chemosensitivity
**Model/species:** human SCC-4, SCC-9, SCC-15; tumour biopsies; one sentence of `Wwox` knockout MEF data
**Genotype/model:** ectopic WWOX overexpression, siRNA and shRNA knockdown, Y33R dominant-negative; `Wwox+/-` and `Wwox-/-` MEFs in the unreachable Supplementary Figure 7
**Transferability:** T3 for the sign in epithelial cancer under antimetabolite stress; T4 for neurons and for any constitutive human genotype
**clinical relevance:** MODERATE - the readable half of the autophagy-direction disagreement
**Claim links:** none
**Role:** Direction: WWOX reduces Beclin-1, Atg12-Atg5, LC3-II, GFP-LC3 puncta and EM autophagosomes, and co-immunoprecipitates with mTOR while raising p-mTOR and p-p70S6K. 🔴 **The lysosomal clamp (E64d + pepstatin A) is applied to METHOTREXATE, never to a WWOX manipulation** (Fig 3c: LC3-II 1.6→1.0 under the clamp at 12 h), so the WWOX→autophagy step is never measured as flux. ⚠️ The mTOR causal order is stated as a possibility by the authors. ⚠️ LC3 loss is routed to the PROTEASOME here (MG132 blocks it), which is a different route from the lysosomal one the same laboratory later assigns to Bcl-XL/Mcl-1 in the same SCC-15 background - different cargo, not one mechanism stated twice. ⚠️ The paper's own scope sentence binds the direction to a drug, a tumour and an apoptotic endpoint. Integrity: no notice on this paper; its reference 15 (PNAS 2005) carries a 2017 expression of concern (`dependency_integrity.py screen`, 2026-10-03).
**LIT link:** [[literature_tracking_log_current#LIT-0158]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 149
**Short title:** Chen 2024 Int J Mol Sci - 'Zfra overrides WWOX' is asserted by a perspective review with no head-to-head experiment
**Full title:** Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration
**Authors:** Chen YA, Liu TY, Wen KY, Hsu CY, Sze CI, Chang NS
**Year:** 2024
**Source type:** perspective review
**Journal/source:** *Int J Mol Sci* 2024;25:3507
**Identifier:** PMID 38542478 / PMCID PMC10970703 / DOI 10.3390/ijms25063507
**Status:** processed
**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-38542478-01`; manifest `deepdive_manifests/PMID38542478.json`; dossier `research/fulltext_dossiers/PMID38542478.md` (figure panels read as legends only)
**Primary pathway:** therapeutic strategy / Zfra peptide / WWOX phospho-code
**Model/species:** none of its own
**Genotype/model:** none of its own; cites a heterozygous `Wwox` mouse cortex finding (pT12-WWOX aggregates) and 3xTg-AD mice
**Transferability:** T4 - no measurement in this article
**clinical relevance:** MODERATE - it is the only source stating a RANK ORDER between a Zfra strategy and a WWOX strategy, which decides whether the two are additive or antagonistic
**Claim links:** none
**Role:** 🔴 **The hierarchy is asserted, not measured.** Section 11 says *'We determined that Zfra overrides WWOX...'*; section 11.2 says *'Zfra may override WWOX deficiency...'*. No experiment in this article - it performs none - and none it cites compares a WWOX-restoration arm with a Zfra arm in one model. The one head-to-head datum is the opposite kind: Zfra4-10 and WWOX7-21 given TOGETHER lose the antitumour effect each has alone. ⚠️ Useful import: it carries two independent-laboratory references on this group's question - PMID 33300063 (WWOX inhibits autophagy, ovarian carcinoma) and PMID 35984507 (blocking WWOX restores mitochondrial homeostasis in neuronal cells under high glucose).
**LIT link:** [[literature_tracking_log_current#LIT-0037]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 150
**Short title:** Liu 2018 Front Neurosci - the WWOX phospho-code maps to compartment and cell fate, and to NO measured organelle endpoint
**Full title:** WWOX Phosphorylation, Signaling, and Role in Neurodegeneration
**Authors:** Liu CC, Ho PC, Lee IT, et al.; Sze CI, Chiang MF, Chang NS
**Year:** 2018
**Source type:** review with one original database analysis
**Journal/source:** *Front Neurosci* 2018;12:563
**Identifier:** PMID 30158849 / PMCID PMC6104168 / DOI 10.3389/fnins.2018.00563
**Status:** processed
**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-30158849-02` (earlier: `FTR-20260811-30158849-01`, partial, over an artefact absent from this checkout); manifest `deepdive_manifests/PMID30158849.json`; dossier `research/fulltext_dossiers/PMID30158849.md`
**Primary pathway:** WWOX phospho-code / neurodegeneration
**Model/species:** none of its own except a public brain-expression database analysis
**Genotype/model:** none of its own
**Transferability:** T4 as evidence; T1 as a map of what the phospho-code is claimed to do
**clinical relevance:** MODERATE - it is LEGEND's named source for the phospho-code, and the open debt `FT-057`
**Claim links:** none
**Role:** 🔴 **Measured answer to the question it was read for: the residue-to-organelle-endpoint mapping does not exist in this source.** pY33 is mapped to mitochondrial/nuclear relocation and apoptosis, pS14 to differentiation and disease progression, pY287 to proteasomal turnover; pT12 is ABSENT from this 2018 review and appears only in the group's 2024 one. No residue is tied to a measured ΔΨm, ROS, lysosomal or autophagic readout. The lysosome appears once, in an uncited list of compartments. ⚠️ One transferable direction is stated for the constitutive null: *'If cells are devoid of WWOX (e.g., Wwox-/- MEF), cell death is retarded'*. The ROS/SDR link is carried from two laboratories that are not the authoring group.
**LIT link:** [[literature_tracking_log_current#LIT-0033]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 151
**Short title:** Tarta-Arsene 2017 Epileptic Disord — one WOREE patient, normal head circumference; the same patient as Piard 2019 P8
**Full title:** Practical clues for diagnosing WWOX encephalopathy
**Authors:** Tarta-Arsene O, Barca D, Craiu D, Iliescu C
**Year:** 2017
**Source type:** primary research — clinical commentary on a single case
**Journal/source:** *Epileptic Disord* 2017;19(3):357-361
**Identifier:** PMID 28721938 / DOI 10.1684/epd.2017.0924 — bronze OA (publisher PDF)
**Status:** processed
**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. No earlier `CORPUS`, `PAPER` or `LIT` record existed (`FT-121`).
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-28721938-01`; manifest `deepdive_manifests/PMID28721938.json`; dossier `research/fulltext_dossiers/PMID28721938.md`
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** compound heterozygous `c.173-1G>T` (intron 2 acceptor; splice effect predicted in this paper, measured as exon 3 skipping for the same allele in another patient of PMID 30356099) + `c.918del p.(Glu306Aspfs*21)`; predicted null / null
**Transferability:** T1 for the null/null clinical course
**clinical relevance:** MODERATE
**Claim links:** none
**Role:** Normal head circumference throughout with progressive atrophy; first MRI (5 weeks) thin corpus callosum with normal myelination **for age**, while the second MRI (2.6 years) records delayed myelination — cite the age with the finding (BATCH_20261003_003, blind locator audit); death at almost 3 years. 🔴 **Count once:** identical genotype and every compared attribute match [[paper_registry_current#PAPER 117]] Patient 8, which Piard presents as novel without citing this report (`PREMISE: INFERENZA`, `CC-20261003W4-A-PATIENT-OVERLAP-01`). Do not sum the two sources.
**LIT link:** [[literature_tracking_log_current#LIT-0444]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 152
**Short title:** Zhao 2020 Mol Med Rep — WWOX lowers Beclin-1/LC3 and raises p-mTOR in paclitaxel-treated ovarian carcinoma lines; flux not clamped on any WWOX arm
**Full title:** WWOX promotes apoptosis and inhibits autophagy in paclitaxel-treated ovarian carcinoma cells
**Authors:** Zhao Y, Wang W, Pan W, Yu Y, Huang W, Gao J, Zhang Y, Zhang S
**Year:** 2020
**Source type:** primary research — cell-line study
**Journal/source:** *Mol Med Rep* 2021;23(2):115 (epub 2020-12-10)
**Identifier:** PMID 33300063 / DOI 10.3892/mmr.2020.11754 — bronze OA (publisher PDF)
**Status:** processed
**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-056]] (kept as history).
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-33300063-01`; manifest `deepdive_manifests/PMID33300063.json`; dossier `research/fulltext_dossiers/PMID33300063.md`
**Primary pathway:** autophagy / mTOR (cancer)
**Model/species:** human ovarian carcinoma cell lines
**Genotype/model:** plasmid overexpression and one siRNA in A2780 / A2780-T / SKOV3; no human allele modelled
**Transferability:** T3 — epithelial cancer lines, overexpression
**clinical relevance:** LOW
**Claim links:** none
**Role:** Sign on steady-state abundance: WWOX up → Beclin-1 and LC3 down, p-mTOR up; WWOX down → the reverse (representative blots, no densitometry, no statistics). The only chloroquine clamp is on the paclitaxel arm; p-p70S6K barely detected although the Discussion says 'mTOR/p70S6K'; no mTOR-inhibitor epistasis. The abstract's 'reduced WWOX' in the resistant line contradicts its Results (highest basal WWOX there). See `FT-074`, `CC-20261003W4-A-AUTOPHAGY-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0080]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 153
**Short title:** Kośla 2020 Exp Biol Med — review, WWOX in brain development and pathology (Lodz group)
**Full title:** The WWOX gene in brain development and pathology
**Authors:** Kośla K, Kałuzińska Ż, Bednarek AK
**Year:** 2020
**Source type:** **narrative review** — no primary data
**Journal/source:** *Exp Biol Med (Maywood)* 2020;245(13):1122-1129
**Identifier:** PMID 32389029 / PMCID PMC7400721 / DOI 10.1177/1535370220924618
**Status:** processed
**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-007]] (kept as history).
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-32389029-01` (figure images unobtainable; schematics read as captions); manifest `deepdive_manifests/PMID32389029.json`; dossier `research/fulltext_dossiers/PMID32389029.md`
**Primary pathway:** CNS development / review
**Model/species:** review
**Genotype/model:** n/a
**Transferability:** T3 — background only
**clinical relevance:** LOW
**Claim links:** none — background
**Role:** Background only, not a claim source. Same group as [[paper_registry_current#PAPER 154]]; the two are not independent. 🔴 Its Table 1 reference numbers disagree with its running text for the same findings; its WOREE definition ('premature STOP codons in two alleles … complete lack of WWOX') is narrower than the cohort it cites; the heterozygous-animal memory sentence is cited to a Zfra/3xTg paper and is unverified; 'in great majority may be lethal in embryonic development' is uncited.
**LIT link:** [[literature_tracking_log_current#LIT-0034]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 154
**Short title:** Baryła 2022 J Mol Med — review, WWOX and metabolic regulation (Lodz group)
**Full title:** WWOX and metabolic regulation in normal and pathological conditions
**Authors:** Baryła I, Kośla K, Bednarek AK
**Year:** 2022
**Source type:** **narrative review** — no primary data
**Journal/source:** *J Mol Med (Berl)* 2022;100(12):1691-1702
**Identifier:** PMID 36271927 / PMCID PMC9691486 / DOI 10.1007/s00109-022-02265-5
**Status:** processed
**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Only `LIT-0029` existed (no `CORPUS` or `PAPER` record).
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-36271927-01` (earlier `FTR-20260921-36271927-01`, partial: no figure, no bibliography); manifest `deepdive_manifests/PMID36271927.json`; dossier `research/fulltext_dossiers/PMID36271927.md`
**Primary pathway:** metabolism / review
**Model/species:** review
**Genotype/model:** n/a
**Transferability:** T3 — background only
**clinical relevance:** LOW
**Claim links:** none — background
**Role:** Background only. The HIF1A arc resolves to refs 26, 14, 15, 74, 84, 88; refs 15 and 74 are the authors' own. 🔴 'MRI of WOREE patients … usually shows also reduced myelination' is not supported by its cited Piard aggregate (delayed myelination 2/34) and its evidence list cites one patient twice (refs 13 and 66). Osteopenia, listed in the abstract beside human conditions, rests on homozygous knockout mice only. See `FT-111`, `CC-20261003W4-A-REVIEWS-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0029]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 155
**Short title:** Li 2014 Int J Biol Sci — review, WWOX in metabolic disorders and tumours
**Full title:** Common Chromosomal Fragile Site Gene WWOX in Metabolic Disorders and Tumors
**Authors:** Li J, Liu J, Ren Y, Yang J, Liu P
**Year:** 2014
**Source type:** **narrative review** — no primary data
**Journal/source:** *Int J Biol Sci* 2014;10(2):142-148
**Identifier:** PMID 24520212 / PMCID PMC3920169 / DOI 10.7150/ijbs.7727
**Status:** processed
**Record provenance:** created by `CC-20261003W4-A-REGISTRY-01` (intake wave 4 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-037]] (kept as history).
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-24520212-01`; manifest `deepdive_manifests/PMID24520212.json`; dossier `research/fulltext_dossiers/PMID24520212.md`
**Primary pathway:** metabolism / tumour suppression / review
**Model/species:** review
**Genotype/model:** n/a
**Transferability:** T3 — background only
**clinical relevance:** LOW
**Claim links:** none — background
**Role:** Background only; nothing neural. 🔴 **Do not cite for the heterozygote tumour figure:** it attaches 10/58 vs 2/60 to ENU-treated mice and lung papillary carcinoma, whereas the corpus's reading of the cited primary ([[paper_registry_current#PAPER 078]], `CLAIM 032`) has those numbers as spontaneous tumours. Its skeletal sentence says 'mice' and cites the rat *lde* paper.
**LIT link:** [[literature_tracking_log_current#LIT-0061]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.
## PAPER 156
**Short title:** Dong 2022 JLR — exome sequencing in hypoalphalipoproteinemia
**Full title:** Whole-exome sequencing reveals damaging gene variants associated with hypoalphalipoproteinemia
**Year:** 2022
**Source type:** human genomic discovery study (whole-exome sequencing, candidate-gene filter + binomial burden test)
**Journal/source:** *Journal of Lipid Research* 2022;63(6):100209
**Identifier:** PMID 35460704 / PMCID PMC9126845 / DOI 10.1016/j.jlr.2022.100209
**Status:** processed
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — ricevuta `FTR-20261003-35460704-01`, JATS Europe PMC, manifest `deepdive_manifests/PMID35460704.json` (6 locator, validatore PASS con `--verify-artifacts`), dossier `fulltext_dossiers/PMID35460704.md`. Parziale: Figure 1 e 3 ispezionate come immagini (ricevuta `FTR-20261004-35460704-02`, wave 9; Figura 2, LDLR, per legenda), lista dei riferimenti non letta.
**Integrity status:** clean
**Primary pathway:** P5 — metabolismo / lipidi
**Model/species:** umano, 204 persone selezionate per HDL-C sotto il 10º percentile di una sola coorte di ricerca
**Genotype/model:** nessuna perturbazione; varianti rare annotate in silico
**Transferability:** T3
**clinical relevance:** LOW
**Claim links:** 045
**Role:** il negativo umano più nitido disponibile sull'eterozigote WWOX
**Note:** 🔴 **DO_NOT_CITE come «quattro portatori WWOX con un'anomalia biochimica».** Le quattro «occorrenze» WWOX sono **tre alleli missenso eterozigoti distinti** — p.Gly30Arg (gnomAD 5.61 × 10⁻⁶, 1 partecipante), p.Arg120Trp (gnomAD 7.50 × 10⁻³, ClinVar **Benign**, 2 partecipanti), p.Leu307Val (gnomAD 5.28 × 10⁻⁵, 1 partecipante) — senza alcun allele loss-of-function, frameshift, di splicing o omozigote. WWOX **non** raggiunge la significatività nel burden test (la raggiungono ABCA1, LDLR, HK3, CFTR); nessun valore lipidico è riportato per un portatore WWOX; e gli autori stessi dichiarano di non avere coorte di confronto a HDL-C normale. Earned null utile: **nessun evento di copy-number** in alcuno dei 104 geni candidati HDL, quindi nessuna delezione o duplicazione WWOX in questa coorte, entro l'insensibilità dichiarata del CNV calling da esoma. «Probably damaging» è una predizione di dieci strumenti, non un saggio. [Wave 9, pannelli: la barra WWOX della Figura 1 vale 4 ed è interamente missenso; nessuna statistica WWOX è stampata in Figura 3 né nel testo. ⚠️ **Emendamento da audit cieco dei locator, 2026-10-04:** l'intestazione della Figura 1 («144 occurrences in 101 patients») non concorda né con i **110 portatori** del testo né con la **coorte di 204 partecipanti** stampata nel testo e nei Metodi — i 110 sono i portatori di almeno una variante, **non** il totale di coorte, e una lettura precedente li aveva etichettati come tale; la discrepanza resta nei totali di coorte e non nel conteggio WWOX. Lo stesso audit rileva che il «No CNVs were found» del paper è limitato ai 104 geni candidati HDL e a un metodo che gli autori stessi dicono spesso poco sensibile.]
**Wikilinks:** [[claim_registry_current#CLAIM 045]]

---
## PAPER 157
**Short title:** Abudiab 2025 bioRxiv — WWOX e riparazione della mielina (**PREPRINT**)
**Full title:** WWOX deficiency uncovers a cell-autonomous mechanism impairing myelin repair
**Year:** 2025
**Source type:** 🔴 **preprint bioRxiv, NON sottoposto a peer review** — v1 del 2025-11-24, CC-BY-NC-ND. Layer di ricerca: non può alzare lo stato di alcuna claim.
**Journal/source:** bioRxiv
**Identifier:** DOI 10.1101/2025.11.22.689900 / bioRxiv PPR1124524 — **nessun PMID**
**Status:** processed
**Registry role:** research layer — a preprint founds no claim (status vocabulary corrected by `BATCH_20261003_003` from «processed (research layer)», which LINT refuses as INVALID_STATUS; nothing else in the record changed)
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — ricevuta `FTR-20261003-PPR1124524-01`, PDF bioRxiv `files/fulltext/PPR1124524_Abudiab2025_bioRxiv.pdf` con layer di testo derivato, dossier `fulltext_dossiers/PPR1124524.md`. **Nessun deep-dive manifest**: i manifest sono indicizzati per PMID e un file con nome PPR non sarebbe risolvibile dal modulo di provenance; i locator stanno nel dossier e in `CC-20261003W4-B-MYELIN-CELLAUT-01`.
**Integrity status:** clean
**Primary pathway:** P4 — mielinizzazione / sostanza bianca
**Model/species:** topo (condizionale Olig2-Cre; colture OPC dal null costitutivo), linea Oli-neu, HEK293T, dati umani snRNA-seq di lesioni di sclerosi multipla
**Genotype/model:** delezione di lignaggio oligodendrogliale (**non** inducibile, **non** temporizzata sull'OPC adulto)
**Transferability:** T2 per il meccanismo, T3 per la sclerosi multipla
**clinical relevance:** MODERATE
**Claim links:** none — un preprint non fonda una claim
**Role:** l'esperimento che `CLAIM 003` nomina come condizione, in una fonte che non può discharge quella condizione
**Note:** al basale **nessuna ipomielinizzazione** (assoni mielinizzati per campo 117.6 ± 12.5 vs 125.1 ± 9, P = 0.22); il fenotipo emerge solo sotto sfida (18 mesi; rimielinizzazione dopo cuprizone, con demielinizzazione uguale fra i genotipi). Meccanismo proposto: WWOX lega e stabilizza SOX10 via dominio WW1. **Stesso laboratorio senior di `PAPER 004`** — non è un osservatore indipendente. Nessun braccio eterozigote: i topi `Wwox +/−` sono nominati nei Metodi e non usati. Disponibilità dei dati «upon publication», nessun accession.
**Wikilinks:** [[paper_registry_current#PAPER 004]] · [[claim_registry_current#CLAIM 003]]

---
## PAPER 158
**Short title:** Lucas-Clarke 2025 bioRxiv — dose di *Wwox* in un modello amiloide di *Drosophila* (**PREPRINT**)
**Full title:** Alzheimer's disease risk gene Wwox protects against amyloid pathology through metabolic reprogramming
**Year:** 2025
**Source type:** 🔴 **preprint bioRxiv, NON sottoposto a peer review** — v1 del 2025-05-07, CC-BY. Layer di ricerca.
**Journal/source:** bioRxiv
**Identifier:** DOI 10.1101/2025.05.01.651195 / bioRxiv PPR1015434 — **nessun PMID**
**Status:** processed
**Registry role:** research layer — a preprint founds no claim (status vocabulary corrected by `BATCH_20261003_003` from «processed (research layer)», which LINT refuses as INVALID_STATUS; nothing else in the record changed)
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — ricevuta `FTR-20261003-PPR1015434-01`, JATS Europe PMC `files/fulltext/PPR1015434_LucasClarke2025_EPMC.xml` più supplemento, dossier `fulltext_dossiers/PPR1015434.md`. Nessun manifest, per la stessa ragione di `PAPER 157`.
**Integrity status:** clean
**Primary pathway:** P5 — metabolismo (piruvato / UPR)
**Model/species:** *Drosophila melanogaster*
**Genotype/model:** RNAi pan-neuronale, pan-gliale e sul clock; **CRISPRa** al sito di inizio della trascrizione di *Wwox* (circa 2× mRNA); cDNA di *Wwox* di mosca e di *WWOX* umano
**Transferability:** T3
**clinical relevance:** LOW-MODERATE (classe di leva, non evidenza clinica)
**Claim links:** none
**Role:** l'unica fonte del corpus che muove WWOX in **entrambe le direzioni nello stesso modello**, e che misura la ri-fornitura come **up-regolazione endogena a dose modesta**
**Note:** il knockdown accorcia la vita e, con Aβ42, è sinergico (interazione p < 0.0001) e alza l'Aβ42 **solubile**; la via è PERK–Atf4 → Ldh → lattato, e il knockdown di *Ldh* **recupera** il deficit locomotorio. Il reporter di HIF1α (*sima*) **non** si muove: un negativo diretto sull'asse WWOX/HIF1A in questo sistema. L'up-regolazione riduce il carico amiloide e recupera vita e locomozione **senza riportare giù il lattato**, abbassando invece la L-metionina — la risposta non percorre a ritroso lo stesso meccanismo. Nessun endpoint di mielina (la mosca non ha mielina nel CNS); nessun livello proteico di WWOX misurato; «AD risk gene» è un'attribuzione GWAS/eQTL su una variante intergenica fra *WWOX* e *MAF*. Dati depositati (ArrayExpress E-MTAB-14948, E-MTAB-14949; MetaboLights MTBLS12344).

---

## PAPER 159
**Short title:** Fukai 2026 Mol Ther — a compact 410-bp mouse Gad1 promoter (cmGAD67) driving selective AAV expression in inhibitory neurons
**Full title:** A compact GAD67 promoter enables inhibitory neuron-targeted AAV gene therapy for seizure suppression
**Authors:** Fukai Y, Konno A, Hosoi N, Miyakawa K, Kaneko R, Hirai H
**Year:** 2026
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther* 2026;34(9):5510-5526
**Identifier:** PMID 42349402 / PMCID PMC13555566 / DOI 10.1016/j.ymthe.2026.06.007
**Status:** processed
**Record provenance:** created by `CC-20261003w4-C-REGISTRY-01` (intake wave 4 2026-10-03, Scientist C, group C); numbers measured and assigned by `BATCH_20261003_003`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-42349402-01`; manifest `deepdive_manifests/PMID42349402.json`; dossier `research/fulltext_dossiers/PMID42349402.md`. Partial: figure panels not inspected as images and no supplementary file fetched — owed.
**Primary pathway:** P7 gene-therapy design
**Model/species:** mouse (C57BL/6J, VGAT-tdTomato), AAV-PHP.eB intravenous and intraparenchymal
**Genotype/model:** no WWOX allele; this source does not mention WWOX
**Transferability:** T3
**clinical relevance:** BACKGROUND — transferable method only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** The group's only quantified promoter-specificity measurement: 92.2 % ± 1.3 % inhibitory-neuron specificity systemically, about 85 % of PV⁺ neurons transduced and over 60 % of transduced cells PV⁺. 🔴 **Specificity is route-contingent**: the same cassette falls to 63.9 % ± 4.1 % after direct hippocampal injection, which the authors attribute to local vector concentration. **Transfer limit:** mouse promoter, no human orthologue tested; one dose throughout, so no dose-response; **no toxicology of any kind**; and this is circuit modulation by adding GAD65, not restoration of a deficient protein.
**LIT link:** [[literature_tracking_log_current#LIT-0448]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 160
**Short title:** Song 2026 Mol Ther — EXG001-307, a dose-optimised intra-CSF AAV9 for SMA; the two-sided dose claim, with its upper limb unmeasured
**Full title:** Challenging the more-is-better dogma: A precision-optimized AAV gene therapy for SMA
**Authors:** Song C, Liu J, Wang Q, Zhu P, Xu J, Zhou Y, et al. (Exegenesis Bio)
**Year:** 2026
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther* 2026;34(7):3783-3804
**Identifier:** PMID 41992613 / PMCID PMC13330066 / DOI 10.1016/j.ymthe.2026.04.027
**Status:** processed
**Record provenance:** created by `CC-20261003w4-C-REGISTRY-01` (intake wave 4 2026-10-03, Scientist C, group C); numbers measured and assigned by `BATCH_20261003_003`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-41992613-01`; manifest `deepdive_manifests/PMID41992613.json`; dossier `research/fulltext_dossiers/PMID41992613.md`. Partial: figure panels not inspected as images and no supplementary file fetched — owed.
**Primary pathway:** P7 gene-therapy design
**Model/species:** SMNΔ7 mouse, Wistar Han rat (male only), juvenile cynomolgus macaque
**Genotype/model:** no WWOX allele; this source does not mention WWOX
**Transferability:** T3
**clinical relevance:** BACKGROUND — transferable method only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** The only two-sided dose claim in the corpus. Lower limb **measured** (i.c.v. median survival 23 d at 2 × 10¹⁰ vg/animal to 373 d at 2 × 10¹¹; MED 2 × 10¹⁰). Upper limb **inferred**: it comes from a different construct at a higher dose, that cohort received no necropsy or histopathology, and the authors write that the measurement *«would be valuable to define this therapeutic window»*. In primates the highest dose tested became the NOAEL, so no toxic dose was reached. **Transfer limit:** sponsor study on its own candidate; *SMN* dose sensitivity does not transfer to WWOX; mouse DRG never harvested; three mutually incompatible vg/kg normalisations of the same rat doses (see `DIS-032`).
**LIT link:** [[literature_tracking_log_current#LIT-0449]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 161
**Short title:** Boitnott 2026 Mol Ther — unregulated DDX3X overexpression after an intra-CSF injection kills newborn mice from the heart
**Full title:** DDX3X overexpression in mice can cause rapid tissue-specific toxicity and mortality
**Authors:** Boitnott A, Hu Y, Wight-Carter M, Lopez Escobar C, Chen X, Gray SJ
**Year:** 2026
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther* 2026;34(9):5135-5144
**Identifier:** PMID 42458834 / PMCID PMC13555558 / DOI 10.1016/j.ymthe.2026.07.032
**Status:** processed
**Record provenance:** created by `CC-20261003w4-C-REGISTRY-01` (intake wave 4 2026-10-03, Scientist C, group C); numbers measured and assigned by `BATCH_20261003_003`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-42458834-01`; manifest `deepdive_manifests/PMID42458834.json`; dossier `research/fulltext_dossiers/PMID42458834.md`. Partial: figure panels not inspected as images and no supplementary file fetched — owed.
**Primary pathway:** P7 gene-therapy design
**Model/species:** wild-type C57BL/6J mouse, bilateral i.c.v. at P1 and intrathecal at P21
**Genotype/model:** no WWOX allele; this source does not mention WWOX
**Transferability:** T3
**clinical relevance:** BACKGROUND — transferable method only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** The group's hardest negative, and sponsor-adverse: all high-dose animals dead by P8 from myocardial degeneration, with hepatic steatosis and a more than 1000-fold cardiac *Ifnb1* rise, while a promoter-matched control vector carrying a different transgene elicited none of it. The lethal dose, scaled by neonatal brain mass, equals a dose the paper says is in clinical use. 🔴 *«The brain was overall unaffected»* is a **morphology** statement: brain *Cxcl10* rose about 23-fold in the same animals. **Transfer limit:** DDX3X's own roles in RIG-I/MAVS signalling and *Ddit3* transcription are plausibly the mechanism, so the magnitude does not transfer; WWOX dose sensitivity is neither shown nor excluded. n per group is reported nowhere in the main text.
**LIT link:** [[literature_tracking_log_current#LIT-0450]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 162
**Short title:** Grubor 2025 Mol Ther Methods Clin Dev — immune events precede AAV DRG pathology in macaques, and dexamethasone plus tacrolimus reduce it across three cargos
**Full title:** Inhibition of immune response reduces pathology in dorsal root ganglia and peripheral nerves in cynomolgus macaques following AAV gene therapy
**Authors:** Grubor B, Henry KL, Chan SJ, Sheehan M, Shah A, Pellerin A, et al. (Biogen)
**Year:** 2025
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101643
**Identifier:** PMID 41404412 / PMCID PMC12704302 / DOI 10.1016/j.omtm.2025.101643
**Status:** processed
**Record provenance:** created by `CC-20261003w4-C-REGISTRY-01` (intake wave 4 2026-10-03, Scientist C, group C); numbers measured and assigned by `BATCH_20261003_003`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-41404412-01`; manifest `deepdive_manifests/PMID41404412.json`; dossier `research/fulltext_dossiers/PMID41404412.md`. Partial: main figure panels read as images (wave-9 re-read, receipt `FTR-20261004-41404412-02`) and Document S1 fetched; supplementary Figures S1-S12, S14 and S15 read by caption only, references unread.
**Primary pathway:** P7 gene-therapy design / BLOCK-1 safety
**Model/species:** cynomolgus macaque, intra-cisterna magna and intrathecal lumbar
**Genotype/model:** no WWOX allele; this source does not mention WWOX
**Transferability:** T3
**clinical relevance:** BACKGROUND — transferable method only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** One pole of an **unresolved contradiction** (`RL-C-20261003w4a`, `DIS-031`). Measures what no other source in the group measures: ultrastructural change and immune infiltrates from day 5, before the first lesion at day 15. Mitigation across three cargos including one expressing no protein, with transgene expression unchanged. **Transfer limit:** sponsor study; the causal claim rests on a multi-target pharmacological block with n = 3 per group; no antigen-specific T cells were detected and the effector mechanism is the authors' postulate; healthy animals, no efficacy endpoint; longest arm 43 days against the authors' own predicted six-month requirement; and the authors state the immune mechanism **does not hold in mouse**.
**LIT link:** [[literature_tracking_log_current#LIT-0451]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 163
**Short title:** Tukov 2022 Hum Gene Ther — intrathecal onasemnogene DRG and trigeminal findings, not mitigated by prednisolone or by rituximab plus everolimus
**Full title:** Single-Dose Intrathecal Dorsal Root Ganglia Toxicity of Onasemnogene Abeparvovec in Cynomolgus Monkeys
**Authors:** Tukov FF, Mansfield K, Milton M, Meseck E, Penraat K, Chand D, Hartmann A
**Year:** 2022
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Hum Gene Ther* 2022;33(13-14):740-756
**Identifier:** PMID 35331006 / PMCID PMC9347375 / DOI 10.1089/hum.2021.255
**Status:** processed
**Record provenance:** created by `CC-20261003w4-C-REGISTRY-01` (intake wave 4 2026-10-03, Scientist C, group C); numbers measured and assigned by `BATCH_20261003_003`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-35331006-01`; manifest `deepdive_manifests/PMID35331006.json`; dossier `research/fulltext_dossiers/PMID35331006.md`. Partial: figure panels not inspected as images and no supplementary file fetched — owed.
**Primary pathway:** P7 gene-therapy design / BLOCK-1 safety
**Model/species:** cynomolgus macaque, intrathecal lumbar with iohexol contrast, plus an intravenous arm
**Genotype/model:** no WWOX allele; this source does not mention WWOX
**Transferability:** T3
**clinical relevance:** BACKGROUND — transferable method only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** The other pole of the same contradiction. Findings from the anticipated clinical dose upward and **with no dose response**; nerve conduction normal in every arm; high vector transcript colocalised with the degenerating neurons. 🔴 The negative is scoped by the authors to **adaptive** immunity, and they state that innate activation *«was not excluded»*; no calcineurin inhibitor was tested. *«Resolution»* is explicitly redefined as lower incidence and severity, because neuronal loss is not reversible. **Transfer limit:** sponsor study run to answer a regulatory partial clinical hold; the negative rests on n = 3 per sex interim and **n = 2 per sex terminal** with no power statement; human relevance declared unknown.
**LIT link:** [[literature_tracking_log_current#LIT-0452]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 164
**Short title:** Johnson 2022 Mol Ther Methods Clin Dev — blood and CSF NfL against AAV9 DRG injury in 260 macaques, with per-animal operating characteristics
**Full title:** Neurofilament light chain and dorsal root ganglia injury after adeno-associated virus 9 gene therapy in nonhuman primates
**Authors:** Johnson EW, Sutherland JJ, Meseck E, McElroy C, Chand DH, Tukov FF, Hudry E, Penraat K
**Year:** 2022
**Source type:** primary research — nonclinical gene-therapy / safety study
**Journal/source:** *Mol Ther Methods Clin Dev* 2022;28:208-219
**Identifier:** PMID 36700120 / PMCID PMC9852542 / DOI 10.1016/j.omtm.2022.12.012
**Status:** processed
**Record provenance:** created by `CC-20261003w4-C-REGISTRY-01` (intake wave 4 2026-10-03, Scientist C, group C); numbers measured and assigned by `BATCH_20261003_003`
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-36700120-01`; manifest `deepdive_manifests/PMID36700120.json`; dossier `research/fulltext_dossiers/PMID36700120.md`. Partial: figure panels not inspected as images and no supplementary file fetched — owed.
**Primary pathway:** P7 gene-therapy design / toxicity surveillance
**Model/species:** cynomolgus macaque, nine pooled studies, intrathecal and intravenous
**Genotype/model:** no WWOX allele; this source does not mention WWOX
**Transferability:** T3
**clinical relevance:** BACKGROUND — transferable method only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** The assay source, over the group's largest denominator: 78 % incidence at 2–12 weeks falling to 42 % by 52 weeks; 18–21 DRG per animal on a five-point scale under pathologist peer review; ROC AUC 0.85 (blood) and 0.95 excluding minimal grade, with sensitivity and specificity at five fold-change cut-offs. Empty capsid and promoter-less vectors caused neither lesion nor NfL rise. **Transfer limits, three:** (1) under `LEGEND_CORE` §13 NfL is **Tier 3** for WWOX — a biomarker of vector toxicity, never a WWOX disease biomarker; (2) not clinically validated, by the authors' own statement, and a raised NfL *«is not disease specific»*; (3) 🔴 **not independent of [[paper_registry_current#PAPER 163]]** — same sponsor, four shared authors, data drawn from the sponsor's own study warehouse. See `RL-C-20261003w4c`, `RC-C-20261003w4`.
**LIT link:** [[literature_tracking_log_current#LIT-0453]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.
## PAPER 165
**Short title:** Greenberg 2026 EBioMedicine - the first-in-human high-dose intrathecal AAV9 trial, and the CRIM rule that makes transgene immunity a recessive-null problem
**Full title:** First-in-human high dose AAV9 intrathecal gene therapy for paediatric CLN7 disease: a phase 1, open-label, single ascending dose, non-randomised clinical trial
**Authors:** Greenberg BM, Minassian B, Messahel S, et al.; Gray SJ, Kayani SN
**Year:** 2026
**Source type:** primary clinical study - phase 1, open label, non-randomised, single ascending intrathecal dose, n = 4
**Journal/source:** *EBioMedicine* 2026;123:106044
**Identifier:** PMID 41314141 / PMCID PMC12703863 / DOI 10.1016/j.ebiom.2025.106044
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number; highest `PAPER` measured 150 on `main` 663970a. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-41314141-01`; manifest `deepdive_manifests/PMID41314141.json`; dossier `research/fulltext_dossiers/PMID41314141.md`
**Primary pathway:** none for WWOX - AAV9 CNS gene replacement, dose and immunosuppression
**Model/species:** human, four children aged 4-5 years at dosing
**Genotype/model:** biallelic *MFSD8* (CLN7); NOT a WWOX genotype
**Transferability:** T2 for the immunosuppression protocol and the empty-capsid arithmetic; T4 for efficacy
**clinical relevance:** HIGH strategic - the only human high-dose intrathecal AAV9 source in this repository
**Claim links:** none
**Role:** 🔵 **Transferable protocol, not WWOX evidence. The paper does not mention WWOX.** It is the repository's source for the cross-reactive-immunological-material (CRIM) rule: patients predicted to make no protein were classified CRIM-negative and given a THIRD immunosuppressant against a response to the gene product, which makes transgene immunity a problem for a biallelic null rather than a non-problem for a "self" protein. Also the source for a clinical lot at 42% genome-containing particles (so a 1 x 10^15 vg dose carried 2.38 x 10^15 capsids) and for attributing dorsal-root-ganglion toxicity to transgene overexpression. ⚠️ Efficacy is not established: declines on every instrument, no matched natural-history comparator, no dose-response, no transgene-expression measurement in any patient, and no formal statistics. ⚠️ Table 2 does not reconcile with itself: counts sum to 58 against a stated 57, and two rows disagree with their own percentages.
**LIT link:** [[literature_tracking_log_current#LIT-0454]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.
## PAPER 166
**Short title:** Quinlan 2025 Mol Ther - an oversized full-length cassette packages, with a measured yield and heterogeneity penalty, in a heterozygous model
**Full title:** AAV delivery of full-length SYNGAP1 rescues epileptic and behavioral phenotypes in a mouse model of SYNGAP1-related disorders
**Authors:** Quinlan MA, Guo R, Clark AG, et al.; Levi BP
**Year:** 2025
**Source type:** primary preclinical study - vector engineering, AAV-PHP.eB delivery, EEG/EMG, two behavioural assays
**Journal/source:** *Mol Ther* 2025
**Identifier:** PMID 40988338 / PMCID PMC12703155 / DOI 10.1016/j.ymthe.2025.09.040
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-40988338-01`; manifest `deepdive_manifests/PMID40988338.json`; dossier `research/fulltext_dossiers/PMID40988338.md`; supplementary document S1 persisted and read (PDF plus derived text layer)
**Primary pathway:** none for WWOX - AAV cargo size, dose-response, expression ceiling
**Model/species:** mouse, conditional *Syngap1* heterozygote (~55% of wild-type protein)
**Genotype/model:** dominant haploinsufficiency; NOT a null and NOT a WWOX genotype
**Transferability:** T2 for the packaging arithmetic; T4 for rescue, which is measured against a 55%-of-wild-type baseline
**clinical relevance:** MODERATE strategic
**Claim links:** none
**Role:** 🔵 **Transferable cargo lesson, not WWOX evidence. The paper does not mention WWOX.** A 5.136 kb ITR-to-ITR cassette above the ~4.7 kb limit packages with a measured two-fold yield loss against a 4.617 kb same-day control and a 94.60:5.40 full-to-empty ratio. ⚠️ Read in the supplement rather than the body, the headline "75.81% full-length" is a 4-6 kb SIZE BIN with a further 15.22% above 6 kb. ⚠️ Table S3 shows 5 of 10 high-dose mice had poor surgical outcomes and only 5 were recorded, against 0 of 8 and 0 of 4 in the lower-dose arms - a dose-confined attrition the Discussion never mentions, which means the high-dose electrophysiology is the surviving half of that group. The authors report a protein ceiling: a 2.5-fold rise in transgene signal produced no further total protein.
**LIT link:** [[literature_tracking_log_current#LIT-0455]]
**Note:** class-level record; no individual-level detail. Not medical advice.
## PAPER 167
**Short title:** Wiseman 2024 EMBO Mol Med - the closest architectural analogue: a complete IND package for a recessive loss-of-function CNS disease, whose immunogenicity arm used wild-type animals
**Full title:** Pre-clinical development of AP4B1 gene replacement therapy for hereditary spastic paraplegia type 47
**Authors:** Wiseman JP, Scarrott JM, Alves-Cruzeiro J, et al.; Ebrahimi-Fakhari D, Azzouz M
**Year:** 2024
**Source type:** primary preclinical study - four cell models, neonatal and adult mouse efficacy, potency assay, two mouse safety studies, GLP non-human-primate toxicology
**Journal/source:** *EMBO Mol Med* 2024;16(11)
**Identifier:** PMID 39358605 / PMCID PMC11554807 / DOI 10.1038/s44321-024-00148-5
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-39358605-01`; manifest `deepdive_manifests/PMID39358605.json`; dossier `research/fulltext_dossiers/PMID39358605.md`
**Primary pathway:** none for WWOX - recessive loss-of-function gene replacement, route, dose translation, window
**Model/species:** *Ap4b1* knockout mouse; wild-type mouse safety studies; wild-type cynomolgus macaque GLP toxicology
**Genotype/model:** biallelic loss of function (AP-4 deficiency); NOT a WWOX genotype
**Transferability:** T2 as a programme template - it is the nearest architectural analogue in the corpus for a recessive null CNS disease
**clinical relevance:** HIGH strategic
**Claim links:** none
**Role:** 🔵 **Transferable programme template, not WWOX evidence. The paper does not mention WWOX.** Intracisterna magna beat intravenous; partial restoration of the complex sufficed; the human dose was derived by scaling to CSF volume on FDA advice (primate high dose equating to 4 x 10^14 genome copies in a four-year-old). 🔴 **The named gap:** transgene immunogenicity was tested only in WILD-TYPE mice dosed at P1-3, with an interferon-gamma ELISpot and no antibody assay anywhere - so the protein-naive host a recessive-null patient models was never tested; the primates were wild type too. ⚠️ The window is endpoint-specific: adult treatment left brain structure unrescued while still rescuing motor function. ⚠️ The abstract's "no significant adverse events" covers dose- and time-dependent nerve and spinal-cord degeneration, a treatment-associated leucocytosis at 28 days and one unexplained death at 80 days in a treated animal. ⚠️ The adult mid dose is stated as 3 x 10^12 vg/kg in Results and 4 x 10^12 vg/kg in the Discussion, and the declared n = 12 per dose is not the analysed n for any endpoint.
**LIT link:** [[literature_tracking_log_current#LIT-0456]]
**Note:** class-level record; no individual-level detail. Not medical advice.
## PAPER 168
**Short title:** Bailey 2026 J Clin Invest - the metabolic and the seizure endpoint do not share a dose, and age costs an order of magnitude of delivery at matched dose and route
**Full title:** AAV-mediated gene therapy in a model of SLC13A5 citrate transporter disorder rescues epileptic and metabolic phenotypes
**Authors:** Bailey LE, Adams RM, Schackmuth MK, et al.; Bailey RM
**Year:** 2026
**Source type:** primary preclinical study - vector design, neonatal dose comparison, adult route comparison, electrophysiology, sleep staging, chemoconvulsant challenge, biodistribution
**Journal/source:** *J Clin Invest* 2026;136(8)
**Identifier:** PMID 41712282 / PMCID PMC13078891 / DOI 10.1172/JCI197503
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-41712282-01`; manifest `deepdive_manifests/PMID41712282.json`; dossier `research/fulltext_dossiers/PMID41712282.md`
**Primary pathway:** none for WWOX - two-sided dose, self-complementary cargo, route versus age
**Model/species:** *Slc13a5* knockout mouse
**Genotype/model:** biallelic loss of function (DEE25); NOT a WWOX genotype
**Transferability:** T2 for the two-axis dose design and the age-versus-route arithmetic; T4 for any dose
**clinical relevance:** HIGH strategic
**Claim links:** none
**Role:** 🔵 **Transferable dosing lesson, not WWOX evidence. The paper does not mention WWOX.** 🔴 **The two endpoints have different dose-response curves:** plasma citrate fell dose-dependently to 65 +/- 8.0% of wild type at the high dose - an overshoot past normal from a baseline about 20% above wild type - while the chemoconvulsant endpoint saturated, the low dose matching the high. The authors themselves name a published developmental harm from overexpressing the same gene. ⚠️ Age cost an order of magnitude of delivery at matched dose and route (cerebellar vector 15.7 x 10^3 at P10 against 1.2 x 10^3 at 3 months, vg per genome), partly recovered by switching the adult route - which is why its apparent window result resolves to delivery. ⚠️ A short synthetic promoter is what permits self-complementary packaging of a 1.7 kb coding sequence. ⚠️ No immune endpoint of any kind is reported, although a human transgene in a knockout host is the closest thing here to a protein-naive recipient. ⚠️ The antibody does not recognise the endogenous mouse protein, so expression has no wild-type reference. ⚠️ The vehicle control arms of the P10 sleep and power-spectrum analysis were already published by the same group.
**LIT link:** [[literature_tracking_log_current#LIT-0457]]
**Note:** class-level record; no individual-level detail. Not medical advice.
## PAPER 169
**Short title:** Duba-Kiss 2025 Mol Ther Methods Clin Dev - early expression buys cellular but not humoral tolerance, does not transfer to a redose, and is antigen-specific
**Full title:** Early postnatal expression mitigates immune responses to Cas9 in the murine central nervous system
**Authors:** Duba-Kiss R, Hampson DR
**Year:** 2025
**Source type:** primary preclinical immunology study - neonatal versus adult CNS delivery, glial and adaptive-immune readouts, EGFP comparator, prime-and-redose arm
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(3):101536
**Identifier:** PMID 40809677 / PMCID PMC12347139 / DOI 10.1016/j.omtm.2025.101536
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-40809677-01`; manifest `deepdive_manifests/PMID40809677.json`; dossier `research/fulltext_dossiers/PMID40809677.md`
**Primary pathway:** none for WWOX - window x immunity interaction, promoter choice and tolerance
**Model/species:** wild-type C57BL/6J mouse
**Genotype/model:** none - the antigen is a bacterial nuclease; NOT a WWOX genotype
**Transferability:** T3 - mechanism transfers, magnitude does not
**clinical relevance:** MODERATE strategic
**Claim links:** none
**Role:** 🔵 **Transferable mechanism, not WWOX evidence. The paper does not mention WWOX.** Early postnatal expression preserved the transgene and raised no MHC II or T-cell response, while adult delivery destroyed the transgene and cost about a third of cortical neurons. 🔴 **Three limits that bound the "early delivery buys tolerance" idea:** antibodies were raised at BOTH ages, so the tolerance is cellular and not humoral; a neonatal prime did not abolish the harm of an adult redose (still -25.3% neuronal density); and the effect is antigen-specific - EGFP in the same compartment at the same age was inert, so "foreign protein" is not one category. ⚠️ A neuron-restricted promoter may itself impede MHC II-dependent regulatory T-cell tolerance, which sets promoter choice against the overexpression-safety argument. ⚠️ The adult arm received four times the vector of the neonatal arm, so age and antigen load are not separated, and the adult quantification used a parenchymal route where the neonatal used intraventricular.
**LIT link:** [[literature_tracking_log_current#LIT-0458]]
**Note:** class-level record; no individual-level detail. Not medical advice.
## PAPER 170
**Short title:** Balestrini 2026 CNS Drugs - landscape review; half its most advanced modalities are structurally unavailable to a biallelic null
**Full title:** Ameliorating Seizures in Dravet Syndrome: A Review of Newly Approved and Investigational Drugs, RNA and Gene-Based Therapies
**Authors:** Balestrini S, Scheffer IE
**Year:** 2026
**Source type:** narrative review - NOT a systematic review and NOT a primary study
**Journal/source:** *CNS Drugs* 2026;40(4):535-548
**Identifier:** PMID 41712149 / PMCID PMC12989007 / DOI 10.1007/s40263-026-01276-x
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-41712149-01`; manifest `deepdive_manifests/PMID41712149.json`; dossier `research/fulltext_dossiers/PMID41712149.md`. The gene- and RNA-based sections were read in full; the small-molecule sections in outline only, as stated in the dossier.
**Primary pathway:** none for WWOX - modality landscape, cargo limit, window counter-datum
**Model/species:** not applicable - review
**Genotype/model:** *SCN1A* haploinsufficiency (dominant, de novo in over 95%); NOT a WWOX genotype
**Transferability:** T4 as evidence - every datum must be traced to a primary before it counts; T2 as a map of which modalities reached patients
**clinical relevance:** MODERATE strategic
**Claim links:** none
**Role:** 🔵 **Positioning map, not evidence. The review does not mention WWOX.** 🔴 **The sharpest transfer limit in the wave:** because this disease leaves one intact allele, almost every modality the review treats as most advanced - antisense upregulation, dCas9 transcriptional activation, an engineered transcription factor, conditional reactivation, paralogue rebalancing - requires an endogenous locus to act on and is therefore STRUCTURALLY UNAVAILABLE to a biallelic null. The one route that does transfer, split-intein dual-vector replacement for an over-6 kb open reading frame, is the one with no human data. ⚠️ It carries the corpus's only expression-matched age comparison - conditional reactivation at P90 in adulthood still rescued seizures after months of seizures - which points the window later rather than earlier, but is review-level and its primary was not retrieved. ⚠️ It quantifies the paediatric CSF cost of repeated intrathecal dosing: transient protein elevations above 50 mg/dL in about three-quarters of children in the extension studies. ⚠️ Its stated search window closes 31 March 2025, before the clinical results it reports; both flagship programmes are sponsored by companies with which the authors declare relationships.
**LIT link:** [[literature_tracking_log_current#LIT-0459]]
**Note:** class-level record; no individual-level detail. Not medical advice.

## PAPER 171
**Short title:** Al Baradie 2022 Epileptic Disord — nine homozygous WWOX patients in six families (P47T, R54*, c.606-1G>A, Q230P) plus a 61-patient literature table
**Full title:** Epilepsy in patients with WWOX-related epileptic encephalopathy (WOREE) syndrome
**Authors:** Al Baradie R, Mir A, Alsaif A, Ali M, Al Ghamdi F, Bashir S, Howsawi Y
**Year:** 2022
**Source type:** primary research — retrospective single-centre case series with a literature aggregation
**Journal/source:** *Epileptic Disord* 2022;24(4):697-712
**Identifier:** PMID 35792847 / DOI 10.1684/epd.2022.1444
**Status:** processed
**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`. Promotes [[paper_registry_current#CORPUS-STUB-060]] (kept as history).
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35792847-01`; manifest `deepdive_manifests/PMID35792847.json`; dossier `research/fulltext_dossiers/PMID35792847.md`
**Primary pathway:** clinical spectrum / WOREE epileptology
**Model/species:** human
**Genotype/model:** all homozygous: P47T (two families, three patients), R54* (two families, three patients), canonical splice acceptor `c.606-1G>A` (one non-consanguineous family, two brothers), Q230P (one patient); an affected sib of the Q230P homozygote carries Q230P heterozygous only, second allele not found at publication
**Transferability:** T1 for the clinical course of each homozygous class; the Q230P homozygote is not the reference genotype (compound heterozygous)
**clinical relevance:** MODERATE — first Q230P-homozygous course with neonatal onset and suppression-burst in LEGEND; P47T homozygotes intermediate between SCAR12 and WOREE
**Claim links:** none (proposed bearing on 032 through `CC-20261003W5-B-CNV-CARRIER-01`; on DL-MECH-022 through `CC-20261003W5-B-ALBARADIE-01`)
**Role:** 🔴 Counting: family 2 (homozygous R54* sibship) is probably the R54* sibship of [[paper_registry_current#PAPER 119]] re-described without cross-citation (`CC-20261003W5-B-PATIENT-OVERLAP-01`); net new patients 7, possibly 6 (one family-3 patient may be in Tabarki 2015, unread). The abstract's 'correlations between genotype and phenotype' are not supported by any analysis in the body (Table 3 has no genotype column). The 70-patient literature denominator double-counts Tarta-Arsene 2017 / Piard 2019 patient 8 and the Ehaideb sibship, and includes the SCAR12-linkage family's patients among its literature cohort, although this article never labels them SCAR12 and lists spinocerebellar ataxia as a separate WWOX phenotype (blind-audit narrowing, `BATCH_20261003_004`): **do not use its percentages as a WOREE denominator.** 🔴 **Family 3 / Tabarki 2015, one more candidate (`CC-20261004W7-B-PATIENT-OVERLAP-01`, intake wave 7):** [[paper_registry_current#PAPER 206]] (PMID 36937954) reports one more homozygous `c.606-1G>A` from a single Saudi centre, in patients diagnosed with neurodevelopmental disorders between 2015 and 2018 (the source dates the **diagnosis**, not the testing — integrator amendment, blind audit), with no sex, onset, course or outcome printed — it can be neither matched to nor excluded from family 3, Tabarki 2015 or the five patients of PMID 26345274. Count it once as unlinked; the four held reports of this allele are not independent families until a primary settles it. PMID 42807679 (a Tunisian heterozygous 16q deletion) cannot bear on the Tabarki overlap at all. `PREMISE: INFERENZA`.
**LIT link:** [[literature_tracking_log_current#LIT-0084]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 172
**Short title:** Burgess 2019 Ann Neurol — EIMFS genetic landscape, 135 patients; one WWOX patient (E17K + two intronic deletions, both VUS here) = patient 6 of the 2023 WWOX-DEE cohort
**Full title:** The Genetic Landscape of Epilepsy of Infancy with Migrating Focal Seizures
**Authors:** Burgess R, Wang S, McTague A, et al.; Scheffer IE
**Year:** 2019
**Source type:** primary research — international consortium cohort
**Journal/source:** *Ann Neurol* 2019;86(6):821-831 (erratum PMID 32176372, content not retrieved)
**Identifier:** PMID 31618474 / PMCID PMC7423163 / DOI 10.1002/ana.25619
**Status:** processed
**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-31618474-01` (earlier `FTR-20260921-31618474-01`, a verification of an artefact without gene symbols, tables or supplement); manifest `deepdive_manifests/PMID31618474.json`; dossier `research/fulltext_dossiers/PMID31618474.md`
**Primary pathway:** clinical spectrum / EIMFS
**Model/species:** human
**Genotype/model:** one compound heterozygote: missense `c.49G>A p.(Glu17Lys)` + two intronic deletions on the other allele (introns 3 and 4, microarray); both alleles VUS in the paper's Table 2; splicing effect predicted only
**Transferability:** T1 for the EIMFS presentation of one missense/null-class genotype
**clinical relevance:** LOW — one patient, counted in [[paper_registry_current#PAPER 018]]
**Claim links:** none
**Role:** 🔴 **Not an independent patient:** [[paper_registry_current#PAPER 018]] states that its patient 6 was briefly reported here and supplies the RNA result this paper lacks (intron-4 deletion → exon 5 skipping; intron-3 deletion benign). Count once, under `PAPER 018`. Not Piard patient 12 (second allele S304F). The cohort's 6.8 Mb deletion includes SCN1A and SCN2A — the article never names a chromosome or coordinates, so the chromosome-2 assignment is an inference from gene identity (blind-audit narrowing, `BATCH_20261003_004`) — and is unrelated to the 16q case of [[paper_registry_current#PAPER 176]].
**LIT link:** [[literature_tracking_log_current#LIT-0460]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 173
**Short title:** Yang 2022 Sci Rep — 36 EIMFS children; the only WWOX carrier (p.M1? + p.H78Y) also carries a pathogenic ATP7A frameshift with Menkes features
**Full title:** Analysis of clinical phenotypic and genotypic spectra in 36 children patients with Epilepsy of Infancy with Migrating Focal Seizures
**Authors:** Yang H, Yang X, Cai F, Gan S, Yang S, Wu L
**Year:** 2022
**Source type:** primary research — retrospective two-centre cohort
**Journal/source:** *Sci Rep* 2022;12:10187
**Identifier:** PMID 35715422 / PMCID PMC9205988 / DOI 10.1038/s41598-022-13974-9
**Status:** processed
**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-35715422-01`; manifest `deepdive_manifests/PMID35715422.json`; dossier `research/fulltext_dossiers/PMID35715422.md`
**Primary pathway:** clinical spectrum / EIMFS · attribution guardrail
**Model/species:** human
**Genotype/model:** WWOX initiator codon `p.M1?` (LP) + `p.H78Y` (VUS) with a hemizygous ATP7A frameshift (P) in one male
**Transferability:** none for WWOX-specific inference (dual diagnosis)
**clinical relevance:** LOW — a guardrail record
**Claim links:** none
**Role:** The abstract's 'WWOX may be associated with poor prognosis' is one patient who also has a Menkes-compatible ATP7A variant; Table 3 records seizure control 'ineffective' beside oxcarbazepine 'effective'. Not counted as a WWOX-DEE case. Supplies the receipted primary behind [[discovery_ledger_current#DL-MECH-059 — Una doppia diagnosi impedisce attribuzioni WWOX-specifiche|DL-MECH-059]], whose data this reading confirms.
**LIT link:** [[literature_tracking_log_current#LIT-0461]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 174
**Short title:** Spagnoli 2021 Int J Mol Sci — systematic review of neonatal-onset genetic epilepsy with movement disorder; all WWOX content re-describes Piard 2019
**Full title:** Genetic Neonatal-Onset Epilepsies and Developmental/Epileptic Encephalopathies with Movement Disorders: A Systematic Review
**Authors:** Spagnoli C, Fusco C, Percesepe A, Leuzzi V, Pisani F
**Year:** 2021
**Source type:** secondary — PRISMA systematic review (49 papers)
**Journal/source:** *Int J Mol Sci* 2021;22(8):4202
**Identifier:** PMID 33919646 / PMCID PMC8072943 / DOI 10.3390/ijms22084202
**Status:** processed
**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-33919646-01`; manifest `deepdive_manifests/PMID33919646.json`; dossier `research/fulltext_dossiers/PMID33919646.md`
**Primary pathway:** movement phenotype (secondary)
**Model/species:** human
**Genotype/model:** six WWOX genotypes, all patients of [[paper_registry_current#PAPER 117]] (Piard 1, 2, 3, 4, 9, 11)
**Transferability:** none beyond its source
**clinical relevance:** LOW — secondary
**Claim links:** none (see `CC-20261003W5-B-HYPOKINESIA-01`)
**Role:** 🔴 Its claim that a neonatal hypokinetic movement disorder occurs only with WWOX rests on five Piard patients whose primary row reads 'poor spontaneous movements', re-labelled 'hypokinesia'; the primary's own movement-disorder row for those patients lists dystonia, myoclonus, startle, pedalling/boxing or 'no'. Zero new patients; do not cite as an independent observation.
**LIT link:** [[literature_tracking_log_current#LIT-0462]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 175
**Short title:** Hengel 2020 Eur J Hum Genet — first-line exome in 83 consanguineous-population families; WWOX row is the published SCAR12 G372R family
**Full title:** First-line exome sequencing in Palestinian and Israeli Arabs with neurological disorders is efficient and facilitates disease gene discovery
**Authors:** Hengel H, Buchert R, Sturm M, et al.; Schöls L
**Year:** 2020
**Source type:** primary research — family exome cohort
**Journal/source:** *Eur J Hum Genet* 2020;28(8):1034-1043 (licence correction PMID 34050322)
**Identifier:** PMID 32214227 / PMCID PMC7382450 / DOI 10.1038/s41431-020-0609-9
**Status:** processed
**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-32214227-01` (earlier `FTR-20260921-32214227-01`, a verification of an artefact without tables); manifest `deepdive_manifests/PMID32214227.json`; dossier `research/fulltext_dossiers/PMID32214227.md`
**Primary pathway:** clinical spectrum / SCAR12 (pointer)
**Model/species:** human
**Genotype/model:** homozygous G372R, two affected sibs — the family of [[paper_registry_current#PAPER 042]] (Supplementary Table 1 names that publication)
**Transferability:** none beyond its source
**clinical relevance:** LOW — pointer
**Claim links:** none
**Role:** 🔴 The 2026-09-21 statement that this paper has 'zero WWOX variants' is wrong: Table 1 carries the WWOX row (the earlier artefact had lost the tables). The 'homozygous nonsense, intellectual disability, epilepsy, corpus callosum dysgenesis' row is TMCO1, not WWOX. Zero new patients.
**LIT link:** [[literature_tracking_log_current#LIT-0463]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 176
**Short title:** Mori 2019 Brain Dev — heterozygous 6.8 Mb 16q22.2-q23.1 deletion ending inside WWOX in an infant with West syndrome; second allele exon-clean; not attributed to WWOX
**Full title:** A 16q22.2-q23.1 deletion identified in a male infant with West syndrome
**Authors:** Mori T, Goji A, Toda Y, Ito H, Mori K, Kohmoto T, Imoto I, Kagami S
**Year:** 2019
**Source type:** primary research — single case report
**Journal/source:** *Brain Dev* 2019;41(10):888-892 (accepted manuscript read)
**Identifier:** PMID 31353122 / DOI 10.1016/j.braindev.2019.07.005
**Status:** processed
**Record provenance:** created by `CC-20261003W5-B-REGISTRY-01` (intake wave 5 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261003-31353122-01` (figures not inspected; Figure 1 is a patient photograph); manifest `deepdive_manifests/PMID31353122.json`; dossier `research/fulltext_dossiers/PMID31353122.md`
**Primary pathway:** copy-number carriers / negative control
**Model/species:** human
**Genotype/model:** heterozygous 57-gene deletion whose distal breakpoint lies inside WWOX (exons removed not stated); other allele clean on exon-targeted panel; no intronic, RNA or parental testing
**Transferability:** none for WWOX haploinsufficiency (56 other genes in the interval)
**clinical relevance:** LOW — a counting boundary
**Claim links:** none (proposed qualification of 032 through `CC-20261003W5-B-CNV-CARRIER-01`)
**Role:** Not a WWOX-DEE case and not a demonstrated haploinsufficiency case; the authors decline the attribution. The drug history (seizure freedom on valproate plus lamotrigine) is one patient with a contiguous deletion and is not a WWOX treatment datum.
**LIT link:** [[literature_tracking_log_current#LIT-0464]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.
## PAPER 177
**Short title:** Wang 2026 Mol Ther - first-in-human single-patient intra-cisterna magna AAV9 in severe MPS I, >5.5 years
**Full title:** First-in-human intracisternal dosing of RGX-111 in severe MPS I is well tolerated and generates sustained neurodevelopment without HSCT
**Authors:** Wang RY, et al.
**Year:** 2026
**Source type:** primary research - single-patient open-label clinical report
**Journal/source:** *Molecular Therapy* 2026
**Identifier:** PMID 41966056 / PMCID PMC13239742 / DOI 10.1016/j.ymthe.2026.04.016
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-41966056-01`; manifest `deepdive_manifests/PMID41966056.json`; dossier `research/fulltext_dossiers/PMID41966056.md` (figure panels not rendered; supplementary documents not fetched)
**Primary pathway:** CSF-route AAV9 delivery - human safety and tolerability
**Model/species:** human, single patient, dosed in the second year of life
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: route, immunosuppression and monitoring transfer; the cargo, the pharmacodynamic readout and the disease do not
**clinical relevance:** LOW for WWOX biology; MODERATE as the only human intracisternal AAV9 datum in the second year of life
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** Carried for four things only: (1) the intra-cisterna-magna route tolerated at ~20 months with next-day discharge; (2) 48 weeks of triple immunosuppression, with 16 of the 17 first-year adverse events attributed by the investigators to the immunosuppression rather than the vector; (3) ⚠️ **the dose literal is printed with an impossible negative exponent in BOTH the abstract and the body** and must never be carried as printed - see `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`; (4) ⚠️ **DRG toxicity was not measured** - the authors state no nerve conduction studies were performed and rest the inference on absence of reported paraesthesia in a toddler. The selection record called this "a first-in-human cohort"; it is n = 1. An intraventricular tumour with vector genome integration after the same route and vector in a different child is **cited** here, not measured, and is an open reading debt.
**LIT link:** [[literature_tracking_log_current#LIT-0465]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.
## PAPER 178
**Short title:** Vono 2025 Mol Ther Methods Clin Dev - pre-existing anti-AAV9 immunity does not bound CNS biodistribution after intrathecal dosing in macaques
**Full title:** Impact of pre-existing immunity on safety and biodistribution of a single AAV9 vector intrathecal injection in cynomolgus monkeys
**Authors:** Vono M, et al.
**Year:** 2025
**Source type:** primary research - non-GLP non-human primate toxicology and biodistribution
**Journal/source:** *Molecular Therapy: Methods & Clinical Development* 2025
**Identifier:** PMID 41210171 / PMCID PMC12590263 / DOI 10.1016/j.omtm.2025.101602
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-41210171-01`; manifest `deepdive_manifests/PMID41210171.json`; dossier `research/fulltext_dossiers/PMID41210171.md` (Figure 6 rendered and read at panel level; supplement fetched and read; Figures 1-5 captions only)
**Primary pathway:** CSF-route AAV9 delivery - pre-existing immunity, biodistribution, histopathology
**Model/species:** 15 female cynomolgus macaques, ~41 months, no immunosuppression, 4 weeks, terminal endpoints
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: the eligibility conclusion and the immunity/biodistribution dissociation transfer; the cargo (mCherry under a strong ubiquitous promoter) does not
**clinical relevance:** LOW for WWOX biology; MODERATE for any future CSF-route eligibility criterion
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** Carried for: high serum anti-AAV9 titre leaving CNS vector-genome biodistribution intact while **reducing** load to DRG, liver and heart and increasing it to spleen; and the authors' conclusion that serostatus should not alone exclude a candidate from intrathecal dosing. ⚠️ **The study has ONE dose level** (1.2 × 10¹³ vg/animal across all treated groups, read from the Figure 6C panel), so it cannot speak to dose at all. ⚠️ **The DRG finding has no incidence or severity count anywhere** - zero tables in the article, Figure 6C tabulates brain only, and the fetched supplement holds only titre tables. ⚠️ Figure 6C further shows the meningeal infiltrate in **2 of 3 vehicle animals**, the immunity "trend" resting on one animal of four, and perivascular infiltrate **non-monotonic** in titre. Female-only, no infant, no male, 4 weeks.
**LIT link:** [[literature_tracking_log_current#LIT-0466]]
**Note:** class-level record. Not medical advice.
## PAPER 179
**Short title:** Aihara 2025 Mol Ther Methods Clin Dev - empty capsid and promoterless vector do not reproduce the liver and DRG toxicity of a full AAV9 vector
**Full title:** Transcriptional changes in non-human primate tissues after intrathecal delivery of serotype 9 adeno-associated viral vector: Insights into organ toxicities
**Authors:** Aihara Y, et al.
**Year:** 2025
**Source type:** primary research - non-human primate transcriptomics across two toxicology studies
**Journal/source:** *Molecular Therapy: Methods & Clinical Development* 2025
**Identifier:** PMID 41257285 / PMCID PMC12621450 / DOI 10.1016/j.omtm.2025.101617
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-41257285-01`; manifest `deepdive_manifests/PMID41257285.json`; dossier `research/fulltext_dossiers/PMID41257285.md` (figures captions only; supplementary figures and tables not fetched)
**Primary pathway:** CSF-route AAV9 delivery - mechanism of organ toxicity; interferon / antigen-presentation transcriptional response
**Model/species:** 40 female cynomolgus macaques, 12-50 months, seronegative-selected, no immunosuppression, 28 days
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T3 for WWOX: the capsid-versus-expression discrimination bears directly on any WWOX restoration cassette, which is a promoter-driven protein transgene and therefore falls on the toxic side of this paper's dividing line
**clinical relevance:** LOW for WWOX biology; HIGH as the mechanistic layer under any CSF-route WWOX programme
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** The most mechanistically informative source in group C and the only one whose design separates capsid from expression: **hepatic and DRG toxicity occurred only with the full expressing vector, not with empty capsids and not with a promoterless genome at comparable capsid dose.** Also carries the interferon/JAK-STAT rather than NF-κB argument for why glucocorticoid prophylaxis may be insufficient (the authors' hypothesis; no immunosuppressed arm was run). ⚠️ **Counterweight from the same paper:** transgene transcript was highest in heart and skeletal muscle, the tissues *without* pathology, so expression **magnitude** does not predict which tissue is injured - this is in tension with [[paper_registry_current#PAPER 182]]'s attribution of DRG toxicity to supraphysiological expression, and the tension is recorded, not resolved. ⚠️ **The NfL correlation, the histopathology and all in-life toxicity are CITED to the authors' prior report, not measured here** - an open reading debt. Female-only, seronegative-only; must not be pooled with [[paper_registry_current#PAPER 178]], which selected the opposite.
**LIT link:** [[literature_tracking_log_current#LIT-0467]]
**Note:** class-level record. Not medical advice.
## PAPER 180
**Short title:** Stavrou 2026 Mol Ther Nucleic Acids - intrathecal AAV9 RNAi for CMT1A in mice and macaques; DRG lesions also present in half the vehicle controls
**Full title:** Safety, efficacy, and distal nerve Schwann cell biodistribution in mice and NHPs to support translation of AAV9 RNAi therapy for CMT1A
**Authors:** Stavrou M, et al.
**Year:** 2026
**Source type:** primary research - murine efficacy/toxicology plus non-human primate safety and biodistribution
**Journal/source:** *Molecular Therapy: Nucleic Acids* 2026
**Identifier:** PMID 41948127 / PMCID PMC13051718 / DOI 10.1016/j.omtn.2026.102881
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-41948127-01`; manifest `deepdive_manifests/PMID41948127.json`; dossier `research/fulltext_dossiers/PMID41948127.md` (Figure 5 rendered and read at panel level; Table 1 not read; supplementary pathology reports not fetched)
**Primary pathway:** CSF-route AAV9 delivery - peripheral nervous system biodistribution, DRG safety, functional electrophysiological monitoring
**Model/species:** CMT1A mice; 20 cynomolgus macaques, 10 male and 10 female, 6 and 12 weeks
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: the monitoring design, the control-arm DRG incidence and the slow-infusion procedure transfer; the cargo does not - this is knockdown of an over-expressed gene, the opposite direction from WWOX restoration, driven by a U6 small-RNA cassette rather than a promoter-driven protein transgene
**clinical relevance:** LOW for WWOX biology; HIGH for the DRG-attribution question and for safety-monitoring design
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** The load-bearing datum is in the **control** arm: minimal-to-mild DRG lesions in **2 of 4 saline-dosed macaques**. Supplies the group's best patient-transferable monitoring design (serial NCV and CMAP at baseline, 6 and 12 weeks, plus troponin I, ECG, ophthalmic examination) and its only explicit dose threshold (murine: 5E11 anti-inflammatory, 1E12 pro-inflammatory). ⚠️ **The Figure 5A caption denies DRG abnormality while the body reports lesions in 40% of animals**; the rendered panel supports the body. ⚠️ **Three internal quantity contradictions**: the low NHP dose is 6E13 in text but 5E13 in the Figure 5A row labels; the infusion volume is 4 mL in Results and 3 mL in Methods; the Figure 5A scale bars are stated in millimetres where the panel prints micrometres. See `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`. ⚠️ NfL is used here as a marker of **benefit** where [[paper_registry_current#PAPER 179]] uses it as a marker of **toxicity**.
**LIT link:** [[literature_tracking_log_current#LIT-0468]]
**Note:** class-level record. Not medical advice.
## PAPER 181
**Short title:** Engelhard 2026 Front Drug Deliv - CSF circulation variability and why a CSF-route dose is a distribution rather than a number
**Full title:** Variability in the circulation of cerebrospinal fluid: causes and clinical implications for intraventricular drug delivery
**Authors:** Engelhard HH, et al.
**Year:** 2026
**Source type:** narrative review - no primary measurement
**Journal/source:** *Frontiers in Drug Delivery* 2026
**Identifier:** PMID 42205472 / PMCID PMC13201979 / DOI 10.3389/fddev.2026.1735474
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-42205472-01`; manifest `deepdive_manifests/PMID42205472.json`; dossier `research/fulltext_dossiers/PMID42205472.md` (Tables 4 and 7 read cell-wise; remaining tables by title; Supplementary Material 2 not fetched)
**Primary pathway:** CSF physiology - production, pathway anatomy, flow dynamics, clearance; determinants of delivered dose at target
**Model/species:** human physiology with laboratory-species comparisons; review
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: a framing and method source, not an evidentiary one
**clinical relevance:** LOW for WWOX biology; MODERATE for dose-setting method on any CSF route
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** ⚠️ **Scope correction: this paper is about INTRAVENTRICULAR delivery, not intrathecal delivery**, contrary to the title under which it was assigned - route is the variable the reading set exists to separate from dose. Carried for: age named among the top three drivers of variability in delivered dose at a CSF route; the statement that fixed dosing across a population is current practice and inadequate for this route; and isotope-labelled AAV9 capsid PET as the only named route to measuring delivery in a living patient rather than at necropsy. ⚠️ **Table 4, the only cross-species scaling table in the group, has a single undated adult "human" row and therefore cannot set an infant dose**; its CSF volumes do independently reproduce the 371-fold mouse-to-macaque factor used in [[paper_registry_current#PAPER 180]]. Every number in this review is attributed to a cited primary and none was read.
**LIT link:** [[literature_tracking_log_current#LIT-0469]]
**Note:** class-level record. Not medical advice.
## PAPER 182
**Short title:** Kagiava 2026 eBioMedicine - the human intrathecal gene therapy record, the regulatory history of the DRG question, and the immunosuppression pattern keyed to predicted-null recipients
**Full title:** Progress and challenges in intrathecal gene therapy for neurological disorders
**Authors:** Kagiava A, et al.
**Year:** 2026
**Source type:** narrative review - no primary measurement
**Journal/source:** *eBioMedicine* 2026
**Identifier:** PMID 42134074 / PMCID PMC13196305 / DOI 10.1016/j.ebiom.2026.106294
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) - receipt `FTR-20261003-42134074-01`; manifest `deepdive_manifests/PMID42134074.json`; dossier `research/fulltext_dossiers/PMID42134074.md` (Table 1 read cell-wise; clinical sections read in full; preclinical sections by title only)
**Primary pathway:** CSF-route gene therapy - human clinical record, dose envelope, immunosuppression regimens, DRG safety history
**Model/species:** human clinical programmes plus preclinical index; review
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T3 for WWOX: the immunosuppression pattern keyed to predicted-null recipients applies to a biallelic loss-of-function WWOX genotype by construction; the nearest disease precedent (a paediatric neurodegenerative seizure-bearing disorder dosed intrathecally with the same capsid) is a precedent only
**clinical relevance:** LOW for WWOX biology; HIGH as the human layer under any CSF-route WWOX programme
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** The selection record called this "deliberately the weakest member" of its group and advised dropping it first; **that judgement is reversed here** - it is the only source carrying the human evidence base. Carries: the regulatory hold placed on a human paediatric intrathecal programme because of primate DRG findings; the human DRG outcome (sensory, mild, improved with symptomatic treatment where it appeared, and absent on MRI and nerve conduction at the highest human doses); and the pattern of **triple immunosuppression where the recipient is predicted null for the transgene product** versus a steroid alone where endogenous protein is present. ⚠️ **One paragraph's four hepatotoxicity percentages are internally incoherent as printed** - it compares one route to itself and gives a sham-control rate exceeding the treated rate - and none may be carried; the same paragraph calls a study single-arm while listing its sham groups. ⚠️ Its attribution of DRG toxicity to supraphysiological expression level is in tension with [[paper_registry_current#PAPER 179]]'s tissue-level data. Every datum is secondary; none of the cited primaries was read.
**LIT link:** [[literature_tracking_log_current#LIT-0470]]
**Note:** class-level record. Not medical advice.

## PAPER 183
**Short title:** Hudry 2023 Mol Ther — liver injury in cynomolgus monkeys after intravenous and intrathecal scAAV9; the hepatic arm of the CSF-route dose question
**Full title:** Liver injury in cynomolgus monkeys following intravenous and intrathecal scAAV9 gene therapy delivery
**Authors:** Hudry E, Aihara F, Meseck E, Mansfield K, McElroy C, Chand D, Tukov FF, Penraat K
**Year:** 2023
**Source type:** primary research — nonclinical safety/toxicology (NHP, mouse-free)
**Journal/source:** *Mol Ther* 2023;31(10):2999-3014
**Identifier:** PMID 37515322 / PMCID PMC10556189 / DOI 10.1016/j.ymthe.2023.07.020
**Status:** processed
**Record provenance:** created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-37515322-01`; manifest `deepdive_manifests/PMID37515322.json` (VERDICT PASS); dossier `research/fulltext_dossiers/PMID37515322.md`. Figure panels were not inspected; the depth label is read off the receipt and is not upgraded here.
**Primary pathway:** gene-therapy safety (P7) · hepatic endpoint · route
**Model/species:** cynomolgus macaque (NHP)
**Genotype/model:** none — cargoes SMN1 and reporter constructs; no WWOX construct
**Transferability:** T3 — transferable as a design fact about route, cassette and immunosuppression; no dose transfers to a WWOX cassette
**clinical relevance:** MODERATE strategic / NOT clinically validated
**Claim links:** none
**Role:** **WWOX content: none — the string WWOX occurs zero times.** Why held: the empty-capsid and promoterless arms that show the organ injury requires a transcriptionally productive genome; three immunosuppressive regimens (prednisolone IV, prednisolone IT, rituximab + everolimus IT) that did **not** prevent the transaminase rise or the microscopic findings; route sets hepatic magnitude and timing (liver 721 vg/dg after IV versus 19 vg/dg after IT; injury at day 3-4 versus about 2 weeks). 🔴 It is the primary behind **reference 10 of PMID 41257285**: the **hepatic** half of the carried sentence 'Hepatic and DRG toxicities were only detected after administration of full AAV9 viral particles' is sourced here; the **DRG** half is **not** — 'DRG' occurs once in this paper, in a biodistribution abbreviation list, and no dorsal-root-ganglion histopathology is reported for any arm (`BATCH_20261003_005`, `CC-20261003W6-C-DRG-ATTRIBUTION-01` §3a).
**LIT link:** [[literature_tracking_log_current#LIT-0476]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 184
**Short title:** Amaral 2026 Mol Ther Adv — intra-CNS AAV9 delivery: species and route differences in safety and transgene expression
**Full title:** Intra-CNS AAV9-delivery yields species and route of administration differences in safety and transgene expression
**Authors:** Amaral AC, Grubor B, Gianni D, Koetzner L, Abraham N, Bourque S, Brown D, Chen Y, Chicoine KE, Clarner P, De Giovanni PJ, Hamann S, Kirkland M, Mendes OR, Michael M, Nadella MVP, Nambiar K, Sebalusky J, Zeng W, Xu S, Trapa P, Plowey ED, Tien E, Fikes J, Walsh DM, Hirst WD, Suh J, Glajch KE
**Year:** 2026
**Source type:** primary research — nonclinical biodistribution and safety (mouse + NHP)
**Journal/source:** *Mol Ther Adv* 2026;34(3):201779
**Identifier:** PMID 42422766 / PMCID PMC13343144 / DOI 10.1016/j.omta.2026.201779
**Status:** processed
**Record provenance:** created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-42422766-01`; manifest `deepdive_manifests/PMID42422766.json` (VERDICT PASS); dossier `research/fulltext_dossiers/PMID42422766.md`. Figure panels were not inspected; the depth label is read off the receipt and is not upgraded here.
**Primary pathway:** gene-therapy safety (P7) · route · CNS biodistribution
**Model/species:** mouse (P0 ICV) + cynomolgus macaque
**Genotype/model:** none — cargo GBA1; no WWOX construct
**Transferability:** T3 — the route-versus-harm contrast transfers as a design fact; the magnitudes are capsid-, cargo- and species-specific
**clinical relevance:** MODERATE strategic / NOT clinically validated
**Claim links:** none
**Role:** **WWOX content: none (zero occurrences).** Why held: the one source in this corpus that holds the cargo fixed and varies the **route** — intracisterna magna gave cord and dorsal-root-ganglion transgene expression with adverse microscopic findings **at every dose level** and no significant brain GCase change, while intraparenchymal dosing gave brain expression, **no AAV-related DRG toxicity**, and adverse **brain** findings with early euthanasia of a whole dose group. 🔴 Its animals received **neither** an antibody pre-screen **nor** immunosuppression, stated by the authors; and its only statement in favour of immunosuppression says it *«can greatly reduce but not eliminate»* the findings and cites the authors' own unpublished data, not a measurement in this paper. The early-postnatal arm confounds age with species by the authors' own admission.
**LIT link:** [[literature_tracking_log_current#LIT-0477]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 185
**Short title:** Okai 2025 Mol Ther Methods Clin Dev — AAV1/AAV5/AAV9/AAVDJ biodistribution after intra-cisterna magna delivery in NHP
**Full title:** Biodistribution of AAV1, AAV5, AAV9, and AAVDJ serotypes after intra-cisterna magna delivery in non-human primates
**Authors:** Okai T, Sato S, Yasuno H, Nakayama M, Yamamoto S, Sjöqvist S, Otake K, Nakashima M, Deshpande M, Galbreath E, Oak JH, Miyamoto S, Proetzel G
**Year:** 2025
**Source type:** primary research — nonclinical biodistribution and tolerability (NHP)
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101593
**Identifier:** PMID 41078870 / PMCID PMC12509745 / DOI 10.1016/j.omtm.2025.101593
**Status:** processed
**Record provenance:** created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-41078870-01`; manifest `deepdive_manifests/PMID41078870.json` (VERDICT PASS); dossier `research/fulltext_dossiers/PMID41078870.md`. Figure panels were not inspected; the depth label is read off the receipt and is not upgraded here.
**Primary pathway:** gene-therapy safety (P7) · capsid choice · CNS biodistribution
**Model/species:** cynomolgus macaque, male only
**Genotype/model:** none — cargo GBA1; no WWOX construct
**Transferability:** T3 — 'capsid is not a lever on this route' transfers as a design fact; the deep-brain ceiling is route-specific
**clinical relevance:** MODERATE strategic / NOT clinically validated
**Claim links:** none
**Role:** **WWOX content: none (zero occurrences).** Why held: four capsids held against one fixed CSF route and one dose — no significant biodistribution difference, the authors decline to rank them, and no capsid reached deep brain above one copy per cell. 🔴 **And the worked example of a tolerability statement made under a regimen stated only in Methods:** every animal in both of its studies was under **weekly systemic methylprednisolone**, which appears in one Methods sentence and is restated nowhere, while the abstract, results and discussion say the procedure 'was well tolerated with no significant toxicity'. Sensory-ganglion degeneration occurred in 1 of 11 dosed animals despite sacral-DRG transgene positivity of 31-80 % of neurons, and the study contains **no unmedicated arm**, so this is not a controlled test of immunosuppression.
**LIT link:** [[literature_tracking_log_current#LIT-0478]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 186
**Short title:** DuBreuil 2025 Mol Ther Adv — a secretable frataxin: lowering vector burden instead of tolerating it
**Full title:** Development of a secretable frataxin for enhanced efficacy in treating Friedreich's Ataxia
**Authors:** DuBreuil DM, Fleming M, Parikh Y, Woo M, Bu J, Ayloo S, Langohr IM, Bangari DS, Mueller C, Ramachandran S
**Year:** 2025
**Source type:** primary research — vector and cargo engineering with NHP and mouse arms
**Journal/source:** *Mol Ther Adv* 2025;34(1):201661
**Identifier:** PMID 42157962 / PMCID PMC13182795 / DOI 10.1016/j.omta.2025.201661
**Status:** processed
**Record provenance:** created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-42157962-01`; manifest `deepdive_manifests/PMID42157962.json` (VERDICT PASS); dossier `research/fulltext_dossiers/PMID42157962.md`. Figure panels were not inspected; the depth label is read off the receipt and is not upgraded here.
**Primary pathway:** gene-therapy design (P7) · cargo engineering · dose window
**Model/species:** mouse + cynomolgus macaque
**Genotype/model:** none — cargo frataxin (FXN); no WWOX construct
**Transferability:** T2 for the **units** (fold-of-endogenous), T3 for the numbers; WWOX protein is intracellular and the secretion strategy does not transfer to it without evidence
**clinical relevance:** HIGH strategic / NOT clinically validated
**Claim links:** none
**Role:** **WWOX content: none (zero occurrences).** Why held: the one design in this corpus that lowers vector burden rather than tolerating it, and the only source that gives an **upper** bound on transgene product as a fold-of-endogenous figure. Route comparison with the same capsid: intravenous gave 62× less dorsal-root-ganglion and 25× less cerebellar-dentate transduction than intracisterna magna, and 10× more heart. 🔴 Even at lowered vector burden, minimal-to-mild DRG degeneration remained while brain and cord were spared. 🔴 The cross-correction logic rests on a **secreted** protein; WWOX is intracellular, so neither the mechanism nor the dose window carries over to a WWOX cassette.
**LIT link:** [[literature_tracking_log_current#LIT-0479]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 187
**Short title:** Chen 2023 J Clin Invest — intrathecal AAV9/AP4M1 for SPG50: the recessive-null IND-directed architecture closest to a WWOX programme
**Full title:** Intrathecal AAV9/AP4M1 gene therapy for hereditary spastic paraplegia 50 shows safety and efficacy in preclinical studies
**Authors:** Chen X, Dong T, Hu Y, De Pace R, Mattera R, Eberhardt K, Ziegler M, Pirovolakis T, Sahin M, Bonifacino JS, Ebrahimi-Fakhari D, Gray SJ
**Year:** 2023
**Source type:** primary research — complete IND-enabling package (patient fibroblasts, KO mouse, rat and NHP toxicology)
**Journal/source:** *J Clin Invest* 2023;133(10):e164575
**Identifier:** PMID 36951961 / PMCID PMC10178841 / DOI 10.1172/JCI164575
**Status:** processed
**Record provenance:** created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-36951961-01`; manifest `deepdive_manifests/PMID36951961.json` (VERDICT PASS); dossier `research/fulltext_dossiers/PMID36951961.md`. Figure panels were not inspected; the depth label is read off the receipt and is not upgraded here.
**Primary pathway:** gene-therapy design and safety (P7) · dose · immune interface
**Model/species:** human fibroblasts, mouse, rat, cynomolgus macaque
**Genotype/model:** none for WWOX — cargo AP4M1, a biallelic loss-of-function CNS disease
**Transferability:** T2 for the **architecture** (recessive null, intrathecal, age-dependent benefit), T3 for every dose figure
**clinical relevance:** HIGH strategic / NOT clinically validated
**Claim links:** none
**Role:** **WWOX content: none (zero occurrences).** Why held: the recessive-loss-of-function, intrathecal, IND-directed design closest in shape to a WWOX programme, and **the only graded per-animal lumbar-DRG incidence table in this corpus**. Under one constant regimen — i.v. methylprednisolone from day 1 to termination plus rapamycin from twelve days before dosing — the lumbar-DRG mononuclear infiltrate was present in **every** dosed animal at **both** dose levels while neuronal degeneration was 100 % at 1.68 × 10^14 vg/animal and 0 % at 8.40 × 10^13; the T-cell ELISpot was null under that regimen. 🔴 Early intervention and higher dose both helped in the mouse, so age and dose are not separable in the efficacy arm. 🔴 n = 2 per cohort in the NHP arm and no unmedicated arm.
**LIT link:** [[literature_tracking_log_current#LIT-0480]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 188
**Short title:** Ma 2025 Mol Med — AAV9-coSMN1 for spinal muscular atrophy: the group's only DRG-negative primate study, and its weakest reporting
**Full title:** Preclinical evaluation of AAV9-coSMN1 gene therapy for spinal muscular atrophy: efficacy and safety in mouse models and non-human primates
**Authors:** Ma W, Wu Z, Zhao T, Xia Y, Qin J, Tian X, Li X, He J, Zhang Y, Zhang L, Li L, Dong Z, Feng Z, Dong X, Sheng W, Wu X
**Year:** 2025
**Source type:** primary research — nonclinical efficacy and safety (mouse + NHP)
**Journal/source:** *Mol Med* 2025;31(1):158
**Identifier:** PMID 40301740 / PMCID PMC12042585 / DOI 10.1186/s10020-025-01207-4
**Status:** processed
**Record provenance:** created by `CC-20261003W6-C-REGISTRY-01` (intake wave 6 2026-10-03, Scientist C); renumbered from the candidate's provisional id by `BATCH_20261003_005`
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-40301740-01`; manifest `deepdive_manifests/PMID40301740.json` (VERDICT PASS); dossier `research/fulltext_dossiers/PMID40301740.md`. Figure panels were not inspected; the depth label is read off the receipt and is not upgraded here.
**Primary pathway:** gene-therapy safety (P7) · dose saturation
**Model/species:** mouse + cynomolgus macaque
**Genotype/model:** none — cargo codon-optimised SMN1; no WWOX construct
**Transferability:** T3 — a counterexample whose reporting depth does not support a strong negative
**clinical relevance:** LOW-MODERATE strategic / NOT clinically validated
**Claim links:** none
**Role:** **WWOX content: none (zero occurrences).** Why held: the one primate intrathecal study in this group that reports **no** dorsal-root-ganglion pathology, at 4.67 × 10^13 vg/animal, and the one whose efficacy saturated below the highest dose tested. 🔴 Recorded as a **live but weak** counterexample, not a refutation: its own Figure 7 legend (*«Representative pictures showing minor detectable sign of toxicity»*) disagrees with its Results text, Tables 1-2 carry no body in the JATS and were not fetched, and the paper is **silent about immunosuppression** — an absence that is itself a finding here.
**LIT link:** [[literature_tracking_log_current#LIT-0481]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 189
**Short title:** Cerulli Irelli 2025 Epilepsia — purified cannabidiol in 266 monogenic epilepsies; one Table 2 row of three WWOX patients (response at last follow-up)
**Full title:** Expanding the therapeutic role of highly purified cannabidiol in monogenic epilepsies: A multicenter real-world study
**Authors:** Cerulli Irelli E, Mazzeo A, Caraballo RH, et al.; Orsini A, Coppola A
**Year:** 2025
**Source type:** primary research — retrospective multicentre real-world cohort
**Journal/source:** *Epilepsia* 2025;66:2253-2267
**Identifier:** PMID 40126049 / PMCID PMC12291005 / DOI 10.1111/epi.18378
**Status:** processed
**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-40126049-01`; manifest `deepdive_manifests/PMID40126049.json`; dossier `research/fulltext_dossiers/PMID40126049.md`
**Primary pathway:** drug response (cannabidiol) · denominator
**Model/species:** human
**Genotype/model:** three WWOX patients, alleles not printed
**Transferability:** T3 — n = 3, adjunctive, uncontrolled; no allele class
**clinical relevance:** LOW-MODERATE — the only genotype-stratified CBD response row naming WWOX
**Claim links:** none (see `CC-20261003W6-B-CBDRESPONSE-01`, DL-MECH-030)
**Role:** Table 2 row WWOX (3 pts): mean seizure reduction 41.7 % (SD 38.2), ≥50 % responders 2/3, CGI-I improved 2/3, at last follow-up (minimum 3 months) on >99 % purified CBD added to a median of three ASMs. 🔴 No allele, age, syndrome, dose or follow-up length for these three; the authors warn that rows of two or three may reflect chance; overlap with held WWOX cases undetermined (INFERENZA); count once as an unlinked aggregate. Not medical advice.
**LIT link:** [[literature_tracking_log_current#LIT-0482]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 190
**Short title:** Innes 2025 Dev Med Child Neurol — IESS aetiopathogenesis and ACTH/corticosteroid mechanisms (scoping review); WWOX in two re-tabulated cohort rows
**Full title:** Aetiopathogenesis of infantile epileptic spasms syndrome and mechanisms of action of adrenocorticotrophin hormone/corticosteroids in children: A scoping review
**Authors:** Innes EA, Han VX, Patel S, Farrar MA, Gill D, Mohammad SS, Dale RC
**Year:** 2025
**Source type:** secondary — scoping review
**Journal/source:** *Dev Med Child Neurol* 2025;67:1004-1025
**Identifier:** PMID 40019827 / PMCID PMC12237231 / DOI 10.1111/dmcn.16273
**Status:** processed
**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-40019827-01`; manifest `deepdive_manifests/PMID40019827.json`; dossier `research/fulltext_dossiers/PMID40019827.md`
**Primary pathway:** denominator (IESS genetics) · ACTH mechanism
**Model/species:** human
**Genotype/model:** none of its own; re-tabulates WWOX (4) from PMID 37583270 and WWOX (1) from PMID 29455050
**Transferability:** none for WWOX — re-tabulation only
**clinical relevance:** LOW
**Claim links:** none
**Role:** Two WWOX counts from two independent cohorts (4 + 1); no WWOX response; ACTH effect placed at a regulatory, not gene-specific, level. 🔴 The four are already held via PMID 37583270; the single patient's primary (PMID 29455050) is unread. Adds no new patient.
**LIT link:** [[literature_tracking_log_current#LIT-0483]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 191
**Short title:** Zhu 2025 Front Pediatr — etiology of 361 IESS patients; one WWOX patient, no allele or response
**Full title:** Infantile epileptic spasms syndrome: an etiologic study of 361 patients with infantile epileptic spasms syndrome
**Authors:** Zhu L, Xia Y, Ding H, Zhang T, Li J, Li B
**Year:** 2025
**Source type:** primary research — retrospective two-hospital series
**Journal/source:** *Front Pediatr* 2025;12:1522079
**Identifier:** PMID 39850204 / PMCID PMC11754263 / DOI 10.3389/fped.2024.1522079
**Status:** processed
**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-39850204-01`; manifest `deepdive_manifests/PMID39850204.json`; dossier `research/fulltext_dossiers/PMID39850204.md`
**Primary pathway:** denominator (IESS)
**Model/species:** human
**Genotype/model:** one WWOX patient in the Genetic (37) group; alleles not printed
**Transferability:** denominator only
**clinical relevance:** LOW
**Claim links:** none
**Role:** 1 WWOX patient among 361 IESS (58 of the 165 'unknown' never genetically tested); authors' 'enzyme synthesis-related' grouping of WWOX is an unassayed construct. 🔴 Etiology only — no WWOX treatment or response.
**LIT link:** [[literature_tracking_log_current#LIT-0484]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 192
**Short title:** Snyder 2024 Genes — IESS genetics and precision-medicine opportunities (narrative review); WWOX one uncited autosomal-recessive list entry
**Full title:** Genetic Advancements in Infantile Epileptic Spasms Syndrome and Opportunities for Precision Medicine
**Authors:** Snyder HE, Jain P, RamachandranNair R, Jones KC, Whitney R
**Year:** 2024
**Source type:** secondary — narrative review
**Journal/source:** *Genes (Basel)* 2024;15(3):266
**Identifier:** PMID 38540325 / PMCID PMC10970414 / DOI 10.3390/genes15030266
**Status:** processed
**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-38540325-01`; manifest `deepdive_manifests/PMID38540325.json`; dossier `research/fulltext_dossiers/PMID38540325.md`
**Primary pathway:** denominator (IESS genetics) · precision medicine
**Model/species:** human
**Genotype/model:** none
**Transferability:** none
**clinical relevance:** LOW
**Claim links:** none
**Role:** WWOX listed (no citation) among autosomal-recessive IESS genes; the precision-medicine section names no WWOX or recessive-LoF strategy. 🔴 Gene-list membership only.
**LIT link:** [[literature_tracking_log_current#LIT-0485]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 193
**Short title:** Yuan 2025 Acta Epileptol — genetic DEE with movement disorders; WWOX top-ten gene, pooled 18-patient row (dystonia 15/18)
**Full title:** Advances in genetic developmental and epileptic encephalopathies with movement disorders
**Authors:** Yuan M, Wang X, Yang Z, Luo H, Gan J, Luo R
**Year:** 2025
**Source type:** secondary — narrative review with bibliometric step
**Journal/source:** *Acta Epileptol* 2025;7(1):9
**Identifier:** PMID 40217411 / PMCID PMC11960234 / DOI 10.1186/s42494-024-00194-z
**Status:** processed
**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-40217411-01`; manifest `deepdive_manifests/PMID40217411.json`; dossier `research/fulltext_dossiers/PMID40217411.md`
**Primary pathway:** movement phenotype
**Model/species:** human
**Genotype/model:** 18 pooled WWOX patients from unnamed primaries
**Transferability:** none for counting — primaries not named
**clinical relevance:** LOW
**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)
**Role:** Table 2 WWOX: dystonia 15/18, hypokinesia 5/18, ataxia 2/18, myoclonus 1/18, tremor 1/18, chorea 0, stereotypies 0. Table 1 (OMIM) lists WWOX under dystonia, myoclonus, ataxia, tremor, hypokinesia — not chorea. The 2021 'neonatal hypokinesia only with WWOX' framing is not repeated. 🔴 The 18 cannot be de-duplicated against held cases; text-table mismatches for other genes (CACNA1A).
**LIT link:** [[literature_tracking_log_current#LIT-0486]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 194
**Short title:** Mohammad 2026 Mov Disord Clin Pract — movement disorders in DEE (non-systematic review); four WWOX rows, all citing one cohort
**Full title:** Movement Disorders in Developmental and Epileptic Encephalopathies
**Authors:** Mohammad S, Ebrahimi-Fakhari D, Morales-Briceno H
**Year:** 2026
**Source type:** secondary — non-systematic structured review
**Journal/source:** *Mov Disord Clin Pract* 2026
**Identifier:** PMID 42068099 / PMCID PMC13339248 / DOI 10.1002/mdc3.70641
**Status:** processed
**Record provenance:** created by `CC-20261003W6-B-REGISTRY-01` (intake wave 6 2026-10-03, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-42068099-01`; manifest `deepdive_manifests/PMID42068099.json`; dossier `research/fulltext_dossiers/PMID42068099.md`
**Primary pathway:** movement phenotype · neuroimaging
**Model/species:** human
**Genotype/model:** none of its own
**Transferability:** none — re-description
**clinical relevance:** LOW
**Claim links:** none (see `CC-20261003W6-B-MOVEMENT-01`)
**Role:** WWOX in four Table 2 rows (IESS, excessive startle/hyperekplexia, corpus callosum abnormalities, white matter changes), every one citing PMID 36779245. 🔴 One cohort re-described four times; not corroboration; inherits the PUBLICATION_INTEGRITY_HOLD of PMID 36779245.
**LIT link:** [[literature_tracking_log_current#LIT-0487]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 195
**Short title:** Reinehr 2022 Biomolecules — rat autoimmune glaucoma; retinal Wwox mRNA lower (microarray probe fails FDR; qPCR 0.24-fold, n 3-4)
**Full title:** Heat Shock Protein Upregulation Supplemental to Complex mRNA Alterations in Autoimmune Glaucoma
**Authors:** Reinehr S, Safaei A, Grotegut P, et al.; Joachim SC
**Year:** 2022
**Source type:** primary research — experimental animal model (rat)
**Journal/source:** *Biomolecules* 2022;12(10):1538
**Identifier:** PMID 36291747 / PMCID PMC9599116 / DOI 10.3390/biom12101538
**Status:** processed
**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-36291747-01`; manifest `deepdive_manifests/PMID36291747.json`; dossier `research/fulltext_dossiers/PMID36291747.md`
**Primary pathway:** CNS injury expression (retina) — off-genotype
**Model/species:** rat (Lewis), immune-mediated retinal ganglion cell loss
**Genotype/model:** no WWOX genotype; acquired injury model
**Transferability:** T4 — expression change in an acquired injury; no transfer to a loss-of-function genotype class
**clinical relevance:** LOW
**Claim links:** none
**Role:** The only in-vivo record in LEGEND of Wwox expression falling in a non-genetic CNS injury. 🔴 The microarray 'fold change 0.864' is a ratio of log-scale means (linear about 0.47) and fails FDR (0.187); whole-retina qPCR 0.24-fold, p 0.002, n 3-4; mRNA only; the authors' 'regulatory role in the retina' is speculation.
**LIT link:** [[literature_tracking_log_current#LIT-0488]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 196
**Short title:** Dugan 2022 Neurobiol Aging — WWOX/MAF locus variants and autopsy endophenotypes (LATE-NC, HS, arteriolosclerosis)
**Full title:** Association between WWOX/MAF variants and dementia-related neuropathologic endophenotypes
**Authors:** Dugan AJ, Nelson PT, Katsumata Y, et al.; Fardo DW
**Year:** 2022
**Source type:** primary research — locus-restricted genetic association meta-analysis (two autopsy cohorts)
**Journal/source:** *Neurobiol Aging* 2022;111:95-106
**Identifier:** PMID 34852950 / PMCID PMC8761217 / DOI 10.1016/j.neurobiolaging.2021.10.011
**Status:** processed
**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-34852950-01`; manifest `deepdive_manifests/PMID34852950.json`; dossier `research/fulltext_dossiers/PMID34852950.md`
**Primary pathway:** adult neurodegeneration genetics — off-genotype
**Model/species:** human, adult autopsy cohorts (European ancestry)
**Genotype/model:** common non-coding variants; no loss-of-function allele
**Transferability:** none to WWOX-DEE
**clinical relevance:** LOW
**Claim links:** none
**Role:** Locus-wide (not genome-wide) associations with LATE-NC, hippocampal sclerosis and arteriolosclerosis. 🔴 The LATE-NC and arteriolosclerosis variants' only brain eQTL link is to MAF, not WWOX; the deposited Supplemental Table 6 (basis of 'independent of ADNC') repeats identical values across the NACC, ROSMAP and meta columns. Promotes [[paper_registry_current#CORPUS-STUB-033]].
**LIT link:** [[literature_tracking_log_current#LIT-0059]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 197
**Short title:** Kang 2026 npj Parkinsons Dis — multi-locus burden and dementia in PD; WWOX SNP rs8050111 one of five loci
**Full title:** Multi-locus genetic dosage shapes cognitive disease progression in Parkinson's patients: 15-year meta-analysis of 24 cohorts
**Authors:** Kang X, Lin Z, et al.; Scherzer CR
**Year:** 2026
**Source type:** primary research — multi-cohort longitudinal survival meta-analysis
**Journal/source:** *NPJ Parkinsons Dis* 2026;12
**Identifier:** PMID 42135313 / PMCID PMC13424109 / DOI 10.1038/s41531-026-01367-y
**Status:** processed
**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-42135313-01`; manifest `deepdive_manifests/PMID42135313.json`; dossier `research/fulltext_dossiers/PMID42135313.md`
**Primary pathway:** adult neurodegeneration genetics — off-genotype
**Model/species:** human, adult Parkinson's disease cohorts
**Genotype/model:** one common SNP (rs8050111), carrier vs non-carrier
**Transferability:** none to WWOX-DEE
**clinical relevance:** LOW
**Claim links:** none
**Role:** 🔴 The 'dose' is the number of loci carried, not WWOX allele dose. WWOX HR 1.56 overall but 1.16 (n.s.) in biomarker cohorts; design-subgroup heterogeneity significant in the supplement (p 0.02) and not reported in the main text; null MMSE slope; not independent of the 2021 discovery study (PMID 33958783).
**LIT link:** [[literature_tracking_log_current#LIT-0489]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 198
**Short title:** Pascual 2025 Biochem J — review: excess Wnt in neurological disease; one WWOX table row
**Full title:** Excess Wnt in neurological disease
**Authors:** Pascual DM, Jebreili Rizi D, Kaur H, Marcogliese PC
**Year:** 2025
**Source type:** review
**Journal/source:** *Biochem J* 2025;482(10):601-618
**Identifier:** PMID 40377402 / PMCID PMC12203940 / DOI 10.1042/BCJ20240265
**Status:** processed
**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-40377402-01` (all read; partial because its single WWOX source, PMID 19465938 / `FT-180`, is unread); manifest `deepdive_manifests/PMID40377402.json`; dossier `research/fulltext_dossiers/PMID40377402.md`
**Primary pathway:** P3 — Wnt/DVL (background)
**Model/species:** review
**Genotype/model:** DEE28 named; no allele class
**Transferability:** none — citation of a cancer-cell primary
**clinical relevance:** LOW
**Claim links:** none
**Role:** Table 1 row: WWOX, DEE28, 'preventing the nuclear import of the Dvl proteins', citing Bouteille 2009 only; the text never discusses WWOX. Adds no evidence independent of that primary (see `CC-20261003W6-A-WNT-01`).
**LIT link:** [[literature_tracking_log_current#LIT-0490]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 199
**Short title:** Sengupta 2025 iScience — sterols regulate DVL2 membrane/nuclear localisation; nuclear DVL2 with inhibited TCF/LEF signalling
**Full title:** Dishevelled localization and function are differentially regulated by structurally distinct sterols
**Authors:** Sengupta S, Yaeger JDW, Schultz MM, May DG, Roux KJ, Francis KR
**Year:** 2025
**Source type:** primary research — cell, iPSC-derived NSC and mouse
**Journal/source:** *iScience* 2025;28(6):112704
**Identifier:** PMID 40524961 / PMCID PMC12167792 / DOI 10.1016/j.isci.2025.112704
**Status:** processed
**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (partial full text) — receipt `FTR-20261003-40524961-01` (Figures 1-6 legends only; its single WWOX source, PMID 32368285, unread); manifest `deepdive_manifests/PMID40524961.json`; dossier `research/fulltext_dossiers/PMID40524961.md`
**Primary pathway:** P3 — Wnt/DVL (background; inference check)
**Model/species:** HEK293T; human iPSC-derived NSC; Dhcr7 mutant mouse cortex
**Genotype/model:** no WWOX manipulation
**Transferability:** none for WWOX data; bears on the inference step of DL-MOL-003
**clinical relevance:** LOW
**Claim links:** none
**Role:** One WWOX sentence citing Celebi 2020. Its own data show DVL2 moving to the nucleus while a TCF/LEF reporter is inhibited (Fig S6E): nuclear DVL2 and canonical Wnt hyperactivation come apart in this system (see `CC-20261003W6-A-WNT-01`). WWOX absent from its TurboID dataset (detection, not interaction, evidence).
**LIT link:** [[literature_tracking_log_current#LIT-0491]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 200
**Short title:** Hsu 2025 IJMS — review: hyaluronan in cancer and neural disease; HYAL-2/WWOX/SMAD4 and C1q-WWOX restated
**Full title:** Hyaluronan: An Architect and Integrator for Cancer and Neural Diseases
**Authors:** Hsu CY, Nguyen-Tran HH, Chen YA, et al.; Chang NS
**Year:** 2025
**Source type:** review
**Journal/source:** *Int J Mol Sci* 2025;26(11):5132
**Identifier:** PMID 40507943 / PMCID PMC12155404 / DOI 10.3390/ijms26115132
**Status:** processed
**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-40507943-01`; manifest `deepdive_manifests/PMID40507943.json`; dossier `research/fulltext_dossiers/PMID40507943.md`
**Primary pathway:** ECM / HYAL-2 / SMAD4 (background)
**Model/species:** review of DU145 prostate-cancer cell work
**Genotype/model:** over-expression paradigm; no loss-of-function genotype
**Transferability:** none to WWOX-DEE
**clinical relevance:** LOW
**Claim links:** CLAIM 027 (evidence boundary added by `CC-20261003W6-A-HYAL2-01`; this record is the review that adds no CNS evidence to that axis)
**Role:** All WWOX data re-presented are DU145 over-expression experiments from the authors' laboratory; the nervous-system section never mentions WWOX; the Alzheimer-risk sentence cites five non-Alzheimer papers; a patent is listed beside a no-conflict declaration (see `CC-20261003W6-A-HYAL2-01`).
**LIT link:** [[literature_tracking_log_current#LIT-0492]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 201
**Short title:** Celebi 2020 J Cancer — WWOX siRNA in a non-cancer oesophageal epithelial line shifts the Dvl cytoplasm/nucleus ratio; no Wnt output measured
**Full title:** Silencing of Wwox Increases Nuclear Import of Dvl proteins in Head and Neck Cancer
**Authors:** Celebi A, Orhan C, Seyhan B, Buyru N
**Year:** 2020
**Source type:** primary research — human cell lines and tumour/normal tissue pairs
**Journal/source:** *J Cancer* 2020;11(14):4030-4036
**Identifier:** PMID 32368285 / PMCID PMC7196265 / DOI 10.7150/jca.40840
**Status:** processed
**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A); promotes [[paper_registry_current#CORPUS-STUB-132]]. Number settled by measurement at `BATCH_20261004_003` [corrected 2026-10-04 from "Provisional number." by `BATCH_20261004_004`, Mirror note F9].
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-32368285-01` (article read end to end; partial because its single gene-direct reference, PMID 19465938, has no lawful free route and stays a declared manifest gap); manifest `deepdive_manifests/PMID32368285.json`; dossier `research/fulltext_dossiers/PMID32368285.md`
**Primary pathway:** P3 — Wnt/DVL (cancer context)
**Model/species:** human HET-1A (oesophageal squamous epithelial, non-cancer) and SCC-15 (tongue SCC); 98 HNSCC tumour/normal pairs, 50 of them for protein
**Genotype/model:** transient siRNA knockdown; no allele, no null
**Transferability:** T4 — epithelial knockdown with a band-intensity ratio readout; no neural, glial or developmental measurement
**clinical relevance:** LOW
**Claim links:** none
**Role:** The assay behind LEGEND's WWOX-Dvl direction, now read. 🔴 The silencing was done in HET-1A, a non-cancer oesophageal line, not in a head-and-neck cancer line; the quantity is a cytoplasm/nucleus band-intensity ratio with no replicate count, dispersion or p value (Table 4); the siRNA blot is not shown (Figure 4 has no siRNA lane and no nuclear-fraction marker); no beta-catenin or TCF/LEF readout exists anywhere in the paper; and Figure 1B prints p = 0.227 for the DVL-3 difference the Results call significant.
**LIT link:** [[literature_tracking_log_current#LIT-0494]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 202
**Short title:** Lange 2026 J Neurosci Res — astrocytes in genetic epilepsies; three of its four WWOX rows marked Unclear on cell autonomy, the fourth N/A
**Full title:** Astrocytes in Genetic Epilepsies: Supporting Actor or Key Player?
**Authors:** Lange J, Zhao E, O'Connell E, Gillham O, McTague A
**Year:** 2026
**Source type:** review (narrative)
**Journal/source:** *J Neurosci Res* 2026;104(8):e70148
**Identifier:** PMID 42558002 / PMCID PMC13444675 / DOI 10.1002/jnr.70148
**Status:** processed
**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A). Provisional number.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-42558002-01`; manifest `deepdive_manifests/PMID42558002.json`; dossier `research/fulltext_dossiers/PMID42558002.md`
**Primary pathway:** astrocyte biology / neuroinflammation (background)
**Model/species:** review of mouse, zebrafish, iPSC and organoid models
**Genotype/model:** four WWOX rows: constitutive null, P47T, human organoids (KO and a canonical splice-acceptor allele), conditional knockouts
**Transferability:** none — re-description of primaries LEGEND already holds
**clinical relevance:** LOW
**Claim links:** CLAIM 005 (evidence boundary added by `CC-20261004W7-A-ASTROCYTE-01`; this record is the third-party review that leaves cell autonomy open)
**Role:** A third-party, non-WWOX group tabulating the WWOX astrocyte evidence (no priority is claimed: no search for an earlier such table was run). 🔴 Of its four WWOX rows, the **three that report an astrocyte phenotype** are marked **Unclear** on the reactive-versus-cell-intrinsic axis — the constitutive null, the `P47T` knock-in and the iPSC organoid — while the Repudi 2021 conditional-knockout row reads **`N/A`**, *«No astrocyte changes reported»* [corrected 2026-10-04 by `CC-20261004-MIRROR-21`, replacing *«The first third-party, non-WWOX group to tabulate the WWOX astrocyte evidence. 🔴 Every one of its four WWOX rows is marked **Unclear** on the reactive-versus-cell-intrinsic axis,»*, the quantifier `BATCH_20261004_001` had already withdrawn from `CLAIM 005`], and it concludes the astrocyte phenotype is downstream of neuronal dysfunction. Two defects of its own: a Table 1 cell reads 'No seizures' where the narrative says only that no seizure activity was reported, and the narrative calls the organoid primary 'iPSCs edited to carry a patient variant' where that paper used CRISPR-engineered ES cells for the knockout and separately patient-derived iPSCs.
**LIT link:** [[literature_tracking_log_current#LIT-0495]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 203
**Short title:** Ramirez 2025 Alzheimers Dement — WWOX transcript differs by donor ancestry in iPSC-derived oligodendrocytes; no WWOX perturbation
**Full title:** Ancestral genomic functional differences in oligodendroglia: implications for Alzheimer's disease
**Authors:** Ramirez AM, Nasciben LB, Moura S, et al.; Vance JM
**Year:** 2025
**Source type:** primary research — iPSC multiome (snRNA-seq, snATAC-seq, Hi-C)
**Journal/source:** *Alzheimers Dement* 2025;21(9):e70593
**Identifier:** PMID 40937943 / PMCID PMC12426912 / DOI 10.1002/alz.70593
**Status:** processed
**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A). Provisional number.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-40937943-01` (figure panels read as captions only; thirteen supplementary tables not fetched); manifest `deepdive_manifests/PMID40937943.json`; dossier `research/fulltext_dossiers/PMID40937943.md`
**Primary pathway:** oligodendrocyte-lineage expression (background)
**Model/species:** human, 12 iPSC lines (four per ancestry) differentiated to neural spheroids with oligodendrocyte-lineage cells
**Genotype/model:** no WWOX manipulation; ancestry and APOE genotype are the contrasts
**Transferability:** T4 — usable only as a baseline-variance denominator for WWOX transcript in that lineage
**clinical relevance:** LOW
**Claim links:** none
**Role:** The only record in LEGEND where WWOX transcript is quantified in named human oligodendrocyte-lineage cells: iOL fold change -1.34 (AF vs AI, adjusted p 1.95E-05) and -1.33 (EU vs AI, adjusted p 9.59E-03), plus an all-female iOPC result. 🔴 What varies is donor ancestry, not WWOX dose; the MAST model carries no donor random effect, so the p values are nucleus-level; the authors' own sex-stratified check dropped seven of nine AD-GWAS genes; and the Results sentence says 'five' while naming six genes.
**LIT link:** [[literature_tracking_log_current#LIT-0496]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 204
**Short title:** Liu 2021 Nat Genet — genome-wide survival study; WWOX rs8050111 a suggestive PD-dementia progression locus
**Full title:** Genome-wide survival study identifies a novel synaptic locus and polygenic score for cognitive progression in Parkinson's disease
**Authors:** Liu G, Peng J, Liao Z, et al.; Scherzer CR
**Year:** 2021
**Source type:** primary research — genome-wide survival analysis, longitudinal cohorts
**Journal/source:** *Nat Genet* 2021;53(6):787-793
**Identifier:** PMID 33958783 / PMCID PMC8459648 / DOI 10.1038/s41588-021-00847-6
**Status:** processed
**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A); discharges the reading debt recorded in wave 6. Provisional number.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-33958783-01` (supplementary data not fetched; Extended Data Fig. 5 inspected as pixels); manifest `deepdive_manifests/PMID33958783.json`; dossier `research/fulltext_dossiers/PMID33958783.md`
**Primary pathway:** adult neurodegeneration genetics — off-genotype
**Model/species:** human, 3,821 Parkinson's patients over 31,053 visits
**Genotype/model:** one imputed common variant, rs8050111, risk allele frequency 0.066
**Transferability:** none to a biallelic loss-of-function genotype class
**clinical relevance:** LOW
**Claim links:** none
**Role:** The discovery source of the WWOX PD-progression SNP that LEGEND met second-hand in PMID 42135313. HR 2.12 (1.63-2.75), discovery p 1.08E-06, replication p 0.01, combined p 2.37E-08; the authors call it **suggestive** and WWOX is the nearest-gene column, with no eQTL or fine-mapping. 🔴 Extended Data Fig. 5 contradicts the sentence that calls WWOX expression neuron-specific: see `CC-20261004W7-A-NEURONSPEC-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0493]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 205
**Short title:** Karaer 2026 Epileptic Disord — exome/clinical exome in 250 Turkish children with unexplained epilepsy; two homozygous WWOX p.Arg264* patients
**Full title:** Clinical utility and genetic landscape of exome sequencing in a large pediatric epilepsy cohort: Insights from a Turkish tertiary care center
**Authors:** Karaer D, Yüzbaşı BK, Şahin İ, Güngör O, Karaer K
**Year:** 2026
**Source type:** primary research — retrospective single-centre exome cohort
**Journal/source:** *Epileptic Disord* 2026;28(4):1252-1273
**Identifier:** PMID 42394473 / PMCID PMC13499239 / DOI 10.1002/epd2.70277
**Status:** processed
**Record provenance:** created by `CC-20261004W7-B-REGISTRY-01` (intake wave 7 2026-10-04, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-42394473-01`; manifest `deepdive_manifests/PMID42394473.json`; dossier `research/fulltext_dossiers/PMID42394473.md`
**Primary pathway:** clinical spectrum / WWOX-DEE · denominator
**Model/species:** human
**Genotype/model:** two patients (Table 2 rows 29, 51), each homozygous `c.790C>T p.Arg264*` (nonsense; ACMG PVS1, PM3, PM2 → P); onset infantile and neonatal; generalized epileptic spasms in both
**Transferability:** T1 for the clinical presentation of a homozygous predicted-null genotype; none for missense classes
**clinical relevance:** LOW-MODERATE — counting source; phenotype is table-level
**Claim links:** none (see `CC-20261004W7-B-PATIENT-OVERLAP-01`)
**Role:** WWOX is one of the three commonest autosomal-recessive genes (n = 2 of 20 AR diagnoses in 89 P/LP). 🔴 Consequence predicted (PVS1), not measured. Regression and abnormal MRI are asserted only in the Discussion. The RTM mark 'R' is defined two incompatible ways (therapy-informed vs drug-resistant) and WWOX is not among the 12 therapy-informed patients; do not read it as a response. Whether the two patients are related is not stated. No held p.Arg264* homozygote is Turkish (the held ones are Indian): counted as two new patients.
**LIT link:** [[literature_tracking_log_current#LIT-0497]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 206
**Short title:** Alotibi 2023 Front Pediatr — array-CGH and WES in 105 Saudi children diagnosed with NDD 2015-2018; homozygous WWOX c.606-1G>A and c.33del rows without phenotype
**Full title:** The diagnostic yield of CGH and WES in neurodevelopmental disorders
**Authors:** Alotibi RS, Sannan NS, AlEissa M, et al.; Alfares A
**Year:** 2023
**Source type:** primary research — retrospective laboratory-record review
**Journal/source:** *Front Pediatr* 2023;11:1133789
**Identifier:** PMID 36937954 / PMCID PMC10014736 / DOI 10.3389/fped.2023.1133789
**Status:** processed
**Record provenance:** created by `CC-20261004W7-B-REGISTRY-01` (intake wave 7 2026-10-04, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-36937954-01`; manifest `deepdive_manifests/PMID36937954.json`; dossier `research/fulltext_dossiers/PMID36937954.md`
**Primary pathway:** clinical spectrum / allele presence · splice-acceptor allele class
**Model/species:** human
**Genotype/model:** two homozygous WWOX variant rows: canonical splice acceptor `NM_016373.4:c.606-1G>A` (P) and frameshift `c.33del p.Asp11GlufsTer69` (LP); no per-patient phenotype
**Transferability:** allele presence only; no course, outcome or RNA
**clinical relevance:** LOW — but the acceptor allele bears on the open Tabarki 2015 / Al Baradie family-3 overlap
**Claim links:** none (see `CC-20261004W7-B-PATIENT-OVERLAP-01`, `CC-20261004W7-B-SPLICE-MEASURED-01`)
**Role:** 🔴 A variant table, not a patient table: two rows, INFERENZA two patients. No sex, onset, course or outcome, so the c.606-1G>A homozygote can be neither matched to nor excluded from held homozygotes of the same allele (Shaukat 2018, Al Baradie 2022 family 3, Tabarki 2015, PMID 26345274): count once as unlinked, never summed with those series. Consequence predicted only (GERP, CADD); exon 7 is 186 nt, so an exon-7 skip would be in frame — not a null by default. Figure 2 shows a 'Seizure' category (~25 %) the text omits.
**LIT link:** [[literature_tracking_log_current#LIT-0498]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 207
**Short title:** Sabau 2025 Int J Mol Sci — panels/exomes/genomes in 140 Romanian children with epilepsy; one compound heterozygous WWOX patient (exon-5 copy gain + intron-6 donor delins)
**Full title:** Impact of Genetic Testing Using Gene Panels, Exomes, and Genome Sequencing in Romanian Children with Epilepsy
**Authors:** Sabau IM, Bacos-Cosma IS, Streata I, Dragulescu B, Puiu M, Chirita-Emandi A
**Year:** 2025
**Source type:** primary research — retrospective cohort
**Journal/source:** *Int J Mol Sci* 2025;26(10):4843
**Identifier:** PMID 40429983 / PMCID PMC12112176 / DOI 10.3390/ijms26104843
**Status:** processed
**Record provenance:** created by `CC-20261004W7-B-REGISTRY-01` (intake wave 7 2026-10-04, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-40429983-01`; manifest `deepdive_manifests/PMID40429983.json`; dossier `research/fulltext_dossiers/PMID40429983.md`
**Primary pathway:** clinical spectrum / WWOX-DEE · copy-number allele class
**Model/species:** human
**Genotype/model:** one child, compound heterozygous in trans: exon-5 copy gain (copy number 3, commercial panel call, no array) + `c.605+1_605+2delinsAA` (intron-6 donor); both LP
**Transferability:** T2 — both consequences predicted; the gain is unconfirmed by an orthogonal method
**clinical relevance:** LOW-MODERATE — first exon-level WWOX copy gain held; mild course
**Claim links:** none
**Role:** Supplement (not the body) carries the patient: DEE label, onset 0.83 years, focal epilepsy, hypotonia, one ASM, < 1 seizure/year, stationary; drug impact scored, its nature not stated. 🔴 The body's array confirmation refers to three other children; this gain's array cell reads 'no'. Orientation and breakpoints of the gain unknown.
**LIT link:** [[literature_tracking_log_current#LIT-0499]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 208
**Short title:** Khadija 2026 Front Genet — corpus callosum abnormalities in 107 Tunisian patients; one de novo heterozygous 16q23q24 deletion including WWOX
**Full title:** Clinical and genomic characterization of corpus callosum abnormalities (CCA) in 107 Tunisian patients using a stepwise diagnostic approach
**Authors:** Khadija B, Abdallah HH, Slimani W, et al.; Depienne C, Mougou-Zerelli S
**Year:** 2026
**Source type:** primary research — cross-sectional referral cohort
**Journal/source:** *Front Genet* 2026;17:1815268
**Identifier:** PMID 42807679 / PMCID PMC13617407 / DOI 10.3389/fgene.2026.1815268
**Status:** processed
**Record provenance:** created by `CC-20261004W7-B-REGISTRY-01` (intake wave 7 2026-10-04, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42807679-01`; manifest `deepdive_manifests/PMID42807679.json`; dossier `research/fulltext_dossiers/PMID42807679.md`
**Primary pathway:** CNV carrier / contiguous-gene deletion
**Model/species:** human
**Genotype/model:** one male infant, de novo heterozygous ~13 Mb 16q deletion (hg18) including WWOX, ANKRD11, ZNF778, CDH15, CDH13; remaining WWOX allele not sequenced
**Transferability:** none for WWOX-DEE allele classes; a contiguous-gene carrier
**clinical relevance:** LOW
**Claim links:** CLAIM 032 (evidence boundary added by `CC-20261004W7-B-CNV-CARRIER-01`; a contiguous-gene heterozygous deletion, not a haploinsufficiency datum)
**Role:** Callosal dysgenesis, hydrocephaly, microcephaly; no epilepsy recorded. 🔴 Not a WWOX-DEE allele-class observation and not a haploinsufficiency datum: dozens of genes deleted, other allele unexamined. Cannot bear on the Tabarki 2015 overlap (that report is a homozygous sequence allele). Wave-9 panel reading: the deletion is evidenced **only by its Table 3 row**; Figures 3-6 carry no array-CGH profile, karyotype or FISH image for it. ⚠️ **Audit amendment (blind locator audit, 2026-10-04):** Figure 6 is a 14-panel array-CGH **and MLPA** montage which does not include this deletion — it is called *representative* in the running text and **not in its own caption**, its panels include variants of uncertain significance, and one panel is an MLPA profile rather than array-CGH; two of the ten pathogenic or likely pathogenic carriers have no panel at all. Figure 3B marks one chromosome 16 long-arm pathogenic or likely pathogenic CNV without breakpoints, and the paper contains **no brain-imaging figure** — the callosal phenotype is a table cell. Figure 2 (patient photographs) was not opened. Arithmetic recomputed: the printed interval gives 13.17 Mb; the array-CGH diagnostic yield is 10/54 = 18.5%, and 16/54 = 29.6% counting variants of uncertain significance — the 54 are a **selected** subset, not the whole cohort.
**LIT link:** [[literature_tracking_log_current#LIT-0500]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 209
**Short title:** De 2025 Sci Rep — CNV dosage in two epilepsy cohorts and ten brain regions; a common WWOX intronic deletion with a nominal drug-response association
**Full title:** Dosage effect of copy number variation in epilepsy and ten regions of the human brain
**Authors:** De T, Coin L, Johnson MR
**Year:** 2025
**Source type:** primary research — CNV association and CNV-eQTL from bead-chip intensities
**Journal/source:** *Sci Rep* 2025;15:45726
**Identifier:** PMID 41345172 / PMCID PMC12753814 / DOI 10.1038/s41598-025-28338-2
**Status:** processed
**Record provenance:** created by `CC-20261004W7-B-REGISTRY-01` (intake wave 7 2026-10-04, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41345172-01`; manifest `deepdive_manifests/PMID41345172.json`; dossier `research/fulltext_dossiers/PMID41345172.md`
**Primary pathway:** population CNV / fragile site · drug response
**Model/species:** human
**Genotype/model:** common intronic deletion chr16:78,371,638-78,385,000 (GRCh37; the paper's region joins the gnomAD deletion DEL_16_156229, 78,371,638-78,384,898, and a multi-allelic record ending at 78,385,000, wave-9 panel reading), allele frequency 47 % in SANAD; gnomAD AF 0.339 with 1447 homozygotes (Supplementary Figure 19)
**Transferability:** none for WWOX-DEE; a population polymorphism at FRA16D
**clinical relevance:** LOW
**Claim links:** CLAIM 032 (evidence boundary added by `CC-20261004W7-B-CNV-CARRIER-01`; a common intronic polymorphism, not a dosage datum)
**Role:** 🔴 The Results sentence joins three signals: the deletion's own best p is nominal (drug response 1.68e-4, Supplementary Table 4; the table covers 559 distinct WWOX probe locations, whose Bonferroni threshold of about 8.9e-5 it does **not** reach, wave-9 measurement; the paper's stated correction adjusts for phenotype correlation and prints no M; «drug response» is binary 12-month remission, Supplementary Table 13); the genome-wide-strength meta-p (4.65e-22) lies ~660 kb away near the 3′ end; the authors themselves call for validation because of the fragile site. Methylation numbers come from cancer cohorts. One imprecise uncited sentence restricts WOREE to missense alleles. Not a disease-allele datum.
**LIT link:** [[literature_tracking_log_current#LIT-0501]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 210
**Short title:** Zhao 2026 NPJ Genom Med — targeted reflex blood RNA-seq after clinical ES/GS; WWOX c.1056+5G>C measured as partial exon deletion (VUS → LP)
**Full title:** Targeted reflex RNA sequencing for enhanced variant classification on exome and genome sequencing improves patient outcomes
**Authors:** Zhao X, Rigobello R, Driver M, et al.; Xia F, Eng CM
**Year:** 2026
**Source type:** primary research — retrospective clinical-laboratory series with a validated RNA assay
**Journal/source:** *NPJ Genom Med* 2026;11:52 [article number added 2026-10-04 by `BATCH_20261004_004` from the JATS front matter's `elocation-id`, Mirror note F7]
**Identifier:** PMID 42248868 / PMCID PMC13562735 / DOI 10.1038/s41525-026-00571-2
**Status:** processed
**Record provenance:** created by `CC-20261004W7-B-REGISTRY-01` (intake wave 7 2026-10-04, Scientist B). Provisional number: the integrator renumbers if taken and updates the `LIT link`.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-42248868-01`; manifest `deepdive_manifests/PMID42248868.json`; dossier `research/fulltext_dossiers/PMID42248868.md`
**Primary pathway:** splice-allele RNA consequence · method
**Model/species:** human
**Genotype/model:** one case, WWOX `c.1056+5G>C` (a donor +5 allele; placing it in **intron 8** is this repository's derivation from the WWOX exon map — `INFERENZA`, the source numbers no intron and no exon), autosomal recessive; zygosity and second allele not printed
**Transferability:** T1 for feasibility of measuring WWOX splicing in blood RNA; T3 for the reference genotype's acceptor allele (different position)
**clinical relevance:** MODERATE — a measured WWOX splice outcome in the same intron as the reference genotype's splice allele
**Claim links:** CLAIM 033 (evidence boundary added by `CC-20261004W7-B-SPLICE-MEASURED-01`; the measured blood-RNA splice outcome)
**Role:** EDTA-blood amplicon RNA-seq, net abnormal-junction threshold 20 %; Case 5 reclassified VUS → LP, RNA consequence 'partial exon deletion', positive, ID/DD. 🔴 No junction, read fraction, frame, NMD or protein reported; the assay reads neither expression nor NMD.
**LIT link:** [[literature_tracking_log_current#LIT-0502]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 211
**Short title:** Hordeaux & Chan 2026 Mol Ther Adv — commentary: how much of AAV dorsal-root-ganglion toxicity is immune-mediated?
**Full title:** Deciphering the role and contribution of AAV immune responses to DRG toxicity
**Authors:** Hordeaux J, Chan YK
**Year:** 2026
**Source type:** commentary (PubMed publication type News); two authors; no abstract, no original data; both declare gene-therapy company employment
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201675
**Identifier:** PMID 42137271 / PMCID PMC13148899 / DOI 10.1016/j.omta.2026.201675
**Status:** processed
**Record provenance:** created by `CC-20261004w7-C1-REGISTRY-01` (intake wave 7 2026-10-04, Scientist C1); the candidate specified the record in prose and the integrator authored it.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-42137271-01`; manifest `deepdive_manifests/PMID42137271.json`; dossier `research/fulltext_dossiers/PMID42137271.md`. The whole body of a two-author commentary (one Main-text section) was read and its single schematic figure inspected as an image; no abstract, table or supplement exists.
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** cynomolgus and rhesus macaque, intracisterna magna route — every result **relayed**, none measured here
**Genotype/model:** no WWOX allele; WWOX occurs zero times in this source (an earned null for the gene)
**Transferability:** T3 — a counter-reading of a primate primary LEGEND already holds ([[paper_registry_current#PAPER 162]], PMID 41404412); it measures nothing of its own
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** A counter-reading of the Biogen primary already held: *«IS reduced but did not eliminate the severity or incidence of DRG toxicity»*; severity *«closely correlated with the levels of transgene expression»*; the protective regimen included **no clinically relevant immunosuppression tapering**, so whether the reduction is sustained is unclear in the commentators' own words; a rebound and a *«delayed AAV-mediated DRG toxicity phenotype equivalent or slightly decreased»* after withdrawal of a time-limited antimetabolite are relayed from the commentators' earlier work; and the discriminating design — a promoterless payload that still raises an immune response — is named as **not done**. ⚠️ Integrator amendment (blind audit): the same paragraph states they *«do not identify a singular driver of toxicity»*, because transgene expression, ultrastructural neuronal changes, innate immune activation and cellular infiltrates were **all present from the earliest time point (day 5)**; and of the two earlier papers cited for the rebound, only the first is identifiable from this artefact as a rhesus-macaque study. 🔴 It measures nothing. Carried into the research layer by `RL-C-20261004w7c1`.
**LIT link:** [[literature_tracking_log_current#LIT-0503]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 212
**Short title:** Flotte 2026 Mol Ther Adv — commentary: the dose makes the poison; three dose-scaled stimuli of high-dose AAV
**Full title:** The dose makes the poison: Mechanisms of cytotoxicity of high-dose AAV vectors
**Authors:** Flotte TR
**Year:** 2026
**Source type:** commentary (PubMed publication type News); single author; no abstract, no original data
**Journal/source:** *Molecular Therapy Advances* 2026;34(2):201746
**Identifier:** PMID 42170349 / PMCID PMC13188094 / DOI 10.1016/j.omta.2026.201746
**Status:** processed
**Record provenance:** created by `CC-20261004w7-C1-REGISTRY-01` (intake wave 7 2026-10-04, Scientist C1); the candidate specified the record in prose and the integrator authored it.
**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-42170349-01`; manifest `deepdive_manifests/PMID42170349.json`; dossier `research/fulltext_dossiers/PMID42170349.md`. Whole body of a single-author commentary read; its figure inspected as an image; no abstract, table or supplement exists.
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** cynomolgus macaque and rat liver — **relayed**; systemic high-dose AAV
**Genotype/model:** no WWOX allele; WWOX occurs zero times in this source (an earned null for the gene)
**Transferability:** T3 — a **liver, systemic-route** commentary, not a DRG source; its DRG content is one sentence and a citation, and the primary it comments on is **not held** by LEGEND
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** Supplies a three-stimulus decomposition of what the held records carry as the single word *dose*: (1) nuclear vector DNA converted to a double-stranded form, presenting *«hundreds of copies of what appear to be double-stranded DNA breaks»* and activating double-strand-break repair, with downstream interactions that *«may lead to various results, including apoptosis in cells that lack p53 expression»*; (2) innate sensing of capsid and genome through TLR2 and TLR9 by vector copies that never enter the nucleus; (3) transgene overexpression once the DNA becomes transcriptionally active, with the unfolded-protein response — where *«the magnitude of UPR activation, particularly the PERK-induced … response, was strongly associated with the level of transgene expression»* across the relayed datasets, and genes triggering mitochondrial apoptosis were induced by the same pathway. 🔴 It measures nothing. Carried into the research layer by `RL-C-20261004w7c1`.
**LIT link:** [[literature_tracking_log_current#LIT-0504]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 213
**Short title:** Rioux 2026 Genes — head-to-head AAV9 biodistribution in mice by route and age; neonatal mortality ordered by route and dose, DRG transduced without DRG injury
**Full title:** A Head-to-Head Comparison of AAV9 Biodistribution in Mice: Routes of Administration and Age Dependence
**Authors:** Rioux M, Boitnott A, Paduri S, Hu Y, Gray SJ
**Year:** 2026
**Source type:** primary research article, peer reviewed, open access
**Journal/source:** *Genes* 2026;17(2):213
**Identifier:** PMID 41751597 / PMCID PMC12940312 / DOI 10.3390/genes17020213
**Status:** processed
**Record provenance:** created by `CC-20261004w7-C1-REGISTRY-01` (intake wave 7 2026-10-04, Scientist C1); the candidate specified the record in prose and the integrator authored it.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41751597-01`; manifest `deepdive_manifests/PMID41751597.json`; dossier `research/fulltext_dossiers/PMID41751597.md`. Partial: Figures 4 to 6 and several appendix figures read as **captions only**; references not read; no supplement beyond the embedded appendix.
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** wild-type C57BL/6J mouse; self-complementary AAV9 carrying GFP under a strong constitutive promoter; lumbar intrathecal, intracerebroventricular, IT & ICV and intravenous routes at postnatal days 1, 5, 10 and 28
**Genotype/model:** no WWOX allele; WWOX occurs zero times in this source (an earned null for the gene); a constitutive reporter models no human allele
**Transferability:** T3 — a reporter-vector biodistribution study; it bounds no WWOX dose, route or age
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** Doses were *«not adjusted to age or body weight»*: one of two fixed **total** vg levels (2.5 × 10¹¹ or 5 × 10¹¹) per animal across a tenfold body-weight and fivefold brain-weight range, so dose per gram of tissue falls with age in every arm. Mortality after lumbar IT dosing at day 1 (47 %, mean 10 days to termination) and day 5 (70 % at 5 × 10¹¹, 17 % at 2.5 × 10¹¹) and **none** after IV dosing; in the euthanised animals reviewed the **spinal cord was injured and the DRG normal**, while the DRG was transduced by every route and age (Figure A6, the authors' word is *«suggests»*; their section summary states it flatly). 🔴 The authors attribute the deaths, *«most likely»*, to localised GFP overexpression toxicity; the design carried only vehicle and two AAV9/GFP dose arms — **no null or promoterless control** — and the authors nowhere note that absence (integrator amendment, blind audit). DRG histology of the **survivors** was not reported, and the paper states that whether route or age affects the amount of DRG transgene *«remains unclear»*. Carried by `RL-C-20261004w7c1` and `RL-C-20261004w7c2`.
**LIT link:** [[literature_tracking_log_current#LIT-0505]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 214
**Short title:** Gao 2026 Biomedicines — four AAV capsids by neonatal intravenous route in the murine nervous system; DRG transduced, liver enzymes raised by one capsid
**Full title:** Comparative Transduction Profiling of Four Intravenously Delivered AAV Capsids in the Neonatal Murine Nervous System
**Authors:** Gao H, Xu T [corrected 2026-10-04 by `CC-20261004-MIRROR-22`, replacing *«Gao H, Xu T, Lebleu B»*: Lebleu B is the journal's Academic Editor in the JATS `editor` contrib-group, not an author]
**Year:** 2026
**Source type:** primary research article, peer reviewed, open access
**Journal/source:** *Biomedicines* 2026;14(7):1426
**Identifier:** PMID 42511902 / PMCID PMC13405926 / DOI 10.3390/biomedicines14071426
**Status:** processed
**Record provenance:** created by `CC-20261004W7-C2-REGISTRY-01` (intake wave 7 2026-10-04, Scientist C2); the candidate specified the record in prose and the integrator authored it.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42511902-01`; manifest `deepdive_manifests/PMID42511902.json`; dossier `research/fulltext_dossiers/PMID42511902.md`.
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** neonatal mouse, intravenous at postnatal day 2; AAV9, rAAV2-retro, AAV-PHP.eB and AAV-MacpnS1; CNS, DRG, heart, liver and serum liver enzymes at one time point
**Genotype/model:** no WWOX allele; WWOX occurs zero times in this source (an earned null for the gene)
**Transferability:** T3 — a neonatal-IV capsid atlas; it is neither a developmental-window result nor a safety study
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** A fourth dose scalar in use: *«1 × 10¹⁰ vg was selected as the dose per pup»* and *«For a P2 pup (~2.0 g body weight), this corresponds to approximately 5.0 × 10¹² vg/kg»* — arithmetic re-derived and exact (1 × 10¹⁰ ÷ 0.002 kg = 5.0 × 10¹² vg/kg). DRG transduction by reporter intensity was high with AAV9 and AAV-MacpnS1 and about **4- to 6-fold lower** with rAAV2-retro and AAV-PHP.eB; serum ALT and AST were raised **only with AAV-MacpnS1**, at one time point. 🔴 Single dose, single age, single harvest; **no immune endpoint at all**; the measured quantity is eGFP fluorescence intensity, which the authors read as transduction. **Carried-number integrity:** the paper states a 2 µL injection volume inside a ~22 µL mixture (20 µL saline + 2 µL stock, internally consistent) and an n of *«at least four»* against n = 6 and n = 8 in legends — carry its numbers with these.
**LIT link:** [[literature_tracking_log_current#LIT-0506]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 215
**Short title:** Zhao 2025 PLOS One — volumetric MRI of dorsal root ganglia as a progression and AAV-response biomarker in a Fabry mouse
**Full title:** Volumetric MRI of dorsal root ganglia as a biomarker for disease progression and response to AAV treatment in a mouse model of Fabry disease
**Authors:** Zhao F, Yuan S, Kaittanis C, Deshpande M, Kugadas A, Derakhchan K, Ruangsiriluk W, Islam R, Boukharov N, McQuade P, et al.
**Year:** 2025
**Source type:** primary research article, peer reviewed, open access; sponsor-authored
**Journal/source:** *PLOS One* 2025;20(10):e0334840
**Identifier:** PMID 41134821 / PMCID PMC12551818 / DOI 10.1371/journal.pone.0334840
**Status:** processed
**Record provenance:** created by `CC-20261004W7-C2-REGISTRY-01` (intake wave 7 2026-10-04, Scientist C2); the candidate specified the record in prose and the integrator authored it.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41134821-01`; manifest `deepdive_manifests/PMID41134821.json`; dossier `research/fulltext_dossiers/PMID41134821.md`.
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety; endpoint and biomarker method
**Model/species:** Fabry mouse (GLA), 7 T MRI of L4 dorsal root ganglia, AAV9-GLA and AAV-null arms
**Genotype/model:** no WWOX allele; WWOX occurs zero times in this source (an earned null for the gene)
**Transferability:** T3 — a **storage-enlargement** endpoint in a different disease; method only
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** The **only DRG imaging endpoint in this corpus**, and it measures the storage-lesion direction: L4 DRG cross-sectional area from an axial maximum-intensity projection detected a roughly 25 % enlargement in the Fabry mouse (0.35 vs 0.28 mm², i.e. 1.25×, re-derived) at 24 weeks and its normalisation after AAV9-GLA. Repeatability in **five wild-type mice (10 L4 DRGs)**: ICC 0.9, limits of agreement −0.060 to 0.066 mm² on a Table 2 grand mean of 0.257 mm² (0.258 test, 0.255 retest; cell-checked by the integrator) — a band of about the same size as the group-level disease effect (0.07 mm²), with per-DRG test-retest relative differences running from −15.4 % to +19.4 %. 🔴 It was never tested against a lesion that **shrinks or destroys** DRG neurons, which is the direction of AAV-associated DRG toxicity, and there is **no wild-type AAV-injected group**, so the design could not register vector injury. ⚠️ Integrator amendments (blind audit): the source adds that its Bland–Altman plot shows *«a trend of increasing variability with larger CSA values»*; and the DRG/spinal-cord contrast failure is confined by the authors to **their own T2-weighted acquisition** — they state published T2 values for the two tissues are distinct — so it is a limitation of this acquisition, not an intrinsic property. Group sizes disagree between Results and Methods (fifteen against thirteen Fabry mice). **Corrects the wave-7 selection note:** this paper conflates benefit and injury in no number, because it measures only the storage direction.
**LIT link:** [[literature_tracking_log_current#LIT-0507]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 216
**Short title:** Thomsen 2026 Mol Ther Adv — CSF-route AAV9 micro-dystrophin preclinical package; DRG held vector genomes without transgene RNA
**Full title:** Preclinical evaluation of INS1201 AAV9-micro-dystrophin via CSF administration as a potential therapy for Duchenne muscular dystrophy
**Authors:** Thomsen G, Kaspar A, Ferraiuolo L, Chu B, Garcia VJ, Weiss R, Slaiwa T, Casanova-Vallve N, Cano R, Hurley E, et al.
**Year:** 2026
**Source type:** primary research article, peer reviewed, open access; sponsor-authored
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201707
**Identifier:** PMID 42137291 / PMCID PMC13148950 / DOI 10.1016/j.omta.2026.201707
**Status:** processed
**Record provenance:** created by `CC-20261004W7-C2-REGISTRY-01` (intake wave 7 2026-10-04, Scientist C2); the candidate specified the record in prose and the integrator authored it.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42137291-01`; manifest `deepdive_manifests/PMID42137291.json`; dossier `research/fulltext_dossiers/PMID42137291.md`. Partial: Table S5 and Figure S7 were fetched in wave 9 (receipt `FTR-20261004-42137291-02`) and carry **no DRG grading** (Table S5 is clinical pathology; Figure S7 is vector-genome biodistribution and shedding); references and most supplementary figures remain unread.
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** mdx mouse and cynomolgus macaque (GLP 1–2 kg, non-GLP 2–4 kg), intrathecal/CSF route; AAV9 with the muscle-derived MHCK7 promoter
**Genotype/model:** no WWOX allele; WWOX occurs zero times in this source (an earned null for the gene)
**Transferability:** T3 — the closest **process** analogue in this corpus by document shape (dose levels, GLP mouse and NHP, DRG evaluation, shedding, CSF-volume dose scaling); a muscle target and a promoter that cannot drive neuronal expression
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** A CSF-route AAV9 with a **muscle-restricted** promoter put vector genomes in DRG (mouse 6.408 vg per diploid genome at 12 weeks, high dose) with **no transgene mRNA or protein there**, and the mouse DRG was reported as healthy cells with normal histopathology at the high dose; NHP (n = 3 per dose group plus n = 3 vehicle) showed no INS1201-related histopathology in a **general** statement, with no transgene RNA in DRG or spinal cord. Dose scaling is by **CSF volume**, 0.04 to 10 mL, a factor of **250** (re-derived exactly), used to call 8.0 × 10¹¹ vg in mouse equivalent to 2.0 × 10¹⁴ vg in a juvenile NHP; the planned human fixed starting doses (5.0 × 10¹⁴ and 1.0 × 10¹⁵ vg) **exceed** the highest NHP per-animal total (3.05 × 10¹⁴ vg). 🔴 No immunosuppression regimen is described and anti-AAV9 antibodies were present in all treated NHP by day 28; the DRG-specific NHP grading is **not printed in the body or the supplement** (verified on the rendered table and figure, wave-9 blind audit 2026-10-04); the body's blanket *«no significant … effects … or histopathology»* sentence **names no neural tissue**, and the only DRG histopathology shown anywhere in the paper is **mouse**. ⚠️ Integrator amendment (blind audit): the authors offer the efficacy plateau at 4.0 × 10¹¹ vg as something that *«could be due to»* dosing at p27–35, after myofibre degeneration and regeneration have begun — a hedged suggestion, not a settled attribution.
**LIT link:** [[literature_tracking_log_current#LIT-0508]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 217
**Short title:** Colin 2023 Front Cell Dev Biol — multi-omics diagnostics; one WWOX genotype with blood RT-PCR and a fibroblast western
**Full title:** Stepwise use of genomics and transcriptomics technologies increases diagnostic yield in Mendelian disorders
**Authors:** Colin E, Duffourd Y, Chevarin M, et al.; Vitobello A
**Year:** 2023
**Source type:** primary research — diagnostic multi-omics series
**Journal/source:** *Front Cell Dev Biol* 2023;11:1021920
**Identifier:** PMID 36926521 / PMCID PMC10011630 / DOI 10.3389/fcell.2023.1021920
**Status:** processed
**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A); numbers re-measured by the integrator with `registry_records.py catalog` at `761b36909fa4` and applied unchanged (`PAPER 216` / `LIT-0508` were the ceiling).
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-36926521-01`; manifest `deepdive_manifests/PMID36926521.json`; dossier `research/fulltext_dossiers/PMID36926521.md`
**Primary pathway:** P1 — allele consequence / splicing
**Model/species:** human — patient blood (PAXgene) RT-PCR and one patient fibroblast line against one control
**Genotype/model:** exon-1 missense `p.(Thr12Arg)` + structural variant inverting exon 5; compound heterozygous
**Transferability:** T3 — neither allele is the reference genotype's class
**clinical relevance:** MODERATE
**Claim links:** CLAIM 033
**Role:** RNA consequence **measured** for the structural allele only — exon 5 skipping by blood RT-PCR over exons 4-6, a 186 bp product beside the expected 293 bp, confirmed by amplicon sequencing, **without a skipped fraction, a frame statement or an NMD test**. One fibroblast western measures the **genotype** qualitatively (strongly reduced band, faint residual, one control, no quantification) and **cannot apportion the reduction between the two alleles**. Nothing transfers to the reference genotype's alleles. See the dossier and `CC-20261004W8-A-MEASURED-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0509]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 218
**Short title:** Pagnamenta 2023 Genome Med — clinical WGS cohort; its WWOX case re-reports Piard 2019 Patient 11
**Full title:** Structural and non-coding variants increase the diagnostic yield of clinical whole genome sequencing for rare diseases
**Authors:** Pagnamenta AT, Camps C, Giacopuzzi E, et al.; Taylor JC
**Year:** 2023
**Source type:** primary research — clinical whole-genome sequencing cohort
**Journal/source:** *Genome Med* 2023;15(1):94
**Identifier:** PMID 37946251 / PMCID PMC10636885 / DOI 10.1186/s13073-023-01240-0
**Status:** processed
**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A); numbers re-measured by the integrator with `registry_records.py catalog` at `761b36909fa4` and applied unchanged (`PAPER 216` / `LIT-0508` were the ceiling).
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-37946251-01`; manifest `deepdive_manifests/PMID37946251.json`; dossier `research/fulltext_dossiers/PMID37946251.md`
**Primary pathway:** P1 — allele consequence / genotype census
**Model/species:** human — DNA only
**Genotype/model:** in-frame deletion of exons 6-8 + `c.705dup p.(His236fs)`; DNA only
**Transferability:** none — re-report of a patient this registry already holds
**clinical relevance:** LOW
**Claim links:** CLAIM 033
**Role:** **Not an independent patient (DATO):** the paper's own Table 1 records its WWOX case as *«Reported as Patient 11 (Table S1) in case series in Piard et al»*, i.e. Patient 11 of [[paper_registry_current#PAPER 117]], and the genotype matches that paper's Supplementary Table 1. **Count once.** The in-frame exons 6-8 deletion is coded with a null criterion (`PVS1, PM2, PM3`) and **no RNA or protein was measured** — a rule, not a measurement. See `CC-20261004W8-A-PATIENT-OVERLAP-01` and `CC-20261004W8-A-MEASURED-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0510]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 219
**Short title:** Hamanaka 2025 NPJ Genom Med — genome sequencing in ID/DD; one WWOX case, intron-5 acceptor allele + exon-5 deletion, DNA only
**Full title:** Genome sequencing provides high diagnostic yield and new etiological insights for intellectual disability and developmental delay
**Authors:** Hamanaka K, Fujita A, Miyatake S, et al.; Matsumoto N
**Year:** 2025
**Source type:** primary research — diagnostic genome-sequencing cohort
**Journal/source:** *NPJ Genom Med* 2025;10(1):60
**Identifier:** PMID 40858643 / PMCID PMC12381280 / DOI 10.1038/s41525-025-00521-4
**Status:** processed
**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A); numbers re-measured by the integrator with `registry_records.py catalog` at `761b36909fa4` and applied unchanged (`PAPER 216` / `LIT-0508` were the ceiling).
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-40858643-01`; manifest `deepdive_manifests/PMID40858643.json`; dossier `research/fulltext_dossiers/PMID40858643.md`
**Primary pathway:** P1 — allele consequence / splicing
**Model/species:** human — DNA only, trio-phased
**Genotype/model:** `c.517-1G>A` + single-exon deletion spanning exon 5; trio-phased
**Transferability:** T3 — an **intron-5** acceptor allele. 🔴 `c.517-1G>A` is **not** the `c.517-2A>G` allele of [[paper_registry_current#PAPER 039]] and **not** the reference genotype's acceptor allele; a shared position class is not a shared allele
**clinical relevance:** LOW
**Claim links:** CLAIM 033
**Role:** Both consequences are **predicted by rule** (`PVS1, PM2, PM3, PP3`) with **no RNA and no protein assay**. An allele coded null without a measurement is a classification. See the dossier and `CC-20261004W8-A-MEASURED-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0511]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 220
**Short title:** Yigit 2026 Front Neurol — re-analysis in children with a cerebral-palsy diagnosis; one homozygous WWOX p.Leu239Arg child
**Full title:** Unmasking genetic etiologies in neurodevelopmental disorders characterized by Cerebral Palsy: insights from integrative genomic approaches
**Authors:** Yigit A, Akgun-Dogan O, Ozkeserli Z, et al.; Ozbek U
**Year:** 2026
**Source type:** primary research — diagnostic re-analysis cohort
**Journal/source:** *Front Neurol* 2026;17:1742186
**Identifier:** PMID 41835067 / PMCID PMC12979860 / DOI 10.3389/fneur.2026.1742186
**Status:** processed
**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A); numbers re-measured by the integrator with `registry_records.py catalog` at `761b36909fa4` and applied unchanged (`PAPER 216` / `LIT-0508` were the ceiling).
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41835067-01`; manifest `deepdive_manifests/PMID41835067.json`; dossier `research/fulltext_dossiers/PMID41835067.md`
**Primary pathway:** P1 — allele consequence / genotype census
**Model/species:** human — DNA and segregation only
**Genotype/model:** homozygous `c.716T>G p.(Leu239Arg)`; DNA and segregation only
**Transferability:** T3 — `p.Leu239Arg` is not Q230P and nothing functional was measured
**clinical relevance:** LOW
**Claim links:** none
**Role:** **Count once (INFERENZA).** One homozygous `p.Leu239Arg` female child of a consanguineous family, seizures from two weeks of age, reached through a cerebral-palsy referral stream; **identity with [[paper_registry_current#PAPER 013]] case 50 is not excluded** — neither source prints enough (syndrome, EEG, onset detail, family structure) to confirm or exclude it, and the standing counting rule applies. See `CC-20261004W8-A-PATIENT-OVERLAP-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0512]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 221
**Short title:** Stamouli 2026 Sci Adv — human glia-to-interneuron reprogramming; WWOX transcript peaks transiently along the trajectory
**Full title:** A distinct lineage pathway drives parvalbumin chandelier cell fate in human interneuron reprogramming
**Authors:** Stamouli CA, Degener A, Cepeda-Prado E, et al.; Rylander Ottosson D
**Year:** 2026
**Source type:** primary research — human cell reprogramming, snRNA-seq
**Journal/source:** *Sci Adv* 2026;12(1):eadv0588
**Identifier:** PMID 41477840 / PMCID PMC12757047 / DOI 10.1126/sciadv.adv0588
**Status:** processed
**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A); numbers re-measured by the integrator with `registry_records.py catalog` at `761b36909fa4` and applied unchanged (`PAPER 216` / `LIT-0508` were the ceiling).
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41477840-01`; manifest `deepdive_manifests/PMID41477840.json`; dossier `research/fulltext_dossiers/PMID41477840.md`
**Primary pathway:** P3 — interneuron / network development
**Model/species:** human — reprogramming culture, wild type, no WWOX manipulation
**Genotype/model:** wild-type; **no WWOX allele and no WWOX manipulation**
**Transferability:** none — expression along a trajectory, with no requirement test of any kind
**clinical relevance:** LOW
**Claim links:** none
**Role:** Transcript-level background datum: WWOX rises transiently along a reprogramming trajectory in wild-type human cells. **No knockdown, no rescue, no requirement test**, so it bears on no claim about WWOX function. The paper's citation of PMID 33255508 does not match that review's wording (recorded in the dossier, § 4).
**LIT link:** [[literature_tracking_log_current#LIT-0513]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 222
**Short title:** Qin 2025 J Transl Med — drug-target MR in a lymphoma; its drug list inverts its own CTD table
**Full title:** Integrative multi-omics and Mendelian randomization identify WWOX and THBS2 as potential therapeutic targets in mature T/NK-cell lymphoma
**Authors:** Qin Y, Wei J, He Y, et al.; Huang Y
**Year:** 2025
**Source type:** computational — Mendelian randomisation and docking
**Journal/source:** *J Transl Med* 2025;23(1):1306
**Identifier:** PMID 41254692 / PMCID PMC12625014 / DOI 10.1186/s12967-025-07301-9
**Status:** processed
**Record provenance:** created by `CC-20261004W8-A-REGISTRY-01` (intake wave 8 2026-10-04, Scientist A); numbers re-measured by the integrator with `registry_records.py catalog` at `761b36909fa4` and applied unchanged (`PAPER 216` / `LIT-0508` were the ceiling). Promotes [[paper_registry_current#CORPUS-STUB-101]].
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41254692-01`; manifest `deepdive_manifests/PMID41254692.json`; dossier `research/fulltext_dossiers/PMID41254692.md`
**Primary pathway:** P8 — repurposing / expression modulation
**Model/species:** none — common-variant expression instruments over blood summary statistics
**Genotype/model:** none — no WWOX allele; common-variant expression proxy
**Transferability:** none to WWOX-DEE
**clinical relevance:** LOW
**Claim links:** none
**Role:** Computational only, and **internally inconsistent on direction**: the Results name vorinostat, valproic acid, sunitinib, Jinfukang and arsenic trioxide as compounds that *«potentially increase»* WWOX expression, while the paper's own deposited CTD export (Table S7) records those WWOX rows as **`Decreases expression`**. The protein-level WWOX association does **not** survive FDR correction (FDR-corrected P = 0.160). Registered as a reading debt, never as evidence about valproate — see `DL-REPO-003` and `CC-20261004W8-A-VPA-DIRECTION-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0514]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 223
**Short title:** Makii 2020 BMC Vet Res — a pure WWOX-measurement protocol, and the ceiling of every direct WWOX read-out it uses
**Full title:** Characterization of WWOX expression and function in canine mast cell tumors and malignant mast cell lines
**Authors:** Makii R, Cook H, Louke D, Breitbach J, Jennings R, Premanandan C, et al.; Fenger JM
**Year:** 2020
**Source type:** primary research — veterinary oncology; declared a pilot study
**Journal/source:** *BMC Vet Res* 2020;16:415
**Identifier:** PMID 33129329 / PMCID PMC7603737 / DOI 10.1186/s12917-020-02638-3
**Status:** processed
**Record provenance:** created by `CC-20261004W8-B-REGISTRY-01` (intake wave 8 2026-10-04, Scientist B); the candidate specified the record in prose and the integrator authored it. The candidate's provisional `PAPER 201`-`206` / `LIT-0494`-`0499` were already taken by `BATCH_20261004_001`; re-measured at `761b36909fa4` and renumbered in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-33129329-01`; manifest `deepdive_manifests/PMID33129329.json`; dossier `research/fulltext_dossiers/PMID33129329.md`
**Primary pathway:** P9 — measurement / assay specification
**Model/species:** canine cutaneous mast cell tumour tissue; canine and murine mast cell lines
**Genotype/model:** no WWOX allele; wild-type canine and murine WWOX
**Transferability:** T4 as biology; **T1 as an assay specification and as a ceiling on it**
**clinical relevance:** MODERATE — the corpus's only end-to-end WWOX measurement protocol
**Claim links:** CLAIM 046
**Role:** 🔴 **Tier 1 modality demonstration under `LEGEND_CORE` §13; not a validated biomarker and not an endpoint.** No limit of detection, no linear range, no calibrator, no sensitivity, no specificity and no disease population anywhere in the paper. Measured reliability ceiling for the tissue read-out: weighted κ **0.264** (intensity) and **0.273** (percent positivity), two blinded boarded pathologists, which the authors themselves call *fair*. The transcript assay is relative comparative-Ct normalised to 18S and the protein assay is densitometry against β-actin, so neither reports a concentration. **WWOX enzymatic activity was not measured at all.** The functional arm is an **earned negative** for proliferation and viability. See `CC-20261004W8-B-BIOMARKER-01`.
**LIT link:** [[literature_tracking_log_current#LIT-0515]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 224
**Short title:** Carpanese 2025 J Cell Physiol — WWOX is one unquantified row of 283 in a murine KCa3.1 proxisome
**Full title:** Intermediate Conductance Calcium-Dependent Potassium Channel (KCa3.1) Interacting Proteins Using Turboid-Based Proximity Labeling Technology: Insights Into Interactome and Related Signaling Pathways in Pancreatic Tumors
**Authors:** Carpanese V, Sadeghi S, Todesca LM, Szabo I, Checchetto V
**Year:** 2025
**Source type:** primary research — proximity-labelling proteomics
**Journal/source:** *J Cell Physiol* 2025;240(9):e70092
**Identifier:** PMID 40952239 / PMCID PMC12435150 / DOI 10.1002/jcp.70092
**Status:** processed
**Record provenance:** created by `CC-20261004W8-B-REGISTRY-01` (intake wave 8 2026-10-04, Scientist B); the candidate specified the record in prose and the integrator authored it. The candidate's provisional `PAPER 201`-`206` / `LIT-0494`-`0499` were already taken by `BATCH_20261004_001`; re-measured at `761b36909fa4` and renumbered in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-40952239-01`; manifest `deepdive_manifests/PMID40952239.json`; dossier `research/fulltext_dossiers/PMID40952239.md`
**Primary pathway:** P5 — interactome / proximity annotation
**Model/species:** murine pancreatic ductal adenocarcinoma cells (KPCY)
**Genotype/model:** no WWOX allele; murine Wwox, non-excitable epithelium
**Transferability:** T5 — murine Wwox, non-excitable epithelium, unvalidated proximity hit
**clinical relevance:** LOW
**Claim links:** none
**Role:** ⚪ **Earned null for the gene at the evidence level.** WWOX's entire presence is **one row of 283** in an annotation table with **no numeric cell anywhere in the sheet**, plus two Discussion sentences. The paper's own co-immunoprecipitation arm confirmed **2 of 8** candidates tested and **WWOX was not among them**, so nothing here is an interaction result.
**LIT link:** [[literature_tracking_log_current#LIT-0516]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 225
**Short title:** Chornyy 2025 Mol Ther Methods Clin Dev — ten CNS promoters head to head; the cell-restricted one put the most protein in the liver
**Full title:** Comparative analysis of cell-specific promoters in AAV9-mediated gene therapy targeting the central nervous system
**Authors:** Chornyy S, Herstine JA, Holaway C, Biddle A, Vetter TA, et al.; Bradbury AM
**Year:** 2025
**Source type:** primary research — vector-engineering comparison
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101588
**Identifier:** PMID 41036104 / PMCID PMC12481918 / DOI 10.1016/j.omtm.2025.101588
**Status:** processed
**Record provenance:** created by `CC-20261004W8-B-REGISTRY-01` (intake wave 8 2026-10-04, Scientist B); the candidate specified the record in prose and the integrator authored it. The candidate's provisional `PAPER 201`-`206` / `LIT-0494`-`0499` were already taken by `BATCH_20261004_001`; re-measured at `761b36909fa4` and renumbered in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41036104-01`; manifest `deepdive_manifests/PMID41036104.json`; dossier `research/fulltext_dossiers/PMID41036104.md`
**Primary pathway:** P7 — gene-therapy design / promoter selection
**Model/species:** C57Bl/6 mouse, neonatal P0-P1, intracerebroventricular ssAAV9-EGFP, ten promoters
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source (an earned null for the gene)
**Transferability:** T3 for promoter ranking; T4 for absolute values
**clinical relevance:** MODERATE — promoter choice is a restoration-spec parameter
**Claim links:** CLAIM 047
**Role:** 🟡 **WWOX appears zero times; read for the promoter question.** The astrocyte-restricted `gfa1405` promoter *«[drove] the most EGFP protein in the liver»*, more than the ubiquitous CAG, while whole-organ liver fluorescence showed minimal signal — so a safety case resting on promoter restriction must measure hepatic **protein**, not fluorescence. ⚠️ **Integrator amendment (blind audit):** that ranking is scoped by the source to the western-blot subset, *«the four top-performing promoters: CAG, p546, gfa1405, and CNP»*, **not to all ten promoters tested**, and `p546` and `CNP` are cell-restricted too — so it is not «any promoter tested». The neuron-restricted `p546` matched CAG for brain-area coverage (**41 %** against CAG *«covering up to 42 %»*, a ratio of **0.98** recomputed from those two printed values) at about **one third** of the mean intensity (**154.0** against **474.8** relative fluorescence units — **0.324**), with **72 %** neuronal and **1.9 %** astrocytic colocalisation. ⚠️ A second amendment: those percentages are **S100B** colocalisation, not GFAP, cover **5 of the 7** promoters so measured, and are restricted to **cortex, hippocampus and olfactory areas**. ⚠️ Doses are **not matched across arms** (7.00-8.50 × 10¹⁰ vg per animal), though the spread is only **1.21-fold** (8.50 ÷ 7.00) — stated so the reader neither ignores it nor overweights it. See `CLAIM 047`.
**LIT link:** [[literature_tracking_log_current#LIT-0517]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 226
**Short title:** Chauhan 2026 Mol Ther — a 126 bp non-viral mini-promoter in AAV-DJ, whose ranking inverts between IT and ICV
**Full title:** Design and initial characterization of a novel mini-promoter for gene therapies targeting the central nervous system
**Authors:** Chauhan M, Daugherty AL, Khadir F, Duzenli OF, Hoffman A, et al.; Pacak CA
**Year:** 2026
**Source type:** primary research — vector-engineering comparison
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201681
**Identifier:** PMID 42137269 / PMCID PMC13148911 / DOI 10.1016/j.omta.2026.201681
**Status:** processed
**Record provenance:** created by `CC-20261004W8-B-REGISTRY-01` (intake wave 8 2026-10-04, Scientist B); the candidate specified the record in prose and the integrator authored it. The candidate's provisional `PAPER 201`-`206` / `LIT-0494`-`0499` were already taken by `BATCH_20261004_001`; re-measured at `761b36909fa4` and renumbered in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42137269-01`; manifest `deepdive_manifests/PMID42137269.json`; dossier `research/fulltext_dossiers/PMID42137269.md`
**Primary pathway:** P7 — gene-therapy design / cassette headroom
**Model/species:** FVB/NJ mouse, neonatal intravenous and adult ICV/IT; **AAV-DJ** capsid
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source
**Transferability:** T3 for the route-dependence result; **T4 for the capsid, which is not AAV9**
**clinical relevance:** MODERATE
**Claim links:** CLAIM 047
**Role:** 🟡 **WWOX appears zero times; read for cassette headroom.** A 126 bp, all-human, non-viral mini-promoter (`CP040`), *«packaged in the same AAV serotype (AAVDJ) using the same doses»* as its three comparators. 🔴 **The same promoter, in the same capsid, at the same dose, in the same strain, ranked significantly higher than CBA, EF1α and hSYN by the intrathecal route in cortex and cerebellum, and below BOTH ubiquitous promoters by the intracerebroventricular route** — **promoter and route must be specified together**. ⚠️ **Integrator amendment (blind audit):** the ICV reversal is scoped by the source to **hippocampus and hypothalamus**; in cortex `CP040` was *«equivalent to those obtained with the EF1α and hSYN promoters»* and below CBA only, and in cerebellum *«equivalent to that obtained with the CBA promoter»* and below EF1α and hSYN. It is a **route-dependent re-ranking**, not a uniform collapse, and the four-region wording would have overstated it. The capsid is AAV-DJ, **not AAV9**. See `CLAIM 047`.
**LIT link:** [[literature_tracking_log_current#LIT-0518]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 227
**Short title:** Haque 2026 Front Med — lumbar IT reaches primate brain at 1-4 vg/DG, with no expression measured anywhere
**Full title:** rAAV9 vector biodistribution in nonhuman primate brain and spinal cord following lumbar intrathecal infusion
**Authors:** Haque E, Devidze N, Nagendran S, Haque-Ahmed R, McAuliffe S, Lamontagne A, et al.; Porter F
**Year:** 2026
**Source type:** primary research — primate biodistribution, sponsor-authored
**Journal/source:** *Frontiers in Medicine* 2026;13:1819594
**Identifier:** PMID 42136830 / PMCID PMC13167494 / DOI 10.3389/fmed.2026.1819594
**Status:** processed
**Record provenance:** created by `CC-20261004W8-B-REGISTRY-01` (intake wave 8 2026-10-04, Scientist B); the candidate specified the record in prose and the integrator authored it. The candidate's provisional `PAPER 201`-`206` / `LIT-0494`-`0499` were already taken by `BATCH_20261004_001`; re-measured at `761b36909fa4` and renumbered in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42136830-01`; manifest `deepdive_manifests/PMID42136830.json`; dossier `research/fulltext_dossiers/PMID42136830.md`
**Primary pathway:** P7 — gene-therapy design / route selection
**Model/species:** cynomolgus macaque, lumbar intrathecal and intracisternal
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source
**Transferability:** T2 for route biodistribution — the only primate record in group B; **T5 for anything about expression, which is absent**
**clinical relevance:** HIGH for route selection
**Claim links:** CLAIM 047
**Role:** 🟡 **WWOX appears zero times; read for the route question.** **1-4 vg/DG** in primate brain, uniform across regions, *«at all doses ≥ 5.8 × 10¹³ vg/animal»*; cerebellum is the lowest brain region, **~2.5 × 10⁴ vg/µg (0.16 vg/DG)** against **~1.3 × 10⁵ vg/µg (0.8 vg/DG)** in prefrontal lobe — a factor of **5.0** recomputed from those two printed values. Dose scaling is **sublinear**: the paper states *«a ~2.5-fold increase»* for a four-fold input increase, and the two necropsy time points recompute to **2.60×** (day 90: 3.9 × 10⁵ ÷ 1.5 × 10⁵) and **2.16×** (day 180: 6.7 × 10⁵ ÷ 3.1 × 10⁵), so the stated figure is the mid-point of the two. ⚠️ **Integrator amendments (blind audit):** the threshold comes from *«a post-hoc analysis»* pooling brain regions, so **«only at the higher doses» is the reader's exclusivity**, not the authors' word — though it is consistent with their low-dose values of 0.02-0.27 vg/DG; and the no-expression statement is scoped to **this report** (*«Analysis was restricted to vector biodistribution, rather than gene or protein expression»*, covering **five** NHP studies), not a claim that expression is unmeasurable. 🔴 The authors **forbid** reading vg/DG as a transduced-cell fraction. Their limitations relay a canine comparison in which ICV-dosed animals developed strong and in one case fatal transgene-directed encephalitis while intracisternally dosed animals did not — ⚠️ with *«comparable biodistribution»* itself qualified: **< 1 vg/dg** in brain by both routes but about **10 vg/dg** with ICM in cervical and thoracic cord, a **~10-fold** difference — and the relevance to primates and humans *«not certain»*. See `CLAIM 047`.
**LIT link:** [[literature_tracking_log_current#LIT-0519]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 228
**Short title:** Nabakowski 2026 Cells — liver de-targeting ~127-fold, at eight-fold worse packaging and fewer brain vector genomes
**Full title:** A Rationally Designed AAV9-DM Capsid with Minimal Liver Tropism
**Authors:** Nabakowski ZC, Jaramillo IC, Tanachaiwiwat P, Keeler GD, Chen S-H
**Year:** 2026
**Source type:** primary research — capsid engineering
**Journal/source:** *Cells* 2026;15(4):334
**Identifier:** PMID 41744777 / PMCID PMC12938943 / DOI 10.3390/cells15040334
**Status:** processed
**Record provenance:** created by `CC-20261004W8-B-REGISTRY-01` (intake wave 8 2026-10-04, Scientist B); the candidate specified the record in prose and the integrator authored it. The candidate's provisional `PAPER 201`-`206` / `LIT-0494`-`0499` were already taken by `BATCH_20261004_001`; re-measured at `761b36909fa4` and renumbered in event order.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41744777-01`; manifest `deepdive_manifests/PMID41744777.json`; dossier `research/fulltext_dossiers/PMID41744777.md`
**Primary pathway:** P7 — gene-therapy design / off-target organ risk
**Model/species:** C57BL/6 mouse, intravenous tail vein, ssAAV-Fluc
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source
**Transferability:** T3 for liver de-targeting; T4 for the CNS claim
**clinical relevance:** MODERATE
**Claim links:** CLAIM 047
**Role:** 🟡 **WWOX appears zero times; read for the dose-ceiling question.** The double-mutant `AAV9-DM` cut hepatic vector genome copies **~127-fold** (the authors' own figure), but packaged **~8-fold worse** — **3.58 × 10¹³** vg for AAV9 against **4.5 × 10¹²** for AAV9-DM, a ratio of **7.96** recomputed from those two printed values — dropped peak whole-animal signal from **7.3 × 10⁷** to **5.8 × 10⁵** (a factor of **126**, i.e. about two orders of magnitude) and, by the paper's own Discussion, put **significantly fewer** vector genomes into the brain than the parent capsid. 🔴 **No toxicity endpoint of any kind**, so the dose-ceiling implication is a mechanism hypothesis, not a safety result. See `CLAIM 047`.
**LIT link:** [[literature_tracking_log_current#LIT-0520]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 229
**Short title:** Moeini 2026 Mol Ther Adv — primate liver after toxic high-dose IV AAV-SMN1: p53/DNA damage at every dose, UPR only above 5e13 vg/kg
**Full title:** DNA damage/p53, innate immune, and unfolded protein responses are activated in primate liver after toxic, high-dose AAV-SMN1 delivery
**Authors:** Moeini P, Bilbao-Arribas M, Guruceaga E, Torrens-Baile J, Lanz TA, et al.; González-Aseguinolaza G
**Year:** 2026
**Source type:** primary research — reanalysis of an existing primate and rat liver RNA-seq dataset
**Journal/source:** *Molecular Therapy Advances* 2026;34(1):201682
**Identifier:** PMID 42137263 / PMCID PMC13148890 / DOI 10.1016/j.omta.2026.201682
**Status:** processed
**Record provenance:** created by `CC-20261004w8-C-REGISTRY-01` (intake wave 8 2026-10-04, Scientist C); the candidate specified the record in a prose table and the integrator authored it. The candidate's provisional `PAPER 281`-`286` / `LIT-0581`-`0586` were a disjoint block chosen to avoid a wave collision; re-measured at `761b36909fa4` and renumbered into the next free run so both registries stay contiguous.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42137263-01`; manifest `deepdive_manifests/PMID42137263.json`; dossier `research/fulltext_dossiers/PMID42137263.md`
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** cynomolgus macaque (2 males + 2 females per dose) and male rat, liver, day 4, intravenous AAV9-PHP.B-CBh-SMN1 at 2 × 10¹³, 5 × 10¹³ and 1 × 10¹⁴ vg/kg
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source (an earned null for the gene)
**Transferability:** T3 for the pathway ordering; **T5 for anything about a CSF-delivered cassette**
**clinical relevance:** MODERATE — it is the primary behind a commentary this registry already carries
**Claim links:** none
**Role:** The **primary** behind the liver-toxicity commentary held at `RL-C-20261004w7c1`. Its ordering by dose is the increment: **DNA-damage/p53 and innate/interferon signatures appear at the lowest dose analysed and in rats showing no clinical signs**, while *«UPR activation was observed only in animals receiving doses ≥ 5 × 10¹³ vg/kg»* — and the authors add that ≥ 5 × 10¹³ is **necessary, not sufficient** (rats at high dose showed no UPR). PERK-arm genes rise with transgene level (DDIT3 r = **0.96**, CES1 r = **−0.89** across lobes and animals); ATF6 and IRE1-XBP1 are reported as *«data not shown»*. 🔴 Correlational by construction: **no expression-null and no dose-matched control arm**, dose and expression and injury are collinear, the statistical unit is the **lobe** (four per animal), and this is a **reanalysis** of a dataset generated elsewhere (accession PRJNA824450) — no new dosing. ⚠️ Integrator amendment (blind audit): the authors' own hedge on separating vector effect from disease is *«remain difficult to disentangle»*, not «cannot». See `RL-C-20261004w8c3`.
**LIT link:** [[literature_tracking_log_current#LIT-0521]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 230
**Short title:** Hordeaux 2018a Mol Ther Methods Clin Dev — rhesus ICM AAV9-hIDUA toxicology; a three-animal immunosuppression arm, single day-90 necropsy
**Full title:** Toxicology Study of Intra-Cisterna Magna Adeno-Associated Virus 9 Expressing Human Alpha-L-Iduronidase in Rhesus Macaques
**Authors:** Hordeaux J, Hinderer C, Goode T, Katz N, Buza EL, et al.; Wilson JM
**Year:** 2018
**Source type:** primary research — GLP-style primate toxicology
**Journal/source:** *Mol Ther Methods Clin Dev* 2018;10:79
**Identifier:** PMID 30073179 / PMCID PMC6070681 / DOI 10.1016/j.omtm.2018.06.003
**Status:** processed
**Record provenance:** created by `CC-20261004w8-C-REGISTRY-01` (intake wave 8 2026-10-04, Scientist C); the candidate specified the record in a prose table and the integrator authored it. The candidate's provisional `PAPER 281`-`286` / `LIT-0581`-`0586` were a disjoint block chosen to avoid a wave collision; re-measured at `761b36909fa4` and renumbered into the next free run so both registries stay contiguous.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-30073179-01`; manifest `deepdive_manifests/PMID30073179.json`; dossier `research/fulltext_dossiers/PMID30073179.md`
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** rhesus macaque, intra-cisterna magna AAV9; immunosuppressed arm of **three** animals
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source
**Transferability:** T2 for the route and the regimen; T5 for any WWOX cassette or infant regimen
**clinical relevance:** MODERATE
**Claim links:** none
**Role:** One of the **two 2018 rhesus primaries behind the immunosuppression-rebound relay** that `RL-C-20261004w7c1` carried as unread. Now read. Regimen: mycophenolate mofetil to day 60 plus rapamycin to necropsy, **one necropsy at day 90** — so a *delayed* or *rebound* DRG phenotype **cannot be observed in this study at all**. The DRG/axonopathy reduction under immunosuppression is a **trend the authors confine to the high-dose arm** (*«trended toward lower scores in the HD IS animals»*) and immediately qualify: *«it is hard to draw any definitive conclusions due to study limitations, such as cohort size»*. Degeneration was present in *«all animals except one HD IS animal»*, i.e. **2 of 3** immunosuppressed animals. ⚠️ Integrator amendments (blind audit): the *«these findings»* sentence cited for the lesion refers to the **T-cell clustering** sentence before it, not to the lesions, whose locator is Figures 3A-3G / Tables S5-S6; the regimen's **anaemia** is at a different locator and the authors state those effects *«emerged before vector dosing and were thus not related to the test article»*; and the figure's *«three animals per group»* holds for the **DRG panel only** — the axonopathy panel's high-dose group fits n = 4. See `RL-C-20261004w8c1`.
**LIT link:** [[literature_tracking_log_current#LIT-0522]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 231
**Short title:** Hordeaux 2018b Mol Ther Methods Clin Dev — companion rhesus ICM AAV9-hIDS toxicology; five-animal immunosuppression arm, no consistent ganglion reduction
**Full title:** Toxicology Study of Intra-Cisterna Magna Adeno-Associated Virus 9 Expressing Iduronate-2-Sulfatase in Rhesus Macaques
**Authors:** Hordeaux J, Hinderer C, Goode T, Buza EL, Bell P, et al.; Wilson JM
**Year:** 2018
**Source type:** primary research — GLP-style primate toxicology; companion to PMID 30073179
**Journal/source:** *Mol Ther Methods Clin Dev* 2018;10:68
**Identifier:** PMID 30073178 / PMCID PMC6070702 / DOI 10.1016/j.omtm.2018.06.004
**Status:** processed
**Record provenance:** created by `CC-20261004w8-C-REGISTRY-01` (intake wave 8 2026-10-04, Scientist C); the candidate specified the record in a prose table and the integrator authored it. The candidate's provisional `PAPER 281`-`286` / `LIT-0581`-`0586` were a disjoint block chosen to avoid a wave collision; re-measured at `761b36909fa4` and renumbered into the next free run so both registries stay contiguous.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-30073178-01`; manifest `deepdive_manifests/PMID30073178.json`; dossier `research/fulltext_dossiers/PMID30073178.md`
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** rhesus macaque, intra-cisterna magna AAV9, a **different cargo** at the same capsid, promoter, route and species; immunosuppressed arm of **five** animals
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source
**Transferability:** T2 for the route and the regimen; T5 for any WWOX cassette
**clinical relevance:** MODERATE
**Claim links:** none
**Role:** The second of the two 2018 primaries, and the **cargo swap**: same capsid, promoter, route and species, a different secreted lysosomal enzyme. Again a **single day-90 necropsy**, so no rebound is observable; a late CSF-cell peak in one low-dose immunosuppressed animal is attributed *«perhaps due to MMF withdrawal»* — a conjecture about CSF cells, **not** about DRG histology. The ganglion score is **not consistently lower** with immunosuppression and is **higher at the low dose**; the authors state *«IS did not prevent neuronal degeneration»* and that immunity is *«probably not the only explanation»*. ⚠️ Integrator amendments (blind audit): **six** animals received the regimen and one was withdrawn before dosing, so **n = 5 is the post-withdrawal number**; and Table 2 renders the antimetabolite start as *«14 to 21 days preinjection»*, not uniformly three weeks. See `RL-C-20261004w8c1`.
**LIT link:** [[literature_tracking_log_current#LIT-0523]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 232
**Short title:** Buss 2022 Mol Ther Methods Clin Dev — the expression-null DRG control: AAV9.Null reaches DRG at DNA parity and produces no neuronal degeneration
**Full title:** Characterization of AAV-mediated dorsal root ganglionopathy
**Authors:** Buss N, Lanigan L, Zeller J, Cissell D, Metea M, et al.; Fiscella M
**Year:** 2022
**Source type:** primary research — controlled primate experiment; sponsor-authored
**Journal/source:** *Mol Ther Methods Clin Dev* 2022;24:342
**Identifier:** PMID 35229008 / PMCID PMC8851102 / DOI 10.1016/j.omtm.2022.01.013
**Status:** processed
**Record provenance:** created by `CC-20261004w8-C-REGISTRY-01` (intake wave 8 2026-10-04, Scientist C); the candidate specified the record in a prose table and the integrator authored it. The candidate's provisional `PAPER 281`-`286` / `LIT-0581`-`0586` were a disjoint block chosen to avoid a wave collision; re-measured at `761b36909fa4` and renumbered into the next free run so both registries stay contiguous.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-35229008-01`; manifest `deepdive_manifests/PMID35229008.json`; dossier `research/fulltext_dossiers/PMID35229008.md`
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** cynomolgus monkey, **2 per sex per group**, single cisterna magna dose, four weeks; AAV9 with a CB7-type promoter and a secreted lysosomal-enzyme cargo
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source
**Transferability:** T2 for the discriminating design; T5 for any WWOX cassette or intracellular cargo
**clinical relevance:** HIGH strategic — it is the discriminating experiment the corpus recorded as NOT DONE
**Claim links:** none
**Role:** 🔴 **The DRG-side expression-null control.** An AAV9 *«Null»* genome *«which lacked a functional promoter and does not produce mRNA or protein»* reached brain, cord and DRG *«at similar or greater levels than those seen with AAV9.hCLN2-treated cynomolgus monkeys»* — **DNA parity** — with *«no evidence of DRG toxicity or any other treatment-related findings»*, while every expressing-vector animal had the lesion at **all three purification routes** (74.1 %, 86.3 % and 95.5 % full capsids), so *«purification process and relative amount of empty capsid are not major determinants»*. 🔴 **Three limits the record carries rather than hides.** (1) The Null arm is **not wholly clean**: the same Results paragraph reports *«a higher incidence of increased cellularity (two of four animals) in the DRG (LS only)»* against one of four vehicle animals, while opening by saying the adverse findings were not seen in the Null animals — an internal tension in the source. (2) ⚠️ Integrator amendment (blind audit, **CONTRADICTED verdict repaired at source**): the lesion is **not** confined to the high dose in every segment — thoracic and lumbar DRG degeneration is high-dose only, but in **cervical** DRG one animal of a 3.1 × 10¹³ group scores 1. The universal «only at the high dose» is **withdrawn**. (3) The authors' own conclusion is offered as *«supports a hypothesis that»* DRG toxicity *«is primarily mediated by transgene overexpression»* — a hypothesis, and expression was **never measured in DRG neurons**, so «transcription, protein or the specific cDNA» is what the data separate. Function: nerve conduction unchanged (⚠️ the assessment *«focused on sensory»*, with motor on **one** pathway); intraepidermal fibre density fell below the control range in **four animals across two of the three low-dose groups** and *«IENFD changes were not observed at the highest dose»*, with *«no relationship to dose»*; MRI only in the high-dose arm and controls. See `RL-C-20261004w8c2`.
**LIT link:** [[literature_tracking_log_current#LIT-0524]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 233
**Short title:** Fortuna 2025 Mol Ther Methods Clin Dev — AAV-PHP.eB beats AAV9 for primate cortical neurons after ICV, with no toxicity endpoint and a heavy liver load
**Full title:** AAV-PHP.eB achieves superior neuronal transduction over AAV9 in pigtail macaques following intracerebroventricular administration
**Authors:** Fortuna MG, Nyberg LH, Taskin N, Hunker A, Weed N, et al.; Ting JT
**Year:** 2025
**Source type:** primary research — capsid comparison in primate
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(4):101636
**Identifier:** PMID 41438872 / PMCID PMC12721033 / DOI 10.1016/j.omtm.2025.101636
**Status:** processed
**Record provenance:** created by `CC-20261004w8-C-REGISTRY-01` (intake wave 8 2026-10-04, Scientist C); the candidate specified the record in a prose table and the integrator authored it. The candidate's provisional `PAPER 281`-`286` / `LIT-0581`-`0586` were a disjoint block chosen to avoid a wave collision; re-measured at `761b36909fa4` and renumbered into the next free run so both registries stay contiguous.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-41438872-01`; manifest `deepdive_manifests/PMID41438872.json`; dossier `research/fulltext_dossiers/PMID41438872.md`
**Primary pathway:** P7 — gene-therapy design / capsid and route selection
**Model/species:** juvenile male pigtail macaque (*Macaca nemestrina*), **n = 3 per capsid**, unilateral intracerebroventricular 4 × 10¹³ vg/kg, necropsy at six weeks; nuclear reporter under a neuronal promoter
**Genotype/model:** no WWOX allele; WWOX occurs **zero times** in this source
**Transferability:** T2 for the capsid comparison after ICV; **T5 for any dose-ceiling or safety inference**
**clinical relevance:** MODERATE
**Claim links:** none
**Role:** A capsid-versus-capsid transduction comparison after ICV. 🔴 **It measures no toxicity endpoint**: no DRG examination, no liver enzymes (the authors' own stated limitation), only necropsy histology, which found *«no vector-related macroscopic or microscopic findings»*. So the idea that a more efficient capsid lowers the dose and shrinks the dose-driven harm **is not testable from this source** — there is no dose titration and no toxicity read-out. What it does add on the boundary side: after ICV, **liver vector genomes were about 100-250 per diploid genome in both capsid groups, about 100-fold heart, kidney or muscle, with no capsid difference** — a CSF route is not a systemic sparing route. The rodent receptor mechanism for PHP.eB is **absent in primates** (the authors' own statement). See `RL-C-20261004w8c3`.
**LIT link:** [[literature_tracking_log_current#LIT-0525]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 234
**Short title:** Boespflug-Tanguy 2026 Mol Ther — a fatal human high-dose systemic AAV9 case under prednisolone plus sirolimus; complement, not adaptive immunity
**Full title:** Death following high-dose AAV9 gene therapy in a patient with advanced SMA-PME
**Authors:** Boespflug-Tanguy O, Valent A, Rambaud J, Léger P-L, Plu I, et al.; Perret G
**Year:** 2026
**Source type:** primary research — single fatal case report, compassionate use
**Journal/source:** *Molecular Therapy* 2026;34(8):4442
**Identifier:** PMID 42198847 / PMCID PMC13464153 / DOI 10.1016/j.ymthe.2026.05.016
**Status:** processed
**Record provenance:** created by `CC-20261004w8-C-REGISTRY-01` (intake wave 8 2026-10-04, Scientist C); the candidate specified the record in a prose table and the integrator authored it. The candidate's provisional `PAPER 281`-`286` / `LIT-0581`-`0586` were a disjoint block chosen to avoid a wave collision; re-measured at `761b36909fa4` and renumbered into the next free run so both registries stay contiguous.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42198847-01`; manifest `deepdive_manifests/PMID42198847.json`; dossier `research/fulltext_dossiers/PMID42198847.md`
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** human — one patient, intravenous AAV9 at 2.2 × 10¹⁴ vg/kg under prednisolone plus sirolimus
**Genotype/model:** no WWOX allele; a different disease and a different gene
**Transferability:** T3 as a **class-level dose boundary** for high-dose systemic AAV9; **T5 for anything quantitative** — one patient, one dose, no counterfactual
**clinical relevance:** HIGH as a safety boundary — **not** as a dose-risk function
**Claim links:** none
**Role:** 🔴 **The human boundary, carried at class level.** A fatal course after high-dose **intravenous** AAV9 in advanced disease, under an immunosuppression regimen begun before dosing: no anti-AAV9 neutralising antibodies at screening but a low total anti-capsid IgG retrospectively (titre 1:157 at day −1), then fever and raised D-dimer and liver enzymes, **complement activation (soluble C5b-9 above 1,650 against a normal below 300)**, circulatory collapse, and death on day 8. Autopsy: acute circulatory failure, **no** myocarditis and **no** thrombotic microangiopathy. Biodistribution (figure panel, read at native resolution): **7,704** vector copies per diploid genome in liver against **14** in cerebellum and **128** in cortex — the authors' own text states a *«16- to 550-fold decrease»* CNS against liver. **What it adds:** the authors state sirolimus *«did not appear to mitigate early immune response in this patient»*, consistent with an adaptive-immunity drug acting on an innate and complement-mediated process. **What it cannot give:** a dose-risk function, a counterfactual, or separation of vector effect from the disease's own inflammation — the authors' words are that these *«remain difficult to disentangle»*. ⚠️ The cytokine evidence for a pre-existing inflammatory state is a **retrospective** multiplex analysis in **one** patient. See `RL-C-20261004w8c3`.
**LIT link:** [[literature_tracking_log_current#LIT-0526]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.
## PAPER 235
**Short title:** Krug 2013 Arch Toxicol — hESC-derived test systems for developmental neurotoxicity, a transcriptomics approach; the platform behind a curated valproate row
**Full title:** Human embryonic stem cell-derived test systems for developmental neurotoxicity: a transcriptomics approach
**Authors:** Krug AK, Kolde R, Gaspar JA, Rempel E, Balmer NV, Meganathan K, Vojnits K, Baquié M, Waldmann T, Ensenat-Waser R, et al.; Sachinidis A (38 authors)
**Year:** 2013
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2013;87(1):123-143
**Identifier:** PMID 23179753 / PMCID PMC3535399 / DOI 10.1007/s00204-012-0967-3
**Status:** processed
**Record provenance:** created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9 2026-10-04, Scientist B); the candidate specified the record in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`222` / `LIT-0509`-`0514` collided with records already landed by `BATCH_20261004_001`/`_002`; re-measured at `a405efc30550` (`PAPER` max 234, `LIT` max 0526) and renumbered into the next free contiguous run.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-23179753-01`; manifest `deepdive_manifests/PMID23179753.json`; dossier `research/fulltext_dossiers/PMID23179753.md`
**Primary pathway:** none — toxicogenomics background; no WWOX pathway is implicated
**Model/species:** human embryonic stem cells (H9), five differentiation systems
**Genotype/model:** no WWOX allele; **WWOX is not mentioned in the running text** (probe-set rows in supplementary tables only)
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** Platform paper behind the curated valproate row of PMID 41254692 Table S7. 🔴 **WWOX occurs zero times in the running text**; it exists only as probe-set rows in the supplementary lists, where (ratio above 1 = up, per the legend) **five WWOX probe-set rows are up with valproate, 1.47 to 2.12, adjusted p 0.0023 to 0.037**, in two neural-lineage systems at 1.05 to 2 mM. Carries the embryoid-body value (2.12) that recurs in `PAPER 238`, so the two are **not independent replications**. See `DL-REPO-003`.
**LIT link:** [[literature_tracking_log_current#LIT-0527]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
## PAPER 236
**Short title:** Balmer 2014 Arch Toxicol — transient transcriptome responses to disturbed neurodevelopment: histone acetylation and methylation as a reversible/irreversible switch
**Full title:** From transient transcriptome responses to disturbed neurodevelopment: role of histone acetylation and methylation as epigenetic switch between reversible and irreversible drug effects
**Authors:** Balmer NV, Klima S, Rempel E, Ivanova VN, Kolde R, Weng MK, Meganathan K, Henry M, Sachinidis A, Berthold MR, Hengstler JG, Rahnenführer J, Waldmann T, Leist M
**Year:** 2014
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2014;88(7):1451-1468
**Identifier:** PMID 24935251 / PMCID PMC4067541 / DOI 10.1007/s00204-014-1279-6
**Status:** processed
**Record provenance:** created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9 2026-10-04, Scientist B); the candidate specified the record in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`222` / `LIT-0509`-`0514` collided with records already landed by `BATCH_20261004_001`/`_002`; re-measured at `a405efc30550` (`PAPER` max 234, `LIT` max 0526) and renumbered into the next free contiguous run.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-24935251-01`; manifest `deepdive_manifests/PMID24935251.json`; dossier `research/fulltext_dossiers/PMID24935251.md`
**Primary pathway:** none — toxicogenomics background; no WWOX pathway is implicated
**Model/species:** human embryonic stem cells (H9) to neuroepithelial precursors
**Genotype/model:** no WWOX allele; **WWOX is not mentioned in the running text** (probe-set rows in supplementary tables only)
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** HDAC-inhibitor time course. 🔴 **WWOX occurs zero times in the running text.** In the supplementary tables **one WWOX probe set is up (1.574, adjusted p 0.042) at 600 µM valproate for 4 days**. ⚠️ The only **down** WWOX row in the four valproate primaries (ratio 0.59, Table S1, 6 h) is in this paper and is an **untreated developmental change** against undifferentiated hESC, **not a drug effect** — the single most mistakable row in the set. See `DL-REPO-003`.
**LIT link:** [[literature_tracking_log_current#LIT-0528]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
## PAPER 237
**Short title:** Rempel 2015 Arch Toxicol — a transcriptome-based classifier for developmental toxicants, optimised for HDAC inhibitors
**Full title:** A transcriptome-based classifier to identify developmental toxicants by stem cell testing: design, validation and optimization for histone deacetylase inhibitors
**Authors:** Rempel E, Hoelting L, Waldmann T, Balmer NV, Schildknecht S, Grinberg M, Das Gaspar JA, Shinde V, Stöber R, Marchan R, et al.; Leist M (18 authors)
**Year:** 2015
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2015;89(9):1599-1618
**Identifier:** PMID 26272509 / PMCID PMC4551554 / DOI 10.1007/s00204-015-1573-y
**Status:** processed
**Record provenance:** created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9 2026-10-04, Scientist B); the candidate specified the record in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`222` / `LIT-0509`-`0514` collided with records already landed by `BATCH_20261004_001`/`_002`; re-measured at `a405efc30550` (`PAPER` max 234, `LIT` max 0526) and renumbered into the next free contiguous run.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-26272509-01`; manifest `deepdive_manifests/PMID26272509.json`; dossier `research/fulltext_dossiers/PMID26272509.md`
**Primary pathway:** none — toxicogenomics background; no WWOX pathway is implicated
**Model/species:** human embryonic stem cells (H9), neural induction; 12 compounds
**Genotype/model:** no WWOX allele; **WWOX is not mentioned in the running text** (probe-set rows in supplementary tables only)
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** Genome-wide supplementary table. 🔴 **WWOX occurs zero times in the running text.** **Three of five WWOX probe sets are up with valproate (1.33 to 1.68; adjusted p 0.007 to 0.027) at 600 µM for 6 days.** ⚠️ The table's own legend is ambiguous on sign; the direction was fixed by the **PAX6 and OTX2 sentinels** in the same block — `INFERENZA`, and recorded as such. Shares the neural-induction measurement with `PAPER 238` (identical 1.68 for the same probe), so they are **one measurement, not two**. See `DL-REPO-003`.
**LIT link:** [[literature_tracking_log_current#LIT-0529]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
## PAPER 238
**Short title:** Shinde 2017 Arch Toxicol — transcriptome-based developmental indices (STOP-Toxukn / STOP-Toxukk); signed fold changes put WWOX up with valproate in both systems
**Full title:** Definition of transcriptome-based indices for quantitative characterization of chemically disturbed stem cell development: introduction of the STOP-Toxukn and STOP-Toxukk tests
**Authors:** Shinde V, Hoelting L, Srinivasan SP, Meisig J, Meganathan K, Jagtap S, Grinberg M, Liebing J, Bluethgen N, Rahnenführer J, et al.; Sachinidis A (22 authors)
**Year:** 2017
**Source type:** primary research
**Journal/source:** *Archives of Toxicology* 2017;91(2):839-864
**Identifier:** PMID 27188386 / PMCID PMC5306084 / DOI 10.1007/s00204-016-1741-8
**Status:** processed
**Record provenance:** created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9 2026-10-04, Scientist B); the candidate specified the record in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`222` / `LIT-0509`-`0514` collided with records already landed by `BATCH_20261004_001`/`_002`; re-measured at `a405efc30550` (`PAPER` max 234, `LIT` max 0526) and renumbered into the next free contiguous run.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-27188386-01`; manifest `deepdive_manifests/PMID27188386.json`; dossier `research/fulltext_dossiers/PMID27188386.md`
**Primary pathway:** none — toxicogenomics background; no WWOX pathway is implicated
**Model/species:** human pluripotent stem cells (H9), two differentiation systems
**Genotype/model:** no WWOX allele; **WWOX is not mentioned in the running text** (probe-set rows in supplementary tables only)
**Transferability:** T3 — transferable platform lesson only
**clinical relevance:** BACKGROUND — transferable lesson only, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** Signed-fold supplementary table, the only one of the four whose sign needs no inference. 🔴 **WWOX occurs zero times in the running text.** **WWOX is up with valproate in both systems: +2.127 in embryoid bodies and +1.683 in neural induction**; Table 7 lists the probe set at 1000 µM **without direction**. ⚠️ Its values **recur** from `PAPER 235` (2.13 against 2.12) and `PAPER 237` (1.68), so the four primaries are **not four replications**. The print year is **2017** although the e-publication is 2016. See `DL-REPO-003`.
**LIT link:** [[literature_tracking_log_current#LIT-0530]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
## PAPER 239
**Short title:** Bey 2020 Mol Ther Methods Clin Dev — intra-CSF AAV9 and AAVrh10 in nonhuman primates under triple immunosuppression; a descriptive DRG baseline, no grade table
**Full title:** Intra-CSF AAV9 and AAVrh10 Administration in Nonhuman Primates: Promising Routes and Vectors for Which Neurological Diseases?
**Authors:** Bey K, Deniaud J, Dubreil L, Joussemet B, Cristini J, Ciron C, Hordeaux J, Le Boulc'h M, Marche K, Maquigneau M, et al.; Colle M-A (22 authors)
**Year:** 2020
**Source type:** primary research
**Journal/source:** *Molecular Therapy. Methods & Clinical Development* 2020;17:771-784
**Identifier:** PMID 32355866 / PMCID PMC7184633 / DOI 10.1016/j.omtm.2020.04.001
**Status:** processed
**Record provenance:** created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9 2026-10-04, Scientist B); the candidate specified the record in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`222` / `LIT-0509`-`0514` collided with records already landed by `BATCH_20261004_001`/`_002`; re-measured at `a405efc30550` (`PAPER` max 234, `LIT` max 0526) and renumbered into the next free contiguous run.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-32355866-01`; manifest `deepdive_manifests/PMID32355866.json`; dossier `research/fulltext_dossiers/PMID32355866.md`
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** cynomolgus macaque (n = 8), GFP reporter; lumbar intrathecal and intracerebroventricular
**Genotype/model:** no WWOX allele; a GFP reporter cassette. **WWOX occurs zero times in the source.**
**Transferability:** T3 as a **class-level route-and-regimen baseline**; **T5 for anything quantitative** — no unmedicated arm, no grade table
**clinical relevance:** BACKGROUND — safety context for a CSF route, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** 🔴 **First author is Bey, not Hordeaux.** The wave-9 selection record labelled this paper «Hordeaux 2020»; measured on the restored JATS front matter the first author is **Bey (Karim)**, the senior authors are Moullier and Colle, and **Hordeaux J is author 7 of 22** — a different group from `PAPER 240`. No held record carried the wrong label; the correction is carried here. **WWOX occurs zero times.** Content: a **descriptive** DRG baseline under sirolimus, prednisolone and mycophenolate in all eight animals — mild-to-moderate mononuclear infiltration in DRG or DRG fibres in all six lumbar-intrathecal animals by the text, six representative panels, **no grade table**, brain clean, three weeks. **Bounds itself:** no unmedicated arm, so the regimen is not shown to have suppressed anything, and nothing here speaks to neuronal degeneration. One cited reference (a 2010 SMA paper retracted in 2022) is a **citation-only** dependency in the Introduction; no datum depends on it. See `RL-C-20261004w9b`.
**LIT link:** [[literature_tracking_log_current#LIT-0531]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
## PAPER 240
**Short title:** Hordeaux 2022 Hum Gene Ther — a graded GLP ICM dose-response without immunosuppression: DRG neuronal degeneration at most grade 1, dorsal axonopathy dose dependent to grade 3
**Full title:** Efficacy and Safety of a Krabbe Disease Gene Therapy
**Authors:** Hordeaux J, Jeffrey BA, Jian J, Choudhury GR, Michalson K, Mitchell TW, Buza EL, Chichester J, Dyer C, Bagel J, Vite CH, Bradbury AM, Wilson JM
**Year:** 2022
**Source type:** primary research
**Journal/source:** *Human Gene Therapy* 2022;33(9-10):499-517
**Identifier:** PMID 35333110 / PMCID PMC9142772 / DOI 10.1089/hum.2021.245
**Status:** processed
**Record provenance:** created by `CC-20261004W9-B-REGISTRY-01` (intake wave 9 2026-10-04, Scientist B); the candidate specified the record in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`222` / `LIT-0509`-`0514` collided with records already landed by `BATCH_20261004_001`/`_002`; re-measured at `a405efc30550` (`PAPER` max 234, `LIT` max 0526) and renumbered into the next free contiguous run.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-35333110-01`; manifest `deepdive_manifests/PMID35333110.json`; dossier `research/fulltext_dossiers/PMID35333110.md`
**Primary pathway:** P7 — gene-therapy design / BLOCK-1 safety
**Model/species:** Twitcher mouse, Krabbe dog, juvenile rhesus macaque (GLP); intracisterna magna
**Genotype/model:** no WWOX allele; a secreted lysosomal-enzyme cassette. **WWOX occurs zero times in the source.**
**Transferability:** T3 as a **class-level graded dose-response without immunosuppression**; **T5 for dose transfer** — different capsid, promoter, cargo and units
**clinical relevance:** BACKGROUND — safety context for a CSF route, not evidence
**Claim links:** none — no canonical claim is touched
**Role:** The **no-immunosuppression graded arm** the held DRG record lacked: 4.5E12, 1.5E13 and 4.5E13 GC per animal (5.0E10 to 5.0E11 GC/g brain), 3 and 6 months, **secreted-enzyme cargo**. **DRG neuronal degeneration never exceeds grade 1 at any dose** (group means about 0 / 0.1 / 0.35 / 0.5, Figure 5C read as an image), while a **secondary dorsal-column axonopathy is dose dependent and reaches grade 3 at the top dose** — ⚠️ a lesion the paper's own *«minimal to mild»* **understates**. Incidence and severity similar at days 90 and 180 (no progression over six months), which bounds a rebound claim **only** for the no-immunosuppression condition. Dogs treated ICM at 3.0E13 GC (n = 4) showed **no** DRG finding with a **canine** transgene, and the authors call the dog less sensitive than the primate. **Cargo limit:** GALC is secreted and cross-corrects, and anti-transgene antibodies and T cells were frequent (14 of 18 T-cell responses) — a WWOX cassette is an **intracellular** protein transgene, so the cross-correction does not carry to it. **WWOX occurs zero times.** See `RL-C-20261004w9b`.
**LIT link:** [[literature_tracking_log_current#LIT-0532]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
## PAPER 241
**Short title:** Henry 2025 Epilepsia — clinical genome sequencing in 733 children with epilepsy; four WWOX diagnoses and the only measured RNA consequence of a deep intronic WWOX allele
**Full title:** Clinical whole genome sequencing in pediatric epilepsy: Genetic and phenotypic spectrum of 733 individuals
**Authors:** Henry OJ, Ygberg S, Barbaro M, Lesko N, Karlsson L, Peña-Pérez L, Båvner A, Töhönen V, Lindstrand A, Stödberg T, Wedell A
**Year:** 2025
**Source type:** primary research — diagnostic cohort
**Journal/source:** *Epilepsia* 2025;66(8):2966-2979
**Identifier:** PMID 40183601 / PMCID PMC12371643 / DOI 10.1111/epi.18403
**Status:** processed
**Record provenance:** created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9 2026-10-04, Scientist C); the candidate specified the landing in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`219` / `LIT-0509`-`0511` collided with group B's block and with records already landed; re-measured at `a405efc30550` and renumbered into the next free contiguous run.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-40183601-01`; manifest `deepdive_manifests/PMID40183601.json`; dossier `research/fulltext_dossiers/PMID40183601.md`
**Primary pathway:** P1 — allele consequence; splice mechanism
**Model/species:** human — a paediatric epilepsy cohort (733 individuals from 710 families by the body; the abstract says «733 families»)
**Genotype/model:** WWOX, four diagnosed individuals, class level; one of the four is the deep intronic allele `NM_016373.4:c.107+119C>G`, homozygous
**Transferability:** T2 for the allele's **qualitative** RNA consequence; **T5 for anything quantitative** — no read fraction, frame position, NMD, protein or tissue is printed
**clinical relevance:** BACKGROUND — class-level allele mechanics. Not medical advice.
**Claim links:** none — no canonical claim is created or narrowed by this record
**Role:** 🔴 **The only source in the read literature that measured an RNA consequence for a deep intronic WWOX allele.** cDNA analysis showed **inclusion of the first intron in NM_016373 with a premature stop codon** for a homozygous `c.107+119C>G`. ⚠️ **The measurement is qualitative only:** no aberrant read fraction, no residual-normal-splicing figure, no frame position, no NMD test, no protein, no tissue — the paper's own SCN8A deep-intronic sentence names a tissue and the WWOX sentence does not. Counts, as printed: **WWOX (4)** of the **51/132 (38.6%)** solved infantile epileptic spasms cases, per individual; the other three WWOX rows are a nonsense and a missense allele. A blind locator audit (2026-10-04) confirmed every quote verbatim and confirmed that **no quantitative measure is printed**. See `RL-C-20261004w9c1` and `FT-194`.
**LIT link:** [[literature_tracking_log_current#LIT-0533]]
**Note:** class-level record; no individual-level detail and no parent-of-origin detail is carried in this public edition. Not medical advice.

---
## PAPER 242
**Short title:** Tang 2026 Cells — WWOX protein measured in L1CAM-captured plasma neuronal-enriched vesicles: relative NPX, singlet, one marked within-sex comparison
**Full title:** Use of Neuronal-Enriched Extracellular Vesicles to Distinguish Cognitive Impairment Levels and Sex Differences in People with HIV
**Authors:** Tang N, Xia F, Freasier H, Tien PC, Glesby MJ, Merenstein D, French AL, McKay H, Diaz MM, Ofotokun I, et al.; Pulliam L (18 authors)
**Year:** 2026
**Source type:** primary research — cross-sectional cohort, multiplex proteomics
**Journal/source:** *Cells* 2026;15(17):1581
**Identifier:** PMID 42738875 / PMCID PMC13565498 / DOI 10.3390/cells15171581
**Status:** processed
**Record provenance:** created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9 2026-10-04, Scientist C); the candidate specified the landing in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`219` / `LIT-0509`-`0511` collided with group B's block and with records already landed; re-measured at `a405efc30550` and renumbered into the next free contiguous run. The journal's Academic Editor appears in the JATS `editor` contrib-group and is **not** listed as an author here.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42738875-01`; manifest `deepdive_manifests/PMID42738875.json`; dossier `research/fulltext_dossiers/PMID42738875.md`
**Primary pathway:** biomarker / endpoint interface (LEGEND_CORE § 13)
**Model/species:** human plasma — L1CAM-immunocaptured extracellular vesicle lysates; adults with HIV and cognitive-impairment groups
**Genotype/model:** **no WWOX genotype**; WWOX is one analyte of a multiplex panel in a non-WWOX disease population
**Transferability:** T3 as a **measurement route**; **T5 as an endpoint** — relative unit, singlet assay, cross-sectional, no WWOX disease population
**clinical relevance:** BACKGROUND — a measurement route, **not** an endpoint and **not** validated. Not medical advice.
**Claim links:** none — no canonical claim is created or narrowed by this record
**Role:** 🔴 **The first blood-accessible, neuron-attributed WWOX protein measurement the model holds** — everything else it holds is tissue, cell line or post-mortem. **§ 13: Tier 1 by kind** (the readout is WWOX protein itself), and **NOT «validated»**: no sensitivity and no specificity are printed for WWOX or for any marker, in any population, and the authors state the study *«was not designed to provide confirmatory evidence for any single biomarker»*. Two bounds measured on the artefact: the unit is **NPX**, a log2 relative unit, and the authors deliberately did not use the assay's quantitative values because some were below detection; and **the text's WWOX sex statement is not the comparison the figure marks** — the sexes-combined WWOX panel carries **no significance bracket at all** and the single bracket is between **two male groups**. The assay was run **in singlet** while the study's other platform was run in duplicate. ⚠️ «Neuronal enrichment» is an **immunocapture operation on L1CAM**, not demonstrated neuronal origin. A blind locator audit (2026-10-04) confirmed all six quotes verbatim, confirmed the figure attestation on the rendered panel, and found no printed sensitivity or specificity. See `RL-C-20261004w9c2`.
**LIT link:** [[literature_tracking_log_current#LIT-0534]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
## PAPER 243
**Short title:** Lima 2026 eLife — PRMT1-SFPQ intron retention in craniofacial development; Wwox named among the long retained-intron genes, with retention marked and abundance not
**Full title:** PRMT1-SFPQ regulates intron retention to control matrix gene expression during craniofacial development
**Authors:** Lima JR, Ungvijanpunya N, Chen Q, Pham HQH, Rosen T, Park G, Vantankhah M, Yen S, Chai Y, Merrill AE, Liu Z, Chen JF, Yang Y, Peng W, Xu J
**Year:** 2026
**Source type:** primary research — developmental biology, transcriptomics
**Journal/source:** *eLife* 2026;13:RP101386
**Identifier:** PMID 42770556 / PMCID PMC13597084 / DOI 10.7554/eLife.101386
**Status:** processed
**Record provenance:** created by `CC-20261004W9-C-REGISTRY-01` (intake wave 9 2026-10-04, Scientist C); the candidate specified the landing in a prose table and the integrator authored the identity fields from the artefact's own JATS front matter. The candidate's provisional `PAPER 217`-`219` / `LIT-0509`-`0511` collided with group B's block and with records already landed; re-measured at `a405efc30550` and renumbered into the next free contiguous run. Two JATS `editor` contribs (a Reviewing Editor and a Senior Editor) are **not** listed as authors here.
**Evidence depth:** `partial_fulltext_read` (**partial full text**) — receipt `FTR-20261004-42770556-01`; manifest `deepdive_manifests/PMID42770556.json`. ⚠️ **No dossier was written:** the write was halted by a model safety classifier; the halt is recorded in the receipt and in the wave note, and the reading is carried by the manifest and by `RL-C-20261004w9c3`.
**Primary pathway:** transcript-level WWOX dose regulation
**Model/species:** mouse — cranial neural crest cells and a stromal cell line; 50% knockdown, not loss
**Genotype/model:** no WWOX allele; mouse *Wwox* is named as one gene in a length-dependent intron-retention set
**Transferability:** T3 for the **existence** of a *trans*-acting mechanism; **T5** for a dose-restoration lever, neuronal relevance or any protein effect
**clinical relevance:** BACKGROUND — mechanism candidate only. Not medical advice.
**Claim links:** none — no canonical claim is created or narrowed by this record
**Role:** 🔴 **The first *trans*-acting candidate regulator of WWOX transcript level the model holds.** Loss of PRMT1 or knockdown of SFPQ raises intron retention in long genes with long introns and the retained-intron transcripts are degraded by NMD; **Wwox is named as one of those genes** (913 kb, 639 kb retained intron), with increased retention of introns 3 and 4 and decreased expression on either perturbation stated in the Discussion. ⚠️ Three qualifications measured on the panels: the **abundance fall is not marked for Wwox** (retention bars carry stars, TPM bars carry none, and Wwox TPM sits within a few TPM of zero on a 0-400 axis) — the caption's «decreased mRNA abundance» is about the **gene set**; the **retained fraction is about 0.8% in control and 1.2-1.4% after knockdown**, so `INFERENZA` NMD of every retaining molecule would remove about half a percent of the pool, too little to explain a dose change by that route alone; and **no Wwox-specific experiment exists** (no RT-PCR, qPCR, NMD-inhibitor arm or CLIP peak; the SFPQ binding data are a reanalysis of embryonic **brain** CLIP-seq). 🔴 **A citation that does not support its sentence:** the Discussion links the Wwox observation to human WWOX epileptic encephalopathy with large intronic deletions and cites a pan-cancer intron-retention paper whose full text contains **zero** occurrences of «WWOX», «epileptic» or «encephalopathy». **Internal inconsistency, recorded not reconciled:** the Results name a single 639 kb retained intron and the Discussion names introns 3 and 4, with no coordinates. Any intron number this source does not print is a **derivation** and must carry `INFERENZA`. See `RL-C-20261004w9c3`.
**LIT link:** [[literature_tracking_log_current#LIT-0535]]
**Note:** class-level record. Not medical advice.

---
## PAPER 244
**Short title:** WWOX oxidoreductase — substrate and enzymatic characterization
**Full title:** WWOX Oxidoreductase – Substrate and Enzymatic Characterization
**Authors:** Sałuda-Gorgul A, Seta K, Nowakowska M, Bednarek AK (the first three are marked as having contributed equally; Bednarek is the author for correspondence, in the Department of Molecular Cancerogenesis, while the first author is in the Department of Analytical Chemistry — two departments of the same university)
**Year:** 2011
**Source type:** Article (peer-reviewed)
**Journal/source:** *Z Naturforsch C J Biosci* 2011;66c:73–82 (the article's own citation line prints `Z. Naturforsch. 66 c, 73 – 82 (2011)` and **no issue number**; the `(1–2)` carried elsewhere is PubMed's, not the artefact's)
**Identifier:** PMID 21476439 / DOI 10.1515/znc-2011-1-210 — ⚠️ the DOI is a publisher assignment that resolves to the article; the article's own front matter prints **no DOI at all** (verified on a 300-dpi render of page 1 by a blind audit, 2026-10-04)
**Status:** processed
**Record provenance:** created 2026-10-04 by `BATCH_20261004_004` from `CC-20261004W10-X-REGISTRY-01` (intake wave 10, Scientist X); promotes [[paper_registry_current#CORPUS P306]], which is kept as history. Number measured with `registry_records.py catalog` at `ce4aa9cc4f52` (highest `PAPER` 243).
**Evidence depth:** complete_fulltext_read — receipt `FTR-20261004-21476439-01`; manifest `disease-models/wwox/research/deepdive_manifests/PMID21476439.json` (PASS, 0 gaps, 17 verbatim locators); dossier `disease-models/wwox/research/fulltext_dossiers/PMID21476439.md`. Blind locator audit 2026-10-04 over 17 triples: 15 SUPPORTED, 2 NOT_SUPPORTED_AS_LABELLED (both repaired in this record before it landed), 0 UNVERIFIABLE.
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** none — human WWOX cDNA expressed in *E. coli*; no human cell, no mammalian cell, no tissue, no animal
**Genotype/model:** **wild-type human WWOX only.** No variant of any kind was made or tested. The insert is a WWOX cDNA **fragment** excised with BamHI and EcoRI and subcloned into pET 44a(+) (NusA fusion) and into pGEX 2TK (GST fusion); the paper does not print the insert's boundaries and describes no SDR-domain-only, WW-deleted or active-site-mutant construct, so *"full-length"* is a DERIVATION (`PREMISE: INFERENZA`) and *"the SDR domain has dehydrogenase activity"* is an attribution rather than a measurement on the domain.
**Transferability:** NONE to any allele. The paper contains no missense, splice or truncating allele and no patient-derived material; P47T, Q230P, G372R, A141T and P252A are each a distinct allele and none was tested. A wild-type reference property only.
**clinical relevance:** LOW for the disease model; HIGH as the corpus's only enzymology primary (`PREMISE: INFERENZA` — a statement about the corpus read here, not about the literature).
**Claim links:** none. The reading supports no canonical claim, and no claim was created or moved by it.
**What it measured:** oxidation of seven steroids (5α-androstane-3,17-dione, 4-androstene-3,17-dione, 17β-estradiol, estrone, 5α-dihydroprogesterone-allo, progesterone, testosterone) followed as NAD(P)H formation at 340 nm, in the **soluble fraction of an unfractionated *E. coli* crude extract** containing a NusA-WWOX or GST-WWOX fusion; apparent Km values in Table II, whose footnote states they are the **difference between the NUS-WWOX and NUS extracts**.
**What it did NOT measure:** no purified enzyme — activity was lost in *any attempt of purification to near-homogeneity*, in both expression systems; no Vmax, kcat, specific activity or enzyme unit, although the Methods promise a Vmax from Lineweaver-Burk fitting; no identification of any reaction product by any method; no Western blot, antibody or mass-spectrometric confirmation, and no molecular-weight marker lane or size annotation in either SDS-PAGE panel; no reduction panel (reported as *"results not shown"*, over the same seven steroids, with the added statement that reduction was *similar* in both extracts).
**Quantitative boundaries re-derived from the printed tables (DERIVATION, `PREMISE: INFERENZA`):** 13 of the 14 Km values lie **below the lowest substrate concentration Table I used** — the single exception is testosterone with NADP⁺ — so almost every Km is a double-reciprocal extrapolation from the saturated arm; and all 14 printed Mann-Whitney p values (0.0000–0.0091) lie below the smallest p attainable from an exact test at the stated n of *at least two or three*.
**Over-inference risk:** HIGH. The record most likely to be mis-carried as *"WWOX enzymology is characterised"*. It is an activity report on a crude lysate, not an assay, and it supports no allele-level or neural statement.
**Independence:** NOT independent of the gene's discovery — the author for correspondence is first author of the WWOX discovery paper (PMID 10786676) and the cDNA came from his own collection. ⚠️ **One attribution is weaker than earlier drafts of this record said:** the sentence identifying the `GANSGIG` (131–137) and `YNRSK` (293–297) motifs carries **no citation of its own**; the discovery-paper citation sits two sentences later, on a different statement about a serine residue. The motif annotation is presented as this paper's own sequence analysis (blind audit 2026-10-04, NOT_SUPPORTED_AS_LABELLED), and the reading debt on PMID 10786676 stands on the generic SDR interpretation rather than on a citation for these coordinates.
**LIT link:** [[literature_tracking_log_current#LIT-0306]]
**Note:** See `CC-20261004W10-X-ENZYMOLOGY-01` for the four landed statements this reading confirms and the four it corrects. Class-level record; no individual-level detail is carried in this public edition. Not medical advice.

---
