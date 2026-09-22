# RESILIENCE NODE — the conditional-deletion ladder: which compartments tolerate cell-autonomous WWOX loss, and why?

**Node:** `COMPARTMENT_RESILIENCE_LADDER` · **Actor:** Scientist C · **Date:** 2026-09-22
**Status:** non-canonical analysis file. No canonical file edited, no registry written, no receipt
claimed, no commit, no git command run, no external contact made.
**Read-only toward every canonical file.**

> 🔴 **NOTHING IN THIS FILE IS MEDICAL ADVICE.** No molecule, class, dose, route, schedule or
> compound screen is named anywhere in it. A mechanistic hypothesis is not a treatment. No generic
> neuroprotection is proposed or implied.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is
> described and no contact detail of any living person is reproduced.
>
> 🔴 **Alleles, drivers and species are never pooled.** `Wwox`-null (Aqeilan strain),
> `Wwox^ΔCre/ΔCre` (EIIA-Cre, Aldaz strain), the NCKU nulls, `gt/gt` hypomorph, `P47T` knock-in,
> `P47R`, `G372R`, `Q230P`, Synapsin-Cre `S-KO`, Nestin-Cre `N-KO`, Olig2-Cre, GFAP-Cre, BK5-Cre,
> Alb-Cre `Wwox^hep−/−`, adipocyte-Cre, ACTA1 `Wwox^ΔSKM`, rat `lde/lde`, human WOREE and human
> SCAR12 are **different objects** and appear in different rows throughout.

---

## 0 · BASELINE — enumerated first, filtered second

**What was enumerated before any question was formed.** Plain `ls` of
`disease-models/wwox/analysis/` (**167 entries**, read end to end, including the four subdirectories
`data/`, `near_miss_cases/`, `orchestration_reviews/`, `scripts/`) and full recursive
`ls -R disease-models/wwox/research/` (**9 subdirectories**; 54 dossiers, 100 deepdive manifests,
117 commit candidates, 43 session evaluations). Only after the whole listing was read were greps
run.

**The seven files I was told already occupy this territory were read before anything was proposed,
and none is re-derived here:**

| File | What it settles | Consequence for this node |
|---|---|---|
| `resilience_and_modifier_census_20260921.md` | Modifier search across human outliers, discordant sibs, mouse strains, paralogue — **NEGATIVE**. No discordant sibling pair exists; mouse survival differences are confounded by allele, targeting, Cre driver and species; WWOX has no paralogue. `:142` records sex as *"not addressed as a modifier anywhere"* but logs the `lde` female-only audiogenic cohort as a **confound, not an effect** | 🔴 **Not re-run.** This node does **not** ask which *individual* or which *strain* is spared. It asks which **cell/tissue compartment** is spared — a question that census did not pose and its negative does not cover |
| `downstream_wwox_independent_rescue_census_20260921.md` | Bounded census of downstream rescue; four positive arms in the whole literature; the ethosuximide/SWD wave | Not reopened |
| `wwox_independent_downstream_rescue_20260922.md` | The **A–L node map**, the selectivity audit, outcome-width scoring, top three (G3, Tau polymer, Kir4.1/AQP4) | Used as the **occupancy map**. I propose no new row of it. §5 argues about how one existing row (**G1**) was scored, not about its mechanism |
| `new_discovery_node_20260922.md` | Subfield-selective vacuolation in the `lde/lde` hippocampus; H0–H6 + the H5a/H5b fork; E1–E5 | 🔴 **Not re-entered.** Its `E1`, `E2`, `E5` remain that file's, unnamed and unclaimed here |
| `lde_myelin_vacuole_bridge_20260922.md` | The bridge — **CANNOT BE ADJUDICATED FROM HELD MATERIAL**; regional surrogate runs against it; `H5a` weakened, `H5b` survives by non-elimination | Verdict accepted. §0.1 states why I did **not** take the operator's suggested restart |
| `mechanism_intervention_map.md` | M-nodes, N-/R- portfolio, the DEPRIORITIZE list (incl. **N-13 pro-myelinating**, **N-08 DCA**, **N-01 mTOR**, **N-14 antioxidants**) | Treated as closed. Nothing here re-proposes a deprioritised class |
| `earliest_lesion_developmental_timeline_20260921.md` | Earliest-lesion timeline; prenatal mapping not supportable; zero prenatal intervention in any WWOX model | Not re-derived |

**Also read before proposing:** `superior_node_search_20260922.md` (three whole-session node
searches already exist; `:74` records **pro-myelinating / OPC maturation** as *"already held and
rejected — wrong cell compartment, closing window"*), `next_node_scout_20260921_orchestrator.md`,
`scientist_node_scouting_20260920.md`, `DISCOVERY_TRACE_metabolic_gating_20260922.md` (self-graded
**REDISCOVERY**; its §7.4 question — *how does a CNS-only vector rescue a death with peripheral
components* — and its §7.5 experiment are **that file's and are not re-proposed**),
`wwox_myelin_oligodendrocyte_census_20260921.md`, `peripheral_phenotype_denominator_audit_20260922.md`,
`AUTONOMOUS_SESSION_STATE.md` (sixth block).

### 0.1 Why I did not restart from hypomyelination-alone or vacuolation-alone

The operator offered both as legitimate independent restarts. I declined both, for a stated reason
rather than a preference:

- **Hypomyelination alone** lands inside `wwox_independent_downstream_rescue_20260922.md` row **E**
  (`:103`) and `superior_node_search_20260922.md:74`, where the class is already **rejected on
  compartment** — *"the OPCs are present and not receiving the axonal signal"*. Reopening it
  without a new variable is re-derivation.
- **Vacuolation alone** is the whole object of `new_discovery_node_20260922.md`, whose H0 —
  *the sparing has never been counted* — is unresolved. A second file on the same unmeasured
  observation adds hypotheses to a table that is already seven rows long and gated on one count.

**What I took from the operator's framing instead** is its shape, not its two candidates: *a spared
compartment next to a failing one under comparable WWOX loss*. The repository holds that comparison
in a **cleaner** place than the hippocampus — in genetics, not in histology.

### 0.2 The gap the enumeration actually exposed

`grep` across every markdown file in `disease-models/wwox/`:

- **`FT-049` is developed in no analysis file anywhere.** It is registered at
  `research/full_text_queue_current.md:1404` as *"il tessuto di misura non è il tessuto di
  necessità"* — priority **ALTA**, epistemic status **`INFERENZA`**, three first-hand-read sources,
  and an explicit terminal note: *"Non può salire a `DATO` senza un esperimento che testi la
  dissociazione compartimento/necessità in modo diretto"*. **That experiment has never been
  designed.** Outside the queue, `FT-049` appears only as a pointer in
  `framework/state/state_manifest_current.md`, one dossier, one commit candidate, one session
  evaluation and one crosswalk — **never as the object of an analysis.**
- **No file in the repository assembles the conditional-deletion lines into a single vulnerability
  table.** `peripheral_phenotype_denominator_audit_20260922.md:18-22` lists the drivers, but as a
  **non-pooling firewall declaration**, explicitly so that they stay in *different rows*. Listing
  objects so they are never compared is the opposite of comparing them.
- **No file offers any explanation for the Olig2-Cre and GFAP-Cre negatives.** They are used
  everywhere as evidence *that* the myelin defect is non-cell-autonomous, and nowhere as a datum
  about the **oligodendrocyte's and astrocyte's own tolerance of WWOX loss**.
- 🎯 **Two first-hand-read data from `PMID 30755385` are used nowhere in the repository.** `soleus`,
  `soleo`, `EDL`, `slow-twitch` and `fibre lente` return **zero hits** outside that paper's own
  dossier. One of them is a within-animal WWOX-abundance-versus-vulnerability gradient — the
  scarcest kind of evidence this node needs.

**That is the node.** Not a new mechanism: a **comparison the repository has structurally forbidden
itself from making**, and which its own `FT-049` says must be made.

---

## 1 · THE OBSERVATION, STATED WITHOUT INTERPRETATION

**The ladder.** Every row is a *cell-autonomous* deletion of `Wwox` restricted to one compartment,
or a compartment-restricted restoration. 🔴 **No row is pooled with any other; each carries its own
driver, strain and endpoint set, and the endpoint sets are not the same.** That non-equivalence is
itself hypothesis `R5` in §2 and is not hidden.

| # | Compartment · driver | Outcome of cell-autonomous WWOX loss | Depth in LEGEND |
|---|---|---|---|
| **L1** | **Hepatocyte · Alb-Cre `Wwox^hep−/−`** | 🟢 **TOLERATES (for the measured endpoints).** Does **not** lower circulating HDL-C in either sex — the phenotype appears only in the whole-body null | 🟢 first-hand: `PMID 24871327`, `complete_fulltext_read`, receipt `FTR-20260810-24871327-01`, dossier `research/fulltext_dossiers/PMID24871327_locators.md` |
| **L2** | **Hepatocyte · Alb-Cre** (second study) | 🟢 **TOLERATES.** In a three-way comparison of hepatocyte, adipocyte and skeletal-muscle deletion, *"solo il KO muscolare altera GTT e peso"* | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:47` and `:67` (paper read in full, `reading_state.md:107`) |
| **L3** | **Adipocyte · adipocyte-Cre** | 🟡 **TOLERATES, weakly evidenced.** Same negative three-way comparison; the adipose negative is *"blot rappresentativo, `n=3`, risoluzione nativa bassa e nessuna quantificazione"* | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:97` and `:106-108` |
| **L4** | **Skeletal muscle · ACTA1-rtTA;tetO-Cre `Wwox^ΔSKM`** | 🔴 **FAILS.** Fasting hyperglycaemia, impaired GTT, weight gain; fat mass ↑ / lean mass ↓; HDL/LDL ↓, TG + cholesterol ↑; reduced `18F-FDG` uptake in gastrocnemius and hamstring; reduced mtDNA, Krebs-cycle transcripts and slow-twitch transcripts; reduced p-AMPK^Thr172^ and p-ACC; HIF1α, PKM2, PDK1, LDHA1, MCT4 up | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:67-81` |
| **L5** | 🎯 **Within L4 — fibre type** | **WWOX immunofluorescence is more intense in soleus than in EDL** (Fig. S4, read as pixels at 512 ppi), and what the knockout loses includes the **slow-twitch transcript programme** | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:96` and `:78` |
| **L6** | 🎯 **Within L4 — other organs of the same animal** | `18F-FDG` uptake *"non rilevato come diverso in cervello o fegato"* | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:72-73` |
| **L7** | **Neuron · Synapsin-Cre `S-KO`** | 🔴 **FAILS.** Spontaneous neocortical bursting, altered oscillatory organisation, ↑phase–amplitude coupling, ↑excitatory drive, ↓spontaneous inhibition | 🟢 `CLAIM 021` read directly, `registries/claim_registry_current.md:382-392` (source `PMID 34634460`, receipt on file) |
| **L8** | **Neuron · Synapsin-Cre; progenitor · Nestin-Cre** | 🔴 **FAILS.** Reproduce the phenotype **including the myelin defects** | 🟡 **SECOND-HAND — see §1.1.** `CLAIM 003`, `registries/claim_registry_current.md:67-79`; `PAPER 004` = `PMID 33914858` |
| **L9** | **Oligodendrocyte · Olig2-Cre; astrocyte · GFAP-Cre** | 🟢 **TOLERATE.** *"produces no evident abnormality"* | 🟡 **SECOND-HAND — see §1.1.** Recorded at `analysis/wwox_myelin_oligodendrocyte_census_20260921.md:36-42` and `analysis/wwox_independent_downstream_rescue_20260922.md:103` |
| **L10** | **Neuron-restricted *restoration* · AAV9-hSynI-WWOX** | Corrects **peripheral** phenotypes, hypoglycaemia included, with oligodendrocytes **never transduced** and myelin improving anyway; rescue **incomplete** against WT | 🟢 `CLAIM 004` read directly, `registries/claim_registry_current.md:84-100` (`PMID 34747138`, receipt `FTR-20260810-34747138-01`) |

### 1.1 🔴 UNDISCHARGED READING DEBT — declared before it is leaned on

**`PMID 33914858` (Repudi 2021, *Brain*) has NO read receipt in this repository.** It is declared in
the registry as `PAPER 004` (`registries/paper_registry_current.md:95-107`, status `integrated`), and
`CLAIM 003` is a `consolidated baseline` claim sourced to it — so citing the **claim** is legitimate.
But the **conditional-Cre content of rows L8 and L9 reaches LEGEND second-hand**, through another
paper's summary (Obeid 2026), as
`analysis/wwox_myelin_oligodendrocyte_census_20260921.md:36-42` states in terms: LEGEND holds that
result *"only second-hand"*, and the census's own remedy is to acquire the paper *"to verify the
attribution, not to learn the answer"*. The repository separately records that this PDF's text layer
is corrupted (`FT-044` suspended after *"P < 0.05"* extracted as *"P 5 0.05"*).

> 🔴 **Consequence, applied throughout and not softened:** **no conclusion in this file rests on L8
> or L9.** They appear in the ladder because omitting them would misrepresent the evidence, and every
> hypothesis in §2 is scored twice — once with them, once without — in §7.2. The node survives
> without them; it is *sharper* with them, and that sharpness is debt, not evidence.

### 1.2 Why this is worth a node at all

**Because the comparison is genetic, not histological.** Every other "why is this spared" question in
this repository — hippocampal subfield, cerebellar layer, Purkinje cell, regional myelin — rests on
reading an image. This one rests on **eight conditional alleles** in which an experimenter removed
the same gene from a named compartment and measured what happened. Three compartments tolerated it;
two did not; and within the one tissue where WWOX was localised at fibre resolution, **the compartment
carrying more WWOX is the compartment whose programme is lost**.

🔴 **And the repository's own rule says this comparison is owed.** `FT-049` is `INFERENZA` at priority
**ALTA** with the note that it cannot become `DATO` without a direct compartment/necessity experiment.
**Designing that experiment is what §6 does.**

---

## 2 · DIVERGE — six mechanistically distinct explanations

**Distinct = predicts a different measurement.** The discriminator column is the value of this table.
Nothing here is offered as established; every row is `IPOTESI` unless its cell says otherwise.

| # | Mechanism | What makes it distinct | 🎯 The readout that separates it from its neighbours |
|---|---|---|---|
| **R1** | **OXIDATIVE-DEPENDENCE GATING.** Vulnerability is set by how much a compartment depends on mitochondrial ATP. WWOX loss forces a glycolytic shift; a cell that can live glycolytically (hepatocyte, adipocyte, and — if L9 holds — oligodendrocyte, astrocyte) is spared; a cell that cannot (oxidative myofibre, neuron) fails | Locates resilience in **fuel strategy**, and predicts it is a property of the *state*, not of the cell identity | 🎯 **Respirometry / OCR:ECAR per compartment, plus a state-change arm.** R1 uniquely predicts that a **resilient** compartment can be made **vulnerable** by forcing it into oxidative metabolism, and that the vulnerable one is protected by substrate availability. **No other row predicts a reversible vulnerability.** Cheap surrogate available today: oxidative-enzyme histochemistry (SDH/COX) mapped onto lesion location within one tissue |
| **R2** | **EXPRESSION-DOSE GATING.** Vulnerability tracks how much WWOX protein the compartment normally carries. Lose more, lose more function | Puts the explanation in the **wild-type baseline**, requiring no lesion mechanism at all | 🎯 **Cell-type-resolved WWOX protein in wild type**, quantified against lesion severity across L1–L9. **L5 is the only existing measurement of this kind and it SUPPORTS R2** (soleus > EDL). R2 predicts a **monotonic** abundance–severity relation; R1 predicts abundance may be **flat or inverted** where fuel strategy differs |
| **R3** | **RENEWAL GATING.** Resilient compartments replace damaged cells (hepatocyte, adipocyte, OPC pool); vulnerable ones are **post-mitotic and long-lived** (myofibre, neuron). The phenotype is a failure to *clear*, not a failure to *function* | Makes resilience an **organ-level** property, invisible in any single-cell assay | 🎯 **Turnover + damage markers, and one perturbation nothing else needs:** apoptosis/proliferation indices in each deleted compartment, and whether **blocking regeneration unmasks a hepatocyte phenotype**. R3 alone predicts a latent, unmasking-dependent lesion in a "resilient" tissue |
| **R4** | **PARTNER-AVAILABILITY GATING.** WWOX has no paralogue, but its PPxY/WW-domain and SDR-span partner sets differ by cell type; a compartment lacking the relevant partner has nothing to lose | Puts the explanation in the **interactome**, not in metabolism or dose | 🎯 **Cell-type expression of the partner set** (the repository's own SDR-span and WW1 partner inventories) against the ladder. R4 predicts severity tracks **partner presence with WWOX abundance held constant** — the one pattern R2 cannot produce |
| **R5** | 🔴 **THERE IS NO LADDER.** The negatives are endpoint-limited and underpowered, not biological: L1 was never given a CNS or muscle endpoint, L3's negative is an unquantified `n=3` blot, and *"no evident abnormality"* (L9) is a phrase, not a panel | **Denies the explanandum entirely** | 🎯 **A per-Cre-line endpoint matrix**: for every published WWOX conditional line, which endpoints were actually run, with what n and what comparator. R5 alone predicts that the "resilient" rows are the rows with the **fewest and least sensitive endpoints**, and it is falsified the moment a resilient line is shown to have been given the same panel as a failing one |
| **R6** | **TIMING, NOT CELL TYPE.** The drivers differ in onset relative to the WWOX-critical window — Alb-Cre, adipocyte-Cre, ACTA1-rtTA (doxycycline-dependent, inducible), Olig2-Cre, Synapsin-Cre and Nestin-Cre do not delete at the same developmental moment. Resilience is an artefact of *when*, not *where* | Makes the ladder a **chronology**, and predicts the cell-type axis is epiphenomenal | 🎯 **Cre-onset age versus phenotype severity**, plus the one decisive design: a **single inducible driver deleting at two different ages in the same compartment**. R6 predicts severity tracks onset with cell type held constant; every other row predicts the opposite |

### 2.1 Rival elimination already available from held material, before any new experiment

- 🎯 **`L5` and `L6` together weaken `R5` and `R6` in one stroke, and this is the most useful thing
  in the table.** Both are **within the same animals, under the same driver, at the same onset, in
  the same experiment**. The vulnerability gradient between soleus and EDL, and the absence of an
  FDG deficit in brain and liver of the very animal whose muscle is affected, cannot be explained by
  a different Cre, a different age or a different endpoint panel — **there is only one of each.**
  R5 and R6 remain live for the *cross-line* rows; they are **excluded for the within-animal rows**.
- 🟡 **`L5` supports `R2` and is consistent with `R1`**, because soleus is both the WWOX-richer and
  the more oxidative fibre. 🔴 **Stated against my own preference: soleus does not dissociate the two
  variables, so L5 cannot rank R1 against R2.** Any design that uses it must add a compartment where
  abundance and oxidative character come apart. §6 does exactly that and nothing less would.
- 🔴 **`R3` is weakened by `L4`.** The skeletal myofibre is post-mitotic, but so is the neuron, and
  the tissue that failed here failed with a **metabolic and transcriptional** signature
  (mtDNA, Krebs transcripts, p-AMPK), not a degenerative one. R3 predicts damage-and-clearance; the
  measured phenotype is programme loss. **Weakened, not killed** — no turnover index was measured.
- 🔴 **And one thing the ladder does NOT show, stated so it is not over-read.** `L1`/`L2` are
  negatives for **HDL-C, GTT and body weight**. They are **not** negatives for liver function in
  general: a third study reports serum ALT ≈2× in `Wwox^hep−/−` under a high-fat diet
  (`analysis/peripheral_phenotype_denominator_audit_20260922.md:91`, `:164`). 🎯 **The hepatocyte is
  not unconditionally resilient — it is resilient at baseline and reportedly not under metabolic
  challenge.** That observation is `R1`'s single best existing foothold and it was found in the
  repository, not in the primary.

---

## 3 · CONNECT — one adjacent field, both halves

**Field of origin: the cell-type-selectivity problem in mitochondrial disease**, specifically the
**NDUFS4** conditional-knockout ladder in Leigh syndrome. 🔴 **Protein and system of origin carried
throughout: NDUFS4 is an accessory subunit of mitochondrial respiratory complex I, in the mouse. It
has no relationship of any kind to WWOX — no shared complex, pathway, domain, family or interactor.**

### ✅ WHAT TRANSFERS

1. **The ladder as a method, and its known failure mode.** That literature ran precisely this design
   — whole-body null versus neuron-restricted versus glia-restricted deletion of one gene — and
   established a discipline for reading it: a compartment-restricted negative is read as *"this
   driver, this onset, this panel produced no detected phenotype"*, never as *"this cell type does
   not need the gene"*. **That is `R5`, borrowed as a method and not as a result.**
2. **The precedent that a "glial negative" is the row most likely to be revised.** In that field the
   glial arms were repeatedly the ones whose negatives narrowed once a more sensitive endpoint or a
   different driver was used. 🎯 **This is why `L9` is the row I refuse to build on**, independent of
   its reading debt — two independent reasons to hold it, not one.
3. **The design principle that a within-animal gradient outranks a cross-line comparison**, because
   it holds driver, onset and panel constant. That principle is what makes `L5`/`L6` load-bearing
   here and the cross-line rows merely suggestive.

### ❌ WHAT DOES NOT TRANSFER

1. 🔴 **No mechanism transfers.** NDUFS4 has a defined biochemical lesion — a named subunit of a
   named complex with a measurable assembly and activity defect. **WWOX has no defined physiological
   substrate and no validated catalytic readout for any disease allele**, which this repository
   records independently (`TX-003`; `analysis/function_per_molecule_assay_design_20260922.md`).
   Importing a complex-I interpretation into a WWOX phenotype would be a category transfer. **`R1`
   is a hypothesis about fuel dependence, NOT a claim that WWOX is a respiratory-chain protein.**
2. 🔴 **No phenotype maps.** Leigh syndrome's neuropathology is bilateral symmetrical brainstem and
   basal-ganglia necrosis. Nothing in the WWOX corpus reports that distribution in any model or in
   any human genotype class. **No anatomical expectation may be imported.**
3. 🔴 **No therapy transfers, and none is named.** That field's intervention classes are not
   mentioned here, are not implied here, and are not made admissible by this analogy.
4. 🔴 **The analogy cannot supply evidence, only design.** If §7 finds that the WWOX ladder behaves
   unlike the NDUFS4 ladder, that is a fact about WWOX, not a failure of the WWOX data.

---

## 4 · HYPOTHESIS AND PREREGISTERED PREDICTIONS

> 🔴 **§4 was written to disk in full, with §5 EMPTY, BEFORE any confirmatory search was run.**
> Nothing in §4 was edited afterwards. Being wrong is acceptable; retrofitting is not.

**Working ranking, which is itself a prediction:**
`R5` ≳ `R6` > `R1` ≈ `R2` > `R3` > `R4`.

**I expect the ladder to be substantially an artefact of unequal endpoint panels and unequal Cre
onset**, and I expect that what survives that deflation is a **within-animal** gradient (L5/L6)
rather than a cross-line one. I am fixing this before looking because it is the *opposite* of the
conclusion the ladder invites, and the invited conclusion is the one I would most enjoy writing.

| # | Prediction (falsifiable) | How it will be scored |
|---|---|---|
| **P1** | **No published study applies the same endpoint panel to a WWOX-resilient and a WWOX-vulnerable conditional line.** The comparison in `L2` (hepatocyte vs adipocyte vs muscle, one panel, one paper) will prove to be the **only** matched-panel comparison in the entire WWOX literature | SUPPORTED if no second matched-panel comparison is findable; REFUTED if one exists |
| **P2** | **No WWOX conditional line has ever been given a neurological or CNS endpoint except the neural drivers themselves.** No Alb-Cre, adipocyte-Cre or ACTA1 animal has been EEG'd, behaviourally phenotyped or had brain histology | SUPPORTED if no such endpoint is findable in any surface |
| **P3** | **No WWOX study anywhere has measured oxygen consumption, extracellular acidification or respiratory flux in any compartment** — the `R1`-versus-`R2` discrimination has no existing data in this gene, in any species | SUPPORTED if no respirometry/flux measurement is findable; REFUTED if any exists |
| **P4** | 🎯 **`L5` (soleus > EDL WWOX immunofluorescence) has never been cited, reused or reasoned from by anyone** — not in the WWOX literature and not in this repository | SUPPORTED if no reuse is findable; the repository half is already measured (zero hits) |
| **P5** | **The hepatocyte "resilience" of `L1` will prove conditional, not absolute** — at least one report of a `Wwox^hep−/−` phenotype under challenge exists | SUPPORTED if such a report exists (the ALT-under-HFD datum already suggests it); REFUTED if the hepatocyte is negative under every tested condition |
| **P6** | **No WWOX conditional line has been deleted at two different ages under one inducible driver**, so `R6` cannot be adjudicated from any published WWOX experiment | SUPPORTED if no two-age induction is findable |
| **P7** | 🔴 **Against my own hypothesis `R1`:** if `R1` were right, the human WWOX-deficient brain should show a glycolytic/oxidative imbalance. I predict the held human evidence will run **AGAINST** it — the repository records human metabolism as normal on four independent screens, with a single cerebral-MRS outlier in the **wrong direction**. I expect this to survive checking and to **weaken `R1`** | SUPPORTED if the human counter-evidence is confirmed as I have described it, which weakens R1; REFUTED if I have mis-stated it |

---

## 5 · RESULTS OF THE CONFIRMATORY SEARCH

*(deliberately empty at the moment of writing — see §4)*

---
