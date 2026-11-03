# MolNexus preliminary qualification (IT23 P5, 2026-11-03)

Scope: key-less GitHub API and raw files only; no clone, no download of data, no training, no account, no contact with authors. Nothing copied into this repository. Not medical advice.

## Decision

NOT USABLE YET. Both gates are unresolved: no licence of any kind, and no checkpoint at any official location. No inference test was attempted and none is possible.

## Repository state read (2026-11-03)

- Repository: ZJUFanLab/MolNexus; default branch main (the only branch); no tags; releases list empty (so no release assets).
- Created 2026-09-09; last push 2026-09-23 (commit "Edit README", 2026-09-23); three commits in total. Not archived. Repository size reported 49,640 KB.
- GitHub API licence field: null.
- Description: knowledge-graph-enhanced prediction of biomedical molecular relationships. Components: BioNexKG (graph over compounds, proteins, genes, metabolites), CPI binary prediction, three-class CGI (compound-gene) and CMI (compound-metabolite) prediction, and an agent "skill" wrapper.

## Licence, recorded separately

- Code: none found. Paths searched (raw, main): LICENSE, LICENSE.md, LICENSE.txt, COPYING all return 404; README.md, skills/README.md, skills/MolNexus/SKILL.md contain no licence, copyright or terms-of-use text; API licence field null. A tree listing (non-truncated) shows no licence-like file anywhere. Under default copyright this means all rights reserved.
- Data (BioNexKG demo graph, task folds, feature tables, about 190 MB in git): none found; same paths. The README does not state provenance or terms of the underlying sources. Whether the demo is a subset of a fuller graph is not stated.
- Weights: none found, and none exist to license (see below).

## Checkpoint state

- The repository tree contains no model/ directory and no .pt files. .gitignore excludes checkpoints/, *.pt, *.pth, *.ckpt, outputs/, results/, logs/, so weights were never committed.
- README and SKILL.md contain no link to Hugging Face, Zenodo, figshare or any other host. Independent searches: Hugging Face model search for MolNexus returned an empty list; Zenodo search for MolNexus BioNexKG returned zero hits.
- What the code expects (local, not downloadable): CGI and CMI load from model/cgi and model/cmi (CGI wrapper globs *.pt recursively; patterns such as fold*/best_checkpoint_fold*.pt; CMI matches ensemble_N-style names, with an optional same-stem .json sidecar read by checkpoint_io.py). CPI wrapper selects model/cpi/<split>/ensemble_N.pt for split Warm, CCS, DCS or PCS. Five-fold ensembles.
- Further inputs the repo does not supply: compound features must be KPGT-type features ("real external compound features"); the shipped feature tables are demo subsets, so any compound outside them needs an external KPGT feature computation, itself a separate tool with its own licence (not assessed). Random-feature fallback is deliberately disabled.
- Only way to obtain weights from the repository as published: run the Slurm training scripts (scripts/train_*.sh). Training is out of scope and not performed.

## Publication terms

No paper, DOI or citation is linked in the README, skill README or SKILL.md. A PubMed title/keyword query for MolNexus and BioNexKG returned zero records. No data/model availability statement could be read; PMID/DOI: none found. The Graphical_abstract.png suggests a manuscript exists or is in preparation; not verified.

## Semantics of outputs (from README, SKILL.md, config.py)

- CGI classes, fixed order: CGI-N no significant change, CGI-D down-regulation, CGI-U up-regulation. CMI likewise CMI-N/D/U. Output predictions.csv with per-class probabilities and per-fold probabilities (fold columns saved by default).
- Unit/direction: direction only (up/down/none) of a gene or metabolite after compound exposure. Not stated in the files read: unit, fold-change or significance threshold defining N versus D/U, cell line, dose, time, platform (the naming cmap_name in the registry hints at a CMap-like source; unverified), and whether D/U are defined relative to vehicle. These must be found in the paper or data documentation before any use.
- CPI is binary interaction (no direction, no potency).
- Relevance to LEGEND: separating binding (CPI) from downstream transcript or metabolite change (CGI/CMI) is the useful design. The N class could only serve as a weak, context-bound "not observed to change in the training source" label. It must be treated as unknown-not-negative: absence of significant change in a specific cell context and power does not exclude an effect in WWOX-deficient neurons. Observed rows (KG) and model predictions must stay separate; neither is validation.

## Reopening condition

Reopen when BOTH hold: (1) a LICENSE file in the repository root (or an explicit licence statement in the README) covering code, plus stated terms for the BioNexKG data and the source databases; and (2) a checkpoint set (CGI and/or CMI five-fold ensembles with their json sidecars where used) at an official URL (GitHub release, Hugging Face or Zenodo) with size and checksum, ideally with the linked paper's availability statement defining the N/D/U threshold and context. At that point the minimal test is: fetch the declared files, run the CGI wrapper in dry-run and then one --execute on the shipped demo input on CPU, comparing with the shipped demo labels. Check also the KPGT feature source licence for any compound outside the demo set.

## Not verified

Repository contents beyond the files named (script internals read only by grep, not fully); whether a manuscript or preprint exists; the licences of the upstream data sources; KPGT licence; whether weights are available on request (not pursued; no contact permitted); any content in repository history other than the three listed commits (not diffed).
