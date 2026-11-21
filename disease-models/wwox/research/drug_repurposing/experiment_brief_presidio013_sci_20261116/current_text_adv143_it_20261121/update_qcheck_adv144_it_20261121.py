"""Recompute QCHECK.tsv from the markers of the current text after the ADV-144 integration (IT, 2026-11-21).
A question with an OPEN-GAP marker keeps the open status of that marker's owner; a question with only a design-team answer is
ANSWERED_IN_TEXT (computed, stated in a source, confirmed) or ANSWERED_BY_RULE_INFERENCE (an inferred rule). Rows for the
second-reader markers (R2...) are added. Prints the totals. Idempotent."""
import csv
import re
from pathlib import Path

H = Path(__file__).resolve().parent
t = (H / "PUP_BRIEF_CURRENT_IT_20261121.md").read_text(encoding="utf-8")
body = t[:t.index("## History (old text kept)")]
open_ = {m.group(1): m.group(2) for m in re.finditer(r"\*\*OPEN-GAP ([A-Z0-9]+) \(owner (\w+)\)", body)}
ans = {}
for m in re.finditer(r"\[Design-team answer ([^,]+), 2026-11-21; status: ([^.]*)\.", body):
    for i in m.group(1).split("/"):
        ans.setdefault(i, m.group(2))
rows = list(csv.DictReader(open(H / "QCHECK.tsv", encoding="utf-8", newline=""), delimiter="\t"))
have = {r["q_id"] for r in rows}
for k, own in open_.items():
    if k.startswith(("R2", "R3")) and k not in have:
        rows.append({"q_id": k, "where_answered_or_gap": "marker added after the second or third cold read", "status": "", "note": "reader gap"})
OWN = {"SCI": "OPEN_GAP_SCI", "laboratory": "OPEN_GAP_LABORATORY", "operator": "OPEN_GAP_OPERATOR"}
for r in rows:
    q = r["q_id"]
    if q in open_:
        r["status"] = OWN[open_[q]]
        if q in ans and "design-team answer" not in r["note"]:
            r["note"] += "; design-team answer integrated 2026-11-21 (" + ans[q] + "); the remaining question is open"
    elif q in ans:
        lab = ans[q]
        r["status"] = "PARTLY_ANSWERED_REMAINDER_UNDER_ANOTHER_ID" if lab.startswith("partly closed") else ("ANSWERED_BY_RULE_INFERENCE" if "INFERENCE" in lab else "ANSWERED_IN_TEXT")
        if "design-team answer" not in r["note"]:
            r["note"] += "; design-team answer integrated 2026-11-21 (" + lab + ")"
with open(H / "QCHECK.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, ["q_id", "where_answered_or_gap", "status", "note"], delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
from collections import Counter
print(len(rows), dict(Counter(r["status"] for r in rows)))
print("OPEN-GAP markers in the body by owner:", dict(Counter(open_.values())), "total", len(open_))
print("CONFLICT-OPEN markers in the body:", len(re.findall(r"\*\*CONFLICT-OPEN ", body)), "| design-team answers integrated:", len(re.findall(r"\[Design-team answer", body)))
