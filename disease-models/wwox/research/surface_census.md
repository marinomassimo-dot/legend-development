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

**Census date:** 2026-08-15  
**Corpus:** `fulltext` — 174 entries, 87 papers, listing digest `825fc4a9d8415b0e`  
**Sentinel:** `deepdive_manifest._refuse_suspect_surface`, PDF text via PyMuPDF 1.26.5

### Totals

| Surface | Papers | What it means |
|---|---:|---|
| `structured` | 67 | publisher XML/HTML present — read this one (rule 5d) |
| `pdf_only` | 20 | no structured surface locally — acquire XML/HTML before reading |
| `absent` | 29 | queued, nothing local at all — retrieve first |

Sentinel over the surface each paper would actually be read from — the structured file where one exists, the PDF otherwise. Structured markup is screened too, because a suffix is not a surface; see the note below:

| Verdict | Papers | What it means |
|---|---:|---|
| `SUSPECT` | 15 | the text carries a known corruption signature — do not quote it; adjudicate against the rendered page, or re-acquire the paper structured |
| `clean` | 72 | no known signature found — this is not a verification |
| `not_screened` | 0 | no deterministic extractor available, or extraction failed |

🔴 **15 of the 20 PDF-only papers cannot be read from their text layer at all**, and all of them should be acquired as XML/HTML rather than read from the PDF. A `clean` PDF is still a PDF: `deepdive_manifest` refuses it as a text surface, and a locator drawn from one has to be anchored to the page.

🔴 **Marked `text dump` below: markup wrapping a PDF text layer, not publisher markup.** These files carry an `.xml`/`.html` suffix and no JATS metadata, and their body sits inside a `<pre>` block. They are counted as PDF-only, because that is what they are — a suffix is not a surface. Files: `PMID17803050_Suzuki2007.html`, `PMID19500159_Suzuki2009.html`.

### Per paper

| Paper | Queue | Surface | Sentinel | Local surfaces |
|---|---|---|---|---|
| PMID 32000863 | FT-001 | `structured` | `clean` | PMID32000863_Cheng2020_PMC.xml, PMID32000863_Cheng2020_supplementary.pdf |
| PMID 32581702 | FT-002 | `structured` | `clean` | PMID32581702_Repudi2020_PMC.xml |
| PMID 30853297 | FT-003 | `absent` | — | — |
| PMID 36779245 | FT-004, FT-029 | `structured` | `clean` | PMID36779245_Oliver2023_PMC.xml |
| PMID 31543760 | FT-005 | `structured` | `clean` | PMID31543760_Kosla2019_EPMC.xml |
| PMID 26390919 | FT-006 | `absent` | — | — |
| PMID 30290271 | FT-008 | `structured` | `clean` | PMID30290271_Hussain2019.html, PMID30290271_Hussain2019.pdf |
| PMID 42397075 | FT-010 | `pdf_only` | `clean` | PMID42397075_Aqeilan2026.pdf, PMID42397075_Aqeilan2026_fitz.txt |
| PMID 38182577 | FT-011, FT-050 | `structured` | `clean` | PMID38182577_Akkawi2024.pdf, PMID38182577_Akkawi2024_PMC.xml |
| PMID 42082822 | FT-013 | `structured` | `clean` | PMID42082822_Denkboy2026_EPMC.xml |
| PMID 41984841 | FT-014 | `structured` | `clean` | PMID41984841_BidanyMizrahi2026.pdf, PMID41984841_BidanyMizrahi2026_PMC.xml |
| PMID 40198927 | FT-015 | `absent` | — | — |
| PMID 40263068 | FT-015 | `absent` | — | — |
| PMID 39952983 | FT-016 | `structured` | `clean` | PMID39952983_Kim2025_EPMC.xml |
| PMID 39933386 | FT-017 | `absent` | — | — |
| PMID 28123895 | FT-018 | `absent` | — | — |
| PMID 21444760 | FT-019 | `absent` | — | — |
| PMID 15664696 | FT-020 | `absent` | — | — |
| PMID 21075834 | FT-020 | `structured` | `clean` | PMID21075834_OKeefe2011_EPMC.xml |
| PMID 21115974 | FT-020 | `structured` | `clean` | PMID21115974_Fu2011.pdf, PMID21115974_Fu2011_PMC.html |
| PMID 34214506 | FT-020 | `pdf_only` | `SUSPECT` — contains the C0 control U+0002 | PMID34214506_Saadane2021.pdf |
| PMID 24308844 | FT-021, FT-055 | `structured` | `clean` | PMID24308844_Schuchardt2013_PMC.xml |
| PMID 20067585 | FT-022 | `absent` | — | — |
| PMID 22193544 | FT-022, FT-023, FT-024, FT-025 | `structured` | `clean` | PMID22193544_Wang2012.pdf, PMID22193544_Wang2012_PMC_JATS.xml |
| PMID 15026124 | FT-023 | `absent` | — | — |
| PMID 15126504 | FT-024 | `absent` | — | — |
| PMID 17178850 | FT-025 | `pdf_only` | `clean` | PMID17178850_Aqeilan2006.pdf |
| PMID 21212533 | FT-026 | `pdf_only` | `SUSPECT` — contains the C0 control U+0002 | PMID21212533_Saeki2011.pdf |
| PMID 12065620 | FT-027 | `absent` | — | — |
| PMID 19607922 | FT-028 | `absent` | — | — |
| PMID 25716914 | FT-030 | `absent` | — | — |
| PMID 32051108 | FT-031 | `absent` | — | — |
| PMID 11719429 | FT-032 | `absent` | — | — |
| PMID 17360458 | FT-032, FT-064 | `structured` | `clean` | PMID17360458_Aqeilan2007.pdf, PMID17360458_Aqeilan2007_PMC.html |
| PMID 26345274 | FT-032 | `absent` | — | — |
| PMID 30094525 | FT-032 | `absent` | — | — |
| PMID 35573960 | FT-032 | `absent` | — | — |
| PMID 40875931 | FT-035 | `absent` | — | — |
| PMID 10861292 | FT-036 | `absent` | — | — |
| PMID 36499501 | FT-037 | `absent` | — | — |
| PMID 30619736 | FT-038 | `absent` | — | — |
| PMID 24871327 | FT-039, FT-046, FT-049 | `structured` | `clean` | PMID24871327_Iatan2014_PMC.html |
| PMID 31340538 | FT-040 | `structured` | `clean` | PMID31340538_Tochigi2019.xml |
| PMID 17803050 | FT-041 | `pdf_only` | `SUSPECT` — PMID17803050_Suzuki2007.html: contains the C0 control U+000C | PMID17803050_Suzuki2007.html *(text dump)*, PMID17803050_Suzuki2007.pdf |
| PMID 19500159 | FT-042 | `pdf_only` | `clean` | PMID19500159_Suzuki2009.html *(text dump)*, PMID19500159_Suzuki2009.pdf |
| PMID 19936220 | FT-043 | `structured` | `clean` | PMID19936220_Ludes-Meyers2009.pdf, PMID19936220_Ludes-Meyers2009_PMC.xml |
| PMID 33914858 | FT-044 | `pdf_only` | `SUSPECT` — contains the C0 control U+0002 | PMID33914858_Aqeilan2021.pdf |
| PMID 42128308 | FT-045 | `pdf_only` | `clean` | PMID42128308_Aqeilan2026.pdf, PMID42128308_Aqeilan2026_fitz.txt |
| PMID 15070730 | FT-046, FT-064 | `structured` | `clean` | PMID15070730_Aqeilan2004.pdf, PMID15070730_Aqeilan2004_PMC.html |
| PMID 18974271 | FT-046 | `structured` | `clean` | PMID18974271_Aqeilan2009.pdf, PMID18974271_Aqeilan2009_PMC.html |
| PMID 17575124 | FT-047, FT-064 | `structured` | `clean` | PMID17575124_Aqeilan2007_PMC.html |
| PMID 20530675 | FT-047, FT-072 | `structured` | `clean` | PMID20530675_Kurek2010_PMC.html |
| PMID 21318118 | FT-047 | `structured` | `clean` | PMID21318118_Drusco2011_PMC.xml |
| PMID 22634283 | FT-047 | `structured` | `clean` | PMID22634283_McDonald2012_PMC.html |
| PMID 23254685 | FT-047 | `structured` | `clean` | PMID23254685_Abdeen2013_PMC.html |
| PMID 26256646 | FT-047 | `structured` | `clean` | PMID26256646_DelMare2015_PMC.xml |
| PMID 27308416 | FT-047 | `structured` | `clean` | PMID27308416_AbuRemaileh2015_PMC.xml |
| PMID 27308504 | FT-047 | `structured` | `clean` | PMID27308504_Hazan2015.pdf, PMID27308504_Hazan2015_PMC.xml |
| PMID 27550453 | FT-047 | `structured` | `clean` | PMID27550453_DelMare2016_PMC.html |
| PMID 27551470 | FT-047 | `structured` | `clean` | PMID27551470_Hazan2015_PMC.xml |
| PMID 29724996 | FT-047 | `structured` | `clean` | PMID29724996_AbuRemaileh2018_PMC.xml, PMID29724996_AbuRemaileh2018_supplement.pdf |
| PMID 30082886 | FT-047 | `structured` | `clean` | PMID30082886_Abdeen2018_PMC.xml |
| PMID 30370248 | FT-047 | `structured` | `clean` | PMID30370248_Tanna2018_PMC.xml |
| PMID 30755385 | FT-047, FT-048, FT-049 | `structured` | `clean` | PMID30755385_AbuRemaileh2019.pdf, PMID30755385_AbuRemaileh2019_PMC.xml |
| PMID 31428585 | FT-047 | `structured` | `clean` | PMID31428585_Chang2019_PMC.xml |
| PMID 32300104 | FT-047 | `structured` | `clean` | PMID32300104_Khawaled2020_PMC.xml |
| PMID 34634460 | FT-047, FT-058 | `structured` | `clean` | PMID34634460_Breton2021_PMC.xml |
| PMID 34831305 | FT-047 | `structured` | `clean` | PMID34831305_Steinberg2021_PMC.xml |
| PMID 42395553 | FT-047 | `structured` | `clean` | PMID42395553_PMC.xml |
| PMID 42422765 | FT-047 | `structured` | `clean` | PMID42422765_Obeid2026_PMC.html |
| PMID 34747138 | FT-049 | `structured` | `clean` | PMID34747138_Repudi2021_PMC.xml |
| PMID 38499540 | FT-051 | `structured` | `clean` | PMID38499540_BidanyMizrahi2024.pdf, PMID38499540_BidanyMizrahi2024_PMC.xml |
| PMID 25331887 | FT-052, FT-053 | `structured` | `clean` | PMID25331887_AbuOdeh2014.pdf, PMID25331887_AbuOdeh2014_PMC.html |
| PMID 24550385 | FT-054, FT-060 | `structured` | `clean` | PMID24550385_AbuOdeh2014.pdf, PMID24550385_AbuOdeh2014_PMC.html |
| PMID 34034642 | FT-056 | `absent` | — | — |
| PMID 17823927 | FT-057 | `absent` | — | — |
| PMID 25411445 | FT-057 | `absent` | — | — |
| PMID 29808465 | FT-057 | `absent` | — | — |
| PMID 30158849 | FT-057 | `structured` | `clean` | PMID30158849_Liu2018_EPMC.xml |
| PMID 30356099 | FT-057 | `structured` | `clean` | PMID30356099_Piard2019_EPMC.xml |
| PMID 34268881 | FT-059 | `structured` | `clean` | PMID34268881_Steinberg2021.pdf, PMID34268881_Steinberg2021_PMC.xml |
| PMID 23435430 | FT-061 | `structured` | `clean` | PMID23435430_Santini2014.pdf, PMID23435430_Santini2014_EPMC.xml |
| PMID 23370280 | FT-062 | `structured` | `clean` | PMID23370280_Salah2013.pdf, PMID23370280_Salah2013_PMC.xml |
| PMID 12514174 | FT-063 | `absent` | — | — |
| PMID 16061658 | FT-063 | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID16061658_Aqeilan2005.pdf |
| PMID 39416860 | FT-065 | `structured` | `clean` | PMID39416860_Feng2024_PMC.xml |
| PMID 26675548 | FT-067 | `structured` | `clean` | PMID26675548_AbuOdeh2016.pdf, PMID26675548_AbuOdeh2016_PMC.xml |
| PMID 18487609 | FT-068, FT-063 | `structured` | `clean` | PMID18487609_Aqeilan2008.pdf, PMID18487609_Aqeilan2008_PMC.html |
| PMID 27869163 | FT-070 | `absent` | — | — |
| PMID 18674750 | FT-071 | `structured` | `clean` | PMID18674750_Lee2008.pdf, PMID18674750_Lee2008_PMC.html |
| PMID 15073125 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID15073125_Aqeilan2004.pdf |
| PMID 15131042 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID15131042_Aqeilan2004.pdf |
| PMID 15548692 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID15548692_Aqeilan2004.pdf |
| PMID 16223882 | — | `structured` | `clean` | PMID16223882_Fabbri2005.pdf, PMID16223882_Fabbri2005_PMC.html |
| PMID 17289881 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID17289881_Aqeilan2007.pdf |
| PMID 17458891 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID17458891_Aqeilan2007.pdf |
| PMID 17909041 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID17909041_Aqeilan2007.pdf |
| PMID 18460020 | — | `structured` | `clean` | PMID18460020_Nakayama2008.pdf, PMID18460020_Nakayama2008_PMC.html |
| PMID 21731849 | — | `structured` | `clean` | PMID21731849_DelMare2011.pdf, PMID21731849_DelMare2011_PMC.html |
| PMID 24510053 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0002 | PMID24510053_Aqeilan2014.pdf |
| PMID 25012504 | — | `structured` | `clean` | PMID25012504_AbuRemaileh2014.pdf, PMID25012504_AbuRemaileh2014_PMC.html |
| PMID 25238781 | — | `structured` | `clean` | PMID25238781_Aqeilan2014.pdf, PMID25238781_Aqeilan2014_PMC.html |
| PMID 25245215 | — | `structured` | `clean` | PMID25245215_Aqeilan2014.pdf, PMID25245215_Aqeilan2014_PMC.html |
| PMID 25491415 | — | `structured` | `clean` | PMID25491415_AbuRemaileh2015.pdf, PMID25491415_AbuRemaileh2015_PMC.html |
| PMID 26499798 | — | `structured` | `clean` | PMID26499798_AbuRemaileh2015.pdf, PMID26499798_AbuRemaileh2015_PMC.html |
| PMID 30470736 | — | `structured` | `clean` | PMID30470736_AbuRemaileh2018.pdf, PMID30470736_AbuRemaileh2018_PMC.xml |
| PMID 30622118 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID30622118_Aqeilan2019.pdf |
| PMID 31075076 | — | `structured` | `clean` | PMID31075076_Abdeen2019.pdf, PMID31075076_Abdeen2019_PMC.html |
| PMID 33255508 | — | `structured` | `clean` | PMID33255508_Aldaz2020.xml |
| PMID 33916893 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID33916893_Banne2021.pdf |
| PMID 35716775 | — | `pdf_only` | `SUSPECT` — PMID35716775_Rotem-Bamberger2022.pdf: contains the C0 control U+0001 | PMID35716775_Rotem-Bamberger2022.pdf, PMID35716775_Rotem-Bamberger2022_supplement.pdf |
| PMID 36572673 | — | `structured` | `clean` | PMID36572673_Husanie2022.pdf, PMID36572673_Husanie2022_PMC.xml |
| PMID 37519886 | — | `structured` | `clean` | PMID37519886_PMC.xml |
| PMID 38355659 | — | `structured` | `clean` | PMID38355659_Akkawi2024.pdf, PMID38355659_Akkawi2024_PMC.xml |
| PMID 39507621 | — | `structured` | `clean` | PMID39507621_Teplyshova2024_PMC.xml |
| PMID 41562193 | — | `pdf_only` | `clean` | PMID41562193_Druck2026.pdf |

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

**Accounting.** Rows: 87 corpus papers + 90 queued papers − 61 in both = **116** emitted. ✓ Entries: 65 resolved + 7 unjoined = **72** queue entries. ✓

*Not medical advice. This page describes file formats, not findings.*

