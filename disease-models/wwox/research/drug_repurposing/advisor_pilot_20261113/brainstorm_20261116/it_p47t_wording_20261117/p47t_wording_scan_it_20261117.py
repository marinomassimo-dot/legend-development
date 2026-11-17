"""Count lines under analysis/ and registries/ that state P47T protein abundance as normal / wild-type.

Run from disease-models/wwox:  python3 -I p47t_wording_scan_it_20261117.py > hits.tsv
Output TSV: file, line, layer, qualified_in_line, phrase, sentence (cut at 300 characters).
Rule (fixed before reading hits): a line names P47T (or its HGVS forms) AND matches an abundance phrase.
Markdown emphasis and backticks are stripped before matching. Line level only: a statement that spans two lines is not seen. Generated exports and the receipt
ledger are listed apart (layer 'generated/ledger') and are not edit targets.
"""
import csv
import pathlib
import re
import sys

P = re.compile(r"P47T|Pro47Thr|c\.139C>A", re.I)
ABUND = re.compile(
    r"(normal|wild[- ]?type|similar|comparable)\s+(total\s+)?(wwox\s+)?(protein|abundance|amounts?|levels?)"
    r"|normal western( blot)?|protein[- ]normal|protein (level )?is normal|abundance is normal|both normal|normal at|at normal"
    r"|protein (retained|preserved)|retains? (the )?protein",
    re.I)
QUAL = re.compile(r"not quantified|visual inspection|by eye|corretto 2026-09-28|corrected 2026-09-28|n ?= ?2|10% input", re.I)
GEN = ("analysis/data/", "registries/fulltext_read_receipts.jsonl")


def layer(path):
    if path.startswith(GEN):
        return "generated/ledger"
    name = path.split("/")[-1]
    if path.startswith("registries/"):
        return "registry history (append-only)" if "history" in name else "live canonical surface (registry)"
    if re.search(r"_20\d{6}\.md$|/20\d\d-\d\d-\d\d_", path):
        return "dated analysis"
    return "living analysis (undated name)"


rows = []
for d in ("analysis", "registries"):
    for f in sorted(pathlib.Path(d).rglob("*")):
        if not f.is_file() or f.suffix not in (".md", ".tsv", ".txt", ".jsonl"):
            continue
        for i, line in enumerate(f.read_text(errors="replace").splitlines(), 1):
            if P.search(line):
                m = ABUND.search(re.sub(r"[*`]", "", line))
                if m:
                    rows.append([str(f), i, layer(str(f)), "yes" if QUAL.search(re.sub(r"[*`]", "", line)) else "no", m.group(0), line.strip()[:300]])
w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
w.writerow(["file", "line", "layer", "qualified_in_line", "phrase", "sentence"])
w.writerows(rows)
files = {}
for r in rows:
    files.setdefault((r[2], r[3]), set()).add(r[0])
print("total lines %d in %d files" % (len(rows), len({r[0] for r in rows})), file=sys.stderr)
for k, v in sorted(files.items()):
    print("  %-40s qualified=%-3s files=%d" % (k[0], k[1], len(v)), file=sys.stderr)
