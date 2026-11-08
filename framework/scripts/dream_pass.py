"""Select the inputs of a Dream pass: what is new, who reads it, what waits for a person.

A Dream pass is the agent's own reasoning (skill `legend-dream`); this script only does the
mechanical part that costs tokens when done by hand. It writes nothing, calls no service and
decides nothing: its output is a list of places to look at, never a finding.

  consumers   research folders added since a date or ref, and the files outside each folder that
              cite it by name (none outside = nothing downstream has read it yet)
  pointers    drafts and hand-offs marked NOT SENT / FOR THE OPERATOR, the identifiers they
              carry, and the files that name the same identifier without naming the draft
  pairs       the lines, verbatim, where two entities occur together, with the table header above
              each tsv hit so context, status and limit columns stay attached; a co-occurrence
              orients retrieval and carries no sign, no count is evidence
  quiet       exit 0 and print one line when nothing material changed, so the pass can end fast

Usage: python3 framework/scripts/dream_pass.py consumers --since 2026-11-05
       python3 framework/scripts/dream_pass.py pairs HDAC5 SLC2A1
       python3 framework/scripts/dream_pass.py pointers
       python3 framework/scripts/dream_pass.py quiet --since HEAD~5
"""
import argparse
import os
import re
import subprocess
import sys

ROOT_DEFAULT = "disease-models/wwox/research"
ID_RE = re.compile(r"\b(E-MTAB-\d+|GSE\d{4,}|PRJ[A-Z]{2}\d+|CHEMBL\d+|NCT\d{8})\b")
MARK_RE = re.compile(r"NOT SENT|FOR THE OPERATOR|for the operator|draft for the operator", re.I)


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    return r.stdout


def since_args(since):
    if re.match(r"^\d{4}-\d{2}-\d{2}$", since):
        return ["--since", since]
    return [f"{since}..HEAD"]


def added_dirs(since, root):
    """Research folders (one level under the module, two under drug_repurposing) with files added
    since `since` that still exist in the working tree; renamed or removed ones are skipped."""
    out = git("log", *since_args(since), "--diff-filter=A", "--name-only", "--format=", "--", root)
    depth = len(root.split("/"))
    dirs = {}
    for line in out.splitlines():
        parts = line.split("/")
        if len(parts) <= depth + 1:
            continue
        cut = depth + 2 if parts[depth] == "drug_repurposing" and len(parts) > depth + 2 else depth + 1
        d = "/".join(parts[:cut])
        if os.path.isdir(d):
            dirs[d] = dirs.get(d, 0) + 1
    return dirs


def citing_files(name, exclude_prefix):
    out = git("grep", "-l", "-F", "--", name)
    return [f for f in out.splitlines() if not f.startswith(exclude_prefix + "/")]


def cmd_consumers(a):
    dirs = added_dirs(a.since, a.root)
    if not dirs:
        print(f"quiet: no research folder added since {a.since}")
        return 0
    print("folder\tfiles_added\tcited_from_outside\texamples")
    for d, n in sorted(dirs.items()):
        cites = citing_files(d.rsplit("/", 1)[-1], d)
        print(f"{d}\t{n}\t{len(cites)}\t{';'.join(cites[:3])}")
    return 0


def cmd_pointers(a):
    files = [f for f in git("ls-files", a.root).splitlines() if f.endswith(".md")]
    rows = []
    for f in files:
        try:
            head = open(f, encoding="utf-8").read(1500)
        except OSError:
            continue
        first = head.splitlines()[0] if head else ""
        if not (MARK_RE.search(first) or re.search(r"Status:\s*\*{0,2}\s*a draft", head, re.I)):
            continue
        ids = sorted(set(ID_RE.findall(head)))
        base = f.rsplit("/", 1)[-1]
        for i in ids:
            mention = set(git("grep", "-l", "-F", "--", i).splitlines())
            named = set(git("grep", "-l", "-F", "--", base).splitlines())
            gap = sorted(x for x in mention - named - {f} if x.endswith(".md"))
            rows.append((f, i, len(mention), len(gap), gap))
    print("draft\tidentifier\tfiles_naming_id\tprose_files_naming_id_without_the_draft")
    for f, i, m, g, gap in rows:
        print(f"{f}\t{i}\t{m}\t{g}")
        for x in gap[: a.show]:
            print(f"    {x}")
    return 0


def cmd_pairs(a):
    pat_a = re.compile(r"\b" + re.escape(a.a) + r"\b", re.I)
    pat_b = re.compile(r"\b" + re.escape(a.b) + r"\b", re.I)
    files = [f for f in git("ls-files", a.root).splitlines() if f.endswith((".tsv", ".md"))]
    shown = 0
    print(f"# lines naming both {a.a} and {a.b}; orients retrieval only, carries no sign, no count is evidence")
    for f in files:
        try:
            lines = open(f, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        hits = [i for i, ln in enumerate(lines) if pat_a.search(ln) and pat_b.search(ln)]
        if not hits:
            continue
        print(f"## {f}")
        if f.endswith(".tsv") and lines:
            print("   header: " + lines[0][:300])
        for i in hits[: a.show]:
            print(f"   {i + 1}: {lines[i][:600]}")
            shown += 1
    print(f"# {shown} lines shown")
    return 0


def cmd_quiet(a):
    out = git("log", *since_args(a.since), "--format=%h", "--", a.root)
    n = len(out.split())
    print(f"quiet: no commit touched {a.root} since {a.since}" if n == 0 else f"material: {n} commits touched {a.root} since {a.since}")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("consumers", cmd_consumers), ("pointers", cmd_pointers), ("quiet", cmd_quiet)):
        s = sub.add_parser(name)
        s.add_argument("--since", default="HEAD~20", help="a date (YYYY-MM-DD) or a git ref")
        s.add_argument("--root", default=ROOT_DEFAULT)
        s.add_argument("--show", type=int, default=6, help="pointers: files listed per identifier")
        s.set_defaults(fn=fn)
    s = sub.add_parser("pairs")
    s.add_argument("a")
    s.add_argument("b")
    s.add_argument("--root", default=ROOT_DEFAULT)
    s.add_argument("--show", type=int, default=3, help="lines shown per file")
    s.set_defaults(fn=cmd_pairs)
    a = p.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
