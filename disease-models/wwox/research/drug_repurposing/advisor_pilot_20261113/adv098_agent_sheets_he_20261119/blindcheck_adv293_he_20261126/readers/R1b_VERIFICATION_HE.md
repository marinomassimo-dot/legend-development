# Reader 1b (batches 3 and 2): HE verification against the original (ADV-293, 2026-11-26)

Reader: legend-delegate, sonnet, effort high (agent transcript: read back by `session_model_census.py` at the end of the
increment). Report as delivered: the two TSVs in this folder (unit, class, grade, reason); the MUST CHANGE and ADD
details were in the reply and are summarised here only where HE checked them. Reader's own count and HE's confirmed count:

| Batch | units | OK | ADD | MUST CHANGE (reader) | MUST CHANGE (HE confirmed) | UNSETTLED | NOT A CLAIM |
|---|---:|---:|---:|---:|---:|---:|---:|
| 3 | 36 | 15 | 10 | 6 | 6 (5 distinct errors) | 3 | 2 |
| 2 | 59 | 18 | 11 | 1 | 1 | 19 | 10 |

Class T alone: batch 3 21 units (OK 14, ADD 3, MUST CHANGE 4); batch 2 22 units (OK 13, ADD 8, MUST CHANGE 1).
Strict rate = confirmed MUST CHANGE / (OK + ADD + MUST CHANGE): batch 3 6/31 = 19.4 percent (T: 4/21 = 19.0); batch 2
1/30 = 3.3 percent (T: 1/22 = 4.5); the two together 7/61 = 11.5 percent (T: 5/43 = 11.6). ADD is not in the numerator.

## Confirmed
- U3.13 sheet "IC50 31.5 to 160 nM": IC50 rows 31.5, 92, 100, 130, 130 (one flagged duplicate) and one with no value;
  160 nM is a Ki (activities 1739820 and 12614262). Changes a range label. CONFIRMED.
- U3.10 "the only functional human value ... no alpha4beta3delta row exists in ChEMBL": two human assay-type-F rows exist
  (activities 1925499, 1925516, GABA-rho1 antagonist FMP assay, Ki 100000 nM); the sheet lists them in its own line 20.
  The "no row" part is true only for the retrieved types (IC50, Ki, Kd, EC50): the scope was missing. CONFIRMED (the
  word "only" without its GABA-A scope).
- U3.16 "symbols for the multi-subunit rows list every GABA-A alpha subunit": rows 1183519 and 25107072 carry
  GABRA1,GABRB2,GABRG2; 25107074 carries GABRA2,GABRB1,GABRG2; only 15244127 and 15244891 (266 and 103 nM) list the
  six alpha and the beta symbols, and neither lists GABRG2 or GABRD. CONFIRMED; no comparison changes.
- U3.17 "the one entry counted apart from the human subunit rows is the rat GABA-A binding row": rows apart from the five
  human subunit EC50 rows are 1183517 (80 nM, rat), 15244147 (42 nM, Sprague-Dawley cortical membranes) and 26123569
  (Ki 790 nM, unspecified origin): three rows, two (target, organism) pairs. CONFIRMED; the 2026-11-25 count of HE (3c)
  was itself wrong.
- U3.33 and U3.35 "free brain exposure" not found for gaboxadol: PMID 17362924 (cited in the same sheet, line 22, "abstract
  not read") reports plasma and CNS concentrations by dynamic-no-net-flux and ultraslow microdialysis after sc dosing,
  peak CNS 0.7 to 3 microM at 2.5 to 10 mg/kg, half-life 28 min. Microdialysis gives an extracellular concentration;
  the abstract does not use the word free and does not give an age. CONFIRMED as a method-based reading; one fact in two
  sentences, counted as two units and one error.
- U2.5 ezogabine 0.43 microM "86Rb+ efflux": activity 5299044 assay text is "atomic absorption Rb'+ efflux assay"; the
  ICA-069673 row 10937909 is "86Rb+ efflux ... liquid scintillation counting". The sheet's own line 6 says "atomic
  absorption". CONFIRMED.

## Borderline, not counted
- U3.26 "5 on neither GABA-A nor GABA-rho": row 927988 (CA1 population spike, target an organism-level entry, not GABA-A)
  gives 6 by ChEMBL target and 5 only if the CA1 row is read as a GABA-A readout; the reader graded it ADD. Left as graded.

## Reader limits
No search, no WebFetch, nothing outside the packet. Forty-three of 95 units were class T (held ChEMBL rows); 22 of 95 were
UNSETTLED (3 in batch 3, 19 in batch 2), mostly search counts, negatives and texts not in the packet. A reader cannot be
blind to its own omissions: the OK grades were not re-verified by HE except the arithmetic checks below.
Spot checks of OK units by HE: U3.7 266/200 = 1.33; U3.14 8 rows; U3.15 values; U3.36 14000/266 to 14000/100 = 52.6 to 140.
