#!/usr/bin/env python3
"""The EFFECT MODEL — what a command would do, stated in a closed vocabulary.

Revisions 1–7 of the runtime bridge answered one question: *is this command text
allowed?* That question has no answer that survives contact with a shell, because the
same text means different things in different places and because the set of texts that
mean "write" is not enumerable. Revision 7 measured the cost of that: three false
positives against its own author in one session, and — under the probe this module was
written for — **thirty-five of forty-six** repository-mutating shapes allowed.

So the question changes shape. Not

    COMMAND → ALLOW / DENY

but

    COMMAND → PREDICTED EFFECT → TARGET → AUTHORIZATION → EXECUTION
            → OBSERVED EFFECT → MATCH / MISMATCH

This module owns the two ends that are pure: the **vocabulary** an effect is stated in,
and the **algebra** over sets of them. It knows nothing about shells, runtimes, hooks or
git. `guard_policy.py` derives predicted effects; `post_effect_verify.py` derives
observed ones; both state their answer in these terms, and that shared vocabulary is the
only reason the two can be compared at all.

## The two rules that make this fail closed

```
UNKNOWN_EFFECT                          → DENY, under every authority, always
OBSERVED_EFFECT != AUTHORIZED_EFFECT    → FAIL CLOSED, the write result is INVALID
```

Neither has an override, an allowlist or a permissive default, and
`test_effect_model.py` asserts that no authority in `AUTHORITIES` admits
`UNKNOWN_EFFECT` — a check over the table rather than over the six rows someone
remembered to write a case for.

## Why a scope is part of an effect and not a property of the actor

`WRITE` is not a thing an actor may or may not do. `WRITE` *to the scratchpad* and
`WRITE` *to `framework/scripts/`* differ by everything that matters, and an authority
model that grants "write" grants both. So an `Effect` carries its target's **scope**,
and an `Authority` is a pair of sets — which kinds, into which scopes. A kind alone is
never a grant.

🔴 **`UNNAMED` and `UNDERIVABLE` are scopes, not errors.** A command that mutates
something it does not name (`xargs rm`, `find -delete`, an archive extraction) and a
command whose target needs a shell to resolve (`$VAR`, a glob, a substitution) are both
*derivable as mutations* and *underivable as targets*. They are refused by every
authority, including the most permissive, because an effect nobody can name is an effect
nobody can review — and that, not the write itself, is what put another actor's
in-flight work into a commit that described something else.
"""
from __future__ import annotations

import posixpath
from typing import Dict, FrozenSet, Iterable, List, Optional, Sequence, Tuple

# ── the closed effect vocabulary ────────────────────────────────────────────────────
#
# Closed is load-bearing. A derivation that cannot place a command in one of these
# eleven says so by emitting UNKNOWN_EFFECT; it never invents a twelfth and it never
# emits nothing, because "no effect derived" and "no effect" are the same value in an
# open vocabulary and opposite values here.

READ = "READ"
WRITE = "WRITE"
DELETE = "DELETE"
RENAME = "RENAME"
STAGE = "STAGE"
COMMIT = "COMMIT"
REF_MUTATION = "REF_MUTATION"
NETWORK_WRITE = "NETWORK_WRITE"
ARCHIVE_EXTRACT = "ARCHIVE_EXTRACT"
PERMISSION_CHANGE = "PERMISSION_CHANGE"
#: 🔴 Handing the work to ANOTHER agent runtime — `codex exec`, `claude -p`, a companion
#: invocation. Its own effects happen in a process this guard never sees, so the only
#: honest derivation is "an unbounded effect set behind a name", and the only honest
#: authorisation is none. It is a kind of its own rather than UNKNOWN_EFFECT because the
#: two need different repairs: an unknown effect wants the derivation taught, a delegation
#: wants the DELEGATE's own write floor demonstrated before the handoff can be allowed.
DELEGATE = "DELEGATE"
UNKNOWN_EFFECT = "UNKNOWN_EFFECT"

KINDS: FrozenSet[str] = frozenset({
    READ, WRITE, DELETE, RENAME, STAGE, COMMIT, REF_MUTATION,
    NETWORK_WRITE, ARCHIVE_EXTRACT, PERMISSION_CHANGE, DELEGATE, UNKNOWN_EFFECT,
})

#: Every kind but READ changes state somewhere. UNKNOWN_EFFECT is in here deliberately:
#: an effect we could not derive is treated as a mutation, never as a read.
MUTATING: FrozenSet[str] = frozenset(KINDS - {READ})

# ── target scopes ───────────────────────────────────────────────────────────────────

#: The ASSIGNED worktree — the one this actor was given. The name is kept from revision
#: 8 because every rule, suite and receipt already speaks it; what changed in revision 9
#: is that it no longer means "the repository", which is now three further scopes wide.
INSIDE_REPO = "INSIDE_REPO"
#: Outside this repository altogether, and not scratch.
OUTSIDE_REPO = "OUTSIDE_REPO"
SCRATCH = "SCRATCH"

#: 🔴 The three subdivisions revision 8 collapsed into OUTSIDE_REPO, where SHELL_DEFAULT
#: grants content writes. Measured on 2026-08-29: from an actor worktree, rewriting a
#: peer's sources, deleting a peer's directories, rewriting the shared checkout's
#: `CLAUDE.md`, and writing `.git/config`, `.git/hooks/pre-commit`, `.git/refs/heads/main`
#: and `.git/worktrees/*/HEAD` were ALL allowed. They are separate scopes rather than one
#: because they are separate authority surfaces: a governed operation might one day be
#: granted the shared checkout without ever being granted the common dir.
PEER_WORKTREE = "PEER_WORKTREE"
SHARED_CHECKOUT = "SHARED_CHECKOUT"
GIT_COMMON_DIR = "GIT_COMMON_DIR"

#: 🔴 The files that decide whether this guard runs at all — revision 10.
#:
#: Measured on 2026-08-29 against the revision-9 engine, at ordinary `SHELL_DEFAULT`:
#: `echo x > <HOME>/.claude/settings.json`, `echo x > <CODEX_HOME>/config.toml` and
#: `rm -rf <CODEX_HOME>` were all ALLOWED. Those files are where a runtime is told which
#: hook to run, and `settings.json` additionally carries the `env` block that supplies
#: `session_binding`'s operator row. So an actor governed by this policy could rewrite
#: the registration that makes the policy govern it, and the write floor would report
#: itself intact right up until the next process start.
#:
#: This is NOT `~/.claude` and NOT `~/.codex`. It is the RESOLVED ACTIVE control surface
#: — the settings file a runtime is actually reading and the registered engine it names
#: — because a scope that swallowed a runtime's caches and scratch would refuse ordinary
#: work, and a guard that refuses ordinary work is a guard that gets turned off.
#: `runtime_config.py` resolves the membership and says when it cannot.
RUNTIME_CONFIG = "RUNTIME_CONFIG"

#: The command performs the effect but does not name what it acts on.
UNNAMED = "UNNAMED"
#: The command names a target that cannot be resolved without running it.
UNDERIVABLE = "UNDERIVABLE"
#: The target is not on this machine — a remote ref, a URL, a `host:path`.
NONLOCAL = "NONLOCAL"

SCOPES: FrozenSet[str] = frozenset({
    INSIDE_REPO, OUTSIDE_REPO, SCRATCH, PEER_WORKTREE, SHARED_CHECKOUT,
    GIT_COMMON_DIR, RUNTIME_CONFIG, UNNAMED, UNDERIVABLE, NONLOCAL,
})

#: 🔴 The scopes a shared object store makes this guard responsible for, beyond the
#: worktree it runs in. `test_effect_model.py` asserts that NO authority grants ANY
#: mutating kind in any of them, which is the property that survives someone adding a
#: seventh authority class without reading this comment.
CONFINED: FrozenSet[str] = frozenset({PEER_WORKTREE, SHARED_CHECKOUT, GIT_COMMON_DIR})

#: 🔴 Every scope no authority class grants a MUTATION in, which is `CONFINED` plus the
#: runtime control surface. Kept as a set of its own rather than folded into `CONFINED`
#: because the two are refused for different reasons and say different sentences: a peer
#: worktree is somebody else's work, and the runtime config is this guard's own switch.
#: `test_effect_model.py` quantifies over THIS set, so a scope added here inherits the
#: property and a scope added to neither fails the suite rather than defaulting to
#: grantable.
UNGRANTED: FrozenSet[str] = CONFINED | frozenset({RUNTIME_CONFIG})

#: 🔴 The (kind, scope) pairs that ARE granted inside an UNGRANTED scope — exactly one, and
#: named here so that a second one has to be added deliberately. `(COMMIT, SHARED_CHECKOUT)`
#: is the landing merge of `DEC-20260905-AGILE-HARNESS-MODE` (LEGEND_CORE §21e): a worktree
#: session runs `git -C <root> merge <its-branch>` to land finished work on `main`. The
#: suite quantifies over `MUTATING × UNGRANTED` minus this set.
UNGRANTED_EXCEPTIONS: FrozenSet[Tuple[str, str]] = frozenset({(COMMIT, SHARED_CHECKOUT)})

#: Scopes in which a mutating effect can be reviewed, because a reader of the command
#: can say what it touched. The complement is refused by every authority.
#:
#: The confined scopes ARE nameable — a reader can see exactly which peer file is meant —
#: so they belong here. What stops them is that no authority grants them, which is a
#: different sentence and produces a different denial: "granted by no authority class"
#: rather than "a mutation whose target is UNNAMED". Putting them in the unnameable set
#: instead would have been one line shorter and would have told the reader the guard
#: could not see the path, which is false and unactionable.
NAMEABLE: FrozenSet[str] = frozenset({
    INSIDE_REPO, OUTSIDE_REPO, SCRATCH, NONLOCAL,
    PEER_WORKTREE, SHARED_CHECKOUT, GIT_COMMON_DIR, RUNTIME_CONFIG,
})


class Effect:
    """One derived or observed effect: what kind, on what, decided how.

    `target` is a path, a ref name, a URL or `None` when the effect has no target the
    command names. It is stored verbatim and normalised only at comparison time, so a
    receipt records what was actually written rather than this module's opinion of it.
    """

    __slots__ = ("kind", "target", "scope", "primitive", "detail")

    def __init__(self, kind: str, target: Optional[str], scope: str,
                 primitive: str = "", detail: str = "") -> None:
        if kind not in KINDS:
            raise ValueError(f"{kind!r} is not an effect kind; the vocabulary is closed")
        if scope not in SCOPES:
            raise ValueError(f"{scope!r} is not a target scope; the vocabulary is closed")
        self.kind = kind
        self.target = target
        self.scope = scope
        self.primitive = primitive
        self.detail = detail

    # Two effects are the same effect when they are the same kind on the same target.
    # The primitive and the detail are provenance: `cp` and `tee` writing one path are
    # one effect observed once, and a comparison that split them would report a
    # mismatch for a difference the filesystem cannot express.
    def key(self, repo_root: Optional[str] = None) -> Tuple[str, str]:
        return (self.kind, normalise_target(self.target, repo_root))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Effect):
            return NotImplemented
        return self.key() == other.key() and self.scope == other.scope

    def __hash__(self) -> int:
        return hash((self.key(), self.scope))

    def __repr__(self) -> str:  # pragma: no cover - diagnostics only
        return f"Effect({self.kind}, {self.target!r}, {self.scope})"

    def as_dict(self) -> Dict[str, object]:
        return {
            "kind": self.kind,
            "target": self.target,
            "scope": self.scope,
            "primitive": self.primitive,
            "detail": self.detail,
        }

    @classmethod
    def from_dict(cls, raw: object) -> "Effect":
        """Rebuild an effect from a receipt. A malformed record raises, never defaults.

        🔴 This is a fail-closed boundary and not a convenience. An `Effect.from_dict`
        that filled in a missing `kind` with `READ`, or a missing `scope` with
        `SCRATCH`, would let a truncated receipt validate as a harmless one.
        """
        if not isinstance(raw, dict):
            raise ValueError("an effect record must be an object")
        for field in ("kind", "scope"):
            if not isinstance(raw.get(field), str):
                raise ValueError(f"an effect record must carry a string `{field}`")
        target = raw.get("target")
        if target is not None and not isinstance(target, str):
            raise ValueError("`target` must be a string or null")
        return cls(
            raw["kind"], target, raw["scope"],
            str(raw.get("primitive", "")), str(raw.get("detail", "")),
        )


def normalise_target(target: Optional[str], repo_root: Optional[str] = None) -> str:
    """Reduce a target to the form two derivations can be compared in.

    A predicted effect comes out of command text (`./framework/x`, `framework//x`); an
    observed one comes out of `git status` (`framework/x`). They must reduce to one
    string or every comparison reports a mismatch that is really a spelling difference.
    """
    if target is None:
        return ""
    text = target.strip()
    if not text:
        return ""
    if "://" in text or (":" in text and "/" not in text.split(":", 1)[0]):
        return text  # a URL or a `host:path` — not a filesystem path, do not touch it
    if repo_root and text.startswith(repo_root.rstrip("/") + "/"):
        text = text[len(repo_root.rstrip("/")) + 1:]
    text = posixpath.normpath(text)
    return text[2:] if text.startswith("./") else text


# ── authority classes ───────────────────────────────────────────────────────────────

class Authority:
    """A mapping from effect kind to the scopes that kind is granted in.

    🔴 **A pair of sets is the wrong shape and the first draft of this file used one.**
    `kinds × scopes` cannot express the grant the shell guard actually needs — *stage a
    named path inside the repository, but do not write content into it* — because
    `STAGE` and `WRITE` both land at `INSIDE_REPO`, and any product that admits the
    first admits the second. A guard built on that product either loses `git commit`,
    which is how every commit in this repository is made, or regains the shell write
    that revisions 1–7 exist to stop. Per-kind scopes cost one dictionary and are the
    only shape in which the two are different sentences.

    An authority is never consulted for *who* an actor is — that is
    `execution_attestation.py`'s question, and keeping the two apart is the whole of
    `ACTOR_ID != RUNTIME != SESSION != WORKTREE != AUTHORITY`. This class answers only
    "given that an actor holds authority X, is this effect within it?".
    """

    __slots__ = ("name", "grants", "rationale")

    def __init__(self, name: str, grants: Dict[str, Iterable[str]],
                 rationale: str = "") -> None:
        self.name = name
        self.grants: Dict[str, FrozenSet[str]] = {
            kind: frozenset(scopes) for kind, scopes in grants.items()
        }
        self.rationale = rationale
        unknown = (set(self.grants) - KINDS) | {
            s for scopes in self.grants.values() for s in scopes if s not in SCOPES
        }
        if unknown:
            raise ValueError(f"{name} names terms outside the vocabulary: {sorted(unknown)}")

    @property
    def kinds(self) -> FrozenSet[str]:
        """The kinds granted in at least one scope. A kind granted nowhere is not one."""
        return frozenset(k for k, scopes in self.grants.items() if scopes)

    def permits(self, kind: str, scope: str) -> bool:
        return scope in self.grants.get(kind, frozenset())

    def __repr__(self) -> str:  # pragma: no cover - diagnostics only
        return f"Authority({self.name})"


#: 🔴 READ is granted everywhere INCLUDING the confined scopes, and that is deliberate.
#: Reading a peer's branch is how Mirror reviews, reading `.git/config` is how the
#: topology is derived, and reading the shared checkout is how anyone learns what `main`
#: says. The confinement is about MUTATION; a read confinement would break the review
#: function this laboratory runs on, and would be the kind of rule that gets turned off.
_EVERYWHERE = {INSIDE_REPO, OUTSIDE_REPO, SCRATCH, NONLOCAL} | set(UNGRANTED)
_CONTENT = (WRITE, DELETE, RENAME, ARCHIVE_EXTRACT)


def _ladder(*layers: Dict[str, Iterable[str]]) -> Dict[str, FrozenSet[str]]:
    """Accumulate grants so each authority is a superset of the one below it.

    The ladder is not decoration. `test_effect_model.py::TheAuthorityLadderIsMonotone`
    asserts it, which turns "a higher authority may do strictly more" from a convention
    into a property — and it is the reason a denial can always name the lowest
    authority that would have permitted the effect.
    """
    merged: Dict[str, FrozenSet[str]] = {}
    for layer in layers:
        for kind, scopes in layer.items():
            merged[kind] = merged.get(kind, frozenset()) | frozenset(scopes)
    return merged


_L1 = {READ: _EVERYWHERE}
# 🔴 PERMISSION_CHANGE belongs on THIS rung outside the repository, not on REF_WRITE.
# The boundary this policy defends is the repository, and it has to be the same boundary
# for every effect kind: a `chmod 755 /tmp/probe.sh` is no more this guard's business
# than an `echo x > /tmp/probe.txt`. Putting the whole kind on the REF_WRITE rung made
# the scratch case refused, which the negative controls caught in the same run that
# added them — a guard that blocks ordinary work gets turned off, and this was ordinary.
_L2 = {kind: {SCRATCH, OUTSIDE_REPO} for kind in _CONTENT}
_L2[PERMISSION_CHANGE] = {SCRATCH, OUTSIDE_REPO}
# 🔴 COMMIT is granted on the SHARED checkout as well — the one carve-out from the
# confinement asserted below, made by the operator on 2026-09-05
# (DEC-20260905-AGILE-HARNESS-MODE, LEGEND_CORE §21e): a worktree session lands its
# finished branch on `main` with `git -C <root> merge <branch>`, which is a COMMIT whose
# HEAD is the root's. Nothing else crosses: STAGE, WRITE, DELETE, RENAME and REF_MUTATION
# at SHARED_CHECKOUT stay ungranted, so a worktree session still cannot stage, edit or
# reset the root's working tree. `UNGRANTED_EXCEPTIONS` names the pair; the suite
# quantifies over everything else.
_L3 = {STAGE: {INSIDE_REPO}, COMMIT: {INSIDE_REPO, SHARED_CHECKOUT}}
_L4 = {kind: {INSIDE_REPO} for kind in _CONTENT}
_L5 = {REF_MUTATION: {INSIDE_REPO}, PERMISSION_CHANGE: {INSIDE_REPO}}
_L6 = {NETWORK_WRITE: {NONLOCAL}, REF_MUTATION: {NONLOCAL}}

#: 🔴 No authority in this table grants UNKNOWN_EFFECT or DELEGATE, none grants any kind
#: at UNNAMED or UNDERIVABLE scope, and none grants any MUTATING kind at any scope in
#: `UNGRANTED` — PEER_WORKTREE, SHARED_CHECKOUT, GIT_COMMON_DIR and, from revision 10,
#: RUNTIME_CONFIG — with exactly the pairs in `UNGRANTED_EXCEPTIONS` excepted (one pair,
#: `(COMMIT, SHARED_CHECKOUT)`, the landing merge of 2026-09-05). All of it is asserted
#: over the table by `test_effect_model.py` rather than trusted to review: a seventh
#: authority added later inherits the properties or fails the suite.
#:
#: DELEGATE and the confined scopes are absent by OMISSION, not by an exclusion rule,
#: and that is worth naming because the two fail differently. An exclusion checked
#: before the grants — as UNKNOWN_EFFECT is — cannot be undone by adding a grant. An
#: omission can: someone writes `_L7 = {DELEGATE: ...}` and the confinement is gone with
#: no error anywhere. The suite is what closes that, which is why it asserts the
#: property over `AUTHORITIES` itself rather than over a list of expected denials.
AUTHORITIES: Dict[str, Authority] = {
    "READ_ONLY": Authority(
        "READ_ONLY", _ladder(_L1),
        "The floor, and where an unattested session sits. A Codex actor stays here "
        "while HOOK_DEMONSTRATED is false.",
    ),
    "SCRATCH_WRITE": Authority(
        "SCRATCH_WRITE", _ladder(_L1, _L2),
        "Working space. The scratchpad and /tmp are not what went wrong.",
    ),
    "SHELL_DEFAULT": Authority(
        "SHELL_DEFAULT", _ladder(_L1, _L2, _L3),
        "🔴 What the PreToolUse guard enforces, and the reason it is a rung of its own: "
        "an actor may stage paths it NAMES and may commit, because that is how work "
        "lands here, but may not write repository content from the shell — that goes "
        "through Write/Edit, whose read-before-overwrite rule is the point.",
    ),
    "WORKTREE_WRITE": Authority(
        "WORKTREE_WRITE", _ladder(_L1, _L2, _L3, _L4),
        "Content mutation inside one worktree, granted to a committed script invoked "
        "by name — never to an ad-hoc shell command.",
    ),
    "REF_WRITE": Authority(
        "REF_WRITE", _ladder(_L1, _L2, _L3, _L4, _L5),
        "Local history rewriting: reset --hard, checkout --, clean, branch -D, chmod. "
        "Local only — REF_MUTATION at NONLOCAL scope is a push and is one rung up.",
    ),
    "PUBLISH": Authority(
        "PUBLISH", _ladder(_L1, _L2, _L3, _L4, _L5, _L6),
        "🔴 Sends bytes off the machine. `development` and `origin` are both PUBLIC "
        "repositories, so a push is a publication and is an operator act. This "
        "authority is never granted by a runtime, a role or a lease.",
    ),
}

#: The ladder, weakest first. Used to name the lowest authority that would permit a
#: denied effect, so a denial says what would be needed rather than only saying no.
LADDER: Tuple[str, ...] = (
    "READ_ONLY", "SCRATCH_WRITE", "SHELL_DEFAULT", "WORKTREE_WRITE", "REF_WRITE", "PUBLISH",
)

#: The authority an actor holds when none has been established. Not a default: a floor.
UNATTESTED = "READ_ONLY"

AUTHORIZED = "AUTHORIZED"
DENIED = "DENIED"


class Decision:
    """The result of authorising a predicted effect set."""

    __slots__ = ("verdict", "authority", "denials", "effects")

    def __init__(self, verdict: str, authority: str,
                 denials: Sequence[Tuple["Effect", str]], effects: Sequence["Effect"]) -> None:
        self.verdict = verdict
        self.authority = authority
        self.denials = list(denials)
        self.effects = list(effects)

    @property
    def authorized(self) -> bool:
        return self.verdict == AUTHORIZED

    @property
    def authorized_effects(self) -> List["Effect"]:
        """The effects a successful execution is permitted to produce, and no others."""
        return [] if not self.authorized else list(self.effects)

    def reason(self) -> str:
        if self.authorized:
            return ""
        lines = [f"Refused under authority {self.authority}. "
                 f"{len(self.denials)} effect(s) fall outside it:", ""]
        for effect, why in self.denials:
            where = effect.target if effect.target else "<not named>"
            lines.append(f"  {effect.kind:<18} {where:<44} {why}")
        return "\n".join(lines)


def authorize(effects: Sequence[Effect], authority: str) -> Decision:
    """Is every predicted effect within this authority?

    The three refusals below are checked **before** the authority's own sets, so an
    authority cannot admit them by listing more kinds. That ordering is the fail-closed
    property; reversing it would make `PUBLISH` a way to authorise an unknown effect.
    """
    if authority not in AUTHORITIES:
        # An authority nobody can resolve is not a weaker authority, it is none.
        return Decision(DENIED, str(authority),
                        [(Effect(UNKNOWN_EFFECT, None, UNNAMED, "authority"),
                          f"{authority!r} is not a known authority class")], effects)

    grant = AUTHORITIES[authority]
    denials: List[Tuple[Effect, str]] = []
    for effect in effects:
        if effect.kind == UNKNOWN_EFFECT:
            denials.append((effect, "the effect could not be derived at all"))
            continue
        if effect.kind in MUTATING and effect.scope not in NAMEABLE:
            denials.append((effect, f"a mutation whose target is {effect.scope}"))
            continue
        if not grant.permits(effect.kind, effect.scope):
            denials.append((effect, _shortfall(effect, authority)))
    return Decision(AUTHORIZED if not denials else DENIED, authority, denials, effects)


def lowest_authority_for(kind: str, scope: str) -> Optional[str]:
    """The weakest rung that permits this effect, or None when no rung does."""
    for name in LADDER:
        if AUTHORITIES[name].permits(kind, scope):
            return name
    return None


def _shortfall(effect: Effect, authority: str) -> str:
    """Say what is missing, and name the rung that would have it. A denial that only
    says no teaches the reader to route around it; one that names the authority it
    would need turns the refusal into a question for the operator."""
    needed = lowest_authority_for(effect.kind, effect.scope)
    if needed is None:
        return f"{effect.kind} at {effect.scope} is granted by no authority class"
    return f"{effect.kind} at {effect.scope} needs {needed}; this actor holds {authority}"


# ── observed vs authorised ──────────────────────────────────────────────────────────

MATCH = "MATCH"
MISMATCH = "MISMATCH"


class Comparison:
    """The verdict of a post-effect check: did execution do exactly what was authorised?"""

    __slots__ = ("verdict", "matched", "extra", "missing")

    def __init__(self, verdict: str, matched: Sequence[Effect],
                 extra: Sequence[Effect], missing: Sequence[Effect]) -> None:
        self.verdict = verdict
        self.matched = list(matched)
        self.extra = list(extra)
        self.missing = list(missing)

    @property
    def valid(self) -> bool:
        return self.verdict == MATCH

    def reason(self) -> str:
        if self.valid:
            return ""
        lines = ["The observed effect set is not the authorised effect set, so the "
                 "write result is INVALID.", ""]
        for effect in self.extra:
            lines.append(f"  EXTRA    {effect.kind:<18} {effect.target or '<unnamed>'}")
        for effect in self.missing:
            lines.append(f"  MISSING  {effect.kind:<18} {effect.target or '<unnamed>'}")
        return "\n".join(lines)


def compare(authorized: Sequence[Effect], observed: Sequence[Effect],
            repo_root: Optional[str] = None) -> Comparison:
    """Set equality over (kind, normalised target). Extra *or* missing is a failure.

    🔴 **Missing is a failure, and that is a deliberate over-strictness.** `rm -f` on a
    path that does not exist produces no observed DELETE, and this call reports
    MISMATCH for it. The alternative — treating a missing effect as benign — makes the
    check unable to distinguish "the write did not happen" from "the write happened
    somewhere this instrument cannot see", and those are the two readings that matter.
    A caller that wants the looser rule asks for it in the open, by not authorising the
    effect it does not expect.
    """
    want = {}
    for effect in authorized:
        want.setdefault(effect.key(repo_root), effect)
    have = {}
    for effect in observed:
        have.setdefault(effect.key(repo_root), effect)

    matched = [have[k] for k in want if k in have]
    extra = [have[k] for k in have if k not in want]
    missing = [want[k] for k in want if k not in have]
    verdict = MATCH if not extra and not missing else MISMATCH
    return Comparison(verdict, matched, extra, missing)


def describe_table() -> str:
    """The authority table, printed. Used by `runtime_parity.py --authorities`.

    One row per (authority, kind), because a kind granted in two scopes and a kind
    granted in one are the difference the flat table used to hide.
    """
    order = [READ, WRITE, DELETE, RENAME, ARCHIVE_EXTRACT, STAGE, COMMIT,
             REF_MUTATION, PERMISSION_CHANGE, NETWORK_WRITE, UNKNOWN_EFFECT]
    width = max(len(k) for k in order)
    rows = [f"{'AUTHORITY':<16} {'EFFECT':<{width}}  SCOPES GRANTED"]
    for name in LADDER:
        grant = AUTHORITIES[name]
        for kind in order:
            scopes = grant.grants.get(kind, frozenset())
            rows.append(f"{name:<16} {kind:<{width}}  "
                        f"{','.join(sorted(scopes)) if scopes else '—'}")
        rows.append("")
    return "\n".join(rows).rstrip()


if __name__ == "__main__":  # pragma: no cover - diagnostics only
    print(describe_table())
