# IGF axis in WWOX-deficient animal models (desk research; proposals, no conclusions)
Paths below are relative to /tmp/legend-dream3-rgzkfo9h/after/disease-models/wwox/research/ unless stated.

## 1. What the repository already holds
- lde/lde rat, GH: PMID 17803050 reports plasma GH "slightly lower in mutant than in normal rats, the difference was not significant" and that the dwarfism "cannot be explained solely by low levels of plasma GH" (deepdive_manifests/PMID17803050.json lines 325, 345). The abstract overstates this; the premise "low pituitary GH causes lde dwarfism" is rejected as DIS-012 (dismissal_ledger_current.md lines 301-311). Sample is small (the ledger says so, line 307; I did not find the exact n). A non-significant difference is not a normal value.
- lde/lde rat, same paper: BUN about 3.2-3.5x normal and creatinine raised, but glucose, Ca, Na, K, Cl and triglycerides comparable to normal (PMID17803050.json line 121). So uraemia without the mouse null's hypoglycaemia.
- Wwox-null mouse rescued by neuronal AAV (PMID 34747138): glucose, seizures, feeding, growth, fertility and bone normalise together; glucose is one tail-prick reading, n = 5 per group, fed state and IGF-1 not stated (fulltext_dossiers/PMID34747138.md lines 7-9; deepdive_manifests/PMID34747138.json line 587). Treated mice also stop seizing, so hypoglycaemia and growth may be secondary (dossier line 9).
- Mouse null serum chemistry (PMID 18487609): 50% lower calcium; the supplementary serum table is unavailable (deepdive_manifests/PMID18487609.json lines 125, 428). Nothing there on IGF-1 or GH that I found.
- Human GWAS lists naming IGF1 or IGFBP7 beside WWOX (PMID 22479346, PMID 28763065) are separate loci. PMID 22479346 makes no measurement in WWOX carriers (deepdive_manifests/PMID22479346.json line 353). The infant brain-volume paper has IGFBP7 and WWOX as separate hits (analysis/human_prenatal_infant_wave1_20260921.md lines 439, 570). These are human data, not animal models, and carry no WWOX-IGF link.
- Staged lead DL-MECH-180 (discovery_ledger_current.md lines 4628-4635; lead_staging/plan/lead_dream3_igf.json): serum IGF-1 plus GH in the Wwox-null / neuronal-rescue cohort against weight-matched controls. Tagged IPOTESI/exploratory.

## 2. Searched vs not re-searched
- Not re-searched: the ledger's literature statement that no source measures the IGF axis in any WWOX-deficient animal (dismissal_ledger_current.md line 311), and the lde GH finding (read from the manifest).
- Searched: PubMed `(Wwox OR WWOX) AND (IGF-1 OR "insulin-like growth factor" OR "growth hormone" OR IGFBP)` gave 4 records (PMIDs 38056170, 28763065, 23666471, 22479346), the same four the ledger lists. I only checked identities against the ledger's description; I did not open their abstracts. A second, broader query was malformed by OR precedence (261,460 hits) and I discarded it.
- NOT checked: Embase or other databases, bioRxiv (unavailable here), full texts of any paper, WWOX-null liver/IGFBP expression data, Wwox conditional knockouts (bone, muscle, liver) for IGF data, the 2019 muscle-specific deletion paper, IGFBP measurements (nothing in the repository), GEO datasets.

## 3. Rival explanations and the proposed measurement
Proposed single measurement (same as DL-MECH-180, which I judge sound): serum IGF-1 and GH together in Wwox-null pups at a stage with reduced growth, against wild-type littermates matched for body weight and feeding (restricted-fed or seizure-burden-matched controls), with fed glucose recorded. IGFBP-3 could be added from the same sample, but the repository has no basis for it.
- Low IGF-1 with high GH: GH resistance, consistent with a consequence of malnutrition or illness.
- Low IGF-1 with low GH: pituitary or hypothalamic origin (a brain effect, which would fit rescue by neuronal AAV).
- Normal IGF-1 with small size: a local or tissue-autonomous effect (skeletal or muscle).
- Low IGF-1 equally low in weight-matched wild-type: the axis follows size, not genotype (the ledger's falsifier).
Caveats: a mouse result does not transfer to the rat lde model or to humans; serum IGF-1 is largely hepatic and WWOX is not detected in liver after AAV rescue (dossier line 9), which makes the uncoupling interpretable but untested.

## 4. Possibly out of date
- The discovery-ledger and lead JSON cite a folder `dream3_20261108/` (README) that is not in this snapshot (only dream1_20261108 and dream2_20261108 exist); the reference cannot be followed here.
- DIS-012 text still says "0 PubMed records" for WWOX AND "growth hormone" (line 308); the dated UPDATE on line 311 corrects it (4 records for the wider query). I confirmed 4 today (2026-11-08).
- The dismissal entry is in Italian; the lead JSON tag "IPOTESI" is Italian. Not an error.

## 5. Tool calls and time
About 5 shell commands (2 greps/listings across the snapshot, 3 targeted line reads), 0 file-reader calls, 2 PubMed searches (1 usable, 1 discarded); no full-text retrievals. Roughly 5 minutes of wall time (not measured precisely).
