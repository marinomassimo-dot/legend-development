# ADV-244 wording placed (IT, 2026-11-25)

Actor `orchestrator` (IT). Hypothesis level; reference genotype class; nothing here is medical advice. Source of the wording: SCI, `brainstorm_20261116/adv244_organoid_clone_reads_sci_20261125/RESULT_ADV244_ORGANOID_CLONE_READS_SCI_20261125.md` section 6 (relayed by SCI at ADV's request; peer message, not operator authority). No value, grade, rank or status changes.

## 1. What was placed (ordinary route)

| Row | Where | What |
|---|---|---|
| K01, D01, D02, M01, E02, I01 | `cards/<id>.packet.json`, field `not_known`, one item; cards rebuilt with `repurposing_bridge.py`; `check_cards.py` 0 problems | whether any organoid transcript difference or null on the card (GSE156243) is independent of the CRISPR clone |
| INV-16 | `ranking_it8_p9_20261029/investigations.tsv`, `investigations_it20.tsv`, `ranking.json`, field `evidence_available`, dated clause after "the human organoid shows SLC2A1 higher on transcript"; translated into it, fr, es, de; views and package regenerated | same limit |
| CLAIM 002 | not edited | no claim text; and see 2 |
| RP-008 | not edited (ADV's portfolio) | see 2 |

D02 was added to SCI's list because its premise reading ("Wnt transcript premise not supported in the organoid") is a null from the same deposit.

## 2. Checked against the source before placing

Held PMC text of PMID 34268881 (Methods, RNA-seq): 8 organoids sequenced (4 WT, 4 KO); one WT failed quality control; another WT "did not cluster with any of the other samples"; both removed, six used. So four KO against two WT is the paper's own count; the clone statement comes from SCI's reads (all four KO libraries carry clone 1B's alleles). The paper says clones 1B and A2 were both used for organoid generation, so "one clone" is a finding about the sequenced libraries only.

* **Second increment (same day): the batch.** First placed without "apparently one batch" (my search of the held text had found batches named only for imaging, qPCR and ephys panels). SCI then supplied sources, which I verified in the held files: Methods, "For all analyses, organoids from the same batch were used, unless stated otherwise"; the authors' reply in the peer-review file (`EMMM-13-e13610-s007.pdf`, PDF page 24), "the subfractionation experiment was done on a totally different batch of the one we performed the RNA-seq". Neither says in so many words that the six libraries share a batch, so the limit now reads "appear to come from one batch", with the sources and that caveat in the text. SCI's third source (the GEO design line, "age- and batch-matched") was not opened by me.
* **Added:** the paper's own account of the two removals (one failed quality control, one did not cluster); SCI's "one further wild type" covers only the second.
* **CLAIM 002** (hyperexcitability, rescue) rests on field-potential, firing and calcium readouts, not on the RNA-seq libraries; its text carries no 4-versus-2 statement. Nothing to place there unless a claim sentence cites the transcript set. **RP-008** carries one sentence on held GSE156243 bulk data (WNT5A up in KO, composition-confounded): the clone limit applies to it; ADV owns that row.
* Cards carrying the identical string "4 versus 2 libraries, one laboratory" and not named by SCI: **E01, E03, F01 now carry the same item** (ADV's instruction, second increment). J01, F02 and F03 are covered by SCI's ADV-239 wording in candidate CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01, not here.

## 3. Files

`apply_adv244_wording_it_20261125.py` (first increment) and `apply_adv244b_it_20261125.py` (batch limit; E01, E03, F01); both idempotent, marker "[IT 2026-11-25, ADV-244".
