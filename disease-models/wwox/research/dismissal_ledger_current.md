# Dismissal Ledger — NEGATIVES are claims

> **Research layer — non-canonical, append-only. Read-only toward the canonical files.**
> A worked example of the epistemic discipline for premises and rejections.

---

## Why it exists

LEGEND has a refined epistemic discipline — `DATO` / `INFERENZA` / `IPOTESI` / `ESPANSIONE` — and **applies it only to positive assertions.**

**It had no discipline for:**
1. **PREMISES** — the things claims rest on;
2. **NEGATIVES** — the conclusions that close a door.

**The epistemic machine was one-sided. And a whole class of errors arose from that side.**

### The asymmetry that makes negatives the real danger

| | False **positive** | False **negative** |
|---|---|---|
| Fate | gets tested → **dies** | **nobody retests it** |
| Noise | makes noise | **silent** |
| Duration | short | **permanent** |
| Self-reinforcing | no | **yes** — once discarded, never revisited |

In a system that accumulates for months, **the false positive is a cost; the false negative is a compounding loss.** And tiers, gates, filters, `refuted`, *"do not assume that…"* are **all machinery that produces negatives.**

### The common form of the errors

**`P → C`, where C is a rejection, and P was never checked — because P was the "obvious" part.**

> **The most dangerous premises are the ones too obvious to write down.**
> Nobody annotates *"polyubiquitination leads to the proteasome"* as a claim to cite: it is background knowledge. And precisely for that reason it is never tagged, and therefore never verified.

---

## The two new obligations

### 1. `PREMISE_TAG` — premises get tagged
Every rejection (and every non-trivial conclusion) must **name its load-bearing premise** and tag it:

| Tag | Meaning |
|---|---|
| `PREMISE: DATO` | primary, citable source |
| `PREMISE: INFERENZA` | derived, declared |
| 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` | **background knowledge, not verified against the source** |

> 🔴 **A `DEFAULT_FROM_TEXTBOOK` is not a foundation: it is a RESEARCH TARGET.**
> If a conclusion rests on one, the conclusion is **provisional by construction** and goes into this ledger with a revival trigger.

### 2. `REVIVAL_TRIGGER` — nothing dies in silence
Every rejection declares **what would revive it**. If the trigger fires, the rejection reopens **automatically**, without waiting for someone to remember it.

### Re-audit rule (the loop that makes this compound)
**Every time a new mechanistic `DATO` arrives, this ledger is re-scanned** for rejections whose premise that datum touches. This is the step that turns self-correction into self-improvement.

---

## 🩸 DEFAULTS THAT BIT US

> The real compound artifact: textbook defaults that, in **this** domain, turned out **false**.
> **It grows. Consult it BEFORE discarding anything.**

| # | "Obvious" default | Why it is FALSE here | Cost |
|---|---|---|---|
| **D-01** | *polyubiquitination → proteasome* | Linkage and context matter. K48 chains commonly support proteasomal turnover; K63 chains are multifunctional and can participate in trafficking/selective autophagy. In the published P252A model, predominant K63 polyubiquitination co-occurred with mutant-selective HSC70 binding and lysosomal localization; the combined evidence supported a CMA interpretation, but did **not** establish that K63 alone enhanced HSC70 recognition. | Discarded a testable ACK1/ITCH cascade for days |
| **D-02** | *misfolded protein → ERAD → chemical chaperones (4-PBA/TUDCA)* | True **only for ER/secretory proteins**. **WWOX is cytosolic/mitochondrial** → the route is **CMA/lysosome**. Wrong compartment. | Two wrong candidate molecules in the ledger |
| **D-03** | *"it is a chaperone" → it helps folding* | **The sign depends on WHICH chaperone and WHICH route.** **HSC70 does not rescue: it delivers to the lysosome.** An HSP70 co-inducer (arimoclomol) could **accelerate** Q230P destruction. | Candidate proposed and withdrawn the same day |
| **D-04** | *stabilizing a protein restores its function* | In WWOX **stability and function are in TENSION**: stability is bought with **occlusion** (WW2 caps the WW1 groove), and occlusion is **anti-function**. P282A demonstrates it: **stable and completely inert**. | Design constraint on the stabilizer |
| **D-05** | *(meta)* *the code does what the documentation says* | The docs said *"ranking decides only reading order"*. The script **refused to download the full text** of the lowest class. **Implementation wins, silently.** | A paper unreadable for months |
| **D-06** | *(meta)* *the tool built for a problem is immune to that problem* | A helper written to find unread gold **filtered by tier** → could not find the very paper it was meant to surface. **`--all` was not "all".** | Records invisible even to the "show everything" flag |
| **D-14** | *a figure shows what its legend says it shows* | 🔴 In Wang 2012 (PMID 22193544) **both** the published supplementary legend **and** the main text describe Supplementary Figure A as the co-IP proving *"WWOX does not associate with Tau"*, stating *"anti-Tau was used to detect endogenous Tau"*. The image contains **no Tau blot at all**: its two panels are labelled **WWOX** and **GSK3β**, and the lower one shows a faint *positive* band in the HA-IP lane. **A caption is authored prose; a blot is data.** The paper's only evidence for that negative does not exist in the displayed data. | Would have registered a **false conflict** against `DL-MECH-019` and weakened a live mechanism on the strength of a caption. **Rule: a negative asserted by a figure must be verified in the figure IMAGE, never on caption authority — and this is strictly stronger than reading the text, because here text and caption agreed with each other and both were wrong.** Corollary: `figures: read` in a receipt must mean *images inspected*; see `captions_only` in [[fulltext_read_receipt]]. |
| **D-15** | *a secondary source correctly attributes what it cites* | 🔴 A review (PMC3139124) wrote *"…on different, with some overlapping, tau residues [75, 76]"* and, separately, *"the interaction of GSK-3β2 with tau is weaker [76]"*. This session extracted the sentence and attributed the **different-sites** claim to ref **76** (Saeki 2011). Reading Saeki 2011 in full: it measures **one site only, Ser396**, and never addresses site selectivity. The claim belongs to ref **75** (Mukai 2002, PMID 12065620), still unread. **A bracketed citation range is not an attribution map.** | Would have carried a mis-sourced premise into `DL-MECH-066` and into a safety argument about lithium. **Rule: when a secondary source cites `[a, b]` for a compound statement, you do not know which clause belongs to which reference — resolve the primary before propagating any clause of it.** Caught by the ordinary discipline of verifying the primary, but **one cycle late**: the misattribution had already been written to a ledger. |
| **D-16** | *(meta)* *the text I typed is the text that got written* | 🔴 Built a hash-chained ledger receipt with an **unquoted shell heredoc** (`<<JSON`) because one field needed `$FP` interpolation. Dropping the quotes to interpolate one variable also enabled **backtick command substitution**: `` `references` `` was executed as a command and silently deleted from the stored JSON. The receipt validated and chained — the JSON stayed well-formed, so **no check could see it**. Damage here was one cosmetic word; the same mechanism could have eaten a fingerprint or a coverage value. | **Rule: never construct append-only-ledger content through an unquoted heredoc. Use a quoted heredoc (`<<'JSON'`) or write the file with a file-writing tool, and inject variables in a separate step.** Corollary: an immutable store makes a silent write-boundary mutation permanent — **validity is not fidelity**, and a schema check cannot detect content that was mangled before it arrived. |
| **D-13** | *a high T accelerates the rare event without touching the reference* | 🔴 I chose **400 K** to accelerate helix breaking in the mutant. But 400 K **melted the helix in the WT too** — during equilibration, before production (WT H-bond occupancy already at 0.06 in the first 10%, vs **0.81** on the folded helix). All 4 systems at the floor (0.02–0.04) → no dynamic range → 12 runs for an `INCONCLUSIVE`. | **Rule: before committing the full compute budget to a screen, spend the cost of ONE run on the cheapest control and verify the observable has dynamic range (the stable reference must stay stable). A destabilizing condition must not also destabilize what is stable by definition.** |
| **D-12** | *small distance between two residues ⇒ they interact* | 🔴 **False if they are close in SEQUENCE.** Minimum atom-atom distance returns the *backbone* — and for adjacent residues returns **covalent bonds**. A *"P282A at 1.3 Å from the catalytic triad"* was **the length of a bond** with S281. A *"C299R at 3.4 Å"* was backbone: the true side-chain distance is **9.4 Å**. | Built an entire **two-route model** and *"the most discriminating test we have"* on a measurement artifact. **Rule: function is about SIDE CHAINS (the atoms doing chemistry), not atom-atom minima. If two residues are ≤2 apart in sequence, any small distance is suspect by construction.** ⚠️ Worse: **the tool to catch it was available and unused.** |
| **D-11** | *(meta)* *adding a safeguard reduces risk* | 🔴 Added **intra-run checkpointing** to avoid losing an interrupted simulation. It bit **twice** in two days: first a non-existent `append` (a whole run lost after 17 min), then a *particle-count mismatch* (an OpenMM checkpoint is tied to the exact system, but re-solvating from scratch each launch → different water count → resume impossible). The insurance cost more than what it insured. | **Removed.** The resume that actually matters — at *whole-run* level, skipping completed ones — already worked and is trivial. **Rule: a robustness mechanism is not free; it has its own bug surface. If its complexity exceeds the damage it prevents, it is a net risk.** |
| **D-10** | *(meta)* *reviewing code is equivalent to testing it* | 🔴 Wrote checkpointing and left it **unverified**. Later tested the *mechanism* (`loadCheckpoint`) and **reviewed** the wrapper, declaring it correct. **But review could not see that `MDTrajDCDReporter(append=...)` does not exist.** On launch, the run failed **after 17 min of equilibration** on exactly that line. | A whole run wasted. **Rule: review finds LOGIC errors; only execution finds API/signature errors. A "mechanism" test that does not exercise the line that can break is not a test of that line.** Corollary: build the objects that can fail **before** the expensive phases (fail-fast). |
| **D-09** | *(meta)* *a performance drop is a software problem* | 🔴 **It was the charger unplugged.** MD collapsed from **58 to 6.8 ns/day** (9×, suddenly) because the machine had switched **to battery**: on Apple Silicon the GPU is throttled under sustained load. **I blamed, in order: reporter I/O, OpenCL, thermal throttling, implicit solvent.** Rewrote the script twice, changed configuration three times. **None of my hypotheses looked outside the software.** | Hours lost. **Rule: facing a performance drop, look FIRST at the physical state of the machine (power, battery, temperature, contention), THEN at the code.** A sharp cliff is hardware; a gradual decay is software. |
| **D-08** | *(meta)* *a GPU benchmark measures execution time* | 🔴 **On GPU `sim.step(n)` is ASYNCHRONOUS**: OpenMM queues the work and returns immediately. A benchmark that stops the clock **without forcing a sync** (`getState`) measures **queueing** time, not execution. My benchmark reported **35,000 ns/day** for implicit solvent; production reality is **43**. Explicit water measured correctly **only by luck**: the barostat forces a sync every 25 steps. | Chose the **worst** configuration believing it 500× better. **Rule: a GPU benchmark without a forced sync is a phantom number.** |
| **D-07** | *(meta)* *"the tool is not installed" → "it cannot be done"* | Wrote *"MD is not runnable here"* after verifying GROMACS and OpenMM **were not installed**. **I did not try to install them.** A later pilot ran fine (OpenMM + PDBFixer + OpenCL). **I produced a false negative on the very day I was building the discipline to eradicate them.** | MD stalled a cycle. Worse: **"not feasible" is the most seductive form of rejection**, because it looks like a technical fact and not a choice. |

---

## Active rejections

*(Wikilinks below point to the private discovery ledger, which is not part of the public edition; they are kept as narrative pointers.)*

### DIS-001 — «Inhibiting ACK1/ITCH will not rescue Q230P» → 🔄 **REOPENED**
- **Original rejection:** *"these are mechanisms of **regulated** degradation (phosphorylation → ubiquitination), **not** ERAD/chaperone quality control, which is different. → Do not assume that inhibiting ACK1/ITCH rescues Q230P."*
- **Load-bearing premise:** that this route ends in the **proteasome**. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` → **D-01**
- **Verdict:** the **reasoning was correct**; the **premise was false**. K63 linkage is not a proteasome-specific signal. K63 chains can contribute to CMA for particular substrates (demonstrated for HIF1A), and K63 polyubiquitination co-occurs with HSC70 binding and lysosomal routing in the published WWOX P252A model. Whether ITCH-dependent K63 chains causally enhance HSC70 recognition in that model—and whether any of it transfers to Q230P—remains to be tested.
- **Outcome:** reopened. **But not as a therapeutic target** (inhibiting ITCH would strip WWOX of its DDR function via ATM; ITCH is promiscuous → autoimmunity in *Itch−/−* mice): **as an experimental probe**, including the double mutant **Q230P+Y287F**.

### DIS-002 — «Oncology papers are background for this disease» → ❌ **FALSE, REVERSED**
- **Load-bearing premise:** that relevance follows the **disease phenotype**. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK`
- **Verdict:** reversed. WWOX **was born a tumor suppressor**: folding, stability, degradation routes, partners were characterized by **cancer research**. Of the papers that produced key commit candidates in this domain, **none was on WOREE** (thyroid, prostate, leukemia).
- **Outcome:** the **parity of sources** principle; the `DOMAIN_PARITY` rule.

### DIS-003 — «Boosting WWOX expression» → ✅ **REJECTION THAT HOLDS**
- **Rejection:** increasing transcription/translation does not help.
- **Load-bearing premise:** Johannsen 2018 — **normal transcript, protein absent** in fibroblasts homozygous for Gln230. ✅ `PREMISE: DATO` (direct measurement, exact variant)
- **Verdict:** **holds.** The premise is an experimental datum, not a default. The bottleneck is downstream.
- **`REVIVAL_TRIGGER`:** if it emerged that a **compound-heterozygous** transcript behaves differently from the Johannsen homozygote.

### DIS-004 — «4-PBA / TUDCA are the right chaperones» → ❌ **WITHDRAWN**
- **Load-bearing premise:** that a misfolded protein is treated with ER chemical chaperones. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` → **D-02**
- **Verdict:** wrong compartment (WWOX is cytosolic; the route is CMA/lysosome).
- **`REVIVAL_TRIGGER`:** 4-PBA is **also an HDAC inhibitor** → could act as an **HSP co-inducer**, a different mechanism. If the lysosomal arm confirms CMA, **re-evaluate 4-PBA on that basis**, not the ER one. **It is not dead: the rationale is dead.**

### DIS-005 — «PMID 25703206 (allostery) gives the rationale for the SDR stabilizer» → ❌ **DOES NOT HOLD (but yields something else)**
- **My load-bearing premise:** that "allostery + conformational switch in WWOX" concerned the **SDR fold**. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` (inferred from **title/abstract**, not the text)
- **Verdict:** the paper concerns **entirely residues 1–91** (WW1-WW2 modules). **The SDR is not even in the constructs.** Wrong domain.
- **But:** it yields **D-04** — a **design constraint** more useful than the rationale I was looking for.
- **Lesson:** *a relevance prediction is also a premise, and must be verified against the text.* The right rejection **comes after reading, never in its place.**

### DIS-006 — «Whether a folded *and* active state for Q230P is reachable is **not resolvable in silico**» → 🔄 **REOPENED — by the re-audit rule**
- **Original rejection:** *"a proline buried in an α-helix imposes a backbone constraint a chaperone cannot remove… **Not resolvable in silico.**"*
- **Load-bearing premise:** that *"in silico"* means **ΔΔG + static structure**. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK`
- **What reopened it:** a mechanism (Zhang) **changes the question**. No longer *"can Q230P fold?"* (thermodynamics, hard) but **"does Q230P expose the KFERQ-like motif LRSVQ (187–191)?"** — which is **dynamics**, and is **tractable**.
- **Immediate outcome:** the motif is **cryptic** (anchors L187/V190 buried, relSASA 0.000) and **Q230 packs against it at 3.9 Å** — **5× closer than P252A (20.6 Å)**, the variant on which the mechanism is *demonstrated*.
- **`REVIVAL_TRIGGER` already fired.** The rejection **still holds** in its original form (the "folded *and* active" question stays open), but **no longer blocks the program**: the decisive sub-question is now attackable.
- **Next step, well posed:** **MD (GROMACS), WT vs Q230P**, measuring **SASA and RMSF of residues 187–191**.
- **Lesson:** *"not resolvable in silico" is not a property of the world: it is a property of the question you are asking.* Change the question, and in-silico becomes decisive again. **This rejection was correct for the old question, and wrong for the new one.**

### DIS-007 — «C299R is a CATALYTIC lesion and the decisive off-lid control» → ❌ **WITHDRAWN: the measurement was wrong**
- **Assertion:** C299 sits **3.4 Å** from the catalytic triad → a catalysis lesion, not folding → an **off-lid control** that decides the lid model. I had called it *"the cheapest and most discriminating test we have"*.
- **Load-bearing premise:** that *"two atoms at 3.4 Å ⇒ the residues interact functionally"*. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK`
- **Why it is false:** I measured the **minimum atom-atom distance of any kind**. For residues **close in sequence** this returns *backbone* proximity — or, at 1.3 Å, a **covalent bond**. C299 is two residues from K297: those 3.4 Å were backbone. **True side-chain → functional-atom distance: 9.4 Å** (SG–NZ 10.7 Å).
- **And it was the opposite of an off-lid control:** **C299 contacts H233 at 3.4 Å**, and **H233 is inside the lid-helix 226–251**. The residue I sold as an independent control **touches the lid**.
- **What falls with it:** the **two-route model** (degradation vs catalysis) rested entirely on this → **superseded**. And the dossier's P1 prediction → withdrawn.
- **What survives:** the human `DATO` (Johannsen) is **normal transcript + protein not detected** — an observation, not a prediction. 🔴 **What does *not* survive (repair 2026-07-14):** calling it *a degradation lesion*. The source declares **impaired translation** *or* premature degradation and does not discriminate; insolubility is a third route. **The cause remains unresolved.** And the geometry of Q230 (7.3 Å from the triad, relSASA 0.000, in contact with the KFERQ anchors) **holds on re-measurement**: Q230 is far from the triad in sequence, so no artifact.
- **Collateral error found:** *"P282A at 1.3 Å from the triad"* → **4.9 Å**. 1.3 Å was a **covalent bond** with adjacent S281.
- **Collateral error that goes AGAINST me:** the lid-helix is not 6.8 Å from the triad but **3.5 Å** (E226 ↔ S281 OG). The `D-04` design constraint is **stricter**, not looser.
- **`REVIVAL_TRIGGER`:** a **validated** exemplar of a WWOX catalytic lesion (measured on side chains, with functional data) would reopen the two-route model. Today we have none.
- **Merit:** found by the **parallel session**, not by me. Two heads checking each other — the false negative died before costing a real experiment.

### DIS-008 — «La calpaina è una via di degradazione/turnover per WWOX» → ⏸️ **NON STABILITA (rigettata come affermazione, non come possibilità)**
- **Chi la afferma:** Saadane et al. 2021, PMID 34214506 — *«Wwox was identified as a substrate for calpain»*, e in Figura 10 l'arco calpaina→WWOX è disegnato come **linea continua**, che la loro stessa legenda definisce *via confermata*.
- **Load-bearing premise:** che una proteasi che regola l'abbondanza di una proteina la tagli. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` → stessa famiglia di **D-01** (polyUb→proteasoma).
- **Verdetto:** nessuna proteolisi è mai stata misurata su WWOX in questo lavoro — nessun saggio di taglio, nessun frammento, nessuno shift di peso. Le sole misure sono **abbondanza** (LFQ) e **trascritto** (qRT-PCR). Peggio, la direzione è invertita per un substrato: la calpaina sale **e WWOX sale**; e sale l'**mRNA**, cosa che una proteasi non può causare. Una via più parsimoniosa è nella loro stessa discussione: calpaina degrada IκBα fuori dal sistema ubiquitina-proteasoma; WWOX lega IκBα; quindi calpaina→NF-κB→**trascrizione** di `Wwox` spiega tutto senza toccare WWOX.
- **Cosa NON viene rigettato:** che la calpaina possa essere una quarta via di turnover di WWOX accanto a proteasoma, CMA e macroautofagia. Resta **aperta e non testata**. È rigettata l'*affermazione*, non l'ipotesi.
- **`REVIVAL_TRIGGER`:** uno qualsiasi fra — (a) frammento di taglio di WWOX dimostrato su attivazione calpainica; (b) digestione in vitro di WWOX ricombinante con calpaina; (c) sito di taglio calpainico mappato su WWOX; (d) proteina WWOX in calo con mRNA tenuto costante sotto attivazione calpainica.
- **Gancio di ri-audit:** rigetto di **via di turnover**. Da riesaminare a ogni nuovo `DATO` meccanicistico sulla degradazione di WWOX (proteasoma, CMA, macroautofagia, calpaina), per la regola di ri-audit.
- **Contesto che spiega l'errore, senza scusarlo:** il gruppo ha 207 lavori, 140 sulla retinopatia diabetica e **1 su WWOX** (questo). L'hit proteomico è non guidato — quindi l'osservazione è forte; l'etichetta meccanicistica è da manuale — quindi l'interpretazione è debole. Le due cose si pesano separatamente.

### DIS-009 — «Un WWOX-mimetico (WWOXtide³⁸⁸⁻⁴⁰⁷) sarebbe più sicuro del litio, perché WWOX inibisce GSK3β in modo substrato-selettivo» → ❌ **RIGETTATA**
- **Chi la avrebbe affermata:** questa sessione, ragionando su PMID 22193544 (`PAPER 056`, proposto in `CC-20260726-003`). L'argomento era attraente: in cellula WWOX abbatte pTau S396/S404 **senza toccare** β-catenina e fosfo-β-catenina (Fig 1b/c), quindi sembrava un inibitore mirato là dove il litio è globale.
- **Load-bearing premise:** che la selettività osservata in cellula sia una **proprietà dell'interazione** WWOX–GSK3β. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — generalizzazione di un risultato cellulare all'interazione biochimica, la stessa famiglia di **D-01**.
- **Verdetto: falsa.** La **Supplementary Figure C** dello stesso paper mostra che WWOX inibisce la fosforilazione GSK3β-dipendente di **GS-1**, peptide derivato dalla glicogeno-sintasi e senza alcuna relazione con Tau, portandola a ⌀18% del controllo (L404A ⌀87%). L'interazione è un **blocco generico del sito di docking** Axin/FRAT/GSKIP, non una selettività di substrato. Il risparmio di β-catenina in cellula si spiega più parsimoniosamente con **segregazione di pool** (la quota di GSK3β scaffoldata da Axin resta protetta) o con stechiometria endogena sub-saturante — mai misurata nel lavoro.
- **Cosa NON viene rigettato:** che una molecola *pool-selettiva* possa esistere. È rigettato l'argomento di sicurezza «è selettivo per costruzione», non l'obiettivo.
- **Conseguenza operativa:** su [[therapeutic_strategies_current#TX-005 — Repurposing: lithium / GSK3β (and other nodes)|TX-005]] il razionale meccanicistico si rafforza (si perde un freno fisico, non solo un livello) ma **il punteggio SAFETY non migliora**. Un peptide WWOX-mimetico **non è** una variante più sicura di TX-005.
- **`REVIVAL_TRIGGER`:** (a) dose-risposta in cellula che mostri il pool Axin-scaffoldato genuinamente risparmiato a stechiometria fisiologica — reporter TCF/LEF piatto mentre pTau scende; oppure (b) un analogo di WWOXtide ingegnerizzato per selettività di pool con selettività dimostrata; oppure (c) la scoperta che l'arco rilevante passi per l'**isoforma GSK3β2 neurone-specifica** (PMID 20067585, [[full_text_queue_current#FT-022]]), che avrebbe preferenza di substrato diversa — in quel caso la selettività tornerebbe possibile, ma per un motivo del tutto diverso da quello rigettato qui.
- **Gancio di ri-audit:** rigetto di **selettività farmacologica**. Da riesaminare a ogni nuovo `DATO` su isoforme di GSK3β, scaffold, o stechiometria WWOX:GSK3β.

> #### 🟢 `REVIVAL_TRIGGER (c)` — **SCATTATO lo stesso giorno, alla lettura successiva**
> Il trigger (c) era scritto così: *«la scoperta che l'arco rilevante passi per l'isoforma
> GSK3β2 neurone-specifica (PMID 20067585) — in quel caso la selettività tornerebbe possibile,
> ma per un motivo del tutto diverso da quello rigettato qui»*. **È esattamente quello che è
> accaduto**, alla prima lettura successiva (`FT-022`, ricevuta `FTR-20260726-20067585-01`,
> `abstract_only`).
>
> **Cosa dice la fonte**: GSK-3 sono tre enzimi; **Axin si associa più facilmente a β1 che a
> β2**; e gli autori concludono che *«GSK-3 inhibitors that target the Axin-binding site in
> GSK-3 will preserve the beneficial effects of GSK-3β2 on axon growth»*. **WWOX lega
> precisamente quel sito** (PMID 22193544).
>
> **Il rigetto RESTA VALIDO COME FORMULATO.** WWOX **non** è substrato-selettivo: la Suppl.
> Fig. C che inibisce GS-1 all'82% non è stata smentita da nulla. Chi affermasse oggi
> «è selettivo per tau» sbaglierebbe ancora.
>
> **Ciò che si apre è un'affermazione DIVERSA**, che non era sul tavolo: **selettività di
> ISOFORMA per occupazione del sito di Axin**, non selettività di substrato. Filata a parte
> come `DL-MECH-067` con la sua premessa portante esposta (che il legame al sito di Axin
> conferisca preferenza per β1 è `PREMISE: INFERENZA`, mai misurato su WWOX) e il suo
> esperimento decisivo (WWOX e WWOXtide contro β1 vs β2 in parallelo).
>
> **Perché vale la pena annotarlo qui e non solo nel discovery ledger**: è la prova che il
> meccanismo funziona come progettato. Il trigger non è stato ricordato da qualcuno — era
> **scritto**, e la lettura successiva lo ha fatto scattare. Senza di esso, il rigetto di
> `DIS-009` avrebbe chiuso silenziosamente una porta che si è riaperta in poche ore, su un
> asse diverso. **Distinguere *quale* affermazione è morta da *quale* è solo diversa è tutto
> il valore di questo ledger.**

### DIS-010 — «WWOX non lega Tau (Wang 2012)» → ⏸️ **NON STABILITA — il negativo è rifiutato per assenza di dato**
- *Rigetto di un rigetto. Il negativo non può entrare nel modello.*
- **Chi lo afferma:** Wang et al. 2012, PMID 22193544, nel testo — *«Tau was not co-immunoprecipitated in the complex (Supplementary Figure A), indicating that WWOX does not stably interact with Tau in SH-SY5Y cells»* — e nella legenda supplementare pubblicata, che dichiara *«anti-Tau was used to detect endogenous Tau protein»*.
- **Load-bearing premise:** che la Supplementary Figure A contenga un blot anti-Tau, perché testo e legenda lo dichiarano. 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` → **D-14**. Il "default da manuale" qui è la regola tacita più invisibile di tutte: *una didascalia descrive la propria figura*. Nessuno la scrive come premessa da verificare, ed è precisamente per questo che non viene mai verificata. **Non lo contiene.** I due pannelli sono etichettati **WWOX** e **GSK3β**; nel secondo si vede una banda debole ma presente nella corsia IP-HA, cioè un co-IP **positivo** di GSK3β, coerente con Fig 2c. Nessun blot Tau è mostrato. Vedi **D-14**.
- **Verdetto:** **non valutabile.** Non si può stabilire se si tratti di figura scambiata o etichette errate: il record pubblicato non lo permette. Di conseguenza l'arco *tau* di `DL-MECH-019` **non è contraddetto — è intatto**.
- **Perché conta più del singolo paper:** fidandosi del testo, LEGEND avrebbe registrato un `conflicting evidence` contro un meccanismo vivo, cioè **fabbricato un falso negativo** della specie peggiore — silenzioso, permanente, auto-rinforzante. È esattamente l'asimmetria descritta in cima a questo ledger. Il difetto è stato visto **solo** ispezionando il raster della figura supplementare.
- **Cosa NON viene rigettato:** che WWOX possa effettivamente non legare Tau in modo diretto e stabile. Resta **aperto e non testato da questo lavoro**. Nota che l'affermazione opposta (Chang/Sze) nasce da yeast two-hybrid, che ha i suoi falsi positivi: **nessuno dei due lati è solido**.
- **`REVIVAL_TRIGGER`:** (a) una Supplementary Figure A corretta da editore o autori; (b) un co-IP WWOX–Tau indipendente in sistema neuronale; (c) la lettura di [[full_text_queue_current#FT-024]] (PMID 15126504, Sze 2004), che è la controparte diretta della questione.
- **Gancio di ri-audit:** rigetto di **interazione proteina-proteina**. Da riesaminare a ogni nuovo `DATO` sull'interattoma SDR di WWOX.

### DIS-011 — «Il modello murino Wwox-null mostra epilettogenesi» → ❌ **RIGETTATA — la fonte terminale afferma il contrario**
- *Rigetto di una premessa che cinque superfici canoniche hanno portato per mesi.*
- **Chi lo afferma:** PMID 30290271 nel proprio testo, attribuendolo a PMID 19936220 e Mallaret 2014. Da lì era entrato in `CLAIM 005`, nel changelog del working model, nel dossier di PMID 30290271, nella session evaluation e in `DL-MECH-072`.
- **Load-bearing premise:** che PMID 19936220 avesse misurato l'epilettogenesi. 🔴 `PREMISE: INFERENZA` — una catena di citazioni a due salti mai verificata a nessuno dei due salti.
- **Verdetto:** **rigettata, e non per assenza di prova ma per prova contraria.** PMID 19936220 non contiene EEG, osservazione di crisi, test comportamentale o istologia cerebrale; l'unica misura cerebrale del paper è il peso dell'organo. Il termine entra una sola volta, come citazione in Discussione del ratto `lde`. E il terminale, PMID 19500159, dichiara in tre punti — e in una Table 2 la cui riga `Epilepsy` è **vuota per entrambi i modelli murini** — che i topi Wwox-null **non hanno epilessia riportata**.
- **Perché è sopravvissuta così a lungo:** la premessa co-citata nella stessa frase — la morte precoce — **era vera di prima mano** (43% a 72 h, 77% al giorno 17). Una clausola vera accanto a una falsa è la mimetizzazione. Nessun controllo esistente poteva prenderla: il ratchet delle premesse non lette chiede *se* una citazione sia stata letta, e questa era perfettamente leggibile.
- **Cosa NON viene rigettato:** che i topi Wwox-null **possano** convulsionare senza che sia stato osservato. Gli autori del terminale lo dichiarano irrisolto e offrono una spiegazione testabile: i topi potrebbero morire prima. La sopravvivenza la rende concreta — 2–3 settimane nel topo contro 3–12 nel ratto, con esordio più precoce delle crisi al giorno 16, già oltre l'intera vita del topo. **Il fenotipo epilettico del ratto non è in discussione:** vedi [[claim_registry_current#CLAIM 037]].
- **`REVIVAL_TRIGGER`:** (a) qualunque EEG o osservazione di crisi in un topo Wwox-null; (b) un modello condizionale che sopravviva oltre le 3 settimane e poi convulsioni; (c) stimolazione audiogena applicata al topo con lo stesso protocollo del ratto.
- **Gancio di ri-audit:** rigetto di **fenotipo per specie**. Da riesaminare a ogni nuovo `DATO` neurologico su un modello murino Wwox.

### DIS-012 — «Il nanismo del ratto *lde* è causato da GH ipofisario basso» → ❌ **RIGETTATA — la fonte citata riporta una differenza non significativa**
- *Rigetto di una citazione che ha preso l'abstract della propria fonte al posto del suo corpo.*
- **Chi lo afferma:** PMID 19500159 — *«The cause of severe dwarfism with retarded bone growth in lde/lde rats may be related, at least in part, to lower levels of pituitary growth hormone (Suzuki et al. 2007)»*.
- **Load-bearing premise:** che PMID 17803050 avesse dimostrato un GH ridotto. 🔴 `PREMISE: INFERENZA` — e la premessa nasce da una sovradichiarazione **interna alla fonte**.
- **Verdetto:** **rigettata.** PMID 17803050 riporta che *«although the plasma GH level was slightly lower in mutant than in normal rats, the difference was not significant»* e conclude *«the severe type of dwarfism observed in lde/lde rats cannot be explained solely by low levels of plasma GH»*. Le cellule GH-positive sono presenti e il GH ha peso molecolare normale. La Fig. 6C mostra barre d'errore ampiamente sovrapposte.
- 🔴 **Dove nasce l'errore, ed è il punto:** l'**abstract** di PMID 17803050 scrive *«as well as decreased concentrations of plasma growth hormone»*, **senza qualificazione**. L'abstract sovradichiara il proprio corpo, e il paper citante ha usato la versione dell'abstract. Verificato meccanicamente: quella frase risolve sulla superficie *abstract* e non sul *body* dell'artefatto.
- **Cosa NON viene rigettato:** che l'asse GH possa contribuire in qualche misura. Resta **non testato adeguatamente**: il campione è piccolo, e nessuno ha fatto un rescue con GH né misurato l'asse IGF-1. Gli autori argomentano soltanto che un GH plasmatico non elevato rende improbabile un modello tipo Laron da recettore.
- **Ciò che resta senza spiegazione:** la causa del nanismo `lde` è **ignota**. `WWOX AND "growth hormone"` restituisce **0** record PubMed.
- **`REVIVAL_TRIGGER`:** (a) un dosaggio GH adeguatamente potenziato; (b) un rescue con GH nel ratto `lde/lde`; (c) misura dell'asse IGF-1.
- **Gancio di ri-audit:** rigetto di **causa endocrina**. E gancio di metodo: da riesaminare ogni volta che una premessa citata compare come **frase breve e citabile** — è la firma di una citazione presa dall'abstract.
