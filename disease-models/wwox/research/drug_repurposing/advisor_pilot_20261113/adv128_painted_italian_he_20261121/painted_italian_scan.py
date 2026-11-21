"""ADV-128 painted-text scan: Italian text visible on non-Italian pages. Usage: scan.py <label> <view-dir>  -> JSON in $OUT.
Detector (written before the scan):
 A  UI-source match: a painted text node equal to, or containing, an Italian interface string of ui_source.json (len >= 8, wording differs from its translation in that language)
 B  distinctive Italian function words (che, della, delle, degli, nella, nelle, sono, più, può, perché, anche, ogni, questo, questa, dei, gli, alla, dalla, quale, quali, è): >= 2 in one node
 C  short Italian label: node (3..60 chars) with one B word or an Italian-only suffix pattern (-zione, -mente, -ità, -are/-ire infinitive start) and no English/target stop word is NOT used (noisy);
    instead a vocabulary of Italian label words harvested from ui_source.json values of <= 4 words (exact node match).
Not counted: text inside [lang=it], .orig, <script>, <style>, display:none ancestors."""
import sys, json, re, os, tempfile
sys.path.insert(0, 'framework/scripts')
import repurposing_view as rv
DR = rv.DEFAULT_DR
I18N = DR / 'view/i18n'
src = json.loads((I18N / 'ui_source.json').read_text(encoding='utf-8'))
LANGS = ('en', 'fr', 'es', 'de')
tr = {l: json.loads((I18N / f'ui_{l}.json').read_text(encoding='utf-8')) for l in LANGS}
JS = r"""(function(){var out=[];var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null);var n;
while((n=w.nextNode())){var t=n.nodeValue.replace(/\s+/g,' ').trim();if(t.length<3)continue;var p=n.parentElement;if(!p)continue;
var tag=p.tagName;if(tag==='SCRIPT'||tag==='STYLE'||tag==='NOSCRIPT')continue;
if(p.closest('[lang="it"],.orig'))continue;if(!p.getClientRects().length)continue;out.push(t);}
return JSON.stringify(out)})()"""
B = re.compile(r"\b(che|della|delle|degli|nella|nelle|sono|più|può|perché|anche|ogni|questo|questa|dei|gli|alla|dalla|quale|quali|è)\b", re.I)
def classify(lang, nodes):
    ui_src = {k: v for k, v in src.items() if k.startswith('UI_IT.') and len(v) >= 8 and tr[lang].get(k) != v}
    ui_vals = set(ui_src.values())
    short_vals = {v for v in ui_vals if len(v.split()) <= 4}
    res = {'A': [], 'B': [], 'C': []}
    for t in nodes:
        if t in short_vals or any(v in t for v in ui_vals if len(v) >= 14):
            res['A'].append(t); continue
        if len(B.findall(t)) >= 2:
            res['B'].append(t); continue
        if t in short_vals: res['C'].append(t)
    return res
if __name__ == '__main__':
    label, vdir, out = sys.argv[1], sys.argv[2], sys.argv[3]
    pages = {}
    for lang in LANGS:
        pages[('full', lang)] = f'{vdir}/index.{lang}.html'
        pages[('shareable', lang)] = f'{vdir}/index_shareable.html' if lang == 'en' else f'{vdir}/index_shareable.{lang}.html'
    result = {}
    for (source, lang), path in pages.items():
        for width in (1280, 390):
            with tempfile.TemporaryDirectory(dir=os.path.expanduser('~/legend_browser_tmp')) as td:
                cdp = rv.Cdp(rv.find_chromium(), td)
                try:
                    cdp.call('Page.enable'); cdp.call('Emulation.setDeviceMetricsOverride', width=width, height=900, deviceScaleFactor=1, mobile=width < 500)
                    cdp.call('Page.navigate', url='file://' + path); cdp.wait_for("document.readyState==='complete'", 120); cdp.settle()
                    nodes = json.loads(cdp.evaluate(JS))
                finally: cdp.close()
            key = f'{source}|{lang}|{width}'
            result[key] = {'nodes': len(nodes), 'unique': sorted(set(nodes))}
            print(label, key, len(nodes), 'unique', len(set(nodes)), flush=True)
    json.dump(result, open(out, 'w'), ensure_ascii=False, indent=1)
