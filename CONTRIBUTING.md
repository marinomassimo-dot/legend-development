# Contributing

This is a research repository with a hard privacy boundary and an unusual invariant: **the canonical state changes only through a batch commit, and every rejection is recorded rather than deleted.** Contributions are welcome inside those rules.

## Before anything else

```bash
python3 framework/scripts/legend_lint.py .
python3 scripts/public_release_gate.py --root . --mode staging --skip-clean-clone
python3 scripts/run_release_regressions.py
```

All three must be green before and after your change. The release gate is not a formality — it checks re-identifying *combinations*, provenance labelling, link integrity and clean-clone executability.

## The rules that are not negotiable

1. **No individual-level content, ever.** No names, geography, institutions, record or sample identifiers, dates tied to a case, family-relationship data, or a specific variant combination presented as one person's genotype. The public layers operate on public evidence only. When unsure, leave it out.
2. **Tag every claim.** `DATO` (data) · `INFERENZA` (inference) · `IPOTESI` (hypothesis) · `ESPANSIONE` (extension). An untagged assertion is not reviewable.
3. **Tag premises and rejections too.** If you close a door, name the premise it rests on and record a `REVIVAL_TRIGGER` — what would reopen it. See [`framework/instruction/epistemic_discipline.md`](framework/instruction/epistemic_discipline.md).
4. **Never delete a record.** Append-only files change status; they do not lose entries. Corrections are annotated at the point where the superseded statement appears, not appended at the end where nobody reads them.
5. **Nothing is medical advice.** No dosing, no treatment recommendation, no clinical instruction.
6. **`grep` is not a reading method.** It is for finding files, deduplicating and auditing after reading — never for deciding what a paper says.

## What is most useful

- **A failure case.** If the system reasoned wrongly, that is the highest-value contribution here: it becomes a row in [`framework/eval/learned_gates_registry.md`](framework/eval/learned_gates_registry.md) and, where possible, a regression test. An error that becomes a gate can never happen twice.
- **A paper the model got wrong**, with the passage that shows it.
- **Adopting the framework for another disease** — see [`framework/ADOPTING.md`](framework/ADOPTING.md). The gaps that surface when someone else instantiates it are worth more than anything found by re-reading it here.
- **Tooling** that makes an existing check stricter without making it noisier.

## What will be declined

- Individual-level clinical material, in any form.
- Therapeutic claims not traceable to a public source.
- Redistribution of third-party code or paywalled full texts (see [`_external_repos/MANIFEST.md`](_external_repos/MANIFEST.md) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)).
- Changes that make a capability claim stronger than what actually ships. Every capability is classified `BUNDLED` / `IMPLEMENTED` / `SPECIFIED` / `EXTERNAL` in [`SKILLS.md`](SKILLS.md), and that classification is enforced by a test.

## Style

Content is English; some deep registry and ledger entries remain in their original language, preserved verbatim because a faithful record of how the reasoning developed is worth more than a polished translation.

Cross-references use basename wikilinks with the **complete** target heading plus an alias — `[[file#Full heading|RECORD-ID]]`. The rules, and the two ways this goes wrong, are in [`framework/protocols/wikilink_schema.md`](framework/protocols/wikilink_schema.md) §1.2.1.
