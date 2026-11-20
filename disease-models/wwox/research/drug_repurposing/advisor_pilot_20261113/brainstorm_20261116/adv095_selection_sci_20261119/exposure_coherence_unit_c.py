#!/usr/bin/env python3
"""ADV-095 unit C: exposure-to-potency arithmetic for the bridge and broad shortlists.

SCI successor, 2026-11-20. Hypothesis level; no dose, no recommendation; not medical advice.

What it does: converts each measured concentration (as printed in a source that was
checked by a blind verifier) to micromolar with a molecular mass computed from the
molecular formula, and divides it by each potency value that the held sheets or
verified abstracts give. It prints the ratio C / potency. It states NO threshold and no
efficacy probability: a ratio is an arithmetic fact about total concentrations, and
every row carries the caveats that change how it may be read (total against free,
adult against juvenile, tissue basis, assay condition).

Usage: python3 exposure_coherence_unit_c.py OUTDIR  (see --help)
Writes OUTDIR/exposure_coherence.tsv and OUTDIR/exposure_coherence.md.
"""
import os
import re
import sys

ATOMIC = {"C": 12.011, "H": 1.008, "N": 14.007, "O": 15.999, "F": 18.998, "Cl": 35.45}


def mass(formula):
    total = 0.0
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        total += ATOMIC[el] * (int(n) if n else 1)
    return total


FORMULA = {
    "ethosuximide": "C7H11NO2",
    "memantine": "C12H21N",
    "ketamine": "C13H16ClNO",
    "retigabine": "C16H18FN3O2",
    "ganaxolone": "C22H36O2",
    "clemastine": "C21H26ClNO",
}

# (agent, label, value, unit, tissue_or_matrix, source, caveat)
# unit: 'ug/g' or 'ng/g' or 'ng/mL' (density 1 g/mL assumed for tissue; stated) or 'nM' or 'uM'
EXPOSURES = [
    ("ethosuximide", "brain total, 72.3 mg/kg i.p., 45 min, adult Swiss mouse", 134.9, "ug/g", "brain",
     "PMID 22315091 Table 3 (verifier 2 V1)",
     "homogenate 1:2 w:v; dilution correction not stated; value may be per g homogenate (factor up to 3 in tissue)"),
    ("ethosuximide", "brain, same, if the printed value is per g of 1:2 homogenate (tissue = 3 x)", 134.9 * 3, "ug/g", "brain",
     "PMID 22315091 Table 3 with the stated 1:2 w:v homogenate",
     "bound of the uncertainty, not a measurement"),
    ("memantine", "brain total Cmax, 10 mg eq./kg s.c., Tmax 1 h, adult male C57Bl/6", 72520, "nM", "brain",
     "PMID 22307216 Table 2 (verifier 2 V2)", "tissue basis of nM not stated; mg eq. undefined (hydrochloride salt)"),
    ("memantine", "plasma total Cmax, same", 7983, "nM", "plasma", "PMID 22307216 Table 2", "total"),
    ("memantine", "brain total Cmax, 1 mg eq./kg s.c.", 5360, "nM", "brain", "PMID 22307216 Table 2", "as above"),
    ("ketamine", "brain total, 10 mg/kg i.p., 1 h, adult male C57BL/6 under chronic restraint stress", 0.23, "uM", "brain",
     "PMID 37853123 Results (verifier 2 V3)", "stress model, not naive; later time point; half-life about 13 min"),
    ("retigabine", "brain total, 5 mg/kg i.p., P7 rat pup, peak 1-2 h", 330, "ng/g", "brain",
     "PMID 26865186 (verifier 2 V5)", "printed ng/mL of tissue; rat pup; time point of the brain value not stated"),
    ("retigabine", "brain total, 15 mg/kg i.p., P7 rat pup", 1296, "ng/g", "brain", "PMID 26865186", "as above; single dose, no apoptosis"),
    ("retigabine", "brain total, 30 mg/kg i.p., P7 rat pup", 2013, "ng/g", "brain", "PMID 26865186", "as above; single dose, no apoptosis"),
    ("retigabine", "brain EC50 for MES protection, adult male CF-1 mouse, oral", 3.58, "uM", "brain",
     "PMID 40806162 Table 1 (verifier 1 B3)", "an effect concentration, not an exposure; mouse range not significant (p 0.12)"),
    ("ganaxolone", "brain total Cmax, 3 mg/kg i.m., Tmax 10 min, adult male NIH Swiss", 1239, "ng/g", "brain",
     "PMID 29453777 Table 1 (verifier 2 V4)", "total; whole brain in 2 mL water; plasma Cmax is the first sample at 120 s"),
    ("clemastine", "plasma total Cmax, 7.5 mg/kg/day oral, steady state, neonatal mouse (about P10)", 44.0, "ng/mL", "plasma",
     "PMID 38942888 (verifier 1 C2)", "plasma only; no brain, CSF or unbound value; 7.5 is not the lowest dose tested"),
    ("gaboxadol", "CNS extracellular peak, 2.5 to 10 mg/kg s.c., adult Wistar rat (low end)", 0.7, "uM", "microdialysate",
     "PMID 17362924 abstract (producer, not verified)", "abstract level; rat; microdialysate is an extracellular, not a total, measure"),
    ("gaboxadol", "CNS extracellular peak, same (high end)", 3.0, "uM", "microdialysate", "PMID 17362924 abstract", "as above"),
]

# (agent, assay label, value in uM, source)
POTENCIES = [
    ("ethosuximide", "persistent T-current IC50, recombinant human Cav3.x", 600.0, "PMID 11641441 abstract (verifier 1 B1)"),
    ("ethosuximide", "CACNA1I IC50, FLIPR (value reported above 5 mM)", 5000.0, "HE batch 1 (ChEMBL, flagged outside typical range)"),
    ("memantine", "IC50 GluN1/2A, -60 mV, HEK293, glutamate-induced (one 2024 document)", 0.84, "HE batch 4"),
    ("memantine", "IC50 GluN1/2A, -40 mV, same document", 28.1, "HE batch 4"),
    ("memantine", "IC50 range with 1 mM Mg2+, -66 mV, GluN2A..2D (low)", 1.61, "ADV-050 held kinetics table (cited by the producer)"),
    ("memantine", "IC50 range with 1 mM Mg2+, -66 mV (high)", 13.4, "ADV-050 held kinetics table"),
    ("ketamine", "IC50 GluN1/2A, -60 mV, HEK293 (one 2024 document)", 0.5, "HE batch 4"),
    ("ketamine", "IC50 GluN1/2A, -40 mV, same document", 53.3, "HE batch 4"),
    ("ketamine", "IC50 range with 1 mM Mg2+ (low)", 1.18, "ADV-050 held kinetics table"),
    ("ketamine", "IC50 range with 1 mM Mg2+ (high)", 5.35, "ADV-050 held kinetics table"),
    ("retigabine", "human Kv7.2/7.3 EC50, lowest across documents (Rb+ efflux)", 0.43, "HE batch 2"),
    ("retigabine", "human Kv7.2/7.3 EC50, highest across documents (fluorescence slope)", 11.2, "HE batch 2"),
    ("ganaxolone", "GABA-A alpha4beta3delta EC50 (CHO, potentiation, one 2015 document)", 0.103, "HE batch 3"),
    ("ganaxolone", "GABA-A alpha1beta2gamma2 EC50 (LTK cells, same document)", 0.266, "HE batch 3"),
    ("clemastine", "OPC differentiation, effective concentrations, lowest (rat OPC)", 0.010, "PMID 24997607 (verifier 1 C1; joint with benztropine)"),
    ("clemastine", "OPC differentiation, most effective concentration", 0.500, "PMID 24997607 (joint with benztropine)"),
    ("clemastine", "muscarinic M1 Ki, [3H]QNB displacement (one 2020 document)", 0.020, "HE batch 6"),
    ("gaboxadol", "GABA-A alpha1beta2gamma2S functional EC50 (FLIPR; no delta row exists in ChEMBL)", 14.0, "HE batch 3"),
    ("gaboxadol", "delta-dependent tonic current evoked at 1 uM THIP (mouse thalamic neurons)", 1.0, "PMID 19302153 abstract (a concentration used, not an EC50)"),
]


def to_uM(value, unit, agent):
    """Concentration in uM. Tissue density is taken as 1 g/mL, so ug/g = mg/L and ng/g = ng/mL.

    ug/g: value (mg/L) / M (g/mol) x 1000 = uM.   ng/g and ng/mL: value (ug/L) / M = uM.
    """
    if unit == "uM":
        return value
    if unit == "nM":
        return value / 1000.0
    m = mass(FORMULA[agent])
    if unit == "ug/g":
        return value * 1000.0 / m
    if unit in ("ng/g", "ng/mL"):
        return value / m
    raise ValueError(unit)


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    rows = []
    for agent, label, val, unit, matrix, src, cav in EXPOSURES:
        c = to_uM(val, unit, agent)
        pots = [p for p in POTENCIES if p[0] == agent]
        if not pots:
            rows.append([agent, label, f"{val:g} {unit}", f"{c:.4g}", "none", "", "", "", src, cav])
            continue
        for _, plabel, pval, psrc in pots:
            rows.append([agent, label, f"{val:g} {unit}", f"{c:.4g}", plabel, f"{pval:g}", f"{c / pval:.3g}", psrc, src, cav])
    header = ["agent", "exposure_as_labelled", "value_as_printed", "conc_uM_computed", "potency_assay", "potency_uM",
              "ratio_C_over_potency", "potency_source", "exposure_source", "caveat"]
    with open(os.path.join(outdir, "exposure_coherence.tsv"), "w", encoding="utf8") as fh:
        fh.write("\t".join(header) + "\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")
    with open(os.path.join(outdir, "exposure_coherence.md"), "w", encoding="utf8") as fh:
        fh.write("# Exposure over potency, arithmetic only (no threshold)\n\n")
        fh.write("Molecular masses from formulas (g/mol): " + ", ".join(f"{a} {mass(f):.2f}" for a, f in FORMULA.items()) + ".\n")
        fh.write("Tissue density taken as 1 g/mL; every concentration is TOTAL unless the label says microdialysate.\n\n")
        fh.write("| " + " | ".join(header[:7]) + " |\n|" + "---|" * 7 + "\n")
        for r in rows:
            fh.write("| " + " | ".join(str(x) for x in r[:7]) + " |\n")
    print(f"wrote {len(rows)} rows to {outdir}")


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Exposure over potency arithmetic for ADV-095 unit C (no threshold, no efficacy claim).")
    ap.add_argument("outdir", help="directory to write exposure_coherence.tsv and .md into")
    main(ap.parse_args().outdir)
