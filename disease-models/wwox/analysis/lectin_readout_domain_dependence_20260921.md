# Is the WWOX lectin/glycosylation phenotype SDR-dependent? — a synthesis of evidence LEGEND already holds

**Date:** 2026-09-21 · **Actor:** Scientist A · **Mode:** SYNTHESIS, READ-ONLY.
No canonical file edited, no `*_current.md` touched, no `BATCH_COMMIT`, no commit candidate,
no receipt written, nothing committed or pushed. **Nothing here is medical advice.**

**Assignment source:** [`wwox_activity_sensor_census_20260921.md`](wwox_activity_sensor_census_20260921.md) § 6,
which identified the lectin readout as the only single-cell-readable candidate and flagged the
domain-attribution risk as decisive and open.

**The question, restated exactly:**
> Does LEGEND's own held evidence predict that the lectin/glycosylation phenotype would be
> **SDR-dependent** — i.e. that an SDR-span missense allele would produce it — or does it not?

> 🔴 **No sensor is proposed. No programme is opened.** This file establishes the domain-dependence
> question and stops.

---

## 1 · VERDICT

### **`CANNOT-TELL`**

The single fact that decides it: **the only evidence LEGEND holds that would make the phenotype
SDR-dependent — the S281A/Y293F/K297A → perinuclear-localisation result — is *unpublished*.** It
exists nowhere as a readable experiment; it is a parenthetical inside a review, explicitly labelled
*"(Aldaz laboratory unpublished observations)"*, with no data shown. It is therefore **cited, not
first-hand**, and it is un-auditable at any depth. Against it, LEGEND holds **first-hand, at
`complete_fulltext_read`**, a *published* primary (`PMID 24550385`, receipt `FTR-20260810-24550385-02`)
in which a **WW1**-routed mechanism also changes WWOX's subcellular localisation — so LEGEND's own
evidence supplies a WW-dependent route to the same class of effect, and does not discriminate.

⚠️ **This verdict is about what LEGEND can *predict*, not about what is true.** The phenotype may
well be SDR-dependent. LEGEND has no evidence that can say so.

---

## 2 · THE PROVENANCE CHAIN for S281A / Y293F / K297A + localisation

| Step | What it is | Depth in LEGEND | Receipt |
|---|---|---|---|
| **LEGEND's statement** | `discovery_ledger_current.md` → **`DL-MECH-036`**: *"i residui catalitici S281A/Y293F/K297A sono necessari **sia** per l'attività enzimatica **sia** per la localizzazione perinucleare"* | non-canonical research ledger; **the ledger itself tags it `DATO (citato in review, primari da recuperare)`** | — |
| **Hop 1 — the document LEGEND read** | **`PMID 24932569`** · Aldaz CM, Ferguson BW, Abba MC (2014) *WWOX at the crossroads of cancer, metabolic syndrome related traits and CNS pathologies*, *BBA Rev Cancer* 1846(1):188–200 · PMC4151823 · [DOI](https://doi.org/10.1016/j.bbcan.2014.06.001) — **a REVIEW, not a primary** | 🟢 **read first-hand**, twice | `FTR-20260726-24932569-01` (`legacy_reconstruction`, `partial_fulltext_read`) and `FTR-20260920-24932569-01` (`partial_fulltext_read`, fresh read, fingerprint `0d7a6670…`) |
| **Hop 2 — the experiment** | *"(Aldaz laboratory unpublished observations)"* | 🔴 **DOES NOT EXIST AS A DOCUMENT.** No primary, no figure, no data shown, no methods, no n | ❌ none possible |

**Hops from LEGEND to the experiment: 2 — and hop 2 terminates in a non-document.**

**Is it first-hand?** The *review* is first-hand (read, receipted). The *result* is not, and cannot
be made so: there is nothing to retrieve. `sdr_missense_readout_assessment_20260920.md` § 0.3 already
classified it **"ACQUISITION-BLOCKED — named, not adjudicated. There is no source to read."**

Two further defects that bound how much weight it can carry, both already on LEGEND's books:

- **🔴 Receipt limitation, stated.** `FTR-20260920-24932569-01` carries `verbatim_locators: null` and
  names `files/fulltext/PMID24932569_PMC_MCPtext.txt`, which **is not present in this session's
  checkout** (`files/fulltext/` holds 14 files; none for 24932569). The Aldaz quote below could
  therefore be re-matched only against LEGEND's own analysis file, **not against the primary
  artefact**. This is a second-order match and is reported as such in § 6.
- **🔴 The transfer, with its distance named** (`sdr_missense_readout_assessment_20260920.md` § 5).
  **S281A / Y293F / K297A are designed catalytic-triad substitutions** — built to abolish catalysis
  *while preserving the fold*, at active-site residues. The reference genotype's allele is a
  **buried disease missense** (`CLAIM 030`: Q230 relSASA **0.000**, α-helix, pLDDT 98.5, 22 contacts
  < 5 Å, **8.2 Å from the catalytic triad**), whose protein is **not detected by Western blot**
  (`DIS-003`, Johannsen 2018 `PMID 29808465`). Reasoning from the first to the second is a transfer
  across **two** boundaries at once: **allele class** (designed-and-folded → natural-and-destabilising)
  and **mechanism** (catalysis-null → folding/abundance-defective). Neither boundary has been
  crossed experimentally by anyone. ⚠️ **A catalytic-site mutant is not a disease allele.**

**Consequence:** the SDR limb of the argument rests on an un-auditable observation, read out by
**localisation** rather than by activity, on an allele class that is not the disease class.

---

## 3 · WHAT THE PREPRINT DOES AND DOES NOT ATTRIBUTE

**Artefact:** `files/fulltext/PMID42523332_PMC_MCPtext.txt` · **50,075 bytes / 50,049 chars** ·
sha256 `7f2da97ba52357412af1e8f5e6b8c746e305b91197f4cad98ebe3af89f14bcbd` — **verified before analysis,
matches the brief. Not re-fetched.** `PMID 42523332` · PMCID `PMC13405132` ·
[DOI](https://doi.org/10.64898/2026.06.16.732723) · **`[PREPRINT]`** · held at
`FTR-20260921-42523332-01`, `partial_fulltext_read`.

⚠️ **WWOX is a minor limb of this paper.** It is a CATCHR (COG/GARP/EARP) proximity-proteomics study;
**WWOX appears 30 times in the body**, confined to one results paragraph, one discussion paragraph
and one figure legend. It is not a WWOX paper.

### 3.1 What it DOES report — verbatim

> *"To assess if WWOX serves any function in Golgi trafficking, we knocked it down using siRNA () used in previous studies."*

> *"WWOX KD caused N- and O-glycosylation defects as revealed by the increased plasma membrane binding of the lectins HPA (and) and GNL ()"*

> *"IF revealed that WWOX colocalizes with COG8 on Golgi membranes (Supplementary Figure 5A), specifically to the mid Golgi"*

**What was perturbed: the whole protein, by siRNA.** Not a domain construct, not an allele.
Causal language is available for exactly that: *depleting WWOX increases surface HPA/GNL binding.*
Nothing more.

### 3.2 What it does NOT attribute — verbatim, and the mood is preserved

> *"Although the molecular mechanism of WWOX remains unknown, its tandem WW domains could function as a scaffold to recruit PPxY-containing trafficking proteins to Golgi membranes, whereas its C-terminal short-chain dehydrogenase/reductase (SDR) domain may regulate Golgi physiology through local NAD(H)- or NADP(H)-dependent redox reactions."*

> *"Future studies should define how WWOX contributes to COG-dependent trafficking and Golgi homeostasis."*

🔴 **Read the mood.** *"remains unknown"* · *"could function"* · *"may regulate"* · *"Future studies
should define"*. The authors offer **one speculative mechanism per domain** and decline to choose.
**This is a stated gap, not a negative result.** The preprint does not say the phenotype is
WW-dependent; it does not say it is SDR-dependent; it says the mechanism is not known. The census's
reading — *"the authors explicitly leave WW-vs-SDR attribution open"* — is exactly right and is
confirmed here against the body.

### 3.3 What is absent — and the class of each zero

| Probe | Count in body | Token class | Admissible? |
|---|---|---|---|
| `rescue` — **of WWOX** | **0** (6 hits, all CATCHR-TurboID: COG/GARP/EARP KO rescue) | roman-class method word | ✅ **admissible zero** |
| `siRNA-resistant` | 0 | roman-class method word | ✅ admissible |
| `domain deletion` · `truncat` · `point mutation` · `catalytic` | 0 · 0 · 0 · 0 | roman-class method words | ✅ admissible |
| `Q230` · `S281` · `WW1` · `WW2` | 0 · 0 · 0 · 0 | HGVS / residue-identifier class | ✅ admissible |
| `PPxY` | 1 — in the speculative sentence only | roman-class | ✅ |

🔴 **There is no WWOX rescue experiment, no siRNA-resistant construct, no domain construct and no
allele anywhere in this preprint.** The domain question is not merely unanswered — **it was never
addressable by this design.** The paper cannot be re-read to extract an answer.

One further limitation the paper states about itself, which bears on any future use:

> *"Commercial anti-WWOX antibodies did not show any specific signal for IF prompting us to use a myc-WWOX for localization studies."*

⚠️ **The localisation claim rests on an overexpressed myc-tagged construct**, because no antibody
worked. This is the same method-class weakness that `chang_aldaz_contradiction_packet_20260920.md`
§ 2.1 identifies as structural on *both* sides of the inter-lab dispute. **Abundance ≠ function ≠
localisation:** this paper measures localisation (myc-WWOX IF) and a downstream function proxy
(lectin binding after KD); it measures neither WWOX abundance across alleles nor WWOX catalysis.

---

## 4 · THE ALDAZ / CHANG DISPUTE — how each position bears on the readout

LEGEND records the dispute in `DL-MECH-036`, verbatim:

> *"Aldaz colloca WWOX in sede **perinucleare/Golgi** … il lab Chang lo colloca in **mitocondri e nucleo** … La localizzazione è proprio ciò che il SDR determina → **la disputa tocca direttamente Q230P** e va tenuta aperta, non risolta per preferenza."*

**The lectin assay is a Golgi-function readout.** Its validity as a WWOX readout therefore depends
on where WWOX is. Both positions, stated without resolution:

| | **If Aldaz is right** (steady-state WWOX at perinuclear/Golgi) | **If Chang is right** (WWOX at mitochondria/nucleus, stress-translocating) |
|---|---|---|
| **Can the lectin readout work at all?** | ✅ **Coherent.** WWOX sits where the glycosylation machinery is; the preprint's medial-Golgi/COG8 colocalisation is the expected result; the KD phenotype is a direct loss-of-local-function | 🟠 **Indirect at best.** WWOX would act on the Golgi from elsewhere, or the phenotype would be a downstream/secondary consequence of losing a mitochondrial or nuclear function. The readout would still *move*, but it would no longer be a WWOX **activity** readout |
| **Does an SDR lesion predict the phenotype?** | 🟡 **Plausible but unestablished** — via the SDR→localisation route, whose only evidence is the unpublished S281A series (§ 2) | 🔴 **No route offered.** Chang's SDR mapping is a **mitochondrial targeting sequence** (`PMID 11058590`), not a Golgi one. An SDR lesion would predict a mitochondrial, not a glycosylation, defect |
| **What each side has actually measured** | GFP/myc fusions + confocal + deletion constructs; **one** endogenous IF (`PMID 15064722`, one cancer line) | Immuno-EM on endogenous protein in vivo (`PMID 15664696`) — the highest-resolution method in the dispute — but under **stress**, and it reported the Golgi **negative** |

🔴 **The dispute is NOT resolved here, and must not be.** `chang_aldaz_contradiction_packet_20260920.md`
row 1a records both foundational claims as **UNRESOLVED — both underdetermined**: both rest on
overexpressed tagged constructs, both predate the first `Wwox`-null animal, and neither has a
genotype-null antibody control. Row 4 supplies the reconciliation LEGEND prefers to hold open — a
constitutive cytoplasmic scaffold that is *additionally* phospho-activated and relocated under
stress — under which **both** compartment assignments can be partly right and the lectin readout
would report only the constitutive limb.

**The bearing, stated plainly:** the dispute does not decide SDR-vs-WW. It decides something
upstream — **whether the lectin readout is a WWOX-activity readout at all.** On Aldaz it is
coherent; on Chang it is an indirect downstream proxy. That question is open, and it is prior to the
domain question.

### 4.1 🆕 A third, independent lab that neither side cites — and that LEGEND has not read

**`PMID 33565365`** · Mahmud MAA *et al.* (2021) *Cellular Expression and Subcellular Localization of
Wwox Protein During Testicular Development and Spermatogenesis in Rats*, *J Histochem Cytochem*
69(4):257–270 · PMC8013998 · [DOI](https://doi.org/10.1369/0022155421991629). Nippon Veterinary and
Life Science University, Tokyo — **neither Aldaz nor Chang nor the preprint's lab.** From the PubMed
abstract (⚪ **abstract depth only — not read; this is an abstract, not a read**):

> *"These signals gradually condensed in germ cells with their differentiation and colocalized with giantin for cis-Golgi marker and partially with golgin-97 for trans-Golgi marker. Biochemically, Wwox was detected in isolated Golgi-enriched fractions. But Wwox was undetectable in the nucleus."*

🔵 **Why this matters and how much.** It is **endogenous protein, in normal non-transformed tissue,
in vivo, with a biochemical fractionation arm** — a method class neither disputant brought to the
compartment question, and independent of both. It supports the **Aldaz** steady-state compartment
assignment. **It does not resolve the dispute**: it is antibody-based without a genotype-null
control (the exact structural defect flagged in § 2.1 of the contradiction packet), it is testis
rather than neurons, and Chang's claim is about **stress-induced** translocation, which this does
not test. **Status in LEGEND:** present in `paper_registry_current.md` and `batch_queue.md` as
`screened`, and listed in `next_scientist_scout_20260921.md` as **"Genuinely unread"**. 🔴 The
activity-sensor census did not surface it. **It is the highest-value unread item bearing on this
question.**

---

## 5 · REPLICATION STATUS of the WWOX–glycosylation link

### 5.1 My queries, written out (PubMed, run 2026-09-21)

| # | Query | Result |
|---|---|---|
| Q1 | `WWOX AND (glycosylation OR glycan OR lectin)` | **10 hits.** Only `42523332` (the preprint) is on topic. Screened all 9 others: **0 relevant** — see § 5.2 |
| Q2 | `(WWOX OR "WW domain-containing oxidoreductase") AND ("Tn antigen" OR "Helix pomatia" OR "Galanthus nivalis" OR "O-glycosylation" OR "N-glycosylation" OR glycomic)` | **`total_count: 0`** — the reagent- and assay-specific query returns **nothing at all**, including the preprint |
| Q3 | `WWOX AND (Golgi OR "vesicle tethering" OR "membrane trafficking" OR secretory)` | **11 hits** — all Aldaz-lineage, Chang-lineage, the preprint, Hussain 2018, one off-topic pharmacogenomics paper, and **`33565365`** (§ 4.1) |
| Q4 | `WWOX AND (SEC23IP OR TMF1 OR "COG complex" OR COG8 OR "conserved oligomeric Golgi")` | **`total_count: 2` — exactly `42523332` and `30619736`.** Nothing else in PubMed |
| Q5 | `WWOX AND (SDR OR "short chain dehydrogenase") AND (localization OR localisation OR perinuclear)` | **4 hits**: `24550385`, `15064722`, `14526170`, `11572989`. **No primary publishes the S281A series** |

**Zero-class ruling.** These are **PubMed index queries**, not the body extractor — the extractor's
italic-token elision does not apply. `"Tn antigen"`, `"Helix pomatia"`, `"Galanthus nivalis"`,
`"N-glycosylation"`, `"COG complex"` are **roman-class method/reagent terms**; `SEC23IP`, `TMF1`,
`COG8` are **gene-symbol class, queried against an index that resolves gene symbols explicitly**
(the returned `query_translation` shows each expanded as `[All Fields]`). **All zeros above are
admissible zeros.**

### 5.2 The Q1 false positives, screened and rejected

`41443103` (ferroptosis/p53) · `36621327` (autophagy/mTOR) · `31230746` (lncRNA TSLD8) · `30362252`
(UPD microdeletion) · `29164763` (TMEM207 — its keyword *"aerobic glycosylation"* is a typo for
*glycolysis*; the paper is about GLUT-1/HIF-1α) · `22226915` (TMEM207/PPxY invasion) · `40507943`,
`27845895`, `17143562` (hyaluronan — a **glycosaminoglycan**, a different molecular class from N-/O-
glycan processing, and all Chang-lineage). **None reports a WWOX glycosylation phenotype.**

### 5.3 🔴 **THE RULING: `CLAIM 026`'s trafficking edge is a COMPATIBLE PRIOR, not independent corroboration**

`CLAIM 026` (status `in observation`, source `PMID 30619736` = Hussain *et al.* 2018, *Front Oncol*,
`PAPER 032`) and `working_model_current.md` line 63 assert a **trafficking–metabolism interface**
from TAP-MS interactome data. **It is a compatible prior. It is not corroboration.** Four
independent reasons, each sufficient:

1. **🔴 It is not evidentially independent — the preprint cites it.** Verbatim from the preprint:
   > *"WWOX was previously shown to interact with the ER-Golgi trafficking factor SEC23IP and the Golgi CCT TMF1, both of which were also identified in our COG proximity proteome"*

   `SEC23IP` is a named top interactor in Hussain 2018 (`DL-MECH-018`). The later work **knew of and
   used** the earlier as supporting context. Corroboration requires that two lines be arrived at
   independently; these were not.
2. **It is the wrong evidential type.** Hussain 2018 is **TAP-MS proximity/binding** — an
   **association** census on a full-length SFB-tagged construct. The preprint's claim is a
   **functional** one (depletion → glycosylation defect). An association does not corroborate a
   function. ⚠️ **Association ≠ causality**, in the direction that matters here: the prior supplies
   no perturbation at all.
3. **Q4 shows there is no third line.** `WWOX AND (SEC23IP OR TMF1 OR COG…)` returns **exactly these
   two PMIDs in all of PubMed.** The "WWOX-at-the-Golgi-machinery" literature is two papers, one of
   which cites the other.
4. **Neither can bear on the domain question.** Hussain 2018 used **full-length** WWOX; the preprint
   used **whole-protein siRNA**. Neither carries a domain construct. Together they cannot
   discriminate WW from SDR *even in principle*.

**Therefore:** the lectin/glycosylation phenotype is **unreplicated — n = 1 paper, n = 1 lab, and
that paper is a `[PREPRINT]`.** `CLAIM 026` makes it *unsurprising*. It does not make it
*corroborated*. **Those are different things, and the distinction is this section's finding.**

### 5.4 The counter-route LEGEND holds first-hand — and it points at WW1

**`PMID 24550385`** · Abu-Odeh M … Aqeilan RI (2014) *Characterizing WW domain interactions of tumor
suppressor WWOX reveals its association with multiprotein networks*, *J Biol Chem* 289(13):8865–80 ·
PMC3979411 · [DOI](https://doi.org/10.1074/jbc.M113.506790). **LEGEND holds this at
`complete_fulltext_read`, receipt `FTR-20260810-24550385-02`** (`fulltext_dossiers/PMID26499798.md`).
From its PubMed abstract (⚪ the *localisation* consequence is quoted at **abstract depth**; LEGEND's
recorded first-hand extract from this paper concerns **stabilisation**, not localisation — the
distinction is stated rather than blurred):

> *"our analysis revealed that the first WW (WW1) domain of WWOX is the main functional interacting domain"* … *"We found that ITCH mediates Lys-63-linked polyubiquitination of WWOX, leading to its nuclear localization and increased cell death."*

🔴 **This is the counterweight, and it is the reason the verdict is `CANNOT-TELL` rather than a
lean.** `DL-MECH-036` — **the very same ledger entry** that carries the SDR→localisation statement —
also carries *"WWOX è anche substrato dell'E3 ligasi **ITCH**"*. LEGEND's own held evidence therefore
contains **both** a route in which the **SDR** governs localisation (cited, unpublished, catalytic-site
mutants) **and** a route in which a **WW1**-mediated interaction governs localisation (published,
primary, held first-hand at complete depth). **Subcellular localisation is not an SDR-exclusive
property in LEGEND's own record.** Any inference of the form *"the SDR determines localisation,
therefore an SDR lesion produces a Golgi-function phenotype"* is defeated at its first step.

---

## 6 · VERBATIM LOCATORS — with programmatic re-match counts

**Artefact A — `files/fulltext/PMID42523332_PMC_MCPtext.txt`**, 50,075 bytes / 50,049 chars,
sha256 `7f2da97b…f14bcbd` (re-computed this session; matches the brief). All matches exact, `str.count`:

| ID | Proposition it supports | Quote (head) | Re-match |
|---|---|---|---|
| `L1` | The phenotype, and what was perturbed | *"WWOX KD caused N- and O-glycosylation defects as revealed by the increased plasma membrane binding of the lectins HPA (and) and GNL ()"* | **1 ✅** |
| `L2` | **The non-attribution** — both domains, modal mood | *"Although the molecular mechanism of WWOX remains unknown, its tandem WW domains could function as a scaffold … whereas its C-terminal short-chain dehydrogenase/reductase (SDR) domain may regulate Golgi physiology …"* | **1 ✅** |
| `L3` | Whole protein knocked down, no construct | *"To assess if WWOX serves any function in Golgi trafficking, we knocked it down using siRNA () used in previous studies."* | **1 ✅** |
| `L4` | Medial-Golgi localisation | *"IF revealed that WWOX colocalizes with COG8 on Golgi membranes (Supplementary Figure 5A), specifically to the mid Golgi"* | **1 ✅** |
| `L5` | **Non-independence from `CLAIM 026`** | *"WWOX was previously shown to interact with the ER-Golgi trafficking factor SEC23IP and the Golgi CCT TMF1, both of which were also identified in our COG proximity proteome"* | **1 ✅** |
| `L6` | The gap is stated, not closed | *"Future studies should define how WWOX contributes to COG-dependent trafficking and Golgi homeostasis."* | **1 ✅** |
| `L7` | Localisation rests on an overexpressed tagged construct | *"Commercial anti-WWOX antibodies did not show any specific signal for IF prompting us to use a myc-WWOX for localization studies."* | **1 ✅** |

**7 / 7 locators re-matched exactly once against artefact A.**

**Artefact B — LEGEND's own files (second-order matches, declared).** 🔴 The primary artefact
`files/fulltext/PMID24932569_PMC_MCPtext.txt` named in `FTR-20260920-24932569-01` **is not present
in this checkout**, and that receipt carries `verbatim_locators: null`. These quotes were therefore
re-matched **against LEGEND's files, not against the source**. This is a weaker match and is not
represented as anything else.

| ID | Source file | Quote (head) | Re-match |
|---|---|---|---|
| `L8` | `analysis/sdr_missense_readout_assessment_20260920.md` § 5 (quoting `PMID 24932569`) | *"K297A) destroying WWOX's catalytic activity. Remarkably, we observed that the amino acids predicted …"* | **1 ✅** (second-order) |
| `L9` | `research/discovery_ledger_current.md` `DL-MECH-036` | *"i residui catalitici S281A/Y293F/K297A sono necessari **sia** per l'attività enzimatica **sia** per la localizzazione perinucleare"* | **1 ✅** |
| `L10` | `research/discovery_ledger_current.md` `DL-MECH-036` | *"Aldaz colloca WWOX in sede **perinucleare/Golgi**"* | **1 ✅** |
| `L11` | `research/discovery_ledger_current.md` `DL-MECH-036` | *"**Tag**: DATO (citato in review, primari da recuperare)"* | **1 ✅** — LEGEND's own self-classification of the entry as cited |

**Total: 11 / 11 locators re-matched, 7 first-order against the fingerprinted preprint, 4 second-order
against LEGEND files with the reason stated.**

🔴 **No figure image was inspected anywhere in this file.** The preprint's extraction strips figure
callouts (the bare `()` in `L1` and `L3`), so every panel behind the HPA/GNL result is unread.

---

## 7 · THE TEST — 🔴 **this is a PREDICTION, not an observation**

**Stated in those words:** *LEGEND's held evidence does not predict that the lectin phenotype is
SDR-dependent. The proposition "an SDR-span missense allele produces increased surface HPA/GNL
binding" is a **hypothesis with a named test**, not a finding.* Nothing in this file is an
observation about an SDR missense allele, because **no such experiment exists anywhere in the
literature surveyed.**

### 7.1 The single cheapest experiment that would confirm or kill it

**A siRNA-rescue domain/allele panel in the preprint's own system.** One experiment, one cell line,
reagents that already exist.

- **System:** RPE1 cells (the preprint's), WWOX siRNA (the preprint's own, KD efficiency already
  validated by RT-PCR in two biological repeats) + **siRNA-resistant** myc-WWOX constructs.
- **Panel (4 arms + 2 controls):** wild-type · **Q230P** (buried SDR missense, severe) · **G372R**
  (SDR missense, *mild* — `CLAIM 030`'s natural negative control) · **S281A** (catalytic triad —
  the only way to test Aldaz's unpublished claim at all) · **P47T** (WW1, PPxY binding abolished,
  **protein at normal levels** — `CLAIM 030`) · empty vector.
- **Readout:** HPA + GNL binding on **intact, unfixed cells by flow cytometry**. The preprint has
  already validated HPA as a rescuable readout in this system (the CATCHR-TurboID clones *"fully
  rescue the knockout phenotype"*), so the assay's rescue arm is established, not assumed.
- **🔴 The control without which the experiment is worthless:** **measure expressed protein per
  construct in the same samples.** `FM-014` and `CLAIM 030` are explicit — abundance measurements
  across this allelic series are not commensurable, and a destabilised allele that is simply
  degraded will score identically to one that is present and functionally dead. Add a 30 °C
  low-temperature arm and an MG132 arm for the buried missense, per
  `sdr_missense_readout_assessment_20260920.md` § 6(C).
- **What each outcome means.** **P47T is the discriminator.** If P47T (normal abundance, WW1-dead)
  **fails** to rescue → the phenotype is **WW-dependent**, and the readout is **useless for the
  reference genotype**. If P47T rescues while Q230P/G372R do not → **SDR-dependent** — *but only if
  the SDR constructs are demonstrated to be present as folded protein*; otherwise the result is the
  abundance confound, not a domain result.

### 7.2 ⚠️ The second, independent reason this readout may not serve the reference genotype — `INFERENZA`

Even if the domain question resolved **SDR-DEPENDENT**, the lectin readout would still likely fail
for the reference genotype's own allele. `DIS-003` records, as a load-bearing `PREMISE: DATO`,
*"normal transcript, **protein absent** in fibroblasts homozygous for Gln230"*. If there is no
protein, the allele scores positive on any loss-of-function readout **for the trivial reason that
it behaves as a null** — and the assay **cannot separate "SDR function lost" from "protein absent"**.
That is precisely the criterion-2 / criterion-4 failure `sdr_missense_readout_assessment_20260920.md`
§ 1 assigns to *every* localisation-class readout in the corpus. ⚠️ Qualified twice: `CLAIM 030`
itself flags `PREMISE: DETECTION_FLOOR` — *"non rilevata" non è "assente"* — and this inference is
`INFERENZA` drawn from two held claims, **not an observation.**

### 7.3 🔴 LEGEND has no wet-lab capacity

**§ 7.1 is a specification, not a plan.** It is written so that the question is decidable by someone
who can run it, and so that LEGEND does not mistake a design for a result. **No programme is opened
and no sensor is proposed.**

---

## 8 · NEGATIVE RESULTS — explicit

1. **No primary publication of the S281A / Y293F / K297A localisation result exists.** Q5 returns 4
   papers, none of which is it. It is `"(Aldaz laboratory unpublished observations)"` and nothing more.
   ✅ roman-class query, admissible.
2. **No WWOX rescue, no siRNA-resistant construct, no domain construct, no allele in `PMID 42523332`.**
   `rescue`-of-WWOX = 0, `siRNA-resistant` = 0, `domain deletion` = 0, `truncat` = 0,
   `point mutation` = 0, `catalytic` = 0 — ✅ **roman-class method words, admissible zeros.**
   `Q230` = 0, `S281` = 0, `WW1` = 0, `WW2` = 0 — ✅ **residue/HGVS class, admissible zeros.**
3. **Zero prior or independent WWOX–glycosylation literature.** Q2 `total_count: 0`; Q1's 9 non-preprint
   hits all screened and rejected (§ 5.2). The census's finding of 0 is **independently reproduced
   with different query strings.** ✅ admissible.
4. **No third line of WWOX–Golgi-machinery evidence.** Q4 `total_count: 2`, and one cites the other.
5. **No figure panel inspected**, in any source, anywhere in this file.
6. **The Aldaz primary artefact is not in this checkout**, and its receipt carries no verbatim
   locators — so 4 of 11 locators are second-order (§ 6).
7. **The question was not settled, and no additional full text was read.** Per the brief's condition
   *"if and only if a specific paper would settle the domain question"*: **no such paper exists.** The
   SDR limb's experiment was never published; the preprint's design cannot address it; Hussain 2018
   and the preprint both used full-length protein. **Reading one more paper would not have changed the
   verdict, so none was retrieved.** 🔴 `PMID 33565365` (§ 4.1) is the one genuinely high-value unread
   item — but it bears on **localisation**, not on **domain attribution**, and would not settle this.

---

## 9 · INFORMATION GAIN

| Axis | Gain | One line |
|---|---|---|
| **Mechanistic graph** | **YES** | The WWOX→Golgi→glycosylation edge is downgraded from "supported by `CLAIM 026`" to **"unreplicated, n=1 preprint, with a prior that cites it"**; and `DL-MECH-036` is shown to contain **two mutually undermining localisation routes** (SDR-cited-unpublished vs WW1-published-first-hand) that no one had set side by side. |
| **Therapeutic hypothesis** | **NO** | Nothing here proposes, ranks or alters an intervention. A readout is not a therapy. |
| **Experimental roadmap** | **YES** | § 7.1 specifies the single cheapest decisive experiment, identifies **P47T as the discriminator** (normal abundance + WW1-dead — the only allele that separates the hypotheses), and names the abundance control without which it is worthless. |
| **Genotype stratification** | **YES** | The reference genotype's SDR-span missense is shown to be **doubly un-served** by this readout: the domain question is unresolved (§ 1) **and** the protein-absent state would make a positive result uninterpretable (§ 7.2). Two independent failure modes, not one. |
| **Intervention ranking** | **NO** | No intervention is ranked, proposed or re-ordered. Out of scope by instruction. |
| **Uncertainty** | **YES** | Three uncertainties are **sharpened rather than resolved**: the S281A result is un-auditable in principle (no document exists); the Aldaz/Chang dispute is shown to be **prior to** the domain question, not parallel to it; and `PMID 33565365` is surfaced as independent third-lab localisation evidence that LEGEND holds **unread** and that the census missed. |

---

## 10 · DEFAULTS_TAKEN

1. **Verdict granularity.** `CANNOT-TELL` was chosen over `BOTH` because `BOTH` would assert that
   LEGEND's evidence positively predicts **two** contributions; it does not. It holds one
   un-auditable pointer toward SDR and one first-hand-held pointer toward WW1, which is
   non-discrimination, not dual attribution. **Default: when evidence fails to discriminate, say it
   fails, rather than claiming both limbs.**
2. **No additional full text retrieved.** The brief permits at most one, *if and only if* it would
   settle the domain question. I ruled that none would (§ 8.7) and read none. **Default: do not spend
   a read that cannot change the verdict.** `PMID 33565365` is flagged for another actor instead.
3. **Abstract-depth material is used and labelled as such** for `PMID 33565365`, `PMID 24550385`'s
   localisation clause, and the Q1/Q5 screening. **An abstract is not a read**
   (`gold_is_in_the_details.md`), and every such use is marked ⚪.
4. **Second-order locators are reported rather than suppressed** (§ 6, artefact B). The alternative —
   presenting `L8`–`L11` as matches against the Aldaz primary — would have been false.
5. **The Aldaz/Chang dispute left open**, per `DL-MECH-036`'s own instruction *"va tenuta aperta, non
   risolta per preferenza"* — including where § 4.1's new third-party datum leans toward one side.
   **A new data point is not a resolution.**
6. **`PMID 42523332` not re-fetched.** sha256 verified against the brief before analysis
   (`7f2da97b…f14bcbd`, 50,075 B / 50,049 chars) and matched.
7. **Read-only respected throughout.** This file is the only artefact created. No canonical file, no
   registry, no ledger and no receipt was written; `PMID 33565365` was **not** ingested, and the
   registry gap it represents is reported, not repaired.

---

*Non-canonical analysis file. Produces no claim, no commit candidate and no canonical change.
Not medical advice.*
