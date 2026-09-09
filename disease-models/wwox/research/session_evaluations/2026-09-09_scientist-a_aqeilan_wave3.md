# Batch self-evaluation — `scientist-a`, AQEILAN-FT-A-001 wave 3, 2026-09-09

## Scope and executable verdict

- **Batch/session:** wave 3 of `AQEILAN-FT-A-001`. Two PMIDs, in lot order, each taken M0→M5 and committed before the next.
- **Studies and complete-read receipt IDs:**
  - PMID **15070730** — `FTR-20260909-15070730-02`, `complete_fulltext_read`, `inadequate_prior_coverage` (prior `FTR-20260814-15070730-01`)
  - PMID **24510053** — `FTR-20260909-24510053-01`, `complete_fulltext_read`, `first_read`
- **`session_self_eval.py`:** `VERDICT: PASS`. receipts 144 · complete_fulltext_events 75 · active_complete_reads 64 · unread_premises 3/4. **Neither of my two PMIDs appears in any `[DECLARED GAP]` line**; all fourteen belong to other papers (22193544, 32000863, 34214506, 35716775, 36779245, 39507621).
- **Per-study manifest(s):** both `--verify-artifacts --require-current-schema` → **PASS, 0 gaps** (15070730: 38 locators; 24510053: 9 locators). Additionally `regenerate_adjudications.py verify --pmid 24510053` → **9/9 digests regenerated, 9/9 needles resolved inside their crops**.
- **Receipt verification:** `OK: 144 chained receipt(s), tail anchored`.
- **Structural LINT:** `PASS` after every commit.
- **Local verdict:** PASS.
- **Workspace/global verdict and concurrent conditions:** shared checkout with `scientist-b` and `scientist-c` working concurrently; ledger moved 140→144 during the wave (two peer appends interleaved with my two). All commits path-scoped through the `flock` wrapper; no peer path touched. One cross-actor condition observed and **reported, not fixed** — see Process, ratchet.

---

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | 15070730: whole body re-read this session (not inherited) + all four body figures re-verified byte-identical + **Supporting Figs 5/6/7 opened for the first time** at 6×–26×. 24510053: all 11 pages read from rendered pages; Tables 1 and 2 read; `figures: not_present` **measured** (pymupdf: 0 embedded images; 0 occurrences of "Figure"/"Fig."). | **strong** | 15070730 supplement **caption stubs HTTP 403** — named as unavailable, and that limit is carried explicitly into three findings. |
| Main message and original contribution | 15070730: WW1/PPxY/Y33 binding architecture — best-supported leg, untouched. 24510053: a somatic-cancer census; its original contribution to *this* model is the ACK1 degradation route, not the cancer survey. | **strong** | — |
| Hidden gold beyond keywords/abstract | 24510053 was `Tier C`, *"background corpus only"*, clinical relevance **LOW**, *"no deep-dive performed"* — and held the **primary provenance of active reopened rejection `DIS-001`** (ref 31 = PMID 16288044). Found by running the re-audit rule, not by looking. `gold_is_in_the_details` rule 1 worked in this lot rather than being quoted. | **strong** | — |
| Source parity: context, type and recency | Both papers are oncology; neither is a CNS or germline study, and both were read at full weight anyway. 24510053's transfer verdict is **negative and measured**, not assumed. | **strong** | — |
| Team type, field density, observation vs interpretation | Both are Aqeilan-lab. `is_primary_group_for_gene: true` / `is_primary_group_for_disease: false` recorded separately in both manifests, with the weighting split stated: mouse-allele **observations** near first-hand (the group made the mice), somatic-mechanism **interpretations** weighted as secondary. Field density measured with dates (e.g. `WWOX AND Ack1` = **4** records). | **strong** | — |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | 24510053: `DATO` reserved for *what the review reports*, never the biology; `ESPANSIONE` for the census; `INFERENZA` for the degradation-route structure. 15070730: binding `DATO`; Y33-phosphorylation `DATO` *in vitro, isolated domain* but `INFERENZA` for its cellular effect on binding; routing `INFERENZA`, overexpression-dependent. | **strong** | — |
| Existing claims touched; conflicts/revival triggers | `CLAIM 023` **NARROW** proposed (R4 satisfied). `DIS-001` strengthened in provenance, **verdict unchanged**. `D-01` gains an in-the-wild instance. Revival triggers written for each negative; the E3-ligase negative recorded as a **dated 2026-superseded snapshot** rather than a standing fact. | **strong** | `CORPUS P206` `Identifier: PENDING` — reported, not repaired (not a reading's authority). |
| Multi-hop and corpus cross-query | 24510053: 103 refs enumerated, **one resolved deliberately** (PMID 16288044) with the reason for resolving only one stated; corpus cross-query found 6 files answering directly, incl. the dismissal ledger. 15070730: 27 refs, prior resolution retained. | **strong** | PMID **12514174** (Chang, Wox1/JNK) still absent — the premise under the whole Y33 story. |

---

## Persistence diagnosis

- **Durable ledger/registry IDs and wikilinks:** `FTR-20260909-15070730-02`, `FTR-20260909-24510053-01`, `CC-20260909-15070730-01`, `CC-20260909-24510053-01`, `DL-MECH-111`, `adjudications.json` for PMID24510053. Commits `a1c07fa`, `8641840`, `3bef8dd`, `5312375`, `8583553`.
- **Reading queue/debt:** PMID **16288044** argued up the queue with its reason. PMID **12514174** restated as an unheld premise. PMID **33914858** remains parked (not retried, per dispatch).
- **Dossier and commit candidate:** both written for both papers. 🔴 **15070730 had never had a dossier at all** — the 2026-08-14 reading's `outputs` list the manifest alone. This wave produced the first.
- **Receipt source fingerprint, coverage and supplement state:** both receipts carry a local fingerprint (`d2ae13cb…`, `ef0ba8d0…`). 15070730 `supplementary: read` with caption stubs named unavailable; 24510053 `supplementary: not_present` (none published).
- **Can a future run distinguish full text from abstract only? How:** yes. Every locator carries `surface` + fingerprinted `artifact`; `abstract` is never an evidentiary surface in either manifest; for 24510053 **every** body locator additionally carries a `page_anchor` recipe that regenerates from the PDF digest, so a future run can reproduce the exact evidentiary pixels without holding my files.

---

## Process and capability diagnosis

- **Skills/gates/patterns used:** M0 duplicate-work gate per PMID (re-run, not inherited); `find-fulltext` cascade; `pmc_pow_fetch.py`; `evidence_presence`-style digest re-verification before building on prior work; rule 5d SUSPECT screen; **rule 5e page adjudication**; `regenerate_adjudications.py verify`; **`legend-locator-audit` with two independent blind auditors**; the epistemic-discipline **re-audit rule** against the dismissal ledger; `legend-session-self-eval`.
- **Plausible skills deliberately declined, with reasons:** `legend-deepdive` on 24510053 — it is a REVIEW, and running a claim-producing pipeline over a secondary source is how a review's summary becomes a datum (`D-15`). `legend-locator-audit` on 24510053 — trigger checked and absent; no claim's evidentiary basis moves. `legend-safety-triage`, `legend-hypothesis-forge` — no molecule, no maturing lever. All recorded in `skills_considered` with reasons.
- **Failures, retries, extraction mismatches or concurrency events:**
  - 24510053 text layer **SUSPECT** (12 `þ` for `+`, 8 `0x02` for `−`, all in genotype/receptor notation); `pymupdf` re-extraction **worse** (drops the minus). Refused, never hand-corrected.
  - `pdftotext -layout` **spliced two columns across the gutter** — caught before quoting; column-aware extraction used as a reading aid only.
  - Manifest validator rejected my first locator design **four times** (needle collisions I created by reusing one snippet across three locators; `panel_supports_text` not in the enum; a panel pointed at another panel; two needles under 30 chars).
  - `regenerate_adjudications.py` rejected all 9 digests — my renderer differed from the canonical call — **and** flagged 2 non-unique needles. Both fixed at source.
  - Receipt writer rejected `analysis_at` later than `event_at`.
  - Ledger moved 140→144 under concurrent peer appends; no rechain needed.
- **What caught each failure before an overclaim — attribution, because self-assessment is the weakest form:**
  - 🔴 **The blind auditors caught what I could not.** 7 of 13 triples corrected. My **most attractive finding was withdrawn in full**: the Fig 6 → Fig 5 cross-panel bridge **fails on cell line** (NIH 3T3 vs SAOS-2). I had built and written it; an auditor found it; I verified it against the body myself before accepting.
  - An auditor forced into the open an assumption I had not declared: **Fig 5 has no caption**, so *which panel is the reduced dose* is an assumption, not a datum.
  - Both auditors corrected my Src-sentence count **upward** (8 → 20) — the finding got *stronger*, which is the shape of an honest correction.
  - **My own measurement caught my own eye.** My visual reading of Fig 5's panels was contradicted by two automated segmentations that also disagreed with each other; I therefore **declined a directional claim** rather than picking the interesting one.
  - **I caught an auditor.** The two disagreed on Fig 7's y-maxima (68/68/128 vs 60/60/120); I adjudicated at 26× upright from the glyph shape — open centre, no waist — and **the auditor was wrong**. Also rejected an auditor's proposed mechanism for lane 10 (centroid 155.75, inside the window) while accepting its substance.
  - The validators caught every schema defect listed above.
- **Disease-agnostic micro-upgrade shipped:** see `legend-capability-scout` output — `framework/scripts/oa_status_dissent.py`, with regressions. Motivated by a measured fact from this wave, not by plausibility: **five OA indexes unanimously reported PMID 24510053 closed and all five were wrong**, because they key on a DOI whose journal has since changed publisher.
- **Regression/evidence that makes the upgrade persistent:** tests shipped alongside and mutation-tested; first measurement recorded in the tool's own output.
- **Residual risk and next decisive action:**
  - 🔴 **The single highest-value action for this lot is reading PMID 16288044.** It is the primary behind `DIS-001`, has an **empty receipt status**, and `WWOX AND Ack1` returns **4 records total**.
  - `CORPUS P206`'s `PENDING` identifier still makes `CLAIM 023` a claim sourced to a placeholder — now with the ancestor **identified** but the registry unrepaired.
  - The three 15070730 supplement **caption stubs (403)** remain the one surface this wave did not obtain; three findings carry that limit explicitly.

### Where I grade myself down

**Grading the process, not the outcome.** The outcome is good: two complete reads, a defensible
baseline narrowing, a first-in-deployment use of rule 5e. **The process had one real defect.** I
built the Fig 6 → Fig 5 bridge, wrote it into a manifest, and committed it — and it was wrong on a
fact available in the body text I had already read and quoted (*"we transfected NIH 3T3"*). The
audit caught it; I did not. The cell line was in a sentence I had captured as a locator two hours
earlier. **`partial` on the dimension "did I check my most attractive finding as hard as my least
attractive one" — I did not, and the pattern is that an appealing cross-panel rescue got less
scrutiny precisely because it was appealing.** That is the same shape as the wave-2 overshoot my
own census caught, and it recurred. The proportional response is the standing habit, not a script:
**the finding I most want to be true is the one to re-derive from the source before writing it.**
