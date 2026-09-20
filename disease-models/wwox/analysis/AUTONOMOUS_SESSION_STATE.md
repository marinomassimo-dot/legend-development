# Autonomous session — continuation state

**Updated:** 2026-09-21 · **Purpose:** recovery point. If this session is interrupted, a cold reader
resumes from here. **Not a handoff and not a stop.**

## Current state
- `main` == `origin/main` · working tree clean · one worktree · LINT **PASS** · publication gate
  **PASS, 0 blocks** · receipts **175 chained, tail anchored**.
- Papers with a receipt: **109** (was 97 at the start of the Chang batch).
- **In flight at this write:** two Scientist readings — `FT-102` / `PMID 25650666` (the founding
  `TRAPPC6AΔ` paper, PMC4414138) and `FT-073` / `PMID 27845895` (Hyal-2/WWOX/Smad4, PMC5386674).

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
1. **FT-090** / `PMID 25416187` (PMC4935222) — the single citation carrying `27551470`'s only link
   to the reference genotype. Same "one sentence holds a claim" shape as `CLAIM 039`.
2. **FT-018** / `PMID 28123895` (PMC5214935) — C1q regulates WWOX **activation state**, not level.
   C1q is central to microglial synaptic pruning **and is druggable**. Highest therapeutic upside
   left in the accessible queue.
3. ~~**FT-098 / FT-099** — the other two independent `TRAPPC6A` cohorts.~~ **CLOSED.** `FT-099`
   read (fails its own permutation); `FT-098` licence-walled. With `FT-097` already null, **all
   three legs of the `TRAPPC6A` node-independence claim are down and the claim is retracted in
   full** — see the retraction appended to `chang_ncku_wave2_node_independence_20260920.md`.
4. **FT-092** / `PMID 25238782` — CFS fragility; cross-cutting citation-fidelity finding.
5. **FT-074** — four mTOR/autophagy stubs two reasoning files already lean on.

## Permanently evidence-blocked — do not retry automated routes
`15126504` (`FT-024`, no PMCID) · `27569545` (`FT-105`, **licence wall**, verified) · `15026124`
(no PMC) · `33914858` (no PMCID) · `24369382` (empty PMC body) · `17803050` (no DOI/PMCID).
Packaged for a human in `acquisition_packet_20260920.md`.
