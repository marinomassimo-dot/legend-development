"""ADV-244: stream the first N reads of one ENA fastq.gz and count the reads that span the WWOX exon-1 T run,
by run length. Nothing is stored except the matching reads.

Pattern (PREREG_ADV244): GCTGCGC(T+)ACGCGG, or its reverse complement. Only sequence lines are accepted.

Usage: python3 -I stream_count_adv244.py <https url of fastq.gz> <n_reads> <matched_reads_out.tsv>
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, re, time, urllib.request, zlib

URL, N, OUT = sys.argv[1], int(sys.argv[2]), sys.argv[3]
PAT = re.compile(rb"GCTGCGC(T+)ACGCGG|CCGCGT(A+)GCGCAGC")
req = urllib.request.Request(URL, headers={"User-Agent": "research-data-client"})
dec = zlib.decompressobj(31)
tail = b""
lines = 0
got = 0
seen = set()
counts = collections.Counter()
t0 = time.time()
next_report = 4_000_000
with urllib.request.urlopen(req, timeout=120) as r, open(OUT, "w") as out:
    out.write("read_number\trun_length\torientation\tsequence\n")
    while lines < 4 * N:
        chunk = r.read(1 << 20)
        if not chunk:
            break
        got += len(chunk)
        data = tail
        while chunk:
            data += dec.decompress(chunk)
            chunk = b""
            if dec.eof:
                chunk = dec.unused_data
                dec = zlib.decompressobj(31)
        cut = data.rfind(b"\n") + 1
        data, tail = data[:cut], data[cut:]
        pos, line_at = 0, lines
        for m in PAT.finditer(data):
            line_at += data.count(b"\n", pos, m.start())
            pos = m.start()
            if line_at % 4 != 1 or line_at >= 4 * N or line_at in seen:
                continue
            seen.add(line_at)
            k = len(m.group(1) or m.group(2))
            a = data.rfind(b"\n", 0, m.start()) + 1
            z = data.find(b"\n", m.start())
            counts[k] += 1
            out.write("%d\t%d\t%s\t%s\n" % (line_at // 4 + 1, k, "fwd" if m.group(1) else "rev", data[a:z].decode()))
            out.flush()
        lines += data.count(b"\n")
        if lines // 4 >= next_report:
            print("progress reads=%d compressed_MB=%d s=%d counts=%s" % (lines // 4, got >> 20, time.time() - t0, dict(counts)), flush=True)
            next_report += 4_000_000
print("DONE reads=%d compressed_MB=%d s=%d counts=%s" % (min(lines // 4, N), got >> 20, time.time() - t0, dict(sorted(counts.items()))))
