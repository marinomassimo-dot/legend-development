"""Locate diagnostic Grin1 RNA sequence and flanking homology in archived transcripts."""
import csv
import gzip
import sys
from difflib import SequenceMatcher
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parents[1] / "perampanel_ampa_splicing_20261123"))
from analyze import CODE

with (here/"cassette_identity.tsv").open() as source:
    classes = {r["transcript"]:r["supported_junction"] for r in csv.DictReader(source,delimiter="\t")}
parts = {name:[] for name in classes}
with gzip.open(next(Path(sys.argv[1]).glob("reference_ensembl_r92/*.fa.gz")),"rt") as source:
    for line in source:
        if line.startswith(">"):
            name = line[1:].split()[0]
        elif name in parts:
            parts[name].append(line.strip().upper())
seq = {name:"".join(lines) for name,lines in parts.items()}
def site(sequence, marker):
    hits = []
    for frame in range(3):
        protein = "".join(CODE.get(sequence[i:i+3],"X") for i in range(frame,len(sequence)-2,3))
        if marker in protein:
            hits.append(frame+3*(protein.index(marker)+len(marker)))
    point, = hits
    return point

left = "ETLLEERESK"
insert = "SKKRNYENLDQLSYDNKRGPK"
inc = next(seq[n] for n in seq if classes[n]=="included")
skip = next(seq[n] for n in seq if classes[n]=="skipped")
a,b = site(inc,left),site(skip,left)
assert inc[a-30:a]==skip[b-30:b] and inc[a+63:a+93]==skip[b:b+30]
# These are aligned diagnostic windows around the peptide insertion boundaries.
windows = [inc[a-15:a+16],inc[a+63-15:a+63+16],skip[b-15:b+16]]
out=csv.writer(sys.stdout,delimiter="\t",lineterminator="\n")
out.writerow(("transcript","protein_class","length","insert_left","insert_right","skip",
              "aligned_upstream","aligned_downstream","included_reference_covered_nt"))
for name,s in seq.items():
    matches = [m for m in SequenceMatcher(None,inc,s,autojunk=False).get_matching_blocks() if m.size>=31]
    upstream = any(m.a+m.size<=a or m.a<=a-31 for m in matches)
    downstream = any(m.a+m.size>=a+63+31 for m in matches)
    out.writerow((name,classes[name],len(s),*(int(w in s) for w in windows),int(upstream),int(downstream),sum(m.size for m in matches)))
