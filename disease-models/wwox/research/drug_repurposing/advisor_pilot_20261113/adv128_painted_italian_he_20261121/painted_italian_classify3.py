import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, 'framework/scripts')
import painted_italian_classify as c0, painted_italian_nb as nbm
TH = 0.1
import re
def prose(t):
    """natural-language-looking node: >= 3 words of >= 2 letters, alpha ratio >= 0.7, no URL"""
    if 'http' in t or '_' in t or len(t) < 12: return False
    ws = re.findall(r'[^\W\d_]{2,}', t)
    return len(ws) >= 3 and sum(ch.isalpha() or ch == ' ' for ch in t) / len(t) >= 0.7
def run(nodes_json, out):
    data = json.load(open(nodes_json)); res = {}; models = {l: nbm.NB(l) for l in ('en', 'fr', 'es', 'de')}
    for key, v in data.items():
        source, lang, width = key.split('|'); nodes = v['unique']
        cl = c0.classify(lang, nodes); done = set(cl['A']) | set(cl['B'])
        N = [t for t in nodes if t not in done and prose(t) and models[lang].llr(t) > TH]
        res[key] = {'unique_nodes': len(nodes), 'A': len(cl['A']), 'B': len(cl['B']), 'N': len(N), 'total': len(cl['A']) + len(cl['B']) + len(N), 'lists': {'A': cl['A'], 'B': cl['B'], 'N': N}}
        print(key, 'unique', len(nodes), 'A', len(cl['A']), 'B', len(cl['B']), 'N', len(N), 'TOTAL', res[key]['total'])
    json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
if __name__ == '__main__': run(*sys.argv[1:3])
