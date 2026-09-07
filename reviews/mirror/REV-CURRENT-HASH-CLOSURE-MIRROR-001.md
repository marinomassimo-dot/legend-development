---
artifact: MIRROR hostile review (Annex C.2) — current-hash closure, control plane and locators
review_id: REV-CURRENT-HASH-CLOSURE-MIRROR-001
object: CPROOT `a3efcb0` · REPOSURFACE `47c6e2c` · APQCONS `897bef7` · ADJFAILCLOSED `775e44e` ·
  RELSURF `bf9c807` · GOVTESTS `c1294fd` · ORCHMAJOR2-A `abdcc7f` ·
  Scientist A's locator packet `CC-20260826-LOCATOR-PACKET-01` on `lettore` `7ecbe43`
supersedes_verdicts_on: APQCONS and ADJFAILCLOSED — the verdicts in REV-P0-CANDIDATES-MIRROR-001
  and REV-P0-CONTROL-PLANE-DETERMINISM-MIRROR-001 were against content hashes that have moved,
  and are labelled STALE_REVIEW in § 1 rather than propagated
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: TWO BLOCKING FINDINGS WITHDRAWN AGAINST THE NEW HASHES · one control-plane shadow still
  open · and the canonical registry states a source predicate the source does not carry, which
  my own previous review propagated
own_gate_delta: release gate `BLOCKS 301 → 301` (+0).
---

# I compressed the output before checking it carried everything, for the second time in one session, and the candidate had already answered me in the lines I dropped

---

## 1 · PHASE 1 — CURRENT_HASH_REVIEW_MAP

`CANDIDATE_CONTENT_HASH` computed with the repository's own
`governance/scripts/candidate_content_hash.py --base <main> --tip <ref>`.

| candidate | reviewed tip | current tip | `REVIEWED_CONTENT_HASH` | `CURRENT_CONTENT_HASH` | `SAME_OBJECT` |
|---|---|---|---|---|---|
| **CPROOT** | — | `a3efcb0` | — | `1cac95c55c1148e5` | **NOT_REVIEWED** → reviewed here |
| **REPOSURFACE** | — | `47c6e2c` | — | `1e3db7f782e36d29` | **NOT_REVIEWED** → reviewed here |
| **APQCONS** | `76c8e3c` | `897bef7` | `76afbf85882a6b2a` | `601963b4e59082f6` | **NO — STALE_REVIEW** |
| **ADJFAILCLOSED** | `dc0d5d9` | `775e44e` | `12f454beae107bec` | `ff99959cbd49305a` | **NO — STALE_REVIEW** |
| **RELSURF** | `bf9c807` | `bf9c807` | `541a2631b67e9500` | `541a2631b67e9500` | **YES** |
| **GOVTESTS** | `c1294fd` | `c1294fd` | `16a20ba43ca9e6cb` | `16a20ba43ca9e6cb` | **YES** |
| **ORCHMAJOR2-A** | `abdcc7f` | `abdcc7f` | `756b9320a1853468` | `756b9320a1853468` | **YES** |

`plan-major2-restricted-repair` also moved (`7d24410` → `5e3a757`); the **option** refs A–D did
not, and the option is the object my § 8 checklist addresses.

**Two verdicts are hereby withdrawn as stale and re-derived below against the current hash.** A
verdict is a property of a blob; carrying it forward by branch name is the error I recorded on
2026-08-25 as *"fixed is a property of a blob"*, and it would have been repeated here.

---

## 2 · PHASE 2 — CPROOT_VERDICT

`repo_root()` uses `git rev-parse --show-toplevel` and raises `RootError` rather than falling back.
Nine cases, `lease_state.py` invoked by absolute path so only the environment varies.

| # | case | exit | answer | verdict |
|---|---|---:|---|---|
| 1 | candidate clone root | 0 | `ACTIVE: 0` | baseline |
| 2 | nested subdir `framework/scripts` | 0 | `ACTIVE: 0` | **FIXED** — was exit 2 |
| 3 | outside any repository (`/tmp`) | 2 | `LEASE STATE UNDERIVABLE` | **fails closed** |
| 4 | detached HEAD | 0 | `ACTIVE: 0` | ok |
| 5 | **decoy `runtime/` in the same checkout** | 0 | `ACTIVE: 0` | **FIXED** — the decoy is ignored; the root is derived, not the cwd |
| 9 | reached via a symlink | 0 | `ACTIVE: 0` | ok |
| **6** | **decoy inside a NESTED GIT REPO** | **0** | **`ACTIVE: 1 — lease #1`** | **FINDING R-1** |
| **7** | **`GIT_DIR`/`GIT_WORK_TREE` set, cwd = candidate root** | **0** | **`ACTIVE: 1 — lease #1`** | **FINDING R-2** |
| **8** | **`git` absent from `PATH`** | **1** | **uncaught `FileNotFoundError` traceback** | **FINDING R-3** |

The four cwd cases the candidate targets are genuinely fixed, including the shadow attack I
constructed against the predecessor. Three shadows remain.

### 2.1 · FINDING R-1 — a nested repository shadows the control plane

`git rev-parse --show-toplevel` from inside a nested repository returns the **nested** root. So a
decoy `runtime/orchestrator_lease.md` inside any nested checkout is read as the laboratory's lease
record: exit 0, `ACTIVE by derivation: 1`. Plausible, wrong, and not a refusal — which is the
property § 2 of the brief asks to be impossible. The predecessor's cwd decoy is closed and the
nested-repository decoy is open.

### 2.2 · FINDING R-2 — the environment overrides the derivation

`git rev-parse` honours `GIT_DIR` and `GIT_WORK_TREE`. Standing in the candidate root with those
set, the tool reports a different repository's live lease. The root is derived from the
environment, not from where the caller stands — which is a smaller surface than the cwd and is
still not the repository.

### 2.3 · FINDING R-3 — `git` missing is a traceback, not a refusal

`repo_root()` checks `result.returncode != 0` and does not catch the `FileNotFoundError` that
`subprocess.run` raises when the binary is absent. Exit **1** — the code `--check` uses for a
finding. A module whose stated contract is *"one answer, or a refusal — never a guess"* has a third
outcome.

### 2.4 · The surface is still not observable

`names surface = 0` in every successful case. The module derives the root correctly and **no tool
prints it**, so R-1 and R-2 are invisible in the output. My C-3 finding is unrepaired, and it is
what would have made R-1 detectable by a reader.

`test_repo_root.py` carries 12 tests. Keyword probe: `nested` 0 · `GIT_DIR` 0 · `GIT_WORK_TREE` 0 ·
`FileNotFoundError` 0 · `submodule` 0. **None of the three findings is reachable by that suite.**

**`CPROOT_VERDICT = MAJOR_FINDING.` The cwd defect is closed and the primitive still answers when
it should refuse.**

---

## 3 · PHASE 3 — LEASE_SINGLETON_CLASSIFIER_VERDICT

**No classifier was built, and the candidate says so.** `repo_root.py`'s docstring states that
under per-worktree lease records the Annex I.3 singleton is **unverifiable**, and
`test_repo_root.py:127` pins it:

```
test_two_checkouts_each_with_one_active_lease_both_report_healthy
    "the invariant became verifiable — update the record that says it is not"
```

A test that asserts the defect still exists, so repairing it cannot happen silently. That is the
correct handling of a boundary this seat has named `NORMATIVE_RELEVANCE_BOUNDARY`, and I record it
as a credit rather than a finding.

The distinction the brief asks for — *duplicate observation of one object* versus *two genuinely
distinct ACTIVE leases* — is **not decidable from the lease record format**: the blocks carry
`LEASE_ID`, `ACTOR_ID` and `SESSION_REF`, and two worktrees holding the same `LEASE_ID` are
indistinguishable from two holding different ones **only if the classifier is given both files**.
Nothing gives it both files, because which files to give it is the relevance-set question.

`LEASE_SINGLETON_CLASSIFIER_VERDICT = NOT BUILT, DELIBERATELY, AND PINNED. Blocked on the
relevance-set decision, which is § 12's one genuine governance item.`

---

## 4 · PHASE 4 — APQCONS_CURRENT_VERDICT

### 4.1 · WITHDRAWAL, with lineage

> **Finding P0-5** *(REV-P0-CANDIDATES-MIRROR-001 § 3.2, against `49303af`; re-confirmed against
> `76c8e3c` in REV-P0-CONTROL-PLANE-DETERMINISM-MIRROR-001 § 3)* — *"the documented workflow
> silently drops lineages"*.
>
> **WITHDRAWN for content hash `601963b4e59082f6` (`897bef7`).** Not "now PASS": the defect was
> real on the two hashes it was raised against, and the object has changed.

Re-run of my own battery, unmodified, against the current hash:

```
fixture: dirA/queue.jsonl  dirB/queue.jsonl  dirC/queue.jsonl
SOURCES_DICT_COUNT             dirA/queue.jsonl=3, dirB/queue.jsonl=3, dirC/queue.jsonl=3
LINEAGES_REACHING_CONSOLIDATE  3
in_lines reported              9   (of 9 on disk)
OUTPUT_RECORD_COUNT            5
LOST SILENTLY                  []
EXIT                           0
```

`source_labels()` replaces the stem key with shortest-unique-suffix labels and refuses on
collision. I attacked the new identity logic at CLI level:

| attack | result |
|---|---|
| same file supplied twice | `SOURCE ERROR`, **exit 2** |
| same file via a symlink alongside the real one | `SOURCE ERROR`, **exit 2** — `resolve()` catches it |
| same file via relative and absolute path | `SOURCE ERROR`, **exit 2** |
| deep paths sharing every trailing component but one | labelled `r1/deep/a/b/queue.jsonl`, `r2/…` — counts consistent |
| three files, two sharing the shortest suffix | three distinct labels, `6` input lines, `2` deduped |
| an empty file among real ones | `e/queue.jsonl=0` — reported, not hidden |

And a **CLI-level suite** now exists (`test_consolidate_approval_queue_cli.py`, 220 lines), closing
the *"the only match for `main(` is `unittest.main()`"* gap exactly.

### 4.2 · What survives, and one new finding

| requirement | verdict |
|---|---|
| same basename / lineage loss | **REPAIRED** |
| input / source / output count consistency | **REPAIRED** — 9 of 9 |
| syntax error not sent to the Operator | **PASS** — `SOURCE ERROR … not valid JSON`, exit 2 |
| same ID / different content | **PASS for `str`** |
| **integer ID** | **STILL FAILS OPEN** — `{"APPROVAL_ID": 7, "STATE": "APPROVED"}` and `…"REJECTED"` both kept, no error, exit 0. `identity()` requires `isinstance(value, str)`, so a non-string id is content-addressed and two contradictory decisions coexist |
| malformed date | **REPAIRED** — `"not-a-date"` sorts after legible dates |
| **missing date** | **STILL OPEN** — `['__HEADER__', 'AP-NO-TS', 'AP-DATED']`: no timestamp sorts to position one |
| **NEW — FINDING A-1** | a **directory** or a **missing file** as a source raises `IsADirectoryError` / `FileNotFoundError` **uncaught**, exit 1 — the `CONFLICT` code. `load()` guards `JSONDecodeError` and not `OSError`. Same class as the one just repaired, one exception type over |

`APQCONS_CURRENT_VERDICT = NO LONGER BLOCKING. Three residual findings, none of which loses an
approval: one fail-open conflict guard, one ordering defect, one uncaught error path.`

---

## 5 · PHASE 5 — ADJFAILCLOSED_CURRENT_VERDICT, scoped to the contract

### 5.1 · I measured the wrong thing first, and the candidate had already answered

My battery compressed the output to a seven-number signature and reported **5 states
indistinguishable from a full pass**. The current candidate adds **two lines** the signature did
not capture:

```
SCOPE: this verifies RECIPES — every declared crop is re-rendered from the source PDF and
       compared to its declared digest. It does NOT read the image files on disk, so a
       corrupted local PNG is outside what the line above asserts.
OBSERVED, NOT VERIFIED — nothing: every file under page_adjudications/ is declared by a
       recipe, and every declared artifact is present.
```

Re-measured on **whole stdout + stderr**: **INDISTINGUISHABLE = 0 of 9.**

That is the second time in one session that I compressed an output before checking it carried
everything — the first was scoring `MANIFEST_KEY_REMOVED` as a false pass while the candidate
reported `18` in a clause my regex dropped. The discipline is the same each time and I did not
apply it.

### 5.2 · WITHDRAWAL, with lineage

> **Findings P0-1 (R1/R2/R3) and P0-2** *(REV-P0-CANDIDATES-MIRROR-001 § 1.2–1.3 against `9cb09c0`;
> re-confirmed with two new states against `dc0d5d9`)* — three false passes and an uncaught
> traceback.
>
> **WITHDRAWN for content hash `ff99959cbd49305a` (`775e44e`):**

| state | now |
|---|---|
| `R1` corrupt declared png | `OBSERVED, NOT VERIFIED — 1 declared artifact(s) on disk whose bytes differ from…` |
| `R2` undeclared png | `OBSERVED, NOT VERIFIED — 1 image file(s) present and declared by no recipe` |
| `R3` directory with no `adjudications.json` | `OBSERVED, NOT VERIFIED — 1 directory(ies) holding images with no adjudications…` |
| `R4` malformed recipe JSON | `FAILED — the recipe cannot be read as a recipe:` — **a verdict, not a traceback** |

And Phase 6 of the previous brief is answered in the direction the documentation determines: the
`SCOPE:` line is `NARROW_SUMMARY`, and the directory question is reported as **observation**
separated from the verification claim, which is stronger than either alternative I laid out.

### 5.3 · Scoped to the contract: what remains

The contract is recipe integrity. I do not demand directory integrity — but the new `OBSERVED`
line makes a **checkable directory claim**, and two states falsify it.

| state | recipe verification | classification |
|---|---|---|
| `N2` two artifacts declaring the same `file` | honest — both rendered, both matched | **`SUMMARY_OVERCLAIM`** — after `write`, `PMID17803050` holds **6** png files for **7** declarations, and the line still says *"every declared artifact is present"*. The check counts files-without-a-declaration and never declarations-without-a-file |
| `N3` `file: "../PMID16061658/escaped.png"` | honest — rendered and matched | **`SUMMARY_OVERCLAIM`** — `write` **did** escape into another study's directory (verified: `escaped.png` exists there), and the observation fires with the wrong cause: *"declared by no recipe"*. It is declared, by the wrong recipe, in the wrong place. `verify` exits 0 |
| `N5` zero-area crop | **corrupted** — the renderer raises | **`IN_SCOPE_FALSE_PASS`-adjacent: uncaught `FzErrorArgument` traceback, exit 1.** A renderer failure during the promised verification produces a stack trace instead of a verdict. The recipe-JSON traceback was fixed; this one was not |
| `N1` stale png no longer declared | honest | `OUT_OF_SCOPE` — summary differs (26 of 26), detectable |
| `N4` duplicate artifact entry | honest | `OUT_OF_SCOPE` — summary differs (28 of 28) |

`ADJFAILCLOSED_CURRENT_VERDICT = CONDITIONAL_PASS ON THE STATED CONTRACT.` Recipe integrity is
verified honestly in every state I could build, and the `SCOPE:` line makes the boundary explicit
for the first time. Three findings sit on the new observation line and on one unguarded renderer
path — none of them a false pass of the promise, all of them a claim wider than the check.

---

## 6 · PHASE 6 — REPOSURFACE_CURRENT_VERDICT

The candidate replaces `(path/".git").exists()` with *"looks like a checkout **and** this
repository tracks nothing inside it"*. Its own measurement is sharper than mine: dropping a bare
`.git` into `governance/` removed **35 tracked documents including `GOVERNANCE_v3.1.1.md` and
every annex**, and turned `BLOCK_PUBLICATION / 1` into `PASS / 0`.

| # | case | files | verdict |
|---|---|---:|---|
| 1 | stray untracked `.git` in a **tracked** directory | 551 = baseline | **FIXED — no longer pruned** |
| 2 | real nested clone, untracked | 551 | correctly pruned |
| 4 | tracked vendored directory, no marker | 552 (+1) | correctly included |
| 5 | gitignored local backup directory | 551 | correctly excluded |
| 3 | real nested clone **+ a force-added outer file** | 551 | **TEST INVALID — the state is not constructible**: `git add -f` inside a nested repository tracks nothing (`0` paths under `vendorclone/`, no gitlink). I report this as an attack I could not build, not as a case the predicate passed |
| **6** | **force-added tracked file under a `SKIP_DIRS` name** | **551** | **`FALSE_EXCLUDE`** |

### 6.1 · FINDING S-1 — the name-based allowlist the gate warned against is still there

`backup/forced.md` is **tracked** (`git ls-files` confirms). `SKIP_DIRS` at line 41 contains
`backup`, and `walk_publishable` skips it at lines 130 and 139 **before any tracked check**. So a
tracked, publishable file is never scanned.

The gate's own `unpublishable_paths()` docstring says exactly this:

> *"a file that is gitignored but has been force-added **is** tracked, is therefore publishable,
> and must still be scanned — **an allowlist keyed on directory names would silently exempt
> exactly the case that matters**."*

`SKIP_DIRS` is that allowlist. The repair moved the `.git` marker from a filesystem name to
repository content and left the directory name doing the same job.

**FALSE_INCLUDE: 0** · **FALSE_EXCLUDE: 1 class.** Live blast radius **0** — measured across
`main`, `mirror`, `lettore`, `lettore-b`, `lettore-c`, `evidence-index` and `orchestrator`, there
are **zero** tracked paths under any `SKIP_DIRS` name. Latent, and the realistic trigger is a
force-add during a recovery, not an attacker.

`REPOSURFACE_CURRENT_VERDICT = PASS_WITH_FINDING.` It closes the defect it names, over-reaches
nowhere, and leaves one sibling of the same class that its own comment already describes.

---

## 7 · PHASE 7 — MAJOR2_A_REVIEW_READY

Option A is unchanged (`abdcc7f`, `756b9320a1853468`). Adoption is not assumed. The checklist,
prepared and executable the moment an A-shaped candidate is routed:

| # | check | how to falsify |
|---|---|---|
| 1 | **`WORK_COMMIT` remains possible** | the clause must not forbid a commit on the actor's own branch. Test by the counterexample table's row 1, not by reading the sentence |
| 2 | **self-canonicalisation blocked** | row 4: Orchestrator's own work inside a batch. GATE 1 already says *"mai lavoro proprio"* — confirm the clause does not weaken it |
| 3 | **direct `main` commit outside a batch is governed elsewhere** | rows 2 and 5 are the discriminating cases: A does **not** prohibit them. Name the clause that does, or record that only § 35.1's *"usare la root come spazio libero"* covers it |
| 4 | **no ORCHSURF rev-4 import** | diff the file list; rev 4 carries `session_home:` and `canonical_batch_surface:`. A must carry neither |
| 5 | **root clause coherent** | *"or treat the root as free working space"* must still stand and still mean something once `worktree: orchestrator` moves the work surface off the root |
| 6 | **no new authority term** | A introduces none: `CANONICAL_BATCH_COMMIT` has 10 normative occurrences and its gates are body § 12. Verify by grep, not by reading |
| 7 | **body alignment** | § 35.1 is the source of the clause and precedence ranks it 1 against role contracts 4. Whichever option is adopted, this remains open and is the Operator's to route |
| 8 | **fingerprint containment** | only `orchestrator` may move: `88dea7a6…` → `756b9320…`; mirror, plan, scientist byte-identical |

`MAJOR2_A_REVIEW_READY = YES, by hash. A new A-shaped candidate will be reviewed against its
content hash on appearance, not against the branch name.`

---

## 8 · PHASE 8 — FIVECLAIM_LOCATOR_REVIEW_STATUS

`CC-20260826-LOCATOR-PACKET-01` on `lettore` `7ecbe43` is addressed *"For: Mirror, or any reviewer
performing a `legend-locator-audit`"* and declares itself *"a verification instrument. Asserts no
claim and changes nothing."* It carries a `DO_NOT_INFER` line per entry and **withholds the
candidates the locators support**, so a `NO` verdict is available without contradicting a
narrative. That design is the reason this review could be done without routing: **verifying a
surface is not adjudicating a claim**, and I have adjudicated none.

14 locators. Two verified mechanically in this session — the two that bear on the highest-priority
claims.

### 8.1 · L-037-b — `PIXEL_MATCH`, exact

| dimension | result |
|---|---|
| `SURFACE_EXISTS` | **YES** — `files/fulltext/PMID19500159_Suzuki2009.pdf`, 11 pages |
| artifact digest | **MATCH** — `e1a0a87dc7faac00…` equals the declared `sha256` |
| `LOCATOR_CORRECT` | page 9 contains `Table 2` and `Epilepsy` |
| `PIXEL_MATCH` | **MATCH** — crop `(40, 60, 560, 470)` at 400 dpi → **2890 × 2279**, `sha256 290cfc8b31d59afc…` **byte-identical** to the declared value |

The visual recipe reproduces exactly. The instrument is sound.

### 8.2 · L-037-a — `TEXT_MATCH` yes, and the fact is not the one the registry states

The sentence exists verbatim on page 2:

> *"Although neither epileptic seizures nor abnormal behavior **has been reported** in Wwox KO
> (knockout) mice, our preliminary experiments showed that sound stimulation often induced WR in
> lde/lde rats."*

`EXPECTED_FACT_TO_VERIFY` — that the predicate is *"has been reported"*, a statement about the
literature, not about the animal — **CONFIRMED**.

I then widened before asserting a count, because the registry states one. Every sentence in the
paper pairing a mouse term with a seizure term:

| page | sentence | kind |
|---|---|---|
| 2 | *"Although neither epileptic seizures nor abnormal behavior **has been reported** in Wwox KO mice…"* | about the **literature** |
| 9 | *"Although the reason for **no detection** of spontaneous epilepsy in the KO mice is unknown, in addition to genetic background and species specificity influencing on survival and epileptogenesis…"* | about **observation**, with the authors' own alternative explanations |
| 10 ×2 | reference-list titles | not assertions |

And Table 2's row, read from the text layer: `Epilepsy | Wild running and tonic–clonic convulsion`
— the value sits in the `lde/lde` column and the mouse columns are **blank**.

**I then checked whether the caption defines a blank, because if it does my reading is the error.**
It does not, and what it says instead settles the question:

```
Table 2: Phenotypic comparison in the WWOX mutated animals
    ∗Wwox−/–      †Wwox gt/gt      lde/lde
    ∗Data from Aqeilan et al. 2007, 2008, and 2009.
    †Data from Ludes-Meyers et al. 2007.
    ‡Hypoproteinemia, hypoglycemia, …
```

Three footnotes, none of them about blanks. **Both mouse columns are marked `∗` and `†` — they are
populated from the cited literature, not from this paper's own observation.** A blank in a column
sourced from other people's publications is *not reported in that literature*, which is the same
epistemic predicate as the page-2 sentence. And blanks are ordinary in this table: `Dwarfism` and
`Tumor formation` each carry two values for three columns.

So the table does not merely fail to state a negative — **its mouse columns are a literature
summary**, and reading a blank there as a measured absence inverts what the column is.

**`CLAIMED_FACT_SUPPORTED`: PARTIAL, and the registry says MORE than the source.** `CLAIM 005`
currently reads:

> *"that terminus asserts the opposite for the mouse: PMID 19500159 states **in three places**, and
> in a Table 2 whose Epilepsy row is empty for both mouse models, that Wwox-null mice **show no
> epilepsy**."*

Measured: **two** substantive statements, not three; and both predicates are **epistemic** — *has
been reported*, *no detection* — not the ontological *show no epilepsy*. A blank cell in a
comparative table is the third, and a blank is not a printed negative.

`CLAIM 037` is closer to its source: its Italian reads *"non hanno epilessia **riportata**"* and its
evidence boundary already records the authors' hedge. The divergence is **inside `CLAIM 005`**, and
`CLAIM 005` is `consolidated baseline`.

**`NEGATIVE_ARM`: the prohibition survives its stated basis.** `CLAIM 005`'s normative sentence —
*"No canonical statement may describe a Wwox-null mouse as showing epileptogenesis"* — is
**unaffected**: *not reported* and *not detected* both forbid asserting the positive. What
overstates is the **evidence description**, not the rule it supports.

### 8.3 · I propagated the stronger reading, and correct it here

In `DECISION-MINIMIZATION-AND-RECORD-SCOPE-SPEC-001` § 3.1, check 6, I wrote:

> *"Distinguish that from Table 2's **empty `Epilepsy` row**, which is a **reported negative**."*

That is the overstatement, in my own checklist, in the row whose whole purpose is *not-reported vs
absent*. The blank cell is at best **not reported**. **Corrected here rather than left standing**;
the checklist item is otherwise unchanged and its distinction is exactly the one the packet tests.

`FIVECLAIM_LOCATOR_REVIEW_STATUS = 2 of 14 verified mechanically · 1 PIXEL_MATCH exact ·
1 TEXT_MATCH exact with the claimed fact PARTIAL and the registry saying more than the source.
No claim adjudicated.`

`CLAIM006_REVIEW_STATUS = NOT STARTED` — `L-007-a/b/c` are in the packet and unverified; they need
`files/fulltext/` artefacts I have not confirmed present.

`DOSE_REVIEW_STATUS = NOT STARTED` — `L-DOSE-a/b/c` are in the packet, and per the brief's own
ordering they follow the five-claim package.

---

## 9 · PHASE 9 — THERAPEUTIC_REVIEW_READINESS

Scientist B's surface is `lettore-b` `b80ae8b`, 20 ahead of `main`. Templates prepared, none
executed — the six required dimensions per target:

| target | `DIRECT_MEASUREMENT` | `TRANSFER_BOUNDARY` | `COMPARATOR` | `NO_GLOBAL_RESCUE_OVERCLAIM` |
|---|---|---|---|---|
| **NMDAR upgrade** | which subunit, which preparation, protein or current? | a receptor measured in one preparation is not a synapse in another | is the comparison drawn against WT, or only KO-vs-treated? | an upgrade in an epistemic tag is not an upgrade in evidence |
| **gap-junction downgrade** | what was measured — coupling, dye transfer, transcript? | a downgrade needs the same standard of evidence as an upgrade | the negative arm must be able to have detected it | a downgrade that removes a claim is a baseline reversal: MIRROR_REQUIRED |
| **AAV9 endpoint split** | list every endpoint and the direction of each | `CLAIM 011` already records that Fig 3B resolves survival and glycaemia and **not** ECoG/SWD, myelination, gliosis | one significant endpoint is not "rescue"; check whether the effect appears in WT too | this is the specific overclaim to test |
| **CLAIM 016 / 035** | five orthogonal biochemical assays and a point mutation are not a seizure endpoint | is 035 the mechanism 016 asserts, or a different one at the same target? | both `in observation`, both `DATO + INFERENZA`, **not cross-referenced** | do not let a residue-mapped inhibition become a seizure claim by adjacency |

Every row additionally requires a `LOCATOR` resolved independently and a `STATISTICAL_STATUS` read
from the panel rather than the text — `L-011-c` in Scientist A's packet is exactly that shape
(*"a printed p-value against a plotted point count"*).

**mTOR / lithium: deliberately not reviewed.** No canonical surface is touched and no routing makes
it useful; reviewing it would consume the budget the AAV9 endpoint split needs.

---

## 10 · PHASE 10 — JSONL_RECORD_PLUS_PAPER_STATUS

Hardened and unchanged in conclusion. Ten declared fixture classes, four scopes, the real gate:
FILE is wrong on **9 of 10**; RECORD on 3; **`PAPER(pmid → doi)` is right on 9 of 10**, the tenth
being the malformed record, which belongs to the fail-closed parse rule and not to scope.

Key precedence is load-bearing and measured: two records with **different PMIDs and one shared
DOI** must not group, and a doi-first key would group them. Live tree: verdict-identical to today
(494 / 489 / 5) with the same recovery of the suppressed `fulltext_read_receipts.jsonl:83`; the
corpus seed is **706 records → 706 paper groups**, so the grouping costs nothing now and is what
stops the same-paper split the day a second record per paper arrives.

**No email or operator privacy policy is decided here.**

---

## 11 · WHAT_WOULD_CHANGE_MY_MIND

- **§ 2.1** — if a nested repository inside a LEGEND checkout is impossible by construction
  (a rule I did not find), R-1 is unreachable and drops to a hardening note.
- **§ 5.3 N3** — if `write` is only ever run on a recipe that a reviewer has read, the traversal is
  caught by the reader and not by the tool, and my finding is about a workflow that does not exist.
- **§ 6.1** — if `SKIP_DIRS` is deliberately a hard exclusion that outranks tracking, S-1 is a
  decision and not a defect. Test: find the decision record. I found the opposite in the gate's
  own comment.
- **§ 8.2** — if *"states in three places"* counts the two sentences plus the table row, the count
  is defensible and only the **predicate** overstates. That still leaves *"show no epilepsy"*
  unsupported, which is the half that matters, and I would narrow the finding rather than drop it.
- **§ 8.3** — this was my open doubt and I closed it rather than leaving it: I checked the caption
  and the three footnotes, and none defines a blank. What would change my mind now is a legend or
  a Methods sentence elsewhere in the paper declaring the convention, or the rendered page showing
  a mark the text layer drops — I read the text layer, and `L-037-b` exists precisely because a
  text layer is not the printed page. **Rule 5d applies to my own reading here**: the crop
  reproduces byte-exactly, and I have not adjudicated the row against the rendered pixels.
- **§ 8.2** — the two mouse columns being literature summaries is read from footnote markers in
  the text layer. If the markers attach to different columns on the printed page, the inference in
  § 8.3 changes.
