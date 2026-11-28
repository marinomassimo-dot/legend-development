import sys,struct,collections
d=open(sys.argv[1],'rb').read()
assert d[:8]==bytes.fromhex('d0cf11e0a1b11ae1'),'not OLE'
ss=1<<struct.unpack_from('<H',d,30)[0]
sec=lambda i: d[(i+1)*ss:(i+2)*ss]
difat=[x for x in struct.unpack_from('<109I',d,76) if x<0xfffffffa]
fat=[]
for s in difat: fat+=struct.unpack('<%dI'%(ss//4),sec(s))
def chain(s):
    out=b''; n=0
    while s<0xfffffffa and n<100000: out+=sec(s); s=fat[s]; n+=1
    return out
dirs=chain(struct.unpack_from('<I',d,48)[0])
for o in range(0,len(dirs),128):
    name=dirs[o:o+64].decode('utf-16le','ignore').split('\0')[0]
    if name in('Workbook','Book'):
        start,size=struct.unpack_from('<II',dirs,o+116); wb=chain(start)[:size]; break
def rk(v):
    n=float(v>>2) if v&2 else struct.unpack('<d',struct.pack('<Q',(v&0xfffffffc)<<32))[0]
    return n/100 if v&1 else n
p=0; sheet=-1; cells=collections.defaultdict(dict); names=[]; sst=[]
while p+4<=len(wb):
    t,l=struct.unpack_from('<HH',wb,p); b=wb[p+4:p+4+l]; p+=4+l
    if t==0x809 and struct.unpack_from('<H',b,2)[0]==0x10: sheet+=1
    elif t==0x85: names.append(b[8:8+b[6]*(2 if b[7]&1 else 1)].decode('utf-16le' if b[7]&1 else 'latin1'))
    elif t==0xfc:
        n=struct.unpack_from('<I',b,4)[0]; q=8
        for _ in range(n):
            if q+3>len(b): break
            c=struct.unpack_from('<H',b,q)[0]; f=b[q+2]; q+=3
            rich=struct.unpack_from('<H',b,q)[0] if f&8 else 0; q+=2 if f&8 else 0
            ext=struct.unpack_from('<I',b,q)[0] if f&4 else 0; q+=4 if f&4 else 0
            w=c*(2 if f&1 else 1); sst.append(b[q:q+w].decode('utf-16le' if f&1 else 'latin1','ignore')); q+=w+4*rich+ext
    elif t in(0x203,0x27e,0xfd,0x6):
        r,c=struct.unpack_from('<HH',b,0)
        if t==0x203: v=struct.unpack_from('<d',b,6)[0]
        elif t==0x27e: v=rk(struct.unpack_from('<I',b,6)[0])
        elif t==0xfd: i=struct.unpack_from('<I',b,6)[0]; v=sst[i] if i<len(sst) else '?'
        else: v=struct.unpack_from('<d',b,6)[0]
        cells[(sheet,r)][c]=v
    elif t==0xbd:
        r,c=struct.unpack_from('<HH',b,0)
        for k in range((l-6)//6): cells[(sheet,r)][c+k]=rk(struct.unpack_from('<I',b,4+6*k+2)[0])
print('sheets',names)
for (s,r) in sorted(cells):
    row=cells[(s,r)]
    print(s,r+1,' '.join(f'{chr(65+c) if c<26 else c}={v:.4g}' if isinstance(v,float) else f'{chr(65+c) if c<26 else c}={v}' for c,v in sorted(row.items()))[:260])
