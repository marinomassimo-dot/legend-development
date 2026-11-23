"""Integration check for GRIA2 strand, edit-state, splicing and Phred handling."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from editing import count, rev, transcript


def main(refseq):
    ref,site=transcript(refseq)
    start=site-35
    full=ref[start:site+41]
    intron=b"GTTGGTTA"  # hg38 sequence immediately following the GRIA2 exon.
    assert full[60:68]==b"ATCCCTCT"
    m=bytearray(full)
    m[35]=ord("G")
    edited=bytes(m)
    precursor=full[:60]+intron+full[68:]
    low_center=bytearray(b"I"*len(full))
    low_center[35]=32+30  # Phred 29, below the required 30.
    low_flank=bytearray(b"I"*len(full))
    low_flank[32]=32+20  # Phred 19, below the required 20.
    short=full[23:48]
    genomic_c=full[:35]+b"C"+full[36:]
    reads=[(v,b"I"*len(v)) for v in (full,rev(edited),precursor,rev(precursor),short,genomic_c)]
    reads.extend([(full,bytes(low_center)),(rev(edited),bytes(low_flank[::-1]))])
    with TemporaryDirectory() as temp:
        wd=Path(temp)
        fastq=wd/"SRR1.fastq.gz"
        with gzip.open(fastq,"wb") as out:
            for i,(seq,q) in enumerate(reads):
                out.write(b"@test"+str(i).encode()+b"\n"+seq+b"\n+\n"+q+b"\n")
        manifest=wd/"runs.tsv"
        manifest.write_text("run_accession\tsample_title\tfastq_bytes\tfastq_md5\tread_count\n"
                            +f"SRR1\tWT\t{fastq.stat().st_size}\t{hashlib.md5(fastq.read_bytes()).hexdigest()}\t{len(reads)}\n")
        target=wd/"counts.tsv"
        count(SimpleNamespace(refseq=refseq,manifest=manifest,fastq=fastq,output=target))
        with target.open() as f:
            got={r["category"]:tuple(int(r[b]) for b in "AGCTN") for r in csv.DictReader(f,delimiter="\t")}
        expected={"primary":(4,1,1,0,0),"flank18":(3,1,1,0,0),"interior20":(3,1,1,0,0),
                  "splice8":(1,1,1,0,0),"low_quality":(1,1,0,0,0)}
        assert got==expected,(got,expected)
    print("Verified 8 known-answer reads in all five counting categories.")


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("refseq",type=Path)
    main(p.parse_args().refseq)
