#!/usr/bin/env python3
"""PARTICIPANT-SAFE PROVENANCE VIEW — a projection, not a second store.

The measured problem: 57 of 58 papers have figure provenance nowhere outside a file that
also states verdicts. The requirement (MSR-1..MSR-4) is that a provenance record be
derivable without reading an adjudication.

This emits, per paper, only:

    SOURCE_ID · FILE_DIGEST · FIGURE_ID · PAGE · REGENERATION_RECIPE · PATH_OR_CONTENT_HANDLE

by WHITELIST of field names. Anything not on the list is dropped, including a field that
looks harmless: a blacklist of words is the mistake at schema level that quoting a caption
is at reading level.

    python3 learning/scientist/evalset/participant_provenance_view.py --feasibility
    python3 learning/scientist/evalset/participant_provenance_view.py --pmid 21212533

EVALUATOR TOOL. Its OUTPUT is participant-safe; this file is not a participant surface.
"""
import argparse, glob, json, os, re, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
MANIFESTS = os.path.join(REPO, 'disease-models/wwox/research/deepdive_manifests')
PAGEADJ = os.path.join(REPO, 'disease-models/wwox/research/page_adjudications')

# The whitelist. Keys are the six required outputs; values are where each may be read from.
EMIT = ('source_id', 'file_digest', 'figure_id', 'page', 'regeneration_recipe', 'handle')

# Keys in the source records that carry adjudication or interpretation and are DROPPED.
# Listed for the record; the emitter does not consult this list — it emits the whitelist
# and nothing else, so a key added upstream tomorrow is dropped without an edit here.
KNOWN_ADJUDICATIVE = ('adjudicates', 'needles', 'why_this_article_is_adjudicated',
                      'the_defect_is_visible_inside_the_adjudicated_set', 'dpi_discipline',
                      'note', 'propositions', 'verbatim_locators', 'citation')

# A filename can itself carry interpretation. Screened, not assumed clean.
INTERPRETIVE_NAME = re.compile(
    r'rationale|refut|contradict|unsupported|overclaim|defect|wrong|missing|empty|'
    r'proof|shows_|proves|no_|absent', re.I)


def from_page_adjudications(pmid):
    p = os.path.join(PAGEADJ, 'PMID%s' % pmid, 'adjudications.json')
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding='utf-8'))
    src = d.get('source_pdf') or {}
    rows = []
    per_page = {}
    for a in d.get('artifacts') or []:
        crop, dpi, page = a.get('crop'), a.get('dpi'), a.get('page')
        recipe = None
        if crop is not None and dpi is not None and page is not None:
            recipe = {'tool': 'regenerate_adjudications.py', 'source_pdf_sha256': src.get('sha256'),
                      'page': page, 'crop_xyxy': crop, 'dpi': dpi,
                      'coordinate_system': 'PDF points, origin top-left, as consumed by PyMuPDF clip'}
        # 🔴 THE STORED FILENAME IS NOT EMITTED. Measured on the three papers that have
        # this record: of 27 crop filenames, at least seven state a conclusion —
        # `p03_CT_indispensable_no_structure`, `p03_ww1_primarily_responsible`,
        # `p02_unfavorable_substrate`, `p02_rationale_common_targets`,
        # `p08_affinity_asymmetry`, `p03_CT_invisible_in_crystal_structures`,
        # `p08_generalised_frame`. A participant handed those handles learns the finding
        # without opening the file. Screening them by word list caught two of the seven,
        # which is the same shape of mistake as a blacklist at schema level. So the name
        # is dropped entirely: the digest IDENTIFIES the object, the recipe LOCATES it,
        # and a positional id ORDERS it. A prior reader's description adds nothing a
        # participant needs and carries their attention.
        per_page[page] = per_page.get(page, 0) + 1
        rows.append({'source_id': 'PMID%s' % pmid,
                     'file_digest': a.get('sha256'),
                     'figure_id': 'p%s_c%d' % (page, per_page[page]),
                     'page': page,
                     'regeneration_recipe': recipe,
                     'handle': '%s.png' % (a.get('sha256') or 'unknown')[:16]})
    return {'origin': 'page_adjudications', 'source_pdf': {'path': src.get('path'),
                                                           'sha256': src.get('sha256')}, 'rows': rows}


# A publisher URL is a location, not an interpretation. It is the ONE thing that may be
# lifted out of the free-text `route` field — and only the URL itself, never the prose
# around it, which is a prior reader's account of how retrieval went.
URL = re.compile(r'\b((?:https?://)?(?:cdn\.ncbi\.nlm\.nih\.gov|www\.ncbi\.nlm\.nih\.gov|'
                 r'europepmc\.org|ftp\.ncbi\.nlm\.nih\.gov)/[^\s,;]+\.(?:jpg|jpeg|png|gif|tif|tiff))')


def from_manifest(pmid):
    p = os.path.join(MANIFESTS, 'PMID%s.json' % pmid)
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding='utf-8'))
    rows = []
    for i, a in enumerate(d.get('source_artifacts') or [], 1):
        if not isinstance(a, dict) or a.get('kind') != 'figure':
            continue
        recipe = None
        m = URL.search(str(a.get('route') or ''))
        if m:
            # kind=fetch: the object is a publisher raster, so there is no crop to state.
            # Only the URL crosses; the surrounding prose does not.
            recipe = {'kind': 'fetch', 'url': m.group(1),
                      'expected_sha256': a.get('sha256'),
                      'native_px': a.get('native_px')}
        rows.append({'source_id': 'PMID%s' % pmid,
                     'file_digest': a.get('sha256'),
                     'figure_id': a.get('figure') or 'a%02d' % i,
                     'page': None,
                     'regeneration_recipe': recipe,
                     'handle': '%s%s' % ((a.get('sha256') or 'unknown')[:16],
                                         os.path.splitext(a.get('path') or '')[1] or '.bin')})
    return {'origin': 'deepdive_manifest', 'source_pdf': None, 'rows': rows}


def view(pmid):
    v = from_page_adjudications(pmid)
    if v and v['rows']:
        return v
    return from_manifest(pmid)


def audit(v):
    """Return findings: emitted keys outside the whitelist, and interpretive filenames."""
    f = []
    for r in v['rows']:
        extra = set(r) - set(EMIT)
        if extra:
            f.append(('WHITELIST', 'row emits non-whitelisted key(s): %s' % sorted(extra)))
        for field in ('handle', 'figure_id'):
            val = r.get(field) or ''
            if INTERPRETIVE_NAME.search(str(val)):
                f.append(('INTERPRETIVE_NAME', '%s=%r reads as a conclusion, not a location'
                          % (field, val)))
    return f


def feasibility():
    pm_fig, complete, partial, none_ = set(), [], [], []
    for p in sorted(glob.glob(os.path.join(MANIFESTS, '*.json'))):
        d = json.load(open(p, encoding='utf-8'))
        pmid = str(d.get('pmid') or os.path.basename(p)[4:-5])
        figs = [a for a in (d.get('source_artifacts') or [])
                if isinstance(a, dict) and a.get('kind') == 'figure']
        if not figs:
            continue
        pm_fig.add(pmid)
        v = view(pmid)
        rows = v['rows'] if v else []
        full = [r for r in rows if r['regeneration_recipe']]
        if full and len(full) == len(rows):
            complete.append(pmid)
        elif full:
            partial.append(pmid)
        else:
            none_.append(pmid)
    print("FEASIBILITY of the six-field participant-safe view, over papers with figure artifacts")
    print("  papers with >=1 figure artifact           %d" % len(pm_fig))
    print("  ALL six fields derivable                  %d   %s" % (len(complete), ' '.join(sorted(complete))))
    print("  SOME rows complete                        %d   %s" % (len(partial), ' '.join(sorted(partial))))
    print("  NO regeneration recipe derivable          %d" % len(none_))
    print()
    print("  🔴 The blocker is not adjudication co-location. It is that PAGE, CROP and DPI")
    print("     do not exist as structured fields in deepdive_manifests[].source_artifacts —")
    print("     which carries path, sha256, kind and, for a minority, native_px/effective_ppi.")
    print("     A digest VERIFIES a render you already hold; it does not let you MAKE one.")
    return complete, partial, none_


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pmid', action='append')
    ap.add_argument('--feasibility', action='store_true')
    a = ap.parse_args()
    if a.feasibility:
        feasibility()
        if not a.pmid:
            return 0
    rc = 0
    for pmid in (a.pmid or []):
        v = view(pmid)
        print("=" * 92)
        print("PMID %s   origin=%s   rows=%d" % (pmid, v['origin'] if v else '-', len(v['rows']) if v else 0))
        print("=" * 92)
        if not v:
            print("  no provenance record"); rc = 1; continue
        print(json.dumps({'source_pdf': v['source_pdf'], 'rows': v['rows'][:4]}, indent=1)[:1600])
        if len(v['rows']) > 4:
            print("  … %d more rows" % (len(v['rows']) - 4))
        f = audit(v)
        print("\n  AUDIT: %s" % ('clean' if not f else '%d finding(s)' % len(f)))
        for cls, msg in f:
            print("    [%s] %s" % (cls, msg))
            rc = 1
    return rc


if __name__ == '__main__':
    sys.exit(main())
