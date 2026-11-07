# Independent audit, IT34 statements against Breton et al. 2021 (PMC8609180)

Method: Europe PMC fullTextXML fetched with curl, tags stripped with a Python regex (no summariser). 76,001 characters of body, legends, Table 1, methods and references. Supplementary files NOT read.

| # | Verdict | Locator | Note |
|---|---|---|---|
| 1 | SUPPORTED (sag unit caveat) | "Resting membrane potential -79.25 ± 1.99 -75.51 ± 1.81* -73.62 ± 1.36 *"; "Sag (at -200 pA) 1.18 ± 0.24 2.04 ± 0.44* 2.57 ± 0.42*"; "Input resistance (Mohm) 102.88 ± 11.74 143.26 ± 15.49* 143.03 ± 8.88*" | Table 1 and Fig 6 legend (superficial layers II/III). All nine numbers match. The sag row has no unit in the table; the legend says "sag voltage", so mV is inferred. Table also gives SDs/SEMs and stars (p<0.05 vs WT; n 13/15/40 cells). |
| 2 | SUPPORTED | "S-WT vrs S-HT p = 0.24947; * p = 0.00393"; Table 1 rebound 0.96, 1.24, 1.86* mV | Fig 6C legend. Uncorrected unpaired t-tests, small n. |
| 3 | OVERSHOOT (inference not authorial) | "no significant difference in the slope of the curve in the S-KOs"; "control of pyramidal neuron membrane potential is a factor underlying" | Sec 2.6 and end of 2.6. Data match (slope 0.184/0.162/0.204 Hz/pA, p=0.37 KO vs WT) and the authors note depolarised cells need less current. But they never say "rather than" intrinsic excitability; they say membrane-potential control is "a factor", and Discussion 3.5 still says "increased evoked spike frequency". The word "intrinsic" does not occur in the body. Also, the slope-shift data are in Supplementary Fig S4 (not read), and S-HT is also depolarised yet hyperexcitability is KO only. |
| 4 | SUPPORTED | "0 of n = 11 slices from 7 S-WT mice; 4 of n = 23 slices from 14 S-HT mice; 36 of n = 42 slices from 24 S-KO mice" | Sec 2.1. Counts are slices, "spontaneous activity" (bursts), neocortical; hippocampal slices were not different. |
| 5 | SUPPORTED (with qualifier) | "it enhanced 4-aminopyridine-induced seizure-like events at high potassium concentrations"; "use of an Ih blocker is controversial" | Sec 3.5. These are cited precedents (Gasparini 1997 hippocampus: ZD7288 reduces excitability; Wang 2016 neocortex: worsened). The paper's own words: "in some cases could make the pathology worse". Not Breton's data. |
| 6 | SUPPORTED (absence, body-text scope) | no hits for HCN, "h-current", "I h"; ZD7288 only at Sec 3.5 (Discussion) and references | Searched the full stripped text for: ZD, ZD7288, zatebradine, ivabradine, Ih, I h, HCN, h-current, "hyperpolarization-activated", "hyperpolarization activated", "blocker", "voltage clamp/voltage-clamp", "intrinsic". Pharmacology (Methods) lists only TTX 1 uM, d-APV 50 uM, CBX 100 uM, BB-FCF 10 uM. Voltage clamp used only for burst reversal potential (-31 mV, Fig 3) and mEPSC at -70 mV. Sag was measured in current clamp; the paper infers "the hyperpolarization activated potassium current was elevated" from a larger hyperpolarisation, with no Ih recording. Supplementary data and figures' images not read; absence is for text. |
| 7 | OVERSHOOT on the last clause; rest SUPPORTED | "CBX (100 μM) decreased the frequency of the events by 87% ( p = 0.008)"; "This did not return to normal levels after washout"; "it could block NMDA receptors ( Chepkova et al., 2008 ), which could partially account" | Sec 2.3 and 3.x. 87% is event frequency (n = 36 bursts, 4 slices, 3 animals); duration -18%, amplitude unchanged. Washout failure stated (d-APV, in contrast, reversed). NMDA caveat stated, plus CBX blocks pannexin (BB-FCF did not mimic it). But the paper does not say the effect is "not attributable to gap junctions": the Abstract says bursts are "NMDAR and gap-junction dependent" and the Discussion says "gap junctional blockade could be a novel anti-epileptic target". The accurate statement is "not specific to gap junctions; NMDA block may partly account". |

## Plain sample

| Item | Result |
|---|---|
| (a) HGNC IDs | Confirmed via rest.genenames.org: HCN1 HGNC:4845, HCN2 HGNC:4846, HCN3 HGNC:19183, HCN4 HGNC:16882, all Approved. |
| (b) GO:0042391 | QuickGO: "regulation of membrane potential", isObsolete=false, biological_process. |
| (c) DisMech file | raw.githubusercontent.com, both commits HTTP 200, 90,399 bytes each, SHA-256 fe762952897bbcc31020f014f704eae719dab520300f3a38967f81ad8a363229 identical. (Short hash adf2b657afb3 resolved by GitHub.) |

No plain error found, so no extension.

## Omissions that matter
- Items 3 and 7 carry conclusions the authors did not draw; use "a factor" and "not specific to gap junctions".
- Item 1 sag unit is inferred. Item 6 absence is for the main text only; supplements unread.
- Table 1 stars are uncorrected t-tests; the heterozygote shows depolarisation, sag and input resistance changes without bursting in most slices (4/23).

## Setting
Sonnet 5.5 (claude-sonnet-5-5), low reasoning effort as presented, no subagents, no spend, no e-mail sent. Depth: full body text of the paper read by regex search and targeted passage reading, not page-by-page figure inspection.
