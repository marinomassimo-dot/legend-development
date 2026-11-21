# SEARCH_RECORD - Ih-blocker effect on resting Rin, juvenile rodent L2/3 pyramidal (IT, 2026-11-21)

Producer: model sonnet, effort high (as stated at dispatch). Pre-registration: `SO_before_search.md` (written before the first retrieval call; Addendum 1 written after the first-pass strings and before any citation list was pulled). Clients: a small Python (urllib, run with `python3 -I`, User-Agent "legend-literature-client"), `pdftotext`, and the PubMed tool of the session. No key, no e-mail, no mailto, no contact in any header, no browser-header spoofing, zero spend, no agent started. Call log (552 logged HTTP calls) and pulled JSON/XML are in scratch `/home/desktop/.claude/jobs/6a8c1a55/tmp/data/` (not repository files). Full texts: `/home/desktop/legend-development/files/fulltext/ih_rin_it_20261121/`.

## 1. Strings (route R1 and R2)

PubMed tool (E-utilities through the session tool), two calls, both 0 hits:
- `(HCN OR "h-current" OR ZD7288) AND "input resistance" AND ("layer 2/3" OR "layer II/III") AND (juvenile OR postnatal)` -> 0
- `ZD7288 AND "layer 2/3" AND pyramidal AND "input resistance"` -> 0
(PubMed read "layer 2/3" as a phrase against All Fields; the 0 is a query defect of the phrase with a slash, not an absence.)

Europe PMC REST `search` (resultType=lite, page size 60 to 1000), hit count read before screening; `hit` = hitCount:
| tag | hits | string (abridged; full text of the string is in the call log) |
|---|---|---|
| e1 | 2 | ABSTRACT: ZD7288/HCN1/h-current AND "layer 2/3" AND "input resistance" |
| e2 | 66 | (ZD7288 OR HCN1 OR h-current) AND "layer 2/3" AND "input resistance" AND (juvenile OR postnatal OR P14 OR P15) AND pyramidal |
| e3 | 22 | TITLE_ABS: Ih terms AND layer 2/3 / supragranular AND neurons AND cortex |
| e4 | 73 | TITLE_ABS: HCN terms AND development/postnatal/maturation AND cortex AND pyramidal/neurons |
| e5 | 190 (first 60 returned and screened) | TITLE_ABS: HCN1/HCN2 AND knockout AND cortex/pyramidal |
| e6 | 13 | TITLE_ABS: ZD7288/cilobradine/zatebradine/ivabradine AND layer 2/3 / supragranular / superficial |
| e7 | 26 | blocker AND layer 2/3 AND "input resistance" AND P13..P17 / postnatal-day strings, HAS_FT, MED |
| f1 | 54 | ZD7288 AND layer 2/3 AND pyramidal AND mice/rats AND OPEN_ACCESS, MED |
| f2 | 30 | cilobradine/zatebradine AND cortex AND pyramidal, MED |
| f3 | 31 | Hcn1 knockout AND layer 2/3 AND "input resistance", MED |
| f4 | 104 | Hcn2 knockout AND neocortex AND pyramidal, MED |
| g2 | 15 | ZD7288 AND layer 2/3 AND P13..P17 strings AND cortex, OPEN_ACCESS, MED |
| g3 | 36 | ZD7288 AND layer 2/3 AND (sag OR Ih) AND rat, OPEN_ACCESS, MED |
| h1 | 15 | TITLE_ABS: Ih terms AND layer 2/3 / supragranular / superficial AND rat/mouse/slices AND intrinsic/resting/input resistance, MED |
| pp | 9 | same family AND SRC:PPR (preprints) |
| w16, w16b, g1 | 1, 7, 1 | targeted look-ups (Wang 2016 reference; the L2/3 HCN preprint title) |
Three exploratory strings (qq*) with 58, 41 and 27 hits were superseded by f1-f3 (same terms plus SRC:MED) and not screened separately.

## 2. Citation graph (route R3, OpenAlex public, no key) and Europe PMC citations

Seeds named in `SO_before_search.md` and its Addendum 1: Kalmbach 2018 (W2899419202, 221 listed), Yang 2018 Ih development in mouse PFC (W2800215535, 30), Atkinson and Williams 2009 postnatal dendritic integration in rat pyramidal neurons (W2022580386, 76), Developmental Changes in HCN Channel Modulation of Layer 1 Interneurons 2018 (W2790652003, 12), Sun-Luhmann-Kilb 2012 resonance in immature mouse neocortex (W2101289389, 19). The Nolan 2003 seed named in the SO was not pulled (a seed named is not obliged); the Fucke thesis had 0 citing works at the earlier package and was not pulled again.
- OpenAlex `filter=cites:<W>` pulled 212 / 27 / 70 / 11 / 18 works. Union 314 unique works, of which 184 carry a PMC id.
- Failure F1: cursor paging returned HTTP 401 on page 2 for Kalmbach 2018 (cursor beyond the first 200). Worked around, not bypassed, by year-sliced requests (publication_year 2005..2026, 22 calls): 212 of the 221 listed works were retrieved (9 not returned).
- Backward references (`referenced_works` resolved by `filter=openalex:` in batches of 50): Kalmbach 88 of 89, Yang 36 of 36, Atkinson 57 of 57. These lists were title-scanned only (juvenile or L2/3 Ih in a title) and were not full-text screened; the titles are dominated by L5 and CA1 dendritic Ih and by reviews; no title of a juvenile L2/3 Ih experiment appeared.
- Europe PMC `/MED/<pmid>/citations` (pageSize 1000) for Kalmbach (178), Yang (25), L1 interneuron paper (9), Atkinson (44): 0 MED records absent from the OpenAlex union (second view agrees; preprints in that list not opened).

## 3. Full-text screen (a screen is not a read)

PMC bodies fetched by E-utilities efetch (`db=pmc`, retmode=xml): 476 distinct PMC ids (the first-pass Europe PMC hits with a PMC id plus the 184 OpenAlex-union works with a PMC id), 478 calls, 477 x HTTP 200 and 1 x HTTP 429 (PMC7100647; retried once after the batch, HTTP 200, no HCN text). A regex screen over the tag-stripped body counted: blocker or HCN1 knockout terms (ZD7288, cilobradine, zatebradine, ivabradine, Hcn1-/-), layer 2/3 or supragranular, age tokens (P12-P18, postnatal day 12-18, 2-3 weeks old), Rin terms. Works with blocker and layer hits were opened as text snippets (ZD7288 lines, age lines, Rin lines); that is "snippet-level", not a Methods and Results read.
Read in full text (Methods, Results, captions): two preprints (C02, C03, receipts staged) and the ZD7288 paragraph of the Fucke thesis (C01, already receipted in the IT48-Q01 package). Snippet-level: C04 to C08. Abstract only: C09 to C13. Full texts of candidates opened: 3 in Methods and Results (far under the stop-rule ceiling of 40, because the screen found no candidate worth a Methods and Results read).

## 4. Routes that failed or were limited (results; nothing bypassed)

- F1: OpenAlex cursor paging 401 on page 2 (Kalmbach), see section 2.
- F2: Europe PMC `fullTextXML` returned HTTP 500 for the preprint id PPR730965 and for PMC9576169 (Routh 2022); not retried in a loop. The preprint was reached on the open bioRxiv `.full.pdf` URL (HTTP 200, no header set), the Routh record stayed abstract-only (efetch body 9 kB).
- F3: PMC held the abstract only (author-manuscript stub) for Song and Moyer 2018 (PMC5866461) and Routh 2022 (PMC9576169); the journals' full texts were not reached.
- F4: no captcha, 403 or challenge page on any route. No OpenAlex `search` call was made (the earlier package met HTTP 429 on it).
- F5: Europe PMC returned only the first 60 of 190 hits of string e5 (page size 60 by my choice); the rest were not screened. 130 of the 314 OpenAlex-union works have no PMC id and were title-scanned only. Preprint-only citing records were not opened.
- F6: PubMed tool strings with a slashed phrase ("layer 2/3") returned 0 hits twice; Europe PMC phrase search did resolve it.

## 5. Papers behind publishers (supply list, not counted as read)

Song and Moyer 2018 (PMID 28978762), Routh, Brager and Johnston 2022 (PMID 36129187), Wang, Dufour, Valiante and Carlen 2016 Int J Neural Syst (PMID 27464853), Huggenberger, Vater and Deisz 2009 (PMID 18775844), Sun, Luhmann and Kilb 2012 (PMID 22748148; age P0-P7, outside the window anyway), Kalmbach 2018 Methods for the mouse age (PMC text present but age not found by regex; a hand read of its Methods was not done).

## 6. Absence statement

Two routes (Europe PMC and PubMed strings; OpenAlex plus Europe PMC citation graph with a PMC full-text regex screen) found no source that meets all four FOUND rules (rodent neocortical L2/3 pyramidal, P13-P17 stated, blocker or HCN knockout with a Rin/conductance/holding-current number, read in full text). This is not proof of absence: the screen covers PMC-body text only, the citation seeds were chosen from the first pass, and papers whose Methods do not use the layer-2/3 or P-numbered phrasing of the regex would be missed.
