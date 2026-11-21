# ADV-138 route result: Sardi 2006 (Cell, PMID 17018285) was NOT obtained; one line and the item stays on the operator supply list (IT, 2026-11-21)

Hypothesis level; reference genotype class only; no dose, no recommendation; nothing here is medical advice. Question (ADV-138, from the RP-003 selection): does nuclear signalling of the ErbB4 intracellular domain REPRESS astrocytic differentiation (species, preparation, age, cell, endpoint; anything on WWOX or WW domains), as the premise of the class-NRG1 sign reading and of R3's P1 verdict needs.

## Route results (plain client, generic client name, no contact address, one request per URL, none repeated, no header spoofing)
| Route | Result | Status |
|---|---|---|
| Held bytes by PMID (`evidence_presence.py --pmid 17018285`; `git grep` of the PMID) | no manifest, no artefact; the PMID appears only in supply-list and checkpoint notes | none held |
| Europe PMC REST record (EXT_ID 17018285) | `inEPMC` N, `isOpenAccess` N, no PMCID, no PDF; abstract only | route closed: not open access |
| DOI landing `doi.org/10.1016/j.cell.2006.07.037` | redirect stub (about 3 KB, meta-refresh to the publisher's preference page) | no content |
| Cell Press full text and PDF URLs (`cell.com/fulltext/S0092-8674(06)01022-9`, the `showPdf` URL for the same PII) | HTTP 403 "Just a moment..." (Cloudflare challenge page) on both | STOP for that route, recorded, not bypassed |
| ScienceDirect article page for the same PII (reached from the DOI redirect) | HTTP 403, about 1.2 MB page with the publisher's text-and-data-mining reservation and a bot-check | STOP for that route |
Two or more routes failed: by the assignment's rule, one line and stop.

## What the abstract (Europe PMC record, already known to R3) says, and no more
"direct nuclear signaling by a receptor tyrosine kinase inhibits the responses of precursors to astrocyte differentiation factors"; after neuregulin-induced activation and presenilin-dependent cleavage the ErbB4 intracellular domain forms a complex with TAB2 and N-CoR, "binds promoters of astrocytic genes, repressing their expression"; "astrogenesis occurs precociously in ErbB4 knockout mice". Abstract level: embryonic multipotent neural precursors, mouse knockout; the species of each experiment, ages, n, endpoints, the knockout genotype (germline or conditional), and any mention of WWOX or WW domains are NOT readable from the abstract. The abstract does not mention WWOX.

## Effect on R3's P1 verdict and on the class-NRG1 sign premise
None. R3's P1 verdict ("enhanced astrogenesis in knockout organoids is incompatible with the release hypothesis") stays PROVISIONAL at abstract level, as written; the class-NRG1 sign premise (Wwox loss weakens PV-ErbB4 signalling) stays UNTESTED; IT59-Q01 stays open and still waits for a laboratory with an Erbb4 manipulation. This note adds a verified access result, not a datum.

## Next
The item stays on the operator supply list (`l_supply_state_sci_20261119`, `supply_sheet_adv087_sci_20261119`); nothing is proposed to the operator beyond what those lists already carry; no e-mail address was sent anywhere. Cost: about 15 minutes, no delegate, no spend.
