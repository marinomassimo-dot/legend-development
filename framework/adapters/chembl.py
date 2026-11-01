"""ChEMBL — mechanism of action and target components for one drug name, or the targets
ChEMBL knows for one gene symbol. REST, key-less, CC BY-SA 3.0. Measured 2026-10-22 (ChEMBL_37).

Request: {"drug": "bortezomib"}  or  {"gene": "WWOX"}
         or {"uniprot": "Q13224"} / {"target": "CHEMBL1904"}  (measured activities, see below)
Output hits: one per mechanism (action_type, mechanism_of_action, target_chembl_id, references)
or one per target found.

Activities (added 2026-10-29, iteration 6): `uniprot` resolves a stable accession to the ChEMBL
targets that contain it (SINGLE PROTEIN and complexes are listed apart, never merged); `target` (and/or
`molecule`, a ChEMBL id, which alone reads every target the molecule was measured on: channel blockers
are often curated against heteromeric complexes, so a single-protein target can be empty while the complex
holds the data) reads the activity rows with the assay context (assay organism, cell type, assay type,
confidence, relationship type) fetched from the assay endpoint. Each row keeps the value as
the source states it (standard_relation/value/units, pchembl_value, document), flags
data_validity_comment and potential_duplicate, and the output states `total_count`, `retrieved`
and `truncated`: a page cap that is hit is reported, never hidden. Optional: `types`
(default IC50, Ki, Kd, EC50), `max_rows` (default 400, at most MAX_ROWS = 20000; a query that still hits the cap says so), `molecule` (a ChEMBL id).
Every activity answer states `coverage`: COMPLETE, TRUNCATED (cap hit, rest unread), PARTIAL_ERROR (a page failed; the rows read are kept, `retrieved` of
`total_count`), NOT_READ (the first page failed) or, for a complete set of rows, COMPLETE_ASSAY_CONTEXT_MISSING / COMPLETE_TARGET_GENES_MISSING when a
batch of the assay or target lookup failed (rows carry null, never an empty string). These are states of one answer, never merged with NO_MATCH_FOUND.
Passing `fetch=_http.make_fetch(cache_dir)` adds a bounded retry and a cache of successful responses only; the answer then carries `transport` (hits, requests, failures).
Name lookup (`drug`): MATCH_FOUND needs a molecule whose name or synonym equals the queried name. A compound ChEMBL stores without any name or synonym
(Ro 25-6981 is CHEMBL305195 with none) or under another name (dizocilpine is stored as MK-801) cannot be found by name: the answer is NO_MATCH_FOUND with the
nearest hits (their synonyms and parent), a statement about the name, not about the compound. Declare the identity with `molecule_id` (a ChEMBL id): the molecule is
then read by id, `identity_basis` is `declared_chembl_id` and the queried name is kept for the record. A salt or child record (hierarchy parent differs) is reported with its
parent; its mechanism rows may be read from the parent and are then marked `mechanism_found_via` = parent_filter (the parent_molecule_chembl_id filter); activity rows of salt, parent, stereoisomer and metabolite are never merged.
An empty answer means "no row under these filters on this date", not that no activity exists. `max_phase` is carried as the source states it (a development stage,
not a score).
"""
from __future__ import annotations

from urllib.parse import quote

from . import _http

INFO = {
    "name": "chembl",
    "gives": "curated mechanism of action per drug with its reference; ChEMBL targets per gene",
    "network": "GET https://www.ebi.ac.uk/chembl/api/data/{status,molecule/search,mechanism,target/search,target,activity,assay}.json",
    "licence": "CC BY-SA 3.0; key-less, no payment",
    "inputs": "drug (name), gene (symbol), uniprot (accession) or target (ChEMBL target id); one of them",
    "outputs": "hits: mechanisms or targets; source_version = chembl_db_version",
    "licence_url": "https://chembl.gitbook.io/chembl-interface-documentation/about (Data Licensing) and "
                   "https://www.ebi.ac.uk/about/terms-of-use",
    "licence_read_on": "2026-10-23",
    "licence_terms": "'The ChEMBL data is made available on a Creative Commons Attribution-Share Alike 3.0 Unported License' "
                     "(share-alike: an adaptation of the data is redistributed under the same licence; this module copies "
                     "fields verbatim and does not redistribute a derived database). Web services under the EMBL-EBI terms of use: "
                     "'EMBL-EBI expects attribution'; no numeric rate limit, use must not prevent service to others. "
                     "Calculated compound properties come from commercial software and carry their own terms (not consumed here).",
    "citation": "Zdrazil B. et al. The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity "
                "data types and time periods. Nucleic Acids Res 2024;52(D1):D1180-D1192. https://doi.org/10.1093/nar/gkad1004; "
                "web services: Davies M. et al. 2015 (Nucleic Acids Res 43:W612)",
    "attribution": "Data from ChEMBL (EMBL-EBI), CC BY-SA 3.0, https://www.ebi.ac.uk/chembl/",
}

BASE = "https://www.ebi.ac.uk/chembl/api/data"
MAX_ROWS = 20000


def _new(request: dict) -> dict:
    return {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
            "requests_sent": [], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
            "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
            "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence", "error": ""}


ACTIVITY_TYPES = ("IC50", "Ki", "Kd", "EC50")
ASSAY_FIELDS = ("assay_organism", "assay_cell_type", "assay_tissue", "assay_type", "assay_test_type", "confidence_score", "relationship_type", "description")


def _targets_for_accession(accession: str, out: dict, fetch) -> bool:
    url = f"{BASE}/target.json?target_components__accession={quote(accession)}&limit=50"
    out["requests_sent"].append(url)
    status, payload = fetch(url)
    if status != 200 or not isinstance(payload, dict):
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return False
    for tg in payload.get("targets") or []:
        out["hits"].append({"kind": "target", "target_chembl_id": tg.get("target_chembl_id"), "pref_name": tg.get("pref_name"),
                            "organism": tg.get("organism"), "target_type": tg.get("target_type"),
                            "accessions": [c.get("accession") for c in tg.get("target_components") or []]})
    out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
    return True


PROTEIN_TYPES = ("SINGLE PROTEIN", "PROTEIN COMPLEX", "PROTEIN COMPLEX GROUP", "PROTEIN FAMILY", "SELECTIVITY GROUP", "PROTEIN-PROTEIN INTERACTION", "CHIMERIC PROTEIN")      # a protein-type target with no component symbol is UNKNOWN (null), not 'non-gene'


def _target_genes(rows: list, out: dict, fetch) -> dict:
    """target_chembl_id -> {target_type, gene_symbols, non_gene_target}, from the target endpoint in batches of 40 (the pattern used for assays).
    A function-to-compound query across heteromeric or complex targets needs the gene symbols of the components; a placeholder target ('Unchecked',
    'NON-PROTEIN TARGET') or a failed lookup stays null and says so in the note, it is never read as 'no gene'."""
    found = {}
    ids = sorted({r.get("target_chembl_id") for r in rows if r.get("target_chembl_id")})
    for i in range(0, len(ids), 40):
        url = f"{BASE}/target.json?target_chembl_id__in={quote(','.join(ids[i:i+40]))}&limit=100"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["note"] = (out.get("note", "") + f" target genes incomplete: HTTP {status} for target batch {i // 40 + 1}; rows carry target_gene_symbols=null where missing.").strip()
            continue
        for t in payload.get("targets") or []:
            syms = sorted({syn.get("component_synonym") for c in (t.get("target_components") or []) for syn in (c.get("target_component_synonyms") or [])
                           if syn.get("syn_type") == "GENE_SYMBOL" and syn.get("component_synonym")})
            ttype = t.get("target_type")
            found[t.get("target_chembl_id")] = {"target_type": ttype, "gene_symbols": syms or None,
                                                "non_gene_target": (False if syms else (None if str(ttype or "").upper() in PROTEIN_TYPES else True))}
    return found


def _activities(request: dict, out: dict, fetch) -> dict:
    target = str(request.get("target", "")).strip()
    types = request.get("types") or list(ACTIVITY_TYPES)
    cap = max(1, min(int(request.get("max_rows") or 400), MAX_ROWS))
    params = f"standard_type__in={quote(','.join(types))}"
    if target:
        params = f"target_chembl_id={quote(target)}&{params}"
    if request.get("molecule"):
        params += f"&molecule_chembl_id={quote(str(request['molecule']))}"
    rows, total, offset = [], None, 0
    while len(rows) < cap:
        url = f"{BASE}/activity.json?{params}&limit={min(200, cap - len(rows))}&offset={offset}"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            out["hits"] = [dict(h) for h in rows]
            out["retrieved"] = len(rows)
            out["total_count"] = total
            out["coverage"] = "PARTIAL_ERROR" if rows else "NOT_READ"
            out["next_offset"] = offset
            out["scope"] = {"target": target or None, "types": types, "molecule": request.get("molecule")}
            out["note"] = (out.get("note", "") + f" PARTIAL: the page at offset {offset} failed; {len(rows)} of {total} rows read. A rerun through a caching fetch reads only what is missing.").strip()
            return out
        total = (payload.get("page_meta") or {}).get("total_count", total)
        page = payload.get("activities") or []
        rows += page
        offset += len(page)
        if not page or not (payload.get("page_meta") or {}).get("next"):
            break
    assays, assay_failed = {}, 0
    ids = sorted({r.get("assay_chembl_id") for r in rows if r.get("assay_chembl_id")})
    for i in range(0, len(ids), 40):
        url = f"{BASE}/assay.json?assay_chembl_id__in={quote(','.join(ids[i:i+40]))}&limit=100"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["note"] = (out.get("note", "") + f" assay context incomplete: HTTP {status} for assay batch {i // 40 + 1}; rows carry assay_context=null where missing").strip()
            assay_failed += 1
            continue
        for a in payload.get("assays") or []:
            assays[a.get("assay_chembl_id")] = {k: a.get(k) for k in ASSAY_FIELDS}
    genes = _target_genes(rows, out, fetch)
    genes_failed = "target genes incomplete" in out.get("note", "")
    for r in rows:
        tg = genes.get(r.get("target_chembl_id"))
        out["hits"].append({"kind": "activity", "activity_id": r.get("activity_id"), "molecule_chembl_id": r.get("molecule_chembl_id"),
                            "parent_molecule_chembl_id": r.get("parent_molecule_chembl_id"), "molecule_pref_name": r.get("molecule_pref_name"),
                            "standard_type": r.get("standard_type"), "standard_relation": r.get("standard_relation"),
                            "standard_value": r.get("standard_value"), "standard_units": r.get("standard_units"),
                            "pchembl_value": r.get("pchembl_value"), "target_chembl_id": r.get("target_chembl_id"),
                            "target_organism": r.get("target_organism"), "target_pref_name": r.get("target_pref_name"), "assay_chembl_id": r.get("assay_chembl_id"),
                            "assay_description": r.get("assay_description"), "assay_context": assays.get(r.get("assay_chembl_id")),
                            "document_chembl_id": r.get("document_chembl_id"), "document_year": r.get("document_year"),
                            "data_validity_comment": r.get("data_validity_comment"), "potential_duplicate": r.get("potential_duplicate"),
                            "target_type": tg["target_type"] if tg else None, "target_gene_symbols": tg["gene_symbols"] if tg else None,
                            "non_gene_target": tg["non_gene_target"] if tg else None})
    out["total_count"], out["retrieved"] = total, len(rows)
    out["truncated"] = bool(total is not None and len(rows) < total)
    out["scope"] = {"target": target or None, "types": types, "molecule": request.get("molecule")}
    out["status"] = "MATCH_FOUND" if rows else "NO_MATCH_FOUND"
    out["coverage"] = ("TRUNCATED" if out["truncated"] else "COMPLETE_ASSAY_CONTEXT_MISSING" if assay_failed else
                       "COMPLETE_TARGET_GENES_MISSING" if genes_failed else "COMPLETE")
    out["assay_batches_failed"] = assay_failed
    if out["truncated"]:
        out["note"] = (out.get("note", "") + f" TRUNCATED: {len(rows)} of {total} rows retrieved under these filters; the rest were not read.").strip()
    return out


def query(request: dict, fetch=_http.get_json) -> dict:
    out = _query(request, fetch)
    stats = getattr(fetch, "stats", None)
    if stats is not None:
        out["transport"] = dict(stats)
    return out


def _molecule_view(mol: dict) -> dict:
    h = mol.get("molecule_hierarchy") or {}
    return {"molecule_chembl_id": mol.get("molecule_chembl_id"), "pref_name": mol.get("pref_name"), "max_phase": mol.get("max_phase"),
            "parent_molecule_chembl_id": h.get("parent_chembl_id") or mol.get("molecule_chembl_id"),
            "synonyms": sorted({str(x.get("molecule_synonym")) for x in mol.get("molecule_synonyms") or [] if x.get("molecule_synonym")})[:12],
            "inchikey": (mol.get("molecule_structures") or {}).get("standard_inchi_key")}


def _query(request: dict, fetch) -> dict:
    out = _new(request)
    drug = str(request.get("drug", "")).strip()
    gene = str(request.get("gene", "")).strip()
    uniprot = str(request.get("uniprot", "")).strip()
    target = str(request.get("target", "")).strip()
    molecule = str(request.get("molecule", "")).strip()
    if not (drug or gene or uniprot or target or molecule):
        out["error"] = "drug, gene, uniprot, target or molecule is required"
        return out
    url = f"{BASE}/status.json"
    out["requests_sent"].append(url)
    status, payload = fetch(url)
    if status == 200 and isinstance(payload, dict):
        out["source_version"] = f"{payload.get('chembl_db_version')} {payload.get('chembl_release_date')}"
    if uniprot:
        _targets_for_accession(uniprot, out, fetch)
        return out
    if target or molecule:
        return _activities(request, out, fetch)
    if gene:
        url = f"{BASE}/target/search.json?q={quote(gene)}&limit=20"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            return out
        for t in payload.get("targets") or []:
            out["hits"].append({"kind": "target", "target_chembl_id": t.get("target_chembl_id"),
                                "pref_name": t.get("pref_name"), "organism": t.get("organism"),
                                "target_type": t.get("target_type")})
        out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
        return out
    declared = str(request.get("molecule_id", "")).strip()
    if declared:
        url = f"{BASE}/molecule/{quote(declared)}.json"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status == 404:
            out["status"] = "NO_MATCH_FOUND"
            out["note"] = f"the declared id {declared} does not exist in this release"
            return out
        if status != 200 or not isinstance(payload, dict) or payload.get("molecule_chembl_id") != declared:
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            return out
        exact = [payload]
        out["identity_basis"] = "declared_chembl_id"
        out["queried_name"] = drug
    else:
        url = f"{BASE}/molecule/search.json?q={quote(drug)}&limit=5"  # a name with spaces is a valid query
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            return out
        molecules = payload.get("molecules") or []
        if not molecules:
            out["status"] = "NO_MATCH_FOUND"
            return out
        # A free-text search returns the nearest molecule, which for a sentence or a class name is some
        # unrelated entry (8 of 10 cached MATCH_FOUND answers of the join were not the named substance).
        # MATCH_FOUND therefore needs a molecule whose pref_name or synonym IS the queried name; the
        # nearest hit is recorded in `nearest` so a reader sees what the search returned instead.
        wanted = " ".join(drug.casefold().split())

        def names_of(mol):
            names = [mol.get("pref_name")] + [syn.get("molecule_synonym") for syn in mol.get("molecule_synonyms") or []]
            return {" ".join(str(n).casefold().split()) for n in names if n}
        exact = [mol for mol in molecules if wanted in names_of(mol)]
        if not exact:
            out["status"] = "NO_MATCH_FOUND"
            out["nearest"] = [_molecule_view(m) for m in molecules[:3]]
            out["note"] = ("NO_MATCH_FOUND is an answer about this query on this date, never absence: no molecule's name or synonym equals the queried name; the nearest "
                           "search hits are in `nearest` and are NOT the named substance (a compound stored under another name or without any name needs `molecule_id`)")
            return out
    for mol in exact[:1]:
        mid = mol.get("molecule_chembl_id")
        parent = (mol.get("molecule_hierarchy") or {}).get("parent_chembl_id") or mid
        via = "molecule"
        url = f"{BASE}/mechanism.json?molecule_chembl_id={mid}&limit=20"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            return out
        mechanisms = payload.get("mechanisms") or []
        if not mechanisms:
            # Measured 2026-10-27: for some molecules (e.g. CHEMBL192, sildenafil) `molecule_chembl_id=` returns 0 rows while
            # `parent_molecule_chembl_id=` returns the curated mechanism; without this second request such a drug was reported as
            # `molecule_without_mechanism`, a false negative of the lookup.
            via = "parent_filter"
            url = f"{BASE}/mechanism.json?parent_molecule_chembl_id={parent}&limit=20"
            out["requests_sent"].append(url)
            status, payload = fetch(url)
            if status != 200 or not isinstance(payload, dict):
                out["error"] = f"HTTP {status}: {str(payload)[:300]}"
                return out
            mechanisms = payload.get("mechanisms") or []
        for m in mechanisms:
            out["hits"].append({"kind": "mechanism", "molecule_chembl_id": mid,
                                "pref_name": mol.get("pref_name"), "max_phase": mol.get("max_phase"),
                                "parent_molecule_chembl_id": parent, "queried_is_salt_or_child": parent != mid, "mechanism_found_via": via,
                                "action_type": m.get("action_type"),
                                "mechanism_of_action": m.get("mechanism_of_action"),
                                "target_chembl_id": m.get("target_chembl_id"),
                                "references": [f"{r.get('ref_type')}:{r.get('ref_id')}" for r in m.get("mechanism_refs") or []]})
        if not out["hits"]:
            out["hits"].append({"kind": "molecule_without_mechanism", "molecule_chembl_id": mid,
                                "pref_name": mol.get("pref_name"), "max_phase": mol.get("max_phase"),
                                "parent_molecule_chembl_id": parent, "queried_is_salt_or_child": parent != mid})
    out["status"] = "MATCH_FOUND"
    return out


SAMPLE = {
    "request": {"drug": "bortezomib"},
    "responses": {
        "status.json": (200, {"chembl_db_version": "ChEMBL_37", "chembl_release_date": "2026-05-01"}),
        "molecule/search": (200, {"molecules": [{"molecule_chembl_id": "CHEMBL325041", "pref_name": "BORTEZOMIB", "max_phase": 4.0}]}),
        "mechanism.json": (200, {"mechanisms": [{"action_type": "INHIBITOR", "mechanism_of_action": "26S proteasome inhibitor",
                                                 "target_chembl_id": "CHEMBL2364701",
                                                 "mechanism_refs": [{"ref_type": "DailyMed", "ref_id": "setid=example"}]}]}),
    },
}


def _canned(url, params=None, body=None, timeout=20):
    for key, value in SAMPLE["responses"].items():
        if key in url:
            return value
    return 404, {}


def selftest(fetch=None) -> dict:
    result = query(SAMPLE["request"], fetch=_canned if fetch is None else fetch)
    ok = result["status"] == "MATCH_FOUND" and any(h.get("kind") == "mechanism" for h in result["hits"])
    return {"ok": bool(ok), "status": result["status"], "hits": len(result["hits"]),
            "source_version": result["source_version"], "error": result["error"]}
