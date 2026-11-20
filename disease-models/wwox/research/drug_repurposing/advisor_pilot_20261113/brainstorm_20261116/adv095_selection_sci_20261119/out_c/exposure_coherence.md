# Exposure over potency, arithmetic only (no threshold)

Molecular masses from formulas (g/mol): ethosuximide 141.17, memantine 179.31, ketamine 237.73, retigabine 303.34, ganaxolone 332.53, clemastine 343.89.
Tissue density taken as 1 g/mL; every concentration is TOTAL unless the label says microdialysate.

| agent | exposure_as_labelled | value_as_printed | conc_uM_computed | potency_assay | potency_uM | ratio_C_over_potency |
|---|---|---|---|---|---|---|
| ethosuximide | brain total, 72.3 mg/kg i.p., 45 min, adult Swiss mouse | 134.9 ug/g | 955.6 | persistent T-current IC50, recombinant human Cav3.x | 600 | 1.59 |
| ethosuximide | brain total, 72.3 mg/kg i.p., 45 min, adult Swiss mouse | 134.9 ug/g | 955.6 | CACNA1I IC50, FLIPR (value reported above 5 mM) | 5000 | 0.191 |
| ethosuximide | brain, same, if the printed value is per g of 1:2 homogenate (tissue = 3 x) | 404.7 ug/g | 2867 | persistent T-current IC50, recombinant human Cav3.x | 600 | 4.78 |
| ethosuximide | brain, same, if the printed value is per g of 1:2 homogenate (tissue = 3 x) | 404.7 ug/g | 2867 | CACNA1I IC50, FLIPR (value reported above 5 mM) | 5000 | 0.573 |
| memantine | brain total Cmax, 10 mg eq./kg s.c., Tmax 1 h, adult male C57Bl/6 | 72520 nM | 72.52 | IC50 GluN1/2A, -60 mV, HEK293, glutamate-induced (one 2024 document) | 0.84 | 86.3 |
| memantine | brain total Cmax, 10 mg eq./kg s.c., Tmax 1 h, adult male C57Bl/6 | 72520 nM | 72.52 | IC50 GluN1/2A, -40 mV, same document | 28.1 | 2.58 |
| memantine | brain total Cmax, 10 mg eq./kg s.c., Tmax 1 h, adult male C57Bl/6 | 72520 nM | 72.52 | IC50 range with 1 mM Mg2+, GluN2A..2D, holding potential not stated in the producer text (low) | 1.61 | 45 |
| memantine | brain total Cmax, 10 mg eq./kg s.c., Tmax 1 h, adult male C57Bl/6 | 72520 nM | 72.52 | IC50 range with 1 mM Mg2+, holding potential not stated in the producer text (high) | 13.4 | 5.41 |
| memantine | plasma total Cmax, same | 7983 nM | 7.983 | IC50 GluN1/2A, -60 mV, HEK293, glutamate-induced (one 2024 document) | 0.84 | 9.5 |
| memantine | plasma total Cmax, same | 7983 nM | 7.983 | IC50 GluN1/2A, -40 mV, same document | 28.1 | 0.284 |
| memantine | plasma total Cmax, same | 7983 nM | 7.983 | IC50 range with 1 mM Mg2+, GluN2A..2D, holding potential not stated in the producer text (low) | 1.61 | 4.96 |
| memantine | plasma total Cmax, same | 7983 nM | 7.983 | IC50 range with 1 mM Mg2+, holding potential not stated in the producer text (high) | 13.4 | 0.596 |
| memantine | brain total Cmax, 1 mg eq./kg s.c. | 5360 nM | 5.36 | IC50 GluN1/2A, -60 mV, HEK293, glutamate-induced (one 2024 document) | 0.84 | 6.38 |
| memantine | brain total Cmax, 1 mg eq./kg s.c. | 5360 nM | 5.36 | IC50 GluN1/2A, -40 mV, same document | 28.1 | 0.191 |
| memantine | brain total Cmax, 1 mg eq./kg s.c. | 5360 nM | 5.36 | IC50 range with 1 mM Mg2+, GluN2A..2D, holding potential not stated in the producer text (low) | 1.61 | 3.33 |
| memantine | brain total Cmax, 1 mg eq./kg s.c. | 5360 nM | 5.36 | IC50 range with 1 mM Mg2+, holding potential not stated in the producer text (high) | 13.4 | 0.4 |
| ketamine | brain total, 10 mg/kg i.p., 1 h, adult male C57BL/6 under chronic restraint stress | 0.23 uM | 0.23 | IC50 GluN1/2A, -60 mV, HEK293 (one 2024 document) | 0.5 | 0.46 |
| ketamine | brain total, 10 mg/kg i.p., 1 h, adult male C57BL/6 under chronic restraint stress | 0.23 uM | 0.23 | IC50 GluN1/2A, -40 mV, same document | 53.3 | 0.00432 |
| ketamine | brain total, 10 mg/kg i.p., 1 h, adult male C57BL/6 under chronic restraint stress | 0.23 uM | 0.23 | IC50 range with 1 mM Mg2+ (low) | 1.18 | 0.195 |
| ketamine | brain total, 10 mg/kg i.p., 1 h, adult male C57BL/6 under chronic restraint stress | 0.23 uM | 0.23 | IC50 range with 1 mM Mg2+ (high) | 5.35 | 0.043 |
| retigabine | brain total, 5 mg/kg i.p., P7 rat pup, peak 1-2 h | 330 ng/g | 1.088 | human Kv7.2/7.3 EC50, lowest across documents (Rb+ efflux) | 0.43 | 2.53 |
| retigabine | brain total, 5 mg/kg i.p., P7 rat pup, peak 1-2 h | 330 ng/g | 1.088 | human Kv7.2/7.3 EC50, highest across documents (fluorescence slope) | 11.2 | 0.0971 |
| retigabine | brain total, 15 mg/kg i.p., P7 rat pup | 1296 ng/g | 4.272 | human Kv7.2/7.3 EC50, lowest across documents (Rb+ efflux) | 0.43 | 9.94 |
| retigabine | brain total, 15 mg/kg i.p., P7 rat pup | 1296 ng/g | 4.272 | human Kv7.2/7.3 EC50, highest across documents (fluorescence slope) | 11.2 | 0.381 |
| retigabine | brain total, 30 mg/kg i.p., P7 rat pup | 2013 ng/g | 6.636 | human Kv7.2/7.3 EC50, lowest across documents (Rb+ efflux) | 0.43 | 15.4 |
| retigabine | brain total, 30 mg/kg i.p., P7 rat pup | 2013 ng/g | 6.636 | human Kv7.2/7.3 EC50, highest across documents (fluorescence slope) | 11.2 | 0.593 |
| retigabine | brain EC50 for MES protection, adult male CF-1 mouse, oral | 3.58 uM | 3.58 | human Kv7.2/7.3 EC50, lowest across documents (Rb+ efflux) | 0.43 | 8.33 |
| retigabine | brain EC50 for MES protection, adult male CF-1 mouse, oral | 3.58 uM | 3.58 | human Kv7.2/7.3 EC50, highest across documents (fluorescence slope) | 11.2 | 0.32 |
| ganaxolone | brain total Cmax, 3 mg/kg i.m., Tmax 10 min, adult male NIH Swiss | 1239 ng/g | 3.726 | GABA-A alpha4beta3delta EC50 (CHO, potentiation, one 2015 document) | 0.103 | 36.2 |
| ganaxolone | brain total Cmax, 3 mg/kg i.m., Tmax 10 min, adult male NIH Swiss | 1239 ng/g | 3.726 | GABA-A alpha1beta2gamma2 EC50 (LTK cells, same document) | 0.266 | 14 |
| clemastine | plasma total Cmax, 7.5 mg/kg/day oral, steady state, neonatal mouse (about P10) | 44 ng/mL | 0.1279 | OPC differentiation, effective concentrations, lowest (rat OPC) | 0.01 | 12.8 |
| clemastine | plasma total Cmax, 7.5 mg/kg/day oral, steady state, neonatal mouse (about P10) | 44 ng/mL | 0.1279 | OPC differentiation, most effective concentration | 0.5 | 0.256 |
| clemastine | plasma total Cmax, 7.5 mg/kg/day oral, steady state, neonatal mouse (about P10) | 44 ng/mL | 0.1279 | muscarinic M1 Ki, [3H]QNB displacement (one 2020 document) | 0.02 | 6.4 |
| gaboxadol | CNS extracellular peak, 2.5 to 10 mg/kg s.c., adult Wistar rat (low end) | 0.7 uM | 0.7 | GABA-A alpha1beta2gamma2S functional EC50 (FLIPR; no delta row exists in ChEMBL) | 14 | 0.05 |
| gaboxadol | CNS extracellular peak, 2.5 to 10 mg/kg s.c., adult Wistar rat (low end) | 0.7 uM | 0.7 | delta-dependent tonic current evoked at 1 uM THIP (mouse thalamic neurons) | 1 | 0.7 |
| gaboxadol | CNS extracellular peak, same (high end) | 3 uM | 3 | GABA-A alpha1beta2gamma2S functional EC50 (FLIPR; no delta row exists in ChEMBL) | 14 | 0.214 |
| gaboxadol | CNS extracellular peak, same (high end) | 3 uM | 3 | delta-dependent tonic current evoked at 1 uM THIP (mouse thalamic neurons) | 1 | 3 |
