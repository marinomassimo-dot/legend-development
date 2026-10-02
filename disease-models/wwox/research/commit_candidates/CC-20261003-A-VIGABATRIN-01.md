# COMMIT CANDIDATE — CC-20261003-A-VIGABATRIN-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 2 2026-10-03, branch `task/sci-A-20261003`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003_A.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
- `claim_registry_current.md` · `CLAIM 001` (`conflicting evidence`) — one addition.
- `paper_registry_current.md` · `PAPER 016` — two text repairs (genotype line over-reads the minigene; note omits the persisting electrographic seizures).
- `discovery_ledger_current.md` · `DL-MOL-007` — an append-only rectification line (phenobarbital and nitrazepam were stopped for adverse events, not reported ineffective).

## Change class
**MINOR** — evidence added on both sides of a claim already `conflicting evidence`; status unchanged; no BLOCCO 1 change.

## Registry landing
PMID 39101447 → `PAPER 016`; PMID 35573960 → `PAPER 133` (created by `CC-20261003-A-REGISTRY-01`, which must run first).

## Ordering
The receipts `FTR-20261003-<pmid>-01` named below must be appended to the ledger before this candidate is propagated, so that no record cites a receipt the ledger does not hold.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-03 against `main` ba5682f with `record_scoped_edit.py apply`: exit 0, 1 op(s), keys ['CLAIM 001'])

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 001",
  "old": "**Nessun VABAM né peggioramento riportato in questo studio.**",
  "new": "**Nessun VABAM né peggioramento riportato in questo studio.** — **Wave 2 2026-10-03 (`CC-20261003-A-VIGABATRIN-01`), due letture complete:** (a) You 2024 ([[paper_registry_current#PAPER 016]], `FTR-20261003-39101447-01`): a 11 mesi, con vigabatrin aggiunto a tre farmaci, il VEEG registra ancora attacchi elettrici focali e spasmi *«not noticed at home by her parents»*; la libertà da crisi riportata è **clinica** (*«no visible seizures»*) fino a 13 mesi. Il dato è riduzione delle crisi visibili, non controllo elettrografico. (b) Riva 2022 ([[paper_registry_current#PAPER 133]], `FTR-20261003-35573960-01`): in un genotipo null/null predetto con esordio al primo giorno, vigabatrin **inefficace** (con valproato, clonazepam, clobazam, levetiracetam, rufinamide, CBD; ACTH e dieta chetogenica senza effetto) eppure mantenuto in terapia; non è una sindrome di West. Entrambi `n = 1`, genotipi null predetti, nessuna RMN di sicurezza. Lo status `conflicting evidence` non cambia."
 }
]
```

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 against `main` ba5682f with `record_scoped_edit.py apply`: exit 0, 2 op(s), keys ['PAPER 016', 'PAPER 016'])

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 016",
  "old": "**Genotype/model:** omozigote splice site c.172+1G>C (null/null per effetto funzionale; proteina troncata da minigene)",
  "new": "**Genotype/model:** omozigote splice site donatore c.172+1G>C (isodisomia inferita da LOH copy-neutral); minigene esoni 1–3 in HEK293T: **skipping dell'esone 2** (WT 426 bp, mutante 361 bp; 65 nt, fuori frame) — la troncatura è una traduzione in silico; nessun RNA del paziente, nessuna proteina (corretto `CC-20261003-A-VIGABATRIN-01`)"
 },
 {
  "op": "replace-within",
  "id": "PAPER 016",
  "old": "riduzione crisi con VGB 200 mg/kg/die in 1 caso null/null;",
  "new": "riduzione delle crisi **visibili** con VGB in 1 caso null/null, ma il VEEG a 11 mesi registra ancora attacchi elettrici e spasmi non notati a casa;"
 }
]
```

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-03 against `main` ba5682f with `record_scoped_edit.py apply`: exit 0, 1 op(s), keys ['DL-MOL-007'])

```json
[
 {
  "op": "replace-within",
  "id": "DL-MOL-007",
  "old": "→ [[clinical_monitoring_endpoints_current]], NON biomarker WWOX.",
  "new": "→ [[clinical_monitoring_endpoints_current]], NON biomarker WWOX.\n- 🔵 **Rettifica append-only, 2026-10-03 (`CC-20261003-A-VIGABATRIN-01`, lettura `FTR-20261003-35573960-01`):** fenobarbitale e nitrazepam non sono riportati come *inefficaci* ma come sospesi per eventi avversi (*«determined adverse events such as extreme drowsiness or increased secretions»*). Il vigabatrin, elencato fra gli inefficaci, resta fra gli ASM correnti. Identity record ora proposto: [[paper_registry_current#PAPER 133]]."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(electrographic seizures persisted at 11 months under vigabatrin | VEEG showed clinical seizures, but these were not noticed at home by her parents | PMID 39101447, Results, Clinical manifestations; files/fulltext/PMID39101447_You2024_PMC.xml)
(the reported seizure freedom is clinical, at 13 months | when the child was 13 months old, she had no visible seizures | PMID 39101447, Results, Clinical manifestations; files/fulltext/PMID39101447_You2024_PMC.xml)
(protein truncation was translated in silico | Finally, Snapgene software was used to translate nucleotide sequences into protein sequences | PMID 39101447, Methods, Minigene splicing assay; files/fulltext/PMID39101447_You2024_PMC.xml)
(the measured consequence is exon 2 loss in the minigene | caused a splicing abnormality, which abrogated the intron 2 canonical splice site and led to a loss of exon 2 | PMID 39101447, Results, Gene testing; files/fulltext/PMID39101447_You2024_PMC.xml)
(vigabatrin and six other drugs were ineffective in the Riva patient | Several anti-seizure medications (ASM) were ineffective (i.e., valproate, vigabatrin, clonazepam, clobazam, levetiracetam, rufinamide, and CBD oil) | PMID 35573960, Results, Clinical Features; files/fulltext/PMID35573960_Riva2022_PMC.xml)
(phenobarbital and nitrazepam were stopped for adverse events | or determined adverse events such as extreme drowsiness or increased secretions (i.e., phenobarbital, nitrazepam) | PMID 35573960, Results, Clinical Features; files/fulltext/PMID35573960_Riva2022_PMC.xml)
(vigabatrin remains among the current medications | Current ASMs include vigabatrin | PMID 35573960, Results, Clinical Features; files/fulltext/PMID35573960_Riva2022_PMC.xml)
