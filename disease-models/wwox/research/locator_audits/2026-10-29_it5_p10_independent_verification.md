# Independent verification of the supplement and EU-context probes (P10), 2026-10-29

Producer: scientist-d. Verifier: independent subagent against the live DSLD API v9 and the EU Open Data Portal files. Verdict: counts reproduce; low defects (thiamine display cap, availability-leaning phrase, EU licence evidence understated, weak salt-to-element matches); none touches a card-linked compound.

# P10 verification (scientist-b), 2026-10-28
Method: own live calls first (DSLD v9: ingredient-groups?method=factsheet&term=..., search-filter?q="..."&size=50 as the producer's script uses, browse-products?method=by_keyword; >=1.1 s spacing; EU files downloaded to own scratch dir, python -I). Producer tables read afterwards. No e-mail, no registration.
Note: ingredient-groups takes `term` (not `q`); with `q` it silently returns 0 hits.

| Claim | My live number | Verdict |
|---|---|---|
| DCA/dichloroacetic acid/sodium DCA: no match | search-filter quoted: 0/0/0; groups 0/0/0; browse-products by_keyword 0. (Unquoted "dichloroacetic acid" gives 48,219 hits = tokenised on "acid"; the producer's quoted-phrase method avoids this.) | SUPPORTED |
| thiamine supplement, 6 groups | search-filter 33,055 hits, sample 26/50 exact name. Factsheet returns 12 groups with thiamine in name/synonym (7 with synonym equal); catalogue itself records dsld_groups_total=13 for THIAMINE. "6" is a display cap (`[:6]` at catalog_build.py:572 and 1542), not a count | UNDERSHOOT as a count (6 vs 12-13); harmless if read as "first 6 listed"; the total (13) is stored. Group 2241 "Thiamin" is category Botanical in DSLD |
| alpha-lipoic acid groups 6878 + 8; thioctic acid synonym | groups 6878 and 8, both name-equal; 8,829 quoted hits; sample 50/50 by group, 42 by name (producer 42/50) ; "thioctic acid" is not a separate group, producer says synonym of the same two groups (its tsv 8,680 hits) | SUPPORTED |
| pyruvate group 1576; Ca/Na/K/creatine pyruvate separate | 1576 Pyruvate (3 synonyms) + 3664, 7924, 7818, 2912 separate; 169 hits; sample 19 exact (17 by name, 19 by group) | SUPPORTED (exact match to producer) |
| beta-hydroxybutyrate groups 6978, 6987 | both name-equal (56 and 2 synonyms); Ca/Mg/K/creatine salts separate groups; 430 hits; 49/50 exact (27 by name) | SUPPORTED |
| carnitine groups 7066 + 7533; levocarnitine 0 equal names | 7066 name-equal, 7533 "L-Carnitine" equal via synonym (also a Botanical-category 255 L-Carnitine); 4,405 hits, 6/50 exact; levocarnitine: 0 groups under factsheet, 2,993 text hits, 0/50 equal names | SUPPORTED. Note: the catalogue links "Levocarnitine" to groups 255 + 7533 through the synonym "L-carnitine" (matched_on), not through levocarnitine itself - correct, but the matched_on field is what shows it |
| CoQ10 groups 7126, 7127; ubiquinone/ubiquinol merged | 7126 and 7127 name-equal; ubiquinone and ubiquinol factsheet queries return the same two groups; 7,352 quoted hits; 50/50 by group. Catalogue additionally has 7134 "CoQ10" | SUPPORTED on groups/hits/merging. Sample counts DIFFER: producer 41 exact (41 by name, 0 by group); mine 50 exact (49 by name, 50 by group) for the same quoted query; total hits 7,352 equal. Sample order or label data changed between runs, so sample-based figures are not stable (LOW) |
| decanoic acid only via synonym of Capric Acid 2486 | factsheet: 2486 Capric Acid synonym-equal; 3291/6680 are 10-hydroxy-2-decanoic acid (partial, not equal); 7,241 text hits, 0/50 exact | SUPPORTED |
| triheptanoin 0 | search-filter 0, groups 0 | SUPPORTED |
| phenylbutyrate 0 | search-filter 0, groups 0 | SUPPORTED |
| TUDCA 46 labels, group 3564 | 46 hits, 46/46 exact by group, 11 by name; group 3564 | SUPPORTED (exact) |
| lithium 439 hits; group "Lithium" 3 ids | 439 hits; 8431 (mineral), 499 (Botanical), 7562 (non-nutrient); 50/50 by group, 47 by name | SUPPORTED (exact) |
| DSLD has no UNII/CAS/InChIKey | group _source keys: category, factsheets, groupId, groupName, nutrientInfo, synonyms; product _source: allIngredients(category, ingredientGroup, name, notes), brandName, claims, ... no identifier fields; no unii/cas/inchi string in any response | SUPPORTED, name-only is the correct label |
| API root CC0 + version | page shows "CC0 1.0 Universal (CC0 1.0)", url creativecommons.org/publicdomain/zero/1.0/, "Version: 9.4.0" | SUPPORTED |
| keys < 4 chars never matched ('ala') | catalog_build.py:1529 `len(k) >= 4`. Live: factsheet "ala" returns Alpha-Linolenic Acid (1029) and both lipoic groups as synonym-equal, so the homonym risk is real and the rule justified | SUPPORTED |

Caveat on sample counts: the "exact in sample" figures depend on the 50 hits returned first; the ones I re-derived (pyruvate 19/17/19, BHB 49/27/49, TUDCA 46/11/46, lithium 50/47/50, ALA 50/42/50, carnitine 6/6/1, thiamine 26/26/0, levocarnitine 0) all equal the producer's. Not every producer row was re-run.

## Ambiguity notes and over-reading
Notes on salt/form/enantiomer, ingredient-vs-product and "name-only" are correct against what I saw (e.g. Thiamin group 2241 category Botanical, L-carnitine 255 Botanical, Lithium 499 Botanical - DSLD category oddities the notes partly mention). The catalogue's `scope` string for the supplement category says "NAME-ONLY evidence ... not the compound's availability, dose, form or safety"; the tsv notes ("commonly sold", row Calcium pyruvate: "Salt form; commonly sold; 146 text hits") is the only phrase I found that edges toward availability. "Commonly sold" is an availability statement on 146 text hits, of which only 23/50 sampled labels name the ingredient. Low severity: reword to "146 text hits, 23 of 50 sampled labels name it". No efficacy or safety statements found in the DSLD rows inspected. "Lithium ... 'carbonate, orotate, citrate, aspartate, chloride listed under group names Lithium'" - not re-verified per salt.

## EU context probe
Files: api.datalake.sante.service.ec.europa.eu downloads answered 200 without key. data.europa.eu portal lists them as "EU Novel Food (Novel foods and food ingredients)" (id xt4uwrpbr87xhm7ta3ffaw) and "European Union Register on Nutrition and Health Claims" (id u3yjqnr7wx2gjkbqmajsya), both DG SANTE, modified 2024-08-13: CONFIRMED. Records: 6,570 novel food, 3,342 health claims (producer's counts match).

| Claim | Mine | Verdict |
|---|---|---|
| CoQ10 8 health-claim entries, all Non-authorised | 8, all Non-authorised Art.13(1) (11 if claim text also searched) | SUPPORTED. Also 1 Novel Food row with status "Not novel in food" (producer's tsv has it) |
| alpha-lipoic acid 9 | 9, all Non-authorised | SUPPORTED |
| carnitine 17 | 17 (16 Art.13(1) + 1 Art.13(5)), all Non-authorised; 11 Novel Food rows "Not novel in food" | SUPPORTED |
| thiamine 7 Authorised nutrient-function | 7, all Authorised, all Art.13(1). Spelling "thiamin" gives 5 further entries, all Non-authorised (producer lists them as a separate row) | SUPPORTED; the README's headline "thiamine 7 Authorised" omits that the "thiamin" spelling carries 5 Non-authorised combination claims (in tsv, not in README prose) - low |
| TUDCA / cannabidiol / benfotiamine 1 Novel Food each | 1 each, status "Novel food" | SUPPORTED |

Licence: commission.europa.eu/legal-notice_en (read today): "Unless otherwise indicated ... content owned by the EU on this website is licensed under CC BY 4.0", reuse policy = Decision of 12 Dec 2011. SUPPORTED. The downloaded records have no licence field (keys listed; none). SUPPORTED. BUT: the data.europa.eu portal catalogue records for both datasets declare licence CC_BY_4_0 (spdx CC-BY-4.0) on their distributions. So the producer's "default reading, not a dataset-specific statement" is more conservative than the evidence: there is a dataset-level declaration in the portal metadata (the notice also says "on this website", i.e. commission.europa.eu, not datalake). Defect LOW-MEDIUM (undershoot, safe direction): add the portal metadata as the primary source and keep the legal notice as corroboration. Not verified: whether the portal licence applies to every record (third-party/proprietary_data field exists in the health-claims records).

## Build effect
Committed catalog.jsonl.gz: 44,211 rows (same before/after); 'supplement' access category: 238 now (126 at dadbda7a^, +112, 0 removed): RECOUNT SUPPORTED. All 238 have strength name_only. Origin: 124 chembl_selected, 84 dgidb_only, 20 matrix_only, 10 openfda_unii_only. The 112 additions are mostly vitamins/minerals/salts (calcium/magnesium citrate, cyanocobalamin, pyridoxine, niacin, etc.) plus pyruvate, 3-hydroxybutyric acid, alpha-lipoic acid, thiamine HCl/mononitrate, lithium citrate, acetylcarnitine, decanoic/octanoic acid, ubiquinol.
Cards (card_links.json, 61 cards, 21 with links): only 3 card-link rows point to a supplement-flagged compound: CANNABIDIOL CAT:CHEMBL190461 (card EB-CBD-AX-01, groups 3397), LITHIUM CAT:CHEMBL1201333 (cards G01_lithium_gsk3 and Q-R-04, groups 499/7562/8431). Both were already supplement-flagged BEFORE P10 (in the 126), so the +112 touches no card-linked compound. Alpha-lipoic, CoQ10, carnitine, thiamine etc. flagged but not card-linked.
Looseness: some additions match through DSLD synonyms to element/mineral groups (e.g. "Disodium phosphate" -> group 8438 "Sodium", via DSLD's own synonym list - confirmed live; also listed under 2920 Sodium Phosphate). Name-only labelled correctly, but a salt carrying "supplement" via an element group is weak evidence. Low.

## Defects
1. LOW-MED: README licence reading for EU datasets understates evidence (portal declares CC BY 4.0).
2. LOW: "thiamine 6 groups" is a storage cap; true count 12-13 (stored in dsld_groups_total=13). Say "13 groups, first 6 listed".
3. LOW: "commonly sold" wording (Calcium pyruvate note) edges to availability.
4. LOW: salt-to-element-group matches (Disodium phosphate -> Sodium) inflate the 112.
5. INFO: README prose omits the thiamin-spelling 5 Non-authorised claims.

## Not verified
Per-label detail beyond the 50-hit samples; producer rows for the other ~50 query strings (only the requested ones re-run); DSLD website terms page (403 for the producer; I did not retry); portal licence applicability per record; whether sample order is stable over time (DSLD updates labels).
