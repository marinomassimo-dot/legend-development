# DREAM-2: a light Dream pass inside the session close (2026-11-08)

Non-canonical working note. Not medical advice. Public edition, reference genotype class. Zero spend; the Dreams service was not used. Pre-registration: [`PRE_REGISTRATION.md`](PRE_REGISTRATION.md) (commit b0fe3049). One disclosure: a first exploratory run of the helper on the repository preceded the pre-registration and is where the D3 gap and the NB-1 case came from.

## What LEGEND does now that it did not

* `legend-dream` (skill) is step 4 of `legend-session-self-eval`, routed from `CLAUDE.md` section 2, `SKILLS.md` and `ARCHITECTURE.md`. It runs only if something material changed; `dream_pass.py quiet` ends it in one line otherwise.
* `framework/scripts/dream_pass.py` (stdlib, writes nothing) selects inputs: `consumers` (new research folders and who cites them from outside), `pointers` (unsent drafts and files naming their accession without them), `pairs` (lines naming two entities, verbatim, table header kept), `quiet`. Tests: `framework/scripts/test_dream_pass.py` (six synthetic fixtures, including the three controls).
* No registry, gate, schedule, service or agent was added.

## Cases

| Case | Kind | Before | After | Limit |
|---|---|---|---|---|
| D3, E-MTAB-14792 draft | replay of a DREAM-1 case | Two fresh sessions never reached the unsent draft; the 403 was recorded in the scout log and two notes with no route to it | Pointers added (dated lines) in the scout log, census reconciliation, bench follow-up and the drug_repurposing README row, plus a recipe row in `framework/scripts/README.md` section 13. One fresh `legend-delegate` (sonnet, effort medium read back) read the draft, named the operator hand-off, no e-mail, no bypass, "not accessible is not absent", in 4 tool calls | One run, graded by me, the private memory index again present in the delegate; it made one permitted read-only status call, still 403. The draft is still unsent and is the operator's decision |
| D7, HDAC5 to SLC2A1 bridge | control, mechanical check | Answer: `--bridges <file>`, off by default | Unchanged: with the flag, HDAC5 rows appear with `direction_unresolved`, the bridge row says `observed_other_context`, human primary muscle cells, knockdown not catalytic inhibition; without the flag, zero HDAC5 rows. Found stale: DREAM-1 named `bridges_it35.tsv`; since IT36 the bridge tables live in package folders (`nb3b_action_it32_20261107/output/bridges.tsv`) | Not a new finding. No direction crosses the bridge |
| NB-1, MYC (current science) | observation on current work | Consumer note proposed changes to a need and flagged three generator relations | Need `NEED-MYC-PROGENITOR-PROLIFERATION` **already consumed** correctly (counter-evidence, inferred line, direction uncertain). **Not consumed:** the three generator relations (sign contrast, "uninformative" label, binding lost with MYC protein high) exist only in the package file; no generation input reads it, so the 555 proposals ending in MYC were made without them. Dated line added to the consumer note | Whether to feed them in is the Orchestrator's choice |
| Generative | observation on current work | INV-17 offers three rivals: driver, marker, consequence | A fourth reading from rows already in the module (E03 SCAR12-class line MYC up with a wild-type-like radial-glia fraction; E80 MYC ChIP, binding at early-neuron promoters lost in knockout stem cells while MYC protein is high; E06 POU5F1 as prominent as MYC): MYC level high but disengaged at neuronal targets. Test: compare MYC occupancy at early-neuron genes across knockout, SCAR12-class and corrected lines, stratified by cell-cycle stage and MYC level. Staged as a lead (IPOTESI) with falsifier and transfer limit | Already in the repository: each row. New: the combination and the cross-line readout. E80 is an auditor's visual reading of one figure, no receipt; SCAR12 occupancy is not stated in what was read; loss of binding may follow closed chromatin. It does not change INV-17, the need or a direction, and suggests no compound |

A first pass found three folders with no outside citation; they had been renamed and no longer existed. The helper now skips removed folders (a defect found by use). Folders cited only by a ledger task file (for example `generation_it33_p4_20261107`) are a place to look, not proof of neglect.

## Controls (synthetic, declared)

Misleading association (`pairs` output carries no sign word and keeps a denying line), lost qualifier (context and status columns stay attached), repeated work (a folder already cited is reported as cited, an orphan as not). Six tests pass.

## Cost

Measured: the D3 delegate, `legend-delegate`, born 17,543 tokens, peak 22,096, output 1,065, cache read 59,606, 4 tool calls, effort medium read back. The pass in the main session was not separated from the rest of the work. Estimated, not observed: any later saving. Not observable here: whether sessions will call the pass. No share of a plan is stated.

## Not shown

No statistical validation (four cases, six fixtures, one author). D3 improvement is a single replay. The gain on D3 is a pointer, which any session could have added by hand; what the helper adds is the list of such gaps (65 prose-and-data files name the accession without the draft; only places a searcher lands were repaired).

## Change or remove

Edit `.claude/skills/legend-dream/SKILL.md` or the helper. To switch it off, delete step 4 in the self-eval skill and the rows in `CLAUDE.md` section 2, `SKILLS.md`, `ARCHITECTURE.md`, `framework/config/fulltext_route_registry.json` and `framework/scripts/README.md`. Pointer lines and the staged lead are ordinary dated records and may stay.
