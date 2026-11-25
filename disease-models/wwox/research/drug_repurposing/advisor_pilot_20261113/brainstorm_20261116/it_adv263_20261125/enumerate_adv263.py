"""ADV-263 enumeration, as frozen in PREREG_ADV263_IT_20261125.md. Read-only on the surfaces.

Run from the repository root: python3 <this file> --out <directory>
Writes sentences.tsv (every sentence with a list word), sample.tsv and counts.json into --out.
"""
import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
W = "disease-models/wwox"
DR = W + "/research/drug_repurposing"
WORDS = ["only", "single", "first", "never", "none", "unique", "sole", "novel", "untested",
         "no report", "no reports", "no study", "no studies",
         "unico", "unica", "unici", "uniche", "solo", "soltanto", "mai", "nessun", "nessuno",
         "nessuna", "primo", "primi"]
PRE = ["only if", "only when", "only after", "only once", "not only", "if and only", "first-line",
       "first-pass", "first author", "at first", "first step", "single-cell", "single cell",
       "single-nucleus", "single nucleus", "single-guide", "single guide", "single-dose",
       "single dose", "single-strand", "single nucleotide", "single-nucleotide", "solo se",
       "solo quando", "non solo"]
WORD_RE = re.compile(r"(?<![\w])(?:" + "|".join(sorted(map(re.escape, WORDS), key=len, reverse=True))
                     + r")(?![\w])", re.I)
PRE_RE = re.compile("|".join(re.escape(p) for p in PRE), re.I)
ABBR = ["e.g.", "i.e.", "vs.", "Fig.", "fig.", "cf.", "approx.", "ca.", "et al.", "es.", "ecc.", "p."]

SURFACES = {
    "CARD": sorted(str(p) for d in ("cards", "cards_early") for p in Path(DR, d).glob("*.card.json")),
    "INV": [DR + "/ranking_it8_p9_20261029/investigations_it20.tsv"],
    "MAP": [W + "/analysis/mechanism_intervention_map.md"],
    "HYP": [W + "/research/therapeutic_hypotheses_ledger_current.md"],
    "PORT": [DR + "/research_portfolio.tsv"],
    "CLAIM": [W + "/registries/claim_registry_current.md"],
}
FLOOR, TOTAL, CEILING_ALL = 8, 100, 150


def sentences(block):
    s = re.sub(r"\s+", " ", block).strip()
    for a in ABBR:
        s = s.replace(a, a.replace(".", "\x00"))
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'(\[*`A-ZÀ-Ý0-9🔴⚠])|\s*;\s+(?=[A-ZÀ-Ý])", s)
    return [p.replace("\x00", ".").strip() for p in parts if p.strip()]


def heading_id(title):
    m = re.match(r"[*_ ]*((?:HYP-\d{8}-\d+)|(?:CLAIM \d+[a-z]?)|(?:[RN]-\d+)|(?:CHAIN [A-H]))", title)
    return m.group(1) if m else None


def md_blocks(path):
    """(record, block text): wrapped lines are joined; table cells and list items stay separate."""
    stack, buf, out = [], [], []

    def record():
        for _, rid, title in reversed(stack):
            if rid:
                return rid
        return stack[-1][2][:60] if stack else "(preamble)"

    def flush():
        if buf:
            out.append((record(), " ".join(buf)))
            buf.clear()

    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = re.sub(r"^\s*(?:>\s?)+", "", raw).strip()
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            flush()
            level, title = len(h.group(1)), h.group(2)
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, heading_id(title), title))
            out.append((record(), title))
        elif not line:
            flush()
        elif line.startswith("|"):
            flush()
            rid = record()
            first = line.strip("|").split("|")[0].strip(" *`")
            out.extend((heading_id(first) or rid, c.strip()) for c in line.strip("|").split("|"))
        elif re.match(r"^(?:[-*+]|\d+\.)\s|^\*\*[^*]+:\*\*", line):
            flush()
            buf.append(line)
        else:
            buf.append(line)
    flush()
    return out


def json_strings(x):
    if isinstance(x, dict):
        for v in x.values():
            yield from json_strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from json_strings(v)
    elif isinstance(x, str):
        yield x


def blocks(surface, path):
    if surface == "CARD":
        rid = Path(path).name[: -len(".card.json")]
        return [(rid, s) for s in json_strings(json.loads(Path(path).read_text(encoding="utf-8")))]
    if surface in ("INV", "PORT"):
        with open(path, encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE))
        if surface == "INV":
            return [(r["inv_id"], v) for r in rows for k, v in r.items() if v and k != "inv_id"]
        return [(r["id"], r["next_action"] or "") for r in rows]
    return md_blocks(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    rows, counts = [], {}
    for surface, paths in SURFACES.items():
        seen, kept = set(), []
        for path in paths:
            for rid, block in blocks(surface, path):
                for s in sentences(block):
                    if not WORD_RE.search(s) or (rid, s) in seen:
                        continue
                    seen.add((rid, s))
                    pre = not WORD_RE.search(PRE_RE.sub(" ", s))
                    words = ",".join(sorted({m.lower() for m in WORD_RE.findall(s)}))
                    kept.append({"surface": surface, "record": rid, "path": path, "words": words,
                                 "prefiltered": int(pre), "sentence": s})
        args = ["git", "grep", "-n", "-w", "-i"] + [x for w in WORDS for x in ("-e", w)] + ["--"] + paths
        lines = subprocess.run(args, capture_output=True, text=True, check=False).stdout.splitlines()
        counts[surface] = {"git_grep_lines": len(lines), "sentences": len(kept),
                           "prefiltered": sum(r["prefiltered"] for r in kept),
                           "records": len({r["record"] for r in kept}), "files": len(paths)}
        rows.extend(kept)
    live = [r for r in rows if not r["prefiltered"]]
    for r in rows:
        r["key"] = hashlib.sha256(f"ADV263|{r['surface']}|{r['record']}|{r['sentence']}".encode()).hexdigest()
    by = {s: sorted((r for r in live if r["surface"] == s), key=lambda r: r["key"]) for s in SURFACES}
    if len(live) < CEILING_ALL:
        quota = {s: len(v) for s, v in by.items()}
    else:
        quota = {s: min(FLOOR, len(v)) for s, v in by.items()}
        while sum(quota.values()) < TOTAL:
            s = max((s for s in by if quota[s] < len(by[s])), key=lambda s: len(by[s]) / (quota[s] + 1))
            quota[s] += 1
    sample = [r for s in SURFACES for r in by[s][: quota[s]]]
    for s in SURFACES:
        counts[s]["sampled"] = quota[s]
    fields = ["surface", "record", "words", "prefiltered", "key", "path", "sentence"]
    for name, data in (("sentences.tsv", rows), ("sample.tsv", sample)):
        with open(out / name, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(fields)
            for r in data:
                w.writerow([str(r[f]).replace("\t", " ") for f in fields])
    (out / "counts.json").write_text(json.dumps(counts, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(counts, indent=1))
    print("live sentences", len(live), "sampled", len(sample))
    return 0


if __name__ == "__main__":
    sys.exit(main())
