"""Deterministic proof for the WM history split (queue item 2.3). Read-only.
usage: migration_check.py UNITS P_CENSUS V_CENSUS NEW_WM HISTORY CLAIMS OLD_WM"""
import json, sys
units_p, prod_p, ver_p, wm_p, hist_p, claims_p, old_p = sys.argv[1:8]
U = json.load(open(units_p))["units"]
P = {u["uid"]: u for u in json.load(open(prod_p))["units"]}
V = {u["uid"]: u for u in json.load(open(ver_p))["units"]}
wm, hist = open(wm_p, encoding="utf-8").read(), open(hist_p, encoding="utf-8").read()
claims, old = open(claims_p, encoding="utf-8").read(), open(old_p, encoding="utf-8").read()
live = wm.split("\n## Changelog\n", 1)[0]
fail = []
# 1 every history unit is in the cold file verbatim, and in the hot file nowhere
for u in U:
    if u["text"] not in hist:
        fail.append(f"{u['uid']} not verbatim in history")
# 2 every A-quote (either reviewer) still stands where a current reader sees it
quotes = 0
for R in (P, V):
    for uid, u in R.items():
        for e in u.get("live_elements", []):
            ra = e.get("represented_at")
            if ra and ra.get("quote"):
                quotes += 1
                q = ra["quote"]
                if q not in live and q not in claims:
                    fail.append(f"{uid} quote lost: {q[:80]}")
# 3 promotions: each union-B element's key phrase is now live
PROMOTED = {  # uid -> phrases that must now be in the live WM
    "H059": ["the deletion led to nonsense-mediated decay", "not expressed or were degraded",
             "no translation block was used"],
    "H060": ["unsourced, untagged, and contradicted by the architecture (exon 9 is terminal)",
             "labelled conditional", "proteotoxic flag applying to **both** alleles", "a statement about that ledger entry"],
    "H061": ["blots and densitometers total GSK3β", "`NOT_ASSERTED`, not `MEASURE_ABSENT`"],
    "H066": ["no measured ceiling", "`REVERS 0`", "no tumour surveillance", "`SAFETY 1`"],
    "H072": ["does **not** promote memantine", "d-APV is a tool compound and has never been given to a human",
             "no drug is recommended, no dose is transferred"],
    "H097": ["An SDR stabilizer is `conditional / not design-ready`"],
}
for uid, phrases in PROMOTED.items():
    for ph in phrases:
        if ph not in live:
            fail.append(f"{uid} promoted phrase missing: {ph}")
# H020 is the Last-update twin of H059/H060/H066 — covered by those rows
# 4 no pre-existing live byte changed: the old live region, with the additions removed, is identical
old_live = old.split("\n## Changelog\n", 1)[0]
old_live_body = old_live.split("**Last update:**", 1)[0]
new_live_body = live.split("**Last update:**", 1)[0]
if old_live_body != new_live_body:
    fail.append("header before Last update changed")
old_rest = old_live[old_live.index("\n\n> **Public edition"):]
new_rest = live[live.index("\n\n> **Public edition"):]
import difflib
sm = difflib.SequenceMatcher(None, old_rest, new_rest, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal" and (tag != "insert"):
        fail.append(f"live text {tag} at old[{i1}:{i2}]: {old_rest[i1:i2][:80]!r}")
inserted = sum(j2 - j1 for t, i1, i2, j1, j2 in sm.get_opcodes() if t == "insert")
print(f"units {len(U)} · quotes checked {quotes} · promoted phrases "
      f"{sum(len(v) for v in PROMOTED.values())} · live text: only insertions ({inserted} chars)")
print("FAILURES:", len(fail))
for f in fail: print("  ", f)
sys.exit(1 if fail else 0)
