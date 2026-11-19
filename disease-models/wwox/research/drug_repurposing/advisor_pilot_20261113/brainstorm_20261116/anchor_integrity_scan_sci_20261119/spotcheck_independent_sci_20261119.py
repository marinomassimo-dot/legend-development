"""Independent spot-check of the anchor scan (PREREG section 8): seed 20261119, 10 anchor rows (A1/A2) drawn from anchors_by_claim_scan_sci_20261119.tsv.
Does NOT import the tool modules (trace_claim_foundation, coverage_report, fulltext_receipts): raw registry text and raw ledger lines only.
Run:  python3 -I spotcheck_independent_sci_20261119.py <repository-root>"""
import csv, json, random, re, sys
from pathlib import Path

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
R = Path(sys.argv[1]).resolve(); HERE = Path(__file__).resolve().parent
reg = (R / "disease-models/wwox/registries/paper_registry_current.md").read_text(encoding="utf-8")
claims = (R / "disease-models/wwox/registries/claim_registry_current.md").read_text(encoding="utf-8")
events = [json.loads(l) for l in open(R / "disease-models/wwox/registries/fulltext_read_receipts.jsonl", encoding="utf-8") if l.strip()]
RANK = {"retrieved_not_read": 0, "queried_not_full_read": 1, "abstract_only": 2, "partial_fulltext_read": 3, "complete_fulltext_read": 4}
withdrawn = {e.get("invalidates_receipt") for e in events} | {e.get("corrects_receipt") for e in events}
withdrawn.discard(None)
active = [e for e in events if e.get("record_kind") != "receipt_invalidation" and e["event_id"] not in withdrawn]


def block(text, heading):
    m = re.search(r"^## " + re.escape(heading) + r"\s*$", text, re.M)
    if not m:
        return None
    n = re.search(r"^## ", text[m.end():], re.M)
    return text[m.end(): m.end() + n.start()] if n else text[m.end():]


def field(b, name):
    m = re.search(r"^\*\*" + re.escape(name) + r":\*\*\s*(.*)$", b, re.M | re.I)
    return m.group(1).strip() if m else ""


rows = [r for r in csv.DictReader(open(HERE / "anchors_by_claim_scan_sci_20261119.tsv", encoding="utf-8"), delimiter="\t") if r["cls"] in ("A1", "A2")]
rows.sort(key=lambda r: (r["claim"], r["anchor"]))
random.seed(20261119)
sample = random.sample(rows, 10)
ok_all = True
for r in sample:
    b = block(reg, r["anchor"]) or ""
    ident = field(b, "Identifier")
    pm = sorted(set(re.findall(r"\bPMID\s*(\d{7,8})\b", ident)))
    dois = sorted(set(d.lower().rstrip(".,;)") for d in re.findall(r"\b10\.\d{4,9}/[^\s,;)]+", ident)))
    if not pm and not dois:
        lvl = "no_identifier" if r["anchor"].startswith("PAPER") else "placeholder"
        ev_ids = []
    else:
        mine = [e for e in active if (str(e["study_id"].get("pmid") or "") in pm) or (e["study_id"].get("doi", "") or "").lower() in dois]
        ev_ids = [e["event_id"] for e in mine]
        if not mine:
            lvl = "none"
        else:
            best = max(mine, key=lambda e: RANK[e["evidence_depth"]])
            d = best["evidence_depth"]
            if d == "complete_fulltext_read":
                # strict: any complete receipt that passes the strict coverage test, taking the deepest one the tool would pick is not needed for level
                def strict(e):
                    c = e.get("coverage") or {}
                    return c.get("results") == "read" and all(c.get(k) in ("read", "not_present") for k in ("abstract", "introduction", "methods", "discussion"))
                comp = [e for e in mine if e["evidence_depth"] == "complete_fulltext_read"]
                lvl = "complete_strict" if any(strict(e) for e in comp) else "complete_loose"
            else:
                lvl = {"partial_fulltext_read": "partial", "abstract_only": "abstract_only"}.get(d, "not_read")
    # link check
    num = r["claim"].split()[-1]
    if r["edge"] == "claim_links":
        cl = field(b, "Claim links")
        head = re.split(r"\(|\s[—–]\s|`", cl)[0]
        link_ok = (not cl.lower().startswith("none")) and num in re.findall(r"\b(\d{3})\b", head)
    elif r["edge"] == "source_field":
        cb = block(claims, r["claim"]) or ""
        link_ok = bool(pm) and pm[0] in re.findall(r"PMID\s*(\d{7,8})", field(cb, "Source")) or (bool(pm) and pm[0] in field(cb, "Source"))
    else:  # A2 edges: the record is named in the claim's Source/Wikilinks, or its own claim links
        cb = block(claims, r["claim"]) or ""
        key = r["anchor"]
        link_ok = key in (field(cb, "Source") + " " + field(cb, "Wikilinks")) or num in re.findall(r"\b(\d{3})\b", re.split(r"\(|\s[—–]\s|`", field(b, "Claim links"))[0])
    match_level = (lvl == r["attested"])
    ok = match_level and link_ok
    ok_all &= ok
    print(f"{r['claim']} | {r['anchor']} {r['cls']}/{r['edge']} | scan level={r['attested']} | raw level={lvl} ({len(ev_ids)} receipts) | link affirmed in raw text={link_ok} | {'MATCH' if ok else 'DIFF'}")
print("ALL MATCH" if ok_all else "AT LEAST ONE DIFFERENCE", "| seed 20261119 | sample of", len(sample), "of", len(rows), "A1/A2 rows")
