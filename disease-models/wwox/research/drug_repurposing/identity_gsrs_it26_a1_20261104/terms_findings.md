# G-SRS terms findings (verifier, 2026-11-04)

## Decisive text: the site's own Licensing page (found by a non-plain-fetch route)
The footer of the SPA links "Licensing" (route `/licensing`, lazy chunk 348 of the Angular bundle). The chunk is a static JS file, fetched from
https://gsrs.ncats.nih.gov/348.7659a7e42e0b2863.js (chunk id taken from https://gsrs.ncats.nih.gov/main.7bf32f449a289080.js and https://gsrs.ncats.nih.gov/runtime.e1e9cf78f49059b0.js). Verbatim page text:

- Heading: "Licensing GSRS"
- "Unless otherwise noted, the data provided by GSRS is public domain and made available with a Creative Commons CC0 1.0 Universal dedication. Under CC0, NCATS has dedicated the work to the public domain by waiving all rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission."
- "The content, documentation, code, and related materials provided by GSRS is licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License."
- "Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied."

## Corroboration
- https://precision.fda.gov/uniisearch (FDA UNII search page, HTTP 200): "UNIIs are generated based on scientific identity characteristics using ISO 11238 data elements. UNII availability does not imply any regulatory review or approval. Synonyms and mappings are based on the best public information available at the time of publication." Offers "Download substance data".
- https://github.com/ncats/gsrs-play : GitHub API license field Apache-2.0 (LICENSE file in repo); NOTICE (https://raw.githubusercontent.com/ncats/gsrs-play/GSRS_DEV/NOTICE) concerns only JSDraw. gsrs-spring-starter, GSRSFrontend and the other ncats/gsrs-spring-* repos carry no LICENSE file at the root (license field null, raw LICENSE paths 404); README of gsrs-spring-starter (https://raw.githubusercontent.com/ncats/gsrs-spring-starter/master/README.md) has no terms, rate-limit or data-use text.
- Peryea et al. NAR 2020 (already cited by the producer): public domain statement.
- The public API root https://gsrs.ncats.nih.gov/api/v1/ returns a JSON list of resources (substances, names, codes, ...); no swagger (https://gsrs.ncats.nih.gov/v3/api-docs and /swagger-ui/index.html return 404).

## Routes that failed or gave nothing
- https://gsrs.ncats.nih.gov/about and /ginas/app/beta/about: SPA shell only (no text in static HTML).
- FDA pages www.fda.gov/.../fda-global-substance-registration-system-gsrs, .../global-substance-registration-system, .../unique-ingredient-identifiers-unii, .../website-policies: HTTP 404 (guessed URLs, not confirmed to exist).
- https://ncats.nih.gov/disclaimer: HTTP 403 to a plain client (the NCATS general disclaimer linked from the footer was not read).
- web.archive.org: availability API gave a snapshot URL for the root only; a query for /licensing returned 429 and was not retried (politeness). Archived pages were not read.
- No robots file, no stated rate limit, no automated-access or attribution clause was found anywhere (not found is not the same as absent: the NCATS disclaimer and the privacy notice were not read; the privacy notice source in the frontend repo was grepped for automat/robot/scrap/rate with no hit).

## Conclusion
(1) Automated low-rate API reads of public names: nothing read forbids them; the Licensing page grants copy/modify/distribute "all without asking permission"; no rate limit is published. Keep the 1.5 s politeness. Basis is the CC0 dedication plus absence of a stated restriction, not an explicit API-use clause.
(2) Committing derived values (UNII, matched name, SMILES) in a public repository: permitted by the CC0 1.0 dedication quoted above ("distribute ... even for commercial purposes"). No attribution is required by that text (attribution is still good practice). Caveats: "Unless otherwise noted" (a per-record exception was not looked for); the NCATS general disclaimer was not read; FDA's note says UNIIs imply no regulatory review.
The producer's gap ("terms page not read") is closed for the Licensing page; it can be stated as read, with the route (static Angular chunk) recorded.
