"""Exploratory equal-exposure waveform perturbations after the short-pulse result."""
from itertools import product
from kinetic import charge

print("width_ms\tpulse_glu_uM\tbaseline_glu_uM\tCa_uM\tcluster_block_pct\teven_block_pct\texcess_pp")
for width, pulse, baseline, calcium in product((.002,.01,.025,.05,.1),(10.,100.,1000.),(0.,.25,1.),(.1,10.)):
    blocks=[]
    for even in (False,True):
        q0=charge(26.2,.66,5,0.,calcium,even,width,pulse,baseline)[1]
        q=charge(26.2,.66,5,.36,calcium,even,width,pulse,baseline)[1]
        blocks.append(100*(1-q/q0))
    print(width*1000,pulse,baseline,calcium,*[f"{v:.5f}" for v in [*blocks,blocks[0]-blocks[1]]],sep="\t")
