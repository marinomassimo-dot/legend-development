# Selective registry access — what a reading stops carrying, and what it must not lose

**Written:** 2026-09-11 · **By:** `orchestrator` · **Mandate:** reduce the Scientists' context and
repeated work while preserving scientific coverage, provenance, caveats and the independence of
the blind first read. Principle: minimum intervention, maximum measurable result.

---

## 1 · The state found, and the three things it is made of

| | |
|---|---|
| **Prescription** | `operator_manual.md` § 1.1–1.3 told MINIMAL, STANDARD and FULL sessions to load *"i 4 file current"*. Two of the four are large and grow monotonically: `paper_registry_current.md` **402 KB / 443 records**, `literature_tracking_log_current.md` **480 KB / 406 records** (re-measured 2026-09-11). A single-paper triage carried the whole history of the corpus. |
| **Observed behaviour** | Over the four session transcripts available on this host: **zero `Read` calls on either registry**. Access happened through ad-hoc shell — 16 Bash calls naming the paper registry, 8 naming the literature log. The expensive prescription was already being avoided, by grepping. |
| **Hypothesis, not measured** | What the 2026-09-09 scientist sessions did. Their transcripts are not on this host. Nothing here claims to know. |

The gap between the two halves is the finding: the written rule was costly, and the unwritten
habit that replaced it returns **fragments**. A fragment is how a caveat dies — the sweep's S3,
*"a caveat alive in prose and dead in a table"*, is the same defect at a different layer.

## 2 · What changed

`framework/scripts/registry_records.py` — one file, two subcommands, no new state, no second
registry. The canonical files are untouched, never summarised, never mirrored; every answer is
parsed from the current file at call time and carries the digest of what it read.

| Guarantee | How |
|---|---|
| Records come back **whole** | the exact byte slice from its `##` heading to the next one — no field dropped, re-ordered or normalised |
| **Identity is not mention** | identity is the `Identifier` / `Identifier value` field; a PMID cited in prose, or in a claim's `Source` line, is a `mention` and is labelled as one |
| Provenance travels | path, record id, line, record digest, and the digest of every source file consulted |
| Links resolve | one hop per `--hops` along declared wikilinks; a link whose target does not exist is reported `UNRESOLVED`, never dropped |
| Expansion is explicit | `--hops`, `--theme`, `--id`; nothing widens by itself |
| Ambiguity is shown, not resolved | two records claiming the same identifiers are named together — *"a reader decides which, not this command"* |
| Prose sections are named, not carried | a block with no identifier and no record-shaped id is listed as matched-and-withheld, with its size and the command to fetch it |
| **No silent truncation** | `--limit` prints the residue; records are never cut inside |
| **An empty result is not a finding** | exit 1, and the words *"this is not evidence that the laboratory does not know this paper"* |

**Prescriptions updated in the same intervention** — a command nobody is told to use changes
nothing: `operator_manual.md` § 1.1, § 1.2, § 1.3, § 2, § 7; `legend-start` step 5; the standing
brief's new **M4b** (the comparison phase); the `legend-deepdive` and `study-intake-triage` agents.

**Deliberately NOT extended.** `working_model_current.md` (46 KB) and `claim_registry_current.md`
(112 KB) stay loaded whole below FULL. They are the global state, and a claim a paper contradicts
may not be linked to that paper — selective retrieval cannot promise to find it. Evaluated
separately, as the mandate required, and left alone.

## 3 · The three phases, now separated in the instructions

| Phase | Carries | Never carries |
|---|---|---|
| **Blind first read** | sources, method, and the technical packet (`paper_packet.py`) | any prior LEGEND conclusion about the paper (`scientist_reading_modes.md` § 3.1, § 3.3) |
| **Comparison** (brief M4b, after the receipt) | the relevant records whole — claims, premises, contradictions, sources — expanded deliberately | the two large registries in full |
| **Integration** | whatever propagation needs; `BATCH_COMMIT` and every scientific obligation unchanged | — |

## 4 · Measured, before and after

Same input, same criterion: the characters a session must carry.

| | Characters |
|---|---|
| OLD — the four current files, every MINIMAL session | **1,066,618** |
| …of which the two now selective | 903,389 |
| NEW — per paper, one hop, records whole (7 papers; median 33,471) | **29,864** |
| …still loaded whole: working model + claim registry | 163,229 |
| **What a MINIMAL session carries** | **1,066,618 → 193,093 (−82 %)** |

Cost: 0.2 s per query. Seven papers measured: 33914858, 29724996, 18460020, 20146584, 25411445,
21115974, 15070730.

🔴 **These are characters, not provider-billed tokens.** The telemetry that would separate input,
output and cached tokens is not exposed here, and the 2026-09-09 startup-context audit measured
text sizes rather than consumption
([`SLR-plan-20260909-startup-context-audit.md`](../../../learning/plan/SLR-plan-20260909-startup-context-audit.md)).
What is established is the size of what must be carried, not a bill.

**And the first measurement was worse than the baseline.** The first cut treated every `##`
heading as a record, so an incidental PMID inside a 470,808-character `## Change-log` block
dragged it in and its wikilinks exploded at hop 1: **602,474 and 689,116 characters** for two
PMIDs, against a 1,066,618 preload. Naming what is addressable fixed it at the root. Capping the
output would have been silent truncation with a better name.

## 5 · The omission check — built independently, then handed to an independent reader

Expected sets were derived with a different mechanism (line scans over the raw files), never from
the selector's own output. Six adverse cases, all instantiated on real records:

| Case | Instance |
|---|---|
| identifier ambiguity | PMID 33914858 is claimed by **two** paper-registry records |
| identity vs incidental citation | the same PMID cited inside a third record's prose |
| dependency between papers | 18460020's reagents descend from 16223882 |
| caveat a fragment would kill | CLAIM 030's methodological caveat, mid-record |
| reachable only past hop 0 | the claim a paper stands on is one wikilink away |
| empty result | a query matching nothing must not read as *"not known"* |

Then an **independent verifier**, given the claim under test, the files and the result format —
and no producer narrative, no verdict, no session record — built its own expected answers first.

**First pass: four of five claims REFUTED**, over 22 PMIDs / 118 records:

1. an em dash in the *next* heading was not a boundary, so `LIT-0405` returned 6,860 characters
   where the file holds 2,751 — and manufactured false mentions on five further PMIDs;
2. `Source` counted as an identity field, so **thirteen claims** were labelled identity matches
   for a PMID that is only their citation;
3. the ambiguity key compared whole identity strings, so `PMID / PMC / DOI` and `PMID / DOI / PMC`
   read as different papers — **ten duplicate pairs unreported**;
4. `CORPUS P###` (188 headings) and `LIT-EX-###` (6) were withheld as prose, so records holding a
   real identifier never came back and their links were never followed.

All four repaired, each pinned as a regression. **Second pass: six of six CONFIRMED**, zero byte,
label or presence differences over 67 PMIDs — and two further ambiguity misses found, where one
record carries a bare PMID and the other `PMID / DOI`; both repaired, with the cosmetic artefact
(digits from a DOI suffix entering the PMID key) repaired beside them.

**This is the case for keeping verification independent and expensive.** This file's own suite
passed while four of its five guarantees were false, because the suite asked the same question
with the same splitter the tool used.

## 6 · What was not established

- **No scientific reading was run through the new path.** Coverage, lost caveats and missed
  contradictions in a real reading are unmeasured; only the transport is verified. The four
  numbers a first wave owes are in
  [`2026-09-11_control_efficacy_baseline.md`](2026-09-11_control_efficacy_baseline.md) § 2.
- **Token consumption is not measured**, only characters carried.
- The verifier's own limit, in its words: where a block has no identifier and no record-shaped id
  but *should* be addressable, *"the tool and I are wrong together"*.
- The scientist sessions' actual loading behaviour on the previous host remains unknown.

## 7 · Residual risks, and how to undo this

| Risk | Mitigation | Reversal |
|---|---|---|
| A relevant record names neither the query nor a returned record | stated in every answer's *limits of this selection* line; `--theme` and `--hops 2` widen deliberately | — |
| A registry grows a record shape the id rule does not know | a block carrying an `Identifier` field is a record whatever its heading; only shapeless prose is withheld, and it is named | add the shape to `RECORD_ID` |
| Selective access becomes an excuse to read less | the reading obligations are untouched: full text, receipts, locators, coverage maps, `BATCH_COMMIT` | — |
| The change is wrong | it is four documentation edits and one new script. Revert the commit; the registries were never modified, so nothing scientific has to be restored | `git revert <sha>` |

Nothing in the claims, the reading depths or the receipts was modified to make a check pass.
