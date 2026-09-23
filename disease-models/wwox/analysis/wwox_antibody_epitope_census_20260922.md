# WWOX antibody epitope census — *does the reagent the design requires exist?*

**Actor:** Scientist E · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Status:** NON-CANONICAL ANALYSIS. This file touches no `*_current.md`, no registry, no queue, no
ledger, no receipt chain and no state manifest. No `BATCH_COMMIT` was run. No `git` command was
executed, not even read-only. No external contact and no purchase was made or initiated — contact,
purchase, quotation and any commercial commitment are `HUMAN_REQUIRED`.
**Nothing here is medical advice.** No molecule, dose, route or clinical recommendation appears below.
**Alleles are never pooled.** Each row is one reagent, or one measurement on one allele in one system.

> 🎯 **AMENDED IN PLACE 2026-09-23 by SCIENTIST 2** (`scientist-2`), on first-hand reading of the complete
> source bundle for `PMID 33914858` (Repudi *et al.* 2021, *Brain*) — a paper that had **zero receipts and
> zero full-text access** when this census was written. **Four additive edits, no deletion, no verdict
> reversed:** row **`A14`** (a third, primary-source attestation, and the authors' own `N.A`); blocker
> **`B2`** (inference → authorial declaration); blocker **`B3`** (second independent `MAB377` confirmation,
> plus its new cerebellar consequence); and **new blocker `B14`**. 🔴 **Untouched:** every `A1`–`A20`
> verdict, every count in §1.1, every epitope cell, the §2 design verdict, and §§4–7. **No new census row was
> created** — the anti-WWOX of `PMID 33914858` *is* `A14` (same laboratory, host, clonality and 1:5,000 IF
> dilution), and adding a row would inflate the `17` denominator that §§2.1 and 4.2 rest on. 🔴 **No epitope
> was gained; `0 / 17 wholly C-terminal to 230` stands.** Full rationale:
> [`repudi2021_complete_bundle_ingestion_20260923.md`](repudi2021_complete_bundle_ingestion_20260923.md) §D.5.

---

## 0 · PRE-REGISTERED TRACE — written and persisted BEFORE any confirmatory search

> 🔴 This section was written to disk in a single act, as the first content of this file, before a
> single external query was issued. Everything after `RESULT` in § 5 was added later. The ordering is
> the point: a prediction reconstructed after seeing evidence is not a prediction.

**OBSERVATION.** Three facts, all held in this repository before today's act:

1. [`wwox_missense_abundance_lysis_census_20260922.md`](wwox_missense_abundance_lysis_census_20260922.md)
   measured **0 / 12** published WWOX-missense abundance rows stating an antibody epitope position
   relative to the variant, and recorded the reason the gap could not be closed there:
   *"no vendor datasheet is reachable from this deployment"* → `EGRESS_BLOCKED`.
2. [`q230p_minimum_discriminator_20260922.md`](q230p_minimum_discriminator_20260922.md) then made
   **two antibodies with stated residue ranges flanking Q230** a *required component* of the minimum
   experiment — *"without it, blank and blind are the same lane"* — and registered as its own open
   item ⭐ 2: *"the epitope of any WWOX antibody, relative to residue 230 — `UNSTATED` in 12/12."*
3. 🔴 **And yet `discovery_ledger_current.md` line 623 already carries, from Tochigi 2019, the
   sentence** *"Reagenti riusabili: anti-Wwox Sigma **HPA050992** (epitopo aa 32-110, 100% identico
   nel ratto)"*. **A residue range for an anti-WWOX antibody has been sitting in the canonical
   discovery ledger, unconnected to the design that declares it missing.**

**DIVERGE — five framings, committed before evidence.**

| # | Framing |
|---|---|
| **D1** | The requirement is satisfiable off the shelf; HPA/PrEST-class antibodies publish residue ranges by program design, and WWOX may have several on both sides of 230 |
| **D2** | Half-satisfiable: the N-terminal member exists and is literature-attested; the C-terminal member is catalogue-only and therefore unverifiable here |
| **D3** | Unsatisfiable from any source reachable in this deployment ⇒ the required component is a wish and the design must be re-specified |
| **D4** | The requirement is the *wrong* requirement — a tagged construct, or a peptide-competition lane that maps the epitope empirically, is strictly cheaper and answers the same question |
| **D5** | The **denominator is wrong**: `0/12` is a statement about *abundance papers*, not about the antibody literature. Epitope information exists, but in a different paper class (histology, HPA/proteomics, antibody-characterisation) that an abundance census never enumerated |

**CONNECT.** The Human Protein Atlas raises its antibodies against **PrESTs** — Protein Epitope
Signature Tags — recombinant fragments deliberately chosen in *low-paralogue-homology* regions, and
the HPA record publishes the PrEST's residue range. `HPA050992` reaching a Methods section **with its
residue range attached** proves the retrieval channel that matters here is **the Methods section, not
the datasheet** — and Methods sections are reachable in this deployment while vendor pages are not.
The corollary is uncomfortable: the epitope question was never egress-blocked in the way the
abundance census concluded; it was **Methods-invisible**, which is a different failure with a
different remedy.

**HYPOTHESIS H1.** *The flanking pair is half-real.* The N-terminal member exists, is
literature-attested with an explicit residue range, and is already in this repository (`HPA050992`,
aa 32–110 — wholly N-terminal to 230). **No anti-WWOX antibody with a residue range stated wholly
C-terminal to residue 230 is identifiable from any source reachable in this deployment**, because
(i) PrEST design avoids the conserved Rossmann-fold SDR region, and (ii) the only route to a
C-terminal range for a non-HPA catalogue antibody is a vendor datasheet, and datasheets are blocked.

**PREDICTIONS — committed, numbered, before searching.**

| # | Prediction | Falsifier |
|---|---|---|
| **P1** | A whole-repository grep finds **exactly one** anti-WWOX antibody with a stated residue range, and it is N-terminal (`HPA050992`, 32–110) | Two or more; or one that is C-terminal |
| **P2** | The total number of **distinct** anti-WWOX primaries identifiable by catalogue number *or* unambiguous citation lineage, across repository + reachable literature, is **6–12** | <6 or >12 |
| **P3** | **≥ 60 %** of those have **no** stated epitope anywhere reachable | <60 % |
| **P4** | At least one further **HPA/PrEST-class** anti-WWOX antibody is findable, and its range is N-terminal or spanning — **not strictly C-terminal to 230** | A PrEST wholly within 231–414 |
| **P5** | Of published *"no detectable WWOX protein"* results, **< 40 %** are attributable to a **named** antibody; the rest are `NOT ATTRIBUTABLE` | ≥40 % attributable |
| **P6** | **≥ 1** *"absent protein"* result exists where a stable N-terminal fragment **could not** have been excluded (epitope C-terminal or unknown **and** lesion truncating the C-terminus) | Zero such results |
| **P7** | The single strongest **counter-example** — a paper that explicitly reasoned about its own epitope versus its own lesion — will be `PMID 19500159` (the *lde* rat), and it will state the relation **qualitatively, without residues** | It states residues; or another paper does it better |

**DISCRIMINATOR.** Only one observation separates **H1/D2** from **D1**: a literature-attested
anti-WWOX antibody whose **stated residue range lies wholly C-terminal to 230**. A catalogue number
alone does **not** count and will **not** be allowed to count — an unreachable datasheet is not a
stated range, and asserting what a datasheet "should contain" is the fabrication class this
laboratory has already had to quarantine once today. If ≥1 epitope-stated antibody is found outside
the 12 abundance rows, **D5 is supported and the `0/12` headline must be re-scoped**, not repeated.

**EXECUTION ORDER, fixed here:** (1) repository enumeration by `ls` then `grep` over all listed
files; (2) PubMed/PMC Methods retrieval; (3) `semanticSearch`; (4) scoring. No step reorders.

<!-- TRACE SEALED. Everything below this line was written after evidence. -->

---

## 1 · THE CENSUS

**Inclusion rule.** One row per distinct anti-WWOX **primary** reagent that appears in the WWOX
literature reachable from this deployment or anywhere in this repository. Tag antibodies (FLAG, myc)
get a row because two published abundance panels are read through them and their position relative to
230 is the whole question. Secondaries and non-WWOX markers are **not** census rows; they appear in
§3 where they block something.

**Epitope column rule, and it is strict.** `STATED` means a residue range, an exon range or a named
modification site **printed in a peer-reviewed body that was read in this act**. A catalogue number
is **not** an epitope. No datasheet was fetched, none could be, and **no epitope was inferred from a
catalogue number anywhere in this file.**

**Read depth.** `full-text` = body served and read in this act · `repo-held` = verbatim already in
this repository · `catalogue-listing` = surfaced by a prior session's search engine only, never in a
Methods section — carried as the weakest class and load-bearing for nothing.

### 1.1 The table

| # | Antibody | Catalogue · supplier | Host | Clonality | Immunogen / epitope, **verbatim** | Side of **230** | Validation | Applications attested | Source |
|---|---|---|---|---|---|---|---|---|---|
| **A1** ⭐ | anti-Wwox | 🟢 **`HPA050992` · Sigma-Aldrich** (Human Protein Atlas / PrEST class) | **rabbit** | polyclonal (PrEST) | 🟢 **STATED:** *"the new antibody, directed against **amino acids 32–110 of human Wwox protein**, a sequence **100% identical** to that of rat Wwox"* | 🟢 **N-TERMINAL** — ends 120 residues before Q230; lies in WW2 + the linker, wholly inside the `ww (1–110 a.a.)` construct boundary of `PMID 22193544` | 🟡 Biological negative: no normal-mobility band in `lde/lde` rat brain. **Not** a KO validation, **not** peptide-blocked | **WB** (1:1000) · **IHC-P** (1:1000) · **IF** on paraffin sections | Tochigi 2019, PMID 31340538, PMC6678113, [DOI](https://doi.org/10.3390/ijms20143596) — `full-text`, PMC XML |
| **A2** ⭐ | anti-WWOX, Aldaz-lab affinity-purified | 🔴 **in-house, no catalogue number** (MD Anderson) | rabbit | polyclonal, affinity-purified | 🟢 **STATED, two papers, one laboratory:** *"raised against WWOX **amino acid residues 16–93**[restored, see §1.2] that are identical between human and mouse"* · and *"affinity purified polyclonal antiserum raised against Wwox **amino acid residues 12–94**[restored — ⚠️ ambiguous, §1.2] that recognizes conserved domains"*. 🎯 **Plus an empirical map:** *"preadsorption of the antiserum to a GST fusion protein containing the **WWOX WW domains** completely eliminated immunohistochemical reactivity"* | 🟢 **N-TERMINAL** — and this is the one antibody in the census whose side of 230 is fixed **twice**, by a stated range *and* by a competition control | 🟢 **Protein-blocked** (preadsorption abolishes signal) + used on `Wwox^gt/gt` hypomorph and KO tissue | **WB** · **IHC** | Ludes-Meyers 2007, PMID 17823927, [DOI](https://doi.org/10.1002/gcc.20497) · Pimenta 2005, PMID 16152610, [DOI](https://doi.org/10.1002/ijc.21446) — both `full-text` |
| **A3** | anti-GST-Wwox antiserum, Huebner/Croce lineage | 🔴 **custom, Cocalico Biologicals — no catalogue number** | rabbit | polyclonal | 🟢 **STATED, but as a construct:** *"**the coding region of Wwox** was cloned into pGEX4T1 … GST-Wwox fusion protein was induced … The antiserum for GST-Wwox was produced in rabbit … by inoculating with GST-Wwox protein"* ⇒ immunogen = **full-length WWOX, aa 1–414** | 🔴 **SPANS 230 — and the epitope *within* the immunogen is UNMAPPED.** A full-length immunogen is not a flanking reagent: it tells you nothing about which fragment you are seeing | 🟢 *"titered for detection of Wwox in human cells with **intact or deleted `WWOX` genes**"*; IHC blocked by *"preincubation … with 0.5–1.0 µg of Wwox, cleaved from GST"* | **WB** (1:5,000–1:20,000) · **IHC** · **IP** context | Guler 2004, [DOI](https://doi.org/10.1002/cncr.20137) — `full-text` |
| **A4** | monoclonal anti-WWOX, Aqeilan lineage | 🔴 **in-house, identified only as** *"(Aqeilan et al., 2004a)"* | UNSTATED (monoclonal ⇒ presumptively mouse, **not stated**) | monoclonal | 🔴 **UNSTATED** — the reagent's identity is a **citation**, not a reagent | 🔴 **UNSTATED** | Used on `Wwox^−/−` tissue (a KO context), but no validation statement | **WB** | Abdeen 2013, [DOI](https://doi.org/10.1002/jcp.24308) — `full-text` |
| **A5** | anti-WWOX, ProteinTech | 🟡 **supplier named, catalogue number NOT given** | UNSTATED | UNSTATED | 🟢 **STATED by exon range:** *"an antibody raised against a peptide translated from **exons 1–7**[restored, §1.2] (ProteinTech)"* ⇒ **aa 1–≈280** by this repository's own boundary map | 🔴 **SPANS 230** (exon 7 = `c.606–≈840` = aa ≈202–280; `c.689`/Q230 sits inside it) | 🟢 Isoform-discriminating on human fibroblasts; resolves the 46 kDa long isoform from the WW-only short isoform | **WB** | Davids 2019, PMID 30362252, [DOI](https://doi.org/10.1002/humu.23675) — `full-text` |
| **A6** ⭐ | anti-WWOX, Abcam | 🟡 **supplier named, catalogue number NOT given** | UNSTATED | UNSTATED | 🟢 **STATED by exon range:** *"one raised against a peptide translated from **exons 1–5**[restored, §1.2] (Abcam)"* ⇒ **aa 1–172** (exon 5 ends `c.516`) | 🟢 **N-TERMINAL** — stops 58 residues before Q230 | 🟢 Same blot as A5; the two together resolved which isoform was lost | **WB** | Davids 2019, same source |
| **A7** | anti-WWOX | 🟢 **`ab238144` · Abcam** | UNSTATED | UNSTATED | 🔴 **UNSTATED.** *"Anti-WWOX antibody (#ab238144) was purchased from Abcam (Cambridge, UK)"* is the whole description | 🔴 **UNSTATED** — datasheet `EGRESS_BLOCKED` | none stated | **WB** (and an IF panel in the same paper, assignment not stated) | Zhang 2025, PMID 41124647, [DOI](https://doi.org/10.1002/advs.202507602) — `full-text` |
| **A8** | anti-WWOX | 🟢 **`ab189410` · Abcam** | UNSTATED | UNSTATED | 🔴 **UNSTATED** | 🔴 **UNSTATED** | 🟡 Isotype control only (*"monoclonal Rabbit IgG … `ab172730`"*) — an isotype control is **not** a specificity control | **IHC** (1:100) | HCC immunohistochemistry study 2018 — 🔴 first author not captured by the retrieval, cited by DOI only, [DOI](https://doi.org/10.1002/cam4.1591) — `full-text` |
| **A9** | anti-WWOX total | 🟢 **`ABN413` · Merck Millipore** | UNSTATED | UNSTATED | 🔴 **UNSTATED** | 🔴 **UNSTATED** | 🔴 none — and see §3, blocker **B6** | listed in Methods; **no WWOX result was ever reported from it** | `repo-held`: `paper_registry_current.md:7241`, PMID 35984507 |
| **A10** | WWOX Protein Antibody | 🟢 **`4045S` · Cell Signaling Technology** | UNSTATED | UNSTATED | 🔴 **UNSTATED** — `cellsignal.com` `EGRESS_BLOCKED` | 🔴 **UNSTATED** | none stated | **WB** (human total cell lysate) | `repo-held`: abundance census row 8, PMID 42082822 |
| **A11** | anti-WWOX (phospho-Y33) | 🟢 **`ab193624` · Abcam** | UNSTATED | UNSTATED | 🟡 **PARTIAL — the modification site is the epitope anchor: `Y33`**. The surrounding immunogen range is UNSTATED | 🟢 **N-TERMINAL** (Y33 sits in WW1) — 🔴 but it detects **only the phosphorylated form**, so it can never serve as the N-terminal member of an abundance pair | none stated | **WB** | `repo-held`: `paper_registry_current.md:7241`, PMID 35984507 |
| **A12** | anti-WWOX (phospho-Y33) | 🟢 **`ab129881` · Abcam** | UNSTATED | UNSTATED | 🟡 same as A11 | 🟢 N-terminal, same caveat | none | — | 🔴 **`catalogue-listing` only** (`wwox_activity_sensor_census_20260921.md:239`). Never seen in a Methods section |
| **A13** | anti-WWOX total | 🟢 **`ab216660` · Abcam** | UNSTATED | UNSTATED | 🔴 **UNSTATED** | 🔴 **UNSTATED** | none | — | 🔴 **`catalogue-listing` only**, same source. Load-bearing for nothing |
| **A14** | rabbit polyclonal anti-WWOX (the TX-007 / AAV-series primary) | 🔴 **NO catalogue number, NO supplier, NO clone** — 🎯 **and the authors themselves now print the absence:** the Supplementary Table 3 of `PMID 33914858` gives `Rabbit anti-WWOX \| 1:5000 \| Catolog No **N.A** \| Source *(cell left empty)*`, in a table whose `Catolog No` column is populated for **nine** other primaries | rabbit | polyclonal | 🔴 **UNSTATED** | 🔴 **UNSTATED** | 🟢 Implicit: gives no signal in `Wwox`-null brain — but that is an observation, not a declared validation | **WB** (1:10,000) · **IHC / IF** on mouse brain (**1:5,000**) — 🟢 the 1:5,000 IF dilution is now attested **three times, in three papers, by one laboratory** | `repo-held`: `cerebellum_layer_localisation_20260922.md` §3.4–3.5, `purkinje_existing_material_experiment_20260922.md` §2.3 · 🎯 **+ `full-text`, added 2026-09-23:** `PMID 33914858` (Repudi 2021, *Brain*) Supplementary Table 3, read first-hand from `files/fulltext/PMID33914858_Repudi2021_suppl_File014_reagents.xlsx` → [`repudi2021_complete_bundle_ingestion_20260923.md`](repudi2021_complete_bundle_ingestion_20260923.md) §D.1 |
| **A15** | in-house rabbit polyclonal anti-WWOX / WOX1, Chang (NCKU) lineage | 🔴 **no catalogue, no lot** | rabbit | polyclonal | 🔴 **UNSTATED** | 🔴 **UNSTATED** | 🔴 **None reported — and the paper had a `Y33R` mutant in hand and never blotted it** | WB · IF / FRET series | `repo-held`: `c1q_wwox_mechanism_audit_20260921.md:108` |
| **A16** | *"polyclonal rabbit-anti-human-WWOX antibody **developed in the laboratory**"* (Adelaide) | 🔴 **no catalogue** | rabbit | polyclonal | 🔴 **UNSTATED** | 🔴 **UNSTATED** | none stated | **WB** | FRA16D / metabolic-reprogramming study 2013 — 🔴 first author not captured by the retrieval, cited by DOI only, [DOI](https://doi.org/10.1002/gcc.22078) — `full-text` |
> ### 🎯 `A17` ≡ `A21` — ONE antibody, established 2026-09-23
>
> The *lde*-rat antibody this census carried as **"unnamed"** is **Santa Cruz `sc-20528`**, i.e. the same
> catalogue item as `A21`. Verbatim, Suzuki 2009 *Genes Brain Behav* 8(7):650–660 Methods:
> *"the membranes were incubated with **goat anti-Wwox polyclonal antibody (1:100; sc-20528, Santa Cruz
> Biotechnology**…), followed by … **Alexa Fluor 680-conjugated rabbit anti-goat** IgG."* Catalogue number,
> vendor, host and secondary all match `A21`.
>
> **Three consequences, kept separate:**
> 1. 🟢 **`sc-20528` is goat polyclonal — now `DATO`**, not entailed from a secondary.
> 2. 🟡 **It DOES have an epitope statement — a negation, and a weak-provenance one.** *"The Wwox epitope
>    bound by the anti-Wwox antibody used in this study **did not contain the region altered by the `lde`
>    mutation** (personal communication from Santa Cruz Biotechnology)."* 🔴 **That excludes only roughly
>    the last ~44 residues and says NOTHING about residue 230.** It remains unusable for a flanking design.
> 3. 🔴 **The reagent behind `Q230P`'s founding negative is the reagent with a documented in-print false
>    negative.** §4.1 rows 2→3: with this antibody, in the `lde` rat, *"both products were **undetectable**"*;
>    a later study of the same model using `HPA050992` (aa 32–110) detected *"a **very weak band** of
>    slightly lower mobility."* 🔴 **The authors attribute that to sensitivity; nobody has tested it.**
>    `IPOTESI`, not `DATO` — and §3 of
>    [`q230p_spt_executability_and_exon7_20260923.md`](q230p_spt_executability_and_exon7_20260923.md)
>    tests it for free by running both antibodies on one membrane.
>
> **The two rows are retained below rather than deleted**, so the provenance of each statement stays
> visible; they are **one reagent** and must be counted once.

| **A17** | anti-Wwox, *lde*-rat 2009 | 🔴 **unnamed** | UNSTATED | UNSTATED | 🟡 **STATED QUALITATIVELY, NOT BY RESIDUE:** *"Because the antibody used for Western blot analysis **does not recognize the C-terminal amino acid sequence** of Wwox protein…"* · and, in the sibling body already in this repository, *"The Wwox epitope bound by the anti-Wwox antibody used in this study **did not contain the region altered by the `lde` mutation**"* | 🟡 **NOT C-TERMINAL** — the only *negative* epitope statement in the literature, and it is unusable for a flanking design because it gives no boundary | 🟢 The epitope-vs-lesion argument is itself the validation, and it is the best epistemic practice in this census | **WB** | Suzuki 2009, PMID 19500159, [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x) — `full-text` + `repo-held` dossier |
| **A18** | anti-FLAG **M2** | 🟢 **`F1804` · Sigma-Aldrich** | mouse | monoclonal (clone M2) | 🟢 Epitope = the **FLAG tag**, not WWOX | 🔴 **UNRESOLVABLE:** vector is *"pCMV-3Tag (#240195, Agilent)"*; the 3Tag family has **both N- and C-terminal members and the paper does not say which** ⇒ the tag's side of 230 is `UNSTATED` | n/a | **WB** · **IP** · **IF** | `repo-held`: abundance census §2.3, PMID 41124647 |
| **A19** | anti-myc (myc-WWOX) | UNSTATED | UNSTATED | UNSTATED | Epitope = the **myc tag** | 🔴 construct terminus UNSTATED in the preprint | n/a | **IF** — adopted *because* commercial anti-WWOX failed (§3, **B1**) | `repo-held`: `batch_queue.md:459`, preprint `42523332` |
| **A20** | anti-**C-DmWWOX** | — | — | — | Raised against the **C-terminus of the *Drosophila* WWOX ortholog** | ❌ **OUT OF SCOPE** — not human WWOX. Listed only so a future keyword sweep for *"C-terminal WWOX antibody"* does not mistake it for one | — | — | `repo-held`: `adelaide_node_discriminator_20260921.md:71` |

| **A21** 🎯 | anti-WWOX — **the antibody that produced `Q230P`'s founding Western blot** | 🟢 **`sc-20528` · Santa Cruz Biotechnology, Dallas TX** — printed in the source as `sc20,528` (the typesetter inserted a thousands comma; a search for `sc-20528` returns an **unearned zero**) | 🟡 **goat** — not stated directly, but entailed by the paper's own secondary, *"1:30,000 **anti-goat** IgG HRP"* | UNSTATED | 🔴 **UNSTATED** — no immunogen, no aa range, no clone anywhere in the paper | 🔴 **UNSTATED** | 🟢 **Strong for specificity, absent for sensitivity:** three CRISPR/Cas9 `WWOX` knock-out PaTu-8988t clones (`sc-403070`) as a true negative, plus three independent positive-control lines (PaTu-8988t, SW620, **HEK293**). 🔴 **No dilution series, no standard, no LOD** | **WB** (1:200; 20–40 µg on 12% SDS-PAGE, PVDF, ECL, band at ~46 kDa) | Johannsen 2018, PMID 29808465, [DOI](https://doi.org/10.1007/s10048-018-0549-5) — `full-text`, read 2026-09-23 → [`johannsen2018_fulltext_q230p_revival_20260923.md`](johannsen2018_fulltext_q230p_revival_20260923.md) §1.1 |

> 🎯 **`A21` closes a named blocker.** `q230p_true_frontier_20260922.md` row `DET-1` read: *"Which
> antibody produced `Q230P`'s founding blot, and where is its epitope? **`NOT ATTRIBUTABLE`. No
> vendor, no catalogue, no clone, no host, no immunogen."* **Vendor, catalogue and host are now
> known.** `DET-1` moves `NOT ATTRIBUTABLE` → **`ATTRIBUTED, EPITOPE UNKNOWN`**, and the epitope is
> now a **one-lookup** question against a real catalogue number rather than an unanswerable one.
> 🔴 **It does not move `DET-4`:** a knock-out negative control establishes that the band is WWOX; it
> says nothing about how little WWOX would still have been seen.

**Counts.**

| | |
|---|---|
| Distinct **anti-WWOX primary** reagents censused (A1–A17 + A21, excluding tags A18–A19 and the fly A20) | **17** 🎯 *(2026-09-23, second pass: `A21` was added (+1), then `A17 ≡ A21` was established (−1). **Net 17**, and the two rows are ONE reagent — see the merge note above `A17`.)* |
| With an **epitope stated by residue range** | **3** — A1 (32–110), A2 (≈12/16–93/94), A3 (1–414, full-length) |
| With an **epitope stated by exon range** | **2** — A5 (exons 1–7), A6 (exons 1–5) |
| With an **epitope anchored to a modification site only** | **2** — A11, A12 (`pY33`) |
| With an **epitope stated only as a negation** | **1** — **`A17 ≡ A21` = `sc-20528`** (*"does not recognize the C-terminal…"* / *"did not contain the region altered by the `lde` mutation"*). 🔴 **This class now contains the antibody that produced `Q230P`'s founding negative.** Its provenance is a **2009 vendor personal communication**, not a datasheet and not an experiment |
| 🔴 With **no epitope information of any kind** | **9 / 17 = 53 %** 🎯 *(`A21` no longer counts here: as `A17` it carries a negation-class statement)* |
| 🟢 Whose epitope is **wholly N-terminal to 230** | **3** — A1, A2, A6 (+ A11/A12, phospho-restricted) |
| 🔴 Whose epitope is **wholly C-terminal to 230** | 🔴 **0 / 17. None. Not one.** 🎯 *(denominator corrected twice in one day; **the zero has never moved**)* |
| Whose epitope **spans 230** | **2** — A3, A5 |
| With **no catalogue number at all** | **6** — A2, A3, A4, A14, A15, A16. 🎯 *(`A17` leaves this class: it is `sc-20528`, printed in Suzuki 2009's Methods)* |
| **Knockout-validated** in the strict sense (signal absent in a genetic null of the epitope region) | **1** — A2 (hypomorph + KO tissue, same laboratory) |
| **Peptide/protein-blocked** (competition control published) | **2** — A2, A3 |
| With published **intracellular-flow-cytometry** validation | 🔴 **0** (carried forward from `wwox_activity_sensor_census_20260921.md`) |

### 1.2 🔴 Extraction damage, declared before it is used

Three of the five epitope ranges above arrive through a text layer that **deletes en dashes**. This
is the damage class this session has already paid for once (`goat anti-rabbit Alexa 647 ()`), and it
is handled here by restoration-with-argument, never by silent correction.

| Raw string as served | Restorations arithmetically possible | Restoration taken | Why it is forced, or not |
|---|---|---|---|
| `amino acid residues 1693` | `16–93` · `1–693` · `169–3` | 🟢 **`16–93`** | WWOX is **414 aa**. `1–693` and `169–3` are impossible. **Forced.** |
| `peptide translated from exons 17` | `1–7` · `17` | 🟢 **`1–7`** | WWOX has **9 exons**. There is no exon 17. **Forced.** |
| `peptide translated from exons 15` | `1–5` · `15` | 🟢 **`1–5`** | Same. **Forced.** |
| `amino acid residues 1294` | `12–94` · `1–294` · `129–4` | 🟡 **`12–94`, with the alternative carried** | `129–4` is impossible. **`1–294` is NOT impossible** and would make A2 **span 230**. Two independent arguments favour `12–94`: (i) the same laboratory prints `16–93` for the same reagent in a sibling paper; (ii) 🎯 **the preadsorption control is decisive** — *"preadsorption … to a GST fusion protein containing the WWOX **WW domains** completely eliminated immunohistochemical reactivity."* An antibody whose reactivity is **completely** abolished by the WW domains alone has no functional epitope C-terminal to ≈110, whatever the immunogen's nominal length. 🔴 **The residual ambiguity is recorded, not closed by assertion**, and A2's row survives on the competition control rather than on the digits. |

---

## 2 · THE DESIGN VERDICT

### 2.1 The answer, plainly

> 🔴 **NO. A pair of anti-WWOX antibodies with stated residue ranges flanking Q230 does not exist in
> any source reachable from this deployment. The N-terminal half of the pair exists, is excellent, and
> has been in this repository's own canonical discovery ledger since it was written. The C-terminal
> half has no candidate at all — not a weak one, not an unverified one. Zero of seventeen.**

**The N-terminal member — name it and stop re-deriving it.**

> **`HPA050992`, Sigma-Aldrich, rabbit polyclonal, immunogen `aa 32–110` of human WWOX,
> 100 % identical in rat, attested for WB *and* IHC *and* IF in rodent brain at 1:1000.**

It is the best-characterised anti-WWOX reagent in the literature by the only criterion this design
cares about, and its residue range is printed **in a peer-reviewed Methods section**, not on a
datasheet — so it is reachable here and always was.

**Runner-up N-terminal member, if a second N-terminal channel is wanted:** the **Abcam exons-1–5**
antibody of Davids 2019 (aa 1–172). 🔴 Its catalogue number is not in the paper, so ordering it
requires either author correspondence or a vendor search — both `HUMAN_REQUIRED`.

**The C-terminal member: `COULD NOT ESTABLISH`.** Four reagents *could* be C-terminal and not one
says so: `ab238144`, `CST 4045S`, `ABN413`, `ab189410`. Every route to their epitopes is a vendor
datasheet and **every vendor datasheet is `EGRESS_BLOCKED` in this deployment**. 🔴 This file will
not say what those pages "should" contain.

### 2.2 The nearest achievable substitutes, ranked

| # | Substitute | What it buys | What it costs | Verdict |
|---|---|---|---|---|
| **S1** 🥇 | **`HPA050992` (aa 32–110) + a C-terminal epitope tag on the expressed allele**, with the **size** of every band scored, not just its presence | A *known* C-terminal read. An N-terminal fragment is anti-WWOX⁺ / anti-tag⁻; full-length is double-positive; nothing made is double-negative | Requires a construct ⇒ only works on the heterologous arm, **not** on patient fibroblasts. Carries the design's own failure mode `F8` (intact tag at anomalous size) | 🟢 **Adopt for the transfected arm.** Specify the tag terminus in writing — the one thing `PMID 41124647` failed to do (A18) |
| **S2** 🥇 | **Map the epitope empirically by fragment competition.** Preadsorb each candidate C-terminal antibody against two GST fusions — `ww (1–110 a.a.)` and `ADH (110–414 a.a.)`, **both already defined verbatim by `PMID 22193544`** — and see which one abolishes the signal | 🎯 **Converts an unreachable datasheet into a measured fact.** Turns *"which side of 230"* from a purchasing question into a bench question, and the answer is publishable | Two bacterial preps, two blots, one afternoon. No egress, no vendor, no correspondence | 🟢 **Adopt, and adopt it whatever else is decided.** This is not a workaround: `PMID 16152610`'s laboratory ran exactly this control in 2005 (A2) and it is why A2 is the only antibody in the census whose side of 230 is fixed twice. **The method the field already has, unused for twenty years.** |
| **S3** | **Antibody-free denominator:** targeted MS (PRM/SRM) with heavy internal standards on **two** tryptic peptides, one N-terminal and one C-terminal to 230 | Absolute copy number per species, epitope-independent, fold-independent | Instrument access, method development, ~10³–10⁴ EUR class | 🟡 **Right answer, wrong budget for a discriminator.** Already carried as `T8` in `wwox_sdr_function_per_molecule_census_20260921.md` |
| **S4** | **Two N-terminally-anchored antibodies of different reach** — A6 (aa 1–172) + A5 (aa 1–≈280) — the Davids 2019 configuration | 🟢 **Published precedent that the logic works**: it resolved a long isoform from a WW-only short isoform on one blot | 🔴 Both are anchored at aa 1, so they bracket a **lesion between 172 and 280** and nothing else. For `Q230P`, a point substitution, they discriminate almost nothing | 🟡 **Cite as precedent, do not adopt as the pair** |
| **S5** | Buy a C-terminal antibody on a vendor's word | — | — | 🔴 **REJECT.** An unread datasheet is not a stated epitope, and this session will not manufacture one. Escalate as `HUMAN_REQUIRED`: one person, one browser, ten minutes |

### 2.3 What this does to the minimum experiment

The component in `q230p_minimum_discriminator_20260922.md` §1.8 — *"epitope stated by residue range,
flanking Q230"* — is **not purchasable as written**. It becomes purchasable if it is rewritten as:

> **one antibody with a published residue range N-terminal to 230 (`HPA050992`, aa 32–110) plus a
> C-terminal read whose position is established by the experimenter — an epitope tag (S1) or a
> fragment-competition map (S2) — and never by a catalogue page nobody opened.**

🔴 **The design's underlying claim is untouched and survives intact.** *"Without it, blank and blind
are the same lane"* is not weakened by this census — §4 shows it happening in print. What changes is
the procurement line, from *"buy two antibodies"* to *"buy one and map the other."*

---

## 3 · THE REPOSITORY'S REAGENT BLOCKERS, GATHERED

| # | Blocker | Verbatim / source | What it blocks |
|---|---|---|---|
| **B1** | 🔴 **Commercial anti-WWOX antibodies fail in immunofluorescence.** | *"Commercial anti-WWOX antibodies did not show any specific signal for IF prompting us to use a myc-WWOX for localization studies."* — preprint `42523332`, `batch_queue.md:459` | **Every endogenous-localisation readout.** Aggregate-vs-diffuse, aggresome scoring, lysosomal colocalisation on **patient** cells. A tagged construct is the only route left, and a tag is not the endogenous allele |
| **B2** | 🔴 **The `TX-007` / AAV-series anti-WWOX primary has no identity.** *"rabbit polyclonal anti-WWOX 1:5,000"* and *"1:10,000"* — **no supplier, no catalogue, no clone, no lot**, and the parenthetical is **missing entirely rather than emptied**, so the omission is the authors', not the extractor's. 🎯 **UPGRADED 2026-09-23 from inference to authorial declaration.** The forensic argument above is no longer load-bearing: the same laboratory's Supplementary Table 3 in `PMID 33914858` prints `Rabbit anti-WWOX \| 1:5000 \| **N.A**` in a **structured `.xlsx`** — no text layer, nothing to corrupt, nine sibling rows populated. 🔴 **The authors declare the catalogue number to be not applicable.** The reagent is in-house and has been in-house across at least three papers | `cerebellum_layer_localisation_20260922.md` §3.4–3.5; `purkinje_existing_material_experiment_20260922.md` V3 · 🎯 **+ `PMID 33914858` Suppl. Table 3** → [`repudi2021_complete_bundle_ingestion_20260923.md`](repudi2021_complete_bundle_ingestion_20260923.md) §D.1, §D.5 | **Every absolute WWOX magnitude in the AAV dose series**, and any cross-species fold-of-WT (human transgene protein vs mouse Wwox, 93 % identical, affinity ratio unstated). Within-field *relative* contrasts survive. ⚠️ **Now also blocks reproduction of `PMID 33914858`'s WWOX immunofluorescence**, including its cerebellar panel (Suppl. Fig. 1B) |
| **B3** | 🔴 **`MAB377` is NeuN clone A60, and clone A60 does not label Purkinje cells.** 🎯 **CONFIRMED 2026-09-23 in a second, independent paper:** Supplementary Table 3 of `PMID 33914858` lists `Mouse anti-NeuN \| 1:500 \| **MAB377** \| Millipore` — the same catalogue number, read first-hand from the authors' own structured reagent table | `full_text_queue_current.md:6723` · 🎯 **+ `PMID 33914858` Suppl. Table 3** → [`repudi2021_complete_bundle_ingestion_20260923.md`](repudi2021_complete_bundle_ingestion_20260923.md) §D.1, §C.4 | Any cerebellar `NeuN⁺WWOX⁺` percentage is a **granule-cell** measurement. Purkinje and basket cells are structurally excluded from the denominator. 🎯 **NEW CONSEQUENCE:** `PMID 33914858` **Supplementary Fig. 1B** — *"cerebellum … in N-KO, N-Control at P16. Neuronal nuclei stained with anti-NeuN antibody"* — is the **only cerebellar anti-WWOX image in that paper**, and its identity channel is Purkinje-blind by this same reagent. A cerebellar WWOX panel now exists in a **Nestin-Cre conditional** and still cannot name a Purkinje cell |
| **B4** | 🔴 **Host-species collision across the whole image archive.** Four **rabbit** primaries (WWOX, GFAP, Iba1, MBP) share **one** anti-rabbit secondary; two **mouse** primaries (βIII-tubulin, NeuN `MAB377`) share one anti-mouse. **Three channels exist, ever** | `purkinje_existing_material_experiment_20260922.md` §2.3, V1 | A WWOX section can carry **no** glial and **no** myelin marker. And — the correction this file inherits — **calbindin (mouse) and NeuN (mouse) cannot sit on the same section**, so a Purkinje stain cannot cross-calibrate against the existing NeuN-gated figure without a third measurement |
| **B5** | 🟡 **Extraction deleted a secondary's catalogue number**: *"goat anti-rabbit Alexa flour 647 **()**, Abcam"* beside a populated *"(ab150117)"* | same, V3 | Nothing scientifically — but it is the calibration case for §1.2. **An empty parenthesis is a deleted number, not an absent one**, and the two damage patterns being *different* is what proves B2 is authorial |
| **B6** | 🔴 **A total-WWOX antibody was bought and no total-WWOX result was ever reported.** The antibody table lists **both** `Anti-WWOX (phospho Y33) Abcam (ab193624)` **and** `WWOX Merck Millipore (ABN413)`, and normalisation is *"β-actin was used as a loading control"* | `paper_registry_current.md:7241`; PMID 35984507 | Any **pWWOX / total-WWOX ratio**. A phospho signal with no denominator cannot distinguish *"more phosphorylation"* from *"more protein"* — and the reagent to settle it was on the shelf |
| **B7** | 🔴 **`CST 4045S`, `ab238144`, `ab189410`, `ABN413`: epitope unverifiable here.** Every vendor datasheet is `EGRESS_BLOCKED` | abundance census §1.3; this file §2.1 | The C-terminal member of the flanking pair. **This is the single blocker that converts §2's answer from "yes" to "no"** |
| **B8** | 🔴 **The Aqeilan-lineage monoclonal is a citation, not a reagent** — *"monoclonal anti-WWOX (Aqeilan et al., 2004a)"* | [DOI](https://doi.org/10.1002/jcp.24308) | Anyone reproducing the Aqeilan-lab WWOX blots must chase a 2004 reference to find out what they are buying, and the immunogen is still not stated at the end of the chain |
| **B9** | 🔴 **Reagent provenance runs into a standing expression of concern.** In `PMID 18460020`, *"Ad-WWOX, Ad-GFP, immunoblot anti-Wwox and IHC anti-Wwox"* are **all** cited to ref 21 = `PMID 16223882`, which carries a standing expression of concern (`PMID 28373548`) | `paper_registry_current.md:7008`; `CC-20260909-18460020-01.md` | ⚠️ **Bounded, and the bound must travel.** The concern's declared scope is **one loading-control panel** of the cited paper. It does **not** impugn the antibody or the adenovirus. Treating it as reagent invalidation is the overreach the wave-3 reading was already corrected for |
| **B10** | 🔴 **An in-house antibody with a specificity control the authors could have run and did not.** The Chang/NCKU anti-WOX1 polyclonal has no catalogue, no lot and no specificity control — *"The paper has a `Y33R` mutant in hand. It never blots or stains `Y33R`"* | `c1q_wwox_mechanism_audit_20260921.md:108` | The entire FRET/localisation series from that laboratory inherits an unvalidated primary, on top of the open `conflicting evidence` flag already recorded against its localisation claims |
| **B11** | 🔴 **The tag terminus is unstated where it is load-bearing.** *"pCMV-3Tag (#240195, Agilent)"* — the 3Tag family has N- **and** C-terminal members and the paper never says which | abundance census §2.3; PMID 41124647 | The only published WWOX-missense **turnover** dataset. If the FLAG is C-terminal, a stable N-terminal fragment is invisible in every lane of the `P252A` CHX chase. 🔴 **Unresolvable as published** — and §4 row 9 turns this from a caveat into a blocker |
| **B12** | 🔴 **No anti-WWOX antibody has published intracellular-flow validation**, and WWOX has never been in a cytometry panel even at CyTOF resolution | `wwox_activity_sensor_census_20260921.md` §4.4 | Any pooled, sort-based or per-cell-quantitative WWOX abundance assay |
| **B13** | 🟡 **Whether any anti-WWOX antibody works for immunoprecipitation from primary fibroblast lysate was never checked**, although it gates a 10³–10⁴ EUR experiment | `proteostasis_discrimination_protocols_20260922.md:169` | Rank-4 of the proteostasis protocol set. Partially answered here: **A3's lineage is used in IP contexts and A18 (`M2`) is the workhorse**, but neither is attested on *primary fibroblast* lysate |
| **B14** 🆕 | 🔴 **A published reagent table that cannot account for its own published figures.** Supplementary Table 3 of `PMID 33914858` lists **exactly three** secondaries — `Goat anti-Mouse AF488 (A11029)`, `Goat anti-Mouse AF647 (A21244)`, `Donkey anti-Rat Cy5 (712-175-150)` — and 🔴 **no anti-rabbit secondary of any kind**, although **four** of its ten primaries are rabbit (anti-WWOX, anti-MBP `Ab65988`, anti-NG2 `AB5320`, anti-GFAP `MAB360`) and **every one of them is imaged in a published panel of that same paper**. 🎯 This is a strictly stronger statement than the usual *"the Methods do not say"*: the figures **prove** a reagent was used that the table omits. No nuclear counterstain (DAPI/Hoechst) is listed either, and the IF Methods name none. ⚠️ Two further **unresolved** host/catalogue flags in the same table: `Rabbit anti-GFAP` assigned `MAB360` and `Rat anti-NF-H` assigned `MAB5448`, where the Millipore `MAB` prefix denotes a mouse monoclonal — 🔴 **raised, not resolved; no datasheet was consulted (`B7`) and nothing in this census depends on it** | 🎯 Added 2026-09-23 · `files/fulltext/PMID33914858_Repudi2021_suppl_File014_reagents.xlsx`, read first-hand → [`repudi2021_complete_bundle_ingestion_20260923.md`](repudi2021_complete_bundle_ingestion_20260923.md) §D.2–§D.4 | **Reproducibility of every immunofluorescence panel in `PMID 33914858`** — including the cerebellar WWOX panel (Suppl. Fig. 1B) and the cerebellar CNP/MBP and CC1/NG2 panels. 🟡 Also bounds the channel arithmetic that `B4` fixes for the EMBO/2026 archive: this paper has **two** anti-mouse secondaries in **different** channels (488 and 647), not one — so its geometry is **not** the *"three channels exist, ever"* of `B4` and the two archives must not be pooled. 🟢 **What it does NOT disturb:** calbindin (mouse) still cannot share a section with NeuN `MAB377` (mouse), so `P4`'s third-measurement cost stands unchanged |

---

## 4 · COULD A STABLE N-TERMINAL SPECIES HAVE BEEN MISSED?

**The mechanism, stated once.** If an antibody's epitope lies C-terminal to a lesion that truncates
or destabilises the C-terminus, a protein that is present, N-terminally intact, and possibly
partially functional reports as **absent**. The failure is silent, it looks like a clean negative, and
it is indistinguishable from a real null **unless a second epitope on the other side is read.**

### 4.1 Row by row

| # | Result, verbatim | Antibody | Epitope | Lesion class | **Could an N-terminal species have been missed?** |
|---|---|---|---|---|---|
| **1** ⭐ | `Q230P`: *"normal levels of WWOX transcripts but **absence of WWOX protein**"* | 🔴 **NOT ATTRIBUTABLE** — `METHODS_INVISIBLE`, Springer-closed, no vendor, no clone, no host, no immunogen | 🔴 unknown | **missense** at 230, inside the SDR | 🔴 **YES, AND NOTHING EXCLUDES IT.** A point substitution does not truncate, so a *fragment* is not the leading hypothesis — but a **fold-dependent epitope loss** in the SDR is, and it is unexcludable with an unknown epitope. 🔴 **The allele this laboratory exists to reason about rests on a blot whose antibody nobody can name.** |
| **2** | `lde/lde` rat: *"both products were **undetectable** in the testes and hippocampi"* | A17, unnamed | 🟡 *"does not recognize the C-terminal amino acid sequence"* | **C-terminal frameshift**, `p.Leu371Thrfs*53` — the N-terminus is intact by construction | 🟡 **NO, in principle** — the epitope is on the surviving side, so a fragment should have shown. 🔴 **YES, in practice** — see row 3 |
| **3** 🎯 | Same rat, ten years later: *"a **very weak band of slightly lower mobility** was detected"* at 46.2 kDa, *"which may have been due to **greater sensitivity of the new antibody, directed against amino acids 32–110**"* | **A1 `HPA050992`** | 🟢 **aa 32–110, N-terminal** | same | 🔴 **IT WAS MISSED, AND THEN IT WAS FOUND.** A published *"no protein"* became *"present, faint, N-terminally intact"* **by changing the antibody and nothing else.** This is the census's decisive datum: it is not a hypothetical failure mode, it is a documented one, in the closest animal model of the splice-null side of the reference genotype, and the repair was an epitope-stated N-terminal antibody |
| **4** 🎯 | `WWOX` exon-6 microdeletion, human fibroblasts: *"**loss of the longer isoform** …, which contains the short-chain dehydrogenase/reductase domain, and the **increased expression of the shorter isoform** …, which only contains the WW-domains"* | **A5** (exons 1–7) **+ A6** (exons 1–5), same blot | 🟢 aa 1–≈280 **and** aa 1–172 | **exon deletion** `c.517_605del` | 🟢 **NO — and this is the positive control for the whole design.** An N-terminal species was not merely *not missed*; it was **detected, named and shown to increase**, because both antibodies were N-terminally anchored. 🔴 The paper never calls this an epitope argument. It simply had the right reagents |
| **5** | `Wwox` KO mouse: *"Wwox protein expression is **abolished** … using Wwox specific antibodies"* | **A2**, Aldaz lineage | 🟢 aa ≈16–93 | **exon 1 floxed out** | 🟢 **NO.** The epitope sits inside the deleted region, so there is no N-terminal species to miss. Coincidentally sound |
| **6** | `G372R` organoids: *"**barely any signal** was observed in WPM D1 and S1"* | 🔴 **NOT ATTRIBUTABLE** — the antibody table is an appendix PMC does not distribute; the citation callout was deleted by extraction | 🔴 unknown | **missense** at 372, far C-terminal | 🔴 **YES.** `G372R` is the allele in this set most likely to destabilise the C-terminus specifically. With an unknown epitope, *"barely any signal"* cannot be separated from *"C-terminal epitope lost"* — nor, as the abundance census showed, from epitope masking inside an aggregate at 0.1 % Triton with no antigen retrieval |
| **7** | `A141T`: *"significantly reduced WWOX protein levels"* | **A10 `CST 4045S`** — 🟢 named, 🔴 epitope unstated, datasheet blocked | 🔴 unknown | **missense** at 141 | 🟡 **YES, weakly.** Named reagent, unknown epitope. The lesion is N-terminal to the SDR and does not predict truncation, so the fragment scenario is not the leading one — but the record does not exclude it, and *"significantly"* here carries no test, no densitometry and no replicate count |
| **8** 🎯 | Oral SCC: *"Products of the aberrant transcripts … **were not seen**, suggesting that these aberrant transcripts were not translated into protein **or, less probably, that the proteins synthesized were being quickly degraded**"* | **A2** | 🟢 WW domains, N-terminal, **confirmed by preadsorption** | **internal exon loss** (exons 6–8, exon 7) — **the N-terminus is preserved** | 🟢 **NO — and the negative is therefore strong.** An N-terminally intact internal-deletion product would have been visible to this antibody. This is the only *"absent"* in the census that an epitope argument actively **supports**, and it is the only one whose authors offered the degradation alternative themselves |
| **9** | `P252A` CHX chase: *"significantly enhanced protein degradation"* | **A18 anti-FLAG M2** | 🟢 the tag — 🔴 **tag terminus UNSTATED** | designed missense; tagged transgene | 🔴 **YES, AND IT IS UNRESOLVABLE AS PUBLISHED.** If the FLAG is C-terminal, every lane of the only published WWOX-missense turnover dataset is blind to an N-terminal fragment. One sentence in the Methods would have settled it |
| **10** | `Wwox^−/−` mouse tissues: *"Western blot … showing **deletion of WWOX**"* | **A4**, monoclonal-by-citation | 🔴 unknown | **exon 1** conditional deletion | 🟡 **Immaterial** — an exon-1 deletion leaves no N-terminal species regardless of epitope. Attributable only through a citation chain (**B8**) |

### 4.2 The tally

| | |
|---|---|
| *"Absent / reduced protein"* results enumerated | **10** |
| Attributable to a **named** antibody (catalogue, or in-house with a stated immunogen) | **7 / 10** — rows 3, 4 (×2 reagents), 5, 7, 8, 9, 10 |
| 🔴 `NOT ATTRIBUTABLE` | **2 / 10** — row 1 (`Q230P`) and row 6 (`G372R`). 🔴 **The two human missense alleles this model turns on** |
| Attributable but with the **epitope still unknown** | **3** — rows 7, 9, 10 |
| 🔴 **Could a stable N-terminal species have been missed?** **YES** | **4 / 10** — rows 1, 6, 7, 9 |
| 🟢 **NO**, on an epitope argument that actually holds | **4 / 10** — rows 4, 5, 8, and row 3 in its corrected form |
| 🔴 **Demonstrated to have happened in print** | **1** — rows 2 → 3, the *lde* rat |

### 4.3 The one sentence this section exists for

🔴 **The two published *"absent WWOX protein"* results that this disease model depends on most —
`Q230P` and `G372R` — are the two the census cannot attribute to any antibody at all.** Everything
downstream of them inherits that. It is not a reason to disbelieve them; it is a reason to stop
citing them as though the instrument were known.

---

## 5 · THE TRACE, SCORED

Predictions were sealed in §0 before the first query. Scored here against what was found, in the
order they were written, with no retrofitting.

| # | Prediction | Result | Grade |
|---|---|---|---|
| **P1** | Exactly one epitope-stated anti-WWOX antibody in the repository, N-terminal | **Repository: exactly one — `HPA050992`, aa 32–110, N-terminal. Correct.** Literature: **five more** (A2, A3, A5, A6, + the pY33 pair) | 🟡 **SPLIT** — the repository clause 🟢 exact; the implied universality 🔴 wrong by 5 |
| **P2** | **6–12** distinct anti-WWOX primaries identifiable | **17** | 🔴 **REFUTED**, and instructively: I counted in catalogue numbers, and **7 of 17 have none**. ⚠️ *(Scored 2026-09-22 and left unrewritten. The counts table now reads **6** without a catalogue number, because `A17` acquired one on 2026-09-23 when it was identified as `sc-20528`. The denominator coinciding at 17 is arithmetic accident, not agreement — see the merge note.)* The field runs on in-house antisera, which is exactly why the epitope question is hard and exactly why I under-counted |
| **P3** | **≥ 60 %** with no stated epitope anywhere reachable | **9 / 17 = 53 %** — plus 2 more (A11, A12) that state only a modification site and 1 (A17) that states only a negation | 🟡 **NARROWLY REFUTED on the strict count, SUPPORTED on the operative one.** If *"usable for a flanking design"* is the test, the figure is **14 / 17 = 82 %** |
| **P4** | A further HPA/PrEST anti-WWOX exists, N-terminal or spanning, **not** strictly C-terminal | No second HPA anti-WWOX appeared in any Methods section read here, and the HPA portal is `EGRESS_BLOCKED` | 🔴 **COULD NOT ESTABLISH.** Untested, not confirmed. **The PrEST-avoids-the-Rossmann-fold reasoning in H1 is therefore unsupported and must not be carried forward** |
| **P5** | **< 40 %** of *"absent protein"* results attributable to a named antibody | **7 / 10 = 70 %** | 🔴 **REFUTED, and badly.** I predicted a field that does not name its reagents; it names them more often than not. **What it does not do is state their epitopes** — a distinction my prediction collapsed |
| **P6** | **≥ 1** *"absent"* result where an N-terminal fragment could not be excluded | **4**, plus **1 documented case of it actually happening** (*lde*, rows 2→3) | 🟢 **SUPPORTED, and exceeded.** The *lde* correction is stronger than anything P6 asked for |
| **P7** | `PMID 19500159` is the counter-example, stating epitope-vs-lesion **qualitatively, without residues** | 🟢 Verbatim: *"Because the antibody used for Western blot analysis **does not recognize the C-terminal amino acid sequence** of Wwox protein…"* — qualitative, no residues, exactly as predicted | 🟢 **SUPPORTED, verbatim** |

**H1 — *the flanking pair is half-real*.** 🟢 **SUPPORTED on its operative claim**, 🔴 **unsupported on
its stated mechanism.** The N-terminal member exists and was already here; no C-terminal member was
found. But P4 never tested *why*, so the PrEST/Rossmann explanation is a story, and it is retired
here rather than repeated.

**D5 — *the denominator was wrong*.** 🟢 **SUPPORTED, and it is this file's most consequential
finding.** *"0 / 12 state an epitope"* is a true statement about **abundance papers** and a false
statement about the **antibody literature**. Six epitope-stated anti-WWOX reagents exist, one of them
carries the exact residue range the design needs, and it had been sitting in
`discovery_ledger_current.md` line 623 — inside a bullet titled *"Reagenti riusabili"*, which is to
say **it was written down as reusable and then not reused.**

**RESULT → GRADE → EXPERIMENT.**

| | |
|---|---|
| **RESULT** | The required component is half-purchasable. The failure it guards against is real and has occurred in print. The N-terminal reagent was already held and unconnected |
| **GRADE** | 🟡 The design survives; its **procurement line** does not, and its own open item ⭐2 (*"`UNSTATED` in 12/12 — final for this session"*) is 🔴 **superseded**: the epitope was never egress-blocked, it was **census-blocked** |
| **EXPERIMENT** | **S2 of §2.2.** Preadsorb each candidate C-terminal antibody against `ww (1–110 a.a.)` and `ADH (110–414 a.a.)` GST fusions, both already defined verbatim in `PMID 22193544`. Two bacterial preps, two blots, one afternoon, **no egress and no vendor**. It converts the census's hardest `UNSTATED` into a measured fact — and it is the control `PMID 16152610` ran in 2005 |

### 5.1 🔴 The method finding, stated so it is not lost

**A negative that came from a census is only as wide as the census.** The abundance census asked
*"what antibody did this abundance measurement use?"*, got `UNSTATED` twelve times, and the number
hardened into *"no WWOX antibody has a stated epitope."* Both steps were locally correct. The
composite was false, because **the reagent's epitope is documented in the paper that first used the
reagent, not in the papers that later used it** — a histology paper, a hypomorph paper, an oral-cancer
paper. None of them measures abundance, so none of them was in the denominator.

Generalised: 🔴 **when a census returns a uniform zero, check whether the question was asked of the
wrong document class before recording the zero as a property of the field.** Filed as a
candidate failure mode for `session_self_evaluation`; this file writes nothing to that protocol.

---

## 6 · REVIVAL TRIGGERS AND `COULD NOT ESTABLISH`

### 6.1 `REVIVAL_TRIGGER`

| # | Statement made here | What would overturn it |
|---|---|---|
| `RT-AB-01` | *"No anti-WWOX antibody with a residue range wholly C-terminal to 230 is identifiable"* | **Any** Methods section, HPA record, supplementary Key Resources Table or Reporting Summary stating such a range. 🔴 **One reachable vendor datasheet flips this**, which is why §2.1 calls it a deployment limit and not a fact about the world |
| `RT-AB-02` | A2's epitope is N-terminal (`12–94` / `16–93`) | A reading of `PMID 16152610`'s reference 21 showing the immunogen is **`1–294`**. The preadsorption control would then have to be reconciled, not discarded |
| `RT-AB-03` | A5 = exons 1–7 = aa 1–≈280 ⇒ spans 230 | A corrected exon 7 / exon 8 boundary. This repository's own map already flags that boundary as bracketed to a 90-nt window (`c.754–843`), so A5's C-terminal reach is `±30 aa` |
| `RT-AB-04` | `HPA050992` is purchasable | 🔴 **Never verified here.** The catalogue number is attested in a 2019 Methods section; whether Sigma-Aldrich still lists it is `UNVERIFIABLE — EGRESS_BLOCKED`. **One human, one browser, ten minutes.** `HUMAN_REQUIRED` |
| `RT-AB-05` | Row 9's tag terminus is unresolvable | The `pCMV-3Tag` member number, or any sequence deposit for the construct |
| `RT-AB-06` | 4 / 10 *"absent"* results could have missed an N-terminal species | Retrieval of Johannsen 2018's or Steinberg 2021's antibody identity. Both are single author-correspondence questions |

### 6.2 `COULD NOT ESTABLISH`

1. 🔴 **The epitope of `ab238144`, `CST 4045S`, `ABN413`, `ab189410`, `ab216660`.** Every route is a vendor datasheet; every datasheet is `EGRESS_BLOCKED`. **Not guessed, not inferred, not described.**
2. 🔴 **The catalogue numbers of the two Davids 2019 antibodies.** Suppliers named, numbers not printed.
3. 🔴 **Whether a second HPA/PrEST anti-WWOX exists** (P4). The HPA portal is unreachable.
4. 🔴 **The immunogen of the Aqeilan-lineage monoclonal (A4).** The chain ends at *"Aqeilan et al., 2004a"* and the immunogen is not stated at the end of it.
5. 🔴 **The identity of the `Q230P` antibody** — `METHODS_INVISIBLE`, and the single most valuable missing fact in this file.
6. 🔴 **The identity of the `G372R` antibody** — appendix not distributed by PMC.
7. 🔴 **The identity of the `TX-007` anti-WWOX primary** (**B2**). Unchanged by this act.
8. 🟡 **The host species and clonality of 11 of 17 reagents.** Given **B4**, host species is not a footnote: it decides which markers can share a section.
9. 🔴 **Whether any anti-WWOX antibody works for IP from primary fibroblast lysate** (**B13**) — narrowed, not closed.

### 6.3 Negatives, and the premise each carries

| Negative | Premise |
|---|---|
| No C-terminal-to-230 epitope found | `PREMISE: METHODS_INVISIBLE` + `EGRESS_BLOCKED`. 🔴 **A reagent named only in Methods is invisible to `[All Fields]`** — which is precisely this reagent class — and the one PubMed query built to find HPA/Atlas antibodies (`WWOX AND ("HPA050992" OR "HPA" antibody OR "Atlas Antibodies" OR "Prestige")`) returned **0**, **for a catalogue number this file has verbatim from a PMC body**. 🎯 **That zero is a worked demonstration of the failure mode, not evidence** |
| No second HPA anti-WWOX | `NOBODY_LOOKED` at the HPA portal — it is unreachable, not empty |
| No published intracellular-flow validation | Carried forward from `wwox_activity_sensor_census_20260921.md` with its premises intact |
| Aqeilan monoclonal immunogen absent | `PREMISE: CITATION_CHAIN_UNRESOLVED` — the 2004a body was not retrieved in this act |

### 6.4 `HUMAN_REQUIRED`

Nobody was contacted and nothing was purchased. Four items need a human, and all four are cheap:
**(i)** open the `HPA050992` catalogue page and confirm listing and current applications (`RT-AB-04`);
**(ii)** open the datasheets for `ab238144`, `CST 4045S`, `ABN413` and read the immunogen field —
this alone may close §2 (`RT-AB-01`);
**(iii)** write to Johannsen 2018 and Steinberg 2021 for the antibody identities (`RT-AB-06`);
**(iv)** write to Davids 2019 for the two catalogue numbers.

---

## 7 · SELF-GRADE

| Dimension | Grade | Why |
|---|---|---|
| **Baseline enumeration** | **A** | Listed the directory, then grepped across all of it; 988 candidate lines, reduced to 17 reagents. The find that mattered — `HPA050992` at `discovery_ledger_current.md:623` — was in a Italian-language bullet in a canonical ledger and would have been missed by reading only the two files the brief named |
| **Prospective discipline** | **A** | Seven predictions sealed to disk before the first query. **Three refuted, one `COULD NOT ESTABLISH`.** P2 and P5 were wrong in ways that taught something (catalogue-counting; naming ≠ epitope-stating), and H1's mechanism is retired rather than quietly kept |
| **Verbatim handling** | **A−** | Every epitope traced to a quoted sentence; four extraction restorations argued from WWOX's own 414 aa / 9 exons rather than assumed. 🔴 **Minus** for `1294`, where the ambiguity between `12–94` and `1–294` is real, is not closed by the digits, and survives on a competition control |
| **Not inventing catalogue data** | **A** | Not one epitope inferred from a catalogue number. Five reagents left `UNSTATED` that a single datasheet would have filled. `ab216660` and `ab129881` explicitly demoted to `catalogue-listing` and used for nothing |
| **Answering §2 as asked** | **A−** | A plain **no**, with the half that exists named and three ranked substitutes, one of which (**S2**) needs no egress and no purchase. 🔴 **Minus** because whether `HPA050992` is *purchasable today* was never verified and is flagged as such |
| **§4 analysis** | **A** | 10 results, 4 `YES`, 4 `NO`, 2 `NOT ATTRIBUTABLE`, and one case where the miss **happened in print and was later corrected by an epitope-stated antibody** — stronger than the brief anticipated |
| **§3 collection** | **B+** | 13 blockers, the three named plus ten more. 🔴 **Minus** because the search was repository-side; a further sweep of `research/` dossiers would likely add more, and **B13** is narrowed rather than closed |
| **Method contribution** | **A** | §5.1 — a census's zero is only as wide as its document class — is a transferable failure mode, and it corrects a `final for this session` verdict in a sibling file written today |
| **Scope discipline** | **A** | One file written. No `git`. No `*_current.md`, registry, queue, ledger, receipt or state manifest touched. No `BATCH_COMMIT`. No contact, no purchase |
| **Overall** | 🟢 **A−** | The brief's premise was that nobody had checked whether the reagent exists. Checking found that **half of it exists, is excellent, and had been recorded in this repository and then not connected to the design that declares it missing.** The other half does not exist in any reachable source and needs one afternoon of bench work rather than a purchase order |

---

*Sources: PubMed / PubMed Central — Tochigi 2019 [DOI](https://doi.org/10.3390/ijms20143596) · Davids 2019 [DOI](https://doi.org/10.1002/humu.23675) · Suzuki 2009 [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x) · Ludes-Meyers 2009 [DOI](https://doi.org/10.1371/journal.pone.0007775) · Aqeilan 2004 [DOI](https://doi.org/10.1073/pnas.0400805101). Scholar Gateway (publisher-side passage retrieval, 4 queries, 50 passages, ~30 articles) — Ludes-Meyers 2007 [DOI](https://doi.org/10.1002/gcc.20497) · Pimenta 2005 [DOI](https://doi.org/10.1002/ijc.21446) · Guler 2004 [DOI](https://doi.org/10.1002/cncr.20137) · Abdeen 2013 [DOI](https://doi.org/10.1002/jcp.24308) · Zhang 2025 [DOI](https://doi.org/10.1002/advs.202507602) · gcc.22078 (2013) [DOI](https://doi.org/10.1002/gcc.22078) · cam4.1591 (2018) [DOI](https://doi.org/10.1002/cam4.1591). Results retrieved by Scholar Gateway; AI-generated summaries were not used as evidence — every quotation above is from a retrieved passage body.*

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

I retrieved `PMC6678113` myself. According to PubMed,
[DOI](https://doi.org/10.3390/ijms20143596) — Tochigi Y *et al.*, *Int J Mol Sci* 2019;20(14):3596.

## V1 · 🟢 BOTH halves of the headline are VERBATIM

> Methods §4.2: *"rabbit anti-Wwox (1:1000 for IH **and WB**, **HPA050992, Sigma-Aldrich**, St. Louis,
> MO, USA)"*
> Discussion: *"…which may have been due to **greater sensitivity of the new antibody, directed
> against amino acids 32–110 of human Wwox protein, a sequence 100% identical to that of rat
> Wwox**."*

🟢 **VERIFIED.** And the second half of the finding is verified locally: `discovery_ledger_current.md:623`
reads *"**Reagenti riusabili**: anti-Wwox Sigma **HPA050992** (epitopo aa 32-110, 100% identico nel
ratto)"* — in a bullet literally headed *reusable reagents*, and the string `HPA050992` appears
**nowhere else in the repository**. **The N-terminal member of the pair has been on the shelf since
that entry was written, and the design that declared the pair missing never reached it.**

## V2 · 🟢 The documented miss is real, and the mechanism is stated by the authors

> *"Although expression of mutant Wwox mRNA was detected in the testes and hippocampus of [lde]
> rats, **no Wwox protein was detected by western blot analysis**"* — the prior result, cited.
> *"The latter, however, showed **weak expression of a slightly heavier protein (46.2 kDa)** …
> which may have been due to greater sensitivity of the new antibody…"*
> *"The Wwox gene of [lde] rats contains a 13-bp deletion (c.1190_1202del) in exon 9 causes
> frame-shift, resulting in an aberrant C-terminal amino acid sequence (p.leu371Thrfs*53),
> **theoretically 0.8 kDa larger than wild type**, suggesting that this faint signal may be that of
> a mutated protein **escaping from ubiquitin-mediated protein degradation due to its instability**."*

🟢 **VERIFIED, and internally coherent**: an N-terminally-directed antibody detects a species whose
lesion is C-terminal, at the mass the frameshift predicts. **A published *"no protein"* became
*"present, faint, N-terminally intact"* with the antibody as the only changed variable**, in the
closest animal model of the splice-null side of the reference genotype.

⚠️ **Bound the file should carry and does not:** the authors themselves judge *"it is unlikely that
this faint expression … would have substantial effects on the phenotype"*, and they are right that
**no functional assay of the residual product was run**. The finding is about **detection**, not
about function. `abundance rescue ≠ functional rescue` applies to a naturally occurring residual
species exactly as it applies to a rescued one.

## V3 · 🔴 The best thing in this paper for us is one the census did not extract

> Methods §4.4: *"organs were minced and **sonicated** in **RIPA lysis buffer (50 mM Tris-HCl pH 7.6,
> 150 mM NaCl, 1 mM EDTA, 1% sodium deoxycholate, 0.1% Triton X-100, and 0.1% sodium dodecyl
> sulfate (SDS))**"*

🎯 **This is a REAL RIPA — deoxycholate *and* SDS — plus sonication**, and the string
`sodium deoxycholate, 0.1% Triton` returns **zero** elsewhere in this repository.

**Two consequences:**
1. It is a **13th row for the abundance census, with a verbatim recipe, in the stringent class** —
   and it is the first row anywhere in this corpus where a *faint* WWOX species was detected **under
   genuinely stringent extraction with mechanical disruption**. That detection is therefore not a
   soft-lysis artefact, which is the objection one would otherwise raise first.
2. It sharpens today's re-read finding rather than duplicating it: Wang 2011 called a
   Tween/Triton buffer *"RIPA"* with neither DOC nor SDS; Tochigi 2019 uses the name correctly.
   **The same word denotes two different chemistries in this corpus**, which is exactly why the
   census must classify by **recipe** and never by **name**.

⚠️ `NO NEW INFORMATION` for the heterozygote datum — *"a single band of normal molecular weight, but
its intensity was **almost half** that observed in [+/+] rats"* is already held in
`discovery_ledger_current.md:1043`, `CC-20260826-CLAIM032-01` and `CLAIM 032` itself.

## V4 · 🟢 The method finding is correct and is the file's most transferable output

> *"`0/12 epitope stated` was a true statement about **abundance papers** and a false statement about
> the **antibody literature**. The reagent's epitope is documented in the paper that *first used*
> the reagent."*

🟢 **Endorsed, and it generalises past antibodies.** A census defines a **document class** as well as
a term, and a uniform zero is as likely to be a property of the class as of the field. Here the
epitope was **census-blocked, not egress-blocked** — which is a different remedy entirely, and a
free one.

**Adopted as the standing form:** *when a census returns a uniform zero, check whether the question
was asked of the wrong document class before recording the zero as a property of the field.* This
is the **tenth** way this corpus has now seen an absence be an artefact, and the second found today
— the ninth being a Markdown-scoped grep missing a JSON string field.

## V5 · The design verdict, accepted with its procurement consequence

🟢 **Half the pair exists and is excellent; the C-terminal half does not exist in epitope-stated
form** (0 of 17, the four candidates all `EGRESS_BLOCKED` datasheets). 🟢 **And the proposed
substitute is better than buying one**: preadsorb each candidate against the **two GST fusions
already defined verbatim in `PMID 22193544`** — `ww (1–110)` and `ADH (110–414)` — two preps, two
blots, and an unreachable datasheet becomes a measured fact. The design's logic is untouched; only
its procurement line changes from *buy two* to **buy one and map the other**.

🔴 **The two `NOT ATTRIBUTABLE` rows are the two that matter most** — `Q230P` (Johannsen) and
`G372R` (Steinberg), the two human missense alleles this model turns on. Combined with V2, the
consequence is stated plainly and without overreach: **for neither allele can it presently be
excluded that an N-terminal species was missed.** That is not a claim that one was.

## V6 · Information gain and grade

**INFORMATION GAIN: HIGH.** It found half the required reagent already in our own ledger, produced
a documented in-gene case of an antibody changing a published negative, and identified a census
failure class that is cheap to fix everywhere.

**Grade: A− endorsed.** Trace scored honestly: three of seven predictions refuted, including two
where the delegate had counted the wrong thing and says so.

**No row is canonical; none is proposed for `BATCH_COMMIT`.**
