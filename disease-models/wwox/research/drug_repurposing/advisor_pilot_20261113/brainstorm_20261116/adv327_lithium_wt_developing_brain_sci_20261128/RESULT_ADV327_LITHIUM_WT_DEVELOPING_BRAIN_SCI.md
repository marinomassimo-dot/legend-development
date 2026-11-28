# ADV-327 result: lithium and GSK3-pathway phosphorylation in wild-type developing rodent brain

SCI, 2026-11-28. Hypothesis level. Research literature only; not medical advice; no transfer to WWOX is claimed.
Pre-registration: [`PREREG_ADV327_LITHIUM_WT_DEVELOPING_BRAIN_SCI.md`](PREREG_ADV327_LITHIUM_WT_DEVELOPING_BRAIN_SCI.md), sha256 `417fd957abbfd93bfe073e1460b7fe5d1e53aa0daccddba329ae52f26618dbcf`, frozen 2026-11-28T13:34:30Z (not edited).

## Verdict

**Not decidable at the pre-registered exposure** (acute, at or below 2.5 mmol Li per kg). The lithium-in-wild-type confound stays open.

* One single-dose study in that range meets the inclusion rule (PMID 21364661). It reports no test of the lithium-versus-vehicle contrast and does not state that there is no change.
* Two further studies meet the inclusion rule with three daily doses, each at or below 2.5 mmol per kg (PMID 27057548; PMID 24787352 if its unnamed salt is LiCl). That is repeated exposure, outside the pre-registered "acute" range. One of them states in words that lithium alone did not significantly alter pSer9; neither reports a pairwise test of that contrast.
* Of the pre-registered sites, all three read only GSK3B pSer9. No qualifying readout of beta-catenin pSer33/Ser37 or pThr41, CRMP2 pThr514 or glycogen synthase pSer641 was found (dated, bounded: see "Search").
* Neither pre-registered strong counterexample was met in the acute range: no quantified significant change (against H2), and no study reporting no change after a single dose with a positive control (against H1). PMID 23167932 is not counted there: its 3-week points carry no asterisk and its adults give a positive signal, but its control is untreated and its dose unknown.

## The three records that meet the inclusion rule

Lithium-alone arm against its control. Bar values are readings by eye, not measurements.

| PMID | Animals and exposure | Dose per administration | Time from last dose to brain | Lithium-alone vs control (label) | n | Same antibody detects a change elsewhere |
|---|---|---|---|---|---|---|
| 21364661 | male Wistar rat, P9, single i.p. LiCl; control: not subjected to hypoxia-ischaemia, saline | 2 mmol/kg | 6 h | Fig 2b, "Cont": about 60,000 (vehicle) vs about 69,000 (lithium) OD per ug protein; no test reported for this contrast; not normalised to total GSK3B; parietal cortex with hippocampus | 6 per arm | yes (loss after hypoxia-ischaemia) |
| 27057548 | C57BL/6 mouse, P6 to P8, one i.p. LiCl daily for 3 days; both arms 60% O2 in a chamber 2 h daily | 100 mg/kg (2.36 mmol/kg) | about 2.5 h (derived) | Fig 4d, "Control" 100 vs "Control + lithium" about 103; no test reported for this contrast; hippocampus | 6 per group (unit read as mice) | yes (lower after isoflurane) |
| 24787352 | C57BL/6J mouse, P6 to P8, one i.p. daily for 3 days; both arms 60% O2 | "lithium (100 mg/kg)", salt not named (2.36 mmol/kg if LiCl) | about 3.5 h (derived) | Fig 6B, "Control+Saline" 100 vs "Control+Lithium" about 100; Fig 6E, 100 vs about 94; text: did not significantly alter; no pairwise P; hippocampus | 6 per group | yes (lower after sevoflurane) |

No serum or brain lithium level was found by term search in these records.

## Read-outs that fail the rule but bear on the design

* **PMID 23167932** (Fig 6, "3 weeks", C57Bl/6 mouse, single i.p. dose; n = 3 per time point; control is untreated, not vehicle). pSer9 as percent of untreated, by eye, at 0.5 / 1.0 / 3.0 h: cortex about 93 / 190 / 132; hippocampus about 160 / 210 / 170. No 3-week point carries an asterisk; 12-week adults in the same figure do. The paper prints "4 mg/kg lithium chloride" (0.094 mmol/kg) in methods and legend. The second reader infers that 4 mmol/kg was meant; the paper does not say so, so the dose of this series is unknown. The legend prints 1.5 h where the figure plots 1.0 h.
* **PMID 18190791** (P7 mouse, single 6 mmol/kg, above the range; about 3.75 h): text states no change with lithium alone, "data not shown"; Fig 1A shows a representative lithium-alone lane, but no quantification; n "3 to 5".
* **PMID 32394966** (maternal LiCl 120 mg/kg, 2.83 mmol/kg, at gestational day 17.5; rat brain from fetal samples to P0): the phospho-GSK3B site is not named; higher at 12 and 24 h, not later; unit of n = 3 unclear. The paper is internally inconsistent (fourth time point P0 in the legend and 72 h on the axis; a legend sentence that disagrees with the bars).
* **PMID 22625652** (maternal 0.24% LiCl in drinking water; E17.5 control embryos, pSer9): each treatment's control is set to 100%, so there is no lithium-versus-NaCl value.
* **PMID 17045245** (abstract only): states no significant effect of lithium on Ser9; Young 2008 (PMID 18595723) describes that work as in vitro. It cannot pass and cannot be a negative.

## Search

* Held texts first: 2,408 text files under `files/fulltext`, `files/supplement` and `files/supplements`; 50 hit a broad screen; no qualifying record by term-and-snippet screen (2,408 is the producer's count, which includes text converted from PDFs). The held WWOX paper with a lithium arm (PMID 32000863, Cheng 2020) has no phospho readout under lithium.
* Then PubMed, queries and counts fixed before reading ([`QUERIES_AND_PMIDS.txt`](QUERIES_AND_PMIDS.txt)): 305 and 165 hits, union 366, run 2026-11-28T13:46:58Z. Every record has a screening line ([`SCREENING_PRODUCER.tsv`](SCREENING_PRODUCER.tsv)); most exclusions are rule-based on title, abstract and MeSH, not hand-read.
* Limits: open full text obtained for 107 union records, read in targeted sections or screened by terms, none cover to cover; 50 PMC records returned no body; supplements of the three passing papers were not checked.
* Not obtained after one try per public route: PMID 23533250, 40024338, 29506051, 42152661, 17906685, 29410165, 41856210, 11886446, 17045245. PMID 40024338 (abstract implies a lithium-alone group in neonatal rats; no site or value given) is the most promising open item. Refusals (403, reCAPTCHA) were recorded and not worked around.
* Open question added by the second reader: PMID 11907184 (gestational dietary lithium, rat) was coded as having no in-vivo lithium; it has one, its abstract states no named-site readout, and its full text was not reachable.

## Second reader

Phase A was written and hashed before the producer's rows were opened (sha256 `f438fd449c7a73ace0afea88b1b40c1a2ae9b6a395813620ea84bd2e4f2e36f3`). No PASS or FAIL verdict changed; the seven candidate quotes are present in their sources. Corrections adopted here: "unchanged" for PMID 27057548 and 24787352 is an untested, about equal value; Fig 6 of PMID 23167932 was obtained and read. Recall sample: all 41 records excluded for lack of developing-age wording and every eighth of 229 other non-manual exclusions; no missed readout found in those samples. A separate regex screen of all 366 abstracts raised one open item (PMID 11907184). These were screens, not full reads. A second pass checked the sentences and table cells of this file; its eleven corrections are applied. Files: `SECOND_READER_*.tsv`; the producer's tables are kept as produced.

## Predictions against outcome

| Pre-registered | Observed |
|---|---|
| Passes at any dose: 2 (range 0 to 6) | 3, all pSer9 |
| Passes at or below 2.5 mmol/kg: 0 or 1 | 1 single-dose; 3 if repeated daily doses are counted per dose |
| Direction where a pass exists: pSer9 raised, substrates lowered | no tested direction; no substrate-site pass |
| Not decidable at the anticonvulsant range (lean, 70%) | not decidable |

## What this changes

1. **Same-animal phospho-substrate panel: keep a lithium-treated wild-type arm** (vehicle and lithium, in both genotypes). No study found here allows it to be left out, and none gives a wild-type substrate-site baseline under lithium to borrow.
2. **Design points, as proposals (hypothesis):** fix the sampling time before the run and include an early point (about 1 h): in the 3-week series of PMID 23167932 the point estimates are highest at 1 h, but no peak is established (nothing starred, n = 3, untreated control, dose unknown), and the three qualifying records sampled at about 2.5 to 6 h; measure serum or brain lithium; report each phospho-site over its total protein.
3. **Dose actually covered, against the held experiment:** the held pentylenetetrazole experiment (PMID 32000863, CLAIM 016) gave LiCl 60 mg/kg i.p. **three times within 1 h** (1.4 mmol Li per kg each, about 4.25 cumulative). No developing-brain readout with that schedule was found. The qualifying records give 2 to 2.36 mmol per kg per administration (2.36 for PMID 24787352 only if LiCl), as one dose or one dose daily, so none reproduces it. A wild-type arm for that experiment should use its schedule.
4. **RP-026:** no change of priority follows from this result alone; the item to add is that the wild-type lithium effect on the substrate sites was not found measured in developing (P28 or younger) brain (dated 2026-11-28, the search above). Adult data were not searched as qualifying records.

## Premise error in the pre-registration

The pre-registration and the assignment read "LiCl 60 mg/kg is about 1.4 mmol per kg" as the exposure of the held experiment. The primary's methods state three such injections within 1 h, so the cumulative exposure (about 4.25) is above the pre-registered ceiling of 2.5. The frozen file is not edited and the verdict is reported against it as written; the verdict therefore does not speak to the held experiment's cumulative exposure. Evidence at higher exposure found here is the unshown statement of PMID 18190791 (6 mmol per kg, single), which cannot pass.

## What would decide it

A single-dose, vehicle-controlled series in wild-type P7 to P28 brain at or below 2.5 mmol Li per kg, with per-animal phospho-over-total values at two or more times, a tested lithium-versus-vehicle contrast and a lithium level.

## Addendum (2026-11-28T15:19:57Z): the held sentence has two readings

The Methods sentence of PMID 32000863 is "LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h before PTZ injection"; the Fig 7d legend gives only "LiCl (60 mg/kg)". The text does not say whether 60 mg/kg is the dose of each injection (reading A: about 4.25 mmol Li per kg cumulative) or the total divided over three injections (reading B: about 1.4 cumulative). The "Premise error" section and change 3 above are stated on reading A only. On reading B the pre-registered anchor of 1.4 would be the cumulative exposure, and the verdict would speak to it. The verdict itself (not decidable at the acute range) does not depend on the reading. Neither reading is adopted here; a design that needs the held regimen must state both.
