# Surface census — what can be read now, per paper

> **Generated file — do not edit by hand.** Regenerate with:
> ```bash
> python3 framework/scripts/surface_census.py --disease wwox \
>     --out disease-models/wwox/research/surface_census.md
> ```
>
> A companion to [[full_text_queue_current]], and deliberately **not** part of it: a paper's presence in the queue is a declaration of reading debt that `session_self_eval.py` counts, and a derived table naming every corpus PMID is not a declaration of anything.
>
> A photograph, not an invariant. `files/fulltext/` is gitignored and grows between sessions, so these numbers describe the corpus on the census date and nothing re-checks them afterwards — compare the listing digest below against your own copy before trusting a row. This page blocks nothing and has no threshold: it exists so that rule 5d's *"record the absence"* is a fact in the state instead of a rediscovery made three papers into a reading.

**Census date:** 2026-09-21  
**Corpus:** `fulltext` — 31 entries, 30 papers, listing digest `b238cfaf6177904f`  
**Sentinel:** `deepdive_manifest._refuse_suspect_surface`, PDF text via none

### Totals

| Surface | Papers | What it means |
|---|---:|---|
| `structured` | 0 | publisher XML/HTML present — read this one (rule 5d) |
| `pdf_only` | 30 | no structured surface locally — acquire XML/HTML before reading |
| `absent` | 117 | queued, nothing local at all — retrieve first |

Sentinel over the surface each paper would actually be read from — the structured file where one exists, the PDF otherwise. Structured markup is screened too, because a suffix is not a surface; see the note below:

| Verdict | Papers | What it means |
|---|---:|---|
| `SUSPECT` | 2 | the text carries a known corruption signature — do not quote it; adjudicate against the rendered page, or re-acquire the paper structured |
| `clean` | 28 | no known signature found — this is not a verification |
| `not_screened` | 0 | no deterministic extractor available, or extraction failed |

🔴 **2 of the 30 PDF-only papers cannot be read from their text layer at all**, and all of them should be acquired as XML/HTML rather than read from the PDF. A `clean` PDF is still a PDF: `deepdive_manifest` refuses it as a text surface, and a locator drawn from one has to be anchored to the page.

### Per paper

| Paper | Queue | Surface | Sentinel | Local surfaces |
|---|---|---|---|---|
| PMID 32000863 | FT-001 | `absent` | — | — |
| PMID 32581702 | FT-002 | `absent` | — | — |
| PMID 30853297 | FT-003 | `absent` | — | — |
| PMID 36779245 | FT-004, FT-029 | `absent` | — | — |
| PMID 31543760 | FT-005 | `pdf_only` | `clean` | PMID31543760_PMC_MCPtext.txt |
| PMID 26390919 | FT-006 | `absent` | — | — |
| PMID 30290271 | FT-008 | `absent` | — | — |
| PMID 42397075 | FT-010 | `absent` | — | — |
| PMID 38182577 | FT-011, FT-050 | `absent` | — | — |
| PMID 42082822 | FT-013 | `absent` | — | — |
| PMID 41984841 | FT-014 | `absent` | — | — |
| PMID 40198927 | FT-015 | `absent` | — | — |
| PMID 40263068 | FT-015 | `absent` | — | — |
| PMID 39952983 | FT-016 | `absent` | — | — |
| PMID 39933386 | FT-017 | `absent` | — | — |
| PMID 28123895 | FT-018 | `absent` | — | — |
| PMID 21444760 | FT-019 | `absent` | — | — |
| PMID 15664696 | FT-020 | `absent` | — | — |
| PMID 21075834 | FT-020 | `absent` | — | — |
| PMID 21115974 | FT-020 | `absent` | — | — |
| PMID 34214506 | FT-020 | `absent` | — | — |
| PMID 24308844 | FT-021, FT-055 | `absent` | — | — |
| PMID 20067585 | FT-022 | `absent` | — | — |
| PMID 22193544 | FT-022, FT-023, FT-024, FT-025 | `absent` | — | — |
| PMID 15026124 | FT-023 | `absent` | — | — |
| PMID 15126504 | FT-024 | `absent` | — | — |
| PMID 17178850 | FT-025 | `absent` | — | — |
| PMID 21212533 | FT-026 | `absent` | — | — |
| PMID 12065620 | FT-027 | `absent` | — | — |
| PMID 19607922 | FT-028 | `absent` | — | — |
| PMID 25716914 | FT-030 | `absent` | — | — |
| PMID 32051108 | FT-031 | `absent` | — | — |
| PMID 11719429 | FT-032 | `absent` | — | — |
| PMID 17360458 | FT-032, FT-064 | `absent` | — | — |
| PMID 26345274 | FT-032 | `absent` | — | — |
| PMID 30094525 | FT-032 | `absent` | — | — |
| PMID 35573960 | FT-032 | `pdf_only` | `clean` | PMID35573960_PMC_MCPtext.txt |
| PMID 40875931 | FT-035 | `absent` | — | — |
| PMID 10861292 | FT-036, FT-080 | `absent` | — | — |
| PMID 36499501 | FT-037 | `absent` | — | — |
| PMID 30619736 | FT-038 | `absent` | — | — |
| PMID 24871327 | FT-039, FT-046, FT-049 | `absent` | — | — |
| PMID 31340538 | FT-040 | `pdf_only` | `clean` | PMID31340538_PMC_MCPtext.txt |
| PMID 17803050 | FT-041 | `absent` | — | — |
| PMID 19500159 | FT-042 | `absent` | — | — |
| PMID 19936220 | FT-043 | `absent` | — | — |
| PMID 33914858 | FT-044 | `absent` | — | — |
| PMID 42128308 | FT-045 | `absent` | — | — |
| PMID 15070730 | FT-046, FT-064 | `absent` | — | — |
| PMID 18974271 | FT-046 | `absent` | — | — |
| PMID 17575124 | FT-047, FT-064 | `absent` | — | — |
| PMID 20530675 | FT-047, FT-072, FT-078 | `absent` | — | — |
| PMID 21318118 | FT-047 | `absent` | — | — |
| PMID 22634283 | FT-047 | `absent` | — | — |
| PMID 23254685 | FT-047 | `absent` | — | — |
| PMID 26256646 | FT-047 | `absent` | — | — |
| PMID 27308416 | FT-047 | `absent` | — | — |
| PMID 27308504 | FT-047 | `absent` | — | — |
| PMID 27550453 | FT-047 | `absent` | — | — |
| PMID 27551470 | FT-047 | `absent` | — | — |
| PMID 29724996 | FT-047 | `absent` | — | — |
| PMID 30082886 | FT-047 | `absent` | — | — |
| PMID 30370248 | FT-047 | `absent` | — | — |
| PMID 30755385 | FT-047, FT-048, FT-049 | `absent` | — | — |
| PMID 31428585 | FT-047 | `absent` | — | — |
| PMID 32300104 | FT-047 | `absent` | — | — |
| PMID 34634460 | FT-047, FT-058 | `absent` | — | — |
| PMID 34831305 | FT-047 | `absent` | — | — |
| PMID 42395553 | FT-047 | `absent` | — | — |
| PMID 42422765 | FT-047 | `absent` | — | — |
| PMID 34747138 | FT-049 | `absent` | — | — |
| PMID 38499540 | FT-051 | `absent` | — | — |
| PMID 25331887 | FT-052, FT-053 | `absent` | — | — |
| PMID 24550385 | FT-054, FT-060 | `absent` | — | — |
| PMID 34034642 | FT-056 | `absent` | — | — |
| PMID 17823927 | FT-057 | `absent` | — | — |
| PMID 25411445 | FT-057 | `absent` | — | — |
| PMID 29808465 | FT-057 | `absent` | — | — |
| PMID 30158849 | FT-057 | `absent` | — | — |
| PMID 30356099 | FT-057 | `absent` | — | — |
| PMID 34268881 | FT-059 | `absent` | — | — |
| PMID 23435430 | FT-061 | `absent` | — | — |
| PMID 23370280 | FT-062 | `absent` | — | — |
| PMID 12514174 | FT-063 | `absent` | — | — |
| PMID 16061658 | FT-063 | `absent` | — | — |
| PMID 39416860 | FT-065 | `absent` | — | — |
| PMID 26675548 | FT-067 | `absent` | — | — |
| PMID 18487609 | FT-068, FT-063 | `absent` | — | — |
| PMID 27869163 | FT-070 | `pdf_only` | `clean` | PMID27869163_PMC_MCPtext.txt |
| PMID 18674750 | FT-071 | `absent` | — | — |
| PMID 27845895 | FT-073 | `pdf_only` | `clean` | PMID27845895_PMC_MCPtext.txt |
| PMID 31966718 | FT-074 | `absent` | — | — |
| PMID 18931939 | FT-075 | `absent` | — | — |
| PMID 16223882 | FT-076, FT-088 | `absent` | — | — |
| PMID 21731849 | FT-077 | `absent` | — | — |
| PMID 16941225 | FT-079 | `absent` | — | — |
| PMID 18193043 | FT-081 | `absent` | — | — |
| PMID 17458891 | FT-082 | `absent` | — | — |
| PMID 36828035 | FT-083 | `absent` | — | — |
| PMID 30350478 | FT-084 | `absent` | — | — |
| PMID 27773744 | FT-085 | `absent` | — | — |
| PMID 15073846 | FT-086 | `absent` | — | — |
| PMID 12704432 | FT-087 | `absent` | — | — |
| PMID 25238781 | FT-089 | `absent` | — | — |
| PMID 25416187 | FT-090 | `absent` | — | — |
| PMID 25245215 | FT-091 | `absent` | — | — |
| PMID 25238782 | FT-092 | `pdf_only` | `clean` | PMID25238782_PMC_MCPtext.txt |
| PMID 20164920 | FT-093 | `absent` | — | — |
| PMID 18000379 | FT-094 | `absent` | — | — |
| PMID 25216703 | FT-095 | `absent` | — | — |
| PMID 25231336 | FT-095 | `absent` | — | — |
| PMID 25238783 | FT-095 | `absent` | — | — |
| PMID 25248392 | FT-095 | `absent` | — | — |
| PMID 25283145 | FT-095 | `absent` | — | — |
| PMID 25297918 | FT-095 | `absent` | — | — |
| PMID 25300511 | FT-095 | `absent` | — | — |
| PMID 20146584 | FT-096 | `absent` | — | — |
| PMID 41390778 | FT-097 | `pdf_only` | `clean` | PMID41390778_PMC_MCPtext.txt |
| PMID 33134515 | FT-098 | `pdf_only` | `clean` | PMID33134515_PMC_MCPtext.txt |
| PMID 21766012 | FT-099 | `pdf_only` | `clean` | PMID21766012_PMC_MCPtext.txt |
| PMID 32020597 | FT-100 | `absent` | — | — |
| PMID 9918798 | FT-101 | `absent` | — | — |
| PMID 25650666 | FT-102 | `pdf_only` | `clean` | PMID25650666_PMC_MCPtext.txt |
| PMID 27569545 | FT-103, FT-105 | `absent` | — | — |
| PMID 29067327 | FT-104 | `pdf_only` | `clean` | PMID29067327_PMC_MCPtext.txt |
| PMID 42092735 | FT-106 | `pdf_only` | `clean` | PMID42092735_PMC_MCPtext.txt |
| PMID 41153369 | FT-107 | `pdf_only` | `clean` | PMID41153369_PMC_MCPtext.txt |
| PMID 19484134 | FT-108 | `pdf_only` | `clean` | PMID19484134_PMC_MCPtext.txt |
| PMID 18371080 | FT-109 | `absent` | — | — |
| PMID 38902482 | FT-110 | `absent` | — | — |
| PMID 42721537 | FT-110 | `absent` | — | — |
| PMID 35328751 | FT-111 | `pdf_only` | `clean` | PMID35328751_PMC_MCPtext.txt |
| PMID 24008736 | — | `pdf_only` | `clean` | PMID24008736_PMC_MCPtext.txt |
| PMID 24932569 | — | `pdf_only` | `clean` | PMID24932569_PMC_MCPtext.txt |
| PMID 25649963 | — | `pdf_only` | `clean` | PMID25649963_PMC_MCPtext.txt |
| PMID 26355344 | — | `pdf_only` | `clean` | PMID26355344_PMC_MCPtext.txt |
| PMID 27551439 | — | `pdf_only` | `clean` | PMID27551439_PMC_MCPtext.txt |
| PMID 31752354 | — | `pdf_only` | `clean` | PMID31752354_PMC_MCPtext.txt |
| PMID 32764489 | — | `pdf_only` | `clean` | PMID32764489_PMC_MCPtext.txt |
| PMID 34140629 | — | `pdf_only` | `clean` | PMID34140629_PMC_MCPtext.txt |
| PMID 34359949 | — | `pdf_only` | `clean` | PMID34359949_PMC_MCPtext.txt |
| PMID 35984507 | — | `pdf_only` | `SUSPECT` — PMID35984507_OPERATOR_PDFtext.txt: contains the C0 control U+001F | PMID35984507_OPERATOR_PDFtext.txt, PMID35984507_SUPP_PDFtext.txt |
| PMID 36271927 | — | `pdf_only` | `SUSPECT` — uses statistical language (16 mentions) and contains none of < > ≤ ≥ ± × − | PMID36271927_PMC_MCPtext.txt |
| PMID 36498839 | — | `pdf_only` | `clean` | PMID36498839_PMC_MCPtext.txt |
| PMID 39101447 | — | `pdf_only` | `clean` | PMID39101447_PMC_MCPtext.txt |
| PMID 41124647 | — | `pdf_only` | `clean` | PMID41124647_PMC_MCPtext.txt |
| PMID 41677633 | — | `pdf_only` | `clean` | PMID41677633_PMC_MCPtext.txt |

### Loss ledger — queue entries this census cannot join to a local surface

Not all of these are defects. An entry resolved by DOI alone says exactly what it is; the corpus is simply keyed by PMID, so there is nothing local to join it to. An entry declaring `NOT_AN_ARTICLE` will never have an identifier. Both are declared rather than dropped, because an entry missing from a derived surface and an entry with nothing to say look identical unless the difference is written down.

| Entry | State | Identity line, verbatim |
|---|---|---|
| FT-007 | `doi_only` | DOI 10.1101/2025.11.22.689900 — bioRxiv preprint, 2025-11-22 (Aqeilan lab; emerso dalla review Obeid 2026, [[paper_registry_current#PAPER 029]]) |
| FT-009 | `doi_only` | DOI 10.1101/2025.05.01.651195 — Lucas-Clarke HJ et al., bioRxiv preprint, 2025-05-01 |
| FT-012 | `not_an_article` | NOT_AN_ARTICLE — comunicato stampa istituzionale, nessun PMID e nessun DOI **per costruzione**, non per debito. L'identificatore comparirà con il report peer-reviewed, ed è quello che questa voce sorveglia. |
| FT-033 | `doi_only` | DOI 10.1093/brain/awm078 — Gribaa M et al. 2007, *Brain* 130(7):1921–1928 |
| FT-034 | `doi_only` | DOI 10.1165/rcmb.2020-0145OC · DOI 10.7759/cureus.46216 · DOI 10.1002/ana.25619 · |
| FT-066 | `doi_only` | DOI 10.1038/onc.2013.52 — Santini S *et al.*, *Oncogene* 2014;33(9):1113–1123 — |
| FT-069 | `not_an_article` | `NOT_AN_ARTICLE` — un contratto, non un paper: `framework/scripts/deepdive_manifest.py` su `main`, |

**Accounting.** Rows: 30 corpus papers + 132 queued papers − 15 in both = **147** emitted. ✓ Entries: 104 resolved + 7 unjoined = **111** queue entries. ✓

*Not medical advice. This page describes file formats, not findings.*

