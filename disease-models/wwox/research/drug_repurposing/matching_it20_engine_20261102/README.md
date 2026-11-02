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

## P3 — residual (b): recovering the specific evidence, and only it

IT19 named the gap: the guard also held back bepridil's valid pharmacology, because the module had
no field in which a documented subunit-level measurement could re-license a direction a group record
cannot carry.

### The source IT19 used, verified at the source

`reference_it19_p5.tsv` row P08 cited `PubMed:15855830 abstract sentences 2-3`. The PubMed record was
fetched again directly (`efetch`, `retmode=xml`, 2026-11-02) and read, not recalled:

> **Voltage-dependent and frequency-independent inhibition of recombinant Cav3.2 T-type Ca2+ channel
> by bepridil.** *Pharmacology* 2005;**74**, doi `10.1159/000085329`.
> "Effects of bepridil on the low voltage-activated T-type Ca2+ channel (CaV3.2) current stably
> expressed in human embryonic kidney (HEK)-293 cells were examined using patch-clamp techniques.
> Bepridil potently inhibited ICa,T with a markedly voltage-dependent manner; the IC50 of bepridil
> was 0.4 micromol/l at the holding potential of -70 mV, which was 26 times as potent as that at
> -100 mV (10.6 micromol/l). … Bepridil exerted the tonic blocking action but not the use-dependent
> block. Bepridil had no effect on the recovery from inactivation of T-type Ca2+ channels."

IT19's figures are confirmed exactly. **One correction this re-read found:** the abstract says
*recombinant* Cav3.2 in a *human* cell line and **does not state the species of the Cav3.2 clone**.
IT19's reference row wrote "human Cav3.2 (CACNA1H) recombinant in HEK293", which is one step beyond
the abstract. The species-resolved target assignment is therefore taken from a different source and
the two statements are kept apart.

### The decisive datum, through legitimate routes

| Route | Asked | Answer |
|---|---|---|
| PubMed 15855830 | functional block of Cav3.2 | **IC50 0.4 µmol/l at a −70 mV holding potential**, 10.6 µmol/l at −100 mV (26-fold), tonic, not use-dependent, no effect on recovery from inactivation; patch clamp in HEK-293. The determining condition is the holding potential: the potency figure is meaningless without it |
| DrugCentral 2027 (`drug.target.interaction.tsv`, via the repo adapter) | is the target assignment species- and subunit-resolved? | **yes**: bepridil, STRUCT_ID 342, `CACNA1H`, UniProt `O95180`, `CAC1H_HUMAN`, `ORGANISM Homo sapiens`, **single** protein, `ACTION_TYPE BLOCKER` |
| the same row | is DrugCentral an independent confirmation of the **direction**? | **no.** `MOA_SOURCE: CHEMBL`, `action_origin: CHEMBL`, `action_origin_class: SHARED` — the action is the ChEMBL group annotation again. The adapter's own field says so |
| the same row | does its activity value carry a direction? | **no.** `ACT_TYPE Ki 5.149` (`ACT_SOURCE WOMBAT-PK`) is a **binding** measure; binding and functional are not interchangeable |
| ChEMBL_37 REST | any activity for CHEMBL1008 on CACNA1H? | **0 rows** against `CHEMBL1859` (CACNA1H single protein) and **0** against `CHEMBL2362995` (T-type family). Silent, not negative |
| GtoPdb 2026.3.1 (local cache) | any Cav3 interaction for bepridil? | bepridil is ligand **2337** but is listed only on **KNa1.1** (rat) and **Kv7.4** (human). Silent, not negative |
| the ChEMBL group record | does it cite this evidence? | no: `CHEMBL2363032` cites `ISBN:9780702034718 PP. 256` and `PubMed:10792039`, a troponin-C structure paper. So PubMed 15855830 is **independent of the module's own input** |

Four things are kept apart and only the first is claimed:

1. **what the compound does at the target** — voltage-dependent functional block of Cav3.2/CACNA1H;
2. **other subtypes** — **no Cav3.1 (CACNA1G) or Cav3.3 (CACNA1I) value was found anywhere.**
   Cav3.2 data do not authorise a Cav3.1 direction;
3. **the link of the target to the WWOX need** — untouched here. It is governed by
   `coverage/target_roles.tsv`, and at `NEED-SEIZURE-CONTROL-SYMPTOMATIC` CACNA1G remains
   `coupling_not_measured` after an independent audit, so bepridil is still abstained there;
4. **experimental or clinical benefit in WWOX deficiency** — nothing here speaks to it. Bepridil is a
   withdrawn agent in the catalogue's access field and no compound is proposed for use.

### The engine link

The datum enters as **one row of the table that already exists**, symmetric to the
`action_contradicted_by_cited_reference:<MOLECULE>:<ACTION>` rule that *removes* a direction:

```
claim_source  symbol    rule                                                 evidence
ChEMBL        CACNA1H   target_level_documented:CHEMBL1008:BLOCKER:single_protein   <locator, species, system, assay, endpoint, concentration, determining condition, independence, and what it does NOT establish>
```

`documented_level_waiver()` reads it. Four deliberate narrownesses keep it from becoming the general
override the task forbids:

- only `single_protein` is an accepted documented level (`DOCUMENTED_LEVELS`), and **anything else
  raises `ValueError`** — a family or class result can never be laundered into a subunit direction;
- the row names **one gene**, so the siblings gain nothing;
- the action must be the one the rule names, and the molecule must be one of this record's own
  identifiers (`molecule_ids`: own ChEMBL id, `inherited_from_parent`, declared parent record — here
  the salt `CHEMBL1200382` matches through its declared parent `CHEMBL1008`, an identifier chain the
  catalogue already holds; **no name is used**);
- it answers **only a record-level abstention**. An unstated action, a missing or inferred role row
  and an uncertain need direction are untouched.

No compound is named in code. No bepridil special case. The rule is deleted like any other row.

### Measured

**Exactly one waiver fires in the whole module** (all 23 needs, 5 240 association rows):

| | it19 (neither row) | P2 datum only | shipped |
|---|---|---|---|
| Directed rows | 336 | 337 | 247 |
| `group_record_mostly_outside_module_targets` | 12 | 11 | 11 |
| `republished_claim_level_not_carried` | 0 | 0 | 90 |
| documented-level waivers | 0 | 1 | 1 |

- `NEED-T-TYPE-CALCIUM` / **CACNA1H** / `CAT:CHEMBL1200382` → `consistent`, matched molecule
  `CHEMBL1008`. L2 coherent cells 73 → **74**, `families_consistent` at T-TYPE 21 → **22**.
- **CACNA1G and CACNA1I stay `group_record_mostly_outside_module_targets`** — the recovery is
  narrower than IT19's framing of P08 as "compatible at the T-TYPE need": the evidence is for one of
  the three genes the need lists, and the engine now says exactly that.
- The **republished copy** on CACNA1H stays `republished_claim_level_not_carried`: a copy carries no
  molecule identifier, so the waiver cannot attach to it. A copy stays a copy.
- At `NEED-SEIZURE-CONTROL-SYMPTOMATIC` bepridil remains abstained with `coupling_not_measured`.
- `deepening_queue.tsv`: bepridil returns (27 → 28 rows) and its `direction_basis` now reads
  `documented single_protein measurement on CACNA1H (record protein_complex_group 3/26 abstained;
  see source_artefacts.tsv)` — `ranking_it8.py direction_basis()` was corrected so a reader is not
  told the direction came from a 3/26 group record, which is the error this whole package is about.
- `provenance_orphans.tsv` falls from 12 rows to **9**: terodiline, suloctidil and phloroglucinol at
  CACNA1G/H/I, exactly the three the IT19 reference scored `indeterminable` or `unknown`.

### The half-of-components rule, reviewed

The 0.5 ratio was **not tuned** — tuning a heuristic until a desired compound reappears is the
failure mode the task names, and it is also unnecessary now. What changed is the threshold's *job*.
Before, the ratio was the last word on whether a group record's action reached a gene. Now it decides
only **when the module must ask for explicit information**, and an explicit, located, measure-typed
datum is what licenses a direction. That is the part of the heuristic replaced by information: the
ratio still routes, but it no longer adjudicates alone. The three IT19 regressions stay meaningful
and still pass unchanged (`test_repurposing_group_transfer.py`, 11 tests), because none of them
depends on the ratio being 0.5 rather than on a record being written above or at the module's level.

### Receipt

One `FULLTEXT_READ_RECEIPT` in [`receipts/`](receipts/):
`FTR-20261102-15855830-02`, depth **`abstract_only`**, `source_kind: abstract`, `prior_receipt:
FTR-20261102-15855830-01` (IT19's first read), `reread_reason:
new_question_outside_prior_coverage`. Validated with
`fulltext_receipts.py record --dry-run` → `DRY RUN OK`. **It was NOT appended to the ledger** and is
handed back for the integrator. Depth was not inflated: no full text was retrieved, the abstract was
read in full, and the receipt records the one correction to IT19's reference row that the re-read
found. The database queries (DrugCentral, ChEMBL REST, GtoPdb) are not literature reads and carry no
receipt; their versions and answers are in the rule's `evidence` field.

---

## P4 — three properties, fixtures written before the verifier sees the change

`framework/scripts/test_repurposing_provenance.py` (20 tests, `verbosity=2`, offline, **synthetic
entries only**). It reuses the existing fixture shape of
`framework/scripts/test_repurposing_group_transfer.py` (which is **not modified**: its 11 tests,
including IT19's three named regressions, still pass unchanged) and adds only the entries the three
properties need. The 65 regressions of `test_repurposing_coverage.py` also pass; one line of that
suite changed, the closed set of `source_artefacts.tsv` rule prefixes, which now admits the two new
rule kinds.

| Property | What it pins |
|---|---|
| **P1 duplicated evidence** | a curated record and another database's copy of it are **one** assertion: both stay listed, they share one `assertion_key`, and `distinct_assertions()` counts one. Two different molecules on the same group record are **two** assertions (the record id alone is not the assertion). An unresolvable copy keeps its own key rather than claiming to be a copy of something |
| **P2 improper transfer** | a record above the gene does not resolve its action to a member gene, **and neither does a copy of it**; a resolved copy inherits the *original's* abstention class and component counts, not a new one; a documented measurement is specific to its gene **and** to its molecule; a family-level document offered as a subunit waiver raises rather than being accepted |
| **P3 unknown stays unknown** | an abstained row is **not excluded** and keeps compound, claim source, action, `action_stated`, limits and reason; an unstated action keeps the source's own reason in record and in copy; an unresolved WWOX coupling is not decided by pharmacology; every new reason has a class and an unknown reason still raises |

### Why these cases discriminate

Each fixture fails at least one plausible wrong implementation, which is what makes it a test rather
than a restatement:

| Fixture | The wrong implementation it catches |
|---|---|
| improper attribution through an intermediary (`GRPCOPY`) | a guard that inspects only the original source's rows and lets a republished copy through — **the exact IT19 residual**, and `test_the_intermediary_route_is_closed` asserts the `consistent` label *before* the fix so the fixture is shown to be capable of failing |
| valid specific evidence kept (`DOCD` on the documented gene) | a guard that abstains on every group record, discarding information the module does have |
| family/complex documented at the relevant level (`FAM`, `CPLX`, `NMDA`) | a guard keyed on "is it a group?" instead of "is it written at the level the module reasons about?" |
| a copy of a **legitimate** record (`FAMCOPY`, and the resolved copy inside `CAT:FAM`) | an over-broad republication rule that abstains on every copy regardless of what it copies |
| unknown pharmacology (`MOD`, `MODCOPY`) | a guard that writes a label, or a new reason, over a row the source itself left unstated |
| WWOX role unresolved despite known pharmacology (`N-NOROLE`, empty role table) | a waiver leaking into the second judgment — what a compound does at a target deciding whether that target is coupled to the need |
| opposing signal kept visible (`OPP`, `OPPCOPY`) | an asymmetric rule that protects an unfavourable label it would have removed if favourable, or that hides an exclusion |
| molecule- and subunit-specificity (`DOCD` siblings, `OTHERMOL`) | a waiver read as a class permission or a compound-family permission |
| a group-level document as a waiver (`test_a_group_level_document_is_refused`) | the table used to launder a class result into a subunit direction |
| `test_the_waiver_matches_through_the_declared_parent_and_only_through_an_identifier` | identity by name creeping in through the parent/salt chain |
| `test_a_malformed_documented_level_row_fails_whatever_gene_it_names` | a bad table row sitting unnoticed until it happens to name the gene under inspection (the shape is checked before the subject) |

### Before / after, on the real catalogue

From `provenance_effect.json` (three arms over all 23 needs; the `it19` arm was cross-checked against
the committed `HEAD` copy of `repurposing_search.py` and agrees exactly), `coverage_summary.json` and
`deepening_queue.tsv`.

| | IT19 (as left) | IT20 (shipped) |
|---|---|---|
| Association rows listed | 5 240 | 5 240 |
| **Unsupported directions still emitted** — directed rows through a republished claim whose original record level is not carried | **90** | **0** |
| Directed rows, all sources | 336 | 247 |
| **Justified abstentions** — `republished_claim_level_not_carried` | 0 | 90 |
| `group_record_mostly_outside_module_targets` | 12 | 11 |
| **Abstentions losing available information** — lost rows whose substance keeps no directed row in that need | — | **9** (terodiline, suloctidil, phloroglucinol × CACNA1G/H/I; the IT19 reference scored all three `indeterminable` or `unknown`) |
| of which the IT19 reference supports | — | **0** |
| **Specific evidence recovered** | 0 | **1** documented-level waiver (bepridil, CACNA1H), and 21 republished copies of legitimate records that keep their direction |
| **Copies counted as distinct support** | 21 | **0** |
| L2 coherent cells | 99 | 74 |
| L2 opposed cells | 13 | 11 |
| `consistent_mechanism_candidate` | 99 | 74 |
| `insufficient_data` | 366 | 381 |
| **Actual queue changes** | 34 rows | **28 rows**: 7 left (bepridil, esketamine, ethosuximide, memantine, phloroglucinol, suloctidil, terodiline), bepridil returned on the recovered evidence, **0 others entered**; `direction_basis` stopped reading a bare `gene_listing` for 20 compounds whose direction rests on a real record |

Of the 7 that left the queue, 3 (ethosuximide, memantine, esketamine) were `dgidb_only` duplicate
families whose ChEMBL sibling is already a **ranked unit** — duplicates of assessed work, not lost
candidates.

### The one IT19 expectation that had to move, and how

`ranking_it8_p9_20261029/test_ranking_it8.py` holds a drift detector,
`test_live_labels_equal_the_guarded_answers_committed_by_it19_p5`, asserting that the live engine
still reproduces every label in IT19's committed `module_answers_guarded.tsv`. After P3 one pair
legitimately differs: **P08 (bepridil) `direction_unresolved` → `mixed:consistent|direction_unresolved`**.

IT19's dated table was **not** rewritten — a dated result stays what it was. Instead the detector now
compares against that same table and carries a `DECLARED_CHANGES_SINCE_IT19_P5` entry naming the
pair, the old label, the new label and the reason. The detector stays sharp in both directions: any
*undeclared* drift on any of the 32 pairs fails, and a declaration that no longer corresponds to a
real difference fails too, so it cannot rot into a blanket exemption. `changed_by_group_guard` is
still 4 and the reference counts (32 pairs, 25 compounds, 17 determinate, 11 functional, 6
class-level, 8 independent) are unchanged.

### What this does and does not establish

No new evaluation set was built and **no IT17–IT19 experiment was rewritten**: the IT18 P4
pre-registration, the IT19 P5 selection, reference, locked answers and dated results are inputs here
and are untouched on disk. The figures above are **counts of the module's own behaviour on its own
catalogue**, not an accuracy measurement: the IT19 reference is the only external yardstick in play,
it covers 32 selected pairs chosen to discriminate attribution kinds, and it is reused, not extended.
So **no claim of general superiority** follows from the four compounds that prompted the work, and
none is made. What is established is narrower and checkable: a route by which a group-level assertion
reached a member gene is closed, including through an intermediary; a specific documented measurement
can re-license a direction for the one gene it was measured on; and a copy is no longer counted as a
second support. The 20 property tests are the claim; the real-catalogue numbers are its size.

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
