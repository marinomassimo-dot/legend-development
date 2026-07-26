# The discovery lens — lead taxonomy + question bank

Operational tool for phases 1–2 of `legend-discovery`. As you read line-by-line, run every section through these questions. Most will give "no" — that is fine. Just **one** yes makes the paper valuable.

## The 4 lead types

### BIO — WWOX biomarker lead
Anything measurable that could reflect the **functional state of WWOX** (expression, activity, or downstream consequence).
- **Tier 1/2 (WWOX-linked)**: transcript/protein/metabolite directly under WWOX control or under a direct partner; a readout of a pathway known to be WWOX-dependent. → candidate for `biomarker_candidates_current.md`.
- **Tier 3 (distal/clinical)**: a clinical endpoint or downstream marker not specific to WWOX. → `clinical_monitoring_endpoints_current.md`, **never** in the biomarker file.
- Always capture: *what* is measured, *with which assay*, in *which matrix* (blood/CSF/fibroblasts/imaging/EEG), and *how close* to WWOX the signal is.

### MOL — molecule / therapy lead
A compound, drug, inhibitor/agonist, factor, or intervention that **at least partially corrects** a pathway dysregulated in WWOX LoF.
- Capture: the compound/target, the pathway it touches, the direction of the effect, the model it was seen in (cell/animal/human), and *how* plausible the transfer to the WWOX context is.

### REPO — drug repurposing
A very high practical-value sub-case of MOL: a **drug already approved for humans** (or in advanced trials) whose mechanism hits a target/pathway relevant to WWOX. Worth double because it lowers the translational barrier.
- Capture: the drug name, approved indication, target, the rationale of the bridge to WWOX, and the known safety profile (relevant for a child).

### MECH — mechanistic clue ("needle in the haystack")
A non-conclusive detail that could still be the **seed of the next step**: an unexpected connection between pathways, a new protein partner, a phenotype that echoes something in the case, a side observation in the Methods/supplementary.
- Capture it even if you do not yet know where it leads. The ledger's purpose is precisely not to lose these needles.

## Question bank per section

**Abstract / Intro** — What is the central pathway? Does it touch one of the dysregulated WWOX pathways (myelin/glia, metabolism/sphingolipids, prenatal structure/GSK3β, GABA, neuroinflammation, cerebellar axis)? Do they cite WWOX or one of its partners?

**Methods (mine #1)** — Which assays do they use? Each is a possible biomarker readout: *could I measure this in the case or its fibroblasts?* Which compounds/reagents/inhibitors? Each is a possible MOL/REPO. Which biological matrix (blood, CSF, fibroblasts, organoid)? Which knockdown/rescue do they do — the *rescue* is gold: it says what returns the system toward normal.

**Results, figure by figure** — What changes quantitatively and in which direction? A dose-response effect of a compound = a strong MOL lead. A marker that tracks the pathway state = a BIO lead. A partial rescue = a direct therapeutic rationale.

**Discussion** — Which limits/openings do they declare? They often point to the next query. Do they cite ongoing molecules/trials?

**Supplementary (mine #2)** — Screening tables, differential gene/metabolite lists, raw dosing data. The most precious needles often hide here.

## Cross-cutting question: is there a platform to test it? (feasibility)
For each MOL/REPO/MECH lead, ask explicitly: **"which already-existing model would test this hypothesis?"** (WOREE iPSC-derived organoids, WWOX-null neurons/MEA, patient fibroblasts, mouse model, zebrafish). A lead with a ready platform is worth much more: it goes from "paper" to "runnable experiment" and enters `maturing` at high priority. If the paper *describes* a platform (assay, cell line, model), it is itself an "enabling" MECH lead — record it: it multiplies all the other leads that platform can test.

## Effect-direction rule (gate for REPO leads)
A lead stays **MOL/IPOTESI** until **the direction** of the intervention is resolved. A "dysregulated" pathway does not say whether it must be *activated* or *inhibited*: naming a drug before knowing the direction is an error — and not only a prudence error, **it can flip the candidate into a harmful one**. (Real case from the ledger: for the Wnt axis, lithium (a GSK3β inhibitor) was proposed; once the direction was fixed — WWOX-loss → Wnt *hyper*-active — lithium turns out *worsening*, and the correct candidate is a Wnt *inhibitor*. Without the gate we would have proposed the wrong molecule.) A lead **rises to REPO** (an approved drug candidate) **only when**: (a) the defect direction is fixed by **≥2 sources** *in the right biological context* (beware transferring a direction from cancer to a developing neuron: Wnt often has timing-dependent roles — flag `conflicting` and verify), (b) an approved drug exists that pushes in the right direction, (c) the rationale has survived the "refutes" side. Until then: a MOL with a `Proposed experiment` that *determines the direction*.

## Case-relevance test (a filter, not a censor)
A lead enters the ledger if it passes **at least one**:
1. It directly touches WWOX or a direct partner.
2. It touches a pathway already mapped as dysregulated in WWOX LoF (see the active meta-analyses).
3. It offers a readout plausibly measurable in the clinical/cellular context of the case.
4. It is a strategic ESPANSIONE that *could* become a bridge (then: tag ESPANSIONE, status `open`).

If none pass, it is not a lead: note in one line why you discarded it (so you do not re-evaluate it every time) and move on.

## Generating the next-search agenda (phase 5)
From each live thread, formulate concrete, not vague, queries. Example forms:
- `"WWOX" AND "<pathway>" AND ("biomarker" OR "CSF" OR "serum")` on PubMed (via `wwox-scout`).
- A **compound/target** name that emerged → search its rescue work in neuronal models.
- A new **protein partner** → search its interactome and the drugs that modulate it.
- An **author/group** with the right assay → search their other work (via `research-group-analyst`).
Record the queries in the ledger and pursue the most promising ones immediately; park the others with status `open`.
