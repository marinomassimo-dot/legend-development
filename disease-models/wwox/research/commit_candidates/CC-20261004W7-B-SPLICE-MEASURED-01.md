# COMMIT CANDIDATE — CC-20261004W7-B-SPLICE-MEASURED-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 7 2026-10-04, branch `task/sci-B-20261004w7`.
**context_policy:** `SOURCE_FIRST` — first pass written and committed from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261004w7_B.md`).
**Not medical advice.** Class-level statements about published patients and genotypes only.

## Target
- `claim_registry_current.md` · `CLAIM 033` (null vs missense mortality; reserve (3) and the operative corollary on RNA evidence): one paragraph after the corollary.
- `discovery_ledger_current.md` · `DL-BIO-002` (transcript of the acceptor allele): one append-only bullet before the `Razionale di trasferimento` line.

## Finding
PMID 42248868 measured, in a clinical targeted RNA-seq on EDTA blood, the splice outcome of a WWOX intron-8 donor allele (`c.1056+5G>C`): "partial exon deletion", VUS → LP, positive diagnosis of WWOX-related disorders with ID/DD. It is the first measured WWOX splice outcome at the exon 8 / intron 8 boundary (the held analysis `analysis/splice_allele_rna_evidence_20260922.md` lists three measured events, none there) and shows that WWOX junctions are readable in blood RNA in a validated clinical assay. **What it does not show:** anything about the reference genotype's acceptor allele (different position, different mechanism); zygosity, second allele, junction coordinates, abnormal-read fraction, frame, NMD (the assay cannot read it) or protein.

Also from this wave, predicted only: PMID 36937954's canonical acceptor `c.606-1G>A` (exon 7, 186 nt — an exon-7 skip would be in frame, as the held analysis already derived) and PMID 40429983's intron-6 donor `c.605+1_605+2delinsAA` carry no RNA measurement. They are named here so that nobody counts them as measured.

## Change class
**MINOR** — an annotation of a feasibility datum on an `in observation` claim and an append-only lead bullet; no status change, no baseline narrowed.

## Registry records needed
`PAPER 206` (created by `CC-20261004W7-B-REGISTRY-01`; renumber with it).

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on main 70513cd merged into the branch: exit 0, 1 op(s), anchors ['CLAIM 033'])

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 033",
  "old": "Un esperimento, due risultati. **Non è parere medico.**",
  "new": "Un esperimento, due risultati. **Non è parere medico.**\n🟢 **Feasibility and one measured outcome in the same intron (intake wave 7, 2026-10-04, `CC-20261004W7-B-SPLICE-MEASURED-01`).** [[paper_registry_current#PAPER 206]] (PMID 42248868) reclassified a WWOX intron-8 donor allele, `c.1056+5G>C`, from VUS to LP after a clinical **targeted RNA-seq on EDTA blood** showed a *«partial exon deletion»* — the PS3-type route this corollary names, run in a blood sample rather than in cultured cells. ⚠️ Limits, measured at source: a different allele at a different position (donor +5, not acceptor −2); zygosity, second allele, junction coordinates, abnormal-read fraction and reading frame are not printed; the assay reads neither expression level nor NMD, and no protein or minigene confirmation was done. It shows the measurement is feasible in blood for WWOX; it says nothing about what the acceptor allele of the reference genotype does. Reserve (1) stands: Oliver's coding of splice alleles as null remains a syntactic class. `PREMISE: DATO (feasibility, one event) + INFERENZA (transfer)`."
 }
]
```

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on main 70513cd merged into the branch: exit 0, 1 op(s), anchors ['DL-BIO-002'])

```json
[
 {
  "op": "replace-within",
  "id": "DL-BIO-002",
  "old": "- **Razionale di trasferimento**: diretto",
  "new": "- 🟢 **Append-only, 2026-10-04 (intake wave 7, `CC-20261004W7-B-SPLICE-MEASURED-01`).** **Matrice alternativa misurata:** [[paper_registry_current#PAPER 206]] (PMID 42248868) ha misurato in un saggio clinico di **RNA-seq mirata su sangue EDTA** l'esito di un allele WWOX di **donatore dell'introne 8** (`c.1056+5G>C`): *«partial exon deletion»*, VUS → LP. È il primo esito di splicing misurato al confine esone 8 / introne 8 e mostra che la giunzione WWOX è leggibile nel sangue (geni > 0.5 TPM studiati in modo affidabile; nessun TPM WWOX stampato). Una lettura a livello di giunzione risolve uno spostamento di 6 nt senza elettroforesi (INFERENZA). **Limiti:** posizione diversa (donatore +5, non accettore −2); nessuna frazione di letture, nessuna giunzione, nessun NMD, nessuna proteina. Non sostituisce la RT-PCR ± inibitore NMD su cellule, ma ne offre un primo passo meno invasivo. `PREMISE: DATO + INFERENZA`.\n- **Razionale di trasferimento**: diretto"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(a WWOX intron-8 donor variant was reclassified after RNA-seq showed partial exon deletion | Case 5 WWOXc.1056+5G>C AR VUS → LP partial exon deletion Positive WWOX-Related Disorders Y Y | PMID 42248868, Table 2; files/fulltext/PMID42248868_Zhao2026_PMC.xml)
(RNA was taken from EDTA peripheral blood | Total RNA was extracted from peripheral blood in an EDTA tube using standard protocols. | PMID 42248868, Methods, Targeted reflex RNA-seq; files/fulltext/PMID42248868_Zhao2026_PMC.xml)
(a splice event required at least a 20 % net abnormal-junction change | The minimum net change in proportion of abnormal junction reads between the case and control was 20% in order to be considered a significant splicing event. | PMID 42248868, Methods; files/fulltext/PMID42248868_Zhao2026_PMC.xml)
(the assay reads neither expression nor NMD and no functional validation was done | The assay does not provide insights into gene expression levels or the impact of NMD due to test limitations | PMID 42248868, Discussion; files/fulltext/PMID42248868_Zhao2026_PMC.xml)
(low-expressed genes are less informative; genes above 0.5 TPM were reliable | Genes in this cohort with TPM values greater than 0.5 TPM were able to be reliably studied. | PMID 42248868, Discussion; files/fulltext/PMID42248868_Zhao2026_PMC.xml)
