#!/usr/bin/env python3
"""Builds the static shareable package of the repurposing view (IT5 P13) into view/shareable_package/.

  python3 -B framework/scripts/repurposing_view.py package [--zip PATH]     # (re)generate the folder, optionally a deterministic zip
  python3 -B framework/scripts/repurposing_view.py package --check          # exit 1 if the folder differs from a fresh build

The folder is a LOCAL PREVIEW for review. Nothing here publishes anything: putting it on any external surface
is a decision of the operator. Contents (all deterministic, no clock is read):

  index.html            the shareable view (same bytes as view/index_shareable.html)
  NOTICE.md             the sources actually embedded, their terms and credit lines, and how each condition is met
  COMPARISON.md         what the full research version holds that this one withholds, with counts, and what is identical
  README.md             how to open it, how to hand it over, limits of the perimeter
  manifest.json         machine-readable: embedded sources with row/field counts, withheld counts by class, file digests, audit summary
  LICENSES/             the licence texts the package relies on (pinned by sha256 in view/shareable_sources.json)
  class_b/chembl_cc-by-sa-3.0/   the ChEMBL records of the cards' twelve compounds, as a separate CC BY-SA 3.0 file with its own licence text and credit

The class-B file is never merged into index.html (the page embeds no ChEMBL content), so the share-alike condition attaches to that
one file only (CC BY-SA 3.0 section 4(a): a Collection is not required to be placed under the licence).
Not legal advice: the policy is the licence reading in catalog/README.md, as corrected by its independent verification.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
import zipfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_view as rv  # noqa: E402
import repurposing_shareable_audit as au  # noqa: E402

SCHEMA = "legend.wwox.repurposing_view.shareable_package/1"
PKG = "view/shareable_package"
CHEMBL_DIR = "class_b/chembl_cc-by-sa-3.0"
CHEMBL_FILE = CHEMBL_DIR + "/chembl_cc-by-sa-3.0.jsonl"
GENERATED = ("index.html", "NOTICE.md", "COMPARISON.md", "README.md", "manifest.json", CHEMBL_FILE, CHEMBL_DIR + "/LICENSE_CC-BY-SA-3.0.txt", CHEMBL_DIR + "/CREDIT.txt")
COMMAND = "python3 -B framework/scripts/repurposing_view.py package"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------------------- the class-B ChEMBL file
def chembl_records(dr: Path, allow: dict) -> list[dict]:
    spec = allow["class_b_files"]["chembl"]
    ids = sorted({x["chembl_id"] for v in rv.jload(dr / "catalog/card_links.json")["cards"].values() for x in v.get("links", []) if x.get("chembl_id")})
    out = []
    with gzip.open(dr / "catalog/catalog.jsonl.gz", "rt", encoding="utf-8") as fh:
        for line in fh:
            e = json.loads(line)
            if (e.get("ids") or {}).get("chembl") not in ids:
                continue
            if not any(s.get("source") == "chembl" for s in e.get("source_records") or []):
                continue
            st = next((s for s in e.get("status_records") or [] if s.get("source") == "ChEMBL"), {})
            mech = []
            for t in e.get("targets") or []:
                if t.get("source") == "ChEMBL curated mechanism":
                    mech.append({"mechanism_of_action": t.get("mechanism_of_action"), "action_type": t.get("action_type"), "target_name": t.get("target_name"),
                                 "target_type": t.get("target_type"), "organism": t.get("organism"), "gene_symbols": sorted(t.get("gene_symbols") or [])})
            mech.sort(key=lambda m: json.dumps(m, sort_keys=True))
            out.append({"chembl_id": e["ids"]["chembl"], "pref_name": e.get("name") if e.get("name_source") == "ChEMBL pref_name" else None, "molecule_type": e.get("molecule_type"),
                        "max_phase": st.get("max_phase"), "withdrawn_flag": st.get("withdrawn_flag"), "first_approval_year": st.get("first_approval_year"),
                        "black_box_warning_in_source": st.get("black_box_warning_in_source"), "curated_mechanisms": mech,
                        "chembl_release": spec["release"], "licence": spec["licence"]})
    out.sort(key=lambda r: r["chembl_id"])
    missing = sorted(set(ids) - {r["chembl_id"] for r in out})
    if missing:
        raise SystemExit("card-linked ChEMBL ids without a ChEMBL record in the catalogue: " + ", ".join(missing))
    return out


def chembl_credit(allow: dict, n: int) -> str:
    c = allow["class_b_files"]["chembl"]
    return (
        "Credit line (CC BY-SA 3.0 section 4(c); ChEMBL's own attribution instruction: the URL of the resource and the release version)\n\n"
        f"  ChEMBL data is from https://www.ebi.ac.uk/chembl/ - the version of ChEMBL is {c['release']}.\n"
        "  Original work: ChEMBL, EMBL-EBI (licensor). Title of the work: ChEMBL database.\n"
        "  Licence: Creative Commons Attribution-ShareAlike 3.0 Unported, https://creativecommons.org/licenses/by-sa/3.0/ ; the legal code is in LICENSE_CC-BY-SA-3.0.txt next to this file.\n\n"
        "Adaptation notice (section 3(b) and 4(c)(iv))\n\n"
        f"  chembl_cc-by-sa-3.0.jsonl is an adaptation of ChEMBL: a selection of {n} molecule records (the compounds the cards of the LEGEND WWOX repurposing module name,\n"
        "  by ChEMBL identifier) and of the fields chembl_id, pref_name, molecule_type, max_phase, withdrawn_flag, first_approval_year, black_box_warning_in_source and the\n"
        "  curated mechanisms (mechanism_of_action, action_type, target_name, target_type, organism, gene_symbols), re-serialised as JSON Lines.\n"
        "  No ChEMBL value was altered. The adaptation is distributed under the same licence (CC BY-SA 3.0). No endorsement by ChEMBL or EMBL-EBI is implied.\n\n"
        "Scope\n\n"
        "  This licence applies to this file and to adaptations of it. It does not apply to ../../index.html, which embeds no ChEMBL content (only ChEMBL identifiers), nor to the other\n"
        "  files of the package, which are a Collection with this file (CC BY-SA 3.0 section 4(a): the Collection apart from the Work is not required to be placed under the licence).\n"
        "  Do not merge this file into another dataset unless the result is distributed under CC BY-SA 3.0 or a licence that clause allows.\n"
    )


# ---------------------------------------------------------------------------- census of what is withheld
def catalogue_census(dr: Path, allow: dict) -> dict:
    pol = allow["claim_source_policy"]
    rows, recs, origins, names = Counter(), 0, Counter(), Counter()
    cat_ids = Counter()
    with gzip.open(dr / "catalog/catalog.jsonl.gz", "rt", encoding="utf-8") as fh:
        for line in fh:
            e = json.loads(line)
            recs += 1
            origins[e["origin"]] += 1
            names[e.get("name_source")] += 1
            for t in e.get("targets") or []:
                rows[t.get("claim_source") or t.get("source")] += 1
            ids = e.get("ids") or {}
            for k in ("drugbank", "chebi", "unii", "matrix_id"):
                v = ids.get(k)
                cat_ids[k] += len(v) if isinstance(v, list) else (1 if v else 0)
            cat_ids["atc"] += len(e.get("atc") or [])
            cat_ids["inchikey"] += 1 if ids.get("inchikey") else 0
    by_class = Counter()
    per_source = {}
    for s, n in sorted(rows.items()):
        c = (pol.get(s) or {}).get("class", "UNCLASSIFIED")
        by_class[c] += n
        per_source[s] = {"class": c, "catalogue_rows": n, "terms": (pol.get(s) or {}).get("terms")}
    return {"records": recs, "records_by_origin": dict(sorted(origins.items())), "records_by_name_source": dict(sorted((k or "none", v) for k, v in names.items())),
            "target_rows_by_class": dict(sorted(by_class.items())), "target_rows_by_claim_source": per_source,
            "third_party_identifier_values_in_catalogue_not_embedded": dict(sorted(cat_ids.items()))}


def compare_payloads(F: dict, S: dict) -> dict:
    """Section-by-section comparison of the full and the shareable payload (both built from the same inputs)."""
    def same(a, b):
        return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
    sections = {}
    for k in sorted(set(F) | set(S)):
        if k in ("source",):
            continue
        sections[k] = "identical" if same(F.get(k), S.get(k)) else "differs"
    cur = {}
    for k in sorted(set(F["cur"]) | set(S["cur"])):
        cur[k] = "identical" if same(F["cur"].get(k), S["cur"].get(k)) else "differs"
    cand_fields = Counter()
    fc = {c["id"]: c for c in F["cur"]["cands"]}
    for c in S["cur"]["cands"]:
        for k, v in c.items():
            if not same(v, fc[c["id"]].get(k)):
                cand_fields[k] += 1
    named_f = sum(1 for r in F["rows"] if r["name"] and not str(r["name"]).startswith(("CHEMBL", "DGIDB")))
    named_s = sum(1 for r in S["rows"] if not r.get("w"))
    return {
        "payload_sections": sections, "curated_sections": cur, "card_fields_that_differ_count_of_cards": dict(sorted(cand_fields.items())),
        "rows_total": len(F["rows"]), "rows_named_full": named_f, "rows_named_shareable_card_names_only": named_s,
        "rows_with_per_row_status_or_modality_full": sum(1 for r in F["rows"] if r["st"] or r["mod"]), "rows_with_per_row_status_or_modality_shareable": sum(1 for r in S["rows"] if r["st"] or r["mod"]),
        "rows_with_access_categories_full": sum(1 for r in F["rows"] if r["acc"]), "rows_with_access_categories_shareable": sum(1 for r in S["rows"] if r["acc"]),
        "pairs_total": len(F["pairs"]), "pairs_with_target_list_full": sum(1 for p in F["pairs"] if p.get("l1") and p["l1"][2]), "pairs_with_target_list_shareable": sum(1 for p in S["pairs"] if p.get("l1") and p["l1"][2]),
        "target_symbols_listed_full": sum(len(p["l1"][2]) for p in F["pairs"] if p.get("l1")), "target_symbols_listed_shareable": sum(len(p["l1"][2]) for p in S["pairs"] if p.get("l1")),
        "card_actions_listed_full": sum(len(c["actions"]) for c in F["cur"]["cands"]), "card_actions_listed_shareable": sum(len(c["actions"]) for c in S["cur"]["cands"]),
        "excluded_rows_with_names_full": sum(1 for e in F["excluded_detail"] if e["genes"]), "excluded_rows_with_names_shareable": sum(1 for e in S["excluded_detail"] if e["genes"]),
        "cards": len(S["cur"]["cands"]), "needs": len(S["cur"]["needs"]),
    }


# ---------------------------------------------------------------------------- text of the documents
def notice_md(allow: dict, S: dict, man: dict) -> str:
    foot = S["cur"]["footer"]
    L = ["# NOTICE: sources, terms and credit lines", "",
         "Package of the LEGEND WWOX repurposing view, shareable edition. LOCAL PREVIEW for review: nothing in it has been published, and publication on any external surface is a decision of the operator.",
         "Research material about a disease-level genotype class, not medical advice, not a ranking of treatments. Not legal advice: the terms below are the licence reading recorded in the repository (`catalog/README.md`, section Licence reconciliation, IT5 P1) as corrected by its independent verification of 2026-10-29.", "",
         "## 1. Own text and computations", "",
         "Cards, needs, priorities, positions (F/C/P), dispositions, counts and the Italian orientation texts were written or computed in this repository. Licence: the repository `LICENSE` (MIT), copied as `LICENSES/LEGEND-MIT.txt`. Credit: LEGEND WWOX repurposing module (this repository). The licence of the repository covers original text only; it does not cover third-party rows.", ""]
    L += ["## 2. Third-party content embedded in `index.html` (class A: attribution)", ""]
    emb = [e for e in foot["embedded"] if e.get("rows")]
    for e in emb:
        L += [f"- **{e['label']}** ({e['rows']} rows or attributes embedded). Terms: {e['licence']}. Credit: {e['attribution']} {e.get('url') or ''}".rstrip()]
    L += ["",
          "How the conditions are met:", "",
          "- CIViC (CC0 1.0): no condition; credit is given as a courtesy. Legal code: `LICENSES/CC0-1.0.txt`.",
          "- DoCM (CC BY 4.0): attribution (above), a link to the licence (https://creativecommons.org/licenses/by/4.0/ ; legal code `LICENSES/CC-BY-4.0.txt`), an indication of changes (rows are reduced to gene symbol and the action recorded, regrouped by this repository), no endorsement implied. The live DoCM site is gone: the terms were read in the project's archived about page.",
          "- openFDA NDC (CC0 1.0 dedication; credit requested, not required): the per-compound access categories `prescription` and `OTC`, stated from the NDC directory. Credit: Data provided by the U.S. Food and Drug Administration. Do not rely on openFDA to make decisions regarding medical care. No FDA endorsement is implied.",
          "- FDA pharmacogenomic biomarkers (public domain unless otherwise noted on fda.gov): allowlisted; zero rows are embedded in this build.",
          "- The Every Cure MATRIX drug list (CC BY 4.0 for the fields its authors own: names, approval flags) is allowlisted for names; no MATRIX name is embedded in this build, and none of the ATC, DrugBank or ChEBI identifiers it carries (third-party content that a dataset-card licence cannot grant).", ""]
    L += ["## 3. Identifiers and bibliographic facts (no third-party content beyond the identifier)", ""]
    for e in foot["identifiers"]:
        L += [f"- **{e['label']}**: {e['licence']}. {e['attribution']} {e.get('url') or ''}".rstrip()]
    L += ["", f"Identifier census of `index.html` (distinct values): {json.dumps(man['audit']['identifiers'], sort_keys=True)}. No abstract and no passage of an article is embedded. Short quotations are marked by quotation marks and attributed (section 6).", "",
          "## 4. Class B (share-alike): shipped as a separate file, never merged into the page", ""]
    for e in foot["class_b"]:
        L += [f"- **{e['label']}**: `{e['path']}` ({e['licence']}). {e['credit']}. Records: {e['records_of']}. Licence text and credit line travel with it in the same folder (`LICENSE_CC-BY-SA-3.0.txt`, `CREDIT.txt`)."]
    L += ["",
          "Decision for the three share-alike sources, with reasons:", "",
          "- **ChEMBL (CC BY-SA 3.0): shipped as a separate file.** The condition is attribution naming the ChEMBL URL and the release version, and distribution of any adaptation under the same licence. It can be met exactly: the file is a selection of twelve records and of listed fields (an adaptation, stated as such), carries the legal code and the credit line, and is not merged with anything else; the single page embeds only ChEMBL identifiers, so the share-alike condition attaches to that file only (CC BY-SA 3.0 section 4(a), Collection).",
          "- **GtoPdb (ODbL database, CC BY-SA 4.0 contents): counts only.** Two licences apply to the same rows, ODbL carries its own rules for a publicly used Derivative Database, and the catalogue merges GtoPdb ligand data into its records. A correct separate file would need a split the catalogue does not hold; it is not widened.",
          "- **ClinPGx / PharmGKB (CC BY-SA 4.0 declared by DGIdb): counts only.** The data-usage policy page was script-rendered and its text was never read; an unread condition is not honoured by guessing.", "",
          "## 5. Counted but not embedded", ""]
    for e in foot["counts_only"]:
        L += [f"- **{e['label']}**: {e['terms']}" + (f" (version {e['version']})" if e.get("version") else "")]
    L += ["", f"Withheld catalogue target rows by class: {json.dumps(man['withheld']['target_rows_by_class'], sort_keys=True)} (class A rows are embedded only where they touch a need; see `manifest.json`).", "",
          "## 6. Provenance of the cards' own text", "",
          "Every output string was compared with the full texts, abstracts and openFDA label sections held locally; the result is recorded in `TEXT_PROVENANCE.json`. Bibliographic titles are facts and are listed apart. Quotations are limited to a few marked passages, each short (the longest is one sentence of an article, introduced by `the authors write`); no label section and no abstract is reproduced. The comparison covers only texts held locally when it was run (stated in that file).", "",
          f"Short third-party labels that card text also contains (checked against ChEMBL's curated-mechanism and target wording; none longer than {au.WORDING_MAX_WORDS} words, otherwise the audit fails): "
          + "; ".join(f"`{w}`" for w, r in man["audit"]["reference"]["co_attested_wording"]) + ". One is a quotation with attribution in card H01 (`ChEMBL_37 curated mechanism: 'Voltage-gated T-type calcium channel blocker'`, a controlled-vocabulary label of five words); the others are generic scientific terms that the cards use in their own sentences. They are listed, not hidden.", "",
          "## 7. What this notice does not do", "",
          "It does not clear anything for publication: the operator decides whether and where to publish. It is not legal advice.", ""]
    return "\n".join(L)


def readme_md(man: dict) -> str:
    return "\n".join([
        "# WWOX repurposing view: shareable package (local preview)", "",
        "Research material at disease and reference-genotype level: what to study for WWOX-related epileptic encephalopathy, and on what evidence. Not medical advice, not a ranking of treatments, not a probability of benefit. The page is in Italian for the physician; scientific citations keep their original form.", "",
        "**Perimeter: this folder is a local preview. It has not been published anywhere, and publication on any external surface (a website, a repository change, an e-mail attachment to third parties) requires the operator's decision.**", "",
        "## Open it", "",
        "Open `index.html` by double-click or from `file://`. It is one self-contained file (inline CSS and JavaScript, data embedded as JSON); it needs no server, loads nothing from the network and opens identically from any folder or from the unzipped archive. Links inside it go to the same page (`#...` anchors) or to public identifiers (PubMed, DOI, ChEMBL, source licence pages); none is a repository-relative path.", "",
        "Card export (print / PDF, standalone HTML download) and the comparison view work offline: use the buttons on a card profile, or the URL fragments `#export=<card id>` and `#compare=<id>,<id>`.", "",
        "## Hand it over", "",
        "Build a zip with the documented command (deterministic: fixed timestamps, sorted entries):", "",
        "```bash", f"{COMMAND} --zip /path/to/wwox_repurposing_shareable_package.zip", "```", "",
        "The zip holds exactly the folder: `index.html`, `NOTICE.md` (sources, terms, credit lines), `COMPARISON.md` (what the full version holds and this one withholds), `manifest.json` (machine-readable inventory with digests), `LICENSES/` and `class_b/chembl_cc-by-sa-3.0/`. Hand over the whole zip, not `index.html` alone: the NOTICE and the credit lines must travel with the page, and the ChEMBL file must travel with its own licence text.", "",
        "## Regenerate and verify", "",
        "```bash",
        "python3 -B framework/scripts/repurposing_coverage.py run",
        "python3 -B framework/scripts/repurposing_view.py run --source shareable",
        f"{COMMAND}",
        f"{COMMAND} --check",
        "python3 -B framework/scripts/repurposing_view.py audit-shareable --dynamic",
        "```", "",
        "`audit-shareable` is the proof that the allowlist did what it says: it builds a reference of forbidden values from the full catalogue and fails if any string, row or identifier traceable to a non-allowlisted source is in the bytes, the rendered pages, the exports, the standalone downloads or the PDF text. It has a mutation test (`framework/scripts/test_repurposing_view.py`, class `ShareableAudit`).", "",
        "## What is in and what is not", "",
        "See `COMPARISON.md`. In short: every card, need, position (F/C/P), priority group, funnel count and chart is the same as in the full version; compound names that only third-party databases carry, per-row status and modality, and rows from non-allowlisted claim sources are replaced by catalogue identifiers and counts.", "",
        "## Limits, stated plainly", "",
        "- Pair-level link existence and association counts are kept for withheld compounds (an identifier with counts); the content of the link (target, action, source) is not. Whether that is acceptable for external circulation is for the operator.",
        "- Bibliographic titles come from NCBI esummary records collected into a tracked cache; they are facts about published works, listed in `NOTICE.md`.",
        "- The provenance-of-text check covers the third-party texts held locally (full texts, abstracts, five openFDA label JSON files fetched for the check); a source not held locally was not compared.",
        "- Names shorter than four characters cannot be traced by string and are covered only by the structural checks (rows carry card names or identifiers).",
        "- The audit proves conformity with the policy file; the policy file is a licence reading that is not legal advice and has components marked uncertain in `NOTICE.md` (not widened).", "",
        f"Data date: {man['data']['data_date']}; catalogue built {man['data']['catalogue_generated']}; DGIdb export {man['data']['dgidb_export']}.", ""])


def comparison_md(man: dict) -> str:
    c, cen = man["comparison"], man["withheld"]
    pct = lambda a, b: f"{100 * a / b:.1f}%" if b else "n/a"
    L = ["# Comparison with the full research version", "",
         "The full version (`view/index.html` in the repository, local use) and this package are built from the same inputs by the same builder; only the data boundary differs. Counts below are computed, not typed.", "",
         "## Same in both", "",
         f"- {c['cards']} candidate cards with their six answers, evidence by scope, counter-evidence, next step, public identifiers and F/C/P positions: card text and positions are identical (the only card fields that differ are listed under 'Different').",
         f"- {c['needs']} needs and their observations, the threads, groups, goals, funnel, access chart (catalogue-wide counts), matrix summary, dispositions, observations, lead dispositions and the Italian orientation texts.",
         f"- Sections of the data object that are byte-identical: {', '.join(k for k, v in c['payload_sections'].items() if v == 'identical')}.",
         f"- Curated sections identical: {', '.join(k for k, v in c['curated_sections'].items() if v == 'identical')}.", "",
         "## Different (withheld here, present in the full version)", "",
         "| What | Full | Shareable |", "|---|---|---|",
         f"| Catalogue rows shown with a name | {c['rows_named_full']} | {c['rows_named_shareable_card_names_only']} (card names only; the other {c['rows_total'] - c['rows_named_shareable_card_names_only']} rows carry an identifier) |",
         f"| Rows with per-row status class or modality | {c['rows_with_per_row_status_or_modality_full']} | {c['rows_with_per_row_status_or_modality_shareable']} |",
         f"| Rows with a per-row access category | {c['rows_with_access_categories_full']} | {c['rows_with_access_categories_shareable']} (openFDA-stated categories and absence statements only) |",
         f"| Matrix pairs with a target list | {c['pairs_with_target_list_full']} of {c['pairs_total']} | {c['pairs_with_target_list_shareable']} of {c['pairs_total']} |",
         f"| Target symbols listed in pairs | {c['target_symbols_listed_full']} | {c['target_symbols_listed_shareable']} |",
         f"| Card actions on targets listed | {c['card_actions_listed_full']} | {c['card_actions_listed_shareable']} |",
         f"| Excluded rows listed with compound name and gene | {c['excluded_rows_with_names_full']} | {c['excluded_rows_with_names_shareable']} |",
         f"| Card fields that differ (count of cards) | n/a | {json.dumps(c['card_fields_that_differ_count_of_cards'], sort_keys=True)} |", "",
         "## Why: counts of catalogue target rows by class", "",
         f"The catalogue holds {cen['records']:,} records. Its target rows by class: {json.dumps(cen['target_rows_by_class'], sort_keys=True)}.", "",
         "| Claim source | Class | Catalogue rows | Terms | In this page |", "|---|---|---|---|---|"]
    emb = {e["label"].split(" (")[0]: e["rows"] for e in man["embedded_sources"] if e.get("rows")}
    for s, v in cen["target_rows_by_claim_source"].items():
        mark = {"A": "attribution", "B": "share-alike", "C": "identifiers and counts", "UNCLASSIFIED": "UNCLASSIFIED"}[v["class"]]
        inpage = next((str(n) for lab, n in emb.items() if lab.startswith(s)), "0")
        L.append(f"| {s} | {v['class']} ({mark}) | {v['catalogue_rows']:,} | {v['terms']} | {inpage} |")
    L += ["", "Classes: **A** redistribute with attribution (only fields the source's own authors own); **B** share-alike: never merged into the page; **C** identifiers and counts only; **D** local only. Class B content is shipped only for ChEMBL, as a separate file; GtoPdb and ClinPGx stay counts-only (reasons in `NOTICE.md`).", "",
          "Third-party identifier values that exist in the catalogue and are not embedded at all (DrugBank, ChEBI, ATC, UNII, InChIKey, MATRIX ids): "
          + json.dumps(cen["third_party_identifier_values_in_catalogue_not_embedded"], sort_keys=True) + ".", "",
          "## What the withheld parts mean for a reader", "",
          "The physician-facing content (what to study, on what evidence, with which gaps) is complete here. What is withheld is the catalogue-level detail that backs the links between compounds and targets: which database says what about which compound. Where the full version shows a target list for a compound, this one shows how many source rows exist and that they were withheld. Nothing is hidden to change a conclusion; the counts and the statement that rows were withheld stay visible on the page.", ""]
    return "\n".join(L)


# ---------------------------------------------------------------------------- build
def build_files(dr: Path, corpus_dirs: list[Path] | None = None, recompute_text: bool = True) -> tuple[dict[str, bytes], dict]:
    allow = rv.load_allowlist(dr)
    html = rv.build(dr, "shareable")
    PF, PS = rv.build_payload(dr, "full"), rv.build_payload(dr, "shareable")
    rep, ref = au.audit_html(html, dr)
    if not rep.ok:
        raise SystemExit("the shareable build fails its audit; no package is written:\n" + au.render_report(rep, "audit"))
    chembl = chembl_records(dr, allow)
    chembl_bytes = ("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in chembl)).encode("utf-8")
    licences = {}
    for rel, spec in allow["licence_texts"].items():
        b = (dr / PKG / rel).read_bytes()
        if sha(b) != spec["sha256"]:
            raise SystemExit(f"{rel} does not match the digest pinned in shareable_sources.json")
        licences[rel] = b
    census = catalogue_census(dr, allow)
    cmp_ = compare_payloads(PF, PS)
    meta = PS["cur"]["meta"]
    audit_info = {"violations": len(rep.violations), "identifiers": rep.info["identifiers"], "links": rep.info["links"],
                  "reference": {k: v for k, v in rep.info["reference"].items() if k != "claim_source_rows"},
                  "field_provenance": {rx: {"class": r["class"], "why": r["why"], "values": r["values"]} for rx, r in sorted(rep.rules.items())},
                  "text_provenance_file": TEXT_FILE}
    class_counts = Counter(r["class"] for r in rep.rules.values())
    embedded_sources = [dict(e) for e in PS["cur"]["footer"]["embedded"]]
    man = {
        "schema": SCHEMA, "generator": COMMAND, "perimeter": "local preview; not published; publication on any external surface needs the operator's decision",
        "data": {"data_date": meta["data_date"], "catalogue_generated": meta["catalogue_generated"], "dgidb_export": meta["dgidb_export"], "view_schema": rv.SCHEMA},
        "embedded_sources": embedded_sources,
        "embedded_field_classes": {k: sum(r["values"] for r in rep.rules.values() if r["class"] == k) for k in sorted(class_counts)},
        "identifier_and_bibliographic_sources": PS["cur"]["footer"]["identifiers"], "class_b_files": PS["cur"]["footer"]["class_b"],
        "counts_only_sources": PS["cur"]["footer"]["counts_only"], "withheld": census, "comparison": cmp_,
        "audit": audit_info,
        "class_b_content": {"file": CHEMBL_FILE, "records": len(chembl), "chembl_ids": [r["chembl_id"] for r in chembl], "mechanism_rows": sum(len(r["curated_mechanisms"]) for r in chembl), "release": allow["class_b_files"]["chembl"]["release"]},
        "licence_texts": {k: v["sha256"] for k, v in allow["licence_texts"].items()},
    }
    files = {"index.html": html.encode("utf-8"), CHEMBL_FILE: chembl_bytes, CHEMBL_DIR + "/LICENSE_CC-BY-SA-3.0.txt": licences["LICENSES/CC-BY-SA-3.0.txt"],
             CHEMBL_DIR + "/CREDIT.txt": chembl_credit(allow, len(chembl)).encode("utf-8")}
    for rel, b in licences.items():
        files[rel] = b
    tb = text_provenance_file(dr, PS, corpus_dirs) if recompute_text else None
    if tb is None and (dr / PKG / TEXT_FILE).exists():
        tb = (dr / PKG / TEXT_FILE).read_bytes()   # no corpus here: carry the recorded result over
    if tb is not None:
        files[TEXT_FILE] = tb
    files["NOTICE.md"] = notice_md(allow, PS, man).encode("utf-8")
    files["COMPARISON.md"] = comparison_md(man).encode("utf-8")
    files["README.md"] = readme_md(man).encode("utf-8")
    man["files"] = {k: {"sha256": sha(v), "bytes": len(v)} for k, v in sorted(files.items())}
    files["manifest.json"] = (json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    return files, man


TEXT_FILE = "TEXT_PROVENANCE.json"


def text_provenance_file(dr: Path, PS: dict, corpus_dirs: list[Path] | None) -> bytes | None:
    """Provenance of the cards' own text against the third-party texts held locally. Environment-dependent (needs the corpus), so the file is written
    when a corpus is present and otherwise carried over unchanged from the folder; no corpus path is recorded."""
    dirs = corpus_dirs if corpus_dirs is not None else au.default_corpus_dirs()
    if not dirs:
        return None
    res = au.text_overlap(PS, dirs)
    r2 = au.Report()
    s = au.judge_text_overlap(res, r2)
    if not r2.ok:
        raise SystemExit("provenance-of-text failures: " + json.dumps(r2.violations[:5]))
    doc = {"schema": "legend.wwox.repurposing_view.text_provenance/1",
           "method": f"every string of the shareable data object against the third-party texts held locally (full texts, abstracts, openFDA label JSON), longest verbatim run in words (shingle {7}); limits: unquoted phrase <= {au.MAX_VERBATIM_WORDS} words, marked quotation <= {au.SHORT_QUOTE_MAX} words, or <= {au.ATTRIBUTED_QUOTE_MAX} words with an attribution phrase",
           "corpus_files": res["corpus_files"], "corpus_by_extension": res["corpus_by_extension"], "corpus_words": res["corpus_words"], "bibliographic_title_runs": s["titles"], "unquoted_runs_within_limit": s["short_unquoted"],
           "short_marked_quotations": s["short_marked_quotations"], "attributed_quotations": s["attributed_quotations"], "failures": s["failures"],
           "not_covered": "third-party texts not held locally; label sections that were not fetched"}
    return (json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def write(dr: Path, files: dict[str, bytes]) -> list[str]:
    base = dr / PKG
    changed = []
    for rel, b in sorted(files.items()):
        p = base / rel
        if not p.exists() or p.read_bytes() != b:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b)
            changed.append(rel)
    return changed


def check(dr: Path, files: dict[str, bytes]) -> list[str]:
    base = dr / PKG
    bad = [rel for rel, b in sorted(files.items()) if not (base / rel).exists() or (base / rel).read_bytes() != b]
    on_disk = {str(p.relative_to(base)) for p in base.rglob("*") if p.is_file()} if base.exists() else set()
    bad += ["unexpected file: " + x for x in sorted(on_disk - set(files))]
    return bad


def make_zip(base: Path, files: dict[str, bytes], target: Path) -> str:
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in sorted(files):
            zi = zipfile.ZipInfo("wwox_repurposing_shareable_package/" + rel, date_time=(2026, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, files[rel])
    return sha(target.read_bytes())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dr", type=Path, default=rv.DEFAULT_DR)
    ap.add_argument("--check", action="store_true", help="exit 1 if the folder differs from a fresh build")
    ap.add_argument("--zip", type=Path, default=None, help="also write a deterministic zip of the folder here")
    ap.add_argument("--no-write", action="store_true", help="build and audit only (the zip, if requested, is still written)")
    ap.add_argument("--text-corpus", type=Path, action="append", help="third-party text directory for TEXT_PROVENANCE.json (default: the local files/fulltext)")
    a = ap.parse_args(argv)
    files, man = build_files(a.dr, a.text_corpus, recompute_text=not a.check)
    rc = 0
    if a.check:
        bad = check(a.dr, files)
        for b in bad:
            print("STALE:", b)
        print("package is current" if not bad else f"package differs: run {COMMAND}")
        rc = 1 if bad else 0
    elif not a.no_write:
        changed = write(a.dr, files)
        print(f"package {a.dr / PKG}: {len(files)} files, {len(changed)} written")
    if a.zip:
        print(f"zip {a.zip}: sha256 {make_zip(a.dr / PKG, files, a.zip)}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
