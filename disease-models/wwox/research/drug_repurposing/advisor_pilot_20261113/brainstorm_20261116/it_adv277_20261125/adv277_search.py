#!/usr/bin/env python3
"""ADV-277 existence check: HDAC inhibitor x neural x protein, in PRIDE, ProteomeXchange and Europe PMC.

Plain requests, generic client name, no e-mail or key. Writes search_log.tsv rows to stdout
of the log file given as argv[1] and raw records to the directory given as argv[2].
"""
import json, re, sys, time, datetime, urllib.parse, urllib.request

LOG, RAW = sys.argv[1], sys.argv[2]
UA = "LEGEND-research-client/1.0"
DATE = datetime.datetime.now(datetime.timezone.utc).date().isoformat()

PRIDE_TERMS = ["valproate", "valproic acid", "vorinostat", "SAHA", "suberoylanilide", "trichostatin",
               "butyrate", "entinostat", "MS-275", "panobinostat", "romidepsin", "CI-994", "tubastatin",
               "mocetinostat", "belinostat", "givinostat", "HDAC inhibitor", "histone deacetylase inhibitor",
               "HDAC inhibition"]
NEURAL = re.compile(r"(?i)\b(neur(al|on|ons|onal|oblastoma|ite|oprogenitor|osphere|odevelopment\w*|odegenera\w*)|"
                    r"brain|cort(ex|ical)|hippocamp\w*|cerebell\w*|cerebr\w*|striat\w*|spinal cord|astrocyt\w*|"
                    r"oligodendro\w*|microglia\w*|glia\w*|glioma|glioblastoma|medulloblastoma|forebrain|"
                    r"hypothalam\w*|amygdala|synap\w*|NSC|NPC|SH-SY5Y|PC12|Neuro-?2a|N2a)\b")


def get(url, timeout=90, data=None, headers=None):
    h = {"User-Agent": UA, "Accept": "application/json"}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()
    except Exception as e:  # network failure is a route result
        return 0, {}, repr(e).encode()


def log(route, obj, query, result):
    with open(LOG, "a") as f:
        f.write("\t".join([DATE, route, obj, query, result]) + "\n")


pride, px = {}, {}
for term in PRIDE_TERMS:
    rows, page, total = [], 0, None
    while True:
        q = urllib.parse.urlencode({"keyword": term, "pageSize": 100, "page": page})
        st, hd, body = get("https://www.ebi.ac.uk/pride/ws/archive/v3/search/projects?" + q)
        if st != 200:
            log("PRIDE v3 search/projects", term, "keyword=" + term, "HTTP %s" % st)
            break
        part = json.loads(body)
        total = int({k.lower(): v for k, v in hd.items()}.get("total_records", -1))
        rows += part
        if len(part) < 100 or page > 30:
            break
        page += 1
        time.sleep(0.5)
    for r in rows:
        pride.setdefault(r["accession"], {"rec": r, "terms": []})["terms"].append(term)
    log("PRIDE v3 search/projects", term, "keyword=" + term,
        "HTTP 200; total header %s; records enumerated %d" % (total, len(rows)))
    time.sleep(0.5)

for term in PRIDE_TERMS:
    q = urllib.parse.urlencode({"resultType": "compact", "pageSize": 1000, "search": term})
    st, hd, body = get("https://proteomecentral.proteomexchange.org/api/proxi/v0.1/datasets?" + q)
    if st != 200:
        log("ProteomeXchange PROXI datasets", term, "search=" + term, "HTTP %s" % st)
        continue
    d = json.loads(body)
    rows = d.get("datasets", [])
    for r in rows:
        px.setdefault(r[0], {"rec": r, "terms": []})["terms"].append(term)
    meta = d.get("result_set", {})
    log("ProteomeXchange PROXI datasets", term, "search=" + term,
        "HTTP 200; records %d; result_set %s" % (len(rows), json.dumps(meta)[:160]))
    time.sleep(0.5)

json.dump(pride, open(RAW + "/pride_all.json", "w"))
json.dump(px, open(RAW + "/px_all.json", "w"))


def text_pride(v):
    return json.dumps(v["rec"])


def text_px(v):
    return " ".join(str(x) for x in v["rec"] if x)


pn = {a for a, v in pride.items() if NEURAL.search(text_pride(v))}
xn = {a for a, v in px.items() if NEURAL.search(text_px(v))}
log("count", "union", "PRIDE union over %d terms" % len(PRIDE_TERMS), "%d projects; %d with a neural word" % (len(pride), len(pn)))
log("count", "union", "PROXI union over %d terms" % len(PRIDE_TERMS), "%d datasets; %d with a neural word" % (len(px), len(xn)))
log("count", "second route", "neural-word accessions in both routes", "%d both; PRIDE only %d; PROXI only %d" % (len(pn & xn), len(pn - xn), len(xn - pn)))
json.dump({"pride_neural": sorted(pn), "px_neural": sorted(xn)}, open(RAW + "/neural_sets.json", "w"))

# Europe PMC
C = ('("valproic acid" OR valproate OR vorinostat OR "suberoylanilide hydroxamic acid" OR "trichostatin A" OR '
     '"sodium butyrate" OR entinostat OR panobinostat OR romidepsin OR "CI-994" OR "histone deacetylase inhibitor")')
N = ('(neuron OR neurons OR neuronal OR "neural stem" OR "neural progenitor" OR organoid OR brain OR hippocampus OR '
     'cortex OR cerebellum OR astrocyte OR microglia OR oligodendrocyte)')
P = '(proteome OR proteomic OR proteomics OR "mass spectrometry")'
queries = {
    "title_abstract_triple": "(TITLE:%s OR ABSTRACT:%s) AND (TITLE:%s OR ABSTRACT:%s) AND (TITLE:%s OR ABSTRACT:%s) AND HAS_FT:Y NOT PUB_TYPE:Review" % (C, C, N, N, P, P),
    "title_abstract_triple_no_ft_filter": "(TITLE:%s OR ABSTRACT:%s) AND (TITLE:%s OR ABSTRACT:%s) AND (TITLE:%s OR ABSTRACT:%s) NOT PUB_TYPE:Review" % (C, C, N, N, P, P),
    "pride_linked": "%s AND %s AND ACCESSION_TYPE:pxd" % (C, N),
    "wwox_with_compound_and_proteome": '(WWOX) AND %s AND %s AND %s NOT PUB_TYPE:Review' % (C, N, P),
}
for name, q in queries.items():
    rows, cur, hit = [], "*", None
    while True:
        u = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
            {"query": q, "format": "json", "pageSize": 1000, "cursorMark": cur, "resultType": "core"})
        st, hd, body = get(u)
        if st != 200:
            log("Europe PMC search", name, q, "HTTP %s" % st)
            break
        d = json.loads(body)
        hit = d.get("hitCount")
        part = d.get("resultList", {}).get("result", [])
        rows += part
        nxt = d.get("nextCursorMark")
        if not part or not nxt or nxt == cur or len(rows) >= 3000:
            break
        cur = nxt
        time.sleep(0.5)
    json.dump(rows, open(RAW + "/epmc_%s.json" % name, "w"))
    log("Europe PMC search", name, q, "hitCount %s; records enumerated %d" % (hit, len(rows)))

# Proteomic Data Commons (CPTAC data service)
q = '{"query":"{ getPaginatedUIStudy(offset:0, limit:1000, sort:\\"\\") { total uiStudies { pdc_study_id submitter_id_name program_name project_name disease_type primary_site analytical_fraction experiment_type } } }"}'
st, hd, body = get("https://pdc.cancer.gov/graphql", data=q.encode(), headers={"Content-Type": "application/json"})
if st == 200:
    open(RAW + "/pdc_studies.json", "wb").write(body)
    try:
        d = json.loads(body)["data"]["getPaginatedUIStudy"]
        st_ = d["uiStudies"]
        pat = re.compile(r"(?i)HDAC|valpro|vorinostat|trichostatin|butyrate|entinostat|panobinostat|romidepsin|deacetylase|perturb|treat|drug|compound|inhibitor")
        hits = [s["pdc_study_id"] + " " + s["submitter_id_name"] for s in st_ if pat.search(s["submitter_id_name"])]
        log("PDC graphql getPaginatedUIStudy", "all studies", "name filter " + pat.pattern,
            "HTTP 200; total %s; enumerated %d; name hits %d: %s" % (d["total"], len(st_), len(hits), "; ".join(hits)[:600]))
    except Exception as e:
        log("PDC graphql getPaginatedUIStudy", "all studies", "getPaginatedUIStudy", "HTTP 200; unreadable: %r %s" % (e, body[:200]))
else:
    log("PDC graphql getPaginatedUIStudy", "all studies", "getPaginatedUIStudy", "HTTP %s %s" % (st, body[:120]))
