#!/usr/bin/env python3
"""History privacy triage (IT8 P1): finding-level scan and deduplicating classifier.

Companion of `licence_inventory_it7.py history-privacy`, which prints only totals. This tool keeps
the finding-level records so that they can be deduplicated and classified. It is read-only toward
the repository (git object reads and a temporary directory outside it) and never rewrites history.

    privacy_triage_it8.py scan     --rev HEAD --public 10118886 --out DIR   # about 5 min on 4 cores
    privacy_triage_it8.py classify --out DIR                                # counts only, no matched text

PRIVACY RULE: `scan` writes the matched LINE TEXT to DIR/findings.jsonl so that a human can decide;
DIR must therefore be a local, git-ignored directory OUTSIDE the worktree (the operator's
`files/privacy_local_it8/`). The refusal below enforces "outside the repository". `classify` prints
blob and commit SHAs, paths, line numbers, classes and counts only; it never prints a matched string.

Population (same rule as the IT7 subcommand, widened in two ways, both reported separately):
  - text blobs (gate TEXT_SUFFIXES plus .html), at most 30 MB, whose blob is not a blob of the
    tip of `--rev`; the (blob, path) pair is the unit;
  - pairs are taken from every ref (`rev-list --objects --all`) and flagged: reachable from `--rev`,
    reachable from `--public` (the commit the hosting service serves), present in the IT7 population.
Binary files, PDFs, images and files over 30 MB are not scanned (see the report).
"""

from __future__ import annotations

import argparse
import collections
import gzip
import hashlib
import importlib.util
import json
import multiprocessing
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TOP = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                     cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()
IT7_REV = "619418f1"
MAX_BLOB = 30_000_000
# Detector vocabulary: the gate, its tests, the independent scanner (both historical locations),
# and the kernel spec. The IT7 subcommand lists the scanner under `framework/scripts/`, where it
# has never lived (it is `scripts/`); both are listed here.
SELF_REF = {"scripts/public_release_gate.py", "scripts/test_public_release_gate.py",
            "scripts/independent_privacy_scan.py", "scripts/test_independent_privacy_scan.py",
            "framework/scripts/independent_privacy_scan.py", "launch/KERNEL_SPEC.md"}


def git(*args, inp=None, text=True):
    r = subprocess.run(["git", *args], capture_output=True, text=text, input=inp, cwd=TOP)
    if r.returncode != 0:
        sys.stderr.write(r.stderr if text else r.stderr.decode("utf-8", "replace"))
        raise SystemExit(3)
    return r.stdout


def load_gate(path=None):
    spec = importlib.util.spec_from_file_location("legend_release_gate", path or TOP + "/scripts/public_release_gate.py")
    gate = importlib.util.module_from_spec(spec)
    sys.modules["legend_release_gate"] = gate
    spec.loader.exec_module(gate)
    return gate


def objects(rev_args):
    out = git("rev-list", "--objects", *rev_args)
    return [l.split(" ", 1) for l in out.splitlines() if " " in l]


def blob_sizes(shas):
    sizes = {}
    for l in git("cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)", inp="\n".join(shas) + "\n").splitlines():
        s, t, z = l.split()
        if t == "blob":
            sizes[s] = int(z)
    return sizes


def cat_blobs(shas):
    shas = list(shas)
    p = subprocess.Popen(["git", "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=TOP)
    import threading

    def feed():
        try:
            for s in shas:
                p.stdin.write((s + "\n").encode())
            p.stdin.close()
        except BrokenPipeError:
            pass
    threading.Thread(target=feed, daemon=True).start()
    for s in shas:
        hdr = p.stdout.readline().split()
        n = int(hdr[2])
        data = p.stdout.read(n)
        p.stdout.read(1)
        yield s, data
    p.wait()


def worker(args):
    chunk_id, pairs = args[0], args[1]
    gate = load_gate(args[2] if len(args) > 2 else None)
    gap = len(args) > 3 and args[3] == "gap"
    by = collections.defaultdict(list)
    for i, (s, p) in enumerate(pairs):
        by[s].append((i, p))
    out = []
    with tempfile.TemporaryDirectory(prefix=f"legend_privtriage_{chunk_id}_") as tmp:
        root = Path(tmp)
        ids = {}
        for s, data in cat_blobs(sorted(by)):
            for i, p in by[s]:
                name = p
                if gap:
                    if p.lower().endswith(".gz"):
                        try:
                            data = gzip.decompress(data)
                        except Exception:
                            continue
                    name = p + ".txt"  # scanned by content, whatever the original suffix
                tgt = root / f"h{i:06d}" / name
                tgt.parent.mkdir(parents=True, exist_ok=True)
                tgt.write_bytes(data)
                ids[f"h{i:06d}"] = (s, p, tgt)
        findings = []
        gate.scan_privacy_and_secrets(root, findings)
        cache = {}
        for f in findings:
            hid = f.path.split("/", 1)[0]
            if hid not in ids:
                continue
            s, p, tgt = ids[hid]
            if s not in cache:
                cache = {s: tgt.read_text(encoding="utf-8", errors="replace").split("\n")}
            lines = cache[s]
            ln = lines[f.line - 1] if 0 < f.line <= len(lines) else ""
            out.append({"blob": s, "path": p, "line": f.line, "code": f.code, "sev": f.severity, "text": ln[:2000]})
    return out


def population(a, gate):
    suffixes = set(gate.TEXT_SUFFIXES) | {".html"}
    tip_sha = {l.split()[2] for l in git("ls-tree", "-r", "--full-tree", a.rev).splitlines()}
    it7_tip = {l.split()[2] for l in git("ls-tree", "-r", "--full-tree", IT7_REV).splitlines()}
    objs_all = objects(["--all"])
    objs_rev = {tuple(x) for x in objects([a.rev])}
    objs_pub = {tuple(x) for x in objects([a.public])}
    objs_it7 = {tuple(x) for x in objects([IT7_REV])}
    sizes = blob_sizes(sorted({s for s, _ in objs_all}))
    pairs = sorted({(s, p) for s, p in objs_all if s in sizes and s not in tip_sha and sizes[s] <= MAX_BLOB
                    and "." + p.rsplit(".", 1)[-1].lower() in suffixes})
    meta = {}
    for s, p in pairs:
        meta[(s, p)] = {"in_rev": (s, p) in objs_rev, "in_public": (s, p) in objs_pub,
                        "in_it7_pop": (s, p) in objs_it7 and s not in it7_tip, "size": sizes[s]}
    return pairs, meta


def outdir(a):
    out = Path(a.out).resolve()
    top = Path(TOP).resolve()
    if out == top or top in out.parents:
        raise SystemExit("refusing: --out must be outside the repository (matched text is written there)")
    out.mkdir(parents=True, exist_ok=True)
    return out


def tip_population(a, gate):
    suffixes = set(gate.TEXT_SUFFIXES) | {".html"}
    pairs, meta = [], {}
    for l in git("ls-tree", "-r", "-l", "--full-tree", a.rev).splitlines():
        m, rest = l.split("\t", 1)
        _, typ, sha, size = m.split()
        if typ == "blob" and int(size) <= MAX_BLOB and "." + rest.rsplit(".", 1)[-1].lower() in suffixes:
            pairs.append((sha, rest))
            meta[(sha, rest)] = {"in_rev": True, "in_public": True, "in_it7_pop": False, "size": int(size)}
    return sorted(pairs), meta


def cmd_scan(a):
    out = outdir(a)
    gate = load_gate()
    pairs, meta = (tip_population if a.tip else population)(a, gate)
    n = max(1, a.jobs)
    chunks = [(i, pairs[i::n]) for i in range(n)]
    with multiprocessing.Pool(n) as pool:
        results = pool.map(worker, chunks, chunksize=1)
    with open(out / ("tip_findings.jsonl" if a.tip else "findings.jsonl"), "w", encoding="utf-8") as fh:
        total = 0
        for res in results:
            for r in res:
                r.update({k: v for k, v in meta[(r["blob"], r["path"])].items()})
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                total += 1
    with open(out / ("tip_population.json" if a.tip else "population.json"), "w") as fh:
        json.dump({"rev": git("rev-parse", a.rev).strip(), "public": git("rev-parse", a.public).strip(),
                   "pairs": len(pairs), "blobs": len({s for s, _ in pairs}),
                   "pairs_in_rev": sum(m["in_rev"] for m in meta.values()),
                   "pairs_in_public": sum(m["in_public"] for m in meta.values()),
                   "pairs_in_it7_pop": sum(m["in_it7_pop"] for m in meta.values()),
                   "pairs_other_refs_only": sum(not m["in_rev"] for m in meta.values()),
                   "findings": total}, fh, indent=1)
    print(f"pairs {len(pairs)}; findings {total}; written to {out}")


def cmd_gate_delta(a):
    """Before/after of a gate change over exactly the blobs that carried a finding (a rule that only
    removes findings cannot change a blob that had none). `--old-rev` names the commit holding the
    gate to compare against; the working-tree gate is the 'after'."""
    out = outdir(a)
    seen = {}
    for l in open(out / "findings.jsonl", encoding="utf-8"):
        r = json.loads(l)
        seen[(r["blob"], r["path"])] = 1
    pairs = sorted(seen)
    old_src = git("show", f"{a.old_rev}:scripts/public_release_gate.py")
    with tempfile.NamedTemporaryFile("w", suffix="_old_gate.py", delete=False) as fh:
        fh.write(old_src)
        old_path = fh.name
    n = max(1, a.jobs)
    res = {}
    for name, gp in (("before", old_path), ("after", None)):
        with multiprocessing.Pool(n) as pool:
            parts = pool.map(worker, [(i, pairs[i::n], gp) for i in range(n)], chunksize=1)
        res[name] = collections.Counter((r["blob"], r["line"], r["code"], r["sev"]) for part in parts for r in part)
    os.unlink(old_path)
    bf, af = res["before"], res["after"]
    print(f"blobs rescanned: {len(pairs)}")
    for name, c in (("before", bf), ("after", af)):
        by = collections.Counter(k[2] for k in c.elements())
        print(f"{name}: {sum(c.values())} findings (BLOCK {sum(v for k, v in c.items() if k[3] == 'BLOCK')}); by code: " + ", ".join(f"{k} {v}" for k, v in sorted(by.items())))
    gone = bf - af
    new = af - bf
    print(f"removed by the change: {sum(gone.values())} findings in {len({k[0] for k in gone})} blobs; codes: " +
          ", ".join(f"{k} {v}" for k, v in sorted(collections.Counter(k[2] for k in gone.elements()).items())))
    print(f"added by the change: {sum(new.values())}")
    for k in sorted(gone):
        print("  removed", k[0][:10], k[1], k[2])


GAP_TEXT_EXT = {"html", "js", "css", "patch", "diff", "cff", "example", "gitignore", "gz", "keep", "xml", "svg", "tex", "ini", "cfg"}


def cmd_gap_scan(a):
    """Close part of the coverage gap: history-only pairs whose suffix the gate does not read but
    which are text (html, js, css, patch, diff, cff, ...) or gzip-compressed text, scanned by
    content through the same gate function. PNG, PDF and other binaries remain NOT covered."""
    out = outdir(a)
    gate = load_gate()
    tip_entries = [(l.split()[2], l.split("\t", 1)[1]) for l in git("ls-tree", "-r", "--full-tree", a.rev).splitlines()]
    tip_sha = {s for s, _ in tip_entries}
    objs_rev = set(tip_entries) if a.tip else {tuple(x) for x in objects([a.rev])}
    if a.tip:
        tip_sha = set()
    sizes = blob_sizes(sorted({s for s, _ in objs_rev}))
    gate_suf = set(gate.TEXT_SUFFIXES)
    pairs = []
    for s, p in sorted(objs_rev):
        if s not in sizes or s in tip_sha:
            continue
        base = p.rsplit("/", 1)[-1]
        ext = base.rsplit(".", 1)[-1].lower() if "." in base else ""
        if ("." + ext) in gate_suf or ext not in GAP_TEXT_EXT:
            continue
        pairs.append((s, p))
    n = max(1, a.jobs)
    with multiprocessing.Pool(n) as pool:
        parts = pool.map(worker, [(i, pairs[i::n], None, "gap") for i in range(n)], chunksize=1)
    total = 0
    with open(out / ("tip_gap_findings.jsonl" if a.tip else "gap_findings.jsonl"), "w", encoding="utf-8") as fh:
        for part in parts:
            for r in part:
                r.update({"in_rev": True, "in_public": True, "in_it7_pop": False, "size": sizes[r["blob"]]})
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                total += 1
    c = collections.Counter((r["sev"], r["code"]) for part in parts for r in part)
    print(f"gap pairs scanned: {len(pairs)} ({len({s for s, _ in pairs})} blobs); findings {total}; by code: " +
          ", ".join(f"{k[0]}/{k[1]} {v}" for k, v in sorted(c.items())))


class _CachedHashlib:
    """Drop-in for the `hashlib` name inside the isolated scanner: same digests, memoised per input.
    The scanner hashes every word of every line, which made a history run exceed 19 minutes; the cache
    changes no digest and therefore no finding."""
    def __init__(self):
        self._c = {}

    def sha256(self, data=b""):
        d = self._c.get(data)
        if d is None:
            d = self._c[data] = hashlib.sha256(data)
        return d


def iso_worker(args):
    chunk_id, pairs = args
    spec = importlib.util.spec_from_file_location("legend_isolated_scan", TOP + "/scripts/independent_privacy_scan.py")
    scn = importlib.util.module_from_spec(spec)
    sys.modules["legend_isolated_scan"] = scn
    spec.loader.exec_module(scn)
    scn.hashlib = _CachedHashlib()
    by = collections.defaultdict(list)
    for i, (s, p) in enumerate(pairs):
        by[s].append((i, p))
    out = []
    errors = []
    with tempfile.TemporaryDirectory(prefix=f"legend_privtriage_iso{chunk_id}_") as tmp:
        root = Path(tmp)
        ids = {}
        for s, data in cat_blobs(sorted(by)):
            for i, p in by[s]:
                tgt = root / f"h{i:06d}" / p
                tgt.parent.mkdir(parents=True, exist_ok=True)
                tgt.write_bytes(data)
                ids[f"h{i:06d}"] = (s, p)
        findings, errs = scn.scan(root)
        for f in findings:
            hid = f.path.split("/", 1)[0]
            s, p = ids[hid]
            out.append({"blob": s, "path": p, "line": f.line, "sev": f.severity, "cat": f.category,
                        "match": f.match, "ctx": f.context})
        for e in errs:
            hid = e.split("/", 1)[0]
            errors.append({"blob": ids[hid][0], "path": ids[hid][1], "err": "unreadable as strict UTF-8 or I/O"})
    return out, errors


def cmd_scan_isolated(a):
    out = outdir(a)
    gate = load_gate()
    pairs, meta = (tip_population if a.tip else population)(a, gate)
    n = max(1, a.jobs)
    chunks = [(i, pairs[i::n]) for i in range(n)]
    with multiprocessing.Pool(n) as pool:
        results = pool.map(iso_worker, chunks, chunksize=1)
    total = 0
    with open(out / ("tip_isolated.jsonl" if a.tip else "isolated.jsonl"), "w", encoding="utf-8") as fh:
        for res, _ in results:
            for r in res:
                r.update({k: v for k, v in meta[(r["blob"], r["path"])].items()})
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                total += 1
    errs = [e for _, es in results for e in es]
    with open(out / ("tip_isolated_errors.json" if a.tip else "isolated_errors.json"), "w") as fh:
        json.dump(errs, fh)
    print(f"pairs {len(pairs)}; isolated-scanner findings {total}; unreadable pairs {len(errs)}; written to {out}")


# ---------------------------------------------------------------------------------------------
# classify: deduplicate and classify the finding-level records. Prints no matched text.
# ---------------------------------------------------------------------------------------------
CLASSES = ["public_or_bibliographic_identifier", "synthetic_fixture_or_example", "detector_text_or_rule_discussion",
           "false_positive_hex_or_common_word", "actual_personal_data", "potentially_identifying_clinical_linkage",
           "unresolved"]
UUID_RX = re.compile(r"(?<![0-9A-Za-z])[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}(?![0-9A-Za-z])")
SHORT_HEX_RX = re.compile(r"(?<![0-9A-Za-z])(?=[0-9A-Fa-f]*[0-9])[0-9A-Fa-f]{8,11}(?![0-9A-Za-z])")
HEX_RUN_RX = re.compile(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{32,}(?![0-9A-Fa-f])")
HEX_FRAGMENT_RX = re.compile(r"(?<![0-9A-Za-z])(?=[0-9A-Fa-f]*[0-9])[0-9A-Fa-f]{12,}(?![0-9A-Za-z])")
TOKEN_RX = re.compile(r"(?<![A-Za-z])[A-Za-z]{3,24}(?![A-Za-z])")
EMAIL_RX = re.compile(r"(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9_%+-])")
STUDY_RX = re.compile(r"(?i)\bPMID[\s:_-]*\d{6,9}\b|\bPMC\d{5,9}\b|\b10\.\d{4,9}/\S{3,}")
PUBLISHED_PATH_RX = re.compile(r"/(?:fulltext_dossiers|deepdive_manifests|page_adjudications)/|(?:PMID|PPR)\d+|CC-\d{8}[A-Z0-9-]*-[A-Z0-9]+-\d{2}")
RULE_TALK_RX = re.compile(r"(?i)\b(?:gate|detector|BLOCK(?:S|ED)?|REVIEW|pairing|public edition|not carried|parent-side|scan(?:ner)?|"
                          r"re-?identif\w*|parent-of-origin)\b")
FIXTURE_DOMAINS = ("example.org", "example.com", "example.net", "example.invalid", "example.test", "x.invalid", "e.st")
VARIANT_RX = [re.compile(r"(?i)(?:\bQ\s*230\s*P\b|\bp\.\s*\(?Gln\s*230\s*Pro\)?\b|\bGln\s*230\s*Pro\b)"),
              re.compile(r"(?i)\bc\.\s*1057\s*[-\N{MINUS SIGN}\N{EN DASH}]\s*2\s*A\s*>\s*G\b")]


class Blobs:
    """Blob reader with a small cache; returns the line the gate numbers as `line` (universal newlines)."""
    def __init__(self):
        self.cache = {}

    def line(self, sha, n, stored):
        if len(stored) < 2000:
            return stored
        if sha not in self.cache:
            if len(self.cache) > 8:
                self.cache.clear()
            raw = subprocess.run(["git", "cat-file", "blob", sha], capture_output=True, cwd=TOP).stdout
            self.cache[sha] = raw.decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "\n").split("\n")
        lines = self.cache[sha]
        return lines[n - 1] if 0 < n <= len(lines) else stored


def digest_labels():
    spec = importlib.util.spec_from_file_location("legend_isolated_ref", TOP + "/scripts/independent_privacy_scan.py")
    scn = importlib.util.module_from_spec(spec)
    sys.modules["legend_isolated_ref"] = scn
    spec.loader.exec_module(scn)
    gate_src = open(TOP + "/scripts/public_release_gate.py", encoding="utf-8").read()
    for d in set(scn.PRIVATE_IDENTIFIER_DIGESTS) | set(scn.CASEFOLD_IDENTIFIER_DIGESTS) | set(scn.PATH_CASEFOLD_IDENTIFIER_DIGESTS):
        assert d in gate_src, "digest sets of the gate and the isolated scanner diverged"
    lab = {}
    for i, d in enumerate(sorted(scn.PRIVATE_IDENTIFIER_DIGESTS)):
        lab[("x", d)] = f"X{i}"
    for i, d in enumerate(sorted(scn.CASEFOLD_IDENTIFIER_DIGESTS)):
        lab[("c", d)] = f"C{i}"
    for i, d in enumerate(sorted(scn.PATH_CASEFOLD_IDENTIFIER_DIGESTS)):
        lab[("p", d)] = f"P{i}"
    return lab, scn


def key(*parts):
    return hashlib.sha256("\x1f".join(parts).encode("utf-8", "replace")).hexdigest()[:16]


def norm(text):
    return re.sub(r"[^a-z0-9]+", "", text.casefold())


def classify_direct(line, path, lab, scn):
    """Return (class, subtype, incident key) for each located token of a DIRECT_IDENTIFIER finding."""
    res = []
    uu = [m.span() for m in UUID_RX.finditer(line)]
    sh = [m.span() for m in SHORT_HEX_RX.finditer(line)]
    skip = [m.span() for m in HEX_RUN_RX.finditer(line)] + [m.span() for m in HEX_FRAGMENT_RX.finditer(line)]
    for t in TOKEN_RX.finditer(line):
        if any(x <= t.start() and t.end() <= y for x, y in skip):
            continue  # the gate skips letters inside a 32+ hex run or a 12+ hex fragment with a digit
        w = t.group(0)
        e = hashlib.sha256(w.encode()).hexdigest()
        c = hashlib.sha256(w.casefold().encode()).hexdigest()
        label = lab.get(("x", e)) or lab.get(("c", c))
        if not label:
            continue
        a, b = t.span()
        hexlike = all(ch in "0123456789abcdefABCDEF" for ch in w)
        if hexlike and any(x <= a and b <= y for x, y in uu):
            span = next((x, y) for x, y in uu if x <= a and b <= y)
            u = line[span[0]:span[1]]
            if re.search(r"(?i)setid", line[max(0, span[0] - 12):span[0]]) or "DailyMed" in line:
                sub = "uuid:dailymed_setid"
            elif "/tmp/" in line[max(0, span[0] - 120):span[0]]:
                sub = "uuid:session_directory_name"
            elif "sigcom" in path.casefold() or "entity" in path.casefold():
                sub = "uuid:signature_commons_entity"
            else:
                sub = "uuid:other"
            res.append(("false_positive_hex_or_common_word", sub, key("uuid", u.lower())))
        elif hexlike and (any(x <= a and b <= y for x, y in sh) or line[a - 1:a].isdigit() or line[b:b + 1].isdigit()):
            res.append(("false_positive_hex_or_common_word", "hex_fragment_short_digest_or_sha", key("hex", norm(line[max(0, a - 12):b + 12]))))
        elif label.startswith("X") or label.startswith("C"):
            res.append(("actual_personal_data", f"name_token_in_text:{label}", key("name", label, norm(line))))
        else:
            res.append(("unresolved", "token", key("tok", label, norm(line))))
    for r in scn.PATH_ROOT.finditer(line):
        run = scn.PATH_RUN.match(line, r.start())
        if run is None:
            continue
        for w in scn.PATH_WORD.finditer(run.group(0)):
            f = hashlib.sha256(w.group(0).casefold().encode()).hexdigest()
            if ("c", f) in lab or ("p", f) in lab:
                res.append(("actual_personal_data", "machine_account_directory_in_path", key("path", run.group(0).casefold())))
    return res


def classify_email(line, path):
    res = []
    for m in EMAIL_RX.finditer(line):
        a = m.group(0).lower()
        local, dom = a.split("@")
        base = path.rsplit("/", 1)[-1]
        if dom.endswith(FIXTURE_DOMAINS) or dom.endswith(".invalid") or dom.endswith(".test"):
            res.append(("synthetic_fixture_or_example", "reserved_or_fake_domain", key("mail", a)))
        elif dom == "github.com" and local == "git":
            res.append(("false_positive_hex_or_common_word", "ssh_remote_not_a_mailbox", key("mail", a)))
        elif dom == "anthropic.com" and local.startswith("noreply"):
            res.append(("public_or_bibliographic_identifier", "vendor_noreply_trailer", key("mail", a)))
        elif "corpus_seed" in path or STUDY_RX.search(line) or re.search(r"(?i)corresponding author|fore_name", line):
            res.append(("public_or_bibliographic_identifier", "third_party_author_contact", key("mail", a)))
        elif base.startswith("test_") or "/tests/" in path:
            res.append(("synthetic_fixture_or_example", "test_file", key("mail", a)))
        else:
            res.append(("unresolved", "address", key("mail", a)))
    return res


def classify_rule(code, line, path, text):
    if path in SELF_REF:
        return [("detector_text_or_rule_discussion", "gate_or_scanner_or_spec", key(code, norm(line)))]
    both = all(rx.search(line) for rx in VARIANT_RX)
    if code == "REIDENTIFYING_VARIANT_COMBINATION" and both:
        return [("potentially_identifying_clinical_linkage", "reference_class_alleles_named_together", key(code, norm(line)))]
    if code in ("PARENT_OF_ORIGIN_ATTRIBUTED",):
        return [("public_or_bibliographic_identifier", "attributed_to_published_study", key(code, norm(line)))]
    if STUDY_RX.search(line) or PUBLISHED_PATH_RX.search(path):
        return [("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", key(code, norm(line)))]
    if RULE_TALK_RX.search(line):
        return [("detector_text_or_rule_discussion", "rule_discussion_in_records", key(code, norm(line)))]
    return [("unresolved", "block_rule", key(code, norm(line)))]


def introducing_commits():
    """blob -> list of (commit, date) that add or modify the blob; one pass over every ref, merges included."""
    out = subprocess.run(["git", "log", "--all", "-m", "--raw", "--no-abbrev", "--diff-filter=AM", "--format=C %H %cs %ct"],
                         capture_output=True, text=True, cwd=TOP).stdout
    res = collections.defaultdict(set)
    cur = None
    for l in out.splitlines():
        if l.startswith("C "):
            _, h, d, ct = l.split()
            cur = (h, d, int(ct))
        elif l.startswith(":") and cur:
            parts = l.split()
            res[parts[3]].add(cur)
    return res


# Manual adjudications of block-rule findings that no automatic rule above classified. Key: (blob
# prefix of 10, line, code); value: (class, sub-type, reason). Each was read in context; none is
# reproduced here. Anyone re-deriving the table can read the same line with `git cat-file blob`.
MANUAL = {
    ("09f94e358c", 118, "PARENT_OF_ORIGIN_PAIRING"): ("detector_text_or_rule_discussion", "rule_discussion_in_records", "review item about wording of third-party parental statements"),
    ("96c4e39628", 118, "PARENT_OF_ORIGIN_PAIRING"): ("detector_text_or_rule_discussion", "rule_discussion_in_records", "same sentence, later version"),
    ("7b89e919d6", 119, "PARENT_OF_ORIGIN_PAIRING"): ("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", "quotes a published variant's inheritance statement"),
    ("7b89e919d6", 119, "PARENT_OF_ORIGIN_REFERENCE_GENOTYPE"): ("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", "same line; the reference-genotype window word comes from neighbouring rule talk"),
    ("fe1e2d078c", 119, "PARENT_OF_ORIGIN_PAIRING"): ("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", "same as 7b89e919d6"),
    ("fe1e2d078c", 119, "PARENT_OF_ORIGIN_REFERENCE_GENOTYPE"): ("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", "same as 7b89e919d6"),
    ("fd357a2609", 28, "PARENT_OF_ORIGIN_REFERENCE_GENOTYPE"): ("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", "describes a published minigene paper's proband"),
    ("3b504b202d", 198, "PARENT_OF_ORIGIN_PAIRING"): ("detector_text_or_rule_discussion", "gate_or_scanner_or_spec", "battery script quoting the gate's own vocabulary regex"),
    ("d54c8937bb", 35, "CLINICAL_CASE_LINKAGE"): ("false_positive_hex_or_common_word", "common_phrase_patient_derived_cells", "generic phrase about patient-derived cell lines"),
    ("2f315577b7", 402, "PARENT_OF_ORIGIN_PAIRING"): ("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", "verbatim quote of a published cohort statement"),
    ("2f315577b7", 402, "PARENT_OF_ORIGIN_REFERENCE_GENOTYPE"): ("public_or_bibliographic_identifier", "third_party_published_case_or_cohort", "same line"),
}


def classify_file(path, lab, scn, blobs):
    groups = collections.OrderedDict()
    for l in open(path, encoding="utf-8"):
        r = json.loads(l)
        groups.setdefault((r["blob"], r["path"], r["line"], r["code"], r["sev"]), [r, 0])[1] += 1
    rows = []
    mismatch = 0
    for (blob, fpath, ln, code, sev), (r, n) in groups.items():
        line = blobs.line(blob, ln, r["text"])
        if code == "DIRECT_IDENTIFIER":
            cl = classify_direct(line, fpath, lab, scn)
        elif code == "EMAIL_ADDRESS":
            cl = classify_email(line, fpath)
        elif sev == "REVIEW" and code == "PUBLIC_BIBLIOGRAPHIC_AUTHOR":
            cl = [("public_or_bibliographic_identifier", "published_author_name_field", key(code, norm(line)))]
        else:
            cl = classify_rule(code, line, fpath, r["text"])
            cl = [MANUAL[(blob[:10], ln, code)] [:2] + (cl[0][2],) if cl[0][0] == "unresolved" and (blob[:10], ln, code) in MANUAL else cl[0]]
            cl = cl * n
        if code in ("DIRECT_IDENTIFIER", "EMAIL_ADDRESS") and len(cl) != n:
            mismatch += 1
            if os.environ.get('PRIVTRIAGE_DEBUG'):
                print('mismatch', blob[:10], ln, code, 'gate', n, 'located', len(cl))
        if not cl:
            cl = [("unresolved", "no_token_located", key(code, norm(line)))]
        for c, sub, k in cl:
            rows.append({**{x: r[x] for x in ("blob", "path", "line", "code", "sev", "in_rev", "in_public", "in_it7_pop")},
                         "cls": c, "sub": sub, "inc": k, "self": fpath in SELF_REF})
    if mismatch:
        print(f"note: {mismatch} (blob, line) groups where located tokens differ from the gate's finding count (counted by located token)")
    return rows


def segment(r):
    return "it7_population" if r["in_it7_pop"] else ("delta_after_it7" if r["in_rev"] else "other_refs_only")


def cmd_classify(a):
    out = outdir(a)
    lab, scn = digest_labels()
    blobs = Blobs()
    rows = classify_file(out / "findings.jsonl", lab, scn, blobs)
    tip_inc = set()
    if (out / "tip_findings.jsonl").exists():
        tip_rows = classify_file(out / "tip_findings.jsonl", lab, scn, blobs)
        tip_inc = {r["inc"] for r in tip_rows}
        print(f"tip rows classified: {len(tip_rows)}; tip incident keys: {len(tip_inc)}")
    intro = introducing_commits()
    first = {}
    for b, cs in intro.items():
        c0 = sorted(cs, key=lambda x: (x[2], x[0]))[0]
        first[b] = (c0[0], c0[1])
    tip_paths = {l.split("\t", 1)[1] for l in git("ls-tree", "-r", "--full-tree", a.rev).splitlines()}
    for r in rows:
        r["intro"] = first.get(r["blob"], (None, None))[0]
        r["intro_date"] = first.get(r["blob"], (None, None))[1]
        r["path_at_tip"] = r["path"] in tip_paths
        r["inc_at_tip"] = r["inc"] in tip_inc
    with open(out / "classified.jsonl", "w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")

    def table(title, sel):
        S = [r for r in rows if sel(r)]
        print(f"\n## {title}")
        print("| class | sub-type | occurrences | blobs | introducing commits | distinct incidents | incidents also at tip |")
        print("|---|---|---|---|---|---|---|")
        g = collections.defaultdict(list)
        for r in S:
            g[(r["cls"], r["sub"].split(":")[0] if r["cls"] != "false_positive_hex_or_common_word" else r["sub"])].append(r)
        for k in sorted(g):
            v = g[k]
            print(f"| {k[0]} | {k[1]} | {len(v)} | {len({r['blob'] for r in v})} | {len({r['intro'] for r in v if r['intro']})} | "
                  f"{len({r['inc'] for r in v})} | {len({r['inc'] for r in v if r['inc_at_tip']})} |")
        print("\n| class | occurrences | blobs | introducing commits | distinct incidents | blobs reachable from the served main | blobs whose path is still at the tip | incidents also at the tip |")
        print("|---|---|---|---|---|---|---|---|")
        for c in CLASSES:
            v = [r for r in S if r["cls"] == c]
            if not v:
                continue
            print(f"| {c} | {len(v)} | {len({r['blob'] for r in v})} | {len({r['intro'] for r in v if r['intro']})} | {len({r['inc'] for r in v})} | "
                  f"{len({r['blob'] for r in v if r['in_public']})} | {len({r['blob'] for r in v if r['path_at_tip']})} | {len({r['inc'] for r in v if r['inc_at_tip']})} |")

    table("BLOCK findings, whole population (IT7 population + delta + other refs)", lambda r: r["sev"] == "BLOCK")
    for seg in ("it7_population", "delta_after_it7", "other_refs_only"):
        table(f"BLOCK findings, segment {seg}", lambda r, seg=seg: r["sev"] == "BLOCK" and segment(r) == seg)
    table("REVIEW findings, whole population", lambda r: r["sev"] == "REVIEW")
    print("\n## unresolved BLOCK findings (blob, path, line, code, sub-type)")
    for r in rows:
        if r["cls"] == "unresolved":
            print(r["blob"][:10], r["path"], r["line"], r["code"], r["sub"], segment(r))
    return rows


def cmd_compare(a):
    """Isolated scanner vs gate: per category, blobs flagged by one, the other, both. Counts only."""
    out = outdir(a)
    pre = "tip_" if a.tip else ""
    iso = [json.loads(l) for l in open(out / f"{pre}isolated.jsonl", encoding="utf-8")]
    gate = [json.loads(l) for l in open(out / f"{pre}findings.jsonl", encoding="utf-8")]
    if not a.tip:
        iso = [r for r in iso if r["in_rev"]]  # other-refs-only pairs differ between runs (live refs)
        gate = [r for r in gate if r["in_rev"]]
    selfp = lambda r: r["path"] in SELF_REF
    gb = {r["blob"] for r in gate if r["sev"] == "BLOCK" and not selfp(r)}
    ga = {r["blob"] for r in gate if not selfp(r)}
    ib = {r["blob"] for r in iso if r["sev"] == "BLOCK" and not selfp(r)}
    print(f"scope: {'tip' if a.tip else 'history-only pairs reachable from the revision'}; self-referential paths (gate, scanner, their tests, kernel spec) excluded")
    print(f"gate: {len(gb)} blobs with a non-self BLOCK ({len(ga)} with any finding); isolated scanner: {len(ib)} blobs with a non-self BLOCK; in both: {len(gb & ib)}; "
          f"gate only: {len(gb - ib)}; scanner only: {len(ib - gb)}")
    print("\n| scanner category | severity | findings | blobs | distinct matches (casefold) | blobs also with a gate BLOCK | blobs the gate never flagged |")
    print("|---|---|---|---|---|---|---|")
    g = collections.defaultdict(list)
    for r in iso:
        if not selfp(r):
            g[(r["cat"], r["sev"])].append(r)
    for k in sorted(g):
        v = g[k]
        bl = {r["blob"] for r in v}
        print(f"| {k[0]} | {k[1]} | {len(v)} | {len(bl)} | {len({r['match'].casefold() for r in v})} | {len(bl & gb)} | {len(bl - ga)} |")
    bib = re.compile(r"(?i)affiliation|fore_name|last_name|\bPMID|\bdoi\b|\bet al\b|university|universit|institute|hospital|department|dipartimento")
    print("\n| scanner category (BLOCK) | blobs | in a bibliographic or affiliation context | other context |")
    print("|---|---|---|---|")
    for cat in sorted({k[0] for k in g if k[1] == "BLOCK"}):
        v = g[(cat, "BLOCK")]
        b1 = {r["blob"] for r in v if bib.search(r["ctx"]) or "corpus_seed" in r["path"]}
        b2 = {r["blob"] for r in v} - b1
        print(f"| {cat} | {len({r['blob'] for r in v})} | {len(b1)} | {len(b2)} |")
    errs = json.load(open(out / f"{pre}isolated_errors.json"))
    print(f"\nscanner read errors (undecodable as strict UTF-8): {len(errs)} pairs, {len({e['blob'] for e in errs})} blobs")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="finding-level scan; writes matched line text to a local directory outside the repository")
    s.add_argument("--rev", default="HEAD")
    s.add_argument("--public", default="development/main", help="commit served by the hosting service")
    s.add_argument("--out", required=True)
    s.add_argument("--jobs", type=int, default=4)
    s.add_argument("--tip", action="store_true", help="scan the text blobs of the tip itself instead of the history-only population")
    s.set_defaults(fn=cmd_scan)
    c = sub.add_parser("classify", help="deduplicate and classify findings.jsonl (prints no matched text)")
    c.add_argument("--rev", default="HEAD")
    c.add_argument("--out", required=True)
    c.set_defaults(fn=cmd_classify)
    gp = sub.add_parser("gap-scan", help="scan history-only text-like files the gate's suffix list skips (html, js, css, gz, ...) through the gate, by content")
    gp.add_argument("--rev", default="HEAD")
    gp.add_argument("--out", required=True)
    gp.add_argument("--jobs", type=int, default=4)
    gp.add_argument("--tip", action="store_true", help="scan the same kinds of files at the tip instead of in history")
    gp.set_defaults(fn=cmd_gap_scan)
    g = sub.add_parser("gate-delta", help="before/after counts of a change to public_release_gate.py over the blobs that carried a finding")
    g.add_argument("--old-rev", default="HEAD", help="commit holding the gate to compare against")
    g.add_argument("--out", required=True)
    g.add_argument("--jobs", type=int, default=4)
    g.set_defaults(fn=cmd_gate_delta)
    cp = sub.add_parser("compare", help="isolated scanner vs gate per category (counts only)")
    cp.add_argument("--tip", action="store_true")
    cp.add_argument("--out", required=True)
    cp.set_defaults(fn=cmd_compare)
    i = sub.add_parser("scan-isolated", help="same population through scripts/independent_privacy_scan.py (matched text kept in the local directory)")
    i.add_argument("--rev", default="HEAD")
    i.add_argument("--public", default="development/main")
    i.add_argument("--out", required=True)
    i.add_argument("--jobs", type=int, default=4)
    i.add_argument("--tip", action="store_true", help="scan the text blobs of the tip instead of the history-only population")
    i.set_defaults(fn=cmd_scan_isolated)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
