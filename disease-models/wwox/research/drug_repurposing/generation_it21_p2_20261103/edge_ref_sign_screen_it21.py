#!/usr/bin/env python3
"""Edge-reference sign screen (IT21 F1). For every edge of a handed-over chain: the PMIDs the network record itself cites -> the abstract of each
-> sentence-level evidence of the direction of effect -> one label per edge:
  SUPPORTS | OPPOSES | SPLIT | NO_ABSTRACT_EVIDENCE   (plus the quoted sentences; nothing is inferred silently)
DEPTH: abstract (title+abstract as served by PubMed), a keyword/sentence heuristic. It is NOT a read of the paper, it cannot see a sign that sits only in the
full text, and it is blind to context (cell type, species, protein v transcript). A label is a prompt for a human reading, never a verdict.

  edge_ref_sign_screen_it21.py fetch    --cache DIR   network: OmniPath edge records + PubMed efetch (NCBI E-utilities), polite rate, cached in DIR (outside git)
  edge_ref_sign_screen_it21.py screen   --cache DIR --out DIR   offline: the tables for the 7 proposals P4a did not qualify
  edge_ref_sign_screen_it21.py validate --cache DIR --out DIR   offline: the screen v the manual P4a verdicts
Standard library only. The cache holds third-party abstracts and stays out of git; the result tables carry PMIDs, a SHA-256 prefix of the abstract and the
quoted sentence."""
import argparse, csv, gzip, hashlib, json, re, time, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
P4A = HERE.parent / "qualification_it21_p4a_20261103"
HANDOFF = HERE / "results" / "handoff_it21.tsv"
NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
OMNI = "https://omnipathdb.org"
UA = "legend-public-research/1.0 (no contact string)"
OMNI_DATASETS = "omnipath,pathwayextra,kinaseextra,ligrecextra,tfregulons,collectri,dorothea,transcriptional"
P4A_IDS = ("0006", "0008", "0057", "0195", "0374", "0512")
REMAINING = ("0014", "0221", "0236", "0296", "0388", "0456", "0542")

ALIASES = {
    "HDAC5": ["HDAC5", "HDAC 5"], "SLC2A1": ["SLC2A1", "GLUT1", "GLUT-1", "glucose transporter 1"],
    "KDM4C": ["KDM4C", "JMJD2C", "GASC1"], "HIF1A": ["HIF1A", "HIF-1alpha", "HIF1alpha", "HIF-1", "HIF1", "hypoxia-inducible factor 1", "hypoxia inducible factor 1", "hypoxia-inducible factor-1"],
    "HK2": ["HK2", "hexokinase 2", "hexokinase II", "hexokinase-2"], "BTK": ["BTK", "Bruton"], "STAT3": ["STAT3"], "NPY": ["NPY", "neuropeptide Y"],
    "EZH2": ["EZH2"], "IL6": ["IL6", "IL-6", "interleukin-6", "interleukin 6"], "TNF": ["TNF", "TNF-alpha", "TNFalpha", "tumor necrosis factor", "tumour necrosis factor"],
    "MAPK1": ["MAPK1", "ERK2", "ERK1/2", "ERK"], "BCL3": ["BCL3", "Bcl-3"], "SIRT1": ["SIRT1"], "MYC": ["MYC", "c-Myc", "cMyc"],
    "XIAP": ["XIAP"], "ROCK2": ["ROCK2", "ROCK-2", "ROCK"], "EP300": ["EP300", "p300"], "PIM2": ["PIM2", "Pim-2"], "NFATC1": ["NFATC1", "NFATc1", "NFAT2", "NFAT"],
    "MAPK3": ["MAPK3", "ERK1", "ERK1/2", "ERK"], "BRD4": ["BRD4"], "MAP3K7": ["MAP3K7", "TAK1"], "NFKBIB": ["NFKBIB", "IkappaBbeta", "IkBbeta", "IkappaB-beta", "IkB-beta"],
    "IL1B": ["IL1B", "IL-1beta", "IL1beta", "interleukin-1beta", "interleukin 1beta"], "JAK2": ["JAK2"], "PGR": ["PGR", "progesterone receptor"],
}
GREEK = {"α": "alpha", "β": "beta", "κ": "kappa", "γ": "gamma"}
UP = r"increas|upregulat|up-regulat|induc|activat|promot|enhanc|stimulat|elevat|rais(?:e|es|ed|ing)\b|stabili[sz]|transactivat|higher|augment|potentiat"
DOWN = r"interfer|inhibit(?!or)|prevent|block|decreas|downregulat|down-regulat|repress|suppress|reduc|attenuat|lower|abolish|diminish|impair|degrad|destabili[sz]|declin|blunt|dampen|negatively regulat"
UPRE = re.compile(UP, re.I)
DOWNRE = re.compile(DOWN, re.I)
LOSS = r"knock-?down|knock-?out|silenc|deplet|deletion|delet(?:ed|ing)|ablat|loss of|lack(?:ing|s|ed)?\b|deficien|antisense|blocker|degrader|degradation of|siRNA|shRNA|inhibitor|inhibition|inhibiting|inhibited|blockade|blocking|dominant[- ]negative|null"
NEG = r"\b(?:not|no|without|failed to|neither|nor|unaffected|independent of)\b"
SIGN_PATH = re.compile(r"(\w+)\s+-([PT])\(([+-])\)->\s+(\w+)")


def norm(t):
    for g, w in GREEK.items():
        t = t.replace(g, w)
    return t


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(\[])", norm(text)) if s.strip()]


def alias_pos(sent, gene):
    """span of the earliest mention of any alias of `gene`; case-sensitive for short or all-capital symbols, case-insensitive otherwise."""
    best = None
    for a in ALIASES.get(gene, [gene]):
        flags = 0 if (len(a) <= 4 or a.isupper()) else re.I
        m = re.search(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(?![A-Za-z0-9])", sent, flags)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), m.end())
    return best


def sentence_sign(sent, reg, tgt):
    """+1 / -1 = effect of `reg` on `tgt` stated in the sentence; 0 = none or ambiguous. Returns (sign, rule).
    Cues are read in the last clause between the regulator and the target (before the regulator in a passive 'TGT ... by REG'); several cues multiply
    ('prevents activation' = -1 x +1). A loss-type word within 35 characters of the regulator (knockdown, inhibitor, deletion ...) flips the sign;
    an 'inhibit*'/'prevent*'/'block*' word elsewhere is an ordinary lowering cue."""
    pr, pt = alias_pos(sent, reg), alias_pos(sent, tgt)
    if not pr or not pt:
        return 0, "alias missing"
    passive = pt[0] < pr[0] and re.search(r"\bby\b[^.]{0,60}$", sent[:pr[0]]) is not None
    if pr[0] > pt[0] and not passive:
        return 0, "target mentioned before regulator"
    if re.search(NEG, sent, re.I):
        return 0, "negation"
    span = sent[pt[1]:pr[0]] if passive else sent[pr[1]:pt[0]]
    span = re.split(r"\b(?:but|whereas|while|however)\b|;", span)[-1]
    cues = [(m.start(), 1 if m.re is UPRE else -1) for rx in (UPRE, DOWNRE) for m in rx.finditer(span)]
    if not cues or len(cues) > 3:
        return 0, "no cue" if not cues else "too many cues"
    s = 1
    for _, c in cues:
        s *= c
    win = sent[max(pr[0] - 35, 0):pr[1] + 35]
    loss = re.search(LOSS, win, re.I)
    if loss:
        s = -s
    return s, ("loss-type perturbation flips the cue" if loss else "direct cue")


def screen_ref(text, reg, tgt):
    return [(sg, s, why) for s in sentences(text) for sg, why in [sentence_sign(s, reg, tgt)] if sg]


def label(edge_sign, per_ref):
    """per_ref: {pmid: [(sign, sentence, rule)]}; edge_sign = sign claimed by the network. Returns (label, supporting, opposing)."""
    sup, opp = [], []
    for pm, hits in per_ref.items():
        for sg, s, why in hits:
            (sup if sg == edge_sign else opp).append((pm, s, why))
    if sup and opp:
        return "SPLIT", sup, opp
    if sup:
        return "SUPPORTS", sup, opp
    if opp:
        return "OPPOSES", sup, opp
    return "NO_ABSTRACT_EVIDENCE", sup, opp


# ----------------------------------------------------------------------------- data
def parse_edges(path_str):
    out = []
    for part in path_str.split("; "):
        m = SIGN_PATH.match(re.sub(r"\s*\[[^\]]*\]", "", part).strip())
        if m:
            out.append((m.group(1), m.group(4), m.group(2), 1 if m.group(3) == "+" else -1))
    return out


def handoff_edges(only=None):
    res = []
    for r in csv.DictReader(open(HANDOFF, newline=""), delimiter="\t"):
        if only and r["proposal_id"][-4:] not in only:
            continue
        res += [(r["proposal_id"], a, b, kind, sg) for a, b, kind, sg in parse_edges(r["mechanism_path"])]
    return res


def refs_of(rec_rows):
    pm = set()
    for r in rec_rows:
        for tok in str(r.get("references", "")).split(";"):
            m = re.fullmatch(r"[A-Za-z0-9_.]+:(\d{5,9})", tok.strip())
            if m:
                pm.add(m.group(1))
    return sorted(pm, key=int)


def parse_efetch(xml_bytes):
    out = {}
    for art in ET.fromstring(xml_bytes).iter("PubmedArticle"):
        t = art.find(".//ArticleTitle")
        out[art.findtext(".//MedlineCitation/PMID")] = {
            "title": "".join(t.itertext()) if t is not None else "",
            "abstract": " ".join("".join(x.itertext()).strip() for x in art.findall(".//Abstract/AbstractText")),
            "types": [x.text for x in art.findall(".//PublicationType") if x.text],
            "year": art.findtext(".//JournalIssue/PubDate/Year") or (art.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]}
    return out


def http(url, params, waits=(0, 2, 6, 15)):
    full = url + "?" + urllib.parse.urlencode(sorted(params.items()))
    st = 0
    for w in waits:
        time.sleep(w)
        try:
            with urllib.request.urlopen(urllib.request.Request(full, headers={"User-Agent": UA}), timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            st = e.code
        except Exception:
            st = 0
    return st, b""


def cmd_fetch(a):
    cache = Path(a.cache)
    cache.mkdir(parents=True, exist_ok=True)
    known = {}
    for r in csv.DictReader(open(P4A / "edge_records_omnipath.tsv", newline=""), delimiter="\t"):
        known.setdefault(r["edge"], []).append(r)
    recs, log = {}, []
    for s, t in sorted({(x[1], x[2]) for x in handoff_edges()}):
        k = f"{s}>{t}"
        if k in known:
            recs[k] = known[k]
            continue
        st, body = http(OMNI + "/interactions", {"sources": s, "targets": t, "genesymbols": 1, "fields": "sources,references,curation_effort,type", "format": "json", "datasets": OMNI_DATASETS})
        rows = []
        if st == 200:
            for d in json.loads(body):   # the service ignores part of its filters: filter locally by symbol
                if d.get("source_genesymbol") == s and d.get("target_genesymbol") == t:
                    rows.append({"edge": k, "references": d.get("references") or ""})
        recs[k] = rows
        log.append([k, st, len(rows)])
        print("omnipath", k, st, len(rows), flush=True)
        time.sleep(0.5)
    pmids = sorted({p for rows in recs.values() for p in refs_of(rows)}, key=int)
    have = json.load(gzip.open(cache / "abstracts.json.gz", "rt")) if (cache / "abstracts.json.gz").exists() else {}
    need = [p for p in pmids if p not in have]
    for i in range(0, len(need), 100):
        st, body = http(NCBI + "efetch.fcgi", {"db": "pubmed", "id": ",".join(need[i:i + 100]), "retmode": "xml"})
        log.append([f"efetch[{i}]", st, 0])
        print("efetch", i, st, flush=True)
        if st == 200:
            have.update(parse_efetch(body))
        time.sleep(0.5)
    json.dump(recs, gzip.open(cache / "edge_records.json.gz", "wt"))
    json.dump(have, gzip.open(cache / "abstracts.json.gz", "wt"))
    json.dump(log, open(cache / "fetch_log.json", "w"))
    print("edges", len(recs), "pmids cited", len(pmids), "abstracts held", len(have))


# ----------------------------------------------------------------------------- screen
def edge_name(a, kind, sg, b):
    return f"{a} -{kind}({'+' if sg > 0 else '-'})-> {b}"


def run_screen(recs, abstracts, edges):
    rows, quotes = [], []
    for pid, a, b, kind, sg in edges:
        pms = refs_of(recs.get(f"{a}>{b}", []))
        per, with_abs, reviews = {}, 0, 0
        for p in pms:
            ab = abstracts.get(p)
            if not ab or not ab.get("abstract"):
                continue
            with_abs += 1
            reviews += any("Review" in t for t in ab.get("types", []))
            h = screen_ref(ab["title"] + ". " + ab["abstract"], a, b)
            if h:
                per[p] = h
        lab, sup, opp = label(sg, per)
        nm = edge_name(a, kind, sg, b)
        rows.append({"proposal_id": pid, "edge": nm, "network_sign": "+" if sg > 0 else "-", "refs_cited": len(pms), "refs_with_abstract": with_abs,
                     "refs_review_type": reviews, "refs_with_sign_sentence": len(per), "n_support": len(sup), "n_oppose": len(opp), "label": lab,
                     "basis_flag": "NO_CITED_REF_OR_ALL_ARE_REVIEWS" if (not pms or (with_abs and reviews == with_abs)) else "",
                     "depth": "abstract keyword/sentence heuristic; not a read"})
        for tag, lst in (("SUPPORT", sup), ("OPPOSE", opp)):
            for p, s, why in lst[:6]:
                quotes.append({"proposal_id": pid, "edge": nm, "pmid": p, "side": tag, "rule": why,
                               "abstract_sha256": hashlib.sha256((abstracts[p]["title"] + abstracts[p]["abstract"]).encode()).hexdigest()[:16], "sentence": s})
    return rows, quotes


def write(path, head, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        for r in rows:
            w.writerow([str(r[h]).replace("\t", " ").replace("\n", " ") for h in head])


def load_cache(c):
    c = Path(c)
    return json.load(gzip.open(c / "edge_records.json.gz", "rt")), json.load(gzip.open(c / "abstracts.json.gz", "rt"))


def chain_label(labels):
    if "OPPOSES" in labels:
        return "OPPOSED"
    if "SPLIT" in labels:
        return "SPLIT"
    return "CLEAR" if labels and all(l == "SUPPORTS" for l in labels) else "UNSCREENED_PARTLY"


# Hand check of the sentences the screen quoted on the OPPOSE side of a SPLIT/OPPOSES edge (done once, by the F1 actor, on the quoted abstract sentences only; abstract depth).
# DISMISSED = every quoted opposing sentence, read by hand, supports the edge (a parse error of the heuristic); CONFIRMED = at least one genuinely states the opposite sign.
HAND_CHECK = {
    ("IT21P2-0014", "HIF1A>HK2"): ("DISMISSED", "6 quoted opposing sentences: inhibiting or suppressing HIF-1 lowers HK2 (supports the edge); heuristic misreads miR/inhibitor wording"),
    ("IT21P2-0221", "EP300>TNF"): ("DISMISSED", "2 quoted: p300 knockdown or blocked p300 recruitment lowers TNF (supports the edge)"),
    ("IT21P2-0236", "NFATC1>IL6"): ("DISMISSED", "1 quoted: IL-6 decreased when NFATc1 was suppressed (supports the edge)"),
    ("IT21P2-0388", "NFKBIB>IL1B"): ("CONFIRMED", "IkappaBbeta overexpression/replacement attenuated IL1B, IL6 expression (PMIDs 21646597, 25908863): IkappaBbeta acts as an NF-kB inhibitor in those systems, opposite to the network's +"),
}


def dispositions(rows, hand):
    disp = []
    for pid in sorted({r["proposal_id"] for r in rows}):
        labs = [r["label"] for r in rows if r["proposal_id"] == pid]
        cl, h = chain_label(labs), hand[pid]
        alt = h["alternatives_same_mechanism"].strip()
        contested = [r for r in rows if r["proposal_id"] == pid and r["label"] in ("OPPOSES", "SPLIT")]
        checks = [HAND_CHECK.get((pid, _key(r["edge"]))) for r in contested]
        standing = [c for c in checks if c is None or c[0] == "CONFIRMED"]
        hand_txt = "; ".join(c[0] + ": " + c[1] for c in checks if c) or ""
        if cl == "OPPOSED" and standing and not alt:
            after, note = "CLOSED_AS_WRITTEN", "edge sign contested by its own references (chain opposed, no alternative arm remains)"
        elif standing:
            after, note = h["status"], "edge sign contested by its own references"
        else:
            after, note = h["status"], ("screen SPLIT dismissed on hand check; no contest standing" if contested else "")
        disp.append({"proposal_id": pid, "compound": h["compound"], "edge_labels": " / ".join(labs), "chain_screen": cl, "hand_check_of_opposing_sentences": hand_txt,
                     "status_before": h["status"], "status_after": after, "alternative_arm_left": "yes" if alt else "no", "disposition_note": note,
                     "depth": "abstract-level screen and abstract sentences; no full text read"})
    return disp


def _key(edge_name_str):
    m = SIGN_PATH.match(edge_name_str)
    return f"{m.group(1)}>{m.group(4)}"


EDGE_HEAD = ["proposal_id", "edge", "network_sign", "refs_cited", "refs_with_abstract", "refs_review_type", "refs_with_sign_sentence", "n_support", "n_oppose", "label", "basis_flag", "depth"]
QUOTE_HEAD = ["proposal_id", "edge", "pmid", "side", "rule", "abstract_sha256", "sentence"]
DISP_HEAD = ["proposal_id", "compound", "edge_labels", "chain_screen", "hand_check_of_opposing_sentences", "status_before", "status_after", "alternative_arm_left", "disposition_note", "depth"]


def cmd_screen(a):
    recs, ab = load_cache(a.cache)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows, quotes = run_screen(recs, ab, handoff_edges(REMAINING))
    write(out / "edge_screen_remaining7.tsv", EDGE_HEAD, rows)
    write(out / "edge_screen_quotes_remaining7.tsv", QUOTE_HEAD, quotes)
    hand = {r["proposal_id"]: r for r in csv.DictReader(open(HANDOFF, newline=""), delimiter="\t")}
    disp = dispositions(rows, hand)
    write(out / "dispositions_remaining7.tsv", DISP_HEAD, disp)
    for r in rows:
        print(r["proposal_id"], r["edge"], r["label"], f"cited={r['refs_cited']} abs={r['refs_with_abstract']} rev={r['refs_review_type']} +{r['n_support']} -{r['n_oppose']}", r["basis_flag"])
    for r in disp:
        print(r["proposal_id"], r["compound"], r["chain_screen"], "|", r["status_after"], "|", r["disposition_note"])


# manual P4a verdicts on the sign of the network record v its references (edge_provenance_it21_p4a.tsv; abstracts read by the P4a actor; some by title only)
GOLD = {
    "HDAC5>SLC2A1": ("SUPPORTS", "reference: knockdown lowers GLUT1"), "BTK>STAT3": ("SUPPORTS", "BTK down-regulates STAT3 activity"),
    "STAT3>NPY": ("SUPPORTS", "by title"), "MAPK1>BCL3": ("SUPPORTS", "phosphorylation increases Bcl3 activity"), "BCL3>TNF": ("SUPPORTS", "by title"),
    "EZH2>IL6": ("CONTESTED", "29132376: EZH2 inhibition raises IL6"), "EZH2>TNF": ("CONTESTED", "29132376: EZH2 inhibition raises TNF"),
    "SIRT1>MYC": ("CONTESTED", "split 2 v 2 inside the edge's list"), "KDM4C>HIF1A": ("CONTESTED", "sole reference is a review; not a measurement"),
}


def cmd_validate(a):
    recs, ab = load_cache(a.cache)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows, quotes = run_screen(recs, ab, handoff_edges(P4A_IDS))
    seen, res = set(), []
    for r, e in zip(rows, handoff_edges(P4A_IDS)):
        k = f"{e[1]}>{e[2]}"
        if k in seen:
            continue
        seen.add(k)
        g = GOLD.get(k)
        if not g:
            res.append({"edge": k, "screen_label": r["label"], "manual_verdict": "", "manual_note": "no manual verdict of the sign", "outcome": "NOT_SCORED", "basis_flag": r["basis_flag"]})
            continue
        flagged, want = r["label"] in ("OPPOSES", "SPLIT"), g[0] == "CONTESTED"
        res.append({"edge": k, "screen_label": r["label"], "manual_verdict": g[0], "manual_note": g[1], "basis_flag": r["basis_flag"],
                    "outcome": "TP" if flagged and want else "TN" if not flagged and not want else "FP" if flagged else "FN"})
    write(out / "validation_p4a_edges.tsv", ["edge", "screen_label", "manual_verdict", "manual_note", "outcome", "basis_flag"], res)
    write(out / "edge_screen_p4a6.tsv", EDGE_HEAD, rows)
    write(out / "edge_screen_quotes_p4a6.tsv", QUOTE_HEAD, quotes)
    for r in res:
        print(r["edge"], r["screen_label"], r["manual_verdict"], r["outcome"], r["basis_flag"])


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sp = ap.add_subparsers(dest="cmd", required=True)
    for n, f in (("fetch", cmd_fetch), ("screen", cmd_screen), ("validate", cmd_validate)):
        p = sp.add_parser(n)
        p.add_argument("--cache", required=True)
        if n != "fetch":
            p.add_argument("--out", required=True)
        p.set_defaults(f=f)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
