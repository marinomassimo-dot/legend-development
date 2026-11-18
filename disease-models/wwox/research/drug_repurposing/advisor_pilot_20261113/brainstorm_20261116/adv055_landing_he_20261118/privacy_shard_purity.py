import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print('Usage: python3 privacy_shard_purity.py <repository root>. Compares the full privacy scan with a scan of a file sample. Read-only; about 5 minutes.'); sys.exit(0)
import sys, time, json, random, importlib.util
from pathlib import Path
from dataclasses import asdict
root = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("prg", root / "scripts" / "public_release_gate.py")
m = importlib.util.module_from_spec(spec); sys.modules["prg"] = m; spec.loader.exec_module(m)
key = lambda f: json.dumps(asdict(f), sort_keys=True)
t = time.perf_counter(); full = []; m.scan_privacy_and_secrets(root, full); tfull = time.perf_counter() - t
print("FULL privacy scan %.1f s, %d findings, severities %s" % (tfull, len(full), sorted({f.severity for f in full})), flush=True)
fp = sorted({f.path for f in full})
tracked = [p for p in m.tracked_paths(root)]
random.seed(7); sample = set(random.sample(tracked, 1500)) | set(fp)
m.ONLY_PATHS = frozenset(sample)
t = time.perf_counter(); part = []; m.scan_privacy_and_secrets(root, part); tpart = time.perf_counter() - t
print("SHARD (%d files incl. all %d files with findings) %.1f s, %d findings" % (len(sample), len(fp), tpart, len(part)), flush=True)
fk = sorted(key(f) for f in full if f.path in sample); pk = sorted(key(f) for f in part if f.path in sample)
only_tree = [f for f in part if f.path not in sample]
print("IDENTICAL on the sampled files:", fk == pk, "| findings outside the sample emitted by the shard run:", len(only_tree), "| full-run findings with a path outside any file (tree-level):", sum(1 for f in full if not f.path or f.path not in set(tracked)), flush=True)
print("PURITY_DONE", flush=True)
