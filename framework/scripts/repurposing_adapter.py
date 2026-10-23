#!/usr/bin/env python3
"""The one CLI over the repurposing adapters in `framework/adapters/`.

    repurposing_adapter.py list                      every adapter the directory holds, with its INFO
    repurposing_adapter.py add <name>                write <name>.py from the template (then edit it)
    repurposing_adapter.py remove <name>             delete <name>.py — nothing else to edit
    repurposing_adapter.py selftest [name] [--live]  offline self-tests (canned responses); --live calls the service
    repurposing_adapter.py query <name> '<json>'     run one adapter on one request, print its dict
    repurposing_adapter.py acknowledgements [--write] render ACKNOWLEDGEMENTS.md from the adapters' own
                                                     licence and citation fields (--write saves it; add/remove do this too)

An adapter is discovered by being a `.py` file in the directory whose name does not start with
`_`. There is no registration, no base class, no schema and no version field: the convention is
`framework/protocols/repurposing_adapter_convention.md` (one page). Every output carries
`retrieved_at`, `status` in MATCH_FOUND / NO_MATCH_FOUND / QUERY_ERROR (the bridge's words),
`evidence_label: NOT WWOX EVIDENCE`, and no score.
"""
from __future__ import annotations

import argparse
import importlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DIR = ROOT / "framework" / "adapters"
# Named by the operator (instruction of 2026-10-23): the module's list of every source it draws
# on, derived from the adapters so that deleting one leaves the list correct after a re-render.
DEFAULT_ACK = ROOT / "disease-models" / "wwox" / "research" / "drug_repurposing" / "ACKNOWLEDGEMENTS.md"
STATES = ("MATCH_FOUND", "NO_MATCH_FOUND", "QUERY_ERROR")
FORBIDDEN_KEYS = ("score", "rank", "probability", "belief")
INFO_KEYS = ("name", "gives", "network", "licence", "inputs", "outputs",
             "licence_url", "licence_read_on", "licence_terms", "citation", "attribution")
OUTPUT_KEYS = ("adapter", "retrieved_at", "request", "requests_sent", "status", "hits",
               "source_version", "evidence_label", "licence", "citation", "note", "error")

TEMPLATE = '''"""<Service> — <what it gives in one line>. <protocol>, key-less, <licence>. Measured <date>.

Request: {{"<field>": "<example>"}}
Output hits: one per <thing>. No score is returned.
"""
from __future__ import annotations

from . import _http

INFO = {{
    "name": "{name}",
    "gives": "<what LEGEND gets that it lacks>",
    "network": "GET https://<host>/<path>",
    "licence": "<licence>; key-less, no payment",
    "inputs": "<field> (required)",
    "outputs": "hits: <shape>; source_version = <where the version comes from>",
    "licence_url": "https://<host>/<terms page you actually read>",
    "licence_read_on": "<YYYY-MM-DD>",
    "licence_terms": "<what the licence/terms page says, quoted: attribution, share-alike, rate limits, user-agent>",
    "citation": "<the citation the source asks for, with DOI>",
    "attribution": "<the credit line to print beside any data from this source>",
}}

URL = "https://<host>/<path>"


def query(request: dict, fetch=_http.get_json) -> dict:
    out = {{"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
           "requests_sent": [URL], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
           "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
           "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence", "error": ""}}
    if not request:
        out["error"] = "a request is required"
        return out
    status, payload = fetch(URL, params=dict(request))
    if status != 200:
        out["error"] = f"HTTP {{status}}: {{str(payload)[:300]}}"
        return out
    # fill out["hits"] from payload, verbatim fields, no score
    out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
    return out


SAMPLE = {{"request": {{"<field>": "<example>"}}, "response": (200, {{}})}}


def selftest(fetch=None) -> dict:
    result = query(SAMPLE["request"], fetch=(lambda u, params=None, body=None, timeout=20: SAMPLE["response"]) if fetch is None else fetch)
    return {{"ok": result["status"] in ("MATCH_FOUND", "NO_MATCH_FOUND"), "status": result["status"],
            "hits": len(result["hits"]), "source_version": result["source_version"], "error": result["error"]}}
'''


def discover(directory: Path = DEFAULT_DIR) -> list[str]:
    return sorted(p.stem for p in directory.glob("*.py") if not p.name.startswith("_"))


def load(name: str, directory: Path = DEFAULT_DIR):
    """Import one adapter as a package member so its `from . import _http` resolves whatever
    the directory is (a copy in a temporary directory included)."""
    package = f"legend_adapters_{abs(hash(str(directory.resolve()))) % 10**8}"
    if package not in sys.modules:
        spec = importlib.util.spec_from_file_location(package, directory / "__init__.py",
                                                      submodule_search_locations=[str(directory)])
        if spec is None:
            raise ImportError(f"{directory} is not an adapter directory (no __init__.py)")
        module = importlib.util.module_from_spec(spec)
        sys.modules[package] = module
        spec.loader.exec_module(module)
    return importlib.import_module(f"{package}.{name}")


def check_output(result: dict) -> list[str]:
    """What every adapter output must carry — reported, so a selftest can fail on it."""
    problems = []
    for key in OUTPUT_KEYS:
        if key not in result:
            problems.append(f"missing key {key}")
    for key in ("licence", "citation"):
        if not str(result.get(key, "")).strip():
            problems.append(f"{key} must name the source's licence/citation (operator instruction 2026-10-23)")
    if result.get("status") not in STATES:
        problems.append(f"status {result.get('status')!r} not in {STATES}")
    if result.get("evidence_label") != "NOT WWOX EVIDENCE":
        problems.append("evidence_label must be NOT WWOX EVIDENCE")
    if "never absence" not in str(result.get("note", "")):
        problems.append("note must say NO_MATCH_FOUND is never absence")
    text = json.dumps(result.get("hits", []), ensure_ascii=False).lower()
    for word in FORBIDDEN_KEYS:
        if f'"{word}"' in text or f'"{word}s"' in text:
            problems.append(f"hits carry a {word} key: the module emits no score")
    return problems


def run_selftest(name: str, directory: Path = DEFAULT_DIR, live: bool = False) -> dict:
    module = load(name, directory)
    fetch = module._http.get_json if live else None
    try:
        report = module.selftest(fetch=fetch)
    except Exception as exc:  # a broken adapter is a red line, not a crash of the CLI
        return {"adapter": name, "ok": False, "error": f"{type(exc).__name__}: {exc}", "live": live}
    sample_fetch = fetch if live else (lambda *a, **k: _sample_response(module))
    problems = check_info(module)
    try:
        problems += check_output(module.query(module.SAMPLE["request"], fetch=sample_fetch))
    except Exception as exc:
        problems.append(f"query raised {type(exc).__name__}: {exc}")
    report = {"adapter": name, "live": live, **report}
    if problems:
        report["ok"] = False
        report["contract_problems"] = problems
    return report


def check_info(module) -> list[str]:
    """Every adapter declares its licence as read from the source, with URL and date."""
    info = getattr(module, "INFO", None)
    if not isinstance(info, dict):
        return ["INFO is not a dict"]
    problems = [f"INFO lacks {key}" for key in INFO_KEYS if not str(info.get(key, "")).strip()]
    if "key-less" not in str(info.get("licence", "")):
        problems.append("INFO.licence must say key-less: an adapter that needs a key is not used")
    if "<" in str(info.get("licence_terms", "")) or "<" in str(info.get("citation", "")):
        problems.append("INFO still carries template placeholders")
    return problems


def render_acknowledgements(directory: Path = DEFAULT_DIR) -> str:
    """The module's list of every source it draws on — derived from the adapters, never typed."""
    lines = [
        "# Acknowledgements — the external sources the Drug Repurposing module draws on",
        "",
        "Rendered by `python3 framework/scripts/repurposing_adapter.py acknowledgements --write` from the",
        "`INFO` block of every adapter in `framework/adapters/`; never edited by hand. Adding or removing an",
        "adapter re-renders it (the `add` and `remove` commands do so), and `test_repurposing_adapter.py`",
        "fails when the committed file no longer matches the adapters. Every licence and citation below was",
        "read from the source's own licence or terms page on the date given, not from memory.",
        "",
        "We are sincerely grateful to the maintainers, curators and funders of these resources. Each of them",
        "makes carefully curated public data available without a key or a fee, and asks in return only for",
        "attribution and a citation; this module honours both, copies their fields verbatim, computes no score",
        "from them, and labels everything it receives **NOT WWOX EVIDENCE** so that their work is never",
        "misrepresented as something it is not. Thank you.",
        "",
        "Nothing here is medical advice. Not one of these sources certifies efficacy, safety or suitability.",
        "",
    ]
    for name in discover(directory):
        info = getattr(load(name, directory), "INFO", {})
        lines += [
            f"## {name}",
            "",
            f"- **What we use:** {info.get('gives', '')}",
            f"- **Access:** {info.get('network', '')}",
            f"- **Licence:** {info.get('licence', '')}",
            f"- **Licence source:** {info.get('licence_url', '')} — read on {info.get('licence_read_on', '')}",
            f"- **Terms as read:** {info.get('licence_terms', '')}",
            f"- **Citation requested:** {info.get('citation', '')}",
            f"- **Attribution line printed with the data:** {info.get('attribution', '')}",
            "",
        ]
    return "\n".join(lines)


def _sample_response(module):
    sample = module.SAMPLE
    if "response" in sample:
        return sample["response"]
    responses = sample.get("responses") or {}
    return next(iter(responses.values()), (200, {}))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR, help="adapter directory (default framework/adapters)")
    parser.add_argument("--acknowledgements", type=Path, default=None,
                        help="where add/remove/acknowledgements --write render the list (default: the module's "
                             "ACKNOWLEDGEMENTS.md when --dir is the default directory; otherwise <dir>/ACKNOWLEDGEMENTS.md)")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    p_ack = sub.add_parser("acknowledgements"); p_ack.add_argument("--write", action="store_true")
    p_add = sub.add_parser("add"); p_add.add_argument("name")
    p_rm = sub.add_parser("remove"); p_rm.add_argument("name")
    p_st = sub.add_parser("selftest"); p_st.add_argument("name", nargs="?"); p_st.add_argument("--live", action="store_true")
    p_q = sub.add_parser("query"); p_q.add_argument("name"); p_q.add_argument("request", help="JSON object")
    args = parser.parse_args(argv)
    directory = args.dir
    ack_path = args.acknowledgements or (DEFAULT_ACK if directory.resolve() == DEFAULT_DIR.resolve()
                                         else directory / "ACKNOWLEDGEMENTS.md")

    def rerender() -> None:
        ack_path.write_text(render_acknowledgements(directory), encoding="utf-8")
        print(f"acknowledgements re-rendered: {ack_path}")

    if args.command == "acknowledgements":
        text = render_acknowledgements(directory)
        if args.write:
            ack_path.write_text(text, encoding="utf-8")
            print(f"written {ack_path}")
        else:
            print(text)
        return 0
    if args.command == "list":
        for name in discover(directory):
            info = getattr(load(name, directory), "INFO", {})
            print(f"{name}\t{info.get('gives', '')}\n\tnetwork: {info.get('network', '')}\n\tlicence: {info.get('licence', '')}")
        return 0
    if args.command == "add":
        if not args.name.isidentifier() or args.name.startswith("_"):
            print("name must be a Python identifier not starting with _", file=sys.stderr); return 2
        path = directory / f"{args.name}.py"
        if path.exists():
            print(f"{path} exists", file=sys.stderr); return 2
        path.write_text(TEMPLATE.format(name=args.name), encoding="utf-8")
        print(f"written {path} — fill INFO (licence as read from the source, with URL and date), URL, "
              f"query() hits and SAMPLE, then `selftest {args.name}` and `acknowledgements --write`")
        rerender()
        return 0
    if args.command == "remove":
        path = directory / f"{args.name}.py"
        if not path.exists():
            print(f"{path} does not exist", file=sys.stderr); return 2
        path.unlink()
        print(f"removed {path} — nothing else to edit by hand")
        rerender()
        return 0
    if args.command == "selftest":
        names = [args.name] if args.name else discover(directory)
        red = 0
        for name in names:
            report = run_selftest(name, directory, live=args.live)
            red += 0 if report.get("ok") else 1
            print(json.dumps(report, ensure_ascii=False))
        print(f"selftest: {len(names)} adapter(s), {red} red, live={args.live}")
        return 1 if red else 0
    if args.command == "query":
        module = load(args.name, directory)
        result = module.query(json.loads(args.request))
        problems = check_output(result)
        if problems:
            result["contract_problems"] = problems
        print(json.dumps(result, indent=1, ensure_ascii=False))
        return 0 if not problems else 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
