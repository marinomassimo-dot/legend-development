#!/usr/bin/env python3
"""ADV-281 STEP 0 screening: one decision per row found by route S or T (card text only; no source opened). Consumers = tracked files naming the id."""
import csv, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NULL = {
 # drug assertions
 "DR-A01-003": "PBA class did not rescue G443D", "DR-A01-004": "no rescue in null alleles", "DR-A01-007": "comparator HDAC inhibitor about 1.05 fold, unmarked",
 "DR-A02-002": "lysosome-inhibitor arm did nothing", "DR-A02-006": "neither inhibitor restored Tg-T191M activity", "DR-A02-007": "activity gain not significant at tolerated exposure",
 "DR-A02-009": "I278T activity did not rise", "DR-A02-010": "no significant change at tolerated exposure", "DR-AAV-GLU10-HD": "not significant against untreated knockout",
 "DR-AAV-GLU10-LD": "not significant against untreated knockout", "DR-B01-002": "no phenotypic rescue", "DR-D01-002": "no recovery of deep-layer markers",
 "DR-E01-002": "trial: no benefit", "DR-E01-003": "amyloid burden not reduced", "DR-E03-001": "enzyme assay: no half-maximal inhibition (phrase match was incidental)",
 "DR-H01-003": "no effect on focal seizures", "DR-H02-005": "pattern not observed in older children and adults", "DR-H02-008": "spasm cessation and behaviour not altered",
 "DR-H02-019": "diffusion coefficient unchanged", "DR-H02-023": "no vacuolation or demyelination found", "DR-H02-024": "no oedema and no primary demyelination seen",
 "DR-H02-030": "no significant difference in older bands", "DR-H02-036": "GABA-A agonist did not reproduce the effect", "DR-I01-001": "phospho-site did not move significantly",
 "DR-I01-002": "no effect on seizure endpoint", "DR-I01-004": "structured null (dichloroacetate, mouse)", "DR-I01-006": "clinical endpoints did not change",
 "DR-I01-014": "no significant effect in control cells", "DR-K01-006": "no acute effect", "DR-L01-001": "Tnf not changed", "DR-L01-003": "cytokine mRNA differences not significant",
 "DR-M01-001": "deep-layer marker unchanged", "DR-P11-004": "no difference in seizure control and development", "DR-P11-006": "CSF magnesium did not change",
 "DR-P9-009": "structured null (adult safety signal)", "DR-P9-010": "label: controlled paediatric null", "DR-W2-002": "variant-level sustained effect not significant",
 "DR-W2-003": "seizure reduction not different", "DR-W2-004": "did not prevent seizures", "DR-W2-007": "no sustained positive effect",
 # disease assertions (genetic or delivery manipulation)
 "DA-GSE-PDK-003": "knockout organoid transcripts not different", "DA-I01-001": "PDK1 inside the single-gene null", "DA-I01-002": "no decrease demonstrated",
 "DA-I01-004": "PDH activity unchanged", "DA-I01-006": "oligodendrocyte and weak ubiquitous promoters did not rescue glucose", "DA-J01-002": "Tnf-a not significant",
 "DA-J01-006": "astrocyte-specific deletion: no abnormality", "DA-J01-007": "reactive genes not separated", "DA-J01-008": "heterozygote: no gliosis (data not shown)",
 "DA-K01-002": "HIF1A mRNA and several glycolytic genes flat", "DA-K01-005": "no significant difference in two conditions", "DA-K01-006": "no difference in nuclear fraction",
 "DA-K01-007": "no elevation in four contrasts", "DA-K01-008": "reporter: no change", "DA-L01-001": "Tnf-a non-significant", "DA-L01-003": "no coherent NRF2 signature",
 "DA-L01-005": "no difference in early passage", "DA-LC-ATF4-002": "not significant without amyloid", "DA-M01-002": "neuron-cluster fraction not reduced",
 "DA-M01-007": "oligodendrocyte and astrocyte deletion do not reproduce", "DA-W2-002": "frequency and decay not different", "DA-W2-011": "oligodendrocyte-promoter vector gave no detectable WWOX",
 "DA-W2-012": "several oligodendroglial transcripts not higher",
}
EQUIV = ["DR-AAV-GFAP-P5HD", "DR-AAV-GFAPAREA-HD", "DR-AAV-GLU20-HD", "DR-AAV-MOTOR-HD", "DR-C01-001", "DR-D01-001"]
OTHER = {
 "DA-H01-001": "'null' names the genotype", "DA-I01-003": "'null' names the statistic of another datum", "DA-I01-007": "cites another row's null", "DA-K01-009": "'not a null' names the allele",
 "DA-LI-PTZ-001": "'null' names the genotype", "DA-M01-008": "'null' names the background", "DR-A01-009": "compared with the wild-type range", "DR-A01-010": "target statement, not a result",
 "DR-A02-005": "correlation, not a readout under a manipulation", "DR-AAV-SURV-LD": "positive effect (postponement)", "DR-E02-006": "phenocopy statement, no null result",
 "DR-H01-004": "identity statement", "DR-I01-007": "restates DR-I01-006", "DR-I01-008": "description of another cohort's changes", "DR-I01-013": "group comparison; the drug had an effect",
 "DR-K01-004": "'null' names a control genotype", "DR-LI-001": "'null' names the genotype", "DR-M01-005": "'null' names the genotype", "DR-M01-009": "'null' names the cell background",
}
NOMANIP = {"DA-J01-003": "age, not an applied manipulation", "DA-Q230P-001": "patient line against reference lines", "DR-H02-013": "association with age at exposure",
           "DR-H02-015": "predisposition in an observed cohort", "DR-H02-018": "comparison within exposed children"}


def main():
    csv.field_size_limit(10**8)
    rows = list(csv.DictReader((HERE / "route_hits_adv281.tsv").open(), delimiter="\t", quoting=csv.QUOTE_NONE))
    skip = ("/view/", "/join/", "/cards/", "checkpoint_sci", "adv281_null_note", "typed_assertions", "assertion_pertinence", "assignments/ADV-281")
    out, counts = [], {}
    for r in rows:
        i = r["id"]
        if i in NULL:
            d, why = "NULL", NULL[i]
        elif i in EQUIV:
            d, why = "X-OTHER", "non-difference from wild type read as restoration (equivalence class, reported apart)"
        elif i in OTHER:
            d, why = "X-OTHER", OTHER[i]
        elif i in NOMANIP:
            d, why = "X-NOMANIP", NOMANIP[i]
        else:
            d, why = "X-EVIDENCE", "phrase is about what was read, measured or can be concluded"
        files = subprocess.run(["git", "grep", "-l", "-F", "-w", i], capture_output=True, text=True).stdout.split()
        cons = [f for f in files if not any(s in f for s in skip)]
        counts[d] = counts.get(d, 0) + 1
        out.append([i, d, why, r["route_S"], r["route_T"], r["in_ten"], str(len(cons)), r["source"][:120], r["receipt"], ";".join(Path(f).name for f in cons)])
    with (HERE / "screen_adv281.tsv").open("w") as fh:
        fh.write("id\tdecision\treason\troute_S\troute_T\tin_ten\tn_consumer_files\tsource\treceipt\tconsumer_files\n")
        for row in out:
            fh.write("\t".join(row) + "\n")
    assert not (set(NULL) | set(EQUIV) | set(OTHER) | set(NOMANIP)) - {r["id"] for r in rows}
    print(counts, "NULL: S&T", sum(1 for x in out if x[1] == "NULL" and x[3] == x[4] == "Y"), "S only", sum(1 for x in out if x[1] == "NULL" and x[3] == "Y" and x[4] == "N"),
          "T only", sum(1 for x in out if x[1] == "NULL" and x[3] == "N"))
    print("ten:", [(x[0], x[1]) for x in out if x[5] == "Y"])
    adds = sorted((x for x in out if x[1] == "NULL" and x[5] == "N"), key=lambda x: (-int(x[6]), x[0]))
    for x in adds[:14]:
        print("ADD", x[0], x[6], x[7][:70], x[8])
    for x in out:
        if x[5] == "Y":
            print("TEN", x[0], x[1], x[6], x[7][:70], x[8])


if __name__ == "__main__":
    sys.exit(main())
