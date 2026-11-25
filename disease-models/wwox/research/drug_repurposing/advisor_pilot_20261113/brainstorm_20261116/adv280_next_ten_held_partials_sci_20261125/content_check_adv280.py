"""ADV-280: which held files are not what their name says (error page, empty file, HTML stub, broken archive).

Usage: python3 content_check_adv280.py <root checkout> <out tsv>
Read-only; no network. A file is defective when it is empty, when its first bytes contradict its
extension, when an XML/CSV/text file is an HTML document or an error document, or when a zip-based
container fails its own CRC test.
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import csv, os, re, zipfile

held, out = sys.argv[1:3]
SEALED = ("adv174", "adv175")
SKIP = ("/check_runs", "/coordination", "/retraction_watch")
ZIPS = ("zip", "xlsx", "docx", "pptx")
HTMLISH = re.compile(rb"^\s*(?:<!--.*?-->\s*)*<(?:!doctype\s+html|html[\s>])", re.I | re.S)
ERRXML = re.compile(rb"<(?:error|errorresult)[\s>]|<title>\s*(?:40\d|50\d|access denied|just a moment)", re.I)


def verdict(path):
    ext = path.rsplit(".", 1)[-1].lower()
    if os.path.getsize(path) == 0:
        return "empty"
    with open(path, "rb") as handle:
        head = handle.read(4096)
    body = head.lstrip(b"\xef\xbb\xbf")
    html = bool(HTMLISH.match(body))
    magic = {"png": (b"\x89PNG",), "jpg": (b"\xff\xd8\xff",), "jpeg": (b"\xff\xd8\xff",), "gif": (b"GIF8",),
             "tif": (b"II*\x00", b"MM\x00*"), "tiff": (b"II*\x00", b"MM\x00*"), "webp": (b"RIFF",),
             "xls": (b"\xd0\xcf\x11\xe0", b"PK"), "doc": (b"\xd0\xcf\x11\xe0", b"PK", b"{\\rtf")}
    if ext in magic:
        if body.startswith(magic[ext]):
            return ""
        return "html_page_under_%s_name" % ext if html else "wrong_magic_for_%s" % ext
    if ext == "pdf":
        if b"%PDF" in head[:1024]:
            return ""
        return "html_page_under_pdf_name" if html else "wrong_magic_for_pdf"
    if ext in ZIPS:
        if html:
            return "html_page_under_%s_name" % ext
        try:
            with zipfile.ZipFile(path) as z:
                return "broken_archive" if z.testzip() else ""
        except Exception:
            return "broken_archive"
    if ext in ("xml", "csv", "tsv", "txt", "json"):
        if ext == "xml" and html and b"<article" not in head:
            return "html_page_under_xml_name"
        if ext != "xml" and html:
            return "html_page_under_%s_name" % ext
        if os.path.getsize(path) < 600 and ERRXML.search(body):
            return "error_document"
        return ""
    if ext in ("html", "htm"):
        if os.path.getsize(path) < 600 or re.search(rb"<title>\s*(?:40\d|50\d|access denied|just a moment|error)", head, re.I):
            return "error_or_stub_html"
    return ""


rows, total = [], 0
for d, sub, names in os.walk(os.path.join(held, "files")):
    sub[:] = [s for s in sub if not s.startswith(SEALED)]
    if any(x in d for x in SKIP):
        continue
    for n in names:
        p = os.path.join(d, n)
        if not os.path.isfile(p):
            continue
        total += 1
        v = verdict(p)
        if v:
            rows.append({"path": os.path.relpath(p, held), "bytes": os.path.getsize(p), "defect": v})
rows.sort(key=lambda r: r["path"])
with open(out, "w") as handle:
    writer = csv.DictWriter(handle, fieldnames=["path", "bytes", "defect"], delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("held files checked:", total, "| defective:", len(rows))
import collections
for k, v in sorted(collections.Counter(r["defect"] for r in rows).items()):
    print(" ", k, v)
