---
artifact: INTEGRATION_CANDIDATE — Orchestrator surface semantics
candidate_id: CAND-20260819-ORCHSURF
revision: 4
task_id: ORCHSURF-001
author: plan
authored_on: 2026-08-20
governance_version: 3.1.1
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file is outside the candidate content domain and cannot move the hash it records
partition: this is the SECOND half of the split declared in CAND-20260819-P5DOMAIN §9. P5 went
  first and is canonical. This candidate carries the Orchestrator surface debt and nothing else
scope_negative: Routing is NOT implemented. No resolver, no registrar, no actors.yaml, no routing
  generations, no CURRENT, no session elected, superseded or registered. Annex D.1 NOT modified.
  Annex I.2 NOT modified and NOT claimed superseded. The governance BODY is NOT modified and NOT
  claimed superseded. P5 NOT reopened. C-9 §7.2 NOT altered. Scientist A/B NOT activated.
  BENCH-AB-001 NOT started
human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here, and none exists
revision_2: remediated B-1, the single blocking finding of REV-ORCHSURF-MIRROR-001, and N-1. The
  remedy is in CONTENT. It does NOT complete the bootstrap transition — it removes the stale
  instructions that recreated the invalid arrangement, and declares the FROZEN residual that no
  lower-precedence document may discharge. §13 records the disposition of every finding. The
  completion claim of revision 1 is WITHDRAWN, in this manifest and in the content
revision_3: the REMEDY IS UNCHANGED. Revision 3 corrects what this candidate SAYS about the
  residual, which was wrong in extent. governance/GOVERNANCE_v3.1.1.md — FROZEN, normative, the
  body every annex derives from — states at §0.2 "La stessa chat viene promossa; non servono due
  chat root", with §0.4 and §47 steps 10 & 14 repeating and executing it. That is B-1's own
  proposition at the highest rank in the system, and the revision-2 package named it nowhere.
  Found by Plan re-reviewing its own package before delivery; not raised by Mirror. §5.5 states
  the finding, §13 re-opens B-1's disposition
revision_4: THE REMEDY DIRECTION IS INVERTED, and not one measurement is withdrawn to do it.
  DEC-20260820-ORCH-SESSION-HOME — RATIFIED by the operator on 2026-08-20 at commit ec4bf60,
  ratified content sha256 9861fb05…c0bee7, record-after-signature sha256 6e89ba5f…e1e1 — states
  that the Orchestrator's SESSION HOME is the repository root by architectural intent, and that
  the `orchestrator` worktree is that actor's WORK_COMMIT surface. Both at once, because they
  answer different questions. Revisions 1–3 read them as rival topologies and proposed to
  extinguish root-promotion; that direction is withdrawn. What revisions 2 and 3 MEASURED stands
  entirely — see §17.1. Three findings are new at revision 4 and none of them was reachable from
  the old direction: body §8 states the architecture at rank 1 and the whole package quoted one
  clause of it against the rest (F-1); the WORK_COMMIT-impossibility premise that grounded the
  fail-closed stop is FALSE and was canonical in main (F-2); and Annex I.2 step 4 and the
  deployment profile were never one list (F-7). §17 carries the disposition of every prior
  finding. NO FROZEN DOCUMENT IS AMENDED, and none is claimed superseded — which is the whole
  point: the residual revision 3 declared HUMAN_REQUIRED is DISSOLVED, not discharged
supersedes: revision 3, CANDIDATE_CONTENT_HASH
  ed020f37c6a33d6c84b0b1eb7a5ed7e3800b4915b599715e3954d1036ab9c1f8 at content tip
  25fa61abe0dfe5c19f11b15d9b906a2e07d64a56; and, transitively, revision 2, CANDIDATE_CONTENT_HASH
  b0a0c9ed6849521a1331a4d6c0850de252ae7c4b5e3b227a477b21f4386465d1 at content tip
  7b6a9d9aeaf2a162fc16de4e4abdb713ddead603; and, transitively, revision 1,
  3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7 at content tip
  b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2. All three bindings are SUPERSEDED, not withdrawn —
  each was correct for the tree it named, all three are reproduced as positive controls in §1, and
  Annex D.2 invalidates them because the bound content moved. REV-ORCHSURF-MIRROR-001 reviewed
  revision 1; NO REVIEW has ever been performed on revision 2, 3 or 4
publication_gate: PASS · 0 BLOCKS at CONTENT_TIP, DELTA 0 against BASE_HEAD. A DIRECT_IDENTIFIER
  block stood at the first revision-4 binding — the `ratified_by` signature in the DEC carried the
  operator's name into public canonical content, and the gate matched it against its register of
  private identifiers. Cleared at 9a70e94 by an operator-approved one-line redaction to
  `Operatore`, the vocabulary the record's own `authority:` field already used; the ratification
  act is unchanged. The history is kept in §1 rather than erased, because a gate measured red and
  then green is worth more in the record than one never measured at all
---

# INTEGRATION_CANDIDATE — `CAND-20260819-ORCHSURF` · revision 4

## 1 · Manifest (Annex D.2)

```
CANDIDATE_ID              CAND-20260819-ORCHSURF
REVISION                  4
BASE_HEAD                 04693e683a254ff0a6d0619fba47103a0fb7d122   (canonical main, read from
                                                                      git at session open and
                                                                      again at binding — never
                                                                      from a manifest or a prompt)
OPERATOR_INPUT            DEC-20260820-ORCH-SESSION-HOME · RATIFIED
                          ratified at   ec4bf603fcdc30dd3b56a92b0102a56eaf838f7e
                          redacted at   9a70e94d6d9863622c22159d0d7f2117b77b793d
                          Each of those two commits changes exactly ONE line, and the line is the
                          signature field — verified by diff, both times.
                          THREE HASHES, all meaningful, none interchangeable:
                            9861fb05c66d4e763f6f1e36e012f6f019a5447356fa35ec87f0153b29c0bee7
                              the content AS RATIFIED, before any signature. Ratification
                              attaches to THIS
                            6e89ba5f23f6a5fd1ae70e7bc339d1cb452b38fb1a5f0c9ffaa22e705fc4e1e1
                              after signature, with a direct identifier. Superseded; it is the
                              value that tripped the publication gate
                            6b5d9c3fd625aed3c72811d8bfff458f38b92f2973aa9b99aa90063df762f83c
                              after identifier redaction — THE RECORD AS IT NOW STANDS
                          The redaction replaced the operator's name with `Operatore`, which is
                          the vocabulary the record's own `authority:` field already used. The
                          RATIFICATION ACT IS UNCHANGED; only its rendering is. Operator decision
                          of 2026-08-20, on the ground that ratification is an operator ACTION
                          and not a public identity assertion.
                          RANK 2 (body §5, OPERATOR STRATEGIC DIRECTIVE), subordinate to
                          NON-NEGOTIABLE governance at rank 1
SOURCE_COMMITS            b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2   CONTENT — revision 1
                          7b6a9d9aeaf2a162fc16de4e4abdb713ddead603   CONTENT — revision 2
                          25fa61abe0dfe5c19f11b15d9b906a2e07d64a56   CONTENT — revision 3
                          1a650d85e7686654e37329576c034b899d43bb40   CONTENT — revision 4, the
                                                                      inverted direction
                          9a70e94d6d9863622c22159d0d7f2117b77b793d   CONTENT — identifier
                                                                      redaction in the DEC
                          <this commit>                              CONTROL PLANE — this manifest.
                                                                      Resolved by the commit that
                                                                      follows; see SELF-REFERENCE
CONTENT_TIP               9a70e94d6d9863622c22159d0d7f2117b77b793d
CANDIDATE_HASH_VERSION    legend-candidate-v4
CANDIDATE_CONTENT_HASH    844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
                          539 included · pre-image 541 lines / 58 040 bytes
REBOUND WITHIN REVISION 4 the first revision-4 binding was
                          79af3e52302aa4ca9fc99e53979904aff2535f28949f2af2a573eee222d82ea0
                          at content tip 1a650d85. It is SUPERSEDED under Annex D.2 because the
                          bound content moved — the DEC is an included domain entry and the
                          redaction changed it. **This is a re-binding, not a revision 5:** no
                          argument, finding, remedy or disposition changed. The domain delta
                          between the two is exactly ONE entry, enumerated below. A reviewer
                          holding that a content change of any kind demands a revision bump
                          should say so; Plan judged the substance unchanged and records the
                          judgement rather than hiding the seam
SUPERSEDED_HASH           ed020f37c6a33d6c84b0b1eb7a5ed7e3800b4915b599715e3954d1036ab9c1f8
                          revision 3, at content tip 25fa61a
                          b0a0c9ed6849521a1331a4d6c0850de252ae7c4b5e3b227a477b21f4386465d1
                          revision 2, at content tip 7b6a9d9
                          3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7
                          revision 1, at content tip b3afdde
                          All three were correct for the trees they named; Annex D.2 invalidates
                          them because the bound content moved. All three are REPRODUCED below
CHANGE_CLASS              MAJOR — unchanged from revision 3. It edits a role contract, the
                          deployment profile and the bootstrap procedure, which is governance
                          (H.1 "governance → Operatore"; Annex G.1 MIRROR_REQUIRED). Classified
                          MAJOR fail-closed; H.1 gives a doubtful MAJOR to Mirror
FROZEN DOCUMENTS          NONE amended, NONE proposed for amendment, NONE claimed superseded.
                          Verified mechanically: `git diff --name-only BASE..TIP` over the body
                          and every annex A–J returns EMPTY. Annex I.2's cardinality of five is
                          AFFIRMED by F-7, not excused
LINT_RESULT               PASS — 1 INFO (MISSING_WIKILINK, CLAIM 010), byte-identical at
                          BASE_HEAD measured in a matched checkout. DELTA 0
PUBLICATION_GATE          PASS · BLOCKS: 0 — and the history is kept, because a gate that went
                          red and back to green is worth more in the record than one that was
                          never measured:
                            at BASE_HEAD, matched checkout        PASS · 0
                            at 1a650d85, first revision-4 binding BLOCK · 1
                            at 9a70e94d, CONTENT_TIP              PASS · 0
                          The block was DIRECT_IDENTIFIER at
                          governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md:14 — the
                          `ratified_by` signature, matched against the gate's register of private
                          identifiers. It was never in this candidate's three edited files:
                          stashing them and re-measuring reproduced the same single block, which
                          is how the cause was attributed rather than guessed.
                          INTRODUCED BY  ec4bf60, the ratification commit
                          CLEARED BY     9a70e94d, operator-approved redaction to `Operatore`
                          DELTA vs BASE  0. The branch no longer carries a publication regression
                          The gate did its job: it caught a registered private identifier entering
                          public canonical content, and it caught it before canonicalization
REGRESSION                NOT RE-MEASURED at revision 4. Revision 3 recorded DELTA 0 against a
                          suite RED at canonical main for a pre-existing reason. This revision
                          does not assert a value it did not take
MIRROR_REVIEW             REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES on revision 1.
                          Revisions 2, 3 and 4 have NEVER been reviewed. None performed, none
                          assumed, and revision 4 inverts the direction revision 1 was reviewed
                          under — so the earlier review does not transfer
HUMAN_APPROVAL            n/a — not requested, not prefilled, and no APPROVAL_ID exists
SNAPSHOT_ID               n/a until canonical execution — GATE 4 belongs to Orchestrator
FINGERPRINT IMPACT        orchestrator  88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb
                                     →  f85d743c8b31597b8c96430ac36b77f62f650b94750f9df941a929dd4022fefe
                          plan · mirror · scientist  UNCHANGED, byte-identical
                          Both ends measured this session — the BASE value in a temporary
                          checkout at BASE_HEAD, not carried from revision 3's manifest. Revision
                          3 PREDICTED f2931147… for orchestrator; that prediction is void because
                          revision 4's roles/orchestrator.md is different content
A.6 CONSEQUENCE           orchestrator checkpoints only. NOT four roles — the body is not
                          amended, so no cross-role rotation occurs. This is the single largest
                          cost the inverted direction removes
SELF-REFERENCE            a manifest cannot name the commit that contains it. `<this commit>` is
                          resolved by the commit that follows, as `c9de134` did for P5DOMAIN and
                          `51d1317` did for revision 2. The seam is harmless because
                          governance/candidates/ is excluded from the hashed domain, so no
                          control-plane commit can move CANDIDATE_CONTENT_HASH. **Fetch the
                          branch tip, not MANIFEST_TIP** — the tip is where the package is whole
```

### Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 04693e683a254ff0a6d0619fba47103a0fb7d122 \
  --tip  9a70e94d6d9863622c22159d0d7f2117b77b793d
# 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
```

**Independent route** — the digest reproduced without trusting the script's own final step, by
re-digesting the emitted pre-image with a different tool:

```bash
… --emit-domain | shasum -a 256
# 844de909…b6dc   (58 040 bytes, 541 lines: 539 domain entries + 2 header lines)
```

**Domain accounting against revision 3 — enumerated, not observed.** The pre-image grew by
exactly **two** included entries, 537 → 539:

```
+ governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md   the operator record, created on this
                                                            branch and absent at BASE_HEAD
+ learning/plan/SLR-plan-0013.md                            the session learning record
~ BOOTSTRAP.md · deployment/deployment_profile.md · roles/orchestrator.md
                                                            same three paths, changed digests —
                                                            these are the candidate's edits, and
                                                            they move the hash without moving the
                                                            entry count
```

537 + 2 = 539, and the three changed digests are the three files this revision edits. Nothing
entered or left the domain unaccounted for.

**Three positive controls — published values authored by earlier sessions, reproduced here at
revision 4.** This is what makes the instrument trustworthy rather than merely self-consistent:

```
ORCHSURF revision 1      base 04693e68 tip b3afdde4  → 3af61c6d…   MATCHES published
ORCHSURF revision 2      base 04693e68 tip 7b6a9d9a  → b0a0c9ed…   MATCHES published
ORCHSURF revision 3      base 04693e68 tip 25fa61ab  → ed020f37…   MATCHES published
```

Revision 3's own value is now a control rather than a claim, which is the strongest form the
check takes: the instrument that binds this revision reproduces the binding it supersedes.

**Three negative controls, verified rather than void.**

```
BASE tree against itself           cfe8957d…1298   ≠ candidate — and it is the value Mirror
                                                    independently measured at revision 1, so this
                                                    control is corroborated from outside Plan
revision 3 vs revision 4           ed020f37… ≠ 844de909…   the binding moved with the content
rev-4 first bind vs the rebind     79af3e52… ≠ 844de909…   exactly ONE domain entry moved — the
                                                    DEC's digest — and the hash moved with it.
                                                    The instrument is sensitive to a single
                                                    redacted field in a single file
SHA-256 of the empty string        e3b0c442…b855   ≠ candidate, and the pre-image is 58 040
                                                    bytes — this comparison is not two voids
```

```
BINDING   PASS
GATE      PASS — publication gate 0 blocks at CONTENT_TIP, DELTA 0 against BASE_HEAD. The
          DIRECT_IDENTIFIER block that stood at the first revision-4 binding is CLEARED. §1
          keeps that history rather than erasing it
```

---

## 2 · What revisions 2 and 3 do, and what they deliberately do not

`roles/orchestrator.md` said its worktree was the repository root checkout. That was true on
2026-08-16 and stopped being true on 2026-08-17. Revision 1 corrected the label, typed the second
surface, stated that a working directory cannot establish who an actor is, and corrected the same
stale row in `BOOTSTRAP.md`.

**Revision 1 then claimed the bootstrap defect was repaired, and it was not.** Two passages of the
same file still executed the old arrangement, and a `FROZEN` annex that outranks everything the
candidate wrote still mandates it. Revision 2 closes the editable half and **declares** the half
that is not Plan's to close.

```
WITHDRAWN AT REVISION 2   the claim that the BOOTSTRAP defect is repaired
                          the claim that no FROZEN governance change is required
                          ORCHESTRATOR SURFACE = RESOLVED_BY_CANDIDATE_IF_CANONICAL
ADDED AT REVISION 2       a fail-closed stop in BOOTSTRAP.md at the promotion step
                          the FROZEN Annex I.2 residual, declared with owner and route
                          the residual's correct owner and its full extent
```

**Revision 3 changes no remedy.** The fail-closed stop, the created `orchestrator` worktree, the
withheld sixth chat line and the blocked table row are byte-for-byte what revision 2 shipped.
What revision 3 corrects is what this candidate **says** — and since the remedy for the half Plan
may not close *is* a declaration, the accuracy of that declaration is the whole of its value.

```
WITHDRAWN AT REVISION 3   "One more document was not updated on 2026-08-17" — there are two
                          "Two governed documents describe two different topologies" — three
                          the residual's extent as `Annex I.2 steps 1, 6, 9–10`
                          the convergence route as an Annex I.2 amendment
                          BOOTSTRAP ROOT-PROMOTION INSTRUCTION AFTER R2 = REMOVED, as stated:
                          removed from the file Plan may edit, intact in the one that outranks it
ADDED AT REVISION 3       the governance BODY named as the first and highest source, quoted
                          the residual's true extent, identical in all three content files
                          the convergence route's real scope AND its fingerprint cost
                          the grounding that authorizes the stop (body §48 hit directly, §4)
                          SLR-plan-0012
```

---

## 3 · Execution was never ambiguous — Annex D.1 is correct and untouched

```
WORK_COMMIT              ogni attore, proprio branch — obbligatorio, non canonico
CANONICAL_BATCH_COMMIT   solo Orchestrator, root, gate 0–5
```

`governance/annex_d_commit_batch.md` is `status: FROZEN`, `normative: yes`, and sits at rank 1 of
body §5 against a role contract's rank 4.

```
ORCHESTRATOR EXECUTION AMBIGUITY   NO
ANNEX D.1                          CORRECT — NOT MODIFIED at either revision
WORK_COMMIT SURFACE                the `orchestrator` worktree, branch `orchestrator`
CANONICAL_BATCH_COMMIT SURFACE     the root checkout, branch `main`, batch window only
```

### 3.1 · N-3 accepted — the independent confirmation is restated at its sound strength

Revision 1 argued that an actor resident in the root *"is a standing writer there, so GATE 0 would
fail from that actor's first durable output onward."* Mirror is right that this is lossy:
committed output leaves the root clean. **The sound version was already canonical at BASE**, in
`deployment/deployment_profile.md`, and revision 2 uses only that one:

> The root's branch is `main`, and a commit to `main` is canonical by definition — so an
> Orchestrator living in the root has **no branch on which a `WORK_COMMIT` is possible**. Its
> output cannot become durable; body §8 obliges it to produce durable output; so the root cannot
> reach clean by anything that actor is permitted to do alone.

That argument, in that form, is what `BOOTSTRAP.md` and the deployment profile now carry. The
compressed version appears nowhere in the content.

---

## 4 · The label was stale, and the file's own body already refuted it

`roles/orchestrator.md` has been touched **exactly once** in its history — `a8cd125`, 2026-08-16,
the original materialization. `e861dc4`, 2026-08-17, changed **one file**:
`deployment/deployment_profile.md`.

```
ORCHESTRATOR ROLE/FRONTMATTER LABEL     STALE — accurate when written, overtaken, never revisited
ORCHESTRATOR ROUTING-SURFACE AMBIGUITY  CONFIRMED
```

**The `worktree:` field was type-inconsistent.** Every other contract carries a bare worktree name;
only Orchestrator carried a prose phrase, and only Orchestrator has two surfaces to name. After the
change all four frontmatters parse as YAML and `worktree` is a bare string in three of them —
`roles/scientist.md` uses plural `worktrees`, which this candidate neither creates nor worsens.

---

## 5 · 🔴 B-1 accepted in full — and the reason it cannot be repaired the obvious way

**Reproduced before accepting, from git and not from the review.** At revision-1 content tip
`b3afdde`, `BOOTSTRAP.md` carried:

| Site | Text | Revision 1 |
|---|---|---|
| lines 31–35 | *"The same chat is promoted — you do not need to open a second one."* | **untouched** |
| step 3, lines 57–58 | creates `lettore`, `lettore-b`, `lettore-c`, `evidence-index`, `mirror` — five, omitting `orchestrator` | **untouched** |
| line 86, the table | `orchestrator` → `the repository root checkout` | **corrected** |

```
REV1 TABLE FIX                        PRESENT
REV1 ROOT-PROMOTION INSTRUCTION       PRESENT — live, in the section headed "The one thing to
                                      understand before anything else", read long before line 93
REV1 ORCHESTRATOR WORKTREE CREATION   ABSENT — the corrected table pointed at a worktree the
                                      procedure never created
```

**A chat's working directory is fixed at session start and cannot be relocated**, so *"the same
chat is promoted"* is operationally identical to *"the Orchestrator stays in the root."* The
reading that would save the sentence requires the act it forbids.

### 5.1 · FROZEN Annex I.2 mandates the same arrangement, and it outranks the fix

`governance/annex_i_bootstrap_deployment.md` is `status: FROZEN`, `normative: yes`, and § I.2
reads, verbatim:

```
1.  prima chat in <REPO_ROOT> → CLAUDE.md → nessun lease ACTIVE → BOOTSTRAP_MODE
4.  crea/verifica worktree: lettore, lettore-b, lettore-c, evidence-index, mirror
6.  presenta all'operatore la LISTA ESATTA delle 5 chat da aprire (path per ACTOR_ID)
9.  condizioni PASS → acquisizione ORCHESTRATOR_LEASE (I.3)
10. ORCHESTRATOR_REGISTRATION durevole → ACTIVE_ORCHESTRATOR → governance ordinaria
```

```
ANNEX I.2 ROOT-PROMOTION MODEL   CONFIRMED — step 1 seats the controller in the root; steps 9–10
                                 promote that same chat in place
ANNEX I.2 CONFLICT               CONFIRMED — against the canonical deployment profile, which
                                 reserves the root to CANONICAL_BATCH_COMMIT and gives the
                                 Orchestrator its own worktree
ANNEX I.2 PRECEDENCE OVER        YES, by two independent routes:
BOOTSTRAP.md                     (a) I.2 is FROZEN + normative, body §5 rank 1; BOOTSTRAP.md is
                                     status: PROPOSED
                                 (b) BOOTSTRAP.md line 5 declares, QUOTED WHOLE:
                                     `authority: Annex I.1, I.2, I.6; body §0.1–0.4, §38, §47`
                                     — it derives from I.2 and cannot outrank its source.
                                     Revisions 1 and 2 quoted this line only as far as the
                                     semicolon. Everything dropped is where the body's §0.2
                                     lives, and that truncation is the entire mechanism of the
                                     miss §5.5 records
ANNEX I.2 CHANGE AUTHORITY       operator. Annex H.1: "Spese / MAJOR approval / governance →
                                 Operatore". Body §4: "Cambio governance / authority model →
                                 attende → human required". Plan may propose; Plan may not adopt
SECOND ORCHESTRATOR CHAT         excluded — not by a prohibition sentence, but determinately, by
                                 step 6's *LISTA ESATTA* of **five** combined with step 1 and
                                 steps 9–10. Stated as a reading of the arithmetic, because that
                                 is what it is
```

**A sixth chat is what I.2 excludes; a sixth *directory* is not.** Step 4 enumerates worktrees to
create and does not prohibit others, and the `orchestrator` worktree is canonical at `main` through
`CAND-20260817-ORCHWT`. Nothing load-bearing rests on that reading: creating a directory confers no
authority, and the blocked act is the promotion.

### 5.2 · The remedy — fail closed, because both executable options are wrong

Revision 2 does **not** make `BOOTSTRAP.md` independently executable in the new topology. That
would be a `PROPOSED` document overriding a `FROZEN` one, which is the failure mode, not the fix.

| Option | Verdict |
|---|---|
| Leave the root-promotion topology executable | **rejected** — recreates the standing root writer. The task directive's §26 names this exact condition *(directive §26, not body §26, which is SEMI-BLIND — the bare citation at revision 2 was ambiguous and is disambiguated here)* |
| Publish the new topology in `BOOTSTRAP.md` | **rejected** — a lower-precedence document silently superseding rank-1 FROZEN law |
| **Surface the conflict, stop, name the owner** | **SELECTED** — body §48's `BLOCKED_BY_GOVERNANCE`, Annex J.3's queue object, `TYPE: GOVERNANCE` |

What that looks like in the file, and where a reader meets it — **line numbers at the revision-3
content tip `25fa61a`**:

```
line  36–41   the top section — which chat is promoted is open; body §0.2 quoted as the
              disputed mandate rather than restated as this file's own instruction
line  63–70   step 3 creates the orchestrator worktree, and says creating a directory
              promotes nobody
line  72–78   step 5 holds the operator's chat list at the five that I.2 step 6 AND body §47
              step 10 both require, and explicitly withholds the sixth line
line  90–93   step 9 carries a STOP *before* the lease-acquisition verb
line  99–159  the block itself: all THREE sources with their statuses, why the topology is
              defective, why that is still not this file's decision, why a stop needs no
              precedence and what grounds it anyway, the route and its cost
line 165      the `orchestrator` row is marked BLOCKED, do not open
line 172–180  the table's prose: the row records a work surface, not an instruction
```

```
BOOTSTRAP EDITABLE                              YES — status: PROPOSED
ROOT-PROMOTION INSTRUCTION IN BOOTSTRAP.md      REMOVED at revision 2; at revision 3 the
                                                proposition is no longer asserted in this
                                                file's own voice at all — it is attributed
                                                and quoted as the disputed FROZEN mandate
ROOT-PROMOTION MANDATE IN FROZEN GOVERNANCE     PRESENT — body §0.2, §0.4, §47 and Annex I.2.
                                                NOT removable by this candidate. DECLARED
BOOTSTRAP ORCHESTRATOR WORKTREE OMISSION        REMOVED — step 3 creates it
BOOTSTRAP FRESH-RUN STATUS                      FAIL_CLOSED_PENDING_FROZEN_TRANSITION
STOP GROUNDING STATED                           YES at revision 3 — body §48 hit directly, §4
FROZEN RESIDUAL                                 HUMAN_REQUIRED — declared, owned, routed, costed
ANNEX I.2 MODIFIED / SUPERSEDED                 NO / NO
GOVERNANCE BODY MODIFIED / SUPERSEDED           NO / NO
```

### 5.3 · Where the residual is declared, so it is not carried by this manifest alone

`deployment/deployment_profile.md` — a new subsection under the section that made the change,
carrying `RESIDUAL / INTRODUCED BY / OWNER / AUTHORITY REQUIRED / STATE / CONVERGENCE ROUTE /
COST OF THAT ROUTE / BLAST RADIUS`. `roles/orchestrator.md` — a paragraph stating that for this
already-bootstrapped laboratory the question is settled and for a fresh bootstrap it is not.
`BOOTSTRAP.md` — the block itself. **Three content files, not a control-plane note.**

**At revision 3 the three agree on the extent, which at revision 2 they did not.** Revision 2 said
`Annex I.2 steps 1, 6, 9–10` in three places and `steps 4, 6 and 9–10` in the convergence route —
a four-way citation of one residual that disagreed with itself on the step `BOOTSTRAP.md` step 3
already departs from. All sites now read: **body §0.2, §0.4, §47 steps 10 & 14, and Annex I.2
steps 1, 4, 6, 9–10.**

### 5.4 · Who introduced it, measured rather than assumed

`CAND-20260817-ORCHWT` corrected the deployment profile and left Annex I.2 mandating the
arrangement it replaced. The conflict therefore **pre-dates this candidate at BASE_HEAD**; ORCHSURF
exposes it and does not create it.

```
CAND-20260817-ORCHWT manifest      "I.2" → 0 hits   "Annex I" → 0 hits
REV-ORCHWT-MIRROR-001              "I.2" → 0 hits   "Annex I" → 0 hits
REV-ORCHWT-MIRROR-002              "I.2" → 0 hits   "Annex I" → 0 hits
ORCHSURF revision 1, all 4 content files            "Annex I.2" → 0, 0, 0, 0
```

Two hostile reviews and an operator approval passed over it. That is recorded as `SLR-plan-0011`
L-5 and is the finding this session considers most worth carrying forward.

### 5.5 · 🔴 REVISION 3 — the residual is in the body as well, and the body outranks the annex

**This was found by Plan re-reading its own delivered package, not by Mirror, and it defeats a
claim revision 2 made in four places.** `governance/GOVERNANCE_v3.1.1.md` is `status: FROZEN`,
`normative: yes`, has **no `authority:` field of its own**, and is the document every annex derives
from. It reads, verbatim:

```
§ 0.2  "La prima chat aperta in <REPO_ROOT> NON è Orchestrator per il fatto di trovarsi lì:
        BOOTSTRAP_CONTROLLER → qualificazione → ORCHESTRATOR_LEASE acquisito → ACTIVE_ORCHESTRATOR
        La stessa chat viene promossa; non servono due chat root."

§ 0.4  "il Controller ... presenta all'operatore la lista esatta delle chat da aprire ... e SOLO
        a condizioni superate acquisisce il lease e diventa ACTIVE_ORCHESTRATOR."

§ 47   10. operatore apre le cinque chat restanti
       14. promozione: BOOTSTRAP_CONTROLLER → ACTIVE_ORCHESTRATOR (lease ACTIVE)
```

**`BOOTSTRAP.md`'s deleted sentence was a translation of § 0.2.** Mirror quoted *"The same chat is
promoted — you do not need to open a second one"* as B-1's evidence. That is *"La stessa chat viene
promossa; non servono due chat root"* in English. Revision 2 removed the rendering and reported
`BOOTSTRAP ROOT-PROMOTION INSTRUCTION AFTER R2 — REMOVED`. It was removed from the file Plan may
edit and left standing at the highest rank in the system.

```
BODY §0.2 ROOT-PROMOTION MANDATE      CONFIRMED — read verbatim at the revision-2 content tip
BODY PRECEDENCE OVER ANNEX I.2        YES — the body has no `authority:` field; the annexes name
                                      it as theirs. It is where a mandate can originate
NAMED IN THE REVISION-2 PACKAGE       NO — grep for "0.2" / "0.4" / "§47" / "due chat" across the
                                      manifest, handoff, author response, SLR-plan-0011 and
                                      SLR-plan-0010-COR-001 → 0 hits in all five
NAMED IN REV-ORCHSURF-MIRROR-001      NO — same grep → 0. Its §18 falsifier 1 searched
                                      `governance/`, and §0.2 sits inside that perimeter
REMEDY CHANGED BY REVISION 3          NO — the stop is byte-for-byte revision 2's
DECLARATION CHANGED BY REVISION 3     YES — extent, route, cost and grounding
```

**Three consequences, and the third is the one that would have hurt an operator.**

1. **The conflict table named two sources.** There are three, and the unnamed one outranks both
   named ones. Corrected in `BOOTSTRAP.md`.
2. **The residual's extent disagreed with itself.** Three content files said `Annex I.2 steps 1,
   6, 9–10`; the convergence route said `steps 4, 6 and 9–10`. Step 4 is the step `BOOTSTRAP.md`
   step 3 already departs from and one of the two Mirror named in its §4.5 item 2. All four sites
   now read the same set, and it includes the body.
3. **The convergence route was under-scoped, and an operator could have executed it in good faith
   and discharged nothing.** Amending `Annex I.2` alone leaves body §0.2 mandating the arrangement.
   The route now names both documents and says so explicitly — and it now names the cost, because
   the body is a fingerprint input for **all four** roles while `Annex I.2` is an input for
   `orchestrator` and `plan` only. The operator is approving a four-role rotation and every
   actor's checkpoint invalidated under Annex A.6, not a two-role one. Enumerated with
   `governance_fingerprint.py inputs --all`, not assumed.

**One further correction, of a different kind.** Revision 2 rested the stop on *"this file may not
choose between them"*, and in the same section handed the reader the precedence argument against
it — I.2 is rank 1, `BOOTSTRAP.md` is `PROPOSED`, a document cannot outrank its source. A
controller applying body §5 literally was given a live reason to proceed. Revision 3 states the
grounding that was there all along and unused: a stop is the *absence* of an instruction and needs
no precedence, and independently, body §48 forbids proceeding past a point that could *"violare
one-writer"*, with body §4 making a directly-hit §48 condition the one route to `HUMAN_REQUIRED`
that does not require an Orchestrator to classify it — the position every bootstrap occupies by
construction.

```
ANNEX I.2 MODIFIED   NO          BODY MODIFIED   NO          CLAIMED SUPERSEDED   NEITHER
```

---

## 6 · Three concepts, and the one that gets no filesystem attribute

```
1. ACTOR WORK SURFACE       per-actor, named by `worktree:` in every contract
2. CANONICAL BATCH SURFACE  Orchestrator only, named by `canonical_batch_surface:`
3. ROUTING / DISCOVERY      NO filesystem attribute — the candidate declines to create one
```

The three ordinary contracts are untouched. Their `ACTOR_ID ↔ worktree` mapping was never
ambiguous, and flattening a real asymmetry to make the schema uniform would be a second error. It
also holds the blast radius to one fingerprint.

---

## 7 · The measurement — why cwd cannot carry concept 3

```
INSTRUMENT     claude agents --json --cwd <path>   (PATH binary)
VERSION        2.1.232 (Claude Code)
SESSION RT     2.1.232 — this session's owning process image. Same version here; recorded
               separately because instrument version and session runtime are different facts
TIMESTAMP      2026-08-19T21:55:28Z
MODE           read-only enumeration; no session elected, superseded or written
```

| Query cwd | Sessions | Composition |
|---|---|---|
| root | **8** | 5 root · 1 `lettore-c` · 1 `mirror` · 1 `evidence-index` |
| `orchestrator` worktree | **0** | — |
| `evidence-index` — POSITIVE CONTROL | **1** | the query can return non-zero |
| `mirror` — POSITIVE CONTROL | **1** | — |
| `lettore-c` — POSITIVE CONTROL | **1** | — |
| nonexistent path — NEGATIVE CONTROL | **0** | — |

**Counts are volatile and are evidence for nothing but structure.** Plan measured 17 at 21:02Z,
Mirror 8 at 21:23Z, this session 8 at 21:55Z. **Every structural claim reproduced exactly, a third
time:**

```
FIELD SET                  cwd · kind · name · pid · sessionId · startedAt — exhaustive union
EXPLICIT ACTOR/ROLE FIELD  NOT_OBSERVED_VIA(claude agents --json, CLI 2.1.232)
NAME == <cwd leaf>-<2 hex> 8/8
ROOT-CWD INTERPRETATION    OVER_BROAD_FOR_ACTOR_DISCRIMINATION — 3 of 8 hits are other actors
ZEROS                      AMBIGUOUS — the orchestrator worktree exists and returns 0; a
                           nonexistent path returns 0. The instrument cannot separate
                           unoccupied from absent
CWD AS ROUTING ATTRIBUTE   PROHIBITED as an actor-identity discriminator
```

The negative claim is stated **instrument-bound**, not as universal impossibility, and requirement 5
in the content excludes the tool from the ontology.

### 7.1 · Worktree containment, counted precisely rather than conveniently

```
TOTAL WORKTREES                    14
AT OR UNDER THE ROOT               7   = the root checkout itself + 6 named actor worktrees
OUTSIDE THE ROOT ENTIRELY          7   = 4 legend-codex-* checkouts + 3 scratchpad worktrees
NAMED ACTOR WORKTREES UNDER ROOT   6/6
UNIVERSAL "every worktree is under root"   FALSE
```

The two figures differ by whether the root counts as under itself; both are stated so neither can
be read as the other. The content asserts only *7 outside* and *6/6 named actors under*, which are
the two that are true under either convention.

### 7.2 · P5DOMAIN §8.3 — carried, not edited

Canonical P5DOMAIN §8.3 supports a **true conclusion** with a **false universal premise**
(*"every worktree lives under the root"*). This candidate does not repeat the premise, states the
narrow 6/6 fact instead, and **does not edit P5DOMAIN**.

```
P5DOMAIN §8.3   CARRIED_SEPARATE_TRUTHFULNESS_DEBT — owner: whichever candidate next opens P5.
                Not load-bearing to ORCHSURF, and requiring ORCHSURF to fix it would be scope creep
```

---

## 8 · Remediation classes considered, at revision 2

| | Class | Verdict |
|---|---|---|
| A | role-label correction alone | **insufficient** — one site, `worktree` still untyped, root-cwd reading still available |
| B | typed-surface semantics alone | **insufficient** — leaves BOOTSTRAP executing the old arrangement |
| C | cwd-nonauthoritative rule alone | **insufficient** — states the prohibition while the contract asserts the thing it prohibits |
| D | A + B + C, each minimal | **insufficient — this was revision 1.** It corrects the sites it names and leaves the procedure beneath them |
| **E** | **D + full BOOTSTRAP remediation + declared FROZEN residual** | **SELECTED** |
| F | E + amend Annex I.2 | **not available to Plan** — H.1 gives governance change to the operator; §25 of the directive forbids it here |
| G | rename `worktree:` in all four contracts | **rejected** — rotates four fingerprints to fix an ambiguity that exists in one |

```
SELECTED REMEDIATION CLASS   E
PROBLEM SOLVED               the stale label at both sites; the untyped word; the availability of
                             cwd as an identity discriminator; and — new at revision 2 — the
                             executable instruction that recreated the root Orchestrator
PROBLEM DECLARED, NOT SOLVED FROZEN Annex I.2 still mandates the legacy topology. HUMAN_REQUIRED
GUARANTEE PROVIDED           scoped deliberately: (a) a future resolver cannot read a
                             canonical-execution surface as an actor home, and cannot read any
                             filesystem location as identity; (b) a fresh bootstrap following this
                             file cannot silently seat a standing root Orchestrator. **NOT**
                             guaranteed: that a fresh bootstrap can complete
WHAT REMAINS UNSOLVED        the Annex I.2 transition; and which session is CURRENT for an
                             ACTOR_ID, untouched, with three holds still blocking it
BLAST RADIUS                 5 content files, 1 fingerprint
BACKWARD COMPATIBILITY       no rule changes; no published hash moves; no executing behaviour
                             depends on any corrected line
```

---

## 9 · Hostile tests — T1–T6 re-run, T7–T9 added

| | Test | Expected | Result | Reason verified |
|---|---|---|---|---|
| T1 | can a non-Orchestrator session satisfy the stale root-cwd reading? | YES (proving it unsafe) | **PASS** | 3 of 8 root-query hits are demonstrably other actors; the 5 at root differ only by `pid`/`sessionId`/`startedAt`/name-suffix — mutually indistinguishable on any governed attribute |
| T2 | does occupying the `orchestrator` worktree confer authority? | NO | **PASS** | `lease_state.py --check`: **ACTIVE by derivation 0** over 5 leases (2 STALE, 3 RELEASED). Authority needs assigned role + ACTIVE lease |
| T3 | can an authorized Orchestrator batch in root without changing its work surface? | YES | **PASS** | measured live: root `main`@`04693e6`, **0 porcelain lines**; `orchestrator` worktree on branch `orchestrator`@`b3596d5`. Coexisting |
| T4 | do ordinary-actor semantics stay coherent? | YES | **PASS** | `git diff --name-only 04693e68 -- roles/` returns **only** `roles/orchestrator.md`; all four frontmatters parse as YAML; plan/mirror/scientist fingerprints byte-identical |
| T5 | does the candidate elect a CURRENT session? | NO | **PASS** | 0 UUID-shaped strings in 235 added lines — with a positive control confirming the regex finds real UUIDs in `ledger/`; `actors.yaml` ABSENT at base and tip; every routing-vocabulary hit read individually — all denials, requirements or descriptions |
| T6 | does it require `claude agents --json` as the identity definition? | NO | **PASS** | two occurrences: a dated measurement, and requirement 5, which excludes it — *"must survive its replacement"* |
| **T7** | **following all CURRENT executable BOOTSTRAP instructions after revision 3, and respecting the declared residual, can the procedure silently create or promote a standing root Orchestrator?** | **NO** | **PASS** | **not tested by phrase absence.** The procedure was walked step by step at the revision-3 tip: the only sites that can seat an Orchestrator are step 9 (lease acquisition, line 93) and step 10 (durable registration, line 94). The STOP is at line 90, **before** the acquisition verb; two further pointers (lines 41, 76) precede it; the block itself states `UNTIL RESOLVED do not promote any chat to ACTIVE_ORCHESTRATOR, in the root or anywhere` (line 154). **The reason is NOT "BOOTSTRAP overrides the body or I.2"** — it is that execution halts and defers, which needs no precedence. Negative control: the same walk on the revision-1 tree reaches step 9 with no stop and line 34 instructing promotion in place |
| **T8** | can an operator reach the Orchestrator bootstrap without being told that FROZEN governance still mandates the legacy topology? | **NO** | **PASS** | the first reference to the block (line 41) precedes the first lease-acquisition verb (line 93) in file order, and step 1 directs a linear read of this file first. References across the three content files: **19 to the body's bootstrap sections, 18 to Annex I.2**. **Positive control**: the same probe on the revision-1 tree returns **0, 0, 0, 0** for I.2 — reproducing Mirror's zero independently — and, re-run at revision 3 for the body, returns **0 across the entire revision-2 package**, which is the finding of §5.5 |
| **T10** | **is the residual confined to Annex I.2, as revisions 1 and 2 asserted?** | **NO — and this is the revision-3 finding** | **PASS (the assertion FAILS)** | exhaustive, not sampled: all **11** FROZEN `normative: yes` governance documents were enumerated from their own frontmatter and grepped for the mandate's vocabulary (`stessa chat`, `ACTIVE_ORCHESTRATOR`, `acquisizione ORCHESTRATOR_LEASE`, `cinque chat`, `LISTA ESATTA`). **Exactly two carry it: the body, 5 hits, and Annex I.2, 3 hits.** The other **nine annexes return 0**, which is the negative control the sweep supplies for itself. The body has **no `authority:` field**; every annex names it as theirs — that is the stopping rule, and it is why the search terminates there |
| **T9** | can the stale `agent_card` / `runtime_inventory` declarations independently confer or redefine Orchestrator work-surface authority? | **NO** | **PASS** | three legs: (a) each file self-declares `authority: none`; (b) body §43 — *"riga stantia = non autoritativa"*; (c) **no executable consumes them** — `git grep` over every `*.py`/`*.sh` on both `HEAD` and branch `orchestrator` returns zero, with a **positive control** (the same search finds the three real consumers of `plan_defined_parameters`) and a **negative control** (a nonexistent token returns empty). `launch/legend_launch.sh` references none of them |

```
WRONG-REASON LOAD-BEARING PASSES   0
```

**One trap that landed, and was caught only at revision 3.** T7 and T8 both passed at revision 2,
for their stated reasons, and both were **scoped to the wrong universe**: they asked whether
`BOOTSTRAP.md`'s procedure could seat a root Orchestrator and whether a reader would be told about
*Annex I.2*. Both answers were correct and neither test could have found the body, because neither
test looked outside the set of documents the candidate had already named. **A test that inherits
the candidate's own list of sources cannot falsify that list.** T10 exists to be the test that
does, and it is the only test here whose universe is enumerated from the tree rather than from
this manifest.

**Four traps avoided at this revision, recorded because they nearly landed.** (i) T7 as a grep for
the deleted sentence — it would have passed on a file that still walked an operator into the root
by a different route, so the test walks the procedure instead. (ii) T9's consumer search run only
on `HEAD`, which does not contain the runtime files — repeated on branch `orchestrator`, where they
live. (iii) the regression comparison run between a working worktree and a fresh checkout, where a
**git-ignored** local corpus (`files/`, `.gitignore:7`) turned four `skipped` into `ok` and looked
like a delta — re-run in matched fresh checkouts, §15. (iv) a worktree-containment count of 6/14
that is 7/14 under the other convention — both stated, §7.1.

---

## 10 · Authority — corrected from revision 1

Revision 1 stated `FROZEN GOVERNANCE CHANGE REQUIRED: NO`. **That was false**, and it is the
sentence that let the completion claim stand.

```
FROZEN GOVERNANCE CHANGE REQUIRED FOR COMPLETION   YES — body §0.2, §0.4, §47 steps 10 & 14
                                                   AND Annex I.2 steps 4, 6, 9–10. Revision 2
                                                   named only the second half of that
FROZEN GOVERNANCE CHANGE MADE HERE                 NO — and none is proposed in this candidate
GOVERNANCE BODY MODIFIED                           NO   (FROZEN — and it is half the residual)
ANNEX D.1 MODIFIED                                 NO   (FROZEN, verified correct, blob identical)
ANNEX H.1 MODIFIED                                 NO   (FROZEN)
ANNEX I.2 MODIFIED                                 NO   (FROZEN — and it is the other half)
```

Every artifact this candidate edits is `status: PROPOSED` or is Plan's to maintain under its own
mandate. The route is unchanged and verified against H.1:

```
plan proposes  →  mirror reviews  →  operator approves (governance, MAJOR)  →  orchestrator
canonicalizes under an ACTIVE lease and gates 0–5
```

Plan does not execute this. GATE 1 keeps proposer and executor distinct.

---

## 11 · Routing holds — accounting only, nothing lifted

```
C-9 §7.2                              OPEN — HUMAN_REQUIRED. Untouched
BUILD_MINIMAL_DIRECTORY               OPEN — framework/state/actors.yaml ABSENT at main and at
                                      the candidate tip. Verified this session
MULTI_AGENT_ARCHITECTURE_FEASIBILITY  OPEN — PRESERVED, NOT AUTHORIZED, NOT STARTED
E5                                    PARTIALLY_RESOLVED — unchanged by this candidate
ORCHESTRATOR SURFACE                  PARTIALLY_RESOLVED — HUMAN_REQUIRED.
                                      Semantics corrected and stale instructions removed;
                                      adoption of the bootstrap topology BLOCKED_BY_FROZEN
                                      Annex I.2, whose amendment is the operator's
ROUTING READY FOR CANDIDATE B         NO — three holds remain, none of which Plan may discharge
```

`PARTIALLY_RESOLVED` and `HUMAN_REQUIRED` are the vocabulary already in use in this table (E5, C-9
§7.2). No new lifecycle state is invented. **Candidate B is not opened here.**

---

## 12 · Residual — N-1 accepted, owner corrected, extent enumerated

**Owner, verified from three sources that agree, none of them the review:**

```
runtime/agent_card_registry.md   frontmatter   maintained_by: plan (body §43)
body §43, canonical at main                     "Plan aggiorna a ogni rehydration/cambio;
                                                 riga stantia = non autoritativa"
runtime_inventory.md, finding C-5               "Owner: Plan, as part of the first
                                                 post-bootstrap candidate"

AGENT CARD OWNER   plan   ← revision 1 said "Orchestrator owns it". WITHDRAWN
```

Revision 1's *reason* for not editing it — it sits on a branch Plan may not write — is sound and
unchanged. Location decides the **route**; ownership metadata decides the **owner**.

**Extent — two tracked files and seven occurrences, plus a third artifact nobody had named:**

| Path (branch `orchestrator`) | Loc | Text | Class | Consumer | Code-read? | Load-bearing? |
|---|---|---|---|---|---|---|
| `runtime/agent_card_registry.md` | 118 | `WORKTREE: the root checkout # branch main` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 38 | table row, Worktree = `root checkout` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 72 | `Working dir: the root checkout` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 73 | `Worktree: root` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 79 | `Write access: root checkout; bootstrap artifacts only` | DERIVED_RUNTIME | none | **no** | no — it describes the I.2 pre-promotion perimeter, which is still FROZEN law |
| `runtime/bootstrap/STEP5-session-open-plan.md` | 32 | *"The Orchestrator chat is already open in the root checkout and is not reopened."* | OBSERVATIONAL — `status: PLAN`, `authority: none` | none | **no** | no — a record of a step executed on 2026-08-17, not a template |
| `runtime/bootstrap/STEP5-session-open-plan.md` | 38 | table row, `orchestrator` \| root checkout \| `main` | OBSERVATIONAL | none | **no** | no |

**Not stale, and recorded so the list is not mistaken for one:**
`deployment/deployment_profile.md` on branches `mirror` and `lettore-c` carries the pre-`e861dc4`
row. Verified: `e861dc4` is **not** an ancestor of either branch, so these are branch-lag copies of
a canonical file, not independent declarations. They refresh when those branches rebase.

```
AGENT CARD AUTHORITY        DERIVED_RUNTIME — not canonical (`runtime/` at main holds only
                            orchestrator_lease.md). WORKTREE is a derived copy of a canonical
                            value that was ALREADY CORRECT at BASE_HEAD (fixed by e861dc4)
CONSUMER RISK               NON_BLOCKING — verified in T9 with positive and negative controls
REMEDIATION OWNER           plan (body §43 + frontmatter + C-5), executing on the Orchestrator
                            surface — routed through Orchestrator, never reached across by Plan
RUNTIME STALE DECLARATIONS  SAFE_CARRIED
```

**No other surface was modified to make this review green.** Plan does not write another actor's
branch, and the correct extent is reported rather than repaired.

---

## 13 · Disposition of every finding in `REV-ORCHSURF-MIRROR-001`

| | Finding | Disposition |
|---|---|---|
| **B-1** | BOOTSTRAP can still recreate a standing root Orchestrator; Annex I.2 never mentioned | **ACCEPTED, REMEDIATED + DECLARED — and the declaration was WRONG IN EXTENT at revision 2, corrected at revision 3.** §5 and §5.5. Editable half closed at revision 2 and unchanged since. The FROZEN half is declared with owner, route and cost — and it is **body §0.2, §0.4, §47 as well as Annex I.2**, which revision 2 did not know. Reproduced independently before accepting; the extension found by Plan, not by Mirror |
| **N-1** | agent-card residual: wrong owner, incomplete extent | **ACCEPTED, CORRECTED** — §12, and `SLR-plan-0010-COR-001`. One further artifact found beyond Mirror's list |
| **N-2** | SLR uses CONFIRMATION_CLASS values outside E.2; six E.6 elements absent | **ACCEPTED, APPLIED FORWARD** — `SLR-plan-0011` uses E.2's vocabulary and carries all E.6 elements. `SLR-plan-0010` left **byte-identical**: a learning record records what a session understood, and Mirror's E.2 curation of it is already durable in the review |
| **N-3** | manifest §3's GATE 0 argument is a lossy compression | **ACCEPTED, RESTATED** — §3.1. Only the canonical no-branch-for-WORK_COMMIT form appears in the content |
| **N-4** | the evidence bundle omits that the regression suite is red at main | **ACCEPTED, DISCLOSED** — §1 and §15 both state it, with the cause traced independently |
| §6 | P5DOMAIN §8.3 false premise | **CARRIED** as a separate truthfulness debt — §7.2. Not edited |
| §12 | `SLR-plan-0010` BOUND, L-4 reclassified to REPLICATION, L-5 upgraded | **ACCEPTED** — Mirror's curation stands; `SLR-plan-0011` proposes its own classes and does not revisit Mirror's |
| §2 | five steelman points | noted; §2.5's mechanical argument for the schema decision is adopted in §4 |

**Author response (C.2 §20):** `reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-001.md`.

**One finding of `REV-ORCHSURF-MIRROR-001` is now known to have been under-scoped by its own
author and by its reviewer.** B-1's §4.5 remedy asked for the residual *"against FROZEN Annex I.2
steps 4 and 6"*. The residual is also against the body, and §18's falsifier 1 searched
`governance/` — the perimeter that contains it — for a document pointing the other way rather than
for further copies of the same mandate. That is not a defect in the review: it found the blocking
claim and the claim was real. It is recorded because revision 3 exists only because the same
search was run once more, upward instead of sideways.

---

## 14 · Fingerprint impact — recomputed from scratch at four trees

```
                BASE_HEAD 04693e68     REV 1 b3afdde     REV 2 7b6a9d9     REV 3 25fa61a
orchestrator    88dea7a6…5ebb      →   42b8575c…908a  →  9d8d823c…1871  →  f2931147…f2e9
plan            0d6987bd…1429          0d6987bd…1429     0d6987bd…1429     0d6987bd…1429
mirror          e01b4108…0412          e01b4108…0412     e01b4108…0412     e01b4108…0412
scientist       b66959cd…9d1a          b66959cd…9d1a     b66959cd…9d1a     b66959cd…9d1a
```

Full values:

```
orchestrator BASE  88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb
orchestrator REV3  f293114766741ffac52d2d0c903522e4b28b54940cc950dae62a3c97b166f2e9
plan               0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429
mirror             e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412
scientist          b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a
```

**Recomputed, not carried forward.** All four were composed in fresh detached checkouts at
BASE_HEAD and at the revision-3 content tip, and revision 1's published `42b8575c…` was reproduced
at `b3afdde` as a positive control on the instrument — the same control, re-run at revision 3.

**The input set was enumerated, not assumed** — `governance_fingerprint.py inputs --all`:

```
governance/GOVERNANCE_v3.1.1.md      input for ALL FOUR roles
governance/annex_i_bootstrap…md      input for orchestrator and plan ONLY
roles/orchestrator.md                input for orchestrator ONLY — the one input this
                                     candidate moves, at every revision
```

That enumeration is what makes §5.5's cost statement checkable rather than plausible: **the
convergence route this candidate declares would rotate all four fingerprints**, because it must
reach the body. This candidate rotates one. The two facts are different and are kept apart.

```
CHANGED INPUT           exactly one of orchestrator's sixteen: roles/orchestrator.md
NOT FINGERPRINT INPUTS  BOOTSTRAP.md · deployment/deployment_profile.md · learning/ —
                        confirmed by enumerating the input set, so the larger edits of
                        revisions 2 and 3 rotate nothing
P2.2 COMPOSITION        untouched — the candidate changes no fingerprint composition
A.6 CONSEQUENCE         only orchestrator checkpoints are invalidated for resume. Plan, Mirror
                        and Scientist checkpoints remain compatible
```

---

## 15 · Gates, LINT, regression

```
LINT @ candidate   PASS — 1 INFO (MISSING_WIKILINK, CLAIM 010)
LINT @ BASE_HEAD   PASS — the SAME 1 INFO → pre-existing, verified rather than asserted
PUBLICATION GATE   PASS · BLOCKS 0 · 4 REVIEW items, pre-existing
```

**Regression — compared as sets, in matched environments.** `run_release_regressions.py` reports
`REGRESSION VERDICT: FAIL` at the candidate **and reports the identical failing set at BASE_HEAD**:

```
SUITE SET              IDENTICAL — 65 suites, name set diffed and equal
FAILING SET            IDENTICAL — 6 suites, by name:
                         scripts/test_release_runner_verdict.py
                         scripts/test_locator_obligation_reaches_every_route.py
                         scripts/test_abstract_corpus_is_not_evidence.py
                         scripts/test_release_surface.py
                         scripts/test_fulltext_trace_contract.py
                         framework/scripts/test_session_self_eval.py
TEST-NAME/OUTCOME SET  IDENTICAL — 834 test-outcome lines each side, zero differences
                       (counted with the pattern `... ok|FAIL|ERROR|skipped`; revision 2's
                       "476" was the same set under a narrower pattern, and the tree did
                       not move — the count is instrument-relative and is stated as such)
REGRESSION DELTA       0
```

**Two BOOTSTRAP-named failures were checked individually, because this candidate edits
`BOOTSTRAP.md` and a shared name is not a shared subject.** `test_the_bootstrap_states_the_rule`
and `test_the_bootstrap_bounds_the_corpus` both assert against **`CLAUDE.md`**, not `BOOTSTRAP.md`
— `file='CLAUDE.md'` in the failure header — and their assertion text is byte-identical at both
trees. Neither is touched by this candidate.

**Residual differences after normalization: 6 lines, all accounted for** — four are
`LEDGER_TAIL_ANCHOR` hashes, which move between runs because the suite appends a timestamped
growth-anchor record, and two are the exit markers this session appended to its own capture files.
The comparison is therefore reported as *identical outcome sets*, not as byte-identical output,
because the latter would be false.

**Both sides were run in fresh detached checkouts**, at `04693e68` and at `25fa61a`. A first
comparison against the working worktree showed four `skipped → ok` differences; the cause was
traced rather than assumed — `files/` is git-ignored (`.gitignore:7`), the working worktree holds
13 full-text entries and a fresh checkout holds 0 — and the comparison was redone in matched
environments, where the difference disappears.

**Cause of the red suite, traced independently (N-4).** Four shebang entrypoints carry mode
`100644` in the git tree at BASE **and** at the tip — `lease_state.py`,
`candidate_content_hash.py`, `governance_fingerprint.py`, `test_candidate_content_hash.py` — and
`test_release_surface.py::test_shebang_python_entrypoints_are_executable` requires
`st_mode & 0o111`. **A pre-existing red suite at canonical main, unchanged by this candidate, and
deliberately not repaired here.**

---

## 16 · What this candidate does NOT claim

Stated as a list because revision 1's defect was a claim that outran its evidence.

- **It does not claim the Orchestrator surface is resolved.** `PARTIALLY_RESOLVED — HUMAN_REQUIRED`.
- **It does not claim Annex I.2 or the governance body is amended, superseded, or interpreted
  away.** Both are FROZEN, both still mandate the legacy topology, and this candidate says so in
  three content files.
- **It does not claim the residual's extent is now complete.** Revision 2 asserted an extent and
  was wrong by one document, and that document outranked the one it named. Revision 3 states the
  extent it measured — body §0.2, §0.4, §47 steps 10 & 14 and Annex I.2 steps 1, 4, 6, 9–10 — and
  the search that produced it terminated at a document with no `authority:` field. That is a
  stopping rule, not a proof of completeness, and Mirror should treat it as the former.
- **It does not claim revision 3 improves the remedy.** The remedy is byte-for-byte revision 2's.
  Revision 3 buys accuracy in a declaration, and nothing else.
- **It does not claim a fresh bootstrap can complete.** It claims a fresh bootstrap cannot silently
  do the wrong thing, which is a smaller and checkable claim.
- **It does not claim the runtime residual is repaired.** `SAFE_CARRIED`, with an owner.
- **It does not claim the regression suite is green.** It is red at main and red here, identically.
- **It does not claim Routing is advanced.** Three holds stand, none of them Plan's to lift.
- **It grants no approval and implies none.** `HUMAN_APPROVAL: NONE`. `main` UNCHANGED at
  `04693e68`.

---

## 17 · Revision 4 — the direction inverted, and what survives the inversion

**§16 above, and §§2–15, were written under revision 3's direction and are retained verbatim as
the record of what this package argued before the operator's intent was ratified.** Where they
conflict with this section, this section governs.

**Retention is an operator directive of 2026-08-20, not a Plan convenience.** Plan offered to
rewrite them for internal consistency and the operator declined, on the ground that rewriting
would replace an observed reasoning evolution with a cleaned narrative and reduce auditability,
and that Mirror should review the candidate with the full history available. It is the same
principle `SLR-plan-0012` L-1 records from the other side — a claim removed from a derived
document is not thereby removed.

**Consequence for a reviewer, stated so the layering cannot hide behind itself:** §§2–15 are in
scope as EVIDENCE, not as current assertions. If §17.1 below fails to withdraw something those
sections assert, that gap is a finding — and it is precisely the class of finding this
arrangement could conceal.

### 17.1 · Every revision-3 finding, disposed by whether it depended on the direction

| Finding | Disposition at revision 4 |
|---|---|
| **T10 enumeration method** — a document universe enumerated from the tree, not from a manifest | **PRESERVED**, and re-run this session. Direction-independent by construction |
| **T7/T8 inherited-universe correction** — a test that inherits the candidate's source list cannot falsify it | **PRESERVED and applied**: every section reference in this revision was re-read at source, and no list was inherited from revisions 1–3, from the DEC, or from any prompt |
| **`SLR-plan-0012` P-2, concerning `SLR-plan-0011`'s truncation** — a procedure that says *read what `authority:` names* is defeated by a quotation ending at a semicolon | **PRESERVED.** Note the attribution: the defect is in 0011, the finding is in 0012. Citing it as "the SLR-plan-0011 finding" sends a reader to the defective quote instead of its diagnosis |
| **The authority-line lesson** — a field a check reads belongs in evidence verbatim and whole | **PRESERVED** |
| **Mirror's B-1, as a finding of contradiction** | **PRESERVED as a finding.** Governed documents did describe two irreconcilable arrangements. What changes is which document was defective: not the body and not Annex I.2, but `deployment/deployment_profile.md`'s WORK_COMMIT sentence and this package's reading of it |
| **N-1 · agent-card owner is `plan`** · **N-2 · E.2/E.6 form** · **N-4 · suite red at main** | **PRESERVED**, all direction-independent |
| **N-3 · the GATE 0 compression is lossy** | **PRESERVED and exceeded** — the uncompressed sentence is false too |
| **`P5DOMAIN` §8.3 carried debt** | **PRESERVED**, still owed, still not ORCHSURF's |
| **cwd-is-not-identity, in all three content files** | **PRESERVED and endorsed** — it is the ratified record's own item 3 |
| the FROZEN residual is `HUMAN_REQUIRED`, discharged by amending body + Annex I.2 | **WITHDRAWN — the residual DISSOLVES.** No FROZEN text required amendment |
| the convergence route rotates all four fingerprints | **WITHDRAWN.** Only `orchestrator` moves |
| `BOOTSTRAP.md` must fail closed at step 9 | **WITHDRAWN.** The stop's §48 grounding did not hold, and the conflict it stopped for was not a conflict |
| the `orchestrator` chat row is BLOCKED | **WITHDRAWN.** There is no sixth chat, and there never was |
| `STEP5-session-open-plan.md` is stale | **RE-ADJUDICATED CORRECT** |
| the profile's WORK_COMMIT argument is the sound version | **WITHDRAWN AS FALSE.** It is the sentence this revision retracts |

### 17.2 · Three ranks, kept apart on purpose

```
RANK 1   FROZEN governance — body §0.2, §0.4, §5, §8, §11, §14, §18, §35.1, §47; Annex D.1,
         Annex I.2. UNAMENDED, unchallenged, and the source of the architecture this candidate
         implements. Verified mechanically: git diff over body and annexes A–J returns EMPTY
RANK 2   DEC-20260820-ORCH-SESSION-HOME, ratified. It RECOGNIZES the rank-1 architecture and
         does not grant it. Where it and rank 1 were ever to conflict, rank 1 prevails and the
         record is revised — the record says so itself
—        THIS CANDIDATE. An implementation. It carries no rank of its own, edits no FROZEN
         document, and cannot make either of the two above mean anything they do not say
```

The F-8 adjudication is a rank-2 **reading** of rank-1 text, quoted verbatim in both content
files rather than paraphrased, so that a later reader can see it is quoted:

> §35.1 constrains where persistent artifacts may be produced, not whether the Orchestrator may
> produce persistent artifacts. The Orchestrator WORK_COMMIT surface is the assigned
> worktree/branch, never the root checkout.

### 17.3 · What revision 4 does NOT claim

- **It does not claim Mirror has reviewed this.** No review exists for revisions 2, 3 or 4, and
  revision 1's review was conducted under the opposite direction, so it does not transfer.
- **It does not claim the publication gate passes.** It does not — see §1. The block is the
  operator's signature in a public-edition repository, it is disclosed rather than absorbed, and
  Plan does not resolve it.
- **It does not claim `PROBE-ORCHWT-001` is discharged.** Legs 1, 2 and 4 are, from durable
  state. **Leg 3 — root non-perturbation — is owed by the Orchestrator** and cannot be taken by
  Plan without writing into another actor's worktree, which would corrupt what it measures.
- **It does not claim the regression suite was re-measured.** It was not, and revision 4 does not
  restate a number it did not take.
- **It does not claim `roles/plan.md`'s cross-worktree write refusal is verified.** It is not.
  What was measured is narrower: Plan can *provision* a worktree it never writes into.
- **It does not open ROOTGUARD, Routing, or P5.** The ratified record's §1 item 5 excludes the
  first; three routing holds stand, none of them Plan's to lift.
- **It grants no approval and implies none.** `HUMAN_APPROVAL: NONE`. `main` UNCHANGED at
  `04693e68`, and Plan does not execute in any case — GATE 1 keeps proposer and executor distinct.
