# Blind audit, INV-05 narrow comparison (nmda_composition_discrim_20261109), verifier nc-v

Date 2026-11-09. Read before writing verdicts: `VERIFIER_BRIEF.md`, `verify/items.md`, `output/*.tsv`, `output/receipts/*`. Not read before verdicts: `output/phase_note.md`, `README.md`, `consumer_delta.md`. No gate, lint or test was run; nothing outside `verify/` was written. Claims placed for 24607230, 26185009, 30946007, 7901753, 9400004, 11182088 and 40994429 (actor `nc-v`).

Routes and depth (mine). Plain curl, default user agent only.
- 24607230 (Hansen 2014): PMC3957490 text and XML from the public open-data bucket (Results, Discussion, Experimental Procedures stub, Tables 1-2, all figure legends); Fig 3 viewed (PMC figure blob via the PMC figure page, since the bucket has no image for this record). Fig 2 not viewed (checked against Table 1 and the Fig 2 legend only). Supplement not reached (the bucket lists only json, txt, xml).
- 26185009 (Mierau 2016): PMC4670611 text and XML from the bucket; Methods, Results, Discussion, Tables 1 and 2, legends. Fig 4 image not re-viewed (Table 2 carries the numbers).
- 30946007 (Koster 2019): PMC6464704 text from the bucket; Results, Discussion, Methods paragraph, Fig 3 legend; Fig 3 image viewed from the bucket.
- 40994429 (radiprodil, D10/D11): PMC12677382 text and XML from the bucket; Methods (oocyte paragraph), Results (triheteromer, time course), Table 1, Discussion. Not in the original brief for this package but D10 was "carried, not reopened", so I opened it.
- 9400004, 7901753, 11182088: abstracts through the PubMed tool. Publisher pages not re-attempted (the producer recorded a bot check; I did not retry).
- D12 re-runs: Europe PMC REST (three new strings), PubMed tool (one string), abstracts of four candidates. PMC article page of 39406518 returned a "Checking your browser" page: recorded unreachable, not retried by another route; the bucket text for that record is a 302-byte stub and the Europe PMC full-text route returned HTTP 500.

---

## A. Verdicts per proposition

| Item | Verdict | Depth I read | Reason |
|---|---|---|---|
| D01 | SUPPORTED | Results, Table 1, Fig 3 (viewed), Fig 3 legend | Text: wt 2B/2B IC50 72 +/- 8 nM, maximal inhibition 88 +/- 2 percent (N = 8); wt 2A/2A "insensitive to 3 uM ifenprodil". Table 1 row identical (also 2BAC1/2BAC2 71 nM, 88). Fig 3A/B legend: 100 uM glutamate plus 50 uM glycine; Results: -40 mV. Rat cDNA, oocytes. pH for this series not stated in the text (producer correct). |
| D02 | SUPPORTED | same | Triheteromer IC50 450 +/- 30 nM, maximal inhibition 32 +/- 1 percent (N = 16); CP-101,606 29 +/- 2 percent, IC50 220 nM (Table 1). Fig 3B/C plateau about 68-70 percent residual (viewed; matches). Escape current "between 3-7%" (Fig 1E text); HEK293 2.5 uM ifenprodil 36 +/- 1 percent (N = 6). Tags are leucine-zipper (GABAB1/GABAB2) plus KKXX retention motifs: producer's wording correct. |
| D03 | SUPPORTED | same, Fig 3D-E viewed | 32 to 50 percent (ifenprodil, N 16 and 8) and 29 to 58 percent (CP-101,606); wt 2B/2B maxima unchanged (88 to 88; 89 to 90, Table 1). Fig 3D plateau about 52, 3E about 43. "Tonic Zn2+ in slice not measured in any source read": true of the sources read. |
| D04 | SUPPORTED, one correction | Results, Table 1, Fig 2 legend | TCN-201 370 +/- 30 nM, 91 +/- 1 percent (2A/2A); triheteromer 1350 +/- 130 nM, 72 +/- 4 percent; "did not display any activity at wild type 2B/2B". **Correction:** the producer writes "glycine level for this series not stated in the text read". It is stated: Fig 2 legend, "100 uM glutamate plus 3 uM glycine" for panel A (TCN-201). That is a low co-agonist level, which matters for transfer of the 72 and 91 percent maxima to a slice (competitive-like glycine dependence is carried from 22553026). |
| D05 | SUPPORTED (abstract level only) | Abstract (PubMed tool) | IC50 0.009 uM (NR1C & NR2B) and 52 uM (NR1C & NR2A), ">5000-fold"; MK-801 binding biphasic, about 60 percent high-affinity, IC50 0.003 uM; "Like ifenprodil, Ro 25-6981 blocked NMDA receptor subtypes in an activity-dependent manner". Producer's labelling as abstract level, not a verification, is correct. Maximum inhibition, agonist levels, potential, pH are indeed not in the abstract. |
| D06 | SUPPORTED (abstract level only) | Abstract | 0.34 uM vs 146 uM, "400-fold", -70 mV, glycine reduces 1 uM ifenprodil effect at NR1A/NR2B, "onset and recovery ... were not activity dependent". The 72 vs 340 nM spread is 4.7-fold ("about five-fold" fine). The "disagreement" with D05 is the producer's INFERENZA: the two abstracts may use "activity dependent" for different operational tests (onset or recovery rate in Williams; use-dependence of block in Fischer), so it is better written as "different wording, not shown to be a conflict". Williams 1993 is an abstract; `comparison.tsv` H_GluN2B calls it one of "two primary sources" (see C). |
| D07 | SUPPORTED on the numbers; label and depth must change | Methods, Results, Tables 1-2, Fig 4 legend | **Table 2 of the PMC text gives the numbers the producer read off a raster bar graph.** WT pyramidal N/A ratio: P15 1.18 +/- 0.08 (n = 15) control vs 0.83 +/- 0.09 (n = 12) ifenprodil, marked ** (P < 0.01); P30 0.96 +/- 0.09 (n = 9) vs 0.81 +/- 0.08 (n = 13), n.s.; P45 0.92 +/- 0.05 (n = 13) vs 0.82 +/- 0.05 (n = 14), n.s. Producer's raster values (1.18/0.82, 0.96/0.80, 0.92/0.82) are within 0.01 of the table. The ratio change at P15 is 29.7 percent, but control and drug are different cell groups (n 15 vs 12, drug in the bath 40 min or more before recording), so the 30 percent has no pairwise error; with the table SEMs a propagated uncertainty is about +/-10 percentage points (my arithmetic, INFERENZA). Species, sex, ages, room temperature, Mg2+ 1.3 mM, 5 uM bicuculline, CsCl pipette with 5 mM QX-314, layer 4 stimulation, 0 to +40 mV slope: all as stated. Receipt FTR-20261109-26185009-71 says `tables: not_read`, which is why the table was missed (see E). |
| D08 | SUPPORTED, caveats to add | Results, Discussion, Methods, Fig 3 legend, Fig 3 (viewed) | Fig 3E WT per-cell points about 91, 83, 76, 74, 72, 70, 70 percent of baseline (7 lines; legend n = 7 cells, 4 mice), significance mark ** for WT; baseline tau_w about 185 ms (Fig 3C). P42, V1 layer II/III, 30 C, +50 mV, CNQX 10 uM, bicuculline 60 uM, SCH 50911, layer IV stimulation: correct. The authors' triheteromer reading and the Stroebel 2018 citation: as the producer says. Additions: (i) no vehicle or time-matched control group is shown for the 30 min Ro 25-6981 infusion, so a part of the tau_w fall could be time-dependent change in the recording (my INFERENZA, not stated in the paper); (ii) the "recording Mg2+ not stated" remark: the Methods give a slicing aCSF with MgCl2 4 mM and CaCl2 0.5 mM and say sections were then held and perfused in "aCSF at 30 C" without a separate recording composition, so Mg2+ of the recording medium is unresolved, not absent from the Methods. |
| D09 | SUPPORTED as arithmetic; caveats incomplete | Table 1, Fig 3, Fig 4A/Table 2 | The envelope 0.88 x f(2B) + 0.32 x f(tri), or 0.50 x f(tri) with 300 nM Zn2+, follows from Table 1. "Lies inside the envelope and does not validate it" is correct. Not stated by the producer: (a) the 32 percent includes 3-7 percent escaped diheteromer current (Fig 1E), so a pure-triheteromer ceiling is probably a few points lower (INFERENZA); (b) the P15 30 percent has about +/-10 pp uncertainty (see D07), so it would be inside the envelope for any f(tri) from 0 to 1 for plausible f(2B) mixtures; it carries almost no information about the share. |
| D10 | PARTLY | 40994429 Table 1, Methods, time-course paragraph | **Species mix-up.** Table 1: Human GluN1-1a/GluN2B 91 +/- 1.0 percent (n = 13); **Rat** GluN1-1a/GluN2B 82 +/- 9 (n = 16); rat GluN1-1b/GluN2B 83 +/- 3 (n = 19); **rat** GluN1-1a/GluN2AC1/GluN2BC2 45 +/- 10 percent (n = 8, IC50 0.091 uM). The triheteromer value is rat, so the like-for-like contrast is 82 (or 83) vs 45, not 91 vs 45. Washout: "only a small amount of current was recovered (4.7 +/- 1.2%) after 3 minutes" (verified). Conditions: 100 uM glutamate plus 30 uM glycine (verified) and the oocyte bath contained 10 uM EDTA to chelate Zn2+ (Methods, not in the producer's record). Triheteromer n = 8 with SEM 10 means "45" is poorly constrained; "shared ceiling" across three compounds is fair as a range 29-45 percent but each value has its own SE and conditions (Zn chelated here; Zn2+ context of Hansen's baseline not stated in the text I read). |
| D11 | SUPPORTED | Hansen Introduction ("selectively bind at the interface between GluN1 and GluN2B ATDs", ifenprodil and CP-101,606); 40994429 Results/Discussion | Radiprodil site now verified: "Radiprodil binds at the subunit interface between the GluN1 and GluN2B NTDs", mode of hydrophobic contacts more similar to ifenprodil than to EU93-31 (crystal structure, GluN1b-GluN2B NTD, 2.74 A). The Ro 25-6981 site statement stays carried/unverified, as the producer says. Inference (a second NAM controls chemotype, not composition) follows. |
| D12 | PARTLY | Re-run queries (below) | The statement is literally true of what the producer reached, but the perimeter was thin (first 12-15 titles of 33-51 hits) and my re-runs surface two L2/3 papers at the target ages that use ifenprodil or Ro 25-6981 and that the producer did not name. See D. |

Counts: 12 propositions; SUPPORTED 10 (four with required corrections or additions: D04, D07, D08, D09); PARTLY 2 (D10, D12); NOT SUPPORTED 0; UNVERIFIABLE 0 (D05, D06 are verified only as the abstracts they claim to be).

---

## B. Species, cell, age, preparation, exposure, readout

- D01-D04: recombinant (rat cDNA, oocytes, HEK), labelled as such; nowhere written as native tissue. Good. Hold: room-temperature oocyte maxima vs a 35 C slice is named (comparison H_state/M-N6) only as "temperature recorded", not as a transfer limit on the NAM ceiling (see C, missed measurement 4).
- D07 is correctly labelled "transfer from other system" and "conductance ratio". Missing: the NMDAR component is read "at the time point after the current at -100 mV had decayed to less than 5 percent of its peak" (Methods), i.e. late in the EPSC, so ifenprodil's effect on the ratio mixes amplitude with decay-time shortening (Table 1: WT pyramidal P15 decay tau 116 +/- 8 ms control vs 76 +/- 10 ms ifenprodil). The "about 30 percent" is therefore an N/A-ratio change at a late time point, not a peak-amplitude fraction removed (my reading, INFERENZA). Ifenprodil was in the bath for 40+ min, so equilibration is not an issue there.
- D08 reads decay time only, labelled correctly. The decay shortening of about 23 percent (mean) is not an amplitude fraction; the producer says so.
- D10: human vs rat mixed (above).
- D05/D06: abstract statements are not carried as mechanism verification. Correct.
- comparison.tsv H_GluN2B cell 3: "IC50 spans 72-340 nM for ifenprodil on GluN2B across two primary sources". Williams 1993 was read as an abstract only; "two primary sources" overstates, and assay differences listed (-40 vs -70 mV, glycine) are partly unread for Williams (glycine level in Williams unknown to the producer).

## C. The comparison

1. **Partial-removal NAM against d-APV at matched percent removed.** Interpretable only over 0 to the NAM's own ceiling, and the producer says so (bounds, not fails). Correct. Weakness: the x-axis (percent of isolated NMDAR EPSC removed) is measured on evoked synaptic EPSCs in separate slices (M-N1, M-N2, M-N7), while the burst is driven by whatever pool is active during the burst. For a non-competitive NAM the percent removed is roughly independent of glutamate; for competitive d-APV it is not. The producer notes this (IPOTESI) and requires the d-APV percent "at the time of the burst". But no measurement in `new_measurements.tsv` can deliver that: an evoked EPSC under a brief high-glutamate transient will understate d-APV's block of a pool exposed to lower or slower glutamate (extrasynaptic, spillover). The d-APV axis is therefore less trustworthy than the NAM axis, so "coincident or left-shifted" is not read on a common axis. This is a reasoning gap in the cell, not an error in a source.
2. **Left-shifted, coincident, plateau-limited.** Mostly right. Two defects: (a) in H_total_gain, "outcome_strengthens" lists "a d-APV curve with a sharp threshold at x, and a NAM that stops at its own ceiling below x". That outcome also follows from H_GluN2A (NAM-insensitive triheteromer or 2A diheteromer pool) and from any composition hypothesis in which the NAM-insensitive pool matters; it does not strengthen total gain over them, it is unresolved. (b) A left-shift is read as "GluN2B-containing receptors weigh more than their share", but a left-shift against an EPSC-based axis could equally come from a synaptic-versus-extrasynaptic or burst-pool difference (the NAM and d-APV act on different parts of the glutamate transient). Not in the table.
3. **Triheteromers, partial inhibition, slow washout.** Handled: ceilings 32/50 percent (Zn), 29/58 (CP-101,606), 45 (radiprodil, rat, Zn-chelated oocyte buffer), time-matched vehicle, plateau pre-determined. Missing: the 3-7 percent escape current inside the 32 percent, and that the radiprodil value is under EDTA.
4. **d-APV surmountability.** Labelled CARRIED with the explicit note that nothing read bears on it. Honest. See point 1 for what is not solved.
5. **Is the pairing the smallest that separates the hypotheses?** The NAM plus d-APV is the smallest for total-gain vs composition; one NAM is enough, since D11 (verified) says the NAMs share site and ceiling. The TCN-201 arm "three equations for three shares": with the normalization the system is two unknowns and the maxima are +/-1 to 4 percent SEM for tri (72 +/- 4) and, more important, depend on 3 uM glycine and no added Zn2+ in the oocyte; in a slice the TCN-201 maxima shift with D-serine/glycine, and tonic Zn2+ raises the NAM maximum (D03). So the three-share solution cannot be called resolvable from public sources and, even as an experiment, its error propagation is large. It still does not separate: (a) NAM-insensitive triheteromer from GluN2A diheteromer without TCN-201; (b) synaptic vs burst pool (above); (c) state vs composition if Mg2+ and K+ are only recorded, not varied (row H_state handles by variation; fine).
6. **Measurements that only a new experiment can supply and are written as such.** M-N1 to M-N7 are all labelled as needing the Wwox slice; none is presented as a literature datum. Good.

   **Missed by the producer (names to add to `new_measurements.tsv`):**
   - M-N8: the NMDAR component of the burst itself (voltage-clamp current or burst-associated NMDAR charge) and the percent of it removed by each drug, as opposed to evoked-EPSC percent. Blocks H_total_gain, H_GluN2B.
   - M-N9: glycine/D-serine level for the NAM arm too: Williams (abstract) says glycine reduces ifenprodil inhibition at NR1A/NR2B, so M-N4 (listed as blocking only H_GluN2A) also bears on H_GluN2B.
   - M-N10: NAM ceiling and potency at slice temperature (35 C) and slice pH; all recombinant maxima read here are room-temperature oocyte values and the only native datum is room-temperature slice (D07).
   - M-N11: NAM equilibration time in the slice (D07 used 40+ min pre-incubation; D08 30 min infusion without a vehicle arm).
   - M-N12: d-APV potency shift against raised extracellular glutamate in these slices (the surmountability the table labels IPOTESI).

## D. Absence and perimeter (D12)

Stated: no source reached gives an ifenprodil or Ro 25-6981 sensitive fraction of the isolated NMDAR EPSC amplitude in mouse neocortical layer II/III pyramidal cells at P13-P17 in a non-visual area; 11182088 identified, not reached.

Re-runs (2026-11-09, Europe PMC REST unless noted):
- `(ifenprodil OR "Ro 25-6981" OR "Ro25-6981") AND ("layer 2/3" OR "layer II/III" OR "layers 2/3") AND (EPSC OR "NMDA receptor") AND (neocortex OR cortex) AND slice AND (mouse OR mice)`: 114 hits (the producer's comparable Q06 reported 51 with a different string).
- `... AND (somatosensory OR barrel OR prefrontal ...)`: 113 hits.
- `(ifenprodil OR "Ro 25-6981" OR "CP-101,606") AND ("NMDA receptor-mediated" OR "NMDAR-EPSC" ...) AND (neocortex ... ) AND ("layer 2/3" ...) AND (juvenile OR postnatal OR P12 ... P16)`: 95 hits.
- Title/abstract-only string on GluN2B, layer 2/3, ifenprodil or Ro 25-6981, EPSC: 4 hits.
- PubMed tool `(ifenprodil OR Ro 25-6981) AND NMDA EPSC AND layer 2/3 pyramidal AND mouse cortex slice`: 0 hits.

New candidates the producer did not name (abstracts read; bodies not reached):
- 39406518 (J Neurosci 2024): mouse somatosensory cortex, L2/3-L2/3 synapses, P13-21, t-LTD "requires ... NMDA-type glutamate receptors containing GluN2B subunits". Non-visual, mouse, target age, layer II/III, but a plasticity readout; whether it reports an isolated NMDAR-EPSC ifenprodil/Ro fraction is UNKNOWN (PMC page bot check; bucket stub; Europe PMC full text HTTP 500). This is the closest match to the absence statement's own wording.
- 21789901 (Chin J Physiol 2011): rat visual cortex layer II/III pyramidal cells, 12-15 day old, Ro 25-6981 and ifenprodil prevent LTD induction (plasticity, not an EPSC fraction; rat and visual).
- 21430146 (J Neurosci 2011): mouse S1 L2/3, second and third postnatal week; the abstract does not mention a GluN2B antagonist; not evidence of any fraction.

Assessment: the absence claim survives as "no fraction of the isolated EPSC found in sources screened at title or abstract level", but the perimeter was inadequate for the wording used: a title screen of the first 12-15 hits of 33-51 cannot exclude a methods-level measurement inside a plasticity paper (for example 39406518 or 21789901), because pharmacological fractions of the NMDAR EPSC are usually a Methods or supplementary control, not in titles. The statement should say "title/abstract screen; methods of plasticity papers not searched" and list 39406518, 21789901 as unreached candidates. The 11182088 abstract remains an abstract (EN21 quote verified).

Also re-run for D05/D06 absences ("maximum inhibition and conditions are not in the abstract"): confirmed by the abstracts retrieved.

## E. Evidence rows and receipts

Evidence rows (`output/evidence.tsv`, 22 rows): each quote compared with the source text.
- Verbatim at the locator: EN01-EN09 (Hansen; EN13 is Mierau), EN10-EN14 (Mierau), EN15-EN17 (Koster), EN18-EN21 (abstracts). Checked 22; correct as quote 21; EN22 is a carried value with no quote (acceptable as labelled).
- Defective in content (not in the quote): EN10 note "Number from Fig 4A bars, not in text" is wrong because Table 2 gives the numbers (see D07). EN22 carries "91 percent GluN2B" without stating human vs rat (D10). EN08 and EN17 quote carried or authors' statements; roles are correctly labelled as context or counter.
- Counts: checked 22, correct 20, defective 2 (EN10 note, EN22 content).
- EN13 quote "1.3 mM MgCl" is a substring of "1.3 mM MgCl2/6H2O" (subscript stripped): verbatim as a fragment.

Receipts spot-checked (2):
- FTR-20261109-24607230-71: fingerprint 6ff59977f27a00ea92fc28238e06bb13a9bf728373f8f28cbafa4e33439a4d3b equals the SHA-256 of the bucket `PMC3957490.1.txt` I downloaded. Both quoted `verbatim_locator` strings (maximal inhibition 32 +/- 1 percent, N = 16; 32 to 50 percent with Zn2+) occur verbatim in Results. Coverage lists `figures: read` while the evidence basis says only Figs 2 and 3 were viewed and Figs 1, 4, 5 were captions only: coverage is broader than the basis (it should read as partial). `prior_receipt` null, `first_read` consistent.
- FTR-20261109-26185009-71: fingerprint 7dcef9fe17115fb7a203d282a8e07ee4b6f735938dbd61c3529d3051150ce114 equals the SHA-256 of the bucket `PMC4670611.1.xml`. Quote "slice were incubated in artificial cerebrospinal fluid with 3 uM ifenprodil" present in Methods. Coverage records `tables: not_read`, but the XML contains Tables 1 and 2 and Table 2 holds the very numbers used: the receipt and the D07 depth statement are inconsistent with what was available.
- 7901753 receipt glanced: abstract only, `source_fingerprint` null, consistent with a PubMed-record source.

Figure notes (`figure_notes.tsv`): FN01 and FN06 re-viewed and agree (FN06 per-cell range 70-91 for WT; baseline tau_w about 185 ms; no vehicle arm drawn). FN04 values are consistent with Table 2 within 0.05 for all cells I compared. FN02 not viewed by me.

## Corrections the producer must make

1. `output/decisive.tsv` (D07) and `output/evidence.tsv` (EN10 note), `output/figure_notes.tsv` (FN04 row): replace "raster bar graph, INFERENZA" by the Table 2 values with n and SEM (WT pyramidal N/A: P15 1.18 +/- 0.08, n = 15 to 0.83 +/- 0.09, n = 12; P30 0.96 +/- 0.09, n = 9 to 0.81 +/- 0.08, n = 13; P45 0.92 +/- 0.05, n = 13 to 0.82 +/- 0.05, n = 14) as DATO; state that the roughly 30 percent has about +/-10 pp from the SEMs and that the readout is a late-time N/A ratio affected by decay shortening (Table 1: 116 to 76 ms at P15). Receipt FTR-20261109-26185009-71: `tables` should be `read` if the table is read.
2. `output/decisive.tsv` D04 (Species/system cell) and `output/comparison.tsv` H_GluN2A row 3 (cell "source_of_action_and_selectivity_limits"): "glycine level for this series not stated" is wrong; Fig 2 legend gives 3 uM glycine (100 uM glutamate) for TCN-201. Add that this is low co-agonist.
3. `output/decisive.tsv` D10 and `output/evidence.tsv` EN22: write "human GluN1-1a/GluN2B 91 +/- 1 percent; rat GluN1-1a/GluN2B 82 +/- 9 percent; rat GluN1/GluN2A/GluN2B triheteromer 45 +/- 10 percent (n = 8); 10 uM EDTA in the oocyte bath" (Table 1 and Methods of 40994429); the contrast cited should be 82 vs 45 (rat). Mark D10 as read in this audit rather than carried only if the producer wants to claim it.
4. `output/decisive.tsv` D12: restate the perimeter as "title/abstract screen of the first 12-15 hits per query; Methods of plasticity papers not searched", and add 39406518 (mouse S1 L2/3, P13-21, GluN2B-dependent t-LTD) and 21789901 (rat V1 L2/3, 12-15 day, Ro 25-6981 and ifenprodil block LTD) as unreached candidates; `output/queries.tsv`: add the re-run strings and hit counts above or equivalent rows.
5. `output/comparison.tsv` H_total_gain "outcome_strengthens" (column 8): change the "NAM stops at its own ceiling below x" arm from "strengthens" to "unresolved" (it equally fits GluN2A or insensitive-triheteromer pools).
6. `output/comparison.tsv` H_GluN2B column 4: "two primary sources" should read "one primary source (Hansen) and one abstract (Williams)"; add that a left-shift on an evoked-EPSC axis may reflect synaptic/extrasynaptic or burst-pool differences, not composition alone.
7. `output/comparison.tsv` H_GluN2B conditions column: add glycine/D-serine for the NAM arm (Williams abstract).
8. `output/new_measurements.tsv`: add M-N8 to M-N12 as listed in C; change M-N4 "blocks_which_comparison_row" to H_GluN2A; H_GluN2B.
9. `output/decisive.tsv` D08 (species cell): replace "recording Mg2+ not stated in the passages read" by "Methods give a slicing aCSF with MgCl2 4 mM; recording aCSF composition not separately given; no vehicle arm for the 30 min infusion".
10. `output/receipts/FTR-20261109-24607230-71.json`: `figures` coverage should reflect that Figs 1, 4, 5 were captions only.
11. D06 wording: say the two "activity dependent" statements may differ in definition; do not call it a disagreement without the full texts.

## What I could not reach

- Full texts of Williams 1993 (7901753), Fischer 1997 (9400004) and Philpot 2001 (11182088): not re-attempted (producer's bot check recorded); verdicts D05, D06 are abstract-level only.
- Hansen 2014 supplement (Supplemental Experimental Procedures, Fig S5 voltage dependence, oocyte bath composition, pH): the bucket lists no supplement; whether the 32 percent baseline was in a Zn2+-chelated bath is therefore unknown to me.
- 39406518 body (PMC page bot check; bucket stub; Europe PMC full text HTTP 500): not retried by another route.
- Hansen Fig 2 and Mierau Fig 4 images were not re-viewed (Table 1 and Table 2 carry the numbers).
- The Stroebel 2018 and Tovar 2013 papers cited for native triheteromer share were not opened (outside the brief).

---

## Recheck (nc-v, after the producer's correction round)

Checked against the sources I downloaded (PMC3957490 Fig 2 legend; PMC4670611 Tables 1-2; PMC12677382 Table 1 and Methods) and my own re-run counts.

| # | Item | Result |
|---|---|---|
| 1 | D07, EN10, FN04 | OK. Table 2 values, n and SEM match the source (WT pyramidal 1.18/0.83, 0.96/0.81, 0.92/0.82; KO 1.02/0.78, 0.96/0.64, 0.91/0.78; Table 1 decay 116 to 76 ms, n = 12 each). The about 30 percent with +/-10 pp and the late-time decay caveat are present. |
| 2 | D04 and H_GluN2A cell | OK. 3 uM glycine with 100 uM glutamate (Fig 2 legend) is stated in D04 and in `comparison.tsv` H_GluN2A col 4. |
| 3 | D10, EN22 | OK in `decisive.tsv` and `evidence.tsv` (91 human, 82 rat, 45 rat triheteromer n = 8, 10 uM EDTA). **Still wrong in `comparison.tsv`, H_GluN2B, col "compound_or_probe..."**: "Radiprodil (carried): 91 vs 45 percent" must read "rat 82 vs 45 percent (human diheteromer 91)". |
| 4 | D12, Q14 | OK. Perimeter wording is now title/abstract level, 39406518 and 21789901 are listed as unreached candidates; Q14 hit counts (114, 113, 95, 4, 0) equal my runs. |
| 5 | H_total_gain, H_GluN2B | OK. The NAM-ceiling outcome moved to outcome_unresolved with the GluN2A/insensitive-triheteromer wording; "one primary source (Hansen) and one abstract (Williams)" and the synaptic/extrasynaptic caveat are present. Cosmetic: outcome_strengthens begins "INFERENZA: INFERENZA:". |
| 6 | M-N8 to M-N12, receipts | OK. M-N4 now blocks H_GluN2A; H_GluN2B. Receipt 24607230 has figures = captions_only. Receipt 26185009 has tables = read; its `figures: read` still sits beside "Figs 1-3, 5-7 captions only" (same coverage-wider-than-basis point as before, minor). |

Residual overstatements and stale text:
- `comparison.tsv` H_GluN2B col 3: "(D07; raster read; ...)" is stale; the number is a Table 2 value (DATO).
- `new_measurements.tsv` M-N2 col 3: "about 30 percent is a raster-read ratio" is stale for the same reason.
- `phase_note.md` line 3: "Mierau's ifenprodil numbers are read from bar graphs (INFERENZA)" contradicts D07; line 1 omits the tables from Mierau's depth.
- `comparison.tsv` H_GluN2B outcome_weakens: "a burst unchanged up to the NAM ceiling (D07: about 30 percent)" treats a visual-cortex P15 native bound (+/-10 pp, late-time ratio) as the NAM ceiling for the Wwox cells; the ceiling there is unknown (recombinant 32/50 to 88 percent).
- `comparison.tsv` H_GluN2B mechanism_discriminating_control (ii): "three equations for three shares" is still given without the fragility noted in section C point 5 (3 uM glycine, Zn2+ dependence, SEM of 72 +/- 4); my correction list did not ask for it, but "if additivity and recombinant maxima hold" understates it.
