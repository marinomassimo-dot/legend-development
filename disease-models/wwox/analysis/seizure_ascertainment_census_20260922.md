# Seizure-ascertainment census across the Wwox rodent literature

**Node:** `SEIZURE_ASCERTAINMENT_CENSUS` · **Actor:** Scientist D · **Date:** 2026-09-22
**Status:** non-canonical analysis file. **READ-ONLY toward every canonical file** — no registry, no
ledger, no state manifest, no receipt touched. **Public edition. Not medical advice.**

---

## 0 · The question, and why it is not the question the brief opened with

The brief opened on a contradiction: `PMID 24369382` (Mallaret 2014, *Brain*, co-authored by the
maker of the knockout mouse) asserts in its abstract that *"the short-lived Wwox knock-out mouse
display spontaneous and audiogenic seizures"*, while `PMID 19500159` (Suzuki 2009) says three times
plus an empty Table 2 row that Wwox-null mice show no epilepsy.

**That contradiction is not the live one.** Mallaret's body is paywalled and unreadable here, but it
is no longer the only mouse evidence: **four first-hand mouse datasets** now exist, three of them
already read to locator depth in this repository. The census below re-frames the question the way
the brief asked for — *what was actually done to each animal* — and the answer separates cleanly
into three findings, one of which is a large, well-evidenced negative.

🔴 **Standing repository conflict, restated not rediscovered.** `CLAIM 037`'s title still says the
seizure phenotype is *"explicitly absent in Wwox-null mice"* and `CLAIM 005` still carries the
prohibition *"No canonical statement may describe a Wwox-null mouse as showing epileptogenesis."*
[`CC-20260826-SEIZURE-RECONCILIATION-01`](../research/commit_candidates/CC-20260826-SEIZURE-RECONCILIATION-01.md)
established on **2026-08-26** that the headline is false against four datasets and proposed a
retarget of the prohibition. **It is still queued and unapplied, 27 days later.** Nothing in this
census changes that verdict; this census supplies the ascertainment layer underneath it.

---

## 1 · The census table

One row per paper × model. Every cell records **what the paper did**, not what it concluded.
`not performed` = the paper's own Methods enumerate its assays and this is not among them.
`not reported` = the paper does not say either way.
Depth label: **`full-text`** = body read (this session or, where marked `repo`, held here at
locator depth) · **`abstract-depth`** = abstract only, body not retrievable.

### 1a · Mouse — global/systemic nulls

| paper (PMID) | model & allele | **EEG?** | **provocation performed?** | **passive observation, how long** | **age window; did animals survive past it** | **n, sex** | what the paper concluded about seizures | depth |
|---|---|---|---|---|---|---|---|---|
| **17360458** Aqeilan 2007 *PNAS* | `Wwox−/−`, targeted (exons 2–4), Croce/Aqeilan line | **no** — not performed | **none** | none declared — oncological necropsy series | necropsy to ~3 wk; all die ≤3–4 wk | 13 nulls (osteosarcoma series); sex not stated | **silent on seizures** | `full-text` (repo dossier) |
| **18487609** Aqeilan 2008 *JBC* | same `Wwox−/−` | **no** — not performed | **none** | unscored husbandry | die 2–3 wk | not stated for behaviour | *"they did not exhibit any abnormal behavior or impaired motor skills"* — a **behavioural** negative, no protocol, no EEG | `full-text` (repo) |
| **19936220** Ludes-Meyers 2009 *PLoS ONE* | `Wwox^ΔCre/ΔCre`, EIIA-Cre germline null from the floxed exon-1 allele | **no** — not performed | **none** | **none** — the only brain measurement in the paper is *brain weight* | 43% dead by 72 h, 77% by d17, none past weaning; χ² at d3 | n=35 survival; n=3/3/3 organ weights; sex not stated | **nothing** — the words *seizure* and *epilepsy* occur once each, in one Discussion sentence citing the **rat** | `full-text` (repo, `FTR-20260806-19936220-01`) |
| **32000863** Cheng 2020 *Acta Neuropathol Commun* | `Wwox−/−`, NCKU/Hsu lines **WD1** (exon 1) and **WD234** (exons 2/3/4) | 🔴 **no in vivo EEG.** The only electrophysiology is **transcranial motor-evoked potentials** under chloral hydrate — a motor-conduction assay, not seizure ascertainment. Methods enumerate every assay; EEG is **not performed** | **YES — chemoconvulsant only:** pilocarpine 50 mg/kg i.p. (+ methylscopolamine 1 mg/kg), PTZ 30 mg/kg i.p.; Racine 0–6 scored over 60 min; ethosuximide 150 mg/kg and LiCl 60 mg/kg pre-treatment arms. **No audiogenic protocol** | **opportunistic husbandry only.** *"spontaneous epileptic seizures were commonly observed after postnatal day 12. Seizures were frequently induced by mild stressors including noise, strobe lights and novel cage during routine handling"* + one video (Movie S1). No duration, no scoring, no blinding, no denominator | seizures from **P12**; *"survived for less than a month"*; motor tests P18–20; Tc-MEP at 3 wk. **The observation window is inside the lifespan** | Tc-MEP n=4 KO / 10 WT / 5 HET. 🔴 **n for the seizure experiments is not in the running text**; figure-legend n is not extractable here and is treated as **suspect**. **Sex is never stated for any experiment in this paper** | spontaneous epilepsy + enhanced pilocarpine/PTZ susceptibility; 50% of injected KO reached status epilepticus, SE absent in `+/+` and `+/−` | `full-text` (**read this session**, PMC6990504, CC BY 4.0) |
| **34747138** Repudi 2021 *EMBO Mol Med* (gene therapy) | `Wwox−/−` (Aqeilan allele, FVB) ± AAV9-hSynI-WWOX | **no** — electrophysiology is **blind cell-attached patch** *in vivo* under ketamine/medetomidine, 4-min per cell, neocortex. Firing rate, not electrography | **none** | *"Each injected mouse was carefully monitored for growth, mobility, seizures, ataxia and general condition"* — unscored, no protocol, no duration, no frequency | P0 injection → P17–P21 analysis; KO dies <4 wk (*"we could not perform recordings in adult KO mice"*); rescued live 6–11 mo | survival: KO n=8 non-injected, n=6 GFP; ephys n=3 mice/group (30–45 neurons). **Sex reported only for the rescued behavioural cohorts**, not for KO seizure observation | KO firing ~6× WT; rescue returns to `ns` vs WT; *"we did not observe any spontaneous seizures in rescued mice"* — an **unscored negative** | `full-text` (**read this session**, PMC8649866, CC BY 4.0) |
| **42422765** Obeid 2026 *Mol Ther Adv* | `Wwox`-null (severe-null mouse model) ± AAV9-hSynI-WWOX dose series | 🟢 **YES — the only in vivo electrography ever performed on a Wwox-null mouse.** Single-channel **epidural ECoG**, transmitter implanted **P14** under isoflurane (not continuous anaesthesia), **continuous wireless 24/7 for 7 days**, reference contralateral; screened for interictal spikes and SWDs; blinded *"when feasible"*; subset cross-validated against time-synchronised video | **none** | the ECoG itself is the observation: 7 days | **P14 → ~P21.** ⚠️ Recording begins at P14, so **onset below P14 is unbounded**; recording started *"immediately after surgery … without a recovery interval"* | **n = 5 per group** (Fig. 7 caption). Sex not stated | SWD/h: `****` WT-vs-KO, `****` KO-vs-HD, `ns` WT-vs-HD. ⚠️ Interictal-spike panel prints **`p = 0.2000`** — the Mann-Whitney floor at those group sizes — while the text calls it *"a significant elevation"* | `full-text` (repo partial read, 2026-08-10; body **not retrievable now**: `is_open_access: false`) |

### 1b · Mouse — conditional / cell-type-restricted

| paper (PMID) | model & allele | **EEG?** | **provocation?** | **passive observation** | **age window; survival** | **n, sex** | conclusion about seizures | depth |
|---|---|---|---|---|---|---|---|---|
| **33914858** Repudi 2021 *Brain* | `Wwox^fl/fl;Syn1-Cre` (S-KO) and `Nes-Cre` (N-KO); GFAP-Cre and Olig2-Cre as negatives | **not reported** at retrievable depth — 🔴 **body not retrievable: no PMCID at all, `is_open_access: false`** | **not reported** | **not reported** | premature death **3–4 weeks**; behavioural seizure onset reported downstream as P9 | not retrievable | abstract: *"brain hyperexcitability, intractable epilepsy, ataxia and postnatal lethality"* | **`abstract-depth`** 🔴 |
| **34634460** Breton 2021 *Neurobiol Dis* | `Wwox^fl/fl;Syn1-Cre` (S-KO), S-HT, S-WT littermates | 🔴 **NO in vivo EEG. In vitro only** — local field potential in **acute 400–500 µm neocortical and hippocampal slices**, plus whole-cell patch. The title says so: *"an **in vitro** Wwox knockout mouse model"* | **electrical stimulation in the slice** (bipolar concentric tungsten, 0.1 ms pulses q30 s). **No in vivo provocation** | **none** — animals are sacrificed for slicing | **P13–P17**, single window. Survival not at issue; no longitudinal observation exists | bursting incidence **0/11 slices from 7 S-WT · 4/23 from 14 S-HT · 36/42 from 24 S-KO**. **Both male and female** | spontaneous neocortical (not hippocampal) bursting, NMDAR- and gap-junction-dependent; reduced sIPSC frequency and amplitude | `full-text` (**re-read this session**, PMC8609180; repo holds `FTR-20260810-34634460-02`, 18 locators) |

🔵 **Breton 2021 also supplies an independent, contemporaneous statement of the census's own
negative.** Its Introduction surveys the field and attributes rodent EEG **only to the rat**:
*"rats possessing a homozygous frame-shift mutation in [Wwox] show ~10 Hz interictal spiking
activity … sound-evoked fast waves during wild-running, and 5–6 Hz spike and wave complexes …
Furthermore, spontaneous seizures after postnatal day 12 are also seen in a mouse [Wwox] knockout
model."* Spontaneous **seizures** in the mouse; **EEG** only in the rat. That is a 2021 electro-
physiology laboratory, working on this exact model, reading the field the way this census does.

### 1c · Mouse — non-null alleles and heterozygotes

| paper (PMID) | model & allele | **EEG?** | **provocation?** | **passive observation** | **age window; survival** | **n, sex** | conclusion | depth |
|---|---|---|---|---|---|---|---|---|
| **17823927** Ludes-Meyers 2007 *Genes Chromosomes Cancer* | 🔴 **`Wwox^gt/gt` gene-trap HYPOMORPH** — no detectable Wwox protein in most tissues, low level in a minority | **no** — not performed | **none** | **none declared** — tumour-watch cohort, oncological endpoints only | **viable into adulthood**; *"significantly shorter lifespan"*; Suzuki 2009 Table 2 records viability as **2 years** | not stated for any neurological endpoint | 🔴 **silent on seizures, behaviour and brain entirely.** Endpoints are B-cell lymphoma, testicular atrophy, fertility | `abstract-depth` (body not retrievable: `is_open_access: false`) |
| **21499303** Abdeen 2011 *Oncogene* | `Wwox^C3H +/−` heterozygote, C3H background | **no** | **none** | none | adult tumour watch | female cohort for mammary endpoint | mammary carcinoma 50% vs 7%; **no neurological endpoint** | `abstract-depth` |
| **36828035** Hussain 2023 *Prog Neurobiol* | 🔴 **`Wwox^P47T/P47T` knock-in — NOT a null.** SCAR12 missense, WW1 domain | 🟢 **YES — simultaneous video-EEG.** Silver-wire electrodes implanted **bilaterally, subdural, frontal + parietal (4 channels)** under isoflurane; **14-day recovery before recording**; 24-hour sessions, freely moving; EEGs reviewed by **two trained observers** | **none** | video-EEG sessions totalling **21–53 h** per animal | **adult, >6 weeks**, in an animal that lives **beyond 1 year**. 🔴 So the sampled window is ~2 days out of a >365-day lifespan, and **no juvenile recording exists** | **n = 3 mutant vs 3 WT**, *"of either sex"*; histology cohorts n=7/19/21 with sex stated | interictal spikes **0–3098/h** (mutant) vs **0–68/h** (WT); **11–22 seizures per 43–53 h**; all three mutants >4 seizures/24 h; WT no seizures. Semiology: *"occasionally beginning with **wild running and jumping**"*, then tonic-clonic | `full-text` (**read this session**, PMC10835625) |

⭐ **Methodologically this is the strongest seizure dataset in the entire WWOX corpus** — bilateral
multi-channel, recovered animals, simultaneous video, electro-behavioural concordance scored on the
same events, both sexes. **And it is not a null.** It cannot falsify a statement restricted to
nulls; it does demolish the framing that seizures are a rat phenomenon.

🔵 **A detail worth carrying:** the P47T mouse's seizures begin *"with wild running and jumping"* —
**the same semiology as the rat `lde/lde` audiogenic seizure** (wild running → tonic-clonic). Two
species, two allele classes, one semiology, and **in neither mouse has anyone applied the acoustic
stimulus that produces it in the rat.**

### 1d · Rat

| paper (PMID) | model & allele | **EEG?** | **provocation?** | **passive observation** | **age window; survival** | **n, sex** | conclusion | depth |
|---|---|---|---|---|---|---|---|---|
| **17803050** Suzuki 2007 | `lde/lde`, 13-bp exon-9 deletion — **structurally a C-terminal frameshift, functionally a protein-level null**; **not** a mouse null and **not** a human WWOX-DEE allele | not reported at this depth | not reported at this depth | gait/seizure observation at 21 d | 3–12 wk | 19♀+20♂ mutants vs 14♀+12♂ normals (gait) | ataxic gait **95% vs 0%**; plasma BUN/creatinine/phosphate raised | `full-text` (repo, `FTR-20260806-17803050-01`); **no DOI, no PMCID, not retrievable here** |
| **19500159** Suzuki 2009 *Genes Brain Behav* | `lde/lde` | 🟢 **YES** — interictal spikes ~10 Hz in **all** unstimulated mutants, bilaterally synchronised, occipital > frontal, absent in normals; 5–6 Hz spike-and-slow-wave before clonic convulsion | 🟢 **YES — audiogenic, three trials.** Latency shortens **56±24 → 36±4 → 25±3 s** across days (kindling-like) | spontaneous-seizure observation in backcross and inbred cohorts | seizures from **day 16**; viability **3–12 wk** | audiogenic **19/20 (95%)**, denominator net of 3 deaths, ⚠️ **female-only, stated only in the Fig. 6 caption**; spontaneous 30/50 (60%) backcross; inbred 33.8% ♂ / 33.9% ♀; controls **0/14**. EEG cohort **n=5 mutant (2M/3F), 3 normal (2M/1F)** | rat `lde/lde` has audiogenic + spontaneous epilepsy with electrographic substrate; **states three times, and in an empty Table 2 `Epilepsy` row, that Wwox-KO mice have none reported** | `full-text` (repo, `FTR-20260806-19500159-01`) |
| **32581702** Iacomino 2020 *Front Neurosci* | `lde/lde` rat (Suzuki colony) + human fetal neuropathology + hNPC transcriptomics (Łódź) | **no** | **none** | **none** | 🔴 **P1 only.** BrdU at E16.5, pups perfused and dissected at **P1** | **n = 3 per genotype**, **both sexes** | 🔴 **no seizure statement about the rat at all** — the paper's endpoints are cortical layering (Satb2/Tbr1/BrdU) and cerebellar foliation | `full-text` (**read this session**, PMC7300205) |

### 1e · Explicitly excluded from the rodent census

| PMID | Why excluded |
|---|---|
| **42397075** Steinberg 2026 *Brain* | 🔴 **Human iPSC-derived brain organoids — no rodent.** Its identity (*Brain*, 2026, Aqeilan senior) makes it a live mis-filing risk for a rodent-model census. It contains no animal, no EEG and no seizure ascertainment |
| **30370248** Tanna & Aqeilan 2018 · **42128308** Obeid 2026 review · **34831305** Steinberg & Aqeilan 2021 · **25537520** · **25416187** | Narrative reviews — secondary synthesis, no cohort. `30370248`'s Figure 1 collapses mouse and rat into one **"Rodents"** box printing *"Seizures, epilepsy, & ataxia"*, which is exactly the compression this census exists to undo |
| **24369382** Mallaret 2014 *Brain* | Primary, and its abstract asserts the mouse result in the first person — but **the body is paywalled** (`is_open_access: false`; `PMC3914474` exists as a deposit and returns 0 bytes). **No method, no n, no strain, no scoring criteria, no controls are recoverable.** It therefore contributes an **assertion**, not an ascertainment row |

---

## 2 · The three answers

### Q1 — Has any Wwox-null mouse ever been given an EEG?

> **Yes — once, in 2026, and not before. One paper, one channel, one week, n = 5.**

**`PMID 42422765` (Obeid 2026)** is the **first and only** in vivo electrographic recording ever made
from a `Wwox`-null mouse: single-channel epidural ECoG, transmitter implanted at P14, continuous for
7 days, n = 5/group. **Before June 2026 the answer was flatly no.**

What that recording does **not** cover, and must not be read as covering:
- **No video-EEG has ever been performed on a Wwox-null mouse.** The only WWOX video-EEG is the
  **`P47T` knock-in**, which is not a null.
- **Single channel cannot distinguish a generalised discharge from a focal artefact** — bilateral
  synchrony is unmeasurable in that montage. The rat's 1979-vintage recording was bilateral.
- **Onset below P14 is unbounded.** Recording begins at implantation. Cheng 2020 observes behavioural
  seizures from P12 and the `Syn1-Cre` conditional is reported to seize from P9 — both **before** the
  only electrographic window opens.
- **No null animal outside P14–P21 has ever been recorded**, in any montage.
- **`Wwox^gt/gt`, `Wwox^+/−`, `Nes-Cre`, `Syn1-Cre` and the Aldaz/EIIA null have never been recorded
  in vivo at all.** For the `Syn1-Cre` the only electrography is **ex vivo slice LFP** (Breton 2021).

**Queries and counts, run 2026-09-22 (PubMed), with controls:**

| query | count | what it contained |
|---|---|---|
| `Wwox` | **708** | the field |
| `Wwox AND (EEG OR electroencephalography OR electrocorticography OR electrocorticogram)` | **12** | 🔴 **11 are human patient studies; exactly 1 is rodent — `19500159`, the rat** |
| `Wwox AND ("spike-wave" OR telemetry OR "video-EEG" OR "sound-induced" OR "acoustic startle" OR startle)` | **0** | — |
| **control** `Scn1a AND ("video-EEG" OR telemetry OR "spike-wave")` | **31** | ✅ the token set finds rodent electrography when it exists |

🔴 **And here is the proof that these counts are a floor and not the finding.** `PMID 36828035`
performed **bilateral video-EEG** on mice and **does not appear in either Wwox query** — its abstract
never uses the string. `PMID 42422765` performed continuous ECoG and does not appear either.
**PubMed `[All Fields]` reads title/abstract/MeSH, not Methods.** Every "nobody did X" in this census
therefore rests on **methods-level reads of each paper**, listed in the depth column of §1 — the query
counts are corroboration, never the evidence. This is a worked instance of the rule that a zero from a
search is not evidence of absence: here the query returns zero **and the fact is present**, twice.

### Q2 — Has any Wwox-null mouse ever been audiogenically provoked?

> 🔴 **No. Nobody has ever applied an acoustic stimulus to a Wwox-null mouse under a scored protocol.
> The mouse/rat discordance on audiogenic seizure is UNTESTED, not observed.**
> **`PREMISE: NOBODY_LOOKED`.**

The complete provocation inventory of the Wwox rodent literature:

| provocation | species | where | status |
|---|---|---|---|
| **audiogenic, 3 trials, scored, latency measured** | **rat `lde/lde`** | `19500159` | performed — **19/20 (95%)**, female-only |
| pilocarpine 50 mg/kg; PTZ 30 mg/kg; Racine-scored 60 min | **mouse null** (NCKU) | `32000863` | performed — the **only** provocation ever applied to a mouse |
| ethosuximide, LiCl pre-treatment arms | mouse null | `32000863` | performed (anticonvulsant arms) |
| **audiogenic / acoustic startle / sound-evoked, in any mouse** | — | — | 🔴 **never performed, in any Wwox mouse, of any allele, by any laboratory** |
| kindling, kainate, flurothyl, hyperthermia, any other provocation | — | — | 🔴 **never performed, in any Wwox rodent** |

**Queries, with controls:**

| query | count | contents |
|---|---|---|
| `Wwox AND audiogenic` | **2** | `19500159` (the rat protocol) and `24369382` (Mallaret — **assertion in an abstract, body paywalled**) |
| `Wwox AND (pentylenetetrazol OR PTZ OR pilocarpine OR kindling OR kainate OR kainic)` | **1** | `32000863` only |
| `Wwox AND (startle OR "sound-induced" OR "acoustic startle")` | **0** | — |
| **control** `Fmr1 AND audiogenic` | **62** | ✅ the term retrieves mouse audiogenic work in abundance when it exists |

🔴 **The two facts that make this a first-order finding rather than a bookkeeping gap:**

1. **Cheng 2020 saw it happen and never measured it.** Verbatim: *"Seizures were frequently induced
   by mild stressors including **noise**, strobe lights and novel cage during routine handling."*
   That is a **reflex/sensory-evoked seizure susceptibility in a Wwox-null mouse, observed
   incidentally during husbandry, with no stimulus specification, no intensity, no latency, no
   denominator, no controls and no blinding.** The one laboratory that noticed the phenomenon in a
   mouse converted it into a **chemoconvulsant** protocol instead. The audiogenic protocol that
   yields 95% in the rat has been in print since 2009 and was never run on the mouse.
2. **The one claim that someone did look is unreadable.** Mallaret 2014 asserts *"spontaneous and
   audiogenic seizures"* in the knockout mouse in the first person, and its body cannot be obtained
   here (`get_copyright_status` → `is_open_access: false`; `PMC3914474` returns an empty body).
   **So the sole assertion of a mouse audiogenic result carries no method, no n, no strain, no
   scoring criteria and no controls that anyone in this repository can inspect.**

⇒ The correct statement is not *"the mouse lacks the audiogenic phenotype"* and not *"the mouse has
it"*. It is: **the stimulus was never applied under a protocol, so the phenotype has never been
either demonstrated or excluded in any mouse.**

**The decisive experiment is small, cheap and 17 years overdue:** Suzuki's audiogenic protocol
(three trials, latency scored) applied to `Wwox−/−` at P12–P18 and to `Wwox^gt/gt` in adulthood,
both sexes, against littermate controls. It requires a sound chamber and existing colonies.

### Q3 — Does the observation window ever outlast the animal?

> **In the early oncology-era papers the window did not exist at all, so the question is moot and
> the negative is empty. In the modern papers the window sits inside the lifespan. And in the one
> Wwox-deficient mouse that lives for years, nobody has ever opened a window.**

| study | observation window for seizures | that study's own survival | verdict |
|---|---|---|---|
| `17360458` Aqeilan 2007 | **none** | all dead ≤3–4 wk | 🔴 **no window.** The negative is the absence of a measurement, not a measurement of absence |
| `18487609` Aqeilan 2008 | unscored husbandry | 2–3 wk | 🔴 a **behavioural** negative with no protocol and no EEG |
| `19936220` Ludes-Meyers 2009 | **none** — the only brain measurement is organ weight | 43% dead by 72 h, 77% by d17, none past weaning | 🔴 **no window.** Not a seizure negative in any sense |
| `19500159` Suzuki 2009 (survey of the above, for mice) | **none of the surveyed papers recorded** | — | 🔴 The canonical negative is a **literature survey over papers that never looked**, and it predates the NCKU null (2020), the `Syn1-Cre` conditional (2021) and the ECoG (2026) entirely |
| `32000863` Cheng 2020 | husbandry observation from **P12** onward | KO survives **<1 month** | 🟢 **window inside the lifespan, and the phenotype appeared.** This is the direct falsifier of *"the mouse dies before it can seize"* for this allele and colony |
| `33914858`/`34747138` Repudi 2021 | unscored monitoring | death 3–4 wk; behavioural seizures reported from P9 | 🟢 window inside the lifespan |
| `42422765` Obeid 2026 | ECoG **P14 → P21** | KO dies ~P21–28 | 🟡 window covers roughly the **final week** only; below P14 unbounded |
| `36828035` Hussain 2023 (`P47T`) | **21–53 h of video-EEG**, adult >6 wk | animal lives **>1 year** | 🔴 **inverted failure**: the window under-samples the lifespan by more than two orders of magnitude, and there is **no juvenile recording at all** in an animal modelling a childhood-onset disorder |
| `17823927` Ludes-Meyers 2007 (`Wwox^gt/gt`) | **none, ever** | 🔴 **viable into adulthood; Suzuki 2009 Table 2 records viability as 2 years** | 🔴🔴 **the decisive untested case — see below** |

#### 🔴🔴 The `Wwox^gt/gt` hypomorph is the experiment the field has been arguing about, and it has been sitting unused since 2007

Suzuki 2009's explanation for the mouse/rat discordance — *"the KO mice may die before they
experience epileptic seizure"* — is testable only in a Wwox-deficient rodent that **does not** die
early. **Exactly one exists.** `Wwox^gt/gt` (`PMID 17823927`) has no detectable Wwox protein in most
tissues examined, is viable, and Suzuki's own Table 2 records its viability as **2 years** against
the null's 2–3 weeks.

**It has never been observed for seizures. Never EEG'd. Never provoked. Never given a single
neurological endpoint.** Its published endpoints are B-cell lymphoma, testicular atrophy and
fertility. Suzuki's Table 2 `Epilepsy` row is empty for `Wwox^gt/gt` **for the same reason it is
empty for the null — nobody looked** — and that emptiness has been read for seventeen years as
though it were a result.

⇒ **The survival-confound hypothesis has had a clean test bed since 2007 and nobody has used it.**
That, not Mallaret's unreadable abstract, is the largest `PREMISE: NOBODY_LOOKED` in this census.

#### Binding rule applied to every onset number recorded above

**`first observed abnormal` is NOT `onset`.** Every age below is an **observation floor** —
no earlier NORMAL measurement exists in the same animals in any of these papers:

| number | how it is usually cited | what it actually is |
|---|---|---|
| mouse, **P12** (Cheng 2020) | "seizure onset at P12" | **floor** — opportunistic husbandry observation; no systematic monitoring and no EEG before P12 |
| mouse, **P9** (`Syn1-Cre`, reported downstream) | "onset P9" | **floor** — body not retrievable here; method unverified |
| mouse, **P14** (Obeid 2026) | "electrographic onset P14" | **floor set by the implant date**, explicitly — the paper itself does not claim onset |
| mouse, **>6 weeks** (`P47T`) | "adult-onset seizures" | **floor** — no juvenile recording was performed |
| rat, **day 16** (Suzuki) | "seizure onset day 16" | **floor** — detection is observational and audiogenic testing begins at an age the paper sets |

---

## 3 · Secondary sweep — Adelaide and Łódź

🔵 **Prior art credited.** [`analysis/scientist_node_scouting_20260920.md`](scientist_node_scouting_20260920.md)
and [`analysis/next_scientist_scout_20260921.md`](next_scientist_scout_20260921.md) already enumerate
both nodes and their corpus counts. **My delta is the seizure-ascertainment axis only.**

### Adelaide — Richards R I / O'Keefe L V, University of Adelaide

**Identity, disambiguated:** Robert I. Richards and Louise V. O'Keefe, Department of Molecular and
Biomedical Science (formerly Discipline of Genetics / Centre for Molecular Pathology), The University
of Adelaide — affiliation verified on every record retrieved. Frequent co-authors Amanda Choo,
Cheng Shoou Lee, Sonia Dayan, Alexander Colella, all same department.

| PMID | year | what it is | organism | seizure/EEG content |
|---|---|---|---|---|
| 21075834 | 2010 | Drosophila Wwox orthologue, aerobic metabolism, ROS | **Drosophila** | none |
| 23765596 | 2013 | metabolic reprogramming and WWOX transcript levels | human cells (HEK293) | none |
| 25595186 | 2015 | review — FRA16D, metabolism, cancer | — | none |
| 26390919 | 2015 | WWOX moderates mitochondrial respiratory complex | **Drosophila** | none |
| 26302329 | 2015 | WWOX in elimination of tumorigenic cells | **Drosophila** | none |
| 34210081 | 2021 | review — molecular biology of WWOX/FRA16D | — | none |
| 10749140 · 10861292 · 15814586 · 16007179 · 16242840 | 2000–2005 | FRA16D/WWOX cloning-era genetics | human | none |

> **`(Richards RI[Author] OR "O'Keefe LV"[Author]) AND (Wwox OR FRA16D) AND (mice OR mouse OR rat OR
> seizure OR epilepsy OR neuron OR brain)` → 1 record**, and that record is the **review** 25595186,
> which matches only because it mentions that the *mouse* WWOX gene also spans a fragile site.

🔴 **The Adelaide group has never made, phenotyped or recorded from a WWOX rodent. Their in vivo
model organism is *Drosophila melanogaster*. Zero EEG, zero seizure provocation, zero behavioural
seizure scoring, in any organism.** Nothing they have published bears on this census except as a
metabolic-mechanism source. **Their absence from the seizure literature is not a gap in this census —
it is a correct description of their programme.**

### Łódź — Bednarek A K / Kośla K, Medical University of Łódź

**Identity, disambiguated:** Andrzej K. Bednarek and Katarzyna Kośla, **Department of Molecular
Carcinogenesis, Medical University of Łódź** — affiliation verified on every record. Co-authors
Elżbieta Płuciennik, Izabela Baryła, Żaneta Kałuzińska, Ewa Styczeń-Binkowska, Magdalena
Orzechowska, same department. ⚠️ `Bednarek AK` in this department is **not** to be merged with other
`Bednarek A*` authors in unrelated fields; every record below was affiliation-checked.

`(Bednarek AK[Author] OR "Kosla K"[Author]) AND WWOX` → **38 records**; narrowed by
`AND (mice OR mouse OR rat OR neuron OR neural OR brain OR seizure OR epilepsy)` → **8**:

| PMID | year | what it is | organism | bears on the census? |
|---|---|---|---|---|
| **32581702** Iacomino 2020 | 2020 | cortical layering in `lde/lde` rat + human fetal neuropathology + hNPC CAGE | **rat (Suzuki colony)** + human | 🟢 **YES — it is a census row (§1d).** And it is a **negative** one: rat pups dissected at **P1**, n=3/genotype, both sexes, **zero seizure ascertainment of any kind** |
| 31543760 Kośla 2019 | 2019 | WWOX silencing in human neural progenitor cells, CAGE transcriptomics | human hNPC | no in vivo readout, no seizure endpoint |
| 32389029 Kośla 2020 | 2020 | review — *The WWOX gene in brain development and pathology* | — | secondary; no new ascertainment |
| 34204789 · 30211123 · 36271927 · 35328751 · 20535528 | 2010–2022 | glioblastoma biomarkers, breast cancer, HIF1α/glycolysis, GBM specimens | human cells/specimens | none |

🔴 **The Łódź group owns no rodent colony. Their single rodent contact is Iacomino 2020, where the
`lde/lde` animals came from Suzuki's laboratory (Nippon Veterinary and Life Science University,
protocol #2019K-28) and the Łódź contribution was the hNPC transcriptomics. They have never
performed EEG, video-EEG, or any seizure provocation, in any species.**

🔵 **One cross-check this sweep does deliver.** Iacomino 2020 is the **only** independent laboratory
to have touched Suzuki's `lde/lde` rat — and it examined it at **P1**, an age at which the seizure
phenotype (floor: day 16) cannot be present. **So the rat seizure phenotype remains, in 2026,
single-laboratory and never independently replicated**, exactly as `CLAIM 037`'s evidence boundary
records. This sweep corroborates that caveat and adds nothing that softens it.

---

## 4 · What I could not verify

| item | why | consequence |
|---|---|---|
| **`PMID 24369382` (Mallaret 2014) mouse methods** | paywalled: `is_open_access: false`, *"© The Author (2013) … All rights reserved."*; `PMC3914474` is a deposit, not a body | 🔴 The **only** claim of an audiogenic mouse result has **no inspectable n, strain, protocol, scoring or controls**. Acquisition is a human action |
| **`PMID 33914858` (Repudi 2021 *Brain*) — the `Syn1-Cre`/`Nes-Cre` primary** | 🔴 **no PMCID at all**; `is_open_access: false` | The conditional models' seizure ascertainment enters this census at **abstract depth only**. The reported P9 behavioural onset is unverified here |
| **`PMID 17823927` (`Wwox^gt/gt`) body** | `is_open_access: false` | The hypomorph row is `abstract-depth`. ⚠️ **"Silent on seizures" is inferred from an abstract whose declared endpoints are oncological, not from a Methods list.** It is a strong inference; it is not a Methods-level negative, and it should be upgraded when the body is obtained |
| **`PMID 42422765` body, now** | `is_open_access: false`; retrievable only via the repository's 2026-08-10 partial read | ECoG parameters are quoted from repository locators, **not independently re-verified this session** |
| **`PMID 17803050` (Suzuki 2007)** | no DOI, no PMCID, not obtainable in this environment | Rat row rests on the repository's existing full-text read |
| **`n` for Cheng 2020's seizure experiments** | figure-legend numbers are not in the extracted running text; the known extractor defect deletes `n`/`p` labels from captions | 🔴 Recorded as **suspect / not extractable**. Do not quote an n for the pilocarpine or PTZ cohorts from this census |
| **Sex in Cheng 2020, Repudi 2021 (KO arm), Obeid 2026, Aqeilan 2007/2008, Ludes-Meyers 2009** | not stated in any retrievable surface | 🔴 **Sex is unreported for every mouse seizure measurement in the literature except Hussain 2023 (*"of either sex"*) and Breton 2021 (*"both male and female"*).** Against a rat headline figure that is **female-only**, this is a systematic blind spot |
| **`PMID 42422765` supplementary** | `files/` is gitignored and empty in this worktree | not inspected |

---

## 5 · Contradictions with what the repository currently asserts

| # | Repository text | This census | Class |
|---|---|---|---|
| **X-1** 🔴 | `CLAIM 037` title: the seizure phenotype *"is explicitly absent in Wwox-null mice"* | **False.** Four first-hand mouse datasets: behavioural seizures from P12 and Racine-scored chemoconvulsant susceptibility (`32000863`), 6× firing rate (`34747138`), neocortical bursting in the `Syn1-Cre` (`34634460`), ECoG SWD at `p<0.0001` (`42422765`) | **already established** by `CC-20260826-SEIZURE-RECONCILIATION-01`; **restated, not rediscovered** |
| **X-2** 🔴 | `CLAIM 005`: *"No canonical statement may describe a Wwox-null mouse as showing epileptogenesis"* | The guard is right and the scope is wrong — it bans **measured facts** rather than the **unmeasured process**. `CC-20260826` §Δ3 already drafts the retarget | **already established**; still queued |
| **X-3** 🔴 | `CLAIM 005`: *"Whether the mouse lacks the phenotype or dies before expressing it is open and testable: the earliest rat seizure onset (day 16) already exceeds the entire lifespan of the mouse null"* | **Two separate errors.** (a) It is not open for the *behavioural* phenotype — Cheng 2020 observes seizures from **P12**, inside the lifespan. (b) 🔴 **NEW:** the survival confound has had a clean test bed since **2007** — `Wwox^gt/gt`, viable to ~2 years, protein-negative in most tissues, **never observed, never recorded, never provoked**. The sentence treats as an open question something that is instead an **unattempted experiment on an existing animal** | (a) already established; **(b) NEW this census** |
| **X-4** 🔴 **NEW** | Repository prose repeatedly treats Suzuki 2009's Table 2 `Epilepsy` row as a **cross-model result** | The row is empty for `Wwox−/−` **and** for `Wwox^gt/gt`. For the hypomorph the emptiness is **provably** an ascertainment gap, since `17823927` reports no neurological endpoint of any kind. A table cell recording that nobody looked has been read as recording that nothing was there | **NEW** |
| **X-5** ⚠️ **NEW** | `CC-20260826` §"Missing decisive experiment" proposes continuous video-EEG P7–P21 across five null/conditional arms | **Correct and incomplete in two ways.** (a) It omits **audiogenic provocation**, which is the one stimulus that distinguishes the rat result and which **no mouse has ever received** (§Q2). (b) It omits **`Wwox^gt/gt`**, the only Wwox-deficient rodent that lives long enough to test the survival confound (§Q3) | **NEW** |
| **X-6** ℹ️ **NEW** | The brief's framing that the mouse-seizure question turns on `PMID 24369382` | Mallaret is the **weakest** evidence in the census — abstract-depth, single-source, unreadable methods. The question turns on **four** inspectable mouse datasets plus **two structural gaps** (no audiogenic protocol in any mouse; no ascertainment ever in the long-lived hypomorph) | **reframing** |
| **X-7** ℹ️ **NEW** | Mis-filing risk | **`PMID 42397075` (Steinberg 2026, *Brain*, Aqeilan senior) is human organoids, not a rodent model.** It carries no animal, no EEG and no seizure ascertainment and must not enter a rodent census | **NEW** |

---

## 6 · Declaration

Author: **Scientist D**. Date: **2026-09-22**. **READ-ONLY** toward every canonical file: nothing
under `registries/` was edited, no receipt recorded or appended, no state manifest touched, no
commit candidate produced, no git operation performed. This file is the only file written.

**Species and allele classes were kept separate throughout.** Rat `lde/lde` is a 13-bp exon-9
frameshift — structurally a C-terminal frameshift, functionally a protein-level null — and is **not**
a mouse null and **not** a human WWOX-DEE allele. `Wwox^P47T/P47T` is a SCAR12 missense knock-in and
is **not** a null. `Wwox^gt/gt` is a hypomorph with residual protein in a minority of tissues and is
**not** a null. No phenotype was transferred across any of these boundaries.

**Depth discipline.** Every row carries an explicit `full-text` / `abstract-depth` label. No
abstract-depth finding was promoted to a datum; `17823927`'s "silent on seizures" is flagged in §4 as
an inference from a declared-endpoint abstract rather than a Methods-level negative.

**Attribution discipline.** All identifiers were resolved with `get_article_metadata` /
`get_copyright_status` / `get_full_text_article` addressed **by identifier**. No content is attributed
by passage or cross-reference ID; Scholar Gateway was not used. No PMID or DOI was reconstructed from
memory. `get_copyright_status` was run as a one-call pre-test before every body attempt.

🔴 **Public-edition compliance.** No contact detail, email address or identifying information of any
living person appears in this file. Author names appear only as scientific attribution with
institutional affiliation, as published. No individual-level human clinical record is reproduced.

**Not medical advice.**

**Sources.** Article metadata, copyright status and full texts retrieved from **PubMed** and
**PubMed Central**. DOIs of every source read at full text this session:
[32000863](https://doi.org/10.1186/s40478-020-0883-3) ·
[34747138](https://doi.org/10.15252/emmm.202114599) ·
[34634460](https://doi.org/10.1016/j.nbd.2021.105529) ·
[36828035](https://doi.org/10.1016/j.pneurobio.2023.102425) ·
[32581702](https://doi.org/10.3389/fnins.2020.00644).
Sources cited at abstract depth or from repository records, with DOI verified this session:
[24369382](https://doi.org/10.1093/brain/awt338) ·
[33914858](https://doi.org/10.1093/brain/awab174) ·
[42422765](https://doi.org/10.1016/j.omta.2026.201791) ·
[42397075](https://doi.org/10.1093/brain/awag239) ·
[17823927](https://doi.org/10.1002/gcc.20497) ·
[18487609](https://doi.org/10.1074/jbc.M800855200) ·
[17360458](https://doi.org/10.1073/pnas.0609783104) ·
[21499303](https://doi.org/10.1038/onc.2011.115).
Cited from LEGEND's own prior full-text reads without re-verification this session:
`19500159`, `17803050`, `19936220`, `30370248`.
