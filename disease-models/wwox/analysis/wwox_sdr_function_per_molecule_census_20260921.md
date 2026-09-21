# Does anyone, anywhere, possess an assay of WWOX function PER MOLECULE?

**Node:** `MECHANISM_WWOX_SDR_FUNCTION_AND_MISSENSE_RESCUE` · **Actor:** Scientist A · **Date:** 2026-09-21
**Status:** non-canonical analysis file. No canonical file edited, no registry written, no receipt claimed, no commit, no gate.
**Read-only toward every canonical file. Not medical advice.**

> **The question, restated exactly.** Does any laboratory in the published literature possess a measurement that
> distinguishes *"this WWOX missense protein is present but inert"* from *"this WWOX missense protein is absent"* —
> and is there a transferable route to test whether a destabilised WWOX missense protein can be **stabilised** and
> shown to **retain useful function**? Exemplar allele: **Q230P** (SDR domain; normal transcript, protein not
> detected on Western blot in patient fibroblasts).
>
> This is the field-wide version of the question that
> [`sdr_missense_readout_assessment_20260920.md`](sdr_missense_readout_assessment_20260920.md) answered `NO` for the
> Chang/NCKU corpus alone.

---

## 1 · Read depth, declared before any finding

| PMID | Identity | Depth reached this session | Body length returned | Figures |
|---|---|---|---|---|
| **21476439** | Sałuda-Gorgul A, Seta K, Nowakowska M, **Bednarek AK**, *Z Naturforsch C* 2011;66(1–2):73–82 — "WWOX oxidoreductase — substrate and enzymatic characterization" | 🔴 **abstract only.** `convert_article_ids` returns **no PMCID**; `get_copyright_status` returns `pmc_id:null`; `find_related_articles(link_type='pubmed_pmc')` returns an **empty linkset** — three independent checks, PMC was consulted and there is no deposit. Publisher egress blocked. **The single most load-bearing paper in this file is one I could not read.** | n/a — no PMC record | ❌ |
| **38161429** | Battaglia L *et al.*, *Front Pediatr* 2023;11:1301166 (PMC10757851) — WOREE neuroimaging mini-review | 🟢 **full deposit read this session** | ≈16 KB (estimate; not byte-exact) | ❌ |
| **30158849** | Liu C-C … Sze C-I, Chang N-S, *Front Neurosci* 2018;12:563 (PMC6104168) — WWOX phosphorylation / neurodegeneration review | 🟢 **full deposit read this session** | ≈30 KB (estimate; not byte-exact) | ❌ |
| **38378758** | Clausen L … Fowler DM, Lindorff-Larsen K, Hartmann-Petersen R, *Nat Commun* 2024;15:1541 (PMC10879094) — "A mutational atlas for Parkin proteostasis" | 🟢 **full deposit read this session** | **71,480 B** (measured) | ❌ |
| **26499798** | Abu-Remaileh M, Dodson E-J, Schueler-Furman O, Aqeilan RI, *JBC* 2015;290:30728–35 (PMC4692203) | 🔴 **PMCID exists, deposit returns `full_text:""`** — abstract only. The failure mode the brief warned about, observed. | **0 B** | ❌ |
| **17067289** | Lukacik P … **Oppermann U**, *Biochem J* 2007;402:419–27 (PMC1863559) — orphan DHRS10 deorphanised | 🔴 **PMCID exists, deposit returns `full_text:""`** — abstract only. | **0 B** | ❌ |
| **15580310** · **14555208** | Chang N-S *et al.*, *Oncogene* 2005 (NSYK / E2) · Chang N-S … **Oppermann U**, *Biochem Pharmacol* 2003 | 🔴 abstract only — no PMCID on either (`convert_article_ids`, `get_copyright_status` both null) | n/a | ❌ |
| **16380372** · **29785012** · **32442409** · **35716775** · **31184403** | Guo 2005 DHRS6 · Matreyek 2018 VAMP-seq · Mighell 2020 PTEN integrated DMS · Rotem-Bamberger 2022 WWOX WW2 · Pejaver 2019 VSP assessment | ⚪ **abstract / metadata only this session.** (35716775 is already a *complete_fulltext_read* in LEGEND, receipt `FTR-20260726-35716775-02`.) | n/a | ❌ |
| Mondragon-Estrada E *et al.*, *Birth Defects Res* 2025;117(12), doi 10.1002/bdr2.70007 | Bangladesh spina bifida GWAS | 🟡 **Discussion-section passage retrieved via Scholar Gateway** (not a PMC fetch) | passage only | ❌ |

🔴 **No figure panel was inspected anywhere in this file.** No finding below rests on a panel. Where a paper's
result exists only in a figure, this file says so and does not adjudicate it.

⚠️ **Extractor state.** The PubMed MCP text surface deletes italicised tokens (gene symbols, variant superscripts,
italic *P* and *n*). **No italic-class zero is used as evidence anywhere in this file.** Every negative below rests
either on a *query census* (explicitly labelled as such — a statement about what a PubMed query returns, not about
biology) or on prose I quote.

---

## 2 · The direct answer

**Partly yes, and the part that is "yes" is not the part the therapeutic strategy needs.**
One laboratory — **Bednarek's group at the Medical University of Łódź, 2011** — did publish an assay of WWOX SDR
*catalysis itself*: bacterially expressed WWOX fusion proteins, a panel of steroid substrates, NAD⁺/NADP⁺ cofactor
dependence, and **Km values**. That is a genuine catalytic measurement and it is the only one in the literature;
**"WWOX enzymatic activity" returns exactly one record in all of PubMed, and this is it.** Two standing statements
in this repository — the 2026-09-20 verdict that no SDR *catalysis* assay exists anywhere, and the 2023 Battaglia
sentence LEGEND holds as a statement of absence — are therefore **too strong as stated and must be narrowed**.
But the paper does not answer the node's question: by its own abstract the activity was measured **"in a crude
extract"**, on **wild-type** protein, with **no disease allele**, and — on the abstract, which is all this
environment can reach — **no purified enzyme, no catalytically-dead triad control, and no per-molecule
normalisation**. Consequently: **no measurement anywhere, for any WWOX allele, normalises a functional output to
the amount of folded WWOX present**; no WWOX assay of any kind can tell "present but inert" from "absent"; and
there is **no deep-mutational-scanning, no VAMP-seq-class abundance map, no targeted mass-spectrometric absolute
quantification and no thermal-stability measurement on full-length WWOX** in the literature (query censuses, §3.4).
A transferable route does exist and it is well specified: the **Oxford Structural Genomics Consortium orphan-SDR
deorphanisation protocol** (purify → substrate screen → kinetics → structure), run by Oppermann — who is the last
author of a 2003 WWOX paper and therefore already sits one step from the target — combined, for the abundance half,
with the **VAMP-seq / Parkin-atlas** design. Both halves are cheap by the standards of this field. Neither has been
pointed at WWOX.

---

## 3 · Field-wide census of WWOX catalytic / functional measurement

Four criteria, in order. **A candidate fails if it fails any one.**
1 · measurable? · 2 · specific to **WWOX function** (not binding, localisation, conformation or a dye)? ·
3 · causally relevant to WOREE? · 4 · survives a **destabilising missense** allele — i.e. does it still return an
interpretable number when the protein is at or below the Western-blot detection floor?

### 3.1 · The candidate that is new to this node

| Candidate | Source | 1 measurable? | 2 WWOX-function-specific? | 3 causally relevant? | 4 survives a destabilising missense? | Verdict |
|---|---|---|---|---|---|---|
| **Steroid-dehydrogenase assay on bacterially expressed WWOX fusion proteins — NAD⁺/NADP⁺ dependence, defined steroid substrates, Km values** | **PMID 21476439** (abstract only) | ✅ **yes** — a rate, a cofactor dependence, and Km. This is the only quantity in the WWOX literature that is a *catalytic constant* | 🟡 **cannot be established from the abstract.** The activity is reported **"in a crude extract"** of a bacterial expression system. A crude *E. coli* lysate carries its own NAD(P)-dependent dehydrogenases; without a purified enzyme and a catalytically-dead triad mutant run side by side, the signal is not attributable to WWOX. The abstract names neither control. **Flagged, not scored.** | 🟡 indirect. Steroidogenesis is a documented *Wwox*-null phenotype, but no WOREE endpoint is attached and the paper is a cancer/fragile-site paper | ❌ **no, as run** — wild-type protein only, no allele tested, and a crude-extract format cannot normalise to folded monomer | **FAILS 4 outright; 2 unverifiable. But it is the only criterion-1 pass in the literature, and it is the correct starting point** |

**Adversarial notes on 21476439, stated before it is allowed to count for anything.**
- **Allele identity: none.** The abstract describes WWOX fusion proteins; **no variant, no residue, no missense** appears. It is not evidence about Q230P, L239R, P252A, P282A or G372R, and it must never be cited as such.
- **Replication: none found.** One paper, one group, 2011, in a low-visibility journal, with **no PMC deposit**. The WWOX mechanism corpus LEGEND has read does not build on it.
- **The field has not adopted it as the answer.** Reviews and primaries after 2011 continue to state the physiological substrate is unidentified (§5, locators L-5, L-6). That is not a contradiction — an *in vitro* activity on exogenous steroids is not a physiological substrate assignment — but it means this result **cannot be upgraded into "WWOX's substrate is known"**.
- **Promiscuity is a warning, not a feature.** The abstract states the SDR domain "is reactive both in the presence of NAD⁺ and NADP⁺ **for all examined steroid substrates**", while **no** reduction activity was seen with NADH/NADPH. An enzyme equally happy with both cofactors on every substrate tested is exactly what unsubtracted crude-extract background looks like. This may be a real dual-cofactor SDR; on the abstract alone it cannot be told apart from background.
- **Acquisition task, not a conclusion.** Reading the body of 21476439 — Methods (purification? controls?), substrate list, Km values with dispersion — is the single highest-value acquisition in this node. Routes that remain: author contact (Bednarek's group is still publishing on WWOX, 38 PubMed records), institutional/ILL access, WWOX Foundation.

### 3.2 · Candidates carried forward from prior LEGEND work — status unchanged by this census

| Candidate | Source | Verdict | Why |
|---|---|---|---|
| **GSK3β pull-down + inhibition of Tau S396/S404 phosphorylation** (`CLAIM 035`) | PMID 22193544 | **still the only WWOX-function readout with residue resolution** | Passes 1–3; **conditional on 4** — only in a purified format with activity normalised to folded monomer, which nobody has run. `CLAIM 035` itself records *"nessun allele WWOX-DEE è stato testato"* |
| **RedoxSensor Red CC-1 "oxidoreductase activity"** | PMID 34140629 | **FAIL (1,2,3,4)** | A cellular-redox dye on a stable overexpressing line. Unchanged by this census; if anything, weakened — the *actual* enzymology paper (21476439) uses defined substrates and cofactors and never appears in that corpus |
| **Binding panels** — TPC6AΔ/D3, Zfra, Tau, POLE4, BRCA1, MERIT40 | 27551439, 32764489, 15126504, 41124647, 27869163, 37248434 | **FAIL (2,4)** | `D-04`: a binding readout may be reporting occlusion rather than function; all are abundance-scaling |
| **Localisation** — mitochondria, Golgi, lipid raft, LAMP1 | 34140629, 24932569, 41124647 | **FAIL (2,4)** by construction | A degraded protein and a mistargeted protein score identically |
| **Intramolecular WW↔SDR FRET** | 34140629 | **not a function readout — a folding probe** | Correctly classified in the 2026-09-20 assessment; that classification stands |
| **Catalytic-triad point mutants S281A / Y293F / K297A** | 24932569, *"Aldaz laboratory unpublished observations"* | **FAIL** as published | No data shown; readout was perinuclear localisation. ⭐ **But see §8** — as *controls* for a real activity assay they become essential |
| **Cancer-cell functional panel** (colony formation, invasion, wound healing, comet, γH2AX, NHEJ reporter, xenograft) | 41124647, 27869163 | **FAIL (3,4)** | Cancer endpoints; and for P252A the readouts are confounded with abundance by the paper's own admission. `CLAIM 030`-class caution: **cancer-assay-dead is not neurologically null** |
| **WW1/WW2 NMR + ITC thermodynamics** | PMID 35716775 (`PAPER 055`) | **FAIL (2,3)** for SDR function — **but it is the field's only real biophysics** | Purified WWOX **WW fragments**, NMR, ITC, and an explicit stability result (WW2 stabilises WW1). LEGEND's own record notes **"nessuna WWOX full-length"** — nobody has ever purified full-length WWOX or the isolated SDR as folded protein and characterised it |

### 3.3 · Candidates sought and **not found** anywhere in WWOX

| Sought | Result | Basis |
|---|---|---|
| A WWOX **crystal or cryo-EM structure** | none surfaced | `WWOX structure` → 75 records, none a structure determination of WWOX or its SDR; the only experimental structural work is NMR on WW fragments (35716775), whose AlphaFold pose LEGEND already records as *"modellata, non risolta sperimentalmente"* |
| **Deep mutational scanning / VAMP-seq / any multiplexed assay of variant effect on WWOX** | **zero records** | query census: `WWOX deep mutational scanning multiplexed assay variant effect` → `total_count: 0` |
| **Targeted MS absolute quantification of WWOX** (PRM/SRM with heavy standard) | **zero records** | query census: `WWOX absolute quantification mass spectrometry parallel reaction monitoring` → `total_count: 0` |
| **Thermal-stability measurement on WWOX** (nanoDSF/CD/CETSA/TPP) | **zero records** | query census: `WWOX thermal shift proteome profiling melting` → `total_count: 0`; `WWOX protein degradation stability chaperone` → 2 records, neither a stability measurement of WWOX (35716775 is WW-fragment thermodynamics; 22634283 is not) |
| A **second** WWOX enzymology paper | **none** | query census: `WWOX enzymatic activity` → `total_count: 1` (=21476439); `WWOX NAD NADP cofactor` → `total_count: 1` (=21476439) |
| A **post-2023 WWOX missense functional study** that tests catalysis | none | `WWOX WOREE missense` 2023– → 3 records (38161429, 36779245, 30356099), none catalytic; `WWOX SDR domain` 2023– → 14 records across all years, of which the only primary enzymology is 21476439 |

🔴 **These are query censuses, not biological zeros.** They state what PubMed returns for these queries in this
environment on 2026-09-21. They do not exclude unindexed, preprint, thesis or supplementary material.

### 3.4 · The criterion-4 statement, unchanged and now field-wide

Every WWOX readout in existence — the binding panels, the localisation panels, the dye, the cancer assays, and
even the one catalytic assay as it was run — **requires the protein to be present at a level sufficient to be
detected**. For a Q230P-class allele it is not. Therefore **every one of them returns, for that allele, the same
number as a complete null, and that number is uninformative.** The distinction "inert" versus "absent" is the
entire question, and nothing in the literature measures it. The 2026-09-20 assessment reached this conclusion for
one corpus; extending the census to the whole field **does not soften it and does not produce a counter-example**.

---

## 4 · Transferable methods from adjacent fields

| # | Method | Disease / system it was developed in | What it measures | What it would need to transfer to WWOX | Cost / feasibility | Verdict |
|---|---|---|---|---|---|---|
| **T1** | **SGC orphan-SDR deorphanisation** — recombinant expression → purification → substrate screen → steady-state kinetics (Km) → apo/holo crystal structure → substrate docking | Human orphan SDRs **DHRS10** (PMID 17067289) and **DHRS6** (PMID 16380372), Oppermann lab, Oxford SGC | An activity, a substrate, a Km, and a fold — for a protein that previously had none | A purified WWOX SDR construct (or full-length), a substrate panel, NAD(P)⁺ cycling readout, and the **S281A/Y293F/K297A** triad mutants as the specificity control. The 21476439 steroid panel is a ready-made starting substrate set | **Low.** This is standard enzymology; the SGC ran it on dozens of orphans. No new technology | ⭐ **ADOPT — this is the cheapest valid route to criteria 1+2.** It is also the *only* route that can produce the active-site ligand that a migalastat-class chaperone (TX-003 family 1) requires |
| **T2** | **VAMP-seq** — GFP:mCherry ratiometric abundance of thousands of variants in one sorted pool | PTEN, TPMT (PMID 29785012); generalised | **Steady-state intracellular abundance per variant.** Explicitly *not* function | A WWOX ORF library and a landing-pad cell line | **Moderate** (one library, one sort, one sequencing run) | **TRIAL for the abundance axis only.** It would give, in one experiment, the abundance of every WWOX missense variant including Q230P, L239R, G372R and P282A — replacing a Western blot at its detection floor with a quantitative score. **It cannot answer "inert vs absent"** on its own |
| **T3** | **The Parkin proteostasis atlas** — VAMP-seq + proteasome/lysosome inhibitor arms + **temperature series (29 / 37 / 39.5 °C)** + degron tiling + QCDPred | Parkin / autosomal-recessive parkinsonism (PMID 38378758) | Abundance, degradation route, thermolability, and the *location of degrons* | Same as T2 plus inhibitor and temperature arms | **Moderate** — incremental on T2 | ⭐ **ADOPT as the template for the degradation half.** Its **29 °C arm** is a multiplexed low-temperature folding-rescue discriminator, exactly the experiment `proteostasis_rationale.md` §5 asks for, run at scale. **And it carries a cautionary negative LEGEND must import (§7, C-3)** |
| **T4** | **Two-dimensional DMS** — abundance map × activity map for the same protein, then joint clinical modelling | PTEN (PMID 32442409, integrating abundance and enzyme-activity DMS) | **Function-per-molecule, genome-wide** — the exact quantity this node asks for | An abundance assay (T2) **and a selectable WWOX function assay**. **WWOX has no selectable function assay.** This is the blocker | High, and **currently impossible** for WWOX | ❌ **BLOCKED until T1 or a GSK3β-docking selection exists.** Recorded because it is the destination |
| **T5** | **Fabry / migalastat HEK amenability assay** — transfect a GLA variant, ± chaperone, read **enzyme activity**, call the variant amenable or not | Fabry disease | Chaperone-responsiveness of a specific allele, scored on **activity**, not band intensity | An active-site-binding ligand and a substrate turnover readout. **WWOX has neither.** | Low *if* T1 succeeds; impossible before | ❌ **BLOCKED — downstream of T1.** `TX-003` already records migalastat as an *assay* precedent, not a mechanistic analogue; this census confirms the blocker is the missing substrate, not the missing molecule |
| **T6** | **TTR / tafamidis kinetic stabilisation** — measure the *dissociation rate* of the native oligomer | Transthyretin amyloidosis | Kinetic stability of the folded state | A folded, purifiable WWOX oligomer | Low–moderate | ⚠️ **Conceptually mismatched.** In TTR the *instability itself* is the pathology, so a stability readout is a disease readout. In WWOX the pathology is loss of function; a stability number alone would repeat the error this node exists to avoid |
| **T7** | **CFTR F508del correctors + low-temperature (27–30 °C) rescue**, read as channel function per unit mature protein | Cystic fibrosis | Rescue of trafficking **and** of specific activity | An electrophysiological-grade function readout. WWOX has none; the closest proxy is the GSK3β/Tau axis | High | 🟡 **Paradigm only.** Its transferable content is the *discipline* — never call a band-intensity increase a rescue — which LEGEND already holds |
| **T8** | **Targeted MS (PRM/SRM) with a heavy internal standard peptide** from a tryptic region unaffected by the variant | Generic clinical proteomics | **Absolute copy number** of the mutant protein, antibody-independent | A WWOX tryptic peptide not overlapping the variant, and a synthetic heavy standard | **Low** — a single assay development | ⭐ **ADOPT.** "Absent" and "below 2 % of wild type" are different molecular diseases with different interventions, and the current evidence base cannot tell them apart. Note `CLAIM 030` already flags that the allelic-series abundance measurements (WB on fibroblasts vs IF on organoids) are **not commensurable** |
| **T9** | **NanoBiT/HiBiT dual-tag: split-luciferase interaction signal normalised to a HiBiT abundance signal on the same construct** | Generic (no WWOX precedent found) | **An interaction output divided by the protein present — function per molecule, in cells, in one well** | The WWOX–GSK3β docking pair from `CLAIM 035` as the interaction; a HiBiT tag placed away from 388–407/L404 | **Low** — commercial reagents, no purification | ⭐ **TRIAL.** This is the cheapest cell-based route to a *ratio* rather than a level. It inherits `D-04` (a binding signal is not proof of catalysis) and must be declared as a docking-competence assay, never as "SDR activity" |

**The honest summary of this table.** For "**prove it still works**" the answer is T1 — and T1 is not a rescue
experiment at all, it is the *deorphanisation* that every rescue experiment is waiting on. For "**stabilise it**"
the answer is T2/T3, and T3 supplies its own warning that a small-molecule stabiliser may simply not work. The
canonical stabilise-and-prove-it-works templates (T5, T7) are **both blocked on the same missing object: a WWOX
substrate**. `proteostasis_rationale.md` §3 already named this as "the honest obstacle"; this census establishes
that it is not merely an obstacle to route 1 — **it is the rate-limiting object for the entire TX-003 class**.

---

## 5 · Verbatim locators

Every quotation below was copied from the fetched text in the same act. Where a token is uncertain, no quotation
marks are used.

| ID | Quotation | Source · section | Depth |
|---|---|---|---|
| **L-1** | *"Due to its potential role in sex-steroid metabolism, using two bacterial expression systems, we have cloned WWOX fusion proteins showing oxidoreductase activity in a crude extract, defined a course of enzymatic reactions for selected steroid substrates, and determined related Km values."* | PMID **21476439**, abstract | `abstract` |
| **L-2** | *"Our results show that the SDR domain of the WWOX protein has dehydrogenase activity and is reactive both in the presence of NAD+ and NADP+ for all examined steroid substrates. On the other hand, with the same substrates and reduced cofactors (NADH and NADPH) reduction activity was not observed."* | PMID **21476439**, abstract | `abstract` |
| **L-3** | *"Specifically, the p.Gln230Pro pathogenic variant affects the SRD domain and has been described both in homozygosity and in compound heterozygosity in eight cases overall (). Nevertheless, how missense variants affecting the SRD domain impair WWOX catalytic activity has not been demonstrated yet."* | PMID **38161429**, §2 *Genetic findings* | **`body`** |
| **L-4** | *"Nevertheless, the mechanistic effects of pathogenic variants on protein function are still not well known."* (italic gene symbol deleted by the extractor between "of" and "pathogenic") | PMID **38161429**, §5 *Discussion* | **`body`** |
| **L-5** | *"The more central short chain dehydrogenase/reductase domain is likely responsible for oxidation of small lipophilic substrates such as lipids or steroids, but the physiological substrate(s) for this domain have not been identified yet."* | Mondragon-Estrada *et al.* 2025, *Birth Defects Res*, **Discussion** | **`body`** (via Scholar Gateway passage) |
| **L-6** | *"The conserved NSYK motif in the SDR domain of WWOX is capable of interacting with androgens and estrogens and other proteins (;). At micromolar levels, exogenous E2 binds WWOX and induces activation of both WWOX and p53 via phosphorylation at Tyr33 and Ser15, respectively, in COS7 fibroblasts (;)."* | PMID **30158849**, §*Estrogen in the pY33-WWOX/pS15-p53 Complex* | **`body`** |
| **L-7** | *"Together, these observations suggest WWOX functions as an enzyme or a receptor involved in sex steroid metabolism to modulate disease progression."* | PMID **30158849**, §*WWOX as a Receptor for Sex Steroid Hormones for Signaling* | **`body`** — ⚠️ mood: *"suggest"* |
| **L-8** | *"WWOX probably functions as a protein chaperone to prevent protein misfolding and degradation by the ubiquitin/proteasome system."* | PMID **30158849**, §*Is WWOX a Molecular Chaperone?* | **`body`** — ⚠️ mood: *"probably"*; the section heading is itself a **question** |
| **L-9** | *"Because high abundance is a necessary, but not sufficient criterion for a variant to be functional, the abundance score is on its own not sufficiently powerful to separate all pathogenic and benign variants."* | PMID **38378758**, Discussion | **`body`** |
| **L-10** | *"However, at 29 °C the low abundance peak almost disappeared entirely and most variants now appeared stable (Fig.). Presumably this effect is the result of both an increased thermodynamic stability of the Parkin variants and a general reduction of protein turnover at the lowered temperature."* | PMID **38378758**, Results | **`body`** — ⚠️ *"Presumably"* |
| **L-11** | *"Thus, we wanted to explore whether the small positive modulator of WT Parkin activity, BIO-2007817, discovered in a recent in vitro study could confer stability to Parkin variants. **However, treatment with the activator did not confer any substantial differences in Parkin abundance (Fig.).** Accordingly, we note that BIO-2007817 was also unsuccessful in increasing mitophagy in cell-based studies, and might only stabilize variants localized to the region or domain where the compound binds."* | PMID **38378758**, Results | **`body`** |
| **L-12** | *"Hence, potentially blocking Parkin degradation or developing small molecule stabilizers or pharmacological chaperones, such as those for TP53 and CFTR, may restore cellular abundance and increase function above the pathogenic threshold."* | PMID **38378758**, Discussion | **`body`** — ⚠️ mood: *"potentially … may"*. A hypothesis, not a result |
| **L-13** | *"In vitro, DHRS10 converts NAD+ into NADH in the presence of oestradiol, testosterone and 5-androstene-3beta,17beta-diol."* and *"The crystal structure of the DHRS10 apoenzyme exhibits secondary structure of the SDR (short-chain dehydrogenase/reductase) family: a Rossmann-fold with variable loops surrounding the active site."* | PMID **17067289**, abstract | `abstract` |
| **L-14** | *"Substrate screening reveals sole NAD(+)-dependent conversion of (R)-hydroxybutyrate to acetoacetate with K(m) values of about 10 mm"* | PMID **16380372**, abstract | `abstract` |
| **L-15** | *"WOX1 possesses a tetrad NSYK motif in the C-terminal short-chain alcohol dehydrogenase/reductase (SDR) domain, which may bind estrogen and androgen."* | PMID **15580310**, abstract | `abstract` — ⚠️ mood: *"may bind"* |

---

## 6 · What LEGEND already knew — NEW findings separated from prior art

### 6.1 · Already held. Not re-reported as new.

- `CLAIM 035` — WWOX↔GSK3β docking at 388–407 with **L404 strictly necessary**, S9-independent, Tau-dependent; and its own admission that **no WWOX-DEE allele was tested**. It remains the only residue-mapped WWOX function readout.
- `CLAIM 030` — the allelic series (Q230P protein absent → severe; G372R barely detectable → mild; P47T normal protein, binding defect → mild) and the **non-commensurability** of the abundance measurements across it.
- `DIS-003` / `DL-MECH-029` — Johannsen 2018: normal transcript, protein not detected; **impaired translation vs premature degradation undiscriminated**.
- The whole P252A/P282A picture from PMID 41124647 (CHX chase with no reported t½, MG-132 negative, CQ/NH₄Cl positive, 3-MA negative, HSC70 co-IP, LAMP2A never manipulated, KFERQ motif never mutated, **no functional rescue tested**) — held in [`wwox_missense_cma_degradation_audit_20260921.md`](wwox_missense_cma_degradation_audit_20260921.md) and [`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md).
- **P282A = "stable but inert"** as a demonstrated SDR-span phenotype — the standing proof that abundance and function are separable in this domain.
- The Y293F/W44F–P47A dissociation from PMID 27869163, and the rule that a WW1-dependent assay cannot score an SDR allele.
- PMID 35716775 (`PAPER 055`) — read in full on 2026-07-26; WW2 stabilises WW1; **no full-length WWOX, no disease allele**.
- The Aldaz S281A/Y293F/K297A triad mutants as *"unpublished observations"* read out by localisation (PMID 24932569).
- The retracted ΔΔG band, the retracted misfolding-dominant tally, the withdrawn P47T read-across — [`proteostasis_rationale.md`](proteostasis_rationale.md) §4.
- `TX-003`'s own statement of the blocker: *"WWOX is an oxidoreductase with undefined physiological substrate/activity"*.
- PMID 38161429's sentence of absence (though **not in the wording LEGEND stores** — see §7, C-1).

### 6.2 · NEW this session

| # | Finding | Why it is new |
|---|---|---|
| **N-1** ⭐ | **A WWOX catalytic assay exists in the literature — PMID 21476439, Sałuda-Gorgul / Bednarek 2011 — with steroid substrates, NAD⁺/NADP⁺ dependence and Km values.** | LEGEND **has the PMID** (`CORPUS P306` / `LIT-0306`) but **not the content**: the record is title-only, tier **C**, `Priority: low / background`, `Filter decision: background only`, `Status: screened`, `Date processed: triage only`, discovered 2026-04-18 in the FASE-1 221–400 batch. **Zero claim links.** The one paper in the world whose title is literally *"WWOX oxidoreductase — substrate and enzymatic characterization"* is filed in this repository as background and has never been read. This is a **triage failure**, not an absence of coverage — and it is precisely the failure the hard rule about checking LEGEND first is designed to catch, operating in the opposite direction: LEGEND had the record and the record was wrong about itself. |
| **N-2** ⭐ | **The census is a singleton.** `WWOX enzymatic activity` → **1** record in PubMed. `WWOX NAD NADP cofactor` → **1** record. Both are 21476439. | Quantifies how thin the enzymology is: not "sparse", but **one paper, one group, once, in 2011**. |
| **N-3** ⭐ | **The SGC orphan-SDR deorphanisation protocol is a named, published, transferable template** (DHRS10 → 17β-HSD activity + crystal structure; DHRS6 → R-β-hydroxybutyrate dehydrogenase, Km ≈ 10 mM + 1.8 Å structure), and **Udo Oppermann, who ran it, is the last author of a 2003 WWOX paper (PMID 14555208)**. | The Oppermann lead in the brief resolves in an unexpected direction: 14555208 is an **apoptosis-signalling paper with no enzymology in its abstract**, so the thread does *not* lead to a WWOX characterisation — but it does establish that the world's leading orphan-SDR deorphanisation group had WWOX in hand in 2003 and the deorphanisation was never done. |
| **N-4** | **PMID 21476439 is unreachable in this environment, and the unreachability is established, not assumed** — three independent PMC checks returned null/empty. | Converts an untested assumption into a measured acquisition ceiling. |
| **N-5** | **No DMS, no VAMP-seq, no targeted-MS absolute quantification and no thermal-stability measurement exists for WWOX** (query censuses). | The 2026-09-20 assessment asked for these as *missing experiments*; this establishes that the absence is field-wide, not corpus-bounded. |
| **N-6** | **A 2025 independent paper (Mondragon-Estrada, *Birth Defects Res*) restates in its Discussion that the SDR's physiological substrates "have not been identified yet"** (L-5). | Tests the Battaglia-2023 statement of absence against 2023–2026 literature from an entirely unrelated field (spina bifida GWAS). **The absence still holds in late 2025.** |
| **N-7** ⚠️ | **PMID 38378758 contains a published NEGATIVE for the small-molecule-stabiliser hypothesis**: a compound that positively modulates wild-type Parkin activity *in vitro* **failed to increase the abundance of destabilised Parkin variants** (L-11). | A directly relevant cautionary precedent for `TX-003` from the best-executed proteostasis atlas in the literature: an activity modulator is **not** automatically a variant stabiliser. |
| **N-8** | **The 29 °C arm of the Parkin atlas is a multiplexed low-temperature folding-rescue assay** (L-10) — the experiment `proteostasis_rationale.md` §5 specifies for one allele, already demonstrated at library scale. | A ready-made protocol for a step LEGEND currently describes only in prose. |
| **N-9** | **The E2/NSYK "ligand" is a micromolar-affinity, phosphorylation-readout observation** (L-6), not a characterised active-site ligand. | Relevant to `TX-003` family 1: the nearest thing WWOX has to an active-site ligand is a weak, indirectly-read interaction — not a starting point for a migalastat-class chaperone. |
| **N-10** | **PMC4692203 (Aqeilan 2015 JBC review) and PMC1863559 (DHRS10) both return `full_text:""`** — PMCIDs exist, deposits are empty. | Two concrete instances of the failure mode the brief warned about, recorded so future sessions do not spend fetches on them. |

---

## 7 · Corrections against prior LEGEND text

| # | Standing LEGEND text | Correction | Basis |
|---|---|---|---|
| **C-1** 🔴 | LEGEND stores the Battaglia 2023 sentence, in three places, as *"how missense variants affecting the **SDR** domain impair WWOX catalytic activity has not been demonstrated yet"* (`discovery_ledger_current.md` lines 914 and 1022; `paper_registry_current.md` line 6491). | **Quotation-integrity defect. The source reads "SRD", not "SDR", in BOTH occurrences.** The source sentence is L-3. LEGEND correctly marks the *first* occurrence as an emendation (`S[D]R`) in two of the three places — and **silently normalises the second occurrence, inside the load-bearing clause, in all three.** The emendation is almost certainly right (the source has a typo), but a silent normalisation inside a quotation that the repository uses as a statement of absence is exactly the practice the discipline forbids. **Both occurrences should read `S[R→D]R` or be bracketed identically**; the ledger line 1022 also drops the bracket on the first occurrence. | PMID 38161429 body, read this session |
| **C-2** 🔴 | [`sdr_missense_readout_assessment_20260920.md`](sdr_missense_readout_assessment_20260920.md) §6: *"There is still **no substrate for the SDR's putative oxidoreductase activity** … Identifying a physiological substrate is the experiment that would make a genuinely complementary second readout possible. It is not in this corpus, and **on the census run here it is not anywhere**."* | **Narrow, do not retract.** The clause *"it is not anywhere"* is **too strong**. An *in vitro* substrate screen with Km values was published in 2011 (PMID 21476439, L-1/L-2). The correct statement is: **no *physiological* substrate has been assigned — a statement that independent sources still make in 2025 (L-5) — but an in-vitro steroid-substrate activity with kinetic constants has been reported once, in crude extract, on wild-type protein.** The assessment's own scope note (*"the census run here"* = the Chang/NCKU corpus) partly protects it; the sentence nonetheless reads as field-wide and was so read. | this census |
| **C-3** ⚠️ | `TX-003` scoring and [`proteostasis_rationale.md`](proteostasis_rationale.md) §3 present families 2 (kinetic/allosteric stabiliser) and 3 (proteostasis regulators) as the routes that *do not require knowing the natural ligand*, with the first experiment framed as *"a blind stability screen"*. | **Add a published counter-precedent.** In the Parkin atlas a small molecule that modulates wild-type enzyme activity *in vitro* **produced no substantial change in the abundance of destabilised variants** (L-11), and the authors' own explanation is that it "might only stabilize variants localized to the region or domain where the compound binds". A blind stability screen is still the right first move, but its **prior probability of success should be adjusted downward**, and the screen must be powered and controlled accordingly rather than treated as a formality. | PMID 38378758 |
| **C-4** ⚠️ | `CORPUS P306` / `LIT-0306`: `Tier: C`, `Priority: low / background`, `Filter decision: background only`, `clinical relevance: LOW`, `Role: background corpus only`, `Claim links: none`. | **Mis-triaged.** This is the only primary enzymology paper on the protein whose enzymology is the declared blocker of `TX-003`. **Flagged for re-triage and for the full-text queue at HIGH priority; not edited — this actor is read-only toward every registry.** | registry read, this session |
| **C-5** ℹ️ | The brief's framing of PMID 14555208 — *"If anyone ever characterised WWOX catalytically, this is the thread."* | **Thread followed; it does not lead there.** The 14555208 abstract describes Tyr33 phosphorylation, p53/JNK1 complexes and apoptosis — **no enzymology, no substrate, no kinetics**. Oppermann's authorship is real and the lead was worth pulling (it produced N-3), but the paper itself is not a catalytic characterisation. ⚠️ Abstract-only: a modelling or sequence-analysis section in the body cannot be excluded. | PMID 14555208 abstract |
| **C-6** ℹ️ | The brief's characterisation of PMID 15580310 as offering *"a PROPOSED SUBSTRATE CLASS (sex steroids)"*. | **Accurate, and weaker than it sounds.** The abstract's wording is *"may bind estrogen and androgen"* (L-15) — a **binding** proposal in the subjunctive, not a substrate assignment. The substrate-class claim that actually carries kinetic content is 21476439's, not 15580310's. | PMID 15580310 abstract |

---

## 8 · The single cheapest missing experiment

# Deorphanise the WWOX SDR domain, with the controls the 2011 paper did not have.

**Name:** an SGC-format orphan-SDR characterisation of the WWOX SDR domain, run on **purified protein** against a
**catalytically-dead triad mutant**, using the 2011 steroid panel as the starting substrate set.

**Why this and not the abundance experiments.** Every other candidate in this node — the abundance-clamped binding
panel, the VAMP-seq map, the CHX chase, the lysosomal-inhibitor arm, the targeted MS — measures *how much protein
there is* or *what it sticks to*. Not one of them measures whether the SDR does its job, because **there is no
assay of the SDR doing its job that has ever been run with a control**. Until that exists, "function per molecule"
has no numerator. `TX-003` cannot be designed, `T5` (Fabry-format amenability) cannot be run, `T4` (two-dimensional
DMS) has no second dimension, and the Q230P question — inert or absent — is unanswerable in principle, not merely
unanswered.

**The design, in four steps.**
1. **Express and purify.** The WWOX SDR domain (and, if it folds, full-length WWOX) in the two formats the 2011 paper used plus a eukaryotic one, and report the three numbers **nobody currently reports for any WWOX construct**: soluble yield per litre, thermal midpoint (nanoDSF or CD), monomer fraction (SEC-MALS). Note that even the field's structural-biology group has only ever purified **WW fragments** (`PAPER 055`), so this step is itself new.
2. **Repeat the 2011 substrate screen on purified enzyme.** Same steroid substrates, NAD⁺ and NADP⁺, NADH and NADPH, spectrophotometric cofactor cycling. The deliverable is a Km and a kcat with dispersion — replacing *"oxidoreductase activity in a crude extract"* (L-1) with a specific activity on a defined protein.
3. **Run the specificity control the 2011 paper could not have run.** **S281A, Y293F and K297A** — the Aldaz triad mutants, which exist as constructs and were published only as *"unpublished observations"* read out by localisation. In a purified assay they become the experiment's internal proof that the signal is WWOX catalysis and not lysate background. **This single addition is what converts an activity report into an assay.**
4. **Only then, the disease alleles.** Q230P, L239R and G372R expressed in the same system, with activity normalised **per mole of folded monomer** from step 1. An allele that yields no folded monomer is **absent, not inert**, and must be reported as absent rather than scored as a negative. P282A is the internal "stable but inert" positive control; L404A is the loss-of-docking control from `CLAIM 035`.

**What it would settle.** Whether WWOX has a measurable catalytic function at all; whether that function survives a
buried-core proline; and therefore whether the proposition at the base of `TX-003` — *"if the missense protein can
be kept from being degraded, there will be more functional WWOX"* — has a numerator. It would also produce, as a
by-product, the active-site ligand that a migalastat-class chaperone requires and that `proteostasis_rationale.md`
§3 correctly names as the obstacle to family 1.

**What it would not settle.** Anything about neurons, myelination, the developmental window, seizures or clinical
course. Anything about whether a drug exists. Whether the degradation route is CMA. And — critically — whether an
*in vitro* steroid activity is the **physiological** function: it would not be, and L-5 must stay attached to any
result. ⚠️ **A prerequisite, not a therapy.** Nothing in this section proposes an intervention.

**Cheapest non-blocking companion, if only one cell-based experiment can be funded instead:** **T9** — a
HiBiT-normalised NanoBiT WWOX↔GSK3β docking assay, giving an interaction signal divided by the protein present, in
one well, with no purification. It answers "inert vs absent" for the *docking* function specifically, and it
inherits `D-04`: it is a docking-competence readout and may not be reported as SDR catalytic activity.

---

## 9 · Declaration and attribution

Author: **Scientist A**. Date: **2026-09-21**. **READ-ONLY** toward every canonical file, registry, ledger and
queue: nothing was edited, no registry record was created or amended (C-4 is flagged, not applied), no receipt was
recorded, no commit candidate was produced, no git operation was performed. **This file is the single file
written.** **Nothing here is medical advice**; no compound, dose or intervention is proposed anywhere, and
chloroquine, ammonium chloride and 17β-estradiol appear only as mechanistic reagents or as literature objects.

**Declared limits.** No figure panel was inspected (`D-14`) — no finding rests on one. The most load-bearing paper
in this file (PMID 21476439) was read **only at abstract depth**; every statement about it is scoped to its
abstract and its Methods-level controls are **unknown, not absent**. Six of the papers cited were reached at
abstract or metadata depth only and are marked as such in §1. All "zero" statements in §3.3 are **query censuses**
of PubMed on 2026-09-21, explicitly not biological zeros, and none rests on a string count in extracted body text.
No supplementary material was retrieved for any paper.

*Article metadata and full texts **retrieved from PubMed / PubMed Central**; one Discussion passage retrieved via
Scholar Gateway.*

**DOIs.** Every DOI below was read from a PubMed metadata record retrieved in this session, **except** those for
22193544, 24932569, 29808465 and 34140629, which are carried over from
[`sdr_missense_readout_assessment_20260920.md`](sdr_missense_readout_assessment_20260920.md) and were not
re-verified here.

[21476439](https://pubmed.ncbi.nlm.nih.gov/21476439/) (no DOI in the PubMed record) ·
[15580310](https://doi.org/10.1038/sj.onc.1208124) ·
[14555208](https://doi.org/10.1016/s0006-2952(03)00484-2) ·
[15126504](https://doi.org/10.1074/jbc.M401399200) ·
[16380372](https://doi.org/10.1074/jbc.M511346200) ·
[17067289](https://doi.org/10.1042/BJ20061319) ·
[19708029](https://doi.org/10.1002/jcb.22298) ·
[22193544](https://doi.org/10.1038/cdd.2011.188) ·
[24520212](https://doi.org/10.7150/ijbs.7727) ·
[24932569](https://doi.org/10.1016/j.bbcan.2014.06.001) ·
[25537520](https://doi.org/10.18632/oncotarget.2961) ·
[25595187](https://doi.org/10.1177/1535370214565989) ·
[25595191](https://doi.org/10.1177/1535370214566747) ·
[26499798](https://doi.org/10.1074/jbc.R115.676346) ·
[27869163](https://doi.org/10.1038/onc.2016.389) ·
[29785012](https://doi.org/10.1038/s41588-018-0122-z) ·
[29808465](https://doi.org/10.1007/s10048-018-0549-5) ·
[30158849](https://doi.org/10.3389/fnins.2018.00563) ·
[30370248](https://doi.org/10.3389/fonc.2018.00420) ·
[31184403](https://doi.org/10.1002/humu.23838) ·
[32185845](https://doi.org/10.1002/cbic.202000032) ·
[32442409](https://doi.org/10.1016/j.ajhg.2020.04.014) ·
[34140629](https://doi.org/10.1038/s42003-021-02271-2) ·
[34359949](https://doi.org/10.3390/cells10071781) ·
[35716775](https://doi.org/10.1016/j.jbc.2022.102145) ·
[35883580](https://doi.org/10.3390/cells11142137) ·
[37248434](https://doi.org/10.1038/s41417-023-00626-x) ·
[38161429](https://doi.org/10.3389/fped.2023.1301166) ·
[38378758](https://doi.org/10.1038/s41467-024-45829-4) ·
[41124647](https://doi.org/10.1002/advs.202507602) ·
Mondragon-Estrada 2025 [10.1002/bdr2.70007](https://doi.org/10.1002/bdr2.70007).

---
---

# WAVE 2

**Actor:** Scientist A · **Date:** 2026-09-21 · Appended after Wave 1 was verified and accepted by the coordinator.
Wave 1 content above is unchanged. **Read-only toward every canonical file. Not medical advice.**

> **The coordinator's directionality correction is accepted and carried forward.** PMID 21476439's abstract states
> *"with the same substrates and reduced cofactors (NADH and NADPH) reduction activity was not observed."*
> **The 2011 assay ran OXIDATION ONLY.** Every activity-assay design below inherits that constraint — and, as §W2.1
> shows, it now also generates a direct conflict with the only competing substrate proposal in the literature.

---

## W2.0 · Read depth, Wave 2

| PMID | Identity | Receipt before reading | Depth reached | Body length returned | Figures |
|---|---|---|---|---|---|
| **25662954** | Farooq A (sole author), *Exp Biol Med (Maywood)* 2015;240(3) — "Structural insights into the functional versatility of WW domain-containing oxidoreductase tumor suppressor" · `CORPUS P376` / `LIT-0376`, Tier C, `background only` | `fulltext_receipts.py status --pmid 25662954` → **`[]`** (none) | 🔴 **PMCID PMC4374002 exists; deposit returns `full_text:""`** — abstract only | **0 B** | ❌ |
| **27339895** | Huang S-S … Chang N-S, *JBC* 2016;291 — "Role of WW Domain-containing Oxidoreductase WWOX in Driving T Cell Acute Lymphoblastic Leukemia Maturation" · `CORPUS P229` / `LIT-0229`, Tier C, `background only` | `fulltext_receipts.py status --pmid 27339895` → **`[]`** (none) | 🔴 **PMCID PMC5016130 exists; deposit returns `full_text:""`** — abstract only | **0 B** | ❌ |
| **40327201** ⭐ | Hammouz RY, Baryła I, Styczeń-Binkowska E, **Bednarek AK** (corresponding), *Funct Integr Genomics* 2025;25(1):100 — **"Twenty-five years of WWOX insight in cancer: a treasure trove of knowledge"** | not in LEGEND (no registry record surfaced) | 🟢 **full deposit read this wave** | **111,350 B** (measured) | ❌ |
| 25703206 · 24308844 · 22634283 · 16393779 | Farooq-lab WWOX primaries (allostery; ErbB4; WBP1/WBP2; WW review) | 25703206 **already read in full by LEGEND** (discovery ledger L1157) | ⚪ metadata/abstract only this wave | n/a | ❌ |
| 18974271 | Aqeilan RI *et al.*, *Endocrinology* 2009 — impaired steroidogenesis in Wwox-null mice · **`PAPER 076`** | ✅ **`FTR-20260811-18974271-01`, `complete_fulltext_read`** — LEGEND has read it | ⚪ abstract + LEGEND record only this wave (no re-read needed) | n/a | ❌ |
| 35290621 · 42589397 · 41007296 · 37781246 · 36979157 | Lodz/Bednarek post-2011 output sample | — | ⚪ metadata/abstract only | n/a | ❌ |

⚠️ **Extractor state for PMID 40327201, declared before its zeros are used.** The **reference list is ABSENT** from
the extracted surface (no `References` heading; the text ends mid-conclusion). **Therefore no citation attribution
is traced or reconstructed from this paper, and the zero counts for `Sałuda`/`Gorgul` are INADMISSIBLE** — a
citation to 21476439 would live in exactly the section the extractor removed. Only **roman-class body-prose**
counts are used below (`substrate`, `Km`, `cofactor`, `NAD`, `steroid`, `retinal`, `retinoid`), and each is
reported as a count in running prose, not as a claim about the bibliography.

---

## W2.1 · Task 1a — PMID 25662954 bounds my Wave 1 statement, and produces a SECOND substrate proposal

### The finding

**Wave 1 said there is no WWOX crystal structure and that the field's structural group has only purified WW
fragments. That stands — and LEGEND already knew it better than I did.** The discovery ledger states at line 1239:
*"Nessuna struttura di WW1. Nessuna del modulo tandem (ecco perché Farooq/Sudol hanno dovuto modellare per omologia
da FBP21). **Nessuna, in oltre vent'anni, del dominio SDR** — quello che contiene Q230P, che determina la gravità,
e che è il nostro bersaglio terapeutico."* **This is prior art, not a Wave 2 finding**, and Wave 1 should have
cited it rather than re-deriving it from PubMed queries.

**What 25662954 adds is not structural. It is a second, competing substrate assignment**, and LEGEND holds nothing
on it — `grep -i "all-trans-retinal|retinoid|retinal oxidoreductase|retinaldehyde"` across
`discovery_ledger_current.md`, `therapeutic_hypotheses_ledger_current.md`, `dismissal_ledger_current.md` and
`claim_registry_current.md` returns **nothing**.

| Locator | Quotation | Source · section | Depth |
|---|---|---|---|
| **W-1** ⭐ | *"Equally importantly, structure-guided functional approach suggests that the catalytic domain of WWOX likely serves as a retinal oxidoreductase that catalyzes the reversible oxidation and reduction of all-trans-retinal."* | PMID **25662954**, abstract | `abstract` |

### 🔴 FLAGGED, NOT SCORED — five verification failures, stated before any use

1. **It is a review, and the body is unreachable.** PMC4374002 returns `full_text:""`. *"Structure-guided functional approach"* is not a method I can inspect. Whether it means homology modelling, docking, sequence-motif comparison or an unpublished experiment **cannot be determined from the abstract**.
2. **There is no primary paper behind it, from that lab or any lab.** Farooq has **five** WWOX-indexed publications in PubMed (25703206, 25662954, 24308844, 22634283, 16393779). The other four are **all WW-domain biophysics** — ITC, NMR, PPXY ligands, WW1/WW2 allostery. **Not one is a catalytic-domain paper.** `Farooq A[Author] AND WWOX` → 5 records, censused.
3. **No independent literature exists.** `WWOX all-trans-retinal` → **1 record** (= 25662954 itself). `WWOX retinal retinoid all-trans-retinal oxidoreductase` → **1 record** (= itself). A Scholar Gateway semantic query on WWOX-as-retinal-oxidoreductase returned WWOX passages that describe the SDR only as a steroid-metabolising or protein-binding domain, **none mentioning retinal**. *(Query censuses, not biological zeros.)*
4. **Mood.** *"suggests … likely serves as"*. A proposal in the subjunctive, twice hedged, in an abstract, in a review. It is the same grammatical class as PMID 15580310's *"may bind estrogen and androgen"* (Wave 1, L-15).
5. 🔴 **It directly conflicts with the only measurement in the field.** W-1 claims *"reversible oxidation **and reduction**"*. PMID 21476439 measured, on WWOX fusion protein: *"with the same substrates and reduced cofactors (NADH and NADPH) **reduction activity was not observed**"* (Wave 1, L-2). One of these is wrong, or they concern different conditions — **and nobody has ever run an experiment that could tell.**

### Verdict on the four criteria

| Candidate | 1 measurable? | 2 WWOX-function-specific? | 3 causally relevant? | 4 survives destabilising missense? | Verdict |
|---|---|---|---|---|---|
| **"WWOX SDR is a retinal oxidoreductase acting reversibly on all-trans-retinal"** (PMID 25662954) | ❌ **no measurement exists** — no rate, no Km, no cofactor data, no protein | ❌ unverifiable | ⚪ unknown | ❌ | **NOT AN ASSAY. A hypothesis with no primary source, conflicting with the field's only data.** Recorded as a **lead**, scored at zero |

### Why it is still worth recording

Because it is **cheap to test and it would discriminate**. If the WWOX SDR is a retinaldehyde-handling enzyme it
belongs to the **RDH sub-branch** of the SDR family — the branch that contains **RDH12**, whose missense variants
cause a childhood retinal dystrophy. And WOREE carries **optic atrophy in 13/13 in the Oliver cohort** and retinal
degeneration across reports (Wave 1 prior art). ⚠️ **That convergence is NOT built here.** It rests on an
unsourced subjunctive clause in an unreachable review, it contradicts the field's only measurement, and a
phenotypic coincidence between "the eye is affected" and "the substrate might be retinal" is exactly the kind of
bridge this node was told to refuse. **Its only legitimate use is as a second substrate to include in the
substrate panel of the §8 experiment** — all-trans-retinal costs one extra well.

---

## W2.2 · Task 1b — PMID 27339895 carries no per-molecule measurement

**Identity:** Chang/NCKU T-cell acute lymphoblastic leukaemia maturation paper (MOLT-4 cells, naïve mouse spleen).
By its abstract it reports Tyr-33-phosphorylated WWOX binding non-phosphorylated ERK and IκBα, complex localisation
partly in mitochondria, WWOX preventing IκBα proteasomal degradation, a phosphorylation time course (Tyr-33,
Tyr-287, Ser-14), CD3/CD8 expression, and **time-lapse FRET** binding-strength measurement.

**Judgement: NO.** Every readout is **binding, phosphorylation state, localisation or FRET** — the four categories
Wave 1 §3.2 already disqualifies on criteria 2 and 4. There is no catalytic measurement, no substrate, no
normalisation to protein amount, and no variant of any kind. It is a **Chang-corpus paper of exactly the type
already adjudicated on 2026-09-20**, and it changes nothing. Its one point of interest is directional and
peripheral: WWOX here *prevents* proteasomal degradation of a partner (IκBα), which is the same "WWOX as chaperone"
motif the Chang corpus asserts elsewhere in the subjunctive (Wave 1, L-8) — WWOX protecting another protein, never
WWOX's own turnover being measured.

**Reading it was still correct**, and the negative is productive: the fixed lens surfaced it, it was checked, and
it is now disposed of with a reason rather than left as an open "might be relevant" stub.

---

## W2.3 · Task 2 — Was the 2011 enzymology ignored, or abandoned?

### The answer is a third option, and it is the good one: **orphaned, not overturned.**

**No replication, no extension, and — decisively — NO FAILED REPLICATION EXISTS TO FIND.**

| Probe | Result |
|---|---|
| `WWOX enzymatic activity` | **1** record (= 21476439) *(Wave 1)* |
| `WWOX NAD NADP cofactor` | **1** record (= 21476439) *(Wave 1)* |
| `WWOX 17beta-hydroxysteroid dehydrogenase estradiol oxidation Km` | **0** records |
| `WWOX all-trans-retinal` | **1** record (= the Farooq review, §W2.1) |
| `WWOX estradiol` | **4** records — 35290621, 30158849, 15580310, 15126504. **None is enzymology**: one Lodz CAGE-transcriptomics paper and three Chang-corpus binding/signalling papers |
| `Bednarek oxidoreductase activity Km steroid Lodz` | **5** records — 36271927, 35290621, 32581702, 25892250, 21476439. Only the last is the enzymology paper |
| `Bednarek AK[Author] AND WWOX`, 2011– | **38** total WWOX papers; **27 published after the enzymology** |

⚠️ `find_related_articles(link_type='pubmed_pubmed')` on 21476439 returns 83 neighbours, **but that is a
word-weighted similarity list, explicitly not a citation index.** It cannot answer "who cited this" and is not
used as if it could. No citation database was reachable in this environment.

### The decisive evidence: the originating lab's own 25-year retrospective

**PMID 40327201 — Hammouz, Baryła, Styczeń-Binkowska & Bednarek, *Funct Integr Genomics* 2025, "Twenty-five years
of WWOX insight in cancer: a treasure trove of knowledge"** — Bednarek corresponding, Medical University of Łódź.
**111,350 B of body read this wave.** Roman-class counts in that body:

| `substrate` | `Km` | `cofactor` | `NAD` | `steroid` | `retinal` | `retinoid` | `enzym*` | `catalyt*` | `oxidoreduct*` | `SDR` |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | **0** | **0** | **0** | **0** | **0** | **0** | 1 | 1 | 2 | 4 |

**In a 111 KB retrospective covering twenty-five years of WWOX, by the laboratory that performed the only WWOX
catalytic characterisation in existence, the word "substrate" does not occur once.** And every one of the four
`SDR` occurrences describes it as an **interaction surface**, not a catalytic unit:

| Locator | Quotation | Source · section | Depth |
|---|---|---|---|
| **W-2** ⭐ | *"The gene encodes a protein that contains two WW domains and a short-chain dehydrogenase/reductase (SDR) domain, **which facilitates interactions with multiple protein partners**."* (italic gene symbol deleted by the extractor before "gene") | PMID **40327201**, Introduction | **`body`** |
| **W-3** ⭐ | *"The protein product of features two N-terminal WW domains and a C-terminal SDR domain **that enables it to engage with various partner proteins and modulate their activities**—essential for maintaining cellular homeostasis and inhibiting tumour development (Khawaled et al.)."* (italic gene symbol deleted after "of") | PMID **40327201**, Introduction | **`body`** |
| **W-4** | *"WWOX acts as a critical bridge connecting Hyal-2 and Smad4 within TGF-β signalling pathways; Hyal-2 interacts with the N-terminal Tyr33-phosphorylated WW domain of WWOX while **Smad4 binds to its SDR domain** (Hsu et al.)."* | PMID **40327201**, body | **`body`** |
| **W-5** | *"For instance, the SNP rs12918952 in exon 5 of the WWOX gene has been implicated in enhancing vascular invasion in hepatocellular carcinoma by **modifying catalytic activity** and reducing WWOX mRNA expression."* | PMID **40327201**, body | **`body`** — the review's **only** use of "catalytic", and it is about a third party's SNP association, not about their own enzymology |

### But they did not disown it either

| Locator | Quotation | Source · section | Depth |
|---|---|---|---|
| **W-6** | *"WWOX is a tumor-suppressive **steroid dehydrogenase**, which relationship with hormone receptors was shown both in animal models and breast cancer patients."* | PMID **35290621** (Pospiech … **Nowakowska** … Bednarek, *J Appl Genet* 2022), abstract, opening sentence | `abstract` |

**Magdalena Nowakowska, third author of the 2011 enzymology paper, is a co-author of this 2022 paper.** The
enzymatic identity is therefore still asserted by the originating lab as late as 2022 — **as a background
descriptor in a sentence of a transcriptomics paper**, with no enzymology anywhere in it.

### What this means, stated exactly

**The 2011 result was not tested and found wanting. It was assumed, then quietly dropped.** The trajectory is:
*measured once (2011) → asserted as background without re-measurement (2022) → vocabulary removed entirely from the
lab's own definitive retrospective (2025), the SDR reframed from a catalytic domain into a protein-interaction
surface.*

🔵 **This is the better of the two outcomes the coordinator posed, and materially so.** Had somebody tried and
failed to reproduce it, the experiment in Wave 1 §8 would be attempting something a laboratory has already shown
does not work, and the prior would collapse. Instead **there is no negative result in the literature to find**: the
measurement is neither corroborated nor refuted, it is **orphaned**. The §8 experiment is therefore not a
re-tread — it is the **first controlled** test of a fourteen-year-old uncontrolled observation, and the absence of
a failed-replication literature is a reason to run it, not a reason to discount it.

⚠️ **The limit on this conclusion.** The reference list of PMID 40327201 was stripped by the extractor. I cannot
state that the review does not *cite* 21476439 — only that its **body prose contains no substrate, cofactor,
kinetic or steroid vocabulary at all**, which is a statement about how the SDR is *described*, not about the
bibliography. And no citation database was reachable here; a proper forward-citation census remains an open task.

---

## W2.4 · Task 3 — Neurosteroids: **the bridge does not exist. Reporting it dead.**

**Direct answer: there is NO evidence that neural WWOX acts on a steroid. None. The allopregnanolone / GABA-A
convergence is not built, and must not be built.**

**LEGEND first.** `neurosteroid`, `allopregnanolone`, `pregnenolone`, `DHEA` across
`discovery_ledger_current.md`, `therapeutic_hypotheses_ledger_current.md`, `dismissal_ledger_current.md`,
`claim_registry_current.md` and `working_model_current.md` → **no occurrence**. LEGEND has never entertained it.

**Then the field.** `WWOX neurosteroid` → **0 records in PubMed**. *(Query census.)*

**The four things that could be mistaken for evidence, and why each is not:**

1. **PMID 18974271 (`PAPER 076`) — "impaired steroidogenesis" in Wwox-null mice.** 🔴 **This is the trap, and LEGEND already read the paper in full** (`FTR-20260811-18974271-01`). Its abstract reports *failure of Leydig cell development in testis and reduced theca cell proliferation in ovary*, and *impaired gene expression of key steroidogenesis enzymes* by Affymetrix microarray. That is **WWOX acting upstream, on the transcription and development of other steroidogenic enzymes** — **not** WWOX catalysing a steroid. It is **gonadal, not neural**. And LEGEND's own record already states the disqualifying confound: *"gonadal autonomy cannot be separated from pituitary suppression, developmental delay and terminal systemic illness."* Nothing here touches the brain or WWOX catalysis.
2. **The 2011 enzymology itself.** Its stated premise is *"its potential role in sex-steroid metabolism"* (L-1), and WWOX expression is highest in **testis, prostate and ovary** (21476439 abstract). The substrates were exogenous steroids added to a bacterial crude extract. **The experiment was designed around gonadal biology and says nothing about brain.**
3. **The E2/NSYK interaction.** Wave 1, L-6: *binding*, at **micromolar** concentrations, in **COS7 fibroblasts**, read out by **Tyr33/Ser15 phosphorylation**. A binding-and-phosphorylation observation in a fibroblast line is not steroid catalysis and is not neural.
4. **Phenotypic adjacency.** WOREE is a GABAergic disease (GAD65/67 reduction, interneuron impairment) and neurosteroids modulate GABA-A. **Both halves are true and there is nothing joining them.** A shared endpoint is not a shared mechanism.

🔴 **Recorded as a dead lead, deliberately.** It is attractive, it is mechanistically tidy, and there is no
evidence for it. Writing it down as dead is worth more than leaving it un-asked, because the next session will
think of it too.

---

## W2.5 · Task 4 — Acquisition routing for PMID 21476439

**Bibliographic identity, for an interlibrary-loan or author request, exactly as PubMed carries it:**
Sałuda-Gorgul A, Seta K, Nowakowska M, Bednarek AK. *WWOX oxidoreductase — substrate and enzymatic
characterization.* **Z Naturforsch C J Biosci. 2011;66(1–2):73–82.** PMID 21476439.
⚠️ **The PubMed record carries NO DOI and NO PMCID.** I have not guessed either. The journal (*Zeitschrift für
Naturforschung C*) is published by De Gruyter; a DOI probably exists at the publisher and should be looked up
rather than constructed.

**Who to ask, in priority order:**

| # | Route | Contact / mechanism | Why this one |
|---|---|---|---|
| **1** ⭐ | **Corresponding author, still active** | **Andrzej K. Bednarek**, Department of Molecular Carcinogenesis, Medical University of Łódź, Poland. 🔴 **The corresponding e-mail is deliberately NOT reproduced here.** It is printed in the author block of `PMID 40327201` (2025) and `PMID 35290621` (2022) and is one metadata call away for whoever is authorised to make contact. *This edition is public; a living researcher's contact address is not ours to republish, and the `public_release_gate` refused this file until it was removed — correctly.* | Last author of the target paper and **still publishing on WWOX in 2025–2026**. The highest-yield route by a wide margin |
| **2** | **Surviving co-author at the same institution** | **Magdalena Nowakowska**, third author of the 2011 paper, still co-authoring Lodz WWOX papers (PMID 35290621, 2022) | A second address in the same department if (1) does not answer |
| **3** | **First author** | Anna Sałuda-Gorgul, then at Department of Analytical Chemistry, Medical University of Łódź, Muszyńskiego 1, 90-151 Łódź *(affiliation as printed on the 2011 paper — may be stale)* | The person who ran the assays; most likely to hold raw data |
| **4** | Interlibrary loan / institutional access to *Z Naturforsch C* 66(1–2):73–82 | any academic library | Gets the PDF but not the raw data or the unreported controls |

**What to ask for — three specific items, not "the paper".** The numbering of figures and tables is unknown
because the body is unreachable, so each is named by **content**:

1. ⭐ **The table (or figure) reporting the Km values**, with: the identity of every steroid substrate tested, which cofactor (NAD⁺ or NADP⁺) each Km belongs to, the units, and the dispersion or replicate number. *This is the single most valuable object.* Wave 1 could establish only that Km values exist, never what they are; a Km in the low-micromolar range versus the millimolar range is the difference between a plausible physiological activity and an artefact. (For calibration: DHRS6's physiologically-argued Km is *"about 10 mm"* — Wave 1, L-14.)
2. ⭐ **The Methods subsection describing protein preparation and the assay control**, answering three questions the abstract leaves open and on which everything downstream depends: *(a)* were the fusion proteins **purified**, or was activity measured in the crude extract as the abstract says? *(b)* what **negative control lysate** was used — empty vector, untransformed host, or none? *(c)* was any **catalytically inactive WWOX mutant** run as a control? If the answer to (c) is "none", the §8 experiment's triad-mutant arm is not a refinement, it is the first specificity control this result has ever had.
3. **Whether all-trans-retinal or any retinoid was among the substrates screened** — a one-line question that would immediately adjudicate the conflict in §W2.1 between the 2011 oxidation-only steroid result and the Farooq retinal proposal.

**A fourth ask, if the authors are willing:** whether any **unpublished** follow-up exists — a purification that
did not work, a substrate that gave no signal, a reviewer's objection. Given §W2.3, an unpublished negative in
that lab's files is the single most decision-relevant document that could exist for this node, and it is
invisible to every census.

---

## W2.6 · Task 5 — Re-scoring the Łódź / Bednarek node

**Answer: the prior scout's demotion was CORRECT about the laboratory, and it asked the wrong question. Both halves
need to be said, and the second does not overturn the first.**

`next_scientist_scout_20260921.md` demoted Łódź as *"predominantly oncology"* whose *"developmental line does not
exist as a line"*. **On the evidence, that characterisation of the lab's present work is right and, if anything,
understated.** The post-2011 Łódź output sampled this wave is: TCGA/RNA-seq prognostic modelling in breast and
ovarian cancer (42589397, 2026), WWOX/HIF1α ratio pathway analysis (41007296, 2025), a cancer retrospective review
(40327201, 2025), glioblastoma cell-line transcriptomics (37781246, 2023; 36979157, 2023), and CAGE transcriptomics
in breast cancer lines (35290621, 2022). This is a **bioinformatics and cancer-transcriptomics group**. There is no
developmental line, no neuronal model, no WOREE allele, and — per §W2.3 — **no enzymology anywhere in it for
fourteen years**. Nothing in Wave 2 argues for re-promoting Łódź as a *biological collaborator* for a
neurodevelopmental disease.

**But the node's value was never going to be biological, and that is what the scout did not ask.** Bednarek is last
author of the **only WWOX catalytic characterisation in existence**, and he is **reachable, corresponding, and
publishing now**. That makes the node valuable along one axis and one axis only:

| Axis | Standing | Change |
|---|---|---|
| Biological collaborator for a neurodevelopmental WWOX model | **LOW** — no developmental line, no neuronal model, no disease allele | **unchanged.** The scout was right |
| Enzymology capability, *today* | **LOW** — `substrate` 0, `Km` 0, `cofactor` 0, `NAD` 0 across a 111 KB 2025 retrospective; the SDR is now described four times as a protein-interaction surface (W-2 … W-5) | **unchanged, and now evidenced rather than assumed** |
| **Custodian of the only WWOX catalytic dataset, and of what was never published about it** | **HIGH** | ⬆️ **This is new, and it is the only thing that changes.** |

**So: the node is re-scored as an ACQUISITION target, not a collaboration target.** Its value is §W2.5 items 1–3
plus the unpublished-negative question — the Km table, the Methods controls, and whether a retinoid was ever
tested. Those are three e-mails, not a partnership. **Standing as a scientific node: unchanged and low. Standing as
the address of a specific missing document: high, and time-sensitive** — a 2011 dataset whose authors are still
contactable will not stay that way indefinitely.

Stated plainly, as instructed: **this does not rehabilitate Łódź as a research partner, and Wave 2 should not be
read as arguing that it does.**

---

## W2.7 · What LEGEND already knew — Wave 2 separation

**Already held, and Wave 1 under-credited one of them:**
- 🔴 **"No structure of the SDR domain in over twenty years"** — `discovery_ledger_current.md` L1239, including the reason Farooq/Sudol homology-modelled from FBP21. **Wave 1 re-derived this from PubMed queries and presented it as a census result. It is prior art and should have been cited as such.** Correction C-7 below.
- PMID 25703206 (Farooq allostery) read in full; Farooq-lab WW-domain work known, with deep-dive manifests for 24308844 and 22634283.
- PMID 18974271 read in full as `PAPER 076` with its confound recorded (`CLAIM 036`).
- The whole Chang-corpus disqualification that 27339895 falls under.

**New this wave:**

| # | Finding |
|---|---|
| **N-11** ⭐ | **A second, competing substrate proposal exists — all-trans-retinal (PMID 25662954)** — absent from every LEGEND ledger and registry, unsupported by any primary paper from any lab, and **in direct conflict with the 2011 oxidation-only result**. Scored at zero; carried as a substrate to include in the §8 panel. |
| **N-12** ⭐ | **The 2011 enzymology is orphaned, not overturned.** No replication, no extension, **and no failed replication** — so the §8 experiment is the first controlled test, not a re-tread. |
| **N-13** ⭐ | **The originating lab silently reframed the SDR from a catalytic domain to an interaction surface** between 2022 (W-6, still "steroid dehydrogenase") and 2025 (W-2…W-5, interaction surface only; `substrate` 0 in 111 KB). |
| **N-14** | **PMID 27339895 carries no per-molecule measurement** — a clean, disposed negative. |
| **N-15** | **The WWOX-neurosteroid bridge does not exist** (`WWOX neurosteroid` → 0), and the one in-vivo steroid phenotype is transcriptional, gonadal and confounded. Recorded dead. |
| **N-16** | **Acquisition routing resolved to a live, corresponding-author e-mail** and three content-named documents (§W2.5). |
| **N-17** | **Two more PMCIDs returning `full_text:""`** (PMC4374002, PMC5016130) — four now catalogued across both waves. |

---

## W2.8 · Corrections — Wave 2 additions

| # | Standing text | Correction | Basis |
|---|---|---|---|
| **C-7** 🔴 | **Wave 1 §3.3** presented *"no WWOX crystal or cryo-EM structure surfaced"* as a fresh query census. | **Under-attributed.** LEGEND already held this, more precisely and with the reason, at `discovery_ledger_current.md` L1239 — *"Nessuna, in oltre vent'anni, del dominio SDR"*. Wave 1's census **corroborates** prior art; it did not discover it. This is a self-correction of the kind hard rule 1 exists to force. | discovery ledger, read this wave |
| **C-8** 🔴 | **Wave 1's census query set** was steroid-, cofactor- and stability-shaped (`WWOX enzymatic activity`, `WWOX NAD NADP cofactor`, `WWOX steroid metabolism sex hormone`, `WWOX SDR domain`). | **It had no retinoid vocabulary, and therefore could not have found PMID 25662954's substrate claim** — the same failure class as `unread_gold.py`'s `MECHANISM_RE` having no catalysis vocabulary. **A census is only as wide as its vocabulary, and Wave 1's statement that the substrate question is closed at "steroids or nothing" was an artefact of my query terms.** Any future WWOX substrate census must carry retinoid, lipid, fatty-acid, prostaglandin and xenobiotic terms as well. | this wave |
| **C-9** ⚠️ | Wave 1 §3.1 treated *"the field has not adopted it"* as the status of the 2011 result. | **Sharpen.** The originating lab **did** keep asserting it as background as late as 2022 (W-6), then dropped the vocabulary entirely by 2025 (W-2…W-5). "Not adopted by the field" understates it: **it was asserted without re-measurement, then abandoned without comment, by its own authors.** | PMIDs 35290621, 40327201 |
| **C-10** ⚠️ | `CORPUS P376` (Farooq 2015) and `CORPUS P229` (Huang 2016) are Tier C, `background only`, zero claim links. | **P376 is mis-triaged** — it carries the only competing substrate assignment for the protein's catalytic domain, and should be re-triaged alongside `CORPUS P306`. **P229 is correctly triaged** and this wave confirms it: Tier C background is the right place for it. **Flagged, not applied — read-only actor.** | this wave |

---

## W2.9 · Effect on the Wave 1 §8 experiment

The experiment is **unchanged in structure and strengthened in three places**:

1. **The substrate panel gains a second class and a directionality test.** Run the 2011 steroid panel **and
   all-trans-retinal**, and run **both directions** — NAD(P)⁺ oxidation *and* NAD(P)H reduction — because the two
   proposals in the literature disagree precisely on reversibility (L-2 versus W-1). One extra dimension on a plate
   adjudicates a fourteen-year-old ambiguity that no one has ever addressed.
2. **The triad-mutant arm is upgraded from "a refinement" to "the first specificity control this result has ever
   had"**, pending the answer to §W2.5 item 2(c).
3. **The prior is better than Wave 1 assumed.** There is no failed-replication literature. The measurement is
   orphaned, not refuted.

**And one thing it must not become.** Nothing in Wave 2 licenses a retina/optic-atrophy mechanism for WOREE, and
nothing licenses a neurosteroid/GABA-A mechanism. Both were looked for; the first has no primary source and
contradicts the only data; the second returns zero records. **Both are recorded dead in this file precisely so
that they are not rediscovered as exciting.**

---

## W2.10 · Wave 2 declaration

Author: **Scientist A**. Date: **2026-09-21**. **READ-ONLY** toward every canonical file, registry, ledger and
queue: nothing was edited, no registry record created or amended (C-10 flagged only), no receipt recorded, no
commit candidate produced, no git operation performed. `framework/scripts/unread_gold.py` was **not** touched.
**This file remains the single file written.** **Not medical advice.**

**Declared limits, Wave 2.** No figure panel inspected. PMID 25662954 and PMID 27339895 were reachable **only at
abstract depth** (both deposits empty, 0 B) — every statement about them is scoped accordingly, and the mechanism
behind *"structure-guided functional approach"* is **unknown, not absent**. The reference list of PMID 40327201 is
absent from the extracted surface, so **no citation attribution is claimed or reconstructed** and author-name zeros
are inadmissible; only roman-class body-prose counts are used. `find_related_articles` similarity output was not
used as a citation index. All "zero" statements are **PubMed query censuses on 2026-09-21**, not biological zeros.
No forward-citation database was reachable; a true citation census of PMID 21476439 remains open.

*Article metadata and full texts **retrieved from PubMed / PubMed Central**; one semantic-search pass via Scholar
Gateway.*

**Wave 2 DOIs** (all read from PubMed metadata records retrieved this wave):
[16393779](https://doi.org/10.1080/15216540500389039) ·
[18974271](https://doi.org/10.1210/en.2008-1087) ·
[22634283](https://doi.org/10.1016/j.jmb.2012.05.015) ·
[24308844](https://doi.org/10.1021/bi400987k) ·
[25662954](https://doi.org/10.1177/1535370214561586) ·
[25703206](https://doi.org/10.1002/jmr.2419) ·
[27339895](https://doi.org/10.1074/jbc.M116.716167) ·
[35290621](https://doi.org/10.1007/s13353-022-00690-3) ·
[36979157](https://doi.org/10.3390/biology12030465) ·
[37781246](https://doi.org/10.3389/fnins.2023.1260409) ·
[40327201](https://doi.org/10.1007/s10142-025-01601-5) ·
[41007296](https://doi.org/10.3390/biology14091151) ·
[42589397](https://doi.org/10.3390/ijms27156740).
**PMID 21476439 carries no DOI in its PubMed record** and none is constructed here.
