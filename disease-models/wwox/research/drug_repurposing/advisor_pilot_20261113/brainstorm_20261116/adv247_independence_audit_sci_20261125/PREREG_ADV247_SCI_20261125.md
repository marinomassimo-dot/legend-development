# ADV-247 pre-registration: independence audit of the carried small-n transcript inferences (SCI; hypothesis level; not medical advice)

Frozen 2026-11-25T02:48:53Z, before any source was reopened for this task. Effort high, no delegate, no spend, no contact. Scope: the 35 rows of ADV-239's `ranked_inferences_adv239.tsv`, with its consumer counts.

## What I already know (not blind)
ADV-244: the four knockout organoid libraries of GSE156243 are one CRISPR clone, against two organoids of the parental line. ADV-242: units of three comparator deposits from GEO records. ADV-239: unit identifiers per deposit; GSE158684 is one pool per genotype; the CAGE set has one library per arm; Hussain 2019 RNA-seq is on neurospheres, 2 knockout and 3 wild type.

## Unit taxonomy (what a "replicate" can be)
| Code | The replicate is | Independent for a genotype or perturbation effect? |
|---|---|---|
| ORG | a separate organism: one animal or one person per sample | yes (litter, sex and batch are noted, not counted) |
| DER | a separately derived clone or line (own editing event, own reprogramming, own donor) | yes for the derivation; several clones of one donor share the donor |
| CULT | a separate culture, organoid or differentiation of one clone or line | no: replicates of one derivation |
| TECH | the same material measured again (wells, libraries of one RNA preparation, lanes) | no |
| POOL | one library made from several organisms or cultures | the pool is one unit |
| CELL | cells or nuclei of one preparation | no |
| NS | the sources do not say | unknown |

## Effective n
Per arm, the number of distinct units at the level where the difference between the arms was created: animals or people for germline and conditional knockouts and variants; separately derived clones or lines for edited or silenced cells (the unedited parental line counts as one); pools for pooled material; preparations for cell-level data. When both arms come from one donor line, donor n is 1 and is stated. Libraries of the same animal or clone count once.

## Dispositions (per inference, by the worse arm)
* **independent**: stated n equals effective n (this can still be n = 1 or 2; the number is given).
* **non-independent (effective n)**: the stated n counts units that are not independent; both numbers given.
* **not stated**: the sources do not let the unit identity be determined.

## Reading rule
Every unit statement is read in two places (methods text, sample record, figure legend, supplement). With only one, it is marked "one source". An expression pattern is not evidence of unit identity. The ADV-244 streaming method is used only where the text cannot answer and the edits are published (under 2 GB, removed afterwards by name).

## Predictions
* P1: the share of the 35 inferences disposed "non-independent" is between 0.35 and 0.55.
* P2: no inference from an animal deposit (GSE215425, GSE158681, GSE158682) is non-independent.
* P3: for the Hussain 2019 neurosphere RNA-seq, whether each library is a separate animal is not stated.
* P4: at least one inference is "not stated" for a reason the streaming method cannot settle.

## Rejecting observation
If every inference other than the organoid rows is independent, the generalisation from ADV-244 adds nothing, and that is the result.

Stop at 120 minutes in two increments; anything not read is listed as not read.
