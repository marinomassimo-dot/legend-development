"""IT 2026-11-25 (IT24): applies increment2/edits_it23b.py (ADV-282) and edits_it24.py (compound values, ADV-283) to the card packets with the
text-level, idempotent machinery of apply_it23.py. Cards are rebuilt by repurposing_bridge.py afterwards. Run from the repository root.
Hypothesis level; nothing here is medical advice."""
import importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
PREV = HERE.parent / "it_adv280_281_238_20261125"
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

if __name__ == "__main__":
    A = load("apply_it23", PREV / "apply_it23.py")
    adv282 = load("edits_it23b", PREV / "increment2" / "edits_it23b.py").EDITS
    mine = load("edits_it24", HERE / "edits_it24.py").EDITS
    A.E.EDITS = adv282 + mine
    A.EXTRA = []
    print("card edits", A.cards())
