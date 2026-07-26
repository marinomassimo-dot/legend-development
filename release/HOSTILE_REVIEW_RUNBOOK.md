# Hostile review from a clean clone

This runbook is executed only after the content owner reports
`transform-done` and the staging gate has produced its first zero-block result.
It is intentionally separate from content transformation.

## Pass contract

All of the following must be true in the same immutable commit:

1. the complete release regression inventory passes;
2. the public release gate returns `PASS` in a clean clone;
3. the independent privacy scan returns zero blocking findings and every
   informational finding is manually accounted for;
4. every repository-local Markdown link resolves;
5. every concrete README claim about shipped files or runnable commands is
   true in the clone;
6. the clone is clean after all checks.

Any non-zero result is a stop. Do not waive or silently suppress a finding.

## 0. Preconditions

- Work from the candidate repository's committed `HEAD`, not from the mutable
  staging directory.
- Record the candidate commit SHA before review.
- Do not use caches, virtual environments, ignored files, or parent-directory
  assets.
- Do not publish or change repository visibility during this review.

## 1. Create the isolated clone

Set `LEGEND_SOURCE` to the local candidate Git repository or to the private
GitHub URL. The temporary directory is deliberately left in place for audit;
remove it manually only after the review is accepted.

```bash
LEGEND_SOURCE=/absolute/path/to/committed/legend-public
review_root="$(mktemp -d /tmp/legend-hostile-review.XXXXXX)"
clone_dir="$review_root/repo"
git clone --no-local "$LEGEND_SOURCE" "$clone_dir"
cd "$clone_dir"
candidate_sha="$(git rev-parse HEAD)"
printf 'candidate_sha=%s\nclone=%s\n' "$candidate_sha" "$clone_dir"
test -z "$(git status --porcelain)"
```

For a remote private repository, use its SSH URL and verify the resolved
commit equals the approved candidate SHA.

## 2. Gate and regression tests

```bash
python3 -m pip install --requirement requirements-analysis.txt
python3 scripts/run_release_regressions.py
python3 scripts/public_release_gate.py \
  --root . \
  --mode clone \
  --skip-clean-clone \
  --report-json "$review_root/public-release-report.json"
```

Expected: all regression targets pass, exit `0`, `VERDICT: PASS`,
`BLOCKS: 0`.

`--skip-clean-clone` is correct here because this checkout is already the
fresh hostile clone. The release-mode self-clone remains covered by CI.

## 3. Independent privacy scan

```bash
python3 scripts/independent_privacy_scan.py . \
  --json > "$review_root/independent-privacy-report.json"
```

Expected: exit `0`, `blocking_count: 0`, `errors: []`. Informational findings
may remain only when they are synthetic examples or documented lexical
homonyms; record each one in the review note.

The scanner is intentionally independent: it does not import or reuse the
release gate. Review all findings, including apparent examples or common-word
false positives; allowlisting requires a documented reason and a new fixture.

## 4. Link integrity

The regression suite checks Markdown fragment anchors and stable-record
wikilink targets; the public gate independently checks repository-local target
files. Run the focused deep-link contract:

```bash
python3 scripts/test_link_targets.py
```

Then confirm the gate's link result families are absent from the
machine-readable report:

```bash
python3 - "$review_root/public-release-report.json" <<'PY'
import json
import sys

report = json.load(open(sys.argv[1], encoding="utf-8"))
bad = [
    item for item in report["findings"]
    if "LINK" in item["code"] or "WIKILINK" in item["code"]
]
if bad:
    for item in bad:
        print(item)
    raise SystemExit(2)
print("LINK_INTEGRITY: PASS")
PY
```

Then inspect outbound links as citations, not merely as syntactically valid
URLs: source name, destination, licence claim, and cited fact must agree.
Network availability alone is not evidence of correct attribution.

## 5. README ↔ repository hostile check

Read `README.md`, `CLAUDE.md`, `ARCHITECTURE.md`, and `CAPABILITIES.md` as a
skeptical new user with access only to this clone. For every concrete promise,
record one of:

- `SHIPPED`: the referenced path exists in `git ls-files`;
- `RUNNABLE`: the documented command succeeds from the clean clone;
- `DESCRIBED`: the text explicitly says implementation/runtime is not shipped;
- `BLOCK`: the claim overstates what the clone contains or can execute.

Minimum mechanical inventory:

```bash
git ls-files | sort > "$review_root/tracked-files.txt"
test -f README.md
test -f LICENSE
test -f DATA_SOURCES.md
test -f THIRD_PARTY_NOTICES.md
test -f scripts/public_release_gate.py
test -f scripts/independent_privacy_scan.py
python3 scripts/test_phenotypic_neighbors.py
```

Manually challenge at least these claim classes:

- “full framework” versus the actual tracked skills, protocols, evals, and
  scripts;
- “no capability lost” versus capabilities marked only `DESCRIBED`;
- “public literature only” versus every shipped data asset;
- “reproducible” versus missing generation scripts/checkpoints;
- WWOX Foundation relationship and any sponsorship/collaboration wording.

## 6. Clean-state and verdict

```bash
test -z "$(git status --porcelain)"
git rev-parse HEAD
```

Create a signed-off review note outside the repository containing:

- candidate SHA;
- UTC timestamp and reviewer;
- four report outcomes;
- every manual README claim checked;
- unresolved caveats;
- final `PASS` or `BLOCK_PUBLICATION`.

Only an all-green review for the recorded SHA can move to the private
publication staging runbook. Any new commit invalidates the review.
