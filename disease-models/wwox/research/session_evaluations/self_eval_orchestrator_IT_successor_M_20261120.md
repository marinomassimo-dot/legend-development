# Self-evaluation: IT Orchestrator successor window M, 2026-11-20 (packet changes 4 to 6, open-question lines, ADV-106 and ADV-109 prospective tests, titles cache, publication-repair collection)

Hypothesis level; no dose; reference genotype class only; not medical advice. No full-text read was completed in this window (no receipt written); the work was card and packet text, open-question lines, two prospective prediction tests (the target bodies were read by SCI as scoring passes, not receipts) and one cache fix.

## Scope and executable verdict
- Batch/session: IT successor window (mandate ORCH-ROADMAP-IT59-20261119), 2026-11-20.
- Studies and complete-read receipt IDs: none created. SCI's truth-table and scoring reads (PMID 19451696, 18509642, 29912275, 30631446) are explicitly not receipts.
- `session_self_eval.py --workspace . --disease wwox`: VERDICT PASS (receipts 2201, complete events 330, unread premises 0/0; declared gaps listed belong to other readers' PMIDs, not this window).
- Receipt verification: OK, 2201 chained receipts, tail anchored.
- Structural LINT: 0 BLOCK; two WARN_BUT_PROCEED (UNLINKED_SUPPORT, claims 040 and 042) are not from this window.
- Local verdict: PASS. Workspace/global verdict and concurrent conditions: CI (the Public release gate 'Regression tests' step) is RED on 3c8cb834d, 812d814f8, 4dad5528f and fc1cc00e1 and was already red on e4275e32c and d5280b5e7; four later SHAs in progress when last read; failing tests not nameable without authenticated logs; HE owns the reproduction (ADV-108). The local gate PASS of `safe_push` is not evidence that CI is green.

## Content diagnosis
| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Not applicable to IT; SCI read three bodies as text (figures not opened as images, stated in the truth table) | partial | figure-only values were not scored; ten of 28 ADV-109 slots definition-exposed |
| Main message and original contribution | ADV-106 and ADV-109: generator ties baseline and abstract-only; inconclusive; RP-005 revise then PARK (ADV) | strong | one-slot margins are not evidence; stated in both records |
| Hidden gold beyond keywords/abstract | SCI N1: the vigabatrin abstract's 'tissue/plasma ratios' are S/R ratios; T2 mice all in withdrawal; Uebele temperature effect time-of-day dependent | strong | consumer lines: WO-24 line landed; two sentences sent to SCI; ADV decides the rest |
| Source parity: context, type and recency | Excluded papers already read by delegates (Brown 2016, Xenon 2025) by ledger and file search before choosing | strong | route flakiness (PMC page vs efetch) disclosed per text |
| Team type, field density, observation vs interpretation | not applicable | n/a | |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | packet text labelled class-level, no dose, no score; blind audits on three packet changes; repairs made after the last check marked UNAUDITED | partial | unaudited repairs stay stated |
| Existing claims touched; conflicts/revival triggers | F02 'tiratricol' and 'tta-a2' reach the shareable page: left untouched (item 17 for the operator); package held | partial | operator decision pending |
| Multi-hop and corpus cross-query | RP-008 census checked: obtainable texts cannot move a decision (SCI ADV-086), so ADV-109 took abstract-cited papers from HE sheets, disclosed | partial | the substitution was disclosed, not asked |

## Persistence diagnosis
- Durable IDs: results at `prospective_rp005_adv106_20261120/RESULT_...` and `prospective_rp005_adv109_20261120/RESULT_...` (landed 910399c06, 10460a250, 7d6542e8b); packet changes 812d814f8, fc1cc00e1; open-question lines 4dad5528f and 310fe19ef; titles ae21f34fd.
- Reading queue/debt: PMID 22315091 human read stays flagged; CLAIM 035 part 2 operator; item 17 operator.
- Dossier and commit candidate: none (no BATCH_COMMIT in this window).
- Receipt source fingerprint: SCI's page hashes are in the truth table; sealed prediction file hash verified before and after.
- Can a future run distinguish full text from abstract only? Yes for ADV-109: each text carries route, status check and the hash of the response SCI read; the abstract-coverage table is in the scorer sheet.

## Process and capability diagnosis
- Skills/gates/patterns used: blind audit packets (sonnet, high) for three packet changes; wording pilot; sealed-file with committed hash and second custody; truth-table-first scoring; mechanical hit computation; independent recomputation by SCI (matched).
- Plausible skills deliberately declined, with reasons: legend-discovery-method (optional); a new compound-proposal run (not the question).
- Failures: a poll that signalled 'landed' on a stale baseline; delegate reports labelled 'verbatim' when condensed; baseline instantiation that did not follow its own rule R3 (two slots); two wrong counts in the first landed ADV-109 result text; ADV's premise that BATCH5 held the vigabatrin ratios; classifier refusal to reword F02.
- What caught each failure before an overclaim: baseline mismatch found by me at assembly, before the truth table existed, and disclosed as amendment 2; wrong counts found by me re-reading the slot table, corrected the same day with a correction note; BATCH5 premise found by search; stale poll found by comparing the stored baseline SHA; condensed-report labels corrected in headers; F02 refusal respected and escalated.
- Disease-agnostic micro-upgrade shipped: the truth-table-first scoring protocol (scorer sees no prediction; hits computed mechanically against a hash-sealed file) replaced anonymous sets plus key: it removes order leakage and lets another person recompute (SCI did, exact match). It lives in the ADV-109 pre-registration section 9 and scorer sheet, not yet as a script.
- Regression/evidence that makes the upgrade persistent: the sealed file and its slot-level table let anyone recompute (SCI's independent recomputation message); no test was added. Honest: this upgrade is a recipe, not a regression.
- Residual risk and next decisive action: CI red unexplained (HE, ADV-108); item 17 for the operator (names guard, then the package); a script that computes hits from a truth table and a sealed file would make the recipe repeatable if RP-005 is ever resumed.

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 8
machine: 1   blind_auditor: 2   peer: 1   self: 4
severity_high: 2   of which self: 2
undetected_known: 0
```
Incidents: classifier refusal on F02 (machine); blind audits finding absence claims without 'found by these routes', non-literal quotes and merged populations in packet text (blind_auditor); wording pilot finding ambiguous slot options and two abstract leaks (blind_auditor); ADV's BATCH5 premise (peer); stale-baseline poll, 'verbatim' mislabel, R3 baseline mismatch, wrong counts in the landed result (self; the mislabel and the wrong counts reached a landed record: severity_high). `undetected_known` is 0 only as far as my own re-reading and SCI's recomputation reach.

## §21c output
DEFAULTS_TAKEN: ADV-109 texts taken from HE-sheet citations instead of the WWOX census (disclosed); stricter truth-table protocol instead of anonymous sets (disclosed, section 9); margin kept, INCONCLUSIVE rule added before scoring (disclosed). STOP_LOG: reCAPTCHA pages on PMC (three texts, 42124576) were not bypassed; the F02 and 'tta-a2' name guard was not touched (item 17, operator).
