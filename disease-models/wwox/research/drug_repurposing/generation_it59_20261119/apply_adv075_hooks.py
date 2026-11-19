"""IT59 / ADV-075 (2026-11-19): SCI's audit G (read-but-not-carried) top four rows CONFIRMED against the held originals by one fresh reader (sonnet; Cheng 2020 PMC XML + supplement; Repudi 2021 operator-supplied text + supplement) and against the
consumers by IT (concept words other than the producer's; newer work folders included). Mapping in dated lines, no tier change. The audit's own statements are corrected where the originals say otherwise. Idempotent."""
import csv
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
B = "advisor_pilot_20261113/brainstorm_20261116/"
G = B + "g_read_not_carried_audit_sci_20261119/G_SPOT_CHECK_AND_SUMMARY_SCI_20261119.md"
Q3 = ["IT59-Q03", G + " ; " + B + "it_q02_origin_20261117/measurements.tsv",
      "Does the heterozygote show a measurable partial deficit (Tc-MEP onset latency 2.13 against 1.39 ms in wild type, null 2.44; amplitude normal; Cheng 2020, 3 weeks, n = 5) that could serve as a carrier readout, and does it replicate?",
      "Whether a heterozygote conduction readout can enter the carrier premise of the pup brief and the myelin cards.",
      "wet_lab_measurement", "OPEN", "main",
      "[IT 2026-11-19, ADV-075, audit G row 1 confirmed against the original and CORRECTED] Cheng 2020 (PMC text, Results 'Nerve degeneration and demyelination', Fig 2): Tc-MEP at 3 weeks, wild type amplitude 59.2 ± 9.0 uV, latency 1.39 ± 0.13 ms (n = 10); heterozygote 59.6 ± 17.2 uV, 2.13 ± 0.22 ms (n = 5; latency P < 0.05 against wild type; paper: 'partial Tc-MEP deteriorative change'); null 11.8 ± 5.4 uV, 2.44 ± 0.37 ms (n = 4); one-way ANOVA generally, no named post hoc test, no heterozygote against null comparison, the legend says SEM. "
      "The audit's statement that the heterozygote latency 'equals the null' is NOT in the source (2.13 against 2.44 ms; the paper calls it partial); its 'amplitude normal' is right. Carried before: the amplitude values only, in the IT56-Q02 origin table (measurements.tsv, a work folder, not a need, card or arm cell); the latency was carried nowhere. Limits: one laboratory, small n, n for the latency panel not given separately, anaesthetised (chloral hydrate), 3 weeks only.",
      "2026-11-19", "Needs a laboratory with heterozygote and null animals and Tc-MEP or an equivalent conduction readout.", "no", ""]
ARM = ("\n\nUpdate 2026-11-19 (IT59, ADV-075: SCI's audit G, top four rows confirmed against the held originals by one fresh reader and against the consumers by IT; " + G + "; the text above is not edited; no tier change). "
       "(1) Heterozygote motor-evoked-potential latency (Cheng 2020, Fig 2, 3 weeks): wild type 1.39 ms, heterozygote 2.13 ms (P < 0.05 against wild type), null 2.44 ms, with a normal heterozygote amplitude (59.6 against 59.2 uV): a PARTIAL latency deficit, NOT 'equal to the null' as the audit worded it; a candidate carrier readout, one laboratory, n = 5 (IT59-Q03). "
       "(2) 'Structure precedes seizure' is narrower than the audit's wording: only the E16.5 cortical thinning (Suppl Fig S5c; no n in the legend) precedes the paper's own seizure age ('commonly observed after postnatal day 12'); DCX high at P14 (n = 5), apoptosis at P20 (TUNEL 0.19 against 0.89 percent, about 4.7-fold by the ratio of the printed values, no n or test in the legend) and vermis lobule fusion at P19 to P20 come after it; the paper does not state a causal sequence and the apoptosis is not 'brain-wide' in its words. "
       "As an arm-cell caveat for acute seizure-drug designs: one embryonic structural finding precedes seizure onset; the other structural findings are concurrent or later. "
       "(3) Peripheral nerve (Cheng 2020, Fig 3): sciatic nerve at P20, N = 3, abnormal fibres, demyelination and onion-bulb degeneration in all null nerves examined; Schwann-cell apoptosis is inferred from cleaved caspase-3 in one representative immunogold image; no quantification, no test; heterozygote 'similar (data not shown)': a qualitative PNS phenotype, relevant to the neuropathy hazard logic of any myelin-directed arm. "
       "(4) The heterozygote spectrum and evoked-response panels of the neuronal deletion (Repudi 2021, Fig 2D, 2F): the S-HT against control comparison is not tested for spectral power and the Fig 2F P values are not assigned to pairs in the legend; the text gives 4 of 23 S-HT slices bursting (17 percent) against 0 of 11 controls and 86 percent of 42 S-KO, the legend 20 and 84 percent, a conflict the paper does not reconcile; the 'behaviourally indistinguishable from control' statement has no data in the text; the brief carries the bursting incidence only. "
       "Audit rows corrected: row 1 (latency 'equals the null': false), row 2 (ages mixed, 'brain-wide' and 'five-fold' are the audit's words); rows 3 and 4 hold with the limits stated. Hypothesis level; no dose.")
csv.field_size_limit(10**9)
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
assert len(Q3[2]) <= 300 and len(Q3[3]) <= 200, (len(Q3[2]), len(Q3[3]))
if Q3[0] not in {r[0] for r in rows}:
    j = [k for k, r in enumerate(rows) if r[0] == "IT59-Q02"][0]; rows.insert(j + 1, Q3)
with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
pa = DR / (B + "ARM_TABLE_V9_NOTES_IT_20261117.md"); s = pa.read_text(encoding="utf-8")
if "(IT59, ADV-075:" not in s: pa.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
print("ok")
