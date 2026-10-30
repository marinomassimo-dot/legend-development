# One request to the operator: publish the shareable view (prepared 2026-10-30, nothing executed)

Everything here is the operator's act: enabling Pages, copying the workflow, dispatching it. Re-verified read-only on 2026-10-30 (evidence:
`evidence/action_pins_and_repo_20261030.txt`).

## Facts re-verified today

| fact | result 2026-10-30 |
|---|---|
| the four pinned SHAs exist in their action repositories | all four `GET /repos/actions/<name>/commits/<sha>` answer 200 |
| the tags still point to them | `v7.0.1` 3d3c42e5..., `v6.0.0` 45bfe019..., `v5.0.0` fc324d35..., `v5.0.1` 368f8252... (lightweight tags, same SHAs as in the workflow); none archived; newer tags of the same major lines: none |
| immutability | a SHA cannot be moved; the workflow uses SHAs, the tags are only comments (a tag could be moved, which is why they are not trusted) |
| Pages limits (docs.github.com, read today) | site at most 1 GB (the package is 3.0 MB), repository recommended 1 GB, soft bandwidth 100 GB/month, deployment timeout 10 minutes |
| Pages source / workflow | "Under Build and deployment, under Source, select GitHub Actions"; the templates use the environment `github-pages` and GitHub recommends a protection rule limiting it to the default branch; the deploy step is skipped on pull requests |
| workflow permissions | `contents: read` at top level; only the `deploy` job holds `pages: write` and `id-token: write`; no secret, no third-party action |
| the proposal matches the package | the proposal's own verify script, run locally against `view/shareable_package` and `view/DEPLOY.md`: "package matches DEPLOY.md and its manifest"; `package --check`: "package is current" |
| repository | public (`private: false`), `has_pages: false`, default branch `main`, remote `main` = `90f26804`; the site URL answers 404 (not deployed) |
| not documented on the pages read, so not asserted | Pages from a private repository (irrelevant: the repository is public) |

Gaps that make the workflow fail if ignored: (1) the workflow reads the package from the checked-out `main`, so the final package must be on the
remote `main` first (the Orchestrator regenerates it at the end of IT9 and pushes); (2) the package text still says "a local preview, not
published" (DEPLOY.md section 6) and has no robots meta tag (section 7): change both in one commit with the decision, regenerate, `package --check`.
Recommendation on indexing: add `noindex,nofollow` while the history findings stay open; the page remains reachable by URL.

## What to do, in order

1. Decide the two wording points above (publish wording, noindex) and tell the Orchestrator; it makes the generator change, runs
   `repurposing_view.py package` and `package --check`, `audit-shareable --dynamic`, `public_release_gate.py`, and pushes.
2. Check that the pushed `main` carries the package: `git ls-remote https://github.com/marinomassimo-dot/legend-development.git refs/heads/main`
   equals your local `git rev-parse main`.
3. GitHub, repository Settings -> Pages -> Build and deployment -> Source -> GitHub Actions. (Click path from the documentation; the page is not
   reachable without your login, so it was not checked.)
4. Settings -> Environments -> `github-pages` (it appears after step 3 or after the first run) -> Deployment branches and tags -> Selected
   branches -> `main`. This is the protection GitHub recommends.
5. Add the workflow file in one commit on `main` (your machine, a token with the `workflow` scope or your usual login):
   ```
   mkdir -p .github/workflows
   cp disease-models/wwox/research/drug_repurposing/view/DEPLOY_pages_workflow.proposal.yml .github/workflows/publish-shareable-view.yml
   git add .github/workflows/publish-shareable-view.yml && git commit -m "Add the manual Pages workflow for the shareable view" && git push development main
   ```
6. Actions tab -> "Publish the shareable view (manual, proposal)" -> Run workflow -> branch `main` -> Run. Two jobs: `verify` (digests) then `deploy`.
7. If `verify` fails it names the file that differs from the DEPLOY.md table: stop, do not edit the table by hand, tell the Orchestrator.

## Verify the URL afterwards (about 5 minutes, no login)

```
URL=https://marinomassimo-dot.github.io/legend-development/
curl -s -o /dev/null -w "%{http_code}\n" "$URL"                                   # expect 200
curl -s "$URL" | sha256sum                                                         # expect the index.html digest of the DEPLOY.md section 4 table
curl -s -o /dev/null -w "%{http_code}\n" "${URL}NOTICE.md"                        # expect 200
curl -s -o /dev/null -w "%{http_code}\n" "${URL}LICENSES/CC-BY-SA-3.0.txt"        # expect 200
curl -s -o /dev/null -w "%{http_code}\n" "${URL}class_b/chembl_cc-by-sa-3.0/CREDIT.txt"   # expect 200
curl -s "$URL" | grep -c 'name="robots"'                                           # 1 if noindex was added
```
Then open `$URL` at 360, 390, 768 and 1280 px (or run `python3 -B framework/scripts/repurposing_view.py viewports` on the package file) and
confirm that the page loads without a network request outside the host. Tell the Orchestrator the result; it records the URL in the README
and the mandate record.

## Restore

Settings -> Pages -> "Unpublish site"; delete `.github/workflows/publish-shareable-view.yml` in a commit. Cached copies already fetched by
third parties cannot be recalled. Cost of the whole operation: free for a public repository; no account, no payment.
