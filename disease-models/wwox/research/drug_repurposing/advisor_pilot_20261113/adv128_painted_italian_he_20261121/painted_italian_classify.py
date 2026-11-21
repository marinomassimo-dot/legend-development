"""Offline classifier for scan.py output. Detectors:
 A  Italian UI-source string (ui_source.json, len>=8, wording differs from its translation in the page language) equal to / inside the node
 B  >= 2 distinctive Italian function words
 D  data-driven lexicon: words (>=4 letters) of the Italian sources (ui_source + content_source values) that occur in NO translation of that language (ui_<l>, content_<l>) and not in the English
    translations either; node is Italian when it has >=1 such word of >=5 letters and they make >= 50% of its words of >=4 letters
Reports per (source, lang, width): unique Italian nodes by detector (a node counted once, first detector wins A>B>D)."""
import sys, json, re
sys.path.insert(0, 'framework/scripts')
import repurposing_view as rv
I = rv.DEFAULT_DR / 'view/i18n'
J = lambda n: json.loads((I / n).read_text(encoding='utf-8'))
src_ui, src_ct = J('ui_source.json'), J('content_source.json')
tr_ui = {l: J(f'ui_{l}.json') for l in ('en', 'fr', 'es', 'de')}
tr_ct = {l: J(f'content_{l}.json') for l in ('en', 'fr', 'es', 'de')}
WORD = re.compile(r"[^\W\d_]{4,}", re.U)
def words(texts):
    out = set()
    for t in texts:
        out.update(w.lower() for w in WORD.findall(t if isinstance(t, str) else ''))
    return out
it_words = words(list(src_ui.values()) + [v['text'] for v in src_ct.values()])
en_words = words(list(tr_ui['en'].values()) + list(tr_ct['en'].values()))
LEX = {}
for l in ('en', 'fr', 'es', 'de'):
    own = words(list(tr_ui[l].values()) + list(tr_ct[l].values()))
    LEX[l] = it_words - own - en_words
B = re.compile(r"\b(che|della|delle|degli|nella|nelle|sono|più|può|perché|anche|ogni|questo|questa|dei|gli|alla|dalla|quale|quali|è)\b", re.I)
def classify(lang, nodes):
    ui = {k: v for k, v in src_ui.items() if k.startswith('UI_IT.') and len(v) >= 8 and tr_ui[lang].get(k) != v}
    vals = set(ui.values()); long_vals = [v for v in vals if len(v) >= 14]
    res = {'A': [], 'B': [], 'D': []}
    for t in nodes:
        if t in vals or any(v in t for v in long_vals): res['A'].append(t); continue
        if len(B.findall(t)) >= 2: res['B'].append(t); continue
        ws = [w.lower() for w in WORD.findall(t)]
        itw = [w for w in ws if w in LEX[lang]]
        if ws and any(len(w) >= 5 for w in itw) and len(itw) / len(ws) >= 0.5: res['D'].append(t)
    return res
if __name__ == '__main__':
    data = json.load(open(sys.argv[1]))
    out = {}
    for key, v in data.items():
        source, lang, width = key.split('|')
        c = classify(lang, v['unique'])
        out[key] = {'unique_nodes': len(v['unique']), **{k: len(x) for k, x in c.items()}, 'lists': c}
        print(key, 'unique', len(v['unique']), 'A', len(c['A']), 'B', len(c['B']), 'D', len(c['D']))
    json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
