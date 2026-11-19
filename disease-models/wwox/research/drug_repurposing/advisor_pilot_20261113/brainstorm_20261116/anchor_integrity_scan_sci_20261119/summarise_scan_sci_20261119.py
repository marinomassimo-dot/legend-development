"""Headline numbers of the anchor scan, read back from the two TSVs the scan wrote (no tool modules). Writes SCAN_SUMMARY_NUMBERS_SCI_20261119.txt next to itself.
Run:  python3 -I summarise_scan_sci_20261119.py"""
import collections, csv, io, sys
from pathlib import Path

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)

HERE = Path(__file__).resolve().parent
claims = list(csv.DictReader(open(HERE / "claims_ranked_scan_sci_20261119.tsv", encoding="utf-8"), delimiter="\t"))
anch = list(csv.DictReader(open(HERE / "anchors_by_claim_scan_sci_20261119.tsv", encoding="utf-8"), delimiter="\t"))
out = io.StringIO()


def p(*a):
    print(*a, file=out)


DEC = {"full_text": 4, "partial_full_text": 3, "abstract": 2, "catalogued": 1, "filtered": 0, "UNRESOLVED": 0}
ATT = {"complete_strict": 4, "complete_loose": 4, "partial": 3, "abstract_only": 2, "not_read": 1, "none": 1, "placeholder": 0, "no_identifier": 0}
a12 = [a for a in anch if a["cls"] in ("A1", "A2")]
a4 = [a for a in anch if a["cls"] == "A4"]
p("claims", len(claims), "| with consumption key > 0:", sum(1 for c in claims if int(c["key"]) > 0), "| slice20:", sum(1 for c in claims if c["slice20"] == "Y"))
p("anchor rows by class:", dict(collections.Counter(a["cls"] for a in anch)))
p("A1+A2 rows by own attested level:", dict(collections.Counter(a["attested"] for a in a12)))
part = [a for a in a12 if a["attested"] == "partial"]
p("partial rows:", len(part), "| of which Results read in at least one surviving receipt:", sum(1 for a in part if "results" in a["union_read"].split(",")), "| without Results read:", [(a["claim"], a["anchor"]) for a in part if "results" not in a["union_read"].split(",")])
weak = [a for a in a12 if ATT[a["effective"]] < 4 and a["effective"] != "partial"]
p("A1+A2 rows below partial after effective level:", [(a["claim"], a["anchor"], a["effective"]) for a in a12 if a["effective"] in ("abstract_only", "not_read", "none", "placeholder", "no_identifier")])
over = [a for a in a12 if DEC[a["declared"]] > ATT[a["attested"]]]
under = [a for a in a12 if DEC[a["declared"]] < ATT[a["attested"]]]
p("declared depth above attested (rows):", len(over), "| below attested:", len(under), "| equal:", len(a12) - len(over) - len(under))
p("DECLARED_NOT_ATTESTED rows:", [(a["claim"], a["anchor"], a["declared"], a["attested"]) for a in a12 if "DECLARED_NOT_ATTESTED" in a["flags"]])
p("A4 negated-link rows:", len(a4), "| by claim:", dict(collections.Counter(a["claim"] for a in a4)))
p("A4 rows by depth:", dict(collections.Counter(a["attested"] for a in a4)))
p("superseded anchors:", [(a["claim"], a["anchor"], a["superseded_by"], a["effective"]) for a in a12 if a["superseded_by"]])
S = [c for c in claims if c["slice20"] == "Y"]
p()
p("SLICE (rank, claim, status, needs/cards/cells = key, anchors A1/A2/dup, strict/loose/partial/other, flags)")
for c in S:
    other = int(c["abstract_only"]) + int(c["not_read"]) + int(c["none"]) + int(c["placeholder"]) + int(c["no_identifier"])
    fl = [k.split("_")[0] for k in ("F1_THIN", "F2_PLACEHOLDER", "F4_DECLARED_NOT_ATTESTED", "F6_HAS_WEAK_ANCHOR", "F7_WIKILINK_ONLY_ANCHOR", "F8_PARTIAL_NO_RESULTS") if c[k]]
    if c["F3_WORDING_VS_DEPTH"]:
        fl.append("F3:" + c["F3_WORDING_VS_DEPTH"])
    p(f"{c['rank']:>2} {c['claim']} {c['status'][:12]:<12} {c['needs']}/{c['cards']}/{c['cells']}={c['key']:>3}  A1 {c['n_A1']} A2 {c['n_A2']} dup {c['n_A2_dup']}  cS {c['complete_strict']} cL {c['complete_loose']} par {c['partial']} oth {other}  {' '.join(fl)}")
p()
p("slice claims with F6:", [c["claim"] for c in S if c["F6_HAS_WEAK_ANCHOR"]], "| with F1:", [c["claim"] for c in S if c["F1_THIN"]], "| F2:", [c["claim"] for c in S if c["F2_PLACEHOLDER"]], "| F4:", [c["claim"] for c in S if c["F4_DECLARED_NOT_ATTESTED"]], "| F7:", [c["claim"] for c in S if c["F7_WIKILINK_ONLY_ANCHOR"]], "| F8:", [c["claim"] for c in S if c["F8_PARTIAL_NO_RESULTS"]])
p("slice claims with a single A1/A2 anchor:", [(c["claim"], c["key"]) for c in S if int(c["n_anchor"]) == 1])
rest = [c for c in claims if c["slice20"] != "Y"]
p("OUTSIDE THE SLICE with F1/F2/F4/F7/F8 (claim, status, key):", [(c["claim"], c["status"][:4], c["key"]) for c in rest if c["F1_THIN"] or c["F2_PLACEHOLDER"] or c["F4_DECLARED_NOT_ATTESTED"] or c["F7_WIKILINK_ONLY_ANCHOR"] or c["F8_PARTIAL_NO_RESULTS"]])
p("claims by status:", dict(collections.Counter(c["status"] for c in claims)))
p("consolidated baseline claims:", sum(1 for c in claims if c["status"] == "consolidated baseline"), "| with consumption:", sum(1 for c in claims if c["status"] == "consolidated baseline" and int(c["key"]) > 0), "| with F6:", sum(1 for c in claims if c["status"] == "consolidated baseline" and c["F6_HAS_WEAK_ANCHOR"]), "| F1:", sum(1 for c in claims if c["status"] == "consolidated baseline" and c["F1_THIN"]), "| F7:", sum(1 for c in claims if c["status"] == "consolidated baseline" and c["F7_WIKILINK_ONLY_ANCHOR"]))
text = out.getvalue()
(HERE / "SCAN_SUMMARY_NUMBERS_SCI_20261119.txt").write_text(text, encoding="utf-8")
print(text)
