# Discovery Ledger — capitale di scoperta cumulativo (WWOX → biomarcatori / molecole / repurposing)

> **Public edition — de-identified, disease-level.** This is LEGEND's *compounding memory*: the cumulative discovery capital that makes each new batch of papers more productive than the last. It is the artifact that distinguishes the system from a bibliography — leads are never deleted, only re-statused, and every lead carries its causal statement, its reasoning chain, its counter-evidence and the experiment that would falsify it.
>
> All individual-linking material has been removed: no identified person, no report or sample identifier, no institution, no family-relationship data, no treatment schedule. Where the private edition reasoned about one child, the public edition reasons about **the reference genotype** — a disease-level genotype class of WWOX-DEE (a destabilizing SDR missense allele and a canonical splice-acceptor allele, carried independently as public worked examples). Cells are described as **donor-derived**. Links whose target is a private operational log (commit queue, inbox, capability-scout log) are rendered as plain text, not broken links.
>
> Much of the body remains in its original language: it is preserved verbatim rather than re-written, because a faithful record of how the reasoning actually developed is worth more here than a polished translation. **Not medical advice.**
>
> Research-layer working file. Append-only sui lead; status, mai cancellazione.
> Tag epistemici: DATO / INFERENZA / IPOTESI / ESPANSIONE. Promozione a canonico SOLO via COMMIT CANDIDATE.
> Status lead: open · maturing · promoted-to-CC · parked · refuted
> Creato: 2026-06-28 · WM di riferimento: WM_v3.0_2026-07-14

## Indice per pathway
- Mielina/glia · Metabolismo/sfingolipidi · Struttura prenatale/GSK3β · GABA · Neuroinfiammazione · Asse cerebellare · **Cross-pathway / network-state (attivo)**

---

## BIO — lead biomarcatore
*(da Riccardi 2026: nessun lead Tier 1/2 — l'EEG è Tier 3 → vedi MECH-003 / endpoint clinico)*

### DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)
- **Status**: open · **Tag**: IPOTESI · **Cosa si misura**: proteina WWOX (Western) + **attività SDR/ossidoreduttasica** dell'allele missense residuo · **Matrice**: fibroblasti cutanei donor-derived (o LCL) · **Vicinanza a WWOX**: massima (è WWOX stesso) → candidato **Tier 1/2**
- **Fonte**: record pubblici di variante (ClinVar / Ensembl VEP) × ragionamento strutturale AlphaFold3/AlphaMissense — *modello da eseguire, non ancora girato*
- **Mappa ABC**: A=WWOX-LoF del genotipo di riferimento · B=destabilizzazione/perdita di folding del dominio SDR predetta in silico per p.Q230P · C=readout misurabile = quantità+attività enzimatica WWOX in fibroblasti
- **Statement causale**: `Q230P —predicted_destabilizes→ WWOX_SDR_fold`; (inferito) `SDR_destabilization —decreases→ WWOX_oxidoreductase_activity`; `fibroblast_WWOX_activity —proxies→ residual_functional_state` · **Belief**: medio (la prolina in un dominio SDR è classico destabilizzante; ma in-silico ≠ dimostrato)
- **Catena di ragionamento**: Q230 cade nel **dominio SDR**, ma **NON è un residuo catalitico** — la mappa del sito attivo SDR di WWOX è S260 (substrato), **S281 + motivo YxxxK Y293–K297** (catalisi), motivo Rossmann GxxxGxG N-terminale per NAD ([struttura, PMC4374002](https://pmc.ncbi.nlm.nih.gov/articles/PMC4374002/)). Q230 è quindi **strutturale**, non catalitico → Gln→Pro (prolina = rigidità backbone, killer dei foglietti/eliche) destabilizza il *folding* della piega di Rossmann → **proteina instabile/degradata**, non enzima cataliticamente morto-ma-presente. **Conferma chiave**: il working model riporta che varianti SDR-missenso analoghe danno *trascritto normale ma proteina assente/instabile* (meccanismo post-traduzionale). → il readout primario è la **quantità/stabilità proteica** (Western, pulse-chase), l'attività SDR è secondaria. **L'output in-silico non è il biomarcatore**: nomina il readout wet.
- **Evidenza**: supporta=Q230 strutturalmente plausibile come perturbazione + endpoint umano `mRNA normale/proteina non rilevata` (Johannsen); refuta/limita=AlphaFold modella struttura statica, non sintesi/stabilità/degradazione; causa da discriminare con metabolic labeling, solubilità e pulse-chase.
- **Esperimento proposto**: (1) in silico — AlphaFold3 WT vs Q230P + AlphaMissense + ΔΔG (FoldX/Rosetta) → soglia di destabilizzazione predetta; (2) wet — Western WWOX e assay ossidoreduttasico su fibroblasti donor-derived vs controllo. Readout atteso: ↓ proteina e/o ↓ attività SDR. **Fattibile** su fibroblasti donor-derived (la biopsia cutanea è una procedura diagnostica standard).
- **Razionale di trasferimento**: diretto (è WWOX) · **Novelty**: nuovo come biomarcatore di *stato funzionale WWOX* paziente-specifico generato da pipeline strutturale · **Rilevanza di malattia**: criterio 1+3 · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-005 — Convergenza biallelica sul dominio SDR/ossidoreduttasi: l'asse metabolico (P5) è meccanicisticamente centrale per il genotipo di riferimento *in particolare*|DL-MECH-005]] (stesso dominio SDR), [[discovery_ledger_current#DL-BIO-002 — Trascritto/proteina dell'allele di sito accettore, nominati dalla predizione di skipping esone 9 (SpliceAI/Pangolin)|DL-BIO-002]] (allele di sito accettore)

### DL-BIO-002 — Trascritto/proteina dell'allele di sito accettore, nominati dalla predizione di skipping esone 9 (SpliceAI/Pangolin)
- **Status**: in-silico done (wet open) · **Tag**: IPOTESI · **Cosa si misura**: trascritto WWOX dell'allele di sito accettore (RT-PCR/RNA-seq su fibroblasti, eventualmente + inibitore NMD) + proteina risultante · **Matrice**: fibroblasti/LCL donor-derived · **Vicinanza**: massima (WWOX) → **Tier 1/2**
- **Fonte**: il record pubblico di variante ("eliminazione esone 9 altamente probabile") × predittori di splicing — **ESEGUITO 2026-07-04** (Ensembl VEP GRCh38 + SpliceAI + MaxEntScan, chr16:79211606 A>G; vedi *inbox entry INBOX-005 (private quarantine log)*): **SpliceAI acceptor-loss DS_AL 0.96** (a −2 nt, high-confidence) + **acceptor-gain criptico DS_AG 0.64** (a +8 nt); **MaxEntScan 7.28→-0.67 (Δ-7.95)**; consequence = splice_acceptor_variant. ClinVar = VUS.
- **Mappa ABC**: A=WWOX-LoF · B=alterazione sito accettore introne 8 → skipping esone 9 predetto · C=readout = trascritto aberrante/NMD misurabile
- **Statement causale**: `c.1057-2A>G —disrupts→ exon9_acceptor`; (predetto) `→ exon9_skipping`; (predetto) `→ frameshift/PTC → NMD or truncated_protein` · **Belief**: **ALTO sul disrupt dell'accettore** (SpliceAI DS_AL 0.96 + MaxEntScan Δ-7.95, 2 metodi ortogonali); **medio sull'esito** = splicing aberrante verso frameshift/PTC (skipping esone 9 e/o sito criptico +8, DS_AG 0.64) → NMD/tronco. Resta in-silico; DATO = RT-PCR wet
- **Catena di ragionamento**: AlphaFold qui **non serve** (è splicing, non missenso) → la lente giusta è SpliceAI/Pangolin (vedi euristica H-003). Se l'esone 9 (anch'esso parte della regione SDR) viene saltato, l'allele di sito accettore è verosimilmente null funzionale (NMD) o tronco. Il readout wet — RT-PCR allele-specifica ± blocco NMD — *misura davvero* cosa produce quell'allele, dato non deducibile in silico.
- **Evidenza**: supporta=sito accettore canonico ±2 (alta probabilità di disruption), gnomAD MAF 0, ClinVar · refuta=l'esito (skipping vs intron retention vs sito criptico) non è prevedibile con certezza, come dice il referto stesso · neutrale=nessun dato RNA donor-derived
- **Esperimento proposto**: SpliceAI/Pangolin score → poi RT-PCR su RNA fibroblasti donor-derived ± emetina/cicloeximide (NMD). Readout: banda di skipping esone 9 / riduzione del trascritto dell'allele di sito accettore. **Fattibile per il genotipo di riferimento.**
- **Razionale di trasferimento**: diretto · **Novelty**: nuovo · **Rilevanza di malattia**: criterio 1+3 · **Interconnessioni**: [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]] (insieme = stato biallelico), [[discovery_ledger_current#DL-MECH-005 — Convergenza biallelica sul dominio SDR/ossidoreduttasi: l'asse metabolico (P5) è meccanicisticamente centrale per il genotipo di riferimento *in particolare*|DL-MECH-005]]

### DL-BIO-010 — ERG scotopico (ampiezza onda-b + implicit time) come endpoint funzionale traslabile — con un caveat che ne cambia l'interpretazione

- **Status:** `open-lead` · **Tag:** ESPANSIONE — seme di endpoint, non biomarcatore WWOX
- **Fonte:** Saadane et al. 2021, PMID 34214506, Figura 8 (letta da immagine).
- **DATO:** 2 mesi di diabete riducono l'onda-b scotopica e allungano l'implicit time; la delezione di `Capn1` previene entrambi (n = 10–14 occhi).
- **🔴 Il dettaglio che gli autori non commentano:** l'**onda-a — la componente generata dai fotorecettori — è invariata**. Solo l'onda-b, post-fotorecettoriale, si muove. La tesi del lavoro è una patologia guidata dai fotorecettori; la sua elettrofisiologia colloca il deficit a valle. Un endpoint ERG **deve specificare quale componente**, o misura un'altra cosa.
- **Perché conta:** l'ERG è non invasivo, standardizzato, già usato nell'uomo, e i disturbi WWOX-correlati hanno coinvolgimento visivo. È Tier 3 (endpoint clinico distale), **non** un biomarcatore gene-linked: non misura WWOX.
- **Belief:** medio sull'osservazione; nullo su qualunque validità in un contesto WWOX, mai testata.
- **REVIVAL_TRIGGER:** ERG in un modello WWOX-deficiente con separazione onda-a/onda-b; o dati ERG in coorte umana WWOX.
- **Interconnessioni:** [[discovery_ledger_current#DL-MECH-061 — Ca²⁺→calpaina come regolatore dell'ABBONDANZA di WWOX in un neurone eccitabile (NON come via di degradazione)|DL-MECH-061]].

**Riflessione di processo:** un endpoint che «funziona» va letto sulla componente giusta. Qui la rescue è reale e il bersaglio dichiarato è sbagliato: adottarlo senza leggere la Figura 8 avrebbe importato l'errore.

## MOL — lead molecola / terapia

### DL-MOL-001 — Antagonismo NMDAR come leva di rescue del bursting da WWOX-loss
- **Status**: **maturing** (salito da open dopo assembly 2026-06-28: convergenza GRIN2A + piattaforma organoidi pronta) · **Tag**: IPOTESI · **Composto/target**: NMDAR (target) — candidato approvato: **memantina**; tool: MK-801/APV · **Pathway toccato**: network-state hyperexcitability (cross-pathway)
- **Fonte**: il *contrasto* tra Riccardi 2026 (PMID 42190144, abstract) e il CLAIM Breton 2021 già a registro
- **Mappa ABC**: A=WWOX-loss/rete iper-eccitabile del genotipo di riferimento · B=bursting spontaneo NMDAR-dipendente (Breton) · C=antagonista NMDAR
- **Statement causale**: `WWOX(loss) —produces→ bursting_neocorticale`; `bursting —depends_on→ NMDAR_activity`; (inferito) `NMDAR_antagonist —decreases→ bursting` · **Belief**: **medio-alto** (alzato in assembly: Breton modello + GRIN2A human-genetics + piattaforma organoidi che rende il test fattibile = 3 fonti convergenti indipendenti)
- **Catena di ragionamento**: Breton mostra che il bursting da Wwox-loss *dipende da NMDAR e gap junction* (CLAIM a registro, fonte papers 210) → se la dipendenza è causale, bloccare NMDAR dovrebbe ridurre il bursting. Riccardi non studia WWOX a questo livello, ma colloca **GRIN2A** (subunità NMDAR) tra i geni che causano lo stesso fenotipo burst-suppression → corroborazione genetica umana del nodo NMDAR (vedi MECH-002). Tag IPOTESI perché mai testato in modello WWOX né nel genotipo di riferimento.
- **Evidenza**: supporta=dipendenza NMDAR dimostrata (Breton) + GRIN2A nel cohort BS (Riccardi) · refuta=la memantina nei DEE pediatrici ha efficacia modesta e finestra ristretta; NMDAR-block cronico ha rischi sul neurosviluppo · neutrale=manca qualunque dato in modello WWOX
- **Esperimento proposto**: in neuroni/organoidi WWOX-null (modello Breton/Repudi) misurare se memantina o MK-801 riducono frequenza/ampiezza del bursting spontaneo (MEA) e il phase-amplitude coupling. Readout atteso: ↓ bursting dose-dipendente. Fattibile per il genotipo di riferimento solo come razionale, non come intervento.
- **Razionale di trasferimento a WWOX**: alto a livello meccanicistico (stesso fenotipo, stessa dipendenza), basso a livello clinico finché non validato · **Novelty**: nuovo come *lead terapeutico WWOX-specifico* (la dipendenza NMDAR è nota; l'inferenza repurposing no) · **Rilevanza di malattia**: criterio 2+3 · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-002 — GRIN2A nel cohort BS: corroborazione human-genetics del nodo NMDAR|DL-MECH-002]] (rafforza), [[discovery_ledger_current#DL-MOL-002 — Modulazione gap-junction (connexine) come co-leva del bursting|DL-MOL-002]] (co-meccanismo)

### DL-MOL-002 — Modulazione gap-junction (connexine) come co-leva del bursting
- **Status**: open · **Tag**: ESPANSIONE · **Composto/target**: gap junction / connexine — candidati: carbenoxolone, chinina, mefloquina · **Pathway**: network-state
- **Fonte**: CLAIM Breton 2021 (gap-junction-dipendenza); Riccardi non lo tocca
- **Mappa ABC**: A=WWOX-loss · B=bursting gap-junction-dipendente · C=gap-junction blocker
- **Statement causale**: `bursting —depends_on→ gap_junction`; (inferito) `gap_junction_blocker —decreases→ bursting` · **Belief**: basso
- **Catena di ragionamento**: stessa logica di MOL-001 sul secondo meccanismo dichiarato da Breton. Tag ESPANSIONE perché i gap-junction blocker disponibili sono poco specifici e con scarsa tollerabilità CNS pediatrica → leva concettuale più che clinica.
- **Evidenza**: supporta=gap-junction-dipendenza (Breton) · refuta=nessun gap-junction blocker sicuro/selettivo per uso cronico pediatrico · neutrale=nessun dato WWOX diretto
- **Esperimento proposto**: stesso assay MEA su WWOX-null + carbenoxolone (controllo meccanicistico, non traslazionale). Readout: ↓ sincronia/bursting.
- **Novelty**: nuovo come lead WWOX · **Rilevanza di malattia**: criterio 2 · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-001 — Antagonismo NMDAR come leva di rescue del bursting da WWOX-loss|DL-MOL-001]]

### DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo
- **Status**: open · **Tag**: IPOTESI · **Composto/target**: via Wnt/β-catenin — candidato (verso corretto) = **inibitore Wnt** (tankyrase-i es. XAV939; o restauro funzione WWOX). ❌ **NON litio/GSK3β-i** (spingerebbe nel verso sbagliato) · **Pathway**: Wnt / struttura prenatale (P3/P4)
- **Fonte**: Repudi & Aqeilan 2021 (PMID 34268881, organoidi WOREE: difetto Wnt) **+ direzione fissata da** Bouteille 2009 (PMID 19465938, DOI 10.1038/onc.2009.120), Li 2012 (PMID 23030478, DOI 10.1111/j.1600-0463.2012.02947.x), Celebi 2020 (PMID 32368285, DOI 10.7150/jca.40840)
- **Mappa ABC**: A=WWOX-loss del genotipo di riferimento · B=**iper-attivazione Wnt/β-catenin** (WWOX normalmente sequestra DVL2 nel citoplasma → senza WWOX, DVL/β-catenin entrano nel nucleo) · C=inibitore Wnt
- **Statement causale**: `WWOX —sequesters→ DVL2_cytoplasm —inhibits→ Wnt/βcat`; quindi `WWOX(loss) —activates→ Wnt/βcat`; (inferito) `Wnt_inhibitor —may_correct→ iperattivazione` · **Belief**: medio (direzione multi-fonte DATO **ma in contesto cancro**; da confermare nel neurone in sviluppo)
- **Catena di ragionamento**: ribaltamento prezioso — avevo nominato il litio (GSK3β-i), ma il litio **stabilizza β-catenin → attiva Wnt**, cioè peggiorerebbe un'iper-attivazione. Tre studi indipendenti danno la direzione: WWOX inibisce Wnt via sequestro di DVL2; la sua perdita iper-attiva. Il gate-direzione (regola C) ha evitato un candidato dannoso. **Resta IPOTESI** per un ⚠️ conflitto di contesto: l'iper-attivazione è dimostrata nel cancro; nel neurone in sviluppo il Wnt ha ruoli timing-dipendenti e l'abstract organoidi dice solo "impairment" senza verso → da verificare (NS-012 done parz., serve full text organoidi).
- **Evidenza**: supporta=meccanismo DVL2-sequestro + iper-attivazione multi-fonte (Bouteille/Li/Celebi) · refuta=tutto in contesto oncologico, non neurodevelopmentale; finestra prenatale; inibitori Wnt sistemici tossici (turnover intestinale/osseo) · neutrale=verso nel neurone non confermato
- **Esperimento proposto**: negli organoidi WOREE (MECH-007) misurare prima lo **stato di β-catenin nucleare** (è iper o ipo-attivo?), poi testare un inibitore Wnt (XAV939) vs CHIR99021 sul rescue del layering corticale. Determina il verso nel contesto giusto.
- **Razionale di trasferimento**: medio · **Novelty**: nuovo; il ribaltamento litio→inibitore è il valore · **Rilevanza di malattia**: criterio 1 (evita un intervento dannoso) +2 · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento|DL-MECH-008]] (la funzione Wnt è WW-scaffold → rilevanza variante SDR del genotipo di riferimento), [[discovery_ledger_current#DL-MECH-007 — Piattaforma organoidi WOREE da iPSC paziente + rescue con WWOX ectopico (abilita gli esperimenti del ledger)|DL-MECH-007]], meta_prenatal_structure

### DL-MOL-004 — Upregolazione del WWOX endogeno residuo (dCas9-CRISPRa / piccola-molecola agonista) per lo stato ipomorfo Q230P
- **Status**: open · **Tag**: IPOTESI · **Composto/target**: locus/proteina WWOX — strumenti: **dCas9-VPR/CRISPRa** sul promotore WWOX; small-molecule **WWOX-agonist** (toosendanin/TSN come tool, non clinico) · **Pathway**: a monte di tutti (ripristina WWOX stesso)
- **Fonte**: nota working model (dCas9/CRISPRa per stati ipomorfi) + Repudi/Aqeilan 2021 (rescue con WWOX ectopico = proof-of-concept) + Yang 2021 (PMID 34015398, DOI 10.1016/j.canlet.2021.05.010 — TSN attiva WWOX)
- **Mappa ABC**: A=WWOX-LoF parziale del genotipo di riferimento · B=presenza di un allele Q230P potenzialmente *ipomorfo* (funzione residua se un po' di proteina sopravvive) · C=alzare la dose di WWOX funzionale (CRISPRa) o stabilizzarne/attivarne il residuo
- **Statement causale**: `ectopic/▲WWOX —rescues→ WOREE_phenotype` (DATO organoidi); (inferito) `CRISPRa(WWOX) —may_raise→ residual_functional_WWOX` · **Belief**: medio (il rescue da WWOX è DATO; la fattibilità CRISPRa in vivo nel SNC è la parte ipotetica)
- **Catena di ragionamento**: a differenza di un null/null, Q230P **potrebbe** lasciare una frazione di proteina funzionale (working model: "possibile funzione residua parziale") → uno stato ipomorfo è il bersaglio ideale per **alzare l'output** del locus, strategia diversa dalla gene-replacement (utile se invece la proteina è del tutto assente). Quale delle due dipende di nuovo da BIO-001 (quanta proteina residua). ⚠️ TSN è un tool di ricerca oncologico, non un farmaco pediatrico: serve solo a provare che WWOX è "drogabile" verso l'alto.
- **Evidenza**: supporta=rescue ectopico DATO (organoidi) + esistenza di un attivatore di WWOX (TSN) = WWOX è up-modulabile · refuta=delivery CRISPRa al SNC immaturo non risolto; se Q230P→proteina assente, non c'è nulla da upregolare (serve replacement) · neutrale=funzione residua di Q230P non quantificata
- **Esperimento proposto**: in fibroblasti/iPSC donor-derived, CRISPRa sul promotore WWOX → misurare se sale proteina funzionale (lega a BIO-001); negli organoidi, rescue fenotipico. Readout: ↑ proteina WWOX stabile + normalizzazione marker.
- **Razionale di trasferimento**: alto come *strategia* (ripristina la causa, non un effetto a valle) · **Novelty**: nuovo come lead esplicito; collega gene-therapy (meta 7 pending) allo stato ipomorfo del genotipo di riferimento · **Rilevanza di malattia**: criterio 1 · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-007 — Piattaforma organoidi WOREE da iPSC paziente + rescue con WWOX ectopico (abilita gli esperimenti del ledger)|DL-MECH-007]], [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]] (decide replacement vs upregulation), [[discovery_ledger_current#DL-MOL-005 — Gene REPLACEMENT AAV9-hSynI-hWWOX-WPRE (ICV, neuron-specific): rescue dose-dipendente e durevole (P300) — genotype-agnostic → NON dipende dagli alleli SDR del genotipo di riferimento|DL-MOL-005]] (strategia alternativa: replacement vs upregulation)

### DL-MOL-005 — Gene REPLACEMENT AAV9-hSynI-hWWOX-WPRE (ICV, neuron-specific): rescue dose-dipendente e durevole (P300) — genotype-agnostic → NON dipende dagli alleli SDR del genotipo di riferimento
- **Status**: **maturing** · **Tag**: DATO (efficacia nel modello murino Wwox-null) + INFERENZA (traslazione al genotipo di riferimento) · **Composto/target**: AAV9 con hWWOX cDNA sotto promotore neuronale **human Synapsin-I** + elemento **WPRE**; via ICV · **Pathway**: a monte di tutti (ripristina WWOX full-length)
- **Fonte**: **Obeid, Aqeilan et al. 2026, OMTA (Mol Ther Methods Clin Dev) vol 34** — supplemental S1–S8 (allegato) + main; predecessore proof-of-concept Repudi & Aqeilan 2021, EMBO Mol Med (PMID 34747138, [DOI](https://doi.org/10.15252/emmm.202114599)). Già a registro come [[paper_registry_current#PAPER 011]] + [[claim_registry_current#CLAIM 011]]
- **Mappa ABC**: A=WWOX-LoF del genotipo di riferimento · B=assenza di proteina WWOX funzionale nei neuroni · C=**consegna esogena di WWOX full-length** (bypassa completamente le due varianti SDR del genotipo di riferimento)
- **Statement causale**: `AAV9-SynI-hWWOX-WPRE —restores→ neuronal_WWOX_protein` (DATO, WB dose-dip. S3/S5); `neuronal_WWOX —rescues→ survival + seizures + myelination + gliosis + glucose + ataxia + fertility` (DATO S2/S4/S7/S8); `rescue —is→ dose-dependent (HD 2.63e11 > LD 1.23e11) & durable (fino a P300)` (DATO S4/S5) · **Belief**: **alto** per efficacia nel null murino (organoidi + in vivo + dose + durata + finestra = convergenza multi-livello); **medio** per il genotipo di riferimento (caveat sotto)
- **Catena di ragionamento**: il punto-scoperta chiave per il genotipo di riferimento è che la **gene replacement è genotype-agnostic** — consegna una copia sana di WWOX, quindi **non le importa** che il genotipo di riferimento porti Q230P + skipping esone 9 sul dominio SDR. Questo la **disaccoppia** dai readout variante-specifici (a differenza di MOL-004/CRISPRa e di un eventuale chaperone, che richiedono proteina residua da upregolare/stabilizzare → dipendono da BIO-001). È la ragione per cui il replacement è robusto *a prescindere* dallo stato ipomorfo. Il rescue neuron-specifico (SynI) di fenotipi **non-cell-autonomous** (mielina, gliosi) e **sistemici** (glucosio) mostra che il compartimento neuronale è il driver a monte (vedi MECH-010).
- **Evidenza**: **supporta**=rescue multi-dominio, dose-dip., durevole a P300, replicato mWwox≈hWWOX, neuron-specific senza espressione epatica (S6); proof-of-concept 2021 indipendente; convergenza con rescue ectopico organoidi (MECH-007) · **refuta/caveat**=(1) modello = **null completo**, il genotipo di riferimento è LoF biallelica potenzialmente ipomorfa → fenotipo/finestra diversi; (2) trattamento murino **neonatale P0–P5** (≈ perinatale umano): efficacia su bambino **già sintomatico e più grande NON dimostrata** (vedi MECH-011); (3) segnale di **tossicità dose-limitante DRG/gangli periferici** ad alta dose sistemica (flag regolatorio pediatrico, nota review PAPER 2026); (4) espressione anche in PNS/midollo (S6) — biodistribuzione da sorvegliare · **neutrale**=via di somministrazione ottimale per l'uomo (ICV vs IT vs IV) non fissata
- **Esperimento proposto**: (per il genotipo di riferimento) il dato traslazionale mancante è l'efficacia del trattamento **post-onset in animale più maturo** e in un modello **ipomorfo** (non null) — chiedere al gruppo Aqeilan se esiste; readout: rescue SWD/ECoG + mielina in trattamento ritardato. Piattaforma pronta: organoidi WOREE da iPSC donor-derived (MECH-007) per testare il replacement sul *suo* fondo genetico.
- **Razionale di trasferimento**: **il più alto del ledger a livello di strategia** (ripristina la causa, non un effetto) · **Novelty**: corrobora/matura CLAIM 011 esistente + aggiunge i design-principle quantitativi dai supplementari (dose, WPRE, promotore, finestra) · **Rilevanza di malattia**: criterio 1 (massima) · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-004 — Upregolazione del WWOX endogeno residuo (dCas9-CRISPRa / piccola-molecola agonista) per lo stato ipomorfo Q230P|DL-MOL-004]] (replacement vs upregulation), [[discovery_ledger_current#DL-MECH-007 — Piattaforma organoidi WOREE da iPSC paziente + rescue con WWOX ectopico (abilita gli esperimenti del ledger)|DL-MECH-007]] (proof-of-concept organoidi), [[discovery_ledger_current#DL-MECH-009 — L'elemento WPRE è un *booster di espressione dose-sparing* (3–16.7× per regione), non un "elemento da rimuovere": tensione di design vs rischio overexpression|DL-MECH-009]] (WPRE), [[discovery_ledger_current#DL-MECH-010 — WWOX *neuronale* (SynI) è SUFFICIENTE a riscattare fenotipi non-cell-autonomous (mielina, gliosi) e sistemici (glucosio) → il compartimento neuronale è il driver a monte; il promotore oligodendrocitario (MBP) è meno efficace|DL-MECH-010]] (neuron-specific driver), [[discovery_ledger_current#DL-MECH-011 — Finestra terapeutica P1–P5 nel topo: efficace se precoce → il gap traslazionale critico per il genotipo di riferimento è l'efficacia del trattamento *post-onset / età più avanzata*|DL-MECH-011]] (finestra), [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]] (biomarcatore di target engagement)

## REPO — drug repurposing

### DL-REPO-001 — Na-channel blockers: leva per le channelopatie BS, NON per WWOX (differenziale terapeutico)
- **Status**: maturing · **Tag**: INFERENZA · **Farmaco**: carbamazepina/fenitoina/oxcarbazepina (Na-channel blockers) · **Indicazione approvata**: epilessia · **Target/pathway**: Nav (KCNQ2-GoF, SCN2A)
- **Fonte**: Riccardi 2026 (PMID 42190144, abstract) — "early use of sodium channel blockers in selected cases"
- **Mappa ABC**: A=burst-suppression DEE · B=channelopatia Nav/K (KCNQ2/SCN2A) · C=Na-channel blocker — **ma per WWOX il nodo B è diverso (NMDAR/gap-junction), quindi C non trasferisce**
- **Statement causale**: `KCNQ2-GoF/SCN2A —causes→ BS`; `Na_channel_blocker —improves→ KCNQ2/SCN2A_BS`; (differenziale) `WWOX-BS —NOT_driven_by→ Nav` → leva diversa · **Belief**: medio-alto (per il differenziale)
- **Catena di ragionamento**: il valore-scoperta qui è **negativo e prezioso**: Riccardi mostra che la precision therapy della BS è gene-dipendente e che i Na-blocker servono alle channelopatie. Incrociato con Breton (WWOX-BS = NMDAR/gap-junction), questo *esclude* i Na-blocker come razionale meccanicistico per WWOX e *punta il faro* su NMDAR (MOL-001). Evita un vicolo cieco terapeutico.
- **Esperimento proposto**: nessuno nuovo — è un razionale di esclusione. Verifica documentale: nei casi WWOX-BS riportati, i Na-blocker hanno fallito? (richiede full text Riccardi + serie WOREE).
- **Ponte verso WWOX**: per differenza, non per analogia · **Novelty**: corrobora/raffina la lettura network-state esistente · **Rilevanza di malattia**: criterio 1 (evita terapia inefficace per il suo meccanismo) · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-001 — Antagonismo NMDAR come leva di rescue del bursting da WWOX-loss|DL-MOL-001]] (per contrasto)

### DL-REPO-002 — Farmaco anti-neuroinfiammatorio riposizionato come leva per la LoF di WWOX (asse Aldaz): direzione RISOLTA (WWOX-loss → infiammazione ↑ → serve INIBIRE)
- **Status**: open · **Tag**: IPOTESI · **Farmaco**: *da identificare* (candidato proposto da C.M. Aldaz per test in topi Wwox; riposizionato da un clinico "Zhang"/Baylor su altra patologia, trial avanzato — **non nel record pubblico**) · **Classe inferita**: soppressore di neuroinfiammazione/microgliosi (IL-1β/NLRP3, o MAPK/NF-κB, o microglia-targeting) · **Pathway**: neuroinfiammazione (meta 6 pending)
- **Fonte**: memoria operatore — grant WWOX Foundation ~25.000 USD, Aldaz (MD Anderson) + clinico Baylor. Ancora meccanicistica pubblicata: [[discovery_ledger_current#DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)|DL-MECH-012]] (Aldaz: WWOX-loss de-reprime segnale infiammatorio). *Nome farmaco e trial NON verificati in letteratura al 2026-07-03.*
- **Mappa ABC**: A=WWOX-LoF · B=**de-repressione dell'infiammazione** (microgliosi/astrogliosi, cascata citochinica) documentata da Aldaz · C=farmaco approvato che spegne quel nodo
- **Statement causale**: `WWOX(loss) —de-represses→ neuroinflammation` (DATO Aldaz, multi-tessuto); (inferito) `anti-inflammatory_drug —decreases→ neuroinflammation → può rallentare degenerazione` · **Belief**: basso-medio (direzione solida; farmaco specifico ignoto; effetto su fenotipo WWOX non testato)
- **Catena di ragionamento**: la **direzione è risolta** e supera il gate REPO — a differenza dell'asse Wnt, qui WWOX-loss *aumenta* l'infiammazione in ≥3 modelli Aldaz (SCAR12 cervelletto, sepsi, polmone), quindi la leva corretta è **sopprimere**, non stimolare → un anti-infiammatorio approvato è direzionalmente sensato. Ciò che manca è (a) il nome del farmaco di Aldaz/Zhang, (b) la prova che agisca sul fenotipo WWOX. ⚠️ Caveat forte: l'anti-infiammatorio agirebbe su un **effetto a valle** (l'infiammazione), non sulla causa (WWOX assente) → beneficio atteso *sintomatico/rallentante*, non curativo; complementare, non alternativo, alla gene therapy (MOL-005).
- **Evidenza**: supporta=asse neuroinfiammazione WWOX robusto e multi-tessuto (Aldaz); direzione univoca; un anti-infiammatorio approvato abbatte la barriera traslazionale (vale doppio per un bambino) · refuta=target a valle (non corregge WWOX); molti anti-neuroinfiammatori hanno fallito in malattie neurodegenerative; specificità/penetranza CNS pediatrica da verificare · neutrale=nessun dato del farmaco-X su modello WWOX
- **Esperimento proposto**: nei topi **Wwox^P47T** (modello Aldaz già esistente e caratterizzato) misurare se il farmaco-X riduce astro-microgliosi (GFAP/Iba1), rallenta la perdita di Purkinje e migliora coordinazione motoria/atassia. Readout atteso: ↓ marcatori infiammatori + ↓ progressione. **Piattaforma pronta** (è il modello del paper 2023).
- **Ponte verso WWOX**: diretto sull'asse infiammatorio del genotipo di riferimento *se* la proteina è globalmente assente (vedi [[discovery_ledger_current#DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento|DL-MECH-008]]) · **Rilevanza di malattia**: criterio 2+3 (asse disregolato + potenziale monitoraggio GFAP/citochine) · **Novelty**: nuovo lead REPO WWOX-specifico · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)|DL-MECH-012]] (ancora meccanicistica), [[discovery_ledger_current#DL-MOL-005 — Gene REPLACEMENT AAV9-hSynI-hWWOX-WPRE (ICV, neuron-specific): rescue dose-dipendente e durevole (P300) — genotype-agnostic → NON dipende dagli alleli SDR del genotipo di riferimento|DL-MOL-005]] (complementare alla gene therapy), [[discovery_ledger_current#DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento|DL-MECH-008]]

## MECH — indizi meccanicistici (aghi nel pagliaio)

### DL-MECH-001 — WWOX confermato tra le cause di EIDEE con burst-suppression (cohort grande)
- **Status**: maturing · **Tag**: DATO (provisional, abstract-only) · **Fonte**: Riccardi 2026, PMID 42190144, DOI 10.1212/WNL.0000000000218013 — WWOX tra le "novel associations" in 110 pz BS, MRI-negativi
- **L'indizio**: in un cohort BS ampio e sistematico, WWOX è causa *rara* (novel association, non tra i geni top) → WWOX-BS è all'estremo severo e poco frequente dello spettro BS.
- **Mappa ABC** (n/a diretto) · **Statement causale**: `WWOX(LoF) —causes→ EIDEE_burst_suppression` · **Belief**: medio (abstract-only; serve full text per dettagli del/i caso/i WWOX)
- **Catena di ragionamento**: il dato è dichiarato direttamente (DATO) ma l'estrazione è da abstract → provisional. Corrobora Sapuppo (EEG>imaging precoce) e Breton (network-state). Non è di per sé un lead nuovo: è l'**ancora di contesto** che dà peso a MOL-001/REPO-001.
- **Perché potrebbe contare**: serve come anchor cohort per quantificare quanto WWOX-BS sia distinguibile dalle channelopatie (→ MECH-003) · **Possibile passo successivo**: full text per timing/morfologia BS WWOX-specifici e risposta ai farmaci · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-002 — GRIN2A nel cohort BS: corroborazione human-genetics del nodo NMDAR|DL-MECH-002]], [[discovery_ledger_current#DL-MECH-003 — Firma qEEG burst-suppression WWOX-specifica come endpoint clinico monitorabile (Tier 3)|DL-MECH-003]]

### DL-MECH-002 — GRIN2A nel cohort BS: corroborazione human-genetics del nodo NMDAR
- **Status**: maturing · **Tag**: INFERENZA · **Fonte**: Riccardi 2026 (GRIN2A tra novel associations) + CLAIM Breton 2021
- **L'indizio**: GRIN2A (subunità NMDAR) causa lo stesso fenotipo burst-suppression. Un'alterazione *diretta* dell'NMDAR produce BS → l'NMDAR è un nodo convergente sufficiente a generare BS.
- **Mappa ABC**: A=BS-DEE · B=NMDAR (GRIN2A) · C=farmacologia NMDAR · **Statement causale**: `GRIN2A(var) —causes→ BS`; `WWOX-bursting —depends_on→ NMDAR` → `NMDAR` è nodo condiviso · **Belief**: medio
- **Catena di ragionamento**: due strade indipendenti convergono sull'NMDAR — genetica umana (GRIN2A→BS, Riccardi) e modello WWOX (bursting NMDAR-dipendente, Breton). La convergenza alza la fiducia che modulare l'NMDAR sia rilevante anche nel contesto WWOX → **sale a INFERENZA** e rafforza MOL-001.
- **Perché conta**: è il ponte che trasforma MOL-001 da IPOTESI isolata a ipotesi sostenuta da convergenza · **Possibile passo successivo**: confronto morfologia/farmacoresponse tra BS-GRIN2A e BS-WWOX (full text) · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-001 — Antagonismo NMDAR come leva di rescue del bursting da WWOX-loss|DL-MOL-001]] (rafforza), [[discovery_ledger_current#DL-MECH-001 — WWOX confermato tra le cause di EIDEE con burst-suppression (cohort grande)|DL-MECH-001]]

### DL-MECH-003 — Firma qEEG burst-suppression WWOX-specifica come endpoint clinico monitorabile (Tier 3)
- **Status**: open · **Tag**: IPOTESI · **Fonte**: Riccardi 2026 — "BS timing e morfologia anticipano il genotipo"
- **L'indizio**: se la BS (timing onset, durata burst vs suppression) è genotipo-predittiva, potrebbe esistere una **firma BS WWOX-specifica**. ⚠️ Disciplina dura LEGEND: EEG/qEEG = **Tier 3**, NON entra nel biomarker file → va in `clinical_monitoring_endpoints_current.md`. Non è un readout di stato funzionale di WWOX; è un endpoint di rete distale.
- **Statement causale**: `WWOX-LoF —produces→ BS_pattern_X (timing/morfologia)` · **Belief**: basso (firma WWOX-specifica non estraibile dall'abstract)
- **Perché potrebbe contare**: un endpoint EEG WWOX-specifico, se esistesse, sarebbe un *outcome measure* monitorabile e non invasivo per qualunque futura terapia di rete nel genotipo di riferimento (es. la leva NMDAR di MOL-001) · **Possibile passo successivo**: full text Riccardi per i parametri BS del/i caso/i WWOX; confronto con l'EEG del genotipo di riferimento · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-001 — WWOX confermato tra le cause di EIDEE con burst-suppression (cohort grande)|DL-MECH-001]]

### DL-MECH-004 — Convergenza "macchinario di rilascio sinaptico" (STXBP1/SNAP25/SYT1) verso BS
- **Status**: open · **Tag**: ESPANSIONE · **Fonte**: Riccardi 2026 (STXBP1 n=16; SNAP25/SYT1 candidati)
- **L'indizio**: una grossa fetta dei geni BS è macchinario di esocitosi (SNARE/vescicole). Domanda aperta: WWOX ha un link col rilascio sinaptico/SNARE? Se sì, sarebbe un secondo asse meccanicistico oltre a NMDAR.
- **Statement causale**: `exocytosis_machinery(LoF) —causes→ BS` · `WWOX —?→ exocytosis` (ignoto) · **Belief**: basso
- **Perché potrebbe contare**: potenziale nuovo asse, ma puramente esplorativo · **Possibile passo successivo**: next-search interattoma WWOX vs SNARE/SYT1 · **Interconnessioni**: —

### DL-MECH-005 — Convergenza biallelica sul dominio SDR/ossidoreduttasi: l'asse metabolico (P5) è meccanicisticamente centrale per il genotipo di riferimento *in particolare*
- **Status**: maturing · **Tag**: INFERENZA · **Fonte**: il record pubblico di variante (mappatura posizionale delle due varianti sui dominî WWOX)
- **L'indizio**: **entrambi** gli alleli del genotipo di riferimento colpiscono il **dominio enzimatico SDR**, non i dominî WW (interazione proteica): Q230P (esone 7) è interno alla regione SDR; lo skipping dell'esone 9 (allele di sito accettore) cade nella stessa porzione catalitica. → l'attività **ossidoreduttasica** di WWOX è il bersaglio convergente delle due varianti.
- **Mappa ABC**: A=genotipo del genotipo di riferimento · B=perdita selettiva attività SDR (vs dominî WW potenzialmente meno colpiti) · C=pathway metabolico/sfingolipidico (P5) · **Statement causale**: `Q230P + exon9-skip —both_hit→ WWOX_SDR_domain`; `SDR_loss —disrupts→ oxidoreductase/lipid_metabolism (P5)` · **Belief**: medio (posizione certa; impatto funzionale differenziale enzima-vs-scaffold da confermare). — Nota 2026-07-04 (INBOX-005): l'impatto dell'esone-9 sull'SDR ora ancorato a score di splicing (SpliceAI 0.96 acceptor-loss); rafforza la convergenza "due varianti → dominio catalitico SDR".
- **Catena di ragionamento**: WWOX ha 2 dominî WW (scaffold/PPI, N-term) + dominio SDR (catalitico, centrale). Se le due varianti del genotipo di riferimento risparmiano relativamente i WW e convergono sull'SDR, allora **per il genotipo di riferimento specificamente** la disfunzione enzimatica/metabolica potrebbe pesare più della perdita di scaffolding → alza la priorità della **meta_metabolism (P5)** e della meta sfingolipidi come asse paziente-rilevante. Questo è esattamente ciò che AF3 (mappa quali dominî restano integri) può aiutare a discriminare → MECH-006.
- **Perché conta**: orienta sia i biomarcatori (BIO-001/002 = readout enzimatico) sia la ricerca di molecole verso il pathway metabolico/redox · **Possibile passo successivo**: verificare nei current se P5 è già flaggato come asse dominante; cercare se Q230P o varianti SDR di WWOX in letteratura hanno fenotipo metabolico distinto · **Interconnessioni**: [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]], [[discovery_ledger_current#DL-BIO-002 — Trascritto/proteina dell'allele di sito accettore, nominati dalla predizione di skipping esone 9 (SpliceAI/Pangolin)|DL-BIO-002]], [[discovery_ledger_current#DL-MECH-006 — Dissociazione enzima-vs-scaffold via modellazione complessi AF3 (WWOX–ATM, WWOX–p53/ERBB4): quali funzioni WWOX restano?|DL-MECH-006]]

### DL-MECH-006 — Dissociazione enzima-vs-scaffold via modellazione complessi AF3 (WWOX–ATM, WWOX–p53/ERBB4): quali funzioni WWOX restano?
- **Status**: open · **Tag**: IPOTESI · **Fonte**: ragionamento strutturale AF3 × [[paper_registry_current#PAPER 030]] (interazione WWOX–ATM nella DDR) · *modello da eseguire*
- **L'indizio**: le interazioni proteina-proteina di WWOX (ATM nella DDR, p53, ERBB4) sono mediate dai dominî **WW**. Se Q230P (in SDR) destabilizza solo localmente senza collassare i WW, lo **scaffolding/PPI potrebbe essere parzialmente preservato** mentre l'**enzima è perso** → dissociazione funzionale. AF3-multimer (WWOX-WT vs WWOX-Q230P + partner) può predire se le interfacce WW reggono.
- **Mappa ABC**: A=WWOX-Q230P · B=stato delle interfacce WW vs sito SDR · C=funzioni preservate (DDR-scaffold?) vs perse (redox) → indirizza biomarcatori diversi · **Statement causale**: `Q230P(SDR) —may_spare→ WW_domain_PPI`; `→ DDR_scaffold partially_preserved?` · **Belief**: basso (ipotesi strutturale pura, da modellare)
- **Catena di ragionamento**: distinguere "WWOX assente" da "WWOX presente-ma-enzimaticamente-morto" cambia la strategia: nel secondo caso un **chaperone/stabilizzatore** (ponte verso AlphaProteo, ESPANSIONE) o un bypass metabolico avrebbero senso; nel primo no. AF3 dà l'IPOTESI strutturale che poi BIO-001 (attività) e un assay DDR (γH2AX dopo danno, in fibroblasti) verificherebbero wet.
- **Perché conta**: discrimina la classe di intervento (rescue enzimatico vs metabolico vs scaffold) e nomina un secondo biomarcatore (competenza DDR in fibroblasti) · **Possibile passo successivo**: AF3 WWOX-ATM WT vs Q230P; poi assay γH2AX/comet su fibroblasti donor-derived · **Interconnessioni**: [[discovery_ledger_current#DL-MECH-005 — Convergenza biallelica sul dominio SDR/ossidoreduttasi: l'asse metabolico (P5) è meccanicisticamente centrale per il genotipo di riferimento *in particolare*|DL-MECH-005]], [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]]

### DL-MECH-007 — Piattaforma organoidi WOREE da iPSC paziente + rescue con WWOX ectopico (abilita gli esperimenti del ledger)
- **Status**: maturing · **Tag**: DATO · **Fonte**: Repudi & Aqeilan, EMBO Mol Med 2021, PMID 34268881, DOI 10.15252/emmm.202013610
- **L'indizio**: esiste **già** un modello organoidi cerebrali WOREE (da hES CRISPR e da iPSC di pazienti) che riproduce difetti di popolazione neurale, differenziazione corticale, Wnt e DNA-damage-response; e l'**espressione ectopica di WWOX riscatta i fenotipi** (proof-of-concept che ripristinare WWOX funziona).
- **Mappa ABC**: A=WWOX-loss · B=piattaforma organoide come banco di prova · C=qualunque molecola/leva del ledger testabile qui · **Statement causale**: `ectopic_WWOX —rescues→ WOREE_organoid_phenotypes` (gene-therapy proof-of-concept) · **Belief**: alto (DATO sperimentale)
- **Catena di ragionamento**: questo non è un lead terapeutico in sé, è il **moltiplicatore**: rende *fattibili e già strumentati* gli esperimenti proposti in MOL-001 (NMDAR/MEA), MOL-003 (Wnt/CHIR), e la lettura enzima-vs-scaffold (il rescue con WWOX intero suggerisce che serve la **proteina full-length funzionale** → coerente con la convergenza SDR di MECH-005). Il rescue ectopico è anche l'ancora razionale per la traccia gene therapy (meta 7 pending).
- **Perché conta**: trasforma le ipotesi del ledger da "carta" a "testabili su una piattaforma esistente"; alza la priorità di contattare il gruppo Aqeilan · **Possibile passo successivo**: verificare se il modello ha già elettrofisiologia (MEA) per il test NMDAR; il rescue ectopico WWOX vale come bersaglio per la traccia gene-therapy · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-001 — Antagonismo NMDAR come leva di rescue del bursting da WWOX-loss|DL-MOL-001]], [[discovery_ledger_current#DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo|DL-MOL-003]], [[discovery_ledger_current#DL-MECH-005 — Convergenza biallelica sul dominio SDR/ossidoreduttasi: l'asse metabolico (P5) è meccanicisticamente centrale per il genotipo di riferimento *in particolare*|DL-MECH-005]], [[discovery_ledger_current#DL-MECH-006 — Dissociazione enzima-vs-scaffold via modellazione complessi AF3 (WWOX–ATM, WWOX–p53/ERBB4): quali funzioni WWOX restano?|DL-MECH-006]], [[discovery_ledger_current#DL-MOL-005 — Gene REPLACEMENT AAV9-hSynI-hWWOX-WPRE (ICV, neuron-specific): rescue dose-dipendente e durevole (P300) — genotype-agnostic → NON dipende dagli alleli SDR del genotipo di riferimento|DL-MOL-005]]
- **Aggiornamento belief 2026-07-03 (assembly)**: il principio "restore WWOX → rescue" è ora sostenuto da **3 livelli indipendenti convergenti** — organoidi (ectopico), in vivo neonatale (2021), in vivo dose-response + durevole P300 (Obeid 2026 OMTA). Belief conferma **alto**; il rescue ectopico organoidi diventa il banco di prova *paziente-specifico* per il replacement di MOL-005 sul fondo genetico del genotipo di riferimento.

### DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento
- **Status**: open · **Tag**: INFERENZA · **Fonte**: Bouteille 2009 (PMID 19465938) — l'interazione WWOX–DVL2 e l'inibizione di Wnt sono mediate dai **dominî WW** (PPI/scaffold), non dall'attività SDR
- **L'indizio**: se il controllo di Wnt passa dai dominî WW e la variante del genotipo di riferimento (Q230P) cade nel dominio **SDR** (catalitico), allora — *se la proteina restasse stabile* — la funzione anti-Wnt potrebbe essere **parzialmente preservata** nel genotipo di riferimento. Ma Q230P → proteina instabile/assente (dato analogico working model) → si perde *tutta* la proteina, WW inclusi. ⚠️ Quindi la rilevanza dell'asse Wnt per il genotipo di riferimento dipende dalla **quantità di proteina residua**, non solo dal dominio colpito.
- **Mappa ABC**: A=Q230P(SDR) · B=stato dominî WW vs stabilità proteica complessiva · C=quali funzioni (anti-Wnt scaffold vs redox enzima) il genotipo di riferimento perde davvero · **Statement causale**: `WWOX_WW —sequester→ DVL2 (Wnt-off)`; `Q230P(SDR) —destabilizes→ whole_protein → loses_WW_too?` · **Belief**: medio (logica di dominio solida; esito dipende dalla stabilità, da misurare)
- **Catena di ragionamento**: collega MECH-005/006 (enzima-vs-scaffold) all'asse Wnt (MOL-003): la domanda "il genotipo di riferimento perde anche il controllo Wnt?" si riduce a "quanta proteina Q230P sopravvive?" → di nuovo il readout di **stabilità proteica** (BIO-001) è il perno che discrimina. Se proteina ~assente → perde anche anti-Wnt → l'asse Wnt è rilevante per lei; se funzione residua parziale → meno.
- **Perché conta**: rende l'asse Wnt (MOL-003) *condizionato* a un dato misurabile sul genotipo di riferimento (proteina residua), invece che assunto · **Possibile passo successivo**: il Western di BIO-001 risponde anche a questa domanda · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo|DL-MOL-003]], [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]], [[discovery_ledger_current#DL-MECH-006 — Dissociazione enzima-vs-scaffold via modellazione complessi AF3 (WWOX–ATM, WWOX–p53/ERBB4): quali funzioni WWOX restano?|DL-MECH-006]]

### DL-MECH-009 — L'elemento WPRE è un *booster di espressione dose-sparing* (3–16.7× per regione), non un "elemento da rimuovere": tensione di design vs rischio overexpression
- **Status**: maturing · **Tag**: DATO (Western blot S3) · **Fonte**: Obeid/Aqeilan 2026 OMTA, **Fig S3** (allegato)
- **L'indizio**: la **rimozione del WPRE riduce** l'espressione di WWOX; la sua presenza la **aumenta** in modo netto e regione-dipendente — quantificazione WB relativa: cortex **3.0×**, ippocampo **3.0×**, mid-brain **5.5×**, **cerebellum 16.7×** (S3E). A parità di dose virale, +WPRE dà molta più proteina soprattutto nel cervelletto (regione critica per l'atassia/SCAR12).
- **Mappa ABC**: A=terapia genica WWOX · B=efficienza di traduzione del transgene · C=elemento WPRE nel cassette AAV · **Statement causale**: `WPRE —increases→ WWOX_protein_output (region-dependent, max cerebellum)`; (design) `+WPRE —enables→ dose-sparing (stesso rescue a dose virale minore)` · **Belief**: alto (dato WB diretto, multi-regione)
- **Catena di ragionamento**: ⚠️ **contraddizione da segnalare** — la review Obeid 2026 (Neurobiol Dis, [DOI](https://doi.org/10.1016/j.nbd.2026.107446), [[paper_registry_current#PAPER 029]]) sintetizza il design-principle come *"WPRE removed to avoid overexpression"*, mentre il **dato primario S3 mostra che WPRE serve ad alzare l'espressione** e la sua rimozione la abbatte. Non è un errore: sono le **due facce dello stesso trade-off** — WPRE massimizza l'output (bene per raggiungere soglia terapeutica a dose bassa = meno tossicità da capside) ma un output troppo alto (specie in cerebellum 16.7×) rischia overexpression → la scelta finale del cassette bilancia i due. A livello di malattia questo significa che la **dose efficace e la scelta ±WPRE sono accoppiate**, non indipendenti.
- **Perché conta**: è un parametro di design **direttamente rilevante** a qualunque futura terapia genica WWOX applicabile al genotipo di riferimento (dose minima efficace ↔ margine di sicurezza) · **Possibile passo successivo**: quale configurazione (dose × ±WPRE) è entrata nel first-in-human? (→ NS-016) · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-005 — Gene REPLACEMENT AAV9-hSynI-hWWOX-WPRE (ICV, neuron-specific): rescue dose-dipendente e durevole (P300) — genotype-agnostic → NON dipende dagli alleli SDR del genotipo di riferimento|DL-MOL-005]], [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]] (WWOX proteico = il readout che misura questo)

### DL-MECH-010 — WWOX *neuronale* (SynI) è SUFFICIENTE a riscattare fenotipi non-cell-autonomous (mielina, gliosi) e sistemici (glucosio) → il compartimento neuronale è il driver a monte; il promotore oligodendrocitario (MBP) è meno efficace
- **Status**: maturing · **Tag**: DATO · **Fonte**: Obeid/Aqeilan 2026 OMTA **Fig S1/S2** (confronto promotori: Ef1a/CMV/MBP/SynI/CBA) + **S7** (gliosi/mielina dose-dip.) + **S8** (rescue MBP/GFAP); coerente con Repudi 2021 (OPC non-cell-autonomous)
- **L'indizio**: espressione WWOX guidata dal promotore **neuronale SynI** ripristina la mielinizzazione (MBP↑), riduce astrogliosi (GFAP↓) e microgliosi (Iba1↓) e normalizza la **glicemia** — pur essendo la proteina *assente* in oligodendrociti (CC1) e fegato (S6). Il promotore **MBP (oligodendrocitario)** è meno efficace del SynI nonostante l'ipomielinizzazione sia il fenotipo gliale.
- **Mappa ABC**: A=WWOX-loss · B=**neurone** come nodo causale sovraordinato · C=leve neuron-dirette bastano per correggere anche difetti gliali/metabolici · **Statement causale**: `neuronal_WWOX(loss) —causes→ OPC_maturation_defect + astrogliosis + hypoglycemia (non-cell-autonomous)`; quindi `restore_neuronal_WWOX —corrects→ questi fenotipi a valle` · **Belief**: alto
- **Catena di ragionamento**: conferma e rafforza [[claim_registry_current#CLAIM 004]]/(ipomielinizzazione non-cell-autonomous) e la lettura per cui **parte di P6/P4 è downstream del neurone**, non processo gliale autonomo. Rilevante per la strategia molecole: correggere il **neurone** (o consegnargli WWOX) propaga a mielina/gliosi/metabolismo → il neurone è il bersaglio a più alto guadagno di rete. Il rescue della glicemia da WWOX *solo cerebrale* rilancia l'asse **metabolico CNS-centrico** (lega a MECH-005, P5).
- **Perché conta**: sostiene la scelta di targeting **neuron-specific** (SynI) come design ottimale e indica il neurone come nodo-master anche per leve non-genetiche · **Possibile passo successivo**: identificare il **segnale neurone→OPC** mediato da WWOX (il mediatore è il vero target druggabile non-genetico) → NS-017 · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-005 — Gene REPLACEMENT AAV9-hSynI-hWWOX-WPRE (ICV, neuron-specific): rescue dose-dipendente e durevole (P300) — genotype-agnostic → NON dipende dagli alleli SDR del genotipo di riferimento|DL-MOL-005]], [[discovery_ledger_current#DL-MECH-005 — Convergenza biallelica sul dominio SDR/ossidoreduttasi: l'asse metabolico (P5) è meccanicisticamente centrale per il genotipo di riferimento *in particolare*|DL-MECH-005]] (glucosio/metabolismo), [[discovery_ledger_current#DL-MECH-007 — Piattaforma organoidi WOREE da iPSC paziente + rescue con WWOX ectopico (abilita gli esperimenti del ledger)|DL-MECH-007]]

### DL-MECH-011 — Finestra terapeutica P1–P5 nel topo: efficace se precoce → il gap traslazionale critico per il genotipo di riferimento è l'efficacia del trattamento *post-onset / età più avanzata*
- **Status**: maturing · **Tag**: DATO (finestra murina, S8) + IPOTESI (limite per il genotipo di riferimento) · **Fonte**: Obeid/Aqeilan 2026 OMTA **Fig S8** (iniezione P1/P2/P3/P5 → sopravvivenza fino a P300, peso, glucosio, mielina, GFAP normalizzati)
- **L'indizio**: il trattamento a **P1, P2, P3 e P5** riscatta sopravvivenza e fenotipi CNS. Tutto lo studio (e il 2021) tratta in finestra **neonatale**; il topo Wwox-null muore a 3–4 settimane, quindi non esiste dato su trattamento in animale sintomatico/maturo.
- **Mappa ABC**: A=terapia genica WWOX · B=**timing** dell'intervento rispetto allo sviluppo/onset · C=finestra di massima efficacia · **Statement causale**: `AAV-WWOX(P1–P5) —rescues→ phenotype (durevole P300)`; (ignoto) `AAV-WWOX(post-onset, older) —?→ rescue` · **Belief**: alto sul dato murino precoce; **il limite per il genotipo di riferimento è IPOTESI** (non testato, non dimostrato negativo)
- **Catena di ragionamento**: P1–P5 murino ≈ **perinatale/tardo-gestazionale umano**. la finestra clinica reale è **post-natale e già sintomatica** → è esattamente la condizione **non coperta** dai dati. Parte del danno WOREE è **prenatale/pre-cablato** ([[claim_registry_current#CLAIM 013]] struttura prenatale) → una quota potrebbe non essere reversibile a valle. Ma: (a) il 2021 discute esplicitamente di esplorare vie/età diverse; (b) restauro anche *parziale/tardivo* è atteso comunque benefico (nota registro, Gao 2025) su rete/mielina/gliosi che sono processi **postnatali dinamici e potenzialmente reversibili**. Il verdetto per il genotipo di riferimento è **aperto**, non negativo.
- **Perché conta**: è **la domanda-cardine** che decide se la gene therapy è un'opzione reale per il genotipo di riferimento *oggi* o solo un paradigma; orienta la conversazione col gruppo Aqeilan e la lettura del first-in-human (che età trattano?) · **Possibile passo successivo**: NS-016 (età/criteri del first-in-human) + NS-018 (esiste dato di trattamento ritardato in qualsiasi modello WWOX o DEE affine?) · **Interconnessioni**: [[discovery_ledger_current#DL-MOL-005 — Gene REPLACEMENT AAV9-hSynI-hWWOX-WPRE (ICV, neuron-specific): rescue dose-dipendente e durevole (P300) — genotype-agnostic → NON dipende dagli alleli SDR del genotipo di riferimento|DL-MOL-005]], [[claim_registry_current#CLAIM 013]] (danno prenatale = quota non reversibile)

### DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)
- **Status**: maturing · **Tag**: DATO (convergente su ≥3 modelli) · **Fonte**: Aldaz lab — SCAR12 cervelletto (PMID 36828035, [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425)); sepsi/neuroinfiammazione (PMID 39868255, [DOI](https://doi.org/10.1101/2025.01.17.633677)); VILI polmone (PMID 38563965, [DOI](https://doi.org/10.1152/ajplung.00277.2023)) *(via PubMed)*
- **L'indizio**: in tutti i tessuti la **perdita di WWOX aumenta l'infiammazione** — cervelletto: astro-microgliosi progressiva + perdita Purkinje (Wwox^P47T); sepsi: peggiore gliosi/apoptosi cerebrale dopo LPS; endotelio polmonare: ↑ IL-6/IL-8/IL-1β/MCP-1 con **↑ERK/JNK e ↓p38 MAPK**, via zyxin. WWOX normalmente *trattiene* il segnale pro-infiammatorio (scaffold WW su partner MAPK/NF-κB).
- **Mappa ABC**: A=WWOX-loss · B=**de-repressione MAPK(ERK/JNK)/NF-κB → citochine → microglia/astrociti** · C=nodo infiammatorio druggabile (→ DL-REPO-002) · **Statement causale**: `WWOX —restrains→ inflammatory_MAPK/NFκB_signaling`; quindi `WWOX(loss) —increases→ IL1β/IL6/IL8/MCP1 + gliosis` · **Belief**: medio-alto (convergenza multi-tessuto, direzione univoca)
- **Catena di ragionamento**: questo è l'**ancora meccanicistica** che rende REPO-002 direzionalmente valido e alza la priorità della **meta neuroinfiammazione (meta 6, pending)**. A livello di malattia: se la proteina SDR-mutata è globalmente instabile/assente ([[discovery_ledger_current#DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento|DL-MECH-008]]), perde anche questo freno → l'asse infiammatorio è rilevante per lei. Nota: il modello di Aldaz è **P47T (WW1-scaffold)**, dominio diverso da quello del genotipo di riferimento (SDR) → il freno anti-infiammatorio potrebbe essere in parte funzione WW-scaffold; da verificare se è WW- o SDR-dipendente (lega a MECH-006 enzima-vs-scaffold).
- **Perché conta**: apre un secondo asse terapeutico (a valle, sintomatico/rallentante) complementare alla gene therapy; e nomina biomarcatori di attività (GFAP/Iba1/citochine — ⚠️ Tier 3 distale, NON biomarker WWOX) · **Possibile passo successivo**: NS-020/021; chiarire se il freno infiammatorio è WW- o SDR-dipendente · **Interconnessioni**: [[discovery_ledger_current#DL-REPO-002 — Farmaco anti-neuroinfiammatorio riposizionato come leva per la LoF di WWOX (asse Aldaz): direzione RISOLTA (WWOX-loss → infiammazione ↑ → serve INIBIRE)|DL-REPO-002]], [[discovery_ledger_current#DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento|DL-MECH-008]], [[discovery_ledger_current#DL-MECH-010 — WWOX *neuronale* (SynI) è SUFFICIENTE a riscattare fenotipi non-cell-autonomous (mielina, gliosi) e sistemici (glucosio) → il compartimento neuronale è il driver a monte; il promotore oligodendrocitario (MBP) è meno efficace|DL-MECH-010]] (gliosi downstream del neurone)

---

### DL-MECH-013 — WWOX come regolatore di sleep/network-state: bridge umano + Drosophila funzionale
- **Status**: open · **Tag**: INFERENZA · **Fonte**: Kim et al. 2025, *Scientific Reports*, PMID 39952983 / PMCID PMC11828923, "Genome-wide identification and functional validation of the WW domain containing oxidoreductase gene associated with sleep duration" (batch PubMed 2026-07-05)
- **L'indizio**: varianti introniche WWOX (rs16948804/rs4887991) sono associate a durata del sonno in coorti umane; in Drosophila, perdita di Wwox riduce e frammenta il sonno diurno e aumenta il sonno notturno senza abolire il ritmo circadiano. Il paper collega il fenotipo a metabolismo/ROS/tau.
- **Mappa ABC**: A=WWOX-LoF · B=stabilità sonno/ritmo network-state, metabolismo/ROS/tau · C=endpoint distale di stato rete e possibile readout pre/post intervento · **Statement causale**: `WWOX(loss) —alters→ sleep_architecture/network_state`; `sleep_fragmentation —may_proxy→ network_instability` · **Belief**: medio (human GWAS + modello fly; non WWOX-DEE pediatrico)
- **Perché conta**: il sonno non è biomarker WWOX Tier 1/2, ma può essere endpoint distale di rete: utile per monitorare finestra, crisi, frammentazione e risposta a interventi, specialmente se integrato con EEG/actigraphy. Non è prova terapeutica.
- **Esperimento minimo**: actigraphy/EEG sleep architecture in WWOX-DEE o modello WWOX rescue; readout atteso = normalizzazione di durata/frammentazione se WWOX/network-state migliora.
- **Interconnessioni**: [[discovery_ledger_current#DL-MOL-001 — Antagonismo NMDAR come leva di rescue del bursting da WWOX-loss|DL-MOL-001]], [[therapeutic_strategies_current#TX-006 — Window protection (time-sensitive variables already active)|TX-006]]

### DL-MECH-014 — Asse RNF138→hnRNPA0→WWOX mRNA→JAK2/STAT3/PD-L1: WWOX come freno di segnale immuno-oncologico
- **Status**: open · **Tag**: ESPANSIONE · **Fonte**: He et al. 2026, *Cell Reports*, PMID 42275215, "RNF138 promotes cisplatin resistance and PD-L1-mediated immune evasion via JAK2/STAT3 activation in nasopharyngeal carcinoma" (abstract PubMed; full text non OA nel run)
- **L'indizio**: l'abstract riporta che RNF138 promuove ubiquitinazione K48-linked di hnRNPA0, destabilizzando WWOX mRNA; la perdita di WWOX libera JAK2 autophosphorylation → JAK2/STAT3 attivo → PD-L1, chemoresistenza e immune evasion.
- **Mappa ABC**: A=WWOX loss/reduced mRNA · B=JAK2/STAT3 de-repression + PD-L1 · C=JAK/STAT o stabilità WWOX mRNA come nodo druggable · **Statement causale**: `RNF138 —destabilizes→ WWOX_mRNA`; `WWOX(loss) —de-represses→ JAK2/STAT3`; `JAK2/STAT3 —increases→ PD-L1/immune_evasion` · **Belief**: basso-medio (oncologia, abstract-only, ma direzione meccanicistica esplicita)
- **Perché conta**: non suggerisce immunoterapia per il genotipo di riferimento; nomina però un asse "WWOX basso → JAK/STAT alto" che può incrociare neuroinfiammazione/glia. Diventa una next-search, non una terapia.
- **Safety/BLOCCO 1**: JAK inhibitors CNS/pediatric = rischio immunosoppressione/infezioni; qualunque ipotesi repurposing resta **flagged** finché non esiste bridge neuro-WWOX specifico.
- **Interconnessioni**: [[discovery_ledger_current#DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)|DL-MECH-012]]

### DL-MECH-015 — WWOX/NME2/KAT1/SCD5/oleic-acid axis: ponte immunometabolico verso macrofagi M2
- **Status**: maturing · **Tag**: INFERENZA/ESPANSIONE · **Fonte**: Liu et al. 2024, *J Immunother Cancer*, PMID 39500530 / PMCID PMC11552608, "WWOX tuning of oleic acid signaling orchestrates immunosuppressive macrophage polarization and sensitizes hepatocellular carcinoma to immunotherapy" (già integrato; riletto nel batch)
- **L'indizio**: WWOX deficiency aumenta SCD5 e oleic acid, promuove polarizzazione macrofagi M2; WWOX interagisce con NME2 e modula acetilazione KAT1/NME2; blocco SCD5 migliora anti-PD-1 nel modello HCC.
- **Mappa ABC**: A=WWOX deficiency · B=NME2/KAT1/SCD5/OA → macrophage polarization · C=asse lipidico-immunitario misurabile/druggable · **Statement causale**: `WWOX(loss) —increases→ SCD5/OA`; `OA —promotes→ M2_macrophage_polarization` · **Belief**: medio per immunometabolismo WWOX; basso per trasferimento CNS/il genotipo di riferimento
- **Perché conta**: rafforza l'idea che WWOX regoli immunometabolismo e fenotipo macrofagico/microgliale. SCD5/OA non è ancora target per il genotipo di riferimento; è un ponte da verificare in microglia/astroglia o modelli neuro-WWOX.
- **Esperimento minimo**: in modello WWOX neuro/glia, misurare SCD5/OA e marker M2-like/microgliali; verificare se rescue WWOX normalizza asse lipidico.
- **Interconnessioni**: [[discovery_ledger_current#DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)|DL-MECH-012]]

### DL-MECH-016 — WWOX induction degrada Bcl-XL/Mcl-1 via lisosoma: stress-response e proteostasi anti-apoptotica
- **Status**: open · **Tag**: INFERENZA · **Fonte**: Su et al. 2026, *Cells*, PMID 41677633 / PMCID PMC12897155, "WWOX Induction Promotes Bcl-XL and Mcl-1 Degradation Through a Lysosomal Pathway upon Stress Responses" (già integrato; full text riletto nel batch)
- **L'indizio**: induzione WWOX sotto stress promuove degradazione lisosomiale di Bcl-XL e Mcl-1, proteine anti-apoptotiche. Il paper richiama anche legami con neurodegenerazione, tau e developmental deficits.
- **Mappa ABC**: A=WWOX stress-response · B=lysosomal turnover di Bcl-XL/Mcl-1 · C=proteostasi/apoptosi come readout o rischio · **Statement causale**: `WWOX(induction) —promotes→ lysosomal_degradation(Bcl-XL/Mcl-1)` · **Belief**: medio per asse cellulare; basso per trasferimento neuronale pediatrico
- **Perché conta**: utile come caution: aumentare WWOX o manipolare stress/proteostasi può toccare apoptosi. Potenziale biomarker sperimentale in cellule, non target terapeutico immediato.
- **Safety/BLOCCO 1**: qualunque modulatore Bcl-XL/Mcl-1 è ad alto rischio in pediatria/CNS; non proporre BH3 mimetics come repurposing per il genotipo di riferimento.
- **Interconnessioni**: [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]]

### DL-MOL-006 — Zfra peptide come asse neurodegeneration-suppression WWOX-related
- **Status**: open · **Tag**: ESPANSIONE · **Fonte**: Chen et al. 2024, *Int J Mol Sci*, PMID 38542478 / PMCID PMC10970703, "Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration" (già integrato; full text riletto nel batch)
- **L'indizio**: Zfra è un peptide di 31 aa riportato come modulatore di neurodegenerazione/cancro; interagisce con WWOX e accelera degradazione WWOX, ma viene proposto dagli autori come capace di sopprimere progressione neurodegenerativa.
- **Mappa ABC**: A=network WWOX/Zfra · B=neurodegeneration/proteostasis/aggregate stress · C=peptide/modulatore · **Statement causale**: `Zfra —binds/modulates→ WWOX_network`; `Zfra —may_suppress→ neurodegeneration_progression` · **Belief**: basso-medio; letteratura di un filone specifico, transfer a WOREE non dimostrato
- **Perché conta**: entra come pista da monitorare, non come proposta terapeutica. L'effetto "degrada WWOX" è potenzialmente controintuitivo in WWOX-LoF, quindi serve capire se il beneficio è WWOX-independent o context-specific.
- **Safety/BLOCCO 1**: peptide sperimentale, nessun profilo pediatrico/CNS utile; non sale a Layer 9.
- **Interconnessioni**: [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]]

### DL-MECH-018 — Interactome WWOX full-length: DVL2/Wnt + traffico endomembrana + metabolismo Acetyl-CoA come hub sperimentale
- **Status**: maturing · **Tag**: DATO (interactome/pathway in HEK293T) + INFERENZA (trasferimento al genotipo di riferimento) · **Fonte**: Hussain et al. 2018, *Frontiers in Oncology*, PMID 30619736 / PMCID PMC6300487 / DOI 10.3389/fonc.2018.00591; dossier locale `staging/dossier_30619736_WWOX_interactome.md`. Questo e' verosimilmente la fonte primaria dietro [[claim_registry_current#CLAIM 026]] / `CORPUS P182`.
- **L'indizio**: TAP-MS con WWOX full-length SFB-tag identifica 216 binding partners ad alta confidenza. Top interactors: **DVL2** (score 1.07), WBP2, DHRS13, HIRIP3, **SEC23IP**, **VOPP1**, AMOT, DVL1, VARS2, **SCAMP3**. Co-IP/GST-pulldown confermano binding diretto di WWOX con SEC23IP, SCAMP3 e VOPP1; pathway enrichment: branched-chain amino-acid degradation, glycolysis/gluconeogenesis, pyruvate metabolism, fatty-acid degradation, convergenti su **Acetyl-CoA**.
- **Mappa ABC**: A=WWOX-LoF/varianti del genotipo di riferimento · B=perdita di scaffold full-length su nodi DVL2/Wnt + ER/Golgi/endosomal/lysosomal trafficking + metabolismo Acetyl-CoA · C=readout sperimentali e target downstream: DVL2/β-catenin localization, SEC23IP/SCAMP3/VOPP1 trafficking, HIF1A/glycolysis, BCAA/fatty-acid/Acetyl-CoA metabolites.
- **Statement causale**: `WWOX_full_length —binds→ DVL2/DVL1 + SEC23IP/SCAMP3/VOPP1`; `WWOX_interactome —enriches→ trafficking/metabolic_Acetyl-CoA_pathways`; (inferito) `WWOX(loss) —disorganizes→ endomembrane-metabolism coupling` · **Belief**: alto per DATO interactome in cellula; medio per trasferimento a neuro-WWOX; medio-alto come supporto a CLAIM 026.
- **Perché conta**: il genotipo di riferimento ha due varianti che convergono sul dominio SDR, ma Q230P probabilmente destabilizza tutta la proteina: se la proteina residua e' bassa, non si perde solo l'attività SDR, ma anche lo scaffold WW/full-length che aggancia DVL2 e traffico endomembrana. Questo paper quindi rende BIO-001 (quantità/stabilità proteina WWOX) ancora più centrale: decide se le funzioni scaffold potenzialmente risparmiate dal dominio mutato siano in realtà perse per instabilità globale.
- **Esperimento minimo**: su fibroblasti/LCL/iPSC donor-derived-derived: (1) Western WWOX ± proteasome/lysosome inhibitors; (2) DVL2 subcellular localization/β-catenin nuclear readout; (3) pannello mirato metaboliti BCAA/fatty-acid/pyruvate/Acetyl-CoA proxy; (4) se iPSC-neuroni disponibili, confrontare traffico ER/Golgi/endosome (SEC23IP/SCAMP3/VOPP1) pre/post rescue WWOX.
- **Officina**: DGIdb/GraphQL conferma che DVL2/WWOX non sono facilmente druggable direttamente; i nodi downstream druggable restano HIF1A, GSK3B, JAK2/STAT3/IL6, ma qui il valore principale e' **biomarker/readout selection**, non farmaco pronto.
- **Interconnessioni**: [[claim_registry_current#CLAIM 026]], [[discovery_ledger_current#DL-MECH-005 — Convergenza biallelica sul dominio SDR/ossidoreduttasi: l'asse metabolico (P5) è meccanicisticamente centrale per il genotipo di riferimento *in particolare*|DL-MECH-005]], [[discovery_ledger_current#DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento|DL-MECH-008]], [[discovery_ledger_current#DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo|DL-MOL-003]], [[biomarker_candidates_current#4. TISSUE ACCESSIBILITY MAP]]

## Euristiche apprese (compounding del metodo)
| ID | Euristica | Nata da |
|----|-----------|---------|
| H-001 | In un cohort multi-gene, il valore-scoperta per WWOX spesso non è "WWOX c'è" ma il **contrasto** con gli altri geni: cosa funziona per loro e *perché non* per WWOX → isola la leva WWOX-specifica. | DL-REPO-001 |
| H-002 | Un gene "vicino" nel cohort (qui GRIN2A) può fornire **corroborazione human-genetics** a un meccanismo visto solo in modello animale (Breton) → alza un'IPOTESI a INFERENZA senza nuovo esperimento. | DL-MECH-002 |
| H-003 | **Strumento in-silico per tipo di variante**: missenso → AlphaFold3/AlphaMissense/ΔΔG (struttura/folding); splicing → SpliceAI/Pangolin/MMSplice (esito trascrizionale); PPI → AF3-multimer. L'output predittivo è sempre **IPOTESI generatrice**, mai DATO: serve a *nominare* un readout wet (proteina/attività/trascritto in fibroblasti donor-derived), che è il vero biomarcatore. | DL-BIO-001/002, DL-MECH-006 |
| H-004 | **Mappare le varianti sui dominî proteici** prima di scegliere lo strumento: dove cadono (catalitico vs scaffold) cambia sia il meccanismo prevalente sia la classe di terapia sensata. La convergenza di alleli sullo stesso dominio è essa stessa una scoperta (alza la priorità del pathway di quel dominio). | DL-MECH-005 |
| H-005 | **Risolvere la direzione PUÒ ribaltare un candidato, non solo confermarlo**: per MOL-003 avevo nominato il litio (GSK3β-i); fissata la direzione (WWOX-loss → Wnt iper-attiva), il litio risulta *peggiorativo* e il candidato corretto è un *inibitore* Wnt. Il gate-direzione non è burocrazia: previene un intervento dannoso. Sempre fissare il verso con ≥2 fonti **prima** di nominare un farmaco. | DL-MOL-003 |
| H-006 | **Mappare il dominio del residuo sul sito attivo noto** (non solo sul dominio): Q230 è nel dominio SDR ma *non* è catalitico (catalisi = S281/Y293/K297) → l'effetto è destabilizzazione del folding (proteina instabile), non perdita catalitica diretta → cambia il readout biomarcatore (stabilità/abbondanza, non attività). | DL-BIO-001 |
| H-007 | **Una funzione downstream è rilevante per il paziente solo se la perde davvero**: il controllo Wnt è WW-scaffold; se la variante è SDR, quella funzione si perde *solo* se la proteina è globalmente instabile → ogni asse a valle va condizionato al dato di proteina residua, non assunto. | DL-MECH-008 |
| H-008 | **Gene replacement = genotype-agnostic → disaccoppia la terapia dalla variante**: consegnare una copia sana bypassa la mutazione, quindi la sua efficacia **non dipende** dallo stato ipomorfo/residuo donor-derived (a differenza di CRISPRa/chaperone/small-molecule che richiedono proteina residua). Corollario: per il replacement il collo di bottiglia non è la variante ma **timing** (finestra) e **biodistribuzione/dose**; per le leve variante-dipendenti il collo di bottiglia è BIO-001 (quanta proteina residua). Classificare ogni lead terapeutico su questo asse chiarisce *quale dato serve* per ciascuno. | DL-MOL-005, DL-MOL-004 |
| H-009 | **Il supplemental è spesso la miniera dei design-principle**: gli avanzamenti quantitativi decisivi (dose-response, ruolo del WPRE, confronto promotori, finestra P1–P5) erano **solo** nelle figure S1–S8, non nell'abstract. E confrontare supplemental primario vs review dello stesso gruppo può scoprire una **contraddizione di framing** ("WPRE removed to avoid overexpression" vs S3 "WPRE alza 3–16.7×") che è essa stessa un nugget (il trade-off dose↔sicurezza). | DL-MECH-009 |

## Next-search agenda (curriculum — ordinata per guadagno atteso)
| ID | Query/target | Prospettiva | Da quale lead nasce | Priorità | Status | Esito |
|----|--------------|-------------|---------------------|----------|--------|-------|
| NS-001 | Full text Riccardi 2026 (find-fulltext / email autore Milh-Villard, Marseille) → dettagli caso/i WWOX: variante, timing BS, outcome, risposta farmaci | elettrofisio/clinica | MECH-001/003, REPO-001 | **alta** | open | — |
| NS-002 | `WWOX AND (NMDA OR NMDAR OR memantine) AND (hyperexcitability OR bursting OR rescue)` | farmacologica | MOL-001 | **alta** | **done** | 49 hit; pescato modello organoidi WOREE (PMID 34268881) → MECH-007, MOL-003 |
| NS-003 | Breton 2021 full text (è il CLAIM papers 210) → condizioni esatte in cui NMDAR/gap-junction block annulla il bursting | elettrofisio | MOL-001/002 | alta | open | non trovato per nome via PubMed (è "papers 210" via review Obeid); ritentare con find-fulltext |
| NS-011 | Contattare/valutare gruppo **Aqeilan** (Haifa): il modello organoidi WOREE può ospitare i test NMDAR (MEA) e Wnt (CHIR)? esiste già elettrofisiologia? | sperimentale/collab | MECH-007, MOL-001/003 | **alta** | open | — |
| NS-012 | `WWOX AND Wnt`/`beta-catenin` → direzione del difetto Wnt | farmacologica | MOL-003 | **alta** | **done** | RISOLTA in contesto cancro: WWOX-loss → Wnt **iper-attiva** (Bouteille 2009/Li 2012/Celebi 2020). Litio ribaltato a contro-indicato; candidato = inibitore Wnt. Resta da confermare nel neurone → NS-013 |
| NS-013 | Full text organoidi WOREE (PMID 34268881, EMBO Mol Med, **open access PMC**) → la disregolazione Wnt è iper o ipo nel neurone in sviluppo? stato β-catenin nucleare? | strutturale/sperimentale | MOL-003, MECH-008 | **alta** | open | — |
| NS-014 | Recuperare score **AlphaMissense** puntuale per WWOX p.Q230P (Ensembl VEP / dbNSFP / AlphaMissense table) — output numerico, non stima | strutturale | BIO-001 | media | open | — |
| NS-015 | KG esterni (Open Targets/DRKG) + AdisInsight (se autorizzato): **inibitori Wnt/tankyrase** approvati o in trial con profilo pediatrico | farmacologica | MOL-003 | media | open | — |
| NS-004 | `GRIN2A AND WWOX` / espressione subunità NMDAR (GluN2A/2B) in modelli WWOX-null | genetica | MECH-002 | media | open | — |
| NS-005 | `WWOX AND (SNARE OR synaptic vesicle OR SNAP25 OR syntaxin)` interattoma | genetica | MECH-004 | bassa | open | — |
| NS-006 | KG esterni (Open Targets/DRKG): farmaci approvati su GRIN2A/NMDAR con profilo pediatrico | farmacologica | MOL-001 | media | open | — |
| NS-007 | Eseguire AF3 + AlphaMissense + ΔΔG (FoldX/Rosetta) su **WWOX-WT vs p.Q230P**; verificare se Q230 è residuo catalitico/NAD-binding del dominio SDR | strutturale | BIO-001, MECH-005/006 | **alta** | open | — |
| NS-008 | SpliceAI/Pangolin/MMSplice su **c.1057-2A>G** → score skipping esone 9 ed esito predetto (PTC/NMD vs sito criptico) | strutturale/genetica | BIO-002 | **alta** | **done (in-silico)** | 2026-07-04: SpliceAI DS_AL 0.96 (acceptor-loss) / DS_AG 0.64 (criptico +8) / MaxEntScan Δ-7.95 → null-like esone 9. Ramo sito-criptico confermato. Residuo: RT-PCR wet per esito quantitativo (skipping vs criptico vs NMD) |
| NS-009 | Lett.: fenotipo di varianti WWOX nel dominio **SDR/missenso** (Johannsen 2018, Weisz-Hubshman 2019) vs varianti null — esiste correlazione genotipo(dominio)-fenotipo? asse metabolico distinto? | clinica/genetica | MECH-005 | media | open | — |
| NS-010 | AF3-multimer **WWOX–ATM** (WT vs Q230P) + assay DDR (γH2AX/comet) come secondo biomarcatore in fibroblasti | strutturale/funzionale | MECH-006 | media | open | — |
| NS-016 | **First-in-human WWOX gene therapy** (Aqeilan lab, giu 2026, registro FT-012): quale costrutto (dose, ±WPRE, promotore, via), quali **criteri di età/onset** di arruolamento, quale endpoint? (ClinicalTrials.gov / press / AdisInsight se autorizzato) | clinica/farmacologica | MOL-005, MECH-009/011 | **alta** | **done (parz.)** | Giu 2026: primo paziente = **lattante** WOREE (crisi da ~6 sett.), AAV9-WWOX intracerebrale, **uso compassionevole** (Dr. Orenstein); **domanda FDA entro ~2 mesi**. Conferma finestra precoce (coerente MECH-011). Età/outcome esatti + follow-up → ancora da recuperare (no dato su bambino più grande) |
| NS-017 | Il **mediatore neurone→OPC** WWOX-dipendente (segnale non-cell-autonomous che matura gli oligodendrociti): interattoma/secretoma neuronale WWOX-dipendente → possibile target druggabile non-genetico per la mielina | genetica/farmacologica | MECH-010 | media | open | — |
| NS-018 | Esiste **qualsiasi** dato di gene therapy WWOX (o DEE affine: CDKL5, STXBP1) con trattamento **ritardato/post-onset** in animale maturo? quanto rescue si perde col timing? | clinica/sperimentale | MECH-011 | **alta** | open | — |
| NS-019 | Full text main OMTA vol 34 (paywall/non ancora su PubMed): dati **ECoG/SWD** primari (rescue elettrofisiologico quantitativo) + eventuale readout comportamentale/cognitivo dose-dip. — via find-fulltext / foundation route / corresponding-author request | elettrofisio/clinica | MOL-005, CLAIM 011 | media | open | — |
| NS-020 | **Contattare il gruppo corrispondente del lavoro P47T** (corresponding author, via canali istituzionali pubblici) — è la via più rapida per il nome del compound e lo stato del test in Wwox^P47T | collaborativa | REPO-002 | **alta** | open | — |
| NS-021 | Identificare farmaco + "trial di Zhang/Baylor": (a) chiedere alla WWOX Foundation il nome del grant Aldaz ~25k USD; (b) cross-check coautori Baylor del paper SCAR12 = **Noebels/Seo (Neurology)** — verificare se il "Zhang" ricordato è di quel gruppo o un trialist separato; (c) ClinicalTrials.gov "Baylor Zhang" per malattia neuro-infiammatoria | clinica/farmacologica | REPO-002, MECH-012 | **alta** | **done (parz., negativo)** | ClinicalTrials.gov: unici "Zhang"/Baylor = **oncologici** (Jun Zhang, lenalidomide NSCLC, Ph1, NCT02018523; Xiang Zhang, sitravatinib TNBC, Ph2, NCT04123704). NESSUN trial neuro-infiammatorio di riposizionamento. Nota debole: lenalidomide (IMiD) ha proprietà anti-TNF/anti-neuroinfiammatorie → thread possibile ma è Ph1-oncologico, improbabile sia quello. **Conclusione: farmaco NON identificabile da fonti pubbliche → resta contatto diretto Aldaz (NS-020)** |
| NS-022 | Chiarire se il **freno anti-infiammatorio di WWOX** è WW-scaffold o SDR-dipendente (rilevante per il genotipo di riferimento che ha varianti SDR, non WW1 come il P47T di Aldaz) | strutturale/meccanicistica | MECH-012, MECH-006 | media | open | — |
| NS-023 | Costruire pannello biomarker sperimentale da interactome WWOX: WWOX protein/stability + DVL2/β-catenin localization + SEC23IP/SCAMP3/VOPP1 trafficking + metaboliti BCAA/fatty-acid/pyruvate/Acetyl-CoA proxy | biomarker/metabolica | MECH-018, BIO-001, MECH-005 | **alta** | open | — |
| NS-024 | Distinguere in campioni donor-derived-derived "SDR-only loss" vs "whole-protein scaffold loss": Western WWOX, proteasome/lysosome rescue, DVL2 localization, attività/metaboliti SDR-linked | strutturale/funzionale | MECH-018, MECH-008, TX-003 | **alta** | open | — |

## Riflessioni di processo (cosa funziona, vicoli ciechi)
| Data | Hop/paper | Cosa ha dato i lead migliori | Vicolo cieco (non riaprire) | Da fare diversamente |
|------|-----------|------------------------------|------------------------------|----------------------|
| 2026-06-28 | Riccardi 2026 (abstract-only) | Il **contrasto** col registro esistente (Breton), non il paper isolato. La differenza KCNQ2-vs-WWOX ha generato la leva NMDAR. | Trattare "WWOX è citato" come scoperta: è solo contesto. | Recuperare il full text *prima* (NS-001): timing BS e farmacoresponse WWOX-specifici sono ciò che manca per far maturare MECH-003 e REPO-001. |
| 2026-06-28 | Referto genetico di riferimento (no paper) | Partire dal **genotipo donor-derived** + mappa dei dominî ha generato lead BIO *fattibili* (assay fibroblasti) più traslabili degli spunti da cohort. La convergenza dei due alleli sul dominio SDR è il nugget. | Aspettarsi che AlphaFold dia il biomarcatore: dà solo l'IPOTESI; il biomarcatore è il readout wet che essa nomina. | Eseguire davvero NS-007/008 (modelli) per far maturare BIO-001/002 da IPOTESI a INFERENZA; verificare nei current quanto P5 è già prioritario. |
| 2026-06-28 | Hop Wnt+catalisi (PubMed, multi-fonte) | Risolvere una **direzione** ha prodotto più valore di un nuovo lead: ha *ribaltato* il candidato litio→inibitore (H-005) e condizionato l'asse Wnt al dato di proteina residua (MECH-008). La mappa del **sito catalitico** ha riclassificato Q230 da "catalitico" a "strutturale" (H-006), cambiando il readout. | Assumere che "pathway disregolato" implichi la direzione del fix: quasi mai vero. Trasferire il verso cancro→neurone senza verifica (flaggato conflitto, NS-013). | Recuperare il full text organoidi (NS-013, è open access PMC) per confermare il verso Wnt nel contesto giusto *prima* di nominare inibitori Wnt specifici. |
| 2026-07-03 | Obeid/Aqeilan 2026 OMTA gene therapy (supplemental S1–S8 + proof-of-concept 2021 full text) | I **supplementari** hanno dato tutti i design-principle quantitativi (dose, WPRE 3–16.7×, promotori, finestra P1–P5) — l'abstract non bastava (H-009). Il nugget più forte non è "la terapia funziona" (già a CLAIM 011) ma **perché è robusta per il genotipo di riferimento nonostante le sue varianti**: replacement = genotype-agnostic (H-008). E la **contraddizione review↔supplemental** sul WPRE = trade-off dose/sicurezza. | Trattare il paper come "solo conferma di CLAIM 011": avrebbe perso i design-principle e il gap-timing, che sono il vero valore decisionale per il genotipo di riferimento. | Inseguire NS-016/018 (età del first-in-human + esiste rescue post-onset?) — è **la** domanda che decide la rilevanza reale per il genotipo di riferimento, più di ogni altro dato del paper. |

## Lead scartati (per non rivalutarli)
| Fonte | Spunto | Perché scartato |
|-------|--------|-----------------|
| Riccardi 2026 | DPM1/PIGO (glicosilazione/GPI) come asse WWOX | Link a WWOX troppo tenue, nessuna convergenza nei current; rivalutare solo se emerge un asse lipide-glicosilazione |

---

## Change-log
| Data | Azione | Voce | Note |
|------|--------|------|------|
| 2026-06-28 | created | ledger | Bootstrap dal template; primo paper = Riccardi 2026 (PMID 42190144) |
| 2026-06-28 | created | DL-MECH-001..004, DL-MOL-001/002, DL-REPO-001 | da Riccardi 2026 (abstract) × CLAIM Breton 2021 |
| 2026-06-28 | created | H-001, H-002 | euristiche distillate |
| 2026-06-28 | created | NS-001..006 | next-search agenda |
| 2026-06-28 | created | DL-BIO-001/002, DL-MECH-005/006 | da referto genetico il record pubblico di variante (genotipo di riferimento) × pipeline strutturale AlphaFold3/AlphaMissense/SpliceAI — modelli da eseguire |
| 2026-06-28 | created | H-003, H-004 | euristiche: strumento-per-tipo-variante; mappare varianti sui dominî |
| 2026-06-28 | created | NS-007..010 | next-search: esecuzione modelli strutturali + correlazione dominio-fenotipo |
| 2026-06-28 | hop NS-002 | DL-MOL-003, DL-MECH-007, NS-011/012 | da Repudi & Aqeilan EMBO Mol Med 2021 (PMID 34268881): organoidi WOREE, asse Wnt, rescue WWOX ectopico |
| 2026-06-28 | assembly | DL-MOL-001 | belief medio→medio-alto, status open→maturing: convergenza Breton+GRIN2A+organoidi (3 fonti indipendenti) |
| 2026-06-28 | hop Wnt/catalisi | DL-MOL-003 (ribaltato), DL-MOL-004, DL-MECH-008, H-005/006/007, NS-013/014/015 | direzione Wnt risolta (Bouteille/Li/Celebi); sito catalitico SDR mappato (PMC4374002); litio→contro-indicato; +lead CRISPRa; conflitto contesto cancro-vs-neurone flaggato |
| 2026-07-03 | paper Obeid/Aqeilan 2026 OMTA gene therapy (supplemental S1–S8) + proof-of-concept 2021 (PMID 34747138) | DL-MOL-005, DL-MECH-009/010/011, H-008/009, NS-016/017/018/019 | gene replacement genotype-agnostic (maturing, belief alto mouse / medio il genotipo di riferimento); WPRE booster 3–16.7× + contraddizione review; neuron-specific driver non-cell-autonomous; gap-timing = domanda-cardine per il genotipo di riferimento. Assembly: belief MECH-007 confermato alto (3 livelli convergenti). Paper già canonico (PAPER Obeid 2026 + CLAIM 011) → nessun CC duplicato; segnalato solo upgrade preprint→published |
| 2026-07-03 | hop "compound Aldaz/Zhang" (richiesta dell'operatore) — ricerca PubMed + web | DL-REPO-002, DL-MECH-012, NS-020/021/022 | asse **neuroinfiammazione** WWOX (Aldaz, multi-tessuto) = ancora meccanicistica; lead REPO anti-infiammatorio riposizionato (direzione risolta: inibire); farmaco specifico + trial "Zhang/Baylor" **NON nel record pubblico** (probabile preclinico/foundation non pubblicato); ponte Baylor reale = Noebels/Seo (Neurology). Recovery via contatto diretto Aldaz (NS-020) |
| 2026-07-05 | deepdive PMID 30619736 | DL-MECH-018, NS-023/024 | WWOX full-length interactome normalizzato come probabile fonte primaria CLAIM 026/CORPUS P182; DVL2 + endomembrane trafficking + Acetyl-CoA diventano pannello sperimentale, non farmaco pronto |

---

## Run 2026-07-05 — lead dalla lista 50-studi (autopilota)

> Deep-dive dei 2 soli paper realmente NUOVI e WWOX-centrali della lista (gli altri 48 già tracciati o rumore/locus-GWAS). Read-only sui 4 current; promozione solo via CC.

### DL-MECH-017 — WW2 come chaperone intramolecolare che stabilizza WW1 (rinforza il razionale stabilizzatori/proteostasi)
- **Status**: open · **Tag**: DATO (meccanismo strutturale) + IPOTESI (estensione terapeutica)
- **Fonte**: Rotem-Bamberger et al. 2022, J Biol Chem (PMID 35716775, PMC9293652) — *nuovo, non era a registro*
- **Finding (DATO)**: con CD/NMR + denaturazione in urea, **WW1 è ripiegato solo nel tandem WW1–WW2, non isolato** → il dominio **WW2 agisce da chaperone intramolecolare** che stabilizza WW1 e ne migliora l'affinità per i motivi PPxY dei partner. Il primo triptofano stabilizza il dominio, il secondo media il binding.
- **Statement causale**: `WW2 —stabilizes→ WW1_fold —enables→ PPxY_partner_binding`
- **Rilevanzal genotipo di riferimento / interconnessioni**: rinforza concettualmente la leva **rescue proteostatico/stabilizzatori** già tracciata ([[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]], *CC-2026-07-04-004 (private commit queue)*): WWOX usa *nativamente* stabilizzazione intramolecolare del folding → un chaperone farmacologico/stabilizzatore su una variante destabilizzata (come Q230P nel dominio SDR, o P47T nel WW1) è meccanicisticamente plausibile. **NB**: qui il dominio è WW1/WW2 (interattoma), Q230P è SDR (enzima) → trasferimento è ESPANSIONE, non prova. **Belief**: medio.
- **Esperimento**: assay di stabilità (Tm/urea) su WWOX-Q230P ± piccoli stabilizzatori. ⚠️ *Aggiornato dopo il repair 2026-07-14:* il banco read-across P47T è **ritirato** — P47T è un **comparator**, **non** una via di trasferimento (proteina normale, difetto WW1/PPxY).

### DL-MOL-007 — Fallimento sistematico degli ASM sintomatici in WOREE severo → priorità alle leve disease-modifying
- **Status**: open · **Tag**: DATO (profilo di farmaco-resistenza riportato) + INFERENZA (implicazione strategica)
- **Fonte**: Riva et al. 2022, Front Pediatr (PMID 35573960, PMC9100683) — *nuovo, non era a registro* — caso WOREE compound-het (p.Arg264* + delezione esone 6)
- **Finding (DATO)**: in WOREE severo, **inefficaci**: valproato, vigabatrin, clonazepam, clobazam, levetiracetam, rufinamide, CBD, fenobarbital, nitrazepam, **3 cicli ACTH**, **dieta chetogenica**. Fino a 50 crisi/die. + WWOX-KO → **↓ sintesi GABA** + perdita interneuroni GABAergici ippocampali e cellule di Purkinje; hNPC → citoscheletro compromesso → migrazione neuronale disrotta.
- **Statement**: `WOREE_null —refractory_to→ symptomatic_ASM` ; `WWOX-LoF —reduces→ GABA_synthesis` (corrobora [[meta_gaba_paradox_current]])
- **Rilevanzal genotipo di riferimento / implicazione (INFERENZA)**: il carico terapeutico sintomatico ha resa attesa bassa nel fenotipo severo → **conferma la priorità strategica della missione** verso leve *disease-modifying / mechanism-targeted* (correzione difetto, protezione-finestra, rescue proteostatico) piuttosto che l'ennesimo ASM. Il dato GABA rinforza l'asse GABA come bersaglio. **Belief**: alto sul dato ASM, medio sull'implicazione.
- **Nota disciplina**: il pattern neuroimaging WOREE (mielinizzazione ritardata, ipoplasia verme, leucomalacia-like) è **Tier 3 endpoint clinico** → [[clinical_monitoring_endpoints_current]], NON biomarker WWOX.

### Change-log
- 2026-07-05 — Aggiunti DL-MECH-017 (WW2 chaperone, PMID 35716775) + DL-MOL-007 (ASM-resistance WOREE + GABA, PMID 35573960) dal run autopilota sulla lista 50-studi. Entrambi i paper sono nuovi → proposti a PAPER via CC staging.

### DL-MECH-032 — WWOX è una GSK-3β-binding protein via motivo GID (ago d'oro da un paper "rumore" su SARS-CoV-2)
- **Status**: open · **Tag**: DATO (WWOX∈GID-proteins) + INFERENZA (implicazione per il genotipo di riferimento) + ESPANSIONE (repurposing)
- **Fonte**: Yook et al. 2022, Mol Cells (PMID 36572560, PMC9794558) — paper su fosforilazione della nucleocapside SARS-CoV-2, classificato "rumore" al triage. *Dimostra la regola "ogni studio è oro".*
- **Finding (DATO, citato nel paper)**: il motivo alpha-elica **GID (GSK-3 interacting domain, L/FxxxL/AxxRL)** è presente in molte proteine endogene che legano GSK-3β — esplicitamente **Axins, FRATs, WWOX, GSKIP**. GSK-3β è druggabile (inibitori GSK-3 sopprimono la replicazione virale → GSK-3β è rate-limiting).
- **Statement causale**: `WWOX —binds(via GID)→ GSK-3β` (DATO strutturale-motivo); (INFERENZA) `WWOX-LoF —dysregulates→ GSK-3β_activity` → tocca [[meta_prenatal_structure_current]] (asse GSK3β/Tau già nel WM)
- **Rilevanza di malattia / implicazione**: se WWOX è un partner/regolatore di GSK-3β (classe Axin), la sua perdita nel genotipo di riferimento può **disregolare GSK-3β** — nodo già druggabile (**litio, inibitori GSK-3**) → candidato **repurposing/leva di compensazione** a valle della perdita di WWOX. Da verificare: direzione dell'effetto (WWOX attiva o inibisce GSK-3β?) e se il GID è nel dominio WW o SDR di WWOX (rilevante per Q230P/P47T). **Belief**: medio-alto sul binding (dato di letteratura consolidato citato), medio sull'implicazione terapeutica.
- **Esperimento**: (in-silico) mappare il motivo GID su WWOX (sequenza/struttura) e verificarne l'integrità in Q230P; (letteratura) recuperare i lavori primari WWOX–GSK-3β (es. gruppo Chang) per la direzione dell'effetto; (wet) attività GSK-3β in fibroblasti donor-derived ± inibitore.
- **Interconnessioni**: [[meta_prenatal_structure_current]], [[discovery_ledger_current#DL-MOL-001 — Antagonismo NMDAR come leva di rescue del bursting da WWOX-loss|DL-MOL-001]] (leve di rescue), possibile nuova TX (litio/GSK-3i) da valutare in [[therapeutic_strategies_current]] con gate della skill `legend-safety-triage`.

---

## Run 2026-07-09 — batch storico 50 studi (2016–2018)

### DL-BIO-005 — Pannello funzionale WWOX–HIF1α/GLUT1/PKM2 + alanina
- **Status:** open · **Tag:** INFERENZA/IPOTESI · **Fonti:** Abu-Remaileh 2018 (PMID 29724996), Teslovich 2018 (PMID 29481666), Bunai 2018 (PMID 29164763).
- **Lead:** WWOX loss aumenta HIF1α e target glicolitici nel fegato; TMEM207 può rendere inefficace WWOX sequestrandone l'interazione con HIF1α; una variante intronica WWOX è associata ad alanina sierica ma non replica significativamente.
- **Mappa ABC:** A=WWOX-LoF · B=HIF1α/glicolisi/stato funzionale partner-dipendente · C=HIF1α, GLUT1, PKM2, lattato/alanina come readout combinato.
- **Statement:** `WWOX(loss or functional sequestration) —increases→ HIF1α/GLUT1/glycolytic_state`; `alanine —may_report→ systemic_metabolic_state` · **Belief:** medio per HIF1α in modelli non-CNS; basso per alanina come marker WWOX.
- **Esperimento:** fibroblasti/LCL/iPSC donor-derived WT/Q230P/KO ± rescue; WWOX totale/emivita + PLA/co-IP WWOX–HIF1α + HIF1α/GLUT1/PKM2/lattato/alanina. Nessun biomarcatore validato.

### DL-BIO-006 — circRNA KIRKOS + WWOX mRNA esosomale come readout liquido del locus
- **Status:** open · **Tag:** IPOTESI · **Fonti:** O'Leary 2017 (PMID 29108237), Xu 2017 (PMID 29100284).
- **Lead:** KIRKOS-71/73 derivano da esoni WWOX e rispondono allo stress in modo cell-type-specifico; WWOX mRNA è tecnicamente rilevabile negli esosomi sierici oncologici.
- **Mappa ABC:** A=WWOX locus · B=back-splicing/EV export · C=ddPCR di junction KIRKOS + isoforme WWOX in EV/LCL/fibroblasti.
- **Guardrail:** non misura direttamente Q230P né lo splice dell'esone 9; segnale periferico/tumorale e normalizzazione EV sono problemi aperti. **Belief:** basso-medio come assay, basso come proxy CNS.
- **Esperimento:** EV purity + spike-in; ddPCR KIRKOS/WWOX full-length/allele-specific; correlazione con proteina e funzione WWOX.

### DL-MECH-023 — WWOX orienta UPR adattativa-vs-terminale sotto stress ER
- **Status:** open · **Tag:** DATO oncologico + INFERENZA per il genotipo di riferimento · **Fonte:** Janczar 2017 (PMID 28749468).
- **Lead:** rescue/knockdown bidirezionale collega WWOX alla morte da paclitaxel/tunicamicina con GRP78, IRE1, PERK/eIF2α, JNK/p38 e BCL-xL:BAX; nessuna interazione fisica WWOX–GRP78/JNK dimostrata.
- **Statement:** `WWOX_state —biases→ ER_stress_outcome(adaptive_vs_apoptotic)` · **Belief:** medio nel tumore, basso-medio nel neurone.
- **Perché conta:** Q230P misfolding rende UPR/proteostasi un pannello prioritario, ma l'obiettivo nel SNC è preservare sopravvivenza, non riprodurre l'apoptosi tumorale.
- **Esperimento:** time-course GRP78, XBP1 splicing, p-PERK/p-eIF2α/ATF4/CHOP, BCL-xL:BAX, caspasi/viability in isogenici WT/Q230P/KO ± rescue.

### DL-MECH-024 — WWOX–BRCA1/WW1 regola end-resection e scelta della riparazione DSB
- **Status:** maturing · **Tag:** DATO oncologico + INFERENZA · **Fonti:** Schrock 2017 (PMID 27869163), Schrock 2017 review/experiments (PMID 27773744).
- **Lead:** WWOX loss aumenta HDR/SSA e RPA32/RAD51, riduce NHEJ/alt-NHEJ; WW1 mutante perde BRCA1 binding, SDR Y293F no.
- **Statement:** `WWOX-WW1 —binds→ BRCA1 —limits→ end_resection/HDR`; `WWOX(loss) —alters→ DSB_pathway_choice` · **Belief:** medio-alto nel sistema cellulare.
- **Transfer al modello di malattia:** Q230P è SDR, quindi non assumere perdita diretta dell'interfaccia WW1; l'instabilità globale della proteina può però ridurre il ramo. Uso principale = assay di stress/GT, non terapia.
- **Esperimento:** WWOX abundance + γH2AX/RPA32/RAD51 + reporter DR-GFP/NHEJ in WT/Q230P/KO, separando progenitori proliferanti e neuroni.

### DL-MECH-025 — Retraction-dependency cluster WWOX/HIF/Met nelle metastasi ossee
- **Status:** flagged · **Tag:** DATO di integrità · **Fonti:** retraction PMID 28151481 / DOI 10.1038/s41419-022-04992-6; review PMID 28045433.
- **Lead negativo:** la review Maroni 2017 riusa come propria Fig. 3B dati dal paper ritirato e poggia i passaggi più originali su almeno tre fonti ritirate della stessa linea/modello.
- **Regola:** `review convergence —invalid_if→ dependent_primary_cluster_retracted`; nessuna proposizione HGF/Met–Twist–decitabina/autofagia da questo cluster può corroborare il WM.
- **Impatto:** nessun claim baseline attuale dipende direttamente dal paper ritirato; CLAIM 025 resta ancorato a fonti indipendenti. Audit cat-5 in attesa di autorizzazione.

### Update DL-MOL-006 — Zfra dopo full text Lee 2017
- **Status:** resta open/flagged · **Belief:** basso-medio → basso per trasferimento terapeutico.
- **Nuovo dato:** Zfra4–10 migliora memoria/riduce aggregati nel 3×Tg-AD con numeri piccoli e reporting incoerente; peptide non rilevato nel cervello, cross-linka/accelera degradazione proteica non selettiva e fallisce se iniziato più tardi.
- **Safety:** possibile riduzione di WWOX residuo + target/off-target ignoti. Non sale a Layer 9; solo probe con proteomica/LC-MS e controlli isogenici.

### Lead molecole parcheggiati
- **Evodiamina (PMID 28708106):** `parked`; aumenta WWOX protein in modelli HCC, ma l'effetto è citotossico, solo parzialmente WWOX-dipendente, senza target engagement/BBB/PK/safety pediatrica. Potrebbe aumentare Q230P misfolded.
- **Digossina (PMID 29724996):** `not-a-il genotipo di riferimento-candidate`; rescue HIF1α in oncologia epatica cronica, finestra terapeutica/cardiotossicità incompatibili con estrapolazione.
- **Paclitaxel/KIRA6/GSK2656157:** probe oncologici/UPR, non repurposing per WWOX-DEE.

### Change-log 2026-07-09
- Aggiunti DL-BIO-005/006 e DL-MECH-023/024/025; aggiornato Zfra; parcheggiate evodiamina/digossina/paclitaxel-axis.
- Dossier: `staging/batch50_branch_A_dossier.md`, `batch50_branch_B_dossier.md`, `batch50_branch_C_dossier.md`.

---

## Run 2026-07-09 — lead dal batch 50-studi WWOX 2015–2016 (autopilota, "l'oro è nei dettagli")

> Batch a maggioranza oncologica (cancer/apoptosis/fragile-site). Triage: 0 già deep-dived, 34 CORPUS_CATALOGUED, 5 NEW, 11 OUT_OF_SCOPE_LIKELY. 12 full-text letti integralmente. **Il rendimento più alto è venuto dai paper etichettati "rumore"** (Alzheimer, zebrafish, Drosophila, farmacogenomica pancreatica). Read-only sui 4 current; promozione solo via CC.

### DL-MECH-019 — Q230 cade nel dominio SDR che media il binding a tau/GSK3β/TPC6AΔ: catalisi intatta ≠ funzione conservata
- **Status**: open · **Tag**: DATO (mappa di binding) + IPOTESI (estensione a Q230P)
- **Fonte**: Chang JY & Chang NS 2015, Cell Death Discov (PMID 27551439, PMC4981022); Chang JY et al. 2015, Oncotarget (PMID 25650666, PMC4414138); Sze CI et al. 2015, Cell Death Dis (PMID 26355344, PMC4650446)
- **Finding (DATO)**: TPC6AΔ lega WWOX sul **tail C-terminale D3 / dominio SDR (aa 120–414)**, **non** sui domini WW (aa 1–95) — mappato via FRET. La co-espressione di WWOX **sopprime ~50%** l'aggregazione di TPC6AΔ. Anche **tau e GSK3β** legano WWOX via SDR (ERK/JNK1 via WW). Gli autori scrivono esplicitamente: *"WWOX may act as a chaperone, which stabilizes proteins from misfolding and being degraded by the ubiquitin/proteasome system."*
- **Statement causale**: `WWOX_SDR —binds→ {TPC6AΔ, tau, GSK3β} —prevents→ aggregation`; (IPOTESI) `Q230P —destabilizes SDR→ loss of anti-aggregation scaffold function`
- **Rilevanza di malattia / implicazione**: **rovescia una nostra assunzione implicita.** Finora la triade catalitica intatta (Ser281/Tyr293/Lys297) in Q230P era letta come "il sito attivo funziona, basta stabilizzare". Questi dati mostrano che nel SDR risiede anche una funzione **non catalitica di scaffold/anti-aggregazione**: una destabilizzazione del fold SDR può abolire il *binding* pur lasciando intatta la *catalisi*. → il rescue proteostatico di Q230P mira a recuperare **due** funzioni distinte, e il readout non può essere solo l'attività ossidoreduttasica. **Belief**: medio-alto sul binding (DATO, ma singolo laboratorio, over-espressione ectopica); medio sull'estensione a Q230P.
- **Esperimento**: co-IP/FRET WWOX-WT vs WWOX-Q230P × TPC6AΔ e × tau → il binding SDR sopravvive alla destabilizzazione? Se no, l'assay di binding diventa il readout funzionale primario di Q230P (più informativo dell'attività SDR).
- **Interconnessioni**: [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]] (readout Q230P: aggiungere binding, non solo attività), [[discovery_ledger_current#DL-MECH-017 — WW2 come chaperone intramolecolare che stabilizza WW1 (rinforza il razionale stabilizzatori/proteostasi)|DL-MECH-017]] (chaperoning intramolecolare WW2→WW1), [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]], [[meta_prenatal_structure_current]] (asse GSK3β/tau)

> #### 🔧 UPGRADE 2026-07-26 — fonte primaria acquisita per l'arco GSK3β; arco *tau* dichiarato non contraddetto
> *Testo originale sopra invariato. Questo blocco lo raffina, non lo sostituisce.*
>
> - **Arco GSK3β → da secondario a `DATO` risolto a livello di residuo.** Fonte primaria letta integralmente: **Wang et al. 2012, PMID 22193544 / PMC3354054** (`PAPER 056` proposto in `CC-20260726-003`; ricevuta `FTR-20260726-22193544-01`). Il legame **non** usa genericamente «il SDR»: richiede il segmento **388–407**, omologo al motivo di docking Axin-GID/FRAT1/GSKIP, con **L404 strettamente necessario**. `L404A` abolisce il legame (pull-down GST *e* co-IP cellulare), abolisce l'inibizione della chinasi in vitro e in cellula, abolisce il recupero dell'assemblaggio dei microtubuli e abolisce il beneficio sul differenziamento; il vicino `L311A` non fa nulla di tutto questo. Le troncature Δ286 e Δ389 non legano. Il co-IP reciproco fra **proteine endogene in estratto di cervello di topo** è il dato più fisiologico del lavoro.
> - **Conseguenza per il readout di Q230P.** Q230 dista **174 residui** da L404: una perdita di legame in Q230P riporterebbe **collasso globale del fold SDR**, non una lesione locale d'interfaccia. È quindi il readout che serve alla domanda di [[claim_registry_current#CLAIM 030]] (*la proteina salvata è funzionale?*), ed è più definito dell'attività ossidoreduttasica, il cui substrato fisiologico resta ignoto. **Set di controlli disponibile senza nuovi reagenti:** `L404A` positivo di perdita, **G372R** negativo naturale (fenotipo lieve) che siede 16 residui a monte del motivo e funge quindi anche da controllo di prossimità, `Q230P` la domanda.
> - 🔴 **Arco *tau*: NON contraddetto.** Wang 2012 afferma nel testo che WWOX non lega Tau, ma la sua Supplementary Figure A **non contiene alcun blot Tau** (pannelli etichettati WWOX e GSK3β). Il negativo è **non valutabile** → `DIS-010` e **D-14**. L'arco *tau* di questa voce **resta in piedi**, con la nota che *nessuno dei due lati è solido*: Chang/Sze lo affermano da yeast two-hybrid, Wang lo nega senza mostrare il dato. Controparte da leggere: [[full_text_queue_current#FT-024]].
> - **Vincolo di design che ne deriva.** Il degrone canonico **ERLIQ 402–406 contiene L404**, cioè un residuo richiesto da una funzione dimostrata. Il missing-info #7 del red-team Q230P (*«residue-level confirmation… cited but not verified»*) è **CHIUSO: confermato**. Qualunque ligando che stabilizzi WWOX agganciando ERLIQ rischia di **recuperare abbondanza abolendo funzione** → istanza nuova e indipendente di **D-04**.
> - **Tag**: arco GSK3β `DATO` (biochimica, cinque saggi ortogonali, una singola mutazione puntiforme) · trasferimento a Q230P `IPOTESI` (mai testato) · arco tau `INDETERMINATO`.

### DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica
- **Status**: open · **Tag**: DATO (modello cancro/MEF) + IPOTESI (trasferimento al neurone del genotipo di riferimento)
- **Fonte**: Abu-Remaileh M, Seewaldt VL, Aqeilan RI 2015, Mol Cell Oncol (PMID 27308416, PMC4904998) — commentary; dati primari in Abu-Remaileh & Aqeilan 2014, Cell Death Differ (PMID 25012504, **da acquisire**)
- **Finding (DATO)**: MEF Wwox-KO (cell-autonomous): ↑uptake glucosio, ↑lattato, ↑NADPH, ↓NADH, **↓ATP, ↓consumo O₂** → shift verso glicolisi aerobica con **soppressione della respirazione mitocondriale**. **HIF1α è aumentato in normossia**. WWOX lega HIF1α via **WW1**, ne sopprime la transattivazione e ne favorisce la degradazione. L'inibizione di HIF1α (genetica *e* farmacologica) **reverte** l'uptake di glucosio in vitro e in vivo. Wwox-KO murino: letalità postnatale ~4 settimane con **ipoglicemia**.
- **Statement causale**: `WWOX_loss —derepresses→ HIF1α —induces→ {GLUT1↑, PDK↑} —inhibits→ PDH —blocks→ piruvato→TCA` ⇒ deficit bioenergetico ossidativo
- **Rilevanza di malattia / implicazione**: **il lead più azionabile e a più basso rischio del batch.** Se il neurone WWOX-carente ha lo stesso blocco all'ingresso del piruvato nel TCA (PDK↑ ⊣ PDH), la **dieta chetogenica bypassa esattamente quel collo di bottiglia**: i corpi chetonici entrano nel TCA come acetil-CoA **a valle di PDH**, senza passare per la glicolisi. La KD è già standard-of-care nelle encefalopatie epilettiche → qui acquisirebbe un **razionale meccanicistico WWOX-specifico**, non solo empirico-antiepilettico. Convergenza ulteriore: **GLUT1** (inversamente correlato a WWOX) — e la GLUT1-deficiency è essa stessa un'encefalopatia trattata con KD. **Belief**: medio-alto sul meccanismo in MEF/cancro; medio sul trasferimento al neurone (non testato in tessuto neurale). **Non è parere medico**: è un razionale da portare al team curante.
- **Esperimento**: (1) Seahorse OCR/ECAR su fibroblasti o LCL del genotipo di riferimento vs controllo → il rapporto glicolisi/OXPHOS è spostato? (2) lattato/piruvato plasmatico e **lattato cerebrale via MRS**; (3) HIF1α e GLUT1 in fibroblasti donor-derived.
- **Interconnessioni**: [[meta_metabolism_current]], [[discovery_ledger_current#DL-MECH-021 — Perdita di wwox altera in vivo le dinamiche del Ca²⁺; il rescue riesce col solo dominio SDR/ADH|DL-MECH-021]] (Ca²⁺/energia), [[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]], [[clinical_monitoring_endpoints_current]]
- ⚠️ **Cautela credibilità**: il ramo HIF1α/WWOX è stato lavorato anche dal gruppo Bendinelli/Desiderio (CORPUS P396, Eur J Cancer 2013), oggi in watchlist per ritrattazioni seriali → non usare quella linea come corroborazione indipendente. Vedi *research-group knowledge base (not published)*.

### DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore
- **Status**: open · **Tag**: DATO (assay esistente e validato in altro contesto) + IPOTESI (uso sul genotipo di riferimento) · **Cosa si misura**: rapporto trascritto-esone8/9 su trascritto-core · **Matrice**: fibroblasti/LCL donor-derived · **Vicinanza a WWOX**: massima → candidato **Tier 1/2**
- **Fonte**: Schirmer MA et al. 2016, J Natl Cancer Inst (PMID 26857392, PMC4859408) — il paper metodologicamente più solido del batch (n=381, 89 LCL, EMSA+supershift+siRNA)
- **Finding (DATO)**: gli autori quantificano separatamente i **trascritti della giunzione esone 8→esone 9** e i **trascritti core (esoni 4–6)**, con rapporto ~67% e correlazione intra-linea r=0.68 (r=0.80 sotto gemcitabina). Documentano inoltre trascritti alternativi che **terminano dentro l'introne 8** (introne lungo 778.856 bp).
- **Rilevanza di malattia / implicazione**: **coincidenza anatomica notevole.** L'allele di sito accettore del genotipo di riferimento, `c.1057-2A>G`, è esattamente la **perdita dell'accettore dell'esone 9**, cioè il confine introne 8/esone 9 — la stessa giunzione che questo assay quantifica. Esiste dunque **già un assay pubblicato e validato** che misura ciò che ci serve: quanta frazione di trascritto WWOX include correttamente l'esone 9. Questo dà (a) un **biomarcatore di stato dell'allele di sito accettore**, (b) un **endpoint di efficacia per un eventuale ASO splice-correcting** (TX-001): se l'ASO funziona, il rapporto esone8-9/core deve salire. **Belief**: alto sull'esistenza dell'assay; medio sulla trasferibilità diretta (loro misurano espressione, non splicing aberrante — servono primer che spannino la giunzione e un controllo NMD, es. inibizione con cicloesimide).
- **Esperimento**: RT-qPCR con primer sulla giunzione es8/es9 + primer core es4-6 su fibroblasti/LCL variant-carrying vs controlli sani, ± inibitore di NMD (cicloesimide/SMG1i) per smascherare il trascritto degradato dell'allele di sito accettore. Affiancare RNA-seq per caratterizzare l'evento di splicing reale (exon skipping vs intron retention vs sito criptico +8 già predetto da SpliceAI).
- **Interconnessioni**: [[discovery_ledger_current#DL-BIO-002 — Trascritto/proteina dell'allele di sito accettore, nominati dalla predizione di skipping esone 9 (SpliceAI/Pangolin)|DL-BIO-002]] (allele di sito accettore), [[therapeutic_strategies_current#TX-001 — Correcting a canonical splice-acceptor allele: RNA assay → ASO/editing choice|TX-001]] (ASO splice-correcting: **questo è il suo endpoint**), [[biomarker_candidates_current]]

### DL-BIO-004 — pTyr33-WWOX come readout dello stato funzionale, con batteria a valle di aggregati
- **Status**: open · **Tag**: DATO (in tessuto umano post-mortem e KO murino) + IPOTESI (fluidi pediatrici)
- **Fonte**: Chang JY et al. 2015, Oncotarget (PMID 25650666, PMC4414138)
- **Finding (DATO)**: **pTyr33-WWOX aggregato è ridotto ~40%** nei cervelli Alzheimer vs controlli non-dementi (n=42 controlli / 96 AD); metodo = **filter retardation assay + SDS-PAGE non riducente**. A valle, cascata sequenziale misurabile: **pSer35-TPC6AΔ → TIAF1 → caspasi-3 → APP → Aβ → pT181-tau**. Nel **Wwox-KO murino a 3 settimane** (null completo, muore <1 mese) compaiono già aggregati extracellulari di TPC6AΔ in corteccia e **pT181-tau significativamente aumentato** (n=5).
- **Rilevanza di malattia / implicazione**: due cose distinte. (1) **pTyr33-WWOX** è il candidato più vicino a una misura *diretta* dello stato funzionale di WWOX (Tyr33 è conservato anche in zebrafish). (2) La cascata di aggregazione **si accende già a 3 settimane nel null dello sviluppo**, non solo nell'invecchiamento → è un processo **tempo-sensibile e pediatrico**, quindi dentro la finestra d'azione della missione. Le sequenze peptidiche dei 5 anticorpi custom sono pubblicate nel paper (riusabili). **Belief**: medio (singolo laboratorio, biologia di TPC6AΔ quasi esclusiva di questo gruppo, non replicata indipendentemente); nessuna evidenza che questi marcatori siano dosabili in CSF/plasma pediatrico.
- **Esperimento**: pTyr33-WWOX e aggregati su fibroblasti/LCL del genotipo di riferimento; se positivo, valutare fattibilità su CSF residuo. Prima però: **replica indipendente** della biologia TPC6AΔ, che oggi manca.
- **Interconnessioni**: [[discovery_ledger_current#DL-MECH-019 — Q230 cade nel dominio SDR che media il binding a tau/GSK3β/TPC6AΔ: catalisi intatta ≠ funzione conservata|DL-MECH-019]], [[biomarker_candidates_current]], [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]]

### DL-MECH-021 — Perdita di wwox altera in vivo le dinamiche del Ca²⁺; il rescue riesce col solo dominio SDR/ADH
- **Status**: open · **Tag**: DATO (zebrafish) + IPOTESI (crisi del genotipo di riferimento)
- **Fonte**: Tsuruwaka Y, Konishi M, Shimada E 2015, PeerJ (PMID 25649963, PMC4312067)
- **Finding (DATO)**: knockdown di wwox in zebrafish (morpholino ATG-blocking, n=2460; siRNA, n=2590) → **edema pericardico** (penetranza 56%/62%), morte entro 1 settimana, e **dinamiche di Ca²⁺ intracellulare marcatamente alterate** misurate in vivo con il reporter FRET **Yellow Cameleon YC2.12** a 30 hpf. **Il rescue (n=770) riesce co-iniettando mRNA del solo dominio ADH/SDR** non-targettabile. Omologia wwox zebrafish/umano 72%; Tyr33 conservato; SDR aa 121–330.
- **Statement causale**: `wwox_loss —dysregulates→ intracellular_Ca²⁺_dynamics`; `SDR_domain_alone —sufficient_to_rescue→ edema_phenotype`
- **Rilevanza di malattia / implicazione**: tre aghi in uno. (1) **Ca²⁺ è il substrato fisico dell'eccitabilità di rete** → primo dato *in vivo* che lega la perdita di WWOX a una disregolazione del calcio, cioè un ponte meccanicistico verso le crisi. La Discussion cita il **ratto *lde*** (mutazione Wwox → nanismo letale + **epilessia e crisi audiogeniche**, Suzuki 2009) — paper **da acquisire, non a registro**. (2) Il fatto che **il solo dominio SDR basti al rescue** è un argomento a favore del fatto che recuperare la funzione SDR (dove siede Q230P) sia terapeuticamente rilevante — cross-species, quindi debole, ma direzionalmente coerente. (3) **Piattaforma di screening pronta**: morfante + imaging Ca²⁺ + edema + rescue già validato = si può testare se un chaperone chimico o un modulatore metabolico normalizza il fenotipo. **Belief**: medio (Ca²⁺ descritto qualitativamente, senza ampiezza/frequenza/latenza; morpholino = tossicità off-target nota, ma qui mitigata da siRNA indipendente + rescue).
- **Esperimento**: riprodurre il morfante con Ca²⁺-imaging quantitativo; screenare stabilizzatori/chaperoni per rescue; esprimere **wwox-Q230P umano** nel morfante → rescue parziale o assente? Sarebbe il primo test funzionale in vivo dell'allele del genotipo di riferimento.
- **Interconnessioni**: [[meta_gaba_paradox_current]], [[meta_network_myelin_glia_current]], [[discovery_ledger_current#DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica|DL-MECH-020]], [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013]]

### DL-MECH-022 — Posizionamento genotipo-fenotipo: il genotipo di riferimento sta tra il null puro (WOREE) e l'ipomorfo (SCAR12)
- **Status**: open · **Tag**: DATO (fenotipi pubblicati) + IPOTESI (posizionamento del genotipo di riferimento)
- **Fonte**: Elsaadany L et al. 2016, BMC Med Genet (PMID 27495153, PMC4975905) — W44X omozigote, famiglia consanguinea, 2 sorelle; Table 1 = confronto genotipo-fenotipo su 6 famiglie
- **Finding (DATO)**: nel **null biallelico puro** (W44X = p.Trp44Stop, nonsense esone 2, NMD predetta): esordio crisi a **7 settimane** in entrambe le sorelle; **fenobarbitone, clonazepam, fenitoina, levetiracetam tutti falliti** nel primo caso (topiramato/clobazam → risposta *parziale* nella sorella); **scarsa mielinizzazione già a 9 settimane**, assente a 23 settimane, **demielinizzazione progressiva**; assottigliamento del corpo calloso; atrofia fronto-temporale; **nessuna microcefalia** (OFC +0.37 SD); pallore dei dischi ottici con **ERG normale**; workup metabolico e mitocondriale **interamente normale**. Table 1: i **missense/ipomorfi** (SCAR12) hanno invece esordio crisi a **9–12 mesi**, atassia cerebellare, e **migliore risposta agli antiepilettici**.
- **Rilevanza di malattia / implicazione**: **l'inferenza-cardine di questo batch.** il genotipo di riferimento è compound eterozigote: un allele **null-like** di sito accettore + un allele **missense** che *produce proteina*. Il suo assetto la colloca **fra** i due estremi della Table 1. Se Q230P conserva o può recuperare funzione residua — cioè se l'ipotesi misfolding-dominance è vera e c'è margine di rescue — allora lo **shift atteso è verso l'estremo SCAR12**: esordio più tardivo, decorso meno fulminante, **migliore risponsività agli antiepilettici**. È precisamente il razionale operativo della missione: il parziale conta, e la funzione residua è la variabile su cui si può agire. **Belief**: medio-alto sulla direzione (convergenza tra Table 1 e la logica dose-di-funzione); N piccolo, W44X mai validato funzionalmente (NMD solo predetta).
- **Corollari operativi**: (a) la **mielinizzazione si degrada già a 9 settimane nel null** → è la variabile tempo-sensibile per eccellenza, e la protezione della finestra mielinica è prioritaria *ora*, indipendentemente da qualunque leva su WWOX; (b) **endpoint EEG concreti** emersi: perdita degli elementi del sonno, background discontinuo nel sonno, conteggio spasmi/ora su EEG 24h, VEP ritardato con ERG normale; (c) **gap terapeutico**: in nessuno dei casi W44X risultano documentati vigabatrin, ACTH, cannabidiolo o dieta chetogenica → la letteratura sul null non ha mai testato le leve che a noi interessano.
- **Interconnessioni**: [[claim_registry_current#CLAIM 019]], [[meta_human_spectrum_current]], [[meta_network_myelin_glia_current]], [[discovery_ledger_current#DL-MOL-007 — Fallimento sistematico degli ASM sintomatici in WOREE severo → priorità alle leve disease-modifying|DL-MOL-007]] (fallimento ASM sintomatici), [[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]]

### DL-MOL-008 — Peptide pTyr33-WWOX: un candidato di "restoration" già testato in vivo su un modello neurologico
- **Status**: open · **Tag**: ESPANSIONE (da inseguire alla fonte primaria)
- **Fonte**: Sze CI et al. 2015, Cell Death Dis (PMID 26355344, PMC4650446) — commentary; **fonte primaria da acquisire**: Lo CP et al. 2008, Eur J Neurosci (PMID 18371080)
- **Finding (citato, non originale)**: *"A small **Tyr33-phosphorylated WWOX peptide**, which mitigates **MPP+-mediated Parkinson-like syndrome in rats**, may be of therapeutic use in the restoration of neural function under WWOX deficiency in vivo."*
- **Rilevanza di malattia / implicazione**: è l'unico puntatore terapeutico **esplicito e già testato in un animale con fenotipo neurologico** emerso da tutto il batch. Un peptide-mimetico che ripristina un segnale WWOX-dipendente aggirerebbe il problema della variante (non serve correggere l'allele: si sostituisce la funzione a valle). **Belief**: basso-medio — il dato è su MPP+/Parkinson, non su WWOX-null; il commentary non riporta dose, via di somministrazione, né penetrazione BBB. Da non presentare come opzione: è una traccia bibliografica da chiudere. **Nessuna falsa speranza.**
- **Esperimento / prossimo passo**: recuperare il full-text di Lo 2008 (PMID 18371080) → dose, via, BBB, durata dell'effetto, controlli. Se il peptide è attivo per via periferica, diventa un lead serio; altrimenti resta ESPANSIONE.
- **Interconnessioni**: [[full_text_queue_current]] (FT da creare), [[therapeutic_hypotheses_ledger_current#HYP-20260709-04 — Peptide pTyr33-WWOX come rescue funzionale a valle della variante|HYP-20260709-04]]

---

## Failure mode registrati (run 2026-07-09)

- **FM-006 — Lo sweep inferenziale non rileva le ritrattazioni.** `batch_inferential_sweep.py` ha rankato **Bendinelli 2015 (PMID 26041563), paper RITRATTATO per manipolazione di western blot**, come `CANONICAL_CANDIDATE` al rank #12, tier P1_HIGH. Il `paper_registry` lo aveva già correttamente confinato (`CORPUS P303`, `Role: background corpus only`, `Claim links: none`) → **nessun claim canonico è stato contaminato**, ma il gate a monte era cieco. → risolto con `retraction_check.py` cablato nel triage (vedi capability log).
- **FM-007 — `OUT_OF_SCOPE_LIKELY` è keyword-based sul titolo e produce falsi negativi gravi.** Lo script ha marcato out-of-scope *"Bubbling cell death"*, *"TRAPPC6AΔ is an extracellular plaque-forming protein in the brain"* e *"UV/cold shock..."* perché "WWOX" non compare nel titolo — ma sono tutti lavori del lab Chang su meccanismi **WWOX-dipendenti nel cervello**, e uno di essi ha prodotto **DL-BIO-004**. La regola "OUT_OF_SCOPE ≠ out-of-discovery" non è una formalità: è ciò che ha salvato tre aghi in questo run.
- **FM-008 — Input one-record-per-line senza righe vuote collassa in un singolo record.** `study_dedup_triage.py` → `split_pubmed_clipboard_blocks()` splitta su `\n\s*\n+`; un file con 50 studi su 50 righe contigue produce **1 solo record** con 50 PMID, silenziosamente. Il primo triage di questo run ha restituito "1 CORPUS_CATALOGUED" ed è stato riconosciuto come bug prima di procedere. → guardia aggiunta.

---

## Run 2026-07-09b — chiusura dei 3 gap (FT-018/019/020) + una correzione a un lead di questo stesso run

> Acquisiti: Abu-Remaileh & Aqeilan 2014 (dati primari HIF1α, via PMC web) e Tochigi 2019 (full-text, PMC6678113). Suzuki 2009 e Lo 2008 restano paywalled (Wiley, HTTP 402) → abstract PubMed usati come fonte primaria, con la cautela che ne consegue.

### Update DL-MOL-008 — CORREZIONE: il peptide pTyr33-WWOX **non** è una "restoration", è un inibitore
- **Status**: open → **`refuted` (nella lettura "restoration")** · **Tag**: la correzione è `DATO` (abstract della fonte primaria)
- **Cosa era stato registrato**: Sze 2015 (commentary) affermava che il peptide pTyr33-WWOX *"may be of therapeutic use in the **restoration** of neural function under WWOX deficiency in vivo"*. L'avevo registrato come unico puntatore terapeutico esplicito del batch.
- **Cosa dice la fonte primaria** (Lo CP et al. 2008, *Eur J Neurosci* 27:1634-46, PMID 18371080, [DOI](https://doi.org/10.1111/j.1460-9568.2008.06139.x), via PubMed): *"activated WOX1 plays an **essential role in the MPP+-induced neuronal death**"*. WOX1 fosforilato in Tyr33 è **pro-apoptotico**: è il mediatore della morte neuronale, non il suo antidoto. Il peptide sintetico pTyr33 (11 aa) **blocca** la morte — dunque agisce da **competitore/inibitore** della funzione pro-apoptotica di WOX1, coerentemente col fatto che il dominante-negativo WOX1 (che inibisce la fosforilazione di Tyr33) abolisce l'apoptosi.
- **Perché conta**: il genotipo di riferimento è **carente** di WWOX. Un composto che **inibisce** la funzione WWOX-dipendente non "ripristina" nulla in un contesto di deficit. Il razionale "restoration" **cade**. Il peptide potrebbe conservare un interesse come neuroprotettore generico (blocca una via di morte neuronale a valle), ma questo è un *altro* meccanismo, non testato in WWOX-deficiency, e non è ciò che il commentary lasciava intendere.
- **Lezione di metodo → [[discovery_ledger_current#^fm-010|FM-010]]**: un commentary che riassume un primario può ribaltarne il senso. Non promuovere mai un lead terapeutico da un commentary senza leggere il primario. Il gate ha funzionato: il lead era registrato come `ESPANSIONE`, `Belief: basso-medio`, "traccia bibliografica, non un'opzione". **Nessuna falsa speranza è stata generata.**
- **Nota d'onestà**: il full-text di Lo 2008 è paywalled (Wiley 402). La correzione poggia sull'**abstract**, che però è esplicito e non ambiguo. Se il full-text mostrasse un meccanismo diverso, va riaperto.

### DL-MECH-026 — Il ratto *lde* è il proxy animale dell'allele di sito accettore del genotipo di riferimento: lesione dell'esone 9 → proteina assente + epilessia audiogenica nel 95%
- **Status**: open · **Tag**: DATO (ratto) + INFERENZA (trasferimento al genotipo di riferimento)
- **Fonte**: Suzuki H et al. 2009, *Genes Brain Behav* 8(7):650-60 (PMID 19500159, [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x)) — **abstract PubMed, full-text paywalled**; corroborato dal full-text di Tochigi Y et al. 2019, *Int J Mol Sci* 20(14):3596 (PMID 31340538, PMC6678113, [DOI](https://doi.org/10.3390/ijms20143596))
- **Finding (DATO)**: il ratto *lde/lde* porta una **delezione di 13 bp nell'esone 9 di Wwox** (`c.1190_1202del`, frameshift `p.Leu371Thrfs*53`). Western blot: **mRNA mutante presente, proteina non rilevabile** in testicoli e ippocampo (solo una bandina debolissima a 46.2 kDa, mutante instabile). Fenotipo: nanismo, letalità postnatale, ipogonadismo maschile, **vacuoli in ippocampo e amigdala**, e **crisi audiogeniche nel 95% degli animali** (wild running → convulsioni tonico-cloniche), con EEG che mostra spike interictali, onde rapide durante il wild running e burst di spike nella fase clonica. Wwox è espresso nel SNC.
- **Dato aggiuntivo da Tochigi 2019 (DATO)**: l'**eterozigote `+/lde` esprime circa metà proteina**, con banda di peso molecolare normale.
- **Rilevanza di malattia / implicazione**: **è il modello genotipicamente più vicino all'allele di sito accettore del genotipo di riferimento che esista.** l'allele di sito accettore colpisce l'accettore dell'esone 9; *lde* è una delezione intra-esonica dello stesso esone. Eventi molecolari diversi, **stesso esone e stesso esito proteico: nessuna proteina funzionale**. Questo (a) **corrobora indipendentemente** che il lato splice-null del genotipo di riferimento sia null-like a livello proteico — finora era una predizione in-silico (SpliceAI/MaxEntScan); (b) fornisce un **modello vivente con fenotipo epilettico WWOX-dipendente** su cui testare leve; (c) l'epilessia **audiogenica** e i vacuoli ippocampo/amigdala sono un fenotipo di rete concreto, non un'astrazione.
- **Belief**: alto sul dato (WB + mappatura genetica), medio-alto sul trasferimento (specie diversa; la classe di riferimento è null/missense mentre il ratto è null biallelico → il ratto modella il *lato splice-null*, **non** l'allele missense).
- **Esperimento**: esprimere `WWOX-Q230P` umano nel background *lde/lde* → rescue parziale o assente? Sarebbe il primo test funzionale in vivo dell'allele missense del genotipo di riferimento, sul fondo genetico che modella il lato splice-null.
- **Interconnessioni**: [[discovery_ledger_current#DL-BIO-002 — Trascritto/proteina dell'allele di sito accettore, nominati dalla predizione di skipping esone 9 (SpliceAI/Pangolin)|DL-BIO-002]], [[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]] (assay esone 9), [[therapeutic_strategies_current#TX-001 — Correcting a canonical splice-acceptor allele: RNA assay → ASO/editing choice|TX-001]] (ASO), [[discovery_ledger_current#DL-MECH-021 — Perdita di wwox altera in vivo le dinamiche del Ca²⁺; il rescue riesce col solo dominio SDR/ADH|DL-MECH-021]] (Ca²⁺ zebrafish), [[meta_gaba_paradox_current]]
- ⚠️ **Il *lde* NON è informativo sulla leva ASO**: è una delezione, non un difetto di splicing. Conferma però che "salvare l'esone 9" è il bersaglio giusto.

### DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile
- **Status**: open · **Tag**: DATO (ratto) + INFERENZA (natura del difetto) + IPOTESI (reversibilità)
- **Fonte**: Tochigi Y et al. 2019, *Int J Mol Sci* (PMID 31340538, PMC6678113) — **full text letto integralmente**
- **Finding (DATO)**, corteccia cerebrale, PND 5/10/15/21:
  - **Numero di neuroni, spessore corticale e distribuzione per strato: NESSUNA differenza** rispetto al wild-type. Wwox non serve a proliferazione né migrazione neuronale.
  - **MAP2 significativamente ridotto a tutte le età** → **crescita neuritica compromessa**, con neuroni presenti.
  - **MBP e CNPase severamente ridotti (PND 5-21)**; **oligodendrociti maturi (APC/CC1) ridotti (PND 15-21)**, sia in corteccia sia nel corpo calloso.
  - Astrociti (GFAP) e microglia (Iba1) ridotti. **Wwox è espresso in neuroni, astrociti e oligodendrociti, ma NON in microglia** (primo report su oligodendrociti) → il calo della microglia è verosimilmente secondario.
  - Wwox **aumenta con l'età** nel prosencefalo da PND5 a PND21 (la mielinizzazione del ratto va da PND10 al picco a PND20).
- **Rilevanza di malattia / implicazione**: due aghi.
  1. **"C'è ancora substrato da salvare."** Il danno non è morte neuronale ma **maturazione e connettività**: neuroni presenti, neuriti corti, mielina scarsa. È esattamente il tipo di danno su cui una leva di protezione-finestra può mordere. Converge con [[discovery_ledger_current#DL-MECH-022 — Posizionamento genotipo-fenotipo: il genotipo di riferimento sta tra il null puro (WOREE) e l'ipomorfo (SCAR12)|DL-MECH-022]] (nel W44X umano la mielinizzazione è persa già a 9 settimane).
  2. ⚠️ **Il gap sperimentale più prezioso oggi identificabile.** Il paper misura gli oligodendrociti **maturi** (APC/CC1) ma **NON conta i precursori** (nessun NG2, PDGFRα, Olig2). Quindi **non distingue** tra *arresto della maturazione degli OPC* (precursori presenti che non differenziano) e *perdita/aplasia dei precursori*. **La differenza è terapeuticamente decisiva**: nel primo caso esistono pro-mielinizzanti che agiscono proprio sbloccando il differenziamento degli OPC (clemastina, benztropina, miconazolo, T3, quetiapina); nel secondo caso non c'è nulla da sbloccare. Gli indizi interni (neuroni normali, difetto di differenziamento, ipomielinizzazione attribuita anche alla ritardata crescita assonale) **inclinano** verso l'arresto di maturazione, ma **non lo dimostrano**.
- **Belief**: alto sui DATI (istologia + WB, marcatori standard); **medio-basso** sull'inferenza arresto-vs-perdita, che resta aperta.
- **Esperimento (il più prezioso da fare/cercare)**: conta OPC (NG2/PDGFRα/Olig2) nella corteccia *lde/lde*, + saggio di differenziamento in vitro di OPC *lde/lde* ± pro-mielinizzante. Chiude il gap e apre (o chiude) un'intera leva terapeutica.
- **Limiti**: ratto, solo maschi, N≈3+3 per stadio, nessun dato oltre PND21, effect size non riportati nel testo (solo soglie di significatività). **Contrasto dichiarato con Hussain 2019** (KO murino: gliosi/attivazione microgliale nell'ippocampo) vs qui (riduzione di GFAP/Iba1 in corteccia) → **il segno del fenotipo gliale/neuroinfiammatorio è regione- e modello-dipendente**. Non assumere una direzione unica per il genotipo di riferimento.
- **Reagenti riusabili**: anti-Wwox Sigma **HPA050992** (epitopo aa 32-110, 100% identico nel ratto); APC clone CC-1; MBP clone 1; CNP clone 11-5B; NeuN A60.
- **Interconnessioni**: [[meta_network_myelin_glia_current]], [[discovery_ledger_current#DL-MECH-022 — Posizionamento genotipo-fenotipo: il genotipo di riferimento sta tra il null puro (WOREE) e l'ipomorfo (SCAR12)|DL-MECH-022]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-07 — Pro-mielinizzanti per la finestra mielinica, **condizionata a un esperimento che nessuno ha ancora fatto**|HYP-20260709-07]]

### DL-MECH-028 — WWOX lega HIF1α via **WW1**, non via SDR: l'asse metabolico potrebbe essere parzialmente preservato in Q230P
- **Status**: open · **Tag**: DATO (dati primari) + IPOTESI (implicazione per Q230P)
- **Fonte**: Abu-Remaileh M & Aqeilan RI 2014, *Cell Death Differ* 21(11):1805-14 (PMID 25012504, PMC4211377, [DOI](https://doi.org/10.1038/cdd.2014.95)) — **full text letto via PMC**
- **Finding (DATO)**: GST-pulldown → **solo i costrutti contenenti il dominio WW1 precipitano HIF1α**. Il mutante **GST-WWOX-WFPA (W44F + P47A, nel WW1)** **non lega** HIF1α. Co-IP conferma l'interazione endogena (HEK293 + MG132). In normossia HIF1α è **appena rilevabile nel WT ma abbondante nei Wwox-KO**; in ipossia WWOX non ne modifica i livelli.
- **Rilevanza di malattia / implicazione**: **Q230P è nel dominio SDR, non nel WW1.** Se il legame a HIF1α richiede WW1 e Q230P lascia WW1 strutturalmente intatto, allora **la funzione anti-HIF1α dell'allele missense potrebbe essere parzialmente conservata** — a patto che la proteina esista e non sia degradata (che è precisamente il dubbio di [[claim_registry_current#CLAIM 019]]). Corollario: il fenotipo metabolico del genotipo di riferimento potrebbe essere **meno severo** di un null puro, e la severità dipenderebbe soprattutto dalla **quantità** di proteina Q230P residua, non dalla sua identità catalitica. Da tenere accanto al fatto — opposto per direzione — che il **SDR** media il binding a tau/GSK3β/TPC6AΔ ([[discovery_ledger_current#DL-MECH-019 — Q230 cade nel dominio SDR che media il binding a tau/GSK3β/TPC6AΔ: catalisi intatta ≠ funzione conservata|DL-MECH-019]]): **Q230P colpisce la funzione scaffold, forse non quella anti-HIF1α**. Dissociazione funzionale testabile.
- **Curiosità che vale un flag**: il mutante usato per abolire il binding è **W44F/P47A**. **W44** è lo stesso residuo del nonsense **W44X** del case report ([[discovery_ledger_current#DL-MECH-022 — Posizionamento genotipo-fenotipo: il genotipo di riferimento sta tra il null puro (WOREE) e l'ipomorfo (SCAR12)|DL-MECH-022]]) e **P47** è lo stesso di **P47T** — variante che LEGEND aveva usato come banco di stabilità read-across, uso poi **ritirato**: resta un **comparator**, **non** una via di trasferimento ([[paper_registry_current#PAPER 007]]). Il paper dimostra dunque che **quei due residui sono funzionalmente critici per il binding a HIF1α** — un'evidenza indipendente della loro importanza. `INFERENZA`
- **Belief**: alto sul binding (pulldown + mutante + co-IP); medio sull'implicazione per Q230P (mai testata).
- **Esperimento**: co-IP WWOX-Q230P × HIF1α (il binding WW1 sopravvive?) + livelli di HIF1α in fibroblasti donor-derived.

### DL-BIO-007 — Lattato sierico, glicemia e insulina come biomarcatori metabolici in vivo del deficit di WWOX
- **Status**: open · **Tag**: DATO (topo) + IPOTESI (traslabilità) · **Cosa si misura**: lattato sierico, glicemia, insulina · **Matrice**: siero · **Tier**: 2-3 (distale, non WWOX-specifico)
- **Fonte**: Abu-Remaileh & Aqeilan 2014 (PMID 25012504, PMC4211377)
- **Finding (DATO, in vivo)**: topi Wwox-KO → **ipoglicemia letale**, **tutti morti entro 4 settimane**, **lattato sierico significativamente aumentato**, **insulina sierica ridotta** con isole pancreatiche normali. Nei MEF KO: uptake di glucosio ↑ (rescue con re-espressione di WWOX), lattato ↑, **ATP ↓**, **OCR ↓**, NADH ↓.
- **Geni bersaglio di HIF1α upregolati nei Wwox-KO (DATO, qRT-PCR)**: **GLUT1, PDK1, HK2, PKM2**, triosofosfato isomerasi, aldolasi, PFK-1.
- **Rilevanza di malattia / implicazione**: ⭐ **questo trasforma HYP-01 (dieta chetogenica) da inferenza a due salti in una catena con un anello misurato.** Finora l'asse era: `WWOX↓ → HIF1α↑` (DATO) → `HIF1α → PDK↑ → ⊣PDH` (biologia nota, **non misurata**). Ora **PDK1 è misurato come direttamente upregolato nei Wwox-KO**, insieme a GLUT1 e HK2. Il blocco all'ingresso del piruvato nel Krebs non è più solo plausibile: il suo enzima-chiave è sovraespresso. La dieta chetogenica bypassa esattamente quel punto.
- Il **lattato sierico elevato in vivo** offre un biomarcatore economico e già dosabile in clinica (attenzione: **aspecifico**, Tier 3 — non è un biomarcatore di stato di WWOX, è una conseguenza distale; da non collocare nel file biomarker Tier 1/2, pena `BLOCK_BATCH_COMMIT` per disciplina biomarker).
- **Belief**: alto sui dati murini; **medio-basso** sul trasferimento al genotipo di riferimento (il topo è null totale e muore di ipoglicemia a 4 settimane; il genotipo di riferimento no → il suo fenotipo metabolico è, se presente, molto più lieve).
- **Esperimento**: lattato/piruvato plasmatico e glicemia del genotipo di riferimento (probabilmente già disponibili in cartella); Seahorse OCR/ECAR su fibroblasti; **lattato cerebrale via MRS**.
- **Interconnessioni**: [[discovery_ledger_current#DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica|DL-MECH-020]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]], [[clinical_monitoring_endpoints_current]] (Tier 3, **non** biomarker Tier 1/2)

### DL-MOL-009 — Digossina reverte in vivo il fenotipo metabolico Wwox-dipendente. Farmaco approvato — e proprio per questo pericoloso
- **Status**: open · **Tag**: DATO (topo) + `SAFETY_SIGNAL`
- **Fonte**: Abu-Remaileh & Aqeilan 2014 (PMID 25012504, PMC4211377)
- **Finding (DATO)**: l'inibitore di HIF1α usato è la **digossina**, somministrata i.p. (dose riportata dal paper: 100 mg/kg — verosimile refuso per µg/kg, **da verificare sul PDF originale**: 100 mg/kg di digossina sarebbe una dose massivamente letale). Effetto: **aumento rapido e specifico della glicemia nei topi KO**, con riduzione dell'espressione di PDK1 e PHD3 nei KO ma non nei WT.
- **Rilevanza di malattia / implicazione**: è **l'unico farmaco già approvato che, in un modello Wwox-deficiente in vivo, corregge un fenotipo Wwox-dipendente.** Come prova di principio meccanicistica è forte: conferma che l'asse HIF1α è *farmacologicamente* aggredibile a valle della perdita di WWOX.
- 🔴 **BLOCCO 1 — bandiera rossa, non promuovibile**: la digossina è un glicoside cardiaco con **finestra terapeutica strettissima**, tossicità cardiaca e **neurologica** dose-dipendente, interazioni multiple, e nessun razionale a correggere il problema del genotipo di riferimento (che non è l'ipoglicemia). L'endpoint corretto nel topo era la glicemia; per il genotipo di riferimento l'endpoint sarebbe la bioenergetica neuronale — **non è lo stesso bersaglio clinico.** Serve `legend-safety-triage` prima di qualunque considerazione, e comunque **[[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]] (dieta chetogenica) domina**: stesso asse metabolico, sicurezza incomparabilmente superiore.
- **Uso corretto di questo lead**: come **validazione del bersaglio (HIF1α/PDK1)**, non come candidato terapeutico.
- **Da verificare**: la dose reale (µg vs mg) sul PDF originale.

---

## Failure mode registrati (run 2026-07-09b)

- **FM-009 — I termini MeSH non sono contenuto sperimentale.** Tochigi 2019 è indicizzato con *"Mitochondrial Diseases"*, *"Signal Transduction"* e *"Amino Acid Transport Systems, Acidic"* (EAAT/GLT-1). **Nessuno dei tre corrisponde a un esperimento nel paper**: sono indicizzazione automatica. Un sweep che pescasse "mitocondri" o "trasportatori del glutammato" da questi MeSH produrrebbe un lead **inesistente**. → I MeSH servono per *trovare* i paper, mai per *dire cosa contengono*. Corollario diretto della regola "il grep non è un metodo di analisi".
- **FM-010 — Un commentary può ribaltare il senso del primario che riassume.** Sze 2015 presentava il peptide pTyr33-WWOX come strumento di *"restoration of neural function under WWOX deficiency"*; la fonte primaria (Lo 2008) mostra che WOX1-pTyr33 è **pro-apoptotico** e che il peptide **inibisce** la morte neuronale — cioè agisce da antagonista, non da sostituto. → **Nessun lead terapeutico può essere promosso da un commentary/review senza leggere il primario.** Vedi la correzione a [[discovery_ledger_current#DL-MOL-008 — Peptide pTyr33-WWOX: un candidato di "restoration" già testato in vivo su un modello neurologico|DL-MOL-008]]. Il danno è stato nullo solo perché il lead era già taggato `ESPANSIONE` e "traccia bibliografica, non un'opzione": **la disciplina epistemica ha fatto esattamente il lavoro per cui esiste.** ^fm-010

---

## Run 2026-07-09c — Il paper decisivo era in corpus da sempre, marcato Tier A / priority-HIGH, mai letto

> Inseguendo il gap "OPC contati?" (HYP-07) sono arrivato a Obeid 2026 GT → Oliver 2023 Epilepsia → **Johannsen 2018**. Quest'ultimo studia **esattamente Gln230** con dati funzionali su fibroblasti donor-derived. Era a registro come `CORPUS P383`, `Tier A`, `disease-level relevance: HIGH`, `Status: screened — corpus placeholder`, **"no deep-dive performed"**.

### 🔴 DL-MECH-029 — Q230P: trascritto normale, **proteina non rilevata**; causa traduttiva versus degradativa non risolta
- **Status**: open · **Tag**: **DATO** sull'endpoint (fibroblasti donor-derived) + **IPOTESI** sulla causa
- **Fonte**: Johannsen J, Kortüm F, Rosenberger G, Bokelmann K, **Schirmer MA**, Denecke J, Santer R. 2018, *Neurogenetics* 19(3):151-156 (PMID 29808465, [DOI](https://doi.org/10.1007/s10048-018-0549-5)) — **abstract PubMed; full-text closed (Springer)**. A registro come `CORPUS P383`.
- **Finding (DATO)**: due sorelle (famiglia consanguinea, Afghanistan) **omozigoti per un missense sull'amminoacido evolutivamente conservato Gln230**, nel dominio SDR catalitico. Analisi funzionale su **fibroblasti donor-derived**: **qRT-PCR → livelli di trascritto WWOX normali; Western blot → assenza di proteina WWOX.** Interpretazione degli autori: *"impaired translation or **premature degradation** of the WWOX protein"*. Fenotipo: epilessia precoce refrattaria, **microcefalia progressiva**, ritardo profondo, anomalie RMN, atrofia ottica bilaterale in una delle due. Gli autori li descrivono come i primi individui all'estremo **più severo** dello spettro pur portando **un solo missense**.
- **Statement causale**: `Q230P —compatible_with→ normal_steady_state_WWOX_mRNA`; `Q230P —associated_with→ WWOX_protein_not_detected`; `cause ∈ {impaired_translation, insolubility, premature_degradation}` non discriminata.
- 🎯 **Rilevanzal genotipo di riferimento — su due fronti opposti, entrambi importanti.**

  **(1) VALIDAZIONE PARZIALE del modello LEGEND.** Johannsen conferma l'endpoint `mRNA normale + proteina non rilevata`, non il passaggio `misfolding → degradazione`. ThermoMPNN Q230P = **+1.514 kcal/mol** ed ESM-2/AlphaFold restano evidenza in-silico di perturbazione plausibile, non di meccanismo. `DATO + IPOTESI`

  **(2) AGGIORNAMENTO PROGNOSTICO SFAVOREVOLE, da riportare senza attenuarlo.** [[discovery_ledger_current#DL-MECH-030 — Genotipo e mortalità in WWOX-DEE: il dato prognostico più diretto che esista per il genotipo di riferimento (e i suoi limiti)|DL-MECH-030]] (Oliver 2023) mostra che i pazienti con **≥1 variante missense** hanno sopravvivenza significativamente migliore dei **null/null**. Ma quel vantaggio poggia su un'assunzione esplicitamente dichiarata **"presunta, non dimostrata"**: che il missense sia **ipomorfo**, cioè lasci funzione residua. **Per Q230P questa assunzione è falsa**: non c'è proteina. il genotipo di riferimento, formalmente `null/missense`, potrebbe essere **funzionalmente null/null**. `INFERENZA` (forte).

  **Contrappesi fattuali, non consolatori** — la variabilità clinica reale è ampia e va guardata in faccia: nella coorte di Oliver, il **Paziente 2 è Q230P omozigote ed è il paziente più anziano dell'intero studio (23 anni e 11 mesi, vivo)**; il Paziente 5, anch'esso Q230P omozigote, è **morto a 8 anni**; il Paziente 1 (**Q230P + delezione esoni 7-8: la combinazione più vicina a quella del genotipo di riferimento**) è **vivo a 4 anni e 7 mesi**. Inoltre: "assenza" al Western blot è un limite di sensibilità, non uno zero assoluto; e la stabilità proteica può essere **tessuto-specifica** (un fibroblasto non è un neurone).

  **(3) CONSEGUENZA TERAPEUTICA CORRETTA (BATCH_20260714_001).** L'endpoint nomina un esperimento discriminante, non ancora un rescue. Sull'allele missense del genotipo di riferimento:
  - non c'è un difetto di **trascrizione** (l'mRNA c'è, in quantità normale);
  - non c'è **NMD** (è un missense, non un PTC);
  - non serve un **ASO** (non è un difetto di splicing);
  - il collo di bottiglia può essere **traduzione, insolubilità o degradazione**.

  Il bersaglio va scelto **dopo** misura di sintesi nascent, solubilità ed emivita. [[therapeutic_hypotheses_ledger_current#HYP-20260709-02 — Boost dell'espressione di WWOX da solo ha verso incerto: va accoppiato a stabilizzazione di Q230P|HYP-20260709-02]] e [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]] restano condizionati.
- **Belief**: alto sul dato di endpoint; basso-medio su ciascun meccanismo specifico; nessuna implicazione terapeutica diretta prima della discriminazione.
- **Esperimento:** Western/qRT-PCR allele-specifici + pulse-labeling della sintesi + frazionamento solubile/insolubile + pulse-chase; poi sonde ortogonali proteasomiali/lisosomiali con vitalità e readout funzionali. Nessuna singola sonda negativa chiude il ramo.
- ⚠️ **Assunzione critica ancora aperta**: che la proteina Q230P, una volta ristabilizzata, sia **cataliticamente e funzionalmente attiva**. Johannsen non lo testa. Se fosse stabile-ma-inerte, il rescue proteostatico non darebbe funzione. Da [[discovery_ledger_current#DL-MECH-019 — Q230 cade nel dominio SDR che media il binding a tau/GSK3β/TPC6AΔ: catalisi intatta ≠ funzione conservata|DL-MECH-019]] sappiamo inoltre che il SDR media anche il binding a tau/GSK3β/TPC6AΔ, quindi il readout deve includere **binding**, non solo catalisi.
- **Interconnessioni**: [[claim_registry_current#CLAIM 019]], [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013]], [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]], [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]], [[discovery_ledger_current#DL-MECH-019 — Q230 cade nel dominio SDR che media il binding a tau/GSK3β/TPC6AΔ: catalisi intatta ≠ funzione conservata|DL-MECH-019]], [[discovery_ledger_current#DL-MECH-030 — Genotipo e mortalità in WWOX-DEE: il dato prognostico più diretto che esista per il genotipo di riferimento (e i suoi limiti)|DL-MECH-030]]
- 🔎 **Nota di provenienza**: **Markus A. Schirmer** è coautore sia di questo paper sia del lavoro Sp1/JNCI letto oggi ([[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]], PMID 26857392). Lo stesso gruppo di Göttingen ha prodotto sia l'assay di inclusione dell'esone 9 sia il dato funzionale su Q230P — cioè **entrambi i pezzi che servono per caratterizzare i due alleli del genotipo di riferimento**. Contatto potenzialmente ad altissimo valore.

### DL-MECH-030 — Genotipo e mortalità in WWOX-DEE: il dato prognostico più diretto che esista per il genotipo di riferimento (e i suoi limiti)
- **Status**: open · **Tag**: DATO (statistica di coorte) + IPOTESI (l'assunzione "missense = ipomorfo")
- **Fonte**: Oliver KL, Trivisano M, … Scheffer IE. 2023, *Epilepsia* 64(5):1351-1367 (PMID 36779245, PMC10952634, [DOI](https://doi.org/10.1111/epi.17542)) — **full text letto integralmente**. Già a registro ([[paper_registry_current#PAPER 018]]) ma **il dato genotipo-sopravvivenza non era mai stato promosso a claim**.
- **Finding (DATO)**:
  - **Regola di codifica esplicita (Methods §2.4)**: *"coded as either **null** (i.e., frameshift, nonsense, **donor/acceptor splice site**, deletion) or **missense**"*. → l'allele di sito accettore del genotipo di riferimento (`c.1057-2A>G`, perdita accettore) è **null** per definizione del paper; Q230P è **missense**. **il genotipo di riferimento = classe `null/missense`**, senza ambiguità.
  - Coorte 13 pazienti + 62 da letteratura = 75. Classi: null/null n=45 (60%), **null/missense n=15**, missense/missense n=15.
  - **Sopravvivenza (Kaplan-Meier, log-rank, p = .0085)**: null/null → **<50% a 5 anni, ~25% a 10 anni**. Gruppi con **≥1 missense** → **>75% a 5 anni, >60% a 10 anni**.
  - ⚠️ **Il confronto significativo è `null/null` vs `(null/missense + missense/missense)` POOLED.** Gli autori scrivono esplicitamente: *"no difference between individuals with one or two missense variants… **no evidence to support an 'intermediate' phenotype**"*. Quindi **non** esiste un gradino intermedio dimostrato: l'ancora corretta per il genotipo di riferimento è la curva aggregata "≥1 missense", non un'interpolazione.
  - **Nessuna mediana di sopravvivenza, nessun hazard ratio, nessun CI numerico** sono riportati. Mortalità complessiva ~35%; causa dominante: **complicanze respiratorie**.
  - Età d'esordio delle crisi **non differisce tra le classi (p=.65)** → il genotipo predice la **mortalità**, non l'esordio.
  - Fenotipo di coorte: esordio mediano 5 settimane; focali 85%, spasmi epilettici 77%, toniche 69%; **tutti** con background lento; RMN: atrofia frontotemporale e ippocampale, **atrofia ottica severa nel 100%**, corpo calloso molto sottile, anomalie di segnale della sostanza bianca; mielinizzazione ritardata già a **giorno 15-19** in 2 pazienti; distonia in 8/13; microcefalia acquisita 10/13; **farmaco-resistenza in 12/13**; **nessun tumore** in alcun paziente.
- **Rilevanza di malattia / implicazione**: è il dato più direttamente prognostico esistente, e colloca formalmente il genotipo di riferimento **dal lato migliore dell'unico split statisticamente sostenuto**. **Ma** — vedi [[discovery_ledger_current#🔴 DL-MECH-029 — Q230P: trascritto normale, **proteina non rilevata**; causa traduttiva versus degradativa non risolta|DL-MECH-029]] — quel vantaggio poggia su un'assunzione (missense = ipomorfo) che **per la specifica variante del genotipo di riferimento è contraddetta da un dato funzionale**. Le due cose vanno tenute insieme, non scelte a convenienza. Onestamente: la statistica di classe è **media di popolazione**, non certifica Q230P.
- **Limiti seri**: N minuscoli per classe; assenza di HR/CI/mediane; bias di ascertainment (letteratura sbilanciata verso i severi); **sopravvivenza confusa dalle cure di supporto** (85% con gastrostomia); la farmaco-responsività non protegge (l'unico paziente non farmaco-resistente è morto a 8 anni).
- **Segnali su farmaci (uso, NON efficacia)**: vigabatrin 7/10 usato per gli spasmi; **cannabidiolo: 4/4 lo hanno continuato**; **dieta chetogenica: solo 1/3 l'ha continuata** (2 sospese per scarsa tolleranza/beneficio). ⚠️ **Nessuna misura di efficacia, nessuna tossicità riportata.** Sono pattern di continuazione, non evidenza. **Il segnale KD è un contrappeso onesto a [[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]]**: nella pratica clinica reale la KD è stata abbandonata nella maggioranza dei casi in cui è stata tentata.
- **Varianti SDR vicine a Q230 (DATO)**: nella finestra ~200-260, **Q230P è l'unico missense**; le altre (p.Arg264Ter, p.Gln244ProfsTer26) sono null. Non esiste un secondo missense vicino su cui fare cross-check. Nota fine: **p.Pro47** dà SCAR12 (→Thr) o WWOX-DEE (→Arg) → **è la sostituzione specifica, non solo la posizione, a determinare la severità.**
- **Endpoint di monitoraggio utilizzabili**: RMN seriata (atrofia frontotemporale/ippocampale/ottica, spessore corpo calloso, progressione della mielinizzazione — **progrediscono in 7/7**); **atrofia ottica** (100%, presente a ogni età); evoluzione EEG; **stato respiratorio** (driver dominante di mortalità → target di sorveglianza per "guadagnare tempo").
- **Interconnessioni**: [[claim_registry_current#CLAIM 019]], [[meta_human_spectrum_current]], [[discovery_ledger_current#DL-MECH-022 — Posizionamento genotipo-fenotipo: il genotipo di riferimento sta tra il null puro (WOREE) e l'ipomorfo (SCAR12)|DL-MECH-022]] (che questo **corregge**: il posizionamento non era una mia IPOTESI, era un DATO pubblicato non promosso)

### DL-MECH-031 — L'ipomielinizzazione WWOX è **secondaria al neurone**, non un difetto autonomo dell'oligodendrocita. E la finestra della terapia genica è neonatale
- **Status**: open · **Tag**: INFERENZA robusta (mielina) + DATO (finestra murina)
- **Fonte**: Obeid M, Akkawi R, Repudi S, … Aqeilan RI. 2026, *Mol Ther Adv* 34(3):201791 (PMID 42422765, PMC13343157, [DOI](https://doi.org/10.1016/j.omta.2026.201791)) — **full text letto integralmente**. **Non era a registro con questo PMID** (il working model lo cita come "Obeid 2026"; il claim canonico è [[claim_registry_current#CLAIM 011]], verificato **accurato**).
- **Finding (DATO)**: confronto sistematico di promotori in AAV9 ICV neonatale su topo Wwox-null. **hSynI (neuronale)** → rescue robusto e durevole (sopravvivenza da ~3 settimane a ~1 anno, ≈WT p=0.78; glicemia normalizzata; peso, comportamento, fertilità; **mielina (MBP) near-complete rescue dose-dipendente**; **SWD ridotti p<0.0001**; gliosi GFAP/Iba1 ridotta). **MBP (oligodendrocitario)** → espressione debole, **zero miglioramento fenotipico**. EF1α → nessun rescue; CMV/CBA → rescue transiente. Nessuna espressione epatica; nessuna tossicità overt; WPRE rimosso **precauzionalmente** (non per danno osservato).
- ⚠️ **Confounder dichiarato dagli autori**: il fallimento del braccio oligodendrocitario *"may reflect the limited oligodendrocyte tropism of AAV9 following neonatal ICV administration rather than a lack of relevance"*, e tutti i vettori sono stati testati alla stessa dose. **Quindi il braccio AAV non prova la tesi.** La prova vera è **genetica** e viene da Repudi 2021: delezione di Wwox in **neuroni (Synapsin-Cre)** o progenitori (Nestin-Cre) ricapitola l'intero fenotipo **inclusi i difetti di mielina**, mentre la delezione in **oligodendrociti (Olig2-Cre)** e astrociti (GFAP-Cre) **non produce anomalie evidenti**.
- **Rilevanza di malattia / implicazione**:
  1. **Riorienta [[therapeutic_hypotheses_ledger_current#HYP-20260709-07 — Pro-mielinizzanti per la finestra mielinica, **condizionata a un esperimento che nessuno ha ancora fatto**|HYP-20260709-07]]**: un pro-mielinizzante che agisce **sull'oligodendrocita** ha razionale debole, perché l'oligodendrocita non è il difetto primario — non riceve il segnale assonale/di attività. La domanda "gli OPC ci sono o mancano?" (che avevo posto come esperimento decisivo) **è meno decisiva di quanto pensassi**: anche se gli OPC ci fossero tutti, spingerli non basterebbe.
  2. **Ma apre una leva migliore**: la mielinizzazione è **attività-dipendente**. Se la mielina dipende dall'attività assonale, allora **ridurre il carico di crisi e stabilizzare la rete potrebbe di per sé migliorare la mielinizzazione** — cioè la leva "protezione-finestra" già nel portafoglio acquisisce un razionale meccanicistico per un beneficio *strutturale*, non solo sintomatico. `IPOTESI`
  3. **La finestra della GT (dato duro)**: il rescue funziona a **qualsiasi punto tra P0 e P5** nel topo. **Oltre P5 non è mai stato testato** — non perché fallisca, ma perché *"Wwox-null mice rapidly deteriorate… precluding effective intervention at later stages"*. Gli autori dichiarano esplicitamente che il limite *"likely reflects model-specific biological constraints and technical limitations, rather than a definitive boundary for therapeutic responsiveness"* e che i pazienti umani *"may exhibit different developmental trajectories… potentially allowing for later intervention"*. **Onestamente: non esiste alcun dato positivo che il trattamento fuori finestra funzioni; ed è una porta lasciata aperta come ricerca, non un risultato.**
  4. **Trasferibilità al genotipo di riferimento**: è **gene replacement** (aggiunge hWWOX wild-type) → in linea di principio **genotype-agnostico**. Un paziente null/missense dovrebbe essere trattabile almeno quanto il null/null testato. Nessun rischio dominante-negativo (malattia recessiva). Il vettore usa già **hWWOX umano**.
  5. 🏭 **Segnale traslazionale**: tre coautori sono dipendenti di **Mahzi Therapeutics** (South San Francisco); Aqeilan è consulente; finanziamento Mahzi + WWOX Foundation. Il paper è scritto in chiave IND-enabling ("clinically relevant range", "viable path toward clinical intervention **in infants**"). **Nessun trial clinico è menzionato** — è preclinica. ⚠️ Il target dichiarato ("infants") è un segnale sui **criteri di eleggibilità per età**, potenzialmente sfavorevole a pazienti più grandi. **Rilevante in modo diretto per la missione "la finestra si sta chiudendo".** → follow-up mirato su Mahzi / WWOX Foundation per stato pipeline, IND, criteri di età. `ESPANSIONE`
- **Limite metodologico**: la mielina è misurata **solo come intensità MBP in immunoistochimica** — nessun g-ratio, nessuna microscopia elettronica, nessuna conta di oligodendrociti. Il rescue "near-complete" è di segnale MBP, non di mielina ultrastrutturale.
- **Interconnessioni**: [[claim_registry_current#CLAIM 011]] (verificato accurato ma sotto-cattura i dettagli di design), [[therapeutic_strategies_current]], [[meta_network_myelin_glia_current]], [[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile|DL-MECH-027]]

---

## Failure mode registrati (run 2026-07-09c)

- **FM-011 — `CORPUS_CATALOGUED` + `Tier A` + `disease-level relevance: HIGH` + `no deep-dive performed` è una combinazione che dovrebbe suonare un allarme.** `CORPUS P383` (Johannsen 2018) conteneva **il dato funzionale sperimentale sulla variante esatta del genotipo di riferimento** ed era marcato con la massima rilevanza — eppure è rimasto un placeholder mentre LEGEND costruiva la stessa conclusione in-silico da zero (CLAIM 019, tre modelli, RC-013). Non è stato un errore di triage: il triage **lo aveva classificato correttamente**. È stato un errore di **priorità di lettura**. → **Micro-upgrade proposto**: un check che elenchi i `CORPUS` con `Tier: A` **e** `disease-level relevance: HIGH` **e** `no deep-dive performed`, e li porti in cima alla coda di lettura, *prima* di qualunque nuovo batch. L'oro non era nei dettagli di uno studio nuovo: era in uno studio che avevamo già schedato e non aperto.
- **FM-012 — Un'inferenza elegante non sostituisce la ricerca della prova.** LEGEND aveva predetto correttamente il meccanismo di Q230P con tre modelli in-silico convergenti, e ne era giustamente soddisfatto. Ma la **prova sperimentale esisteva dal 2018**. La domanda giusta non era *"quanto è robusta la mia predizione?"* ma *"qualcuno l'ha già misurato?"* — che costa una query PubMed. → Prima di aprire un `research_candidate` per validare sperimentalmente un'ipotesi, **cercare se il dato esiste già** in letteratura.

---

## Run 2026-07-10 — L'oro non letto, aperto. La serie allelica di WWOX si chiude, e sposta la domanda.

> Ho eseguito il gate `unread_gold.py` invece di aprire il batch nuovo. I 5 paper Tier-A/priority-HIGH mai letti hanno prodotto più del batch. In parallelo, dal batch nuovo ho estratto **Mallaret 2014** (P47T), che è il pezzo mancante della serie.

### ⭐ DL-MECH-033 — La serie allelica di WWOX: **la quantità di proteina non predice la severità. Conta la funzione residua.**
- **Status**: open · **Tag**: DATO (quattro fonti indipendenti su fibroblasti/organoidi di paziente) + INFERENZA (la regola)
- **Fonti**: Mallaret M et al. 2014, *Brain* 137:411-419 (PMID 24369382) · Johannsen J et al. 2018, *Neurogenetics* (PMID 29808465) · Steinberg DJ et al. 2021, *EMBO Mol Med* (PMID 34268881, PMC8350905, **full text letto**) · Abdel-Salam G et al. 2014, *Orphanet J Rare Dis* (PMID 24456803, **full text letto**) · Aldaz CM et al. 2014, *BBA* (PMID 24932569, **full text letto**)

| Variante | Dominio | **Proteina misurata** | **Funzione** | Fenotipo |
|---|---|---|---|---|
| **P47T** | WW1 | **normale** (WB fibroblasti paziente, 3 passaggi vs 4 controlli) | **binding PPxY abolito** (pull-down); SDR *"presumibilmente ancora funzionale"* | **SCAR12 lieve** (vivi a 17-26 anni) |
| **G372R** | SDR | *"barely any signal"* (IF organoidi paziente) | ? | **SCAR12 lieve**; organoidi forebrain con sviluppo corticale e astrogenesi **normali**, nessun eccesso di danno al DNA |
| **Q230P** | SDR | **assente** (WB fibroblasti paziente; trascritto normale) | ? | **WOREE severo** |
| **p.Arg54\*** | — | zero (nonsenso) | zero | **letale a 16 mesi**, microcefalia progressiva, retinite pigmentosa precoce |
| *Wwox^gt/gt* (topo ipomorfo) | — | bassa ma **rilevabile** | parziale | **vitale**, vita accorciata |
| *Wwox*-KO (topo) | — | zero | zero | morte a 3-4 settimane |

- **Le due osservazioni che rompono il modello semplice:**
  1. **P47T ha proteina a livelli normali e binding WW1 completamente abolito — eppure il fenotipo è lieve.** Gli autori attribuiscono la mitezza al fatto che *"the dehydrogenase/reductase domain of the mutant protein is presumably still functional"*. → **La funzione WW1/PPxY-binding non è essenziale per un fenotipo grave. Il SDR sì.**
  2. **G372R è nel SDR, ha proteina quasi non rilevabile all'IF — eppure il fenotipo è lieve** e i suoi organoidi sono quasi normali. Steinberg lo nota esplicitamente in Discussione: nei genitori eterozigoti sani l'espressione di WWOX varia molto, nei pazienti omozigoti affetti pochissimo, e si chiedono *"whether the disease severity is correlated with the **functional levels** of WWOX rather than the total expression levels."*
- **Conseguenza per il genotipo di riferimento — e per HYP-08 (importante, e non è quella che speravo):**
  La relazione dose-proteina→severità è **vera nel topo** (ipomorfo vitale vs null letale) ma **non basta a spiegare la serie umana**. Q230P e G372R stanno **entrambe nel SDR** ed **entrambe** danno poca proteina rilevabile — ma una dà WOREE severo e l'altra SCAR12 lieve. **La differenza non può essere la sola quantità.**
  → **La domanda giusta non è "quanta proteina Q230P riusciamo a salvare" ma "la proteina Q230P salvata è funzionale?"** È esattamente l'assunzione che avevo già marcato come non testata in [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]]. Ora sappiamo che **è l'assunzione su cui tutto poggia**, e che esiste un controllo naturale per testarla.
- **💡 Ipotesi strutturale a costo zero, immediatamente testabile (nuova):** LEGEND ha già calcolato che **Gln230 è sepolto nel core del SDR** (relSASA 0.00, su α-elica) e fortemente destabilizzante (ThermoMPNN ΔΔG +1.51 kcal/mol; ESM-2 LLR -9.08, la peggiore sostituzione del sito). **Se G372R risultasse superficiale e poco destabilizzante**, la serie allelica si spiegherebbe con la **stabilità del folding** — e HYP-08 ne uscirebbe rafforzata. Se invece G372R fosse anch'essa sepolta e destabilizzante, allora la quantità di proteina non spiega nulla e la differenza è funzionale/qualitativa (p.es. **Q230P potrebbe non essere solo instabile ma proteotossica/aggregante**). → **Eseguire la stessa pipeline (AlphaFold + relSASA + ThermoMPNN + ESM-2) su G372R e P47T.** Costo: nullo. Valore: discrimina tra i due scenari che decidono HYP-08. **Questo è il prossimo passo in-silico prioritario.**
- **Belief**: alto sui singoli DATI (tutti su cellule di paziente); medio sull'inferenza unificante (misure eterogenee: WB su fibroblasti vs IF su organoidi — **non confrontabili quantitativamente**; è un limite reale, non retorico).
- **Interconnessioni**: [[claim_registry_current#CLAIM 019]], [[claim_registry_current#CLAIM 007]], [[claim_registry_current#CLAIM 008]] (la caution "P47T ≠ Q230P" era corretta e ora è **spiegata**: domini diversi, meccanismi diversi), [[discovery_ledger_current#DL-MECH-026 — Il ratto *lde* è il proxy animale dell'allele di sito accettore del genotipo di riferimento: lesione dell'esone 9 → proteina assente + epilessia audiogenica nel 95%|DL-MECH-026]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]], [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013]]

### 🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica
- **Status**: open · **Tag**: DATO (RNA-seq su organoidi cerebrali umani)
- **Fonte**: Steinberg DJ et al. 2021, *EMBO Mol Med* (PMID 34268881, PMC8350905) — **full text letto integralmente**; RNA-seq pubblico su **GEO GSE156243**
- **Finding (DATO)**: RNA-seq di organoidi cerebrali WWOX-KO (settimana 15) → GSEA/GO mostrano **inibizione della sintesi di ATP accoppiata al trasporto di elettroni e della fosforilazione ossidativa**, con **arricchimento di glicolisi/gluconeogenesi**.
- **Perché conta**: in [[discovery_ledger_current#DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica|DL-MECH-020]] e [[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]] avevo scritto il caveat: *"il fenotipo Warburg è documentato in MEF e in cancro, **mai nel neurone WWOX-carente**"*. **Quel caveat cade.** Lo shift OXPHOS↓/glicolisi↑ è ora documentato in **tessuto neurale umano tridimensionale**, in un modello indipendente e con una tecnica diversa (trascrittomica, non Seahorse). Il razionale meccanicistico WWOX-specifico della dieta chetogenica ne esce sostanzialmente rafforzato.
- **Altri assi alterati (DATO)**: **Wnt cronicamente attivato** (β-catenina nucleare ~1.7×; WNT1/2B/3/3A/5A/8B, LEF1, AXIN2 ↑) — recuperato parzialmente da W-AAV; **Shh ↑** (SHH, GLI1, PTCH1, HHIP); **autofagia ↓** (RB1CC1/FIP200, MDM2, RB1); **mTOR/EIF4EBP1 ↓**. Dislaminazione corticale progressiva (strati I-IV ↓, CUX1/RELN ↑).
- **Belief**: alto sul dato trascrittomico; **medio** sul salto trascrittoma→flusso metabolico (l'espressione genica non è il flusso: servirebbe Seahorse/fluxomica sugli organoidi). Nota: n basso (WT n=2, KO n=4).
- **Esperimento**: Seahorse OCR/ECAR sugli organoidi WWOX-KO; e, per il genotipo di riferimento, su fibroblasti/LCL.
- ⚠️ **Ma vedi la contraddizione in [[discovery_ledger_current#⚠️ DL-BIO-008 — Contraddizione sul lattato: alto nel siero del topo, **"extremely low" nell'MRS cerebrale umana**|DL-BIO-008]]** prima di considerare il razionale chiuso.
- **Interconnessioni**: [[meta_metabolism_current]], [[discovery_ledger_current#DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica|DL-MECH-020]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]]

### ⚠️ DL-BIO-008 — Contraddizione sul lattato: alto nel siero del topo, **"extremely low" nell'MRS cerebrale umana**
- **Status**: open · **Tag**: DATO (entrambi) — **contraddizione non risolta**
- **Fonti**: Abu-Remaileh & Aqeilan 2014 (PMID 25012504): topi Wwox-KO → **lattato sierico significativamente aumentato**, ipoglicemia letale. · Davids et al. 2019, *Hum Mutat* (PMID 30362252, PMC6296882, **full text letto**): paziente WWOX EIEE28, **MR spectroscopy → aminoacidi non essenziali globalmente ridotti e lattato cerebrale estremamente basso**. · Abdel-Salam 2014 (PMID 24456803): paziente WOREE null/null → **screening metabolico interamente normale** (ammonio, lattato, aminoacidi, acidi organici, VLCFA).
- **Il problema**: il modello Warburg predice **lattato alto** (glicolisi ↑ → più lattato). Il topo lo conferma nel siero. **L'unico dato di spettroscopia cerebrale umana disponibile dice l'opposto**, e l'unico screening metabolico umano completo è normale.
- **Letture possibili (nessuna dimostrata)**: (a) differenza **compartimentale** (siero ≠ cervello); (b) differenza **di specie** (il topo KO muore di ipoglicemia, l'umano no); (c) in un cervello con OXPHOS depressa **e** flusso glicolitico ridotto dalla scarsa richiesta neuronale, il lattato può essere basso; (d) l'MRS è un singolo caso, con un fenotipo confuso da una seconda variante (**HSPG2**, perlecan).
- **Conseguenze operative (importanti):**
  1. **Il lattato NON è un biomarcatore affidabile dello stato di WWOX** → declassare [[discovery_ledger_current#DL-BIO-005 — Pannello funzionale WWOX–HIF1α/GLUT1/PKM2 + alanina|DL-BIO-005]] da candidato a **segnale ambiguo**; non collocarlo in `biomarker_candidates` (sarebbe comunque Tier 3, distale).
  2. **Non indebolisce direttamente il razionale della dieta chetogenica** (che poggia sul blocco PDK1→PDH e sulla OXPHOS depressa, non sul lattato), **ma toglie l'endpoint più facile** per verificarlo. L'endpoint corretto resta **Seahorse/OCR su cellule donor-derived**.
  3. È un promemoria: **la direzione del metabolismo umano WWOX-deficiente non è stata misurata.** Va misurata prima di costruirci sopra.
- **Interconnessioni**: [[discovery_ledger_current#DL-BIO-007 — Lattato sierico, glicemia e insulina come biomarcatori metabolici in vivo del deficit di WWOX|DL-BIO-007]] (declassato), [[discovery_ledger_current#🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica|DL-MECH-034]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]], [[clinical_monitoring_endpoints_current]]

### DL-MECH-035 — GABA depolarizzante negli organoidi WWOX-KO: perché gli antiepilettici standard sottoperformano
- **Status**: open · **Tag**: DATO (organoidi) + INFERENZA (clinica)
- **Fonte**: Steinberg DJ et al. 2021 (PMID 34268881, PMC8350905)
- **Finding (DATO)**: negli organoidi WWOX-KO, **GAD67 (GABAergico) marcatamente aumentato**, VGLUT1 (glutamatergico) invariato; concordanza a RNA (GAD1/GAD2 ↑); recettori GABA (GABRB3, GABRB2) ↓. Elettrofisiologia (LFP, settimana 7): potenza aumentata nelle **oscillazioni lente 0.25-1 Hz**, ridotta a 30-79.9 Hz; sotto provocazione con **4-aminopiridina 100 µM** i KO sono significativamente iperreccitabili, con accoppiamento cross-frequency δ:HFO aumentato (firma di stato pre-critico). Neuroni da paziente WOREE: frequenza di scarica **~4× quella dei genitori** (P<0.0001), **completamente normalizzata** dal rescue W-AAV (P=0.77 vs genitori). Il rescue lentivirale recupera lo spettro di potenza.
- **Interpretazione degli autori (INFERENZA)**: nei neuroni immaturi il GABA è **depolarizzante**; un eccesso di segnale GABAergico in questo contesto è **eccitatorio**, il che spiegherebbe perché gli antiepilettici GABAergici classici rendono poco in WOREE.
- **Rilevanza di malattia**: converge in modo diretto con [[meta_gaba_paradox_current]] (già "emerging / high-priority" nel sistema) e con il **DATO clinico** di farmaco-resistenza (12/13 in Oliver 2023; tutti gli AED falliti nel W44X; risposta solo *parziale* a valproato+lamotrigina in Abdel-Salam). ⚠️ **Nota di sicurezza coerente con quanto già a registro**: il vigabatrin agisce aumentando il GABA — e in LEGEND è già `conflicting evidence — non pro-vigabatrin` ([[claim_registry_current#CLAIM 001]]). Questo dato meccanicistico **offre un razionale al perché**. Non è parere medico: è un'ipotesi meccanicistica da portare al team curante.
- **Endpoint riusabili**: potenza LFP nella banda 0.25-1 Hz (AUC), frequenza di scarica cell-attached, rapporto GAD67/VGLUT1.
- **Belief**: alto sul dato negli organoidi; medio-basso sul trasferimento clinico (organoidi = tessuto immaturo per costruzione; il GABA depolarizzante è atteso a *qualunque* genotipo in quel contesto → il confronto KO-vs-WT è però interno e regge).

### DL-MOL-010 — Il banco per testare HYP-08 esiste già. Manca un solo reagente, e il genotipo di riferimento lo possiede.
- **Status**: open · **Tag**: ESPANSIONE (azione), fondata su DATO (le linee esistono)
- **Fonte**: Steinberg DJ et al. 2021 (PMID 34268881) — Materials & Methods, Tabelle EV3-EV5
- **Finding (DATO)**: il laboratorio **Aqeilan** possiede e ha caratterizzato: linee **hESC WWOX-KO** (WiBR3, CRISPR); una linea di **rescue stabile W-AAV** (WWOX cDNA in safe-harbor AAVS1); **lenti-WWOX** per rescue a mosaico; **iPSC da paziente WOREE** (famiglia WSM, `c.517-2A>G`, splice, omozigote); e — decisivo — **iPSC da paziente SCAR12 con missense nel dominio SDR** (famiglia WPM, **G372R**, omozigote). Piattaforma di readout completa: organoidi cerebrali e forebrain, elettrofisiologia (LFP + cell-attached), foci di danno al DNA (γH2AX/53BP1), astrogenesi, RNA-seq (GEO **GSE156243**), pannelli di anticorpi e primer pubblicati.
- **Perché è il lead più azionabile del ledger**: HYP-08 chiede una cosa sola — *se stabilizziamo la proteina Q230P, recupera funzione?* Per rispondere serve **una linea cellulare con un missense SDR** e **un readout funzionale** (non di abbondanza — vedi [[discovery_ledger_current#⭐ DL-MECH-033 — La serie allelica di WWOX: **la quantità di proteina non predice la severità. Conta la funzione residua.**|DL-MECH-033]]: l'abbondanza inganna). **Il lab Aqeilan ha entrambi**, e ha già un **controllo naturale perfetto**: G372R, missense SDR con fenotipo *lieve*. Confrontare **Q230P vs G372R vs P47T vs null** nello stesso sistema, misurando funzione (non quantità), è **l'esperimento che decide l'intera ipotesi**.
- **Cosa manca**: una linea iPSC con **Q230P**. il genotipo di riferimento la può fornire (PBMC → iPSC è routine; il lab ha già fatto esattamente questo per due famiglie).
- ⚠️ **Vincolo emerso dallo stesso paper (BLOCCO 1, e riguarda anche la GT)**: il rescue W-AAV era **supra-fisiologico e in tutte le popolazioni cellulari**, e ha dato un recupero **solo parziale**; gli autori insistono su *"the importance of optimizing population-targeted delivery and fine-tuning of expression levels"*. E la perdita di WWOX causa **proliferazione di progenitori con danno al DNA e perdita del checkpoint apoptotico**. → **Né troppo poco né troppo WWOX.** Vale per la terapia genica e vale per qualunque strategia di boost.
- **Interconnessioni**: [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]], [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]], *research-group knowledge base (not published)*, [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013]]

### DL-MECH-036 — Vie di degradazione di WWOX già note e druggabili (ma probabilmente non quelle giuste)
- **Status**: open · **Tag**: DATO (citato in review, primari da recuperare) + IPOTESI
- **Fonte**: Aldaz CM, Ferguson BW, Abba MC 2014, *BBA* 1846(1):188-200 (PMID 24932569, PMC4151823) — **full text letto**
- **Finding (DATO, citato)**: WWOX è degradato via **poliubiquitinazione e proteasoma**. **ACK1** fosforila WWOX su **Tyr287** innescandone la degradazione rapida; WWOX è anche substrato dell'E3 ligasi **ITCH**. Inoltre: la disruzione del dominio SDR **altera la localizzazione subcellulare** (perinucleare/Golgi), e i residui catalitici S281A/Y293F/K297A sono necessari **sia** per l'attività enzimatica **sia** per la localizzazione perinucleare.
- **Rilevanzal genotipo di riferimento / la cautela che conta**: esistono vie di degradazione **note e in principio aggredibili** (ACK1, ITCH). Ma sono meccanismi di **degradazione regolata** (fosforilazione → ubiquitinazione), **non** di controllo qualità di una proteina misfolded. Il misfolding di Q230P verrebbe verosimilmente gestito dal sistema di **quality control ERAD/chaperoni**, che è un'altra cosa. → **Non assumere che inibire ACK1/ITCH salvi Q230P.** I chaperoni chimici (4-PBA, TUDCA), che agiscono sul folding, **non compaiono in nessuno di questi paper**: restano IPOTESI da letteratura esterna. `IPOTESI`
- **Corollario su Q230P (INFERENZA aggiuntiva)**: se il SDR governa **anche la localizzazione**, Q230P potrebbe compromettere simultaneamente **stabilità, catalisi e localizzazione**. Il readout funzionale deve includere la **localizzazione subcellulare**, non solo l'attività e il binding.
- ⚠️ **Conflitto tra laboratori da registrare** (`conflicting evidence`): Aldaz colloca WWOX in sede **perinucleare/Golgi** e **nega** di aver mai osservato apoptosi da trasfezione, attribuendo il ruolo pro-apoptotico riportato dal lab Chang ad **artefatto dei vettori adenovirali**; il lab Chang lo colloca in **mitocondri e nucleo** con traslocazione stress-indotta. La localizzazione è proprio ciò che il SDR determina → **la disputa tocca direttamente Q230P** e va tenuta aperta, non risolta per preferenza.

---

## Failure mode registrati (run 2026-07-10)

- **FM-013 — "Più proteina" non è l'obiettivo; "più funzione" lo è. E il rescue supra-fisiologico è un rischio, non un successo.** Steinberg rescue-a con espressione supra-fisiologica in tutte le popolazioni cellulari, ottiene un recupero **parziale**, e avverte esplicitamente di *"fine-tuning"*. WWOX-loss causa proliferazione di progenitori danneggiati e perdita del checkpoint apoptotico; WWOX è un oncosoppressore pro-apoptotico in alcuni contesti. → **Qualunque leva (GT, chaperone, boost) deve puntare a livelli fisiologici, non massimi.** Registrato come vincolo BLOCCO 1 permanente. ^fm-013
- **FM-014 — Abbondanza ≠ funzione, e le misure di abbondanza non sono confrontabili tra loro.** La serie allelica ([[discovery_ledger_current#⭐ DL-MECH-033 — La serie allelica di WWOX: **la quantità di proteina non predice la severità. Conta la funzione residua.**|DL-MECH-033]]) mette insieme un Western blot su fibroblasti (P47T), un Western blot su fibroblasti (Q230P) e un'immunofluorescenza su organoidi (G372R). **Non sono commensurabili.** Un'ipotesi costruita sul confronto tra quei numeri sarebbe fragile. La regola: quando si costruisce una serie genotipo-fenotipo, verificare che le misure siano **la stessa misura**. ^fm-014
- **FM-015 — Il caveat che scrivi oggi può cadere domani, e devi accorgertene.** Avevo scritto in HYP-01 che il fenotipo Warburg *"non è mai stato documentato nel neurone WWOX-carente"*. Era vero rispetto a ciò che avevo letto — ed era **falso in letteratura**, dove Steinberg 2021 lo mostrava in organoidi cerebrali umani. Quel paper era in corpus, Tier A, mai letto. → Un caveat non è una conclusione: è **un compito di ricerca aperto**. Vanno riletti quando il corpus cresce. ^fm-015

---

## Run 2026-07-10b — Il gate in-silico di HYP-08, eseguito. Lo scenario favorevole regge, ma la metrica era sbagliata.

### ⭐ DL-MECH-037 — Q230P è **l'unica delle tre varianti a essere una lesione di ripiegamento del core**. Il ΔΔG non lo diceva; la sepoltura sì.
- **Status**: open · **Tag**: IPOTESI robusta (in-silico, su struttura predetta) — **non** DATO
- **Metodo**: struttura AlphaFold `AF-Q9NZC7-F1` (già in repo) + nuovo `scripts/legend/residue_context.py` (Shrake-Rupley, P-SEA, pLDDT, contatti, distanza dalla triade; numpy puro) + saturazione ThermoMPNN già presente (`WWOX_ThermoMPNN_saturation.csv`, 414×20). Output completo: `staging/insilico_20260710/`.
- **Controllo di qualità**: lo script riproduce indipendentemente `relSASA(Gln230) = 0.000`, identico al valore già a registro in [[claim_registry_current#CLAIM 019]] (ottenuto con altra pipeline). Le due catene di calcolo concordano.

| Variante | Dominio | relSASA | Sepoltura | SSE | pLDDT | d(triade) | ΔΔG | Proteina | Fenotipo |
|---|---|---:|---|---|---:|---:|---:|---|---|
| **P47T** | WW1 | 0.286 | parz. esposto | β-strand | 82.3 | 51.4 Å | **+2.81** | **normale** | **lieve** |
| **P47R** | WW1 | 0.286 | parz. esposto | β-strand | 82.3 | 51.4 Å | +2.53 | n.d. | **severo** |
| **Q230P** | SDR | **0.000** | **sepolto (core)** | **α-elica** | 98.5 | 8.2 Å | +1.51 | **assente** | **severo** |
| **G372R** | SDR | 0.163 | parz. esposto | β-strand | 93.8 | 17.8 Å | +1.58 | quasi assente | **lieve** |

- **Finding 1 — Il ΔΔG predetto non predice né l'abbondanza né la severità (DATO sui numeri, INFERENZA sulla regola).** Due controlli indipendenti, uno dei quali perfetto:
  - **Stesso residuo, ΔΔG quasi identici, fenotipi opposti**: **P47T** (ΔΔG **+2.81**, il più alto dei tre) → SCAR12 **lieve**, con **proteina a livelli normali** al Western blot di paziente; **P47R** (ΔΔG +2.53) → WWOX-DEE **severo**. **Il ΔΔG più alto ha il fenotipo più lieve.**
  - **Residui diversi, ΔΔG quasi identici, fenotipi opposti**: Q230P (+1.51) severo vs G372R (+1.58) lieve.
- **Finding 2 — ⚠️ Correzione interna: l'euristica "finestra recuperabile" (ΔΔG 0.8–3.5) non è validata.** `WWOX_pathogenic_missense_classified.csv` classifica **tutte e tre** le varianti come `stability (rescuable window)`, ma i loro fenotipi divergono e P47T ha proteina normale. **La finestra non discrimina.** L'argomento *"7/13 missensi patogeni ClinVar cadono nella finestra recuperabile, quindi dominanza del misfolding"*, citato in [[claim_registry_current#CLAIM 019]] a sostegno dell'ipotesi proteostatica, **va declassato**: su questi dati la finestra non ha valore predittivo dimostrato. Il sostegno alla misfolding-dominance sembrava reggere su **Johannsen 2018** e sul contesto strutturale, **non** su quell'euristica. 🔴 **Superato dal repair 2026-07-14 — CAUSA NON RISOLTA:** Johannsen dichiara esplicitamente due alternative, **traduzione compromessa** *oppure* degradazione prematura, e non le discrimina; l'insolubilità è la terza. Il dato wet è `trascritto normale + proteina non rilevata`, non `misfolding → degradazione`.
- **Finding 3 — Il contesto strutturale, invece, discrimina in modo netto (IPOTESI robusta).**
  - **Q230 è l'unico residuo completamente sepolto** (relSASA 0.000, il minimo possibile), su **α-elica**, 22 contatti pesanti entro 5 Å, pLDDT 98.5 (massima affidabilità della struttura). **Gln→Pro in un'α-elica sepolta è il caso peggiore possibile**: la prolina non dona il legame H del backbone (rompe il pattern i,i−4), impone φ ≈ −60° rigido, e in un core denso non c'è spazio per riorganizzarsi. → collasso del ripiegamento locale plausibile. 🔴 **Annotazione post-repair 2026-07-14:** la catena `misfolding → degradazione` era un'inferenza, non un dato. Il dato wet di Johannsen è `trascritto normale + proteina non rilevata`, ed è compatibile anche con **traduzione compromessa** o con **insolubilità**: la **causa resta non risolta**. La geometria (sepoltura, elica, contatti) regge; l'esito molecolare no.
  - **G372 e P47 sono entrambi parzialmente esposti, su β-strand, in superficie** → una sostituzione superficiale è tollerabile per il folding (la catena laterale sporge nel solvente).
  - **P47 dista 51 Å dal sito attivo** (dominio WW1, modulo autonomo): la sua lesione è **funzionale** (binding PPxY abolito, pull-down di Mallaret), **non strutturale** — ed è esattamente per questo che la proteina P47T è presente a livelli normali. La serie torna.
- 🎯 **Conseguenza corretta per [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]]:** sepoltura + contesto strutturato + chimica della prolina rendono Q230P una perturbazione di core plausibile, non una lesione di folding/degradazione dimostrata. Un chaperone ha razionale solo condizionato a sintesi, turnover e stato funzionale recuperabile.
- 🔴 **Il nuovo dubbio, ora preciso e falsificabile.** Una **prolina sepolta in un'α-elica** impone un vincolo di backbone che **un chaperone non può rimuovere**: un chaperone favorisce il raggiungimento di uno stato foldato, non cambia la chimica del backbone. Quindi: **esiste, per Q230P, uno stato foldato *e* cataliticamente attivo raggiungibile?**
  - *A favore*: Q230 dista **8.2 Å** dalla triade catalitica — la perturba per prossimità, non per contatto. Una distorsione locale dell'elica potrebbe non spostare Ser281/Tyr293/Lys297.
  - *Contro*: 22 contatti pesanti entro 5 Å indicano un core denso, poco tollerante a una distorsione.
  - **Nessuno dei due è dirimente in silico. Serve il wet.** Questo è il limite reale dell'analisi, non una formalità.
- 🧪 **L'esperimento discriminante che questo risultato genera (nuovo, e migliora il piano di HYP-08).** Eseguire il test di rescue proteostatico **in parallelo su Q230P e su G372R** — il lab Aqeilan possiede iPSC **G372R** ([[discovery_ledger_current#DL-MOL-010 — Il banco per testare HYP-08 esiste già. Manca un solo reagente, e il genotipo di riferimento lo possiede.|DL-MOL-010]]). Predizione del modello strutturale:
  - **Q230P** (lesione di folding del core) → **risponde** a 4-PBA/TUDCA: la proteina riemerge.
  - **G372R** (lesione di superficie) → **non risponde**, o risponde poco.
  Se **G372R rispondesse identicamente a Q230P**, il modello strutturale qui proposto sarebbe **falso** e il rescue osservato sarebbe un artefatto aspecifico dei chaperoni chimici. **È il controllo negativo che rende l'esperimento interpretabile** — e prima di oggi non l'avevamo.
- **Limiti (da non omettere)**: ThermoMPNN e AlphaFold sono predittori, nessun ΔΔG sperimentale è stato misurato; relSASA e SSE sono calcolati su un **monomero**, ma WWOX **omodimerizza via SDR** e l'interfaccia non è modellata; pLDDT alto indica confidenza della *struttura*, non della *predizione di stabilità*; P-SEA è un'annotazione geometrica semplificata, non DSSP; l'abbondanza di P47T (WB su fibroblasti) e G372R (IF su organoidi) **non sono misure commensurabili** ([[discovery_ledger_current#^fm-014|FM-014]]).
- **Belief**: alto sui numeri strutturali (pLDDT eccellente, doppia pipeline concordante); **medio-alto** sull'interpretazione "Q230P = lesione di folding"; **medio-basso** sull'assunzione che la proteina ristabilizzata sia funzionale — che resta l'ignoto centrale.
- **Interconnessioni**: [[claim_registry_current#CLAIM 019]] (euristica finestra → declassare), [[discovery_ledger_current#DL-MECH-026 — Il ratto *lde* è il proxy animale dell'allele di sito accettore del genotipo di riferimento: lesione dell'esone 9 → proteina assente + epilessia audiogenica nel 95%|DL-MECH-026]], [[discovery_ledger_current#🔴 DL-MECH-029 — Q230P: trascritto normale, **proteina non rilevata**; causa traduttiva versus degradativa non risolta|DL-MECH-029]], [[discovery_ledger_current#DL-MOL-010 — Il banco per testare HYP-08 esiste già. Manca un solo reagente, e il genotipo di riferimento lo possiede.|DL-MOL-010]], [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013]], [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]]

## Failure mode registrati (run 2026-07-10b)

- **FM-016 — Un'euristica interna non validata si era travestita da evidenza.** La "finestra recuperabile ΔΔG 0.8–3.5" era stata usata in CLAIM 019 per sostenere la misfolding-dominance ("7/13 missensi ClinVar ci cadono dentro"). Il primo test reale la falsifica: **tutte e tre** le varianti della serie allelica cadono nella finestra, con fenotipi opposti, e la variante col ΔΔG più alto ha **proteina normale**. → Un'euristica costruita in casa va **testata su casi a esito noto** prima di essere citata come supporto. Il sostegno all'ipotesi proteostatica non crolla — ma ora poggia su Johannsen (wet) e sul contesto strutturale, non su quella soglia. ^fm-016
- **FM-017 — La rete può cadere a metà di un'installazione: preferire dipendenze che non servono.** `freesasa` non compilava e `numpy<2` non si è potuto scaricare (DNS down). Riscrivere lo script in **numpy puro** (Shrake-Rupley + P-SEA implementati direttamente, ~90 righe) è costato meno del debug dell'ambiente, e lascia uno strumento **senza dipendenze di rete**, riusabile offline. Registrato come preferenza di progettazione per gli strumenti in-silico di LEGEND.

---

## Run 2026-07-10c — Chiuso il gate: 5/5 paper letti. Gli ultimi due correggono due cose che avevo appena scritto.

> `CORPUS P298` (Battaglia 2023, neuroimaging WOREE) e `CORPUS P356` (Shaukat 2018, West syndrome) — entrambi Tier A / priority HIGH, mai deep-dived. Il secondo, recuperato come bronze-OA da Wiley/JLE e letto integralmente da PDF, contiene i dati terapeutici più diretti dell'intero corpus.

### 🔴 DL-MECH-038 — Il vigabatrin **ha funzionato** in due bambini WWOX-null. Il razionale GABA-depolarizzante non predice la risposta clinica.
- **Status**: open · **Tag**: DATO (clinico, n=2) — **contraddice un'inferenza registrata ieri**
- **Fonte**: Shaukat Q, Hertecant J, El-Hattab AW, Ali BR, Suleiman J. 2018, *Epileptic Disord* 20(5):401-12 (PMID 30361190) — **full text letto integralmente** (`complete_fulltext_read`; tabella 1 estratta da PDF in colonne, mappatura varianti verificata)
- **Finding (DATO)**: due bambini non imparentati, entrambi da famiglie consanguinee, entrambi con **null biallelico** (caso 1: delezione omozigote esoni 3-4; caso 2: **splice acceptor omozigote c.606-1G>A**, introne 6) e **sindrome di West** (spasmi + ipsaritmia).
  - **Caso 1**: prednisolone orale (protocollo UKISS) → **risposta parziale**. **Vigabatrin aggiunto → "the spasms resolved"** (gli spasmi si sono risolti). Successivamente comparsa di mioclonie focali e crisi cloniche → migliorate con **levetiracetam**. A 2 anni: crisi miste infrequenti, EEG con fondo lento e attività multifocale infrequente.
  - **Caso 2**: fenobarbital → crisi migliorate. **Vigabatrin → risposta parziale.** A 11 mesi, nonostante 4 antiepilettici (vigabatrin, valproato, clobazam, fenobarbital), spasmi emilaterali residui in cluster; ventilatore-dipendente dai 4 mesi.
- ⚠️ **Perché questo conta, e perché va detto senza attenuarlo.** Ieri ho registrato [[discovery_ledger_current#DL-MECH-035 — GABA depolarizzante negli organoidi WWOX-KO: perché gli antiepilettici standard sottoperformano|DL-MECH-035]]: negli organoidi WWOX-KO il segnale GABAergico è aumentato e, poiché nei neuroni immaturi il GABA è depolarizzante, un farmaco che alza il GABA dovrebbe rendere poco o nuocere. **Il vigabatrin alza il GABA (inibisce la GABA-transaminasi). E in questi due pazienti ha risolto o ridotto gli spasmi.**
  - Il razionale meccanicistico **non è falsificato come meccanismo** (resta un dato sugli organoidi), ma **è falsificato come predittore della risposta clinica agli spasmi**. Un modello di tessuto immaturo in vitro non predice l'effetto di un farmaco su un cervello di 7 mesi in vivo.
  - **Nessun peggioramento né VABAM (anomalie RMN da vigabatrin) è riportato in questo paper.** Il segnale VABAM resta quello di Choi 2025, già a registro.
  - **Effetto netto su [[claim_registry_current#CLAIM 001]]**: lo stato `conflicting evidence — non pro-vigabatrin` **è confermato come corretto** — ed è ora conflicting in modo più informato: c'è evidenza di **efficacia sugli spasmi** (Shaukat, n=2) e evidenza di **tossicità RMN** (Choi, n=2). Nessuna delle due chiude la questione. **Non è parere medico.**
- **Belief**: alto sul dato (descrizione clinica esplicita); il limite è N=2, aperto, non controllato, senza follow-up EEG standardizzato.
- **Lezione di metodo → [[discovery_ledger_current#^fm-018|FM-018]]**: avevo costruito un razionale elegante su un modello in vitro e stavo per usarlo per interpretare la clinica. Il dato clinico esisteva, in un paper già a corpus, marcato Tier A, mai letto.

### 🔴 DL-MECH-039 — È una **DEE, non una EE**: controllare le crisi non salva lo sviluppo. E questo tocca la logica stessa di "guadagnare tempo".
- **Status**: open · **Tag**: DATO (osservazione clinica) + INFERENZA (degli autori, che condivido) — **implicazione strategica sfavorevole**
- **Fonte**: Shaukat 2018 (PMID 30361190), Discussione
- **Finding, con le parole degli autori (DATO)**: *"The developmental outcome was unfavourable with profound impairment **despite improvement of epileptic activity**"*; e ancora: *"the cognitive and psychomotor impairment **preceded the onset of epileptic encephalopathy** and **did not improve with achievement of better control of epileptic activity**"*. Concludono che è la mutazione di WWOX stessa — non l'attività epilettica — a causare sia il deficit cognitivo sia l'encefalopatia epilettica, secondo il concetto di **DEE** (developmental *and* epileptic encephalopathy) di Scheffer 2017, in opposizione al vecchio concetto di EE in cui le crisi stesse aggravano la cognizione.
- 🎯 **Implicazione per la missione, da guardare in faccia.** La strategia "guadagnare tempo" contiene implicitamente l'idea che **ridurre il carico di crisi protegga lo sviluppo**. Questi dati dicono che, in WWOX, **il danno di sviluppo precede le crisi e non risponde al loro controllo**. Il caso 1 ne è l'illustrazione: gli spasmi si sono **risolti** col vigabatrin, e a due anni il bambino era **profondamente ritardato** comunque.
  - **Cosa NON segue**: che controllare le crisi sia inutile. Restano ragioni solide e indipendenti — qualità di vita, prevenzione dello stato epilettico (causa di morte documentata in Abdel-Salam), riduzione del rischio di SUDEP, sonno, gestibilità familiare.
  - **Cosa segue, e va corretto nel nostro modello**: il beneficio atteso dal controllo delle crisi **non va contato come protezione dello sviluppo cognitivo**. E l'ipotesi che stabilizzare la rete protegga indirettamente la mielina ([[therapeutic_hypotheses_ledger_current#HYP-20260709-07 — Pro-mielinizzanti per la finestra mielinica, **condizionata a un esperimento che nessuno ha ancora fatto**|HYP-20260709-07]], riorientata ieri) **si indebolisce**: se il controllo delle crisi non migliora l'esito neurologico, l'inferenza "meno crisi → più mielina → migliore sviluppo" perde il suo anello finale.
  - **Cosa resta rafforzato, per contrasto**: le leve che agiscono **sulla causa** — terapia genica, rescue proteostatico dell'allele Q230P — sono le uniche che il modello DEE prevede possano modificare l'esito di sviluppo. Il che è coerente con Obeid 2026, dove il rescue **neuronale precoce** (non il controllo delle crisi) recupera comportamento, mielina e sopravvivenza.
- **Belief**: medio-alto. È un'osservazione clinica su casistica piccola, ma converge con Oliver 2023 (l'unico paziente non farmaco-resistente è morto a 8 anni: **la responsività ai farmaci non protegge la sopravvivenza**) e con Obeid 2026 (il rescue causale funziona; nessun antiepilettico lo fa).
- **Interconnessioni**: [[discovery_ledger_current#DL-MECH-030 — Genotipo e mortalità in WWOX-DEE: il dato prognostico più diretto che esista per il genotipo di riferimento (e i suoi limiti)|DL-MECH-030]] (Oliver), [[therapeutic_hypotheses_ledger_current#HYP-20260709-07 — Pro-mielinizzanti per la finestra mielinica, **condizionata a un esperimento che nessuno ha ancora fatto**|HYP-20260709-07]] (da indebolire), [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]] (rafforzata per contrasto), [[gold_is_in_the_details]] (la mappa delle leve va letta alla luce di questo)

### 🟢 DL-MECH-040 — Un **fenotipo intermedio** esiste, ed è documentato proprio nella classe genotipica del genotipo di riferimento (null + missense)
- **Status**: open · **Tag**: DATO (clinico, n=2 fratelli) + INFERENZA (trasferimento al genotipo di riferimento, con una riserva importante)
- **Fonte**: Shaukat 2018 (PMID 30361190), Discussione + Table 1, che ricompila Mignot et al. 2015 (casi 3 e 4)
- **Finding (DATO)**: due fratelli **compound eterozigoti** per una **frameshift** (`c.45_48delGGAC`, p.Asp16Serfs*63) e un **missense** (`c.140C>G`, **p.Pro47Arg**). Gli autori: *"These children had profound developmental delay as well as severe epilepsy and epileptic encephalopathy, **however, they did not have spastic quadriplegia, microcephaly or abnormality on cranial MRI**. This could be considered an **intermediate phenotype** which supports genotype-phenotype correlation."* Nella Table 1 risultano infatti: microcefalia **assente**, morte precoce **assente**, **RMN normale**.
- **Rilevanzal genotipo di riferimento — e la riserva che la limita.** il genotipo di riferimento è di classe **null + missense**: la stessa classe genotipica. Questo è il **primo dato clinico positivo** che vedo per quella classe: mostra che è possibile avere ritardo profondo ed epilessia severa **senza** microcefalia, **senza** tetraparesi spastica e **con RMN normale** — cioè senza il quadro neurodegenerativo progressivo dei null biallelici.
  ⚠️ **La riserva è seria e non va nascosta**: il missense di quei fratelli è **P47R**, nel dominio **WW1**, un residuo **superficiale** che ([[discovery_ledger_current#⭐ DL-MECH-037 — Q230P è **l'unica delle tre varianti a essere una lesione di ripiegamento del core**. Il ΔΔG non lo diceva; la sepoltura sì.|DL-MECH-037]]) **non è una lesione di ripiegamento** — plausibilmente lascia proteina. Il missense del genotipo di riferimento è **Q230P**, nel core del **SDR**, e il dato wet di Johannsen dice che **azzera la proteina**. **Sul piano proteico, il genotipo di riferimento potrebbe assomigliare più a un null/null che a questi fratelli.** Le due letture — classe genotipica favorevole, meccanismo proteico sfavorevole — **coesistono e non si annullano**. È esattamente la tensione già registrata in [[discovery_ledger_current#🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica|DL-MECH-034]].
- **Consolida anche**: 23/23 pazienti a registro in questa review hanno ritardo severo **ed** epilessia, **qualunque** sia la classe genotipica; la tetraparesi spastica è invece 14/23 — cioè **è la spasticità, non l'epilessia, a discriminare i fenotipi**.
- **Belief**: alto sul dato riportato; medio-basso sul trasferimento al genotipo di riferimento, per la riserva sopra.

### DL-MECH-041 — Polimicrogiria: WWOX tocca anche la **migrazione neuronale** (e una review recente lo nega)
- **Status**: open · **Tag**: DATO (n=2, due studi indipendenti) — **contraddice una fonte secondaria**
- **Fonte**: Shaukat 2018 (caso 2: **polimicrogiria parietale/posteriore bilaterale**, RMN a 2 mesi) + Ben-Salem 2015 (polimicrogiria frontoparietale destra), via Table 1
- **Finding**: gli autori concludono che *"WWOX may play a role in neuronal migration"* e che servono più casi per confermarlo come gene di malformazione dello sviluppo corticale.
- ⚠️ **Conflitto con [[discovery_ledger_current#DL-MECH-042 — Il quadro di neuroimaging del WOREE: cosa è costante, cosa progredisce, cosa non sappiamo misurare|DL-MECH-042]]** (Battaglia 2023, mini-review neuroimaging), che afferma l'assenza di polimicrogiria nel WOREE riportando solo un "pattern girale semplificato". **La review secondaria omette due casi primari.** → Ulteriore istanza di [[discovery_ledger_current#^fm-010|FM-010]]: le review non sostituiscono i primari.
- **Rilevanza di malattia**: se WWOX partecipa alla migrazione neuronale, una parte del danno è **prenatale e strutturale**, quindi fuori dalla portata di qualunque leva postnatale. È un limite reale alla finestra terapeutica, coerente con la RMN fetale a 21 settimane che mostra già ipoplasia del verme.

### DL-MECH-042 — Il quadro di neuroimaging del WOREE: cosa è costante, cosa progredisce, cosa non sappiamo misurare
- **Status**: open · **Tag**: DATO (compilazione secondaria) + limiti metodologici seri
- **Fonte**: Battaglia et al. 2023, *Front Pediatr* (PMID 38161429, PMC10757851) — **full text letto integralmente**. **Mini-review narrativa**, non sistematica: 101 casi da 9 studi, ma le coorti **si sovrappongono** (Banne n=56 ricompila casi già pubblicati) → **nessuna prevalenza aggregata è calcolabile**; solo percentuali intra-studio sono oneste.
- **Reperto più costante (DATO)**: **corpo calloso ipoplasico/sottile — presente in tutti e 9 gli studi.** Poi: atrofia cerebrale (7/9), iperintensità simmetriche T2 della sostanza bianca, atrofia ottica, ritardo di mielinizzazione, atrofia ippocampale.
- **Precocità (DATO)**: anomalie già a **15-19 giorni di vita** (corpo calloso sottile + ritardo di mielinizzazione + atrofia frontotemporale). **RMN fetale a 21 settimane**: lieve **ipoplasia del verme cerebellare**, con **girazione e laminazione corticale normali per l'età**. → il primo segno rilevabile è cerebellare.
- **Progressione (DATO)**: documentata su imaging seriato in Tabarki (5/5) e Oliver (7/13) — "pattern di neurodegenerazione", da atrofia lieve a severa.
- ⚠️ **Correzione a un mio prior**: avevo scritto che l'atrofia ottica è "100% a tutte le età" (da Oliver). Vero **solo nella coorte Oliver**, dove è stata cercata sistematicamente; negli altri 7 studi **non è tabulata** → **sotto-accertata, non universale**. Da non generalizzare.
- ⚠️ **Correzione a un altro mio prior — e conta.** Avevo scritto (da Elsaadany) "**demielinizzazione progressiva**". Questa review — che non cita Elsaadany — usa sistematicamente il linguaggio di **ritardo di mielinizzazione / ipomielinizzazione**, e documenta la progressione dell'**atrofia**, non una demielinizzazione mielino-specifica. **La distinzione è terapeuticamente decisiva**: un ritardo di mielinizzazione è in linea di principio recuperabile; una demielinizzazione progressiva molto meno. **La questione resta aperta**, e la letteratura pende verso "ipomielinizzazione + neurodegenerazione atrofica", non verso "demielinizzazione". Non usare più "demielinizzazione progressiva" come se fosse stabilito.
- 💎 **il genotipo di riferimento, esplicitamente nominata dalla letteratura**: la review scrive che *"the **p.Gln230Pro** pathogenic variant affects the S[D]R domain and has been described both in homozygosity and in compound heterozygosity in **eight cases overall**. Nevertheless, **how missense variants affecting the SDR domain impair WWOX catalytic activity has not been demonstrated yet**."* → Q230P è un **hotspot ricorrente riconosciuto** (8 casi), e **il meccanismo con cui i missense SDR aboliscono la funzione non è dimostrato**. È letteralmente lo spazio di ricerca di [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]], dichiarato aperto da una review del 2023.
- **MRS (rilevante per la contraddizione lattato)**: unica menzione = paziente 1 di Johannsen, **spettroscopia normale**. Nessun valore di lattato riportato. Sommato ai lattati **normali** dei due pazienti di Shaukat e allo screening metabolico normale di Abdel-Salam, il quadro umano è: **metabolismo periferico e MRS sostanzialmente normali**, contro un topo che muore di ipoglicemia con lattato sierico alto.
- **Gap che la review lascia scoperto (DATO, assenza verificata)**: **nessuna metrica quantitativa** — nessuna volumetria, nessuna area medio-sagittale del corpo calloso, nessun DTI/FA, nessun indice di mielinizzazione, nessuna MRS strutturata, nessun protocollo di monitoraggio oftalmologico (né OCT, né ERG, né VEP). → **Se serve un endpoint di imaging per il genotipo di riferimento, va progettato da noi.** Candidati: area medio-sagittale del CC (il reperto più costante e più precoce), volumetria frontotemporale, lesion-load T2, tutti su **stesso scanner e stessa sequenza a intervalli fissi**.

### DL-BIO-009 — Il metabolismo umano nel deficit di WWOX è, per quanto misurato, **normale**. Il modello murino non si trasferisce.
- **Status**: open · **Tag**: DATO (convergenza di 4 fonti umane) — **chiude parzialmente [[discovery_ledger_current#DL-BIO-006 — circRNA KIRKOS + WWOX mRNA esosomale come readout liquido del locus|DL-BIO-006]]**
- **Fonti**: Shaukat 2018 (entrambi i pazienti: **lattato, ammonio, acilcarnitine, acido urico, omocisteina, aminoacidi plasmatici, acidi organici urinari, isoforme della transferrina — tutti normali**) · Abdel-Salam 2014 (screening metabolico e mitocondriale interamente normale, biopsia muscolare inclusa) · Battaglia 2023 (MRS normale nel paziente 1 di Johannsen) · Davids 2019 (MRS: lattato cerebrale "estremamente basso", aminoacidi non essenziali ridotti — **l'unico outlier, in un paziente con una seconda variante confondente in HSPG2**).
- **Contro**: topo Wwox-KO → **ipoglicemia letale, lattato sierico aumentato, morte a 3-4 settimane** (Abu-Remaileh 2014); organoidi cerebrali umani WWOX-KO → **OXPHOS ridotta, glicolisi aumentata** a livello trascrittomico (Steinberg 2021).
- **Sintesi onesta**: il fenotipo metabolico è **robusto nel topo e nel modello cellulare, ma non si manifesta come anomalia biochimica misurabile nei pazienti umani.** Le due cose non sono necessariamente in contraddizione — un difetto bioenergetico *neuronale* può esistere senza alterare il metabolismo sistemico o il lattato periferico — ma **significa che oggi non abbiamo alcun biomarcatore metabolico utilizzabile nel genotipo di riferimento**, né periferico né di imaging.
- **Conseguenze operative**:
  1. [[discovery_ledger_current#DL-BIO-005 — Pannello funzionale WWOX–HIF1α/GLUT1/PKM2 + alanina|DL-BIO-005]] (lattato) resta **declassato**; il declassamento è ora sostenuto da 4 fonti umane, non da una.
  2. **[[therapeutic_hypotheses_ledger_current#HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)|HYP-20260709-01]] (dieta chetogenica) va ricalibrata**: il suo razionale poggia sul deficit bioenergetico neuronale documentato in organoidi e MEF, **non** su alcuna anomalia metabolica misurabile nel paziente. **L'unico test che può falsificarla resta il Seahorse su cellule donor-derived.** Se anche quello risultasse normale, l'ipotesi cade.
  3. Non cercare conferme nel sangue: **sono già state cercate, quattro volte, e sono normali.**

---

## Failure mode registrati (run 2026-07-10c)

- **FM-018 — Un razionale meccanicistico in vitro non è una predizione clinica, e non va usato come tale.** Ieri, dagli organoidi (GABA depolarizzante), avevo inferito che i farmaci GABAergici dovessero rendere poco in WWOX-DEE. Oggi, da un paper a corpus e mai letto, scopro che **il vigabatrin ha risolto gli spasmi** in un bambino WWOX-null. Il meccanismo resta valido come meccanismo; **la predizione clinica era mia, non del dato.** → Quando un modello in vitro suggerisce una conseguenza terapeutica, **cercare prima se esiste il dato clinico**, che spesso è già pubblicato. ^fm-018
- **FM-019 — Una review secondaria può omettere reperti primari.** Battaglia 2023 nega la polimicrogiria nel WOREE; Shaukat 2018 e Ben-Salem 2015 la documentano in due pazienti. Seconda istanza di [[discovery_ledger_current#^fm-010|FM-010]] nello stesso ciclo di lavoro.
- **FM-020 — "Demielinizzazione progressiva" era mia, non della letteratura.** L'avevo scritto da un singolo case report (Elsaadany). La letteratura più ampia parla di **ritardo di mielinizzazione** e di **atrofia progressiva**, che non sono la stessa cosa e hanno implicazioni terapeutiche opposte. → Non promuovere il linguaggio di un case report a descrizione di malattia.

---

## Nota di processo 2026-07-10d — Audit dei rilievi di Codex sulla coda CC

### FM-021 — Ho ri-derivato fatti che erano già canonici, perché non avevo caricato i 4 current
- **Come è emerso**: audit incrociato dei rilievi di Codex. Verificando il paper registry ho trovato che **PAPER 011** (Obeid 2026 GT) contiene **già** i "dettagli di design" che credevo di aver estratto per primo dal full-text: *promotore SynI neuronale ottimale vs MBP/CMV; WPRE aumenta WWOX 3–16.7×/regione; espressione durevole fino a P300; finestra terapeutica P1–P5; neuron-specific, fegato negativo*. E la nota di **PAPER 004/005** (Repudi 2021) contiene già: *"restauro neuronale-only → mielinizzazione **non-cell-autonoma**; gliosi downstream della disfunzione neuronale"*.
- **Cioè**: [[discovery_ledger_current#DL-MECH-031 — L'ipomielinizzazione WWOX è **secondaria al neurone**, non un difetto autonomo dell'oligodendrocita. E la finestra della terapia genica è neonatale|DL-MECH-031]] ("l'ipomielinizzazione è secondaria al neurone") e buona parte di quanto ho scritto su Obeid **erano già a registro**, alcuni dal 2026-07-03/05. Non li ho contraddetti — li ho **riscoperti**, spendendo un deep-dive completo.
- **Perché è successo**: ho aperto la sessione in modalità leggera (state manifest + gate + ledger) **senza caricare i 4 current scientifici**. Il gate `unread_gold.py` protegge dal non leggere i `CORPUS` placeholder ad alta rilevanza; **non protegge dall'ignorare il contenuto del registry che già possediamo**.
- **Micro-upgrade proposto** (non ancora implementato): estendere il triage con un **"registry brief"** — per ogni PMID in ingresso, se è già a registro come `PAPER`, stampare le sue `Note` e i `Claim links`, **prima** di decidere il deep-dive. Costo: una lettura mirata. Beneficio: evita di ri-derivare ciò che sappiamo già, e trasforma il deep-dive in *upgrade mirato* invece che in ri-analisi.
- **Distinzione onesta**: il deep-dive **non** è stato inutile — ha aggiunto il **confounder dichiarato dagli autori** sul braccio AAV-oligodendrocitario (tropismo AAV9), il limite metodologico della mielina (solo MBP-IHC, no g-ratio/EM) e il vincolo BLOCCO 1 sul rescue supra-fisiologico. Ma il *finding principale* era già nostro.

### FM-022 — Tre errori strutturali nei miei CC, rilevati da Codex e confermati
1. **Target WM obsoleto.** I miei CC dichiarano `target_wm_version: WM_v1.8` / `WM_v1.9`. **Il Working Model corrente è `WM_v2.0_2026-07-10`** (aggiornato da `URGENT_20260710_001`, che ha anche chiuso l'URGENT cat-5: `pending_urgent_requests: []`). Tutti i miei target vanno **ribasati su v2.0**.
2. **Collisione di PAPER ID su Steinberg 2021.** `CC-2026-07-05-006` propone **PAPER 039**; il mio `CC-2026-07-10-001` propone **PAPER 049** per lo stesso PMID 34268881. Se entrambi venissero propagati, **lo stesso studio entrerebbe due volte con due ID diversi**. Errore mio: ho assegnato un ID nuovo senza controllare le prenotazioni della coda.
3. **Obeid 2026 non è un nuovo PAPER.** Il mio `CC-2026-07-09-004` propone di crearlo come **PAPER 048**. **È già PAPER 011.** Va trattato come **upgrade** (arricchimento di note + eventuale claim_update), non come nuova entry.
- **Causa comune**: ho assegnato ID PAPER localmente, guardando solo il `max` del registry (032) e le prenotazioni che *conoscevo*, invece di derivarli da un'assegnazione centrale sulla coda intera. → **L'assegnazione degli ID PAPER va fatta in un unico passo di riconciliazione pre-commit, non dentro i singoli CC.** È esattamente ciò che Codex propone, ed è corretto.

---

## Nota metodologica 2026-07-10e — Perché la classificazione null/missense è un **proxy rumoroso**, e cosa implica per il genotipo di riferimento

> Sollevata dall'operatore. È corretta, e verificandola sui file risulta **più forte** di come l'avevo formulata. Va scritta *dentro* il claim, non solo qui.

### DL-MECH-043 — `null` vs `missense` classifica la **sintassi della variante**, non la **funzione residua della proteina**
- **Status**: open · **Tag**: INFERENZA metodologica (fondata su DATO)
- **Il fatto (DATO, verificato)**: Oliver 2023 codifica *"each **pathogenic/likely pathogenic** variant… as either **null** (frameshift, nonsense, donor/acceptor splice site, deletion) or **missense**"*. La classe è dedotta **dal tipo di lesione nel DNA**, mai dall'effetto misurato sulla proteina.
- **Perché è un proxy rumoroso, con le nostre stesse prove:**
  1. **Un "missense" può essere funzionalmente null.** Johannsen 2018: **Q230P** → trascritto normale, **proteina assente** ([[discovery_ledger_current#🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica|DL-MECH-034]]). Sintatticamente missense; funzionalmente amorfo.
  2. **Un "missense" può conservare proteina e perdere solo una funzione.** Mallaret 2014: **P47T** → proteina a livelli **normali**, binding PPxY **abolito**, fenotipo **lieve**.
  3. **Lo stesso residuo, due sostituzioni, due classi cliniche.** **P47T** → SCAR12 lieve; **P47R** → WWOX-DEE severo. Identica posizione, identica etichetta "missense".
  4. **Un "null" può essere leaky.** Splicing aberrante parziale, read-through, isoforme alternative: la nota di Davids 2019 documenta la **sovraespressione compensatoria di un'isoforma corta** priva del dominio SDR — abbondanza senza funzione.
  → Dentro l'etichetta "missense" convivono **almeno tre meccanismi distinti** (proteina normale/funzione persa · proteina assente · proteina ridotta/funzione parziale). L'etichetta non li distingue.
- **Conseguenza statistica (INFERENZA, e non è un tecnicismo)**: la misclassificazione qui è verosimilmente **non differenziale** rispetto all'esito → il suo effetto atteso è di **diluire** la differenza vera fra le classi verso il nullo. Cioè: il `p = .0085` di Oliver potrebbe essere una **sottostima** della separazione reale fra *"funzione residua presente"* e *"assente"*. **La variabile biologica vera è la funzione residua; null/missense ne è solo l'ombra.** Questo taglia in entrambe le direzioni e non favorisce nessuna prognosi.
- **Corollario che rafforza il programma**: se la variabile che conta è la funzione residua, allora **misurarla** (Western + pulse-chase + assay funzionale su cellule donor-derived, [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]]) vale più di qualunque raffinamento della classificazione genetica.

### DL-MECH-044 — Il caso del genotipo di riferimento è **doppiamente fuori scala** rispetto alla classificazione
- **Status**: open · **Tag**: DATO (stato di classificazione) + INFERENZA
- **(a) Un allele è VUS.** Il manifest registra, per l'allele di sito accettore `c.1057-2A>G`: **`ClinVar = VUS`**. Il supporto alla patogenicità è **in-silico** (VEP GRCh38 + **SpliceAI DS_AL 0.96** acceptor-loss + DS_AG 0.64 sito criptico +8 + **MaxEntScan Δ −7.95**) e il record pubblico di variante giudica *"eliminazione esone 9 altamente probabile"*. **Nessun dato di RNA su cellule donor-derived è mai stato prodotto.**
  ⚠️ **Implicazione diretta, e va detta**: Oliver arruola **solo varianti pathogenic/likely pathogenic**. Con un allele VUS, **il genotipo di riferimento non sarebbe stata arruolabile in quella coorte.** La curva di sopravvivenza per la classe `≥1 missense` **non descrive una popolazione di cui sappiamo con certezza che il genotipo di riferimento rientri.** Non è un dettaglio burocratico: è la validità esterna del dato prognostico.
- **(b) L'altro allele è "missense" per sintassi e null-like per funzione.** Il missense SDR: proteina non rilevata (Johannsen; causa non risolta). Sul piano proteico di riferimento potrebbe assomigliare a un **null/null** pur essendo formalmente `null/missense`.
- **Le due incertezze puntano in direzioni opposte** e **non si compensano**: (a) mette in dubbio che il genotipo di riferimento appartenga alla classe favorevole *e persino* che la diagnosi biallelica sia stabilita con certezza formale; (b) suggerisce che, anche appartenendovi, il vantaggio di classe non le si applichi. **Nessuna delle due autorizza né ottimismo né pessimismo.** Autorizzano una sola cosa: **misurare.**
- 🎯 **Conseguenza operativa di alto valore — l'assay dell'esone 9 ha un secondo motivo, indipendente e più immediato.**
  Finora [[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]] e [[therapeutic_hypotheses_ledger_current#HYP-20260709-06 — Assay di inclusione dell'esone 9 come biomarcatore abilitante e endpoint dell'ASO|HYP-20260709-06]] giustificavano la RT-qPCR sulla giunzione esone 8→9 come **endpoint di efficacia per un futuro ASO**. Ma quello stesso esperimento, fatto oggi su cellule donor-derived, **testerebbe se l'allele di sito accettore altera davvero lo splicing** — cioè fornirebbe l'evidenza funzionale (criterio ACMG **PS3**) che può **riclassificare la VUS** da incerta a patogenetica.
  Un esperimento, due risultati: (1) conferma (o smentisce) la base molecolare della diagnosi; (2) fissa il baseline per misurare un ASO. **È il test più economico con la resa più alta del programma, e non dipende da nessuna ipotesi terapeutica.**
- **Belief**: alto sui fatti (stato VUS, criterio di arruolamento di Oliver, dato di Johannsen); l'inferenza sulla non-arruolabilità è meccanica, non speculativa.
- **Interconnessioni**: [[claim_registry_current#CLAIM 019]], [[discovery_ledger_current#DL-BIO-002 — Trascritto/proteina dell'allele di sito accettore, nominati dalla predizione di skipping esone 9 (SpliceAI/Pangolin)|DL-BIO-002]], [[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-06 — Assay di inclusione dell'esone 9 come biomarcatore abilitante e endpoint dell'ASO|HYP-20260709-06]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]]

### FM-023 — Avevo scritto la riserva nel posto sbagliato
La riserva su CLAIM 031 ("il vantaggio della classe ≥1 missense potrebbe non applicarsi al genotipo di riferimento") era una **nota nel ledger**. Ma un claim canonico viene letto **da solo**, fuori dal contesto del ledger. Se entra senza la riserva **dentro** il claim, il registro afferma implicitamente una prognosi più favorevole di quanto i dati sostengano — su una bambina reale. → **Le riserve che qualificano un claim vanno nel claim.** Il ledger non è un disclaimer.

---

## Run 2026-07-10f — "Conoscere per gestire". Applicando il criterio, due leve cambiano forma.

> L'operatore ricalibra l'essenza di LEGEND: non classificare la gravità (la clinica la vede già), ma **cercare soluzioni** — per tutti i WWOX-LoF *e* per il genotipo di riferimento. Applicato come filtro a ciò che sappiamo, produce subito due correzioni strutturali e un lead nuovo.

### 🔴 DL-MECH-045 — L'esone 9 è **l'ultimo esone**: l'allele di sito accettore del genotipo di riferimento non è un "null silente", ma probabilmente produce una **proteina tronca instabile**
- **Status**: open · **Tag**: INFERENZA forte (regole di splicing/NMD applicate a dati verificati) — **non** DATO
- **Fatti verificati**:
  1. **WWOX ha nove esoni** (Shaukat 2018, PMID 30361190: *"contains nine exons"*). Quindi **l'esone 9 è l'ultimo**.
  2. L'allele di sito accettore `c.1057-2A>G` distrugge il **dinucleotide AG invariante** dell'accettore dell'introne 8 → esone 9. `c.1057` corrisponde al **codone 353**: l'esone 9 codifica gli ultimi ~62 amminoacidi (C-terminale del dominio SDR).
  3. Predizione in-silico già a registro: **SpliceAI DS_AL 0.96** (perdita accettore) + **DS_AG 0.64** (sito criptico a +8); **MaxEntScan Δ −7.95**.
- **L'inferenza (e perché conta)**: la sorveglianza NMD degrada i trascritti con codone di stop prematuro **solo se il PTC si trova a monte dell'ultima giunzione esone-esone** (regola dei ~50-55 nt). Tutti gli esiti plausibili di questa variante — uso del sito criptico +8 (frameshift), ritenzione dell'introne 8, skipping dell'ultimo esone — collocano il PTC **a valle dell'ultima giunzione**. → **NMD-escape**: l'mRNA dell'allele di sito accettore è verosimilmente **stabile**, e viene **tradotto** in una proteina tronca priva della porzione C-terminale del SDR.
- **Corroborazione sperimentale, e viene dal ratto *lde***: una **delezione di 13 bp nell'esone 9** (`c.1190_1202del`, `p.Leu371Thrfs*`) — cioè la **stessa regione, stesso tipo di conseguenza** — produce **mRNA presente** ma proteina **quasi non rilevabile**: al Western resta solo una banda debolissima di 46.2 kDa, interpretata come **mutante instabile sfuggito alla degradazione** ([[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile|DL-MECH-027]], Tochigi 2019). **Non "niente": pochissimo, e instabile.**
- 🎯 **Conseguenze, tutte azionabili:**
  1. **L'assunzione "allele di sito accettore = null silente" va corretta.** È più probabile: *trascritto stabile → proteina tronca → degradata*. Il fenotipo funzionale è null; **il meccanismo non lo è.**
  2. **L'assay RT-qPCR esone 8→9 va riprogettato.** Se l'mRNA sfugge a NMD, il trascritto aberrante **c'è**, e un semplice calo del rapporto es8-9/core **non si osserverà**. Serve un assay che discrimini la **sequenza della giunzione** (RT-PCR + Sanger, o RNA-seq mirata), non solo l'abbondanza. **Questo salva l'esperimento dal produrre un falso negativo.** → correggere [[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]] e [[therapeutic_hypotheses_ledger_current#HYP-20260709-06 — Assay di inclusione dell'esone 9 come biomarcatore abilitante e endpoint dell'ASO|HYP-20260709-06]].
  3. **Un Western su cellule donor-derived potrebbe mostrare due difetti distinti**: proteina tronca (dall'allele di sito accettore) + proteina assente (dall'allele missense). Vanno cercate entrambe, con anticorpi che riconoscano epitopi **N-terminali** (per vedere il tronco) e **C-terminali** (per distinguerlo dal full-length).
  4. ⚠️ **Domanda di sicurezza aperta**: una proteina tronca, anche in tracce, è **inerte** o ha effetti (dominante-negativa? aggregante?)? Nel *lde* omozigote il fenotipo è severo, coerente con perdita di funzione — ma il *lde* non testa la tossicità del tronco.
- **Belief**: alto sulle premesse (9 esoni; posizione della variante; regola NMD; dato del *lde*); **medio** sull'esito preciso dello splicing, che **nessuno ha misurato nel genotipo di riferimento**.

### 🔴 DL-MOL-011 — Un ASO **non può ripristinare un sito accettore canonico distrutto**. `TX-001` va riclassificato; la leva corretta è l'editing.
- **Status**: open · **Tag**: INFERENZA forte (biologia degli SSO) — **corregge una priorità di Layer 9**
- **Il problema**: `TX-001` in [[therapeutic_strategies_current#TX-001 — Correcting a canonical splice-acceptor allele: RNA assay → ASO/editing choice|TX-001]] è marcata *"ASO splice-modulante su c.1057-2A>G — ⭐ PRIORITÀ"*. Ma gli oligonucleotidi splice-switching agiscono **mascherando elementi** dell'mRNA: siti criptici, silencer/enhancer esonici, pseudo-esoni. **Non creano siti di splicing.** La variante del genotipo di riferimento colpisce il **dinucleotide AG invariante** dell'accettore: lo spliceosoma **non ha più nulla da riconoscere** in quella posizione. Nessun ASO può ricostruirlo.
  - Un ASO potrebbe al massimo **mascherare il sito criptico +8**, costringendo lo spliceosoma a cercare altrove — ma il risultato non sarebbe il trascritto wild-type, bensì un altro prodotto aberrante (skipping o criptico ulteriore). **Non è correzione.**
  - Le eccezioni note non si applicano: gli **U1 snRNA modificati** correggono siti **donatori** (5′), non accettori; l'**editing dell'RNA via ADAR** converte A→I (letto come G) — **la direzione sbagliata**, qui serve G→A.
- ✅ **La leva corretta esiste, ed è concreta.** La variante è `A>G` in posizione −2. Sul **filamento antisenso** ciò corrisponde a `T→C`. Un **cytosine base editor (CBE)** che esegua **C→T sull'antisenso** ripristina la `A` sul senso e **ricostruisce l'accettore AG**. In alternativa, il **prime editing** consente qualunque sostituzione puntiforme. → **La correzione dell'allele di sito accettore è un problema di *editing del DNA*, non di ASO.**
- 🎯 **Implicazione strategica (e va detta all'operatore senza girarci intorno)**: la leva 1 del portafoglio (correzione dello splicing via ASO sull'allele di sito accettore) **poggia su un meccanismo che non può funzionare**. Va **retrocessa**, e sostituita da:
  - **TX-001-bis — base editing (CBE) / prime editing su `c.1057-2A>G`**: `IPOTESI`. Molto lontana dalla clinica (delivery al CNS, off-target, bystander editing), ma **meccanicisticamente valida**, mentre l'ASO non lo è.
  - L'ASO **resta pertinente** per altri usi in WWOX (es. inibizione di un repressore), **non** per correggere questa variante.
- **Cosa NON cambia**: l'assay dell'esone 9 resta prezioso — non più come "endpoint per l'ASO", ma (a) per **riclassificare la VUS** (ACMG PS3) e (b) come baseline per **qualunque** strategia di correzione, editing incluso.
- **Belief**: alto sul principio (è biologia standard degli SSO); **da sottoporre a verifica esterna** prima di retrocedere formalmente TX-001 — è una correzione importante e va sbagliata il meno possibile. → `legend-aso-designer` deve confermare o confutare.
- **Interconnessioni**: [[therapeutic_strategies_current#TX-001 — Correcting a canonical splice-acceptor allele: RNA assay → ASO/editing choice|TX-001]], [[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]], [[discovery_ledger_current#🔴 DL-MECH-045 — L'esone 9 è **l'ultimo esone**: l'allele di sito accettore del genotipo di riferimento non è un "null silente", ma probabilmente produce una **proteina tronca instabile**|DL-MECH-045]], [[therapeutic_hypotheses_ledger_current#HYP-20260709-06 — Assay di inclusione dell'esone 9 come biomarcatore abilitante e endpoint dell'ASO|HYP-20260709-06]]

### 🟢 DL-MOL-012 — **Q230P è un hotspot ricorrente (8 casi)**: una soluzione "per il genotipo di riferimento" è una soluzione per una sotto-popolazione
- **Status**: open · **Tag**: DATO (conteggio in letteratura) + INFERENZA strategica
- **Fonte**: Battaglia et al. 2023 (PMID 38161429): *"the **p.Gln230Pro** pathogenic variant affects the SDR domain and has been described both in homozygosity and in compound heterozygosity in **eight cases overall**. Nevertheless, **how missense variants affecting the SDR domain impair WWOX catalytic activity has not been demonstrated yet**."* Confermato da Oliver 2023: Q230P è **il missense più ricorrentemente riportato** (famiglie da Iran, Afghanistan, Francia, Marocco), presente in omozigosi (pazienti 2 e 5) e in compound eterozigosi (paziente 1).
- 🎯 **Perché ricalibra il portafoglio**: avevo classificato [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]] (rescue proteostatico di Q230P) come leva **"il genotipo di riferimento-specifica"**, implicitamente n-of-1. **È sbagliato.** Q230P è una variante **ricorrente e riconosciuta**, con almeno 8 casi noti in 4+ Paesi, e nessuno ha dimostrato il suo meccanismo. Un chaperone che stabilizzi Q230P servirebbe a una **sotto-popolazione identificabile**, non a un singolo individuo.
- **Conseguenze pratiche**: (a) un lab o un finanziatore ha un incentivo che una n-of-1 non offre; (b) esiste già una **coorte reclutabile** per un endpoint funzionale; (c) l'esperimento chiave — *la proteina Q230P ristabilizzata è funzionale?* — è **una domanda aperta dichiarata dalla letteratura**, non una nostra curiosità.
- **Il modo giusto di presentarlo**: non *"aiutateci con un singolo caso"*, ma *"il meccanismo del missense SDR più ricorrente in WWOX non è mai stato dimostrato; abbiamo un'ipotesi, un controllo negativo (G372R) e la cellula per testarla."*
- **Interconnessioni**: [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]], [[discovery_ledger_current#DL-MOL-010 — Il banco per testare HYP-08 esiste già. Manca un solo reagente, e il genotipo di riferimento lo possiede.|DL-MOL-010]] (banco Aqeilan), [[claim_registry_current#CLAIM 019]]

### FM-024 — Il filtro mancante: "questa conoscenza cambia una decisione?"
Rileggendo il ledger col criterio dell'operatore, molti item sono **conoscenza di stato** (quale pathway è disregolato, quanto è grave, quale reperto è più frequente) e pochi sono **leve** (cosa possiamo fare, e cosa lo sblocca). La conoscenza di stato serve **solo se vincola una leva**. → **Nuovo campo obbligatorio** per ogni item del discovery ledger e per ogni claim proposto:
`actionability:` **quale leva tocca** · **quale esperimento/decisione sblocca** · **chi ne beneficia** (`tutti i WWOX-LoF` / `sotto-popolazione` / `solo il genotipo di riferimento`) · oppure `none — background`.
Un item con `actionability: none` non è un errore: è **background dichiarato**, e non compete per la prima fila di un batch.
**Prima applicazione**: `CLAIM 031` (genotipo↔mortalità) ha `actionability: none` — descrive la gravità, che la clinica già mostra. **Retrocesso da Batch A a Batch B.**

---

## Run 2026-07-10g — Verifica ASO. La tesi regge. E per verificarla ho trovato la soglia terapeutica.

### 🥇 DL-MECH-046 — **L'aploinsufficienza di WWOX non è deleteria.** Il bersaglio non è il 100%: è molto meno.
- **Status**: open · **Tag**: **DATO** (topo, ratto, e ogni famiglia umana pubblicata) · **actionability**: ridefinisce la soglia di successo di **ogni** leva del portafoglio · **beneficia**: tutti i WWOX-LoF
- **Fonti e citazioni verbatim**:
  - **Aldaz 2014** (PMID 24932569, full text): *"loss of one Wwox allele (i.e. **haploinsufficiency**) appears **not to be deleterious** or carcinogenic in the longer-lived heterozygous mice"*; *"The lifespan of the Wwox heterozygotes was **indistinguishable from WT mice**"*; *"loss of a single Wwox allele… **did not have any observable phenotypic effect** in the mammary gland"*.
  - **Tochigi 2019** (PMID 31340538, full text): i ratti **`+/lde`** mostrano *"a single band of normal molecular weight, but its intensity was **almost half** that observed in +/+ rats"*; l'immunoistochimica è **intensa** in corteccia e corpo calloso come nei `+/+`, e **assente** nei `lde/lde`. → **metà proteina, cervello normale.**
  - **Ogni famiglia umana pubblicata**: i genitori portatori (Shaukat, Elsaadany, Abdel-Salam, Mallaret, Johannsen — tutte consanguinee) sono **eterozigoti sani**.
  - **Topo ipomorfo `Wwox^gt/gt`** (proteina bassa **ma rilevabile**): **vitale**, vita accorciata. Topo null: morte a 3-4 settimane.
- 🎯 **Perché è il fatto più importante del programma, e nessuno di noi l'aveva messo a fuoco come *soglia*:**
  - **Circa il 50% della proteina WWOX basta per un fenotipo normale.** E poiché l'**ipomorfo** (ben sotto il 50%) è **vitale** mentre il null muore, **la soglia fra letale e vitale sta da qualche parte sotto il 50%** — non sappiamo dove, ma sappiamo che **non è al 100%**.
  - **Correggere un solo allele basta, in linea di principio.** Se l'editing riparasse l'allele di sito accettore, il genotipo di riferimento diventerebbe geneticamente equivalente a un **portatore sano**. Se il rescue proteostatico recuperasse abbastanza proteina Q230P funzionale, idem.
  - **Non serve efficienza alta.** È il corollario che cambia la fattibilità. Base editing, prime editing e terapia genica hanno tutti efficienze **modeste** in vivo, e non trasducono ogni cellula. Se l'aploinsufficienza è tollerata, **un mosaicismo terapeutico parziale può bastare**. L'asticella di ogni leva del portafoglio si abbassa.
  - **Il "parziale conta" della missione ha ora un fondamento quantitativo**, non retorico. Un rescue del 20-30% non è un premio di consolazione: potrebbe essere **sopra la soglia**.
- ⚠️ **I limiti, che non vanno taciuti**: (a) la soglia è nota per **sopravvivenza e morfologia**, non per **cognizione ed epilessia** — nessuno ha misurato quanta WWOX serve al *neurosviluppo*; (b) l'aploinsufficienza è tollerata **dalla nascita**, mentre un rescue nel genotipo di riferimento arriverebbe **dopo** che parte del danno di sviluppo è avvenuto (e ricordiamo: è una **DEE**, [[discovery_ledger_current#🔴 DL-MECH-039 — È una **DEE, non una EE**: controllare le crisi non salva lo sviluppo. E questo tocca la logica stessa di "guadagnare tempo".|DL-MECH-039]]); (c) nei topi eterozigoti è documentato un **aumento di tumorigenicità sotto carcinogeni** — irrilevante per una strategia che *aumenta* WWOX, ma da non dimenticare.
- **L'esperimento che fisserebbe la soglia**: curva dose-risposta di WWOX (allelic series ipomorfa, o GT a dosi scalari) contro endpoint **neurologici** — ECoG/SWD, mielina, comportamento. Obeid 2026 ha già la dose-risposta (LD/HD): **rileggerlo per estrarre la soglia minima efficace** è lavoro a costo zero e ad alta resa.
- **Interconnessioni**: [[therapeutic_hypotheses_ledger_current#HYP-20260709-08 — Allele missense SDR: distinguere difetto di sintesi, insolubilità e turnover prima del rescue proteostatico|HYP-20260709-08]] (il rescue non deve essere completo), [[therapeutic_strategies_current#TX-007 — AAV9-WWOX gene therapy (gene addition) — the north-star, now FIRST-IN-HUMAN ⭐|TX-007]] (GT: non serve trasdurre tutto), [[discovery_ledger_current#🔴 DL-MOL-011 — Un ASO **non può ripristinare un sito accettore canonico distrutto**. `TX-001` va riclassificato; la leva corretta è l'editing.|DL-MOL-011]] (editing: efficienza modesta accettabile), [[gold_is_in_the_details]]

### DL-MOL-013 — VERDETTO sulla tesi ASO: **regge**, con una via RNA che non avevo considerato

- **Aggiorna:** [[discovery_ledger_current#🔴 DL-MOL-011 — Un ASO **non può ripristinare un sito accettore canonico distrutto**. `TX-001` va riclassificato; la leva corretta è l'editing.|DL-MOL-011]]
- **Status**: `stress-tested` · **Tag**: INFERENZA forte (meccanicistica) — **non** DATO
- **Tesi**: un SSO non può correggere `c.1057-2A>G`, perché la variante distrugge l'**AG invariante** dell'accettore dell'esone 9. Gli SSO **mascherano elementi** (siti criptici, ESE/ISE/ESS/ISS, pseudo-esoni); **non creano siti di splicing**. Non c'è nulla da smascherare che restituisca il trascritto wild-type.
- **Controlli condotti, uno per uno:**
  | Via | Verdetto | Motivo |
  |---|---|---|
  | **SSO che maschera il sito criptico +8** | ❌ | Sposterebbe lo splicing verso *un altro* prodotto aberrante (skipping o criptico ulteriore). **Non ripristina il wild-type.** |
  | **Skipping in-frame terapeutico** (logica DMD) | ❌ | L'esone 9 è **l'ultimo**: contiene lo stop e gli ultimi ~62 aa del SDR. Saltarlo perde il C-terminale **e** il codone di stop. Il ratto *lde* prova che perdere il C-term destabilizza la proteina. |
  | **U1 / U7 snRNA modificati (ExSpeU1)** | ❌ | Correggono siti **donatori (5′)**. L'accettore è riconosciuto da U2AF/U2 snRNP, non da U1. Non applicabile. |
  | **Editing dell'RNA via ADAR** | ❌ | ADAR fa **A→I** (letto G). Qui serve **G→A**. Direzione sbagliata; nessun editor RNA fa G→A. |
  | **Trans-splicing (SMaRT/RTM)** | 🟡 **teoricamente applicabile** | Sostituisce l'intera porzione 3′ del pre-mRNA a valle di un sito di trans-splicing → **rimpiazzerebbe l'esone 9 difettoso**. Efficienze storicamente basse; nessuna applicazione CNS matura. **È RNA-terapeutica, non ASO.** Questa via non l'avevo considerata. |
  | **Base editing (CBE) su filamento antisenso** | ✅ **meccanicisticamente valido** | La variante è `A>G` in −2; sull'antisenso è `T→C`. Un CBE che faccia **C→T sull'antisenso** ripristina la `A` e **ricostruisce l'AG**. Da verificare: PAM disponibile, **bystander editing** di C vicine, delivery CNS (split-AAV). |
  | **Prime editing** | ✅ **valido, più flessibile** | Qualunque sostituzione puntiforme, senza bystander. Cargo grande; delivery CNS immaturo. |
- 🎯 **Conclusione**: la tesi **regge**. **`TX-001` (ASO splice-modulante) va retrocessa**: poggia su un meccanismo che non può funzionare. Sostituita da **`TX-001-bis` — correzione dell'allele di sito accettore via base/prime editing (o, come outsider, trans-splicing)**, tag `IPOTESI`, lontana dalla clinica ma **meccanicisticamente possibile**, mentre l'ASO non lo è.
- ✅ **E ora ha un argomento che prima non aveva**: per [[discovery_ledger_current#🥇 DL-MECH-046 — **L'aploinsufficienza di WWOX non è deleteria.** Il bersaglio non è il 100%: è molto meno.|DL-MECH-046]], **non serve correggere tutte le cellule** — l'aploinsufficienza è tollerata. L'efficienza modesta del base editing, che sarebbe fatale per una malattia che richiede il 100%, qui potrebbe **bastare**.
- ⚠️ **Onestà sulla forza della verifica**: il verdetto poggia sul **ragionamento meccanicistico** e su biologia standard degli SSO. **Non ho eseguito una ricerca sistematica di controesempi**: due query PubMed sono state mal interpretate dal parser e hanno restituito zero risultati. **Prima di retrocedere formalmente TX-001 nel Layer 9, questa conclusione va sottoposta a un revisore esterno o a una ricerca bibliografica dedicata.** Fino ad allora resta `stress-tested`, non `refuted`.
- **Nessuna sequenza è stata progettata. Non è design clinico né parere medico.**

---

### DL-MECH-047 — P252A mostra degradazione lisosomiale HSC70-associata; **CMA e trasferimento a Q230P non dimostrati**

- **Fonte:** Zhang X et al., *Adv Sci* 2025 — PMID 41124647 / PMC12767083 / DOI 10.1002/advs.202507602. Full text letto (Intro, Risultati 2.1-2.5, Discussione; non letti Metodi e supplementari).
- **Tag:** `DATO` (turnover/sonde/HSC70 su P252A) → `IPOTESI PONTE` (route specifica e Q230P)
- **Provenienza:** paper a registro come **Tier C, "screened — corpus placeholder", triage only**, etichettato P6/DDR. Recuperato perché il gate su Q230P richiedeva la *via* di degradazione, non altre keyword. Vedi *capability-scout entry 2026-07-12 (private operational log)*.

**Il dato.** Paziente con varianti germinali omozigoti **P252A** e **P282A**, entrambe nel dominio SDR (cancro tiroideo misto; **nessuna malattia neurologica**).

| Sonda | Esito su WWOX-P252A |
|---|---|
| mRNA | **normale** (non ridotto) |
| Proteina + CHX chase | fortemente ridotta, **turnover accelerato** |
| **MG-132** (proteasoma) | ❌ **nessun accumulo** |
| **Clorochina / NH₄Cl** (lisosoma) | ✅ **proteina ripristinata** |
| **3-MA** (macroautofagia) | ❌ nessun effetto |
| **Co-IP HSC70** | ✅ lega **solo il mutante** (non WT, non P282A) |
| **Co-loc. LAMP1** | ✅ presente |
| Poliubiquitinazione | ↑, prevalentemente **K63** (K63 potenzia il riconoscimento HSC70, cfr. HIF1α via STUB1) |
| Motivo KFERQ-like | **LRSVQ, aa 187-191** |

**Meccanismo (modello degli autori, non interamente dimostrato):** la missenso riduce rigidità, espone un motivo KFERQ-like e porta a HSC70/CMA. I dati dimostrano turnover lisosomiale HSC70-associato per P252A; senza dipendenza da LAMP2A o epistasi del motivo non distinguono definitivamente CMA da altre vie HSC70/endolisosomiali.
Contrasto esplicito con **NPC1-I1061T**, che misfolda nell'**ER** ed è degradato da **proteasoma + ER-autofagia**: **WWOX non segue quella via.**

**Perché riguarda il genotipo di riferimento (IPOTESI PONTE).** Q230P e P252A condividono dominio e un endpoint di bassa proteina, ma differiscono per variante, sistema e misure. La route P252A rende razionale testare HSC70/lisosoma su Q230P; non assegna probabilità alta, CMA, degron o trigger.

**Conseguenza operativa.** Affiancare sonde lisosomiali e proteasomiali, sintesi nascent, solubilità ed emivita. HSC70/LAMP1 sono readout associativi; la route richiede controlli di vitalità, LAMP2A e mutanti dei candidati degron.

**Corollario scomodo (DATO).** **P282A**: stessa domain SDR, **proteina stabile, nessun HSC70** — e **funzione completamente persa**. → **Stabilità e funzione sono separabili nel SDR di WWOX.** "Stabile ma inerte" è un **fenotipo dimostrato**, non più un timore. Il readout funzionale è obbligatorio.

**Reperto secondario.** Nuovo partner di WWOX: **POLE4** (subunità di DNA pol ε, nucleotide excision repair); i mutanti perdono il legame. Estende l'asse DDR.

**Limiti.** Linee di cancro tiroideo + HEK293T **in sovraespressione**; non neuroni, non cellule di paziente; la CMA è tessuto-specifica. **Q230P non testato.** I portatori omozigoti P252A/P282A **non hanno fenotipo neurologico** → ipomorfi: **il meccanismo si trasferisce, la severità no.**

---

### DL-MECH-048 — **SUPERSEDED:** possibile convergenza ACK1/ITCH/HSC70, non cascata assegnata a Q230P

- **Tag:** `DATO` (i singoli anelli) → `IPOTESI` (la cascata applicata a Q230P)
- **Fonti — tre paper, tutti nel corpus, tutti mai letti fino al 2026-07-12:**
  - **Zhang 2025** — PMID 41124647, `Tier C`, *cancro tiroideo* ([[discovery_ledger_current#DL-MECH-047 — P252A mostra degradazione lisosomiale HSC70-associata; **CMA e trasferimento a Q230P non dimostrati**|DL-MECH-047]])
  - **Abu-Odeh 2014** — PMID 24550385, *J Biol Chem*, `corpus placeholder`
  - **Mahajan 2005** — PMID 16288044, *Cancer Res*, `corpus placeholder`

**Cosa avevamo concluso (e perché era ragionevole).** Il ledger registrava già ACK1 e ITCH, e li archiviava così: *"sono meccanismi di degradazione **regolata** (fosforilazione → ubiquitinazione), **non** di controllo qualità ERAD/chaperoni, che è un'altra cosa. → Non assumere che inibire ACK1/ITCH salvi Q230P."*
Il ragionamento era corretto. **La premessa era falsa**: assumeva che quella via finisse al **proteasoma**.

**Cosa dicono davvero i tre paper messi insieme.**

| Anello | Fonte | Dato |
|---|---|---|
| **ACK1** (TNK2) fosforila WWOX su **Tyr287** → poliubiquitinazione → degradazione. La fosforilazione **è necessaria**: la variante non fosforilabile **non** viene degradata. Y33 **attiva**, Y287 **degrada**. | Mahajan 2005 | `DATO` |
| **ITCH** è l'E3 ligasi che appone **poliUb K63** su WWOX → localizzazione nucleare | Abu-Odeh 2014 *JBC* (PMID 24550385) | `DATO` |
| Il residuo è **Lys274**; il danno al DNA la innesca → accumulo nucleare → **ATM → riparo DNA** | Abu-Odeh 2014 *PNAS* (PMID 25331887, = [[paper_registry_current#PAPER 030]]) | `DATO` |
| Nel mutante SDR P252A, la **poliUb K63 predominante**, il legame selettivo a HSC70 e la localizzazione lisosomiale sono osservazioni sperimentali; il paper interpreta l'insieme come CMA. Che K63 **potenzi causalmente** il riconoscimento HSC70 non è dimostrato nel modello WWOX (precedente meccanicistico distinto: HIF1α via STUB1). | Zhang 2025 | `DATO` per le osservazioni; `INFERENZA` per il nesso K63→HSC70 |

→ **La K63-ubiquitinazione non è un segnale proteasomiale specifico e può partecipare a vie lisosomiali/autofagiche.** Nel modello P252A, K63, legame HSC70 e localizzazione lisosomiale convergono su una lettura CMA; non dimostrano però che K63 sia sufficiente né che la stessa catena causale valga per Q230P. La barriera rigida tra "degradazione regolata" e "controllo qualità" era quindi ingiustificata, ma riaprire la cascata significa **testarla**, non considerarla dimostrata.

**⚠️ Ma la conclusione NON è "inibiamo ITCH". È più fine, e migliore.**
Zhang mostra che **HSC70 lega SOLO il mutante**, non il WT — eppure **anche il WT è K63-ubiquitinato** da ITCH. Quindi:
- il **tag K63 non basta**; il suo ruolo di **amplificatore del riconoscimento** resta un'inferenza da verificare;
- il fold/degron era stato assunto come discriminante; per Q230P non sono dimostrati né degradazione, né degron, né route.

**Verdetto attivo:** conformazione e cascata sono entrambi rami da testare. `LRSVQ` non è canonico senza fosforilazione; `ERLIQ` è il candidato canonico e nessuno dei due è stato validato in Q230P.

**🔴 E colpire ITCH sarebbe attivamente dannoso.** La K63-Ub di ITCH su **Lys274** è **funzione fisiologica**: guida l'**accumulo nucleare** di WWOX e l'**interazione con ATM** → riparo del DNA (Abu-Odeh 2014 **PNAS**, PMID 25331887 = [[paper_registry_current#PAPER 030]]; NON il paper JBC). Inibire ITCH **spoglierebbe WWOX della sua funzione di riparo del DNA** — in una bambina. In più ITCH è promiscua (i topi *Itch−/−* sviluppano **autoimmunità**). **BLOCCO 1: rosso come bersaglio terapeutico.**

**✅ Ma ACK1 e ITCH restano SONDE SPERIMENTALI eccellenti — ed è questo il valore operativo.**
Sui fibroblasti donor-derived, accanto al braccio lisosomiale ([[discovery_ledger_current#DL-MECH-047 — P252A mostra degradazione lisosomiale HSC70-associata; **CMA e trasferimento a Q230P non dimostrati**|DL-MECH-047]]):
- **inibitore di ACK1** (es. AIM-100) → la proteina Q230P riemerge? *(nota: Hsp90β lega ACK1, e la geldanamicina ne inibisce l'attività — Mahajan 2005)*
- **knockdown di ITCH** → la degradazione rallenta?
- **mutante Y287F di Q230P** → il controllo più pulito: se togliere il sito di fosforilazione salva la proteina, la cascata è confermata.
Una risposta suggerirebbe coinvolgimento della cascata; un negativo non dimostrerebbe degradazione puramente conformazionale. Sono necessari sintesi/turnover e controlli ortogonali.

**Coincidenza strutturale da non sopravvalutare, ma da annotare.** La triade catalitica del SDR è **Ser281 / Tyr293 / Lys297**. Il sito di fosforilazione di ACK1 è **Tyr287** — **dentro** quella regione. E **Q230 dista 8.2 Å dalla triade** ([[claim_registry_current#CLAIM 019]]). Un core destabilizzato attorno alla triade **potrebbe** aumentare l'accessibilità di Y287 ad ACK1 → più fosforilazione → più degradazione. **`IPOTESI`, non dato**: è una catena inferenziale lunga, ogni anello è un'assunzione separata, e nessuno è stato testato su Q230P.

**Limiti.** Tutti e tre i paper sono su **WWOX wild-type o mutanti oncologici in linee tumorali**, in sovraespressione. **Q230P non è mai stato testato in nessuno di essi.** La cascata applicata a Q230P è **IPOTESI**. La CMA è tessuto-specifica; nessun dato in neuroni.

---

### DL-MECH-049 — In WWOX **stabilità e funzione sono in TENSIONE STRUTTURALE**: la stabilità si compra con l'occlusione. Vincolo di progetto per qualunque stabilizzatore di Q230P.

- **Fonte:** Schuchardt, Mikles, Bhat, McDonald, **Sudol**, **Farooq** — *J Mol Recognit* 2015 — PMID 25703206 / PMC4376589 / DOI 10.1002/jmr.2419. **Full text letto integralmente** (Intro, Metodi, Risultati/Discussione, Conclusioni).
- **Tag:** `DATO` (ITC/CD) + `INFERENZA` (meccanismo del coperchio, da omologia+MD)
- **Provenienza:** `corpus placeholder` mai letto, recuperato dall'audit `--mechanism` del 2026-07-12.

**⚠️ Prima il limite di scopo, perché ribalta l'aspettativa.** Il paper studia **esclusivamente i residui 1-91** (moduli WW1-WW2). **Q230 è nel dominio SDR (~137-350), che non è nemmeno nei costrutti.** Era stato indicato come possibile *"razionale per lo stabilizzatore conformazionale del SDR"*: **quella lettura non regge** ([[dismissal_ledger_current#DIS-005 — «PMID 25703206 (allostery) gives the rationale for the SDR stabilizer» → ❌ **DOES NOT HOLD (but yields something else)**|DIS-005]]).

**Ma il reperto è più utile del razionale cercato.**

**`DATO` (ITC/CD, n≥3):**
- **WW1 lega tutti i ligandi PPXY; WW2 nessuno.** WW2 è un **dominio orfano**.
- WW1 **nel modulo tandem** lega **2-3× più forte** che da solo, con **guadagno entropico**.
- **WW1 da solo è parzialmente destrutturato e si ripiega legando il ligando**; nel modulo tandem il legame avviene su un **WW1 già completamente ripiegato**.

→ **Esistenza-prova:** un dominio instabile di WWOX viene **riscattato in stato ripiegato e funzionale** da un partner che vi si aggancia. **Stabilizzare un fold floscio di WWOX non è ipotetico: è il design nativo della proteina.** Cade l'obiezione *"non puoi stabilizzare WWOX legandoci qualcosa"*. (Conferma e meccanizza [[discovery_ledger_current#DL-MECH-017 — WW2 come chaperone intramolecolare che stabilizza WW1 (rinforza il razionale stabilizzatori/proteostasi)|DL-MECH-017]].)

**🔴 `INFERENZA` (omologia FBP21/2JXW + MD 4 μs, 4 force field) — il vincolo che conta:**
Il WW2 si aggancia con la faccia **convessa** sulla faccia **concava** di WW1 (contatti: W44 di WW1 stretto tra Q65/V73 di WW2; T67 di WW2 tra W31/Y33 di WW1; H-bond W44 Nε1–Q65 Oε1). E — **il punto**:

> *"la giustapposizione di WW2 sulla faccia concava di WW1 **blocca parzialmente il solco di legame**… WW2 agisce come un **coperchio** che deve essere spostato"*
> *"in assenza di ligando, l'equilibrio aperto↔chiuso è **nettamente a favore del chiuso**"*

**L'interazione che STABILIZZA WW1 è la stessa che ne BLOCCA la funzione.** WWOX risolve il conflitto con uno **switch allosterico**: il ligando paga il costo entropico e solleva il coperchio (*binding-coupled dissociation*).

**→ VINCOLO DI PROGETTO (`IPOTESI` operativa, alta priorità):**
> **Una molecola che irrigidisce un fold di WWOX per impedirne la degradazione rischia, con lo stesso gesto, di CHIUDERLO in uno stato non funzionale.**

Questo dà una **ragione strutturale, specifica di WWOX**, allo scenario *"stabile ma inerte"* che P282A ha dimostrato empiricamente ([[discovery_ledger_current#DL-MECH-047 — P252A mostra degradazione lisosomiale HSC70-associata; **CMA e trasferimento a Q230P non dimostrati**|DL-MECH-047]]). Non era solo una possibilità: **in WWOX la stabilità si compra con l'occlusione, e l'occlusione è anti-funzione.** → default `D-04` in [[dismissal_ledger_current]].

**Conseguenze operative:**
1. Lo stabilizzatore per Q230P deve essere **allosterico e reversibile**, **non una morsa**: deve alzare l'energia libera di folding **senza occludere la superficie funzionale**.
2. **Il readout di abbondanza è insufficiente per costruzione.** Serve il readout **funzionale** (attività SDR, binding ai partner, soppressione di HIF1α, localizzazione) — e ora sappiamo *perché*, non solo *che*.
3. **Failure mode pre-registrato**: se un candidato fa riemergere proteina Q230P **inerte**, non è un fallimento inatteso — è **la predizione**.

**Reperto minore (basso valore per il genotipo di riferimento, annotato per completezza).** L'interfaccia W44↔Q65/V73 è una PPI piccola e definita, in principio druggabile. **Ma la funzione WW1/PPxY non determina la gravità** (P47T abolisce il binding PPxY e dà fenotipo **lieve**; il SDR sì) → **non è il nostro bersaglio.**

**Limiti (dichiarati dagli autori e da me).** Il modello è **omologia + MD**, non struttura sperimentale; gli autori ammettono che il modello *"non supporta né contraddice"* l'associazione dei domini. La conformazione **non-legata di partenza è stata assunta identica alla legata**, il che orienta la "burst phase". Riprodotto su AMBER/GROMOS/CHARMM/OPLS. **Nessun dato sul SDR. Nessun dato su Q230P.**

**🎯 Il buco che questo paper rende visibile:** non esiste, nel nostro corpus, **biofisica strutturale del dominio SDR di WWOX**. L'in-silico interno gira su **AlphaFold** ([[claim_registry_current#CLAIM 019]]). **Per progettare uno stabilizzatore allosterico del SDR serve una struttura del SDR** — sperimentale o almeno una caratterizzazione dinamica. **È il prossimo bersaglio di ricerca.**

---

### DL-MECH-050 — Il motivo KFERQ-like di WWOX è **CRIPTICO**, e **Q230 ci impacchetta direttamente contro (3,9 Å)**. La vicinanza prioritizza il test dinamico, ma non ne predice l'esito.

- **Tag:** `INFERENZA` (in-silico, modello statico WT) — **NON `DATO` strutturale**
- **Fonte:** analisi propria su **AlphaFold AF-Q9NZC7** (pLDDT ~98 nella regione), Shrake-Rupley + geometria. Riproducibile: `scripts/legend/kferq_geometry.py`.
- **Innesco:** regola di ri-audit ([[dismissal_ledger_current#DIS-006 — «Whether a folded *and* active state for Q230P is reachable is **not resolvable in silico**» → 🔄 **REOPENED — by the re-audit rule**|DIS-006]]) applicata dopo [[discovery_ledger_current#DL-MECH-047 — P252A mostra degradazione lisosomiale HSC70-associata; **CMA e trasferimento a Q230P non dimostrati**|DL-MECH-047]].

**Il reperto strutturale.** Il motivo KFERQ-like `LRSVQ` (aa 187-191) è **criptico**: le sue **due ancore idrofobiche sono completamente sepolte** — **L187 relSASA 0.000, V190 relSASA 0.000** — mentre R188/Q191 guardano il solvente. È la firma esatta di un motivo **accessibile solo quando il fold si allenta**. Coerente con Zhang: HSC70 lega **solo** il mutante, non il WT.

**Il numero che conta:**

| Variante | relSASA | **d → ancore KFERQ** |
|---|---|---|
| **Q230P** *(il genotipo di riferimento)* | 0.000 | **3,9 Å** — contatto di van der Waals |
| **L239R** | 0.000 | **3,5 Å** |
| P252A *(la variante su cui Zhang DIMOSTRA il meccanismo)* | 0.452 | **20,6 Å** |
| P282A | 0.040 | 15,4 Å |
| G372R | 0.165 | 22,5 Å |
| P47T | 0.292 | 56,0 Å |

**→ `IPOTESI` testabile:** Q230P può perturbare localmente il packing di `LRSVQ`. P252A — variante con legame HSC70 e turnover lisosomiale — dista **20,6 Å**, mentre Q230 contatta le ancore nel WT. La geometria prioritizza il test ma non predice esposizione, degron o route.
Coerenza clinica (**da non sovra-interpretare**): i portatori omozigoti P252A/P282A **non hanno malattia neurologica**; Q230P dà **WOREE severa**.

**🎯 Predizione generata, su una variante non ancora letta.** **L239** (relSASA 0.000, **3,5 Å** dalle ancore) è nel medesimo core. **`L239R`** — Leu sepolta → Arg carica — dovrebbe essere **devastante** per quel packing. → **Predizione falsificabile: anche L239R è un forte substrato di CMA.** Il paper è a registro non letto (*capability-scout entry 2026-07-12 (private operational log)*, PMID **41153369**). **Leggerlo è ora un test della nostra ipotesi, non solo lettura arretrata.**

### ⚠️ Due buchi nel paper di Zhang, che vanno detti

1. **Zhang NON dimostra che sia quel motivo a legare HSC70.** Dimostra (co-IP) che il **mutante** lega HSC70 e il WT no — questo è `DATO`. Ma **non hanno mai mutato il motivo** per provare che sia lui il responsabile. L'assegnazione a `LRSVQ` è **loro INFERENZA, non loro DATO**.
2. **`LRSVQ` non è un KFERQ canonico**: manca il residuo acido (regola di Dice: Q/N + tetrapeptide con 1-2 basici, 1-2 idrofobici, **1 acido**). Zhang lo chiama infatti *"KFERQ-**like**"*. Scansionando WWOX, **l'unico motivo canonico è altrove**: `ERLIQ` @402-406 (relSASA medio 0.276, più esposto).
   *(`IPOTESI` mia, non verificata: **S189 è dentro il motivo**. Una **fosforilazione di S189** aggiungerebbe la carica negativa mancante e renderebbe `LRSVQ` **canonico** — meccanismo noto di generazione di motivi CMA. **Non ho verificato che S189 sia un fosfosito reale**: da controllare in PhosphoSitePlus.)*

**→ Esperimento necessario ma non sufficiente:** mutare `LRSVQ` **e** `ERLIQ` separatamente nel contesto Q230P. L'epistasi assegna il degron, non da sola il trigger elicoidale o CMA; per CMA serve dipendenza da LAMP2A.

### 🔴 Limiti — questo NON è un dato strutturale

- **Modello STATICO del WILD-TYPE.** AlphaFold predice il fold **wild-type**: **non dice nulla su cosa faccia la mutazione.** Che Q230P *esponga* il motivo è **INFERENZA**, non dimostrazione.
- pLDDT ~98 e il fold SDR è una delle famiglie meglio caratterizzate → il modello WT è probabilmente affidabile sulla **geometria**. Ma **alto pLDDT ≠ affidabilità sulla dinamica**.
- **La domanda vera è dinamica, non termodinamica** — e ora è ben posta: *Q230P aumenta la SASA/RMSF dei residui 187-191?* → **MD, WT vs Q230P.** Vedi [[dismissal_ledger_current#DIS-006 — «Whether a folded *and* active state for Q230P is reachable is **not resolvable in silico**» → 🔄 **REOPENED — by the re-audit rule**|DIS-006]].
- Nessun dato sperimentale: **non esiste alcuna struttura del dominio SDR di WWOX** (vedi sotto).

### 🕳️ Il vuoto strutturale, ora misurato
**Interrogato il PDB: l'unica struttura sperimentale di WWOX esistente è `1WMV` — il dominio WW2, 54 residui, NMR, 2005.**
**Nessuna struttura di WW1. Nessuna del modulo tandem** (ecco perché Farooq/Sudol hanno dovuto modellare per omologia da FBP21). **Nessuna, in oltre vent'anni, del dominio SDR** — quello che contiene Q230P, che **determina la gravità**, e che è **il nostro bersaglio terapeutico**.
→ Spiega **perché nessuno ha mai progettato un chaperone farmacologico per WWOX**: non si fa design strutturale su un dominio che nessuno ha risolto.
→ **Risolvere il SDR di WWOX** (cristallografia/crio-EM) è una richiesta concreta, finanziabile e ad alta leva — e un aggancio naturale per un gruppo di biologia strutturale.

---

### DL-MECH-051 — ⚠️ **SUPERSEDED:** il modello a due vie e C299R catalitico non superano l'audit strutturale

- **Tag:** `INFERENZA` (in-silico su AlphaFold, serie allelica n=11) — **correttivo di [[discovery_ledger_current#DL-MECH-050 — Il motivo KFERQ-like di WWOX è **CRIPTICO**, e **Q230 ci impacchetta direttamente contro (3,9 Å)**. La vicinanza prioritizza il test dinamico, ma non ne predice l'esito.|DL-MECH-050]]**
- **Innesco:** test di falsificazione della mia stessa ipotesi, eseguito su **tutte** le missenso WWOX a fenotipo noto.

### La falsificazione, per prima
[[discovery_ledger_current#DL-MECH-050 — Il motivo KFERQ-like di WWOX è **CRIPTICO**, e **Q230 ci impacchetta direttamente contro (3,9 Å)**. La vicinanza prioritizza il test dinamico, ma non ne predice l'esito.|DL-MECH-050]] suggeriva: *"i severi sono i sepolti vicini al KFERQ."* **Falso.**
**`C299R`: relSASA 0.004 (sepolto), ma a 13,8 Å dal KFERQ — e severo.** → **La prossimità al KFERQ NON è necessaria per la severità.**
La precedente distanza C299R–K297 di **3,4 Å** misurava atomi di backbone fra residui vicini, non i gruppi funzionali: SG(C299)–NZ(K297) = **10,706 Å**. C299 contatta H233 a 3,435 Å e non è un controllo off-lid indipendente. La classificazione «lesione catalitica» è ritirata.

### Il modello corretto: **due vie indipendenti verso la severità**

| Variante | relSASA | d→KFERQ | d→triade | Fenotipo | **Via** |
|---|---|---|---|---|---|
| **Q230P** *(il genotipo di riferimento)* | 0.000 | **3,9 Å** | 6,8 Å | SEVERO (WOREE) | ? sintesi/solubilità/degradazione |
| **L239R** | 0.000 | **3,5 Å** | 13,1 Å | SEVERO (West) | 🔴 **degradazione** *(predetta)* |
| **C299R** | 0.004 | 13,8 Å | backbone 3,4 Å; sidechain 10,706 Å | SEVERO | ? non assegnata |
| M352I | 0.237 | 23,2 Å | 11,9 Å | SEVERO | ? superficiale |
| R310P | 0.382 | 16,7 Å | 16,8 Å | SEVERO | ? superficiale |
| T12M | 0.593 | 51,8 Å | 39,4 Å | SEVERO | WW1 — altra via |
| P47T | 0.292 | 56,0 Å | 48,2 Å | **LIEVE** | superficie WW1 |
| G372R | 0.165 | 22,5 Å | 14,9 Å | **LIEVE** | superficie SDR |
| P252A | 0.452 | 20,6 Å | 23,1 Å | **nessuna neuro** | superficie |

**→ IPOTESI ristretta, e più difendibile:**
> **La prossimità al KFERQ non predice *quanto* una variante è grave. Predice *COME* viene distrutta.**
> Fra le varianti il cui meccanismo è la **degradazione** (trascritto normale, proteina assente), quelle **sepolte e in contatto col motivo criptico** dovrebbero degradare in modo più efficiente.

**Verdetto attivo:** non regge come modello di route. Johannsen non assegna degradazione e la prossimità statica al motivo non predice esposizione dinamica.

### 🎯 Predizione affilata, e falsificabile
> **Predizione ritirata:** C299R non è un killer control pulito; Q230P e L239R non hanno route assegnata dal modello.

Il dato verificato è Q230P → proteina non rilevata; C299R non conferma né refuta da solo una route. Nessuna conseguenza terapeutica diretta deriva da questo confronto.

### 🧩 Rompicapo che devo segnalare, non spiegare
**`P282A` sta a 1,3 Å dalla triade catalitica**, **abolisce completamente** la funzione oncosoppressiva (Zhang, in vitro e in vivo), la **proteina è stabile** — e **il portatore omozigote non ha alcuna malattia neurologica**.
→ Se confermato, suggerirebbe che **la funzione neuronale di WWOX non è la sua catalisi SDR**. Sarebbe rilevante per il genotipo di riferimento (il bersaglio del rescue non sarebbe l'attività enzimatica ma la **presenza/interazioni** della proteina). **Ma è n=1**, e i saggi di Zhang sono su linee tumorali, non neuroni. **Segnalato come rompicapo aperto, non come inferenza.**

### Limiti
- Serie **piccola (n=11)** e fenotipi da fonti eterogenee (case report, coorti, ClinVar).
- **Sepoltura e prossimità-KFERQ sono confuse** per Q230/L239: stanno nella **stessa tasca**. Non posso separare *"lesione generica del core"* da *"esposizione specifica del motivo CMA"* con la sola geometria.
  **→ L'esperimento che li separa resta lo stesso: mutare il motivo (L187A/V190A) nel contesto Q230P.** Se la degradazione persiste, non è il KFERQ.
- Tutto su **modello statico wild-type** (AlphaFold). Nessuna dinamica, nessun dato sperimentale.

---

### DL-MECH-052 — **WEAKENED:** ipotesi di packing elica/degron, non catena meccanicistica Q230P

- **Tag:** `IPOTESI` unificante (post-hoc su n=4) — **NON `DATO`.** Il valore sta nelle predizioni, non nella spiegazione.
- **Metodo:** AlphaFold AF-Q9NZC7 + Shrake-Rupley + mappatura legami H i,i+4. Riproducibile: `scripts/legend/kferq_geometry.py`.

### Come ci sono arrivato (e cosa ho falsificato per strada)
[[discovery_ledger_current#DL-MECH-050 — Il motivo KFERQ-like di WWOX è **CRIPTICO**, e **Q230 ci impacchetta direttamente contro (3,9 Å)**. La vicinanza prioritizza il test dinamico, ma non ne predice l'esito.|DL-MECH-050]] proponeva: *"Q230 tocca il motivo a 3,9 Å → lo scopre."* **Testato: la versione STERICA è falsa.** Rimuovendo la catena laterale di Q230, le ancore si espongono solo di **Δ +0.034** (L187) e **+0.000** (V190). **Q230 è solo il 5° occlusore.** Davanti a lui: D223, Y238, L409, L234.
**Ma gli occlusori hanno la periodicità di un'elica** (223, 225, 230, 234, 238, 239, 242).

### Il reperto strutturale
- **Segmento strutturato 227-249**, con DSSP α 227-229, π 230-234 e α 235-249 nel modello AlphaFold; non è un'α-elica continua sperimentalmente risolta.
- **Quell'elica È il coperchio del motivo KFERQ criptico.** Rimuovendo le catene laterali dell'intera elica: **L187 0.000 → 0.128** e **V190 0.000 → 0.060** (Δ totale **+0.188**). Q230 da solo ne vale il **18%**.
- **Q230P mette una prolina a metà elica** (posizione 5 dopo l'N-cap: oltre il primo giro → mid-helix). **Pro non dona il legame H di backbone → rompi-elica canonico.**

### 🎯 L'unificazione — e il controllo negativo è nel paper di Zhang stesso

| Variante | Rapporto con l'elica 226-251 | Dato sperimentale |
|---|---|---|
| **Q230P** *(il genotipo di riferimento)* | 🟢 **sulla elica** — Pro a metà | **proteina ASSENTE** (Johannsen, `DATO`) |
| **L239R** | 🟢 **sulla elica** — Leu sepolta → Arg | severo (West, omoz.) — *proteina non misurata* |
| **P252A** | fuori dalla parte elicoidale regolare; possibile ruolo di cap non dimostrato | lega HSC70, turnover lisosomiale (Zhang, `DATO`); CMA non discriminata |
| **P282A** | ⚪ **FUORI** (4,1 Å) | **NON lega HSC70, proteina STABILE** (Zhang, `DATO`) |

**Interpretazione storica ora indebolita:** P252A/P282A mostrano esiti biologici diversi nel sistema Zhang, ma non validano la rottura del segmento 227-249. P252 è fuori dalla parte elicoidale regolare nel DSSP e può avere un ruolo di cap solo ipotetico.

**Catena da testare, non completa:**
`Q230P` → perturbazione del segmento 227-249? → esposizione di quale degron? → HSC70/endolisosoma? → proteina non rilevata. Ogni arco intermedio è aperto; Johannsen chiude soltanto l'endpoint.

### 🔴 Rischio di over-fitting — da tenere davanti, non in fondo
**Il modello è costruito DOPO aver visto i dati.** È **post-hoc**, non predittivo. n=4. I confini dell'elica li ho calcolati io su un **modello AlphaFold**, non su una struttura sperimentale (che **non esiste**). La distinzione P252 (1,3 Å) vs P282 (4,1 Å) è **sottile**. Il proxy "rimuovo le catene laterali" **sottostima** l'effetto di una vera rottura d'elica (il backbone non si muove) — il che va a favore, ma resta un proxy.
**Una storia che spiega tutto e non predice nulla è un racconto, non un modello.** Quindi:

### 🧪 Le predizioni falsificabili (è qui che il modello si gioca)
1. **C299R non è un controllo off-lid pulito** e non può decidere da solo il modello.
2. **`L239R` → proteina assente** (stessa elica).
3. Testare separatamente `LRSVQ` e `ERLIQ` nel contesto Q230P, con rescue/non-rescue interpretato solo sull'asse del degron.
4. Dimostrare prima sintesi e turnover Q230P; poi distinguere CMA (LAMP2A-dipendente) da vie alternative.

### 💡 Conseguenza terapeutica (nuova, `IPOTESI`)
Un molecular glue che riseppellisca un degron è una possibilità **condizionata** alla validazione di route, degron e stato foldato funzionale. Non è ancora un bersaglio design-ready.
⚠️ **Vincolo `D-04` da verificare prima di ogni design:** l'elica-coperchio dista **6,8 Å dalla triade catalitica** (S281/Y293/K297). Un legante lì **rischia di occludere il sito attivo** → *stabile ma inerte*. **Da controllare, non da assumere.**

### Limiti
Modello **statico**, **wild-type**, **AlphaFold** (nessuna struttura sperimentale del SDR esiste). Nessuna dinamica: **la MD (WT vs Q230P, SASA/RMSF a 187-191) resta il test in-silico corretto**, e non è eseguibile in sessione (serve μs su GPU; una run corta darebbe un **falso negativo sicuro di sé** — vedi `D-05`).

---

### DL-MECH-053 — Una chiamata exon-level corretta puo' nascondere un'architettura WWOX allelica diversa

- **Status:** `promoted-to-CC` · **Tag:** DATO (PMID 37974179) + INFERENZA multi-paper (con PMID 35573960)
- **Fonte:** Dong et al. 2023, PMID 37974179 / PMCID PMC10652538; main text, figure e due supplementari letti integralmente. Dossier: `staging/deepdive_PMID37974179_Dong2023.md`.
- **Statement causale/metodologico:** `risoluzione exon-level WES/qPCR —non determina necessariamente→ fase + breakpoint + architettura allelica WWOX`.
- **DATO:** WES/ExomeDepth e qPCR mostravano perdita biallelica dell'esone 6; WGS 30x + gap-PCR/Sanger hanno rivelato un allele di sito accettore `del ex6-8` e un allele missense con due delezioni discontinue (`intron 5` + `exon 6`). La diagnosi WWOX biallelica non era falsa, ma la rappresentazione era incompleta.
- **Convergenza:** PMID 35573960 (*CC-2026-07-15-004 (private commit queue)*) documenta il failure mode complementare: ES-CNV non informativa per una delezione esonica, risolta con RT-PCR/qPCR/array-CGH. Insieme, i due studi sostengono che “negativo” e “positivo exon-level” possono entrambi richiedere conferma ortogonale.
- **Mappa ABC:** A=`WWOX-LoF/alleli complessi` · B=`fase, breakpoint e prodotto molecolare non risolti dall'exome-CNV` · C=`WGS + gap-PCR/Sanger + RNA/proteina isoform-resolved`.
- **Catena di ragionamento:** DNA exon-level -> WGS/breakpoint -> fase parentale -> RNA/proteina -> scelta dell'assay o intervento allele-specifico. Il paper chiude i primi tre passaggi, non misura gli ultimi due.
- **Supporta:** segregazione familiare, tre breakpoint Sanger e gel originale supplementare.
- **Refuta/limita:** n=1; nessun RNA, proteina o funzione; le dimensioni delle due delezioni paterne sono scambiate in una frase narrativa; funzione residua della `del ex6-8` soltanto predetta.
- **Belief:** alto sul failure mode diagnostico del caso; medio sull'inferenza generalizzata, sostenuta da due case report indipendenti.
- **Esperimento/procedura proposta:** per una CNV/SV WWOX complessa, non fermarsi a WES/qPCR: risolvere fase/breakpoint e poi misurare giunzioni RNA, NMD/isoforme e proteina con epitopi N-/C-terminali. Readout atteso: distinzione fra alleli genomicamente sovrapposti ma funzionalmente diversi.
- **Applicabilità al modello di malattia:** nessuna informazione diretta sugli alleli worked-example; applicazione come guardrail di caratterizzazione pre-terapeutica. Non e' biomarcatore WWOX e non sale nel file biomarker.
- **Interconnessioni:** [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 033]] · [[paper_registry_current#CORPUS-STUB-096]] · *CC-2026-07-15-004 (private commit queue)* · [[discovery_ledger_current#🔴 DL-MECH-045 — L'esone 9 è **l'ultimo esone**: l'allele di sito accettore del genotipo di riferimento non è un "null silente", ma probabilmente produce una **proteina tronca instabile**|DL-MECH-045]].

**Next-search agenda:** `READ_NEXT` PMID 37781246. In parallelo, cercare soltanto quando serve al design sperimentale studi WWOX con WGS + RNA/proteina sulla stessa CNV; il guadagno atteso e' separare architettura DNA da conseguenza funzionale, non accumulare altri case report descrittivi.

**Riflessione di processo:** la tabella supplementare ha aggiunto contesto fenotipico, ma l'ago decisivo era nel confronto fra metodi e nella fase parentale. Per i paper di genetica strutturale, la coverage deve includere sempre breakpoint, schema allelico e dati originali di segregazione; la semplice etichetta “homozygous deletion” e' una compressione potenzialmente pericolosa.

---

### DL-MECH-054 — Espressione WWOX alta non identifica da sola uno stato funzionale benefico

- **Status:** `promoted-to-CC` · **Tag:** DATO contestuale + INFERENZA metodologica; non meccanismo Q230P
- **Fonte:** Kałuzińska-Kołat et al. 2023, PMID 37781246 / PMCID PMC10540236; main text, cinque figure principali, cinque figure supplementari e sette workbook supplementari letti integralmente. Dossier: `staging/deepdive_PMID37781246_Kosla2023.md`.
- **Statement:** `abbondanza/espressione WWOX —non determina necessariamente→ localizzazione + partner occupancy + output funzionale nel medesimo contesto`.
- **DATO:** WWOX-OE stabile produce firme trascrizionali differenti in quattro linee GBM; DBTRG-05MG e' un outlier rispetto a U87MG/T98G/U251MG. Piccoli sottogruppi TCGA selezionati su WWOX/POLE4/HSF2BP mostrano outcome di segno opposto fra i profili “UTU” e DBTRG.
- **NON DATO:** nessuna misura di proteina/localizzazione/PTM/interazione dimostra che WWOX sia davvero “inaccessibile” ai partner. POLE4/HSF2BP non sono partner diretti dimostrati; nessuna causalita' WWOX→prognosi.
- **Rischio di selezione/confondimento:** bootstrap di `n=3` biologici, soglia DEA rilassata durante il workflow, cutpoint diversi fra OS/DFS, gruppi `n=8–13`, nessuna validazione esterna o Cox multivariata; MGMT, sottotipo mesenchimale, NF1/MUC16/EGFR e TMZ-IC50 predetta differiscono fra gruppi.
- **Belief:** alto sul guardrail `abundance ≠ functional state`; basso sulla specifica spiegazione di partner sequestrati e sul valore prognostico della firma.
- **Mappa ABC:** A=`rescue/aumento WWOX` · B=`stato molecolare e contesto possono dissociare quantita' e funzione` · C=`dose WT + solubilita' + localizzazione + PTM + partner occupancy + output funzionale`.
- **il genotipo di riferimento:** valore soltanto come controllo di qualita' del rescue Q230P; nessun trasferimento di POLE4/HSF2BP, nessuna terapia e nessun biomarcatore.
- **Interconnessioni:** *CC-2026-07-22-002 (private commit queue)* · *capability-scout entry 2026-07-15 — `PROTEIN_STATE_IDENTITY_GATE`: un rescue è un vettore, non un Western (private operational log)*.

**Next-search agenda:** `READ_NEXT` PMID 37519886. Per questo asse, leggere Bonin/VOPP1 soltanto se serve a distinguere sequestro, degradazione e partner occupancy; il paper GBM non chiude nessuno dei tre.

**Riflessione di processo:** i supplementi hanno trasformato un titolo apparentemente forte in un segnale esplorativo: senza le tabelle non erano visibili i gruppi da 8–13 pazienti, i cutpoint endpoint-specifici e i confondenti. Per firme prognostiche data-derived, numerosita', soglie e covariate sono parte del risultato, non dettagli accessori.

---

### DL-MECH-055 — LINC01137/miR-186/WWOX e' un circuito predetto, non un asse causale dimostrato

- **Status:** `promoted-to-CC` · **Tag:** DATO di espressione + IPOTESI computazionale; nessun meccanismo Q230P
- **Fonte:** Kołat et al. 2023, PMID 37519886 / PMCID PMC10373930; main text, sette figure principali, dieci figure e tre tabelle supplementari letti integralmente. Dossier: `staging/deepdive_PMID37519886_Kolat2023.md`.
- **Statement:** `co-espressione WWOX/LINC01137/MIR186 + archi predetti —non dimostra→ feedback ceRNA/triplex causale`.
- **DATO:** WWOX-OE si associa a LINC01137, UPF1 e ZC3H12A più alte e MIR186 relativamente più bassa in tre linee BLCA; qPCR corrobora le associazioni di espressione.
- **NON DATO:** nessun reporter miRNA, AGO-RIP, binding LINC01137–miR-186, perturbazione/rescue, UPF1 ChIP o triplex assay. TargetScan, RNAhybrid, GTRD e ncFANs producono ipotesi, non chiudono gli archi.
- **Rischio strutturale:** le tre linee sono trattate come repliche biologiche; 10-fold CV su 18 profili, feature selection e validazione data-derived, cutpoint multipli e assenza di Cox multivariata. I segnali prognostici headline non replicano coerentemente fra GSE31684 e TCGA-BLCA.
- **Belief:** alto che il paper sostenga un'associazione contestuale WWOX-OE/RNA; basso sul circuito causale e sul valore prognostico/traslazionale.
- **Mappa ABC:** A=`aumento WWOX in linee BLCA` · B=`cambiamenti RNA contestuali` · C=`perturbazioni a coppie + rescue + assay fisici + repliche within-line`.
- **il genotipo di riferimento:** nessun trasferimento diretto. LINC01137/miR-186 non salgono a biomarker o target; UPF1 resta un ponte teorico verso NMD, ma qui non e' collegato a `c.1057-2A>G` o Q230P.
- **Interconnessioni:** [[paper_registry_current#CORPUS-STUB-095]] · *CC-2026-07-22-003 (private commit queue)*.

**Next-search agenda:** `READ_NEXT` PMID 37324196. Trattare lo studio sui polimorfismi prostatici come associazione genetica oncologica e verificare correzione multipla, covariate, numerosita' dei sottogruppi e assenza di funzione prima di qualsiasi interpretazione WWOX.

**Riflessione di processo:** una figura finale con frecce puo' comprimere archi di natura diversa — dato nuovo, interazione da letteratura, predizione e pura assunzione. La lettura deve ricostruire la provenienza di ogni arco e impedire che la grafica trasformi una rete candidata in causalita'.

---

### DL-MECH-056 — Un'associazione SNP nominale non e' ancora funzione WWOX né predizione clinica

- **Status:** `promoted-to-CC` · **Tag:** ASSOCIAZIONE OSSERVAZIONALE + guardrail di validazione
- **Fonte:** Lin et al. 2023, PMID 37324196 / PMCID PMC10266044; main text e quattro tabelle supplementari letti integralmente. Dossier: `staging/deepdive_PMID37324196_Lin2023.md`.
- **Statement:** `SNP WWOX associato a BCR in una coorte —non determina→ effetto funzionale WWOX o predictor clinico validato`.
- **DATO:** rs12918952 GA associa BCR binaria con AOR `2,053` (`1,088–3,872`; `p=0,026`) nella singola coorte chirurgica taiwanese; quattro altri SNP sono nulli per BCR.
- **LIMITI:** molte comparazioni senza multiplicity correction, nessun follow-up/time-to-event, QC genetico incompleto, modello clinico sovraccarico e nessuna validazione. L'associazione metastasi rs3764340 poggia su `3 vs 3` eventi.
- **NON DATO:** nessuna misura WWOX nel tumore o prova SNP→espressione/proteina/funzione in questa coorte; nessun incremento predittivo rispetto alle covariate cliniche.
- **Belief:** medio-basso sull'associazione rs12918952 specifica; alto sul principio che l'etichetta “predictor” richieda validazione e performance incrementale.
- **il genotipo di riferimento:** nessuna trasferibilita' diretta; SNP comuni oncologici non modellano le varianti bialleliche rare Q230P/`c.1057-2A>G`.
- **Interconnessioni:** [[paper_registry_current#CORPUS-STUB-057]] · *CC-2026-07-22-004 (private commit queue)*.

**Next-search agenda:** `READ_NEXT` PMID 36530994, dopo collegamento audit-only del corrigendum PMID 37095367 e skip dei record già letti 37248434, 36979157, 36828035 e 36572673.

**Riflessione di processo:** per studi di associazione, il verbo “predice” va riservato a modelli con timing, discriminazione/calibrazione e validazione. Un AOR nominale in un unico dataset descrive associazione, non utilita' clinica.

---

### DL-MECH-057 — Predizione terapeutica richiede interazione trattamento×genotipo

- **Status:** `promoted-to-CC` · **Tag:** ASSOCIAZIONE POST-HOC + meccanismo incompleto
- **Fonte:** Chen et al. 2022, PMID 36530994 / PMCID PMC9756969; main text, otto figure, cinque figure e dieci tabelle supplementari letti integralmente. Dossier: `staging/deepdive_PMID36530994_Chen2022.md`.
- **Statement:** `outcome migliore nei trattati GG —non dimostra→ efficacia differenziale di ADI-PEG20 per genotipo` senza confronto controllo e test di interazione.
- **DATO:** nella coorte ADI-PEG20 monoterapia, `GG n=9` associa OS con HR aggiustato `0,420` (`0,180–0,980`; `p=0,045`). Il segnale e' nullo nella coorte ADI-PEG20+mFOLFOX (`GG n=5`) e nel pooled (`GG n=14`).
- **DATO BIOLOGICO:** GG associa WWOX/ASS1 T/N inferiori nei tessuti resecati; shWWOX sotto CoCl2 aumenta HIF1A, riduce ASS1 e attenua Alamar Blue sotto ADI-PEG20.
- **NON DATO:** nessuna causalita' SNP→WWOX, nessuna epistasi HIF1A o rescue ASS1, nessuna prova di morte/autofagia, nessun trattamento combinato TACE/TKI/immunoterapia testato.
- **Belief:** basso sul predictor clinico rs13338697; medio sul ruolo contestuale di WWOX nella risposta HIF1A/ASS1 sotto CoCl2; alto sul gate metodologico.
- **il genotipo di riferimento:** nessuna trasferibilita' terapeutica; la strategia oncologica di ridurre WWOX/ASS1 e' opposta al rescue WWOX-LoF.
- **Interconnessioni:** [[paper_registry_current#CORPUS-STUB-049]] · *CC-2026-07-22-005 (private commit queue)*.

**Next-search agenda:** `READ_NEXT` PMID 35883580, dopo skip dei record già letti 36498839, 36364214 e 35984507. Trattare la review pY33/pS14 come mappa di fonti, non come nuova prova.

**Riflessione di processo:** una coorte trattata puo' mostrare prognosi diversa fra genotipi senza dimostrare che il farmaco causi la differenza. Il requisito discriminante e' l'interazione fra trattamento e marker in un confronto appropriato, idealmente pre-specificato e replicato.

---

### DL-MECH-058 — pY33→pS14 e' un modello di stato, non uno switch molecolare dimostrato

- **Status:** `promoted-to-CC` · **Tag:** REVIEW/BACKGROUND + declassificazione causale
- **Fonte:** Liu et al. 2022, PMID 35883580 / PMCID PMC9323965; testo, otto figure, legenda PDF e tre video letti integralmente. Dossier: `staging/deepdive_PMID35883580_Liu2022.md`.
- **Statement:** `pattern pY33/pS14 fra contesti —non dimostra→ conversione temporale diretta o switch causale universale`.
- **Evidenza:** la review aggrega studi precedenti con pY33 associata a stress/apoptosi e pS14 a lesioni tumorali/AD. Non presenta cinetica nello stesso sistema, identità di chinasi/fosfatasi, mutanti phospho-null/mimetic validati o rescue.
- **Lineage:** 30/86 referenze includono N.S. Chang; figure e video sono dati adattati/ripubblicati. La coerenza interna non e' replica indipendente.
- **Video:** tre sferoidi 4T1 qualitativi supportano differenze con anticorpi sotto ceritinib, ma sono campi diversi senza quantificazione/repliche e S3 ha PI già al basale.
- **NON DATO:** nessuna PTM in WOREE/Q230P, nessuna efficacia clinica di Zfra/WWOX7-21/HAson8/Z cells, nessuna validazione della transizione in neuroni di paziente.
- **Belief:** basso sulla transizione come meccanismo universale; medio su pY33/pS14 come readout contestuali da validare; nullo su trasferimento terapeutico al genotipo di riferimento.
- **Interconnessioni:** [[paper_registry_current#CORPUS-STUB-009]] · *CC-2026-07-22-006 (private commit queue)*.

**Next-search agenda:** `READ_NEXT` PMID 35715422, coorte EIMFS di 36 bambini; verificare quali geni sono realmente diagnostici, quanti casi WWOX sono presenti e se il paper aggiunge fenotipo/gestione o soltanto pannello genetico.

**Riflessione di processo:** una review grafica puo' trasformare associazioni longitudinalmente separate in una freccia di “transition”. Ogni switch richiede prova nello stesso sistema, ordine temporale, perturbazione dei due stati e rescue; altrimenti resta una tassonomia di stati.

---

### DL-MECH-059 — Una doppia diagnosi impedisce attribuzioni WWOX-specifiche

- **Status:** `promoted-to-CC` · **Tag:** DATO CLINICO CONFUSO + guardrail di attribuzione
- **Fonte:** Yang et al. 2022, PMID 35715422 / PMCID PMC9205988; testo, cinque tabelle e Figura 1 letti integralmente. Dossier: `staging/deepdive_PMID35715422_Yang2022.md`.
- **Statement:** `fenotipo/risposta in portatore WWOX+ATP7A —non determina→ effetto WWOX-specifico` senza disambiguazione della seconda diagnosi.
- **DATO:** il solo caso WWOX ha p.M1? LP + p.H78Y VUS e una frameshift patogena ATP7A, con ceruloplasmina bassa e fenotipo Menkes; RM anomala, grave ritardo e controllo finale inefficace.
- **INTEGRITY:** la Tabella 3 classifica il controllo come inefficace ma elenca oxcarbazepina “efficace”; dose, tempo ed entita' della risposta non sono riportati.
- **PROGNOSI:** RM anomala non aumenta l'inefficacia (`47,1%` vs `47,4%`); burst-suppression ha inefficacia inferiore (`14,3%` vs `36,8%`) pur con mortalita' maggiore. Nessun test o aggiustamento sostiene un predictor.
- **Belief:** alto sul confondimento duale e sulle incongruenze numeriche; basso su qualunque attribuzione WWOX-specifica o marker prognostico.
- **il genotipo di riferimento:** nessuna informazione su Q230P/`c.1057-2A>G`; nessun farmaco o biomarcatore promosso. Il valore e' un guardrail per evitare trasferimenti da casi multi-diagnosi.
- **PREMESSA: DATO:** ATP7A patogena e segni biochimico-clinici Menkes coesistono nel medesimo paziente.
- **REVIVAL_TRIGGER:** caso WWOX senza seconda diagnosi, variante funzionalmente validata, fenotipo e risposta longitudinali con misura pre/post e replica indipendente.
- **Interconnessioni:** *CC-2026-07-22-007 (private commit queue)* · [[claim_registry_current#CLAIM 031]].

**Next-search agenda:** `READ_NEXT` PMID 37583270, coorte multicentrica indiana IESS di 124 bambini; verificare il numero reale di casi WWOX, definizione degli outcome, terapie e separazione fra descrizione sindromica e genotipo.

**Riflessione di processo:** un gene presente in tabella non e' automaticamente la causa isolata del fenotipo. Nei casi con due diagnosi plausibili, ogni arco gene→fenotipo→farmaco deve essere marcato come non identificabile finche' dati funzionali o casi indipendenti non separano i contributi.

---

### DL-MECH-060 — La composizione dei positivi genetici non e' resa diagnostica né prevalenza

- **Status:** `promoted-to-CC` · **Tag:** COORTE SELEZIONATA + guardrail di denominatore
- **Fonte:** Nagarajan et al. 2023, PMID 37583270 / PMCID PMC10690684; testo, quattro tabelle, tre figure e supplementi S1–S2 letti integralmente. Dossier: `staging/deepdive_PMID37583270_Nagarajan2023.md`.
- **Statement:** `frequenza di un gene fra casi geneticamente confermati e reclutati —non determina→ prevalenza o yield nel totale IESS` senza denominatore dei testati/negativi.
- **DATO:** 124 positivi selezionati includono 104 disturbi nucleari monogenici e quattro WWOX null-like; il totale IESS valutato, i negativi e la resa per test non sono disponibili.
- **WWOX:** esordio spasmi 2–4 mesi, microcefalia e ipotonia in 4/4. Tre sono classificati seizure-free a 6–12 mesi, uno ha DRE e KD fallita a 30 mesi; nessun protocollo uniforme o sviluppo standardizzato.
- **INTEGRITY:** `97/124` e' 78,2%, non 72,5%; le percentuali di ambulation/scuola usano il totale 124 anziché i denominatori applicabili; p.Trp398Ter e' etichettata missense.
- **Belief:** alto sul fenotipo descrittivo e sul guardrail; basso su frequenze di popolazione, confronto terapeutico o prognosi WWOX-specifica.
- **il genotipo di riferimento:** nessun dato Q230P/N-M, biomarcatore o terapia. Coerente ma non quantitativo con `seizure control ≠ developmental rescue`.
- **PREMESSA: DATO:** il campionamento parte dai geneticamente confermati e non conserva il denominatore di tutti gli IESS.
- **REVIVAL_TRIGGER:** registro prospettico consecutivo con tutti gli IESS, test uniformi, negativi, denominatori per piattaforma e follow-up genotipo-specifico.
- **Interconnessioni:** *CC-2026-07-22-008 (private commit queue)* · [[claim_registry_current#CLAIM 031]].

**Next-search agenda:** `READ_NEXT` PMID 41378749, studio folati/difetti del tubo neurale nel Bangladesh; spremere il valore metodologico/traslazionale senza confondere contesto prenatale generico con WWOX.

**Riflessione di processo:** prima di interpretare una percentuale genetica bisogna nominare il denominatore reale: tutti i pazienti, tutti i testati, soli positivi o soli pubblicabili. Senza questa distinzione, una “landscape” puo' diventare involontariamente un falso yield.

---

### DL-MECH-061 — Ca²⁺→calpaina come regolatore dell'ABBONDANZA di WWOX in un neurone eccitabile (NON come via di degradazione)

- **Status:** `open-lead` · **Tag:** INFERENZA meccanicistica + guardrail di via di turnover
- **Fonte:** Saadane et al. 2021, PMID 34214506 / PMCID PMC8579242; testo, Figure 1–10 e Tabelle 1–2 letti integralmente. Ricevuta `FTR-20260726-34214506-01`. Dossier: `staging/commit_candidate_20260726_001.md`.
- **Statement:** `attività calpainica ↑ —associata a→ WWOX (proteina e mRNA) ↑` in fotorecettori di topo diabetico. La freccia è **misurata come associazione**, non come proteolisi.
- **DATO:** proteomica label-free non guidata, log2 LFQ `N −3.55 → D −1.75 → DT −2.94` (p 0.002 / 0.01); `Wwox` mRNA ↑1.9× nella retina esterna; in 661W l'alto glucosio alza `Wwox` e l'inibitore di calpaina annulla il rialzo.
- **🔴 CORREZIONE ALLA FONTE:** gli autori scrivono *«Wwox was identified as a substrate for calpain»* e disegnano l'arco come **linea continua = via confermata** in Figura 10. **Non è dimostrato:** nessun saggio di taglio, nessun frammento; la calpaina sale **e WWOX sale** (un substrato proteolitico scenderebbe); sale anche l'mRNA, che la proteolisi non produce. Via alternativa già presente nella loro discussione: calpaina→IκBα→NF-κB→**trascrizione** di `Wwox`. Vedi [[dismissal_ledger_current#DIS-008 — «La calpaina è una via di degradazione/turnover per WWOX» → ⏸️ **NON STABILITA (rigettata come affermazione, non come possibilità)**]].
- **Perché conta per il modello:** l'eccitotossicità e il carico di Ca²⁺ da crisi attivano la calpaina. Se la calpaina modula l'abbondanza di WWOX, in un allele ipomorfo il **carico convulsivo potrebbe retroagire sulla WWOX residua** — un anello feed-forward. `IPOTESI`, non dimostrata in nessun sistema WWOX.
- **Belief:** alto sull'associazione calpaina↔abbondanza di WWOX in questo sistema; **nullo** sulla proteolisi; basso su qualunque trasferimento al CNS pediatrico.
- **Densità di campo (misurata 2026-07-26):** `WWOX AND calpain` = **2** record in tutto PubMed; `WWOX AND photoreceptor` = 2; `WWOX AND retina` = 4. Intersezione praticamente vergine.
- **PREMESSA: DATO:** la calpaina è una proteasi Ca²⁺-dipendente attivata da carico di Ca²⁺. **PREMESSA: DEFAULT_FROM_TEXTBOOK (RESPINTA):** «una proteasi che regola una proteina la taglia».
- **REVIVAL_TRIGGER (per l'arco proteolitico):** frammento di taglio di WWOX su attivazione calpainica; digestione in vitro di WWOX ricombinante; sito di taglio mappato; caduta della proteina a mRNA costante.
- **Interconnessioni:** *CC-20260726-001 (staging)* · [[claim_registry_current#CLAIM 028]] · [[claim_registry_current#CLAIM 009]] · [[dismissal_ledger_current#DIS-008 — «La calpaina è una via di degradazione/turnover per WWOX» → ⏸️ **NON STABILITA (rigettata come affermazione, non come possibilità)**]].

**Next-search agenda:** `READ_NEXT` le due sole altre voci dell'intersezione WWOX×calpaina; poi rif. 38 e 39 di questa fonte (WWOX attivato in fotorecettori degeneranti da danno luminoso e in topi `rd`; ortologo WWOX di *Drosophila* su metabolismo aerobico e stress ossidativo) — entrambi WWOX-diretti e mai risolti a PMID in questa sessione: **debito di lettura esplicito**.

**Riflessione di processo:** l'assenza di expertise di dominio nel gruppo che pubblica non invalida l'osservazione — la rafforza quando il dato è non guidato — ma **predice l'errore interpretativo**. Un laboratorio con 140 lavori su retinopatia diabetica e 1 su WWOX produce un hit proteomico affidabile e un'etichetta meccanicistica da manuale. Le due cose vanno pesate separatamente.

---

### DL-MECH-062 — Neuroligina-3 nello stesso set proteomico calpaina-sensibile

- **Status:** `open-lead` · **Tag:** IPOTESI — ago incidentale
- **Fonte:** Saadane et al. 2021, PMID 34214506, Tabella 2 (letta da immagine rasterizzata, non dal livello testo).
- **DATO:** `Nlgn3` compare fra le 15 proteine alterate dal diabete e normalizzate dall'inibitore di calpaina (log2 `−1.18 → −0.43 → −1.10`, p 0.02 / 0.02).
- **Perché conta:** NLGN3 è una molecola di adesione sinaptica legata a bilancio E/I, autismo ed epilessia — assi centrali del modello di malattia. Nessun legame WWOX–NLGN3 è qui affermato né implicato.
- **Belief:** basso. È una co-occorrenza in una tabella, non un arco.
- **REVIVAL_TRIGGER:** qualunque evidenza di co-regolazione WWOX–NLGN3, o di NLGN3 in un modello WWOX-deficiente.
- **Interconnessioni:** [[discovery_ledger_current#DL-MECH-061 — Ca²⁺→calpaina come regolatore dell'ABBONDANZA di WWOX in un neurone eccitabile (NON come via di degradazione)|DL-MECH-061]].

**Riflessione di processo:** l'ago stava in una tabella supplementare-simile che nessuna ricerca per parola chiave «WWOX» avrebbe restituito. È il caso d'uso letterale di *the gold is in the details*.

---

## Run 2026-07-26 — full-text certification PMID 35716775

### STATUS UPDATE — DL-MECH-017 — WW2 non è soltanto uno chaperone: è un secondo modulo di binding condizionale

- **Status:** `open` → `maturing` · **Tag:** DATO strutturale/biofisico + INFERENZA di assay design
- **Fonte certificata:** Rotem-Bamberger et al. 2022, PMID 35716775 / PMCID PMC9293652 / DOI 10.1016/j.jbc.2022.102145; main text, Figure 1–8, Tabelle 1–4 e supplemento S1–S6 letti integralmente. Dossier: `staging/deepdive_PMID35716775_RotemBamberger2022.md`; ricevuta completa `FTR-20260726-35716775-02`.
- **Correzione/raffinamento:** il vecchio enunciato `WW2 —stabilizes→ WW1_fold` resta supportato ma era incompleto. La catena completa è `WW2 —pre-orders→ WW1` e, per ligandi tandem con geometria compatibile, `PPxY1—binds→WW1 → local concentration ↑ → PPxY2—binds weakly→WW2 → affinity ↑`.
- **Quantificazione:** PY3 su WW1 `K_D 78 ± 10,9 μM`; su WW1–WW2 `30 ± 2,3 μM`. PY3PY3 ingegnerizzato su WW1–WW2 `3,1 ± 0,3 μM`, ma su WW1 isolato `50 ± 16 μM`: l'aumento ~10× richiede WW2 e non è semplice avidità.
- **Guardrail:** l'effetto diretto WW2 più netto usa peptidi tandem con linker corto ingegnerizzato. Il PY1PY2 naturale lega il tandem a `14 ± 2,6 μM` ma mostra affinità apparente WW2 di circa `1000 μM`, quindi prevalentemente WW1. `due motivi presenti —non implica automaticamente→ occupazione WW2`.
- **Belief:** alto su stabilizzazione WW2→WW1 e cooperatività topology-dependent nel frammento; medio sul pose parallelo atomistico; basso sul trasferimento a WWOX full-length/Q230P.
- **Interconnessioni:** [[claim_registry_current#CLAIM 024]] (corrobora e raffina) · [[claim_registry_current#CLAIM 028]] (supporta partner/context dependence) · [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]] (solo principio di assay, non prova SDR).

### DL-BIO-011 — Pannello multivalente PPxY come endpoint prossimale di rescue funzionale WWOX

- **Status:** `open` · **Tag:** IPOTESI sperimentale · **Tier:** 1/2 research assay, non biomarcatore clinico validato
- **Source:** PMID 35716775, Tabelle 2–4 e Figure 4–7; dossier e ricevuta come sopra.
- **What is measured:** funzione di binding topology-dependent di WWOX full-length · **Assay:** partner occupancy/co-IP o biophysical binding, con single-PPxY, natural dual-PPxY e engineered dual-PPxY positive control · **Matrix:** cellule isogeniche/recombinant protein; non sangue/CSF
- **Closeness to WWOX:** diretta: misura una funzione fisica del tandem WW1–WW2, ma deve essere adattata dalla proteina frammento al full-length.
- **ABC map:** A=`WWOX WT/Q230P/corretto` · B=`solubilità + localizzazione + geometria WW1–WW2` · C=`occupancy e output su partner PPxY a diversa topologia`.
- **Reasoning chain:** il paper dimostra che abbondanza e singolo peptide non esauriscono la funzione; un rescue Q230P valido deve recuperare proteina solubile **e** una gerarchia di binding/partner routing coerente. Tag IPOTESI perché Q230P e full-length non sono testati.
- **Evidence:** supports=`NMR+ITC+SEC–MALS convergenti nel frammento` · refutes=`nessuno sul pannello full-length` · neutral/unknown=`effetto del dominio SDR e delle PTM`.
- **What would validate it:** WT/null/Q230P/isogenic-corrected full-length nello stesso sistema; almeno due readout ortogonali (occupancy + localizzazione/output); criteri pre-specificati.
- **Applicabilità al modello di malattia:** alta come controllo di qualità di un futuro rescue, nulla come test clinico attuale.
- **Interconnessioni:** [[research_candidates_current#RC-013 — Experimental validation of Q230P instability|RC-013]] · [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]] · DL-MECH-017.

### DL-MECH-063 — La topologia del partner è parte dello stato funzionale di WWOX

- **Status:** `open` · **Tag:** INFERENZA meccanicistica
- **Source:** PMID 35716775, Figure 5–8 e Tabelle 2–4.
- **Statement:** `numero di PPxY da solo —non determina→ affinità/occupazione WW2`; servono sequenza, carica flanking, distanza e linker.
- **DATO:** PY1PY2 naturale, PY1PY2S, PY1PY3 e PY3PY3 mostrano affinità e CSP WW2 differenti; accorciare/sostituire il linker cambia l'ingaggio WW2 anche con gli stessi motivi terminali.
- **Why it matters:** la funzione residua di una variante WWOX può essere partner-selettiva; un singolo score “WWOX activity” rischia di nascondere conservazione/perdita differenziale dell'interattoma.
- **Belief:** alto nel sistema peptidico; medio-basso nel proteoma cellulare full-length.
- **Possible next step:** catalogare i partner WWOX con motivi PPxY singoli/tandem e testare un pannello minimo in cellule full-length; evitare predizioni da motif count senza struttura/linker.
- **Interconnessioni:** DL-BIO-011 · [[claim_registry_current#CLAIM 024]] · [[claim_registry_current#CLAIM 028]].

**Next-search agenda:** priorità a PMID 24308844 (WWOX–ErbB4, fonte primaria precedente) solo se il ledger non contiene una ricevuta completa; domanda: il ranking di affinità e la geometria osservati con peptidi sopravvivono in costrutti più lunghi/cellule? In parallelo, risolvere l'identità bibliografica di `CORPUS P204` senza creare un PAPER duplicato.

**Riflessione di processo:** la distinzione fra peptide naturale e linker ingegnerizzato ha cambiato il peso del messaggio: il “10×” è reale ma non generalizzabile a ogni partner tandem. Il supplemento S3 ha inoltre mostrato che una parte del CD viene dal peptide; supplementi e costrutti sono parte del risultato, non decorazione.

### Change-log 2026-07-26

- `DL-MECH-017`: fonte full-text certificata, meccanismo raffinato, status `maturing`.
- Creati `DL-BIO-011` e `DL-MECH-063`.
- Accodato `CC-20260726-002`; nessun aggiornamento diretto ai quattro current scientifici.

### STATUS UPDATE — autovalutazione del run PMID 35716775

- **Diagnosi durevole:** [[2026-07-26_PMID35716775]] — copertura, contenuto, gruppo,
  inferenze, landing, attriti, skill usate/rifiutate e micro-upgrade verificati.
- **Verdetto separato:** paper `PASS`; workspace `BLOCK_BATCH_COMMIT` finché la ricevuta
  concorrente di PMID 22193544 non atterra e la collisione del commit-candidate non viene
  risolta. Il verde locale non maschera il blocco globale.

---

## Run 2026-07-26 — deep dive PMID 22193544 (Wang 2012, WWOX ⊣ GSK3β)

Fonte unica: **PMID 22193544 / PMC3354054 / DOI 10.1038/cdd.2011.188**, letta integralmente
(ricevuta `FTR-20260726-22193544-01`, figure e supplementari ispezionate come immagini).
Candidato: `CC-20260726-003`. Manifest: `deepdive_manifests/PMID22193544.json`.

### DL-MECH-064 — WWOX è un inibitore diretto di GSK3β via motivo Axin-like 388–407/L404, **S9-indipendente**, con Tau come effettore
- **Status**: open · **Tag**: `DATO` (biochimica, cinque saggi ortogonali) + `IPOTESI` (trasferimento al neurone umano e al genotipo di riferimento)
- **Fonte**: Wang HY, Juo LI, Lin YT, Hsiao M, Lin JT, Tsai CH, Tzeng YH, Chuang YC, Chang NS, Yang CN, Lu PJ 2012, *Cell Death Differ* 19(6):1049-1059 — **PMID 22193544**, PMC3354054
- **Finding (DATO)**: WWOX lega GSK3β col dominio **ADH/SDR**, sul segmento **388–407** omologo al motivo di docking di Axin1-GID/Axin2/FRAT1/GSKIP (26–40% similarità), con **L404 necessario**. In vitro l'inibizione della fosforilazione di Tau è quasi totale (⌀1.00 → **0.07**; `L404A` **0.96**); in cellula pTau **S396 → 0.18** e **S404 → 0.28**, mentre **S422** (sito MKK4) è intatto. WWOX restituisce a Tau la capacità di promuovere l'assemblaggio dei microtubuli (⌀0.15 → ⌀0.30 di torbidità; `L404A` nulla). Co-IP reciproco fra **proteine endogene in cervello di topo**. Il peptide **WWOXtide³⁸⁸⁻⁴⁰⁷** riproduce l'inibizione, ma solo a **concentrazione millimolare** (1 mM → 0.07). **Epistasi**: il knockdown di Tau annulla il beneficio *sia* della sovraespressione di WWOX *sia* del knockdown di GSK3β, e WWOX + siRNA-GSK3β **non è additivo** → una sola via lineare, Tau effettore.
- 🔑 **Il dettaglio che vale più del titolo**: tutto questo avviene con **GSK3β totale, fosfo-GSK3β **S9**, β-catenina e fosfo-β-catenina invariati** per 4 giorni. L'inibizione **non passa** dall'interruttore canonico S9: è occupazione del sito di docking dei substrati.
- **Statement causale**: `WWOX —(L404, blocco del sito di docking)⊣ GSK3β —(S396/S404)⊣ Tau —→ assemblaggio microtubuli —→ neurite outgrowth`
- **Rilevanza di malattia / implicazione**: due conseguenze operative, **nessuna terapeutica**. (1) **Avvertenza di misura, immediatamente azionabile**: una iperattività di GSK3β dovuta a perdita di WWOX sarebbe **invisibile a un western pGSK3β-S9**, che è l'assay standard → qualunque studio WWOX-DEE che lo usi come readout di attività produrrà un **falso negativo**. Questo tagga anche una premessa di [[claim_registry_current#CLAIM 016]]: *«l'abbondanza di GSK3β riporta l'attività di GSK3β»* → 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK`, qui dissociate. (2) Fornisce a [[claim_registry_current#CLAIM 030]] il **readout funzionale** che le mancava, con controlli già esistenti (vedi UPGRADE in `DL-MECH-019`).
- **Limiti da non perdere**: linea unica SH-SY5Y (neuroblastoma, aneuploide); tutto in sovraespressione; stechiometria endogena WWOX:GSK3β **mai misurata**; endpoint di differenziamento contato a mano e non in cieco; **magnitudo non riproducibile fra figure dello stesso lavoro** (RA a d4: ⌀72% in Fig 1a vs ⌀46% in Fig 1e; WWOX+RA a d1: ⌀13→23% in Fig 5g vs ⌀18→44% in Fig 6b); condizioni del saggio chinasico **non ricostruibili univocamente** (0.3 vs 0.2 µg di GST-WWOX, 25 µg/ml vs 0.5 µg di Tau, 30 °C/20 min vs 20 °C/10 min fra Methods, Results e legenda); il modello strutturale Fig 3f–h è **predizione GOR IV innestata su 1O9U**, non dato strutturale — il risultato funzionale su L404 è però indipendente da esso. **Nessun allele WWOX-DEE testato.**
- **Belief**: alto sul meccanismo biochimico (cinque saggi, una mutazione che rompe tutto, co-IP endogeno in cervello); medio-basso sul trasferimento al neurone umano WWOX-carente (mai testato).
- **Esperimento**: pull-down GSK3β + inibizione della chinasi su **WT vs Q230P vs G372R vs L404A**.
- **Interconnessioni**: `DL-MECH-019` · `DL-MECH-065` · `DL-MECH-066` · `DL-BIO-012` · [[claim_registry_current#CLAIM 016]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 028]] · [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]] · `DIS-009`

### DL-MECH-065 — Il degrone ERLIQ e la funzione GSK3β potrebbero essere **lo stesso evento conformazionale**
- **Status**: open · **Tag**: 🔴 `IPOTESI` — poggia su **due** premesse in-silico, entrambe `PREMISE: INFERENZA`
- **Fonte**: composizione fra il mapping d'interfaccia di **PMID 22193544** (L404 in contatto idrofobico con V267/L270 e I296 di GSK3β) e la misura interna del red-team Q230P (**L404 sepolto, RSA 0.02**, su monomero AlphaFold)
- **Finding**: se L404 è **sepolto nel monomero** *e* **residuo d'interfaccia** per GSK3β, allora l'elica 388–407 deve **staccarsi dal core SDR** per ingaggiare la chinasi. Ma 402–406 è il **degrone canonico ERLIQ**. Ne segue che l'evento che espone il degrone e l'evento che abilita il legame a GSK3β potrebbero **coincidere**.
- **Statement causale (ipotetico)**: `esposizione elica 388-407 —abilita→ {legame GSK3β, riconoscimento del degrone}` ⇒ turnover e funzione **accoppiati**, non indipendenti
- **Rilevanza di malattia / implicazione**: se vero, riscrive il target di [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]]: **non si può stabilizzare quella regione senza spegnere la funzione** — non per sfortuna di design, ma per costruzione. Sarebbe la forma più forte di **D-04** incontrata finora, e spiegherebbe *perché* le due zone-degrone candidate confinino entrambe con una funzione da non toccare. Sarebbe anche un meccanismo per cui l'abbondanza di WWOX e la sua attività su GSK3β si muovono insieme.
- 🔴 **Onestà sulle premesse**: (a) RSA 0.02 è calcolato su **struttura predetta**, non sperimentale; (b) il modello d'interfaccia di Wang è **GOR IV innestato su 1O9U con sostituzione di catene laterali**, e il metodo è auto-citato dallo stesso gruppo (rif. 18, Tang 2011, coautore Chuang YC) → **indipendenza ridotta**. Nessuna delle due è dato strutturale. **Non trattare come stabilito.**
- **Belief**: basso-medio. Meccanicisticamente elegante, evidenza strutturale assente.
- **Esperimento**: HDX-MS o mutagenesi di rigidificazione sul core SDR con doppio readout — emivita **e** legame a GSK3β. Se rigidificare aumenta l'emivita *e* abbatte il legame, l'accoppiamento è dimostrato e TX-003 va ridisegnato.
- **Interconnessioni**: `DL-MECH-064` · `DL-MECH-019` · [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]]

### DL-MECH-066 — L'**isoforma GSK3β2 neurone-specifica** potrebbe risolvere la contraddizione storica GSK3β↔neurite (e cambia la lettura del litio)
- **Status**: open · **Tag**: `IPOTESI` (derivata da reference list, fonte primaria **non ancora letta**)
- **Fonte**: rif. 27 di PMID 22193544 → **Castaño Z, Gordon-Weeks PR, Kypta RM**, *The neuron-specific isoform of glycogen synthase kinase-3β is required for axon growth*, J Neurochem — **PMID 20067585**. **Ignoto al modello prima di oggi.** In coda come [[full_text_queue_current#FT-022]].
- **Finding**: Wang 2012 **ammette e non risolve** una contraddizione: la sua Discussion cita più lavori (rif. 25, 26, 27) in cui l'**attivazione** di GSK3β *favorisce* la crescita neuritica, mentre il suo modello dice l'opposto. La risoluzione candidata che il paper non prende in considerazione è **l'identità dell'isoforma**: esiste una isoforma GSK3β neurone-specifica, e il rif. 27 la dichiara *richiesta* per la crescita assonale. Wang usa costrutti **GSK3β generici** (WT, S9A, kinase-dead, R96A) e non distingue le isoforme in nessun esperimento.
- **Rilevanza di malattia / implicazione**: se l'arco WWOX-rilevante passa per una isoforma e la crescita assonale per l'altra, allora **un inibitore globale come il litio colpisce entrambe** — cioè potrebbe spegnere l'iperfosforilazione di Tau *e insieme* la crescita assonale, in un cervello in sviluppo. Sarebbe un rischio su [[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]] **non presente oggi nel punteggio**. È anche il `REVIVAL_TRIGGER` (c) di `DIS-009`: una selettività sarebbe di nuovo possibile, ma per identità di isoforma, non per selettività di substrato.
- 🔴 **Come è stato trovato, e perché è un difetto di processo**: leggendo la **reference list**, che nella prima passata **non era stata nemmeno elencata**. Il debito multi-hop era stato *dichiarato* e non *svolto*; dichiararlo non lo paga. Vedi la diagnosi in `session_evaluations/2026-07-26_PMID22193544.md`.
- **Belief**: basso sul meccanismo (fonte primaria non letta, inferenza da titolo e contesto di citazione); **alto sul fatto che sia una domanda aperta e non posta**.
- **Esperimento**: prima leggere PMID 20067585; poi ripetere i punti chiave di Wang distinguendo le isoforme.
- **Interconnessioni**: `DL-MECH-064` · `DIS-009` · [[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]] · [[full_text_queue_current#FT-022]]

> #### 🔧 AGGIORNAMENTO 2026-07-26 (stessa giornata) — ipotesi **sostanziata**, e il verso è più interessante del previsto
> **Acquisizione**: PMID 20067585 è **paywalled** — cascata esaurita e documentata (PMC non
> depositato · Unpaywall `closed` · OpenAlex nessun repository · Semantic Scholar `CLOSED` ·
> Wiley HTTP 403). Quattro fonti indipendenti concordano. Ricevuta
> `FTR-20260726-20067585-01`, profondità **`abstract_only`**, copertura `unavailable` — non
> *saltata*: **non ottenibile lecitamente**. ⚠️ Quanto segue è **di livello abstract**.
>
> **`DATO` (abstract) — GSK-3 sono TRE enzimi**: GSK-3α, GSK-3β1 e l'isoforma
> **neurone-specifica GSK-3β2** (inserto di 13 aa nel dominio catalitico, splicing fra esone 8
> e 9). Il verso è **opposto** a quello di Wang: *silenziare* β2 **inibisce** la crescita
> neuritica RA-indotta **in SH-SY5Y** e la crescita assonale in neuroni corticali di ratto; il
> rescue riesce **solo** con β2, non con α né β1; l'espressione ectopica di β2 **aumenta**
> l'effetto di RA e induce neuriti **anche senza RA**.
>
> 🔴 **Conflitto diretto con `DL-MECH-064` D14 — stessa linea cellulare, stesso stimolo.** Wang
> 2012 riporta che il knockdown di GSK3β **aumenta** la crescita neuritica (Fig 5c/d); Castaño,
> con silenziamento **isoforma-specifico**, riporta l'opposto per β2. La risoluzione è l'identità
> dell'isoforma: Wang usa un siRNA **generico** (Abnova H00002932-R02) e costrutti generici, che
> colpiscono **entrambe**. ⇒ il readout di differenziamento di Wang è il **netto di due archi
> opposti**. **Cosa NON è toccato**: la biochimica (legame 388–407/L404, inibizione in vitro,
> assemblaggio microtubuli), indipendente dall'isoforma. **Cosa è indebolito**: il passaggio
> interpretativo *«WWOX promuove il differenziamento inibendo GSK3β»*, ora vero solo per β1.
>
> **Corroborazione open access** del dettaglio assente dall'abstract (ricevuta
> `FTR-20260726-21776376-01`, `queried_not_full_read` su PMC3139124 — **non** lettura completa):
> β2 fosforila tau **più lentamente**, su residui in parte diversi e in parte sovrapposti, e
> **lega tau più debolmente**; ha **attività in vitro inferiore**; è arricchita in neuroni,
> **neuriti e coni di crescita**, con livelli **massimi nel cervello in sviluppo**. 🔑 **`Ser396`
> è fosforilato da ENTRAMBE le varianti**; `Ser199` è bersaglio di β1 e non di β2. Fonte primaria
> del punto: **Saeki 2011, PMID 21212533** → [[full_text_queue_current#FT-026]], **non letta**.
>
> **Conseguenza per S396/S404, i siti che contano in Wang**: **non sono isoforma-esclusivi**. Un
> inibitore che risparmiasse β2 ridurrebbe S396 solo **in parte**. Che il grosso sia comunque
> β1-dipendente (β2 più lenta, meno attiva, lega tau più debolmente) è **`INFERENZA`**.
>
> ##### 🔴 CORREZIONE 2026-07-26, dopo la lettura integrale di FT-026 — attribuzione sbagliata, mia
> Il blocco sopra attribuiva a **Saeki 2011** il dato dei *«residui in parte diversi»* e la coppia
> `Ser396`/`Ser199`. **Saeki 2011 non lo dice.** Letta integralmente (ricevuta
> `FTR-20260726-21212533-01`, `complete_fulltext_read`), quel lavoro misura **un solo sito, Ser396**,
> e non affronta mai la selettività di sito. Il claim sui *siti diversi* risale a **Mukai F,
> Ishiguro K, Sano Y, Fujita SC 2002, J Neurochem 81:1073-1083 — PMID 12065620**, che è il rif. 75
> della review PMC3139124 e il rif. 4 di Saeki: **mai letto**, ora accodato come
> [[full_text_queue_current#FT-027]].
>
> **Come è nato l'errore, perché conta più dell'errore**: ho letto una review (fonte secondaria)
> per estrazione mirata, e ho attribuito il contenuto al primo lavoro che la review citava accanto
> ad esso. La review citava *«[75, 76]»* per la frase su cinetica e siti, e *«[76]»* — Saeki — solo
> per l'interazione più debole. Verificare la fonte secondaria alla primaria è **esattamente** ciò
> che ha fatto emergere lo scarto: la disciplina ha funzionato, con un ciclo di ritardo.
>
> ⚠️ **E resta un buco che nessuno ha colmato: `Ser404` non è stato testato da Saeki.** È il secondo
> sito chiave di Wang 2012. Su `Ser396` sappiamo che entrambe le isoforme lo fosforilano (con β1
> molto più efficiente); su `Ser404` **non esiste dato per isoforma**. Da chiedere a FT-027.
>
> **Tag rivisto**: esistenza e ruolo opposto di β2 → `DATO` (abstract) · biologia comparata delle
> isoforme → `DATO` (review OA, fonte secondaria) · quale isoforma domini S396/S404 in un neurone
> WWOX-carente → **`IPOTESI`, mai misurata da nessuno**.

### DL-MECH-067 — 🔑 WWOX lega **il sito di Axin**, ed è quindi la classe di inibitore che la letteratura raccomanda per **risparmiare** l'isoforma neuronale
- **Status**: open · **Tag**: `INFERENZA` da convergenza di due fonti che non si parlano · **il lead terapeuticamente più interessante emerso finora sull'asse GSK3β**
- **Fonte**: convergenza fra **PMID 22193544** (Wang 2012, letto integralmente — WWOX lega la tasca di docking Axin/FRAT/GSKIP: α-elica G262-L273 + loop N285-H299, omologa ad Axin-GID) e **PMID 20067585** (Castaño 2010, `abstract_only`)
- **Finding**: Castaño riporta che **Axin si associa più facilmente a β1 che a β2**, e conclude — testualmente — che *«GSK-3 inhibitors that target the Axin-binding site in GSK-3 will preserve the beneficial effects of GSK-3β2 on axon growth»*. **WWOX lega esattamente quel sito.**
- **Statement causale (inferenziale)**: `ligando del sito Axin —inibisce preferenzialmente→ β1 (pro-fosforilazione tau, anti-crescita) —risparmiando→ β2 (pro-crescita assonale, arricchita nei coni di crescita, massima nel cervello in sviluppo)`
- **Perché è importante**: **nessuno dei due lavori fa questa connessione.** Wang cita Castaño (rif. 27) solo per *ammettere* una contraddizione sulla direzione, non per risolverla via isoforma; Castaño non conosce WWOX. Ne segue che **WWOX è un inibitore endogeno, naturale, della classe raccomandata** — isoforma-*biased* per costruzione strutturale, non per selettività di substrato. E ne segue un modello più coerente della patologia: **la perdita di WWOX de-reprime selettivamente β1** → più fosforilazione di tau *e* più inibizione della crescita, mentre β2 resta intatta. Più pulito del generico *«GSK3β sale»*.
- 🔴 **Premessa portante da verificare**: che il legame al sito di Axin conferisca **preferenza per β1**. 🔴 `PREMISE: INFERENZA` — deriva dall'affermazione abstract-level di Castaño sull'affinità di Axin, **non da una misura su WWOX**. Wang non ha mai testato le isoforme. **È l'esperimento decisivo, e non è mai stato fatto.**
- **Effetto sui candidati terapeutici — i due si separano in direzioni opposte**: (a) 🔴 **litio e inibitori ATP-competitivi globali** ([[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]]): nulla suggerisce che discriminino le isoforme, e la conclusione di Castaño implica che **non lo facciano** → sopprimere β2 **in un cervello in sviluppo** rimuove una chinasi pro-crescita arricchita nei coni di crescita e ai suoi massimi proprio in quella finestra. **Rischio di finestra evolutiva oggi assente dal punteggio SAFETY di TX-005.** (b) 🟢 **approcci diretti al sito Axin/GID**, inclusa la logica WWOX-mimetica: profilo **potenzialmente migliore**, per un motivo del tutto diverso da quello rigettato in `DIS-009`.
- **Belief**: medio sull'inferenza (due fonti solide ma una a livello di abstract, e il ponte è mio); **alto sul fatto che sia una domanda decisiva e non posta**.
- **Esperimento**: pull-down e saggio chinasico di WWOX (e di WWOXtide³⁸⁸⁻⁴⁰⁷) contro **β1 vs β2** in parallelo, con lettura di pTau S396/S404. Se WWOX inibisce β1 ≫ β2, la logica WWOX-mimetica acquista un razionale di sicurezza che il litio non ha. Se le inibisce uguale, cade — e con essa il vantaggio.
- **Interconnessioni**: `DL-MECH-064` · `DL-MECH-066` · `DIS-009` · [[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]] · [[full_text_queue_current#FT-022]] · [[full_text_queue_current#FT-026]]

### DL-MECH-068 — 🔑 **tau è un substrato SFAVORITO per β2**, e il discrimine è la coda C-terminale: un inibitore ATP-competitivo **non può** separare le isoforme, un ligando del sito di Axin sì
- **Status**: open · **Tag**: `DATO` (biochimica primaria, full text letto) + `INFERENZA` (conseguenza per il litio) + `IPOTESI` (preferenza di isoforma di WWOX, mai misurata)
- **Fonte**: **Saeki K, Machida M, Kinoshita Y, Takasawa R, Tanuma S 2011**, *Biol Pharm Bull* 34(1):146-149 — **PMID 21212533**, DOI 10.1248/bpb.34.146. Full text J-STAGE, letto integralmente (ricevuta `FTR-20260726-21212533-01`, figure ispezionate come immagini). Lab senza alcun investimento pregresso su GSK-3 (Tanuma S: 259 lavori, **1** su GSK, **0** su WWOX).
- **Finding (`DATO`)**: β2 fosforila tau su **Ser396** molto meno di β1 — in cellule HEK293T co-esprimenti (Fig 1) e con proteina ricombinante in vitro (Fig 3: β1 attiva già a **1 µg/mL**, β2 serve **10 µg/mL** → ~3–10×). 🔑 **Ma non è un deficit generale di attività**: la fosforilazione di **APP-Thr668 è equivalente** fra le due isoforme in cellula (Fig 2), e l'attività chinasica sul peptide **pGS-2 è equivalente e quantificata** (Tab. 1: β1 **234.5±7.8** vs β2 **246.5±2.4** nmol/min/mg — β2 marginalmente *superiore*). ⇒ **«tau è un substrato sfavorito per β2»**, non «β2 è una chinasi debole».
- **Meccanismo (`DATO`)**: la **coda C-terminale (CT, 40 aa)** ha **sequenza identica** nelle due isoforme (Fig 4), ma è **indispensabile per β2 e quasi dispensabile per β1**: `β2ΔCT` **perde quasi del tutto** l'attività su tau, `β1ΔCT` la riduce solo lievemente (Fig 5 — verificata come immagine: le bande αGSK-3β mostrano che ΔCT **è espresso**, quindi non è perdita di espressione). Interpretazione degli autori: β1 può ingaggiare tau via CT **e** regioni adiacenti, β2 **solo** via CT, la cui struttura d'ordine superiore è alterata dall'inserto. ⚠️ **La CT è invisibile in tutte le strutture cristallografiche di GSK-3β** (rif. 13–24) per flessibilità → **nessuna struttura di β2 esiste**, e il meccanismo resta un'ipotesi strutturale degli autori, dichiarata come tale.
- 🔑 **Il dato di posizione, verificato su fonte terza e citabile**: **UniProt P49841** — isoforma canonica **420 aa**; **isoforma 2 = `K303 → KDSSGTGHFTSGVR`**, cioè inserto di **13 residui dopo Lys303** (`VSP_004790`). La tasca di docking Axin/GID che **WWOX lega** è, per Wang 2012, l'α-elica **G262-L273** + loop **N285-H299**. ⇒ **l'inserto cade 4 residui a valle di H299**: immediatamente adiacente alla superficie di docking. Mentre il **sito ATP** (dominio catalitico, ~85 e ~134-200) è **identico** fra le isoforme e lontano da 303.
- **Statement causale**: `inserto 13aa dopo K303 —altera→ {struttura CT, superficie adiacente al loop di docking N285-H299} —riduce→ ingaggio di tau da parte di β2` ; e `sito ATP identico —implica→ inibitore ATP-competitivo NON discrimina β1/β2`
- **Rilevanza di malattia / implicazione — qui i due candidati si separano in modo pulito**:
  🔴 **(a) Litio e inibitori ATP-competitivi** ([[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]]): poiché le due isoforme differiscono **solo** per 13 residui dopo K303 e il sito ATP è identico, un inibitore ATP-competitivo **non può** separarle. Colpirebbe quindi anche **β2**, che Castaño riporta *necessaria* per la crescita assonale, arricchita nei **coni di crescita** e **massima nel cervello in sviluppo**. **Rischio di finestra evolutiva, oggi assente dal punteggio SAFETY di TX-005** — e ora sostanziato da identità di sequenza, non da congettura.
  🟢 **(b) Ligandi del sito Axin/GID, inclusa la logica WWOX-mimetica**: agiscono su una superficie **adiacente all'inserto**, quindi hanno una base strutturale per discriminare. Rafforza `DL-MECH-067`.
  🧩 **(c) Coerenza ritrovata**: β2 promuove la crescita assonale **pur essendo una cattiva chinasi di tau** ⇒ il suo ruolo sulla crescita passa per **altri substrati** (CRMP-2, MAP1B — non testati qui). Il profilo ideale diventa quindi esplicito: **inibire β1, risparmiare β2.**
- 🔴 **Premesse portanti da non perdere di vista**: (i) che il legame al sito di Axin conferisca preferenza per **β1** resta `PREMISE: INFERENZA` — deriva dall'affinità differenziale di **Axin** (Castaño, `abstract_only`), **mai misurata su WWOX**; (ii) Saeki usa **HEK293T**, non neuroni; (iii) **Ser404 non è stato testato** da nessuno per isoforma.
#### 🔴 AGGIUNTA 2026-08-10 — l'aggiudicazione di pagina chiude il debito di locator e corregge tre punti di questa voce

La lettura del 2026-07-26 era completa ma **senza locator**: il debito era dichiarato nel
manifest e non colmato. Colmarlo ha richiesto la strada lunga, perché il **text layer di questo
PDF è `SUSPECT`** — `×` diventa `U+0002`, `±` diventa `U+0003`, e **`µ` viene semplicemente
perso**, così che *«10 μl di tampone 2×»* si estrae come *«10 ml of 2\x02»*: un volume sbagliato
di mille volte, in una frase che continua a leggersi come inglese corretto. Non esiste superficie
XML/HTML per questo articolo. I 14 locator sono quindi ancorati alla **pagina stampata**, ognuno
dentro un ritaglio che si rigenera al proprio digest dal PDF sorgente
([`page_adjudications/PMID21212533/adjudications.json`](page_adjudications/PMID21212533/adjudications.json),
11 ritagli, `regenerate_adjudications.py verify` PASS). Aprire le figure ha cambiato tre cose.

1. 🔴 **Il fattore «~3–10×» sopra non è una misura, ed è sbagliato per difetto.** Le due
   titolazioni di Figura 3 **non sono appaiate**: β1 corre 0–0.1–0.3–1–3 µg/mL, β2 corre
   0–0.3–1–3–10. **Non esiste una concentrazione massima comune** e β1 non è mai stata testata a
   10. Il pannello inferiore αGSK-3β mostra enzima **solo nelle corsie più alte** di ciascuna
   serie: è un controllo di presenza, non di input equivalente. Nessuna densitometria, figura
   *«representative of three independent experiments»*. Ciò che il pannello sostiene è
   **β1-a-1 contro β2-a-10**, cioè **dell'ordine di 10× e plausibilmente più**; ciò che non può
   sostenere è un rapporto misurato. *Sostituire «~3–10×» con «≥10× a ispezione, non
   quantificato».*
2. 🔴 **La posizione dell'inserto: la figura degli autori e UniProt non concordano di un
   residuo.** Figura 4 marca l'inserto **fra V303 e K304**, e dà CT = **380–420** in β1 e
   **393–433** in β2, con didascalia *«The sequence of CT is identical between GSK-3β1 and
   GSK-3β2»*. Questa voce cita `UniProt P49841` / `VSP_004790` come **`K303`**. Nulla di portante
   si muove — su entrambe le numerazioni l'inserto cade **4–5 residui a valle di H299**, adiacente
   alla superficie di docking Axin/GID (`G262-L273` + `N285-H299`) che WWOX lega, e lontano dal
   sito ATP identico — ma il numero **non va citato come se le due fonti coincidessero**.
3. 🟢 **Figura 5 dice più di quanto dicesse questa voce, nella direzione giusta.** Nel pannello
   β1 la banda `αptau(Ser396)` di `ΔCT` è **comparabile al WT** mentre la sua banda `αGSK-3β` è
   **visibilmente più debole** del WT: fosforilazione piena con **meno enzima**. Nel pannello β2
   `ΔCT` scende **al livello del mock** con banda `αGSK-3β` forte. Quindi la perdita in β2 non è
   perdita di espressione *e* la tenuta in β1 non è un vantaggio di espressione. 🔴 **Confine:**
   i due pannelli sono **blot separati** — la figura confronta WT contro ΔCT *dentro* un'isoforma
   e non autorizza alcun confronto di ampiezza β1-contro-β2.
4. ⚠️ **Figura 1 non è normalizzata, e conviene saperlo.** Il controllo `αtau` **non è uguale fra
   le corsie**: nella corsia β1 domina la banda superiore (ritardata) e quella inferiore è
   impoverita — lo shift di mobilità atteso da tau fortemente fosforilata — mentre mock e β2
   mostrano entrambe le bande. Nessuna densitometria. La direzione dell'asimmetria corre **contro**
   la conclusione del paper, non a favore: β1 raggiunge più fosfo-tau su meno substrato non
   spostato. La conclusione regge; un numero preso da quel pannello no.
5. ⚠️ **Il controllo APP è «equivalente per segnale totale», non per unità di enzima**: nel
   pannello inferiore di Figura 2 β2 è espressa almeno quanto β1.

Nessuna di queste sposta lo `statement causale` né l'argomento del sito ATP. Tre spostano un
numero che era presentato come misura, e uno rafforza il meccanismo. Locator:
`deepdive_manifests/PMID21212533.json`, voci 5–11.

- **Belief**: **alto** sul dato biochimico (controlli interni di specificità APP e pGS-2, doppio sistema cellule + ricombinante, figure coerenti col testo); **alto** sull'argomento del sito ATP (identità di sequenza); **medio-basso** sulla preferenza di isoforma di WWOX (non misurata).
- **Esperimento**: invariato e decisivo — **WWOX e WWOXtide³⁸⁸⁻⁴⁰⁷ contro β1 vs β2 in parallelo**, con lettura di pTau S396 **e S404**. Aggiungere `β2ΔCT` come controllo: se WWOX inibisce β1 ≫ β2 e l'effetto su β2 non cambia rimuovendo la CT, la discriminazione è nella tasca di docking e non nella coda.
- **Interconnessioni**: `DL-MECH-064` · `DL-MECH-066` · `DL-MECH-067` · `DL-BIO-013` · `DIS-009` · [[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]] · [[claim_registry_current#CLAIM 016]] · [[full_text_queue_current#FT-027]] · [[full_text_queue_current#FT-028]]

### DL-BIO-013 — Il rapporto di splicing **β1:β2** di GSK3B come candidato modificatore genetico della severità
- **Status**: open · **Tag**: `IPOTESI` / `ESPANSIONE` · **Cosa si misura**: rapporto di trascritti GSK3B β1:β2 · **Matrice**: RNA (sangue, fibroblasti, organoidi) · **Tier**: 3 — distale, non WWOX-specifico
- **Fonte**: **PMID 20067585** (`abstract_only`): *«un polimorfismo genetico che aumenta il rapporto GSK-3β1/GSK-3β2 interagisce con gli aplotipi di tau per modificare il rischio di malattia in Parkinson e Alzheimer»*
- **Finding / implicazione**: esiste una **variabilità genetica umana comune** che sposta il rapporto fra l'isoforma pro-fosforilazione-tau e quella pro-crescita, con effetto dimostrato su rischio di malattia **in interazione con tau**. Se l'asse WWOX→β1→tau è reale, quel rapporto è un candidato **modificatore della severità** in un disturbo che già mostra ampia variabilità fenotipica a genotipo simile ([[claim_registry_current#CLAIM 017]], [[claim_registry_current#CLAIM 030]]).
- 🔴 **Limiti da non mascherare**: il dato è su malattie neurodegenerative dell'adulto, non su una encefalopatia evolutiva; è abstract-level; non esiste alcuna evidenza di interazione WWOX × GSK3B nell'uomo. **Non è un biomarcatore, è una domanda.**
- **Esperimento**: misurare il rapporto β1:β2 (qPCR isoforma-specifica) nei modelli WWOX-carenti già disponibili, prima di qualunque ipotesi clinica.
- **Interconnessioni**: `DL-MECH-067` · `DL-MECH-066` · [[claim_registry_current#CLAIM 017]] · [[claim_registry_current#CLAIM 030]]

### DL-BIO-012 — Il pull-down GSK3β come **readout di integrità del fold SDR** per gli alleli missense
- **Status**: open · **Tag**: `DATO` (il saggio esiste e funziona) + `IPOTESI` (che discrimini gli alleli di malattia) · **Cosa si misura**: legame WWOX–GSK3β e inibizione della fosforilazione di Tau · **Matrice**: proteina ricombinante, poi lisato cellulare · **Tier**: 1 — gene-linked, funzionale, diretto
- **Fonte**: **PMID 22193544** (saggio e controlli); domanda da [[claim_registry_current#CLAIM 030]]
- **Finding**: due saggi economici e già validati — pull-down GST e inibizione della chinasi su Tau — con una **mutazione di controllo interna** (`L404A`) che li azzera entrambi. Trasformano la domanda *«la proteina salvata è funzionale?»* in una misura binaria e leggibile.
- **Rilevanza di malattia / implicazione**: risponde a [[claim_registry_current#CLAIM 030]] meglio dell'attività ossidoreduttasica, il cui **substrato fisiologico è ignoto** — non si può misurare bene un'attività di cui non si conosce il substrato. E poiché **Q230 dista 174 residui da L404**, l'esito riporta **integrità globale del fold**, che è esattamente ciò che serve per decidere se uno stabilizzatore ha prodotto proteina *funzionale* o soltanto proteina *presente*. Da usare **in parallelo** all'abbondanza, mai in sua sostituzione.
- **Limite onesto**: nessun allele di malattia è stato testato in questo saggio da nessuno. Che discrimini Q230P da G372R è **previsione, non risultato**.
- **Esperimento**: WT vs Q230P vs G372R vs L404A, in parallelo a western per l'abbondanza.
- **Interconnessioni**: `DL-MECH-064` · `DL-MECH-019` · [[claim_registry_current#CLAIM 030]] · [[therapeutic_strategies_current#TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)|TX-003]] · [[discovery_ledger_current#DL-BIO-001 — Livello + attività ossidoreduttasica di WWOX in fibroblasti donor-derived, nominati dalla destabilizzazione predetta dell'allele missense SDR (AlphaFold3/AlphaMissense)|DL-BIO-001]]

---

### STATUS UPDATE — DL-MECH-055 (2026-08-05)

`DL-MECH-055` è stato **verificato in modo indipendente contro il documento**, non ereditato. Nella edizione pubblica non esisteva alcuna ricevuta per PMID 37519886 (`fulltext_receipts.py status --pmid 37519886` → `[]`, exit 1) e il dossier citato (`staging/deepdive_PMID37519886_Kolat2023.md`) non era presente, perché `staging/` è escluso dal privacy hard-guard: **la lettura era avvenuta, la prova non aveva viaggiato**. Il protocollo vieta di dedurre una ricevuta completa da un lead promosso, quindi il paper è stato riletto integralmente il 2026-08-05 — testo, sette figure principali e dieci figure supplementari **ispezionate come immagini**, tre tabelle supplementari, 80 referenze enumerate. Ricevuta `FTR-20260805-37519886-01`; dossier ricostruito allo stesso path.

**Esito: conclusioni confermate, nessuna correzione.** Il paragrafo di rischio strutturale di `DL-MECH-055` regge in ogni sua parte. La rilettura aggiunge però quantificazione e provenienza che il lead non conteneva, e che cambiano *quanto* il paper può essere citato:

- l'unità di replicazione è scritta **in faccia alla Figura 1** — *«each variant (WK, WA, WC, KA, KC, KK) had 3 biological replicates (one per specific cell line)»*;
- **miR-186 non è mai stato un DEG** nel loro stesso CAGE-seq: non compare fra i 31 ncRNA differenziali (Figura 2A) ed entra solo come nodo predetto da database (Figura 3A, Suppl. Fig. S1, senza il bordo che la legenda riserva ai DEG);
- la feature **meglio classificata era HIPK1-AS1** (AvgRank 1.0, `***`), scartata perché *scende* con WWOX-OE; `LINC01137` (AvgRank 2.6) è stata scelta perché la direzione corrisponde all'ipotesi sotto test → nuovo gate `RANK_OVERRIDE_SELECTION_GATE`;
- la correlazione che sostiene lo sponge è `r = −0.234` (5% di varianza) con una fascia densa di campioni a MIR186 = 0; `miR-6515` dava `r = −0.081, p = 0.102` ed è stato lasciato cadere;
- 🔴 **l'arco che fallisce la validazione indipendente è esattamente lo sponge**: in GSE31684 la correlazione LINC01137↔MIR186 sparisce, mentre WWOX↔LINC01137 e WWOX↔MIR186 tengono (Suppl. Fig. S8). Gli autori lo concedono in una subordinata; abstract e conclusione no;
- i numeri di sopravvivenza, leggibili solo nelle risk table: **WWOX non è prognostico in TCGA-BLCA su nessun endpoint** (`p = 0.163 / 0.392 / 0.943`), `MIR186` non lo è in nessuna delle due coorti, e il risultato di punta — `HR 0.190` per WWOX↑&LINC01137↑ — è **25 pazienti contro 7**, con 58 scartati su 93, non replicato in TCGA (`0.933 / 0.760 / 0.789`). I segnali prognostici più consistenti dell'intera tabella sono `RAB34` e `HES1`, che non appartengono all'asse del titolo → nuovo gate `CUTPOINT_ENDPOINT_DRIFT_GATE`;
- tre geni (`ACTB`, `S100A9`, `RPS19`) sono stati **rimossi dal set finale** perché introducevano «excessive deviation» (Suppl. Fig. S7), e l'intersezione a tre vie per il double-strand break repair è **vuota** (Suppl. Fig. S6) benché il DSBR sia uno dei cinque processi che strutturano l'analisi.

**Lezione di processo, indipendente dal paper:** un lead promosso in una edizione non è una lettura in un'altra. Il ledger portava la conclusione; il receipt ledger — l'unica autorità sulla lettura — era vuoto. La disciplina ha funzionato: ha imposto di riaprire il documento, e riaprendolo sono emersi undici fatti a livello di figura che il lead non conteneva.

---

### DL-MECH-069 — 🔑 L'efficienza dell'NMD potrebbe essere **WWOX-dipendente**, e questo tocca sia l'allele di sito accettore sia l'esperimento disegnato per caratterizzarlo

- **Status:** open · **Tag:** `DATO` (interazione WWOX·UPF1, misurata altrove) + `DATO` (WWOX-OE → UPF1 su, misurato due volte qui) + `IPOTESI` (che ne segua un cambio di flusso NMD) + 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` sul presupposto silenzioso
- **Fonte:** Kołat et al. 2023, PMID 37519886 / PMCID PMC10373930; lettura completa 2026-08-05, ricevuta `FTR-20260805-37519886-01`, dossier `staging/deepdive_PMID37519886_Kolat2023.md`. L'arco proteico proviene da Hussain et al. 2018, PMID 30619736 (TAP-MS, → `FT-038`).
- **Statement causale:** `WWOX —lega (WW1 ↔ ¹⁰⁰⁵PPGY¹⁰⁰⁸ di UPF1)→ UPF1` ; `WWOX-OE —aumenta→ trascritto UPF1` ; (ipotesi) `stato WWOX —modula→ efficienza NMD` ; (conseguenza) `efficienza NMD —determina→ destino del trascritto PTC dell'allele c.1057-2A>G`
- **DATO:** UPF1 è fra i top interattori di WWOX e ingaggia il dominio **WW1** tramite un motivo PPxY canonico — la stessa chimica di riconoscimento che il modello già usa per i partner di WWOX. In questo paper, WWOX-OE si associa a **UPF1 più alto** sia in CAGE-seq sia in qPCR (`p < 0,05` in entrambi), nelle stesse cellule in cui l'interazione dovrebbe avvenire.
- **NON DATO:** nessuna misura di flusso NMD, nessun reporter PTC, nessun knockdown di UPF1, nessun contesto neuronale. La direzione della causalità non è testata in nessuno dei due sensi.
- 🔴 **La premessa che nessuno scrive:** *«l'efficienza dell'NMD è una costante dell'assay»*. È esattamente il tipo di default da manuale che la tabella `DEFAULTS THAT BIT US` esiste per intercettare. Se WWOX modula UPF1, **non è una costante: è una variabile che covaria con il genotipo che si sta studiando.**
- **Conseguenza 1 — sull'allele.** `DL-BIO-002` predice per `c.1057-2A>G` skipping dell'esone 9 → frameshift → PTC → NMD *oppure* proteina tronca. È una domanda di efficienza NMD. Una cellula WWOX-carente con meno UPF1 degraderebbe **meno** quel trascritto, producendo **più proteina tronca**, non più null — che è precisamente la biforcazione già aperta da `DL-MECH-045` (l'esone 9 è l'ultimo esone; l'allele non è un null silente).
- 🔴 **Conseguenza 2 — sull'assay, ed è qui che morde.** `DL-BIO-002` propone RT-PCR su fibroblasti donor-derived **± inibitore NMD (emetina/cicloeximide)**. Se lo stato WWOX modula l'NMD basale, il contrasto ±inibitore mette a confronto **due cellule con velocità di decadimento basali diverse**, e l'effetto dell'inibitore risulta confuso con il genotipo. Il rimedio va **disegnato dentro**, non scoperto dopo: un **reporter NMD** (β-globina PTC o dual-luciferase PTC/no-PTC) o un substrato NMD endogeno canonico (`GAS5`, `SRSF2`, target uORF di ATF4) misurato **nelle stesse cellule**, così che la capacità di NMD sia misurata invece che assunta uguale.
- **Belief:** alto sulla plausibilità dell'interazione (biochimica misurata da un laboratorio indipendente); **basso** su direzione e magnitudine dell'effetto sul flusso NMD (un'associazione trascrizionale in linee tumorali che sovraesprimono non dimostra nulla sul flusso); **alto** sul fatto che il controllo mancante vada aggiunto comunque — costa una piastra e chiude un confondente silenzioso.
- **Mappa ABC:** A=`allele PTC del genotipo di riferimento` · B=`efficienza NMD assunta costante fra genotipi` · C=`reporter NMD in parallelo, nelle stesse cellule`
- **Esperimento falsificante:** reporter PTC/no-PTC in fibroblasti donor-derived WWOX-WT vs WWOX-carenti (e nella coppia isogenica), ± knockdown di UPF1 come controllo positivo. Se il rapporto non si muove con lo stato WWOX, il confondente è chiuso e `DL-BIO-002` procede invariato.
- **Trasferibilità dichiarata (debole su tre assi):** genotipo — sovraespressione WT contro ipomorfo/null biallelico, direzione opposta; modello — linea tumorale immortalizzata contro fibroblasto donor-derived/organoide; stadio — tumore adulto contro finestra prenatale. Per questo il lead è scritto come **controllo da installare**, non come meccanismo da credere.
- **Interconnessioni:** [[discovery_ledger_current#DL-BIO-002 — Trascritto/proteina dell'allele di sito accettore, nominati dalla predizione di skipping esone 9 (SpliceAI/Pangolin)|DL-BIO-002]] · `DL-MECH-045` · `DL-MECH-055` · [[full_text_queue_current#FT-038]] · [[paper_registry_current#CORPUS-STUB-095]] · *CC-20260805-001*

#### DL-MECH-069b — Il 3′UTR di WWOX è un elemento regolato, e quindi una **scelta di progetto** in qualunque cassetta terapeutica

- **Status:** open · **Tag:** `DATO` (il sito esiste, predetto con coordinate) + `IPOTESI` (le conseguenze di design)
- **DATO/predizione:** sito **8mer** per miR-186-5p in posizione **637–644 del 3′UTR** di `WWOX` (`ENST00000566780`; posizione 2007–2014 dell'mRNA), context++ score −0,19 (TargetScan, Figura 7). La Tabella 1 dello stesso paper elenca **altri dieci** miRNA che bersagliano il 3′UTR di WWOX in contesti tumorali diversi (miR-134-5p, miR-214-3p, miR-153-3p, miR-24-3p, miR-187-5p, miR-670-5p, miR-625-3p, oltre alla famiglia miR-29 che agisce sul promotore via DNMT3).
- 🔑 **Implicazione di design:** qualunque costrutto di terapia genica o mRNA per WWOX compie una scelta sul 3′UTR, e la scelta non è neutra. Con il 3′UTR nativo il transgene eredita il sito 8mer e il resto della lista, quindi la resa diventa funzione del programma miRNA della cellula ricevente — che nel cervello è specifico per tipo cellulare e per finestra di sviluppo. Con un 3′UTR minimo o eterologo sfugge a quella regolazione, e insieme a qualunque tuning endogeno essa fornisca. **Va dichiarato esplicitamente in ogni ipotesi di delivery, non ereditato per default dal clone cDNA.** Tocca direttamente l'entrata «idrogel lentivirale intravescicale WWOX» del [[therapeutic_hypotheses_ledger_current]] e qualunque concetto AAV per il SNC.
- 🔴 **Perché un antagomiR NON è un candidato per questo genotipo:** togliere la repressione di miR-186-5p può alzare l'output solo di un allele che produce un mRNA con 3′UTR — cioè l'allele **missense**, il cui problema è che la proteina è instabile, non che l'mRNA sia scarso. Più trascritto di una proteina destabilizzata è più substrato di degradazione, non più funzione (`PROTEIN_STATE_IDENTITY_GATE`). L'allele null non guadagna nulla. Si conserva il lead perché la stessa logica varrebbe per un allele ipomorfo che produce proteina stabile ma scarsa — un'altra classe di genotipo.
- **Come biomarcatore:** al massimo `Tier 3`, e come sorgente di varianza. Se l'abbondanza di proteina WWOX viene usata come readout di un rescue, il programma miRNA della cellula saggiata è una varianza fra campioni oggi non misurata. **Misura un regolatore di WWOX, non WWOX.**
- **Interconnessioni:** `DL-MECH-054` · `DL-MECH-069` · [[therapeutic_hypotheses_ledger_current]] · [[full_text_queue_current#FT-037]]

**Next-search agenda:** `READ_NEXT` PMID 36499501 (`FT-037`) — miR-186-5p esosomiale e disfunzione NK in BLCA: è la referenza più vicina all'asse e **mancava da ogni file LEGEND**. Poi PMID 30619736 (`FT-038`), l'interattoma TAP-MS che fornisce l'arco WWOX·UPF1 su cui `DL-MECH-069` poggia: è citato come premessa e non è mai stato letto. Non mettere in coda gli altri contesti tumorali di LINC01137: senza un esperimento di perturbazione aggiungono coorti, non meccanismo.

**Riflessione di processo:** il valore di questa lettura è quasi tutto nelle **immagini** — undici dei fatti registrati non esistono nell'XML, che porta solo le didascalie. Le figure principali sono arrivate da `pmc.ncbi.nlm.nih.gov/articles/instance/<PMCID>/bin/`, il supplemento da `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC<ID>/supplementaryFiles`, che ha restituito in un solo zip il DOCX da 23 MB **e** tutte le figure, dopo che la rotta PMC `bin/` per il supplemento aveva risposto con un interstiziale JavaScript e l'API Frontiers con un 500. Quella rotta va promossa a **prima** opzione per i supplementi in `find-fulltext`, non a ultima.

---

### DL-MECH-070 — Il ponte WWOX–lipidi/traffico–mielina è una sintesi plausibile, non una catena causale dimostrata

- **Status:** open · **Tag:** `DATO` (espressione da dataset pubblici e primari citati) +
  `INFERENZA` (ponte integrativo) · **Fonte:** Aldaz & Hussain 2020, PMID 33255508 /
  PMCID PMC7727818 / DOI 10.3390/ijms21238922; full text, nove figure e due tabelle
  supplementari letti il 2026-08-06 (`FTR-20260806-33255508-01`). Dossier:
  `research/fulltext_dossiers/PMID33255508.md`.
- **Cosa mostra davvero:** la rianalisi di BrainRNAseq colloca Wwox più alto negli OPC che
  negli oligodendrociti maturi; i primari citati collegano separatamente WWOX a metabolismo
  lipidico e proteine di traffico endosoma/lisosoma. Nessun esperimento del paper perturba
  questi nodi in neuroni o oligodendrociti e nessuna mediazione della mielinizzazione è
  misurata.
- **Statement epistemico:** `WWOX -> {lipid homeostasis, endomembrane trafficking}` è
  supportato da primari esterni; `{lipid homeostasis, trafficking} -> myelin biogenesis` è
  biologia generale; quindi `WWOX -> myelination via those routes` resta `INFERENZA`.
- **Confronto col grafo:** non crea un claim. `CLAIM 003/004` e `DL-MECH-010/031` possiedono
  prove primarie più forti per un difetto mielinico non-cell-autonomo guidato dal neurone;
  `CLAIM 026/DL-MECH-018` porta l'interattoma cellulare, ma non il trasferimento neurale.
  L'espressione negli OPC non dimostra autonomia cellulare e non contraddice la genetica
  condizionale successiva.
- **Q230P:** la review conta otto casi in sei famiglie ma dichiara ignoto il meccanismo della
  maggior parte dei missense. La ricorrenza non autorizza né perdita catalitica né
  misfolding; il record resta subordinato ai dati funzionali primari già presenti nel grafo.
- **Esperimento discriminante:** in un modello neurale isogenico WWOX-loss/rescue, misurare
  in parallelo traffico SEC23IP/SCAMP3/VOPP1, lipidomica della linea oligodendrogliale e
  maturazione/mielina; una normalizzazione della mielina senza normalizzazione dei primi due
  falsifica la mediazione proposta.
- **Debito esplicito:** leggere PMID 24871327 (`FT-039`) e PMID 31340538 (`FT-040`) prima di
  usare il ponte come premessa; PMID 30290271 e 30619736 restano rispettivamente `FT-008` e
  `FT-038`. **Belief:** alto che il ponte sia una domanda ben motivata; basso che la via
  mediatrice sia già identificata.
- **Interconnessioni:** `CLAIM 003` · `CLAIM 004` · `CLAIM 005` · `CLAIM 026` ·
  `DL-MECH-010` · `DL-MECH-012` · `DL-MECH-018` · `DL-MECH-031` · `FT-039` · `FT-040`.

---

### DL-MECH-071 — Il ratto *lde* separa numero neuronale da maturazione neurite/mielina, ma non dimostra prenatalità, autonomia gliale o reversibilità

- **Status:** open · **Tag:** `DATO` (fenotipo PND5–21) + `INFERENZA` (dissociazione
  abbondanza/maturazione) + `CORREZIONE` (limiti dello stato precedente) · **Fonte:** Tochigi
  et al. 2019, PMID 31340538 / PMCID PMC6678113 / DOI 10.3390/ijms20143596; testo, sei
  figure e 56 riferimenti letti integralmente il 2026-08-06, receipt
  `FTR-20260806-31340538-01`; dossier `research/fulltext_dossiers/PMID31340538.md`.
- **DATO:** tra PND5 e PND21 il `lde/lde` non mostra differenze rilevate in conta NeuN,
  NeuN-WB o spessore corticale, ma mostra MAP2/processi neuritici ridotti, MBP/CNP ridotti e
  meno oligodendrociti maturi APC/CC1 a PND15–21. GFAP/Iba1 corticali sono ridotti, non
  attivati.
- **Correzione di perimetro:** “neuroni intatti” in `DL-MECH-027` significa soltanto
  **abbondanza NeuN e spessore misurati preservati**; neuriti, connettività e fisiologia non
  sono intatti. “Il substrato è salvabile” resta `IPOTESI`: nessun rescue o reversibilità è
  testato. Il paper non conta OPC (`NG2/PDGFRA/Olig2`) e quindi non dimostra arresto di
  maturazione. Non separa un effetto oligodendrocitario autonomo da malattia sistemica o
  segnalazione assone–glia.
- **Correzione temporale:** tutti i nuovi esperimenti sono PND5–21. Questo studio sostiene
  maturazione corticale/mielinica **postnatale precoce**, non è da solo un dato prenatale né
  una prova di migrazione/cortical layering. `CLAIM 014/015` dipendono per la prenatalità
  dagli altri studi della convergenza.
- **Tensione gliale:** gli autori dichiarano il contrasto con PMID 30290271: riduzione
  GFAP/Iba1 nella corteccia del ratto contro attivazione astro/microgliale nell'ippocampo del
  topo KO. La direzione gliale è regione/modello/stadio-dipendente finché un disegno
  comparativo non la risolve; non usare uno dei due segni come universale.
- **Genotipo:** la delezione esone 9 `c.1190_1202del/p.Leu371Thrfs*53` rende il ratto un
  comparator utile per il lato exon-9/null del genotipo di riferimento, non un modello di
  splicing correggibile e non un modello di Q230P. La bandina mutante è osservata; instabilità
  e assenza di funzione sono interpretazioni non misurate qui.
- **Qualità:** soli maschi, almeno `n=3+3` per età/esperimento, molti t-test senza correzione
  di molteplicità, nessun blinding/randomizzazione/power dichiarato, litter size ridotta per
  sopravvivenza. Effetti grandi e convergenti fra IHC/WB sostengono il fenotipo; precisione e
  causalità di linea cellulare restano limitate.
- **Esperimento discriminante:** confronto isogenico/condizionale con conta OPC, lineage
  tracing, g-ratio/EM e funzione di conduzione, più rescue neuronale versus oligodendrogliale.
  L'esito separa ritardo sistemico, segnale assone–glia e difetto gliale autonomo.
- **Debito:** `FT-041` (PMID 17803050, fenotipo originario del ratto) e `FT-042` (PMID
  19500159, mappatura causale/epilessia) prima di usare penetranza delle crisi o causalità
  genetica come dati letti. **Interconnessioni:** `DL-MECH-026` · `DL-MECH-027` ·
  `DL-MECH-031` · `CLAIM 014` · `CLAIM 015` · `CLAIM 032` · `FT-041` · `FT-042`.
### DL-MECH-072 — Il KO murino definisce vulnerabilità PV pan-ippocampale e NPY regionale, con reattività gliale, ma non misura GABA, E/I, morte interneuronale o causalità infiammazione→crisi
- **Status:** open · **Tag epistemico:** `DATO` + `INFERENZA`. Le etichette
  `CORREZIONE`, `TENSION` e `UNRESOLVED` sotto sono funzioni diagnostiche del ledger, non
  livelli epistemici aggiuntivi e non devono migrare come stati canonici.
- **Fonte:** Hussain et al. 2019, *Neurobiology of Disease* — PMID **30290271**,
  PMCID **PMC7104842**, DOI `10.1016/j.nbd.2018.09.026`; full text, sei figure,
  Table 1, entrambi i supplementi e 90 riferimenti letti integralmente; receipt
  `FTR-20260806-30290271-01`.
- **DATO — PV:** nel KO sistemico a due settimane i conteggi stereologici PV+ sono inferiori
  in DG (`p<.005`), CA1 (`p<.05`) e ippocampo intero (−44%, `p<.005`); CA3 non raggiunge
  significatività. `n=7/gruppo`.
- **DATO — NPY:** riduzione del 30% soltanto in DG (`p<.05`); CA1, CA3 e ippocampo intero
  non sono significativi. `n=6/gruppo`. La sintesi testuale degli autori è più larga dei
  pannelli quantitativi.
- **CORREZIONE — marker ≠ perdita cellulare:** PV+/NPY+ sono conteggi di cellule positive al
  marcatore. Senza lineage pan-GABA, fate mapping, apoptosi o birthdating non distinguono
  morte da downregulation del marcatore, cambio di destino o ritardo maturativo.
- **DATO — glia:** area fraction IBA1 e GFAP aumentata in CA1/CA3/ippocampo intero, DG
  marginale; la morfologia IBA1 è compatibile con reattività. Area fraction non è numero di
  cellule e non separa ipertrofia da iperplasia. Solo `Il6`, non `Tnf-a`, è significativo
  (`n=4/gruppo`).
- **TENSION:** PMID 31340538 misura nel ratto *lde* una riduzione corticale di GFAP/Iba1,
  segno opposto a questo ippocampo murino. Regione, specie, età, modello e stadio di malattia
  restano spiegazioni concorrenti; “WWOX loss causa gliosi” non è una direzione universale.
- **CORREZIONE — GABA/E-I:** il Western mostra meno GAD65/67 (`n=5/gruppo`), non GABA,
  flusso di sintesi, rilascio, gradiente del cloro, correnti sinaptiche o rapporto E/I. Il
  deficit inibitorio funzionale va attribuito al diverso studio elettrofisiologico, non
  retroproiettato qui.
- **DATO — RNA-seq:** neurosfere ippocampali neonatali coltivate, KO `n=2` versus WT `n=3`;
  283 DEG (184 up, 99 down), con singoli trascritti in entrambe le direzioni: `Kcna2`, `Grm3`,
  `Grin2b`, `Arx`, `Atp1a2`, `Grin2c` e `Wwox` down; `Gabbr2`, `Gabra2`, `Calb2` e `Htr3a`
  up. Con questo `n`, il dataset non stabilisce né il programma “epilessia” degli autori né
  un coerente contro-programma “misto”. Le categorie IPA sono annotazione/enrichment, non
  validazione causale; la validazione qPCR completa nelle neurosfere è `data not shown`. In
  vivo sono mostrati solo `Grin2c`, `Grm3` e `Kcna2` concordanti (`n=4/gruppo`).
- **UNRESOLVED — causalità:** nessun EEG, crisi, comportamento, rescue o KO condizionale.
  Gli autori stessi dichiarano irrisolto che l'infiammazione sia causa o conseguenza.
  `PREMISE IMPORTATA`: epileptogenesis e morte a circa tre settimane sono attribuite nel
  paper a Ludes-Meyers 2009 (PMID 19936220) e Mallaret 2014, non rimisurate qui. Finché
  `FT-043` non è letto, crisi precedenti/malattia terminale restano confondenti plausibili,
  non una base verificata per un rigetto canonico.
- **Transfer:** T2 per vulnerabilità conservata da perdita biallelica di WWOX; basso per
  residuo funzionale Q230P, allele splice-acceptor e strategia farmacologica. Il paper non
  testa farmaci e non autorizza una regola clinica “carico GABAergico forte = cautela”.
- **Esperimento discriminante:** KO neuronale/interneurone-condizionale e time course prima e
  dopo l'esordio, con lineage pan-GABA + PV/NPY, apoptosi, GABA misurato, patch clamp/EEG e
  quantificazione gliale per numero/morfologia; rescue temporizzato di Wwox per separare
  difetto primario da conseguenza di crisi/malattia.
- **Impatto sul grafo:** `PAPER 006`/`LIT-006` vanno normalizzati con PMID/PMCID/DOI e uniti
  append-only al duplicato `CORPUS-STUB-085`; `CLAIM 005` e il meta GABA devono preservare
  PV pan-ippocampale versus NPY DG-specifico ed essere privati dell'inferenza farmacologica
  non sostenuta. Correzioni isolate in
  `staging/commit_candidate_20260806_30290271.md`, in attesa di `BATCH_COMMIT`.
- **Multi-hop:** tutte le 90 referenze enumerate; 20 WWOX-/modello-/malattia-dirette. PMID
  **19936220**, primario per generazione del modello, non ha receipt ed è ora `FT-043`.
  PMID **19500159** resta `FT-042`. PMID **17470496** è solo lineage SCAR pre-gene, già
  documentato altrove e non load-bearing per gli endpoint di questo studio.
- **RISOLTO 2026-08-06 (parziale):** `FT-043` è stato letto integralmente
  (`FTR-20260806-19936220-01`). La premessa importata si spezza in due: la **morte precoce**
  è misurata di prima mano in PMID 19936220; l'**epilettogenesi non è misurata lì in nessuna
  forma**. Vedi `DL-MECH-073`. La causalità resta `UNRESOLVED`, ma il confondente sistemico
  è ora quantificato anziché plausibile: vedi `DL-MECH-074`.

### DL-MECH-073 — La catena "epilettogenesi" del KO murino non termina in un topo: attraversa PMID 19936220 e atterra nel ratto *lde*
- **Status:** open · **Tag epistemico:** `DATO` (assenza di misura, verificata) +
  `CORREZIONE` di attribuzione. `CORREZIONE` è una funzione diagnostica del ledger, non uno
  stato canonico.
- **Fonte:** Ludes-Meyers et al. 2009, *PLoS ONE* 4:e7775 — PMID **19936220**,
  PMCID **PMC2777388**, DOI `10.1371/journal.pone.0007775`; full text JATS, sei figure
  ispezionate come immagini, tre tabelle e 28 riferimenti letti integralmente; receipt
  `FTR-20260806-19936220-01`, manifest con 23 locator verbatim verificati.
- 🔴 **DATO — assenza di misura:** PMID 19936220 non contiene EEG, osservazione di crisi,
  test comportamentale, istologia cerebrale o esame neurologico. L'**unica** misura cerebrale
  dell'intero paper è il peso del cervello in Table 2. Le parole *seizure* ed *epilepsy*
  compaiono nel corpo una sola volta ciascuna, dentro una singola frase di Discussione che
  cita un **ratto** (referenza 26 = PMID 19500159). Le stringhe `EEG`, `hippocamp`, `GABA`,
  `convuls` e `behav` non compaiono affatto. Verificato con audit meccanico **dopo** la
  lettura, non al posto di essa.
- **DATO — l'altra metà regge:** la mortalità precoce è di prima mano e quantificata: 43%
  (15/35) morti a 72 h, 77% entro il giorno 17, nessuno oltre lo svezzamento; Figura 3B
  mostra un **arresto** della crescita (plateau a ~4 g dal giorno 10 al 17), non un
  rallentamento.
- 🔴 **CORREZIONE — doppio salto non dichiarato:** l'allele del ratto *lde* è una delezione
  di 13 bp nell'esone 9 → frameshift C-terminale (371–424aa), **non un null**, e le crisi
  citate sono **audiogene**. Trasferirle a un KO murino null attraversa specie *e* classe
  allelica senza che nessuna delle due transizioni sia mai stata scritta.
- 🔴 **CORREZIONE — driver Cre diverso:** PMID 19936220 usa **EIIA-Cre** (Jackson 003724),
  PMID 30290271 usa **BK5-Cre**. Condividono l'allele floxed, non il knockout. PMID 19936220
  è il primario per l'**allele**, solo parzialmente per il **modello**.
- 🔴 **PREMISE: DEFAULT_FROM_TEXTBOOK — ablazione nel cervello mai mostrata.** Il Western
  (Fig. 2C, identità dei tessuti visibile solo nel raster) copre **rene, polmone e milza**;
  l'IHC (Fig. 6) copre solo il rene. Nessun lisato cerebrale, in nessun punto del paper.
  "Una Cre zigotica delete ovunque" è attesa, non misura — ed è esattamente il tipo di
  premessa troppo ovvia per essere scritta che questo sistema obbliga a nominare.
- **Impatto sul grafo:** cinque superfici ripetono la stessa frase e vanno **spezzate**, non
  cancellate: `CLAIM 005` (evidence boundary), changelog `WM_v4.0`, dossier PMID 30290271,
  session evaluation 2026-08-06, e `DL-MECH-072` sopra. Morte precoce → confermata di prima
  mano; epilettogenesi → non in questo paper.
- **Debito:** `FT-042` (PMID 19500159) e `FT-041` (PMID 17803050) passano da "primari del
  modello ratto" a **terminale effettivo di una premessa oggi attribuita a un paper murino**.
  Nessun nuovo debito aperto: 22 delle 28 referenze sono già nello stato strutturato e le
  due che contano erano già in coda.
- **Esperimento discriminante:** nessuno serve per questa correzione — è una questione di
  attribuzione, risolvibile solo leggendo `FT-042`/`FT-041`. **Interconnessioni:**
  `DL-MECH-072` · `DL-MECH-074` · `CLAIM 005` · `FT-041` · `FT-042` · `FT-043`.

### DL-MECH-074 — Il null sistemico di Wwox a 2–3 settimane è un animale metabolicamente scompensato: il confondente non è plausibile, è misurato
- **Status:** open · **Tag epistemico:** `DATO` (le misure) + `INFERENZA` (la portata come
  confondente).
- **Fonte:** PMID **19936220**, Table 2, Table 3 e Figure 4/6; receipt
  `FTR-20260806-19936220-01`.
- **DATO — crisi metabolica sistemica a P18:** glucosio 143.5 vs 250.6 mg/dL (`p=0.000131`);
  bicarbonato totale 14.50±3.5 vs 21.67 mEq/L (`p=0.006227`); BUN 37.25 vs 17.67 mg/dL
  (`p=0.01086`); calcio 10.18 vs 11.13 mg/dL (`p=0.000385`); WBC 4.2 vs 9.45 ×10³/µL
  (`n=2/gruppo`, non testato); 3% di eritrociti nucleati in 1 KO su 2. Più atrofia splenica
  (0.21% vs 0.53% del peso corporeo, `p=0.0015`) con ipocellularità della polpa rossa e
  corticale timica assottigliata.
- **INFERENZA — perché conta oltre questo paper:** ipoglicemia e acidosi metabolica alterano
  di per sé espressione dei marcatori interneuronali, reattività gliale e soglia convulsiva.
  Qualunque fenotipo ippocampale misurato in un null **sistemico** a 2–3 settimane è misurato
  in un animale simultaneamente ipoglicemico, acidotico, uremico e anemico. Questo non
  confuta quei fenotipi: rende **impossibile per design** separare la perdita neuronale
  cell-autonoma di Wwox dal danno metabolico secondario. È esattamente il divario che
  l'allele condizionale generato in questo paper è stato costruito per chiudere.
- 🔴 **CORREZIONE — peso del cervello letto al contrario:** Table 2 dà assoluto 0.390 → 0.356 g
  (−8.7%) e relativo 5.0% → **8.5%** del peso corporeo (`p=0.0003`). La significatività è sul
  **relativo** ed è guidata dal denominatore crollato. È **brain sparing** in cachessia, non
  crescita cerebrale. Importare "increased brain weight in KO mice" senza il rapporto inverte
  la biologia.
- **DATO — l'ipotesi degli autori, e cosa ne è stato:** il paper propone l'acidosi tubulare
  renale come causa di morte (`we hypothesize`, `we speculate`), sostenuta dall'espressione
  di Wwox nei tubuli contorti distali (Fig. 6). Densità di campo misurata 2026-08-06: la query
  `WWOX AND ("metabolic acidosis" OR "renal tubular acidosis")` restituisce **esattamente un
  record — questo paper**. `WWOX AND hematopoiesis` → 3 (uno è questo); `WWOX AND "bone
  mineralization"` → 1 (questo). `WWOX AND osteosarcoma` → 28. In diciassette anni nessuno,
  autori compresi, ha testato il meccanismo che il paper propone per la letalità.
- **TENSION — osteosarcoma, conflitto esplicito e irrisolto:** 9 KO per necroscopia completa,
  raggi X, istopatologia multiorgano e microCT → **zero** lesioni neoplastiche. Aqeilan 2007
  (PMID 17360458) riporta 4/13 (31%) con lesioni periostali compatibili con osteosarcoma.
  Secondo conflitto: attività osteoclastica superiore in Aqeilan **senza quantificazione**,
  nessuna differenza qui **con** quantificazione. Gli autori chiudono con *"The reason(s) for
  the discrepancies between studies remain to be determined."* → `conflicting evidence`, non
  biologia risolta.
- **Esperimento discriminante:** delezione condizionale ristretta al sistema nervoso con
  l'allele `Wwox^flox` già validato qui, con chimica del sangue misurata in parallelo, per
  separare Wwox neuronale cell-autonomo da acidosi/ipoglicemia sistemica. Il reagente esiste
  dal 2009 e, per le densità sopra, è largamente inutilizzato in questa direzione.
- **Interconnessioni:** `DL-MECH-072` · `DL-MECH-073` · `CLAIM 005` · `FT-043`.

### DL-MECH-075 — La catena non finisce in assenza di prova: finisce in una prova contraria. Il terminale dichiara che i topi Wwox-null NON hanno epilessia
- **Status:** open · **Tag epistemico:** `DATO` (come resoconto della letteratura fatto dal
  terminale) + `CORREZIONE` di attribuzione.
- **Fonte:** Suzuki et al. 2009, *Genes Brain Behav* 8:650–660 — PMID **19500159**, DOI
  `10.1111/j.1601-183X.2009.00502.x`, nessun PMCID; undici pagine, otto figure, due tabelle e
  referenze lette integralmente; receipt `FTR-20260806-19500159-01`, manifest con 30 locator
  verificati. Full text ottenuto dall'operatore per via istituzionale dopo il rifiuto di otto
  tier automatici.
- 🔴 **DATO — il terminale afferma l'opposto della premessa, quattro volte:** *"Although
  neither epileptic seizures nor abnormal behavior has been reported in Wwox KO (knockout)
  mice"* (Introduzione); *"neither abnormal behavior nor impaired motor skill was observed in
  the Wwox KO mice … lde/lde rats show ataxic gait and spontaneous epileptic seizures"*
  (Discussione); *"the reason for no detection of spontaneous epilepsy in the KO mice is
  unknown … the KO mice may die before they experience epileptic seizure"* (Discussione); e
  **Table 2**, dove la riga *Epilepsy* è compilata **solo** per `lde/lde` ed è vuota per
  entrambi i modelli murini.
- **Catena completa, ora chiusa:** PMID 30290271 *"this model develops epileptogenesis"* →
  cita PMID 19936220, che **non lo misura** → cita PMID 19500159, che **lo nega per il topo**.
  Due salti di citazione hanno trasformato un negativo esplicito su un **ratto** in
  un'asserzione positiva su un **topo**.
- **DATO — il fenotipo del ratto è invece solido:** 19/20 (95%) con almeno una crisi
  audiogena su tre prove; 30/50 (60%) crisi spontanee nella progenie backcross; 0/14 nei
  controlli normali; latenza che si accorcia 56±24 → 36±4 → 25±3 s (progressione
  kindling-like); spike interictali ~10 Hz in **tutti** i mutanti non stimolati, occipitali >
  frontali, assenti nei normali (`n=5`); vacuoli extracellulari nell'ippocampo di 9/9 affetti
  e nell'amigdala di 6, contro 0/10 normali.
- 🔴 **Restrizione visibile solo nella figura:** la didascalia della Fig. 6 specifica *"21- to
  33-day-old lde/lde **females**"*. Il 95% di titolo è una coorte **solo femminile**. Né i
  Results né l'abstract lo dicono.
- 🔴 **Didascalia della Fig. 1 sbagliata:** il titolo assegna normal a (a, b) e affetti a
  (c, d); l'immagine mostra a e c puliti, b e d vacuolati. Chi legge la didascalia senza
  guardare l'immagine inverte quale ippocampo è malato. È esattamente la classe di difetto per
  cui esiste il valore di copertura `captions_only`.
- **CORREZIONE — classe allelica, precisata:** avevo registrato da PMID 19936220 che l'allele
  del ratto è "un frameshift C-terminale, **non un null**". Fedele alla descrizione di
  Ludes-Meyers, ma incompleto. Qui è misurato: mRNA **normale** (Fig. 4), proteina **assente**
  — né 47 né 42 kDa in testicolo e ippocampo `lde/lde` (Fig. 5) — con il controllo che rende
  la conclusione ammissibile: *"The Wwox epitope bound by the anti-Wwox antibody used in this
  study did not contain the region altered by the lde mutation"*. Verbatim degli autori: *"the
  13-bp deletion in exon 9 of the Wwox gene is a **functional null mutation**"*.
  **Formulazione corretta:** strutturalmente frameshift C-terminale, funzionalmente null a
  livello proteico nei due tessuti saggiati. Le due metà viaggiano insieme.
- 🔴 **PREMISE: DEFAULT_FROM_TEXTBOOK nel terminale stesso:** *"may lead to the aberrant
  conformation of them, **as degenerated by ubiquitin proteasome system**"*. Nessun saggio di
  turnover, nessun inibitore, nessuna determinazione di via in tutto il paper. È lo stesso
  default "misfolded → proteasoma" che il caso del 2026-07-12 ha già falsificato per un altro
  allele WWOX, dove il turnover passava per una via lisosomiale HSC70-associata e non
  rispondeva a MG-132. **`REVIVAL_TRIGGER`:** un chase con cicloesimide più inibitori
  proteasomali versus lisosomiali/CMA sulla proteina lde chiude la questione.
- **DATO — differenza di sopravvivenza:** Table 2 dà 2–3 settimane per il KO murino contro
  **3–12 settimane** per `lde/lde`. È la base materiale della spiegazione degli autori — i
  topi potrebbero morire prima di poter convulsionare — **testabile e mai testata in
  diciassette anni**.
- **Densità di campo:** `Wwox AND audiogenic` → **2 record**; `Wwox AND "lethal dwarfism"` →
  **2**. In entrambi i casi la coppia è questo paper e `FT-041`, dallo stesso laboratorio,
  **mai replicati indipendentemente**. Nota a favore: il laboratorio non è un gruppo WWOX (43
  record, 2 su Wwox) e il fenotipo epilettico fu osservato **prima** che il gene fosse noto,
  quindi non può essere un gruppo WWOX-motivato che trova un risultato WWOX-forma.
- **Esperimento discriminante:** EEG longitudinale in topi Wwox-null **prima** della morte,
  con stimolazione audiogena, per distinguere "il topo non convulsiona" da "il topo muore
  prima di convulsionare". Il reagente condizionale di PMID 19936220 permette inoltre di
  prolungare la sopravvivenza deletendo solo nel sistema nervoso.
- **Interconnessioni:** `DL-MECH-072` · `DL-MECH-073` · `DL-MECH-076` · `CLAIM 005` ·
  `FT-041` · `FT-042` · `FT-043`.

### DL-MECH-076 — "Clearly excluded": l'esclusione della causa metabolica sistemica nel ratto poggia su una fonte non letta il cui abstract la contraddice in parte
- **Status:** open · **Tag epistemico:** `INFERENZA` contestata. **Non risolvibile senza
  `FT-041`.**
- **Fonti:** PMID **19500159** (letto, `FTR-20260806-19500159-01`) e PMID **17803050**
  (`FT-041`, **NON letto** — il 2026-08-06 l'operatore ne ha fornito il **solo abstract**).
- **Il contesto:** il 2026-08-06 `DL-MECH-074` ha stabilito, da PMID 19936220, che il null
  **murino** sistemico a P18 è metabolicamente scompensato — ipoglicemia, acidosi, uremia,
  ipocalcemia, leucopenia, anemia — un confondente misurato per qualunque fenotipo cerebrale
  in quella finestra.
- **L'affermazione del ratto:** PMID 19500159 sembra dissociare l'asse: *"By contrast,
  28-day-old lde/lde rats had normal levels of these constituents"* e, in modo decisivo,
  *"**Normal levels of serum constituents clearly excluded the possibility** that these
  abnormal excitabilities are resulted from a systemic metabolic disorder"*. Se reggesse, i
  due roditori formerebbero una dissociazione naturale pulita: **crisi senza crisi metabolica**
  (ratto) contro **crisi metabolica senza crisi** (topo).
- 🔴 **La tensione:** l'intera affermazione è citata a `FT-041`, non letto. Il suo abstract
  riporta che i ratti mutanti *"had significantly increased concentrations of plasma **urea
  nitrogen, creatinine, and inorganic phosphate**"*. Non sono costituenti sierici normali: è
  una **firma di compromissione renale** — la stessa misurata nel topo null (BUN 37.25 vs
  17.67 mg/dL) e la stessa che Ludes-Meyers 2009 annotava esplicitamente come *coerente tra le
  due specie*.
- **Precisione necessaria:** le due affermazioni non sono strettamente contraddittorie —
  l'elenco del 2009 è proteine/glucosio/colesterolo/elettroliti/calcio, mentre le anomalie del
  2007 sono BUN/creatinina/fosfato. **Ma "clearly excluded" fa un lavoro che la sua stessa
  fonte non autorizza.** Un ratto con urea e creatinina elevate ha una derangement sistemica;
  se basti a guidare l'ipereccitabilità è una domanda aperta, non esclusa.
- **Convergenza che rafforza il segnale renale:** firma renale nel topo (`DL-MECH-074`,
  misurata), nel ratto (abstract di `FT-041`), e notata come conservata da Ludes-Meyers. La
  query `WWOX AND ("metabolic acidosis" OR "renal tubular acidosis")` restituisce **un solo
  record** e nessuno ha mai testato l'ipotesi. Il rene continua a comparire e nessuno lo
  guarda.
- **Un abstract non è una lettura.** Questa voce registra la tensione, non la risolve, e non
  cancella il debito di `FT-041`.
- **Esperimento discriminante / azione:** ottenere `FT-041` e leggere la sua tabella di
  chimica ematica. È la singola azione con il rapporto valore/costo più alto oggi disponibile.
- **Interconnessioni:** `DL-MECH-073` · `DL-MECH-074` · `DL-MECH-075` · `FT-041` · `FT-042`.
- **RISOLTO 2026-08-06:** `FT-041` letto integralmente (`FTR-20260806-17803050-01`). Verdetto
  diviso: il **contrasto specifico** con il topo è confermato (glucosio, calcio, elettroliti
  normali nel ratto), ma **"clearly excluded" è sovradimensionato** — BUN ~3.2–3.5× e
  creatinina significativamente aumentati. Vedi `DL-MECH-077`. E una seconda affermazione di
  `FT-042` è **refutata dalla sua stessa fonte**: vedi `DL-MECH-078`.

### DL-MECH-077 — Il ratto è uremico senza essere ipoglicemico: il confondente non si esclude, si sposta — e gli autori offrono una spiegazione che nessuno ha mai testato
- **Status:** open · **Tag epistemico:** `DATO` (le misure) + `IPOTESI` (le due spiegazioni
  concorrenti).
- **Fonte:** Suzuki, Takenaka, Suzuki 2007, *Comparative Medicine* 57(4):360–369 — PMID
  **17803050**, **nessun DOI, nessun PMCID**; dieci pagine, sei figure, tre tabelle e 35
  referenze lette integralmente; receipt `FTR-20260806-17803050-01`, manifest con 32 locator
  verificati. Full text ottenuto dall'operatore dopo il rifiuto di ogni aggregatore.
- **DATO — Table 2, `n=4` normali e `5` mutanti per sesso:** BUN 12.6 → **40.3** mg/ml (♀,
  `P<0.05`) e 10.1 → **35.6** (♂, `P<0.01`); creatinina 0.48 → **0.64** (♀, `P<0.01`) e 0.45 →
  **0.58** (♂, `P<0.01`); fosfato inorganico significativo solo nelle femmine. **Glucosio,
  calcio, Na⁺, K⁺, Cl⁻ e trigliceridi: tutti non significativi.**
- **VERDETTO sulla tensione di `DL-MECH-076`, diviso:** il **contrasto specifico** che
  `FT-042` traccia col topo è **confermato** — il ratto non ha ipoglicemia, ipocalcemia né
  squilibrio elettrolitico, che sono invece il profilo del null murino. Ma la frase
  *"**Normal levels of serum constituents** clearly excluded the possibility that these
  abnormal excitabilities are resulted from a systemic metabolic disorder"* è **falsa come
  affermazione generale**: BUN triplo e creatinina elevata non sono livelli normali. Il ratto
  è **uremico senza essere ipoglicemico**. Il confondente sistemico non è escluso: è di natura
  diversa da quella del topo.
- 🔴 **IPOTESI CONCORRENTE MAI TESTATA — la scoperta che questa lettura porta:** gli autori
  scrivono *"Alternatively, the increases in plasma BUN and CRE may be related to the
  **increased production** of these compounds"* e *"the production of urea-nitrogen and
  creatinine may be increased due to **hypercatabolism and muscle disruption**"*, con
  precedente nominato: il ceppo **SER** ha BUN elevato insieme a ritardo di crescita e crisi
  motorie. **Questo compete direttamente con l'ipotesi di acidosi tubulare renale che PMID
  19936220 ha costruito per il topo sullo stesso marcatore** — e quel paper non l'ha mai
  considerata. Un animale con convulsioni tonico-cloniche ripetute, gravemente cachettico e
  atassico ha una via non renale ovvia verso urea e creatinina alte.
- **DATO — i tre negativi che complicano la lettura renale:** *"we could not find any
  pathologic alteration in their kidneys"*; *"urostick tests and blood examinations did not
  identify any manifestations of proteinuria and anemia"*; e la cautela degli autori *"if
  renal excretive function is reduced in the mutant rats, the degree of dysfunction may not be
  severe"*. Da confrontare col topo, dove PMID 19936220 trovò invece anemia (3% NRBC in 1 di 2).
- **Densità di campo 2026-08-06:** `WWOX AND ("blood urea nitrogen" OR creatinine)` → **1**
  record. `WWOX AND (hypercatabolism OR "muscle disruption")` → **0**. Il BUN elevato è ora
  documentato di prima mano in **tre** luoghi — topo null, questo ratto, e la citazione
  incrociata fra i due — con **tre spiegazioni implicite diverse e zero follow-up**.
- **Esperimento discriminante:** gli autori lo nominano e spiegano perché non l'hanno fatto —
  test di clearance renale, impraticabile perché nanismo e letalità rendono difficile
  raccogliere urina. Nel topo servirebbe in parallelo creatina-chinasi e massa muscolare per
  separare le due vie.
- **Interconnessioni:** `DL-MECH-074` · `DL-MECH-076` · `DL-MECH-078` · `FT-041` · `FT-042`.

### DL-MECH-078 — Un abstract che sovradichiara il proprio corpo, e la citazione che ci si è appoggiata: il nanismo *lde* NON è spiegato dal GH
- **Status:** open · **Tag epistemico:** `CORREZIONE` di attribuzione su un `DATO` negativo.
- **Fonti:** PMID **17803050** (letto) e PMID **19500159** (letto, `FTR-20260806-19500159-01`).
- 🔴 **La catena, terza istanza in un giorno:** PMID 19500159 scrive *"The cause of severe
  dwarfism with retarded bone growth in lde/lde rats may be related, at least in part, to
  **lower levels of pituitary growth hormone** (Suzuki et al. 2007)"*. Ma PMID 17803050 —
  la fonte citata — dice il contrario nel corpo: *"although the plasma GH level was slightly
  lower in mutant than in normal rats, **the difference was not significant**"*, e conclude
  *"suggesting that the severe type of dwarfism observed in lde/lde rats **cannot be explained
  solely by low levels of plasma GH**"*. Le cellule GH-positive sono presenti e il GH ha peso
  molecolare normale.
- 🔴 **Da dove nasce l'errore — ed è il punto:** l'**abstract** di PMID 17803050 scrive *"as
  well as decreased concentrations of plasma growth hormone"*, **senza qualificazione**,
  mentre il corpo la dichiara non significativa. **L'abstract sovradichiara il proprio corpo**,
  e il paper del 2009 ha citato la versione dell'abstract. Verificato meccanicamente: quella
  frase risolve sulla superficie *abstract* e non sul *body* dell'artefatto.
- **Perché conta per il metodo, non solo per il fatto:** il 2026-08-06 l'operatore ha fornito
  esattamente quell'abstract e la sessione ha rifiutato di trattarlo come lettura. Se lo avesse
  accettato, **"GH ridotto" sarebbe entrato nel modello come dato, e non lo è.** È la
  dimostrazione più pulita possibile della regola *un abstract non è una lettura*, e la terza
  istanza in giornata di `IMPORTED_PREMISE_ATTRIBUTION_GATE` — la prima in cui la
  sovradichiarazione nasce **dentro l'abstract della fonte** anziché nel paper citante.
- **DATO — cosa resta non spiegato:** il nanismo *lde* non ha causa nota. Non è GH, non è
  recettore del GH (gli autori argomentano che un GH plasmatico non elevato esclude il modello
  Laron), e la crescita cerebrale relativa raddoppiata è dichiarata GH-indipendente. Densità di
  campo: `WWOX AND "growth hormone"` → **0** record.
- **DATO collaterale — l'atassia:** 95% dei mutanti, 0% dei normali, e **non cerebellare**
  (*"we did not detect any marked pathologic changes in the cerebella"*). È il fenotipo più
  penetrante dell'intero modello *lde*, più delle crisi (34%), e la letteratura a valle non lo
  porta affatto.
- **Interconnessioni:** `DL-MECH-075` · `DL-MECH-076` · `DL-MECH-077` · `FT-041` · `FT-042`.

### DL-METH-079 — Un **titolo** che afferma il contrario del proprio paper, e viaggia più lontano di qualunque altra superficie
- **Status:** open · **Tag epistemico:** `CORREZIONE` di attribuzione a livello di **titolo**, non di claim.
- **Fonte:** PMID **38182577** (Akkawi 2024, *Cell Death Dis*; letto integralmente, `FTR-20260810-38182577-01`, manifest strict PASS 22 locator).
- 🔴 **Il fatto:** il titolo pubblicato è *"WWOX **promotes** osteosarcoma development via **upregulation** of Myc"*. Letto alla lettera afferma che WWOX promuove il tumore e alza MYC. Il paper dimostra l'opposto su **tre** superfici concordi: il corpo (*"depletion of WWOX results in Myc upregulation as an early event"*), la didascalia della propria Figura 6 (*"WWOX expression is inversely correlated with c-Myc in OS"*) e l'**abstract**, che è corretto e coerente. La lettura intesa è *"WWOX **[loss]** promotes…"*. L'errata PMID 38355659 corregge un nome d'autore e **non tocca il titolo**.
- 🔴 **Perché è un reperto di metodo e non di biologia:** il titolo è l'artefatto che viaggia più lontano. Sta in PubMed, nel TSV `NOT_EVIDENCE` del corpus, nelle liste di citazione, e **stava nella tabella di triage consegnata dalla sessione fornitore il 2026-08-10** come "WWOX promuove l'osteosarcoma via Myc". Un modello costruito leggendo titoli registra **WWOX come oncogene nell'osso** — cioè l'inverso della sua funzione. È la dimostrazione concreta della **regola 4** (`grep`/keyword vietati come metodo d'analisi) e del perché il corpus di abstract è `NOT_EVIDENCE`: qui nemmeno l'abstract sbaglia, sbaglia solo il titolo, e nessuna quantità di triage sui metadati poteva accorgersene.
- **DATO — la direzione, che è quella giusta:** WWOX↓ → MYC↑, misurata in quattro modi indipendenti nel paper (RNA-seq DKO vs SKO; qPCR; ChIP-Seq di MYC sui promotori; e correlazione inversa WWOX/MYC in osteosarcoma umano TCGA TARGET GTEx, P<0,001). **Stessa direzione** di PMID 29724996 nel fegato, letto lo stesso giorno. **Nessun conflitto cross-tissue: WWOX sopprime MYC in entrambi i tessuti.**
- ⚠️ **Limite da portare con il dato:** la "restoration" di WWOX in Fig 6G è una **sovraespressione 9×** che porta MYC a 0,4, cioè *sotto* la baseline SKO; e il divario proteico DKO/SKO è **1,4×** contro **4,7×** di mRNA, non riconciliato dal paper. Il livello fisiologico di WWOX non è stato testato.
- **REVIVAL_TRIGGER per la classe di errore:** ogni volta che una sessione ordina o cita un paper del corpus **a partire dal titolo**, quel titolo va considerato non verificato finché il corpo non è aperto. Un titolo non è un abstract e non è una lettura.
- **Interconnessioni:** `DL-MECH-078` · `IMPORTED_PREMISE_ATTRIBUTION_GATE` · regola 4 in [[gold_is_in_the_details]].

### DL-THER-080 — Simvastatina→MCM7 in osteosarcoma *Wwox/Trp53*-null: seme di repurposing, con i suoi limiti attaccati
- **Status:** open · **Tag epistemico:** `IPOTESI` / seme di repurposing. **Non** un candidato terapeutico.
- **Fonte:** PMID **38182577**, Figura 7 (ispezionata a 1975 px).
- **DATO in vivo:** simvastatina 60 mg/kg per gavage, 10 giorni, su tumori da iniezione di yBM DKO in NOD/SCID: dimensione da ~0,42 a ~0,21 cm³ (`****`), peso da ~0,71 a ~0,55 g (`***`), MCM7 all'IHC da ~0,43 a ~0,30 (`**`).
- ⚠️ **Tre limiti che il testo non porta, e che il pannello sì:**
  1. la selettività dichiarata è smentita dalla figura stessa — il testo scrive *"did not affect control BM cells"*, ma in Fig 7C la vitalità del midollo di controllo scende da ~1,05 a ~0,73 a 40 µM: **effetto ridotto, non assente**;
  2. il trattamento abbassa **sia MCM7 sia c-Myc** (Fig 7B), quindi l'esperimento non separa i due bersagli;
  3. la maggiore sensibilità del DKO rispetto al SKO (Fig 7E) è affermata **senza alcun test statistico nel pannello** e su due repliche biologiche per gruppo.
- 🔴 **Perché NON entra in BLOCK-1 oggi:** il bersaglio è MCM7 nell'osso; non esiste in questo paper alcun razionale CNS, nessuna misura di penetrazione della barriera, nessun legame con un genotipo WWOX-DEE. Promuoverlo richiederebbe che la direzione WWOX→MYC sia stabilita *nel cervello* e che il MYC neuronale sia un bersaglio con un readout prossimale — nessuna delle due condizioni è soddisfatta.
- **Interconnessioni:** `DL-METH-079` · PMID **29724996** (asse WWOX–proliferazione, `c-Myc` soppresso nel fegato).

### DL-METH-081 — **Le superfici-titolo si invertono, la scienza no**: seconda occorrenza consecutiva, e adesso è una classe
- **Status:** open · **Tag epistemico:** `CORREZIONE` di attribuzione a livello di **superficie**, mai di dato.
- **Fonti:** PMID **38182577** (`DL-METH-079`) e PMID **38499540** (letto, `FTR-20260810-38499540-01`), stesso laboratorio, consecutivi.
- 🔴 **Il pattern:** in entrambi i paper il **corpo**, i titoli di sezione dei Risultati e — dove esiste — l'**abstract grafico** sono corretti e concordi. A invertirsi è la superficie che fa da titolo:
  - `38182577`: il **titolo dell'articolo** dice *«WWOX promotes osteosarcoma development via upregulation of Myc»* mentre il paper dimostra che è la **perdita** di WWOX ad alzare MYC;
  - `38499540`: **tre didascalie di figura su sei**. Fig 2 dice *«redirects the DSB repair to NHEJ»* e il pannello mostra 53BP1 (NHEJ) che **scende** da ~0,123 a ~0,027 (`***`) e RAD51 (HDR) che **sale** da ~0,008 a ~0,052 (`***`). Fig 4 e Fig 5 dicono *«Loss of WWOX…»* su esperimenti di **sovraespressione**, con i pannelli etichettati `EV` vs `WWOX OE` — e la didascalia della Fig 4 si smentisce da sola **undici parole dopo**, scrivendo *«with EV (left) or WWOX OE (right)»*.
- 🔴 **Perché è un reperto di sistema e non di due paper:** un curatore automatico che ingerisce **titoli e didascalie prima del corpo** — cioè il comportamento normale di un estrattore — registrerebbe su questi due lavori **l'esatto contrario di ciò che dimostrano**. È la dimostrazione più concreta disponibile del perché serve il source-lock verso DisMech, e del perché la **regola 4** vieta grep e keyword come metodo d'analisi. Nessuna quantità di triage sui metadati poteva accorgersene: qui nemmeno gli abstract sbagliano.
- **DATO di 38499540, direzione corretta:** WWOX presente → NHEJ; WWOX perso → NHEJ compromesso e più HDR. Misurato in vivo (Fig 2A/B) e in vitro (Fig 5E: 53BP1 sale nell'OE, `****`).
- ⚠️ **Tre limiti che il testo non dichiara:** il reporter SeeSaw **non fa see-saw** — l'HDR sta allo 0,03–0,83% degli eventi, quindi il nullo sull'HDR poggia su una misura al pavimento e solo il NHEJ si muove; il braccio di controllo della sopravvivenza (Fig 1B) porta **due sole marche di censura** e nessun *n* stampato; e il corpo afferma che il danno al DNA non varia mentre Fig 5C stampa `**` **due volte** proprio nella linea dove gli effetti sono massimi.
- **REVIVAL_TRIGGER:** se un terzo paper dello stesso gruppo mostra la stessa inversione, non è più una classe di errore editoriale ma un problema di produzione da segnalare alla Fondazione, che finanzia il laboratorio.
- **Interconnessioni:** `DL-METH-079` · regola 4 in [[gold_is_in_the_details]] · spec di export/source-lock.

### DL-METH-082 — **Una coppia è una contraddizione solo se il pannello che falsifica è quello che la frase cita**
- **Status:** open · **Tag epistemico:** `CORREZIONE` di metodo, applicata retroattivamente a tre manifest già validati.
- **Origine:** regola proposta da A e verificata dall'orchestratore nell'XML; audit eseguito il 2026-08-10 su tutte le **14 coppie** `text_contradicted_by_panel` esistenti nei manifest di questa sessione (`PMID29724996` 6, `PMID38182577` 4, `PMID38499540` 4).
- 🔴 **La regola:** una coppia testo↔pannello afferma che *il paper si contraddice*. Quell'affermazione regge solo se il pannello che falsifica è **quello che la frase stessa cita**. Se il lettore ha scelto un altro pannello, l'asimmetria si rovescia: non è la frase smentita dalla propria evidenza, è **un'altra evidenza che la qualifica** — relazione più debole, e da dichiarare come tale. Operativamente: lo snippet del bersaglio è **esteso fino a contenere la citazione dell'autore**, così il collegamento frase→pannello diventa un'asserzione della fonte e non del lettore; ogni entry-pannello porta un `cited_panel_check` che dice se il pannello letto è quello citato.
- **Esito dell'audit — 12 su 14 passano, 2 declassate.** Le due che non passano sono entrambe in `38182577`, ed è la seconda volta in due giorni che il supplement e poi l'audit correggono le mie coppie sullo stesso paper:
  - la frase *«significant reduction in Myc levels upon WWOX restoration»* cita **Fig 6D**, io avevo usato **Fig 6G**;
  - la frase *«low expression of Myc and its targets in SKO yBM»* cita **Fig 6A, B**, io avevo usato **Fig 6C**.
  Nessuna delle due è stata **ri-puntata**: ri-puntare avrebbe fatto sembrare sane le coppie e cancellato il disallineamento, che è esso stesso il reperto. Sono state declassate a `panel_qualifies_text` con puntatore `qualifies`, campo coniato in anticipo sulla spec esattamente come `panel_text_relation`.
- 🔴 **Reperto nuovo emerso dall'audit — la citazione di `38182577` punta a un pannello che non contiene l'esperimento.** La frase riporta l'effetto della **ri-espressione di WWOX** su Myc e cita Fig 6D. Fig 6D, per **propria didascalia** (*«D mRNA levels of Myc target genes in DKO and SKO yBM cells»*) e per **propri pixel** (cinque grafici, due sole categorie sull'asse x, `SKO-yBM` e `DKO-yBM`, nessuna corsia `EV`/`OE`), **non contiene alcun braccio di sovraespressione** — e il suo c-Myc va nella direzione **opposta** alla frase, `~4,7×` in **salita** nel doppio knockout (`****`). L'unico pannello con una corsia WWOX OE è **6G**, che la frase non cita. Terza superficie difettosa nello stesso articolo dopo il titolo invertito (`DL-METH-079`): **titolo, e ora puntatore interno**. Il corpo, di nuovo, resta corretto.
- ⚠️ **Errore mio, dichiarato:** sulla frase *«low expression of Myc… in SKO yBM»* il mio snippet si fermava **prima del comparatore dell'autore** — *«as compared to those in DKO cells»*. Tolto il comparatore, una frase **relativa** sembra assoluta, e la coppia che ci poggiava sopra era una mia costruzione, non un errore del paper. È la stessa forma della calibrazione Iatan segnalata dall'operatore: **una citazione che perde il qualificatore diventa un'affermazione diversa.** Lo snippet ora arriva fino alla citazione.
- **Sesta coppia di `29724996`, tenuta ma etichettata debole:** *«it continued rising in Wwox ΔHep mice»* **non cita alcuna figura**; la citazione `(Fig. 7a, b )` appartiene alla frase precedente. L'eredità è dichiarata su entrambi i membri invece di restare invisibile. Debole e dichiarata, non scartata.
- **REVIVAL_TRIGGER:** se il validator adotta `panel_qualifies_text`, le due coppie declassate vanno rilette per stabilire se il disallineamento è un errore di citazione dell'autore (`6D`: dimostrato) o una scelta del lettore (`6C`: sì).
- **Interconnessioni:** `DL-METH-079` · `DL-METH-081` · `PATTERN_ALREADY_SOLVED_GATE` — l'invariante `surface: figure`/`article_text` e questo `cited_panel_check` sono la stessa disciplina applicata a due livelli, e in entrambi i casi il secondo livello è stato scoperto **dopo** aver applicato il primo.

### DL-MECH-083 — **La catena K63 su WWOX-K274 lo stabilizza: il default che ci aveva morso, misurato al contrario sul gene stesso**
- **Status:** open · **Tag epistemico:** `DATO` sul meccanismo in cellule tumorali e MEF; `INFERENZA` per qualunque trasferimento a un genotipo WWOX-DEE.
- **Fonte:** PMID **25331887** (Abu-Odeh 2014, *PNAS*; letto, `FTR-20260810-25331887-01`, manifest strict PASS 29 locator).
- 🔴 **Il fatto:** WWOX porta poliubiquitinazione **K63-linked** sulla lisina **K274**, mediata dall'E3 ligasi **ITCH**, e quella catena **non lo degrada — lo conserva e lo sposta**. Il mutante `K274R` ha **emivita più corta** del wild type e non accumula nel nucleo. La ubiquitinazione è qui il segnale di *ingresso nel nucleo* e di *stabilizzazione*, non di distruzione.
- 🔴 **Perché è un reperto per il sistema e non solo per il paper:** la tabella `DEFAULTS THAT BIT US` del dismissal ledger apre con *polyUb → proteasoma*, il default che il 2026-07-12 aveva prodotto un falso negativo. Qui lo stesso default è misurato al contrario **sulla proteina di cui ci occupiamo**, non su un substrato analogo. **Regola di ri-audit:** ogni rigetto che poggia su «è ubiquitinato, quindi è degradato» va rivisto contro questo dato — e in particolare qualunque ragionamento su turnover, stabilizzazione o rescue di un allele WWOX deve partire dal fatto che almeno una delle sue catene fa il contrario.
- ⚠️ **Limiti attaccati al dato, tutti dal pannello e non dal testo:** in Fig 6A l'**input** di `K274R` è molto più debole del wild type, quindi il pull-down confronta un'esca abbondante con una scarsa e «lacked ubiquitination» non è separabile da «ce n'era meno» — e il paper stesso dichiara `K274R` meno stabile, il che **peggiora** il confondimento invece di spiegarlo. La discriminazione K63-contro-K48 vive in **Fig S6C**, e il supplementary è **irrecuperabile** (`FT-053`). L'identificazione di K274 e di ITCH **non è un risultato di questo paper**: è importata dal rif. 3 (Abu-Odeh 2014 *JBC*), non letto e accodato — `IMPORTED_PREMISE_ATTRIBUTION_GATE`.
- **PREMISE_TAG:** `PREMISE: DATO` per la direzione (emivita più corta senza la lisina); `PREMISE: INFERENZA` per il ruolo di K274 come accettore principale, che è misurato con un confondimento di input dichiarato.
- **REVIVAL_TRIGGER:** se il supplementary o il rif. 3 diventano leggibili, riverificare S6C e la mappatura ITCH→K274 e promuovere o declassare di conseguenza.
- **Interconnessioni:** `DEFAULTS THAT BIT US` in [[dismissal_ledger_current]] · `DL-METH-084` · [[epistemic_discipline]].

#### 🔴 CALIBRAZIONE 2026-08-10 — questa voce era scritta come se fosse nuova, e il modello sapeva già più di lei
Aperto il rif. 3 (`PMID 24550385`, `FT-054`) sono emerse tre cose che riscrivono la voce sopra. Registrate qui invece che riscrivendola, perché la differenza fra ciò che avevo concluso e ciò che il modello già conteneva è essa stessa il reperto.

1. **`DL-MECH-083` non si aggancia a niente, e doveva.** `DL-MECH-048` (superseded), `DIS-001` (**riaperta**) e la riga **`D-01`** della tabella `DEFAULTS THAT BIT US` trattano già ACK1/ITCH e il default *polyUb → proteasoma*, con più sfumature di quante ne avessi io. **Mahajan 2005 è già in casa come `corpus placeholder`, PMID 16288044.** Ho scritto una voce parallela a un ragionamento esistente: è la stessa **applicazione disomogenea** che ho contestato altrove oggi, commessa da me.

2. **La formulazione giusta non è «il default è invertito», è «su WWOX la via è biforcata».** Il rif. 3 nomina **due** vie di ubiquitinazione con esiti opposti sulla stessa proteina: la propria — ITCH, catena **K63**, **Lys-274**, esito localizzazione nucleare — e quella di Mahajan, dove **WWOX full-length è poliubiquitinato *e degradato*** mentre `WWOXΔ5–8` non lo è. Gli autori notano che gli esoni 5–8 contengono proprio il residuo K274 e dichiarano aperto se sia lo stesso: *«Whether Lys-274 is the same lysine in the WWOX C terminus that also targets WWOX for degradation is not known and would be of great interest to determine»* — verificato verbatim contro l'artefatto. Quindi il default non va sostituito con il suo inverso: **va sostituito con l'obbligo di misurare la via**, che è ciò che `D-01` diceva già.

3. ✅ **E qui il ri-audit produce compounding invece di sola correzione.** `DIS-001` porta, come cautela argomentata e senza fonte, *«inhibiting ITCH would strip WWOX of its DDR function via ATM»*. Era un ragionamento scritto **prima** che qualcuno leggesse `25331887`. Adesso ha una misura sotto: `25331887` mostra che la deplezione di WWOX smorza il checkpoint ATM, e in **Fig 7C** che i MEF `Itch`-KO hanno p-KAP1 ridotto **e** accumulo di WWOX ridotto. **La cautela di `DIS-001` passa da inferenza a inferenza sostenuta**, e la sua conclusione operativa — ITCH come *sonda sperimentale*, mai come bersaglio terapeutico — si rafforza.

- **PREMISE_TAG aggiornato:** `PREMISE: DATO` per l'identificazione ITCH/K63/Lys-274 (spettrometria sul peptide `FTDINDSLGK274LDFSR` più mutagenesi `K274R`, rif. 3 Fig 5 E–G — da riverificare come locator alla lettura completa); 🔴 `PREMISE: NON RISOLTA` per la **stabilizzazione**, che poggia sulla sola asserzione di `25331887` con l'evidenza in `Fig S7B`, cioè in un supplementary **irrecuperabile** (`FT-053`).
- **Interconnessioni aggiunte:** `DL-MECH-048` · `DIS-001` · `D-01` · `FT-053` · `FT-054` · PMID **16288044**.

### DL-METH-084 — **Due paper dello stesso laboratorio si contraddicono sulla direzione dell'HDR, lo dicono in stampa, e la spiegazione pubblicata è incompleta**
- **Status:** open · **Tag epistemico:** `DATO` per entrambe le misure; `INFERENZA` per la riconciliazione.
- **Fonti:** PMID **25331887** (2014) e PMID **38499540** (2024), entrambi con Aqeilan autore senior, entrambi letti il 2026-08-10.
- **Il conflitto, misurato:**

| | manipolazione | sistema | esito su HDR |
|---|---|---|---|
| `25331887` Fig 3E | **sovraespressione** di WWOX | U2OS, reporter DR-GFP, I-SceI | GFP⁺ da **10,0% a 20,8%** (`P<0,01`) — WWOX **alza** l'HDR |
| `38499540` Fig 2A/B | **perdita** di *Wwox* | epitelio mammario murino, foci | **più** RAD51 e **meno** 53BP1 — la perdita **alza** l'HDR |

- ✅ **Gli autori lo dichiarano**, e questo va detto a loro credito: *«In contrast, a previous paper by Abu-Odeh and colleagues, has shown that WWOX enhances HDR in U2OS cells [36]»*, attribuendolo a linee cellulari e sistemi reporter diversi.
- 🔴 **Ciò che la spiegazione pubblicata omette, e che si vede solo aprendo il pannello:** in Fig 3E di `25331887` **non esiste alcun braccio di perdita di funzione**. Tutte e quattro le barre sono costrutti *aggiunti* a U2OS — `EV`, `WWOX`, `WFPA`, `K274R`. Quindi un paper misura il **guadagno** e l'altro la **perdita**, e i due risultati **non sono opposti simmetrici**: non è escluso che WWOX alzi l'HDR in sovraespressione *e* che la sua assenza la alzi per un'altra via (resezione precoce, come sostiene Park et al., rif. 17). «Linee diverse» è vero e insufficiente: la differenza di **direzione della manipolazione** è la variabile non nominata.
- ⚠️ **Nota sulla barra `K274R`:** sta a **~8,3%**, cioè **sotto** l'`EV` a 10,0%. Il testo la rende come *«was not associated with improved HR»*. Un mutante che scende sotto la linea di base non è semplicemente inattivo, e il paper non lo commenta.
- 🔴 **E l'errore che ha portato qui era mio:** avevo accodato `25331887` (`FT-052`) sostenendo che `38499540` vi ancorasse la propria direzione in vivo. La frase *«correspond with previous in vitro findings»* cita **[17], [38], [39]**; `25331887` è il **[36]**. Avevo attribuito una citazione senza leggere il numero — la stessa forma dell'audit `cited_panel_check`, spostata dal pannello alla bibliografia. Corretto nel `multihop` di `PMID38499540.json` e in `FT-052`.
- **Conseguenza operativa:** qualunque claim canonico su «WWOX e scelta della via di riparazione» deve portare il conflitto attaccato e **dichiarare la direzione della manipolazione**, non solo il sistema. Un claim che dica soltanto «WWOX favorisce il NHEJ» o «WWOX favorisce l'HDR» è sottospecificato rispetto a ciò che la letteratura contiene oggi.
- **REVIVAL_TRIGGER:** la lettura di Park et al. (rif. 17 di `38499540`, PMID non risolto) è ora l'hop di massimo valore: è lo studio con cui `38499540` dichiara allineamento, e definirebbe se la via «resezione precoce» riconcilia le due misure.
- **Interconnessioni:** `DL-MECH-083` · `IMPORTED_PREMISE_ATTRIBUTION_GATE` · `DL-METH-082`.

> 🔴 **Nota di merge, 2026-08-10.** Le voci che seguono arrivano da un secondo ramo che ha
> appeso al ledger nello stesso momento del precedente. **Tenute entrambe**: un ledger
> append-only si somma, non si sceglie, e scartare un lato avrebbe cancellato la lettura di un
> attore nel file che esiste per accumularla.
>
> Una collisione di numerazione va dichiarata invece che nascosta: i due rami hanno allocato
> «il prossimo numero libero» contro istantanee diverse, ed entrambi sono arrivati a **081**.
> La voce di questo secondo blocco è stata rinumerata da `DL-THER-081` a **`DL-THER-089`**,
> che era il buco lasciato dalla stessa collisione — verificato prima di toccarla che nessun
> file la citasse, mentre `DL-METH-081` è citata dalla coda dei full text e quindi non si
> muove. È la stessa forma dei quattro `FT-` duplicati trovati oggi, e la stessa ragione:
> **due rami che contano l'ultimo numero di due code diverse producono lo stesso numero.**

### DL-THER-089 — A51, primo intervento farmacologico su un modello neurale umano WWOX-deficiente: recupera i progenitori e non i neuroni di strato
- **Status:** open · **Tag epistemico:** `IPOTESI`. **Non è un candidato terapeutico** e non va descritto come tale: nessuno dei quattro requisiti di Track C è soddisfatto — la direzione di pathway non è firmata, il readout prossimale non è Tier 1/2, la sicurezza CNS pediatrica non è valutata, e il composto non è selettivo per il bersaglio nominato.
- **Fonti:** PMID **42397075** (letto, `FTR-20260810-42397075-04`, manifest `PMID42397075.json`, **30 locator**, `MANIFEST STRICT PASS`). *Conteggio e receipt aggiornati il 2026-08-10 sera: la voce era stata scritta a 25 locator e sul receipt `-03`, entrambi veri quando scritti e superati dalla chiusura della lettura.*
- **Cosa è A51:** un inibitore **multi-chinasi**, non un inibitore di MYC. Il paper stesso lo definisce *"a multi-kinase inhibitor (A51) established to suppress Wnt and MYC expression"*. Dose submassimale 125 nM, dalla settimana 8 alla 15 in vitro, composto fornito dal gruppo Ben-Neriah. 🔴 `PREMISE_TAG` · `PREMISE: INFERENZA` — «l'inibizione di MYC recupera la neurogenesi» poggia su un intervento che sopprime **due** vie, e l'attribuzione causale a MYC eredita l'ambiguità. Gli autori la dichiarano, non la nascondono.
- 🔴 **DATO dai pannelli — il recupero è parziale e selettivo, e il pannello separa ciò che la frase unisce** (Suppl. Fig. 7F–G, letta a 170 ppi e **ri-letta a 258 ppi** il 2026-08-10 sera — il contenitore ne forniva 213 e la lettura originale era sotto; i valori qui sotto **reggono**, artefatti entrambi fingerprintati):

  | misura | WT | KO | KO + A51 | verdetto |
  |---|---:|---:|---:|---|
  | SOX2⁺ | ≈27% | ≈60% | ≈33% | normalizzato (`ns` vs WT) |
  | SOX2⁺MYC⁺ | ≈48% | ≈72% | ≈50% | normalizzato (`ns` vs WT) |
  | NEUN⁺ | ≈30% | ≈6% | ≈18% | recuperato (`*` vs KO) |
  | **SATB2⁺** | ≈1,4% | ≈0,35% | ≈0,7% | **`ns` KO-vs-A51 — nessun recupero** |
  | **CTIP2⁺** | ≈12,5% | ≈0,2% | ≈0,3% | **`ns` KO-vs-A51**, resta `****` sotto WT |

  Inibire MYC ripristina **identità progenitrice e marcatura pan-neuronale** e lascia dove stava la **produzione di neuroni di strato**, profondi e superficiali. Qualunque riformulazione a valle deve portarsi dietro questa scissione.
- 🔴 **BLOCK-1 — la domanda di sicurezza, aperta e non risolta:** un inibitore multi-chinasi che sopprime **Wnt** in un contesto **neurologico pediatrico in sviluppo**. Wnt canonico è richiesto per la proliferazione dei progenitori neurali e la patterning corticale; sopprimerlo durante la corticogenesi non è un effetto collaterale ipotetico ma il meccanismo stesso per cui il composto riduce i progenitori — che in questo esperimento è l'esito desiderato. **La finestra terapeutica fra «riduce i progenitori in eccesso» e «impedisce la corticogenesi normale» non è misurata da nessuna parte in questo lavoro**, che testa una dose sola su un genotipo solo. Nessuna promozione oltre `IPOTESI` finché non esiste una curva dose-risposta con un braccio WT trattato.
- **Vincoli metodologici ereditati, tutti dichiarati dal paper:** l'esperimento di inibizione MYC è uno dei **tre** che il paper esclude dalle differenziazioni indipendenti (con scRNA-seq e ChIP-seq NSC) — cioè i tre su cui poggia la tesi WWOX–MYC; e *"No randomization or blinding was applied in this study"*.
- **Cosa serve per muoverlo di un gradino:** (a) un inibitore MYC selettivo, per separare Wnt da MYC; (b) una dose-risposta con braccio WT trattato, per la finestra; (c) un readout prossimale Tier 1/2 legato al gene, che oggi non esiste — SOX2 e NEUN sono marcatori di identità cellulare, non biomarcatori di funzione WWOX.
- **Interconnessioni:** `FT-039` · `DL-MECH-078` · [[claim_registry_current#CLAIM 003]] · [[therapeutic_hypotheses_ledger_current]] · manifest `PMID42397075.json` entries A51.
- **Destinazione dichiarata:** questa voce **è materiale per un commit candidate**, non un commit candidate. La distinzione è quella che l'orchestratore ha isolato oggi: né il nome di un file né una stringa contenuta identificano un candidato, quindi lo dichiaro qui in prosa e la promozione resta di chi possiede il gate.

---

> ## 🔢 Nota di allocazione — perché queste quattro voci partono da 085 e non da 082
>
> `082` e `084` sono liberi. Non li prendo. **L'allocazione degli ID di questo ledger è
> concorrente e non guardata**, e la collisione di allocazione è stata isolata come classe
> proprio oggi: chi scrive fa la cosa giusta e collide lo stesso, perché nessuna disciplina di
> scrittura la previene — solo una guardia o un'allocazione centralizzata. So che B ha in mano
> `DL-METH-079` e `DL-MECH-083`; non so cosa abbiano Plan e Codex.
>
> Quindi prendo **085–088 come blocco contiguo, con uno stacco sopra 083**, e lo dichiaro qui
> invece di prendere i numeri liberi in silenzio. Uno stacco costa nulla; una collisione costa
> un `BLOCK_BATCH_COMMIT` a chi merge per secondo. Se l'allocazione diventa centralizzata,
> questa nota è il primo posto da cui cancellarla.

### DL-BIO-085 — L'abbondanza di proteina WWOX non è una lettura della funzione di WWOX, e le due misure che lo chiudono vengono da lati opposti
- **Status:** open · **Tag epistemico:** `DATO` per ciascuna delle due osservazioni, `INFERENZA` per la conclusione congiunta.
- **Fonti:** PMID **42128308** (letto, `FTR-20260810-42128308-02`, manifest `PMID42128308.json`, 25 locator, `MANIFEST STRICT PASS`), sezioni 10.1 e 10.3. **Nessuna delle due misure dipende da un preprint** — è la ragione per cui questa voce è la più solida delle quattro.
- 🔴 **Le due misure, e sono in direzione opposta:**

  | modello | proteina WWOX | fenotipo | fonte primaria citata |
  |---|---|---|---|
  | **`Wwox^P47T/P47T`** knock-in murino | **pari al wild type** | epilessia ad esordio adulto, neurodegenerazione cerebellare, atassia, neuroinfiammazione progressiva | Hussain et al. 2023 |
  | **Organoidi frontali SCAR12** da iPSC paziente | **minima** | morfologia, marcatori di strato e rapporto E/I **simili ai controlli sani** | Steinberg et al. 2021 |

- **Il meccanismo che spiega la prima riga è dichiarato:** la mutazione P47T *«disrupts the WW1 domain's PPXY motif, leading to partial WWOX loss-of-function and impaired binding with downstream interaction partners»*. Cioè **perdita di funzione per interazione fallita, non per proteina persa.**
- 🔴 **La conseguenza per il layer biomarker, che è la ragione di questa voce:** un biomarcatore Tier 1/2 costruito sull'**abbondanza** di WWOX classificherebbe **P47T come normale** e **SCAR12 come gravemente colpito**, e sarebbe sbagliato **in entrambi i casi e in direzioni opposte**. L'abbondanza non predice né la presenza né l'assenza del fenotipo cellulare.
- **Come si connette a ciò che questo repository già sa:** è l'asse **funzione** che fallisce mentre **sintesi** e **solubilità** passano — la separazione a cinque vie (*sintesi · solubilità · turnover · rotta · funzione*) che il caso del carcinoma tiroideo del 2026-07-12 impose a questo sistema. Allora fu dimostrata su una linea tumorale e su un allele; **qui è dimostrata in vivo su un allele di malattia e su materiale neurale umano di paziente.**
- 🔴 `PREMISE_TAG` — *«se la proteina c'è, la funzione c'è»* · `PREMISE: DEFAULT_FROM_TEXTBOOK`. Va nella tabella `DEFAULTS THAT BIT US` del [[dismissal_ledger_current]], accanto a *«stabilizzare ⇒ funzione ripristinata»*, che è la stessa premessa vista dal lato terapeutico.
- **Cosa serve per muoverlo di un gradino:** un readout **funzionale** prossimale e legato al gene — un partner di interazione la cui occupazione si misuri, non una banda su un blot. Oggi non esiste in questo corpus, e questa voce serve soprattutto a dire che **il posto vuoto è quello**.
- **Interconnessioni:** `FT-045` · `DL-THER-089` · `DEFAULTS THAT BIT US` in [[dismissal_ledger_current]] · [[biomarker_endpoint]].
- **Destinazione dichiarata:** **materiale per un commit candidate**, non un candidato. Promozione a chi possiede il gate.

### DL-MECH-086 — La review dice «restored» dove il suo stesso primario mostra dieci volte il wild type, e la parentesi che lo falsificherebbe non è disegnata
- **Status:** open · **Tag epistemico:** `DATO` sui due fatti, `INFERENZA` sul nesso.
- **Fonti:** PMID **42128308** §10.4 (testo) contro PMID **42397075** Suppl. Fig. 10B–C (pannelli, riletti a **258 ppi**).
- **Il fatto testuale:** la review, dello stesso gruppo e con lo stesso primo autore del primario di ottimizzazione, scrive che la ri-espressione neuronale di WWOX ha *«restored deep-layer neuronal markers (CTIP2, SATB2)»*.
- 🔴 **Il fatto grafico:** nel primario, SATB2 mRNA nel WOREE trattato **non torna al wild type**: la scatola va da ≈1 a ≈11 contro wild type a ≈1,3, con la linea non trattata a ≈0,6. BCL11B/CTIP2 arriva a ≈3,0 contro 1. *(Correzione registrata: avevo prima scritto «circa dieci volte» come valore centrale; a 258 ppi quello è il tetto della scatola. La lettura corretta **affila** il reperto — una distribuzione trattata che va da wild type a undici volte wild type è **assenza di controllo del livello**, che nomina il meccanismo invece della magnitudine.)*
- 🔴 **Perché la parola sopravvive, ed è la parte strutturale:** le parentesi di significatività corrono **WT-vs-EGFP** e **EGFP-vs-WWOX**. **La parentesi WT-vs-trattato non è disegnata.** Il confronto che falsificherebbe *«restored»* non è mai stato fatto. Verificato come **assenza** a 258 ppi dopo che la lettura originale era a 170 — *una parentesi assente è un reperto ed è anche ciò che una risoluzione bassa fabbrica*, quindi ogni affermazione di assenza di quella pagina è stata ricontrollata, non solo la sospetta.
- 🔴 **Il passaggio che va nominato e non dato per fatto:** la review cita `Steinberg et al. 2024` al **DOI del preprint** `10.1101/2024.12.22.630016`, mentre io ho letto il **manoscritto accettato** (`PMID 42397075`, *Brain*). La contraddizione è quindi fra **la lettura che la review fa del preprint** e **la mia del manoscritto accettato**. Non si dissolve — la versione accettata è quella che il campo citerà — ma i pannelli supplementari aggiudicati a 258 ppi **possono non essere quelli che la review ha letto**, e questo va scritto nel candidate invece che assunto.
- **Interconnessioni:** `FT-045` · `FT-039` · `DL-MECH-087` · manifest `PMID42128308.json` entries[5] e `PMID42397075.json` entries[22].
- **Destinazione dichiarata:** **materiale per un commit candidate**.

### DL-THER-087 — L'anello WPRE si chiude dentro un solo documento, e nessuno dei due capi cita l'altro
- **Status:** open · **Tag epistemico:** `DATO` sui tre fatti, `INFERENZA` sul nesso.
- **Fonti:** PMID **42128308** §10.4 e §11 (testo) · PMID **42422765** `entries[15]` (pannelli).

  | dove | cosa dice |
  |---|---|
  | **§10.4** | rimuovere WPRE era *«aimed at avoiding excessive or poorly controlled transgene expression while preserving sufficient therapeutic efficacy»* |
  | **primario** | la rimozione **richiese sei volte la dose** per recuperare efficacia; la proteina senza WPRE a 2E10 sta **a o sotto il wild type** |
  | **§11** | *«high-dose AAV administration»* è il motore della patologia dei gangli delle radici dorsali e *«a key regulatory concern in pediatric CNS gene therapy programs»* |

- 🔴 **L'efficacia non è stata *preservata a dose*: è stata ricomprata con vettore**, nella valuta che la review stessa nomina come il problema di sicurezza. La review celebra la scelta di progetto in una sezione e, due sezioni dopo, nomina il costo di quella scelta come il principale ostacolo regolatorio del campo — **senza collegarli**.
- **Il vincolo che il primario e la review si scambiano senza saperlo:** §11 pretende che *«any effective strategy must recapitulate its natural spatiotemporal expression patterns»*; `PMID 42397075` mostra che l'AAV9 produce WWOX **da 0,4 a 7 volte il wild type** fra linee trattate con lo stesso vettore. **La review enuncia un requisito che il vettore corrente dimostrabilmente non soddisfa, e il primario che lo dimostra è dello stesso gruppo.**
- **Cosa serve per muoverlo di un gradino:** una curva dose-risposta che riporti **insieme** efficacia e biodistribuzione periferica sullo stesso asse. Oggi vivono in paper diversi e in sezioni diverse dello stesso paper.
- **Interconnessioni:** `FT-045` · `FT-041` · `DL-MECH-086` · manifest `PMID42128308.json` entries[6].
- **Destinazione dichiarata:** **materiale per un commit candidate**.

### DL-META-088 — Due fonti non referate, lo stesso statuto, due trattamenti diversi a due pagine di distanza
- **Status:** open · **Tag epistemico:** `DATO`. **Non è una critica al paper: è un fatto sulla superficie che un lettore a valle eredita senza vederlo.**
- **Fonti:** PMID **42128308**, bibliografia enumerata (**103 voci**, 35 WWOX-dirette, 4 preprint, tutti WWOX-diretti).
- **L'asimmetria:**

  | fonte | statuto | come la review la presenta |
  |---|---|---|
  | Lucas-Clarke et al. 2025 | bioRxiv `10.1101/2025.05.01.651195` | *«A recent preprint by (Lucas-Clarke et al., 2025)»* — **dichiarato** |
  | **Abudiab et al. 2025** | bioRxiv `10.1101/2025.11.22.689900` | citato **sette volte in modo sostanziale** — **mai dichiarato** |

- 🔴 **Dove pesa:** due citazioni in sezione 6 (WWOX fra i geni oligodendrogliali più disregolati; il risultato cuprizone *«at least in part through regulation of the key oligodendrocyte transcription factor SOX10»*) e **quattro righe distinte della Tabella 1** — Olig2-Cre O-KO, la sfida cuprizone su quella linea, la coltura OPC ex vivo, lo snRNA-seq delle lesioni MS. La Tabella 2 chiama il concetto cell-autonomo *«a particularly important emerging concept»* e i meccanismi SOX10 *«a major new direction»*.
- **Chi legge la Tabella 1 porta via quattro righe di evidenza murina senza sapere che nessuna è referata.**
- 🔴 **Conseguenza già pagata, su di me:** avevo registrato il contrasto basale-contro-cuprizone come *requisito condizionale* con la formula *«un readout oligodendrogliale non sfidato è un falso negativo per costruzione»*. **Declassato a `IPOTESI`**: fonte unica, non referata. La forma del reperto non cambia; il suo supporto sì, e non avevo controllato quale. `PREMISE_TAG` mancante sotto una conclusione che sembrava reggersi da sola.
- **Il reperto collaterale, che vale una riga in coda e non un'indagine:** due dei quattro preprint (`Steinberg 2024`, `Obeid 2026`) sono citati a DOI di preprint **benché pubblicati** come `PMID 42397075` e `PMID 42422765`. **Il corpus contiene ora almeno due paper la cui citazione più recente in letteratura punta a una versione che non abbiamo.**
- **Cosa lo renderebbe generale invece che aneddotico:** un controllo su ogni review nel corpus che confronti **quante fonti non referate cita** con **quante ne dichiara tali**. Riporterebbe `matched N of population P` ed esibirebbe `P − N`, che è la forma che Mirror ha isolato oggi. Non l'ho costruito: è infrastruttura e questa era una sessione di lettura.
- 🔴 **AGGIUNTO LA SERA STESSA — l'asimmetria dei preprint non è isolata: è una delle TRE compressioni indipendenti dello stesso documento, su tre lati diversi.** Tre istanze indipendenti in un solo testo non sono uno stile: sono un modo di leggere le fonti, ed è una proprietà della superficie che un lettore a valle eredita per intero.

  | lato | la review dice | il suo stesso primario mostra |
  |---|---|---|
  | **molecolare** | AAV9 ha *«restored deep-layer neuronal markers (CTIP2, SATB2)»* | SATB2 va da wild type a **undici volte** wild type, e **la parentesi WT-vs-trattato non è disegnata** (`PMID 42397075`) |
  | **terapeutico** | rimuovere WPRE *«aimed at avoiding excessive or poorly controlled transgene expression while preserving sufficient therapeutic efficacy»* | la rimozione richiese **sei volte la dose**, e §11 della review stessa nomina l'alta dose come la principale preoccupazione regolatoria pediatrica (`PMID 42422765`) |
  | **clinico** | *«a homozygous missense WWOX mutation (p.Ser304Tyr) … despite the mutation type typically being associated with milder phenotypes»* | la variante è **ACMG «Unclear clinical significance»**, gli autori scrivono che la patogenicità *«require[s] validation»*, e c'è un **secondo candidato in `CACNA1A`** contro una DEE **autosomica dominante** (`PMID 39416860`) |

  **Tre volte la metà semplice**, e ogni volta la metà che cade è quella che introdurrebbe una qualificazione. Nessuna delle tre è visibile leggendo la review; tutte e tre lo sono leggendo **ciò che la review cita**. Fonti: `FT-045` · `FT-055` · manifest `PMID42128308.json` entries[5], entries[6], entries[23], entries[24].
- 🔴 **QUARTA, TROVATA DOPO LE ALTRE TRE, E DI UNA SPECIE DIVERSA: le prime tre RIDUCONO un risultato, questa ne INVERTE il senso.** La review presenta il caso dell'introne 4 di Oliver 2023 come una crepa nel framework — *«technically falls under category 2 … However, the observed clinical severity was comparable to that of patients with category 1 genotypes»*. Ma Oliver **codifica quella delezione come null**, perché causa lo skipping dell'esone 5 mentre quella dell'introne 3 è benigna, e tabula il paziente 6 come **`Missense/null`**: un ordinario caso di classe 2. E in uno schema dove la classe 2 **non mostra alcun fenotipo intermedio**, un classe-2 grave quanto un classe-1 è **il risultato atteso**. La review lo offre come anomalia; è il framework che funziona come la sua fonte dice che funziona. Fonte: `FT-056`, `FTR-20260810-36779245-03`.

---

> ## 🔢 Nota di allocazione — `089` lasciato libero
> Il blocco `085`–`088` era il mio, dichiarato. Questa voce arriva dopo ed è indipendente, quindi
> prendo **`090`** lasciando `089` come stacco, per la ragione già scritta sopra: l'allocazione
> è concorrente e non guardata, e nel frattempo altri attori hanno allocato.

### DL-BIO-090 — «Missenso» non è una classe funzionale: la premessa sotto la traccia ipomorfi/ASO va riscritta, non difesa con un controesempio
- **Status:** open · **Tag epistemico:** `DATO` sulle tre osservazioni, `INFERENZA` sulla riscrittura.
- **Perché esiste questa voce:** oggi la premessa *«missenso ⇒ funzione residua ⇒ più lieve»* è stata attaccata due volte cercando un **controesempio** — Feng 2024, poi Oliver 2023. **Era il modo sbagliato di affrontarla.** Un controesempio presuppone che la categoria sia ben formata e che qualche membro si comporti male. Qui è la **categoria** a non esistere.

- 🔴 **Le tre osservazioni, tutte dalla stessa fonte e tutte verbatim:**

  | osservazione | citazione |
  |---|---|
  | **stesso residuo, due malattie** | *«p.Pro47 has been associated with two pathogenic variants; the more conservative change to threonine was found in SCAR12»* — contro l'arginina in WWOX-DEE |
  | **nessuna via di scampo regionale** | *«no region of the gene emerged as specific for being associated with WWOX-DEE»*; le due missenso SCAR12 stanno **vicine** a varianti DEE |
  | **nessun intermedio, dalla fonte dello schema** | *«We found no difference between individuals with one or two missense variants and therefore no evidence to support an "intermediate" phenotype»* |

- **La riscrittura, e va usata al posto della premessa vecchia:** la gravità in WWOX è **specifica della sostituzione**, non del tipo di variante, non del residuo e non della regione. `p.Pro47Thr` e `p.Pro47Arg` sono entrambi missensi sullo **stesso residuo** e danno malattie diverse. Quindi:
  - **`missense` è una categoria di annotazione, non una categoria funzionale.** Usarla per predire la gravità, la funzione residua o l'idoneità a un approccio terapeutico è una **inferenza non supportata**, e ogni volta che compare in questo repository va sostituita con la domanda *«questa sostituzione, misurata come?»*.
  - **La sola stratificazione che i dati sostengono è binaria e su un asse solo:** null/null contro *almeno un missenso*, sulla **sopravvivenza** (p = .0085). Sull'esordio delle crisi **nessuna differenza fra i tre gruppi** (p = .65).
  - 🔴 **Conseguenza per la traccia ASO/ipomorfi:** un allele non è un bersaglio ASO perché è missenso. Lo è se **quella sostituzione** lascia proteina misurabilmente funzionale — che è la domanda di `DL-BIO-085`, dove `P47T` mostra proteina a livello wild type e funzione persa per fallimento di interazione. **Le due voci sono la stessa domanda vista dalle due estremità:** 085 dice che l'abbondanza non misura la funzione, 090 dice che l'annotazione non la predice. **Fra le due non resta nessuna scorciatoia: la funzione va misurata.**

- 🔴 **E la ricorrenza cambia quanto vale rispondere.** `p.Gln230Pro` compare in **tre dei dodici pazienti non imparentati** di Oliver — omozigote in due — **più sei famiglie già riportate** da Iran, Afghanistan, Francia e Marocco. È **l'allele missenso WWOX-DEE più ricorrente della letteratura**, ed è quello attorno a cui è costruito l'intero lavoro di proteostasi di questo repository. La domanda su Q230P non è uno studio di caso: **riguarda l'allele più frequente del campo.**

- **Cautela sull'unico numero che qualcuno sarà tentato di citare come prognosi:** la coorte di Oliver è dichiaratamente **più anziana** (media 8a 2m contro 3a 4m) e **meno letale** (23% contro 38%) della letteratura con cui è messa in pool, con null/null al 50% contro 60%. La curva di sopravvivenza è un **confronto fra gruppi**, non una prognosi. Chi la citasse come prognosi userebbe un dato di ascertainment come dato clinico.

- **Cosa serve per muoverlo di un gradino:** un saggio funzionale per singola sostituzione — non abbondanza, non solubilità, ma **occupazione di un partner di interazione** — applicato per primo a `Q230P` per ricorrenza e a `P47T`/`P47R` perché sono la coppia che dimostra il punto sullo stesso residuo.
- **Interconnessioni:** `DL-BIO-085` · `DL-META-088` · `FT-055` · `FT-056` · `DEFAULTS THAT BIT US` in [[dismissal_ledger_current]] · [[claim_registry_current]].
- **Destinazione dichiarata:** **materiale per un commit candidate.** È una *sostituzione* di premessa, non un'aggiunta, quindi tocca affermazioni già in stato canonico e la promozione va fatta da chi possiede il gate, non da me.
- **Interconnessioni:** `FT-045` · `DL-MECH-086` · manifest `PMID42128308.json` entries[7], entries[23], entries[24].
- **Destinazione dichiarata:** **materiale per un commit candidate**.

---

### 🔴 DL-META-091 — Johannsen 2018 non è mai stato letto, e il modello ci poggia sopra 21 volte

> **Allocazione:** 091–093 sono miei (sessione A, 2026-08-10 sera). 084 e 089 restano i buchi
> dichiarati in precedenza; 083 è di B.

- **Status:** open · **Tag epistemico:** `DATO` sul censimento, `INFERENZA` su cosa comporta.
- **Come è emerso — e il punto è *come*, non *cosa*.** Non l'ho cercato. Stavo registrando la
  ricevuta di `PMID 32581702` e avevo scritto `references: not_read`. **Il writer del ledger ha
  rifiutato**: una `complete_fulltext_read` non può lasciare una sezione non letta. Enumerare la
  `<ref-list>` è costato due minuti — 50 referenze, 22 WWOX-dirette — e incrociarle contro ogni
  ricevuta di tutti e sei i rami ha prodotto nove paper invisibili al piano di lettura (`FT-057`).
  Uno di quei nove è **Johannsen 2018, `PMID 29808465`**.

- 🔴 **Il censimento, misurato e non stimato:**

  | dove | quante volte |
  |---|---|
  | `discovery_ledger_current.md` | **21** occorrenze |
  | `claim_registry_current.md` · `paper_registry_current.md` · `disease_model.md` | presente |
  | `dismissal_ledger_current.md` · `therapeutic_hypotheses_ledger_current.md` | presente |
  | `analysis/proteostasis_rationale.md` | presente |
  | **ricevute full-text, su `main` · `lettore` · `lettore-b` · `mirror` · `evidence-index` · `codex`** | **0** |

- 🔴 **Cosa regge esattamente.** Il dato che il modello importa da Johannsen è
  *«Q230P → trascritto normale, proteina assente»*. **È la base dell'intera traccia di
  proteostasi**: è ciò che rende Q230P un amorfo funzionale invece che un missenso ipomorfo, ed
  è la ragione per cui il genotipo di riferimento viene letto «più vicino a null/null che a
  quei fratelli» (`DL-MECH-037`, e la riserva a riga 819 di questo ledger). Se quel dato fosse
  qualificato — un solo paziente, una sola condizione, un anticorpo, un'unica frazione — nulla
  di ciò che ne discende cambierebbe *segno*, ma tutto cambierebbe *forza*.

- **`PREMISE_TAG`:** 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — non perché il dato sia dubbio, ma
  perché **nessuno in questo sistema ha visto la figura che lo mostra.** È il caso puro di
  `UNREAD_PREMISE`: una premessa che ha attraversato l'intero stato canonico senza mai passare
  dal gate che esiste per le premesse.
- **`REVIVAL_TRIGGER` / condizione di chiusura:** leggere `PMID 29808465` per intero, con
  ispezione della figura che mostra trascritto e proteina, e verificare **(a)** che il dato sia
  su Q230P e non su un'altra variante SDR, **(b)** con quale n e in quale materiale, **(c)** se
  il trascritto normale sia stato misurato o inferito.
- **Interconnessioni:** `FT-057` · `FT-002` · `DL-MECH-037` · `DL-BIO-090` · `DL-BIO-085` ·
  [[dismissal_ledger_current#DEFAULTS THAT BIT US]] · `analysis/proteostasis_rationale.md`.
- **Destinazione dichiarata:** **priorità di lettura**, non commit candidate. Non c'è nulla da
  promuovere finché il paper non è letto; c'è da leggere.

#### 🔴 CORREZIONE APPEND-ONLY, stessa sera, dopo aver provato a leggerlo — **la metà allarmistica di questa voce era sbagliata**

Ho tentato la lettura un'ora dopo aver scritto quanto sopra. Due risultati, e il secondo
ribalta il primo.

**(a) Non è leggibile, e non da oggi.** `PMID 29808465` — *Neurogenetics* 19(3):151-156,
Springer. `pmcid: null` · `inPMC: N` · `isOpenAccess: N` · Unpaywall `is_oa: false`,
`oa_status: closed`, `has_repository_copy: false`, `oa_locations: []` · nessun artefatto locale.
🔴 **Formulazione deliberata: non l'ho potuto recuperare per queste rotte, non «è
irrecuperabile».** Quindi le 47 citazioni non sono una svista di nessuno: **il paper non è mai
stato disponibile a chi lo citava.** Il dato è entrato dall'abstract, che è dove sta.

**(b) 🔴 E lo stato canonico lo ha trattato meglio di come questa voce lasciava intendere.**
Ho verificato invece di assumere, e il modello **porta già** ogni qualificazione che conta:

| ciò che temevo | ciò che lo stato dice davvero |
|---|---|
| che «proteina assente» fosse letta come degradazione | `disease_model.md`: **inversione MAJOR `WM v2.1 → v3.0`** che *ritira* l'equazione `mRNA normale + proteina assente = degradazione post-traduzionale`, citando le due alternative di Johannsen |
| che il meccanismo fosse dato per risolto | **`DL-MECH-029`**, il cui titolo stesso è *«Q230P: trascritto normale, **proteina non rilevata**; causa traduttiva versus degradativa non risolta»*, e che porta *«cause ∈ {impaired_translation, insolubility, premature_degradation} non discriminata»* |
| che «assente» fosse letto come zero | *«"assenza" al Western blot è un limite di sensibilità, non uno zero assoluto»* |
| che il fibroblasto fosse letto come neurone | *«la stabilità proteica può essere tessuto-specifica (un fibroblasto non è un neurone)»* |
| che si assumesse funzione dopo ristabilizzazione | *«⚠️ Assunzione critica ancora aperta … Johannsen non lo testa»* |

**Questo è il sistema che funziona**, e va detto con la stessa forza con cui ho suonato
l'allarme. Una premessa importata da un abstract è stata qualificata meglio di molte importate
da letture complete.

**(c) Il difetto che RESTA non è il contenuto: è la classe di evidenza, e vive su un rifiuto.**
`dismissal_ledger_current.md` `DIS-003` — *«Boosting WWOX expression» → ✅ REJECTION THAT
HOLDS* — dichiara come premessa portante: *«Johannsen 2018 — normal transcript, protein absent
in fibroblasts homozygous for Gln230. ✅ `PREMISE: DATO` (direct measurement, exact variant)»*.
🔴 **`direct measurement` di una misura che nessuno qui ha mai visto.** Il contenuto è giusto;
l'etichetta afferma un atto — aver consultato la fonte primaria — che non è avvenuto. E lo fa
sotto un **rifiuto**, che è la classe asimmetrica: un falso positivo viene testato e muore, un
falso negativo è silenzioso, permanente e auto-rinforzante.

**(d) Due scarti che solo l'abstract rende visibili**, entrambi piccoli e entrambi del tipo che
un'etichetta `DATO` nasconde:
- l'abstract dice *«Functional WWOX analysis was performed in fibroblasts of **one patient**»* —
  su **due** sorelle. Lo stato scrive «in fibroblasts homozygous for Gln230» **senza l'n**;
- l'abstract offre **due** alternative — *«impaired translation **or** premature degradation»* —
  mentre il ledger ne scrive **tre**, aggiungendo `insolubility`. È un'aggiunta difendibile (un
  insolubile scompare dalla frazione solubile di un western) ma **non è ciò che dice l'autore**,
  e siede in uno `Statement causale` accanto alla citazione.

🔴 **E la conseguenza terapeutica che il ramo «impaired translation» porta con sé, che non
trovo enunciata da nessuna parte:** se la proteina non viene **mai sintetizzata**, non c'è
niente da stabilizzare. Una strategia proteostatica indirizza uno solo dei due rami autoriali.
`DIS-003` rifiuta il boost dell'espressione *perché* il collo di bottiglia è a valle — ma se il
collo di bottiglia fosse la traduzione, «a valle della trascrizione» e «stabilizzabile» non
sono la stessa cosa. **Il rifiuto potrebbe essere giusto per una ragione e sbagliato per
l'altra**, e l'unico modo di saperlo è la figura che nessuno ha visto.

- **`REVIVAL_TRIGGER` aggiornato:** ottenere il PDF per via istituzionale e guardare **il
  western**: quante corsie, quale controllo di caricamento, quale esposizione, se il segnale è
  assente o sotto soglia, e se la qRT-PCR è su un solo amplicone. Chi ha accesso a Springer lo
  prenda — è il singolo recupero a più alto rendimento di questa coda.
- **Riclassificazione proposta, non applicata** (tocca un rifiuto in stato canonico, quindi
  spetta a chi possiede il gate): `DIS-003` da `PREMISE: DATO (direct measurement)` a
  **`PREMISE: DATO — abstract-only, primary source never retrieved`**, con il rifiuto che
  *resta valido* e la sua etichetta che smette di affermare un atto non avvenuto.

- 🔴 **`REVIVAL_TRIGGER` proposto per `DIS-003`, che oggi non ne dichiara uno sul meccanismo:**
  > *«Un western che discrimini traduzione da degradazione su fibroblasti Q230P — pulse-labeling
  > della sintesi nascente, o inibizione del proteasoma/lisosoma con recupero del segnale —
  > riapre `DIS-003`. Se il collo di bottiglia è la sintesi, "boosting expression" non è
  > rifiutato dalla stessa ragione con cui è rifiutato oggi.»*

  Il rifiuto attuale poggia su *«il collo di bottiglia è a valle»*: vero, ma **copre due
  meccanismi con conseguenze terapeutiche opposte.** Può essere giusto per uno e sbagliato per
  l'altro, e finché il trigger non lo nomina la distinzione non ha modo di risvegliarlo.
  L'attuale `REVIVAL_TRIGGER` di `DIS-003` riguarda solo il caso composto-eterozigote, cioè la
  *generalizzabilità* del dato, non il **meccanismo** che il dato lascia aperto.

- **Nota di attribuzione, corretta due volte in dieci minuti e vale la pena registrarlo.** Avevo
  scritto che la disgiunzione stava su `DL-MECH-034`: sbagliato, quella è il Warburg negli
  organoidi. L'Orchestratore ha corretto in `CLAIM 019`: **sbagliato anche quello.** È
  **`DL-MECH-029`**, il cui titolo *enuncia* la disgiunzione. Due attori hanno sbagliato lo
  stesso puntatore in direzioni diverse, e solo il terzo controllo — `awk` sull'intestazione che
  precede la riga — ha dato la risposta. *Citare un identificatore a memoria è la stessa classe
  di errore del locator non verificato, applicata alla nostra stessa scrittura.*

---

### 🔴 DL-MECH-092 — `p.R264Ter` non è un null finché qualcuno non misura: tronca **dopo** l'MTS e **prima** del sito catalitico

- **Status:** open · **Tag epistemico:** `DATO` sulla posizione (pannello 1G di `PMID 32581702`),
  `INFERENZA` sulle due biologie che ne discendono.
- **Il fatto.** Il pannello 1G colloca `p.R264Ter` in rosso al confine C-terminale del blocco
  **MTS**, immediatamente prima del `Loop` e del `Catalytic Site`, su una proteina di 414 residui.
  Il paper dichiara la disgiunzione e non la risolve: *«resulting in a loss of normal Wwox
  function either through protein truncation (and disruption of the active C-terminal
  short-chain dehydrogenase/reductase SDR domain), or nonsense-mediated mRNA decay»*. Nessun
  western, nessuna quantificazione del trascritto, nessun materiale del paziente.
- 🔴 **Perché i due rami non sono intercambiabili.** Se il trascritto è degradato dall'NMD, il
  prodotto è **assenza**. Se sfugge all'NMD, il prodotto conserva **WW1, l'NLS, WW2, il sito
  NADP e l'intera sequenza di targeting mitocondriale**, e perde solo la catalisi e ciò che le
  sta a valle: cioè una **Wwox cataliticamente morta che raggiunge ancora i mitocondri e presenta
  ancora entrambi i domini WW ai partner PPXY**. Sono due malattie diverse — e due problemi
  terapeutici opposti: *un'assenza non si può stabilizzare; un interattore morto-ma-presente
  potrebbe non doverlo essere.*
- **`PREMISE_TAG`:** 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — «variante nonsenso ⇒ null». È la
  stessa premessa non misurata su cui poggia la classificazione null/missenso di Oliver 2023
  (`PMID 36779245`), dove una delezione intronica viene codificata `null` per convenzione.
  Sommata a `DL-BIO-090` — «missenso» non è una classe funzionale — resta che **nessuna delle
  due classi del sistema a tre classi è definita da una misura.**
- **`REVIVAL_TRIGGER`:** qualunque dato proteico su un allele nonsenso WWOX — western su
  materiale di paziente, o un modello che esprima il troncato — decide il ramo.
- **Interconnessioni:** `FT-002` · `FT-057` · `DL-BIO-090` · `DL-META-091` · manifest
  `PMID32581702.json` entries[6], entries[7].
- **Destinazione dichiarata:** **materiale per un commit candidate**, come qualificazione di
  premessa e non come nuova affermazione.

---

### DL-META-093 — Tre modi in cui il riassunto di un paper non è il suo dato, tutti e tre nello stesso articolo

- **Status:** open · **Tag epistemico:** `DATO` — tutti e tre verificati contro i pannelli.
- **Perché una voce sola per tre reperti:** perché sono la stessa cosa vista da tre lati, e
  perché tutti e tre sarebbero passati inosservati leggendo solo il testo corrente.

  | # | il testo dice | il pannello mostra |
  |---|---|---|
  | 1 | *«altered distribution of BrdU-positive cells»*, senza numeri | **8 zone su 10** significative, con la zona 2 che va da ~810 a ~70 cellule/mm² — **un ordine di grandezza**, il più grande effetto del paper |
  | 2 | l'abstract attribuisce il reperto trascrittomico ai **progenitori** | nel pannello progenitori i geni etichettati sono **grigi o verdi sotto soglia**; sono rossi solo nel pannello **neuroni** |
  | 3 | la Discussione dice *«significantly reduced expression»* | l'asse di significatività **non è ricostruibile**: soglia a ~0.83 su un asse che si dichiara `-Log10 p`, cioè p≈0.15, e punti sopra 1.0 che una probabilità NOISeq non può assumere |

- 🔴 **L'inversione di enfasi è il reperto generale.** L'effetto che il testo mette in prima
  linea (Satb2, ~un terzo, due asterischi) è **molto più piccolo** di quello che liquida in sei
  parole (BrdU, 8/10, ~11×). Non è disonestà: è che il testo racconta la storia che l'autore
  sta argomentando, e il pannello contiene quello che l'esperimento ha prodotto. **Chi legge
  solo il testo eredita l'enfasi dell'autore al posto dei suoi dati.**
- **Corollario operativo, e va oltre questo paper:** la regola di copertura dei pannelli non
  serve a «trovare di più». Serve perché **il testo corrente è una selezione fatta da qualcun
  altro con un obiettivo diverso dal nostro.**
- **Interconnessioni:** `FT-002` · `DL-BIO-085` · manifest `PMID32581702.json` entries[2], [3],
  [10], [11], [20] · l'istruzione permanente dell'Orchestratore del 2026-08-10 sulla copertura.
- **Destinazione dichiarata:** **materiale per un commit candidate** e argomento a favore della
  regola di copertura, misurato invece che asserito.

---

### 🔴 DL-MECH-094 — La firma «Warburg» degli organoidi è confusa con il difetto di differenziamento che il paper stesso dichiara nel titolo della figura

> **Allocazione:** 094 è mio (sessione A, 2026-08-10 sera). Vedi `DL-META-091` per l'allocazione
> 091–093.

- **Status:** open · **Tag epistemico:** `DATO` sulle due citazioni, `INFERENZA` sul confondimento.
- **Cosa qualifica:** `DL-MECH-034`, che porta la firma OXPHOS↓/glicolisi↑ di `PMID 34268881`
  come chiusura del caveat *«il fenotipo Warburg è documentato in MEF e in cancro, mai nel
  neurone WWOX-carente»*, e con essa il razionale WWOX-specifico della dieta chetogenica.

- ✅ **Prima, ciò che NON contesto, perché lo stato lo dice già e lo dice bene.** `DL-MECH-034`
  dichiara esplicitamente **`Belief: medio sul salto trascrittoma→flusso metabolico
  («l'espressione genica non è il flusso: servirebbe Seahorse/fluxomica»)`**, dichiara l'n basso
  (WT n=2, KO n=4), nomina la tecnica come trascrittomica e rimanda a `DL-BIO-008`, la
  contraddizione sul lattato. **Il salto trascrittoma→flusso era già sotto controllo.** Arrivavo
  per segnalarlo e l'ho trovato scritto meglio di come lo stavo scrivendo io.

- 🔴 **Ciò che invece non trovo da nessuna parte: la spiegazione alternativa sta nel titolo della
  figura da cui il dato proviene.** La sezione che produce la firma metabolica si intitola —
  verbatim — *«Cerebral organoid RNA sequencing revealed **major differentiation defects**»*, e
  l'arricchimento glicolitico compare dentro un elenco di vie **dello sviluppo**:

  > *«marked enrichment was seen in pathways related to regionalization, neuron fate commitment
  > and specification, axis specification (ventral–dorsal and anterior–posterior), and
  > **glycolysis and gluconeogenesis**»*

  mentre l'altro braccio della firma è:

  > *«inhibition of processes related to ATP synthesis‐coupled electron transport and
  > **oxidative phosphorylation**»*

- **L'inferenza, e perché non è una pignoleria.** I progenitori neurali sono **glicolitici**; la
  maturazione neuronale comporta uno **switch verso la fosforilazione ossidativa**. È biologia
  dello sviluppo di base. Un tessuto che il paper stesso descrive come **immaturo e con
  differenziamento difettoso** produrrà per *quella* ragione un trascrittoma con OXPHOS↓ e
  glicolisi↑. **La firma metabolica è quindi il fenotipo atteso dell'immaturità, e non è
  separabile — con questi dati — da un ruolo metabolico di WWOX.**

- **`PREMISE_TAG`:** 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` sulla premessa non scritta *«un
  trascrittoma OXPHOS↓/glicolisi↑ in questo tessuto riflette un assetto metabolico
  WWOX-dipendente»*. La spiegazione concorrente non è esotica: è la tesi principale del paper.

- 🔴 **Conseguenza sull'esperimento discriminante, che è la parte operativa.** `DL-MECH-034`
  propone giustamente **Seahorse OCR/ECAR sugli organoidi WWOX-KO**. Ma un Seahorse su organoidi
  KO contro WT alla stessa settimana di coltura **riprodurrebbe lo stesso confondimento**: se i
  KO sono developmentally più giovani, misurerei l'immaturità e la chiamerei metabolismo.
  L'esperimento deve essere **appaiato per stadio di differenziamento**, non per età di coltura —
  per esempio normalizzando su marcatori di maturazione, o confrontando popolazioni cellulari
  ordinate anziché organoidi interi. Senza quel controllo, un risultato positivo non
  discriminerebbe le due ipotesi.

- **Che cosa lo falsificherebbe (a favore di `DL-MECH-034`):** una firma OXPHOS↓/glicolisi↑ che
  persista **dopo** appaiamento per stadio; oppure la stessa firma in un sistema WWOX-carente
  *senza* difetto di differenziamento — che è precisamente ciò che i MEF e i modelli oncologici
  di `DL-MECH-020` offrono, e che rende quel corpus più probante di quanto la voce attuale lasci
  intendere, non meno.

- 🔴 **Nota di provenienza, e non è secondaria.** `DL-MECH-034` dichiara *«full text letto
  integralmente»*. **Il ledger delle ricevute non lo sostiene:** l'unica ricevuta per
  `PMID 34268881` è `FTR-20260726-34268881-01`, `partial_fulltext_read`, con `source_locator`
  che punta al **paper registry**, **nessuna impronta** e tutti gli slot a `unknown_legacy` —
  una delle ventitré ricostruzioni del 26 luglio. La superficie strutturata (`PMC8350905`, CC BY)
  **esisteva e non era stata recuperata**; l'ho recuperata in questa sessione. Le due citazioni
  qui sopra sono le prime di questo paper verificate contro un artefatto impronta-to.

- **Interconnessioni:** `DL-MECH-034` · `DL-MECH-020` · `DL-BIO-008` · `DL-BIO-085` · `FT-059` ·
  [[therapeutic_hypotheses_ledger_current#HYP-20260709-01]] · [[meta_metabolism_current]].
- **Destinazione dichiarata:** **materiale per un commit candidate**, come qualificazione di
  `DL-MECH-034` e come **correzione dell'esperimento discriminante**. Non tocca il verso della
  conclusione: tocca ciò che serve per stabilirlo.

---

### 🔴 DL-THER-095 — ITCH **alza** l'abbondanza di WWOX, e nessun file canonico lo dice: `DIS-003` ha una maniglia a valle che non ha mai nominato

- **Status:** open · **Tag epistemico:** `DATO` sulle misure di Abu-Odeh 2014, `INFERENZA` sulla
  convergenza terapeutica.
- **Fonte:** `PMID 24550385` — Abu-Odeh et al. 2014, *J Biol Chem* 289(13):8865-8880. Letto il
  2026-08-10, receipt `FTR-20260810-24550385-01` (`partial_fulltext_read`: testo integrale,
  pannelli non ispezionati), manifest `PMID24550385.json`, 13 locator, `MANIFEST STRICT PASS`.
  **Prima lettura di questo paper in questo corpus dalla sua fonte primaria.**

- ✅ **Cosa lo stato sapeva già** — e va detto per primo, perché è la terza volta stasera. Il
  linkage e il sito ci sono: `DEFAULTS THAT BIT US` porta `D-01` *«polyubiquitination →
  proteasome»* come default falsificato, e `DIS-001` è stato riaperto esattamente su questa
  biologia, con la nota corretta che **inibire ITCH sarebbe sbagliato** (si toglierebbe a WWOX
  la funzione DDR via ATM; ITCH è promiscuo, i topi `Itch⁻/⁻` sono autoimmuni).

- 🔴 **Cosa non c'è: il segno.** *(Titolo corretto in append — vedi la nota in fondo alla voce:
  la prima stesura diceva «in nessuno dei 18 punti in cui ITCH compare» e «tutte le menzioni»,
  e nessuna delle due misure era quella che dichiarava di essere.)* Le tre misure, dalla fonte
  primaria:

  | esperimento | risultato, verbatim |
  |---|---|
  | CHX chase, sovraespressione | *«Expression of ITCH in the presence of CHX **extended the half-life** of WWOX as compared with CHX alone»* |
  | MEF `Itch⁻/⁻`, livelli | *«We found that WWOX levels were **decreased** in Itch[⁻/⁻] mouse embryonic fibroblasts»* |
  | MEF `Itch⁻/⁻`, emivita | *«WWOX **half-life is shorter** in the absence of ITCH»*, p < 0.001 |
  | inquadramento degli autori | *«ITCH ubiquitinates WWOX **independent of degradation**»* · *«coexpression of WWOX and ITCH **stabilizes** WWOX levels»* |

  Guadagno **e** perdita di funzione, per livello **e** per emivita, in cellule non trasfettate
  per la metà delle misure. Non è un artefatto da sovraespressione.

- 🔴 **La conseguenza, ed è il motivo per cui questa voce è `DL-THER` e non `DL-MECH`.**
  `DIS-003` — *«Boosting WWOX expression» → REJECTION THAT HOLDS* — rifiuta di alzare
  trascrizione/traduzione **perché il collo di bottiglia è a valle**. Ma «a valle» non è un
  luogo vuoto: **l'ubiquitinazione K63 mediata da ITCH è una maniglia a valle sull'abbondanza di
  WWOX**, cioè precisamente il ramo che quel rifiuto lascia aperto e non nomina.

- **`PREMISE_TAG`:** `PREMISE: DATO` sulle tre misure (fonte primaria, letta, citazioni
  verificate contro artefatto impronta-to) · `PREMISE: INFERENZA` sul trasferimento al genotipo
  di riferimento, che **non è dimostrato**: Abu-Odeh lavora su WWOX wild-type in HEK293 e MEF,
  non su Q230P, e non testa se un allele destabilizzato risponda alla stessa via.

- 🔴 **La convergenza, che è la parte operativa.** Se ITCH sia una leva per il genotipo di
  riferimento dipende dalla disgiunzione che `DL-META-091` non ha potuto risolvere:

  > **degradazione prematura → una leva stabilizzante è on-target · traduzione impedita → non
  > c'è niente da stabilizzare.**

  Quindi **il western che discrimina traduzione da degradazione su fibroblasti Q230P decide
  anche se ITCH è una leva.** È lo stesso recupero già indicato come il più redditizio della
  coda — il PDF di Johannsen, `PMID 29808465`, closed access. **Due premesse aperte, una sola
  misura.** Un esperimento che risolve due voci del ledger vale più di due che ne risolvono una
  ciascuna, ed è la ragione per cui questa convergenza va scritta e non lasciata implicita.

- **Cosa NON si propone.** Non inibire ITCH — `DIS-001` ha già ragione su questo. E non si
  propone *nulla* come candidato terapeutico: la direzione plausibile sarebbe **aumentare** o
  mimare l'ubiquitinazione K63 su WWOX, che oggi non ha un agente, non ha un readout proximale
  e non ha dati CNS/pediatrici. Resta ipotesi nei ledger, come impone `mission.md`.
- **`REVIVAL_TRIGGER` / condizione di chiusura:** ① il western che discrimina i due rami su
  Q230P; ② una misura di abbondanza di WWOX-Q230P in funzione dell'attività di ITCH, che è
  l'esperimento che trasferisce — o no — Abu-Odeh al genotipo di riferimento.
- **Interconnessioni:** `DL-MECH-083` (premessa chiusa) · `DL-META-091` · `DIS-001` · `DIS-003` ·
  `D-01` in [[dismissal_ledger_current#DEFAULTS THAT BIT US]] · `FT-060` · `FT-057`.
- **Destinazione dichiarata:** **materiale per un commit candidate.** Tocca un rifiuto canonico
  (`DIS-003`) aggiungendogli un ramo che non nomina, quindi la promozione è di chi possiede il
  gate.

#### 🔴 AGGIUNTA 2026-08-11 — il corollario sulla NON-SELETTIVITÀ è `NON ANCORATO`, e lo dichiaro io prima che lo trovi qualcun altro

Da `PMID 23370280`, letto l'11 agosto, era emerso il corollario:

> **alzare l'attività di ITCH per stabilizzare WWOX aumenterebbe insieme la degradazione
> ITCH-mediata dei suoi altri bersagli — ΔNp63α e p73. Una leva su ITCH non è selettiva per
> WWOX.**

Poggia sul **frame di competizione WW1** — WWOX che compete con altre proteine WW per bersagli
PY comuni — che `23370280` cita come già stabilito e la cui **fonte primaria è `PMID 16061658`**
(Aqeilan 2005, WWOX e YAP competono per ErbB-4).

🔴 **Quella fonte oggi non può portare una citazione verificabile.** Screening dell'11 agosto,
receipt `FTR-20260811-16061658-01`, `retrieved_not_read`: nessun deposito PMC, nessuna copia in
repository, e il text layer del PDF locale è **`SUSPECT`** — `µ` diventa `A` sedici volte,
**`p73β` diventa `p73h` sette volte**, `×` è un byte di controllo. Superficie **rifiutata**, non
riparata.

**La classificazione esatta è `NON ANCORATO`, e non è né `rifiutato` né `confermato`:**

| stato | significato |
|---|---|
| confermato | esiste un locator verificato che lo sostiene |
| **non ancorato** | **la proposizione resta plausibile e non esiste oggi un locator che possa sostenerla** |
| rifiutato | esiste evidenza contraria |

Il corollario **non è sbagliato**: `23370280` lo enuncia in proprio (*«WWOX can compete with
other WW domain-containing proteins, like YAP and ITCH, for binding common target proteins, such
as ErbB4 and p73»*, verificato contro artefatto impronta-to) e quella citazione **è** ancorata.
Ciò che non è ancorato è la **fonte del frame**, cioè la dimostrazione originale che la
competizione avviene davvero al WW1. Chi userà il corollario deve sapere che poggia su una
citazione secondaria.

- **Cosa lo ancorerebbe:** ① aggiudicazione di pagina su `16061658` secondo la 5e — decisione
  dell'operatore, oggi **fuori mandato e non revocata**, e quindi non presa; oppure ②
  `PMID 12514174` (Chang 2003, JNK1/WOX1), che il preflight dell'11 agosto trova **open access
  ibrido con PDF all'editore** — ma è un PDF JBC del 2003, coetaneo di quello appena rifiutato, e
  va **schermato prima** di essere considerato una lettura.
- 🔴 **Cosa NON lo ancorerebbe, e va detto perché era il candidato indicato:** `PMID 18487609`
  (Aqeilan 2008, sopravvivenza postnatale e metabolismo osseo). Il suo HTML PMC locale è una
  superficie **pulita e leggibile** — 67 363 caratteri, `×` 10 · `α` 3 · `β` 5, zero controlli
  C0 — ma il paper **non contiene il frame**: `WW1` 0 · `ITCH` 0 · `competition` 0 · `ErbB` 2.
  **Chiude il gate multi-hop di `FT-062`; non ancora questa inferenza.** Le due cose sono state
  confuse una volta e non devono esserlo di nuovo.

Avevo scritto: *«ITCH compare **18 volte** e **ogni** menzione lo tratta come qualcosa da
inibire»*. Entrambe le metà sono difettose e in modi diversi.

- **Il 18 erano righe, non occorrenze**, e su quattro file scelti da me. Misurato sull'intero
  `disease-models/wwox/`: **175 occorrenze in 24 file** — che però includono i seed del corpus,
  i log e il manifest che ho appena scritto io, cioè cose che non sono affermazioni dello stato.
  L'Orchestratore ne ha misurate 46 in 101 file. **Tre numeri, tre strumenti, nessuno
  riproducibile** — la stessa forma del «6,5× contro 4,7×» di stamattina.
- **«Ogni menzione» era una generalizzazione che non avevo verificato**, e non potevo: non le
  avevo lette tutte. Lo stato porta almeno una cautela esplicita, nel paper registry:
  *«meccanismi di degradazione **regolata**, non controllo-qualità di proteina misfolded: **non
  assumere** che inibire ACK1/ITCH salvi Q230P»*, e `DIS-001` dice la stessa cosa meglio.

🔴 **Ma la proposizione che conta sopravvive, e ora è testata invece che contata.** Ho cercato
nello stato una frase che desse la **direzione** — ITCH che *aumenta* l'abbondanza o l'emivita
di WWOX — e **ogni singolo riscontro è testo scritto da me stasera** (`FT-060` e questa voce).
L'unico altro riscontro parla della stabilizzazione di WW1 da parte di un'altra interazione, non
di ITCH.

**E le due proposizioni non sono la stessa:** *«non assumere che inibire aiuti»* è **agnostica**;
*«inibire plausibilmente danneggia, perché ITCH allunga l'emivita di WWOX»* ha un **segno**. La
cautela già presente non poteva dire la seconda, perché il segno non era noto qui.

**La lezione non è "verifica di più prima di allarmarti" — è che l'allarme e il reperto vanno
separati nel testo, perché è il titolo che viaggia.** Un conteggio nel titolo invita a
controllare il conteggio; la proposizione sostanziale sta sotto e sopravvive. Terza volta
stasera che arrivo con un titolo troppo forte su un nucleo che regge — Johannsen, Steinberg,
questa. Le tre correzioni restano accanto ai rispettivi reperti invece di essere cancellate.
