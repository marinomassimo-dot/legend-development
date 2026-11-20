"""Substring check of quotes against saved source bytes. Usage: python3 -I quote_check.py SPEC.tsv
SPEC.tsv rows: file<TAB>quote. Tags stripped, entities unescaped, thin and no-break spaces folded."""
import html, re, sys
for line in open(sys.argv[1]):
    line = line.rstrip("\n")
    if not line or line.startswith("#"):
        continue
    path, quote = line.split("\t", 1)
    t = open(path, errors="replace").read()
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = re.sub(r"[\s  ]+", " ", t)
    print("FOUND" if quote in t else "MISSING", "|", path.split("/")[-1], "|", quote[:80])
