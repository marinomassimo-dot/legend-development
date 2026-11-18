# ADV response to the blind audit of CLOSING_SYNTHESIS.md (2026-11-16; non-canonical)

Audit: it_synthesis_audit_20261116/AUDIT_RESULT.md (audit_table.tsv sha256 bcfc0a2c..., number_check.tsv sha256 54195c23..., input copy sha256 9f486e46...). Audited text a0bc5e0c729f; corrected text: CLOSING_SYNTHESIS.md in this commit. Not edited: the audit files. Verdicts: supported 28, overstated 12, unsupported 1, not checkable 5; numbers: 135 of 148 match, 10 do not (8 distinct), 3 source not found.

| Claim | Verdict | What I did |
|---|---|---|
| A2 | overstated | ACCEPTED. 'Every scoring thread' narrowed to the three threads that carry the top set (T1, T2, T13), all from Breton 2021; other threads from other sources do not drive the top set. |
| A3 | overstated | ACCEPTED. 'The only agent with a WWOX experiment is ethosuximide' was wrong: lithium was also tested in Wwox-null pups (origin hunt C8); 'no agent ranking' now cites the generator's 'agent ranking not licensed' output. |
| A7 | overstated | ACCEPTED. The valproate tension kept as the cited tension; 'first candidate for a frozen prediction' relabelled ADV opinion (not in the folder); 'the sign follows the context' limited to the agent level (lamotrigine, carbamazepine), not shown for the valproate class. |
| G1 | overstated | ACCEPTED. 'About 24' was only the paper-content subset: the ledger check gives 44 rows with the scored file already in the tree (24 paper-content), 51 predictor = scorer, 84 hitting at least one limit (some hit both). |
| G2 | overstated | ACCEPTED. 'Disclosed by IT before anyone read it' removed (session event not in the cited files); replaced by what the files state: the invalid run saw 14 full hypotheses, its table was withheld. |
| G7 / X8 | overstated | ACCEPTED. 'Three freezes' corrected to FOUR items (HE's leap file, IT's leap file, IT's extractor release record, arm A's output); the protocol is status PROPOSED, not normative. |
| G8 / D1 | overstated | ACCEPTED. 'Twelve' replaced by eleven by id (PS-01..07, PS-11..14); PS-08, 09, 10, 15 are event statements. The sources (SCI's README, IT's count) say twelve: the discrepancy is in the sources, and the ids are used. |
| G9 | not checkable | ACCEPTED. Marked as ADV opinion, not derived from the arm comparisons (which are not separable); only the cost figure is checkable; relabelled a hypothesis for the next programme, not a finding. |
| E2 | overstated | ACCEPTED. For 'no arm suppresses' (S7) the generator prints valproate-type alone, size 1, 'discriminating' (a breadth-only, untested class); 'none' was the brief's reading. Both now stated. |
| E4 | overstated | ACCEPTED. Radiprodil is clinical-stage (PMID 42596612), not a tool compound; ADMET-AI and RDKit are named in the readiness README, medchem in IT's triage README. |
| K1 | unsupported | ACCEPTED. The four session totals now follow the committed PROGRAMME_COST.md (935 turns, 1,217,228 output, 2,306,863 cache written, 401,673,811 cache read); the earlier figures came from HE's draft message. Final rerun at 15:10Z. |
| X5 | overstated | PARTLY ACCEPTED. IT's `--help` syntax error documented; SCI's missing executable bit is documented in git (commit fb06c2473 'verify_quotes.py executable and --help safe'), which the audit did not search; 'within minutes' removed. |
| X1, X4, X6, X7 | not checkable | NOT DISPUTED. Session events: X1 and X4 are in my task record's trial log; X6 is SCI's own report; X7 has no file record. The synthesis now says 'session event, not checkable from the files'. |
| Decisions D2-D7 | premise only | NOTED: the audit verified the factual premise, not who decides: the decisions are the operator's. |

Audit conditions I record: the auditor's three attempts to read UNBLINDED.md, UNBLINDED_1B.md and PLANTED_KEY.json were denied by the permission classifier and nothing was read; arm labels came only from cited files; it could not rerun programme_cost.py (transcripts are not in the repository). Cost of the audit (IT): 76 turns, 80,641 output tokens, cache written 254,653, cache read 10,672,945.

Net effect: 12 of 12 overstated or unsupported rows corrected; no headline of section 0 changed; two statements of fact were wrong in the draft (lithium; radiprodil) and are the kind of error a reader would have repeated.
