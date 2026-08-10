# FULL TEXT QUEUE — Legend
**Version:** v1.0
**Date baseline:** 2026-04-10
**Status:** bootstrap-created

---

## Scope
Queue of priority full texts to retrieve or deep-dive to consolidate the operational dataset.

**Ogni voce dichiara un identificatore risolvibile.** `**Paper:**` / `**Papers:**` apre con un PMID o un DOI — o con `NOT_AN_ARTICLE` per l'unica voce che non è un articolo e non lo sarà mai. Il `LINT` lo verifica (`QUEUE_ENTRY_WITHOUT_IDENTIFIER`, `QUEUE_ENTRY_IDENTIFIER_NOT_LEADING`) come verifica i wikilink: **un riferimento che non si risolve non è un riferimento.** Il 2026-08-10, 21 voci su 45 nominavano il proprio paper solo con un numero interno morto, un id d'inbox o un autore-anno; `FT-004` e `FT-029` erano lo stesso paper da mesi, duplicato che nessun dedup poteva vedere.

**La riga `**Surface:**` è derivata — non modificarla a mano.** La rigenera `python3 framework/scripts/surface_census.py --annotate`, e nomina solo i PMID che la voce già dichiara. Il quadro d'insieme, con i paper del corpus che nessuna voce ha in coda, sta in [[surface_census]]: pagina generata, tenuta **fuori** da questo file perché un PMID qui è una dichiarazione di debito di lettura, e una tabella derivata dell'intero corpus non lo è.

---

## FT-001
**Paper:** PMID 32000863 / DOI 10.1186/s40478-020-0883-3 — Cheng et al. 2020, *Acta Neuropathol Commun* ([[paper_registry_current#PAPER 019]])
**Title:** Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and GSK3β-mediated epileptic seizure activity in mice
**Surface:** PMID 32000863 · `structured` · sentinella `clean` · PMID32000863_Cheng2020_PMC.xml, PMID32000863_Cheng2020_supplementary.pdf
**Priority:** HIGH
**Why:** structural substrate + GSK3β + PNS + cerebellar involvement
**Current status:** ✅ **RISOLTA — letta integralmente il 2026-08-04**, receipt `FTR-20260804-32000863-01`, `complete_fulltext_read`. 🔴 La voce è rimasta ferma a *«cited in meta, not yet deeply extracted»* per sei giorni **dopo** la lettura: il receipt esisteva, la coda non lo sapeva. Non è un caso isolato — vedi `FT-004` e `FT-010`.
**Next action:** nessuna. Voce chiusa con la sua ragione, conservata per tracciabilità.

---

## FT-002
**Paper:** PMID 32581702 / DOI 10.3389/fnins.2020.00644 — Iacomino et al. 2020, *Front Neurosci* ([[paper_registry_current#PAPER 020]])
**Title:** Loss of Wwox Perturbs Neuronal Migration and Impairs Early Cortical Development
**Surface:** PMID 32581702 · `structured` · PMCID `PMC7300205`, JATS XML da PMC efetch, CC BY ·
`PMID32581702_Repudi2020_PMC.xml` · quattro figure dall'editore in `files/figures/PMID32581702/`
**Priority:** HIGH
**Why:** core prenatal migration/cortical layering paper
**Current status:** ✅ **LETTO INTEGRALMENTE il 2026-08-10** — receipt `FTR-20260810-32581702-01`,
`complete_fulltext_read`; manifest `PMID32581702.json`, 21 locator, `MANIFEST STRICT PASS` sotto
**entrambi** i validatori (`80e6f03` e `2e6fd6a`). Copertura pannelli **22/22**, budget dichiarato
*prima* della lettura. La voce diceva *«cited in meta, not yet deeply extracted»*: era esatta, ed
è la classe `UNREAD_PREMISE` — una fonte su cui il modello si appoggiava senza averla letta.

**Cosa ha prodotto la lettura** (dettaglio completo nel manifest e nel receipt):

| reperto | dove vive |
|---|---|
| 🔴 il paper si contraddice sull'`n` dei controlli del suo unico esperimento umano — Methods *un* feto, Results *tre*, e la figura mostra **una** colonna Ctrl per colorazione | entries[0], [1], [14] |
| 🔴 l'effetto più grande del paper (BrdU, **8 zone su 10** significative, ~11× alla zona 2) è riassunto nel testo come *«altered distribution»*, senza un numero | entries[2], [3] |
| 🔴 `p.R264Ter` tronca **subito dopo l'MTS e prima del sito catalitico**: se il trascritto sfugge all'NMD il prodotto conserva WW1, WW2, NLS e l'intera sequenza di targeting mitocondriale | entries[6], [7] |
| 🔴 l'asse di significatività dell'unica figura molecolare **non è ricostruibile** — né p-value né probabilità NOISeq | entries[10], [20] |
| 🔴 l'abstract attribuisce ai **progenitori** ciò che il pannello mostra nei **neuroni** | entries[11] |
| 🔴 il test proteico della claim centrale è stato fatto, è risultato **non significativo**, e la Discussione non lo ripete | entries[13] |
| `p.P47R` (WOREE, pannello 1G) contro `p.Pro47Thr` (SCAR12, Discussione) — conferma indipendente del reperto di Oliver 2023 | entries[7], [8] |

**Supplementari:** `unavailable` — cinque rotte esaurite e nominate nel manifest. Pesa: la
`Supplementary Figure S3` **è** l'immunoistochimica di TUBA1A, cioè il negativo proteico, e non è
stata ispezionata. Chi la ottiene riapra `entries[13]` per primo.

**Next action:** nessuna sul paper. Il debito residuo è `FT-057`, che questa lettura ha generato.

---

## FT-003
**Paper:** PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003 — Piard et al. 2019, *Eur J Paediatr Neurol* ([[paper_registry_current#PAPER 025]])
**Title:** Novel WWOX deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay and dysmorphic features
**Surface:** PMID 30853297 · `absent`
**Priority:** HIGH
**Why:** exon 6 skipping + Q230P compound-context logic
**Current status:** abstract-level use in system
**Next action:** full text retrieval or user upload if needed

---

## FT-004
**Paper:** PMID 36779245 / DOI 10.1111/epi.17542 — Oliver KL et al. 2023, *Epilepsia* ([[paper_registry_current#PAPER 018]])
**Title:** WWOX developmental and epileptic encephalopathy: Understanding the epileptology and the mortality risk
**Surface:** PMID 36779245 · `structured` · sentinella `clean` · PMID36779245_Oliver2023_PMC.xml
**Priority:** HIGH
**Why:** key survival/natural history cohort; directly relevant to N/M vs N/N interpretation
**Current status:** ✅ **RISOLTA — duplicata di [[full_text_queue_current#FT-029]]**, che è la voce viva per questo paper. Letta integralmente il 2026-08-04, receipt `FTR-20260804-36779245-02`, `complete_fulltext_read` (preceduto da `-01`, `partial_fulltext_read`). 🔴 Due voci per lo stesso PMID sono esistite in parallelo perché questa lo nominava come *«30 / PAPER 018»* e quella per PMID: **un identificatore non risolvibile non è solo debito, è un duplicato che nessun dedup può vedere.**
**Next action:** nessuna. Conservata: cancellarla toglierebbe la traccia del duplicato invece della sua causa.

---

## FT-005
**Paper:** PMID 31543760 / DOI 10.3389/fncel.2019.00391 — Kośla et al. 2019, *Front Cell Neurosci* ([[paper_registry_current#PAPER 022]])
**Title:** The WWOX Gene Influences Cellular Pathways in the Neuronal Differentiation of Human Neural Progenitor Cells
**Surface:** PMID 31543760 · `absent`
**Priority:** MED
**Why:** supports developmental differentiation axis
**Current status:** processed only at bootstrap level
**Next action:** full text if prenatal axis needs refinement

---

## FT-006
**Paper:** PMID 26390919 / DOI 10.1002/gcc.22286 — Choo et al. 2015, *Genes Chromosomes Cancer*
**Title:** Tumor suppressor WWOX moderates the mitochondrial respiratory complex
**Surface:** PMID 26390919 · `absent`
**Priority:** MED
**Why:** could strengthen mitochondrial axis beyond HIF1A/glycolysis
**Current status:** cited in meta only
**Next action:** assess whether needed for P5 upgrade

---

## FT-007
**Paper:** DOI 10.1101/2025.11.22.689900 — bioRxiv preprint, 2025-11-22 (Aqeilan lab; emerso dalla review Obeid 2026, [[paper_registry_current#PAPER 029]])
**Title:** WWOX deficiency uncovers a cell-autonomous mechanism impairing myelin repair
🔴 **Titolo corretto il 2026-08-10.** La voce portava *«WWOX as a cell-autonomous regulator of oligodendrocyte differentiation and remyelination (cuprizone; SOX10)»*, che è una **parafrasi del meccanismo, non il titolo del lavoro**. Stessa classe di difetto del titolo inventato di `PAPER 021`. La parafrasi resta utile e sopravvive qui sotto in `Why`; smette di fingersi un titolo.
**Surface:** `unjoined` — la voce dichiara solo un DOI; il corpus locale è indicizzato per PMID, quindi non c'è nulla a cui agganciarla.
**Priority:** HIGH
**Why:** adds a SECOND myelin mechanism (cell-autonomous oligodendroglial, via SOX10, stress/remyelination-dependent) alongside the known non-cell-autonomous neuronal one → P4/P6
**Current status:** not in registry; cited via review only
**Next action:** retrieve full text; candidate new claim (oligodendroglial WWOX/SOX10)

---

## FT-008
**Paper:** PMID 30290271 — Hussain et al. 2019, *Neurobiology of Disease* 121:163–176
**Title:** Wwox deletion leads to reduced GABA-ergic inhibitory interneuron numbers and activation of microglia and astrocytes in mouse hippocampus
**Surface:** PMID 30290271 · `structured` · sentinella `clean` · PMID30290271_Hussain2019.html, PMID30290271_Hussain2019.pdf
**Priority:** HIGH
**Why:** primary systemic-KO source for regional PV/NPY marker-positive counts, IBA1/GFAP
area fractions and GAD65/67 protein. It does not directly measure GABA synthesis/abundance,
E/I balance, synaptic inhibition, seizure activity or interneuron death.
**Current status:** ✅ full text, all 6 figures, Table 1, both supplementary tables and all 90
references read on 2026-08-06; receipt `FTR-20260806-30290271-01`; dossier
`fulltext_dossiers/PMID30290271.md`. Already represented by `PAPER 006` and `LIT-006`, with
duplicate `CORPUS-STUB-085`; canonical normalization awaits `BATCH_COMMIT`.
**Next action:** propagate the queued identifier/dedup and evidence-boundary corrections only
through an authorised `BATCH_COMMIT`.

---

## FT-009
**Paper:** DOI 10.1101/2025.05.01.651195 — Lucas-Clarke HJ et al., bioRxiv preprint, 2025-05-01
**Title:** Alzheimer's disease risk gene *Wwox* protects against amyloid pathology through metabolic reprogramming
🔴 **Titolo corretto il 2026-08-10** — anche qui la voce portava una parafrasi (*«WWOX, Aβ42 neurotoxicity and metabolic reprogramming in Drosophila (ATF4/UPR; methionine; HIF1α-independent)»*) al posto del titolo. Due su due fra le voci senza identificatore: **una voce che non dichiara un ID tende a non dichiarare nemmeno un titolo verificabile.**
**Surface:** `unjoined` — la voce dichiara solo un DOI; il corpus locale è indicizzato per PMID, quindi non c'è nulla a cui agganciarla.
**Priority:** MED-HIGH
**Why:** P5 metabolism — introduces a HIF1α-INDEPENDENT axis → tension with CLAIM 025 (WWOX/HIF1A ratio); protection via methionine suppression, not lactate
**Current status:** not in registry; preprint (observation only)
**Next action:** retrieve; reconcile with CLAIM 025 / meta_metabolism

---

## FT-010
**Paper:** PMID 42397075 / DOI 10.1093/brain/awag239 — Aqeilan lab 2026, *Brain* ([[paper_registry_current#PAPER 001]], registrato come preprint «Steinberg 2024 organoids»)
**Title:** Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids
**Surface:** PMID 42397075 · `pdf_only` · sentinella `clean` · PMID42397075_Aqeilan2026.pdf
**Priority:** MED
**Why:** mechanistic depth (MYC↔WWOX, progenitor dynamics) for CLAIM 002 / human spectrum
**Come è stato risolto:** `PAPER 001` dichiara `Identifier: preprint` e nessun PMID; il ponte al pubblicato è nel tracking log, `CC-2026-07-05-008 — upgrade di PAPER 001 (Aqeilan/Davila, *Brain* awag239)`. **L'identità c'era, in un altro file, in una riga di changelog.**
**Current status:** 🟡 **letto parzialmente il 2026-08-09** — receipt `FTR-20260809-42397075-01` e `-02`, entrambi `partial_fulltext_read`. La voce diceva *«cited; full mechanistic detail not extracted»*: vero prima del 9 agosto, non aggiornato dopo. Debito residuo reale, ma minore di quanto la voce dichiarasse.
**Next action:** chiudere il parziale → `complete_fulltext_read`. Superficie: PDF, `clean` al sentinella ma pur sempre PDF — cercare prima XML/HTML PMC.

---

## FT-011
**Paper:** PMID 38182577 / DOI 10.1038/s41419-023-06378-8 — Akkawi R, Hidmi O, Haj-Yahia A, Monin J, Diment J, Drier Y, Stein GS, Aqeilan RI 2024, *Cell Death Dis*
**Title:** WWOX promotes osteosarcoma development via upregulation of Myc
🔴 **Titolo corretto il 2026-08-10, e questa correzione cambia il segno.** La voce dichiarava *«MYC is negatively regulated by WWOX»* — che è il **verso opposto** del titolo del lavoro. Il paper mostra entrambe le cose (il ripristino di WWOX riduce Myc nelle cellule doppio-KO), ma la voce presentava la conclusione che serviva al nodo MYC come se fosse il titolo. **Una parafrasi orientata è peggio di un titolo mancante: sopravvive alla lettura di chi si fida della coda.**
**Surface:** PMID 38182577 · `pdf_only` · sentinella `clean` · PMID38182577_Akkawi2024.pdf
**Priority:** MED
**Why:** mechanistic anchor for the MYC node seen in WWOX-KO radial glia — da leggere sapendo che il contesto è osteosarcoma e che la direzione dichiarata nel titolo è positiva
**Current status:** non nel paper registry; presente nel corpus locale come PDF, con l'erratum `PMID 38355659` (*Correction: WWOX promotes osteosarcoma development via upregulation of Myc*) anch'esso locale.
**Next action:** recuperare; leggere insieme all'erratum; ricollegare a `FT-010` / CLAIM 002 **dopo** aver stabilito in che condizioni il segno si inverte.

---

## FT-012 — STRATEGIC WATCH (not a standard FT item)
**Paper:** NOT_AN_ARTICLE — comunicato stampa istituzionale, nessun PMID e nessun DOI **per costruzione**, non per debito. L'identificatore comparirà con il report peer-reviewed, ed è quello che questa voce sorveglia.
**Source:** PRESS / institutional release, NOT peer-reviewed — EurekAlert 1131219, Times of Israel, Jerusalem Post, AFHU (2026-06-15)
**Event:** **FIRST-IN-HUMAN WWOX gene-replacement therapy** (Aqeilan lab) reported 2026 in an infant with WWOX-related genetic epilepsy, delivered directly into the brain (ICV). *(News-level; individual case specifics are not reproduced here.)*
**Surface:** `n/a` — non è un articolo, non c'è superficie da censire.
**Priority:** STRATEGIC — HIGHEST
**Epistemic status:** background/observation only — press, no clinical data published; do NOT treat as DATO. Watch for the peer-reviewed clinical report.
**Why:** the closest existing development to the disease context — same gene, same disorder class, pediatric, the exact therapy class. Decision-relevant for gene-therapy strategy / possible access pathways.
**Next action:** dedicated STRATEGIC deep dive when clinical details/protocol/outcome are published (variant treated, dose, AAV design, window, safety incl. DRG). Monitor Aqeilan-lab output.

---

## FT-013
**Paper:** PMID 42082822 / DOI 10.1007/s43032-026-02112-9 — Denkboy Öngen et al. 2026, *Reprod Sci* (INBOX-007)
**Title:** The Role of WWOX Gene Variant in Hypospadias and 46,XY Disorders of Sexual Development
**Surface:** PMID 42082822 · `absent`
**Priority:** MED
**Why:** WWOX-direct human variant paper outside CNS; possible genotype/variant biology bridge, but likely low direct applicability.
**Current status:** queued from PubMed clipboard triage 2026-07-05
**Next action:** retrieve full text/abstract; classify whether variant effect has mechanistic relevance or remains background.

---

## FT-014
**Paper:** PMID 41984841 / DOI 10.1073/pnas.2534844123 — Bidany-Mizrahi / Aqeilan 2026, *PNAS* (INBOX-008)
**Title:** WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma
**Surface:** PMID 41984841 · `pdf_only` · sentinella `clean` · PMID41984841_BidanyMizrahi2026.pdf
**Priority:** HIGH
**Why:** WWOX-direct Aqeilan-lab mechanistic paper; EMT/identity/stress-response bridge may inform broader WWOX pathway logic despite oncology domain.
**Current status:** queued from PubMed clipboard triage 2026-07-05
**Next action:** full-text deep extraction; look specifically for WWOX interactors/pathways transferable to neurodevelopment or proteostasis hypotheses.

---

## FT-015
**Paper:** PMID 40263068 / DOI 10.1016/j.tice.2025.102926 — Tang et al. 2025, *Tissue Cell* (corrigendum; l'originale è PMID 40198927 / DOI 10.1016/j.tice.2025.102885) (INBOX-009)
**Title:** Corrigendum to "WWOX attenuates the progression of gallbladder cancer by suppressing cellular glycolysis through the modulation of the P73/HIF-1a signaling pathway"
**Surface:** PMID 40263068 · `absent`  ·  PMID 40198927 · `absent`
**Priority:** MED-HIGH
**Why:** Corrigendum to a WWOX/HIF1A/p73 metabolism paper already relevant to CLAIM 025-style metabolism logic; must verify whether correction is formal or affects interpretation.
**Current status:** queued from PubMed clipboard triage 2026-07-05
**Next action:** retrieve corrigendum text; compare against original PAPER/CORPUS record before any claim-level use.

---

## FT-016
**Paper:** PMID 39952983 / DOI 10.1038/s41598-024-81158-8 — Kim et al. 2025, *Sci Rep* (INBOX-011)
**Title:** Genome-wide identification and functional validation of the WW domain containing oxidoreductase gene associated with sleep duration
**Surface:** PMID 39952983 · `absent`
**Priority:** MED-HIGH
**Why:** WWOX-direct, human genetics + functional validation; possible neuro/circadian/excitability bridge, not WOREE-specific.
**Current status:** queued from PubMed clipboard triage 2026-07-05
**Next action:** retrieve full text; evaluate WWOX functional assay, tissue relevance, and whether sleep/excitability readouts connect to seizure/network state.

---

## FT-017
**Paper:** PMID 39933386 / DOI 10.1016/j.seizure.2025.01.025 — Martin et al. 2025, *Seizure* (INBOX-012)
**Title:** Infantile Epileptic Spasms Syndrome: Unveiling clinical and genetic variability in a case series from Argentina
**Surface:** PMID 39933386 · `absent`
**Priority:** LOW-MED
**Why:** DEE/epileptic-spasms bridge literature; useful only if WWOX appears in the cohort or if genotype/phenotype management patterns transfer.
**Current status:** queued from PubMed clipboard triage 2026-07-05
**Next action:** check gene list and phenotype table; filter if no WWOX/SCAR12/WOREE or actionable DEE bridge appears.

---

## FT-018
**Paper:** PMID 28123895 — Bandini 2016
**Title:** The non-inflammatory role of C1q during Her2/neu-driven mammary carcinogenesis
**Surface:** PMID 28123895 · `absent`
**Priority:** HIGH
**Why:** l'abstract riporta **attivazione di WWOX ridotta** in tumori C1q-deficienti → C1q come regolatore a monte dello **stato di attivazione** di WWOX (non del livello). C1q è centrale nel pruning sinaptico microgliale ed è druggabile (anticorpi anti-C1q già in trial umani). Asse neuroinfiammazione + stato di attivazione.
**Current status:** `NEW` all'intake 2026-07-26; abstract letto, **full text NON letto**. PMCID PMC5214935 (open).
**Next action:** full text deep extraction
**⚠️ Nota di calibrazione:** la matrice di priorità l'ha collocato **P3_LOW** scorando sull'asse `BLOCK-1/safety`, mentre il contenuto reale è neuroinfiammazione + repurposing. Accodato HIGH **a dispetto del tier**, per la regola «il ranking ordina la lettura, non la sostituisce».

---

## FT-019
**Paper:** PMID 21444760 — Leduc 2011
**Title:** The mouse QTL map helps interpret human genome-wide association studies for HDL cholesterol
**Surface:** PMID 21444760 · `absent`
**Priority:** MEDIUM
**Why:** `Wwox` emerge come gene candidato per HDL per convergenza QTL murino × GWAS umano. Rilevante per la meta metabolica e, via colesterolo cerebrale, per l'asse mielina.
**Current status:** `NEW` all'intake 2026-07-26; abstract letto, **full text NON letto**. PMCID PMC3090235 (open).
**Next action:** full text deep extraction

---

## FT-020
**Papers:** PMID 21075834 *(rif. 39, confermato)* · PMID 15664696 *(rif. 38, **candidato**)* · PMID 21115974 *(rif. 87, **candidato**)* — i tre riferimenti WWOX-diretti di PMID 34214506 rimasti non risolti alla creazione della voce
**Title:** (39) **confermato** — *Drosophila orthologue of WWOX, the chromosomal fragile site FRA16D tumour suppressor gene, functions in aerobic metabolism and regulates reactive oxygen species* (O'Keefe 2011, *Hum Mol Genet*): titolo e descrizione coincidono. · (38) **candidato** — *Light-induced retinal damage involves tyrosine 33 phosphorylation, mitochondrial and nuclear translocation of WW domain-containing oxidoreductase in vivo* (2005, *Neuroscience*): copre il danno luminoso, **non** i topi `rd` che la descrizione nomina. · (87) **candidato** — *The tumor suppressor gene WWOX links the canonical and noncanonical NF-κB pathways in HTLV-I Tax-mediated tumorigenesis* (Fu 2011, *Blood*): modula NF-κB, ma il legame diretto a IκBα non compare nel titolo.
🔴 **I due candidati non sono risolti, sono ristretti.** Vanno confermati contro la reference list di PMID 34214506, non contro la loro plausibilità. Restano marcati finché quella verifica non avviene: **un candidato promosso a identità è come si perde il paper giusto senza accorgersene.**
**Surface:** PMID 21075834 · `absent`  ·  PMID 15664696 · `absent`  ·  PMID 21115974 · `pdf_only` · sentinella `SUSPECT` · PMID21115974_Fu2011.pdf  ·  PMID 34214506 · `pdf_only` · sentinella `SUSPECT` · PMID34214506_Saadane2021.pdf
**Priority:** HIGH
**Why:** tutti e tre **WWOX-diretti** e citati dentro una fonte già letta integralmente. Il rif. 87 è la base della via trascrizionale alternativa che regge [[dismissal_ledger_current#DIS-008 — «La calpaina è una via di degradazione/turnover per WWOX» → ⏸️ **NON STABILITA (rigettata come affermazione, non come possibilità)**]]: finché non è letto, quella via resta plausibile ma non verificata alla fonte.
**Current status:** debito di espansione multi-hop **non svolto** nella sessione 2026-07-26.
**Next action:** risolvere i tre riferimenti a PMID, dedup contro il registry, poi full text

---

## FT-021
**Paper:** PMID 24308844 — Schuchardt et al. 2013
**Title:** Molecular origin of the binding of WWOX tumor suppressor to ErbB4 receptor tyrosine kinase
**Surface:** PMID 24308844 · `absent`
**Priority:** HIGH
**Why:** fonte primaria WWOX–ErbB4 direttamente a monte di PMID 35716775; serve a verificare quali determinanti di sequenza/affinità precedenti sopravvivono oltre il nuovo modello topology-dependent e a evitare che peptidi ingegnerizzati vengano generalizzati ai partner naturali.
**Current status:** già catalogato in paper/tracking registry; nessuna `complete_fulltext_read` receipt trovata al 2026-07-26. Debito multi-hop esplicitamente aperto.
**Next action:** receipt preflight → full text; confrontare costrutti, buffer, PY1/PY2/PY3, full-length/cell context e qualsiasi tensione con il pose parallelo di PMID 35716775.

---

> **Espansione multi-hop del deep dive PMID 22193544** (2026-07-26). Le quattro voci sotto
> vengono dalla **reference list** di quel lavoro, che nella prima passata non era stata
> elencata: il debito era stato *dichiarato* e non *svolto*. Risolte a PMID e deduplicate
> contro registry, tracking log e batch queue. **Tre su quattro erano ignote al modello.**

## FT-022
**Paper:** PMID 20067585 — Castaño Z, Gordon-Weeks PR, Kypta RM (rif. 27 di PMID 22193544)
**Title:** The neuron-specific isoform of glycogen synthase kinase-3β is required for axon growth
**Surface:** PMID 20067585 · `absent`  ·  PMID 22193544 · `structured` · sentinella `clean` · PMID22193544_Wang2012.pdf, PMID22193544_Wang2012_PMC_JATS.xml
**Priority:** **HIGH**
**Why:** candidata risoluzione della contraddizione che Wang 2012 **ammette e non risolve** (GSK3β blocca o favorisce la crescita neuritica?). Se l'arco WWOX-rilevante e la crescita assonale passano per **isoforme diverse**, un inibitore globale come il litio le colpisce entrambe → rischio su [[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]] **oggi assente dal punteggio**. È anche il `REVIVAL_TRIGGER` (c) di `DIS-009`. Regge `DL-MECH-066`.
**Current status:** 🔴 **PAYWALLED — resta APERTO, e vale ancora la priorità HIGH.** Cascata di
acquisizione esaurita e documentata il 2026-07-26: PMC (non depositato) · Unpaywall (`oa_status:
closed`) · OpenAlex (`any_repository_has_fulltext: false`) · Semantic Scholar (`CLOSED`) · Wiley
(HTTP 403). Quattro fonti indipendenti concordano. Ricevuta `FTR-20260726-20067585-01` a
profondità **`abstract_only`**, copertura `unavailable` (non saltata: non ottenibile lecitamente).
**L'abstract da solo è già stato decisivo** → ha sostanziato `DL-MECH-066`, generato
`DL-MECH-067` e `DL-BIO-013`, e fatto scattare il `REVIVAL_TRIGGER (c)` di `DIS-009`.
**Next action:** vie residue per il full text, in ordine di costo: (1) **e-mail agli autori** —
R. M. Kypta e P. R. Gordon-Weeks, richiesta di estratto per ricerca accademica su malattia rara;
(2) **canale della fondazione** (WWOX Foundation) per accesso istituzionale; (3) **prestito
interbibliotecario / ILL**. Domande da porre al testo quando disponibile, **nessuna risolta
dall'abstract**: quali siti esatti di tau per ciascuna isoforma (S404 in particolare — di S396
sappiamo già che è di *entrambe*); come è stata misurata l'affinità differenziale di Axin per β1
vs β2 e quanto è grande; se il litio o inibitori ATP-competitivi discriminano le isoforme.

---

## FT-026
**Paper:** PMID 21212533 — Saeki K, Machida M, Kinoshita Y, Takasawa R, Tanuma S 2011, *Biol Pharm Bull* 34(1):146-149
**Title:** Glycogen synthase kinase-3β2 has lower phosphorylation activity to tau than glycogen synthase kinase-3β1
**Surface:** PMID 21212533 · `pdf_only` · sentinella `SUSPECT` · PMID21212533_Saeki2011.pdf
**Priority:** **HIGH**
**Why:** **fonte primaria** del fatto oggi più carico di conseguenze sull'asse GSK3β: che le due
isoforme fosforilino tau con cinetica e siti diversi. Oggi lo conosciamo solo attraverso una
**review** (PMC3139124, ricevuta `queried_not_full_read`) — cioè una fonte secondaria letta per
estrazione mirata, non un dato verificato alla fonte. Regge `DL-MECH-066` e, indirettamente, il
razionale di sicurezza di `DL-MECH-067`.
**Current status:** ✅ **LETTO INTEGRALMENTE il 2026-07-26** — ricevuta
`FTR-20260726-21212533-01`, `complete_fulltext_read`, PDF gratuito J-STAGE, fingerprint
`790f6020…92dca7`, figure ispezionate come immagini, 24 referenze enumerate. Manifest:
`deepdive_manifests/PMID21212533.json`. Prodotti: `DL-MECH-068` (nuovo), correzione di
`DL-MECH-066`, rafforzamento di `DL-MECH-067`, `FT-027` e `FT-028` accodati.
**Esito, e una correzione a nostro carico:** stabilisce che **tau è un substrato *sfavorito* per
β2** — non che β2 sia una chinasi debole (APP-Thr668 e pGS-2 equivalenti). 🔴 **Ma NON dice quello
che gli avevamo attribuito**: misura **un solo sito, Ser396**, e non affronta la selettività di
sito. Il claim sui *«residui diversi»* è di **Mukai 2002** → `FT-027`. **`Ser404` resta non testato
per isoforma da chiunque.**

---

## FT-027
**Paper:** PMID 12065620 — Mukai F, Ishiguro K, Sano Y, Fujita SC 2002, *J Neurochem* 81(5):1073-1083
**Title:** Alternative splicing isoform of tau protein kinase I / glycogen synthase kinase 3beta
**Surface:** PMID 12065620 · `absent`
**Priority:** **HIGH**
**Why:** è la **vera fonte primaria** del claim che le due isoforme fosforilino tau su **residui in
parte diversi** (`Ser199` β1-specifico) — claim che questa sessione aveva erroneamente attribuito a
Saeki 2011 leggendolo attraverso una review. Vedi la correzione dentro `DL-MECH-066`. È anche il
rif. 4 di Saeki per la distribuzione CNS di β2.
**Current status:** **ignoto al modello**; retraction check già eseguito (OK) il 2026-07-26.
**Next action:** acquisire. **Domanda che nessun altro lavoro ha risolto: `Ser404` — il secondo sito
chiave di Wang 2012 — è fosforilato da entrambe le isoforme o solo da β1?** Da questo dipende quanta
parte dell'asse WWOX→tau sia realmente β1-selettiva, e quindi quanto valga il vantaggio di sicurezza
ipotizzato in `DL-MECH-067`/`DL-MECH-068`.

## FT-028
**Paper:** PMID 19607922 — Wood-Kaczmar A, Kraus M, Ishiguro K, Philpott KL, Gordon-Weeks PR 2009, *Mol Cell Neurosci* 42(3):184-194
**Title:** An alternatively spliced form of glycogen synthase kinase-3beta is targeted to growing neurites and growth cones
**Surface:** PMID 19607922 · `absent`
**Priority:** **HIGH**
**Why:** fonte primaria della localizzazione di β2 in **neuriti e coni di crescita**, che è il perno
dell'argomento di sicurezza sulla finestra evolutiva in `DL-MECH-068`(a). Oggi la conosciamo solo
via review (`queried_not_full_read`). **Stesso laboratorio di `FT-022`** (Gordon-Weeks PR): leggere
i due insieme dà la visione completa del gruppo che ha definito la biologia di β2.
**Current status:** **ignoto al modello**; retraction check già eseguito (OK) il 2026-07-26.
**Next action:** acquisire; estrarre la **finestra temporale** di espressione di β2 e la sua
localizzazione subcellulare quantitativa, poi confrontarla con la finestra mielinica e con
[[meta_prenatal_structure_current]].

## FT-023
**Paper:** PMID 15026124 — Chen ST et al. 2004, *Neuroscience* (rif. 12 di PMID 22193544)
**Title:** Expression of WW domain-containing oxidoreductase WOX1 in the developing murine nervous system
**Surface:** PMID 15026124 · `absent`  ·  PMID 22193544 · `structured` · sentinella `clean` · PMID22193544_Wang2012.pdf, PMID22193544_Wang2012_PMC_JATS.xml
**Priority:** **HIGH**
**Why:** è la **motivazione dichiarata** dell'intero lavoro di Wang 2012 e, più in generale, la fonte originaria della tesi che WWOX abbia un ruolo nel differenziamento e nella maturazione neuronale — cioè una premessa del modello di malattia. Ed è **ignota al modello**: la tesi neuroevolutiva è in uso senza che la sua fonte primaria sia mai stata letta. Stessa classe di difetto di `UNREAD_PREMISE`.
**Current status:** **ignoto al modello** — assente da paper registry, tracking log e batch queue al 2026-07-26.
**Next action:** full text; estrarre la finestra temporale precisa di espressione (bassa nell'embrionale precoce, media-alta nel fetale medio-tardivo secondo la citazione di seconda mano) e confrontarla con la finestra mielinica e con [[meta_prenatal_structure_current]].

## FT-024
**Paper:** PMID 15126504 — Sze CI et al. 2004, *J Biol Chem* (rif. 2 di PMID 22193544)
**Title:** Down-regulation of WW domain-containing oxidoreductase induces Tau phosphorylation in vitro. A potential role in Alzheimer's disease
**Surface:** PMID 15126504 · `absent`  ·  PMID 22193544 · `structured` · sentinella `clean` · PMID22193544_Wang2012.pdf, PMID22193544_Wang2012_PMC_JATS.xml
**Priority:** **HIGH**
**Why:** **controparte diretta** di `DIS-010` e dell'arco *tau* di `DL-MECH-019`. Sarebbe anche il **terzo studio** che consentirebbe di riesaminare lo status di [[claim_registry_current#CLAIM 016]] (oggi due sole fonti, e `WWOX AND GSK3` restituisce 5 record in tutto PubMed).
**Current status:** 🔴 **citato come premessa da `analysis/therapy_levers.md` (lever B1) senza essere mai stato letto** — è l'istanza che ha motivato il check `UNREAD_PREMISE`. In batch queue, segnalato senza full text libero; JBC 2004 è plausibilmente disponibile su PMC post-embargo.
**Next action:** acquisire; verificare se il legame WWOX–Tau è diretto o mediato, e con quale metodo (l'affermazione originale nasce da yeast two-hybrid, che ha falsi positivi noti).

## FT-025
**Paper:** PMID 17178850 — Gaudio E et al. 2006, *Cancer Res* (rif. 17 di PMID 22193544)
**Title:** Physical association with WWOX suppresses c-Jun transcriptional activity
**Surface:** PMID 17178850 · `pdf_only` · sentinella `clean` · PMID17178850_Aqeilan2006.pdf  ·  PMID 22193544 · `structured` · sentinella `clean` · PMID22193544_Wang2012.pdf, PMID22193544_Wang2012_PMC_JATS.xml
**Priority:** MEDIUM
**Why:** regge l'**unico controllo di folding** offerto per il mutante `L404A` (co-IP di c-jun conservato). Un controllo a partner singolo è debole per escludere un difetto conformazionale locale proprio nella regione in esame: serve sapere quanto è robusta e quanto è sensibile al fold quella interazione.
**Current status:** **ignoto al modello** — assente da paper registry, tracking log e batch queue al 2026-07-26.
**Next action:** acquisire opportunisticamente; stabilire quale dominio media il legame a c-Jun (se WW e non SDR, il controllo di Wang è ancora più debole di quanto sembri).

---

## FT-029
**Paper:** PMID 36779245 — Oliver KL et al. 2023, *Epilepsia* 64:1351–1367 ([[paper_registry_current#PAPER 018]])
> **ID corretto il 2026-08-04.** Questa voce era stata creata come `FT-026`, ID già occupato da
> Saeki 2011. Rinumerata a `FT-029`; il wikilink `[[full_text_queue_current#FT-026]]` nel
> discovery ledger punta correttamente alla voce Saeki e non va toccato.
**Title:** WWOX developmental and epileptic encephalopathy: Understanding the epileptology and the mortality risk
**Surface:** PMID 36779245 · `structured` · sentinella `clean` · PMID36779245_Oliver2023_PMC.xml
**Priority:** **HIGH**
**Why:** è la fonte di [[claim_registry_current#CLAIM 017]] (spettro WOREE↔SCAR12) e del `p = .0085` citato da [[claim_registry_current#CLAIM 033]]. Una lettura **completa** renderebbe lo spettro esportabile verso DisMech e darebbe al modulo condiviso l'evidenza che gli manca — oggi il routing verso entrambe le entry poggia su una claim che non può essere esportata.
**Current status:** 🟡 **letto parzialmente** il 2026-08-04, receipt `FTR-20260804-36779245-01`, `evidence_depth: partial_fulltext_read`. Testo JATS letto per intero (abstract, introduzione, metodi, risultati, discussione, Tabelle 1 e 3); **le quattro figure sono disponibili solo come didascalie** e due supplementary non sono stati recuperati. Figura 4 *è* l'analisi di sopravvivenza e Figura 3 la mappa delle varianti: giudicarle dalla didascalia è il fallimento per cui esiste il valore `captions_only`. Tentativi falliti: pacchetto OA PMC (404), OA PDF (404), URL immagine `/bin/` (301 non risolto), endpoint PDF Europe PMC (404).
**Aggiornamento 2026-08-04 — le figure sono state recuperate e ispezionate.** Il blocco non era
l'accesso, era la rotta. Tutte e quattro le immagini si ottengono da
`https://pmc.ncbi.nlm.nih.gov/articles/instance/<PMCID-senza-PMC>/bin/<file>.jpg`, con il PMCID
risolto via `elink.fcgi?dbfrom=pubmed&db=pmc&id=<PMID>` — non dal nome host provato in
precedenza, che restituiva 301. La rotta è stata trovata usandola su un altro paper
(PMID 39507621) e poi riprovata qui: **la lezione riutilizzabile è che un 301/404 su una rotta
immagine non è un verdetto di indisponibilità, ed era stato registrato come tale.**
Contenuto letto dalle immagini, non dalle didascalie: **Fig. 4A** ordina la sopravvivenza
null/missenso > missenso/missenso > null/null, con bande di confidenza ampiamente sovrapposte
fra i primi due — e il `p = .0085` è un log-rank **a tre gruppi**, non un confronto a coppie;
**Fig. 4B** dà `p = .65` sull'esordio delle crisi, cioè il gruppo genotipico **non** predice
l'età d'esordio; **Fig. 3** colloca le due missenso associate a SCAR12 (p.Pro47Thr esone 2,
p.Gly372Arg esone 9) alle estremità opposte della proteina; **Fig. 1C** documenta una semiologia
focale lateralizzante; **Fig. 2** mostra atrofia fronto-temporale e ippocampale, atrofia del
nervo ottico, anomalie della sostanza bianca e corpo calloso sottile.
**Supplementary: confermati non disponibili.** `s001.docx` e `s002.xlsx` rispondono 200 ma
servono HTML, non i documenti. `unavailable` non impedisce un receipt completo.
**✅ CHIUSA il 2026-08-04.** Receipt `FTR-20260804-36779245-02`,
`evidence_depth: complete_fulltext_read`, 20 `verbatim_locators`, manifest
[`PMID36779245.json`](deepdive_manifests/PMID36779245.json). Copertura: testo, Tabelle 1–3 e
tutte e 4 le figure `read`; supplementary `unavailable` (verificato: HTTP 200 che serve HTML).
**Correzione editoriale del 24 marzo 2023** presa in conto — riguarda la colonna 9 di Tabella 1,
cioè il Paziente 9: qualunque lettura di quella tabella deve usare i valori corretti.
**Il risultato che cambia il modello:** il paper afferma esplicitamente che **non esiste
evidenza di un fenotipo "intermedio"** — vedi le tre commit candidate su
[[claim_registry_current#CLAIM 017]] e [[claim_registry_current#CLAIM 033]] in
[`locator_contract_live_test.md`](../analysis/locator_contract_live_test.md).

---

## FT-030
**Paper:** PMID 25716914 — Mignot C et al. 2015 (riferimento 18 di [[paper_registry_current#PAPER 015]])
**Title:** WWOX and severe autosomal recessive epileptic encephalopathy: first case in the prenatal period
**Surface:** PMID 25716914 · `absent`
**Priority:** **MEDIA-ALTA**
**Why:** Teplyshova 2024 registra **assenza di attività motoria fetale nell'ultimo mese di
gravidanza** e attribuisce alla letteratura l'idea che le varianti WWOX disturbino lo sviluppo
del sistema nervoso già in fase embrionale. Questo è il caso a presentazione prenatale, cioè il
test diretto di quell'attribuzione: o la sostiene con un dato indipendente, o mostra che poggia
su un singolo caso. Rilevante per la finestra temporale d'insorgenza, che vincola qualsiasi
ipotesi di intervento precoce.
**Come è emerso:** enumerando la lista dei riferimenti di PMID 39507621. Assente da
`paper_registry_current`, dalla coda full-text e dal tracking log — LEGEND non l'aveva mai visto.
**Current status:** ⬜ non recuperato, non letto.

---

## FT-031
**Paper:** PMID 32051108 — (riferimento 6 di [[paper_registry_current#PAPER 015]])
**Title:** A Chinese patient with epilepsy and WWOX compound heterozygous mutations
**Surface:** PMID 32051108 · `absent`
**Priority:** **MEDIA**
**Why:** caso a eterozigosi composta, cioè la classe genotipica intermedia (null/missenso) che
in Oliver 2023 Fig. 4A mostra la sopravvivenza **migliore** delle tre. Ogni caso indipendente in
quella classe conta, perché è quella su cui le bande di confidenza sono più larghe e la
lettura del gradiente è meno solida.
**Come è emerso:** stessa enumerazione di FT-030. Mai visto da LEGEND.
**Priorità alzata il 2026-08-04:** compare **anche** nella lista riferimenti di Oliver 2023
([[paper_registry_current#PAPER 018]]). Due paper indipendenti lo citano e LEGEND non l'aveva
mai visto — la doppia citazione non duplica la voce, ne alza la priorità. Lo stesso vale per
FT-030.
**Current status:** ⬜ non recuperato, non letto.

---

## FT-032
**Papers:** PMID 30094525 · PMID 35573960 · PMID 26345274 · PMID 17360458 · PMID 11719429 — i 5
riferimenti gene-diretti di [[paper_registry_current#PAPER 018]] (Oliver 2023) assenti da
registry, coda e tracking log. *(Gli ID erano già nella tabella qui sotto; qui salgono sulla
riga di identità, dove un dedup li può leggere.)*
**Surface:** PMID 30094525 · `absent`  ·  PMID 35573960 · `absent`  ·  PMID 26345274 · `absent`  ·  PMID 17360458 · `pdf_only` · sentinella `SUSPECT` · PMID17360458_Aqeilan2007.pdf  ·  PMID 11719429 · `absent`
**Priority:** **MEDIA-ALTA** — sui primi due, **ALTA**.

| PMID | Anno | Sede | Titolo | Perché |
|---|---|---|---|---|
| 30094525 | 2018 | *Neurol Sci* | WWOX-associated encephalopathies: identification of the phenotypic spectrum and the resulting genotype-phenotype correlation | è **la** correlazione genotipo-fenotipo pre-Oliver: serve per sapere se il "range intermedio" che Teplyshova 2024 attribuisce alla letteratura nasce qui, e se Oliver lo stia contraddicendo o correggendo |
| 35573960 | 2022 | *Front Pediatr* | A phenotypic-driven approach for the diagnosis of WOREE syndrome | approccio diagnostico fenotipo-guidato; tocca direttamente la questione se il fenotipo predica la classe genotipica — che Oliver Fig. 4B nega sull'asse dell'esordio |
| 26345274 | 2015 | *Am J Med Genet A* | Severe CNS involvement in WWOX mutations: description of five new cases | cinque casi nella serie storica su cui poggia la statistica di mortalità |
| 17360458 | 2007 | *PNAS* | Targeted deletion of Wwox reveals a tumor suppressor function | il knockout murino originale — fonte primaria per il modello animale |
| 11719429 | 2001 | *Cancer Res* | WWOX, the FRA16D gene, behaves as a suppressor of tumor growth | il paper fondativo del gene. Parità delle fonti: è oncologia, ed è la biologia molecolare di WWOX alla sorgente |

**Come sono emersi:** enumerando i 50 riferimenti di Oliver 2023 — 26 gene-diretti con PMID, 19
già nel registry, **7 no**. Un tasso di mancanza del 27% sulla bibliografia di un paper già in
registry come fonte di tre claim.
**Current status:** ⬜ nessuno recuperato, nessuno letto.

---

## FT-033
**Paper:** DOI 10.1093/brain/awm078 — Gribaa M et al. 2007, *Brain* 130(7):1921–1928
(riferimento 4 di [[paper_registry_current#PAPER 014]]). *Nessun PMID nelle fonti locali: la voce
è pre-WWOX e assente dal seed PubMed WWOX, quindi il DOI è l'identificatore, non un ripiego.*
**Title:** A new form of childhood onset, autosomal recessive spinocerebellar ataxia and epilepsy is localized at 16q21-q23
**Surface:** `unjoined` — la voce dichiara solo un DOI; il corpus locale è indicizzato per PMID, quindi non c'è nulla a cui agganciarla.
**Priority:** **ALTA**
**Why:** è **l'origine di SCAR12** — lo studio di linkage che definisce l'entità prima ancora
che WWOX fosse identificato come il gene (Mallaret 2014). Tutto il polo mite dello spettro
poggia su questa descrizione, e LEGEND non l'ha mai letta: sta usando SCAR12 come categoria
senza aver visto il documento che la costituisce. Rilevante per
[[claim_registry_current#CLAIM 017]] e [[claim_registry_current#CLAIM 008]].
**Come è emerso:** enumerazione dei 47 riferimenti di Gao 2025.
**Current status:** ⬜ non recuperato, non letto.

---

## FT-034
**Papers:** DOI 10.1165/rcmb.2020-0145OC · DOI 10.7759/cureus.46216 · DOI 10.1002/ana.25619 ·
**Surface:** `unjoined` — la voce dichiara solo un DOI; il corpus locale è indicizzato per PMID, quindi non c'è nulla a cui agganciarla.
DOI 10.1684/epd.2017.0924 · DOI 10.1007/s12035-023-03346-3 · DOI 10.21203/rs.3.rs-1682290/v1 —
i restanti 6 riferimenti gene-diretti di [[paper_registry_current#PAPER 014]] ignoti a LEGEND.
*(Come per `FT-032`: gli ID erano nella tabella, non sulla riga di identità. La nota sul metodo
qui sotto — «un audit con una sola chiave sovrastima i propri risultati» — vale anche qui: una
voce che tiene gli ID solo in tabella è invisibile a un dedup che legge la riga `Paper:`.)*

| Rif. | Anno | DOI | Titolo | Perché |
|---|---|---|---|---|
| 46 | 2021 | 10.1165/rcmb.2020-0145OC | Cigarette smoke and e-cigarette vapor downregulate lung WWOX expression, associated with increased severity of murine ARDS | **il seed di repurposing.** Gao propone antinfiammatori per le complicanze respiratorie WWOX-null appoggiandosi a questo e ai rif. 45/47. Il 45 (Singla 2017) LEGEND ce l'ha; questo no |
| 9 | 2023 | 10.7759/cureus.46216 | Respiratory dysfunction in epileptic encephalopathies: insights and challenges | l'altro pilastro dell'asse respiratorio, che in Gao è una delle tre sole associazioni significative |
| 26 | 2019 | 10.1002/ana.25619 | The genetic landscape of epilepsy of infancy with migrating focal seizures | EIMFS è una delle sindromi in cui Oliver classifica WWOX-DEE; qui c'è il panorama genetico completo |
| 41 | 2017 | 10.1684/epd.2017.0924 | Practical clues for diagnosing WWOX encephalopathy | indizi diagnostici pratici — utile alla domanda "il fenotipo predice la classe genotipica?" |
| 24 | 2023 | 10.1007/s12035-023-03346-3 | Whole-genome sequencing among Kazakhstani children with early-onset epilepsy | coorte non occidentale: contrasta il bias di ascertainment che Gao dichiara su di sé |
| 29 | 2022 | 10.21203/rs.3.rs-1682290/v1 | Compound heterozygous deletions of WWOX caused a WOREE syndrome (**preprint**) | preprint: solo osservazione, non può superare `in observation` |

**Nota sul metodo, da registrare.** Il primo controllo su questa bibliografia era **su DOI** e
dava 12 ignoti. Cinque erano stati accodati poche ore prima da Oliver e Teplyshova e registrati
**per PMID**: la chiave singola non li vedeva. Rifatto su entrambe le chiavi → 7.
**Un audit di bibliografia con una sola chiave sovrastima i propri risultati, e li sovrastima
nella direzione che lo lusinga.**
**Current status:** ⬜ nessuno recuperato, nessuno letto.

---

## FT-035
**Paper:** PMID 40875931 / DOI 10.1212/WNL.0000000000213883 — Gao K et al. 2025, *Neurology* ([[paper_registry_current#PAPER 014]]) — materiale mancante della **stessa** lettura
**Title:** Gao 2025 — eTable 1/2/3 e figure a risoluzione piena
**Surface:** PMID 40875931 · `absent`
**Priority:** **MEDIA-ALTA**
**Why:** il receipt `FTR-20260804-40875931-02` è `partial_fulltext_read` per una ragione
precisa, non generica: **eTable 1** contiene i dati grezzi per caso (le 18 risposte binarie e
le classificazioni di variante) e **Figura 2B** è la griglia 44 × 18 da cui Tabella 2 è
calcolata. Senza, due cose non si possono verificare: (a) l'identità del **quinto individuo
senza crisi** — il testo ne nomina quattro ma riporta crisi in 45/50, quindi ce n'è uno non
nominato, e con M/M a n=6 un singolo individuo sposta la proporzione di 17 punti sul `p=0.016`;
(b) se le tre associazioni significative reggano a una riclassificazione **funzionale** invece
che sintattica delle varianti.
**Next action:** eTable 1 è supplementary di *Neurology*; serve accesso istituzionale o
richiesta agli autori (i dati grezzi sono dichiarati disponibili su richiesta al
corresponding author).
**Current status:** ⬜ non recuperato.

---

## FT-036
**Paper:** PMID 10861292 — riferimento gene-diretto di [[paper_registry_current#PAPER 019]]
(Cheng 2020, receipt `FTR-20260804-32000863-01`)
**Title:** Common chromosomal fragile site FRA16D sequence: identification of the FOR gene spanning FRA16D
**Surface:** PMID 10861292 · `absent`
**Priority:** **MEDIA**
**Why:** è la caratterizzazione di sequenza del sito fragile che **contiene** WWOX. Parità delle
fonti: è un lavoro di genomica del cancro del 2000, e per LEGEND è il documento che descrive
*perché* questo locus si rompe. Rilevante per l'interpretazione delle CNV, che in
[[paper_registry_current#PAPER 014]] sono il 31% delle varianti e si concentrano sull'esone 6.
**Come è emerso:** enumerazione dei 66 riferimenti di Cheng 2020 — 27 gene-diretti con PMID, **26
già nel corpus**. Il tasso di copertura del 96% su quest'asse contrasta con le tre letture
cliniche precedenti, che avevano trovato 7 o più lacune ciascuna: **la densità del corpus non è
uniforme, è alta sul meccanismo murino e bassa sulle coorti cliniche.**
**Current status:** ⬜ non recuperato, non letto.

---

## FT-037
**Paper:** PMID 36499501 — Huyan et al. 2022, *Int J Mol Sci* 23(23):15177
**Title:** miR-221-5p and miR-186-5p are the critical bladder cancer derived exosomal miRNAs in natural killer cell dysfunction
**Surface:** PMID 36499501 · `absent`
**Priority:** **MEDIA-ALTA**
**Why:** è il riferimento **più vicino all'asse** del paper che lo cita e l'unico dei 29
riferimenti gene-/asse-diretti di PMID 37519886 **assente da ogni file LEGEND** — registro
paper, tracking log, batch queue, coda full-text e discovery ledger. Dà a miR-186-5p una
biologia misurata (miRNA esosomiale che induce disfunzione delle cellule NK in BLCA) là dove
Kołat 2023 gli dà solo un ruolo predetto in una rete ceRNA. Se WWOX-loss alza miR-186-5p, il
percorso verso l'evasione immunitaria è meglio sostenuto dell'asse ceRNA del titolo; e la
direzione conta anche per capire *quale* metà dell'asse valga la pena inseguire.
**Come è emerso:** enumerazione dei 80 riferimenti di Kołat 2023 durante la lettura completa del
2026-08-05 (receipt `FTR-20260805-37519886-01`), poi cross-query meccanica dei 29 PMID
gene-/asse-diretti contro le registry: 19 nel registro paper, 9 solo in `batch_queue.md`,
**1 assente ovunque**. Questo.
**Transfer atteso al genotipo di riferimento:** basso e dichiarato — oncologia/immunologia
adulta. Va letto come `DISCOVERY_ONLY`, non come candidato canonico.
**Current status:** ⬜ non recuperato, non letto.

---

## FT-038
**Paper:** PMID 30619736 — Hussain et al. 2018, *Front Oncol* 8:591
**Title:** Delineating WWOX protein interactome by tandem affinity purification-mass spectrometry: identification of top interactors and key metabolic pathways involved
**Surface:** PMID 30619736 · `absent`
**Priority:** **ALTA**
**Why:** è la **sorgente dell'arco WWOX·UPF1** su cui poggia [[discovery_ledger_current#DL-MECH-069 — 🔑 L'efficienza dell'NMD potrebbe essere **WWOX-dipendente**, e questo tocca sia l'allele di sito accettore sia l'esperimento disegnato per caratterizzarlo|DL-MECH-069]]:
l'interazione WW1 ↔ ¹⁰⁰⁵PPGY¹⁰⁰⁸ di UPF1, cioè il ponte fra WWOX e il macchinario NMD che
decide il destino del trascritto PTC dell'allele di sito accettore. Il record è già nel registro
paper e **è citato come premessa** nel discovery ledger, ma **non ha alcuna ricevuta di
lettura**: è esattamente la forma di debito che il ratchet `unread_premise` esiste per rendere
visibile. Da leggere prima che `DL-MECH-069` possa salire di stato — servono la stechiometria
dell'interazione, i controlli di specificità, e se UPF1 compaia con altri componenti del
complesso EJC/NMD.
**Come è emerso:** durante la lettura di PMID 37519886, che importa l'arco senza misurarlo.
**Current status:** ⬜ recuperato? no — non letto.

---

## FT-039
**Paper:** PMID 24871327 — Iatan et al. 2014, *Circ Cardiovasc Genet* 7:491-504
**Title:** The WWOX gene modulates high-density lipoprotein and lipid metabolism
**Surface:** PMID 24871327 · `structured` · sentinella `clean` · PMID24871327_Iatan2014_PMC.html
**Priority:** **ALTA**
**Why:** è il primario citato da PMID 33255508 per il primo dei due passaggi del ponte
`WWOX -> lipid homeostasis -> myelin`. La review lo descrive come “strong evidence”, ma la
lettura corrente non trasferisce quell'etichetta: servono modello, perturbazione, endpoint e
dimensioni d'effetto del primario prima che il nodo lipidico possa sostenere un'inferenza
neurale o un biomarcatore.
**Come è emerso:** multi-hop della lettura completa di PMID 33255508, receipt
`FTR-20260806-33255508-01`, `DL-MECH-070`.
**Current status:** ⬜ presente nel corpus, non letto integralmente.

---

## FT-040
**Paper:** PMID 31340538 — Tochigi et al. 2019, *Int J Mol Sci* 20:3596
**Title:** Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination
in a Rat Model of Lethal Dwarfism with Epilepsy
**Surface:** PMID 31340538 · `structured` · sentinella `clean` · PMID31340538_Tochigi2019.xml
**Priority:** **ALTA**
**Why:** è il primario animale direttamente citato dalla review per sviluppo corticale e
ipomielinizzazione. Il grafo lo usa già come ancora strutturale, ma non esiste ancora un
receipt completo; deve essere letto prima di estrarre tempistica, autonomia cellulare o
mediazione lipidico/traffico.
**Come è emerso:** multi-hop e horizontal pass di PMID 33255508, receipt
`FTR-20260806-33255508-01`, `DL-MECH-070`.
**Current status:** ✅ full text, tutte le 6 figure e 56 referenze letti il 2026-08-06;
receipt `FTR-20260806-31340538-01`; dossier `fulltext_dossiers/PMID31340538.md`.

---

## FT-041
**Paper:** PMID 17803050 — Suzuki et al. 2007, *Comparative Medicine* 57:360-369
**Title:** Phenotypic characterization of spontaneously mutated rats showing lethal dwarfism
and epilepsy
**Surface:** PMID 17803050 · `pdf_only` · sentinella `SUSPECT` · PMID17803050_Suzuki2007.html, PMID17803050_Suzuki2007.pdf
**Priority:** **ALTA**
**Why:** è il primo primario fenotipico del ratto `lde` e l'unico dei 30 riferimenti
WWOX/modello/malattia-diretti di PMID 31340538 assente da paper registry, tracking log, batch
queue, coda full-text e discovery ledger. Deve portare mortalità, crescita, atassia e
fenotipo epilettico antecedenti alla mappatura Wwox; il paper 2019 li importa soltanto.
**Come è emerso:** enumerazione delle 56 referenze durante la lettura completa di PMID
31340538 (`FTR-20260806-31340538-01`), seguita da cross-query meccanica del corpus.
**Priorità rivista 2026-08-06:** compare anche come referenza 27 di PMID 19936220, accanto a
`FT-042`, nella stessa frase di Discussione da cui l'intera premessa "epilettogenesi" del KO
murino deriva. Va letto insieme a `FT-042`, non dopo. Vedi `DL-MECH-073`.
**Priorità rivista 2026-08-06 (seconda volta) — MASSIMA.** Dopo la lettura completa di
`FT-042`, questo non è più un primario di contorno: è la fonte su cui poggia
**interamente** l'affermazione più forte che `FT-042` fa sul meccanismo — *"Normal levels of
serum constituents **clearly excluded** the possibility that these abnormal excitabilities are
resulted from a systemic metabolic disorder"* — oltre al 33% di crisi spontanee e al GH
ipofisario basso. Vedi `DL-MECH-076`.
**Current status:** ✅ **LETTO INTEGRALMENTE 2026-08-06** — receipt
`FTR-20260806-17803050-01`; manifest schema-v2 con **32 locator** verificati strict (25 corpo,
4 tabella, 3 figura), zero gap, zero waiver di sezione; dossier in
`fulltext_dossiers/PMID17803050.md`. Dieci pagine, sei figure e tre tabelle ispezionate sulle
pagine renderizzate, 35 referenze enumerate. Nessun materiale supplementare esiste.
**Provenienza:** irrecuperabile da ogni aggregatore — **senza DOI** Unpaywall, OpenAlex e
Semantic Scholar non sono indirizzabili e non c'è deposito PMC. Full text fornito
dall'operatore; layer testuale trascritto verbatim in artefatto HTML locale con separazione
abstract/corpo dimostrata prima dell'uso — **separazione qui load-bearing**, perché
l'errore centrale che questa lettura scopre vive in una frase presente **solo nell'abstract**.
🔴 **Esito — verdetto diviso su `FT-042`, e la seconda metà cade.** (1) Il contrasto specifico
col topo è **confermato**: glucosio, calcio ed elettroliti normali nel ratto. Ma *"clearly
excluded"* è **sovradimensionato** — BUN ~3.2–3.5× e creatinina significativamente aumentati:
il ratto è **uremico senza essere ipoglicemico**. Gli autori offrono inoltre una spiegazione
concorrente mai testata (ipercatabolismo e disgregazione muscolare da crisi ripetute, con
precedente nel ceppo SER) che **compete direttamente con l'ipotesi di acidosi tubulare renale
costruita per il topo**. Vedi `DL-MECH-077`. (2) 🔴 L'attribuzione del nanismo al GH ipofisario
basso è **refutata dalla fonte stessa**: la differenza **non è significativa** e il paper
conclude che il nanismo *"cannot be explained solely by low levels of plasma GH"*. La frase
non qualificata esiste **solo nell'abstract** di questo paper. Vedi `DL-MECH-078`.
**Nota di metodo:** il 2026-08-06 l'operatore aveva fornito prima il solo abstract, registrato
come `abstract_only` **senza receipt**. Se fosse stato accettato come lettura, "GH ridotto"
sarebbe entrato nel modello come dato — e non lo è. Correzioni isolate in
`staging/commit_candidate_20260806_17803050.md`.

**🔴 RIAPERTO 2026-08-09 — LA SUPERFICIE TESTUALE DI QUESTA LETTURA È RIFIUTATA.**
**Questa lettura è ora nello stesso stato di `FT-044` (PMID 33914858).**

L'artefatto `files/fulltext/PMID17803050_Suzuki2007.html` è una trascrizione del text layer
del PDF, e quel text layer è difettoso: contiene **34 corruzioni note** in cui un carattere di
confronto è stato sostituito dal separatore C0 `U+001D`. Il paper stampa `(P < 0.023)`;
l'artefatto dice `(P \x1d 0.023)`; il locator persistito dice `(P  0.05)`.

**Perché nessun controllo l'aveva vista.** `_normalise_text` usava `str.split()`, e in Python
`'\x1d'.isspace()` è `True`: il separatore veniva collassato a spazio su *entrambi* i lati,
artefatto e citazione normalizzavano alla stessa stringa, e il match usciva timbrato
**`strict`** — il livello che significa "sequenza di caratteri dell'autore trovata intatta".
Il normalizzatore lavava via il difetto che avrebbe dovuto esporre.

**Conseguenza sui 29 locator testuali di questa lettura:** non sono verificabili. Il
validatore ora rifiuta l'intera superficie (`SUSPECT text surface`) invece di normalizzarla,
perché ripulire i controlli spalmerebbe il difetto su ogni citazione tratta da lì e le
citazioni tornerebbero a verificare — contro un documento che non è più il paper.

**🔴 AGGIORNAMENTO 2026-08-09 — i cinque locator corrotti sono AGGIUDICATI sulla pagina.**
Verbale e immagini fingerprintate in
[`page_adjudications/PMID17803050/`](page_adjudications/PMID17803050/README.md). Misura invece
di stima: i 29 locator stanno su **5 pagine**, 0 non localizzati, e solo **5** hanno
corruzione *dentro* la citazione; gli altri 24 sono puliti nel proprio span e vanno solo
ri-ancorati. Cinque rendering, non ventinove, perché `entries[0]` e `entries[1]` sono frasi
adiacenti e un solo ritaglio le aggiudica entrambe. Mappature confermate sulla pagina:
`U+001D`→`<`, `U+000C`→`⁺` in apice, `–`→`⁻` in apice, `q`→`±`.
**Nessuna delle cinque cambia un valore, una direzione o un verdetto di significatività:**
`CLAIM 038` e `CLAIM 039` reggono esattamente come scritte. Mancava la capacità di
*dimostrarle*, non i fatti. Restano da ri-ancorare i 24 puliti e da sostituire la superficie
dichiarata nel manifest — scrittura canonica, quindi dietro `BATCH_COMMIT`.

**Nota di metodo, pagata sul campo:** il primo rendering ha usato come ago `significantly (P`
ed è finito su **un'altra frase** di pagina 2 che porta la stessa corruzione. Avrebbe
aggiudicato il carattere giusto per il locator sbagliato. È il rischio della prima occorrenza
documentato in `_quote_matches`, incontrato pochi minuti dopo averlo scritto: **si aggiudica
su un ago univoco per quel locator**, non sul frammento che contiene il carattere corrotto.

**Debito latente registrato (non lavoro):** tre `.xlsx` sono dichiarati con `kind` testuale in
due manifest e il validatore non sa leggerli. Nessun locator li nomina, quindi il difetto è
inerte e fallisce nella direzione sicura — chi ci appoggiasse un locator lo vedrebbe rifiutato
in scrittura.

**La superficie va RI-DERIVATA dalla fonte, non corretta a mano.** Una correzione manuale su
34 punti è indistinguibile da una riscrittura e non è verificabile da nulla. Finché non è
ri-derivata, `CLAIM 038` e `CLAIM 039` poggiano su locator non verificabili: le *conclusioni*
non sono in discussione — restano lette da un umano sul documento — ma la loro **catena di
prova** sì.

## FT-042
**Paper:** PMID 19500159 — Suzuki et al. 2009, *Genes Brain Behav* 8:650-660
**Title:** A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with
lethal dwarfism and epilepsy
**Surface:** PMID 19500159 · `pdf_only` · sentinella `clean` · PMID19500159_Suzuki2009.html, PMID19500159_Suzuki2009.pdf
**Priority:** **ALTA**
**Why:** è il primario load-bearing per mappatura della delezione esone 9, mRNA/proteina e
crisi audiogeniche del modello `lde`. `DL-MECH-026` usa già questi risultati ma il full text
non ha receipt; Tochigi 2019 li cita, non li rimisura tutti. Va letto prima di usare il 95% di
penetranza o la causalità genetica come dato di prima mano.
**Come è emerso:** multi-hop di PMID 31340538 e audit del preesistente `DL-MECH-026`.
**Priorità rivista 2026-08-06 — ALTA/1:** la lettura completa di `FT-043` ha stabilito che
l'epilettogenesi attribuita al KO murino **non è misurata** in PMID 19936220 e vi entra solo
come citazione di questo paper (referenza 26). PMID 19500159 non è più "il primario del
modello ratto": è il **terminale effettivo** di una premessa oggi attribuita a un paper
murino, su specie e classe allelica diverse (delezione 13 bp esone 9 → frameshift
C-terminale, non un null; crisi audiogene). Finché non è letto, nessuna formulazione
canonica può dire che un modello murino Wwox-null "mostra epilettogenesi". Vedi `DL-MECH-073`.
**Current status:** ✅ **LETTO INTEGRALMENTE 2026-08-06** — receipt
`FTR-20260806-19500159-01`; manifest schema-v2 con **30 locator** verificati strict (24 corpo,
2 tabella, 4 figura), zero gap, zero waiver di sezione; dossier in
`fulltext_dossiers/PMID19500159.md`. Undici pagine, otto figure e due tabelle ispezionate sulle
pagine renderizzate, referenze enumerate.
**Provenienza:** otto tier automatici rifiutati (bronze OA, Cloudflare); full text ottenuto
dall'operatore per accesso istituzionale. Poiché il paper non esiste in alcuna forma
strutturata leggibile, il layer testuale del PDF è stato trascritto verbatim in un artefatto
HTML locale **con l'abstract racchiuso in un contenitore riconosciuto**, così la separazione
abstract/corpo di schema-v2 è preservata anziché aggirata — e la separazione è stata dimostrata
prima dell'uso.
⚠️ **Supplementari dichiarati `unavailable`, non saltati:** Figure S1/S2, Video S1 e Tabelle
S1/S2 esistono e sono citati cinque volte. Il recupero ha restituito **HTTP 403** sia
sull'endpoint supplementi Wiley sia sull'ancora supporting-information, e il PDF non contiene
allegati. Curve di crescita, sopravvivenza, pesi d'organo e statistica di segregazione sono
quindi letti solo come i Results li descrivono.
🔴 **Esito — la premessa non è solo priva di sostegno: il terminale afferma il contrario.**
Questo paper dichiara in tre punti e in Table 2 che i **topi Wwox-null non hanno epilessia**;
la riga *Epilepsy* della tabella è compilata solo per `lde/lde`. Il fenotipo del **ratto** è
invece solido (95% crisi audiogene, 60% spontanee, 0/14 controlli, spike interictali in tutti i
mutanti, vacuoli ippocampali 9/9 vs 0/10). Vedi `DL-MECH-075`.
⚠️ **Aperto:** l'esclusione della causa metabolica sistemica nel ratto (*"clearly excluded"*)
poggia interamente su `FT-041`, non letto, il cui abstract riporta urea, creatinina e fosfato
**aumentati**. Vedi `DL-MECH-076`. Correzioni isolate in
`staging/commit_candidate_20260806_19500159.md`.

---

## FT-043
**Paper:** PMID 19936220 — Ludes-Meyers et al. 2009, *PLoS ONE* 4:e7775
**Title:** Generation and characterization of mice carrying a conditional allele of the Wwox tumor suppressor gene
**Surface:** PMID 19936220 · `structured` · sentinella `clean` · PMID19936220_Ludes-Meyers2009.pdf, PMID19936220_Ludes-Meyers2009_PMC.xml
**Priority:** **ALTA**
**Why:** è il primario load-bearing per generazione, ricombinazione e fenotipo basale del
modello knockout usato da PMID 30290271. Hussain 2019 importa quel protocollo e non rimisura
tutti i passaggi di costruzione/validazione del modello. Il record è già nel corpus ma non ha
una ricevuta completa; va letto prima di promuovere causalità genetica, specificità del
controllo o dettagli di generazione come dati di prima mano.
**Come è emerso:** enumerazione delle 90 referenze durante la lettura completa di PMID
30290271 (`FTR-20260806-30290271-01`) e cross-query dei 20 riferimenti WWOX-/modello-/malattia-diretti.
**Current status:** ✅ **LETTO INTEGRALMENTE 2026-08-06** — receipt `FTR-20260806-19936220-01`;
manifest schema-v2 con 23 locator verbatim verificati strict e zero gap; dossier in
`fulltext_dossiers/PMID19936220.md`. Full text JATS + PDF + sei figure ispezionate come
immagini + tre tabelle + 28 referenze (28/28 PMID risolti). Nessun materiale supplementare
esiste; nessuna sezione limitations.
**Esito:** la premessa importata si spezza. **Morte precoce = confermata di prima mano**
(43% a 72 h, 77% al giorno 17, 100% prima dello svezzamento; arresto della crescita dal
giorno 10). 🔴 **Epilettogenesi = non misurata qui in nessuna forma** — nessun EEG, crisi,
comportamento o istologia cerebrale; l'unica misura cerebrale del paper è il peso in Table 2.
La catena prosegue verso il ratto *lde* (`FT-042`/`FT-041`). Vedi `DL-MECH-073` e
`DL-MECH-074`. Correzioni isolate in `staging/commit_candidate_20260806_19936220.md`.

## FT-044
**Paper:** PMID 33914858 — Repudi et al. 2021, *Brain* 144:3061–3077
**Title:** Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects
**Surface:** PMID 33914858 · `pdf_only` · sentinella `SUSPECT` · PMID33914858_Aqeilan2021.pdf
**Priority:** **ALTA**
**Why:** è la fonte primaria di `CLAIM 003` (*consolidated baseline*) — ipomielinizzazione
non-cell-autonoma da delezione neuronale di Wwox — e il sistema non ne ha mai avuto il testo
fino al 2026-08-07. Nessuna receipt esiste per questo PMID.
**Come è emerso:** corpus Aqeilan RI, gruppo 1 della sessione di lettura 2026-08-09.
**Current status:** 🔴 **LETTURA SOSPESA 2026-08-09 — NESSUNA RECEIPT EMESSA.** La sospensione
**non** è per budget né per copertura incompleta: è per invalidità della superficie testuale.
L'estrazione deterministica (PyMuPDF `get_text()`) restituisce dai Methods
`Results were considered significant when P 5 0.05`, mentre la pagina **stampa** `P < 0.05`
— dimostrato renderizzando a 600 dpi p. 5 dello stesso PDF. In tutto il documento: **zero
occorrenze di `<`, `>`, `≤`, `≥`** contro 14 di `P 5 0.0…`; anche `fold change 41.5`
(`> 1.5`) e `delta (55 Hz)` (`<5 Hz`, una banda di frequenza). `fitz`, `pdfplumber` e `pypdf`
concordano tutti e tre sul carattere sbagliato, quindi **incrociare due estrattori non
rileva il difetto**.
**Perché non è stato riparato:** riparare il testo richiede un gate che non esiste ancora, e
una riparazione non verificata da un gate è indistinguibile da una riscrittura. 🔴 **Il
meccanismo del difetto NON è stabilito** — l'ipotesi `ToUnicode` è stata testata e falsificata
(15 font su 16 non dichiarano alcun `ToUnicode`, e la copertura non discrimina: PMID 42397075
ha 7/18 ed estrae pulito, PMID 17803050 ha 5/6 ed estrae corrotto). L'unico `DATO` è la
**discrepanza fra pagina renderizzata e testo estratto**. Un guard non può poggiare sulla
causa finché la causa è ignota: dovrà essere sintomatico e la pagina renderizzata dovrà
dirimere. Dettaglio completo e riproduzione in
[`framework/eval/finding_20260809_text_surface_fidelity.md`](../../../framework/eval/finding_20260809_text_surface_fidelity.md).

**🔴 CORREZIONE APPEND-ONLY 2026-08-09 (seconda passata) — due affermazioni di questa voce
erano sbagliate, ed entrambe erano rassicuranti.**

**(a) «Il difetto non ha raggiunto lo stato canonico» era FALSO.** L'ho scritto sulla base di
un audit che cercava le firme sbagliate: `\x1d` e `P\s*[45]\s*0?\.\d+`. La firma reale che
domina in questo corpus è il **comparatore assente del tutto** — non sostituito da un altro
carattere, semplicemente sparito. `deepdive_manifests/PMID17803050.json` entries[0] cita
`«significantly (P  0.05) higher»`, dove il paper stampa `(P < 0.05)`. Il difetto **è dentro
un manifest persistito**, in una fonte canonica (`PAPER 059`, base di `CLAIM 038`/`CLAIM 039`).
Il mio «242 stringhe, zero contaminate» era un falso negativo prodotto da una query, non una
verifica. *Un audit che non trova nulla va sospettato prima di essere creduto: la prima cosa
da verificare è che stesse cercando la cosa giusta.*

**(b) Il sentinella dichiarato non intercetta quella firma**, e non per una svista nelle
soglie: perché **la normalizzazione precede il controllo**. Il criterio veniva applicato dopo
un passaggio che già scartava la punteggiatura, quindi guardava una stringa da cui il
comparatore era stato tolto — cercava un carattere sbagliato in un testo da cui ogni
carattere di quel tipo era già stato rimosso.

**Firma aggiunta al sentinella:** `\([Pp]\s+\d` — «parentesi, P, spazio, cifra», cioè una
soglia statistica senza comparatore. Va valutata **sul testo grezzo**, prima di qualunque
normalizzazione.

**Difetto correlato, riparato oggi nel verificatore** (`deepdive_manifest._match_key`):
la chiave di match scartava *ogni* carattere non alfanumerico, mappando `(P < 0.05)`,
`(P > 0.05)` e `(P 0.05)` sulla stessa chiave `P005`. Il verificatore era cieco esattamente
sull'asse su cui si decide se un risultato è un risultato — lo stesso di `CLAIM 005`. Ora:
match strict per primo; fallback alfanumerico **solo** se lo snippet non porta comparatori,
uguaglianze o numeri con segno; altrimenti `UNVERIFIABLE_PUNCTUATION` e il locator non passa.
Costo misurato sui 118 locator persistiti: **96 strict · 13 folded · 9 refused**. I 9 vanno
ricatturati dal documento. Mutation-test 4/4, zero fughe, in entrambe le direzioni.

**🔴 SECONDA RITRATTAZIONE APPEND-ONLY 2026-08-09 — la ritrattazione precedente era a sua
volta parziale, ed è il tipo di errore peggiore: una correzione che sembra chiudere il caso.**

La riparazione descritta sopra copriva la **sostituzione** e non la **cancellazione**.
Chiedeva *«lo snippet sembra rischioso?»*, ispezionandolo per comparatori. Ma uno snippet che
ha **perso** il comparatore non ne contiene alcuno: `(P 0.05)` non ha nulla da segnalare, e
si ripiega esattamente sulla stessa chiave del `(P < 0.05)` che la fonte afferma. La
direzione pericolosa era quella scoperta.

E il locator citato qui sopra — `(P  0.05)` in `PMID17803050.json` — **non era `folded`: era
`strict`**, per la ragione descritta in `FT-041`. Dire «il matcher ora lo copre» era falso.

**La domanda giusta non è «lo snippet sembra rischioso?» ma «normalizzare cambia la
risposta?»** La seconda riparazione la implementa: il fold costruisce la chiave alfanumerica
**conservando gli offset originali**, localizza il match, ritaglia dallo *artifact* lo span
corrispondente e confronta la sequenza di caratteri decisivi dei due lati. Cancellazione,
sostituzione e segno inserito cambiano tutti quella sequenza, quindi sono tutti intercettati —
esatto in entrambe le direzioni, e indipendente da quanto lo snippet «sembri» innocuo.

In più: `_normalise_text` non usa più `str.split()` ma una **classe di whitespace esplicita**
(`[ \t\n\r\f\v   ]`), e un `article_text` che contiene controlli C0 è una
superficie `SUSPECT` **rifiutata alla validazione**, mai normalizzata.

**Nuova misura sui 118:** **79 strict · 10 folded · 29 non verificabili** — i 29 sono l'intera
superficie di `PMID17803050`, ora rifiutata in blocco. Mutation-test 6/6, zero fughe. La prima
passata ne aveva 4/6 con una fuga scoperta solo aggiungendo un test unitario sul
normalizzatore: le due difese si sovrapponevano, e una difesa che esiste solo come effetto
collaterale di un'altra smette di valere il giorno in cui l'altra viene ristretta.
**Debito:** aperto e **non** parzialmente saldato. Non esiste lettura parziale di questo
paper da cui ripartire: nessun locator è stato estratto dalla superficie sospetta, per
scelta. Riaprire **solo dopo** il gate sulla superficie testuale.
**Nota di sicurezza già chiusa:** audit di tutti i locator persistiti — 242 stringhe citate su
15 manifest, **zero contaminate**. Le claim canoniche 038/039, che poggiano sull'altro PDF
affetto (PMID 17803050), non citano soglie e sono intatte. Il difetto esiste nella pipeline e
**non ha raggiunto lo stato canonico**.

## FT-045 — ✅ CHIUSA il 2026-08-10

**Paper:** PMID 42128308 — Obeid, Wang, Abudiab, Akkawi & Aqeilan 2026, *Neurobiol Dis* 107446
**Title:** WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities
**Surface:** PMID 42128308 · `pdf_only` — **nessun deposito PMC**, verificato (`esummary`
restituisce solo `pubmed`/`doi`/`pii`, `elink` a `pmc` nessun linkset) · sentinella `clean` ·
`PMID42128308_Aqeilan2026.pdf` + `_fitz.txt` con ricetta di estrazione dichiarata.

**Lettura completa**, receipt `FTR-20260810-42128308-02`, manifest
[`PMID42128308.json`](deepdive_manifests/PMID42128308.json) — 23 locator, `MANIFEST STRICT
PASS`, 0 gap, ricontrollato in modo indipendente da `locator_audit.py` a 20/20 testo, 3
immagine, zero citazioni non trovate. Dossier:
[`PMID42128308_partial_locators.md`](fulltext_dossiers/PMID42128308_partial_locators.md).
Copertura: tutte e dodici le sezioni, entrambe le tabelle, tutte e quattro le figure `read`;
`methods`/`results`/`supplementary` **`not_present`** — è una review narrativa senza dati
primari.

**Il receipt precedente non era una lettura.** `FTR-20260726-42128308-01` è un
`record_kind: legacy_reconstruction`, costruito da una dichiarazione di registry. Il nuovo lo
cita come `prior_receipt` con `reread_reason: inadequate_prior_coverage`.

### 🔴 Il reperto: una figura generata da un modello linguistico contraddice il testo, e la regola 5c punta dalla parte sbagliata

La sezione 1 elenca **sei** categorie di gene neuroevolutivo ai siti fragili, fra cui
*glutamate receptor signaling pathways (GRID1, GRM5)*. **La Figura 2 ne mostra cinque:** la
categoria sparisce, **GRID1 non compare da nessuna parte** e **GRM5 è spostato sotto
*neuron projection development***. Anche la didascalia ne elenca cinque — didascalia e pannello
concordano fra loro e **divergono entrambi dal corpo del testo**. L'ultima frase della
didascalia è: *«This figure was prepared using Gemini.»*

La 5c privilegia il pannello sulla prosa, e se l'è guadagnato — il 2026-08-04 un pannello
rovesciò una conclusione che il testo non conteneva. **Ma quella regola è scritta per i
pannelli di DATI**, dove il pannello è l'osservazione. Questo pannello è un *rendering a valle
della prosa*, e la sua didascalia lo dichiara. Chi applicasse qui il default della 5c
porterebbe via che GRM5 è un gene di *neuron projection development* e che GRID1 non è affatto
un gene neuroevolutivo ai CFS. **Sbagliato due volte, e il testo aveva ragione.**

🔴 `PREMISE_TAG` — la premessa portante della 5c è *una figura è un'osservazione*.
`PREMISE: DEFAULT_FROM_TEXTBOOK`, falsa per questa classe. **Il discriminante è già nel
documento e costa zero: la didascalia dichiara il generatore** — FigureLabs (Fig. 1), Gemini
(Fig. 2), Biorender (Fig. 3), Biorender + Figure Labs (Fig. 4).

### Tre difetti di infrastruttura, annotati e non riparati qui

1. **`contradicts` è un puntatore intra-manifest** (`entries[N]`). Due dei reperti più forti di
   questa lettura legano un locator di questo manifest a un locator di un *altro*
   (`PMID 42397075 entries[22]`, `PMID 42422765 entries[15]`). La grammatica non ha una casella
   per il legame cross-paper: vive solo nella prosa e **nessuno strumento lo vede**.
2. **`text_contradicted_by_panel` presuppone che il pannello sia un dato.** Entrambe le voci
   `figure` di questa lettura puntano a **schemi**. La relazione è reale come discrepanza e
   priva di senso come evidenza, e il valore non ha modo di dire quale delle due.
3. **I dossier in prosa portano citazioni che nessun validatore vede.** La citazione della
   sezione 11 scritta stamattina in questo stesso dossier era **unita attraverso un a capo** e
   **non verifica** contro la superficie; gli snippet di manifest sono confrontati carattere per
   carattere, quelli dei dossier no. Ri-ancorata nel manifest.

### Cosa cambia una decisione

- 🔴 **La review dice «restored» dove il suo stesso primario mostra dieci volte il wild type**
  (§10.4 su Steinberg 2024 = `PMID 42397075`, chiuso lo stesso giorno; SATB2 ≈ 10×, CTIP2 ≈ 3×).
  La parola sopravvive perché **la parentesi WT-vs-trattato non è disegnata**.
- 🔴 **L'anello WPRE si chiude dentro un solo documento e nessuno dei due capi cita l'altro:**
  §10.4 presenta la rimozione come scelta di sicurezza, `PMID 42422765` mostra che è costata
  **sei volte la dose**, §11 nomina l'alta dose come la principale preoccupazione regolatoria
  pediatrica.
- 🔴 **L'abbondanza di proteina WWOX non è una lettura della funzione di WWOX**, dimostrato dai
  due lati: P47T ha proteina pari al wild type e fenotipo grave; gli organoidi SCAR12 hanno
  proteina minima e fenotipo quasi normale.
- 🔴 **Il framework genotipo-fenotipo a tre classi è pubblicato e falsificato nella stessa
  sezione** — e il controesempio decisivo è un **missenso omozigote (p.Ser304Tyr) che uccide
  nella prima infanzia**. «Missenso ⇒ funzione residua ⇒ più lieve» è la premessa sotto buona
  parte del ragionamento su ipomorfi e ASO in questo repository.
- **Un requisito che solo una sfida rivela:** `Olig2-Cre; O-KO` è *«No major defects»* al
  basale e difettoso sotto cuprizone. **Un readout oligodendrogliale non sfidato è un falso
  negativo per costruzione.**
- **Correnti di potassio elevate** nei neuroni piramidali Wwox-KO, lette come compenso
  maladattivo: nodo prossimale, firmato e farmacologicamente maturo che **nessuno qui ha ancora
  guardato**.

### ✅ Debito multi-hop chiuso lo stesso giorno — 103 riferimenti, 35 WWOX-diretti, 4 preprint

**Il verdetto sul delimitatore è calcolato, non affermato:** 100% delle voci accettate inizia
con il cognome del primo autore, 87,4% porta un DOI, e il controllo stampa un rigetto se una
delle due scende sotto soglia. 🔴 **Due tentativi precedenti hanno fallito e sono il punto.**
Spezzare su `Cognome, X.,` dava **237** — sovrastima, perché il pattern cattura anche autori a
metà lista. Filtrare per ordine alfabetico dava **4** — sottostima catastrofica, perché il primo
candidato era un autore di metà lista che ordina a `v` e ha avvelenato la catena. E quel
tentativo **stampava «piccolo, quindi l'assunzione regge» accanto a un tasso di rigetto del
98%**, perché la frase era hardcoded invece che calcolata. **Un verdetto che non può fallire non
è un verdetto.**

### 🔴 La claim di autonomia cellulare della mielina poggia su un preprint mai dichiarato tale

`Abudiab et al. 2025` è **bioRxiv `10.1101/2025.11.22.689900`**. È citato **sette volte in
modo sostanziale** — due in sezione 6 (WWOX fra i geni oligodendrogliali più disregolati; il
risultato cuprizone e SOX10) e in **quattro righe distinte della Tabella 1**: Olig2-Cre O-KO,
la sfida cuprizone su quella linea, la coltura OPC ex vivo, e lo snRNA-seq delle lesioni MS.
La Tabella 2 chiama il concetto cell-autonomo *«a particularly important emerging concept»* e i
meccanismi SOX10 *«a major new direction»*.

**Mai una volta è descritto come preprint.** Due pagine prima la review scrive *«A recent
preprint by (Lucas-Clarke et al., 2025)»* dell'altra fonte non referata che usa. **L'asimmetria
di dichiarazione è dentro lo stesso documento.**

🔴 **Correzione a una mia affermazione di due ore prima.** Avevo registrato il contrasto
basale-contro-cuprizone come *requisito condizionale* e chiamato un readout oligodendrogliale
non sfidato *un falso negativo per costruzione*. Resta **IPOTESI e non DATO**: la sua unica
fonte non è referata. La forma del reperto non cambia, il suo supporto sì — **e non avevo
controllato quale**.

### Due dei quattro preprint sono citazioni scadute, e una tocca lavoro già qui dentro

La review cita `Steinberg et al. 2024` a `10.1101/2024.12.22.630016` e `Obeid et al. 2026` a
`10.64898/2026.03.11.710995` — entrambi DOI di preprint. **Entrambi sono pubblicati**: come
`PMID 42397075` (*Brain*) e `PMID 42422765` (*Mol Ther Nucleic Acids*), letti oggi nella loro
forma pubblicata.

🔴 **La conseguenza non è cosmetica:** il preprint di `42397075` può differire dal manoscritto
accettato che ho aggiudicato, **inclusi i pannelli supplementari letti a 258 ppi**. Ogni
affermazione di questa review attribuita a *«Steinberg et al. 2024»* riguarda una versione che
non ho controllato — quindi la contraddizione sul *«restored»* è fra **la lettura che la review
fa del preprint** e **la mia lettura del manoscritto accettato**. Non la dissolve, perché la
versione accettata è quella che il campo citerà: ma nomina un passaggio che avevo dato per
scontato.

**Debito residuo:** i 31 riferimenti WWOX-diretti che non sono né preprint né già in registro
**non sono triageati in coda**. È lavoro di coda e questa era una sessione di lettura;
l'enumerazione esiste perché il triage si possa fare **senza riaprire il paper**. La lista è
DOI-keyed con **un solo PMID su 103**, quindi il dedup contro un registro PMID-keyed richiede
prima la risoluzione dei DOI.

---

## FT-039 — ✅ CHIUSA il 2026-08-10

**Paper:** PMID 24871327 — Iatan et al. 2014, *Circ Cardiovasc Genet* 7:491–504
**Surface:** PMID 24871327 · `structured` · sentinella `clean` · PMID24871327_Iatan2014_PMC.html
**Lettura completa**, receipt `FTR-20260810-24871327-01`, manifest
[`PMID24871327.json`](deepdive_manifests/PMID24871327.json), 22 locator verbatim in
[`PMID24871327_locators.md`](fulltext_dossiers/PMID24871327_locators.md). Superficie: PMC
HTML (nessun PDF usato). Copertura: testo, Tabelle 1–2 e tutte e 6 le immagini di figura
`read`; **supplementary `unavailable`** — author manuscript fuori dal subset open access,
cascata di cinque rotte documentata nel file dei locator.

**La domanda che FT-039 poneva era se "strong evidence" si trasferisse al nodo lipidico. La
risposta è no, e la ragione è il paper stesso:** il knockout epatico **non** abbassa l'HDL-C
circolante in nessuno dei due sessi. L'unico modello che mostra il fenotipo HDL è il null
totale, misurato in cuccioli di due giorni di una linea che muore entro quattro settimane.
Il passo che il primario autorizza davvero è `WWOX → ApoA-I/ABCA1 → biogenesi HDL`, **non
epatocita-autonomo**; la seconda gamba del ponte, `omeostasi lipidica → mielina`, **non
riceve nulla da qui — il paper non misura alcun endpoint neurale.**

**Tre reperti leggibili solo dai pannelli**, non dal testo né dalle didascalie:
- **Fig. 4F** stampa `*P = 0.0229` (maschi) e `P = 0.0877` (femmine): l'aumento di ANGPTL4 è
  significativo nei **maschi**, e la discussione costruisce il meccanismo TG **femmina**-specifico
  proprio su ANGPTL4 nelle femmine. I due P non compaiono altrove nel documento.
- **Fig. 5E**: la parentesi `***P<0.00058` copre **solo Abca1**; ApoAI non ha marcatore, mentre
  il testo afferma che *entrambi* gli mRNA sono diminuiti. È di nuovo la distinzione di
  [[claim_registry_current#CLAIM 005]].
- **Fig. 5H/J** arbitrano due P discordanti fra testo e didascalia, **uno per parte**
  (`0.0015` corretto in didascalia, `0.0007` corretto nel testo).
- **Fig. 1A**: l'aplotipo non è né necessario (l'affetta 401 non lo porta) né sufficiente (la
  fondatrice 102 lo porta e non è affetta). Il testo dice "perfectly co-segregated".

---

## FT-046
**Papers:** PMID 18974271 · PMID 15070730 — i riferimenti gene-diretti di PMID 24871327 ignoti
a LEGEND, più due premesse esterne portanti non risolte a PMID (rif. 44 Lichtenstein, rif. 53
Timmins), elencate nella tabella qui sotto.
*(Riga di identità riaperta il 2026-08-10: apriva con «i riferimenti gene-diretti di PMID
24871327», e quel PMID è il paper **citante**, non un paper di questa voce.)*
**Surface:** PMID 18974271 · `pdf_only` · sentinella `SUSPECT` · PMID18974271_Aqeilan2009.pdf  ·  PMID 15070730 · `pdf_only` · sentinella `SUSPECT` · PMID15070730_Aqeilan2004.pdf  ·  PMID 24871327 · `structured` · sentinella `clean` · PMID24871327_Iatan2014_PMC.html
**Priority:** **MEDIA-ALTA** sui primi due; **ALTA** su `18974271`.

| PMID / rif. | Anno | Titolo | Perché |
|---|---|---|---|
| 18974271 (rif. 20) | 2008 | Aqeilan et al. — Targeted ablation of *Wwox* … | 🔴 **ignoto a LEGEND.** È la fonte primaria citata in introduzione per "Wwox KO mice exhibit marked reductions in serum lipid levels and display impaired gene expression of key steroidogenic enzymes": cioè la premessa su cui poggia l'intero fenotipo lipidico del null totale, che 24871327 estende ma non stabilisce |
| 15070730 (rif. 17) | 2004 | Aqeilan et al. — Functional association … | 🔴 **ignoto a LEGEND.** Partner/funzione, serie fondativa del gruppo primario del gene |
| rif. 44 — Lichtenstein et al. | — | ANGPTL4 inattiva LPL convertendo il dimero in monomero | premessa **esterna portante** del meccanismo TG proposto. Non gene-diretta, quindi invisibile a un audit di bibliografia che filtri per WWOX — e proprio per questo va accodata a mano |
| rif. 53 — Timmins et al. | — | Il KO epatico di *Abca1* abbassa HDL plasmatico di ~80% | è il comparatore che gli autori invocano **contro** il proprio risultato negativo. Serve per sapere se il null epatico di Wwox differisce da quello di Abca1 per grado o per natura |

**Come sono emersi:** enumerazione dei **53** riferimenti di PMID 24871327 — 14 gene-diretti,
di cui **12 già noti** (uno letto integralmente, `19936220`) e **2 no**. I due non gene-diretti
sono stati aggiunti a mano perché portano premesse su cui il paper appoggia conclusioni.
**Current status:** ⬜ nessuno recuperato, nessuno letto.

---

## FT-047 — un difetto della coda, non di un paper
**Papers:** PMID 17575124 · PMID 20530675 · PMID 21318118 · PMID 22634283 · PMID 23254685 · PMID 26256646 · PMID 27308416 · PMID 27308504 · PMID 27550453 · PMID 27551470 · PMID 29724996 · PMID 30082886 · PMID 30370248 · PMID 30755385 · PMID 31428585 · PMID 32300104 · PMID 34634460 · PMID 34831305 · PMID 42395553 · PMID 42422765
*(Riga di identità aggiunta il 2026-08-10. La voce non ne aveva alcuna, e il `LINT` l'ha
segnalata al primo passaggio. Gli ID erano già nel corpo — qui salgono dove un dedup, e
l'annotazione `**Surface:**`, possono leggerli. **La voce denuncia che questi paper non sono
classificati: darle una riga di identità non li classifica, ma smette di renderli invisibili
anche alla propria denuncia.**)*
**Surface:** PMID 17575124 · `structured` · sentinella `clean` · PMID17575124_Aqeilan2007_PMC.html  ·  PMID 20530675 · `structured` · sentinella `clean` · PMID20530675_Kurek2010_PMC.html  ·  PMID 21318118 · `structured` · sentinella `clean` · PMID21318118_Drusco2011_PMC.xml  ·  PMID 22634283 · `structured` · sentinella `clean` · PMID22634283_McDonald2012_PMC.html  ·  PMID 23254685 · `structured` · sentinella `clean` · PMID23254685_Abdeen2013_PMC.html  ·  PMID 26256646 · `structured` · sentinella `clean` · PMID26256646_DelMare2015_PMC.xml  ·  PMID 27308416 · `structured` · sentinella `clean` · PMID27308416_AbuRemaileh2015_PMC.xml  ·  PMID 27308504 · `structured` · sentinella `clean` · PMID27308504_Hazan2015_PMC.xml  ·  PMID 27550453 · `structured` · sentinella `clean` · PMID27550453_DelMare2016_PMC.html  ·  PMID 27551470 · `structured` · sentinella `clean` · PMID27551470_Hazan2015_PMC.xml  ·  PMID 29724996 · `structured` · sentinella `clean` · PMID29724996_AbuRemaileh2018_PMC.xml  ·  PMID 30082886 · `structured` · sentinella `clean` · PMID30082886_Abdeen2018_PMC.xml  ·  PMID 30370248 · `structured` · sentinella `clean` · PMID30370248_Tanna2018_PMC.xml  ·  PMID 30755385 · `structured` · sentinella `clean` · PMID30755385_AbuRemaileh2019.pdf, PMID30755385_AbuRemaileh2019_PMC.xml  ·  PMID 31428585 · `structured` · sentinella `clean` · PMID31428585_Chang2019_PMC.xml  ·  PMID 32300104 · `structured` · sentinella `clean` · PMID32300104_Khawaled2020_PMC.xml  ·  PMID 34634460 · `structured` · sentinella `clean` · PMID34634460_Breton2021_PMC.xml  ·  PMID 34831305 · `structured` · sentinella `clean` · PMID34831305_Steinberg2021_PMC.xml  ·  PMID 42395553 · `structured` · sentinella `clean` · PMID42395553_PMC.xml  ·  PMID 42422765 · `structured` · sentinella `clean` · PMID42422765_Obeid2026_PMC.html
**Priority:** **ALTA** (è una perdita sistematica, non un singolo studio)

**Ventidue full text locali con superficie strutturata XML/HTML non hanno una lettura
completa, e ventuno di essi non compaiono affatto in questa coda.** Non sono stati
deprioritizzati: non sono mai stati classificati. Fra questi c'è l'intera serie Aqeilan
locale — `27308416`, `27308504`, `27551470`, `29724996`, `30082886`, `30755385`, `32300104`,
`34831305`, `26256646`, `27550453` — più `21318118`, `22634283`, `23254685`, `31428585`,
`34634460`, `17575124`, `20530675`, `42395553`, `42422765`, `30370248` *(aggiunto il
2026-08-10: mancava da questa lista, vedi la riconciliazione sotto)*.

**Perché conta più dei singoli titoli:** la coda ordina ciò che qualcuno ha pensato di
accodare, non ciò che è in casa. Un paper può stare sul disco in una superficie pulita e
strutturata — cioè nella condizione *migliore* per essere letto, senza sentinella e senza
aggiudicazione — ed essere invisibile alla lista che decide cosa si legge. Oggi
l'intersezione fra "ha una priorità dichiarata" e "ha una superficie strutturata locale"
conteneva **un solo elemento**, ed è il motivo per cui è stato letto 24871327.

**Come è emerso:** cross-query del corpus durante la lettura di FT-039.
**Next action:** classificare i 21, non leggerli — è lavoro di triage, non di lettura.
**Current status:** ⬜ aperto.

### 🔴 Come ho contato — e perché il numero va letto con la definizione accanto (2026-08-10)

Riconciliazione richiesta dopo che due conteggi diversi sullo stesso corpus hanno dato 21 e
19. Non erano in disaccordo sui fatti: erano due domande diverse, e una terza risposta era
sbagliata. Tutte e tre servono a chi legge questa voce dopo.

**Il criterio usato qui è: il PMID compare letteralmente in un blocco `## FT-`.** Stretto,
verificabile con un comando, e insensibile a come un record nomina il suo paper.

| criterio | classificati | non classificati |
|---|---|---|
| PMID letterale in un blocco FT | 19 / 21 | 2 |
| PMID **oppure** cognome+anno del nome file | 20 / 21 | 1 |

**Il 19 è un artefatto di questa voce, e va detto.** Quei 19 PMID hanno un record `FT-`
**perché FT-047 li elenca** — cioè perché li ha elencati la voce che denuncia che non erano
classificati. Prima che FT-047 esistesse il conteggio era **zero su 21**. Un conteggio che si
soddisfa da sé non misura nulla: se qualcuno rilancia la query domani troverà 19 "in coda" e
concluderà che il problema è quasi risolto. Non lo è — sono 19 righe in una tabella di
reclamo, non 19 triage.

**Il criterio largo è peggiore, non migliore: entrambi i suoi due match in più sono falsi.**
- `34747138` → `FT-044`: FT-044 è **PMID 33914858**, Repudi et al. 2021 su *Brain*. `34747138`
  è Repudi et al. 2021 su *EMBO Mol Med*. **Stesso primo autore, stesso anno, due paper
  diversi** — e il secondo ha un record proprio altrove. Cognome+anno non è una chiave.
- `42422765` → `FT-007`: FT-007 è Abudiab et al. 2025, e nomina "Obeid 2026" solo come la
  review che l'ha fatto emergere. Il match cade sulla **citazione della fonte**, non sul paper.

Questo replica esattamente la lezione già scritta in FT-034 — *"un audit di bibliografia con
una sola chiave sovrastima i propri risultati, e li sovrastima nella direzione che lo
lusinga"* — con l'aggravante che qui la seconda chiave non aggiunge copertura: **aggiunge due
falsi positivi**, e li aggiunge nella direzione che fa sembrare la coda più completa.

**E la lista sopra ne aveva persa una.** `PMID 30370248` (Tanna 2018, XML PMC locale) non
compariva né in FT-047 né altrove: l'omissione è stata commessa **dentro la voce che denuncia
le omissioni**, il che è la prova più diretta possibile che l'enumerazione a mano non è
affidabile a questa scala. È aggiunta qui: `30370248`.

**Il conteggio corretto, con la definizione attaccata:** 21 superfici strutturate senza
lettura completa. **Zero hanno una voce `FT-` dedicata al paper**: i 19 compaiono soltanto
nell'elenco di reclamo di questa voce, `30370248` non compariva da nessuna parte fino a oggi,
e `34747138` — l'unico con debito già *misurato*, tre receipt `partial_fulltext_read` — non
ha una voce di coda affatto. Il triage resta interamente da fare, e il numero da citare
quando si dice "quanti sono classificati" è **0 su 21**, non 19.

---

## FT-055 — ✅ APERTA E CHIUSA il 2026-08-10

> **Numerazione:** `048`–`052` sono in uso o in rinumerazione da altri attori, `053`–`054`
> lasciati liberi come stacco. Stessa disciplina dichiarata per `DL-*-085`: l'allocazione qui è
> concorrente e non guardata, uno stacco costa nulla e una collisione costa un
> `BLOCK_BATCH_COMMIT` a chi mergia per secondo.

**Paper:** PMID 39416860 / DOI 10.3389/fped.2024.1453778 — Feng et al. 2024, *Front Pediatr* 12:1453778
**Title:** WWOX-related epileptic encephalopathy caused by a novel mutation in the WWOX gene: a case report
**Surface:** PMID 39416860 · `structured` · PMC11479972, JATS XML, CC BY 4.0 · più il PDF
dell'editore come contenitore della figura.
**Priority:** **ALTA** — non per il paper, per **la premessa che si diceva falsificasse**.

**Perché è stata aperta:** `PMID 42128308` §9 la offre come uno dei tre controesempi che
falsificano il framework genotipo-fenotipo a tre classi — *«a homozygous missense WWOX mutation
(p.Ser304Tyr), in which the patient exhibited rapid clinical deterioration and died in early
infancy, despite the mutation type typically being associated with milder phenotypes»*.
**«Missenso ⇒ funzione residua ⇒ più lieve» è la premessa sotto il ragionamento su ipomorfi e
ASO in questo repository**, quindi un controesempio pubblicato che la uccide vale più di
qualunque paper nuovo.

**Lettura completa**, receipt `FTR-20260810-39416860-01`, manifest
[`PMID39416860.json`](deepdive_manifests/PMID39416860.json) — 11 locator, `MANIFEST STRICT
PASS`. Copertura: testo, Tabella 1 e Figura 1 `read`; **supplementary `unavailable`** (checklist
CARE; PMC 404 sul percorso `bin`, pacchetto OA offerto solo su `ftp://`).

### 🔴 Il verdetto: la premessa NON è falsificata, e la review l'ha presentata come se lo fosse

La zigosità che la review riporta è **accurata**. Quattro cose che la review non porta:

| | |
|---|---|
| **ACMG** | la variante è **«Unclear clinical significance»**, dichiarato **due volte** — prima frase dell'analisi genetica e Tabella 1 |
| **gli autori stessi** | ultima frase: la patogenicità *«require[s] validation through animal experiments and additional cases»* |
| **secondo gene** | `CACNA1A c.4646A>G` p.Gln1549Arg, paterna, eterozigote, contro **DEE-42 autosomica dominante**, anch'essa VUS |
| **coerenza interna** | il paper scrive **c.991C>A** nel testo e in conclusione, **c.911C>A** in Tabella 1 e in discussione |

Sull'ultima, **l'aritmetica decide contro il testo corrente**: il codone 304 copre i nucleotidi
910–912, quindi `c.911` cade nel codone 304 e `c.991` nel codone **331**. Solo `c.911C>A` è
compatibile con `p.Ser304Tyr`. **E la stessa frase sbaglia anche l'amminoacido** — dice *«from
glycine to serine»* stampando `p.Ser304Tyr`, serina→tirosina, nella propria parentesi. Due
errori in una frase, e la metà che propaga a valle è la notazione proteica, cioè quella giusta.

Gli autori argomentano contro il contributo di CACNA1A — il fenotipo DEE-42 non corrisponde
bene, il padre lo porta senza fenotipo — e **l'argomento è ragionevole**. Ma è un argomento, non
una dimostrazione, e un controesempio usato per rovesciare una regola genotipo-fenotipo non può
lasciar cadere in silenzio un candidato concorrente in un gene epilettico dominante.

**Cosa sopravvive, e non è poco:** un bambino omozigote per un missenso WWOX, da genitori
consanguinei (cugini) entrambi portatori eterozigoti, esordio a un mese, nessun inseguimento
oculare, nessun controllo del capo, ipoacusia bilaterale, corpo calloso sottile, EEG
epilettiforme con asincronia interemisferica, **morto a sei mesi**. Come **osservazione
fenotipica** regge qualunque sia la classificazione formale della variante. Ciò che il paper non
può stabilire è che il missenso l'abbia **causata** — ed è il passo che la review compie.

### 🔴 Terza istanza in una sola review della stessa compressione, ora sul lato clinico

`PMID 42128308` dice *«restored»* dove il suo stesso primario mostra dieci volte il wild type;
presenta la rimozione di WPRE come scelta di sicurezza dove il primario mostra un costo di sei
volte la dose; e qui comprime **una VUS con un candidato concorrente** in *«despite the mutation
type typically being associated with milder phenotypes»*. **Tre volte la review enuncia la metà
semplice.** È una proprietà della review, visibile solo leggendo ciò che cita.

### Cosa la figura ha risolto e cosa ha rifiutato di risolvere

Il **trio è interamente nel pannello e solo asserito nel testo**: probando omozigote su lettura
**forward e reverse**, entrambi i genitori eterozigoti per WWOX, **madre wild-type** per
CACNA1A — che è ciò che rende quell'allele esclusivamente paterno.

🔴 **L'aggiudicazione per cui avevo aperto il pannello è fallita, e registrarlo è il risultato.**
Le tracce mostrano che la sostituzione è **C→A**, compatibile con **entrambe** le posizioni
candidate perché entrambe sono C>A: **un cromatogramma non porta una coordinata**. Ho anche
**rifiutato di aggiudicare l'EEG** — una singola epoca rappresentativa non stabilisce la
distribuzione regionale che la didascalia rivendica.

**La rotta della figura è essa stessa un reperto:** PMC dà 404 sul percorso `bin`, il pacchetto
OA è offerto solo su `ftp://`, l'HTML di Frontiers serve `image_m` a **1056×604**. Il PDF
dell'editore porta la stessa figura a **1955×1118, 300 ppi effettivi, `smask = 0`** — 1,85× più
pixel per dimensione. Misurato prima di estrarre, secondo la regola corretta stasera. Leggere
una base Sanger dalla copia servita avrebbe significato leggerla con un terzo dei pixel che
l'editore ha spedito.

**Debito residuo, ed è dove va guardato adesso:** i due controesempi che deciderebbero davvero
la questione — **la delezione dell'introne 4 di Oliver 2023** (categoria 2 per genotipo,
categoria 1 per gravità) e i **sei pazienti prevalentemente missenso di Havali 2021** — restano
non letti. Dopo questa lettura sono loro, e non questo paper, gli elementi di coda di maggior
valore per la premessa ipomorfi/ASO. **Entrambi triageati la sera stessa: vedi `FT-056`.**

---

## FT-056 — 🟡 TRIAGE, NON LETTURA — i due controesempi che decidono la premessa

**Papers:** PMID 34034642 / DOI 10.1080/01616412.2021.1932173 — Havali et al. 2021, *Neurol Res*
· PMID 36779245 / DOI 10.1111/epi.17542 — Oliver et al. 2023, *Epilepsia*
**Priority:** **ALTA** — sono i due che decidono *«missenso ⇒ funzione residua ⇒ più lieve»*,
dopo che `FT-055` ha stabilito che il terzo controesempio non la falsifica.

### 🔴 Havali 2021 — closed access, e lo dichiaro come rotta, non come proprietà

| rotta | risposta letterale |
|---|---|
| `elink pubmed→pmc` | **nessun linkset `pubmed_pmc`** — solo `pubmed_pmc_refs`, che sono articoli *che citano* questo |
| `esummary articleids` | solo `pubmed` e `doi`; **nessun `pmc`** |
| Europe PMC | `isOpenAccess: N` · `inPMC: N` · `hasPDF: N` · *«Subscription required»* |
| Unpaywall | `is_oa: false` · `oa_status: closed` · nessuna `oa_location` |

🔴 **Formulazione deliberata:** *non l'ho potuto recuperare per queste rotte*, **non** *«è
irrecuperabile»*. La lezione del 2026-08-10 mattina è che ho già testato una volta la mia
capacità di recuperare un artefatto e registrato la risposta come proprietà dell'artefatto —
due ritrattazioni poggiavano su quella premessa falsa. Chi ha accesso istituzionale lo prenda.

🔴 **E una trappola nella rotta stessa, che vale oltre questo paper:** `elink` ha restituito tre
`<Id>` e leggerli senza il `LinkName` avrebbe fatto concludere che un deposito PMC esisteva.
Erano `pubmed_pmc_refs`. **Un `<Id>` nella risposta non è un `<Id>` alla domanda che hai fatto.**

### 🔴 Oliver 2023 — già letto il 2026-08-04, e i suoi locator non sono verificabili

`FTR-20260804-36779245-02`, `complete_fulltext_read`. Manifest `PMID36779245.json`: **schema
`None`, 20 locator, ZERO `source_artifacts`**. L'artefatto però **esiste**
(`PMID36779245_Oliver2023_PMC.xml`, 183 753 byte, CC BY-NC-ND). Nessuna rilettura: la regola 7
la ammette solo con `reread_reason`, e qui non serve una rilettura — serve una misura.

**Misurata. E la causa non sono le letture: è la normalizzazione del validatore.**

| variante | verificati |
|---|---|
| il validatore com'è oggi | **7 / 20** |
| + punteggiatura Unicode ripiegata | 9 / 20 |
| elementi inline uniti **senza** spazio | 7 / 20 |
| **entrambe insieme** | **16 / 20** |

Il meccanismo, misurato e non supposto: l'XML contiene `<italic>WWOX</italic>‐DEE` **30 volte**,
e `_xml_surfaces` unisce **ogni** nodo di testo con uno spazio. La superficie estratta legge
quindi `WWOX ‐DEE` (27 occorrenze) e `WWOX‐ DEE` (8) — **uno spazio che l'autore non ha mai
scritto**, fabbricato al confine del markup. Unendo gli elementi inline senza separatore,
`WWOX ‐DEE` passa da 27 a **0** e `WWOX‐DEE` da 0 a **35**.

**Nessuna delle due correzioni basta da sola** — 7 e 7 — e insieme fanno 16. I **4 residui**
falliscono tutti in posizione tarda e su un marcatore di citazione: è una **terza causa
distinta**, probabilmente il contenuto di `<xref>` che la citazione omette e l'estrattore
conserva.

🔴 **Una prima ipotesi era sbagliata e la misura l'ha colta:** avevo attribuito tutto alla
punteggiatura Unicode, che da sola ne recupera **2 su 13**. Registrato perché è il motivo per
cui la seconda ipotesi è stata *testata* invece che asserita.

**Perché conta oltre questo paper:** il nome del gene è in corsivo in ogni rivista, quindi
**ogni citazione che contiene `WWOX-DEE` fallisce, in tutto il corpus** — e il gene attorno a
cui ruota questo repository è il token che più probabilmente rompe un locator. I conteggi
*«not found»* di chi misura la salute del corpus vanno riletti alla luce di questo: **le letture
sono in larga parte sane e il difetto è nel normalizzatore.**

**Controllo sui miei:** 90 locator testuali su sei manifest, **0 portano uno spazio fabbricato**.
Non per merito — le mie catture verificavano contro l'estrattore stesso, quindi uno spazio
fabbricato sarebbe entrato nello snippet e avrebbe *superato* il controllo. Non è successo, ma
la protezione era accidentale.

**Non riparato qui:** è infrastruttura e oggi si legge. La correzione tocca `_xml_surfaces` e
va con la sua batteria di mutazione, perché una normalizzazione troppo aggressiva
nasconderebbe esattamente le sostituzioni stampabili che il sentinella della regola 5d esiste
per trovare.

**Cosa resta da leggere davvero:** il caso dell'introne 4 di Oliver 2023 — categoria 2 per
genotipo, categoria 1 per gravità — **non è fra i 20 locator esistenti**, verificato. Quindi il
paper è letto ma il reperto che serve alla premessa non è catturato. **Fatta la sera stessa:
vedi sotto.**

### ✅ Lettura mirata di Oliver 2023 — `FTR-20260810-36779245-03`, `partial_fulltext_read`

`reread_reason: inadequate_prior_coverage`. Lette: metodi 2.4, risultati 3.6 e 3.7, Tabella 3 e
la discussione corrispondente. **Le sezioni non toccate sono dichiarate `not_read`**, non
ereditate dal receipt precedente. Nove citazioni verificate uniche contro il corpo estratto, e
**sette di nove anche nel markup grezzo** — scelte deliberatamente per non attraversare un
confine di corsivo, così sono verbatim in entrambi i sensi e non solo rispetto all'artefatto
dell'estrattore.

#### 🔴 La risposta è più grande della domanda: la classe centrale del framework non esiste nei dati della fonte che l'ha costruita

Lo schema a tre classi **è di Oliver**: *«classified into three genotypic classes based on
variant types: (1) null/null, (2) null/missense, (3) missense/missense»*. E la conclusione di
Oliver è:

> *«We found no difference between individuals with one or two missense variants and therefore
> no evidence to support an "intermediate" phenotype»*

La review `PMID 42128308` presenta la classe 2 come *«associated with intermediate phenotypes»*
e poi offre controesempi a un framework **la cui stessa fonte nega quella classe**. Non è un
controesempio dentro il framework: è **la fonte del framework che ne smentisce un terzo**.

#### Ciò che i dati sostengono è binario, non ternario, e su un asse solo

75 casi: null/null n=45 · null/missense n=15 · missense/missense n=15.

| asse | risultato |
|---|---|
| **tempo alla morte** | *«survival was much poorer for the double null group compared with the patients who had at least one missense pathogenic variant»* — **p = .0085** log-rank; sopravvivenza a 5 anni **<50%** contro **>75%**; a 10 anni **25%** contro **>60%** |
| **tempo all'esordio delle crisi** | *«we found no difference in time to seizure onset between the three genetic groups»* — **p = .65** |

Il paper stesso raggruppa le due classi missenso come *«the other two, presumably less severe,
genetic groups»*: **una divisione binaria, scritta come tale.**

#### 🔴 Il caso introne 4 — ed è la review a sbagliarne la classe

Paziente 6 è tabulato `c.49G > A, p.Glu17Lys (mat)/intron 4 deletion (pat)` con combinazione
genetica **`Missense/null`**: Oliver classifica la delezione dell'introne 4 **come null**,
perché *«the intron 3 deletion was a benign variant, whereas the intron 4 variant resulted in
exon 5 skipping»*. È dunque **un ordinario caso di classe 2 secondo la codifica di Oliver**, non
un'anomalia. La review lo descrive come un caso che *«technically falls under category 2 … with
one allele lacking a canonical deletion mutation»* la cui gravità eguagliava la categoria 1 —
ma in uno schema dove la classe 2 **non mostra alcun fenotipo intermedio**, un paziente di
classe 2 grave quanto la classe 1 è **il risultato atteso, non un controesempio**.

#### 🔴 E «missenso» non è affatto una classe di gravità — la risposta profonda alla premessa

> *«p.Pro47 has been associated with two pathogenic variants; the more conservative change to
> threonine was found in SCAR12»* — contro la sostituzione ad arginina trovata in WWOX-DEE.

**Lo stesso residuo, due sostituzioni, due malattie.** E *«no region of the gene emerged as
specific»* per DEE contro SCAR12: le due varianti missenso SCAR12 stanno **vicine** a varianti
DEE. La gravità è **specifica della sostituzione**, non del residuo e non della regione: quindi
*«missenso ⇒ funzione residua ⇒ più lieve»* fallisce **al livello della propria categoria**.

Chiude un anello con `FT-045`: **P47T** è l'allele del modello murino SCAR12 che tiene la
proteina WWOX **a livello wild type** disattivando il motivo PPXY della WW1.

#### Due dati che atterrano qui dentro

- **`p.Gln230Pro` è l'allele missenso WWOX-DEE più ricorrente della letteratura**: tre dei dodici
  pazienti non imparentati di Oliver — omozigote in due, eterozigote composto in uno — più **sei
  famiglie già riportate** da Iran, Afghanistan, Francia e Marocco. È l'allele attorno a cui è
  costruito il lavoro di proteostasi di questo repository.
- **Ascertainment, dichiarato dal paper:** la loro coorte è più anziana (media 8a 2m contro 3a
  4m) e meno letale (23% contro 38%) della letteratura con cui è messa in pool, con null/null al
  50% contro 60%. È una ragione per leggere la curva di sopravvivenza **come confronto fra
  gruppi**, non come prognosi assoluta.

#### 🔴 Perché queste nove citazioni non sono nel manifest

`PMID36779245.json` è schema `None` con zero artefatti, e 13 dei suoi 20 locator falliscono per
la causa misurata sopra. **Dichiarare l'artefatto e alzare lo schema porterebbe quei 13 da
"non verificati" a FAIL duro** — è lavoro di un altro attore e non sta a me romperlo. Le
citazioni stanno nel receipt, verificate, **pronte ad atterrare quando il normalizzatore sarà
riparato**, che è di Plan.

---

## FT-057 — 🔴 NOVE REFERENZE WWOX-DIRETTE CHE LA CODA NON AVEVA MAI VISTO

**Papers:** PMID 30356099 · PMID 25411445 · PMID 29808465 · PMID 30158849 · PMID 17823927 ·
PMID 16941225 · PMID 25403906 · PMID 25416187 · PMID 17163164
**Origine:** multi-hop di `FT-002` (`PMID 32581702`), svolto il 2026-08-10.
**Priority:** **ALTA** — due di queste sono i maggiori lavori di coorte WOREE del campo.

**Come sono emerse, e perché è un reperto e non un elenco.** Avevo scritto `references:
not_read` sulla ricevuta di una lettura completa. **Il writer del ledger l'ha rifiutato** — una
lettura completa non può lasciare una sezione non letta. Enumerare la `<ref-list>` JATS è
costato due minuti: **50 referenze, 49 con PMID, 22 WWOX-dirette.** Incrociate contro ogni
ricevuta di tutti e sei i rami e contro questa coda, **nove non esistono da nessuna parte**.

🔴 **Il rifiuto ha prodotto più della scorciatoia.** Non è un aneddoto: è la misura di quanto
costa dichiarare aperto un debito invece di chiuderlo. Due minuti contro nove paper invisibili
al piano di lettura.

| PMID | lavoro | perché conta |
|---|---|---|
| **30356099** | Piard 2018 — *The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome* | **la coorte WOREE più grande del campo.** `FT-002` la cita per il dato «segni antenatali fino al 25% dei casi» |
| **25411445** | Mignot 2015 — *WWOX-related encephalopathies: delineation of the phenotypical spectrum* | il lavoro che **ha definito lo spettro**. Citato come fonte delle varianti nonsenso/frameshift severe |
| **29808465** | Johannsen 2018 — *A novel missense variant in the SDR domain leads to complete loss of WWOX protein* | 🔴 **CHIUSO COME NON RECUPERABILE PER QUESTE ROTTE — vedi sotto.** Regge **47 citazioni in 7 file canonici** |
| 30158849 | Liu 2018 — *WWOX phosphorylation, signaling, and role in neurodegeneration* | asse neurodegenerazione, *Front Neurosci* |
| 17823927 | Ludes-Meyers 2007 — topi ipomorfi per WWOX | modello ipomorfo, non nullo — la classe che manca al confronto |
| 16941225 | Nunez 2006 — *WWOX protein expression in normal human tissues* | la mappa di espressione basale su cui poggiano gli argomenti tissutali |
| 25403906 | Ben-Salem 2015 — delezione di un intero esone | fenotipo antenatale |
| 25416187 | Tabarki 2015a — *The fragile site WWOX gene and the developing brain* | |
| 17163164 | Ramos & Aldaz 2006 — WWOX come gene di sito fragile nel cancro | parità delle fonti: oncologia |

**Stato delle altre 13, per completezza:** già lette integralmente `19500159`, `24871327`,
`30370248`, `31340538` · ricevuta parziale `24369382`, `24456803`, `24932569` · in coda non lette
`11719429` (`FT-020`… no: da verificare), `15026124` (`FT-023`), `17360458`, `25716914`
(`FT-030`), `26345274`, `31543760` (`FT-005`).

**Preflight di superficie: NON ancora eseguito su queste nove.** Va fatto come primo gesto,
prima di aprire qualunque PDF, e l'esito va registrato in entrambi i casi.

**Next action:** preflight strutturale sulle nove → poi `30356099` e `25411445` per prime, perché
sono le coorti su cui ogni ragionamento genotipo-fenotipo di questo modello si appoggia.

### 🔴 29808465 — tentato per primo, la sera stessa. Chiuso, e il reperto non è quello atteso

Ricevuta `FTR-20260810-29808465-01`, `abstract_only` — **non salda alcun debito di lettura**, ed
è depositata esattamente perché nessuno la scambi per una lettura.

**Rotte esaurite** (*non l'ho potuto recuperare per queste rotte*, **non** «è irrecuperabile»):

| rotta | risposta letterale |
|---|---|
| Europe PMC | `pmcid: null` · `inPMC: N` · `inEPMC: N` · `isOpenAccess: N` · `hasPDF: N` · solo link DOI *«Subscription required»* |
| NCBI idconv | *«Identifier not found in PMC»* |
| Unpaywall `10.1007/s10048-018-0549-5` | `is_oa: false` · `oa_status: closed` · `has_repository_copy: false` · `oa_locations: []` |
| `files/fulltext/` locale | assente |

🔴 **Quindi le 47 citazioni non sono la disattenzione di nessuno: il paper non è mai stato
disponibile a chi lo citava.** Il dato è entrato dall'abstract, che è dove sta.

🔴 **E lo stato canonico lo ha trattato meglio dell'allarme che avevo suonato.** Verificato, non
assunto: `disease_model.md` registra un'**inversione MAJOR `WM v2.1 → v3.0`** che *ritira*
l'equazione `mRNA normale + proteina assente = degradazione`; `DL-MECH-034` porta la causa come
**non discriminata**; è annotato che l'assenza al western è *«un limite di sensibilità, non uno
zero assoluto»* e che *«un fibroblasto non è un neurone»*. **Una premessa importata da un
abstract è stata qualificata meglio di molte importate da letture complete.**

**Il difetto che resta è la classe di evidenza, e siede su un rifiuto:** `DIS-003` dichiara
`PREMISE: DATO (direct measurement, exact variant)` — *direct measurement* di una misura che
nessuno qui ha visto. Dettaglio completo e riclassificazione proposta (non applicata) in
`DL-META-091`, correzione append-only.

**Il recupero a più alto rendimento di questa coda** *(vedi anche `FT-058`)*. Chi ha accesso Springer prenda il PDF e
guardi **il western**: quante corsie, quale controllo di caricamento, quale esposizione, se il
segnale è assente o sotto soglia, e se la qRT-PCR è su un solo amplicone. Dalla risposta dipende
se il collo di bottiglia sia **traduzione** o **degradazione** — e se fosse traduzione, *non c'è
niente da stabilizzare*, cioè la traccia proteostasi indirizzerebbe uno solo dei due rami che
l'autore stesso lascia aperti.

---

## FT-058 — Breton 2021, elettrofisiologia della neocorteccia: ✅ LETTO, e la ricevuta del 26 luglio non era una lettura

**Paper:** PMID 34634460 / DOI 10.1016/j.nbd.2021.105529 — Breton et al. 2021, *Neurobiol Dis*
160:105529 ([[paper_registry_current#PAPER 031]])
**Title:** Altered neocortical oscillations and cellular excitability in an in vitro Wwox
knockout mouse model of epileptic encephalopathy
**Surface:** `structured` · PMCID `PMC8609180`, JATS XML, CC BY ·
`PMID34634460_Breton2021_PMC.xml` · sei figure in `files/figures/PMID34634460/`
**Priority:** **ALTA** — è la fonte di `CLAIM 021` e l'unico strato cellulare fra il gene e la
fenomenologia epilettica.

**Current status:** ✅ **LETTO INTEGRALMENTE il 2026-08-10** — receipt `FTR-20260810-34634460-02`,
`complete_fulltext_read`; manifest `PMID34634460.json`, **21 locator**, `MANIFEST STRICT PASS`
sotto entrambi i validatori. Copertura pannelli **29/29**, budget dichiarato prima.

### 🔴 La ricevuta precedente diceva `partial_fulltext_read`. Non era una lettura parziale

`FTR-20260726-34634460-01` ha `source_locator` che punta al **paper registry**, non a un
documento; **nessuna impronta**; tutti e nove gli slot di copertura a `unknown_legacy`. La sua
base dichiara: *«PAPER 031 declares Evidence depth: full text verificato
(`files/fulltext/PMID34634460_Breton2021.md`, PMC MCP)»* — l'autorità viene da un **markdown
prodotto da un convertitore ML**, cioè la classe di superficie che la regola 5c vieta come
artefatto dietro un locator, e quel file oggi non è su disco.

🔴 **Leggere la ricevuta prima del documento è ciò che l'ha fatto emergere.** «Parziale dal 26
luglio» si legge come una lettura che si è fermata; era una ricostruzione che non era mai
cominciata. `reread_reason: inadequate_prior_coverage` — non c'era copertura da giudicare.

### Cosa hanno dato i 29 pannelli

| reperto | dove |
|---|---|
| 🔴 il bloccante della pannessina **alza la frequenza dei burst ~2,5×**; Results dice *«not recapitulated»*, Discussione *«minimal effect»* | entries[2], [3] |
| 🔴 convenzione degli asterischi **invertita in Fig 3** (`*`=0.0036, `**`=0.0274) e ordinaria in Fig 6 — stesso paper | entries[4], [20] |
| 🔴 effetto eccitatorio **+6%** (23,3→24,7 pA) contro inibitorio **−52%** (57,3→27,5); l'abstract li elenca al contrario | entries[6], [7], [18] |
| 🔴 eterozigoti al **17%** delle slice contro **86%**; la Discussione dice *«manifested similarly»* | entries[0], [1] |
| 🔴 `ch?` — segnaposto pubblicato, nel pannello della dissociazione ippocampo/neocorteccia | entries[10] |
| 🔴 asse di Fig 2C: `100, 0, 100, 200` — manca il meno, ed è il pannello che definisce il **segno del lag** | entries[11] |
| 🔴 didascalia di Fig 5D dice *«No significance»*, il pannello stampa `p = 0.0312` con asterisco | entries[19] |
| resistenza d'ingresso **satura a un allele** (143,26 HT vs 143,03 KO) mentre RMP e sag graduano | entries[15] |

**A 101 ppi ho letto male il pannello 3D e il ritaglio l'ha corretto** — avevo attribuito al CBX
un aumento di frequenza che è l'opposto del risultato. Le figure sono servite a un terzo dei ppi
del paper precedente; sei pannelli ritagliati a risoluzione nativa e ingranditi 6×–10×.

**Supplementari:** `unavailable` — `mmc1.docx` non recuperabile dalla rotta PMC. Pesa: `S4` è la
curva frequenza-corrente su cui poggia il negativo centrale del paper.

**Debito generato:** una sola referenza gene-diretta né letta né in coda — **`PMID 26499798`**,
Abu-Remaileh 2015, *Pleiotropic functions of tumor suppressor WWOX*, JBC. Che sia una e non nove
è la misura di `FT-057`: novanta minuti prima aveva già assorbito Mignot 2015 e Piard 2018, che
anche questo paper cita.

---

## FT-059 — Steinberg 2021, organoidi: 🟡 superficie recuperata, **69 pannelli da leggere**, lettura NON iniziata

**Paper:** PMID 34268881 / DOI 10.15252/emmm.202013610 — Steinberg et al. 2021, *EMBO Mol Med*
([[paper_registry_current#PAPER 039]])
**Title:** Modeling genetic epileptic encephalopathies using brain organoids
**Surface:** `structured` — 🔴 **esisteva e non era stata recuperata.** `PMC8350905`, CC BY,
`isOpenAccess: Y`, mentre sul disco c'era solo `PMID34268881_Steinberg2021.pdf`. Recuperata il
2026-08-10: `PMID34268881_Steinberg2021_PMC.xml`, 265 997 byte,
`sha256 de340289bc6704c9…`. *Il preflight non è «cercare e non trovare»: qui era «esiste, non
ce l'abbiamo», che è un'azione.*
**Priority:** **ALTA** — sostiene `DL-MECH-034` a `DATO`, cioè il razionale WWOX-specifico
della dieta chetogenica.

**Current status:** 🟡 **LETTURA MIRATA E DICHIARATA PARZIALE il 2026-08-10** — receipt
`FTR-20260810-34268881-02`, `partial_fulltext_read`, `reread_reason:
new_question_outside_prior_coverage`. Letta **solo** la sottosezione RNA-sequencing dei Results.
Abstract, introduzione, metodi, discussione, referenze **non letti**; figure `captions_only`;
nove elementi supplementari **non recuperati**.

🔴 **La lettura completa non è stata iniziata, deliberatamente.** Il budget è **11 figure e 69
pannelli** — il più grande di questo corpus. Cominciarla in coda a una sessione lunga e
abbandonarla è il costo che questo repository ha già pagato quattro volte. È specificata qui
invece che lasciata a metà.

### 🔴 Il conteggio dei pannelli: 69, non 17

Il mio contatore aveva detto **17** e non aveva segnalato nulla. EMBO marca i pannelli come
`<list-item>` nella didascalia, non con lettere nel testo: un contatore che cerca lettere ne
trova quasi nessuna e restituisce un numero piccolo e plausibile. Contando i `list-item`:

    EV1 10 · Fig 1 6 · Fig 2 6 · Fig 3 6 · EV2 8 · EV3 6 · Fig 4 8 · Fig 5 5 · Fig 6 6 · EV4 4 · EV5 4  =  69

**Terza volta oggi della stessa forma nel mio strumentario** — dopo l'incrocio referenze che
stampava tre categorie vuote uscendo con 0. *Un conteggio che non può sembrare sbagliato non è
un conteggio.* Chi fa la lettura completa parta da 69.

### La ricevuta precedente è un'altra delle ventitré del 26 luglio

`FTR-20260726-34268881-01`: `source_locator` sul **paper registry**, nessuna impronta, tutti gli
slot `unknown_legacy`, `workflow: public-registry-legacy-reconstruction`. La sua base registra
che **PAPER 039 dichiara `coverage_status: complete_fulltext_read`** — quindi il registry
rivendica una lettura completa e il ledger contiene una ricostruzione. È il disallineamento che
il ratchet `registry_only_fulltext_declarations` conta, visto dall'interno.

### Cosa ha prodotto la lettura mirata

`DL-MECH-094` — la firma OXPHOS↓/glicolisi↑ è **confusa con il difetto di differenziamento** che
il paper dichiara nel titolo della sezione da cui il dato proviene. Conseguenza operativa: un
Seahorse su KO contro WT alla stessa settimana **riprodurrebbe il confondimento**; l'esperimento
va appaiato per **stadio di differenziamento**, non per età di coltura.

### 🔴 Secondo preflight — quello sulle FIGURE, che è una domanda diversa dalla prima

*«Superficie strutturata trovata» non implica «migliore superficie figure trovata».* Misurato:

| sorgente | figure | larghezza | ppi effettivi @7in | `smask` |
|---|---|---|---|---|
| CDN PMC (`cdn.ncbi.nlm.nih.gov/pmc/blobs/…`) | 12 file | 585–712 px | **84–102** | — |
| **PDF locale** `PMID34268881_Steinberg2021.pdf` | **6** immagini >40 kpx | 1213–1419 px | **173–203** | **0** su tutte e sei |

🔴 **Il PDF locale è la superficie figure migliore, di un fattore 2.** E `smask = 0` su tutte
significa che `extract_image()` restituisce ciò che la pagina mostra — la condizione stabilita
il 2026-08-10 mattina. **Il PDF resta però solo superficie FIGURE:** il testo continua a venire
dall'XML, che è la superficie della regola 5d. Le due cose non si mescolano.

**A 84–102 ppi la lettura dei 69 pannelli non è fattibile:** un pannello di `EV1` sarebbe
~200×180 px. Chi apre `FT-059` estragga le figure dal PDF, non le scarichi dal CDN.

### 🔴 I supplementari sono dietro un controllo anti-automazione, e non l'ho aggirato

`/articles/instance/8350905/bin/EMMM-13-e13610-s00N.*` restituisce `200` con una pagina
*«Preparing to download…»* che porta un **challenge proof-of-work** (`cloudpmc-viewer-pow`,
`POW_DIFFICULTY 4`, cookie `cloudpmc-viewer-pow`). **Risolverlo sarebbe aggirare un controllo di
accesso che l'operatore del servizio ha messo deliberatamente. Non è stato fatto.** La rotta è
registrata con la sua risposta letterale; chi ha accesso da browser scarichi gli otto file a
mano — sono `s001.pdf` (Expanded View Figures), `s004.docx` (Appendix), `s002/003/005/006/008.xlsx`
(Table EV1–EV5), `s007.pdf` (Review Process File).

🔴 **Conseguenza sul budget, ed è pesante:** le cinque figure EV — `EV1 10 · EV2 8 · EV3 6 ·
EV4 4 · EV5 4` = **32 dei 69 pannelli** — vivono nell'Expanded View PDF, cioè **dietro quel
controllo**. Le sei figure principali (37 pannelli) sono nel PDF locale. Senza `s001.pdf` la
copertura massima raggiungibile è **37/69**, e va dichiarata come tale invece che presentata
come completa.

**Next action:** ① procurarsi `s001.pdf` e `s004.docx` per via manuale — la `Appendix Fig S3A/B`
**è** l'output GSEA/GO su cui poggia `DL-MECH-034` e anche `DL-MECH-094`; ② estrarre le sei
figure principali dal PDF locale a 173–203 ppi; ③ lettura completa partendo da Fig 4 ed EV3
(RNA-seq) e da Fig 2 (iperreccitabilità, confrontabile con `FT-058`). **Se ② e ③ partono senza
①, dichiarare `figures: read` su 37/69 e `supplementary: unavailable` con questa rotta citata.**
