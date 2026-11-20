# Blind audit 1 of the unit B packet change: delegate report, verbatim

Fresh legend-delegate, claude-sonnet-5-5, effort high (read back from its transcript). Packet AUDIT_PACKET.md. **IT defect: the anchor fields naming the SCI verified-reading file and the HE sheets were blank in this packet (shell expansion inside the builder), so the delegate could read only the primary papers it could reach; most judgements are UNVERIFIABLE for that reason, not for lack of support.** Persisted by IT before any repair; not edited. Repairs from its notes applied; second audit on AUDIT_PACKET_2.md with the anchors written out.

BLIND AUDIT REPORT, unit B packet (IT59). Verdicts are limited to what I could read. Source: PubMed tools and Europe PMC.

Files read: only AUDIT_PACKET.md. In the packet the anchor fields for the SCI verified reading and the HE sheet are blank, with no file names, so I could not open them. Every judgement on items 1, 2, 4, 7, 8, 11, 12–14 and the HE rows is therefore UNVERIFIABLE here. Scratch (not repository files): /home/desktop/.claude/jobs/96cc479a/tmp/blind_unitb/pmc3401299.xml and p.py.

| # | Verdict | Basis |
|---|---|---|
| U1 brain value, 45 min, i.p., 0.96 mM, dilution unstated | SUPPORTED_WITH_LIMIT | 22315091 Table 3 |
| U1 "about half the dose of the Wwox experiment" | UNVERIFIABLE (Wwox dose not in my anchors) | arithmetic below |
| U1 equilibration within minutes, half-life about 1 h | SUPPORTED | 708147 abstract |
| U1 potency (0.6 mM, >5 mM FLIPR), ChEMBL origins, label | UNVERIFIABLE | no anchor reached |
| U2 | SUPPORTED_WITH_LIMIT | same as U1 brain value |
| U3 Odell Cmax 44.0 ng/mL, plasma, not lowest dose, no unbound or brain value | SUPPORTED_WITH_LIMIT | PMID 38942888 (PMC11502491) |
| U3 six-fold M1, harm paper, juvenile rat, label | UNVERIFIABLE | not reached |
| U4 numbers (3.4–26-fold, seven of eight, about three-fold), late start, labels | UNVERIFIABLE | not reached |
| U4 "papers exist" (titles) | SUPPORTED | 28385597, 31809508 |
| U5 | SUPPORTED_WITH_LIMIT | Odell; scope the parenthetical |

**U1 and U2**
- Table 3 row, verbatim: "ETS (72.3) + saline 134.9 ± 7.73 µg/g". Footnote: "mean ± standard error of the mean (SEM) of at least eight separate brain preparations. Sildenafil and the studied AEDs were administered i.p." Methods: "ETS 45 min … prior to the tests" and "whole brains … homogenized in distilled water (1:2, w:v)".
- The paper expresses the result "in μg/g … of wet tissue". It states no dilution correction, so the packet's "not stated" is right.
- The 134.9 value is the saline co-treated arm. The sildenafil arm was 153.5 ± 7.99, not significant. The statement is faithful to that.
- The paper says "Male albino Swiss mice weighing 24–30 g". It gives no age, so "adult" is an inference from weight. Say "male Swiss mice of 24–30 g".
- The brain was taken "at times chosen to coincide with that scheduled for the PTZ test". "45 minutes" is therefore an inference from the injection schedule. It is reasonable.
- 72.3 mg/kg is the ethosuximide ED50 in the sildenafil arm. The ethosuximide-alone ED50 was 155.8 mg/kg (Table 2), so 72.3 is about 46% of that (72.29/155.8 = 0.464). The packet could add that this dose was sub-median when given alone.
- "About half" holds only if the Wwox dose is roughly 130–170 mg/kg. I did not read that dose.
- Conversion: 134.9 / 141.17 = 0.9556, so 0.96 mmol/kg, or 0.96 mM at 1 g/mL. The molecular weight 141.17 is my own knowledge, not read from any anchor. A homogenate reading uncorrected for the 1:2 w:v dilution could mean a higher tissue value. The statement already says this.
- 708147 abstract, verbatim: "In female rats, ethosuximide had an average half-life of 10 hr, in mice of hardly 1 hr. Concentrations in serum and brain of mice equilibrated within 10 min." The mouse data are a side note in a dog paper. The abstract gives no strain, sex, age or route for the mice. "Abstract-level" is correctly labelled.

**U3 (Odell 2024)**
- The abstract, which is the only place the figure appears, gives "C44.0 ng/mL". The subscript is lost; Methods define Cmax as the observed maximum.
- Doses tested were "0.5, 2, 7.5, or 10 mg per kg", so the PK dose of 7.5 is neither the lowest nor the highest.
- Verbatim: "Fifty mice were treated daily with oral clemastine at the MED, 7.5 mg/kg". Sampling was after the 8th dose. The Methods section is titled "Plasma sample collection", with LC-MS/MS on EDTA plasma. No unbound or brain value was measured.
- The paper says "dosed based on the clemastine fumarate salt". Add the salt basis to the wording.
- The PK animals are not stated to be hypoxia-exposed. "Neonatal mouse" is fine.
- Label: Odell writes "approved in children as young as 12 months old in many countries". The packet's 6–12 years is a different jurisdiction. I did not read its anchor, so name the jurisdiction.

**U4**
- 28385597 abstract: "Several of these systemically administered prodrugs deliver more sobetirome to the brain." This is adult mice.
- 31809508 abstract: "TRIAC content increased in the brain". This is intracerebroventricular delivery in Mct8-KO mice, not a systemic route.
- 36555189 shows early-life TRIAC improving white-matter thinning in Mct8/Oatp1c1 double-knockout mice. I did not find a late-start paper, so that claim is unverified.

**U5**
- The Odell plasma-only reading is right. Odell cites earlier brain-penetration work for clemastine, and 28385597 reports sobetirome brain delivery in adult mice.
- "No brain concentration for either class" must be scoped to neonatal or pup. Unscoped it overstates.

**Routes**
- PMC article page via WebFetch returned a reCAPTCHA, so I stopped that route. The PubMed full-text tool dropped the table cells. Europe PMC fullTextXML worked.
- Not reached: ChEMBL potency rows, the M1 six-fold document, the clemastine harm paper (searches empty), the sobetirome and tiratricol selectivity numbers, and all labels. I report no values for these.
- I did not read delegation_budget.md, because the dispatch forbade other repository files.
