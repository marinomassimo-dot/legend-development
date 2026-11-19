# Real-browser validation of the public page (2026-11-19)

Non-normative record. Browser: `repurposing_view.py browser` resolves `/snap/chromium/3583/usr/lib/chromium-browser/chrome` (Chromium 157.0.8103.38; headless and DevTools start in 0.5-1.8 s, temporary profile per run, no sandbox-bypass flag). The other candidates fail as listed by the probe: the snap wrapper ("cannot track application process") and revisions 3593/current (GLIBC 2.43 needed, the host has 2.39). "No browser here" was therefore wrong; the probe's line 2 names the working one.

Scope: the five shareable editions (en, it, fr, es, de) as built in the working tree identical to `development/main` at the time (view files unchanged by later landings).

| Check | Method | Result |
|---|---|---|
| Layout at 360, 390, 768, 1280 px and A4 print, 129 measurements per edition | `repurposing_view.py viewports --source shareable --out <edition>` | 0 overflow in en, it, fr, es; **de: 1** (`print_first_screen` 813 px against A4 794 px: the kind chips of the compound lists could not wrap). Fixed in `view/assets/curated.css` (print rule after the base rule); re-measured on rebuilt pages: 0 overflow in all five; regression `RealViewports.test_no_edition_overflows_the_a4_print_width_in_any_scenario` |
| Language selector, filters, search, comparison, details (390 and 1280 px, each edition, own temporary profile) | Cdp script over the page: `interaction_table.json` | selector 5 links; thread filter 39 -> 11 -> 39 after reset; search ISRIB 1 result; comparison view holds both card ids; a details element opens on click; 1 intentional original-language marker on each non-English page, 0 on en; no error |
| Scientific qualifications reachable | text search then opening the ancestor details, element visibility and size | F03 (outside details), INV-04 (inside an open details) and INV-09 (inside a closed details, visible once opened) are present in en, fr and de at 13.76 px; the first screen carries the research-preview, not-medical-advice and limited-source notices (screenshots) |
| Evidence | `browser_validation_20261119_evidence/` | interaction table, two screenshots (fr 390 px, de 1280 px), the German viewport table before the print fix |

Limits: emulated device metrics, not a physical phone; one engine (Chromium); the interaction pass is a scripted selection of controls, not exhaustive; the live online pages were checked for byte identity by IT, not re-driven here; the print fix needs the views and package to be regenerated before it is online.
