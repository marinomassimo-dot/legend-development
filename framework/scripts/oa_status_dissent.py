#!/usr/bin/env python3
"""Detect the case where every DOI-keyed open-access index says CLOSED and all of them are wrong.

🔴 WHY THIS EXISTS, measured rather than imagined.

On 2026-09-09, PMID 24510053 (DOI 10.1177/1535370213519213) was reported closed by
**five independent sources at once**:

    NCBI idconv        "Identifier not found in PMC"
    Europe PMC         isOpenAccess N, inPMC N, inEPMC N
    Unpaywall          is_oa false, oa_status closed, ZERO oa_locations
    OpenAlex           is_oa false, two non-OA locations
    Semantic Scholar   openAccessPdf.status CLOSED

All five were wrong. The article is served free and complete on its publisher's current
platform. Every one of those indexes keys on the **DOI record**, and the DOI prefix
(10.1177 = SAGE) still names the *original* publisher, while the journal has since
migrated to a different one. Crossref was the only structured source that showed it:
its `publisher` field read "Frontiers Media SA" against a `sagepub.com` licence URL.

The failure mode is therefore NOT "an index was stale". It is:

    a closed verdict from DOI-keyed indexes is not evidence of a paywall
    when the journal has changed publisher since the DOI was minted.

That is a general fact about scholarly infrastructure, not a fact about one paper, and it
costs a real reading every time it is believed. Journals migrate constantly (society
titles moving between SAGE, Wiley, Springer, Frontiers, Karger, OUP); the DOI prefix is
immutable by design and therefore goes stale by design.

WHAT THIS TOOL DOES

Given a DOI, it asks Crossref two questions the OA indexes never ask:

    1. who does Crossref say the CURRENT publisher is?      (works/<doi> -> .publisher)
    2. who OWNS the DOI prefix?                             (prefixes/<prefix> -> .name)

When those disagree, the DOI prefix is stale, and any "closed" verdict derived from it is
untrustworthy. The tool returns PUBLISHER_MIGRATION_SUSPECTED and names the current
publisher, so the retrieval cascade can be pointed at the right platform instead of
stopping at a false paywall.

WHAT IT DELIBERATELY DOES NOT DO

It does not fetch the article, does not guess a URL, and does not assert the paper is
open. It asserts only that **the closed verdict is not evidence**, which is the whole of
what the measurement supports. Overstating that would be the same class of error the tool
exists to catch.

Usage:
    oa_status_dissent.py 10.1177/1535370213519213
    oa_status_dissent.py --json 10.1177/1535370213519213
    oa_status_dissent.py --offline-fixture <path.json>     # tests; no network
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "LEGEND-research/1.0 (rare-disease literature model; metadata only)"
TIMEOUT = 30

VERDICT_MIGRATION = "PUBLISHER_MIGRATION_SUSPECTED"
VERDICT_CONSISTENT = "PREFIX_CONSISTENT"
VERDICT_UNKNOWN = "UNDETERMINED"

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")


def doi_prefix(doi: str) -> str:
    """The registrant prefix of a DOI: everything before the first '/'."""
    return doi.split("/", 1)[0]


def _get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as fh:
        return json.loads(fh.read().decode("utf-8", "replace"))


def fetch_crossref(doi: str) -> dict:
    """Current publisher, title, licence hosts — the fields the OA indexes do not expose."""
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    msg = _get_json(url)["message"]
    return {
        "publisher": msg.get("publisher"),
        "container_title": (msg.get("container-title") or [None])[0],
        "licence_urls": [lic.get("URL") for lic in msg.get("license", []) if lic.get("URL")],
        "link_urls": [ln.get("URL") for ln in msg.get("link", []) if ln.get("URL")],
    }


def fetch_prefix_owner(prefix: str) -> str | None:
    """Who Crossref says OWNS the prefix. This is what every DOI-keyed index inherits."""
    data = _get_json("https://api.crossref.org/prefixes/" + urllib.parse.quote(prefix))
    return (data.get("message") or {}).get("name")


def _norm(name: str | None) -> str:
    """Compare publisher names on their significant words only.

    🔴 Deliberately crude, and the crudeness is the safe direction. A false
    PREFIX_CONSISTENT would silence the tool on a real migration; a false
    PUBLISHER_MIGRATION_SUSPECTED only causes one extra look at a platform. So this
    normaliser strips corporate suffixes and matches on the leading significant token,
    which merges 'SAGE Publications' with 'SAGE Publications Ltd' but keeps 'SAGE' and
    'Frontiers Media SA' apart.
    """
    if not name:
        return ""
    n = name.lower()
    # Separators first: a hyphen is a word boundary here, not a character. Without this,
    # "Wiley" and "Wiley-Blackwell" compare as different leading tokens and a routine
    # imprint rename is reported as a migration. Caught by its own regression.
    for sep in ("-", "/", "–", "—", "'", "’"):
        n = n.replace(sep, " ")
    for junk in (
        "publications", "publishing", "publishers", "publisher", "press",
        "media", "group", "ltd", "limited", "inc", "llc", "sa", "bv", "b.v.",
        "gmbh", "ag", "co", "company", "&", ",", ".", "(", ")",
    ):
        n = n.replace(junk, " ")
    return " ".join(n.split())


def compare(crossref: dict, prefix_owner: str | None) -> dict:
    current = crossref.get("publisher")
    a, b = _norm(current), _norm(prefix_owner)
    if not a or not b:
        verdict = VERDICT_UNKNOWN
        why = "Crossref did not supply both a current publisher and a prefix owner."
    elif a == b or a.split()[:1] == b.split()[:1]:
        verdict = VERDICT_CONSISTENT
        why = (
            "The DOI prefix owner and the current publisher agree, so a closed verdict "
            "from a DOI-keyed index is not undermined by a migration. It may still be "
            "wrong for other reasons; this tool tests one failure mode only."
        )
    else:
        verdict = VERDICT_MIGRATION
        why = (
            "The DOI prefix is owned by %r while Crossref reports the current publisher "
            "as %r. Every DOI-keyed open-access index (Unpaywall, OpenAlex, Semantic "
            "Scholar, Europe PMC, NCBI idconv) inherits the stale prefix, so a CLOSED "
            "verdict from them is NOT evidence of a paywall. Search the current "
            "publisher's own platform before declaring the article unavailable."
            % (prefix_owner, current)
        )
    return {"verdict": verdict, "explanation": why}


def assess(doi: str, fetcher=fetch_crossref, prefix_fetcher=fetch_prefix_owner) -> dict:
    if not DOI_RE.match(doi):
        raise ValueError("not a DOI: %r" % doi)
    crossref = fetcher(doi)
    prefix = doi_prefix(doi)
    owner = prefix_fetcher(prefix)
    out = {
        "doi": doi,
        "doi_prefix": prefix,
        "prefix_owner": owner,
        "current_publisher": crossref.get("publisher"),
        "container_title": crossref.get("container_title"),
        "licence_urls": crossref.get("licence_urls", []),
    }
    out.update(compare(crossref, owner))
    return out


def render(result: dict) -> str:
    lines = [
        "DOI                %s" % result["doi"],
        "prefix             %s" % result["doi_prefix"],
        "prefix owner       %s" % result["prefix_owner"],
        "current publisher  %s" % result["current_publisher"],
        "journal            %s" % result["container_title"],
        "",
        "VERDICT: %s" % result["verdict"],
        "",
        result["explanation"],
    ]
    if result["verdict"] == VERDICT_MIGRATION:
        lines += [
            "",
            "NEXT: this tool does not fetch and does not claim the article is open. It "
            "claims only that the closed verdict carries no weight. Point find-fulltext "
            "at the current publisher's platform and let it validate what comes back.",
        ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("doi", nargs="?", help="the DOI to assess")
    ap.add_argument("--json", action="store_true", help="emit the record as JSON")
    ap.add_argument("--offline-fixture",
                    help="a JSON file with keys crossref/prefix_owner/doi; no network")
    args = ap.parse_args()

    if args.offline_fixture:
        fx = json.load(open(args.offline_fixture, encoding="utf-8"))
        result = assess(fx["doi"],
                        fetcher=lambda _d: fx["crossref"],
                        prefix_fetcher=lambda _p: fx["prefix_owner"])
    else:
        if not args.doi:
            ap.error("a DOI is required unless --offline-fixture is given")
        try:
            result = assess(args.doi)
        except urllib.error.HTTPError as exc:
            print("Crossref refused the request (HTTP %s). No verdict." % exc.code,
                  file=sys.stderr)
            return 2
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2

    print(json.dumps(result, indent=1) if args.json else render(result))
    return 0 if result["verdict"] != VERDICT_UNKNOWN else 1


if __name__ == "__main__":
    raise SystemExit(main())
