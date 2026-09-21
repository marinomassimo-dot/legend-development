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
**Corpus:** `fulltext` — 16 entries, 9 papers, listing digest `69d3415592cb982b`  
**Sentinel:** `deepdive_manifest._refuse_suspect_surface`, PDF text via PyMuPDF 1.28.2

### Totals

| Surface | Papers | What it means |
|---|---:|---|
| `structured` | 0 | publisher XML/HTML present — read this one (rule 5d) |
| `pdf_only` | 9 | no structured surface locally — acquire XML/HTML before reading |
| `absent` | 148 | queued, nothing local at all — retrieve first |

Sentinel over the surface each paper would actually be read from — the structured file where one exists, the PDF otherwise. Structured markup is screened too, because a suffix is not a surface; see the note below:

| Verdict | Papers | What it means |
|---|---:|---|
| `SUSPECT` | 2 | the text carries a known corruption signature — do not quote it; adjudicate against the rendered page, or re-acquire the paper structured |
| `clean` | 7 | no known signature found — this is not a verification |
| `not_screened` | 0 | no deterministic extractor available, or extraction failed |

🔴 **2 of the 9 PDF-only papers cannot be read from their text layer at all**, and all of them should be acquired as XML/HTML rather than read from the PDF. A `clean` PDF is still a PDF: `deepdive_manifest` refuses it as a text surface, and a locator drawn from one has to be anchored to the page.

### Per paper

| Paper | Queue | Surface | Sentinel | Local surfaces |
|---|---|---|---|---|
| PMID 32000863 | FT-001 | `absent` | — | — |
| PMID 32581702 | FT-002 | `absent` | — | — |
| PMID 30853297 | FT-003 | `absent` | — | — |
| PMID 36779245 | FT-004, FT-029 | `absent` | — | — |
| PMID 31543760 | FT-005 | `absent` | — | — |
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
| PMID 35573960 | FT-032 | `absent` | — | — |
| PMID 40875931 | FT-035 | `absent` | — | — |
| PMID 10861292 | FT-036, FT-080 | `absent` | — | — |
| PMID 36499501 | FT-037 | `absent` | — | — |
| PMID 30619736 | FT-038 | `absent` | — | — |
| PMID 24871327 | FT-039, FT-046, FT-049 | `absent` | — | — |
| PMID 31340538 | FT-040 | `absent` | — | — |
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
| PMID 30356099 | FT-057 | `pdf_only` | `clean` | PMID30356099_PMC_MCPtext.txt |
| PMID 34268881 | FT-059 | `absent` | — | — |
| PMID 23435430 | FT-061 | `absent` | — | — |
| PMID 23370280 | FT-062 | `absent` | — | — |
| PMID 12514174 | FT-063 | `absent` | — | — |
| PMID 16061658 | FT-063 | `absent` | — | — |
| PMID 39416860 | FT-065 | `absent` | — | — |
| PMID 26675548 | FT-067 | `absent` | — | — |
| PMID 18487609 | FT-068, FT-063 | `absent` | — | — |
| PMID 27869163 | FT-070 | `absent` | — | — |
| PMID 18674750 | FT-071 | `absent` | — | — |
| PMID 27845895 | FT-073 | `absent` | — | — |
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
| PMID 25238782 | FT-092 | `absent` | — | — |
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
| PMID 41390778 | FT-097 | `absent` | — | — |
| PMID 33134515 | FT-098 | `absent` | — | — |
| PMID 21766012 | FT-099 | `absent` | — | — |
| PMID 32020597 | FT-100 | `absent` | — | — |
| PMID 9918798 | FT-101 | `absent` | — | — |
| PMID 25650666 | FT-102 | `absent` | — | — |
| PMID 27569545 | FT-103, FT-105 | `absent` | — | — |
| PMID 29067327 | FT-104 | `absent` | — | — |
| PMID 42092735 | FT-106 | `absent` | — | — |
| PMID 41153369 | FT-107 | `absent` | — | — |
| PMID 19484134 | FT-108 | `absent` | — | — |
| PMID 18371080 | FT-109 | `absent` | — | — |
| PMID 38902482 | FT-110 | `absent` | — | — |
| PMID 42721537 | FT-110 | `absent` | — | — |
| PMID 35328751 | FT-111 | `absent` | — | — |
| PMID 42464650 | FT-112 | `absent` | — | — |
| PMID 28763065 | FT-113 | `absent` | — | — |
| PMID 35712340 | FT-113 | `pdf_only` | `clean` | PMID35712340_PMC_MCPabstract.txt, PMID35712340_PMC_MCPtext.txt |
| PMID 37974179 | FT-113 | `pdf_only` | `clean` | PMID37974179_PMC_MCPabstract.txt, PMID37974179_PMC_MCPtext.txt |
| PMID 41378749 | FT-113 | `absent` | — | — |
| PMID 42589397 | FT-113 | `pdf_only` | `clean` | PMID42589397_PMC_MCPabstract.txt, PMID42589397_PMC_MCPtext.txt |
| PMID 26302329 | FT-114 | `absent` | — | — |
| PMID 32389029 | FT-114 | `absent` | — | — |
| PMID 33520443 | FT-114 | `absent` | — | — |
| PMID 34210081 | FT-114 | `absent` | — | — |
| PMID 29785012 | FT-115 | `absent` | — | — |
| PMID 34314704 | FT-115 | `absent` | — | — |
| PMID 39319420 | FT-115 | `absent` | — | — |
| PMID 40463067 | FT-115 | `pdf_only` | `clean` | PMID40463067_PMC_MCPabstract.txt, PMID40463067_PMC_MCPtext.txt |
| PMID 42425971 | FT-115 | `pdf_only` | `SUSPECT` — PMID42425971_PMC_MCPabstract.txt: uses statistical language (6 mentions) and contains none of < > ≤ ≥ ± × − | PMID42425971_PMC_MCPabstract.txt, PMID42425971_PMC_MCPtext.txt |
| PMID 31618474 | FT-116 | `absent` | — | — |
| PMID 32214227 | FT-116 | `absent` | — | — |
| PMID 35715422 | FT-116 | `absent` | — | — |
| PMID 37095367 | FT-116 | `absent` | — | — |
| PMID 37583270 | FT-116 | `absent` | — | — |
| PMID 42523332 | FT-117 | `pdf_only` | `clean` | PMID42523332_PMC_MCPabstract.txt, PMID42523332_PMC_MCPtext.txt |
| PMID 11058590 | FT-118 | `absent` | — | — |
| PMID 28416821 | FT-120 | `absent` | — | — |
| PMID 33565365 | — | `pdf_only` | `SUSPECT` — PMID33565365_PMC_MCPtext.txt: the artifact's own decoded text was zero-length; a screen over no bytes establishes nothing | PMID33565365_PMC_MCPtext.txt, PMID33565365_abstract_PubMedMCP.txt |
| PMID 41228229 | — | `pdf_only` | `clean` | PMID41228229_PMC_MCPtext.txt |

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
| FT-119 | `not_an_article` | `NOT_AN_ARTICLE` — non esiste un articolo da accodare, e **questo è esattamente il punto**: la fonte è *"(Aldaz laboratory unpublished observations)"*, una parentetica dentro `PMID 24932569`. Il paper leggibile della catena è quella review, già letta di prima mano. |

**Accounting.** Rows: 9 corpus papers + 155 queued papers − 7 in both = **157** emitted. ✓ Entries: 112 resolved + 8 unjoined = **120** queue entries. ✓

*Not medical advice. This page describes file formats, not findings.*

