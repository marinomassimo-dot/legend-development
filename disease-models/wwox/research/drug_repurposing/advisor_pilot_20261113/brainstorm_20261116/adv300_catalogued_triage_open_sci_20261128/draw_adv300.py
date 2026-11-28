"""ADV-300: test every remaining catalogued-only record for an open full-text route, then draw ten from those that have one.
Usage, from the repository root: python3 draw_adv300.py SEED HELD_DIR OUT_TSV
HELD_DIR is the held full-text folder. Plain requests, no address, no retry. Prints ids, PMIDs, PMCIDs, routes and counts only:
no title, no abstract, no article text (fetched XML is parsed in memory and discarded)."""
import hashlib, json, random, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

if len(sys.argv) != 4 or not sys.argv[1].isdigit():
    print(__doc__)
    raise SystemExit(0 if sys.argv[1:] in (["-h"], ["--help"]) else 2)
sys.path.insert(0, str(Path("framework/scripts").resolve()))
import coverage_report as cov  # noqa: E402
import fulltext_receipts as receipts  # noqa: E402

EXCLUDED = {"42422765"}
DRAWN_ADV297 = {"CORPUS P399", "CORPUS P252", "CORPUS-STUB-197", "CORPUS P247", "CORPUS P214",
                "CORPUS-STUB-136", "CORPUS P376", "CORPUS P375", "CORPUS P364", "CORPUS-STUB-071"}
MIN_BODY_CHARS, MIN_HELD_BYTES = 3000, 20000


def get(url):
    time.sleep(0.4)
    request = urllib.request.Request(url, headers={"User-Agent": "literature-route-check"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return str(response.status), response.read()
    except urllib.error.HTTPError as error:
        return str(error.code), b""
    except Exception as error:  # a result, not retried
        return type(error).__name__, b""


def body_chars(data):
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return 0
    body = root.find(".//body")
    return len("".join(body.itertext())) if body is not None else 0


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
    pool.append((entry["_id"], sorted(set(pmids))))
print("pool_no_receipt", len(pool))
pool = [p for p in pool if p[0] not in DRAWN_ADV297 and not EXCLUDED.intersection(p[1])]
print("pool_after_exclusions", len(pool))
unresolved = [p for p in pool if len(p[1]) != 1]
pool = sorted((rid, pmids[0]) for rid, pmids in pool if len(pmids) == 1)
print("unresolved_identifier", len(unresolved), "testable", len(pool))

pmcid, epmc_flag = {}, {}
ids = [p for _, p in pool]
for start in range(0, len(ids), 50):
    chunk = ids[start:start + 50]
    query = "(" + " OR ".join("EXT_ID:" + p for p in chunk) + ") AND SRC:MED"
    status, data = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": query, "format": "json", "resultType": "lite", "pageSize": 100}))
    print("europepmc_search", start, status)
    if status == "200":
        for hit in json.loads(data)["resultList"]["result"]:
            pmid = hit.get("pmid")
            if pmid in chunk:
                pmcid[pmid] = hit.get("pmcid", "")
                epmc_flag[pmid] = hit.get("isOpenAccess", "")

held_files = [f for f in Path(sys.argv[2]).iterdir()
              if f.is_file() and f.suffix.lower() in (".xml", ".txt", ".html", ".pdf") and f.stat().st_size >= MIN_HELD_BYTES
              and "abstract" not in f.name.lower() and "suppl" not in f.name.lower()]
rows = []
for rid, pmid in pool:
    pmc = pmcid.get(pmid, "")
    pattern = re.compile(r"(?<!\d)%s(?!\d)" % pmid + (r"|%s(?!\d)" % pmc if pmc else ""))
    held = sorted(f.name for f in held_files if pattern.search(f.name))
    route, detail = "", []
    if held:
        route = "held:" + held[0]
    elif pmc:
        status, data = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&rettype=xml&id=" + pmc[3:])
        n = body_chars(data) if status == "200" else 0
        detail.append("efetch=%s/%s" % (status, "body" if n >= MIN_BODY_CHARS else "nobody"))
        if n >= MIN_BODY_CHARS:
            route = "efetch"
        else:
            status, data = get("https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML" % pmc)
            n = body_chars(data) if status == "200" else 0
            detail.append("epmcxml=%s/%s" % (status, "body" if n >= MIN_BODY_CHARS else "nobody"))
            if n >= MIN_BODY_CHARS:
                route = "europepmc"
    rows.append((rid, pmid, pmc, epmc_flag.get(pmid, ""), route, " ".join(detail)))
Path(sys.argv[3]).write_text("record\tpmid\tpmcid\tepmc_open_flag\troute\ttest_detail\n"
                             + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
open_pool = [(r[0], r[1]) for r in rows if r[4]]
print("with_pmcid", sum(1 for r in rows if r[2]), "open_route", len(open_pool),
      "held", sum(1 for r in rows if r[4].startswith("held:")), "efetch", sum(1 for r in rows if r[4] == "efetch"),
      "europepmc", sum(1 for r in rows if r[4] == "europepmc"))
print("open_pool_sha256", hashlib.sha256("\n".join("%s\t%s" % p for p in open_pool).encode()).hexdigest())
for rank, (rid, pmid) in enumerate(random.Random(int(sys.argv[1])).sample(open_pool, 10), 1):
    print("draw", rank, rid, pmid, sep="\t")
