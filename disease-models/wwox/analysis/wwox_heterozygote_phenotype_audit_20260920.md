# WWOX heterozygote neuro-phenotype audit — is it reported outside the Chang lab?

**Date:** 2026-09-20 · **Batch:** `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION`
· **Actor:** Scientist B · **Target proposition:** *the `Wwox` heterozygote neurobehavioural /
cognitive phenotype* · **Anchor claim:** `CLAIM 032` (in observation, clinical relevance VERY HIGH).

Non-canonical analysis file. **No canonical file edited. No commit candidate created. `CLAIM 032`
is not overturned here** — this file establishes the *evidence state* behind it.

> 🔴 **Declared acquisition ceiling, stated before any finding.** Network egress denies
> `eutils.ncbi.nlm.nih.gov` and `ebi.ac.uk`; `WebFetch` to `pmc.ncbi.nlm.nih.gov`, `jbc.org`,
> `sciencedirect.com` is `EGRESS_BLOCKED`. The **PubMed MCP server is the only reading route** and
> it reaches PMC open-access deposits only. There are no PDF tools and no figure images.
> Consequences that bind every line below:
> 1. **No finding here is anchored to a figure panel.** No panel was inspected. None is claimed.
> 2. The MCP text extraction **strips italicised gene and genotype tokens**. In rodent papers this
>    deletes exactly the strings `Wwox`, `+/+`, `+/−`, `lde/lde`, `+/lde`. Where a sentence below
>    needs a genotype that the extraction removed, this is **marked `[genotype stripped]`** and the
>    genotype is inferred from the surrounding argument, never asserted as verbatim.
> 3. Superscript exponents are also stripped from p-values (`3.7 × 10` for what is certainly
>    `3.7 × 10⁻⁸`). Exponents are **not** reproduced as fact below.

## Per-paper read depth (honest)

| Source | PMID | Route | Depth |
|---|---|---|---|
| Aldaz 2014, *BBA Rev Cancer* (review) | 24932569 | PMC4151823 | **full** (body read, het passage located verbatim) |
| Tochigi 2019, *IJMS* (`lde` rat) | 31340538 | PMC6678113 | **full** (Results + Methods read end to end) |
| Breton 2021, *Neurobiol Dis* (Carlen/Aqeilan) | 34634460 | PMC8609180 | **full** (Results, Discussion, Methods) |
| Cheng 2020, *Acta Neuropathol Commun* (NCKU) | 32000863 | PMC6990504 | **full** |
| Hussain 2018, *Neurobiol Dis* (Aldaz) | 30290271 | PMC7104842 | **full** |
| Aldaz & Hussain 2020, *IJMS* (review) | 33255508 | PMC7727818 | **full** |
| Obeid 2026, *Mol Ther Adv* (Aqeilan GT) | 42422765 | PMC13343157 | **full** |
| Repudi 2021, *EMBO Mol Med* (Aqeilan GT) | 34747138 | PMC8649866 | **full** |
| Chang 2022, *IJMS* (Chang lab, het NOR) | 36498839 | PMC9739312 | **full** |
| Chang 2017, *Alzheimers Dement (N Y)* | 29067327 | PMC5651433 | full — **read in Wave 1**, re-used here, not re-read |
| Iacomino 2020, *Front Neurosci* | 32581702 | PMC7300205 | **full** (no heterozygote content) |
| Ludes-Meyers 2009, *PLoS ONE* | 19936220 | — | **abstract only** |
| Leppa 2016, *AJHG* (ASD CNV) | 27569545 | — | **abstract only**; het-CNV numbers below are **review-reported** via PMID 33255508 |
| Mallaret 2014, *Brain* | 24369382 | PMC3914474 | ⛔ **body blocked** — PMC deposit returns an **empty `full_text`**; abstract only |
| Repudi 2021, *Brain* (neuronal KO) | 33914858 | — | ⛔ **no PMCID — acquisition-blocked** |
| Suzuki 2009, *Genes Brain Behav* (`lde` rat, audiogenic) | 19500159 | — | ⛔ **no PMCID — acquisition-blocked**; abstract only |
| De La Cruz 2025, *bioRxiv* (Aldaz co-author) | 39868255 | PMC11761808 | ⛔ **body empty** — abstract only; **genotype unresolvable** (see §4) |

Search coverage: PubMed queries on `Wwox AND (heterozygous OR heterozygote OR haploinsufficiency)`
(**31 records, all triaged**), `Wwox AND (behavior OR cognition OR memory OR learning OR novel
object)` (101), `Wwox AND (seizure OR epilepsy OR EEG OR excitability OR ataxia) AND (mouse OR mice
OR rat)` (23), `Aqeilan RI[Author] AND Wwox AND (brain OR neural OR epilepsy OR behavior)` (15),
`Wwox AND (Nestin-Cre OR conditional knockout OR neuron-specific OR Syn1-Cre OR brain-specific)` (4),
`Wwox AND (lde OR Tochigi OR Suzuki H OR rat) AND (brain OR neuro OR behavior)` (14),
`Wwox AND (Morris water maze OR open field OR rotarod OR elevated plus OR fear conditioning OR novel
object recognition)` (**2 records in all of PubMed**), `WWOX AND (carrier OR parents) AND (cognitive
OR EEG OR neuroimaging OR subclinical OR intellectual disability)` (7).

---

## 1 · The table

| Source | Lab | Model & allele | Age | Endpoint measured | n | Heterozygote result | Analysed, or just a control? |
|---|---|---|---|---|---|---|---|
| **Chang 2017** PMID 29067327 §3.5 | Chang NS, NCKU | germline `Wwox+/−` mouse | "age-related", ~11 mo implied | novel object recognition (STM + LTM) | **not reported** | **worse**: "an age-related faster decline in both short- and long-term memories than those in 3xTg mice" | **Analysed** — but one sentence, no n, no statistic, no figure |
| **Chang 2022** PMID 36498839 §2.5 | Chang NS, NCKU | germline `Wwox+/−` mouse | **10 months** | novel object recognition (STM + LTM) | **not reported anywhere in the paper** | **worse**: "wild-type mice performed significantly better than heterozygous [Wwox] mice" | **Analysed** (primary comparison) |
| **Chang 2022** PMID 36498839 §2.6–2.7 | Chang NS, NCKU | germline `Wwox+/−` mouse | **11 months** | cortical/hippocampal IHC: TPC6AΔ, pS35-TPC6AΔ, SH3GLB2, pT12-WWOX aggregates | not reported | **worse**: significant increases in cortex vs WT; pT12-WWOX plaques present in het, absent in WT | **Analysed** |
| **Cheng 2020** PMID 32000863 | Hsu L-J / Chang NS, **NCKU — same institution, Chang is an author** | germline `Wwox+/−` mouse (exon1 and exon2/3/4 lines) | **3 weeks** | **transcranial motor evoked potential (Tc-MEP) latency** | **n = 5 het vs n = 10 WT** | **worse**: latency **2.13 ± 0.22 ms vs 1.39 ± 0.13 ms WT, p < 0.05**; amplitude normal (59.6 ± 17.2 vs 59.2 ± 9.0 µV) | **Analysed** |
| **Cheng 2020** PMID 32000863 | idem | germline `Wwox+/−` | **P18–20** | rotarod (constant + accelerating), footprint/gait, limb-clasping | not reported | **normal**: "There were no significant differences between [WT] and [het] mice" | **Analysed** (explicit negative) |
| **Breton 2021** PMID 34634460 | **Carlen (Toronto)** + Aqeilan — *outside the Chang lab* | **Syn1-Cre conditional** `Wwox^fl/+` ("S-HT") | **P13–P17** | neocortical slice LFP — spontaneous epileptiform bursting | **23 slices / 14 S-HT** vs **11 slices / 7 S-WT** vs **42 slices / 24 S-KO** | **intermediate**: bursting in **4 of 23** S-HT slices vs **0 of 11** S-WT slices vs **36 of 42** S-KO slices. **No statistic reported for S-HT vs S-WT** | **Analysed as its own group** — then **frequently pooled with WT into "S-CTL"** for the cellular assays |
| **Breton 2021** PMID 34634460 | idem | idem | P13–P17 | hippocampal slice LFP | as above | **normal**: "hippocampal slices exhibited spontaneous activity indistinguishable from controls or heterozygotes" | Analysed |
| **Breton 2021** PMID 34634460 | idem | idem | P13–P17 | overt behavioural seizures (visual) | — | **normal**: "there are no clear behavioral seizures in these animals" | Observed, not instrumented |
| **Tochigi 2019** PMID 31340538 (**`CLAIM 032` source**) | Suzuki H / Katayama, Nippon Vet & Life Sci Univ | **rat `+/lde`** | **PND 5, 10, 15, 21** | **western blot band intensity + immunohistochemistry only** | ≥3 per group per day | Wwox protein "almost half"; cortical layer V + corpus callosum IHC intense as `+/+` | **Not analysed as a phenotype group.** Het is a *protein-dosage datum*; Methods pool `+/+` and `+/lde` as "normal" controls. **No behavioural, EEG or cognitive test exists in this paper** |
| **Aldaz 2014** PMID 24932569 (**`CLAIM 032` source**) | Aldaz, MD Anderson (**review**) | germline `EIIA-Cre;Wwox+/−` mouse | lifespan | **spontaneous neoplasia; lifespan** | not given (review) | "no evidence of spontaneous neoplasia"; "lifespan … indistinguishable from WT mice" | **Not analysed neurologically.** See §2 — the "not deleterious" sentence is a **tumour** sentence |
| **Hussain 2018** PMID 30290271 | Aldaz, MD Anderson | `Wwox` KO vs `flox` littermate controls | **2 weeks** | PV+/NPY+ interneuron stereology, GFAP, IBA-1, transcriptome | **7 vs 7** | **het not in the design** — controls are floxed littermates, not heterozygotes | **Absent** |
| **Aldaz & Hussain 2020** PMID 33255508 (review) | Aldaz, MD Anderson | germline `Wwox+/−` mouse | unspecified | narrative | — | **normal**: "heterozygous [Wwox] mice, similar to mutation carrier parents of WOREE children, **failed to display any distinct abnormal CNS phenotypes** or significantly decreased overall survival" | **Review assertion, unquantified**; primary is Mallaret 2014 — **body blocked** |
| **Repudi 2021** PMID 34747138 / **Obeid 2026** PMID 42422765 | Aqeilan, Hebrew Univ | germline `Wwox+/−` mouse | adult | **breeding; fertility rate and litter size only** | 20 breeding cages/group (Obeid) | comparable to WT | **Pure control / breeder. Never analysed neurologically.** The whole colony is het×het bred; every experiment had het littermates and none was phenotyped |
| **Hussain 2023** PMID 36828035 (LEGEND receipt `FTR-20260826`) | Aldaz, MD Anderson | **`Wwox^P47T/WT` — missense het, not null het** | adult | clasping, sociability, social novelty; survival | small | **normal** on all three; survival difference from WT **not significant**; but het **is** named in a positive liver/gallbladder histopathology finding | Analysed — **but a missense het is weak transfer to a haploinsufficiency claim** |
| **Suzuki 2009** PMID 19500159 | Suzuki H, Nippon Vet & Life Sci Univ | rat `lde/lde` | post-PND16 | audiogenic seizure susceptibility + EEG | — | **`+/lde` not mentioned in the abstract**; body ⛔ blocked | **Unknown — acquisition-blocked** |
| **Leppa 2016** PMID 27569545 (via review PMID 33255508) | Geschwind, UCLA — *fully independent* | **human heterozygous `WWOX` CNVs** (intragenic del/dup) | children | ASD diagnosis (AGRE + SSC) | 3565 families vs 2633 unaffected sibs | **enriched**: 12 families (0.34%) vs 1 unaffected sibling (0.04%), **p = 0.01, OR = 8.8**; authors call `WWOX` a "**low-penetrance ASD associated locus**" | **Analysed** (human monoallelic) — ⚠️ **review-reported, primary body not read** |

---

## 2 · What `CLAIM 032` actually rests on

`CLAIM 032`'s own caveat already says the threshold is known "per **sopravvivenza e morfologia**, non
per **cognizione ed epilessia**." This audit confirms that caveat is *exactly right*, and sharpens it
in one place the claim does not currently state.

### Source 1 — Aldaz 2014, PMID 24932569 (*BBA Rev Cancer*) — **a review, and the quote is a tumour sentence**

Verbatim, from the body (PMC4151823, §7.1):

> "analysis of EIIA-Cre; Wwox KO mice found **no evidence of spontaneous neoplasia in any tissue
> examined**. This was also the case for EIIA-Cre;Wwox heterozygous mice indicating that **loss of
> one Wwox allele (i.e. haploinsufficiency) appears not to be deleterious or carcinogenic in the
> longer-lived heterozygous mice**."

**What was measured:** spontaneous neoplasia, and lifespan. **At what age:** lifespan-long observation.
**What was not measured:** anything neurological. The sentence LEGEND quotes as the general-purpose
"haploinsufficiency is not deleterious" line is the **second half of a sentence whose subject is
spontaneous tumour formation**, and the qualifier "or carcinogenic" is in the source and is dropped
when the quote is shortened. This is also a **narrative review**, not a primary phenotyping study;
the primary is Ludes-Meyers 2009 (PMID 19936220), whose abstract characterises metabolic acidosis,
hypoglycaemia, hypocalcaemia, impaired haematopoiesis and bone mineralisation in the KO — and runs
**no behavioural test on any genotype**.

The same review also records, in the same paragraph, the countervailing fact: "**Increase
tumorigenicity was reported when Wwox heterozygous mice are exposed to chemical carcinogens … or when
backcrossed into a C3H mammary tumor susceptible genetic background**." The het is unremarkable
**unchallenged** and not unremarkable **challenged** — which `CLAIM 032`'s `BATCH_20260815_001`
qualification already records.

### Source 2 — Tochigi 2019, PMID 31340538 (*IJMS*) — **no behavioural endpoint exists in this paper**

The `+/lde` datum LEGEND quotes is real and I confirm it. Verbatim [genotype stripped by extraction]:

> "Assessments of brains of [`+/lde`] rats showed a **single band of normal molecular weight, but its
> intensity was almost half** that observed in [`+/+`] rats. … Immunohistochemistry showed intense
> signals of Wwox protein in the cerebral cortex layer V and corpus callosum of [`+/+`] and
> [`+/lde`] rats, but not of [`lde/lde`] rats."

**What was measured:** western-blot band intensity, and immunohistochemistry of neurons / astrocytes
/ oligodendrocytes / microglia. **At what age:** **PND 5, 10, 15 and 21 — weanlings.** **n:** "At
least three affected and three normal males were included in each experiment (**western blot and
immunostaining**) and examined each day."

Three things follow, and they matter:

1. **The entire methods section contains only immunohistochemistry and western blotting.** There is
   no rotarod, no maze, no EEG, no seizure challenge. **This paper cannot speak to cognition or
   epilepsy in the heterozygote because it measured neither, in any genotype.**
2. The Methods treat `+/+` and `+/lde` as one pooled category: "**Normal** ([`+/+`], [`+/lde`]) and
   [`lde/lde`] rats at PNDs 5, 10, 15, and 21 were anesthetized…". The heterozygote is a *control
   arm*, not an analysed group.
3. Maximum age is **PND 21**. Both Chang-lab het findings are at **10–11 months**. Tochigi's design
   could not have seen an aged phenotype even if it had run behaviour.

### Source 3 — the published human carrier parents (Shaukat, Elsaadany, Abdel-Salam, Mallaret, Johannsen)

**What was measured:** in every case, the carrier parent's **clinical unremarkableness as observed
during a proband work-up**. Abdel-Salam 2014 (PMID 24456803), which `CLAIM 032` cites, states only:
"As in rats, **no tumors** were observed in the patient or heterozygous mutation carriers." That is a
**tumour** observation, again.

**At what age:** adult, single time point, incidental. **What was not measured, in any published
WWOX-DEE family:** no carrier parent has had a formal neuropsychological battery, an EEG, or
structural/quantitative neuroimaging reported. My search
(`WWOX AND (carrier OR parents) AND (cognitive OR EEG OR neuroimaging OR subclinical OR intellectual
disability)`) returned **7 records and none is a carrier phenotyping study**. The human leg of
`CLAIM 032` is therefore **"nobody looked", not "somebody looked and found nothing."**

---

## 3 · Who outside the Chang lab has measured it

**Breton et al. 2021, PMID 34634460 (Carlen lab, Toronto; Aqeilan co-author) is the one non-Chang
paper that analysed heterozygotes as their own group on a CNS endpoint — and it found a signal.**

> "In the neocortical preparations, spontaneous electrographic bursting activity was present in S-KO
> mice, but not present in S-WT control slices (**0 of n = 11 slices from 7 S-WT mice; 4 of n = 23
> slices from 14 S-HT mice; 36 of n = 42 slices from 24 S-KO mice**)."

And, in the Discussion, the authors state it as a finding:

> "**Of note, the spontaneous bursts resulting from WWOX deletion were also observed in heterozygote
> mice, and manifested similarly as those observed in the knockouts.** The presence of these bursts
> in the heterozygote **may be reflective of epileptic network activity**; however, there are no
> clear behavioral seizures in these animals. We cannot discount the possibility that heterozygotes
> have a form of absence seizures that we are unable to detect visually. However, the more likely
> explanation is that it reflects a **negative correlation between WWOX protein expression and
> hyperexcitable bursting activity**."

Five limits, all load-bearing:

- The model is a **Synapsin1-Cre conditional heterozygote** (`Wwox^fl/+`; Cre+), **not a germline
  null heterozygote**. Neuron-restricted monoallelic loss is not the same genotype as a carrier.
- **No statistical test of S-HT vs S-WT burst incidence is reported.** 4/23 against 0/11 is a
  direction, not a demonstrated difference. I did not compute a test and do not assert one.
- The paper's own design instruction pulls the other way: "**Where no significant difference exists
  between S-HT and S-WT groups, they are occasionally represented as a clustered group (S-CTL)**."
  For the cellular electrophysiology the heterozygote is **absorbed into the control**.
- Age **P13–P17** — developmental, not aged. So this is *not* a replication of the Chang aged-memory
  result; it is a different endpoint at a different age.
- Aqeilan is a co-author and supplied the mice, so this is **not fully lab-independent of the Aqeilan
  axis** — but it is unambiguously independent of the Chang lab.

**Second, within the NCKU orbit but on a different endpoint: Cheng 2020, PMID 32000863.**

> "Although the mean amplitude of Tc-MEP recoded in [het] mice (59.6 ± 17.2 μV; n = 5) was comparable
> to [WT] mice, an **increase in Tc-MEP latency was determined in [het] mice (2.13 ± 0.22 msec;
> p < 0.05)** when compared with the wild-type mice, suggesting that **[Wwox] haploinsufficiency may
> cause a partial Tc-MEP deteriorative change in mice**."

At **3 weeks of age**, with the *same animals* normal on rotarod, gait and clasping at P18–20
("There were no significant differences between [WT] and [het] mice"). This is a **subclinical
central motor-conduction phenotype in a developmental-age heterozygote**. It is a striking
independent-endpoint echo of the Breton bursting result — normal behaviour, abnormal instrument. But
Nan-Shan Chang is an author and the work is from National Cheng Kung University, so it is
**same-institution corroboration, not independent replication**.

**Third, the human monoallelic signal — genuinely independent (Geschwind lab, UCLA).** Reported via
the Aldaz & Hussain 2020 review (PMID 33255508), which I read in full; the Leppa primary (PMID
27569545) was **not** obtained:

> "Leppa et al. identified CNVs specifically spanning the [WWOX] locus in affected children from **12
> families with multiple individuals with ASD out of a total of 3565 families (i.e., 0.34%)**, in
> comparison to **only one unaffected sibling out of 2633 families (i.e., 0.04%, p = 0.01, odds ratio
> (OR) = 8.8)**. … the authors proposed that [WWOX] qualifies as a **low-penetrance ASD associated
> locus**."

The same review adds that SFARI classifies `WWOX` as a "**Category 2 gene (Strong Candidate ASD
gene)**", that a meta-analysis of seven genome-wide linkage scans placed the `WWOX`-containing
ch16q23.1-qter region at "**very highly significant risk association with ADHD**", and — the most
directly cognitive datum in the whole audit — that in a GWAS of ~1.1 million individuals "**various
SNPs identified [WWOX] among several genome-wide significant loci associated with measures of
educational attainment**", including years of education and mathematical ability.

⚠️ **These do not establish haploinsufficiency.** Common SNPs are not monoallelic loss. Intragenic
`WWOX` CNVs occur in healthy people too — the same review notes germline `WWOX` CNVs in the normal
population are "significantly enriched, overlapping a clear hotspot within intron 5", and that DGV
puts >100 kb `WWOX` CNVs at 0.10% of 27,263 individuals. FRA16D is a fragility hotspot; a CNV there
is not automatically a null allele. What this body of work does establish is that **`WWOX` dosage
variation is statistically associated with human neurodevelopmental and cognitive outcomes** — which
is not the same proposition as `CLAIM 032`, and not its contradiction either.

**Fourth, the explicit non-Chang negative, and what it is worth.** Aldaz & Hussain 2020 (PMID
33255508) state:

> "Notably, **heterozygous [Wwox] mice, similar to mutation carrier parents of WOREE children, failed
> to display any distinct abnormal CNS phenotypes** or significantly decreased overall survival."

This is the strongest independent statement *against* a het phenotype. It is also **unquantified, in
a review, with no endpoint, no age, no n and no test named**, and its primary (Mallaret 2014, PMID
24369382) is **acquisition-blocked** — the PMC deposit returns an empty body. The Mallaret abstract
describes only that "the short-lived [Wwox] knock-out mouse display spontaneous and audiogenic
seizures"; the heterozygote is not mentioned in the abstract at all. The endpoint the negative rests
on appears to be **observed spontaneous/audiogenic seizures and gross ataxia** — i.e. the same class
of gross observation that Breton and Cheng both showed is *insensitive* to the het, since in both
papers the het was behaviourally normal while instrumented measures were not.

**Fifth, the Aqeilan colony — the largest missed opportunity in the field.** The `Wwox`-null line is
maintained by heterozygote breeding: "**Heterozygote [Wwox] mice were used for breeding to get the
[Wwox]-null mice**" (PMID 34747138), and in the 2026 gene-therapy paper heterozygotes appear once
more, as a fertility comparator — "fertility rates and litter sizes comparable to WT and
**heterozygous controls**" (PMID 42422765). Across ~15 Aqeilan-lab CNS papers, **every experiment had
heterozygous littermates available and not one reports a neurological or cognitive measurement on
them.** This is the textbook case the task named: *a heterozygous phenotype hiding in someone's
control group.*

---

## 4 · Things I could not obtain, and one I must not over-read

- **PMID 33914858** (Repudi 2021, *Brain*, neuronal `Wwox` deletion) — **no PMCID, acquisition-blocked.**
  This is the parent paper of the Breton dataset and the place a germline/conditional het
  characterisation would most likely sit. Its content reaches me only through Breton's one-line
  citation that KO mice seize "as compared to their heterozygote and wildtype counterparts".
- **PMID 19500159** (Suzuki 2009, *Genes Brain Behav*) — **no PMCID, acquisition-blocked.** The
  abstract reports audiogenic seizure induction in "95% of lde/lde rats" and says nothing about
  `+/lde`. Whether the `+/lde` rat was sound-challenged is **unknown**, and this is the single most
  valuable unobtained datum in this audit: it is the only paper in the corpus that ran a seizure
  *provocation* on a `Wwox` colony with heterozygotes present.
- **PMID 24369382** (Mallaret 2014, *Brain*) — PMC deposit returns an **empty body**. The primary
  behind the strongest non-Chang het negative is unread.
- **PMID 27569545** (Leppa 2016, *AJHG*) — abstract only. The abstract independently confirms "another
  lower-penetrance locus involving **inherited deletions and duplications of WWOX**", but the 12-vs-1
  / OR 8.8 numbers above are **review-reported and not verified against the primary**.
- **PMID 39868255** (De La Cruz 2025, *bioRxiv*, "Partial Wwox Loss of Function Increases Severity of
  Murine Sepsis and Neuroinflammation", Aldaz co-author) — PMC body **empty**, abstract only, and the
  abstract's genotype tokens are stripped. ⚠️ **I cannot tell whether "partial loss of function" here
  means a heterozygote or the `Wwox^P47T/P47T` homozygote** — the Aldaz lab uses that exact phrase for
  P47T (cf. PMID 36828035's title, "WWOX **P47T partial loss-of-function** mutation"). **It is
  therefore not counted as heterozygote evidence.** If it *is* a heterozygote, it would be a second
  independent genotype×stress CNS result and should be re-acquired when egress permits.

---

## 5 · Verdict

### `HET PHENOTYPE SINGLE-LAB ONLY`

Precisely:

- **On cognition/memory — the endpoint that matters to `CLAIM 032`'s untested axis — the answer is
  `NOBODY ELSE HAS MEASURED IT`.** In all of PubMed, exactly **two** `Wwox` papers index a named
  cognitive behavioural assay (`Morris water maze`, `open field`, `rotarod`, `elevated plus`, `fear
  conditioning`, `novel object recognition`), and **both are the Chang lab's** (PMID 36498839; and
  PMID 39868255, whose open-field is a sickness-behaviour readout in an unresolvable genotype). The
  aged `Wwox+/−` memory phenotype is **corroborated within the Chang lab across two papers and
  replicated by no one**, and even inside the Chang lab it is reported without an n in either paper.
- **On CNS phenotype more broadly, a non-Chang lab has seen a heterozygote signal.** Breton 2021
  (Carlen, Toronto) reports epileptiform neocortical bursting in 4/23 slices from 14 conditional
  heterozygotes against 0/11 slices from 7 wild types at P13–P17, and says so explicitly in the
  Discussion. It is untested statistically, in a conditional not a germline het, and the same paper
  pools het with WT elsewhere. **This is a concordant independent hint, not a replication.**
- **The published "heterozygotes are normal" statements do not cover cognition.** Aldaz 2014's "not
  deleterious" is a *spontaneous-neoplasia and lifespan* sentence. Tochigi 2019 ran **no behavioural
  test at all** and stopped at PND 21. Aldaz & Hussain 2020's CNS negative is an unquantified review
  assertion whose primary is unreadable here. Human carrier parents were never formally phenotyped.
- **The reconciliation the task anticipated is the correct one.** Both sides are right about
  different endpoints and different ages. Survival, gross morphology, gross behaviour and
  tumour-freedom in the unchallenged heterozygote: **genuinely established, and `CLAIM 032` is safe
  on that ground.** Cognition, aged cognition, network excitability and challenged states in the
  heterozygote: **either untested, or tested once, or tested with an instrument and found abnormal
  while behaviour looked normal.**

---

## 6 · What this does, and does not do, to the gene-therapy dose-threshold argument

**It does not lower the case for partial restoration, and it does not raise it.** What it removes is
the right to state the dose-threshold corollary *without a stated endpoint*. `CLAIM 032`'s corollary
— that partial restoration or therapeutic mosaicism may suffice because a carrier-equivalent state is
healthy — remains a reasonable inference **for survival, growth, gross morphology and the absence of
overt seizures**, because that is what the carrier-equivalent state has actually been shown to be
healthy *for*. It is **not yet licensed for cognition**, because the carrier-equivalent state has
never been tested for cognition by anyone outside one laboratory, and the one laboratory that tested
it found a deficit.

Three boundaries that must travel with any use of this audit:

1. **An aged-cognition phenotype in a mouse is not a developmental threshold in a human.** The Chang
   finding is at 10–11 months in an animal whose WWOX has been at ~50% since conception. It speaks to
   *maintenance* of memory in a long-lived heterozygote. A WWOX-DEE child's problem is *construction*,
   not maintenance, and `CLAIM 031` already states that a rescue arrives after part of the
   developmental damage. These are different biological questions, and a deficit in one does not
   transfer to a threshold in the other.
2. **The direction of the aged finding, if real, is conservative for gene therapy, not fatal to it.**
   It would mean the durable target is *higher than 50%*, not that partial restoration is worthless —
   Breton's own reading is "a **negative correlation** between WWOX protein expression and
   hyperexcitable bursting activity", i.e. a graded relationship, which is exactly the shape in which
   more restoration buys more benefit. Obeid 2026's dose-dependent rescue in the null is consistent
   with a graded, not a switch-like, dose-response.
3. **The strongest operational consequence is an endpoint requirement, not a claim revision.** Any
   dose-finding argument that leans on `CLAIM 032` should now name the endpoint it is claiming a
   threshold *for*, and should treat "cognitive sufficiency of ~50% WWOX" as **an open question with
   one lab's negative answer against it**, not as a settled premise. The decisive missing
   experiments are cheap and specific: a behavioural battery on aged germline `Wwox+/−` mice run by a
   lab that is not the Chang lab; a seizure provocation on the `+/lde` rat heterozygote; and EEG plus
   a neuropsychological battery on the already-identified, already-consented WWOX-DEE carrier parents.

**This is not medical advice.** Nothing here alters `BLOCCO 1`, no canonical file was edited, and no
commit candidate was created.
