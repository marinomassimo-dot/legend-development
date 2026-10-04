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

**Census date:** 2026-10-04  
**Corpus:** `fulltext` — 463 entries, 227 papers, listing digest `ef9a7a4ab52ef01e`  
**Sentinel:** `deepdive_manifest._refuse_suspect_surface`, PDF text via PyMuPDF 1.28.2

### Totals

| Surface | Papers | What it means |
|---|---:|---|
| `structured` | 207 | publisher XML/HTML present — read this one (rule 5d) |
| `pdf_only` | 19 | no structured surface locally — acquire XML/HTML before reading |
| `absent` | 192 | queued, nothing local at all — retrieve first |

Sentinel over the surface each paper would actually be read from — the structured file where one exists, the PDF otherwise. Structured markup is screened too, because a suffix is not a surface; see the note below:

| Verdict | Papers | What it means |
|---|---:|---|
| `SUSPECT` | 8 | the text carries a known corruption signature — do not quote it; adjudicate against the rendered page, or re-acquire the paper structured |
| `clean` | 218 | no known signature found — this is not a verification |
| `not_screened` | 0 | no deterministic extractor available, or extraction failed |

🔴 **7 of the 19 PDF-only papers cannot be read from their text layer at all**, and all of them should be acquired as XML/HTML rather than read from the PDF. A `clean` PDF is still a PDF: `deepdive_manifest` refuses it as a text surface, and a locator drawn from one has to be anchored to the page.

### Per paper

| Paper | Queue | Surface | Sentinel | Local surfaces |
|---|---|---|---|---|
| PMID 32000863 | FT-001 | `structured` | `clean` | PMID32000863_Cheng2020_PMC.xml, PMID32000863_Cheng2020_supplementary.pdf |
| PMID 32581702 | FT-002 | `absent` | — | — |
| PMID 30853297 | FT-003, FT-117 | `pdf_only` | `SUSPECT` — PMID30853297_WeiszHubshman2019.pdf: contains the C0 control U+0001 | PMID30853297_WeiszHubshman2019.pdf, PMID30853297_WeiszHubshman2019_fitz.txt |
| PMID 36779245 | FT-004, FT-029, FT-122 | `structured` | `clean` | PMID36779245_Oliver2023_PMC_2026-09-27.xml |
| PMID 31543760 | FT-005 | `structured` | `clean` | PMID31543760_Kosla2019_EPMC.xml, PMID31543760_Kosla2019_PMC.xml |
| PMID 26390919 | FT-006 | `absent` | — | — |
| PMID 30290271 | FT-008 | `absent` | — | — |
| PMID 42397075 | FT-010 | `pdf_only` | `clean` | PMID42397075_Steinberg2026_OUP-AM.pdf, PMID42397075_Steinberg2026_OUP-AM_fitz.txt, PMID42397075_Steinberg2026_OUP-AM_layout.txt |
| PMID 38182577 | FT-011, FT-050 | `absent` | — | — |
| PMID 42082822 | FT-013 | `absent` | — | — |
| PMID 41984841 | FT-014 | `absent` | — | — |
| PMID 40198927 | FT-015 | `absent` | — | — |
| PMID 40263068 | FT-015 | `absent` | — | — |
| PMID 39952983 | FT-016 | `structured` | `clean` | PMID39952983_Kim2025_EPMC.xml, PMID39952983_Kim2025_PMC.xml |
| PMID 39933386 | FT-017 | `absent` | — | — |
| PMID 28123895 | FT-018 | `absent` | — | — |
| PMID 21444760 | FT-019 | `absent` | — | — |
| PMID 15664696 | FT-020 | `absent` | — | — |
| PMID 21075834 | FT-020 | `absent` | — | — |
| PMID 21115974 | FT-020 | `structured` | `clean` | PMID21115974_Fu2011_PMC.html, PMID21115974_Fu2011_supplement.pdf, PMID21115974_Fu2011_supplement.txt |
| PMID 34214506 | FT-020 | `absent` | — | — |
| PMID 24308844 | FT-021, FT-055 | `structured` | `clean` | PMID24308844_Schuchardt2013_PMC.xml, PMID24308844_Schuchardt2013_PMC_2026-09-27.xml |
| PMID 20067585 | FT-022 | `absent` | — | — |
| PMID 22193544 | FT-022, FT-023, FT-024, FT-025 | `structured` | `clean` | PMID22193544_Wang2012_PMC.xml |
| PMID 15026124 | FT-023 | `absent` | — | — |
| PMID 15126504 | FT-024 | `absent` | — | — |
| PMID 17178850 | FT-025, FT-183 | `absent` | — | — |
| PMID 21212533 | FT-026 | `absent` | — | — |
| PMID 12065620 | FT-027 | `absent` | — | — |
| PMID 19607922 | FT-028 | `absent` | — | — |
| PMID 25716914 | FT-030 | `absent` | — | — |
| PMID 32051108 | FT-031 | `absent` | — | — |
| PMID 11719429 | FT-032 | `absent` | — | — |
| PMID 17360458 | FT-032, FT-064 | `absent` | — | — |
| PMID 26345274 | FT-032 | `absent` | — | — |
| PMID 30094525 | FT-032 | `absent` | — | — |
| PMID 35573960 | FT-032 | `structured` | `clean` | PMID35573960_Riva2022_PMC.xml |
| PMID 40875931 | FT-035 | `absent` | — | — |
| PMID 10861292 | FT-036, FT-080 | `absent` | — | — |
| PMID 36499501 | FT-037 | `absent` | — | — |
| PMID 30619736 | FT-038 | `structured` | `clean` | PMID30619736_Hussain2018_EPMC_render.pdf, PMID30619736_Hussain2018_EuropePMC.xml, PMID30619736_Hussain2018_efetch.xml, PMID30619736_Hussain2018_frontiers.pdf |
| PMID 24871327 | FT-039, FT-046, FT-049 | `absent` | — | — |
| PMID 31340538 | FT-040 | `absent` | — | — |
| PMID 17803050 | FT-041 | `absent` | — | — |
| PMID 19500159 | FT-042 | `absent` | — | — |
| PMID 19936220 | FT-043 | `absent` | — | — |
| PMID 33914858 | FT-044 | `pdf_only` | `SUSPECT` — PMID33914858_Repudi2021_Brain_operator_supplied.pdf: contains the C0 control U+0002 | PMID33914858_Repudi2021_Brain_operator_supplied.pdf, PMID33914858_Repudi2021_Brain_operator_supplied.txt, PMID33914858_Repudi2021_OUP_browserprint.pdf, PMID33914858_Repudi2021_OUP_browserprint_pdftotext.txt |
| PMID 42128308 | FT-045 | `absent` | — | — |
| PMID 15070730 | FT-046, FT-064 | `structured` | `clean` | PMID15070730_Aqeilan2004.pdf, PMID15070730_Aqeilan2004_PMC_2026-09-09.html |
| PMID 18974271 | FT-046 | `absent` | — | — |
| PMID 17575124 | FT-047, FT-064 | `absent` | — | — |
| PMID 20530675 | FT-047, FT-072, FT-078 | `structured` | `clean` | PMID20530675_Kurek2010_PMC.xml, PMID20530675_Kurek2010_supplement1.pdf, PMID20530675_Kurek2010_supplement1.txt |
| PMID 21318118 | FT-047 | `absent` | — | — |
| PMID 22634283 | FT-047 | `absent` | — | — |
| PMID 23254685 | FT-047 | `absent` | — | — |
| PMID 26256646 | FT-047 | `absent` | — | — |
| PMID 27308416 | FT-047 | `absent` | — | — |
| PMID 27308504 | FT-047 | `absent` | — | — |
| PMID 27550453 | FT-047 | `absent` | — | — |
| PMID 27551470 | FT-047 | `structured` | `clean` | PMID27551470_Hazan2015_PMC.pdf, PMID27551470_Hazan2015_PMC.xml |
| PMID 29724996 | FT-047 | `structured` | `clean` | PMID29724996_AbuRemaileh2018_PMC.xml, PMID29724996_AbuRemaileh2018_article.pdf, PMID29724996_AbuRemaileh2018_supplement.pdf, PMID29724996_AbuRemaileh2018_supplement.txt |
| PMID 30082886 | FT-047 | `absent` | — | — |
| PMID 30370248 | FT-047 | `absent` | — | — |
| PMID 30755385 | FT-047, FT-048, FT-049 | `absent` | — | — |
| PMID 31428585 | FT-047 | `structured` | `clean` | PMID31428585_Chang2019_PMC.xml |
| PMID 32300104 | FT-047 | `absent` | — | — |
| PMID 34634460 | FT-047, FT-058 | `structured` | `clean` | PMID34634460_Breton2021_EPMC_2026-09-27.xml |
| PMID 34831305 | FT-047 | `absent` | — | — |
| PMID 42395553 | FT-047 | `pdf_only` | `clean` | PMID42395553_Petrozziello2026_bioRxiv.pdf, PMID42395553_Petrozziello2026_bioRxiv.txt |
| PMID 42422765 | FT-047 | `structured` | `clean` | PMID42422765_Obeid2026_PMC_2026-09-27.xml |
| PMID 34747138 | FT-049, FT-152 | `structured` | `clean` | PMID34747138_Repudi2021_PMC.xml |
| PMID 38499540 | FT-051 | `structured` | `clean` | PMID38499540_BidanyMizrahi2024_PMC.xml |
| PMID 25331887 | FT-052, FT-053 | `structured` | `clean` | PMID25331887_AbuOdeh2014.pdf, PMID25331887_AbuOdeh2014_PMC_2026-09-09.html |
| PMID 24550385 | FT-054, FT-060 | `absent` | — | — |
| PMID 34034642 | FT-056 | `absent` | — | — |
| PMID 17823927 | FT-057 | `structured` | `clean` | PMID17823927_LudesMeyers2007.html, PMID17823927_LudesMeyers2007.pdf |
| PMID 25411445 | FT-057 | `absent` | — | — |
| PMID 29808465 | FT-057, FT-122, FT-154 | `pdf_only` | `clean` | PMID29808465_Johannsen2018.pdf, PMID29808465_Johannsen2018.txt |
| PMID 30158849 | FT-057 | `structured` | `clean` | PMID30158849_Liu2018_PMC.xml |
| PMID 30356099 | FT-057 | `structured` | `clean` | PMID30356099_Piard2019_EPMC.xml, PMID30356099_Piard2019_PMC_2026-09-27.xml |
| PMID 34268881 | FT-059 | `structured` | `clean` | PMID34268881_Steinberg2021.pdf, PMID34268881_Steinberg2021_PMC.xml |
| PMID 23435430 | FT-061 | `absent` | — | — |
| PMID 23370280 | FT-062 | `absent` | — | — |
| PMID 12514174 | FT-063 | `absent` | — | — |
| PMID 16061658 | FT-063 | `absent` | — | — |
| PMID 39416860 | FT-065 | `absent` | — | — |
| PMID 26675548 | FT-067 | `absent` | — | — |
| PMID 18487609 | FT-068, FT-063 | `absent` | — | — |
| PMID 27869163 | FT-070 | `structured` | `clean` | PMID27869163_Schrock2017.xml, PMID27869163_efetch.xml, PMID27869163_epmc.pdf, PMID27869163_epmc2.pdf, PMID27869163_pmc.pdf |
| PMID 18674750 | FT-071 | `structured` | `clean` | PMID18674750_Lee2008.pdf, PMID18674750_Lee2008_PMC.html, PMID18674750_Lee2008_supplement.pdf, PMID18674750_Lee2008_supplement.txt |
| PMID 27845895 | FT-073 | `absent` | — | — |
| PMID 31966718 | FT-074 | `absent` | — | — |
| PMID 18931939 | FT-075 | `absent` | — | — |
| PMID 16223882 | FT-076, FT-088 | `pdf_only` | `SUSPECT` — contains the C0 control U+0001 | PMID16223882_Fabbri2005_PMC.pdf |
| PMID 21731849 | FT-077 | `pdf_only` | `clean` | PMID21731849_DelMare2011_AJCR.pdf, PMID21731849_DelMare2011_AJCR.txt |
| PMID 16941225 | FT-079 | `pdf_only` | `clean` | PMID16941225_Nunez2006.pdf, PMID16941225_Nunez2006.txt |
| PMID 18193043 | FT-081 | `absent` | — | — |
| PMID 17458891 | FT-082 | `absent` | — | — |
| PMID 36828035 | FT-083 | `structured` | `clean` | PMID36828035_Hussain2023.pdf, PMID36828035_Hussain2023_EPMC.xml, PMID36828035_Hussain2023_PMC.xml |
| PMID 30350478 | FT-084 | `absent` | — | — |
| PMID 27773744 | FT-085 | `absent` | — | — |
| PMID 15073846 | FT-086, FT-179 | `absent` | — | — |
| PMID 12704432 | FT-087 | `absent` | — | — |
| PMID 25238781 | FT-089 | `structured` | `clean` | PMID25238781_Aqeilan2014_PMC.html, PMID25238781_Aqeilan2014_PMC.pdf |
| PMID 25416187 | FT-090 | `absent` | — | — |
| PMID 25245215 | FT-091 | `structured` | `clean` | PMID25245215_Aqeilan2014_PMC.html, PMID25245215_Aqeilan2014_PMC.pdf |
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
| PMID 20146584 | FT-096 | `structured` | `clean` | PMID20146584_Salah2010_PMC.xml |
| PMID 41390778 | FT-097 | `absent` | — | — |
| PMID 33134515 | FT-098 | `absent` | — | — |
| PMID 21766012 | FT-099 | `absent` | — | — |
| PMID 32020597 | FT-100 | `absent` | — | — |
| PMID 9918798 | FT-101 | `absent` | — | — |
| PMID 25650666 | FT-102 | `structured` | `clean` | PMID25650666_Chang2015_PMC.xml |
| PMID 27569545 | FT-103, FT-105 | `absent` | — | — |
| PMID 29067327 | FT-104 | `structured` | `clean` | PMID29067327_Lee2017_PMC.xml |
| PMID 42092735 | FT-106 | `structured` | `clean` | PMID42092735_SercePehlevan2026_PMC.xml |
| PMID 41153369 | FT-107 | `structured` | `clean` | PMID41153369_SunnetciAkkoyunlu2025_PMC.xml |
| PMID 19484134 | FT-108 | `absent` | — | — |
| PMID 18371080 | FT-109 | `absent` | — | — |
| PMID 38902482 | FT-110 | `absent` | — | — |
| PMID 42721537 | FT-110 | `absent` | — | — |
| PMID 35328751 | FT-111 | `structured` | `clean` | PMID35328751_Baryla2022_PMC.xml |
| PMID 14555208 | FT-113 | `absent` | — | — |
| PMID 15580310 | FT-113 | `absent` | — | — |
| PMID 16380372 | FT-113 | `absent` | — | — |
| PMID 17067289 | FT-113 | `absent` | — | — |
| PMID 29785012 | FT-113 | `absent` | — | — |
| PMID 32442409 | FT-113 | `absent` | — | — |
| PMID 38378758 | FT-113 | `absent` | — | — |
| PMID 41442931 | FT-114 | `absent` | — | — |
| PMID 41510857 | FT-115 | `absent` | — | — |
| PMID 22534828 | FT-116 | `absent` | — | — |
| PMID 17289941 | FT-118 | `absent` | — | — |
| PMID 25866966 | FT-118 | `absent` | — | — |
| PMID 31704158 | FT-118 | `absent` | — | — |
| PMID 30949922 | FT-119 | `absent` | — | — |
| PMID 26070663 | FT-120 | `absent` | — | — |
| PMID 28721938 | FT-121 | `pdf_only` | `clean` | PMID28721938_TartaArsene2017_JLE.pdf, PMID28721938_TartaArsene2017_JLE.txt |
| PMID 30783266 | FT-121 | `absent` | — | — |
| PMID 39140066 | FT-123 | `absent` | — | — |
| PMID 40665325 | FT-123 | `absent` | — | — |
| PMID 41704356 | FT-123 | `absent` | — | — |
| PMID 42714273 | FT-123 | `absent` | — | — |
| PMID 34523672 | FT-124 | `absent` | — | — |
| PMID 38159337 | FT-124 | `absent` | — | — |
| PMID 38658199 | FT-124 | `absent` | — | — |
| PMID 36537114 | FT-125 | `absent` | — | — |
| PMID 24369382 | FT-128 | `structured` | `clean` | PMID24369382_Mallaret2014.pdf, PMID24369382_Mallaret2014.txt, PMID24369382_Mallaret2014_PMCreader.html, PMID24369382_Mallaret2014_PMCreader.txt, PMID24369382_Mallaret2014_efetch.xml |
| PMID 18216017 | FT-129 | `absent` | — | — |
| PMID 22113611 | FT-129 | `absent` | — | — |
| PMID 24891511 | FT-129 | `structured` | `clean` | PMID24891511_Nakasone2014_PMC_2026-09-26.html, PMID24891511_Nakasone2014_PMC_2026-09-26.txt |
| PMID 26780369 | FT-129 | `absent` | — | — |
| PMID 30202070 | FT-129 | `absent` | — | — |
| PMID 21476439 | FT-130, FT-147 | `pdf_only` | `clean` | PMID21476439_SaludaGorgul2011_DeGruyter.pdf, PMID21476439_SaludaGorgul2011_DeGruyter.txt |
| PMID 28097321 | FT-131 | `absent` | — | — |
| PMID 23583307 | FT-132 | `structured` | `clean` | PMID23583307_Semple2013_PMC.xml |
| PMID 38122823 | FT-133 | `structured` | `clean` | PMID38122823_Nascimento2023_PMC.xml |
| PMID 40659844 | FT-134 | `absent` | — | — |
| PMID 38407561 | FT-135 | `absent` | — | — |
| PMID 18273838 | FT-136 | `absent` | — | — |
| PMID 17314322 | FT-137 | `absent` | — | — |
| PMID 38515655 | FT-138 | `absent` | — | — |
| PMID 41957021 | FT-138 | `absent` | — | — |
| PMID 17019711 | FT-139 | `absent` | — | — |
| PMID 17200365 | FT-139 | `absent` | — | — |
| PMID 31618474 | FT-140 | `structured` | `clean` | PMID31618474_Burgess2019_PMC_efetch.xml |
| PMID 32214227 | FT-140 | `structured` | `clean` | PMID32214227_Hengel2020_PMC.xml |
| PMID 40463067 | FT-141 | `absent` | — | — |
| PMID 42425971 | FT-141 | `absent` | — | — |
| PMID 28763065 | FT-142 | `structured` | `clean` | PMID28763065_Xia2017_PMC.xml |
| PMID 41378749 | FT-142 | `structured` | `clean` | PMID41378749_MondragonEstrada2025_PMC.xml |
| PMID 11058590 | FT-143 | `absent` | — | — |
| PMID 42523332 | FT-143 | `absent` | — | — |
| PMID 28416821 | FT-144 | `absent` | — | — |
| PMID 33520443 | FT-144 | `absent` | — | — |
| PMID 37583270 | FT-144 | `structured` | `clean` | PMID37583270_Nagarajan2023_PMC.xml |
| PMID 42464650 | FT-144 | `absent` | — | — |
| PMID 42589397 | FT-144 | `structured` | `clean` | PMID42589397_ZZ2026_PMC_2026-09-27.xml |
| PMID 11007791 | FT-145 | `absent` | — | — |
| PMID 11306088 | FT-145 | `absent` | — | — |
| PMID 17258342 | FT-145 | `absent` | — | — |
| PMID 17567906 | FT-145 | `absent` | — | — |
| PMID 37285720 | FT-145 | `absent` | — | — |
| PMID 35243249 | FT-146 | `absent` | — | — |
| PMID 17291468 | FT-148 | `absent` | — | — |
| PMID 17470496 | FT-149, FT-177 | `absent` | — | — |
| PMID 29141528 | FT-150 | `absent` | — | — |
| PMID 27595938 | FT-151 | `absent` | — | — |
| PMID 28779490 | FT-151 | `absent` | — | — |
| PMID 19088074 | FT-153 | `absent` | — | — |
| PMID 20062057 | FT-153 | `absent` | — | — |
| PMID 22611163 | FT-153 | `absent` | — | — |
| PMID 28911204 | FT-153 | `absent` | — | — |
| PMID 30279493 | FT-153 | `absent` | — | — |
| PMID 30518535 | FT-153 | `absent` | — | — |
| PMID 31271415 | FT-153 | `absent` | — | — |
| PMID 31605637 | FT-153 | `absent` | — | — |
| PMID 34934109 | FT-153 | `absent` | — | — |
| PMID 35065072 | FT-153 | `absent` | — | — |
| PMID 38131282 | FT-153 | `absent` | — | — |
| PMID 19054067 | FT-155 | `absent` | — | — |
| PMID 21633011 | FT-156 | `absent` | — | — |
| PMID 27129733 | FT-157 | `absent` | — | — |
| PMID 18676360 | FT-158 | `absent` | — | — |
| PMID 19918364 | FT-159 | `structured` | `clean` | PMID19918364_Li2009_PMC.xml |
| PMID 36247526 | FT-160 | `absent` | — | — |
| PMID 40235507 | FT-161 | `absent` | — | — |
| PMID 41776383 | FT-162 | `absent` | — | — |
| PMID 28742274 | FT-163 | `absent` | — | — |
| PMID 30820047 | FT-164 | `absent` | — | — |
| PMID 34190042 | FT-165 | `absent` | — | — |
| PMID 34616292 | FT-166 | `absent` | — | — |
| PMID 35053314 | FT-167 | `absent` | — | — |
| PMID 36882863 | FT-168 | `absent` | — | — |
| PMID 42266427 | FT-169 | `absent` | — | — |
| PMID 33963278 | FT-170 | `absent` | — | — |
| PMID 40006511 | FT-171 | `absent` | — | — |
| PMID 24152123 | FT-172 | `absent` | — | — |
| PMID 10356397 | FT-173 | `absent` | — | — |
| PMID 16921370 | FT-174 | `absent` | — | — |
| PMID 39868255 | FT-175 | `structured` | `clean` | PMID39868255_DeLaCruz2025_biorxiv.pdf, PMID39868255_DeLaCruz2025_biorxiv.source.xml, PMID39868255_DeLaCruz2025_biorxiv_full.html, PMID39868255_DeLaCruz2025_preprint.pdf |
| PMID 35409089 | FT-176 | `structured` | `clean` | PMID35409089_Park2022.xml, PMID35409089_epmc.pdf |
| PMID 28283473 | FT-178 | `absent` | — | — |
| PMID 11572989 | FT-179 | `structured` | `clean` | PMID11572989_Paige2001_PMC_2026-09-27.html, PMID11572989_Paige2001_PMC_2026-09-27.xml |
| PMID 14526170 | FT-179 | `absent` | — | — |
| PMID 14695174 | FT-179 | `absent` | — | — |
| PMID 19465938 | FT-180 | `absent` | — | — |
| PMID 22574198 | FT-181 | `structured` | `clean` | PMID22574198_Ferguson2012.pdf, PMID22574198_Ferguson2012.xml |
| PMID 25538133 | FT-182 | `absent` | — | — |
| PMID 16438931 | FT-184 | `absent` | — | — |
| PMID 25398664 | FT-185 | `absent` | — | — |
| PMID 19525979 | FT-186 | `absent` | — | — |
| PMID 20571887 | FT-187 | `absent` | — | — |
| PMID 21519330 | FT-188 | `absent` | — | — |
| PMID 15735698 | FT-189 | `absent` | — | — |
| PMID 9626493 | FT-190 | `absent` | — | — |
| PMID 10451696 | FT-191 | `absent` | — | — |
| PMID 10749140 | FT-191 | `absent` | — | — |
| PMID 10910080 | FT-191 | `absent` | — | — |
| PMID 7644498 | FT-192 | `absent` | — | — |
| PMID 11042109 | FT-192 | `absent` | — | — |
| PMID 41404412 | FT-193 | `structured` | `clean` | PMID41404412_Grubor2025_PMC.xml |
| PMID 42422766 | FT-193 | `structured` | `clean` | PMID42422766_Amaral2026_PMC.xml |
| PMID 40183601 | FT-194 | `structured` | `clean` | PMID40183601_Henry2025_EPI-66-2966-s002.txt, PMID40183601_Henry2025_EPI-66-2966-s003.txt, PMID40183601_Henry2025_PMC.xml, PMID40183601_Henry2025_supp_tableS9.txt |
| PMID 15064722 | — | `structured` | `clean` | PMID15064722_LudesMeyers2004.pdf, PMID15064722_LudesMeyers2004.txt, PMID15064722_LudesMeyers2004_PMCreader.html, PMID15064722_LudesMeyers2004_PMCreader.txt, PMID15064722_LudesMeyers2004_efetch.xml |
| PMID 15266310 | — | `structured` | `clean` | PMID15266310_Park2004.pdf, PMID15266310_Park2004.xml |
| PMID 15870886 | — | `structured` | `clean` | PMID15870886_Gourley2005.html, PMID15870886_Gourley2005.pdf, PMID15870886_Gourley2005_PMC_2026-09-27.xml |
| PMID 16152610 | — | `structured` | `clean` | PMID16152610_Pimenta2006.html, PMID16152610_Pimenta2006.pdf |
| PMID 16187332 | — | `structured` | `clean` | PMID16187332_Thavathiru2005.html, PMID16187332_Thavathiru2005.pdf |
| PMID 17679088 | — | `structured` | `clean` | PMID17679088_Zhang2007_PMC.html |
| PMID 18047428 | — | `structured` | `clean` | PMID18047428_Dias2007.html, PMID18047428_Dias2007.pdf |
| PMID 18061530 | — | `structured` | `clean` | PMID18061530_Pimenta2008.html, PMID18061530_Pimenta2008.pdf |
| PMID 18452537 | — | `structured` | `clean` | PMID18452537_Ramos2008.html, PMID18452537_Ramos2008.pdf |
| PMID 18460020 | — | `pdf_only` | `clean` | PMID18460020_Nakayama2008_PMC.pdf, PMID18460020_Nakayama2008_PMC.txt |
| PMID 21212468 | — | `structured` | `clean` | PMID21212468_Dudekula2010_PMC.xml |
| PMID 21368882 | — | `structured` | `clean` | PMID21368882_Lee2010_PMC.xml |
| PMID 21964341 | — | `structured` | `clean` | PMID21964341_Sanai2011_PMC.xml |
| PMID 23179753 | — | `structured` | `clean` | PMID23179753_Krug2013_PMC.xml |
| PMID 24008736 | — | `structured` | `clean` | PMID24008736_Tsai2013_PMC.xml |
| PMID 24330518 | — | `structured` | `clean` | PMID24330518_Ferguson2013.pdf, PMID24330518_Ferguson2013.xml |
| PMID 24456803 | — | `structured` | `clean` | PMID24456803_AbdelSalam2014_PMC.xml |
| PMID 24510053 | — | `pdf_only` | `SUSPECT` — PMID24510053_Gardenswartz2014.pdf: contains the C0 control U+0002 | PMID24510053_Gardenswartz2014.pdf, PMID24510053_Gardenswartz2014.txt |
| PMID 24520212 | — | `structured` | `clean` | PMID24520212_Li2014_PMC.xml |
| PMID 24932569 | — | `structured` | `clean` | PMID24932569_Aldaz2014.pdf, PMID24932569_Aldaz2014_efetch.xml |
| PMID 24935251 | — | `structured` | `clean` | PMID24935251_Balmer2014_PMC.xml |
| PMID 24949445 | — | `structured` | `clean` | PMID24949445_Szymanska2014_PMC.xml |
| PMID 25024751 | — | `structured` | `clean` | PMID25024751_Stewart2014.pdf, PMID25024751_Stewart2014.xml |
| PMID 25537520 | — | `structured` | `clean` | PMID25537520_Chang2014_PMC.xml |
| PMID 25649963 | — | `structured` | `clean` | PMID25649963_Tsuruwaka2015_PMC.xml |
| PMID 26272509 | — | `structured` | `clean` | PMID26272509_Rempel2015_PMC.xml |
| PMID 26302329 | — | `structured` | `clean` | PMID26302329_OKeefe2015_PMC.xml |
| PMID 26499798 | — | `structured` | `clean` | PMID26499798_AbuRemaileh2015.pdf, PMID26499798_AbuRemaileh2015_PMC.html |
| PMID 27188386 | — | `structured` | `clean` | PMID27188386_Shinde2016_PMC.xml |
| PMID 27495153 | — | `structured` | `clean` | PMID27495153_Elsaadany2016_PMC.xml |
| PMID 27551439 | — | `structured` | `clean` | PMID27551439_Chang2015_PMC.xml |
| PMID 28373548 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0002 | PMID28373548_EoC_PNAS2017.pdf |
| PMID 28749468 | — | `structured` | `clean` | PMID28749468_Janczar2017_PMC.xml |
| PMID 29390993 | — | `structured` | `clean` | PMID29390993_Rim2018_PMC.xml |
| PMID 30073178 | — | `structured` | `clean` | PMID30073178_Hordeaux2018b_PMC.xml |
| PMID 30073179 | — | `structured` | `clean` | PMID30073179_Hordeaux2018a_PMC.xml |
| PMID 30285739 | — | `structured` | `clean` | PMID30285739_Bonin2018.pdf, PMID30285739_Bonin2018.xml |
| PMID 30361190 | — | `pdf_only` | `SUSPECT` — PMID30361190_Shaukat2018_JLE.pdf: contains the digit '3' where the page prints U+00D7 '×' in scientific notation (Elsevier/LiveCycle text layer) ('0\n3\n10') | PMID30361190_Shaukat2018_JLE.pdf, PMID30361190_Shaukat2018_JLE.txt |
| PMID 30362252 | — | `structured` | `clean` | PMID30362252_Davids2019_PMC_2026-09-27.xml |
| PMID 30470736 | — | `structured` | `clean` | PMID30470736_AbuRemaileh2018_correction_PMC.xml |
| PMID 30746283 | — | `structured` | `clean` | PMID30746283_Ehaideb2018_PMC.xml |
| PMID 31275852 | — | `structured` | `clean` | PMID31275852_McBride2019.pdf, PMID31275852_McBride2019.xml |
| PMID 31315632 | — | `structured` | `clean` | PMID31315632_Chou2019_PMC.xml |
| PMID 31353122 | — | `pdf_only` | `clean` | PMID31353122_Mori2019_IR.pdf, PMID31353122_Mori2019_IR.txt |
| PMID 32081867 | — | `structured` | `clean` | PMID32081867_Bacchelli2020_PMC.xml |
| PMID 32355866 | — | `structured` | `clean` | PMID32355866_Bey2020_PMC.xml |
| PMID 32368285 | — | `structured` | `clean` | PMID32368285_Celebi2020_PMC.xml, PMID32368285_Celebi2020_publisher.pdf |
| PMID 32389029 | — | `structured` | `clean` | PMID32389029_Kosla2020_PMC.xml |
| PMID 33058734 | — | `pdf_only` | `SUSPECT` — uses statistical language (6 mentions) and contains none of < > ≤ ≥ ± × − | PMID33058734_Zeng2021.pdf |
| PMID 33129329 | — | `structured` | `clean` | PMID33129329_Makii2020_PMC.xml |
| PMID 33195192 | — | `structured` | `clean` | PMID33195192_Chou2020_PMC.xml |
| PMID 33255508 | — | `structured` | `clean` | PMID33255508_Aldaz2020.xml |
| PMID 33300063 | — | `pdf_only` | `clean` | PMID33300063_Zhao2020_Spandidos.pdf, PMID33300063_Zhao2020_Spandidos.txt, PMID33300063_Zhao2020_Spandidos_suppl.pdf |
| PMID 33612478 | — | `structured` | `clean` | PMID33612478_Liu2021_PMC.xml |
| PMID 33726816 | — | `structured` | `clean` | PMID33726816_Stranneheim2021_13073_2021_855_MOESM3_ESM.txt, PMID33726816_Stranneheim2021_PMC.xml |
| PMID 33916893 | — | `structured` | `clean` | PMID33916893_Aqeilan2021_PMC.xml |
| PMID 33919646 | — | `structured` | `clean` | PMID33919646_Spagnoli2021_PMC.xml |
| PMID 33958783 | — | `structured` | `clean` | PMID33958783_Liu2021_PMC.xml |
| PMID 34204789 | — | `structured` | `clean` | PMID34204789_Kaluzinska2021_PMC.xml |
| PMID 34359949 | — | `structured` | `clean` | PMID34359949_Hsu2021_PMC.xml |
| PMID 34852950 | — | `structured` | `clean` | PMID34852950_Dugan2022_PMC.xml |
| PMID 35229008 | — | `structured` | `clean` | PMID35229008_Buss2022_PMC.xml |
| PMID 35331006 | — | `structured` | `clean` | PMID35331006_Tukov2022_PMC.xml |
| PMID 35333110 | — | `structured` | `clean` | PMID35333110_Hordeaux2022_PMC.xml |
| PMID 35460704 | — | `structured` | `clean` | PMID35460704_Dong2022_PMC.xml |
| PMID 35712340 | — | `structured` | `clean` | PMID35712340_Sukkar2022_PMC.xml |
| PMID 35715422 | — | `structured` | `clean` | PMID35715422_Yang2022_PMC.xml |
| PMID 35792847 | — | `structured` | `clean` | PMID35792847_AlBaradie2022_JLE.pdf, PMID35792847_AlBaradie2022_JLE_abstract.html, PMID35792847_AlBaradie2022_JLE_fulltext.html |
| PMID 36271927 | — | `structured` | `clean` | PMID36271927_Baryla2022_PMC.xml |
| PMID 36291747 | — | `structured` | `clean` | PMID36291747_Reinehr2022_PMC.xml |
| PMID 36498839 | — | `structured` | `clean` | PMID36498839_Lin2022_PMC.xml |
| PMID 36700120 | — | `structured` | `clean` | PMID36700120_Johnson2022_PMC.xml |
| PMID 36926521 | — | `structured` | `clean` | PMID36926521_Colin2023_PMC.xml |
| PMID 36937954 | — | `structured` | `clean` | PMID36937954_Alotibi2023_PMC.xml |
| PMID 36951961 | — | `structured` | `clean` | PMID36951961_Chen2023_PMC.xml |
| PMID 37095367 | — | `structured` | `clean` | PMID37095367_Bayanova2023_PMC.xml |
| PMID 37248434 | — | `structured` | `clean` | PMID37248434_Taouis2023_PMC.xml |
| PMID 37501399 | — | `structured` | `clean` | PMID37501399_Yang2023_PMC.xml |
| PMID 37515322 | — | `structured` | `clean` | PMID37515322_Hudry2023_PMC.xml |
| PMID 37781246 | — | `structured` | `clean` | PMID37781246_KaluzinskaKolat2023_PMC.xml |
| PMID 37897534 | — | `structured` | `clean` | PMID37897534_Cheng2023_PMC.xml |
| PMID 37946251 | — | `structured` | `clean` | PMID37946251_Pagnamenta2023_PMC.xml |
| PMID 37974179 | — | `structured` | `clean` | PMID37974179_Dong2023_PMC.xml |
| PMID 38161429 | — | `structured` | `clean` | PMID38161429_Battaglia2023_PMC_2026-09-27.xml |
| PMID 38355659 | — | `structured` | `clean` | PMID38355659_Akkawi2024_correction.pdf, PMID38355659_Akkawi2024_correction_PMC.xml |
| PMID 38540325 | — | `structured` | `clean` | PMID38540325_Snyder2024_PMC.xml |
| PMID 38542478 | — | `structured` | `clean` | PMID38542478_Chen2024_PMC.xml |
| PMID 38563965 | — | `structured` | `clean` | PMID38563965_Zeng2024_PMC.html |
| PMID 38719828 | — | `structured` | `clean` | PMID38719828_MartinezLumbreras2024_PMC.xml |
| PMID 39101447 | — | `structured` | `clean` | PMID39101447_You2024_PMC.xml |
| PMID 39358605 | — | `structured` | `clean` | PMID39358605_Wiseman2024_PMC.xml |
| PMID 39847501 | — | `structured` | `clean` | PMID39847501_Chen2025_PMC.xml |
| PMID 39850204 | — | `structured` | `clean` | PMID39850204_Zhu2025_PMC.xml |
| PMID 40019827 | — | `structured` | `clean` | PMID40019827_Innes2025_PMC.xml |
| PMID 40083435 | — | `structured` | `clean` | PMID40083435_Kava2025_PMC.xml, PMID40083435_Kava2025_Table1.txt |
| PMID 40126049 | — | `structured` | `clean` | PMID40126049_CerulliIrelli2025_PMC.xml |
| PMID 40191585 | — | `structured` | `clean` | PMID40191585_Robertson2025_PMC.xml |
| PMID 40217411 | — | `structured` | `clean` | PMID40217411_Yuan2025_PMC.xml |
| PMID 40263630 | — | `structured` | `clean` | PMID40263630_Wagner2025_PMC.xml |
| PMID 40301740 | — | `structured` | `clean` | PMID40301740_Ma2025_PMC.xml |
| PMID 40336300 | — | `structured` | `clean` | PMID40336300_Lawrence2025_PMC.xml |
| PMID 40349107 | — | `structured` | `clean` | PMID40349107_Aeran2025_PMC.xml |
| PMID 40377402 | — | `structured` | `clean` | PMID40377402_Pascual2025_PMC.xml |
| PMID 40429983 | — | `structured` | `clean` | PMID40429983_Sabau2025_PMC.xml |
| PMID 40507943 | — | `structured` | `clean` | PMID40507943_Hsu2025_PMC.xml |
| PMID 40524961 | — | `structured` | `clean` | PMID40524961_Sengupta2025_PMC.xml |
| PMID 40809677 | — | `structured` | `clean` | PMID40809677_DubaKiss2025_PMC.xml |
| PMID 40858643 | — | `structured` | `clean` | PMID40858643_Hamanaka2025_PMC.xml |
| PMID 40884527 | — | `structured` | `clean` | PMID40884527_Beretti2025_AppendixS1.pdf, PMID40884527_Beretti2025_PMC.xml |
| PMID 40937943 | — | `structured` | `clean` | PMID40937943_Ramirez2025_PMC.xml |
| PMID 40943441 | — | `structured` | `clean` | PMID40943441_Panchenko2025_PMC.xml |
| PMID 40952239 | — | `structured` | `clean` | PMID40952239_Carpanese2025_PMC.xml |
| PMID 40988338 | — | `structured` | `clean` | PMID40988338_Quinlan2025_PMC.xml, PMID40988338_Quinlan2025_PMC_supp_mmc1.pdf, PMID40988338_Quinlan2025_PMC_supp_mmc1.txt |
| PMID 41036104 | — | `structured` | `clean` | PMID41036104_Chornyy2025_PMC.xml |
| PMID 41078870 | — | `structured` | `clean` | PMID41078870_Okai2025_PMC.xml |
| PMID 41090157 | — | `structured` | `clean` | PMID41090157_Hussain2025.pdf, PMID41090157_Hussain2025.xml |
| PMID 41124647 | — | `structured` | `clean` | PMID41124647_Zhang2025_PMC.xml |
| PMID 41134821 | — | `structured` | `clean` | PMID41134821_Zhao2025_PMC.xml |
| PMID 41210171 | — | `structured` | `clean` | PMID41210171_Vono2025_PMC.xml |
| PMID 41254692 | — | `structured` | `clean` | PMID41254692_Qin2025_PMC.xml |
| PMID 41257285 | — | `structured` | `clean` | PMID41257285_Aihara2025_PMC.xml |
| PMID 41314141 | — | `structured` | `clean` | PMID41314141_Greenberg2026_PMC.xml |
| PMID 41345172 | — | `structured` | `clean` | PMID41345172_De2025_PMC.xml |
| PMID 41438872 | — | `structured` | `clean` | PMID41438872_Fortuna2025_PMC.xml |
| PMID 41477840 | — | `structured` | `clean` | PMID41477840_Stamouli2026_PMC.xml |
| PMID 41562193 | — | `structured` | `clean` | PMID41562193_Druck2026_EuropePMC_render.pdf, PMID41562193_Druck2026_PMC.xml |
| PMID 41677633 | — | `structured` | `clean` | PMID41677633_Su2026_PMC.xml |
| PMID 41712149 | — | `structured` | `clean` | PMID41712149_Balestrini2026_PMC.xml |
| PMID 41712282 | — | `structured` | `clean` | PMID41712282_Bailey2026_PMC.xml |
| PMID 41744777 | — | `structured` | `clean` | PMID41744777_Nabakowski2026_PMC.xml |
| PMID 41751597 | — | `structured` | `SUSPECT` — contains '¼' where the page prints '=' (Elsevier/LiveCycle text layer) ('d ¼ t') | PMID41751597_Rioux2026_PMC.derived.txt, PMID41751597_Rioux2026_PMC.xml |
| PMID 41835067 | — | `structured` | `clean` | PMID41835067_Yigit2026_PMC.xml |
| PMID 41948127 | — | `structured` | `clean` | PMID41948127_Stavrou2026_PMC.xml |
| PMID 41966056 | — | `structured` | `clean` | PMID41966056_Wang2026_PMC.xml |
| PMID 41992613 | — | `structured` | `clean` | PMID41992613_Song2026_PMC.xml |
| PMID 42068099 | — | `structured` | `clean` | PMID42068099_Mohammad2026_PMC.xml |
| PMID 42134074 | — | `structured` | `clean` | PMID42134074_Kagiava2026_PMC.xml |
| PMID 42135313 | — | `structured` | `clean` | PMID42135313_Kang2026_PMC.xml |
| PMID 42136830 | — | `structured` | `clean` | PMID42136830_Haque2026_PMC.xml |
| PMID 42137263 | — | `structured` | `clean` | PMID42137263_Moeini2026_PMC.xml |
| PMID 42137269 | — | `structured` | `clean` | PMID42137269_Chauhan2026_PMC.xml |
| PMID 42137271 | — | `structured` | `clean` | PMID42137271_Hordeaux2026_PMC.xml |
| PMID 42137291 | — | `structured` | `clean` | PMID42137291_Thomsen2026_PMC.xml |
| PMID 42157962 | — | `structured` | `clean` | PMID42157962_DuBreuil2026_PMC.xml |
| PMID 42170349 | — | `structured` | `clean` | PMID42170349_Flotte2026_PMC.xml |
| PMID 42181696 | — | `structured` | `clean` | PMID42181696_Diaz2026_PMC.xml |
| PMID 42193054 | — | `structured` | `clean` | PMID42193054_Sapuppo2026_PMC.xml |
| PMID 42198847 | — | `structured` | `clean` | PMID42198847_BoespflugTanguy2026_PMC.xml |
| PMID 42205472 | — | `structured` | `clean` | PMID42205472_Engelhard2026_PMC.xml |
| PMID 42248868 | — | `structured` | `clean` | PMID42248868_Zhao2026_PMC.xml |
| PMID 42349402 | — | `structured` | `clean` | PMID42349402_Fukai2026_PMC.xml |
| PMID 42394473 | — | `structured` | `clean` | PMID42394473_Karaer2026_PMC.xml |
| PMID 42436860 | — | `structured` | `clean` | PMID42436860_NaViPA1_2026_PMC.xml |
| PMID 42458834 | — | `structured` | `clean` | PMID42458834_Boitnott2026_PMC.xml |
| PMID 42511902 | — | `structured` | `clean` | PMID42511902_Gao2026_PMC.xml |
| PMID 42521212 | — | `structured` | `clean` | PMID42521212_Saravanan2026_PMC.xml |
| PMID 42538560 | — | `structured` | `clean` | PMID42538560_ICVchoroid2026_PMC.xml |
| PMID 42558002 | — | `structured` | `clean` | PMID42558002_Lange2026_PMC.xml |
| PMID 42738875 | — | `structured` | `clean` | PMID42738875_Tang2026_PMC.xml |
| PMID 42770556 | — | `structured` | `clean` | PMID42770556_Lima2026_PMC.xml |
| PMID 42771216 | — | `structured` | `clean` | PMID42771216_Kohler2026_PMC.xml |
| PMID 42807309 | — | `pdf_only` | `clean` | PMID42807309_16q231_pancreatitis_2026.pdf, PMID42807309_16q231_pancreatitis_2026.txt |
| PMID 42807679 | — | `structured` | `clean` | PMID42807679_Khadija2026_PMC.xml |
| PMID 42812991 | — | `pdf_only` | `clean` | PMID42812991_AAV_AD_review_2026.pdf, PMID42812991_AAV_AD_review_2026.txt |

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
| FT-126 | `not_an_article` | NOT_AN_ARTICLE — this entry records instrument behaviour, not a source. |
| FT-127 | `not_an_article` | NOT_AN_ARTICLE — this entry records an adjudication and two artefact-integrity facts. |

**Accounting.** Rows: 227 corpus papers + 254 queued papers − 63 in both = **418** emitted. ✓ Entries: 184 resolved + 9 unjoined = **193** queue entries. ✓

*Not medical advice. This page describes file formats, not findings.*

