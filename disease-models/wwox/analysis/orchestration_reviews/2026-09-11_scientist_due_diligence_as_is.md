# Due diligence — the Scientists' way of working, as it is (post-Aqeilan sweep)

**Written:** 2026-09-11 · **By:** `orchestrator` (`ORCH-SCIENTIST-IMPROVEMENT-20260911`) ·
**Scope:** the 2026-09-09 Aqeilan sweep (3 Scientists, 23 papers assigned, 11 waves) and the 81
deep-dive manifests, 54 dossiers, 35 session evaluations and 78 commit candidates the repository
holds today · **Method:** every number below was produced by a command run on this checkout on
2026-09-11 or read from the primary record it names; the retrospective's counts are cited as its.
This document **consolidates** the error analysis
([`2026-09-10_scientist_improvement_roadmap.md`](2026-09-10_scientist_improvement_roadmap.md),
[`data/2026-09-10_scientist_incident_controls.jsonl`](data/2026-09-10_scientist_incident_controls.jsonl))
with the pattern analysis reported to the operator the same afternoon. It changes nothing; it is
the picture of the state of the art *as is*, with its fragilities ranked.

---

## 1 · Executive summary

- **Errors.** Six near-errors were one step from the record; machines caught none. Five of six are
  now refused or made visible on their own fixture; one (a cross-panel bridge across two cell
  lines) still depends entirely on a blind reviewer. Detail in § 3.
- **Extraction without use.** 1,458 verbatim locators were captured; the claim registry cites
  **zero** of them by index, dossiers cite them in 6 of 54 files, and 189 of 1,536 propositions
  (12 %) bind to any claim. 28 % of "propositions" exceed 400 characters. § 4.
- **Figures and tables are the weakest surface.** 14 of the 52 incidents (27 %) are about pixels,
  panels, resolutions or tables; 495 locators (34 %) stand on a figure; every measurement was done
  by hand with no shared instrument. § 5.
- **Process text outweighs scientific text.** 132 commits and 33,142 words of commit message in
  three days; a 152-line self-evaluation per wave; state files of 300–480 KB reloaded at every
  resume; five rate-limit kills in two days and 3 of 11 waves without a self-evaluation. § 6.
- **The controls that work best are the rarest.** Two blind audits ran in the whole sweep and
  corrected 7 of 13 and 6 of 10 triples. Self-review by the author caught 1 of 13 on the actor
  that was audited. § 7.
- **There are real best practices, and they are personal, not systemic.** Thirteen are listed with
  their evidence in § 8; none is enforced, most are not even in the brief.
- **Three sessions ran out of budget mid-work.** Nothing was lost in any of them, because durable
  state was written before the expensive step in two cases and reconstructed from the dossier in
  the third — the recipe is documented in § 9 and is the strongest procedural finding of the sweep.
- **Fragility register**, ranked, in § 10; recommendations, not implemented, in § 11.

---

## 2 · What the corpus is, in numbers (2026-09-11)

| Object | Count / size |
|---|---|
| Deep-dive manifests | 81 · median 22 KB · max 67 KB (`PMID31543760.json`, 41 locators) |
| Verbatim locators | 1,458 · median 17 per paper · max 41 |
| Locator surfaces | body 873 · figure 495 · table 26 · supplement 31 · undeclared 33 |
| Locator relation markers | `panel_text_relation` on 1,228 · `qualifies` 68 · `contradicts` 63 · `audit_status` 10 · `contradicts_locator` 0 |
| Propositions over 400 characters | 413 of 1,458 (28 %); median 210 chars; max 2,123 · `python3` over `deepdive_manifests/*.json` |
| Dossiers | 54 · median 178 lines · max 889 · 10,804 lines total |
| Commit candidates | 78 · median 148 lines · max 850 |
| Session evaluations | 35 · median 77 lines; the sweep's 10 · median 152 · max 238 |
| Full-text queue | 4,324 lines · 302 KB, append-only |
| Paper registry · literature log · claim registry | 402 KB · 480 KB · 112 KB |
| Retrospective of the sweep | 1,066 lines · 81 KB |
| Commit messages 2026-09-09 → 11 | 132 commits · 33,142 words · median 189 words · max 1,070 · `git log --since=2026-09-09 --format=%B` |

Producer: `python3` over the directories named, `git log --format=%B | wc -w`, `wc -l`.

---

## 3 · The error picture, consolidated

The six near-errors (retrospective § 5.2), their catcher then, and their control now:

| ID | Case | Caught then | Control now (landed) | Still human |
|---|---|---|---|---|
| NE-1 | false correction of a correct locator, 29724996 Fig 6A, read at 667 px | the reader's rule | `contradicts_locator` validated; unaudited → not a complete read; undeclared rewrite visible from history and in the working tree (`de3628b`) | whether the correction is right; the native-resolution rule |
| NE-2 | screen called with inverted arguments, green over a filename | the reader's disbelief | call-shape guard; every screen names its bytes; exit 2 over nothing (`db35127`) | whether the bytes were the intended surface |
| NE-3 | cross-panel bridge NIH 3T3 vs SAOS-2, 15070730 | blind auditor | **none structural** — proposal only | everything |
| NE-4 | PMID from a search while in the artefact, 31428585 | both auditors | provenance WARN + declaration; calendar check | pertinence |
| NE-5 | REFUSED accepted without its reason, 25245215 | coordinator | verdict names its signature; positive and negative fixtures | corruptions no signature knows |
| NE-6 | derived surfaces regenerated over peers' uncommitted manifests | the actor, reverted | `derived_inputs.py` refuses dirty inputs in four generators (`4810628`) | whose the file is |

Two things the error picture alone hides, and § 4–7 make visible: the six near-errors sit on top of
a working pattern that produces far more material than the model uses, and the two mechanisms that
caught the worst of them (a rule applied in the right order; a blind reader of triples) are the ones
the process invests least in.

---

## 4 · Extracted much, used little

| Question | Measured |
|---|---|
| How many locators exist | 1,458 across 81 manifests |
| How many propositions bind to a claim node (pathograph, `pathograph_inventory.md`) | 189 of 1,536 scanned (12 %); 424 carry a relational connective; 244 of those are "low (ambiguous / degenerate)" · `pathograph.py` inventory |
| How many manifests bind to any claim at all | 37 of 81 · `pathograph.py` inventory |
| How the claim registry cites its evidence | 29 distinct PMIDs, 9 receipt IDs, **0** `entries[N]` references |
| How dossiers cite locators | 6 of 54 dossiers reference an `entries[N]`; 34 references in total · `grep -l 'entries\['` over `fulltext_dossiers/*.md` |
| How the sweep's commit candidates cite locators | 20 candidates reference 32 distinct entry indices — against ~600 locators captured in the same sweep |
| What a "proposition" looks like | median 210 characters; 413 (28 %) longer than 400; the longest is 2,123 characters — a paragraph with the authority of a quotation |

**Reading.** The locator is the right unit of evidence and the discipline of capturing it while the
document is open is sound. But the *volume* is uncoupled from what the model absorbs: a paper yields
17–41 locators, a claim cites none of them by address, and downstream documents re-describe the
evidence in prose. The cost is paid three times — capture, validation (the strict validator
verifies every snippet against the artefact), and rereading at every resume — and the benefit is
realised for roughly one locator in eight. The long propositions are the visible symptom: when the
reader is not choosing, the reader transcribes.

---

## 5 · Figures, panels, pixels, tables — the full incident list

14 of 52 incidents in the retrospective's tables concern a visual or tabular surface. Classified:

| Class | Incidents | What happened | Root pattern |
|---|---|---|---|
| **Resolution** | B1 | bars counted at a 667 px PMC rendering; the publisher PDF holds vector art, crisp at 400 dpi | no rule "native surface first"; the reader started from the convenient asset |
| **Wrong image taken for the figure** | B15 | `pdfimages` returned a 1447×1521 Separation layer that *is not* the figure; the real one is the 697×565 JPEG | tooling returns layers, not figures; "bigger is better" is the natural wrong move |
| **Structural fact from indirect evidence** | B5 | "no supplementary figures in this PDF" concluded from per-page text lengths; `pdfimages -list` showed 16 images | a property of the file asserted without the command that measures it |
| **Hand segmentation** | C12 | colour segmentation attributed 13 px of the plot frame to a signature in every column; a legend border mistaken for a swatch | bar-chart reading done with ad-hoc pixel code, no calibration step |
| **Hand baseline** | C13 | baseline placed on the x-axis *labels* (y=1992) not the axis (y=1574); every bar read ~25 | same |
| **Panel joined across systems** | A9 | Fig 6 → Fig 5 bridge across NIH 3T3 and SAOS-2 | no field for the experimental system on a relation |
| **Caption absent** | A10 | which panel is "reduced dose" is an assumption, Fig 5 has no caption | assumption not declared |
| **Background knowledge on a figure** | A11 | Fig 2A markers named as known phosphosites; the article names one | textbook default used as a datum |
| **Coverage by analogy** | B17 | `figures: read` nearly recorded on 20146584 by analogy with a sibling paper | refused; the partial downgrade taken |
| **Own reasoning tested** | C21 | an apparent Fig 3c-vs-3d contradiction and a β-actin confound both **refuted** by measuring | the good pattern (§ 8) |
| **Relation marker on the wrong side** | B6 | five coupled locators marked on the text side | schema learned, not applied |
| **Table rows as furniture** | C20 | the intrusion tool's `TABLE_ROW_RE` produced 25 false positives because PyMuPDF emits one cell per line | a tool written mid-lot against one paper's layout |
| **Validator rejections on figure locators** | A7 | four rejections: needle collisions, a panel pointing at a panel, short needles | schema friction, not error |

Three more facts bound the picture. **(a)** In the sweep `fitz`/PyMuPDF was *absent* (I2), so the
canonical remedy for a SUSPECT text layer — anchoring locators to rendered pages — ran only through
`regenerate_adjudications.py`; it is present now (1.28.2, pinned). **(b)** PMC began serving a
reCAPTCHA mid-sweep (I3), which cost 20146584 its two figures and its `complete` depth; the figures
were recovered on 2026-09-11 from the article's CDN routes and are verified real. **(c)** Where the
readers *did* have a method — `scientist-c`, 15 of 15 panels at 200–900 dpi, Table 1 read as text
*and* re-read on the page — the figure work produced the sweep's most defensible measurements
(C21). The difference between the good and the bad figure readings is not care; it is whether a
measurement had a second instrument to disagree with.

---

## 6 · Process text, tokens, and the sessions that die

| Signal | Measured |
|---|---|
| Closing writes per wave | self-evaluation (median 152 lines) + capability-scout entry + task-record wave block + narrative commit message (median 189 words) + dossier (median 178 lines) + commit candidate (median 148 lines) |
| Commit prose | 33,142 words in three days — the length of a short book, in messages |
| State reloaded at resume | queue 302 KB, paper registry 402 KB, literature log 480 KB, retrospective 81 KB, brief 16 KB, core 31 KB |
| Rate-limit kills | 3 during the sweep (retrospective I1) + 2 on 2026-09-10 → 11 = **5 in two days** · `2026-09-09_actor_retrospective.md` § 6.4 and `2026-09-10.md` § 2g |
| Waves without a self-evaluation | 3 of 11 — exactly the three killed · `2026-09-09_actor_retrospective.md` § 6.4 |
| Paper landing cadence (afternoon waves, from commit timestamps) | 12–60 minutes between successive paper commits per Scientist; a short editorial and a 26-page primary sit in the same pipeline |
| Tools written by Scientists *during* reading waves | 4 in one day (`oa_status_dissent`, `manifest_flag_drift`, `genre_discriminator`, the intrusion check); one produced 25 false positives on its second paper (C20) |

**Reading.** The obligations the brief places on every wave — self-evaluation, micro-upgrade,
attribution census, `DEFAULTS_TAKEN`, `STOP_LOG`, a full commit narrative — were each earned by a
real incident and each is defensible alone. Together they make the closing of a wave cost as much as
the reading, and the *"one micro-upgrade per session"* rule has turned readers into tool authors at
the moment they are least able to test a tool. Token exhaustion is the direct consequence: the
sessions die at the end of the wave, when the closing writes are being produced, which is why the
three killed waves are precisely the three without an evaluation. Nothing scientific was lost
(§ 9), but the process is operating at the edge of its budget by design.

---

## 7 · Review: what catches what

| Reviewer | Runs in the sweep | Yield | Cost |
|---|---|---|---|
| Blind locator audit (triples only, no conclusions) | 2 (R4 fired on consolidated-baseline claims only) | 7 of 13 and 6 of 10 triples corrected; two factual attestations found wrong; one unsupported clinical claim found by omission (§ 1.4) | one auditor session per audit; two were killed by a rate limit mid-run · `2026-09-09_actor_retrospective.md` § 1.1, § 1.4, `AQEILAN-FT-A-001.json` WAVE_2_RESULT |
| Author's own re-reading | every wave | on the audited actor: 1 of 13 incidents self-caught (retrospective § 5.1) | free, and nearly blind to the author's own preferred finding · `2026-09-09_actor_retrospective.md` § 5.1 |
| Self-evaluation (written diagnosis) | 8 of 11 waves | 4 defects caught and 1 target set (retrospective § 5.3) | ~150 lines per wave · `2026-09-09_actor_retrospective.md` § 5.3 |
| Peer / coordinator | ad hoc | 5 incidents, including B16 | attention of the orchestrator |
| Validators and screens | every write | 24 of 57 incidents — schema, timestamps, needle lengths — and **0 of the 6** near-errors before 2026-09-10; 5 of 6 now | free · `2026-09-09_actor_retrospective.md` § 5.1; `data/2026-09-10_scientist_incident_controls.jsonl` |

**Reading.** The only reviewer with a measured yield on *content* is the blind auditor, and it is the
only one gated behind a threshold. The validators are excellent at malformed declarations and were
blind to wrong content by design; three of today's controls move them one step toward content (a
contradiction must be pointed and audited; a screen must name its bytes; a derivation must name its
inputs), but none of them reads a figure.

---

## 8 · Best practices observed — real, personal, unenforced

Each with the actor, the evidence and where it lives today.

| # | Practice | Actor · evidence | Status |
|---|---|---|---|
| 1 | **Land the reading before the expensive step; write no commit candidate until verdicts exist.** After wave 2 lost an audit to a session boundary, wave 4 lost two auditors and lost nothing | `scientist-a`, retrospective § 1.3 | not in the brief |
| 2 | **Write the limit into the locator instead of being more careful** — declined verdicts at 421×196; a band stated as an ordering, not a cleavage | `scientist-c` wave 3 | not in the brief |
| 3 | **Cross-measurement**: let two instruments disagree (own eye vs two segmentations; arithmetic vs printed totals), and test one's own reasoning to the point of refutation | `scientist-c` C12, C13, C21; `scientist-a` wave-3 eval line 58 | not in the brief |
| 4 | **Pre-verify every snippet against the validator's own extractor before writing the manifest** (caught `µ` vs `μ`) | `scientist-c` C6 | not in the brief |
| 5 | **Two-surface parity** — compare XML and PDF before attributing a missing sentence to the publisher (`finally` vs `ﬁnally`) | `scientist-b` B14 | not in the brief |
| 6 | **Control run of a new tool on papers whose answer is known** before trusting it (found that every primary was flagged) | `scientist-b` B13 | not in the brief |
| 7 | **Make debts specific enough that the answer is recognisable when it appears** — a contradiction in 25245215 closed four hours later by 20146584 | `scientist-b` wave 6 | not in the brief |
| 8 | **Take the downgrade** rather than promote coverage by analogy | `scientist-b` B17 | brief M2 (captions_only) |
| 9 | **Read the erratum / expression of concern as its own source, with its own receipt** | `scientist-c`, 28373548 | practice, not rule |
| 10 | **Correct a persisted wrong value lawfully** — a linked `receipt_correction`, never an edit | `scientist-a` A13 | protocol |
| 11 | **Structured surface first** (XML/HTML before PDF), and record the route | brief M1, from measured PMC behaviour | brief |
| 12 | **Blind audit on omission, not only on error** — the second unsupported clinical claim in 31428585 | retrospective § 1.4 | `roles/orchestrator.md` dispatch rule |
| 13 | **Refuse to derive shared surfaces from in-flight state** — reverted rather than land three actors' work | `scientist-c` C22 | mechanical since `4810628` |

Nine of thirteen exist only as one actor's habit recorded in a self-evaluation. The brief carries
three; one became a mechanism today. That gap — proven practice that no other reader inherits — is
itself a fragility (§ 10, F-7).

---

## 9 · The three sessions that ran out of budget

| Session | Where it died | What was on disk | What was lost | How it was closed |
|---|---|---|---|---|
| `scientist-a` wave 2 (25331887, 33916893) | after the reading and the manifest; the blind audit *completed* but its report never reached the session | manifest, dossier, receipt, candidate **HELD**, 10 SI locators marked `[UNAUDITED]` | nothing scientific; time | the orchestrator relayed the audit verbatim; verdicts applied: SUPPORTED 4, OVERSHOOT 6, five clauses struck, **two attestations factually wrong** (no γ-H2AX foci at 48 h in either genotype) — the candidate was released only after |
| `scientist-b` wave 3 (38499540) | after the full reading (the supplement debt paid) and **before any manifest or receipt** | a dossier with a "mechanical closing recipe" in its § 8; no receipt | nothing — but the paper stayed `partial` in the ledger and was **not** silently marked complete: `ANALYSIS_DONE_RECEIPT_NOT_PERSISTED` | closed a wave later by a receipt, without re-reading; a validator change the session had started was **deliberately not built** on resume ("a validator change written under a rate limit gets its tests written to match whatever it does") |
| `scientist-c` wave 2 (38355659, 21115974) | between a receipt append and its declared discovery-ledger append | receipt appended; LINT at `BLOCK_BATCH_COMMIT: OUTPUT_STUDY_MISMATCH` | nothing; self-evaluation and scout skipped because the resume was scoped to landing only | the intended append was written on resume rather than the receipt walked back; the two obligations were discharged in wave 3 |

**What the three have in common, and it is the finding.** In all three the expensive, irreproducible
step — the reading — had been made durable *before* the budget ran out, and the cheap step was
what remained. Where that order was inverted (wave 3 of `scientist-b`: reading done, nothing
persisted) the recovery still worked because the dossier carried its own closing recipe. No
artefact anywhere describes the process exit itself; the ledger learns about it only from the
next session's first line. The sessions also died at the *end* of the wave, during the closing
writes — which is the cost structure of § 6 expressed as an outage.

---

## 10 · Fragility register, ranked

| # | Fragility | Evidence | Severity · likelihood | Mitigation today |
|---|---|---|---|---|
| F-1 | **Figure and table reading has no shared instrument**; measurements are hand-made pixel code per paper | 14/52 incidents; C12, C13, B15, B1; `fitz` absent during the sweep | high · high | native-resolution rule in the brief; PyMuPDF now pinned; nothing standard (`2026-09-09_actor_retrospective.md` incident tables) |
| F-2 | **Volume of extraction uncoupled from use** — 12 % of propositions bind to a claim; claims cite 0 locators by index; 28 % of propositions are paragraphs | § 4 | medium · certain | none |
| F-3 | **Closing obligations exceed the budget of a wave**; sessions die during closing writes | 5 kills / 2 days; 3 of 11 waves without evaluation; 33k words of commit prose | high · high | resume-by-hand recipe; two streams at a time (`2026-09-09_actor_retrospective.md` § 6.4; `git log --format=%B`) |
| F-4 | **A relation between panels carries no experimental context**, so a cross-system bridge is invisible to every check | NE-3 | high · medium | blind audit at R4 only; proposal written |
| F-5 | **The best reviewer is the rarest** — blind audits run twice per sweep, gated on claim status | § 7 | high · certain | the fourth R4 trigger now includes contradictions |
| F-6 | **Readers write tools mid-lot** under the one-micro-upgrade rule; one produced 25 false positives | C20; four tools in a day | medium · high | none |
| F-7 | **Proven practices are personal**: 9 of 13 live only in one actor's evaluation | § 8 | medium · certain | none (`2026-09-11_scientist_due_diligence_as_is.md` § 8) |
| F-8 | **Uniform depth**: an editorial and a load-bearing primary get the same five-milestone pipeline; the three most important primaries remain unread | § 6 cadence; roadmap § 5.3 | high · certain | `legend-proband-priority-matrix` exists for triage, not for depth |
| F-9 | **Restatement compression** — load-bearing genotype facts sit in reviews the repository cannot check (29808465, 25411445, 15126504) | retrospective § 7.3; receipt `abstract_only` on 29808465 | high · certain | named as debt |
| F-10 | **Acquisition is hostage to publisher defences** (Cloudflare 403, reCAPTCHA) and to the gitignored `files/` tree | I3, I4; 33914858; 428/464 artefacts absent from a fresh checkout | medium · certain | recipes + `reacquire.py` (26/32 recovered); operator's browser for the rest |
| F-11 | **State files grow append-only and are reloaded whole** | queue 302 KB, log 480 KB | medium · certain | none |
| F-12 | **No artefact describes a process exit**; the resume learns it from the next session | § 9 | low · high | `DEFAULTS_TAKEN` in the task record; dossier closing recipes |
| F-13 | **Screens outside the validator run only if the reader runs them** (genre, erratum, OA dissent, flag drift); `session_self_eval.py` executes none | roadmap § 2 | medium · high | enrolled in the battery; not in the reading flow |
| F-14 | **Lot definition shapes the finding** — 20 of 23 PMIDs Aqeilan-adjacent by construction; "independent corroboration" partly reflects how the lot was drawn | retrospective § 7.4 | medium · medium | INTERNAL_EDGES at M0 (`2026-09-09_actor_retrospective.md` § 7.4) |

---

## 11 · Recommendations — proposed, none implemented

Ordered by expected benefit per hour; every item names the fragility it addresses.

1. **A figure milestone with an instrument (F-1).** One standard step: render the page at native
   resolution, crop the panel, and read bars/points with a single calibrated routine that reports
   the axis it found and the pixels it counted — so a second reader can disagree with a number, not
   with an eye. Until it exists, the rule is "two measurements or a declared limit".
2. **A locator budget and a proposition contract (F-2).** At most 10–15 locators per paper, each
   the evidence for one proposition; a proposition is one sentence under ~250 characters; a
   claim that rests on a locator cites it by address. Reduces capture, validation and resume cost
   together.
3. **Depth triage before reading (F-8, F-9).** Editorials, reviews and background papers in a light
   mode (receipt, ≤5 locators, no dossier); load-bearing primaries in the full pipeline with a
   mandatory short blind audit. Read 29808465, 25411445 and 15126504 before any further review.
4. **A short blind audit on every full read (F-5).** Three to five load-bearing triples per paper,
   always, instead of thirteen triples twice per sweep. Run it *on omission* too.
5. **Close a wave in one write (F-3).** A structured self-evaluation of fixed length; commit
   messages of ≤ 80 words with the rest in the record; the capability-scout obligation moved to
   harness sessions. No reader writes a tool during a reading lot (F-6).
6. **Promote the thirteen practices into the brief (F-7)** as one page of "what the readers who
   did well actually did", each with its incident.
7. **`experimental_context` on coupled relations, WARN on discordance (F-4)** — specified in the
   roadmap § 4.
8. **Process-exit artefact (F-12).** A one-line `SESSION_EXIT` record written by the resume
   instruction itself: what was on disk, what was not, what is next.
9. **Run the standalone screens from `session_self_eval.py` (F-13)** over the session's manifests.
10. **Split the append-only state files by year or by lot (F-11)** with an index; the whole-file
    reload is the single largest fixed cost of every resume.

None of these changes the meaning of an attestation; items 2, 3 and 5 are brief changes and
dispatch rules, items 1 and 7–10 are harness work, item 4 is a dispatch rule.

---

## 12 · What this document does not claim

It measures the caught errors and the visible costs; it cannot count the errors nobody surfaced.
Token consumption is inferred from kill counts, text volume and file sizes, not from a meter. The
landing cadence is a commit-timestamp observation, not a measure of reading effort. The best
practices are attributed to the actor whose evaluation records them; an actor that did the same
without writing it down is not credited here, which is one more reason for § 11 item 6.
