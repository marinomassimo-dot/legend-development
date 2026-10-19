#!/usr/bin/env python3
"""Does the DOI that PubMed stores for a PMID resolve to the same article PubMed describes?

WHY THIS EXISTS (2026-10-19, metabolic batch, scientist-b)
-----------------------------------------------------------
PMID 31145772 is a hybrid record: PubMed shows the title and abstract of Jamaspishvili et al.
2019 (Acta Biochim Pol 66:159-165) together with the authors, DOI and page range of a 2021
Permana et al. article. Following the stored DOI at the publisher served a different paper's PDF,
and nothing in the pipeline noticed: the selection file even carried the wrong first author. An
actor who reads the PDF that the DOI returns reads the wrong article; an actor who trusts the
title reads a DOI that does not carry it. The check below is the one-call test.

WHAT IT DOES
------------
For each PMID: fetch the PubMed record (efetch XML), then the Crossref record of the DOI PubMed
stores, and compare (a) title word overlap and (b) the first author's family name. It returns a
record that names both identities and the verdict, never a bare boolean:

  MATCH          title overlap >= 0.6 and the first author's family name agrees
  TITLE_MISMATCH PubMed's title and Crossref's title for the stored DOI are different works
  AUTHOR_MISMATCH the titles agree but the first author's family name does not
  NO_DOI / CROSSREF_UNAVAILABLE   nothing to compare; this is not a pass

Exit code 0 only when every PMID is MATCH. A MISMATCH is a prompt to look at the true DOI (a
Crossref bibliographic search by PubMed's title usually names it), not a claim about which record
is wrong. Network: NCBI eutils and api.crossref.org, no key, no spend.

  python3 framework/scripts/pubmed_identity_check.py --pmid 31145772 --pmid 33520443
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

STOP = set("a an and of the in on for to with by at from as is are was were be or its their into using use via study analysis".split())


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", (text or "").lower()) if w not in STOP and len(w) > 2}


def overlap(a: str, b: str) -> float:
    wa, wb = words(a), words(b)
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / min(len(wa), len(wb))


def norm_name(s: str) -> str:
    return re.sub(r"[^a-z]", "", (s or "").lower())


def verdict(pubmed: dict, crossref: dict | None, threshold: float = 0.6) -> dict:
    """Pure function: compares two already-fetched identity records."""
    out = {"pmid": pubmed.get("pmid"), "doi": pubmed.get("doi"), "pubmed_title": pubmed.get("title"),
           "pubmed_first_author": pubmed.get("first_author"), "crossref_title": (crossref or {}).get("title"),
           "crossref_first_author": (crossref or {}).get("first_author")}
    if not pubmed.get("doi"):
        out["verdict"] = "NO_DOI"
        return out
    if not crossref:
        out["verdict"] = "CROSSREF_UNAVAILABLE"
        return out
    out["title_overlap"] = round(overlap(pubmed.get("title", ""), crossref.get("title", "")), 3)
    if out["title_overlap"] < threshold:
        out["verdict"] = "TITLE_MISMATCH"
    elif norm_name(pubmed.get("first_author")) != norm_name(crossref.get("first_author")):
        out["verdict"] = "AUTHOR_MISMATCH"
    else:
        out["verdict"] = "MATCH"
    return out


def _get(url: str, retries: int = 5) -> bytes:
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": ""}), timeout=30) as r:
                return r.read()
        except Exception:
            time.sleep(2 + 2 * i)
    raise RuntimeError(f"could not fetch {url}")


def fetch_pubmed(pmid: str) -> dict:
    xml = _get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=" + pmid)
    root = ET.fromstring(xml)
    art = root.find(".//PubmedArticle")
    title = "".join(art.find(".//ArticleTitle").itertext()) if art is not None and art.find(".//ArticleTitle") is not None else ""
    first = art.find(".//AuthorList/Author/LastName") if art is not None else None
    doi = None
    for e in (art.findall(".//ELocationID") if art is not None else []):
        if e.get("EIdType") == "doi":
            doi = (e.text or "").strip()
    if doi is None and art is not None:
        for e in art.findall(".//ArticleId"):
            if e.get("IdType") == "doi":
                doi = (e.text or "").strip()
    return {"pmid": pmid, "title": title, "doi": doi, "first_author": first.text if first is not None else None}


def fetch_crossref(doi: str) -> dict | None:
    try:
        data = json.loads(_get("https://api.crossref.org/works/" + urllib.parse.quote(doi)))["message"]
    except Exception:
        return None
    fam = (data.get("author") or [{}])[0].get("family")
    return {"title": (data.get("title") or [""])[0], "first_author": fam}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--pmid", action="append", required=True)
    args = ap.parse_args(argv)
    bad = 0
    for pmid in args.pmid:
        pm = fetch_pubmed(pmid)
        rec = verdict(pm, fetch_crossref(pm["doi"]) if pm.get("doi") else None)
        print(json.dumps(rec, ensure_ascii=False))
        bad += rec["verdict"] != "MATCH"
        time.sleep(0.4)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
