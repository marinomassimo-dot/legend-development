"""IT59: reading-debt reconciliation with the receipt ledger (2026-11-19). A READING script over existing modules (coverage_report, fulltext_receipts, batch_queue output); it writes two TSVs next to itself and edits no registry.
Run from the repository root:  python3 disease-models/wwox/research/drug_repurposing/generation_it59_20261119/reading_debt_reconcile_it59.py
Categories of the coverage_report 'reading debt' entries (CORPUS records whose effective depth is catalogued):
  A  the paper has a receipt (event id carries its PMID) owned by ANOTHER registry entry: the stub duplicates a processed record;
  D  no receipt and no promoted/resolved pointer: genuinely catalogued as far as the ledger and the registry say."""
import argparse, collections, csv, json, re, subprocess, sys
from pathlib import Path
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Reading debt against the receipt ledger (reading only): classifies the coverage_report reading-debt entries and writes reading_debt_classified_it59.tsv and queue_start_here_with_depth_it59.tsv next to this script. Run from the repository root; no registry is edited.")
    ap.parse_args()
ROOT = Path.cwd(); HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "framework/scripts"))
import coverage_report as C, fulltext_receipts as receipts
entries = C.parse_entries((ROOT / "disease-models/wwox/registries/paper_registry_current.md").read_text(encoding="utf-8"))
ledger = receipts.default_ledger_path(ROOT, "wwox"); idx = receipts.receipt_depth_index(ledger); events = receipts.load_ledger(ledger)
owners = C.receipt_owners(entries, idx); byid = {e["_id"]: e for e in entries}
debt = [e for e in entries if C.effective_depth(e, owners.get(e["_id"])) == "catalogued"]
evpm = collections.defaultdict(list)
for ev in events:
    m = re.match(r"FTR-\d{8}-(\d+)-", ev["event_id"])
    if m and ev["record_kind"] in ("contemporaneous_receipt", "legacy_reconstruction"): evpm[m.group(1)].append(ev)
ownerof = {rc["event_id"]: oid for oid, rc in owners.items()}
rows = []
for e in debt:
    ps = C.PMID.findall(e.get("identifier", "")); rec = [ev for p in ps for ev in evpm.get(p, [])]
    own = None
    if rec:
        keys = [f"pmid:{p}" for p in ps if f"pmid:{p}" in idx]
        own = ownerof.get(idx[keys[0]]["event_id"]) if keys else None
    rows.append(dict(id=e["_id"], cat="A" if rec else "D", pmid=";".join(ps), status=e.get("status", "")[:70],
                     receipt_depth=max((ev["evidence_depth"] for ev in rec), key=lambda d: receipts.DEPTHS[d]) if rec else "",
                     receipt_owner=own or "", owner_status=byid[own].get("status", "")[:30] if own else "", title=(e.get("short title") or e.get("full title") or "")[:90]))
with open(HERE / "reading_debt_classified_it59.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
q = json.loads(subprocess.run(["python3", "framework/scripts/batch_queue.py", "--disease", "wwox", "--json"], capture_output=True, text=True, check=True).stdout)["queue"]
sh = [x for x in q if x["action"].startswith("start here — catalogued")]
mis = [x for x in sh if x["depth"] not in ("catalogued only", "screened")]
with open(HERE / "queue_start_here_with_depth_it59.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["pmid", "depth", "record", "action", "title"])
    for x in mis: w.writerow([x["pmid"], x["depth"], x["record"], x["action"], (x["title"] or "")[:90]])
print("coverage_report debt entries:", len(debt), dict(collections.Counter(r["cat"] for r in rows)))
print("A by receipt depth:", dict(collections.Counter(r["receipt_depth"] for r in rows if r["cat"] == "A")))
print("D by status:", dict(collections.Counter(r["status"][:34] for r in rows if r["cat"] == "D")))
print("queue 'start here - catalogued, never processed':", len(sh), "of which the queue's own depth column is beyond catalogued/screened:", len(mis), dict(collections.Counter(x["depth"] for x in mis)))
