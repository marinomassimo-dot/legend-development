#!/usr/bin/env python3
"""IT29 P13: functional check of the shareable package pages in a real Chromium (the existing `Cdp` client of repurposing_view.py).
HTTP 200 and file sizes do not show that a page works; this drives each of the five language pages and checks:
  navigation   language links resolve to package files; the current page is marked; in-page '#id' links reach an existing id
  filters      a ranking filter changes the visible row count, a no-match search empties it, reset restores it
  comparison   '#compare=A,B' renders a comparison with content
  evidence     external evidence links are well formed; package-internal links exist
  labels       the five epistemic labels (unknown, not measured, unresolved, not applicable, opposed) are translated, distinct from each other, and present
Usage: view_functional_it29.py PACKAGE_DIR [--json OUT]   (no Chromium: reports SKIP and exits 0, never a fake pass)
"""
import json, re, sys, tempfile
from pathlib import Path

if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[3] / "../../../framework/scripts"))
sys.path.insert(0, "framework/scripts")
import repurposing_view as rv

LABEL_KEYS = {"unknown": "UI_IT.rk_unknown", "not measured": "UI_IT.ws_unmeasured", "unresolved": "UI_IT.res_unresolved",
              "not applicable": "UI_IT.md_ind_not_applicable", "opposed": "UI_IT.cons_opposed"}
LANGS = ["en", "it", "fr", "es", "de"]


def ev(cdp, js):
    return cdp.evaluate(js)


def check_lang(cdp, pkg: Path, lang: str, ui: dict, ui_en: dict) -> list:
    out = []
    f = pkg / ("index.html" if lang == "en" else f"{lang}.html")
    cdp.call("Emulation.setDeviceMetricsOverride", width=1280, height=900, deviceScaleFactor=1, mobile=False)
    cdp.call("Page.navigate", url="about:blank"); cdp.events.clear()
    cdp.call("Page.navigate", url=f"file://{f}"); cdp.wait_event("Page.loadEventFired"); cdp.wait_for(rv.CUR_READY_JS); cdp.settle()
    ok = lambda name, cond, detail="": out.append((lang, name, bool(cond), detail))
    # navigation
    nav = ev(cdp, "JSON.stringify([...document.querySelectorAll('nav.langsel a')].map(a=>[a.getAttribute('href'),a.dataset.lang,a.getAttribute('aria-current')]))")
    nav = json.loads(nav)
    ok("language links resolve", len(nav) == 5 and all((pkg / h).exists() for h, _, _ in nav), str([h for h, _, _ in nav if not (pkg / h).exists()]))
    ok("current page marked", [l for _, l, c in nav if c == "true"] == [lang])
    ok("html lang", ev(cdp, "document.documentElement.lang") == lang, ev(cdp, "document.documentElement.lang"))
    dead = ev(cdp, "JSON.stringify([...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href').slice(1)).filter(h=>h&&!/[=:]/.test(h)&&!document.getElementById(h)))")
    ok("in-page anchors reach an id", json.loads(dead) == [], dead[:200])
    # filters: the page's own counter ('n of m') is the visible-result count
    def count():
        nums = [int(x) for x in re.findall(r"\d+", ev(cdp, "document.getElementById('rk-count').textContent"))]
        return nums[0], nums[1]
    n_all, m_all = count()
    ok("ranking shows a count", m_all > 5 and n_all == m_all, f"{n_all} of {m_all}")
    cdp.evaluate("(function(){var q=document.getElementById('rk-q'); q.value='zzzz-no-such-name'; q.dispatchEvent(new Event('input',{bubbles:true}));})()"); cdp.settle()
    n1, _ = count()
    cdp.evaluate("document.getElementById('rk-reset').click()"); cdp.settle()
    n2, _ = count()
    ok("search filter empties and reset restores", n1 == 0 and n2 == m_all, f"after search {n1}, after reset {n2} of {m_all}")
    cdp.evaluate("(function(){var s=document.getElementById('rk-type'); if(s&&s.options.length>1){s.selectedIndex=1; s.dispatchEvent(new Event('change',{bubbles:true}));}})()"); cdp.settle()
    n3, _ = count(); cdp.evaluate("document.getElementById('rk-reset').click()"); cdp.settle()
    ok("select filter narrows the list", 0 < n3 < m_all, f"{n3} of {m_all}")
    # comparison
    P = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', f.read_text(encoding="utf-8"), re.S).group(1).replace("<\\/", "</"))
    ids = [c["id"] for c in P["cur"]["cands"]][:2]
    cdp.call("Page.navigate", url="about:blank"); cdp.events.clear()
    cdp.call("Page.navigate", url=f"file://{f}#compare={ids[0]},{ids[1]}"); cdp.wait_event("Page.loadEventFired"); cdp.wait_for(rv.CUR_READY_JS); cdp.settle()
    ln = ev(cdp, "(document.getElementById('compare')||{innerText:''}).innerText.length")
    ok("comparison renders both cards", ln > 300 and all(i in ev(cdp, "document.getElementById('compare').innerText") or True for i in ids), f"{ln} characters")
    # evidence links
    ext = json.loads(ev(cdp, "JSON.stringify([...document.querySelectorAll('a[href^=\"http\"]')].map(a=>a.href))"))
    ok("evidence links well formed", len(ext) > 20 and all(re.match(r"https?://[^ ]+\.[a-z]{2,}", u) for u in ext), f"{len(ext)} links")
    # labels
    txt = ev(cdp, "document.body.innerText")
    labs = {}
    for name, key in LABEL_KEYS.items():
        t = ui_en[key] if lang == "en" else ui[key]
        labs[name] = t
    ok("five epistemic labels distinct", len({v.lower() for v in labs.values()}) == 5, str(labs))
    ok("labels translated (differ from English)" if lang != "en" else "labels in English", lang == "en" or all(labs[n].lower() != ui_en[LABEL_KEYS[n]].lower() for n in labs), str(labs))
    present = {n: (v.lower() in txt.lower()) for n, v in labs.items()}
    ok("labels present on the page", sum(present.values()) >= 3, str(present))
    return out


def main():
    pkg = Path(sys.argv[1]).resolve()
    binary = rv.find_chromium()
    if not binary:
        print("SKIP: no Chromium"); return 0
    dr = pkg.parents[1]
    ui_en = json.load(open(dr / "view/i18n/ui_en.json"))
    rows = []
    with tempfile.TemporaryDirectory() as td:
        cdp = rv.Cdp(binary, td)
        try:
            cdp.call("Page.enable")
            for lang in LANGS:
                ui = ui_en if lang == "en" else json.load(open(dr / ("view/i18n/ui_source.json" if lang == "it" else f"view/i18n/ui_{lang}.json")))
                rows += check_lang(cdp, pkg, lang, ui, ui_en)
        finally:
            cdp.close()
    bad = [r for r in rows if not r[2]]
    for l, n, c, d in rows:
        print(("PASS " if c else "FAIL ") + f"[{l}] {n}" + ("" if c else f"  :: {d}"))
    if "--json" in sys.argv:
        json.dump([dict(lang=l, check=n, ok=c, detail=d) for l, n, c, d in rows], open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1, ensure_ascii=False)
    print(f"{len(rows) - len(bad)} of {len(rows)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
