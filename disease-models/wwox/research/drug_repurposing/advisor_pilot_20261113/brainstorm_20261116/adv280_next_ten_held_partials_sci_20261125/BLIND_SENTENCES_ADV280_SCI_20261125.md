# ADV-280: repository sentences put to the second reader (SCI, 2026-11-25)

Dispatch: `legend-delegate`, model sonnet, effort high stated in the prompt. The reader saw copies of the held source files for ten records (folders A to J; no folder E, the preprint, was included) and the verbatim repository sentences below, not the first reader's conclusions. Some sentences are quoted verbatim in Italian.

Each sentence below is taken verbatim from a research repository that cites the paper in the named folder. Some are in Italian. For EACH sentence, check it against that folder only, and give a verdict:
- MUST CHANGE: some factual part is wrong or unsupported as written (say which words, what the source shows, and a corrected wording);
- ADD: nothing is wrong, but a window, dose, species, unit or evidence level is missing and a reader would be misled without it (say what);
- STANDS: supported as written.
Be strict and look for errors; do not assume the sentences are right or wrong. Check supplements, figures and tables, not only the text. Quote the panel, row or sentence you rely on.

## S1 (folder A)
A patient-fibroblast western is read by the authors as *«WWOX loss»*; the panel shows a strongly reduced band with a faint residual band, **one** control and **no quantification**, and it measures the **genotype** — it **cannot apportion the reduction between the two alleles**.  (b) RNA was measured for the structural allele only: exon 5 skipping, a 186 bp product beside the expected 293 bp, **without a skipped fraction, a frame statement or an NMD test** — and ⚠️ the short product is present **in an unaffected first-degree relative of the proband as well as in the proband** — the source names the relationship; this record does not, because a parental side does not belong in a statement about the reference genotype. What follows is that the assay measures the **presence** of an alternative junction and not severity: it is a qualitative splice read-out, not a severity marker. 

## S2 (folder B)
Whether the ISR in a WWOX-deficient system is compensatory rather than harmful: in the AFG3L2 precedent (PMID 37804316) HRI or DELE1 loss worsens, and a GADD34-targeted compound improves, patient-cell and mouse endpoints (survival gain about 6 to 7 days at the median by plot reading), a different direction from the PARS2 fly, with different species, endpoint and manipulation; the AFG3L2 kinase evidence is siRNA in fibroblasts, GCN2 and PERK were not tested

## S3 (folder C)
Cell viability and extracellular acidification fall at tens of micromolar. LDH activity in a lysate of treated cells and on recombinant enzyme falls only at hundreds of micromolar (the size of the lysate inhibition is not in the text and no LDH IC50 exists). NADH-driven oxygen consumption of isolated mouse heart and liver mitochondrial preparations, with complex I as the entry point (a flux readout of the organelle preparation, not an isolated-enzyme activity; the same paper's NADH-activity assays are dye-reduction measures), is inhibited from tens of micromolar (plot readings, auditor-confirmed, about 3 points of uncertainty: heart about 48, 5 and 1 percent remaining across the three lowest-to-highest concentrations tested; liver about 67, 36 and 23); no assay compares the two, so potencies are not comparable (INFERENZA: the effective concentrations are ordered complex I below LDH). The text figure of about 70 percent inhibition at the middle concentration is 51 to 53 percent raw in Supplementary Fig 2. The complex I paper reports no inhibition of malate dehydrogenase. Genetic LDHA/B double knockout raises respiratory capacity whereas stiripentol lowers it, so the drug does not phenocopy LDH ablation on respiration (INFERENZA). Cellular effects of stiripentol are therefore not attributable to LDH alone on the available data (the 2026 glioblastoma paper itself reports 'at least a partial role' of LDH). In a mouse glioblastoma xenograft stiripentol prolonged survival (log-rank P 0.002; median survival 80 versus 97 days, human stem-like cells in immunodeficient mice; the dose stated in the Results and legend is not stated in the Methods). None of the sources states which stereoisomer was used. Tumour models: no seizure, neurodevelopment or WWOX meaning.   [Only the parts that rest on THIS paper, or that this paper's files can contradict or qualify, are your concern.]

## S4 (folder D)
Whether an ATF4 protein or P-eIF2a rise in a WWOX-deficient neural system survives silencing of network activity (tetrodotoxin or an mGluR5 antagonist): group I mGluR agonism raises both in minutes without an Atf4 mRNA change in normal mouse hippocampus (PMID 41706892; that network activity does so is an inference), and WWOX-deficient systems are hyperexcitable (IT8 P5 loop 1).

## S6 (folder F)
### DL-MECH-058 — pY33→pS14 e' un modello di stato, non uno switch molecolare dimostrato

- **Status:** `promoted-to-CC` · **Tag:** REVIEW/BACKGROUND + declassificazione causale
- **Fonte:** Liu et al. 2022, PMID 35883580 / PMCID PMC9323965; testo, otto figure, legenda PDF e tre video letti integralmente. Dossier: `staging/deepdive_PMID35883580_Liu2022.md`.
- **Statement:** `pattern pY33/pS14 fra contesti —non dimostra→ conversione temporale diretta o switch causale universale`.
- **Evidenza:** la review aggrega studi precedenti con pY33 associata a stress/apoptosi e pS14 a lesioni tumorali/AD. Non presenta cinetica nello stesso sistema, identità di chinasi/fosfatasi, mutanti phospho-null/mimetic validati o rescue.
- **Lineage:** 30/86 referenze includono N.S. Chang; figure e video sono dati adattati/ripubblicati. La coerenza interna non e' replica indipendente.
- **Video:** tre sferoidi 4T1 qualitativi supportano differenze con anticorpi sotto ceritinib, ma sono campi diversi senza quantificazione/repliche e S3 ha PI già al basale.


## S7a (folder G)
Flow shift of a library, not a protein recovery measure; a lysosome-inhibitor control did nothing, placing the loss on the proteasome.  [concerns two papers; judge this one]

## S7 PB-1 (folder G)
(parts about this paper only) | PB-1 | Inhibitor arm first, chase second (a chase from an undetectable baseline has almost no discriminating power) | **KEEP** | Two primaries solved the baseline problem by moving to overexpression because mutant protein was "very low in neurons" (30266908); an inhibitor-only library read shifted the low-abundance shoulder (38378758, 38740822); a chase paired with a perturbation separated "newly synthesised" from "mature pool" (33914734); a recessive missense protein returned from undetectable to about 20 percent with an inhibitor (42875792) | A dossier-specified design performed on WWOX |

## S7 PB-2 (folder G)
(parts about this paper only) | PB-2 | A permissive-temperature arm perturbs two variables and should be excluded | **KEEP (confirmed in primaries)** | The Parkin atlas writes of the 29 degree effect: "Presumably this effect is the result of both an increased thermodynamic stability of the Parkin variants and a general reduction of protein turnover at the lowered temperature." (hedged by the authors; no separating control described) [REPAIRED 2026-10-22: the earlier version of this quotation was stitched with an ellipsis]; the ASPA and Parkin libraries lose the low peak at 29 degrees (38378758, 38740822) | A temperature arm run with a degradation-independent control |

## S7 Premise 0 (folder G)
(parts about this paper only) | Premise 0 | "Quantity of protein is not function": a rescued quantity may leave function behind | **KEEP, strengthened (several measured divergences)** | PTEN 22 percent loss-of-abundance only and 6 percent loss-of-activity only (34649609); Parkin abundance AUC 0.69 and half of pathogenic variants wild-type-abundant (38378758); ASPA C152W stabilised as insoluble and inactive (33914734); butyrate raises total immature GAT-1 with a small, variant-dependent function gain, which the authors read as non-specific accumulation (42157447; partial dissociation, not a clean quantity-up, function-flat case) [REPAIRED 2026-10-22]; the amenability call differs 12.9 percent between two assays with no clinical correlation (32023956); G443D reaches the membrane and is dead (40485335) | A WWOX per-molecule function assay |

## S8 (folder H)
The review states that concentrations inhibiting LDH in vitro (tens to hundreds of micromolar) lie at or above total plasma levels at effective antiseizure doses and well above the estimated free tissue level, that brain to plasma ratio in the rat is near one, and that a liver to plasma ratio of about thirty-five was measured once in the rat; it ranks LDH inhibition last in sensitivity among stiripentol's mechanisms. Secondary statement of other people's measurements by a manufacturer-authored review; its Table 2 LDH range rests on three rows (the 2015 report and Guyon 2022 at hundreds of micromolar, the first second-hand; Le Dudal 2019 from tens to hundreds of micromolar, indirect oxalate); not re-derived.  [the note also mentions a Table 2 resting on three rows]

## S9a (folder I)
- **The drug does not act as the title suggests.** The existing antiseizure drug raises surface alpha1 to indistinguishable from wild type; beta2 reaches 0.934 but the rise over untreated Q390X is not significant (p = 0.088, the text's own value) and gamma2 rises only from 0.474 to 0.572 (not significant, p = 0.106) [REPAIRED 2026-10-22]; it does not change total mutant gamma2 in cells; it raises HRD1 only slightly in untransfected cells and not in receptor-expressing cells; HRD1 and SEL1L are unchanged in the mouse; BiP is raised in wild type and not in the mutant. The authors accordingly offer a hedged mechanism ("at least partially" ER stress reduction and a moderate HRD1 rise) and name the drug's direct sodium-channel actions in the same paragraph. HRD1 is therefore not shown to mediate the drug's effect.

## S9b (folder I)
- **The seizure endpoint is within-animal, uncontrolled and statistically fragile.** Twenty-four-hour EEG before and after seven days of daily treatment, with no vehicle-injected EEG group. The per-animal plot (Figure 6C-E, opened) shows six paired animals (the reported baseline mean 15.58 matches six animals read from the colours), but the legend says N = 3 female mice and "one-tailed paired t-tests" while Methods say male and female (the blind audit resolved this in favour of the panel: six animals, since the reported baseline mean and standard error reproduce with n = 6, so the legend is the outlier) [REPAIRED 2026-10-22]; the count of discharges falls in all six animals as drawn (one of them from about 1 to 0, so it cannot show a reduction). The reported p of 0.0358 for the count is one-tailed; the two-tailed equivalent is about 0.07 (INFERENZA: doubling a symmetric one-tailed p), whereas time spent seizing stays below 0.05 either way. Event duration is not consistently reduced (one animal rises). Protein measurements and EEG come from different animals at different ages (one to one and a half months against two to three months). These are the cautions a card needs before citing "reduces seizures".

## S9c (folder I)
- **Exposure window (design fact).** Once-daily intraperitoneal treatment for seven days in both the lysate and the EEG experiments; no exposure measurement.

## S10a (folder J)
Flow shift of a library, not a protein recovery measure; a lysosome-inhibitor control did nothing, placing the loss on the proteasome.  [concerns two papers; judge this one]

## S10b (folder J)
- **Route of loss (library-wide).** E1 inhibition and proteasome inhibition raise the low-abundance population, Hsp70 inhibition raises it modestly, chloroquine does not, 29 degrees removes most of it (the Parkin atlas, 38378758, from related authors, notes that cold also slows turnover generally; this paper does not discuss it) (Figure 4, read from the image). The substrate (N-acetyl-aspartate) had no effect, but its intracellular level is unknown, so substrate stabilisation was not tested.

## S10c (folder J)
- **What it establishes (DATO, HEK293T, GFP fusion at one landing pad, undetectable endogenous enzyme).** 6,152 of 6,260 variants scored. **50 of 61 pathogenic missense variants score below 0.5** (Figure 6A, read from the image), the pathogenic variants that keep abundance are mostly at the catalytic site, and the three benign variants sit at about 0.8 to 1.0. For an enzyme, then, loss of abundance is the dominant pathogenic mechanism in this assay, with a catalytic-site minority that quantity-raising cannot fix. This is the nearest enzyme-class prior for "is a Q230P-class lesion a stability lesion by default": for ASPA, yes in about four of five pathogenic variants, as a measured quantity and in a non-native cell; the authors cite "about half" as the general figure and state it as an estimate.
