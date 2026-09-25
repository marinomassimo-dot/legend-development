#!/usr/bin/env bash
# git commit-msg hook: the commit subject names the SURFACE touched, never the CONCLUSION reached.
#
# HARNESS-P-20260914 P8. The Claude Code runtime prints recent commit subjects into every fresh
# session's context before the actor can act, which defeats the blinding firewall of a blind
# verification. `scripts/legend_commit.sh` already enforces the rule for every commit made through
# it; this hook extends it to a bare `git commit` in a checkout where the owner installs it.
#
# NOT INSTALLED BY ANY ACTOR. Hooks live in the shared `.git/hooks`, so installing one changes
# the behaviour of every actor on this checkout at once; that is the checkout owner's act.
#
# Install (from the repository root, once per clone; worktrees share the common hooks dir):
#     install -m 0755 deployment/git_commit_msg_subject_hook.sh "$(git rev-parse --git-common-dir)/hooks/commit-msg"
# Uninstall:
#     rm "$(git rev-parse --git-common-dir)/hooks/commit-msg"
# Bypass for one commit, with the reason left visible in the shell history rather than the log:
#     LEGEND_SUBJECT_OVERRIDE="<reason>" git commit ...
#
# Fails open when python3 or the checker is missing: a hook that blocks every commit because a
# tool is absent trains people to delete the hook.
set -u
MESSAGE_FILE="$1"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
CHECKER="$ROOT/framework/scripts/commit_subject.py"
[ -f "$CHECKER" ] && command -v python3 >/dev/null 2>&1 || exit 0
if ! python3 "$CHECKER" check --message-file "$MESSAGE_FILE" >&2; then
  if [ -n "${LEGEND_SUBJECT_OVERRIDE:-}" ]; then
    printf '\nSubject-Check-Override: %s\n' "$LEGEND_SUBJECT_OVERRIDE" >> "$MESSAGE_FILE"
    exit 0
  fi
  echo "commit-msg: the subject must name the surface touched; put the conclusion in the body" >&2
  exit 1
fi
exit 0
