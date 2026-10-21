# Session self-evaluation — `REPURP-P3-KNOWNROADS-A-20261020`

**ACTOR_ID `scientist-a`** · task branch `task/REPURP-P3-KNOWNROADS-A-20261020`, worktree
`.claude/worktrees/lettore` · opened 2026-10-20, closed 2026-10-21 after a runtime interruption.
Written **before** the capability scout and **before** the report, per the standing brief § 5.

---

## 1 · The executable gate

| Check | Result |
|---|---|
| `session_self_eval.py` | **PASS** — *every complete read has landed and every declared output resolves*. 680 receipts, unread_premises 0/0. Two non-blocking historical ratchets (`retraction_check.dependencies` absent on 59 manifests, `acquisition_recipe` on 96) and seven declared gaps, **none of them mine** |
| `deepdive_manifest.py --verify-artifacts --require-current-schema` | **MANIFEST STRICT PASS, 0 gaps** on both new manifests (`PMID22938201.json`, 11 locators; `PMID40544182.json`, 9 locators), with exact text locators verified against the fingerprinted artefacts |
| `paper_packet.py check` | `ok` — *every applicable check screened something and none refused* |
| `staged_receipt_check.py --check-doi` | **OK** on both staged receipts |
| `fulltext_receipts.py record --dry-run` | **DRY RUN OK** on both; nothing written. The ledger was **not** appended to — the Orchestrator records staged receipts in event-ID order |
| `fulltext_receipts.py verify` (shared checkout) | **OK**, 680 chained receipts, tail anchored |
| `legend_lint.py .` | **WARN**, **zero** `BLOCK_BATCH_COMMIT` and zero `BLOCK_SYSTEM`. All warnings pre-exist this branch |
| `dependency_integrity.py screen` | `SCREENED_CLEAN` on both papers (45/50 and 43/43 references; snapshot 2026-09-10) |

---

## 2 · The written judgement

### What went right, and is reusable

**The repository answered the task.** Twenty-four roads were censused and twenty-two of them needed
no new reading: the claim registry, the therapeutic tracker, the hypotheses ledger, the dismissal
ledger and the discovery ledger between them carried model, genotype, endpoint, control, result and
limit for every one. The single most valuable artefact was a **persisted manifest**, not a paper:
`deepdive_manifests/PMID32000863.json` holds first-hand, image-read panel locators for the lithium
and ethosuximide arms, including the sentence that decides the lithium road — *«The wild-type panel
is marked as significantly as the null one»* — which the caption and the Results text of the primary
never say. A previous reading paid for that, and reading the paper again would have bought nothing.
**That is what the compounding memory is for, and this is the first session I can point to where it
replaced ten readings rather than supplementing two.**

**The budget was spent where the record was empty.** One road had zero records anywhere:
amlexanox. Both readings went there, in publication order, and the second one — the independent,
comparator-controlled test — turned the operator's standing caution (*protein quantity does not prove
function*) from a principle into a measured instance. That is the strongest single result of the
task, and it is a **negative**.

### What went wrong, named without softening

🔴 **I built both manifests against a remembered schema and the validator rejected them twenty-four
ways at once.** Surface vocabulary, `panel_text_relation` vocabulary, five `group_assessment` fields,
`field_density.queries` shape, `user_agent_policy` enum, `retraction_check.dependencies` as an object,
declined-skill reasons, and **two stitched quotes joined by an ellipsis** — each verbatim on its own
and not verbatim as a whole. I copied the shape of an existing manifest instead of running the
validator on a stub first. **One instance of that list is worse than the rest**: the stitched quote is
not a schema defect, it is a *fidelity* defect, and the validator's own words name why — an external
checker matching exact substrings would reject it, which means the locator would have looked verified
and not been. The machine caught all of it. **I caught none of it.**

🔴 **Two of the three honest-coverage decisions were made under context pressure, not by principle.**
Figures as `captions_only` and supplements `not_read` are correctly declared in both receipts and both
manifests, and no assertion anywhere rests on a panel. But the reason they were not opened is that I
was managing remaining context, and the right way to record that is as a **declared debt with an
order** — which § 8 of the note now does — rather than as a methodological choice. The protocol's
*understate rather than overstate* rule held; the practice behind it was weaker than the declaration.

🔴 **I ran the dependency screen from the wrong tree and read its refusal as a tool defect.** The
screen said the snapshot was absent; it was present, in the shared checkout, and I was in the
worktree. That is the **evidence-locality rule of my own standing brief**, which I had read an hour
earlier, and for about a minute I was on the way to patching a framework script a Harness agent owns
because of it. The adjacent real defect — `dependency_integrity.py fetch` crashing on a
Windows-1252 byte in a freshly downloaded CSV — is genuine and is reported, not patched (§ 4).

### The one that would have reached the record

🔴 **In the first draft of the note I wrote that lithium and ethosuximide were two tested roads.**
They are **two arms of one experiment** — same animals, same assay, same figure — and counting them
twice is precisely the double-counting the contract's *deduplicate by experimental origin* clause
exists to stop. I caught it while writing § 3, from the manifest's own entry numbers sitting side by
side. It is the only `severity_high` incident of this session that I caught myself, and it is the
reason § 3 of the note exists as a section rather than a sentence.

---

## 3 · ATTRIBUTION_CENSUS

```
ATTRIBUTION_CENSUS
incidents: 5
machine: 3   blind_auditor: 0   peer: 1   self: 1
severity_high: 2   of which self: 1
undetected_known: 0
```

**The counting, so it is reproducible.**

1. **Manifest schema rejection** — `machine` (`deepdive_manifest.py`). One incident, 24 instances
   across two files. `severity_high`: **yes**, because one instance (the stitched quotes) was a
   fidelity defect that would have put a non-verbatim locator in the record looking verified.
2. **Staged receipts missing `event_at`** — `machine` (`staged_receipt_check.py`). Not
   `severity_high`: the writer's own gate could never have passed it, and `record --dry-run` had
   already said the chain position was fine.
3. **Dependency screen run from the worktree** — `machine` (the screen's own refusal, which failed
   closed rather than reporting clean). Not `severity_high`; and the failing-closed behaviour is worth
   noting as the gate working exactly as designed.
4. **Lithium and ethosuximide counted as two roads** — `self`. `severity_high`: **yes**. It would
   have inflated the evidence base of the census by one independent study that does not exist.
5. **The clinical-benefit column** — `peer` (the coordinator's reconciliation message, carrying the
   Harness clinical census). Not a defect of mine, counted because it changed the note: without it § 1
   would have said "not searched" where the correct statement is a **finding with its own caveat**.

**`severity_high · of which self` = 1 of 2.** That is the line to watch and it is only half. The
machine caught the locator-fidelity defect; I caught the double-count. The honest reading is that my
own re-reading is carrying more weight than in the waves where the ratio was 0 of n, and still not
enough: the stitched quote was mine to catch at the moment I typed the ellipsis, and I did not.

---

## 4 · The proportional micro-upgrade

🔴 **Finding, reported and not patched: `dependency_integrity.py fetch` cannot ingest a current
Retraction Watch snapshot.** The download succeeds and `build_pin` → `count_rows` then dies with
`UnicodeDecodeError: 'utf-8' codec can't decode byte 0x92 in position 6514` — a Windows-1252 right
single quotation mark inside a title field. Three call sites open that CSV with a bare
`encoding="utf-8"` (`count_rows`, `load_index`, and the staleness path). The consequence is that the
held snapshot can never be refreshed: every manifest written from here on carries a snapshot that is
41 days old and ageing, and the staleness is invisible except inside each dependency block.

**The fix is two characters of policy and is deliberately NOT applied here**:
`errors="replace"` (or a `cp1252` fallback) on those opens. DOIs are ASCII, so the index is
unaffected; only the odd character in a title field would be substituted. **I am not editing a shared
`framework/scripts/` file mid-task while a Harness agent is active in the tree** — that is a
coordination risk out of proportion to the defect — so the upgrade this session makes is the
**measurement and the exact patch location**, handed to Harness Engineering, plus the operational
note now recorded in `DEFAULTS_TAKEN`: run the screen from the shared checkout with
`--manifest-dir` pointing at the worktree, because from a worktree it fails closed on a snapshot that
exists.

**Second, smaller upgrade, already applied where it belongs:** the stitched-quote lesson is written
into the note's own method section as a rule I will carry — *a locator is one contiguous span or it is
two locators* — rather than left as a resolved validator complaint nobody will re-read.

---

## 5 · `skills_considered`

| Skill | Used | Reason |
|---|---|---|
| `legend-session-self-eval` | **yes** | this file |
| `legend-capability-scout` | **yes** | § 4 |
| `find-fulltext` | no | both papers are PMC open access and the NCBI efetch JATS route returned a complete body on the first call; no cascade was needed |
| `legend-locator-audit` | no | no locator narrows, reverses or corroborates a consolidated baseline claim, and the commit candidate declares MINOR; the triples are persisted for a later audit |
| `legend-safety-triage` | no | an ADMET/BBB triage is a promotion step for a molecule this reconnaissance deliberately does not promote |
| `legend-discovery-method` | no | optional toolkit; the task was a bounded census of what has been tested, not a search for a new mechanism |
| `legend-paperqa` | no | external API spend is reserved to the operator |
| `legend-proband-priority-matrix`, `legend-hypothesis-forge` | no | both would rank or generate candidates; the contract asks for a census that promotes nothing |

---

**Not medical advice. Class level only.**
