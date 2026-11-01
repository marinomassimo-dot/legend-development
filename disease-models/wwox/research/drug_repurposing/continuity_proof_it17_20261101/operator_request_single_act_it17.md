# Request to the operator: one bundled act, publication of the shareable repurposing view

> **STATUS UPDATE, 2026-11-01 (IT18): AUTHORISED by the operator in the IT18 mandate integration.** First publication of the shareable view and its later updates are authorised **only while free, initially and in steady state** (no paid service, purchased domain, backend or commercial dependency; a change of the provider's terms does not authorise any spend). This standing authorisation covers the four steps below and later updates of the package; it is not to be requested again within that perimeter. The "reserved act" wording that follows is kept as history. Residual items, if any, are recorded in `view/DEPLOY.md` section 9.


Prepared 2026-11-01 (IT17, phase 2). This text asks; it applies, enables and dispatches nothing. Nothing in it is medical advice; the page is research material about a disease-level genotype class. The act is reserved to the operator (`LEGEND_CORE.md` section 21d, publication to any public surface other than a development-repository push; `view/DEPLOY.md` section 9). A Pages site is a second public surface. No operator answer to the earlier requests (`ops_it11_p5_20261031/operator_request_publish_view_it11.md`) is recorded.

## The decision asked

Answer yes or no to this single act. If yes, the four steps below are done together, by the operator or by an actor the operator names for exactly this act. If no, nothing changes and the preview stays local.

## The four steps (in order)

| # | Step | What it does | Reversible, and how |
|---|---|---|---|
| 1 | Apply `ops_it11_p5_20261031/activate_workflow.patch` (`git apply` on `main`; phase 1 found it applies cleanly at `3e167e25`) and commit both parts together | Adds `.github/workflows/publish-shareable-view.yml` (`workflow_dispatch` only, jobs `verify`, `deploy`, `smoke`, every `uses:` pinned to a commit SHA, no secret, no schedule, no push trigger) and edits one assertion in `framework/scripts/test_repurposing_view.py` so the test expects that file under `.github`. The test reads `git ls-files`, so the two must land in one commit | `git revert` of the commit (`DEPLOY.md` section 8, point 2) |
| 2 | Settings, Pages, Source = GitHub Actions; restrict the `github-pages` environment to `main` | Lets the workflow publish to a Pages site and only from `main` (GitHub's own recommendation, `DEPLOY.md` section 11) | Settings, Pages, "Unpublish site" or disable the source (section 8, point 1); effective within minutes, CDN caches may linger |
| 3 | Push the step-1 commit, which holds the workflow file, to remote `main` (a push under the push rule of section 21d; a `workflow_dispatch` needs the workflow on the default branch), then dispatch the workflow on `main` | `verify` compares every package file with the section 4 table and `manifest.json`; `deploy` publishes exactly `view/shareable_package/`; `smoke` fetches the live page (200, digest, robots tag) | Same as step 2; the dispatch can be repeated, nothing runs by itself |
| 4 | Run the post-publication checker (below) and the two local checks | Confirms conditions a to f against the live URL; g and h run on the package file | Read-only |

Expected address: `https://marinomassimo-dot.github.io/legend-development/`. Phase 1 (2026-11-01 16:49 UTC) read it as HTTP 404, the repository as public with no Pages site, and remote `main` as holding only the release-gate workflow; the package digests match the section 4 table, and the package is already on remote `main`.

## What the act does not change

- No history is rewritten and no visibility is changed. The findings of `licence_inventory_it7_20261029.md` (rights and history of third-party material) remain a separate reserved decision, still open.
- Copies that a third party has already made or cached cannot be recalled by any rollback.
- The page collects nothing and loads nothing from another host (the checker verifies the second point on static markup only: `src`, `link href`, `script`, not scripts that fetch at run time).
- Indexing default: the page carries `noindex,nofollow`; GitHub Pages sets no per-site header, so this is the only lever, and the page stays reachable by anyone who has the URL.
- The ChEMBL records stay a separate CC BY-SA 3.0 file with its own licence text and credit, next to the page.

## Command after publication

```bash
python3 -B disease-models/wwox/research/drug_repurposing/continuity_proof_it17_20261101/check_published_view.py https://marinomassimo-dot.github.io/legend-development/
python3 -B framework/scripts/repurposing_view.py viewports        # g: 360, 390, 768, 1280 px, on the package file; a line 'SKIP: no Chromium' with exit 0 means NOT measured
python3 -B framework/scripts/repurposing_view.py audit-shareable --dynamic   # h: on the deployed commit
```

The checker makes GET requests only, needs no credential, refuses redirects to another host and has no default URL. Exit 0 means conditions a to f hold; 1 prints one `FAIL [condition] ...` line per failure; 3 means `NOT_YET_PUBLISHED` (the production URL answers 404), the expected state today and never a pass. The phone re-run of g on the real device remains a manual step. The `smoke` job in the patch covers only a, the `index.html` digest and the robots tag; the checker covers the rest. Adding it to the workflow would change the patch and is not proposed here.

## What is unknown

- Whether the Pages feature is available to this repository on its plan is not verifiable from public information; `DEPLOY.md` section 11 does not assert it. Settings, Pages shows it before step 2.
- Decision to answer yes or no: does each later dispatch need a fresh instruction? Until the operator says otherwise, yes (`DEPLOY.md` section 12, last sentence).
- Update cycle after later versions (one line, `DEPLOY.md` section 12): regenerate, package, audit, land, push, re-dispatch, re-run the checker.
- Correction to an earlier statement: the `smoke` job of the patch enforces only the HTTP 200 and the `index.html` digest; its robots check only prints a note and never fails the job. The robots tag is verified by the checker (condition c).
