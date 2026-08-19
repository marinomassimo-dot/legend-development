---
artifact: BENCH-AB-001 — output schema
schema_version: 1
manifest_schema_version: 2
benchmark_id: BENCH-AB-001
identical_for: scientist-a, scientist-b
---

# OUTPUT SCHEMA — the same shape for both readers

**Nothing here is a new data model.** Three of the four artifacts are the forms this repository
already uses; the fourth is the MODE B critical record. The only addition anywhere is the block
of **seven benchmark fields** in §3 (plus the `Locators:` cross-reference), and it is a
**benchmark field set**, not a change to the canonical claim registry.

---

> **Every path in this file is relative to the root of YOUR SURFACE**, written here as
> `<SURFACE>/`. It is not a path in the LEGEND repository, and a reader who resolves it there
> will not find it: your surface is a standalone repository that reuses LEGEND's layout so the
> validators run unmodified. Where a path is written without the marker it is relative to the
> same root.

## 1 · The work manifest — `<SURFACE>/disease-models/wwox/research/deepdive_manifests/PMID42397075.json`

`schema_version: 2`, validated by `framework/scripts/deepdive_manifest.py` in this surface.
The validator is the specification; this section names only what the benchmark fixes.

```
schema_version   2
pmid             "42397075"
doi              "10.1093/brain/awag239"
receipt          "BENCH-AB-001-<ACTOR_ID>-01"      ← benchmark id, NOT a receipt-ledger id:
                                                      this reading does not touch the ledger
landing          ["output/claim_candidates.md", "disease-models/.../fulltext_dossiers/PMID42397075.md"]
skills_considered / group_assessment / field_density / multihop / corpus_crossquery /
retraction_check   — each performed with evidence, or waived with a reason someone can
                     disagree with. 🔴 Several of these ask about the corpus, which this
                     surface does not contain: waive them, and say THAT is why. A waiver
                     naming the surface boundary is honest; a fabricated corpus query is not.
source_artifacts[]  {path, sha256, kind} — every packet file you used, plus every render you
                    made. kind ∈ article_binary · article_text · supplement_text · figure · table
verbatim_locators   {entries: [...]}
```

Each locator entry, exactly the fields the validator accepts:

```
proposition           what this quote is evidence FOR — one sentence, no conclusion verbs
snippet               the sentence, verbatim; elisions marked […]
surface               body | figure | table | supplement | abstract
artifact              a path INSIDE this surface, present in source_artifacts
anchor                section / figure / table / page — enough to find it again
panel_text_relation   text_only | panel_only | text_confirmed_by_panel |
                      text_contradicted_by_panel | panel_qualifies_text
contradicts / contradicts_needle      required when text_contradicted_by_panel
qualifies  / qualifies_needle         required when panel_qualifies_text
found_or_sought       "sought — …" or "found — …", one clause on how you came to it
```

`surface: figure` is an **attestation**, not a quotable text match, and the validator treats it
that way. Declare it as such rather than paraphrasing a panel into a quote.

---

## 2 · The dossier — `<SURFACE>/disease-models/wwox/research/fulltext_dossiers/PMID42397075.md`

The existing dossier form. An artifact table with role, path and SHA-256; then locators grouped
by section of the paper, each with its quote, surface and anchor; then, at the end, the coverage
note. It is the human-readable twin of the manifest, and the two must not disagree.

---

## 3 · Claim candidates — `output/claim_candidates.md`

The **canonical claim form**, section per claim, exactly as `claim_registry_current.md` writes
it — then the seven benchmark fields and the `Locators:` cross-reference. Eight labels, all
required. Nothing is renamed to fit the benchmark.

```markdown
## CLAIM BENCH-<ACTOR_ID>-001
**Title:** …
**Status:** consolidated baseline | in observation | conflicting evidence | flagged for review |
            background only | archived
**Type:** DATO | INFERENZA | IPOTESI | ESPANSIONE   (compound allowed, e.g.
            "DATO (organoid) + INFERENZA (transfer to human neuron)")
**Pathway:** …
**Genotype/model relevance:** genotype · model/population · cell type · developmental stage ·
            intervention · endpoint — the exact context, not a summary of it
**Transferability:** T1 | T2 | T3
**clinical relevance:** HIGH | MEDIUM | LOW | NONE
**Summary:** …
**Clinical meaning:** … (or "none — preclinical"; never invent one)
**Source:** the artifact(s) and where in them
**Wikilinks:** locator references inside this reading — NOT [[paper_registry_current#…]]:
            this surface has no registry and a wikilink to one would be a dangling assertion
**Impact on Working Model:** what would change if this were promoted — stated as a proposal

**Observation:** what was measured, in what system, with what result. No verb of conclusion.
**Author interpretation:** what the authors conclude from it, in their terms, marked as theirs.
**LEGEND interpretation:** what YOU conclude, typed (INFERENZA / IPOTESI), or "none".
**Direction:** increase | decrease | no change | not tested | mixed — of the endpoint named in
            Observation, under the intervention/genotype named there.
**Uncertainty:** what is not settled, and by what.
**Limitations:** authors' limitations and yours, distinguished.
**Contradictory evidence:** inside this paper, or "none found — searched: <what>".
**Locators:** the entry indices in the manifest that support this claim.
```

🔴 **The seam is the point.** `Observation`, `Author interpretation` and `LEGEND interpretation`
exist because the one thing a second reader must be able to attack is where measurement ends and
conclusion begins — and today, in the registry, that seam sits inside a paragraph. A claim whose
`Observation` contains "shows that", "demonstrates", "suggests" or "supports" has put the
conclusion in the wrong field.

`Uncertainty`, `Limitations` and `Contradictory evidence` are **benchmark fields**, exactly like
`Observation`, `Author interpretation`, `LEGEND interpretation` and `Direction`. Seven in all,
plus `Locators:`. Write every one of the eight, or the claim is incomplete.

An earlier revision of this schema described the last three as *"labelled prose under stable
labels the registry already carries"*. It does not: measured over the 39 claims of
`claim_registry_current.md`, `**Uncertainty:**`, `**Limitations:**` and
`**Contradictory evidence:**` appear as labels **0, 0 and 0 times**. There is no existing
convention to defer to, which is why they are fields here.

None of the seven is written to `claim_registry_current.md`. They live in the benchmark output,
they are compared there, and whether any becomes canonical is a later governed decision.

---

## 4 · The receipt — `output/receipt.json`

```json
{
  "benchmark_id": "BENCH-AB-001",
  "actor_id": "<ACTOR_ID>",
  "mode": "PRIMARY_EVIDENCE_READ | INDEPENDENT_CRITICAL_READ",
  "evidence_depth": "complete_fulltext_read | partial_fulltext_read",
  "coverage": {
    "abstract": "read", "introduction": "read", "methods": "read", "results": "read",
    "figures": "read", "tables": "not_present", "discussion": "read",
    "limitations": "read", "supplementary": "read"
  },
  "supplements_covered": ["File008", "File009", "File010", "File011", "File012"],
  "renders": [{"path": "output/renders/…", "sha256": "…", "of": "Figure 3F", "dpi": 300}],
  "validator": {
    "command": "python3 framework/scripts/deepdive_manifest.py --workspace . --pmid 42397075 --verify-artifacts --require-current-schema",
    "verdict_line": "<verbatim>",
    "exit_code": 0
  },
  "self_check": {
    "locators_inside_surface": true,
    "no_not_read_in_coverage": true,
    "all_claims_typed": true,
    "negatives_carry_premise_and_revival_trigger": true,
    "mode_b_axes_all_answered": "n/a | true"
  },
  "blockers": [],
  "contamination_declared": [],
  "started_at": "<ISO-8601>", "completed_at": "<ISO-8601>",
  "notes": "anything a reader of this record would otherwise have to guess"
}
```

Every value is a fact you checked, not an intention. `"contamination_declared"` is where a
broken prohibition goes, and declaring one costs far less than the alternative.

---

## 5 · MODE B only — `output/critical_reading.md`

One entry per finding. **Every mandatory axis of `scientist_reading_modes.md` §5.2 appears**,
including those with nothing to report — with what was searched.

```markdown
### <AXIS>
**Finding:** …            (or: "searched; none found — searched: <what, concretely>")
**Target:** CLAIM BENCH-…-00n | locator entries[k] | "the paper's conclusion that …"
**Statement:** the criticism, typed — a criticism can itself be INFERENZA or IPOTESI
**Locators:** entry indices that anchor it
**What would resolve it:** the experiment, the statistic, the panel, or the datum
```

An axis with no entry at all is an incomplete reading, not a clean paper.

---

## 6 · Forbidden output shapes

`claims.json` · `claim_schema.yaml` · any second locator format · any renaming of the twelve
canonical claim fields · any writing to a `*_current.md`, to a receipt ledger, or to any path
outside this surface.
