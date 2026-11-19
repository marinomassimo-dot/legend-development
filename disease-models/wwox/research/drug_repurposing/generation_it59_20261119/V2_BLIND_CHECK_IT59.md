# Blind check of SCI's v2 consolidation (ADV-077) by a reader who did not produce it

Non-canonical working note (IT, 2026-11-19). One fresh `legend-delegate` (requested sonnet/medium; read back from the transcript: model ['claude-sonnet-5-5'], effort ['medium']), one pass; the reader's report as delivered, verbatim, below. Five addenda picked by IT (pup brief 9.4, 9.5, 9.7, 9.10; the post-washout lines of the technical brief Addendum 14 and the slice package) and the seven conflicts of the ordering page. IT's summary follows the report.

---

Setup note: the V2 files and originals were not in the /tmp/it56_iso working tree. I read them from development/main. Quotes use file:line of those blobs. Pup = pup brief V1; Tech = EXPERIMENT_BRIEF_V1_1.md; Slice = outreach package.

PART 1

(a) Pup 9.4 (2026-11-18): PRESENT, with one number and one note dropped.
- Orig line 86: "the sizing flag and section 3 on one set of numbers (44 to 79 per arm for log SD 0.6 to 0.8)"; "generalised … stages 4 to 5 with a tonic phase"; "own-vehicle rule"; "no schedule of our own".
- V2 line 3 has "no schedule of our own". V2 line 30 has the stage 4–5 tonic-phase definition. V2 line 47 has the dose-check total with "The pilot decides the dose check first". V2 line 83 has the single definition of "General". V2 line 46 has "A stage that runs in another session carries its own vehicle group".
- Dropped: the original sizing flag said "the arithmetic of this flag is corrected by the dated addendum in section 3". V2 line 22 keeps this as "(Corrected in the ADV-061 paragraph…)".
- Dropped: the original sentence "even then needs about 75 litters across the three knockout arms" is missing from V2 line 46.
- COVERAGE_TABLE says "already in body".
- No withdrawn statement was involved.

(b) Pup 9.5 (2026-11-18, ADV-064): PRESENT.
- Orig line 88: "'diazepam ontogeny' … it was found … rat status epilepticus not stopped at P9 and stopped at P15 and P21; mouse febrile … P11 and not at P14". The other items are confirmed not found "with a stated age".
- V2 line 76 item 3: "diazepam ontogeny was found on blind re-search", with the other items "confirmed with a stated age". V2 line 28 has the P9/P15/P21 and P11/P14 wording.
- The withdrawn "not found" for diazepam is absent. Good.
- Flag: V2 line 28 repeats the "worsened at P11 and not P14" claim and "an agent can change direction between P11 and P14" with no Kasahara caveat. The V2 text two lines earlier (line 26) calls that same study confounded. The original 9.5 had the same unqualified form, and 9.7 only said what stays.

(c) Pup 9.7 (2026-11-18, Kasahara 2019): PRESENT BUT CHANGED (some limits dropped).
- Orig line 92: "'suppressed the worsening' … weakened: at P11 the modulators did not raise the clonic incidence (5 of 5 in saline); the worsening is in latency, threshold temperature and LFP events; bumetanide did not block the latency effect and alone lowered incidence; … 5 of 5 deaths with high-dose diazepam at P11 and P14 and near-normothermia in the co-treatment arms; groups were 4 to 5 mice. No other source supports a P11 to P14 chloride window".
- V2 line 26: "confounded (clonic incidence at P11 not raised, bumetanide did not block the latency effect, 5 of 5 deaths on high-dose diazepam at both ages), … groups of 4 to 5 … no other source supports it".
- The withdrawn sentence "suppressed the worsening" is not in V2.
- Dropped limits: "5 of 5 in saline", "bumetanide alone lowered incidence", "near-normothermia in co-treatment arms", "worsening is in latency, threshold temperature and LFP events".
- COVERAGE_TABLE says "changed" and cites P2 2.2 only.
- V2 does carry the abstract-level statement from 9.6 on diazepam and bumetanide in line 35. That line says "a bumetanide effect on latency was the same in wild type and mutant in one model".

(d) Pup 9.10 (2026-11-19, onset-age round): PRESENT, wording the same.
- Orig line 98: "behavioural spontaneous seizures commonly after postnatal day 12 (Cheng 2020; no EEG); cortical ECoG … from about P14 (a 2026 report; n = 5 per group; nothing was recorded earlier, so onset may be earlier); slice bursting at P13 to P17 (Breton 2021); the null dies at about three to four weeks. No EEG before P14…".
- V2 line 26: same items and numbers.
- The date appears only in COVERAGE_TABLE ("added"), not in the V2 body.
- No correction was involved.

(e) Slice Addendum 14 and the dated lines on post-washout reads: PRESENT BUT CHANGED (weaker, numbers dropped).
- Tech dated line to Addendum 14 (2026-11-18, ADV-063, line 184): "30 minutes is the end of the rebound zone, not clear of it, and the 60-minute read is the clean one; … an optional 45-minute read". It also gives the end dates 25 and 30 min, then 10, 15 and 20 min; a residual of about 1.1 to 1.3 for about 50 to 95 min at tau_w 7200; "the report … was not re-read here".
- Slice dated line (2026-11-18, line 60): "the read at 30 minutes can sit on the tail of a rebound with a long time constant, the 60-minute read is the clean one, and one optional read at about 45 minutes is welcome".
- V2 line 23: "the 30-minute read can sit on the tail, the 60-minute read is the clean one, … optional 45-minute read". V2 adds "the 5-minute read lies inside it, the 15-minute read inside or at its end".
- Changed: V2 uses the weaker slice-package form. It drops "end of the rebound zone, not clear of it". It also drops the date range of the rebound's end, the residual and the "report not re-read" caveat.
- The withdrawn earlier form (Tech line 181, "so the reads at 30, 60 and 120 minutes start after it") is not carried. Good.
- COVERAGE_TABLE: "changed (30 minutes not clear of rebound)". That is stronger than what the V2 body says.

PART 2

1. Sizing: CONFIRMED, but the original calls it a correction, not an open conflict.
- Pup line 12: "four equal cells … at 44 per cell that is about 176 animals … 75 litters". The same line says "(the arithmetic of this flag is corrected by the dated addendum in section 3)".
- Pup line 37: "an interaction contrast needs twice (not four times) … 180 to 320 animals per cell … 700 to 1,300 animals".
- README line 60 (fig7_quant): "needs twice, not four times, the simple-effect n per cell".
- Pup line 34 still says "about four times as many per cell".
- ORDERING_PAGE (line 90) lists both as unresolved, "none chosen". This is less decisive than the originals, which mark the addendum as the correction.

2. Conduction n: PARTLY.
- Tech line 200 (Addendum 20): "callosal conduction latency was measured once, with an inconsistent n in the legend". That line gives no numbers.
- Pup 9.11 (line 100) gives "8 slices from 5 animals for controls, 8 from 6 for the knockout".
- R1 note line 6: "8 slices from 5 animals for controls and 8 slices from 6 … may be a copied n; nothing in the originals decides it".
- So the earlier line says only "inconsistent n", and the number-bearing lines come later. The original lines were not contradictory; the R1 note says the "8 slices from 5" figure was "incomplete".

3. Time to death: CONFIRMED, but the sources differ in line and population.
- Pup line 78: "untreated knockouts die by about day 17 in the comparator's panel".
- Pup line 96 (9.9): "the null dies by about four weeks" (Cheng).
- Pup line 98 (9.10): "three to four weeks".
- Repudi 2021 text (neuron-targeted line): "100% of the N-KO mice died postnatally by 4 weeks".
- The comparator is the AAV9 panel. The originals give no reconciliation.

4. Rat paper year: PARTLY. This is not a conflict of statements; the repository is consistent.
- Suzuki 2009 (Genes Brain Behav, PMID 19500159): serum data. R4 report line 97 says: "28-day-old lde/lde rats had normal levels", "cited to the unread Suzuki 2007".
- Suzuki 2007 (Comp Med 57:360, PMID 17803050): abstract only; reports raised BUN, creatinine and phosphate.
- The glucose first-pass note (line 25) says the 2009 original is not held and Suzuki 2007 is not held either.
- Older analysis files (amygdala_expression_lesion_node_20260922.md, acquisition_wave_20260922.md) call 2007 "the `lde` phenotype primary" and 2009 "the lesion primary". That is the only year confusion I found.

5. Washout reads: CONFIRMED.
- Tech lines 174 and 181: "the 30, 60 and 120 min washout reads"; "Add reads at about 5 and 15 minutes".
- Tech line 184: optional 45 minutes.
- Priors file line 8: "Post-washout window = 30 to 60 min". Priors line 9: "depolarising sag ratio".
- Tech Addendum 13 (line 169) makes sag paired and in mV.
- Slice line 48 states the 30-to-60 window.

6. Cheng 2020 blot age: CONFIRMED.
- Methods (Western blotting): "three genotypes of mice at postnatal day 14".
- Fig 7 legend (c): "Wwox−/− mice at postnatal day 20 … dephosphorylation of GSK3β at Ser9".
- The Fig 6a legend says "day 14 or 20" for DCX.

7. S-HT panels: CONFIRMED.
- Text: "17% of slices from S-HT animals showed bursting (4 of n = 23 slices across 14 animals) and 86% of slices from S-KO … (36 of n = 42 slices across 24 animals)".
- Fig 2 legend: "four slices from three S-HT animals showed bursting (20%), and 36 slices from 20 S-KO animals showed bursting (84%)".
- The legend also differs on S-KO animals (20 against 24).
- Paper: Repudi S, Steinberg DJ, Elazar N, Breton VL, Aquilino MS, et al. "Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects". Brain 2021;144(10):3061–3077, PMID 33914858. Breton is fourth author, so first-author citation is Repudi 2021.
- "Breton 2021" in the slice package is a different paper: Neurobiol Dis 160:105529, PMID 34634460. Calling the S-HT panels "Breton S-HT panels" is therefore wrong. They belong to Repudi 2021, Brain.
- I did not check whether Breton 2021 carries the same panels.

V2 says MORE than its source:
- ORDERING_PAGE, header and conflict 4: ORDERING calls conflict 4 "resolved by SCI" and says the 2009 paper "cites" Suzuki 2007 "for its serum data". Only the dossier-relayed R4 report states that.
- V2 pup brief line 20: "A preventive or early arm cannot be read as a reversal in respect of the E16.5 finding only". The original said an arm cannot be read as a reversal at all, and the correction narrowed that.
- COVERAGE_TABLE row on dated line 2: it says "30 minutes not clear of rebound" while the V2 body is weaker ("can sit on the tail").
- COVERAGE_TABLE section D: "no difference I could not avoid".
- V2 pup brief line 28 repeats the P11-versus-P14 diazepam direction-change claim from 9.5 without the Kasahara confound caveat.

---

## IT's summary (what is demonstrated, what is not)
* **All five addenda are present in v2** (none absent). Three are carried with limits or numbers dropped: 9.7 (Kasahara: the withdrawn 'suppressed the worsening' is gone, but 'saline 5 of 5', 'bumetanide alone lowered incidence', 'near-normothermia' and 'latency, threshold temperature, LFP events' are not carried); the post-washout line (v2 uses the weaker slice-package wording and drops 'end of the rebound zone, not clear of it', the end dates, the residual and 'report not re-read', while COVERAGE_TABLE says 'not clear of rebound': the table is stronger than the body); 9.4 ('about 75 litters across the three knockout arms' missing).
* **One weakened claim is repeated without its caveat:** v2 pup brief line 28 repeats the P11-against-P14 diazepam direction change from 9.5 ('an agent can change direction between P11 and P14') without the Kasahara confound that 9.7 and v2's own line 26 state. A reader of that line is given a stronger statement than the source (SCI's file; correction to be applied by SCI).
* **Conflicts:** 3, 5, 6 and 7 confirmed from the originals; 1 confirmed but the originals mark the later number as a CORRECTION of the earlier one (the ordering page lists it as unresolved; the pup brief line 34 still says 'four times', an internal inconsistency of the original); 2 partly (the earlier line says only 'inconsistent n', the numbers come from later lines); 4 is not a conflict of statements (Suzuki 2009 against 2007 is consistent in the repository; 'resolved' rests on the dossier-relayed R4 report, secondary).
* **Attribution error on the ordering page (conflict 7):** the S-HT numbers (text 4 of 23 slices, 17 percent, and 36 of 42, 86 percent; legend 20 and 84 percent, and 20 against 24 S-KO animals) are in Repudi et al., Brain 2021 (PMID 33914858; Breton is fourth author), not in 'Breton 2021' (Neurobiol Dis 160:105529, PMID 34634460), a different paper that the IT14 note cites for slice electrophysiology. The reader did not check whether Breton 2021 carries the same panels: OPEN.
* **Nothing here asks for a trim** (ADV: no trim without the operator's word); the edits are SCI's to make in copies.
