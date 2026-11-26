#!/usr/bin/env python3
"""ADV-296 read-only scan: negative sentences beside a citation the file says it read by title only.
Usage: scan_negative_beside_unread.py OUT.tsv   (reads git blobs at BASE for sheets, working tree for cards)
Method frozen in PREREG_ADV296_HE_20261126.md."""
import re, subprocess, sys, glob, json
BASE = '75981649b'
SHEETS = 'disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/adv098_agent_sheets_he_20261119'
CARDS = 'disease-models/wwox/research/drug_repurposing/cards'
UNREAD = re.compile(r'title read|titles read|title only|abstract not read|not read|title truncated', re.I)
NEG = re.compile(r'not found|none found|\bno\b[^.;]{0,60}\bfound\b|not measured|\bno\b[^.;]{0,40}\bfigure\b|not confirmed|by these routes', re.I)
PMID = re.compile(r'PMIDs?\s*:?\s*(\d{5,8})|\bPMID\b[^)]{0,10}?(\d{5,8})', re.I)
STOP = set('the and for with from that this which were was are not but its their been have has into than then also only one two three more most other such very'.split())
GENERIC = set('found routes read title titles abstract abstracts these none measured confirmed figure record records search query returned pubmed'.split())
V2 = len(sys.argv) > 2 and sys.argv[2] == 'v2'
CLASSES = {
 'exposure': set('exposure concentration concentrations plasma serum csf brain cns pharmacokinetic pharmacokinetics microdialysis penetration penetrates distribution levels level'.split()),
 'safety': set('harm safety adverse toxicity tolerability signal signals sedation'.split()),
 'potency': set('potency ic50 ki affinity selectivity value values'.split()),
 'efficacy': set('efficacy seizure seizures anticonvulsant survival outcome'.split()),
}
def topic_shared(a, b):
    wa = set(re.findall(r'[a-z0-9\-]+', a.lower())); wb = set(re.findall(r'[a-z0-9\-]+', b.lower()))
    return {'class:' + k for k, v in CLASSES.items() if (wa & v) and (wb & v)}
def words(s):
    return {w for w in re.findall(r'[a-z0-9\-]{4,}', s.lower()) if w not in STOP and w not in GENERIC}
def sentences(text):
    out = []
    for i, line in enumerate(text.split('\n')):
        for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(*\[])', line):
            if s.strip(): out.append((i + 1, s.strip()))
    return out
def scan(name, text, window_lines, window_sent=None):
    sents = sentences(text)
    unread = []
    for idx, (ln, s) in enumerate(sents):
        m = PMID.search(s)
        if m and UNREAD.search(s):
            unread.append((idx, ln, s, m.group(1) or m.group(2)))
    flags = []
    for idx, (ln, s) in enumerate(sents):
        if not NEG.search(s): continue
        sw = words(s)
        linked = []
        for uidx, uln, us, pm in unread:
            if uidx == idx: continue
            near = abs(ln - uln) <= window_lines if window_sent is None else abs(idx - uidx) <= window_sent
            if not near: continue
            shared = sw & words(us)
            cls = topic_shared(s, us) if V2 else set()
            if len(shared) >= 2 or cls:
                linked.append((pm, ','.join(sorted(shared | cls))))
        if linked:
            flags.append((name, ln, ';'.join(sorted({p for p, _ in linked})), s[:300], '', ';'.join(sorted({w for _, w in linked}))))
    return flags
def blob(path):
    return subprocess.run(['git', 'show', f'{BASE}:{path}'], capture_output=True, text=True).stdout
def main(out):
    rows = []
    files = subprocess.run(['git', 'ls-tree', '--name-only', BASE, SHEETS + '/'], capture_output=True, text=True).stdout.split()
    for p in files:
        if re.search(r'/BATCH\d+_.*\.md$', p):
            rows += scan(p.split('/')[-1], blob(p), 8)
    for p in sorted(glob.glob(CARDS + '/*.card.json') + glob.glob(CARDS + '/*.packet.json')):
        try: d = json.load(open(p))
        except Exception: continue
        strings = []
        def walk(o):
            if isinstance(o, str): strings.append(o)
            elif isinstance(o, dict):
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
        walk(d)
        rows += scan(p.split('/')[-1], '\n'.join(strings), 3, None)
    with open(out, 'w') as f:
        f.write('file\tline\tunread_pmid\tnegative_sentence\tunread_sentence\tshared_words\n')
        for r in rows: f.write('\t'.join(str(x).replace('\t', ' ') for x in r) + '\n')
    print(len(rows), 'flagged')
main(sys.argv[1])
