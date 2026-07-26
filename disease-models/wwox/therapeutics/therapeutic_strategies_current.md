# THERAPEUTIC STRATEGIES

> **Operational tracker of candidate therapeutic strategies** for "buying time" until gene therapy.
> Enacts the mission defined in [[mission]] (§2 levers, §3 guardrails).
> Version: v1.4 (disease-level public edition).
>
> **Public edition.** Disease-level portfolio for the WWOX-DEE population. No identified individual is described. Specific variants are used only as decoupled public worked examples — a destabilizing SDR missense on one side, a canonical splice-acceptor variant on the other — each carried independently in the analysis layer, never as one person's genotype.

---

## 0. What it is / is not

- **It is** a structured portfolio of *candidate* interventions (ASO, editing, molecules, repurposing, supplements, window-protection), each scored and with a next action.
- **It is NOT** a list of validated therapies nor a clinical plan. Every entry is material for discussion **with a treating clinical team**. Nothing here is medical advice.
- **READ-ONLY toward the canonical files.** A strategy that matures into promotable evidence goes through the normal pipeline (INGEST → DEEP_DIVE → COMMIT); it does not enter the canonical files from here.
- Every entry is tagged `DATO` / `INFERENZA` / `IPOTESI` / `ESPANSIONE`. **No implicit epistemic upgrade.**
- Every entry declares its beneficiary scope and a falsifiable next action. Severity without a bearing on a lever, safety, monitoring or trial stays background and does not set priority.

---

## 1. Scorecard (0–3 per dimension)

| Dim | Question |
|---|---|
| **MATCH** | how well the mechanism fits the specific biology (alleles/pathway)? |
| **EVID** | strength of evidence (0=speculative EXTENSION · 1=HYPOTHESIS · 2=INFERENCE/convergent preclinical · 3=human DATA) |
| **TIME→patient** | how quickly it could realistically reach the patient (3=already available · 0=years/decades) |
| **SAFETY** | pediatric safety profile (3=very favorable · 0=high/unknown risk) |
| **TIME-BUY** | does it act on a *time-sensitive* (window) variable? (3=yes, strong) |
| **REVERS** | reversibility if it fails/harms (3=stoppable immediately · 0=irreversible) |
| **ACTION** | concrete actionability with the clinical team *now* (3=discussable immediately · 0=theoretical only) |
| **PROTO-FIT** | compatibility with the safety block (one variable at a time; protect concurrent care) |

> Priority = holistic reading (not a simple sum): a strategy with high MATCH + high TIME-BUY + high SAFETY rises even if EVID is low — provided it is honestly labeled.

---

## 2. Active strategies

### TX-001 — Correcting a canonical splice-acceptor allele: RNA assay → ASO/editing choice
- **Scope:** carriers of the same splicing architecture · **Axis:** 🧬 allele-specific correction · **Tag:** HYPOTHESIS conditional on the real transcript
- **Mechanism:** SpliceAI predicts loss of the exon-9 acceptor (DS_AL 0.96), but the biological output is not yet measured. Exon skipping, cryptic acceptors, intron retention or multiple isoforms could emerge. An ASO does not repair the sequence, but could redirect splicing if a productive outcome exists; editing/prime editing remains the alternative if the sequence must be corrected.
- **Real precedent:** *Milasen* (Kim et al. 2019, NEJM) — an n-of-1 ASO designed for a single child with a splice variant (Batten/CLN7), from identification to dosing in ~1 year. An n-of-1 regulatory/ethical model exists (individual FDA IND).
- **Provisional scoring:** MATCH 3 · EVID 1 · TIME→patient 1 · SAFETY 1–2 · TIME-BUY 3 · REVERS 2 for ASO / 0 for editing · ACTION 2 (assay immediately actionable) · PROTO-FIT 2
- **Mandatory gate:** no ASO-vs-editing choice before junction-specific RT-PCR + amplicon sequencing + allele-specific quantification; long-read if multiple isoforms appear. The Milasen precedent is an n-of-1 regulatory precedent, not proof of amenability for WWOX.
- **Next action:** (1) measure the RNA output in variant-carrying cells using a published exon-8→9 assay as a template to redesign; (2) define which transcript/protein is recoverable; (3) only then run an ASO design walk or evaluate editing; (4) map n-of-1 channels with the clinical team.

### TX-002 — CRISPRa / endogenous WWOX transcriptional boost — PARKED, not refuted
- **Scope:** subgroups with dose-limited functional protein output · **Axis:** 🔼 endogenous boost · **Tag:** HYPOTHESIS `stress-tested`
- **Mechanism:** for Q230P, published data show normal transcript but protein not detected, leaving open impaired translation or premature degradation. mRNA normality does not prove the boost is useful, but does not falsify the translational branch.
- **Scoring:** MATCH 1 · EVID 1 · TIME→patient 0 · SAFETY 1 · TIME-BUY 1 · REVERS 1 · ACTION 1 · PROTO-FIT 1
- **Status/next action:** `parked`; reopen only after metabolic labeling/fractionation/turnover and a boost-vs-rescue-vs-combination comparison with function.

### TX-003 — Pharmacological chaperone / proteostasis modulators (Q230P example)
- **Scope:** the missense-example class; extendable only to variants with demonstrated amenability · **Axis:** 🧪 proteostatic rescue · **Tag:** HYPOTHESIS `stress-tested`
- **Mechanism:** Q230P has normal transcript and protein not detected in fibroblasts, but synthesis, insolubility and degradation are not discriminated. AlphaFold makes a core perturbation plausible; it does not demonstrate degradation or a recoverable state. Any rescue must produce **soluble, correctly localized, functional WWOX**.
- **Correction (epistemic-discipline example):** a prior ΔΔG heuristic, a "misfolding-dominant" tally, and a P47T↔Q230P equivalence were retracted. P47T has normal protein and a WW1/PPxY defect; G372R is a natural variant comparator, **not** a validated negative control.
- **Three families (in order of applicability here):** (1) site-specific chaperone (e.g. **migalastat**/Fabry — closest analogy, but requires an active-site ligand); (2) kinetic/allosteric stabilizer (e.g. **tafamidis**/TTR); (3) indirect proteostasis regulator (HSP70/HSP90, heat-shock response; e.g. **4-PBA, TUDCA**, already in pediatric use). Other paradigm precedents: **Trikafta** (CFTR-F508del), **sapropterin** (PKU), **ambroxol** (Gaucher, repurposing).
- **Scoring:** MATCH 3 · EVID 1 · TIME→patient 1 · SAFETY 1–2 · TIME-BUY 3 · REVERS 3 · ACTION 2 · PROTO-FIT 2
- **Openings/obstacles:** WWOX is an oxidoreductase with undefined physiological substrate/activity; migalastat is a variant-specific assay precedent, not a direct mechanistic analog. CMA, degron and helical trigger are not assigned to Q230P. A stabilizer targeting the SDR domain remains `conditional / not design-ready` and must avoid both the functional region (388–407/L404) and perturbations of the putative catalytic triad.
- **Next action:** (1) variant-carrying cells + WT/null and, as soon as possible, an isogenic corrected/knock-in Q230P; (2) distinguish synthesis, degradation and insolubility (qRT-PCR/RT-PCR, metabolic labeling, CHX chase, soluble/insoluble fractions, brief proteasome/lysosome perturbations with viability); (3) a mini-screen with pre-specified endpoints; (4) promote only hits recovering at least two orthogonal readouts beyond abundance; (5) confirm in iPSC neurons. G372R/P47T remain comparators, not read-across proof.

### TX-004 — Wnt / MYC modulation (downstream)
- **Scope:** potentially all WWOX-LoF, pending context validation · **Axis:** 🔻 Wnt/MYC · **Tag:** INFERENCE (preclinical)
- **Mechanism:** Steinberg 2024 identifies **MYC overexpression** as a key node of hyperexcitability in WWOX organoids, corrected by rescue. Wnt-adjacent. Wnt/tankyrase inhibitors would act *downstream*, without repairing WWOX → potentially genotype-agnostic.
- **Scoring:** MATCH 2 · EVID 2 · TIME→patient 1 · SAFETY 1 (Wnt inhibitors: intestinal/bone toxicity, high pediatric caution) · TIME-BUY 2 · REVERS 2 · ACTION 1 · PROTO-FIT 1
- **Caution:** "lower MYC/Wnt = better" is NOT a safe default (context-dependent WWOX output). A narrow therapeutic window is required.
- **Next action:** map Wnt/tankyrase inhibitors with a pediatric profile (Open Targets/DRKG); look for MYC/Wnt data as state biomarkers.

### TX-005 — Repurposing: lithium / GSK3β (and other nodes)
- **Scope:** potentially all WWOX-LoF with a compatible network endpoint · **Axis:** 💊 Repurposing · **Tag:** INFERENCE (preclinical) → to evaluate
- **Mechanism:** lithium abolishes PTZ-induced seizures in Wwox-/- (see prenatal-structure meta); GSK3β is an emerging node. A known, pediatrically used drug, narrow but manageable therapeutic window.
- **Scoring:** MATCH 2 · EVID 2 · TIME→patient 3 (existing drug) · SAFETY 1 (pediatric lithium: tight monitoring, low therapeutic index) · TIME-BUY 2 · REVERS 3 · ACTION 2 · PROTO-FIT 1 (would interfere with concurrent-care readability → critical timing)
- **Caution:** high potential but requires safety caution and NOT during titration phases. To be discussed with the team as a hypothesis, not an immediate move.
- **Next action:** targeted review of lithium/GSK3β in WWOX/DEE; map other repurposing candidates on model nodes (Ca²⁺, myelin, metabolic).

### TX-006 — Window protection (time-sensitive variables already active)
- **Scope:** all WWOX-LoF, individualized to the clinical profile · **Axis:** ⏳ Window protection · **Tag:** DATA/INFERENCE
- **Mechanism:** optimize network stabilization, quality of life, status-epilepticus/SUDEP prevention and respiratory/ophthalmologic surveillance while causal levers mature. WWOX is a DEE: seizure control **must not be automatically counted as recovery of development or myelination**. It remains essential for symptomatic benefit, safety and preserving the conditions needed to access therapies.
- **Scoring:** MATCH 3 · EVID 3 · TIME→patient 3 · SAFETY 3 · TIME-BUY 2 (benefit/safety, not demonstrated developmental recovery) · REVERS 3 · ACTION 3 · PROTO-FIT 3
- **Note:** this is the care floor, not a substitute for causal levers. Endpoints and interventions must declare which concrete benefit they measure without turning symptomatic improvement into disease modification.
- **Next action:** define the time-sensitive N-of-1 endpoints and their priority (link to [[clinical_monitoring_endpoints_current]]).

### TX-007 — AAV9-WWOX gene therapy (gene addition) — the north-star, now FIRST-IN-HUMAN ⭐
- **Scope:** all WWOX-LoF · **Axis** (mission §2): 🧬 gene therapy / gene addition · **Tag:** preclinical DATA (mouse) + **news-level n=1** (human compassionate use) — ⚠️ human efficacy NOT demonstrated
- **Mechanism:** AAV9 delivers a healthy copy of WWOX to neurons → restores the protein **bypassing any mutation** (gene addition) → **genotype-agnostic**, covering both allele classes. Preclinical base = Repudi/Aqeilan 2021 (AAV9-hSynI-WWOX, neonatal ICV → seizure/myelin/survival rescue in the Wwox-null mouse).
- **Clinical event (2026):** first-in-human WWOX gene therapy reported at news level — a compassionate-use n-of-1 in an infant with WOREE, by the Aqeilan group with an industrial partner (Mahzi Therapeutics). One-month outcome reported as stable, with no recurrence of severe seizures. An FDA filing was reported as pending. *(Details are news-level, not peer-reviewed; individual case specifics are not reproduced here.)*
- **Scoring:** MATCH 3 · EVID 2 (strong preclinical + n=1 news; *not* 3 = no proven human efficacy) · TIME→patient 1–2 (company + FDA route exist; trial not yet open; n-of-1 compassionate route possible) · SAFETY 1–2 (AAV9 CNS: n=1, immunogenicity/dose/long-term unknown) · TIME-BUY 3 (causal lever) · **REVERS 0** (⚠️ irreversible — AAV persists) · ACTION 2 · PROTO-FIT 2
- ⚠️ **Window/age caveat (from the group's own preclinical work):** neuronal GT rescues excitability/function but does **NOT** repair the progenitor defect (radial glia/neurogenesis), largely prenatal/early-postnatal. The older the patient, the smaller the reversible fraction. For a patient older than the neonatal window: reasonable to aim at **functional protection/recovery**, not reversal of developmental damage. Consistent with "reduce damage / buy time", not a reset.
- **Why it is central:** it is the mission **destination** becoming real, with a class genotype-match.
- **Next action:** (1) structured monitoring (📡 block below); (2) evaluate **with the clinical team** contacting the program for expanded-access/trial eligibility and the **window question** (how much a given patient benefits, given age); (3) on publication of the case report → INGEST → DEEP_DIVE (real route/dose/promoter/mutation/follow-up).

#### 📡 MONITOR (watchlist — review every LEGEND session)
| # | What to monitor | Where | Action trigger |
|---|---|---|---|
| M1 | Peer-reviewed case report | PubMed ("WWOX gene therapy", Aqeilan), Brain/NEJM/Nat Med | → INGEST + DEEP_DIVE on the real data |
| M2 | Mahzi / WWOX trial registration | ClinicalTrials.gov ("WWOX", "Mahzi Therapeutics") | → evaluate patient eligibility |
| M3 | FDA filing/decision (IND, orphan, RMAT) | FDA / Mahzi releases | → regulatory pathway opening |
| M4 | ≥3/6/12-month follow-up (durability, safety, development) | news / publications | → update TX-007 EVID/SAFETY |
| M5 | Expanded-access / compassionate program open | Mahzi / Aqeilan group | → concrete channel for a patient |
- **Cadence:** fast-moving event → **~monthly** check. Hook: `wwox-scout` includes "WWOX gene therapy / Mahzi / Aqeilan clinical" in scans; every update refreshes the corresponding M row.

---

## 3. Summary view (current priority)

| ID | Strategy | Axis | Tag | Priority | Critical next step |
|---|---|---|---|---|---|
| TX-007 | GT AAV9-WWOX (north-star) | 🧬 | preclin. DATA + news n=1 | **active watch** | 📡 monitor M1–M5 + evaluate contact with the team |
| TX-003 | Functional Q230P rescue | 🧪 | HYPOTHESIS | **high experimental** | define synthesis/degradation → screen → function |
| TX-001 | Splice-allele correction | 🧬 | conditional HYPOTHESIS | **high experimental** | allele-specific RNA → decide ASO vs editing |
| TX-006 | Protection/safety | ⏳ | DATA/INF | **ongoing** | real benefit endpoints; do not confuse with disease modification |
| TX-005 | Lithium/GSK3β repurposing | 💊 | INFERENCE | med-high | targeted review + safety/timing |
| TX-004 | Wnt/MYC downstream | 🔻 | INFERENCE | medium | inhibitors with a pediatric profile |
| TX-002 | WWOX CRISPRa | 🔼 | stress-tested HYPOTHESIS | **parked** | discriminate synthesis/turnover; then boost-vs-rescue test |

---

## 4. Layer rules

- New strategy → new ID `TX-NNN`, with a mandatory epistemic tag and scoring.
- Status/next-action updates: free (this is an operational tracker, not canonical).
- Promotion of a strategy to canonical evidence (claim/paper) → **only via the pipeline** INGEST → DEEP_DIVE → BATCH_COMMIT.
- Every entry keeps the disclaimer: discussion with the clinical team, not medical advice.
- Minimum fields: `beneficiary_scope`, lever, next decisive experiment/decision and `what changes if true`; `none_background` does not enter the priority view.

---

**End of `therapeutic_strategies_current.md`.**

> The portfolio exists for one reason: **to have the right lever ready when it is needed, not to be looking for it when it is too late.**
