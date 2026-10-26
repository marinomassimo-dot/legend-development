# Independent verification of the P3A knowledge-contribution trial (scientist-b)

Verifier: scientist-b (did not produce the trial, reference, answers or producer scores).
Object: `disease-models/wwox/research/drug_repurposing/knowledge_contribution_trial_20261027/` (commit 54ae9851).
Non-canonical research-work quality check. Nothing here is efficacy evidence or medical advice. No trial file was edited.
Depth declared per item: figure image opened (Fig. 7), PMC XML text searched, PubMed abstracts retrieved live, Bacq 2024 full text searched.

## 0. Pre-answer ordering and reference hash
- `sha256sum reference.md` = e47a33de...9b8b, equal to the hash in `pre_answer_hashes.txt` (the file lists `out/reference.md`; same bytes).
- Timestamps in the committed tree are all checkout times and prove nothing. The producer's original `out/` directory shows: reference, questions and hash file 22:35:34Z; `answer_a.md` 22:37:42Z, `answer_b.md` 22:38:29Z, `answer_c.md` 22:39:27Z. The three answer file hashes are not in the hash file, so unchanged-since-writing for the answers rests on those mtimes plus the single commit (22:45Z); the reference predating the answers is supported by the mtimes, not cryptographically. Anyone able to touch the files could have rewritten both; this is a process-honesty record, not tamper evidence.
- Independent leak check: answer A (external only) contains no text from the reference; B and C cite local records, not the trial directory (they state so; consistent with their text).

## 1. Decisive: Fig. 7d of PMID 32000863 (lithium in wild type) - SUPPORTED
Source: `files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png` (opened and viewed) and `PMID32000863_Cheng2020_PMC.xml`.
- Fig. 7d has three rows (+/+, +/-, -/-), each PTZ versus PTZ + LiCl, each with the significance mark `****` between the two curves: PTZ N=12 vs LiCl N=8 (+/+), N=12 vs 12 (+/-), N=6 vs 7 (-/-). In +/+ the PTZ curve peaks near stage 1.2 and the LiCl curve sits near 0 to 0.3; in -/- PTZ peaks near 3.5 and LiCl near 1.3, then near 0.
- The legend and Results text name only Wwox-/- ("suppressed PTZ-induced seizure activity in Wwox-/- mice"); the abstract likewise. The wild-type and heterozygous panels are visible only in the figure. So the B/C reading "lithium suppressed PTZ seizures in all three genotypes, wild type included" is correct and is a figure-level correction of the text.
- Corollary in the same figure, Fig. 7b (ethosuximide): n.s. in +/+ and +/-, *** in -/-. The authors' Discussion says lithium's efficacy is "better than" ethosuximide in Wwox-/-; the figure shows ethosuximide with a genotype pattern and lithium without one.
- Limits of that reading (keep both sides): wild-type baseline severity is at floor (stage about 1), so a visible effect there is small in absolute terms; no genotype-by-treatment interaction test is reported. B's phrase "failed specificity test" is slightly stronger than the data: the figure shows specificity was not demonstrated (and no evidence of genotype specificity in the plotted effect), not that a test was designed and failed. C's "acts as a general anticonvulsant" is the same step. "Does not establish a WWOX-specific rescue" (B's own conclusion, C's Q3) is exactly right.
- Consequence for scores. Verdict is not OVERSHOOT, so B and C keep 5.1 and 5.2 at 1. Reference item 5.2 should be strict about it: required content = non-selective single compound AND no genotype contrast shown (wild type also suppressed, Fig. 7d). Under the stricter item A (abstract-only, never saw the wild-type panels) drops from 1 to 0.5 (non-selectivity named, genotype specificity not addressed); B and C stay at 1. Lithium case totals: A 3.5 (3.0 strict), B 3.5, C 3.0.
- Supporting nuance (not scored): the Ser9 densitometry (Fig. 7c) is one lane per genotype and region, no replicates drawn; the local record's NOT_TESTED label matches what the image shows.

## 2. Abstract-level reference items against PubMed abstracts (retrieved live)
| Item | Reference wording | Abstract says | Verdict |
|---|---|---|---|
| 1.4 GC 24146979 | GCN2 deletion in 5XFAD aggravates PERK/ATF4/BACE1/Abeta | GCN2-/- and +/- "aggravate rather than suppress" BACE1 and ATF4 elevations, exacerbate Abeta and plaques, and overactivate the PERK pathway in 5XFAD only | SUPPORTED |
| 1.4 SI 23741617 | ISRIB "toxic under chronic PERK activation" | ISRIB "reduces the viability of cells subjected to PERK-activation by chronic endoplasmic reticulum stress"; also enhances memory in mice | OVERSHOOT in the item name ("toxic"); the fact (reduced viability under chronic ER stress, in cells) is right. Reword as "reduces viability of cells under chronic PERK activation". A tool-based condition could not be penalised for not calling this "toxicity". |
| 2.2 SA 25792327 | stiripentol is an LDH inhibitor; clinically used antiepileptic | "stiripentol, a clinically used antiepileptic drug, is an LDH inhibitor"; LDH inhibition suppressed seizures in a mouse model | SUPPORTED. Abstract gives no potency; the item correctly asks none. |
| 3.3 DC 16476929 | DCA 25 mg/kg/day in MELAS: neuropathy, trial terminated, no benefit detected | 25 mg/kg/day, 30 patients; 17 of 19 discontinuations for new or worse peripheral neuropathy; terminated early; GATE not different; authors "unable to detect any beneficial effect" | SUPPORTED. "No benefit detected" is not "no benefit": the abstract says neuropathy overshadows assessment; the item wording is acceptable but should not be read as efficacy-negative. |
| 4.1 WO 36537114 | 3 of 5 WOREE epilepsy "responded" to KD; uncontrolled | Abstract: "epilepsy that responded to a ketogenic diet in three patients" among five; full text (local SG chunks): patients 1, 2 and 4 "notably improved seizure control"; authors say "premature to assert" benefit | SUPPORTED. Response is not quantified; the full text also says two of the five were previously published. |
| 5.3 G1 30237424 | decreasing GSK-3 activity (DN or inhibitors) worsened seizure severity/damage | Yes ("surprisingly ... also exacerbated hippocampal damage and increased seizure severity"); but the paper is bidirectional: GSK-3beta overexpression also exacerbated neurodegeneration; kainate-amygdala status epilepticus, adult | SUPPORTED, incomplete: the item omits that overexpression was also harmful and that the model is adult status epilepticus, not a chemoconvulsant threshold test or a developmental model |
| 5.3 G2 35253420 | neuronal GSK-3beta-/- mice more susceptible to 6 Hz seizures | The abstract states the contrast with a lost superscript ("compared to GSK-3beta [..] mice, neuronal GSK-3beta [..] mice show increased susceptibility"); the comparator is not recoverable from the abstract text; TCS2002 acutely anticonvulsant; OE mice less susceptible but kindle faster | PARTLY UNVERIFIED from the abstract alone. Direction (loss increases susceptibility) is the natural reading but should be confirmed in full text before it carries a score. Acute-inhibitor-vs-sustained-loss contrast (item 5.4) is explicit in the abstract. |

Net: no abstract-level item is falsified; one wording overshoot (ISRIB "toxic"); one item (G2) rests on an abstract with a garbled comparator. Since nobody retrieved 5.3 (all three score 0), the G2 uncertainty moves no score.

## 3. Independent re-scoring (from the answer files and the reference as written)
Method: I read answers A, B and C case by case against the reference items. Half credits are explained only where I differ or could differ.

| Item | A | B | C | Note |
|---|---|---|---|---|
| 1.1 | 1 | 1 | 1 | |
| 1.2 | 1 | 1 | 1 | |
| 1.3 | 0.5 | 1 | 1 | A: "fly Abeta-background" but not the absence without it |
| 1.4 | 0 | 0.5 | 0.5 | Fair but generous for B/C: none retrieved GC/SI or the OE dissociation. B/C credit rests on "ISR may be adaptive" plus local negatives (ALS eIF2B activator trial, opposite-sign organoid transcript). A also writes "ISR can be adaptive" unsourced. Strict reading (GC/SI or LC dissociation only) gives 0/0/0; I keep 0.5 for B/C because they bring sourced, locally held counter-evidence to the same point, and report the 0-sensitivity below. |
| 1.5 | 1 | 1 | 1 | |
| 1.6 | 1 | 1 | 1 | |
| 2.1 | 0.5 | 1 | 1 | A has the fly rescue but not the interaction dependence |
| 2.2 | 0.5 | 1 | 1 | A names no source for stiripentol-LDH (references not opened); C has Sada abstract |
| 2.3 | 0.5 | 1 | 1 | B and C: partial rescue, drug vs knockdown, other targets. Neither cites the Wwox-OE dissociation in C2; the rubric lists it among several limits, so 1 is fair, 0.75 would also be defensible |
| 2.4 | 1 | 1 | 1 | |
| 2.5 | 1 | 1 | 1 | |
| 3.1 | 1 | 1 | 1 | |
| 3.2 | 1 | 1 | 1 | |
| 3.3 | 0 | 0.5 | 1 | C: retrieved PMID 23611579 (long-term DCA, modest nerve-conduction decrease, no symptomatic neuropathy) = "equivalent primary DCA toxicity evidence"; it did not open the MELAS RCT (cited via the local map). I accept 1 under "or equivalent", noting that this primary is milder than the reference's DC. B: card statement only, no primary: 0.5 fair |
| 3.4 | 0 | 0 | 0 | agreed; no answer says the lactate rise may be adaptive. Fair item (LC: ATP unchanged) |
| 3.5 | 0 | 1 | 1 | see section 4 |
| 3.6 | 1 | 1 | 1 | |
| 4.1 | 1 | 0.5 | 1 | see section 5 |
| 4.2 | 1 | 1 | 1 | |
| 4.3 | 1 | 1 | 1 | |
| 4.4 | 1 | 1 | 1 | |
| 5.1 | 1 | 1 | 1 | |
| 5.2 | 1 | 1 | 1 | as written; stricter item (section 1): A 0.5 |
| 5.3 | 0 | 0 | 0 | agreed |
| 5.4 | 0.5 | 0.5 | 0 | A: "single acute PTZ endpoint, no chronic data", proposes chronic endpoint; B: developmental-window GSK3beta2 risk and a dose-by-timing series. Neither makes the G2 acute-vs-sustained distinction; 0.5 is the most that is fair, and generous for A. C: none, 0 |
| Case total (max 26) | 18.5 | 22.0 | 22.5 | identical to the producer's totals |
| X.1 to X.4 | 4 | 4 | 4 | X.3 not independently rerun for all 24 PMIDs; the seven reference PMIDs I fetched exist and match their descriptions; the one A citation flagged as weakly relevant (35047994) is a relevance, not an existence, issue |
| Total (max 30) | 22.5 | 26.0 | 26.5 | agrees with scoring.md |

Sensitivity (all from my table):
- Drop 3.5 (section 4): case max 25, totals max 29: A 18.5 / 22.5, B 21.0 / 25.0, C 21.5 / 25.5. B over A: 2.5 case points (was 3.5); C over B: 0.5.
- Also strict 1.4 (0/0/0): A 18.5, B 20.5, C 21.0 on 25. B over A: 2.0.
- Also strict 5.2 (A 0.5): A 18.0; B over A: 2.5 again.
- Lithium case under a correction in the opposite direction (producer's fear that B/C "over-read"): none; B and C are correct, so no lithium score falls.
- Ranking A < B <= C is stable under every variant; the size of the A-to-B gap (2 to 3.5 of 25 to 26) is inside the n = 5, one-run, one-rubric noise the README already concedes.

The four items nobody met: 3.4, 5.3 fair and unmet by all three. 1.4 partial (above). 3.3 for A is a true miss. The half-credit items 1.4, 2.1, 2.3, 3.3, 5.4 are fair within plus or minus 0.25 per cell; 1.4 for B/C is the only one I consider generous, 2.3 for B/C marginally generous.

## 4. Item 3.5 (PDK1/PDPK1): contaminated, drop it
- README contamination point 2 states the producer read `lucas_clarke_followup_20261026/README.md` (which documents the PDK1/PDPK1 collision, the empty DGIdb/Open Targets rows for eIF2B activators and "no Wnt/GSK3 premise") before writing the reference, and wrote 3.5 and the ISRIB items after seeing it. Item 3.5 therefore encodes a finding of the local repository, not a primary-source fact; it cannot discriminate local knowledge from external tool use without presupposing the local result. Its source (HGNC) is cited, but the choice of that trap came from the local work.
- Direction of bias: rewards B and C (B met it from its card, C from live ChEMBL/DGIdb checks; A never saw "PDK1" collide because it queried PDK2/CHEMBL3861). The item also measures something real (a PDK1 query does return PDPK1 first in ChEMBL and DGIdb, C confirmed it live), so keep it as an observation, not a score.
- Recommendation: drop 3.5 from the score (A 22.5, B 25.0, C 25.5 of 29, as the README already computes). The README says the ISRIB items were also written after seeing that page; the only ISRIB-specific wording I can locate in the reference is in 1.4 (the "ISRIB toxic" source SI), where no condition earned full credit, so it moves no between-condition gap.

## 5. Ketogenic datum "B: 3 tried, 1 continued" versus PMID 36537114 - no conflict, different cohorts
- 36537114 is Chong et al. 2022/23 (Am J Med Genet A), five WOREE patients; "responded to a ketogenic diet in three" (patients 1, 2, 4 per the full text).
- B's datum is a different paper: Oliver et al. 2023, Epilepsia, PMID 36779245, a 13-patient WWOX-DEE cohort (DOI 10.1111/epi.17542): "Only 1 of 3 individuals who started the ketogenic diet continued it" (verified in the deepdive manifest PMID36779245.json entry and the commit candidate CC-20261019-SCIENTIST-B-GOLD-CLINICAL-01). B correctly attributed it to "Oliver 2023" and described it as a continuation pattern, not efficacy, but never mentions the Chong series.
- Therefore B's 0.5 on 4.1 is fair (a human KD observation in WOREE/WWOX-DEE, uncontrolled, but not the reference's source and without the "3 of 5 responded" datum). Keep 0.5.
- C made an error not scored by the producer: it treated the abstract ("responded in three of five", Chong) and the local map ("tried in 3, continued in 1", Oliver) as one discrepancy about the same series and recommended a follow-up full-text read to resolve it. They are two cohorts with different endpoints (response reported by authors vs continuation) and are compatible. This is a false disagreement flagged by C, not a resolution failure: scoring.md's "Beyond the rubric" praise of C flagging "KD response vs continuation" as one of three local-versus-external disagreements should be downgraded to "one real (lithium) and one apparent-but-spurious (KD)". C's 4.1 stays 1, but X.2 (evidence classes labelled apart) is mildly weakened for C.
- A side finding the trial missed: the Chong full text itself says the authors consider benefit premature to assert; and the abstract-level 4.1 reading is consistent.

## 6. Stiripentol potency sources versus the locator audits
Compared B's C2 account with `2026-10-27_PMID39769031_blind_audit.md`, `_reaudit.md`, `_reaudit2.md` and with Bacq 2024 (`files/fulltext/PMID38443647_Bacq2024_PMC_r2.xml`, searched).
- Bacq 2024 (38443647): "the effective concentrations on the LDH target (42-500 uM) are globally higher than therapeutic concentrations"; free brain/hepatic concentrations 0.2 to 1 uM; ranking "GABAA potentiation > ion channels >> attenuation of energy metabolism or LDH activity"; "high concentrations (500 uM) of STP were needed, suggesting that other MoAs were involved". B's account is SUPPORTED. Its "in-vitro LDH-inhibiting concentrations ... at or above total plasma levels" is a slight shorthand of "globally higher than therapeutic concentrations" with a nuance (the same Table includes 42-427 uM oxalate-synthesis values, which in a liver context are reached); not distorting.
- Rico-Molina 2024 (39769031) per the second re-audit: stiripentol rows are single-concentration (500 uM, n = 4; 9.9, 34, 38 percent; IC50 ">500"); fitted IC50s (101.7 to 213.7 uM) are for the analogues. B's "single-concentration measurements ... IC50 is a bound, not a fitted value" for the stiripentol rows is SUPPORTED. B's "racemate about a tenth, enantiomers about a third each" matches the re-audit (10 percent racemate, 34 and 38 enantiomers).
- B's DR-E02-006 summary ("viability falls at tens of micromolar while lysate LDH activity falls significantly only at hundreds; complex I inhibited directly and fast"): the re-audit finds the card row SUPPORTED with two caveats: the lysate leg is weaker than implied (reversible inhibitor diluted at lysis), and the row omits the Guyon 2022 lactate-production fall of about 50 percent at 500 uM. B repeats the row, so B inherits both caveats; "Cellular effects are therefore not attributable to LDH" is stronger than the card's own "not attributable to LDH alone" and the re-audit's "at least a partial role of LDH" in Yadav 2026. Mild OVERSHOOT in B's wording; the card is fine.
- Also noted in the audit chain: the note-2.1 heading was an OVERSHOOT ("none gives a stiripentol potency" over-generalised "single-concentration"); B's wording follows the repaired claim ("only single-concentration data exist" for stiripentol), which is correct for the stiripentol rows only.
- Overall: the potency limit B alone put on stiripentol is well sourced; it is also the claim most exposed to reviewer correction (reversible-inhibitor and lactate-fall caveats).

## 7. README limits: are they stated without overclaiming?
Mostly yes. Checks:
- n = 5, one run per condition, one producer-scorer, same-model subagents, rubric overlapping the cards, abstract-depth for seven of nine sources, "C-over-B gap (0.5) is not a finding": all stated, correct, and in the "Cannot" paragraph.
- "+3.5 case points of 26 for B over A" and "local the larger single contribution on this rubric": defensible as a descriptive statement on this rubric, but after dropping 3.5 it is +2.5 of 25 and after strict 1.4 about +2; the README presents the 3.5 figure beside the 3.5 contaminated item. Recommend quoting "+2 to +3.5 depending on rubric choices".
- "Complementary" reading: C's 0.5 edge over B and the specific external contributions (identifier checks, DCA safety paper, Chong series) support a qualitative statement only; C's flagged "disagreements" included one false one (section 5).
- "Transcript check: A made no repository read; B made no network query": consistent with the answer run logs (A: adapters and PubMed; B: 17 calls, no network); not re-verified against raw transcripts by me.
- Three omissions that would tighten the limits: (i) the reference's two full-text sources were both chosen by the same actor who knew the local conclusions (the second contamination point is stated, but "was written after reading the local follow-up README" also affects item 1.x selection beyond 3.5); (ii) rubric items 5.1 and 5.2 were written from a text that omits the wild-type panels (section 1), so the "gold" for the lithium case under-specified the primary source; (iii) the item 4.1 gold cites Chong 2022/23 while the local record's KD datum comes from Oliver 2023, so B's miss is partly a rubric-source coupling, not a retrieval failure.
- No claim of efficacy, ranking of candidates or general superiority is made; transfer-error count 0/0/0 stands.

## 8. Findings to act on
1. Fig. 7d: wild-type and heterozygous panels show LiCl suppression (****); B/C correct, reference 5.2 to be tightened (A 0.5 under the stricter item). No lithium score drops.
2. Drop item 3.5 from the headline total; treat the A/B gap as 2 to 3.5 of 25 to 26, rank stable.
3. B's "3 tried, 1 continued" is Oliver 2023 (36779245), not a conflict with Chong (36537114); C's "discrepancy" is spurious.
4. Reword the 1.4 SI item (reduces viability under chronic PERK activation, not "toxic").
5. G2 (35253420) needs a full-text check before carrying score weight; none was awarded.
6. B's stiripentol "not attributable to LDH" should read "not attributable to LDH alone" (re-audit).

Not done: raw subagent transcripts were not re-read; the 24 PMIDs spot-checked by the producer were not re-run; full texts of 36537114 (other than the Scholar Gateway text), 30237424 and 35253420 were not read beyond abstracts.
