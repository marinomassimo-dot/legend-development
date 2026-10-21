# Self-evaluation — repurposing batch group R4, scientist-d (2026-10-21)

## Scope and executable verdict
- Batch/session: `ORCH-REPURPOSING-10H-20261021`, task `REPURP-10H-R4-D-20261021`, branch `task/repurp-r4-d`. NOT WWOX EVIDENCE throughout.
- Receipts: 22 staged `FTR-20261021-<pmid>-01` under `receipt_staging/scientist-d/` (15 `complete_fulltext_read`, 7 `partial_fulltext_read`); 22 manifests under `deepdive_manifests/`, all PASS, 14 to 27 verbatim locators each.
- `session_self_eval.py`: VERDICT PASS (unread_premises 0/0; declared gaps listed belong to other PMIDs). `fulltext_receipts.py verify`: OK, 685 chained receipts. LINT: run at close (see task JSON RESULT).
- Local verdict: PASS. Global: concurrent actors R1 to R3 and audits were running; no blocking condition seen.

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Sequential full text, figures, tables, supplements | Figures opened as images for the load-bearing trials; supplements read for EPISTOP, soticlestat, SCN2A ASO. Figures and supplement of 37638552 and 41061327 not retrievable (404/403) | partial | Parked with cascade; 7 readings are partial |
| Main message | Early-benefit claims in this family: EPISTOP concept did not replicate in placebo-controlled PREVeNT; two soticlestat phase 3 non-replications despite ~80% 24HC fall; n-of-1 and ASO claims rest on own baselines that drift | strong | Blind audit owed |
| Hidden gold | SCN2A ASO Vineland moved 15 to 28 points before any dose; Fig 4a labelling; LGS endpoint chosen from post hoc phase 2 subgroup whose interval included zero; BUTTERFLY drift exceeds the 2 to 3 point meaningful-change band | strong | Audit owed |
| Source parity | Reviews and protocols read as syntheses, primary trials as data; recent 2025/2026 work weighted for design, not for WWOX | strong | None |
| Team type | Mostly consortium trial groups and descriptive sponsors; no WWOX group | partial | Not scored per group |
| DATO/INFERENZA/IPOTESI/ESPANSIONE | Design table facts are DATO; WOREE consequences are INFERENZA; endpoint proposals are IPOTESI | strong | None |
| Existing claims touched | CLAIM 046 and PMID 36537114 row read against, neither narrowed nor reversed | strong | None |
| Multi-hop / cross-query | Registry compared per paper; adjacent search found 6 further readings; 42389070, 42334048, 37045569, 36538782 queued as candidates | partial | Not read |

## Persistence diagnosis
- Note: `disease-models/wwox/research/repurposing_10h_scientist-d_20261021.md`; selection-file answers entered; commit candidate `CC-20261021-SCIENTISTD-R4-REGISTRY-01`.
- Receipts staged only (Orchestrator records). Each receipt carries coverage and fingerprint, so full text versus abstract is mechanical.

## Process and capability diagnosis
- Skills used: paper_packet rank, identity check, staged_receipt_check, deepdive_manifest. Declined: `legend-discovery-method` (optional, no novelty claim made), batch inferential sweep (not an ingest batch).
- Friction: lxml absent; manifest enum/derived-artifact rejections; NUL byte in a protocol text layer (SUSPECT); ToUnicode-less CONSORT PDF; `captions_only` vs complete; sub-30-character and hyphen-variant snippets; `@` in a URL; worktree-only rank root; Retraction Watch snapshot absent in worktree. Each caught by a validator before landing.
- Self-caught: Fig 4a caption versus panel; count 13 vs 12; 41061327 first author; 41531035 methods coverage overstated (corrected after reading full text).
- Micro-upgrade: CHANGE = NONE as a code change. Gap evidence: the spec-to-manifest builder (hyphen-variant fallback, derived-artifact metadata) lives only in the session scratchpad; disease-agnostic, worth promoting to `framework/scripts` by the Orchestrator if a second group needs it. Not shipped to avoid an unrequested tool.
- Residual risk: audits owed (listed in the note); partial readings; hyphen-stripped Scholar Gateway text not used for numbers.

ATTRIBUTION_CENSUS
incidents: 9
machine: 6   blind_auditor: 0   peer: 0   self: 3
severity_high: 3   of which self: 3
undetected_known: 0
