# Audit of the 31 PMIDs excluded by the 2026-09-08 duplicate-work gate

**Actor:** `auditor-31` · **Date:** 2026-09-09 · **Scope:** the 31 PMIDs that
[`2026-09-08.md`](2026-09-08.md) § 1 withheld from the three scientist lots because each already
carried a `complete_fulltext_read` receipt. The gate re-ran unchanged on 2026-09-09
([`2026-09-09.md`](2026-09-09.md) § 2): "the 31 excluded remain correctly excluded."

This audit does **not** re-read them. The duplicate-work gate exists to prevent exactly that, and
re-reading on suspicion alone would be the waste it guards against. It ranks the 31 by risk on
evidence that can be cited, and re-examines only where a **concrete new anomaly** — not a
suspicion — makes a re-examination legitimate. Four papers met that bar. For each, the trigger is
stated in one sentence.

---

## 1 · What the mechanical audit already established, and is not redone here

| Check | Result over all 31 |
|---|---|
| `evidence_presence.py` | 248 declared artifacts · **248 ABSENT** · 0 DIGEST_MISMATCH · 0 present |
| `manifest_flag_drift.py` | 29 PASS · **2 FINDINGS**, both `multihop.performed: false -> true` |
| Receipts | all 31 carry a governing `complete_fulltext_read`; ledger verify OK, 154 chained |
| Manifests | 31/31 present, **all schema v2** — no v1 migration debt in this set |

Every declared path lies under `files/`, which is gitignored (`git ls-files files/` returns 0), so
no evidence byte is ever versioned. **The absence is structural and says nothing about whether a
reading happened.** The tool's own verdict is "expected in a fresh checkout". Raw output:
`ep31.jsonl`, `ep31_summary.json`, `drift31.txt` in this session's scratchpad `closure/`.

Both drift findings are advisory and are resolved in § 5 below.

---

## 2 · How the ranking was built

Five weighted axes, each requiring citable evidence:

1. **Load-bearing weight** — does the paper support a `consolidated baseline`, or a claim at high
   transferability tier? Verified directly against `claim_registry_current.md` and
   `paper_registry_current.md`, not taken on report.
2. **Dependency on secondary sources** — the pattern `scientist-a` established: load-bearing
   genotype-level facts reaching this corpus through reviews and editorials by one laboratory
   whose primaries were never opened.
3. **Shared reagent chains** — the `16223882` adenovirus/antibody chain under a standing
   expression of concern (`28373548`).
4. **A standing expression of concern or erratum** — `erratum_scope_check.py`, run per PMID.
5. **Text-versus-figure discrepancy or incoherent documentation** already recorded in the
   manifest or dossier.

### 2.1 · Two premises in the brief that the evidence corrected

Recorded because an audit that silently drops a false premise teaches nothing.

- **The reagent chain does not touch these 31.** The chain `scientist-c` documented runs
  `16223882` → **`18460020`**, with `20530675` as the upstream surfacing paper. Neither is among
  the 31. Four of the 31 (`26256646`, `18974271`, `17360458`, `18487609`) cite `16223882`
  *bibliographically*, and in the first three the manifest explicitly excludes it as
  non-load-bearing. That link is **absent, not merely unrecorded**.
- **The expression of concern does not impugn the reagents.** Per
  `CC-20260909-18460020-01` § 2, its declared scope is **one loading-control panel** (Fig 1B of
  `16223882`). The reagent dependency is a fact; the invalidation is not. The brief's framing of
  "both anti-Wwox antibodies" as compromised overstates what the repository records, and this
  audit does not adopt it.

---

## 3 · Per-PMID risk table

Ranked most to least risk. `CB` = consolidated baseline. Claim linkage was verified against the
registry's own `Source:` and `Wikilinks:` lines.

| # | PMID | Risk | Load-bearing weight | Evidence for the ranking | Triage |
|---:|---|---|---|---|---|
| 1 | **34831305** | **HIGH** | Wikilink support of **CB 003** and **CB 004**; PMID-cited inside CLAIM 016 | `paper_registry_current.md` PAPER 063 states verbatim: *Source type:* "review narrativa / atlante di modelli — **nessuna coorte sperimentale nuova**"; *clinical relevance:* "**BACKGROUND come evidenza di claim**"; *Claim links:* "**none — è una sintesi, non una replica indipendente dei primari che elenca**". The registry says it is not claim evidence; two consolidated baselines wikilink it as support. Axis 2 at maximum. | RE-ACQUIRE ONLY |
| 2 | **34747138** | **HIGH** | **SOLE named `Source:` of CB 004** (T2); co-wikilink of CB 003 | CLAIM 004 `Source:` names PMID 34747138 and no other. The only one of the 31 whose content reaches `disease_model.md` (L43, "Repudi 2021"). Its manifest does not carry the `panel_text_relation` key, so text-versus-figure agreement is undocumented for its 4 figure locators. | RE-ACQUIRE ONLY |
| 3 | **34634460** | **HIGH** | **SOLE wikilink of CB 021** (T2) | CLAIM 021 `Wikilinks:` names PAPER 031 alone. Manifest self-flags: *"THE PPI IS A THIRD OF THE PREVIOUS PAPER'S AND THAT CHANGED WHAT COULD BE CLAIMED… At full-figure scale I first misread whic[h]"* — a sole-source baseline resting on a figure surface at 101–108 effective ppi. 2 `text_contradicted_by_panel` locators. | RE-ACQUIRE ONLY |
| 4 | **42422765** | **HIGH** | **SOLE wikilink of CLAIM 011** (`flagged for review`, T2); shared in CLAIM 031 | `disease_model.md` L45 still reads "dose-dependent durable rescue" — the lexicon CLAIM 011's flag and `working_model_current.md` corrected to a *threshold*. An un-propagated correction sitting in the disease model. 2 `text_contradicted_by_panel`, one of them: *"THE PAPER'S TEXT CONTRADICTS ITS OWN FIGURE 4."* | NO ACTION (referred) |
| 5 | **42128308** | **HIGH** | Narrative review corroborating 8 claims incl. 3 baselines (002, 019, 020) | Axis 2 in its purest form: the gene's primary laboratory reviewing its own field. Flag drift `multihop.performed: false -> true` (**noted**). Two `text_contradicted_by_panel`: *"A FIGURE DECLARED AS PREPARED BY A GENERATIVE MODEL"* and *"THE SCHEMATIC PROMOTES 'SUPPRESSES' TO 'NO SEIZURES'"* — compression toward confidence, recorded in the manifest. Text surface is a PyMuPDF extraction of a PDF, not structured markup. | NO ACTION (referred) |
| 6 | **26675548** | **MED** | No claim (`Claim links: none`) | **Concrete new anomaly.** Manifest quotes an Ad-WWOX/Ad-GFP rescue (Fig 3C/3D) while its multi-hop names **no source for the virus**; dossier has zero occurrences of `Ad-GFP`, `Ad-WWOX`, `adenovir`. A shared-reagent gap surfacing the week a reagent-descent risk was established. | **RE-EXAMINE** |
| 7 | **18487609** | **MED** | No claim (corpus placeholder) | `surface_preflight`: *"SUSPECT — REFUSED AS A TEXT SURFACE"* (126 C0 controls, zero of `< > ≤ ≥ ± × −` against 12 uses of "significan") — correctly refused. `coverage_gaps/supplementary`: *"UNAVAILABLE, AND ONE LOAD-BEARING NUMBER DEPENDS ON IT."* **4** `text_contradicted_by_panel`, the most of the 31. `16223882` sits in its own multi-hop `queued` list, unread. | NO ACTION (referred) |
| 8 | **24550385** | **MED** | No claim (corpus placeholder) | **The only unnoted flag drift of the 31** (`multihop.performed: false -> true` @ `df00bb3e3`, "unaccompanied by a note"). Manifest also self-flags a stale receipt pointer and *"FOURTEEN OF THE NINETEEN GENE-DIRECT REFERENCES ARE NEITHER READ NOR QUEUED."* | **RE-EXAMINE** |
| 9 | **38182577** | **MED** | No claim (`not_processed` stub) | **The only `SCOPE_UNDECLARED` of the 31.** `erratum_scope_check.py`: *"retraction_check names an erratum but declares no `corrected_items`; the question cannot be answered and is NOT assumed clean."* Named as an open item in [`2026-09-09.md`](2026-09-09.md) § 6.3. | **RE-EXAMINE** |
| 10 | **41984841** | **MED** | CLAIM 032 (`in observation`, T1/T2) | **Declared `article_text` digest not reproduced by any of six lawful routes today** (§ 5.4). Named in `working_model_current.md` L7 as the paper whose ITCH statement `23370280` supersedes. | **RE-ACQUIRE ONLY** (attempted, unresolved) |
| 11 | **21318118** | **MED** | No claim (`Claim links: none`) | **Declared `article_text` digest not reproduced by any of six lawful routes today** (§ 5.4). Narrative review. | **RE-ACQUIRE ONLY** (attempted, unresolved) |
| 12 | **42397075** | **MED** | **None — absent from every registry** | Present only as the held-out subject of blind benchmark `BENCH-AB-001`, with an explicit exclusion pattern. Its text surface is a line-numbered accepted manuscript whose extraction interpolates digits: *"Nine of fifteen candidate snippets failed for exactly this reason."* Risk is quarantine integrity, not claim support. | NO ACTION |
| 13 | **25012504** | **MED-LOW** | CLAIM 009 (`in observation`, INFERENZA, T2) | `retraction_check`: *"One background reference in its bibliography is marked retracted and was not used as primary support"* — **the retracted reference is not named**, so the exclusion cannot be checked. Antibody source not recorded. | NO ACTION (referred) |
| 14 | **26256646** | **MED-LOW** | CLAIM 032 (`in observation`) | Cites `16223882` and handles it correctly: *"Cited PMID 16223882 is held separately and is not load-bearing."* Manifest weighting is appropriately restrained (*"Same-group continuity is not replication"*). Risk retired by its own documentation. | NO ACTION |
| 15 | **27308416** | **MED-LOW** | CLAIM 009, recorded as *"009 as interpretation, not replication"* | A commentary carrying a claim link. Axis 2, but the registry already labels the modality. | NO ACTION |
| 16 | **27308504** | **MED-LOW** | No claim (`not_processed` stub) | Commentary by the primary group on its own work; manifest separates observation from interpretation explicitly and weights the interpretation down. Correctly handled. | NO ACTION |
| 17 | **31075076** | **MED-LOW** | No claim (`not_processed` stub) | Review by the same laboratory on its own primary. Manifest carries seven self-corrections dated 2026-08-11, including a falsification of its own earlier reasoning. Documentation is coherent *because* it records its incoherences. | NO ACTION |
| 18 | **17360458** | **LOW** | CLAIM 032 **and** CLAIM 036, both reciprocated in the claim text | Foundational Wwox-null mouse. Reciprocity intact in both directions. | NO ACTION |
| 19 | **17575124** | **LOW** | CLAIM 032, reciprocated (L585) | Reciprocity intact. | NO ACTION |
| 20 | **18974271** | **LOW** | CLAIM 036 (`in observation`, T3) | Cites `16223882`, resolved with *"no new unresolved load-bearing citation was created."* | NO ACTION |
| 21 | **23254685** | **LOW** | CLAIM 036 (`in observation`, T3) | Shared support; no anomaly. | NO ACTION |
| 22 | **30755385** | **LOW** | CLAIM 009 (`in observation`, INFERENZA) | Coverage map fully `read` — one of only two of the 31 with no non-read slot. No `panel_text_relation` key. | NO ACTION |
| 23 | **23370280** | **LOW** | No claim, but **arbitrates** in `working_model_current.md` L7 | Four receipts including an `adversarial_reanalysis`. Digest reproduced. Among the best-evidenced of the 31. | NO ACTION |
| 24 | **36572673** | **LOW** | CLAIM 032 (`in observation`) | 1 `text_contradicted_by_panel`, recorded (*"Figure 2B visibly contains two lanes per group, not three"*). Digest reproduced. | NO ACTION |
| 25 | **30082886** | **LOW** | CLAIM 032 (`in observation`) | Digest reproduced. No anomaly. | NO ACTION |
| 26 | **27550453** | **LOW** | CLAIM 032 (`in observation`) | No anomaly. | NO ACTION |
| 27 | **32300104** | **LOW** | No claim (`Claim links: none`) | 1 recorded caption defect (*"Figure 1's caption swaps the plotted WWOX and WFPA colour identities"*). Digest reproduced. | NO ACTION |
| 28 | **30370248** | **LOW** | No claim | Narrative review, no claim linkage — axis 2 exposure without axis 1 weight. Digest reproduced. | NO ACTION |
| 29 | **25491415** | **LOW** | No claim | Review, no claim linkage. | NO ACTION |
| 30 | **22634283** | **LOW** | No claim (corpus placeholder) | Manifest: *"TWENTY REFS CHECKED, ZERO RECEIPTS ANYWHERE"* — population stated with its denominator. Independent biophysics group; the manifest notes its interpretation is unusually restrained. | NO ACTION |
| 31 | **24871327** | **LOW** | No claim, **affirmatively** | Registry states: *"Claim links: none — nessuna claim canonica ne dipende, e la lettura è la ragione per cui non ne nasce una."* A read that produced a documented negative. The safest record in the set. | NO ACTION |

---

## 4 · Triage decisions

| Disposition | Count | PMIDs |
|---|---:|---|
| **RE-EXAMINE** | 3 | `26675548` · `24550385` · `38182577` |
| **RE-ACQUIRE ONLY** | 15 | the 15 declaring a PMC XML text surface (§ 5.4), incl. `34831305`, `34747138`, `34634460`, `41984841`, `21318118` |
| **NO ACTION** | 13 | the remainder |

`26675548` and `38182577` appear in both of the first two rows: each declares an XML surface and
also carried a re-examination trigger. Counts therefore overlap by design and do not sum to 31.

---

## 5 · What was actually done, and what it found

### 5.1 · `26675548` — RE-EXAMINE

> **Trigger:** the manifest quotes an Ad-WWOX/Ad-GFP rescue carrying a load-bearing figure result
> while naming no source for the virus anywhere in the manifest or dossier, in the same week the
> corpus established that reagents in this literature descend from a paper under an expression of
> concern.

**Cheapest sufficient action taken:** the text surface was re-acquired rather than the paper
re-read. The re-acquired XML is **byte-identical to the declared artifact**
(`8bf84348ebe881daf153987b4197addb41a944a19ada0390d9e6d1dbf9a4a584`), so the Methods read below
are the author's characters and not a reconstruction.

**Found — the paper names no source for the adenovirus at all.** Its `MATERIALS AND METHODS`
comprises exactly seven subsections: *Cell culture and transfection · RNA extraction and mRNA
level quantification · Karyotype analysis · G2/M checkpoint analysis · GST-pull down · Cellular
fractionation · List of antibody*. **There is no adenovirus subsection** — no preparation, no
titre, no supplier, no citation — although Ad-WWOX and Ad-GFP carry the Figure 3C/3D chromosomal-
break rescue. The two "as previously described" deferrals resolve to ref 16 = PMID **25331887**
and ref 17 = PMID **24550385**, neither of which describes an adenovirus.

**And the antibody provenance is a gift, not a citation.** Verbatim from `List of antibody`:

> "Gout Polyclonal anti-WWOX antibody (a gift of Dr. Kay Huebner)"

Kay Huebner is the Huebner/Croce lineage that produced `16223882`. The reagent therefore descends
from that laboratory **by gift rather than by citation** — which is precisely the dependency a
per-PMID retraction check cannot see, and precisely what the unlanded `Reagent provenance:` field
of `CC-20260909-18460020-01` was proposed to capture. This is a **second, independent instance**
of the pattern `scientist-c` found, reached from a different paper.

This is a promotable finding. It is written as a commit candidate in § 6 and **not integrated**.

### 5.2 · `38182577` — RE-EXAMINE, resolved without re-reading

> **Trigger:** the only `SCOPE_UNDECLARED` of the 31, and a named open item in
> [`2026-09-09.md`](2026-09-09.md) § 6.3.

**Resolved from evidence that already exists, at zero acquisition cost.** The attached erratum,
PMID **38355659**, was read as a source by `scientist-c` yesterday
(`FTR-20260909-38355659-01`, `complete_fulltext_read`) with verbatim locators drawn from **both**
the XML body **and** the rendered page pixels. Its locators establish the corrected scope from the
deposit itself rather than from any prior reader's assertion:

> "In this article the third author name has been given erroneously as Ameen Haji Yehya."
> "It should be read: Ameen Haj-Yahia."

with a visual attestation recording that the page "carries no figure, no table, no abstract and no
reference list", and that the notice's title reproduces the original title unchanged.

**The scope is therefore established: the third author's name, and nothing else.** No datum,
figure, panel, table or conclusion is corrected. This independently confirms what `38182577`'s own
manifest asserted in prose, from a source read by a different actor.

**The residual is a field shape, not an open scientific question.** `erratum_scope_check.py` reads
a structured `corrected_items` key; the manifest carries its scope in the free text of
`retraction_check.result`. **The manifest was not edited.** Making the checker green by writing the
field would be retroactively altering an attestation so two dimensions agree, which is forbidden;
and the 2026-09-09 norm — *"None belongs to a lot in flight, so none was edited by a passing
actor"* — points the same way. Referred as a commit candidate in § 6.

### 5.3 · `24550385` — RE-EXAMINE, advisory closed and a live gap found

> **Trigger:** the only flag drift of the 31 that `manifest_flag_drift.py` reports as
> "unaccompanied by a note written in the same edit" — the tool's standing question is "point at
> the work, or put the flag back."

**The work is pointed at.** The same commit `df00bb3e3` that flipped `multihop.performed`
`false -> true` also rewrote the whole block in one edit: `references_enumerated` 0 → **67**,
`gene_direct_count` → **19**, a populated `gene_direct_refs_in_source`, a stated
`enumeration_method` and a `cross_check_result`. The commit message records "67 references
enumerated". **The drift is answered by its own diff; the advisory is closed, not escalated.**

**But its cross-check is now stale, and two primaries beneath it have still never been read.** The
manifest's 2026-08-11 statement that fourteen of nineteen gene-direct references were "neither read
nor queued" was measured against the ledger of that date. Re-measured today:

| Named in the 2026-08-11 cross-check | Status on 2026-09-09 |
|---|---|
| `15070730`, `21075834`, `22634283`, `23370280` | **complete_fulltext_read** — debt paid |
| `24308844` | partial only |
| **`17178850`** | **no receipt of any kind** |
| **`16288044`** | **no receipt of any kind** — named in the manifest as "the other half of the DIS-001 pairing" |

The open multi-hop debt of this paper is **2, not 14**. That is the good news and the bad news in
one line: the count improved by four-fifths, and what remains sits underneath a dismissal-ledger
entry. `16288044` is a candidate for the unread-primaries list of
[`2026-09-09.md`](2026-09-09.md) § 7.3. Referred, not queued — queueing is not mine.

### 5.4 · The digest re-derivation sweep — RE-ACQUIRE ONLY, 15 papers

> **Trigger:** `evidence_presence.py` reports 248 ABSENT and cannot distinguish "gitignored" from
> "never existed". For any paper whose text surface is a public archive deposit, that distinction
> is cheaply testable, and no reading is required to test it.

15 of the 31 declare a PMC XML `article_text`. Each declared SHA-256 was tested against the live
archive. **A first pass through one route reproduced only 4 of 15 — and that verdict was wrong.**
Testing the route before accusing the artifact showed that the Europe PMC `fullTextXML` endpoint
reproduces `34747138` exactly, and re-running both routes gives:

| Result | Count | Route |
|---|---:|---|
| **Reproduced byte-identical** | **13 / 15** | Europe PMC `fullTextXML` (9) · NCBI eutils `rettype=xml` (4) |
| Not reproduced by any of six routes | 2 / 15 | `41984841`, `21318118` |

**For those 13, the declared evidentiary artifact is byte-for-byte re-derivable from a public
archive today.** That is materially stronger than "absent": the digest was not fabricated, the
surface was structured markup as declared, and any locator drawn from it remains checkable against
the author's characters by anyone with a network connection. It includes `34747138`, `34634460` and
`34831305` — the three highest-ranked papers and the ones carrying the consolidated baselines.

For `41984841` and `21318118`, six routes were tried (Europe PMC `fullTextXML`, its `?format=xml`
and `unicode` variants, eutils `rettype=xml` and `retmode=xml`, and the PMC OAI `GetRecord`
endpoint). None matched. **This is not evidence the artifact was wrong.** A public archive
re-serialises its deposits, and `41984841` is a 2026 paper whose deposit has had every opportunity
to change since 2026-08-10. What it does mean is concrete: **those two papers' locators cannot
currently be re-verified against the author's bytes**, and that is a live reading debt.

**Infrastructure observation, tested rather than assumed.** Every request above was made with **no
User-Agent** and none met a reCAPTCHA. That is consistent with the § 7.3 observation and does not
establish its cause; it is one session's measurement, not a mechanism. One route trap worth
recording: `www.ncbi.nlm.nih.gov/pmc/utils/idconv/` now 301-redirects to
`pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/`.

**One error of my own, recorded because it is the exact failure rule 5c warns about.** I guessed
`PMC4826207` for `26675548` from an adjacent identifier. It fetched cleanly, parsed cleanly, and was
a **different paper** — the article actually deposited at `PMC4826207`, "CCL3 promotes angiogenesis
by dysregulation of miR-374b/VEGF-A axis in human osteosarcoma cells", DOI
`10.18632/oncotarget.6708`. Checking the title and identifiers
inside the fetched bytes caught it; digest comparison alone would also have caught it, but a reader
who trusted the fetch would have read the wrong article's Methods and found no adenovirus there
either — reaching my conclusion for an entirely invalid reason. **Identifiers are resolved, never
guessed.**

That wrong article is named here by PMCID, DOI and title rather than by PMID, deliberately. It is
not a premise of anything in this document — it is the record of an error — and `legend_lint.py`'s
`UNREAD_PREMISE` ratchet correctly counts a bare PMID in a reasoning-layer file as a paper the
reasoning leans on. Writing it as a citation raised the ratchet from 3 to 4 and produced a
`BLOCK_BATCH_COMMIT` that would have been inherited by whoever ran the next batch. The check was
right and the citation was wrong; the identification is unchanged and remains fully traceable.

---

## 6 · Commit candidates — written, deliberately not integrated

Promotable findings are recorded here as candidates. Integration is a `BATCH_COMMIT` and is the
operator's; the registry schema is reserved.

- **`CC-CANDIDATE-auditor31-26675548-01` · Reagent provenance, second instance.**
  `26675548` uses Ad-WWOX/Ad-GFP for the Fig 3C/3D rescue with **no Methods entry of any kind** for
  the vector, and declares its anti-WWOX antibody as "a gift of Dr. Kay Huebner" — the lineage that
  produced `16223882`. Descent by gift rather than by citation is invisible to a per-PMID
  integrity check. Supports the `Reagent provenance:` field proposed by
  `CC-20260909-18460020-01` and supplies it a second, independent instance. Evidence: digest-
  verified XML `8bf84348…a584`, `MATERIALS AND METHODS`, subsection `List of antibody`.

- **`CC-CANDIDATE-auditor31-38182577-01` · Erratum scope, established and unwritten.**
  The scope of the erratum attached to `38182577` is established from the deposit itself by
  `FTR-20260909-38355659-01`: the third author's name and nothing else. Proposes that
  `PMID38182577.json` gain `retraction_check.corrected_items` recording that scope with the
  erratum's receipt as its evidence, **written by that manifest's own author, not by a passing
  actor**. This closes one of the four `SCOPE_UNDECLARED` items of § 6.3 on evidence rather than by
  assumption.

- **`CC-CANDIDATE-auditor31-24550385-01` · Two unread primaries under a dismissal entry.**
  `17178850` and `16288044` carry no receipt of any kind; `16288044` is named in
  `PMID24550385.json` as "the other half of the DIS-001 pairing". Proposes both for the unread-
  primaries list of § 7.3.

- **`CC-CANDIDATE-auditor31-34831305-01` · A review carrying baseline weight against its own
  record.** PAPER 063 declares `Claim links: none — è una sintesi, non una replica indipendente`
  and `BACKGROUND come evidenza di claim`, while CLAIM 003 and CLAIM 004 — both
  `consolidated baseline` — carry it as a `Wikilinks:` support and CLAIM 016 cites its PMID.
  Proposes that the contradiction be resolved in one direction or the other. **This candidate
  proposes no change to any claim**; adjudicating a baseline is not an auditor's act.

### 6.1 · One structural finding, referred to the operator without a candidate

It is too large to be a candidate and is not mine to resolve.

**Consolidated baseline `CLAIM 003`'s named primary source has never been read in full.** Its
`Source:` line reads "Repudi et al., 2021, *Brain*" = PAPER 004 = **PMID 33914858**, whose registry
record carries `Status: integrated` alongside the note *"Full-text PDF OA-ma-bot-blocked (Oxford
advance-access) → handoff … per recupero manuale; arricchimento quantitativo del claim rimandato al
PDF."* That PDF was never acquired; § 6.1 of [`2026-09-09.md`](2026-09-09.md) records that
`scientist-a` failed to acquire it yesterday through a 19-tier lawful cascade, and that the
previously held copy did not survive the empty `files/` tree.

Its two co-wikilinked supports are both in these 31: `34747138`, a companion paper from the same
laboratory, and `34831305`, a review the registry itself classes as background rather than claim
evidence. So a consolidated baseline stands on an unread primary, a same-group companion, and a
secondary source labelled "not an independent replication".

This is `scientist-a`'s conclusion landing on a consolidated baseline — **measured here on the 31,
not projected onto them.** The operator action is the mechanical one already stated in § 6.1: open
the DOI in a real browser, save the PDF, and re-test its text layer rather than assume it clean.

---

## 7 · A rate measured on the 31, and not borrowed

[`2026-09-08.md`](2026-09-08.md) assigned 23 papers **because their prior coverage was inadequate**.
Any defect frequency observed there was measured on a selected set and **is not projected here**.
The rates below were measured on the 31 themselves and carry their own denominators.

| Measured on the 31 | Value |
|---|---|
| Manifests present, schema v2 | **31 / 31** (100%) |
| Governing receipt is `complete_fulltext_read` | **31 / 31** |
| Verbatim locators, total | **468** across 31 manifests (median 12) |
| Manifests declaring `panel_text_relation` | **28 / 31** — absent as a key in `34747138`, `30755385`, `24871327` |
| `text_contradicted_by_panel` locators | **19 / 468 = 4.1%** of locators |
| Papers carrying ≥ 1 such contradiction | **10 / 28 = 35.7%** of those declaring the key |
| `SCOPE_UNDECLARED` on `erratum_scope_check.py` | **1 / 31** (`38182577`) |
| Flag drift findings | **2 / 31**, of which unnoted **1** (`24550385`) — both resolved in § 5 |
| Declared XML digests re-derivable today | **13 / 15** (86.7%) |
| Papers where this audit found a defect needing action | **5 / 31 = 16.1%** |

**The 4.1% must be read in the right direction.** These contradictions are text-versus-figure
defects **in the published literature**, found and recorded by the prior readings. They are
evidence that those readings opened the figures — the discipline rule 5c exists to enforce. They
are not defects in the readings.

The three manifests lacking `panel_text_relation` are the same shape: the key is **absent**, not
null, and their figure locators are substantive pixel attestations (*"READ FROM THE PANEL — …"*).
That is an optional-key gap in an append-only record, not a missed figure check.

---

## 8 · Limits of this verification

Stated in the required terms, and applying to every row of § 3.

- **For 26 of the 31, this audit is a mechanical audit and nothing more. Mechanical checks green
  is not evidence of scientific correctness.** Nothing here re-derives a result, re-checks a
  statistic, or re-reads a figure for any paper other than the four named in § 5. A manifest can be
  perfectly formed, digest-verified and internally coherent while the reading it attests reached a
  wrong conclusion. This audit cannot see that and does not claim to.

- **Local absence is not evidence a reading never happened.** All 248 declared artifacts are
  ABSENT because `files/` is gitignored by design. For the 13 papers of § 5.4 the absence is now
  additionally shown to be *recoverable*; for the other 18 it remains simply structural. In neither
  case does absence bear on whether the paper was read.

- **A re-derived artifact is not the same event as the original acquisition.** The 13 digest
  matches prove the declared bytes exist publicly and are unchanged. They do not prove the original
  reader held them, nor that they were read attentively. They retire one specific doubt — that a
  digest might name nothing — and no other.

- **Two papers could not be re-derived and this is not a verdict against them.** `41984841` and
  `21318118` failed six routes. Archives re-serialise. The honest statement is that their locators
  are **not currently re-verifiable**, and that is a debt, not a finding.

- **The claim-linkage map underlying § 3 was compiled by search across the registries.** The
  load-bearing rows — CLAIM 003, 004, 011, 021 and PAPER 063's own record — were re-read verbatim
  by me before ranking on them. The lower-risk rows were not independently re-verified line by
  line, and a reciprocity error in the registry could shift a LOW row without shifting the ranking's
  top.

- **The 4.1% contradiction rate measures what prior readers recorded, not what exists.** A
  contradiction nobody noticed appears in no manifest and therefore in no rate here. The true rate
  is bounded below by 4.1% and is unknown above it.

- **No attestation was altered to make any two dimensions agree.** In particular, `38182577`'s
  manifest was left `SCOPE_UNDECLARED` despite the scope now being established, because writing the
  field to satisfy a checker is exactly the retroactive alteration that is forbidden. The checker
  and the evidence disagree, the disagreement is recorded, and the fix is referred to that
  manifest's author.

- **`26675548`'s negative is a negative about the paper, not about the reagent.** The paper names
  no source for its adenovirus; that is a documentation gap in the literature. It does not
  establish that the vector came from `16223882`, and this audit does not assert that it did.

---

## 9 · Process record

**DECISIONS_TAKEN.** *(1)* Re-examine 4 of 31 rather than more — the duplicate-work gate is the
protocol's, a concrete anomaly is the only lawful override, and four papers had one; reversible,
and the other 27 remain open to any actor with a trigger. *(2)* Prefer surface re-acquisition to
re-reading wherever it settles the question — settled `26675548` for one network fetch. *(3)* Leave
`38182577`'s manifest untouched and refer it; alternative rejected: writing `corrected_items`
myself, which would be a passing actor editing another's attestation. *(4)* Rank on directly
re-read registry lines for the load-bearing claims rather than on a compiled map alone.

**DEFAULTS_TAKEN.** *(a)* Brief's premise that the reagent chain touches these 31 — contradicted by
the evidence; the correction was recorded (§ 2.1) and work continued, rather than stopping to ask.
Safe because the correction narrows scope and is fully cited. *(b)* Digest mismatch on a first
route — treated as a route hypothesis rather than an artifact finding, and tested; had I not, I
would have reported 11 false mismatches. *(c)* Guessed PMCID returning a valid but wrong paper —
identifiers re-resolved through `idconv` and identity checked inside the bytes thereafter.

**STOP_LOG.** Class 1: **0.** Class 2: **0.** Nothing on this task required a reserved act.

**Reserved acts not taken.** No push to any remote; no history rewrite; no deletion of unique
material; no external spend (only free public archive endpoints were used); no modification of the
four scientific current files or `disease_model.md`; no `BATCH_COMMIT`; no change to the receipt
schema; no edit to any manifest, dossier or receipt belonging to another actor. Findings are
candidates in § 6, and integrating them is not mine.
