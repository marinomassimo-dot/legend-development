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


class GitError(Exception):
    pass


def git(*args):
    """Run git; a failed command raises, so an unknown ref never reads as 'nothing changed'."""
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if r.returncode != 0 and not (args and args[0] == "grep" and r.returncode == 1):
        raise GitError(f"git {' '.join(args[:3])}: {r.stderr.strip() or 'exit ' + str(r.returncode)}")
    return r.stdout


def worktree_changes(root):
    """Uncommitted paths under root: ('M'|'A'|'D'|'?', path). Untracked folders are expanded to files."""
    out = git("status", "--porcelain", "--untracked-files=all", "--", root)
    return [(ln[:2].strip()[:1] or "M", ln[3:]) for ln in out.splitlines() if ln.strip()]


def since_args(since):
    if re.match(r"^\d{4}-\d{2}-\d{2}$", since):
        return ["--since", since + " 00:00"]
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
    depth = len(a.root.split("/"))
    for st, f in worktree_changes(a.root):
        parts = f.split("/")
        if st in ("?", "A") and len(parts) > depth + 1:
            cut = depth + 2 if parts[depth] == "drug_repurposing" and len(parts) > depth + 2 else depth + 1
            d = "/".join(parts[:cut])
            if os.path.isdir(d):
                dirs[d] = dirs.get(d, 0) + 1
    print("# scope: committed history since the given date or ref, plus uncommitted new files in the working tree")
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


def clip(text, width, full, path, lineno):
    """Cut an economical view, but say how much was left out and where to read all of it."""
    if full or len(text) <= width:
        return text
    return f"{text[:width]} [+{len(text) - width} chars omitted: {path}:{lineno}, or --full]"


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
            print("   header: " + clip(lines[0], a.width, a.full, f, 1))
        for i in hits[: a.show]:
            print(f"   {i + 1}: " + clip(lines[i], a.width, a.full, f, i + 1))
            shown += 1
        if len(hits) > a.show:
            print(f"   [{len(hits) - a.show} more matching lines in {f} not shown; --show N or grep -n]")
    print(f"# {shown} lines shown; a line cut at --width is marked, and --full prints every line whole")
    return 0


def cmd_quiet(a):
    out = git("log", *since_args(a.since), "--format=%h", "--", a.root)
    n = len(out.split())
    wt = worktree_changes(a.root)
    if n == 0 and not wt:
        print(f"quiet: no commit since {a.since} and no uncommitted change under {a.root} "
              "(this checks files under that path only; a change elsewhere, in chat or in another checkout is not seen)")
    else:
        print(f"material: {n} commits since {a.since}; {len(wt)} uncommitted paths under {a.root}")
        for st, f in wt[:10]:
            print(f"    {st} {f}")
        if len(wt) > 10:
            print(f"    ... {len(wt) - 10} more (git status --porcelain -- {a.root})")
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
    s.add_argument("--width", type=int, default=300, help="characters per line before an omission marker")
    s.add_argument("--full", action="store_true", help="print lines and headers whole")
    s.set_defaults(fn=cmd_pairs)
    a = p.parse_args()
    try:
        return a.fn(a)
    except GitError as e:
        print(f"ERROR: {e}\nThis is not 'nothing changed': fix the reference or check the change by hand.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
