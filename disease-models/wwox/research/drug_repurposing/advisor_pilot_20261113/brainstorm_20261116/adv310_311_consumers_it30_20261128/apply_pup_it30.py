"""IT30: apply the two post-round-2 fragments to the live pup brief by exact-once replacement. Run from the repository root; --dry writes nothing."""
import importlib.util, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
S = HERE.parent / "adv310_311_consumers_it29_20261128" / "edits_it29b.py"
spec = importlib.util.spec_from_file_location("e", S); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
x = {a["tag"][:3]: a for a in E.X}
OLD_TAIL = "so at the Cheng frequency the pilot size in litters is set by the knockout need, and the same litters would supply the wild types if these are about 25 percent of the pups (Q45)."
NEW_TAIL = ("so, if wild types are at least about 13 percent of the pups (the pilot needs twice as many wild types as knockouts, so twice the 6.5 percent knockout frequency; 10.2 percent suffices at 5.1 percent), "
            "the pilot size in litters at the Cheng frequency is set by the knockout need and the same litters would supply the wild types; at the Mendelian 25 percent the 27 to 45 knockout litters would give about 47 to 79 wild types "
            "against the 24 to 32 needed, and below those thresholds the wild-type need would set the litter count (Q45).")
t6_old = x["T06"]["new"]; assert t6_old.count(OLD_TAIL) == 1
t6_new = t6_old.replace(OLD_TAIL, NEW_TAIL).replace("27 to 45 litters at the Cheng 2020 knockout frequency of 5.1 to 6.5 percent, DERIVED, rounded up", "27 to 45 litters at the Cheng 2020 knockout frequency of 5.1 to 6.5 percent, DERIVED at 7 pups per litter, rounded up", 1)
t9_old = x["T09"]["new"]
t9_new = t9_old.replace("and to the morphology and histology panels)", "and to the brain weight, brain water content and histology panels)")
assert t9_new != t9_old and t6_new != t6_old
B = Path("disease-models/wwox/research/drug_repurposing/experiment_brief_presidio013_sci_20261116/current_text_adv143_it_20261121/PUP_BRIEF_CURRENT_IT_20261121.md")
t = B.read_text(encoding="utf-8")
for tag, old, new in (("T06", t6_old, t6_new), ("T09", t9_old, t9_new)):
    n = t.count(old)
    if n != 1:
        if t.count(new) == 1: print("already", tag); continue
        raise SystemExit(f"COUNT {n} for {tag}")
    t = t.replace(old, new, 1)
if "--dry" not in sys.argv: B.write_text(t, encoding="utf-8")
print("fragments 2", "dry" if "--dry" in sys.argv else "applied")
