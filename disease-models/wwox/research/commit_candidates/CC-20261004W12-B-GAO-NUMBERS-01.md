# CC-20261004W12-B-GAO-NUMBERS-01 - PAPER 214 against its own panels and Methods: a 4- to 6-fold sentence the panel does not support, a liver-enzyme scope that is too narrow, and a volume statement that is not "internally consistent"

`context_policy: QUESTION_DRIVEN` (re-read of PMID 42511902 against PAPER 214 and the wave-7 arm of DL-METH-117, intake wave 12, 2026-10-04, Scientist B)
**Date:** 2026-10-04 · **Change class: MINOR.** One paper-registry record gains measured qualifications and one ledger lead gains an appended note. No claim, no baseline, no WWOX statement is touched.
**Target records:** `disease-models/wwox/registries/paper_registry_current.md` (`PAPER 214`, three `replace-within` ops), `disease-models/wwox/research/discovery_ledger_current.md` (`DL-METH-117`, one `append`).
Receipt: `FTR-20261004-42511902-02` (prepared, not recorded) · Manifest PASS · Dossier `PMID42511902.md`, part 2.
**Nothing here is medical advice. WWOX occurs zero times in the paper; earned null for the gene.**

## 1 - The wave-5 flattened-table risk, answered

The JATS has no `table-wrap` and no `table` element (counts 0 and 0), the body text never contains the word "Table", and the article declares no supplement. **There is no table whose flattening could have been misread**; every number the registry carries from this paper is running text or a figure panel. All seven figure images were inspected. The mechanism of the wave-5 finding does not apply here, but a text-versus-panel disagreement does (below).

## 2 - What was measured

- **Holds:** 1 x 10^10 vg per pup; "~2.0 g" pup and about 5.0 x 10^12 vg/kg (1e10 / 0.002 kg = 5.0e12, exact); ALT and AST raised only with AAV-MacpnS1 at one time point (Figure 7A and B: ALT about 50 U/L against about 33 for uninjected wild type; AST about 170 against about 110; the other three capsids at or below wild type); single dose, single age, single harvest, no immune endpoint.
- **Text holds, panel does not (Figure 5B).** The text gives DRG eGFP intensity "approximately 4- to 6-fold lower" for rAAV2-retro and AAV-PHP.eB than for AAV9 and AAV-MacpnS1. The bars, read against the printed tick spacing (28.4 px per 10^7), sit near 7 x 10^7 (AAV9), 6 x 10^7 (MacpnS1), 0.4 to 0.9 x 10^7 (retro) and 0.1 to 0.3 x 10^7 (PHP.eB): about 8- to 18-fold lower for retro and more than 25-fold lower for PHP.eB than AAV9. Dots and SEM marks overlay the bar tops, so the values are approximate; neither capsid is within 4- to 6-fold.
- **Scope of the liver-enzyme statement (Figure 7C).** ALP-2c is about 2.5 to 3 times the uninjected-wild-type level (about 250, 275, 300 and 310 U/L against about 100) in all four injected groups, as the text also says; ALT and AST are the ones raised by one capsid. The only control is uninjected wild type: there is no vehicle-injected and no eGFP-only arm.
- **Volume statement (Methods 2.1 against 2.2).** 2.1: "an absolute dose of 1 x 10^10 vg in a 2 uL injection volume". 2.2: about 2 uL of undiluted stock was mixed into a 20 uL saline droplet and "the entire viral mixture" of about 22 uL was injected (about 11 mL/kg for a 2 g pup). So 2 uL is the stock aliquot; the injected volume is about 22 uL; the stock titre is not printed.
- **Group sizes.** The Methods give "at least four" biological replicates; the legends give 4 (cell counts), 5 (heat map, neuronal fraction), 6 (motor-neuron fraction, DRG and liver intensity) and 8 (serum chemistry).

## 3 - Ops (record-scoped; `old` measured unique in `PAPER 214` / `DL-METH-117` with the registry reader)

### Op 1 - `PAPER 214`, short title

- `old` (unique): `liver enzymes raised by one capsid`
- `new`: `ALT and AST raised by one capsid (ALP-2c in all four, against uninjected wild type only)`

### Op 2 - `PAPER 214`, `Role`, the DRG sentence

- `old` (unique): `about **4- to 6-fold lower** with rAAV2-retro and AAV-PHP.eB`
- `new`: `about **4- to 6-fold lower** with rAAV2-retro and AAV-PHP.eB **by the paper's text; its Figure 5B bar tops, read against the printed ticks, give about 8- to 18-fold lower for rAAV2-retro and more than 25-fold lower for AAV-PHP.eB (approximate, 2026-10-04)**`

### Op 3 - `PAPER 214`, `Role`, the carried-number sentence

- `old` (unique): `the paper states a 2 µL injection volume inside a ~22 µL mixture (20 µL saline + 2 µL stock, internally consistent) and an n of *«at least four»* against n = 6 and n = 8 in legends — carry its numbers with these.`
- `new`: `the paper calls 2 µL the injection volume (Methods 2.1) and then states that the entire ~22 µL mixture (20 µL saline + 2 µL stock) was injected (Methods 2.2), so 2 µL is the stock aliquot and the stock titre is not printed; it gives n as *«at least four»* in the Methods and 4, 5, 6 and 8 in different legends (serum chemistry n = 8 against an uninjected wild-type control only) — carry its numbers with these.`

### Op 4 - `DL-METH-117`, append one bullet

`op: APPEND` bullet:

`- 🟢 **Append-only, 2026-10-04 (intake wave 12, \`CC-20261004W12-B-GAO-NUMBERS-01\`): the per-kilogram arithmetic of PMID 42511902 holds exactly, and its volume scalar is ambiguous in its own Methods.** 1 × 10¹⁰ vg per ~2 g pup is 5.0 × 10¹² vg/kg as the authors print; but the Methods call 2 µL the «injection volume» and then inject the «entire» ~22 µL mixture (about 11 mL/kg), so a per-volume scalar for this paper is 2 µL (stock) or 22 µL (injected) depending on which sentence is carried, and the stock titre is not printed. The article has no table: every carried number is running text or a figure panel. Transfer limit: neonatal mouse, intravenous, reporter cassette; not a CSF route, not WWOX.`

## 4 - Defaults taken

- The Figure 5B ratios are stated as approximate and as read by this reader; the paper's text is quoted unchanged beside them.
- The registry's "internally consistent" wording is replaced rather than deleted, because the dose per pup is unaffected if the whole mixture was given.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Methods 2.1 calls 2 microlitres the injection volume | in a 2 µL injection volume intravenously via the temporal vein | Methods 2.1, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (The 2 microlitres is stock, mixed into a 20 microlitre saline droplet | a 20 µL sterile saline droplet was dispensed first, followed by 2 µL concentrated viral stock | Methods 2.2, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (The whole mixture of about 22 microlitres was injected | The full ~22 µL mixture was aspirated into a 1 mL insulin syringe fitted with a 29-gauge needle for injection. | Methods 2.2, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (The entire mixture was administered | The entire viral mixture was administered to each pup via the temporal vein | Methods 2.2, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (The DRG fold-difference stated in the text | approximately 4- to 6-fold lower than those of AAV9 and AAV-MacpnS1 | Results 3.3, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (Figure 5B bar positions against printed ticks | `[figure attestation]` Figure 5B, y axis ticks at 0, 2, 4, 6, 8 x 10^7 located by pixel scan (28.4 px per 10^7): AAV9 about 7 x 10^7, MacpnS1 about 6 x 10^7, retro about 0.4 to 0.9 x 10^7, PHP.eB about 0.1 to 0.3 x 10^7 | `files/fulltext/PMID42511902_Gao2026_figures/biomedicines-14-01426-g005.jpg`)
- (ALP-2c is elevated in all four injected groups against wild type | In contrast, ALP-2c levels were elevated in all four groups compared to WT controls. | Results 3.5, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (The control is uninjected wild type | Wild-type (WT) mice without injections served as controls. | Figure 7 legend, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (Group size stated in the Methods | At least four biological replicates (individual mice) were carried out per group | Methods, quantification, `files/fulltext/PMID42511902_Gao2026_PMC.xml`)
- (Figure 7 panels A to C: ALT and AST differ from wild type only for MacpnS1; ALP-2c is about 2.5 to 3 times wild type in all four groups | `[figure attestation]` Figure 7A to 7C | `files/fulltext/PMID42511902_Gao2026_figures/biomedicines-14-01426-g007.jpg`)

## BATCH DISPOSITION — `BATCH_20261004_006` (2026-10-04, ACTOR_ID `scientist`, Scientist P), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED

Class re-judged **MINOR** (a paper record gains measured qualifications; one ledger lead gains a bullet). **Blind locator audit with pixel-level panel measurement: 10 triples and 4 independent checks — 10 SUPPORTED, 0 adverse.** The audit confirmed the text-versus-panel disagreement and **re-measured it**, so the landed figure is the auditor's band rather than the candidate's: about **8- to 11-fold** lower for one capsid and about **24- to 80-fold** for the other, against the paper's *«4- to 6-fold»*, with the two small bars explicitly unreadable to better than about ±50 % because they sit under their own dot clusters. Three further measurements were folded in: the article has **no table and no supplement at all**, so every number it carries is a bar in a figure with no deposited source data; the legends give 5, 4, 5, 6, 6, 6, 6 and 8 as n, including **two different n for one cohort in two panels of one figure**; and there is **no vehicle-injected and no reporter-only arm anywhere**, with all four capsids carrying the identical reporter genome — so the one finding common to all four (the phosphatase elevation, re-derived as 2.4- to 3.0-fold) is the least likely of them to be capsid-specific. Landed as 3 ops on `PAPER 214` and 1 appended bullet on `DL-METH-117`.
