# IT44-Q02 and the K2P/TASK/THIK half of IT44-Q01 from primary papers (IT55 producer delegate, 2026-11-15)

Non-canonical working note. Not medical advice; no dose, schedule or route; no compound nominated. Reference genotype class only. No ranking, need, candidate state, card or frozen package edited; no receipt appended (three receipt drafts only). context_policy: QUESTION_DRIVEN. Predictions were frozen in a local commit before any paper body was opened: `predictions_frozen.md` (commit f77c652d4 in the working clone; never pushed).

## Answer first

**IT44-Q02 (EC50 and conditions, riluzole on TRAAK and TREK-1, fenamate on TREK): not answered from a primary paper on the cloned channels; one finding changes how the repository's riluzole number should be read.**

1. **The "riluzole EC50 139.4 uM on TREK-1" in the ChEMBL review rows has an identically valued primary, and that primary is a native-neuron measurement, not a cloned TREK-1.** Cadaveira-Mosquera 2011 (PMID 21273422, PMC6623616) writes "a dose–response curve for riluzole in the blockers solution provided an EC50 of 139.4 μm (supplemental Fig. 1 ...)" [V02]. The preparation is cultured mouse superior cervical ganglion neurons, perforated-patch whole-cell, room temperature (no number), bath K+ 3 mM, pH 7.2 [V03, V06, V07, V08, V10, V13]. The riluzole experiments were held at -30 mV [V03]; the voltage of the dose-response curve and its n are **not stated in the page text** (the curve is in a supplementary figure that is not on the page). The ChEMBL row says "TREK1 (unknown origin) expressed in COS7 cells ... whole cell currents at +50 mV" (copied in `verify_s11/VERDICTS.md` from CHEMBL3817738 = Vivier 2016, PMID 26588045). Same number to four digits, different preparation and voltage. **That the ChEMBL value comes from this paper is an inference** (the review document was not read and is not in PMC), but no other source reached carries 139.4 uM (not a search of the whole literature). The authors themselves assign the native current mainly to TREK-2-like channels and say TRAAK "do[es] not contribute substantially" [V12]; they do not claim a TREK-1 EC50 [V46].
2. **EC50 of riluzole on cloned TRAAK and TREK-1: not reached.** Duprat 2000 (PMID 10779373, the paper that holds those curves) returned a 2.7 kB link-resolver page to one plain request, not the article [V43]; Fink 1998 (PMID 9628867, PMC1170668) is an abstract-and-PDF-link page [V34-V36], and the abstract gives no value ("TRAAK channels are stimulated by the neuroprotective drug riluzole" [V35]). So species, temperature, pH, external K+, voltage and n for riluzole on cloned TRAAK and TREK-1 remain **not stated in anything read**. Not zero, not negative: unread.
3. **Fenamate on TREK: abstract only.** Takahira 2005 (PMID 16075240) is behind a paywall [V42]; its abstract says COS-7 cells, perforated patch, and each fenamate at a **single concentration of 100 uM** (flufenamic, niflumic, mefenamic acid) "markedly stimulated TREK-1, TREK-2, and TRAAK" [V40, V41]. No EC50 appears in the abstract. The ChEMBL "flufenamic acid EC50 100 uM" coincides with that single working concentration; this is **consistent with** the EC50 row being a curation of the test concentration, but the body was not read, so it is not shown. (Abstract = census, not a read.)

**IT44-Q01, K2P/TASK/THIK half (Ba2+, 50-200 uM): no primary value inside the window was found for TASK-1, TASK-3 or THIK-1. TASK-1 is now measured outside the window; TASK-3 and THIK-1 stay not reached.**

* **TASK-1** (one primary read): O'Connell 2005 (PMID 15611021, PMC1665531), murine TASK-1 in Xenopus oocytes, two-electrode voltage clamp, **100 mM external K+, pH 8, 22-24 C**, holding 0 mV, steps -100 to +20 mV [V27-V31]. Ba2+ was tested "between 0.3 and 10 mm" [V27]: **the lowest tested concentration (0.3 mM) is above the 50-200 uM window, so no point lies inside it.** Reported KD at 0 mV is 36 +/- 10 mM (n = 6), a model extrapolation because "there were no currents at the equilibrium potential" [V25, V26]; Hill coefficient about 1; block is voltage-dependent and the KD "increased at more positive voltages (Fig. 6A)" [V32], with the voltage-resolved KD values in a figure that was not read. The authors call TASK1 "relatively insensitive to conventional channel blockers such as Ba2+" [V24]. **Derived, not measured:** with the usual exponential voltage law (equation not in the page text; form and sign convention are my assumption), the means give KD about 0.24 mM at -100 mV and about 4.8 mM at -40 mV in 100 mM K+, pH 8 (row 10 of `values.tsv`). The high-K+, alkaline, extrapolated and mean-plugged character of that figure means it must not be quoted as a TASK-1 Ba2+ potency at physiological conditions.
* **TASK-3**: not reached. Kim 2000 (PMID 10734076) returned a link-resolver page [V44]; no page that was read carries a TASK-3 Ba2+ value (term search of the saved pages: no TASK-3 Ba2+ statement in the pages read; TASK-3 appears only in pH or zinc context).
* **THIK-1**: not reached. Rajan 2001 (PMID 11060316) returned a link-resolver page [V45]. Unchanged from `verify_s11`: the only Ba2+ number tied to THIK-1 is a native Purkinje current assigned by similarity (not re-read here).
* Context values read this session (not the named channels): rat TWIK-1 K274E mutant in CHO, IC50 960 +/- 9.8 uM, h = 0.84, about 50 percent at 800 uM [V14, V15, V18]; rat TREK-1 in CHO, "no effect" at 800 uM [V16]; hippocampal astrocyte passive conductance 17 +/- 6 percent block at 1.2 mM (n = 6, +20 mV) [V17]; native riluzole-activated mouse SCG current reduced at a single 5 mM Ba2+ [V05]. These reproduce, from the primary text, the figures that `verify_s11` quoted for Zhou 2009 and add nothing in the window.

## Primary values against the review values

| Item | Review / row value | Primary reached | Conditions of the primary | Status |
|---|---|---|---|---|
| Riluzole, "TREK-1" EC50 | 139.4 uM, COS7, +50 mV, "unknown origin" (CHEMBL3817738 via Vivier 2016) | 139.4 uM, native TREK-like current, cultured mouse SCG neurons (V02) | perforated patch; room temperature; K+ 3 mM; pH 7.2; riluzole runs at -30 mV; curve voltage and n not stated; blockers solution (TEA, 4-AP, CsCl, CdCl, TTX) | value matches, preparation does not; source identity inferred |
| Riluzole fold change 2.0 (100 uM, COS7), 1.4 (10 uM, CHO) | rows in ChEMBL | not reached (Duprat 2000 unread) | none | unresolved |
| Riluzole on cloned TRAAK, TREK-1 | EC50 not in the repository | not reached | none | unresolved |
| Riluzole at 100 uM and 300 uM, native current | not in the rows | 89.6 +/- 4.8 pA (n = 6) and 188.3 +/- 35.7 pA (n = 8) at -30 mV (V03, V04); transient (V11) | as above | new, native only |
| Flufenamic acid, TREK-1 | EC50 100 uM (COS7); 3.5-fold and 250 percent at 100 uM (HEK293) | abstract: 100 uM single concentration, COS-7, perforated patch (V40, V41) | body not read; species, temperature, pH, K+ not stated in the abstract | consistent with a single-concentration origin; not shown |
| TASK-1 Ba2+ (50-200 uM) | not reached | none in window; KD0 36 mM extrapolated; lowest tested 0.3 mM (V25, V27) | murine, oocytes, 100 mM K+, pH 8, 22-24 C, hold 0 mV | window not measured |
| TASK-3 Ba2+ | not reached | not reached | none | unchanged |
| THIK-1 Ba2+ | not reached | not reached | none | unchanged |
| TWIK-1 Ba2+ | 100 uM (human, oocytes) vs 960 uM (rat, CHO) | 960 +/- 9.8 uM (V15) confirmed in the primary text; the 100 uM paper not re-read | rat K274E mutant, CHO, ramp -140 to +80 mV, pipette pH 7.4; bath and temperature for these runs not stated | unchanged |

## What is unchanged

* The family-level statement of `relation_s11_result_it44.md`: the catalogued K2P openers act on TREK/TRAAK, the Ba2+-weak subfamily; every Ba2+ value read this session is in the millimolar range for a K2P channel (TASK-1 KD0 36 mM extrapolated; TWIK-1 960 uM; TREK-1 no effect at 800 uM; native TREK-like current reduced by 58.7 percent at 5 mM [V05], printed as "37 ± 6.3 pA; 58.7%; n = 4"). Nothing read contradicts that a current lost at 200 uM Ba2+ or less points away from TREK/TRAAK; nothing read measured TASK-3 or THIK-1 there.
* Opener caveats (about 100 uM or more for K2P activation, transient TREK-1 effect): the transient effect is confirmed in the text of the primary that cites Duprat 2000 [V11] (a citation, not Duprat's own data).

## Predictions scored (from `predictions_frozen.md`)

| Prediction | Result |
|---|---|
| P1 PMC pages return bodies; non-PMC end limited or blocked | **Partly missed.** All six PMC pages returned HTTP 200, but two (Fink 1998, Duprat 1997) carry abstract plus a PDF link only, no body. Non-PMC: Takahira paywall preview (held); the three Elsevier-hosted papers returned a link-resolver page, not a 403 or challenge (outcome held, mechanism different). |
| P2 riluzole EC50 within a factor of 3 of 139 uM on clones; ChEMBL 139.4 may come from a different paper | **Second half held, first half not testable.** 139.4 uM is in a different paper (native neurons). No cloned-channel EC50 reached. |
| P3 fenamate concentration-response, possible curation artefact | **Not testable** (body paywalled). The abstract's single 100 uM concentration is consistent with the artefact reading. |
| P4 native riluzole current, mouse SCG, several tens to a few hundred uM, Ba2+ single high concentration | **Held**, and exceeded: an EC50 (139.4 uM) is stated, which I had not predicted for this paper. |
| P5 no Ba2+ concentration-response in 50-200 uM for TASK-1, TASK-3, THIK-1 | **Held for TASK-1** (lowest tested 0.3 mM); **not testable** for TASK-3 and THIK-1 (unreached). The "at most 30 percent block at 100-200 uM" expectation was not tested by any number. |
| P6 family-level statement unchanged | **Held.** |
| P7 four to six papers read | **Missed**: three read with locators (Cadaveira-Mosquera 2011, Zhou 2009, O'Connell 2005). |

## Depth and requests

Of ten papers reached (the cap): **3 read with locators** (partial full text from PMC pages, selected Methods and Results: PMC6623616, PMC6665656, PMC1665531), **1 abstract read plus mechanical term search of the body** (PMC2492388; Ba2+ appears once, in a reference title), **2 PMC pages with abstract only** (PMC1170668, PMC1170177), **1 publisher abstract behind a paywall** (Takahira 2005), **3 not reached** (Duprat 2000, Kim 2000, Rajan 2001: link-resolver page only). Vivier 2016 (the review) was identified, not requested. **Requests: 24 curl invocations** (14 Europe PMC REST identifier or metadata queries, 6 PMC article pages, 4 publisher routes through doi.org), one per source, no retries; space of 8-12 s between page requests; no contact parameter; no challenge, captcha, proof-of-work or 403 was met. `access.tsv` lists each source with status, size and SHA-256 of the saved page (the page copies are in the delegate's scratchpad, not in git).

## Limits

* One reader, no blind verifier. All 46 quotes in `verbatim.tsv` were found in the saved page text by `verify_quotes.py` (46 of 46; output in `verify_output.txt`); that proves the text is on the page, not that each reading is right. The three receipt drafts pass `fulltext_receipts.py record --dry-run` (nothing written).
* Figures were not viewed; supplementary figures are not on PMC pages; equations 2 and 3 of O'Connell 2005 and the KD(V) values of its Fig. 6A are not in the page text. Page text conversion drops images and equations.
* The Cadaveira-Mosquera EC50 is a native-neuron value: it does not give the EC50 of any one channel isoform.
* The "same number, same source" link for 139.4 uM is an inference from an identical value; the Vivier table was not read.
* The Zhou 2009 temperature sentence sits in the slice paragraph; whether it covers the CHO runs is not stated.
* The doi.org route for Elsevier-hosted papers ended at a link-resolver page with an HTML meta-refresh. The rule "one plain request per source" was kept, so the refresh was not followed; it is not a block, and following it would be a second request that the dispatch did not authorise.

## Next steps that need an operator or IT decision (nothing done here)

1. One further request each to the journal pages behind the three link-resolver pages (Duprat 2000, Kim 2000, Rajan 2001); the journal sites sit behind a CDN and may return a bot check, which would be a stop.
2. The PMC PDFs of Fink 1998 and Duprat 1997 (links on the pages read); text layers of 1997-98 scans may be poor (use rendered-page locators).
3. Cadaveira-Mosquera supplementary Fig. 1 (the 139.4 uM curve: range, voltage, n) and O'Connell Fig. 3B/6A (KD against voltage at 0.3-10 mM); check whether the figures are vector before treating values as unresolvable.
4. Vivier 2016 table (not in PMC) to confirm which primary the 139.4 uM and the 100 uM flufenamic acid EC50 rows cite.

## Proposal only: wording of the K2P opener rows

State the riluzole potency as "about 100 to 300 uM for the K2P-type effect, with the one primary EC50 reached (139.4 uM) coming from native mouse sympathetic-neuron current at room temperature, not from cloned TREK-1 or TRAAK", the fenamate as "tested at 100 uM in COS-7 cells (abstract), EC50 not shown", and the Ba2+ line as "no primary Ba2+ concentration-response in 50-200 uM for TASK-1, TASK-3 or THIK-1; TASK-1 tested only from 0.3 mM in 100 mM K+, pH 8 oocytes" instead of citing a ChEMBL EC50 as a measurement on TREK-1; as a dated Update, not an edit of cells.

## Files

`predictions_frozen.md`, `values.tsv` (17 rows), `verbatim.tsv` (46 quotes, all found), `access.tsv` (16 rows), `verify_quotes.py`, `verify_output.txt`, `receipts/FTR-20261115-21273422-01.json`, `receipts/FTR-20261115-19571146-01.json` (prior_receipt FTR-20261111-19571146-96, abstract-only earlier events), `receipts/FTR-20261115-15611021-01.json`.

## Integrator note (IT, 2026-11-15)
Delegate: one legend-delegate, sonnet, effort high (read back: sonnet x59 turns, effort high x59; output 73,060 tokens, cache written 175,795, cache read 5,675,647, peak context 175,797; 24 curl requests, no challenge met). Predictions were frozen in the local commit f77c652d4 before any body was opened. IT re-checked three decisive quotes against the saved pages: the riluzole EC50 of 139.4 uM and the single 5 mM Ba2+ reduction of 58.7% in PMC6623616 (a native mouse sympathetic-neuron current), and the TASK-1 Ba2+ KD of 36 +/- 10 mM at 0 mV in 100 mM K+ in PMC1665531: all three present. The remaining rows rest on the delegate's own mechanical check (46/46 quotes found), no blind verifier (one reader). Receipts recorded by IT after dry-run: FTR-20261115-15611021-01, -19571146-01 (prior receipt FTR-20261111-19571146-96, abstract-only), -21273422-01. The "same number, same source" link for 139.4 (ChEMBL review row from Vivier 2016 to Cadaveira-Mosquera 2011) is an inference, not read. Further requests the delegate listed (journal pages behind three link-resolver pages, two PMC PDFs, one supplementary figure, one table) were NOT made: none would decide a comparison now.
