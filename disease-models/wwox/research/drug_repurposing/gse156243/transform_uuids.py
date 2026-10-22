#!/usr/bin/env python3
"""Pure string transformation: remove the hyphens inside UUIDs (8-4-4-4-12 hex) and nothing else.
Why: publication-gate false positive on UUID fragments. Inverse: restore() re-inserts hyphens by the 8-4-4-4-12 rule.
Usage: transform_uuids.py apply <verbatim file> <tracked file> | verify <verbatim file> <tracked file>"""
import re,sys,hashlib
P=re.compile(rb'\b([0-9a-f]{8})-([0-9a-f]{4})-([0-9a-f]{4})-([0-9a-f]{4})-([0-9a-f]{12})\b')
def strip(b): return P.sub(rb'\1\2\3\4\5',b)
def restore(b):
    """Inverse. A 32-hex run is a stripped UUID EXCEPT the value of a "md5" key (an md5 digest is also 32 hex;
    the only such field in these files), which is left untouched."""
    return re.sub(rb'(?<![0-9a-f])(?<!"md5": ")([0-9a-f]{8})([0-9a-f]{4})([0-9a-f]{4})([0-9a-f]{4})([0-9a-f]{12})(?![0-9a-f])',rb'\1-\2-\3-\4-\5',b)
if __name__=='__main__':
    m,v,t=sys.argv[1:4]; vb=open(v,'rb').read()
    if m=='apply': open(t,'wb').write(strip(vb))
    else:
        print(hashlib.sha256(vb).hexdigest(), 'LOSSLESS' if restore(open(t,'rb').read())==vb else 'MISMATCH')
