"""Find folate and CSF co-mentions in held, WWOX-titled JATS full texts."""
import csv
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

TITLE = re.compile(r'\b(wwox|woree|scar12|wo[xX]1)\b|WW domain.containing oxidoreductase', re.I)
FOLATE = re.compile(r'folate|folic acid|folinic|leucovorin|5[ -]?MTHF|methyltetrahydrofol', re.I)
CSF = re.compile(r'cerebrospinal|\bCSF\b', re.I)


def extract(files, output):
    results = {}
    seen = 0
    for path in sorted((files / 'fulltext').glob('*.xml')):
        seen += 1
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError:
            continue
        for article in [root] if root.tag == 'article' else root.findall('.//article'):
            meta = article.find('front/article-meta')
            if meta is None:
                continue
            title = meta.find('title-group/article-title')
            if title is None or not TITLE.search(''.join(title.itertext())):
                continue
            pmid = meta.findtext("article-id[@pub-id-type='pmid']")
            if not pmid or article.find('body') is None:
                continue
            flags = results.setdefault(pmid, [False, False, False])
            for para in article.findall('./body//p'):
                text = ' '.join(''.join(para.itertext()).split())
                f, c = bool(FOLATE.search(text)), bool(CSF.search(text))
                flags[0] |= f
                flags[1] |= c
                flags[2] |= f and c
    with output.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['pmid', 'folate_term', 'csf_term', 'same_paragraph'])
        for pmid, flags in sorted(results.items()):
            writer.writerow([pmid, *map(int, flags)])
    print('XML files scanned', seen, 'unique titled body records', len(results),
          'with both terms in one paragraph', sum(v[2] for v in results.values()))


if __name__ == '__main__':
    extract(Path(sys.argv[1]), Path(sys.argv[2]))
