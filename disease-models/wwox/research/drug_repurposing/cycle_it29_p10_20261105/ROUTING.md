# IT29 P10 step 4: routing (2026-11-05)

Challenge `CH-IT29-CLASSIIA-CNS-MYELIN`; nature `shared_premise` (a premise carried by several rows is partly unsupported) -> thematic batch, by `challenge_batch.py` routing. Three Scientists, no verifier at launch.

| Actor | Sub-question | Brief | Output directory | Tools it needs | Does not overlap with |
|---|---|---|---|---|---|
| Scientist F | class IIa HDACs inside the CNS oligodendrocyte lineage (genetic, compound, expression) | `BRIEF_F.md` | `cycle_it29_p10_20261105/p10_F/` | PubMed MCP (search, metadata, full text), Europe PMC REST, Write | G (peripheral source), H (neuron/axon, adversarial) |
| Scientist G | PMID 29472387 completely, plus catalytic v scaffold in myelinating glia | `BRIEF_G.md` | `cycle_it29_p10_20261105/p10_G/` | same | F, H |
| Scientist H | neuronal/axonal route to myelin, and adversarial search for a favourable or neutral sign | `BRIEF_H.md` | `cycle_it29_p10_20261105/p10_H/` | same | F, G |

Shared: `BRIEF_COMMON_P10.md` (constraints, TSV schema, receipt format, event-id suffix -08), `QUESTION.md` (done v new, pre-registered consequences).

Launch: the three are independent and may run concurrently (no shared file is written; each reader works in its own folder). Prompt for each: "Follow `<brief path>`" is sufficient, since the brief names the common file; the host should not summarise the brief.

Not routed, and why: Wong 2018 interneuron-survival lead (needs a measurement, not a read); GSK3B and EZH2-inhibitor direction (no live proposal depends on them); pracinostat assay descriptions (mandate step P11, already queued); any WWOX-specific search (no class IIa x WWOX datum is expected; if a reader meets one it reports it).

On return (step 5): receipts dry-run then `record`; `challenge_batch.py check --task ORCH-FRESH-IT29-P10-20261105`; recompute each reader's row counts from its TSV; consumers named in the challenge `returned` list; no edit to the four scientific current files.
