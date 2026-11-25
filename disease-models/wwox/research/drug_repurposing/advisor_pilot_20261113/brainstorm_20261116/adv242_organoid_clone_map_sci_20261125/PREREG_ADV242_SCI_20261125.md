# ADV-242 pre-registration: GSE156243 library-to-clone/batch map and clone-level removals (SCI; hypothesis level; not medical advice)

Written in the job scratch folder while a gated push held the worktree; committed afterwards unchanged (digest and time recorded beside it). Written before opening the GEO sample records or the paper's methods in this task. Effort high, no delegate, no spend; held files only.

## Disclosed prior reading (not blind)
ADV-069 recorded two knockout clusters (cko1+cko2, cko3+cko4) from expression, without a clone map. ADV-239 showed that for the Wnt readouts and most glycolytic genes all four knockout libraries lie above both wild types.

## The map
Accepted only if a source states it: GEO sample titles, characteristics or descriptions, or the paper's methods, legends or supplement. Expression clustering is not a map. A statement that is about the study's lines in general, but does not tie libraries to clones, is recorded as such and is not a map. Exit 20 minutes after this file's time stamp if the map is not stated.

## Removal rule (only if libraries are tied to clones)
* Scale and items: as in ADV-239 (log2(CPM+1), same genes and sets): Wnt readouts; LDHA, HK2, SLC2A1, EPAS1; PDK1; HIF1A; MYC; NPY, GAD1, GAD2.
* Leave-one-library-out (all six) and clone level: each knockout clone alone (mean of its libraries) against the wild-type mean.
* **clone-dependent**: a clone alone gives the opposite sign, or less than 0.50 of the all-library effect.
* **same in both clones**: neither. This does not upgrade ADV-239's "not testable": with one parental line as control and two knockout clones the arms stay below 3. The check can weaken a reading, not strengthen it to robust.
* If clones are confounded with batch or differentiation, say so; no removal separates them.

## What would change a reading
A clone-dependent item that a listed consumer carries gets proposed wording naming it ("seen in one of two knockout clones"). If no item is clone-dependent, wording changes only by stating the number of clones.

## Predictions
* P1: the held sources tie each knockout library to a clone (probability I assign: 0.4).
* P2: if so, the Wnt set and LDHA, HK2, SLC2A1, EPAS1 are the same in both clones.
* P3: units per arm are recoverable from held files for at least one of GSE268132, GSE327470, GSE274921.
