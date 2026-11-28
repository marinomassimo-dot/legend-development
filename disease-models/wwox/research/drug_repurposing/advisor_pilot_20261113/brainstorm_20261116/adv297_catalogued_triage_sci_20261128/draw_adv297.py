"""ADV-297: seeded draw of ten catalogued-only records with no receipt. Usage, from the repository root: python3 draw_adv297.py SEED
Prints record ids, PMIDs and counts only: no title, no abstract."""
import hashlib, random, re, sys
from pathlib import Path

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print(__doc__)
    raise SystemExit(0 if sys.argv[1:] in (["-h"], ["--help"]) else 2)
sys.path.insert(0, str(Path("framework/scripts").resolve()))
import coverage_report as cov  # noqa: E402
import fulltext_receipts as receipts  # noqa: E402

EXCLUDED = {"42422765"}
root = Path(".").resolve()
papers = (root / "disease-models/wwox/registries/paper_registry_current.md").read_text(encoding="utf-8")
entries = cov.parse_entries(papers)
ledger = receipts.default_ledger_path(root, "wwox")
events = receipts.load_ledger(ledger)
owners = cov.receipt_owners(entries, receipts.receipt_depth_index(ledger))
receipted = set()
for event in events:
    m = re.match(r"FTR-\d{8}-(\d+)-", event.get("event_id", ""))
    if m and event.get("record_kind") in ("contemporaneous_receipt", "legacy_reconstruction"):
        receipted.add(m.group(1))
pool = []
for entry in entries:
    if cov.effective_depth(entry, owners.get(entry["_id"])) != "catalogued":
        continue
    pmids = cov.PMID.findall(entry.get("identifier", ""))
    if any(p in receipted for p in pmids):
        continue
    pool.append((entry["_id"], pmids[0] if pmids else ""))
print("pool_no_receipt", len(pool))
pool = sorted(p for p in pool if p[1] not in EXCLUDED)
print("pool_after_exclusion", len(pool), "without_pmid", sum(1 for p in pool if not p[1]))
print("pool_sha256", hashlib.sha256("\n".join("%s\t%s" % p for p in pool).encode()).hexdigest())
for rank, (rid, pmid) in enumerate(random.Random(int(sys.argv[1])).sample(pool, 10), 1):
    print("draw", rank, rid, pmid or "-", sep="\t")
