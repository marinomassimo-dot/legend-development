# Brief (producer) — IT48-Q01 juvenile half, third route: forward citations (2026-11-21)

Model/effort to state in the dispatch: sonnet, effort high; read back with session_model_census.py.

Question (IT48-Q01, second half; IT49-Q09 as a side output only if a source falls out):
Is there any measurement of the Ba2+-sensitive share of resting (or input) conductance in layer II/III
pyramidal neurons of rodent neocortex at about P13-P17, any cortex, any laboratory?

Already done, do not repeat (read first):
- advisor_pilot_20261113/brainstorm_20261116/it_it48q01_20261117/RESULT.md, SEARCH_RECORD.md, measurements.tsv, human_access_list.tsv
  (28 PubMed + 43 Europe PMC strings, screen of 210 PMC ids: NOT FOUND for P13-17; adjacent ages P26-51 and P28-42 only)
- kir2_drugname_sci49_20261112/output/ba_share_p13_p17.tsv (two string sets, not found)

New route (the only difference): citations, not strings.
1. Seed set = papers that report a Ba2+ experiment in cortical L2/3 pyramidal neurons at any age:
   Xue 2014 (V1 L2/3, P14-23, 50 uM), Nguyen 2024 (mPFC L2/3), Goldberg 2011, Day 2005, Routh 2022,
   the 2026 Fmr1 A1 preprint, WNK3 2022 (36311015), plus rows R01-R13 of measurements.tsv.
2. For each seed: backward references and forward citations (OpenAlex cited_by and references via the
   public API without any e-mail or key; Europe PMC citations endpoint). Zero spend, no contact address
   sent anywhere (the operator's e-mail must never go to a service).
3. Screen the citing/cited set for a Methods or Results statement with an age window overlapping P13-P17
   plus Ba2+ (or BaCl2) plus L2/3 or layer 2/3 pyramidal; read the Methods and the relevant Results lines of every
   candidate in full text (no abstract-level verdict).
4. Record every route that failed (captcha, 403, 429) as a route result; do not bypass it; use another route.
   An absence is reported as two-route, never as proof.

Output (producer): table of candidates with age, species, area, layer, Ba2+ concentration, measure, value,
locator (verbatim, with FULLTEXT_READ_RECEIPT where a full text is read), read depth; plus SEARCH_RECORD.
A blind verifier (different delegate, own strings) re-derives the decisive rows. Answer first, limits stated.

## Dispatch terms (added at dispatch)

- Role: producer. Model sonnet, effort high (stated; the orchestrator reads it back with session_model_census.py). Do not start agents.
- Output folder (write only here): disease-models/wwox/research/drug_repurposing/it48q01_forward_citations_it_20261121/output/
  Files: RESULT.md (answer first, then limits), candidates.tsv, SEARCH_RECORD.md (every call: route, seed, query or URL, result count, failures), receipts/ (staged FULLTEXT_READ_RECEIPT JSON files only; do NOT run fulltext_receipts.py record, the integrator records them).
- Full texts go under /home/desktop/legend-development/files/fulltext/it48q01_fwd_it_20261121/ (git-ignored). This worktree has no files/ folder.
- The route is citations, not strings. Count and name each seed's citing and cited set; screen titles/abstracts only to choose what to open; a verdict on a paper needs its Methods and the Ba2+ Results lines read in full text. Abstract-level is stated as abstract-level.
- A source you cannot reach (captcha, 403, 429, 500) is a route result: record it, use another route (OpenAlex works API, Europe PMC REST citations and references, PubMed elink without e-mail, bioRxiv/PMC OA copies). Never bypass a captcha, never spoof a browser header.
- Never send any e-mail address or personal detail to any service (no mailto parameter, no contact in a User-Agent; use a generic client name).
- Pre-register before searching (SO_before_search.md): what counts as FOUND (age window overlapping P13-P17 for rodent neocortical L2/3 pyramidal cells; Ba2+ or BaCl2; a share, a conductance fraction, or numbers from which one derives); what counts as a share versus a current density; what a negative result will and will not say.
- Report: where the first candidate is found or after the seed set is exhausted, whichever is first; then stop. If nothing is found, state the number of seeds, citing and cited papers screened, and the papers behind publishers (list for the supply list).
- Persist your report in the output folder; the orchestrator reads the files, not your chat reply.

## Conditions from ADV (approval 2026-11-21, applied at dispatch)

- Pre-register in SO_before_search.md, before any retrieval: the decision this question changes (whether the first INV-18 arm needs the K2P or high-Ba2+ step, ladder step 2b, or reduces to the Kv7 spiking-range arm) and the rejecting observation (what finding would make the answer "no juvenile share exists in the retrievable literature" versus "a share exists at a different age/concentration only").
- Every row of candidates.tsv carries, from the first pass: preparation (slice, acute/culture, temperature), age (P13 to P17 or the stated window), species, cortical area, layer, cell type, Ba2+ concentration, and the denominator (share of resting conductance, of input conductance, of holding current, or a current density; say which).
- A value that sits only in an Extended Data or supplementary figure is recorded as "figure-only, unread" unless you measure the figure geometry (state how); never as a number you did not read.
- A challenge page (captcha, bot check) stops that route; record it in SEARCH_RECORD.md and move to another route.
- IT49-Q09 side output (which Kir2 subunits carry the neuronal Ba2+-sensitive current in cortical L2/3 pyramidal neurons): note any source that falls out of the citation screen in a separate file `kir2_subunit_leads.tsv`; do not search for it separately.
