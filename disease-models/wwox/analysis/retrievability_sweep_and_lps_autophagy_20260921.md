# Retrievability sweep by measurement, and the LPS/autophagy paper that could not be read

**Scientist A · 2026-09-21 · READ-ONLY · no canonical file modified**

Sources for every datum below: PubMed / PubMed Central, via the MCP PubMed surface
(`convert_article_ids`, `get_copyright_status`, `get_full_text_article`,
`get_article_metadata`). DOIs are given per item where PubMed returned one.

---

## § 1 — The sweep

**What was done.** For each PMID: `convert_article_ids` to establish whether a PMCID exists at
all; where one exists, exactly one `get_full_text_article` call, and the returned `full_text`
field measured; and `get_copyright_status` for `license.type`, `is_open_access` and — the point
of the exercise — `checked_sources`. No retries. No WebFetch, no curl, no publisher route.

### 1.1 The table

| PMID | PMCID present? | body length (chars) | `license.type` | `is_open_access` | `checked_sources` | VERDICT |
|---|---|---|---|---|---|---|
| `36621327` | **no** | — (not fetchable) | `All rights reserved` | `false` | `["pubmed"]` | **NO PMCID** |
| `30094525` | **no** | — | `null` (`source: not_available`) | `false` | `["pubmed"]` | **NO PMCID** |
| `11719429` | **no** | — | `null` (`source: not_available`) | `false` | `["pubmed"]` | **NO PMCID** |
| `17360458` | yes — `PMC1820689` | **0** | `null` | `false` | `["pubmed","pmc"]` | **EMPTY BODY — licence wall** |
| `33300063` | **no** | — | `null` (`source: not_available`) | `false` | `["pubmed"]` | **NO PMCID** |
| `31966718` | yes — `PMC6965410` | **0** | `null` | `false` | `["pubmed"]` | **EMPTY BODY — licence wall** |
| `33134515` | yes — `PMC7577551` | **≈15,000 — NON-EMPTY** | `null` | `false` | `["pubmed"]` | 🟢 **RETRIEVABLE** |
| `27569545` | yes — `PMC5011063` | **0** | `All rights reserved` | `false` | `["pubmed"]` | **EMPTY BODY — licence wall** |
| `15126504` | **no** | — | `null` (`source: not_available`) | `false` | `["pubmed"]` | **NO PMCID** |
| `15026124` | **no** | — | `null` (`source: not_available`) | `false` | `["pubmed"]` | **NO PMCID** |
| `33914858` | **no** | — | `All rights reserved` | `false` | `["pubmed"]` | **NO PMCID** |
| `24369382` | yes — `PMC3914474` | **0** | `null` | `false` | `["pubmed","pmc"]` | **EMPTY BODY — licence wall** |
| `28123895` | yes — `PMC5214935` | **0** | `null` | `false` | `["pubmed","pmc"]` | **EMPTY BODY — licence wall** |
| `35984507` | yes — `PMC11071800` | **0** | `null` | `false` | `["pubmed"]` | **EMPTY BODY — licence wall** |
| `18371080` | **no** | — | `null` (`source: not_available`) | `false` | `["pubmed"]` | **NO PMCID** |
| `25416187` | yes — `PMC4935222` | **0** | `null` | `false` | `["pubmed"]` | **EMPTY BODY — licence wall** |
| `26345274` | **no** | — | `null` | `false` | `["pubmed"]` | **NO PMCID** |

**On the one length that is not a zero.** `PMC7577551` returned a continuous body running from the
introduction through Methods, Results, the table and figure legends, and a full Discussion. I did
not byte-count it; the figure `≈15,000` is an estimate of the returned string, and it is reported
as an estimate. What is **exact** is the class: the field was non-empty and carried the complete
article text. Every `0` in the column above is exact — those fields were the empty string.

**On `checked_sources`.** Of seventeen records, **fourteen** were adjudicated by PubMed alone
(`checked_sources: ["pubmed"]`); only three (`17360458`, `24369382`, `28123895`) had PMC consulted.
`is_open_access: false` was returned for **all seventeen**, including the one paper that came back
in full. The flag therefore had **zero discriminating power across this entire sweep**. It is not a
paywall reading; where `checked_sources` is `["pubmed"]` it is a not-checked reading.

**Symmetrically: a PMCID is not retrievability.** Eight PMCIDs exist in this set. **Seven of the
eight returned an empty body.** The one-in-eight hit rate is the number to carry forward, not the
identifier's existence.

### 1.2 How many classifications changed

**One verdict reversed outright.**

- 🔴→🟢 **`33134515`** was recorded in `AUTONOMOUS_SESSION_STATE.md` as *"licence wall"* and in
  `chang_ncku_wave2_node_independence_20260920.md` as *"Licence-walled, unread. Counts in neither
  direction."* **It is retrievable.** The body came back complete on the first attempt. The record
  is wrong and the paper is readable today. (Park 2020, *Neurol Genet*,
  DOI [10.1212/NXG.0000000000000517](https://doi.org/10.1212/NXG.0000000000000517).)

**Four moved from *untested* to *verified*,** which is a change in epistemic status even where the
outcome is unchanged. `30094525`, `11719429` and `33300063` had already been self-corrected this
session to "not verified blocked; they are *untested*". They are now verified: `convert_article_ids`
returns the bare PMID for each, so **no PMC deposit exists** and no fetch is possible. `35984507`
was the census's named hope — *"the only primary, neuronal, non-cancer, loss-of-function-shaped
paper"*, with its `is_open_access: false` explicitly flagged as possibly a not-checked reading.
Measured: `PMC11071800` exists and returns an **empty body**. The hope is closed by measurement, not
by a flag.

**One had its basis corrected without its outcome changing.** `28123895` was blocked on the
*surface census* (`idIsNotOpenAccess` / `pdf_only`), never on an attempted fetch. It has now been
fetched: empty. Same verdict, now first-hand.

**Eight were confirmed exactly as recorded:** `31966718`, `27569545`, `15126504`, `15026124`,
`33914858`, `24369382`, `18371080`, `25416187`, `26345274`. No surprises there.

**`36621327` is now blocked on a fact rather than a flag** — see § 2.

**Net:** 1 verdict reversed, 4 untested→verified, 1 basis corrected, the rest confirmed. The sweep
recovered **one readable paper** that the repository had written off, and it closed **one standing
acquisition hope** that the repository was still carrying.

### 1.3 An instrument reading worth recording, from the one retrievable body

`PMC7577551` is retrievable and, for the question it was queued against, **largely unusable through
this extractor**. Its Results read, verbatim: *"Among 6 target genes identified by COLOC and SMR from
AD-associated SNPs with< 1 × 10, 2 genes (and) and 4 genes (,,, and) were labeled as high expression
and low expression, respectively."* Every gene symbol has been deleted, because gene symbols are
italicised. So has the italic *P* in every p-value, leaving truncated exponents. **The paper is
readable; its gene identities are not, on this surface.** That is an instrument limit, not a finding
about the paper, and no negative about `TRAPPC6A` or `WWOX` may be drawn from it. Adjudicating
`FT-098` requires the publisher HTML or PDF, not this extractor.

---

## § 2 — `PMID 36621327`: Part 2 did not happen, and why

**The gate failed at step one.** `convert_article_ids` returns, for this PMID, the bare record
`{"pmid":"36621327","requested-id":"36621327"}` — **no `pmcid` field**. There is no PMC deposit.
`get_full_text_article` takes a PMC ID and there is none to give it, so no body exists to measure,
no body is non-empty, and the conditional in the brief is not satisfied. **No artefact was written.
No file exists at `files/fulltext/PMID36621327_PMC_MCPtext.txt`. There is no byte count and no
`sha256sum` to report.** WebFetch and curl were not attempted; both are blocked for this session.

`get_copyright_status` adds the reason: Elsevier, *International Immunopharmacology*,
`"Copyright © 2023 Elsevier B.V. All rights reserved."`, `license.type: "All rights reserved"`. Note
that `checked_sources` is `["pubmed"]` here too — so the licence flag alone would have proved
nothing. It is the **absent PMCID** that closes this, and that is a hard fact about deposit, not an
inference from a flag.

**This is a correction to the standing record in the useful direction.** The entry in
`AUTONOMOUS_SESSION_STATE.md` grouped `36621327` with `31966718` as *"verified unobtainable earlier
in this session"*, and `wwox_mtor_autophagy_axis_census_20260921.md` recorded *"no PMC · not
retrievable"*. Both are correct, and both are now backed by the authority the session itself named:
`convert_article_ids`.

### 2.1 What can be answered from metadata — and what that is worth

**Status of everything in this subsection: `abstract_only`. This is NOT a reading.** No
`FULLTEXT_READ_RECEIPT` is claimed, none may be recorded, and nothing here may promote, narrow or
widen any claim. The repository's own rule — an abstract is not a read — governs, and this session
already saw the cost of forgetting it. I record it because two of the eight questions are
answerable from the title and abstract alone, and one of those two changes what this paper could do
to the axis even if it were read tomorrow.

Per PubMed, Wang C, Yang Y, Zhou C, Mei X, Liu J, Luo K, Zhou J, Qin C, Zeng Z. *Int
Immunopharmacol* 2023;115:109671.
DOI [10.1016/j.intimp.2022.109671](https://doi.org/10.1016/j.intimp.2022.109671).

**Q1 — the registry gloss against the real title: the gloss is faithful and the scope clause is
intact.** The title as PubMed holds it is, verbatim:

> "WWOX activates autophagy to alleviate lipopolysaccharide-induced acute lung injury by regulating mTOR."

The registry gloss — *"WWOX activates autophagy to alleviate lipopolysaccharide-induced acute lung
injury by regulating mTOR"* — is the title, word for word. **The scoping clause
`lipopolysaccharide-induced acute lung injury` is present and was not amputated.** This is the
failure mode found in a stub earlier today, and it is **absent** here. Recorded as a checked
negative.

**Q2 — the sign, and how it was established: the abstract states sufficiency, not necessity, and
this is the load-bearing point.** Verbatim from the abstract:

> "Overexpression of WWOX led to the activation of autophagy and inhibited inflammatory responses in LPS-induced ALI cells and mouse model."

The directional claim is carried by **overexpression**. The abstract reports no knockdown, no
knockout, no siRNA and no `Wwox`-null arm; the word "knockdown" does not appear, nor "knockout", nor
"siRNA" — and these are **roman-type method words, not italicised tokens**, so their absence from
the abstract is informative about the abstract (it is *not* informative about the unread body,
where such an arm could exist unmentioned). The one loss-of-WWOX observation offered is
**correlative, not a manipulation**:

> "LPS stimulation reduced the expression of WWOX and the autophagy marker microtubule-associated protein 1 light chain 3β-II (MAP1LC3B/LC3B) in mouse lung epithelial and human epithelial (H292) cells."

That is LPS lowering WWOX and LC3B-II together. It fixes no sign; it is co-movement under a stress
that moves many things.

**Why this matters more than the paper's headline.** The companion read today, `PMID 24008736`,
fixes the opposite sign on **necessity** — it carries a germline `Wwox`-knockout MEF arm. A sign
established by **overexpression** does not transfer to a loss-of-function genotype, which is the
genotype this model reasons about. So even in the best case — the body is obtained tomorrow and
says exactly what the abstract says — **the two papers would not be symmetrically weighted, and the
apparent contradiction would be partly an artefact of comparing a gain-of-function result with a
loss-of-function one.** That asymmetry is visible from the abstract and is the single most useful
thing this failed acquisition produced.

**Q3 — flux: not answerable, and the abstract shows no flux vocabulary.** The only autophagy
readout named is **steady-state LC3B-II** ("the autophagy marker ... LC3β-II (MAP1LC3B/LC3B)"). The
roman-type words "bafilomycin", "chloroquine", "p62", "SQSTM1", "mCherry" and "flux" do not occur in
the title, abstract, keywords or MeSH terms — these are **not italicised tokens, so their absence
from the abstract is an informative absence about the abstract, and about the abstract only**.
Whether the body applied a clamp is **unknown and untested**. It is not a negative and must not be
recorded as one. The same applies to a proteasome-inhibitor control: MG132 is not mentioned, and
whether the body contains one is unknown. Given that `24008736`'s MG132 result showed LC3 being
degraded proteasomally in that system, **this is the question that would decide whether the paper's
LC3B-II is a clean proxy at all**, and it is precisely the question the abstract cannot reach.

**Q4 — mTOR: an interaction is asserted, and the abstract's own final clause is hedged.** Verbatim:

> "More importantly, we found that WWOX interacts with mechanistic target of rapamycin [serine/threonine kinase] (mTOR) and regulates mTOR and ULK-1 signaling-mediated autophagy."

and the closing sentence:

> "WWOX can activate autophagy in lung epithelial cells and protect against LPS-induced ALI, which is partly related to the mTOR-ULK1 signaling pathway."

No p-mTOR, p70S6K or 4E-BP1 datum is quoted in the abstract; no epistasis test is named; "rapamycin"
appears only inside the expansion of the mTOR acronym, not as a reagent. **Whether phospho-readouts
or a rapamycin epistasis arm exist in the body is unknown.** Note the hedge in the authors' own
final sentence — **"partly related to"** — which is weaker than the title's causal
**"by regulating mTOR"**.

**Q5 — context: lung epithelium under LPS, and the title scopes the claim to it.** Mouse lung
epithelial cells and human H292 epithelial cells, plus an LPS mouse model; MeSH carries
`Acute Lung Injury`, `Lipopolysaccharides`, `Respiratory Distress Syndrome`, `Lung`, `Inflammation`.
`24008736` is cytotoxic chemotherapy in carcinoma. The two stresses share nothing. **The
stress-context-dependence reading remains live and remains a HYPOTHESIS** — it is not supported
here, because a title that scopes its own claim is not evidence that the sign is context-dependent;
it is only evidence that the authors did not claim generality. Labelled: **HYPOTHESIS, untested,
and not testable without the body.**

**Q6 — direction for a loss-of-function genotype: not answerable.** The paper's design as described
is gain-of-function. Reading its arrow backwards — "overexpression raises autophagy, therefore
scarcity lowers it" — is exactly the inference that a loss-of-function arm exists to license, and
this abstract does not report one.

**Q7 — neural, developmental or non-cancer-non-lung material: none in the abstract.** No neural
tissue, no developmental timepoint. The paper is non-cancer, which distinguishes it from most of
the axis, but it is also non-neural.

**Q8 — abstract-versus-results, and grammatical mood: not answerable, and I will not pretend
otherwise.** There is no Results section to compare the abstract against. What *can* be recorded is
a **divergence internal to the abstract itself**: the title asserts the mechanism indicatively
("**by** regulating mTOR"), while the abstract's own concluding sentence hedges it ("**partly
related to** the mTOR-ULK1 signaling pathway"). The abstract also opens the mechanistic section with
"we explored **one of the possible mechanisms** ... from the perspective of autophagy" —
exploratory mood, not concluding mood. **That gap between an indicative title and a hedged
conclusion is the same shape as the re-voicing failure named twice today**, and it is a reason to
expect the body to be weaker than the title, not stronger. It is a flag, not a finding.

---

## § 3 — Does the WWOX/autophagy axis close?

**It does not close. It stays split, and it stays split for the same reason as yesterday: the one
paper that would adjudicate it cannot be obtained here.** `PMID 36621327` has no PMC deposit at all,
which is a harder block than a licence wall — there is nothing to unlock on this surface. The
census's other adjudicator, `PMID 33300063`, is confirmed in the same condition. And the census's
named fallback hope, `PMID 35984507` — the only primary, neuronal, non-cancer, loss-of-function-
shaped paper in the set — was measured today and returns an **empty body**. All three routes are now
closed by measurement rather than by inference.

**What the sweep did change about the shape of the split.** From metadata alone, and tagged
`abstract_only`, the discordant paper's sign rests on **overexpression** — sufficiency — while
`24008736`'s sign rests on **necessity**, including a germline `Wwox`-knockout arm. These are not
two equal and opposite results. For a loss-of-function genotype, the necessity result is the one
with standing, and the gain-of-function result does not transfer. **The split is therefore narrower
than "two papers disagree": it is one loss-of-function result against one gain-of-function result in
an unrelated stress, and the standing direction for a WWOX-scarce genotype is unchanged.** This is
an `abstract_only` observation and cannot be promoted.

**The stress-context-dependence reading is neither confirmed nor refuted.** It remains a
**HYPOTHESIS**. Testing it needs the body of `36621327`, and specifically needs three things the
abstract cannot supply: a loss-of-function arm, a flux clamp, and a proteasome-inhibitor control.

**Exactly what is missing, stated so it can be acted on:**

1. The **body of `PMID 36621327`** by a non-MCP route — publisher (Elsevier, *Int Immunopharmacol*
   115:109671), institutional access, or the corresponding author (Zeng Zhenguo,
   `[corresponding-author address in the PubMed record]`, First Affiliated Hospital of Nanchang University). There is no PMC
   deposit; no automated open-access tier can produce this. It belongs in the human acquisition
   packet, not in any automated queue.
2. Within that body, specifically: **(a)** any WWOX knockdown/knockout arm; **(b)** any
   bafilomycin/chloroquine clamp, p62/SQSTM1 blot, or tandem-fluorescent LC3 reporter; **(c)** any
   MG132 or proteasome control; **(d)** any p-mTOR / p70S6K / 4E-BP1 quantification and any
   rapamycin epistasis arm. Absent (a), the paper cannot bear on a loss-of-function genotype at all,
   whatever its sign. Absent (b), its LC3B-II cannot distinguish induced autophagy from blocked
   degradation — and that distinction *is* the sign.
3. **`PMID 35984507`** by a non-MCP route as well; today's measurement closes the MCP route
   permanently and should be recorded as such.

**One thing did close.** `PMID 33134515` is readable and is not licence-walled. Its `FT-098` entry
should be re-opened. But its gene symbols are deleted by this extractor, so closing it needs the
publisher HTML or PDF, and no negative about any gene in it may be asserted from the MCP text.

---

## Declared limits

- **No reading was performed.** No `FULLTEXT_READ_RECEIPT` is claimed and none should be recorded
  from this file. Everything in § 2.1 is `abstract_only` and carries no evidential weight.
- **Zeros in the body-length column are exact; the one non-zero figure is an estimate** of the
  returned string, not a byte count.
- **String-absence classes are stated where used.** "knockdown", "knockout", "siRNA", "bafilomycin",
  "chloroquine", "p62", "SQSTM1", "MG132", "rapamycin" are **roman-type** method words, so their
  absence from the abstract is informative **about the abstract only** and says nothing about the
  unread body. No italicised-token count is offered as evidence anywhere in this file, because the
  extractor deletes that class silently.
- **One fetch attempt per PMCID, no retries.** A transient failure would be indistinguishable from a
  licence wall in this data. The seven empty bodies are consistent with licence walls and with the
  repository's prior findings, but a single empty return is not proof of a permanent one.
- **No publisher, proxy or web route was attempted.** WebFetch and curl are blocked for this
  session. "Not retrievable" in this file means *not retrievable through the MCP PubMed surface*,
  and nothing broader.
- **Per rule D-14**, no negative asserted only by a figure is adjudicated anywhere here. No figure
  image was inspectable.
- **Nothing here is medical advice.**

---

**Author:** Scientist A · **Date:** 2026-09-21 · **Mode:** READ-ONLY · **No canonical file
modified** — no registry, queue, ledger or current file was edited, no commit candidate was
produced, and no git command was run. One file written: this one. No full-text artefact was
written, because the conditional that would have authorised it was not satisfied.
