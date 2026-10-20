#!/usr/bin/env python3
"""Which image file carries which figure caption, read from a JATS/PMC XML — before a locator
names a panel.

WHY. In one wave of the metabolic batch (2026-10-19/20) three of eight PMC deposits paired
figure files and captions in a way the file names did not say: `g002` was Figure 1; files
`g003, g002, g004, g001` were Figures 1 to 4; one deposit showed a timeline image under a
caption describing a pathway. A reader who opens `g002.jpg` "as Figure 2" anchors a locator to
the wrong panel, and the blind auditor caught one such case only because it had the XML (N7 of
PLAN-HARNESS-FROM-METABOLIC-BATCH-20261020).

WHAT. One row per `<fig>`: its id, label, the first words of its caption, the graphic file(s)
the XML binds to it, whether each file is on disk (with `--figures DIR`), and two flags:

    NUMBER_DIFFERS   the trailing number of the file name is not the figure's label number
                     (legitimate, often — but it is exactly where readers mis-pair)
    MISSING_FILE     the XML names a graphic that is not in --figures DIR
    SHARED_GRAPHIC   two figures name the same file

It pairs from the XML only. It cannot see what an image depicts: a caption over the wrong
picture in the deposit itself is found by opening every image, and this tool says which caption
each opened image must be read against. A screen, never a gate: exit 0 always unless the XML
is unreadable (2).

    python3 framework/scripts/figure_legend_pairs.py files/fulltext/PMID<pmid>_<tag>_PMC.xml \
        --figures files/figures/PMID<pmid> [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

XLINK = "{http://www.w3.org/1999/xlink}href"


def _text(node) -> str:
    return re.sub(r"\s+", " ", "".join(node.itertext())).strip() if node is not None else ""


IMAGE_SUFFIX = re.compile(r"\.(jpe?g|png|gif|tiff?|webp|eps|svg)$", re.I)


def _bare(name: str) -> str:
    """A graphic name without an image extension (`pone.0123.g002` has none to strip)."""
    return IMAGE_SUFFIX.sub("", name or "")


def _number(text: str) -> str:
    match = re.search(r"(\d+)\s*$", _bare(text))
    return str(int(match.group(1))) if match else ""


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def pairs(xml_text: str, figures: Path | None = None) -> list[dict]:
    root = ET.fromstring(xml_text)
    rows: list[dict] = []
    for fig in root.iter():
        if _local(fig.tag) != "fig":
            continue
        label = _text(next((c for c in fig if _local(c.tag) == "label"), None))
        caption = _text(next((c for c in fig.iter() if _local(c.tag) == "caption"), None))
        graphics = [g.get(XLINK) or g.get("href") or "" for g in fig.iter()
                    if _local(g.tag) == "graphic"]
        graphics = [g for g in graphics if g]
        flags = []
        label_number = _number(re.sub(r"[^\w\s]", " ", label))
        if label_number and any(_number(g) and _number(g) != label_number for g in graphics):
            flags.append("NUMBER_DIFFERS")
        on_disk = {}
        if figures is not None:
            for g in graphics:
                found = sorted(p.name for p in figures.iterdir()
                               if p.name == g or _bare(p.name) == _bare(g)) \
                    if figures.is_dir() else []
                on_disk[g] = found
                if not found:
                    flags.append("MISSING_FILE")
        rows.append({"id": fig.get("id", ""), "label": label,
                     "caption": caption[:140], "graphics": graphics,
                     "on_disk": on_disk, "flags": sorted(set(flags))})
    seen: dict[str, int] = {}
    for row in rows:
        for g in row["graphics"]:
            seen[g] = seen.get(g, 0) + 1
    for row in rows:
        if any(seen[g] > 1 for g in row["graphics"]):
            row["flags"] = sorted(set(row["flags"]) | {"SHARED_GRAPHIC"})
    return rows


def render(rows: list[dict]) -> str:
    lines = [f"{len(rows)} figure(s) in the XML; read each opened image against the caption "
             "on ITS row, never by file number"]
    for row in rows:
        files = ", ".join(row["graphics"]) or "(no graphic)"
        if row["on_disk"]:
            files += "  [on disk: " + "; ".join(
                f"{g} -> {', '.join(v) or 'NONE'}" for g, v in row["on_disk"].items()) + "]"
        flag = f"  !! {', '.join(row['flags'])}" if row["flags"] else ""
        lines.append(f"  {row['label'] or row['id'] or '(unlabelled)'}: {files}{flag}\n"
                     f"      {row['caption'][:110]}")
    flagged = sum(bool(r["flags"]) for r in rows)
    lines.append(f"{flagged} row(s) flagged — a flag is where pairing goes wrong, not an error")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("xml", type=Path)
    parser.add_argument("--figures", type=Path, default=None,
                        help="directory holding the figure files, to check each is present")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        rows = pairs(args.xml.read_text(encoding="utf-8", errors="replace"), args.figures)
    except (OSError, ET.ParseError) as exc:
        print(f"figure_legend_pairs: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(rows, indent=1, ensure_ascii=False) if args.json else render(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
