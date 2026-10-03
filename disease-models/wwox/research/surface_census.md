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

**Census date:** 2026-10-03  
**Corpus:** `fulltext` — 250 entries, 119 papers, listing digest `3550a18deed3ac62`  
**Sentinel:** `deepdive_manifest._refuse_suspect_surface`, PDF text via PyMuPDF 1.28.2

### Totals

| Surface | Papers | What it means |
|---|---:|---|
| `structured` | 107 | publisher XML/HTML present — read this one (rule 5d) |
| `pdf_only` | 11 | no structured surface locally — acquire XML/HTML before reading |
| `absent` | 198 | queued, nothing local at all — retrieve first |

Sentinel over the surface each paper would actually be read from — the structured file where one exists, the PDF otherwise. Structured markup is screened too, because a suffix is not a surface; see the note below:

| Verdict | Papers | What it means |
|---|---:|---|
| `SUSPECT` | 5 | the text carries a known corruption signature — do not quote it; adjudicate against the rendered page, or re-acquire the paper structured |
| `clean` | 113 | no known signature found — this is not a verification |
| `not_screened` | 0 | no deterministic extractor available, or extraction failed |

🔴 **5 of the 11 PDF-only papers cannot be read from their text layer at all**, and all of them should be acquired as XML/HTML rather than read from the PDF. A `clean` PDF is still a PDF: `deepdive_manifest` refuses it as a text surface, and a locator drawn from one has to be anchored to the page.

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
| PMID 42397075 | FT-010 | `absent` | — | — |
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
| PMID 33914858 | FT-044 | `pdf_only` | `clean` | PMID33914858_Repudi2021_OUP_browserprint.pdf |
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
| PMID 29808465 | FT-057, FT-122, FT-154 | `pdf_only` | `clean` | PMID29808465_Johannsen2018.pdf |
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
| PMID 35328751 | FT-111 | `absent` | — | — |
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
| PMID 28721938 | FT-121 | `absent` | — | — |
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
| PMID 21476439 | FT-130, FT-147 | `absent` | — | — |
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
| PMID 31618474 | FT-140 | `absent` | — | — |
| PMID 32214227 | FT-140 | `absent` | — | — |
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
| PMID 24008736 | — | `structured` | `clean` | PMID24008736_Tsai2013_PMC.xml |
| PMID 24330518 | — | `structured` | `clean` | PMID24330518_Ferguson2013.pdf, PMID24330518_Ferguson2013.xml |
| PMID 24456803 | — | `structured` | `clean` | PMID24456803_AbdelSalam2014_PMC.xml |
| PMID 24510053 | — | `pdf_only` | `SUSPECT` — PMID24510053_Gardenswartz2014.pdf: contains the C0 control U+0002 | PMID24510053_Gardenswartz2014.pdf, PMID24510053_Gardenswartz2014.txt |
| PMID 24932569 | — | `structured` | `clean` | PMID24932569_Aldaz2014.pdf, PMID24932569_Aldaz2014_efetch.xml |
| PMID 24949445 | — | `structured` | `clean` | PMID24949445_Szymanska2014_PMC.xml |
| PMID 25024751 | — | `structured` | `clean` | PMID25024751_Stewart2014.pdf, PMID25024751_Stewart2014.xml |
| PMID 25537520 | — | `structured` | `clean` | PMID25537520_Chang2014_PMC.xml |
| PMID 25649963 | — | `structured` | `clean` | PMID25649963_Tsuruwaka2015_PMC.xml |
| PMID 26302329 | — | `structured` | `clean` | PMID26302329_OKeefe2015_PMC.xml |
| PMID 26499798 | — | `structured` | `clean` | PMID26499798_AbuRemaileh2015.pdf, PMID26499798_AbuRemaileh2015_PMC.html |
| PMID 27495153 | — | `structured` | `clean` | PMID27495153_Elsaadany2016_PMC.xml |
| PMID 27551439 | — | `structured` | `clean` | PMID27551439_Chang2015_PMC.xml |
| PMID 28373548 | — | `pdf_only` | `SUSPECT` — contains the C0 control U+0002 | PMID28373548_EoC_PNAS2017.pdf |
| PMID 28749468 | — | `structured` | `clean` | PMID28749468_Janczar2017_PMC.xml |
| PMID 29390993 | — | `structured` | `clean` | PMID29390993_Rim2018_PMC.xml |
| PMID 30285739 | — | `structured` | `clean` | PMID30285739_Bonin2018.pdf, PMID30285739_Bonin2018.xml |
| PMID 30362252 | — | `structured` | `clean` | PMID30362252_Davids2019_PMC_2026-09-27.xml |
| PMID 30470736 | — | `structured` | `clean` | PMID30470736_AbuRemaileh2018_correction_PMC.xml |
| PMID 30746283 | — | `structured` | `clean` | PMID30746283_Ehaideb2018_PMC.xml |
| PMID 31275852 | — | `structured` | `clean` | PMID31275852_McBride2019.pdf, PMID31275852_McBride2019.xml |
| PMID 31315632 | — | `structured` | `clean` | PMID31315632_Chou2019_PMC.xml |
| PMID 32081867 | — | `structured` | `clean` | PMID32081867_Bacchelli2020_PMC.xml |
| PMID 33058734 | — | `pdf_only` | `SUSPECT` — uses statistical language (6 mentions) and contains none of < > ≤ ≥ ± × − | PMID33058734_Zeng2021.pdf |
| PMID 33195192 | — | `structured` | `clean` | PMID33195192_Chou2020_PMC.xml |
| PMID 33255508 | — | `structured` | `clean` | PMID33255508_Aldaz2020.xml |
| PMID 33916893 | — | `structured` | `clean` | PMID33916893_Aqeilan2021_PMC.xml |
| PMID 34204789 | — | `structured` | `clean` | PMID34204789_Kaluzinska2021_PMC.xml |
| PMID 34359949 | — | `structured` | `clean` | PMID34359949_Hsu2021_PMC.xml |
| PMID 35712340 | — | `structured` | `clean` | PMID35712340_Sukkar2022_PMC.xml |
| PMID 36498839 | — | `structured` | `clean` | PMID36498839_Lin2022_PMC.xml |
| PMID 37095367 | — | `structured` | `clean` | PMID37095367_Bayanova2023_PMC.xml |
| PMID 37501399 | — | `structured` | `clean` | PMID37501399_Yang2023_PMC.xml |
| PMID 37781246 | — | `structured` | `clean` | PMID37781246_KaluzinskaKolat2023_PMC.xml |
| PMID 37897534 | — | `structured` | `clean` | PMID37897534_Cheng2023_PMC.xml |
| PMID 37974179 | — | `structured` | `clean` | PMID37974179_Dong2023_PMC.xml |
| PMID 38161429 | — | `structured` | `clean` | PMID38161429_Battaglia2023_PMC_2026-09-27.xml |
| PMID 38355659 | — | `structured` | `clean` | PMID38355659_Akkawi2024_correction.pdf, PMID38355659_Akkawi2024_correction_PMC.xml |
| PMID 38542478 | — | `structured` | `clean` | PMID38542478_Chen2024_PMC.xml |
| PMID 38563965 | — | `structured` | `clean` | PMID38563965_Zeng2024_PMC.html |
| PMID 39101447 | — | `structured` | `clean` | PMID39101447_You2024_PMC.xml |
| PMID 39847501 | — | `structured` | `clean` | PMID39847501_Chen2025_PMC.xml |
| PMID 40191585 | — | `structured` | `clean` | PMID40191585_Robertson2025_PMC.xml |
| PMID 40263630 | — | `structured` | `clean` | PMID40263630_Wagner2025_PMC.xml |
| PMID 40349107 | — | `structured` | `clean` | PMID40349107_Aeran2025_PMC.xml |
| PMID 41090157 | — | `structured` | `clean` | PMID41090157_Hussain2025.pdf, PMID41090157_Hussain2025.xml |
| PMID 41124647 | — | `structured` | `clean` | PMID41124647_Zhang2025_PMC.xml |
| PMID 41562193 | — | `structured` | `clean` | PMID41562193_Druck2026_EuropePMC_render.pdf, PMID41562193_Druck2026_PMC.xml |
| PMID 41677633 | — | `structured` | `clean` | PMID41677633_Su2026_PMC.xml |
| PMID 42181696 | — | `structured` | `clean` | PMID42181696_Diaz2026_PMC.xml |
| PMID 42193054 | — | `structured` | `clean` | PMID42193054_Sapuppo2026_PMC.xml |
| PMID 42521212 | — | `structured` | `clean` | PMID42521212_Saravanan2026_PMC.xml |

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

**Accounting.** Rows: 119 corpus papers + 251 queued papers − 54 in both = **316** emitted. ✓ Entries: 182 resolved + 9 unjoined = **191** queue entries. ✓

*Not medical advice. This page describes file formats, not findings.*

