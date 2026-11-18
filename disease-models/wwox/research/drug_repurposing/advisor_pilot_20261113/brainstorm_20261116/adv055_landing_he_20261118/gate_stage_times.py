import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print('Usage: python3 gate_stage_times.py <repository root>. Times each of the four scan stages of scripts/public_release_gate.py once. Read-only.'); sys.exit(0)
import sys, time, importlib.util
from pathlib import Path
root = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("prg", root / "scripts" / "public_release_gate.py")
m = importlib.util.module_from_spec(spec); sys.modules["prg"] = m; spec.loader.exec_module(m)
res = {}
for name in ("scan_privacy_and_secrets", "scan_links", "scan_provenance", "scan_readme_consistency"):
    f = []; t = time.perf_counter(); getattr(m, name)(root, f); res[name] = (time.perf_counter() - t, len(f))
    print(name, "%.1f s" % res[name][0], "findings", len(f), flush=True)
print("STAGES_DONE total %.1f s" % sum(v[0] for v in res.values()), flush=True)
