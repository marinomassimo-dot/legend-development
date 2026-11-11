# SCI45 follow-up N1 — consumer delta (proposals only)

| # | Consumer | Change proposed | Source rows |
|---|---|---|---|
| 1 | `glun2b_comparators_sci42_20261110/S3_design.md` §4 item A4 and its consumer rows (NP10679 and ifenprodil/Ro 25-6981 at two pH) | Record that GluN2B-containing receptors are themselves proton-inhibited (pH IC50 7.3-7.6, 44-65 percent at pH 7.4, a further 21-36 percent for 7.4 to 7.2, oocytes, Mg-free): a pH change moves the NMDAR current irrespective of drug, so vehicle and d-APV at each pH are required (already in A4) and an apparent drug-by-pH interaction must be read against that baseline | `output/proton_sensitivity.tsv` PS07, V7-2, V7-3 |
| 2 | `investigations` INV-18 step 2b and the SCI45 P1 measurement sheet | Add burst incidence and the NMDAR-dependent component to the pHo-step arm; a lower pHo in the knock-out may be a protective state against bursts (IPOTESI) | `net_sign.tsv`; README answers 4-5 |
| 3 | `open_questions_map.tsv` | Add: proton response of GluN2B-containing and triheteromeric receptors at 35 C and 1.3 mM Mg2+ (no source); NMDAR proton sensitivity in layer II/III neurons (no source). Closed: ASIC1a does not open for 7.4 to 7.2 | PS16-PS19; D10-D12 |
| 4 | `hypothesis_packages.tsv` / SCI45 P1 KP1 | Cross-reference: the K2P route (partial at best) and the NMDAR proton route have opposite signs on excitability; net sign not defined | `net_sign.tsv` |
| 5 | `compound_view.tsv` roles of NP10679 and ifenprodil-site NAMs | No change of tier; note that the pH dependence of the tool must be separated from the pH dependence of the target receptor | PS07; Regan 2019 Table 4 |
| 6 | Comparison engine (condition vocabulary) | Extends row 10 of the P1 delta: add pH and Mg2+ as comparability conditions for NMDAR rows (the same GluN2B compound read at pH 7.6 and 7.4 is not COMPARABLE) | `output/proton_sensitivity.tsv` conditions |
| 7 | Receipts | 7 producer (`-84`) and 8 verifier (`-83`) staged; `prior_receipt` set by the verifier (24607230 to the existing -99); none recorded | `output/receipts/`, `verify/receipts/` |
