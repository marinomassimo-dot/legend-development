"""ADV-294: card sentences that mention WWOX/Q230P and carry a negative, ranked as the PREREG states.
Usage (from the repository root): python3 <this file> > universe_adv294.tsv"""
import glob, html, json, os, re, subprocess, sys

D = "disease-models/wwox/research/drug_repurposing"
MENTION = re.compile(r"wwox|q230p|gln230pro", re.I)
NEG = re.compile("|".join([
    r"unmeasured",
    r"\b(not|never) (been )?(measured|held|read|tested|assessed|examined|established|determined|studied|reported|known)\b",
    r"\buntested\b", r"\bunknown\b", r"\bunread\b",
    r"\bno (held |direct |measured |published )?(measurement|datum|data|record|study|reading|source|test|result|report|assay|value|evidence)\b",
    r"\b(none|nothing) (is |was )?(held|measured|read|tested|known)\b",
    r"\bhas no (held )?(measurement|datum|data)\b",
    r"\bno [^.;]{0,60} (is|are|was|were|has been|have been) (held|measured|reported|known|tested)\b",
]), re.I)

def strings(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from strings(v, f"{path}.{k}" if path else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from strings(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o

def sentences(s):
    return [x.strip() for x in re.split(r"(?<=\.)\s+|\n+", s) if x.strip()]

def rendered(sent, pages):
    key = sent.rstrip(".")[:120]
    return key in pages

def page_text(paths):
    out = []
    for p in paths:
        out.append(open(p, encoding="utf-8", errors="replace").read())
    return "\n".join(out)

rows = []
for p in sorted(glob.glob(f"{D}/cards/*.packet.json")):
    stem = os.path.basename(p)[: -len(".packet.json")]
    seen = set()
    for order, (path, s) in enumerate(strings(json.load(open(p)))):
        for sent in sentences(s):
            if sent in seen or not (MENTION.search(sent) and NEG.search(sent)):
                continue
            seen.add(sent)
            rows.append((stem, order, path, sent))

consumers = {}
for stem in {r[0] for r in rows}:
    got = subprocess.run(["git", "grep", "-l", "-F", stem, "--", ".", f":(exclude){D}/cards"],
                         capture_output=True, text=True).stdout.split()
    consumers[stem] = len(got)

view = sorted(glob.glob(f"{D}/view/**/*.html", recursive=True) + glob.glob(f"{D}/view/**/*.js", recursive=True)
              + glob.glob(f"{D}/view/**/*.json", recursive=True))
share = [p for p in view if "shareable" in p]
full = [p for p in view if "shareable" not in p]
sys.stderr.write(f"view files: shareable {len(share)} full {len(full)}\n")
share_text, full_text = page_text(share), page_text(full)

def exposure(sent):
    cands = [sent[:100], json.dumps(sent)[1:101], json.dumps(sent, ensure_ascii=False)[1:101],
             sent[:100].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"),
             html.escape(sent[:100]), html.escape(sent[:100], quote=False)]
    if any(c in share_text for c in cands):
        return 0
    if any(c in full_text for c in cands):
        return 1
    return 2

ranked = sorted(rows, key=lambda r: (-consumers[r[0]], r[0], exposure(r[3]), r[1]))
print("rank\tcard\tconsumers\texposure\tfield\tsentence")
for i, (stem, order, path, sent) in enumerate(ranked, 1):
    print(f"{i}\t{stem}\t{consumers[stem]}\t{['shareable','full_only','not_found'][exposure(sent)]}\t{path}\t{sent}")
sys.stderr.write(f"negative sentences with mention: {len(rows)} over {len({r[0] for r in rows})} cards\n")
allneg = 0
for p in glob.glob(f"{D}/cards/*.packet.json"):
    allneg += len({x for _, s in strings(json.load(open(p))) for x in sentences(s) if NEG.search(x)})
sys.stderr.write(f"negative sentences, any mention: {allneg}\n")
