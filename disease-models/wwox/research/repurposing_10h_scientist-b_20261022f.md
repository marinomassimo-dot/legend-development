# scientist-b, 2026-10-22 (f): R2 lot 4, seven more first-relay readings completed

Every source is NOT WWOX EVIDENCE (transferable mouse, rat, cell-line and clinical-genetics literature on the T-type axis). Class level, no dose, no suitability, not medical advice.

## 1. Method and the image-read rule

Same route as the previous lot: `paper_packet.py rank` first, completing receipts `FTR-20261022-<PMID>-02` STAGED (not recorded) with `prior_receipt` set and `reread_reason: inadequate_prior_coverage`, manifests STRICT PASS, `locator_audit.py --strength-scan` before commit. Following the coordinator's rule, a figure value was written only from an image that was displayed in full. **In this lot every image read returned an image**; no value is marked UNVERIFIED. Where a PMC figure file number differs from the figure number (35184274: files g001 to g004 are Figures 1, 4, 3, 2), the entries say so.

| PMID | Paper (short) | Result | Manifest locators | Supplement |
|---|---|---|---:|---|
| 37082241 | pan-Cav3 inhibitor in Dravet mouse, 6 Hz and GAERS | complete | 22 | read (two TIF figures, one table) |
| 32878331 | three CACNA1G missense variants, infantile DEE | complete | 14 | read (one page) |
| 33704440 | four CACNA1I missense variants | partial | 16 | captions_only |
| 40825030 | paired CACNA1I variants (A398E/V, M1425V/I) | partial | 12 | captions_only |
| 35079122 | glutathione deficiency and T-type hypofunction in reticular neurons | partial | 10 | captions_only |
| 35184274 | stiripentol, absence rats and T-type block | complete | 14 | not present |
| 40068874 | Cav3.2 knockout, dentate granule-cell excitability | complete | 14 | read (two TIF figures) |

## 2. Substance bearing on DL-MECH-170/171/172 (DATO)

- **Variants in human T-type genes (32878331, 33704440, 40825030).** The human CACNA1G variants shift activation to more negative potentials in all three; two raise the peak current density in cells and one (L208P) slows recovery and inactivation strongly (recovery about 65 percent at 1000 ms against full for wild type). For CACNA1I, four variants slow kinetics and left-shift activation (half-activation about 7 to 16 mV more negative) and inactivation; in the paired-variants paper two substitutions at one residue go in opposite directions (A398E left-shifts activation, A398V right-shifts it and lowers peak current; the modelled neuron fires more with A398E and is silent at rest with A398V). For the three leads this establishes that a T-type gene lesion has no single sign: gain and loss of channel function both produce disease-linked phenotypes, so a Wwox-related T-type change cannot be signed from the fact that it is a channel pathway lesion.
- **A non-channel lesion moving T-type current (35079122).** In glutathione-deficient mice T-type current in reticular neurons is lower only after an early-life oxidative challenge, and antioxidant treatment returns it to about minus 7 pA/pF (with a larger resting current than wild type); the MAM model shows the same decrease (about minus 3 against minus 7). This adds a second direction to the Cntnap2 case (increase) and supports the requirement that a Wwox test measure current in the right cell type and age; the age gating in this paper makes P17 transcript tables (DL-MECH-171) additionally ambiguous.
- **A T-type blocker with a second target (35184274).** The anticonvulsant blocks the three T-type isoforms in cell lines (residual current at 50 micromolar about 64, 61 and 43 percent) and suppresses spike-wave discharges in the inbred absence rat, and the authors say they cannot separate T-type block from GABA-A alpha3 modulation in vivo. For DL-MECH-172 this is a reminder that a "T-type blocker" effect needs a second class or a genetic arm to attribute.
- **A pan-Cav3 inhibitor with no efficacy and an aggravation (37082241).** The inhibitor did not reduce spontaneous seizures in the Scn1a heterozygous mice (P = 0.67; survival P = 0.09), protected about 50 percent of mice at the highest dose in the 6 Hz test and increased spike-wave discharges in the absence rats (raw incidence about 65 against about 78; total duration about 940 against about 1,200 s), with brain exposure short-lived (about an hour). The authors cite that Cav3.3 null mice show more discharges, so pan-block could be proconvulsant. This is a measured instance of a T-type-class compound worsening the endpoint it was expected to help.
- **Knockout of one T-type gene in a non-thalamic neuron (40068874).** Cav3.2 deletion changes granule-cell excitability in opposite directions by maturity (burst-spiking share 48 to 38 percent in intermediate cells; shorter intervals in intermediate regular-spiking cells; higher frequency in mature cells, about 11.3 against 9.4 Hz), with subthreshold and frequency-following measures unchanged, and the authors call the effect "relatively subtle" despite a strong phenotype; the Cav3.2 antibodies tested in the supplement gave no specific signal or cross-reacted with doublecortin, so protein localisation is unresolved in that paper.

## 3. What changed

Nothing in the choice of next experiment for DL-MECH-170, 171 or 172; these readings reinforce the earlier statement (cell-type-resolved current and a design with a genetic arm and a second drug class), and add that direction of T-type change depends on lesion type and age in every model checked so far (increase, decrease, no change at the transcript level, opposite signs for two substitutions at one residue).

## 4. Still owed

First-relay receipts still showing `figures=captions_only` and/or `supplementary=not_read` and not opened here: 24002024 (zebrafish drug screen), 26419537 (worm primary), 31781019 (APP/PS1 spike classes), 36282524 (worm model), 41137852 (clinical landscape of absence seizures). Debts on papers touched here: 33704440 and 40825030 supplementary figures and tables as images; 35079122 supplementary Word file (text layer contains embedded reference-manager blobs; not used); the earlier-lot debts in note 20261022e.

## 5. Unaudited items

All new figure attestations and the strength-scan narrowings below are unaudited: 37082241 entries 2 and 3; 33704440 entry 2; 35079122 entries 0, 1 and 3; 35184274 entry 4; 40068874 entry 2 (each carries `contradicts_locator` with an `ADVISORY_STRENGTH_SCAN` audit field, no blind audit).

## 6. DEFAULTS_TAKEN and STOP_LOG

Seven completions (ordering by lead relevance, then by figure effort); 32878331, 33704440 and 40825030 supplements: text layer of a font without Unicode map was not used for locators except where the verifier accepted it; three PMC-bucket supplement TIF files were converted to PNG with ImageMagick for viewing. STOP_LOG: none.

## 7. Text-control repairs (blind text control in `locator_audit_R2d_figures_20261022.md`: 6 of 32 OVERSHOOT)

The six adverse text entries were repaired from the source, each with `contradicts_locator` declared (repairs unaudited): 40827489 e2, 32719346 e2, 35243344 e2, 42536722 e2 and 32751129 e7 were narrowed to their quotes; 37275776 e9 (chronic in-vitro arm) was repaired by widening the quote to the three source sentences, which carry both the restoration of close-to-normal firing at the middle concentration and the authors' statement that the highest concentration seemed to produce an overshoot and greatly reduced network activity (so the earlier "over-suppressed" is the authors' own word, and the earlier quote had simply omitted it).

Self-sweep of every text entry written in the R2c to R2e passes (20 manifests) by form: 15 further entries whose proposition added a clause or an inference beyond the quote were narrowed (30175250 e19; 32678276 e10, e12; 32719346 e6, e8, e9, e11; 32751129 e5, e6; 33704440 e8, e10; 34483921 e11; 35243344 e7, e9; 37082241 e11, e13, e21; 40068874 e9; 40166234 e4; 42536722 e9, e10, e12, e15; 32878331 e6), all declared (`ADVISORY`/self-sweep audit field, unaudited). `locator_audit.py --strength-scan` over all 20 manifests now flags one entry (37082241 e3, "null" in "Cav3.3 null mice": a mouse-line name, not a null-result claim). Figure attestations that rendered were not touched; the 53 unrendered ones await the audit rerun.
