# Rescue window: what is prevented, what is recovered, what is unmeasured (iteration 6, package P7)

Non-canonical research record. Actor `scientist-b`, task `ORCH-ROADMAP-IT6-20261029`, branch `task/it6-p7`, 2026-10-29.
It changes none of the four scientific current files, writes no ledger event, and is not medical advice. No dose,
schedule or administration for any person appears here. Class level only. Association is not modulation and
modulation is not rescue; "rescue" below always means the authors' word for a measured change in a stated endpoint of a
stated model.

**Question.** Across the WWOX rescue-type studies already read or readable, which damage is PREVENTED (intervention
before the endpoint's phenotype exists), which is RECOVERED (intervention after it had manifested), and which is
UNMEASURED?

**Reuse and new questions.** Receipts, manifests and dossiers were reused by event ID (`receipt_linkage.py` maps them;
all IDs below are RECORDED in the ledger). Passages were reopened only for these new questions, each with a staged
receipt (section 6):

- Q1 (Obeid 2026, Repudi 2021): at the day of injection, what is stated about the phenotype's onset, and what exactly is
  the comparator and follow-up of the P0-P5 arms? Supplement S8 was rendered from `mmc1.pdf` p.10 at 300 dpi and opened.
- Q2 (Steinberg 2021, Steinberg 2026): when was the add-back given relative to the first measured phenotype?
- Q3 (Breton 2021, Tsuruwaka 2015, Cheng 2020): what is the timing and persistence of each intervention or onset sentence?

Surface note (`paper_packet.py rank`, run with `--root /home/desktop/legend-development`): S8 sits on `mmc1.pdf` p.10
and is a raster-plus-vector page; the page was rendered, not extracted. Figure 7 of Obeid (the ECoG figure) is
LIKELY_VECTOR and was not re-rendered here (its 400 dpi page render is already receipted, entry 43).

Status vocabulary used in this file: **PREVENTED** (intervention precedes the phenotype), **RECOVERED** (intervention
follows a manifested phenotype), **EARLY-WINDOW** (intervention precedes the measured endpoint, but onset of that
endpoint was never located, so prevention versus very early recovery cannot be separated), **UNMEASURED**,
**UNVERIFIED** (I could not check it at the source).

---

## 1. The reading rule that decides everything

Every in-vivo genetic rescue in the corpus treats the Wwox-null mouse at P0 to P5 and measures endpoints at P10 or later.
Untreated nulls are dead by about P15 (Obeid S8A: KO+RI reaches 0 percent at about day 15, read on the rendered
page). So:

1. A treated animal is compared with an untreated animal at the age when the untreated one is already abnormal. That
   shows the intervention changed the trajectory. It does not show that damage present at injection was undone,
   because **no study measures the phenotype in the same animal, or in a same-age cohort, at the moment of injection**.
2. Later-than-P5 intervention was not done in mice. The authors say so in plain words (section 3). A perinatal result
   therefore cannot be carried to a later intervention.
3. Each result is an improvement of a named endpoint. None is global recovery: the residue
   (myelination, cerebellum, radial glia) is listed per study.

---

## 2. Per-study table

Columns as asked: intervention time; onset of the phenotype (source statement); endpoint; comparison group; follow-up;
persistence; limits of the window; class. Locators are verbatim; "(JATS)" = the article XML in `files/fulltext/`.
Quotes from extracted text lose italics, superscripts and genotype signs; panel readings are marked as readings.

### 2.1 Repudi 2021, *EMBO Mol Med* (PMID 34747138; receipts `FTR-20260810-34747138-01` complete, `FTR-20261019-34747138-01`; manifest entries 1-29)

| Field | Content |
|---|---|
| System, genotype | Wwox-null mouse (FVB, targeted-deletion line), whole-body null. AAV9-hSynI-mWwox or -hWWOX, neuron-directed |
| Intervention time | ICV at **P0**. Methods; Results: "Viral particles (2 x 10^10/hemisphere) ... were injected into the ICV region of Wwox-null mice at birth (P0)". Free-hand injection (manifest entry 4) |
| Onset of the phenotype | Statement in this paper: "Wwox-null and AAV9-hSynI-EGFP-injected mice were hypoglycemic from the second week until they succumbed" (Results, first section). Seizure onset is not stated here; from another paper (Cheng 2020, 2.7) "after postnatal day 12". Hypomyelination onset: not stated |
| Endpoints | survival; body weight; glucose (Appendix S1C/D only); hindlimb clasping (App. S3); cell-attached firing at P18-21 and in adults (Fig 3); GFAP/Iba1 (P19, 9 months); MBP, CC1/PDGFRa, EM g-ratio (P17, 6 months); open field, EPM, rotarod (8-10 weeks, 8-9 months) |
| Comparison group | AAV9-hSynI-EGFP-injected null and non-injected null for survival, firing, myelin at P17-P21; **for every behavioural endpoint the comparator is wild type only**: "Unfortunately, we could not assess behavior of Wwox-null mice due to their poor conditions and premature death" (Results, behaviour section). Adult firing: only WT versus treated, because "KO mice died within less than 4 weeks, we could not perform in vivo recordings in adult KO mice" |
| Follow-up | WWOX "detected in 9 months post-injection"; behaviour to 8-9 months; survival curves read from panels (manifest entry 28): treated arms reach 0 percent at about 350 and about 330 days, all dead or censored before 400 days, "no explanation of the late deaths is given" |
| Persistence | expression 9 months, EM improvement at 6 months with "some minor differences in the g-ratio and the number of unmyelinated axons" versus WT (Results, EM paragraph); residual differences "could be attributed to an oligodendrocyte-specific WWOX function" (Discussion) |
| Window limits | "The limited life span and poor conditions of Wwox-null mice prompted us to treat these mice very early on in their life (P0). Nevertheless, attempts to treat post-natal Wwox-null mice by different route of AAV administration should and will be explored in the future." (Discussion, penultimate paragraph) |
| Class | **EARLY-WINDOW, effectively PREVENTED** for seizures (none observed in treated animals, which were never recorded before onset), glycaemia, growth, survival; **myelin partly**, glia reduced, residual gap untested against WT. **Nothing RECOVERED** |

### 2.2 Obeid 2026, *Mol Ther Adv* (PMID 42422765; receipts `FTR-20260814-42422765-06` complete, `FTR-20261023-42422765-01`; manifest 48 entries)

| Field | Content |
|---|---|
| System | Wwox-null FVB mouse (targeted-deletion allele), AAV9-hSynI-hWWOX, WPRE-free: LD 1.23e11 vg, HD 2.63e11 vg "as printed" (convention undeclared) |
| Intervention time | Main cohorts "P0-P1" (Fig 4A caption). Timing experiment: "ICV injection ... at daily intervals from P0 to P5, with at least three littermates treated per time point" (Results, "Early postnatal WWOX gene therapy achieves durable therapeutic rescue"); the S8 legend states the arms as "P1-P5 (n=3-7)" and there is no P0 arm in S8 (manifest entry 11, registry correction of 2026-08-10) |
| Onset (source statements) | ECoG: "Continuous ECoG monitoring was performed ... beginning at approximately P14 after ICV administration at P0" (Results, epileptiform section). Glucose: untreated KO about 95 against WT about 130 at P10 (Fig 3E, panel reading, manifest entry 38). Deterioration timing: "Wwox-null mice rapidly deteriorate after P5, developing severe growth retardation, progressive weight loss, and frequent seizures" (Discussion; cites refs 42 and 69, not an own measurement). Hypomyelination: KO MBP at P18 (Fig 6A-E). No age-resolved onset is measured for any endpoint inside P0-P5 |
| Endpoints | survival (to P40 and P300), weight, glucose P10/P20/P30/P180, hindlimb-clasping at P18, behaviour at 3 months, vector genomes/mRNA/protein, MBP (qualitative), GFAP/Iba1, ECoG spikes and SWDs from about P14 for 7 days |
| Comparison | KO+RI and WT+RI. Fig 7E: WT, KO, KO+HD only: "there is no LD arm in this panel". Behaviour: WT versus HD only ("LD-treated mice did not survive to P90"). Fig 6F has no untreated-KO column. Fig S8C/D: the "ns" bracket spans WT to the treated bars, KO bar is separate (rendered page, panel reading: weight P14 about 8.6 WT, about 3.1 KO with ***, treated about 7.5-8.1; glucose about 160 WT, about 43 KO with **, treated about 157-160) |
| Follow-up | HD to P180 (weight/glucose), WWOX protein to P240 and P300; S8B: P1 arm 100 percent to about day 300, **P5 arm 75 percent from about day 35 to day 300** (n=7); no P2, P3, P4 on the 300-day plot; **no P4 survival curve at all** (manifest entry 11, re-read on the rendered page today: S8A legend lists P1, P2, P3, P5) |
| Persistence | "Treated mice exhibited a dramatic extension in survival, from approximately three weeks to nearly one year" (Results, same section). P300 expression is survivor-selected and regionally supraphysiological (S5 labels, entry 29) |
| Window limits | Verbatim, Results: "Therapeutic rescue beyond this early postnatal window was not explored, as Wwox-null mice rapidly deteriorate with progressive neurological dysfunction and early lethality, precluding effective intervention at later stages." Discussion: "the inability to assess later intervention likely reflects a combination of model-specific biological constraints and technical limitations, rather than a definitive boundary for therapeutic responsiveness" |
| Class | survival, growth, glucose, SWD rate at P14-21, motor score: **PREVENTED / EARLY-WINDOW**. P5 arm: **EARLY-WINDOW with an unmeasured pre-treatment state**. Astrogliosis at P5 injection: GFAP-positive cells WT about 5, KO about 44, treated about 5, ns versus WT (S8I, rendered today). **No RECOVERED endpoint** |
| What S8 does not show | S8 contains no group treated after any phenotype was measured in the injected animal; P5 histology panels E-I test only P5; P1-P3 have no histology; no age beyond P5 |

### 2.3 Steinberg 2021, *EMBO Mol Med* (PMID 34268881; receipts `FTR-20260814-34268881-03`, `FTR-20261025-34268881-11`)

| Field | Content |
|---|---|
| System | human cerebral organoids: engineered knockout hESC line; knock-in of WWOX cDNA at the AAVS1 safe-harbour locus ("W-AAV"; "AAV" here is the locus, not a virus); lentiviral WWOX in KO organoids; patient-derived lines with the same safe-harbour add-back |
| Intervention time | (a) **W-AAV: present in the stem-cell line before differentiation**. (b) **Lentivirus: "At day 35 of culture, individual COs were transferred to an Eppendorf tube containing CMM with 1:100 of virus-containing medium"** (Methods); the Figure 2 legend says "reintroduced into week 6 WWOX-KO COs". The two sources differ by about a week and are both kept |
| Onset | The hyperexcitability phenotype was first measured at **week 7**: "Mean spectral power of week 7 WT and KO COs in baseline conditions" (Fig EV legend). No earlier recording exists. Onset: UNMEASURED |
| Endpoints | 0.25-1 Hz spectral power at week 7 (lenti); VZ SOX2/neuron composition, GABAergic/glutamatergic balance at week 10, astrocytes weeks 15 and 24, DNA damage, apoptosis, layer markers weeks 15 and 24 (W-AAV) |
| Comparison | KO non-treated (NT) and WT organoids; W-AAV n=4 from one batch for most panels |
| Follow-up | lenti: one week after infection (week 7); W-AAV: to week 24 |
| Persistence | W-AAV astrocytosis "progressed through time, and was partially reversed in W-AAV COs"; layer markers "CTIP2+ cell and SATB2+ cell numbers recovered and layering improved ... although RNA levels did only partially"; the Discussion calls the W-AAV result "supraphysiological expression of WWOX in all cell populations seen in COs and a partial rescue" |
| Window limits | Add-back at stem-cell stage cannot be a time-of-intervention test; the lenti arm precedes the earliest measurement by one to two weeks |
| Class | W-AAV: **PREVENTED (by construction), partial**. Lentivirus excitability: **EARLY-WINDOW**, not RECOVERED, because the earliest recording is already after treatment |

### 2.4 Steinberg 2026, *Brain* (PMID 42397075; receipts `FTR-20260810-42397075-04` complete, `FTR-20261023-42397075-01`, `FTR-20261025-42397075-01`)

Source read for the re-read: accepted-manuscript PDF (`PMID42397075_Steinberg2026_OUP-AM.pdf`, sha256 `9775f766...`); page and line numbers below are that file's.

| Field | Content |
|---|---|
| System | WOREE and SCAR12 patient-derived organoids, engineered knockout, WT |
| Intervention time | "we infected week 10 organoids with either AAV9-WWOX ... or AAV9-EGFP ..., followed by 6 weeks of culture" (Results, "Neuron-specific Gene Therapy Rescues Neuronal Hyperexcitability", p.12 lines 30-31) |
| Onset | hyperactivity measured "in an earlier time point, where both organoids showed similar neuronal hyperactivity [Fig. 1B(i) and Fig. 1C]" (p.12-13); Fig 1C legend: "week 7 of culture" (WT and KO raster; the patient-line quantification is in 1D). So the phenotype exists at week 7, three weeks before infection |
| Endpoints | Ca2+ imaging firing at week 16 (percentage active ROIs, event amplitude, rate); CTIP2/SATB2 at week 16; transcripts of neurons; radial-glia DEGs and cell cycle |
| Comparison | AAV9-EGFP control in the same lines, plus WT. No recording of the same organoids before infection |
| Follow-up | 6 weeks (to week 16) |
| Persistence | UNMEASURED beyond week 16 |
| Limits | "Remarkably, neuron-specific restoration of WWOX was sufficient to reduce hyperexcitability to a level similar to the WT organoids". CTIP2/SATB2 rose in WOREE "but not in SCAR12, which showed ... levels similar to WT". Radial-glia abnormalities were not corrected, and the infection "did not affect the RGs" (p.13). Discussion p.16: "neuron-targeted AAV9-hSynI-WWOX restoration effectively rescued neuronal functional phenotypes without correcting RG abnormalities, suggesting that optimal therapeutic intervention may require stage and cell-type-specific targeting depending on disease progression". Organoid age is culture age, not gestational age (earliest-lesion analysis, section 3 there) |
| Class | hyperexcitability and layer-marker output in WOREE organoids: **RECOVERED in a model (post-onset by 3 weeks, for one endpoint family, one time point)**; radial-glia and progenitor composition: **not recovered by this arm** |

### 2.5 Breton 2021, *Neurobiol Dis* (PMID 34634460; receipts `FTR-20260810-34634460-02`, `FTR-20261019-34634460-01` complete)

| Field | Content |
|---|---|
| System | Synapsin-Cre neuron-specific knockout (S-KO) mouse, neocortical slices |
| Intervention | acute bath d-APV 50 uM; also CBX, BB-FCF; no genetic add-back |
| Onset | slices aged P13-P17 only; "Since the recordings were obtained at P13-17, yet these mice die between 3 and 4 postnatal weeks, the chosen age group may mimic a late-stage disorder of WWOX" (Discussion 3.4) |
| Endpoint, comparison | spontaneous burst frequency, duration, amplitude, baseline versus drug versus washout; WT slices carry no bursts (0 of 11) |
| Follow-up, persistence | minutes. d-APV "eliminated the spontaneous bursting events ... Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal" (after washout the burst properties return, i.e. the bursting reappears). The effect does not outlast the drug |
| Limits | ex vivo, acute, one age band; the authors "cannot rule out the possibility that a pannexin 1 blocker could be an anti-epileptic treatment at earlier developmental stages" |
| Class | **symptom-level suppression of a manifested network state, reversible; neither PREVENTED nor RECOVERED**. Pharmacological, not genetic, so it is outside the rescue class but it is the only manifested-state intervention in a neuron-specific knockout |

### 2.6 Tsuruwaka 2015, *PeerJ* (PMID 25649963; receipts `FTR-20260921-25649963-01`, `FTR-20261003-25649963-02`)

| Field | Content |
|---|---|
| System | zebrafish morphant (MO and siRNA), not a mutant |
| Intervention | phenotype rescue "by co-injection of a target gene RNA (ADH domain) that does not bind MO or siRNA" at the single-cell stage (Methods) |
| Onset, endpoint | pericardial/yolk oedema from the segmentation period, 48 hpf penetrance 56 and 62 percent; embryos "died within 1 week" |
| Comparison, follow-up | MO-alone and siRNA-alone; follow-up about 48 hpf to 1 week; no neural endpoint |
| Class | **PREVENTED by simultaneous co-injection, non-neural endpoint (oedema)**. No zebrafish evidence on neurodevelopment, seizures or later intervention. Mechanism-level only |

### 2.7 Others read and what they contribute to the question

| Study | Role | Statement |
|---|---|---|
| Cheng 2020 (PMID 32000863; `FTR-20260804-32000863-01`, `FTR-20261021-32000863-03`) | onset reference for a null allele other than the one used in the rescue studies | "In our generated Wwox-/- mice, spontaneous epileptic seizures were commonly observed after postnatal day 12." Ethosuximide before PTZ suppressed provoked seizure in nulls (Fig 7b): acute, provoked endpoint, symptom-level, age stated only as "preweaning" |
| Repudi 2021 *Brain* (PMID 33914858) via Obeid intro and discussion | cell-type necessity | Nestin-Cre and Synapsin-Cre deletion gives "severe epilepsy, hypomyelination, ataxia, and early lethality by 3-4 weeks"; astrocyte (GFAP-Cre) and oligodendrocyte (Olig2-Cre) deletion "produced no overt abnormalities" (Obeid Discussion; not re-read here: UNVERIFIED at its own source) |
| Rat lde: Tochigi 2019, Iacomino 2020, Suzuki 2007/2009 | timing of lesion, no intervention | registry: measures "no rescue or reversibility" (PAPER 021); rescue in the rat is **UNMEASURED**. Not re-opened (UNVERIFIED by me) |
| Conditional / inducible | requirement not reversibility | all conditional alleles in the corpus are constitutive-from-development Cre lines (Nestin, Synapsin, GFAP, Olig2, Alb, BK5, Cd19, Osterix). A repository search of manifests and registry for tamoxifen / Cre-ER / doxycycline-regulated in-vivo Wwox found none in a neural context; a bounded PubMed search (two queries, 2026-10-29) returned two irrelevant records. **No inducible neural deletion or restoration is known to this record: UNMEASURED** (a bounded search, not proof of absence) |
| Earlier-lesion datum (not mine) | pre-P5 systemic signal | body weight already below WT at day 3 in a systemic null (earliest-lesion analysis, 2026-09-21, from PAPER 057, `figure-attestation-from-prior-session`). **UNVERIFIED: the paper's full text is not on disk** |

---

## 3. Verbatim timing statements that the verifier should check first

1. Repudi 2021, Discussion: "The limited life span and poor conditions of Wwox-null mice prompted us to treat these mice very early on in their life (P0)."
2. Obeid 2026, Results, last section: "Therapeutic rescue beyond this early postnatal window was not explored ..."
3. Obeid 2026, Discussion: "Therapeutic intervention beyond this period was not feasible, as Wwox-null mice rapidly deteriorate after P5 ..."
4. Obeid 2026, Results (ECoG): recording "beginning at approximately P14 after ICV administration at P0".
5. Obeid S8 legend: "treated with AAV9-hSyn1-hWWOX (2.63x10^11 vg) at P1-P5 (n=3-7)"; S8A has no P4 survival curve.
6. Steinberg 2021 Methods: "At day 35 of culture, individual COs were transferred ..."; legend: "week 6"; Fig EV legend: "week 7 WT and KO COs".
7. Steinberg 2026 Results: "we infected week 10 organoids ... followed by 6 weeks of culture".
8. Breton Discussion 3.4: "the chosen age group may mimic a late-stage disorder of WWOX."
9. Cheng 2020: "commonly observed after postnatal day 12."
10. Tsuruwaka Methods: "phenotype rescue was achieved by co-injection of a target gene RNA (ADH domain)".

---

## 4. Synthesis

### 4.1 Prevented, recovered, unmeasured

| Damage | PREVENTED (early-window) | RECOVERED after manifestation | UNMEASURED |
|---|---|---|---|
| Lethality, growth failure, hypoglycaemia (null mouse) | yes, P0-P5, one laboratory; survival to about one year, with an unexplained late attrition in the 2021 cohort | none | any intervention after P5; whether the P5 arm's 25 percent early loss (S8B) reflects a window edge (n=7, one curve) |
| Seizures / SWD (null mouse) | SWD rate at P14-21 not different from WT at HD, one dose, n=5; no spontaneous seizures reported in treated animals | none | convulsive repertoire (SWD is an absence-type correlate); low-dose ECoG; any treated-after-onset ECoG |
| Network hyperexcitability (organoid) | stem-cell add-back (partial, supraphysiological) | **AAV9-WWOX at week 10 on a phenotype present at week 7, read at week 16** | persistence beyond week 16; effect at later culture age; same-organoid baseline |
| Myelination | improved at P17-P90 with residual gaps, never quantified in the treated arms of the 2026 paper | none | whether an already hypomyelinated brain can re-myelinate (no treated-after-onset myelin arm); oligodendrocyte-autonomous function (MBP-promoter arm gave no detectable protein) |
| Astrogliosis | GFAP back to WT at P5 injection (S8I) | none | |
| Radial-glia / progenitor composition, MYC | not tested by gene addition in vivo; stem-cell add-back partially | **not recovered** by neuron-targeted AAV at week 10 ("without correcting RG abnormalities") | progenitor-targeted restoration; timing of the prenatal lesion (the earliest looked E12.5 is already abnormal) |
| Cerebellum, ataxia endpoints | motor score improved | none | cerebellar efficacy endpoint (vector reaches cerebellum least; protein stays below WT at P30 and P300) |
| Tumour surveillance, overexpression toxicity | | | not measured in a powered way ("limited number" at 8-11 months) |

Reading: in mouse, WWOX re-expression is shown only as an early-window intervention. The organoid arm is the only
genetic add-back after a documented phenotype, and it recovers function-level output, not progenitor state.

### 4.2 What broad recovery may require

- Treatment inside the same developmental period as the mouse P0-P5 window, **or** evidence that a later window works.
  The sentence "rapidly deteriorate after P5" is the authors' own limit, not a boundary of responsiveness. Neither
  statement licenses a human age.
- A neuronal compartment is necessary and sufficient in the mouse for survival and glycaemia (neuronal promoter works;
  oligodendrocyte promoter gave no detectable protein, so that question is open). Radial-glia abnormalities in organoids
  survive neuron-targeted add-back, so broad recovery of the prenatal substrate would need a progenitor-stage action.
- Dose in the dosed range: LD gave survival to a median of about day 48 and no animal to P90, HD gave WT-like survival
  (Fig 3B reading, entry 41). Two doses do not separate a step from a gradient (kept as stated in the registry).
- Expression is regionally uneven (cerebellum low) and supraphysiological in survivors; the transfer to a missense
  context is a reason to expect a different, not a larger, result (card C01 text).

### 4.3 What a bridge intervention should preserve or improve

A bridge intervention is anything given before or alongside a disease-modifying route. From the table:

- Preserve the **early window**: whatever is chosen should not delay or damage the early-window route, and should leave
  the neuronal compartment competent to receive it. Chronic NMDAR block is a named unmeasured risk for activity-dependent
  myelination (needs register).
- Improve the **endpoints that deteriorate before P5-P14** in the null: glucose and weight (P10), seizure onset (after
  P12), network bursting (P13-P17). Symptom control (acute d-APV, ethosuximide pre-treatment) acts on manifested states,
  reversibly, and says nothing about trajectory.
- Do not count a symptom endpoint as protection of development (SEIZURE-CONTROL-SYMPTOMATIC is already worded so).

### 4.4 Endpoints that would distinguish prevention from recovery

1. A **pre-treatment baseline in the same animals** (or an age-matched untreated cohort sacrificed at the injection
   day) for glucose, weight, spike rate and MBP; without it P5 results cannot be called recovery.
2. **Treated-after-onset arms**: injection at an age after the first measured abnormality (glucose at P10, ECoG at P14),
   with the untreated comparator measured at the same age. The model's life span (death at about P15) limits this to
   organoids or a slower-onset model.
3. **Untreated-null versus treated-at-each-age contrasts** (S8 compares treated with WT; the "ns" is not equivalence).
4. Quantified myelin (MBP densitometry or g-ratio) at the same age across KO, treated, WT.
5. **Reversibility proper**: stop or switch off the transgene, or a Cre-ER restoration/deletion, to see whether the
   benefit is maintained (none exists).
6. Persistence in organoids beyond week 16 and with a same-organoid baseline before infection.

---

## 5. Cards and needs whose meaning changes, with exact proposed wording

Wording is proposed for the orchestrator to apply; nothing in `cards/`, `needs/` or `view/` was edited.

| Item | Current text (quoted) | Proposed change |
|---|---|---|
| Card `C01_aav9_wwox` `temporal_or_model_limit` | "earliest postnatal treatment ages only and NOT_MEASURED is not SMALLER; ..." | Append: "Every endpoint is measured after neonatal treatment (P0 to P5) in animals that were never measured before treatment: the result is PREVENTION or EARLY-WINDOW, not recovery of a manifested deficit. No treated-after-onset arm exists; the authors state later intervention 'was not explored' and that this reflects 'model-specific biological constraints and technical limitations, rather than a definitive boundary'." |
| Card `C01` `endpoint_pursued` | "Restoration of WWOX function by neuron-directed replacement; the single useful endpoint carried is spike-wave discharge rate." | Replace "Restoration" by "Early-window restoration (before the first recorded phenotype at about P14)". Add: "SWD rate is a prevention readout." |
| Card `C04` `temporal_or_model_limit` | same as C01 | Same append as C01, plus: "P5 arm: survival 75 percent from about day 35 to day 300 (n=7, S8B); no P4 survival curve; S8 compares treated against wild type, so ns is not equivalence." |
| Card `C04` `functional_evidence_available` | "survival to 300 days at the higher level ..." | Add: "all PREVENTED/EARLY-WINDOW; astrogliosis at P5 injection back to WT (S8I); myelin unquantified in treated arms." |
| Need `NEED-WWOX-GENE-ADDITION` `inferred` | "That gene addition would act in humans at the stage a patient is treated (the efficacious window in mouse is perinatal, and the stated reason is model survival)." | Replace by: "That gene addition would recover a manifested deficit: in the mouse every endpoint is measured after P0-P5 treatment of animals never measured before it (prevention or early-window). The only post-onset add-back is organoid hyperexcitability at week 10 to 16, which did not correct radial-glia abnormalities." Add to `do_not_assume`: "Do not carry a perinatal result to a later intervention." |
| Need `NEED-WWOX-GENE-ADDITION` label / goal | goal `deep_recovery` | Keep the goal field, add to `notes`: "Goal reads 'deep recovery' as an aim; the evidence is early-window prevention plus one organoid post-onset functional recovery." |
| Need `NEED-MYELINATION` rationale | "A structural deficit that partly recovers after the causal (neuronal) rescue, so recovery is achievable in principle." | "A structural deficit that is partly prevented when WWOX is restored in neurons at P0-P5; whether an established hypomyelination re-myelinates is unmeasured, and the treated arms of the 2026 paper are unquantified." |
| Need `NEED-SYSTEMIC-GLYCAEMIA-GROWTH` rationale | "Supportive endpoint correction." | "Endpoints prevented by early neuronal restoration (glucose normal at P14 and P20 at HD, weight WT-like at P30); correction after the hypoglycaemia is established was not tested." |
| Need `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR` | "A perturbation result, not a reversal inference: ..." | Append: "The slice is a P13-P17 manifested state ('may mimic a late-stage disorder'); the effect is acute and reverses on washout. It is symptom-level suppression, not prevention and not recovery." |
| Card `F01_glutamate_receptor_node` `temporal_or_model_limit` | "Juvenile mouse slices, one laboratory, acute pharmacology; the authors themselves bound the age window; ..." | Append: "The state tested is manifested (burst already present at P13-P17); no drug was given before onset or for longer than minutes, so nothing is known about prevention or persistence." |
| Need `NEED-MYC-PROGENITOR-PROLIFERATION` (and card D01/D02 text on A51) | organoid progenitor phenotype | Add: "Neuron-targeted AAV9-WWOX at week 10 did not correct radial-glia abnormalities; the progenitor phenotype is the part of the disease for which no genetic add-back after onset has been shown." |
| Any card or view text using "rescue" or "reverses" for AAV9 | e.g. C01 "Recovery of function by replacement (R-class demonstrated in the null mouse)" (`p4_card.expected_contribution`) | Replace "Recovery" by "Early-window restoration"; "R-class demonstrated" by "early-window benefit demonstrated; recovery after onset not tested". |
| View thread / first-screen text on gene addition | (not read here) | UNVERIFIED: the orchestrator should grep `view/` for "recover", "reverse" and "rescue" next to AAV9 and apply the same two-state wording (PREVENTED/EARLY-WINDOW versus RECOVERED). |

Proposed new column for the need x intervention matrix: `window state` with values `prevented_early_window`,
`recovered_post_onset_model`, `symptom_suppression_reversible`, `unmeasured`.

---

## 6. Staged receipts

Staged JSONs under `disease-models/wwox/research/receipt_staging/scientist-b/` (listed in the report): one per
re-read PMID (42422765, 34747138, 34268881, 42397075, 34634460, 25649963, 32000863). All are `partial_fulltext_read`,
coverage understated, `reread_reason` `new_question_outside_prior_coverage`. The integrator records them.

## 7. UNVERIFIED

- Body weight below WT at day 3 (PAPER 057 / PMID 19936220): full text not on disk.
- Rat lde reversibility/rescue absence: registry statement only (PAPER 021), not reopened.
- Repudi 2021 *Brain* (PMID 33914858) cell-type necessity: taken through the Obeid text, not reopened.
- Cheng 2020: age of the PTZ/ethosuximide test is "preweaning" only; the null allele differs from the rescue studies' allele, so the "after P12" onset is a cross-line reference.
- Steinberg 2026: page and line numbers are of the accepted manuscript; the published version and its supplement were not opened (the supplement is absent on this host, see registry PAPER 094).
- Obeid Figure 7 vector panels were not re-rendered today (reuse of entry 43).
- A fuller literature search for inducible Wwox models and zebrafish/rat rescue is a bounded one (registry plus two PubMed queries); absence is not established.
- Whether the P5 arm's 75 percent plateau reflects a window edge: n=7, one curve; not decided.
