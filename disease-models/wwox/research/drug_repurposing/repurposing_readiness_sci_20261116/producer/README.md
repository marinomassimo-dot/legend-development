# Producer output: repurposing-readiness sheets, first-pilot arms (SCI, 2026-11-16; non-canonical; not medical advice)

Abstract-level, not a safety review. Reference genotype class only. No recommendation, ranking, dose, schedule or route. Files: `sheets.tsv` (13 rows), `signals.tsv` (33 rows, at least one per agent).

## Method and limits (read first)
- Labels: DailyMed lookup pages by setid, read with WebFetch (default client, no contact address, no browser User-Agent). The fetch tool returns an extractor's excerpt, capped near 125 characters per quote. Consequences: (1) quotes marked `[fragment]` are cut; (2) quotes were NOT byte-checked against the label page, so a verifier should re-open each setid; (3) for several labels only characters 0-100000 were read (listed below).
- Abstracts: PubMed tools (search plus metadata). No full text opened. BBB sentences were searched narrowly; `not stated at abstract level` means not found in what was read, not absent from the literature.
- Repackager labels were used where they were first in the DailyMed result list (not the innovator label, except Ketalar, Spravato, Onfi). Label revision dates varied (some text says Revised 2021-2022). Ketalar is an anaesthetic label; carbamazepine is the extended-release label; phenytoin is the oral extended-release capsule label (the injection label was not read).
- Flags follow the source wording per the brief. Count by flag: red 11 (esketamine, zolpidem, eszopiclone, diazepam, clobazam, clonazepam, ethosuximide, zonisamide, carbamazepine, lamotrigine, phenytoin), yellow 2 (memantine, ketamine), none 0. `none` was never assigned; no `none` means nothing about safety.
- Phenytoin red rests on "may be fatal" in a Warnings sentence of the oral capsule label; no boxed warning appeared in that label text.
- Pediatric statement for lamotrigine and phenytoin: `none found`; the extractor returned text that did not look like a section 8.4 statement (indication-like and dosage-like), so it was not entered.
- Carbamazepine mechanism: `not stated`; the first label sentence is an animal observation and no retrieved abstract was read for the sodium-channel class. Memantine, clonazepam, clobazam, diazepam, lamotrigine: arm class comes from the brief; the sources give only the partial sentences shown.
- Some `mechanism_sentence`/`indications` cells have bracketed glosses `[...]` added by the producer to mark fragments or joins; the text outside brackets is the source's.

## Sources opened, per agent
Label = DailyMed `https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=<id>`.

| Agent | Label setid (read) | PubMed abstracts opened | Not reachable lawfully |
|---|---|---|---|
| memantine | 65c9e7bc-71f0-4113-8de1-4fcaa591735f (tablet) | 33744690 (BBB sentence, indirect); 38964146, 37593987, 31922720 opened, not used | none |
| ketamine | 46dab560-8ecd-4d92-8c92-6baa2310b09b (Ketalar) | 41869093 | none |
| esketamine | d81a6a79-a74a-44b7-822c-0dfa3036eaed (Spravato; chars 0-100000 of 150887) | none beyond ketamine review | none |
| zolpidem | 38c838a4-9943-445a-8e80-e823d56eeaa5 (chars 0-100000 of 108205) | none (search for a zolpidem review returned 0) | none |
| eszopiclone | bb972d36-4b2c-45ae-8504-3a16d352dd8b (chars 0-100000 of 103942) | 20945020, 31274695 | none |
| diazepam | 2f799120-0d08-47cd-8183-a98f0267c845 | none | none |
| clobazam | de03bd69-2dca-459c-93b4-541fd3e9571c (Onfi; chars 0-100000 of 131902) | 33541771, 31625159 (cannabidiol interaction papers; no sentence used) | none |
| clonazepam | 9a74ea97-1c00-4d96-a06f-81c183943dc6 | search only (35997362 etc. not opened) | none |
| ethosuximide | a4dbc665-4db1-4d0a-9630-5cd200ec4c82 | 28720615 (protocol abstract; weak mechanism source) | none |
| zonisamide | 53ecba6c-0de4-4e11-81d5-6deac79accd5 (chars 0-100000 of 105304) | 21967409; 30194563 opened, not used | none |
| carbamazepine | 726a127b-03b2-44e8-a63d-078b35e27525 (ER; chars 0-100000 of 104106) | none | none |
| lamotrigine | 70cd448a-2921-4c69-bdf2-5a6ce883bd07 (chars 0-200000 of 218457) | 42417183 | none |
| phenytoin | 46d5c0d1-a97b-46d9-8cf4-994780673337 (ER capsule; chars 0-100000 of 101991) | none | none |

No reCAPTCHA, interstitial or login was met. DOIs of abstracts used: 33744690 10.1016/j.ejmech.2021.113338; 41869093 10.7759/cureus.103774; 20945020 10.1590/s1516-44462010000300014; 28720615 10.1136/bmjopen-2016-015380; 21967409 10.1517/14656566.2011.622268; 42417183 10.1111/dom.71053. Source of abstracts: PubMed.

## Not done
No PubMed review per agent for BBB or class mechanism where the label was silent (clonazepam, clobazam, carbamazepine, lamotrigine, phenytoin, zolpidem, eszopiclone, ethosuximide, zonisamide). No second route for any absence claim. No verification pass.
