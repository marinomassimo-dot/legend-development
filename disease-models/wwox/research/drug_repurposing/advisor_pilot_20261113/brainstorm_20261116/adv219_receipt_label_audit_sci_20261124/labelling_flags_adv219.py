"""Print-only audit of receipt coverage labels against held full-text artefacts (ADV-219).

For every study whose latest receipt is partial (or another non-complete depth), flag each
section that the latest receipt labels not_present / unavailable (class A, MISLABEL) or
not_read / captions_only (class B, OWED BUT HELD) while a held artefact demonstrably
contains it. The rules are the ones frozen in PREREG_ADV219_SCI_20261124.md.

It reads the receipts ledger, the held artefact folders and (for the ranking) two JSON
files produced by other tools; it writes nothing except stdout; no network.

Usage:
  python3 labelling_flags_adv219.py --root <repo root> --held <files dir> [--held <dir> ...]
                                    [--catalog catalog.json] [--map open_questions_map.tsv]
                                    [--seed 20261124] [--sample 15] [--limit N]
"""
import argparse
import collections
import csv
import json
import os
import random
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

SECTIONS = ["abstract", "introduction", "methods", "results", "discussion",
            "limitations", "figures", "tables", "supplementary", "references"]
CLASS_A = {"not_present", "unavailable"}
CLASS_B = {"not_read", "captions_only"}
SEC_RX = {
    "introduction": re.compile(r"intro", re.I),
    "methods": re.compile(r"method|materials and methods", re.I),
    "results": re.compile(r"result", re.I),
    "discussion": re.compile(r"discussion", re.I),
    "limitations": re.compile(r"limitation", re.I),
}
HEAD_RX = re.compile(r"^\s*(?:\d+\.?\s*)?(abstract|introduction|methods|materials and methods|"
                     r"results|discussion|limitations|references)\s*$", re.I)
TABLE_RX = re.compile(r"^\s*Table\s+\d+\s*[.:]")
FIG_RX = re.compile(r"^\s*(?:Figure|Fig\.?)\s*\d+\s*[.:]")
SUPP_RX = re.compile(r"^\s*(?:Supplementary|Supplemental)\s+(?:Figure|Fig\.?|Table)\s*S?\d+|"
                     r"^\s*Extended Data Fig", re.I)
NUM_RX = re.compile(r"^[-+−]?\d[\d.,]*%?$")
SUPP_NAME_RX = re.compile(r"supp|mmc|media|additional", re.I)


def load_ledger(path):
    latest, events = {}, collections.defaultdict(list)
    for line in open(path, encoding="utf-8"):
        if not line.strip():
            continue
        e = json.loads(line)
        if e.get("record_kind") != "contemporaneous_receipt":
            continue
        s = e.get("study_id") or {}
        key = s.get("pmid") or s.get("doi")
        if not key:
            m = re.match(r"FTR-\d{8}-(.+)-\d+$", e["event_id"])
            key = m.group(1) if m else e["event_id"]
        key = str(key)
        events[key].append(e)
    for k, evs in events.items():
        latest[k] = max(evs, key=lambda e: (e["event_at"], e["event_id"]))
    return latest, events


def best_state(evs, section):
    rank = ["read", "not_present", "captions_only", "unavailable", "not_read", "unknown_legacy"]
    vals = [(e.get("coverage") or {}).get(section) for e in evs]
    vals = [v for v in vals if v in rank]
    return min(vals, key=rank.index) if vals else None


def index_files(dirs):
    idx = collections.defaultdict(list)
    for d in dirs:
        for dp, _, fns in os.walk(d):
            for fn in fns:
                if not fn.lower().endswith((".xml", ".pdf", ".html", ".htm", ".txt")):
                    continue
                p = os.path.join(dp, fn)
                idx["name:" + fn].append(p)
                for m in re.finditer(r"PMID(\d+)", fn):
                    idx["pmid:" + m.group(1)].append(p)
                for m in re.finditer(r"(PPR\d+)", fn):
                    idx["id:" + m.group(1)].append(p)
                idx["doi:" + fn.lower()].append(p)
    return idx


def match_files(key, ev, idx):
    out = []
    if re.fullmatch(r"\d{5,9}", key):
        out += idx.get("pmid:" + key, [])
    elif key.startswith("PPR"):
        out += idx.get("id:" + key, [])
    elif "/" in key:
        san = key.lower()
        for a in (san.replace("/", "_"), san.replace("/", "-")):
            for fn, ps in ((k[4:], v) for k, v in idx.items() if k.startswith("doi:")):
                if a in fn:
                    out += ps
    loc = os.path.basename(ev.get("source_locator", "") or "")
    loc = re.sub(r"^.*\): ", "", loc)
    if loc:
        out += idx.get("name:" + loc, [])
    seen, uniq = set(), []
    for p in out:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq


def scan_xml(path):
    found = {}
    try:
        root = ET.parse(path).getroot()
    except Exception as ex:
        return None, "xml parse: %s" % ex
    ab = root.find(".//abstract")
    if ab is not None and "".join(ab.itertext()).strip():
        found["abstract"] = "xml: abstract element"
    for s in root.iter("sec"):
        t = (s.findtext("title") or "").strip()
        for name, rx in SEC_RX.items():
            if t and rx.search(t) and name not in found:
                found[name] = "xml: sec title '%s'" % t[:40]
    for w in root.iter("table-wrap"):
        if any(True for _ in w.iter("tr")):
            found["tables"] = "xml: table-wrap with rows"
            break
    rl = root.find(".//ref-list")
    if rl is not None and "".join(rl.itertext()).strip():
        found["references"] = "xml: ref-list"
    folder = os.path.dirname(path)
    names = set(os.listdir(folder))
    for g in root.iter("graphic"):
        href = os.path.basename(g.get("{http://www.w3.org/1999/xlink}href") or "")
        if href and any(n.startswith(href) for n in names):
            found["figures"] = "xml: graphic file %s held" % href
            break
    return found, None


def scan_pdf(path):
    try:
        txt = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True,
                             timeout=120).stdout.decode("utf-8", "replace")
    except Exception as ex:
        return None, "pdftotext: %s" % ex
    pages = txt.split("\f")
    if sum(len(p.strip()) for p in pages) < 500:
        return None, "no text layer"
    return scan_pages(pages, path=path), None


def scan_pages(pages, path=None):
    found, ref_page = {}, None
    for i, p in enumerate(pages, 1):
        lines = [l.strip() for l in p.splitlines()]
        for l in lines:
            m = HEAD_RX.match(l)
            if m:
                w = m.group(1).lower()
                w = "methods" if w == "materials and methods" else w
                if w == "references":
                    ref_page = ref_page or i
                    found.setdefault("references", "pdf p%d: References heading" % i)
                else:
                    found.setdefault(w, "pdf p%d: heading '%s'" % (i, l[:30]))
        nlines = [l for l in lines if l]
        for j, l in enumerate(nlines):
            if TABLE_RX.match(l) and "tables" not in found:
                numeric = sum(1 for r in nlines[j + 1:j + 40]
                              if sum(1 for t in r.split() if NUM_RX.match(t)) >= 2)
                if numeric >= 3:
                    found["tables"] = "pdf p%d: '%s'" % (i, l[:30])
            if FIG_RX.match(l) and "figures" not in found and path:
                nimg = 0
                try:
                    out = subprocess.run(["pdfimages", "-list", "-f", str(i), "-l", str(i), path],
                                         capture_output=True, timeout=30).stdout.decode()
                    nimg = max(0, len(out.strip().splitlines()) - 2)
                except Exception:
                    pass
                if nimg >= 1 or len(p) < 1500:
                    found["figures"] = "pdf p%d: '%s' (images %d, chars %d)" % (i, l[:30], nimg, len(p))
            if SUPP_RX.match(l) and ref_page and i > ref_page and "supplementary" not in found:
                found["supplementary"] = "pdf p%d after References p%d: '%s'" % (i, ref_page, l[:35])
    return found


class _H(HTMLParser):
    def __init__(self):
        super().__init__()
        self.heads, self.cur, self.rows = [], None, 0

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3", "h4"):
            self.cur = ""
        if tag == "tr":
            self.rows += 1

    def handle_data(self, d):
        if self.cur is not None:
            self.cur += d

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4") and self.cur is not None:
            self.heads.append(self.cur.strip())
            self.cur = None


def scan_html(path):
    try:
        h = _H()
        h.feed(open(path, encoding="utf-8", errors="replace").read())
    except Exception as ex:
        return None, "html: %s" % ex
    found = {}
    for t in h.heads:
        for name, rx in SEC_RX.items():
            if rx.search(t) and name not in found:
                found[name] = "html: heading '%s'" % t[:40]
    if h.rows >= 2:
        found["tables"] = "html: table rows"
    return found, None


def scan_file(path):
    low = path.lower()
    if low.endswith(".xml"):
        return scan_xml(path)
    if low.endswith(".pdf"):
        return scan_pdf(path)
    if low.endswith((".html", ".htm")):
        return scan_html(path)
    try:
        txt = open(path, encoding="utf-8", errors="replace").read()
    except Exception as ex:
        return None, "txt: %s" % ex
    return scan_pages([txt]), None


def audit(args):
    latest, events = load_ledger(os.path.join(args.root, "disease-models/wwox/registries/fulltext_read_receipts.jsonl"))
    idx = index_files(args.held)
    flags, stats = [], collections.Counter()
    cache = {}
    for n, key in enumerate(sorted(latest)):
        ev = latest[key]
        depth = ev.get("evidence_depth")
        if depth == "complete_fulltext_read":
            continue
        pop = "primary" if depth == "partial_fulltext_read" else "secondary"
        stats["studies_" + pop] += 1
        files = match_files(key, ev, idx)
        if not files:
            stats["no_artefact_" + pop] += 1
            continue
        main = [p for p in files if not SUPP_NAME_RX.search(os.path.basename(p))]
        supp = [p for p in files if SUPP_NAME_RX.search(os.path.basename(p))]
        contains, notes = {}, []
        for p in main:
            if p not in cache:
                cache[p] = scan_file(p)
            f, err = cache[p]
            if f is None:
                notes.append(err)
                continue
            for s, e in f.items():
                contains.setdefault(s, (p, e))
        if supp:
            contains.setdefault("supplementary", (supp[0], "separate held file by name"))
        if not contains and notes:
            stats["not_assessable_" + pop] += 1
            continue
        stats["assessed_" + pop] += 1
        study_flags = []
        for s in SECTIONS:
            lab = (ev.get("coverage") or {}).get(s)
            if lab in CLASS_A | CLASS_B and s in contains:
                cls = "A" if lab in CLASS_A else "B"
                p, e = contains[s]
                study_flags.append((key, pop, depth, s, lab, cls, os.path.relpath(p, args.held[0]) if p.startswith(args.held[0]) else p, e))
        flags += study_flags
        if any(f[5] == "A" for f in study_flags):
            stats["with_A_" + pop] += 1
        if any(f[5] == "B" for f in study_flags):
            stats["with_B_" + pop] += 1
        if study_flags:
            stats["with_any_" + pop] += 1
        if args.limit and n >= args.limit:
            break
    return flags, stats


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", required=True)
    ap.add_argument("--held", action="append", required=True)
    ap.add_argument("--seed", type=int, default=20261124)
    ap.add_argument("--sample", type=int, default=15)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    flags, stats = audit(args)
    print("#key\tpopulation\tdepth\tsection\treceipt_label\tclass\tartefact\tevidence")
    for f in flags:
        print("\t".join(f))
    print("#SUMMARY " + json.dumps(dict(stats), sort_keys=True))
    prim = sorted((f for f in flags if f[1] == "primary"), key=lambda f: (f[0], f[3]))
    a = [f for f in prim if f[5] == "A"]
    b = [f for f in prim if f[5] == "B"]
    rng = random.Random(args.seed)
    na = min(len(a), 8)
    pick = rng.sample(a, na) if na else []
    nb = min(len(b), args.sample - len(pick))
    pick += rng.sample(b, nb) if nb else []
    print("#SAMPLE seed=%d universe_primary=%d (A=%d,B=%d)" % (args.seed, len(prim), len(a), len(b)))
    for f in pick:
        print("#S\t" + "\t".join(f))


if __name__ == "__main__":
    sys.exit(main())
