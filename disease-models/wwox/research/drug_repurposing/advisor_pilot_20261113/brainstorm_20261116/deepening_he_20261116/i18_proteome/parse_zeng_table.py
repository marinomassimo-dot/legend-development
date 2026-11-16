#!/usr/bin/env python3
"""Parse the text layer of Supplemental Table 1 (Zeng 2024, PMID 38563965; WWOX-silenced human endothelial cells, TMT proteome) into a TSV.

    python3 parse_zeng_table.py --pdf <Supplemental_Table_1.pdf> --out <file.tsv>      (needs pdftotext)
    python3 parse_zeng_table.py --help

Columns as the PDF names them: Row, Protein, UniProtKB/Swiss-Prot, BH.adj.P.val, Neg.Log10.BH.adj.P.val, Log2FoldChange (Treatment - Reference), Log2 normalised intensity (controls), (WWOX-silenced).
The minus sign in the PDF is U+2010; NA stays NA; an accession followed by '(+n)' (isoform or group marker) keeps the first accession; decoy rows (accession ending -DECOY) are counted and left out. Rows that do not parse are listed on stderr, never dropped silently. Not medical advice.
"""
import argparse, csv, hashlib, re, subprocess, sys
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--pdf"); ap.add_argument("--out"); a = ap.parse_args()
if not (a.pdf and a.out):
    ap.print_help(); sys.exit(0)
txt = subprocess.run(["pdftotext", "-layout", a.pdf, "-"], capture_output=True, text=True, check=True).stdout.replace("\u2010", "-").replace("\u2212", "-")
lines = txt.splitlines()
rows, bad, decoys = [], [], []
NUMTOK = re.compile(r"^(NA|-?[\d.]+(?:[eE]-?\d+)?)$")
i = 0
while i < len(lines):
    line = lines[i]; i += 1
    if not re.match(r"^\s*\d+\s+\S+", line): continue
    if "-DECOY" in line:
        decoys.append(line); continue
    tok = line.split()
    row, sym, acc = tok[0], tok[1], tok[2]; rest = tok[3:]
    if rest and re.match(r"^\(\+\d+\)$", rest[0]): rest = rest[1:]            # isoform or group marker, e.g. '(+1)'
    m = re.match(r"^sp\|([A-Z0-9]+)\|", acc)
    if m: acc = m.group(1)                                                        # accession given in sp|ACC|NAME form
    while len(rest) < 5 and i < len(lines) and not re.match(r"^\s*\d+\s+\S+\s", lines[i]):   # values wrapped onto the next line
        rest += lines[i].split(); i += 1
    if len(rest) == 5 and all(NUMTOK.match(x) for x in rest):
        rows.append((row, sym, acc, *rest))
    else:
        bad.append(line)
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["row", "symbol", "uniprot", "bh_adj_p", "neg_log10_bh", "log2fc", "log2_int_control", "log2_int_silenced"]); w.writerows(rows)
print(f"parsed {len(rows)} real rows; decoy rows left out {len(decoys)}; unparsed {len(bad)}; pdf sha256 {hashlib.sha256(open(a.pdf, 'rb').read()).hexdigest()}")
for b in bad[:10]: print("UNPARSED:", b, file=sys.stderr)
