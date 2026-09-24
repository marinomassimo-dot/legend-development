# D0 — what a record is, on each surface `registry_records.py` reads

> **Non-normative design record.** Source-first + retrieval foundation AQP, block D0: a
> read-only census taken **before** any change to the parser, so the identity rule is derived
> from the files and not from an earlier proposal. Nothing canonical is modified here.

## Question

`registry_records.py` promises whole records, addressed by identity. For each of the seven
surfaces it reads, what structurally makes a record, where does it end, can an ID occur twice,
and can one rule serve every surface?

## Method (reproducible)

At `main` = `73fb5f3`, every Markdown heading (`#`–`######`) of the seven files was listed with
its level, its enclosing heading path, its line range (to the next heading of the same or a
higher level) and its nested headings. Lines inside fenced code blocks were excluded, because
Markdown does not render them as headings. A heading was an **identity candidate** when its
text, after leading decoration (emoji, symbols, whitespace), begins with a known ID shape
followed by the end of the text, a space, a dash or a colon. A heading that names an ID anywhere
else was classified as **update / reference**. Every ID that the first rule found more than once was
listed with all its occurrences. The census was then compared with what the current parser
returns for the same files.

## Record shapes, per surface

| Surface | Identity heading | Records | Repeated IDs | Fields as declared | Other headings that look like IDs |
|---|---|---:|---|---|---|
| `paper_registry_current` | `##` — `PAPER nnn`, `CORPUS Pnnn`, `CORPUS PMID n`, `CORPUS-STUB-n` | 448 | none | `**Name:** value`; all 448 carry `**Identifier:**` | none |
| `literature_tracking_log_current` | `##` — `LIT-n`, `LIT-EX-n` | 398 | none | `**Name:** value`, `**Identifier:**` | `## LIT-[NNN]` **inside a fenced template** — not a heading |
| `claim_registry_current` | `##` — `CLAIM nnn` | 40 | none | `**Name:** value`; **no** `Identifier` — the PMIDs in `Source` are citations | none |
| `working_model_current` | `#` — `BLOCK n` | 3 | none | prose, with `##`/`###` sub-sections | none |
| `dismissal_ledger_current` | `###` under `## Active rejections` — `DIS-nnn` | 12 | none | `- **Name:** value` (bulleted) | none |
| `discovery_ledger_current` | `###` (151) and `####` (2) — `DL-{BIO,MOL,REPO,MECH,METH,THER,META,BIOM}-nnn[a]`, often after an emoji | 153 | none | `- **Name**: value · **Name**: value` (bulleted, colon outside the bold, several per line) | 4 `### Update DL-… ` / `### STATUS UPDATE — DL-…`, each **after** its definition; `## Run … (FT-018/019/020)` |
| `full_text_queue_current` | `##` — `FT-nnn` | 173 | none | `**Name:** value` | 2 `#` **range headings** `FT-158 … FT-169`, `FT-165 … FT-168`; `## CORREZIONE APPEND-ONLY FT-062 …`, `## Aggiornamento … FT-044` |

## Answers

1. **What defines identity.** A heading, at the surface's identity level, whose text begins with
   the surface's ID. An `Identifier` field confirms identity on the paper registry and the
   literature log. It is not what defines identity: the claim registry, the ledgers, the queue
   and the working model carry no such field.
2. **Can an ID occur twice?** Not as a definition, on any surface. It does occur as an
   update heading (`Update DL-MOL-006`, `STATUS UPDATE — DL-MECH-017`), as a navigation heading
   (`# FT-158 … FT-169`) and in prose.
3. **Which occurrence is the definition, and why.** The one whose heading **begins** with the ID
   at the identity level. It is not the first occurrence, and here is the counterexample: the range heading
   `# FT-158 … FT-169` (line 7078) precedes the real `## FT-158` (line 7107). **"First occurrence
   = identity" is rejected on evidence.**
4. **Later dated occurrences.** On the discovery ledger, all four `Update` / `STATUS UPDATE`
   headings follow the definition they update. On the queue, `CORREZIONE APPEND-ONLY` and
   `Aggiornamento` are `##` update sections. Both are updates, not identities, and they stay
   discoverable as sections and mentions.
5. **Identity levels observed:** `#` (BLOCK), `##` (PAPER, CORPUS, LIT, CLAIM, FT), `###` (DIS, DL),
   `####` (two DL records).
6. **Where a record ends:** immediately before the next heading of the **same or a higher**
   level, fences excluded. It is verified on every surface: nested `###`/`####` blocks inside
   FT, DL and BLOCK records are appended content of that record (`AGGIUNTA …`, `CORREZIONE
   APPEND-ONLY …`, `La domanda di FT-062, risposta`).
7. **Nested headings:** part of the record. Two DL definitions sit at `####` inside another
   record: `DL-MECH-069b` inside `DL-MECH-069` (a sub-record by name) and `DL-METH-107` inside
   `DL-MECH-106` (a different family, probably mis-levelled). Each is still addressable by its
   own ID, and its parent's record contains it, losslessly.
8. **Section headings that resemble an ID:** yes — the two `#` FT ranges, and `##` headings that
   carry an ID after a leading word. The "begins with the ID" rule excludes the second group,
   and the level table excludes the first.
9. **Generic or surface-aware?** **Surface-aware in the level, generic in everything else.** A
   generic "begins with an ID shape, at any level" rule would take the FT ranges as definitions.
   A generic `##`-only rule misses the 168 DL, DIS and BLOCK records. The ID shapes, the
   decoration rule, the end rule and fence handling are the same on every surface. Only the
   admissible identity levels differ, and they are the table above.

## What the current parser does against this census

| Defect | Evidence |
|---|---|
| DL, DIS and BLOCK records are unaddressable: a `##`-only split puts them inside prose sections | `get --id DL-MECH-029`, `--id DIS-001`, `--id "BLOCK 1"` → `NO RECORD MATCHED`; `--theme GSK3 --source discovery_ledger_current` → no record, although the term occurs 49 times |
| A `##` record absorbs a following `#` heading and its introduction | `FT-157` carries `# FT-158 … FT-169 …`, `FT-069` the `# ⏭️ HANDOFF …` heading, `FT-062` the first `# 📎 APPENDICE`; the working model's `##` sections carry all three BLOCK headings |
| A heading inside a fenced block is parsed as a record | `LIT-[NNN]`, the log's own record template, is returned as a record |
| `--id` needs the whole heading text, so a bare ID misses every titled record | `--id FT-069` → `NO RECORD MATCHED`; `--id FT-158` (untitled) works |
| Bulleted fields are invisible to `--field` and `fields` | DIS (`- **Name:**`) and DL (`- **Name**:`) declare no fields to the parser |

## Decision

**D1 may proceed on all seven surfaces.** None is ambiguous on identity. The two nested DL
records are recorded here and not resolved: the file's structure is science content, and this
block does not edit it. Identity levels: `paper_registry_current`, `literature_tracking_log_current`,
`claim_registry_current`, `full_text_queue_current` at `##`; `working_model_current` at `#`;
`dismissal_ledger_current` at `###`; `discovery_ledger_current` at `###`–`####`.

No persistent index was created, and no canonical file was changed.
