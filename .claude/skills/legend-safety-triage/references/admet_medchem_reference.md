# ADMET-AI + medchem — operational reference

Local tools (CPU, pip). The web-apps/APIs are optional and involve external traffic → do not use them without explicit authorization.

## Installation
```bash
pip install admet-ai        # ADMET-AI v2 (Chemprop v2, TDC-trained). GPU optional, CPU ok.
uv pip install medchem datamol   # medchem 2.0.5 (RDKit/datamol). Py>=3.9.
# optional: mamba install -c conda-forge lilly-medchem-rules
```

## ADMET-AI — quick use
```python
from admet_ai import ADMETModel
model = ADMETModel()
preds = model.predict(smiles="CC(=O)Oc1ccccc1C(=O)O")   # dict or endpoint DataFrame
```
CLI: `admet_predict --data_path mols.csv --save_path out.csv` (SMILES column).

### Key endpoints for a CNS target (pediatric context)
| Category | Endpoint | Why it matters |
|---|---|---|
| Distribution | **BBB penetration (Martins)** | ⭐ must reach the CNS; null BBB = of little use systemically |
| Distribution | PPBR, VDss | free fraction, distribution |
| Toxicity | **hERG** | cardio risk (QT) |
| Toxicity | **DILI** | hepatotoxicity |
| Toxicity | AMES | mutagenicity |
| Absorption | Caco-2, HIA, Pgp-substrate | permeability/absorption |
| Metabolism | CYP (2D6/3A4/2C9...) | drug interactions |
| Excretion | clearance (hepatocyte/microsome), half-life | dosing |
| Physchem | solubility, lipophilicity (logP) | formulability |

ADMET-AI also reports the **percentile** relative to DrugBank → read the value *in context*, not in absolute terms.

## medchem — quick use
```python
import datamol as dm
from medchem.rules import RuleFilters
from medchem.structural import CommonAlertsFilters   # PAINS/NIBR/ChEMBL alerts

mols = [dm.to_mol(s) for s in smiles_list]
rules = RuleFilters(rule_list=["rule_of_five", "rule_of_veber", "rule_of_cns"])
df_rules  = rules(mols=mols)          # pandas DataFrame, pass/fail per rule
df_alerts = CommonAlertsFilters()(mols=mols)
```

### Useful rules/catalogues
- **rule_of_cns** (and CNS-MPO if available) — priority for a CNS target.
- rule_of_five (Lipinski), rule_of_veber, lead-like — general drug-likeness.
- **PAINS / NIBR / ChEMBL alerts** — pan-assay interference and toxicophores: a hit here is often grounds for discarding.
- Complexity vs ZINC thresholds; functional-group detection.

## Interpretation → BLOCK-1 traffic light
- 🔴 toxicophore/serious alert · high predicted hERG or DILI · **null BBB** (systemic use, CNS target) · AMES positive.
- 🟡 one rule violated · uncertain permeability/solubility · CYP with possible interactions.
- 🟢 no alert · CNS rules respected · ADMET in favourable ranges.

> All of this is **prediction (`IPOTESI`)**. The validation step (a real hERG assay, a BBB measurement, etc.) must always be named as the next step. medchem itself warns: the filters are *context-specific guidelines*, to be combined with target knowledge.
