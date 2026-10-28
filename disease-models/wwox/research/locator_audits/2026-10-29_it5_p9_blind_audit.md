# Blind audit of card I01, PDK inhibition by dichloroacetate (P9), 2026-10-29

Producer: scientist-d. Auditor: independent subagent; packet and primary sources first. Verdict: quotes and values accurate, no transfer, efficacy or dosing breach; one HIGH defect (cirrhosis glucose sign), two MEDIUM (PDK1 sign-only, glycolysis overshoot) and low ones; producer asked to repair.

# Blind audit, card I01 (PDK inhibition / DCA premise, seizure, glycaemia) - scientist-c

Method: packet read first; each cited source fetched (PubMed efetch abstracts, Europe PMC open JATS for 35328751, 42422765, 36432491, 35730570, 38106446; ClinicalTrials.gov v2 JSON; repo files cited as locators). README read last. Downloads in own scratchpad dir, Python -I. No e-mail, registration, spend or captcha bypass (PMC page for 25012504 returned only a stub; not worked around).

## Per-assertion table
Verdicts: S supported, O overshoot, U undershoot, N not in source, V unverifiable.

| ID | (a) quote/value | (b) scope label | (c) sign | (d) depth | Verdict / note |
|---|---|---|---|---|---|
| DA-001 PDK1 organoid -0.39 | matches comparison doc | COMPUTATIONAL ok | sign-only; doc: inside single-gene null p~0.30 | queried_not_full_read ok | S for value; the assertion row omits "inside the null" (note says only the PDK SET is chance) -> U on caveat, see D2 |
| DA-002 PDK1 hNPC -0.67 | matches (+-0.45, n=1, neurons +0.44) | ok | sign-only; p~0.49 not stated in row | ok | S; same omission |
| DA-003 PDK qPCR up, human fibroblast | quote verbatim from JATS Results | label WWOX_EXPERIMENT_IN_DEE_SYSTEM is allowed by bridge definition (engineered KO cells) but system is non-neural, flagged in context | UP, S | partial ok | S with qualifiers: (i) "knockout" is lentiviral CRISPR polyclonal, WWOX mRNA only ~3x lower, protein ~8.5x lower; (ii) control is scrambled-sgRNA, not "empty vector" (empty Puro-Blank is the OE control; one Results sentence does say "control empty vector cells"); (iii) Methods qPCR list names PDK1, so "isoform not named" is only true of the sentence; (iv) Discussion says PDK mRNA also rose in hypoxia-hyperglycaemia, card says "one condition of four" (Results list names only PFK1/PKM2 there; paper internally inconsistent) |
| DA-004 PDH activity unchanged | wording flag confirmed: normoxia-normoglycaemia sentence says "pyruvate dehydrogenase kinase (PDK) and citrate synthase were not changed"; PDH named unchanged in normoxia-hyper and hypoxia-normo; hypoxia-hyper "no effect on enzymes activity"; Fig 5 caption "Pyruvate Dehydrogenase"; kit is PDH. The locator quote is a truncated prefix ("...activity of pyruvate") of the hypoxia-normoglycaemia sentence, not of the normoxia sentence that carries the flag | ok | NO_CHANGE ok | partial ok | S (minor: truncated locator) |
| DA-005 Pdk1 up, Wwox-null MEF | abstract consistent (HIF1a targets up); sentence on Pdk1 not seen | ok | up plausible | claimed complete_fulltext_read; producer admits bytes absent | V (closed; PMC XML refused). Not contradicted |
| DA-006 hypoglycaemia in null / rescue | abstract of 25012504 "succumb to a lethal hypoglycemia early in life" verbatim, but it is a background sentence (prior work), not a result of that paper. Obeid JATS: EF1a (weak) failed to rescue hypoglycaemia; CMV/CBA rescued early but "not sustained at later stages"; MBP no improvement; hSynI rescued. P10 ~95 vs ~130 and ~10 vs 130 are figure readings | ok | DECREASE S | partial ok | S on promoter statement; U: card omits that strong ubiquitous rescue was transient; V for the two figure values |
| DA-007 lactate up | HK 1.6x, LDH 1.4x, lactate 1.6x (medium), later conditions up (1.3x hypoxia-hyper) | ok | S | ok | S (lactate is culture-medium lactate) |
| DA-008 brain lactate low, 1 patient | ledger DL-BIO-008: PMID 30362252 full text read, MRS "extremely low", HSPG2 confound | ok | S | card says UNKNOWN / INFERENZA; ledger says DATO and full-text read | U on depth/tag (conservative, harmless) |
| DR-001 PDH activity partly restored | abstract: -65% in SE mice, "partially alleviated with DCA", protein -37%, Ser300 +52% not significantly changed by DCA | OTHER_DISEASE ok | S | abstract_only ok | S. "wild-type CD1" strain is not in the abstract: V |
| DR-002 acute flurothyl no latency increase | verbatim | ok | S | ok | S |
| DR-003 6 Hz slightly proconvulsant | verbatim; abstract: DCA lowered total PDH 23% in No-SE mice "which may explain" | ok | S | ok | S |
| DR-004 second-hit latency not restored | verbatim ("not restored by DCA"; "did not have any anti-convulsant effects in the tested models") | ok | S | ok | S. Note: the 2023 review PMC10725694 misstates Durie as DCA "shortening" latency; card correctly follows the abstract |
| DR-005 DCA+pyruvate NeuN up (rat) | CA1 +36.8%, CA3 +21.7%, Sub +16%; PDK2 +83.1%, PDH -62.1%, p-Ser293 +62.3%; treatment 2 h after onset | ok | S | partial ok | S with caveats: PDH "level" by IF/WB, not activity; WB n=3, IF 5 cells; legend n differ from Methods (sham 4 vs 5, seizure 5-7 vs 8); "single agents inactive" is the Discussion citing ref 48, not shown as this paper's own result in text read (design had DCA-only and pyruvate-only arms; figure not read) |
| DR-006 paediatric trial null | 43 patients, no difference in GATE, growth, illness | ok | S | ok | S |
| DR-007 meal lactate down; CSF lactate down | 16651305 and 18411236 verbatim | ok | S | ok | S; "DCA reaches the CNS" is an inference from CSF lactate, drug level in CSF not measured (conflicts with translation.cns_exposure UNKNOWN) -> O (low) |
| DR-008 MELAS neuropathy | 15/15 vs 4/15, 17/19, terminated early | ok | S | ok | S |
| DR-009 nerve conduction, oxalate | verbatim incl. attribution caveat, +22% oxalate | ok | S | ok | S |
| DR-010 fasting glucose -24% | verbatim; "uncontrolled" in note is not in the abstract (N, trivial) | ok | S | ok | S |
| DR-011 minipig | 33.6 vs 50.6 mg/dl, n=5 vs 8, lethality 60% vs 67% | ok | S | ok | S |
| DR-012 septic mouse | verbatim "reversed ... hypoglycemia" (i.p.); body: plasma glucose and lactate LOWER in septic mice; fasting confound acknowledged by authors | ok | S for glucose | ok | S, but note "comparable lactic-acidosis-with-hypoglycaemia state" is wrong, see D1 |
| DR-013 cirrhosis | abstract: DCA decreased plasma lactate ~50%, glucose production 7-9% and plasma glucose 9-14% in BOTH cirrhotic and control subjects; no exaggeration in cirrhosis; clearance 36% | ok | card says NO_CHANGE for glucose production: WRONG sign. It is a modest DECREASE in both groups; the "null" is cirrhosis-vs-control | ok | O/sign defect, see D1 |
| DR-014 PDC fibroblasts | -29% glycolysis in patient cells, no effect in controls, LPR unchanged | ok | S | ok | S; omitted: the 29% excludes one patient with an unusual splicing mutation; six patients, five controls |

Registry facts: ClinicalTrials.gov 27 dichloroacetate intervention records confirmed; NCT02616484 phase 3 active-not-recruiting, NCT06931262 expanded access AVAILABLE, NCT00068913 MELAS (status UNKNOWN), NCT03356457 completed early phase 1. GSTZ1 25-30 fold, 2-fold, 17 children plateau, G6PD neonate case, oxalate +22%, Abdelmalak 2013 (no symptomatic neuropathy, 3 patients had dose reduction) all match abstracts. 1998 review abstract says "hepatotoxicity and neoplasia" (card says "hepatic tumours": slightly beyond abstract). Thiamine/oxalate rat item has no PMID in the card (untraceable, producer admits).

## INFERENZA claims
1. Seizure-secondary PDH restraint: reasonable competing explanation, correctly kept as INFERENZA, but worded "consequence of seizures". Both models are chemoconvulsant status epilepticus injuries (pilocarpine, followed by diazepam; neuron loss in tissue), so the data cannot separate seizure, SE injury, neuron loss or drug exposure; Lee measures protein/phospho levels 1 week out, not activity; Durie is activity but abstract-only. "Documented independent of genotype" is true (wild-type animals) but "consequence of seizures" should read "after chemoconvulsant SE". Low-medium.
2. Glucose-sign contrast: pig (deeper) vs septic mouse (reversed) is stated as context-dependent and unresolved: fair. But the record the card builds on is incomplete or wrong in two places (D1): the cirrhosis paper shows lowering, not a null, so 3 of 4 relevant datasets (625308, 3521930, 10546922) point to lowering and only the mouse sepsis study to reversal, and that reversal arrives with anorexia reversal and a baseline of LOW lactate. The "unresolved" framing is thus tilted toward balance that the sources do not give. Prediction (2) also credits the minipig with "glucose, lactate and alanine fall together"; alanine was not reported in the minipig abstract (alanine fall is from the human 1978 study).
3. Cross-system PDK transcript contrast: card is careful in DA rows (confounded, not a finding about WWOX) but the card prose repeatedly states "PDK1 lower in two human neural systems" and uses it as contradiction ("contradicted in its middle"), while the comparison doc says sign only, both inside single-gene null (p~0.30, 0.49), "the finding is the absence of support, not a demonstrated decrease"; neuron stage is +0.44. Overshoot, see D2.
4. Predictions: both registered in both directions with a stated closing condition and an uninformative-negative clause: adequate. Gaps: prediction 2 is binary (falls below vehicle / does not fall) with no category for the modest fall that cirrhosis and diabetic adults show in non-hypoglycaemic baselines; and it cannot separate hepatic from feeding effects unless intake is measured (card says feeding recorded: ok).
5. Transfer discipline: every non-WWOX row labelled NOT WWOX EVIDENCE, scope OTHER_DISEASE_PRECEDENT, an explicit no-transfer sentence, no dose, route, schedule, efficacy or individual statement found (amounts omitted; "12.5 mg/kg" not printed; the pharmacology paragraph quotes only fold-changes and says no dose). PASS. Residual: "DCA reaches the CNS compartment in children" in the "for" list reads as exposure evidence (translation field says UNKNOWN).

## Defects
- D1 (HIGH for the glucose strand) DR-I01-013 and every restatement (p4_card evidence_against "absent in cirrhotic adults", DR-013 note "a human glucose-kinetics null", README finding 6): the source reports DCA lowered glucose production 7-9% and plasma glucose 9-14% in cirrhotic and healthy subjects alike; only the group difference is null. Direction should be DECREASE (modest), the contrast should read pig down / adults down / mouse sepsis up. Also DR-012 note calls the septic mouse a "comparable lactic-acidosis-with-hypoglycaemia state" but the paper shows plasma lactate LOWER in septic mice (and pyruvate lower); only the minipig had raised lactate. Comparability premise is false.
- D2 (MEDIUM) PDK1 transcript overstated: DA-001/002 rows omit that PDK1 is inside its single-gene null (p~0.30/0.49) and that neurons are +0.44; p4_fields, mechanism, evidence_against and expected_contribution say "PDK1 lower"/"contradicted" in two human neural systems. Should say "lower in sign only, no support for raised, not a demonstrated decrease".
- D3 (MEDIUM) "glycolytic signature robust ... in two human neural transcript systems" (evidence_for, expected_contribution): comparison doc restricts this to LDHA and a hand-picked HIF-type 10-gene set; the broader 19-gene panel is inside null in hNPC and the organoid mean is driven by five genes. README says "robust in three human systems": same overshoot.
- D4 (LOW-MEDIUM) Baryla system described as "knockout versus empty-vector control": it is CRISPR/Cas9 lentiviral knockdown-like (mRNA ~3x lower, protein ~8.5x lower), control scrambled sgRNA; abstract itself says "silenced". PDK1 named in Methods. Fibroblast KO labelled WWOX_EXPERIMENT_IN_DEE_SYSTEM although non-neural, flagged in text; consider WWOX_BIOLOGY_OTHER_CONTEXT for the non-neural lines.
- D5 (LOW) DA-004 locator quote is a truncated sentence from a different condition than the one carrying the PDK/PDH wording flag; quote the normoxia-normoglycaemia sentence for the flag.
- D6 (LOW) DA-006: 2014 abstract sentence is background; ubiquitous-promoter rescue transient; omitted in note.
- D7 (LOW) DR-005: "single agents inactive" is not demonstrated in the text read (Discussion citing another study); Lee sample sizes are inconsistent between Methods and legends; WB n=3.
- D8 (LOW) "DCA reaches the CNS compartment" inferred from CSF lactate; contradicts translation.cns_exposure UNKNOWN.
- D9 (LOW) DA-008 depth/tag understated vs ledger (full text of Davids 2019 read; DATO).
- D10 (LOW) Prediction 2 attributes alanine fall to minipig study; DR-014 omits 29% excludes one patient.

## UNVERIFIABLE
- DA-005 Pdk1 sentence in Wwox-null MEFs (PMID 25012504 full text not obtainable; PMC XML refused, page gave no body).
- Figure values: P10 ~95 vs ~130 (Obeid), ~10 vs ~130 (2014 Fig 1), digoxin figure.
- Durie 2018 beyond abstract (closed): strain, n, statistics, effect sizes; "no replication" claim.
- Stacpoole 2006/2008, Kaufmann 2006 beyond abstract (adverse-event lines, arms).
- Absence claims ("not previously in repository", openFDA no match 2026-10-29): not re-run.
- Thiamine/oxalate rat observation (no PMID given); Lee 2022 figures.

## Producer README: disagreements
1. Finding 6 and card: cirrhosis reported as "no exaggerated inhibition" only; source shows glucose lowered in all (D1).
2. "Glycolytic signature robust in three human systems" (D3).
3. Finding 1 headline "PDK1 lower in both human neural transcript systems" in "datum that decides" paragraph lacks the sign-only/inside-null qualification that the producer's own comparison doc carries (D2).
4. Finding 4 "single agents were inactive" stated as result of the rat paper (D7).
5. "isoform of the human fibroblast qPCR is unknown": Methods lists PDK1 (D4).
6. Finding 3 "documented as a consequence of seizures" (see INFERENZA 1).
7. README is otherwise honest about depths (Durie abstract-only, 25012504 bytes absent, Lee n=3 WB), and I agree with its Durie, paediatric trial, MELAS, minipig, sepsis, PDC-fibroblast readings, with its wording flag, and with the hypoglycaemia/promoter reading.

## Bottom line
Quotes and values are overwhelmingly accurate; the Durie special check passes exactly (partial PDH activity restoration, second-hit latency not restored, slightly proconvulsant in 6 Hz, no anticonvulsant effect). Fix D1 (sign error on cirrhosis, false lactic-acidosis comparability for septic mice) and D2/D3 (transcript overstatement) before the card's INFERENZA about glucose and the PDK transcript contrast is relied on. No transfer-of-evidence, efficacy or dosing breach found.
