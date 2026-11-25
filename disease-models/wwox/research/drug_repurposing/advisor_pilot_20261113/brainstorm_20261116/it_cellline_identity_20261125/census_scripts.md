# Scripts used for the census and the look-up

## census.py

```python
import re, json, glob, collections, sys
W = '/home/desktop/legend-development/.claude/worktrees/it_22_20261125/disease-models/wwox/'
REG = ['registries/claim_registry_current.md','registries/paper_registry_current.md','registries/literature_tracking_log_current.md','registries/working_model_current.md',
 'research/discovery_ledger_current.md','research/therapeutic_hypotheses_ledger_current.md','research/experiment_ledger_current.md','research/dismissal_ledger_current.md',
 'analysis/wwox_expression_boost_census_20260922.md']
cards = sorted(glob.glob(W+'research/drug_repurposing/cards/*.card.json')+glob.glob(W+'research/drug_repurposing/cards_early/*.card.json'))
NODIG = ['HeLa','Neuro-2a','Neuro2a','N2a','PC12','SH-SY5Y','HEK','HEK293','HEK-293','COS-7','COS7','U2OS','U-2 OS','HepG2','Huh-7','Huh7','Hep3B','Jurkat','Raji','Daudi','Ramos','CHO','NIH3T3','NIH 3T3','3T3-L1','Vero','MCF-7','MCF7','MCF10A','MDA-MB-231','MDA-MB-435','HaCaT','Caco-2','KYSE','SiHa','CaSki','HCT116','HCT-116','SW480','LNCaP','DU145','DU-145','PC-3','PC3','RWPE','U87','U87MG','U-87 MG','U251','T98G','LN229','LN18','SK-N-SH','SK-N-AS','BE(2)-C','IMR-32','IMR90','HT22','HT-22','BV2','BV-2','C2C12','MEF','HMEC','HUVEC','THP-1','K562','HL-60','Kelly','SKOV3','SK-OV-3','OVCAR','HO8910','HO-8910','A2780','ES-2','A549','H1299','H460','Calu','SGC-7901','BGC-823','AGS','MKN','MGC-803','SMMC-7721','BEL-7402','QGY-7703','L-02','LO2','QSG-7701','Hep-2','HEp-2','KB','Chang liver','ECV304','WRL-68','Girardi','Int-407','HEL','FL','WISH','Hs578T','T47D','ZR-75','BT-549','MNNG/HOS','Saos-2','SaOS','MG-63','HOS','143B','ReNcell','NT2','NTERA','LUHMES','SVG','hCMEC','MO3.13','Oli-neu','CG-4','RT4','RSC96','F11','NSC-34','NSC34','Min6','INS-1','GC-1','GC-2','TM3','TM4','KGN','JEG-3','BeWo','HTR-8','Ishikawa','HEC-1','TCA8113','CAL-27','SCC','Tb3.1','CNE-2','CNE2','SUNE','5-8F','6-10B','HNE','C666','KATO','SNU','YCC','NUGC','MIA PaCa-2','PANC-1','BxPC','AsPC','Capan','KYSE30','Eca109','EC9706','TE-1','786-O','ACHN','Caki','T24','5637','UMUC','J82','TCCSUP','H9','H1','WA09','iPSC','HAP1']
SHAPE = re.compile(r'(?<![\w/.-])((?:[A-Z]{1,6}|[A-Z][a-z]{0,3}[A-Z]{0,2})[-‑]?\d{1,5}[A-Za-z]{0,3}(?:[-/]\d{1,4}[A-Za-z]{0,2})?)(?![\w])')
CTX = re.compile(r'cell|line\b|lines\b|cellul|linea|xenograft|fibroblast|carcinoma|glioma|blastoma|knock-?down in|transfect', re.I)
def tokens(text):
    out = collections.Counter()
    for m in SHAPE.finditer(text):
        a, b = m.span(1)
        if CTX.search(text[max(0,a-60):b+60]): out[m.group(1)] += 1
    for n in NODIG:
        c = len(re.findall(r'(?<![\w-])'+re.escape(n)+r'(?![\w])', text))
        if c: out[n] += c
    return out
# route S
S = collections.Counter(); wh = collections.defaultdict(set)
def walk(o, f):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ('cell_type','cellular_context') and isinstance(v, str):
                for t, c in tokens('cell ' + v).items(): S[t] += c; wh[t].add('S:'+f)
            walk(v, f)
    elif isinstance(o, list):
        for v in o: walk(v, f)
for f in cards: walk(json.load(open(f)), f.split('/')[-1].split('_')[0])
FIELD = re.compile(r'^[-*\s]*\*\*(Model/species|Genotype/model|Species|Model type|Genotype/model tag):?\*\*:?(.*)$', re.M)
for r in ('registries/paper_registry_current.md','registries/literature_tracking_log_current.md'):
    for m in FIELD.finditer(open(W+r).read()):
        for t, c in tokens('cell ' + m.group(2)).items(): S[t] += c; wh[t].add('S:'+r.split('/')[-1][:5])
# route T
T = collections.Counter()
for f in [W+r for r in REG] + cards:
    for t, c in tokens(open(f).read()).items(): T[t] += c; wh[t].add('T:'+f.split('/')[-1][:14])
json.dump({'S': S, 'T': T, 'where': {k: sorted(v) for k, v in wh.items()}}, open('/home/desktop/.claude/jobs/9945c156/tmp/cl/raw_tokens.json','w'))
print('S', len(S), 'T', len(T), 'union', len(set(S)|set(T)))
print(' '.join(f'{k}:{v}' for k, v in sorted(T.items())))
```

## ctx.py

```python
import re, glob, sys
W = '/home/desktop/legend-development/.claude/worktrees/it_22_20261125/disease-models/wwox/'
R = ['registries/claim_registry_current.md','registries/paper_registry_current.md','registries/literature_tracking_log_current.md','registries/working_model_current.md','research/discovery_ledger_current.md','research/therapeutic_hypotheses_ledger_current.md','research/experiment_ledger_current.md','research/dismissal_ledger_current.md','analysis/wwox_expression_boost_census_20260922.md']
files = [W+r for r in R] + sorted(glob.glob(W+'research/drug_repurposing/cards/*.card.json')+glob.glob(W+'research/drug_repurposing/cards_early/*.card.json'))
for t in sys.argv[1:]:
    n = 0
    for f in files:
        s = open(f).read()
        for m in re.finditer(r'(?<![\w-])' + re.escape(t) + r'(?![\w])', s):
            line = s.count('\n', 0, m.start()) + 1
            print(f'== {t} | {f.split("/")[-1][:20]}:{line} | ' + s[max(0, m.start()-70):m.end()+50].replace('\n', ' '))
            n += 1
            if n >= 2: break
        if n >= 2: break
```

## curate.py

```python
import json, re
J = '/home/desktop/.claude/jobs/9945c156/tmp/cl/'
raw = json.load(open(J + 'raw_tokens.json'))
import importlib.util, sys
sys.argv=['x']
ns={}
exec(open(J+'ctx.py').read().split('for t in sys.argv[1:]:')[0], ns)
for extra in ['KHOS','K7M2','MC3T3','SW620','SNU-719']:
    c=0; w=set()
    for f in ns['files']:
        n=len(re.findall(r'(?<![\w-])'+re.escape(extra)+r'(?![\w])', open(f).read()))
        if n: c+=n; w.add('T:'+f.split('/')[-1][:14])
    raw['T'][extra]=c; raw['where'][extra]=sorted(set(raw['where'].get(extra,[]))|w)
# Hand decision from context, written before any register look-up. Key = line; value = spellings.
LINES = {
 '5637':['5637'],'A2780':['A2780'],'A549':['A549'],'AC16':['AC16'],'AGS':['AGS'],'BGC-823':['BGC-823'],'BV-2':['BV2'],'C2C12':['C2C12'],'CAL-62':['CAL-62'],'CHO':['CHO'],'CNE2':['CNE2'],
 'COS-7':['COS-7','COS7'],'Calu-3':['Calu-3','Calu'],'DBTRG-05MG':['DBTRG-05MG'],'DU145':['DU145'],'H1299':['H1299'],'HCCLM3':['HCCLM3'],'HCT116':['HCT116'],
 'HEK293 family':['HEK','HEK-293','HEK-293T','HEK293','HEK293A','HEK293H','HEK293T'],'HET-1A':['HET-1A'],'HOS':['HOS'],'KHOS':['KHOS'],'K7M2':['K7M2'],'MC3T3':['MC3T3'],'SW620':['SW620'],'HT22':['HT22'],'HT-29':['HT-29','HT29'],'HaCaT':['HaCaT'],'HeLa':['HeLa'],
 'HepG2':['HepG2'],'Huh7':['Huh7'],'Ishikawa':['Ishikawa'],'Jurkat':['Jurkat'],'L929':['L929'],'LNCaP':['LNCaP'],'MCF-7':['MCF-7','MCF7'],'MCF10A':['MCF-10A','MCF10'],'MDA-MB-231':['MDA-MB-231'],
 'ME180':['ME180'],'MG-63':['MG-63'],'MHCC97H':['MHCC97H'],'MIN6':['MIN6'],'MOLT-4':['MOLT-4','Molt-4','Molt4'],'Mv1Lu':['Mv1Lu'],'NIH3T3':['NIH3T3'],'Neuro2a':['Neuro2a'],'Oli-neu':['Oli-neu'],
 'P493-6':['P493-6'],'PC-3':['PC-3'],'PC12':['PC12'],'PEO1':['PEO1'],'RPE-1':['RPE-1'],'Ramos':['Ramos'],'SCC-15':['SCC-15'],'SCC-9':['SCC-9'],'SGC-7901':['SGC-7901'],'SH-SY5Y':['SH-SY5Y'],'SK-N-SH':['SK-N-SH'],'SKOV3':['SKOV3'],
 'SMMC-7721':['SMMC-7721'],'SNU-719':['SNU-719'],'SW480':['SW480'],'Saos-2':['Saos-2','Saos2'],'SiHa':['SiHa'],'T-24':['T-24'],'T47D':['T47D'],'T98G':['T98G'],'THP-1':['THP-1'],'U2OS':['U2OS'],'U87MG':['U87MG'],'Vero':['Vero'],
 'XG218':['XG218'],'HO-8910':['HO-8910','HO8910'],'WiBR3 (hESC)':['WiBR3'],'H9 (hESC)':['H9'],'HAP1':['HAP1'],'GM08399 (fibroblast)':['GM08399'],'GM18453 (fibroblast)':['GM18453'],
}
used = {s for v in LINES.values() for s in v}
rows = []
for k, v in LINES.items():
    s = sum(raw['S'].get(x, 0) for x in v); t = sum(raw['T'].get(x, 0) for x in v)
    where = sorted({w for x in v for w in raw['where'].get(x, [])})
    rows.append((k, s, t, where))
json.dump({'LINES': LINES}, open(J + 'curated.json', 'w'))
nS = sum(1 for r in rows if r[1]); nT = sum(1 for r in rows if r[2])
print('lines', len(rows), 'route S', nS, 'route T', nT, 'T only', sum(1 for r in rows if r[2] and not r[1]), 'S only', sum(1 for r in rows if r[1] and not r[2]), 'neither', [r[0] for r in rows if not r[1] and not r[2]])
print('S only:', [r[0] for r in rows if r[1] and not r[2]])
with open(J + 'census_lines.tsv', 'w') as f:
    f.write('line\tstructured_field_mentions\ttext_mentions\twhere\n')
    for r in rows: f.write(f'{r[0]}\t{r[1]}\t{r[2]}\t{";".join(r[3])}\n')
```

## lookup.py

```python
import re, json, collections
J = '/home/desktop/.claude/jobs/9945c156/tmp/cl/'
entries = []
cur = None
for line in open(J + '../cellosaurus_dl/cellosaurus.txt', encoding='utf-8'):
    tag, val = line[:2], line[5:].rstrip('\n')
    if tag == 'ID': cur = {'ID': val, 'AC': '', 'SY': [], 'CC': [], 'OX': []}
    elif cur is None: continue
    elif tag == 'AC' and line.startswith('AC   '): cur['AC'] = val
    elif tag == 'SY': cur['SY'] += [x.strip() for x in val.split(';') if x.strip()]
    elif tag == 'CC' and val.startswith('Problematic cell line'): cur['CC'].append(val)
    elif tag == 'OX': cur['OX'].append(val.split('!')[-1].strip())
    elif tag == '//': entries.append(cur); cur = None
norm = lambda s: re.sub(r'[\s\-_./]', '', s).lower()
by_id, by_sy = collections.defaultdict(list), collections.defaultdict(list)
for e in entries:
    by_id[norm(e['ID'])].append(e)
    b = re.sub(r'\s*\[.*\]$', '', e['ID'])
    if b != e['ID']: by_id[norm(b)].append(e)
    for s in e['SY']: by_sy[norm(s)].append(e)
cur_lines = json.load(open(J + 'curated.json'))['LINES']
ALIAS = {'HEK293 family': ['HEK293', 'HEK293T'], 'WiBR3 (hESC)': ['WIBR3'], 'H9 (hESC)': ['WA09'], 'GM08399 (fibroblast)': ['GM08399'], 'GM18453 (fibroblast)': ['GM18453'], 'XG218': ['XG218'], 'MCF10A': ['MCF-10A']}
out = []
for key, spells in cur_lines.items():
    names = ALIAS.get(key, spells)
    hits, how = [], ''
    for n in names:
        hits = by_id.get(norm(n), [])
        how = 'ID'
        if not hits: hits, how = by_sy.get(norm(n), []), 'synonym'
        if hits: break
    out.append((key, how if hits else 'none', [(e['AC'], e['ID'], e['OX'], e['CC']) for e in hits]))
json.dump(out, open(J + 'lookup.json', 'w'))
print('entries', len(entries))
for key, how, hits in out:
    fl = [h for h in hits if h[3]]
    if how == 'none': print('U ', key)
    elif fl:
        for h in fl: print('F ', key, '|', how, f'{len(hits)} hit(s)', h[0], h[1], h[2][0][:20], '|', h[3][0][:230])
    if len(hits) > 1: print('   AMB', key, how, [(h[0], h[1], h[2][0][:12], bool(h[3])) for h in hits][:6])
```

## recall.py

```python
exec(open('lookup.py').read().split("cur_lines = json.load")[0])
exec(open('ctx.py').read().split("for t in sys.argv[1:]:")[0])
import collections
corpus = {f: open(f).read() for f in files}
cur_lines = json.load(open(J + 'curated.json'))['LINES']
have = {norm(s) for v in cur_lines.values() for s in v}
# one pass: every word-like chunk (and adjacent pairs) of the perimeter, indexed by normalised form
idx = collections.defaultdict(list)
tok = re.compile(r'[A-Za-z0-9][A-Za-z0-9\-/.()]*[A-Za-z0-9)]|[A-Za-z0-9]')
for f, s in corpus.items():
    ms = list(tok.finditer(s))
    for i, m in enumerate(ms):
        cands = [(m.group(0), m.start(), m.end())]
        if i + 1 < len(ms) and ms[i+1].start() - m.end() == 1 and s[m.end()] == ' ':
            cands.append((s[m.start():ms[i+1].end()], m.start(), ms[i+1].end()))
        for w, a, b in cands:
            idx[w].append((f, a, b))
flag = [e for e in entries if e['CC']]
found = {}
for e in flag:
    for n in [e['ID']] + e['SY']:
        n2 = re.sub(r'\s*\[.*\]$', '', n)
        if len(n2) < 3 or n2 in found: continue
        if n2 in idx and norm(n2) not in have: found[n2] = (e['AC'], e['ID'], e['CC'][0][:90], idx[n2])
for n, (ac, i, cc, occ) in sorted(found.items()):
    f, a, b = occ[0]; s = corpus[f]
    print(f'{n!r} x{len(occ)} -> {ac} {i} | ' + s[max(0, a-50):b+30].replace('\n', ' '))
```

