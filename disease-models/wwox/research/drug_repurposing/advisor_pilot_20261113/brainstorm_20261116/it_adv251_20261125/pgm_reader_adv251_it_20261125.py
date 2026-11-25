# Helper for measure_fig1k_adv251_it_20261125.py (reads a binary PGM; run with D=<folder holding g0.pgm and g1.pgm>)
import sys,os
def rd(f):
    b=open(f,'rb').read(); parts=b.split(None,4); w,h=int(parts[1]),int(parts[2]); px=parts[4] if len(parts)>4 else b''
    # P5: header 'P5 w h 255\n' then data
    i=b.index(b'255')+4; px=b[i:]; assert len(px)==w*h,(len(px),w,h); return w,h,[list(px[r*w:(r+1)*w]) for r in range(h)]
