import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); os.chdir(os.environ['D'])
import statistics as S
from pgm_reader_adv251_it_20261125 import rd
w1,h1,X=rd('g1.pgm'); C={'WT':130,'1C':227,'2C':325,'1C_AAV':422,'2C_AAV':526}; HALF=40
def dark(c,r): return [255-X[r][x] for x in range(c-HALF,c+HALF+1)]
bgrows=list(range(37,67))+list(range(119,150))
for n,c in C.items():
    bg=S.median([v for r in bgrows for v in dark(c,r)])
    out=[]
    for a in (105,115,125,135,150,165,178):  # blank-ish 13-row windows below the band
        out.append(round(sum(S.mean(dark(c,r))-bg for r in range(a,a+13)),1))
    print(n,'bg',bg,'blank-window sums (13 rows, same lane)',out)
