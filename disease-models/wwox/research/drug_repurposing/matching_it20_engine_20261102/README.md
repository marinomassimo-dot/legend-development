# IT20 engine — provenance of a republished claim (P2), bepridil's specific evidence (P3), properties (P4)

Non-canonical research material; not medical advice; pharmacological compatibility only, no benefit
claim; no compound is proposed for use. Public edition, WWOX-DEE genotype class.

This package continues [`../matching_it19_p5_20261102/`](../matching_it19_p5_20261102/README.md),
which is read and **not modified**. The IT17 freeze, the IT18 P4 pre-registration and every dated
result of IT17–IT19 stay as they are.

---

## P2 — residual (a): the guard was bypassed through an intermediary

### Reproduced in the active path, before any change

IT19 added `group_transfer_unresolved()`: a ChEMBL mechanism curated on a `PROTEIN FAMILY` or
`PROTEIN COMPLEX GROUP` target whose components are fewer than half inside the module's intervention
targets no longer resolves a direction to a member gene. On the real catalogue that held back the
four ChEMBL rows it was meant to hold back:

```
$ python3 framework/scripts/repurposing_search.py need NEED-T-TYPE-CALCIUM --json
TERODILINE HYDROCHLORIDE  CACNA1G  ChEMBL curated mechanism  BLOCKER  protein_complex_group  direction_unresolved
SULOCTIDIL                CACNA1G  ChEMBL curated mechanism  BLOCKER  protein_complex_group  direction_unresolved
PHLOROGLUCINOL            CACNA1G  ChEMBL curated mechanism  BLOCKER  protein_complex_group  direction_unresolved
BEPRIDIL HYDROCHLORIDE    CACNA1G  ChEMBL curated mechanism  BLOCKER  protein_complex_group  direction_unresolved
```

and, on the same need, in the same listing, let the same four assertions through anyway:

```
Terodiline Hydrochloride  CACNA1G  DGIdb interaction  blocker  gene_listing  consistent
Suloctidil                CACNA1G  DGIdb interaction  blocker  gene_listing  consistent
Phloroglucinol            CACNA1G  DGIdb interaction  blocker  gene_listing  consistent
Bepridil Hydrochloride    CACNA1G  DGIdb interaction  blocker  gene_listing  consistent
```

### The row path, followed to the original source

| Step | What is there |
|---|---|
| The row LEGEND reads | a separate catalogue record (`CAT:DGIDB:5626675dc6fe`, origin `dgidb_only`, no InChIKey, no ChEMBL id), target row `source: DGIdb interaction`, `claim_source: ChEMBL`, `gene_claim_name: CACNA1G`, `gene_concept_id: hgnc:1394`, `interaction_type: blocker`, `identity.state: as_served` |
| What the module made of it | `target_level: gene_listing` — a statement about one gene — hence outside the group guard, which only reads ChEMBL rows |
| The republishing source | DGIdb, export of **2024-06-10** (`cache_manifest.json`; `catalog_stats.json` `dgidb.version`) |
| The release of the republished claims | **ChEMBL 33**, measured on the held export: `interactions.tsv`, column `interaction_source_db_version`, 16 941 ChEMBL rows, all `33` |
| What the live DGIdb service declares | **ChEMBL 37** (`cache/dgidb/live_sources.json`, fetched 2026-10-28). The live service's version is **not** the version of the export held. The IT20 radar scout read the live file; the rows the module actually consumes are the 2024 export |
| This catalogue's own ChEMBL backbone | `ChEMBL_37 2026-05-01` |
| The original assertion | the ChEMBL curated mechanism on **`CHEMBL2363032`**, "Voltage-gated calcium channel", `target_type: PROTEIN COMPLEX GROUP`, **26 components** (CACNA1A–S, CACNA2D1–4, CACNB1–4, CACNG1–8), `action_type: BLOCKER`, `mechanism_of_action: "Voltage-gated calcium channel blocker"` |
| Record level actually behind the gene row | `protein_complex_group`, **3 of 26** components among the module's intervention targets |
| What the republication does **not** carry | the ChEMBL target record id, and therefore the record's **level**. DGIdb flattens one group assertion into 26 one-gene rows and keeps only the action |

So the defect is not DGIdb's and not ChEMBL's. ChEMBL's annotation is legitimate at group level;
DGIdb's flattening is a documented export shape; **LEGEND's step of reading a flattened copy as a
statement about one gene is the improper one** — the same improper transfer IT19 fixed, arriving
through an intermediary that hides the level.

A copy of a previous release is also not automatically the same assertion as the record held here:
the copy is ChEMBL 33, the backbone is ChEMBL_37.

### The change

**One datum, in data, plus the code that reads it.** `coverage/source_artefacts.tsv` gains one row
of the kind the table already holds (per `claim_source`, per `symbol`, a `rule` and its `evidence`):

```
claim_source  symbol  rule                   evidence
ChEMBL        *       republication:ChEMBL   <republisher, export date, measured release, what the copy does not carry, the catalogue's own release, the measured consequence>
```

`framework/scripts/repurposing_search.py` reads it generically:

| Added | What it does |
|---|---|
| `republication_rule(rules, claim_source)` | the declaration for this claim source, or `None`. **No source is excluded and no compound is named.** Delete the row and every DGIdb ChEMBL row behaves exactly as before IT20 |
| `claim_provenance(e, t, rules)` | for a republished row: `original_source`, `republisher`, `republished_record_level`, `original_record`, `duplicate_of_record`, `missing`. The original record is resolved **only through an identifier the catalogue already trusts** — this record's own ChEMBL molecule id plus a ChEMBL curated mechanism row **of the same record** naming this gene with the same direction. No name matching, no release-to-release guessing |
| `republished_transfer_unresolved(prov, module_symbols)` | when the original record **is** resolved, the copy is asked exactly what the original is asked: `group_transfer_unresolved` is run **on the original row**. A copy can never do what the record it copies cannot, and a copy of a legitimate record stays usable. When the original is **not** resolved, the row keeps its action, its claim source and its place in the listing and carries no direction, with `missing` naming the datum |
| `assertion_key(e, src, t, prov)` | one key per underlying assertion (substance record + source record + action). A resolved copy gets the key of the record it copies, so a copy is never a second support |
| new association fields | `claim_source` (it was not exposed at all before), `claim_provenance`, `effective_target_level` (`EFFECTIVE_TARGET_LEVELS = TARGET_LEVELS + ("unresolved",)`), `assertion_key`, and a `limits` line naming original source, republisher, original record, its level and what is missing |
| new abstention class | `republished_claim_level_not_carried` (the closed vocabulary is extended, not bypassed) |

Both consumers of the rule inside the search layer are covered: `associations_for_need` and
`compound_to_needs`. Nothing is excluded from the listing, no source action is rewritten, and
`TARGET_LEVELS` is unchanged — the level the SOURCE ROW is about stays `gene_listing`, because that
is what DGIdb serves; the level of the **assertion** is the new, separate field.

`framework/scripts/repurposing_coverage.py`: `action_contexts()` now carries `claim_source`,
`effective_target_level`, `republished_copy_of` and `adds_independent_support`; `distinct_assertions()`
counts assertions rather than rows; each L2 cell gains `consistent_distinct_assertions`,
`opposed_distinct_assertions` and `republished_copies_not_counted_as_support`; each need gains
`direction_rows_by_effective_target_level` and a `republished_rows` block. The two counts sit side by
side — `consistent_associations` is still there — because a row count and an assertion count answer
different questions.

### Measured, on the real catalogue

`provenance_effect.py` runs the active path twice over all 23 needs, differing **only** in whether
the `republication:ChEMBL` row is present (`provenance_effect.json`, `provenance_rows.tsv`,
`provenance_orphans.tsv`). The "before" figures were re-derived independently from the committed
`HEAD` copy of `repurposing_search.py` and agree exactly (5 240 rows, 336 directed).

| | Before | After |
|---|---|---|
| Association rows listed | 5 240 | 5 240 (**no row leaves the listing**) |
| Rows asserting a direction | 336 | 246 |
| Rows that lost a direction | — | 90, all classed `republished_claim_level_not_carried` |
| Rows that gained one | — | 0 |
| Republished rows seen | — | 566; original record resolved through an identifier 80, level not carried 486 |
| Resolved copies still directed | — | 21 (a legitimate record's copy stays usable, e.g. AZD8108 on GRIN1/2A/2B through `CHEMBL2094124`, 4 of 7) |
| Copies no longer countable as distinct support | — | 21 |
| L2 coherent cells | 99 | 73 |
| L2 opposed cells | 13 | 11 |
| `consistent_mechanism_candidate` priorities | 99 | 73 |
| `insufficient_data` priorities | 366 | 382 |
| Deepening-queue compounds | 34 | 27 |

### The price, stated rather than smoothed

Of the 28 cells that lost a direction, **17** are duplicate records of a substance that still carries
a directed row in the same need, so nothing was lost but a second count of one assertion. Three more
(ethosuximide, memantine, esketamine) were duplicate `dgidb_only` families whose ChEMBL sibling is
already a **ranked unit**, i.e. already assessed — their queue rows were duplicates of assessed work.

The substances left with **no** directed row in their need are exactly **12 rows = 4 compounds × 3
genes** (`provenance_orphans.tsv`): terodiline, suloctidil, phloroglucinol and bepridil at
CACNA1G/H/I — precisely the four IT19 named. Three of them the IT19 reference scored
`indeterminable` or `unknown`; the fourth is bepridil, and P3 below is about it.

**Two rows lost an `opposed` label** (Apimostinel `agonist`, Neboglamine `positive modulator` on
GRIN1/2A/2B). An opposing signal is an exclusion and losing one is not symmetric with losing a
favourable label, so it was checked rather than assumed: **the opposing signal is not lost** — the
ChEMBL curated records `APIMOSTINEL` (PARTIAL AGONIST) and `NEBOGLAMINE` (POSITIVE ALLOSTERIC
MODULATOR) still read `opposed` on GRIN1/2A/2B. Only the `dgidb_only` duplicate records of the same
substances stopped asserting it. No special case keeps an opposed label that a favourable label
would have lost: that would be tuning for a desired outcome.

### Queue change, per compound

`ranking_it8_p9_20261029/deepening_queue.tsv`: 34 → 27 rows, 7 left, **0 entered**
(bepridil, esketamine, ethosuximide, memantine, phloroglucinol, suloctidil, terodiline). The
`direction_basis` column, which IT19 P6 added so a queue row says what kind of record carries its
direction, now stops saying `gene_listing` for 20 compounds whose direction rests on a real
`protein_family 3/3`, `protein_complex 2/2` or `single_protein` record — the bare `gene_listing`
basis was in every case the republished copy. Where a copy's original record **is** resolved the
column now shows `gene_listing 4/7` (azd8108, gw468816, indantadol, orphenadrine, ralfinamide):
the component counts of the record the copy copies, printed where a reader can check them.

### Consumers reached

`repurposing_search.py` (`need`, `compound`), `repurposing_coverage.py run` (`coverage_matrix.json`,
`priorities.json`, `coverage_summary.json`, `associations.jsonl.gz` — `check` says
`OK: files match a fresh regeneration`), `ranking_it8.py run` (`ranking.json`,
`deepening_queue.tsv`, `inventory_families.tsv.gz`), and `repurposing_view.py run` for both the full
and the shareable view (`check` says current). The only view **code** change is one label string for
the new abstention class, as agreed with the actor working on view presentation in a separate branch.

### What was deliberately not done

No general exclusion of DGIdb or of its ChEMBL rows (111 directed republished rows before, 21 still
directed after, and 4 022 DGIdb rows are untouched). No name whitelist. No compound named in code or
in the republication datum's rule field. No new override system. The 121 directed
Guide-to-Pharmacology rows, whose identity is checked against GtoPdb's own target id and which
therefore carry a real `single_protein` level, are untouched — that is the general principle
("a specific documented record stays usable"), not an exception for a list of names.

---

## Reproduce

```bash
cd /path/to/legend-development
python3 framework/scripts/repurposing_search.py need NEED-T-TYPE-CALCIUM --json
python3 disease-models/wwox/research/drug_repurposing/matching_it20_engine_20261102/provenance_effect.py
python3 framework/scripts/repurposing_coverage.py check
python3 framework/scripts/repurposing_view.py check
python3 -B framework/scripts/test_repurposing_group_transfer.py
python3 -B framework/scripts/test_repurposing_provenance.py
```
