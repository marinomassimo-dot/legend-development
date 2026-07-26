# WWOX-Q230P red-team — deliverables

**Verdict: WEAKENED** — structural spine sound (AlphaFold SDR pLDDT 90.3, helix–degron PAE 1.4 Å),
mechanistic half (CMA via LRSVQ) extrapolated from P252A and under-determined.

## Read first
- `WWOX_Q230P_redteam_report.md` — full dossier (verdict, premises, alternatives, predictions, druggability, failure modes, missing info)
- `discriminating_experiment.md` — the one 2-week experiment that settles it

## Figures
- `fig_plddt_pae.png` — AlphaFold model confidence (the model is NOT the weak link)
- `fig_helix.png` — helix boundaries 227-249, π-bulge at Q230, burial
- `fig_contacts_burial.png` — lid packs on degron; C299 abuts the catalytic triad
- `fig_kferq.png` — all 5 KFERQ motifs; LRSVQ non-canonical, ERLIQ canonical
- `fig_falsification_matrix.png` — alternative-model scorecard
- `fig_druggability.png` — no druggable pocket at the interface

## Tables (CSV)
- `premises_epistemic_table.csv`, `alternatives_scorecard.csv`
- `confidence_table.csv`, `dssp_secondary_structure.csv`, `contact_burial_table.csv`
- `kferq_scan.csv`, `pocket_analysis.csv`
- `residue_ledger.csv`, `provenance_data_vs_inference.csv`

## Structural inputs — **not shipped, reconstructed on demand**

Only `AF_SDR.pdb` (the SDR crop actually used by the figures) is committed. The remaining
structural inputs are **not shipped**: they are third-party public data, and are regenerated
or downloaded on demand, then checked against the SHA-256 values recorded during the
public-data audit:

```bash
# local derivation only (uses the AlphaFold model already in this repository)
python3 disease-models/wwox/analysis/scripts/prepare_redteam_structures.py \
    --alphafold-pdb disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb \
    --output-dir <dir>

# additionally retrieve the AlphaFold PAE JSON and RCSB entry 1WMV
python3 disease-models/wwox/analysis/scripts/prepare_redteam_structures.py \
    --alphafold-pdb disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb \
    --output-dir <dir> --fetch-public
```

- `AF-Q9NZC7-F1.pdb` (AlphaFold DB model) and `AF-Q9NZC7-F1-PAE.json` — downloaded on demand.
  AlphaFold DB data are CC BY 4.0 and require AlphaFold / EMBL-EBI attribution.
- `AF_nohelix.pdb` — the in-silico lid-removal control, **deterministically reconstructed**
  by deleting the ATOM records for residues 227–249.
- `1WMV.pdb` — the only experimental WWOX structure (WW2 domain, **not** the SDR) — downloaded
  on demand; RCSB PDB data-use terms and the primary-structure citation apply.
