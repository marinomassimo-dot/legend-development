# GluN2B-site follow-up (SCI, 2026-11-16; non-canonical; not medical advice)

Abstract-level, not a safety review. Files: `sheets_glun2b.tsv` (3 rows), `signals_glun2b.tsv` (6 rows). No recommendation, ranking, dose, schedule or route.

Sources opened (PubMed tools; abstracts only, no full text). DailyMed API (default client) returned 0 results for ifenprodil and radiprodil; Ro 25-6981 was not queried (research compound). Nothing was unreachable lawfully.
- ifenprodil: 39067562 (DOI 10.1016/j.ejphar.2024.176860), 38794209 (DOI 10.3390/ph17050639).
- Ro 25-6981: 42117259 (DOI 10.1111/jnc.70456), 39067562.
- radiprodil: 42596612 (DOI 10.1111/bph.70630), 42470359 (DOI 10.1002/epi.70346), 42651828, 41188625, 38794209. A search for a radiprodil paediatric safety/tolerability trial returned 0 hits.

Flags: yellow 2 (ifenprodil, radiprodil), none 1 (Ro 25-6981), red 0. Both yellows rest on one sentence that names extrapyramidal effects for many NMDA receptor antagonists in general (PMID 38794209); it does not name these agents, so the flag is a higher-flag-in-doubt choice. The same abstract says "low side-effect profiles" for ifenprodil and radiprodil. `none` for Ro 25-6981 means nothing was stated in two abstracts, not that it is safe.

Other notes: approved indications are `none found` (ifenprodil, Ro 25-6981) and `no approved label found` (radiprodil); I did not search for ex-US approvals of ifenprodil. The radiprodil development-stage sentence (PMID 42470359: seizures and other symptoms associated with GRIN-related neurodevelopmental disorder, tuberous sclerosis complex, and focal cortical dysplasia type II) sits in flag_basis in the sheet because the sheet has no development-stage column. Held potency numbers were not used. Mechanism sentences for the two tool compounds are the abstracts' sentences naming them as GluN2B inhibitors/antagonists, not binding-site statements. Abstract text is as returned by the PubMed tool; not byte-checked.
