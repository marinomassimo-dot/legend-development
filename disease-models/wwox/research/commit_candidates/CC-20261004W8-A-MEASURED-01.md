# COMMIT CANDIDATE — CC-20261004W8-A-MEASURED-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 8 2026-10-04, branch `task/sci-A-20261004w8`.
**context_policy:** `SOURCE_FIRST` — first passes written and committed from the sources before CLAIM 033 or DL-BIO-002 were opened.
**Not medical advice.** Class-level statements only.

## Target
- `claim_registry_current.md` · `CLAIM 033` (reserve (1), the syntactic classification): one paragraph after the operative corollary.
- `discovery_ledger_current.md` · `DL-BIO-002`: one append-only bullet before the `Razionale di trasferimento` line.

## Finding (the wave's Group A answer, per allele)
| Allele | Source | Measured / predicted | Matrix | Not measured | Reference-genotype class? |
|---|---|---|---|---|---|
| `p.(Thr12Arg)` exon-1 missense | PMID 36926521 | predicted (gnomAD absence, in silico) | — | RNA, protein, stability of this allele alone | no |
| exon-5 inversion SV | PMID 36926521 | **RNA measured**: exon 5 skipping, 186 vs 293 bp, qualitative | blood (PAXgene) RT-PCR + amplicon seq | skipped fraction, frame, NMD | no |
| genotype (missense + SV) | PMID 36926521 | **protein measured**, qualitative: strongly reduced band, faint residual | one fibroblast line vs one control | quantity, replicate, per-allele attribution | no |
| in-frame del exons 6-8 + `c.705dup` | PMID 37946251 (= Piard 2019 P11) | DNA only; protein loss annotated from coordinates | — | RNA, protein | no |
| `c.517-1G>A` + exon-5 deletion | PMID 40858643 | DNA only; PVS1 by rule | — | RNA, protein | no (intron-5 acceptor) |
| homozygous `p.(Leu239Arg)` | PMID 41835067 | DNA and segregation only; PP3 | — | everything functional | no |
| WWOX (wild-type) | PMID 41477840 | transcript time course | human reprogramming culture | protein, requirement | no allele |
| WWOX (wild-type) | PMID 41254692 | common-variant expression proxy (MR) | blood summary statistics | everything biological | no allele |

## Change class
**MINOR** — annotation on an `in observation` claim and an append-only lead bullet; no status change, no baseline narrowed.

## Registry records needed
`PAPER 207`, `PAPER 208`, `PAPER 209` (created by `CC-20261004W8-A-REGISTRY-01`; renumber with it). If `CC-20261004W7-B-SPLICE-MEASURED-01` propagates first, both anchors below still exist unchanged (that candidate inserts after the same CLAIM 033 sentence and before the same DL-BIO-002 line); order the two paragraphs by event.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-04 with `record_scoped_edit.py apply` (no `--apply`) on this branch: exit 0, 1 op(s), keys ['CLAIM 033'])

```json
[
 {"op": "replace-within", "id": "CLAIM 033",
  "old": "Un esperimento, due risultati. **Non è parere medico.**",
  "new": "Un esperimento, due risultati. **Non è parere medico.**\n🟠 **Reserve (1), three more syntactic labels checked against measurement (intake wave 8, 2026-10-04, `CC-20261004W8-A-MEASURED-01`).** (a) [[paper_registry_current#PAPER 207]] (PMID 36926521): a formally `null/missense` genotype (exon-1 missense + exon-5 inversion) with a **measured** patient-fibroblast western read by the authors as 'WWOX loss'; the panel shows a strongly reduced band with a faint residual band, one control, no quantification — it measures the genotype and cannot apportion the reduction between the two alleles. (b) [[paper_registry_current#PAPER 208]] (= Piard 2019 Patient 11) and [[paper_registry_current#PAPER 209]]: an in-frame exons 6-8 deletion and an exon-5 deletion are coded PVS1 (null) with **no RNA or protein measured**. A missense allele in trans does not by itself mean detectable protein, and an in-frame deletion coded null is a rule, not a measurement. `PREMISE: DATO (one blot, qualitative) + INFERENZA (classification)`. Nothing here transfers to Q230P or to any splice allele."}
]
```

## Op list — `discovery_ledger_current.md` (record-scoped; same dry run: exit 0, 1 op(s), keys ['DL-BIO-002'])

```json
[
 {"op": "replace-within", "id": "DL-BIO-002",
  "old": "- **Razionale di trasferimento**: diretto",
  "new": "- 🟢 **Append-only, 2026-10-04 (intake wave 8, `CC-20261004W8-A-MEASURED-01`).** **Un secondo saggio RNA WWOX misurato nel sangue:** [[paper_registry_current#PAPER 207]] (PMID 36926521) ha amplificato per RT-PCR la regione esoni 4-6 di WWOX da RNA di sangue PAXgene e, con sequenziamento dell'amplicone, ha mostrato lo skipping dell'esone 5 causato da un allele strutturale (inversione dell'esone 5). Il prodotto normale (293 bp) resta la banda forte e quello mutato (186 bp) è debole, senza quantificazione. **Limiti:** allele strutturale, non di sito accettore; nessuna frazione, nessun NMD, nessun frame dichiarato. Conferma che una giunzione WWOX è leggibile per RT-PCR nel sangue. `PREMISE: DATO + INFERENZA`.\n- **Razionale di trasferimento**: diretto"}
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the missense allele is supported only by population absence and in-silico scores | which was absent in gnomAD with in silico prediction scores in favor of its pathogenicity | PMID 36926521, Results 3.2.2; files/fulltext/PMID36926521_Colin2023_PMC.xml)
(blood RT-PCR over exons 4-6 shows a shorter product beside the expected one | using primers encompassing exons 4 through 6, obtained from blood, revealed the presence of a shorter amplicon isoform (186 bp) in addition to the expected 293 bp band | PMID 36926521, Results 3.2.2; files/fulltext/PMID36926521_Colin2023_PMC.xml)
(the shorter product is exon 5 skipping caused by the structural variant | Amplicon-sequencing analysis of the 186 bp gel-purified PCR product demonstrated that the structural variant caused exon 5 skipping | PMID 36926521, Results 3.2.2; files/fulltext/PMID36926521_Colin2023_PMC.xml)
(the western compares one patient fibroblast line with one healthy sample and is attributed to both variants | Western blotting revealed WWOX loss in a fibroblast cell line obtained from a skin biopsy of Individual 11 compared with a sample from a healthy individual, confirming the pathogenic effect of the two identified variants | PMID 36926521, Results 3.2.2; files/fulltext/PMID36926521_Colin2023_PMC.xml)
(the western panel shows a strongly reduced band with a faint residual band and no quantification | Control Proband WWOX 46 kDa Actin 43 kDa | PMID 36926521, Supplementary Figure S5G; files/supplements/PMID36926521/Image5.TIFF)
(the in-frame exons 6-8 deletion is classified with a null criterion | G=inframe_deletion | H=CH | I=het | L=PMID: 30356099 | M=PVS1, PM2, PM3 | PMID 37946251, Additional file 3 Table S7; files/supplements/PMID37946251/MOESM3_009Sev001_rows.txt)
(the intron-5 acceptor allele is classified by rule with no RNA assay | R=- | S=- | T=25.1 | U= | V=Pathogenic | W=PVS1, PM2, PM3, PP3 | PMID 40858643, Supplementary Data 1; files/supplements/PMID40858643/MOESM2_Pt2317_rows.txt)
