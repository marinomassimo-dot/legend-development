# What separates severe WOREE from unexpectedly mild or long-lived WWOX deficiency?

**Node:** `MODIFIER_AND_RESILIENCE_BIOLOGY` · **Actor:** Scientist A · **Date:** 2026-09-21
**Status:** non-canonical analysis file. No canonical file edited, no registry written, no receipt claimed, no commit.
**Read-only toward every canonical file. Public edition — no contact details, no identifying information of any
living person. Not medical advice.**

---

## 1 · Read depth, declared before any finding

| Source | Identity | Depth reached | Body length | Figures |
|---|---|---|---|---|
| **PMID 39507621** / PMC11537890 | Teplyshova A & Sharkov A, *Front Genet* 2024 — "Case report: Adult patient with WWOX developmental and epileptic encephalopathy: 40 years of observation" · `PAPER 015`, receipt on file | 🟢 **full deposit read this wave** | ≈18 KB (estimate; not byte-exact) | ❌ |
| **PMID 25411445** | Mignot C *et al.*, *J Med Genet* 2015 — WWOX-related encephalopathies, genotype–phenotype correlation | 🔴 **abstract only** this wave. 12 registry records, **no receipt** | n/a | ❌ |
| **PMID 30949922** | Peter B *et al.*, *Behav Genet* 2019 — two siblings, compound-het WWOX, ASD + severe speech sound disorder | 🔴 **abstract only.** **Absent from LEGEND entirely** — 0 registry records, 0 receipts | n/a | ❌ |
| **PMID 27569545** | Leppa VM *et al.*, *Am J Hum Genet* 2016 — inherited WWOX CNVs, lower-penetrance ASD locus | 🔴 abstract only this wave. 2 registry records, **no receipt**; LEGEND holds an audit (`leppa2016_wwox_cnv_audit_20260920.md`) | n/a | ❌ |
| **PMID 26070663** | Weckselblatt 2015, *Genome Res* — the sole hit for `WWOX paralog` | ⚪ abstract only; **irrelevant** (incidental "paralogous repeats"; a SIRPG-WWOX fusion) | n/a | ❌ |
| LEGEND local | `CLAIM 017/020/026/030/033/036/037`, `working_model_current` row 020, `discovery_ledger_current`, dossiers `PMID33916893.md`, `PMID19936220.md`, `locator_contract_live_test.md` | 🟢 read directly | — | — |
| Receipt pre-checks | `fulltext_receipts.py status` run on all nine cohort PMIDs named in the brief — **all nine carry receipts** (30356099, 36779245, 40875931, 42193054, 39507621, 33916893, 24369382, 24456803, 36537114) | — | — | — |

🔴 **No figure panel inspected.** All tabulated ages below are reproduced from LEGEND's dossiers of papers read by
prior sessions, or from body prose I read this wave, and each is labelled with which.

---

## 2 · The direct answer

**Every survival and severity outlier in this literature is explained by allele class, by ascertainment, or by
both. No modifier of WWOX-deficiency outcome has ever been identified in any species.**

The pattern is not subtle and it is not mine — **LEGEND had already reached it** and has it queued as a commit
candidate: *"Adult survival in this disease tracks **the presence of a missense allele**, not phenotypic
mildness."* This wave adds the quantified version from the primary literature: the presence of **at least one
missense variant** is reported to raise five-year survival **from <50% to >75%**. Every long-lived patient in the
census carries a missense allele — the 40-year-old is homozygous missense, the oldest previously reported patient
(23 y 11 m) is homozygous missense, the longest DEE28 survivors in the Banne table are homozygous missense. **Test
(b) kills them all.** Ascertainment then kills them a second time: the 40-year-old carried a diagnosis of cerebral
palsy for decades and was identified only when exome sequencing arrived, so the adult WWOX cohort is composed
exclusively of people who survived long enough to be sequenced — **selected for mildness by construction**, in a
disease whose early-fatal cases born in the same era died undiagnosed. **No discordant sibling pair is established
anywhere in this literature.** On the mouse side the survival differences between laboratories are **confounded by
allele, targeting strategy, Cre driver and species** and have never been tested as background effects: nobody has
backcrossed one Wwox allele onto two strains, which is the single experiment that would convert this from noise to
a mapped modifier. **WWOX has no paralogue and no documented functional backup.**

🔵 **One thing survives, and it is the only place a modifier could still hide.** The allele-class rule is
statistical, and **its mechanism is not residual protein**. LEGEND records that **Q230P is a missense that
abolishes the protein** — yet homozygous Q230P patients are the longest survivors in two independent cohorts. So
"missense ⇒ more protein ⇒ milder" is **false for the very allele that carries the survival signal**. Whatever
makes a missense genotype survivable in WWOX disease is **not** explained by protein abundance, and that gap is
§7.

---

## 3 · Task 1 — The outlier table, with the four-test discipline applied to each

**Tests, in the order the brief specifies.** (a) genotype — null/null, or residual protein? · (b) is mildness
explained by the **allele**? · (c) is it explained by **ascertainment**? · (d) only what survives (a)–(c) is a
candidate modifier.

| # | Outlier | Genotype (a) | Allele explanation? (b) | Ascertainment explanation? (c) | Residual candidate? (d) |
|---|---|---|---|---|---|
| **O-1** | **40-year-old man, WWOX-DEE, 40 years of observation** (PMID 39507621; `CLAIM 020`, `working_model` row 020) | **homozygous missense** `c.35C>T`, `p.Thr12Met`, exon 1, N-terminal, **outside any known domain**. Protein **never measured** | ✅ **YES, decisively.** The paper itself states the rule: ≥1 missense variant raises 5-year survival **from <50% to >75%** (L-4). A homozygous missense is the most favourable class on that rule | ✅ **YES, doubly.** *"For many years, the patient was given a diagnosis of cerebral palsy"*; molecular diagnosis came **38 years after onset** (L-2). He entered the literature only because he survived into the exome era. Contemporaneous early-fatal cases died undiagnosed | ❌ **NO.** Dies at (b) and again at (c) |
| **O-2** | **Oldest previously reported living patient, 23 y 11 m**, 21 years of follow-up, EEG evolving to a diffuse low-voltage background (Oliver 2023, via LEGEND `locator_contract_live_test.md`) | **homozygous missense p.Gln230Pro** — and 🔴 **`CLAIM 030`/`CLAIM 033` record that Q230P protein is NOT DETECTED** | ✅ **YES** on allele class — but ⚠️ **NOT via residual protein.** See §7 | ✅ likely — a 21-year follow-up exists only for someone who lived 21 years | ❌ **NO as a modifier** — but it is the cleanest counter-example to the *mechanism* usually assumed for (b) |
| **O-3** | **DEE28 long survivors in the Banne 2021 table** — alive at **12 y and 10 y** (homozygous Q230P) | homozygous **missense** | ✅ YES | 🟡 partly — the table's own header is `Death/ last date of examination`, so *"alive at"* may be **follow-up length, not survival** (LEGEND's dossier, restraint 2) | ❌ NO |
| **O-4** | **Homozygous nonsense R264\*** recorded at **8 y 11 m and 5 y 2 m** — the within-genotype divergence | **null/null**, no residual protein expected | ❌ **NO — the allele is identical in both.** This is the only row where (b) fails | 🟡 **unresolved.** Same mixed-endpoint problem; and **sibship is NOT stated** (LEGEND's dossier, restraint 3), so shared background is not established | 🟡 **WEAK CANDIDATE — the only one in the table.** But it cannot be scored: the two numbers may be a death and a last examination, and the pair may not be siblings. **FLAGGED, NOT SCORED** |
| **O-5** | **Homozygous W44\*** at **7 y and 20 months** | **null/null** | ❌ NO | 🟡 same unresolved mixed endpoint | 🟡 same as O-4, and weaker — LEGEND explicitly records that *"whether the 7 y vs 20 m divergence is survival or follow-up length is not resolved by the table"* |
| **O-6** | **A homozygous Q230P patient with endpoint 3 y 3 m** — a *short* survival on the *favourable* allele | homozygous missense | ⚠️ **runs AGAINST (b)** at the individual level | — | ⚪ **Not a resilience outlier — the opposite.** Recorded because it is the honest other tail: the allele rule is a probability shift, not a determinism |
| **O-7** | **Two siblings, compound-heterozygous WWOX, presenting as ASD + severe speech sound disorder — not WOREE** (PMID 30949922) | compound het, **alleles not characterised in the abstract**; no protein data | 🟡 **probably** — a non-DEE presentation from a biallelic genotype is what hypomorphic alleles do (Mignot's rule, L-5) | ✅ **YES, strongly.** Ascertained through an **autism/speech** study, not an epilepsy clinic. A cohort recruited for ASD cannot contain severe WOREE | ❌ **NO** — but ⭐ **genuinely new to LEGEND** (§6) |
| **O-8** | **Inherited WWOX deletions/duplications as a lower-penetrance ASD locus** (PMID 27569545) | CNV, heterozygous/inherited | n/a — this is **monoallelic**, a different question | ✅ ASD-multiplex ascertainment | ❌ **NO.** Incomplete penetrance of a *heterozygous* CNV is not resilience in a *biallelic* disease. LEGEND already audited this paper |
| **O-9** | **SCAR12 in general** — later onset, ataxia, survival into adulthood | **biallelic missense / hypomorphic** | ✅ **YES — this is the definition of the allele class**, not a modifier. `CLAIM 026` | — | ❌ NO. Restating `CLAIM 026` |

**Result: 0 of 9 survive to (d) as scored candidates. Two (O-4, O-5) are flagged and cannot be scored**, for
reasons that are documentary rather than biological — a mixed endpoint column and unstated sibship.

⚠️ **One more ascertainment fact that applies to the whole table.** The 2024 case report states:
*"Approximately 80 patients with-DEE have been described in the literature, with the oldest being 23 years and 11
months old at date"* (L-3). A literature of ~80 patients, assembled from case reports and clinic series, is
**exactly the sampling frame in which survivorship bias is strongest** — severe neonatal deaths in the pre-exome
era are not in it at all.

---

## 4 · Task 2 — Discordant siblings

### **None is established. The design does not exist in this literature.**

- `WWOX siblings` → **3 records**, censused: PMID 30949922 (two **concordant** affected siblings; the third, unaffected sibling **does not carry** the compound-heterozygous genotype — so it is a segregation observation, not discordance), PMID 27569545 (multiplex ASD CNV study), PMID 25411445 (Mignot).
- `WWOX siblings discordant phenotype same variant intrafamilial variability` → **0 records**. *(Query census, not a biological zero.)*
- **Mignot 2015 reports siblings, and they are CONCORDANT:** *"the phenotype in two siblings carrying a null allele and a missense mutation was intermediate"* (L-5) — one genotype, one shared phenotypic description.
- **The two within-genotype divergences that look like discordant sibships are not established as sibships.** LEGEND's own dossier of Banne 2021 states it exactly: *"The tables write \"4 siblings\" and \"2 siblings\" explicitly for the two SCAR12 rows and write only \"2 … F/F\" for the Q230P, R264\* and W44\* pairs. Sibship is what would make a within-pair divergence a shared-background comparison, so it is **not asserted here** and must be sourced to the primary reports."*
- **The 40-year-old has a sibling and it is uninformative:** he is *"the second child of healthy, non-consanguineous parents"* with *"no family history of any neurodevelopmental disorders or epilepsy"* — so the sibling is unaffected and, by inference, not homozygous. Not a discordant pair.

**What it would take.** Two or more siblings, **genotype-confirmed identical and biallelic**, with **independently
ascertained** outcomes measured on the **same endpoint** (age at death, or age at a defined functional milestone —
not "last examination"), reported with sibship stated explicitly. The cheapest route is **not a new study**: it is
**re-interrogation of the primary reports behind the Banne table rows** to establish whether the R264\* and W44\*
pairs are sibs and whether each recorded age is a death or a censoring. That is a records question, and it would
convert O-4 and O-5 from unscoreable to either scored or dismissed.

---

## 5 · Task 3 — The mouse side, and why it is not yet a modifier result

🔴 **The operator's §12 rule applied first: these are not one animal.** Before any survival number is compared,
the allele, the targeting strategy, the driver and the laboratory:

| Model | Allele / strategy | Reported survival | Laboratory | Source status |
|---|---|---|---|---|
| **`Wwox`-null (Aldaz line)** | targeted deletion; LEGEND records the systemic null as generated with **EIIA-Cre** (`CLAIM 036`) | **43% dead by 72 h, 77% by day 17** | Aldaz / Ludes-Meyers | LEGEND dossier `PMID19936220.md`, **full text read**; the dossier also flags **survivor bias**: the animals plotted at day 17 are the survivors of a cohort 77% of which was dead |
| **`Wwox`-null (Aqeilan line)** | targeted null | **death at 3–4 weeks**, repeatedly recorded | Aqeilan | LEGEND ledger, multiple entries |
| **`Wwox^gt/gt` hypomorph** | gene-trap; **protein low but DETECTABLE** | **viable, shortened lifespan** | — | LEGEND ledger |
| **`Wwox^P47T/P47T` knock-in** | missense, WW1 PPxY disruption; **protein equal to wild type** | survives to **adult-onset** epilepsy, cerebellar neurodegeneration, ataxia | Aldaz (Hussain 2023) | LEGEND `DL-BIO-085` |
| **`lde/lde` rat** | spontaneous 13 bp deletion, exon 9 | **3–12 weeks** | Suzuki | `CLAIM 037`, full texts read |

**Answer to the brief's question: it is not one thing, and none of the three candidate explanations has been
tested.**
1. **Different alleles/strategies** — the gene-trap hypomorph and the P47T knock-in are *not nulls* and their longer survival is an **allele** effect, the mouse analogue of test (b). They therefore say nothing about background.
2. **Different constructs and drivers even among "nulls"** — LEGEND already records that `CLAIM 036` (EIIA-Cre) and `CLAIM 005` (BK5-Cre) share a floxed allele but are **different knockouts**: *"allele floxed condiviso, knockout diverso."*
3. **Different species** — the rat lives 3–12 weeks against the mouse's 2–3, and `CLAIM 037` records the discordance rather than smoothing it.
4. **Husbandry and ascertainment** — the Aldaz figures are a **perinatal** mortality curve (72 h, day 17) and the Aqeilan figure is a **terminal age** (3–4 weeks). These are not the same measurement, and comparing them directly would be an endpoint error of exactly the kind §3's table already suffers on the human side.

🔴 **Is there any WWOX strain-background effect in the literature at all?** The only one is **oncological and in a
sensitised background**: aged germline `Wwox`-heterozygous mice on the **mammary-susceptible C3H** background
develop mammary tumours at ~50% penetrance. LEGEND already corrected itself on this entry — the source **reports
rather than measures** it, citing an unread primary — and already states the disqualifier: *"Un fenotipo
oncologico in un fondo sensibilizzato **non è** un'affermazione sui portatori di un genotipo neurosviluppo."*

⇒ **No neurodevelopmental strain-background modifier has been looked for, let alone found.** The experiment that
would settle it is stated in §9 and it is the most tractable modifier experiment in the disease.

---

## 6 · Task 4 — Naturally occurring modifiers, and the paralogue question

| Candidate modifier class | Result |
|---|---|
| **A WWOX paralogue or functional backup** | 🔴 **None.** `WWOX paralog` → **1** record, and it is **irrelevant** (PMID 26070663, a translocation-mechanism paper where "paralogous repeats" describes breakpoint junctions and a SIRPG-WWOX fusion is incidental). `WWOX paralog redundancy` → **0**. `WWOX paralog paralogue redundancy compensation homolog family member` → **0**. **WWOX is a single-copy gene with two WW domains and an SDR domain, and no gene has been proposed to substitute for it.** *(Query censuses.)* |
| **Genetic background** | Not tested in any neurodevelopmental WWOX model (§5) |
| **A second variant / oligogenic effect** | ⚪ **One published instance, and it points the wrong way**: in PMID 30949922 one affected sibling additionally carries a *de novo* variant in `RIMS1`. That is a candidate **aggravator in a mild presentation**, not a protective modifier, and it is abstract-level, uncharacterised and n=1 |
| **Sex** | ⚪ Not addressed as a modifier anywhere. ⚠️ LEGEND records that the rat audiogenic-seizure cohort was **female-only**, declared solely in a figure legend — a sex *confound* already logged, not a sex *effect* |
| **Expression modifiers** | 🟡 **The nearest real thing, and it is not about disease severity.** LEGEND holds `rs2548861`, intron 8 of WWOX, a **cis-regulatory element with allele-specific reporter and EMSA activity**, associated with low HDL-C across 9,798 subjects. That is a *quantitative-trait* modifier of WWOX regulation in the general population — **never tested as a modifier of WWOX-deficiency outcome**, and in a biallelic-null context there may be no transcript left for it to modify |
| **Tissue-specific compensation** | ⚪ Not reported |
| **Penetrance modifiers of heterozygous WWOX CNVs** | 🟡 PMID 27569545 describes WWOX deletions/duplications as a *lower-penetrance* ASD locus — incomplete penetrance in the **heterozygous** state. **Not transferable** to biallelic disease |

⇒ **Nothing published changes WWOX-deficiency outcome without touching WWOX.**

---

## 7 · The one thing that survives, and why it matters

**The allele-class rule is real, statistical, and mechanistically unexplained — and the explanation usually assumed
is falsified by LEGEND's own records.**

The intuitive account of test (b) is: *missense ⇒ some protein ⇒ residual function ⇒ longer survival.* But:

- **Q230P is the allele that carries the survival signal** — the longest survivors in Banne 2021 (12 y, 10 y) and the oldest living patient in Oliver 2023 (23 y 11 m) are all homozygous Q230P;
- **and Q230P protein is NOT DETECTED.** `CLAIM 030` records normal transcript and absent protein on Western blot in patient fibroblasts, and `locator_contract_live_test.md` states the consequence in terms: *"the longest-followed survivor carries a missense allele with null-like protein consequence. That is the sharpest single case against reading the genotype classes as a functional gradient."*

So either (i) the abundance measurement is wrong or incommensurable — `CLAIM 030` already flags that the allelic
series mixes **Western blot on fibroblasts** with **immunofluorescence on organoids** and that these are *not
commensurable*; or (ii) a trace of Q230P protein below the blot's floor is functionally decisive; or (iii) the
survival advantage is **not** mediated by WWOX protein at all — which is the only door in this census through which
a genuine modifier could still enter.

🔴 **This is a question, not a finding, and it must not be promoted into one.** It is also the point at which this
node touches Wave 1's result directly: **distinguishing (i) from (ii) requires an absolute quantification of
Q230P protein (targeted MS, `T8` of the Wave 1 census) and a function-per-molecule readout** — neither of which
exists. *"Absent"* and *"below 2% of wild type"* are different molecular diseases, and only the second is
compatible with a residual-function explanation of the survival signal.

---

## 8 · Verbatim locators

| ID | Quotation | Source · section | Surface |
|---|---|---|---|
| **L-1** | *"The patient is a 40-year-old man, the second child of healthy, non-consanguineous parents. There was no family history of any neurodevelopmental disorders or epilepsy."* | PMID 39507621, *Case report* | **`body`** |
| **L-2** ⭐ | *"For many years, the patient was given a diagnosis of cerebral palsy; 38 years after the onset of the disease, he was given a molecular genetic diagnosis of-associated developmental and epileptic encephalopathy."* (italic gene symbol deleted by the extractor before "associated") | PMID 39507621, **abstract** | `abstract` |
| **L-3** | *"Approximately 80 patients with-DEE have been described in the literature, with the oldest being 23 years and 11 months old at date ()."* | PMID 39507621, Discussion | **`body`** |
| **L-4** ⭐ | *"It has been shown that the risk of mortality correlates with thegenotype, with the presence of at least one missense variant increasing the probability of 5-year survival from <50% to >75% ()."* | PMID 39507621, Discussion | **`body`** — ⚠️ the paper **reports** this, citing a reference the extractor emptied; it is not this paper's own measurement |
| **L-5** | *"The phenotype in four patients carrying two predicted null alleles was characterised by (1) little if any psychomotor acquisitions… (3) possible retinal degeneration, acquired microcephaly and premature death. This contrasted with the less severe autosomal recessive spinocerebellar ataxia type 12 phenotype due to hypomorphic alleles. In line with this correlation, the phenotype in two siblings carrying a null allele and a missense mutation was intermediate."* | PMID 25411445, abstract | `abstract` |
| **L-6** | *"A homozygous variant in exon 1 of thegene (hg19, chr16:78133710C>T):c.35C>T was identified, leading to the replacement of an amino acid at position 12 (p.Thr12Met)."* | PMID 39507621, *Exome sequencing* | **`body`** |
| **L-7** | *"Patients with-DEE have a high mortality rate, estimated at approximately 35% ()."* | PMID 39507621, Discussion | **`body`** |
| **L-8** | *"Microcephaly, retinal degeneration, and premature death between 2 and 4 years of age have been observed in severe cases ()."* | PMID 39507621, Introduction | **`body`** — ⚠️ note the hedge *"in severe cases"*; LEGEND already holds a warning that the unhedged version of this sentence is a generalisation that the cohort tables falsify |
| **L-9** | *"Brain computed tomography at the age of 35 years did not show any significant pathological lesions. No magnetic resonance imaging of the brain was performed."* | PMID 39507621, *Clinical features* | **`body`** |
| **L-10** | *"The affected siblings but not the unaffected sibling share a rare deleterious compound heterozygous mutation in WWOX, implicated both in ASD and motor control."* | PMID 30949922, abstract | `abstract` |
| **L-11** | *"another lower-penetrance locus involving inherited deletions and duplications of WWOX"* | PMID 27569545, abstract | `abstract` |

⚠️ **Token discipline on L-9, applied because it is tempting.** A **normal brain CT at 35** in a disease where MRI
anomalies approach 100% looks like a resilience marker. It is not usable as one: **CT is a different and far less
sensitive modality** for myelination and white-matter change, and the paper states plainly that **no MRI was
performed**. Absence of a lesion on CT is not absence of a lesion. **Recorded as a non-finding.**

---

## 9 · What LEGEND already knew, separated from what is new

**Already held — not re-reported as new:**
- 🔴 **The core conclusion of this node.** `locator_contract_live_test.md`: *"Adult survival in this disease tracks **the presence of a missense allele**, not phenotypic mildness"*, already queued as a commit candidate to qualify `CLAIM 017`'s Summary. **This wave corroborates and quantifies it; it did not discover it.**
- `CLAIM 026` and its `BATCH_20260909_001` addition — long survival inside the severe end; *"the largest severity variance in this table is within a genotype rather than between syndromes"*; the full Banne age list.
- `CLAIM 020` / `working_model` row 020 — adult survival with severe disability, 40 years.
- The three restraints in LEGEND's Banne dossier: long survival is not confined to missense; the endpoint column mixes deaths with last examinations; **sibship is not stated**.
- `CLAIM 030` / `CLAIM 033` — Q230P protein not detected; the abundance measurements across the allelic series are not commensurable.
- Every mouse and rat survival figure in §5, including the Aldaz **43% / 72 h, 77% / day 17** and its survivor-bias note; the `gt/gt` hypomorph; `P47T`; `lde/lde`; and that EIIA-Cre and BK5-Cre are different knockouts.
- The C3H heterozygote mammary-tumour entry **and its own self-correction**.
- `rs2548861` as a cis-regulatory WWOX variant associated with HDL-C.
- The Leppa 2016 CNV audit.

**New this wave:**

| # | Finding |
|---|---|
| **N-26** ⭐ | **The allele rule now has a number**: *"the presence of at least one missense variant increasing the probability of 5-year survival from <50% to >75%"* (L-4). LEGEND held the direction; it did not hold the magnitude. ⚠️ Reported, not measured, by this paper. |
| **N-27** ⭐ | **The ascertainment argument is documented in the primary source, not inferred**: 38 years misdiagnosed as cerebral palsy before exome sequencing (L-2), against a literature of ~80 patients whose previous oldest was 23 y 11 m (L-3). The adult cohort is **selected for survival by construction**. |
| **N-28** ⭐ | **The 40-year-old's genotype is homozygous MISSENSE** `c.35C>T p.Thr12Met`, exon 1, outside any known domain (L-6) — so the single most striking outlier in the disease dies at test (b) on its own data. |
| **N-29** | **No discordant sibling pair exists** — `WWOX siblings` → 3 records, all concordant or non-carrier; the Mignot siblings are explicitly concordant (L-5); the Banne pairs have unstated sibship. |
| **N-30** | **WWOX has no paralogue** — `WWOX paralog` → 1 irrelevant record; `WWOX paralog redundancy` → 0. No functional backup has ever been proposed. |
| **N-31** ⭐ | **PMID 30949922 is absent from LEGEND entirely** (0 registry records, 0 receipts): two siblings with biallelic WWOX presenting as **ASD + severe speech sound disorder rather than WOREE**, with an unaffected non-carrier sibling. A genuinely non-DEE presentation of a biallelic genotype. Ascertainment-explained, but **new material**. |
| **N-32** | **The mechanism of the allele rule is falsified by LEGEND's own records** (§7): the survival signal is carried by Q230P, and Q230P protein is not detected. "Missense ⇒ residual protein ⇒ milder" cannot be the explanation. |

---

## 10 · Corrections

| # | Standing text | Correction | Basis |
|---|---|---|---|
| **C-1** 🔴 | **The brief** refers to *"a **21-year-old** patient with multifocal epileptiform activity evolving to a low-voltage background."* | **21 is the follow-up duration, not the age.** LEGEND's record reads: Oliver's *"oldest living patient, **23 y 11 m** — Patient 2, homozygous p.Gln230Pro"*, with *"**21 years of follow-up**"*. Age 23 y 11 m; follow-up 21 y. This is precisely the drift the §12 rule exists to catch, and it matters here because the patient's **genotype** (homozygous Q230P missense) is what decides test (b). | LEGEND `locator_contract_live_test.md` |
| **C-2** ✅ | **The brief** says the adult was *"diagnosed 38 years after onset"*; `PAPER 015` and `CLAIM 020` say *"40 years of observation"* / *"40 years follow-up"*. | **Checked for drift; there is none — the two numbers describe different things and both are correct.** Onset at 4 months, current age 40, genetic diagnosis **38 years after onset** (L-2); title and abstract give **40 years of observation / follow-up**. **Recorded as a passed check**, not a correction, because §12 requires the verification to be visible whether or not it finds an error. | PMID 39507621, read this wave |
| **C-3** ⚠️ | **`CLAIM 017`** ties *"survival into later childhood/adulthood"* to *"milder phenotypes such as SCAR12"*. | **Already flagged by LEGEND as needing qualification, and this wave adds a second independent source.** Both long-lived adults are **full DEE**, not SCAR12 — the 40-year-old is profoundly impaired, ventilator-dependent, non-verbal; Oliver's Patient 2 is *"a full DEE, profoundly impaired and non-ambulant"*. **Survival and mildness are separable axes in this disease**, and `CLAIM 017` conflates them. Not a reversal — the WOREE↔SCAR12 spectrum stands. **Flagged, not edited.** | LEGEND + PMID 39507621 |
| **C-4** ⚠️ | Any use of the Banne survival ages as **survival**. | **The column is `Death/ last date of examination`.** LEGEND's dossier already says so; this file repeats it because §3's table is built on those ages and the distinction changes what O-3, O-4 and O-5 mean. **No age in that table should be cited as a survival time without resolving which it is.** | LEGEND dossier `PMID33916893.md` |
| **C-5** ℹ️ | LEGEND's registry gaps surfaced this wave. | **PMID 30949922 is absent entirely** (0 records). **PMIDs 25411445 (12 registry records) and 27569545 (2 records) carry no read receipt.** All three are relevant to this node. **Flagged for the queue, not created — read-only actor.** | this wave |

---

## 11 · Task 5 — The negative, and the study design that would overturn it

### The negative, stated for the record

**Every apparent resilience outlier in the WWOX literature is explained by allele class, by ascertainment, or by
both. No modifier of WWOX-deficiency outcome has been identified in humans, mice, rats or any other system. No
discordant sibling pair is established. No strain-background effect on a neurological WWOX phenotype has been
tested. WWOX has no paralogue and no proposed functional backup. The one published second-hit is an aggravator in
n=1, not a protector.**

This closes the domain honestly. **The next session should not go looking for a modifier in the published
literature, because it is not there.**

### What would find one — three designs, cheapest first

1. **A records question, not an experiment (cheapest by far).** Go back to the primary reports behind the Banne 2021 rows and resolve two things for the homozygous **R264\*** pair (8 y 11 m / 5 y 2 m) and the **W44\*** pair (7 y / 20 months): **(i) are they siblings?** and **(ii) is each age a death or a censoring?** If any pair is sibs with two genuine deaths, that is **the first discordant sibship in the disease on a null/null genotype** — the one configuration in which the allele explanation cannot apply — and O-4 becomes a real candidate. If not, O-4 and O-5 are dismissed and the negative is complete. **This requires no wet lab, no funding and no new patient.**
2. **The mouse experiment, and it is the most tractable modifier question in the disease.** Take **one** Wwox null allele and backcross it onto **two** defined inbred backgrounds, then measure survival on a **single pre-specified endpoint** with littermate controls and blinded scoring. A reproducible background difference in survival is, by construction, **a mapped modifier waiting to be found** — the cross that produced it is the mapping cross. 🔴 **Nothing published does this**: every survival comparison available today differs in allele, targeting strategy, Cre driver, species or endpoint simultaneously (§5), so no existing pair of numbers can be attributed to background.
3. **The human design, honestly costed.** A modifier search in a biallelic ultra-rare disease needs the one thing this literature does not have: **a cohort with uniform genotype, uniform endpoint definition, and enough null/null patients to compare survivors against non-survivors** — plausibly only achievable through an international WWOX registry with genome-wide data. **Do not attempt it on ~80 published case reports with a mixed `Death/last examination` endpoint**; that dataset cannot support it and would manufacture a false positive.

### And the question §7 leaves open, which is not a modifier question but is the live one

**Why does a missense genotype survive longer when the exemplar missense allele produces no detectable protein?**
Resolving it needs absolute quantification of the mutant protein and a function-per-molecule readout — both of
which the Wave 1 census established do not exist for any WWOX allele. **That is where the two nodes of this session
meet**, and it is a better use of the next session than looking for a modifier that the literature does not
contain.

---

## 12 · Declaration

Author: **Scientist A**. Date: **2026-09-21**. **READ-ONLY** toward every canonical file, registry, ledger and
queue: nothing was edited, no registry record created or amended (C-3, C-5 flagged only), no receipt recorded, no
commit candidate produced, no git operation performed. This file is the single file written.

🔴 **Public edition compliance.** **No e-mail address, no contact detail, no institutional address and no
identifying information of any living person appears in this file.** The patients above are described only by the
clinical and genotypic facts their published reports carry, without names, geography, family identifiers or dates
of birth. *(The publication gate blocked an earlier file of mine this session for a corresponding author's e-mail;
it was right to, and this file is written to that standard from the start.)*

**Not medical advice.** Nothing here is prognostic for any individual. The genotype–survival association in L-4 is
a population-level statistic **reported** by a case report citing another source; it must never be used to predict
an individual course, and an individual on the "favourable" allele class can do badly — **O-6 is exactly that
case, and it is in the table for that reason.**

**Declared limits.** No figure panel inspected. Four of the six external sources were reachable **only at abstract
depth** (25411445, 30949922, 27569545, 26070663), and every statement about them is scoped accordingly. The
tabulated ages in §3 rows O-2 to O-6 are reproduced from **LEGEND's dossiers of papers read by prior sessions**,
not from primaries I read this wave, and are labelled as such. All "zero" statements are **PubMed query censuses on
2026-09-21**, not biological zeros. The `Death/ last date of examination` ambiguity is **unresolved** and is
carried as a limit rather than assumed away in either direction.

*Article metadata and full texts **retrieved from PubMed / PubMed Central**.*

**DOIs** (read from PubMed metadata retrieved this session, except as noted):
[39507621](https://doi.org/10.3389/fgene.2024.1477466) ·
[25411445](https://doi.org/10.1136/jmedgenet-2014-102748) ·
[30949922](https://doi.org/10.1007/s10519-019-09957-8) ·
[27569545](https://doi.org/10.1016/j.ajhg.2016.06.036) ·
[26070663](https://doi.org/10.1101/gr.191247.115) ·
[33916893](https://doi.org/10.1136/jmedgenet-2020-107375) *(Banne 2021 — DOI as recorded in LEGEND; **not** re-verified this wave, and flagged as unverified given this session's pattern of reconstructed identifiers)* ·
[19936220](https://doi.org/10.1128/MCB.00926-09) *(Ludes-Meyers 2009 — DOI as recorded in LEGEND; **not** re-verified this wave, same flag)*.
