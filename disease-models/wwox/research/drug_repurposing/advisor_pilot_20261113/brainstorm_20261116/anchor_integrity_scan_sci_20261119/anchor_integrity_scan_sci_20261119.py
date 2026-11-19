"""SCI 2026-11-19: anchor-integrity scan of the canonical claims, as frozen in PREREG_ANCHOR_SCAN_SCI_20261119.md.
Reading and counting only. Writes TSV/JSON next to itself; edits no registry, card, need, arm table or receipt.
Run from any directory:  python3 -I anchor_integrity_scan_sci_20261119.py <repository-root>
"""
import collections, csv, json, re, sys
from pathlib import Path

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
ROOT = Path(sys.argv[1]).resolve()
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "framework/scripts"))
import coverage_report as C
import fulltext_receipts as FR
import trace_claim_foundation as T

DR = ROOT / "disease-models/wwox/research/drug_repurposing"
REG = ROOT / "disease-models/wwox/registries"
CLAIM_RE = re.compile(r"(?<![A-Za-z])CLAIM[ _-]?(\d{3})(?!\d)")
CORPUS_RE = re.compile(r"CORPUS[ -](?:STUB-\d+|P\d+)")
PMID_RE = re.compile(r"\b(\d{7,8})\b")
RANK = {"complete_strict": 6, "complete_loose": 5, "partial": 4, "abstract_only": 3, "not_read": 2, "none": 1, "placeholder": 0, "no_identifier": 0}
log = {}


def _strip_parens(s):
    out, depth = [], 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def strict_links(s):
    """AMENDMENT 6: claim numbers a `Claim links` field AFFIRMS. A field that begins 'none' links nothing, whatever claim numbers its explanation names;
    backticked text and parenthetical annotations are not links; text after a spaced dash is annotation."""
    s = s.strip()
    if re.match(r"(?i)^(\W*)(none|nessun|no\b|not\b)", s):
        return set()
    t = re.sub(r"`[^`]*`", " ", _strip_parens(s))
    t = re.split(r"\s[—–]\s|\s--\s", t)[0]
    return set(re.findall(r"\b(\d{3})\b", t))

# ---- claims and registry entries -------------------------------------------------------------
F = T.Foundation(ROOT, "wwox")
claims = sorted(F.claims)
log["claims_foundation"] = len(claims)
entries = C.parse_entries((REG / "paper_registry_current.md").read_text(encoding="utf-8"))
byid = {e["_id"]: e for e in entries}
log["entries"] = dict(collections.Counter(e["_kind"] for e in entries))
ledger_path = FR.default_ledger_path(ROOT, "wwox")
idx = FR.receipt_depth_index(ledger_path)
active = FR.active_receipts(FR.load_ledger(ledger_path))
by_pmid = collections.defaultdict(list); by_doi = collections.defaultdict(list)
for _r in active:  # AMENDMENT 7: all surviving receipts of the same study, by the receipt's OWN study_id
    if _r.get("record_kind") == "receipt_invalidation":
        continue
    if _r["study_id"].get("pmid"):
        by_pmid[str(_r["study_id"]["pmid"])].append(_r)
    if _r["study_id"].get("doi"):
        by_doi[FR.normalise_doi(_r["study_id"]["doi"])].append(_r)


def union_coverage(pmids, dois):
    recs = {r["event_id"]: r for p in pmids for r in by_pmid.get(p, [])}
    recs.update({r["event_id"]: r for d in dois for r in by_doi.get(FR.normalise_doi(d), [])})
    read = set()
    for r in recs.values():
        read |= {k for k, v in (r.get("coverage") or {}).items() if v == "read"}
    return sorted(read), len(recs)


paper_pmids = collections.defaultdict(set)
for e in entries:
    for p in C.PMID.findall(e.get("identifier", "")):
        paper_pmids[p].add(e["_id"])


def attested(entry):
    """(level, receipt) for one registry entry; placeholder when it has no PMID and no DOI."""
    ident = entry.get("identifier", "")
    has_id = bool(C.PMID.findall(ident) or C.DOI.findall(ident))
    # AMENDMENT 5 (dated, after the second run): a record is a placeholder only when it carries no PMID/DOI (or says PENDING);
    # a CORPUS record that carries a PMID/DOI is levelled by the receipt of its study like any record. PAPER records without an identifier: 'no_identifier'.
    if ident.strip().upper() == "PENDING" or not has_id:  # AMENDMENT 9: only a literal PENDING; a promoted record that mentions PENDING in its history carries a real PMID
        return ("placeholder" if entry["_kind"] == "CORPUS" else "no_identifier"), None
    rc = C.entry_receipt(entry, idx)
    if rc is None:
        return "none", None
    d = rc["evidence_depth"]
    if d == "complete_fulltext_read":
        cov = rc.get("coverage") or {}
        ok = cov.get("results") == "read" and all(cov.get(k) in ("read", "not_present") for k in ("abstract", "introduction", "methods", "discussion"))
        return ("complete_strict" if ok else "complete_loose"), rc
    return {"partial_fulltext_read": "partial", "abstract_only": "abstract_only"}.get(d, "not_read"), rc


# ---- anchors -------------------------------------------------------------------------------------
anchor_rows = []
claim_anchor = collections.defaultdict(list)
for cid in claims:
    num = cid.split()[-1]
    cf = F.claims[cid]
    src, wl = cf.get("Source", ""), cf.get("Wikilinks", "")
    ids = {}
    for pid, edge in F.supporting_papers(cid):
        if edge == "claim_links" and num not in strict_links(F.papers[pid].get("Claim links", "")):
            ids[pid] = ("A4", "negated_link")  # AMENDMENT 6: the paper's own Claim links says 'none ...' and merely names this claim; the tool counts it as a link
            continue
        if edge in T.EVIDENTIAL_EDGES:
            ids[pid] = ("A1", edge)
        elif edge == "wikilink_only":  # AMENDMENT 1 (dated, after the first run): kept apart as A3, never counted as A1/A2
            ids[pid] = ("A3", edge)
    corpus_named = {" ".join(m.replace("-", " ").split()) if not m.startswith("CORPUS-STUB") else m for m in CORPUS_RE.findall(src + " " + wl)}
    for m in corpus_named:
        key = m if m in byid else m.replace("CORPUS ", "CORPUS-") if m.replace("CORPUS ", "CORPUS-") in byid else m
        ids.setdefault(key, ("A2", "source_or_wikilink"))
    for e in entries:
        if e["_kind"] == "CORPUS" and num in strict_links(e.get("claim links", "")):
            ids.setdefault(e["_id"], ("A2", "own_claim_links"))
    for aid, (cls, edge) in sorted(ids.items()):
        e = byid.get(aid)
        if e is None:
            anchor_rows.append(dict(claim=cid, anchor=aid, cls=cls, edge=edge, pmid="", doi="", declared="UNRESOLVED", attested="placeholder", effective="placeholder", superseded_by="", receipt="", receipt_pmid_ok="", flags="ANCHOR_RECORD_NOT_FOUND"))
            claim_anchor[cid].append(anchor_rows[-1]); continue
        lvl, rc = attested(e)
        declared = C.classify_depth(e)
        # AMENDMENT 8: a record whose Status is 'superseded' by a named PAPER is levelled at the better of its own level and the superseding record's
        # AMENDMENT 9: also a record whose Status is 'promoted — see [[PAPER nnn]]' (a CORPUS audit-trail record kept after promotion)
        st = e.get("status", "")
        sup = re.search(r"(?:promoted|superseded)[^\[]{0,240}\[\[paper_registry_current#(PAPER \d{3})\]\]", st, re.I)
        if not sup and re.search(r"superseded", st, re.I):
            sup = re.search(r"[Ss]uperseded[^\[]{0,240}\[\[paper_registry_current#(PAPER \d{3})\]\]", e.get("_body", ""))
        sup_id = sup.group(1) if sup else ""
        eff = lvl
        if sup_id and sup_id in byid:
            l2, _rc2 = attested(byid[sup_id])
            if RANK[l2] > RANK[lvl]:
                eff = l2
        pm = C.PMID.findall(e.get("identifier", "")); dois = C.DOI.findall(e.get("identifier", ""))
        evid = rc["event_id"] if rc else ""
        evpm = (re.match(r"FTR-\d{8}-(\d+)-", evid).group(1) if evid and re.match(r"FTR-\d{8}-(\d+)-", evid) else "")
        pm_ok = "" if not rc else ("yes" if (evpm == str(rc["study_id"].get("pmid") or "") or not rc["study_id"].get("pmid")) else "NO")
        flags = []
        ur, n_rc = union_coverage(pm, dois)
        if lvl in ("partial", "abstract_only", "not_read") and "results" not in ur:
            flags.append("PARTIAL_NO_RESULTS")  # AMENDMENT 7: no surviving receipt of this study has Results read
        if declared == "full_text" and lvl not in ("complete_strict", "complete_loose"):
            flags.append("DECLARED_NOT_ATTESTED")
        row = dict(claim=cid, anchor=aid, cls=cls, edge=edge, pmid=pm[0] if pm else "", doi=dois[0] if dois else "", declared=declared, attested=lvl, effective=eff, superseded_by=sup_id,
                   receipt=evid, receipt_pmid_ok=pm_ok, flags=";".join(flags), n_receipts_study=n_rc, union_read=",".join(ur), dup_of_A1="", _pmids=set(pm), _dois={FR.normalise_doi(d) for d in dois})
        anchor_rows.append(row); claim_anchor[cid].append(row)
    # AMENDMENT 5: an A2 record naming the same study (PMID or DOI) as an A1 anchor of the same claim is a duplicate of it
    for a in claim_anchor[cid]:
        if a["cls"] == "A2":
            dups = [b["anchor"] for b in claim_anchor[cid] if b["cls"] == "A1" and ((a["_pmids"] & b["_pmids"]) or (a["_dois"] & b["_dois"]))]
            a["dup_of_A1"] = ";".join(dups)

# ---- consumption -------------------------------------------------------------------------------
cons = {k: collections.defaultdict(set) for k in ("needs", "cards", "cells", "queries")}
paths = collections.Counter()


def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f"{path}/{k}")
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v, f"{path}[]")
    elif isinstance(obj, str):
        yield path, obj


def note(kind, unit, text, path):
    for m in set(CLAIM_RE.findall(text)):
        cons[kind]["CLAIM " + m].add(unit)
        paths[(kind, re.sub(r"\[\]", "", path.split("/")[1] if path.count("/") >= 1 else path))] += 1


needs = json.loads((DR / "needs/needs.json").read_text(encoding="utf-8"))["needs"]
for n in needs:
    for p, s in walk(n):
        note("needs", n["id"], s, p)
for folder in ("cards", "cards_early"):
    for f in sorted((DR / folder).glob("*.card.json")):
        for p, s in walk(json.loads(f.read_text(encoding="utf-8"))):
            note("cards", f"{folder}/{f.name}", s, p)
for it in json.loads((DR / "join/cards.json").read_text(encoding="utf-8")):
    for p, s in walk(it["card"]):
        note("cards", f"join/{it['query_id']}", s, p)
with open(DR / "matrix_v2_cells_sci_20261116/output/cells_v2_form.tsv", encoding="utf-8", newline="") as fh:
    rd = csv.DictReader(fh, delimiter="\t")
    nrows = 0
    for row in rd:
        nrows += 1
        for k, v in row.items():
            note("cells", row["cell_id"], v or "", "/" + k)
log["cells_rows"] = nrows
for q in json.loads((DR / "join/queries.json").read_text(encoding="utf-8")):
    if q.get("kind") == "claim" and CLAIM_RE.search(q.get("origin_id", "")):
        cons["queries"]["CLAIM " + CLAIM_RE.search(q["origin_id"]).group(1)].add(q["digest"] + ":" + str(q.get("axis")))
log["needs"] = len(needs)

# ---- claim table ------------------------------------------------------------------------------
src_pmids_unanchored = {}
rows = []
for cid in claims:
    cf = F.claims[cid]
    anc_all = [a for a in claim_anchor[cid] if a["cls"] not in ("A3", "A4")]
    n_a4 = sum(1 for a in claim_anchor[cid] if a["cls"] == "A4")
    anc = [a for a in anc_all if not a["dup_of_A1"]]  # AMENDMENT 5: a duplicate A2 record of an A1 study is not a separate anchor
    a3 = [a for a in claim_anchor[cid] if a["cls"] == "A3"]
    a3_deepest = max((a["attested"] for a in a3), key=RANK.get) if a3 else ""
    a3_weakest = min((a["attested"] for a in a3), key=RANK.get) if a3 else ""
    a1 = [a for a in anc if a["cls"] == "A1"]
    a2 = [a for a in anc if a["cls"] == "A2"]
    levels = collections.Counter(a["attested"] for a in anc)
    deepest = max((a["attested"] for a in anc), key=RANK.get) if anc else "none"
    weakest = min((a["attested"] for a in anc), key=RANK.get) if anc else "none"
    a1_deepest = max((a["attested"] for a in a1), key=RANK.get) if a1 else "none"
    status = cf.get("Status", "")
    f1 = not any(a["effective"] == "complete_strict" for a in a1)
    f2 = bool(a2)
    f2a = all(a["attested"] in ("placeholder", "no_identifier", "none") for a in anc) if anc else True
    f3 = ""
    if status == "consolidated baseline" and f1:
        f3 = "strong"
    elif status == "in observation" and RANK[a1_deepest] <= RANK["abstract_only"]:
        f3 = "medium"
    f4 = any("DECLARED_NOT_ATTESTED" in a["flags"] for a in anc)
    # AMENDMENTS 2 and 3 (dated, after the first run; post hoc)
    f6 = any(RANK[a["effective"]] < RANK["complete_loose"] for a in anc)  # depth only after Amendment 5(c); F2 keeps the record-kind flag
    f8 = any("PARTIAL_NO_RESULTS" in a["flags"] for a in anc)  # AMENDMENT 7
    f7 = (not anc) and bool(a3)
    spm = [p for p in set(T.PMID.findall(cf.get("Source", ""))) if p not in paper_pmids]
    f5 = bool(spm)
    n_need, n_card, n_cell, n_q = (len(cons[k].get(cid, ())) for k in ("needs", "cards", "cells", "queries"))
    rows.append(dict(claim=cid, status=status, type=cf.get("Type", "")[:40], n_anchor=len(anc), n_A1=len(a1), n_A2=len(a2), n_A2_dup=len(anc_all) - len(anc),
                     complete_strict=levels["complete_strict"], complete_loose=levels["complete_loose"], partial=levels["partial"], abstract_only=levels["abstract_only"],
                     not_read=levels["not_read"], none=levels["none"], placeholder=levels["placeholder"], no_identifier=levels["no_identifier"],
                     deepest=deepest, weakest=weakest, F1_THIN="Y" if f1 else "", F2_PLACEHOLDER="Y" if f2 else "", F2a_ONLY_PLACEHOLDER_OR_NONE="Y" if f2a else "",
                     F3_WORDING_VS_DEPTH=f3, F4_DECLARED_NOT_ATTESTED="Y" if f4 else "", F5_SOURCE_PMID_UNANCHORED=";".join(spm),
                     F6_HAS_WEAK_ANCHOR="Y" if f6 else "", F8_PARTIAL_NO_RESULTS="Y" if f8 else "", F7_WIKILINK_ONLY_ANCHOR="Y" if f7 else "", n_A4_negated=n_a4, n_A3=len(a3), A3_deepest=a3_deepest, A3_weakest=a3_weakest,
                     needs=n_need, cards=n_card, cells=n_cell, key=n_need + n_card + n_cell, queries_context=n_q))
rows.sort(key=lambda r: (-r["key"], r["claim"]))
for i, r in enumerate(rows, 1):
    r["rank"] = i
    r["slice20"] = "Y" if (i <= 20 and r["key"] > 0) else ""

with open(HERE / "claims_ranked_scan_sci_20261119.tsv", "w", encoding="utf-8", newline="") as fh:
    cols = ["rank", "slice20", "claim"] + [k for k in rows[0] if k not in ("rank", "slice20", "claim")]
    w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
with open(HERE / "anchors_by_claim_scan_sci_20261119.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, [k for k in anchor_rows[0] if not k.startswith("_")], delimiter="\t", lineterminator="\n", extrasaction="ignore"); w.writeheader(); w.writerows(anchor_rows)
with open(HERE / "consumption_field_paths_scan_sci_20261119.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["consumer_kind", "top_level_field", "mentions"])
    for (k, p), n in sorted(paths.items()):
        w.writerow([k, p, n])
bad = [a for a in anchor_rows if a["receipt_pmid_ok"] == "NO"]
log["event_pmid_mismatch"] = [(a["claim"], a["anchor"], a["receipt"]) for a in bad]
log["anchors_total_A1_A2"] = sum(1 for a in anchor_rows if a["cls"] in ("A1", "A2"))
log["anchors_by_class"] = dict(collections.Counter(a["cls"] for a in anchor_rows))
log["anchors_by_level_A1_A2"] = dict(collections.Counter(a["attested"] for a in anchor_rows if a["cls"] in ("A1", "A2")))
log["anchors_by_level_A3"] = dict(collections.Counter(a["attested"] for a in anchor_rows if a["cls"] == "A3"))
log["claims_F6"] = sum(1 for r in rows if r["F6_HAS_WEAK_ANCHOR"]); log["claims_F7"] = sum(1 for r in rows if r["F7_WIKILINK_ONLY_ANCHOR"])
log["claims_with_key_gt0"] = sum(1 for r in rows if r["key"] > 0)
log["ledger_events"] = len(FR.load_ledger(ledger_path))
(HERE / "scan_log_sci_20261119.json").write_text(json.dumps(log, indent=1, sort_keys=True), encoding="utf-8")
print(json.dumps(log, indent=1, sort_keys=True))
