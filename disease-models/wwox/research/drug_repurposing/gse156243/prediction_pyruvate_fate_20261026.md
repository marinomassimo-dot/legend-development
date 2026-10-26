# Which way does the KO organoid push pyruvate at transcript level: toward lactate (LDH) or toward oxidation (PDH)? — fixed before running

Declared 2026-10-26 by the Orchestrator. Exploratory. Not medical advice; no dose, route or suitability.
Everything below that is not WWOX data is NOT WWOX EVIDENCE.

## Why this question, and what the paper does and does not give
Lucas-Clarke et al. (Brain Communications 2026, PMID 42909904) show in Drosophila, with an Abeta42 transgene, Wwox knockdown raising
Ldh and lactate, and genetic Ldh reduction partly rescuing locomotion. The paper measures no pyruvate, no PDH or PDK, no flux, no oxygen
consumption, no NAD/NADH (manifest entry 49), and its metabolic schematic has no node for pyruvate dehydrogenase (entry 44). It therefore
gives no direct support to a PDH hypothesis. What it implies is a branch point: pyruvate goes to lactate through LDH or to acetyl-CoA through
PDH, and a raised Ldh pushes toward the first. LEGEND's own hypotheses sit on that branch (HYP-20260709-01 ketogenic, HYP-20260709-05 dichloroacetate,
which inhibits the PDH kinases). In the KO organoid both LDHA (+0.75, up) and PDHA1 (+1.00, up) were found up on 2026-10-25/26, which is
not the pattern a one-way push to lactate would give. This asks whether the branch point itself shifts, read in the way the transcripts allow.

## What it can and cannot say
- CAN say: whether the ratio of expression of the lactate-forming gene (LDHA, with LDHB) to the pyruvate-oxidising complex (PDHA1, PDHB, DLAT,
  DLD) differs between KO and WT, and whether that difference is outside what random gene pairs show.
- CANNOT say: flux. PDH is controlled by phosphorylation (PDK, PDP), LDH by substrate and NADH; a transcript ratio is not an enzyme-activity ratio.
  Nothing here says pyruvate is or is not diverted to lactate in the organoid.

## Fixed readout
Per library, log2 of (LDHA + LDHB) CPM over (PDHA1 + PDHB + DLAT + DLD) CPM; the KO-minus-WT difference of that log ratio, with the four KO
libraries against two WT libraries shown individually (no test is quoted from six libraries). Null: 10,000 random draws of a "fate-A" set of two genes and a
"fate-B" set of four genes from the expressed universe, the same statistic; reported as the fraction of random pairs with a difference at least as
large in absolute value. Culture-time slope of the same ratio in GSE150123 with the between-line interval, as before.

## Prediction (written before running)
P1. The KO log-ratio is higher than WT (a push toward lactate), but by less than the LDHA shift alone, because PDHA1 is also up.
P2. The shift is NOT outside the random-pair distribution (the two arms move together, so a ratio hardly moves).
P3. The ratio falls with culture time in GSE150123 (LDHA falls with time; PDH genes are flat or rise), so any KO excess is as consistent with
    a less advanced tissue as with a WWOX effect.

## What would change the reading
- A ratio shift well outside random pairs would make "pyruvate diverted to lactate" a transcript-supported statement and would put the LDH / PDH
  branch point at the centre of the metabolic hypotheses.
- A ratio at the random centre says the two arms rise together and the transcriptome does not favour one fate.

---

# RESULT (appended 2026-10-26, after the run; the prediction above is unchanged)

Script: `hif1a_pdk_chain.py --pyruvate-fate` (the same reproducible script; the first run of this calculation was a terminal fragment and was moved into
the script before any number was recorded, which is the third time in this line of work that a result was nearly quoted from a fragment; the script
reproduces the fragment exactly). 10,000 random 2-gene/4-gene pairs, seed 20261025, expressed universe 19,694 genes.

| per library | cko1 | cko2 | cko3 | cko4 | cwt1 | cwt2 |
|---|---|---|---|---|---|---|
| log2[(LDHA+LDHB)/(PDHA1+PDHB+DLAT+DLD)] | 1.346 | 1.349 | 1.295 | 1.242 | 1.222 | 1.669 |

KO mean +1.308, WT mean +1.446, **KO minus WT = -0.138**; **74 percent of random pairs have a KO-WT difference at least that large in absolute
value (0.743)**. Culture-time slope of the same ratio in GSE150123 (WWOX-unperturbed spheroids): -0.650 per log10 day, between-line interval
[-1.418, +0.119] over five lines, which includes zero.

## The prediction, point by point
- **P1 falsified in sign.** I expected a push toward lactate; the KO ratio is slightly LOWER than WT, not higher.
- **P2 held.** The shift is not outside what random gene pairs give.
- **P3 not supported.** The ratio shows no detectable dependence on culture time; the age comparison is inconclusive for this quantity.

## The limit that matters most
The two wild-type libraries differ from each other (1.222 and 1.669, a spread of 0.45) by more than the KO mean differs from the WT mean (0.14), and
the four KO libraries lie in a narrow band (1.242 to 1.349). With two WT libraries the WT mean rests on one library for its upper value; the
-0.138 is inside that noise. The random-pair test says the same in its own terms: nothing distinguishable.

## Reading, at the strength it has
EXPLORATORY. In the one human WWOX-knockout neural transcriptome on hand, the transcript ratio of the lactate-forming arm to the pyruvate-oxidising arm
is not shifted, so the transcripts give no support to a diversion of pyruvate to lactate. Taken with the two earlier analyses on this organoid (HIF1A-PDK:
glycolytic targets up, PDK1 down; ATF4 route: target set lower than chance), three routes to a lactate-forming state have now each been checked at
transcript level in human neural tissue and none shows its distinguishing signature. This is not evidence that lactate or PDH flux is normal
(transcript is not flux; PDH is phosphorylation-controlled; lactate was not measured), and it is not a contradiction of the fly result, which is reported
only with an Abeta42 transgene.
