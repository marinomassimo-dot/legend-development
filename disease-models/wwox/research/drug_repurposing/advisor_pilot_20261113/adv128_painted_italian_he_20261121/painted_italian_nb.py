"""Detector N: character-trigram naive Bayes, Italian vs (English + the page language). Trained on the repo's own strings:
Italian = ui_source values + content_source passages with src 'it'; other = ui_<l> values + content_<l> values + content_source passages with src 'en'. Held-out accuracy is printed."""
import sys, json, re, math, collections, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, 'framework/scripts')
import painted_italian_classify as c0
def grams(t):
    t = ' ' + re.sub(r'\s+', ' ', t.lower()) + ' '
    return [t[i:i+3] for i in range(len(t) - 2)]
def train(texts):
    c = collections.Counter()
    for t in texts: c.update(grams(t))
    return c, sum(c.values())
def make(lang, holdout=0.0, seed=1):
    it = [v for v in c0.src_ui.values() if isinstance(v, str) and len(v) >= 12] + [v['text'] for v in c0.src_ct.values() if v.get('src') == 'it' and len(v['text']) >= 12]
    en_auth = [v['text'] for v in c0.src_ct.values() if v.get('src') == 'en' and len(v['text']) >= 12]
    other = [v for v in c0.tr_ui[lang].values() if isinstance(v, str) and len(v) >= 12] + [v for v in c0.tr_ct[lang].values() if isinstance(v, str) and len(v) >= 12] + en_auth
    if lang != 'en': other += [v for v in c0.tr_ui['en'].values() if isinstance(v, str) and len(v) >= 12]
    random.Random(seed).shuffle(it); random.Random(seed).shuffle(other)
    k, m = int(len(it) * holdout), int(len(other) * holdout)
    return it[k:], other[m:], it[:k], other[:m]
class NB:
    def __init__(self, lang, holdout=0.0):
        it, other, self.it_h, self.oth_h = make(lang, holdout)
        self.ci, self.ni = train(it); self.co, self.no = train(other); self.V = len(set(self.ci) | set(self.co)) + 1
    def llr(self, t):
        g = grams(t); s = 0.0
        for x in g:
            s += math.log((self.ci.get(x, 0) + 1) / (self.ni + self.V)) - math.log((self.co.get(x, 0) + 1) / (self.no + self.V))
        return s / max(1, len(g))          # mean per trigram, length independent
if __name__ == '__main__':
    for lang in ('en', 'de', 'fr', 'es'):
        nb = NB(lang, holdout=0.2)
        for th in (0.0, 0.05, 0.1):
            fn = sum(1 for t in nb.it_h if nb.llr(t) <= th); fp = sum(1 for t in nb.oth_h if nb.llr(t) > th)
            print(lang, 'threshold', th, 'held-out Italian missed', fn, '/', len(nb.it_h), '| other flagged', fp, '/', len(nb.oth_h))
