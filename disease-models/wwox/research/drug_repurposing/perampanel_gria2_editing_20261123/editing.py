"""Count central bases in a RefSeq-anchored GRIA2 window on either strand."""
import argparse
from collections import Counter, defaultdict
import csv
import gzip
import hashlib
from pathlib import Path
import re


COMP = bytes.maketrans(b"ACGTN", b"TGCAN")
BASES = b"AGCTN"


def rev(seq):
    return seq.translate(COMP)[::-1]


def transcript(path):
    gb = path.read_text()
    assert "VERSION     NM_000826.6" in gb
    seq = re.sub(r"[^acgt]", "", gb.split("ORIGIN", 1)[1]).upper().encode()
    start = int(re.search(r"^     CDS\s+(\d+)\.\.",gb,re.M)[1])
    site = start - 1 + 3 * (607-1) + 1
    assert site+1==2135 and seq[site-1:site+2]==b"CAG"
    assert re.search(r"^     exon\s+1789\.\.2159$",gb,re.M)
    return seq, site


def expressions(reference, site, width):
    left=reference[site-width:site]
    right=reference[site+1:site+width+1]
    return re.compile(left+b"[ACGTN]"+right+b"|"+rev(right)+b"[ACGTN]"+rev(left)), left


def records(path):
    # Retain the longest window minus one base between blocks. This keeps
    # whole-genome validation within a few MB without missing boundary hits.
    with gzip.open(path,"rb") as f:
        name, buf, carry, consumed = None, bytearray(), b"", 0
        for line in f:
            if line.startswith(b">"):
                if buf:
                    yield name,carry+bytes(buf).upper(),consumed,len(carry)
                name,buf,carry,consumed=line[1:].strip(),bytearray(),b"",0
                continue
            buf.extend(line.strip())
            if len(buf)>=2**20:
                chunk=carry+bytes(buf).upper()
                yield name,chunk,consumed,len(carry)
                consumed+=len(buf)
                buf.clear()
                carry=chunk[-36:]
        if buf:
            yield name,carry+bytes(buf).upper(),consumed,len(carry)


def check_reference(args):
    ref,site=transcript(args.refseq)
    with args.output.open("w") as out:
        print("width\trecord\tgene\tcenter_1based\tstrand\tbase",file=out)
        for header,seq,consumed,overlap in records(args.fasta):
            symbol=re.search(rb" gene_symbol:(\S+)",header)
            for w in [12,18]:
                regex,left=expressions(ref,site,w)
                for m in regex.finditer(seq):
                    if m.end() <= overlap:
                        continue
                    fwd=m.group().startswith(left)
                    base=m.group()[w:w+1]
                    print(w,header.split()[0].decode(),symbol[1].decode() if symbol else "NA",
                          consumed-overlap+m.start()+w+1,"+" if fwd else "-",(base if fwd else rev(base)).decode(),sep="\t",file=out)


def count(args):
    ref,site=transcript(args.refseq)
    w=12
    regex,left=expressions(ref,site,w)
    counters=defaultdict(Counter)
    offsets=defaultdict(set)
    total=0
    run=args.fastq.name.removesuffix(".fastq.gz")
    with args.manifest.open() as f:
        entries={r["run_accession"]:r for r in csv.DictReader(f,delimiter="\t")}
    expected=entries[run]
    assert int(expected["fastq_bytes"])==args.fastq.stat().st_size
    with args.fastq.open("rb") as f:
        assert hashlib.file_digest(f,"md5").hexdigest()==expected["fastq_md5"]
    with gzip.open(args.fastq,"rb") as f:
        for header in f:
            seq=f.readline().rstrip()
            sep=f.readline()
            qual=f.readline().rstrip()
            if not header.startswith(b"@") or not sep.startswith(b"+") or len(seq)!=len(qual) or not seq:
                raise ValueError(f"Invalid FASTQ entry near {total+1}")
            total+=1
            m=regex.search(seq)
            if not m:
                continue
            if regex.search(seq,m.end()):
                raise ValueError("Multiple target hits in one read")
            pos=m.start()+w
            if not m.group().startswith(left):
                seq,qual,pos=rev(seq),qual[::-1],len(seq)-pos-1
            base=chr(seq[pos])
            if qual[pos]<63 or min(qual[pos-w:pos+w+1])<53:
                counters["low_quality"][base]+=1
                continue
            def record(category):
                counters[category][base]+=1
                # Orient starts by transcript. Offsets show collision/sampling,
                # not the number of independent molecules in non-UMI data.
                offsets[category,base].add(pos)
            record("primary")
            if min(pos,len(seq)-pos-1)>=20:
                record("interior20")
            if pos>=18 and len(seq)-pos-1>=18 and seq[pos-18:pos]==ref[site-18:site] and seq[pos+1:pos+19]==ref[site+1:site+19] and min(qual[pos-18:pos+19])>=53:
                record("flank18")
            # Site = 2135. Exon ends at 2159. Require exact agreement through
            # 2167 and Q20 along this span to support the known splice junction.
            after=2159+8-(site+1)
            if seq[pos+1:pos+after+1] ==ref[site+1:site+after+1] and min(qual[pos+1:pos+after+1])>=53:
                record("splice8")
    if total!=int(expected["read_count"]):
        raise ValueError(f"Read count {total} differs from ENA declaration")
    tmp=args.output.with_suffix(".partial")
    with tmp.open("w") as out:
        print("run\tgroup\tcategory\tread_total\tA\tG\tC\tT\tN\tA_distinct_offset\tG_distinct_offset",file=out)
        for key in ["primary","flank18","interior20","splice8","low_quality"]:
            print(run,"KO" if "KO" in expected["sample_title"] else "WT",key,total,
                  *(counters[key][chr(b)] for b in BASES),len(offsets[key,"A"]),len(offsets[key,"G"]),sep="\t",file=out)
    tmp.replace(args.output)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    subs=parser.add_subparsers(dest="command",required=True)
    for name,args_list in [("reference",["refseq","fasta","output"]),("count",["refseq","manifest","fastq","output"])]:
        sub=subs.add_parser(name)
        for key in args_list:
            sub.add_argument(key,type=Path)
    args=parser.parse_args()
    (check_reference if args.command=="reference" else count)(args)
