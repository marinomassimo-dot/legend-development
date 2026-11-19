"""IT59 / ADV-079 (2026-11-19): SCI's harm-against-phenotype table mapped in ONE pass, AS CORRECTED (section 4.5 governs: the vigabatrin retina and optic cell is PARTIAL, not YES, by the blind verifier). Dated lines only, readout names only, no dose,
no tier change. (1) the arm-table dated line (per-arm harm readouts, the cells that move, the limits); (2) the ADV-053 comparison note (its section 6 'vigabatrin label not held' and 'P47T Supplementary Table 4 not located' are out of date); (3) the harm cell C-EP6
of the INV-04 package (marker). Idempotent."""
import csv
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
B = "advisor_pilot_20261113/brainstorm_20261116/"
N = B + "harm_against_phenotype_adv079_sci_20261119/HARM_AGAINST_PHENOTYPE_ADV079_SCI_20261119.md"
V = B + "harm_against_phenotype_adv079_sci_20261119/VERIFIER_REPORT_VIGABATRIN_RETINA_OPTIC_AS_DELIVERED.md"
ARM = ("\n\nUpdate 2026-11-19 (IT59, on SCI's ADV-079 harm-against-phenotype table AS CORRECTED, " + N + " sections 1, 4.5 and 5; verifier report " + V + "; the text above is not edited; no tier change; readout names only, no dose): "
       "the stop rule is not met: 13 candidate-phenotype intersections, 5 YES (3 thin) and 8 PARTIAL; every NO is a keyword absence in the text searched, not a safety statement; the ketogenic diet's harm literature is not held (UNKNOWN). "
       "Readouts by arm. Every arm, as a control: liver and kidney histology with the vehicle group of each genotype, body weight, blood glucose with the fed or fasted state recorded. Ethosuximide (stage 2): liver and kidney readouts, a blood count. Lithium (stage 3): serum creatinine and urea, kidney histology, urine output, serum sodium and calcium, thyroid function, glucose and weight series, with the lithium-alone arm kept. "
       "NMDA pore blocker (stage 4, last): bile-duct and gallbladder histology with ALP, GGT and bilirubin, bladder and kidney histology, cleaved caspase-3 or TUNEL in cortex and cerebellum against the null vehicle baseline, a myelin readout. Vigabatrin (not an arm of the pup design): a visual-pathway readout WITH A DRUG-FREE BASELINE (optic atrophy is already reported in 8 of 14 children in four held primary reports, some vigabatrin-exposed), a myelin readout, nerve conduction or histology; ALT and AST are unreliable because the label says the drug lowers them. "
       "Cells that move: vigabatrin retina and optic from 'not held' to PARTIAL (blind verifier: the label describes visual-field constriction and central retinal damage and never names optic atrophy; no held vigabatrin-exposed WWOX child has attributable vision data; first delivered as YES); vigabatrin brain size, myelin and peripheral nerve become YES cells; ethosuximide gains a liver and kidney intersection; pore blockers a thin hepatobiliary one; lithium kidney becomes PARTIAL (the P47T nephropathy). "
       "Limits carried: the kidney and liver relative weights of the P47T homozygotes (29 against 41 g body weight) are not evidence of organ enlargement, so those cells rest on the Supplementary Table 4 histology and the labels; the P47T 'nephropathy typical of ageing' reading is over-credited (an unadjusted excess in both mutant groups, heterozygote above homozygote, no test, wild-type n = 7); the other 12 cells were not blind-verified. Hypothesis level.")
ADV53 = ("\n\nUpdate 2026-11-19 (IT59, on SCI's ADV-079, " + N + " section 3; the text above is not edited): two statements of section 6 are out of date for the repository: the vigabatrin label IS held (DailyMed SPL under files/fulltext/: boxed warning on vision loss, juvenile-rat statement, interaction with ALT and AST, peripheral neuropathy in adults) and the P47T Supplementary Table 4 IS held (files/supplement/PMID36828035/; WT n = 7, P47T/WT and P47T/P47T percentages for neoplasia, cholestasis, focal liver degeneration and nephropathy). "
         "The ketogenic diet's harm literature remains not held.")
CELL = ("[ADV-079 mapping, 2026-11-19, IT, from SCI's note as corrected (" + N + " sections 4.5 and 5), mapped not authored: harm cells that move: vigabatrin retina and optic PARTIAL (blind verifier; first delivered YES), vigabatrin brain size, myelin and peripheral nerve YES, ethosuximide liver and kidney, pore blockers hepatobiliary (thin), lithium kidney PARTIAL; "
        "13 intersections (5 YES, 8 PARTIAL); a NO is a keyword absence, not a safety statement; vigabatrin ALT and AST unreliable (label); a vigabatrin visual readout needs a drug-free baseline (optic atrophy in 8 of 14 children in four held reports).]")
csv.field_size_limit(10**9)
pa = DR / (B + "ARM_TABLE_V9_NOTES_IT_20261117.md"); s = pa.read_text(encoding="utf-8")
if "(IT59, on SCI's ADV-079" not in s: pa.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
pa = DR / (B + "it_adv053_20261118/COMPARISON_BY_ENDPOINT_ADV053_IT_20261118.md"); s = pa.read_text(encoding="utf-8")
if "(IT59, on SCI's ADV-079" not in s: pa.write_text(s.rstrip("\n") + ADV53 + "\n", encoding="utf-8")
p = DR / "comparison_adv066_20261118/inv04_ethosuximide_age_assay/output/comparison.tsv"
rows = list(csv.reader(open(p, encoding="utf-8"), delimiter="\t")); h = rows[0]; i = h.index("documented_action_and_limits")
for r in rows[1:]:
    if r[0] == "C-EP6" and "[ADV-079 mapping" not in r[i]: r[i] = r[i] + " " + CELL
with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok")
