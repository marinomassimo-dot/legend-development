import re, sys, glob, os, json
ROOT='/home/desktop/legend-development/.claude/worktrees/he_z_20261126'
D=ROOT+'/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/adv098_agent_sheets_he_20261119'
OUT=os.path.join(os.environ['CLAUDE_JOB_DIR'],'tmp/adv293/packets')
MARK=re.compile(r'\s*\(corrected 2026-11-25, HE(?:[^()]|\([^()]*\))*\)')
SPLIT=re.compile(r'(?<=[.!?])(?<!e\.g\.)(?<!i\.e\.)(?<!et al\.)(?<!vs\.)\s+(?=[A-Z\*\[\("0-9])|(?<=\.\*\*)\s+')
SKIP=re.compile(r'^(No (patient )?dose (is )?given( here)?\.?|Not medical advice\.?|\*\*Written for.*)$')
for n in (1,2,3,4,5,10,11,12):
    f=glob.glob(D+f'/BATCH{n}_*.md')[0]
    text=open(f).read()
    text=re.split(r'\n## Dated line 2026-11-25: row-by-row re-check',text)[0]
    leftover=text.count('2026-11-25')
    text=MARK.sub('',text)
    text=re.sub(r';\s*corrected 2026-11-25, HE; see the dated line at the end','',text)
    leftover=text.count('2026-11-25')
    units=[];head='';para_first=True
    for i,line in enumerate(text.split('\n'),1):
        s=line.strip()
        if not s: continue
        if s.startswith('#'): head=s.lstrip('# '); continue
        if s.startswith('Written for:'): continue
        if s.startswith('|'):
            if set(s)<=set('|-: ') : continue
            units.append((i,head,s)); continue
        s=re.sub(r'^([-*]|\d+\.)\s+','',s)
        for part in SPLIT.split(s):
            part=part.strip()
            if len(part)<15 or SKIP.match(part): continue
            units.append((i,head,part))
    os.makedirs(f'{OUT}/batch{n}',exist_ok=True)
    with open(f'{OUT}/batch{n}/units.md','w') as o:
        o.write(f'# Sheet batch {n}: {os.path.basename(f)}\nEach numbered unit is a sentence of the repository sheet, in order. L = line in the sheet.\n\n')
        h=None
        for k,(ln,hd,u) in enumerate(units,1):
            if hd!=h: o.write(f'\n## {hd}\n'); h=hd
            o.write(f'U{n}.{k} (L{ln}) {u}\n')
    pm=sorted(set(re.findall(r'\b\d{7,8}\b',text)))
    json.dump({'file':f,'units':len(units),'numbers7_8':pm},open(f'{OUT}/batch{n}/meta.json','w'))
    print(n,len(units),'leftover25=',text.count('2026-11-25'), 'chars', sum(len(u) for _,_,u in units))
