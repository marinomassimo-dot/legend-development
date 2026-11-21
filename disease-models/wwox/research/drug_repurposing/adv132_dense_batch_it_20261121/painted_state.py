"""ADV-132 painted state of the shareable pages: for the 50 ADV-131 passages and the 25 ADV-132 passages, per language and width, how many are painted as English / as their translation, in which sections, and which sections carry the English-source notice.
Usage: painted_state.py <dir-with-pages> <out.json>   (run from the repository root; Chromium through repurposing_view.Cdp, TMPDIR under the home)"""
import sys, json, os, re, tempfile, html
sys.path.insert(0, "framework/scripts")
import repurposing_view as rv
vdir, out = sys.argv[1], sys.argv[2]
R = "disease-models/wwox/research/drug_repurposing/"
S50 = json.load(open(R + "adv131_english_batch_it_20261121/selected50.json"))
S25 = json.load(open(R + "adv132_dense_batch_it_20261121/selected_batch3.json"))
I = R + "view/i18n/"
JS = r"""(function(){var out=[];var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null);var n;
while((n=w.nextNode())){var t=n.nodeValue.replace(/\s+/g,' ').trim();if(t.length<3)continue;var p=n.parentElement;if(!p)continue;
var tag=p.tagName;if(tag==='SCRIPT'||tag==='STYLE'||tag==='NOSCRIPT')continue;if(!p.getClientRects().length)continue;
var s=p.closest('section');out.push([s?s.id:'',t,p.classList.contains('sec-en-note')?1:0]);}
return JSON.stringify(out)})()"""
res = {}
for lang in ("fr", "de", "es"):
    tr = json.load(open(I + f"content_{lang}.json"))
    for width in (1280, 390):
        with tempfile.TemporaryDirectory(dir=os.path.expanduser("~/legend_browser_tmp")) as td:
            cdp = rv.Cdp(rv.find_chromium(), td)
            try:
                cdp.call("Page.enable"); cdp.call("Emulation.setDeviceMetricsOverride", width=width, height=900, deviceScaleFactor=1, mobile=width < 500)
                cdp.call("Page.navigate", url="file://" + f"{vdir}/index_shareable.{lang}.html"); cdp.wait_for("document.readyState==='complete'", 120); cdp.settle()
                nodes = json.loads(cdp.evaluate(JS))
            finally:
                cdp.close()
        row = {"notice_sections": sorted({s for s, t, f in nodes if f})}
        for name, sel in (("batch50", S50), ("batch25", S25)):
            en = {o["text"]: o["n"] for o in sel}
            trd = {re.sub(r"\s+", " ", html.unescape(tr[o["hash"]])): o["n"] for o in sel if o["hash"] in tr}
            e, t = {}, {}
            for sec, txt, f in nodes:
                if txt in en: e.setdefault(en[txt], set()).add(sec)
                if txt in trd: t.setdefault(trd[txt], set()).add(sec)
            row[name] = {"english_painted": len(e), "translated_painted": len(t), "english_sections": sorted({s for v in e.values() for s in v}),
                         "english_in_section_with_notice": len([n for n, v in e.items() if v & set(row["notice_sections"])])}
        res[f"{lang}|{width}"] = row
        print(lang, width, json.dumps(row), flush=True)
json.dump(res, open(out, "w"), indent=1)
