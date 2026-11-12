# Strategic Advisor brief — Stage B

## Snapshot
- Repository SHA: `eb424cd06bc63439be5f26a8de6ccba171e3cbda` (branch `task/it48`)
- Dispatch time (UTC): 2026-11-12T20:50:29Z
- Uncommitted paths (9; read as on disk):
  - `edger/tasks/orchestrator/ORCH-ROADMAP-IT48-20261112.json` (M) sha256 ``
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/A1/assessment.md` (??) sha256 `d9ae8762955d0d12`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/A1/brief.md` (??) sha256 `a10d9501ef95f1f7`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/A1/meta.json` (??) sha256 `252ceb6351c3eae8`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/advisor_sealed/INTENDED_ACTION_1.md` (??) sha256 `cf739080b3d5d7d5`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/brief_A.md` (??) sha256 `a10d9501ef95f1f7`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/inputs/constraints.md` (??) sha256 `0d3795727a1378ff`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/inputs/mission.md` (??) sha256 `add4e65fbf47183d`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/invocations.jsonl` (??) sha256 `695d526bbee407bd`
- Dashboard: https://marinomassimo-dot.github.io/legend-development/ · source revision 3870f5457705917940530f9fa896b4697af9793a 2026-11-12T20:36:16+00:00 · the public page shows no build stamp; the package commit above is the source revision it is generated from. Publication date of the live page was not checked.

## Mission and limits (verbatim from the caller)


## Operational constraints
Constraints: zero new external spend; no contact with external people, no operator e-mail to any service; no clinical treatment recommendation, patient-level analysis, gene-therapy development, business activity or broad infrastructure redesign; public edition (no individual-level record); not medical advice; ranking means research investment, not expected efficacy in a child; no change of rank, sign or qualification to show an effect; AED evidence kept separate (clinical / preclinical / untested); one scientific delegate at a time, producer and verifier distinct; originals read in full when accessible.
Time: at most 24 hours from the first Stage A dispatch (2026-11-12). Ceilings: two Stage A, two Stage B. Owner session: orchestrator (legend-development-4e).
Dependencies: SCI48 science delivery is available when it arrives and is not a constraint. Public view and CI of the last delivered main commit may still be completing. The browser test host has a Snap Chromium fault (CHROME_BIN workaround).

## Saved Stage A assessment (complete, verbatim)
sha256 `d9ae8762955d0d12f8d7142884babe757a4ef9a5f043b922f39ba0c63d8d3c01`

## 1 · Principal decision

Which research increment the IT48 campaign should buy first with its two bounded slots, given zero external spend, no wet-lab capability and ~24 h: further depth in the active excitability / K‑channel branch, another existing investigation or open question, a premise shared by several candidates, knowledge already held but unused, or a small technical obstacle that blocks a scientific decision.

---

## 2 · Leading recommendation

**Execute the SCI43 "next brief" that has been written and never run: the juvenile (P10–P21) layer II/III share of the resting conductance carried by Ba²⁺‑sensitive (Kir2‑type / K2P‑type) channels — with the drug‑name‑led second route that was explicitly never run for Kir2, and a second independent verification of the eight rows the SCI43 verifier could not reach.**

Facts it rests on (all in the repository):

- `potassium_conductances_sci43_20261110/next_brief_sci43_20261110.md` lines 7 and 13 state the question, the decision it changes ("whether the first INV‑18 arm needs a K2P or high‑Ba²⁺ step (ladder step 2b) or whether the K branch reduces to the Kv7 spiking‑range arm"), the deliverable, the stop criterion ("a juvenile layer II/III figure or a bounded 'not found' with the strings used"), and the reopen condition for rows **D01–D04, D07, D08, D11, D13**.
- `S7_coda.md` §1: the premise carries **KH1**; the only share of that size (~23 %) comes from an **adult auditory‑cortex preprint whose digits the verifier could not re‑read (D01, D02)**; "if the juvenile share is small, KH1 loses its magnitude and the K branch reduces to KH2 (spiking range) **with no resting lever**". The same section records that a **drug‑name‑led search was not run for Kir2**, after the verifier had already shown that exact omission produced a *false* absence claim for K2P (`README.md` §Verification, item 1).
- `potassium_shares_sci44_20261110/README.md` item 6: those eight rows **still** stand producer‑read only ("recorded, not retried"; bioRxiv 429 / Cloudflare 1015, J Neurosci and PMC behind bot checks), and the 28 % deficit the whole ladder is scaled against (`README.md` line 9, 2.7 nS, Rin 102.9→143.0 MΩ) remains a constraint, not a discriminator (the verifier's size‑plus‑shunt degeneracy, same line).

Interpretation: the branch that has absorbed IT43–IT47 is ordered by a number read once, by one actor, from a source nobody could re‑open — and the module itself wrote down both the question and the two routes that would settle it. Strategic judgment: this is the only zero‑spend step I found that can **demote a whole branch**, not merely re‑word one arm, and it is the oldest unexecuted brief inside the branch the campaign is standing in.

---

## 3 · Relevant alternatives

- **Companion increment (my second slot, and the safer of the two): apply the unapplied "single condition record for the preparation".** `S7_coda.md` §4 shows one record (capacitance, access resistance, measured junction potential, selection rule, bath pH, Mg²⁺, K⁺, internal chloride) **serves four separate questions at once** — SCI42 chloride M03, SCI42 NP10679 M01, IT40 CP‑MH1 flat‑tau, SCI43 ladder step 0 — and is "proposed in `consumer_delta.md` row 11; **not applied**", status "known … but unused". Zero access risk, certain to complete, changes four next‑experiment designs, and stops a fifth package re‑requesting the same conditions. If the Orchestrator judges delegate access risk high, do this one first.
- **Verify what is already published and was never verified.** `cell_context_sci47_20261112/README.md` §Verification, item 2: "**Verification of the biological inferences (not done)** … no delegate was used", yet those inferences (OPC contribution to a bath‑applied Kv7 modulator; withdrawal of "human neurons lack KCNQ2") were landed in five languages on the public page (task record, OBJ_P0 evidence: "b67d209a (B1 cell‑class rows, Kv7 clause in five languages)"). Memory *verification-overturns-first-drafts.md* (audits overturned headlines) argues this is not a formality. Lower reach than the leading item, higher public exposure.
- **Complete the HE46/IT47 hypothesis mapping.** `p1_hypotheses_it47.md` line 20: SCI43 KH1–KH5 and HCN HY1–HY3 are "reachable and **not mapped**" (8 of 19 rows). Cheap, path exists (`PKG_MAP`), delivers to the conditional‑proposal table and the page. Note the dependency: if the leading increment moves KH1, mapping KH1–KH5 *after* it is better than before.
- **The case for staying where the ranking points instead.** INV‑02 (ISR sign) and INV‑08 (NRF2 genetic arm) are rank‑1/rank‑4 ties whose own rows call them "the cheapest act that converts the largest blocked slice of the catalogue". Their next step is a protein measurement — not available at zero spend. The remaining zero‑spend steps in other branches (IT46‑Q02 ABAT panel identity, IT46‑Q06 Winkel full text, IT46‑Q09 sulforaphane null arm, IT44‑Q05 PDK protein, IT47‑Q01/Q02) each change *one arm's wording or qualification*; none can close or keep a branch. That asymmetry, not loyalty to the branch, is why I stay.
- **INV‑11's three‑cause separation (4 needs with no catalogue reach).** Still OPEN and zero‑spend, but its upside shrank once I read `followup_it20_20261102/README.md`: the sibling diagnosis of the six abstaining needs found **every abstention correct**, named the one need a measurement could flip (NEED‑MYELINATION, 318 associations, CHRM1, "no row at all"), and showed that the "fix" a session would be tempted to make is the edit an audit already made in the other direction. Three of the four zero‑reach needs also carry direction `uncertain` (`needs/needs.md` lines 55, 64, 67, 68), so a target‑listing repair would not qualify anything.
- **Rejected on reading, recorded here so it is not re‑proposed:** extending `NEED-WWOX-ENDOGENOUS-BOOST` to give the pharmacological deep‑recovery route a target list. `dismissal_ledger_current.md` DIS‑003 holds that rejection on a `PREMISE: DATO` (normal transcript, protein absent in Gln230 homozygous fibroblasts) with a specific revival trigger (a compound‑heterozygous transcript behaving differently); `mission.md` §5 parks it; D‑39 and D‑04 add that abundance without function is half a result.

---

## 4 · Why now

- Three deliveries just landed in this branch (SCI46, SCI47, IT47) and the next‑batch brief `next_batch_it47_20261112/BRIEFS.md` sends B3/B4 to the wet lab and B5 to literature — the SCI43 question sits under both and is in neither.
- The campaign ceiling is 24 h with two increments and one scientific delegate at a time: the leading item is a *reading + verification* task with a written stop criterion, which is exactly the shape that finishes inside that window.
- The reopen condition is dated 2026‑11‑10 and has survived four iterations unexecuted while its premise kept being *used* (SCI44 scaled a KATP expectation against the 28 %; SCI45 refined pH arms above it). Carrying an unverified ordering premise forward is how the branch becomes expensive.
- Caution from memory (*check-integrator-before-queue-item.md*: SCI46 duplicated IT46 P4): read `next_batch_it47_20261112/BRIEFS.md` and any arriving SCI48 brief **before** dispatching, so the increment does not re‑do B1 (already executed as `generation_it47_20261112/b1_cellclass/`) or a B5 row.

---

## 5 · Evidence and uncertainty

**Facts.** The 28 % / 2.7 nS figure is derived from printed Table 1 means of PMID 34634460 and is explicitly a constraint, not a discriminator (SCI43 README line 10, with the verifier's shunt equivalence and a 95 % implied‑reversal interval of −143 to −77 mV). Eight of sixteen decisive rows are unverified by access. The Kir2 catalogue reach is one blocker row (dronedarone); K2P rows are five volatile anaesthetics plus doxapram; `azetukalner` has zero target rows and is reached only by name (SCI43 README §Catalogue finding). `k2p_pointers_sci45_20261111/consumer_delta.md` row 1 shows a pointer whose potency was off by ~10–20× and whose species label the primary paper does not support.

**Uncertainty.** (a) Access: three of the decisive sources sat behind bot checks and a preprint behind Cloudflare; re‑acquisition may fail again. The constraint set forbids contact and the classifier forbids UA spoofing (memory *he43-he44-pitfalls.md*), so "bounded not found with the strings used" must be an accepted outcome — and must be written as a measurement of reach, never as "no such conductance exists" (D‑18, D‑20, D‑25, D‑37). (b) Even a clean juvenile share does not make the Ba²⁺‑sensitive family druggable: the module holds no Kir2 activator (KH1 row) and a bath Ba²⁺ effect is not neuron‑only (`S7_coda.md` §2). (c) The result changes an ordering and a design, not a rank, sign or qualification — and must not be allowed to.

**What would *not* count as success:** more molecules, a novelty claim, or a promoted compound. The constraint file and `roadmap_current.md` §"Two orders, never one" both bind here.

---

## 6 · Next bounded action

**Principal question:** *What share of the resting conductance of juvenile (P10–P21) layer II/III neocortical pyramidal neurons is Ba²⁺‑sensitive (Kir2‑type, K2P‑type), and do the eight SCI43 rows (D01–D04, D07, D08, D11, D13) survive a second independent reading at digit level?*

Shape: one producer delegate (drug‑name‑led strings for Kir2 *and* K2P per `next_brief_sci43_20261110.md` §"What a producer should read", plus a second route outside the family that already answered — D‑19), then a distinct verifier; the already‑identified open‑access texts (40595546 figures 5d–g, 41233736 Methods, 37321992 Suppl. Fig 14) first, since they need no re‑acquisition.

**Result that would count:** a share table by family carrying preparation, age, layer, temperature, internal solution, blockers, tool, concentration, panel locator and depth — and then one of two dispositions written into `experiment_ladder.tsv`, `hypotheses.tsv` (KH1), the INV‑18 `next_test` field and a dated row of the open‑questions map:
- the juvenile share is of the order of 20–30 % → step 2/2b keeps precedence, KH1 keeps its magnitude; or
- the juvenile share is small, or remains a bounded "not found" after two routes → **KH1 loses its magnitude and the K branch reduces to the Kv7 spiking‑range arm with no resting lever**, which also reorders IT43‑Q03/Q04, IT44‑Q01/Q06 and the KATP sub‑arm.

Either disposition is a success; the second is the more valuable, because it is the one that frees investment.

---

## 7 · What would change my view

- A **wet capability or a funded collaboration** appearing: then INV‑02's protein‑level ISR sign or INV‑08's genetic KEAP1 arm outranks everything here (their own rows say so, and the Standing method measured that a need‑direction measurement unlocks more catalogue than any compound search).
- **SCI48 arriving with the K‑branch shares, the preparation conditions, or the SCI47‑B inference verification.** Then the leading increment is duplicated and I would switch to the condition record plus the unmapped KH/HY rows.
- Evidence that the **three reCAPTCHA sources and the preprint are unreachable by every permitted route** (two routes tried, logged): then the leading item collapses to a partial deliverable, and the condition record becomes the leading recommendation.
- A **public deposit of the Wwox raw traces or a juvenile layer II/III K⁺ dataset** (S7_coda §3 records none found, with no new search run): that would replace reading with analysis and would be worth more than either increment.
- A reader showing that the **OPC caveat now live on the public page is wrong**: that raises the SCI47‑B verification above both, because a published claim would be carrying an unverified inference.

---

## 8 · Resource implications

Two sequential delegates (producer, then a distinct verifier) per increment, consistent with "one scientific delegate at a time"; memory *delegation-budget-settings.md* notes the verifier is the costly role and that absence claims need two routes — budget the second route inside the producer's run, not as a third delegate. Zero external spend; no contact; no new dependency, registry, gate or scheduler.

Integration cost the Orchestrator should budget explicitly: touching `investigations.tsv`, `hypotheses.tsv`, `experiment_ladder.tsv` or the open‑questions map **stales generated dossiers** (memory *regenerate-dossiers-before-freezing.md*: `build_questions.py --write` plus touched‑folder suites before a battery; failures in IT40/IT43), and the browser suites need `CHROME_BIN` on this host. The 1,600‑character `carried_limits` cap and the closed abstention/coverage vocabularies apply if any generator row is re‑emitted.

---

## 9 · Inspected

Opened in full: `ledger/tasks/orchestrator/ORCH-ROADMAP-IT48-20261112.json`; `advisor_campaign_it48_20261112/inputs/mission.md`, `inputs/constraints.md`; `disease-models/wwox/mission.md`; `drug_repurposing/roadmap_current.md`; `needs/needs.md` (lines 30–99); `ranking_it8_p9_20261029/investigations.tsv` (rows 1–20, read in five passes); `batch_sci_20261105/map/open_questions_map.tsv` (header, WO‑01/WO‑02, rows 125–157; 82 OPEN rows counted by pattern); `next_batch_it47_20261112/BRIEFS.md`; `generation_it47_20261112/README.md`, `p1_hypotheses_it47.md`, `dream_it47.md`, `b1_cellclass/scored_it47.md`; `cell_context_sci47_20261112/README.md`; `potassium_conductances_sci43_20261110/README.md`, `S7_coda.md`, `next_brief_sci43_20261110.md`; `potassium_shares_sci44_20261110/README.md`; `k2p_pointers_sci45_20261111/consumer_delta.md`; `followup_it20_20261102/README.md`; `view/README.md`; `dismissal_ledger_current.md` (lines 1–220 plus the full DIS heading index); memory index `MEMORY.md` and its named entries as cited.

Not reached: the full `dismissal_ledger_current.md` (342 further lines) and `discovery_ledger_current.md`; `capability_scout_log.md`, `SKILLS.md`, `CAPABILITIES.md` and the `HARNESS-SCOUT-*` candidates (radar entry point — so I make no claim about public tools or datasets that could substitute for the reading above); `session_evaluations/` (>100 files, none opened); `inhibitory_defect_sci47_20261112/` and `keap1_nrf2_sci46_20261111/` originals beyond the quotations carried in the investigations rows; `advisor_build_20261112/PILOT_MANDATE.md`; the 519 k characters of the dashboard beyond the first 100 k.

---

## 10 · Freshness and exposure

- **Uncommitted inputs read as on disk:** the task record (modified), `inputs/mission.md`, `inputs/constraints.md`. The brief lists a fourth, `advisor_sealed/INTENDED_ACTION_1.md`; the task record states it was "written and sealed before any assessment was read; kept out of the brief" — **I deliberately did not open it**, so this Stage A view is independent of it.
- **Partial exposure I do have:** the task record carries `PILOT_STAGE_A_1` and the OBJ_P1–P4 step list, i.e. the campaign's *shape* (sealed action, Stage A/B, two increments, closure) and the IT47 scientific baseline. It does not state the intended action's content. I did not open `PILOT_MANDATE.md`.
- **Staleness.** The task record itself records CI #672 and view publication #38 as *pending at the last check* for the landed `b67d209a`, and the battery state as "no full battery of its own, only the CI gate"; I did not verify CI or Pages state. The dashboard source revision given in the brief (`3870f545`) is ahead of the landed `b67d209a`.
- **Dashboard fetch was partial** (first ~100 k of 619 k characters, one prompt, no screenshot; I made no visual inspection). What I saw: the page carries the caveat "Order of the investigations to be funded … not the efficacy of an intervention", and **no build or revision stamp appears**, consistent with the brief. One unresolved observation, offered for checking rather than as a defect claim: the fetched text appeared to enumerate **21** investigations while `investigations.tsv` holds **19** rows — the difference may be the "where to begin" entries or the conditional‑hypothesis rows, and a partial fetch cannot settle it.
- Nothing in this assessment reproduces a private identifier, an address, or any individual‑level record; the only external request I made was to the public dashboard URL, with no identifier in it.

## Orchestrator's intended action (complete, verbatim)
sha256 `cf739080b3d5d7d5aae06d9b5d1b470bc4f58b0097d90fa7bf3f31dd33c77973`

Intended action without the advisor (recorded 2026-11-12 before reading any assessment).
Increment 1: continue the current GSK3 / eIF2B thread (INV-09) by executing its two literature-executable open questions IT47-Q01 (is there any source with the catalytically dead eIF2B epsilon in tissue with intact Gsk3b?) and IT47-Q02 (is a Ser535 phosphomimetic validated; is DYRK2 at the priming serine relevant in neurons?), reading originals in full where accessible, and consuming the result into INV-09, its package card and the generator row GSK3-H1.
Reason: zero-spend and executable now, and the thread already has a pre-registered case with a blind reader.
Increment 2 (provisional): integrate the Kv7 / OPC specificity control (IT47-Q04) into the IT46-Q04 two-lever design review.

Begin with 'Response to the intended action': refinements, alternatives or a justified disagreement.

## Neutral entry points
| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit |
|---|---|---|---|---|
| limits | Authorised mission and resource limits: the task record named in the brief, and its siblings | `ledger/tasks/*/*.json` | 197 | 2026-11-12 |
| invariants | Canonical project invariants and the operating rules | `CLAUDE.md`<br>`ARCHITECTURE.md`<br>`framework/master/harness_development_principles.md`<br>`framework/master/designed_for_growth.md`<br>`framework/master/gold_is_in_the_details.md`<br>`framework/instruction/LEGEND_CORE.md`<br>`framework/instruction/epistemic_discipline.md`<br>`disease-models/wwox/mission.md` | 8 | 2026-11-12 |
| repurposing_method | Drug-repurposing roadmap and Standing method | `disease-models/wwox/research/drug_repurposing/roadmap_current.md`<br>`framework/protocols/repurposing_adapter_convention.md` | 2 | 2026-11-07 |
| dashboard | Dashboard: source records of the public page (the page is a map, the records are the facts) | `disease-models/wwox/research/drug_repurposing/view/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/DEPLOY.md` | 4 | 2026-11-12 |
| investigations | Investigations (research investment, not efficacy), needs and cards | `disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv`<br>`disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json`<br>`disease-models/wwox/research/drug_repurposing/needs/needs.md`<br>`disease-models/wwox/research/drug_repurposing/cards/*` | 65 | 2026-11-12 |
| open_questions | Open-question maps and rows | `disease-models/wwox/research/drug_repurposing/**/open_questions*` | 3 | 2026-11-12 |
| candidates | Candidates, comparisons and hypothesis packages | `disease-models/wwox/research/drug_repurposing/generation_it*/`<br>`disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv`<br>`disease-models/wwox/research/drug_repurposing/**/hypotheses*` | 46 | 2026-11-12 |
| packages | Completed packages and their consumer notes | `disease-models/wwox/research/drug_repurposing/*/README.md`<br>`disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md` | 227 | 2026-11-12 |
| diagnoses | Diagnoses, evaluations and DREAM | `disease-models/wwox/research/session_evaluations/*`<br>`disease-models/wwox/research/drug_repurposing/diagnosis_*/*`<br>`disease-models/wwox/research/dream*/README.md` | 192 | 2026-11-12 |
| memory_dismissals | Dismissal and discovery ledgers, memory index (outside the repository) | `disease-models/wwox/research/dismissal_ledger_current.md`<br>`disease-models/wwox/research/discovery_ledger_current.md`<br>`/home/desktop/.claude/projects/-home-desktop-legend-development/memory/MEMORY.md` | 3 | 2026-11-12 |
| radar | Radar findings and capability gaps | `governance/candidates/HARNESS-SCOUT-*.md`<br>`disease-models/wwox/research/capability_scout_log.md`<br>`SKILLS.md`<br>`CAPABILITIES.md` | 4 | 2026-11-12 |
| tools | Which tool answers which question (the advisor has no shell; this explains what the records came from) | `framework/scripts/README.md` | 1 | 2026-11-12 |

Memory directory (read-only): `/home/desktop/.claude/projects/-home-desktop-legend-development/memory`

## Output
Return one assessment with the headings given in your definition. Name every file or page you opened under 'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them.
