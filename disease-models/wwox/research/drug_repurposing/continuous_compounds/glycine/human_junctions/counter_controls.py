"""Verify the frozen counting binary with diagnostic reads of known class and quality."""
import csv
import gzip
import io
from pathlib import Path
import subprocess
import sys
import tempfile

folder = Path(__file__).resolve().parent
probes = folder/"junction_probes.tsv"
with probes.open() as stream:
    seq = {(r["class"], int(r["offset"])):r["seq"] for r in csv.DictReader(stream,delimiter="\t")}
inc, skip = seq["included",15], seq["skipped",15]
reverse = lambda s:s.translate(str.maketrans("ACGT","TGCA"))[::-1]
examples = [
    (inc,30), (reverse(skip),30), (inc,20), (skip,19),
    (seq["skipped",10],30), (inc+"N"+skip,30),
    (inc+"N"+inc,30), ("N"*31,40),
]
expected = {("centered",20):(3,1,1), ("any",20):(3,2,1),
            ("centered",30):(2,1,1), ("any",30):(2,2,1)}
with tempfile.TemporaryDirectory() as work:
    path=Path(work)/"controls.fastq.gz"
    with gzip.open(path,"wt") as stream:
        for i,(s,q) in enumerate(examples):
            stream.write(f"@control{i}\n{s}\n+\n{chr(33+q)*len(s)}\n")
    output=subprocess.check_output([sys.argv[1],"count",probes,path],text=True)
rows=list(csv.DictReader(io.StringIO(output),delimiter="\t"))
assert len(rows)==len(expected)
assert {(r["rule"],int(r["Q"])):tuple(int(r[k]) for k in ("included","skipped","conflict")) for r in rows}==expected
assert all(int(r["reads"])==len(examples) for r in rows)
print(output,end="")
