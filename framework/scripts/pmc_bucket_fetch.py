#!/usr/bin/env python3
"""Re-acquire the open-access bytes of one paper from NCBI and the PMC open-data bucket, with digests.

WHY THIS EXISTS (2026-10-20, gold wave, scientist-b)
----------------------------------------------------
Eleven of the fourteen manifests re-read in the wave 2026-10-19 declared artefacts that were absent
from the shared checkout (files/ is gitignored). Re-acquisition was done by hand each time, and
three lessons repeated: the PMC web pages serve a reCAPTCHA to any User-Agent, the efetch XML is
a short stub when the publisher forbids XML ("does not allow downloading of the full text in XML
form"), and the open-data bucket (listing by prefix) holds the figure JPEGs, the supplements (PDF,
DOCX, XLSX) and a PDF that efetch does not. This tool does the same sequence once and reports,
per file, the route, the HTTP status, the size and the SHA-256, so the manifest's
`acquisition_recipe` can be filled from its output.

  python3 framework/scripts/pmc_bucket_fetch.py --pmid <PMID> --tag Author2024 [--root <checkout>]

Writes only under <root>/files/ (fulltext/PMID<pmid>_<tag>_PMC_r2.xml, figures/PMID<pmid>_r2/,
supplement/PMID<pmid>_r2/); never overwrites an existing file; prints one JSON record. A stub or
restricted XML is reported as `xml_state: restricted_stub` and exit code 2 so it is never taken
for a full text. Network: NCBI eutils and the public bucket, no User-Agent, no key. Spend: none.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
BUCKET = "https://pmc-oa-opendata.s3.amazonaws.com/"
SUPP_EXT = {"pdf", "docx", "doc", "xlsx", "xls", "zip", "ppt", "pptx", "csv", "txt", "mp4"}


def curl(url: str, out: Path | None = None) -> tuple[str, str]:
    """GET with no User-Agent. Returns (status, body text) or (status, '') when saved to a file."""
    cmd = ["curl", "-sS", "-L", "-A", "", "-m", "90", url]
    if out is not None:
        r = subprocess.run(cmd[:-1] + ["-o", str(out), "-w", "%{http_code}", url], capture_output=True, text=True)
        return r.stdout.strip(), ""
    r = subprocess.run(cmd + ["-w", "\n%{http_code}"], capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    return code.strip(), body


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def classify_xml(text: str) -> str:
    """full | restricted_stub — a stub carries a publisher comment or has no real body."""
    if "does not allow downloading of the full text in XML" in text:
        return "restricted_stub"
    return "full" if re.search(r"<body[ >]", text) and len(text) > 20000 else "restricted_stub"


def figure_names(xml: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r'<graphic[^>]*xlink:href="([^"]+)"', xml)))


def bucket_keys(listing_xml: str) -> list[str]:
    return re.findall(r"<Key>([^<]+)</Key>", listing_xml)


def wanted(key: str, pmcid: str) -> str | None:
    """'figure', 'supplement', 'article_pdf' or None for a bucket key."""
    name = key.rsplit("/", 1)[-1]
    if re.search(r"\.(jpg|jpeg|png|gif)$", name, re.I):
        return "figure"
    if name == f"{pmcid}.1.pdf":
        return "article_pdf"
    if name.startswith(pmcid):
        return None
    return "supplement" if name.rsplit(".", 1)[-1].lower() in SUPP_EXT else None


def fetch(pmid: str, tag: str, root: Path, get=curl) -> dict:
    rec: dict = {"pmid": pmid, "files": []}
    code, body = get(f"{EUTILS}esummary.fcgi?db=pubmed&id={pmid}&retmode=json")
    try:
        ids = {x["idtype"]: x["value"] for x in json.loads(body)["result"][pmid]["articleids"]}
    except Exception:
        rec["error"] = f"esummary unreadable (HTTP {code})"
        return rec
    pmcid = ids.get("pmc")
    rec.update(doi=ids.get("doi"), pmcid=pmcid)
    if not pmcid:
        rec["error"] = "no PMCID: not in PMC, nothing to fetch lawfully here"
        return rec
    xml_path = root / "files/fulltext" / f"PMID{pmid}_{tag}_PMC_r2.xml"
    xml_path.parent.mkdir(parents=True, exist_ok=True)
    if xml_path.exists():
        rec["error"] = f"refusing to overwrite {xml_path}"
        return rec
    code, text = get(f"{EUTILS}efetch.fcgi?db=pmc&id={pmcid}&rettype=xml")
    xml_path.write_text(text, encoding="utf-8")
    rec["xml_state"] = classify_xml(text)
    rec["files"].append({"kind": "article_text", "path": str(xml_path.relative_to(root)), "http": code,
                         "bytes": xml_path.stat().st_size, "sha256": sha256(xml_path), "route": "pmc_efetch_xml"})
    code, listing = get(f"{BUCKET}?list-type=2&prefix={pmcid}.1/")
    for key in bucket_keys(listing):
        kind = wanted(key, pmcid)
        if kind is None:
            continue
        sub = {"figure": f"files/figures/PMID{pmid}_r2", "supplement": f"files/supplement/PMID{pmid}_r2",
               "article_pdf": f"files/supplement/PMID{pmid}_r2"}[kind]
        dest = root / sub / key.rsplit("/", 1)[-1]
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            continue
        c, _ = get(BUCKET + key, dest) if get is curl else get(BUCKET + key)
        if get is not curl:  # test double returns (status, body)
            dest.write_bytes(_.encode() if isinstance(_, str) else _)
        rec["files"].append({"kind": kind, "path": str(dest.relative_to(root)), "http": c,
                             "bytes": dest.stat().st_size, "sha256": sha256(dest), "route": "pmc_oa_opendata_s3"})
    if rec["xml_state"] == "full":
        missing = [n for n in figure_names(text) if not any(f["path"].endswith(n) or Path(f["path"]).stem == Path(n).stem
                                                           for f in rec["files"])]
        rec["figures_declared_in_xml_but_not_in_bucket"] = missing
    return rec


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pmid", required=True)
    ap.add_argument("--tag", required=True, help="AuthorYear tag used in the file name")
    ap.add_argument("--root", type=Path, default=Path.cwd())
    a = ap.parse_args(argv)
    rec = fetch(a.pmid, a.tag, a.root)
    print(json.dumps(rec, indent=1))
    if "error" in rec:
        return 1
    return 2 if rec.get("xml_state") != "full" else 0


if __name__ == "__main__":
    sys.exit(main())
