#!/usr/bin/env python3
"""Minimal pure-Python reader for an R .rds file holding a counts matrix (dense matrix, data.frame, or Matrix::dgCMatrix). No package installed; numpy only. Hypothesis level, read-only.
    python3 read_rds_matrix.py --help
    python3 read_rds_matrix.py describe <file.rds>             # structure, dimensions, first names; prints NO numeric values
    python3 read_rds_matrix.py dump <file.rds> <out.tsv.gz>    # dense genes x samples table, tab separated
Supports XDR serialization version 2 and 3 (gzip, bzip2 or plain). Raises on anything outside the types below."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help") or sys.argv[1] not in ("describe", "dump"):
    print(__doc__); raise SystemExit(0)
import bz2, gzip, struct
import numpy as np

def opener(path):
    with open(path, "rb") as f:
        magic = f.read(3)
    if magic[:2] == b"\x1f\x8b": return gzip.open(path, "rb")
    if magic == b"BZh": return bz2.open(path, "rb")
    return open(path, "rb")

class R:
    def __init__(self, buf): self.b = buf; self.p = 0; self.refs = []
    def i32(self):
        v = struct.unpack(">i", self.b[self.p:self.p + 4])[0]; self.p += 4; return v
    def head(self):
        assert self.b[self.p:self.p + 2] == b"X\n", "not an XDR serialization"
        self.p += 2; ver = self.i32(); self.i32(); self.i32()
        if ver == 3:
            n = self.i32(); self.p += n
        assert ver in (2, 3), ver
    def length(self):
        n = self.i32()
        if n == -1:
            hi = self.i32(); lo = self.i32(); n = (hi << 32) | lo
        return n
    def item(self):
        flags = self.i32(); t = flags & 0xFF; has_attr = bool(flags & 512); has_tag = bool(flags & 1024)
        if t == 254: return None                       # NULL
        if t in (242, 241, 251, 252, 253, 247): return ("special", t)
        if t == 255:                                   # reference
            idx = flags >> 8
            if idx == 0: idx = self.i32()
            return self.refs[idx - 1]
        if t == 1:                                     # symbol
            s = self.item(); self.refs.append(s); return s
        if t == 9:                                     # CHARSXP
            n = self.i32()
            if n == -1: return None
            s = self.b[self.p:self.p + n].decode("utf-8", "replace"); self.p += n; return s
        if t == 2:                                     # pairlist
            out = {}; node_flags = flags
            while True:
                attr = self.item() if (node_flags & 512) else None
                tag = self.item() if (node_flags & 1024) else None
                val = self.item()
                out[tag] = val
                nxt = self.i32()
                nt = nxt & 0xFF
                if nt == 254: break
                if nt != 2: self.p -= 4; self.item(); break
                node_flags = nxt
            return out
        if t == 10 or t == 13:                         # logical / integer
            n = self.length(); v = np.frombuffer(self.b, dtype=">i4", count=n, offset=self.p).astype(np.int64); self.p += 4 * n
            data = v
        elif t == 14:                                  # double
            n = self.length(); data = np.frombuffer(self.b, dtype=">f8", count=n, offset=self.p).astype(np.float64); self.p += 8 * n
        elif t == 16:                                  # character vector
            n = self.length(); data = [self.item() for _ in range(n)]
        elif t == 19 or t == 20:                       # list / expression
            n = self.length(); data = [self.item() for _ in range(n)]
        elif t == 25:                                  # S4 object: attributes only
            data = None
        else:
            raise ValueError("unsupported SEXP type %d at offset %d" % (t, self.p))
        attrs = self.item() if has_attr else {}
        return ("obj", t, data, attrs or {})

def get(attrs, name): return attrs.get(name)

def to_matrix(o):
    """Return (matrix float64 [genes x samples] dense, row names, col names, kind)."""
    kind = None
    _, t, data, attrs = o
    if t == 25:                                        # dgCMatrix (column-compressed)
        i = attrs["i"][2]; p = attrs["p"][2]; x = attrs["x"][2]; dim = attrs["Dim"][2]; dn = attrs["Dimnames"][2]
        m = np.zeros((int(dim[0]), int(dim[1])), dtype=np.float64)
        for j in range(int(dim[1])):
            m[i[p[j]:p[j + 1]], j] = x[p[j]:p[j + 1]]
        rn = dn[0][2] if dn and dn[0] else None; cn = dn[1][2] if dn and dn[1] else None
        return m, rn, cn, "dgCMatrix"
    if t in (13, 14) and "dim" in attrs:               # dense matrix, column-major
        dim = attrs["dim"][2]; m = np.asarray(data, dtype=np.float64).reshape((int(dim[1]), int(dim[0]))).T
        dn = attrs.get("dimnames"); rn = dn[2][0][2] if dn and dn[2][0] else None; cn = dn[2][1][2] if dn and dn[2][1] else None
        return m, rn, cn, "matrix"
    if t == 19 and "names" in attrs:                   # data.frame: columns are samples, row.names are genes
        cols = [np.asarray(c[2], dtype=np.float64) for c in data]; m = np.column_stack(cols)
        rnv = attrs.get("row.names"); rn = rnv[2] if rnv and rnv[1] == 16 else None
        return m, rn, attrs["names"][2], "data.frame"
    raise ValueError("object is not a recognised matrix type (SEXP %d)" % t)

buf = opener(sys.argv[2]).read()
r = R(buf); r.head(); obj = r.item()
m, rn, cn, kind = to_matrix(obj)
if sys.argv[1] == "describe":
    print("kind", kind, "shape", m.shape, "rownames", "none" if rn is None else (len(rn), rn[:3]), "colnames", "none" if cn is None else (len(cn), cn[:40]))
else:
    out = gzip.open(sys.argv[3], "wt")
    out.write("gene\t" + "\t".join(cn if cn else ["s%d" % k for k in range(m.shape[1])]) + "\n")
    for k in range(m.shape[0]):
        out.write((rn[k] if rn else "r%d" % k) + "\t" + "\t".join(repr(float(v)) if v != int(v) else str(int(v)) for v in m[k]) + "\n")
    out.close(); print("wrote", sys.argv[3], m.shape)
