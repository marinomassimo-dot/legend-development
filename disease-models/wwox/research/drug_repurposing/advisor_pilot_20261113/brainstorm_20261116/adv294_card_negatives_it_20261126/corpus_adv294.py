"""ADV-294: extract the text of the held originals (read only) and search it.
build:  python3 -I corpus_adv294.py build <root-checkout> <out-dir>
near:   python3 -I corpus_adv294.py near <out-dir> <regexA> <regexB> [window]   (files and hit counts)
show:   python3 -I corpus_adv294.py show <out-dir> <regexA> <regexB> <file-substring> [n]
The index maps each text file to its source path. Downloaded bytes are only read, never executed."""
import hashlib, html, io, json, os, re, subprocess, sys, zipfile

TEXT = (".txt", ".csv", ".tsv", ".json", ".md")
MARKUP = (".xml", ".html", ".htm")

def strip(s):
    s = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(s)

def pdf(data):
    p = subprocess.run(["pdftotext", "-q", "-", "-"], input=data, capture_output=True, timeout=180)
    return p.stdout.decode("utf-8", "replace")

def office(data):
    out = []
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for n in z.namelist():
            if n.endswith(".xml") and ("sharedStrings" in n or "worksheets/" in n or n.startswith("word/") or n.startswith("ppt/slides/")):
                x = z.read(n).decode("utf-8", "replace")
                out.append(strip(x.replace("</w:p>", "\n").replace("</row>", "\n").replace("</si>", "\n")))
    return "\n".join(out)

def extract(name, data, depth=0):
    low = name.lower()
    if low.endswith(TEXT):
        return data.decode("utf-8", "replace")
    if low.endswith(MARKUP):
        return strip(data.decode("utf-8", "replace"))
    if low.endswith(".pdf"):
        return pdf(data)
    if low.endswith((".xlsx", ".docx", ".pptx")):
        return office(data)
    if low.endswith(".zip") and depth < 2:
        out = []
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for i in z.infolist():
                if i.file_size < 40_000_000:
                    t = extract(i.filename, z.read(i), depth + 1)
                    if t:
                        out.append(f"\n[member {i.filename}]\n{t}")
        return "".join(out)
    return None

def build(root, out):
    os.makedirs(out, exist_ok=True)
    index, skipped = {}, []
    tops = ["files/fulltext", "files/supplement", "files/supplements", "disease-models/wwox/research/deepdive_manifests"]
    paths = []
    for t in tops:
        for d, _, fs in os.walk(os.path.join(root, t)):
            paths += [os.path.join(d, f) for f in fs]
    import glob
    paths += glob.glob(os.path.join(root, "disease-models/wwox/registries/*.md"))
    paths += glob.glob(os.path.join(root, "disease-models/wwox/registries/*.json*"))
    for p in paths:
        rel = os.path.relpath(p, root)
        try:
            if os.path.getsize(p) > 80_000_000:
                skipped.append((rel, "size")); continue
            t = extract(p, open(p, "rb").read())
        except Exception as e:
            skipped.append((rel, type(e).__name__)); continue
        if t is None:
            skipped.append((rel, "type")); continue
        if len(t.strip()) < 20:
            skipped.append((rel, "no_text")); continue
        key = hashlib.sha1(rel.encode()).hexdigest()[:16] + ".txt"
        open(os.path.join(out, key), "w").write(re.sub(r"[ \t]+", " ", t))
        index[key] = rel
    json.dump(index, open(os.path.join(out, "index.json"), "w"))
    json.dump(skipped, open(os.path.join(out, "skipped.json"), "w"))
    from collections import Counter
    print("indexed", len(index), "skipped", len(skipped), Counter(w for _, w in skipped))

def hits(out, a, b, window):
    index = json.load(open(os.path.join(out, "index.json")))
    ra, rb = re.compile(a, re.I), re.compile(b, re.I)
    for key, rel in sorted(index.items(), key=lambda kv: kv[1]):
        s = open(os.path.join(out, key)).read()
        pa = [m.start() for m in ra.finditer(s)]
        if not pa:
            continue
        import bisect
        got = []
        for m in rb.finditer(s):
            i = bisect.bisect_left(pa, m.start() - window)
            if i < len(pa) and pa[i] <= m.start() + window:
                got.append((m.start(), pa[i]))
        if got:
            yield rel, s, got

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "build":
        build(sys.argv[2], sys.argv[3])
    elif cmd == "near":
        w = int(sys.argv[5]) if len(sys.argv) > 5 else 400
        tot = files = 0
        for rel, _, got in hits(sys.argv[2], sys.argv[3], sys.argv[4], w):
            print(len(got), rel); files += 1; tot += len(got)
        print("== files", files, "hits", tot)
    elif cmd == "show":
        n = int(sys.argv[6]) if len(sys.argv) > 6 else 3
        for rel, s, got in hits(sys.argv[2], sys.argv[3], sys.argv[4], 400):
            if sys.argv[5] not in rel:
                continue
            last = -10**9
            shown = 0
            for pos, _ in got:
                if pos - last < 500:
                    continue
                last = pos; shown += 1
                print(f"--- {rel} @{pos}\n" + " ".join(s[max(0, pos - 300): pos + 300].split()))
                if shown >= n:
                    break
