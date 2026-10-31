# Request to the operator: publish the shareable view (IT11 P5, prepared 2026-10-30 UTC, nothing executed)

Replaces nothing: the IT9 request (`../sharing_it9_20261030/operator_request_publish_view.md`) stays valid for its facts. This file adds what IT11 changed
and states, without ambiguity, which acts exist, who can perform them from where, and which artefact is ready to approve.

## 1. The decision

| item | answer |
|---|---|
| Is the publication authorised already? | **No.** The roadmap (R10) says "respect existing publication authority and any operator approval already granted"; none for a web surface is recorded anywhere I could read (roadmap, IT9 and IT11 mandate records, IT9 request, memory index). LEGEND_CORE 21d lists "publication ... to any public surface other than a development-repository push" as RESERVED. The repository itself is already public (`private: false`, API read 2026-10-30 22:4x UTC); a Pages site is a second, separate surface. |
| What did IT11 prepare so that your part is only the reserved acts? | The page and package text are now true both before and after publication; the indexing choice is made explicit (default: `noindex,nofollow`); the workflow gained a post-deployment check; the package is regenerated from current main and audited (static and dynamic: 0 violations); a ready patch adds the workflow file and the one test line it changes. |
| What can the Orchestrator do from this host? | Everything that is a git push over SSH: push `main` (package, generator, workflow file). The host's SSH key authenticates as the repository owner (a read-only SSH greeting test answers with the owner's login); there is **no GitHub token** (no `gh`, no `GH_*`/`GITHUB_*` variable, no credential helper, no `~/.config/gh`, no `~/.git-credentials`, no `.netrc`). |
| What can it NOT do from here? | (a) Read or change repository settings: `GET /repos/.../pages` answers 404 and `GET /repos/.../actions/permissions` answers 401 "Requires authentication" without a token. (b) Enable Pages with "GitHub Actions" as source. (c) Create the `github-pages` environment rule. (d) Dispatch the workflow (needs the Actions UI or a token). Nothing was attempted that would change a setting. |
| Therefore the minimum human acts are | **Three clicks and one authorisation**, section 3. |

## 2. What is ready to approve (artefacts)

| artefact | path | what it does | how to check |
|---|---|---|---|
| distributable package, regenerated from main `d6ccf8d1` | `view/shareable_package/` (13 files) | the static site that would be served; `index.html` carries one `<meta name="robots" content="noindex,nofollow">`; README, NOTICE and manifest no longer say "local preview / not published" | `python3 -B framework/scripts/repurposing_view.py package --check` -> "package is current"; `audit-shareable` and `audit-shareable --dynamic` -> PASS, 0 violations on both files |
| workflow proposal (updated) | `view/DEPLOY_pages_workflow.proposal.yml` | `workflow_dispatch` only; `verify` (digests against the DEPLOY.md table and the manifest), `deploy` (the only job with `pages: write`, `id-token: write`), new `smoke` (read-only; fetches the live URL, requires HTTP 200 and the package `index.html` digest) | four action SHAs re-checked 2026-10-30: all four `GET /repos/actions/<name>/commits/<sha>` answer 200 and the tags `v7.0.1`, `v6.0.0`, `v5.0.0`, `v5.0.1` still point to them |
| activation patch | `ops_it11_p5_20261031/activate_workflow.patch` | adds `.github/workflows/publish-shareable-view.yml` (same bytes as the proposal) and changes the single test assertion that says "nothing is tracked under .github except the gate" | `git apply --check` passes on this branch; the deployment test class (4 tests) passes without the patch, and with it once the new file is git-added (the test reads `git ls-files`, so an untracked file fails it: apply, `git add`, commit together) |
| local access-path rehearsal | (not a file) | the package served under the prefix `/legend-development/` from a local server: `index.html`, `NOTICE.md`, `LICENSES/CC-BY-SA-3.0.txt`, `class_b/chembl_cc-by-sa-3.0/CREDIT.txt`, `manifest.json` all 200; the served `index.html` SHA-256 equals the package file (`ed6c5260...f04a`); robots meta count 1; no `src=` or stylesheet loads from another host (external addresses are hyperlinks only). This is an intermediate result, not the delivery. |

## 3. The acts, in order, with who and where

| # | act | who | reason | reversible? |
|---|---|---|---|---|
| 0 | Confirm the two wording points: (i) indexing default `noindex,nofollow` (set in the generator; to accept indexing, empty `SHAREABLE_ROBOTS_META` and regenerate); (ii) the neutral package wording (it does not claim publication). A single reply "yes" is enough. | operator | a choice about what is published | yes (regenerate) |
| 1 | Authorise the Orchestrator to land this branch, apply `activate_workflow.patch` and push `main` over SSH. The workflow reads the package from the remote `main`, so the package must be there first. Remote `main` today is `cc4d629b` (2 commits behind local `d6ccf8d1`). | operator authorises, Orchestrator pushes | a workflow file is code that will run with Pages write permission once dispatched; it is inert until steps 2 and 3 | yes (`git revert`) |
| 2 | GitHub web, repository Settings -> Pages -> Build and deployment -> Source -> **GitHub Actions**. Then Settings -> Environments -> `github-pages` -> Deployment branches -> Selected branches -> `main` (the protection GitHub recommends). | operator, logged in | a repository setting; no token exists on this host | yes (Unpublish site) |
| 3 | Actions tab -> "Publish the shareable view (manual, proposal)" -> Run workflow -> branch `main`. Three jobs: `verify`, `deploy`, `smoke`. If `verify` fails it names the differing file: stop, do not edit the table by hand. | operator, logged in (or a future token with the `actions` scope) | the publication act itself | yes (Unpublish site; delete the workflow) |

The workflow title still says "(manual, proposal)" because the string is asserted by the existing test; it is the active workflow once copied.

## 4. What must be enabled, and the URL

| item | value |
|---|---|
| Expected URL | `https://marinomassimo-dot.github.io/legend-development/` (host lower-case; today it answers **404**, `has_pages: false`) |
| Must be enabled | Pages with source "GitHub Actions" (step 2). Nothing else. No account, no payment (public repository). |
| Updates | only when someone dispatches the workflow again after regenerating and pushing; no push or schedule trigger. |
| Indexing | meta tag only. A `robots.txt` is deliberately not shipped: crawlers read it at the host root (`https://marinomassimo-dot.github.io/robots.txt`), which a project site cannot control. The tag is a request to well-behaved crawlers, not an access control; anyone with the URL can read the page. |
| Verification after step 3 (about 5 minutes, no login) | the commands of the IT9 request; the `smoke` job performs the first three automatically. |

## 5. What publishing does not change (carried from IT9, unchanged)

The Git history keeps whatever it holds (IT9 reserved decisions 1, 4, 5, 6, 7 stay open); third-party copies cannot be recalled; the page states counts, identifiers,
own text and one licensed ChEMBL class-B file with credit. Not medical advice; reference-genotype level only.

## 6. If you decline or defer

Nothing is lost: the package and the patch stay in the repository, and the roadmap item R10 stays "prepared, awaiting the reserved decision".
