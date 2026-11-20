# Blind audit 2 of the unit B packet change: delegate report, verbatim

A second fresh legend-delegate, claude-sonnet-5-5, effort high (read back from its transcript); packet AUDIT_PACKET_2.md with the anchors written out. Persisted by IT; not edited. Result: SUPPORTED_WITH_LIMIT 4 (U1, U3, U4, U5), OVERSHOOT 1 (U2: 'adult'), plus one clause OVERSHOOT in U5 ('clemastine only'); repairs applied afterwards (narrowing only, unaudited).

BLIND AUDIT 2, unit B packet statements U1 to U5 (verifier, sonnet, high, one round)

Sources are PubMed tools and Europe PMC (HTTP 200, no 403 and no reCAPTCHA).
- PMC3401299 (PMID 22315091, DOI 10.1007/s00702-012-0767-1). Methods came through the PubMed tool. Tables 1 to 4 came through Europe PMC fullTextXML, because the PubMed tool dropped the tables.
- PMID 708147 abstract (no DOI listed).
- Odell 2024, PMC11502491 (PMID 38942888, DOI 10.1038/s41390-024-03326-w): full text through the PubMed tool and Table 1 through Europe PMC.
- PMID 28385597 (DOI 10.1016/j.bmc.2017.03.047) and PMID 31809508 (DOI 10.1371/journal.pone.0226017): abstracts.

Repository files read, and no others:
- AUDIT_PACKET_2.md
- VERIFIER_PASS_READING_SCI_20261120.md
- BATCH1_ethosuximide_lithium_memantine_HE_20261119.md
- BATCH6_broad_clemastine_sobetirome_tiratricol_HE_20261119.md

Scratch: /home/desktop/.claude/jobs/96cc479a/tmp/blind_unitb2/ (two XML downloads only).

| Unit | Verdict | Anchor says more or less than the statement |
|---|---|---|
| U1 | SUPPORTED_WITH_LIMIT | The numbers, population and arm are exact. The limits are in the notes below: "disputed", an unstated link between the two 0.6 mM values, and route-bound "not found". |
| U2 | OVERSHOOT | "adult" is not in the source. The WOREE part has no anchor. |
| U3 | SUPPORTED_WITH_LIMIT | "callosal" is not in item 4. "fewer nodes" is omitted, so the anchor says more. |
| U4 | SUPPORTED_WITH_LIMIT | "adult mice" is not in the abstract. "Equipotent" drops the "nearly every pair" quantifier. "So the window matters" is an inference from one small arm. |
| U5 | SUPPORTED_WITH_LIMIT; the "clemastine only" clause is OVERSHOOT | No anchor searched thyromimetic plasma. The thyromimetic brain "unknown" rests on titles and abstracts. |

**Notes**

U1, verified against the primary paper:
- Methods: "Male albino Swiss mice weighing 24–30 g". No age is given.
- Methods: "homogenized in distilled water (1:2, w:v)". The concentration is "expressed in μg/g ... of wet tissue", and no dilution correction is stated.
- Methods: "times chosen to coincide with that scheduled for the PTZ test". Separately, "ETS 45 min" before the tests.
- Table 3: "ETS (72.3) + saline | 134.9 ± 7.73 µg/g". Its footnote says "at least eight separate brain preparations".
- Table 2: control ED50 "155.8 (139.7–173.7)". The 72.3 mg/kg dose is the ED50 in the sildenafil 40 arm, not the control ED50. The statement does not claim otherwise, but a reader should know no brain value exists at 155.8.
- Arithmetic: 134.9 / 141.17 = 0.9556 µmol/g, which is 0.96 mM if density is 1. 72.3 / 150 = 0.482, so "about half" holds. The 150 mg/kg Wwox dose comes from the verifier file, item 14.
- PMID 708147: "in mice of hardly 1 hr. Concentrations in serum and brain of mice equilibrated within 10 min." This is an aside in a dog paper, with no mouse dose, route, sex or age. "Within minutes" is fair, but this is thin evidence.
- "Disputed" is the weak word. BATCH1 says "The two values are not comparable: a different assay, one at a single channel subtype". Item 12 says the abstract "must not be quoted as evidence that native studies disagree".
- BATCH1 gives the 0.6 mM row as "unknown origin" (document CHEMBL4229462). Nothing in the anchors says that row is the Gomora recombinant human value. "One origin" assumes it.
- "No juvenile exposure found" is route-bound. BATCH1 names two PubMed routes. Item 13 lists ten papers read only at abstract level.
- Label wording: BATCH1 says "absence (petit mal) epilepsy"; the packet says "absence seizures". Near enough.

U2: The packet's own U1 says "no age given". Table 3 and Methods give only 24 to 30 g, so "adult" is HE's characterisation in BATCH1, not the paper's. The WOREE exposure part is not addressed by any anchor.

U3:
- Odell Table 1 gives Cmax 44.0 ng/mL, CV 49.4%, Tmax 0.5 h, geometric mean of each time point, "plasma analysis was done at steady state".
- Methods: "weighed and dosed based on the clemastine fumarate salt". Doses were 0.5, 2, 7.5 and 10, so 7.5 was not the lowest.
- The paper has no brain or unbound value. It says steady state was "assumed after 7 days of dosing".
- The paper states M1 antagonism is "the most likely mechanism", which is literature mechanism.
- Arithmetic: 117/20 = 5.85, so "six-fold" holds. The 2020 document values are M1 20, M2 117, M3 56, M4 53.7 and M5 27.5 nM.
- The harm sentence rests only on item 4: 50 mg/kg/day i.p. only, "N1 slower", "fewer nodes", thinner myelin in 0 to 0.5 µm axons, n 3 for EM. Item 4 never says "callosal", and I could not check the primary paper.
- Label wording matches BATCH6.

U4:
- Ratios recomputed from BATCH6:
  - Sobetirome pairs: 18, 6.6, 12.5, 3.41, 6.43, 7.14, 26.5 and 0.167. That is seven of eight beta-preferring, from 3.4 to 26-fold, one reversed.
  - Tiratricol: binding 2.92 and 3.47 (about three-fold), reporter EC50 alpha 2.0 against beta 4.0 nM (alpha-preferring).
- BATCH6 says T3 is "about 1-fold in nearly every pair", with three examples only.
- Abstract of 28385597: "systemically administered", MeSH Male and Mice; no age.
- Abstract of 31809508: ICV delivery in mice lacking MCT8, "TRIAC content increased in the brain".
- Item 7: late start, "myelination was not improved". Triac 400 ng/g/day s.c., n 3 to 4, sex not stated. Item 7 does not name the model.
- Sobetirome "none found" is one route (openFDA NO_MATCH_FOUND).

U5:
- BATCH6 titles show juvenile Triac work in Mct8-deficient mice (PMID 36565029 "Juvenile Stages"; PMID 36555189). Item 7 puts Triac dosing at P1 to P20. Numbers were not read, and BATCH6 only excludes "juvenile wild-type or Wwox-context" values.
- "Unknown" for thyromimetics should read "not found, papers not read".

Not reached: Gomora 2001, PMID 29584714 and the Wang and Mei papers. Items 1, 4, 7, 8 and 11 are judged against the SCI file only.
