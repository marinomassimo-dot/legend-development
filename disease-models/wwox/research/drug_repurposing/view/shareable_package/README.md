# WWOX repurposing view: shareable package (local preview)

Research material at disease and reference-genotype level: what to study for WWOX-related epileptic encephalopathy, and on what evidence. Not medical advice, not a ranking of treatments, not a probability of benefit. The page is in Italian for the physician; scientific citations keep their original form.

**Perimeter: this folder is a local preview. It has not been published anywhere, and publication on any external surface (a website, a repository change, an e-mail attachment to third parties) requires the operator's decision.**

## Open it

Open `index.html` by double-click or from `file://`. It is one self-contained file (inline CSS and JavaScript, data embedded as JSON); it needs no server, loads nothing from the network and opens identically from any folder or from the unzipped archive. Links inside it go to the same page (`#...` anchors) or to public identifiers (PubMed, DOI, ChEMBL, source licence pages); none is a repository-relative path.

Card export (print / PDF, standalone HTML download) and the comparison view work offline: use the buttons on a card profile, or the URL fragments `#export=<card id>`, `#brief=<card id>` (one A4 page per card) and `#compare=<id>,<id>`; the sections on selection, hypotheses and predictive test print on their own through `#section=selection`, `#section=hypotheses` and `#section=predictive`.

## Hand it over

Build a zip with the documented command (deterministic: fixed timestamps, sorted entries):

```bash
python3 -B framework/scripts/repurposing_view.py package --zip /path/to/wwox_repurposing_shareable_package.zip
```

The zip holds exactly the folder: `index.html`, `NOTICE.md` (sources, terms, credit lines), `COMPARISON.md` (what the full version holds and this one withholds), `manifest.json` (machine-readable inventory with digests), `LICENSES/` and `class_b/chembl_cc-by-sa-3.0/`. Hand over the whole zip, not `index.html` alone: the NOTICE and the credit lines must travel with the page, and the ChEMBL file must travel with its own licence text.

## Regenerate and verify

```bash
python3 -B framework/scripts/repurposing_coverage.py run
python3 -B framework/scripts/repurposing_view.py run --source shareable
python3 -B framework/scripts/repurposing_view.py package
python3 -B framework/scripts/repurposing_view.py package --check
python3 -B framework/scripts/repurposing_view.py audit-shareable --dynamic
```

`audit-shareable` is the proof that the allowlist did what it says: it builds a reference of forbidden values from the full catalogue and fails if any string, row or identifier traceable to a non-allowlisted source is in the bytes, the rendered pages, the exports, the standalone downloads or the PDF text. It has a mutation test (`framework/scripts/test_repurposing_view.py`, class `ShareableAudit`).

## What is in and what is not

See `COMPARISON.md`. In short: every card, need, position (F/C/P), priority group, funnel count and chart is the same as in the full version; compound names that only third-party databases carry, per-row status and modality, and rows from non-allowlisted claim sources are replaced by catalogue identifiers and counts.

## Limits, stated plainly

- Pair-level link existence and association counts are kept for withheld compounds (an identifier with counts); the content of the link (target, action, source) is not. Whether that is acceptable for external circulation is for the operator.
- Bibliographic titles come from NCBI esummary records collected into a tracked cache; they are facts about published works, listed in `NOTICE.md`.
- The provenance-of-text check covers the third-party texts held locally (full texts, abstracts, five openFDA label JSON files fetched for the check); a source not held locally was not compared.
- Prose is protected by an explicit redaction list (`prose_policy`) plus audit checks: compound-target pairs asserted only by class-B/C sources are found by derivation from the catalogue; a compound whose only provenance is a catalogue row is found only when a local full-text corpus is present (otherwise reported as unchecked). A new card or lead sentence of that kind fails the audit until it is redacted.
- Names shorter than four characters cannot be traced by string and are covered only by the structural checks (rows carry card names or identifiers).
- The audit proves conformity with the policy file; the policy file is a licence reading that is not legal advice and has components marked uncertain in `NOTICE.md` (not widened).

Data date: 2026-10-31; catalogue built 2026-10-31T07:28:37Z; DGIdb export 2024-06-10.
