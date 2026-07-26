---
name: legend-lint-repair-plan
description: Turn LEGEND LINT output into a safe repair plan grouped by gate impact. Use when LINT reports BLOCK_BATCH_COMMIT, BLOCK_SYSTEM, missing wikilinks, invalid statuses, duplicate IDs, or the operator asks how to unblock BATCH_COMMIT. Produces plans only unless explicitly asked to edit.
---

# LEGEND Lint Repair Plan

Produce a repair plan for LEGEND integrity findings without applying canonical changes by default.

## Workflow

1. Run or read:

```bash
python3 framework/scripts/legend_lint.py .
```

2. Classify findings:
   - `BLOCK_SYSTEM`: recovery first; no deep dive, no commit.
   - `BLOCK_BATCH_COMMIT`: deep dive/ingest can continue; BATCH_COMMIT blocked.
   - `WARN_BUT_PROCEED`: include in backlog; do not block unless linked to a block.
   - `INFO`: note only.
3. Map each finding to the smallest safe repair:
   - invalid status -> normalize vocabulary only via BATCH_COMMIT if in current files.
   - missing claim-to-paper wikilink -> identify whether the support paper already exists or must be promoted from corpus-paper.
   - paper without claim-link -> check status; `background_only`, `archived`, `bridge_only` are exempt.
   - duplicate ID -> stop and require manual resolution.
4. Output a sequenced plan:
   - `Now / commit-blocking`
   - `Batch candidate`
   - `Backlog`
   - `Do not do`

## Hard Rules

- Do not create scientific claims just to satisfy a structural rule.
- Do not modify the 4 canonical current files unless the user explicitly asks for a BATCH_COMMIT-like edit and the full protocol is followed.
- If a fix changes scientific meaning, mark it `OPERATOR TO DECIDE`.
- Prefer structural fixes that preserve all existing text.

## Output Template

```markdown
## LINT Repair Plan

### Gate
- Deep dive: READY | BLOCKED
- BATCH_COMMIT: READY | BLOCKED

### Commit-Blocking
| Finding | Cause | Minimal repair | Where | Gate |

### Backlog
| Finding | Why deferred | Suggested batch |

### Do Not Do
- ...
```
