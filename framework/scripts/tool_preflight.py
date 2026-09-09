#!/usr/bin/env python3
"""Report which external tools this repository's own scripts need, and which are missing here.

🔴 WHY THIS EXISTS, and it was paid for. On 2026-09-09 a scientist actor set out to restore the
figure evidence of `PMID25331887`, whose manifest fingerprints seven PNGs extracted **by xref**
with PyMuPDF — the method `figure_ppi_preflight.py` uses (`import fitz`). This deployment has no
`fitz`, and no `pip` to add one. That was discovered **mid-reading**, after the article PDF had
already been re-acquired and verified byte-identical, and only because the strict manifest
validator refused seven paths.

The cost was not the missing package. The cost was that its **scope** was invisible: the same
absence blocks figure-evidence restoration for EVERY manifest in this repository that declares
xref-extracted crops, and nothing anywhere said so. `evidence_presence.py` (2026-09-09) answers
"are the bytes here?" — it cannot answer "could they be put here?", because recoverability is a
property of the TOOLCHAIN, not of the manifest.

So this reports the toolchain, once, in one line, at session start — before a reading commits to a
plan the environment cannot execute.

DISCOVERY, NOT A GATE. Exits 0 whether tools are missing or not, following the discipline
`artifact_index.py` states and `evidence_presence.py` follows. A missing optional tool is the
normal condition of a fresh container and must not be an error, or the check gets switched off.
`--fail-on-missing` raises status **only** for tools marked REQUIRED, never for optional ones.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

# Each entry: (name, kind, required, what breaks without it)
# `required` is deliberately conservative: a tool is REQUIRED only when a repository script has no
# fallback path at all. Everything else is optional and its absence is reported, never raised.
TOOLS = [
    ("fitz", "python", False,
     "PyMuPDF. Needed to extract figure images from a PDF BY XREF at deposited resolution, which is "
     "how several manifests' figure artifacts were produced. Without it those crops cannot be "
     "regenerated and their manifests cannot pass --verify-artifacts in this checkout. "
     "poppler is NOT a substitute: pdfimages re-encodes and yields different bytes."),
    ("pdftotext", "binary", False,
     "poppler. Deterministic PDF text extraction for a declared `article_text` surface."),
    ("pdftoppm", "binary", False,
     "poppler. Renders PDF pages as images — the fallback surface rule 5d requires when a PDF text "
     "layer is SUSPECT and locators must be anchored to the rendered page instead."),
    ("pdfimages", "binary", False,
     "poppler. Lists/extracts embedded PDF images. Useful for inventory; does NOT reproduce "
     "PyMuPDF xref bytes."),
    ("git", "binary", True, "Version control. Every durable milestone is a commit."),
    ("flock", "binary", False,
     "util-linux. Serialises commits when several actors share one checkout."),
]


def probe(name: str, kind: str) -> bool:
    if kind == "python":
        try:
            return importlib.util.find_spec(name) is not None
        except (ImportError, ValueError):
            return False
    return shutil.which(name) is not None


def scripts_needing(root: Path, tool: str) -> list[str]:
    """Which repository scripts reference this tool. Read-only, and text-matched on purpose.

    A grep is a legitimate FILE SEARCH here, not a method of analysis: it answers "which files
    mention this name", which is exactly the question, and the answer is reported as a pointer for
    a human to open rather than used to conclude anything about behaviour.
    """
    hits: list[str] = []
    pattern = re.compile(rf"(?:^|[^\w]){re.escape(tool)}(?:[^\w]|$)")
    for path in sorted(root.glob("framework/scripts/*.py")):
        if path.name == "tool_preflight.py":
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if pattern.search(stripped):
                hits.append(path.relative_to(root).as_posix())
                break
    return hits


def run(root: Path) -> dict:
    rows = []
    for name, kind, required, why in TOOLS:
        present = probe(name, kind)
        rows.append({
            "tool": name, "kind": kind, "required": required, "present": present,
            "consequence": why, "referenced_by": scripts_needing(root, name),
        })
    return {
        "tools": rows,
        "present": sum(1 for r in rows if r["present"]),
        "missing": sum(1 for r in rows if not r["present"]),
        "missing_required": sorted(r["tool"] for r in rows if not r["present"] and r["required"]),
        "missing_optional": sorted(r["tool"] for r in rows if not r["present"] and not r["required"]),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fail-on-missing", action="store_true",
                    help="exit 1 if a REQUIRED tool is missing; never for an optional one")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    result = run(root)

    if args.json:
        print(json.dumps(result, indent=1))
    else:
        for r in result["tools"]:
            mark = "OK     " if r["present"] else ("MISSING" if r["required"] else "absent ")
            tag = " [REQUIRED]" if r["required"] else ""
            print(f"  [{mark}] {r['tool']}{tag}")
            if not r["present"]:
                print(f"            {r['consequence']}")
                if r["referenced_by"]:
                    print(f"            referenced by: {', '.join(r['referenced_by'])}")
        print(f"tools: {len(result['tools'])} | present: {result['present']} | "
              f"missing: {result['missing']}")
        if result["missing_required"]:
            print(f"VERDICT: REQUIRED TOOL MISSING — {', '.join(result['missing_required'])}")
        elif result["missing_optional"]:
            print(f"VERDICT: usable, with {len(result['missing_optional'])} optional tool(s) absent "
                  f"— {', '.join(result['missing_optional'])}. Plans depending on them will fail "
                  f"LATE unless chosen against now.")
        else:
            print("VERDICT: every declared tool is available")

    if args.fail_on_missing and result["missing_required"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
