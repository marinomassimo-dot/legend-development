#!/usr/bin/env python3
"""The verdict contract every screen in ``framework/scripts/`` returns.

🔴 WHY THIS EXISTS, and both halves were measured on 2026-09-09, not imagined.

Two of that sweep's most severe near-errors are the same defect at two altitudes.

1. **A screen returned CLEAN on a surface nobody screened.** A reader called
   ``_refuse_suspect_surface(text, path_string)`` — the arguments inverted. The function
   returned normally, because the loop screened the *filename*, which holds no control
   characters. The surface actually in question, the PMID 16223882 PDF text layer, carries
   **191 C0 controls and zero comparators**; the correct call refuses it. The reader's own
   words: *"my check asserted nothing and I reported it as though it had."* Nothing in the
   repository would have caught it.

2. **A screen returned REFUSED for the wrong reason.** A refusal fired on 8 harmless
   front-matter separators while the actual genotype corruption matched no signature at all.
   It was one step from being accepted as a verdict about the corruption.

Both are invisible to a screen that returns a **boolean**. ``True`` cannot say what it looked
at, and ``False`` cannot say what fired. A boolean is a claim with its evidence deleted, and
the caller then has a green result to point at — which is worse than no screen, because it
wears the badge of having been checked.

So a verdict here is a **record**, and the record carries the digest of *exactly the bytes
that were screened*. Two callers holding the same verdict can now answer, mechanically, the
question neither could answer before: *did this screen look at the surface I am asking about?*
Compare ``verdict.screened["digest"]`` against the digest of your own bytes. If they differ,
the verdict is about a different document, whatever colour it is.

THE ONE GUARANTEE THIS MODULE ENFORCES, rather than recommends
--------------------------------------------------------------

    A ``CLEAN`` verdict cannot be constructed without a digest.

Not discouraged: **unrepresentable**. ``ScreenVerdict(verdict="CLEAN", screened=None)`` raises
``ScreenContractError``, as does a digest over zero bytes. This is deliberate and is the whole
design: a guard an actor can forget is the control that already failed. The 2026-09-09
inversion happened to a careful reader who had read the rule that same session, and the
repository's response at the time — an argument-shape guard — closes the inversion case only.
This closes the class: there is no code path, correct or inverted, that yields a CLEAN verdict
about bytes that were never hashed.

THE VOCABULARY
--------------

``CLEAN``
    This signature was looked for, over these exact bytes, and was not found. It is **never**
    a claim that the surface is faithful — only that this screen's signature is absent. Every
    screen's ``detail`` should keep saying so.

``REFUSED``
    A signature fired, and the verdict **names which one**. ``signature`` is mandatory. A
    refusal that cannot name its signature is the B16 defect: a verdict the caller accepts
    without asking what it refused for. ``evidence`` carries the located instances.

``INSUFFICIENT_DATA``
    The screen could not run, and the verdict **names the missing input**. ``missing`` is
    mandatory. A zero-length input, an absent file, or a path handed where content was
    expected are all ``INSUFFICIENT_DATA`` — **never** a pass. This was already
    ``genre_discriminator.py``'s design rule; here it is the repository-wide convention.

HOW TO USE IT — the whole of the API a screen needs
---------------------------------------------------

::

    from screen_verdict import ScreenVerdict, screened_of, ScreenContractError

    def screen_surface(path: Path) -> ScreenVerdict:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            return ScreenVerdict.insufficient(
                "my_screen", missing=f"artifact {path}", detail=str(exc))

        # Refuses a path handed where content belongs, and zero-length content, by
        # returning INSUFFICIENT_DATA rather than a verdict about nothing.
        bad = ScreenVerdict.reject_uninformative("my_screen", text, expected="the surface text")
        if bad is not None:
            return bad

        hits = SIGNATURE.findall(text)
        if hits:
            return ScreenVerdict.refused(
                "my_screen", text, signature="C0_CONTROL",
                detail=f"{len(hits)} control characters",
                evidence={"instances": hits[:20], "count": len(hits)})
        return ScreenVerdict.clean(
            "my_screen", text,
            detail="no C0 controls; not proof the surface is faithful")

``screened_of(data)`` alone returns the ``{"digest": "sha256:…", "bytes": n}`` mapping if you
are assembling a record by hand. ``str`` is encoded as UTF-8 before hashing, so the digest of
a text surface is the digest of its UTF-8 bytes and is reproducible from the shell with
``python3 -c 'import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest())'``
when the file is UTF-8 on disk.

``.as_dict()`` is the JSON form; ``.from_dict()`` round-trips it and re-applies every guard,
so a CLEAN verdict cannot be smuggled past the contract by writing JSON either. ``.render()``
is the one-line human form.

WHAT THIS MODULE DOES NOT DO. It does not screen anything and knows no signatures — it is the
shape of an answer, not an answer. It does not decide exit codes: a caller maps verdicts to
process status, and the mapping differs (a review-surface tool exits 0 on REFUSED; a gate does
not). And it does not make a screen correct. It makes a screen **accountable**: whatever it
concluded, it has to say what it read to conclude it.
"""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass, field
from typing import Any, Mapping

CLEAN = "CLEAN"
REFUSED = "REFUSED"
INSUFFICIENT_DATA = "INSUFFICIENT_DATA"

VERDICTS = (CLEAN, REFUSED, INSUFFICIENT_DATA)

# The prefix is carried in the value rather than assumed by the reader, so a later change of
# hash is visible in every stored record instead of silently comparing unequal things.
DIGEST_ALGORITHM = "sha256"


class ScreenContractError(TypeError):
    """A verdict was constructed that would assert more than it screened.

    ``TypeError`` and not ``ValueError`` on purpose: this is a defect in the *calling code's
    shape*, the same class as the inverted-argument call that motivated the module, and it is
    never something a caller should catch and continue past.
    """


def _digest_bytes(raw: bytes) -> str:
    return f"{DIGEST_ALGORITHM}:{hashlib.sha256(raw).hexdigest()}"


def as_bytes(data: Any) -> bytes:
    """Coerce screened content to the exact bytes that will be hashed.

    ``str`` is UTF-8 encoded; ``bytes``/``bytearray``/``memoryview`` pass through. Anything
    else — a ``Path``, an open file, a parsed dict — raises, because the digest must be over
    the bytes the screen actually inspected and nothing else. Hashing ``str(path)`` here is
    precisely how a screen ends up certifying a filename.
    """
    if isinstance(data, str):
        return data.encode("utf-8")
    if isinstance(data, (bytes, bytearray, memoryview)):
        return bytes(data)
    if isinstance(data, os.PathLike):
        raise ScreenContractError(
            "screened content must be the bytes or text that were inspected, not a path "
            f"({data!r}). Read the file and screen its content; a digest over a path name "
            "certifies the file name, which always passes and asserts nothing")
    raise ScreenContractError(
        f"screened content must be str or bytes, not {type(data).__name__}")


def screened_of(data: Any) -> dict[str, Any]:
    """Return ``{"digest": "sha256:…", "bytes": n}`` over exactly ``data``.

    Zero-length input is allowed *here* — it is the verdict constructors that refuse to call
    it CLEAN — so that a screen may still record, on an ``INSUFFICIENT_DATA`` verdict, that
    what it received was empty rather than absent. Those are different repairs.
    """
    raw = as_bytes(data)
    return {"digest": _digest_bytes(raw), "bytes": len(raw)}


def _validate_screened(screened: Any) -> dict[str, Any] | None:
    if screened is None:
        return None
    if not isinstance(screened, Mapping):
        raise ScreenContractError(
            f"screened must be a mapping with 'digest' and 'bytes', not {type(screened).__name__}")
    digest = screened.get("digest")
    size = screened.get("bytes")
    if not isinstance(digest, str) or ":" not in digest or len(digest.split(":", 1)[1]) != 64:
        raise ScreenContractError(
            f"screened['digest'] must be '<algorithm>:<64 hex>', got {digest!r}")
    if not isinstance(size, int) or isinstance(size, bool) or size < 0:
        raise ScreenContractError(
            f"screened['bytes'] must be a non-negative int, got {size!r}")
    return {"digest": digest, "bytes": size}


@dataclass(frozen=True)
class ScreenVerdict:
    """What a screen returns. Immutable, JSON-serialisable, and self-describing.

    Attributes
    ----------
    screen
        The screen's name — the tool or function that reached this verdict. Required, because
        a verdict travelling between tools without one is a verdict nobody can attribute.
    verdict
        One of ``CLEAN``, ``REFUSED``, ``INSUFFICIENT_DATA``.
    screened
        ``{"digest": "sha256:…", "bytes": n}`` over exactly the inspected bytes. Mandatory for
        ``CLEAN`` and ``REFUSED``; optional for ``INSUFFICIENT_DATA``, where there may be
        nothing to hash.
    signature
        Mandatory on ``REFUSED``: which signature fired. Forbidden otherwise.
    missing
        Mandatory on ``INSUFFICIENT_DATA``: what input was missing. Forbidden otherwise.
    detail
        Human sentence. On ``CLEAN`` it should say what the verdict does *not* claim.
    evidence
        Free-form mapping — located instances, counts, offsets. Never load-bearing for the
        contract; the guards never read it.
    """

    screen: str
    verdict: str
    screened: dict[str, Any] | None = None
    signature: str | None = None
    missing: str | None = None
    detail: str = ""
    evidence: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.screen, str) or not self.screen.strip():
            raise ScreenContractError("a verdict must name the screen that reached it")
        if self.verdict not in VERDICTS:
            raise ScreenContractError(
                f"verdict must be one of {VERDICTS}, got {self.verdict!r}")

        object.__setattr__(self, "screened", _validate_screened(self.screened))

        if self.verdict == CLEAN:
            # 🔴 The guarantee. Everything else in this module is convenience.
            if self.screened is None:
                raise ScreenContractError(
                    "CLEAN requires screened={'digest','bytes'}: a screen that cannot say "
                    "which bytes it read has not established that anything is clean. This is "
                    "the 2026-09-09 inverted-argument defect, made unrepresentable")
            if self.screened["bytes"] == 0:
                raise ScreenContractError(
                    "CLEAN over zero bytes is INSUFFICIENT_DATA, not a pass: an empty surface "
                    "matches no signature, and reporting that as clean is a silent pass")
        if self.verdict == REFUSED:
            if not self.signature or not str(self.signature).strip():
                raise ScreenContractError(
                    "REFUSED must name the signature that fired. 'The gate said no' is not a "
                    "finding; 'the gate said no because X' is")
            if self.screened is None:
                raise ScreenContractError(
                    "REFUSED requires screened={'digest','bytes'}: a refusal is a statement "
                    "about specific bytes and must identify them")
        elif self.signature is not None:
            raise ScreenContractError(
                f"signature is meaningful only on {REFUSED}; got it on {self.verdict}")

        if self.verdict == INSUFFICIENT_DATA:
            if not self.missing or not str(self.missing).strip():
                raise ScreenContractError(
                    f"{INSUFFICIENT_DATA} must name the missing input")
        elif self.missing is not None:
            raise ScreenContractError(
                f"missing is meaningful only on {INSUFFICIENT_DATA}; got it on {self.verdict}")

        if not isinstance(self.evidence, Mapping):
            raise ScreenContractError("evidence must be a mapping")
        object.__setattr__(self, "evidence", dict(self.evidence))

    # ---- constructors -------------------------------------------------------------

    @classmethod
    def clean(cls, screen: str, data: Any, *, detail: str = "",
              evidence: Mapping[str, Any] | None = None) -> "ScreenVerdict":
        """CLEAN over exactly ``data``. Raises unless ``data`` is non-empty content."""
        return cls(screen=screen, verdict=CLEAN, screened=screened_of(data),
                   detail=detail, evidence=dict(evidence or {}))

    @classmethod
    def refused(cls, screen: str, data: Any, *, signature: str, detail: str = "",
                evidence: Mapping[str, Any] | None = None) -> "ScreenVerdict":
        """REFUSED over exactly ``data``, naming ``signature``."""
        return cls(screen=screen, verdict=REFUSED, screened=screened_of(data),
                   signature=signature, detail=detail, evidence=dict(evidence or {}))

    @classmethod
    def insufficient(cls, screen: str, *, missing: str, detail: str = "",
                     data: Any = None,
                     evidence: Mapping[str, Any] | None = None) -> "ScreenVerdict":
        """INSUFFICIENT_DATA naming ``missing``.

        ``data`` is optional and is hashed when present, so a verdict can distinguish
        *"the surface was empty"* (digest of zero bytes) from *"there was no surface"*
        (no digest at all). The repairs differ.
        """
        return cls(screen=screen, verdict=INSUFFICIENT_DATA,
                   screened=None if data is None else screened_of(data),
                   missing=missing, detail=detail, evidence=dict(evidence or {}))

    @classmethod
    def reject_uninformative(cls, screen: str, data: Any, *,
                             expected: str = "content") -> "ScreenVerdict | None":
        """Return an ``INSUFFICIENT_DATA`` verdict if ``data`` cannot inform a screen, else None.

        Catches, in one call, the three shapes that produced a silent pass on 2026-09-09:

        * ``None`` — nothing was read;
        * zero-length, or whitespace-only, content — a surface that matches every absence;
        * a ``Path``, or a one-line string that names an existing filesystem path — the
          inverted call, where the *filename* gets screened and always comes back clean.

        The path check is deliberately conservative: it fires only on a single-line string
        that exists on disk, so a genuine text surface (multi-line, or not a path) is never
        mistaken for one. A screen calls this immediately after reading its input and returns
        the verdict unchanged if it is not ``None``.
        """
        if data is None:
            return cls.insufficient(screen, missing=expected,
                                    detail=f"{expected} was None; nothing was screened")
        if isinstance(data, os.PathLike):
            return cls.insufficient(
                screen, missing=expected,
                detail=(f"a path ({os.fspath(data)!r}) was handed where {expected} was "
                        "expected; screening a path name always passes and asserts nothing"))
        if isinstance(data, str) and data.strip() and "\n" not in data and len(data) <= 4096:
            try:
                if os.path.exists(data):
                    return cls.insufficient(
                        screen, missing=expected,
                        detail=(f"a filesystem path ({data!r}) was handed where {expected} "
                                "was expected; screening a path name always passes and "
                                "asserts nothing"))
            except (OSError, ValueError):  # pragma: no cover - exotic path values
                pass
        raw = as_bytes(data)
        if len(raw) == 0:
            return cls.insufficient(screen, missing=expected, data=data,
                                    detail=f"{expected} was zero-length; a screen over no "
                                           "bytes establishes nothing")
        if not raw.strip():
            return cls.insufficient(screen, missing=expected, data=data,
                                    detail=f"{expected} was whitespace only; a screen over no "
                                           "content establishes nothing")
        return None

    # ---- accessors ----------------------------------------------------------------

    @property
    def is_clean(self) -> bool:
        return self.verdict == CLEAN

    @property
    def is_refused(self) -> bool:
        return self.verdict == REFUSED

    @property
    def is_insufficient(self) -> bool:
        return self.verdict == INSUFFICIENT_DATA

    @property
    def digest(self) -> str | None:
        return None if self.screened is None else self.screened["digest"]

    def covers(self, data: Any) -> bool:
        """Did this verdict screen exactly ``data``?

        The question a boolean could never answer. A caller holding both a verdict and the
        bytes it means to act on asks this before trusting the colour.
        """
        if self.screened is None:
            return False
        return self.screened["digest"] == screened_of(data)["digest"]

    def as_dict(self) -> dict[str, Any]:
        record: dict[str, Any] = {"screen": self.screen, "verdict": self.verdict,
                                  "screened": self.screened}
        if self.signature is not None:
            record["signature"] = self.signature
        if self.missing is not None:
            record["missing"] = self.missing
        record["detail"] = self.detail
        if self.evidence:
            record["evidence"] = self.evidence
        return record

    @classmethod
    def from_dict(cls, record: Mapping[str, Any]) -> "ScreenVerdict":
        """Rebuild from ``as_dict()``, re-applying every guard.

        A stored CLEAN verdict with no digest is refused on the way back in, so the JSON
        surface is not a way around the contract.
        """
        unknown = set(record) - {"screen", "verdict", "screened", "signature", "missing",
                                 "detail", "evidence"}
        if unknown:
            raise ScreenContractError(f"unknown verdict fields: {sorted(unknown)}")
        return cls(screen=record.get("screen", ""), verdict=record.get("verdict", ""),
                   screened=record.get("screened"), signature=record.get("signature"),
                   missing=record.get("missing"), detail=record.get("detail", ""),
                   evidence=dict(record.get("evidence") or {}))

    def render(self) -> str:
        """One line, and the digest is on it — the point is that it is never omissible."""
        where = "screened nothing" if self.screened is None else (
            f"{self.screened['bytes']}B {self.screened['digest']}")
        named = ""
        if self.signature:
            named = f" signature={self.signature}"
        elif self.missing:
            named = f" missing={self.missing}"
        tail = f" — {self.detail}" if self.detail else ""
        return f"[{self.verdict}] {self.screen} ({where}){named}{tail}"

    def __str__(self) -> str:  # pragma: no cover - convenience
        return self.render()
