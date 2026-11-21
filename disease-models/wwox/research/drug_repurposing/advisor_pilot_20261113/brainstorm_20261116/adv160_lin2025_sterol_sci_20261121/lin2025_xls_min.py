"""Minimal stdlib reader for BIFF8 .xls (OLE2): sheets -> cell dicts. Written for ADV-160; values only."""
import struct, sys, json

def ole_stream(data, name):
    hdr = data[:512]
    ssz = 1 << struct.unpack_from("<H", hdr, 30)[0]
    mssz = 1 << struct.unpack_from("<H", hdr, 32)[0]
    nfat, dirstart, cutoff, minifat_start, nminifat, difstart, ndif = struct.unpack_from("<I", hdr, 44)[0], struct.unpack_from("<I", hdr, 48)[0], struct.unpack_from("<I", hdr, 56)[0], struct.unpack_from("<I", hdr, 60)[0], struct.unpack_from("<I", hdr, 64)[0], struct.unpack_from("<I", hdr, 68)[0], struct.unpack_from("<I", hdr, 72)[0]
    difat = list(struct.unpack_from("<109I", hdr, 76))
    sec = lambda n: data[512 + n * ssz: 512 + (n + 1) * ssz]
    d = difstart
    for _ in range(ndif):
        s = sec(d); vals = struct.unpack("<%dI" % (ssz // 4), s); difat += list(vals[:-1]); d = vals[-1]
    fat = []
    for f in difat:
        if f >= 0xFFFFFFFA: continue
        fat += list(struct.unpack("<%dI" % (ssz // 4), sec(f)))
    def chain(start, table):
        out = []; n = start
        while n < 0xFFFFFFFA and len(out) < 100000: out.append(n); n = table[n]
        return out
    dirdata = b"".join(sec(n) for n in chain(dirstart, fat))
    ents = []
    for i in range(len(dirdata) // 128):
        e = dirdata[i * 128:(i + 1) * 128]
        nl = struct.unpack_from("<H", e, 64)[0]
        nm = e[:max(nl - 2, 0)].decode("utf-16le", "ignore")
        typ = e[66]; start = struct.unpack_from("<I", e, 116)[0]; size = struct.unpack_from("<I", e, 120)[0]
        ents.append((nm, typ, start, size))
    root = ents[0]
    mini = b"".join(sec(n) for n in chain(root[2], fat))
    minifat = []
    for n in chain(minifat_start, fat): minifat += list(struct.unpack("<%dI" % (ssz // 4), sec(n)))
    for nm, typ, start, size in ents:
        if nm == name and typ == 2:
            if size < cutoff:
                return b"".join(mini[n * mssz:(n + 1) * mssz] for n in chain(start, minifat))[:size]
            return b"".join(sec(n) for n in chain(start, fat))[:size]
    raise KeyError(name)

def rk(v):
    if v & 2: x = float(struct.unpack("<i", struct.pack("<I", v))[0] >> 2)
    else: x = struct.unpack("<d", struct.pack("<Q", (v & 0xFFFFFFFC) << 32))[0]
    return x / 100 if v & 1 else x

def read(path):
    data = open(path, "rb").read()
    try: wbk = ole_stream(data, "Workbook")
    except KeyError: wbk = ole_stream(data, "Book")
    recs = []; p = 0
    while p + 4 <= len(wbk):
        t, l = struct.unpack_from("<HH", wbk, p); recs.append((t, wbk[p + 4:p + 4 + l])); p += 4 + l
    # merge CONTINUE (0x3C) into previous for SST
    sst = []; sheets = []; cur = None; out = {}
    i = 0
    while i < len(recs):
        t, b = recs[i]
        if t == 0x00FC:  # SST
            full = bytearray(b); j = i + 1; segs = [len(b)]
            while j < len(recs) and recs[j][0] == 0x3C: full += recs[j][1]; segs.append(len(recs[j][1])); j += 1
            bounds = []; acc = 0
            for s in segs: acc += s; bounds.append(acc)
            n = struct.unpack_from("<I", full, 4)[0]; q = 8
            for _ in range(n):
                if q >= len(full): break
                cc = struct.unpack_from("<H", full, q)[0]; fl = full[q + 2]; q += 3
                rt = 0; ex = 0
                if fl & 8: rt = struct.unpack_from("<H", full, q)[0]; q += 2
                if fl & 4: ex = struct.unpack_from("<I", full, q)[0]; q += 4
                chars = []; need = cc; wide = fl & 1
                while need > 0:
                    nxt = min([bb for bb in bounds if bb > q] or [len(full)])
                    avail = (nxt - q) // (2 if wide else 1)
                    take = min(need, avail) if avail > 0 else need
                    nb = take * (2 if wide else 1)
                    chars.append(bytes(full[q:q + nb]).decode("utf-16le" if wide else "latin-1", "ignore")); q += nb; need -= take
                    if need > 0 and q in bounds: wide = full[q] & 1; q += 1
                q += rt * 4 + ex
                sst.append("".join(chars))
            i = j; continue
        if t == 0x0085: 
            off = struct.unpack_from("<I", b, 0)[0]; nl = b[6]; fl = b[7]
            nm = b[8:8 + nl * (2 if fl & 1 else 1)].decode("utf-16le" if fl & 1 else "latin-1", "ignore")
            sheets.append((off, nm))
        i += 1
    # cells: re-walk by absolute offset
    offs = sorted(sheets)
    for off, nm in sheets:
        cells = {}; p = off; started = False
        while p + 4 <= len(wbk):
            t, l = struct.unpack_from("<HH", wbk, p); b = wbk[p + 4:p + 4 + l]; p += 4 + l
            if t == 0x0809:
                if started: break
                started = True; continue
            if t == 0x000A: break
            if t == 0x00FD: r, c, x, k = struct.unpack_from("<HHHI", b, 0); cells[(r, c)] = sst[k]
            elif t == 0x0203: r, c, x = struct.unpack_from("<HHH", b, 0); cells[(r, c)] = struct.unpack_from("<d", b, 6)[0]
            elif t == 0x027E: r, c, x, v = struct.unpack_from("<HHHI", b, 0); cells[(r, c)] = rk(v)
            elif t == 0x00BD:
                r, c0 = struct.unpack_from("<HH", b, 0); n = (l - 6) // 6
                for k in range(n): cells[(r, c0 + k)] = rk(struct.unpack_from("<I", b, 4 + 6 * k + 2)[0])
            elif t == 0x0204 or t == 0x0004:
                r, c, x, ln = struct.unpack_from("<HHHH", b, 0); cells[(r, c)] = b[8:8 + ln].decode("latin-1", "ignore")
            elif t == 0x0006:
                r, c, x = struct.unpack_from("<HHH", b, 0)
                if b[12:14] != b"\xff\xff": cells[(r, c)] = struct.unpack_from("<d", b, 6)[0]
        out[nm] = cells
    return out

if __name__ == "__main__":
    wb = read(sys.argv[1])
    for nm, cells in wb.items():
        rs = [r for r, c in cells]; cs = [c for r, c in cells]
        print(nm, "rows", (max(rs) + 1 if rs else 0), "cols", (max(cs) + 1 if cs else 0), "cells", len(cells))
