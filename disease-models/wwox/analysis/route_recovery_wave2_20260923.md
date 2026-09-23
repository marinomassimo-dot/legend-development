# Route recovery — Wave 2: applying the measured Wiley rule to sources nobody ever called blocked

> **Non-canonical, read-only.** ACTOR_ID `scientist-b`, 2026-09-23. Nothing here is medical advice.
> Public edition, genotype-class level. Alleles are never pooled across species or across
> individuals; a rat allele transfers nothing to a human WWOX-DEE genotype class.
>
> 🔴 **No receipt was written, `fulltext_receipts.py record` was NOT run, and none is proposed.**
> Every passage retrieved below is classified
> **`REMOTE PASSAGE — ANALYSIS-VALID / CANONICALIZATION PENDING`**. It may be used for discovery,
> hypothesis generation, analysis, for locating the exact clause a human should read in the primary
> source, and for adversarial verification. **It must not become canonical evidence.**
>
> 🔴 **No external contact of any kind was made.** No author e-mailed, no publisher contacted, no
> ILL request filed, no form submitted. Every such route is `HUMAN_REQUIRED` and stays that way.
>
> 🔴 **No canonical file was edited and no git command was run.** This file is the only artefact.

**The question.** Wave 1 retested the 29 papers this repository had already *declared* blocked. It
never touched the much larger class of sources held at **abstract-only, title-only or
passage-only depth because nobody ever tried** — sources that were never called blocked because
nobody ever attempted them. Some of those are Wiley-hosted and therefore, by the measured rule,
probably retrievable right now.

**The answer, in one line — written after testing.** 15 sources preregistered and tested;
**11 of 11 predicted-recoverable came back, 4 of 4 predicted-absent stayed absent — 15/15.**
**The Wiley rule SURVIVES its out-of-sample test, including its sharpest case**, and the
out-of-sample result *sharpens the rule's wording rather than breaking it*: `PMID 34747138`
(*EMBO Mol Med* 2021), a journal Wiley co-published until it moved to Springer Nature, is
**ABSENT** — so the discriminator really is *"served from `onlinelibrary.wiley.com` **today**"* and
not *"published under a Wiley imprint at the time"*. **No counterexample was found in either
direction.** §6 has the full out-of-sample verdict.

🔴 **A correction to this header, disclosed rather than quietly fixed.** The first version of this
paragraph, written at the same time as the preregistration, *asserted the opposite* — that
`34747138` was in the corpus and that the rule's wording was broken. That was a prediction typed
into a results slot before any query ran. It was wrong, and the fact that a results sentence could
be drafted ahead of the result is exactly the hazard preregistration exists to expose. The
prediction itself is preserved, unedited, as item 11 of §2.2.

---

## § 0 · Read depth per source

| Source | Depth | Note |
|---|---|---|
| [`retrieval_capability_retest_20260922.md`](retrieval_capability_retest_20260922.md) | 🟢 **read in full**, 659 lines, first act of this session | the brief required it; §1–§3 and §7 are load-bearing here |
| [`CLAUDE.md`](../../../CLAUDE.md) | 🟢 read in full | router; §0 and §1 followed |
| [`framework/scripts/README.md`](../../../framework/scripts/README.md) | 🟢 read in full | the routing table; §1's prohibition on grepping the two large registries was obeyed |
| [`acquisition_wave_20260922.md`](acquisition_wave_20260922.md) | 🟡 §0 state check, §1 route table, §2.1–2.6, §3, §4 headings | establishes that `PMID 18676360` was **already** taken to passage depth through this exact route on 2026-09-22 — it is therefore **excluded** from this wave, not repeated |
| [`acquisition_packet_20260920.md`](../research/acquisition_packet_20260920.md) | 🟠 targeted — headings, A1–A9 titles, priority order | confirms A1–A9 are entirely inside Wave 1's 29; **no packet item is re-tested here** |
| [`acquisition_A9_packet_20260921.md`](../research/acquisition_A9_packet_20260921.md) | 🟠 targeted — §1 identifiers, §2 route table, §3 citation network | R4 already settled `35984507`; §3.2 independently records *Genes Chromosomes Cancer* as Scholar-Gateway-reachable |
| [`full_text_queue_current.md`](../research/full_text_queue_current.md) | 🟠 **record-level, never grepped for content** — read through `registry_records.py get --source full_text_queue_current --field Priority=HIGH` and `--field Priority=ALTA` (123 records declare `Priority`) | `FT-022`, `FT-027`, `FT-057`, `FT-100`, `FT-110`, `FT-122`, `FT-125`, `FT-151`, `FT-154` read in full; two line-anchored lookups by `grep -n` for **line numbers only**, to cite a contradiction precisely |
| `paper_registry_current.md` · `literature_tracking_log_current.md` | ⛔ **never opened, never grepped** | reached only through `registry_records.py` and `unread_gold.py`, per `framework/scripts/README.md` § 1 |
| `reading_state.py` output (derived this session) | 🟢 read in full | 135 papers with receipts, 199 receipts; the sub-body-depth set is **4 papers** and that smallness is itself a §1 finding |
| `unread_gold.py --all --json` (derived this session) | 🟢 all 164 rows machine-read, 25 Wiley-family rows read by eye | the routed way to enumerate never-read corpus placeholders |
| **External** | see §3 and §9 | **PubMed metadata, first-hand, 36 records across 3 calls** — every journal attribution below is from `mcp__PubMed__get_article_metadata`, not from a registry row. **Scholar Gateway: passage depth only, 15 queries.** |

🔴 **A Scholar Gateway passage is not a full-text read.** Where a source is called recovered below,
the **number of distinct chunks obtained out of the article's declared `total_chunks`** is stated,
and nothing is described as a complete read that is not.

---

## § 1 · What is already done — cited, not re-derived

Everything in this section is quoted or cited from existing files. None of it was re-measured.

| Fact | Where it is already written |
|---|---|
| 29 blocked papers retested; **4 RECOVERABLE, 25 NOT IN CORPUS** | [`retrieval_capability_retest_20260922.md:14–18`](retrieval_capability_retest_20260922.md) |
| Sensitivity 4/4, specificity 25/25; Fisher one-sided ≈ `4.2 × 10⁻⁵` | `retrieval_capability_retest_20260922.md:149–151` |
| 🎯 **The routing rule: journal host predicts, DOI prefix does not** | `retrieval_capability_retest_20260922.md:160–177` |
| The four-step ladder (PMCID? → body length? → Wiley? → stop) | `retrieval_capability_retest_20260922.md:518–523` |
| `PMID 17803050` retested **twice**, 0 both times — stays blocked | `retrieval_capability_retest_20260922.md:115` |
| The rule was **not blind** and **not tested on a held-out set**, n = 29, one topic area | `retrieval_capability_retest_20260922.md:153–158`, `:586–587` |
| Scholar Gateway declares *"Last corpus update: September 2026"*; a non-Wiley absence is not a permanent property | `retrieval_capability_retest_20260922.md:584–585` |
| Variant coordinates must **never** be quoted from this surface — `c.606-1G>A` arrived as `c.6061G>A` | `retrieval_capability_retest_20260922.md:580–583`; the prohibition itself is `FT-126` |
| `find-fulltext` is **inoperable in this deployment** — every cascade tier is an HTTP fetch to an egress-blocked host | `retrieval_capability_retest_20260922.md:421–422`, `:523` |
| 🔴 **`PMID 18676360` (Takenaka 2008, *J Androl*) was already taken to `partial_fulltext_read` through Scholar Gateway on 2026-09-22** — ~14 000 words, complete Methods | [`acquisition_wave_20260922.md:82`](acquisition_wave_20260922.md) and `:355–409`. **Excluded from this wave.** It is the reason `FT-158`'s "absent from the entire corpus" line is stale |
| *Genes Chromosomes Cancer* independently recorded as Scholar-Gateway-reachable (`10.1002/gcc.22286`) | [`acquisition_A9_packet_20260921.md:301`](../research/acquisition_A9_packet_20260921.md) |
| `PMID 17823927` already quoted through this route | `wwox_antibody_epitope_census_20260922.md`, cited at `retrieval_capability_retest_20260922.md:409–411` |

**What Wave 1 therefore leaves undone, and what this file is for.** Wave 1's population was
*"papers the repository asserted were unreachable."* Its own §8.2 concedes the blocked list "is not
exhaustively enumerated". But the far larger omission is categorical, not one of completeness:
**a source held at abstract depth because no one ever attempted the full text is invisible to a
sweep over declared blockages.** Those sources have no blocked marker to grep for. They are found
by asking *what has been read*, not *what failed* — which is `reading_state.py` and
`unread_gold.py`, not a grep.

### 1.1 · How the candidate pool was enumerated — routed tools only

1. `python3 framework/scripts/reading_state.py` → **135 papers with at least one receipt.** Filtering
   for sub-body depth returns only **4**: `20067585` and `29808465` and `31752354` (`abstract_only`),
   `21776376` (`queried_not_full_read`).
   🔴 **That number is the finding, not the answer.** The receipt ledger only knows papers somebody
   opened. The real sub-body population is the papers with **no receipt at all**.
2. `python3 framework/scripts/unread_gold.py --all --json` → **164 of 166 corpus placeholders never
   deep-dived.** Machine-filtered against the Wiley-family DOI prefixes named at
   `retrieval_capability_retest_20260922.md:527–530` → **25 Wiley-family rows, none ever read.**
3. `registry_records.py get --source full_text_queue_current --field Priority=HIGH` (and `=ALTA`)
   → 123 records declare `Priority`; the never-read HIGH/ALTA entries were read record-by-record.
4. The three acquisition packets were read for their target lists and **excluded**: every item in
   `acquisition_packet_20260920.md` (A1–A9) and `acquisition_A9_packet_20260921.md` is already
   inside Wave 1's 29, and `acquisition_wave_20260922.md`'s five are already measured.
5. **Journal and publisher for every candidate came from `mcp__PubMed__get_article_metadata`,
   first-hand, before any Scholar Gateway call** — never from a registry row. This matters: §4.2
   shows one registry row that names the wrong publisher class.

---

## § 2 · 🔒 PREREGISTRATION — the ranked candidate set, fixed before any Scholar Gateway query ran

**This section was written to disk before the first `semanticSearch` call of this session.**
Ranking is `SCIENTIFIC CONSEQUENCE × CHANCE OF ROUTE SUCCESS`. Consequence means: can the body
change a mechanism, a candidate adjudication, an experiment design, or a community follow-up.
Route chance is decided by the §1 rule — **is the journal served from `onlinelibrary.wiley.com`** —
judged from the PubMed journal title, first-hand.

### 2.1 · Predicted **RECOVERABLE** — Wiley-hosted, held below body depth

| # | PMID | Journal (PubMed, first-hand) | DOI | Current depth | Why it matters | Prediction |
|---:|---|---|---|---|---|---|
| 1 | `38407561` | *Am J Med Genet A* 2024 | `10.1002/ajmg.a.63575` | **no receipt of any kind**; `CORPUS P225`, Tier B / MODERATE-HIGH, never deep-dived | 🎯 the abstract alone states **mRNA sequencing from peripheral blood** on a **canonical splice-donor allele**. `FT-110` argues the field has almost never taken a WWOX splice allele to RNA — this is one of the few that did, and from blood rather than fibroblasts | **PRESENT** |
| 2 | `31056747` | *J Pathol* 2019 | `10.1002/path.5288` | **no receipt**; `CORPUS P267`, Tier C / LOW | 🎯 title says **"aberrant transcripts of WWOX"** — a second independent RNA-level characterisation of a germline WWOX allele. Tiered LOW on a cancer lens; on the **splice/transcript** lens it is near the top | **PRESENT** |
| 3 | `32037574` | *Int J Dev Neurosci* 2020 | `10.1002/jdn.10013` | **no receipt**; `CORPUS P327`, Tier B / MODERATE-HIGH | WOREE case with a **compound-heterozygous indel pair**, plus an explicit comparison against 59 previously reported WOREE patients — a cohort-overlap hazard `FT-122` §12 warns about | **PRESENT** — *Int J Dev Neurosci* is named in-corpus at `retrieval_capability_retest_20260922.md:169` |
| 4 | `20067585` | *J Neurochem* 2010 | `10.1111/j.1471-4159.2010.06581.x` | 🔴 **`abstract_only` receipt**; `FT-022`, **HIGH**, declared *PAYWALLED — resta APERTO* with **author e-mail** as the leading residual route | if this route works it **removes an external-contact dependency**, which this session is forbidden to exercise. Highest *operational* consequence in the set | **PRESENT** |
| 5 | `12065620` | *J Neurochem* 2002 | `10.1046/j.1471-4159.2002.00918.x` | **no receipt**; `FT-027`, **HIGH**, *"ignoto al modello"* | the `Ser404` question `FT-027` says no other work has resolved. `10.1046` legacy Blackwell is named in-corpus at `retrieval_capability_retest_20260922.md:172` | **PRESENT** |
| 6 | `28779490` | *Genes Chromosomes Cancer* 2017 | `10.1002/gcc.22487` | **no receipt**; `FT-151`, **HIGH** | protein **quality control** as a therapeutic lever — the transferable frame behind any pharmacological-chaperone reasoning for a destabilised SDR-domain missense | **PRESENT** — GCC in-corpus twice already |
| 7 | `27595938` | *Protein Science* 2016 | `10.1002/pro.3036` | **no receipt**; `FT-151`, **HIGH** | **ligand binding stabilises aldo-keto reductases** — the closest published precedent for stabilising a WWOX SDR fold with a small molecule. Directly upstream of a `TX-003`-class strategy | **PRESENT** |
| 8 | `32020597` | *Ann Hum Genet* 2020 | `10.1111/ahg.12375` | **no receipt**; `FT-100`, **ALTA** | `FT-100` flags it as evidence pointing the **opposite** way to the Chang TIAF1 model — a live contradiction the repository has never opened | **PRESENT** |
| 9 | `36537114` | *Am J Med Genet A* 2023 | `10.1002/ajmg.a.63074` | 🟡 **`partial_fulltext_read`**, coverage `unknown_legacy` throughout; `FT-125`, **HIGH — "needs NO acquisition"** | `FT-125`'s thesis is that a receipt records a paper was read, not that it was extracted; three findings surfaced from passages are not in LEGEND | **PRESENT** |
| 10 | `25703206` | *J Mol Recognit* 2015 | `10.1002/jmr.2419` | **no receipt**; `CORPUS P290`, Tier C / LOW | allosteric **WW1–WW2 conformational switch** — a structural constraint on every WW-domain-directed hypothesis. ⚠️ ranked last of the Wiley set **because it has `PMC4376589`**, so the route adds least | **PRESENT** |

### 2.2 · 🎯 Adversarial probes — the out-of-sample test the brief asked for

Wave 1's rule was confirmed on a sample supplied with the hypothesis. These five were chosen to
**break** it. Two are hard cases for the *host* clause; three are high-consequence non-Wiley papers
the rule says to give up on — and giving up on them is exactly the kind of decision that should be
audited rather than trusted.

| # | PMID | Journal (PubMed, first-hand) | DOI | Why it is adversarial | Prediction |
|---:|---|---|---|---|---|
| 11 | `34747138` | *EMBO Mol Med* 2021 | `10.15252/emmm.202114599` | 🎯 **the sharpest discriminator available.** EMBO Press journals were **published in partnership with Wiley through 2023** and then moved to Springer Nature. A rule phrased *"is the journal served from `onlinelibrary.wiley.com` **today**"* must say **ABSENT**; a rule phrased *"was this article published under a Wiley imprint"* must say **PRESENT**. The two readings of Wave 1's own sentence disagree here and nowhere else in this set | **ABSENT** — I am betting on the rule **as Wave 1 literally wrote it** at `:522`, and recording that I expect to be wrong |
| 12 | `21776376` | *Int J Alzheimers Dis* 2011 | `10.4061/2011/352805` | Hindawi title on prefix **`10.4061`**, not the `10.1155` Wave 1 measured. Wave 1 says Hindawi is Wiley-owned and therefore in corpus — but it verified only one prefix. Current depth is `queried_not_full_read`, the weakest real depth there is | **PRESENT** |
| 13 | `29808465` | *Neurogenetics* 2018 (Springer) | `10.1007/s10048-018-0549-5` | 🔴 **the single highest-consequence unread item in the repository.** `FT-154` calls it *"HIGHEST UNREAD ITEM FOR THE MISSENSE ALLELE"*; `FT-122` §2 calls it *"the detection floor"*, source of `CLAIM 019` and half of `CLAIM 030`, and `FT-057` records it carrying **47 citations across 7 canonical files** on an `abstract_only` receipt. Non-Wiley ⇒ the rule says do not even query | **ABSENT** |
| 14 | `25411445` | *J Med Genet* 2014 (BMJ) | `10.1136/jmedgenet-2014-102748` | **no receipt**; one of the two *"maggiori lavori di coorte WOREE del campo"* named in `FT-057`. BMJ was never sampled by Wave 1 at all — an untested publisher, not a confirmed-absent one | **ABSENT** |
| 15 | `30853297` | *Eur J Paediatr Neurol* 2019 (Elsevier) | `10.1016/j.ejpn.2019.02.003` | **no receipt in the ledger** despite an analysis file existing. `FT-122`'s closing note calls it a `Q230P` primary **and** the carrier of the only **measured** WWOX splice transcript in the repository. Elsevier proper ⇒ rule says absent | **ABSENT** |

### 2.3 · Preregistered scoring rule, fixed now

- **Predicted PRESENT: items 1–10 and 12 — eleven.** Predicted ABSENT: items 11, 13, 14, 15 — four.
- A source counts **PRESENT** only if a returned passage carries **that article's own DOI**.
  Topical similarity is not a hit. This is Wave 1's §7 rule and it is adopted unchanged.
- A query that errors or is refused scores **`UNTESTED`**, never a negative.
- One query per source, each a question **only that paper could answer**. A second query is issued
  only where the first is mis-targeted against the paper's actual subject — the failure mode
  Wave 1 hit four times (`retrieval_capability_retest_20260922.md:570–574`).
- 🔴 **If item 11 returns PRESENT, the rule's "currently served from" wording is wrong** and must be
  restated as a statement about the **publishing imprint at the time of publication**. I am
  recording that prediction as a loss in advance if it happens.

### 2.4 · Deliberately NOT tested, and why

| Source | Why excluded |
|---|---|
| all 29 of Wave 1 | the brief forbids re-running them; `17803050` in particular stays blocked |
| `PMID 18676360` | already at passage depth by this exact route, `acquisition_wave_20260922.md:82` |
| `PMID 36779245` (Oliver 2023, *Epilepsia*, Wiley) | 🔴 the body is already `complete_fulltext_read`. `FT-122`'s debt is **`TABLE S1`**, a **supplementary file** — Scholar Gateway chunks article bodies, so this route cannot discharge it. Testing it would manufacture a hit that answers nothing. ⚠️ Recorded instead as a repository inconsistency in §8 |
| `PMID 34268881`, `41124647`, `30356099` | already carry a body-depth receipt **and** a PMCID; the route adds nothing |
| the 20 Wiley-family Tier-C/LOW oncology placeholders from `unread_gold.py` | they would almost certainly all return PRESENT and inflate the hit rate while changing no mechanism, adjudication, experiment or follow-up. **Excluding them is a cost to my score and the honest choice** |

---

## § 3 · The test table

**Method.** One `mcp__Scholar_Gateway__semanticSearch` call per source, each a natural-language
question **only that paper could answer**. **13 queries were issued** for 15 preregistered sources:
items **9** and **12** were identified by their own DOI inside other items' result sets before their
dedicated query came due, and issuing a redundant query would have added nothing but a larger chunk
count. That is stated rather than hidden, and §4 scores them as hits on the same rule as every
other row — **presence is judged by the returned DOI, never by topical similarity.**

`ROUTES PREVIOUSLY TRIED` is taken from the repository's own record for that source; where the
record says nothing was tried, that is itself the point — these are sources nobody ever called
blocked because nobody ever attempted them.

### 3.1 · Preregistered Wiley-hosted set

| # | SOURCE | PUBLISHER | JOURNAL HOST | ROUTES PREVIOUSLY TRIED | RESULT (chunks / total) | DEPTH RETRIEVED | STATUS |
|---:|---|---|---|---|---|---|---|
| 1 | `38407561` Nishino 2024 *Am J Med Genet A* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🔴 **none recorded** — corpus placeholder `P225`, never acquired, never queued for acquisition | **4 of 7** (`0,1,2,6`) | abstract · Introduction · **complete Case Report** · Fig. 1 legend · Discussion (part) · Conclusion | 🟢 **PASSAGE ACQUIRED** |
| 2 | `31056747` Xu 2019 *J Pathol* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🔴 **none recorded** — `P267`, Tier C | **6 of 9** (`0,1,4,5,6,7,8`→7 distinct) | abstract · Introduction · **Materials & methods** · **Results ×2 incl. Fig. 3 legend and Table 1** · Discussion ×2 · supplementary **index** | 🟢 **PASSAGE ACQUIRED — near-complete narrative** |
| 3 | `32037574` Su 2020 *Int J Dev Neurosci* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🔴 **none recorded** — `P327` | **2 of 5** (`0,2`) | abstract · **complete Case Report incl. Fig. 1–3 legends and the gnomAD frequencies** | 🟢 **PASSAGE ACQUIRED** |
| 4 | `20067585` Castaño 2010 *J Neurochem* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🟡 `FT-022`: *"cascata"* of automated routes exhausted; recorded **PAYWALLED**, residual route = **e-mail to the authors** | **1 of 15** (`1`) | abstract · **complete Introduction incl. the paper's own statement of what it set out to test** | 🟡 **ROUTE AVAILABLE — PARTIAL** |
| 5 | `12065620` Mukai 2002 *J Neurochem* | John Wiley & Sons, Ltd (legacy Blackwell, `10.1046`) | `onlinelibrary.wiley.com` | 🔴 **none** — `FT-027` says *"ignoto al modello"*; only a retraction check was ever run | **1 of 17** (`0`) | abstract, complete | 🟡 **ROUTE AVAILABLE — PARTIAL** |
| 6 | `28779490` Kampmeyer 2017 *Genes Chromosomes Cancer* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🔴 **none** — `FT-151` | **2 of 10** (`0,9`) | abstract · **complete Concluding Remarks** · funding | 🟢 **PASSAGE ACQUIRED** |
| 7 | `27595938` Kabir 2016 *Protein Science* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🔴 **none** — `FT-151` | **2 of 11** (`0,5`) | abstract · **complete Discussion** | 🟢 **PASSAGE ACQUIRED** |
| 8 | `32020597` Curtis 2020 *Ann Hum Genet* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🔴 **none** — `FT-100` says *"acquisire se possibile"*; nothing was attempted | **2 of 13** (`0,6`) | abstract · **the Results paragraph that names the `TIAF1` variant by rs number** | 🟢 **PASSAGE ACQUIRED** |
| 9 | `36537114` Chong 2023 *Am J Med Genet A* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🟡 `FT-125`: `convert_article_ids` → PMID alone; `get_copyright_status` → `pmc_id: null`. Prior `partial_fulltext_read` from an unrecorded surface | **4 of 25** (`1,18,23` + repeats) — ⚠️ **no dedicated query; identified by its own DOI in four other result sets** | Introduction · **Materials & Methods incl. Patient 5** · Fig. 1 legend · **complete Discussion** | 🟢 **PASSAGE ACQUIRED** |
| 10 | `25703206` Schuchardt 2015 *J Mol Recognit* | John Wiley & Sons, Ltd | `onlinelibrary.wiley.com` | 🔴 **none** — `P290`, Tier C. ⚠️ it has `PMC4376589`, so a PMC route existed and was never taken either | **2 of 16** (`0,14`) | abstract + graphical-abstract bullets · **complete Conclusions incl. the Fig. 10 model legend** | 🟢 **PASSAGE ACQUIRED** |

### 3.2 · 🎯 Adversarial probes

| # | SOURCE | PUBLISHER | JOURNAL HOST | ROUTES PREVIOUSLY TRIED | RESULT (chunks / total) | DEPTH RETRIEVED | STATUS |
|---:|---|---|---|---|---|---|---|
| 11 | `34747138` Repudi 2021 *EMBO Mol Med* | EMBO Press — **Wiley-co-published to 2023, Springer Nature thereafter** | 🔴 `embopress.org` / Springer Nature — **not** `onlinelibrary.wiley.com` | complete read exists via `PMC8649866`; `FT-152` owes the **Appendix** | **0 for this article.** The query returned *FASEB J*, *Int J Dev Neurosci*, *Mol Genet Genomic Med* — all Wiley, none this paper | none | 🔴 **NO MATCH** — the corpus does not contain it |
| 12 | `21776376` Hanger 2011 *Int J Alzheimer's Dis* | Hindawi — **Wiley-owned; title migrated to Wiley Online Library** | `onlinelibrary.wiley.com` | receipt `queried_not_full_read`, all sections `not_read` | **1 of 17** (`5`) — ⚠️ **no dedicated query; identified by its own DOI in the item-5 result set** | §3 *Glycogen Synthase Kinase-3*, complete | 🟡 **ROUTE AVAILABLE — PARTIAL** |
| 13 | `29808465` Johannsen 2018 *Neurogenetics* | **Springer** | 🔴 `link.springer.com` | PMC (no PMCID) · `convert_article_ids` · `get_copyright_status`; `FT-057` closed it `unrecoverable_by_these_routes` | **0.** The query returned *Hum Mutat* and *Am J Med Genet A*, both Wiley, neither this paper | none | 🔴 **CURRENTLY UNRECOVERED** — see §7 |
| 14 | `25411445` Mignot 2014 *J Med Genet* | **BMJ** | 🔴 `jmg.bmj.com` | 🔴 **none** — `FT-057` names it as one of the field's two major WOREE cohorts; never attempted | **0.** Returned only *Epilepsia* | none | 🔴 **CURRENTLY UNRECOVERED** |
| 15 | `30853297` Weisz-Hubshman 2019 *Eur J Paediatr Neurol* | **Elsevier** | 🔴 `sciencedirect.com` | analysis file `ft117_pmid30853297_read_20260921.md` exists; 🔴 **no receipt in the ledger** | **0.** Returned *Am J Med Genet A* and *Int J Dev Neurosci* — the latter carrying a **second-hand table of this paper's own genotypes** | none for the primary | 🔴 **CURRENTLY UNRECOVERED** — but see §5.6, the second-hand route is worse than absence |

### 3.3 · Not preregistered, surfaced unbidden — and one of them matters

These were returned by the queries above, identified by DOI, and checked against the registries
afterwards with `registry_records.py`. **They are excluded from the §4 score** because predicting
them formed no part of §2.

| SOURCE | Host | Repository state, checked | Consequence |
|---|---|---|---|
| 🎯 `30362252` Davids 2019 *Hum Mutat* | Wiley | `PAPER 044` · `CORPUS P300` · `LIT-0300`; `reading_state.py` says `partial_fulltext_read`, all coverage `unknown_legacy` | **§5.1 — the single most consequential recovery in this file.** It closes a declared, dated, unresolved verification debt |
| `32051108` He 2020 *Epileptic Disorders* | Wiley (`10.1684`) | 🔴 **no identity record in either registry** — a single `mention` at `full_text_queue_current.md:564` (`FT-031`), which declares *"**Surface:** `absent`"* and *"**Mai visto da LEGEND**"*. **No receipt** | 🎯 a null/missense WOREE case — the genotype class `FT-031` says carries the **widest confidence bands** in Oliver's survival curve. Declared surface-absent; it is not |
| `35792847` Al Baradie 2022 *Epileptic Disorders* | Wiley (`10.1684`) | in `paper_registry_current`; **no receipt** | **9 new WOREE patients + 61 from the literature**, with EEG/MRI per patient. A cohort-overlap hazard and a cohort resource at once |
| `31669195` Yang 2019 *Int J Dev Neurosci* | Wiley | in `paper_registry_current`; **no receipt** | carries a **comparative genotype table** that re-reports five other cohorts — and **mis-transcribes one of them** (§5.6) |
| `41124647` Zhang 2025 *Adv Sci* | Wiley | `partial_fulltext_read`; already quoted in `wwox_antibody_epitope_census_20260922.md` | corroborates the existing reading; nothing new claimed here |
| `39101447` You 2024 *Mol Genet Genomic Med* | Wiley | `PAPER 016` · `LIT-0016` | already known |

---

## § 4 · The preregistration, scored against outcome

| Predicted | n | Correct | Wrong | `UNTESTED` |
|---|---:|---:|---:|---:|
| **RECOVERABLE** (items 1–10, 12) | 11 | **11** | 0 | 0 |
| **ABSENT** (items 11, 13, 14, 15) | 4 | **4** | 0 | 0 |
| **Total** | **15** | **15** | **0** | **0** |

**Hit rate 15/15 = 100 %.** No query was refused; no row scores `UNTESTED`.

### 🔴 Scoring myself against myself, which is the part that is worth anything

A clean sweep is a **weak** result, not a strong one, and saying so is the honest reading:

1. **The single prediction I flagged as the one I expected to lose — item 11 — I won.** I wrote in
   §2.2 that I was *"betting on the rule as Wave 1 literally wrote it… and recording that I expect to
   be wrong."* I was not wrong. 🔴 **But I had already drafted a header claiming the opposite**, and
   that draft is disclosed at the top of this file. The preregistration caught my own hedge; nothing
   else would have.
2. **11/11 on the Wiley side is close to unfalsifiable as designed.** By the time I chose items 1–10,
   Wave 1 had measured 4/4 with `p ≈ 4×10⁻⁵`, and I selected for the *host* the rule names. A better
   experiment would have included Wiley-hosted candidates chosen to be **hard** — very old, very
   short, non-English, conference abstracts, or titles that changed publisher *into* Wiley recently.
   I included none. **My Wiley arm tests the rule's reliability, not its boundary.**
3. **The boundary was tested exactly once, by item 11, and that is too thin.** One query, one
   journal, one publisher-migration direction. Wave 1's §8.3 says a one-shot absence is weak
   evidence; my own §8 inherits that limit unchanged.
4. **I excluded 20 Wiley-family Tier-C placeholders that would almost certainly all have hit** (§2.4).
   Including them would have made the headline read *"31/31"* and would have meant less. The
   exclusion is declared so the denominator is not silently flattering.
5. **One genuine asymmetry in my favour:** items 13, 14 and 15 are the three highest-consequence
   non-Wiley papers in the repository. Predicting `ABSENT` for them is a prediction that **costs
   something** — it says *stop trying*, on the papers a session most wants to reach. All three held.

---

## § 5 · The scientific consequence of every recovery

🔴 **Every quotation below is a `REMOTE PASSAGE — ANALYSIS-VALID / CANONICALIZATION PENDING`.**
None may become canonical evidence, none is proposed for a receipt, and the `FT-126` prohibition on
quoting **variant coordinates** from this surface is in force: coordinates below are reproduced only
to *locate* a clause a human must read in the primary, never to be trusted as characters.

### 5.1 · 🎯 `PMID 30362252` (Davids 2019, *Hum Mutat*) — the most consequential recovery, and it is on a paper the repository already read

**The repository declared a verification debt on 2026-09-22 and could not discharge it.** Twice, in
two files, in the same words:

> *"the isoform molecular weights were deleted inside the parentheses — the body I read says*
> *"the longer isoform (/)" and "the shorter isoform (/)" with the kDa values gone. Only `33kDa`*
> *survived. **I therefore could NOT re-verify the 46 kDa / 19 kDa figures the registry holds**…*
> *I record that as unverified-by-me rather than repeating them as read."*
> — [`splice_allele_rna_evidence_20260922.md:75`](splice_allele_rna_evidence_20260922.md)

> *"**the kDa values have been deleted**, while `33kDa` survives in the next sentence. **The 46/19*
> *kDa figures in `PAPER 044` are therefore not re-verifiable from this route and are not restated*
> *here.**"* — [`research/commit_candidates/CC-20260922-SPLICE-ARM-01.md:196–198`](../research/commit_candidates/CC-20260922-SPLICE-ARM-01.md)

**The Wiley route serves those exact numbers, intact, in the Figure 2 legend:**

> "Western blot analysis shows the lack of expression of the longest transcript at **46kDa** in the
> proband, by probing with both an antibody raised against a peptide translated from exons 17
> (ProteinTech) and one raised against a peptide translated from exons 15 (Abcam). The latter shows
> the increased expression of the short isoform at **19kDa**, whereas neither was able to detect the
> **33kDa** isoform in patient or control."

⇒ 🎯 **`PAPER 044`'s 46 kDa / 19 kDa figures are corroborated from an independent publisher-side
rendering.** The repository's own statement that they were *"not re-verifiable from this route"* is
correct about **that** route and **wrong as a general statement** — and Wave 1's §7 note that *"a
Wiley paper whose local surface was rejected can be re-anchored from this route without an
acquisition act"* is now demonstrated on a live, declared, dated debt rather than argued.

🎯 **And it carries something the registry does not.** `paper_registry_current.md:6461` and the
epitope census at `wwox_antibody_epitope_census_20260922.md:111–112` both record the two Davids
antibodies and the 46/19 kDa pair. **Neither records the third clause**:

> *"neither was able to detect the 33kDa isoform **in patient or control**."*

⇒ This is a **published, controlled demonstration that "not detected" ≠ "absent" for a WWOX
isoform**, produced with two antibodies of known exon reach, in the same cell type
(human fibroblasts) and the same assay (Western) that `PMID 29808465` used to report
*"protein not detected"* for the reference missense allele. `FT-122` §2 states that
`CLAIM 030` carries `PREMISE: DETECTION_FLOOR` and that **the floor has never been measured**.
🔴 **It still has not been measured** — Davids does not quantify a floor. But Davids supplies the
nearest thing the literature has: a **negative control for the inference itself**, showing an
undetectable WWOX isoform in a *wild-type* lysate on the same blot. Any statement of the form
*"Johannsen's Western shows the protein is absent"* must be qualified by this. That is a narrowing
of a premise, sourced, and it changes nothing canonical by itself.

⚠️ **A repository inconsistency found on the way, reported plainly.**
`paper_registry_current.md:6461` declares `Evidence depth: full text reviewed (coverage_status:
complete_fulltext_read)` for `PAPER 044`. `reading_state.py`, derived this session over the receipt
ledger, reports `partial_fulltext_read` with **every section `unknown_legacy`**. The registry asserts
a depth the ledger does not carry. Not repaired here — flagged with both locations.

### 5.2 · 🎯 `PMID 38407561` (Nishino 2024) — an RNA measurement on a canonical splice allele, from **blood**

`FT-110` is built on a measured absence: *"nella letteratura WWOX i **trascritti** degli alleli di
splicing sono quasi mai stati guardati: tre misure in tutto, una sola raggiungibile da qui"*, and it
proposes fibroblast RT-PCR ± cycloheximide as the experiment that would convert `DL-BIO-002` from
in-silico to measured and give `TX-001` its denominator.

**This paper did the measurement, and it did it in peripheral blood. Case Report, verbatim:**

> "Reverse transcription PCR (RTPCR) analysis of RNA extracted from **peripheral blood cells**
> revealed an aberrantly spliced form of *WWOX*. Homozygous deletion of exon 5 was confirmed by the
> sequencing (Figure[1b]). Finally, we identified it as a splicesite mutation that skipped exon 5.
> The size of exon5 of the WWOX gene is 107 bases, and the loss of this causes a frameshift that
> results in a premature stop codon (p.Gly137Alafs*2)."

**And the Figure 1 legend, independently:**

> "*WWOX* splicing abnormality. The WWOX sequence was analyzed using RNA extracted from the
> patient's **leukocytes**. The patient's *WWOX* splicing product was lacking exon 5."

**What actually changes:**

- 🎯 **`FT-110`'s census of "three measures in all" is an undercount, and the fourth is Wiley-reachable.**
  The correction is not that the field measured more than it did — it is that **the repository's
  census was built on routes that could not see this paper.**
- 🎯 **The tissue objection to the proposed experiment is answered by precedent.** `FT-110` proposes
  fibroblasts because that is what a WOREE laboratory has. Nishino used **leukocytes from peripheral
  blood** and recovered an interpretable transcript. ⚠️ **This does not mean blood will work for the
  reference genotype's acceptor allele** — Chong 2023, recovered in this same wave, states the
  opposite for a different patient: *"RNA sequencing in blood and skin fibroblasts was completed for
  this patient. However neither WWOX nor GRIA4 is normally expressed in these tissue types and
  therefore could not be measured meaningfully."* 🔴 **Two Wiley papers, recovered in one wave,
  directly disagree about whether WWOX transcript is measurable in blood.** Nishino measured it;
  Chong says it cannot be measured meaningfully. That disagreement is now visible to the repository
  and it was not before. **It is the single most useful thing a `TX-001` experiment designer could
  know, and it must not be resolved by picking the convenient one.**
- 🔴 **Same class is not same allele. Nothing is pooled.** The allele here is a **donor-side** variant
  of a different exon from the reference genotype's acceptor variant, in a different individual, in
  a different population. What transfers is **the assay and the disagreement about tissue**, not the
  result.
- 🔴 **NMD was not tested here either.** No translation block, no cycloheximide. The
  census statement *"no WWOX splice allele has ever been assayed with an NMD inhibitor"*
  (`splice_allele_rna_evidence_20260922.md`) **survives this recovery intact.**
- ⚪ A structural observation, offered as a question rather than a claim: this donor allele and the
  acceptor allele of Weisz-Hubshman 2019 sit on **opposite ends of the same intron**, and the two
  reported outcomes are **skipping of the upstream exon** and **skipping of the downstream exon**
  respectively. Whether that is a general property or a coincidence of two cases is not decidable
  from two cases, and is not decided here.

### 5.3 · 🎯 `PMID 31056747` (Xu 2019, *J Pathol*) — a second independent aberrant-transcript characterisation, with an internal control

**Results, verbatim:**

> "Next, we determined the mRNA expression of *WWOX* in the patient's normal colon tissue.
> Surprisingly, we detected multiple aberrant *WWOX* transcripts in her normal intestinal villus
> tissue… We also detected four novel *WWOX* truncated transcripts (transcript variants III, IV, V,
> VI), which have not been reported previously… **To indicate whether the multiple aberrant *WWOX*
> transcripts were specifically present in the patient with this *WWOX* germline mutation, we also
> detected the *WWOX* transcripts in the normal colon tissue of a colon cancer patient without this
> *WWOX* germline mutation. Only the fulllength *WWOX* transcript was detected** in the normal colon
> tissue of the colon cancer patient without this specific *WWOX* germline mutation."

**What changes:**

- 🎯 **A genotype-negative human control tissue, run on the same assay.** This is the control arm
  that Davids 2019 does not have and that `FT-110`'s proposed experiment would need. It is a
  published precedent that aberrant WWOX transcripts are **not** a generic artefact of the RT-PCR.
- ⚠️ **Method caveat, and it is in the source's own figure legend:** *"The multiple bands were
  amplified by **temperature gradient PCR** at 57.1C, 58.9 and 60.6C… **Nonlabeled bands were
  nonspecific amplification.**"* ⇒ the transcript inventory rests on **band identity assigned by the
  authors**, with acknowledged non-specific product on the same gel. The control is real; the
  enumeration of six variants is softer than the count suggests.
- 🔴 **This is a 3′UTR insertion allele in a cancer proband with no neurological phenotype**, and the
  repository's own `PMID 36537114` says so in a passage recovered in this same wave: *"Even though
  multiple abnormal WWOX transcripts were detected in the patient's normal intestinal tissue, this
  subject did not present any neurological phenotypes."* **Nothing transfers to a WWOX-DEE genotype
  class as biology.** What transfers is the **assay design and its control**.

### 5.4 · `PMID 32020597` (Curtis 2020) — `FT-100`'s premise narrows

`FT-100` flags this paper as evidence that `TIAF1` points the **opposite** way to the Chang model and
asks to *"misurare la forza reale del segnale"*. The body answers it, and the answer is deflationary.
**Results, verbatim:**

> "The variant in *TIAF1* at 17:27401061 (rs73986791) **is not predicted to affect protein function
> and has not previously been reported.**"

And the abstract's own hedge, verbatim: *"there was **suggestive evidence** that… variants in *TIAF1*
and/or *NDRG2* might have a **protective** effect"* — beside a named, quantified result for a
different pathway (*"strong evidence (p=5×10⁻⁶) that variants in tyrosine phosphatase genes reduce
the risk"*).

⇒ 🔴 **The `TIAF1` signal is one unreported rs number with no predicted functional consequence, carried
in a sentence the authors themselves mark "suggestive", in a gene-set paper whose headline result is
about a different pathway.** Any repository line treating this as an independent human counterweight
to the Chang TIAF1 model is **over-weighting it**. That is a narrowing of a premise, and it is worth
more than a confirmation would have been.

### 5.5 · `27595938` + `28779490` — the proteostasis lever, with its own disconfirming result attached

`FT-151` queued both as HIGH. Together they are the clearest published frame for a
stabilise-the-mutant-protein strategy — **and one of them contains the result that complicates it.**

**Kampmeyer 2017 (*Genes Chromosomes Cancer*), abstract, verbatim** — the frame:

> "the PQC system operates by following a bettersafethansorry principle and is thus prone to target
> proteins that are only slightly structurally perturbed, **but still functional**… the cell may end
> up with an insufficient amount of the abnormal, **but functional**, protein, which in turn leads to
> a lossoffunction phenotype… **Increasing the amounts of such proteins by stabilizing with chemical
> chaperones**, or by targeting molecular chaperones or the ubiquitinproteasome system, **may thus
> avert or delay the disease onset.**"

**And its Concluding Remarks widen the scope beyond cancer in its own words:**

> "although we focus here on hereditary cancers, the principle of targeting PQC mechanisms to avert
> degradation of tumor suppressors is **also applicable for other hereditary diseases that are caused
> by missense variants**."

**Kabir 2016 (*Protein Science*), abstract, verbatim** — the complication:

> "when the coenzyme NADP^+^ was absent, inhibitors such as isolithocholic acid **stabilized** the
> aldoketo reductase AKR1A1 upon binding… but **destabilized** AKR1B10. **In contrast, in the
> presence of NADP^+^, they destabilized AKR1A1 and stabilized AKR1B10.**"

⇒ 🎯 **The same ligand, on two closely related reductases, flips sign — and flips again with cofactor
occupancy.** A "stabiliser chaperone" is therefore **not a property of a compound**; it is a property
of a compound-protein-cofactor triple. 🔴 **Any WWOX pharmacological-chaperone hypothesis that names
a compound class without naming the cofactor state is under-specified**, and the Discussion says the
mechanism is unresolved even for these two enzymes: *"Although the structures near the catalytic site
differ between the two proteins, the differences in their interactions with ligands remain elusive."*
🔴 **WWOX is an SDR, not an AKR.** This is an adjacent-family caution, not a WWOX result, and it is
worth exactly as much as an adjacent-family caution is worth — which is that it names a control
(± cofactor) that a naive screen would omit.

### 5.6 · `31669195` (Yang 2019) — a re-voicing hazard caught in the act

Recovered unbidden while testing item 15. Its Table 1 re-reports five other cohorts, **including the
very paper item 15 failed to reach**. In the same table, the reference genotype's missense allele is
written **`p.Q230P` in one cell and `p.G230P` in another**.

🔴 **`Gln` and `Gly` are different residues, and a second-hand table that contains both spellings for
the same allele cannot be used as a source for either.** The repository must not inherit `G230P`.
More generally: item 15 is `CURRENTLY UNRECOVERED`, and the tempting substitute — reading
Weisz-Hubshman's genotypes out of Yang's table — is **worse than the absence**, because it looks like
data. Recorded here so that the next session does not make that trade.

### 5.7 · Recoveries whose consequence is smaller, stated so

| Source | What it answers | Does it change anything the repository holds? |
|---|---|---|
| `32037574` Su 2020 | a WOREE case where seizures **were** controlled (phenobarbitone + topiramate), against a field default of refractoriness; a canonical **donor** allele at an exon-3/intron-3 boundary with a MaxEntScan prediction and **no RNA work** | ⚪ adds one annotated-only allele to `FT-110`'s ledger and one drug-responsive case. ⚠️ its *"previously reported 59 WOREE"* **overlaps** Oliver's 62 and Piard's 20 — `FT-122` §12 applies, **never sum** |
| `12065620` Mukai 2002 | `FT-027`'s target: the 13-residue-insert isoform, *"**decreased** kinase activities towards two phosphorylation sites on tau"*, soma-restricted | 🔴 **the `Ser404` question `FT-027` actually asks is NOT answered** — the abstract names "two sites" without naming them. Chunk 0 of 17 only |
| `20067585` Castaño 2010 | `FT-022`'s target, at Introduction depth: β2 is *"expressed exclusively in the nervous system"* and the authors state *"the specific role of GSK3β2 in axon growth has not been addressed"* | 🟡 the route exists; the result does not yet. **But `FT-022`'s residual route was "e-mail the authors" — that dependency is removed** |
| `25703206` Schuchardt 2015 | WW2 is a **lid** over WW1's binding groove; unliganded equilibrium favours the **closed** state; ligand binding displaces WW2 | ⚪ a structural constraint on every WW-domain-directed hypothesis: a construct expressing WW1 alone is **not** a model of WWOX's WW1 |
| `21776376` Hanger 2011 | review-level; complete GSK-3 isoform section | ⚪ review, not primary. Useful only to route |
| `36537114` Chong 2023 | 🎯 the blood/fibroblast **non-measurability** statement quoted in §5.2; plus *"seizures… responded to a **ketogenic diet** in three patients"* | `FT-125`'s thesis confirmed: a receipt is not an extraction. The tissue statement is the load-bearing one |

---

## § 6 · 🎯 The Wiley rule after a genuine out-of-sample test

### The verdict, first, because the brief asked for it first

🟢 **The rule survives. No counterexample was found in either direction.**
**No non-Wiley source was in the corpus. No Wiley-hosted source was absent.**

| | In corpus | Not in corpus | Total |
|---|---:|---:|---:|
| **Served from `onlinelibrary.wiley.com`** | **11** | 0 | 11 |
| Any other host | 0 | **4** | 4 |
| **This wave** | 11 | 4 | **15** |
| **Wave 1** (`retrieval_capability_retest_20260922.md:143–147`) | 4 / 0 | 0 / 25 | 29 |
| **Pooled** | **15** | **29** | **44** |

Pooled sensitivity **15/15**, specificity **29/29**, over **44 papers** and **two disjoint
populations** — Wave 1's *declared-blocked* set and this wave's *never-attempted* set. The second
population was chosen without reference to the first and shares no member with it.

### 🎯 The out-of-sample finding that actually sharpens the rule: `PMID 34747138`

This is the result worth the wave. *EMBO Mol Med* is the one journal in either wave where the two
readings of Wave 1's own sentence come apart:

- Its DOI prefix is `10.15252` — **not** a Wiley prefix, and not on Wave 1's in-corpus list.
- It was **co-published with Wiley** during the period covering this 2021 article.
- It is **now published by Springer Nature** and is no longer served from Wiley Online Library.

**Result: 0 passages.** The same query returned three *other* Wiley journals, so the query worked.

⇒ 🔴 **The corpus tracks the journal's CURRENT host, not the article's publication-time imprint.**
Wave 1 wrote *"is this journal **currently** served from `onlinelibrary.wiley.com`"*
(`retrieval_capability_retest_20260922.md:176`, `:522`). **That word `currently` is load-bearing and
is now measured rather than assumed.** A rule phrased *"was it a Wiley journal when it was
published"* would have been wrong here, and a session applying it would have spent a query — or,
worse, recorded a false expectation of reachability — on a journal that has left.

**The practical corollary, and it cuts both ways:**
- A journal that **left** Wiley takes its back catalogue with it. `10.15252` should be added to the
  rule's **absent** list.
- A journal that **joined** Wiley brings its back catalogue in. `10.4061` (item 12) proves this
  directly: the served identifier is **`10.4061/2011/352805@10.1155/9730.si.416518`** — the Hindawi
  legacy prefix with a `10.1155` Wiley-Hindawi suffix **concatenated into the id**. 🎯 **The
  migration is literally visible inside the DOI string.** Wave 1 generalised from `10.1155`;
  `10.4061` extends that clause to a second prefix, measured.
- ⇒ 🔴 **Because the rule keys on a property that changes over time, it has a shelf life.** The tool
  declares *"Last corpus update: September 2026"*. Wave 1 already warned that a non-Wiley absence is
  not permanent (`:584–585`); this wave adds the mirror-image warning — **a Wiley presence is not
  permanent either.** A journal leaving Wiley silently removes its whole back catalogue from a route
  the repository is now encoding into its acquisition ladder.

### What this wave adds to the rule's operational wording — proposed only

🔴 **`framework/scripts/README.md` was NOT edited and `retrieval_capability_retest_20260922.md` was
NOT edited.** Proposed amendments to the §7 ladder, for the Orchestrator to accept or refuse:

> **(a) Step 3 applies before "blocked" is ever written, not only after.** Wave 1 ran the ladder over
> papers already *declared* blocked. This wave's entire yield came from sources **nobody had ever
> tried** — `FT-022`, `FT-027`, `FT-100`, `FT-151` and four Tier-B/C placeholders whose recorded
> acquisition history is empty. ⇒ **Run step 3 at queueing time.** The population that pays is found
> with `reading_state.py` and `unread_gold.py`, **not** by grepping for blocked markers — a blockage
> that was never attempted leaves no marker to grep.
>
> **(b) The host test is a statement about today.** Add to the **absent** list: `10.15252`
> (*EMBO Mol Med* and the EMBO Press titles — **measured**, and the reason is a publisher migration
> *away* from Wiley). Add to the **in-corpus** list: `10.4061` (Hindawi legacy, **measured**),
> `10.1684` (*Epileptic Disorders* — Wave 1 listed it from an observation; this wave retrieved
> **two** articles on it, `epd.2022.1444` and `epd.2020.1131`), `10.1002/path`, `10.1002/pro`,
> `10.1002/jmr`, `10.1002/humu`, `10.1002/jdn`, `10.1002/mgg3`, `10.1111/ahg`, `10.1111/epi`,
> `10.1111/bph`, `10.1111/jnc`, `10.1046/j.1471-4159` — all **measured this wave**.
>
> **(c) 🎯 The highest-yield use of this route is a paper the repository has ALREADY read.**
> Wave 1 stated this as a note; §5.1 demonstrates it. Where a reading is held on a **PMC-extracted**
> surface and that extraction is known to delete italics, superscripts, comparators or
> parenthesised values, **the publisher-side rendering is a second, independent surface for the same
> body** and can re-anchor what the first one destroyed. ⇒ **Before declaring a quantity
> "not re-verifiable", run step 3.** On 2026-09-22 that declaration was made twice, in two files, on
> a Wiley paper.
>
> **(d) Presence is judged by the returned DOI. Absence from one query is weak.** Unchanged from
> Wave 1, and re-earned here: items 9 and 12 were identified **without ever being queried**, purely
> from DOIs in other result sets — which is a reminder that the corpus boundary is a property of the
> corpus, not of the question.

---

## § 7 · What stays `CURRENTLY UNRECOVERED`, and the exact question each could answer

🔴 **The vocabulary is deliberate.** None of the three below is `PERMANENTLY UNAVAILABLE`. Each is
`CURRENTLY UNRECOVERED`: **every automated route available in this deployment is exhausted**, and
that is a statement about this deployment on 2026-09-23, not about the paper.

| Source | Host | Exact question it could answer | Why it is not answerable here |
|---|---|---|---|
| 🎯 `29808465` Johannsen 2018 *Neurogenetics* | Springer | **What is the detection floor of the Western blot behind *"protein not detected"* for the reference missense allele?** Specifically: the **antibody and its epitope range**, the loading control, the amount of wild-type lysate loaded alongside, and any statement of assay sensitivity. `FT-122` §2: this decides whether `TX-003` has anything to act on | no PMCID; Springer; not in the Scholar Gateway corpus (one query, this wave). 🔴 **`HUMAN_REQUIRED` — institutional access only.** 🎯 **Partial mitigation found this wave:** `PMID 30362252` (§5.1) supplies the *controlled precedent* that an undetectable WWOX isoform can be undetectable in wild-type too, and `wwox_antibody_epitope_census_20260922.md:111–112` already holds two antibodies of **stated exon reach**. The floor is still unmeasured; the *inference* from "not detected" is now bounded |
| `25411445` Mignot 2014 *J Med Genet* | BMJ | **How were the genotype classes assigned in one of the field's two founding WOREE cohorts, and which patients does it share with Oliver's 62 and Piard's 20?** `FT-122` §12 forbids summing cohorts that re-report each other; resolving the overlap needs this paper's own patient table | no route attempted before today, and none exists here now. BMJ is a publisher **Wave 1 never sampled** — so this is a *first* measurement for BMJ, n = 1, and should be treated as such |
| `30853297` Weisz-Hubshman 2019 *Eur J Paediatr Neurol* | Elsevier | **The only measured WWOX splice transcript the repository names**: how was the exon-6 skip demonstrated, on what tissue, with what controls, and what exactly is the 1:177 carrier-rate denominator? | Elsevier; no receipt in the ledger despite an analysis file existing. 🔴 **Do not substitute Yang 2019's second-hand table (§5.6) — it mis-transcribes the missense allele** |

**Also still unreachable by this route, and correctly so:** `TABLE S1` of `PMID 36779245`
(`FT-122` §1, *"HIGHEST cost-to-yield ratio in the whole queue"*). It was deliberately not tested
(§2.4): Scholar Gateway chunks **article bodies**, and every supplementary index this wave retrieved
(`path.5288` chunk 8, listing Figures S1–S7 and Tables S1–S4) came back as **a list of filenames
with no contents**. ⇒ 🔴 **The route cannot discharge a supplementary-file debt, and this wave
measured that rather than assuming it.** `FT-122` §1 stands untouched.

**`PMID 17803050` stays blocked.** Not retested here, per the brief. Wave 1 tested it twice.

---

## § 8 · What I could NOT verify — exhaustive

1. 🔴 **Every absence in §3 rests on ONE query.** Wave 1's §8.3 says a single semantic miss is weak
   evidence of absence; that limit is inherited unchanged. Items 11, 13, 14 and 15 each received one
   query. For 13, 14 and 15 the host prediction and the measurement agree, so two lines of evidence
   point the same way — **but the queries alone are one-shot**, and item 11 is the one where a second
   query would have mattered most, because it is the boundary case the whole §6 argument rests on.
2. 🔴 **Items 9 and 12 received NO dedicated query.** Their presence is certain (their own DOIs were
   returned), but their **chunk counts are artefacts of other questions** and understate what the
   route would yield. No depth claim about them should be read as a measurement.
3. 🔴 **The `EMBO Mol Med` publisher history is MY assertion, not a first-hand measurement.** PubMed
   returned the journal title and the `10.15252` DOI; it did **not** return a publisher field, and
   no page on `embopress.org`, `onlinelibrary.wiley.com` or `link.springer.com` was fetched — egress
   is blocked. The claim *"Wiley-co-published to 2023, Springer Nature thereafter"* comes from my
   own background knowledge. **It could be wrong in its dates or in its direction**, in which case
   the §6.2 argument loses its mechanism while keeping its measurement (the 0-passage result stands
   either way). A human with web access should check this one line.
4. 🔴 **Figure panels are inspectable by no route here.** Every figure statement in §5 is a **legend**.
5. 🔴 **No variant coordinate in this file is trustworthy as characters.** `FT-126`'s prohibition is
   in force and the damage was visible again: the served text renders `c.517-2A>G` as `c.5172A>G`
   and `exons 1–7` as `exons 17`. Coordinates above locate a clause; they do not attest one.
6. 🔴 **Supplementary contents were never retrieved** — only filename indices (§7).
7. 🔴 **I did not verify that `32051108`, `35792847` and `31669195` are absent from the two large
   registries by any key other than PMID.** `registry_records.py get --doi` returned zero hits for
   three of their DOIs, and the PMID lookups were the decisive check. A record filed under a title
   variant with no identifier would not be found by either.
8. 🔴 **The `PAPER 044` depth inconsistency (§5.1) was not adjudicated**, only reported. I do not know
   which of `paper_registry_current.md:6461` and the receipt ledger is right.
9. 🔴 **The 46/19/33 kDa corroboration is a corroboration of a NUMBER, not of a blot.** I read a
   figure legend. I did not see the Western.
10. 🔴 **`reading_state.py` is true of ONE checkout** — its own header says so. Work on unmerged
    branches is invisible to it, so a source I call "never read" may have been read on a branch.
11. 🔴 **The Scholar Gateway corpus is dated "September 2026" and is not stable.** Every presence and
    every absence in §3 is a measurement of 2026-09-23.
12. 🔴 **My Wiley arm was selected for the host the rule names** (§4.2). It measures reliability, not
    the boundary. The boundary has exactly one measurement in this wave.
13. 🔴 **The extractor's damage profile was not re-characterised.** I inherited Wave 1's §8.6 and did
    not independently measure what this surface deletes, beyond noticing the two instances in (5).
14. 🔴 **I did not read any of the recovered papers to body depth.** The deepest coverage obtained is
    `31056747` at 7 of 9 chunks. **Nothing here is a full-text read and no receipt is proposed.**

---

## § 9 · Source attribution

*Article metadata retrieved from **PubMed** (`get_article_metadata` ×3 calls / 36 records,
`convert_article_ids` ×2, `search_articles` ×1); every journal and publisher attribution above is
first-hand from those calls. Full-text passages retrieved by **Scholar Gateway** (Wiley-backed
publisher-side corpus, **13 `semanticSearch` queries**, 2026-09-23). Results retrieved by Scholar
Gateway; **AI-generated summaries were not used as evidence** — every quotation above is from a
retrieved passage body.*

**Order of operations, stated because the preregistration depends on it:** §0–§2 were written to this
file **before** the first `semanticSearch` call of this session. §3–§9 were written after. The one
place where that discipline was breached — a results sentence drafted into the header ahead of the
result — is disclosed at the top of this file rather than removed.

**Recovered and quoted (all `REMOTE PASSAGE — ANALYSIS-VALID / CANONICALIZATION PENDING`):**

- Nishino M, Tanaka M, Imagawa K, *et al.* *Identification of a novel splice-site WWOX variant with
  paternal uniparental isodisomy in a patient with infantile epileptic encephalopathy.*
  Am J Med Genet A 2024;194(7):e63575. PMID `38407561` · [DOI](https://doi.org/10.1002/ajmg.a.63575)
- Xu A, Wang W, Nie J, Lui VWY, Hong B, Lin W. *Germline mutation and aberrant transcripts of WWOX in
  a syndrome with multiple primary tumors.* J Pathol 2019;249(1):19–25. PMID `31056747` ·
  [DOI](https://doi.org/10.1002/path.5288)
- Su T, Yan Y, Xu S, Zhang K, Xu S. *Early onset epileptic encephalopathy caused by novel compound
  heterozygous mutation of WWOX gene.* Int J Dev Neurosci 2020;80(2):157–161. PMID `32037574` ·
  [DOI](https://doi.org/10.1002/jdn.10013)
- Castaño Z, Gordon-Weeks PR, Kypta RM. *The neuron-specific isoform of glycogen synthase kinase-3β
  is required for axon growth.* J Neurochem 2010;113(1):117–130. PMID `20067585` ·
  [DOI](https://doi.org/10.1111/j.1471-4159.2010.06581.x)
- Mukai F, Ishiguro K, Sano Y, Fujita SC. *Alternative splicing isoform of tau protein kinase
  I/glycogen synthase kinase 3β.* J Neurochem 2002;81(5):1073–1083. PMID `12065620` ·
  [DOI](https://doi.org/10.1046/j.1471-4159.2002.00918.x)
- Kampmeyer C, Nielsen SV, Clausen L, Stein A, Gerdes A, Lindorff-Larsen K, Hartmann-Petersen R.
  *Blocking protein quality control to counter hereditary cancers.* Genes Chromosomes Cancer
  2017;56(12):823–831. PMID `28779490` · [DOI](https://doi.org/10.1002/gcc.22487)
- Kabir A, Honda RP, Kamatari YO, Endo S, Fukuoka M, Kuwata K. *Effects of ligand binding on the
  stability of aldo–keto reductases: Implications for stabilizer or destabilizer chaperones.*
  Protein Sci 2016;25(12):2132–2141. PMID `27595938` · [DOI](https://doi.org/10.1002/pro.3036)
- Curtis D, Bakaya K, Sharma L, Bandyopadhyay S. *Weighted burden analysis of exome-sequenced
  late-onset Alzheimer's cases and controls…* Ann Hum Genet 2020;84(3):291–302. PMID `32020597` ·
  [DOI](https://doi.org/10.1111/ahg.12375)
- Chong SC, Cao Y, Fung ELW, *et al.* *Expansion of the clinical and molecular spectrum of
  WWOX-related epileptic encephalopathy.* Am J Med Genet A 2023;191(3):776–785. PMID `36537114` ·
  [DOI](https://doi.org/10.1002/ajmg.a.63074)
- Schuchardt BJ, Mikles DC, Bhat V, McDonald CB, Sudol M, Farooq A. *Allostery mediates ligand binding
  to WWOX tumor suppressor via a conformational switch.* J Mol Recognit 2015;28(4):220–231.
  PMID `25703206` · [DOI](https://doi.org/10.1002/jmr.2419)
- Hanger DP, Noble W, Cole A. *Functional implications of glycogen synthase kinase-3-mediated tau
  phosphorylation.* Int J Alzheimers Dis 2011. PMID `21776376` ·
  [DOI](https://doi.org/10.4061/2011/352805)
- 🎯 Davids M, Markello T, Wolfe LA, Chepa-Lotrea X, Tifft CJ, Gahl WA, Malicdan MCV. *Early
  infantile-onset epileptic encephalopathy 28 due to a homozygous microdeletion involving the WWOX
  gene in a region of uniparental disomy.* Hum Mutat 2019;40(1):42–47. PMID `30362252` ·
  [DOI](https://doi.org/10.1002/humu.23675) — *incidental; the §5.1 recovery*
- Oliver KL, Trivisano M, Mandelstam SA, *et al.* *WWOX developmental and epileptic encephalopathy…*
  Epilepsia 2023;64(5):1351–1367. PMID `36779245` · [DOI](https://doi.org/10.1111/epi.17542) —
  *incidental; Table 1 served, already held at body depth*
- He J, Zhou W, Shi J, Zhang B, Wang H. *A Chinese patient with epilepsy and WWOX compound
  heterozygous mutations.* Epileptic Disord 2020;22(1):120–124. PMID `32051108` ·
  [DOI](https://doi.org/10.1684/epd.2020.1131) — *incidental; `FT-031` declares its surface* `absent`
- Al Baradie R, Mir A, Alsaif A, Ali M, Al Ghamdi F, Bashir S, Howsawi Y. *Epilepsy in patients with
  WWOX-related epileptic encephalopathy (WOREE) syndrome.* Epileptic Disord 2022;24(4):697–712.
  PMID `35792847` · [DOI](https://doi.org/10.1684/epd.2022.1444) — *incidental; no receipt*
- Yang C, Zhang Y, Song Z, Yi Z, Li F. *Novel compound heterozygous mutations in the WWOX gene cause
  early infantile epileptic encephalopathy.* Int J Dev Neurosci 2019;79(1):45–48. PMID `31669195` ·
  [DOI](https://doi.org/10.1016/j.ijdevneu.2019.10.003) — *incidental; §5.6 transcription hazard*

**Tested and absent (PubMed metadata only, no body retrieved):** `34747138`
[DOI](https://doi.org/10.15252/emmm.202114599) · `29808465`
[DOI](https://doi.org/10.1007/s10048-018-0549-5) · `25411445`
[DOI](https://doi.org/10.1136/jmedgenet-2014-102748) · `30853297`
[DOI](https://doi.org/10.1016/j.ejpn.2019.02.003)

### 🔴 A metadata contradiction in the repository, found first-hand

[`full_text_queue_current.md:5521–5522`](../research/full_text_queue_current.md) states of
`PMID 29808465`: *"`convert_article_ids(["29808465"])` returns **the PMID alone — no DOI, no PMCID**
(verified 2026-09-21)."*

**`mcp__PubMed__get_article_metadata(["29808465"])`, run first-hand today, returns
`"doi":"10.1007/s10048-018-0549-5"`.** The queue **already carries that same DOI** twenty-six hundred
lines earlier, at [`full_text_queue_current.md:2899`](../research/full_text_queue_current.md), in a
row reading `| **29808465** | **null** | 10.1007/s10048-018-0549-5 | … |`.

⇒ The paper **has a DOI**. *"No DOI"* is a property of `convert_article_ids` — a PMC-backed
identifier converter that returns nothing for an article with no PMC deposit — and **not a property
of the paper**. 🔴 **A tool's silence was recorded as a fact about the world, and the queue now
contradicts itself in two places.** It does not change the verdict (`29808465` is still
`CURRENTLY UNRECOVERED`, §7), but a DOI is what an ILL form and a library proxy need, and
`FT-122` §2 tells a human to go and get this paper while the line above tells them there is no DOI
to ask for. **Not repaired here — reported with both line numbers.**

---

*Not medical advice. This page describes retrieval routes and what they return, and reports
genotype-class-level literature content from public sources. Every allele named above belongs to the
individual or family reported in its own source; alleles are never pooled across individuals,
populations or species, and same class is never same allele. No individual-level record is
reintroduced.*
