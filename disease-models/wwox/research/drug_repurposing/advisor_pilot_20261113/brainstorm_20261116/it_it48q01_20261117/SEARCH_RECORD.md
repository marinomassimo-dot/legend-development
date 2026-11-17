# SEARCH_RECORD - IT48Q01 Ba2+-sensitive share of resting conductance, rodent neocortical L2/3 pyramidal neurons, P13-17

Date 2026-11-17. Clients: PubMed MCP tools (search_articles, hit lists only), Europe PMC REST search/fullTextXML (curl, no key, no e-mail), NCBI E-utilities efetch db=pmc (no key, no e-mail), NCBI PMC article pages (curl, stopped when a reCAPTCHA page came back), WebFetch of open pages. No e-mail address was sent to any service. Zero spend.

Query families (independent): A = Ba2+/barium + resting conductance / input resistance / holding current + layer 2/3 + postnatal or age; B = Kir2.x / inward rectifier / leak or K2P + developmental, neocortex, pyramidal; C = full-text phrase screens of Europe PMC (Ba2+ near layer 2/3 + pyramidal + P13-P18), each hit with a PMC id fetched and the text searched automatically for Ba2+/barium/BaCl2; D = broader developmental-physiology and K2P/Kir4.1 families. Family labels in the Europe PMC table are as logged by the wrapper (A, B, C, D, A/B).

## 1. PubMed MCP queries (28 query strings; hit count = total_count returned)

Note on the tool: it AND-s every term and expands each into MeSH/field synonyms, so long strings return 0; shorter two- and three-concept strings were therefore added. Zero-hit strings are kept below on purpose.

| # | family | query string | hits |
|---|---|---|---|
| P1 | A | `barium AND (layer 2/3 OR "layer II/III") AND pyramidal AND (input resistance OR "resting conductance" OR "holding current") AND (postnatal OR development)` | 0 |
| P2 | B | `Kir2 inward rectifier developmental neocortex pyramidal neurons resting membrane potential postnatal` | 0 |
| P3 | A | `Ba2+ sensitive leak conductance cortical pyramidal neuron development input resistance` | 0 |
| P4 | A | `barium resting conductance layer 2/3 pyramidal neurons` | 0 |
| P5 | B | `Kir2 channels developmental neocortex pyramidal neuron` | 0 |
| P6 | A | `developmental changes in resting membrane properties layer II/III pyramidal neurons barium` | 0 |
| P7 | B | `"inward rectifier" "pyramidal neurons" neocortex postnatal development resting potential` | 0 |
| P8 | B | `Kir2 pyramidal neurons barium` | 0 |
| P9 | A | `barium input resistance neocortex pyramidal neurons development` | 0 |
| P10 | B | `Kir2.1 neocortex` | 7 |
| P11 | A | `barium pyramidal neurons (first call max 10; repeated with max 130 to list all)` | 123 |
| P12 | B | `Kir2 channels cortical pyramidal neurons resting membrane potential` | 7 |
| P13 | B | `Kir2.1 postnatal development cortex neurons` | 10 |
| P14 | B | `inward rectifier potassium channel neocortex development` | 14 |
| P15 | B | `Kir2 layer 2/3 pyramidal` | 4 |
| P16 | A | `barium neocortical neurons postnatal` | 1 |
| P17 | A | `resting membrane potential development layer 2/3 pyramidal neurons potassium leak` | 0 |
| P18 | A | `Ba2+ holding current layer II/III neurons juvenile rat cortex` | 0 |
| P19 | A | `developmental decrease input resistance cortical pyramidal neurons potassium channels barium` | 0 |
| P20 | B | `Kir2 developmental upregulation cortex resting potential hyperpolarization` | 0 |
| P21 | A | `barium neocortex input resistance` | 0 |
| P22 | B | `Kir2 developmental neocortex` | 3 |
| P23 | A | `barium neocortex development rat neurons` | 0 |
| P24 | A | `potassium leak conductance postnatal development neocortical pyramidal` | 0 |
| P25 | A | `barium developing neocortex` | 0 |
| P26 | B | `TASK channels neocortical pyramidal neurons development` | 1 |
| P27 | B | `Kir2 channels pyramidal neurons juvenile` | 0 |
| P28 | A | `barium-sensitive potassium conductance layer II/III` | 0 |

## 2. Europe PMC REST search queries (46 rows, 43 distinct strings; 3 strings were run twice because the first run was stopped for slowness)

| # | family | query string | hitCount |
|---|---|---|---|
| E1 | A | `(barium OR "Ba2+") AND ("layer 2/3" OR "layer II/III" OR "layer 2/3") AND pyramidal AND ("input resistance" OR "resting conductance" OR "holding current")  [first test call, run before the logging wrapper existed; hit count 54 as printed]` | 54 |
| E2 | A | `(barium OR "Ba2+" OR BaCl2) AND ("layer 2/3" OR "layer II/III" OR "layer 2/3" OR "layer II-III") AND (pyramidal) AND (postnatal OR "P13" OR "P14" OR "P15" OR "P16" OR developmental) AND ("resting" OR leak OR "input resistance")` | 69 |
| E3 | A | `TITLE_ABS:(barium OR "Ba2+") AND TITLE_ABS:(pyramidal AND (cortex OR cortical OR neocortex OR neocortical)) AND TITLE_ABS:(postnatal OR development OR developmental OR maturation)` | 2 |
| E4 | B | `TITLE_ABS:("inward rectifier" OR Kir2 OR "Kir2.1" OR "Kir2.3") AND TITLE_ABS:(neocortex OR neocortical OR cortical) AND TITLE_ABS:(postnatal OR development OR developmental OR maturation)` | 16 |
| E5 | A | `TITLE_ABS:(barium OR "Ba2+" OR BaCl2) AND TITLE_ABS:("layer 2/3" OR "layer II/III" OR "layer 2/3" OR "layers II/III" OR "layer II" OR "layer 2")` | 12 |
| E6 | A | `TITLE_ABS:(barium OR "Ba2+") AND TITLE_ABS:("resting membrane potential" OR "resting potential" OR "input resistance" OR "leak current" OR "leak conductance") AND TITLE_ABS:(neocortex OR neocortical OR cortex OR cortical)` | 27 |
| E7 | A | `TITLE_ABS:("Kir2" OR "inward rectifier" OR "inwardly rectifying") AND TITLE_ABS:("pyramidal") AND TITLE_ABS:(postnatal OR development OR developmental OR age OR maturation)` | 21 |
| E8 | B | `TITLE_ABS:(barium OR "Ba2+" OR BaCl2) AND TITLE_ABS:(neocortical OR neocortex OR "visual cortex" OR "somatosensory cortex" OR "barrel cortex" OR "prefrontal") AND TITLE_ABS:(postnatal OR developing OR development OR developmental OR neonatal OR juvenile)` | 4 |
| E9 | B | `TITLE_ABS:("resting conductance" OR "leak conductance" OR "background conductance" OR "leak current" OR "leak K+") AND TITLE_ABS:("layer 2/3" OR "layer II/III" OR "layer 2/3" OR "layers 2/3") AND TITLE_ABS:(development OR postnatal OR developmental OR maturation)` | 2 |
| E10 | B | `TITLE_ABS:("input resistance" OR "membrane resistance" OR "resting potential" OR "resting membrane potential") AND TITLE_ABS:(postnatal OR developmental OR maturation) AND TITLE_ABS:("layer 2/3" OR "layer II/III" OR "layer 2/3" OR "superficial") AND TITLE_ABS:(pyramidal)` | 13 |
| E11 | B | `TITLE_ABS:(K2P OR TASK OR TREK OR TWIK OR "two-pore" OR "two pore") AND TITLE_ABS:(pyramidal) AND TITLE_ABS:(neocortex OR neocortical OR cortex) AND TITLE_ABS:(postnatal OR developmental OR development)` | 67 |
| E12 | A | `("Ba2+-sensitive" OR "barium-sensitive" OR "Ba-sensitive") AND ("layer 2/3" OR "layer II/III" OR "layer 2/3") AND (pyramidal) AND (postnatal OR P14 OR P15 OR "P13")` | 7 |
| E13 | A | `("Ba2+-sensitive" OR "barium-sensitive") AND ("resting conductance" OR "leak conductance" OR "holding current" OR "input resistance") AND neocortex AND (postnatal OR developing OR "P14")` | None |
| E14 | A | `TITLE_ABS:("Kir2" OR "Kir2.1" OR "inward rectifier") AND TITLE_ABS:("layer 2/3" OR "layer II/III" OR "layer 2/3")` | 6 |
| E15 | A | `TITLE_ABS:("Kir4.1" OR Kir2) AND TITLE_ABS:(neurons) AND TITLE_ABS:(cortex) AND TITLE_ABS:(postnatal OR "developmental") AND TITLE_ABS:("resting membrane potential" OR "resting potential")` | 0 |
| E16 | B | `TITLE_ABS:("leak" OR "background" OR "resting") AND TITLE_ABS:("potassium conductance" OR "K+ conductance" OR "K+ current" OR "potassium current") AND TITLE_ABS:(neonatal OR postnatal OR developing OR development) AND TITLE_ABS:(neocortical OR neocortex OR cortical)` | 10 |
| E17 | B | `TITLE_ABS:("intrinsic properties" OR "intrinsic excitability" OR "membrane properties") AND TITLE_ABS:("layer 2/3" OR "layer II/III" OR "layer 2/3") AND TITLE_ABS:(postnatal OR development OR maturation OR developmental) AND TITLE_ABS:(pyramidal)` | 23 |
| E18 | B | `TITLE_ABS:(Kir2 OR "inward rectifier" OR "inwardly rectifying") AND TITLE_ABS:(neocortical OR neocortex OR "visual cortex" OR "somatosensory cortex" OR "prefrontal cortex") AND TITLE_ABS:(pyramidal)` | 52 |
| E19 | B | `TITLE_ABS:(Kir2.1 OR Kir2.2 OR Kir2.3 OR KCNJ2 OR KCNJ12 OR KCNJ4) AND TITLE_ABS:(cortex OR cortical OR neocortex) AND TITLE_ABS:(neurons) AND TITLE_ABS:(excitability OR "resting")` | 10 |
| E20 | C-fulltext-screen | `(barium OR "Ba2+" OR BaCl2) AND ("layer 2/3" OR "layer II/III" OR "layers 2/3") AND pyramidal AND (P13 OR P14 OR P15 OR P16 OR P17) AND (Kir OR "inward rectif" OR "resting")` | 34 |
| E21 | C-fulltext-screen | `("Ba2+" OR BaCl2 OR barium) AND ("layer 2/3" OR "layer II/III") AND pyramidal AND ("holding current" OR "input resistance") AND (postnatal OR "P14")` | 39 |
| E22 | C-fulltext-screen | `(Kir2 OR "inward rectifier") AND ("layer 2/3" OR "layer II/III") AND pyramidal AND (developmental OR "postnatal day")` | 104 |
| E23 | C | `(barium OR "Ba2+" OR BaCl2) AND ("layer 2/3" OR "layer II/III" OR "layers 2/3") AND pyramidal AND (P13 OR P14 OR P15 OR P16 OR P17) AND (Kir OR "inward rectif" OR "resting")` (repeat run of an earlier string) | 34 |
| E24 | C | `("Ba2+" OR BaCl2 OR barium) AND ("layer 2/3" OR "layer II/III") AND pyramidal AND ("holding current" OR "input resistance") AND (postnatal OR "P14")` (repeat run of an earlier string) | 39 |
| E25 | C | `(Kir2 OR "inward rectifier") AND ("layer 2/3" OR "layer II/III") AND pyramidal AND (developmental OR "postnatal day")` (repeat run of an earlier string) | 104 |
| E26 | A/B | `TITLE_ABS:(barium OR "Ba2+" OR BaCl2 OR "Ba(2+)") AND TITLE_ABS:("pyramidal" OR "pyramidal neurons" OR "pyramidal cells") AND TITLE_ABS:("neocortical" OR "neocortex" OR "barrel cortex" OR "visual cortex" OR "somatosensory" OR "auditory cortex" OR "prefrontal" OR "frontal cortex") AND TITLE_ABS:("juvenile" OR "neonatal" OR "young" OR "postnatal" OR "developing")` | 1 |
| E27 | A/B | `TITLE_ABS:("potassium leak" OR "K+ leak" OR "leak K+" OR "leak potassium" OR "leak conductance") AND TITLE_ABS:("pyramidal") AND TITLE_ABS:("cortex" OR "cortical" OR "neocortex")` | 18 |
| E28 | A/B | `TITLE_ABS:(Kir2 OR "Kir2.1" OR "Kir2.2" OR "Kir2.3" OR "Kir2.4") AND TITLE_ABS:(pyramidal) AND TITLE_ABS:(cortex OR cortical)` | 10 |
| E29 | A/B | `TITLE_ABS:("inward rectifier" OR "inwardly rectifying" OR Kir) AND TITLE_ABS:("resting membrane potential" OR "resting potential") AND TITLE_ABS:(neonatal OR postnatal OR developmental OR development) AND TITLE_ABS:(neocortex OR neocortical OR cortical OR cortex) AND TITLE_ABS:(neurons)` | 2 |
| E30 | A/B | `TITLE_ABS:("passive membrane properties" OR "membrane properties" OR "intrinsic properties") AND TITLE_ABS:(maturation OR development OR developmental OR postnatal) AND TITLE_ABS:(neocortical OR neocortex OR barrel OR "somatosensory cortex" OR "visual cortex") AND TITLE_ABS:(pyramidal) AND TITLE_ABS:(rat OR mouse OR mice OR rats)` | 23 |
| E31 | C | `"layer 2/3" AND pyramidal AND ("Ba2+" OR BaCl2) AND ("holding current" OR "input resistance") AND (P14 OR P15 OR P16 OR P17 OR P13) AND (mouse OR rat) AND ("leak" OR "resting conductance")` | 9 |
| E32 | C | `("layer II/III" OR "layer 2/3") AND ("barium" OR "Ba2+") AND ("resting membrane potential") AND (juvenile OR "P14" OR "P21" OR "P18") AND ("Kir" OR "K2P" OR "leak")` | 22 |
| E33 | C | `("Ba2+-sensitive" OR "barium-sensitive") AND (pyramidal) AND (cortex) AND ("input resistance") AND (postnatal OR juvenile)` | 23 |
| E34 | C | `("Kir2" OR "Kir") AND ("layer 2/3" OR "layer II/III") AND pyramidal AND ("input resistance") AND (P14 OR P15 OR P16 OR P17 OR "postnatal day")` | 25 |
| E35 | C | `(Ba2+ OR BaCl2 OR barium) AND (barrel OR "somatosensory cortex") AND ("layer 2/3" OR "layer II/III") AND pyramidal AND ("resting" OR "leak") AND (P14 OR P15 OR P16 OR "P18")` | 23 |
| E36 | C | `(Ba2+ OR BaCl2 OR barium) AND ("prefrontal" OR "frontal cortex" OR "cingulate" OR "visual cortex" OR "auditory cortex") AND ("layer 2/3" OR "layer II/III") AND pyramidal AND ("resting" OR "leak") AND (P14 OR P15 OR P16 OR "P18")` | 26 |
| E37 | C | `("layer 2/3" OR "layer II/III") AND pyramidal AND (Ba2+ OR BaCl2) AND ("holding current")` | 28 |
| E38 | C | `("layer 2/3" OR "layer II/III") AND pyramidal AND (Ba2+ OR BaCl2) AND ("input resistance") AND (increased OR depolarized)` | 62 |
| E39 | C | `("layer 2/3" OR "layer II/III") AND pyramidal AND (Ba2+ OR BaCl2) AND ("Kir" OR "inward rectifier") AND ("resting membrane potential")` | 41 |
| E40 | C | `("layer 2/3" OR "layer II/III") AND pyramidal AND ("Ba2+-sensitive" OR "barium-sensitive" OR "BaCl2-sensitive")` | 18 |
| E41 | C | `(Ba2+ OR BaCl2) AND ("Kir2" OR "Kir") AND ("layer 2/3" OR "L2/3") AND (P14 OR P15 OR P16 OR P17 OR P18 OR P21 OR "postnatal day 14")` | 17 |
| E42 | C | `(Ba2+ OR BaCl2) AND ("K2P" OR "TASK" OR "leak channels") AND ("layer 2/3" OR "L2/3") AND pyramidal AND (P14 OR P15 OR P16 OR P17 OR P18 OR "postnatal day")` | 20 |
| E43 | D | `TITLE_ABS:(neonatal OR postnatal OR "developing" OR immature) AND TITLE_ABS:(neocortical OR neocortex OR "cerebral cortex" OR "cortical neurons") AND TITLE_ABS:("potassium conductance" OR "potassium current" OR "K+ conductance" OR "K+ current" OR "inward rectifi*" OR "membrane resistance" OR "input resistance") AND TITLE_ABS:(rat OR mouse OR rodent OR slices)` | 50 |
| E44 | D | `TITLE_ABS:(TASK-1 OR TASK-3 OR TASK OR TREK OR TWIK OR K2P OR KCNK) AND TITLE_ABS:(cortical OR neocortical) AND TITLE_ABS:(pyramidal) AND TITLE_ABS:(barium OR "Ba2+" OR leak)` | 1 |
| E45 | D | `TITLE_ABS:(Kir4.1 OR Kir2.1 OR Kir2) AND TITLE_ABS:(neurons) AND TITLE_ABS:("cortical" OR "neocortex") AND TITLE_ABS:(maturation OR "developmental" OR "ontogeny" OR "postnatal")` | 10 |
| E46 | D | `TITLE_ABS:("subthreshold" OR "resting") AND TITLE_ABS:("Kir" OR "inward rectifier" OR "barium") AND TITLE_ABS:("layer 2/3" OR "layer II/III") AND TITLE_ABS:(pyramidal)` | 3 |

Row E13 shows hitCount None: Europe PMC returned no count field; read as zero hits. E20-E22 are the first run of the three family-C strings (stopped for slowness); E23-E25 are the same three strings re-run with the faster script.

## 3. Lookups (not searches)

- Europe PMC EXT_ID lookups of PMIDs to read titles/abstracts (about 8 calls, around 100 PMIDs): 39740351, 30535288, 21123568, 18076085, 17376848, 16177047, 11850502, 41505254, 21460837, 17494709, 9098551, 36567290, 33020214, 30057116, 25472417, 20861444, 20688390, 17121744, 16393152, 8871192, 2118822, the 123 hits of P11, 1857546, 8233033, 9209118, 16510775, 14973314, 14602839, 18417631, 20705896, 15936845, 25355958, 12611962, 27534393.
- Europe PMC TITLE lookups of two preprints: "Synaptic input-selective homeostasis safeguards developing cortical neurons toward setpoint activity" (PPR1291058) and "Enhanced Ba2+-sensitive inward rectifying potassium conductance reduces intrinsic excitability of layer 2/3 pyramidal neurons in the primary auditory cortex of Fmr1 knockout mice" (PPR1225217).

## 4. Automated full-text screens (family C)

Three batches (E23-E25, then E31-E36, then E37-E42) produced 210 unique PMC ids. For each, the full text was fetched (NCBI efetch db=pmc; Europe PMC fullTextXML returned HTTP 500 for most) and searched for Ba2+/barium/BaCl2. 122 had a retrievable body and 91 had none (publisher withholds XML, meeting abstracts, supplements; efetch returned no body). Counts of Ba mentions were then used to choose papers to read. A paper whose body could not be fetched was NOT counted as read and, when plausibly relevant, is in human_access_list.tsv.

## 5. Routes stopped or failed

- NCBI PMC article page for PMC10942629 returned a Google reCAPTCHA challenge page at about 06:54 on 2026-11-17 (earlier PMC page requests for other ids in the same session had returned article text). Treated as a STOP: no further PMC article pages were requested after that; not bypassed.
- Europe PMC fullTextXML: HTTP 500 for most ids (including PMC3056441, PMC6725503, PMC5242407, PMC9576169, PMC2765623, PMC6742316 and the preprint PPR1225217).
- journals.physiology.org (Sceniak and MacIver 2006) via WebFetch: HTTP 403.
- bioRxiv direct curl: HTTP 429 (Cloudflare error 1015) then 302 to nowhere; the preprint text was read through WebFetch only (summariser-mediated; see RESULT.md limits).
- Europe PMC image route for Xue 2014 Extended Data Fig. 4 (europepmc.org/articles/PMC4117808/bin/nihms584335f9.jpg): HTTP 403. Not retried. Nature article page returned a 303. Figure values for that paper therefore not read.
- Open route that worked for one figure: eLife IIIF image server (iiif.elifesciences.org) for Nguyen 2024 Figure 3 - figure supplement 3, fetched as a plain JPEG and read by eye; values read are approximate.

## 6. Absence statements

No paper giving the Ba2+-sensitive share of resting (leak/holding) conductance in layer II/III pyramidal neurons at P13-P17 was found by query families A and B (28 PubMed strings P1-P28 and 43 distinct Europe PMC strings among E1-E46, above) or by the family-C full-text screen of 210 PMC ids. This is a statement about those queries and about the openly retrievable texts, not that no such measurement exists. Paywalled or non-retrievable papers that could contain it are in human_access_list.tsv.
