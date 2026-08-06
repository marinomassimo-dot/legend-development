# Paper Registry Current

> **Public edition — de-identified.** Disease-level registry from public literature. All individual-linking data removed (names, geography, report/sample IDs, dates, parent-of-origin, cell-line ownership). Specific variants appear only as decoupled disease-model worked examples drawn from public literature, never as one persistent individual's inherited alleles. Some entries remain in their original language. Not medical advice.
## WWOX Paper Registry
**Version:** v1.8.2
**Date baseline:** 2026-03-28  
**Last update:** 2026-07-25 — `BATCH_20260725_001` (public audit, **traceability repair, no scientific change**): the historical CLAIM 028 source typo 213→207 was resolved against the tracking log and CORPUS P207; the superseded 213 pointer remains visibly withdrawn in the batch summary. Prev: `BATCH_20260725_DEPTH` normalized PAPER 005 evidence-depth metadata without scientific change. Prev: 2026-07-10 — URG_2026-07-09_001 category 5 invalidated the retracted/dependency-contaminated source line without affecting a baseline claim.

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

---

## PAPER 001
**Short title:** Steinberg 2024 organoids
**Full title:** WWOX deficiency impairs neurogenesis and neuronal function in human organoids
**Authors:** Steinberg et al.
**Year:** 2024
**Source type:** preprint / organoid study
**Journal/source:** bioRxiv
**Identifier:** preprint
**Status:** integrated
**Primary pathway:** P1 — Ca²⁺ / network dysregulation
**Secondary pathway:** P3 / P7
**Model/species:** human organoids
**Genotype/model:** WWOX-KO + WOREE-derived WWOX-deficient models
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 002
**Role:** core baseline paper
**Note:** key paper for network dysregulation, radial glia, MYC, AAV rescue

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
**Claim links:** 003
**Role:** myelination anchor paper
**Note:** justifies MRI + DTI logic. Identifier normalizzato + abstract/key-findings verificati via PubMed 2026-07-05 (CC-2026-07-05-002). Full-text PDF OA-ma-bot-blocked (Oxford advance-access) → handoff `files/fulltext/PMID33914858_Repudi2021.handoff.md` per recupero manuale; arricchimento quantitativo del claim rimandato al PDF. Reperto cross-pathway (abstract): organoidi cerebrali umani WWOX-KO mostrano iperattivazione + ipomielinizzazione → cross-link [[claim_registry_current#CLAIM 002]]. ⚠️ Duplicato corpus **CORPUS-STUB-087** (stesso DOI) → mergiare in un prossimo BATCH_COMMIT.
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
**Evidence depth:** full text reviewed (verified 2026-07-05, retrieved via Europe PMC)
**Primary pathway:** P7 — gene therapy readiness
**Secondary pathway:** P1 / P4
**Model/species:** mouse
**Genotype/model:** Wwox-null
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 004
**Role:** causal strategy anchor
**Note:** preclinical, but central for trial-readiness logic; now complemented by Obeid 2026. Full text verified 2026-07-05 (retrieved via Europe PMC/PMC MCP; According to PubMed, [DOI](https://doi.org/10.15252/emmm.202114599)) — CC-2026-07-05-001; CLAIM 004 finora derivato da review, ora ancorato a fonte primaria. Dettagli verificati: singola ICV neonatale (P0) AAV9-hSynI-WWOX (murino o umano, equivalenti) recupera sopravvivenza, crescita, ipoglicemia, crisi, atassia, mielinizzazione (OPC→oligodendrociti maturi, g-ratio, corpo calloso+nervo ottico), comportamento e neuroinfiammazione (GFAP/Iba1); restauro neuronale-only → mielinizzazione non-cell-autonoma; gliosi downstream della disfunzione neuronale; ipoglicemia reversibile da restauro CNS-only; durata ≥9 mesi, nessuna leakage periferica. ⚠️ Modello Wwox-null sistemico + P0 → design-principle trasferibili, non dose/timing (genotype caution "alta", the reference genotype compound het N/M). ⚠️ Duplicato corpus **CORPUS-STUB-042/048** (stesso DOI) → mergiare in un prossimo BATCH_COMMIT.

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
**Full title:** P47T model shows progressive neuroinflammation and altered PPxY binding
**Authors:** Hussain et al.
**Year:** 2023
**Source type:** variant-specific mechanistic study
**Journal/source:** pending normalization
**Identifier:** pending normalization
**Status:** integrated
**Primary pathway:** P6 — neuroinflammation
**Secondary pathway:** P3 — interaction logic
**Model/species:** mouse / functional variant study
**Genotype/model:** P47T
**Transferability:** T3 with genotype caution
**clinical relevance:** LOW
**Claim links:** 006, 007
**Role:** genotype caution anchor
**Note:** key for "P47T ≠ Q230P". In-silico read-across (IPOTESI, `INBOX-006` — quarantine record, private overlay, CC-2026-07-04-004): pur essendo clinicamente distinto da Q230P ("P47T ≠ Q230P" resta valido sul piano fenotipico), P47T appartiene alla **stessa classe di stabilità** — variante destabilizzante (ΔΔG in-silico +2.8), lontana dal sito attivo (~48 Å), LoF parziale, topo che sopravvive >1 anno. ⚠️ **Lettura poi RITIRATA (repair 2026-07-14):** P47T **non** è equivalente sul piano meccanicistico — ha **proteina normale** e un difetto di binding **WW1/PPxY**, cioè un'altra lesione in un altro dominio. Resta un **comparator model**, **non** un banco read-across: nessuna prova su un missenso SDR sepolto può passare di lì. Vedi `MECHANISM_TRANSFER_FIREWALL`.

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
**Evidence depth:** full text reviewed (open access PMC)
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
**Journal/source:** Molecular Therapy - Methods & Clinical Development (OMTA) 2026;34 (Cell Press)
**Identifier:** PMID 42422765 / PMCID PMC13343157 / DOI 10.1016/j.omta.2026.201791 — *Mol Ther Adv* 2026;34(3):201791. Identifier normalizzato in BATCH_20260710_A (era "da confermare"); main text full letto integralmente. Versione published del preprint bioRxiv omonimo.
**Status:** integrated
**Evidence depth:** full text reviewed
**Primary pathway:** P7 — gene therapy readiness
**Secondary pathway:** P4 / P6 indiretto
**Model/species:** murine — Wwox-null (severo)
**Genotype/model:** Wwox-null full KO
**Transferability:** T2
**clinical relevance:** HIGH
**Claim links:** 011
**Role:** P7 design-principle paper
**Note:** AAV9-hSynI-hWWOX ICV neonatale; rescue dose-dependent durable su survival, ECoG/SWD, myelination, gliosis; neuron-specific targeting; full KO ≠ the reference genotype ma design principles sono trasferibili alla logica di trial-readiness. — Versione published (peer-reviewed, OMTA vol 34) del preprint bioRxiv; riferimento preprint conservato per tracciabilità. Design-principle quantitativi dai supplementari S1–S8 (BATCH_20260703 discovery): promotore SynI neuronale ottimale vs MBP/CMV; WPRE aumenta WWOX 3–16.7×/regione (trade-off dose↔sicurezza; la review PAPER 029 lo sintetizza come "WPRE removed to avoid overexpression"); espressione durevole fino a P300; finestra terapeutica P1–P5; neuron-specific (fegato negativo). Gap traslazionale per il genotipo di riferimento: nessun dato post-onset/età avanzata. Main-text OMTA full da recuperare (NS-019).

---

## PAPER 012
**Short title:** Sapuppo 2026 WOREE syndrome plus
**Full title:** WOREE syndrome: Clinical Case Study and Literature Review
**Authors:** Sapuppo et al.
**Year:** 2026
**Source type:** human case report (peer-reviewed)
**Journal/source:** Current Issues in Molecular Biology 2026;48(5):449 (MDPI)
**Identifier:** PMID 42193054 · PMCID PMC13205014 · DOI 10.3390/cimb48050449
**Status:** integrated
**Evidence depth:** full text reviewed
**Primary pathway:** clinical spectrum / genotype-phenotype
**Secondary pathway:** P5 hypothesis-adjacent / weak P7 contextual
**Model/species:** human
**Genotype/model:** exon 6–7 deletion + exon 8 frameshift case
**Transferability:** T1 phenotypic / low therapeutic
**clinical relevance:** MODERATE
**Claim links:** 012
**Role:** phenotype-severity refinement paper
**Note:** MRI precoce normale non esclude rete severamente disorganizzata; nomenclatura "WOREE syndrome plus" non operativamente validata. Versione published del preprint Preprints.org [titolo preprint precedente: "WWOX Gene Disease as Infantile Catastrophic Epileptic Encephalopathy (WOREE Syndrome Plus): A Comprehensive Case Study with Brief Literature Update"] — stesso caso: CNV 38 kb esoni 6–7 + c.1043del p.Phe348Serfs*57 esone 8, ClinVar 421407. INCOERENZA PRISMA interna nella literature review (200→150→30 full-text; testo dichiara '70 esclusi su 30 full-text' = contraddizione aritmetica; nessuna figura PRISMA): conteggio review a bassa affidabilità, case report non invalidato. Test parentale non eseguito → cis/trans non determinato. Nessuno studio funzionale. Varianti del genotipo di riferimento (Q230P, c.1057-2A>G) NON presenti.

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
**Genotype/model:** two siblings with homozygous WWOX p.L239R
**Transferability:** T1 contextual
**clinical relevance:** LOW-MODERATE
**Claim links:** none
**Role:** supportive cohort context paper
**Note:** useful as human spectrum support only; not a strategy-shaping paper

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
**Evidence depth:** full text reviewed (PMC open access)
**Primary pathway:** P2 — safety / AED management
**Model/species:** human
**Genotype/model:** omozigote splice site c.172+1G>C (null/null per effetto funzionale; proteina troncata da minigene)
**Transferability:** T1 (umano) — genotipo null/null ≠ the reference genotype compound het missense + splice
**clinical relevance:** MODERATE-HIGH — safety-relevant (conflicting evidence vigabatrin)
**Claim links:** 001 (conflicting evidence)
**Role:** tensione evidence su vigabatrin; non pro-vigabatrin
**Note:** riduzione crisi con VGB 200 mg/kg/die in 1 caso null/null; senza MRI controllo per VABAM; follow-up brevissimo (13 mesi); non invalida Choi 2026; genotipo null/null ≠ the reference genotype

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
**Note:** KD associata a miglioramento crisi in 3/5 (P1, P2, P4); vigabatrin: resistente in P3, combinato con KD in P4; lattato lievemente elevato in P4 (2.4-3.3 mmol/L); Q230P/SDR: trascritto normale ma proteina assente/instabile → meccanismo post-traduzionale → compatibile con funzione residua parziale nel genotipo di riferimento; pancreatite ricorrente e sordità neurosensoriale come feature espansive; valutazione visiva indicata (4/5 con deficit visivo)

---

## PAPER 018
**Short title:** Oliver 2023 WWOX-DEE epilettologia mortalità
**Full title:** WWOX developmental and epileptic encephalopathy: Understanding the epileptology and the mortality risk
**Authors:** Oliver KL, Trivisano M, Mandelstam SA, et al.
**Year:** 2023
**Source type:** multicenter cohort study
**Journal/source:** *Epilepsia*
**Identifier:** PMID 36779245 / PMC PMC10952634 / DOI 10.1111/epi.17542
**Status:** filtered_in
**Evidence depth:** abstract + frammenti Scholar Gateway
**Primary pathway:** clinical spectrum / natural history / survival analysis
**Model/species:** human — 13 pazienti, 12 famiglie, 5 centri
**Genotype/model:** biallelic WWOX variants — N/N / N/M / M/M
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** pending
**Role:** epilettologia WWOX-DEE; sopravvivenza Kaplan-Meier; missense vs non-missense survival
**Next action:** full text retrieval PMC10952634 — alta priorità
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
**Primary pathway:** P3 — prenatal structure / GSK3β
**Secondary pathway:** P4 / P1
**Model/species:** mouse
**Genotype/model:** Wwox-null full KO
**Transferability:** T2 mechanistic
**clinical relevance:** HIGH
**Claim links:** 015, 016
**Role:** structural / GSK3β anchor paper
**Note:** severe model; supports prenatal malformation axis and GSK3β as research node; full text still prioritized

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
**Model/species:** mixed mechanistic / non-CNS direct
**Genotype/model:** WWOX downregulation framework
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Role:** metabolic axis anchor
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
**Primary pathway:** P5 — metabolism / HIF1A
**Secondary pathway:** none
**Model/species:** cell / animal metabolic models
**Genotype/model:** WWOX loss / downregulation
**Transferability:** T2 conceptual
**clinical relevance:** MODERATE
**Claim links:** 009
**Role:** foundational HIF1A metabolic anchor
**Note:** strengthens HIF1A/Warburg framework

---

## PAPER 025
**Short title:** Piard 2019 EJPN exon 6 / Q230P
**Full title:** Novel WWOX deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay and dysmorphic features
**Authors:** Piard et al.
**Year:** 2019
**Source type:** human case series
**Journal/source:** *European Journal of Paediatric Neurology*
**Identifier:** PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003
**Status:** processed
**Primary pathway:** genotype-phenotype / exon 6 logic
**Secondary pathway:** clinical spectrum
**Model/species:** human
**Genotype/model:** severe compound heterozygous and splice-related human variants
**Transferability:** T1
**clinical relevance:** HIGH
**Claim links:** 018, 019
**Role:** exon 6 skipping + Q230P compound-context anchor
**Note:** important for allele-specific logic and exon-based pathogenicity


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
**Authors:** Schrock et al.
**Year:** 2014
**Source type:** primary mechanistic DDR study
**Journal/source:** *Proceedings of the National Academy of Sciences USA*
**Identifier:** PMID 25331887 / DOI 10.1073/pnas.1409252111
**Status:** integrated
**Primary pathway:** genome stability / ATM / DNA damage response
**Secondary pathway:** developmental vulnerability (candidate)
**Model/species:** cellular DDR systems / cancer-linked mechanistic context
**Genotype/model:** WWOX deficiency with damage-induced nuclear relocalization and ATM interaction; non-CNS pediatric direct
**Transferability:** T2 conceptual / indirect
**clinical relevance:** LOW direct / MEDIUM structural
**Claim links:** 029
**Role:** new structural-axis paper
**Note:** Shows that WWOX deficiency reduces ATM activation, compromises γ-H2AX response and impairs DNA repair; introduces a plausible genome-/replicative-stress vulnerability branch relevant to proliferative developmental compartments, but not yet promotable to core clinical logic.


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
**Status:** claim_linked
**Evidence depth:** abstract reviewed (PubMed metadata; full text not yet extracted)
**Primary pathway:** genome stability / ATM / DNA damage response
**Model/species:** HEK293, HeLa, mouse — non-CNS, oncology/DDR
**Genotype/model:** Wwox deficiency (cell lines + mouse); not pediatric CNS
**Transferability:** T2 conceptual / indirect for the reference genotype
**clinical relevance:** INDIRECT — structurally important (genome-stability axis), not operational
**Claim links:** 029
**Role:** primary mechanistic source for the WWOX→ATM/DDR axis (CLAIM 029)
**Note:** Promosso 2026-06-28 (BATCH_20260628_002) da corpus-paper 138 a PAPER record completo per ancorare CLAIM 029. Metadati verificati via PubMed (According to PubMed). Tesi: Wwox-deficiency riduce attivazione ATM, compromette induzione/mantenimento γ-H2AX, impairs DNA repair; danno → ITCH-mediata K63-ubiquitinazione di WWOX su Lys274 → accumulo nucleare → interazione con ATM. Contesto tumorale/genome-instability, NON CNS pediatrico → CLAIM 029 resta `in observation`. Full text non ancora estratto (solo abstract).
**Wikilinks:** [[claim_registry_current#CLAIM 029]]


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
**Claim links:** 021
**Role:** fonte primaria verificata di CLAIM 021 (network-state pathology come core pathway)
**Note:** Promosso 2026-07-05 (CC-2026-07-05-003) da placeholder corpus a PAPER pieno; CLAIM 021 era ancorato solo a [[paper_registry_current#CORPUS P210]] (identificato via review Obeid 2026), ora ancorato a full-text verificato. According to PubMed, [DOI](https://doi.org/10.1016/j.nbd.2021.105529). Contenuto verificato: burst neocorticali spontanei (36/42 slice KO vs 0/11 WT), assenti in ippocampo (patologia predominante di rete neocorticale), propagazione L2/3→L5 ~11 mm/s, accoppiamento fase-ampiezza delta-gamma/theta-HFO (biomarker epilessia pediatrica); burst NMDAR- e gap-junction-dipendenti (d-APV abolisce; carbenoxolone ↓87%; pannexina no); ↑ampiezza mEPSC (postsinaptico), ↓ampiezza+frequenza sIPSC (sbilancio E/I); piramidali L2/3 depolarizzati, ↑sag/Ih, ↑rebound post-inibitorio. Lead terapeutici (IPOTESI, non DATO): blocco gap-junction / modulazione NMDAR — ⚠️ CBX non specifico, Ih-blocker (ZD7288) controversi. ⚠️ Duplicati corpus **CORPUS P210** e **CORPUS P300** (stesso paper) → mergiare in un prossimo BATCH_COMMIT.
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
**Evidence depth:** full text verificato (staging/fulltext_xml_20260705/30619736_PMC6300487.xml)
**Primary pathway:** P5 — trafficking / endomembrane systems / metabolism
**Secondary pathway:** P3 — Wnt/DVL / scaffold-interaction logic
**Model/species:** HEK293T TAP-MS / proteomics; validation co-IP/GST pulldown
**Genotype/model:** full-length WWOX SFB-tag interactome; not WWOX-DEE/patient model
**Transferability:** T2 conceptual
**clinical relevance:** INDIRECT-HIGH for biomarker/readout design; no direct clinical action
**Claim links:** 026
**Role:** primary mechanistic source for CLAIM 026 (WWOX interactome / trafficking-metabolism coupling)
**Note:** Promosso 2026-07-05 (CC-2026-07-05-004) da [[paper_registry_current#CORPUS P182]] placeholder a PAPER pieno; full text verificato via PMC. TAP-MS identified 216 high-confidence WWOX binding partners. Top interactors include DVL2, WBP2, DHRS13, HIRIP3, SEC23IP, VOPP1, AMOT, DVL1, VARS2, SCAMP3. Co-IP/GST pulldown validated WWOX binding with SEC23IP, SCAMP3 and VOPP1. Enriched pathways include valine/leucine/isoleucine degradation, glycolysis/gluconeogenesis, pyruvate metabolism and fatty acid degradation, converging on Acetyl-CoA generation. Normalizes previous `CORPUS P182` placeholder; do not duplicate.
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-004
**Corpus paper no:** 4
**Full title:** WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders
**Identifier:** PMID 33255508 / DOI 10.3390/ijms21238922
**Status:** not_processed
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
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-007
**Corpus paper no:** 7
**Full title:** The WWOX gene in brain development and pathology
**Identifier:** PMID 32389029 / DOI 10.1177/1535370220924618
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-011
**Corpus paper no:** 11
**Full title:** Modeling WWOX Loss of Function in vivo: What Have We Learned?
**Identifier:** PMID 30370248 / DOI 10.3389/fonc.2018.00420
**Status:** not_processed
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
**Corpus paper no:** 22
**Full title:** Decoding the link between WWOX and p53 in aggressive breast cancer
**Identifier:** PMID 31075076 / DOI 10.1080/15384101.2019.1616998
**Status:** not_processed
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
**Corpus paper no:** 27
**Full title:** WWOX promotes osteosarcoma development via upregulation of Myc
**Identifier:** PMID 38182577 / DOI 10.1038/s41419-023-06378-8
**Status:** not_processed
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-056
**Corpus paper no:** 56
**Full title:** WWOX promotes apoptosis and inhibits autophagy in paclitaxel-treated ovarian carcinoma cells
**Identifier:** PMID 33300063 / DOI 10.3892/mmr.2020.11754
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-060
**Corpus paper no:** 60
**Full title:** Epilepsy in patients with WWOX-related epileptic encephalopathy (WOREE) syndrome
**Identifier:** PMID 35792847 / DOI 10.1684/epd.2022.1444
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-074
**Corpus paper no:** 74
**Full title:** Wwox Binding to the Murine Brca1-BRCT Domain Regulates Timing of Brip1 and CtIP Phospho-Protein Interactions
**Identifier:** PMID 35409089 / DOI 10.3390/ijms23073729
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
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
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-078
**Corpus paper no:** 78
**Full title:** WWOX loss activates aerobic glycolysis
**Identifier:** PMID 27308416 / DOI 10.4161/23723548.2014.965640
**Status:** not_processed
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
**Status:** not_processed
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
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-088
**Corpus paper no:** 88
**Full title:** Wwox Deletion in Mouse B Cells Leads to Genomic Instability, Neoplastic Transformation, and Monoclonal Gammopathies
**Identifier:** PMID 31275852 / DOI 10.3389/fonc.2019.00517
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-096
**Corpus paper no:** 96
**Full title:** Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome
**Identifier:** PMID 37974179 / DOI 10.1186/s12920-023-01731-4
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-102
**Corpus paper no:** 102
**Full title:** WWOX and p53 Dysregulation Synergize to Drive the Development of Osteosarcoma
**Identifier:** PMID 27550453 / DOI 10.1158/0008-5472.CAN-16-0621
**Status:** not_processed
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-108
**Corpus paper no:** 108
**Full title:** The WWOX gene modulates high-density lipoprotein and lipid metabolism
**Identifier:** PMID 24871327 / DOI 10.1161/CIRCGENETICS.113.000248
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-109
**Corpus paper no:** 109
**Full title:** Associations between TUBB-WWOX SNPs, their haplotypes, gene-gene, and gene-environment interactions and dyslipidemia
**Identifier:** PMID 33612478 / DOI 10.18632/aging.202514
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-110
**Corpus paper no:** 110
**Full title:** Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation [PREPRINT bioRxiv]
**Identifier:** PMID 39868255 / DOI 10.1101/2025.01.17.633677
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Corpus paper no:** 113
**Full title:** Unveiling the relationship between WWOX and BRCA1 in mammary tumorigenicity and in DNA repair pathway selection
**Identifier:** PMID 38499540 / DOI 10.1038/s41420-024-01878-8
**Status:** not_processed
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
**Status:** not_processed
**Integrity status:** 🔴 `PUBLICATION_INTEGRITY_HOLD` — **expression of concern**. Field added in `BATCH_20260806_002`, closing a debt declared on 2026-08-06. **No canonical claim rests on this record.** It is cited once, as reference 17 of [[paper_registry_current#PAPER 057]], among four background xenograft examples in that paper's Introduction, and supports none of its measured results — verified during the complete read (`FTR-20260806-19936220-01`). Not admissible as evidentiary support; admissible only as bibliographic lineage.
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-120
**Corpus paper no:** 120
**Full title:** Endothelial knockdown of WWOX increases inflammation in ventilator-induced lung injury
**Identifier:** PMID 38563965 / DOI 10.1152/ajplung.00277.2023
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Corpus paper no:** 123
**Full title:** WWOX guards genome stability by activating ATM
**Identifier:** PMID 27308504 / DOI 10.1080/23723556.2015.1008288
**Status:** not_processed
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
**Status:** not_processed
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-148
**Corpus paper no:** 148
**Full title:** WWOX protein expression varies among ovarian carcinoma histotypes and correlates with less favorable prognosis
**Identifier:** PMID 15982416 / DOI 10.1186/1471-2407-5-64
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-152
**Corpus paper no:** 152
**Full title:** Tumor Suppressor WWOX inhibits osteosarcoma metastasis by modulating RUNX2 function
**Identifier:** PMID 26256646 / DOI 10.1038/srep12959
**Status:** not_processed
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.

## CORPUS-STUB-165
**Corpus paper no:** 165
**Full title:** VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX
**Identifier:** PMID 30285739 / DOI 10.1186/s12915-018-0576-6
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Corpus paper no:** 175
**Full title:** WWOX-related epileptic encephalopathy caused by a novel mutation in the WWOX gene: a case report
**Identifier:** PMID 39416860 / DOI 10.3389/fped.2024.1453778
**Status:** not_processed
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
**Status:** not_processed
**Registry role:** corpus placeholder only
**Claim links:** none
**Next action:** screening / triage required
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
**Status:** screened — corpus placeholder
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
**Status:** screened — corpus placeholder
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
**Short title:** Frequent downregulation and loss of WWOX gene expression in human hepatocellu...
**Full title:** Frequent downregulation and loss of WWOX gene expression in human hepatocellular carcinoma
**Authors:** Park et al.
**Year:** 2004
**Source type:** Article
**Journal/source:** Br J Cancer
**Identifier:** PMID 15266310 / PMC2364795 / DOI 10.1038/sj.bjc.6602023
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0244
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** cell line
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Authors:** Pimenta et al.
**Year:** 2008
**Source type:** Article
**Journal/source:** Oral Oncol
**Identifier:** PMID 18061530 / PMC4143237 / DOI 10.1016/j.oraloncology.2007.08.019
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0260
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P261
**Short title:** Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenes...
**Full title:** Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenesis of osteosarcoma
**Authors:** Mare et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Am J Cancer Res
**Identifier:** PMID 21731849 / PMC3124638
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0261
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Status:** screened — corpus placeholder
**LIT link:** LIT-0263
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** rat
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** MODERATE
**Claim links:** none — triage only
**Role:** secondary full-text target
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Status:** screened — corpus placeholder
**LIT link:** LIT-0268
**Primary pathway:** clinical spectrum / WWOX-DEE
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Status:** screened — corpus placeholder
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
**Status:** screened — corpus placeholder
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
**Status:** screened — corpus placeholder
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
**Short title:** Association between decreased WWOX protein expression and thyroid cancer deve...
**Full title:** Association between decreased WWOX protein expression and thyroid cancer development
**Authors:** Dias et al.
**Year:** 2007
**Source type:** Article
**Journal/source:** Thyroid
**Identifier:** PMID 18047428 / PMC4150466 / DOI 10.1089/thy.2007.0232
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0286
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Model/species:** rat
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
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
**Status:** screened — corpus placeholder
**LIT link:** LIT-0305
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

## CORPUS P306
**Short title:** WWOX oxidoreductase--substrate and enzymatic characterization
**Full title:** WWOX oxidoreductase--substrate and enzymatic characterization
**Authors:** Sałuda-Gorgul et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Z Naturforsch C J Biosci
**Identifier:** PMID 21476439
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0306
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Status:** screened — corpus placeholder
**LIT link:** LIT-0308
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Authors:** Nunez et al.
**Year:** 2005
**Source type:** Comparative Study
**Journal/source:** Breast Cancer Res Treat
**Identifier:** PMID 15692750 / PMC4145848 / DOI 10.1007/s10549-004-1474-x
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0324
**Primary pathway:** P5 — metabolism / mitochondria / redox
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Status:** screened — corpus placeholder
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
**Short title:** WWOX mRNA expression profile in epithelial ovarian cancer supports the role o...
**Full title:** WWOX mRNA expression profile in epithelial ovarian cancer supports the role of WWOX variant 1 as a tumour suppressor, although the role of variant 4 remains unclear
**Authors:** # et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Int J Oncol
**Identifier:** PMID 15870886 / PMC4166600 / DOI 10.3892/ijo.26.6.1681
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0337
**Primary pathway:** oncology / tumor suppressor biology
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Status:** screened — corpus placeholder
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
**Year:** 2026
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
**Status:** screened — corpus placeholder
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
**Authors:** Pimenta et al.
**Year:** 2006
**Source type:** Article
**Journal/source:** Int J Cancer
**Identifier:** PMID 16152610 / PMC4145845 / DOI 10.1002/ijc.21446
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0367
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Short title:** Impact of decitabine on immunohistochemistry expression of the putative tumor...
**Full title:** Impact of decitabine on immunohistochemistry expression of the putative tumor suppressor genes FHIT, WWOX, FUS1 and PTEN in clinical tumor samples
**Authors:** Stewart et al.
**Year:** 2014
**Source type:** Article
**Journal/source:** Clin Epigenetics
**Identifier:** PMID 25024751 / PMC4094901 / DOI 10.1186/1868-7083-6-13
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0378
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** human
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Authors:** Thavathiru et al.
**Year:** 2005
**Source type:** Article
**Journal/source:** Mol Carcinog
**Identifier:** PMID 16187332 / PMC4166602 / DOI 10.1002/mc.20122
**Tier (FASE 1):** C
**Status:** screened — corpus placeholder
**LIT link:** LIT-0385
**Primary pathway:** P6 — DDR / genome stability
**Model/species:** not assessed in triage
**Genotype/model:** unassigned in triage
**Transferability:** unassigned in triage
**clinical relevance:** LOW
**Claim links:** none — triage only
**Role:** background corpus only
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.

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
**Status:** screened — corpus placeholder
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
**Identifier:** PENDING — likely overlaps PAPER 026 (PMID 32185845, WWOX–p73 phospho-binding); verify before merge
**Status:** deep-dived — registry placeholder (lint restored)
**Note:** Source description from tracking log 2026-04-17. Possible duplicate of PAPER 026 — flagged for the operator.

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
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read; Expanded-View raw tables non incluse)
**Primary pathway:** P1 — network hyperexcitability / E-I balance
**Secondary pathway:** P5 — metabolism (OXPHOS↓/glycolysis↑); P3 — Wnt; DDR
**Model/species:** human cerebral & forebrain organoids; WiBR3 hESC WWOX-KO; patient iPSC (WSM c.517-2A>G WOREE; WPM G372R SCAR12); W-AAV / lenti-WWOX rescue
**Genotype/model:** KO ≠ the reference genotype (compound het N/M); patient lines include an SDR-domain missense (G372R)
**Transferability:** T2
**clinical relevance:** HIGH — piattaforma umana + il controllo negativo (G372R) necessario a testare il rescue proteostatico
**Claim links:** 002, 030, 032
**Role:** primary source for CLAIM 002 extension; provides the human bench for HYP-08
**Note:** Promosso in BATCH_20260710_A da [[paper_registry_current#CORPUS P365]] (Tier A, priorità HIGH, mai deep-dived). Findings: **GABA depolarizzante** — GAD67/GAD1/GAD2 ↑, VGLUT1 invariato, GABRB2/3 ↓; neuroni da paziente WOREE scaricano a ~4× la frequenza dei genitori (P<0.0001), **normalizzata dal rescue W-AAV (P=0.77)**. LFP: potenza ↑ in banda 0.25–1 Hz; iperreccitabilità sotto 4-aminopiridina 100 µM. DDR: γH2AX 1.5 (KO) vs 0.78 (WT) vs 0.58 (W-AAV); checkpoint apoptotico perso. Wnt cronicamente attivo (β-catenina nucleare ~1.7×). RNA-seq (GEO **GSE156243**): **OXPHOS/ATP-synthesis ↓, glicolisi ↑** → fenotipo Warburg in **tessuto neurale umano**; autofagia (RB1CC1/FIP200) e mTOR/EIF4EBP1 ↓. Discussione: la severità potrebbe correlare con i **livelli funzionali** di WWOX, non con quelli totali (G372R mostra proteina quasi assente all'IF ma fenotipo lieve). ⚠️ **Vincolo BLOCCO 1:** il rescue W-AAV era **supra-fisiologico e in tutte le popolazioni cellulari**, con recupero **solo parziale**; gli autori richiamano *"population-targeted delivery and fine-tuning of expression levels"*. **Né troppo poco né troppo WWOX.** Lead terapeutico non ancora forgiato: **bumetanide/NKCC1** (correzione del GABA depolarizzante) — da safety-triage. ⚠️ La microcefalia **non** è ricapitolata negli organoidi.
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
**Evidence depth:** full text reviewed (via PMC web; non-OA all'API)
**Primary pathway:** genotype-phenotype / WW1 domain function
**Model/species:** human — fibroblasti di paziente; due famiglie
**Genotype/model:** **p.Pro47Thr omozigote** (WW1) e **p.Gly372Arg omozigote** (SDR) — entrambi SCAR12, fenotipo lieve
**Transferability:** T1/T2 — genotipo caution OBBLIGATORIA: P47T ≠ Q230P (domini e meccanismi diversi)
**clinical relevance:** HIGH — è il controllo che dimostra che l'abbondanza di proteina non predice la severità
**Claim links:** 007, 008, 019, 030
**Role:** fonte primaria della serie allelica; àncora della regola "P47T ≠ Q230P"
**Note:** Promosso in BATCH_20260710_A da [[paper_registry_current#CORPUS P294]]. **Finding decisivo:** Western blot su fibroblasti del paziente P47T (passaggi 10/13/14 vs 4 controlli) → *"similar amounts of the mutant and wild-type WWOX protein"*; *"the mutation does not alter global protein levels"*. **La proteina P47T è presente a livelli normali.** Peptide pull-down: *"only the wild-type and not the mutant fusion peptides were efficiently pulled down with the PPPY containing oligopeptide"* → **P47T abolisce completamente il binding ai motivi PPxY**. Gli autori spiegano la mitezza del fenotipo con *"a partial loss of function… the dehydrogenase/reductase domain of the mutant protein is presumably still functional"*. Pazienti vivi a 17-26 anni. → **Nessuna menzione di Gln230.** Vedi [[claim_registry_current#CLAIM 030]].
**Wikilinks:** [[claim_registry_current#CLAIM 007]] · [[claim_registry_current#CLAIM 008]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]]

---

## PAPER 045
**Short title:** Shaukat 2018 — West syndrome / DEE in WWOX-null
**Full title:** West syndrome, developmental and epileptic encephalopathy, and severe CNS disorder associated with WWOX mutations
**Authors:** Shaukat Q, Hertecant J, El-Hattab AW, Ali BR, Suleiman J
**Year:** 2018
**Source type:** primary — case reports (n=2) + review of 23 reported cases
**Journal/source:** *Epileptic Disord* 2018;20(5):401-12
**Identifier:** PMID 30361190 / DOI 10.1684/epd.2018.1005 — bronze OA
**Status:** claim_linked
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read; PDF recuperato da JLE, testo estratto con PyMuPDF; Table 1 in colonne verticali, mappatura varianti verificata riga per riga)
**Primary pathway:** clinical spectrum / treatment response
**Secondary pathway:** P2 — GABAergic safety (vigabatrin)
**Model/species:** human — due bambini non imparentati, famiglie consanguinee
**Genotype/model:** null biallelici — caso 1: delezione omozigote esoni 3-4; caso 2: **splice acceptor omozigote c.606-1G>A** (introne 6)
**Transferability:** T1
**clinical relevance:** VERY HIGH
**Claim links:** 001, 031
**Role:** fonte primaria per il concetto DEE-non-EE e per il lato "efficacia" del claim vigabatrin
**Note:** Promosso in BATCH_20260710_A da [[paper_registry_current#CORPUS P356]] (Tier A, priorità HIGH, mai deep-dived). **Trattamento:** caso 1 — prednisolone (protocollo UKISS) → risposta parziale; **vigabatrin → "the spasms resolved"**; poi mioclonie focali/cloniche migliorate con **levetiracetam**. Caso 2 — fenobarbital → miglioramento; **vigabatrin → risposta parziale**; a 11 mesi spasmi in cluster nonostante 4 antiepilettici. **Nessun VABAM riportato.** **DEE non EE (testuale):** *"The developmental outcome was unfavourable with profound impairment **despite improvement of epileptic activity**"*; *"the cognitive and psychomotor impairment **preceded the onset of epileptic encephalopathy** and **did not improve with achievement of better control of epileptic activity**"*. **Fenotipo intermedio:** Table 1 riporta due fratelli (Mignot 2015, casi 3-4) compound eterozigoti **frameshift + missense (p.Pro47Arg)** con ritardo profondo ed epilessia severa ma **senza tetraparesi spastica, senza microcefalia e con RMN normale**. Su 23 casi: ritardo severo + epilessia in **23/23**; tetraparesi spastica **14/23** → è la spasticità, non l'epilessia, a discriminare. **Polimicrogiria** parietale bilaterale nel caso 2 → WWOX partecipa alla migrazione neuronale. **Metabolico normale** in entrambi (lattato, ammonio, acilcarnitine, aminoacidi, acidi organici, transferrina). Microcefalia **acquisita** (nascita normale → −3.38 SD a 6 mesi).
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
**Evidence depth:** full text reviewed (CC-2026-07-05-007, letto per intero)
**Primary pathway:** genotype-phenotype / clinical spectrum
**Model/species:** human — meta-coorte da letteratura e database
**Genotype/model:** 56 pazienti WOREE/DEE28 + 6 SCAR12 (la coorte pubblicata più ampia al 2021)
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
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)
**Primary pathway:** clinical spectrum / null biallelico
**Model/species:** human — famiglia egiziana consanguinea
**Genotype/model:** **p.Arg54\* omozigote** (c.160G>T, esone 2) — nonsenso, null biallelico "puro"
**Transferability:** T1
**clinical relevance:** HIGH — è il benchmark del caso peggiore (proteina zero su entrambi gli alleli)
**Claim links:** 030, 032
**Role:** estremo inferiore della serie allelica; sostiene il claim sull'aploinsufficienza
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P359]]. Fenotipo index: esordio crisi a **2 mesi**, risposta **parziale** a valproato + lamotrigina; **microcefalia progressiva/acquisita** (OFC −3.6 SD a 3 mesi → **−4.6 SD a 12 mesi**); nessuna tappa di sviluppo acquisita; **atrofia ottica + pigmentazione retinica anomala**, ERG ridotto, VEP ritardato; RMN: atrofia sopratentoriale, pattern girale semplificato, ipoplasia ippocampo/lobo temporale, **corpo calloso sottile**; **cervelletto non menzionato**. **Screening metabolico e mitocondriale interamente normale** (ammonio, lattato, aminoacidi, acidi organici, VLCFA, biopsia muscolare). **Morte a 16 mesi in stato epilettico.** Sorella: morta a 3 mesi. ⭐ **Citazione chiave per [[claim_registry_current#CLAIM 032]]:** *"As in rats, **no tumors** were observed in the patient or **heterozygous mutation carriers**"* → i portatori eterozigoti sono sani e non oncologicamente a rischio. ⚠️ Limiti: famiglia singola, **nessun assay proteico** (la nullità è inferita dal nonsenso), nessuna autopsia.
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
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P300]] (Tier A, priorità HIGH, mai deep-dived). **Finding trasferibile:** *"the deletion led to **nonsense-mediated decay** of the NM_016373.3 transcript; the exon 6 of an **alternative transcript (NM_130791.3), lacking the short-chain dehydrogenase**, was utilized"*. Al Western: **isoforma piena da 46 kDa (contiene il dominio SDR) persa**; **isoforma corta da 19 kDa (solo domini WW) aumentata** → **abbondanza senza funzione**. ⭐ **Clinical relevance:** il triplo assay (qPCR giunzione-specifica sui tre trascritti + Western isoform-resolved + ddPCR CNV) è il **template pronto** per dimostrare l'effetto dell'allele di sito accettore `c.1057-2A>G`. ⚠️ Nota critica: qui l'NMD **avviene** perché la lesione è sull'**esone 6**; l'esone 9 è l'**ultimo**, e un PTC nell'ultimo esone **sfugge all'NMD** — l'assay per il genotipo di riferimento va progettato di conseguenza (discovery ledger DL-MECH-045). **MRS cerebrale: lattato "estremamente basso"** — outlier confuso dalla variante HSPG2.
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
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)
**Primary pathway:** neuroimaging / clinical monitoring
**Model/species:** human — 101 casi da 9 studi
**Genotype/model:** misto
**Transferability:** T2
**clinical relevance:** MODERATE — utile per gli endpoint di imaging, **non** come fonte di prevalenze
**Claim links:** none — background
**Role:** background di imaging; **non** fonte di claim (review secondaria)
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P298]] come **background**. ⚠️ **Limite metodologico dirimente:** review **narrativa non sistematica**, senza PRISMA né criteri di inclusione; le coorti **si sovrappongono** (Banne n=56 ricompila casi già pubblicati) → **nessuna prevalenza aggregata è calcolabile**; solo le percentuali intra-studio sono oneste. **Reperto più costante:** corpo calloso ipoplasico/sottile, presente in **tutti e 9** gli studi. Poi atrofia cerebrale, iperintensità T2 simmetriche della sostanza bianca, atrofia ottica, ritardo di mielinizzazione. Anomalie già a **15-19 giorni**; **RMN fetale a 21 settimane**: lieve ipoplasia del verme cerebellare con girazione e laminazione corticale **normali**. Progressione su imaging seriato (Tabarki 5/5; Oliver 7/13). ⚠️ **Due correzioni ai nostri prior:** (1) "atrofia ottica 100% a tutte le età" vale **solo nella coorte Oliver**, dove è stata cercata sistematicamente; altrove non tabulata → sotto-accertata. (2) **Non usare "demielinizzazione progressiva"**: la review parla sistematicamente di **ritardo di mielinizzazione / ipomielinizzazione** e di **atrofia progressiva** — un ritardo è in principio recuperabile, una demielinizzazione molto meno. La questione resta aperta. **Omissione rilevata:** la review nega la polimicrogiria, che è invece documentata in [[paper_registry_current#PAPER 045]] (Shaukat, caso 2) e in Ben-Salem 2015. ⭐ **For the disease model:** *"the p.Gln230Pro pathogenic variant affects the S[D]R domain and has been described both in homozygosity and in compound heterozygosity in **eight cases overall**. Nevertheless, **how missense variants affecting the SDR domain impair WWOX catalytic activity has not been demonstrated yet**."* → Q230P è un **hotspot ricorrente**; il suo meccanismo è dichiarato **non dimostrato**. **Gap:** nessuna metrica quantitativa (no volumetria, no area del CC, no DTI/FA, no MRS strutturata, no OCT/ERG/VEP) → un endpoint di imaging per il genotipo di riferimento va progettato internamente.
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
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)
**Primary pathway:** clinical spectrum / null biallelico
**Model/species:** human — famiglia araba consanguinea (Qatar)
**Genotype/model:** **p.Trp44Stop omozigote** (c.131G>A, esone 2) — null biallelico
**Transferability:** T1
**clinical relevance:** HIGH — comparatore fenotipico del null puro
**Claim links:** 031, 032
**Role:** fonte primaria sul decorso del null biallelico e sulla risposta agli antiepilettici
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS P343]]. Esordio crisi a **7 settimane** in entrambe le sorelle. **Case 1 (older sibling): fenobarbitone, clonazepam, fenitoina e levetiracetam tutti falliti**; sorella: risposta **parziale** a topiramato/clobazam. RMN: **scarsa mielinizzazione già a 9 settimane**, assente a 23; assottigliamento simmetrico del **corpo calloso**; atrofia fronto-temporale; deformità ippocampale; **nessuna microcefalia** (OFC +0.37 SD). EEG: **perdita degli elementi del sonno**, background discontinuo, ~8 spasmi/ora su registrazione 24h. Pallore dei dischi ottici con **ERG normale**. Workup metabolico e mitocondriale interamente normale. Genitori **eterozigoti sani** ([[claim_registry_current#CLAIM 032]]). ⚠️ **Nota terminologica (correzione):** questo case report descrive la mielinizzazione come progressivamente compromessa; **non se ne inferisca "demielinizzazione progressiva"** come descrizione di malattia — la letteratura più ampia parla di **ipomielinizzazione + atrofia progressiva** ([[paper_registry_current#PAPER 046]]). ⚠️ W44X non è mai stata validata funzionalmente (NMD solo predetta).
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
**Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)
**Primary pathway:** P5 — metabolism; interattoma; CNS
**Model/species:** review — topo, umano
**Genotype/model:** modelli murini condizionali; GWAS umani
**Transferability:** T2
**clinical relevance:** HIGH per il claim sull'aploinsufficienza; **background** per il resto
**Claim links:** 032
**Role:** fonte (secondaria) del dato sull'aploinsufficienza; background su interattoma e metabolismo
**Note:** Promosso in BATCH_20260710_B da [[paper_registry_current#CORPUS-STUB-020]] come **background con un claim link**. ⭐ **Citazioni chiave per [[claim_registry_current#CLAIM 032]]:** *"loss of one Wwox allele (i.e. **haploinsufficiency**) appears **not to be deleterious** or carcinogenic in the longer-lived heterozygous mice"*; *"The lifespan of the Wwox heterozygotes was **indistinguishable from WT mice**"*; *"loss of a single Wwox allele… **did not have any observable phenotypic effect** in the mammary gland"*. ⚠️ Nota: negli eterozigoti è documentato **aumento di tumorigenicità sotto carcinogeni chimici** o su fondo suscettibile — irrilevante per una strategia che *aumenta* WWOX, ma da non dimenticare. **Altri contenuti**: WWOX degradato via **poliubiquitinazione/proteasoma** (ACK1 fosforila Tyr287; substrato dell'E3 ligasi **ITCH**) — ⚠️ meccanismi di degradazione **regolata**, non controllo-qualità di proteina misfolded: **non assumere** che inibire ACK1/ITCH salvi Q230P. Il dominio **SDR governa anche la localizzazione subcellulare** (S281A/Y293F/K297A necessari sia alla catalisi sia alla localizzazione perinucleare) → il readout funzionale di Q230P deve includere la **localizzazione**. WWOX inibisce TGFβ/SMAD3 sequestrando SMAD3 nel citoplasma. Topi Wwox-KO: morte postnatale 72h-4 settimane, **ipoglicemia**, ipocalcemia, acidosi metabolica, nanismo. ⚠️ **Conflicting evidence da registrare:** Aldaz colloca WWOX in sede **perinucleare/Golgi** e attribuisce il ruolo pro-apoptotico riportato dal lab Chang ad **artefatto da vettori adenovirali**; il lab Chang lo colloca in mitocondri e nucleo. La disputa tocca direttamente il SDR.
**Wikilinks:** [[claim_registry_current#CLAIM 032]] · [[paper_registry_current#PAPER 021]]

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
**Note:** WWOX lega GSK3β tramite il dominio ADH/SDR su un segmento di 20 residui (**388–407**) omologo al motivo di docking Axin/FRAT/GSKIP, con **L404 strettamente necessario**: `L404A` abolisce legame, inibizione della chinasi in vitro e in cellula, recupero dell'assemblaggio dei microtubuli e beneficio sul differenziamento, mentre il vicino `L311A` non fa nulla di tutto ciò. Il legame blocca la fosforilazione di Tau su **S396/S404** ma non su S422 (sito MKK4), **con GSK3β totale e fosfo-S9 invariati**. Il risultato più fisiologico è la **co-IP reciproca fra proteine endogene in estratto di cervello di topo**. 🔴 **Difetto documentato:** la Supplementary Figure A, citata dal testo *e* dalla propria legenda come la co-IP che dimostra *«WWOX does not associate with Tau»*, **non contiene alcun blot per Tau** — i suoi due pannelli sono etichettati WWOX e GSK3β. Il negativo **non è valutabile**: vedi [[dismissal_ledger_current#DIS-010 — «WWOX non lega Tau (Wang 2012)» → ⏸️ **NON STABILITA — il negativo è rifiutato per assenza di dato**]]. ⚠️ Altri limiti trovati leggendo: linea cellulare unica e aneuploide; sovraespressione ovunque (stechiometria endogena mai misurata); endpoint di differenziamento soggettivo e non in cieco; ampiezze d'effetto **incoerenti fra figure** per la stessa manipolazione; il saggio chinasico non è ricostruibile senza ambiguità (0.3 vs 0.2 µg di GST-WWOX, 25 µg/ml vs 0.5 µg di Tau, 30 °C/20 min vs 20 °C/10 min); il modello di interfaccia Fig 3f-h è **predizione GOR IV innestata su 1O9U**, non dato strutturale; il controllo di folding per L404A è a **partner singolo** (c-jun); WWOXtide è attivo a concentrazione **millimolare**. ⚠️ Il co-autore **Chang N-S** è l'originatore del campo WWOX; [[paper_registry_current#PAPER 053]] registra che le affermazioni del suo laboratorio su **localizzazione** e ruolo pro-apoptotico sono contestate da Aldaz. Nulla in questo lavoro dipende da quella localizzazione contesa, quindi la disputa non si propaga — ma il flag viaggia con qualunque uso della sua cornice di biologia cellulare. **Lineage:** il riferimento `CORPUS P263` del candidato CC-20260726-003 è un indice della TSV di seed, **non** il record [[paper_registry_current#CORPUS P263]] del registry (che è Chang 2014, PMID 25537520).
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
