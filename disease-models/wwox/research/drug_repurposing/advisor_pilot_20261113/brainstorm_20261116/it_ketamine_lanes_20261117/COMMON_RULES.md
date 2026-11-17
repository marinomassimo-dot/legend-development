# KDS lanes B2, B3, B5, E, C: rules every package follows (IT; 2026-11-17; non-canonical; not medical advice)

Written for: the delegate that reads this file. You are a producer (sonnet, medium) for ONE package; a different context verifies you blind afterwards. Do not start agents.

## The input under audit
Complete original (read it whole before your package; do NOT rely on any summary): `/home/desktop/legend-development/files/operator_inputs/KETAMINE_REPORT_OPERATOR_INPUT_20261117.md` (sha256 7c6a71956c43815679aaa394f98e521a57c011c6852a288158fc0ba1f90fa2e5). It is a synthesis by an unknown pipeline: an input to audit, NOT evidence. The programme record naming claims K1 to K14: `/home/desktop/legend-development/.claude/worktrees/adv-ket/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/ketamine_deep_adv_20261117/KDS_PROGRAMME_ADV_20261117.md`.

## Hard rules
* Reference genotype class only (WWOX loss of function, WOREE/DEE28 class). No individual-level record is sought or written. No outreach of any kind to registries, authors, journals or services; no e-mail address, no contact parameter in any request. Never send any person's e-mail address to a service.
* No dose, no schedule, no recommendation for or against any use of any drug. If a source states a dose or regimen, record it ONLY as a descriptor of what that study did (units as stated), never as guidance. Nothing here is medical advice; therapeutic questions belong to a treating clinical team.
* Plain documented routes only, one request at a time, no API key, no spend: PubMed/PMC through the PubMed tools you have, Europe PMC REST (europepmc.org/rest), PMC article pages, publisher open-access pages. A reCAPTCHA, Cloudflare, proof-of-work or interstitial page is a STOP for that source: record "access blocked" with the URL and move on; never bypass. No browser-agent spoofing.
* **Check the bytes.** For every full-text route: save the retrieved file under your `sources/` folder (name it PMID<id>_<FirstAuthor><year>_<route>.<ext>), then confirm it is the article and not an error body or a landing page (title and a known sentence present; size; first lines). Record per source: route, URL, bytes, sha256 (`sha256sum`), what you checked, depth reached (abstract / partial full text / complete full text). A source whose bytes you did not check is "not read".
* Quotes are VERBATIM from the bytes you hold, with a locator (section or table or figure and, for XML, the element or paragraph order). If you cannot quote it, you did not read it.
* Label every statement DATO (stated by the source, with quote and locator), INFERENZA (your reasoning from DATO), IPOTESI (a guess), or TRANSFER (from another species, age, disease or preparation). A transfer is never promoted to a finding.
* Report negatives and unchanged results. Report absence only with the routes searched and the exact query strings (and counts returned). An absence claim needs two routes.
* Harms beside every benefit. Registered a funding source or conflict where the paper states it. Report what the paper does NOT state (denominator, randomisation, blinding, responder definition, follow-up) as 'not stated'.
* Answer first, then evidence. Keep every output a table or a short list of labelled statements; no prose padding.
* Do NOT edit any file in the git repository. Write ONLY inside your package folder under `/tmp/it56_ket/<package>/` (create `sources/` for the bytes). No git commands that write.
* Final message back to the caller: one paragraph (what you answered, what you could not, access blocks, the file list). The tables are in your files.

## Output contract (all packages)
1. `REPORT.md`: answer-first per question asked in the package brief; per claim K tested: verdict in {SUPPORTED, PARTLY SUPPORTED, NOT SUPPORTED, UNVERIFIABLE (why)} with the checking route; evidence table (study, design, n, endpoint, result, locator, quote); what is not stated; limits.
2. `SOURCES.tsv`: pmid, citation, route, url, bytes, sha256, depth, check_done.
3. `SEARCHES.tsv`: route, exact query string, date, count returned, how many opened, why others were not.
