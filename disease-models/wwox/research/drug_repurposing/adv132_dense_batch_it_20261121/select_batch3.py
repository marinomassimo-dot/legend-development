"""ADV-132 selection, as fixed in SELECTION_AND_PROTOCOL_ADV132_IT_20261121.md. Usage: python3 -I select_batch3.py  (from the repository root) -> selected_batch3.json"""
import html, json, re, sys
sys.path.insert(0, "framework/scripts")
sys.path.insert(0, "disease-models/wwox/research/drug_repurposing/adv132_dense_batch_it_20261121")
import repurposing_view as rv
import parity_check as pc
V = "disease-models/wwox/research/drug_repurposing/view/"
WANT = ("overview", "ranking", "hypotheses", "priorities-cur", "priorities", "leads")
scope = set(json.load(open(V + "i18n/en_scope.json")))
page = open(V + "index_shareable.fr.html", encoding="utf-8").read()
masked = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", lambda m: " " * len(m.group(0)), page, flags=re.S)
spans, stack = [], []
for m in rv.SECTION_TAG.finditer(masked):
    if m.group(0).startswith("</"):
        if stack:
            spans.append((*stack.pop(), m.end()))
    else:
        stack.append((m.start(), m.end()))
cands, seen = [], set()
for start, open_end, end in sorted(spans):
    idm = re.search(r'\bid="([^"]+)"', masked[start:open_end])
    sid = idm.group(1) if idm else None
    if sid not in WANT:
        continue
    last = open_end
    own = []
    for a, b in sorted((a, b) for a, _, b in spans if start < a and b < end):
        if a > last:
            own.append((last, a))
        last = max(last, b)
    own.append((last, end - len("</section>")))
    for a, b in own:
        for m in rv.TEXT_NODE.finditer(masked, max(a - 1, 0), b):
            if m.start(1) < a:
                continue
            t = html.unescape(page[m.start(1):m.end(1)]).strip()
            h = rv.text_hash(t)
            if h in scope or h in seen or len(t) < 40 or not rv.english_authored_node(t, "fr"):
                continue
            seen.add(h)
            t2 = re.sub(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b", " ", t)   # rule v2: copied hyphenated capital identifiers are not scored
            sc = sum(pc.numeric_tokens(t2).values()) + sum(pc.symbol_tokens(t2).values())
            cands.append({"sec": sid, "pos": m.start(1), "hash": h, "len": len(t), "score": sc, "text": t})
cands.sort(key=lambda o: (-o["score"], o["pos"], -o["len"]))
top = cands[:25]
for i, o in enumerate(top):
    o["n"] = 51 + i
json.dump(top, open("disease-models/wwox/research/drug_repurposing/adv132_dense_batch_it_20261121/selected_batch3.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("candidates", len(cands), "by section", Counter(o["sec"] for o in cands), "selected by section", Counter(o["sec"] for o in top), "scores", [o["score"] for o in top], "total chars", sum(o["len"] for o in top))
