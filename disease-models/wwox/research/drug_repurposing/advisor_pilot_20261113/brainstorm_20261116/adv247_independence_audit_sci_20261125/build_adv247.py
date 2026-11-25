"""ADV-247: attach to each ADV-239 inference the replicate unit, effective n and independence disposition.
Unit statements are hand-read per deposit (sources in the result); this script only joins and counts them.

Usage: python3 build_adv247.py <ranked_inferences_adv239.tsv> <out.tsv>
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, csv

ORG = ("CULT: organoids of one CRISPR clone v organoids of the parental line",
       "1 clone v 1 line", "non-independent (effective n 1 v 1)",
       "genotype contrast rests on one clone and one line")
P47T = ("ORG: one mouse per library; the four regions come from the same mice",
        "5 v 5 per region (cerebellum 4 v 3)", "independent",
        "agreement across regions is within the same animals, not replication")
CTX = ("ORG: one mouse cortex per library", "4 v 3", "independent", "litter not stated")
HPC_PART = ("hippocampal libraries: one mouse per library is not said in words (n given per genotype); whether the "
            "same mice gave the cortices is not stated")
UNIT = {"O": ORG, "T": P47T,
        "M3": CTX,
        "M1": ("NS: hippocampal libraries", "as stated 2 v 3; not confirmed as animals", "not stated", HPC_PART),
        "M4": ("NS: hippocampal libraries", "arms of 2 or 3 as stated; not confirmed as animals", "not stated", HPC_PART),
        "M2": ("ORG (cortex) and NS (hippocampus)", "cortex 4 v 3; hippocampal arms as stated", "not stated", HPC_PART),
        "M5": ("ORG (cortex) and NS (hippocampus)", "cortex 4 v 3; hippocampal arms as stated", "not stated", HPC_PART),
        "M6": ("ORG (cortex) and NS (hippocampus)", "cortex 4 v 3; hippocampal arms as stated", "not stated", HPC_PART),
        "M7": ("ORG (cortex) and NS (hippocampus)", "cortex 4 v 3; hippocampal arms as stated", "not stated", HPC_PART),
        "C1": ("CULT: one transduced population of one hESC-derived progenitor line per arm", "1 v 1", "independent",
               "the two stages come from the same two populations; control is scrambled shRNA in the paper, labelled wild type in GEO"),
        "S1": ("POOL or dataset: one matrix per genotype; nuclei are not replicates", "1 v 1 as analysed", "independent",
               "animals per genotype not stated; four GEO records per genotype, three readings on record (IT14 identity table row 15)"),
        "H2": ("ORG: one mouse hippocampus per sample (qRT-PCR)", "4 v 4", "independent",
               "technical triplicates are not counted; one article"),
        "H1": ("NS (neurosphere RNA-seq); ORG-like for qRT-PCR (hippocampi)", "RNA-seq 2 v 3 not confirmed as animals; qRT-PCR 4 v 4",
               "not stated", "whether each neurosphere library is a separate pup is not stated")}
rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
count = collections.Counter()
cons = collections.defaultdict(list)
with open(sys.argv[2], "w") as o:
    o.write("rank\tid\tn_consumers\tdeposit\tstated_n\treplicate_unit\teffective_n\tdisposition\tflag\tstatement\tconsumers\n")
    for r in rows:
        u = UNIT.get(r["id"]) or UNIT[r["id"][0]]
        d = u[2].split(" (")[0]
        count[d] += 1
        cons[d].append(int(r["n_consumers"]))
        o.write("\t".join([r["rank"], r["id"], r["n_consumers"], r["deposit"], r["n_mutant_v_control"], u[0], u[1], u[2], u[3],
                           r["statement"], r["consumers"]]) + "\n")
print(len(rows), "inferences")
for d in count:
    print(d, count[d], "share %.2f" % (count[d] / len(rows)), "consumer links", sum(cons[d]))
top = [UNIT.get(r["id"]) or UNIT[r["id"][0]] for r in rows[:12]]
print("top 12:", dict(collections.Counter(t[2].split(" (")[0] for t in top)))
