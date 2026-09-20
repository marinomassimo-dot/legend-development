# FT-090 — Citation-fidelity read: `PMID 25416187` (Tabarki 2015) as ref. 14 of `PMID 27551470`

> **Research layer — non-canonical. READ-ONLY toward every canonical file.** No commit candidate,
> no canonical edit, no therapeutic proposal. Not medical advice.

**Actor:** scientist-b · **Date:** 2026-09-21 · **Queue entry:** `FT-090`
**Target:** Tabarki B, Al Mutairi F, Al Hashem A. *The fragile site WWOX gene and the developing
brain.* *Exp Biol Med (Maywood)* 2015;240(3):400–402. PMID `25416187` · PMCID `PMC4935222` ·
DOI [10.1177/1535370214561952](https://doi.org/10.1177/1535370214561952). Deposited 2014-11-21.
**Citing document:** Hazan I, Aqeilan RI, *Cell Death Discov* 2015;1:15040. PMID `27551470` ·
DOI [10.1038/cddiscovery.2015.40](https://doi.org/10.1038/cddiscovery.2015.40).

Source of all retrieved text below: **PubMed / PubMed Central**, via the PubMed MCP
(`get_full_text_article`, `get_copyright_status`, `get_article_metadata`, `search_articles`).

---

## 0 · HEADER — declared read depth, genre, symbol survival

### 0.1 Declared read depth: 🟠 `abstract_only` — **the body was never obtained**

`get_full_text_article(pmc_ids=["PMC4935222"])` returned the record with:

> `"full_text": ""`

`get_copyright_status(pmids=["25416187"])` returned, verbatim:

> `"copyright": {"statement": "© 2014 by the Society for Experimental Biology and Medicine.",`
> `"year": "2014", "holder": "by the Society for Experimental Biology and Medicine"},`
> `"license": {"type": null, "url": null, "is_open_access": false}`
> `… "summary": {"total_checked": 1, "found_in_pubmed": 1, "found_in_pmc": 0, "not_found": 0,`
> `"open_access_count": 0}`

`is_open_access: false`, `found_in_pmc: 0`, no licence type, no licence URL. **This is a permanent
licence wall, not a transient failure and not a retry candidate.** It reproduces exactly what the
earlier surface census already recorded for this PMID in
`full_text_queue_current.md` (`idIsNotOpenAccess` → 🟠 `pdf_only`) — two independent route families
(that census's `oa.fcgi` / `europepmc` / `efetch` probes, and today's MCP) converge on the same
answer. The acquisition routes ruled out in the FT-090 brief (`curl` → `403`, `WebFetch` →
`EGRESS_BLOCKED`) were not re-tested. No PDF tooling and no figure access are available here.

**Therefore the three pages of body text, the reference list, and any table or figure of
`PMID 25416187` were NOT read and are NOT reported on below.** Per
`framework/master/gold_is_in_the_details.md` rule 8 — *"an `abstract_only` event is honest but
clears no reading debt. Un abstract non è una lettura."* — **nothing in this file clears `FT-090`,
and `FT-090` remains ⬜ open.**

What *was* obtained is the PubMed deposit: title, full author-supplied abstract, keywords, MeSH,
publication types, pagination. That is a real, quotable artefact and it is quoted verbatim
throughout — but it is a deposit record, not the article.

### 0.2 Genre verdict: **mini-review (secondary) — self-declared in the deposit**

Established from the deposit's own text, not from the PubMed publication type alone, as `FT-090`
requires. The abstract's **closing sentence is the author's own genre declaration**:

> *"The aim of this review is to summarize the roles of WWOX in the developing brain."*

Corroborating, non-decisive: `article_types: ["Journal Article", "Review"]`; pagination `400-2`
(three pages); keywords `["WWOX gene", "ataxia", "brain", "seizures", "spasticity"]`; MeSH includes
`Animals`, `Mice`, `Rats`, `Disease Models, Animal` — an animal-model spread no three-page human
case report would carry. Metadata and self-declaration **agree**, which is the state this
repository could not reach on the genre cases that previously misled it in both directions.

It is **not** a case report, not a commentary, not a News item. It is a short
review — in *Exp Biol Med*'s house terminology, a minireview.

### 0.3 Gene symbols: 🟢 **survived** — in the channel obtained

`WWOX` occurs **10 times** in the retrieved abstract and once more in the title; `FRA16D` also
survives intact. The italicised-symbol stripping that was verified twice on other papers **did not
occur here**.

⚠️ **Scope of that statement:** it holds for the *title + abstract* channel, which is all that was
retrieved. The body was never returned, so whether symbols would survive body extraction for this
paper is **untested and unknown** — it is not a clean bill of health for the extractor, only an
observation that the channel I actually read was undamaged. Every quote below is therefore one
where the gene identity is explicit in the retrieved string and **not inferred**.

---

## 1 · Question 1 — What kind of paper is it?

Answered in § 0.2: **a three-page mini-review, self-declared**. The decisive quote is the author's
own: *"The aim of this review is to summarize the roles of WWOX in the developing brain."*

The genre matters to FT-090 for one reason only, and it is a strong one: `27551470` cites this
document **for a fact**. A self-declared summary of other people's work cannot be the terminal
holder of that fact (see § 4).

---

## 2 · Question 2 — What it reports about germline WWOX mutations / loss of function

🔴 **All quotable material is from the abstract. Every sentence of the abstract bearing on germline
mutation, loss of function, or the neurological phenotype is reproduced below in full and in order.
Nothing bearing on the question is omitted.**

> (1) *"WWOX was cloned as a tumor suppressor gene mapping to chromosomal fragile site FRA16D."*

> (2) *"Loss of WWOX is closely related to tumorigenesis, cancer progression, and therapy
> resistance."*

> (3) *"Recent studies demonstrate the growing role of WWOX gene in other human pathologies such as
> metabolic and nervous system-related conditions."*

> (4) *"The neurologic phenotype of WWOX mutation includes seizures, ataxia, developmental delay,
> and spasticity of variable severity."*

> (5) *"WWOX is a ubiquitous protein with high expression in many tissues including brain,
> cerebellum, brain stem, and spinal cord."*

> (6) *"WWOX is highly expressed in different brain regions during murine fetal development and
> remained unchanged in the cortex and the corpus callosum in adult mice."*

> (7) *"The mechanism or the putative role of WWOX in the nervous system is still unclear but may
> include abnormal signaling protein, disruption of neuronal pathways, neuronal differentiation,
> mitochondrial dysfunction, or apoptosis."*

> (8) *"Homozygous mutations affecting WWOX in humans are likely to be more described in the future
> using exome sequencing."*

> (9) *"The described findings highlight that WWOX plays a critical role in normal central nervous
> system development and disease."*

### What the quotes do and do not contain

| Asked by `FT-090` | Answer at the depth obtained |
|---|---|
| Patients? | **None reported in the abstract.** No cohort, no family, no case. |
| n? | **Absent.** No number of any kind appears in the abstract. |
| Which variants? | **None named.** No cDNA, protein, exon or deletion coordinate appears. |
| Which phenotype — WOREE, SCAR12, epilepsy, ataxia? | **No syndrome name is used.** Not "WOREE", not "SCAR12", not "epileptic encephalopathy". Only a *symptom list*, quote (4): *"seizures, ataxia, developmental delay, and spasticity of variable severity."* The phrase *"of variable severity"* is the abstract's only gesture at a spectrum; it does not partition it. |
| Any primary observation? | **None visible.** No method, no sequencing performed, no measurement made, no animal experiment of the authors' own. Quotes (5)–(6) restate expression findings in *mice*; quote (7) offers an explicitly unresolved mechanism list. |
| Is it restating others? | **Yes, by its own account** — quote (3) *"Recent studies demonstrate…"*, quote (9) *"The described findings…"*, and the genre declaration in § 0.2. |

### Two features of the wording that bear directly on § 3

**(a) The abstract keeps "loss of function" and "mutation" on separate arms.** The only occurrence
of loss is quote (2), *"Loss of WWOX is closely related to tumorigenesis, cancer progression, and
therapy resistance"* — the **cancer** arm. The **neurological** arm is stated in terms of
*mutation*: quote (4) *"the neurologic phenotype of WWOX mutation"*, quote (8) *"Homozygous
mutations affecting WWOX in humans"*. The abstract never writes "loss of function" of WWOX into a
neuronal sentence.

**(b) The word "germline" does not occur anywhere in the retrieved text.** The closest term is
*"Homozygous"* in quote (8) — a zygosity, which in humans implies a constitutional/inherited allele
but is a narrower and different assertion than "germline", and specifically a **biallelic**
assertion. No heterozygous human neurological claim appears.

---

## 3 · Question 3 — Does it support the proposition `27551470` draws from it?

### 3.1 The proposition, in the citing document's own words

From this repository's completed read of `PMID 27551470`
(`disease-models/wwox/research/fulltext_dossiers/PMID27551470.md`, § 2.4), the passage carrying
ref. 14 reads:

> *"cancer usually occurs after the reproductive phase and therefore loss of CFS would not have an
> inherited selective pressure. **In support of this assumption**, germline mutations or loss of
> function of WWOX are associated with neuronal disorders"*

**Proposition P (the part ref. 14 is made to carry):** *germline mutations **or loss of function**
of WWOX are associated with neuronal disorders.*

**Rhetorical use R:** P is offered **"in support of"** the premise that loss of a common fragile
site carries no inherited selective pressure.

### 3.2 🔴 VERDICT

# `CANNOT DETERMINE`

**This is a depth verdict, not a fidelity judgement.** The body of `PMID 25416187` sits behind a
permanent licence wall (§ 0.1) and was not read. Under `gold_is_in_the_details.md` rule 8 an
abstract clears no reading debt, so an abstract cannot license `SUPPORTS AS CITED`,
`SUPPORTS A NARROWER CLAIM` or `DOES NOT SUPPORT` either. **The single citation holding up
`27551470`'s entire connection to the reference genotype cannot be checked in this deployment.**

That is itself the finding FT-090 asked for, and it should be recorded as a state, not as a
pending task: the routes are exhausted, not untried.

### 3.3 Direction of travel at abstract depth — ⚠️ NOT PROMOTABLE, recorded for the next reader

Offered only so a future reader with the PDF knows what to test. **This is not the verdict and must
not be cited as one.**

- **The factual core of P is asserted by the source's own abstract.** Quote (4) —
  *"The neurologic phenotype of WWOX mutation includes seizures, ataxia, developmental delay, and
  spasticity of variable severity"* — and quote (9) are a direct, unhedged association between WWOX
  mutation and neurological disease. At abstract depth this citation **points where it claims to
  point**. That is worth saying plainly in a repository that has found four bad citations in two
  days: **this one shows no sign of being a fifth.**
- **Two candidate narrowings to test against the body.**
  **(N1) the disjunction.** P says *"germline mutations **or loss of function**"*. The abstract
  assigns *loss* to cancer (quote 2) and *mutation* to the nervous system (quotes 4, 8); P fuses two
  arms the source keeps apart. **(N2) zygosity.** The abstract's human-genetic statement is
  *"**Homozygous** mutations affecting WWOX in humans"* (quote 8) — biallelic — whereas P says
  "germline", which reads as covering heterozygous carriers. Both narrowings, if the body confirms
  them, would move the verdict toward `SUPPORTS A NARROWER CLAIM`, not toward `DOES NOT SUPPORT`.
- **The inversion recorded in § 2.4 of the `27551470` dossier is untouched by this reading and
  needs no source.** Whether Tabarki says P narrowly or broadly, R remains self-defeating: a
  germline, pre-reproductive, biallelic-lethal neurological phenotype — quote (4)'s seizures and
  spasticity — *is* inherited selective pressure. **The stronger this source turns out to be, the
  worse it is for the argument it was cited to support.** The defect is `27551470`'s, not
  Tabarki's, and reading Tabarki cannot repair it.

---

## 4 · Question 4 — Primary or secondary? Does the chain bottom out?

**Secondary, self-declared** (§ 0.2), and **the chain does not bottom out here — it recedes at
least one hop, and I cannot see where it lands.**

Two independent indications, both from retrieved text:

1. **The document says so.** *"The aim of this review is to summarize the roles of WWOX in the
   developing brain"*; *"Recent studies demonstrate…"*; *"The described findings…"*. It reports no
   patient, no n, no variant, no experiment of its own (§ 2).
2. **Chronology rules out the authors' own series as its basis.** The same first author later
   published a primary case series — Tabarki B, AlHashem A, AlShahwan S, Alkuraya FS, Gedela S,
   Zuccoli G, *Severe CNS involvement in WWOX mutations: Description of five new cases*,
   *Am J Med Genet A* 2015;167A(12):3209–13, PMID `26345274`,
   DOI [10.1002/ajmg.a.37363](https://doi.org/10.1002/ajmg.a.37363),
   `article_types: ["Case Reports", "Journal Article"]`. Its publication date is **2015-09-08**;
   the review under audit was deposited **2014-11-21**, roughly ten months *earlier*. **The review
   therefore cannot rest on its own group's series**, and its quote (8) —
   *"Homozygous mutations affecting WWOX in humans are likely to be **more described in the
   future**"* — is the abstract stating in its own words that the human primary literature it
   summarises was, at the time of writing, thin and not yet its own.

**What this means for `27551470`.** The chain as far as it can be traced here is:
`27551470` (editorial-style review, 2015) → ref. 14 `25416187` (mini-review, 2014) → *unidentified
primary reports by other groups, 2014*. **The reference list of `25416187` is inside the walled
body and could not be read**, so the third hop cannot be named — I will not guess which 2014
primaries they are.

**Two review hops before any measurement, with the terminal primary unnamed, is the finding.**
`27551470`'s only sentence reaching the reference genotype is at minimum two removes from a patient,
and this repository holds no receipt for either intervening hop.

---

## 5 · Question 5 — Anything usable in its own right?

**From `PMID 25416187` itself: essentially nothing new, and nothing promotable.** At abstract depth
it offers no variant, no n, no natural-history datum, no endpoint. Quotes (5)–(7) are the only
substantive content:

- **Expression** — quote (5): *"WWOX is a ubiquitous protein with high expression in many tissues
  including brain, cerebellum, brain stem, and spinal cord."* Note it lists **cerebellum** among
  high-expression tissues; that is an expression statement, carrying no motor or anatomic
  phenotype claim, and it does **not** bear on `CLAIM 039`, whose subject is the rat `lde/lde`
  cerebellum's *histology*.
- **Developmental time-course** — quote (6): *"WWOX is highly expressed in different brain regions
  during murine fetal development and remained unchanged in the cortex and the corpus callosum in
  adult mice."* A murine restatement, unattributed in the abstract; source untraceable without the
  body.
- **Mechanism** — quote (7) is an explicit five-item *"still unclear"* list
  (*"abnormal signaling protein, disruption of neuronal pathways, neuronal differentiation,
  mitochondrial dysfunction, or apoptosis"*). It is a menu of hypotheses, not a finding, and the
  hedge *"is still unclear"* is the author's own.

**One incidental lead, from a different paper, flagged not banked.** While establishing the
chronology in § 4 I retrieved the abstract of `PMID 26345274`, which is **already queued as
`FT-032`, recorded `absent` in `surface_census.md`, and unread**. Its abstract contains a human
neuroimaging statement that a targeted grep shows this repository does **not** currently hold in
any registry:

> *"We suggest that neuroimaging in these patients reveals a characteristic pattern of
> neurodegeneration in which the cerebellum is spared that could help with early diagnosis in the
> appropriate clinical setting."*

It also states a homozygous splice-acceptor allele `NM_016373.3:c.606-1G>A` in five patients from
two families, *"All five patients died before their third birthday"*, and *"Retinopathy was
observed in two patients"*. The `c.606-1G>A` allele **is** already held
(`paper_registry_current.md` line ~6398, via another paper); the *"cerebellum is spared"* human
imaging statement is **not**.

⚠️ **This is abstract-depth material on a paper I was not assigned and did not read.** Under rule 8
it clears nothing and is promotable by no route. It is recorded here solely as a reason to raise
`FT-032`'s priority: a human "cerebellum is spared" claim sits adjacent to `CLAIM 039`'s unresolved
anatomical question (*"L'atassia non ha spiegazione strutturale in questo paper"*), and
`26345274` — unlike `25416187` — is a primary case series.

---

## 6 · What should happen to `27551470`'s dependent sentence — **text only, not an edit**

The verdict is not `SUPPORTS AS CITED`, so this section is required. **Nothing below is an
instruction to modify any file; no canonical file was touched by this reading, and no commit
candidate is created.**

Because the verdict is `CANNOT DETERMINE` **for reasons of access rather than of fidelity**, the
correct disposition is *annotation of status*, not retraction. What a future integrator should
consider, and in this order:

1. **The dependent sentence of `27551470` should carry an explicit unverified-support marker,** not
   a defect marker. This repository can now state that its sole support is a **three-page
   self-declared mini-review whose body is behind a permanent licence wall in this deployment**, and
   that the fidelity test was attempted and could not be completed. Recording it as a *bad* citation
   would be as unfaithful as the failures this laboratory has been cataloguing — the abstract-depth
   evidence in § 3.3 points, if anything, the other way.
2. **`FT-090` should stay ⬜ open and be re-tiered from "unread" to `pdf_only ·
   routes_exhausted`.** The distinction matters operationally: it is not awaiting effort, it is
   awaiting a *different acquisition channel* (publisher PDF, institutional access, author contact,
   ILL). Leaving it as ordinary reading debt will make some future session re-run routes that are
   already known to fail — this reading re-ran them once already.
3. **The evidential weight assigned to `27551470`'s reference-genotype sentence should be lowered
   on grounds that do not depend on FT-090 at all** — namely § 4: two review hops with the terminal
   primary unnamed. That finding is fully established by this reading and needs no further access.
4. **The § 2.4 inversion stands and is independent of all of the above.** No outcome of a future
   full read of `25416187` can repair it, because it is a defect in `27551470`'s own two consecutive
   sentences. It should not be left waiting on `FT-090`.

---

## 7 · What could not be obtained

| Item | State |
|---|---|
| Body text of `PMID 25416187` (pp. 400–402) | 🔴 **Permanently walled in this deployment.** `full_text: ""`, `is_open_access: false`, `found_in_pmc: 0`. Not a retry. |
| Reference list of `PMID 25416187` | 🔴 Not obtained — inside the walled body. Terminal primary therefore unnamed. |
| Any table or figure | 🔴 No PDF tooling, no figure-image access. **No panel or table was inspected and none is claimed.** |
| Whether symbols survive *body* extraction for this paper | ⚠️ Untested — there is no body to test. |
| `curl` / `WebFetch` routes | Not re-tested; ruled out in the `FT-090` brief (`403` / `EGRESS_BLOCKED`). |

**No `FULLTEXT_READ_RECEIPT` is produced by this reading, and none may be:** no full text was read.
This file is an `abstract_only` record and clears no reading debt.
