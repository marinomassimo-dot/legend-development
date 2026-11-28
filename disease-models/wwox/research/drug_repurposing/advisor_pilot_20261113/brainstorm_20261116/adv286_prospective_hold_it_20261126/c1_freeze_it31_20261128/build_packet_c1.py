import sys, csv, pathlib
csv.field_size_limit(10**7)
base = pathlib.Path('disease-models/wwox/research/drug_repurposing')
adv = base/'advisor_pilot_20261113/brainstorm_20261116/adv139_nappi_inv15_sci_20261121/RESULT_ADV139_NAPPI_INV15_SCI_20261121.md'
readme = base/'nappi_poster_it32_20261107/README.md'
out = ['# ADV-286 C1: input packet (held material, copied verbatim on 2026-11-28)\n',
       'Hypothesis level; nothing here is medical advice. Extracts of repository files; the files stand as written.\n']
L = adv.read_text().splitlines()
out.append('\n## A. RESULT_ADV139, lines 1 to 10 and 25 to 32 (levels table)\n')
out += L[0:10] + [''] + L[24:32]
out.append('\n## B. NINDS poster 014 README (whole file)\n')
out += readme.read_text().splitlines()
def row(path, key):
    with open(path, newline='') as f:
        r = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        head = next(r)
        for x in r:
            if x and x[0] == key:
                return ['%s: %s' % (h, v) for h, v in zip(head, x)]
    sys.exit('missing %s in %s' % (key, path))
for title, path, key in (('C. Portfolio row RP-042', base/'research_portfolio.tsv', 'RP-042'),
                         ('D. Portfolio row RP-019', base/'research_portfolio.tsv', 'RP-019'),
                         ('E. Investigation INV-15', base/'ranking_it8_p9_20261029/investigations_it20.tsv', 'INV-15')):
    out.append('\n## %s (%s)\n' % (title, path.name))
    out += row(path, key)
pathlib.Path(sys.argv[1]).write_text('\n'.join(out) + '\n')
