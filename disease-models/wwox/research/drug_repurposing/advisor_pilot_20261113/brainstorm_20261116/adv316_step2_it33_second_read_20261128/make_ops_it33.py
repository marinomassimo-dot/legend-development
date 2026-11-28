"""IT33: build the propagate ops for the ADV-316 step 2 wording (after the blind second read). Run from the repository root."""
import json
from pathlib import Path
D = Path(__file__).resolve().parent
paper = [
 {"op":"replace-within","id":"PAPER 228",
  "old":"The double-mutant `AAV9-DM` cut hepatic vector genome copies **~127-fold** (the authors' own figure)",
  "new":"`AAV9-DM` (five point mutations; the paper never says \"double mutant\") cut hepatic vector genome copies **~127-fold** (the authors' own figure; vg per µg liver DNA at week 9, mouse, one dose of 1 × 10¹¹ vg)"},
 {"op":"replace-within","id":"PAPER 228",
  "old":"dropped peak whole-animal signal from **7.3 × 10⁷** to **5.8 × 10⁵** (a factor of **126**, i.e. about two orders of magnitude)",
  "new":"dropped peak whole-animal signal from **7.3 × 10⁷** to **5.8 × 10⁵** (a factor of **126**, i.e. about two orders of magnitude; text-stated in Results 3.3 as average radiance from the ventral side of the animal, citing Figure 2 but printed in no panel, statistic not stated, while Fig 3 liver means at week 3 are about 1.7 × 10⁷ and 1 × 10⁵ by eye, so Fig 3 does not reproduce the text peaks)"},
 {"op":"replace-within","id":"PAPER 228",
  "old":"put **significantly fewer** vector genomes into the brain than the parent capsid",
  "new":"put **significantly fewer** vector genomes into the brain than wild-type AAV9 (about 60-fold lower per µg DNA, Fig 4D by eye, one star; the ~8-fold is packaging only; brain Fluc RNA is not different from AAV9, Fig 5D, and the authors call the capsid \"minimally affecting CNS tropism\")"},
 {"op":"replace-within","id":"PAPER 362",
  "old":"overexpression; a fractionation blot without a mitochondrial marker row",
  "new":"endogenous protein in the mitochondrial data, a marker row on separate fractionation blots only"},
 {"op":"replace-within","id":"PAPER 362",
  "old":"A nanomolar PMA with ionophore induces",
  "new":"PMA at 0.55 nM with the ionophore A23187 at 0.30 µM (the ionophore is micromolar) induces"},
 {"op":"replace-within","id":"PAPER 362",
  "old":"with confocal co-localisation percentages falling after the stimulus (WWOX about 84 to 60 percent, n = 3)",
  "new":"with percent-localisation-to-mitochondria values falling after the stimulus (Fig 4E; MitoTracker Red is named only in Methods; WWOX about 84 to 60 percent by eye, n = 3 in the legend, replicate unit undefined; TNF-alpha leaves WWOX at about 86)"},
 {"op":"replace-within","id":"PAPER 362",
  "old":"(every manipulation is overexpression; the rescue shown is one blot pair)",
  "new":"(the WWOX constructs, EGFP-WWOX and the dominant-negative dn-WWOX, belong to the binding, FRET, immunoprecipitation and rescue work, while the mitochondrial data, Fig 4C to 4E, are endogenous protein in MOLT-4; the rescue shown, Fig 5B, is one blot pair with no n)"},
 {"op":"replace-within","id":"PAPER 362",
  "old":"(the fractionation blot has no mitochondrial or cytosolic purity marker row)",
  "new":"(no fractionation blot carries both markers: Fig 4C has an alpha-tubulin row under the cytosol lanes only, Fig 4D a cytochrome C row under the mitochondria lanes that is faint in Control, 0 and 1 h and strong at 2 and 3 h, by eye; Fig 4D prints % reduction rows, WWOX 91, 25 and 12 at 1, 2 and 3 h, with no method stated, and the 1 h WWOX band is almost absent by eye while the 2 and 3 h bands cannot be checked)"},
]
claims = [
 {"op":"replace-within","id":"CLAIM 009",
  "old":"(MOLT-4 cells, a fractionation blot without a mitochondrial marker row and confocal co-localisation percentages, n = 3)",
  "new":"(MOLT-4 cells, fractionation blots with a cytosolic marker on one blot and a mitochondrial marker that is not constant across lanes on another, and percent-localisation-to-mitochondria values, n = 3, replicate unit undefined)"},
 {"op":"replace-within","id":"CLAIM 009",
  "old":"with overexpression or dominant-negative constructs and no Wwox-null cell",
  "new":"with, in the MOLT-4 paper, endogenous protein in the mitochondrial data (its constructs belong to binding, imaging and rescue work; the Jurkat paper as recorded in PAPER 361), and no Wwox-null cell in a mitochondrial readout (MDA-MB-231, which does not express WWOX, appears in Fig 5B for IκBα degradation only)"},
 {"op":"replace-within","id":"CLAIM 009",
  "old":"the leg 'WWOX localises to mitochondria under stress' is carried by",
  "new":"the leg 'WWOX localises to mitochondria under stress' (the MOLT-4 paper's manipulation is a PMA plus ionophore differentiation stimulus after which WWOX falls in the mitochondrial fraction at 1 h and partly returns at 2 to 3 h in Fig 4D, with printed reductions still 25 and 12 percent; the Discussion cites earlier work, not tested there, on WWOX relocation to mitochondria after high-concentration PMA; and the word stress occurs once on its page, in a reference title) is carried by"},
 {"op":"replace-within","id":"CLAIM 011",
  "old":"so the toxicity **is quantified and is not disease-specific on these data**",
  "new":"so the toxicity **is quantified and shows no significant treatment x genotype interaction on these data** (power unknown, so equal toxicity is not shown; the genotype main effect, F(1,28) = 6.181, p = 0.0192, is reported with an uncorrected p and the 65Q vehicle bar is already about 7 percent below the 27Q vehicle bar by eye; the replicate unit is not defined, Fig 4A states n = 4 biological replicates and Fig 4B only F(1,28), which implies 8 per cell if balanced; the 100 ng/mL dose is in the Fig 4B legend, the 24 h duration only in the Results text)"},
 {"op":"replace-within","id":"CLAIM 047",
  "old":"dropped peak whole-animal transgene signal from **7.3 × 10⁷** to **5.8 × 10⁵** (a factor of **126**, about two orders of magnitude), and put **significantly fewer** vector genomes into the brain than its parent capsid.",
  "new":"dropped peak whole-animal transgene signal from **7.3 × 10⁷** to **5.8 × 10⁵** (a factor of **126**, about two orders of magnitude; text-stated in Results 3.3 from the ventral-side image, printed in no panel, while Fig 3 liver means at week 3 are about 1.7 × 10⁷ and 1 × 10⁵ by eye), and put **significantly fewer** vector genomes into the brain than wild-type AAV9 (about 60-fold lower per µg DNA, Fig 4D by eye; the ~8-fold is packaging only; brain Fluc RNA is not different, Fig 5D)."},
]
wm = [
 {"op":"replace-within","heading":"BLOCK 2 — claim registry mirror (baseline)",
  "old":"a liver-de-targeted capsid costs ~8-fold packaging and brain exposure",
  "new":"the liver-de-targeted capsid AAV9-DM costs ~8-fold packaging and about 60-fold fewer brain vector genomes per µg DNA than wild-type AAV9 (mouse; brain RNA not different)"},
]
for n, o in (("ops_paper_it33.json", paper), ("ops_claims_it33.json", claims), ("ops_working_model_it33.json", wm)):
    (D / n).write_text(json.dumps(o, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ok")
