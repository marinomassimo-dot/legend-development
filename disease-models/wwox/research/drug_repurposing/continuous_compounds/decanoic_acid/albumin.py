"""One-binding-step sensitivity for C10; no conversion from plasma to brain is assumed."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ALBUMIN_MASS_DA = 66500  # rounded human albumin mass
K_HIGH_PER_UM = 11.0
K_LOW_PER_UM = 0.14


def occupied(free, association):
    product = free * association
    return product / (1.0 + product)


def total_at(free, albumin, high_fraction):
    occupancy = (high_fraction * occupied(free, K_HIGH_PER_UM)
                 + (1 - high_fraction) * occupied(free, K_LOW_PER_UM))
    return free + albumin * occupancy


def unbound(total, albumin, high_fraction):
    low, high = 0.0, total
    for _ in range(90):
        mid = (low + high) / 2
        if total_at(mid, albumin, high_fraction) > total:
            high = mid
        else:
            low = mid
    free = (low + high) / 2
    assert abs(total_at(free, albumin, high_fraction) - total) < 1e-8
    return free


def run(directory, output):
    pediatric = ET.parse(directory / 'PMC8557697.xml')
    table, = [t for t in pediatric.findall('.//table-wrap') if t.findtext('label') == 'Table 4']
    header = table.find('.//tr')
    assert header.findall('th')[1].text == 'Children'
    albumin_row, = [r for r in table.findall('.//tr') if r.findtext('td') == 'Albumin (g/l)']
    assert albumin_row.findall('td')[2].text.strip() == '44 (39–50)'
    all_text = ' '.join(' '.join(pediatric.getroot().itertext()).split())
    assert '165.1 (18.3–407.4)' in all_text
    binding = ET.parse(directory / 'binding_primary.xml')
    study, = [a for a in binding.findall('PubmedArticle') if a.findtext('.//PMID') == '3407921']
    abstract = ' '.join(study.find('.//Abstract').itertext())
    assert '1.1 X 10(7) and 1.4 X 10(5) M-1' in abstract and '0.65' in abstract
    with output.open('w', newline='') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['albumin_g_L', 'C10_total_uM', 'available_fraction_assumed', 'high_fraction',
                         'free_uM_first_step_only', 'free_pct'])
        for grams in (39, 44, 50):
            for total in (165.1, 407.4):
                for available in (1, 0.5, 0.1):
                    for high_fraction in (0.65, 0):
                        albumin = grams * 1e6 / ALBUMIN_MASS_DA * available
                        free = unbound(total, albumin, high_fraction)
                        writer.writerow([grams, total, available, high_fraction, round(free, 4),
                                         round(100 * free / total, 4)])


if __name__ == '__main__':
    run(Path(sys.argv[1]), Path(sys.argv[2]))
