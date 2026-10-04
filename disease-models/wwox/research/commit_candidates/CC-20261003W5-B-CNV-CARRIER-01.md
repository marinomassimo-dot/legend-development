# COMMIT CANDIDATE — CC-20261003W5-B-CNV-CARRIER-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 5 2026-10-03, branch `task/sci-B-20261003w5`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w5_B.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`claim_registry_current.md` · `CLAIM 032` (one copy of WWOX; carriers): one paragraph after the `REVIVAL_TRIGGER` sentence.

## Finding
Two heterozygous WWOX observations **with a phenotype** were read this wave, and neither is a haploinsufficiency datum:
(a) PMID 31353122 — a heterozygous 6.8 Mb, 57-gene deletion ending inside WWOX in a child with West syndrome. What was examined in the carrier: exon-targeted panel sequencing with exon-level CNV calling and IGV inspection of the 12 panel genes in the interval; chromosomal microarray for the breakpoints. Not examined: introns or deep-intronic variants of the other allele, structural variants below array resolution, RNA, protein, parents. The authors decline the WWOX attribution; 56 other genes are deleted with it.
(b) PMID 35792847 — an affected sib of a Q230P homozygote is Q230P-heterozygous only, labelled a carrier pending further testing.

**Interaction with the open `CC-20261003W4-A-REVIEWS-01`**, which edits the same `REVIVAL_TRIGGER` sentence: this op anchors on its final clause, which that candidate keeps verbatim, so either order applies.

## Change class
**MINOR** — a qualification inside an `in observation` claim; no status change.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main f110c76 merged into the branch (no registry file changed on the branch): exit 0, 1 op(s), anchors ['CLAIM 032'])

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 032",
  "old": "or in any carrier of an exon-level WWOX deletion.",
  "new": "or in any carrier of an exon-level WWOX deletion.\n🔴 **Two heterozygous observations WITH a phenotype — intake wave 5, 2026-10-03 (`CC-20261003W5-B-CNV-CARRIER-01`); neither is a haploinsufficiency datum.** (a) [[paper_registry_current#PAPER 161]] (PMID 31353122): a heterozygous 6.8 Mb, 57-gene deletion whose distal breakpoint lies inside WWOX, in a child with West syndrome; the other WWOX allele is clean on an **exon-targeted** panel (no intronic, structural-below-array, RNA or parental analysis), and the authors decline to attribute the phenotype to WWOX. Fifty-six other genes are deleted with it, so the seizure history neither fires nor refutes the trigger above for WWOX. (b) [[paper_registry_current#PAPER 156]] (PMID 35792847): an affected sib of a Q230P homozygote carries Q230P **heterozygous only**, with a presentation the authors call similar, labelled 'a carrier' pending further testing. The simpler reading is an undetected second allele (exome and panel testing miss deep-intronic and small structural variants), not a dominant effect. ⇒ Neither carrier may be cited as a heterozygote with a WWOX phenotype, and neither is a demonstrated negative. `PREMISE: INFERENZA`."
 }
]
```

## Registry records needed
`PAPER 156`, `PAPER 161` (created by `CC-20261003W5-B-REGISTRY-01`).

### LOCATOR TRIPLES FOR BLIND AUDIT
(the deletion is heterozygous, 6.8 Mb, 57 genes, including WWOX | A 6.8 Mb heterozygous chromosomal deletion was detected within 16q22.2-q23.1, which contains 57 Refseq genes including PHLPP2 and WWOX | PMID 31353122, Molecular genetic analysis; files/fulltext/PMID31353122_Mori2019_IR.txt)
(the distal breakpoint lies within WWOX | Both breakpoints of the deleted region were located within those genes. | PMID 31353122, Molecular genetic analysis; files/fulltext/PMID31353122_Mori2019_IR.txt)
(the other allele was examined by exon-targeted panel | We conducted a targeted panel sequencing (TPS) for the targeted exons of 4813 disease-related genes | PMID 31353122, Molecular genetic analysis; files/fulltext/PMID31353122_Mori2019_IR.txt)
(no pathogenic variant on the other allele | no pathogenic variants were detected in the other allele of WWOX. | PMID 31353122, Abstract; files/fulltext/PMID31353122_Mori2019_IR.txt)
(parents not tested | Parental DNA was unavailable; therefore, the deletion was not confirmed as occurring de novo. | PMID 31353122, Molecular genetic analysis; files/fulltext/PMID31353122_Mori2019_IR.txt)
(the authors leave the WWOX link unresolved | Thus, the relationship between haploinsufficiency of WWOX and/or other genes located around WWOX and West syndrome remains unclear | PMID 31353122, Discussion; files/fulltext/PMID31353122_Mori2019_IR.txt)
(the affected sib is a Q230P heterozygote labelled a carrier | The brother of Patient 6 harbours a familial heterozygous missense pathogenic c.689A>C p.(Gln230Pro) variant and was labelled as a carrier | PMID 35792847, Results, Genetics; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(the second allele search is unfinished | Further testing is underway to determine whether the heterozygous variant is a disease-causing compound heterozygous variant. | PMID 35792847, Results, Genetics; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)

---

## BATCH DISPOSITION — `BATCH_20261003_004` (2026-10-03, ACTOR_ID `scientist`, Scientist I), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED · class **MINOR**, judged against the **live** status of the target: `CLAIM 032` is `in observation` (measured in the claim registry before propagating), its status, type and summary are unchanged, and the op appends a boundary to the record. The baseline-adjacent audit was run anyway: eight triples, all quotes found, none NOT_SUPPORTED.

The genotype caution travels with the record: an I136V carrier, a Menkes-Yang dual diagnosis and a Mori CNV carrier are **not** WOREE/SCAR12 observations, and a heterozygote is neither a demonstrated negative nor a positive for haploinsufficiency.

**Not medical advice.**
