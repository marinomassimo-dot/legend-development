#!/usr/bin/env python3
"""Extract the embedded images of a supplementary .docx so each can be opened as an image.

`docx_to_text.py` lists every embedded image as "not read as text". This is the next step: it
writes each file of `word/media/` unchanged into an output directory and, for an `.emf` file
that no viewer on the host can render, decodes the single uncompressed EMF+ bitmap object it
carries into a PNG (standard library only). Per file it prints name, bytes, SHA-256 and, for a
decoded bitmap, width and height.

Honest limits, stated in the output and never hidden:
  * only an EMF+ bitmap object in pixel format 24bppRGB, 32bppRGB, 32bppARGB or 32bppPARGB is
    decoded; vector EMF (lines and text), compressed bitmaps and other formats are reported
    "not decoded" and left as the unchanged .emf;
  * transparent regions of a decoded bitmap are written as black (the alpha channel is
    dropped), so a figure drawn on a transparent background looks dark where it is empty;
  * the PNG is a derived view: declare it in a manifest as derived from the docx with this
    script as the extractor, and keep the unchanged `.emf` beside it.
"""
import argparse, hashlib, struct, sys, zipfile, zlib
from pathlib import Path

PIXEL_FORMATS = {0x21808: (3, "24bppRGB"), 0x22009: (4, "32bppRGB"), 0x26200A: (4, "32bppARGB"), 0xE200B: (4, "32bppPARGB")}


def emf_plus_bitmap(data: bytes):
    """Return (width, height, rgb_bytes, format_name) for the first EMF+ bitmap object, or None."""
    objs = {}
    off = 0
    while off + 8 <= len(data):
        rtype, size = struct.unpack_from("<II", data, off)
        if size < 8:
            break
        if rtype == 70 and data[off + 12:off + 16] == b"EMF+":  # EMR_COMMENT carrying EMF+ records
            comment_len = struct.unpack_from("<I", data, off + 8)[0]
            p, end = off + 16, off + 12 + comment_len
            while p + 12 <= end:
                rt, fl, rs, ds = struct.unpack_from("<HHII", data, p)
                if rs < 12:
                    break
                if rt == 0x4008 and ((fl >> 8) & 0x7F) == 5:  # EmfPlusObject, object type Image
                    oid, chunk = fl & 0xFF, data[p + 12:p + 12 + ds]
                    if fl & 0x8000:  # continued object: first 4 bytes are the total size
                        objs.setdefault(oid, bytearray()).extend(chunk[4:])
                    else:
                        objs[oid] = bytearray(chunk)
                p += rs
        off += size
    for blob in objs.values():
        if len(blob) < 28 or struct.unpack_from("<I", blob, 4)[0] != 1:  # image type 1 = bitmap
            continue
        w, h, stride, pf, btype = struct.unpack_from("<iiiII", blob, 8)
        if btype != 0 or pf not in PIXEL_FORMATS or w <= 0 or h <= 0:
            continue
        bpp, name = PIXEL_FORMATS[pf]
        if len(blob) < 28 + abs(stride) * h:
            continue
        rgb = bytearray()
        for y in range(h):
            row = blob[28 + y * abs(stride):28 + y * abs(stride) + w * bpp]
            for x in range(w):
                b, g, r = row[x * bpp], row[x * bpp + 1], row[x * bpp + 2]
                rgb += bytes((r, g, b))
        return w, h, bytes(rgb), name
    return None


def png_bytes(w: int, h: int, rgb: bytes) -> bytes:
    def chunk(tag, payload):
        body = tag + payload
        return struct.pack(">I", len(payload)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)
    raw = b"".join(b"\x00" + rgb[y * w * 3:(y + 1) * w * 3] for y in range(h))
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 6)) + chunk(b"IEND", b"")


def extract(docx: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    lines = []
    with zipfile.ZipFile(docx) as z:
        for info in z.infolist():
            if not info.filename.startswith("word/media/") or info.filename.endswith("/"):
                continue
            data = z.read(info.filename)
            name = Path(info.filename).name
            (out / name).write_bytes(data)
            line = f"{name} bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}"
            if name.lower().endswith(".emf"):
                bmp = emf_plus_bitmap(data)
                if bmp:
                    w, h, rgb, fmt = bmp
                    png = out / (Path(name).stem + "_decoded.png")
                    png.write_bytes(png_bytes(w, h, rgb))
                    line += f" decoded={png.name} {w}x{h} {fmt} (alpha dropped, transparent areas black)"
                else:
                    line += " not decoded (no uncompressed EMF+ bitmap of a supported pixel format)"
            lines.append(line)
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("docx", type=Path)
    ap.add_argument("--out", type=Path, required=True, help="output directory (created; existing files are overwritten)")
    a = ap.parse_args(argv)
    lines = extract(a.docx, a.out)
    print(f"DOCX {a.docx.name} media_files={len(lines)}")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
