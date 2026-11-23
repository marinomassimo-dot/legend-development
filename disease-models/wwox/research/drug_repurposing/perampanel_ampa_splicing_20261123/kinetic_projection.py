"""Translate the cortical splice-share estimate into conditional peak-normalized charge."""
import csv
from math import expm1
from pathlib import Path
from analyze import write

# Koike et al., J Neurosci 2000, PMID 10704491. Each form represented at the same
# glutamate pulse and holding potential within the original experiment. Plateau is fraction of peak.
KINETICS = {"GluA2Q":((5.89,.068),(1.18,.011)),
            "GluA2Q_plus_R":((6.40,.067),(1.00,.012))}


def charge(duration,tau,plateau):
    return plateau*duration-(1-plateau)*tau*expm1(-duration/tau)


def projected(share, relative_peak, qflip, qflop):
    weight=share*relative_peak/(share*relative_peak+1-share)
    return weight*qflip+(1-weight)*qflop


def main():
    out=Path(__file__).parent/"results"
    with (out/"contrasts.tsv").open() as f:
        row,=[r for r in csv.DictReader(f,delimiter="\t") if r["region"]=="cortex" and r["method"]=="all_cassette"]
    ctrl,ko=[float(row[k]) for k in ("control_flip_share","KO_flip_share")]
    values=[]
    for state,(flip,flop) in KINETICS.items():
        for duration in [5,20,100]:
            qflip,qflop=charge(duration,*flip),charge(duration,*flop)
            for relative_peak in [.25,.5,1,2,4]:
                baseline=projected(ctrl,relative_peak,qflip,qflop)
                case=projected(ko,relative_peak,qflip,qflop)
                values.append([state,duration,relative_peak,qflip,qflop,baseline,case,100*(case/baseline-1)])
    write(out/"kinetic_projection.tsv","recombinant_configuration pulse_ms relative_peak_per_flip_receptor pure_flip_charge pure_flop_charge control_charge KO_charge relative_change_percent",values)


if __name__=="__main__":
    main()
