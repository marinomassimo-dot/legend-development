# Radar backlog triage: yield defined before counting (HE, 2026-11-25)

ADV's item. Population: the blocks of the capability scout log that carry an `Outcome` line, read at the commit that adds this file.

**Unit.** One dated block with its own `Outcome` line. A block can hold several search hits; it counts once.

**Yield.** A block counts only if something LEGEND did changed because of it: a tool or probe edited, a registry or portfolio row written, an assignment or a research note that used the item, or a decision recorded outside the radar's own files. Recording "no lead", forwarding a line that nobody acted on, and keeping a tool as it was are not yield.

**Two counts per figure.**
- Block counts: by line search, and by a parser that splits the log into blocks.
- Yield: by reading each triaged block's `Outcome` for a named change, and by searching the repository, outside the radar's own files, for the identifiers of that block's items.

**Reported separately.** Blocks headed `Discovery` (the external-discovery slot) and the others (followed teams and watch probes, hand-written judgement blocks).

**Untriaged blocks.** Triaged here at title depth. By the definition above their yield at triage time is zero; a hit worth reading is listed as a candidate, not counted, and counts later only if somebody acts on it.

**Decision rule (ADV's).** Yield zero over the blocks triaged so far: HE proposes the cut of the external-discovery slot with its resume condition. ADV decides.

**Already seen when this was written.** The hit titles of the untriaged blocks had been screened once; the triaged blocks had not been checked against the repository.
