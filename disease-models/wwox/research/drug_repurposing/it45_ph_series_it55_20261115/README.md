# IT45-Q06, Q07, Q08 (pH series) from primary papers (IT55 producer delegate, 2026-11-15)

Non-canonical working note. Not medical advice; no dose, schedule or route; no compound nominated. Reference genotype class only. No ranking, need, candidate state, card or frozen package edited; no receipt appended (four receipt drafts, dry-run only). context_policy: QUESTION_DRIVEN. Predictions were frozen in a local commit before any paper body was opened: `predictions_frozen.md` (never pushed). Labels: DATO = stated in a page text read here (verbatim id given); CARRIED = taken from an earlier package, not re-read; DERIVED = arithmetic by this delegate; INFERENZA = reading, not stated.

## Answer first

**IT45-Q06 (do the family-level K2P tools change potency between pH 7.4 and 7.6?): no tool has a primary two-pH potency in anything that could be read. For every tool the answer is "not stated", not "insensitive".**

| Tool | What the primary read gives | pH conditions of the tool measurement | Two-pH potency |
|---|---|---|---|
| A1899 (comparator) | Human TASK-1 IC50 35.1 +/- 3.8 nM in oocytes; Table 1 also TASK-3 0.318, TREK-1 23.8, TREK-2 8.4, THIK-1 2.2, TRAAK >20 uM; CHO TASK-1 7 nM, TASK-3 70 nM [V11, V12, V13] | oocyte recording solution pH 7.5, 20-22 C [V09, V10]; CHO conditions not on the page | **not stated** (page text has 3 pH tokens, all in Methods/Introduction at one pH; supplemental procedures not on the page) |
| A1899 on native TASK (rat carotid-body type-1 cells) | 0.3 uM lowers channel activity (NPo) by 23 percent, n = 5 patches [V22] | bath pH 7.4 only, 36-37 C [V16, V17, V20] | **not stated** |
| PK-THPP (comparator) | 0.1 uM lowers native TASK NPo by 26 percent, n = 5 patches [V23] | pHo 7.4 only [V20] | **not stated** |
| ML365 (probe) | not tested in the one paper that names it among tools (reference title only) [V24]; Flaherty 2014 (the discovery paper) was access-blocked here (reCAPTCHA); earlier package reports pH 7.4 only (CARRIED) | CARRIED: pH 7.4 | **not stated** |
| ML365 and A293 (= AVE1231, per `pointers.tsv`) in whole hearts | abstract only (paywall): no atrial APD/ERP prolongation at pH 7.4; at pH 7.8, "which augments K2P3.1 currents", ERP prolonged by 11.6 percent (p = 0.004) [V25, V26, V27] | 7.4 versus 7.8, tissue effect | **tissue effect at two pH, not a potency**; channel IC50 at each pH not in the abstract |
| ONO-TR-772 (TREK-1/TREK-2 inhibitor pointer) | follow-up main text gives only Tl+ IC50 0.26 uM for it [V02]; patch-clamp protocols are in the SI, not on the page [V07]; the primary page was blocked | not stated in anything read (term search: pH only in synthesis text) | **not stated** |
| Zn2+ (TASK-3), spadin, BL-1249, riluzole | Zn2+: abstract only (publisher page HTTP 403): TASK-3 IC50 19.8 uM at +80 mV, H98 and E70 required [V36]; spadin, BL-1249, riluzole: no hit in the pH-targeted searches (Q07 empty) | not reached | **not stated** |

What the readable sources add for reading a K2P arm across pH:

1. **The baseline moves with pH on the same preparation, and tools are tested at one pH.** In native rat TASK-1/TASK-3-like channels (cell-attached, 36-37 C) single-channel amplitude falls by 10.2 +/- 0.6 percent from pHo 7.4 to 7.3, 22.1 +/- 1.1 percent at 7.2 and 78.0 +/- 4.0 percent at 6.4 [V18, V19]. The two tools were applied at pHo 7.4 only [V20]. So an apparent tool-by-pH difference could not be separated from the channel's own pH response by any paper read (INFERENZA).
2. **A1899 potency depends on at least one other external condition.** At 400 nM, block at +40 mV was about 90 percent in 2 mM K+ and 59.7 percent in high K+, which the authors call an almost 10-fold IC50 increase [V14]. This is K+, not pH, but it shows tool potency is condition-dependent; the comparison engine's pH axis (consumer delta row 10) should come with the K+ and temperature fields already proposed.
3. **Preparations differ in more than pH** (oocyte, 20-22 C, pH 7.5, 2 mM K+ [V09, V10] versus native cells, 36-37 C, pH 7.4 bicarbonate/CO2 [V16, V17]); a 7.4 versus 7.6 reading from these rows would also change preparation and temperature (INFERENZA).
4. **The only pH-split observation for a named probe is at tissue level**, 7.4 versus 7.8, and it is abstract-level only [V25, V26].

**IT45-Q07 (true human patch-clamp potency of the TREK-1/TREK-2 dual-inhibitor pointer): not settled; the primary page (PMC12067145, PMID 40365404) returned a reCAPTCHA challenge and was not read. Stopped on that source. Both numbers stay, labelled by method.**

* CARRIED, not re-read (earlier package, `k2p_pointers_sci45_20261111/output/pointers.tsv` T1, receipts FTR-20261111-40365404-85/-86): human TREK-1 manual patch clamp 15 nM (text and abstract), QPatch 0.15 uM (SI Table S2), Tl+ flux 0.26 uM, mouse TREK-1 manual patch clamp 67 nM, TREK-2 QPatch 0.17 uM; species human (CHO) and mouse, not rat; patch-clamp temperature, pH, voltage and n not stated in the paper or SI as read there. The catalogue 15 nM is therefore a **manual patch-clamp value as printed**; 0.15 uM is the **automated (QPatch) value**; both are patch clamp.
* New context from the follow-up paper of the same group (PMID 41104520, main text read): compound 5 = ONO-TR-772 carries only a Tl+ IC50 of 0.26 uM there [V02]; manual patch clamp (MPC) IC50 values are given for other compounds. Within that series MPC is below Tl+ by a factor of 10 for 13d (0.011 versus 0.11 uM) [V03, V04], about 2.7 for 7 (0.079 versus 0.21; V42, V04), and nearly equal for compounds 10 and 11 [V05, V06]. DERIVED ratios MPC/Tl+: 0.10, 0.38, 0.94, 0.58. For ONO-TR-772 the carried pair is 0.015/0.26 = 0.058 (DERIVED, 17-fold). This is a larger gap than any of the four, but not by an order of magnitude, so the earlier package's reading that 15 nM "looks like a unit slip" (from ">67-fold" = 10 uM / 0.15 uM) is **not the only reading**: a genuinely lower manual patch-clamp IC50 is not excluded by series behaviour. Neither reading is shown (INFERENZA).
* The follow-up main text has no patch-clamp temperature, pH, voltage or n [V07; term search, `absence_check_output.txt`]; its SI (PDF) was not on the page. The earlier package's "bath pH 7.4, pipette 7.35, no stimulus" came from that SI and is CARRIED, applying to ONO-TR-772 by INFERENZA only.

**IT45-Q08 (proton response of GluN2B-containing and triheteromeric NMDARs at 35 C and 1.3 mM Mg2+, and in layer II/III neurons): supported abstention. No source found by the allowed routes meets 35 C or 1.3 mM Mg2+ for a GluN2B-containing or triheteromeric receptor, and none concerns layer II/III.**

* Closest primary read: Banke 2005, rat NR1-1a/NR2B in HEK 293 cells [V28]: proton IC50 pH 6.9-7.1 with Hill slope 0.8-1.0 in three protocols, pH 7.1 with both co-agonists [V31, V32]; kinetic Kd 77 nM = pH 7.2 [V33]. Conditions: **23 C** [V29, V30], external solution with no Mg2+ listed (150 NaCl, 10 HEPES, 3 KCl, 0.7 CaCl2, 0.2 EDTA, pH 7.4) [V29]; Mg2+ only in the culture medium and the internal solution [V34]. It is a GluN2B diheteromer, not a triheteromer and not a neuron.
* Triheteromer: no proton IC50, slope or residual in any source reached; abstract-level only: ASIC1a activation selectively facilitates the NR1/NR2A/NR2B current (Neuroscience 2019) [V39], which is not a proton-response curve. CARRIED (SCI45 N1): three triheteromer sources without a proton midpoint.
* Mg2+ and temperature: none of the NMDAR queries (Q11-Q21; list in `queries.tsv`) returned a primary with a pH series together with 35 C or about 1.3 mM Mg2+ in the abstract; the two hippocampal-slice abstracts (Brain Res 1998; J Neurophysiol 1999) [V37, V40] are the only candidates with physiological preparations, but their bodies were not reached (1998 not requested after the cap; 1999 returned HTTP 202 with an empty body) and the abstracts give no subunit, Mg2+ or temperature.
* Layer II/III: queries Q13 and Q21 (layer/neocortical terms with GluN2B/proton terms) returned no source with an NMDAR proton series in layer II/III neurons.
* CARRIED (SCI45 N1, not re-read): GluN1/GluN2B pH IC50 7.50 +/- 0.02 (Regan 2019, oocytes, Mg-free, about 23 C), native P13-P19 prefrontal pyramidal neurons pH50 6.97 (Mg-free, 22-24 C), GluN1/GluN2A 7.21 (Kostakis 2011, Mg-free). All are Mg-free and room temperature.

## Proposal for a dated Update (no cell edited)

K2P and NMDAR tool arms should be worded as **single-pH measurements**: each tool potency carries its recorded pH, temperature, external K+ and, for NMDAR, Mg2+ (A1899: pH 7.5, 20-22 C, 2 mM K+; native cells pH 7.4, 36-37 C; ONO-TR-772: pH not stated, 15 nM manual patch clamp and 0.15 uM QPatch both carried with their method), "tested at a second pH: not stated" (never "pH-insensitive"), and no pH 7.4 versus 7.6 comparison of a K2P tool or a GluN2B-targeting tool read as COMPARABLE, because the target's own pH response moves the baseline (native TASK amplitude falls 10 percent for 0.1 pH unit [V18]; GluN2B pH IC50 about 7.1-7.5 [V31, CARRIED Regan]) and no Mg2+/35 C proton response exists for GluN2B-containing or triheteromeric receptors; the 15 nM versus 0.15 uM pointer keeps both values labelled by method until the primary text or SI is read.

## Predictions scored (`predictions_frozen.md`)

| Prediction | Result |
|---|---|
| P1 no two-pH potency for ML365, PK-THPP, A1899 | **Held for what was read** (A1899 in two papers, PK-THPP in one); ML365's discovery paper was blocked and PK-THPP's discovery paper (ChemMedChem 2012) was not requested, so not shown for those two primaries. |
| P2 a two-pH potency most likely for Zn2+ or another class; about 40 percent any named tool | **Missed** for Zn2+ (abstract only, 403). One two-pH observation for a named probe exists (ML365/A293, 7.4 versus 7.8) but it is a tissue effect, not a potency. |
| P3 spadin, ONO-TR-772 one pH; BL-1249/riluzole not found | **Held as absence by search** (Q07 empty); ONO-TR-772 not re-read. |
| P4 baseline confound; no study separating it | **Held**: baseline fall shown [V18, V19]; no separating study found. |
| P5 3-5 bodies read; about 40 percent blocked | **Held**: 4 bodies partially read; of 10 sources, 3 gave a bot check or 403, 1 an empty HTTP 202, 1 a link-resolver page, 1 a paywall. |
| P6 15 nM printed as manual patch clamp, 0.15 uM a table column | **Carried, not tested here.** |
| P7 ">67-fold" is arithmetically 10/0.15 | **Carried; and now qualified** by the series MPC/Tl+ ratios (above). |
| P8 temperature/pH/voltage/n not stated | **Not tested** on the primary (blocked); consistent with the follow-up main text. |
| P9 no pH series in the paper | **Carried**; follow-up main text has none either. |
| P10 no source with 35 C and 1.3 mM Mg2+ | **Held.** |
| P11 a source with Mg2+ 0.5-1 mM and a pH series (35 percent) | **Not found / not testable** (slice abstracts only). |
| P12 an abstract at 30-37 C (40 percent) | **Not found**: Q14 and Q20 (title/abstract temperature terms) empty; PMID 8287051 not re-opened. |
| P13 no layer II/III source | **Held.** |
| P14 triheteromer midpoint not found | **Held.** |

## Depth, requests and blocked items

Ten sources were requested (the cap): **4 read partially from article pages with locators** (PMC12621189, PMC3077598, PMC9970648, PMC6725198), **1 publisher abstract behind a paywall** (Skarsfeldt 2016), **3 access-blocked** (PMC12067145 and PMC4160056: reCAPTCHA challenge page; Clarke 2004: HTTP 403 bot check; each recorded and not retried), **2 not reached** (Plutino 2019: link-resolver page; Tong and Chesler 1999: HTTP 202, empty body). Abstract-census only, no body request: Saybasili 1998, Ma 2019, Coburn 2012. **Requests: 34 curl invocations** (24 Europe PMC REST searches, 2 of them metadata-by-identifier with abstracts; 10 article requests, 6 on PMC spaced 10-11 s, no bursts). No e-mail or contact parameter sent; no browser spoofing; nothing solved or worked around; no spend.

## Limits

* One reader, no blind verifier. 42 of 42 quotes in `verbatim.tsv` were found in the saved page text by `verify_quotes.py` (`verify_output.txt`); this proves the text is on the page, not that each reading is right. The Europe PMC abstracts (V36-V40; V41 is the bot-check page title) are metadata copies, saved as `EPMC_ABSTRACTS.html` outside git.
* Figures were not viewed; SI PDFs and supplemental procedures are not on the pages; PMC page text drops images and equations.
* The Q07 answer is CARRIED from the earlier package because the primary page returned a reCAPTCHA; I did not try another route for that source (stop rule). A reader with an open route could settle it by reading the SI manual patch-clamp section and the potency table.
* "Not stated" means not stated in the page text read, not that the paper lacks it.
* The Skarsfeldt A293 = AVE1231 link rests on the synonym in `pointers.tsv` (T4), not on a structure check.

## Integrator note (IT, 2026-11-15)
Delegate: one legend-delegate, sonnet, effort high (read back: sonnet x67 turns, effort high x67; output 74,150 tokens, cache written 207,623, cache read 8,445,660, peak context 207,625; 34 curl requests, 24 of them Europe PMC searches; reCAPTCHA met on PMC12067145 and PMC4160056 and a 403 on Clarke 2004: each stopped, none worked around). Predictions frozen in the local commit 89657919c before any body was opened. IT re-checked three decisive quotes in the saved pages (A1899 IC50 35.1 +/- 3.8 nM at +40 mV in oocytes, PMC3077598; native TASK amplitude -10.2% from pHo 7.4 to 7.3, PMC9970648; the neuronal NMDAR proton IC50 range 6.9-7.3 in the PMC6725198 introduction, which is a literature statement, not the paper's own value): present. The remaining rows rest on the delegate's mechanical check (42/42), one reader, no blind verifier. Receipts recorded by IT after dry-run: FTR-20261115-15634765-01, -21362619-01, -36692168-01, -41104520-01 (the last with prior FTR-20261111-41104520-86). Q07 stays unsettled because its primary page returned a reCAPTCHA: the 15 nM / 0.15 uM / 0.26 uM values are carried from the earlier package and not re-read.
