#!/usr/bin/env python3
"""Audit of the shareable repurposing view (IT5 P13): is every embedded content distributable?

The allowlist (view/shareable_sources.json) is a mechanism. This tool is the proof that the mechanism did
what it says, read from the BYTES of the shareable output and compared with the FULL catalogue:

  1. Provenance map. Every string, number and key of the embedded JSON is assigned to a provenance rule
     (own text, bibliographic fact, identifier, count, class-A third-party row, source metadata). A field no
     rule names fails the audit, so a new field cannot slip in unclassified.
  2. Forbidden-value scan. The reference set is built from the full catalogue (catalog/catalog.jsonl.gz and
     coverage/associations.jsonl.gz): the names and synonyms of records whose name source is not on the
     allowlist, ChEMBL curated-mechanism wording, DrugBank/ChEBI/ATC/UNII/InChIKey/MATRIX identifiers. Any of
     them found in a string of the output (JSON leaf, visible text, attribute, script literal) fails the audit,
     unless the very same wording is also in the repository's own text (cards, needs, lead records, the page's
     own strings and code): the co-attested values are counted and reported, never silently dropped.
  3. Structural checks. Withheld rows carry an identifier and counts only; per-row status and modality are
     empty; per-pair target lists and link sources come only from class-A claim sources and are re-derived
     from the catalogue (claim source of the row in catalog.jsonl.gz), not from the builder's own list;
     every catalogue claim source is classified; no link leaves the document except to public hosts; no
     repository-relative path is a link; no e-mail address.
  4. Dynamic surfaces (needs a Chromium binary): the rendered first screen with every <details> open, every
     card's export view, the standalone-HTML download of every card, the comparison view, and the PDF text of
     the combined export are scanned with the same forbidden values.
  5. Provenance of the cards' own text (needs the local full-text corpus): longest verbatim run of every
     output string against the full texts, abstracts and label sections held locally. Bibliographic titles
     are facts and listed apart; a run over the limit that is not a short, attributed quotation fails.

  python3 -B framework/scripts/repurposing_shareable_audit.py audit [--html FILE] [--dynamic] [--text-corpus DIR]
  python3 -B framework/scripts/repurposing_view.py audit-shareable            # same, through the view tool

Exit 0 only when no violation was found. Not legal advice: it checks that the output matches the policy
file, and the policy file is the licence reading of catalog/README.md.
"""
from __future__ import annotations

import argparse
import gzip
import html as htmlmod
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_view as rv  # noqa: E402

SCHEMA = "legend.wwox.repurposing_view.shareable_audit/1"
GRAM = 6                       # words per n-gram of the forbidden-value index
MAX_VERBATIM_WORDS = 25        # longest unquoted run shared with a third-party text before the audit fails
WORDING_MAX_WORDS = 8          # a ChEMBL mechanism / target label our own text also contains may be this long (a label, not a passage)
SHORT_QUOTE_MAX = 12           # a marked quotation up to this long needs no attribution phrase
ATTRIBUTED_QUOTE_MAX = 30      # a quotation in marks with an attribution phrase may be up to this long
PUBLIC_HOSTS = {"dgidb.org", "civicdb.org", "www.docm.info", "open.fda.gov", "huggingface.co", "www.ebi.ac.uk", "www.guidetopharmacology.org",
                "dsld.od.nih.gov", "pubmed.ncbi.nlm.nih.gov", "doi.org", "www.genenames.org", "www.nlm.nih.gov", "creativecommons.org", "opendatacommons.org"}
ATTRIBUTION_WORDS = re.compile(r"(authors? (write|state|note|say|report|conclude)|per the .{0,40}(source|paper|study|abstract)|according to|the abstract|the label)", re.I)

# ---------------------------------------------------------------------------- provenance rules (generalised JSON path -> class)
# class: OWN own text or computation; UI own Italian orientation text; BIBLIO bibliographic fact (A); ID identifier only;
# COUNT count derived from a source; SRC_A row or attribute of a class-A source; SRC_META facts about a source (state, version, licence);
# EMPTY must hold no value in the shareable build.
PATH_RULES: list[tuple[str, str, str]] = [
    (r"^\.funnel\.excluded_rows\.alias_risk_rows_unresolved\[\]\.catalogue_id$", "ID", "catalogue identifier of an excluded row (name and gene withheld)"),
    (r"^\.funnel\.excluded_rows\.alias_risk_rows_unresolved\[\]\.", "EMPTY", "compound name and gene of an excluded DGIdb row: not embedded"),
    (r"^\.ui\.", "UI", "Italian orientation text (builder data UI_IT and siblings)"),
    (r"^\.rows\[\]\.(id|kind)$", "ID", "catalogue row identifier and row kind"),
    (r"^\.rows\[\]\.(dup|rec|tr|w)$", "COUNT", "record counts of a catalogue row"),
    (r"^\.rows\[\]\.name$", "ROWNAME", "card name (own text), opaque identifier, or a class-A name source"),
    (r"^\.rows\[\]\.acc\[\]$", "SRC_A", "access category stated from openFDA NDC (class A) or an absence statement"),
    (r"^\.rows\[\]\.(st|mod)\[\]$", "EMPTY", "status class and modality derive from ChEMBL/MATRIX/DGIdb statements: not embedded"),
    (r"^\.rows\[\]\.cards\[\]\.(id|att|path)$", "OWN", "card attachment (in-page anchor)"),
    (r"^\.pairs\[\]\.l1\.(state|n_assoc|readout_only|why|stale)$", "OWN", "level-1 state, association count and note computed by the coverage tool"),
    (r"^\.pairs\[\]\.l1\.withheld$", "COUNT", "number of association rows withheld by the allowlist"),
    (r"^\.pairs\[\]\.l1\.(targets|pathway)\[\]$", "SRC_A", "gene symbols (HGNC) of class-A association rows"),
    (r"^\.pairs\[\]\.l1\.sources\[\]$", "SRC_A", "provenance tag of a class-A association row"),
    (r"^\.pairs\[\]\.(l2|l3|l4|x|n|r)(\.|\[\]|$)", "OWN", "levels 2-4, indices: computed from cards and needs"),
    (r"^\.pairs\[\]\.p\.cr\.pha\[\]\[\]$", "EMPTY", "status classes of a row derive from ChEMBL/DGIdb/MATRIX statements: not embedded in pair objects"),
    (r"^\.pairs\[\]\.p\.cr\.dir\[\]\[\]$", "SRC_A", "criteria: class-A link sources and class-A targets"),
    (r"^\.pairs\[\]\.p\.", "OWN", "priority criteria computed by the coverage tool"),
    (r"^\.strings\[\]$", "OWN", "string table of repeated coverage-tool sentences"),
    (r"^\.cur\.cands\[\]\.(pmids\[\]\.(id|role)|dois\[\])$", "BIBLIO", "PMID / DOI of a cited work"),
    (r"^\.cur\.cands\[\]\.pmids\[\]\.(title|journal|year)$", "BIBLIO", "title, journal, year of a cited work (bibliographic facts)"),
    (r"^\.cur\.cands\[\]\.brief\.sources\[\]\.(kind|id)$", "BIBLIO", "PMID / ChEMBL identifier of an essential source of the one-page synthesis"),
    (r"^\.cur\.cands\[\]\.brief\.sources\[\]\.(title|journal|year)$", "BIBLIO", "title, journal, year of an essential source (bibliographic facts)"),
    (r"^\.cur\.evidence_graph\.chains\[\]\.(nodes\[\]\.pmids\[\]|edges\[\]\.src\.id)$", "BIBLIO", "PMID cited by the hand-authored evidence graph"),
    (r"^\.cur\.evidence_graph\.chains\[\]\.edges\[\]\.src\.title$", "BIBLIO", "title of a cited work (bibliographic fact, from the title cache)"),
    (r"^\.cur\.cands\[\]\.chembl\[\]$", "ID", "ChEMBL identifier of a compound named by a card"),
    (r"^\.cur\.cands\[\]\.actions\[\]\.(need|target|action|cons|n)$", "SRC_A", "stated action on a target, from class-A claim sources only"),
    (r"^\.cur\.cands\[\]\.access\[\]$", "SRC_A", "access category stated from openFDA NDC or an absence statement"),
    (r"^\.cur\.cands\[\]\.", "OWN", "card text and computed positions (provenance of the prose: see text audit)"),
    (r"^\.cur\.needs\[\]\.obs\[\]\.(cite)$", "BIBLIO", "title, journal, year of a cited work"),
    (r"^\.cur\.needs\[\]\.obs\[\]\.pmid$", "BIBLIO", "PMID of the observation source"),
    (r"^\.cur\.ranking\.units\[\]\.(pmids\[\]|views\.(broad|partial)\.evidence\.pmids\[\])$", "BIBLIO", "PMID of a cited work (ranking)"),
    (r"^\.cur\.ranking\.units\[\]\.(access|access_cats\[\])$", "SRC_A", "access statement of a ranked intervention: class-A sources (openFDA NDC, MATRIX) only in the shareable edition; other categories are withheld"),
    (r"^\.cur\.(needs|threads|groups|gaps|goals|tracks|scopes|group_note|meta|evidence_graph|work_order|selection|hypotheses|predictive|contexts|ranking)(\.|\[\]|$)", "OWN", "needs, threads, positions, evidence graph, work order and the IT7 selection, comparison, predictive-test and context sections: own text or counts computed from own census files"),
    (r"^\.cur\.footer\.", "SRC_META", "attribution footer: sources, licences, credit lines"),
    (r"^\.access\.", "COUNT", "catalogue-wide counts and category labels (no compound)"),
    (r"^\.(funnel|matrix_summary|dispositions|observations|level_defs|leads_note|pair_unit|ranking_note|no_probability|schema|source|exploration_flagged|has_distinct|orphan_priorities)(\.|\[\]|$)", "OWN", "counts and definitions computed from the module's own outputs"),
    (r"^\.excluded_detail\[\]\.(id|name|src)$", "ID", "catalogue identifier of an excluded row"),
    (r"^\.excluded_detail\[\]\.(reason|n_needs|genes\[\])$", "COUNT", "reason class and counts of an excluded row"),
    (r"^\.card_leads\[\]\.", "OWN", "lead dispositions attached to cards"),
    (r"^\.leads\[\]\.catalogue_ids\[\]$", "ID", "catalogue identifiers"),
    (r"^\.leads\[\]\.", "OWN", "lead dispositions written in this repository"),
    (r"^\.needs\[\]\.", "OWN", "needs records written in this repository"),
    (r"^\.tech\.", "SRC_META", "state, version, licence and digests of the sources"),
]
L1_NAMES = ["state", "n_assoc", "targets", "sources", "readout_only", "why", "pathway", "stale", "withheld"]

# Paths whose strings are allowed to coincide with a forbidden name (bibliographic titles are checked against the title cache; category labels
# and source labels are not compound names). Every suppression is counted in the report.
EXEMPT_NAME_HITS = [
    (r"^\.cur\.cands\[\]\.pmids\[\]\.title$", "bibliographic title (validated against the title cache)"),
    (r"^\.cur\.cands\[\]\.brief\.sources\[\]\.title$", "bibliographic title (validated against the title cache)"),
    (r"^\.cur\.cands\[\]\.pmids\[\]\.journal$", "bibliographic journal name (validated against the journals of the cache)"),
    (r"^\.cur\.cands\[\]\.brief\.sources\[\]\.journal$", "bibliographic journal name (validated against the journals of the cache)"),
    (r"^\.cur\.evidence_graph\.chains\[\]\.edges\[\]\.src\.title$", "bibliographic title (validated against the title cache)"),
    (r"^\.cur\.needs\[\]\.obs\[\]\.cite$", "bibliographic title (validated against the title cache)"),
    (r"^\.access\.", "category labels of catalogue-wide counts"),
    (r"^\.tech\.", "names of sources, not compounds"),
]
EXEMPT_RE = [(re.compile(p), why) for p, why in EXEMPT_NAME_HITS]


def norm(s: str) -> str:
    return " ".join(re.findall(r"[^\W_]+", htmlmod.unescape(str(s)).lower()))


def strip_cite(s: str) -> str:
    """'Title. (Journal (Edition), 2026)' -> 'Title.' (the journal may carry its own parentheses)."""
    m = re.search(r",\s*\d{4}\)$", s)
    if not m:
        return s
    depth = 0
    for i in range(len(s) - 1, -1, -1):
        depth += (s[i] == ")") - (s[i] == "(")
        if depth == 0:
            return s[:i].rstrip()
    return s


def tokens(s: str) -> list[str]:
    return re.findall(r"[^\W_]+", htmlmod.unescape(str(s)).lower())


def grams(words: list[str], n: int = GRAM):
    for k in range(1, n + 1):
        for i in range(len(words) - k + 1):
            yield " ".join(words[i:i + k])


# ---------------------------------------------------------------------------- extraction
DATA_RE = re.compile(r'<script id="data" type="application/json">(.*?)</script>', re.S)


def extract_payload(text: str) -> dict:
    m = DATA_RE.search(text)
    if not m:
        raise SystemExit("no embedded data object found")
    return json.loads(m.group(1).replace("<\\/", "</").replace("<\\!--", "<!--"))


def rest_of_page(text: str) -> str:
    return DATA_RE.sub("", text)


def visible_surfaces(text: str) -> list[tuple[str, str]]:
    """Strings of the page outside the data object: visible text, attribute values, script and style text."""
    rest = rest_of_page(text)
    out = []
    for m in re.finditer(r"<(script|style)[^>]*>(.*?)</\1>", rest, re.S):
        out.append((f"<{m.group(1)}>", m.group(2)))
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", rest, flags=re.S)
    for m in re.finditer(r'\s([\w:-]+)="([^"]*)"', body):
        out.append((f"@{m.group(1)}", m.group(2)))
    out.append(("html-text", re.sub(r"<[^>]+>", " ", body)))
    return out


def walk(o, path=""):
    """(generalised path, value, is_key) for every key and every scalar of the payload; pair levels get named positions."""
    if isinstance(o, dict):
        for k, v in o.items():
            yield path + "." + k, k, True
            yield from walk(v, path + "." + k)
    elif isinstance(o, list):
        if path == ".pairs[]" and False:
            return
        for i, v in enumerate(o):
            yield from walk(v, path + "[]")
    else:
        yield path, o, False


def named_pairs(P: dict):
    """Rewrite the positional l1 list of each pair to a dict so that its fields can carry rules."""
    out = []
    for p in P.get("pairs") or []:
        q = dict(p)
        if isinstance(q.get("l1"), list):
            q["l1"] = {n: v for n, v in zip(L1_NAMES, q["l1"])}
        out.append(q)
    return out


# ---------------------------------------------------------------------------- reference sets built from the full catalogue
class Reference:
    def __init__(self, dr: Path):
        self.dr = dr
        self.allow = rv.load_allowlist(dr)
        allowed_name_sources = set((self.allow.get("name_sources") or {}).keys())
        self.names: dict[str, str] = {}            # normalised forbidden name -> record id
        self.allowed_names: set[str] = set()       # names a class-A name source states
        self.ident: dict[str, str] = {}            # forbidden identifier -> kind
        self.texts: dict[str, str] = {}            # normalised long wording (ChEMBL mechanism, action text) -> record id
        self.claim_rows: Counter = Counter()       # claim source -> rows in the catalogue
        self.claims: dict[tuple, set] = defaultdict(set)   # (record id, gene) -> claim sources
        self.name_records: dict[str, set] = defaultdict(set)   # normalised name or synonym -> record ids
        self.rec_genes: dict[str, dict] = defaultdict(dict)    # record id -> gene -> claim sources
        self.records = 0
        self.family_of: dict[str, str] = {}
        with gzip.open(dr / "catalog/catalog.jsonl.gz", "rt", encoding="utf-8") as fh:
            for line in fh:
                e = json.loads(line)
                self.records += 1
                allowed_name = e.get("name_source") in allowed_name_sources
                cand = [] if allowed_name else [e.get("name")]
                cand += list(e.get("synonyms") or [])
                cand.append((e.get("ids") or {}).get("dgidb_drug_name"))
                for sr in e.get("source_records") or []:
                    if sr.get("source") in ("matrix", "openfda_ndc") and sr.get("name"):
                        self.allowed_names.add(norm(sr["name"]))
                    elif sr.get("dgidb_drug_name"):
                        cand.append(sr["dgidb_drug_name"])
                if allowed_name and e.get("name"):
                    self.allowed_names.add(norm(e["name"]))
                for n in cand:
                    k = norm(n) if n else ""
                    if not k or re.fullmatch(r"chembl\d+", k) or len(k) < 4 or (len(k) < 5 and not k.isalpha()):
                        continue
                    self.names.setdefault(k, e["id"])
                    self.name_records[k].add(e["id"])
                ids = e.get("ids") or {}
                for kind in ("drugbank", "chebi", "unii", "matrix_id", "iuphar_ligand", "concept_ids"):
                    v = ids.get(kind)
                    for x in (v if isinstance(v, list) else ([v] if v else [])):
                        if len(str(x)) >= 6 and not str(x).isdigit():
                            self.ident[str(x)] = kind
                for kind in ("inchikey", "skeleton_key"):
                    if ids.get(kind):
                        self.ident[str(ids[kind])] = kind
                for a in e.get("atc") or []:
                    self.ident[str(a)] = "atc"
                for t in e.get("targets") or []:
                    cs = t.get("claim_source") or t.get("source")
                    self.claim_rows[cs] += 1
                    if t.get("gene"):
                        self.claims[(e["id"], t["gene"])].add(cs)
                        self.rec_genes[e["id"]].setdefault(t["gene"], set()).add(cs)
                    for sym in t.get("gene_symbols") or []:
                        self.claims[(e["id"], sym)].add(cs)
                        self.rec_genes[e["id"]].setdefault(sym, set()).add(cs)
                    for fld in ("mechanism_of_action", "target_name", "action_raw"):
                        w = norm(t.get(fld) or "")
                        if len(w.split()) >= 3:
                            self.texts.setdefault(w, e["id"])
        self.allowed_names -= {""}
        for k in list(self.names):
            if k in self.allowed_names:
                del self.names[k]
        self.assocs = rv.read_associations(dr)
        self.allowed_tags = {"DGIdb:" + k for k in (self.allow.get("dgidb_claim_sources") or {})}
        # genes backed by an allowed association, per (family, need) and per need
        self.gene_ok_pair: dict[tuple, set] = defaultdict(set)
        self.gene_ok_need: dict[str, set] = defaultdict(set)
        self.assoc_unverified = 0
        for a in self.assocs:
            tag = rv.assoc_tag(a)
            if tag not in self.allowed_tags:
                continue
            g = a.get("target") or a.get("gene")
            src = tag[6:]
            # independent re-derivation: the claim source must be on the catalogue record itself
            if src not in self.claims.get((a.get("catalogue_id"), a.get("gene")), set()) and src not in self.claims.get((a.get("catalogue_id"), g), set()):
                self.assoc_unverified += 1
                continue
            self.gene_ok_pair[(a.get("family"), a["need"])].update(x for x in (a.get("target"), a.get("gene")) if x)
            self.gene_ok_need[a["need"]].update(x for x in (a.get("target"), a.get("gene")) if x)
        pol = self.allow.get("claim_source_policy") or {}
        # (name, gene) pairs asserted ONLY by class-B/C claim sources, derived from the catalogue (a pair that any record of that name also gets from a class-A source is not in it)
        class_a = {k for k, v in pol.items() if v.get("class") == "A"}
        self.pair_bc: dict[str, set] = {}
        for k, rids in self.name_records.items():
            if k not in self.names:
                continue
            bc, a_ = set(), set()
            for rid in rids:
                for g, srcs in self.rec_genes.get(rid, {}).items():
                    (a_ if srcs & class_a else bc).add(g)
            bc = {g for g in bc - a_ if len(g) >= 3}
            if bc:
                self.pair_bc[k] = bc
        self.unclassified_sources = sorted(s for s in self.claim_rows if s not in pol)
        self.policy_mismatch = sorted(k for k, v in pol.items() if (v.get("class") == "A") != (k in (self.allow.get("dgidb_claim_sources") or {})) and k not in ("ChEMBL", "ChEMBL curated mechanism"))
        # titles cache for the bibliographic exemption
        self.titles = set()
        self.journals = set()           # exact journal strings of the title cache: a journal can share a name with a catalogue record (IT8 P5: "Nature")
        tp = dr / rv.TITLES_NAME
        if tp.exists():
            for v in (rv.jload(tp).get("titles") or {}).values():
                if v.get("title"):
                    self.titles.add(norm(v["title"]))
                if v.get("journal"):
                    self.journals.add(v["journal"])
        for f in (dr / "join/pubmed_cache").glob("*.json"):
            try:
                d = rv.jload(f)
                for t in (d.get("title"), (d.get("result") or {}).get("title") if isinstance(d.get("result"), dict) else None):
                    if t:
                        self.titles.add(norm(t))
            except Exception:
                pass
        self.card_names = set()
        for cid, (card, _) in rv.load_cards(dr).items():
            self.card_names.add(card["input"]["candidate"]["name"].split(" (")[0].strip())
        self.card_cat_ids = set()
        lk = dr / "catalog/card_links.json"
        if lk.exists():
            for v in (rv.jload(lk).get("cards") or {}).values():
                for x in v.get("links") or []:
                    if x.get("catalogue_id"):
                        self.card_cat_ids.add(x["catalogue_id"])
        self.own_grams = self._own_corpus()

    def _own_corpus(self) -> set:
        parts = []
        for pat in ("cards/*.json", "cards_early/*.json"):
            for f in sorted(self.dr.glob(pat)):
                parts.append(f.read_text(encoding="utf-8"))
        for rel in ("needs/needs.json", "coverage/lead_dispositions.json", "view/assets/curated.html", "view/assets/curated.css", "view/assets/curated.js"):
            if (self.dr / rel).exists():
                parts.append((self.dr / rel).read_text(encoding="utf-8"))
        parts.append(Path(rv.__file__).read_text(encoding="utf-8"))
        return set(grams(tokens(" ".join(parts))))


# ---------------------------------------------------------------------------- the audit
class Report:
    def __init__(self):
        self.violations: list[dict] = []
        self.suppressed: Counter = Counter()
        self.coattested: Counter = Counter()
        self.wording: list[dict] = []
        self.pair_unmarked: list[dict] = []
        self.rules: dict[str, dict] = {}
        self.info: dict = {}

    def bad(self, kind: str, where: str, value) -> None:
        self.violations.append({"kind": kind, "where": where, "value": str(value)[:200]})

    @property
    def ok(self) -> bool:
        return not self.violations


def classify_paths(P: dict, rep: Report) -> None:
    rules = [(re.compile(p), c, w) for p, c, w in PATH_RULES]
    pairs = named_pairs(P)
    P2 = dict(P, pairs=pairs)
    seen_unclassified = set()
    for path, val, is_key in walk(P2):
        if is_key:
            continue
        for rx, cls, why in rules:
            if rx.search(path):
                r = rep.rules.setdefault(rx.pattern, {"class": cls, "why": why, "values": 0, "chars": 0})
                r["values"] += 1
                r["chars"] += len(str(val))
                if cls == "EMPTY":
                    rep.bad("field-must-be-empty", path, val)
                break
        else:
            if path not in seen_unclassified:
                seen_unclassified.add(path)
                rep.bad("unclassified-field", path, val)


def scan_strings(items: list[tuple[str, str]], ref: Reference, rep: Report, label: str) -> None:
    """Forbidden names, wording and identifiers in a list of (where, string)."""
    names, texts = ref.names, ref.texts
    long_names = {k: v for k, v in names.items() if len(k.split()) > GRAM}
    long_first = defaultdict(list)
    for k in long_names:
        long_first[" ".join(k.split()[:GRAM])].append(k)
    for k, v in texts.items():
        if len(k.split()) > GRAM:
            long_first[" ".join(k.split()[:GRAM])].append(k)
    id_rx = re.compile(r"[A-Za-z0-9:_-]{5,}")
    tl = sorted((t for t in ref.titles if len(t.split()) >= 4), key=len, reverse=True)
    title_rx = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(t) for t in tl) + r")(?!\w)") if tl else None
    jl = sorted({norm(j) for j in ref.journals if norm(j)}, key=len, reverse=True)
    journal_rx = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(j) for j in jl) + r")\s+(?:19|20)\d{2}(?!\w)") if jl else None
    for where, s in items:
        if not isinstance(s, str) or not s:
            continue
        w = tokens(s)
        ns = " ".join(w)
        if title_rx:
            ns = title_rx.sub(" ", ns)   # a bibliographic title is a fact wherever it is printed; it is validated against the cache, then masked
        if journal_rx:
            ns = journal_rx.sub(" ", ns)   # "(Journal, 2026)" in a printed citation: a journal of the cache followed by a year is a bibliographic fact, not a compound name
        if title_rx or journal_rx:
            w = ns.split()
        exempt = next((why for rx, why in EXEMPT_RE if rx.search(where)), None)
        if exempt and "title" in exempt:
            t = strip_cite(s) if where.endswith(".cite") else s
            if norm(t) not in ref.titles:
                rep.bad("title-not-in-cache", where, s)
        elif exempt and "journal" in exempt and s not in ref.journals:
            rep.bad("journal-not-in-cache", where, s)
        done = set()
        for g in grams(w):
            hit = None
            if g in names and len(g.split()) <= GRAM:
                hit = ("forbidden-name", g, names[g])
            elif g in texts and len(g.split()) <= GRAM:
                hit = ("forbidden-wording", g, texts[g])
            elif g in long_first:
                for k in long_first[g]:
                    if k in ns:
                        hit = ("forbidden-name" if k in names else "forbidden-wording", k, names.get(k) or texts.get(k))
                        break
            if not hit or hit[1] in done:
                continue
            done.add(hit[1])
            if hit[1] in ref.own_grams or all(x in ref.own_grams for x in grams(hit[1].split(), min(GRAM, len(hit[1].split())))):
                rep.coattested[hit[0]] += 1
                if hit[0] == "forbidden-wording":   # third-party wording that our own text also contains: a short label is reported, a long one is copying
                    rep.wording.append({"wording": hit[1], "record": hit[2], "where": f"{label}:{where}", "words": len(hit[1].split())})
                    if len(hit[1].split()) > WORDING_MAX_WORDS:
                        rep.bad("third-party-wording-in-own-text", f"{label}:{where}", f"{len(hit[1].split())} words: {hit[1][:120]}")
                continue
            if exempt:
                rep.suppressed[exempt] += 1
                continue
            if any(hit[1] in t for t in ref.titles):   # a PDF text layer breaks lines inside a title: the hit is part of a bibliographic title
                rep.suppressed["inside a bibliographic title (line-broken text layer)"] += 1
                continue
            rep.bad(hit[0], f"{label}:{where}", f"{hit[1]!r} ({hit[2]})")
        for m in id_rx.finditer(s):
            kind = ref.ident.get(m.group(0))
            if kind:
                rep.bad("forbidden-identifier:" + kind, f"{label}:{where}", m.group(0))
        for rx, kind in ((r"\bDB\d{5}\b", "drugbank"), (r"\bCHEBI:\d+\b", "chebi"), (r"\bEC:\d{4,}\b", "matrix_id"), (r"\b[A-Z]{14}-[A-Z]{10}-[A-Z]\b", "inchikey")):
            for m in re.finditer(rx, s):
                rep.bad("forbidden-identifier:" + kind, f"{label}:{where}", m.group(0))
        if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}", s):
            rep.bad("e-mail-like-string", f"{label}:{where}", s[:80])


MARKER_RX = re.compile(r"\b(GtoPdb|Guide[- ]to[- ]Pharmacology|PharmGKB|ClinPGx|DTC|TTD|JAX[- ]CKB|OncoKB|claim source|target rows?|max phase|curated mechanism)\b"
                       r"|\b(ChEMBL|DGIdb|catalogue)\b[^.;]{0,40}\b(mechanism|rows?|document|statement|potency|activity|action|inhibitor|agonist|antagonist)\b", re.I)
SENT_RX = re.compile(r"(?<=[.;])\s+")
FILE_ALLOWED = {"README.md", "NOTICE.md", "COMPARISON.md", "manifest.json", "TEXT_PROVENANCE.json", "index.html"}


def pair_scan(items: list[tuple[str, str]], ref: Reference, rep: Report, label: str, literature=None) -> None:
    """A compound-target pair asserted only by class-B/C claim sources must not be stated in prose or in a pair object.
    Per sentence: a catalogue name and a gene symbol that the catalogue gives that name only through class-B/C claims.
    It fails when the sentence names a database or claim (marker) or the compound is catalogue-only (no cited full text, not a card subject)."""
    names = ref.pair_bc
    tl = sorted((t for t in ref.titles if len(t.split()) >= 4), key=len, reverse=True)
    title_rx = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(t) for t in tl) + r")(?!\w)") if tl else None
    seen = set()
    for where, s in items:
        if not isinstance(s, str) or len(s) < 6 or where.endswith("#key"):
            continue
        for sent in SENT_RX.split(s):
            ns = " ".join(tokens(sent))
            if title_rx:
                ns = title_rx.sub(" ", ns)
            w = ns.split()
            if not w:
                continue
            genes = set(re.findall(r"[A-Za-z0-9]+", sent))
            for g in grams(w):
                bc = names.get(g)
                if not bc:
                    continue
                common = bc & genes
                if not common:
                    continue
                marker = MARKER_RX.search(sent)
                subject = bool(ref.name_records.get(g, set()) & ref.card_cat_ids)
                attested = literature.contains(g) if literature is not None else None
                catalogue_only = (attested is False) and not subject
                key = (where, g, tuple(sorted(common)))
                if key in seen:
                    continue
                seen.add(key)
                if marker or catalogue_only:
                    rep.bad("class-bc-compound-target-pair-in-text", f"{label}:{where}", f"{g!r} + {sorted(common)} ({'marker ' + marker.group(0) if marker else 'catalogue-only compound'}): {sent[:120]}")
                else:
                    rep.pair_unmarked.append({"name": g, "genes": sorted(common), "attested": attested, "subject": subject})


def file_token_scan(items: list[tuple[str, str]], rep: Report, label: str) -> None:
    for where, s in items:
        if not isinstance(s, str):
            continue
        for m in rv.FILE_TOKEN_RE.finditer(s):
            tok = m.group(0)
            if tok in FILE_ALLOWED or tok.startswith("class_b/"):
                continue
            rep.bad("repository-file-name", f"{label}:{where}", tok)


def structural(P: dict, ref: Reference, rep: Report) -> None:
    allow = ref.allow
    ok_tags = ref.allowed_tags
    # every catalogue claim source is classified; the allowlist equals the class-A set
    for s in ref.unclassified_sources:
        rep.bad("unclassified-claim-source", "catalogue", s)
    for s in ref.policy_mismatch:
        rep.bad("policy-mismatch", "shareable_sources.json", s)
    if ref.assoc_unverified:
        rep.bad("association-not-on-catalogue-record", "coverage/associations.jsonl.gz", f"{ref.assoc_unverified} allowed association rows have no matching claim on the catalogue record")
    # rows
    allowed_cats = {c for c in ("prescription", "OTC", "unknown/unverified")}
    for i, r in enumerate(P["rows"]):
        w = f".rows[{i}]"
        if r.get("w"):
            if r["acc"] or r["st"] or r["mod"]:
                rep.bad("withheld-row-carries-attributes", w, r["id"])
            if not re.fullmatch(r"[A-Za-z0-9_.:-]+", r["name"]):
                rep.bad("withheld-row-name", w, r["name"])
        else:
            nm = r["name"]
            if nm not in ref.card_names and norm(nm) not in ref.allowed_names:
                rep.bad("row-name-not-from-card-or-class-A-name-source", w, nm)
            if r["st"] or r["mod"]:
                rep.bad("row-status-or-modality-embedded", w, r["id"])
            for a in r["acc"]:
                if a not in allowed_cats and not rv.access_category_allowed(a, allow)[0]:
                    rep.bad("access-category-not-class-A", w, a)
    # pair-level sources and genes
    rows = P["rows"]
    need_ids = [n["id"] for n in P["needs"]]
    for i, p in enumerate(named_pairs(P)):
        l1 = p.get("l1")
        if not isinstance(l1, dict):
            continue
        fam = rows[p["r"]]["id"]
        need = need_ids[p["n"]]
        for t in l1.get("sources") or []:
            if t not in ok_tags:
                rep.bad("pair-link-source-not-class-A", f".pairs[{i}].l1", t)
        ok_genes = ref.gene_ok_pair.get((fam, need), set())
        for g in (l1.get("targets") or []) + (l1.get("pathway") or []):
            if g not in ok_genes:
                rep.bad("pair-target-not-backed-by-class-A-row", f".pairs[{i}].l1", f"{fam} / {need} / {g}")
        pc = (p.get("p") or {}).get("cr", {}).get("dir")
        if pc:
            for t in pc[1]:
                if t not in ok_tags:
                    rep.bad("criteria-link-source-not-class-A", f".pairs[{i}].p", t)
            for g in pc[2]:
                if g not in ok_genes:
                    rep.bad("criteria-target-not-backed-by-class-A-row", f".pairs[{i}].p", f"{fam} / {need} / {g}")
    for c in P["cur"]["cands"]:
        for a in c["actions"]:
            if a["target"] not in ref.gene_ok_need.get(a["need"], set()):
                rep.bad("card-action-target-not-backed-by-class-A-row", c["id"], a)
        for a in c["access"]:
            if a not in allowed_cats and not rv.access_category_allowed(a, allow)[0]:
                rep.bad("card-access-not-class-A", c["id"], a)
        if c.get("card_path") and (c["card_path"].startswith(("../", "/", "cards/")) or ".." in c["card_path"].split("/")[:1]):
            rep.bad("repository-relative-card-path", c["id"], c["card_path"])
    for coll, key in ((P["rows"], "cards"), (P["needs"], "cards")):
        for x in coll:
            for cd in x.get(key) or []:
                if cd.get("path") and not str(cd["path"]).startswith("#"):
                    rep.bad("non-anchor-card-link", x.get("id"), cd["path"])
    for c in P["card_leads"]:
        for cd in c["cards"]:
            if cd.get("path") and not str(cd["path"]).startswith("#"):
                rep.bad("non-anchor-card-link", c.get("row"), cd["path"])
    # footer: what is listed as embedded must be class A
    for e in P["cur"]["footer"]["embedded"]:
        if not (e.get("licence") and e.get("attribution")):
            rep.bad("embedded-source-without-licence-or-credit", "footer", e.get("label"))
        lab = e.get("label", "")
        if any(x in lab for x in ("ChEMBL", "GtoPdb", "ClinPGx", "PharmGKB", "NCI", "DSLD", "DTC", "TTD")):
            rep.bad("non-class-A-source-listed-as-embedded", "footer", lab)
    emb_tags = {e["label"] for e in P["cur"]["footer"]["embedded"]}
    rep.info["embedded_labels"] = sorted(emb_tags)


def link_checks(text: str, rep: Report, rendered_hrefs: list[str] | None = None) -> None:
    rest = rest_of_page(text)
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", rest, flags=re.S)
    hrefs = re.findall(r'href="([^"]*)"', body) + list(rendered_hrefs or [])
    bad = [h for h in hrefs if not (h.startswith(("#", "https://", "http://")))]
    for h in bad:
        rep.bad("link-not-document-or-public-url", "href", h)
    for h in hrefs:
        if h.startswith(("http://", "https://")):
            host = h.split("/")[2]
            if host not in PUBLIC_HOSTS and not host.endswith((".nih.gov", ".ebi.ac.uk")):
                rep.bad("link-host-not-public-reference", "href", h)
    if re.search(r'(src|href)="\.\./', text):
        rep.bad("repository-relative-link", "html", "../")
    if re.search(r"<link |@import|url\(\s*https?:|src=\"https?:", rest):
        rep.bad("external-resource-load", "html", "")
    uh = sorted(set(hrefs))
    rep.info["links"] = {"distinct_hrefs": len(uh), "internal_anchors": sum(1 for h in uh if h.startswith("#")), "external_public": sum(1 for h in uh if h.startswith("http")), "hosts": sorted({h.split("/")[2] for h in uh if h.startswith("http")})}


def identifier_census(text: str) -> dict:
    kinds = {"PMID": r"\bPMID[: ]*\d{6,8}\b", "DOI": r"\b10\.\d{4,9}/[^\s\"<>]+", "CHEMBL": r"\bCHEMBL\d+\b", "HGNC": r"\bHGNC:\d+\b", "CAT": r"\bCAT:[A-Z]+:?[A-Za-z0-9]+", "NCT": r"\bNCT\d{8}\b"}
    return {k: len(set(re.findall(rx, text))) for k, rx in kinds.items()}


def audit_html(text: str, dr: Path, ref: Reference | None = None, extra_surfaces: list[tuple[str, str]] | None = None, literature=None) -> tuple[Report, Reference]:
    rep = Report()
    ref = ref or Reference(dr)
    P = extract_payload(text)
    if P.get("source") != "shareable":
        rep.bad("not-a-shareable-build", "source", P.get("source"))
    classify_paths(P, rep)
    structural(P, ref, rep)
    items = []
    P2 = dict(P, pairs=named_pairs(P))
    for path, val, is_key in walk(P2):
        if isinstance(val, str):
            items.append((path + ("#key" if is_key else ""), val))
    scan_strings(items, ref, rep, "data")
    vis = visible_surfaces(text)
    scan_strings(vis, ref, rep, "page")
    pair_scan(items, ref, rep, "data", literature)
    pair_scan(vis, ref, rep, "page", literature)
    file_token_scan(items, rep, "data")
    file_token_scan(vis, rep, "page")
    rhrefs = []
    if extra_surfaces:
        rhrefs = [h for w, v in extra_surfaces if w.startswith("rendered-href") for h in v.split("\n") if h]
        rendered = [x for x in extra_surfaces if not x[0].startswith("rendered-href")]
        scan_strings(rendered, ref, rep, "rendered")
        pair_scan(rendered, ref, rep, "rendered", literature)
        file_token_scan(rendered, rep, "rendered")
    link_checks(text, rep, rhrefs)
    rep.info["identifiers"] = identifier_census(text)
    rep.info["reference"] = {"catalogue_records": ref.records, "forbidden_names": len(ref.names), "forbidden_wordings": len(ref.texts), "forbidden_identifiers": len(ref.ident),
                             "claim_source_rows": dict(sorted(ref.claim_rows.items())), "co_attested": dict(rep.coattested), "pair_unmarked_attested_or_unchecked": {"count": len(rep.pair_unmarked), "unchecked_without_corpus": sum(1 for x in rep.pair_unmarked if x["attested"] is None), "names": sorted({x["name"] for x in rep.pair_unmarked})[:60]}, "co_attested_wording": sorted({(w["wording"], w["record"]) for w in rep.wording}), "suppressed_by_exemption": dict(rep.suppressed)}
    return rep, ref


# ---------------------------------------------------------------------------- dynamic surfaces (Chromium over the DevTools protocol)
def dynamic_surfaces(html_path: Path, P: dict) -> tuple[list[tuple[str, str]], dict]:
    """Rendered text of the first screen (every <details> open), each card's export view and standalone download, the comparison view, and the PDF text of the combined export."""
    import base64
    import shutil
    import subprocess
    import tempfile
    binary = rv.find_chromium()
    info = {"chromium": bool(binary)}
    if not binary:
        return [], info
    ids = [c["id"] for c in P["cur"]["cands"]]
    out: list[tuple[str, str]] = []
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:   # the browser may still be writing its profile when it exits
        cdp = rv.Cdp(binary, td)
        try:
            cdp.call("Page.enable")
            cdp.call("Emulation.setDeviceMetricsOverride", width=1280, height=900, deviceScaleFactor=1, mobile=False)

            def load(frag: str):
                cdp.call("Page.navigate", url="about:blank")
                cdp.events.clear()
                cdp.call("Page.navigate", url=f"file://{html_path}{frag}")
                cdp.wait_event("Page.loadEventFired")
                # IT8: poll for the ready marker and, for an export or section view, for the export area itself; a fixed 350 ms crashed under load
                cdp.wait_for(rv.CUR_READY_JS)
                if frag.startswith(("#export=", "#brief=", "#section=")):
                    cdp.wait_for("(function(){var e=document.getElementById('export-area');return !!e&&e.innerText.length>0})()")
                cdp.settle()

            load("")
            out.append(("rendered:first-screen", cdp.evaluate("(function(){document.querySelectorAll('details').forEach(function(d){d.open=true});return document.body.innerText})()")))
            HREFS = "Array.from(document.querySelectorAll('a[href]')).map(function(a){return a.getAttribute('href')}).join('\\n')"
            out.append(("rendered-href:first-screen", cdp.evaluate(HREFS)))
            n_std = 0
            for sid in ("selection", "hypotheses", "predictive"):   # IT7 P7: the printable sections are scanned like the exports
                load("#section=" + sid)
                out.append((f"rendered:section:{sid}", cdp.evaluate("document.getElementById('export-area').innerText")))
                out.append((f"rendered-href:section:{sid}", cdp.evaluate(HREFS)))
            for cid in ids:
                load("#brief=" + cid)   # IT6 P13: the one-page synthesis and its standalone download are scanned like the dossier
                out.append((f"rendered:brief:{cid}", cdp.evaluate("document.getElementById('export-area').innerText")))
                out.append((f"rendered-href:brief:{cid}", cdp.evaluate(HREFS)))
                bstd = cdp.evaluate("(function(){var cap=null;URL.createObjectURL=function(b){cap=b;return 'blob:x'};var a=document.getElementById('x-dl');if(!a)return Promise.resolve('');a.click();return cap?cap.text():Promise.resolve('')})()")
                if bstd:
                    out.append((f"rendered:brief-standalone:{cid}", re.sub(r"<[^>]+>", " ", bstd)))
                    out.append((f"rendered:brief-standalone-markup:{cid}", bstd))
                load("#export=" + cid)
                out.append((f"rendered:export:{cid}", cdp.evaluate("document.getElementById('export-area').innerText")))
                out.append((f"rendered-href:export:{cid}", cdp.evaluate(HREFS)))
                std = cdp.evaluate("(function(){var cap=null;URL.createObjectURL=function(b){cap=b;return 'blob:x'};var a=document.getElementById('x-dl');if(!a)return Promise.resolve('');a.click();return cap?cap.text():Promise.resolve('')})()")
                if std:
                    n_std += 1
                    out.append((f"rendered:standalone:{cid}", re.sub(r"<[^>]+>", " ", std)))
                    out.append((f"rendered:standalone-markup:{cid}", std))
            for i in range(0, len(ids), 4):
                grp = ids[i:i + 4]
                if len(grp) >= 2:
                    load("#compare=" + ",".join(grp))
                    out.append((f"rendered:compare:{'+'.join(grp)}", cdp.evaluate("document.getElementById('cmp-out').innerText")))
            load("#export=" + ",".join(ids))
            cdp.call("Emulation.setEmulatedMedia", media="print")
            pdf = base64.b64decode(cdp.call("Page.printToPDF", paperWidth=8.27, paperHeight=11.69, printBackground=True, preferCSSPageSize=True)["data"])
            cdp.call("Emulation.setEmulatedMedia", media="")
            info.update({"standalone_downloads": n_std, "exports": len(ids), "pdf_bytes": len(pdf)})
            if shutil.which("pdftotext"):
                pp = Path(td) / "x.pdf"
                pp.write_bytes(pdf)
                txt = subprocess.run(["pdftotext", "-q", str(pp), "-"], capture_output=True, text=True, timeout=120).stdout
                out.append(("rendered:pdf-export-all-cards", txt))
                info["pdf_text_chars"] = len(txt)
            else:
                info["pdf_text"] = "pdftotext not available: the PDF is a print render of the export view scanned above"
        finally:
            cdp.close()
    return out, info


# ---------------------------------------------------------------------------- provenance of the cards' own text
def read_corpus(corpus_dirs: list[Path]) -> dict[str, list[str]]:
    """Token lists of the third-party texts held locally (full texts, abstracts, label JSON)."""
    import subprocess
    texts: dict[str, list[str]] = {}
    for d in corpus_dirs:
        for f in sorted(d.rglob("*")):
            if not f.is_file():
                continue
            ext = f.suffix.lower()
            try:
                if ext in (".xml", ".html", ".htm"):
                    s = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", f.read_text(encoding="utf-8", errors="ignore"), flags=re.S))
                elif ext in (".txt", ".md"):
                    s = f.read_text(encoding="utf-8", errors="ignore")
                elif ext == ".json":
                    s = " ".join(_json_strings(json.loads(f.read_text(encoding="utf-8", errors="ignore"))))
                elif ext == ".pdf":
                    s = subprocess.run(["pdftotext", "-q", str(f), "-"], capture_output=True, text=True, timeout=90).stdout
                else:
                    continue
            except Exception:
                continue
            texts[str(f)] = tokens(s)
    return texts


class Literature:
    """Does a compound name occur in any third-party text held locally (full texts, abstracts, openFDA label JSON)? A name that does not, and is not a card subject,
    entered the repository only through a catalogue row."""

    def __init__(self, texts: dict[str, list[str]]):
        self.blob = " | " + " | ".join(" ".join(w) for w in texts.values()) + " | "
        self.cache: dict[str, bool] = {}

    def contains(self, name: str) -> bool:
        if name not in self.cache:
            self.cache[name] = (" " + name + " ") in self.blob
        return self.cache[name]


def text_overlap(P: dict, corpus_dirs: list[Path], k: int = 7, texts: dict | None = None) -> dict:
    """Longest verbatim run (in words) of each output string against the third-party texts held locally (full texts, abstracts, label JSON)."""
    texts = texts if texts is not None else read_corpus(corpus_dirs)
    idx: dict[str, str] = {}
    for f, w in texts.items():
        for i in range(len(w) - k + 1):
            idx.setdefault(" ".join(w[i:i + k]), f)
    rows = []
    for path, val, is_key in walk(dict(P, ui={}, pairs=[])):
        if not isinstance(val, str) or is_key:
            continue
        w = tokens(val)
        if len(w) < k:
            continue
        hit = [i for i in range(len(w) - k + 1) if " ".join(w[i:i + k]) in idx]
        if not hit:
            continue
        runs, st, pr = [], hit[0], hit[0]
        for h in hit[1:]:
            if h == pr + 1:
                pr = h
            else:
                runs.append((st, pr))
                st = pr = h
        runs.append((st, pr))
        a, b = max(runs, key=lambda r: r[1] - r[0])
        rows.append({"words": b - a + k, "path": path, "run": " ".join(w[a:b + k]), "source": idx[" ".join(w[a:a + k])], "string": val})
    rows.sort(key=lambda r: -r["words"])
    by_ext = Counter(Path(f).suffix.lower().lstrip(".") for f in texts)
    return {"corpus_files": len(texts), "corpus_by_extension": dict(sorted(by_ext.items())), "corpus_words": sum(len(v) for v in texts.values()), "runs": rows}


def _json_strings(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k != "openfda":
                yield from _json_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _json_strings(v)
    elif isinstance(o, str):
        yield o


def judge_text_overlap(res: dict, rep: Report) -> dict:
    """A shared run is acceptable when it is a bibliographic title; or at most MAX_VERBATIM_WORDS words outside quotation marks (a phrase,
    not a passage); or a marked quotation of at most SHORT_QUOTE_MAX words; or a marked quotation of at most ATTRIBUTED_QUOTE_MAX words
    with an attribution phrase in the same string. Anything longer fails."""
    summary = {"titles": 0, "short_unquoted": 0, "short_marked_quotations": [], "attributed_quotations": [], "failures": 0}
    seen = set()
    for r in res["runs"]:
        key = (r["path"], r["string"])
        if key in seen:
            continue
        seen.add(key)
        quoted = _in_quotes(r["string"], r["run"])
        if re.search(r"(title|\.cite)$", r["path"]):
            summary["titles"] += 1
        elif quoted and r["words"] <= SHORT_QUOTE_MAX:
            summary["short_marked_quotations"].append({"words": r["words"], "path": r["path"], "run": r["run"]})
        elif quoted and r["words"] <= ATTRIBUTED_QUOTE_MAX and ATTRIBUTION_WORDS.search(r["string"]):
            summary["attributed_quotations"].append({"words": r["words"], "path": r["path"], "text": r["string"][:300]})
        elif not quoted and r["words"] <= MAX_VERBATIM_WORDS:
            summary["short_unquoted"] += 1
        else:
            summary["failures"] += 1
            rep.bad("verbatim-run-over-limit", r["path"], f'{r["words"]} words: {r["run"][:160]}')
    return summary


def _in_quotes(s: str, run: str) -> bool:
    for m in re.finditer(r"[\"“]([^\"”]{15,})[\"”]|(?<!\w)'([^']{15,})'(?!\w)", s):
        if run in " ".join(tokens(m.group(0))):
            return True
    return False


# ---------------------------------------------------------------------------- CLI
def default_corpus_dirs() -> list[Path]:
    import subprocess
    out = []
    here = rv.ROOT / "files/fulltext"
    if here.exists():
        out.append(here)
    else:
        try:
            common = subprocess.run(["git", "-C", str(rv.ROOT), "rev-parse", "--git-common-dir"], capture_output=True, text=True).stdout.strip()
            p = (Path(common) if Path(common).is_absolute() else rv.ROOT / common).resolve().parent / "files/fulltext"
            if p.exists():
                out.append(p)
        except Exception:
            pass
    return out


LABEL_QUERIES = ['set_id:"082d818a-4f4e-4675-98c6-91db0294e63c"'] + [f'openfda.generic_name:"{n}"' for n in ("VIGABATRIN", "CLOBAZAM", "STIRIPENTOL", "MEMANTINE", "PERAMPANEL", "BUMETANIDE", "ETHOSUXIMIDE", "CANNABIDIOL", "LITHIUM CARBONATE")]


def fetch_labels(out: Path) -> int:
    """Anonymous openFDA drug-label queries for the drugs the cards cite (the set id named in card H02 first). Keyless, no e-mail or tool parameter, one call per query."""
    import time
    import urllib.parse
    import urllib.request
    out.mkdir(parents=True, exist_ok=True)
    rc = 0
    for q in LABEL_QUERIES:
        url = "https://api.fda.gov/drug/label.json?" + urllib.parse.urlencode({"search": q, "limit": 3})
        name = re.sub(r"[^A-Za-z0-9]+", "_", q).strip("_") + ".json"
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                (out / name).write_bytes(r.read())
            print("fetched", name)
        except Exception as e:   # a missing label is reported, never silently skipped
            print("FAILED", q, str(e)[:100])
            rc = 1
        time.sleep(0.5)
    return rc


def render_report(rep: Report, title: str) -> str:
    lines = [f"{title}: {'PASS' if rep.ok else 'FAIL'} ({len(rep.violations)} violation(s))"]
    for k, v in Counter(x["kind"] for x in rep.violations).most_common():
        lines.append(f"  {v:5d}  {k}")
    for x in rep.violations[:25]:
        lines.append(f"      {x['kind']} @ {x['where']}: {x['value']}")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", nargs="?", choices=["audit", "fetch-labels"], help="audit: scan the shareable output against the full catalogue; fetch-labels: save the openFDA label JSON of the drugs the cards cite into --out (anonymous public API call, no key, no contact string) so the text audit can compare with them")
    ap.add_argument("--out", type=Path, default=None, help="fetch-labels: directory for the label JSON files")
    ap.add_argument("--dr", type=Path, default=rv.DEFAULT_DR)
    ap.add_argument("--html", type=Path, action="append", help="file to audit (default: view/index_shareable.html and, when present, view/shareable_package/index.html)")
    ap.add_argument("--dynamic", action="store_true", help="also render the page in Chromium and scan the first screen, every export, standalone download, comparison and the PDF text")
    ap.add_argument("--text-corpus", type=Path, action="append", help="directory of third-party texts for the provenance-of-text audit (default: the local files/fulltext)")
    ap.add_argument("--no-text", action="store_true", help="skip the provenance-of-text audit")
    ap.add_argument("--json", type=Path, default=None, help="write the machine-readable report here")
    a = ap.parse_args(argv)
    if not a.command:
        ap.print_help()
        return 0
    if a.command == "fetch-labels":
        return fetch_labels(a.out or Path("labels"))
    files = a.html or [p for p in (a.dr / "view/index_shareable.html", a.dr / "view/shareable_package/index.html") if p.exists()]
    ref = Reference(a.dr)
    corpus_cache: dict = {}
    rc, reports = 0, {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        P = extract_payload(text)
        extra, dinfo = ([], {})
        if a.dynamic:
            extra, dinfo = dynamic_surfaces(f.resolve(), P)
            if not dinfo.get("chromium"):
                print("SKIP dynamic: no Chromium binary found; rendered surfaces were NOT scanned")
        dirs = (a.text_corpus or default_corpus_dirs()) if not a.no_text else []
        if dirs and corpus_cache.get("dirs") != dirs:
            corpus_cache.update(dirs=dirs, texts=read_corpus(dirs))
            corpus_cache["lit"] = Literature(corpus_cache["texts"])
        rep, _ = audit_html(text, a.dr, ref, extra, corpus_cache.get("lit") if dirs else None)
        rep.info["dynamic"] = dinfo
        if not a.no_text:
            if dirs:
                res = text_overlap(P, dirs, texts=corpus_cache["texts"])
                rep.info["text_provenance"] = dict(judge_text_overlap(res, rep), corpus_files=res["corpus_files"], corpus_words=res["corpus_words"])
            else:
                rep.info["text_provenance"] = "SKIPPED: no local third-party text corpus found"
        print(render_report(rep, str(f)))
        rc |= 0 if rep.ok else 1
        reports[str(f)] = {"ok": rep.ok, "violations": rep.violations, "rules": rep.rules, "info": rep.info}
    if a.json:
        a.json.write_text(json.dumps({"schema": SCHEMA, "reports": reports}, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    return rc


if __name__ == "__main__":
    sys.exit(main())
