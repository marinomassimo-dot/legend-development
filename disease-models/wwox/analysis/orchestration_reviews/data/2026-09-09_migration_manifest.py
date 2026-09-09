#!/usr/bin/env python3
"""Build the migration manifest for the root -> desktop handover on this VPS.

Absolute paths, byte sizes, SHA-256. Classifies every item as INDISPENSABLE
(nothing reproduces it), RECONSTRUCTIBLE (derived, regenerable) or DO_NOT_COPY
(credentials: the target user re-authenticates instead).
Re-runnable; nothing here is typed by hand.
"""
import hashlib, json, os, sys
from pathlib import Path

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/migration_manifest.jsonl")

ROOTS = [
    ("INDISPENSABLE", "evidence",     Path("/root/legend-development/files")),
    ("INDISPENSABLE", "transcripts",  Path("/root/.claude/projects/-root-legend-development")),
    ("INDISPENSABLE", "claude_config", Path("/root/.claude/settings.json")),
    ("INDISPENSABLE", "claude_plugins", Path("/root/.claude/plugins")),
    ("RECONSTRUCTIBLE", "scratchpad", Path("/tmp/claude-0/-root-legend-development/3e1bc608-80c5-4c1c-a5a3-3c4da9b68c75")),
    ("DO_NOT_COPY", "credentials",    Path("/root/.claude/.credentials.json")),
    ("DO_NOT_COPY", "cli_state",      Path("/root/.claude.json")),
]

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

rows, totals = [], {}
with OUT.open("w", encoding="utf-8") as out:
    for cls, group, root in ROOTS:
        if not root.exists():
            rows.append({"class": cls, "group": group, "path": str(root), "state": "ABSENT"})
            continue
        paths = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file())
        for p in paths:
            size = p.stat().st_size
            rec = {"class": cls, "group": group, "path": str(p.resolve()), "bytes": size,
                   "sha256": (sha256(p) if cls != "DO_NOT_COPY" else None)}
            out.write(json.dumps(rec) + "\n")
            rows.append(rec)
            k = (cls, group)
            n, b = totals.get(k, (0, 0))
            totals[k] = (n + 1, b + size)

for (cls, group), (n, b) in sorted(totals.items()):
    print(f"{cls:17} {group:15} files={n:5}  bytes={b:>13,}  ({b/1048576:.1f} MiB)")
print(f"\nmanifest: {OUT}  righe={sum(1 for r in rows if 'bytes' in r)}")
