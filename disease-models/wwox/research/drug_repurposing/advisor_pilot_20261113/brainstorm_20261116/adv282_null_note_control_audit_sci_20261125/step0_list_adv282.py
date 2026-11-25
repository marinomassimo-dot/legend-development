#!/usr/bin/env python3
"""ADV-282 STEP 0: the 48 queued null notes on today's cards, ordered by HE's consumer_count.py. Run from the repository root.

Ordering rule, fixed before any source was opened: (1) number of units that carry any study named in the row's `source`
field (PMID forms), union over those studies, by consumer_count.py; (2) tracked files that name the assertion id, with
card, view, join, checkpoint and audit files left out (the ADV-281 proxy); (3) id. A row whose source names no PMID
gets 0 on (1) and is ordered by (2).
"""
import csv, glob, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIT281 = HERE.parent / "adv281_null_note_control_audit_sci_20261125"
sys.path[:0] = [str(AUDIT281), "framework/scripts"]
import consumer_count as cc  # noqa: E402
import list_adv281 as L  # noqa: E402

AUDITED = {"DR-A01-003", "DR-A01-004", "DR-A02-002", "DR-A02-009", "DR-E03-001", "DR-H01-003", "DR-L01-001", "DR-M01-001",
           "DR-P11-006", "DR-D01-002", "DA-LC-ATF4-002", "DR-AAV-GLU10-HD", "DR-AAV-GLU10-LD", "DR-P11-004", "DR-H02-019"}
SKIP = ("/view/", "/join/", "/cards/", "checkpoint_sci", "adv281_null_note", "adv282_null_note", "typed_assertions",
        "assertion_pertinence", "assignments/ADV-281", "assignments/ADV-282", "ledger/tasks/")
def pmids(text):
    """7 or 8 digit numbers of a `source` that names a PMID; PMC ids, 8 digit dates and DOI digits are removed first."""
    if "PMID" not in text:
        return []
    clean = re.sub(r"PMC\d+|(?<!\d)202\d[01]\d[0-3]\d(?!\d)|10\.\d{4,9}/\S+", " ", text)
    return sorted(set(re.findall(r"(?<![\d.\-])(\d{7,8})(?![\d\-]|\.\d)", clean)))


def main():
    now = {}
    for card, key, a in L.rows():
        now.setdefault(a["id"], dict(a, _cards=set()))["_cards"].add(card)
    old = {r["id"]: r for r in csv.DictReader((AUDIT281 / "route_hits_adv281.tsv").open(), delimiter="\t", quoting=csv.QUOTE_NONE)}
    screen = {r["id"]: r for r in csv.DictReader((AUDIT281 / "screen_adv281.tsv").open(), delimiter="\t", quoting=csv.QUOTE_NONE)}
    text = lambda a: " || ".join(x for x in (a.get("measured_result_note"), a.get("note")) if x).replace("\t", " ").replace("\n", " ")
    hits = {i for i, a in now.items() if a.get("direction") == "NO_CHANGE" or any(rx.search(text(a)) for rx in L.RX)}
    new_ids = sorted(hits - set(old))
    queued = sorted(i for i, r in screen.items() if r["decision"] == "NULL" and i not in AUDITED)
    gone = [i for i in queued if i not in now]
    changed = [i for i in queued if i in now and text(now[i]) != old[i]["note"]]
    print("new route hits since ADV-281:", new_ids)
    print("queued", len(queued), "gone", gone, "note text changed", changed)
    ids = cc.registry_ids(Path("."))
    units = cc.units(Path("."))
    rows = []
    for i in queued:
        a = now[i]
        src = str(a.get("source", ""))
        keys = pmids(src)
        if not keys:  # a registry id or a bare modern PMID stands for the study
            paper = set(re.findall(r"PAPER \d+", src))
            keys = sorted({k for k, v in ids.items() if k.isdigit() and v & paper} | set(re.findall(r"(?<![\w.\-])([34]\d{7})(?![\w\-])", src)))
        found = cc.consumers(keys, ids, units) if keys else {}
        union = sorted(set().union(*found.values())) if found else []
        files = subprocess.run(["git", "grep", "-l", "-F", "-w", i], capture_output=True, text=True).stdout.split()
        proxy = [f for f in files if not any(s in f for s in SKIP)]
        rows.append((-len(union), -len(proxy), i, keys, len(union), len(proxy), a))
    rows.sort(key=lambda r: r[:3])
    with (HERE / "queue_ordered_adv282.tsv").open("w") as fh:
        fh.write("rank\tincrement\tid\tstudy_pmids\tstudy_consumer_units\tid_files\tcards\tdirection\treading_depth\treceipt\tsource\tnote\n")
        for n, r in enumerate(rows, 1):
            a = r[6]
            c = lambda t: str(t).replace("\t", " ").replace("\n", " ")
            fh.write("\t".join([str(n), str((n - 1) // 8 + 1), r[2], ",".join(r[3]), str(r[4]), str(r[5]), ",".join(sorted(a["_cards"])),
                                c(a.get("direction")), c(a.get("reading_depth", "")), c(a.get("receipt") or a.get("receipt_reference") or ""),
                                c(a.get("source", "")), text(a)]) + "\n")
    for n, r in enumerate(rows, 1):
        print(n, r[2], r[4], r[5], ",".join(r[3])[:60])


if __name__ == "__main__":
    sys.exit(main())
