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
**Surface:** PMID 32581702 · `absent`
**Priority:** HIGH
**Why:** core prenatal migration/cortical layering paper
**Current status:** cited in meta, not yet deeply extracted
**Next action:** full text deep extraction

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

## FT-045
**Paper:** PMID 42128308 — Aqeilan 2026, *Neurobiol Dis*
**Title:** WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities
**Surface:** PMID 42128308 · `pdf_only` · sentinella `clean` · PMID42128308_Aqeilan2026.pdf
**Priority:** **MEDIA**
**Why:** review di sintesi del leader del campo sull'asse cervello; utile come mappa delle
posizioni correnti del gruppo, non come fonte primaria di dati.
**Come è emerso:** corpus Aqeilan RI, coda 2026-08-08 (posizione 3, il più recente dopo i due
2026 primari).
**Current status:** ⬜ **MAI APERTO — NESSUNA LETTURA È AVVENUTA.** Va detto con precisione,
🔴 **e va detto anche che il ledger sembra dire il contrario:** esiste
`FTR-20260726-42128308-01`, `partial_fulltext_read`, del 2026-07-26. Non è una contraddizione,
è un `record_kind: legacy_reconstruction` — un receipt costruito da una dichiarazione di
registry, non da una lettura. Il ledger e questa voce dicono la stessa cosa in due vocabolari,
e senza questa riga la prossima sessione avrebbe dovuto scoprirlo da sola.
perché è diverso da una lettura che non produce affermazioni: il documento non è mai stato
aperto in alcuna sessione, non esiste testo estratto, non esiste receipt e non esiste
rinuncia argomentata da scrivere — non c'è lettura su cui argomentare. L'artefatto è presente
e fingerprintato (`PMID42128308_Aqeilan2026.pdf`, 17 pp., 7 immagini, SHA-256
`520c2743630b86e5e6c2af7a3e2f527d7a31ab7810839ed275c87b0d804d6be7`).
**Debito:** interamente aperto. È un PDF, quindi al momento della lettura va prima cercata una
superficie XML/HTML PMC e, se non esiste, applicato il sentinella sulla superficie testuale
prima che qualunque locator vi poggi.

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

## FT-048
*Discrepanza interna in PMID 30755385, da risolvere alla fonte.*
**Paper:** PMID 30755385 / DOI 10.1016/j.molmet.2019.01.010 — AbuRemaileh et al. 2019, *Mol Metab*
**Title:** Loss of Wwox in skeletal muscle — ITT age discrepancy between Figure 2 caption and Methods
**Surface:** PMID 30755385 · `structured` · sentinella `clean` · PMID30755385_AbuRemaileh2019.pdf, PMID30755385_AbuRemaileh2019_PMC.xml
**Priority:** **MEDIA**
**Why:** la didascalia della Figura 2 data l'ITT a **10 mesi**, la sezione Methods 4.4 a **6
mesi**. Non è una svista tipografica indifferente: l'insulin tolerance test è la misura da cui
dipende l'interpretazione metabolica sistemica, e quattro mesi in un modello murino sono una
finestra di malattia diversa. Finché non è risolta, qualunque uso quantitativo di quella
figura porta con sé un'incertezza di età che nessuna citazione a valle riporterebbe.
**Come è emerso:** dal **rapporto di lettura** di una seconda sessione su PMID 30755385, non
dalla lettura stessa — cioè da qualcuno che ha confrontato didascalia e Methods invece di
leggerli in sequenza. Vale la pena registrarlo come metodo: le discrepanze interne non si
vedono leggendo, si vedono confrontando.
**Next action:** risolvere alla fonte — corrispondenza con gli autori o erratum — prima che la
figura sostenga un'affermazione quantitativa. Nel frattempo, chi la cita dichiara entrambe le
età.
**Current status:** ⬜ aperta. Il paper è letto (`FTR-20260810-30755385-01`); è la discrepanza
a non essere risolta, non la lettura.

---

## FT-049
*🔴 `INFERENZA`: il tessuto di misura non è il tessuto di necessità.*
**Papers:** PMID 24871327 · PMID 34747138 · PMID 30755385 — le tre fonti che la sostengono
**Title:** Un fenotipo misurato nel sangue o a livello sistemico non identifica il tessuto in cui la lesione causale risiede
**Surface:** PMID 24871327 · `structured` · sentinella `clean` · PMID24871327_Iatan2014_PMC.html  ·  PMID 34747138 · `structured` · sentinella `clean` · PMID34747138_Repudi2021_PMC.xml  ·  PMID 30755385 · `structured` · sentinella `clean` · PMID30755385_AbuRemaileh2019.pdf, PMID30755385_AbuRemaileh2019_PMC.xml
**Priority:** **ALTA** (è una regola di lettura, non un singolo studio)
**Epistemic status:** **`INFERENZA`** — convergenza di tre osservazioni indipendenti, mai
dimostrata come principio nel contesto WWOX. Non è `DATO` e non va citata come tale.
`PREMISE: DATO` per ciascuna delle tre osservazioni; `PREMISE: INFERENZA` per la
generalizzazione.
**Why:** le tre fonti si dispongono in una figura che nessuna di loro afferma da sola.

| Fonte | Osservazione | Direzione |
|---|---|---|
| Iatan 2014 (PMID 24871327) | il KO **epatico** di *Wwox* **non** abbassa l'HDL plasmatico | il tessuto ovvio non è quello necessario |
| Repudi 2021 (PMID 34747138) | il restauro **neuronale-only** (AAV9-hSynI) recupera fenotipi **periferici**, ipoglicemia inclusa | il tessuto di necessità può stare a monte del compartimento misurato |
| AbuRemaileh 2019 (PMID 30755385) | il KO **muscolare** produce un fenotipo **sistemico** | un compartimento non ovvio basta a generare la misura sistemica |

**Perché conta qui e non altrove:** il modello di malattia ragiona su marcatori periferici —
lipidi, glucosio, BUN/creatinina — come se il compartimento in cui si misurano indicasse dove
agire. Queste tre letture dicono che non lo indica. Vincola direttamente la scelta dei
biomarcatori Tier 1/2 (un marcatore ematico può essere valido come *readout* ed essere muto
sul *bersaglio*) e la logica di targeting terapeutico.
**Come è emersa:** dal rapporto di una seconda sessione su PMID 30755385, che ha messo in fila
tre letture separate. 🔴 **Non esisteva in alcun file canonico** — né claim registry, né
working model, né meta — pur essendo sostenuta da tre paper già letti. È il tipo di perdita
che il sistema è costruito per non subire: tre `DATO` in casa e l'inferenza che li unisce in
nessun posto interrogabile.
**Next action:** promuoverla via commit candidate → `BATCH_COMMIT`, come `INFERENZA` esplicita
nel claim registry o in [[meta_metabolism_current]], con le tre fonti wikilinkate. **Non può
salire a `DATO`** senza un esperimento che testi la dissociazione compartimento/necessità in
modo diretto.
**Current status:** ⬜ registrata qui perché interrogabile subito; canonicamente **non**
promossa — `batch_commit_gate` è chiuso.

---

## FT-050 — Supplementary di PMID 38182577: il debito che tiene la lettura a `partial`
*(🔴 **Rinumerata da FT-046 il 2026-08-10.** Aperta su `lettore-b` con un ID che `main` aveva
già assegnato a un'altra voce: due rami hanno preso lo stesso numero libero perché entrambi
avevano contato, non letto, la coda. Il receipt `FTR-20260810-38182577-02`, già nel ledger a
catena hash, cita questa voce come **FT-046**: il ledger non si riscrive, quindi il collegamento
è dichiarato qui.)*
**Paper:** PMID 38182577 / DOI 10.1038/s41419-023-06378-8 — Akkawi 2024 — *WWOX promotes
osteosarcoma development via upregulation of Myc*
(⚠️ titolo invertito rispetto al proprio contenuto — vedi `DL-METH-079`).
**Priority:** MEDIUM-HIGH
**Artefatto:** già in locale e fingerprintato —
`files/fulltext/PMID38182577_Akkawi2024_assets/41419_2023_6378_MOESM1_ESM.pdf`
(SHA-256 `bf64e0e7133a…`), più `MOESM2_ESM.pptx` non aperto.
**Perché è debito e non rifinitura:** il corpo e le sette figure principali sono letti
(`FTR-20260810-38182577-01`), ma i pannelli **S1–S5 non sono stati adjudicati**, e uno di essi
è portante: la claim *"Trp53 SKO yBM is not tumorigenic"* — cioè il contrasto che regge
l'intero modello a due colpi — poggia su **Fig S5A,B**. Finché quel pannello non è letto, il
contrasto DKO-vs-SKO è sostenuto dal testo e non dalla figura.
**Perché la lettura è `partial_fulltext_read`:** lo scrittore del receipt ha **rifiutato**
`complete_fulltext_read` con `coverage.supplementary: not_read`, e ha fatto bene. Una prima
stesura del manifest dichiarava "Coverage: complete"; è stata corretta.
**Next action:** ~~adjudicare S1–S5 come immagini a risoluzione originale, poi ri-registrare a
profondità completa con `reread_reason: inadequate_prior_coverage`.~~ **Fatto.**
**Current status:** ✅ **CHIUSO** — `FTR-20260810-38182577-02`, `complete_fulltext_read`.

---

## FT-051 — Supplementari di PMID 38499540, e la lezione applicata invece che ripetuta
*(Rinumerata da FT-047 il 2026-08-10, stessa collisione di `FT-050`. Il receipt
`FTR-20260810-38499540-01` la cita come **FT-047**.)*
**Paper:** PMID 38499540 / DOI 10.1038/s41420-024-01878-8 — Bidany-Mizrahi 2024 — *Unveiling
the relationship between WWOX and BRCA1…*
(⚠️ tre didascalie su sei invertite rispetto ai propri pannelli — vedi `DL-METH-081`).
**Priority:** MEDIUM
**Da recuperare:** `MOESM1-4` (tre `.pptx`, un `.docx`) — **non ancora scaricati**.
**Perché è debito dichiarato e non una svista:** `Supplementary Fig. 1` è citata nel corpo per
il confronto foci tumore-contro-normale, e non è stata adjudicata. La lettura è quindi
`partial_fulltext_read` (`FTR-20260810-38499540-01`) **per dichiarazione, non per omissione** —
la stessa forma che oggi, su `FT-050`, ha corretto due mie coppie di contraddizione. Registrarlo
subito costa una riga; scoprirlo dopo costa la lettura due volte.
**Next action:** recuperare i quattro supplementari, adjudicare S1, ri-registrare a profondità
completa con `reread_reason: inadequate_prior_coverage`.
**Current status:** ⬜ aperto.

---

## FT-052 — PMID 25331887, e la premessa con cui l'ho accodato era sbagliata
*(Rinumerata da FT-048 il 2026-08-10, stessa collisione di `FT-050`.)*
**Paper:** PMID 25331887 / DOI 10.1073/pnas.1409252111 — Abu-Odeh 2014 *PNAS* — *WWOX, the
common fragile site FRA16D gene product, regulates ATM activation and the DNA damage response*
**Priority:** HIGH
**Perché — versione originale, conservata perché è l'errore:** *«38499540 conclude che i suoi
risultati in vivo "correspond with previous in vitro findings" citando questo lavoro. La
direzione WWOX→NHEJ nel modello murino è quindi ancorata a una fonte non letta.»*
🔴 **Falso, e la lettura lo ha dimostrato.** La frase *«correspond with previous in vitro
findings»* cita **[17], [38], [39]** — nessuno dei quali è questo paper. `25331887` è il
riferimento **[36]**, citato per l'asse ATM insieme a [35], e nella Discussione è nominato
**come conflitto**: *«In contrast, a previous paper by Abu-Odeh and colleagues, has shown that
WWOX enhances HDR in U2OS cells [36]»*. Il DOI che avevo scritto era inventato
(`1409753111`); quello vero è `1409252111`. Il `multihop` del manifest di 38499540 mappava
questo PMID ai rif. 17 e 34: entrambi corretti nello stesso commit.
**La forma dell'errore è quella di tutta la giornata, un piano più su:** avevo attribuito una
citazione a una frase senza leggere il numero che la frase porta. È lo stesso difetto che
l'audit `cited_panel_check` cerca fra testo e pannello, qui fra testo e bibliografia.
**Perché valeva leggerlo lo stesso, e di più:** il conflitto è reale, è **dichiarato dagli
autori**, e i due lavori hanno lo stesso autore senior. E il pannello aggiunge ciò che la
spiegazione pubblicata non dice — vedi `DL-METH-084`.
**Artefatto:** superficie strutturata acquisita dalla sweep del 2026-08-10
(`PMID25331887_AbuOdeh2014_PMC.html`), più il PDF locale usato **solo** come contenitore di
immagini per estrarre le sette figure alla risoluzione depositata.
**Current status:** ✅ **CHIUSO** — `FTR-20260810-25331887-01`, `partial_fulltext_read`
(supplementary irrecuperabile, vedi `FT-053`). Manifest strict PASS, 29 locator.
S1–S5 resi dal PDF sorgente a 220 dpi e ispezionati come immagini; la ricetta di rendering
(digest sorgente · pagina · dpi · digest immagine) è nel manifest sotto
`supplement_page_renders`, così un lettore con la propria copia rigenera byte identici senza
che il repository ridistribuisca le figure dell'editore.
🔴 **Il debito non era formale, e vale registrarlo perché la prossima volta si creda al gate:**
il supplementary ha **corretto due coppie di contraddizione di questo stesso manifest**, in
entrambi i casi perché avevo confrontato una frase con una figura principale che la frase
**non cita** — `Fig 4D` invece di `S5B`, `Fig 4A` invece di `S4D`. E ha prodotto quattro
reperti che esistono solo lì, fra cui **due conteggi di tumorigenicità incompatibili per lo
stesso genotipo** (12/28 in Fig 4D contro 11/21 in S5B) e **MCM7 che non è più alto** nel
pannello che il testo cita per dirlo. Lo scrittore della receipt aveva ragione a rifiutare
`complete` al primo passaggio.

---

## FT-053 — Il supplementary di PMID 25331887 non è irrecuperato: è **irrecuperabile** dalle vie sancite
**Paper:** PMID 25331887 / DOI 10.1073/pnas.1409252111 — Abu-Odeh 2014 *PNAS*
**Priority:** ~~MEDIA-ALTA~~ → **ALTA**, elevata il 2026-08-10 a fine sessione.
🔴 **Perché è salita, e non per rifinitura:** dopo il ri-audit in coda a `DL-MECH-083`, la
**stabilizzazione** di WWOX da parte della catena K63 è ritaggata `PREMISE: NON RISOLTA` — e la
sua unica evidenza è **`Fig S7B`**, che sta esattamente in questo supplementary. È la premessa
più consequenziale della catena K63/ITCH/K274, quella che decide se `DL-MECH-083` sia un `DATO`
o un'inferenza, e il repository **non può raggiungerla** per le quattro vie documentate sotto.
Non è un fallimento: è un debito localizzato al pannello, che è il massimo ottenibile quando
manca l'accesso. Ma vale ora quanto una lettura mancante, non quanto una figura non adjudicata.
**Che cosa manca:** `pnas.201409252SI.pdf`, figure **S1–S7**. Non è rifinitura: **S2B** porta
l'unico confronto `WWOX+/+ / +/− / −/−` in MEF — cioè il solo dato genetico a dosaggio del
paper — **S6C** è la discriminazione K63-contro-K48 su cui poggia l'intera lettura della catena
ubiquitinica, e **S7B** è la misura di emivita citata nel corpo per dire che K274R è meno
stabile. Tre affermazioni portanti del manifest hanno la loro evidenza lì dentro.
**🔴 Le vie tentate, con la risposta letterale — questa voce esiste per non farle ritentare a
qualcun altro fra un mese:**

| Via | Risposta |
|---|---|
| OA package service (`oa.fcgi?id=PMC4226089`) | `error code="idIsNotOpenAccess"` |
| Europe PMC `supplementaryFiles` per `PMC4226089` | `errCode 0` — *«Article with id PMC4226089 is not open access one»* |
| CDN dell'editore, `pnas.org/lookup/suppl/doi:.../DCSupplemental/` | serve una **pagina HTML**, non il PDF (5 701 byte, `HTML document text`) — la stessa trappola già documentata nel manuale deep-dive |
| PDF locale (`PMID25331887_AbuOdeh2014.pdf`) | dieci pagine, **solo l'articolo principale**; il SI non è allegato |

**La distinzione che conta:** il paper ha un full text libero su PMC ma **non è open access**,
e le due cose non coincidono. Il corpo si legge, il supplementary no. Un lettore che assume
«è su PMC quindi il pacchetto OA esiste» tenta le tre vie e conclude che ha sbagliato comando.
**Next action:** richiesta agli autori, oppure copia via biblioteca istituzionale. È materiale
per la Fondazione allo stesso titolo dei dodici senza link libero del 2026-08-07.
**Current status:** ⬜ aperto — **bloccato su accesso, non su tempo.**

---

## FT-054 — PMID 24550385, la fonte da cui `25331887` importa K274 e ITCH senza dimostrarli
**Paper:** PMID 24550385 / DOI 10.1074/jbc.M113.506790 — Abu-Odeh 2014 *J Biol Chem*
289(13):8865–8880 — *Characterizing WW Domain Interactions of Tumor Suppressor WWOX Reveals Its
Association with Multiprotein Networks*
**Priority:** **ALTA**
**Surface:** `structured` · `PMID24550385_AbuOdeh2014_PMC.html` (corpo 85 983 caratteri,
abstract 2 186 separato dal validator) · più `PMID24550385_AbuOdeh2014.pdf` locale
**Identità verificata dall'artefatto, non assunta:** l'intestazione PMC stampa
`J Biol Chem . 2014 Feb 18;289(13):8865–8880. doi: 10.1074/jbc.M113.506790`, che coincide
carattere per carattere con la citazione del **rif. 3** di `25331887`. Verificata prima di
spendere, perché due volte oggi ho attribuito una citazione senza controllare il numero che la
frase porta.
**Perché è il prossimo:** `25331887` scrive *«Our recent data revealed that ITCH mediates WWOX
ubiquitination at K274 (3)»* e *«ITCH … mediates K63-linked polyubiquitination of WWOX, leading
to its stabilization and nuclear translocation (3)»*. **L'identificazione del residuo e della
ligasi non è un risultato di `25331887`**: arriva già fatta da qui, e tutto ciò che ne discende
— il mutante `K274R`, l'import nucleare ubiquitina-dipendente, il modello di Fig 7D, e
`DL-MECH-083` — vi poggia sopra. È `IMPORTED_PREMISE_ATTRIBUTION_GATE` nella forma più pura
che questo corpus abbia prodotto finora.
**🔴 Le due domande che la lettura deve chiudere** — *poste come domande, non come reperti*: il
solo materiale ispezionato finora è **l'abstract**, che è `NOT_EVIDENCE` e non chiude nulla.
Sono scritte qui perché il prossimo giro parta già puntato, non perché siano una risposta.
1. ~~**Questo paper nomina `K274`?**~~ → **RISTRETTA il 2026-08-10, non chiusa.** Ricerca
   d'esistenza a pattern dichiarato (`K\s*-?\s*274|Lys\s*-?\s*274|lysine\s+274`, case-insensitive)
   sul corpo estratto: **10 occorrenze**, nelle forme `K274`, `K 274`, `Lys-274`. Il residuo
   **è nominato nel corpo** — l'abstract non lo diceva, e il mio sospetto nasceva dall'unica
   superficie che avevo guardato, che è `NOT_EVIDENCE` per costruzione. Cade quindi l'ipotesi
   peggiore, cioè che `25331887` attribuisca il residuo a una fonte che non lo contiene.
   ⚠️ Il conteggio non stabiliva che il residuo fosse **identificato per esperimento qui**,
   invece che citato, elencato fra i mutanti dei Metodi o importato a sua volta. Dieci
   occorrenze sono un fatto d'esistenza; *«è identificato in questa fonte»* è un fatto di
   contenuto. **Risolta ispezionando i dieci contesti** — non il conteggio — e l'esperimento
   c'è: spettrometria di massa che identifica il peptide ubiquitinato `FTDINDSLGK274LDFSR`
   (Xcorr 2,11) accanto a `LAFTVDDNPTK100PTTR` (Xcorr 1,54), poi mutagenesi sito-diretta con
   `K274R` non ubiquitinato da ITCH, in Fig 5 E–G, e la conclusione degli autori *«ITCH
   predominantly mediates polyubiquitination of WWOX at Lys-274»*. **Domanda 1 chiusa:
   l'attribuzione di `25331887` regge.**
   *(Osservazione di triage, non un locator: le citazioni qui sopra vanno riverificate contro
   l'artefatto in sede di lettura completa, e non sostituiscono la lettura del corpo.)*
2. **Questo paper riporta una `stabilizzazione`?** L'abstract dice che la ubiquitinazione K63
   porta a *«nuclear localization and increased cell death»*. `25331887` cita la stessa fonte
   per *«stabilization and nuclear translocation»*. **Localizzazione e stabilizzazione non sono
   la stessa affermazione**, e `DL-MECH-083` — la voce che rovescia il default *polyUb →
   proteasoma* — poggia sulla seconda.
   ⚠️ **I conteggi non chiudono questa domanda e non vanno usati come se lo facessero.** Sul
   corpo ricorrono `stabil` 12 volte, `degrad` 14, `half-life` 7, `proteasom` 2. Dicono che il
   paper **discute** la stabilità; non dicono che riporti che la catena K63 **stabilizzi** WWOX.
   🔴 **Il termine ricorre: se la lettura riporta la stabilizzazione, deve venire da un
   esperimento nominato, non dalla frequenza della parola.** Una ricerca tecnica risponde a una
   domanda d'esistenza, mai a una domanda di contenuto — è la regola 4 applicata al proprio
   strumento di triage.
   ⚠️ **Una frase della Discussione sembrava chiuderla e NON la chiude — correzione registrata
   perché il quasi-reperto era persuasivo.** Avevo isolato *«Whether Lys-274 is the same lysine
   in the WWOX C terminus that also targets WWOX for degradation is not known»* e ne avevo
   tratto che la fonte non afferma la stabilizzazione. **Non segue.** Letto il paragrafo intero
   e verificato verbatim contro l'artefatto, quel *«non è noto»* riguarda **se K274 sia anche
   il sito di degradazione**, non se la catena K63 stabilizzi: sono domande imparentate e
   distinte. Se avessi pesato la frase fuori dal suo paragrafo avrei avuto un reperto forte e
   sbagliato. **La domanda 2 resta aperta esattamente dov'era.**
   🔴 **Il paragrafo però serve alla lettura vera, per un'altra ragione:** introduce
   **Mahajan et al. (rif. 62)** — *«full-length WWOX but not a truncated form of WWOX that
   lacks the C terminus, WWOXΔ5–8, is polyubiquitinated **and degraded**»* — cioè una
   **seconda via di ubiquitinazione su WWOX, con esito degradativo**, accanto a quella
   ITCH/K63/K274. Il rif. 62 è **PMID 16288044**, Mahajan 2005 *Cancer Res* 65:10514–10523,
   *«Role of Ack1 in polyubiquitination of tumor suppressor Wwox»*, **già presente in LEGEND
   come `corpus placeholder`** e già trattato in `DL-MECH-048` e `DIS-001`. La lettura deve
   quindi pesare la stabilizzazione **sapendo che la via alternativa è documentata**, non come
   se il default fosse semplicemente invertito. Vedi la calibrazione in coda a `DL-MECH-083`.
**Come è emersa:** dalla lettura di `25331887` (`FTR-20260810-25331887-01`), enumerando le
premesse importate invece dei risultati.
**Current status:** ⬜ aperto, artefatto in casa, **identità verificata**. Non iniziato:
interrotto prima di aprire il corpo per contesto residuo insufficiente a chiuderlo bene, che è
una condizione d'interruzione dichiarata e non un rinvio.

---

## FT-055 — Le sette figure di PMID 24308844, e l'esperimento che **non** è stato eseguito
**Paper:** PMID 24308844 / DOI 10.1021/bi400987k — Schuchardt 2013, *Biochemistry* 52(51) —
*Molecular Origin of the Binding of WWOX Tumor Suppressor to ErbB4 Receptor Tyrosine Kinase*
**Priority:** **ALTA**
**Surface:** `structured` · `PMID24308844_Schuchardt2013_PMC.xml` (JATS da `efetch`,
sha256 `00da56df…`) · corpo letto integralmente, `FTR-20260810-24308844-01`
*(Voce creata il 2026-08-10 **dopo** che tre riferimenti la citavano già — manifest, ricevuta e
rapporto — senza che esistesse. Uno dei tre è dentro la catena hash e non si riscrive. Un debito
citato e mai aperto è un debito che evapora: è la stessa forma delle collisioni di ID, vista dal
lato opposto — non due voci con un nome, ma un nome senza voce.)*

### 🔴 Il punto non è la copertura: è che l'esperimento non è stato eseguito
Questo paper era stato assegnato come **controllo** su una domanda precisa: il mio tasso di
contraddizione del **29,3%** contro il 12–18% degli altri lettori è il metodo o il campione? Quel
tasso è definito come **contraddizioni per locator su figura ispezionato**.

**Ho ispezionato zero figure.** Quindi lo «zero contraddizioni» che la lettura ha prodotto è
testo-contro-tabelle — **una quantità diversa, su un altro asse**, con numeratore e denominatore
entrambi assenti. Non falsifica nulla e non conferma nulla. **L'esperimento resta aperto, non
fallito**, e si esegue qui.

⚠️ **E la lezione di metodo va con la voce, perché è la stessa che il paper insegna:** il titolo
del mio rapporto diceva *«zero contraddizioni»* mentre l'ultimo paragrafo diceva che non è sullo
stesso asse. **A viaggiare è il titolo.** È letteralmente la forma trovata nell'abstract di
questo stesso articolo — *«akin to the binding of WW1»* smentito dalla sua Tabella 3 — applicata
al mio rapporto su di esso.

### Che cosa manca, con il costo di ciascuna
| figura | che cosa porta | perché pesa |
|---|---|---|
| **2** e **4** | isoterme ITC | **ogni Kd citato** (144 · 383 · 362 · 68 µM) esce da questi fit, mai ispezionati |
| **3** | modello strutturale WW1/WW2–ErbB4_PY3 | è l'evidenza dell'argomento **W44/Y85**, il reperto di raggio maggiore della lettura |
| **5** | light scattering, profili di eluizione | la spalla di omodimerizzazione che gli autori dichiarano irrilevante |
| **6** e **7** | RMSD/RMSF/Rg e istantanee MD | il modello «chaperone», che gli autori stessi dichiarano non dimostrato |
| **1** | architettura ErbB4 e sequenze dei peptidi | la nomenclatura P0/P+1/Y+3 su cui poggia tutto il resto |

**Next action:** recuperare le sette figure — `smask` misurato prima di scegliere fra estrazione
e render, e **registrare la risoluzione oltre alla superficie** — un locator per figura o
rinuncia nominata, poi ri-registrare a profondità completa con
`reread_reason: inadequate_prior_coverage`. Solo allora il tasso è calcolabile su questo paper.
**Current status:** ⬜ aperto. Debito **di sessione, non del paper**: la rinuncia è nominata nel
manifest sotto `figure_coverage.waiver`, con il costo di ciascuna figura scritto.

🔴 **AGGIUNTA 2026-08-10, e cambia la natura del debito.** Sopra ho attribuito la rinuncia al
budget. C'era una **seconda ragione, che non conoscevo mentre scrivevo**: `PMID24308844_Schuchardt2013_PMC.xml`
colloca **0 dei suoi 7 elementi `<fig>` dentro `<body>`**, e l'ho letto con un estrattore delimitato
al corpo. **Non ho mai visto una sola didascalia di questo paper.** Si vede nel manifest: le sette
voci figura sono tutte attestazioni da pixel e **non esiste un solo locator su didascalia**, mentre
su `25331887` — HTML, didascalie nella pagina — ne ho due, ed entrambe portano peso. L'assenza
sembrava una scelta; era una superficie invisibile. Censimento e regola in `DL-METH-086`.
**Al prossimo run le didascalie si leggono per prime**, prima delle figure: costano nulla e sono
il posto dove questo corpus ha già trovato tre reperti.

---

## FT-056 — Santini et al., *Oncogene* 2014: la freccia ATM→ITCH non è di questo laboratorio, e dal commentary non è raggiungibile

**Paper:** DOI 10.1038/onc.2013.52 — Santini S *et al.*, *Oncogene* 2014;33(9):1113–1123 —
*ATM kinase activity modulates ITCH E3-ubiquitin ligase activity*
**PMID 23435430** · **PMCID PMC3938399** — risolti nella stessa sessione via `esearch` sul DOI,
subito dopo aver scritto questa voce. La citazione originaria era stata letta dalla reference list
di `PMID 25331887` (voce 42), verificata carattere-per-carattere contro
`files/fulltext/PMID25331887_AbuOdeh2014_PMC.html` (`sha256 8c629a54…`).

**Surface (preflight eseguito, 3 vie):** `oa.fcgi` → record presente, `license="none"`,
`retracted="no"` (manoscritto d'autore depositato, non licenza aperta) · Europe PMC `fullTextXML`
→ **200, 96 812 byte, corpo presente** · `efetch db=pmc` → **200, 92 519 byte, corpo presente**.
Otto figure `F1`–`F8`, 38 referenze, nessuna tabella. **È raggiungibile.**

🔴 **E le due vie non concordano su che cosa sta dentro `<body>`.** Corpo `efetch` 29 341
caratteri contro **46 114** di Europe PMC. La differenza non è coda: `efetch` colloca **tutti e
otto** gli elementi `<fig>` **fuori** dal `<body>`, Europe PMC tutti e otto **dentro**. Otto
didascalie — otto frasi dichiarative, una per figura — che un estrattore delimitato al `<body>`
non mostra affatto. **Dichiarare Europe PMC come `article_text`**, e comunque contare le figure
dentro il corpo prima di leggere (vedi `DL-METH-086`).

**Perché è in coda, e non è una questione bibliografica.** `PMID 25331887` scrive nella Discussion
*«After DNA damage, ATM positively regulates the ligase activity of ITCH (42)»* — con il numero.
Il suo Author's View `PMID 27308504` scrive nella didascalia della propria unica figura *«Activated
ATM phosphorylates and positively regulates the ligase activity of ITCH»* — **senza numero**, dentro
un modello presentato come proprio, e **il riferimento 42 non compare fra le dieci voci del
commentary**. Un lettore che partisse dall'Author's View per risalire a quella freccia non
troverebbe alcun percorso.

🔴 **È la freccia che chiude l'anello.** Senza ATM→ITCH il *feed-forward loop* del modello è aperto:
resta ITCH→WWOX→ATM, una catena lineare. L'anello — la proprietà che rende il modello
interessante — poggia interamente su un lavoro di terzi che questo corpus non ha letto.
`IMPORTED_PREMISE_ATTRIBUTION_GATE`, su una premessa che porta peso.

**Next action (sessione fredda):** risolvere `10.1038/onc.2013.52` → PMID/PMCID via `idconv` o
`esearch`; preflight a tre vie; se `Oncogene` 2014 non è open access, dichiararlo e accodare come
`PREMISE: NON RISOLTA` invece di assumere il segno. **La domanda precisa da porre al paper:** ATM
fosforila ITCH *direttamente*, e l'effetto sull'attività ligasica è misurato o inferito? La
direzione conta: se ATM *attiva* ITCH e ITCH *stabilizza* WWOX, l'anello è positivo; se in quel
paper l'effetto fosse inibitorio, il modello di `27308504` si rovescia.
**Current status:** ⬜ aperto. **Priorità: ALTA** — è l'unica premessa non risolta di una catena
che questo corpus cita in tre letture.

---

## FT-057 — I due paper fondativi del KO che il commentary invoca e questo corpus non ha letto

**Papers:** PMID 18487609 / DOI 10.1074/jbc.M800855200 — Aqeilan RI *et al.*, *JBC*
2008;283:21629–39, PMC2490770 — *The WWOX tumor suppressor is essential for post-natal survival
and normal bone metabolism* · PMID 17360458 / DOI 10.1073/pnas.0609783104 — Aqeilan RI *et al.*,
*PNAS* 2007;104:3949–54, PMC1820689 — *Targeted deletion of Wwox reveals a tumor suppressor
function*.

🔴 **PREMESSA SBAGLIATA, CORRETTA UN'ORA DOPO AVERLA SCRITTA — e la tengo accanto a quella giusta.**
Avevo scritto: *«Entrambi PMC, quindi superficie strutturata attesa — da verificare, non da
presumere»*. Ho scritto «da verificare», poi ho verificato, e **la previsione era falsa**.
`PMID 18487609`: `oa.fcgi` risponde `idIsNotOpenAccess`, Europe PMC `fullTextXML` risponde **404**,
`efetch db=pmc` risponde 200 con **11 699 byte e nessun elemento `<body>`** — metadati e abstract,
zero corpo, zero figure, zero referenze. **Un PMCID non è una superficie.** Il 200 di `efetch` è la
parte pericolosa: una pipeline che controlli solo lo status code o solo che il file non sia vuoto
archivierebbe quel file come «full text recuperato». La copia locale
`PMID18487609_Aqeilan2008_PMC.html` esiste già nel `files/` condiviso ed è la sola via aperta —
**da ispezionare prima di qualunque altra cosa**, perché nessuno ha ancora verificato se porti il
corpo o soltanto il landing.

Ordinati per priorità di lettura, non per data: vedi sotto.

**Perché pesano più di quanto suggerisca il titolo.** `PMID 27308504` li cita insieme per una
sola frase — *«Wwox knockout (KO) mice exhibit post-natal lethality and die by 4 weeks of age»* —
e quella frase è il fondamento fenotipico di ogni trasferimento dal modello murino alla malattia.
**`PMID 18487609` è il paper meno oncologico dei due**: sopravvivenza post-natale e metabolismo
osseo, cioè esattamente il registro non tumorale in cui vive il genotipo di riferimento. Sta in
coda da tempo per il titolo che promette osso; è la forma classica descritta in
`gold_is_in_the_details`.

**Next action (sessione fredda):** preflight a tre vie su entrambi i PMCID, **e preflight separato
sulla superficie figure** — «superficie strutturata trovata» non implica «migliore superficie
figure trovata», e su `27308504` la copia dentro il PDF aveva 3,1× i pixel del deposito PMC.
Leggere `18487609` per primo. Budget figure dichiarato *prima* di aprire.
**Current status:** ⬜ aperto. Priorità: media-alta.

---

## FT-058 — Il campo che ho coniato non è controllato da nulla, e lo dico prima che sembri verificato

**Source:** `NOT_AN_ARTICLE` — un contratto, non un paper: `framework/scripts/deepdive_manifest.py` su `main`,
`COUPLED_RELATIONS` e `_pointer_needle_errors`; l'istanza vive in
`disease-models/wwox/research/deepdive_manifests/PMID27308504.json`, `entries[2]`.

**Che cosa esiste.** `PMID27308504.json` `entries[2]` porta tre campi nuovi:
`cross_document_relation: "hedge_deleted_by"`, `restates: "entries[1]"`, `restates_needle`.
Seguono la grammatica che `main` ha fissato — puntatore più frammento, con la *suffix law*
`<pointer>_needle`.

**Perché non è dentro `panel_text_relation`.** Quell'enum è delimitato dal proprio nome: dice come
un **pannello** sta rispetto a un **testo**. Questa relazione sta fra **due documenti**. Allargare
l'enum sarebbe stato lo stesso ragionamento che ha prodotto `panel_qualifies_text` applicato al
contrario per arrivare alla conclusione opposta: là nessun valore ammesso era vero e il difetto
era l'enum; qui il difetto sarebbe stato usarlo.

🔴 **E qui sta il debito.** Il validatore di `main` **ignora del tutto** questi tre campi: il
manifest passa `MANIFEST STRICT PASS, 0 gaps` **senza che siano stati controllati**. È esattamente
la forma «verde silenzioso» che questo repository esiste per impedire — un campo che *sembra*
verificato perché sta accanto a campi che lo sono. La regola dell'ago è stata quindi eseguita **a
mano** contro `_match_key` di `main` (il frammento appartiene allo snippet del bersaglio e a
nessun altro), e il risultato è scritto nel manifest sotto
`cross_document_relation_selfcheck`. **Un controllo eseguito a mano è più debole di un gate**, ed è
offerto come argomento per costruirlo, non come sostituto.

**Next action:** proporre a chi possiede `framework/scripts` di estendere `COUPLED_RELATIONS` con
una tabella gemella per le relazioni cross-documento — il codice esiste già, `_pointer_needle_errors`
è agnostico rispetto al nome della relazione e servirebbe solo una seconda mappa. **Non è mio da
scrivere**: è lo stesso confine per cui `24308844` e `38182577` falliranno alla fusione finché il
mio ramo porta un validatore più vecchio della regola.
**Current status:** ⬜ aperto. Priorità: media — nessuna lettura ne dipende oggi, ma la seconda
istanza del campo arriverà prima del gate se nessuno lo costruisce.

---

# ⏭️ HANDOFF — lettore B, ramo `lettore-b`, 2026-08-10 22:xx UTC

*Scritto per una **sessione fredda**: chi legge domani non ha nulla di questa conversazione. Tutto
ciò che serve per ripartire senza rileggere niente sta qui.*

## Dove sono gli artefatti
**Tutti nel `files/` del checkout condiviso** `/Users/massimo/Desktop/legend-public/files/fulltext/`,
**mai nel worktree** — `files/` è gitignored per copyright, quindi il ramo porta il manifest e non
l'evidenza. Validare sempre con `--artifact-workspace /Users/massimo/Desktop/legend-public`.

| artefatto | sha256 | note |
|---|---|---|
| `PMID27308504_Hazan2015_PMC.xml` | `4124af2c…` | JATS `efetch`, corpo 11 944 car. — superficie dichiarata |
| `PMID27308504_Hazan2015.pdf` | `20d80aa0…` | 3 pagine, `article_binary` |
| `PMID27308504_Hazan2015_assets/p2_x4.jpeg` | `a979aad0…` | Fig 1, **1302×1051**, `smask=0` |
| `PMID27308504_Hazan2015_assets/orig_g001.jpg` | `45e02106…` | deposito PMC, **730×597** — 3,1× meno pixel, tenuto solo per il confronto |
| `PMID25331887_AbuOdeh2014_PMC.html` | `8c629a54…` | **secondo `article_text`**: entrambi i lati di ogni confronto sono verificati |

## Che cosa è stato letto, per sezione
`PMID 27308504` — **completo**, ed è un documento piccolo: `article-commentary` (Author's View),
abstract + 4 paragrafi + didascalia + 10 referenze. Metodi, risultati e limiti **non esistono**;
tabelle **zero** (verificato in entrambe le vie); supplementary **assente** (né `oa.fcgi` né il PDF
ne portano). Figura unica ispezionata a 1302×1051 in due metà. `FTR-20260810-27308504-01`,
`MANIFEST STRICT PASS, 0 gaps` contro il validatore di `main`. Ledger a **67**, tail ancorato.

## Il debito preciso
1. **`FT-056` · `PMID 23435430` (Santini, *Oncogene* 2014) — ALTA, e il preflight è già fatto.**
   PMC3938399, corpo presente in entrambe le vie, 8 figure, 38 ref. **Dichiarare Europe PMC**, non
   `efetch`: `efetch` tiene le 8 didascalie fuori dal `<body>`. È la premessa non risolta della
   freccia ATM→ITCH. Domanda al paper: la fosforilazione è diretta, e l'effetto sull'attività
   ligasica è **misurato o inferito**? Se fosse inibitorio, il modello di `27308504` si rovescia.
2. **`FT-057` · `PMID 18487609` — la via PMC è chiusa**, `efetch` dà 200 e nessun corpo. Unica
   strada: `PMID18487609_Aqeilan2008_PMC.html`, già nel `files/` condiviso, **mai ispezionato**.
3. **`FT-053`** — ristretta oggi: ITCH→stabilizzazione è ora *misurata* (`24550385`, lettore A);
   K274→emivita resta su `Fig. S7B` irraggiungibile.
4. **`FT-055`** — Figure 1 e 7 di `24308844`, **e le didascalie di tutte e sette**, mai viste.
5. **`FT-058`** — il campo coniato non è controllato da nulla.
6. **Non mio da riparare:** `24308844` e `38182577` falliranno alla fusione finché questo ramo
   porta un `deepdive_manifest.py` più vecchio della regola. Appartiene a chi possiede il contratto.

## Due trappole misurate oggi, da non ripagare
- **Contare `<fig>` dentro `<body>` prima di dichiarare una superficie** — 10 XML su 35 le tengono
  fuori (`DL-METH-086`). Il validatore non se ne accorge perché percorre l'articolo; **chi legge sì.**
- **Misurare la risoluzione di entrambe le copie** — su `27308504` la copia dentro il PDF aveva
  3,1× i pixel del deposito PMC, l'inverso dell'assunzione portata da `25331887`. E la vecchia via
  `www.ncbi.nlm.nih.gov/pmc/articles/…/bin/` risponde **404 con 48 KB di HTML**: chi controlla solo
  lo status code o solo la dimensione salva quel file come immagine.
