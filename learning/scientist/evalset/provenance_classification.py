#!/usr/bin/env python3
"""FOUR-WAY PROVENANCE CLASSIFICATION, decided structurally.

    PROVENANCE_SEPARATED         all six fields derivable, from a file that carries no
                                 adjudication-bearing key
    CONTAMINATED                 all six fields derivable, but ONLY from a file that also
                                 carries adjudication
    MISSING_PROVENANCE_STRUCTURE not derivable, but every artifact is IDENTIFIED by a
                                 digest — a debt that closes by adding structure
    UNRESOLVABLE                 not derivable and not identifiable: no future act can
                                 reconstruct provenance from what exists

🔴 This supersedes a count I published last session. `participant_provenance_view.py
--feasibility` reports how many papers have all six fields DERIVABLE, and I carried that
number forward as `PROVENANCE_SEPARATION_COUNT 5`. Derivability is not separation. The
projection drops adjudication from its OUTPUT; it cannot drop it from its INPUT, and
`verbatim_locators` is present in 64 of 64 deepdive manifests — carrying, in the one I
opened, prose that states the paper's finding outright. Every field the projection emits
is read out of a file that states conclusions about the same paper.

For the PARTICIPANT nothing changes: the surface never contains a manifest, and the
emitted record is whitelisted. What changes is the claim MSR-1..MSR-4 actually make —
that a provenance record be derivable WITHOUT READING AN ADJUDICATION. The derivation
act, not the emitted record, is what fails that.

A paper is classified by its WEAKEST figure row. A paper is only as separated as its
least-provenanced figure, and aggregating any other way optimises the count.

    python3 learning/scientist/evalset/provenance_classification.py
    python3 learning/scientist/evalset/provenance_classification.py --show CONTAMINATED

EVALUATOR TOOL.
"""
import argparse, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from participant_provenance_view import view, MANIFESTS, PAGEADJ, REPO   # noqa: E402

# Keys whose PRESENCE anywhere in a record means the file states conclusions about the
# paper. Tested as KEYS at any depth, not as words in text: a word list over a JSON file
# fires on the vocabulary of the schema, and misses a conclusion phrased in ordinary prose.
ADJUDICATION_KEYS = {
    'verbatim_locators', 'propositions', 'adjudicates', 'needles',
    'why_this_article_is_adjudicated', 'the_defect_is_visible_inside_the_adjudicated_set',
    'claim_links', 'invalidates_receipt', 'coverage_gaps', 'declared_reading_gap',
}


def keys_at_any_depth(obj, acc=None):
    acc = set() if acc is None else acc
    if isinstance(obj, dict):
        for k, v in obj.items():
            acc.add(k)
            keys_at_any_depth(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            keys_at_any_depth(v, acc)
    return acc


def adjudication_keys_in(path):
    try:
        d = json.load(open(path, encoding='utf-8'))
    except (OSError, ValueError):
        return None
    return sorted(ADJUDICATION_KEYS & keys_at_any_depth(d))


def source_files_for(pmid, origin):
    """The files that must be OPENED to derive this paper's provenance."""
    if origin == 'page_adjudications':
        return [os.path.join(PAGEADJ, 'PMID%s' % pmid, 'adjudications.json')]
    return [os.path.join(MANIFESTS, 'PMID%s.json' % pmid)]


def classify(pmid):
    v = view(pmid)
    if not v or not v['rows']:
        return {'pmid': pmid, 'klass': 'UNRESOLVABLE', 'why': 'no figure provenance record at all',
                'rows': 0, 'derivable': 0, 'identified': 0, 'sources': [], 'adj_keys': []}

    rows = v['rows']
    derivable = [r for r in rows if r.get('regeneration_recipe')]
    identified = [r for r in rows if r.get('file_digest')]

    srcs = source_files_for(pmid, v['origin'])
    adj = sorted({k for s in srcs for k in (adjudication_keys_in(s) or [])})

    # A crop rectangle is a prior reader's attention, stated more precisely than a render.
    # The case specs EXCLUDE prior-reader renders because "their selection encodes a prior
    # reader's attention — which pages, at what dpi". A recipe carrying `crop_xyxy` encodes
    # the same thing and narrower. So separability and participant-safety are two questions,
    # and a record can pass the first and fail the second.
    crop_rows = [r for r in rows if isinstance(r.get('regeneration_recipe'), dict)
                 and r['regeneration_recipe'].get('crop_xyxy') is not None]

    if len(derivable) == len(rows):
        klass = 'CONTAMINATED' if adj else 'PROVENANCE_SEPARATED'
        why = ('every row carries a recipe, but deriving it means opening %s, which carries %s'
               % (', '.join(os.path.basename(s) for s in srcs), ', '.join(adj))) if adj else \
              'every row carries a recipe, and no source file carries an adjudication key'
    elif len(identified) == len(rows):
        klass = 'MISSING_PROVENANCE_STRUCTURE'
        why = ('%d of %d rows have no regeneration recipe; every row is identified by a '
               'digest, so the debt closes by adding page/crop/dpi or a fetch URL'
               % (len(rows) - len(derivable), len(rows)))
    else:
        klass = 'UNRESOLVABLE'
        why = ('%d of %d rows carry neither a recipe nor a digest: the object is neither '
               'makeable nor identifiable' % (len(rows) - len(identified), len(rows)))
    return {'pmid': pmid, 'klass': klass, 'why': why, 'rows': len(rows),
            'derivable': len(derivable), 'identified': len(identified),
            'sources': srcs, 'adj_keys': adj, 'origin': v['origin'],
            'crop_rows': len(crop_rows)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--show', action='append', default=[],
                    help='print the per-paper reason for these classes')
    a = ap.parse_args()

    results = []
    for p in sorted(glob.glob(os.path.join(MANIFESTS, '*.json'))):
        d = json.load(open(p, encoding='utf-8'))
        pmid = str(d.get('pmid') or os.path.basename(p)[4:-5])
        figs = [x for x in (d.get('source_artifacts') or [])
                if isinstance(x, dict) and x.get('kind') == 'figure']
        if not figs:
            continue
        results.append(classify(pmid))

    order = ['PROVENANCE_SEPARATED', 'CONTAMINATED', 'MISSING_PROVENANCE_STRUCTURE',
             'UNRESOLVABLE']
    print("PROVENANCE CLASSIFICATION — papers with >=1 figure artifact: %d" % len(results))
    print()
    for k in order:
        sel = [r for r in results if r['klass'] == k]
        print("  %-30s %3d" % (k, len(sel)))
    print()
    sep_route = [r for r in results if r['klass'] == 'CONTAMINATED']
    crop_bearing = [r for r in sep_route if r['crop_rows']]
    print("  separable by emitting the whitelisted projection to a standalone")
    print("  file carrying no adjudication key                      %3d" % len(sep_route))
    print("     of those, carrying crop_xyxy — a prior reader's attention, stated")
    print("     MORE precisely than the renders the case specs exclude  %3d" % len(crop_bearing))
    print("     carrying only a publisher fetch URL for a whole figure  %3d"
          % (len(sep_route) - len(crop_bearing)))
    print()
    tot = sum(r['rows'] for r in results)
    print("  figure rows total                %3d" % tot)
    print("  rows with a regeneration recipe  %3d" % sum(r['derivable'] for r in results))
    print("  rows identified by a digest      %3d" % sum(r['identified'] for r in results))
    print()
    print("  🔴 PROVENANCE_SEPARATED counts papers whose provenance can be derived WITHOUT")
    print("     opening a file that states conclusions about that same paper. It is not the")
    print("     same question as whether the six fields exist, and last session I reported")
    print("     the second number under the first name.")

    for k in a.show:
        sel = [r for r in results if r['klass'] == k]
        print()
        print("=" * 92)
        print("%s — %d" % (k, len(sel)))
        print("=" * 92)
        for r in sel:
            print("  PMID %-9s rows=%-3d recipe=%-3d origin=%-19s %s"
                  % (r['pmid'], r['rows'], r['derivable'], r.get('origin', '-'), r['why'][:60]))
            if r['adj_keys']:
                print("      adjudication keys in the source: %s" % ', '.join(r['adj_keys']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
