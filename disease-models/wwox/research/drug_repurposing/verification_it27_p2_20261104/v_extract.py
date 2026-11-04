"""Verifier stage 1: extract ion chromatograms (EIC) from negative-mode mzXML.
Usage: python3 -I v_extract.py <dir_with_mzXML> <out_npz_dir>
Independent of the producer's code. Targets are [M-H]- exact masses computed from formulas.
Writes one npz per file: rt (s), and for each target the summed intensity inside +/-5 ppm and +/-10 ppm,
plus intensity-weighted mean m/z error (ppm) per scan-aggregate, and TIC (sum of all MS1 intensities)."""
import sys, os, base64, zlib, struct, hashlib
import numpy as np
import xml.etree.ElementTree as ET
E=0.00054858
M={'S':31.97207117,'C':12.0,'H':1.00782503,'O':15.99491462,'N':14.0030740}
def mass(f):  # f dict
    return sum(M[k]*v for k,v in f.items())
def mh(f):
    d=dict(f); d['H']-=1
    return mass(d)+E   # [M-H]-
TARGETS={
 'lactate':mh({'C':3,'H':6,'O':3}),
 'hydroxyglutarate':mh({'C':5,'H':8,'O':5}),
 'citrate':mh({'C':6,'H':8,'O':7}),
 'itaconate':mh({'C':5,'H':6,'O':4}),
 'lysine':mh({'C':6,'H':14,'N':2,'O':2}),
 'glucuronate':mh({'C':6,'H':10,'O':7}),
 'orotate':mh({'C':5,'H':4,'N':2,'O':4}),
 'glutamate':mh({'C':5,'H':9,'N':1,'O':4}),
 'pyruvate':mh({'C':3,'H':4,'O':3}),
 # reference panel for a non-TIC normalisation (not chosen for being stable; fixed before looking at areas)
 'leucine':mh({'C':6,'H':13,'N':1,'O':2}),
 'methionine':mh({'C':5,'H':11,'N':1,'O':2,'S':1}),
 'aspartate':mh({'C':4,'H':7,'N':1,'O':4}),
 'phenylalanine':mh({'C':9,'H':11,'N':1,'O':2}),
 'tryptophan':mh({'C':11,'H':12,'N':2,'O':2}),
}
def read(fn):
    rts=[];arrs=[]
    for ev,el in ET.iterparse(fn,events=('end',)):
        tag=el.tag.split('}')[-1]
        if tag=='scan':
            if el.get('msLevel')=='1':
                rt=float(el.get('retentionTime').strip('PTS'))
                pk=None
                for c in el:
                    if c.tag.split('}')[-1]=='peaks':
                        pk=c; break
                if pk is not None and pk.text:
                    raw=base64.b64decode(pk.text)
                    if pk.get('compressionType','none')=='zlib': raw=zlib.decompress(raw)
                    dt='>f8' if pk.get('precision','32')=='64' else '>f4'
                    a=np.frombuffer(raw,dtype=dt).astype(np.float64).reshape(-1,2)
                else: a=np.zeros((0,2))
                rts.append(rt);arrs.append(a)
            el.clear()
    return np.array(rts),arrs
def main(d,out):
    os.makedirs(out,exist_ok=True)
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.mzXML'): continue
        rt,arrs=read(os.path.join(d,fn))
        res={'rt':rt,'tic':np.array([a[:,1].sum() for a in arrs])}
        for k,t in TARGETS.items():
            for ppm in (5,10):
                e=np.zeros(len(rt))
                for i,a in enumerate(arrs):
                    m=np.abs(a[:,0]-t)<=t*ppm*1e-6
                    e[i]=a[m,1].sum()
                res[f'{k}_{ppm}']=e
            # mass error: intensity-weighted over +/-10ppm scans
            num=0.0;den=0.0
            for a in arrs:
                m=np.abs(a[:,0]-t)<=t*10e-6
                num+=((a[m,0]-t)/t*1e6*a[m,1]).sum();den+=a[m,1].sum()
            res[f'{k}_ppmerr']=np.array([num/den if den>0 else np.nan])
        np.savez(os.path.join(out,fn.replace('.mzXML','.npz')),**res)
        print(fn,len(rt),float(rt.min()),float(rt.max()),flush=True)
if __name__=='__main__':
    main(sys.argv[1],sys.argv[2])
