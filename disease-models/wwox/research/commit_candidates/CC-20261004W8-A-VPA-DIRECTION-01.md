# COMMIT CANDIDATE — CC-20261004W8-A-VPA-DIRECTION-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 8 2026-10-04, branch `task/sci-A-20261004w8`.
**context_policy:** `SOURCE_FIRST` — the first pass of PMID 41254692 was written and committed before any registry or ledger record was opened.
**Not medical advice.** No clinical reading of any kind follows from this candidate.

## Target
`discovery_ledger_current.md`: **create** one lead record after `DL-METH-120` (provisional id `DL-REPO-003`).

## Finding
PMID 41254692's Results name vorinostat, valproic acid, sunitinib, Jinfukang and arsenic trioxide as compounds that "potentially increase" WWOX expression, and its Discussion builds an HDAC-inhibitor strategy on that. Its own deposited CTD export (Table S7, read cell-wise) lists **every WWOX row as `Decreases expression`** and every THBS2 row as `Increases expression` — the text is inverted relative to its data. The valproate row cites five reference PMIDs, none held and none read.

The lead is registered with its debt and its falsifier, not as evidence: a curated database annotation, from unread primaries in unknown cell types, says nothing about a patient with two loss-of-function alleles. It is recorded so that nobody later finds the inverted sentence in the paper and carries it the wrong way round.

## Change class
**MINOR** — one new research-layer lead record; no claim, registry record or working-model block changes.

## Registry records needed
`PAPER 222` (created by `CC-20261004W8-A-REGISTRY-01`; renumber with it).

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on this branch at b57ac61 (main 2de75c1 merged): exit 0, 1 op(s), keys ['DL-METH-120'])

```json
[
 {
  "op": "insert-after",
  "id": "DL-METH-120",
  "text": "\n### DL-REPO-003 — A curated database says valproate LOWERS WWOX expression in human cells, and the paper that carries the row states the opposite: the direction is a reading debt, not a lead\n\n- **Tag:** DATO (what the table says) + INFERENZA (what it would mean)\n- **Status:** open\n- **Created:** 2026-10-04 · intake wave 8, Scientist A, from `CC-20261004W8-A-VPA-DIRECTION-01`. Provisional id; the integrator renumbers.\n- **The finding.** [[paper_registry_current#PAPER 222]] (PMID 41254692) proposes raising WWOX as a therapeutic direction and names vorinostat, valproic acid, sunitinib, Jinfukang and arsenic trioxide as compounds that \"potentially increase\" WWOX expression. Its own deposited CTD export, Table S7, lists **every one of those rows as `Decreases expression`** in *Homo sapiens* (and every THBS2 row as `Increases expression`, again the opposite of the text). The valproic-acid / WWOX row cites five reference PMIDs: 23179753, 24935251, 26272509, 27188386, 28001369.\n- **Why it matters here, with the limits stated.** Valproate is an anti-seizure medicine used in WWOX-DEE patients, and `CC-20261003W3-A-VIGABATRIN-01` already records one L239R child whose spasms stopped on valproate plus clobazam. If the curated direction is right and transfers, a drug that lowers WWOX expression would be worth knowing about in a disease of WWOX loss. **None of that is established here:** the direction is a database annotation, not a measurement in this paper; the five primaries are **unread**; the cell types, doses, species and readouts (transcript or protein) are unknown; CTD rows are extracted from cancer and toxicology experiments; and nothing connects an expression change in a cultured cell to a patient carrying two loss-of-function alleles, where the question is residual function of a specific allele, not transcription of a wild-type gene.\n- **Counter-evidence / what would refute this:** reading the five primaries and finding the direction is cell-type- or dose-specific, or absent; or a measurement showing valproate does not change WWOX transcript or protein in a neural human cell.\n- **Falsifying experiment:** WWOX transcript and protein in human neural cells (or patient fibroblasts) with and without valproate at clinically plausible concentrations, with a positive control for HDAC inhibition.\n- **Next action:** read PMIDs 23179753, 24935251, 26272509, 27188386 and 28001369 and record, per paper, the direction, cell type, dose and readout. Until then, **no clinical reading of any kind**, and no entry in the therapeutic tracker.\n- **Transfer limit:** no WWOX allele, no neural tissue, no patient. Not medical advice.\n- **Links:** [[paper_registry_current#PAPER 222]] · `CC-20261004W8-A-VPA-DIRECTION-01` · `research/intake_wave_20261004w8_A.md`\n"
 }
]```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the Results say these compounds potentially increase WWOX expression | The compounds potentially increasing WWOX expression include Vorinostat, Valproic Acid, Sunitinib, Jinfukang, and Arsenic Trioxide. | PMID 41254692, Results, drug screening and docking; files/fulltext/PMID41254692_Qin2025_PMC.xml)
(the deposited table records valproic acid as decreasing WWOX expression in human cells | A=Valproic Acid | B=D014635 | C=WWOX | D=Homo sapiens | E=Decreases expression | PMID 41254692, Additional file 1 Table S7; files/supplements/PMID41254692/MOESM1_TableS7_rows.txt)
(the deposited table records vorinostat as decreasing WWOX expression in human cells | A=Vorinostat | B=D000077337 | C=WWOX | D=Homo sapiens | E=Decreases expression | PMID 41254692, Additional file 1 Table S7; files/supplements/PMID41254692/MOESM1_TableS7_rows.txt)
(the deposited table records valproic acid as increasing THBS2 expression | A=Valproic Acid | B=D014635 | C=THBS2 | D=Homo sapiens | E=Increases expression | PMID 41254692, Additional file 1 Table S7; files/supplements/PMID41254692/MOESM1_TableS7_rows.txt)
(the protein-level WWOX association does not survive multiple-testing correction | but this association did not reach statistical significance after FDR correction (FDR-corrected P = 0.160) | PMID 41254692, Results, pQTL-MR; files/fulltext/PMID41254692_Qin2025_PMC.xml)
