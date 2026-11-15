"""Stdlib check behind the 'not stated' labels (python3 -I absence_check.py PAGES_DIR).
For each read page: count of pH tokens, and for the tool names the pH tokens within 300 characters."""
import re, sys
sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('vq', 'verify_quotes.py')
vq = importlib.util.module_from_spec(spec); spec.loader.exec_module(vq)
d = sys.argv[1]
tools = {'PMC9970648': ['A1899', 'PK-THPP', 'ML365'], 'PMC3077598': ['A1899'], 'PMC12621189': ['ONO-TR-772']}
for pg in ['PMC12621189', 'PMC3077598', 'PMC9970648', 'PMC6725198']:
    t = vq.page_text('%s/%s.html' % (d, pg))
    print(pg, 'len', len(t), 'pH tokens', len(re.findall(r'\bpH', t)))
    for tool in tools.get(pg, []):
        seen = set()
        for m in re.finditer(re.escape(tool), t):
            w = t[max(0, m.start() - 300): m.end() + 300]
            for x in re.findall(r'pH[o ]?\s?\d+\.\d', w):
                seen.add(x.replace(' ', ''))
        print('  tool', tool, 'occurrences', len(re.findall(re.escape(tool), t)), 'pH values within +-300 chars:', sorted(seen))
