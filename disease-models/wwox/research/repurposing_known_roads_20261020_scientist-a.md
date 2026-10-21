# Known therapeutic roads for WOREE / WWOX-DEE — what has really been TESTED

**Scientist A · task `REPURP-P3-KNOWNROADS-A-20261020` · written 2026-10-20, closed 2026-10-21.**
READ-ONLY toward the four scientific current files and toward `disease_model.md`. No canonical file
is modified here. `TX-001`–`TX-007` are not re-ranked. Nothing in this file is a dose, a route, an
administration recommendation or a statement about any individual; **nothing here is medical advice**,
and every statement is at the level of a WWOX-DEE genotype class assembled from public literature.

> **What this file is.** The roadmap's declared first scientific task: a reconnaissance of the known
> roads, each reduced to *molecule identified · model · genotype · endpoint · controls · result ·
> limit*. It is a census of **tests**, not a ranking of candidates, and it promotes nothing.
>
> **The roadmap is a plan, not an authority.** Where it and the repository's rules differ, the
> repository wins; `ADOTTATO NEL_PIANO` in it never means verified.
>
> **Method.** Repository first, by record: the claim registry, the therapeutic strategies tracker,
> the therapeutic-hypotheses ledger, the dismissal ledger with its `REVIVAL_TRIGGER`s, the discovery
> ledger's molecule and therapy leads, the experiment ledger, and the paper/literature registries
> read through `framework/scripts/registry_records.py get --theme … / --pmid …`. The two large
> registries were never loaded whole and never grepped as a method. Persisted first-hand locators in
> `deepdive_manifests/` were used where a reading already existed, rather than re-reading. **Two**
> new full texts were then read, for the one road the repository had never touched at all
> (§ 4). Budget was twelve readings; two were used, and § 8 says why the other ten would have bought
> nothing.

---

## 0 · The four outcomes, and why they are never merged

The roadmap's instruction is the spine of this file. Four different things get called "it worked",
and each changes priority in a different direction:

| # | Outcome | What it means here | Who can show it |
|---|---|---|---|
| **S** | **Symptomatic benefit** | a sign or a seizure count improves in a patient | clinical reports only |
| **R** | **Rescue of an experimental phenotype** | a measured readout in a model moves toward the comparator | cells, organoids, animals |
| **C** | **Clinical benefit** | a patient-level endpoint improves under controlled or at least documented observation | trials, registries, case series with an endpoint |
| **D** | **Disease modification** | the trajectory of the disease changes, not its symptoms | nobody, in any WWOX system, in any human |

🔴 **Two conversions are forbidden and both have been attempted in this literature.**
**R does not imply C**, and **S does not imply D** — the second is not a generality but a measured
fact in this disease: [`claim_registry_current#CLAIM 031`] records that cognitive and psychomotor
impairment preceded the epileptic encephalopathy and *«did not improve with achievement of better
control of epileptic activity»*, with the authors' own hedge *«in some of these cases»*. Seizure
control is fully indicated for quality of life, status-epilepticus and SUDEP prevention; **it may not
be counted as protection of development.**

🔴 **And a third conversion, named by this reconnaissance's own new reading (§ 4): protein quantity
does not imply function, and function in one endpoint does not imply phenotype.** That is the
operator's standing caution on amlexanox, and it now has a measured, independent instance behind it.

---

## 1 · The headline: the C column is empty on every road

**On registry evidence, no known road has a clinical-benefit datum.** The Harness clinical census of
2026-10-20 ([`drug_repurposing/clinical_census_20261020.md`](drug_repurposing/clinical_census_20261020.md),
read, not re-run) returned **no registered WOREE interventional study** on the public
ClinicalTrials.gov v2 API: `WOREE`, `WWOX-related epileptic encephalopathy` and `EIEE28` all resolve
to **one** record, an observational rare-disease registry and natural-history study; `DEE28` and the
gene-therapy candidate designation returned nothing.

⚠️ **Read that correctly, in the census's own words: a missing hit does not prove that no study
exists.** It is an answer about seven queries against one registry on one date; a study may be
unregistered, worded otherwise, registered elsewhere, or registered later. What follows for this
reconnaissance is narrow and is a **finding, not a gap**: every "clinical benefit" cell below is
`UNKNOWN` or `not verified`, and no road may be ranked on a clinical-benefit expectation today.

---

## 2 · The census, by road

Classification vocabulary, exactly as the contract sets it: **relevant negative · partial ·
inconclusive · exposure-or-toxicity limit · not verified · UNKNOWN · `NON_TROVATO_NELLA_RICERCA`**.
Outcome letters are those of § 0. **Deduplication is by experimental origin, not by drug name** — § 3
lists the collapses.

### 2.1 · Gene replacement — the only road with a measured rescue triad

| Field | Content |
|---|---|
| **Molecule / modality** | AAV9 carrying human *WWOX* cDNA under the neuronal human Synapsin-I promoter, with and without a `WPRE` element; intracerebroventricular |
| **Model** | `Wwox`-null mouse (two papers, one laboratory); human WWOX-KO and WOREE-derived cerebral organoids |
| **Genotype** | constitutive null; **no missense allele and no splice allele has ever been treated** |
| **Endpoints** | survival; firing rate in cell-attached recording; **spike-wave discharges on 7-day continuous ECoG**; myelination (OPC→mature oligodendrocyte, g-ratio, corpus callosum, optic nerve); gliosis; glycaemia; ataxia; behaviour; durability to P300 |
| **Controls** | wild-type, untreated null, and in the dose study two doses ± `WPRE`. The SWD contrast is the corpus's strongest causal design: `****` WT-vs-KO, `****` KO-vs-rescue, **`ns` WT-vs-rescue** at n = 5 per group, blind-scored |
| **Result** | **R: demonstrated, on multiple endpoints, in one species, by one laboratory.** **S/C/D: none** |
| **Limits** | (1) Not independently replicated: the 2021 proof-of-concept and the 2026 dose study share senior author and institution, and *«replicato mWwox≈hWWOX»* is an **intra-study control, not a replication**. (2) The dose relation is a **threshold, not a continuum** — the low-dose arm does not rescue survival, it postpones death; so *«a lower, safer dose would still help»* is refused by the panel. (3) **No measured ceiling**: the target is a pro-apoptotic tumour suppressor delivered irreversibly, and the dose study contains **no tumour surveillance of any kind** (`neoplas`, `carcinog`, `histopatholog`, `necropsy` all 0 on the fingerprinted main-text surface). (4) Treatment window tested only P0–P5; **`NOT_MEASURED ≠ SMALLER`** — the age–response slope is retired as unsourced, and the authors themselves decline the biological reading. (5) The cerebellum, the organ carrying the ataxic phenotype, is the region the vector reaches least, and **no efficacy endpoint was measured there**. (6) SWD is an absence-type electrographic signature and is not the convulsive repertoire of human WOREE |
| **Class** | **partial** — the strongest thing on the table and still partial, because R is complete and C/D are absent |
| **Records** | `CLAIM 002` · `CLAIM 004` · `CLAIM 011` · `CLAIM 040` · `TX-007` · `DL-MOL-005` · `DIS-021` · `DIS-023` (`D-23` in `DEFAULTS THAT BIT US`) |

### 2.2 · Lithium / GSK3β — the clearest relevant negative in the corpus

| Field | Content |
|---|---|
| **Molecule** | lithium chloride, intraperitoneal pretreatment (dose and schedule are recorded in `deepdive_manifests/PMID32000863.json` and are deliberately not reproduced here) |
| **Model** | `Wwox`-null mouse, pentylenetetrazol-induced seizure, **three genotypes in parallel** (`+/+`, `+/−`, `−/−`) |
| **Endpoint** | PTZ-induced seizure activity, behavioural |
| **Controls** | the two non-null genotypes **were** run, and that is what decides the road |
| **Result** | 🔴 **relevant negative on specificity.** First-hand panel reading, persisted: *«Panel d stacks three genotype panels … and each carries its own **** significance bracket. The wild-type panel is marked as significantly as the null one.»* The caption and the Results text name only the `−/−` panel. **The assay could detect genotype specificity and for lithium it did not** — this is a general anticonvulsant effect, not a WWOX-directed rescue. Outcome class: **R only, and not WWOX-specific** |
| **Limits** | per-genotype significance is not an interaction test and the paper reports none; the wild-type suppression is significant against a near-floor baseline; the causal attribution to GSK3β rests on lithium, whose other documented actions in this same system the paper's own Discussion lists (Wnt-dependent cerebellar neurogenesis, β-catenin-mediated myelin gene expression) |
| **Two further brakes from elsewhere in the records** | (a) `DIS-009` **rejects** the argument that a WWOX-mimetic peptide would be a safer lithium because WWOX inhibits GSK3β substrate-selectively: the same paper's supplementary figure shows inhibition of a glycogen-synthase-derived peptide unrelated to tau, so the interaction is a generic docking-site block; the mechanistic rationale strengthens while **`SAFETY` does not improve**. (b) `DL-MOL-003` points the opposite way on the Wnt axis: if WWOX loss **hyper**-activates Wnt, a GSK3β inhibitor pushes the wrong way. The direction gate on that lead is what kept a harmful candidate out |
| **Class** | **relevant negative** (specificity tested, not found) + **exposure-or-toxicity limit** (paediatric lithium carries a low therapeutic index; `TX-005` also notes it would interfere with the readability of concurrent care) |
| **Records** | `CLAIM 016` · `CLAIM 035` · `TX-005` · `DIS-009` · `DL-MOL-003` · `DL-MECH-032` |

### 2.3 · Ethosuximide — the genotype-specific signal nobody has followed

| Field | Content |
|---|---|
| **Molecule** | ethosuximide, a T-type Ca²⁺-channel blocker, intraperitoneal pretreatment (dose in the manifest, not reproduced) |
| **Model / genotype / endpoint / controls** | **the same single experiment as § 2.2** — same animals, same PTZ assay, same three genotypes, same figure |
| **Result** | **partial, and it is the mirror image of lithium.** First-hand panel reading: *«Figure 7b, image inspected — PTZ versus PTZ+ETS marked n.s. in the +/+ and +/− panels and significant in the −/− panel»*, and the paper's own text says so for ethosuximide while **never stating the converse for lithium**. So in the one assay where both were run, **the drug the paper does not favour is the one that behaved genotype-specifically** |
| **Limits** | one experiment, one laboratory, one assay, one species, behavioural endpoint, acute pretreatment, **constitutive null genotype only**; a provoked-seizure threshold is not a spontaneous-seizure outcome; no EEG; no interaction test; and genotype-specific suppression of a provoked seizure is **S-class at best and says nothing about D** |
| **What it is not** | not a recommendation and not a ranking. It is the single most under-exploited observation found by this reconnaissance, and what it earns is an **experiment**, not a promotion |
| **Class** | **partial** |
| **Records** | `CLAIM 016` (the lithium boundary note names the ethosuximide contrast) · `deepdive_manifests/PMID32000863.json` entries 1, 17 |

### 2.4 · MYC-linked antitumour interventions

Three distinct roads, routinely conflated because all three say "MYC".

**(a) A51, a multi-kinase inhibitor — the only pharmacological intervention ever applied to a human
WWOX-deficient neural model.**

| Field | Content |
|---|---|
| **Molecule** | **A51, a multi-kinase inhibitor, NOT a MYC inhibitor** — the source's own words: *«a multi-kinase inhibitor (A51) established to suppress Wnt and MYC expression»*. Submaximal concentration, weeks 8→15 in vitro |
| **Model / genotype** | human WWOX-**KO** cerebral organoids; a constitutive engineered null, no disease allele |
| **Endpoints** | SOX2⁺ and SOX2⁺MYC⁺ progenitor fractions; NEUN⁺ pan-neuronal; **SATB2⁺ and CTIP2⁺ layer-neuron fractions** |
| **Controls** | WT, untreated KO. **No treated-WT arm and no dose–response** |
| **Result** | 🔴 **partial, and the split is the finding.** Progenitor identity and pan-neuronal marking normalise (`ns` vs WT); **layer-neuron production does not move** — SATB2 and CTIP2 are `ns` KO-vs-treated, CTIP2 remaining far below WT. Inhibiting the MYC axis restores *who the cells are* and not *which neurons get made* |
| **Limits** | the compound suppresses **two** pathways, so causal attribution to MYC inherits the ambiguity (the authors declare this); no randomisation or blinding in the study; this is one of three experiments the paper excludes from its independent differentiations; **BLOCK-1 open and unresolved** — suppressing canonical Wnt during corticogenesis is the very mechanism by which the compound reduces progenitors, and the window between "removes excess progenitors" and "prevents normal corticogenesis" is measured nowhere; and the panel values behind the table above are **no longer re-auditable** — the published supplement exists in no checkout and the preprint does not contain the A51 experiment at all |
| **Class** | **partial**, with an **exposure-or-toxicity limit** that is unmeasured rather than favourable |
| **Records** | `DL-THER-089` · `DL-MECH-086` · `CLAIM 003` |

**(b) Simvastatin → MCM7 in `Wwox`/`Trp53`-null osteosarcoma.** In vivo tumour-size, tumour-weight
and MCM7 endpoints move; **the system is bone, the endpoint is a tumour, and there is no CNS
rationale, no barrier measurement and no WWOX-DEE genotype anywhere in it.** Its own panels contradict
the text's selectivity claim (control marrow viability falls, it does not stay flat), the treatment
lowers **both** MCM7 and c-Myc so the two targets are not separated, and the DKO-versus-SKO
sensitivity claim carries no statistical test at two biological replicates. A developing-brain sterol
question attaches to any paediatric or CNS reading and belongs in a BLOCK-1 screen if the seed is ever
promoted. **Class: not verified for this disease** (`DL-THER-080`).

**(c) Wnt / tankyrase inhibition as a downstream lever (`TX-004`).** Never administered in any WWOX
system. The direction now has a first-hand measurement — read cell-wise from the organoid paper's own
deposited differential-expression tables, β-catenin/TCF targets are **all** on the up side — but the
measurement is **transcript only**: no TCF/LEF reporter, no nuclear-versus-cytosolic β-catenin ratio,
raw-P gene lists, 2 WT versus 4 KO organoids, and a constitutive engineered null. The activation
*step* is unmeasured; only the pathway's transcriptional *output* is. **Class: UNKNOWN as an
intervention; `NON_TROVATO_NELLA_RICERCA` as a test** (`DL-MOL-003`, `TX-004`).

🔴 **The brake that governs all three.** *«Lower MYC/Wnt is better»* is **not a safe default** in this
disease, and the records say why in two independent ways: WWOX output is partner- and
context-dependent (`CLAIM 028`), and `DL-THER-115` records across three organisms that restoring WWOX
*raises* apoptotic sensitivity under stress. A narrow therapeutic window is required and has never
been measured.

### 2.5 · The ZFRA peptide — a category objection, not a dose objection

| Field | Content |
|---|---|
| **Molecule** | Zfra4–10 / Zfra1–31 peptides |
| **Models and what each tested** | (i) a 3×Tg Alzheimer model with **wild-type `Wwox`** — i.e. **no WWOX allele in the intervention cohort at all**; (ii) neuronal cells under high glucose, where an **independent** laboratory (no link to the originating group) uses Zfra1–31 and describes it as *«the specific inhibitor of WWOX»* |
| **Endpoints / controls** | (i) histology and behaviour, with PBS sham as the only comparator — no vehicle-plus-scrambled arm, no dose–response, no pharmacokinetics, blinding and randomisation not mentioned, group sizes internally inconsistent four ways, statistics computed over fields and cells rather than animals; (ii) mitochondrial homeostasis and viability, with **no genetic perturbation of WWOX** (`siRNA`, `shRNA`, knockdown, knockout, CRISPR, silencing, transfection all **0** in main and supplementary), **no scrambled/inactive peptide control**, and **total WWOX never measured** although both antibodies were in house |
| **Result** | 🔴 **relevant negative on transfer, twice over.** `DIS-030` rejects both halves of the citation that the field repeats: the peptide was never given to an animal with a defined WWOX genotype, and the supplementary bar chart said to show faster decline in `Wwox+/−` than in 3×Tg **carries no genotype label on any bar, no age 12, no n and no test**, and reproduces its own legend under neither assignment |
| **The direction, which is the real objection** | the independent neuronal paper obtains its benefit **by reducing WWOX signal**, in a disease whose problem is too little functional WWOX. Causal attribution of the protection to *inhibition* is itself unresolved — a pTyr33 signal normalised to β-actin falls if phosphorylation falls **or** if the protein falls, and zfration takes WWOX as substrate, so *«inhibited»* and *«consumed»* are not separated. **But both readings point the same way**, which is why this is an objection of **category, not of dose, route or formulation** |
| **Class** | **relevant negative** (transfer) + **exposure-or-toxicity limit** (experimental peptide, no paediatric or CNS profile) |
| **Records** | `HYP-20260705-05` (`flagged` — *monitor, do not promote*) · `DIS-030` · `DL-MOL-006` and its update |

**Its sibling, kept separate because the error class is instructive.** The pTyr33-WWOX peptide was
once carried as a *restoration* candidate on the strength of a commentary; the primary shows
phospho-Tyr33 WOX1 is **pro-apoptotic** and the peptide **blocks** neuronal death, i.e. it is a
competitive inhibitor of the WWOX-dependent function, not a substitute for it. **Status `refuted`,
and the refutation is the repository's own** (`HYP-20260709-04`, `DL-MOL-008`, failure mode `FM-010`:
no therapeutic lead may be promoted from a commentary without reading the primary).

### 2.6 · Amlexanox — the road with no WWOX record at all

Treated in full in § 4, because it is the only candidate for which the repository held **zero**
scientific records and the only one that required new reading.

### 2.7 · Symptomatic antiseizure therapy and the ketogenic diet — the S column, and only the S column

| Road | Model / genotype | Result and class |
|---|---|---|
| **Vigabatrin** | human WWOX-DEE, several series | **partial + exposure-or-toxicity limit.** Spasms *«resolved»* in one null child after it was added; **ineffective** in a predicted null/null with first-day onset; and in a third series, under vigabatrin added to three drugs, video-EEG still recorded focal electrical attacks and spasms *«not noticed at home by her parents»* — the reported freedom is **clinical, not electrographic**. Separately associated with vigabatrin-associated brain abnormality on MRI in two WWOX-DEE cases, which is why `CLAIM 001`'s status is **conflicting evidence** |
| **Ketogenic diet** | human WOREE, uncontrolled series | **inconclusive.** Three of five patients *«notably improved seizure control»*, but **the number exposed is not stated**, so 3/5 is not a response rate; «responded» is undefined; the one Q230P carrier has **no diet entry at all**, so nothing transfers to that allele class; and a DEE base-rate comparison spans 0 to 100 per cent, so this count is not distinguishable from the base rate. Elsewhere: *«did not significantly improve seizures and was suspended»* in a biallelic-null WOREE patient; tried in three and continued in one in another cohort |
| **ACTH / corticosteroids, phenobarbital-containing regimens, lamotrigine + valproate** | human, >21 heterogeneous primary reports tabulated in one curation | **partial, and visible only in the supplement.** A per-patient response column records **six explicit responders** in a disease the same paper's running text calls flatly *«not effective»*. 🔴 But West syndrome and hypsarrhythmia are frequent in this cohort and hormonal therapy is standard of care for infantile spasms **generally**, so a responder subset concentrated on hormonal regimens is at least as well explained by ordinary West-syndrome pharmacology. «Yes» is nowhere defined; no control arm, no dosing, no duration, no standardised follow-up |
| **Cannabidiol** | human, cohort observation | **inconclusive** — continued in 4/4 patients who started it in one cohort (a continuation pattern, not an efficacy measure); ineffective in the severe WOREE case above |
| **The broad ASM load** | one severe WOREE case, compound heterozygous | **relevant negative as a profile**: valproate, vigabatrin, clonazepam, clobazam, levetiracetam, rufinamide, cannabidiol, three ACTH cycles and the ketogenic diet all ineffective, up to 50 seizures a day. Two agents on that list were **suspended for adverse events rather than for inefficacy** — a correction this repository made to its own record |
| **Class for the whole row** | **S only.** `CLAIM 031` forbids counting any of it as **D** |

### 2.8 · Roads that exist as rationale and have never been administered in a WWOX system

Each is `NON_TROVATO_NELLA_RICERCA` as a **test**, with its own status as a hypothesis unchanged.

| Road | Status in the records | Why it is not a tested road |
|---|---|---|
| **Splice-correcting ASO / editing (`TX-001`)** | conditional hypothesis | 🔴 `antisense` and `oligonucleotide` are **zero** in the whole WWOX literature. **No intragenic precedent exists.** And the efficacy endpoint has **no baseline denominator in any allele, in any tissue**: of 20 relevant records, three measured a transcript from a WWOX splice allele and two merely annotated one; **no aberrant:normal ratio exists anywhere**, and **no WWOX splice allele has ever been assayed with an NMD inhibitor** |
| **CRISPRa / endogenous boost (`TX-002`, `DL-MOL-004`)** | parked, not refuted | never attempted in any WWOX system; and a non-allele-specific boost raises **both** alleles, so the sign of the benefit depends on a folding fate that is unknown |
| **Pharmacological chaperones — 4-PBA, TUDCA (`TX-003`)** | 🔴 `DIS-004`: **withdrawn** | the rationale was wrong-compartment (WWOX is cytosolic; the candidate route is lysosomal), not the molecule. **`REVIVAL_TRIGGER` is live**: 4-PBA is also an HDAC inhibitor and could act as an HSP co-inducer — *«it is not dead: the rationale is dead»* |
| **HSP70 co-inducers (arimoclomol)** | candidate proposed and **withdrawn the same day** | `D-03`: HSC70 is the chaperone that **delivers** the mutant to the lysosome, so amplifying that axis may **accelerate** degradation. *«It is a chaperone»* does not give the sign of the effect |
| **Chloroquine, NH₄Cl, bafilomycin A1, MG-132, 3-MA** | bench reagents | discrimination probes in culture, **never therapies**; chronic chloroquine in a child is explicitly refused, and CMA is neuroprotective in neurons so inhibiting it globally is dangerous |
| **Dichloroacetate (`HYP-20260709-05`)** | parked | the paper does not name it; dose-dependent peripheral neurotoxicity; and the ketogenic diet reaches the same metabolic bypass with an incomparably better profile, so it **dominates** this candidate |
| **Digoxin (`DL-MOL-009`)** | open, with a `SAFETY_SIGNAL` | 🔴 it **is** a measured R-class result — the only approved drug that corrects a *Wwox*-dependent phenotype in vivo (rapid, specific rise in blood glucose in nulls, with PDK1 and PHD3 down in nulls and not in wild type). **But the endpoint was glycaemia, not neuronal bioenergetics**, the therapeutic window is among the narrowest in medicine with dose-dependent cardiac *and* neurological toxicity, and the reported dose is probably a unit typo the records flag for verification. **Use: target validation for the HIF1α/PDK1 axis. Not a candidate.** Class: **exposure-or-toxicity limit** |
| **Memantine / NMDAR antagonism (`DL-MOL-001`), gap-junction modulation (`DL-MOL-002`)** | maturing / open hypotheses | the NMDAR- and gap-junction-dependence of the bursting is measured in a WWOX model; **no antagonist has ever been given to one** |
| **Anti-miR-153 (`HYP-20260709-03`)** | `flagged` | de-repressing endogenous WWOX in an animal is **demonstrated — in liver**; the paper never says whether miR-153 is expressed in brain, the antagomiR is pleiotropic, and it inherits the proteotoxic objection whole |
| **Pro-myelinating agents — clemastine and class (`HYP-20260709-07`)** | parked | the lever is in the wrong cell: WWOX-dependent hypomyelination is largely **secondary to the neuron** (oligodendrocyte- and astrocyte-restricted deletion produce no evident anomaly; neuronal deletion recapitulates the phenotype including myelin), so pushing OPCs alone would yield little. Not refuted: the AAV-oligodendrocyte arm is technically confounded |
| **N-acetylcysteine** | a therapeutic-direction lead, deliberately not promoted | a fibroblast-culture rescue with **no neural and no in vivo arm**; recorded as a lead in an intake wave, not as a road |
| **Read-through agents — ataluren, PTC124, ELX-02, gentamicin** | 🔴 **absent** | `ataluren` 0, `read-through` 0, `PTC124` 0, `ELX-02` 0 across the whole repository; PubMed `WWOX AND (ataluren OR readthrough OR "nonsense suppression" OR gentamicin OR PTC124 OR "ELX-02")` = **0** (2026-10-20). See § 4 and § 5 |

---

## 3 · Deduplication by experimental origin

The roadmap's instruction, applied. Five collapses, each one a place where a drug name would have
double-counted the evidence:

1. **Lithium and ethosuximide are ONE experiment** — same animals, same PTZ assay, same three
   genotypes, same figure of one paper. They are two arms, not two studies, and the comparison
   *between* them is the informative object (§ 2.2 vs § 2.3).
2. **The two gene-therapy papers are ONE laboratory** — shared senior author and institution, the
   earlier being the later's proof of concept. `mWwox ≈ hWWOX` inside the dose study is an intra-study
   control. **No laboratory outside that one has replicated any part of WWOX gene replacement**
   (census: 3 records, one laboratory). Dose-response therefore rests on a **single** paper and,
   inside it, on two figures.
3. **A51 (§ 2.4a) and the Wnt/MYC rationale (§ 2.4c) share a source lineage** — the organoid work and
   the review that restates it have the same first author, and the review is cited at the **preprint**
   DOI while the panels read here are the accepted manuscript. The review writes *«restored»* where
   its own primary shows a treated distribution running from wild-type level to about eleven times it,
   and **the significance bracket that would falsify the word is not drawn**.
4. **Zfra and the pTyr33 peptide are the same originating programme** read two ways, and both arrive
   at the same structural objection: the molecule acts against the WWOX-dependent function rather
   than for it. The genuinely independent datum is the Coimbra neuronal paper, and it strengthens the
   objection rather than the candidate.
5. **The "WWOX promotes osteosarcoma via MYC" title and the simvastatin seed are the same lab's
   consecutive papers**, and that lab has a measured **title-and-caption inversion** class: the
   article title says the opposite of what the paper demonstrates, and three of six figure captions
   in the next paper invert their own panels. **Any MYC-direction statement taken from a title or a
   caption of that lineage is unsafe; the bodies and the panels are correct and concordant.**

---

## 4 · Amlexanox — the road qualified, not promoted

### 4.1 · What the repository held: nothing

| Surface | Result |
|---|---|
| `registry_records.py get --theme amlexanox` over all seven registry surfaces | **0 records** |
| `git grep -ril amlexanox` over the whole checkout | occurrences **only** in the Harness-owned `drug_repurposing/` directory and in this task's own contract JSON |
| PubMed `amlexanox AND WWOX` (2026-10-20) | **0** |
| PubMed `WWOX AND (ataluren OR readthrough OR "nonsense suppression" OR gentamicin OR PTC124 OR "ELX-02")` (2026-10-20) | **0** |

🔴 **Classification: `NON_TROVATO_NELLA_RICERCA`, never `MAI_TENTATO`.**
**Query:** the four above. **Sources:** the seven LEGEND registry surfaces, the whole working tree,
and PubMed ESearch. **Date:** 2026-10-20. **Limits, stated because they are real:** a PubMed zero on
a drug name reaches titles and abstracts and not Methods (`D-25`: the miss rate on *reagents* in this
gene has been 100%); the WWOX Foundation's reported individual experience is **not formally
published** and so is unreachable by any literature query by construction; a conference poster
abstract may never enter PubMed; and no selector-based absence is trustworthy until the selector is
shown to match more than zero records somewhere (`D-18`) — here it matches 17 records on amlexanox
read-through, so the instrument reads.

### 4.2 · What the two sources named by the roadmap are, and are not

Per the roadmap, and not re-derived here: the WWOX Foundation reports **an individual experience, not
formally published**, and a GSRS2024 poster abstract (17–19 September 2024) **narrates it without
controls**. **Those are not two independent replications and they are not confirmed efficacy** — they
are one narrated experience and one uncontrolled account of it. This reconnaissance adds nothing to
them and does not treat them as evidence of benefit.

### 4.3 · What amlexanox has actually been tested for — two readings, done here

**Reading 1 — the originating claim** (manifest `PMID22938201.json`, MANIFEST STRICT PASS, 11
locators; receipt staged `FTR-20261020-22938201-01`, `partial_fulltext_read`, figures
`captions_only`).

| Field | Content |
|---|---|
| **Molecule** | amlexanox, identified as *«the only one drug confirmed on the primary assay after screening»* of a >1200-compound marketed-drug library, in a tethering assay that reports NMD inhibition and nothing about any disease gene. **All drugs tested once**, hit threshold mean + 3 SD — a hit-finding design, not an effect-size measurement |
| **Models / genotypes** | three human cell lines, **all non-neural, all nonsense alleles**: a lung-cancer line with a homozygous *TP53* PTC, immortalised myocytes from a Duchenne patient with a dystrophin PTC, and a cystic-fibrosis airway epithelial line compound heterozygous for a codon-2 *CFTR* nonsense allele and ΔF508. **No animal arm, no neural arm, no missense arm anywhere in the work** |
| **Endpoints / controls** | PTC-containing mRNA level normalised to a housekeeping gene; protein by Western blot with N- and C-terminal antibodies; function in two of three systems (a transcriptional target as a proxy for p53; cAMP-dependent halide efflux for CFTR). Controls: vehicle, untreated reference lines, viability, nascent-protein synthesis, eIF2α phosphorylation, three natural NMD targets, and head-to-head comparison with two read-through agents |
| **Result** | mRNA rose severalfold; protein appeared; and in the authors' terms both activities were present. **R-class, in non-neural cells, for nonsense alleles** |
| 🔴 **Limits, from the source's own sentences** | (1) **The full-length species can be the minor one**: in the p53 line *«a truncated p53 protein was well detected»* while *«a very low level of full-length p53 was also detected»*. (2) **No wild-type-referenced fraction of function is established anywhere**: the one quantitative function measurement lands at *«about 20% of the CFTR activity … measured in Calu-3 cells»*, a comparator the authors themselves say over-expresses the protein. (3) **The dystrophin functional argument is a citation, not a measurement** — *«Truncated dystrophin from our DMD cell line would be as functional as the wild-type dystrophin [31]. Therefore, we analyzed the cellular localization»*; that reference is the load-bearing unread citation of this reading and is named, not assumed. (4) **The concentration–response is not monotonic** and the authors *«cannot exclude some cellular toxicity at the highest concentration»*. (5) **Allele- and context-specificity is stated by the authors**: each cell model *«needs to be independently assayed»*, so no effect size transfers from one PTC to another. (6) **The dual mechanism is declared unresolved in its own originating paper.** (7) **The entire safety argument is historic use for other indications and other routes** — *«used for more than 30 years per os or topically to treat asthma and aphthous ulcers»*; there is **no paediatric datum, no CNS datum and no pharmacokinetic measurement of any kind** |

**Reading 2 — the independent test, and it is the finding** (manifest `PMID40544182.json`, MANIFEST
STRICT PASS, 9 locators; receipt staged `FTR-20261020-40544182-01`, `partial_fulltext_read`, figures
`captions_only`). A Verona/Genoa/Insubria group with **no shared author and no shared institution**
with the originating laboratory ran amlexanox **head-to-head with ataluren** in patient-derived
Fanconi-anaemia cells carrying nonsense alleles, in the same lines and on the same endpoints.

| Endpoint | Amlexanox | Comparator in the same cells |
|---|---|---|
| Full-length protein, gene 1 | *«no effect on FANCF protein levels»* | restored to healthy-control level |
| Full-length protein, gene 2 | ≈ **9 %** of healthy control | ≈ 11 % of healthy control |
| Transcript (the NMD-inhibition arm of the 2012 claim) | 🔴 *«neither amlexanox nor ataluren was able to rescue FANCA transcription»* — **NMD was active and was not relieved** | same |
| Survival under a genotoxic challenge | 🔴 **no improvement** | improved |
| Chromosomal aberrations | 🔴 **no effect** | *«almost completely depleting»* them |
| Micronuclei in primary fibroblasts | 🔴 **no significant effect** | reduced |
| Mechanism of what it *did* do | pSTAT2 down ≈ 50 %, attributed by the authors to **TBK1/IKKε inhibition** — **not read-through** | read-through |

🔴 **The authors' own two sentences are the ones this reconnaissance needs.**
*«Thus, this study suggests that a partial downregulation of p53 per se is not sufficient to produce
phenotypic rescue in human cells.»* And: *«These findings emphasize the need for a reliable
experimental pipeline to assess whether the minimal amount of neomorphic protein synthesized upon
translational read-through is actually followed by phenotypic rescue.»*

**So the operator's caution is no longer only a principle: protein quantity does not prove function,
and here it is measured — an intermediate marker moved, a protein appeared, and no phenotype
followed, in the one study that ran the drug against a comparator in the same cells.**

⚠️ **Limits of reading 2, and they cut both ways.** The amlexanox arms are the paper's smallest
(n = 3 on the genotoxicity endpoints); the group's standing programme is the comparator, which is a
declared directional interest **in favour of ataluren** and therefore a reason to weight the
amlexanox negative as the arm they had least incentive to make work, **and** a reason not to take the
ataluren arm at face value; the systems are lymphoblastoid and dermal, never neural; and the
supplement — which holds the exact alleles and the transcript panels behind the NMD negative — was
not fetched and is a declared debt. Also recorded rather than resolved: on the NMD arm **the two
papers disagree**, and this file does not adjudicate which is right; it records that the dual-activity
claim is **not reproduced** outside its originating laboratory.

### 4.4 · The structural point that no amount of new data can soften

🔴 **Read-through of a nonsense variant is a different action from any other, and it cannot correct a
missense substitution.** `p.(Gln230Pro)` is a missense change: there is no premature termination codon
to read through, and the mRNA is present at normal level with the protein not detected. **Read-through
is not a mechanism for that allele, at any dose, by any agent.** Any other pharmacological action of
amlexanox — NMD inhibition, TBK1/IKKε inhibition, anti-inflammatory activity — is a **separate
hypothesis requiring its own evidence**, and none has ever been tested in a WWOX system.

**Where the read-through-eligible class actually is, and that it has never been counted.** The
repository's own census records that step one for this road is *«an enumeration, not an
experiment»* — there is **no systematic count of WWOX PTC alleles and no PTC-context annotation**
(stop-codon identity and the +4 nucleotide, which govern read-through efficiency). Nonsense alleles
are held — including `p.(Trp44*)`, `p.(Arg54*)`, `p.(Arg264*)`, `p.(Gln191*)` and `p.Trp218*` — but no
published cohort separates splice from nonsense from frameshift from CNV, so the class is pooled into
"null" everywhere and its size is unknown. And the clinical ceiling is set by biology, not by the
drug: the largest genotype-classified cohort puts **about 57 % of classifiable individuals at
null/null**, so a majority of reported patients have **no recoverable endogenous substrate for any
allele-specific lever at all**.

🔴 **No paediatric suitability and no systemic availability may be inferred from historic
authorisations for other uses or other routes.** The 2012 paper's own safety sentence is exactly such
an inference, and it is cited here as the source's statement, never adopted.

### 4.5 · Verdict on this road

**A road to qualify, not a candidate to promote** — which is where the roadmap put it and where this
reconnaissance leaves it. Classification: **`NON_TROVATO_NELLA_RICERCA` for WWOX** (§ 4.1), and in the
adjacent literature where it *has* been tested, **partial in one gene, relevant negative in another,
and a relevant negative on phenotypic rescue in the only comparator-controlled study** (§ 4.3). The
promotion gate is the second paper's own demand, and it is the right gate: show that the protein
produced does something.

---

## 5 · What this reconnaissance did not find, said as a negative

- **No clinical-benefit datum on any road**, on registry evidence of one date (§ 1).
- **No disease-modification datum in any human, on any road.** The only disease-modification-shaped
  results in the corpus are R-class, in the constitutive-null mouse, from one laboratory.
- **No independent replication of WWOX gene replacement**, by any laboratory.
- **No intragenic precedent for a splice-correcting ASO**, and **no baseline measurement** against
  which such a therapy's endpoint could be read.
- **No read-through datum of any kind for WWOX**, and no enumeration of the alleles for which
  read-through would even be conceivable.
- **No pharmacological intervention in a patient-derived WWOX neural system except one** — the
  multi-kinase inhibitor of § 2.4a, in an engineered KO organoid, which is not a patient allele.
- **No drug has ever been administered to a WWOX model carrying a missense or a splice allele.**
  Every intervention in this census was given to a constitutive null, to a non-WWOX system, or to a
  patient as symptomatic care.
- **An extra self-chosen literature sweep found nothing new.** PubMed `(Wwox OR WWOX) AND
  (pharmacological OR inhibitor OR treated OR administration) AND (seizure OR epilep* OR
  encephalopathy OR neuron*)` returned 42 records (2026-10-20); five were not held on any registry
  surface and **none of the five is a therapeutic intervention in a WWOX-deficient system** (an
  exercise-and-methylation cohort study, two glioma-expression papers, a splicing-factor oncology
  paper and a fragile-site mapping paper). The sweep is bounded by that query and that date.

---

## 6 · Priority consequences, stated as the roadmap asks and not as a ranking

The roadmap is explicit that the classes move priority differently and that **the absence of a
consolidated clinical success does not prove failure**. Four consequences follow from this census, and
none of them is a recommendation:

1. **A relevant negative on specificity retires an argument, not a molecule.** Lithium's failed
   specificity test bounds what may be claimed for it; it does not make the GSK3β node uninteresting,
   and `CLAIM 035` makes that node a *measurable assay* and a *design exclusion zone*.
2. **The cheapest unexploited observation in this census is a comparison, not a compound** — one
   assay in which the only drug that behaved genotype-specifically (§ 2.3) was the one the originating
   paper did not favour, never followed up by anyone, in any model, in six years.
3. **The gate that would most change the amlexanox road is a function measurement, not more protein
   data**, and the second paper read here states it as a general requirement for the whole
   read-through class.
4. **The emptiest cell in the whole table is the one with the cheapest experiment behind it**: no
   WWOX splice allele has ever had its RNA examined, in ten reported patients across two canonical
   alleles, and one junction-spanning RT-PCR with an NMD block would **either populate or empty** an
   entire therapeutic class.

---

## 7 · Candidate-level summary

| Road | S | R | C | D | Class |
|---|---|---|---|---|---|
| AAV9-WWOX gene replacement | — | **yes**, mouse + organoid, one lab | UNKNOWN | — | partial |
| Lithium / GSK3β | — | yes, **not genotype-specific** | UNKNOWN | — | relevant negative + exposure limit |
| Ethosuximide | — | yes, **genotype-specific**, one assay | UNKNOWN | — | partial |
| A51 multi-kinase (MYC/Wnt) | — | **split**: progenitors yes, layer neurons no | — | — | partial + unmeasured exposure limit |
| Simvastatin → MCM7/c-Myc | — | yes, in bone tumour | — | — | not verified for this disease |
| Wnt / tankyrase inhibition | — | never administered | — | — | `NON_TROVATO_NELLA_RICERCA` |
| ZFRA peptide | — | yes, in **wild-type-`Wwox`** animals | — | — | relevant negative (transfer) + exposure limit |
| pTyr33-WWOX peptide | — | yes, wrong direction | — | — | refuted (premise) |
| Digoxin / HIF1α | — | yes, glycaemia in null mouse | — | — | exposure-or-toxicity limit |
| **Amlexanox** | — | **not in WWOX**; elsewhere partial, with a phenotype-rescue negative | UNKNOWN | — | `NON_TROVATO_NELLA_RICERCA` for WWOX |
| Read-through class (ataluren etc.) | — | — | — | — | `NON_TROVATO_NELLA_RICERCA` |
| Vigabatrin | **yes**, inconsistent | — | not verified | — | partial + exposure limit (VABAM) |
| Ketogenic diet | **reported**, no denominator | — | not verified | — | inconclusive |
| ACTH / steroids / phenobarbital regimens | **yes**, six responders in a supplement | — | not verified | — | partial, confounded by West-syndrome pharmacology |
| Cannabidiol | continuation pattern only | — | not verified | — | inconclusive |
| Splice-correcting ASO / editing | — | — | — | — | `NON_TROVATO_NELLA_RICERCA` (no precedent, no baseline) |
| CRISPRa / endogenous boost | — | — | — | — | `NON_TROVATO_NELLA_RICERCA` |
| 4-PBA / TUDCA | — | — | — | — | withdrawn rationale, live `REVIVAL_TRIGGER` |
| Arimoclomol / HSP70 co-induction | — | — | — | — | withdrawn (direction of effect unknown, possibly inverted) |
| Memantine / NMDAR, gap-junction modulation | — | dependence measured, **drug never given** | — | — | `NON_TROVATO_NELLA_RICERCA` |
| Anti-miR-153 | — | yes, **in liver** | — | — | `flagged` (pleiotropy, proteotoxicity) |
| Pro-myelinating agents | — | — | — | — | parked (wrong cell: hypomyelination is secondary to the neuron) |
| N-acetylcysteine | — | yes, fibroblast culture | — | — | lead, not a road |
| Dichloroacetate | — | — | — | — | parked, dominated by the ketogenic diet |

**Every `D` cell is empty. Every `C` cell is `UNKNOWN` or `not verified`. That is the state of the
known roads on 2026-10-21, and it is a measurement, not a verdict about what is possible.**

---

## 8 · DEFAULTS_TAKEN, debts, and why two readings and not twelve

**Readings: 2 of 12 permitted.** The contract set a ceiling, not a quota. The repository already held
first-hand, manifest-persisted panel locators for every other road in this census — including the
lithium and ethosuximide panels, which were read from the image by a previous reading and verified
character-for-character against the fingerprinted artefact — so re-reading them would have duplicated
work the repository had already paid for, which is the specific failure the duplicate-work check
exists to prevent. The only road with **zero** records was amlexanox, and that is where the budget
went. Ten unused readings are a deliberate default, recorded here.

**Declared debts, in the order a next session should close them:**
1. The supplement of reading 2 (exact alleles; the transcript panels behind the NMD negative).
2. The figures of both new readings, as images — both receipts say `captions_only` and **no panel
   value is asserted anywhere in this file**.
3. The load-bearing unread citation of reading 1 (that the truncated dystrophin of that line would be
   functional) and of reading 2 (that ~10 % of functional protein suffices in a recessive disease — a
   transfer from another gene and another protein class).
4. The read-through **enumeration** of § 4.4: a count of WWOX PTC alleles with stop-codon identity and
   the +4 nucleotide. It is a list, not an experiment, and nobody has made it.

**Boundaries honoured:** no dose, route or schedule is reproduced in this file, including for the
cell-culture work, where the figures exist in the manifests; no paediatric suitability is presumed for
anything, including supplements and historically authorised drugs; `drug_repurposing/` and
`framework/scripts/repurposing_bridge.py` were **read and never written** (a Harness agent owns both);
receipts are **staged and never recorded**; no PMID-looking literal appears outside the tables of this
research file.

---

*Not medical advice. Class level only. The four outcomes are kept apart deliberately, and a reader who
merges them will get a different answer from the same evidence.*
