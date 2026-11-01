#!/usr/bin/env python3
"""Post-publication checker for the shareable repurposing view (DEPLOY.md section 12, conditions a to f).

Read-only and GET-only: stdlib, no credential, no write, no request to any host other than the base URL's own.
The base URL is a required argument; there is no default and the production URL is never assumed.

  python3 -B check_published_view.py BASE_URL [--deploy-md PATH]

Conditions checked against BASE_URL (every file path is relative to it, so a path prefix such as /legend-development/ is part of it):
  a  index.html answers 200
  b  every package file answers 200 and equals the byte count and SHA-256 of the DEPLOY.md section 4 table,
     and the served manifest.json lists the same digests; no served manifest entry is missing from the table
  c  exactly one robots meta tag, with noindex,nofollow
  d  NOTICE.md, LICENSES/CC-BY-SA-3.0.txt and class_b/chembl_cc-by-sa-3.0/CREDIT.txt answer 200 (also covered by b)
  e  the footer of the served page names every source of NOTICE.md section 2
  f  #ranking, #deepened-cases and a #cand- id exist in the served page; no root-absolute src/href and no <base> tag
     (the page survives under a path prefix); no resource loaded from another host (script, stylesheet, image, frame, @import, url())
Not checked here: g (repurposing_view.py viewports, on the package file) and h (repurposing_view.py audit-shareable --dynamic).

Exit codes: 0 every condition holds; 1 at least one FAIL line; 2 usage error; 3 NOT_YET_PUBLISHED (index.html answers 404 at the
production URL: an expected state before the reserved act, reported and never a pass).
"""
import argparse
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

PRODUCTION_URL = "https://marinomassimo-dot.github.io/legend-development/"   # compared with, never defaulted to
HERE = Path(__file__).resolve().parent
DEFAULT_DEPLOY = HERE.parent / "view" / "DEPLOY.md"
EXTRA_200 = ["NOTICE.md", "LICENSES/CC-BY-SA-3.0.txt", "class_b/chembl_cc-by-sa-3.0/CREDIT.txt"]
ANCHORS = ["ranking", "deepened-cases"]


class _SameHost(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urllib.parse.urlsplit(newurl).netloc != urllib.parse.urlsplit(req.full_url).netloc:
            raise urllib.error.HTTPError(req.full_url, code, "redirect to another host refused: " + newurl, headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def get(url, timeout=30):
    """(status, bytes). Transport failure -> (0, message bytes). Only GET."""
    op = urllib.request.build_opener(_SameHost)
    try:
        with op.open(urllib.request.Request(url, method="GET", headers={"User-Agent": "legend-view-checker/1"}), timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # noqa: BLE001 - any transport failure is a FAIL line, not a crash
        return 0, str(e).encode()


def deploy_table(path):
    text = Path(path).read_text(encoding="utf-8")
    m = re.search(r"<!-- FILES:BEGIN.*?-->(.*?)<!-- FILES:END -->", text, re.S)
    if not m:
        raise SystemExit("usage error: no FILES:BEGIN/END table in " + str(path))
    rows = re.findall(r"^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \|$", m.group(1), re.M)
    if not rows:
        raise SystemExit("usage error: the table in %s has no rows" % path)
    return {p: (int(b), s) for p, b, s in rows}


class _Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.robots, self.ids, self.loads, self.rooted, self.style, self.footer = [], set(), [], [], [], []
        self.base = 0
        self._in_style = False
        self._in_footer = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "meta" and (a.get("name") or "").lower() == "robots":
            self.robots.append((a.get("content") or "").lower())
        if tag == "base":
            self.base += 1
        if tag == "style":
            self._in_style = True
        if tag == "footer":
            self._in_footer += 1
        for k in ("src", "href", "data", "poster", "srcset"):
            v = a.get(k)
            if v is None:
                continue
            loads = (k != "href") or (tag == "link")      # <a href> is a link, not a load
            if loads and re.match(r"(?i)(https?:)?//", v.strip()):
                self.loads.append("<%s %s=%s>" % (tag, k, v[:80]))
            if k in ("src", "href") and v.startswith("/") and not v.startswith("//"):
                self.rooted.append("<%s %s=%s>" % (tag, k, v[:80]))
        if a.get("style"):
            self.style.append(a["style"])

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False
        if tag == "footer" and self._in_footer:
            self._in_footer -= 1

    def handle_data(self, d):
        if self._in_style:
            self.style.append(d)
        if self._in_footer:
            self.footer.append(d)


def notice_sources(notice_text):
    sec = re.search(r"^## 2\..*?(?=^## 3\.)", notice_text, re.S | re.M)
    return re.findall(r"^- \*\*(.+?)\*\*", sec.group(0), re.M) if sec else []


def run(base, table):
    out = []                                        # (ok, condition, text)

    def ok(c, t):
        out.append((True, c, t))

    def bad(c, t):
        out.append((False, c, t))

    base = base if base.endswith("/") else base + "/"
    served = {}
    ist, ibody = get(base + "index.html")
    (ok if ist == 200 else bad)("a", "index.html answers %s at %sindex.html" % (ist, base))
    for rel, (nbytes, want) in sorted(table.items()):
        st, body = (ist, ibody) if rel == "index.html" else get(base + rel)
        if st != 200:
            bad("b", "%s answers %s" % (rel, st))
            if rel in EXTRA_200:
                bad("d", "%s answers %s" % (rel, st))
            continue
        served[rel] = body
        have = hashlib.sha256(body).hexdigest()
        if len(body) == nbytes and have == want:
            ok("b", "%s matches the table (%d bytes, %s...)" % (rel, nbytes, want[:12]))
        else:
            bad("b", "%s differs from the table: %d bytes vs %d, sha256 %s... vs %s..." % (rel, len(body), nbytes, have[:12], want[:12]))
        if rel in EXTRA_200:
            ok("d", "%s answers 200" % rel)
    if "manifest.json" in served:
        try:
            files = json.loads(served["manifest.json"])["files"]
            for rel, meta in files.items():
                if rel not in table:
                    bad("b", "served manifest.json lists %s, absent from the DEPLOY.md table" % rel)
                elif meta.get("sha256") != table[rel][1] or meta.get("bytes") != table[rel][0]:
                    bad("b", "served manifest.json disagrees with the table on %s" % rel)
            ok("b", "served manifest.json cross-checked against the table (%d entries)" % len(files))
        except Exception as e:  # noqa: BLE001
            bad("b", "served manifest.json unreadable: %s" % e)
    page = served.get("index.html")
    if page is None:
        bad("c-f", "no index.html served: robots, footer, anchors and external-load checks not run")
        return out
    sc = _Scan()
    sc.feed(page.decode("utf-8", "replace"))
    if len(sc.robots) == 1 and "noindex" in sc.robots[0] and "nofollow" in sc.robots[0]:
        ok("c", "one robots meta tag: " + sc.robots[0])
    else:
        bad("c", "robots meta tags found: %r (want exactly one noindex,nofollow)" % sc.robots)
    names = notice_sources(served["NOTICE.md"].decode("utf-8", "replace")) if "NOTICE.md" in served else []
    foot = html.unescape(" ".join(sc.footer))
    if not names:
        bad("e", "no source names parsed from NOTICE.md section 2 (NOTICE.md not served or changed shape)")
    for n in names:
        if n in foot:
            ok("e", "footer names '%s'" % n)
        else:
            bad("e", "footer does not name NOTICE source '%s'" % n)
    for a in ANCHORS:
        (ok if a in sc.ids else bad)("f", "anchor #%s %s" % (a, "present" if a in sc.ids else "MISSING in the served page"))
    cands = sorted(i for i in sc.ids if i.startswith("cand-"))
    (ok if cands else bad)("f", "a #cand- id %s" % ("present (" + cands[0] + ")" if cands else "MISSING in the served page"))
    if sc.rooted:
        bad("f", "root-absolute reference breaks under a path prefix: %s" % sc.rooted[:3])
    else:
        ok("f", "no root-absolute src/href")
    if sc.base:
        bad("f", "<base> tag present")
    else:
        ok("f", "no <base> tag")
    css = " ".join(sc.style)
    ext = list(sc.loads) + re.findall(r"@import\s+[^;]*(?:https?:)?//[^;]+", css) + re.findall(r"url\(\s*['\"]?(?:https?:)?//[^)]+\)", css)
    if ext:
        bad("f", "resource loaded from another host: %s" % ext[:3])
    else:
        ok("f", "no resource loaded from another host")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check a published copy of the shareable repurposing view against DEPLOY.md section 12 (a to f). GET only; base URL required.")
    ap.add_argument("base_url", help="the URL the package is served at, including any path prefix (no default)")
    ap.add_argument("--deploy-md", default=str(DEFAULT_DEPLOY), help="DEPLOY.md holding the section 4 table")
    a = ap.parse_args(argv)
    if urllib.parse.urlsplit(a.base_url).scheme not in ("http", "https"):
        print("usage error: base URL must be http(s)", file=sys.stderr)
        return 2
    table = deploy_table(a.deploy_md)
    base = a.base_url if a.base_url.endswith("/") else a.base_url + "/"
    if base == PRODUCTION_URL:
        st, _ = get(base + "index.html")
        if st == 404:
            print("NOT_YET_PUBLISHED: %sindex.html answers 404, the expected state before the operator's publication act. This is not a pass." % base)
            return 3
    res = run(base, table)
    for good, cond, text in res:
        print("%s [%s] %s" % ("PASS" if good else "FAIL", cond, text))
    fails = [r for r in res if not r[0]]
    print("RESULT: %s (%d checks, %d failed) at %s" % ("FAIL" if fails else "PASS", len(res), len(fails), base))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
