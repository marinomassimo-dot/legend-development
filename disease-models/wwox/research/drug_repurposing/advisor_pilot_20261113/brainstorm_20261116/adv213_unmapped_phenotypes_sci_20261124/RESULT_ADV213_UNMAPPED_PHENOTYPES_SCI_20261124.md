# RESULT ADV-213 (SCI window AB): which reproducible WWOX phenotypes the 58 dossiers do not reach

Hypothesis level; reference genotype class; no dose, no treatment recommendation, nothing is medical advice. Pre-registration frozen at `PREREG_ADV213_TIME_UTC.txt` (SHA-256 in `PREREG_ADV213_SHA256.txt`, commit dd15cb677) before any dossier decision line was opened. No delegate, no model call, no spend, no contact, no new source. Tables: `decision_lines.tsv` (extraction, all 58) and `coverage_map.tsv` (labels).

## Answer first
**Reach is wide and the unreached part is small.** Of the 16 frozen phenotype classes, 9 have three or more direct dossiers (circuit, myelin, energy, cofactor, lipid and redox classes carry 6 to 16 each), 1 is thin (developmental timing, one dossier) and 6 have none. Of those six, three are already carried by an INV or RP row (proteostasis and integrated stress response, systemic and somatic laboratory signs, glia and neuroinflammation), one is partly carried (kinase and growth signalling through WW-domain partners: lithium is carried, the docking and Tau limb is not), and **two are carried by nothing: Golgi, glycosylation and trafficking, and genome stability; a third, partner routing, is carried by nothing and has no molecule.** Three gaps survive the four-field rule. **Recommend the GSK3B-Tau limb (kinase signalling) as the next strand; drop the genome-stability gap; and do not extend the myelin strand with a tenth compound.**

## Deviations from the pre-registration, stated
1. Only 2 of 58 dossier READMEs use the exact heading "Current decision". I widened the extraction, before reading any content, to: title, opening paragraph, any bold-labelled paragraph containing decision, disposition, parked or closed (48 of 58 have one), and the queue README's checkpoint paragraph (all 58 have one). The labels below rest on those texts, not on the full dossiers.
2. The pre-registered "thinly reached" rule (all direct dossiers parked on one missing anchor) would apply to nearly every class, because the dossiers share an anchor (next section). I therefore flagged "thin" by count (fewer than three direct dossiers) and report the shared-anchor finding separately.

## What the dossiers share (the surprise)
In a keyword screen of the 58 decision texts (not a classification), 44 contain a reopening condition or an open, unresolved or unmeasured item and 32 of those also name exposure or a measured amount. Read by hand, the decisions repeat one anchor across otherwise unrelated classes: a **WWOX-specific functional response at a measured, attributable exposure**. Examples: creatine and ascorbic acid (transcript or nominal-only), clemastine, citicoline and squalene (same-tract first-sheath and conduction denominator), thiamine and riboflavin (cofactor occupancy), KBr, rufinamide, lamotrigine and stiripentol (matched exposure in a WWOX preparation). The map therefore says that **adding classes does not reduce uncertainty; one shared measurement would**. Nothing here reopens any dossier.

## Coverage map (class, direct dossiers, carriers, verdict)
| class | direct dossiers | carried by | verdict |
|---|---|---|---|
| C1 network hyperexcitability, bursting, rebound | 16 | INV-03, INV-05, RP-016, RP-024, RP-025 | reached |
| C2 inhibitory hypofunction and recruitment | 12 | INV-05 (GABA-A subtype), RP-019, RP-038, RP-042 | reached |
| C3 developmental timing, chloride polarity, cell fate | 1 (taurine) | RP-044, INV-17, the chloride deepening of this mandate | thin, carried |
| C4 myelin and oligodendroglial maturation | 9 | INV-06, INV-12, RP-017 | reached (over-covered) |
| C5 axonal conduction and intrinsic channels | 6 | INV-18 | reached |
| M1 energy and mitochondrial function | 16 | INV-07, RP-033 | reached |
| M2 cofactor, one-carbon, amino acids | 8 | none needed | reached |
| M3 lipid, sterol, membrane supply | 6 | RP-036 | reached |
| M4 redox and glutathione | 7 | INV-08 | reached |
| S1 WW-partner kinase and growth signalling | 0 (calcium alpha-ketoglutarate adjacent) | partly: RP-026 (lithium, seizure assay), RP-038 (ErbB4 only) | gap, partly carried |
| S2 partner routing and relocalisation | 0 | none | gap, uncarried |
| P1 proteostasis, ISR, autophagy | 0 | INV-02, INV-13, RP-015, RP-018, RP-037 | gap, carried (not ranked) |
| P2 Golgi, glycosylation, trafficking | 0 | none | gap, uncarried |
| G1 genome stability | 0 | none | gap, uncarried |
| Y1 systemic and somatic | 0 | RP-035 (laboratory findings only) | gap, carried (not ranked) |
| Z1 glia composition and neuroinflammation | 0 (three redox dossiers adjacent) | INV-14, RP-019, RP-039 | gap, carried (not ranked) |

Boundary of the taxonomy: structural malformation and neuronal migration (the prenatal architecture claim) are not a class of their own; they sit in C3 and would be a gap there if they were. Vision and dysphagia sit in Y1 and have no molecule in the held record.

## Negative results already on record, by reached class (from the decision lines; not reopened)
Circuit: topiramate infant trial without a significant effect on its focal-seizure endpoint; gabapentin and brivaracetam did not identify selective suppression of excess excitatory input; rufinamide's comparator started from a different intrinsic phenotype. Myelin: clemastine's conduction rescue used a different drug; citicoline's marker rise is confounded by precursor proliferation. Energy and cofactor: creatine failed its two-model criterion; riboflavin's RNA signal failed adult transfer; triheptanoin's controlled study did not establish efficacy; uridine raised two pools without restoring mtDNA in the comparator. Redox: sulforaphane's WWOX sulfur genes were absent from its add-on list; selenite's medium already supplies selenium.

## Ranked gaps (at most five; four fields each; scores a/b/c/d on 0 to 2)
| rank | gap | held source and replication unit | molecule or class | opposing mechanism | discriminating outcome | a b c d | total |
|---|---|---|---|---|---|---|---|
| 1 | **S1: WWOX as a physical GSK3B brake (docking motif, Tau limb)** | one residue-mapped primary (five orthogonal assays, endogenous interaction in mouse brain) plus a second paper whose abundance datum is withdrawn (single-lane densitometry); two papers, one weak | GSK3 inhibitor class (lithium already carried as a seizure candidate; a selective inhibitor has no row; no WWOX-null test of any selective inhibitor exists in the held record) | the interaction is S9-independent and its microtubule limb is cell-free and only partly restored, so inhibiting the kinase may not touch the WWOX-specific output; seizure benefit of lithium could be off-GSK3B | Tau S396/S404 phosphorylation and neurite outgrowth in WWOX-deficient neurons with a selective inhibitor against lithium, with docking-motif mutant as control | 1 1 1 1 | **4** |
| 2 | P2: Golgi, glycosylation, trafficking | one preprint (one siRNA, mRNA-only verification, unit = cells, controls unstated; my ADV-205 result) plus a non-neural interactome co-purification with no measured coupling | substrate-supply class used in congenital glycosylation disorders (sugar or nucleotide-sugar precursors), nothing WWOX-specific | the lectin shift is a knockdown or off-target effect (no second siRNA, no rescue); precursor supply may not limit the pathway | HPA lectin binding with rescue under a second independent knockdown, then precursor response | 0 1 1 1 | 3 |
| 3 | G1: ATM-linked genome stability | one primary plus murine B-cell observations (no CNS transfer) | none pediatric-feasible in the held record | effect restricted to proliferating non-neural cells | none accessible in neurons | 1 1 0 0 | 2 |
| not ranked | S2 partner routing | one overexpression-dependent example | none named | overexpression artefact | none | 0 0 0 0 | fails the four-field rule |
| not ranked | P1, Y1, Z1 | carried | see carriers | | | | covered, not ranked |

Scores are mine and rest on registry and working-model lines plus my own ADV-205 reading; the "d" scores follow the README's feasibility definition and mean only that a formulation or pediatric experience exists for the class, never an exposure at site.

## Recommendation, and what to drop
* **Recommend: S1, the GSK3B-Tau limb, with a cheap first step before any compound strand:** search the held WWOX-deficient proteomic and phosphoproteomic tables for GSK3B substrate phosphorylation and Tau sites, because the one claim that put abundance on the table was withdrawn. If those held tables are silent, the strand opens with the docking-motif control rather than a drug. It would change the lithium decision (is the single in vivo result on-mechanism) and select between lithium and a selective inhibitor.
* **Drop: the genome-stability gap (G1)** (lowest score, no accessible neuronal outcome). **Do not extend: the myelin strand with a further compound** (nine direct dossiers, parked on one anchor); the same holds for C1 (sixteen) and M1 (sixteen). That is a recommendation about where the next dossier would not add information, not a ruling on any parked compound.
* The shared measurement above is the more valuable next move than any single class; ADV may prefer to read this before choosing.

## Limits
Labels are my reading of decision lines (not of full dossiers) and could differ with the dossiers' full text; the taxonomy is frozen but not unique; reproducibility rests on registry and model lines, not on re-reading papers; the keyword screen is a screen; no paper was re-read, so no receipt.
