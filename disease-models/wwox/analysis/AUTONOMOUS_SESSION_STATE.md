# Autonomous session — continuation state

**Updated:** 2026-09-21 · **Purpose:** recovery point. If this session is interrupted, a cold reader
resumes from here. **Not a handoff and not a stop.**

## Current state
- `main` == `origin/main` · working tree clean · one worktree · LINT **PASS** · publication gate
  **PASS, 0 blocks** · receipts **181 chained, tail anchored**.
- Papers read and receipted in this continuation: `21766012`, `25650666` (adversarial re-read),
  `27845895`, `25238782`, `24008736`, `41124647`, `35573960`.
- **In flight at this write:** a **retrievability sweep by fetch** over every paper this repository
  calls blocked (with `36621327` read if its body is non-empty), and a **census of WWOX splice
  transcript evidence** for `DL-BIO-002` / `TX-001`.

## ✅ RESOLVED — the publication-gate blocker (kept as a worked example, not a precedent)

**2026-09-21. Operator-authorized, scope-limited, closed.** The gate had blocked on the ledger tail
`FTR-20260921-39101447-01`, where a published study's parental attribution for a chromosome-16
uniparental disomy sat in the same JSONL record as reference-genotype language. Two words were
removed, leaving `homozygous through uniparental disomy of chromosome 16`; the ledger was
re-anchored and the chain re-validated at **182**; gate **PASS, 0 blocks**.

**How the edit was made safe.** It ran under a **programmatic scope assertion that refused to write**
unless exactly one `evidence_basis` element differed and every other field was byte-identical —
`study_id`, `evidence_depth`, `source_locator`, `source_fingerprint`, `coverage`, `prior_receipt`,
`ledger_prev_hash`, `outputs`, `workflow`. **It caught my own first attempt**, which named the wrong
element index, and wrote nothing. Worth reusing: when an authorized edit is narrow, encode the
narrowness as an assertion rather than as care.

🔴 **Not a precedent, and the Operator said so explicitly.** This authorises nothing about historical
receipts, ledger rewriting, parent-of-origin removal elsewhere, gate bypass, allowlists or waivers.
**A later case of the same shape gets judged again on its own terms.**

### The rule that prevents the recurrence

**Keep inheritance-side attribution out of receipts entirely** — including for a published study's
proband, not only for this model's own genotype. The gate reads one JSONL record as a single window
and cannot tell whose family is meant, so the mere co-occurrence blocks publication; and because the
ledger is append-only, **by the time the gate tells you, the record can no longer be fixed without an
authorisation.** The scientific content almost never needs the side: write the mechanism — *"disomy
produced homozygosity"*, *"biallelic, both alleles inherited"* — and stop there.

⚠️ **And the same restraint applies to prose that merely explains the rule.** The first version of
this very note tripped the same check three more times by reproducing the offending words, and a
second version tripped it once more; the wording above is the third attempt. **Describe the shape,
never quote the phrase.**

---

## 🔴 The three results a cold reader should know before anything else

1. **Every therapeutic candidate this literature has produced acts by ANTAGONISING WWOX**, and an
   independent laboratory now says so in neurons. `PMID 35984507` (Coimbra, outside NCKU):
   *"**WWOX inhibition** by Zfra1-31 **restores** mitochondrial homeostasis and viability of
   neuronal cells exposed to high glucose."* With the pTyr33 peptide (`18371080`: *"activated WOX1
   plays an essential role in the MPP+-induced neuronal death"*) and the C1q axis (`19484134`:
   *"C1q activates WOX1 in neurons, which ultimately leads to cell death"*), that is three lines.
   **A WWOX antagonist has nothing to antagonise in a WWOX-deficient brain. This is a category
   objection, not a dosing one.** Packet item `A9`; rests on an abstract, so it must be *read*.
2. **The first node of the Chang cascade disclaims its own load-bearing step.** `25650666`'s
   Discussion asserts TGF-β1 dissociates WWOX from TPC6AΔ and, two paragraphs later, says
   *"Whether TGF-β1 regulates the binding of WWOX with TPC6AΔ **is unknown**"*. There is **no
   binding assay in the paper**. And `TRAPPC6AΔ` and `TIAF1` are **one measurement, not two**.
3. **All four levers the model cared about were finally tried in a WOREE null, and all four
   failed** (`35573960`): vigabatrin, ACTH, CBD oil, ketogenic diet. `n = 1`, null/null,
   day-one onset — **not a refutation for a genotype with residual protein**, and the ledger
   says so.

## Completed programme so far
1. **`SCIENTIST_CHANG_NS_…` waves 1–5** — closed, formally saturated.
2. **Fallback queue P1–P5** — closed.
3. **Open-ended continuation** (current) — dynamic queue, regenerated at each boundary.

## Standing commit candidates — `PARKED_PENDING_OPERATOR`, do not re-litigate
| Candidate | Class | One line |
|---|---|---|
| `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01` | MINOR | `CLAIM 032`'s cognition leg is *nobody looked*; headline quote is a tumour sentence |
| `CC-20260920-DETECTION-FLOOR-01` | MINOR | `CLAIM 030` says *proteina assente* where `CLAIM 019` says *non rilevata*; proposes `D-17` |
| `CC-20260920-CLAIM039-CEREBELLAR-01` | ORDINARY | *not cerebellar* rests on one hedged sentence; a P1 contradiction was read and never landed |
| `CC-20260920-PAPER34140629-PROMOTION-01` | MINOR | `CORPUS-STUB-150` → `PAPER 096` |

**None is a session blocker.** Revisit only if new evidence materially changes one.

## Live findings a cold reader must not re-derive
- **Six abstract-versus-results inversions** across six papers: `32764489` (brain engagement),
  `29067327` (Zfra pY33), `25650666` (null rendered temporal), `31543760` (p=0.0626 conjoined),
  `42092735` (neurotransmitter studies "normal" when never obtained), `25649963` (breast-cancer
  similarity unsupported). **In this literature the abstract does not index the results.**
- **Normal by blunt instrument, abnormal by sharp one** — four instances. Proposed as `D-17`.
- **The heterozygote phenotype is inside the control groups**, not missing from the literature.
- **Two "read but never landed" locators** (`CLAIM 016` lithium, `CLAIM 039` cerebellar) plus three
  more found in the narrow audit (spontaneous het tumours ×2, het bone deficit).
- **Zfra / all WWOX peptides: DISMISSED for WOREE.** No brain engagement; never dosed in a
  WWOX-deficient animal by anyone.
- **Lithium: DOWN.** One record in all of PubMed; no GSK3β inhibitor ever used in any WWOX context.
- **SDR missense readout: NO.** Nine of nine candidates fail on "would the protein even be there?"
- **`DL-MECH-021` lowered** medio → basso; domain-sufficiency arc demoted to author assertion; the
  seizure bridge withdrawn as a category transfer. **The platform survives.**

## Method rules earned here — apply, do not rediscover
- **Never grep `paper_registry_current.md` or `literature_tracking_log_current.md`** — use
  `registry_records.py`.
- **The MCP extractor elides gene lists into empty commas.** An abstract read through it is not a
  reliable index of a paper's content. *(This bit us on `PMID 41153369`, against our own registry.)*
- **No figure panel is inspectable in this environment.** No JATS, no PDF tooling, egress denied to
  NCBI/EBI/publishers. Per `D-14`, no figure-asserted negative may be adjudicated here.
- **A paper can be in PMC and outside the OA subset** — that is a permanent licence wall. Check
  `get_copyright_status` before re-queuing.
- **The broad `landing`-field audit is a definitional artefact** (74/81) and expands into the
  fenced-off mass reconciliation. Run that screen only against a specific claim under question.
- 🔴 **An identifier or a byline enters a durable record only by copy, in the same act, from a
  verified source — never from recall and never from a delegate's prose.** This failed **twice in
  two days**, both times mine, both times against a repository that already held the correct value:
  `FT-108` was written with `CORPUS P331` and "Hsu L-J … Chang N-S" (correct: `CORPUS P330`,
  first author **Hong Q**), and `FTR-20260921-21766012-01` was written with "Houlihan LM, Harris SE,
  Luciano M" (correct: **Hamilton G**, Harris SE, Davies G, Liewald DC, Tenesa A, Starr JM,
  Porteous D, Deary IJ — the queue entry and the analysis file both had it right). Corrected by
  append in `FTR-20260921-21766012-02`.
- 🔴 **Never re-fetch an article to a path an existing receipt already fingerprints, and check the
  ledger for the PMID before dispatching a read.** `PMID 25650666` was re-fetched to
  `files/fulltext/PMID25650666_PMC_MCPtext.txt` on 2026-09-21; the bytes changed
  (`9635516b…` → `c6e336a9…`) and the original is **unrecoverable**, because `files/` is in
  `.gitignore` and the artefact was never under version control. The earlier reading stands — its
  quotations are all present in the current artefact and were re-verified — but its fingerprint no
  longer binds to a file. Declared in `FTR-20260921-25650666-02` rather than quietly re-anchored.
- 🔴 **`is_open_access: false` is often a NOT-CHECKED reading, not a paywall.** Look at
  `checked_sources`: if it is `["pubmed"]` alone, PMC was never consulted and the flag means
  nothing. **A PMCID existing is not evidence of retrievability either** (`PMC4935222` and
  `PMC6965410` both resolve and both return a zero-length body). **Retrievability is established
  only by attempting the fetch and measuring the body length.** Both halves of this rule cost this
  session real work before it was written down.
- 🔴 **INTERROGATIVE-TO-DECLARATIVE RE-VOICING — a citation-fidelity failure mode that string
  comparison cannot catch.** A source's *question* is quoted accurately and re-attributed as its
  *finding*. Every content word matches, so quote-matching and grep find nothing; only reading the
  sentence's **grammatical mood** catches it. Found on `PMID 25238782`, whose abstract asks
  *"a question that emerges is whether fragility in these regions is only a structural 'passive'
  incident…"* and which was cited as having *concluded* that it is *"unlikely only a structural
  'passive' incident"*. **When auditing a citation, check the mood of the sourced sentence, not
  just its words.** Distinct from the seven abstract-versus-results inversions recorded here, which
  are contradictions *inside* one paper.
- **A stale queue entry will dispatch duplicate work.** `FT-102` still read *"non acquisito"* a day
  after the paper had been read. Close a queue entry in the same cycle as the read, not later.
- **A zero string count for a gene symbol in MCP body text is an instrument reading, not a
  negative.** Demonstrated conclusively on `PMID 21766012`: `TRAPPC6A` occurs **zero** times in the
  body — as do `APOE`, `APP`, `BIN1`, `CLU`, `PICALM`, which the paper is entirely about — while the
  symbol **survives intact in the PubMed metadata abstract**. The extractor deletes italicised
  tokens. Under `D-15`, never let such a count carry a negative; rest the conclusion on study
  design stated in Methods, or on prose you can quote.

## Next queue, ranked (as of this write)
0. **Landed this cycle:** `FT-102` / `PMID 25650666` (adversarial re-read — internal contradiction
   on the load-bearing binding step; human arm is an age-confounded null; TPC6AΔ and TIAF1 collapse
   to **one** node) and `FT-073` / `PMID 27845895` (the DisMech quote is real but is the strongest
   of four statements, and the axis **attenuates** death when WWOX is scarce). `DL-BIO-004` and
   `DL-MOL-008` updated; `PMID 18371080` added to the acquisition packet as **A6**.
1. ~~**FT-090** / `PMID 25416187`~~ — **CLOSED, `EVIDENCE_BLOCKED` (licence).** `PMC4935222` is a
   metadata-only stub (`full_text:""`, `is_open_access: false`, `found_in_pmc: 0`). **But the
   question that mattered is answered from metadata: `27551470` cites a REVIEW as evidence**
   (`article_types` includes `Review`; *"The aim of this review is to summarize…"*). The chain does
   not bottom out there — it passes through. Acquisition debt `A7`; **ask for the reference list,
   not the body.**
2. ~~**FT-018** / `PMID 28123895`~~ — **NOT ACCESSIBLE.** The surface census already records it as
   `idIsNotOpenAccess` / `pdf_only`. Do not re-dispatch; it is acquisition work.
3. ~~**FT-098 / FT-099** — the other two independent `TRAPPC6A` cohorts.~~ **CLOSED.** `FT-099`
   read (fails its own permutation); `FT-098` licence-walled. With `FT-097` already null, **all
   three legs of the `TRAPPC6A` node-independence claim are down and the claim is retracted in
   full** — see the retraction appended to `chang_ncku_wave2_node_independence_20260920.md`.
4. ~~**FT-092** / `PMID 25238782`~~ — **CLOSED, read.** The 2016 framing is the faithful one: the
   chapter **proposes**, it does not conclude, and the phrase attributed to it is its **question**.
   Named the re-voicing failure mode above.
5. ~~**FT-074** — four mTOR/autophagy stubs two reasoning files already lean on.~~ **PARTLY
   CLOSED, and the standing negative is FALSIFIED as stated.** `24008736` read: it **fixes** the
   sign (WWOX ⊣ autophagy), four times, including a **germline `Wwox`-knockout MEF arm** that is
   loss-of-function, drug-free and non-cancer. The narrowed form that survives: the direction **is**
   fixed on **steady-state autophagy-protein abundance**; it is **not** established on **flux**
   (no clamp was ever applied to a WWOX manipulation, and the paper's own MG132 result shows LC3 is
   being degraded proteasomally in that system), **not** established in neural tissue, and the
   **mTOR-mediated route is asserted, never tested**. The two-directions standoff now reduces to
   **one** discordant paper, `36621327`, whose acquisition priority rises above the other two.
6. **`PMID 27869163`** (Wwox–Brca1, CC BY-NC-ND) — copyright-verified open, never dispatched.

## Permanently evidence-blocked — do not retry automated routes
`15126504` (`FT-024`, no PMCID) · `27569545` (`FT-105`, **licence wall**, verified) · `15026124`
(no PMC) · `33914858` (no PMCID) · `24369382` (empty PMC body) · `17803050` (no DOI/PMCID).
Packaged for a human in `acquisition_packet_20260920.md`.

**Added 2026-09-21, each verified with `get_copyright_status` and/or `convert_article_ids` — do not
re-test:**

| PMID | Why it is blocked | Where it now lives |
|---|---|---|
| `18371080` | **no PMCID** (record returns the PMID alone); Wiley paywall | `FT-109` · packet **`A6`** |
| `25416187` | PMCID **`PMC4935222` exists but is a metadata-only stub** — `full_text:""`, `is_open_access:false`, `found_in_pmc:0` | `FT-090` · packet **`A7`** |
| `26345274` | **no PMCID** | `FT-032` · packet **`A8`** |
| `33134515` | licence wall | `FT-098` |
| `33300063` | ⚠️ **weaker than first written — see the correction below** | `FT-074` |
| `31966718`, `36621327` | verified unobtainable earlier in this session | `FT-074` |
| `30094525` | ⚠️ **weaker than first written — see the correction below** | `FT-032` |
| `11719429` | ⚠️ **weaker than first written — see the correction below** | `FT-032` |
| `17360458` | `PMC1820689` exists, PNAS 2007, **not OA-licensed**; a local PDF exists but **this checkout has no PDF tooling** | `FT-032` |
| `28123895` | `PMC5214935`, `idIsNotOpenAccess` / `pdf_only` per the surface census | `FT-018` |

🔴 **CORRECTION TO THE THREE ROWS MARKED ABOVE, made the same hour, against myself.**
`is_open_access: false` is **not** a statement that a paper is paywalled. For `33300063`,
`30094525` and `11719429` the tool returned `source: "not_available"` with
`checked_sources: ["pubmed"]` — **PMC was never consulted**, so the flag records *what was not
checked*, not *what is not there*. Demonstrated within this session: `41124647` returned
`is_open_access: false` with `checked_sources: ["pubmed"]`, and its body then came back **in full at
68,491 characters**. Those three rows are therefore **not verified blocked**; they are *untested*.
The authority on whether a PMCID exists is **`convert_article_ids`**, and the only authority on
retrievability is **attempting the fetch and measuring the body length**. The rows that ARE verified
are the ones where `checked_sources` includes `pmc`, or where a fetch was attempted and returned an
empty body.

⚠️ **The stub trap, stated once so it is not rediscovered:** a **PMCID existing does not mean a body
exists**. `PMC4935222` resolves, round-trips through `convert_article_ids`, and returns HTTP success
with `"full_text":""`. **Check `get_copyright_status` for `found_in_pmc` and `is_open_access` before
dispatching a read**, and treat an empty body as a licence wall, not a transient failure.

**Copyright-verified OPEN and still unread:** `27869163` (Wwox–Brca1, CC BY-NC-ND 4.0, PMC5398941) ·
`35573960` (Front Pediatr 2022, `PMC9100683` — the tool reports `is_open_access:false` with a null
licence field, but Frontiers deposits full text, **so this one is worth exactly one fetch
attempt**).
