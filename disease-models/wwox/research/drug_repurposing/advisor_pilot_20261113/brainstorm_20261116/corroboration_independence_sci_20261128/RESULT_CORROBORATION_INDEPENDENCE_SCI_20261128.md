# Independence of the corroboration behind claim-registry sentences (SCI, 2026-11-28; hypothesis level; no claim file edited; not medical advice)

Question: where a claim-registry sentence says that more than one source supports something, do the sources carry different
primary data and different authors? Prereg `PREREG_CORROBORATION_INDEPENDENCE_SCI_20261128.md` (sha256
846ea80aaf5de86568f9f92a88b84519272d0dc64e640cc52c27891c1cf48ede), committed before any source was opened (58ec4c48c).
First verdicts `sci_first_verdicts.tsv` (sha256 492100ea58e9118e0f7d87f874c329c4e1d9190f5b2672293c3348105fc5fec2), written
before the second reading was received. Second reader: `legend-delegate`, requested sonnet, effort high, blind to SCI's
verdicts (`BLIND_PACKET_SECOND_READER.md`, `SECOND_READING.md`). It read targeted sections, not whole papers.

## Denominator
138 sentences carry a corroboration term; 23 assert support from two or more publications or datasets. 10 of 23 are
BLOCKED-SKIP (drug, vector or treatment proposition or source) and nothing was checked for them: K01, K03, K05, K06, K07,
K08, K09, K17, K18, K19. **13 were checked.** The result does not speak for the 10 skipped ones.

## Verdicts (frozen rule: different primary data, no shared first or last author, no restatement)

| key | claim | what the sentence offers | SCI | second reader |
|---|---|---|---|---|
| K16 | 030 | "Corroborated independently" (two reviews, P47R) | FAILS a,c | FAILS a,b,c |
| K04 | 014 (consolidated baseline) | "multi-paper convergence is retained" | HOLDS | FAILS a (judgement call) |
| K22 | 036 | two Wwox-null rodent negatives | HOLDS (from held records) | UNSETTLED (rat text not on disk) |
| K23 | 038 | rat measure and mouse "convergent" measure | HOLDS (from held records) | UNSETTLED (rat text not on disk) |
| K10 | 023 | corroboration from a different literature | HOLDS | HOLDS |
| K15 | 030 | Steinberg 2021 "observes it independently" | HOLDS | HOLDS |
| K21 | 036 | three papers reproduce early collapse | HOLDS | HOLDS |
| K11 | 024 | weak corroboration from a second pull-down paper | HOLDS | not sent |
| K13 | 026 | "Independently, PAPER 103 measures" | HOLDS | not sent |
| K20 | 034 | fly paper "independently supports" | HOLDS | not sent |
| K02 | 005 | NPY direction, human organoid and mouse | DECLARED (says itself independence is not shown) | not sent |
| K12 | 025 | "confirmed in vivo" | UNSETTLED | not sent |
| K14 | 028 | "convergenza multi-paper (207, 218, 206, 214)" | UNSETTLED | not sent |

**Share failing.** SCI: 1 of 10 graded (HOLDS or FAILS); 0 of 9 without K16, which was known before the prereg. Counting the
second reader's K04: 2 of 10. The prediction of about 35 percent is missed; explanation E1 (sound at the first/last-author
level, at most 20 percent) fits the sentences that could be checked.

**On K04.** The second reader's point stands on the record's own words: CLAIM 014 already says that PMID 31340538 measures no
prenatal time point and that PMID 31543760 (cultured neural progenitors) measures no migration, layering or prenatal
phenotype. For a prenatal proposition the in vivo observation is then in PMID 32581702 alone. SCI's recorded HOLDS counted
the cell model as an observation. The verdict depends on that choice and is not averaged.

## What the first/last-author rule does not see (post hoc, not part of the prereg)
In 5 of the 10 graded sentences the sources still share people or a patient family:
* K04: the author list of PMID 32581702 contains, as middle authors, the first and senior authors of both other papers
  (Tochigi, Suzuki H; Kosla, Bednarek). One collaboration, not three groups. Its transcriptome part reuses GSE126075.
* K10: R. I. Aqeilan is first author of PMID 15070730 and a middle author of PMID 21115974.
* K15: the G372R organoids of PMID 34268881 are from the family reported in PMID 24369382 (the paper cites it so); the protein
  samples differ. Mahajnah is on both.
* K21: the three papers the sentence names (23254685, 18974271, 17360458) are one laboratory line; the independent pair is
  with PMID 19936220, the claim's own source.
* K16: also fails the frozen rule.

## What changes for the claim lines (one batch candidate for IT43; SCI edits nothing)
1. **CLAIM 030, "Corroboration" paragraph.** The header says "independent secondary source" and "Corroborated independently";
   the same paragraph says the records are not independent patients. Propose: "second secondary transmission of the same
   Mignot 2015 patient; same last author; not corroboration". (Already raised by ADV-339 S6; one repair, not two.)
2. **CLAIM 014** (consolidated baseline, so its audit rule applies). Say beside "multi-paper convergence" that the three papers
   come from one collaboration and that the prenatal in vivo observation is in PMID 32581702.
3. **CLAIM 025.** "confirmed in vivo" names no first source (the original statement rests on CORPUS P191, `Identifier: PENDING`).
   Propose "measured in vivo in mouse liver (PMID 29724996)".
4. **CLAIM 028** (flagged for review). Of the four papers of the "multi-paper convergence", one is identified (P206 = PMID
   15070730); P207, P214 and P218 are placeholders with `Identifier: PENDING`, so the convergence cannot be checked. Say so, or
   source them. The placeholders were already listed (`adv302_consumer_first_sci_20261128/DEFECT_FOR_IT_PLACEHOLDERS.md`); new
   here is that a claim's whole support rests on them.
5. **CLAIM 030, severity sentence.** Say that the Steinberg G372R line is the Mallaret family, that Steinberg words the point as
   a question, and that "(null)" for p.Arg54* is read from the genotype: no patient protein measurement was found in PMID
   24456803 (XML text, query `western|immunoblot|immunohisto|protein (level|expression|was|is)|fibroblast`, 0 hits, 2026-11-28;
   the second reader also saw none in the supplement slide).
6. **CLAIM 036.** "reproduce early systemic collapse": say that the three are one laboratory line.

## Consumers
Portfolio rows RP-017 and RP-019 cite CLAIM 030 or CLAIM 036, and several compound cards cite CLAIM 025, 028, 030 or 036. The
contexts opened (RP-017, RP-019, CLAIM 030 uses in cards A01 to A03) cite these claims for other content, not for the
sentences above; the remaining card contexts were not opened. No ranking, need or candidate state changes.

## Side finding for HE (not repaired)
Receipts record complete reads from `files/fulltext/PMID17803050_Suzuki2007.html`, `PMID19500159_Suzuki2009.html`,
`PMID23254685_Abdeen2013_PMC.html` and `PMID17360458_Aqeilan2007_PMC.html`. None is under `files/` by those names, and no
`.html/.htm/.xml/.txt` file under 3 MB has the recorded digest (2026-11-28; the sealed `adv17[45]*` folders excluded; larger
files and other types not hashed). PMID 17360458 has a PDF copy; the other three have no text copy found.

## Limits and disclosures
* Recall: only sentences with one of the listed terms were found; the screen from 138 to 23 was SCI's, read once.
* K11, K13, K20, K02, K12, K14 had one reader.
* Independence was graded, not whether each proposition is true or well scoped.
* While looking for a missing file SCI ran one recursive file search over `files/` that matched names inside file contents
  and so passed over the sealed ADV-174 and ADV-175 folders. It returned no path from them and displayed nothing from them;
  later searches excluded them.
