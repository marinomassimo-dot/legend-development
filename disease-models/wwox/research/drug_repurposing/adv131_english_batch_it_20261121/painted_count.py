"""ADV-131 painted count: how many of the selected English passages are painted (visible text nodes) as English, and how many as their translation, per page and width.
Usage: painted.py <label> <dir-with-pages> <N passages> <out.json>   (run from the repository root; Chromium through repurposing_view.Cdp, TMPDIR under the home)"""
import sys, json, os, re, tempfile, html
sys.path.insert(0, "framework/scripts")
import repurposing_view as rv
label, vdir, N, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
T = os.environ["CLAUDE_JOB_DIR"] + "/tmp/adv131/"
sel = json.load(open(T + "selected50.json"))[:N]
I = "disease-models/wwox/research/drug_repurposing/view/i18n/"
JS = r"""(function(){var out=[];var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null);var n;
while((n=w.nextNode())){var t=n.nodeValue.replace(/\s+/g,' ').trim();if(t.length<3)continue;var p=n.parentElement;if(!p)continue;
var tag=p.tagName;if(tag==='SCRIPT'||tag==='STYLE'||tag==='NOSCRIPT')continue;if(!p.getClientRects().length)continue;
var s=p.closest('section');out.push([s?s.id:'',t]);}
return JSON.stringify(out)})()"""
res = {}
for lang in ("fr", "de", "es"):
    tr = json.load(open(I + f"content_{lang}.json"))
    en = {o["text"]: o["n"] for o in sel}
    trd = {re.sub(r"\s+", " ", html.unescape(tr[o["hash"]])): o["n"] for o in sel if o["hash"] in tr}
    for width in (1280, 390):
        with tempfile.TemporaryDirectory(dir=os.path.expanduser("~/legend_browser_tmp")) as td:
            cdp = rv.Cdp(rv.find_chromium(), td)
            try:
                cdp.call("Page.enable"); cdp.call("Emulation.setDeviceMetricsOverride", width=width, height=900, deviceScaleFactor=1, mobile=width < 500)
                cdp.call("Page.navigate", url="file://" + f"{vdir}/index_shareable.{lang}.html"); cdp.wait_for("document.readyState==='complete'", 120); cdp.settle()
                nodes = json.loads(cdp.evaluate(JS))
            finally:
                cdp.close()
        e = {}; t = {}
        for sec, txt in nodes:
            if txt in en: e.setdefault(en[txt], set()).add(sec)
            if txt in trd: t.setdefault(trd[txt], set()).add(sec)
        key = f"{lang}|{width}"
        res[key] = {"nodes": len(nodes), "english_passages_painted": len(e), "english_in_scope_sections": len([n for n, s in e.items() if s & {"overview", "ranking"}]),
                    "translated_passages_painted": len(t), "english_passage_numbers": sorted(e), "translated_passage_numbers": sorted(t)}
        print(label, key, {k: v for k, v in res[key].items() if not k.endswith("numbers")}, flush=True)
json.dump(res, open(out, "w"), indent=1)
