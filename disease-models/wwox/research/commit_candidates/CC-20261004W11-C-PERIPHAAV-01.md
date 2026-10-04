# CC-20261004W11-C-PERIPHAAV-01 — a peripheral-nerve AAV safety read-out whose dose was chosen by copy number in two rats per dose, with route and sex statements that disagree inside the paper

- `context_policy: SOURCE_FIRST` (first pass written before the held DRG and dose records were opened; compared afterwards).
- Sources: PMID 42436860 (`FTR-20261004-42436860-01`), primary; PMID 42812991 (`FTR-20261004-42812991-01`) as a secondary pointer only. Manifests `VERDICT: PASS`. WWOX occurrences: zero in both (earned null for the gene).
- Change class: **MINOR.** One new research-line record. Narrows no `consolidated baseline` claim.
- **Nothing here is medical advice.**

## 1 · The finding in one sentence

PMID 42436860 is a peripheral sensory-neuron programme (sciatic-nerve injection, painful neuropathy), not a CNS cassette; its dose of 4e11 genome copies per rat was selected from a pilot of two rats per dose read only as sciatic-nerve vector copy at 3 weeks ("not shown"), its safety read-out at 12-14 weeks is histology and immunohistochemistry with the vector-versus-injury comparison carried by an unread supplement, and its own legends and Methods disagree on route (sciatic nerve versus DRG) and on sex.

## 2 · Numbers (recomputed)

| Quantity | Value | How |
|---|---|---|
| Dose | 4e11 GC in 20 microlitres = 2e13 GC per ml | 4e11 / 0.020 ml; Methods |
| Pilot | 1e11/5 microlitres, 2e11/10 microlitres, 4e11/20 microlitres, two rats each; read at 3 weeks, nerve copy only; data not shown | Methods |
| Ratio of top to bottom pilot dose | 4 | 4e11 / 1e11 |
| Sciatic-nerve genome copies at 12-14 weeks | plotted mean about 3.4e5 | Fig. 5 panel |
| DRG L3-L6, lumbar cord, paw skin | plotted means about 2e3 to 5e3, i.e. about 0.6 to 1.5 percent of nerve | Fig. 5 panel; 2e3/3.4e5 and 5e3/3.4e5 |
| Liver, kidney, heart, blood, CSF | under the 500-copy cutoff on the plotted means; several points sit just below 500 | Fig. 5 panel |
| Points plotted for sciatic nerve | about eight, against n = 6 in text and legend | Fig. 5 panel |

## 3 · What this adds, bounds or leaves untouched

- **Corrects a selection premise:** route is peripheral nerve, not CNS; transfer to a CNS restoration spec is route-different.
- **Adds** to the held dose-scalar series a worked case in which "dose" is a per-animal figure with no per-kilogram statement, chosen by efficacy-of-expression and not by tolerability.
- **Bounds** its "no apparent pathology" statement: the imaged panels compare treated injured animals with naive animals, so the mild GFAP and Iba1 increase cannot be attributed to the vector rather than the nerve injury on those panels; the control-vector comparison (ATF3, CD6/CD8, caspase-3) is in Fig. S2, not read.
- **Inconsistencies for the integrator:** Fig. 5 legend says injection into RL4 and RL5 DRG, Fig. 2 legend says DRG delivery, Methods and Results say sciatic nerve; Methods say adult male rats while Results report females; human sensory-neuron work used a lentiviral vector, not AAV.
- **Untouched:** all immunosuppression-pattern and DRG-attribution records; this paper has no immunosuppression arm and no primate data.
- **Pointer from PMID 42812991:** two primaries the review cites (a non-human-primate DRG-detargeting study; an intracranial B-cell re-dosing study) are queue candidates; neither was read.

## 4 · Transfer limits

Rat, AAV6.2FF, peptide payload, peripheral route, 3-month horizon, single laboratory. No transfer to a CNS dose ceiling, to any WWOX cassette or to a human allele.

## 5 · Ops (provisional)

`disease-models/wwox/research/research_lines_current.md`: op `append`. Record: `RL-C-20261004w11c2 — Peripheral-nerve AAV: dose chosen by copy number at n = 2 per dose, safety read against naive not against control vector on the imaged panels, and internal route and sex disagreements`. Status `open`; tag `DATO` for printed values, `INFERENZA` for the attribution limit. Body: sections 1 to 4. No `old` string for an append. Revival trigger: the supplement (Fig. S2) showing the control-vector arm for ATF3 and glia.

### LOCATOR TRIPLES FOR BLIND AUDIT

Artefact `files/fulltext/PMID42436860_NaViPA1_2026_PMC.xml` unless stated.

- (Dose was chosen from a two-rat-per-dose pilot. | (two rats for each dose) | Methods, AAV sciatic nerve injection)
- (Off-target organs were below the quantification cutoff. | There were weak qPCR signals of the AAV genome below the cutoff of 500 copies in the liver, kidney, heart, blood, and biofluids | Results, qPCR biodistribution)
- (The Fig. 5 legend names a DRG injection. | harvested 3 months after AAV6.2FF-CoNaViPA1 injection into RL4 and RL5 DRG, ipsilateral to TNI | Fig. 5 legend)
- (Histology was compared with naive animals. | no observable microscopic pathology compared to tissues from naive animals | Results, pathology)
- (Mild glial proliferation was reported. | mild proliferation of GFAP-positive satellite glial cells and Iba1-positive microglia | Results, pathology)
- (Capsid humoral immunity was not examined. | Although the AAV capsid-specific humoral immunity was not examined in this study | Discussion)
- (Methods list male rats only. | Adult male Sprague-Dawley (SD) rats weighing 100–125 g | Methods, Animals)
- (Human sensory-neuron work used a lentiviral vector. | We first produced a high-titer lentiviral vector (LV)-encoded CoNaViPA1 or CoNP | Results, human DRG neurons)
- [PMID 42812991, artefact `files/fulltext/PMID42812991_AAV_AD_review_2026.txt`] (The review reports DRG pathology across several CNS-directed AAV programmes. | sensory-neuron pathology in dorsal root ganglia has emerged across several CNS-directed AAV programmes | 5.2)
