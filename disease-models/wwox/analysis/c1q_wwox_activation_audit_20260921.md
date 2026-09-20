# C1q → WWOX activation-state audit — PMID 28123895 (Bandini 2016), `FT-018`

**Actor:** Scientist B · **Date:** 2026-09-20 (file dated 20260921 per task) · **Mode:** READ-ONLY toward every canonical file. No commit candidate. No canonical edit.

---

## 0 · Header — declared read depth

| Field | Value |
|---|---|
| **Declared read depth** | 🔴 **ABSTRACT ONLY — NO FULL TEXT READ.** Not a `FULLTEXT_READ_RECEIPT`-eligible reading. No Results section, no Methods, no figure legend, no statistic, no n was ever on my surface. |
| **Body obtainable?** | **No.** `get_full_text_article` returned `"full_text": ""` on both `["PMC5214935"]` and `["5214935"]`. |
| **Tables obtainable?** | **No** — no body was returned at all, so the question of the extractor stripping tables never arose. |
| **Figures** | **No.** No PDF tooling, no figure images. I did not inspect any panel and make no claim about one. |
| **Gene symbols survived extraction?** | **In the abstract, yes** — `C1q`, `WWOX`, `Her2/neu`, `C3`, `neuT-C1KO` all present and legible. **For the body: untestable**, because the body came back empty rather than stripped. This is *not* the `PMID 41153369` failure mode (symbols silently deleted from delivered text); it is a total absence of delivered text. |
| **Source of every quote below** | The PubMed/PMC **abstract record** for PMID 28123895, retrieved via the PubMed MCP server. Attribution: according to PubMed. [DOI](https://doi.org/10.1080/2162402X.2016.1253653) |

---

## 1 · Identifier verification (done first, independently)

`get_article_metadata(["28123895"])` and `convert_article_ids(["28123895"])` both return, concordantly:

- **PMID** 28123895
- **PMCID** PMC5214935
- **DOI** 10.1080/2162402X.2016.1253653
- **Title:** "The non-inflammatory role of C1q during Her2/neu-driven mammary carcinogenesis"
- **Journal:** *Oncoimmunology* 2016;5(12):e1253653, published 2016-11-08
- **First author:** Bandini, Silvio (Molecular Biotechnology Center, University of Torino). **Last author:** Cavallo, Federica.

✅ Every identifier in the task and in the queue entry is correct.

### 🔴 One queue record is wrong, and it is the acquisition record

`full_text_queue_current.md` `FT-018` states: *"PMCID PMC5214935 (open)."* **PMC does not agree.**

`get_copyright_status(["28123895"])` returns verbatim:

> `"copyright": {"statement": "© 2016 Taylor & Francis Group, LLC", "year": "2016", "holder": "Taylor & Francis Group"}`
> `"license": {"type": null, "url": null, "is_open_access": false}`
> `"source": "pmc"` · `"summary": {"open_access_count": 0}`

The article is **not in the PMC open-access subset**. The acquisition table elsewhere in the same queue file already carries the correct flag for `FT-018` — `idIsNotOpenAccess` · `pdf_only` — so the queue **contradicts itself**, and the `## FT-018` prose entry carries the optimistic half. Recorded here as a finding; **not edited** (read-only).

---

## 2 · Acquisition log — what was tried, what it returned

| Route | Call | Return |
|---|---|---|
| PubMed MCP full text | `get_full_text_article(pmc_ids=["PMC5214935"])` | `"full_text": ""` — abstract field populated, body empty |
| PubMed MCP full text, bare id | `get_full_text_article(pmc_ids=["5214935"])` | `"full_text": ""` — identical |
| PubMed MCP licence | `get_copyright_status(["28123895"])` | `is_open_access: false`, Taylor & Francis |
| Europe PMC REST body | `curl .../europepmc/webservices/rest/PMC5214935/fullTextXML` | `curl: (56) CONNECT tunnel failed, response 403` — egress blocked at the proxy, request never reached EBI |
| PMC article page | `curl https://pmc.ncbi.nlm.nih.gov/articles/PMC5214935/` | `curl: (56) CONNECT tunnel failed, response 403` — same |

**Two independent walls, both permanent on this surface:** (a) a licence/deposit wall — the PMC deposit is closed-access and `pdf_only`, so the MCP extractor has no XML body to return, and would not return one on retry; (b) a network wall — outbound HTTPS to EBI and to PMC is refused by the agent proxy at CONNECT time. Neither is a transient failure and **neither is worth re-testing**. The paper is acquirable only by a route this deployment does not have: a PDF fetched through an authorised channel.

**No snippet, no search result and no secondary description was used as a substitute for the body.** A snippet is not a read.

---

## 3 · Question 1 — What is the actual WWOX result?

🔴 **CANNOT ANSWER. The Results section was never on my surface.** The task required the Results sentence verbatim; there is no Results sentence to quote.

What exists is the **abstract** sentence, quoted verbatim and labelled as abstract, not result:

> "By contrast, a significant higher number of intratumor blood vessels and a decrease in the activation of the tumor suppressor WW domain containing oxidoreductase (WWOX) were observed in tumors from neuT-C1KO as compare with neuT mice."

And the abstract's own conclusion, verbatim:

> "Taken together, our findings suggest that C1q plays a direct role both on halting tumor angiogenesis and on inducing apoptosis in mammary cancer cells by coordinating the signal transduction pathways linked to WWOX, and, furthermore, highlight the role of C1q in mammary tumor immune surveillance regardless of complement system activation."

**"Activation" is not cashed out anywhere on the available surface.** The abstract:

- names **no residue** — not pY33, not pS14, not any other;
- names **no readout** — not phospho-WWOX, not total WWOX, not localisation, not transcript. Note that "activation" in this literature is most often scored by **immunohistochemistry for a phospho-epitope on tumour sections**, which would make it a stained-section intensity measure rather than a blot — but **that is my inference about the field, not a statement this paper makes**, and it is recorded here only so that no later reader mistakes it for a finding;
- gives **no n**, **no statistic**, **no test**, **no effect size**. The word "significant" appears attached to the **blood-vessel count**, and the grammar of that sentence does not unambiguously extend it to the WWOX clause. Whether the WWOX decrease was itself statistically significant **is not determinable from the abstract**.

⚠️ Because the task began from the abstract, and six abstract-versus-results inversions have been found in this corpus in two days, the abstract's "decrease in the activation of WWOX" must be held as an **untested hypothesis about what the body reports**. It has not been checked against the body. It may be a blot, a stain, a single panel, or an inversion. This audit does not know.

---

## 4 · Question 2 — Direction and causality

🔴 **CANNOT DETERMINE, and the one thing the abstract does tell us points to correlation.**

The only manipulation named anywhere on the available surface is a **germline C1q knockout crossed into a neuT background** — "C1q deficient (neuT-C1KO) and C1q competent neuT mice". Verbatim:

> "This study compares carcinogenesis progression in C1q deficient (neuT-C1KO) and C1q competent neuT mice in order to investigate the role of C1q in mammary carcinogenesis."

From this:

- **No add-back is described in the abstract.** No exogenous C1q, no reconstitution, no rescue arm.
- **No second, independent manipulation is described** — no acute depletion, no blocking antibody, no cell-autonomous arm, no WWOX-side manipulation.
- Whether such an arm exists **in the body is unknown**, because the body is unobtainable.
- A germline knockout compared against a genotype-matched control in a **tumour context that the abstract itself says differs in several other ways at once** — vessel density up, Her2/neu membrane expression up, carcinogenesis accelerated, metastasis accelerated — cannot separate "C1q drives WWOX activation" from "tumours that grew faster for any reason show less WWOX activation." The abstract stacks at least four co-varying differences and offers no ordering among them.
- The authors' own verb is hedged: **"our findings suggest"**, and the proposed relation is the loose **"coordinating the signal transduction pathways linked to WWOX"** — not "C1q phosphorylates WWOX", not "C1q is required for WWOX activation".

**On this surface the relation is associative between two genotypes. Nothing establishes direction or causality.**

---

## 5 · Question 3 — Classical cascade or the non-inflammatory arm?

This is the **one question the abstract answers substantively**, and it answers it clearly — though still at abstract level.

> "Surprisingly, this effect was not caused by differences in the tumor-infiltrating cells or in the activation of the complement classical pathway, since neuT-C1KO mice did not display a reduction in C3 fragment deposition at the tumor site."

> "...highlight the role of C1q in mammary tumor immune surveillance **regardless of complement system activation**."

**Reading:** the paper positions its whole effect — the title's "non-inflammatory role" — as running **outside** classical-cascade activation, with unchanged C3 fragment deposition as the negative control that licenses that claim. So the phenotype is **not** attributed to complement activation.

**But the specific question — does the *WWOX* arm run through a C1q receptor on the tumour-cell surface? — is not answered.** The abstract names **no receptor**, no binding partner, and no proximal signalling step between C1q and WWOX. "Coordinating the signal transduction pathways linked to WWOX" is a placeholder, not a mechanism.

### Against LEGEND's existing C1q→WWOX holding, PMID 19484134

**Whether Bandini 2016 cites, corroborates or contradicts Hong 2009 cannot be checked** — that requires the reference list and Discussion, which are in the unobtainable body.

Two things can be established without it:

1. **LEGEND's existing holding is itself not a read.** `paper_registry_current.md` carries PMID 19484134 as **`CORPUS P331`**, `Tier (FASE 1): C`, `Status: screened — corpus placeholder`, `Role: background corpus only`, `Claim links: none — triage only`, `Note: FASE 1 triage 221–400 — no deep-dive performed`. So LEGEND holds C1q→WWOX at **triage depth on both papers**. There is no read-backed C1q→WWOX material in this repository at all. That is a materially different state from the one the `FT-018` framing implies.

2. **The two papers are not the same experiment, and the older one is by far the more mechanistic.** Hong 2009 (Chang lab, PLoS ONE, open access) states in its own abstract, verbatim: *"Exogenous C1q rapidly restored the WOX1 activation (with Tyr33 phosphorylation) in less than 2 hr"* and *"A dominant negative and Y33R mutant of WOX1 blocked the apoptotic effect."* That is **an add-back plus a residue plus a point-mutant epistasis test, in a human prostate cell line, with the readout named (pTyr33)**. Bandini 2016's abstract offers none of those three things — no add-back, no residue, no mutant — and works in an autochthonous mouse tumour.

   **So on abstract-level comparison the specificity runs backwards from the queue's premise:** the *older, already-held, open-access* paper is the one that names the measured quantity; the *new, HIGH-priority, unobtainable* paper does not. If LEGEND wants "WWOX activation state" cashed out into a residue, **PMID 19484134 / PMC2685983 is the open-access target and it has never been read.** (Stated as an acquisition fact, not as a conclusion about its content.)

---

## 6 · Question 4 — Any neural, microglial or synaptic content?

**None detectable. Stated plainly: there is no evidence of any neural, microglial or synaptic content in this paper.**

- The abstract contains **zero** neural, glial, microglial, synaptic, pruning, brain, neuron, epilepsy or CNS terms. The tissues named are mammary tumour and lung (metastasis).
- The author keyword list, verbatim: `C1q`, `Complement`, `ErbB2`, `Her2/neu`, `genetically engineered mice`, `immunosurveillance`, `mammary cancer`. **No neural term.**
- MeSH is not yet assigned on this record; the 2009 comparator's MeSH is likewise entirely oncological.
- The body is unobtainable, so I cannot exclude an incidental sentence — but nothing in title, abstract or keywords suggests one, and it would be extraordinary for a mammary-carcinogenesis paper.

**Consequence, and it is the important one:** any microglial-pruning or neuroinflammation argument attached to this paper is **imported wholesale from other literature**. This paper supplies none of it. The transfer argument therefore rests entirely on C1q biology established elsewhere, and this paper adds **nothing** to that half of it — a point already anticipated in the task framing and here confirmed as far as the surface allows.

---

## 7 · Question 5 — Central or incidental?

**Incidental, on every indicator available without the body.**

- **WWOX is not in the title.** The title's subject is C1q and Her2/neu-driven mammary carcinogenesis.
- **WWOX is not among the seven author keywords.**
- In the abstract, WWOX appears in **1 of 10 sentences**, sharing that sentence with the vessel-count result, and once more in the hedged conclusion.
- The paper's framing is tumour immunology and angiogenesis; WWOX enters as one of several downstream differences observed between two genotypes.
- **Body proportion could not be counted** — no body.

An incidental panel in a tumour-immunology paper carries incidental weight. Nothing here justifies HIGH weight for the WWOX claim even if the body were read and confirmed it.

---

## 8 · VERDICT on the proposition *"C1q is an upstream regulator of WWOX activation state"*

# 🔴 `CANNOT DETERMINE ON THIS SURFACE`

**Grounds:**

1. The Results section, Methods, statistics, n, figure legends and reference list of PMID 28123895 were **never obtainable** — closed-access `pdf_only` PMC deposit plus proxy egress refusal, both permanent here.
2. The abstract, the only surface available, **does not cash "activation" out into any measured quantity** — no residue, no readout, no n, no statistic. The proposition's central term is therefore unmeasured on the record I hold.
3. Even taken at face value, the abstract describes a **single germline-knockout genotype comparison with no add-back and no second manipulation**, against a background of at least four co-varying tumour differences — a design that at best supports an associative statement, not "upstream regulator".

**What would a full read most likely upgrade this to?** On the abstract's own design description, the realistic ceiling is `CORRELATIVE ONLY` — and a clean `CORRELATIVE ONLY` would be a complete result. `SUPPORTED` would require an add-back or an independent manipulation that the abstract gives no sign of.

**`FT-018` should not be closed as read.** It should be re-flagged: `HIGH` priority is not supported by the WWOX content's incidental placement, the "open access" note is factually wrong, and the acquisition route recorded for it does not work. A documented dismissal or a downgrade is the honest discharge; this audit is not one, because it is not a read.

---

## 9 · Direction of effect, and why it may be the wrong way round for WOREE

On the surface available, C1q **loss** is associated with **reduced** WWOX activation — i.e. C1q sits on the side that *increases* whatever WWOX activity is present, and the prior prostate work (PMID 19484134, abstract level) points the same way, with exogenous C1q *restoring* WOX1 activation. If that direction holds, then **removing or blocking C1q would lower WWOX activity, not raise it**, which is the opposite of what a loss-of-function WWOX genotype needs; the intervention direction that this biology would motivate is toward *more* C1q signalling, not less.

That inversion is not a small detail to be corrected later — it reverses the sign of any intervention built on the C1q node, and it applies even in the best case where a full read confirms the abstract. **No therapeutic argument is advanced here and no drug or drug class is named or proposed.** The biology is not established: the verdict above is `CANNOT DETERMINE ON THIS SURFACE`, and a proposition that cannot be determined cannot support an intervention rationale in either direction.

---

## 10 · Contamination note

The repository carries prior LEGEND *inference* about this paper — in the `FT-018` `**Why:**` field and at two points in `literature_tracking_log_current.md` — written **before** anyone read it. That text asserts the activation-state reading, the microglial-pruning link and the druggability point as though established. None of it is read-backed; all of it predates any full-text access, which has never occurred. **No conclusion in this audit rests on that prior text**, and it is quoted nowhere above except to flag the self-contradiction in the queue's own acquisition record (§ 1).

---

*Sources retrieved via the PubMed MCP server. According to PubMed: Bandini S et al., Oncoimmunology 2016;5(12):e1253653, [DOI](https://doi.org/10.1080/2162402X.2016.1253653); Hong Q et al., PLoS One 2009;4(6):e5755, [DOI](https://doi.org/10.1371/journal.pone.0005755).*
