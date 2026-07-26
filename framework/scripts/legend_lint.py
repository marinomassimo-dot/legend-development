#!/usr/bin/env python3
"""LEGEND structural LINT engine (mechanizable subset).

Paths point to the public, disease-level layer. All four required current files
live under ``disease-models/wwox/registries/``; absence of any one produces the
fail-closed ``BLOCK_SYSTEM`` signal.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass

CURRENTS = [
    "disease-models/wwox/registries/working_model_current.md",
    "disease-models/wwox/registries/claim_registry_current.md",
    "disease-models/wwox/registries/paper_registry_current.md",
    "disease-models/wwox/registries/literature_tracking_log_current.md",
]
DISCOVERY_LEDGER = "disease-models/wwox/research/discovery_ledger_current.md"
SESSION_COMMIT_LOG = "disease-models/wwox/registries/session_commit_log.md"
DISMISSAL_LEDGER = "disease-models/wwox/research/dismissal_ledger_current.md"
RECEIPT_LEDGER = "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
STATE_MANIFEST = "framework/state/state_manifest_current.md"
RATCHET_BASELINE = re.compile(
    r'(?m)^registry_only_fulltext_declarations_baseline:\s*(\d+)\s*$'
)
RATCHET_IDS = re.compile(
    r'(?m)^registry_only_fulltext_declaration_ids:\s*(\[[^\n]*\])\s*$'
)
RECEIPT_LEDGER_PATH = re.compile(r'(?m)^fulltext_ledger_path:\s*(\S+)\s*$')

VALID_CLAIM_STATES = {
    "consolidated baseline", "in observation", "conflicting evidence",
    "flagged for review", "background only", "archived",
}
VALID_PAPER_STATES = {
    "discovered", "screened", "filtered_in", "filtered_out", "processed",
    "claim_linked", "integrated", "flagged_for_review", "background_only", "superseded",
}

WIKILINK_PAPER = re.compile(r'\[\[paper_registry_current#PAPER\s+(\d+)\]\]')
WIKILINK_CORPUS = re.compile(r'\[\[paper_registry_current#CORPUS\s+P(\d+)\]\]')
WORKING_MODEL_MIRROR = re.compile(
    r'^#\s+BLOCK 2\b[^\n]*claim registry mirror[^\n]*\n(.*?)(?=^#\s+BLOCK 3\b|\Z)',
    re.I | re.M | re.S,
)
MIRROR_ROW_ID = re.compile(r'^\|\s*(\d+)\s*\|', re.M)

# Premise/negative discipline tags are matched bilingually (canonical vocabulary may be kept
# in the original Italian or translated): PREMESSA/PREMISE, DEFAULT_DA_MANUALE/DEFAULT_FROM_TEXTBOOK.
PREMISE_TAG_RE = re.compile(r'(?:PREMESSA|PREMISE):\s*(DATO|INFERENZA|DEFAULT_DA_MANUALE|DEFAULT_FROM_TEXTBOOK)')
DEFAULT_PREMISE_RE = re.compile(r'(?:PREMESSA|PREMISE):\s*(?:DEFAULT_DA_MANUALE|DEFAULT_FROM_TEXTBOOK)')
REVIVAL_RE = re.compile(r'REVIVAL_TRIGGER|RIAPERTO|REOPENED|ROVESCIAT|OVERTURNED|RITIRATO|WITHDRAWN|NON REGGE|DOES NOT HOLD|FALSO|FALSE', re.I)

@dataclass
class Finding:
    severity: str
    code: str
    message: str

class LintResult:
    def __init__(self, findings):
        self.findings = findings
    @property
    def verdict(self):
        sevs = {f.severity for f in self.findings}
        if "BLOCK_SYSTEM" in sevs:
            return "BLOCK_SYSTEM"
        if "BLOCK_BATCH_COMMIT" in sevs:
            return "BLOCK_BATCH_COMMIT"
        if "WARN_BUT_PROCEED" in sevs:
            return "WARN"
        return "PASS"
    @property
    def blocks_deepdive(self):
        """A DEEP_DIVE (read-only) stops ONLY on BLOCK_SYSTEM."""
        return any(f.severity == "BLOCK_SYSTEM" for f in self.findings)
    @property
    def blocks_commit(self):
        """A BATCH_COMMIT stops on any BLOCK_*."""
        return any(f.severity.startswith("BLOCK_") for f in self.findings)

def parse_ids(text, kind):
    return re.findall(r'^##\s+' + kind + r'\s+(\d+)\b', text, re.M)

def parse_corpus_ids(text):
    return re.findall(r'^##\s+CORPUS\s+P(\d+)\b', text, re.M)

def working_model_claim_mirror_findings(working_model_text, claims_text):
    """Require the Working Model's BLOCK 2 mirror to contain every canonical claim ID."""
    findings = []
    match = WORKING_MODEL_MIRROR.search(working_model_text)
    if not match:
        return [Finding(
            "BLOCK_BATCH_COMMIT",
            "CLAIM_MIRROR_MISSING",
            "Working Model has no parseable BLOCK 2 claim-registry mirror",
        )]

    registry_ids = parse_ids(claims_text, "CLAIM")
    mirror_ids = MIRROR_ROW_ID.findall(match.group(1))
    for claim_id in sorted(set(registry_ids) - set(mirror_ids)):
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT",
            "CLAIM_MISSING_FROM_MIRROR",
            f"CLAIM {claim_id} exists in claim_registry but is absent from the Working Model mirror",
        ))
    for claim_id in sorted(set(mirror_ids) - set(registry_ids)):
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT",
            "ORPHAN_CLAIM_IN_MIRROR",
            f"CLAIM {claim_id} appears in the Working Model mirror but not in claim_registry",
        ))
    for claim_id in sorted({item for item in mirror_ids if mirror_ids.count(item) > 1}):
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT",
            "DUPLICATE_CLAIM_IN_MIRROR",
            f"CLAIM {claim_id} is duplicated in the Working Model mirror",
        ))
    return findings

def split_blocks(text, kind):
    pat = re.compile(r'^##\s+' + kind + r'\s+(\d+)\b', re.M)
    ms = list(pat.finditer(text))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out.setdefault(m.group(1), []).append(text[m.end():end])
    return out

def field(block, name):
    m = re.search(r'^\*\*' + re.escape(name) + r':\*\*\s*(.+?)\s*$', block, re.M)
    return m.group(1) if m else None

def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()

def _check_ids_states(findings, text, kind, valid_states):
    blocks = split_blocks(text, kind)
    for cid, bodies in blocks.items():
        if len(bodies) > 1:
            findings.append(Finding("BLOCK_BATCH_COMMIT", "DUPLICATE_ID",
                                    f"{kind} {cid} duplicated ({len(bodies)} times)"))
        for body in bodies:
            st = field(body, "Status")
            if st is not None and st not in valid_states:
                findings.append(Finding("BLOCK_BATCH_COMMIT", "INVALID_STATUS",
                                        f"{kind} {cid}: invalid status '{st}'"))

def _check_discovery_ids(findings, text):
    """Reject ambiguous discovery-ledger anchors created by parallel appends."""
    ids = re.findall(
        r'^###\s+(?:[^\w\n]*\s*)?((?:DL|FM)-[A-Z]+-?\d+)\b',
        text,
        re.M,
    )
    for item_id in sorted(set(ids)):
        count = ids.count(item_id)
        if count > 1:
            findings.append(Finding(
                "BLOCK_BATCH_COMMIT",
                "DUPLICATE_DISCOVERY_ID",
                f"{item_id} duplicated in the discovery ledger ({count} times)",
            ))

def _check_dismissals(findings, text):
    """Every rejection MUST name its load-bearing premise and tag it.

    2026-07-12. LEGEND's epistemic discipline covered only positive assertions. The three errors
    of that day were all `P -> C` with C = a rejection and P never checked, because P was
    "obvious" (e.g. "polyubiquitination -> proteasome", false: K48 -> proteasome, K63 ->
    autophagy/CMA). A false positive is tested and dies; a false negative is silent, permanent
    and self-reinforcing.

    Written as an executable check and not only as a rule in CLAUDE.md, because default D-05
    says: when principle and implementation diverge, the implementation wins, silently.
    """
    blocks = re.split(r'\n(?=###\s+DIS-\d{3})', text)
    for b in blocks:
        m = re.match(r'###\s+(DIS-\d{3})', b.strip())
        if not m:
            continue
        dis_id = m.group(1)
        if not PREMISE_TAG_RE.search(b):
            findings.append(Finding(
                "WARN_BUT_PROCEED",
                "DISMISSAL_WITHOUT_PREMISE",
                f"{dis_id}: rejection without a tagged `PREMISE:` — an unaudited negative "
                f"is a compounding loss (see CLAUDE.md, discipline on negatives)",
            ))
        # A rejection resting on a textbook default, still "active", is provisional by
        # construction: it must declare what would revive it.
        if DEFAULT_PREMISE_RE.search(b) and not REVIVAL_RE.search(b):
            findings.append(Finding(
                "WARN_BUT_PROCEED",
                "DEFAULT_PREMISE_NO_TRIGGER",
                f"{dis_id}: rests on a textbook default without a REVIVAL_TRIGGER — "
                f"a default is not a foundation, it is a research target",
            ))


def _check_commit_candidate_ids(findings, text):
    """Reject duplicate CC identifiers in the append-only operational queue."""
    ids = re.findall(r'^##\s+(CC-\d{4}-\d{2}-\d{2}-\d{3})\b', text, re.M)
    for cc_id in sorted(set(ids)):
        count = ids.count(cc_id)
        if count > 1:
            findings.append(Finding(
                "BLOCK_BATCH_COMMIT",
                "DUPLICATE_COMMIT_CANDIDATE_ID",
                f"{cc_id} duplicated in the session commit log ({count} times)",
            ))

def _load_receipt_engine():
    """Import the receipt engine that lives beside this linter."""
    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    import fulltext_receipts  # noqa: PLC0415 - deliberately lazy, so absence is a finding
    return fulltext_receipts


def _check_fulltext_receipts(findings, repo_root):
    """Make the full-text trace contract *gate*, instead of merely reporting.

    Before this check the receipt ledger was honest but unguarded: deleting a historical
    event, or the whole ledger, left `VERDICT: PASS` untouched, and `BATCH_COMMIT` opened
    on top of a corpus whose reading history had silently changed. Coverage report and
    batch queue did fail closed, but they are *views* — nothing that can say
    `BLOCK_BATCH_COMMIT`, which is the only word this system acts on.

    The severities encode which kind of damage occurred. A ledger that fails to parse is a
    commit-blocking defect. A ledger whose *past* moved is a state you cannot reason from
    at all, so it is `BLOCK_SYSTEM`: recovery before progress.
    """
    manifest_path = os.path.join(repo_root, STATE_MANIFEST)
    manifest_text = _read(manifest_path) if os.path.isfile(manifest_path) else ""
    ledger_path = os.path.join(repo_root, RECEIPT_LEDGER)
    configured = os.path.isfile(ledger_path) or any(
        token in manifest_text
        for token in ("fulltext_ledger_", "registry_only_fulltext_declaration")
    )
    if not configured:
        return
    path_declarations = RECEIPT_LEDGER_PATH.findall(manifest_text)
    if len(path_declarations) != 1 or path_declarations[0] != RECEIPT_LEDGER:
        findings.append(Finding(
            "BLOCK_SYSTEM", "RECEIPT_LEDGER_PATH_INVALID",
            f"State manifest must declare exactly one fulltext_ledger_path equal to "
            f"{RECEIPT_LEDGER}",
        ))
    if not os.path.isfile(ledger_path):
        findings.append(Finding(
            "BLOCK_SYSTEM", "RECEIPT_LEDGER_MISSING",
            f"The authoritative ledger {RECEIPT_LEDGER} is absent: "
            f"the full-text reading history cannot be reconstructed",
        ))
        return

    try:
        engine = _load_receipt_engine()
    except Exception as error:
        findings.append(Finding(
            "BLOCK_SYSTEM", "RECEIPT_ENGINE_MISSING",
            f"Receipt ledger present but its validator cannot be loaded ({error}): "
            f"the append-only guarantee is unverifiable",
        ))
        return

    from pathlib import Path
    try:
        receipts = engine.load_ledger(Path(ledger_path))
    except (OSError, ValueError) as error:
        findings.append(Finding(
            "BLOCK_SYSTEM", "RECEIPT_LEDGER_HISTORY_UNTRUSTED",
            f"Full-text receipt ledger cannot be trusted: {error}",
        ))
        return

    for message in engine.validate_state_anchor(manifest_text, receipts):
        findings.append(Finding(
            "BLOCK_SYSTEM", "RECEIPT_LEDGER_ANCHOR_MISMATCH",
            f"Full-text receipt ledger tail anchor: {message}",
        ))

    _check_fulltext_declaration_ratchet(findings, repo_root, manifest_text, engine)


def _check_session_self_evaluation(findings, repo_root):
    """Route reading-landed/output-identity failures into the blocking authority."""
    script = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "session_self_eval.py"
    )
    if not os.path.isfile(script):
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT", "SESSION_SELF_EVAL_MISSING",
            "session_self_eval.py is unavailable; completed reads cannot be checked for landing",
        ))
        return
    completed = subprocess.run(
        [sys.executable, script, "--workspace", repo_root, "--disease", "wwox"],
        check=False, capture_output=True, text=True,
    )
    if completed.returncode == 0:
        return
    parsed = False
    pattern = re.compile(r"^\s*\[BLOCK_BATCH_COMMIT\]\s+([A-Z_]+):\s*(.+)$")
    for line in completed.stdout.splitlines():
        match = pattern.match(line)
        if match:
            parsed = True
            findings.append(Finding("BLOCK_BATCH_COMMIT", match.group(1), match.group(2)))
    if not parsed:
        detail = (completed.stdout or completed.stderr).strip().splitlines()
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT", "SESSION_SELF_EVAL_FAILED",
            detail[-1] if detail else f"self-evaluation exited {completed.returncode}",
        ))


def _check_fulltext_declaration_ratchet(findings, repo_root, manifest_text, engine):
    """A registry may keep its historical full-text declarations; it may not add new ones.

    The honest position is that 21 records were read before receipts existed and their
    coverage maps did not survive. Deleting them would falsify history; upgrading them to
    `complete_fulltext_read` would manufacture evidence. So they are grandfathered by count,
    and the count is a ratchet: any *new* full-text declaration must carry a persisted
    receipt. This is what makes the contract compound instead of merely existing.
    """
    baseline_matches = RATCHET_BASELINE.findall(manifest_text)
    id_matches = RATCHET_IDS.findall(manifest_text)
    if len(baseline_matches) != 1 or len(id_matches) != 1:
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT", "RECEIPT_RATCHET_UNDECLARED",
            "State manifest must declare exactly one grandfathered full-text count and "
            "exactly one identity list; otherwise new declarations cannot be detected",
        ))
        return
    baseline = int(baseline_matches[0])
    try:
        grandfathered = json.loads(id_matches[0])
    except json.JSONDecodeError as error:
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT", "RECEIPT_RATCHET_INVALID",
            f"Grandfathered full-text identity list is invalid JSON: {error.msg}",
        ))
        return
    if (
        not isinstance(grandfathered, list)
        or not all(isinstance(item, str) and item.strip() for item in grandfathered)
        or len(set(grandfathered)) != len(grandfathered)
        or baseline != len(grandfathered)
    ):
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT", "RECEIPT_RATCHET_INVALID",
            "Grandfathered full-text identities must be unique non-empty strings and "
            "their number must equal registry_only_fulltext_declarations_baseline",
        ))
        return
    grandfathered_ids = set(grandfathered)

    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    try:
        import coverage_report  # noqa: PLC0415 - shares the registry parser, never re-implements it
        from pathlib import Path
        root = Path(repo_root)
        papers_path = Path(os.path.join(repo_root, CURRENTS[2]))
        entries = coverage_report.parse_entries(papers_path.read_text(encoding="utf-8"))
        index = engine.receipt_depth_index(engine.default_ledger_path(root, "wwox"))
        owners = coverage_report.receipt_owners(entries, index)
    except Exception as error:
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT", "RECEIPT_RATCHET_UNCHECKABLE",
            f"Cannot evaluate the full-text declaration ratchet ({error})",
        ))
        return
    unbacked_ids = {
        entry["_id"]
        for entry in entries
        if coverage_report.classify_depth(entry) == "full_text"
        and (
            owners.get(entry["_id"]) is None
            or owners[entry["_id"]]["evidence_depth"] != "complete_fulltext_read"
        )
    }
    new_ids = unbacked_ids - grandfathered_ids
    if new_ids:
        findings.append(Finding(
            "BLOCK_BATCH_COMMIT", "UNBACKED_FULLTEXT_DECLARATION",
            f"New registry records declare full-text review with no persisted complete "
            f"receipt: {', '.join(sorted(new_ids))}. The historical identity allowlist "
            f"cannot be exchanged one-for-one",
        ))
    elif len(unbacked_ids) < baseline:
        findings.append(Finding(
            "INFO", "RECEIPT_RATCHET_IMPROVED",
            f"Unbacked full-text declarations fell to {len(unbacked_ids)} "
            f"(baseline {baseline}): lower the baseline and remove resolved IDs from the "
            f"grandfathered list",
        ))


def claim_paper_findings(claims_text, paper_ids, corpus_ids=None):
    corpus_ids = corpus_ids or set()
    findings = []
    for cid, bodies in split_blocks(claims_text, "CLAIM").items():
        for body in bodies:
            refs = WIKILINK_PAPER.findall(body)
            corpus_refs = WIKILINK_CORPUS.findall(body)
            if not refs and not corpus_refs:
                src = field(body, "Source")
                status = (field(body, "Status") or "").strip().lower()
                if src and status == "background only":
                    # A 'background only' claim (framing/non-operational IPOTESI) does not
                    # require anchoring to a PAPER, just as background_only papers are exempt
                    # from the claim-link (wikilink_schema §2.1). INFO only.
                    findings.append(Finding("INFO", "MISSING_WIKILINK",
                                            f"CLAIM {cid}: background only, PAPER wikilink not required"))
                elif src:
                    # Support declared in prose (e.g. a corpus-paper not yet promoted to a PAPER
                    # entry): a pending wikilink retrofit, not an orphan.
                    findings.append(Finding("WARN_BUT_PROCEED", "MISSING_WIKILINK",
                                            f"CLAIM {cid}: prose support, PAPER wikilink missing"))
                else:
                    findings.append(Finding("BLOCK_BATCH_COMMIT", "CLAIM_NO_PAPER",
                                            f"CLAIM {cid}: no supporting paper"))
            for ref in refs:
                if ref not in paper_ids:
                    findings.append(Finding("BLOCK_BATCH_COMMIT", "DANGLING_WIKILINK",
                                            f"CLAIM {cid}: PAPER {ref} does not exist"))
            for ref in corpus_refs:
                if ref not in corpus_ids:
                    findings.append(Finding("BLOCK_BATCH_COMMIT", "DANGLING_WIKILINK",
                                            f"CLAIM {cid}: CORPUS P{ref} does not exist"))
    return findings

def lint(repo_root):
    findings = []
    for rel in CURRENTS:
        if not os.path.isfile(os.path.join(repo_root, rel)):
            findings.append(Finding("BLOCK_SYSTEM", "MISSING_CURRENT",
                                    f"Missing current file: {rel}"))
    if not findings:
        working_model = _read(os.path.join(repo_root, CURRENTS[0]))
        claims = _read(os.path.join(repo_root, CURRENTS[1]))
        papers = _read(os.path.join(repo_root, CURRENTS[2]))
        _check_ids_states(findings, claims, "CLAIM", VALID_CLAIM_STATES)
        _check_ids_states(findings, papers, "PAPER", VALID_PAPER_STATES)
        findings.extend(working_model_claim_mirror_findings(working_model, claims))
        paper_ids = set(parse_ids(papers, "PAPER"))
        corpus_ids = set(parse_corpus_ids(papers))
        findings.extend(claim_paper_findings(claims, paper_ids, corpus_ids))
        discovery_path = os.path.join(repo_root, DISCOVERY_LEDGER)
        if os.path.isfile(discovery_path):
            _check_discovery_ids(findings, _read(discovery_path))
        session_log_path = os.path.join(repo_root, SESSION_COMMIT_LOG)
        if os.path.isfile(session_log_path):
            _check_commit_candidate_ids(findings, _read(session_log_path))
        dismissal_path = os.path.join(repo_root, DISMISSAL_LEDGER)
        if os.path.isfile(dismissal_path):
            _check_dismissals(findings, _read(dismissal_path))
        _check_fulltext_receipts(findings, repo_root)
        if not any(item.severity == "BLOCK_SYSTEM" for item in findings):
            _check_session_self_evaluation(findings, repo_root)
    return LintResult(findings)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    args = parser.parse_args(argv)
    res = lint(args.root)
    print(f"VERDICT: {res.verdict}")
    for f in res.findings:
        print(f"  [{f.severity}] {f.code}: {f.message}")
    if res.blocks_deepdive:
        print("GATE: BLOCK_SYSTEM — even DEEP_DIVEs are blocked (recovery).")
    elif res.blocks_commit:
        print("GATE: only BATCH_COMMIT blocked — DEEP_DIVEs may proceed.")
    # exit: 3 = BLOCK_SYSTEM, 2 = BLOCK_BATCH_COMMIT, 0 = PASS/WARN
    return 3 if res.blocks_deepdive else 2 if res.blocks_commit else 0


if __name__ == "__main__":
    raise SystemExit(main())
