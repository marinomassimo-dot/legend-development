#!/usr/bin/env python3
"""ADV-089 (IT, 2026-11-19): read-only scan of every quoted string and every number in the interpretive layer of the
consumed claims, against the held bytes of the claims' anchors.

Universe: the 26 claims with consumers > 0 in SCI's ranked scan (claims_ranked_scan_sci_20261119.tsv, key > 0).
Scanned text: Title, Summary, Clinical meaning, and every note-like field (Wave note, Nuance, Narrowing/Wording record,
Corollario, Nota, Additional efficacy, Vincolo, Meccanismo, Counter-directional); the Evidence-boundary fields are scanned
and labelled 'boundary' (reported apart from the headline).
Anchors: PMIDs in the claim's Source field plus SCI's A1/A2 anchor PMIDs; other PMIDs the record mentions are checked second (FOUND_ONLY_IN_MENTIONED_PMID) and, if unheld, make a miss MISS_SOME_UNHELD. Held bytes: the article_text, supplement_text,
table and PDF (pdftotext) artefacts of each anchor's deep-dive manifest that evidence_presence reports PRESENT.
Classes: FOUND_EXACT (whitespace-collapsed substring, nothing else normalised: the ADV-006 rule), FOUND_FORMAT
(Unicode/dash/quote/case normalisation), FOUND_ALNUM (letters and digits only), MISS_ALL_HELD (every anchor has held text),
MISS_SOME_UNHELD (at least one anchor has none: may sit there), NO_ANCHOR_TEXT (no anchor has held text).
Nothing is written to the registry; outputs are TSV and a summary next to this file.
Usage: python3 quote_number_scan_it_20261119.py --repo REPO --bytes-root ROOT_WITH_files/  |  --help
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import html
import json
import re
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT_KINDS = {"article_text", "supplement_text", "table", "article_binary"}
INLINE = r"i|italic|b|bold|sup|sub|em|strong|span|a|xref|ext-link|u|sc|named-content"
SKIP_FIELDS = re.compile(r"^(Status|Type|Pathway|Genotype/model relevance|Transferability|clinical relevance|Source|Wikilinks|"
                         r"Impact on Working Model|Full text status|Record provenance|REVIVAL_TRIGGER|.*PREMISE_TAG)")


def norm1(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def norm2(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).casefold()
    s = re.sub(r"[‐-―−­]", "-", s)
    s = re.sub(r"[‘’‚‛′]", "'", s)
    s = re.sub(r"[“”„«»]", '"', s)
    s = re.sub(r"(?<=\d),(?=\d{3}\b)", "", s)
    return norm1(s)


def norm3(s: str) -> str:
    return re.sub(r"[^0-9a-z]", "", norm2(s))


def _fmt(v: float) -> list[str]:
    out = {repr(v)}
    for k in range(1, 8):
        r = round(v, k)
        out.add(("%.*f" % (k, r)).rstrip("0").rstrip(".") if k else str(int(r)))
        out.add("%.*f" % (k, r))
    return sorted(out)


def read_office(path: Path) -> str | None:
    """xlsx: shared strings plus every numeric cell in its rounded renderings; docx: paragraph text. Stdlib only."""
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            if path.suffix.lower() == ".docx":
                x = z.read("word/document.xml").decode("utf-8", "replace")
                return html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"</w:p>", "\n", x)))
            parts = []
            if "xl/sharedStrings.xml" in names:
                parts.append(html.unescape(re.sub(r"<[^>]+>", " ", z.read("xl/sharedStrings.xml").decode("utf-8", "replace"))))
            for n in names:
                if n.startswith("xl/worksheets/") and n.endswith(".xml"):
                    x = z.read(n).decode("utf-8", "replace")
                    for m in re.finditer(r"<c\b([^>]*)>(?:<f>.*?</f>)?<v>([^<]*)</v>", x):
                        if 't="s"' in m.group(1) or 't="str"' in m.group(1):
                            continue
                        try:
                            parts.append(" ".join(_fmt(float(m.group(2)))))
                        except ValueError:
                            pass
            return "\n".join(parts)
    except Exception:
        return None


def read_text(path: Path) -> str | None:
    if path.suffix.lower() in (".xlsx", ".docx"):
        return read_office(path)
    try:
        if path.suffix.lower() == ".pdf":
            r = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, timeout=120)
            return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None
        raw = path.read_text(encoding="utf-8", errors="replace")
        if path.suffix.lower() in (".xml", ".html", ".htm", ".nxml"):
            raw = re.sub(rf"</?(?:{INLINE})(?:\s[^>]*)?>", "", raw, flags=re.I)
            raw = re.sub(r"<[^>]+>", " ", raw)
            raw = html.unescape(raw)
        return raw
    except Exception:
        return None


class Held:
    def __init__(self, repo: Path, broot: Path):
        self.broot = broot
        out = subprocess.run([sys.executable, str(repo / "framework/scripts/evidence_presence.py"), "--root", str(broot), "--json"],
                             capture_output=True, text=True).stdout
        self.by_pmid: dict[str, list[str]] = collections.defaultdict(list)
        for ln in out.splitlines():
            try:
                m = json.loads(ln)
            except ValueError:
                continue
            for a in m["artifacts"]:
                if a["state"] == "PRESENT" and a["kind"] in TEXT_KINDS and not a["path"].lower().endswith((".jpg", ".png", ".zip")):
                    self.by_pmid[str(m["pmid"])].append(a["path"])
        self.cache: dict[str, tuple[str, str, str] | None] = {}
        self.undeclared: dict[str, list[str]] = {}

    def disk(self, pmid: str) -> None:
        """Files on disk that name the PMID but that no manifest declares (a manifest can declare PDF and HTML absent while
        a PMC XML copy sits beside them). Text-like extensions only; figures excluded; nothing is read from outside files/."""
        have = set(self.by_pmid.get(pmid, []))
        found = []
        for pat in (f"files/fulltext/PMID{pmid}*", f"files/fulltext/PMID{pmid}*/**/*", f"files/supplement/PMID{pmid}*", f"files/supplement/PMID{pmid}*/**/*"):
            for f in self.broot.glob(pat):
                rel = str(f.relative_to(self.broot))
                if f.is_file() and f.suffix.lower() in (".xml", ".html", ".htm", ".txt", ".pdf", ".xlsx", ".docx", ".tsv", ".csv") and rel not in have:
                    found.append(rel)
        if found:
            self.by_pmid[pmid] = sorted(have | set(found))
            self.undeclared[pmid] = sorted(set(found))

    def text(self, pmid: str) -> tuple[str, str, str] | None:
        if pmid not in self.cache:
            self.disk(pmid)
            parts = [read_text(self.broot / p) for p in sorted(self.by_pmid.get(pmid, []))]
            parts = [p for p in parts if p]
            if not parts:
                self.cache[pmid] = None
            else:
                t = "\n".join(parts)
                self.cache[pmid] = (norm1(t), norm2(t), norm3(t))
        return self.cache[pmid]


def claims(repo: Path) -> dict[str, dict[str, str]]:
    t = (repo / "disease-models/wwox/registries/claim_registry_current.md").read_text(encoding="utf-8")
    parts = re.split(r"(?m)^## (CLAIM \d{3})\s*$", t)
    out = {}
    for i in range(1, len(parts), 2):
        fields: dict[str, str] = {}
        cur = None
        for ln in parts[i + 1].split("\n"):
            m = re.match(r"\*\*(.+?):\*\*\s*(.*)$", ln)
            if m:
                cur = m.group(1)
                fields[cur] = m.group(2)
            elif cur and ln.strip() and not ln.startswith(("---", "## ")):
                fields[cur] += "\n" + ln
        out[parts[i]] = fields
    return out


MASKS = [r"\[\[[^\]]*\]\]", r"`[^`]*(?:BATCH_|CC-|FTR-|CORPUS|PAPER|CLAIM|WM_v|PMID)[^`]*`", r"\b(?:PMID|PAPER|CLAIM|CORPUS-P|WM_v|BATCH_)\s?[\w.-]+",
         r"\bCC-[A-Z0-9-]+", r"\bFTR-[0-9-]+", r"\b\d{4}-\d{2}-\d{2}\b", r"\b10\.\d{4,}/\S+", r"\bPMC\d+", r"\bF\d{1,2}\b", r"\b\d{4}-\d{2}(?:-\d{2})?\b", r"\b(?:19|20)\d{2}\b", r"\b[0-9a-f]{16,}\b", r"\S+\.(?:pdf|xml|tsv|json|md|html)\b"]
Q_RE = [re.compile(r"(?<![\w'])'([^'\n]{3,240}?)'(?![\w'])"), re.compile(r'(?<![\w"])"([^"\n]{3,240}?)"(?![\w"])'),
        re.compile(r"«([^»\n]{3,240}?)»"), re.compile(r"‘([^’\n]{3,240}?)’"), re.compile(r"“([^”\n]{3,240}?)”")]
NUM_RE = re.compile(r"(?<![\w.])(?:\d+(?:[.,]\d+)?|\.\d+)(?![\w])")


def mask(s: str) -> str:
    for m in MASKS:
        s = re.sub(m, " ", s)
    return s


def items(text: str):
    m = mask(text)
    strings = []
    for rx in Q_RE:
        for x in rx.finditer(text):
            q = x.group(1).strip()
            if re.search(r"[A-Za-z]{2}", q) and not re.search(r"(?:BATCH_|CC-|FTR-)", q):
                strings.append(q)
    nums = [x.group(0) for x in NUM_RE.finditer(m)]
    return list(dict.fromkeys(strings)), nums


IT_WORDS = re.compile(r"\b(?:di|della|delle|degli|dei|il|la|le|lo|che|non|è|un|una|per|con|quindi|dove|sono|come|resta|restano|vale|togliendo|almeno|fra|sia)\b", re.I)


def is_italian(q: str) -> bool:
    return len(IT_WORDS.findall(q)) >= 1 and bool(re.search(r"[àèéìòù]|\b(?:di|della|delle|degli|dei|che|non|quindi|vale|resta|restano|togliendo|almeno|fra|elevata|piatta|assente|inibizione|quasi)\b", q, re.I)) \
        or q.lower() in ("elevata", "piatta", "assente", "inibizione", "guadagnare tempo")


def segments(q: str) -> list[str]:
    q = re.sub(r"[*`]", "", q)
    segs = [x.strip(" .,;:") for x in re.split(r"…|\.\.\.|\[\s*\.\.\.\s*\]|\[…\]", q)]
    return [x for x in segs if len(x) >= 6] or [q.strip()]


def variants(n: str) -> list[str]:
    v = [n, n.replace(",", ".")]
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", n):
        v.append(n.replace(".", ""))
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+", n):
        v.append(n.replace(",", ""))
    return list(dict.fromkeys(v))


def informative(n: str) -> bool:
    return "." in n or "," in n or len(n) >= 2


def find(kind: str, item: str, texts: list[tuple[str, str, str]]) -> str:
    if kind == "string":
        segs = segments(item)
        for lvl, norm in ((0, norm1), (1, norm2), (2, norm3)):
            if any(all(norm(sg) in t[lvl] for sg in segs) for t in texts):
                return ("FOUND_EXACT", "FOUND_FORMAT", "FOUND_ALNUM")[lvl]
        return ""
    for lvl in (0, 1):
        for v in variants(item):
            n = v if lvl == 0 else norm2(v)
            rx = re.compile(r"(?<![\d.,])" + re.escape(n) + r"(?![\d]|[.,]\d)")
            if any(rx.search(t[lvl]) for t in texts):
                return "FOUND_EXACT" if (lvl == 0 and v == item) else "FOUND_FORMAT"
    return ""


def selftest() -> int:
    t = norm1("The mean was 0.390 g (p = 0.0003) and the authors wrote: it could block NMDA receptors, 12 per cent.")
    texts = [(t, norm2(t), norm3(t))]
    ok = (find("number", "0.390", texts) == "FOUND_EXACT" and find("number", "0,390", texts) == "FOUND_FORMAT"
          and find("number", "0.391", texts) == "" and find("string", "it could block NMDA receptors", texts) == "FOUND_EXACT"
          and find("string", "it could block **NMDA** receptors \u2026 12 per cent", texts) == "FOUND_EXACT"
          and find("string", "it could block AMPA receptors", texts) == "")
    print("selftest", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", type=Path)
    ap.add_argument("--bytes-root", type=Path)
    ap.add_argument("--selftest", action="store_true", help="check the matcher on synthetic text and exit")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.repo and a.bytes_root):
        ap.error("--repo and --bytes-root are required")
    repo, broot = a.repo.resolve(), a.bytes_root.resolve()
    sci = repo / "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/anchor_integrity_scan_sci_20261119"
    ranked = list(csv.DictReader((sci / "claims_ranked_scan_sci_20261119.tsv").open(encoding="utf-8"), delimiter="\t"))
    consumed = [r["claim"] for r in ranked if int(r["key"] or 0) > 0]
    anchors = collections.defaultdict(set)
    for r in csv.DictReader((sci / "anchors_by_claim_scan_sci_20261119.tsv").open(encoding="utf-8"), delimiter="\t"):
        if r["cls"] in ("A1", "A2") and r["pmid"]:
            anchors[r["claim"]].add(r["pmid"])
    reg = claims(repo)
    held = Held(repo, broot)
    rows, per_claim = [], []
    for c in consumed:
        f = reg[c]
        pm = set(anchors[c]) | set(re.findall(r"(?<![\d_-])(\d{7,8})(?![\d_-])", f.get("Source", "")))
        mentioned = set(re.findall(r"\bPMID[ :]*(\d{7,8})\b", "\n".join(f.values()))) | set(re.findall(r"\bPMID(\d{7,8})\b", "\n".join(f.values())))
        mentioned -= pm
        have = {p: held.text(p) for p in sorted(pm)}
        texts = [v for v in have.values() if v]
        unheld = [p for p, v in have.items() if not v]
        have_m = {p: held.text(p) for p in sorted(mentioned)}
        texts_m = [v for v in have_m.values() if v]
        unheld_m = [p for p, v in have_m.items() if not v]
        status = "ALL_HELD" if pm and not unheld else ("NONE_HELD" if not texts else "SOME_HELD")
        per_claim.append((c, ",".join(sorted(pm)), ",".join(p for p in sorted(pm) if have[p]), ",".join(unheld), status, ",".join(sorted(mentioned)), ",".join(unheld_m)))
        for name, body in f.items():
            if SKIP_FIELDS.match(name):
                continue
            scope = "boundary" if "Evidence boundary" in name or "Limiti" in name else "headline"
            strs, nums = items(body)
            for kind, lst in (("string", strs), ("number", nums)):
                for it in lst:
                    cls = find(kind, it, texts) if texts else ""
                    if not cls and kind == "string" and is_italian(it):
                        cls = "NON_ENGLISH_GLOSS"
                    if not cls and texts_m and find(kind, it, texts_m):
                        cls = "FOUND_ONLY_IN_MENTIONED_PMID"
                    if not cls:
                        cls = "NO_ANCHOR_TEXT" if not texts else ("MISS_SOME_UNHELD" if (unheld or unheld_m) else "MISS_ALL_HELD")
                    inf = "yes" if (kind == "string" or informative(it)) else "no"
                    ctx = body.replace("\n", " ")
                    k = ctx.find(it)
                    sent = ctx[max(0, k - 80): k + len(it) + 80] if k >= 0 else ""
                    rows.append((c, name[:40], scope, kind, inf, it, cls, status, sent))
    with (HERE / "scan_items_it_20261119.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["claim", "field", "scope", "kind", "informative", "item", "class", "anchor_status", "context"])
        w.writerows(rows)
    with (HERE / "scan_claims_it_20261119.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["claim", "anchor_pmids", "held_pmids", "unheld_pmids", "status", "mentioned_pmids", "mentioned_unheld"])
        w.writerows(per_claim)
    # calibration: how often does a number that is NOT in the claim hit an anchor's text by chance? (fixed seed)
    import random
    rnd = random.Random(20261119)
    probes = ["%d.%02d" % (rnd.randint(0, 99), rnd.randint(1, 99)) for _ in range(25)]
    hits = tot = 0
    for c in consumed:
        pm = set(anchors[c]) | set(re.findall(r"(?<![\d_-])(\d{7,8})(?![\d_-])", reg[c].get("Source", "")))
        tx = [held.text(p) for p in sorted(pm)]
        tx = [t for t in tx if t]
        if not tx:
            continue
        for pr in probes:
            tot += 1
            hits += bool(find("number", pr, tx))
    calib = {"probes_per_claim": len(probes), "tests": tot, "hit_rate_two_decimal_random_numbers": round(hits / tot, 3) if tot else None}
    cnt = collections.Counter((r[2], r[3], r[4], r[6]) for r in rows)
    summ = {"chance_hit_calibration": calib, "undeclared_files_used_by_pmid": {k: len(v) for k, v in sorted(held.undeclared.items())}, "claims": len(consumed), "items": len(rows), "by_scope_kind_informative_class": {"|".join(k): v for k, v in sorted(cnt.items())},
            "claims_by_anchor_status": dict(collections.Counter(p[4] for p in per_claim))}
    (HERE / "scan_summary_it_20261119.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summ, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
