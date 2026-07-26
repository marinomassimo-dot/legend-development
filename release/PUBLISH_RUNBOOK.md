# Publication runbook — staged only

**DO NOT EXECUTE without the repository owner's explicit authorization.**
Creating a remote, pushing, inviting a collaborator, or changing visibility
are separate external mutations and each requires a named target and approval.

## Required decisions before any command

- Confirm the final GitHub owner and repository name.
- Confirm the exact GitHub login for the intended Foundation reviewer; do not
  infer it from a display name or email.
- Confirm who legally owns the repository-authored material.
- Resolve the current `LICENSE` attribution: it says
  `LEGEND project / WWOX Foundation`, and `SPONSORSHIP.md` asserts formal
  sponsorship. Independently verify the written confirmation and that the
  Foundation authorised both the public wording and the copyright/licensing
  attribution; otherwise use an ownership line the actual rights holder can
  grant.
- Obtain a hostile-review `PASS` tied to the exact candidate commit SHA.

## 1. Local preflight

Run read-only checks first:

```bash
cd /absolute/path/to/legend-public
git status --short --branch
git ls-files | sort
git check-ignore -v \
  _qa/example files/example backup/example staging/example tmp/example \
  overlay/example patient.txt proband.txt .env
python3 scripts/run_release_regressions.py
python3 scripts/public_release_gate.py \
  --root . --mode release \
  --report-json /tmp/legend-public-release-report.json
python3 scripts/independent_privacy_scan.py .
```

Stop unless the worktree is clean, the candidate SHA matches the hostile
review, both scanners return zero blocking findings, every informational
finding is documented, and all regression tests pass.

Review `.gitignore` against the complete tracked set, not only filenames:

```bash
git ls-files | rg -i \
  '(^|/)(files|_qa|backup|staging|tmp|overlay)(/|$)|private|patient|proband|\.env'
git ls-files -z | xargs -0 file
```

Any tracked forbidden path, unexpected archive, database, executable, PDF,
notebook output, cache, or binary blob is a stop pending manual review.

## 2. Licence and notices preflight

Verify all four layers:

1. repository-authored code/text licence and true copyright holder;
2. `DATA_SOURCES.md` coverage for every shipped derivative;
3. `THIRD_PARTY_NOTICES.md` attribution and licence compatibility;
4. unresolved run lineage: ClinVar date, GTEx access date, ESM-2 checkpoint,
   ThermoMPNN commit/checkpoint, and generation scripts.

“Publicly accessible” is not synonymous with “freely redistributable”.
Unresolved ownership or incompatible terms block publication.

## 3. Create a private GitHub repository — authorization hold

The following is a staged command template only:

```bash
OWNER=<approved-owner>
REPO=<approved-repository-name>
gh repo create "$OWNER/$REPO" \
  --private \
  --source=. \
  --remote=origin \
  --push
gh repo view "$OWNER/$REPO" --json nameWithOwner,visibility,url
```

Expected visibility is exactly `PRIVATE`. If it is not, stop immediately.
Do not add topics, releases, packages, Pages, Actions secrets, or public forks.

## 4. Invite the Foundation reviewer — separate authorization hold

After the repository owner confirms the exact GitHub login and permission:

```bash
OWNER=<approved-owner>
REPO=<approved-repository-name>
COLLABORATOR_LOGIN=<verified-github-login>
gh api \
  --method PUT \
  "repos/$OWNER/$REPO/collaborators/$COLLABORATOR_LOGIN" \
  -f permission=pull
```

Use least privilege (`pull`) unless the repository owner explicitly approves a
broader role. Verify the invitation and repository visibility without
disclosing the invitee's email or other personal data in repository files.

## 5. Private-review loop

- Push only reviewed commits.
- Require CI `Public release gate` to pass.
- Re-run the hostile review from a fresh clone of the private remote.
- Any fix creates a new SHA and invalidates the prior sign-off.
- Keep all review reports outside the repository if they contain residual
  strings or sensitive context.

## 6. Make public — final authorization hold

Changing visibility is irreversible in practical exposure terms even if later
reverted. Do it only after the repository owner explicitly approves the exact
`OWNER/REPO@SHA` and the private-review loop is green.

Staged command template:

```bash
OWNER=<approved-owner>
REPO=<approved-repository-name>
gh repo edit "$OWNER/$REPO" \
  --visibility public \
  --accept-visibility-change-consequences
gh repo view "$OWNER/$REPO" --json nameWithOwner,visibility,url
```

After publication, verify the public clone and CI once more. Never rewrite
history to “remove” an exposed secret or identifier as the only response:
rotate/revoke the secret, assess exposure, remove the data, and follow the
appropriate incident process.
