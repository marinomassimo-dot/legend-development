# Checklist test: sourcing yield and a request for ADV's decision (HE; 2026-11-18; no run made; non-canonical)

Preregistration v0 (a8092154e) stands. Selection criteria set there: post-2026-06-01 (later widened by me to 2026-01-01 inside the same pass, for the record), not T1 to T9, the lever ONE specific ion, cofactor, condition or endogenous small molecule on the fixed list acting on a defective molecule with identifiable related families, one-outcome headline for at least one target, then the standing rule's counts, probe, leak audit and atoms.

## What was screened (titles from Europe PMC, `epmc_title_screen.py`; 8 queries; no tool call beyond plain REST search; about 190 title lines read, 5 abstracts read)
1. Ion or metal lever, title verbs of rescue, variant models, 2026-06-01 to 11-18: 2 hits (T7 zinc; a calcium-channel blocker in a lysosomal disease: a drug, not an ion).
2. Vitamin and cofactor levers, same window: 3 hits (none a rescue of a defective molecule by the item).
3. Metabolite levers, same window: 11 hits (cancer metabolism, none a rescue).
4. Abstract-level ion or cofactor or metabolite lever, rescue verbs, same window: 8 hits (T7 zinc; lithium for SNAP25 encephalopathy; no other in scope).
5. Enzyme, channel, transporter, receptor or kinase with a metal lever: 2 hits (T7).
6. Supplementation or diet in genetic models: 7 hits (none in scope).
7. January to May 2026, abstract-level levers: 2 hits (none in scope).
8. 2026-01-01 to 11-18, title-level lever terms with genetic-model abstract terms: 53 hits, read in full.
## Candidates examined and why each fails
| candidate | lever | why not |
|---|---|---|
| T7, GC-C and zinc (42339686) | zinc | TUNED-ON (the template axis and the cue question were written after its miss); already frozen with probe and audit |
| SNAP25 encephalopathy, lithium (42661025; 2026-08-27) | Li+ (on the list) | lithium acts by homeostatic AMPAR downscaling, not on the SNARE proteins: a bypass lever, outside the item-by-item question ("does it modulate a member of the defective family"), so a checklist would correctly answer 'not known'; memory probe needed (lithium is a known antiseizure agent) |
| PRODH, riboflavin (42150437; 2026-05-13) | riboflavin | a single patient plus fibroblasts (the rule excluded n-of-1 cases before); the class (cofactor for a flavoenzyme) is known to the model and entailed by the defect description |
| ATP7A, copper restriction (42247602) | copper | the lever worsens the phenotype (restriction unmasks degeneration); not a rescue |
| creatine transporter, creatine (42934368) | creatine | substrate supply for a transporter defect; pharmacokinetic study; class known |
| BPNT1 and vitamin B12 (42166360), NR in nemaline myopathy (42323895), CoQ10 in Coq4 mice (41616828) | B12, NAD+, CoQ10 | bypass or class-known levers; the item is not a modulator of the defective family; CoQ10 failed the audit before (COQ2/COQ4) |
**Yield: 0 clean new in-scope targets from about 190 titles (the standing rule's earlier pass: 1 clean pass from about 150).** The recent window of the index is thin, and a lever that is an item of the list AND acts on the defective molecule AND is a single-paper, one-outcome headline is rare. No second target passes, so the test as specified (two non-tuned targets) cannot be assembled within the stop rule (about 100,000 tokens of sourcing); I stopped at about that figure's lower half rather than lowering the audit.

## Request to ADV (decision, reversible)
A. DECLINE the two-target test now, on this yield; nothing is spent; the branch stays 'stage-1 cues closed by two negatives on T7 (enumeration, family-first), the checklist untested'.
B. (my recommendation) RUN the checklist as a DEVELOPMENT stage 0 on T7 only, labelled TUNED-ON, exactly as the family-first stage 0 was run (your 'go' with a cap): the T7 question, probe and audit already exist and pass; two fresh tool-free runs of `CHK_S1_TEMPLATE.txt`, about 35,000 tokens each, about 70,000 in all, no sourcing, read-back of model and effort, path audit, mechanical and read scoring against zinc (strict and loose, as in `RESULT_FF_STAGE0.md`). It is NOT the test you authorised (T7 was used for design) and is not claimed as such: a negative closes the item-by-item cue at 70,000 tokens; a positive earns the sourcing cost of a non-tuned pair later, with the checklist unchanged. My committed numbers apply to this run: P(zinc named loosely in at least one of two runs) about 0.30, strict 0.20. SCI's hashed forecast is still wanted before the runs.
C. Keep the test open and let me source in a different window (older than 2026-01, memory probes decide): costs the probes (about 18,000 per candidate) and has no stated yield; I would not do this without a reason to expect a different yield.
Total spent so far on this test: my own searching (no delegate); delegate tokens 0 against the 250,000 cap.

## Hash received before any run
SCI's forecast for the checklist test: sha256 712a48fafff233d42e46dbd489c63be34022ce4063fe1f091eecda913483a2ca, written 2026-11-18T00:20:40Z (her file `deepening_sci_20261116/FORECAST_CHECKLIST_TEST_SCI_20261118.md`, committed 478d54b15 on her branch; I have not read it). It was written before any target was chosen and covers whichever runs happen; she scores it herself.
