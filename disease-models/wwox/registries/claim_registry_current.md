# Claim Registry Current

> **Public edition — de-identified.** Disease-level registry from public literature. All individual-linking data removed (names, geography, report/sample IDs, dates, parent-of-origin, cell-line ownership). Specific variants appear only as decoupled disease-model worked examples drawn from public literature, never as one persistent individual's inherited alleles. Some entries remain in their original language. Not medical advice.
## WWOX Claim Registry
**Version:** v1.6.2  
**Date baseline:** 2026-03-28  
**Last update:** 2026-07-25 — `BATCH_20260725_001` (public audit, **traceability repair, no scientific change**): CLAIM 028 source pointer corrected from nonexistent paper 213 to tracked CORPUS P207. No claim text, status or epistemic tag changed. Prev: `BATCH_20260725_LINKS` migrated wikilink fragments and privacy-safe headings without scientific change. Prev: 2026-07-05 — BATCH_20260705_001: CLAIM 004 enriched from Repudi 2021 full text; CLAIM 019 proteostasis-rescue IPOTESI note added; CLAIM 021 and CLAIM 026 source-normalized to PAPER 031/032.

---

## Purpose
Canonical audit trail of numbered claims relevant to the Working Model.

### Rules
- A claim here does **not** automatically modify BLOCCO 1
- Promotion requires Working Model Updater logic
- Every claim must be tagged for:
  - pathway
  - genotype/model relevance
  - transferability to a case
  - status

### Possible statuses
- consolidated baseline
- in observation
- conflicting evidence
- flagged for review
- background only
- archived

---

## CLAIM 001
**Title:** Vigabatrin associated with VABAM in WWOX-DEE
**Status:** conflicting evidence
**Type:** DATO
**Pathway:** P2 — GABAergic vulnerability / safety
**Genotype/model relevance:** umano / WWOX-DEE pediatrico — genotipo vario; trasferibile direttamente al genotipo di riferimento indipendentemente dal genotipo specifico (safety claim)
**Transferability:** T1
**clinical relevance:** HIGH
**Summary:** In WWOX-related epileptic encephalopathy, vigabatrin è stato associato a VABAM (Choi 2026, 2 casi). You 2024 riporta riduzione delle crisi con vigabatrin in 1 caso null/null severo, senza MRI di follow-up per VABAM. Chong 2023: un caso resistente al vigabatrin, uno migliora in combinazione con KD. Gao 2025: vigabatrin tra i farmaci più usati nel cohort ma senza dati di efficacia/sicurezza specifici. — **BATCH_20260710_A, lato efficacia ([[paper_registry_current#PAPER 045]]):** Shaukat 2018 riporta due bambini WWOX-**null** con sindrome di West. Caso 1: prednisolone (UKISS) → risposta parziale; **vigabatrin aggiunto → "the spasms resolved"**; successive mioclonie/cloniche migliorate con levetiracetam. Caso 2: fenobarbital → miglioramento; **vigabatrin → risposta parziale**; a 11 mesi spasmi residui in cluster nonostante 4 antiepilettici. **Nessun VABAM né peggioramento riportato in questo studio.**
**Clinical meaning:** La posizione per il genotipo di riferimento non cambia: cautela / evitare vigabatrin come orientamento generale, salvo esaurimento delle alternative e documentazione esplicita del rischio. I due effetti (riduzione crisi e rischio VABAM) non si escludono. Conflicting evidence / hold — nessun dato nuovo modifica sostanzialmente il profilo. — **Nota epistemica (BATCH_20260710_A):** il razionale meccanicistico *"GABA depolarizzante nei neuroni immaturi → i farmaci GABAergici rendono poco"*, derivato dagli organoidi ([[claim_registry_current#CLAIM 002]]), **non predice questi esiti clinici**: il vigabatrin ha risolto gli spasmi in un WWOX-null. Il meccanismo resta valido come meccanismo; **non è un predittore di risposta clinica**. Lo status `conflicting evidence` è confermato come corretto, ed è ora conflicting in modo più informato: **evidenza di efficacia sugli spasmi** (Shaukat, n=2) **contro evidenza di tossicità RMN** (Choi, n=2). Nessuna delle due chiude la questione. **Non è parere medico.**
**Source:** Choi et al. 2026 *Pediatric Neurology* (safety anchor) / You et al. 2024 *Mol Genet Genomic Med* (tensione evidence) / Chong et al. 2023 *AJMG* (dato misto) / Gao et al. 2025 *Neurology* (utilizzo clinico senza safety data)
**Wikilinks:** [[paper_registry_current#PAPER 003]] (Choi) · [[paper_registry_current#PAPER 016]] (You) · [[paper_registry_current#PAPER 017]] (Chong) · [[paper_registry_current#PAPER 014]] (Gao) · [[paper_registry_current#PAPER 045]] (Shaukat — lato efficacia) · [[claim_registry_current#CLAIM 031]]
**Impact on Working Model:** BLOCCO 1 safety position unchanged; BLOCCO 2 status updated to conflicting evidence

---

## CLAIM 002
**Title:** WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype
**Status:** consolidated baseline
**Type:** DATO + INFERENZA prudente
**Pathway:** P1 — Ca²⁺ / network dysregulation; P7 — gene therapy readiness
**Genotype/model relevance:** umano organoide WWOX-KO + WOREE-derived; genotipo caution: KO ≠ una classe null/missense; trasferibile con cautela a meccanismo di rete
**Transferability:** T2
**clinical relevance:** HIGH
**Summary:** WWOX-deficient organoids show hyperexcitability and altered Ca²⁺ dynamics; WWOX re-expression improves the phenotype. **BATCH_20260710_C — estensione da fonte primaria pubblicata:** Steinberg et al. 2021 mostra in organoidi WWOX-KO e WOREE-derived: squilibrio E/I con firma GABAergica immatura; astrogenesi aumentata; difetto DDR con perdita del checkpoint apoptotico; attivazione Wnt; dyslamination corticale; firma OXPHOS↓/glicolisi↑; firing aumentato e normalizzato dal rescue. Il rescue del modello con variante splice `c.517-2A>G` prova che la reintroduzione di WWOX può correggere più domini cellulari, ma non dimostra che un ASO corregga `c.1057-2A>G`.
**Clinical meaning:** Strongly supports the network-level model, la terapia genica e l'uso degli organoidi come piattaforma sperimentale. Non predice da solo risposta clinica né trasferibilità quantitativa al genotipo di riferimento. Therapeutic relevance: `all_WWOX_LoF` per gene addition; `the reference genotype` come piattaforma per test allele-specifici. Next decisive experiment: modelli isogenici **per singolo allele** — uno per il missense SDR, uno per l'allele di sito accettore — con rescue e readout ortogonali.
**Evidence boundary (BATCH_20260909_001 — cortical layering endpoint; R4 satisfied).** 🔴 **The AAVS1 rescue (`W-AAV`, constitutive UBP promoter) is marker-selective, not uniformly normalising.** In Figure 4H: for **CTIP2/nuclei** the WT-versus-W-AAV comparison **is** drawn and is **significant (`**`) with the rescue ABOVE wild type** — an *overshoot* of the wild-type set point, not a return to it; for **TBR1** and the third (**SATB2**) sub-panel **no** WT-versus-W-AAV bracket is drawn, which under the legend's all-pairwise *"one-way ANOVA with Tukey's multiple comparisons test"* means **tested and not significant**, not omitted. The paper's own sentence scopes recovery to the knockout comparator («…recovered and layering improved in W-AAV COs **compared with WWOX-KO COs**, RNA levels did only partially»), and the section closes with «prevents these changes **to some extent**». **So `normalizzato` is accurate for firing rate (P = 0.7681, parents vs rescued patient organoids) and over-general for cortical lamination: the rescue normalises two of three layer markers and overshoots the third.** Nothing is reversed and no evidence is demoted; the electrophysiology half is untouched, and this is **not** a harm finding — an overshoot on a patterning marker measures no toxicity endpoint. *(The audit corrected this reading before it entered: the first wording called the TBR1/SATB2 comparison "untested" and was returned `OVERSHOOT`; the corrected finding is stronger and narrower. The third sub-panel bears no printed title — SATB2 is an identification by elimination from legends G and H, and that inference is stated in the locator itself.)*
**Adjacent negatives anchored by the same reading, neither previously in this claim.** **(1) Organoid size is a clean null** — Appendix Table S1, WT vs KO: wk6 `0,3675`, wk10 `0,5619`, wk15 `0,9949`, wk18 `0,8952` (ordinary one-way ANOVA, Tukey), all W-AAV rows likewise null. **The model does not reproduce the microcephaly seen in some patients**, and unlike the layering boundary this null is a *performed and reported* test — relevant because the human phenotype is explicitly variable on this point. **(2) Dorsal/ventral identity is unchanged but not uniformly so** — Appendix Fig S3C rows: dorsal `1`, combined `1`, **ventral `0,064`** (Kruskal–Wallis), where the running text reports simply no significant difference. `0,064` is not significant and is not nothing; recorded so a future regional-identity claim starts from the number rather than the summary.
**Source:** Steinberg et al., 2024 preprint; Steinberg et al., 2021, *EMBO Molecular Medicine*, full text reviewed
**Wikilinks:** [[paper_registry_current#PAPER 001]] · [[paper_registry_current#PAPER 039]]
**Impact on Working Model:** supports BLOCCO 1 and P7

---

## CLAIM 003
**Title:** Neuronal WWOX deletion induces non-cell-autonomous hypomyelination
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** P4 — myelination / white matter
**Genotype/model relevance:** murino / delezione neuronale condizionale; non null/null sistemico; genotipo caution moderata; meccanismo mielinizzazione plausibilmente trasferibile
**Transferability:** T2
**clinical relevance:** MODERATE
**Summary:** Neuronal WWOX loss impairs myelination despite presence of OPCs.
**Clinical meaning:** Justifies MRI + DTI before discussing myelination adjuncts.
**Source:** Repudi et al., 2021, *Brain*
**Evidence boundary — quanto lontano arriva «non-cell-autonoma» (2026-08-10, `BATCH_20260810_005`):** il lavoro gemello del 2021 dallo stesso laboratorio ([[paper_registry_current#PAPER 005]], PMID 34747138, letto integralmente) rafforza il meccanismo e ne segna il limite nello stesso gesto. **Rafforza:** gli oligodendrociti **non sono mai trasdotti** dal vettore neurone-specifico, verificato con co-staining CC1/anti-WWOX, e la mielinizzazione migliora comunque — è la prova diretta che l'effetto passa per i neuroni. **Limita:** il recupero è **incompleto**, e gli autori attribuiscono il residuo a *«an oligodendrocyte-specific WWOX function»*. Quindi *non-cell-autonoma* descrive **una componente**, non l'intero fenomeno; una funzione WWOX autonoma dell'oligodendrocita resta aperta e non è esclusa. `PREMISE_TAG`: l'attribuzione del residuo agli oligodendrociti è **`IPOTESI` degli autori**; il divario residuo è `DATO`. Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici.
**Wikilinks:** [[paper_registry_current#PAPER 004]] · [[paper_registry_current#PAPER 005]] · [[paper_registry_current#PAPER 063]] · [[claim_registry_current#CLAIM 004]]
**Impact on Working Model:** surveillance logic integrated

---

## CLAIM 004
**Title:** AAV9-WWOX neuron-targeted rescue shows multi-domain in vivo improvement
**Status:** consolidated baseline
✅ **Flag risolto 2026-08-10 (`BATCH_20260810_005`) — il comparatore è ora scritto nella claim, non rimandato.** La riscrittura era stata deliberatamente rinviata a una propagazione che avesse davanti i locator di `deepdive_manifests/PMID34747138.json`. Quei locator esistono (receipt `FTR-20260810-34747138-01`, 20 voci, validatore PASS) e dicono esattamente quanto serviva: **dove il rescue è confrontato con il WT il confronto o non è tracciato, o è significativo contro il rescue.** La claim torna `consolidated baseline` perché il dato non è mai stato in discussione — mancava la sua qualificazione. Testo del flag conservato qui sotto come storia di audit.
> 🔴 **Flagged 2026-08-10 (`CC-20260810-CLAIM004-REVIEW`) — the comparator is missing, not the finding.** La claim elenca i domini recuperati senza dire *contro cosa*. La lettura del 2026-08-10 della sua stessa fonte (PMID 34747138) riporta che **dove il rescue è confrontato con il wild type e non con il null non trattato, è significativamente incompleto**. Non è falsa: è non qualificata, e in `P7 — gene therapy readiness` la differenza fra *migliora* e *normalizza* è la differenza fra un principio di design e un esito atteso. La riscrittura è deliberatamente **rinviata** a una propagazione che abbia davanti i locator di `deepdive_manifests/PMID34747138.json`; sceglierla ora significherebbe decidere, senza la lettura, quali domini raggiungono il WT e di quanto.
**Type:** DATO
**Pathway:** P7 — gene therapy readiness
**Genotype/model relevance:** murino / Wwox-null full KO; genotipo caution alta: null/null sistemico ≠ the reference genotype compound het; design principles trasferibili, non il modello in toto
**Transferability:** T2
**clinical relevance:** HIGH
**Summary:** Preclinical AAV9-WWOX rescue improves survival, hyperexcitability and myelin-related phenotype. Full-text verificato (CC-2026-07-05-001): singola ICV neonatale (P0) di AAV9-hSynI-WWOX (murino o umano, equivalenti) recupera sopravvivenza/letalità postnatale, crescita, ipoglicemia, crisi, atassia, mielinizzazione (OPC→oligodendrociti maturi, g-ratio, corpo calloso + nervo ottico), comportamento e neuroinfiammazione (↓GFAP/Iba1). Restauro neuronale-only → mielinizzazione migliorata **non-cell-autonoma**; gliosi **downstream** della disfunzione neuronale; ipoglicemia reversibile da restauro **CNS-only** (controllo centrale del glucosio); espressione durevole ≥9 mesi.
**Clinical meaning:** Supports gene therapy as the main causal strategic axis. ⚠️ Cautela verificata: modello Wwox-null sistemico + finestra P0 neonatale → design-principle trasferibili, NON dose/timing (the reference genotype = compound het N/M, non neonata).
**🔴 Evidence boundary — il comparatore (2026-08-10, lettura integrale, `BATCH_20260810_005`):** *migliora* e *normalizza* non sono la stessa parola, e in `P7 — gene therapy readiness` la differenza è fra un principio di design e un esito atteso. **Ciò che è testato contro il WT:** il **g-ratio**, che normalizza (la nuvola trattata si sovrappone al WT, quella KO resta piatta a 0.8–0.95); e il **conteggio di assoni non mielinizzati**, che è significativo **contro** il rescue (~26 per campo in WT contro ~52 nei trattati, `**`). **Ciò che NON è testato contro il WT:** assoni mielinizzati per campo (corpo calloso ~130/46/105, nervo ottico ~140/68/124), CC1⁺ (WT ~170 / KO+GFP ~77 / rescued ~135) e PDGFRα⁺ (WT ~53 / KO+GFP ~87 / rescued ~70) — in ogni caso le parentesi corrono **WT-vs-KO** e **KO-vs-rescued**, e il divario residuo visibile **resta non testato**. Gli autori lo dichiarano: *«there are still some differences between rescued and WT mice which could be attributed to an oligodendrocyte-specific WWOX function in regulating the myelination process»* — attribuzione che è la loro **`IPOTESI`**, mentre il divario è `DATO`. **Corollari da non perdere:** trasduzione **60–70%** dei neuroni (non quasi-totale); **oligodendrociti mai trasdotti**, che è ciò che rende il recupero non-cell-autonomo; finestra **P0** con la ragione dichiarata (sopravvivenza del modello) e il dosaggio post-natale **esplicitamente futuro**; **n = 3** per genotipo nella quantificazione EM; elettrofisiologia **sotto ketamina**; il non-rilievo di tumori qualificato tre volte (*gross*, *limited number*, *8–11 months*) in un oncosoppressore con periferia ancora null.
**Source:** Repudi et al., 2021, *EMBO Molecular Medicine* — PMID 34747138, `complete_fulltext_read` 2026-08-10, receipt `FTR-20260810-34747138-01` (prima: verifica di metadati e contenuti-chiave del 2026-07-05; According to PubMed, [DOI](https://doi.org/10.15252/emmm.202114599))
**Wikilinks:** [[paper_registry_current#PAPER 005]] · [[paper_registry_current#PAPER 063]] · [[claim_registry_current#CLAIM 003]]
**Impact on Working Model:** strategic / trial-readiness support

---

## CLAIM 005
**Title:** Reduced GABAergic interneurons and glial activation in WWOX-KO
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** P2 — GABAergic vulnerability; P6 — neuroinflammation / glia
**Genotype/model relevance:** murino / Wwox-KO sistemico; genotipo caution: KO ≠ compound het; segnale GABAergico e gliale plausibilmente trasferibile come meccanismo generale di vulnerabilità
**Transferability:** T2
**clinical relevance:** MODERATE
**Summary:** In **one** systemic constitutive Wwox-KO mouse model at two weeks, PV-positive interneuron counts are lower in DG, CA1 and across the whole hippocampus (−44%), NPY-positive counts are lower **in DG only**, and IBA1/GFAP immunoreactive area fractions are higher in CA1, CA3 and whole hippocampus. Marker-positive abundance and area fraction — not cell loss, not glial cell number.
**Clinical meaning:** Supports the glial axis as a modifier. **No medication implication.** The source measures no GABA concentration, no synaptic inhibition, no E/I ratio and no drug: a medication caution cannot be attributed to it, and would have to enter as a separately sourced multi-source inference.
**Source:** Hussain et al., 2019, *Neurobiology of Disease* 121:163–176 — PMID 30290271 (full text read 2026-08-06, receipt `FTR-20260806-30290271-01`)
**Wikilinks:** [[paper_registry_current#PAPER 006]]
**Impact on Working Model:** modifier logic. **Not** BLOCK-1 / medication policy.
**Evidence boundary:** NPY CA1/CA3 are reported as showing no obvious difference; the whole-hippocampus NPY panel carries **no significance marker** — a visual panel observation, not a reported test. IBA1/GFAP in DG are marginal and unmarked. Only `Il6`, not `Tnf-a`, is significant (`n=4/group`). GAD65/67 is protein abundance only. **Imported premises, now traced to their end (2026-08-06).** Early death and epileptogenesis were attributed here to PMID 19936220 and Mallaret 2014. All three links of that chain have since been read in full. **Early death is first-hand** in PMID 19936220: 43% dead by 72 h, 77% by day 17, none past weaning (`FTR-20260806-19936220-01`). 🔴 **Epileptogenesis is not measured there in any form** — no EEG, no seizure observation, no behavioural assay, no brain histology; the only brain measurement in that paper is organ weight. It enters it once, as a Discussion citation of the **rat** `lde` model. 🔴 **And that terminus asserts the opposite for the mouse:** PMID 19500159 states in three places, and in a Table 2 whose `Epilepsy` row is **empty for both mouse models**, that Wwox-null mice show no epilepsy (`FTR-20260806-19500159-01`). Seizures in the Wwox literature are a **rat `lde/lde`** phenotype — see [[claim_registry_current#CLAIM 037]]. **No canonical statement may describe a Wwox-null mouse as showing epileptogenesis.** Whether the mouse lacks the phenotype or dies before expressing it is open and testable: the earliest rat seizure onset (day 16) already exceeds the entire lifespan of the mouse null.

---

## CLAIM 006
**Title:** P47T model shows progressive neuroinflammation
**Status:** consolidated baseline
**Type:** DATO + INFERENZA prudente
**Pathway:** P6 — neuroinflammation / glia
**Genotype/model relevance:** murino / variante P47T specifica; genotipo caution OBBLIGATORIA: P47T ≠ Q230P — non trasferire automaticamente al genotipo di riferimento; P47T abolisce binding PPxY in WW1, meccanismo diverso da Q230P/SDR
**Transferability:** T3 with genotype caution
**clinical relevance:** LOW
**Summary:** P47T murine model shows progressive microgliosis and astrogliosis.
**Clinical meaning:** Supports glia as possible modifier, but cannot be directly transferred to Q230P.
**Source:** Hussain et al., 2023
**Wikilinks:** [[paper_registry_current#PAPER 007]]
**Impact on Working Model:** surveillance only, genotype caution mandatory

---

## CLAIM 007
**Title:** P47T abolishes PPxY binding to WW-domain partners
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** P3 — MYC/Wnt / interaction logic
**Genotype/model relevance:** studio funzionale su variante P47T specifica (WW1 domain); genotipo caution OBBLIGATORIA: Q230P è nel dominio SDR, non WW1 — meccanismo di interazione diverso; questo claim serve principalmente come àncora della regola P47T ≠ Q230P
**Transferability:** T3 with genotype caution
**clinical relevance:** LOW
**Summary:** P47T alters WWOX WW-domain binding behavior.
**Clinical meaning:** Reinforces rule that Q230P and P47T are not interchangeable.
**Source:** Hussain et al., 2023
**Wikilinks:** [[paper_registry_current#PAPER 007]]
**Impact on Working Model:** genotype caution logic

---

## CLAIM 008
**Title:** WOREE and SCAR12 form a genotype-phenotype spectrum
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** Clinical spectrum / genotype-phenotype
**Genotype/model relevance:** umano / revisione clinica su spettro WWOX; applicabile direttamente al genotipo di riferimento come framework nosologico; non richiede cautela genotipica — è un claim di contesto clinico trasversale
**Transferability:** T1 contextual
**clinical relevance:** MODERATE
**Summary:** WWOX-related disorders occupy a phenotypic spectrum; severity differs by genotype.
**Clinical meaning:** Supports caution when transferring from severe/null models to the reference genotype.
**Source:** Aldaz 2020 / Banne 2021
**Wikilinks:** [[paper_registry_current#PAPER 008]]
**Impact on Working Model:** contextual background

---

## CLAIM 009
**Title:** WWOX deficiency plausibly alters mitochondrial quality control, redox and energy efficiency
**Status:** in observation
**Type:** INFERENZA
**Pathway:** P5 — metabolism / mitochondria / redox / mitophagy
**Genotype/model relevance:** revisione mista (cellulare/animale/umano indiretti); non modello CNS pediatrico specifico; piccolo segnale clinico umano da Chong 2023 (lattato P4, null/null); inferenza concettuale applicabile al genotipo di riferimento con cautela
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Summary:** WWOX deficiency appears coherent with ROS increase, energetic inefficiency and mitochondrial quality-control stress. Chong 2023 aggiunge un piccolo segnale clinico (lattato lievemente elevato in P4) compatibile con vulnerabilità metabolica minore. Baryła 2025 rafforza il framework HIF1A/glicolisi.
**Clinical meaning:** Supports NAC / CoQ10 / creatine / KD logic, but remains only partially CNS-linked in pediatric WWOX. Non sufficiente per upgrade operativo.
**⚠️ Counter-directional evidence (BATCH_20260726_001):** in fotorecettori di topo diabetico WWOX è **up-regolata** e il suo knockdown con siRNA **riduce** il superossido ([[paper_registry_current#PAPER 054]], T3). La direzione deficienza→ROS **non è quindi stabilita come monotona né come indipendente dal contesto**. Lo stato resta `in observation` e **non** sale a `conflicting evidence`: il protocollo riserva quello stato a studi *comparabili*, e questi non lo sono — CLAIM 009 poggia su modelli di deficienza/germinali, PAPER 054 sul knockdown acuto di una proteina di stress indotta in una cellula adulta wild-type. La nota è però obbligatoria, perché il claim è citato a supporto della logica NAC / CoQ10 / creatina / KD e ora esiste un esperimento diretto in un neurone in cui *rimuovere* WWOX ha *abbassato* i ROS. Vedi [[claim_registry_current#CLAIM 034]] e [[claim_registry_current#CLAIM 028]].
**Source:** Baryła et al. 2022 + mechanistic synthesis + Chong 2023 (lattato P4) + Baryła 2025 (WWOX/HIF1A ratio) + [[paper_registry_current#PAPER 054]] (evidenza controdirezionale)
**Wikilinks:** [[paper_registry_current#PAPER 002]] · [[paper_registry_current#PAPER 023]] (Baryła 2022) · [[paper_registry_current#PAPER 017]] (Chong) · [[paper_registry_current#PAPER 054]] · [[paper_registry_current#PAPER 061]] (AbuRemaileh 2019) · [[claim_registry_current#CLAIM 034]] — Baryła 2025 non ancora in registry
🔴 **Aggiunto 2026-08-10 (`CC-20260810-30755385`, BATCH_20260810_003): [[paper_registry_current#PAPER 061]] come evidenza a sostegno, con due confini espliciti.** La perdita di WWOX nel **muscolo scheletrico** è *sufficiente* a produrre fenotipi metabolici locali e sistemici — il che rafforza la claim ma **non la trasferisce al CNS**: il modello è un KO condizionale muscolare, non un allele WWOX-DEE. Secondo confine, più stretto: fra le misure del paper **non c'è l'ossidazione mitocondriale del glucosio** (nessuna respirometria, nessun saggio di flusso), che fino a oggi [[meta_metabolism_current]] elencava come `DATO`. La claim resta `INFERENZA` e il suo `Type` non cambia. **Condizione per stringere:** flusso ex-vivo su fibre primarie o rescue muscolo-specifico.
**Impact on Working Model:** rationale support, not BLOCCO 1 upgrade yet
🔴 **BATCH_20260815_001:** [[paper_registry_current#PAPER 071]] adds a second counter-directional primary system: fly Wwox loss lowers, and overexpression raises, thresholded CM-H2DCFDA fluorescence, with Wwox×Idh and Wwox×Sod genetic interactions. This strengthens the claim's context-dependent redox boundary and does not license a monotonic direction or intervention.

---

## CLAIM 010
**Title:** Mitophagy may be more relevant than senolytics for WWOX-related mitochondrial dysfunction
**Status:** background only
**Type:** IPOTESI
**Pathway:** P5 — metabolism / mitochondria / mitophagy
**Genotype/model relevance:** sintesi meccanicistica speculativa — nessun modello specifico; non applicabile operativamente al genotipo di riferimento
**Transferability:** T4
**clinical relevance:** VERY LOW / BACKGROUND ONLY
**Summary:** If the core issue is damaged mitochondria rather than senescent cells, mitochondrial quality control is more relevant than senolysis.
**Clinical meaning:** Research framing only; not actionable for the reference genotype at present.
**Source:** mechanistic synthesis from WWOX + general mitochondrial literature
**Impact on Working Model:** none

---

## CLAIM 011
**Title:** AAV9-hSynI-hWWOX: dose-dependent durable rescue in Wwox-null murine model su domini multipli inclusi ECoG/SWD, mielinizzazione e gliosi
**Status:** flagged for review
🔴 **Flagged 2026-08-10 (`CC-20260810-CLAIM011-REVIEW`) — «dose-dependent» descrive un continuo dove il pannello mostra una soglia.** La Figura 3B di PMID 42422765, letta all'immagine (`gr3.jpg`, sha256 `c63f930c…4997d`): **LD = 1.23 × 10¹¹ vg**, **HD = 2.63 × 10¹¹ vg**; il braccio a dose bassa **non recupera la sopravvivenza** — sposta la morte da ~20 a ~90 giorni e poi la curva raggiunge lo zero, mentre l'alta dose plateau a ~80% fino a 300 giorni. A **P20** la dose bassa non ha corretto l'ipoglicemia, l'alta sì. Non è una differenza graduata su un asse: è qualitativa, e colloca una **soglia** fra 1.23 e 2.63 × 10¹¹ vg. Le parole del paper — *«dose-dependent»*, *«graded improvement»*, *«a clear dose-response relationship»* — sono tutte vere dei dati e tutte descrivono un continuo; la claim ne ha ereditato il lessico. Chi non apre il pannello B porta con sé *«più dose, più beneficio»* invece di *«sotto soglia, nessuna sopravvivenza»*, e le due credenze raccomandano trial diversi. 🔴 `PREMISE_TAG`: ogni inferenza del tipo *«una dose più bassa e più sicura aiuterebbe comunque»* legge la dose-risposta come continuo, e il pannello B la **rifiuta** per la sopravvivenza in questo modello. `REVIVAL_TRIGGER`: un braccio a dose intermedia fra 1.23 e 2.63 × 10¹¹ vg localizzerebbe la soglia — l'esperimento più informativo che questo paper implica. Riscrittura rinviata: la Figura 3B risolve sopravvivenza e glicemia, **non** gli altri domini della claim (ECoG/SWD, mielinizzazione, gliosi), e la lettura che li risolverebbe è `partial_fulltext_read`.
**Type:** DATO preclinico (full text reviewed)
**Pathway:** P7 — gene therapy readiness; P4 — myelination; P6 indiretto
**Genotype/model relevance:** murino / Wwox-null full KO severo; genotipo caution alta: full KO ≠ the reference genotype N/M compound het; i design principles (neuron targeting, dose, early window) sono trasferibili alla logica di trial-readiness; il livello di rescue atteso nel genotipo di riferimento è potenzialmente superiore (funzione residua parziale)
**Transferability:** T2
**clinical relevance:** HIGH
**Summary:** Nel modello murino Wwox-null severo, la terapia AAV9-hSynI-hWWOX con somministrazione ICV neonatale produce rescue dose-dependent e durevole su: sopravvivenza, crescita, glucosio, comportamento, mielinizzazione, gliosi, ipereccitabilità / SWD su ECoG (spike-wave discharges — surrogato elettrofisiologico delle crisi). Il rescue migliore emerge con targeting neuronale, controllo dell'espressione, calibrazione della dose, finestra postnatale precoce. Gliosi ridotta dopo rescue neuronale-specifico → parte di P6 è downstream della disfunzione neuronale, non solo processo gliale autonomo.
**Clinical meaning:** P7 matures from proof-of-concept to design-principle stage. Non cambia pratica immediata per il genotipo di riferimento. Rafforza trial-readiness logic e argomento per partial restoration (anche restore parziale è atteso benefico secondo Gao 2025).
**Source:** Obeid, Aqeilan et al. 2026, Molecular Therapy - Methods & Clinical Development (OMTA) vol 34 (peer-reviewed; versione published del preprint bioRxiv precedente — contenuto "dose-dependent durable rescue" identico nelle due versioni)
**Wikilinks:** [[paper_registry_current#PAPER 011]]
**Full text status:** complete article plus S1–S8 — latest receipt `FTR-20260814-42422765-06`
**Impact on Working Model:** BLOCCO 2 integrated; gene therapy context section updated in BLOCCO 1
🔴 **BATCH_20260815_001 boundary:** long-term W-AAV expression is regionally uneven and supraphysiological in surviving animals; P300 observations are survivor-selected and do not establish physiological replacement across CNS cell types. S2 reports `n=5` on graph labels and `n=4` in its caption.

---

## CLAIM 012
**Title:** Fenotipo WWOX severo neonatale-fatale con MRI inizialmente normale: genotipo-severità heterogeneity
**Status:** consolidated baseline
**Type:** DATO descrittivo (full text reviewed)
**Pathway:** clinical spectrum / genotype-phenotype
**Genotype/model relevance:** umano / singolo caso / delezione esoni 6–7 + frameshift esone 8 (null/null funzionale, probabilmente); genotipo severo diverso dal genotipo di riferimento (N/M); trasferibilità fenotipica: alta per EEG/MRI timing lesson; trasferibilità terapeutica: nulla
**Transferability:** T1 phenotypic
**clinical relevance:** MODERATE
**Summary:** Caso umano con delezione esoni 6–7 + frameshift esone 8: crisi nelle prime ore di vita, microcefalia, EEG multifocale patologico, MRI precoce normale, decesso a 3 mesi. MRI normale in fase precoce non esclude disfunzione di rete severa. Rafforza EEG come endpoint più sensibile dell'imaging nelle fasi iniziali in WWOX-DEE.
**Clinical meaning:** Supporta genotype-severity heterogeneity. Non valida "WOREE syndrome plus" come sottotipo operativo. Rafforza cautela nel confrontare casi WWOX tra loro.
**Source:** Sapuppo et al., 2026, Curr Issues Mol Biol 48(5):449; PMID 42193054; DOI 10.3390/cimb48050449 (peer-reviewed; versione published del preprint precedente)
**Wikilinks:** [[paper_registry_current#PAPER 012]]
**Full text status:** reviewed
**Impact on Working Model:** BLOCCO 2 integrated; EEG priority note added to monitoring section

---

## CLAIM 013
**Title:** In WWOX-DEE, genotipi biallelici null/null associati a maggiore rischio di crisi, ipertonia e complicanze respiratorie rispetto ai genotipi con almeno una variante missense
**Status:** in observation
**Validation:** validazione dell'operatore richiesta
**Type:** DATO con limiti metodologici dichiarati
**Pathway:** Clinical spectrum / genotype-phenotype / P2 / sorveglianza respiratoria
**Genotype/model relevance:** umano / cohort pediatrico / 50 individui biallelic WWOX; classificazione N/N vs N/M vs M/M; survey parentale con bias di sopravvivenza; la classe N/M (un allele missense + un allele splice a null atteso) è la classe di riferimento di questo modello; Q230P presente in 2 individui nel cohort
**Transferability:** T1
**clinical relevance:** HIGH
**Summary:** Studio su 50 individui con varianti bialleliche WWOX (più grande cohort pubblicato). Solo 3 associazioni statisticamente significative dopo correzione FDR Benjamini-Hochberg: ipertonia (p=0.003; N/N 72% vs N/M 23% vs M/M 17%), crisi (p=0.016; N/N 100% vs N/M 92% vs M/M 67%), complicanze respiratorie (p=0.020; N/N 76% vs N/M 31% vs M/M 50%). Drug resistance, feeding, MRI, disabilità globale: non differiscono significativamente tra genotipi. Bias di sopravvivenza documentato (registro parentale). una classe N/M (allele missense + allele splice classificabile null) si colloca fuori dal gruppo N/N a rischio più alto, ma non autorizza riduzione della vigilanza. Q230P presente in 2 individui nel cohort; case ID 11 (N/M: null+Q230P) è l'unico deceduto nel cohort (causa sconosciuta).
**Clinical meaning:** Rafforza lettura genotype-aware per crisi, tono, respiratorio. Non cambia strategia terapeutica immediata. Supporta sorveglianza respiratoria strutturata anche nei profili N/M. Partial restoration (anche parziale) attesa benefica secondo gli autori.
**Source:** Gao K et al., *Neurology* 2025;105:e213883. PMID 40875931. DOI 10.1212/WNL.0000000000213883
**Wikilinks:** [[paper_registry_current#PAPER 014]]
**Full text status:** reviewed (PDF fornito dall'operatore)
**Impact on Working Model:** BLOCCO 2 in observation; proposta raffinamento BLOCCO 1 sezione "Note on Q230P" — in attesa validazione dell'operatore

---

## CLAIM 014
**Title:** WWOX loss perturbs prenatal cortical development, neuronal migration and cortical maturation across species
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** P3 — neurodevelopment / migration / cortical assembly
**Genotype/model relevance:** umano fetale + rat lde/lde + hNPC; modelli severi/null-like; trasferibilità meccanicistica moderata con cautela al genotipo di riferimento N/M
**Transferability:** T2
**clinical relevance:** HIGH
**Summary:** Across fetal human tissue, rat lde/lde and human neural progenitor models, WWOX loss is associated with impaired neuronal migration, altered cortical layering, dysregulated cytoskeleton-related developmental programs, and defective cortical maturation with downstream hypomyelination/glial-development abnormalities.
**Clinical meaning:** Strongly supports the reading that part of WWOX-DEE may arise on a prenatal/early structural substrate, not only on postnatal network instability.
**Source:** Iacomino et al. 2020 / **Tochigi** et al. 2019 / Kośla et al. 2019
**Wikilinks:** [[paper_registry_current#PAPER 020]] (Iacomino) · [[paper_registry_current#PAPER 021]] (Tochigi) · [[paper_registry_current#PAPER 022]] (Kośla)
**Evidence boundary (BATCH_20260806_002):** the multi-paper convergence is retained, but **PMID 31340538 (Tochigi) contributes early postnatal maturation and hypomyelination at PND5–21 — not prenatal migration, not cortical layering, and no directly observed prenatal assembly.** It measures no prenatal time point. Its record previously carried an invented title naming *lissencephaly*, which had been steering it toward a migration/layering reading the study does not make. The prenatal component of this claim therefore rests on Iacomino and Kośla, not on this paper.
**Impact on Working Model:** supports P3 as central structural axis and tightens link P3↔P4; no direct operational change

---

## CLAIM 015
**Title:** Part of WWOX-related epileptic encephalopathy likely arises on a structurally misassembled prenatal cortical substrate
**Status:** consolidated baseline
**Type:** INFERENZA strongly supported
**Pathway:** P3 / P1 / P4
**Genotype/model relevance:** inferenza da convergenza di modelli severi (paper 97, 93, 163, 87); null/null-like ≠ the reference genotype; applicabile come framework con cautela
**Transferability:** T2 conceptual
**clinical relevance:** HIGH
**Summary:** The convergence of impaired migration, cortical misassembly, layering defects, hypomyelination, glial-maturation abnormalities and early network hyperexcitability strongly suggests that part of WWOX-DEE is developmentally pre-wired rather than generated only postnatally.
**Clinical meaning:** Refines interpretation of EEG severity and explains why early MRI may underestimate structural burden. Supports a structural reading of WWOX-DEE without implying a direct treatment change for the reference genotype.
**Source:** Iacomino 2020 / Cheng 2020 / **Tochigi** 2019 / Repudi 2021
**Wikilinks:** [[paper_registry_current#PAPER 020]] (Iacomino) · [[paper_registry_current#PAPER 019]] (Cheng) · [[paper_registry_current#PAPER 021]] (Tochigi) · [[paper_registry_current#PAPER 004]] (Repudi Brain)
**Evidence boundary (BATCH_20260806_002):** *"developmentally pre-wired"* must not be read as *"prenatally demonstrated"*. **PMID 31340538 (Tochigi) is an early postnatal study (PND5–21)** and contributes maturation and hypomyelination, not prenatal misassembly; it is the postnatal bridge between the prenatal core and P4, not one of the prenatal measurements. Its author and title were corrected in this batch after the full-text read.
**Impact on Working Model:** strengthens structural reading of the reference genotype; now baseline-level conceptual support

---

## CLAIM 016
**Title:** GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency
**Status:** in observation
**Type:** DATO (abbondanza, murino) + **DATO meccanicistico risolto a livello di residuo** (biochimica, [[paper_registry_current#PAPER 056]]) + INFERENZA prudente (trasferimento clinico)
**Pathway:** emerging node — GSK3β / seizure susceptibility
**Genotype/model relevance:** murino / Wwox-null full KO; litio-sensitive PTZ phenotype in severe model; non trasferibile operativamente al genotipo di riferimento
**Transferability:** T2 mechanistic / T4 clinical
**clinical relevance:** MODERATE
**Summary:** In Wwox-null mice, GSK3β is elevated in cortex, hippocampus and cerebellum, and lithium significantly suppresses PTZ-induced seizure susceptibility. Within the structural block, this suggests GSK3β acts more plausibly as an amplifier of an already misassembled/vulnerable system than as a standalone upstream driver.
**Meccanismo aggiunto (BATCH_20260726_001):** WWOX non è soltanto correlata al livello di GSK3β — ne è un **inibitore fisico diretto**, tramite il motivo di docking Axin-like 388–407/L404 del dominio SDR ([[paper_registry_current#PAPER 056]], [[claim_registry_current#CLAIM 035]]). L'affermazione causale si sposta quindi da *«GSK3β è elevata»* (osservazione di abbondanza) a *«GSK3β è de-repressa»* (perdita di un freno fisico). L'inibizione è **S9-indipendente**: nel sistema di Wang la fosfo-S9 e l'abbondanza di GSK3β restano invariate mentre l'output della chinasi cambia.
**🔴 `PREMISE_TAG` sul claim esistente:** la premessa portante di CLAIM 016 è che **l'abbondanza di proteina GSK3β riporti l'attività di GSK3β**. `PREMISE: DEFAULT_FROM_TEXTBOOK`. In questo sistema abbondanza e attività sono **dissociabili**: la premessa è un **bersaglio di ricerca**, non una fondazione.
**Clinical meaning:** High-value mechanistic node and research line. Not a clinical candidate for the reference genotype at present. **Lo stato resta `in observation`, non `consolidated baseline`:** il consolidamento richiede ≥3 studi convergenti o uno studio ad alto impatto, e le fonti sono **due** (Cheng 2020, Wang 2012) su una densità di campo di `WWOX AND GSK3` = 5 record in tutto PubMed. L'acquisizione di [[full_text_queue_current#FT-024]] (Sze 2004) porterebbe a tre e giustificherebbe la rivalutazione.
**🔴 Evidence boundary — il braccio litio NON è genotipo-specifico (propagato 2026-08-10, `BATCH_20260810_005`).** Il `Summary` sopra riporta che *«lithium significantly suppresses PTZ-induced seizure susceptibility»* in topi Wwox-null, e la frase è vera del testo del primario ([[paper_registry_current#PAPER 019]], PMID 32000863: *«Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice»*). **La figura dice qualcosa di più largo, e lo diceva già.** Il locator letto all'immagine in `deepdive_manifests/PMID32000863.json` registra che **il litio ha soppresso le crisi da PTZ in TUTTI E TRE i genotipi, wild-type incluso** (Fig. 7b; per l'etosuccimide il testo dichiara `n.s.` in `+/+` e `+/−` e significativo in `−/−`, e per il litio **non dichiara il converso**). ⇒ **l'esperimento non stabilisce un rescue farmacologico WWOX-specifico**: mostra un anticonvulsivante che funziona, in un modello che ha crisi. Lo stesso scarto è stato ritrovato indipendentemente dall'altra direzione: la review **Steinberg & Aqeilan 2021** (PMID 34831305, promossa a record in questo stesso batch) trasmette la lettura genotipo-specifica che il pannello del primario non sostiene — **una sintesi che stringe ciò che la fonte aveva lasciato largo**. *(Il record della review è citato deliberatamente per PMID e non per wikilink: `CLAIM 016` è una delle tre claim bersaglio del bundle cieco DisMech, e ogni identificatore di paper dentro il suo blocco entra nell'insieme di input di quell'export. Il primario resta la fonte; la review è contesto corroborante.)* 🔴 `PREMISE_TAG`: ogni inferenza della forma *«il litio aiuta perché il bersaglio è GSK3β de-repressa»* poggia su una specificità di genotipo che **questo esperimento non ha misurato**. `REVIVAL_TRIGGER`: un braccio PTZ+litio con confronto **esplicito e testato** fra `−/−` e `+/+`, oppure un inibitore diverso con lo stesso disegno. **Cosa NON cambia:** il dato di abbondanza, il meccanismo a livello di residuo di [[paper_registry_current#PAPER 056]], e lo stato `in observation`. Il locator esisteva dal giorno della lettura e non era mai arrivato fin qui: è un difetto di propagazione, non di lettura.
**Source:** Cheng et al. 2020 · [[paper_registry_current#PAPER 056]] (Wang 2012 — meccanismo a livello di residuo)
**Wikilinks:** [[paper_registry_current#PAPER 019]] · [[paper_registry_current#PAPER 056]] · [[claim_registry_current#CLAIM 035]]
**Impact on Working Model:** no BLOCCO 1 change; research-line priority increased. Il razionale meccanicistico di TX-005 si rafforza (si perde un freno, non solo un livello); **l'argomento di sicurezza no** — vedi [[dismissal_ledger_current#DIS-009 — «Un WWOX-mimetico (WWOXtide³⁸⁸⁻⁴⁰⁷) sarebbe più sicuro del litio, perché WWOX inibisce GSK3β in modo substrato-selettivo» → ❌ **RIGETTATA**]].

---

## CLAIM 017
**Title:** WWOX-related human disease spans a spectrum from severe WOREE/WWOX-DEE to milder SCAR12-like phenotypes
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** human spectrum / genotype-phenotype
**Genotype/model relevance:** human case reports, cohorts and reviews; directly relevant to the reference genotype because it frames severity interpretation
**Transferability:** T1
**clinical relevance:** HIGH
**Summary:** Human WWOX disease is not phenotypically uniform: the severe end is WOREE/WWOX-DEE with profound developmental and epileptic encephalopathy, whereas milder phenotypes such as SCAR12 are associated with slower development, later seizure onset and survival into later childhood/adulthood.
**Clinical meaning:** Supports genotype-aware counseling and prevents collapsing all WWOX cases into a single severity profile.
**Addition (BATCH_20260909_001, PMID 33916893 — [[paper_registry_current#PAPER 040]]; R4 satisfied).** This source places **long survival inside the severe end as well**: within DEE28, alive at **12 y and 10 y** (homozygous **missense** Q230P), **8 y 11 m and 5 y 2 m** (homozygous **nonsense** R264\*), **7 y** (homozygous nonsense W44\*), **6 y**, and alive at **7 y**. **The spectrum is not fully partitioned by genotype**, and the largest severity variance in this table is *within* a genotype rather than between syndromes.
🔴 **A warning attached to this claim, raised by the audit.** The review's own §2 sentence «death by the age of 1–4 years» is a **generalisation cited to Piard [5]**, not a result derived from the review's own dataset — and **the review's own tables falsify it seven times**. **It must not be promoted into any claim without that qualifier**, because doing so would silently *narrow* `CLAIM 017` and [[claim_registry_current#CLAIM 020]].
**Source:** Abdel-Salam 2014 / Piard 2018 / Oliver 2023 / Teplyshova 2024 / Banne 2021 ([[paper_registry_current#PAPER 040]])
**Wikilinks:** [[paper_registry_current#PAPER 025]] (Piard) · [[paper_registry_current#PAPER 018]] (Oliver) · [[paper_registry_current#PAPER 015]] (Teplyshova) · [[paper_registry_current#PAPER 040]] (Banne 2021) — Abdel-Salam 2014 corpus, non in registry
**Impact on Working Model:** supports human-spectrum framing without changing BLOCCO 1

---

## CLAIM 018
**Title:** The exon 6 splice-site variant c.517-2A>G is pathogenic and causes exon 6 skipping in humans
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** genotype / splicing / pathogenicity
**Genotype/model relevance:** directly relevant because this allele sits in the reference genotype logic
**Transferability:** T1
**clinical relevance:** HIGH
**Summary:** Human data support that c.517-2A>G is a pathogenic splice-site variant causing exon 6 skipping. This establishes it as a true loss-of-function / null-like allele rather than an uncertain sequence variant.
**Clinical meaning:** Strengthens the interpretation of the reference genotype as carrying a null-like splice allele in compound context.
**Source:** Weisz-Hubshman / Piard 2019 abstract-supported + prior claim integration
**Wikilinks:** [[paper_registry_current#PAPER 025]] (Piard)
**Impact on Working Model:** reinforces genotype logic; no direct therapeutic change

---

## CLAIM 019
**Title:** Q230P is pathogenic in severe human compound context and must not be treated as a benign or weak missense by default
**Status:** consolidated baseline
**Type:** DATO (endpoint funzionale: mRNA normale + proteina non rilevata) + IPOTESI (causa e recuperabilità)
**Pathway:** genotype / compound-context interpretation
**Genotype/model relevance:** directly relevant to the reference genotype
**Transferability:** T1/T2
**clinical relevance:** HIGH
**Summary:** Human reports place p.Gln230Pro (Q230P) within severe WWOX-DEE / WOREE phenotypes, including compound contexts with a null-like allele. This argues against interpreting Q230P as a mild missense by default.
**Clinical meaning:** Supports reading the reference genotype's genotype as N/M severe-risk logic rather than a trivially attenuated missense combination.
**Source:** Oliver 2023 / Weisz-Hubshman-Piard 2019 abstract-supported / human spectrum literature. — Supporto IN-SILICO multi-metodo convergente (IPOTESI, 2026-07-04, `INBOX-003` — quarantine record, private overlay): (1) AlphaFold AF-Q9NZC7-F1 + SASA/SSE colloca Gln230 nel core SDR, in un segmento elicoidale ben confident; (2) ThermoMPNN Q230P ΔΔG **+1.514 kcal/mol** (non misura sperimentale e non predittore di severità); (3) ESM-2 650M LLR -9.08. Questi dati rendono plausibile una perturbazione di folding/packing, ma non dimostrano né degradazione né recuperabilità. L'annotazione precedente di C299R come lesione catalitica/off-lid è ritirata: la distanza 3.44 Å usata era backbone-backbone; SG(C299)-NZ(K297) = 10.706 Å e C299 contatta H233 nel modello. Validazione wet → [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013 — Validazione sperimentale instabilità Q230P]]. Implicazione terapeutica (IPOTESI, non DATO): Q230P può essere candidata a rescue solo dopo aver distinto sintesi, solubilità e turnover e dimostrato funzione della proteina recuperata ([[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]]). Nessun cambio BLOCCO 1.

— **DATO FUNZIONALE, CAUSA NON RISOLTA (BATCH_20260710_A; corretto da BATCH_20260714_001, [[paper_registry_current#PAPER 041]]).** Johannsen et al. 2018, *Neurogenetics* 19(3):151-156 (PMID 29808465) studia **esattamente Q230P** in due sorelle omozigoti. Nei **fibroblasti di paziente**: **qRT-PCR → livelli di trascritto WWOX normali; Western blot → proteina WWOX non rilevata**. Gli autori lasciano aperte due alternative: **traduzione compromessa oppure degradazione prematura**. Non misurano sintesi, solubilità, emivita o via di smaltimento. Il DATO è quindi l'endpoint `mRNA normale + proteina non rilevata`, non un meccanismo post-traduzionale.
— **Implicazione terapeutica (IPOTESI, non DATO):** boost dell'espressione e rescue proteostatico restano entrambi **condizionati**. Il boost non è falsificato dalla sola normalità dell'mRNA, perché il collo di bottiglia potrebbe essere traduttivo; il rescue proteostatico richiede prima prova di turnover accelerato sulla variante esatta. Se Q230P fosse degradata, la via HSC70/lisosomiale osservata per P252A è un'**IPOTESI PONTE**, non prova di CMA, del motivo `LRSVQ` o del trigger elicoidale. Il test decisivo deve separare sintesi, insolubilità e degradazione e associare l'abbondanza a un readout funzionale. Vedi anche [[claim_registry_current#CLAIM 032]]: un rescue efficace potrebbe non dover essere completo.
— **Implicazione prognostica, da non attenuare:** se Q230P non produce proteina, the reference genotype — formalmente `null/missense` — potrebbe essere **funzionalmente null/null**. Contrappesi fattuali: nella coorte Oliver 2023 un paziente **Q230P omozigote** è il **più anziano dello studio (23 anni e 11 mesi, vivo)**; un altro Q230P omozigote è **morto a 8 anni**; il paziente con **Q230P + delezione** (la combinazione più vicina a quella del genotipo di riferimento) è **vivo a 4 anni e 7 mesi**. La variabilità individuale è ampia.
— ⚠️ **CORREZIONE INTERNA (BATCH_20260710_A; irrigidita da BATCH_20260714_001).** L'euristica *"finestra recuperabile ΔΔG 0.8–3.5"* è ritirata: non ha valore predittivo dimostrato. Il contesto strutturale WT rende Q230P una perturbazione di core plausibile, ma resta AlphaFold/in-silico e non dimostra misfolding, degradazione o uno stato foldato recuperabile. Non esiste una struttura sperimentale del dominio SDR di WWOX. Vedi [[claim_registry_current#CLAIM 030]].
— **Addition (BATCH_20260909_001, PMID 33916893 — [[paper_registry_current#PAPER 040]]; R4 satisfied, two independent blind audits).** In this review's cohort **Q230P is present in 8 patients across 6 families — 4 homozygous** (Afghan ×2, Moroccan, Iranian) **and 4 compound heterozygous** (2 French; 2 Yemenite in trans with the `c.517-2A>G` splice allele). **All 8 sit in the DEE28/WOREE block and none in SCAR12.** Figure 3B independently draws Q230P at the axis maximum, the tallest lollipop of **any** mutation class. So the claim's evidence is **broader than "compound context"**: Q230P is pathogenic **homozygous** as well, and it is the most recurrent single WWOX allele in the 2021 census. **And a counterweight the claim absorbs:** within **homozygous** Q230P alone the recorded endpoint spans **death at 3 y 3 m** to **alive at 12 y and 10 y**. **Q230P is severe without being deterministic for early death.** ⚠️ These are **secondary-source facts awaiting primary verification** — `PAPER 041` (Johannsen 2018, PMID 29808465), the only functional study of Q230P, is held here as abstract only and is the highest-value acquisition target in this lot. `PREMISE: INFERENZA` on any mixing of death ages with last-examination ages.
**Wikilinks:** [[paper_registry_current#PAPER 041]] (Johannsen — fonte funzionale primaria) · [[paper_registry_current#PAPER 042]] (Mallaret — P47T) · [[paper_registry_current#PAPER 018]] (Oliver) · [[paper_registry_current#PAPER 025]] (Piard) · [[paper_registry_current#PAPER 040]] (Banne 2021 — census) · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 032]] · [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013 — Validazione sperimentale instabilità Q230P]]
**Impact on Working Model:** genotype interpretation strengthened; no BLOCCO 1 change

---

## CLAIM 020
**Title:** Selected WWOX-related trajectories may include survival into adulthood with severe disability and late motor regression
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** natural history / clinical spectrum
**Genotype/model relevance:** umano single case with different genotype from the reference genotype; transferable as natural-history possibility, not prognosis
**Transferability:** T1 phenotypic
**clinical relevance:** MODERATE
**Summary:** Adult survival with persistent severe disability and possible late motor regression is documented in at least one WWOX-DEE case (40 years follow-up).
**Clinical meaning:** Refines natural-history expectations and supports long-horizon respiratory and functional surveillance. Not predictive for the reference genotype individually.
**Source:** Teplyshova & Sharkov 2024
**Wikilinks:** [[paper_registry_current#PAPER 015]]
**Impact on Working Model:** long-term spectrum broadened; no immediate treatment change


---

## CLAIM 021
**Title:** WWOX loss directly destabilizes neocortical network physiology through combined synaptic and intrinsic mechanisms
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** P1 — network hyperexcitability / cortical oscillatory disorganization
**Genotype/model relevance:** modello animale / meccanicistico — neuron-specific Wwox loss; non null/null sistemico; trasferibilità meccanicistica moderata al genotipo di riferimento N/M
**Transferability:** T2
**clinical relevance:** HIGH
**Summary:** Neuron-specific Wwox loss is associated with spontaneous neocortical bursting activity, altered oscillatory organization and increased phase-amplitude coupling. Layer 2/3 pyramidal neurons show increased excitatory drive, reduced spontaneous inhibition, depolarization, increased firing, increased sag and post-inhibitory rebound. Bursting depends on NMDAR and gap junction activity. This supports a model in which WWOX-related epileptic encephalopathy includes a primary network-state pathology, not only secondary seizures or developmental damage.
**Clinical meaning:** Eleva la network-state pathology a core-pathway status. Rafforza la lettura che l'EEG disorganizzato del genotipo di riferimento rifletta una disfunzione primaria di stato di rete, non solo attività epilettiforme secondaria. Non cambia la pratica immediata.
**Source:** Breton et al., *Neurobiol Dis* 2021;160:105529 (full-text verificato 2026-07-05); PMID 34634460 / PMCID PMC8609180 / DOI 10.1016/j.nbd.2021.105529.
**Wikilinks:** [[paper_registry_current#PAPER 031]]
**Impact on Working Model:** strengthens ACTIVE 1 / network hyperexcitability as core pathway; no BLOCCO 1 operational change

---

## CLAIM 022
**Title:** Severe WWOX-null phenotypes can begin prenatally and may include detectable fetal brain abnormalities
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** prenatal developmental architecture / severe human spectrum
**Genotype/model relevance:** umano / caso fetale con delezione omozigote primi sei esoni WWOX (null); stesso contesto familiare supporta genotipo null severo-letale precoce; non direttamente transferable to a case N/M ma rilevante come framework per la severità null-null
**Transferability:** T1 phenotypic (null-severe context) / framework only per il genotipo di riferimento
**clinical relevance:** HIGH per framework / INDIRECT per trattamento
**Summary:** Homozygous deletion involving the first six exons of WWOX was identified in a fetus with prenatal brain abnormalities. This indicates that severe WWOX disease should not be modeled as purely postnatal seizure-driven deterioration. In null genotypes, developmental disorganization may begin in utero.
**Clinical meaning:** Rafforza il reading strutturale-prenatale del modello WWOX-DEE. Aumenta il peso del substrato prenatal/developmental nell'interpretazione dei casi null-severi. Non cambia il framework N/M per il genotipo di riferimento, ma rafforza la plausibilità che parte del fenotipo sia pre-wired.
**Source:** paper 216 (corpus 181–220)
**Wikilinks:** [[paper_registry_current#CORPUS P216]]
**Impact on Working Model:** increases weight of prenatal/developmental branch in null-severe reasoning; strengthens RL-007; no direct BLOCCO 1 change

---

## CLAIM 023
**Title:** WWOX controls partner-protein function not only by binding, but by subcellular rerouting that changes downstream biological output; Tyr33 phosphorylation regulates the **binding**, and its effect on rerouting is untested
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** signaling organization / routing / scaffold logic
**Genotype/model relevance:** studio meccanicistico su WWOX–p73; WW1-mediated binding; fosforilazione Tyr33; non modello CNS pediatrico diretto; rilevante come principio architetturale
**Transferability:** T2 mechanistic / indirect for the reference genotype
**clinical relevance:** INDIRECT — structurally important for model architecture
**Summary:** WWOX binds p73 via WW1; Tyr33 phosphorylation enhances binding; WWOX relocalizes p73 from nucleus to cytoplasm, reducing nuclear transcriptional activity while cytoplasmic cooperation contributes to proapoptotic output. WWOX should be modeled as a routing/scaffold regulator, not merely a passive binding protein.
**Clinical meaning:** Non cambia la pratica immediata per il genotipo di riferimento. Cambia il linguaggio concettuale con cui leggere WWOX biology: non solo "quanta proteina" ma "dove va la proteina e chi trascina con sé".
**Evidence boundary (BATCH_20260909_001 — NARROWING of a `consolidated baseline` title, R4 satisfied).** 🔴 **The summary was faithful and the title was not.** The summary lists three *separate* facts; the title welded two of them into a **causal relation** — that the rerouting is *phosphorylation-dependent* — and **no experiment in the source manipulates phosphorylation and measures localisation.** Made machine-checkable rather than asserted: **20 sentences in the body mention Src, and ZERO of them also mention localisation, cytoplasm, nucleus, redistribution or sequestration**, confirmed by both blind auditors, one with a ±400-character proximity screen whose only near-misses are adjacent sentences. Fig 4 is entirely binding and phospho-blot biochemistry; Fig 2 and Fig 5 are localisation **with no Src arm**. **The binding leg is not weakened — it is the best-supported content in the paper** (bidirectional co-IP, endogenous interaction in two cell types, PPxY dependence confirmed three ways, direct GST pull-down with the isolated first 50 aa, p53 excluded as a specificity control), and `Status` stays `consolidated baseline`. Three qualifications now travel with the routing leg: (1) it is **overexpression-dependent by the authors' own words** — *"Overexpression of Wwox caused the redistribution of p73 from the nuclear compartment to the cytosol."*; (2) the paper's only graded-dose titration (Fig 5) carries **no dose labels, no merged channel, no cell count, no n and no statistic**, while the proposition it supports is about a *proportion*, and the Wwox-positive **area** in the reduced-dose field is **not lower** than in the higher-dose field; (3) **the modal dies inside the paper** — Results say *"suggesting that phosphorylation enhances this interaction"*, the Discussion four paragraphs later says *"We have also demonstrated specific phosphorylation of Y33."* ⚠️ Fig 5 has **no caption** on either surface, so which panel is the reduced dose is an **assumption, not a datum**. Change class **ORDINARY**: an untested coupling is removed from a title; the claim is not reversed, not removed, and the working model's architecture is unchanged.
**Corroboration (BATCH_20260909_001 — the *"not only by binding"* leg, independent source).** [[paper_registry_current#PAPER 086]] (PMID 21115974, Fu 2011, *Blood*; group **Xiao**, not the Aqeilan group) corroborates the headline leg from a different literature: **Y33R binds Tax and still fails to suppress it**, and the authors state it outright (Fig 6C read at 850%, Fig 4B/4D, Fig 5). 🔴 **Its mechanism leg is NOT narrowed and remains unresolved**: that paper *asserts* WWOX does not relocalise Tax **on unshown data**, and the cited supplement cannot carry it — Figure S2A has Myc-WWOX in all eight lanes with no WWOX-negative comparator and no Tax input row, so it shows where the *complex* is recovered, never where Tax *goes*. A third mode is observed and typed `INFERENZA`: WWOX blocks the **Tax-mediated increment** of IKKα recruitment to RelA, returning it to the Tax-negative baseline.
**Source:** [[paper_registry_current#PAPER 081]] (PMID 15070730, Aqeilan 2004, *PNAS* — **the identified primary source of this claim's mechanism**, established by `FTR-20260909-15070730-02` and independently corroborated as reference 19 of PMID 21115974) · [[paper_registry_current#PAPER 086]] (PMID 21115974 — corroboration of the binding-independence leg only) · `CORPUS P206` (the historical placeholder, preserved append-only)
**Wikilinks:** [[paper_registry_current#PAPER 081]] · [[paper_registry_current#PAPER 086]] · [[paper_registry_current#CORPUS P206]]
**Impact on Working Model:** foundational principle for future reading of WWOX partner biology; relevant to genotype interpretation framework. **`BATCH_20260909_001`: the working-model narrative line that named Tyr33-dependent relocalization as the anchoring example is narrowed in step with this title — the mirror moves with the claim.**
⚠️ **Provenance, reported and not repaired by the reading that found it:** this claim descended from `CORPUS P206`, a placeholder whose `Identifier` was the literal string `PENDING` and whose note flagged a possible overlap with [[paper_registry_current#PAPER 026]] (PMID 32185845). The overlap is **disproved** — the source is PMID 15070730 — but `PAPER 026` remains **abstract-only** and reports the **opposite direction** for the Tyr33 effect (phosphorylation *decreases* affinity for a p73-derived peptide). That tension is recorded, not resolved: an abstract has no parity with a complete full-text read.
**Reading debt:** PMID 12514174 (Chang et al., murine Wox1/JNK) is the source of the entire Y33 rationale and this corpus does not hold it — `PREMISE: DATO` in the source, *a `DATO` never verified here*.

---

## CLAIM 024
**Title:** WWOX WW-domain function depends on WW1–WW2 tandem cooperativity, not only on isolated domain integrity
**Status:** consolidated baseline
**Type:** DATO
**Pathway:** domain architecture / variant interpretation
**Genotype/model relevance:** studio strutturale/meccanicistico su architettura WW domain; WW2 non è un dominio PPxY-binding standalone ma contribuisce a stabilità tandem e riconoscimento target; rilevante per interpretazione varianti missense in WW domain
**Transferability:** T2 — indirect but high for genotype interpretation framework
**clinical relevance:** INDIRECT — high for genotype interpretation
**Summary:** WW2 is not a canonical standalone PPxY-binding domain, but contributes to tandem stability and target recognition. Cooperative WW1–WW2 architecture improves recognition of dual PPxY-containing partners. Variants in WW domains should not be interpreted domain-by-domain in isolation; disruption of tandem cooperativity may alter stability, partner selection and residual function.
**Precisazione meccanicistica (BATCH_20260726_001, fonte primaria identificata):** WW2 contribuisce con **due meccanismi distinti** — pre-ordina/stabilizza il WW1 altrimenti instabile, **e** può ingaggiare direttamente un secondo motivo PPxY quando sequenza, spaziatura, linker e orientamento creano una topologia compatibile. ⚠️ Ma l'effetto WW2 diretto più grande in [[paper_registry_current#PAPER 055]] si ottiene con **peptidi tandem ingegnerizzati a linker corto**; il PY1PY2 nativo di ErbB4 guadagna affinità e resta comunque prevalentemente legato a WW1. **La sola presenza di due motivi PPxY non stabilisce quindi l'occupazione di WW2** — la topologia del partner fa parte dello stato funzionale.
**Clinical meaning:** Cambia il framework interpretativo per varianti in WW domain. Non applicabile direttamente a Q230P (SDR domain), ma rafforza la regola generale: la biologia WW domain è cooperativa, non additiva.
**Source:** [[paper_registry_current#PAPER 055]] (Rotem-Bamberger et al., *J Biol Chem* 2022; PMID 35716775; PMCID PMC9293652; DOI 10.1016/j.jbc.2022.102145) — fonte primaria identificata. Il pointer storico `paper 204 (corpus 181–220)` è conservato come audit trail: la coincidenza fra il placeholder e questa pubblicazione **non è stata confermata**, quindi il placeholder non è stato fuso.
**Wikilinks:** [[paper_registry_current#PAPER 055]] · [[paper_registry_current#CORPUS P204]]
**Impact on Working Model:** changes conceptual language for interpreting WWOX missense/domain variants; no direct BLOCCO 1 change

---

## CLAIM 025
**Title:** The WWOX/HIF1A ratio may function as a systems-level marker of maladaptive biological state, linking glycolysis, inflammatory tone and Wnt-related signaling
**Status:** in observation
**Type:** DATO + INFERENZA
**Pathway:** P5 — metabolism / state transition / inflammatory-metabolic coupling
**Genotype/model relevance:** studio su leucociti umani non tumorali (GDM); WWOX ridotto, HIF1A aumentato, ratio marcatamente ridotto; cross-context support da dati translazionali multipli; non CNS pediatrico diretto
**Transferability:** T2 conceptual — human non-tumoral support strong; CNS transferability indirect
**clinical relevance:** INDIRECT — high for model architecture
**Summary:** In human GDM leukocytes, WWOX is reduced, HIF1A is increased, and the WWOX/HIF1A ratio is markedly decreased. Lower ratio associates with increased expression of glycolytic genes and correlates with inflammatory and Wnt-related components. Cross-context data suggest the ratio captures more than glycolysis alone; it functions as a state marker of maladaptive biology rather than a narrow Warburg-only axis.
**Clinical meaning:** Raffina CLAIM 009: il branch metabolico non si riduce a HIF1A/glicolisi ma include inflammatory-metabolic coupling e possibili Wnt-adjacent state shifts. Non cambia la pratica per il genotipo di riferimento; rafforza il razionale di KD e supporto mitocondriale.
**Evidence boundary (2026-09-09, PMID 29724996 — [[paper_registry_current#PAPER 091]]).** The HIF1α axis is confirmed **in vivo** in mouse liver, where WWOX deletion raises HIF1α occupancy on glycolytic promoters. Two boundaries come with it. **The occupancy evidence is closed at five promoters** — PKM, GAPDH, HK2, Glut1, Aldoa — so it does **not** cover *Pdk1* or *Ldha*. And **the responding gene set is context-dependent**: under high-fat diet PKM2, the target with the strongest ChIP enrichment, is not elevated at all, while PDK1/LDHA1/ENO1 are. The ratio may be a state marker; **the gene set that reports it is not fixed**, so no single transcript should be treated as its invariant readout. `Status` unchanged (`in observation`); no baseline is reversed and no evidence is demoted. The source is liver, carcinogen-driven and carries **no neural endpoint** — nothing transfers to CNS on this route, and digoxin is not promoted.
**Source:** paper 191 (corpus 181–220)
**Wikilinks:** [[paper_registry_current#CORPUS P191]]
**Impact on Working Model:** strengthens P5 / metabolism branch; integrates with meta_metabolism update; no BLOCCO 1 operational change
**Nuance (Obeid 2026 review / Lucas-Clarke 2025):** a Drosophila model shows a WWOX metabolic effect that is HIF1α-INDEPENDENT (via ATF4/UPR; neuroprotection via methionine suppression, not lactate). Not a direct contradiction (different system) but it tempers the HIF1A-centric framing of this claim. Status unchanged (in observation); primary queued FT-009.

---

## CLAIM 026
**Title:** WWOX may function as a trafficking–metabolism coupling node linking endomembrane systems with catabolic pathways converging on Acetyl-CoA
**Status:** in observation
**Type:** DATO + INFERENZA
**Pathway:** P5 — trafficking / endomembrane systems / metabolism
**Genotype/model relevance:** dati da interactome + pathway analysis; non modello CNS pediatrico diretto; altamente rilevante come principio architetturale metabolico
**Transferability:** T2 conceptual — indirect, potentially high for future research
**clinical relevance:** INDIRECT — potentially high for future research
**Summary:** High-confidence WWOX interactors include ER/Golgi/endosomal/lysosomal trafficking proteins. Enriched pathways include glycolysis/gluconeogenesis, pyruvate metabolism, fatty acid degradation and branched-chain amino acid degradation, with multiple pathways converging on Acetyl-CoA generation. WWOX metabolic biology may involve compartmental organization and intracellular logistics, not only transcriptional regulation of glycolysis.
**Clinical meaning:** Non cambia la pratica immediata per il genotipo di riferimento. Apre un asse di ricerca di alto valore: la disfunzione metabolica WWOX-related potrebbe essere in parte una disfunzione logistica endomembranosa, non solo un problema di segnalazione HIF1A.
**Source:** Hussain et al. 2018, *Front Oncol*; PMID 30619736 / PMCID PMC6300487 / DOI 10.3389/fonc.2018.00591.
**Wikilinks:** [[paper_registry_current#PAPER 032]]
**Impact on Working Model:** major refinement of P5 metabolism branch; informs meta_metabolism update; no direct BLOCCO 1 change

---

## CLAIM 027
**Title:** WWOX may act as an ECM/membrane-to-nucleus signaling node through HYAL-2/SMAD4 complexes, with context-dependent relevance to injury response and cell death
**Status:** in observation
**Type:** INFERENZA
**Pathway:** ECM / membrane signaling / injury response
**Genotype/model relevance:** review-supported + supporto sperimentale in sistemi HA-responsivi; rilevanza CNS/sviluppo non ancora dimostrata direttamente
**Transferability:** T3 — indirect; not yet promoted to central pathway
**clinical relevance:** INDIRECT
**Summary:** HYAL-2/WWOX/SMAD4 signaling has been proposed and experimentally supported in HA-responsive systems. Nuclear accumulation of signaling complexes is linked to context-dependent cell death output. Not ready for promotion to central pathway. High-value research candidate for cross-domain exploration, including possible relevance to CNS injury biology.
**Clinical meaning:** Nessun impatto operativo immediato per il genotipo di riferimento. Asse da monitorare come candidato di ricerca.
**Source:** paper 214 (corpus 181–220)
**Wikilinks:** [[paper_registry_current#CORPUS P214]]
**Impact on Working Model:** add to research-facing layer only; not core baseline

---

## CLAIM 028
**Title:** WWOX biological output is strongly partner- and context-dependent; expression level alone is insufficient to infer uniform functional benefit
**Status:** flagged for review
**Type:** INFERENZA — principio interpretativo trasversale
**Pathway:** cross-pathway interpretive principle
**Genotype/model relevance:** inferenza da convergenza multi-paper (papers 207, 218, 206, 214); non modello singolo; principio architetturale generale
**Transferability:** T2 — indirect but important for disciplined inference
**clinical relevance:** INDIRECT — important for disciplined inference across all pathways
**Summary:** WWOX signaling output varies depending on partner composition, subcellular context and signaling state. Some systems suggest that WWOX availability does not translate into simple linear benefit unless relevant partners and network accessibility are preserved. WWOX should not be modeled as a uniformly monotonic regulator whose increase or decrease has identical meaning across tissues or disease states. Partner accessibility, phosphorylation state, compartmentalization and network context must be considered.
**Clinical meaning:** Principio di cautela interpretativa trasversale. Impedisce di leggere "più WWOX = meglio" in modo lineare e uniforme. Rilevante per interpretazione di terapia genica, modulazione farmacologica e lettura di studi in sistemi non-CNS.
**Source:** papers 207, 218, 206, 214 (corpus 181–220)
**Wikilinks:** [[paper_registry_current#CORPUS P207]], [[paper_registry_current#CORPUS P218]], [[paper_registry_current#CORPUS P206]], [[paper_registry_current#CORPUS P214]]
**Impact on Working Model:** cautionary interpretive principle; no direct BLOCCO 1 change; informs disciplined reading of all future WWOX biology

---

## Consolidation rules
A claim may be escalated only if:
- at least 3 convergent studies support it, or
- a single high-impact study justifies review, or
- a direct safety override applies, or
- slow accumulation across 8–12 weeks activates review

## Contradicting evidence protocol
If comparable studies conflict:
- status becomes `conflicting evidence`
- no BLOCCO 1 promotion
- no premature claim discard
- deep review may be required


## CLAIM 029
**Title:** WWOX contributes directly to DNA-damage-response competence and genome-stability maintenance, at least in part via ATM activation and damage-induced nuclear relocalization
**Status:** in observation
**Type:** DATO + INFERENZA prudente
**Pathway:** genome stability / ATM / DNA damage response
**Genotype/model relevance:** studio meccanicistico primario in contesti cellulari oncologici / DDR; non modello CNS pediatrico diretto; Clinical relevance indiretta ma strutturalmente importante come possible progenitor-vulnerability axis
**Transferability:** T2 conceptual / indirect for the reference genotype
**clinical relevance:** INDIRECT — structurally important, not operational
**Summary:** WWOX deficiency reduces ATM activation, compromises γ-H2AX induction/maintenance and impairs DNA repair. DNA damage promotes ITCH-dependent K63 ubiquitination of WWOX on Lys274, nuclear accumulation of WWOX, and interaction with ATM, enhancing checkpoint signaling. This supports a model in which WWOX contributes directly to DDR competence and genomic-stability maintenance rather than acting only as a distal tumor suppressor marker.
**Clinical meaning:** No direct therapeutic implication for the reference genotype. The main value is structural: WWOX-related disease may include vulnerability to genome / replicative stress, particularly relevant to proliferative developmental compartments. This remains unproven in human pediatric CNS and therefore stays in observation.
**Counter-directional observation (BATCH_20260909_001, PMID 41562193 — [[paper_registry_current#PAPER 010]]).** The **ATM-activation leg is untouched**: that paper measures no ATM, no γH2AX, no 53BP1 and no relocalization, so it cannot bear on the mechanism. What it **qualifies** is the *genome-stability-maintenance* leg at its phenotypic end: the only panel plotting Wwox wild type beside Wwox knockout — Supplementary Figure 1 — shows the **wild type carrying the highest total mutation burden in the whole Wwox dataset** (`Wwox3WT`, ≈2829, above every knockout and mutant), with WT and KO **interleaving across the entire rank order** and the three P47T kidneys sitting inside the range of their own matched wild types. 🔴 **Deliberately not stated as a reversal.** A mutation-burden null in MEFs and kidney does not overturn a DDR-competence mechanism: the burden endpoint is downstream, noisy, culture-history-dependent in MEF lines, measured on exomes rather than genomes, and passed through a filter that removes every variant seen in any wild-type mouse. `Status` unchanged (`in observation`).
**Source:** paper 138 / PMID 25331887 / PNAS 2014 (Abu-Odeh et al., promosso a PAPER 030 il 2026-06-28); supported conceptually by later ATM/ATR commentary and by γH2AX / 53BP1 signals in WWOX-deficient neurodevelopmental models
**Wikilinks:** [[paper_registry_current#PAPER 030]]
**Impact on Working Model:** adds candidate structural axis (ATM/DDR competence) without changing BLOCCO 1; justifies research-candidate propagation

---

---

## CLAIM 030
**Title:** In WWOX the severity tracks residual protein FUNCTION, not protein abundance
**Status:** in observation
**Type:** DATO (serie allelica su cellule di paziente) + INFERENZA (la regola)
**Pathway:** genotype / protein function / proteostasis
**Genotype/model relevance:** direttamente rilevante al genotipo di riferimento — riguarda the missense allele Q230P e il suo controllo naturale G372R
**Transferability:** T1
**clinical relevance:** VERY HIGH
**Summary:** Confrontando quattro varianti su cellule di paziente: **P47T** (WW1) ha **proteina a livelli normali** e **binding PPxY abolito** → fenotipo **lieve** (SCAR12, pazienti vivi a 17-26 anni). **P47R** — stesso residuo — dà fenotipo **severo**. **Q230P** (SDR) ha **proteina assente** → **severo**. **G372R** (SDR) ha proteina quasi non rilevabile all'IF → **lieve**, con organoidi forebrain quasi normali. **p.Arg54\*** (null) → letale a 16 mesi. ⇒ **L'abbondanza di proteina non predice la severità.** Steinberg 2021 lo osserva indipendentemente: la severità potrebbe correlare con i *"functional levels"* di WWOX, non con quelli totali. La funzione WW1/PPxY-binding **non** determina la gravità; il dominio **SDR** sì.
**Clinical meaning:** Riformula il bersaglio del rescue proteostatico ([[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]]): la domanda non è *quanta proteina Q230P si riesce a salvare*, ma **se la proteina salvata sia funzionale**. **G372R è il controllo negativo naturale** dell'esperimento: se rispondesse a un chaperone allo stesso modo di Q230P, il modello strutturale sarebbe falso e il rescue un artefatto aspecifico. Nessuna implicazione clinica diretta; non è parere medico.
**Source:** [[paper_registry_current#PAPER 042]] (Mallaret — WB e pull-down su P47T) · [[paper_registry_current#PAPER 041]] (Johannsen — Q230P) · [[paper_registry_current#PAPER 039]] (Steinberg — G372R, organoidi) · [[paper_registry_current#PAPER 043]] (Abdel-Salam 2014 — `p.Arg54*` omozigote, letale a 16 mesi). Analisi strutturale in-silico: `scripts/legend/residue_context.py` su AlphaFold AF-Q9NZC7-F1 — Q230 relSASA **0.000** (sepolto, α-elica, pLDDT 98.5, 22 contatti <5 Å, 8.2 Å dalla triade); G372 relSASA 0.163 e P47 0.286 (superficiali, β-strand). ΔΔG ThermoMPNN: P47T +2.81, P47R +2.53, G372R +1.58, Q230P +1.51 → **il ΔΔG non discrimina**.
**Evidence boundary (BATCH_20260909_001 — the codon-47 contrast; narrows the EVIDENCE LINE, not the conclusion).** In the Banne 2021 review's Table 1 — resolved from the table's **`rowspan` markup**, not from its linearised text — `c.140C>G p.Pro47Arg` appears **only** as the **second allele of a compound heterozygote**, in trans with the exon-1 frameshift `c.46_49del p.Asp16fs`: 2 patients, Portuguese, onset 5 m / 5 m, **alive at 4 y and 3 y**. The P47T SCAR12 patients are **homozygous**. 🔴 **The two genotypes are therefore not matched, and P47R's severity cannot be separated from the null-like allele in trans.** A same-residue argument requires comparable genotypes; this source does not supply them. Additionally, **Figure 3B cannot be used to separate the two alleles**: it merges them onto one lollipop labelled `P47R/T`, and mis-colours it. **The conclusion of `CLAIM 030` is not challenged and its status does not move** — what is asked is that the **P47R limb be restated at genotype level**, and that this review not be cited as independent support for an allele-level P47T-vs-P47R contrast.
**Corroboration (BATCH_20260909_001 — independent secondary source, R4 satisfied).** Corroborated independently by Abu-Remaileh et al. 2015, *J Biol Chem* 290(52), **PMID 26499798** = [[paper_registry_current#PAPER 089]], whose Figure 2B draws P47R in trans with a codon-16 exon-1 truncating allele and is **the only patient row in that figure not assigned a single phenotype class**. ⚠️ **The two records are NOT independent patients**: both trace to Mignot 2015 (PMID 25411445), which this corpus holds at **no depth at all**. ⚠️ The second allele is annotated three different ways across sources — Banne Table 1 `p.Asp16fs`, the 2015 review's text *"exon 1 frameshift"*, and its Figure 2B `A16*`. **Registered, not adjudicated: no claim in this registry should carry either annotation as established.** `REVIVAL_TRIGGER`: any reading of PMID 25411445, or of the deposited ClinVar/DECIPHER record for `c.140C>G`, that names the second allele's annotation.
**Wikilinks:** [[paper_registry_current#PAPER 039]] · [[paper_registry_current#PAPER 041]] · [[paper_registry_current#PAPER 042]] · [[paper_registry_current#PAPER 040]] · [[paper_registry_current#PAPER 089]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 032]]
**Impact on Working Model:** genotype interpretation refined; **⚠️ methodological caveat obbligatorio**: le misure di abbondanza confrontate non sono commensurabili (WB su fibroblasti per P47T e Q230P; IF su organoidi per G372R). La serie orienta, **non quantifica**. Nessun cambio BLOCCO 1.

---

## CLAIM 031
**Title:** WWOX-DEE is a developmental AND epileptic encephalopathy: seizure control does not rescue development
**Status:** in observation
**Type:** DATO (osservazione clinica) + INFERENZA (degli autori)
**Pathway:** clinical course / therapeutic strategy
**Genotype/model relevance:** umano — null biallelici; il principio è atteso indipendente dal genotipo
**Transferability:** T1
**clinical relevance:** HIGH
**Summary:** In due bambini WWOX-null con sindrome di West, il deficit cognitivo e psicomotorio **precede** l'esordio dell'encefalopatia epilettica e **non migliora** quando l'attività epilettica viene controllata. Testuale: *"The developmental outcome was unfavourable with profound impairment **despite improvement of epileptic activity**"*; *"the cognitive and psychomotor impairment **preceded the onset** of epileptic encephalopathy and **did not improve with achievement of better control** of epileptic activity"*. Nel caso 1 gli spasmi si sono **risolti** col vigabatrin, e a due anni il bambino era comunque profondamente ritardato. Convergenza: in Oliver 2023 l'unico paziente **non** farmaco-resistente è morto a 8 anni — la responsività ai farmaci non protegge la sopravvivenza.
**Clinical meaning:** ⚠️ **Corregge la logica di "guadagnare tempo".** Il controllo delle crisi **non va contato come protezione dello sviluppo cognitivo**. Resta pienamente indicato per qualità di vita, prevenzione dello stato epilettico (causa di morte documentata) e del SUDEP, sonno e gestibilità — ma non come leva disease-modifying. **Per contrasto, rafforza le leve causali** (terapia genica; rescue proteostatico dell'allele Q230P), le uniche che il modello DEE prevede possano modificare l'esito di sviluppo. Coerente con Obeid 2026, dove il rescue **neuronale precoce** recupera comportamento, mielina e sopravvivenza, mentre nessun antiepilettico lo fa. **Non è parere medico.**
**Source:** [[paper_registry_current#PAPER 045]] (Shaukat 2018) · convergenza con [[paper_registry_current#PAPER 018]] (Oliver 2023) e [[paper_registry_current#PAPER 011]] (Obeid 2026)
**Wikilinks:** [[paper_registry_current#PAPER 045]] · [[paper_registry_current#PAPER 018]] · [[paper_registry_current#PAPER 011]] · [[claim_registry_current#CLAIM 001]]
**Impact on Working Model:** ridimensiona la leva "protezione della finestra" come strategia di protezione dello sviluppo; rafforza le leve causali. Limiti: N=2, osservazionale, non controllato. Nessun cambio BLOCCO 1.

---

## CLAIM 032
**Title:** WWOX haploinsufficiency is not deleterious: the therapeutic threshold is well below full restoration
**Status:** in observation
**Type:** DATO (topo, ratto, e ogni famiglia umana pubblicata)
**Pathway:** P7 — gene therapy readiness / dose-threshold logic
**Genotype/model relevance:** trasversale — vale per tutte le leve di ripristino (GT, editing, chaperone)
**Transferability:** T1/T2
**clinical relevance:** VERY HIGH
**Summary:** La perdita di **un solo** allele di WWOX non produce fenotipo. Aldaz 2014: *"loss of one Wwox allele (i.e. **haploinsufficiency**) appears **not to be deleterious**"*; *"the lifespan of the Wwox heterozygotes was **indistinguishable from WT mice**"*. Tochigi 2019: i ratti **`+/lde`** hanno *"a single band of normal molecular weight, but its intensity was **almost half**"*, con immunoistochimica corticale intensa come i `+/+` e **assente** nei `lde/lde`. Ogni famiglia umana pubblicata (Shaukat, Elsaadany, Abdel-Salam, Mallaret, Johannsen) ha **genitori portatori eterozigoti sani**. Inoltre, il topo **ipomorfo** `Wwox^gt/gt` (proteina bassa **ma rilevabile**) è **vitale**, mentre il null muore a 3-4 settimane ⇒ **la soglia fra letale e vitale sta sotto il 50%**.
**Clinical meaning:** Ridefinisce la **soglia di successo di ogni leva del portafoglio**. (1) **Correggere o compensare un solo allele basta**, in linea di principio: the reference genotype diventerebbe l'equivalente funzionale di un portatore sano. (2) **Non serve efficienza elevata**: terapia genica, base/prime editing e chaperoni hanno rese modeste in vivo e non raggiungono ogni cellula — se l'aploinsufficienza è tollerata, **un mosaicismo terapeutico parziale può bastare**. (3) Il principio "il parziale conta" acquisisce un **fondamento quantitativo**, non retorico. ⚠️ **Limiti che vietano di estrapolare:** la soglia è nota per **sopravvivenza e morfologia**, **non per cognizione ed epilessia** — nessuno ha misurato quanta WWOX serva al neurosviluppo; l'aploinsufficienza è tollerata **dalla nascita**, mentre un rescue nel genotipo di riferimento arriverebbe **dopo** parte del danno di sviluppo (vedi [[claim_registry_current#CLAIM 031]]); nei topi eterozigoti è documentato un aumento di tumorigenicità **sotto carcinogeni**. **Non è parere medico.**
**Source:** [[paper_registry_current#PAPER 053]] (Aldaz 2014 — *"haploinsufficiency appears not to be deleterious"*; *"lifespan indistinguishable from WT mice"*) · [[paper_registry_current#PAPER 021]] (Tochigi 2019 — ratti `+/lde`: banda di peso normale a **metà** intensità, IHC corticale normale) · [[paper_registry_current#PAPER 043]] (Abdel-Salam 2014 — *"no tumors were observed in the patient or **heterozygous mutation carriers**"*) · [[paper_registry_current#PAPER 045]] e [[paper_registry_current#PAPER 049]] (genitori portatori eterozigoti sani) · [[paper_registry_current#PAPER 042]] (idem)
**Wikilinks:** [[paper_registry_current#PAPER 053]] · [[paper_registry_current#PAPER 021]] · [[paper_registry_current#PAPER 043]] · [[paper_registry_current#PAPER 045]] · [[paper_registry_current#PAPER 049]] · [[paper_registry_current#PAPER 042]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 031]] · [[therapeutic_strategies_current#TX-007 — AAV9-WWOX gene therapy (gene addition) — the north-star, now FIRST-IN-HUMAN ⭐|TX-007]]
**Impact on Working Model:** abbassa la soglia di efficacia richiesta a tutte le leve di ripristino; **da riflettere in TX-003 e TX-007**. Nessun cambio BLOCCO 1.
🔴 **BATCH_20260815_001 qualification:** [[paper_registry_current#PAPER 077]] and [[paper_registry_current#PAPER 078]] show that adult heterozygotes can be unremarkable in unchallenged assays yet strongly tumour-susceptible after NMBA or ENU. This is genotype×stress interaction, not proof that untreated heterozygotes phenocopy biallelic disease; tumour protein positivity does not establish an intact residual allele.

---

## CLAIM 033
**Title:** Biallelic null WWOX carries higher mortality than genotypes with at least one missense — but the classification is a noisy proxy for residual function
**Status:** in observation
**Type:** DATO (statistica di coorte) + IPOTESI (l'assunzione "missense = ipomorfo")
**Pathway:** genotype-phenotype / prognosis
**Genotype/model relevance:** umano — coorte WWOX-DEE (n=13 + 62 da letteratura). the reference genotype è formalmente `null/missense`
**Transferability:** T1 nominale, **T3 di fatto** (vedi riserva 3)
**clinical relevance:** MODERATE — **`actionability: none`**: descrive la gravità, che la clinica del genotipo di riferimento già mostra. Registrato per completezza, non per guidare una decisione
**Summary:** In WWOX-DEE i pazienti con genotipo biallelico **null/null** hanno sopravvivenza significativamente peggiore di quelli con **almeno una variante missense** (Kaplan-Meier, log-rank **p = .0085**; 5 anni: <50% vs >75%; 10 anni: ~25% vs >60%). Le varianti di sito di splicing accettore/donatore sono codificate come **null**. Mortalità complessiva ~35%, causa dominante **respiratoria**.
**Clinical meaning:** ⚠️ **Quattro riserve, tutte obbligatorie, senza le quali questo claim afferma più di quanto i dati sostengano.**
**(1) La classificazione è sintattica, non funzionale.** La classe è dedotta dal *tipo di lesione nel DNA*, mai dall'effetto misurato sulla proteina. Le nostre stesse fonti la falsificano come proxy: **Q230P** è missense e **azzera la proteina** ([[paper_registry_current#PAPER 041]]); **P47T** è missense, ha **proteina normale**, binding abolito, fenotipo **lieve** ([[paper_registry_current#PAPER 042]]); **P47R** — stesso residuo — dà fenotipo **severo**. Dentro "missense" convivono almeno tre meccanismi distinti. Vedi [[claim_registry_current#CLAIM 030]].
**(2) Nessun fenotipo intermedio è dimostrato.** Gli autori scrivono: *"no difference between individuals with one or two missense variants… no evidence to support an 'intermediate' phenotype"*. La classe del genotipo di riferimento (`null/missense`) **non è risolta separatamente**: è aggregata a `missense/missense`. Il confronto significativo è `null/null` **contro tutto il resto**.
**(3) Un genotipo con un allele VUS potrebbe non appartenere alla popolazione studiata.** Oliver arruola **solo varianti pathogenic/likely pathogenic**. Un allele di sito accettore canonico di questo tipo può essere **VUS in ClinVar**; il supporto è **in-silico** (SpliceAI DS_AL 0.96; MaxEntScan Δ −7.95) e **non esiste alcun dato di RNA su cellule variant-carrying**. Con un allele VUS, **un tale genotipo non sarebbe arruolabile in quella coorte**.
**(4) Limiti statistici.** N minuscoli per classe (`null/missense` n=15, aggregati da decenni di case report eterogenei); **nessun hazard ratio, nessun intervallo di confidenza numerico, nessuna mediana di sopravvivenza**; sopravvivenza confusa dalle **cure di supporto** (85% con gastrostomia); bias di pubblicazione verso i casi severi. La responsività ai farmaci **non protegge**: l'unico paziente non farmaco-resistente della coorte è morto a 8 anni.
**Nota di direzione (INFERENZA, taglia in entrambi i sensi):** poiché la misclassificazione è verosimilmente **non differenziale** rispetto all'esito, il suo effetto atteso è di **diluire** la separazione vera fra le classi. Il `p = .0085` potrebbe quindi **sottostimare** la differenza reale fra *"funzione residua presente"* e *"assente"*. **La variabile biologica vera è la funzione residua; `null/missense` ne è l'ombra.** Questo non favorisce alcuna prognosi: rende esplicito che la classificazione genetica **non sostituisce la misura**.
**(5) Riserva aggiunta (BATCH_20260909_001, PMID 33916893 — [[paper_registry_current#PAPER 040]]).** La premessa *"refractory to AEDs"* che inquadra la prognosi WOREE è **non uniforme nel supplemento stesso che la review cita per essa**: esiste un sottoinsieme di responder ai farmaci antiepilettici, censito nel discovery ledger come `DL-THER-106` ed esplicitamente **come censimento di risposta sintomatica, non come alcunché di disease-modifying**. La riserva (1) è inoltre corroborata dalle righe R264\*/W44\*/Q230P: **la statistica di Kaplan–Meier in sé resta intatta**, ma la classe sintattica continua a non predire l'esito individuale.
**Corollario operativo:** la RT-qPCR sulla giunzione esone 8→9 su cellule variant-carrying — finora giustificata come endpoint per una futura correzione — è anche il test che può fornire l'**evidenza funzionale (ACMG PS3)** capace di **riclassificare la VUS dello splice-site allele**. Un esperimento, due risultati. **Non è parere medico.**
**Source:** [[paper_registry_current#PAPER 018]] (Oliver 2023) · [[paper_registry_current#PAPER 041]] (Johannsen — Q230P azzera la proteina) · [[paper_registry_current#PAPER 040]] (Banne 2021, dataset di riferimento)
**Wikilinks:** [[paper_registry_current#PAPER 018]] · [[paper_registry_current#PAPER 040]] · [[paper_registry_current#PAPER 041]] · [[paper_registry_current#PAPER 042]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]]
**Impact on Working Model:** nessuna azione clinica. Il claim esiste per **impedire** che la classe genotipica venga letta come prognosi. Nessun cambio BLOCCO 1.

---

## CLAIM 034
**Title:** In a post-mitotic excitable neuron under metabolic stress, WWOX up-regulation is pro-oxidant — reducing WWOX reduces superoxide. WWOX↔ROS is not monotonic and its sign is context-dependent
**Status:** in observation
**Type:** DATO (sistema fotorecettoriale) + ESPANSIONE (qualunque trasferimento a WWOX-DEE)
**Pathway:** P5 — metabolism / redox · secondario P1 — Ca²⁺
**Genotype/model relevance:** topo + linea di coni 661W, **WWOX wild-type**, knockdown acuto sotto stress iperglicemico. **Nessuna variante WWOX, nessuna perdita germinale, nessun contesto CNS pediatrico.**
**Transferability:** T3
**clinical relevance:** INDIRECT — interpretativo, non azionabile
**Summary:** Nei fotorecettori di topo diabetico la proteina e l'mRNA di WWOX salgono (proteomica LFQ non guidata, log2 N −3.55 → D −1.75 → DT −2.94, p 0.002 / 0.01; `Wwox` mRNA ↑1.9×) e il knockdown con siRNA di `Wwox` **riduce** il superossido indotto da alto glucosio (−27% / −37%). In questo sistema più WWOX significa più stress ossidativo e meno WWOX significa meno. La direzione è opposta alla cornice deficienza→ROS di [[claim_registry_current#CLAIM 009]].
**Clinical meaning:** ⚠️ **Non va letto come «la perdita di WWOX protegge».** Tre ragioni per cui il trasferimento fallisce: (1) un *knockdown acuto in una cellula adulta stressata* non è una *perdita germinale durante il neurosviluppo*; (2) qui WWOX è una **proteina di risposta allo stress che viene indotta** — sopprimere una risposta indotta non equivale a non avere mai la proteina; (3) l'evidenza di loss-of-function è **n = 2** contro un controllo scrambled non inerte (Fig 9 di [[paper_registry_current#PAPER 054]]). Il claim si guadagna il posto come **claim di disciplina**, non terapeutico: è evidenza concreta che il segno della relazione WWOX↔ROS è fissato dal contesto, e istanzia direttamente [[claim_registry_current#CLAIM 028]]. **Non è parere medico.**
**Source:** [[paper_registry_current#PAPER 054]] (Saadane 2021)
**Wikilinks:** [[paper_registry_current#PAPER 054]] · [[claim_registry_current#CLAIM 028]] · [[claim_registry_current#CLAIM 009]] · [[dismissal_ledger_current#DIS-008 — «La calpaina è una via di degradazione/turnover per WWOX» → ⏸️ **NON STABILITA (rigettata come affermazione, non come possibilità)**]]
**Impact on Working Model:** nessun cambio BLOCCO 1. Obbliga CLAIM 009 a portare una nota controdirezionale esplicita.
🔴 **BATCH_20260815_001:** [[paper_registry_current#PAPER 071]] independently supports the context-dependence principle through Wwox×Idh/Sod genetics and a counter-directional ROS readout; it does not broaden the neuron-specific title or its T3 boundary.

---

## CLAIM 035
**Title:** WWOX is a direct, residue-mapped inhibitor of GSK3β through an Axin-like docking motif in the SDR domain (388–407 / L404); the inhibition is S9-independent and its neuronal output requires Tau
**Status:** in observation
**Type:** DATO (biochimica, cinque saggi ortogonali, una mutazione puntiforme) + INFERENZA (trasferimento al neurone umano e a WWOX-DEE)
**Pathway:** P1 neurosviluppo / GSK3β–Tau–microtubuli; funzione del dominio SDR
**Genotype/model relevance:** SH-SY5Y + ricombinanti + co-IP endogena da cervello di topo. Solo WWOX wild-type e mutanti ingegnerizzati — **nessun allele WWOX-DEE è stato testato**. Rilevante per il genotipo di riferimento perché identifica una *funzione SDR misurabile* e una *regione da non toccare*.
**Transferability:** T2 meccanicistico
**clinical relevance:** INDIRECT — alto valore come saggio e come vincolo di disegno; non ne segue alcuna terapia
**Summary:** WWOX lega GSK3β attraverso il dominio ADH/SDR, su un segmento di 20 residui (388–407) omologo al motivo di docking Axin/FRAT/GSKIP, con **L404 strettamente necessario**. Il legame blocca la fosforilazione di Tau su S396/S404 (ma non sul sito MKK4 S422), ripristina l'assemblaggio dei microtubuli Tau-dipendente e promuove la crescita neuritica indotta da RA. L'interazione è rilevabile fra **proteine endogene in cervello di topo**. Criticamente, tutto questo avviene con **fosfo-GSK3β-S9 invariata**: l'interruttore inibitorio canonico non è coinvolto. L'epistasi (knockdown di Tau; non additività di WWOX + siRNA-GSK3β) colloca WWOX, GSK3β e Tau su un'unica via lineare con Tau come effettore.
**Clinical meaning:** Due conseguenze operative, nessuna terapeutica. **(1) Un saggio funzionale per gli alleli missense del dominio SDR** — pull-down GSK3β + inibizione della chinasi su Tau in vitro — più economico e meglio definito dell'attività ossidoreduttasica, il cui substrato fisiologico è ignoto (vedi [[claim_registry_current#CLAIM 030]]). **(2) Un avvertimento di misura:** la de-repressione di GSK3β causata dalla perdita di WWOX sarebbe **invisibile a un western anti-fosfo-S9**, che è il saggio standard — qualunque studio WWOX-DEE che usi pS9 come readout di attività GSK3β produrrà un **falso negativo**. **Non è parere medico.**
**Source:** [[paper_registry_current#PAPER 056]] (Wang 2012, PMID 22193544)
**Wikilinks:** [[paper_registry_current#PAPER 056]] · [[claim_registry_current#CLAIM 016]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 028]]
**Impact on Working Model:** nessun cambio BLOCCO 1. Irrigidisce il vincolo di disegno su TX-003 (la regione 388–407/L404 è ora una zona di esclusione supportata da `DATO`, non da citazione); fornisce un readout funzionale a CLAIM 030; aggiunge un caveat di misura sui biomarcatori.

---

## CLAIM 036
**Title:** A systemic constitutive Wwox-null mouse at P18 is metabolically decompensated, so any brain phenotype measured in that window carries a quantified systemic confounder
**Status:** in observation
**Type:** DATO (le misure) + INFERENZA (la portata come confondente)
**Pathway:** P5 — metabolismo / rene; confondente trasversale a P1, P2, P6
**Genotype/model relevance:** topo, null sistemico costitutivo `Wwox^ΔCre/ΔCre` generato con **EIIA-Cre**. Nessun allele WWOX-DEE. Rilevante come **vincolo di disegno**, non come meccanismo di malattia.
**Transferability:** T3 — non trasferisce un fenotipo, trasferisce un avvertimento metodologico
**clinical relevance:** INDIRECT
**Summary:** A postnatal day 18 il null sistemico mostra glucosio 143.5 vs 250.6 mg/dL (`p=0.000131`), bicarbonato totale 14.50±3.5 vs 21.67 mEq/L (`p=0.006227`), BUN 37.25 vs 17.67 mg/dL (`p=0.01086`), calcio 10.18 vs 11.13 mg/dL (`p=0.000385`), WBC 4.2 vs 9.45 ×10³/µL (`n=2/gruppo`), atrofia splenica (0.21% vs 0.53% del peso corporeo, `p=0.0015`) con ipocellularità della polpa rossa e corticale timica assottigliata. Chimica ematica `n=3/3/4`.
**Clinical meaning:** Nessuna. È un vincolo di disegno: qualunque fenotipo ippocampale o cerebrale misurato in un null **sistemico** nella finestra P14–P18 è misurato in un animale simultaneamente ipoglicemico, acidotico, uremico e anemico. Questo **non confuta** tali fenotipi — rende **impossibile per costruzione** separare la perdita neuronale cell-autonoma di Wwox dal danno metabolico secondario. È esattamente il divario che l'allele condizionale `Wwox^flox`, generato nello stesso paper, è stato costruito per chiudere e che nessuno ha usato in questa direzione. **Non è parere medico.**
**Evidence boundary:** 🔴 Il peso cerebrale è **brain sparing in cachessia, non crescita**: assoluto 0.390 → 0.356 g (−8.7%), relativo 5.0% → **8.5%** del peso corporeo, e la significatività (`p=0.0003`) è sul **relativo**, guidata dal denominatore crollato. Importarlo senza il rapporto inverte la biologia. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — **l'ablazione di Wwox nel cervello non è mai mostrata**: il western copre rene, polmone e milza (identità dei tessuti visibile solo nel raster di Fig. 2C) e l'IHC solo il rene. Una Cre zigotica rende attesa la delezione globale, ma l'attesa non è misura. **`REVIVAL_TRIGGER`:** un western o un'IHC su lisato cerebrale da `EIIA-Cre; Wwox^ΔCre/ΔCre`, da qualunque fonte. 🔴 Driver Cre **diverso** da quello di [[claim_registry_current#CLAIM 005]]: EIIA-Cre qui, BK5-Cre in PMID 30290271 — allele floxed condiviso, knockout diverso.
**Source:** [[paper_registry_current#PAPER 057]] (Ludes-Meyers 2009, PMID 19936220; full text read 2026-08-06, receipt `FTR-20260806-19936220-01`)
**Wikilinks:** [[paper_registry_current#PAPER 057]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 038]]
**Impact on Working Model:** nessun cambio BLOCCO 1. Aggiunge un vincolo di disegno trasversale: i null sistemici nella finestra P14–P18 non separano cell-autonomo da sistemico.
🔴 **BATCH_20260815_001 qualification:** [[paper_registry_current#PAPER 075]], [[paper_registry_current#PAPER 076]] and [[paper_registry_current#PAPER 078]] reproduce early systemic collapse with bone/endocrine abnormalities but do not separate local autonomy from pituitary input, developmental delay or terminal metabolic illness. Juvenile osteosarcoma remains conflicting: 4/13 morphology-positive in PAPER 078, rare malignant-appearing cells without denominator in PAPER 075, and 0/9 by multimodal examination in PAPER 057.

🔴 **`BATCH_20260909_001` qualification — the pro-osteosarcoma extreme is 86%, not 100%.** `PMID 20530675` (Kurek 2010, `FTR-20260909-20530675-01`, `CORPUS P268`) is the source of the strongest pro-osteosarcoma number in this literature — *"100% of Wwox-deficient mice had developed OS by 18 days-of-age"* — and **the paper's own Figure S1 legend reports 19 of 22 knockout mice with tumours (86%)**, with 13/19 bilateral against Supplemental Table 1's 15+7=22. The percentages nearly coincide (68.2% of 19 versus 68% of 22), **which is why the discrepancy survives a reader checking percentages rather than counts.** Supplemental Table 1's footnote — *"only one femur was analyzed by microCT in 3 mice"* — supplies the arithmetic: 22 − 19 = 3, split 2 bilateral + 1 unilateral, so **two animals were scored bilateral from a single imaged femur**. The screening criterion (*irregular protrusions on the endosteal or periosteal sides of the cortex*) is applied to a knockout cortex that Figure S1 itself shows is thinner and more porous than wild type, and **no blinding is stated anywhere**. This **narrows** the conflict rather than widening it.

🔴 **`BATCH_20260909_001` qualification — the conflict has a named resolution in the literature, and it rests on nothing.** `PMID 21731849` (Del Mare 2011, `FTR-20260909-21731849-01`, `CORPUS P261`), the group's own **review**, disposes of both independent negatives in one sentence: *"Analyses by others of other Wwox null rodent models failed to detect osteosarcomas [36, 47], most likely due to the lack of a sensitive detection method such as μCT to find these tiny tumors."* Ref 36 is [[paper_registry_current#PAPER 057]] (PMID 19936220, 0/9) and ref 47 is the **lde/lde rat** ([[paper_registry_current#PAPER 058]] / [[paper_registry_current#PAPER 059]]) — **both read in full in this repository**. The attribution is offered as the likely cause with **no test, no re-examination of those animals and no method comparison**. `PREMISE: DEFAULT_FROM_TEXTBOOK` — *a negative result is explained by method insensitivity*. **`REVIVAL_TRIGGER`:** μCT re-imaging of archived limbs from either negative cohort, or a blinded side-by-side of histology versus μCT on the same animals. The same review states the positive at its maximum — *"osteosarcomas are detected in 100% of the post-natal mice prior to their death"* — where its own primary carries 86% in its Figure S1 legend. **So across the two papers the pro-osteosarcoma extreme is 86%, asserted as 100%, and the two contrary results are explained away untested.**

**`BATCH_20260909_001` — the design constraint is corroborated by the authors themselves.** The same review: *"specific ablation of Wwox in mouse bone **without the compound effects of total Wwox deletion** will likely be instrumental to specifically address the role of WWOX in bone homeostasis and the pathogenesis of osteosarcoma."* This claim's evidence boundary already holds that the conditional allele *"was built to close [the gap] and nobody has used it in this direction"*; **this is the earliest statement of that intent, from the lab that built the allele**, announced there as *"[unpublished data]"* and later read by this repository as `PMID 23254685`.

---

## CLAIM 037
**Title:** The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype, electrographically documented, and it is explicitly absent in Wwox-null mice
**Status:** in observation
**Type:** DATO
**Pathway:** P2 — eccitabilità / epilettogenesi
**Genotype/model relevance:** ratto, ceppo LDE, delezione spontanea di 13 bp nell'esone 9 di `Wwox` — **strutturalmente frameshift C-terminale (371–424aa), funzionalmente null a livello proteico** (mRNA normale, né 47 né 42 kDa rilevabili in testicolo e ippocampo, con epitopo dell'anticorpo **fuori** dalla regione alterata). Non è un allele WWOX-DEE umano.
**Transferability:** T2 per la vulnerabilità conservata da perdita biallelica; **T3** per qualunque trasferimento del fenotipo epilettico a un modello murino o a un genotipo umano
**clinical relevance:** MODERATE
**Summary:** Crisi audiogene in **19/20 (95%)** su tre stimolazioni (coorte **solo femminile**, denominatore al netto di 3 morti); crisi spontanee **30/50 (60%)** nella progenie backcross e **33.8% (22/65) ♂ / 33.9% (19/56) ♀** nel ceppo inbred; **0/14** controlli normali, né indotte né spontanee. Latenza che si accorcia 56±24 → 36±4 → 25±3 s su tre giorni (progressione kindling-like). **EEG:** spike interictali ~10 Hz sporadici in **tutti** i mutanti non stimolati, sincronizzati bilateralmente, ampiezza occipitale > frontale, assenti nei normali (`n=5` mutanti, `3` normali); complessi punta-onda lenta 5–6 Hz prima delle convulsioni cloniche. **Substrato anatomico:** vacuoli extracellulari in CA1 e amigdala, 9/9 affetti contro 0/10 normali, con giro dentato e CA3 risparmiati.
**Clinical meaning:** Nessuna implicazione farmacologica. Il modello è un candidato per l'**epilessia pediatrica** per tempistica di esordio (16–63 giorni postnatali) e possiede il substrato strutturale che la letteratura murina non ha. **Non è parere medico.**
**Evidence boundary:** 🔴 **I topi Wwox-null non hanno epilessia riportata** — affermato tre volte in PMID 19500159 e formalizzato in Table 2, dove la riga `Epilepsy` è compilata solo per `lde/lde`. Gli autori lasciano aperta la spiegazione (i topi potrebbero morire prima di convulsionare) e la sopravvivenza la rende testabile: 2–3 settimane nel topo contro **3–12 settimane** nel ratto, con esordio più precoce delle crisi al giorno 16. ⚠️ Il 95% audiogeno è **solo femminile**, dichiarato unicamente nella didascalia della Fig. 6. ⚠️ Il 34% spontaneo è **un pavimento, non un tasso**: gli autori dichiarano che crisi non rilevate e morte precoce lo spingono in basso. ⚠️ La vacuolizzazione **non ha corrispettivo** in epilessia umana né in altri modelli animali, il che limita il trasferimento. ⚠️ Due soli paper, **un solo laboratorio, mai replicati indipendentemente** — mitigato dal fatto che il fenotipo fu osservato **prima** che il gene fosse identificato. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — la scomparsa della proteina mutante è attribuita al sistema ubiquitina-proteasoma **senza alcun saggio di turnover, inibitore o determinazione di via**; è lo stesso default falsificato il 2026-07-12 per un altro allele WWOX, il cui turnover passava per una via lisosomiale HSC70-associata insensibile a MG-132. **`REVIVAL_TRIGGER`:** un chase con cicloesimide più inibitori proteasomali versus lisosomiali/CMA sulla proteina lde.
**Source:** [[paper_registry_current#PAPER 058]] (Suzuki 2009, PMID 19500159; receipt `FTR-20260806-19500159-01`) · [[paper_registry_current#PAPER 059]] (Suzuki 2007, PMID 17803050; receipt `FTR-20260806-17803050-01`)
**Wikilinks:** [[paper_registry_current#PAPER 058]] · [[paper_registry_current#PAPER 059]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 038]] · [[claim_registry_current#CLAIM 039]]
**Impact on Working Model:** nessun cambio BLOCCO 1. Sposta l'epilettogenesi da premessa importata su un modello murino a `DATO` misurato su un modello **di ratto**, con la discordanza di specie registrata anziché appianata.

---

## CLAIM 038
**Title:** Elevated BUN and creatinine recur across Wwox rodent models with two competing explanations — renal insufficiency or seizure-driven hypercatabolism — and neither has ever been tested
**Status:** in observation
**Type:** DATO (le misure) + IPOTESI (entrambe le spiegazioni)
**Pathway:** P5 — metabolismo / rene
**Genotype/model relevance:** ratto `lde/lde` (misure primarie) e topo `Wwox`-null sistemico (misura convergente). Nessun dato umano.
**Transferability:** T3 — questione aperta, non fenotipo trasferibile
**clinical relevance:** INDIRECT
**Summary:** Nel ratto a 28 giorni: BUN 12.6 → **40.3** mg/ml (♀, `P<0.05`) e 10.1 → **35.6** (♂, `P<0.01`); creatinina 0.48 → **0.64** (♀) e 0.45 → **0.58** (♂), entrambe `P<0.01`; fosfato inorganico significativo solo nelle femmine (`n=4` normali, `5` mutanti per sesso). **Glucosio, calcio, Na⁺, K⁺, Cl⁻ e trigliceridi: tutti non significativi.** Il ratto è dunque **uremico senza essere ipoglicemico** — profilo opposto a quello del topo null, che è entrambi (vedi [[claim_registry_current#CLAIM 036]]).
**Clinical meaning:** Nessuna. Due spiegazioni concorrenti, entrambe `IPOTESI`, entrambe mai testate: **(1) insufficienza renale** — ma i reni sono **istologicamente normali**, non c'è proteinuria né anemia, e gli autori stessi concludono che «if renal excretive function is reduced … the degree of dysfunction may not be severe»; **(2) produzione aumentata da ipercatabolismo e disgregazione muscolare** dovuta a crisi ripetute, con precedente nominato nel ceppo SER (BUN elevato + ritardo di crescita + crisi motorie). 🔴 La seconda **compete direttamente con l'ipotesi di acidosi tubulare renale** che PMID 19936220 avanza per il topo sullo stesso marcatore, e che quel paper non ha mai considerato. **Non è parere medico.**
**Evidence boundary:** Il BUN elevato è ora documentato di prima mano in **tre** luoghi — topo null, ratto `lde/lde`, e la citazione incrociata fra i due — con **tre spiegazioni implicite diverse e zero follow-up**. Densità di campo misurata 2026-08-06: `WWOX AND ("metabolic acidosis" OR "renal tubular acidosis")` → **1** record; `WWOX AND ("blood urea nitrogen" OR creatinine)` → **1**; `WWOX AND (hypercatabolism OR "muscle disruption")` → **0**. ⚠️ CPK, ALP, GPT e GOT nella Table 2 del ratto portano note di **numerosità campionaria, non di significatività**: il CPK femminile è ~8.5× più alto **senza alcun marcatore** — non importabile in nessuna direzione. **Esperimento discriminante**, nominato dagli autori insieme alla ragione per cui non l'hanno fatto: test di clearance renale, impraticabile perché nanismo e letalità rendono difficile raccogliere urina. Nel topo servirebbero in parallelo creatina-chinasi e massa muscolare per separare le due vie.
**Source:** [[paper_registry_current#PAPER 059]] (Suzuki 2007, PMID 17803050) · [[paper_registry_current#PAPER 057]] (Ludes-Meyers 2009, PMID 19936220)
**Wikilinks:** [[paper_registry_current#PAPER 059]] · [[paper_registry_current#PAPER 057]] · [[claim_registry_current#CLAIM 036]] · [[claim_registry_current#CLAIM 037]]
**Impact on Working Model:** nessun cambio BLOCCO 1. Apre una domanda meccanicistica mai posta e impone che qualunque testo canonico che tocchi Wwox e funzione renale porti **entrambe** le ipotesi.

---

## CLAIM 039
**Title:** Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model — 95% versus 0% — and it is not cerebellar
**Status:** in observation
**Type:** DATO
**Pathway:** P1 — neurosviluppo / funzione motoria
**Genotype/model relevance:** ratto `lde/lde`, valutato a 21 giorni in 19 femmine e 20 maschi mutanti contro 14 femmine e 12 maschi normali
**Transferability:** T3 — fenotipo di ratto, allele non umano
**clinical relevance:** INDIRECT
**Summary:** **95%** dei mutanti mostra andatura atassica contro **0%** dei normali. È più penetrante delle crisi spontanee (~34%) e più penetrante di qualunque altro fenotipo neurologico del modello. Gli autori esaminano il cervelletto e **non trovano alterazioni patologiche marcate**, in contrasto esplicito con il topo *ataxia and male sterility* (AMS).
**Clinical meaning:** Nessuna. È registrata perché è il fenotipo neurologico **più penetrante dell'intero modello `lde`** e la letteratura a valle non lo porta affatto: la catena di citazioni che ha trasmesso «epilessia» attraverso due specie ha lasciato cadere per strada un fenotipo quasi completamente penetrante. **Non è parere medico.**
**Evidence boundary:** L'atassia **non ha spiegazione strutturale** in questo paper: il cervelletto è istologicamente indenne e nessun'altra regione, oltre a ippocampo e amigdala, mostra alterazioni al microscopio ottico. Non sono stati eseguiti test motori quantitativi (rotarod, footprint, analisi cinematica): la valutazione è osservazionale e non in cieco. Nessun dato su progressione temporale.
**Source:** [[paper_registry_current#PAPER 059]] (Suzuki 2007, PMID 17803050; receipt `FTR-20260806-17803050-01`)
**Wikilinks:** [[paper_registry_current#PAPER 059]] · [[claim_registry_current#CLAIM 037]]
**Impact on Working Model:** nessun cambio BLOCCO 1. Recupera un fenotipo perso in trasmissione e apre una domanda anatomica non risolta.
